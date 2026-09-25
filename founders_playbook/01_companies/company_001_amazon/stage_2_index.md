# Amazon.com Stage 2 — volume index

One forensic document, split at section boundaries for the 60,000-word per-file cap (method §9.2/§9.3).
Nothing is duplicated across volumes and nothing is dropped: the four assembly parts under `_parts/`
remain the audit trail of who wrote which section, including the double-dispatch collision of
2026-09-24 (method §14.7).

| Volume | Sections | Words |
|---|---|---|
| `stage_2_part_1.md` | Header, STAGE BOUNDARY JUSTIFICATION, §A–§H, + the carried conventions block | 18,360 |
| `stage_2_part_2.md` | §I–§P (incl. §P.2 derived arithmetic) | 25,346 |
| `stage_2_part_3.md` | §Q–§U (+ §S.9 carried untried lists) | 37,423 |
| **Narrative total** | §A–§U | **81,129** |

Stage 1's equivalent single file (`stage_1.md`) is 49,545 words, so Stage 2 runs ~1.63× Stage 1 — the
growth is concentrated in §P (13,753 w) and §U (19,351 w), which is what a stage with four SEC filing
lineages and 68 live conflicts should look like.

## Numbering continuity

* Conflict blocks: **§U.44 → §U.111** (Stage 1 owns U.1–U.43). 68 blocks ↔ 68 rows in `conflicts.csv`.
* Metric IDs continue Stage 1's sequence in §P.
* Assembly-part record IDs (S2A-*, S2B-*, S2C-*, S2D-*, S2E-*) resolve to the dossiers in `research/`.

## Registers — Stage 2 rows applied 2026-09-25

The `>>> CSV APPEND BLOCK` sections of `_parts/s2_p4.md` were applied to the nine registers by the
orchestrator, validated before writing: header equality with the §13 schema, uniform field count per row,
no duplicate `conflict_id` or `source_id`, `derived_arithmetic` populated on every DERIVED row, and stage
values checked. That pass left every register holding both stages, which is intended — the registers are
per-company, not per-stage.

| Register | Stage 1 rows | Stage 2 added | Total |
|---|---|---|---|
| conflicts.csv | 43 | 68 | 111 |
| quantitative.csv | 111 | 82 | 193 |
| timeline.csv | 57 | 58 | 115 |
| validation.csv | 29 | 11 | 40 |
| failures.csv | 33 | 13 | 46 |
| decisions.csv | 15 | 10 | 25 |
| channels.csv | 15 | 8 | 23 |
| sources.csv | 102 | 11 | 113 |
| data_gaps.csv | 23 | 22 | 45 |

## Status of this stage

`RECONSTRUCTION`. Not audited. The five Stage-2 gates (chronology, citation, numbers, hindsight,
adversarial) have not run, and per method §11 the stage cannot be called complete until they do — with
auditors who wrote none of the text they audit. The claim-record appendix (`stage_2_claim_records.md`) is
also not yet built; Stage 1's carries 432 records and Stage 2 needs its equivalent.
