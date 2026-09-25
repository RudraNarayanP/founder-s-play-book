# Amazon.com Stage 2 — volume index

One forensic document, split at section boundaries for the 60,000-word per-file cap (method §9.2/§9.3).
Nothing is duplicated across volumes and nothing is dropped: the four assembly parts under `_parts/`
remain the audit trail of who wrote which section, including the double-dispatch collision of
2026-09-24 (method §14.7).

| Volume | Sections | Words (pre-repair) | Words (post-repair, 2026-09-25) |
|---|---|---|---|
| `stage_2_part_1.md` | Header, STAGE BOUNDARY JUSTIFICATION, §A–§H, + the carried conventions block | 18,360 | 18,560 |
| `stage_2_part_2.md` | §I–§P (incl. §P.2 derived arithmetic) | 25,346 | 25,409 |
| `stage_2_part_3.md` | §Q–§U (+ §S.9 carried untried lists) | 37,423 | 39,760 |
| **Narrative total** | §A–§U | **81,129** | **83,729** |

Word counts are whitespace tokens of the file as written. The growth in part_3 is the two §U blocks
and the §Q re-anchoring added by the Audit-1 chronology repair pass (see Status below); no text was
removed to offset it, and no volume approaches the 60,000-word cap.

Stage 1's equivalent single file (`stage_1.md`) is 49,545 words, so Stage 2 runs ~1.69× Stage 1 — the
growth is concentrated in §P (13,753 w) and §U (19,351 w before the repair pass), which is what a stage
with four SEC filing lineages and 70 live conflicts should look like.

## Numbering continuity

* Conflict blocks: **§U.44 → §U.113** (Stage 1 owns U.1–U.43). **70 blocks ↔ 70 rows in `conflicts.csv`**,
  1:1 with no duplicate and no orphan, re-verified by read-back. **U.112 and U.113 were appended by the
  Audit-1 chronology repair pass of 2026-09-25**, each emitted together with its register row so the
  invariant never broke. **No id anywhere in the spine was re-based, renumbered or reused** (method §9.3).
* Metric IDs continue Stage 1's sequence in §P.
* Assembly-part record IDs (S2A-*, S2B-*, S2C-*, S2D-*, S2E-*) resolve to the dossiers in `research/`.
* Claim-record IDs: Stage-2 volume 1 carries **409** lettered records (A01–T40; §Q now Q17–**Q69**) and
  volume 2 carries **70** conflict records (**U.44–U.113**) plus the U.111a addendum — **479** in all.

## Registers — Stage 2 rows applied 2026-09-25

The `>>> CSV APPEND BLOCK` sections of `_parts/s2_p4.md` were applied to the nine registers by the
orchestrator, validated before writing: header equality with the §13 schema, uniform field count per row,
no duplicate `conflict_id` or `source_id`, `derived_arithmetic` populated on every DERIVED row, and stage
values checked. That pass left every register holding both stages, which is intended — the registers are
per-company, not per-stage.

| Register | Stage 1 rows | Stage 2 added | Total data rows | Field count |
|---|---|---|---|---|
| conflicts.csv | 43 | **70** (was 68: +U.112 +U.113) | **113** | 15 uniform |
| quantitative.csv | 111 | 82 | 193 | uniform (untouched by this pass) |
| timeline.csv | 57 | **59** (was 58: +1 `(POST-BOUNDARY)` 1997-06 row) | **116** | 11 uniform |
| validation.csv | 29 | 11 | 40 | uniform (untouched) |
| failures.csv | 33 | 13 | 46 | uniform (untouched) |
| decisions.csv | 15 | 10 | 25 | uniform (untouched) |
| channels.csv | 15 | 8 | 23 | uniform (untouched) |
| sources.csv | 102 | 11 | 113 | uniform (untouched) |
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
* `_MANIFEST.md` is owned by the orchestrator and was **not** edited by this pass; the count deltas it must
  pick up are §U 68→70 blocks, conflicts.csv stage-2 rows 68→70, timeline.csv stage-2 rows 58→59, and
  claim records 476→479.
