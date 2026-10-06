# _MANIFEST — company_014_cigna (Stage 1)

**Counts regenerated 2026-10-06** by the Stage-1 merge pass (`merge-cigna`) with `wc -w` / `wc -c` on the
bytes **after the last write of this operation** (word = whitespace-delimited token, byte = file size). Every
figure below is a measurement, not a recollection: re-measure before publishing any of them again. The merge
applied **78 register rows against 78 requested** — the account, the census readings before and after, and the
validation/failures adjudication live in `03_quality_control/cigna_s1_merge.md`.

**Which ceiling governs which file.** §9.1's hard upload constraint (**500,000 words / 200 MB per file,
whichever binds first**) governs every file including the restored evidence under `sources/`. §9.2's caps
govern a stage volume and its companion deliverables: **soft target ≤ 40,000 words**, amber 40,000–60,000,
**hard cap 60,000**. The **tier cap is a density target, not a file limit** (RD-122): `tools/gates.py --tier
auto` read this dossier's tier as **core = T2** and applied the **22,000-word** T2 cap to `stage_1.md`, which
measures **14,513 words** — **66% of the T2 tier target (22,000), 36% of the 40,000-word soft target, 24% of
the 60,000-word hard cap.** No overage, no split (§9.3), and nothing was trimmed to reach it.

**Tier as issued, as measured, and as read by the machine — three different numbers, all kept.** The probe
(`research/A_chronology_feasibility.md` §7) issues **Stage 1 = T2 core, PROVISIONAL** on the lineage frame and
**T3 register** on the strict-registrant frame (0 families name CIK 0001739940 before 2018). This merge did
**not** re-tier. `gates.py --tier auto` now resolves the dossier to **core (22,000)**; the probe recorded the
same detector printing **T3** on 2026-10-06 because of its first-30,000-character lexicographic tie-break
(§13). That divergence is registered as conflict **U.4**, not fixed by deleting the T3 mention. A tier-cap
overage would be advisory and would **not** be evidence to delete.

## Deliverables (read these)

| File | Words | Bytes | Contents | Status |
|---|---|---|---|---|
| `stage_1.md` | **14,513** | 94,432 | merge record (assembly, 78-row application account, `CG01–CG16`→**S4407–S4422** id map, folds, anchor parity, two tier frames, carry-forward, COR-01…COR-03) + the author's body **unchanged and unre-numbered** (Header, §boundary, §A–§U with §U.1–§U.6, 25 claim records A01…S01, `## UNTRIED` 9 items) + the register-application record | **MERGED 2026-10-06**; one volume; under every cap that applies |
| `sources.csv` | 872 | 9,346 | 16 data rows × 18 cols, keys **S4407–S4422**, `independence_note` per row, three SEC/lineage collapses honoured, 3 decoy rows + 1 unheld pointer row kept as UNTRIED carriers | APPLIED 16/16 |
| `quantitative.csv` | 353 | 3,511 | 15 × 12 — the INA 1979 printed set plus 1 ESTIMATE, 1 DERIVED (flagged mixed bases) and 1 corpus-census row | APPLIED 15/15 |
| `timeline.csv` | 441 | 4,241 | 14 × 11 — Line 1 (1792 → 1994/95), Line 2 (1982 as hypothesis only), Line 3 (UNKNOWN incorporation, 2018 floor, 2018-12-20 closing) | APPLIED 14/14 |
| `data_gaps.csv` | 404 | 3,381 | 12 × 8 — 6 High / 4 Medium / 2 Low; follow-up tasks cite FR-1…FR-7; row 12 is the record-selection null named as a permanent deliverable | APPLIED 12/12 |
| `conflicts.csv` | 424 | 3,606 | 6 × 15 — **U.1–U.6, one row per declared anchor, 1:1 with §U** | APPLIED 6/6 |
| `failures.csv` | 223 | 2,139 | 6 × 11 — adverse signals; block bound at merge (COR-02) | APPLIED 6/6 |
| `validation.csv` | 150 | 1,503 | 4 × 11 — validating signals; block bound at merge (COR-02) | APPLIED 4/4 |
| `decisions.csv` | 173 | 1,715 | 3 × 15 — HMO International 1978-12; the 1979 prepaid expansion mix; the 1979 underwriting posture | APPLIED 3/3 |
| `channels.csv` | 90 | 908 | 2 × 11 — acquire-then-brand; hospital management contracts | APPLIED 2/2 |
| `stage_1_index.md` | 1,141 | 7,053 | volume index: section map, anchor→register homes, register counts, reading order | MERGED 2026-10-06 |
| `CORRECTIONS.md` | 1,076 | 7,435 | COR-01 id supersession · COR-02 validation/failures binding · COR-03 the probe's withdrawn 17:20 zero-count / T3-only claim · "Not corrected, and why" | LIVING — append, never rewrite history |

**This register is not self-listed** — a file cannot publish its own final size. It measured 10,573 bytes at
the previous touch and is re-measured whenever it is written; the row that changes its size is the one that
would have to quote it.

Upload batch 1 = the readable stage volume; batch 2 = the nine registers + index + corrections; batch 3 =
`_parts/`, `research/` and `sources/` (evidence and audit trail). **No file was shortened to meet a number**
(§9.6 forbids it).

## Intermediate emission (`_parts/`) — retained, read-only

| File | Words | Bytes | Contents | Why retained |
|---|---|---|---|---|
| `_parts/s1_p1.md` | 16,016 | 114,204 | the whole author emission: Header, §boundary, §A–§U, 25 claim records, `## UNTRIED`, and the nine fenced register blocks (78 rows, l.492–l.651) — **plus the `SUPERSEDED 2026-10-06` footer the merge appended** (15,707 words are the author's body and blocks; 309 words and 1,956 bytes are the footer) | the emission of record. The merge moved register data out of it and edited nothing above the footer; the footer supersedes **placement and keys only** — no narrative word needed correction. The three merge corrections (key / propagation / schema) are in `CORRECTIONS.md` |
| `_parts/NOTES_cigna_p1.md` | 1,003 | 7,830 | the author's log: byte-verification pass, new evidence mined, register tally, refusals, gate record | shows what the merge accepted and what the author refused to claim |

## Research dossiers (scope of record — not touched by the merge)

| File | Words | Bytes | Role |
|---|---|---|---|
| `research/A_chronology_feasibility.md` | 7,190 | 48,751 | issued the Stage-1 window (1979-01-01 → 1995-12-31, PROPOSED), the tier verdicts, the five-family table, the census and FR-1…FR-7 |
| `research/A4_harvest_mine.md` | 833 | 5,611 | harvest-mine census carrier — 96 / 12 / 81 at l.5 as re-read by the author (79 / 12 / 65 as the probe caught it; movement = U.5) |

## The five families, carried into this manifest with their states distinct

Verdict as issued by the probe for **Stage 1 (1979-01-01 → 1995-12-31)**; **TRIED–ANSWERED**,
**TRIED–UNANSWERED** (attempted, the tool or network refused — remedy named) and **UNTRIED** (0 calls, never
reported as a null) are kept apart in every row. No family is reported empty that was not attempted.

| # | family | state | measured basis | in-window Tier-1 text? | closing route |
|---|---|---|---|---|---|
| (a) | SEC / EDGAR filings | **TRIED–ANSWERED as a perimeter; UNTRIED for the predecessor registrant** | 1,018 filings enumerated, 0 UNANSWERED slices, perimeter 2018-05-16 → 2026-09-08; Stage-1 in-window pass stored **0** documents; 18 in-window filings never listed at `--max-docs 30` → **TRIED–UNANSWERED** inside this family | **NO** — and structurally so: this registrant's EDGAR life begins 23 years after the window closes | **FR-1** (predecessor CIK, CIK-scoped write paths), **FR-2** (certificate of incorporation / first 10-K), **FR-3** (re-run at `--max-docs 60`) |
| (b) | Web archives | **UNTRIED — 0 calls** | no `sources/web_archive/`, no sidecar, no `http_status` residue: not a refusal, a route never attempted | NO — a search never run | **FR-6** (first CDX/Wayback pass; also the route that moves Stage 3 to T1) |
| (c) | Periodical corpora | **TRIED–ANSWERED for the IA main thread; TRIED–UNANSWERED for Chronicling America and HathiTrust; TRIED–ANSWERED as leads-only for Google Books; 81 of 96 candidate rows UNTRIED at `--limit`** | three in-window SCOTUS microfiche records held (1989 / 1991 / 1994-95); CA: 4 cigna rows 404/UNANSWERED and 7 of 7 URL shapes CHALLENGED (403) — "no CA zero may be cited as a null"; HT: 1 row, no status; GB: 11 rows, 0 bytes fetched | **YES** — but the subject is the predecessor, not this registrant | **FR-4** (mine the backlog), **FR-5** (CA endpoint from Actions egress) |
| (d) | Digitised corporate print | **TRIED–ANSWERED by document class, off-shelf; TRIED–UNANSWERED as the harvester's own `corporate_print` task** | `INAC2115_1979` (INA Corporation Annual Report 1979, 111,357 B) prints the 1792 origin narrative and the whole financial set; it was fetched by the `internet_archive` task and stored under `periodicals/`, so family counting follows document class not shelf (**U.6**); both CP tasks are YEAR-faceted (RD-130) and 0 facet-free CP rows exist for any company | **YES** — one annual report, in-window (1979), Tier-1, self-reported and retrospective | **FR-4** (facet-free CP + an `ina corporation` creator task) |
| (e) | Auction / museum / manuscript | **UNTRIED — 0 calls** | no directory, no task in `queries.json`, no residue of any kind | NO — a search never run | a scripted auction/museum pass per the probe brief's tool forms; the INA/CIGNA archival bodies (Hagley, Historical Society of Pennsylvania) are the named class |

**Second frame, kept distinct and never averaged:** on the **strict-registrant** reading of the same window all
five families return **0** — no held document in any family names CIK 0001739940 before 2018 — which is the
**T3 register** row of the probe's §7 and the reason U.1, U.3 and the Line-3 timeline rows exist.

## Census of this operation (measured, not asserted)

| reading | before any write | after the final write |
|---|---|---|
| structured blocks parsed | 9 | 9 |
| rows requested | 78 | 78 |
| `conflicts.csv` present / missing | 0 / 6 | **6 / 0** — anchor parity proven |
| `sources.csv` present / missing | 0 / 16 | 0 / 16 — the 16 "missing" keys are the superseded local tags `CG01–CG16`; the minted ids S4407–S4422 are on disk (COR-01) |
| unattributed block-groups | 2 (validation/failures, identical 11-col schemas) | 2 — same schema property; adjudicated by reading, recorded in the merge report and COR-02 |
| third emission in `research/*.csv` | none (0 CSVs under `research/`) | none |

## Gate and merge records

- `03_quality_control/cigna_s1_merge.md` — the merge's live account: census before and after, the
  validation/failures adjudication, the id allocation, the five cells annotated with COR pointers, the uncarried
  follow-ups and the 78-requested / 78-applied total.
- `03_quality_control/cigna_s1_gates_merge.md` (+ `.json`) — the gate run after the last write:
  **Findings 1 | Passes 19**; `corrections propagation` and `anchors parity` both pass; the single finding is
  `quotes/verbatim` on a quotation of `research/A4_harvest_mine.md` l.5, which the quote gate cannot match
  because its corpus is `sources/**` only (evidence recorded in the merge report; the data was left alone).
- `03_quality_control/cigna_s1_gates_p1.md` — the author's pre-merge gate (coverage-only), and
  `cigna_s1_gates_probe.md` — this merge's intermediate gate run, kept because the merge report cites the quote
  finding it already showed.

## Open items this merge did NOT close (named, not dropped)

1. `research/_EVIDENCE_CACHE.md` still does not exist. `data_gaps.csv` row 11 asks for it "at merge", but no
   cache was among this pass's claimed deliverables; the row stays **OPEN** (CORRECTIONS.md, "Not corrected").
2. **FR-8** has no `data_gaps.csv` row (the author emitted none); its home is UNTRIED item 8 and the U.2
   residual cell.
3. 18 in-window filings never listed (FR-3) and 81 of 96 harvest candidate rows unmined (FR-4) remain open
   exactly as measured; the census numbers U.5 carries are movement, not verdicts.
4. The two tier frames stay unreconciled on purpose: reconciliation requires FR-2, and until then any single
   tier number quoted from this company is a misquote.
