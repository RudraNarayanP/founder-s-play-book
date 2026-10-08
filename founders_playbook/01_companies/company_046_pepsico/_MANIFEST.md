# _MANIFEST.md — company_046_pepsico

Regenerated 2026-10-07 by `merge-pepsico` after the last byte of the merge was written (§9.6: counts are live,
not inherited). Counts re-measured with `len(re.findall(r"\S+", text))` and `os.path.getsize`, not copied from
any earlier pass.

| File | Words | Bytes | Sections contained | Upload batch | Status |
|---|---|---|---|---|---|
| `stage_1.md` | 22,958 | 150,036 | MERGE RECORD (assembly, register application, id map, validation/failures adjudication, anchor parity, census before/after, the four carried results, the five families, tier, tool facts, COR-01…COR-06) + Header + boundary + §A–§U + claim records `P1-01…P1-42` (§T.2) + §Untried + §Fetch requests + the closing coverage paragraph | 5 (companies 041–050) | MERGED, complete; 0 PENDING sections |
| `sources.csv` | 1,727 | 15,281 | 16 rows × 18 cols, keys S4479–S4494 | 5 | APPLIED |
| `quantitative.csv` | 641 | 6,959 | 25 rows × 12 cols | 5 | APPLIED |
| `timeline.csv` | 640 | 5,181 | 16 rows × 11 cols | 5 | APPLIED |
| `conflicts.csv` | 1,598 | 11,171 | 15 rows × 15 cols, keys U.1–U.15 | 5 | APPLIED |
| `data_gaps.csv` | 691 | 4,988 | 15 rows × 8 cols | 5 | APPLIED |
| `decisions.csv` | 279 | 2,323 | 4 rows × 15 cols | 5 | APPLIED |
| `validation.csv` | 274 | 2,179 | 4 rows × 11 cols (adjudicated block, COR-06) | 5 | APPLIED |
| `failures.csv` | 455 | 3,748 | 8 rows × 11 cols (adjudicated block, COR-06) | 5 | APPLIED |
| `channels.csv` | 219 | 1,825 | 3 rows × 11 cols | 5 | APPLIED |
| `CORRECTIONS.md` | 953 | 6,634 | COR-01 … COR-06 + "Not corrected, and why" | 5 | WRITTEN |
| `_parts/s1_p1.md` | 25,525 | 178,526 | the author's emission of record, verbatim, + the merge's superseded footer | 5 | READ-ONLY — **DO NOT RE-APPLY its blocks** |
| `_parts/NOTES_pepsico_p1.md` | 1,534 | 10,602 | author log | 5 | untouched by the merge |
| `_parts/_tmp_pepsico_layers.json` | 1,165 | 9,794 | the `ia_text.py list-files --id 01-pepsi-co` stdout (102 layers, 17,860,942 B), **relocated here from the repo root by COR-04**, contents unchanged | 5 | cited by S4492 and `data_gaps.csv` S-10 |
| `research/A_chronology_feasibility.md` | 4,632 | 31,647 | probe dossier — **T3 register**, five-family verdict, A.1–A.12 | 5 | provenance, not a register |
| `research/A4_harvest_mine.md` | 993 | 7,298 | later harvest-mine dossier (mtime after the probe); emits no register rows | 5 | provenance, LEAD ONLY |

**Register totals: 106 rows across nine registers, 106 requested, 106 applied, 0 unapplied, 0 added, 0 folded,
0 refused.** Stage vocabulary: `stage` is the controlled literal **`stage1` on all 106 rows of all nine files**;
a per-file distinct-value scan returned `['stage1']` every time, so **0 numeric stage values were found and
there is no §13 normalisation count to report**.

**Non-destruction accounting, line by line.** Part as emitted 25,400 words → volume 22,958:

| line | words | running |
|---|---|---|
| `_parts/s1_p1.md` as emitted | 25,400 | 25,400 |
| − the part's filename H1 (replaced by the volume H1) | −21 | 25,379 |
| − the nine fenced register blocks with their headings and markers, moved into the CSVs (§9.1(2), COR-05) | −6,245 | 19,134 |
| + the nine printed pointers naming where each block's rows and verbatim text live | +557 | 19,691 |
| + the four printed merge annotations (register-section scope note 54 w; three COR-04 path notes, net +44 w) | +98 | 19,789 |
| + the MERGE RECORD header | +3,169 | **22,958** |

Nothing in that arithmetic is a deletion of evidence: the 6,245 words moved **into** the nine CSVs (106 rows on
disk, censused), and the part still holds them verbatim. **42 claim records before, 42 after; 15 §U anchors
before, 15 after; 106 register rows requested, 106 applied; 5 FETCH REQUESTS before, 5 after; 12 `## Untried`
items before, 12 after.**

**Coverage — what does not exist for this company, named rather than papered over.** No `stage_1_index.md`
(one volume; §9.3 lists an index under the split procedure), no `stage_1_claim_records.md` (the claim records
are §T.2 of the narrative and were not cut out of a section), no `stage_2*`/`stage_3*` (not dispatched), no
`context_appendices.md` (this dossier's environmental context is inside §E/§G and is under the §9.1(4) size
trigger), no `sources/web_archive/` (family (b) **UNTRIED**, not empty), no bytes in `sources/corporate_print/`
(family (d): a **tool artefact**, not a null — its in-window layers are named and costed at S4492), no XBRL
series, and **0 of the 48 named in-window archive layers fetched** (FETCH 1 stays open). `sources/periodicals/`
holds 11 layers and `sources/sec/` 27 documents = **38 held items**, which is the population every occurrence
count in the registers was measured over.

**Tier as published here: T3 register** (probe §A.7, re-measured by the author, carried by the merge; 1B/1C
PROVISIONAL pending FETCH 1). The wave plan's dispatch label said T2 — **the probe's measured tier governs**
(COR-02). `gates.py` was run with `--tier register` passed explicitly and reports 18 passes; the one substantive
finding is the quotes gate's scope, documented in `03_quality_control/pepsico_s1_merge.md`.

STATUS: WRITTEN 2026-10-07
