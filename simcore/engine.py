from __future__ import annotations

import csv
import copy
import hashlib
import heapq
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Callable


class SimulationError(ValueError):
    pass


@dataclass
class ActorDecision:
    decision: str
    channel: str = "none"
    target_ids: list[str] = field(default_factory=list)
    action_text: str = ""
    knowledge_source_ids: list[str] = field(default_factory=list)
    task_update: str = ""
    visibility: str = "public"
    dais_knows: bool = True
    data: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def parse(cls, raw: dict[str, Any]) -> "ActorDecision":
        value = cls(**raw)
        if value.decision not in {"act", "wait", "continue_drafting", "abandon_task"}:
            raise SimulationError(f"invalid actor decision: {value.decision}")
        if value.decision == "act" and value.channel == "none":
            raise SimulationError("an action needs a channel")
        if value.decision != "act" and value.channel != "none":
            raise SimulationError("non-actions must use channel=none")
        if value.visibility not in {"public", "private"}:
            raise SimulationError(f"invalid visibility: {value.visibility}")
        return value


@dataclass
class Event:
    event_id: str
    at: int
    actor_id: str
    channel: str
    text: str
    target_ids: list[str] = field(default_factory=list)
    visibility: str = "public"
    dais_knows: bool = True
    knowledge_source_ids: list[str] = field(default_factory=list)
    causal_parent_ids: list[str] = field(default_factory=list)
    data: dict[str, Any] = field(default_factory=dict)


@dataclass
class Card:
    card_id: str
    title: str
    trigger_type: str
    trigger: dict[str, Any]
    text: str
    recipients: list[str] = field(default_factory=list)
    status: str = "candidate"
    eligible_at: int | None = None
    fired_at: int | None = None
    withheld_reason: str = ""
    fingerprint: str = ""

    def _fingerprint(self) -> str:
        if self.trigger_type not in {"clock", "state", "consequence", "failure_to_act", "reserve"}:
            raise SimulationError(f"invalid trigger type: {self.trigger_type}")
        raw = json.dumps(
            {"id": self.card_id, "type": self.trigger_type, "trigger": self.trigger},
            sort_keys=True,
            separators=(",", ":"),
        )
        return hashlib.sha256(raw.encode()).hexdigest()

    def freeze(self) -> None:
        self.fingerprint = self._fingerprint()

    def verify_frozen(self) -> None:
        if self._fingerprint() != self.fingerprint:
            raise SimulationError(f"card trigger changed after freeze: {self.card_id}")


@dataclass
class Problem:
    problem_id: str
    live: bool = True
    last_development_at: int = 0
    unresolved: list[str] = field(default_factory=list)


ActorRunner = Callable[[str, dict[str, Any]], dict[str, Any]]
Resolver = Callable[[Event, dict[str, Any]], list[dict[str, Any]]]


class Engine:
    """Small deterministic event loop. It contains no Disney story logic."""

    def __init__(self, seed: int):
        self.seed = seed
        self.now = 0
        self._sequence = 0
        self._next_event = 1
        self._next_invocation = 1
        self._scheduled: list[tuple[int, int, str, dict[str, Any]]] = []
        self.events: list[Event] = []
        self.invocations: list[dict[str, Any]] = []
        self.facts: dict[str, dict[str, Any]] = {}
        self.values: dict[str, Any] = {}
        self.value_access: dict[str, dict[str, Any]] = {}
        self.cards: dict[str, Card] = {}
        self.problems: dict[str, Problem] = {}
        self.tasks: dict[str, str] = {}
        self.directive_queue: list[str] = []
        self.directive_status: dict[str, str] = {}

    # ---------- deterministic time ----------

    def schedule_actor(self, actor_id: str, at: int) -> None:
        if at < self.now:
            raise SimulationError("cannot schedule in the past")
        self._sequence += 1
        heapq.heappush(self._scheduled, (at, self._sequence, "actor", {"actor_id": actor_id}))

    def next_scheduled(self) -> tuple[int, str, dict[str, Any]] | None:
        if not self._scheduled:
            return None
        at, _, kind, payload = self._scheduled[0]
        return at, kind, dict(payload)

    def advance_to(self, at: int) -> list[str]:
        if at < self.now:
            raise SimulationError("cannot move time backward")
        if self._scheduled and self._scheduled[0][0] < at:
            raise SimulationError("cannot skip a scheduled item")
        self.now = at
        return self.evaluate_cards()

    def deterministic_int(self, label: str, low: int, high: int) -> int:
        if low > high:
            raise SimulationError("low must not exceed high")
        digest = hashlib.sha256(f"{self.seed}|{label}".encode()).digest()
        return low + int.from_bytes(digest[:8], "big") % (high - low + 1)

    # ---------- information ----------

    def add_fact(self, fact_id: str, text: str, *, holders: list[str] | None = None, public: bool = False) -> None:
        if fact_id in self.facts:
            raise SimulationError(f"duplicate fact: {fact_id}")
        self.facts[fact_id] = {"text": text, "holders": sorted(set(holders or [])), "public": public}

    def transfer_fact(self, fact_id: str, actor_id: str) -> None:
        fact = self.facts[fact_id]
        fact["holders"] = sorted(set(fact["holders"]) | {actor_id})

    def can_access(self, actor_id: str, fact_id: str) -> bool:
        fact = self.facts.get(fact_id)
        return bool(fact and (fact["public"] or actor_id in fact["holders"]))

    def set_value(self, key: str, value: Any, *, public: bool = False, holders: list[str] | None = None) -> None:
        self.values[key] = value
        self.value_access[key] = {"public": public, "holders": sorted(set(holders or []))}

    def actor_packet(self, actor_id: str) -> dict[str, Any]:
        facts = {
            fid: fact["text"]
            for fid, fact in self.facts.items()
            if fact["public"] or actor_id in fact["holders"]
        }
        visible = [
            asdict(event)
            for event in self.events[-12:]
            if event.visibility == "public" or actor_id == event.actor_id or actor_id in event.target_ids
        ]
        return {
            "actor_id": actor_id,
            "now": self.now,
            "facts": facts,
            "recent_visible_events": visible,
            "task": self.tasks.get(actor_id, ""),
            "visible_values": {
                key: value
                for key, value in self.values.items()
                if self.value_access.get(key, {}).get("public")
                or actor_id in self.value_access.get(key, {}).get("holders", [])
            },
        }

    def chair_view(self) -> list[Event]:
        return [event for event in self.events if event.visibility == "public" or event.dais_knows]

    # ---------- actors and resolver ----------

    def step(self, actor_runner: ActorRunner, resolver: Resolver | None = None) -> Event | None:
        if not self._scheduled:
            return None
        at, _, kind, payload = heapq.heappop(self._scheduled)
        self.now = at
        if kind != "actor":
            raise SimulationError(f"unsupported scheduled kind: {kind}")

        actor_id = payload["actor_id"]
        packet = self.actor_packet(actor_id)
        raw_decision = actor_runner(actor_id, packet)
        invocation = {
            "invocation_id": f"I{self._next_invocation:05d}",
            "at": self.now,
            "actor_id": actor_id,
            "packet": packet,
            "response": raw_decision,
            "packet_hash": self._hash_json(packet),
            "response_hash": self._hash_json(raw_decision),
            "schema_status": "pass",
        }
        self._next_invocation += 1
        self.invocations.append(invocation)
        try:
            decision = ActorDecision.parse(raw_decision)
        except (SimulationError, TypeError) as error:
            invocation["schema_status"] = f"fail: {error}"
            raise
        attempt = self._apply_decision(actor_id, decision)
        if attempt and resolver:
            for outcome in resolver(attempt, self.resolver_state()):
                self._apply_outcome(attempt, outcome)
        self.evaluate_cards()
        return attempt

    def _apply_decision(self, actor_id: str, decision: ActorDecision) -> Event | None:
        inaccessible = [fid for fid in decision.knowledge_source_ids if not self.can_access(actor_id, fid)]
        if inaccessible:
            raise SimulationError(f"{actor_id} cannot access: {', '.join(inaccessible)}")

        if decision.task_update:
            self.tasks[actor_id] = decision.task_update
        if decision.decision != "act":
            return None

        if decision.channel == "directive" and (decision.visibility != "public" or not decision.dais_knows):
            raise SimulationError("a formal directive must be public and visible to the dais")

        event = self._append_event(
            actor_id=actor_id,
            channel=decision.channel,
            text=decision.action_text,
            target_ids=decision.target_ids,
            visibility=decision.visibility,
            dais_knows=decision.dais_knows,
            knowledge_source_ids=decision.knowledge_source_ids,
            data=decision.data,
        )
        if decision.channel == "directive":
            self.directive_queue.append(event.event_id)
            self.directive_status[event.event_id] = "submitted"
        self._touch_problems(event)
        return event

    def resolver_state(self) -> dict[str, Any]:
        return {
            "now": self.now,
            "values": dict(self.values),
            "live_problems": {pid: asdict(problem) for pid, problem in self.problems.items() if problem.live},
            "directive_queue": list(self.directive_queue),
        }

    def _apply_outcome(self, attempt: Event, raw: dict[str, Any]) -> Event:
        parents = list(raw.get("causal_parent_ids") or [attempt.event_id])
        self._require_existing_parents(parents)
        effects = raw.get("axis_effects", [])
        for effect in effects:
            evidence = effect.get("evidence_event_ids", [])
            if not evidence:
                raise SimulationError("axis effects require evidence_event_ids")
            self._require_existing_parents(evidence)
        event = self._append_event(
            actor_id=raw.get("actor_id", "WORLD"),
            channel=raw.get("channel", "outcome"),
            text=raw.get("text", ""),
            target_ids=list(raw.get("target_ids", [])),
            visibility=raw.get("visibility", "public"),
            dais_knows=bool(raw.get("dais_knows", True)),
            causal_parent_ids=parents,
            data={"axis_effects": effects, **raw.get("data", {})},
        )
        self._touch_problems(event)
        return event

    # ---------- cards and problems ----------

    def add_problem(self, problem: Problem) -> None:
        if problem.problem_id in self.problems:
            raise SimulationError(f"duplicate problem: {problem.problem_id}")
        self.problems[problem.problem_id] = problem

    def add_card(self, card: Card) -> None:
        if card.card_id in self.cards:
            raise SimulationError(f"duplicate card: {card.card_id}")
        stored = copy.deepcopy(card)
        stored.freeze()
        self.cards[stored.card_id] = stored

    def evaluate_cards(self) -> list[str]:
        newly_eligible = []
        for card in self.cards.values():
            card.verify_frozen()
            if card.status != "candidate" or not self._trigger_true(card):
                continue
            card.status = "eligible"
            card.eligible_at = self.now
            newly_eligible.append(card.card_id)
        return newly_eligible

    def fire_card(self, card_id: str) -> Event:
        card = self.cards[card_id]
        card.verify_frozen()
        if card.status != "eligible":
            raise SimulationError(f"card is not eligible: {card_id}")
        parents = list(card.trigger.get("parent_event_ids", []))
        self._require_existing_parents(parents)
        card.status = "fired"
        card.fired_at = self.now
        event = self._append_event(
            actor_id="WORLD",
            channel="crisis_card",
            text=card.text,
            target_ids=card.recipients,
            visibility="public" if not card.recipients else "private",
            dais_knows=not bool(card.recipients),
            causal_parent_ids=parents,
            data={"card_id": card.card_id, "card_fingerprint": card.fingerprint},
        )
        self._touch_problems(event)
        return event

    def withhold_card(self, card_id: str, reason: str) -> None:
        card = self.cards[card_id]
        if card.status != "eligible":
            raise SimulationError(f"card is not eligible: {card_id}")
        card.status = "withheld"
        card.withheld_reason = reason

    def _trigger_true(self, card: Card) -> bool:
        trigger = card.trigger
        if card.trigger_type == "clock":
            return self.now >= int(trigger["at"])
        if card.trigger_type == "state":
            return self._compare(self.values.get(trigger["key"]), trigger["op"], trigger.get("value"))
        if card.trigger_type == "consequence":
            required = set(trigger.get("parent_event_ids", []))
            return bool(required) and required.issubset({event.event_id for event in self.events})
        if card.trigger_type == "failure_to_act":
            problem = self.problems[trigger["problem_id"]]
            return problem.live and self.now - problem.last_development_at >= int(trigger["quiet_seconds"])
        if card.trigger_type == "reserve":
            quiet = int(trigger.get("quiet_seconds", 600))
            last = max((problem.last_development_at for problem in self.problems.values()), default=0)
            return not any(problem.live for problem in self.problems.values()) and self.now - last >= quiet
        return False

    @staticmethod
    def _compare(left: Any, op: str, right: Any) -> bool:
        operations = {
            "eq": lambda: left == right,
            "ne": lambda: left != right,
            "gt": lambda: left is not None and left > right,
            "gte": lambda: left is not None and left >= right,
            "lt": lambda: left is not None and left < right,
            "lte": lambda: left is not None and left <= right,
        }
        if op not in operations:
            raise SimulationError(f"invalid state operator: {op}")
        return operations[op]()

    def _touch_problems(self, event: Event) -> None:
        for problem_id in event.data.get("problem_ids", []):
            if problem_id in self.problems:
                self.problems[problem_id].last_development_at = event.at

    # ---------- directive queue ----------

    def take_next_directive(self) -> Event | None:
        if not self.directive_queue:
            return None
        event_id = self.directive_queue.pop(0)
        self.directive_status[event_id] = "in_review"
        return self.event(event_id)

    def rule_directive(self, directive_event_id: str, status: str, text: str) -> Event:
        if self.directive_status.get(directive_event_id) != "in_review":
            raise SimulationError("directive must be in review")
        if status not in {"revision_requested", "approved", "rejected"}:
            raise SimulationError(f"invalid directive status: {status}")
        self.directive_status[directive_event_id] = status
        return self._append_event(
            actor_id="DAIS",
            channel="directive_ruling",
            text=text,
            causal_parent_ids=[directive_event_id],
        )

    # ---------- state and output ----------

    def _append_event(self, **values: Any) -> Event:
        event = Event(event_id=f"E{self._next_event:05d}", at=self.now, **values)
        self._next_event += 1
        self.events.append(event)
        return event

    def event(self, event_id: str) -> Event:
        for event in self.events:
            if event.event_id == event_id:
                return event
        raise SimulationError(f"missing event: {event_id}")

    def _require_existing_parents(self, event_ids: list[str]) -> None:
        known = {event.event_id for event in self.events}
        missing = [event_id for event_id in event_ids if event_id not in known]
        if missing:
            raise SimulationError(f"missing causal parents: {', '.join(missing)}")

    def to_dict(self) -> dict[str, Any]:
        scheduled = [
            {"at": at, "sequence": sequence, "kind": kind, "payload": payload}
            for at, sequence, kind, payload in sorted(self._scheduled)
        ]
        return {
            "seed": self.seed,
            "now": self.now,
            "sequence": self._sequence,
            "next_event": self._next_event,
            "next_invocation": self._next_invocation,
            "scheduled": scheduled,
            "events": [asdict(event) for event in self.events],
            "invocations": self.invocations,
            "facts": self.facts,
            "values": self.values,
            "value_access": self.value_access,
            "cards": {key: asdict(value) for key, value in self.cards.items()},
            "problems": {key: asdict(value) for key, value in self.problems.items()},
            "tasks": self.tasks,
            "directive_queue": self.directive_queue,
            "directive_status": self.directive_status,
        }

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Engine":
        engine = cls(seed=raw["seed"])
        engine.now = raw["now"]
        engine._sequence = raw["sequence"]
        engine._next_event = raw["next_event"]
        engine._next_invocation = raw.get("next_invocation", 1)
        engine._scheduled = [
            (item["at"], item["sequence"], item["kind"], item["payload"])
            for item in raw["scheduled"]
        ]
        heapq.heapify(engine._scheduled)
        engine.events = [Event(**event) for event in raw["events"]]
        engine.invocations = raw.get("invocations", [])
        engine.facts = raw["facts"]
        engine.values = raw["values"]
        engine.value_access = raw.get("value_access", {})
        engine.cards = {key: Card(**value) for key, value in raw["cards"].items()}
        engine.problems = {key: Problem(**value) for key, value in raw["problems"].items()}
        engine.tasks = raw["tasks"]
        engine.directive_queue = raw["directive_queue"]
        engine.directive_status = raw["directive_status"]
        return engine

    def save(self, path: str | Path) -> None:
        Path(path).write_text(json.dumps(self.to_dict(), indent=2, sort_keys=True), encoding="utf-8")

    @classmethod
    def load(cls, path: str | Path) -> "Engine":
        return cls.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))

    def write_outputs(self, directory: str | Path) -> None:
        output = Path(directory)
        output.mkdir(parents=True, exist_ok=True)
        self._write_events(output / "master_timeline.csv", self.events)
        self._write_events(output / "chair_view.csv", self.chair_view())
        with (output / "actor_invocations.jsonl").open("w", encoding="utf-8") as handle:
            for invocation in self.invocations:
                handle.write(json.dumps(invocation, sort_keys=True) + "\n")
        with (output / "card_ledger.csv").open("w", newline="", encoding="utf-8") as handle:
            fields = ["card_id", "title", "trigger_type", "status", "eligible_at", "fired_at", "withheld_reason", "fingerprint"]
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            for card in self.cards.values():
                writer.writerow({field: getattr(card, field) for field in fields})

    @staticmethod
    def _hash_json(value: Any) -> str:
        raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        return hashlib.sha256(raw.encode()).hexdigest()

    @staticmethod
    def _write_events(path: Path, events: list[Event]) -> None:
        fields = ["event_id", "at", "actor_id", "channel", "text", "target_ids", "visibility", "dais_knows", "knowledge_source_ids", "causal_parent_ids", "data"]
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            for event in events:
                row = asdict(event)
                for field_name in ("target_ids", "knowledge_source_ids", "causal_parent_ids", "data"):
                    row[field_name] = json.dumps(row[field_name], sort_keys=True)
                writer.writerow(row)
