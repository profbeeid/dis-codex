# Disney 4.0 Crisis-Material Calibration Runbook

**Purpose:** estimate how many crisis cards and core problem engines each committee session needs, observe how medium-level delegates respond, and learn which Money–Love–Control pressures create useful council dynamics.

**Primary simulation:** 240 active committee minutes, M3 — The Blackout followed by M1 — The Empty Vault.

**Actual-room warning:** the live committee has more seats than the nine core characters. A nine-character run is useful for understanding motives and causal texture, but it will usually overestimate the need for external crisis cards and underestimate dais traffic. Therefore this protocol uses one full-fidelity nine-character run and one lighter full-roster load calibration.

---

## 1. The question this run must answer

This is not a screenplay contest and not a prediction of particular students. The experiment asks:

1. How long can one major crisis generate live decisions before it needs new information?
2. How many prepared crisis cards become eligible, how many actually need to fire, and how many are redundant?
3. Which kinds of pressure wake multiple roles and produce negotiation, coalition, resistance, or executable directives?
4. How do those pressures trade Money, Love, and Control?
5. Which room developments arise endogenously from delegates, and which require a world injection?
6. What remains unresolved at the close, and what later sessions can inherit?

The simulation succeeds even if a session is quiet, confused, or indecisive. Those are findings. It fails if it manufactures activity to make the transcript entertaining.

---

## 2. Lessons from the first two attempts

The Claude attempt built useful machinery but let the engine preselect behavior and then used generated prose as decoration. The Codex attempt understood the 4.0 business logic but hardcoded the whole story before exporting simulation artifacts.

The corrected division is strict:

- the scheduler decides **when an actor becomes eligible**;
- the actor decides **whether and how to act**;
- the world resolver decides **what the attempted action can actually cause**;
- the crisis deck supplies **facts, clocks, counterparty moves, and matured consequences**;
- the dais sees and decides only what real cochairs could see;
- the recorder preserves everything without changing it;
- the ending narrator writes only after terminal state is locked.

The engine must never choose an actor's intention. The actor must never resolve its own success. The narrator must never repair the run.

---

## 3. The unit of design: problem engines, not piles of cards

A **core problem engine** is a persistent causal knot that can produce several developments. A **crisis card** is one observable manifestation of that problem. Ten disconnected surprises create noise; one good problem engine can create six meaningful consequences.

Each major crisis should contain three intertwined knots:

### 3.1 Capability knot

Something Disney wants to do cannot be done at full scale with present people, systems, time, cash, rights, or operating capacity.

This mainly tests Money, but it becomes dynamic when authority says yes and capability still says no.

### 3.2 Dependency knot

A counterparty, platform, regulator, talent coalition, board faction, lender, distributor, or supplier controls something Disney needs.

This mainly tests Control. The strongest versions offer real value rather than acting as villains.

### 3.3 Legitimacy knot

Customers, employees, creators, investors, communities, or audiences disagree about what Disney owes them and what the company is for.

This mainly tests Love. Love means observable trust, attachment, cooperation, willingness to return, or willingness to lend one's reputation—not sentiment in the abstract.

A strong session forces the three knots to touch. For example, buying temporary capability may preserve Love while renting away Control; protecting Control may consume Money and frustrate audiences; maximizing Money may reveal that the company no longer knows whom its product is for.

---

## 4. What a crisis card is

Here, a card is a prepared world development. It is **not** an action currency held by delegates.

Every candidate card must contain:

```yaml
card_id: M3-C07
family: capability | counterparty | evidence | deadline | legitimacy | consequence | reserve
title: short chair-facing label
trigger_type: clock | state | action_consequence | failure_to_act | reserve
trigger: exact observable condition
earliest_time: committee timestamp
latest_useful_time: committee timestamp or null
delivery: public_update | private_note | direct_counterparty_message | document
recipients: [actor_ids]
observable_text: what recipients actually receive
new_information: what changes in their decision set
live_choice: the decision or conflict this makes newly relevant
actor_hooks: [two_to_four_roles]
money_exposure: amount, capacity, or direction with evidence
love_exposure: affected stakeholder behavior with evidence
control_exposure: affected right, dependency, data, authority, or reversibility
possible_children: [card_ids]
expires_when: condition that makes the card obsolete
business_principle: one principle only
```

Do not write a required social reaction. “Mara betrays Josh” is not a crisis card. “The board receives evidence that the announced capacity does not exist” can be one; Mara may exploit it, ignore it, investigate it, or bargain privately.

---

## 5. The discovery deck

For calibration, overprepare digitally and discover what the room naturally consumes. Begin each simulated session with fifteen candidate cards:

- three clock or deadline cards that occur independently of delegate preference;
- three evidence cards that clarify, segment, or contradict the opening picture;
- seven conditional consequence cards covering the main strategic branches;
- two reserve cards that are not used merely because the room is quiet.

Only a fraction should fire. Expectation is not a quota.

A card may fire only when its trigger is true. A clock card may fire at its time. A consequence card requires a cited parent action or failure to act. A reserve card may fire only when no unresolved pressure, decision, counterparty response, unfinished directive, or maturing consequence has been live for ten committee minutes.

Silence under a live deadline is itself an event. Let the clock charge its price instead of injecting entertainment.

### 5.1 Card families versus printed cards

The practical object to prepare is a **card family**, not fifteen unrelated scripts. One family can have two or three prewritten variants responding to different choices.

For example, a distributor-response family might contain:

- a settlement variant after Disney demonstrates a credible alternative;
- a harder-terms variant after Disney bluffs without capacity;
- a public-escalation variant after Disney attacks the counterparty.

The simulation should recommend both the number of families and the number of printable variants.

---

## 6. Which cards create council dynamics

The most productive cards change who needs whom. They do not merely make a number worse.

### 6.1 Capacity collision

Two approved initiatives require the same team, budget, data, physical asset, executive attention, or delivery window. This creates real opportunity cost and forces roles to bargain over displaced work.

Typical pattern: Money pressure activates Finance and operating owners; Control enters when someone claims priority rights; Love enters when the displaced project has a constituency.

### 6.2 Valuable offer with durable strings

An external party offers cash, reach, speed, or rescue in exchange for data custody, exclusivity, rights, vetoes, windowing, or long dependence.

Typical pattern: Money and Love improve now while Control falls later. This is usually more dynamic than a hostile ultimatum because reasonable delegates can disagree honestly.

### 6.3 Segmented evidence

The average result is weak but one audience, product, character, geography, or channel is strong. This prevents a simple yes/no answer and forces the room to separate an asset from a project.

Typical pattern: Love becomes specific rather than rhetorical; Money asks whether the signal can be tested cheaply; Control asks who owns the learning and future rights.

### 6.4 Approval meets implementation

A directive is legally or politically authorized but lacks staff, cooperation, vendor capacity, system readiness, rights, or time.

Typical pattern: Control appears high on paper but is low in reality. Money burns through delay; Love falls if the company promised delivery too early.

### 6.5 Deadline with asymmetric information

Different roles hold different parts of the walk-away point, cost curve, legal exposure, customer effect, or counterparty tolerance.

Typical pattern: notes and selective disclosure matter. Delay should change the bargaining range instead of merely triggering a generic penalty.

### 6.6 Public interpretation of a technically sound act

An action works operationally but is understood by audiences, talent, employees, investors, or regulators as evidence of something larger.

Typical pattern: Money may improve while Love falls. Control may rise through decisive action but later weaken when cooperation disappears.

### 6.7 Governance threshold

The board, regulator, shareholder, or coalition does not take over operations; it demands a standard, record, deadline, remedy, review, or leadership consequence.

Typical pattern: Control changes hands indirectly. The argument becomes who may decide, what evidence makes the decision legitimate, and when failure becomes leadership failure.

Cards that only add bad news, punish a successful plan, or summon a new antagonist without changing the decision set are weak cards.

---

## 7. Money, Love, and Control as evidence

Do not move a dial because a sentence sounds persuasive. A movement requires an observable receipt.

### Money

Record actual or bounded exposure: cash committed, cash avoided, margin, capacity hours, staff displacement, contractual liability, financing runway, or revenue at risk.

### Love

Record stakeholder behavior: audience retention, churn, attendance, creator cooperation, employee participation, partner willingness, public trust, or a credible change in attachment. Noise on social media alone is weak evidence.

### Control

Record enforceable position: decision rights, ownership, data custody, distribution dependence, vetoes, exit rights, reversibility, board authority, or the operational ability to execute.

The observer may record Love and Control changes on an ordinal scale from -2 to +2, but every entry must cite the event and evidence class. Money should use a real unit where possible. The public room sees direction and explanation, not false precision.

The most useful analytical label is the **conversion**:

```text
Money buys Love but rents Control.
Control is protected by spending Money and accepting short-term Love damage.
Love creates an option, but Money and capability are needed to convert it.
Delay burns Money and Love because fragmented Control prevents action.
```

---

## 8. Participants and the student layer

The full-fidelity run uses the nine core roles. Each receives a separately assigned synthetic student profile. The role determines motive, authority, information and leverage. The player profile determines comprehension, public confidence, drafting speed, attention, risk tolerance and tendency to ask for help.

No player is generically “medium.” Medium is the cohort average. Use uneven profiles so one student may understand quickly but draft slowly, another may speak confidently but misunderstand finance, and another may spot leverage but avoid public confrontation.

Do not use dialogue style as a substitute for cognition. A fragment is not evidence of confusion. Confusion must appear as a belief, question, wrong inference, or failed action.

For full-roster calibration, add the remaining delegate roles as lower-frequency actors with complete offices and player profiles. Invoke them only when a card, decision, resource, or relationship touches their remit. This second pass estimates congestion and endogenous activity, not literary depth.

---

## 9. Continuous-time actor loop

The simulation clock runs continuously. Thirty-minute blocks are checkpoint windows only.

At each step:

1. Advance to the next scheduled clock event, actor eligibility time, note arrival, drafting completion, directive service event, or matured consequence.
2. Recalculate readiness only for affected actors.
3. Invoke each eligible actor separately with a fresh authorized packet.
4. Accept `act`, `wait`, `continue_drafting`, or `abandon_task`.
5. Merge only observable outputs into the appropriate channels.
6. Resolve attempted actions through authority, capability, cooperation, legitimacy, time, and uncertainty.
7. Re-evaluate card triggers. Do not fire a card merely because one became available; fire it when the world event would actually occur and it remains decision-relevant.
8. Update card, problem, resource, relationship, promise, directive, dais-load and axis ledgers.
9. Checkpoint authoritative state.

One invocation may involve only one actor. Agents do not chat directly through shared context. Interaction occurs through delivered speech, notes, meetings and consequences.

---

## 10. Actor decision contract

Each actor receives only its role layer, player layer, living private state, observations, delivered messages, relevant public events, accessible resources, deadlines and pending work.

It returns structured JSON:

```json
{
  "actor_id": "HUGH",
  "decision": "act | wait | continue_drafting | abandon_task",
  "channel": "floor | paper_note | private_meeting | directive | resource_commitment | leak | none",
  "target_ids": [],
  "action_text": "",
  "claimed_authority": "",
  "resources_requested_or_committed": [],
  "knowledge_source_ids": [],
  "belief_updates": [],
  "task_update": "",
  "confidence": "low | medium | high"
}
```

The engine must reject inaccessible knowledge IDs. It must not convert the actor's reasoning into success. A polished directive can still fail for lack of capability or cooperation.

---

## 11. Dais and paper reality

Paper notes are private and default to `dais_knows=false`. Directives alone enter the formal queue. A private bargain expecting company resources must later produce an implementation registration containing owner, resource, counterparty and deadline; this registers operational demand without surrendering the note.

The dais workload includes:

- receiving paper;
- OCR and human correction;
- confirming directive text;
- assigning a cochair;
- checking authority, capability, cooperation and evidence;
- requesting revisions;
- ruling and returning paper;
- updating state and selecting eligible world consequences;
- portraying external pressure characters;
- managing floor procedure.

Do not model dais members as three abstract directive servers. Chairing and role portrayal consume time too.

---

## 12. Two-pass experiment

### Pass A — full-fidelity room-feel run

Run the nine core roles for 240 committee minutes using the fifteen-card discovery deck per session. Use real actor invocations and preserve silence, drafting and incomplete work. This produces the qualitative replay.

### Pass B — full-roster load calibration

Run the actual roster with compact JSON responses and minimal prose. Preserve the same crises and candidate cards, but use a different registered seed and the full delegate count. This tests whether more endogenous traffic reduces card consumption and whether dais work expands.

If budget permits, add three lean replications with rotated player–role assignments. One story cannot estimate card quantity reliably.

---

## 13. Required outputs

Write:

```text
outputs/run_<id>/
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

### Card ledger fields

```text
card_id, family, session, trigger_type, became_eligible_at, fired_at,
withheld_reason, expired_at, parent_event_ids, recipients, actor_responses,
directive_descendants, money_effect, love_effect, control_effect,
classification, chair_effort_seconds
```

Classification is one of:

- **essential:** changed the available decision, information, deadline, capability, or counterparty position;
- **productive:** activated a dormant role or converted talk into action without forcing a result;
- **redundant:** repeated live pressure without changing behavior or options;
- **distorting:** introduced an unrelated plot or social outcome;
- **unused:** never became necessary.

### Problem-state fields

Track each core knot, its live decisions, unresolved dependencies, active roles, time since last endogenous development, and whether external material was actually needed.

---

## 14. How to recommend the physical deck

Do not report only “seven cards fired.” Explain why.

For each session report:

- number of candidate cards;
- number that became eligible;
- number fired;
- number essential, productive, redundant and unused;
- natural minutes between cards;
- longest period with no live problem;
- percentage of meaningful developments generated by delegates rather than cards;
- which card families repeatedly created multi-role action;
- which branches lacked prepared coverage;
- chair effort per fired card.

After multiple runs, recommend:

```text
required card families
= all branches that became decision-relevant in any credible run

printable card count
= highest natural fired count across baseline and load runs
   plus a 25% operational reserve, rounded up
```

Do not count redundant or distorting cards in the base. Keep at least two reserve cards, but do not assume they will fire.

The expected practical answer may be something like five to seven families, eight to twelve printable variants, and five to eight cards actually fired. The simulation must discover the number rather than force it.

---

## 15. Ending architecture

The ending is a balance sheet of choices, not a dial-score victory screen.

Lock terminal state first. Then generate two endings from the state and causal graph. The narrator cannot add events, reveal unexposed secrets to the room, or improve anyone's reasoning.

### 15.1 Ending after the first two sessions

This ending should feel provisional. It must answer six questions:

1. What did Disney save?
2. What did Disney deliberately kill or postpone?
3. Which dependency did it accept?
4. Who gained or lost practical decision power?
5. Which stakeholders still cooperate, and on what conditions?
6. Which unpaid invoice will enter Sessions 3–7?

End with three inherited hooks, not a cliffhanger invented for drama. A useful closing line describes a new operating doctrine and its contradiction—for example: Disney has learned to demand stop gates from its own projects, but it still rents the audience relationship from the party it just fought.

### 15.2 Ending after seven sessions

The final narrative should answer, “What kind of company did this council make?” Use the dominant transaction, not the highest total score.

Possible families include:

- **Rented recovery:** Money and Love recover through a partner, while Control migrates outside Disney.
- **Costly independence:** Disney protects Control by spending Money and accepting slower Love recovery.
- **Beloved fragility:** audiences and talent remain attached, but the company has not built an economically durable operating model.
- **Efficient fortress:** Money and Control improve while Love becomes thinner, older, or more transactional.
- **Coherent sacrifice:** Disney kills real opportunities, aligns capability behind fewer promises, and becomes smaller but more executable.
- **Hollow consensus:** the room agrees publicly, but staffing, cooperation, rights, or evidence never convert approval into reality.

These are narrative lenses, not endings to assign in advance. Mixed endings are preferable when the state supports them.

### 15.3 Required ending forms

`ending_public.md` is a 250–400 word chair-readable close using only public and dais-known information. It names the decision, visible receipt, visible invoice, and next review.

`ending_observer.md` is a 700–1,000 word analysis for Rizky. It may use omniscient state and should identify the dominant Money–Love–Control conversion, unrealized counterfactuals, hidden bargains that mattered, material that never fired, and three credible future paths.

---

## 16. Validation

The run is invalid if:

- events are hardcoded before actors decide;
- the seed is decorative;
- invocation logs are reconstructed rather than captured from actual calls;
- checkpoints cannot resume the next event;
- actor actions lack accessible knowledge sources;
- private notes enter chair view without a leak or operational registration;
- card triggers are absent or retrofitted after firing;
- a card is injected only to prevent boredom;
- the world outcome simply repeats what the actor requested;
- axis movement lacks observable evidence;
- derived files contradict the master timeline;
- the ending introduces facts or closure absent from terminal state.

Diagnostic findings—silence, domination, weak directives, no betrayal, an unused card pool, or an unresolved ending—must be preserved rather than repaired.

---

## 17. Final report questions

The calibration report must answer plainly:

1. How many card families should Rizky prepare for each of these sessions?
2. How many printable variants and reserves should sit behind the dais?
3. Which cards were essential, and which merely made the story prettier?
4. Which core problem generated the most endogenous activity?
5. Which Money–Love–Control conversions produced genuine disagreement?
6. Which roles remained inert, and was that caused by office design, player profile, missing information, or model behavior?
7. Did the larger roster consume fewer cards but create more dais work?
8. What should be removed, rewritten, or added before September?
9. What provisional ending did the first two sessions earn?
10. Which three unpaid invoices should later sessions inherit?

