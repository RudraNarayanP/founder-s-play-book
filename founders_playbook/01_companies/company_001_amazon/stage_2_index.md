# Amazon.com Stage 2 — volume index

One forensic document, split at section boundaries for the 60,000-word per-file cap (method §9.2/§9.3).
Nothing is duplicated across volumes and nothing is dropped: the four assembly parts under `_parts/`
remain the audit trail of who wrote which section, including the double-dispatch collision of
2026-09-24 (method §14.7).

| Volume | Sections | Words (pre-repair) | Words (post-repair, 2026-09-25 Audit 1) | Words (post-repair, 2026-09-25 Audit 2 citation) |
|---|---|---|---|---|
| `stage_2_part_1.md` | Header, STAGE BOUNDARY JUSTIFICATION, §A–§H, + the carried conventions block | 18,360 | 18,560 | 19,289 |
| `stage_2_part_2.md` | §I–§P (incl. §P.2 derived arithmetic) | 25,346 | 25,409 | 25,524 |
| `stage_2_part_3.md` | §Q–§U (+ §S.9 carried untried lists) | 37,423 | 39,760 | 40,385 |
| **Narrative total** | §A–§U | **81,129** | **83,729** | **85,198** |

*The third column was measured by whitespace tokens on 2026-09-25 after the AUDIT-2 citation repair pass; that
pass added in-cell correction and retraction notes (DEFECT-1/2/3/5/7/9) and deleted no text, so each volume grew.*

Word counts are whitespace tokens of the file as written. The growth in part_3 is the two §U blocks
and the §Q re-anchoring added by the Audit-1 chronology repair pass (see Status below); no text was
removed to offset it, and no volume approaches the 60,000-word cap.

Stage 1's equivalent single file (`stage_1.md`) is 49,545 words, so Stage 2 runs ~1.69× Stage 1 — the
growth is concentrated in §P (13,753 w) and §U (19,351 w before the repair pass), which is what a stage
with four SEC filing lineages and 70 live conflicts should look like.

## Numbering continuity

* Conflict blocks: **§U.44 → §U.113b** (Stage 1 owns U.1–U.43). **The spine emits 72 blocks — 70 numbered
  U.44–U.113 plus the two lettered addenda U.113a and U.113b — against 70 rows in `conflicts.csv`,** 1:1 with no
  duplicate and no orphan through U.113. **The two-row excess is declared, not repaired, and its history is a
  retraction:** the 2026-09-25 AUDIT-4/AUDIT-5 pass reported that it had appended two new blocks (an IPO price-walk
  re-key and the FY1996/FY1997 restatement pair) and RESERVED their register rows, but §U on disk ended at U.113 with
  **no `>>> CSV APPEND BLOCK: conflicts.csv` section and no RESERVED marker anywhere** in `stage_2_part_3.md`, and the
  two ids its prose cited are **Stage 3's**, so a Stage-2 reader following them landed in another stage's conflict
  (RD-079). Both conflicts are now **written** as the lettered addenda **U.113a and U.113b** at the foot of
  `stage_2_part_3.md` §U, per the U.111a precedent, with **nothing renumbered** (§9.3). `conflicts.csv` holds
  **70 Stage-2 rows** and stays there until the register owner appends U.113a/U.113b at `stage2` — which takes
  Stage-2 rows 70→**72**, the total 113→**115**, and restores equality at 72↔72. Full sheet:
  `03_quality_control/amazon_s2_dangling_refs_repair.md` (2026-09-26). **U.112 and U.113 were appended by the
  Audit-1 chronology repair pass of 2026-09-25**, each emitted together with its register row so the
  invariant never broke. **No id anywhere in the spine was re-based, renumbered or reused** (method §9.3).
* Metric IDs continue Stage 1's sequence in §P.
* Assembly-part record IDs (S2A-*, S2B-*, S2C-*, S2D-*, S2E-*) resolve to the dossiers in `research/`.
* Claim-record IDs: Stage-2 volume 1 carries **411** lettered records (A01–T40; §Q now Q17–**Q69**; the two §U
  records this line reserved at Stage-3 ids are now **U.113a/U.113b, minted 2026-09-26**) and
  volume 2 carries **72** conflict records (**U.44–U.113b**, i.e. U.44–U.113 plus the two lettered addenda) plus the
  U.111a addendum — **481** in all. **The 411/481 tally is the 2026-09-25 pass's own and was printed against 70
  blocks; this pass re-keys the two ids and does NOT re-verify the counts — the claim registrar owes them a recount.**
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
| conflicts.csv | 43 | **70 APPLIED** (the register holds 70 Stage-2 rows and the spine emits **72** blocks: U.44–U.113 plus the lettered addenda U.113a and U.113b, minted 2026-09-26, RD-079. **No CSV rows were emitted or RESERVED for them by the 2026-09-25 pass, contrary to that pass's report** — the register owner appends U.113a/U.113b at `stage2`, which takes Stage-2 rows 70→**72** and the total 113→**115**) | **113 now / 115 after the append** | 15 uniform |
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
* `_MANIFEST.md` is owned by the orchestrator and was **not** edited by this pass; the count deltas it must
  pick up are §U 68→70 blocks, conflicts.csv stage-2 rows 68→70, timeline.csv stage-2 rows 58→59, and
  claim records 476→479.
