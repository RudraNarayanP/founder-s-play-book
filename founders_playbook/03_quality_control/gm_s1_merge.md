# General Motors Stage 1 — MERGE RECORD (live; closed out 2026-10-07)

Agent `merge-gm`. Operation: merge `_parts/s1_p1.md` (the only part; 25,046 words, §A–§U, claim records
GM1-C01…GM1-C33, nine fenced register append blocks = **114 rows**) into
`founders_playbook/01_companies/company_023_gm/stage_1.md` + `stage_1_claim_records.md` + the nine registers at
that directory root + `_MANIFEST.md` + `CORRECTIONS.md`. `_parts/` was **read-only** to this pass: no file under
it was edited, moved, renamed or deleted, and it stays the emission of record.

**I am the merger: nothing in this sheet is an audit and nothing is a certification.** Every statement below is
arithmetic, geometry, application, or a restatement of what the probe and the author already issued. Tool calls
used: fewer than 50 of the 130 ceiling — this pass closed out on completion, not at the cap — and this file was
written incrementally: the census, the id block and the adjudication were on disk before the first CSV was
written.

## 1. Rows requested vs rows applied — 114 of 114

| register | requested | applied | cols | status (measured on the bytes on disk) |
|---|---|---|---|---|
| `quantitative.csv` | 26 | **26** | 12 | APPLIED 26 rows — uniform width, 0 empty cells, 0 duplicate `(date, metric)` |
| `timeline.csv` | 30 | **30** | 11 | APPLIED 30 rows — 0 duplicate `(date_or_range, event)` |
| `sources.csv` | 8 | **8** | 18 | APPLIED 8 rows — keys **S4423–S4430**, 0 duplicate keys, 0 `PROV-*` as keys |
| `conflicts.csv` | 10 | **10** | 15 | APPLIED 10 rows — keys **U.01–U.10**, 0 duplicates |
| `data_gaps.csv` | 13 | **13** | 8 | APPLIED 13 rows — keys **G-01…G-13**, no gap, no repeat |
| `decisions.csv` | 8 | **8** | 15 | APPLIED 8 rows — 0 duplicate `(date, decision)` |
| `validation.csv` | 6 | **6** | 11 | APPLIED 6 rows — adjudicated block, reason in §3 below and COR-02 |
| `failures.csv` | 8 | **8** | 11 | APPLIED 8 rows — adjudicated block, reason in §3 below and COR-02 |
| `channels.csv` | 5 | **5** | 11 | APPLIED 5 rows — 0 duplicate `channel` |
| **TOTAL** | **114** | **114** | — | 0 withheld, 0 added, 0 folded |

**Rows not applied: none — every one of the 114 requested rows is on disk.** Nothing was dropped, merged away,
deduplicated or withheld, and the merge invented no row: `channels.csv` got its 5, no more; `failures.csv` its 8;
no register was topped up from prose to make a number look tidy. All nine header rows were compared against the
corresponding Amazon register column-for-column before writing (identical: 12 / 11 / 18 / 15 / 8 / 15 / 11 / 11 /
11). The one textual tension inside the emission is named in §7 rather than resolved by me.

## 2. Census, before and after

**Before any write** (`python tools/merge_census.py --company-dir founders_playbook/01_companies/company_023_gm
--verbose`): 9 structured blocks parsed; **2 block-groups unattributed**
(`AMBIGUOUS:validation.csv,failures.csv`, content hints "either |" on all 14 rows); `TOTAL missing keyed rows:
18` = conflicts 10 (`s1_p1.md:U.01…U.10`) + sources 8 (`s1_p1.md:PROV-FH28…`); every other register censused by
count and shown as `unkeyed` (channels 5, data_gaps 13, decisions 8, quantitative 26, timeline 30). `present` = 0
everywhere because no register CSV existed at the company root (`ls` = `_parts/`, `research/`, `sources/`).

**After the merge** (same command, exit 0): `conflicts.csv requested 10 / present 10 / missing 0` — parity is now
machine-checkable. `sources.csv` reports `requested 8 / missing 8` keyed on `PROV-FH28 … PROV-A4MINE`. **That is
the mandated central re-mint, not a lost row**: those provisional keys were never supposed to survive into the
live register, and the 8 rows exist under their minted keys **S4423–S4430** (verified: `source_id` column reads
exactly that list, in block order). The other seven registers carry no key column, so the census keeps reporting
them `unkeyed`; they were checked by count on the written files instead — the 114/114 table above. The
`AMBIGUOUS` pair persists after the merge, as it must: it is a property of two identical 11-column schemas, now
adjudicated on the record (§3) rather than left to a future pass.

**Third-emission check** (the census is blind to `research/*.csv`): `find` over the company dir for `*.csv` before
any write returned only intake inventories under `sources/` (`sources/_index/submissions*.csv`,
`sources/sec/_MANIFEST.csv` / `_PLAN.csv` / `_SKIPPED.csv` / `_UNANSWERED.csv`) — not register emissions. Zero CSVs
under `research/`, zero register CSVs at the root. **114 is the whole request**; there is no Tesla-style 25-row
third emission here.

## 3. The validation / failures adjudication, and the reason it was decided that way

The census cannot attribute these two blocks — the headers are byte-identical — and its own output says content
words are "hints, not proof". Adjudicated by reading, three independent checks, and **no row moved between the
registers**:
1. **The author's markers.** `_parts/s1_p1.md` l.747 names `validation.csv` — rows emitted: 6 (block l.751–756);
   l.759 names `failures.csv` — rows emitted: 8 (block l.763–770). `_parts/NOTES_gm_p1.md` §8 states the same
   widths (6×11, 8×11).
2. **Arithmetic closes.** 6 + 8 = 14 = exactly the rows the census called unattributed; the two groups share no
   row (`validation ∩ failures = 0` measured on the written rows).
3. **Content against each register's meaning** (Amazon's conformant usage: validation = a signal that validated
   something; failures = an incurred negative). Validation: the 1908-10-01 exchange cleared; the 1910-11 notes
   fully sold in advance of offering; the 1915-10-15 first cash dividend on the common; the 1915-10-01
   voting-trust expiry; the 1916-05 United Motors distribution at $62; the 1918-20 internal self-financing.
   Failures: portfolio abandonment but the Oakland; $600,000 lost unwinding Elmore; the Ford option and
   Maxwell-Briscoe lapses; 21% → 7.8% of US physical output; $12,531,013.19 of write-offs; the bankers' plant
   closures on partisan testimony; the 1921-22 Sheridan/Scripps-Booth liquidations; the lost Dodge bid. A
   keyword split would have mis-served both directions here — several validation rows speak of "harsh terms",
   and the plant-closure failure row is quoted testimony — so the block heading plus row-by-row reading, with
   the counts agreeing, is what bound them. Recorded as **COR-02** in `CORRECTIONS.md` and propagated into the
   first row of each of the two registers.

## 4. Cross-block duplicate-key checking

Run on the written rows, not on the blocks: **zero** identical normalised rows within or across all nine blocks;
**zero** duplicates on `source_id` (8), `conflict_id` (10), `gap` G-01…G-13 (13, contiguous, none repeated),
`(date, metric)` (26), `(date_or_range, event)` (30), `(date, decision)` (8), `channel` (5), and
`(date, signal_or_failure)` in validation (6) and failures (8) separately and against each other. Read as well as
hashed: `timeline.csv` 1916-10-13 and `sources.csv` S4424 cite the same Delaware act because `FH28` and `AR37`
are **one corporate-record lineage** (gap G-12) — a document cited twice, not a duplicate row, and the dossier
says so in terms.

## 5. Id block allocated

`python tools/id_mint.py --audit` before minting: 343 distinct issued ids, range **S0001–S4422**, 91 registry
claims, **`next assignable: S4423`**; highest live block `company_014_cigna S4407..S4422`. The audit prints 17
collisions, including the one my brief named: **`S4222–S4229` cited by both `company_011_microsoft` and
`company_042_target`** — left alone (not allocated into, not repaired; that is the id owner's and the log
owner's job).

Minted: `python tools/id_mint.py --count 8 --company company_023_gm --claim --agent merge-gm` →
**S4423, S4424, S4425, S4426, S4427, S4428, S4429, S4430** — contiguous, **above the highest live id S4422**, so
no gap was re-entered and the Microsoft/Target collision range was not touched. Written to
`founders_playbook/00_universe/_ID_BLOCKS.tsv` as eight rows of `company_023_gm / merge-gm` (verified by reading
the file back). Binding: `PROV-FH28`→S4423, `PROV-AR37`→S4424, `PROV-NPSH29`→S4425, `PROV-DW20`→S4426,
`PROV-TRUCK31`→S4427, `PROV-CF95`→S4428, `PROV-SEC1467858`→S4429, `PROV-A4MINE`→S4430. The re-mint is complete
and mechanical — compound cells included (`PROV-FH28 L9467` → `S4423 L9467`) — and the part's narrative carried
no `Snnnn` token, so the mint could not collide with prose. Post-write check: 0 `PROV-*` values remain in any
`source_id` column (the only remaining literal `PROV-` strings are the two inside my own COR-01 annotation, which
names what it superseded, and the eight in the merge note's map).

## 6. Anchors ↔ conflicts parity — 10 ↔ 10, and gate-confirmed

10 anchors declared in one line (`<!-- ANCHORS: U.01-U.10 -->`) ↔ 10 `### U.nn` sections written in §U ↔ 10
`conflicts.csv` rows keyed U.01–U.10. Same ids both ways, no gap, no declared anchor without a section or a row,
no register anchor without a declared section. `gates.py --checks anchors` now passes it twice:
`anchors citation resolution — every register-cited anchor resolves (10 distinct ids across registers and
volumes)` and `anchors parity — 10 narrative anchors <-> 10 register anchors`. Nine of the ten are cited from
registers beyond `conflicts.csv`; **U.03 is cited only from its own section and one narrative line at §B.1** —
named here rather than padded with an invented citation. No anchor was renumbered, and no `U.nn` was minted by
the merge.

## 7. Words, volumes and what was moved

| file | words | what it holds |
|---|---|---|
| `stage_1.md` | **20,192** | title; MERGE RECORD; Stage boundary; §A–§U with the 10 anchors; registers pointer |
| `stage_1_claim_records.md` | **2,921** | GM1-C01…GM1-C33 (33 records; 2,801 words as emitted), relocated verbatim |
| `CORRECTIONS.md` | **2,195** | COR-01…COR-09 (see §9) |
| nine registers | **4,410** | 114 rows |

25,046 (part) → 20,192 + 2,921 = **23,113 words of volume**, i.e. the T2 22,000-word **target** is met for the
narrative volume with the claim records outside it, and §9.6's rule was obeyed the other way round: nothing was
trimmed. Two geometry moves, no content move: (i) the 4,490 words of raw CSV text left the prose and became the
registers; (ii) the claim-record appendix moved to its companion deliverable **at the §U / claim-record section
boundary** — the cut the author recommended in `_parts/NOTES_gm_p1.md` §8, allowed by method §9.1(3)/§9.3, and
excluded from volume caps by `gates.py stage_docs()` by name. Record ids, order, passages, tiers, confidences and
`Conflicts:` cells are unchanged; `stage_1.md` ends §U and points at it.

**No renumbering anywhere.** Section letters A–U, claim ids, metric ids, gap ids and `U.nn` anchors are the
author's; the merge note in `stage_1.md` says so on its first lines.

**Non-destruction census, part vs merged (measured line by line).** Of the part's 622 non-empty lines, every one
is present verbatim in `stage_1.md` or `stage_1_claim_records.md` **except 152**, and those 152 are exactly the
range l.612–l.782 — the register section: 114 CSV data rows (now the registers themselves, their content
byte-recoverable from the applied rows) plus 38 structural lines (the `## REGISTERS` heading, the emission note,
the nine `>>> REGISTER ROWS FOR MERGE <<<` markers and the fence ticks). **Zero prose lines, zero table lines,
zero claim records and all 10 `### U.nn` sections were lost** — 33/33 claim records recovered in the appendix,
10/10 §U sections in the volume. Reverse check on the data side: `sources.csv` keys are S4423–S4430 with no
`PROV-*` key anywhere in a register, and `conflicts.csv` keys are U.01–U.10 with no row added for the merge's own
convenience.

## 8. The two GM carries, kept instead of smoothed

**(a) An index label misreporting a year is a corpus-level hazard — registered, not typo-corrected.**
`research/A4_harvest_mine.md` stamps the 197,373-byte layer `? / title:1918 | in-window |
TIER1_CANDIDATE_TEXT`; the layer's own first pages print **"TWENTY-NINTH ANNUAL REPORT OF GENERAL MOTORS
CORPORATION / YEAR ENDED DECEMBER 31, 1937"**, its officers page dates the meeting Wilmington, Delaware,
1938-04-26, and its sidecar URL names the file **`gm1937_djvu.txt`** of a multi-file item of which only that
member is on disk. It is **registrant-record material used only as `RETROSPECTIVE`**: S4424 is classed
`RESTATED / RETROSPECTIVE SOURCE`, and every Stage-1 fact it carries (the 1908-09-16 / 1916-10-13 succession
note, the 1929 Holding Corporation, the April-1930 Management Corporation, the 1918 Bonus Plan) is tagged `RETRO`
in `timeline.csv` and in the claim records, never in-window. The mismatch lives in three places on purpose —
**`conflicts.csv` U.09** (both claims, "the printed page wins", the residual question about the item's other
members), **`data_gaps.csv` G-04** (enumerate the whole item), the **`sources.csv` S4424 `notes`** cell — plus
**COR-08**. `A4_harvest_mine.md` was **not** edited: it belongs to the fleet-mine pass, and the hazard is
corrected where a reader of the evidence will meet it. An "in-window" stamp that is wrong would have put a 1937
registrant record inside Stage 1 as contemporaneous evidence; nothing in this dossier is dated from a `title:`
metadatum or a `TIER1_CANDIDATE_TEXT` promotion.

**(b) The author's own self-correction stays visible.** The part's first draft said its naming counts held "over
all six held layers"; the author **withdrew** it because every count in the file is **line-wise over OCR layers
and is therefore a floor, not a census** (method §14.14). The withdrawal is recorded in the dossier at the §B.2
caveat, repeated in §I.3 and §R.2, and in NOTES §8 — all of it untouched by this pass, restated in
`stage_1.md`'s merge record, and registered as **COR-09** with propagation into `conflicts.csv` U.07's
`residual_uncertainty` and `quantitative.csv`'s first `notes` cell. Consequence honoured: `General Motors of
Canada` = 0, `General Motors, Limited` = 0, `General Motors of New York` = 0 are **0-line results**, not evidence
of absence, and the Canadian/UK registry routes stay **UNTRIED** (G-09).

## 9. `CORRECTIONS.md` seeded (gap G-13 answered)

G-13 asks the QC/merge owner to seed the file from U.04, U.05, U.06, U.07, U.09. It exists with nine entries:
COR-01 id re-mint · COR-02 validation/failures binding · COR-03 claim-record relocation · COR-04 "1910
receivership" refuted · COR-05 "1916 expulsion of Durant" re-dated to two attested acts · COR-06 "the 1920 Fisher
merger" is four printed acts · COR-07 Fiat-of-Canada / Anderson / Sheridan / London unsupported · COR-08 the
1918/1937 index mis-stamp · COR-09 the withdrawn "six layers" phrasing. **Each tag reaches the register layer and
a stage volume** — `gates.py --checks corrections`: "9 retraction ids; register layer reaches 9, volumes 9" →
`corrections propagation — all 9 retraction(s) reach registers and volumes`. Propagation was **append-only**: a
tag written at the end of an existing `notes` / `residual_uncertainty` / `claim_supported` / `follow_up_task`
cell. No value, date, metric, carrier key, evidence class or confidence on any of the 114 rows was altered.

## 10. Gate

Required command, run verbatim:
`python tools/gates.py --company-dir founders_playbook/01_companies/company_023_gm --tier auto --out
03_quality_control/gm_s1_gates_merge.md` → **Findings: 2 | Passes: 18, exit 0**
(`03_quality_control/gm_s1_gates_merge.md`).

**The tier reader misses a verdict expressed only as a table row.** `--tier auto` printed
`tier T3 (… 4 mentions, 0 on a verdict line)` and then graded the volume against the T3 8,000-word target,
producing finding 2: `advisory stage_1.md — 20192 words over the T3 density target 8000`. The dossier issues
**T2 core** (`research/A_chronology_feasibility.md` §3, Stage-1 row: "(c) periodical + (d) corporate print = 2 |
**T2 core**"). The tool's own message says to trust the dossier and tell it, so that is what was done: the budget
check was re-run with **`--tier core` explicit** →
`python tools/gates.py --company-dir … --tier core --out 03_quality_control/gm_s1_gates_merge_tiercore.md` →
**Findings: 1 | Passes: 19, exit 0**, and `budget stage_1.md — 20192 words (target 22000, hard cap 60000)`
**PASS**. **The dossier was not edited to satisfy the tool, and no data was reshaped to silence a gate** (shared
brief, "Gate before you report"). The reader defect is recorded here for whoever owns `gates.py`.

_Where the sheets live_: `--out` resolves against the caller's working directory, so the two reports were
regenerated at the canonical company-QC location —
`founders_playbook/03_quality_control/gm_s1_gates_merge.md` (+ `.json`) and
`founders_playbook/03_quality_control/gm_s1_gates_merge_tiercore.md` (+ `.json`) — beside the author's
`gm_s1_gates_p1.md`; the duplicate pair a first run dropped in the repository-top `03_quality_control/` was
removed by this pass, which created it. Both were re-run **after the final write** so the counts in them are the
counts on disk (20,192 words).

What the passing checks now say: all nine registers width-clean
(`timeline 30×11, quantitative 26×12, conflicts 10×15, sources 8×18, data_gaps 13×8, validation 6×11,
failures 8×11, decisions 8×15, channels 5×11`); `csv … .source_id all S#### tokens resolve` on timeline,
validation, failures, decisions, channels; `keys stage_1.md 8 source tokens all resolve`;
`anchors parity 10 <-> 10`; `corrections propagation all 9`; `coverage 9 registers, 1 stage volumes,
49 source documents` — the pre-merge `no register CSVs … csv/anchors gates DID NOT RUN` finding is gone.

Two findings remain, and neither is the merger's to close:
1. **`quotes` ADVISORY — 10 of 24 checked spans unmatched (42%)**, the tool itself labelling it "a triage list,
   NOT as defects", plus 65 unattributed spans. Every one of the ten lines is a **verbatim quotation the author
   cited with a carrier and line number** (e.g. `FH28` L9151 "The present General Motors Corporation was
   incorporated under the laws of Delaware on October 13, 1916", the $1,827,694/$1,195,880/$17,279 Olds
   consideration, the 96-and-20-per-cent-bonus note terms). The part declares a standing OCR reading-text
   convention on its own header lines (hyphenation and double spacing closed up, no word changed), and the
   matcher indexes the raw squashed layers — that is exactly the class of mismatch the citation-and-verbatim
   audit exists to settle, span by span, against the page. **I did not re-quote, re-punctuate or delete any
   span to make this advisory go away.** Handed to the audit pass with the ten evidence lines printed in the
   gate file.
2. **The T3-target advisory above**, which disappears on the `--tier core` run and reappears on every `auto`
   run until the reader is fixed. Two notes recorded with it, not as findings: `keys` reports "stage_1.md
   mentions 4 retired keys inside collision/re-key/range text — protected history, not re-pointed: S0001, S4222,
   S4229, S4422" (that is my own id-audit sentence naming the collision range and the ranges I minted above);
   and `anchors` reads 2 ids (U.01, U.09) as backticked range endpoints rather than citations.

## 11. Five families as carried into Stage 1 (restated from the probe and §S/§T — this pass ran no retrieval)

| family | Stage-1 status | what it yielded, or why it is not a null | registered at |
|---|---|---|---|
| **(a) filings** | **RETURNS-NOTHING-WITH-PERIMETER** | `sec_intake` resolves "General Motors" to CIK **1467858**, the 2009 Delaware person (a fourth holder of the name), index floor **2009-07-16**; historic CIK **140139** is **UNANSWERED** (HTTP 404 `NoSuchKey`); 319 in-window filings left NOT-ENUMERATED at our own `--max-docs 40` | S4429 · G-08 · §S · U.01 |
| **(b) web archives** | **UNTRIED** | no tool was run for gm; no wayback byte exists under `sources/`, so `archived_url` = `NONE_HELD (no wayback capture exists under sources/)` in all 8 source rows — a status, not a null | `sources.csv` · §S · NOTES §5 |
| **(c) periodical corpora** | **RETURNS** | the load-bearing in-window layers: 1928 book (S4423), 1929 Hong Kong newspaper (S4425, misfiled under `corporate_print/`, md5-identical twin), plus the 1895 shell (S4428) used **only** as a negative control; **7 in-window Google Books items reached but never text-resolved (HTTP 503)** = UNANSWERED with remedy | §B–§T · G-01 · FETCH REQUEST 2 |
| **(d) digitised corporate print** | **RETURNS** | 1920 Dayton-Wright brochure (S4426, earliest held naming, not an origin document), 1937 registrant annual report (S4424, `RETRO` only), 1931 GM Truck report (S4427, refused into Stage 1); the fleet `NULL` for this family stays **refused** — a year-faceted `numFound=0` (RD-130) | §T · G-04 · U.09 · FETCH REQUEST 1 |
| **(e) auction / museum documentary** | **UNTRIED — structurally: no tool exists** | the family that has produced other companies' founding papers; for a 1908 holding-company act whose paper is a charter and stock certificates it is the most relevant untouched route | G-02 · U.03 · FETCH REQUEST 4 |

Tier inherited and unchanged: **Stage 1 T2 core** (2 of 5 families with in-window opened text; 22k cap; 6–9 runs),
Stage 2 T3 provisional, Stage 3 T3 provisional-and-not-yet-a-verdict. No re-tiering on this pass; the author's
logged disagreement stays where he logged it.

## 12. Not applied, refused, and left open — named rather than dropped

- **FETCH REQUESTs (4, in `_parts/NOTES_gm_p1.md` §6): NOT RUN.** Enumerating the whole
  `general-motors-annual-reports` item; retrying the seven 503'd in-window Google Books ids;
  `sec_intake.py index 140139` + a `--max-docs 400` re-run; the Canadian/UK registry and the auction/museum
  route. They are the orchestrator's dispatch list; this pass used **0 WebSearch / 0 WebFetch** and has no
  retrieval mandate. They remain open as G-01/G-02/G-04/G-08/G-09/G-10 — none is a null.
- **`_parts/s1_p1.md` was not "tidied".** Three dangling cross-references to a section **§V** the part never
  wrote (l.7, l.17, l.44) and the absence of a `## Untried` heading (the routes are in §S's gap rows and NOTES §5)
  are recorded here and in `stage_1.md` for the audit pass; §14 rule 4 bars a merge from rewriting another pass's
  released words. Same for the ambiguous sentence at l.614 ("One row was withheld from every register: no row
  anywhere asserts a figure absent from a held line") — its second clause contradicts its first; the census
  parsed 114 rows and 114 are on disk, so nothing is missing, and the wording is the audit pass's to settle.
- **No row was added from prose.** `channels.csv` has exactly the 5 emitted; the claim records, §K and §P were
  not mined for extra register rows.
- **`research/*.md`, `sources/**`, `tools/`, `_ID_BLOCKS.tsv` beyond my 8 minted rows, and every sibling company
  were left untouched.** `sources/` was not deleted, moved, pruned or renamed; `candidates.csv` (72 gm rows),
  `sources/harvest_mine/_index.json` and `sources/sec/` (85 files) were **not re-opened** — the earliest
  filingDate there is 2009-07-16, the perimeter S4429 and G-08 already record.
- **What I did not examine, stated plainly:** I did not verify a single quotation against the page images or the
  OCR layers (that is the citation-and-verbatim audit), I did not re-measure any adjacency count, I did not
  re-derive any figure, and I did not test whether the 25,046-word part is *right* — only whether all of it
  landed.
- **Claims released, not bypassed.** Every path written by this pass was claimed with
  `scaffold.py claim --agent merge-gm` before writing and released `--done` after; no `--force` was used.
  Two claims found in this directory belong to dead agents (`s1-gm-p1` on `_parts/s1_p1.md`, `probe-gm` on
  `research/A_chronology_feasibility.md`) and were **left held for the orchestrator**, which owns
  `scaffold.py release --agent X --all`.

## 13. Next passes

Audits (numbers+hindsight; citation+verbatim) by agents other than the author and this merger, then a certifier
who is neither author, merger, auditor nor repairer. The `quotes` advisory list in §10 is the natural opening
triage for the verbatim auditor; the `--tier auto` reader defect is `gates.py`'s owner's.

STATUS: WRITTEN (closed out, merge-gm, 2026-10-07)
