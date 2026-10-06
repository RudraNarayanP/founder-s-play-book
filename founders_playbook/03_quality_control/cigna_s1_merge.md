# Cigna Stage 1 — MERGE RECORD (live, written incrementally)

Agent `merge-cigna`. Operation: merge `_parts/s1_p1.md` (the only part) into
`founders_playbook/01_companies/company_014_cigna/stage_1.md` + the nine registers + `_MANIFEST.md` +
`stage_1_index.md` + `CORRECTIONS.md`. Status legend per register below: **PENDING** = not yet on disk,
**APPLIED n rows** = verified on disk at the stated width. If this file is read mid-operation, the
`requested` column is the emission of record and the CSVs are the ground truth — re-measure, do not trust
this tally.

**Rows requested by the part: 78** (`_parts/s1_p1.md` l.490 and `_parts/NOTES_cigna_p1.md`:
sources 16 · quantitative 15 · timeline 14 · decisions 3 · validation 4 · failures 6 · channels 2 ·
conflicts 6 · data_gaps 12).

## Register application account (this is the account the last merge died without)

| register | requested | applied | status |
|---|---|---|---|
| `sources.csv` | 16 | **16** | APPLIED 16 rows (18 cols; keys S4407–S4422, 0 duplicate keys) |
| `conflicts.csv` | 6 | **6** | APPLIED 6 rows (15 cols; keys U.1–U.6, 0 duplicate keys) |
| `quantitative.csv` | 15 | **15** | APPLIED 15 rows (12 cols) |
| `timeline.csv` | 14 | **14** | APPLIED 14 rows (11 cols) |
| `decisions.csv` | 3 | **3** | APPLIED 3 rows (15 cols) |
| `validation.csv` | 4 | **4** | APPLIED 4 rows (11 cols; adjudicated block, see §validation/failures below) |
| `failures.csv` | 6 | **6** | APPLIED 6 rows (11 cols; adjudicated block, see §validation/failures below) |
| `channels.csv` | 2 | **2** | APPLIED 2 rows (11 cols) |
| `data_gaps.csv` | 12 | **12** | APPLIED 12 rows (8 cols) |
| **TOTAL** | **78** | **78** | — |

Unapplied rows: **none — 78 requested, 78 applied.** No row was dropped, merged away, deduplicated or withheld
by the merge. Nothing was added beyond the emission either.

## Census BEFORE any write (measured 2026-10-06, `tools/merge_census.py --company-dir … --verbose`)

9 structured blocks parsed; **78 rows requested**; `present` = 0 for every register (no CSVs yet);
**22 keyed rows "missing"**: conflicts 6 (`s1_p1.md:U.1…U.6`) + sources 16 (`s1_p1.md:CG01…CG16`).
**2 block-groups unattributed** — the 4-row and 6-row groups, `AMBIGUOUS:validation.csv,failures.csv`.

## The validation/failures adjudication (the census cannot decide; I did, by reading)

`validation.csv` and `failures.csv` share a byte-identical 11-column header, so the census prints both
4-row and 6-row groups as `AMBIGUOUS:validation.csv,failures.csv` with content hints only. Adjudication:

1. **Declared target by block heading.** `_parts/s1_p1.md` l.576 `### \`validation.csv\` — 4 rows` immediately
   precedes the 4-row block; l.589 `### \`failures.csv\` — 6 rows` immediately precedes the 6-row block. The
   `>>> REGISTER ROWS FOR MERGE <<<` markers name their target by the heading above them, exactly as the other
   seven blocks do.
2. **Declared counts match.** `_parts/NOTES_cigna_p1.md` (l.26) states "validation 4 · failures 6"; the blocks
   parse to 4 and 6 rows. No count tension exists, so nothing turns on the content reading.
3. **Content check, row by row, against the two registers' semantics** (Amazon's conformant usage: `validation`
   = a signal that validated something; `failures` = a negative/adverse signal):
   - 4-row block: health pre-tax income +48%; repetition of the buy-a-plan pattern; three SCOTUS records naming
     the structure; the 2018 indenture still designating both carriers. Each cell in
     `what_it_demonstrated` is a positive validation claim → **validation.csv**.
   - 6-row block: 101.8 combined ratio (underwriting loss); $84.8M 1978 P&C losses; reserves outgrowing earned
     premiums; the 5%-of-income parent-and-other LOSS line; goodwill write-downs; three appearances as a
     litigation respondent. Each is an adverse signal → **failures.csv**.
   - Cross-check: no row appears in both groups; 4 + 6 = 10 = the 10 rows the census listed as unattributed.

## Third-emission check (the census is blind to `research/*.csv`)

`find` over the company dir to depth 2 for `*.csv` before any merge write: **zero CSVs** under `research/` and
zero at the company root other than the 9 scaffolded stubs created by `scaffold.py claim` in this pass.
`research/` holds only `A_chronology_feasibility.md` and `A4_harvest_mine.md`. **No third emission exists**;
78 is the whole request.

## Id allocation (minted centrally, never into a gap, never reused)

`python tools/id_mint.py --audit` before minting: 327 distinct issued ids, range `S0001–S4406`; highest live
block = `company_013_costco` `S4393..S4406`; tool's own `next assignable: S4407`. Known live collision set
reported by the audit: **`S4222–S4229` cited by both `company_011_microsoft` and `company_042_target`** (task
#31) — which is why Target's next mint is deliberately held. I did **not** mint into `S4230+`: allocating
above the highest live id means the gap cannot swallow another company's held number.

Minted here: `python tools/id_mint.py --count 16 --company company_014_cigna --claim --agent merge-cigna` →
**S4407 … S4422** (16 ids, contiguous, no gap). Binding to the dossier-local tags is the mapping table in
`stage_1.md` (the map is also the only place `CG01–CG16` survive into the global space).

## Census AFTER the final write (same command, re-run on the finished bytes)

| reading | before | after |
|---|---|---|
| structured blocks parsed | 9 | 9 |
| rows requested | 78 | **78** |
| `conflicts.csv` present / missing | 0 / 6 | **6 / 0** ← anchor parity proven |
| `sources.csv` present / missing | 0 / 16 | 0 / **16** (the 16 are the superseded `s1_p1.md:CG01…CG16` tags; the minted ids S4407–S4422 are the live keys — COR-01) |
| TOTAL missing keyed rows | 22 | **16** |
| unattributed block-groups | 2 (validation/failures) | 2 — unchanged: a schema property of the two registers, now adjudicated on the record (COR-02), not a missing row |
| unkeyed rows (no key column to match) | channels 2 · data_gaps 12 · decisions 3 · quantitative 15 · timeline 14 | same — all of them are on disk and were counted by row, not by key |

**Requested 78 ↔ applied 78.** The census's "22 missing then / 16 missing now" is therefore fully accounted:
6 conflicts rows landed (0 remaining), 16 sources rows landed under minted keys, and the remaining 16 "missing"
entries are the local tags the census reads out of the read-only part file. Nothing is unaccounted for.

**Third emission:** still none. After every write, `research/` contains 0 CSVs, and the nine live registers are
the only CSVs at the company root, so no hidden second source of rows exists.

## Register integrity, measured across the whole operation at once

`sources.csv` 16×18 · `quantitative.csv` 15×12 · `timeline.csv` 14×11 · `data_gaps.csv` 12×8 ·
`conflicts.csv` 6×15 · `failures.csv` 6×11 · `validation.csv` 4×11 · `decisions.csv` 3×15 · `channels.csv`
2×11 = **78 data rows**. Per-file checks, run over all nine files together: **0** rows off-header-width,
**0** empty cells, **0** exact duplicate rows across blocks, **0** duplicate keys in `sources.csv`
(S4407–S4422) and `conflicts.csv` (U.1–U.6), `stage` = `stage1` on **78/78** rows, `CG`-tag residue **0** in
the live registers. Headers compared by string equality against `company_001_amazon/<name>` — all nine
**byte-identical**.

## Cells the merge annotated (the only writes to author row text)

Row *values* were never altered. Five `notes` / `residual_uncertainty` cells had a COR pointer appended at the
end of the existing cell so each correction reaches the register layer (method §14.10; the gate measures it):
`sources.csv` S4407 · `quantitative.csv` census row · `conflicts.csv` U.2 · `validation.csv` first row ·
`failures.csv` first row. Width re-verified at the header's width after each append. Every substitution of
`CG01–CG16` → `S4407–S4422` was a token-level re-key inside cells the author said the merge would re-key
(`_parts/s1_p1.md` l.490, merge instruction (4)).

## Anchors ↔ conflicts parity (proof by census, not assertion)

Declared by the part: `<!-- ANCHORS: U.1-U.6 -->` (l.410) and the six sections §U.1–§U.6. On disk:
`conflicts.csv` keys = `['U.1','U.2','U.3','U.4','U.5','U.6']`, 0 duplicates. Final gate:
`anchors | parity | 6 narrative anchors <-> 6 register anchors` and
`anchors | citation resolution | every register-cited anchor resolves (6 distinct ids …)` — no orphan in
either direction, no seventh row, no unanchored section. The volume's §U letters and numbers are the author's,
unchanged.

## Volume

`stage_1.md` = merge record (assembly, application, COR-01 id map, folds, anchor parity, two tier frames,
carry-forward, COR propagation) + the author's body **verbatim, section letters intact, no renumbering** + the
register-application record at the foot. **14,513 words / 94,432 bytes** (`wc`, re-measured after the last
write). The nine fenced blocks were not reprinted in the volume: `_parts/` remains the emission of record, and
a second copy would read to the census as new rows. `_parts/s1_p1.md` was not edited; a `SUPERSEDED 2026-10-06`
footer was appended to it, and the footer's own wording limits its reach to **placement and key-space** — the
78 rows now live in the CSVs and `CG01–CG16` are superseded there. The body above the footer was byte-checked
after the append: 9 blocks, 78 rows, 0 width defects, LF endings preserved.

**Two tier frames kept, not averaged:** T2 core PROVISIONAL (lineage frame, 2 families in-window) and T3
register (strict-registrant frame, 0 families name CIK 0001739940 before 2018) both carried as states, attributed
to the probe §7, with the machine's T3 tie-break reading registered at U.4. The final gate's tier reader printed
`tier: T2 … (35 mentions, 0 on a verdict line)` and applied the **core / 22,000-word** cap: 14,513 = 66% of it.
No overage, no split, nothing trimmed.

## Five families, as the probe issued them and as this merge carried them (TRIED / UNANSWERED / UNTRIED kept distinct)

| family | state | register/volume home |
|---|---|---|
| (a) SEC / EDGAR | **TRIED–ANSWERED as a perimeter**; **UNTRIED** for the predecessor registrant; **TRIED–UNANSWERED** on the 18 filings never listed at `--max-docs 30` | `sources.csv` S4407–S4409/S4417; `timeline.csv` Line-3 rows; `data_gaps.csv` rows 1, 2, 9; FR-1/FR-2/FR-3 |
| (b) Web archives | **UNTRIED — 0 calls** (no `sources/web_archive/` at all, not a refusal) | `data_gaps.csv` row 7; UNTRIED item 2; FR-6 |
| (c) Periodical corpora | **TRIED–ANSWERED** for the IA main thread (3 in-window SCOTUS records); **TRIED–UNANSWERED** for Chronicling America (7/7 shapes 403 — a dead route, no CA zero citable) and HathiTrust; **TRIED–ANSWERED leads-only** for Google Books; **81 of 96** candidate rows **UNTRIED** at `--limit` | `sources.csv` S4411–S4413, S4420; `validation.csv` row 3; `failures.csv` row 6; `data_gaps.csv` rows 5, 9; UNTRIED items 4, 5; FR-4/FR-5 |
| (d) Digitised corporate print | **TRIED–ANSWERED by document class** (the INA 1979 annual report, Tier-1, off-shelf on `periodicals/`); **TRIED–UNANSWERED** as the harvester's own facet-ed `corporate_print` task | `sources.csv` S4410; `conflicts.csv` U.6; `quantitative.csv` 14 of its 15 rows; `data_gaps.csv` rows 6, 10; UNTRIED item 6; FR-4 |
| (e) Auction / museum / manuscript | **UNTRIED — 0 calls** (no directory, no task, no residue) | `data_gaps.csv` row 8; UNTRIED item 3 |

Strict-registrant frame: all five families return **0** for CIK 0001739940 before 2018 — that is the T3 row,
carried, never averaged into the T2 verdict.

## Gate (final, run after every write)

`python tools/gates.py --company-dir founders_playbook/01_companies/company_014_cigna --tier auto --out
founders_playbook/03_quality_control/cigna_s1_gates_merge.md` → **Findings 1 | Passes 19**.

- `corrections` **whole**: "3 retraction ids; register layer reaches 3, volumes 3" → `corrections |
  propagation | all 3 retraction(s) reach registers and volumes` in the passing list.
- `anchors` **whole**: parity 6↔6, citation resolution passes, `csv` passes for all nine registers,
  `keys` passes (16 source tokens resolve; 5 retired ids read as protected history in the collision note).
- `budget` passes: 14,513 words against target 22,000 / hard cap 60,000.
- The single finding is `quotes | verbatim | 1 of 5 quoted spans not found in local sources`, and the evidence
  line names it: `stage_1.md :: 96 candidate rows in the harvest index 12 items mined 81 left untried at the
  limit`. **This is the gate's scope, not a defect in the data.** The string is a quotation of
  `research/A4_harvest_mine.md` **l.5**, an internal measurement record that is one of this dossier's sources
  (S4421) — `grep -c "96 candidate rows in the harvest index" research/A4_harvest_mine.md` = **1**, verbatim.
  `gate_quotes` builds its corpus from `sources/**` only (`*.txt`, `*.htm*`), so a quotation from `research/`
  can never match locally. The same span was flagged in the pre-merge run (`cigna_s1_gates_probe.md`,
  Findings 1), i.e. it is inherited from the author's body and was introduced by neither the merge nor the
  annotations. Per the dispatch rule the data is left alone and the evidence is recorded here; the quote is
  neither deleted nor "repaired" into a form the detector likes.

## Uncarried follow-ups, named (not dropped)

1. `research/_EVIDENCE_CACHE.md` — `data_gaps.csv` row 11 asks for it "at merge", but no cache was among this
   pass's claimed deliverables (`stage_1.md`, `_MANIFEST.md`, `stage_1_index.md`, `CORRECTIONS.md`, the nine
   registers). The row stays **OPEN**; `CORRECTIONS.md` §"Not corrected" records why.
2. **FR-8** has no `data_gaps.csv` row because the author emitted none; its homes are UNTRIED item 8 and the
   `conflicts.csv` U.2 residual cell. Adding a 13th row was refused: the merge applies emissions, it does not
   author them.
3. FR-1…FR-7 remain open exactly as the probe and the author measured them; 18 never-listed filings (FR-3) and
   81 unmined candidate rows (FR-4) are reported as measured, not as nulls.

## Claims released

`stage_1.md`, `_MANIFEST.md`, `stage_1_index.md`, `CORRECTIONS.md` and the nine register CSVs — 13 paths, all
released `--done` at the close of this pass, none forced.

**Merger's limit on this report:** I assembled, applied, verified and published. I did not audit or certify
this volume; the numbers above are measurements of my own writes, and an audit must re-measure them
independently.

STATUS: COMPLETE — 78 requested / 78 applied
