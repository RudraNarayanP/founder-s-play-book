# _MANIFEST — company_006_cvs (CVS Corporation, CIK 0000064803, the Melville line) — Stage 1

**Counts regenerated 2026-10-07** by the Stage-1 merge pass (`merge-cvs`) with `wc -w` / `wc -c` on the bytes
**after the last write of this operation** (word = whitespace-delimited token, byte = file size). Every figure is
a measurement, not a recollection — re-measure before publishing any of them again. The merge applied **126
register rows against 126 requested** (0 unapplied, 0 added); the account, the pre/post census, the
validation/failures content adjudication, the timeline foreign-key repair, and the id-mint audit live in
`03_quality_control/cvs_s1_merge.md`. **This merge did not audit and does not certify.**

## Which ceiling governs which file

§9.1's hard upload constraint (**500,000 words / 200 MB per file**, whichever binds first) governs every file,
including the held evidence under `sources/`. §9.2's caps govern the stage volume: soft ≤ 40,000, amber
40,000–60,000, hard 60,000. `gates.py --tier core` reads the issued T2 tier and applies the **22,000-word tier
target** to `stage_1.md`, which measures **19,520 words — 89% of the tier target, 49% of the soft target, 33% of
the hard cap.** No overage, no §9.3 split, and nothing was trimmed to reach it. The tier cap is a **density
target measured on the assembled volume after merge, not on a part** (the part's raw 22,951 exceeds 22k mainly
because it carries the 126 register rows inline; the volume moves those out to the CSVs).

## Tier as issued vs as read (not re-tiered)

The probe (`research/A_chronology_feasibility.md`) issues the **whole dispatched window 1963-01-01→1996-12-31 =
T2 core (2 of 5 families)** and the per-stage tiers **S1a/S1b/S1c = T3 register, S1d = T2 core**. The merge carried
these verbatim and **did not re-tier.** `gates.py --tier auto` cannot read a tier written only as a table row, so
the budget check here was run at `--tier core` explicitly and that fact is recorded (not worked around by editing
prose).

## Deliverables (read these)

| File | Words | Bytes | Rows | Contents | Status |
|---|---|---|---|---|---|
| `stage_1.md` | 19,520 | 127,222 | — | MERGE RECORD (assembly, 126-row application, `PROV-CVS`→S4431–S4448 id map, geometry + foreign-key fixes, anchor parity, five-family carry, three spine carries) + the author's body **unchanged and un-renumbered** (Header, §boundary, §A–§U with §U.01–U.10, 20 claim records CVS-A01…A20) + the register-application pointer (`## registers — …`) | **MERGED 2026-10-07**; one volume; under every cap |
| `sources.csv` | 709 | 9,239 | 18 | 18×18, keys **S4431–S4448**, independence ledger (S-4 lineage = 1 source; FY1996 10-K405 = 2nd doc, 0×1963; corporate_print md5-dups; index rows are pointers) | APPLIED 18/18 |
| `quantitative.csv` | 584 | 6,630 | 29 | 29×12 — estate/revenue/pricing metrics, 1 counterparty row, 3 trade-box rows, the origin-window UNKNOWN row | APPLIED 29/29 |
| `timeline.csv` | 504 | 5,411 | 24 | 24×11 — 1963 recital + absences + naming rows 1980/1983/1987 + estate + restructuring + succession | APPLIED 24/24 |
| `conflicts.csv` | 961 | 7,421 | 10 | 10×15 — **U.01–U.10**, one row per declared anchor, 1:1 with §U | APPLIED 10/10 |
| `data_gaps.csv` | 480 | 3,920 | 10 | 10×8 — S.1–S.10, routes R-1…R-5 + families (b)/(e) + registry + intake | APPLIED 10/10 |
| `decisions.csv` | 646 | 6,131 | 14 | 14×15 — registrant decisions (no founder decision) — **row 1 width fixed (COR-02)** | APPLIED 14/14 |
| `validation.csv` | 266 | 2,577 | 8 | 8×11 — validating signals; block bound at merge (**COR-03**) | APPLIED 8/8 |
| `failures.csv` | 260 | 2,407 | 7 | 7×11 — adverse signals incl. the intake-manifest disclosure failure; bound at merge (**COR-03**) | APPLIED 7/7 |
| `channels.csv` | 255 | 2,298 | 6 | 6×11 — drugstore format, multi-name estate, DCs, pharmacy, PBM, leased departments | APPLIED 6/6 |
| `stage_1_index.md` | — | — | — | volume index: section map, anchors→register homes, register counts, reading order | MERGED |
| `CORRECTIONS.md` | 1,477 | 9,918 | — | COR-01 id supersession · COR-02 decisions width · COR-03 validation/failures binding · COR-04 timeline foreign key · "Not corrected, and why" | LIVING — append, never rewrite history |

**Register data rows applied: 126 (quantitative 29 · timeline 24 · sources 18 · conflicts 10 · data_gaps 10 ·
decisions 14 · validation 8 · failures 7 · channels 6). 0 unapplied, 0 added.**

## Intermediate emission (`_parts/`) — retained, read-only

| File | Words | Bytes | Contents |
|---|---|---|---|
| `_parts/s1_p1.md` | 22,951 | 165,695 | the whole author emission: Header, §boundary, §A–§U, 20 claim records, and the nine fenced register blocks (126 rows, l.1124–1312). The merge moved register data out of it; it did **not** edit it. No `SUPERSEDED` footer — nothing in its prose required correction; the corrections ledger is `CORRECTIONS.md` |
| `_parts/NOTES_cvs_p1.md` | 2,106 | 14,362 | the author's log: scope carried, corpus movement, R-1 yield, probe corrections, five-family, refusals, numbers re-measured |

## Research dossiers (scope of record — not touched by the merge)

| File | Words | Bytes | Role |
|---|---|---|---|
| `research/A_chronology_feasibility.md` | 8,271 | 56,245 | the probe dossier: window, per-stage tiers, five-family verdict, census, R-1…R-5 routes |
| `research/A4_harvest_mine.md` | 750 | 4,733 | harvest-mine census carrier (index close reads candidates 70 / mined 12 / untried_by_limit 57) |

## The five families, carried into this manifest with their states distinct

Verdict as issued by the probe for **Stage 1 (1963-01-01 → 1996-12-31)**; TRIED–ANSWERED / TRIED–UNANSWERED (the
tool or network refused — remedy named) / UNTRIED (0 calls, never reported as a null) kept apart in every row. No
family is reported empty that was not attempted.

| # | family | state | in-window Tier-1 text? | closing route |
|---|---|---|---|---|
| (a) | SEC / EDGAR | **TRIED–ANSWERED** (identity/S1d; S1a by recital only) | YES (S1d filings; S1a one recital) | 1990–1993 accessions + Oct–Dec 1996 8-K, add-only `sec_intake grab` |
| (b) | Web archives | **UNTRIED — 0 calls** | NO — a route never attempted | first CDX pass for `cvs.com`/`melville.com` 1996–2001 (S.8) |
| (c) | Periodical corpora | **TRIED–ANSWERED in part; TRIED–UNANSWERED for Chronicling America; 57 candidates UNTRIED at the limit** | YES (S1c/S1d trade press) | mine backlog; re-run CA under `andtext:"Consumer Value Stores"`, no state facet |
| (d) | Digitised corporate print | **TRIED–UNANSWERED (year-faceted) and ZERO BYTES** — its 4 files are IA serial layers, 2 md5-dups of (c), **not counted as a family (U.08)** | NO — zero bytes | facet-free corporate print (RD-130) |
| (e) | Auction / museum / manuscript | **UNTRIED — 0 calls; no query block exists for `cvs`** | NO — never queried | a scripted pass; the missing ask is the query block (S.6) |

**Families that counted: 2 — (a) and (c) — for the dispatched window ⇒ T2 core carried; S1a/S1b/S1c remain T3
register. (b) and (e) are UNTRIED, stated as such, never as answered nulls.**

## Census of this operation (measured, not asserted)

| reading | before any write | after the final write |
|---|---|---|
| structured blocks parsed | 9 | 9 |
| rows requested | 126 | 126 |
| `conflicts.csv` present / missing | 0 / 10 | **10 / 0** — anchor parity proven |
| `sources.csv` present / missing (by key) | 0 / 18 | 0 / 18 — the 18 "missing" are the superseded local tags `PROV-CVS-01…18`; minted ids S4431–S4448 are on disk (COR-01) |
| unattributed block-groups | 2 (validation/failures, identical 11-col schemas) | 2 — same schema property; adjudicated by reading, recorded in the merge report and COR-03 |
| third emission in `research/*.csv` | none (0 CSVs under `research/`) | none |
| gate findings | 1 (coverage — pre-merge state) | 2 named residuals (quantitative UNKNOWN date; OCR `[~]` quote), 19 passes |

## Open items this merge did NOT close (named, not dropped)

1. **Timeline `source_id` column is a running counter** (COR-04): 6 cells repaired to resolve; the remaining
   semantic mis-pointings (e.g. row 7's 1987 DSN-88 carrier is not among the 18 sources) are left for the
   citation auditor, since fixing them needs sources the author did not emit.
2. **2 verbatim-quote findings for audit**, not merge: the `[~]` OCR-corruption quotation (§D.2) and the
   `--tier auto` table-row limitation (budget checked at `--tier core` explicitly).
3. Families **(b)** and **(e)** remain UNTRIED; **(d)** has zero bytes; 57 periodical candidates remain unmined;
   Chronicling America must be re-run without the state facet and with the corrected string.
4. `_FLEET_INTAKE.tsv` / `_RUN.json` manifest drift and the 8-B12B's absence from both manifests are **reported**
   (failures.csv, data_gaps.csv S.10), not repaired — not this agent's files.
