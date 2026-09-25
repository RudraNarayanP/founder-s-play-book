# Amazon.com Stage 2 — volume index

One forensic document, split at section boundaries for the 60,000-word per-file cap (method §9.2/§9.3).
Nothing is duplicated across volumes and nothing is dropped: the four assembly parts under `_parts/`
remain the audit trail of who wrote which section, including the double-dispatch collision of
2026-09-24 (method §14.7).

| Volume | Sections | Words (pre-repair) | Words (post-repair, 2026-09-25 Audit 1) | Words (post-repair, 2026-09-25 Audit 2 citation) | Words (measured 2026-09-26, blocker-repair pass) |
|---|---|---|---|---|---|
| `stage_2_part_1.md` | Header, STAGE BOUNDARY JUSTIFICATION, §A–§H, + the carried conventions block | 18,360 | 18,560 | 19,289 | **22,967** |
| `stage_2_part_2.md` | §I–§P (incl. §P.2 derived arithmetic) | 25,346 | 25,409 | 25,524 | **28,399** |
| `stage_2_part_3.md` | §Q–§U (+ §S.9 carried untried lists) | 37,423 | 39,760 | 40,385 | **46,016** |
| **Narrative total** | §A–§U | **81,129** | **83,729** | **85,198** | **97,382** |

*The third column was measured by whitespace tokens on 2026-09-25 after the AUDIT-2 citation repair pass; that
pass added in-cell correction and retraction notes (DEFECT-1/2/3/5/7/9) and deleted no text, so each volume grew.*

**Word columns and cap status re-measured 2026-09-26 (blocker-repair pass; AUDIT-6 B7 / T1 / T9).** The Audit-2 column is a stale-but-labelled snapshot and is kept as the earlier state; the new column is this pass's measurement (whitespace tokens of the file as written). **AUDIT-6's `budget` finding that `stage_2_claim_records.md` stood at 60,718 words over the 60,000 cap is a pre-split measurement** - after the §9.3 budget split the appendix measures **44,766** (vol 1a) + **17,352** (vol 1b) + **29,492** (vol 2) = **91,610** across three volumes, and the `budget` gate passes every Stage-2 volume; the max is `stage_2_part_3.md`. **No text was cut to keep it that way** (§9.6 forbids it). Claim records on disk today: **305 + 105 + 72 = 482** (two §U records and B125 minted by this pass).

Word counts are whitespace tokens of the file as written. The growth in part_3 is the two §U blocks
and the §Q re-anchoring added by the Audit-1 chronology repair pass (see Status below); no text was
removed to offset it, and no volume approaches the 60,000-word cap.

Stage 1's equivalent single file (`stage_1.md`) is 49,545 words, so Stage 2 runs ~1.69× Stage 1 — the
growth is concentrated in §P (13,753 w) and §U (19,351 w before the repair pass), which is what a stage
with four SEC filing lineages and 70 live conflicts should look like.

## Numbering continuity

* Conflict blocks: **§U.44 → §U.113b** (Stage 1 owns U.1–U.43). **The spine emits 72 blocks — 70 numbered
  U.44–U.113 plus the two lettered addenda U.113a and U.113b — against 72 `stage2` rows in `conflicts.csv`,** 1:1 with no
  duplicate and no orphan through U.113b. **[SUPERSEDED NOTE, 2026-09-26 blocker-repair pass: this bullet and the register
  table below both asserted "70 rows in `conflicts.csv`" and "stays there until the register owner appends
  U.113a/U.113b". The rows **are** appended. Measured on the file today: 170 data rows = 43 `stage1` / **72 `stage2`** /
  55 `stage3`, and all 170 parse at 15 fields under RFC-4180. The earlier wording stays visible rather than being deleted,
  per §14 rule 4.]** **The two-row excess was declared, not repaired, and its history is a retraction (itself now superseded, 2026-09-26: the rows were appended the same day and the excess this clause describes is closed — see the register table below):** the 2026-09-25 AUDIT-4/AUDIT-5 pass reported that it had appended two new blocks (an IPO price-walk
  re-key and the FY1996/FY1997 restatement pair) and RESERVED their register rows, but §U on disk ended at U.113 with
  **no `>>> CSV APPEND BLOCK: conflicts.csv` section and no RESERVED marker anywhere** in `stage_2_part_3.md`, and the
  two ids its prose cited are **Stage 3's**, so a Stage-2 reader following them landed in another stage's conflict
  (RD-079). Both conflicts are now **written** as the lettered addenda **U.113a and U.113b** at the foot of
  `stage_2_part_3.md` §U, per the U.111a precedent, with **nothing renumbered** (§9.3). `conflicts.csv` held **70 Stage-2 rows** and was to stay there until the register owner appended U.113a/U.113b at
  `stage2`. **That append has happened: the register now holds 72 Stage-2 rows and 170 data rows in total, and the 72↔72
  equality is restored and re-measured by the 2026-09-26 blocker-repair pass, which also re-keys the U.113a row's false
  CLAIM B (COR-16) — the rewrite is handed to the register owner in
  `03_quality_control/amazon_s2_blocker_repairs.md`, not applied through the live owner.** Full sheet:
  `03_quality_control/amazon_s2_dangling_refs_repair.md` (2026-09-26). **U.112 and U.113 were appended by the
  Audit-1 chronology repair pass of 2026-09-25**, each emitted together with its register row so the
  invariant never broke. **No id anywhere in the spine was re-based, renumbered or reused** (method §9.3).
* Metric IDs continue Stage 1's sequence in §P.
* Assembly-part record IDs (S2A-*, S2B-*, S2C-*, S2D-*, S2E-*) resolve to the dossiers in `research/`.
* Claim-record IDs — **RECOUNTED ON DISK 2026-09-26 (blocker-repair pass); the 411/481 tally this line carried is superseded by measurement, not by assertion.** Volume 1a `stage_2_claim_records.md` = **305** records (A01–P90, **B125** minted 2026-09-26); volume 1b `stage_2_claim_records_part_1b.md` = **105** (Q17–T40 plus the §U carry-forward stub); volume 2 `stage_2_claim_records_part_2.md` = **72** conflict records (**U.44 → U.113b**: U.44–U.113 plus the two lettered records, now **minted** 2026-09-26) plus the unnumbered U.111a addendum — **482** lettered records in all, against 72 §U blocks and 72 `stage2` conflict rows. The superseded sentence stays readable here: "Stage-2 volume 1 carries **411** lettered records … volume 2 carries **72** conflict records … **481** in all" — printed when the appendix was two volumes; the 411 matched no disk count of any volume after the §9.3 split (304 + 105). **No record id was renumbered or reused (§9.3).**
* **Accession inventory, updated 2026-09-25 by AUDIT-5 R-2:** the language "**1997 accessions unread**" is retired.
  **S-1/A Nos. 1 (…603, 1997-04-21), 2 (…659, 1997-04-29), 4 (…822, 1997-05-13) and 6 (…847, 1997-05-14) are ON DISK
  and READ**, and are registered in §T as **S0807, S0808, S0809, S0810**; the **FY1998 10-K and FY1999 10-K are also
  ON DISK and now used**, registered as **S0811 and S0812**. Still local-but-unopened: the 8-A12G, the S-8, the S-8
  POS, the 1997-11-10 8-K and the Q2/Q3-1997 Forms 10-Q — a reading debt, not a retrieval gap. Genuine non-local
  witnesses remain the five at `local_copy: NO` (S2006–S2009, S2012) plus the documented null S2005.

## Line-reference keying (AUDIT-2 DEFECT-6, declared here once 2026-09-25)

**Every `l.NNNN` / `ll.NNNN–NNNN` / `LNNNN` in the Stage-2 spine is a line of the convention-named, headered
file `sources/<FORM>_acc-<ACCN>_filed-<DATE>.txt`.** Two accessions also exist as bare-named duplicates without
the 17-line provenance header (`s1_original_0000891618-97-001309.txt`, `s1_0000891020-97-000839.txt`), and the
conversion is exact and directional: **`twin line = keyed line − 17`**. Nothing was deleted; the duplicates are
retained as restoration audit trail. Full table of the four measured probes in
`research/_EVIDENCE_CACHE.md` (the declaration written by the DEFECT-6 repair, 2026-09-25, and keyed there
rather than only here so a grepping agent finds it).

**Citation discipline, added 2026-09-26 (COR-16):** the conversion above is **directional** — a pass that names a keyed path must print a **keyed** number; twin numbers belong only to the two bare duplicates. §U.113a as minted printed twin numbers against keyed paths (l.191 / l.149 / l.1204 where the keyed file has the text at l.208 / l.166 / l.1221) and is re-keyed; its fourth cite (No. 3, "$13.00 per share", l.1230) was re-read and is **exact**, and stays.

**Register visibility of local copies (AUDIT-2 DEFECT-7, 2026-09-25).** Every Stage-2 row of `sources.csv` now
carries a `local_copy: YES|NO` token in `notes` — **6 YES** (S2001–S2004, S2010, S2011: the file named in
`archived_url` is on disk, re-verified this pass) and **6 NO** (S2006 the June-1996 release, S2007 Fortune,
S2008 WIRED, S2009 the B&N 10-K, S2012 the pricing release — five non-SEC witnesses with no byte anywhere — plus
S2005, a documented null where no such document exists at all). Non-SEC witnesses therefore inherit the same visible
status the `(PB)` tag gives post-boundary values, and the in-text `(NO LOCAL COPY — unverifiable at the citation)`
tags point at a register property that actually exists.

## Registers — Stage 2 rows applied 2026-09-25

The `>>> CSV APPEND BLOCK` sections of `_parts/s2_p4.md` were applied to the nine registers by the
orchestrator, validated before writing: header equality with the §13 schema, uniform field count per row,
no duplicate `conflict_id` or `source_id`, `derived_arithmetic` populated on every DERIVED row, and stage
values checked. That pass left every register holding both stages, which is intended — the registers are
per-company, not per-stage.

| Register | Stage 1 rows | Stage 2 added | Total data rows | Field count |
|---|---|---|---|---|
| conflicts.csv | 43 | **72 APPLIED** (measured 2026-09-26: 170 data rows = 43 `stage1` / **72 `stage2`** / 55 `stage3`, every row parsing at 15 fields under RFC-4180. The 2026-09-25 wording "70 APPLIED … the register owner appends U.113a/U.113b" is the superseded state: the rows **were** appended, and the appended U.113a row carries the proposition **COR-16 retracts** — the rewritten row is handed to the register owner in `03_quality_control/amazon_s2_blocker_repairs.md`, because this pass does not edit through a register another agent owns. AUDIT 6's B6 width finding (rows 135/170/171 at 16/18/17) re-measured as a **gate artifact of the retired dialect-sniffing reader**: with `doublequote=False` those three rows shatter into exactly 16/18/17 fields; with the fixed `csv.excel` reader all 170 rows are 15 and the `csv` gate reports **0 findings**) | **170** | 15 uniform |
| quantitative.csv | 111 | 82 | 193 | uniform (untouched by this pass) |
| timeline.csv | 57 | **59** (was 58: +1 `(POST-BOUNDARY)` 1997-06 row) | **116** | 11 uniform |
| validation.csv | 29 | 11 | 40 | uniform (untouched) |
| failures.csv | 33 | 13 | 46 | uniform (untouched) |
| decisions.csv | 15 | 10 | 25 | uniform (untouched) |
| channels.csv | 15 | 8 | 23 | uniform (untouched) |
| sources.csv | 102 | **12** (S2001–S2012; **S2012 added by the AUDIT-2 DEFECT-3 repair** as the register row for the 1997-05-14 pricing release) | **115** | 18 uniform |
| data_gaps.csv | 23 | 22 (3 rows annotated, none added) | 45 | 8 uniform |

## Status of this stage

`RECONSTRUCTION`. **Not audited clean.** The five Stage-2 gates (chronology, citation, numbers, hindsight,
adversarial) are running; auditors who wrote none of the text they audit do the judging, and per method §11
the stage cannot be called complete until all five pass.

* **Audit 1 — chronology (`03_quality_control/amazon_s2_audit1_chronology.md`): CONDITIONAL FAIL, 2026-09-25.**
  Its two mandated re-test classes both recurred inside §Q, and its other findings are itemised below. **The
  defects were FOUND BY THAT AUDIT and are NOT marked complete here**: a repair pass executed the instructions
  the same day (`03_quality_control/amazon_s2_audit1_repairs.md`), and the sheet must be **re-run clean**
  before the gate can be called.
  - **Check 1 (two §Q date defects) — repaired, awaiting re-audit.** (i) `1996-04-26 · "A Section 4(2) window
    closes"` carried **no source in any dossier, filing, register note or Stage-1 record** — the RD-020 class
    repeating. The close is now printed on its filed day **1996-05-16**, the three cross-references are
    re-pointed, and the drift is registered at **U.113**. (ii) *"the Associates Program opened in July 1996
    per the filings"* attributed to a Tier-1 instrument a date it demonstrably lacks — no accession dates the
    launch. Re-rendered as the company's own retrospective `RETRO` dating, and registered at **U.112**.
  - **Check 4 (five §Q ordering items) — repaired, awaiting re-audit.** the duplicated 4(2) close; the
    duplicated CFO row headed **1996-03** (matched no event; merged into the December row, which is now keyed
    `1996-12` because the filing dates the month only); the Seafirst row standing a month before its own stated
    end (re-keyed **1996-12**); the two monotonicity breaks in the `(PB)` block (re-sorted to date order); and
    **U.94**'s false structural claim about §Q (corrected to describe the paired rows rather than deny them).
  - Also repaired: the §R Gift Center import (**November 1997** untagged in a Stage-2 state cell — the only
    genuine firewall breach in the volume set, now excluded and tagged per §D.5); the §F.3 and §C rows'
    untagged FY1997 legs; the rename-null bounds conflict (restored to the register's **1994-11 → 1995-07**);
    the register's unsupported day-precision at **1997-01 / 1997-02** (U.87); the IPO-week and volume-header
    boundary labels; the missing `(POST-BOUNDARY)` register row for §Q's 1997-06 row.
  - **Check 5 (IPO week) PASSED unchanged** — no boundary date moved, and none was moved by this repair pass.
* The claim-record appendix **is** now built (`stage_2_claim_records.md` + `stage_2_claim_records_part_2.md`,
  **479** records against Stage 1's 432), and was aligned to this repair pass: Q20/Q21/Q23/Q36/Q37/Q63/Q66,
  R12 and S17 re-pointed, **Q69** added for the re-anchored Associates row, and **U.112/U.113** records added.
* * **Audits 4 and 5 (hindsight, adversarial) ran on 2026-09-25.** Audit 4 returned **FAIL** on checks 1–5 with 16
  instructions C-1…C-16; Audit 5 returned **CONDITIONAL** with R-1/R-2/R-3 blocking, and its central finding was that
  the four amendments and the two later annual reports this stage had declared unread or un-retrieved were on disk
  throughout. **Both sheets were repaired in one pass on 2026-09-25; the record is
  `03_quality_control/amazon_s2_audit4_repairs.md`. Its headline outcomes: the price walk is re-keyed to seven dated
  states across eight accessions and the "same morning" / "five days" / "first stated range" / "obsolete on its own
  filing date" wording is retracted at every site (U.113a); the FY1996 EPS enumeration moves from three bases to five
  and the "numerator unchanged" claim is retracted because the issuer restated FY1996's own loss upward by $469k
  (U.113b); U.95 is closed with its finding; §T gains six rows; the FY1997 margin pair is tagged `(PB)` at the three
  untagged `part_1` sites and §S's false universal about its own volume is narrowed. NO confidence was raised, NO
  claim restored, and §D's verdict — demand and revenue repeated, economics not shown to repeat, the test transferred
  to Stage 3 unperformed — stands unchanged. Neither audit may be re-run clean until the register owner applies the
  two appended conflicts.**
* `_MANIFEST.md` is owned by the orchestrator and was **not** edited by this pass; the deltas it must now pick up are §U 68→**72** blocks, conflicts.csv stage-2 rows 68→**72** (170 data rows in total), timeline.csv stage-2 rows 58→59, and claim records 476→**481** (304 + 105 + 72, measured 2026-09-26). **Handed off, not applied** — the manifest is not a Stage-2 repair path.


---

**PART LIST OF THE CLAIM-RECORD APPENDIX as at 2026-09-26** (mechanical §9.2/§9.3 budget split; sheet `03_quality_control/amz_claim_record_split.md`). The appendix is **three** volumes of one document with continuous ids — nothing re-based, renumbered or reused:

1. `stage_2_claim_records.md` — volume 1a: front matter + §A–§P; records **A01 → P90**, 304 records, 44,044 words.
1. `stage_2_claim_records_part_1b.md` — volume 1b: §Q–§T, the §U carry-forward stub and volume 1's coverage note; records **Q17 → T40**, 105 records, 17,340 words.
1. `stage_2_claim_records_part_2.md` — volume 2: §U conflict spine + the closing coverage note; records **U.44 → U.113**, 70 records, 27,908 words.

Stage-2 total: **479 records**, unchanged by the split. The two-volume statements earlier in this index are superseded by this register, not rewritten (method §14 rule 4).
