# Codex Runbook v2 — Simulating the First Two Disney Committee Sessions

**Scope:** 240 active committee minutes, representing roughly four months of Disney-world time  
**Sessions:** M3 — The Blackout, followed by M1 — The Empty Vault  
**Room:** six delegate-held offices and three dais-held pressure characters  
**Cohort:** medium-level SMA delegates who can learn but do not begin as executives  
**Purpose:** reveal structural tendencies in the committee design, not predict particular students

---

# 1. The decision

Do not ask one Codex conversation to role-play nine people and write a four-hour screenplay. Build a continuous-time simulation engine and use Codex only for bounded human decisions inside it.

The engine owns time, causality, knowledge access, resources, queues, and world consequences. Every character decision is produced through a fresh isolated Codex invocation that receives only that character's identity kernel, synthetic student profile, current private state, and exact observations. The invocation may act, wait, or continue unfinished work. It does not see the master transcript or the other private files.

This combines the strongest parts of the earlier design and the later anti-collapse critique:

- continuous rather than round-robin time;
- isolated role generation rather than nine voices in one context;
- structured memory rather than transcript memory;
- deterministic scheduling before prose generation;
- an omniscient world director separated from a limited-information dais;
- a clean baseline separated from deliberately difficult stress runs;
- an observer record for analysis and a chair-view replay for felt workload.

The simulation is successful if it tells Rizky where roles die, crises run out, private politics fail to reach directives, the dais becomes overloaded, or the mechanics teach the wrong lesson. Entertainment is secondary.

---

# 2. What changed from v1

The first runbook treated isolated permanent characters as a poor fit because they constantly affect one another. That was only half right. They should not communicate through shared agent context, but they should be invoked separately and receive exact messages through the engine. Isolation protects role differences; the engine preserves interaction.

The second change is experimental. Silence, domination, poor directives, misunderstanding, and running out of material must not be compulsory baseline outcomes. If the simulator is ordered to produce them, it cannot reveal whether the committee naturally produces them. Those pressures belong in a registered stress condition.

The third change separates a Disney office from the teenager playing it. The real room is not nine executives. It is nine students attempting nine offices. Every simulated participant therefore has a stable **role layer** and a separately assigned **player layer**.

The fourth change rejects invented mechanics. There are no action cards, expiring grants, or automatic penalties for broken promises unless they are later adopted into the 4.0 canon. Love, Money, and Control remain the three public lenses. Patience and Peace are faces of Control, not two extra global dials.

The fifth change treats fixed six-minute beats as computation windows only. Social events occur at continuous timestamps. A window may contain a burst, parallel drafting, or silence.

---

# 3. What this simulation can and cannot answer

It can test whether the crisis deck has enough material, whether offices possess usable leverage, whether private traffic becomes operational, whether directives improve, whether the dais queue is survivable, and whether Session 1 meaningfully changes Session 2.

It cannot forecast the students, reproduce embodied room energy, or establish that Codex or Claude simulates people accurately. A polished betrayal is not evidence that a real betrayal will happen. A quiet role may indicate a weak office design, a quiet synthetic player, a scheduling defect, or model failure. The experiment must distinguish these explanations.

Seconds-level timestamps are scheduled committee time. They are not the wall-clock time spent by Codex and they are not predictions of the actual event to the second.

---

# 4. Architecture

Use five components with hard boundaries.

| Component | Knows | Decides |
|---|---|---|
| Scheduler | public engine state plus numeric readiness variables | who becomes eligible to act and when |
| Actor invocation | one role packet only | whether that participant acts, waits, or continues work |
| World resolver | omniscient state and submitted interventions | implementation, resistance, delay, consequence, and mini-crises |
| Simulated dais | public floor, submitted directives, and dais-only messages | procedure, revision requests, rulings, and update release |
| Recorder | all event streams | durable logs, derived views, audits, and replay |

The world resolver is not the dais. It may know every secret and causal variable. The dais may use only what the real cochairs could know.

The actor model does not schedule itself. The scheduler determines when an actor becomes eligible; only then does Codex receive the actor packet. This prevents eloquent prose from manufacturing convenient initiative.

The model should not resolve its own action. Every directive is an attempted intervention, not a spell. Authority, capability, and legitimacy remain different.

---

# 5. Common experiment contract

Codex and Claude Code must consume the same contract. Only the actor-rendering command changes between platforms.

Freeze these before a registered run:

- crisis files and opening information;
- role identity kernels;
- synthetic student profiles and role assignment;
- initial resources, authority, and knowledge;
- scheduler algorithm and engine seed;
- action schema;
- adjudication rules;
- time conversion;
- output schemas and validators;
- experiment condition: baseline or named stress condition.

Do not edit a registered run after seeing its first events. If Rizky intervenes, label it an exploratory run and record the intervention as an event. A clean baseline contains no human steering.

An engine seed makes scheduling, service times, and rule-based uncertainty reproducible. It does not guarantee identical language-model output. Record the platform, model, settings, prompt hash, response hash, and timestamp for every invocation.

---

# 6. The nine roles

The first run uses:

1. Josh D'Amaro — CEO
2. Dana Walden — President and Chief Creative Officer
3. Hugh Johnston — CFO
4. Horacio Gutierrez — Chief Legal and Global Affairs Officer
5. James Gorman — Board Chair
6. Mara Voss — activist investor, composite character
7. Evelyn Ward — regulator, dais-held composite character
8. Avery Cole — marquee talent, dais-held composite character
9. Jordan Lee — distributor/platform executive, dais-held composite character

Robert Iger and the additional roster may appear as event-driven NPCs. They do not become continuous participants unless activated in authoritative state.

The three dais-held pressure characters respond and apply pressure. They do not author the delegates' solution. A cochair never adjudicates the action of a standing character they themselves are portraying.

---

# 7. Role layer and player layer

## 7.1 Identity kernel

Do not inject the full dossier on every call. Compile it into six durable fields:

- office mandate;
- private objective;
- central contradiction;
- feared failure;
- protected secret or vulnerability;
- habitual tempo and decision style.

The full dossier remains source material. The kernel is the behavioral operating system. It should be short enough that no attribute can hide inside decorative biography.

## 7.2 Synthetic student profile

Assign each participant a separate five-field player profile on a 1–5 scale:

- business literacy;
- verbal confidence;
- strategic reasoning;
- writing speed;
- social risk tolerance.

All are medium-level in aggregate, but not identical. A student may speak quickly and reason poorly, understand the business but draft slowly, or spot leverage while fearing public conflict.

Use the same player profiles and the same role assignment in the Codex and Claude baselines. Later, rotate the profiles between roles. This distinguishes a structurally weak seat from a quiet simulated player.

## 7.3 Living private state

Each actor also carries changing state:

- known facts with source event IDs;
- beliefs and uncertainties;
- trust, access, reliability, and legitimacy toward others;
- promises, grievances, and dependencies;
- available and committed resources;
- current task and drafting progress;
- fatigue, cognitive load, and confidence;
- locally learned procedural or business lessons;
- earliest next eligible time.

Reinject the identity kernel on every invocation, but never reset living state. Identity must remain stable while the participant learns.

## 7.4 What distinctness means

Shared vocabulary is not necessarily collapse. Real participants learn common terms. Evaluate whether roles preserve different motives, choices, timing, information use, and willingness to bear costs. Do not force accents, catchphrases, or theatrical eccentricity merely to make voices classifiable.

---

# 8. Time and pace

Use three clocks.

| Field | Meaning |
|---|---|
| `committee_elapsed` | active committee time from `00:00:00` to `04:00:00` |
| `session_elapsed` | active time within the current session from `00:00:00` to `02:00:00` |
| `world_datetime` | Disney-world date; one committee hour advances one calendar month |

World anchors:

- `00:00:00` = 5 September 2026
- `01:00:00` = 5 October 2026
- `02:00:00` = 5 November 2026
- `03:00:00` = 5 December 2026
- `04:00:00` = 5 January 2027

Interpolate within each month. The active clock pauses during lunch, coffee, and overnight breaks unless an explicit off-session event is enabled.

## 8.1 Scheduler

There is no turn order. Each actor has a base tempo, initiative, cognitive load, fatigue, current relevance, direct requests, deadlines, threats, unread messages, and unfinished work. The scheduler uses these numbers to assign an earliest eligible time with seeded jitter.

The exact formula may be simple:

```text
pressure = relevance + direct_request + threat + deadline + motive
           - cognitive_load - fatigue

delay = clamp(base_delay / exp(pressure_factor), 30, 1500)
        + seeded_jitter
```

The formula chooses **when to ask**, not what the person does. On invocation, the person may still wait.

After an event, recalculate only actors who observed it or whose task, deadline, resource, or relationship changed. Never wake all nine merely because a crisis update arrived.

## 8.2 Parallel activity

The engine must allow overlapping work. While one participant speaks, another may draft, wait for a note, meet privately, or become unavailable. Drafting consumes time. Private meetings occupy their participants. Paper has delivery latency. Dais staff can process only a limited number of directives at once.

Thirty-minute blocks are checkpoint windows, not social turns. Later blocks read authoritative state, not transcript summaries.

---

# 9. Isolated actor invocations

Every actor call starts fresh. Do not resume an actor conversation across the run. Continuity comes from the structured role packet, not chat history.

The packet contains only:

1. the six-field identity kernel;
2. the five-field player profile;
3. current private state;
4. exact observed events and received notes, identified by event ID;
5. current task and time pressure;
6. the allowed action schema.

It excludes the master timeline, other roles' private state, world secrets, future crisis cards, and observer interpretation.

Use an invocation directory containing only the packet and schema. Run without network and without write access outside the invocation directory. For stronger enforcement, use a disposable container or permission profile whose readable files are limited to that packet. Prompt discipline alone is not a knowledge firewall.

Explicitly name the actor by stable ID on every call. Do not depend on automatic routing from a role description.

A Codex CLI pattern is:

```bash
codex exec --ephemeral \
  --sandbox read-only \
  --output-schema actor_action.schema.json \
  --output-last-message actor_return.json \
  - < actor_prompt.md
```

The orchestration script validates the return before merging anything into state. It stores the raw prompt and response separately from the social transcript.

## 9.1 Allowed actor outcomes

An actor may:

- `act` through floor speech, paper note, private meeting request, resource commitment, directive submission, or deliberate leak;
- `wait` because the person lacks motive, information, confidence, access, or readiness;
- `continue_drafting` without producing a visible event;
- `abandon_task` after delay, contradiction, or changed priorities.

Silence is not a narrated action. It appears as elapsed time and unfinished state.

## 9.2 Actor output schema

```json
{
  "actor_id": "HUGH",
  "decision": "act | wait | continue_drafting | abandon_task",
  "channel": "floor | paper_note | private_meeting | directive | resource_use | leak | none",
  "target_ids": [],
  "action_text": "",
  "reasoning_tags": [],
  "knowledge_source_ids": [],
  "resources_attempted": [],
  "love_priority": 0,
  "money_priority": 0,
  "control_priority": 0,
  "task_state_update": "",
  "requested_next_delay_seconds": 180
}
```

The three priority fields describe intent, not automatic dial movement. A strong synthesis may improve all three; a foolish intervention may damage all three. The resolver determines consequences from authority, capability, legitimacy, timing, resources, resistance, and implementation.

---

# 10. Memory and information firewall

The orchestrator should never reread the full transcript. It reads structured state and the minimum relevant event window.

For each actor invocation, retrieve:

- the last two relevant local interactions;
- unresolved promises and grievances;
- active beliefs and uncertainties;
- current relationships and resources;
- pending directives or drafting work;
- older events explicitly linked to the present situation.

An old promise may matter more than the last two messages. Relevance retrieval therefore uses IDs and state links, not recency alone.

Every fact has a provenance record:

```text
knowledge_id
fact
source_event_id
knowers
confidence
quotable
public
```

Every actor action must cite the knowledge IDs that materially support it. The validator rejects inaccessible sources.

Paper notes default to `dais_knows=false`. They affect the world only by changing later behavior, a submitted directive, a resource commitment, or an explicit leak. The observer may see them. The dais may not.

The engine maintains three derived views:

- `omniscient_view`: all events and causal state;
- `chair_view`: only public, submitted, and dais-only material available at that time;
- `actor_view/<actor_id>`: exactly what that participant knew at that time.

---

# 11. Resources and the three dials

Resources are capabilities, permissions, relationships, attention, time, cash, data, reputation, and contractual leverage. They are not a universal card currency.

Track only resources that can change a decision. Every role should normally have two to four concrete resources, each with:

- owner;
- authority to commit;
- current capacity;
- restrictions;
- commitment state;
- replenishment or exhaustion rule;
- visibility.

Keep office resources separate from personal leverage and public institutional resources. A person may control an office budget without owning it, possess personal access without formal authority, or enjoy legitimacy without operational capacity.

Love, Money, and Control are public interpretive dials. They move only after observable evidence. Patience and Peace may appear as descriptions of Control: Patience is willingness to tolerate delayed payoff; Peace is stability among actors and stakeholders. Do not expose them as two additional global scores.

Every major intervention receives an immediate receipt and, when appropriate, a delayed invoice. Neither must be negative. The purpose is to make time, dependency, and implementation visible.

---

# 12. World resolution and mini-crises

Prefer rules and bounded seeded uncertainty over a free-form LLM narrator. The resolver evaluates:

- whether the actor has authority;
- whether required capability and partners exist;
- whether implementation is specified;
- timing and queue delay;
- counterparty incentives and resistance;
- Love, Money, and Control exposure;
- prior promises, fatigue, and credibility;
- a seeded uncertainty term inside a declared range.

Possible outcomes include success, partial success, delay, refusal, leak, misinterpretation, backlash, implementation failure, or a new dependency.

Most mini-crises should arise from unresolved dependencies, accumulated commitments, external clocks, or earlier interventions. A smaller reserve may be exogenous. Every mini-crisis declares its trigger, teaching purpose, affected resources, recipients, and earliest/latest eligible time.

The resolver never inserts a crisis merely because the transcript feels quiet. Silence is data. If a stress condition authorizes outside pressure, that authorization is recorded before the run.

---

# 13. Simulated dais and physical throughput

The room has three cochairs with limited service capacity:

- Chair/Rizky: final judgment, pacing, and terminal arc;
- Dais 2: state and causality, including resources, commitments, and delayed invoices;
- Dais 3: information and voice, including news, NPCs, public display, and note delivery.

Model the operational queue. Every directive passes through:

1. paper submission;
2. transport delay;
3. OCR draft where enabled;
4. human confirmation;
5. assignment to a cochair;
6. adjudication or revision request;
7. implementation scheduling;
8. public or private return.

The simulated dais may become overloaded. It may not use private notes to compensate. Queue delay is part of the committee design, not noise to edit away.

Use a simple room layout only to model access and paper latency. Do not build unnecessary spatial physics. It is enough to know who can confer privately, who is occupied, and how long paper takes to travel.

---

# 14. First two sessions

## Session 1 — M3: The Blackout

A major distributor removes ESPN, ABC, and Disney entertainment channels during a high-value sports and advertising window. The distributor demands lower fees, in-product ESPN access, and customer-data custody. Disney's direct product cannot absorb all affected households.

The session should expose bargaining power, credible alternatives, channel conflict, customer ownership, implementation, and delayed consequences.

Opening information is partitioned:

- Jordan knows that the distributor's internal tolerance is weaker than its public line.
- Hugh knows rebate and cash exposure.
- an NPC technology resource knows migration capacity is inadequate;
- an NPC sports resource knows a league reach obligation may become material;
- Dana sees content and talent consequences;
- Mara sees a governance and portfolio vulnerability.

Do not prescribe the arc. Valid possibilities include settlement, escalation, a partial bridge, an attempted direct migration, a coalition split, or strategic delay. Each must obey capability and contractual limits.

## Session 2 — M1: The Empty Vault

Disney can fully support only two of three portfolios: proven franchises, original owned worlds, or creator-led interactive experiments. A leaked audience study suggests adult nostalgia still converts while under-twelve attachment to new Disney characters is weakening. One weak original contains a character that performs strongly when tested separately.

The session should expose portfolio choice, opportunity cost, sunk cost, staged investment, stop rules, and value before monetization.

Session 2 inherits the exact credibility, trust, resources, promises, fatigue, learning, and unresolved consequences from Session 1. Do not reset coalitions or competence.

---

# 15. Experiment conditions

## 15.1 Registered baseline

The baseline contains no compulsory betrayal, dominant speaker, quiet delegate, dead air, unclear directive, misunderstanding, or material shortage. These outcomes are allowed but not demanded. There is no human steering and no invented action-card economy.

## 15.2 Registered stress run

The stress run changes only predeclared player or operating conditions. A useful first stress condition is:

- one low-confidence but strategically strong player;
- one high-confidence but low-business-literacy player;
- slower paper delivery;
- one OCR correction delay;
- higher early uncertainty about directive format.

Do not mandate the social result. The condition may produce domination or silence; it need not.

## 15.3 Exploratory run

Rizky may pause, inject, or alter the room. Record each intervention and do not compare the result statistically with registered runs.

## 15.4 Cross-platform minimum

Run two baseline engine seeds and one identical stress seed on Codex and Claude Code. One run on each platform yields two stories, not a comparison. If cost permits only one run each, treat the result as workflow testing.

Blind the platform label before qualitative scoring.

---

# 16. Output files

Produce these primary artifacts.

## `outputs/master_timeline.csv`

The omniscient event record. Required columns:

```text
run_id
event_id
session_no
committee_elapsed
committee_elapsed_seconds
session_elapsed
world_datetime
actor_id
target_ids
channel
visibility
dais_knows
event_text
source_event_ids
knowledge_source_ids
causal_parent_ids
directive_id
causal_importance
love_delta
money_delta
control_delta
resource_changes
relationship_changes
promise_changes
invocation_id
```

## `outputs/directive_ledger.csv`

Only submissions, revision requests, confirmed text, rulings, implementation updates, and visible consequences.

## `outputs/chair_view.csv`

The timed view available to the Chair. It excludes private notes, private meetings, hidden motives, observer interpretation, and unrevealed causes.

## `outputs/dais_queue.csv`

```text
directive_id
submitted_at
paper_received_at
ocr_completed_at
human_confirmed_at
assigned_cochair
adjudication_started_at
decision_at
returned_at
status
revision_count
ocr_corrections
```

## `outputs/state_snapshots.csv`

One snapshot every fifteen committee minutes and at session boundaries. Include resources, dials, active deadlines, public commitments, coalitions, unresolved directives, queue length, and delayed invoices.

## `outputs/checkpoints/block_01.json` through `block_08.json`

Complete authoritative state after each thirty-minute checkpoint window.

## `outputs/invocations.jsonl`

One record per actor call: actor ID, eligible time, prompt hash, response hash, model, platform, schema result, token usage where available, and merge status. Store raw prompt and response files under `outputs/invocations/` but do not place private prompt contents in the chair view.

## `outputs/run_manifest.json`

The frozen contract: source hashes, engine version, condition, engine seed, player-role assignment, platform, model, settings, start time, and validator version.

## `outputs/simulation_report.md`

Explain causal development, pace, alliances, learning, business principles experienced, dais workload, capture gap, convincing moments, artificial moments, and design changes supported by evidence.

## `outputs/chair_replay.jsonl`

Timed chair-visible events for accelerated playback. The replay must not contain future or hidden knowledge.

---

# 17. What counts as an event

Log an event when something becomes observable to another actor, consumes or changes a resource, transfers knowledge, creates or breaks a promise, changes directive state, occupies a shared channel, or changes the world.

Do not log thoughts as room traffic. Internal belief updates remain in private state. Do not invent chatter merely to keep the CSV busy.

An alliance requires repeated cooperation, exchanged risk, or a credible promise. A betrayal requires a prior expectation. Opposition without prior trust is not betrayal.

Tag `causal_importance` as `low`, `medium`, or `high` when the event is resolved, not when it is first generated. This permits a meaningful comparison between total traffic and what the dais could see.

---

# 18. Evaluation

The simulation should measure failure rather than merely describe it.

| Question | Measure |
|---|---|
| Did one participant dominate? | share of floor events, speaking time, and initiative Gini |
| Did pace feel lumpy? | response-latency variance, silence lengths, overlapping tasks |
| Did roles remain distinct? | blinded role identification from decisions and costs, not writing style |
| Did shared context cause collapse? | pairwise similarity of policy choices and reasoning tags over time |
| Did information leak? | inaccessible knowledge-source count; any confirmed leak is a failed run |
| Did private politics matter? | high-importance private events later represented in public conduct or directives |
| Did directive-only capture miss the room? | high-importance events absent from chair view and directive chain |
| Could the dais keep up? | median and 90th-percentile directive turnaround; maximum queue length |
| Did delegates learn? | implementation completeness, revision count, and repeat-error rate over time |
| Did the crisis deck last? | unused events, improvised events, content burn rate, quiet intervals |
| Did Session 1 matter? | inherited resources, credibility, relationships, and decisions used in Session 2 |

Do not treat lexical similarity as automatic persona collapse. The serious failure is convergence of motives, choices, pace, or information use.

Use design-review triggers rather than fake scientific cutoffs. Investigate when:

- a delegate produces no meaningful action for thirty committee minutes without a state-based reason;
- one participant supplies more than forty percent of floor activity;
- a high-importance private development never affects any dais-visible artifact;
- the 90th-percentile directive turnaround exceeds twelve committee minutes;
- the same directive defect recurs after explicit correction;
- a role cannot be identified above chance from its decisions across multiple runs;
- an unplanned mini-crisis is required to prevent the baseline from stopping.

These are prompts for diagnosis, not automatic proof that the committee is broken.

---

# 19. Validation contract

## Structural

- elapsed times parse and increase monotonically;
- committee time remains within 0–14,400 seconds;
- world time matches the monthly anchors;
- IDs are unique and all references point backward;
- directive transitions are valid;
- derived files agree with the master timeline;
- checkpoints reproduce the next block's opening state;
- every actor return validates against the schema;
- the manifest and source hashes are complete.

## Information

- every material fact used by an actor has an accessible knowledge source;
- the dais never acts on a private note without an explicit leak or operationalization event;
- actor packets contain no unauthorized file or event;
- chair replay contains no observer-only material;
- NPC knowledge is explicitly assigned.

## Causal

- every dial movement cites observable evidence;
- interventions are tested against authority, capability, and legitimacy;
- mini-crises cite a trigger or declare themselves exogenous;
- delayed invoices arise from earlier state;
- Session 2 begins from Session 1's terminal checkpoint;
- no model invocation resolves its own action.

## Behavioral audit

Behavioral checks are diagnostic, not story requirements. Report equal airtime, constant pace, instant universal reaction, perfect directives, clean endings, unearned betrayals, or stereotyped voices as suspicious. Do not repair them by inserting theatre. Repair only a demonstrated engine, state, or prompting defect; otherwise preserve the run and report the finding.

Never weaken a validator merely to pass a run.

---

# 20. Repository structure

```text
disney-room-sim/
├── AGENTS.md
├── README.md
├── context/
│   ├── Disney_4.0_Crisis_Architecture_and_Dossiers.md
│   ├── Disney_4.0_Foundation.md
│   ├── Study_Guide_Legacy.md
│   └── wiki/
├── canon/
│   ├── assumptions.md
│   ├── business_principles.yaml
│   ├── crises/
│   ├── roles/
│   ├── player_profiles/
│   └── schemas/
├── engine/
│   ├── simulate.py
│   ├── scheduler.py
│   ├── actor_runner.py
│   ├── resolver.py
│   ├── dais_queue.py
│   ├── information_firewall.py
│   ├── replay.py
│   └── validate.py
├── experiments/
│   ├── baseline.yaml
│   └── stress_01.yaml
├── outputs/
│   ├── checkpoints/
│   ├── invocations/
│   └── runs/
└── tests/
    ├── test_scheduler.py
    ├── test_information_firewall.py
    ├── test_resolver.py
    ├── test_dais_queue.py
    ├── test_replay.py
    └── test_outputs.py
```

The source documents are immutable. Record every consequential reconciliation or addition in `canon/assumptions.md`.

---

# 21. Repository `AGENTS.md`

```md
# Disney room simulation — working agreement

## Purpose

Build reproducible experiments for the first two Disney Executive Crisis Committee sessions. The objective is to expose structural room dynamics and dais workload, not predict particular students or manufacture a dramatic story.

## Canon

- Treat `context/` as immutable.
- Treat `Disney_4.0_Crisis_Architecture_and_Dossiers.md` as the current authority when legacy files conflict.
- Separate fact, institutional inference, simulation canon, and experimental condition.
- Record material assumptions in `canon/assumptions.md`.

## Non-negotiable laws

- Continuous time; no turn rotation or airtime quota.
- Schedule actors before generating their actions.
- Invoke each actor in a fresh isolated context using only its authorized packet.
- Separate office identity from synthetic student profile.
- Allow waiting, unfinished drafting, silence, mistakes, and uneven learning.
- The world director is omniscient; the simulated dais is not.
- Private paper notes remain invisible to the dais unless explicitly leaked or operationalized.
- Approval is not implementation. Authority, capability, and legitimacy differ.
- A model invocation never resolves its own intervention.
- Session 2 inherits the exact terminal state of Session 1.
- Love, Money, and Control are evidence-based public lenses. Patience and Peace remain faces of Control.
- The baseline contains no compulsory friction and no action-card economy.
- Seconds are scheduled committee time, not model execution time.

## Workflow

- Compile and audit canon before running.
- Freeze a run manifest before the first event.
- Execute eight sequential thirty-minute checkpoint windows.
- Store authoritative state, not transcript summaries.
- Validate chronology, information access, causality, queues, and derived outputs after every block.
- Do not steer a registered run.
- Never weaken a validator to make a run pass.

## Done when

- all required artifacts exist;
- all structural, information, and causal validators pass;
- chair replay contains only contemporaneously available information;
- Session 2 inherits Session 1;
- the report distinguishes engine defects, role-design findings, player-profile effects, and model artifacts.
```

---

# 22. Codex workflow

## Phase A — compile and challenge canon

Run this before simulation:

```text
Read AGENTS.md, this runbook, and context/. Do not simulate.

Compile a machine-readable canon for M3 The Blackout and M1 The Empty Vault. Produce short six-field identity kernels for the core nine, a separate pool of five-field medium-level student profiles, crisis rules, resource definitions, knowledge partitions, directive rules, and JSON schemas.

Audit every conflict between the 4.0 architecture, legacy study guide, and wiki. Preserve Love, Money, and Control. Do not introduce action cards, expiring grants, a fixed plot, compulsory friction, or additional global dials.

Create canon/, experiments/baseline.yaml, experiments/stress_01.yaml, and an implementation plan. Do not modify context/.

Done when a run can be frozen without unresolved material assumptions.
```

This is the highest-leverage human checkpoint. Rizky reviews `canon/assumptions.md`, role kernels, player profiles, crisis triggers, and resource rules before accepting the experiment.

## Phase B — build the engine without running the room

```text
Build the deterministic continuous-time engine, actor-packet builder, isolated Codex actor runner, world resolver, limited-information simulated dais, directive queue, recorder, chair replay, schemas, tests, and validators defined in the runbook.

Use fresh schema-constrained actor invocations. The actor runner must expose only the authorized packet. Store prompt and response hashes. Keep scheduling and consequence resolution outside the actor model.

Create a dry-run fixture covering ten committee minutes with one public statement, one private note, one unfinished directive, one revision request, one queue delay, and one delayed consequence. This fixture tests mechanics; it is not a behavioral sample.

Done when the fixture passes every structural, information, causal, and replay validator.
```

## Phase C — registered baseline

```text
Freeze a baseline run manifest using engine seed 40917. Do not steer the run after freezing.

Run 240 active committee minutes: Session 1 M3 The Blackout followed by Session 2 M1 The Empty Vault. Use the accepted role–player assignments. Generate eight sequential thirty-minute checkpoint windows. Validate and checkpoint after each.

Do not force betrayal, domination, silence, misunderstanding, unclear directives, material exhaustion, or a tidy ending. Do not inject a mini-crisis merely to make the transcript lively. Preserve genuine quiet and failure.

Produce every output defined in the runbook, including chair replay, dais queue, invocation audit, run manifest, and simulation report.

Done when the registered timeline is complete, validators pass, and the report preserves uncomfortable findings rather than repairing them into a story.
```

## Phase D — stress and comparison

Run the identical registered stress manifest on both platforms. Then repeat with a second baseline seed. Do not use platform-specific role prompts or crisis rules.

The cross-platform comparison should be generated from blinded outputs and should separate:

- engine invariants;
- model-dependent behavior;
- player-profile effects;
- role-design effects;
- random run variation.

---

# 23. How Rizky should experience the result

First inspect validation and the run manifest. Then watch `chair_replay.jsonl` at four times speed without pausing. A two-hour session becomes thirty minutes. Record moments of overload, boredom, uncertainty, premature intervention, and missed information. This tests the chair position rather than omniscient hindsight.

Only afterward read the master timeline. Compare the chair view with high-importance hidden traffic. Ask whether the missing information should remain legitimately private or whether the real committee needs a better capture channel.

For the real room, note volume can be measured without reading private content. Pre-numbered slips can record sender, recipient, and approximate delivery time while preserving message privacy. This reveals the network and traffic rate without turning the dais into an intelligence service.

The most useful questions are:

1. Which role was weak across different player profiles and seeds?
2. Which important social developments never reached an executable artifact?
3. When did the dais queue change the substance rather than merely delay it?
4. Which repeated mistake showed failed learning rather than simple inexperience?
5. What from Session 1 actually constrained Session 2?

---

# 24. OCR for the real committee

OCR is for official directives, not private notes. Use a preprinted directive ID or QR code, photograph the original, generate OCR text, and require human confirmation before adjudication. Preserve the image and confirmed text together.

Explicitly verify names, amounts, deadlines, and negations. Record submission, OCR completion, confirmation, assignment, ruling, revision, implementation, and consequence times. OCR should shorten transcription and routing; it should not pretend the dais understands every paper.

---

# 25. Final interpretation

The strongest result is not “this is how the students will behave.” It is:

> Under these roles, player capabilities, information rules, physical constraints, crises, and adjudication rules, this pattern repeatedly becomes possible.

If a pattern appears once, keep it as a hypothesis. If it survives model, seed, and player-profile changes, treat it as a design signal. If it disappears when only the actor model changes, treat it as a model artifact. If the real room later contradicts both simulators, the real room wins.

---

# Sources informing this runbook

OpenAI product guidance:

- [Codex best practices](https://learn.chatgpt.com/guides/best-practices)
- [Codex subagents and custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Project instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Codex non-interactive mode, JSONL, and output schemas](https://learn.chatgpt.com/docs/non-interactive-mode)
- [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk)

Research warnings used as hypotheses rather than universal laws:

- [The Chameleon's Limit: Investigating Persona Collapse and Homogenization in Large Language Models](https://arxiv.org/html/2604.24698v1)
- [BOUNDARY_SYNC: Measuring Communication-Induced Representational Coupling in Multi-Agent LLM Systems](https://arxiv.org/html/2607.01600v1)
- [Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://www.trychroma.com/research/context-rot)

The persona and coupling papers are recent preprints with task-specific limitations. In particular, the reported three-versus-five-agent result does not justify a universal rule that no more than three characters may share a room. This runbook instead limits each actor to information they plausibly observed and measures convergence directly.
