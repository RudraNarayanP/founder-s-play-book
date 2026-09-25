# STAGE 1 INDEX — company_002_walmart (WAL-MART STORES, INC., 1945 → 1970-10-08)

*Ordered volume list, word counts and which sections live where (method §9.3). Written by the merge pass, 2026-09-26.*

Stage 1 exceeded the 60,000-word hard cap as one file (the three parts total **64,649** words), so it is split **at a section boundary** into two continuing volumes with **continuous numbering**. Nothing was trimmed to fit the cap, and no section letter, claim id, metric id or conflict id was renumbered to make a volume look self-contained (§9.3).

| Volume | Words | Sections contained |
|---|---|---|
| `stage_1.md` | 57,991 | Header, STAGE BOUNDARY JUSTIFICATION, §A–§U (part-1 header/boundary/§A–§D; part-2 §E–§L + its register-handoff block; part-3 §M–§U incl. its preamble and the §U canonical anchor set + §U.0.1 mapping table) |
| `stage_1_part_2.md` | 7,132 | UNTRIED ROUTES, CARRIED FORWARD; CLAIM RECORDS APPENDIX (§§M–U); part-3 >>> REGISTER ROWS FOR MERGE <<< block (audit trail) |

**Merged narrative: 65,123 words across 2 volumes** = 64,649 words of part text (byte-verified retained in full) + 474 words of merge headers. The §U canonical anchor set, and with it the whole `U.nnn` spine the `anchors` gate reads, sits in volume 1; the claim records and the carried-forward UNTRIED block continue in volume 2, whose heading says so.

## Where the stable labels live

- **§U.001–§U.048** live conflicts, and **§U.0.1** the mapping table for every local key ever used (U-C0/1, U-E/1, U-F/1, U-K/1, U-A2/1–10, U-A3/1–9, U-A4/1–9, U-A5/1, probe U-1/U-2/U-3, U-W-4/U-W-5, D-R03c, D-R09c, COR-A3-04, A3-002) — `stage_1.md`, §U.
- **§U.101–§U.116** documented nulls and **§U.201–§U.222** unanswered/untried routes — `stage_1.md`, §U.2 and §U.3; the route detail continues as `UNTRIED ROUTES, CARRIED FORWARD` in `stage_1_part_2.md`.
- **Claim records for §§M–U** — `stage_1_part_2.md`. Part 1’s dated record set (D-R01–D-R10 with its four `c` correction notes) stays in `stage_1.md` §D, where it was written.
- **Register-handoff blocks** stay where the parts put them: part 2’s after §L in `stage_1.md`; part 3’s at the end of `stage_1_part_2.md`. They are the merge’s audit trail, not live register content.

## Cross-reference form

`(Walmart S1 §D.1, stage_1.md)` — a pointer names the section letter and the volume, never a line number (§14 rule 12).

## Registers (company root)

| Register | Rows | Purpose |
|---|---|---|
| `sources.csv` | 47 | append-only provenance register |
| `conflicts.csv` | 39 | canonical U.nnn conflict register |
| `timeline.csv` | 59 | chronology register |
| `quantitative.csv` | 114 | metric register |
| `data_gaps.csv` | 52 | gaps, documented nulls, unanswered and untried routes |
| `decisions.csv` | 9 | founder decisions |
| `failures.csv` | 13 | negative signals and failures |
| `validation.csv` | 0 | validation signals — EMPTY register, named reason in _MANIFEST.md |
| `channels.csv` | 0 | acquisition channels — EMPTY register, named reason in _MANIFEST.md |

U.002–U.010 stay **reserved** and uncited, as §U.0 minted them; U.011 onward are all issued. `research/{sources,conflicts,timeline,quantitative}.csv` are the pre-merge registers, retained but superseded by the root copies (§9.6 / `gates.py` reads the root first).

