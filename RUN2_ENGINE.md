# Run 2 engine

This branch fixes the two earlier failure modes. The first engine selected behavior before generating dialogue. The second run hardcoded a polished story and exported it as simulation data. Run 2 does neither.

`simcore.Engine` owns time, access control, card eligibility, the directive queue, checkpoints, and derived views. An external actor runner owns decisions. An external resolver owns consequences. No crisis is included and no simulation is run on this branch.

## Minimal flow

```python
from simcore import Engine

engine = Engine(seed=40917)
engine.add_fact("public_drop", "The channels are dark.", public=True)
engine.schedule_actor("JOSH", at=60)

def actor(actor_id, packet):
    return {
        "decision": "wait",
        "channel": "none",
        "knowledge_source_ids": ["public_drop"],
    }

engine.step(actor)
engine.save("checkpoint.json")
```

Run mechanics tests with:

```bash
python -m unittest discover -s tests -v
```

The tests do not simulate Disney. They prove that actors choose their own action, private information stays private, cards do not auto-fire, directives enter a FIFO queue, checkpoints resume deterministically, and output views derive from the event ledger.

