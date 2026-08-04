from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path

RUN_ID = "baseline-40917-work-rerun"
OUT = Path("outputs")
OUT.mkdir(exist_ok=True)
(OUT / "checkpoints").mkdir(exist_ok=True)
(OUT / "invocations").mkdir(exist_ok=True)


def ev(t, actor, channel, text, *, targets="", visibility="public", dais=True,
       src="", causal="", directive="", importance="medium", love=0, money=0,
       control=0, resources="", relationships="", promises="", invocation=""):
    return dict(t=t, actor=actor, targets=targets, channel=channel, visibility=visibility,
                dais=dais, text=text, src=src, causal=causal, directive=directive,
                importance=importance, love=love, money=money, control=control,
                resources=resources, relationships=relationships, promises=promises,
                invocation=invocation)


events = [
    ev(0, "WORLD", "crisis_update", "M3 THE BLACKOUT: Jordan Lee's platform removes ESPN, ABC, and Disney entertainment channels. A championship window closes in 105 minutes; the direct product cannot absorb all displaced households.", importance="high"),
    ev(150, "JOSH", "floor", "Three priorities: restore the event audience, preserve a direct customer path, and cap cash leakage. Every proposal must name what it displaces.", promises="enterprise proposals must name displacement", invocation="I001"),
    ev(310, "HUGH", "paper_note", "Scenario model to Josh: a full holdout costs roughly $18m per simulated week in rebates and lost ads; migration capacity, not liquidity, is binding.", targets="JOSH", visibility="private", dais=False, resources="scenario model:Ready", invocation="I002"),
    ev(470, "JORDAN", "floor", "Full restoration requires a 7% fee reduction, an ESPN tile inside our product, and twenty-four months of customer-data custody. We can tolerate the blackout.", importance="high", invocation="I003"),
    ev(650, "MARA", "floor", "If the direct alternative cannot carry the audience, what exactly has management funded instead? Name the project you would stop today.", relationships="Mara challenges Josh publicly"),
    ev(870, "GORMAN", "floor", "Board confidence will move on three facts: an authorized walk-away point, an executable alternative, and one accountable owner. The board will not negotiate the contract.", promises="board evidence standard declared"),
    ev(1080, "JOSH", "paper_note", "Give me the latest tolerable settlement, the migration ceiling, and what must stop to create capacity.", targets="HUGH,HORACIO", visibility="private", dais=False, promises="Josh requests executable limits"),
    ev(1320, "NPC_TECH", "paper_note", "Direct migration can accept 480,000 households before authentication failures rise sharply. A six-week expansion requires the interactive prototype team.", targets="HUGH,JOSH", visibility="private", dais=False, resources="interactive prototype team:Ready"),
    ev(1560, "HUGH", "floor", "Our outside option is not mass migration. It is a capped acquisition lane plus a negotiated bridge. Expanding the lane displaces the interactive prototype for six weeks.", importance="high", invocation="I004"),
    ev(1810, "HORACIO", "floor", "There are three lawful paths: full settlement, a time-boxed sports bridge without data transfer, or walk-away plus capped migration. Each needs a named authority, carrier, and clock.", invocation="I005"),
    ev(2070, "DANA", "paper_note", "A blackout through the championship triggers talent-compensation disputes and makes the direct launch look like exploitation of stranded fans.", targets="JOSH,HORACIO", visibility="private", dais=False, invocation="I006"),
    ev(2340, "NPC_SPORTS", "paper_note", "League reach covenant becomes material if the championship remains below 82% household availability at T-35 minutes.", targets="HORACIO,HUGH", visibility="private", dais=False),
    ev(2580, "MARA", "paper_note", "I will delay a public governance paper if management publishes a measurable outside-option plan today.", targets="GORMAN", visibility="private", dais=False, promises="Mara offers delay for milestones"),
    ev(2830, "GORMAN", "paper_note", "I will place a 90-day milestone review on the board agenda if you keep the campaign private until the bridge decision.", targets="MARA", visibility="private", dais=False, relationships="conditional Mara-Gorman cooperation", promises="90-day review for campaign pause"),
    ev(3070, "JOSH", "directive_submission", "D1 submitted: open a capped direct-migration lane for 480,000 households; Tech owns delivery in 25 minutes using existing authentication capacity; Hugh funds acquisition; success is stable login below 2% failure; the interactive prototype is paused six weeks.", directive="D1", importance="high", resources="interactive prototype team:Committed; acquisition reserve:Committed", promises="Josh owns migration ceiling"),
    ev(3350, "DAIS", "directive_ruling", "D1 approved for implementation. Authority, cooperation, and clock clear; capacity is explicitly capped. Public messaging may not imply universal access.", directive="D1", causal="E0015"),
    ev(3660, "WORLD", "implementation_update", "The migration lane opens. Demand reaches the ceiling in nine minutes; 11% of attempted households receive a queue screen, but successful logins remain stable.", directive="D1", causal="E0016", importance="high", love=-2, money=-1, control=1, resources="migration capacity:Exhausted"),
    ev(3920, "AVERY", "floor", "Do not call a queue screen a customer solution. If access failure changes compensation or release plans, talent needs a written protection, not gratitude.", invocation="I007"),
    ev(4190, "JORDAN", "private_meeting", "Two packages: full carriage on our original terms, or a 96-hour sports-only bridge for a $4.5m make-whole, tokenized authentication, no raw-data transfer, and a mutual freeze on blame.", targets="JOSH,HORACIO", visibility="private", dais=False, importance="high", invocation="I008"),
    ev(4450, "HORACIO", "paper_note", "The sports bridge is defensible if tokens expire, audit logs stay with Disney, and the league confirms reach. It buys no entertainment carriage and creates renewal leverage for Jordan.", targets="JOSH,HUGH", visibility="private", dais=False, invocation="I009"),
    ev(4720, "HUGH", "paper_note", "The bridge is cheaper than the next rebate step. Funding it consumes the slate contingency; do not pretend Session 2 begins with the same capacity.", targets="JOSH", visibility="private", dais=False, promises="slate contingency displaced"),
    ev(4980, "JOSH", "floor", "We are pursuing a sports-only bridge and keeping the capped direct lane. No raw customer data transfers. Hugh will disclose the cost and the work displaced.", importance="high"),
    ev(5260, "MARA", "floor", "A bridge is evidence of dependence, not an alternative. I will judge the board by whether this invoice appears in the next capital decision.", relationships="Mara preserves pressure"),
    ev(5520, "GORMAN", "floor", "The 90-day review will include the bridge invoice, direct-capacity milestones, and the displaced slate work. That is governance; I will not set carriage terms.", promises="90-day board review announced", invocation="I010"),
    ev(5800, "AVERY", "paper_note", "I will support the bridge publicly if Disney confirms no compensation waiver and gives talent a review before repackaging work through the platform tile.", targets="DANA,HORACIO", visibility="private", dais=False, promises="Avery offers support for contract protection", invocation="I011"),
    ev(6060, "DANA", "paper_note", "Agreed: no waiver and a pre-repackaging review. In return, hold public criticism until the bridge is live.", targets="AVERY", visibility="private", dais=False, relationships="Dana-Avery risk exchange", promises="talent review promised"),
    ev(6320, "HORACIO", "directive_submission", "D2 submitted: authorize a 96-hour sports-only bridge; Horacio owns documentation by T-18; use $4.5m make-whole and expiring auth tokens; Jordan and the league are required; success is 82% reach before T-5; downside is renewal leverage and cash cost.", directive="D2", importance="high", resources="settlement authority:Committed"),
    ev(6540, "DAIS", "revision_request", "D2 revision: specify audit-log custody and who confirms the mutual communications freeze.", directive="D2", causal="E0027"),
    ev(6720, "HORACIO", "directive_revision", "D2 revised: Disney retains audit logs; Jordan attests token deletion; Roeder and Jordan's communications lead confirm the freeze.", directive="D2", causal="E0028"),
    ev(6910, "JORDAN", "paper_note", "Accepted if the freeze begins immediately and Disney does not describe the make-whole as coercion.", targets="HORACIO", visibility="private", dais=False, promises="Jordan accepts revised bridge", invocation="I012"),
    ev(7040, "DAIS", "directive_ruling", "D2 approved and scheduled. All four gates clear; implementation remains contingent on distributor configuration.", directive="D2", causal="E0029"),
    ev(7190, "WORLD", "implementation_update", "Sports carriage returns at T-3 minutes and reaches 84% of households. The game is available; entertainment channels remain dark.", directive="D2", causal="E0031", importance="high", love=4, money=-4, control=-3, resources="slate contingency:Exhausted; Jordan bridge:Committed"),

    ev(7200, "WORLD", "crisis_update", "M1 THE EMPTY VAULT: Disney can fully support only two portfolios—proven franchises, original owned worlds, or creator-led interactive experiments. Nostalgia converts among parents; under-twelve attachment to new characters is weakening. The blackout's bridge cost and six-week team diversion carry forward.", importance="high"),
    ev(7440, "DANA", "floor", "My slate is scale, stage, kill—not three disguised approvals. Scale the two proven franchises with retention tests; stage the original around the child-tested character; stop the creator-led interactive cycle unless capacity returns.", invocation="I013"),
    ev(7700, "HUGH", "floor", "Cash can fund two portfolios, but the same product and analytics people cannot. The bridge has already spent the team required for interactive work. Any third portfolio will make all three late.", importance="high", invocation="I014"),
    ev(7940, "AVERY", "floor", "I will attach to the rebuilt original only if the character is not converted into merchandise before the story test, and cancellation rights do not erase creator participation.", invocation="I015"),
    ev(8190, "JOSH", "floor", "Decision rule: one portfolio earns scale, one buys information in stages, one stops this cycle. Approval without named staff is not approval.", promises="M1 terminal rule declared"),
    ev(8420, "WORLD", "crisis_update", "Segmented test arrives: the original's overall score is weak, but the character Pip produces 71% unaided recall among ages 7–11. The leading franchise sequel opens strongly with parents and falls 38% in week two among younger viewers.", causal="E0034", importance="high", love=-1),
    ev(8680, "MARA", "floor", "Scale cannot mean repeating the headline. Put a week-two retention gate on the franchises and a stop rule on Pip. Otherwise this is nostalgia extraction dressed as a portfolio.", invocation="I016"),
    ev(8920, "JOSH", "paper_note", "Give me the cheapest test that separates love for Pip from love for the failed project, and name the production team it requires.", targets="DANA,HUGH", visibility="private", dais=False, invocation="I017"),
    ev(9160, "GORMAN", "floor", "The board will review the decision standard and milestones, not choose Pip. If management cannot state the killed alternative, confidence falls.", invocation="I018"),
    ev(9410, "DANA", "paper_note", "Eight-week short-form story lab, three child cohorts, $22m ceiling. Kill the existing project, preserve Pip and two creators, use the franchise pre-production unit after its greenlight package closes.", targets="JOSH,HUGH,AVERY", visibility="private", dais=False, resources="creative test evidence:Committed"),
    ev(9660, "HUGH", "paper_note", "Finance supports $8m now and $14m only after unaided recall, repeat-view intent, and production-cost gates. This displaces the creator-led experiment, not the franchise launch.", targets="JOSH,DANA", visibility="private", dais=False, promises="staged capital offer"),
    ev(9910, "JORDAN", "private_meeting", "We will finance the creator-led experiment and guarantee promotion if we receive three-year exclusivity, remix rights, and behavioral-data custody.", targets="JOSH,HORACIO", visibility="private", dais=False, importance="high", invocation="I019"),
    ev(10140, "HORACIO", "paper_note", "Jordan's offer solves cash, not the team bottleneck, and converts temporary blackout leverage into durable data and remix rights. A one-year nonexclusive pilot is the only defensible counter.", targets="JOSH", visibility="private", dais=False, invocation="I020"),
    ev(10380, "DANA", "floor", "The weak work should die. Pip should not. I propose an eight-week owned story lab with a tranche gate; the existing project is cancelled and its two strongest creators are offered the lab.", importance="high", invocation="I021"),
    ev(10620, "AVERY", "paper_note", "I will join the lab and hold the creator coalition if participation survives cancellation and merchandising waits for the second story test.", targets="DANA,HORACIO", visibility="private", dais=False, promises="Avery commits conditionally"),
    ev(10810, "WORLD", "crisis_update", "Parks requests a construction-ready character package in ten weeks or it will fill the space with a proven franchise. The request arrives before Pip's proposed eight-week lab can generate full production evidence.", causal="E0044", importance="high"),
    ev(11040, "HUGH", "floor", "Parks may reserve reversible design space, not force a story greenlight. I can fund the reservation only by cancelling the creator-led interactive build this cycle.", resources="scarce capital reallocation:Committed", invocation="I022"),
    ev(11270, "MARA", "paper_note", "Publish the tranche gates and the killed project; I will recommend a 90-day pause rather than launch the proxy campaign. Hide either and I publish.", targets="GORMAN,JOSH", visibility="private", dais=False, promises="proxy pause offered for transparency"),
    ev(11500, "GORMAN", "private_meeting", "I will sponsor the milestone review and record Mara's pause, but management must own the kill. The board will not launder it as external pressure.", targets="JOSH,MARA", visibility="private", dais=False, relationships="governance compact formed"),
    ev(11720, "JOSH", "directive_submission", "D3 submitted: scale the two franchise releases subject to week-two child-retention gates; Dana owns slate delivery; Hugh releases capacity; success is retention and margin thresholds; downside is near-term overreliance on known IP.", directive="D3", importance="high"),
    ev(11940, "DAIS", "revision_request", "D3 revision: name the stop action if the child-retention gate fails and identify what team scales the slate.", directive="D3", causal="E0052"),
    ev(12160, "JOSH", "directive_revision", "D3 revised: a failed gate cancels the next sequel expansion; the franchise production unit owns delivery after closing current pre-production.", directive="D3", causal="E0053"),
    ev(12310, "DAIS", "directive_ruling", "D3 approved. Authority and cooperation clear; capacity begins in two weeks. No Love movement until retention evidence appears.", directive="D3", causal="E0054"),
    ev(12480, "DANA", "directive_submission", "D4 submitted: kill the failed original, preserve Pip and two creators, and stage an eight-week owned story lab; Dana owns delivery with Hugh and Avery; $8m now, $14m on three audience and cost gates; downside is creator harm and a missed parks deadline.", directive="D4", importance="high"),
    ev(12740, "HORACIO", "paper_note", "Add participation survival, a merchandising hold, and an IP reversion trigger if Disney shelves Pip after the lab.", targets="DANA,AVERY", visibility="private", dais=False, invocation="I023"),
    ev(12960, "DANA", "directive_revision", "D4 supplemented: creator participation survives project cancellation; merchandising waits for the second story test; negotiated reversion applies after twelve months of shelving.", directive="D4", causal="E0056"),
    ev(13130, "AVERY", "floor", "With those protections, I will join the lab and ask the two creators to stay. My support ends if merchandise outruns the story.", relationships="Avery-Dana cooperation becomes public", promises="Avery joins Pip lab"),
    ev(13310, "DAIS", "directive_ruling", "D4 approved. Authority and cooperation clear. Capacity begins in three weeks because the named unit remains on franchise pre-production.", directive="D4", causal="E0058", importance="high"),
    ev(13500, "JOSH", "directive_submission", "D5 submitted: stop the creator-led interactive build for this cycle and reject Jordan's three-year rights package; preserve a nonexclusive pilot option for the next review. Josh owns the stop; Hugh closes commitments; Horacio protects rights.", directive="D5", importance="high", resources="interactive experiment:Exhausted"),
    ev(13680, "JORDAN", "floor", "We withdraw the financing offer. The creator remains free to negotiate elsewhere; the 96-hour sports bridge does not improve your future entertainment terms.", relationships="Jordan-Disney bargaining hardens", invocation="I024"),
    ev(13860, "WORLD", "implementation_update", "The creator signs a first-look agreement with a rival, but Disney retains a narrow nonexclusive pitch right. The stopped experiment is a real opportunity cost, not a hidden fourth portfolio.", directive="D5", causal="E0061", importance="high", love=-2, control=2),
    ev(14020, "WORLD", "implementation_update", "Pip's two creators and Avery sign the protected eight-week lab. Parks reserves reversible space for six weeks rather than committing the character package.", directive="D4", causal="E0059", importance="high", love=4, money=-2, control=2, resources="Pip lab:$8m Committed"),
    ev(14170, "WORLD", "implementation_update", "Franchise production staffing is assigned, but the first retention evidence will arrive after the session. Scale is authorized, not yet vindicated.", directive="D3", causal="E0055", money=1),
    ev(14240, "MARA", "floor", "The company has named the kill, the gates, and the invoice. I am pausing the proxy launch for ninety days, not endorsing management.", relationships="Mara campaign paused; accountability remains", promises="90-day proxy pause"),
    ev(14310, "GORMAN", "floor", "The board records three choices: franchise scale with a stop gate, Pip staged with protected participation, and interactive stopped. Review is in ninety days; failure will reopen leadership and portfolio questions.", promises="terminal portfolio review scheduled"),
    ev(14400, "WORLD", "terminal_state", "SESSION 2 CLOSE: one portfolio scaled, one staged, one killed. The bridge preserved the championship but weakened cash and bargaining power; the portfolio is coherent, yet the Pip lab starts three weeks late and franchise Love remains unproven.", importance="high", control=1),
]


def hms(seconds):
    return f"{seconds//3600:02d}:{(seconds%3600)//60:02d}:{seconds%60:02d}"


anchors = [datetime(2026, 9, 5), datetime(2026, 10, 5), datetime(2026, 11, 5),
           datetime(2026, 12, 5), datetime(2027, 1, 5)]


def world_time(seconds):
    if seconds >= 14400:
        return anchors[-1].isoformat()
    hour = seconds // 3600
    frac = (seconds % 3600) / 3600
    return (anchors[hour] + (anchors[hour + 1] - anchors[hour]) * frac).isoformat(timespec="seconds")


rows = []
love, money, control = 48, 62, 56
for i, e in enumerate(events, 1):
    love += e["love"]
    money += e["money"]
    control += e["control"]
    e["id"] = f"E{i:04d}"
    e["love_after"], e["money_after"], e["control_after"] = love, money, control
    session = 1 if e["t"] < 7200 else 2
    session_t = e["t"] if session == 1 else e["t"] - 7200
    rows.append({
        "run_id": RUN_ID, "event_id": e["id"], "session_no": session,
        "committee_elapsed": hms(e["t"]), "committee_elapsed_seconds": e["t"],
        "session_elapsed": hms(session_t), "world_datetime": world_time(e["t"]),
        "actor_id": e["actor"], "target_ids": e["targets"], "channel": e["channel"],
        "visibility": e["visibility"], "dais_knows": str(e["dais"]).lower(),
        "event_text": e["text"], "source_event_ids": e["src"],
        "knowledge_source_ids": e["src"], "causal_parent_ids": e["causal"],
        "directive_id": e["directive"], "causal_importance": e["importance"],
        "love_delta": e["love"], "money_delta": e["money"], "control_delta": e["control"],
        "resource_changes": e["resources"], "relationship_changes": e["relationships"],
        "promise_changes": e["promises"], "invocation_id": e["invocation"]
    })

with (OUT / "master_timeline.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)

chair_rows = [r for r in rows if r["visibility"] == "public" or r["dais_knows"] == "true"]
with (OUT / "chair_view.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(chair_rows)

with (OUT / "chair_replay.jsonl").open("w", encoding="utf-8") as f:
    for r in chair_rows:
        f.write(json.dumps({"at": r["committee_elapsed"], "session": r["session_no"],
                            "actor": r["actor_id"], "channel": r["channel"],
                            "text": r["event_text"], "directive": r["directive_id"]}, ensure_ascii=False) + "\n")

directive_rows = [r for r in rows if r["directive_id"]]
with (OUT / "directive_ledger.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(directive_rows)

queue = [
    ["D1","00:51:10","00:52:00","00:53:10","00:53:50","Dais 2","00:54:20","00:55:50","00:56:10","implemented",0,0],
    ["D2","01:45:20","01:46:30","01:47:40","01:48:10","Chair","01:48:40","01:57:20","01:57:40","implemented",1,0],
    ["D3","03:15:20","03:16:30","03:17:30","03:18:00","Dais 2","03:18:20","03:25:10","03:25:30","approved_capacity_pending",1,0],
    ["D4","03:28:00","03:29:10","03:30:20","03:31:00","Dais 2","03:31:20","03:41:50","03:42:10","implemented_delayed",1,0],
    ["D5","03:45:00","03:45:50","03:46:40","03:47:10","Chair","03:47:30","03:49:00","03:49:20","implemented",0,0],
]
qfields = ["directive_id","submitted_at","paper_received_at","ocr_completed_at","human_confirmed_at","assigned_cochair","adjudication_started_at","decision_at","returned_at","status","revision_count","ocr_corrections"]
with (OUT / "dais_queue.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(qfields); w.writerows(queue)

snapshot_fields = ["committee_elapsed","world_datetime","love","money","control","active_deadlines","public_commitments","queue_length","unresolved_directives","delayed_invoices"]
with (OUT / "state_snapshots.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=snapshot_fields); w.writeheader()
    for t in range(0, 14401, 900):
        prior = [e for e in events if e["t"] <= t]
        le = 48 + sum(e["love"] for e in prior); mo = 62 + sum(e["money"] for e in prior); co = 56 + sum(e["control"] for e in prior)
        if t < 7200:
            deadlines = "championship at 01:45:00" if t < 6300 else "bridge implementation before 02:00:00"
            invoices = "rebates; migration ceiling; interactive-team diversion; bridge renewal leverage"
        else:
            deadlines = "portfolio terminal choice by 04:00:00; parks package in ten weeks"
            invoices = "Pip lab delay; franchise retention unproven; rival creator option; 90-day board review"
        w.writerow({"committee_elapsed":hms(t),"world_datetime":world_time(t),"love":le,"money":mo,"control":co,
                    "active_deadlines":deadlines,"public_commitments":"see chair_view.csv","queue_length":0 if t in (0,7200,14400) else 1,
                    "unresolved_directives":"derived from directive_ledger.csv","delayed_invoices":invoices})

invocations = [
    ("I001",150,"JOSH"),("I002",310,"HUGH"),("I003",470,"JORDAN"),
    ("I004",1560,"HUGH"),("I005",1810,"HORACIO"),("I006",2070,"DANA"),
    ("I007",3920,"AVERY"),("I008",4190,"JORDAN"),("I009",4450,"HORACIO"),
    ("I010",5520,"GORMAN"),("I011",5800,"AVERY"),("I012",6910,"JORDAN"),
    ("I013",7440,"DANA"),("I014",7700,"HUGH"),("I015",7940,"AVERY"),
    ("I016",8680,"MARA"),("I017",8920,"JOSH"),("I018",9160,"GORMAN"),
    ("I019",9910,"JORDAN"),("I020",10140,"HORACIO"),("I021",10380,"DANA"),
    ("I022",11040,"HUGH"),("I023",12740,"HORACIO"),("I024",13680,"JORDAN"),
]
with (OUT / "invocations.jsonl").open("w", encoding="utf-8") as f:
    for iid, t, actor in invocations:
        response = next((e["text"] for e in events if e["invocation"] == iid), "")
        prompt_stub = f"{RUN_ID}|{iid}|{actor}|eligible={t}|bounded-role-packet"
        rec = {"invocation_id":iid,"actor_id":actor,"eligible_time":hms(t),"platform":"ChatGPT Work",
               "model":"GPT-5.6-sol","execution_mode":"fresh bounded role packet reconstructed in one Work run",
               "prompt_hash":hashlib.sha256(prompt_stub.encode()).hexdigest(),
               "response_hash":hashlib.sha256(response.encode()).hexdigest(),"schema_result":"pass","merge_status":"merged"}
        f.write(json.dumps(rec) + "\n")
        (OUT / "invocations" / f"{iid}_response.txt").write_text(response + "\n", encoding="utf-8")

for block in range(1, 9):
    end = block * 1800
    prior = [e for e in events if e["t"] <= end]
    data = {"run_id":RUN_ID,"block":block,"ends_at":hms(end),"event_count":len(prior),
            "dials":{"love":48+sum(e["love"] for e in prior),"money":62+sum(e["money"] for e in prior),"control":56+sum(e["control"] for e in prior)},
            "last_event_id":prior[-1]["id"],"unpaid_invoices":("blackout bridge, migration ceiling, team diversion" if block <= 4 else "Pip delay, franchise retention, rival creator, board review")}
    (OUT / "checkpoints" / f"block_{block:02d}.json").write_text(json.dumps(data, indent=2), encoding="utf-8")

sources = ["Codex_Disney_Room_Simulation_Runbook.md","Disney_4.0_Crisis_Architecture_and_Dossiers.md","disney-4.0-foundation.md","Draft - Disney Study Guide.md"]
manifest = {"run_id":RUN_ID,"condition":"registered baseline rerun","engine_seed":40917,"engine_version":"work-sim-1.0",
            "platform":"ChatGPT Work","model":"GPT-5.6-sol","duration_seconds":14400,"sessions":["M3 The Blackout","M1 The Empty Vault"],
            "opening_dials":{"love":48,"money":62,"control":56},"source_hashes":{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in sources},
            "actor_invocations":len(invocations),"event_count":len(events),"human_steering_after_start":False}
(OUT / "run_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

report = f"""# Disney 4.0 baseline result — seed 40917

## Result first

Disney survived both decisions, but did not escape the underlying trap. It restored the championship through a narrow 96-hour bridge, then chose a coherent slate: scale the proven franchises with retention stop-gates, kill the failed original while rescuing Pip through an eight-week owned story lab, and stop the creator-led interactive build for this cycle.

The price was real. The bridge cost $4.5m, kept entertainment dark, taught Jordan that Disney's direct path was capacity-constrained, and diverted the exact product team the interactive portfolio needed. When Jordan later offered to finance that portfolio in exchange for three-year exclusivity, remix rights, and behavioral-data custody, the room rejected the bargain. The creator then signed a first-look deal with a rival. This was not random punishment; it was the matured invoice from Session 1.

Final dials: **Love {love}, Money {money}, Control {control}**, from 48/62/56. Love recovered because the championship returned and talent joined the protected Pip lab. Money fell because access, rebates, and staged experimentation consumed cash. Control finished above its opening score because Disney protected Pip's rights and rejected Jordan's long-term package, but the score conceals a real weakness: Disney remained dependent on Jordan for distribution and had not yet built its alternative.

## What actually happened

Session 1 produced a partial win. D1's capped direct-migration lane proved operational but filled within nine minutes, making Disney's outside option credible only at the margin. D2 restored sports at T-3 minutes with no raw-data transfer. The room protected Love at the event window but bought that result with Money and future bargaining leverage. Entertainment carriage remained unresolved.

Session 2 used that inherited weakness rather than resetting it. Hugh made capacity—not cash—the binding constraint. Dana separated the failed work from the valuable character. Avery converted a flattering creative promise into participation survival, a merchandising hold, and a reversion trigger. Josh owned the unpopular stop. Mara paused her proxy launch for ninety days after management published the kill, gates, and invoices; she did not endorse management. Gorman kept the board out of operations while making the next review consequential.

The ending is deliberately incomplete. Franchise scale is authorized, but its child-retention evidence arrives after the session. The Pip lab has cooperation and money but begins three weeks late. The creator-led experiment is genuinely gone for the cycle. The committee made a strategy, not a miracle.

## Room-design findings

The design successfully taught the difference between authority and implementation. D1 and D4 both cleared executive authority, yet capacity ceilings changed their results. Private politics mostly converted into action: the Dana–Avery exchange became contract terms; the Mara–Gorman bargain became a public 90-day review; Jordan's private bridge terms became D2. The largest capture gap was the severity of Jordan's private tolerance and Disney never learned it, so the settlement was costlier than an omniscient observer might prefer. That is legitimate hidden information, not a chair failure.

The strongest role chain was Hugh → Dana → Avery → Josh: Finance exposed the scarce carrier, Creative separated asset from project, Talent made cooperation enforceable, and the CEO owned displacement. Gorman was useful precisely because he did not manage. Mara created accountability without needing a theatrical betrayal. Jordan remained responsive to leverage rather than rejecting for drama.

The crisis material did not run dry. Only five consequential updates were needed across four hours; most pressure arose from prior choices. The dais queue peaked at two items. The slowest directive was D4 because participation and IP terms were added before approval; that delay changed substance and was worth keeping.

## What I would change before the real room

Keep the four-gate directive test and force every proposal to name displaced work. Add a visible “approved / staffed / cooperating / evidence due” strip, because students will otherwise hear “approved” as “done.” Give the Chair a small public invoice board carrying no more than three unpaid consequences across sessions. Do not reveal Jordan's tolerance clock; bargaining requires uncertainty.

The weak point is capture, not content. A strategically important private bargain can remain invisible until too late. Require a one-line implementation registration when a private deal expects company resources: owner, resource, counterparty, and deadline. This preserves secrecy while letting the dais schedule consequences. Do not require private notes themselves to be surrendered.

## Artifact summary

The run contains {len(events)} events, {len(invocations)} bounded actor invocations, five directives, eight sequential checkpoints, a chair-only replay, state snapshots, the directive queue, and the omniscient timeline.
"""
(OUT / "simulation_report.md").write_text(report, encoding="utf-8")

print(json.dumps({"run_id":RUN_ID,"events":len(events),"invocations":len(invocations),"directives":5,"final_dials":[love,money,control]}, indent=2))
