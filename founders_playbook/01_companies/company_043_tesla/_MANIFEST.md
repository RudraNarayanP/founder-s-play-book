# _MANIFEST — company_043_tesla

Counts regenerated **2026-09-30** by the Stage-1 merge pass (`tesla-s1-merge`), on the written bytes after the
last append (word = whitespace-delimited tokens, `wc -w`-equivalent; byte = file size). Per method §9.6 every
directory carrying split files keeps this register so a file can be checked against the ceilings before handoff
or upload. **Nothing in this directory is a cleanup target** (§14 rule 4): `_parts/`, `research/`, `sources/` and
the superseded emissions are left exactly where they are.

**Which ceiling governs which file.** §9.1's hard upload constraint (500,000 words / 200 MB per file) governs
every file including the restored primaries under `sources/` — the largest held document, the 424B4 submission
txt, is 4.7 MB, ~2% of the byte ceiling. §9.2's **60,000-word hard cap** governs `stage_1.md`. §15.2's **8,000-word
T3 figure** governs the *dispatch budget*, not the written evidence (RD-122; §9.6 forbids trimming evidence to fit
a file limit; §15.4 makes a missed length target legitimate).

## Deliverables (read these)

| File | Words | Bytes | Contents | Upload batch | Status |
|---|---|---|---|---|---|
| `stage_1.md` | **53,553** | 370,566 | Merge header + Stage-1 merge note + widened `ANCHORS: U.1-U.23` + Volume 1 (part 1: §Header, §Boundary, §A–§F, claim records P1-01–P1-33, register emission) + Volume 2 (part 2: §G–§U, claim records P2-01–P2-54, its `## Untried`, register emission) + merge `## Untried` addendum + `U.23` anchor + COR-01…COR-06 propagation block | 5 | **MERGED 2026-09-30, ONE volume.** 89% of the 60,000 hard cap → under it, so **no §9.3 split performed**; above the 40,000 soft target (amber, allowed to finish as one file) and 6.7× the T3 8,000 target (**known accepted state**, see "Budget" below) |
| `CORRECTIONS.md` | 1475 | 10454 | COR-01…COR-06, each with the withdrawn wording, the measured basis, the register home and the volume home | 5 | WRITTEN by this merge (Tesla had none). `gates.py` propagation: **all 6 reach registers and volumes** |
| `stage_1_index.md` | 1564 | 10451 | Ordered volume list, word counts, section locations, anchor ranges, register table, the six merge decisions | 5 | WRITTEN by this merge |

## Structured dataset (canonical registers, company root)

| Register | Rows | Cols | Words | Bytes | Requested | Applied by |
|---|---|---|---|---|---|---|
| `sources.csv` | **24** | 18 | 3,732 | 29,716 | 40 | 16 aliased into 8 fold groups |
| `quantitative.csv` | **61** | 12 | 1,756 | 15,749 | 61 | 0 folds |
| `timeline.csv` | **46** | 11 | 1,862 | 15,189 | 47 | 1 fold (2010-06-29 closing edge) |
| `conflicts.csv` | **23** | 15 | 3,152 | 22,274 | 22 | +1 minted at merge (`U.23`) |
| `data_gaps.csv` | **15** | 8 | 1,604 | 11,565 | 23 | 8 aliased into 7 fold groups |
| `decisions.csv` | **9** | 15 | 841 | 6,329 | 9 | 0 folds |
| `validation.csv` | **9** | 11 | 372 | 3,121 | 9 | census-AMBIGUOUS block, attributed by content |
| `failures.csv` | **11** | 11 | 536 | 4,232 | 11 | census-AMBIGUOUS block, attributed by content |
| `channels.csv` | **10** | 11 | 468 | 3,768 | 10 | 0 folds |
| **Total** | **208** | | **13,329** | **111,343** | **232** | **16 collision groups, 0 refused** |

Headers are **byte-identical to `company_001_amazon`'s conformant ones** (verified string-for-string against all
nine reference headers on this pass; Amazon supplied **format only — no Amazon data was read into this company**).
`stage` column: **all 208 rows carry the literal `stage1`** — no numeric stage value exists anywhere in this
register set (the vocabulary RD-048/RD-075 fixed and a numeric `stage` still leaked into one company's
`sources.csv`). **Normalisation on touch:** the probe emission's 25 rows carried `company = tesla`; the **9** of them that survive as
their own rows (6 conflicts `U.1`-`U.6`, the two probe-only source rows `S4391`/`S4392`, and the surviving probe gap
row for the untried documentary family) were normalised to `Tesla Motors Inc`, the name the registrant filed under;
the other **16** aliased rows survive verbatim inside `MERGE[…]` alias text - `company` cell included - and were not
rewritten.

## Intermediates and read-only evidence (do not re-apply, do not clean)

| Path | Words | Bytes | Status |
|---|---|---|---|
| `_parts/s1_p1.md` | 13,737 | 95,964 | **SUPERSEDED notice appended 2026-09-30** (body carried verbatim into `stage_1.md` Volume 1, offset 9,746). **Truncation reported, not repaired:** the file ends at a stray `#` after its `data_gaps` block and its `## Untried` — cited four times in its own body — is not on disk (RD-132's Nvidia defect class). §14 rule 4: it stays exactly where it is |
| `_parts/s1_p2.md` | 37,770 | 260,447 | **SUPERSEDED notice appended 2026-09-30** (body carried verbatim into Volume 2, offset 102,736) |
| `research/A_chronology_feasibility.md` | 8,745 (probe) | — | read-only dossier; its 12 claim records F01–F12 are prose, not register rows. Its §Verdict EDGAR wording is corrected by `COR-03` |
| `research/A3_intake_regrade.md` | 1,617 | — | **the later file on the tier: re-issues T3 unchanged**, so there is no regrade for the merge to obey; it does supersede the probe's row-count wording and adds the 336-row XBRL series |
| `research/sources.csv`, `research/conflicts.csv`, `research/data_gaps.csv` | 12 / 6 / 7 rows | — | the **third emission**, invisible to `merge_census.py`; 25 rows censused by hand, 15 applied (6 fold into kept rows… see merge notes §4), 0 discarded |
| `research/_harvest_queries_tesla.json`, `..._ca2.json`, `_write_registers_tesla.py` | — | — | inputs and a build script; untouched |
| `sources/` | 60.7 MB tree: 83 documents / 32 accessions / **59,881,144 B** under `sec/`, `_index/submissions.csv` 1,750 rows, `financials/xbrl_early_series.csv` 336 rows, `legal/cl_*.json`, `wayback/` (transcript-only + negative artefacts), `harvest/` (9 response bodies) | — | protected archive, read-only (§14 rule 4/9). `_MANIFEST.csv` inside `sec/` carries 76 rows / 25 accessions and omits the 3 corrupted UPLOAD PDFs and the 4 CORRESP letters — measured and reported as `COR-06` |

## Open research debt carried out of this merge (all five families named in
`03_quality_control/tesla_s1_merge_notes.md` §11; FETCH REQUEST blocks FR-1…FR-8 §10)

Filings: exhibit folder of `0001193125-10-017054` / `-149105` (charter, Series A–B purchase agreements, the 2003
plan, the 424B4 balance-sheet column heads) and the binary re-fetch of the three staff PDFs. Web archives:
domain-scoped CDX 2003–2009 then one `id_` snapshot of the **August 2009 joint statement**. Periodicals: the
**page-text layer, never searched** for this company. Corporate print: the two identified items, **never opened**.
Documentary/auction: **UNTRIED entirely** — a family never tried, never written as a null. Legal: the **San Mateo
County** registry, outside CourtListener's federal-only scope. Every High-importance row in `data_gaps.csv`
carries a `follow_up_task`, so no High gap is unassigned.| Gate finding | **Findings: 2 \| Passes: 20** on the final bytes. `advisory \| stage_1.md \| 53553 words over the register density target 8000 — NOT a split mandate and NOT a defect`, plus the tool-labelled ADVISORY `quotes \| 16 of 58 checked spans unmatched (28%)`. `gates.py` was edited by a concurrent pass at 00:45 on 2026-09-30 between this merge's two runs, and now separates the hard cap (defect) from the tier cap (advisory) exactly as RD-122 demanded; the earlier run printed `budget \| … > register cap 8000 (split required)`, whose "split required" wording was wrong at 53,553 words (§9.2 requires a split only above the 60,000 hard cap). Data left alone in both cases — report at `03_quality_control/tesla_s1_gates.md/` |

## Intermediates and read-only evidence (do not re-apply, do not clean)

| Path | Words | Bytes | Status |
|---|---|---|---|
| `_parts/s1_p1.md` | 13,737 | 95,964 | **SUPERSEDED notice appended 2026-09-30** (body carried verbatim into `stage_1.md` Volume 1, offset 9,746). **Truncation reported, not repaired:** the file ends at a stray `#` after its `data_gaps` block and its `## Untried` — cited four times in its own body — is not on disk (RD-132's Nvidia defect class). §14 rule 4: it stays exactly where it is |
| `_parts/s1_p2.md` | 37,770 | 260,447 | **SUPERSEDED notice appended 2026-09-30** (body carried verbatim into Volume 2, offset 102,736) |
| `research/A_chronology_feasibility.md` | 8,745 (probe) | — | read-only dossier; its 12 claim records F01–F12 are prose, not register rows. Its §Verdict EDGAR wording is corrected by `COR-03` |
| `research/A3_intake_regrade.md` | 1,617 | — | **the later file on the tier: re-issues T3 unchanged**, so there is no regrade for the merge to obey; it does supersede the probe's row-count wording and adds the 336-row XBRL series |
| `research/sources.csv`, `research/conflicts.csv`, `research/data_gaps.csv` | 12 / 6 / 7 rows | — | the **third emission**, invisible to `merge_census.py`; 25 rows censused by hand, 15 applied (6 fold into kept rows… see merge notes §4), 0 discarded |
| `research/_harvest_queries_tesla.json`, `..._ca2.json`, `_write_registers_tesla.py` | — | — | inputs and a build script; untouched |
| `sources/` | 60.7 MB tree: 83 documents / 32 accessions / **59,881,144 B** under `sec/`, `_index/submissions.csv` 1,750 rows, `financials/xbrl_early_series.csv` 336 rows, `legal/cl_*.json`, `wayback/` (transcript-only + negative artefacts), `harvest/` (9 response bodies) | — | protected archive, read-only (§14 rule 4/9). `_MANIFEST.csv` inside `sec/` carries 76 rows / 25 accessions and omits the 3 corrupted UPLOAD PDFs and the 4 CORRESP letters — measured and reported as `COR-06` |

## Open research debt carried out of this merge (all five families named in
`03_quality_control/tesla_s1_merge_notes.md` §11; FETCH REQUEST blocks FR-1…FR-8 §10)

Filings: exhibit folder of `0001193125-10-017054` / `-149105` (charter, Series A–B purchase agreements, the 2003
plan, the 424B4 balance-sheet column heads) and the binary re-fetch of the three staff PDFs. Web archives:
domain-scoped CDX 2003–2009 then one `id_` snapshot of the **August 2009 joint statement**. Periodicals: the
**page-text layer, never searched** for this company. Corporate print: the two identified items, **never opened**.
Documentary/auction: **UNTRIED entirely** — a family never tried, never written as a null. Legal: the **San Mateo
County** registry, outside CourtListener's federal-only scope. Every High-importance row in `data_gaps.csv`
carries a `follow_up_task`, so no High gap is unassigned.
