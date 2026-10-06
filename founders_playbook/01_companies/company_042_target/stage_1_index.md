# stage_1_index.md — company_042_target, Stage 1

Index of the merged Stage-1 volume, built by the merge pass 2026-09-26 (`03_quality_control/target_s1_merge.md`).
Method §9.1/§9.3: one file per company per stage; parts are **volumes of one document**, numbering is
continuous across them, and nothing was renumbered to make a part look self-contained.

## Volumes

| order | file | words | bytes | sections contained | status |
|---|---|---|---|---|---|
| 1 | `stage_1.md` | 42,833 (37,507 at the merge; 38,489 after the 2026-09-29 repair pass; 41,534 at the 2026-09-30 recertification; re-measured after the 2026-09-30 round-3 pass) | 292,456 | merge header + merge note, then Volume 1 (Header, Boundary, §A–§H) then Volume 2 (§I–§U, claim records P1/P2 blocks, the three register-emission blocks) | **canonical**; **42,833 now exceeds the 40,000 soft target — the figure was already over it at the recertifier's 41,534 measurement, not a change introduced here — but the hard cap (60,000) is far off and §9.3's part-split is a soft-target judgment, not a mandate**: RD-122 ruled the density figure a *planning* budget and not a limit on written evidence, and the `budget`/`advisory` gate reports the overage as ADVISORY, not a defect; the volume stays one file |
| — | `_parts/s1_p1.md` | 15,467 | 105,781 | superseded intermediate, retained as the merge's audit trail; carried untouched, one dated `MERGED 2026-09-26` line appended | SUPERSEDED |
| — | `_parts/s1_p2.md` | 21,633 | 146,584 | superseded intermediate, same treatment | SUPERSEDED |

Section ranges and ownership: §Header/Boundary/§A–§H from volume 1; §I–§U and the P2 claim records from
volume 2; §K, §N and §U are mandatory at every tier and are present. Claim-record appendix blocks stay inside
their own volume (never split mid-block per §9.3). Cross-references use the `(Amazon S1 §D.1, part_1)` form
where they point into another company's split set.

## Anchor ranges

**Declared: `<!-- ANCHORS: U.001-U.037, U.101-U.103 -->` — 40 anchors, re-read from the carrier at `stage_1.md:1078` on 2026-10-06 (round-4/N-2). The 37 anchors (`U.001-U.037`) carried verbatim from volume 2's assembly note were the declared set at the merge and are retained here as that state's dated census (§14 rule 4), not as the current count.**
Volume 1 minted none, so no re-keying of the declared set was needed and `U.101-up` (the range volume 2
reserved against a sibling that had not yet written) **was left unused at the merge and is in use now: COR-24/RB-7 minted `U.101`, `U.102` and `U.103` on 2026-09-30 as keys for three formerly-unkeyed `data_gaps.csv` rows, and the declaration at `stage_1.md:1078` extended to match.** Coverage, checked mechanically
(`gates.py --checks anchors`: **40 narrative anchors ↔ 40 register anchors**, 46 distinct ids resolving — the gate this pass re-ran, `03_quality_control/target_s1_gates_round4.md`; the 37 ↔ 37 parity published here was the merge-state census, superseded and kept visible per §14 rule 4, and §14 rule 12 is why the correction costs more than it looks: a reader counting anchors from the stale line would "discover" three register rows with no anchor and chase a defect that is only a stale pointer):

| range | what it holds | where the register row lives |
|---|---|---|
| U.001–U.017 | live conflicts (§U.1) | `conflicts.csv` — one row per anchor (U.006 shares the row keyed U.003) |
| U.018–U.024 | documented nulls (§U.2) | `data_gaps.csv` |
| U.025–U.029 | UNANSWERED — route or tool failure, never an absence | `data_gaps.csv` + `sources.csv` S4218/S4219/S4220 |
| U.030–U.037 | UNTRIED routes, each with the command or archive that would settle it | `data_gaps.csv` |

Register cells that pointed at §U's *subsection numbers* (`section U.1` etc.) are not anchor citations; the 16
such cells were rewritten as block names so the parity test means what it says. `U.0`–`U.5` and the (formerly reserved)
`U.101`–`U.103`, minted by COR-24/RB-7 on 2026-09-30, are **live gap keys** citing three real `data_gaps.csv` rows (1963-64 openings, 1962-65 cost/land/vendor, payroll/wages/headcount); the reservation wording stood here until this pass and is retained as the pre-COR-24 state (§14 rule 4). `U.0`–`U.5` remain narrative prose only, and the gate reports them ADVISORY, not as defects. **Do not read "reserved" as current: `stage_1.md:1078` declares 40 ids and `stage_1.md:2298` says 40 declared.**

## Register counts (company root, all nine present)

`sources.csv` **25** × 18 · `quantitative.csv` **72** × 12 · `timeline.csv` 24 × 11 · `conflicts.csv` 18 × 15 ·
`data_gaps.csv` **23** × 8 · `decisions.csv` 3 × 15 · `validation.csv` 4 × 11 · `failures.csv` 1 × 11 ·
`channels.csv` 3 × 11 = **173 rows** (**157 at the merge → 164 on the 2026-09-29 repair pass (+7 `quantitative.csv`:
the six dropped `Q20` component rows under COR-09 plus the printed deduction total required by COR-12) → 172 at the
2026-09-30 recertification (+4 `sources.csv` under COR-20 and +4 `quantitative.csv` rows r69–r72 under COR-15) →
**173** after the 2026-09-30 round-3 pass minted `U.103` in `data_gaps.csv` (COR-24); no row was deleted by any
pass**). `stage` = `stage1` on
every row; headers byte-identical to `company_001_amazon/`; 0 empty cells; 0 duplicate primary keys; 0 dangling
`source_id`.

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
4. **Ids minted centrally.** Global `S4201`–`S4225` (company-scoped, 4-digit so `gates.py` resolves them;
   `S4222`–`S4225` added 2026-09-30 under COR-20 and shared with `company_011_microsoft`, tracked cross-company as
   task #31 — never re-minted here; RB-1/COR-23 corrected this line from the stale `S4201`–`S4221`);
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
5. **Corrections carried to the register layer** — COR-01…COR-06 at merge, 47 tagged rows; **COR-07…COR-14 added by
   the 2026-09-29 repair pass, COR-15…COR-24 by the 2026-09-30 round-3 lineage: 24 ids in total**, each reaching
   both the register layer and a stage volume (the
   `corrections` gate reconciles that: *"24 retraction ids; register layer reaches 24, volumes 24"* (re-run after the
   round-3 wiring, 2026-10-06). See
   `CORRECTIONS.md`. The FY1965 layer's period end **1966-01-29** re-bases B1's Q20 by superseding note inside the
   same cell; **COR-07 supersedes the December year-ends COR-01 itself wrote.**
6. **Nothing was trimmed to fit a limit**, and nothing in `_parts/` was rewritten: the two parts are byte-for-byte
   the pass that wrote them, plus one dated `MERGED` line each.

## Repair pass 2026-09-29 (`target-s1-repair`) — what moved, and what it did not

Report: `03_quality_control/target_s1_repairs.md`. Eight corrections were opened (COR-07 … COR-14) against the
three Stage-1 audits and the orchestrator's own re-verification in RD-125. Files touched: `quantitative.csv`,
`timeline.csv`, `conflicts.csv`, `data_gaps.csv`, `stage_1.md`, `stage_1_index.md`, `CORRECTIONS.md`,
`_MANIFEST.md`. **`sources.csv`, `sources/_index/_INDEX.md` and everything under `sources/` were not written**: the
provenance register belongs to a parallel agent and the archive is read-only to this pass (§14 rule 4). One defect
landed entirely inside `sources.csv` — the S4203 `relevant_passage` cell that drops the possessive from
`Target’s sales` — and is recorded as an **outbound correction at COR-13** rather than edited.

**Line numbers inside `stage_1.md` are stale below the edited anchors (§14 rule 12).** Six passages were edited
(§Boundary 4, §E.2, §K.3, §P.1, §T.2, §U.2 and the claim records B05 / E02 / P2-02), the volume grew from 37,507 to
38,489 words, and every pointer that addressed them by line number — including the auditors' `L226-227` and `L1240`
— now reads against a shifted file. Address them by the labels above. This pass could not re-key the pointers held
in `03_quality_control/`, which is outside its file set, and says so rather than pretending to have.

Rows before → after: `quantitative.csv` 61 → 68 · `timeline.csv` 24 → 24 · `conflicts.csv` 18 → 18 ·
`data_gaps.csv` 22 → 22 · `validation.csv` 4 · `failures.csv` 1 · `decisions.csv` 3 · `channels.csv` 3 · nine
registers **157 → 164**. No row was deleted; the two timeline rows changed identity in place (row 17 re-pointed from
`S4201` to `S4211` and re-classed, row 23 re-dated) with their withdrawn wording retained inside the same cells.
