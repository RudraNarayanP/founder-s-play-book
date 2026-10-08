# CORRECTIONS — PepsiCo, Stage 1

Ledger for the merge operation of 2026-10-07 (`merge-pepsico`). Six entries, all of them **placement, key-space
or attribution** corrections applied by the merge; **no claim, figure, date or quotation in the author's
narrative was withdrawn, rewritten or trimmed.** Each id is printed in the register layer and in
`stage_1.md`, which is the propagation `gates.py --checks corrections` measures. Nothing in `tools/`,
`00_universe/` or `sources/` was edited by this pass.

| id | what was corrected | what replaced it | where it lands |
|---|---|---|---|
| **COR-01** | The register rows carried **provisional dossier-local source keys** (`P1S01–P1S16`), which are not global. The author's own §Header states they "are minted centrally at merge"; the merge did exactly that. | Minted **S4479–S4494** (`python tools/id_mint.py --count 16 --company company_046_pepsico --claim --agent merge-pepsico`), allocated above the highest live id; every cell citing a local key re-pointed; each local tag kept as an alias inside the `notes` cell of the row that replaces it. No value altered. | `sources.csv` (all 16 rows, `notes`), `timeline.csv`, `decisions.csv`, `validation.csv`, `failures.csv`, `channels.csv` (`source_id` cells), `quantitative.csv` (`source` cells); id map in `stage_1.md` |
| **COR-02** | The **dispatch label** in `00_universe/_AUTHOR_WAVE_PLAN.md` reads `s1-pepsico-p1 … T2 22k`. That is ambition, not measurement, and the same plan's standing correction says the probe's measured tier governs. | **T3 register** — probe `research/A_chronology_feasibility.md` §A.7 for 1A/1B/1C and for the stage, 1B/1C PROVISIONAL; re-measured by the author against §15.2 (one family returns in-window Tier-1 text held: `CAT48`, S4486). `gates.py` run with **`--tier register` passed explicitly** because `--tier auto` cannot read a table-row verdict (wave-plan correction 3). No re-tiering, no trimming, no split. | `conflicts.csv` U.15 (`residual_uncertainty`); the tier section of `stage_1.md`; `03_quality_control/pepsico_s1_merge.md` |
| **COR-03** | The probe's A.3 verdict that **"the merger story itself: UNKNOWN — no carrier in this corpus"** — true when written, refuted by bytes that arrived later. | **Superseded on that one point only, and preserved as the author's own supersession.** `01-pepsi-co` l.122 (PepsiCo 2017 shareholder letter, signed Indra K. Nooyi) prints "Two years later, in 1965, Frito-Lay and Pepsi-Cola merged to form PepsiCo." → one carrier, one lineage, 52 years late → **Low / RESTATED**, registered at **U.10**. Everything else the probe measured (the folklore zeros, the two-origin-lines structure, the ex-21 subsidiary finding, the single-lineage verdict, the five-family states, T3) **stands unchanged**. The companion refusal also stands: five filings do **not** corroborate 1965 — they are one lineage, and their second clause dates **1973** by arithmetic, which is a DERIVED row and not corroboration (U.11). | `conflicts.csv` U.10 (`residual_uncertainty`), `quantitative.csv` (`merger_statements_in_whole_corpus`), `timeline.csv` (2017 row); §U.10 and the carry-forward section of `stage_1.md` |
| **COR-04** | The author's layer-enumeration scratch **`_tmp_pepsico_layers.json` sat at the repository root**, outside the company directory, and three places in the dossier pointed at that root path. | Moved, **byte-for-byte unchanged** (9,794 B), to `company_046_pepsico/_parts/_tmp_pepsico_layers.json`; the three path references in the volume annotated in place; cited from `sources.csv` S4492 and `data_gaps.csv` S-10. The repo root now carries no company scratch. Nothing was re-run and no count changed: 102 layers, 17,860,942 B, 27 pre-1965 / 21 in 1965–1986, 7 `(Frito-Lay)`, 1984 absent. | `sources.csv` S4492 (`notes`), `data_gaps.csv` S-10 (`follow_up_task`); §T.1 row, claim record P1-33, the volume's closing paragraph |
| **COR-05** | The nine fenced register blocks were **inside a prose file**, which §9.1(2) forbids ("supporting data lives in CSV, never inside prose files") and which invites a second application of rows that are already on disk. | Each block replaced at its own heading by a printed pointer naming the register, the applied row count, the column count and the `_parts/` line range of the verbatim emission, with **DO NOT RE-APPLY**. `_parts/s1_p1.md` remains the emission of record; the CSVs are canonical. 6,245 words of register data left the prose; 0 rows left the corpus. | the nine pointers in §registers of `stage_1.md`; `sources.csv` S4479 (`notes`); `_parts/s1_p1.md` superseded footer |
| **COR-06** | The census could not attribute the two schema-identical blocks: `AMBIGUOUS:validation.csv,failures.csv`, with **content hints scoring all 12 rows as `either`** — i.e. the hints decided nothing. | Adjudicated **by content** against the two registers' semantics (validation = what a carrier established; failures = what the retrieval or the toolchain failed to do), cross-checked against the author's own emit headings and stated counts (validation 4, failures 8), and 4 + 8 = 12 = the census's whole unattributed total; no row text in both groups. **How** it was decided is recorded, not silently applied. | `validation.csv` row 1 (`notes`), `failures.csv` row 1 (`notes`); the adjudication section of `stage_1.md` |

## Not corrected, and why

- **The five pipeline defects in §M.2** (the `drop_year_facet` YEAR-facet artefact that reports corporate print
  as empty; the two layers filed under the wrong person or year; the unledgered `ERIC_ED337649` arrival; the
  `--max-docs 30` cap that left 88 in-window filings unlisted; the probe's unparseable `list-files` CLI form)
  are **recorded, not repaired**: they live in `tools/` and in intake, outside a merge's WRITE scope. Each
  already has a `failures.csv` row and, where a route exists, a FETCH REQUEST.
- **The five FETCH REQUESTS** are not executed here. A merge applies emissions; retrieval belongs to the
  orchestrator (§15.1). They stay open exactly as measured, and none is reported as a null.
- **`stage` vocabulary, evidence classes, confidence values and every `UNKNOWN`** were taken as issued. No
  `UNKNOWN` was smoothed into a date and no folklore origin date was adopted to make a section populate.
- **Nothing in `MASTER_RESEARCH_LOG.md` or `RESUME_HANDOFF.md`** was opened or edited by this pass; if either
  carries a stale PepsiCo line (the 1898 window, a "no carrier" merger verdict, or a T2 label), that is an
  outbound correction handed to the log's owner, per §14 rule 4.

STATUS: WRITTEN 2026-10-07
