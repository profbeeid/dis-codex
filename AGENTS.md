# Run 2 rules

Read `Disney_4.0_Crisis_Material_Calibration_Runbook.md` before changing the simulator.

- Do not hardcode a run or write events before actors decide.
- The scheduler chooses when an actor is eligible, never what the actor does.
- Actors choose `act`, `wait`, `continue_drafting`, or `abandon_task`.
- The resolver, not the actor, determines consequences.
- Cards become eligible from frozen triggers; eligibility never auto-fires a card.
- Private notes are hidden from the dais unless explicitly registered or leaked.
- Checkpoints must resume the next scheduled item exactly.
- Derived outputs come only from authoritative engine state.
- Do not run a full simulation unless the user explicitly asks.
- Keep the engine dependency-free and the tests small.
- Push every completed, verified checkpoint to `run2`; do not accumulate finished work only in the local workspace.
