# Meta Stage 1 — MERGE RECORD (live, written incrementally)

Agent `merge-meta`. Operation: merge `_parts/s1_p1.md` (25,200 words, §Header–§J, 33 claim records `P1-01…P1-33`,
99 register rows, anchors `U.1–U.7`) and `_parts/s1_p2.md` (9,721 words, §K–§U, 17 claim records, 43 register
rows, anchors `U.1–U.8`) into **one volume** `stage_1.md` + the nine live registers + `_MANIFEST.md` +
`stage_1_index.md` + `CORRECTIONS.md`.

Status legend per register: **PENDING** = not yet on disk, **APPLIED n rows** = verified on disk at the header's
width. This file is the account; the CSVs are the ground truth. If it is read mid-operation, re-measure — do not
trust the tallies below.

I assembled, applied, verified and published. **I did not audit and I do not certify this volume** (merge wave,
`00_universe/_AUTHOR_WAVE_PLAN.md`: "Merge agents may not certify").

## Register application account (written before the writes, updated after each one)

Rows **requested**: 142 = p1 99 (sources 11 · quantitative 30 · timeline 22 · decisions 3 · validation 6 ·
failures 5 · channels 4 · conflicts 7 · data_gaps 11) + p2 43 (sources 9 · timeline 4 · quantitative 6 ·
conflicts 8 · data_gaps 8 · decisions 3 · validation 2 · failures 3 · channels 0).

| register | requested (p1+p2) | applied | status |
|---|---|---|---|
| `sources.csv` | 11 + 9 = 20 | **15** | **APPLIED 15 rows** (18 cols; keys **S4495–S4509**, 0 duplicate keys; 5 p2 rows aliased into their p1 carriers, 4 p2 rows kept as their own carriers) |
| `quantitative.csv` | 30 + 6 = 36 | **36** | **APPLIED 36 rows** (12 cols; no (date, metric) collision between the volumes; p1's 845 row re-verified and its source re-keyed to S4496) |
| `timeline.csv` | 22 + 4 = 26 | **23** | **APPLIED 23 rows** (11 cols; 3 p2 rows aliased on (date, event), p2's month-level 2004-07 row kept as its own row beside p1's 2004-07-29 day-level row) |
| `decisions.csv` | 3 + 3 = 6 | **5** | **APPLIED 5 rows** (15 cols; p2's incorporation decision aliased into p1's, p2's other 2 rows kept) |
| `validation.csv` | 6 + 2 = 8 | **8** | **APPLIED 8 rows** (11 cols; 7 from the emissions — p2's 2004-09-02 row aliased into p1's — **plus 1 row authored by this merge on dispatch instruction**, the provenance-drift row; adjudicated block, see §validation/failures above) |
| `failures.csv` | 5 + 3 = 8 | **8** | **APPLIED 8 rows** (11 cols; 0 folds; adjudicated block, see §validation/failures above) |
| `channels.csv` | 4 + 0 = 4 | **4** | **APPLIED 4 rows** (11 cols; p2's 0-row block is an earned null and was left a null — no junk row invented) |
| `conflicts.csv` | 7 + 8 = 15 | **8** | **APPLIED 8 rows** (15 cols; keys **U.1–U.8**, one row per subject, 0 duplicate keys) |
| `data_gaps.csv` | 11 + 8 = 19 | **13** | **APPLIED 13 rows** (8 cols; 6 p2 rows aliased into p1 gap subjects, 2 kept as their own rows) |
| **TOTAL** | **142** | **120** | **119 rows applied from the 142 emitted + 1 merge-authored row** |

**Every unapplied row is named** — 23 of the 142 emitted rows were **aliased, not dropped**, and each alias is
written inside the surviving row with its source part:
`sources.csv` P2SRC-1→S4496, P2SRC-2→S4495, P2SRC-3→S4503, P2SRC-4→S4502, P2SRC-7→S4501 (5);
`conflicts.csv` p2's U.1, U.2, U.3, U.4, U.5, U.6, U.7 → p1's canonical rows of the same ids (7);
`timeline.csv` p2's 2003-04, 2004-09-02, 2005-05-06 → p1's rows of the same event (3);
`decisions.csv` p2's 2004-07 incorporation row → p1's (1); `validation.csv` p2's 2004-09-02 row → p1's (1);
`data_gaps.csv` p2's day-level-record row → p1 row 2, its 2004-2008-data row → p1 row 4, its founding-narrative
row → p1 row 1, its press row → p1 row 8, its REGDEX-attribution row → p1 row 6, its complaint-text row → p1
row 3 (6). **No author row was deleted, and no author cell was overwritten: every fold is an append of p2's own
text into p1's row, prefixed `[p2 …]` or `[MERGE: aliased from …]`.**

**Cells the merge authored or filled, all declared:** (1) one `validation.csv` row for the S-1 provenance drift,
authored on the dispatch's explicit instruction (it is not an author emission and is counted separately: 120
applied = 119 + 1); (2) **10 empty cells conformed** — `sources.csv` rows 13–14 (`P2SRC-8`, `P2SRC-9`, the CDX
and harvest negative artifacts) had empty `event_date`/`publication_date`, filled with
`UNKNOWN (no capture: the service refused)` / `n/a (negative artifact, never published)`, and all 6 p2
`quantitative.csv` rows had empty `derived_arithmetic`, filled with p1's controlled literal `not_derived`.
Every fill carries the marker `[MERGE FILL: p2 left this cell empty; no value invented]`. **No value was
invented and no UNKNOWN was replaced.**

## Census BEFORE any write (measured 2026-10-07, `tools/merge_census.py --company-dir … --verbose`)

**17 structured blocks parsed; 142 rows requested; `present` = 0 for every register** (the company root held no
CSVs at all — only `_parts/`, `research/`, `sources/`). Requested per register: conflicts 15 · sources 20 ·
data_gaps 19 · timeline 26 · quantitative 36 · decisions 6 · channels 4; **TOTAL missing keyed rows: 35**
(conflicts 15 as `s1_p1.md:U.1…U.7` + `s1_p2.md:U.1…U.8`; sources 20 as `P1S01…P1S11` + `P2SRC-1…P2SRC-9`).
**4 block-groups unattributed** — the 6-row and 5-row groups from `s1_p1.md` and the 2-row and 3-row groups from
`s1_p2.md`, all printed `AMBIGUOUS:validation.csv,failures.csv`.

## The validation/failures adjudication (the census cannot decide; I did, by reading)

`validation.csv` and `failures.csv` share a byte-identical 11-column header, so the census cannot bind those
four blocks. Adjudication, three independent tests, all agreeing:

1. **Declared target by heading.** `s1_p1.md` l.1020 `### validation.csv — …` precedes the 6-row block and
   l.1035 `### failures.csv — …` precedes the 5-row block; `s1_p2.md` l.572 `Target register:
   \`validation.csv\` — rows emitted: 2` precedes the 2-row block and l.580 `Target register: \`failures.csv\` —
   rows emitted: 3` precedes the 3-row block. Each is bound to the marker immediately beneath it, exactly as the
   other seven blocks are.
2. **Declared counts match both author logs.** `NOTES_meta_p1.md` §1 says "validation 6 · failures 5";
   `NOTES_meta_p2.md` says "validation.csv — 2 rows … failures.csv — 3 rows". The blocks parse to 6, 5, 2, 3.
   6+2 = 8 validation and 5+3 = 8 failures = the 16 rows the census left unattributed. No count tension.
3. **Content, row by row**, against the two registers' semantics (`validation` = a signal that validated
   something; `failures` = an adverse signal): p1's 6-row block = certificate filed, third parties sue the
   founder, family working capital, Series A + outside director, Zynga addendum, 15-year landlord lease — each
   `what_it_demonstrated` cell asserts something positive → **validation**; p1's 5-row block = the option
   LAPSED, a copyright suit against the registrant, FY2007 operating loss, FY2008 loss, three years of EDGAR
   silence → **failures**. p2's 2-row block = the 2004-09-02 suit as an existence signal and the explicit
   "NONE RECOVERABLE" earned null → **validation**; p2's 3-row block = contested ownership, the repudiated
   April-2003 agreement, a disclosure failure → **failures**.

## Id allocation (minted centrally, above the highest live id, never into a gap)

`python tools/id_mint.py --audit` before minting: **383 distinct issued ids, range S0001–S4462**, 163 registry
claims. Highest live block `company_035_att` S4449..S4462. The audit's collision list confirms the task's
warning: **`S4222–S4229` are cited by both `company_011_microsoft` (S4222..S4243) and `company_042_target`
(S4201..S4229)**, and `company_043_tesla` is recorded against the impossible range S0001..S4392, which is what
makes S0001–S0010 read as amazon/tesla collisions. Minting into `S4463+` would have re-entered the registry gap
the audit lists (S4463…S4494, "registry ids not present in any sources.csv"), so I did not choose that number.

Minted here: `python tools/id_mint.py --count 15 --company company_017_meta --claim --agent merge-meta` →
**S4495 … S4509** (15 ids, contiguous, no gap, above every live id). The map from the dossier-local tags
(`P1S01…P1S11`, `P2SRC-1…P2SRC-9`) to the minted block is published in `stage_1.md` and `CORRECTIONS.md`
(COR-01); it is the only place the local tags survive into the global space.

## Conflict de-duplication (outbound correction 1, taken from `NOTES_meta_p1.md` §12)

Both volumes emit `conflicts.csv` rows keyed `U.1–U.7`: p1 seven rows, p2 eight rows (`U.1–U.8`), p2 having
adopted p1's taxonomy verbatim and added `U.8`. Applied as written that is **15 rows against 8 subjects and
seven duplicate `conflict_id` primary keys**, which the `csv` key gate fails. Resolution applied here, per
§14 rule 7's recovery rule (never delete the other pass's work; declare one canonical; alias the rest):

* **One row per subject, one id, 8 rows: `U.1`–`U.8`.** `U.8` (the truncated-index tooling artifact, probe
  META-C3) is part 2's alone and applies unaltered.
* **For `U.1`–`U.7` part 1's rows are canonical**, because p2 never opened Ex-3.3: `TheFacebook` and
  `July 29, 2004` have **0 occurrences** anywhere in p2's reads, so p2's `U.1` rests on the proposition that
  the day is "unobtainable from EDGAR permanently" — a proposition p1's byte-level finds refute. p1's rows
  also carry the Ex-10.16A "Saverin Agreement" narrowing (U.4), the `thirty days` / `30 days` census (U.6) and
  the window carriers (U.7).
* **Both statements are kept inside the single row**, attributed: each merged row keeps p1's cell text and
  appends `[MERGE: from p2's U.n row — …]` for every sentence p2 contributed that is genuinely additive
  (p2's §U.4 "settled-then-dropped dispute need not be named" rationale, its §U.7 "the load-bearing findings
  hold under either reading", its §U.3 "gap marker not a founding event", its §U.6 5–6 % duplicate-account
  argument, its §U.2 "the company asserts the emails are fraudulent"). Where p2's cell asserts something p1's
  bytes refute, it is recorded as the superseded claim with the refuting measurement named — not deleted.
* **No anchor was renumbered** (`_AUTHOR_WAVE_PLAN.md` correction 2). `U.1–U.7` mean the same subject in both
  volumes; `U.8` exists only in p2 and stays `U.8`.

## `company` literal normalisation (outbound correction 2, from `NOTES_meta_p1.md` §12)

p1 writes `Facebook Inc.` on all 99 rows; p2 writes `Meta` on all 43. `merge_census.py` keys on
`conflict_id`/`source_id`, but the primary-key gate and any later cross-company join treat `Meta` and
`Facebook Inc.` as different subjects. Convention adopted — **carrier-faithful per row, i.e. the registrant as
printed in the document the row cites** — and stated in `_MANIFEST.md`:

* **`Facebook, Inc.`** (with the comma the S-1's own cover prints) on every row whose cited carrier is the 2012
  registration lineage, a filed exhibit of it, a federal docket caption of 2004–2008, or any event dated
  2003–2012. This is the Stage-1 subject and it is what those instruments print.
* **`Meta Platforms, Inc.`** only on the rows whose cited document *is* the EDGAR registrant record or speaks
  of the 2021 renaming — the two rows where that literal is the one the carrier prints
  (`sources.csv` S4501 ← `P1S07`; `data_gaps.csv` row 12). Its `former_names` field is what connects the two,
  and it is **undated in this corpus**.
* **`Meta` bare is used on no row.** p2's literal is superseded row by row; the prose of both parts is
  untouched (`_parts/` is the emission of record and is read-only to the merge except for a supersession
  footer).
* No 2004 or 2005 instrument is dated by a modern literal: the 2005-05-06 `REGDEX` rows stay attributed
  **UNKNOWN** under `Facebook, Inc.` (U.3), because writing `Meta Platforms, Inc.` there would assert the
  attribution U.3 exists to forbid.

## Measurements taken by this merge (re-measured from `sources/` bytes before any row was written)

| proposition | measured on the current bytes | consequence |
|---|---|---|
| provenance drift, S-1 body | disk **2,657,075 B / sha1 `d749855af0…`**; sidecar + `_MANIFEST.csv` record **2,627,682 B / sha1 `bf14d10705…` / fetched 2026-09-29T19:05:37Z** | CONFIRMED, reported not repaired (COR-04) |
| `845 million` in the S-1 | raw bytes print `845&nbsp;million` **11 times**; a plain grep for `845 million` returns **0**; stripped text 11 hits, context "We had 845 million MAUs as of December 31, 2011, an increase of 39% as compared to 608 million MAUs as of December 31, 2010" | p1's `845` row **VERIFIED**; p2's NOTES correction 1 ("not found in the held S-1 text") is a grep artifact of the same class as p1's `July&nbsp;29, 2004` note |
| `901 million` / `680 million` | 424B4: `901 million` 5 hits, `900 million` 11, `845 million` 0 — "We had 901 million MAUs as of March 31, 2012, an increase of 33% as compared to 680 million MAUs as of March 31, 2011" | p1's 2012-03-31 rows VERIFIED |
| `TheFacebook` | exactly **1 of 31** stored SEC documents (`0001193125-12-175673_d287954dex33.htm`); 0 in the S-1 body and 0 in the 424B4 | p1's U.1 provenance survives |
| `Saverin` | exactly **1** occurrence in the whole SEC corpus, in `d287954dex1016a.htm` (Ex-10.16A), as the defined title "the Saverin Agreement" | p1's COR-2 stands; p2's 0-hit census is correct only for the S-1 and 424B4, which is what it cited |
| `thirty days` / `30 days` | `thirty days` = **1** (`d287954dex102.htm`, the 2005 Stock Plan option window); `30 days` = **71 in raw bytes / 73 after tag-and-entity stripping**, across 19 documents | p1's 1/71 census reproduced; p2's U.6 claim "the corpus contains **no** 'thirty days' string at all" is REFUTED by 1 hit in a filed exhibit — and the adjudication it supports (no growth carrier, no substitute number) is unaffected |
| `February 2004` | **0** in the S-1 | launch month stays UNKNOWN |
| Ex-3.3 recital | `July&nbsp;29, 2004` in `d287954dex33.htm`, `Dated:` line blank | day-level date is a recital in an unexecuted form: **Medium**, Delaware stays the upgrade route (U.1) |
| S-1 accession image inventory | held `_index/S1_accession_filelist.txt` lists **28 items**, of which **23 are JPGs = 22 `g287954g*.jpg` figures + `g287954zuckerberg_sig.jpg`**; exactly one exhibit (`d287954dex231.htm`); **0 JPGs are actually stored** under `sources/sec/` | the probe's and p1's "26 figures" is **not reproducible from held bytes** and p2's "23 JPGs + a signature image" over-counts by one: reported, not repaired (COR-05) |

## STATUS: registers applied — 120 rows live (119 from the 142 emitted + 1 authored); 23 aliased, all named above

## Volume

`stage_1.md` = **merge head** (tier, window, the seven carried findings, the `company` literal convention, the
anchor-parity before/after) + **part 1's body verbatim** (§Header, §boundary, §A–§J, the register pointer section,
`## Untried` 11 routes, F-1…F-5) + **part 2's body verbatim** (§K–§U with §U.1–§U.8, claim records K01…T01) +
**register-application foot** (id map, five-family table, open follow-ups, COR-01…COR-09 propagation table).
**30,212 words / 197,633 bytes**, re-measured after the last write; 34,921 words is the combined emission and
11,051 words of it were the 18 fenced register blocks, which are **not reprinted** (pointer lines instead, each
naming its row count) so `merge_census.py` cannot read the same rows twice. `_parts/` was **not edited**: no
footer, no correction, no renumbering — both parts remain byte-identical to what their authors wrote.

**One volume.** 30,212 words is **137% of the T2 core density target (22,000)**, 76% of the §9.2 soft target
(40,000) and **50% of the 60,000 hard cap**: over the tier target, under the cap, **overage logged as advisory and
nothing trimmed** (§9.2/§9.3; a tier overage is not a split mandate). `CORRECTIONS.md` 2,142 words,
`stage_1_index.md` 990 words, `_MANIFEST.md` carries the counts and the two rulings the dispatch required (the
`company` literal convention and the provenance drift).

**Seven merge annotations** (`[MERGE 2026-10-07 …]` or `[MERGE: …]`) were inserted in part 2's body inside the volume — §K.2, §K.5, §Q.1,
§U.1 (twice: CLAIM B and BEST-SUPPORTED INTERPRETATION), §U.4, §U.6 — each placed **after** the sentence it
supersedes, **deleting no paragraph** (§14 rule 7, exactly as `NOTES_meta_p1.md` §10 directed: "superseded with a
`[MERGE]` annotation; do not delete part 2's paragraphs"). Part 1's body needed no annotation: it is the part whose
bytes were right.

## Census AFTER the final write (same command, re-run on the finished bytes)

| reading | before | after |
|---|---|---|
| structured blocks parsed | 17 | 17 |
| rows requested | 142 | 142 |
| `conflicts.csv` present / missing | 0 / 15 | **15 / 0** — every emitted `U.n` key resolves, which is the de-duplication proved by the tool: 15 emitted keys land on **8 live rows**, no duplicate primary key |
| `sources.csv` present / missing | 0 / 20 | 0 / **20** — the 20 "missing" keys are the superseded local tags `P1S01…P1S11`, `P2SRC-1…9`; the minted ids `S4495–S4509` are the live keys (COR-01) |
| TOTAL missing keyed rows | 35 | **20** — all 20 are local tags read out of the read-only part files; **0 rows are unaccounted for** |
| unattributed block-groups | 4 (`AMBIGUOUS:validation.csv,failures.csv`) | 4 — unchanged: a schema property of the two registers, now adjudicated on the record (COR-02), not a missing row |
| unkeyed rows | channels 4 · data_gaps 19 · decisions 6 · quantitative 36 · timeline 26 | same — all counted by row and all on disk |
| third emission in `research/*.csv` | none (2 dossiers only, 0 CSVs) | none — `find` re-run after the last write |
| live rows at the company root | 0 | **120** |

## Register integrity, measured across the whole operation at once

`sources.csv` 15×18 (keys S4495–S4509) · `quantitative.csv` 36×12 · `timeline.csv` 23×11 · `conflicts.csv` 8×15
(keys U.1–U.8) · `data_gaps.csv` 13×8 · `validation.csv` 8×11 · `failures.csv` 8×11 · `decisions.csv` 5×15 ·
`channels.csv` 4×11 = **120 data rows**. Over all nine files: **0** rows off header width, **0** empty cells,
**0** duplicate keys in `sources.csv` and `conflicts.csv`, `stage` = `stage1` on **120/120** rows, and **every
`S####` token in every register cell resolves** to a live `sources.csv` key (the gate checks this per file).
Headers compared by string equality against `company_001_amazon/<name>`: all nine **byte-identical**. Local-tag
residue in the live registers is **5 intentional mentions** in `sources.csv` `notes` cells — each one the alias
account naming the retired `P2SRC-n` tag it folded into — and nothing else. `company` column distribution on the
written bytes: `Facebook, Inc.` **104**, `Meta Platforms, Inc.` **1**, bare `Meta` **0** (`sources.csv` carries no
`company` column; its 15 rows are the remaining 15 of the 120).

## Gate (final, run after every write)

`python tools/gates.py --company-dir founders_playbook/01_companies/company_017_meta --tier core --out
founders_playbook/03_quality_control/meta_s1_gates_merge.md` → **Findings 2 | Passes 18**, and **both findings are
advisory, neither is a defect**:

* `advisory | stage_1.md | 30212 words over the core (this volume's issued tier) density target 22000 — NOT a split
  mandate and NOT a defect`. Logged, not trimmed. The tier passed to the gate is **`core` explicitly**, per
  wave-plan correction 3, because `--tier auto` on the same bytes stamps **T1** (see "Tier" below) and so does not
  grade the volume at all.
* `quotes | ADVISORY | 10 of 35 checked spans unmatched (29%) — gate precision is not established, treat as a triage
  list, NOT as defects`. The evidence lines are quotations of the **probe dossier** and of the **shared author
  contract** (`no edgar document can ever fix the founding day`; `deliberately wide where the founding date is
  itself unestablished`; `a row you cannot attribute to a register is worse than a paragraph`), plus filed exhibit
  text whose words sit across table cells (`facebook inc 2005 stock plan as amended april 2006 …`). `gate_quotes`
  indexes `sources/**` only, so a quotation from `research/` or from a brief can never match locally. **The data
  was left alone and the evidence recorded here** — nothing was deleted or rephrased to please the detector, and no
  quotation was invented: the flagged filed-text span is a genuine exhibit heading and the dossier spans quote
  held bytes verbatim.
* Passing that matter most: `csv` for all nine registers; `*.source_id` all resolve; `keys` "15 source tokens all
  resolve" (with 5 retired ids — S0001, S4222, S4229, S4449, S4462 — read as collision/range history in my own id
  narrative and correctly **not re-pointed**); **`anchors` parity 8 narrative ↔ 8 register** and citation resolution
  across 8 distinct ids; **`corrections` propagation "all 9 retraction(s) reach registers and volumes"**;
  coverage "9 registers, 1 stage volumes, 43 source documents".

## The two divergences, preserved rather than smoothed

1. **Tier.** Dispatch label **T1**; `gates.py --tier auto` stamp **T1** (`tier: T1 (a stated-verdict line) from
   A_chronology_feasibility.md — T1/T2 all mentioned in research/ (7 mentions, 2 on a verdict line)`); the
   **dossier's measured verdict T2 core, 2 of 5**. The registers and `_MANIFEST.md` are written to **T2**; the label
   error is recorded in COR-06 and in the manifest; the dossier stays the authority, as the wave plan's Dell
   correction requires. Nothing was re-tiered and no prose was edited to satisfy the tool.
2. **Window.** Dispatched dossier window **2003-01-01 → 2012-12-31** vs the probe's **July-2004 Stage-1 close**;
   part 1 wrote to one, part 2 to the other, both bodies published unaltered, and the conflict **U.7** carries it.
   This merge recorded its own staging call inside U.7 (keep the dispatched window for Stage 1; hand the 2005–2012
   re-homing to the cross-company pass) so the seam is **decided on the record rather than settled by silence** —
   and it did **not** re-stage the company, move any row between stages, or delete part 2's out-of-window labels.

## Five families as the merge found and carried them (states kept distinct — see the volume foot and `_MANIFEST.md` for the full table)

(a) filings **TRIED–ANSWERED**, registrant-retrospective for the origin (31 stored documents; 397-row enumeration);
legal **TRIED–ANSWERED at register level, UNTRIED for pleadings** (7 matters, 2004-09-02 → 2008-11-19);
(b) web **TRIED–UNANSWERED**, not a null, and unrunnable as written because `tools/web_domains.json` has **no meta
slug** — F-1 stands and a provenance-sourced domain must be requested, never invented; (c) periodicals
**TRIED–UNANSWERED** (CA 403 ×3, HathiTrust status 0 ×2) / **metadata-only** for Google Books / **UNQUERIED** for
internet_archive; (d) corporate print **UNQUERIED** (breaker-killed; "exists only in private hands" is not
licensed); (e) auction/museum **UNTRIED**, 0 calls, structurally. **2 of 5 → T2.**

## What the merge did NOT do

No audit, **no certification** (a merge may supply neither). No `sources/` write of any kind: no sidecar rewritten
(COR-04), no accession re-listed (COR-05), nothing pruned, moved or tidied. **0 web calls**, so no Tier-4 material
entered the dossier. `_parts/` unedited. No value invented: **no substitute date, month, day, growth figure, first
customer, first salary, ad price or 2004–2006 metric** was written anywhere; the channels register was left
unpadded; every UNKNOWN in either part's emission stayed UNKNOWN. No Amazon value imported — `company_001_amazon/`
was read for the nine header lines and section shape only, and those headers were matched byte-for-byte.
**Not examined by this pass:** the S-1 financial statements beyond the origin strings, the `CORRESP` letters, the
six `UPLOAD`/`.paper` items, the 23 accession JPGs (none stored, no OCR run), the FY2012 10-K, the counterparties'
own filed copies, the Delaware and California registries, RECAP/PACER pleadings, and families (b)–(e) re-runs.

## Claims released

Fifteen paths were claimed at the start of this pass with `python tools/scaffold.py claim --path <p> --agent
merge-meta` — `stage_1.md`, `stage_1_index.md`, `_MANIFEST.md`, `CORRECTIONS.md`, the nine register CSVs,
`03_quality_control/meta_s1_merge.md` and `03_quality_control/meta_s1_gates_merge.md` — and each returned
`CREATED … (owner=merge-meta ttl=240 min)`. **`--force` was never used.** At the close, `release --done` returned
**`no claim for <path>` on all 15**: the shared `founders_playbook/_OWNER_LEDGER.json` no longer carries any
`merge-meta` entry — it holds only `s1-meta-p1` on `_parts/s1_p1.md` (still LIVE, not mine to release),
`s1-meta-p2` (done) and `probe-meta` (done) for this company. Concurrent agents write that same ledger in this
wave (the working tree shows `tools/scaffold.py` itself modified plus three other companies' `_parts/` files
changing between my calls), so a claim taken here can be overwritten by another agent's save. **Reported as
measured, not smoothed:** no lock is held by `merge-meta` now, which is what the release was for, but I cannot
claim I released what I could no longer find. `_parts/` was confirmed untouched — its mtimes
(`s1_p1.md` 03:22, `NOTES_meta_p1.md` 03:25, `s1_p2.md` 03:18) all predate this pass's first write at 03:30, and
`git diff` on the directory is empty.

Five temporary build files were written under `tools/_tmp_meta_*` (three scripts and the two record fragments the
volume's head and foot were assembled from) and deleted after the final measurement; the merge wrote no other file
outside the fifteen claimed paths. Two stray gate outputs briefly landed at the repository-root
`03_quality_control/` because the dispatch's `--out` path is relative to the launch directory; they were re-run
into the claimed `founders_playbook/03_quality_control/` path and the strays deleted.

**Merger's limit on this report:** I assembled, applied, verified and published. I did not audit and I do not
certify this volume; every number above is a measurement of my own writes and an audit by a different agent must
re-measure it.

STATUS: COMPLETE — **142 requested / 119 applied + 1 authored = 120 live / 23 aliased by name**

