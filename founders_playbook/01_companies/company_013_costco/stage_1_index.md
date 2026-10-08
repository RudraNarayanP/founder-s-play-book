# Costco Stage 1 — volume index

Written by the Stage-1 merge pass on 2026-09-30 (`costco-s1-merge`). **One volume**, sections continuous; no
§9.3 split was triggered (46,992 words against the 40,000-word soft target and the 60,000-word hard cap — the
volume sits in §9.2's amber band, which is *allowed to finish the stage as one file*). Company tier: **T2 core**
(`research/A3_intake_regrade.md` issued T3 PROVISIONAL with family (c) unmeasured; `research/A4_harvest_mine.md`
then returned two in-window `TIER1_CANDIDATE_TEXT` periodical items, which is the 2-family condition of §15.2).
The tier's 22,000-word figure is a dispatch budget and not a limit on written evidence (RD-122): nothing was
trimmed, nothing was re-tiered on word count, and `gates.py --tier core` reports the overage as an advisory
density note, not a defect.

## Volumes in order

| # | File | Words | Bytes | Sections contained | Status |
|---|---|---|---|---|---|
| 1 | `stage_1.md` | 46,992 | 297,182 | merge record (assembly, application, id map, folds, anchor parity, site marks, UNTRIED carry-forward, FETCH REQUEST), then **Volume 1** = Header, Boundary, §A–§F, claim records Boundary/A–F; then **Volume 2** = §G–§U (incl. the anchor block and the K09–K21 conflict section), claim records §G–§U, and `## Untried`; then **Volume 3** = the merge-pass register record | MERGED 2026-09-30, one file, amber band, no split |
| – | `_parts/s1_p1.md` | 19,694 as it now stands | 138,110 | Header, Boundary, §A–§F, claim records, 94-row register emission — **plus a `SUPERSEDED 2026-09-30` footer appended by the merge** | SUPERSEDED, read-only audit trail; body carried verbatim |
| – | `_parts/s1_p2.md` | 39,874 as it now stands | 265,229 | §G–§U, claim records, 105-row register emission, `## Untried` — **plus a `SUPERSEDED 2026-09-30` footer appended by the merge** | SUPERSEDED, read-only audit trail; body carried verbatim |

**What the merge did not carry into the prose volume.** The parts' fenced `csv` register blocks (20 blocks, 199
rows) are register data, not narrative: method §9.1(2) and §13 put them in CSV. They were **applied** to the nine
registers (191 rows on disk) and remain verbatim in `_parts/` as the emission record. Claim records **are**
narrative and all 116 of them are in `stage_1.md`.

## Section map and where each section lives

| section | lives in | note |
|---|---|---|
| Header, Boundary, §A–§F | Volume 1 (`stage_1.md`, part-1 slice) | boundary = two legs, opened 1976 and 1983, closed 1993-10-21 |
| §G–§K, §L–§S | Volume 2 (part-2 slice) | §L is the hindsight-firewall audit, §K the cannot-settle section |
| §T independence ledger, §U anchor block | Volume 2 | 32 anchors declared: U.101–U.115 conflicts, U.120–U.136 nulls and open routes |
| Claim records, part 1 (45 records) | Volume 1 | ids B01…F06, A-series and Boundary series, unchanged |
| Claim records, part 2 (71 records) | Volume 2 | ids G01…T03, KS-series, unchanged |
| `## Untried` | Volume 2, carried forward in full | 8 UNTRIED, 6 UNANSWERED, 2 EMPTY, 1 NOT KNOWABLE (§U coda's own tally) |
| Merge record + register record | front and back of `stage_1.md` | the only prose the merge wrote |

## Anchors and their register homes

| range | what it holds | register home |
|---|---|---|
| `U.101`–`U.111` | the thirteen part-2 conflicts: merger effective date, the fee schedule pair, format average size, club population, the FY1995 capital plan, the headcount correction, the state of incorporation, the Item 6 share row, the harvest-count drift, the "Price Club" brand/category error, the 13D/13G denominator | `conflicts.csv` (K09–K21), echoed in `timeline.csv`, `sources.csv` and `data_gaps.csv` |
| `U.112`, `U.113` | part 1's boundary-date conflict as narrowed, and part 1's 1975-against-1976 conflict unclosed | `conflicts.csv` K05 (address printed at merge, COR-04) and K01 (echoed in `timeline.csv`) |
| `U.114`, `U.115` | the item-count null corrected on held bytes; the brand-split estate count | `conflicts.csv` K16, K17; `quantitative.csv` notes |
| `U.120`–`U.136` | the documented nulls and open routes (founding capital, leg P founder, advertising spend, renewal rate, opening fee schedule, per-leg statements, the 1989 warehouse question, the convertible terms, the dilution note, the unread filings, the trade-periodical, documentary, web-archive, Chronicling America and HathiTrust routes, the two Google Books volumes, the Item 6 row) | `data_gaps.csv` (26 rows), with echoes in `channels.csv`, `failures.csv`, `validation.csv`, `timeline.csv`, `sources.csv` and `conflicts.csv` |

Parity measured on the final bytes: **32 declared anchors ↔ 32 distinct anchors cited in the register layer**, 0
undeclared, 0 declared-with-no-row.

## Registers at the company root (canonical)

| register | cols | rows on disk | rows requested from the parts | words | bytes |
|---|---|---|---|---|---|
| `sources.csv` | 18 | 14 | 17 | 2,145 | 18,453 |
| `quantitative.csv` | 12 | 46 | 46 | 1,540 | 15,617 |
| `timeline.csv` | 11 | 35 | 35 | 1,866 | 14,543 |
| `conflicts.csv` | 15 | 22 | 22 | 2,388 | 16,980 |
| `data_gaps.csv` | 8 | 26 | 24 | 1,729 | 12,237 |
| `decisions.csv` | 15 | 13 | 13 | 1,414 | 10,188 |
| `validation.csv` | 11 | 8 | 11 | 848 | 6,027 |
| `failures.csv` | 11 | 11 | 15 | 1,079 | 7,693 |
| `channels.csv` | 11 | 16 | 16 | 964 | 7,590 |
| **total** | – | **191** | **199** | – | – |

Difference explained: **10 rows folded as duplicates** (3 `sources.csv` per COR-01, 3 `validation.csv` and 4
`failures.csv` per COR-03) and **2 rows minted by the merge** into `data_gaps.csv` per COR-04. Headers are copied
column-for-column from `company_001_amazon`'s conformant registers; `stage` is the controlled literal `stage1` on
every row (0 numeric values to normalise); line endings are `\n` per §13 (Amazon's `conflicts.csv` carries CRLF,
which §13 overrides).

## Companion files

| File | Words | Contents |
|---|---|---|
| `CORRECTIONS.md` | 1,456 | COR-01 to COR-05, each printed in the register layer and in the volume |
| `_MANIFEST.md` | see file | §9.6 upload-safety register with live counts and the measured tier overshoot |
| `../../../03_quality_control/costco_s1_merge_notes.md` | see file | the merge's own record: census baseline, AMBIGUOUS-block attribution, id block, fold list, residue, gate findings |
| `../../../03_quality_control/costco_s1_gates.md/gates_company_013_costco.md` | see file | the mechanical gate report (the tool writes into a directory named by `--out`) |

**Cross-reference form.** Citations into this dossier use `(Costco S1 §D.2, part_1)` as both parts defined it;
`P1S01`–`P1S12` and `P2S01`–`P2S05` in the prose are dossier-local aliases resolved by `sources.csv` `notes` and
by the id map in the volume's merge record.
