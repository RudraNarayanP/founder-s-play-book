# Cigna Stage 1 — volume index

Written by the Stage-1 merge pass on 2026-10-06 (`merge-cigna`). **One volume, one part, sections continuous**
— no §9.3 split was triggered (14,513 words against the 40,000-word soft target and the 60,000-word hard cap;
`gates.py --tier auto` reads the tier as **core (T2)** and reports the 22,000-word tier target as met, not
exceeded). Company tier **as issued by the probe and not re-tiered here**: **T2 core, PROVISIONAL** on the
lineage frame; **T3 register** on the strict-registrant frame. Both frames are carried as states; neither is
averaged.

## Volumes in order

| # | File | Words | Bytes | Contents | Status |
|---|---|---|---|---|---|
| 1 | `stage_1.md` | 14,513 | 94,432 | merge record (assembly, register application, id map COR-01, folds, anchor parity, two tier frames, carry-forward, COR-01…COR-03 propagation), then the author's body **unchanged and unre-numbered**: Header, Stage-boundary justification, §A–§U (incl. §U.1–§U.6), claim-record appendix (25 records A01…S01), `## UNTRIED` (9 items), then the merge's register-application record | MERGED 2026-10-06, one file, under the tier target |
| – | `_parts/s1_p1.md` | 16,016 | 114,204 | the whole emission: the same body plus the nine fenced register blocks (78 rows, l.492–l.651) — **plus a `SUPERSEDED 2026-10-06` footer appended by the merge**, which supersedes the placement and key-space of that emission only | **read-only**; superseded for the live layer by `stage_1.md` + the CSVs; no narrative word was corrected, so the footer says "placement and keys", and the corrections ledger is `CORRECTIONS.md` |
| – | `CORRECTIONS.md` | 1,076 | 7,435 | COR-01 id supersession · COR-02 validation/failures binding · COR-03 the probe's withdrawn 17:20 zero-count/T3-only claim · "Not corrected, and why" | LIVING — append, never rewrite history |
| – | `research/A_chronology_feasibility.md` | 7,190 | 48,751 | the probe dossier that issued the window, the five-family verdict and both tier frames | scope of record (not touched by this pass) |
| – | `research/A4_harvest_mine.md` | 833 | 5,611 | the harvest-mine census carrier (96 / 12 / 81 as re-read by the author; 79 / 12 / 65 as the probe caught it) | measurement record (not touched) |

**What the merge did not carry into the prose volume.** The part's nine fenced `csv` blocks are register data,
not narrative (method §13): all **78 rows** were applied to the nine CSVs at this directory root and are not
reprinted in `stage_1.md`, where the heading now reads `## Register rows for merge — APPLIED TO THE NINE CSVs`.
The verbatim text stays in `_parts/s1_p1.md` as the emission of record. Claim records **are** narrative and all
25 remain in the volume.

## Section map — where each section lives (letters are the author's; nothing was renumbered)

| section | lives in | note |
|---|---|---|
| Header + MERGE RECORD + COR propagation | `stage_1.md`, head | the only prose the merge wrote |
| Stage boundary justification | `stage_1.md` | three rows: the T2 lineage frame, the **strict-registrant T3 reading**, stages 2–3 out of scope |
| §A–§S | `stage_1.md` | §K.1–§K.3 money, §P the 15-row metrics table, §Q the 14-row micro-timeline, §R the 1995-12-31 snapshot, §S gaps |
| §T source/provenance table | `stage_1.md` | CG01–CG16 with the independence ledger; keys bind to S4407–S4422 via the merge record's map |
| §U.1–§U.6 | `stage_1.md` | the declared anchor set (`<!-- ANCHORS: U.1-U.6 -->`), 1:1 with `conflicts.csv` |
| Claim-record appendix | `stage_1.md` | 25 records A01…S01, `Conflicts:` keyed to U.1–U.6 |
| `## UNTRIED` (9 items) | `stage_1.md`, carried verbatim from the part | states TRIED–ANSWERED / UNANSWERED / UNTRIED distinctly; names FR-1…FR-8 with the closing commands |
| Register application record | `stage_1.md`, foot | rows per register with words/bytes and the integrity checks |

## Anchors and their register homes (parity proven by census, not by assertion)

| anchor | what it holds | register home |
|---|---|---|
| `U.1` | "incorporated in Delaware in 1981" (a recital about Cigna Corporation) vs the registrant's own identity as Halfmoon Parent, Inc., renamed 2018-12-20; the registrant's incorporation date printed nowhere | `conflicts.csv` U.1; echoed in `timeline.csv` (3 rows: UNKNOWN birth, 2018-05-16 floor, 2018-12-20 closing) and `sources.csv` S4407/S4408 |
| `U.2` | 1792: whose origin and what class of statement — one retrospective self-report, 2 occurrences corpus-wide, capped Medium, never a founding date for the registrant | `conflicts.csv` U.2; `timeline.csv` 1792 row; `quantitative.csv` census row; `sources.csv` S4410 |
| `U.3` | the 1982 combination (no held byte) and the 1850s-1872 second ancestor (never queried) — inherited assertion vs query-scope silence | `conflicts.csv` U.3; `timeline.csv` 1982 hypothesis row; `data_gaps.csv` rows 3 and 4 |
| `U.4` | machine tier read vs issued tier (T3 tie-break vs T2 core PROVISIONAL) | `conflicts.csv` U.4; `sources.csv` S4422 |
| `U.5` | harvest census movement 79/12/65 → 96/12/81, both readings preserved | `conflicts.csv` U.5; `sources.csv` S4421; `quantitative.csv` census row |
| `U.6` | shelf-vs-family miscount: the INA 1979 annual report is Tier-1 corporate print stored on the periodicals shelf | `conflicts.csv` U.6; `timeline.csv` 1994/95 row; `sources.csv` S4410/S4413 |

**Parity measured on the final bytes:** 6 declared anchors ↔ 6 `conflicts.csv` rows keyed U.1–U.6, **0 orphans
in either direction**, proven by `merge_census.py` (`conflicts.csv | requested 6 | present 6 | missing 0`) and
by `gates.py` (`anchors parity — 6 narrative anchors <-> 6 register anchors`).

## Registers at the company root (canonical)

| register | cols | data rows | rows requested | words | bytes |
|---|---|---|---|---|---|
| `sources.csv` | 18 | 16 | 16 | 872 | 9,346 |
| `quantitative.csv` | 12 | 15 | 15 | 353 | 3,511 |
| `timeline.csv` | 11 | 14 | 14 | 441 | 4,241 |
| `data_gaps.csv` | 8 | 12 | 12 | 404 | 3,381 |
| `conflicts.csv` | 15 | 6 | 6 | 424 | 3,606 |
| `failures.csv` | 11 | 6 | 6 | 223 | 2,139 |
| `validation.csv` | 11 | 4 | 4 | 150 | 1,503 |
| `decisions.csv` | 15 | 3 | 3 | 173 | 1,715 |
| `channels.csv` | 11 | 2 | 2 | 90 | 908 |
| **total** | — | **78** | **78** | 3,130 | 30,350 |

Counts in this table were measured after the COR-01…COR-03 annotations landed and are re-published live in
`_MANIFEST.md`; `_MANIFEST.md` governs if the two ever disagree.

## Reading order

1. `stage_1.md` merge record (what was applied, which ids, which corrections, what is UNTRIED).
2. `stage_1.md` §boundary → §A → §B (the three lines: ancestor / asserted combination / registrant).
3. §C–§S for the substance; §T for provenance and independence; §U for the six conflicts.
4. The claim-record appendix for the verbatim passages behind anything load-bearing.
5. `CORRECTIONS.md` before reusing any key. The registers last — they are the same 78 rows in structured form.
