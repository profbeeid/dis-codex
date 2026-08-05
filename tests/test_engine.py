import csv
import tempfile
import unittest
from pathlib import Path

from simcore import Card, Engine, Problem, SimulationError


class EngineTests(unittest.TestCase):
    def test_actor_chooses_action_and_wait_is_silent(self):
        engine = Engine(40917)
        engine.schedule_actor("JOSH", 10)
        result = engine.step(lambda actor, packet: {"decision": "wait", "channel": "none"})
        self.assertIsNone(result)
        self.assertEqual(engine.events, [])
        self.assertEqual(engine.invocations[0]["response"]["decision"], "wait")

        engine.schedule_actor("JOSH", 20)
        result = engine.step(lambda actor, packet: {
            "decision": "act", "channel": "floor", "action_text": "Name the displaced work."
        })
        self.assertEqual(result.channel, "floor")
        self.assertEqual(result.text, "Name the displaced work.")

    def test_private_fact_and_note_stay_out_of_chair_view(self):
        engine = Engine(1)
        engine.add_fact("walkaway", "Jordan can wait.", holders=["JORDAN"])
        engine.schedule_actor("JORDAN", 5)
        engine.step(lambda actor, packet: {
            "decision": "act",
            "channel": "paper_note",
            "target_ids": ["JOSH"],
            "action_text": "We can wait longer than you think.",
            "knowledge_source_ids": ["walkaway"],
            "visibility": "private",
            "dais_knows": False,
        })
        self.assertEqual(len(engine.actor_packet("JOSH")["recent_visible_events"]), 1)
        self.assertEqual(engine.chair_view(), [])

    def test_inaccessible_knowledge_is_rejected(self):
        engine = Engine(1)
        engine.add_fact("secret", "Only Hugh knows.", holders=["HUGH"])
        engine.schedule_actor("JOSH", 5)
        with self.assertRaises(SimulationError):
            engine.step(lambda actor, packet: {
                "decision": "act", "channel": "floor", "action_text": "I know.",
                "knowledge_source_ids": ["secret"]
            })

    def test_hidden_world_values_stay_out_of_actor_packet(self):
        engine = Engine(1)
        engine.set_value("public_direction", "money down", public=True)
        engine.set_value("jordan_tolerance", 91, holders=["JORDAN"])
        self.assertEqual(engine.actor_packet("JOSH")["visible_values"], {"public_direction": "money down"})
        self.assertEqual(engine.actor_packet("JORDAN")["visible_values"]["jordan_tolerance"], 91)

    def test_card_becomes_eligible_but_does_not_auto_fire(self):
        engine = Engine(1)
        engine.add_card(Card("C1", "Deadline", "clock", {"at": 30}, "The deadline lands."))
        engine.advance_to(30)
        self.assertEqual(engine.cards["C1"].status, "eligible")
        self.assertEqual(engine.events, [])
        event = engine.fire_card("C1")
        self.assertEqual(event.data["card_id"], "C1")

    def test_frozen_card_trigger_cannot_be_changed(self):
        engine = Engine(1)
        engine.add_card(Card("C1", "Deadline", "clock", {"at": 30}, "Deadline."))
        engine.cards["C1"].trigger["at"] = 5
        with self.assertRaises(SimulationError):
            engine.evaluate_cards()

    def test_reserve_card_waits_until_no_problem_is_live(self):
        engine = Engine(1)
        engine.add_problem(Problem("capacity", live=True))
        engine.add_card(Card("R1", "Reserve", "reserve", {"quiet_seconds": 10}, "Reserve."))
        engine.schedule_actor("JOSH", 20)
        engine.step(lambda actor, packet: {"decision": "wait", "channel": "none"})
        self.assertEqual(engine.cards["R1"].status, "candidate")
        engine.problems["capacity"].live = False
        self.assertEqual(engine.evaluate_cards(), ["R1"])

    def test_directives_are_fifo_and_need_a_ruling(self):
        engine = Engine(1)
        for actor, at in (("JOSH", 10), ("DANA", 20)):
            engine.schedule_actor(actor, at)
            engine.step(lambda actor_id, packet: {
                "decision": "act", "channel": "directive", "action_text": f"Directive by {actor_id}."
            })
        first = engine.take_next_directive()
        self.assertEqual(first.actor_id, "JOSH")
        ruling = engine.rule_directive(first.event_id, "revision_requested", "Name the carrier.")
        self.assertEqual(ruling.causal_parent_ids, [first.event_id])

    def test_checkpoint_resumes_next_item_exactly(self):
        engine = Engine(40917)
        engine.schedule_actor("JOSH", 20)
        engine.schedule_actor("HUGH", 10)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "checkpoint.json"
            engine.save(path)
            restored = Engine.load(path)
        self.assertEqual(engine.next_scheduled(), restored.next_scheduled())
        self.assertEqual(engine.deterministic_int("latency:HUGH", 1, 100), restored.deterministic_int("latency:HUGH", 1, 100))

    def test_outputs_are_derived_from_events(self):
        engine = Engine(1)
        engine.schedule_actor("JORDAN", 5)
        engine.step(lambda actor, packet: {
            "decision": "act", "channel": "paper_note", "target_ids": ["JOSH"],
            "action_text": "Private.", "visibility": "private", "dais_knows": False
        })
        engine.schedule_actor("JOSH", 10)
        engine.step(lambda actor, packet: {
            "decision": "act", "channel": "floor", "action_text": "Public."
        })
        with tempfile.TemporaryDirectory() as directory:
            engine.write_outputs(directory)
            with open(Path(directory) / "master_timeline.csv", newline="", encoding="utf-8") as handle:
                master = list(csv.DictReader(handle))
            with open(Path(directory) / "chair_view.csv", newline="", encoding="utf-8") as handle:
                chair = list(csv.DictReader(handle))
        self.assertEqual(len(master), 2)
        self.assertEqual([row["text"] for row in chair], ["Public."])


if __name__ == "__main__":
    unittest.main()
