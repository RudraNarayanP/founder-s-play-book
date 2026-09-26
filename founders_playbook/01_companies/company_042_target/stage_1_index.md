# stage_1_index.md — company_042_target, Stage 1

Index of the merged Stage-1 volume, built by the merge pass 2026-09-26 (`03_quality_control/target_s1_merge.md`).
Method §9.1/§9.3: one file per company per stage; parts are **volumes of one document**, numbering is
continuous across them, and nothing was renumbered to make a part look self-contained.

## Volumes

| order | file | words | bytes | sections contained | status |
|---|---|---|---|---|---|
| 1 | `stage_1.md` | 37,507 | 255,104 | merge header + merge note, then Volume 1 (Header, Boundary, §A–§H) then Volume 2 (§I–§U, claim records P1/P2 blocks, the three register-emission blocks) | **canonical**; 37,507 < 40,000 soft target, so no §9.3 part-split was triggered (hard cap 60,000) |
| — | `_parts/s1_p1.md` | 15,467 | 105,781 | superseded intermediate, retained as the merge's audit trail; carried untouched, one dated `MERGED 2026-09-26` line appended | SUPERSEDED |
| — | `_parts/s1_p2.md` | 21,633 | 146,584 | superseded intermediate, same treatment | SUPERSEDED |

Section ranges and ownership: §Header/Boundary/§A–§H from volume 1; §I–§U and the P2 claim records from
volume 2; §K, §N and §U are mandatory at every tier and are present. Claim-record appendix blocks stay inside
their own volume (never split mid-block per §9.3). Cross-references use the `(Amazon S1 §D.1, part_1)` form
where they point into another company's split set.

## Anchor ranges

**Declared: `<!-- ANCHORS: U.001-U.037 -->` — 37 anchors, carried verbatim from volume 2's assembly note.**
Volume 1 minted none, so no re-keying of the declared set was needed and `U.101-up` (the range volume 2
reserved against a sibling that had not yet written) was left unused. Coverage, checked mechanically
(`gates.py --checks anchors`: 37 narrative anchors ↔ 37 register anchors):

| range | what it holds | where the register row lives |
|---|---|---|
| U.001–U.017 | live conflicts (§U.1) | `conflicts.csv` — one row per anchor (U.006 shares the row keyed U.003) |
| U.018–U.024 | documented nulls (§U.2) | `data_gaps.csv` |
| U.025–U.029 | UNANSWERED — route or tool failure, never an absence | `data_gaps.csv` + `sources.csv` S4218/S4219/S4220 |
| U.030–U.037 | UNTRIED routes, each with the command or archive that would settle it | `data_gaps.csv` |

Register cells that pointed at §U's *subsection numbers* (`section U.1` etc.) are not anchor citations; the 16
such cells were rewritten as block names so the parity test means what it says. `U.0`–`U.5` and the reserved
`U.101` remain as narrative prose only, and the gate reports them ADVISORY, not as defects.

## Register counts (company root, all nine present)

`sources.csv` 21 × 18 · `quantitative.csv` 61 × 12 · `timeline.csv` 24 × 11 · `conflicts.csv` 18 × 15 ·
`data_gaps.csv` 22 × 8 · `decisions.csv` 3 × 15 · `validation.csv` 4 × 11 · `failures.csv` 1 × 11 ·
`channels.csv` 3 × 11 = **157 rows**. `stage` = `stage1` on every row; headers byte-identical to
`company_001_amazon/`; 0 empty cells; 0 duplicate primary keys; 0 dangling `source_id`.

## Merge decisions

1. **No split.** 36,954 words across the parts → 37,507 merged. Amber never reached, so §9.3 did not fire.
   Splitting a file that fits would have broken "one file per company per stage" for no reason.
2. **Rows applied from three emissions, not two** (47 + 79 from the parts, 65 from
   `research/B1_dayton_print_records.md`), because both parts write their rows *against* B1's series ("IDs
   continue B1's Q-series", "B1's thirteen timeline rows already carry the estate and offering sequences",
   "the merge applies both sets"). Applying only the stated 126 would have silently dropped B1's store-and-group
   series and 13 timeline rows.
3. **34 emissions folded into 28 collision groups; 0 refused.** In each group one row is kept and the aliased
   emission's distinct wording is appended in place with a printed `MERGE[...]` marker. Same-fact pairs include
   P1K10 ≡ K8 → **U.011**, p1's `parent_net_income` ≡ p2's re-based row, p1's 44-percent row ≡ p2's
   `target_unit_sales_growth_rate`, p1's 127,000 sq ft average ≡ p2's, and B1's Q20 ≡ p2's 186,166,671 row.
4. **Ids minted centrally.** Global `S4201`–`S4221` (company-scoped, 4-digit so `gates.py` resolves them);
   200 source-token and 63 conflict-key re-pointings inside the registers. Retired local ids are kept as
   aliases in the replacing row's `notes` cell — never deleted:
   S4201←P1S01+B1S01 · S4202←P1S02+B1S02+P2S01 · S4203←P1S03+B1S03 · S4204←B1S04 · S4205←B1S05 ·
   S4206←P1S04+B1S06 · S4207←B1S07 · S4208←B1S08 · S4209←P2S08+B1S09 · S4210←B1S10 · S4211←B1S11 ·
   S4212←B1S14 · S4213←B1S12 · S4214←B1S13 · S4215←P1S05 · S4216←P2S05+P1S06 · S4217←P2S06+P1S07 ·
   S4218←P2S02+P1S08 · S4219←P2S03 · S4220←P2S04 · S4221←P2S07.
   Conflict keys: `K1→U.001, K2→U.002, K3→U.003, K4→U.004, K5→U.005, K4b→U.007, K6→U.008, K7→U.009,
   K8→U.011, K9→U.010, K10→U.012 … K15→U.017, P1K10→U.011, P1K11→K16, P1K12→K17`.
   **The part prose still cites the local carriers it was written against**; that is deliberate (§13 makes
   dossier-local ids legal inside a dossier, and §9.3/§14 rule 12 forbid renumbering and line-number
   addresses). The register plus this map are the only place global uniqueness lives.
5. **Corrections carried to the register layer** — COR-01…COR-06, 47 tagged rows; see `CORRECTIONS.md`. The
   FY1965 layer's period end **1966-01-29** re-bases B1's Q20 by superseding note inside the same cell.
6. **Nothing was trimmed to fit a limit**, and nothing in `_parts/` was rewritten: the two parts are byte-for-byte
   the pass that wrote them, plus one dated `MERGED` line each.
