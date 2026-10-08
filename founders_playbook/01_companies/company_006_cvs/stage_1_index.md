# CVS (company_006_cvs) Stage 1 — volume index

Written by the Stage-1 merge pass on 2026-10-07 (`merge-cvs`). **One volume, one part, sections continuous** — no
§9.3 split (19,520 words against the 40,000 soft target and 60,000 hard cap; `gates.py --tier core` reads the tier
as **core (T2)** and reports the 22,000-word tier target as met, 89%). Company tier **as issued by the probe and
not re-tiered here**: whole dispatched window **T2 core**; **S1a/S1b/S1c = T3 register**, **S1d = T2 core**.
**The merger did not audit and does not certify.**

## Volumes in order

| # | File | Words | Bytes | Contents | Status |
|---|---|---|---|---|---|
| 1 | `stage_1.md` | 19,520 | 127,222 | MERGE RECORD (assembly, 126-row application, `PROV-CVS`→S4431–S4448 id map, geometry + foreign-key fixes, anchor parity, five-family carry, three spine carries) then the author's body **unchanged and unre-numbered** (Header, §boundary, §A–§U incl. §U.01–U.10, claim-record appendix A01…A20, 10 `## Untried` items) then the `## registers —` application pointer | MERGED 2026-10-07, one file, under the tier target |
| – | `_parts/s1_p1.md` | 22,951 | 165,695 | the whole emission + the nine fenced register blocks (126 rows, l.1124–1312) | **read-only**; superseded for the live layer by `stage_1.md` + the CSVs; no `SUPERSEDED` footer (no prose correction was required) |
| – | `CORRECTIONS.md` | 1,477 | 9,918 | COR-01 id supersession · COR-02 decisions width · COR-03 validation/failures binding · COR-04 timeline foreign key · "Not corrected, and why" | LIVING — append, never rewrite history |
| – | `research/A_chronology_feasibility.md` | 8,271 | 56,245 | the probe that issued the window, five-family verdict, per-stage tiers | scope of record (untouched) |
| – | `research/A4_harvest_mine.md` | 750 | 4,733 | harvest-mine census carrier (70 / 12 / 57 at close) | measurement record (untouched) |

**What the merge did not carry into the prose volume.** The part's nine fenced `csv` blocks are register data, not
narrative (method §13): all **126 rows** were applied to the nine CSVs at this directory root and are not reprinted
in `stage_1.md`, where the heading now reads `## registers — Register rows applied to the nine CSVs` (the author's
`## registers` anchor is preserved so the in-body "full-width rows … are in `## registers`" cross-references still
resolve). The verbatim text stays in `_parts/s1_p1.md`. Claim records **are** narrative and all 20 remain.

## Section map — where each section lives (letters are the author's; nothing renumbered)

| section | lives in | note |
|---|---|---|
| Header + MERGE RECORD + COR propagation | `stage_1.md`, head | the only prose the merge wrote |
| §boundary | `stage_1.md` | five rows (S1a/S1b/S1c/S1d/whole) + the five things the boundary does NOT claim; 1996-not-an-IPO measurement (0 S-1/S-1/A/SB-2/10-A in 2,968) |
| §A–§S | `stage_1.md` | §K money register-shaped (T3 origin window), §P the 29-row metrics table, §Q the 24-row micro-timeline, §R the 1996-12-31 snapshot, §S 10 gaps |
| §T source / provenance | `stage_1.md` | document shorthands; the 8-B12B absent from both manifests; lineage collapses |
| §U.01–§U.10 | `stage_1.md` | the declared anchor set (`<!-- ANCHORS: U.01-U.10 -->`), 1:1 with `conflicts.csv` |
| Claim-record appendix | `stage_1.md` | 20 records CVS-A01…A20 (A20 the standing non-claim), `Conflicts:` keyed to U.01–U.10 |
| `## registers —` application pointer | `stage_1.md`, foot | rows per register, the COR-01…COR-04 edits, and the timeline-counter residual |

## Anchors and their register homes (parity proven by census + gate, not assertion)

| anchor | what it holds | register home |
|---|---|---|
| U.01 | which legal person was "founded in 1963" — S-4 business recital vs 1996-08-22 Delaware person | `conflicts.csv` U.01; `timeline.csv` 1963/1996 rows; `sources.csv` S4433/S4431; `quantitative.csv` 1963 + organise rows |
| U.02 | is *Consumer Value Stores* the name of the 1963 entity — folk story vs 1980–1994 third-party naming | `conflicts.csv` U.02; `timeline.csv` naming rows; `quantitative.csv` origin UNKNOWN; `sources.csv` S4435/S4436 |
| U.03 | **was 1996 an IPO — NO: reincorporation-by-succession, 0 S-1/S-1/A/SB-2/10-A in 2,968, 1 8-B12B** | `conflicts.csv` U.03; `timeline.csv` 1996-11-04 row; `sources.csv` S4431/S4447 |
| U.04 | 1989 chain sales $1.02bn vs $1.95bn (same press, five months apart) | `conflicts.csv` U.04; `quantitative.csv` two 1989-sales rows; `timeline.csv` 1989 estate row |
| U.05 | "Consumer Value Stores" the chain or the four-name segment | `conflicts.csv` U.05; `quantitative.csv` trade-box rows; `timeline.csv` box rows; `channels.csv` multi-name estate |
| U.06 | the 1963s/CVSs that are not this company (Civic Drugs, director history, medical abbreviation) | `conflicts.csv` U.06; `timeline.csv` 1979 absence + 2001 decoy; `sources.csv` S4438/S4446 |
| U.07 | same CIK, different taxpayer — EIN 04-1611460→05-0494040; disclosure vs charter continuity | `conflicts.csv` U.07; `timeline.csv` 1976/1996-03-15/1996-10-07/1996-11 rows; `sources.csv` S4445 |
| U.08 | **the `corporate_print` shelf is not family (d)** — 4 IA serial layers, 2 md5-dups of (c); tier stays put | `conflicts.csv` U.08; `sources.csv` S4437/S4448; `data_gaps.csv` S.8/S.10 |
| U.09 | `CVS, Inc.` (RI) vs `CVS Pharmacy, Inc.` (RI) — RESOLVED one person renamed | `conflicts.csv` U.09; `sources.csv` S4442/S4434; `decisions.csv` estate rows |
| U.10 | **supersession: 6 *Drug Store News* rows 1980-01-21→1994-04-25** (OCR-hyphen healing) not the probe's 4 | `conflicts.csv` U.10; `timeline.csv` naming rows; `sources.csv` S4435/S4436; `quantitative.csv` naming-year rows |

**Parity measured on the final bytes:** 10 declared anchors ↔ 10 `conflicts.csv` rows (U.01–U.10) ↔ 10 §U headings,
**0 orphans**; `merge_census.py` reads `conflicts.csv present 10 / missing 0`; `gates.py` reads `anchors parity —
10 narrative anchors <-> 10 register anchors`.

## Registers at the company root (canonical)

| register | cols | data rows | requested | words | bytes |
|---|---|---|---|---|---|
| `sources.csv` | 18 | 18 | 18 | 709 | 9,239 |
| `quantitative.csv` | 12 | 29 | 29 | 584 | 6,630 |
| `timeline.csv` | 11 | 24 | 24 | 504 | 5,411 |
| `conflicts.csv` | 15 | 10 | 10 | 961 | 7,421 |
| `data_gaps.csv` | 8 | 10 | 10 | 480 | 3,920 |
| `decisions.csv` | 15 | 14 | 14 | 646 | 6,131 |
| `validation.csv` | 11 | 8 | 8 | 266 | 2,577 |
| `failures.csv` | 11 | 7 | 7 | 260 | 2,407 |
| `channels.csv` | 11 | 6 | 6 | 255 | 2,298 |
| **TOTAL** | — | **126** | **126** | **4,565** | **43,974** |

## Reading order for the next passes

1. `stage_1.md` MERGE RECORD → §boundary (the 1996-not-an-IPO spine) → §U (the ten conflicts).
2. `conflicts.csv` + `sources.csv` (the S-4 one-lineage / corporate-print-not-(d) discipline).
3. audits by different agents — numbers+hindsight, then citation+verbatim (the verbatim auditor owns the `[~]`
   §D.2 quote and the timeline-counter residual named in `CORRECTIONS.md`).
4. a certifier who is neither author (`s1-cvs-p1`), merger (`merge-cvs`), auditor, nor repairer.
