# _MANIFEST — company_045_jnj

**Counts regenerated 2026-10-07 by the `merge-jnj` pass** (word = whitespace-delimited tokens, `wc -w`
equivalent; byte = file size; register rows counted through `csv.reader`, not by line). `_parts/s1_p1.md` is
**read-only** and was measured, not edited. Per method §9.6 this register lets a file be checked against the
ceilings before handoff; **regenerate after every merge or repair pass.** This manifest carries **no audit and
no certification** — the merger may not certify (wave plan: audits by different agents, then a certifier who is
neither author, merger, auditor nor repairer).

## Which ceiling governs which file (method §9.2 / §15.2)

- §9.2's **60,000-word hard cap** is the only word count whose breach is a *defect*. `stage_1.md` is
  **27,043 words = 45% of the cap — UNDER it; no split, nothing trimmed.**
- **T2 core is a 22,000-word density TARGET, not a file limit.** The part was emitted at **32,410 words**; the
  merged narrative volume is **27,043 words**, **OVER the T2 target** (by 5,043) and **under the
  60,000 hard cap**. It is kept as **ONE volume**; the overage is logged as **advisory**, and no evidence was
  deleted to meet the tier figure. `gates.py` was run with **`--tier core`** because **`--tier auto` cannot read
  a table-row verdict** (it reads the dossier's stated tier); the explicit value was passed and that fact is
  recorded rather than editing prose to satisfy the tool.
- The nine registers and the two restored-primary shelves are checked against §9.1 only; none is near a cap.

## Deliverables (read these)

| File | Words | Bytes | Contents | Status |
|---|---|---|---|---|
| `stage_1.md` | **27,043** | 173,168 | MERGE RECORD + Header, Stage boundary, §A–§U, **23 inline claim records**, five-family report, Untried, FETCH REQUESTs, refusals; **12 anchors U.001–U.012** | MERGED (single volume) |
| `CORRECTIONS.md` | 541 | 3,859 | COR-01 (id map) · COR-02 (validation/failures bound by content) · COR-03 (late-arrival preserved) · COR-04 (quantitative source_date aligned to carrier date) | LIVING — append, never rewrite |

## Registers (nine CSVs at this directory root — 102 data rows applied)

| register | cols | data rows | rows requested | key / integrity | words | bytes |
|---|---|---|---|---|---|---|
| `sources.csv` | 18 | **16** | 16 | keys S4463–S4478, 0 dup | 1689 | 15,708 |
| `quantitative.csv` | 12 | **21** | 21 | 0 dup row texts | 633 | 6,522 |
| `timeline.csv` | 11 | **18** | 18 | 0 dup row texts | 777 | 6,225 |
| `conflicts.csv` | 15 | **12** | 12 | keys U.001–U.012, 0 dup | 1517 | 10,682 |
| `data_gaps.csv` | 8 | **11** | 11 | 0 dup row texts | 711 | 5,268 |
| `decisions.csv` | 15 | **8** | 8 | 0 dup row texts | 595 | 4,494 |
| `validation.csv` | 11 | **7** | 7 | 0 dup row texts | 480 | 3,738 |
| `failures.csv` | 11 | **5** | 5 | 0 dup row texts | 407 | 2,917 |
| `channels.csv` | 11 | **4** | 4 | 0 dup row texts | 304 | 2,339 |
| **TOTAL** | — | **102** | **102** | **0 unapplied, 0 folded, 0 added** | — | — |

**Header conformity:** every header byte-identical to `company_001_amazon/<name>`. **Stage vocabulary:** the
literal `stage1` on every row. **Width/duplicate-key check run across all nine blocks in one operation:** 0 rows
off-header-width, 0 empty cells, 0 duplicate keys in the two keyed registers (`source_id` S4463–S4478,
`conflict_id` U.001–U.012). **Line endings:** all nine LF-only, UTF-8, no BOM, trailing newline present.

**Row-count reconciliation (defect found at merge, not papered over).** The part's `## registers-part-2` prints
"16+21+18+8+7+5+4+12+11 = **101**". That per-register breakdown is authoritative and matches the
`merge_census.py` request side exactly, but **the nine numbers sum to 102, not 101** — the `= 101` is
an arithmetic slip in the author's own tally. The merge applied all **102** emitted rows; it did
**not** delete a real row to reach the headline figure (cutting evidence to fit a number is forbidden, §9.6).
**0 rows unapplied; every requested row applied.**

## Late-arrival accounting — preserved (§14 rule 11; U.011; COR-03)

The corpus grew after the probe. This is the dossier's measurement, carried from the part so no later pass
inherits the probe's lower figures as live.

| Measure | Probe (2026-09-29) | This pass (2026-10-07) | Delta |
|---|---|---|---|
| OCR periodical layers on disk | 14 | **15** | +1 — `John0851_1970` (33,583 B, fetched 2026-10-06) |
| Held layer bytes | 23,275,060 | **23,308,643** | +33,583 (live-measured 23,308,643 B across 15 `_djvu.txt`) |
| Entity-naming lines | 619 | **642** | +23 — all in the late 1970 annual-report layer |

- **`John0851_1970` is `(PB)`** and load-bearing negative for Stage 1: **0 occurrences of `1886`** in the earliest
  company annual report on disk. Its bytes carry **23 namings** while `research/A4_harvest_mine.md` records the
  same item as **NULL, 0 entity hits** — a label outranked by the bytes (RD-124, **U.011**). Harvest NULL counts
  cannot bound coverage for this slug.
- **26 SEC filing bodies** now on disk (4,671,102 B; 26 `.txt`), accessions 1994-03-10→1999, **all `(PB)`**;
  the probe's `SEC document bytes held: 0` is stale (**U.008**). `1886` occurs **0 times** across them.
- **EDGAR re-measured by the author:** 3,371 rows, earliest 1994-03-10, latest 2026-09-10, 65 forms,
  **0 forms beginning `S-1`, 0 rows ≤ 1960-12-31**, 134 rows with no `primaryDocument`.
- **Tier unchanged: T2 core — PROVISIONAL** (two families return in-window Tier-1 text; the new arrivals are all
  post-window). The disagreement is logged (U.008/U.012), never enacted silently.

## FIVE FAMILIES, AS MEASURED ON THIS PASS

| Family | In-window state | Verdict class |
|---|---|---|
| **(a) Filings** | 3,371 rows enumerated and **re-measured this pass** (earliest 1994-03-10, latest 2026-09-10, 65 forms, **0 forms beginning `S-1`, 0 rows ≤ 1960-12-31**); 26 filing bodies now on disk (4,671,102 B) but **every one `(PB)`**; `1886` occurs **0 times** in them | **TRIED–ANSWERED — documented in-window NULL** (route answered, so the zero is a statement about the record). Unanswered sub-slice: 134 rows with no `primaryDocument`, plus `_UNANSWERED.csv`/`_SKIPPED.csv` slots = UNANSWERED, not null |
| **(b) Web archives** | `tools/web_domains.json` contains **no `jnj` slug** (verified by grep this pass), so `tools/cdx_intake.py` has never been run for this company and writes an UNTRIED record for it. The probe's *ad-hoc* urllib CDX floor (www.jnj.com 1996-10-18; johnsonandjohnson.com 1998-01-26) is recorded as a **floor measurement, two URLs, not the archive** | **UNTRIED as a scripted family** (per the dispatch's rule, because no jnj domain is cited in `web_domains.json`); and in-window **impossible by construction** for the registrant's own domains — 36 years past the window's close |
| **(c) Periodical corpora** | 5 American Druggist volumes held and read (1896, 1902 ×2, 1904 ×2), **47 naming lines** with printed volume legs; **790 of 795 items unopened; 44 of 44 *Pharmaceutical Era* items unopened**; Chronicling America `CHALLENGED` on all 7 endpoint shapes | **TRIED–ANSWERED (in-window Tier-1 text returned)** + **UNTRIED** at 99% of the corpus + **UNANSWERED** for CA (never a null) |
| **(d) Digitised corporate print** | 6 company-authored layers read to the line: house organ ×2, 1897 manual, contested-date pamphlet, first-aid manual, belladonna contribution volume; **504 of the corpus's 642 namings**; plus the `(PB)` 1970 annual report | **TRIED–ANSWERED — the richest family, and it is self-narrative** (U.012) |
| **(e) Auction / museum documentary** | no tool: `tools/HARVEST_README.md` family 4 is *"(not implemented) … no read-only public API was verified"*; **no command exists to run**; one museum artefact exists repo-wide, at Walmart, never for jnj | **UNTRIED — has no tool** (a statement about us, not about the record). Highest-value unopened door for an 1886 company |

## Intermediate merge volumes (`_parts/`) — retained, read-only to every later pass

| File | Words | Bytes | Contents | Why retained |
|---|---|---|---|---|
| `s1_p1.md` | 32,410 | 221,512 | author `s1-jnj-p1`: §Header–§U + the nine `csv` register blocks (verbatim source of the 102 applied rows) | emission of record; the merge read it and applied from it, editing nothing |
| `NOTES_jnj_p1.md` | 1,410 | 9,614 | author log incl. four FETCH REQUESTs (FR-1…FR-4) and the probe-supersession notes | handoff record |

`_parts/` is **read-only** to the merge: no footer was appended and nothing above any marker was edited. The
supersession of the register emission's *placement and key-space* (the 102 rows now live in the CSVs;
`P1Sxx` superseded there by **S4463–S4478**) is recorded in `stage_1.md`'s MERGE RECORD and `CORRECTIONS.md`, not
by editing the part.

## Specialist dossiers (`research/`) and primary evidence (`sources/`) — protected, untouched

- `research/` dossiers: A4_harvest_mine.md, A_chronology_feasibility.md.
- `sources/periodicals/` holds **15** OCR `_djvu.txt` layers (23,308,643 B) plus `.meta.json` sidecars;
  `sources/sec/` holds **26** filing bodies (4,671,102 B); `sources/_index/` holds the
  `submissions.csv` / `submissions_CIK0000200406.csv` **duplicate pair — disclosed, left in place, not tidied**
  (§14 rule 4). `sources/corporate_print/` and `sources/harvest_mine/` are retrieval scratch.
- **Nothing under `sources/` was created, moved, pruned or edited by this merge.**

## Aggregate

| Measure | Value (2026-10-07, `wc`-measured) |
|---|---|
| Deliverable text this pass (stage_1.md + CORRECTIONS.md + 9 registers) | **34,697 words / 234,920 B** |
| — stage volume alone | 27,043 words (45% of §9.2 cap; **T2 target OVER**) |
| `sources/` total (all files, all shelves) | 95 files / 30,176,973 B |
| Files over §9.2's 60,000-word hard cap | **0** |
| Files over the T2 22,000 density target | `stage_1.md` (27,043) — **advisory**, single volume kept, nothing trimmed |
| Register rows applied | **102** (sources 16 · quantitative 21 · timeline 18 · decisions 8 · validation 7 · failures 5 · channels 4 · conflicts 12 · data_gaps 11) |

**Housekeeping.** The `stage` column is the literal `stage1` throughout. The global source ids **S4463–S4478**
are claimed in `00_universe/_ID_BLOCKS.tsv` for `company_045_jnj / merge-jnj` and allocated **above the highest
live id** (a concurrent merge had already taken the block below, so the mint landed at S4463). **This manifest is
a count register, not a certification.**
