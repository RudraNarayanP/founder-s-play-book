# Microsoft Stage 1 -- volume index

Written by the Stage-1 merge pass on 2026-09-29 (`msft-s1-merge`). **One volume**, sections A-U continuous;
no section 9.3 split was triggered (34707 words against the 40,000-word soft target and the 60,000-word hard
cap). Company tier: **T2 core** (probe verdict, section 15.2), whose 22,000-word figure is a dispatch budget
and not a limit on written evidence (RD-122): nothing was trimmed, nothing was re-tiered on word count, and
`gates.py --tier core` therefore reports one budget finding on this volume, which is the adjudicated
non-defect.

## Volumes in order

| # | File | Words | Bytes | Sections contained | Status |
|---|---|---|---|---|---|
| 1 | `stage_1.md` | 34,707 | 235,007 | merge header + Stage-1 merge note, then Volume 1 (Header, Boundary, sections A-J and its register emission) and Volume 2 (sections K-U, 38 claim records, its register emission) | merged 2026-09-29 |
| - | `_parts/s1_p1.md` | 13,778 as emitted | 92,220 as emitted | superseded: carried verbatim into `stage_1.md`, plus a 177-word SUPERSEDED notice appended by the merge | SUPERSEDED, DO NOT RE-APPLY notice present |
| - | `_parts/s1_p2.md` | 19,203 as emitted | 131,795 as emitted | superseded: carried verbatim into `stage_1.md`, plus a 177-word SUPERSEDED notice appended by the merge | SUPERSEDED, DO NOT RE-APPLY notice present |

## Anchor ranges and where each row lives

The volume declares **14 anchors**: `U.1`-`U.4` and `U.6`-`U.15` (unpadded `U.n`, the Microsoft convention).
Every declared anchor has at least one register row and every register-cited anchor is declared: parity is
**14 narrative anchors <-> 14 register anchors**, 0 undeclared, 0 uncovered.

| range | what it holds | register home |
|---|---|---|
| `U.1`-`U.4` | the retracted Altair BASIC date (COR-01), the paid-fraction dispute, the 1975 assertion against 1975 silence, the 1980 close against the filed 1981 transition | `conflicts.csv` (rows carried from `research/B1_periodical_records.md`; `U.1` amended by part 1); cited again in `timeline.csv` `conflict_ref`, `quantitative.csv` notes, `sources.csv` `claim_supported` and `data_gaps.csv` |
| `U.6`-`U.12` | the third-party `Inc.` legend, who the partners were, the $40,000 against the $2/hour, who owned Altair BASIC, the APL outcome, Microsoft Consumer Products, ecosystem prints that are not counts | `conflicts.csv` (part 2), with `U.12` echoed in `channels.csv`, `validation.csv` and `timeline.csv` |
| `U.13`-`U.15` | the 1976 hardware posture against the 1980 hardware product, the Albuquerque-to-Bellevue interval, the 134/136 hit-line measurement | `conflicts.csv`; `U.14` mirrored in `decisions.csv`, `U.15` in `quantitative.csv` and `sources.csv` |
| retired | B1's fifth conflict id (136/134 hit lines) | folded into the `U.15` row on 2026-09-29; the token prints nowhere in the register layer, the retirement is printed inside the kept row's `residual_uncertainty` |

## Registers at the company root (canonical)

| register | cols | rows | requested | words | bytes |
|---|---|---|---|---|---|
| `timeline.csv` | 11 | 28 | 36 | 1,355 | 11,334 |
| `quantitative.csv` | 12 | 26 | 28 | 1,067 | 9,079 |
| `conflicts.csv` | 15 | 14 | 16 | 1,732 | 13,886 |
| `sources.csv` | 18 | 22 | 22 | 2,203 | 18,903 |
| `data_gaps.csv` | 8 | 13 | 20 | 1,670 | 12,206 |
| `validation.csv` | 11 | 7 | 9 | 502 | 3,965 |
| `failures.csv` | 11 | 5 | 5 | 183 | 1,658 |
| `decisions.csv` | 15 | 5 | 5 | 324 | 2,605 |
| `channels.csv` | 11 | 7 | 7 | 389 | 3,138 |
| **total** | | **127** | **148** | | |

## The six merge decisions this index records

1. **Three emissions, not two.** 148 rows requested (`research/B1_periodical_records.md` 55 + part 1 30 +
   part 2 63) -> **127 rows applied**, 21 emission rows folded into 18 collision groups, 0 refused.
   `merge_census.py` reports 63 because it globs `_parts/*.md` and reads fenced-`csv` blocks only: part 1
   fences plain and B1 lives under `research/`.
2. **Global `source_id`s minted centrally: `S4222`-`S4243` (22).** Checked free against every `sources.csv`
   in the corpus and a corpus-wide text scan before use; the nearest neighbours are Target's `S4201`-`S4221`
   and UnitedHealth's `S4301`-`S4331`, so the block is contiguous with neither and no id is re-used
   (RD-123). `D22` and `D23` were never emitted, so no id is minted for them. Alias map, global <- dossier-local:
   S4222<-D01 B1, S4223<-D02 B1, S4224<-D03 B1, S4225<-D04 B1, S4226<-D05 B1 (part 2's second FY1994 10-K
   passage unioned into its `relevant_passage`, no new row), S4227<-D06 B1, S4228<-D07 B1, S4229<-D08 B1,
   S4230<-D09 B1 (annotated as one identifier with S4238/S4243), S4231<-D10 B1, S4232<-D11 B1, S4233<-D12 B1,
   S4234<-D13 B1, S4235<-D14 P1, S4236<-D15 P1, S4237<-D16 P1 (deliberately NOT de-duplicated against S4222:
   same file, different author), S4238<-D17 P2, S4239<-D18 P2, S4240<-D19 P2, S4241<-D20 P2, S4242<-D21 P2,
   S4243<-D24 P2. Retired anchor id: B1's fifth conflict -> `U.15`. 90 citation cells re-pointed onto the
   global ids; every `sources.csv` row prints the local id it replaced, so prose citing `D09` still resolves.
3. **Column-width drift: 3 rows, re-joined at the printed split point, tagged COR-04**, 0 refused (part 1's
   amended `U.1` conflict row and its MITS-licence and APL-outcome gap rows).
4. **Validation against failure attribution by content**, not by column list -- the two registers share 11
   identical column names, which is what makes the census call them AMBIGUOUS. Six endorsement, payment and
   third-party-visibility signals to `validation.csv` (7 rows with part 1's three); five loss records (unpaid
   copying, the written substitute, the unauthorised resellers, the terminal-criticism letter, the unshipped
   APL line) to `failures.csv` (5 rows). Neither group was dropped.
5. **Empty cells: 0** except `quantitative.derived_arithmetic` on non-DERIVED rows, which section 13's
   per-column rule leaves empty and which all three emissions declare as their convention; every
   DERIVED/ESTIMATE row carries its arithmetic. `stage` carries only the literals stage1 (110), stage2 (6),
   stage3 (11); 0 numeric values found.
6. **One gate finding refused rather than repaired:** `keys` reads the OCR price string in section M.1 as a
   source token. It is the byte's damaged dollar sign ($435 list / $45 dealer, `byte-magazine-1980-12`
   l.38112-38113), whose carrier is `S4243`. Rewriting the quotation would break the byte-identical body
   slice; minting an id for a price would make it read as a document. Recorded as **COR-05** in
   `CORRECTIONS.md` and tagged into the 3 register rows that carry the passage.

Claim records: **38** (K01-K07, L01-L06, M01-M08, N01-N06, O01-O05, P01-P06), all in Volume 2; part 1 emits
none, which is the T2 shape its own header declares. Corrections reaching both the register layer and the
volume: **COR-01, COR-02, COR-03, COR-04, COR-05**. Sections not yet written for this company: `stage_2.md`,
`stage_3.md`, `final_report.md`, `adversarial_review.md`, `context_appendices.md`.
