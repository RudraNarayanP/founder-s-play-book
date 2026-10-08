# jnj Stage-1 MERGE LOG — company_045_jnj

**Merge agent:** `merge-jnj`. **Date:** 2026-10-07. **Source part:** `_parts/s1_p1.md`
(author `s1-jnj-p1`, 32,410 words as emitted, §A–§U complete, 23 claim records, 12 anchors U.001–U.012).
**Single part → single volume.** This is a **merge**, not an audit and not a certification: per the wave plan
the merger may not certify; audits come from different agents, then a certifier who is neither author, merger,
auditor nor repairer. Nothing here certifies the dossier.

## Procedure followed (and the two command-shape facts that make it work)

1. **Census first.** `python tools/merge_census.py --company-dir
   founders_playbook/01_companies/company_045_jnj --verbose`. Run **from the repo root**: the tool resolves the
   reference-header path relative to CWD, so run from inside `founders_playbook/` it finds no Amazon schema and
   reports `no attributable merge-request blocks found (UNANSWERED, not a pass)` — that message is a working-
   directory artifact, not an empty dossier. From the root it parses **9 blocks** and lists the request side.
2. **Ids only from `id_mint.py`.** `python tools/id_mint.py --count 16 --company company_045_jnj --claim
   --agent merge-jnj` → **S4463 … S4478** (16 source ids, claimed in `00_universe/_ID_BLOCKS.tsv`). Allocated
   **above the highest live id**: `--audit` before the mint read a lower `next assignable`, but a concurrent
   merge had taken the intervening block, so the tool returned S4463+ and re-entered **no gap** — including the
   `S4222–S4229` Microsoft/Target collision the brief names, which sits below and was not touched. No id was
   minted by the author; the part's `source_id` was deliberately provisional (`P1Sxx`).
3. **Duplicate-key checks across all blocks in ONE operation**, not per block: every header byte-identical to
   `company_001_amazon/<name>`; `stage` = literal `stage1` on every row; **0 rows off-header-width, 0 empty
   cells, 0 duplicate keys** in the two keyed registers (`source_id` S4463–S4478; `conflict_id` U.001–U.012).
   Rows re-serialised through `csv.writer` (LF, UTF-8, no BOM, trailing newline, RFC-4180).
4. **`validation` / `failures` adjudicated by CONTENT, with the reason recorded.** The two registers share a
   byte-identical 11-column header, so the census reports the pair `AMBIGUOUS` and cannot bind them (its hint
   digest even echoes a different block's rows — a known tool artifact; not evidence). Bound on the author's
   own `### validation.csv` (7 positive-demonstration rows) / `### failures.csv` (5 adverse/record-selection
   rows) headings and confirmed by content. Recorded as **COR-02** and in `stage_1.md` §L/§M.
5. **No renumbering.** Section letters, claim ids and conflict keys are the author's, applied verbatim.
6. **`_parts/` is read-only.** The part was read, never edited; no footer was appended. Supersession of the
   emission's placement/key-space is recorded in `stage_1.md` MERGE RECORD + `CORRECTIONS.md`.
7. **Live `wc`-measured counts** published in `_MANIFEST.md` after the last write.

## Register application — APPLIED n rows per register

| register | requested (breakdown) | APPLIED | cols |
|---|---|---|---|
| sources.csv | 16 | **APPLIED 16 rows** | 18 |
| quantitative.csv | 21 | **APPLIED 21 rows** | 12 |
| timeline.csv | 18 | **APPLIED 18 rows** | 11 |
| decisions.csv | 8 | **APPLIED 8 rows** | 15 |
| validation.csv | 7 | **APPLIED 7 rows** | 11 |
| failures.csv | 5 | **APPLIED 5 rows** | 11 |
| channels.csv | 4 | **APPLIED 4 rows** | 11 |
| conflicts.csv | 12 | **APPLIED 12 rows** | 15 |
| data_gaps.csv | 11 | **APPLIED 11 rows** | 8 |

**Every requested row was applied: 0 unapplied, 0 folded, 0 added by the merge.** No unapplied row exists to
name. (The author's prose "rows withheld on purpose" describes rows they chose **not to emit** — noise-carrier
sources and the `1886`-only Canadian layers — which is an emission decision, not an applied-register gap.)

**Row-count reconciliation (defect found at merge, not silenced).** The task and `_parts/s1_p1.md`
`## registers-part-2` state **101 requested** and print `16+21+18+8+7+5+4+12+11 = 101`. That per-register
breakdown is authoritative and matches the census request side exactly — but **the nine numbers sum to 102, not
101**. The `= 101` is an arithmetic slip in the author's own tally. The merge applied all **102** emitted rows;
it did **not** delete a real row to reach a headline figure (cutting evidence to fit a number is forbidden,
§9.6). **Honest count: 102 applied against a 102-row per-register request; the "101" is a mis-sum, not a row.**

## Anchor ↔ conflict parity

The part declares **12 anchors U.001–U.012**, each with a §U section; `conflicts.csv` carries exactly **12**
rows keyed U.001–U.012. Census re-run after the final write: `conflicts.csv | requested 12 | present 12 |
missing 0`. Gate `anchors`: **parity 12 narrative ↔ 12 register anchors** and **citation resolution: every
register-cited anchor resolves (12 distinct ids)**. 1:1 holds, no orphan, no unanchored row. The `sources.csv`
line still lists the 16 `P1Sxx` tags as "missing keyed rows" — the **expected residue of a central mint** (the
globals S4463–S4478 are present; the local tags live only in the read-only part and the id map).

## Five families, as carried through the merge (verbatim verdicts preserved)

| Family | State carried into the merged volume | Verdict class |
|---|---|---|
| (a) Filings | 3,371 EDGAR rows re-measured; earliest 1994-03-10, latest 2026-09-10, 65 forms, **0 forms begin `S-1`, 0 rows ≤ 1960-12-31**; 26 bodies on disk all `(PB)`, `1886`×0 | **TRIED–ANSWERED — documented in-window NULL** (route answered); 134 no-`primaryDocument` + `_SKIPPED`/`_UNANSWERED` slots = UNANSWERED, not null |
| (b) Web archives | `tools/web_domains.json` has **no `jnj` entry** → `cdx_intake.py` never ran for this slug; the probe's 1996 CDX floor is a 2-URL ad-hoc measurement, not the archive | **UNTRIED** (no cited jnj domain → no route; never a null). In-window **impossible by construction** (domains captured 1996, 36 yrs past the close) |
| (c) Periodical corpora | 5 American Druggist volumes read (1896/1902×2/1904×2), **47 naming lines** with printed legs; **790 of 795 Druggist unopened; 44 of 44 *Pharmaceutical Era* unopened**; CA `CHALLENGED` on all 7 shapes | **TRIED–ANSWERED (in-window Tier-1 text) + UNTRIED at 99% + UNANSWERED for Chronicling America (never a null). THE independent family** |
| (d) Digitised corporate print | 6 company-authored layers read to the line; **504 of the corpus's 642 namings**; + the `(PB)` 1970 annual report | **TRIED–ANSWERED — the richest family, and it is SELF-NARRATIVE** (U.012) |
| (e) Auction / museum / manuscript | **no tool exists at all** (`tools/HARVEST_README.md` family 4 "not implemented"; no read-only public API verified; one museum artefact repo-wide, at Walmart, never jnj) | **UNTRIED — structural** (a statement about us, not the record). **Never a null.** |

Stage-1 window carried as the author's **1886\*–87 → 1904-12-31**; the harvester's 1886→1960 bracket is rejected
as a **retrieval setting**, not a boundary (§Boundary 4; U.012). Family (b)/(e) are UNTRIED because **no route
exists**, never because a null was returned.

## Late-arrival accounting — preserved in `_MANIFEST.md` and `stage_1.md` MERGE RECORD (COR-03)

The corpus grew after the probe; the merge keeps both measurements rather than replacing one with the other:

- **15 layers / 23,308,643 B / 642 entity namings** (this pass) **vs the probe's 14 / 23,275,060 / 619.**
- The single delta is **`John0851_1970`** (33,583 B, fetched 2026-10-06, **23 namings**), `(PB)`, **0 `1886`**
  in the earliest company annual report on disk — and its bytes carry 23 namings while
  `research/A4_harvest_mine.md` records the same item as **NULL, 0 entity hits** (a label outranked by the bytes,
  RD-124, **U.011**). Live re-measure confirms **15** `_djvu.txt` layers totalling **23,308,643 B** and **26**
  SEC bodies totalling **4,671,102 B**.
- **Tier therefore unchanged: T2 core — PROVISIONAL** (inherited, not re-tiered; disagreement logged U.008/U.012).

## The three hazards carried, not smoothed over

1. **Origin stays a range inside a retrospective.** `1886-*87 (the date of the formation of the firm)` — the
   asterisk is **OCR**, `1886-'87` occurs **0 times in bytes**; the company's *later* collapse into "1886; in
   1887 they became a corporation" **is the finding** (U.001/U.002). Brothers are **roles only**: 0
   founder-adjacency lines across three tests, 0 "three brothers", no Band-Aid (U.005).
2. **The author's three self-supersessions survive the merge:** a "not found" line-bound incorporation regex
   defeated by a line-broken two-column sentence (U.002); `asepsissecunduma00john` authorship printed on its own
   title page (U.004); `redcrossnotes01` dated ≥1919 by its copyright legs, lengthening the lag past 33 years
   (U.006). Plus U.009/U.010: the `americandruggis07` L45597 "Robert Wood Johnson" is a **New York Red Cross
   incorporator**, a **locator defect, not evidence**.
3. Family states kept distinct end-to-end (**TRIED–ANSWERED / TRIED–UNANSWERED (remedy named) / UNTRIED**);
   (d) self-narrative-richest, (c) the independent one, (b)/(e) UNTRIED for lack of route/tool.

## Gate

`python tools/gates.py --company-dir founders_playbook/01_companies/company_045_jnj --tier core
--out founders_playbook/03_quality_control/jnj_s1_gates_merge.md` → **Findings 2 / Passes 18**, and **both
findings are ADVISORY**: (i) `stage_1.md` **27,043 words over the core 22,000 density target** — the volume is
above the T2 target, under the 60,000 hard cap, so **one volume, overage logged as advisory, nothing trimmed**;
(ii) `quotes` **7 of 8 checked spans unmatched (88%)** — gate precision unestablished, treated as a triage list
(NOT defects); expected for OCR periodicals. `--tier auto` **cannot read a table-row verdict**, so `--tier core`
was passed explicitly and recorded. **`--fail-on substantive` exits 0** (clean); `--fail-on all` exits 1 only on
the two advisories. Passes include: csv width ×9, all `source_id` tokens resolve, keys (16 source tokens all
resolve), anchors citation-resolution + 12↔12 parity, corrections **4/4 propagate to registers and volumes**.

**Corrections issued at merge:** COR-01 (id map, `P1Sxx`→S4463–S4478) · COR-02 (validation/failures bound by
content) · COR-03 (late-arrival preserved) · COR-04 (three quantitative `source_date` cells reading bare
`UNCONFIRMED` aligned to carrier S4464's own established date `UNCONFIRMED (>=1919)`; added the year the U.006
finding supplies, removed no value — the only register value the merge touched, and it strengthens fidelity).

**Tool facts recorded (so no later agent refuses a working script):** `sec_intake auto` versions its run records
rather than overwriting (RD-139) and `grab`'s enumeration was fixed (RD-138); selftests pass (sec_intake 54/0,
gates 18 controls, harvest_mine 9/0, cdx_intake 37/0). Not exercised by this merge (a merge is byte-assembly of
an authored part, not a retrieval pass), but logged so the "intake/grab broken" belief does not resurface.

**Not examined / not done by this merge:** no source bytes were fetched, no probe re-run, no audit, no
certification. `_parts/s1_p1.md` and everything under `sources/` were left exactly as found (the
`submissions.csv` / `submissions_CIK0000200406.csv` duplicate pair is disclosed, not tidied). `company_001_amazon`
was read for **format only**; no Amazon value, date or phrasing was imported.

**Files written this pass:** `stage_1.md`, `sources.csv`, `quantitative.csv`, `timeline.csv`, `conflicts.csv`,
`data_gaps.csv`, `decisions.csv`, `validation.csv`, `failures.csv`, `channels.csv`, `CORRECTIONS.md`,
`_MANIFEST.md`, this log, and `03_quality_control/jnj_s1_gates_merge.md`. Id block **S4463–S4478** claimed for
`company_045_jnj / merge-jnj`.
