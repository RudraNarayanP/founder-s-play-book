# Repair Sheet — Amazon.com (company_001_amazon) · Stage 2 · Audit 1 (Chronology)
Repairs agent: Level-3 (independent of auditor; executes `amazon_s2_audit1_chronology.md` instruction set)
Date opened: 2026-09-25 · Mode: write (restricted file set only) · Web requests: **0** (local `sources/` + `research/` decide everything)
Source of instructions: `founders_playbook/03_quality_control/amazon_s2_audit1_chronology.md` (CONDITIONAL FAIL), "Repair instructions for a separate pass" items 1–12 plus per-check defect lists.
Files permitted: `stage_2_part_1.md`, `stage_2_part_2.md`, `stage_2_part_3.md`, `stage_2_claim_records.md`, `stage_2_claim_records_part_2.md`, `stage_2_index.md`, `timeline.csv`, `conflicts.csv`, `data_gaps.csv`, this sheet. Stage-1 files untouched (second agent owns them).

## Defect rows

| D# | Defect (audit ref) | File | Site | Before → After | Evidence | Sweep command | Status |
|---|---|---|---|---|---|---|---|
| D1 | Check 1.1 / R1 — unsourced 1996-04-26 "window closes" | stage_2_part_3.md | :33 (refs :151, :164, :1526) | "1996-04-26 · A Section 4(2) window closes" → row merged into 1996-05-16 row; 1996 slice UNKNOWN | S-1 orig. Item 5 ¶4 l.4300 (1995-12-06 → 1996-05-16); no dossier record | `grep -n "1996-04-26\|04-26" stage_2_part_*.md timeline.csv` | OPEN |
| D2 | Check 1.1 / R1 — register twin says "continues" | timeline.csv | :61 | retitle to checkpoint / window continues, or delete | same | `awk -F, 'NR==61' timeline.csv` | OPEN |
| D3 | Check 1.2 / R2 — Associates "per the filings" | stage_2_part_3.md | :36, :113, :125 | strike filing attribution → company-retrospective `RETRO`, start UNKNOWN | §D.1 part_1:181; part_2:35, :349; §S part_3:153; S2A-G5 | `grep -n "Associates" stage_2_part_*.md` | OPEN |
| D4 | Check 6.2 / R2 — Associates drift not in §U | stage_2_part_3.md + conflicts.csv | new U.112 + row | add block + row 1:1 | as D3 | `grep -c "^stage-2" conflicts.csv` | OPEN |
| D5 | Check 6.1 — 4(2) close-date drift not in §U | stage_2_part_3.md + conflicts.csv | new U.113 + row | add block + row 1:1 | as D1 | same | OPEN |
| D6 | Check 2.1 / R3 — Gift Center in-window §R cell | stage_2_part_3.md | :113 | move to tail tagged Nov-1997 (PB) | §D.5 part_1:238; part_2:349 | `grep -n "Gift Center" stage_2_part_*.md` | OPEN |
| D7 | Check 2.2 / R10 — FY1997 terminators untagged | stage_2_part_1.md | :360 | tag ~1,500,000 / 164,015 / derived legs (PB) | 10-K405; part_1:356; part_2:303 | `grep -n "1,500,000\|164,015" stage_2_part_*.md` | OPEN |
| D8 | Check 2.3 / R10 — 58%-of-1997 label slip | stage_2_part_1.md | :132 | add "(1997, post-boundary)" | part_1:390 | `grep -n "58% of 1997" stage_2_part_1.md` | OPEN |
| D9 | Check 4.4 / R4 — Covey duplicate at 1996-03 | stage_2_part_3.md | :32 → :55 | merge into 1996-12-01 row as in-cell absence note | S2A-31 "December 1996"; timeline.csv Covey row | `grep -n "Covey" stage_2_part_3.md timeline.csv` | OPEN |
| D10 | Check 4.3 / R6 — Seafirst row before its event | stage_2_part_3.md | :54 | header 1996-11 → 1996-12 (guarantee ENDS Dec 1996) | orig. S-1 l.2852–2854; S2B-54 (ST2_B_finance.md:138) | `grep -n "Seafirst" stage_2_part_3.md` | OPEN |
| D11 | Check 4.4 / R5 — (PB) block non-monotonic | stage_2_part_3.md | :90–:94 | re-sort to date order | §Q scope rule :22 | read-back of §Q tail | OPEN |
| D12 | Check 4.5 / R7 — U.94 false structural claim | stage_2_part_3.md | :1266–1267 | claim rewritten to describe §Q paired rows | §Q :51/:52 | `grep -n "no §Q row is created" stage_2_part_3.md` | OPEN |
| D13 | Check 3.2 / R9 — rename bounds conflict | stage_2_part_3.md | :95 | bound restated 1994-11 → 1995-07 per register | timeline.csv:114, :19; Ex. 10.12 | `grep -n "bounded" stage_2_part_3.md` | OPEN |
| D14 | Check 7.1 / R8 — U.87 register day-precision | timeline.csv :87,:90 + conflicts.csv :88 | 1997-01-31 / 1997-02-20 → 1997-01 / 1997-02 | orig. S-1 Item 5 ¶7 l.4330 months only | `grep -n "1997-01-31\|1997-02-20" *.csv stage_2_part_*.md` | OPEN |
| D15 | Check 7.3 / R12 — §Q :92 row has no register row | timeline.csv | new (POST-BOUNDARY) row or fold into 1998-06 row | §Q :92; music register row | `grep -n "music" timeline.csv` | OPEN |
| D16 | Check 5 / R11 — §Q :17 pricing-date label | stage_2_part_3.md | :17 | "424B1 pricing date" → filing date; pricing 14 May | 424B1 l.98; S2A-53; 10-K405 l.1126 | `grep -n "pricing date" stage_2_part_3.md` | OPEN |
| D17 | Check 5 / R11 — volume header effectiveness shorthand | part_1/part_2/part_3 | :9 each | "bounded at the IPO's effectiveness" → final priced prospectus, effectiveness 1997-05-14 | 10-K405 l.1126; part_1:18 | `grep -n "bounded at the IPO" stage_2_part_*.md` | OPEN |
| D18 | Check 4 / R11 — §Q scope promises 1995-12 row | stage_2_part_3.md | :18–19 | drop/declare the promised class | §Q rows | read-back §Q head | OPEN |
| D19 | Check 7.4 / R11 — quarterly-vs-dated convention unstated | stage_2_part_3.md | :18–24 | add convention line (1997-Q1 vs 1997-03-31) | timeline.csv BOUNDARY STATE vs §Q :76 | read-back §Q head | OPEN |
| D20 | R12 — index/claim-record status + §U counts | stage_2_index.md, stage_2_claim_records*.md | counts, Status | 68 → 70 blocks; log audit findings as repaired | conflicts.csv recount | `grep -c "U\." stage_2_index.md` | OPEN |

## Invariant ledger (recomputed at close)

| Invariant | Before | After | Check |
|---|---|---|---|
| §U stage-2 blocks in part_3 | 68 (U.44–U.111) | TBD | must equal stage-2 conflicts.csv rows |
| stage-2 rows in conflicts.csv | 68 | TBD | 1:1, no dups/extras |
| stage-2 rows in timeline.csv | 58 | TBD | uniform field count |
| timeline.csv / conflicts.csv / data_gaps.csv field counts | TBD | TBD | uniform per file |
| DERIVED arithmetic intact | TBD | TBD | recheck touched rows |

## Decided NOT to fix (with reasons)
(populated at close)
