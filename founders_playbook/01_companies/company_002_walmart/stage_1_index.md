# STAGE 1 INDEX — company_002_walmart (WAL-MART STORES, INC., 1945 → 1970-10-08)

*Ordered volume list, word counts and which sections live where (method §9.3). Written by the merge pass, 2026-09-26.*

Stage 1 exceeded the 60,000-word hard cap as one file (the three parts total **64,649** words), so it is split **at a section boundary** into two continuing volumes with **continuous numbering**. Nothing was trimmed to fit the cap, and no section letter, claim id, metric id or conflict id was renumbered to make a volume look self-contained (§9.3).

| Volume | Words | Sections contained |
|---|---|---|
| `stage_1.md` | 59,516 | Header, STAGE BOUNDARY JUSTIFICATION, §A–§U (part-1 header/boundary/§A–§D; part-2 §E–§L + its register-handoff block; part-3 §M–§U incl. its preamble and the §U canonical anchor set + §U.0.1 mapping table). Front matter carries the 2026-09-26 identity-line repair (**COR-301/COR-302**) and the 2026-09-26 A6 re-census disposition paragraph (**COR-303/COR-304/COR-305/COR-306**) |
| `stage_1_part_2.md` | 7,132 | UNTRIED ROUTES, CARRIED FORWARD; CLAIM RECORDS APPENDIX (§§M–U); part-3 >>> REGISTER ROWS FOR MERGE <<< block (audit trail) |

**Merged narrative: 66,648 words across 2 volumes** = 64,649 words of part text (byte-verified retained in full) + 1,999 words written by the merge pass, the 2026-09-26 identity-line repair, and the 2026-09-26 A6 re-census paragraph
(**COR-303**–**COR-306**), which adds no narrative and renumbers nothing. No part text was cut to fit any cap.
`stage_1.md` is **59,516 words against the 60,000 hard cap (9.2): 484 words of headroom**, so the next pass that writes
into volume 1 must split rather than append (§9.3), and §9.6 forbids curing the pressure by trimming evidence. The §U
canonical anchor set, and with it the whole `U.nnn` spine the `anchors` gate reads, sits in volume 1; the claim records
and the carried-forward UNTRIED block continue in volume 2, whose heading says so.

## Where the stable labels live

- **§U.001–§U.048** live conflicts, and **§U.0.1** the mapping table for every local key ever used (U-C0/1, U-E/1, U-F/1, U-K/1, U-A2/1–10, U-A3/1–9, U-A4/1–9, U-A5/1, probe U-1/U-2/U-3, U-W-4/U-W-5, D-R03c, D-R09c, COR-A3-04, A3-002) — `stage_1.md`, §U.
- **§U.101–§U.116** documented nulls and **§U.201–§U.222** unanswered/untried routes — `stage_1.md`, §U.2 and §U.3; the route detail continues as `UNTRIED ROUTES, CARRIED FORWARD` in `stage_1_part_2.md`.
- **The declared anchor set** lives at `stage_1.md` U.0: an explicit `ANCHORS` declaration listing the **77** minted anchors `U.001`, `U.011`–`U.048`, `U.101`–`U.116`, `U.201`–`U.222` plus the three section labels the registers cite as prose (`U.0`, `U.2`, `U.3`). It is what the `anchors` gate reads instead of guessing from heading text; `U.1` and `U.4` are headings only and are deliberately not declared.
- **Claim records for §§M–U** — `stage_1_part_2.md`. Part 1’s dated record set (D-R01–D-R10 with its four `c` correction notes) stays in `stage_1.md` §D, where it was written.
- **Register-handoff blocks** stay where the parts put them: part 2’s after §L in `stage_1.md`; part 3’s at the end of
  `stage_1_part_2.md`. They are the merge’s audit trail, not live register content. **One emission was never censused by
  the merge and is applied now:** `research/A6_held_corpus_mine.md` §Records for merge (22 rows, four fenced blocks, marked
  `>>> REGISTER ROWS FOR MERGE <<<`) — see `CORRECTIONS.md` **COR-303**, and the id-collision repair of the nine numbers
  that emission proposed at **COR-304**. Its 22 rows are **16 minted + 6 folded with reasons + 0 dropped**.
- **Source ids `S0148`–`S0155`** were minted on the 2026-09-26 A6 re-census at the top of the issued range (never on an
  occupied number, §13); each carries the `A6-ALIAS` under which the dossier proposed a different number, and each live
  row `S0139`–`S0147` carries the matching redirect. The mine’s proposed **S0148 for the FY1973 report is void**: **S0102**
  has been that report’s own row since the pre-merge register (**COR-305**). Confidence on the landed fleet rows is carrier-specific, not uniform (**COR-306**): FY1973 = 64 / 55 / 9 are **High** on
`WALMART_AR_1974.txt` **Note 8**, which prints those values beside "January 31, 1973" inside the audited notes, while
FY1970 / FY1971 / FY1972 stay **Medium** because their years come only from the five-year table's column order and the
page image is UNTRIED (`S0150` names the renderings).

## Cross-reference form

`(Walmart S1 §D.1, stage_1.md)` — a pointer names the section letter and the volume, never a line number (§14 rule 12).

## Registers (company root)

| Register | Rows | Purpose |
|---|---|---|
| `sources.csv` | 55 | append-only provenance register (`S0101`–`S0155`; `S0148`–`S0155` minted by the 2026-09-26 A6 re-census, **COR-303**/**COR-304**) |
| `conflicts.csv` | 39 | canonical U.nnn conflict register (unchanged in count; **U.011**, **U.040**, **U.045** carry the three A6 conflict folds) |
| `timeline.csv` | 63 | chronology register (+4 A6 rows: 1970-10, 1973, 1974, 1946-1947) |
| `quantitative.csv` | 118 | metric register (+4 A6 fleet rows: FY1971 = 38, FY1973 = 64, FY1973 = 55, FY1973 = 9; FY1970/FY1972 carriers extended in place, not duplicated) |
| `data_gaps.csv` | 52 | gaps, documented nulls, unanswered and untried routes (untouched by the A6 re-census) |
| `decisions.csv` | 9 | founder decisions |
| `failures.csv` | 13 | negative signals and failures |
| `validation.csv` | 0 | validation signals — EMPTY register, named reason in _MANIFEST.md |
| `channels.csv` | 0 | acquisition channels — EMPTY register, named reason in _MANIFEST.md |

U.002–U.010 stay **reserved** and uncited, as §U.0 minted them; U.011 onward are all issued. `research/{sources,conflicts,timeline,quantitative}.csv` are the pre-merge registers, retained but superseded by the root copies (§9.6 / `gates.py` reads the root first).

