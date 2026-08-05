# Instructions for GPT-5.6 Sol in Codex

You are running a Disney 4.0 crisis-material calibration. Your task is not to write a plausible four-hour story. Your task is to execute a real actor–world simulation that tells me how many crisis-card families and printable variants I should prepare, how medium-level delegates might respond, and which Money–Love–Control pressures produce council dynamics.

## Governing source

Read these completely before acting:

1. `Disney_4.0_Crisis_Material_Calibration_Runbook.md`
2. `Disney_4.0_Crisis_Architecture_and_Dossiers.md`
3. `disney-4.0-foundation.md`
4. the study guide and wiki only as legacy sources

Use this precedence: calibration runbook for simulation method, Architecture and Dossiers for current council design, foundation for still-compatible principles, and the study guide/wiki as legacy material. When files conflict, do not silently merge them. Record the conflict and follow the higher source.

Do not introduce delegate action cards, expiring grants, automatic promise penalties, extra global dials, compulsory betrayal, compulsory confusion, or a predetermined ending.

## Result required

Execute:

- Pass A: a full-fidelity nine-core-character run covering 240 committee minutes, M3 The Blackout followed by M1 The Empty Vault;
- Pass B: a lighter full-roster load calibration using the actual delegate roster and the same crisis logic;
- if compute budget permits, three compact replications with rotated player–role assignments.

The seconds are scheduled committee time, not wall-clock model time. Do not sleep for four hours.

## Start by building the experiment

Before simulating, create:

```text
canon/
  roles/
  player_profiles/
  role_player_assignments.yaml
  resources.yaml
  problem_engines.yaml
  crisis_cards_m3.yaml
  crisis_cards_m1.yaml
  directive_rules.yaml
  knowledge_map.yaml
engine/
  clock.py
  scheduler.py
  actor_runner.py
  packet_builder.py
  world_resolver.py
  card_engine.py
  dais.py
  recorder.py
  state.py
  validate.py
tests/
experiments/
  baseline_40917.yaml
  full_roster_load.yaml
```

Compile fifteen candidate world cards for each session: three clock/deadline cards, three evidence cards, seven conditional consequence cards covering credible strategic branches, and two reserves. These are discovery candidates, not a firing quota.

Freeze the manifest, canon hashes, engine seed, actor model, player assignments, card triggers, starting state and validator version before the first event.

## Non-negotiable architecture

The scheduler may decide only when an actor becomes eligible. It may not choose the actor's action type, target, position, coalition or directive.

Every eligible actor must be invoked separately in a fresh context. The actor receives only its authorized role packet, player profile, beliefs, observations, delivered notes, resources, deadlines and pending work. It must return schema-valid JSON choosing:

```text
act
wait
continue_drafting
abandon_task
```

An actor choosing `act` must choose its own channel, targets, text, resource commitment and knowledge sources. Store the complete actual packet and return, or their exact durable hashes plus retrievable files. Do not create invocation records after writing the story.

The world resolver, not the actor, determines success. Evaluate authority, capability, cooperation, legitimacy, time, contractual constraints and uncertainty. Approval is not implementation.

The dais is limited-information. It sees public events, directives, direct dais messages and explicit operational registrations. It does not see private notes or the omniscient state.

## Card discipline

A card fires only when its frozen trigger is true and it remains decision-relevant.

Never fire a card because the transcript is quiet. If an unresolved problem, deadline, unfinished directive, negotiation or maturing consequence exists, allow the room to work or fail under that pressure.

For every candidate card, record when it became eligible, whether it fired, why it was withheld or expired, which actors responded, whether it produced a directive or resource decision, and its Money–Love–Control evidence.

Do not make cards generic punishments. Prefer cards that change who needs whom:

- capacity collisions;
- valuable offers with durable strings;
- segmented evidence;
- approved plans that lack implementation capability;
- deadlines under asymmetric information;
- public interpretation of technically sound acts;
- governance thresholds.

## Money, Love and Control

Do not move an axis because dialogue sounds good.

Money requires cash, margin, liability, runway, staff capacity or displaced-work evidence. Love requires stakeholder behavior such as retention, attendance, cooperation, trust or withdrawal. Control requires changes in rights, data custody, dependency, decision authority, reversibility or executable capacity.

Record the dominant conversion caused by each consequential event. Examples:

```text
Money buys Love but rents Control.
Control is protected by spending Money and accepting short-term Love damage.
Delay burns Money and Love because fragmented Control prevents action.
Love creates an option that still needs Money and capability to convert.
```

## Run sequence

Run a ten-minute mechanics fixture first. It must include one actor waiting, one private note, one unfinished draft, one directive entering the OCR queue, one revision, and one delayed consequence. Fix mechanics only. Discard the fixture's social results.

Then execute Pass A continuously from 00:00:00 through 04:00:00. Checkpoint at each thirty-minute boundary, but do not treat blocks as turns. Overlapping drafting, meetings, paper travel and dais work must be possible.

Session 2 must load Session 1's exact terminal state, including resources, relationships, promises, credibility, fatigue, knowledge, unfinished tasks, queue state and delayed invoices.

After Pass A, execute the full-roster load calibration with compact JSON responses. Do not copy Pass A's outcome. The same card may become eligible and remain unused.

## Outputs

For each run, write:

```text
run_manifest.json
master_timeline.csv
chair_view.csv
chair_replay.md
actor_invocations.jsonl
card_ledger.csv
problem_state.csv
axis_ledger.csv
directive_ledger.csv
dais_load.csv
actor_activity.csv
checkpoints/block_01.json ... block_08.json
ending_public.md
ending_observer.md
calibration_report.md
validation_report.md
```

Every checkpoint must contain enough authoritative state to resume the next event. Prove this by resuming one middle checkpoint and matching the next deterministic scheduling decision.

Derived files must be regenerated from the master timeline and state, never hand-authored separately.

## Ending

Lock terminal state before writing either ending.

The public ending may use only public and dais-known information. It must state what Disney chose, the visible receipt, the visible invoice and the next review. It must not declare victory from dial totals.

The observer ending must explain:

- what Disney saved;
- what it killed or postponed;
- which dependency it accepted;
- who gained practical power;
- which stakeholders still cooperate and on what conditions;
- which unpaid invoice enters later sessions;
- the dominant Money–Love–Control conversion;
- three credible future paths.

Do not force a named ending family. Classify it only after reading terminal state. Possible families include rented recovery, costly independence, beloved fragility, efficient fortress, coherent sacrifice and hollow consensus.

## Calibration judgment

The final report must recommend, separately for M3 and M1:

1. number of core problem engines;
2. number of card families;
3. number of printable variants;
4. expected cards actually fired;
5. reserve count;
6. which cards should be removed as redundant;
7. which unprepared branches need coverage;
8. chair effort and OCR burden;
9. which pressures activated multiple roles;
10. which Money–Love–Control conversions produced the strongest dynamics.

Use the highest natural card consumption across credible runs plus a 25% operational reserve, rounded up. Do not include redundant or distorting cards in the base recommendation.

## Stop conditions

Stop and report the run as invalid if you discover that:

- events are being written before actor decisions;
- the seed does not affect scheduling or uncertainty;
- actor invocations are reconstructed rather than executed;
- private information leaks to the dais;
- cards fire without their frozen triggers;
- checkpoints cannot resume;
- outputs disagree;
- the ending requires inventing facts absent from terminal state.

Do not conceal an invalid run by producing a polished report. Repair the engine, restart under a new run ID, and preserve the failed run for comparison.

## Completion standard

The task is complete only when the actual simulation has run, all outputs exist, validation passes, Pass B has been compared with Pass A, and the report gives a defensible physical-card recommendation rather than merely narrating what happened.
