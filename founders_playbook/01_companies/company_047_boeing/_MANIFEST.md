# _MANIFEST — company_047_boeing (Stage 1)

**Counts regenerated 2026-10-07** by the Stage-1 merge pass (`merge-boeing`) with `wc -w` / `wc -c` on the bytes
**after the last write of this operation** (word = whitespace-delimited token, byte = file size). Every figure
below is a measurement, not a recollection; re-measure before publishing any of them again. The merge applied
**211 register rows against 211 requested** — the account, the census readings before and after, the id
allocation and the validation/failures adjudication live in `03_quality_control/boeing_s1_merge.md`.

**Which ceiling governs which file.** §9.1's hard upload constraint (500,000 words / 200 MB per file, whichever
binds first) governs every file including the evidence under `sources/` (largest single held file here is the
4,594,867 B munitions layer — under the byte ceiling). §9.2 governs a stage volume: soft target ≤ 40,000
words, amber 40,000–60,000, **hard cap 60,000**. The **tier cap is a density target, not a file limit**.
`gates.py --tier auto` mis-stamps this dossier **T3** (its reader counts tier *mentions* across `research/`
rather than reading the verdict line — a table-row verdict it cannot see), so the budget check was run with
**`--tier core` (T2, 22,000) passed explicitly**, as `_AUTHOR_WAVE_PLAN.md` directs, and that is recorded here
rather than editing prose to satisfy the tool. `stage_1.md` measures **34,817 words = 158% of the T2 tier
target, 87% of the 40,000 soft target, 58% of the 60,000 hard cap** — over the density target, under every cap
that is a defect.

## Geometry decision and volume map

The part file measured **44,732 words** (author's body + blocks; 45,006 after the merge's `SUPERSEDED` footer).
The author (NOTES §4) offered a split at a section boundary (Header+boundary+A–O / P–U+claim records /
registers). **Decision: one volume, not split.** Reasoning, so a later reader is not tempted to cut evidence to
meet a number (§9.6 — the limit governs file geometry, never research depth):

1. After the merge the nine fenced register blocks (211 rows) are applied to the CSVs and **moved out of the
   prose**, so the narrative volume itself is 34,817 words — comfortably under the 60,000-word hard cap (§9.2).
2. The whole T2 deliverable (§A–§U, claim records, full registers, `## Untried`) fits one file; there is no
   §9.2 defect to repair. The overage against the 22,000 tier target is **advisory only** and was **not**
   remedied by deleting anything.
3. A boundary-only, never-renumbered split buys nothing here and would add a volume map to maintain without
   removing the advisory.

**Volume map (single stage, one part, one volume):**

| volume | file | sections | anchors | status |
|---|---|---|---|---|
| Stage 1 | `stage_1.md` | Header, Stage boundary, §A–§U, claim-record appendix (P1A01…P1S02), `## Untried` (11 items), `## FETCH REQUEST` (#1–#5) | U.001–U.017 (declared `<!-- ANCHORS: U.001-U.017 -->`, kept in `stage_1.md` l.60-region) | **MERGED 2026-10-07** — one volume; nothing trimmed; overage advisory |

No Stage 2 / Stage 3 volumes exist for this company; the probe proposed (PROVISIONAL) spans only, and §15.2 /
RD-112 requires any later stage to re-measure its tier against its own span.

## Deliverables (read these)

| File | Words | Bytes | Contents | Status |
|---|---|---|---|---|
| `stage_1.md` | 34,817 | 224,150 | MERGE RECORD (assembly, one-volume geometry decision, 211-row application, `P1SRC01–19`→**S4510–S4528** id map, validation/failures binding, anchor parity, five-family table, the four carried registrant-identity items, gate_quotes gap, carry-forward) + the author's body **unchanged and unre-numbered** (§Header…§U, 24 claim records, `## Untried`, FETCH REQUESTs) + the register-application pointer | **MERGED 2026-10-07**; one volume; under the 60k hard cap; over the 22k tier target (advisory) |
| `sources.csv` | 2,458 | 21,796 | 19 × 18 — keys **S4510–S4528**, one corporate-print lineage (S4510–S4515/22/23), S4525 = one registry record re-printed 26×, S4526 = two lineages one sentence, S4519/20 negative controls, S4521/S4527/S4528 carriers not witnesses | APPLIED 19/19 |
| `quantitative.csv` | 2,524 | 22,334 | 75 × 12 — FY1934–FY1940 audited-adjacent set, DERIVED rows with arithmetic, C$ row labelled; **0 FY1937 income/balance rows and 0 FY1936 rows** (withheld by design) | APPLIED 75/75 |
| `timeline.csv` | 1,507 | 13,677 | 42 × 11 — 1916 (RESTATED) → 1940-12-31 boundary; `1916-07-22` DERIVED row (U.003); A.M. 18 three-way date rows at U.004 | APPLIED 42/42 |
| `conflicts.csv` | 2,045 | 14,550 | 17 × 15 — **U.001–U.017, one row per declared anchor, 1:1 with §U**; U.004 unreconciled, U.010 motive UNTRIED, U.014 six-not-seven report count | APPLIED 17/17 |
| `data_gaps.csv` | 1,042 | 7,694 | 18 × 8 — 10 High; **FY1937 (P1GAP16), FY1936 absence (P1GAP05/08) carried as damage-with-route**; follow-ups cite FETCH #2/#3/#4; P1GAP18 intake regression | APPLIED 18/18 |
| `decisions.csv` | 1,128 | 8,703 | 11 × 15 — 1934-08 formation (motive UNKNOWN) → 1940 accounting change; the 1936 decision-void row (not held) | APPLIED 11/11 |
| `validation.csv` | 983 | 7,776 | 13 × 11 — positive signals (P1VAL01–13); **bound to validation.csv by content at merge** (shares failures.csv's schema) | APPLIED 13/13 |
| `failures.csv` | 708 | 5,475 | 9 × 11 — incurred losses / attestation limits (P1FAI01–09); **bound to failures.csv by content at merge** | APPLIED 9/9 |
| `channels.csv` | 532 | 4,120 | 7 × 11 — A.M. 18 bid, sub-contract, municipal leases, direct military, commercial sales, export, equity markets | APPLIED 7/7 |

**This register is not self-listed** — a file cannot publish its own final size; it is re-measured whenever it
is written. Upload batch 1 = `stage_1.md`; batch 2 = the nine registers; batch 3 = `_parts/`, `research/`,
`sources/`. **No file was shortened to meet a number.**

## Intermediate emission (`_parts/`) — retained, read-only

| File | Words | Bytes | Contents | Why retained |
|---|---|---|---|---|
| `_parts/s1_p1.md` | 45,006 | 318,033 | the whole author emission (44,732 words: Header…§U, 24 claim records, `## Untried`, FETCH #1–#5, nine fenced register blocks at l.1401–l.1698) **+ a 274-word `SUPERSEDED 2026-10-07` footer the merge appended** | emission of record; the merge moved register data out and edited nothing above the footer — the footer supersedes **placement and keys only** (P1SRC→S, validation/failures bound). No narrative word needed correction |
| `_parts/NOTES_boeing_p1.md` | 2,257 | 14,934 | the author's log: measurements, four probe corrections, refusals, the split proposal, FETCH #1–#5, the `--tier auto` mis-read | shows what the merge accepted and what the author refused to claim |

## Research dossiers (scope of record — not touched by the merge)

| File | Words | Bytes | Role |
|---|---|---|---|
| `research/A_chronology_feasibility.md` | 4,000 | 28,197 | issued the Stage-1 window (1916-01-01 → 1940-12-31), **T2 core**, the five-family table, the census and `## Untried` #1–#9; its D-1…D-5 defects and load-bearing open questions |
| `research/A4_harvest_mine.md` | 930 | 6,541 | harvester census carrier for the 12 NASA layers + item enumeration (all out of window; cited only for the modern name's third-party printings) |

## The five families, carried into this manifest with their states distinct

Verdict as issued by the probe for **Stage 1 (1916-01-01 → 1940-12-31)**; **TRIED–ANSWERED**,
**TRIED–UNANSWERED** (attempted, tool/network refused — remedy named) and **UNTRIED** (0 calls, never reported
as a null) are kept apart. No family is reported empty that was not attempted. **Stage 1 = T2 core; tier not
re-graded by this merge.**

| # | family | state | measured basis | in-window Tier-1 text? | closing route |
|---|---|---|---|---|---|
| (a) | SEC / EDGAR filings | **TRIED–ANSWERED as a perimeter; nothing in-window** | registrant `BOEING CO` CIK 0000012927; 4,026 filings enumerated, earliest indexed **1994-03-15**; **no S-1 exists**; 37 stored docs all post-1994 (`(PB)`); 333 accessions never enumerated (`--max-docs 40`) | NO — the EDGAR floor is 54 years after the window closes; only origin voice is the 1996/1998 S-4 boilerplate | FETCH #1 (earliest corporate-history paragraph); Washington/Delaware charter records (no tool) |
| (b) | Web archives | **UNTRIED (now REACHABLE; still cannot bear on Stage 1)** | the probe's "no script reaches CDX" is stale — `tools/cdx_intake.py` (mtime 2026-10-06) is the scripted route; family floor is mid-1990s vs a 1916-1940 window (§14.6) | NO | `python tools/cdx_intake.py …` (orchestrator); bears on Stage 3 |
| (c) | Periodical / gov print corpora | **TRIED–ANSWERED, with two content-verified NULLs** | holds D.C. Cir. 1934 air-mail record + 1933 Wyoming record (Tier-1 federal/judicial); *Aviation* 1916-08-01 `Boeing` 0 (149,286 chars), Senate munitions `Boeing` 0 / `Seattle` 0 (4,594,867 B) — live negative controls; probe opened 3 of 47 in-window items | **YES** (the two court records) | **UNTRIED** #3 (Aeronautics Branch/CAB), #6 (44 unopened IA items), #8 (HathiTrust/Google Books) |
| (d) | Digitised corporate print | **TRIED–ANSWERED — the family that moved Boeing** | IA item `boeingairplanecompanyannualreports`; **six** in-window audited reports FY1934/35/38/39/40 (the `1934a` layer is a Hamilton Metalplane advertisement, not a report), 137,518 B; FY1937 column-interleaved (fragments only) | **YES** — company-authored audited-adjacent print | **UNANSWERED** #3 (FY1937 re-OCR, FETCH #3); 39 unopened 1941-78 layers (FETCH #8 route) |
| (e) | Auction / museum / manuscript | **UNTRIED — structurally** | no source-family in `queries.json`; nothing in `tools/` reaches a finding aid — the family that carries founders' papers/logbooks/certificates for pre-1930 companies | NO — a search never run | **UNTRIED** #1/#2 — `python tools/periodical_harvest.py --company boeing --source-family auction …`; the single route most likely to change the Stage-1 verdict |

**Two untried families remain the upgrade path** to T1; the probe's honest headline — *Boeing's origin window
has in-window primary text, and that text contradicts the folk founding date at the level of which legal entity
it attaches 1916 to* — is carried into `stage_1.md` §A/§B.3/§U.001 unchanged.

## Census of this operation (measured, not asserted)

| reading | before any write | after the final write |
|---|---|---|
| structured blocks parsed | 9 | 9 |
| rows requested | 211 | 211 |
| `conflicts.csv` present / missing | 0 / 17 | **17 / 0** — anchor parity U.001–U.017 proven |
| `sources.csv` present / missing | 0 / 19 | 0 / 19 — the 19 "missing" keys are the superseded local tags `P1SRC01–19`; the minted ids **S4510–S4528** are on disk (see the id map in `stage_1.md`) |
| unattributed block-groups | 2 (validation/failures, identical 11-col schemas) | 2 — same schema property; adjudicated by reading, reasoning in-cell and in the merge report |
| duplicate keys across all nine blocks | — | 0 (sources 19 keys, conflicts 17 keys, all unique) |
| rows off header width | — | 0 (all 211 at header width) |
| third emission in `research/*.csv` | none (0 CSVs under `research/`) | none |

## Gate and merge records

- `03_quality_control/boeing_s1_merge.md` — the merge's live account: census before/after, the 211-requested /
  211-applied per-register total, the id allocation, the validation/failures adjudication, the five-family
  table, the geometry decision, and every uncarried follow-up named.
- `03_quality_control/boeing_s1_gates_merge.md` (+ `.json`) — the gate run after the last write with **`--tier
  core`** (see the exit-code note in the merge report).
- `03_quality_control/boeing_s1_gates_p1.md` — the author's pre-merge gate (coverage-only, expected state).

## Open items this merge did NOT close (named, not dropped)

1. **FY1937 and FY1936 data are withheld, not absent.** All FY1937 income/balance figures (column-interleaved
   OCR) and all FY1936 quantities (the layer is **absent from the archive item**) are carried as
   `data_gaps.csv` rows (P1GAP16, P1GAP05, P1GAP08) and FETCH #3/#4; they were never back-solved from
   neighbours and `quantitative.csv` deliberately has 0 FY1937 rows.
2. **FETCH #1 and #5 have no dedicated `data_gaps.csv` row** (the author emitted none); their homes are
   `## Untried` #9/#10 and the `residual_uncertainty` cells of `conflicts.csv` U.001–U.003 — named here, not
   dropped.
3. **`sources/sec/_MANIFEST.csv` regression** (header row, 0 data rows, though 33 `.txt` + 37 sidecars are on
   disk) is **reported not repaired** (P1GAP18, §14 rule 4); the held-SEC list must be re-derived from
   filenames or re-intaked. This merge did not modify `sources/`.
4. **Origin identity unresolved on held evidence.** Five namings, no held byte conjoining any two; origin day
   **DERIVED 1916-07-22** (July 15 unheld, not contradicted); A.M. 18 award date three-valued at U.004; the
   1934–38 reorganisation motive **UNTRIED, mechanism UNKNOWN** (no antitrust witness); the 1960 renaming
   refused as a Stage-1 fact. All preserved; none "reconciled".
5. **The two tier frames** (probe verdict vs `gates.py --tier auto`'s mis-stamp) stay unreconciled; this merge
   ran the gate with **`--tier core`** and recorded the tool mis-read rather than editing the dossier.
