# _MANIFEST — company_023_gm (General Motors)

**Counts regenerated 2026-10-07 by the Stage-1 merge pass (`merge-gm`)** — every number in the tables below was
measured off the bytes on disk **after the last write of this pass**, per `00_METHOD_AND_STYLE.md` §9.6 (a stale
count is a defect) and §14 line-number rule (re-measure anything you publish). Word = whitespace-delimited token
(`\S+` count, `wc -w`-equivalent); byte = file size. Any later pass that edits one of these files makes this
register stale for that file and must say so in its own sheet.

**Which ceiling governs which file.** `stage_1.md` is measured against **T2 core: 22,000 words per stage** — the
tier this company's own probe issued at `research/A_chronology_feasibility.md` §3, Stage-1 row — and against
§9.2's 60,000-word hard cap. Live: **20,192 words, 91.8% of the T2 target**, one volume, no split required and
none done. `gates.py --tier auto` reads **T3** from that dossier because the Stage-1 verdict sits on a *table
row* the reader's "verdict line" heuristic cannot see; the budget check for this pass was therefore run with
**`--tier core` explicit** (see `03_quality_control/gm_s1_gates_merge.md` and `…_tiercore.md`). **The dossier was
not edited to satisfy the tool and no data was reshaped to silence a gate.** The claim-record appendix and the
volume map are companions, not narrative volumes (`stage_docs()` excludes them), so they are not graded at
volume caps. §9.1's hard upload constraint (500,000 words / 200 MB per file, whichever binds first) governs the
held primaries under `sources/`: the largest single file is **10,915,696 B** (`sources/sec/0001193125-10-255258_ds1a.htm`,
2009 out-of-window material), **5.5%** of the 200 MB ceiling; nothing under `sources/` is near any ceiling.

## Deliverables (read these)

| File | Words | Bytes | Contents | Upload batch | Status |
|---|---|---|---|---|---|
| `stage_1.md` | **20,192** | 129,867 | Title; **MERGE RECORD** (application table, id map S4423–S4430, duplicate checks, validation/failures adjudication, anchor parity, the two GM carries, `COR-01…COR-09`, not-applied list); Stage boundary; §A–§U incl. the 10 anchors **U.01–U.10**; registers pointer | 1 | **MERGED 2026-10-07** — 91.8% of the T2 22,000-word target, under §9.2's 60,000 hard cap; no audit, no certification on this pass |
| `stage_1_claim_records.md` | **2,921** | 18,804 | Claim-record appendix **GM1-C01 … GM1-C33** (33 records), relocated byte-for-byte at the §U section boundary (§9.1(3)) | 1 | MERGED — ids unchanged, nothing renumbered |
| `CORRECTIONS.md` | **2,195** | 15,289 | `COR-01 … COR-09`: three mechanical merge corrections + six registered retractions of inherited premises (U.04, U.05, U.06, U.07, U.09 and the author's own withdrawn "over all six held layers") | 3 | **SEEDED at merge, answering gap G-13** — append-only; every tag reaches both the register layer and a stage volume |
| `quantitative.csv` | 436 | 5,042 | **26** data rows × 12 cols | 2 | APPLIED 26 rows — uniform width, 0 empty cells, 0 duplicate `(date, metric)` |
| `timeline.csv` | 655 | 6,830 | **30** data rows × 11 cols | 2 | APPLIED 30 rows — 0 duplicate `(date_or_range, event)` |
| `sources.csv` | 600 | 6,136 | **8** data rows × 18 cols, keyed **S4423–S4430** (minted centrally; no `PROV-*` left) | 2 | APPLIED 8 rows — 0 duplicate keys; `archived_url` = `NONE_HELD` on all 8 (family (b) UNTRIED, not empty) |
| `conflicts.csv` | 987 | 7,441 | **10** data rows × 15 cols, keyed **U.01–U.10** | 2 | APPLIED 10 rows — 1:1 with the declared anchors, 0 duplicates |
| `data_gaps.csv` | 494 | 4,060 | **13** data rows × 8 cols, keyed **G-01…G-13** | 2 | APPLIED 13 rows — no gap, no repeat; TRIED–ANSWERED / TRIED–UNANSWERED / UNTRIED per row |
| `decisions.csv` | 462 | 3,871 | **8** data rows × 15 cols | 2 | APPLIED 8 rows — 0 duplicate `(date, decision)` |
| `validation.csv` | 241 | 2,093 | **6** data rows × 11 cols | 2 | APPLIED 6 rows — adjudicated block (COR-02), reason on the record |
| `failures.csv` | 306 | 2,660 | **8** data rows × 11 cols | 2 | APPLIED 8 rows — adjudicated block (COR-02); `validation ∩ failures = 0` |
| `channels.csv` | 229 | 1,870 | **5** data rows × 11 cols | 2 | APPLIED 5 rows — 0 duplicate `channel` |

**Registers total: 114 rows requested by `_parts/s1_p1.md`, 114 rows applied, 0 withheld, 0 added.**
Volumes + registers + `CORRECTIONS.md` = **29,718 words / 203,972 bytes** written by this merge; adding the two
read-only `_parts/` emissions and the two `research/` dossiers, the tracked markdown + csv total is
**62,880 words / 433,835 bytes**. No file is at
amber (§9.2) and none is at hard cap. Upload batch 1 = readable volumes, 2 = structured data, 3 = evidence and
audit trail; company_023_gm sits in the **3rd ten-company upload group** (companies 21–30).

## Intermediate merge volumes (`_parts/`) — retained, read-only, NOT edited by the merge

| File | Words | Bytes | Contents | Why retained |
|---|---|---|---|---|
| `_parts/s1_p1.md` | 25,046 | 173,515 | author `s1-gm-p1`'s emission: Header, boundary, §A–§U, claim records, and the nine fenced register blocks at l.616–l.781 | the emission of record for every one of the 114 rows; the verbatim text of the register blocks survives only here. No `SUPERSEDED` footer was written: nothing in it required correction by the merge (§14 rule 4) |
| `_parts/NOTES_gm_p1.md` | 2,561 | 17,530 | author log: tier/tier-reader note, the late-arriving 1937 carrier, trap-by-trap verdicts, `## Untried`, **four `FETCH REQUEST:` blocks** (§6), refusals (§7), merge notes (§8) | the four FETCH REQUESTs are the orchestrator's dispatch list, not a closed matter; §8 is the width statement the merge checked against |

`research/A_chronology_feasibility.md` (4,824 w / 34,179 B) and `research/A4_harvest_mine.md` (731 w / 4,639 B)
were **not** edited: they belong to the probe and fleet-mine passes. `A4` is where the `title:1918 / in-window`
mis-stamp lives (COR-08) — corrected at the use layer, in the registers and the dossier, not by rewriting
another agent's index.

## Evidence base under `sources/` (considered, not merged)

**111 files / 107,780,139 bytes.** `sources/sec/` 85 files (40 filings + sidecars + intake inventories; earliest
filingDate **2009-07-16** — out of every Stage-1 window, carried as perimeter row S4429 and gap G-08);
`sources/periodicals/` 12 (6 layers + 6 sidecars, incl. the 1928 book S4423, the 1937 report S4424 and the 1895
shell S4428); `sources/corporate_print/` 6 (3 layers + 3 sidecars: the 1920 brochure S4426, the 1929 newspaper
S4425 — misfiled, md5-identical to its twin on the periodicals shelf — and the 1931 truck report S4427, refused
into Stage 1); `sources/_index/` 7; `sources/harvest_mine/` 1. **Nothing was deleted, moved, pruned or renamed**
anywhere in this directory tree by this pass; duplicate shelves were md5-compared before any corroboration was
counted (three layers are one document each).

## The five families as the dossier carries them (restatement, not a re-run — this merge did no retrieval)

| family | Stage-1 status as held | what it gave / why it is empty | where registered |
|---|---|---|---|
| **(a) filings** | **RETURNS-NOTHING-WITH-PERIMETER** | `sec_intake` resolves "General Motors" to CIK **1467858** (the 2009 Delaware person, a fourth holder of this name), index floor **2009-07-16**; the historic registrant CIK 140139 is **UNANSWERED** (HTTP 404 `NoSuchKey`, not a null); 319 in-window filings left NOT-ENUMERATED at our own `--max-docs 40` | S4429, G-08, §S, §T, U.01 |
| **(b) web archives** | **UNTRIED** | no wayback capture exists under `sources/` for any layer; `archived_url` reads `NONE_HELD (…)` in all 8 source rows; `tools/cdx_intake.py` was never run for gm | `sources.csv` `archived_url`, §S, NOTES §5 |
| **(c) periodical corpora** | **RETURNS** | the load-bearing in-window layers: 1928 book (S4423), 1929 newspaper (S4425), plus the 1895 shell used only as a negative control (S4428); **7 in-window Google Books items reached but never text-resolved (HTTP 503)** — UNANSWERED with a remedy | §B–§T, G-01, FETCH REQUEST 2 |
| **(d) digitised corporate print** | **RETURNS** | 1920 Dayton-Wright divisional brochure (S4426, earliest held naming), 1937 registrant annual report (S4424, `RETRO` only), 1931 GM Truck report (S4427, refused into Stage 1); the fleet `NULL` for this family is **refused** — it is a year-faceted `numFound=0` (RD-130) | §T, G-04, U.09, FETCH REQUEST 1 |
| **(e) auction / museum documentary** | **UNTRIED — structurally: no tool exists** | the family that produced another company's founding papers; for a 1908 holding-company act whose paper is a charter and stock certificates it is the most relevant untouched route | G-02, U.03, FETCH REQUEST 4 |

Tier as inherited: **Stage 1 = T2 core** (2 of 5 families return in-window opened text), Stage 2 = T3
provisional, Stage 3 = T3 provisional-and-not-yet-a-verdict. Not re-tiered by this merge; the disagreement the
author logged (`_parts/NOTES_gm_p1.md` §2) is carried in `stage_1.md` §boundary and §S, and the `--tier auto`
reader artifact is named above rather than repaired in the data.

**Cross-references that are still wrong, and are left wrong on purpose.** Three lines in `stage_1.md` cite a
section **§V** this part never wrote (l.7, l.17, l.44 in the part's numbering), and the part has no `## Untried`
heading — its untried routes live in §S and in `_parts/NOTES_gm_p1.md` §5. Both are named in the merge record
and in `03_quality_control/gm_s1_merge.md` for the audit pass; a merge does not tidy another pass's released
words.
