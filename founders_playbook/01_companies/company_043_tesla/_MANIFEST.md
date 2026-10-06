# _MANIFEST — company_043_tesla

Counts regenerated **2026-09-30** by the Stage-1 merge pass (`tesla-s1-merge`) and **re-measured from disk by
repair pass 1 the same date (`tesla-repair-1`, 0 web calls)**, on the written bytes after the last append (word = whitespace-delimited tokens, `wc -w`-equivalent; byte = file size). Per method §9.6 every
directory carrying split files keeps this register so a file can be checked against the ceilings before handoff
or upload. **The merge's own total row did not foot against its own cells** (published 13,329 w / 111,343 B
against cells summing to 14,323 w / 111,943 B), and this file printed its last two sections **twice**, with a
table row glued onto the end of a prose paragraph; both are repaired here (BLOCKER-4, A9). The superseded
figures stay quoted in this sentence so the correction is itself checkable.

**Nothing in this directory is a cleanup target** (§14 rule 4): `_parts/`, `research/`, `sources/` and
the superseded emissions are left exactly where they are.

**Which ceiling governs which file.** §9.1's hard upload constraint (500,000 words / 200 MB per file) governs
every file including the restored primaries under `sources/` — the largest held document, the 424B4 submission
txt, is 4.7 MB, ~2% of the byte ceiling. §9.2's **60,000-word hard cap** governs `stage_1.md`. §15.2's **8,000-word
T3 figure** governs the *dispatch budget*, not the written evidence (RD-122; §9.6 forbids trimming evidence to fit
a file limit; §15.4 makes a missed length target legitimate).

## Deliverables (read these)

| File | Words | Bytes | Contents | Upload batch | Status |
|---|---|---|---|---|---|
| `stage_1.md` | **54,903** | 382,275 | Merge header + Stage-1 merge note + widened `ANCHORS: U.1-U.23` + Volume 1 (part 1: §Header, §Boundary, §A–§F, claim records P1-01–P1-33, register emission) + Volume 2 (part 2: §G–§U, claim records P2-01–P2-54, its `## Untried`, register emission) + merge `## Untried` addendum + `U.23` anchor + COR-01…COR-06 propagation block + **`## Stage-1 repair pass 1` block appended, a `COR-07` row, and repair annotations bracketed inside the two verbatim volumes (appended to the sentences they correct, never substituted for them)** | 5 | **MERGED 2026-09-30, ONE volume.** 91% of the 60,000 hard cap → under it, so **no §9.3 split performed**; above the 40,000 soft target (amber, allowed to finish as one file) and 6.7× the T3 8,000 target (**known accepted state**, see "Budget" below) |
| `CORRECTIONS.md` | 2,792 | 19,666 | COR-01…COR-07. COR-01 **re-grades itself**: the merge's conclusion that the 2009-12-31 refundable-reservation balance is UNKNOWN is withdrawn in place, with the carrier sentences quoted; COR-07 carries the four register statements the bytes do not support | 5 | WRITTEN by this merge (Tesla had none); **superseded-in-place + extended by repair pass 1**. `gates.py` propagation: **7 ids, 7 reach registers, 7 reach volumes** |
| `stage_1_index.md` | 2,005 | 13,369 | Ordered volume list, word counts, section locations, anchor ranges, register table, the six merge decisions, **plus repair pass 1's re-adjudication of decision 5 and of `U.23`** | 5 | WRITTEN by this merge; repaired by pass 1 |

## Structured dataset (canonical registers, company root)

| Register | Rows | Cols | Words | Bytes | Requested | Applied by |
|---|---|---|---|---|---|---|
| `sources.csv` | **24** | 18 | 4,261 | 33,577 | 40 | 16 aliased into 8 fold groups; **8 rows' fold claim corrected at repair** (`S4369`, `S4371`, `S4372`, `S4375`–`S4377`, `S4389`, `S4390`: the boilerplate 'nothing dropped' is withdrawn, and `S4390`'s title no longer claims CDX rows) |
| `quantitative.csv` | **62** | 12 | 2,567 | 20,945 | 61 | **0 folds; +1 row minted at repair** (2009-12-31 reservation balance) |
| `timeline.csv` | **46** | 11 | 2,004 | 16,101 | 47 | 1 fold (2010-06-29 closing edge); silence row narrowed at repair |
| `conflicts.csv` | **23** | 15 | 3,402 | 24,056 | 22 | +1 minted at merge (`U.23`), **re-graded at repair; no row added or removed, parity stays 23↔23** |
| `data_gaps.csv` | **16** | 8 | 1,829 | 13,063 | 23 | 8 aliased into 7 fold groups; **+1 row minted at repair** (the near-collapse gap `failures.csv` pointed at but no row carried) |
| `decisions.csv` | **9** | 15 | 951 | 7,089 | 9 | 0 folds; row 1 re-labelled carried-and-supported |
| `validation.csv` | **9** | 11 | 541 | 4,223 | 9 | census-AMBIGUOUS block, attributed by content; **Daimler row re-dated 2009-05 → 2009-11** |
| `failures.csv` | **11** | 11 | 814 | 5,990 | 11 | census-AMBIGUOUS block; **two rows repaired** (ten→thirteen months / 2008-02→2009-03; memory-layer row labelled an evidentiary null) |
| `channels.csv` | **10** | 11 | 468 | 3,768 | 10 | 0 folds |
| **Total** | **210** | | **16,837** | **128,812** | **232** | **16 collision groups, 0 refused; repair pass 1 adds 2 rows and deletes none** |

**The Total row foots against the cells above it (measured twice: once mid-pass at 16,494 / 126,229, and again after
the `sources.csv` fold-claim sweep, which added 343 words and 2,583 bytes to that file): 4,261+2,567+2,004+3,402+1,829+951+541+814+468 = **16,837** words
and 33,577+20,945+16,101+24,056+13,063+7,089+4,223+5,990+3,768 = **128,812** bytes; rows
24+62+46+23+16+9+9+11+10 = 210.** The merge's published **13,329 / 111,343** were transpositions of the
**14,323 / 111,943** its own cells summed to - measured again on this pass, and the per-cell numbers matched the
disk exactly. Row growth is +2 (`quantitative.csv`, `data_gaps.csv`); no row was deleted. **23 register rows** carry this pass's markers (sources 8, quantitative 8, timeline 1, conflicts 1, data_gaps 1, decisions 1, validation 1, failures 2); the cell-level detail is in
`03_quality_control/tesla_s1_repair_pass1.md`.

Column counts are unchanged by the repair; headers remain **byte-identical to `company_001_amazon`'s conformant ones** (verified string-for-string against all
nine reference headers on this pass; Amazon supplied **format only — no Amazon data was read into this company**).
`stage` column: **all 210 rows carry the literal `stage1`** — no numeric stage value exists anywhere in this
register set (the vocabulary RD-048/RD-075 fixed and a numeric `stage` still leaked into one company's
`sources.csv`). **Normalisation on touch:** the probe emission's 25 rows carried `company = tesla`; the **9** of them that survive as
their own rows (6 conflicts `U.1`-`U.6`, the two probe-only source rows `S4391`/`S4392`, and the surviving probe gap
row for the untried documentary family) were normalised to `Tesla Motors Inc`, the name the registrant filed under;
the other **16** aliased rows survive verbatim inside `MERGE[…]` alias text - `company` cell included - and were not
rewritten.

## Intermediates and read-only evidence (do not re-apply, do not clean)

| Path | Words | Bytes | Status |
|---|---|---|---|
| `_parts/s1_p1.md` | 13,737 | 95,964 | **SUPERSEDED notice appended 2026-09-30** (body carried verbatim into `stage_1.md` under the heading `## Volume 1`; **no character offset is published here any more** - REPAIR 2026-09-30 (tesla-repair-1): the merge's 9,746 and audit 1's 9,859 measured different things (the injected `## Volume N` heading falls between them), this pass's own annotations moved every later offset again, and audit 1's evidence offsets are character- not byte-based - so §14 rule 12 applies and the slice is addressed by its heading and its first body line. **Truncation reported, not repaired:** the file ends at a stray `#` after its `data_gaps` block and its `## Untried` — cited four times in its own body — is not on disk (RD-132's Nvidia defect class). §14 rule 4: it stays exactly where it is |
| `_parts/s1_p2.md` | 37,770 | 260,447 | **SUPERSEDED notice appended 2026-09-30** (body carried verbatim into `stage_1.md` under the heading `## Volume 2`; offset retired for the same reason - the merge printed 102,736 and audit 1 re-measured 103,967, and any such address must be re-located before it is cited) |
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
carries a `follow_up_task`, so no High gap is unassigned. **[repair pass 1]: the 424B4 balance-sheet column heads
come OFF that list for the reservation line — the 2009-12-31 balance was never missing from the held bytes, only
unread (COR-01). What a fetch can still settle is the gross receipts/refunds flow, open at `U.23`'s residual and at
`data_gaps.csv`; the three staff PDFs (FRA-3) and the CDX re-query (FRA-1) stay outstanding.**

## Gate finding — named with its tier and the tool's date (A6)

| Run | Bytes | Tier as resolved | Result |
|---|---|---|---|
| merge pass | pre-repair | `--tier T3` (the tier the merger used) | Findings: 2 \| Passes: 20 → `03_quality_control/tesla_s1_gates.md/` |
| audit 1 | same bytes, tool re-edited between runs | `--tier auto` → T3 | Findings: 2 \| Passes: 18 → `03_quality_control/tesla_s1_gates_audit1.md` |
| **repair pass 1** | **repaired bytes** | `--tier auto` → **T3** from `research/A_chronology_feasibility.md` | **Findings: 2 \| Passes: 18 — both ADVISORY**: `stage_1.md` over the T3 8,000-word density target (NOT a split mandate, NOT a defect; §9.2 splits only above the 60,000 hard cap) and the quote gate's 16-of-58 unmatched triage list. **0 substantive** → `03_quality_control/tesla_s1_gates_repair1.md` |

`tools/gates.py` on this disk is dated 2026-10-06 17:39 and was edited three times on 2026-09-30; pass counts are **not**
reproducible across those edits, which is why the tier and the tool date are printed above rather than a bare
number (RD-122). The merge's published "Passes: 20" and this pass's 18 are the same two findings.

## Repair pass 1 — what this file does NOT claim

`_parts/s1_p1.md` and `_parts/s1_p2.md` were **not touched**: they already carry their SUPERSEDED 2026-09-30
notices, are read-only to this pass, and every repair inside the merged volume is a bracketed annotation appended
to the sentence it corrects. The stale "UNKNOWN"/"not carried" sentence at
`03_quality_control/tesla_s1_merge_notes.md` §7 is **not in this pass's write set** — it belongs to the merge
pass's own report, and the residual hit is carried to the certifier in
`03_quality_control/tesla_s1_repair_pass1.md` rather than edited by a non-owner (§14 rule 7, one path one owner).
A **different** agent must re-certify Stage 1; this pass does not sign its own repair (§15.6).
