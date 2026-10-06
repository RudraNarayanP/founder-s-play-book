# Tesla Stage 1 — volume index

Written by the Stage-1 merge pass on 2026-09-30 (`tesla-s1-merge`); **re-measured and re-adjudicated by repair
pass 1 on the same date (`tesla-repair-1`, 0 web calls), which retired this file's false null about the 2009-12-31
refundable-reservation balance - see the `U.23` row and decision 5 below, and `CORRECTIONS.md` COR-01/COR-07.**
**One volume**, section letters A–U
continuous across the two parts; **no §9.3 split was triggered** (54,903 words now, 53,553 at merge, against the 40,000-word soft
target and the 60,000-word hard cap). Company tier: **T3 register** (probe `research/A_chronology_feasibility.md`,
**re-issued unchanged** by the later `research/A3_intake_regrade.md` — the later file did not move the family
count, so the merge obeys T3), whose §15.2 8,000-word figure is a **dispatch budget, not a limit on written
evidence** (RD-122). Nothing was trimmed, nothing was re-tiered on word count, and `gates.py --tier register`
therefore reports one budget finding on this volume, which is the adjudicated non-defect.

## Volumes in order

| # | File | Words | Sections contained | Status |
|---|---|---|---|---|
| 1 | `stage_1.md` | **54,903** | merge header + Stage-1 merge note (tier, row application, the 20-row ambiguous attribution, the mint, `U.23`, the truncation report, residue) + `ANCHORS: U.1-U.23` + **Volume 1** (Header, Boundary, §A–§F, claim records P1-01–P1-33, register emission) + **Volume 2** (§G–§U, claim records P2-01–P2-54, `## Untried` NEW-1…NEW-11, register emission) + merge `## Untried` addendum (probe U-1…U-8, five-family table, `U.23` anchor) + COR-01…COR-06 propagation block
  **+ `## Stage-1 repair pass 1` block + COR-07 row + the repair annotations printed inside the two verbatim volumes** | merged 2026-09-30, **single volume — 54,903 words against the 60,000 hard cap, so no second volume exists** |
| – | `_parts/s1_p1.md` | 13,481 as emitted | superseded: carried verbatim as Volume 1 (carried as a byte-identical slice; **no character offset is published here any more** - REPAIR 2026-09-30 (tesla-repair-1): the merge's
  9,746 and audit 1's re-measured 9,859 disagreed because the injected `## Volume 1` heading sits between them,
  and this pass's own header annotation moved every later offset again - so the slice is addressed by its heading
  `## Volume 1` and its first body line `STATUS: WRITTEN 2026-09-27 (authoring pass 1 …)`, which survive edits), SUPERSEDED + truncation notice appended | SUPERSEDED, DO NOT RE-APPLY notice present |
| – | `_parts/s1_p2.md` | 37,551 as emitted | superseded: carried verbatim as Volume 2 (**offset retired for the same reason as volume 1's**; address it by the
  heading `## Volume 2` and its first body line `STATUS: WRITTEN 2026-09-27 (authoring pass 2 …)`), SUPERSEDED notice appended | SUPERSEDED, DO NOT RE-APPLY notice present |

**Section map.** §Header, §Boundary, §A state at the edge, §B founder state, §C concept and licence, §D first
experiment, §E product and the contemporaneous layer, §F customers → **Volume 1**. §G channel, §H competitive and
technological field, §I scaling, §J money and instruments, **§K what the record cannot settle**, §L hindsight
firewall, §M numbers with carriers, **§N contemporaneous vs retrospective**, §O failures, §P decisions, §Q
consequences, §R conflict adjudication, §S fiscal basis and the record-selection null, §T independence ledger,
**§U anchor block** → **Volume 2**. §K, §N and §U are the three T3-mandatory sections and all three are on disk.
Cross-references in the parts use the `(Tesla S1 §B.2, part_1)` form and survive the merge unchanged; the volume
addresses them as **Volume 1 / Volume 2** rather than by line number (§14 rule 12).

## Anchor ranges and where each row lives

The volume declares **23 anchors, `U.1`–`U.23`** (unpadded `U.n`, the convention both parts used). Parity is
**23 narrative anchors ↔ 23 `conflicts.csv` rows**, 0 undeclared, 0 uncovered, 0 duplicate `conflict_id` —
re-measured after the final write (`gates.py`: `anchors | parity`, and `anchors | citation resolution | every
register-cited anchor resolves`).

| range | what it holds | home |
|---|---|---|
| `U.1`–`U.6` | the probe's six: entity date against the 2004 financing-and-hire layer; "one of our founders" against an April 2004 relationship and investment-acquired equity; early officers described only as "former officer and director"; `tesla.com` captures that pre-date the entity (domain precedence); "early 2008" against commercial introduction ≈ 2008-09; the 2026 `Founder is CEO` flag against the dated office record | `conflicts.csv` rows carried from `research/conflicts.csv` — **the emission the census could not see**; extended in Volume 2 §R.1; cited again in `timeline.csv` `conflict_ref`, `data_gaps.csv` and `sources.csv` |
| `U.7`–`U.9` | part 1's three, re-keyed from `P1U-07/08/09` as both parts instructed: one document holding two "earliest" claims nine months apart; four Roadster arrival dates; the prospectus keeps the founder word, the 10-K drops it | `conflicts.csv`; `U.8` is cited from `timeline.csv` three times |
| `U.10`–`U.22` | part 2's thirteen, re-keyed from `P2U-10…22`: the founder adjective against the staff comments; the moving Volt estimate; "no agreements with Toyota" against the executed Toyota agreements; the 8,000,000 → 2,666,666 split restatement; refundability composition; Series A gross vs struck-net; the $22.4m financing residual; FY2009 as-filed against filed-known-understated; the contemporaneous-instrument count; the Amendment No. 2/3 ordinal; the Q1 2010 revenue caption; "dealer" as securities dealer; zero-independent against the enlarged authorship census | `conflicts.csv`, mirrored in `channels.csv`, `validation.csv`, `failures.csv`, `decisions.csv` and `timeline.csv` |
| `U.23` | **minted by this merge, RE-GRADED by repair pass 1.** It is **not** a conflict between two values: $24.8m (2009-09-30, `S4369`), $26.0m (**2009-12-31**) and $26.0m (2010-03-31, unaudited) are **adjacent period-ends of one filed series**, and the 2009-12-31 balance is printed by **11 held bodies across 8 accessions** - `S4370` binds $26.0m to that date in four sentences of one body, and the 424B4 prints the 2008/2009/2010-03-31 triad. What stays in dispute is only part 2's claim that a 2010-03-31 figure supersedes a 2009-09-30 datum: **declined**, across dates. The merge's wording here - "the 2009-12-31 value is UNKNOWN" - is **withdrawn**; it was a false null, and the read that settles it was local, so the 0-call web budget never bore on it | `conflicts.csv` row `U.23` (re-graded in place); anchor line + the `COR-01` and `COR-07` rows of the volume's correction block + the repair-pass block; `quantitative.csv` rows at 2009-12-31 (new), 2010-03-31 (total and by product); `decisions.csv` row 1 |

## Registers at the company root (canonical, nine files)

| register | cols | rows | requested | words | bytes |
|---|---|---|---|---|---|
| `sources.csv` | 18 | **24** | 40 | 4,261 | 33,577 |
| `quantitative.csv` | 12 | **62** | 61 | 2,567 | 20,945 |
| `timeline.csv` | 11 | **46** | 47 | 2,004 | 16,101 |
| `conflicts.csv` | 15 | **23** | 22 | 3,402 | 24,056 |
| `data_gaps.csv` | 8 | **16** | 23 | 1,829 | 13,063 |
| `decisions.csv` | 15 | **9** | 9 | 951 | 7,089 |
| `validation.csv` | 11 | **9** | 9 | 541 | 4,223 |
| `failures.csv` | 11 | **11** | 11 | 814 | 5,990 |
| `channels.csv` | 11 | **10** | 10 | 468 | 3,768 |
| **total** | | **210** | **232** | **16,837** | **128,812** |

*Counts re-measured from the written bytes after repair pass 1. Rows: +1 `quantitative.csv` (the 2009-12-31
reservation period-end the merge called unknowable) and +1 `data_gaps.csv` (the near-collapse gap that
`failures.csv` had been pointing at but which was not registered). No row was deleted. The total line above
replaces the merge's **13,329 / 111,343**, which did not foot against its own cells (they summed to
14,323 / 111,943) - BLOCKER-4. *`sources.csv` grew again after the pass's first measurement, because the
sweep then found the same false `nothing dropped` fold claim in the other seven rows that carried the
boilerplate (S4371, S4372, S4375-S4377, S4389, S4390) and corrected all seven; the figures in the table
above are the final disk state and `_MANIFEST.md` publishes the same numbers from it.*

## The seven merge decisions this index records

1. **Three emissions, not the two in the brief.** 232 requested = part 1 **69** + part 2 **138** + the probe
   dossier's **25** (`research/{sources,conflicts,data_gaps}.csv`). `merge_census.py` reported 207 and cannot see
   `research/` at all; both parts presuppose the probe rows and Tesla had **no** root register, so a merge that
   briefed from the census would have dropped the six anchor rows, the CourtListener registry row and the whole
   independence null. RD-122 and RD-131's rule held a third time.
2. **208 applied, 25 aliased into 16 collision groups, 0 refused.** Folds are not deletions: every aliased row's
   `relevant_passage`, `notes`, `gap`, `why_missing`, `best_available_evidence` and `follow_up_task` print verbatim
   inside the surviving row under a `MERGE[…]` tag, and every dossier-local key that became a minted key prints
   there too — verified by re-scan of the register layer after the final write (40/40 source keys, 16/16 conflict
   keys present).
3. **The 20-row AMBIGUOUS census pair, attributed by content.** Both blocks carry the identical 11-column
   reference header, so the tool cannot attribute either (RD-132's standing defect). The 9-row block is
   `validation.csv` and the 11-row block is `failures.csv`: content first (demand and execution signals versus
   losses, cancellations, recall, settlement, filed error, control deficiency), then part 2's own two independent
   tallies (`validation 9 · failures 11`), then block order. The reasoning is printed inside both registers.
4. **`source_id` block minted centrally: `S4369`–`S4392`** (`tools/id_mint.py --count 24 --claim --agent
   tesla-s1-merge`), allocated above the highest live id and never into a gap. Binding table in
   `03_quality_control/tesla_s1_merge_notes.md` §5. Narrative keeps the parts' `P1Sxx`/`P2Sxx` labels as protected
   history; all register citation cells were re-pointed; **nothing inside a quotation was re-pointed** — an
   `S####` in OCR text is print, not a pointer (RD-131). The `--audit` this pass ran also surfaced a
   **pre-existing** `S4222`–`S4225` collision between Microsoft and Target, handed on untouched.
5. **One conflict minted at merge (`U.23`) and one supersession declined — re-adjudicated by repair pass 1.**
   "Supersede, don't erase" governs documents, not dates: part 2's $26.0m at 2010-03-31 cannot supersede part 1's
   $24.8m at 2009-09-30. **That half stands. The rest of the merge's sentence was wrong:** part 2's 2009-12-31 cells
   *do* have a registered carrier - `S4370`, on this disk since intake, printing $26.0m at that date in four
   sentences, with the 424B4 printing the 2008/2009/2010-03-31 triad. All three period-ends now stand as filed
   values, the flat 2009-12-31 to 2010-03-31 reading is **carried as supported** (its causal reading is not), and the
   contradiction registered here is the lineage's dropping of the 2009-09-30 interim datum, not a missing number.
6. **Tier held at T3 on the families, not on the volume.** The re-grade multiplied family (a) by 10× in bytes and
   added a 336-row XBRL series, but added no family, so §15.2 still gives T3 and the register deliverable is what
   was built — 208 rows, five families accounted for (one TRIED and answered, one TRIED and unanswered, two TRIED
   at the metadata layer only, one UNTRIED entirely), §K/§N/§U all present. The 8,000-word overage is logged as a
   known accepted state in `_MANIFEST.md`, and the gate's "(split required)" wording is recorded as a gate error
   at 53,553 words: §9.2 requires a split only above the 60,000 hard cap.
7. **A pass's own report is not evidence the bytes are on disk.** Part 2's §Untried says "Part 1's `## Untried`
   listed eleven routes"; **part 1's block is not on disk** — the file stops at a stray `#` after its `data_gaps`
   block while citing that section four times (RD-132's Nvidia class). Part 2's eleven items plus the probe's eight
   are carried forward; part 1's wording of them is **reported lost, not reconstructed**.

## What the next reader must not conclude from this volume

Single-lineage is the finding, not a gap to fill: **zero independent carriers of any 2003–2008 founding
statement** across 59.9 MB of held bytes. The founder adjective entered the registration statement between
2010-01-29 and 2010-04-29, is confined to the prospectus family, and does **not** appear in the FY2010 10-K. The
2003-07-01 incorporation date has no non-corporate carrier held. `tesla.com`'s earliest captures pre-date the
entity, so they are domain precedence, not company history — and those CDX rows are transcribed, not re-fetched.
Nothing here resolves whether any named person founded the company, and the volume does not try.
