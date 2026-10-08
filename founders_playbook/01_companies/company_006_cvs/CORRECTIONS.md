# CORRECTIONS — company_006_cvs, Stage 1 (merge pass, 2026-10-07)

Written by `merge-cvs`. A correction ledger: it **appends and records propagation, never rewrites or deletes
history, and never touches a claim in the narrative**. These are key / schema / binding entries issued at merge,
not claim retractions. The author's part (`_parts/s1_p1.md`) and its `NOTES_cvs_p1.md` stay read-only.
**I am the merger; I did not audit and I do not certify.** If a later auditor finds a correction wrong, they
append to this file; they do not erase it.

## COR-01 — provisional ids superseded by minted global ids (key propagation)

`PROV-CVS-01 … PROV-CVS-18` are dossier-local keys. In the **live registers** they are superseded by the centrally
minted ids **S4431 … S4448** (`id_mint.py --count 18 --company company_006_cvs --claim --agent merge-cvs`),
allocated above the highest live id (`company_023_gm S4430`) so no gap was re-entered and the **S4222–S4229
Microsoft/Target collision** was not touched.

- **Scope of the remap:** every `source_id`-bearing cell of `sources.csv`, `timeline.csv`, `decisions.csv`,
  `validation.csv`, `failures.csv`, `channels.csv` (and compound cells) carries the minted id.
- **Where `PROV-CVS-nn` still lives:** only in the read-only part, and in the binding map in `stage_1.md` (the
  MERGE RECORD) — that table is the sole place the local and global ids co-exist, exactly as `CG01–CG16` survive
  in Cigna's map. No register row keeps a `PROV-*` token.
- **No source was added, dropped, or redefined:** 18 local → 18 global, 1:1, ordered.

## COR-02 — `decisions.csv` row 1 width defect repaired (schema geometry)

- **The defect:** the part emitted `decisions.csv` row 1 (the standing non-claim, `claim_ref = CVS-A20`,
  "Founding act of the chain") at **16** fields against a **15**-column header. A stray duplicate `"UNKNOWN"` sat
  between `actual_result` and `source_id`, shifting `source_id / confidence / claim_ref` one column right. All
  fields were quoted, so this is a spurious extra field, not the unquoted-comma shift the wave plan warns about —
  same register-corrupting consequence, different cause.
- **The repair:** dropped **exactly one** `"UNKNOWN"` so the row lands at 15 fields: `rationale = "no carrier"`,
  `expected_result = UNKNOWN`, `actual_result = UNKNOWN`, `source_id = S4432` (the term-census carrier, correct
  for a "no byte" row), `confidence = UNKNOWN`, `claim_ref = CVS-A20`. Before → after field count 16 → 15; the
  only character removed is one `"UNKNOWN"` token.
- **What was NOT done:** no value changed, moved, invented, or removed other than the redundant placeholder; no
  other row touched. Re-measured: all 14 decisions rows are 15-wide, 0 off-width.
- **Owner:** the author emitted the width; the merge is the first writer of the live register, so it fixes the
  geometry it is shipping. This is recorded so an auditor can see the emission differed and re-derive it.

## COR-03 — validation.csv / failures.csv block binding recorded (schema ambiguity)

`validation.csv` and `failures.csv` share a byte-identical 11-column header, so `merge_census.py` printed the
8-row and 7-row groups as `AMBIGUOUS:validation.csv,failures.csv`. (The census's printed content hints were a
**tool artifact** — it echoes the `data` variable from the prior loop iteration, i.e. the decisions rows — and
were not used.) Binding applied, per the wave plan's "adjudicate by content":

1. **Declared target:** the part's `>>> REGISTER ROWS FOR MERGE <<<` markers name `validation.csv — rows emitted:
   8` and `failures.csv — rows emitted: 7`; `NOTES_cvs_p1.md` §9 states the same widths.
2. **Counts close:** 8 + 7 = 15 = the two census-unattributed groups; no row in both.
3. **Content:** the 8-row block is every row that *validated* something (naming, warehouse plan, estate counts,
   the acquisition, the filed segment, the Marshalls exit, the Delaware re-cut, the productivity filing); the
   7-row block is every incurred negative (review-because-shape-needed-answering, the $585m/$195m/$230m charges,
   the Q4 earnings hit, the three-legs-in-exit, the Peoples-name erasure, the origin-failure absence-row, and the
   `_FLEET_INTAKE.tsv` disclosure-side failure). Heading and content agree; **no row was moved between registers.**

## COR-04 — `timeline.csv.source_id` foreign-key repair (schema geometry)

- **The defect:** the author emitted `timeline.csv` `source_id` as a **per-row running counter**
  `PROV-CVS-01 … PROV-CVS-24` (one incrementing label per timeline event), not as a foreign key into the
  18-row `sources.csv`. Cells 1–18 coincidentally resolve to `S4431…S4448` (which exist as keys) but cells
  19–24 mapped to `S4449…S4454`, which the merge never minted and `sources.csv` does not contain. `gates.py`
  flags exactly those six (`timeline.csv | source_id token not a key in sources.csv: S4449–S4454`).
- **The repair (minimal, non-inventing):** repointed **only** the six non-resolving cells to the carrier each
  row's **own note** names, using no document outside the 18 minted sources:
  | row | event (date) | old | new | in-row evidence |
  |---|---|---|---|---|
  | 19 | 1996-03-15 TJX preferred transfer | S4449 | **S4445** | SC 13D filed by Melville (CVS-A18); row 18 note names the same 1996-04-08 SC 13D |
  | 20 | 1996-08-22 CVS organised (DE) | S4450 | **S4431** | row note "8-B12B Item 1(a)" |
  | 21 | 1996-08-30 merger agreement | S4451 | **S4431** | row note "Merger Subsidiary named CVS New York, Inc." (8-B12B App A) |
  | 22 | 1996-10-07 proxy mailed | S4452 | **S4431** | row note "Attached to the 8-B12B as Exhibit 2.1" |
  | 23 | 1996-11-04 8-B12B filed | S4453 | **S4431** | the instrument itself |
  | 24 | 1996-11 name change | S4454 | **S4431** | row/claim evidence "8-B12B cover names CVS CORPORATION (Successor…)" |
- **What was NOT done:** cells 1–18 were left in place because they resolve as keys; the merger did **not**
  rewrite them. **Residual for the citation auditor (named, not dropped):** the entire column is a counter, so
  several of 1–18 (e.g. row 3 the 1976 name change → `S4433`, which is the S-4, not the EDGAR header; row 7 the
  1987 DSN-88 owner row → `S4437`, whose true carrier DSN-88 is not among the 18 sources; rows 17–18 → `S4447`
  /`S4448`, index carriers, for events whose documents are the 8-K `S4444`/SC 13D `S4445`) are semantically
  mis-pointed while gate-valid. Re-pointing them is re-derivation that would require sources the author did not
  emit, so it is audit work, not merge work, and the merger performed neither.

## Propagation record (what `gates.py` corrections-check enforces)

Each COR-nn is echoed in the register layer and in `stage_1.md` so a reader of either meets the correction:
**COR-01** → `sources.csv` S4431 notes ("ids superseded from PROV-CVS-01 per COR-01"); **COR-02** →
`decisions.csv` row 1 unknowns cell ("row width repaired per COR-02"); **COR-03** → `validation.csv` +
`failures.csv` row-1 notes ("block bound per COR-03"); **COR-04** → `timeline.csv` row-23 notes ("source_id
repointed per COR-04") and the `registers` section of `stage_1.md`. These are key/schema/binding entries, **not
claim retractions** — no substantive value was withdrawn from any register.

## Not corrected, and why

- **Two accepted gate findings the merger deliberately did NOT reshape away** (method: never reshape real data
  to silence a gate — name it instead):
  1. `quantitative.csv` last row (the origin-window UNKNOWN, `date = 1963-1979`) carries `source_date = "-"`,
     which `gates.py csv` flags as "carries no four-digit year." That is the author's honest marker for a metric
     with no dated carrier (0 carriers in 36 SEC files + 16 unique press/print docs). Inventing a year to satisfy
     the check would be fabrication; the row stays as emitted and is listed here.
  2. `gates.py quotes` reports **1 of 11 quoted spans not found**: the §D.2 warehouse sentence
     "…CVS increased distribution capacity by [~]a 400,000-square-foot DC in New Jersey. That raised…". The
     `[~]` is the author's in-quotation OCR-corruption marker (CVS-A14 / §D note "OCR corruption in the 1990
     sentence"), so the literal bytes differ from the squashed index and the matcher misses it. It is a
     verbatim-check question for the citation auditor to resolve against the held DSN bytes — not a merge edit,
     and the merger did not alter the quotation to force a match.
- **No claim retracted.** The folk origin (1963 shoe store, Consumer Value Stores as the 1963 entity,
  Jacksonville, Riverside–Newport) is **UNKNOWN** in the part (CVS-A20) and stays UNKNOWN; the merge neither
  asserts nor deletes it. "Founded in 1963" remains **COMPANY CLAIM, retrospective, Medium, one lineage**.
- **No re-tiering.** The window stays **T2 core**; **S1a/S1b/S1c stay T3 register**; family **(d) is not counted**
  (its bytes are family (c), md5-proved — **U.08**). The merge restated the probe's verdict, it did not change it.
- **Probe's stale census states kept visible, not deleted.** §U.10 reports the probe's earlier 36/6/29 and
  68/12/55 harvest readings as stale states of a live lane (close = 70/12/57); they remain reported, not erased.
- **Intake-manifest drift not repaired.** The `_FLEET_INTAKE.tsv` / `_RUN.json` disagreement is a **disclosure-side
  failure of the run**, reported in `failures.csv` and `data_gaps.csv` (S.10) — not this agent's file to fix, and
  the bytes themselves are fine (36 stored files, sidecars `http_status 200` + `sha1`).
- **`## registers` label preserved.** The author's in-body cross-references ("full-width rows … are in
  `## registers`") keep their anchor: the merged volume's register section is headed `## registers — Register rows
  applied to the nine CSVs`, so nothing renumbered and no reference dangles.
