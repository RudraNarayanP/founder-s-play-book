# _MANIFEST — company_004_apple (Apple Computer Company)

**Counts regenerated 2026-09-26** by the Stage-1 merge pass (`apple-s1-merge`), which assembled `stage_1.md` +
`stage_1_part_2.md` from `_parts/s1_p1…3.md` and created the five missing registers. Words are whitespace
tokens (`wc -w`-equivalent); bytes are file size. Per `00_METHOD_AND_STYLE.md` §9.6 this register exists so a
file can be checked against its ceiling before handoff or upload. **Nothing here is a cleanup target (§14 rule 4)**:
the superseded `_parts/`, the `sources/` archive, the `research/` dossiers and the harvester run records in
`../../tools/` all stay exactly where they are, and nothing in this company was deleted, moved or renamed on this pass.

**Which ceiling governs which file.** §9.1's hard upload ceiling (500,000 words / 200 MB) governs every file,
primaries included; §9.2's **60,000-word cap** governs the stage volumes and their deliverables. The merged Stage-1
document measured **65,250 words**, over the cap, so §9.3 split it at one section boundary into two continuing
volumes — **no content was cut to fit**, and §9.6's prohibition on trimming evidence is why the split rather than an
edit is the response to the cap.

## Deliverables of this company

| File | Words | Bytes | Sections contained | Upload batch | Status |
|---|---|---|---|---|---|
| `stage_1.md` | **57,502** | 375,019 | Volume 1 of 2: Header + merge note, STAGE BOUNDARY JUSTIFICATION, §A–§U (incl. the S1P1/S1P2 claim-record blocks and part 2's register-request block) | 1 | MERGED 2026-09-26 · 96% of the 60,000 cap — amber §9.2, legal |
| `stage_1_part_2.md` | **8,834** | 65,846 | Volume 2 of 2, numbering continuous: consolidated `Untried routes` (§X continuation), part 3 handoff, part 3 register-request blocks | 1 | MERGED 2026-09-26 · under cap |
| `stage_1_index.md` | **1,472** | 9,664 | Volume map, key/collision map, register inventory, refusals and repairs, parity statement | 1 | WRITTEN 2026-09-26 |
| `CORRECTIONS.md` | **1,449** | 9,593 | Correction register: **COR-01…COR-05**, standing positions, untouched-on-this-pass list | 1 | **MINTED 2026-09-26** by the repair pass; the `corrections` gate previously DID NOT RUN for Apple |
| `_MANIFEST.md` | (this file, written last) | — | Directory register | 1 | WRITTEN 2026-09-26; **updated 2026-09-26 after the repair pass**; not self-measured |
| `stage_2.md`, `stage_3.md`, `final_report.md`, `adversarial_review.md`, `context_appendices.md` | — | — | — | 1 | **NOT STARTED** — Stage 1 only was in scope on this pass |

## Registers (all in `research/`, where this company's registers live until assembly; `gates.py::locate()` reads root then `research/`)

| File | Rows | Bytes | Header | Upload batch | Status |
|---|---|---|---|---|---|
| `research/conflicts.csv` | **38** | 30,589 | §13, 15 cols (identical to Amazon's modulo Amazon's own CRLF) | 1 | 13 legacy `U-A2-*` rows untouched + 25 canonical `U.nnn` rows appended 2026-09-26 |
| `research/data_gaps.csv` | **35** | 14,489 | byte-identical to Amazon's | 1 | **created** 2026-09-26 (5 from s1_p2 + 30 anchor-keyed `U.025–U.054`) |
| `research/quantitative.csv` | **44** | 9,940 | identical to Amazon's, 12 cols | 1 | 30 legacy + 14 appended (6 s1_p2, 8 s1_p3) |
| `research/timeline.csv` | **30** | 9,178 | identical to Amazon's, 11 cols | 1 | 23 legacy + 7 appended, `CS-01`/`CS-05` local keys re-pointed |
| `research/sources.csv` | **23** | 16,660 | identical to Amazon's, 18 cols | 1 | 13 `A2S-01…13` untouched + 10 appended under centrally assigned `S1M-01…S1M-10` (§9.4 append-only) |
| `research/validation.csv` | **6** | 2,787 | byte-identical to Amazon's | 1 | **created** 2026-09-26 (6 rows from s1_p2) |
| `research/failures.csv` | **6** | 2,484 | byte-identical to Amazon's | 1 | **created** 2026-09-26 (6 rows from s1_p3) |
| `research/decisions.csv` | **4** | 3,784 | byte-identical to Amazon's | 1 | **created** 2026-09-26 (4 rows from s1_p3) |
| `research/channels.csv` | **0** | 108 | byte-identical to Amazon's | 1 | **created** 2026-09-26, header only — no part requested a channel row and the merge invents none |

**Stage vocabulary (§13, RD-048/RD-075).** Registers carry **186** data rows in total and every `stage` cell is the
controlled literal `stage1` (or `stage2` in two pre-existing `timeline.csv` rows that record the December 1980 /
February 1981 outer-edge events, which the dossier that wrote them staged as Stage 2). **Numeric stage values found
and normalised on this pass: 0.** One semantic mismatch is recorded rather than rewritten: part 3's out-of-window
1980-12 cap-table row is staged `stage1` by its requester while `timeline.csv` holds the same event as `stage2`;
both stay, and the audit pass decides.

## Inputs retained as the audit trail (`_parts/`, not edited — `SUPERSEDED 2026-09-26` appended to each)

| File | Words | Bytes | Contained | Status |
|---|---|---|---|---|
| `_parts/s1_p1.md` | 17,066 | 110,426 | Header, boundary, §A–§D, S1P1-01…34, S1P1-CF-01…10, handoff | SUPERSEDED → `stage_1.md`; its three requested self-corrections carried to the audit pass, not applied here |
| `_parts/s1_p2.md` | 17,165 | 113,815 | §E–§L, S1P2-01…16, 27 requested rows | SUPERSEDED → `stage_1.md` |
| `_parts/s1_p3.md` | 31,000 | 209,736 | §M–§U (U.001–U.055), §X untried, handoff, 85 requested rows | SUPERSEDED → `stage_1.md` (§M–§U) + `stage_1_part_2.md` (tail) |

Word totals of the parts **as released**, before any `SUPERSEDED` marker; the repair pass appended three such markers (**+247 words** across `_parts/`, append-only, no rewrite):
64,744 whitespace tokens; merged 65,250 = 64,744 − 70 scaffolding + 576 added headers/merge note; **after the 2026-09-26 repair pass the merged volumes total 66,336 (57,502 + 8,834)** — 1,086 words of corrections, re-measurements and propagation text, no evidence cut. Record census
identical across the two: 66 claim records, 16 part-local conflict keys, 57 `U.nnn` tokens, 167 dossier keys
(1,391 occurrences).

## Evidence base

`research/` dossiers (not owned by this pass, listed for upload counting): `A_chronology_feasibility.md` 17,617 w ·
`A2_periodical_archive_mine.md` 29,129 w · `B_founder_forensics.md` 25,713 w · `C_corporate_legal_org.md` 18,418 w ·
`D_adversarial.md` 11,113 w. `sources/` holds **41** retrievable primary documents (the FY1994 Form 10-K text and
EDGAR probes, the cached BYTE 1976/1977/1981 and Homebrew runs, the collector-registry pages, retrieval logs) plus
its `_RETRIEVAL_LOG.md`; none was touched, and the largest is far below the §9.1 ceiling.

**Gate status on this pass.** `tools/gates.py --company-dir … --checks csv,keys,anchors,budget` — before the merge
`Findings: 0 | Passes: 8`, with `anchors` reporting `no register anchors found — UNANSWERED, not passed`; after the
merge `Findings: 0 | Passes: 18`, with `anchors parity 55 narrative anchors <-> 55 register anchors` and every
register width-clean. **Known gate defect for the audit pass:** `gates.py`'s `NARR_GLOBS["stage1"]` lists only
`stage_1.md` and has no `stage_1_part_*.md` entry (its stage-2 and stage-3 lists do), so on any future Stage-1 split
the anchors gate reads volume 1 alone — which is why this document was cut after §U rather than before it.

## Repairs applied on this path (2026-09-26, apple-s1-repair)

Five retractions, each reaching registers **and** volumes, recorded in `CORRECTIONS.md`: **COR-01** the §Q
1977-01-19 row's window label and the row count resting on it; **COR-02** BYTE's volume-wide Tier-1 rank,
re-tiered per item (periodical prose Tier 3, first-party and directory artifacts Tier 1); **COR-03**
S1P1-05/06's "inside the window" wording and their `Source date: UNKNOWN`; **COR-04** post-edge marking
extended to seven `timeline.csv` rows, no new stage literal; **COR-05** the §6 `RETROSPECTIVE SOURCE
(1977-04)` tag at §H.2. `gates.py` (csv,keys,anchors,budget,corrections): **0 findings, 20 passes**, anchor
parity held at **55 ↔ 55**; the `corrections` check moved from DID NOT RUN to **5 ids, registers 5,
volumes 5**. Registers were rewritten by CSV parser, not by hand: widths unchanged (30×11, 44×12, 38×15,
23×18, 6×11), row counts unchanged, `stage` cells untouched.
