# stage_1_index.md — company_017_meta, Stage 1 (volume map, merged 2026-10-07 by `merge-meta`)

One volume, `stage_1.md`, **30,212 words / 197,633 bytes** (measured after the last write). Tier **T2 core
(2 of 5 families)** as the dossier measures it — **not** the dispatch's T1 label, and not the T1 that
`gates.py --tier auto` stamps (§"Tier" in `_MANIFEST.md`, COR-06). Window **2003-01-01 → 2012-12-31** as
dispatched, with the probe's July-2004 Stage-1 close carried as conflict **U.7**. Registrant for the registers:
**`Facebook, Inc.`** (104 of the 105 rows that carry a `company` column); `Meta Platforms, Inc.` on the single row
whose carrier is the EDGAR registrant record (`data_gaps.csv` row 9); bare `Meta` on no row; `sources.csv`'s 15 rows
carry no `company` column at all (COR-08).

## Reading order

1. `_MANIFEST.md` — what was measured, which cap governs, the `company` literal convention, the provenance drift.
2. `stage_1.md` head — the merge record: the **seven findings carried intact**, anchor parity before/after, the
   tier and window rulings.
3. `stage_1.md` **part 1 body** — §Header, §boundary (8 sub-sections: entity question, rival windows, where the
   record stops, the two routes, CONTEMPORANEOUS/RESTATED test, the five corrections, post-boundary conventions,
   the seven conflicts), §A–§J, `## Untried` (11 routes), FETCH REQUESTs **F-1…F-5**.
4. `stage_1.md` **part 2 body** — §K–§T, **§U.1–§U.8** (the only §U body in the corpus; both parts' registers cite
   it), `## claims` (K01…T01), `## registers` (pointer lines).
5. `stage_1.md` foot — register-application record, the **local-tag → S4495…S4509 id map**, the five-family table,
   open follow-ups, the COR-01…COR-09 propagation table.
6. The nine live registers at the company root; then `CORRECTIONS.md`; then `_parts/` (the emission of record,
   read-only) and `research/` (the authority for tier and families).

## Section homes and what each is load-bearing for

| section | part | carries | register homes |
|---|---|---|---|
| §Header | p1 | registrant identification, the two-boundary window, tier as found, the single-lineage rule, the record-selection null | `sources.csv` S4501; conflicts U.7 |
| §boundary | p1 | the entity question (which person, which name, which date), 7 rival windows measured and rejected, where the record physically stops, CONTEMPORANEOUS/RESTATED test run on held bytes, COR-1…COR-5 as the author took them, the seven conflicts | all eight `conflicts.csv` rows; `data_gaps.csv` rows 1–2, 11 |
| §A–§J | p1 | state of the company at window open and close; the founder as the registrant described him; the problem; the first experiment; the product; the customer; supply/ops; market; competition; technology | `quantitative.csv` (the FY2007–FY2011 and 2011–2012 metric sets), `timeline.csv`, `validation.csv`, `failures.csv`, `channels.csv` |
| §K–§T | p2 | money, the void where traction should be, the contested origin, decisions, competition-as-litigation, financial series, chronology, organisation at the boundary, artifacts, independence/provenance census | `timeline.csv` (dockets), `decisions.csv`, `validation.csv` (the earned null), `quantitative.csv` (the 6 void-sizing rows) |
| **§U.1–§U.8** | p2 body, **p1 rows canonical for U.1–U.7** | every conflict, adjudicated | `conflicts.csv` 8 rows, 1:1 |
| `## claims` | p2 | K01, K02, K03, K04, L01, M01, M02, M03, N01, N02, O01, P01, P02, Q01, R01, S01, T01 (17 records) | cited from `decisions.csv` `claim_ref` |
| p1 claim records | p1 | `P1-01 … P1-33` (33 records), each in its section | cited from `sources.csv` `claim_supported`, `decisions.csv` `claim_ref` |
| `## Untried` | p1 | 11 named routes, each with its fetch request | `data_gaps.csv` rows 1–13 |

## Anchor ↔ register parity (the merge's proof, not the author's assertion)

Declared: part 1 `U.1–U.7`, part 2 `U.1–U.8`; the volume publishes the **union `U.1–U.8`** and renumbered nothing.
Before de-duplication **15** `conflicts.csv` rows were emitted against **8** subjects (7 duplicate primary keys);
after, **8 rows ↔ 8 narrative anchors**, which the gate confirms (`anchors parity 8 narrative anchors <-> 8
register anchors`; `citation resolution: every register-cited anchor resolves, 8 distinct ids`).

| anchor | subject | canonical part | the other part's contribution |
|---|---|---|---|
| U.1 | formation day: Ex-3.3 recital (unexecuted form) vs the absent registry record | **p1** | p2's month-level cells kept; its "day UNKNOWN / unobtainable from EDGAR permanently" superseded (COR-03) |
| U.2 | subject of the origin: registrant vs Mr Zuckerberg personally (April 2003 / Ceglia) | **p1** | p2's "the company asserts the emails are fraudulent" folded |
| U.3 | 2005-05-06 `REGDEX` activity vs "the first filing is the 2012 S-1" | **p1** | p2's "gap marker, not a founding event" folded; standing prohibition carried |
| U.4 | prospectus silence vs a live federal register (seven matters) | **p1** | p2's settled-then-dropped rationale folded; "Saverin 0" narrowed to the two documents it cited |
| U.5 | "February 2004 / dorm room" vs the dated origin statements | **p1** | p2's popular-pages Harvard note folded |
| U.6 | the "thirty days" growth claim vs the corpus's actual windows | **p1** | p2's 5–6 % duplicate-account argument folded; its "no `thirty days` string at all" refuted (1 hit) |
| U.7 | stage architecture: July-2004 close vs the dispatched 2003→2012 window | **p1** | p2's "the load-bearing findings hold under either reading" folded; the merge's staging call recorded |
| U.8 | tooling: "EDGAR reaches nothing before 2024" vs the 397-row enumeration | **p2 alone** | p1 never enumerated it; RD-138/RD-139 context added by the merge |

## Register counts as applied

`sources.csv` **15 × 18** (S4495–S4509) · `quantitative.csv` **36 × 12** · `timeline.csv` **23 × 11** ·
`decisions.csv` **5 × 15** · `validation.csv` **8 × 11** (7 applied + 1 authored) · `failures.csv` **8 × 11** ·
`channels.csv` **4 × 11** · `conflicts.csv` **8 × 15** · `data_gaps.csv` **13 × 8** = **120 live rows** from
**142 emitted** (23 aliased by subject, 1 authored on instruction). Headers byte-identical to
`company_001_amazon/`; 0 rows off header width; 0 empty cells; `stage` = `stage1` on 120/120.

## What this index is not

Not an audit and not a certification: a merge may supply neither. Every number here is a measurement of the
merge's own writes and must be re-measured by a different agent.
