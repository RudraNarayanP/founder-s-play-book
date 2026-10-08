# Alphabet — `CORRECTIONS.md`

Retractions opened by the Stage-1 merge pass (2026-09-30, agent `alphabet-s1-merge`). Each id is
**printed into the register rows that carried the withdrawn text and into `stage_1.md`**, which is the
propagation the `corrections` gate measures (§14 rule 10). Nothing here deletes a row: a superseded value
stays visible inside the cell that replaces it, because the record of the error is evidence.

| id | what was withdrawn | where it lands |
|---|---|---|
| **COR-01** | the probe's Stage-1 **closing geometry (Q1-1999)** and the dispatch's **1996-2004 span**: `research/A_chronology_feasibility.md` proposed a Q1-1999 close and the brief's window is a *harvest* window, not a stage window. Part 1 refuted both and adopted **1998-01-09 → 2001 (year-granular, closing day UNKNOWN)** with five rival geometries named and rejected at its `## Boundary` | `timeline.csv` rows **P1TML01** (the adopted opening, 1998-01-09) and **P2TML08** (the adopted close, 2001-12-31 leg); §Boundary and §Header of `stage_1.md` |
| **COR-02** | the records dossier's **lineage map**: `research/B1_filing_records.md` states one registration statement under "file no. 333-117934 / 000-50726, re-filed as S-1/A eight times". Read from the SGML header block and cover page of each held `.txt`, that premise does **not** reproduce: there are **two** Securities Act numbers (333-114984 with Amendments 1-5, 333-117934 with Amendment 1), a separate Exchange Act number (000-50726) on the 8-K, and one accession (-04-138034) held as an index page only, so its number is **UNTESTED — a coverage hole, not an absence** | `conflicts.csv` **P1CNF01**; `sources.csv` rows **S4335** (S-1 as filed), **S4336** (header/cover pages), **S4343** (Amendment No. 5), **S4346** (the cover-only stub); `data_gaps.csv` **P1GAP06** |
| **COR-03** | part 1's **A.1 / record B18** claim that operating detail for 1998-2000 has **no carrier** and that "no cost figure exists before 2003". The 2004-04-29 printing carries a full statement of operations for FY1999 and FY2000 — costs by line, operating loss, net loss, per-share and share counts. The claim is **refuted for costs and the bottom line**; it **survives** for headcount, users, queries, index size and year-by-year cash | `conflicts.csv` **U.017**; `quantitative.csv` rows **P2QTN04, P2QTN05, P2QTN08-P2QTN11, P2QTN13, P2QTN14, P2QTN15** |
| **COR-04** | part 1's **Boundary refusal (iii)** as written: "no pre-IPO funding quantum exists". §J.1 reads **private sales of preferred stock totalling 37.6 million USD since inception** in a region of the lineage part 1 did not quote. The refusal of a **named and dated round** stands; the claim that **no money quantum** exists is retracted | `conflicts.csv` **U.024**; `quantitative.csv` **P2QTN17**; `data_gaps.csv` **P1GAP05** (which now also carries part 2's `U.032` wording) |
| **COR-05** | the undated **rescission ceiling**. Part 1 printed "up to $34 million"; the August printing prints "up to **25.9 million** USD including statutory interest". U.021 required the merge to date each ceiling to its printing, which is now done inside the row: **34 million is the April printing, 25.9 million the August printing**, one contingent liability re-estimated twice | `conflicts.csv` **U.021**; `failures.csv` row **P2FAI03** (which absorbed part 1's `P1FAI02`); `quantitative.csv` **P2QTN21** |
| **COR-06** | nothing was withdrawn — a **tool** defect is recorded so no later pass reads it as missing data: `merge_census.py` reported the two shared `validation.csv`/`failures.csv` blocks as `AMBIGUOUS` (11 identical column names, RD-132) and could attribute neither. The 23 rows were attributed **by the parts' own leading `notes` tags** (`P1VAL01-06`, `P1FAI01-03`, `P2VAL01-07`, `P2FAI01-07`): **13 validation + 10 failures, 0 dropped**. One trap on the way: part 2's `P2FAI02` row cites `P2FAI07` inside its own caveat cell, so a first-match reader mis-keys it — the leading tag is the address | every row of `validation.csv` (12) and `failures.csv` (9) carries `[COR-06]`; `stage_1.md` merge note |
| **COR-07** | nothing was withdrawn — the **dossier-local source keys are retired as keys**: `P1SRC01-P1SRC11` and `P2SRC01-P2SRC11` (22 emissions, 21 records) are replaced by the globally minted **S4332-S4352**, allocated through `tools/id_mint.py --claim` (registry `00_universe/_ID_BLOCKS.tsv`), never by inspection. Every local key stays printed in the `notes` cell of the row that replaces it, and inside every `MERGE[...]` marker, so prose citing `P1SRC04` or `B01`-`B43` still resolves | all 21 `sources.csv` rows; the id map in `stage_1_index.md` and the `stage_1.md` merge note |
| **COR-08** | two **carried citation defects** corrected against the held bytes: `research/A2_periodical_settlement.md` cites the Yahoo Internet Life passage at lines **11027-11033**, which stops mid-sentence (the passage is at held lines 11026-11036); and the probe reported the CIA beta-agreement layer as **16,305 B** where the disk prints **16,235 B** | `sources.csv` rows **S4338** (YIL July 2000) and **S4339** (CIA evaluation agreement) |

## Instruction-layer sweep (§14 rule 10)

`RESUME_HANDOFF.md` and `MASTER_RESEARCH_LOG.md` were grepped for the values retracted above —
`333-117934`, the Q1-1999 close, and the `1996-2004` window. **Zero Alphabet hits in either file** (the
Q1-1999 lines in this log belong to Amazon's Stage-3 boundary finding, not to Alphabet). No stale value
lives in the instruction layer for this company, so there is **no outbound correction to hand off**.
Neither file was edited by this pass.

## Not corrections

* One §13 vocabulary repair, printed rather than silent: `channels.csv` row **P1CHN05** carried
  `never dated and never measured` in the year-bearing `date_tested` column; the cell now reads
  `UNKNOWN (never dated and never measured)`. The wording is unchanged, the controlled literal is added.
* Post-boundary `(PB)` rows (2002-Q1, 2002-04, 2003-06, 2004-07-06, 2004-08-06, 2004-08-09) stay
  `stage1` because both parts labelled them so and every one is used only as a consequence; stated here
  rather than applied silently, exactly as the Target merge did (RD-122).
* `merge_census.py` cannot see `research/` at all (RD-131 defect 1). This pass checked the four dossiers
  for a fourth emission: `B1_filing_records.md` (9,179 w), `A_chronology_feasibility.md`,
  `A2_periodical_settlement.md` and `A4_harvest_mine.md` contain **zero fenced-`csv` register blocks**;
  B01-B43 and U-1-U-16 are claim records and hyphen-form conflict keys, cited by the parts and aliased in
  the register `notes` cells, not rows to apply. Requested side = 180, all in the two parts.

STATUS: WRITTEN 2026-09-30 (alphabet-s1-merge)
