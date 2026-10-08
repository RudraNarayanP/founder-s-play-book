# NVIDIA Stage 1 -- merge notes (`nvidia_s1_merge_notes.md`)

Agent `nvidia-s1-merge`, 2026-09-30. Sole owner of: `company_016_nvidia/stage_1.md`, `stage_1_index.md`,
`_MANIFEST.md`, `CORRECTIONS.md`, the nine registers, and this file. Web calls used: **0** (none required, and
none made). Nothing under `_parts/` or `sources/` was rewritten except the authorized `SUPERSEDED 2026-09-30`
footers named at the end of these notes.

## 1. Starting measurement -- `merge_census.py` before any write

Command: `python tools/merge_census.py --company-dir founders_playbook/01_companies/company_016_nvidia
--verbose`. Output as printed:

| register | requested | present | missing | unkeyed |
|---|---|---|---|---|
| channels.csv | 9 | 0 | 0 | 9 |
| conflicts.csv | 16 | 0 | 16 | 0 |
| data_gaps.csv | 20 | 0 | 0 | 20 |
| decisions.csv | 7 | 0 | 0 | 7 |
| quantitative.csv | 65 | 0 | 0 | 65 |
| sources.csv | 16 | 0 | 16 | 0 |
| timeline.csv | 37 | 0 | 0 | 37 |

17 structured blocks parsed; **3 block-groups unattributed**, all with the same cause
`AMBIGUOUS:validation.csv,failures.csv`: `_parts/s1_p1.md` (10 rows), `_parts/s1_p2.md` (6 rows),
`_parts/s1_p2.md` (6 rows) = **22 rows**. TOTAL missing keyed rows 32 (sources 16 + conflicts 16); the
keyless registers report `missing = 0` only because they are censused by count, which carries no information
(RD-127, defect 3).

**Re-measured against the brief.** The brief's Nvidia note reads "3 of 10 blocks unattributed". The measured
figure on this pass is **3 of 17 blocks** (the census counts blocks, and both parts fence every block: p1
carries 8, p2 carries 9 = 17). The row-level figure is what matters: 22 of 192 emitted rows were
unattributable by column overlap. Nothing was dropped for that reason -- see section 3.

**Emission arithmetic, read off the parts' own footers and re-counted by CSV parser:** p1 declares "Row count
requested: 91" (sources 7, quantitative 30, timeline 21, decisions 3, validation 5 + failures 5, channels 3,
conflicts 7, data_gaps 10); p2 declares "Row count requested: 101" (sources 9, quantitative 35, timeline 16,
decisions 4, validation 6, failures 6, channels 6, conflicts 9, data_gaps 10). **192 rows requested total =
170 attributable by schema + 22 in the AMBIGUOUS pair.** The parser reproduced both per-block counts exactly,
so the census total (192) is the number the merge had to account for.

`research/` was also censused by hand, per RD-122's dispatch rule (the tool globs `_parts/*.md` only):
`A_chronology_feasibility.md`, `A3_intake_regrade.md` and `A4_harvest_mine.md` contain **zero**
`>>> REGISTER ROWS FOR MERGE <<<` markers and zero fenced register blocks. There is **no third emission** on
this company; the two parts are the whole request.

## 2. Tier issued, and what it caps

Nvidia's own probe verdict is in `research/A_chronology_feasibility.md` (probe dossier, 5,088 words):
**TIER VERDICT: T3 (register)** -- 1 of 5 corpus families (filings) returns in-window Tier-1 text; family (b)
web archives **UNANSWERED** (six CDX requests, HTTP 503/504, zero bodies), family (c) periodicals
**LEAD_ONLY** (17 scripted tasks, 145 candidate rows, no body read; HathiTrust status 0, Chronicling America
403), family (d) corporate print **NULL in-window** (the one item holds FY2005-FY2026 layers), family (e)
documentary **UNTRIED**. `research/A3_intake_regrade.md` re-confirmed T3 on 31 stored documents / 7,942,444 B
and explicitly **did not re-issue** the tier; `research/A4_harvest_mine.md` adds one
`TIER1_CANDIDATE_TEXT` item (`01.-nvidia-annual-reports`, promoted by `nvidia corporation`) and 5 UNANSWERED.
**I therefore issue T3 / `register` (cap 8,000 words per stage, §15.2) and run `gates.py --tier register`.**
The probe's T2 upgrade condition (one browser-egress Wayback CDX answer AND one in-window periodical body
read) is untested and unmet, so the tier is not lifted.

The emitted parts carry 15,962 + 28,955 = **44,917 words** (measured `wc -w`) against that 8,000-word tier
budget. Per RD-122 this is a dispatch-budget overshoot, not an evidence defect: §9.6 forbids cutting evidence
to fit a file limit, §15.4 makes a missed length target legitimate, and the shape is the dispatch's -- two
parts written at exemplar density against a T3 verdict. Nothing is trimmed, nothing is re-tiered on word
count. Against §9.2's file geometry the merged volume sits in the **amber 40,000-60,000 band**, which is
"allowed to finish the stage as one file", so no §9.3 split is required and none was made.

## 3. The AMBIGUOUS pair: how 22 rows were attributed, and on what evidence

`validation.csv` and `failures.csv` share all 11 column names byte-for-byte (§13 gives them one schema), so
`merge_census.match_register()` scores them tied and returns `AMBIGUOUS`. Attribution was made **by content**,
from the parts' own declarations, and is reproducible:

| block | rows | attributed to | evidence |
|---|---|---|---|
| `_parts/s1_p1.md` combined block | 5 | `validation.csv` | p1's emission footer, verbatim: "validation 5 + failures 5 (one shared column list per §13; **rows 1-5 are `validation.csv`, rows 6-10 `failures.csv`**)". Rows 1-5 are positive signals (Series B 3.6x price; first product shipped; first re-architected revenue; first net income quarter; counterparty-signed Ex-4.3). |
| same block | 5 | `failures.csv` | same footer; rows 6-10 are failures (negative 1995 gross margin; NV1 discontinued/NV2 cancelled; ST yield failure; 94% two-customer concentration; down-priced Series D). |
| `_parts/s1_p2.md` block 5 | 6 | `validation.csv` | p2 emits the pair as **two separate fenced blocks**; this one's rows are all `what_it_demonstrated` = positive readings (Diamond 86%; contract credits as sponsorship proof; first profitable quarter $1,424K; January-1998 month $1,347K; customers lending $11.0M; buyer set widening 94%->80%). Matches p2 §Q's own signal list. |
| `_parts/s1_p2.md` block 6 | 6 | `failures.csv` | every row is a loss class (product withdrawn; three competitor patent suits; negative gross-margin quarter at the new fabricator; receivable allowance to $3,506K; largest customer being acquired by a patent plaintiff). Matches p2 §H.2/§O and §R's failure inventory. |

**Rows kept: 11 validation + 11 failures = 22. Rows dropped: 0. Rows refused: 0.** The two p2 blocks were also
cross-checked against row text, not just against block order, because block order is a convention the census
cannot see.

## 4. Part-1 truncation inventory (coverage limit, not a clean merge)

`_parts/s1_p1.md` as committed: 15,962 words / 113,913 B / 844 lines. **It ends after its own row-count footer
with a horizontal rule and a single stray `#` character -- the first keystroke of a heading that was never
written.** The promised content after that point is absent.

| promised by p1 itself | state on disk | consequence for claims resting on it |
|---|---|---|
| `## Untried` block (explicitly referenced at p1 L123 "See `## Untried`", L459, L523 "items 3-6", L590 "3, 5, 6", L639, and inside emitted rows: `P1K07` residual says "named in Untried", timeline row 1998-05-07 says "the clearest example of a named UNTRIED event") | **ABSENT.** No `## Untried` section exists anywhere in p1. | Seven in-window routes are *cited by number* (items 1, 3, 4, 5, 6, 7, 10) and never *written*. Every `data_gaps.csv` follow-up task that says "UNTRIED-1 / -3/4/5/6 / -7" points at a block that does not exist in part 1. The routes are recoverable ONLY from p2's re-numbered `## Untried` (carried into the merged volume) and from the probe dossier's own `## Untried`, which is a different list. |
| p1's file plan "part 1 of 3 ... (p1 = Header/Boundary/A-F; p2 = G-P; p3 = Q-U + appendix)" | p1 delivered its scope; **no p3 was ever dispatched**; p2 took §G-§U and states the plan change in its own header | No narrative section is missing from the merged volume, but the *appendix* p1's plan assigned to p3 does not exist as a separate artefact: claim records are inline per section (p1 §A.4/§B.6/§C.4/§D.5/§E.4/§F.4; p2 per section). |
| §G-§U, §K, §N, §U | Not p1's scope -- owed by later volumes and delivered by p2 | Nothing owed. |

**Sections present in p1 (all complete in themselves):** Header (incl. dataset, firewall, lineage rule, ID
scheme), Boundary 1-7, §A (A.1-A.4), §B (B.1-B.6), §C (C.1-C.4), §D (D.1-D.5), §E (E.1-E.4), §F (F.1-F.4),
Register rows for merge (8 blocks + footer). **Sections cut off: none mid-table and none mid-prose** -- the
break falls after a completed section, which is why the merge can carry p1 verbatim. What is *unwritten* is
the `## Untried` block that p1's prose presupposes. Per the brief I did **not** reconstruct it; p2's version
is carried forward as the volume's `## Untried`, and the missing p1 block is recorded here, in
`_MANIFEST.md`, in `CORRECTIONS.md` and as a `data_gaps.csv` row.

Claims that rest on the missing block: none of p1's *factual* claims. What is weakened is p1's **route
inventory** -- its UNTRIED item numbers are load-bearing for 8 `data_gaps.csv` follow-up tasks and for the
statement in §Boundary 3 that "family (b)/(c)/(d)/(e) ... See `## Untried`". A reader of the merged volume
finds p2's eleven-route `## Untried` (which re-numbers and cross-references part 1's items explicitly), so the
routes are not lost; the *part-1 numbering* is.

**p1 sections present, enumerated from the file:** Header (dataset/stage/how-to-read, hindsight firewall,
record-selection null, confidence rule, single-lineage finding, ID scheme), Boundary §1 entity question, §2
candidate windows, §3 where the record physically stops, §4 basis of numerals, §5 CONTEMPORANEOUS/RESTATED test,
§6 corrections taken on its own dispatch premises, §7 post-boundary convention, §A (A.1-A.4), §B (B.1-B.6), §C
(C.1-C.4), §D (D.1-D.5), §E (E.1-E.4), §F (F.1-F.4), Register rows for merge (8 blocks + row-count footer).
**Cut off:** everything after the footer -- the `## Untried` block above all, and the third volume p1's own plan
projected (`p3 = Q-U + appendix`), which was never dispatched. **No section is cut mid-sentence and no table is
cut mid-row**, which is what makes the verbatim carry safe: the break falls between complete units.

## 5. Ids minted centrally

`python tools/id_mint.py --count 16 --company company_016_nvidia --claim --agent nvidia-s1-merge` -> **S4353 ...
S4368**, claimed in `founders_playbook/00_universe/_ID_BLOCKS.tsv`, allocated **above the highest live id** (the
tool's own `--audit` printed `next assignable: S4353`, 21 registry claims, 252 ids present in a `sources.csv`)
and never into a gap. Mapping: `P1S01`->`S4353` (S-1 1998-03-06) · `P1S02`->`S4354` (S-1/A No. 5) ·
`P1S03`->`S4355` (424B4) · `P1S04`->`S4356` (FY1999 10-K405) · `P1S05`->`S4357` (submissions index) ·
`P1S06`->`S4358` (stored-document manifest census) · `P1S07`->`S4359` (harvest-mine dossier, part 1) ·
`P1S08`->`S4360` ... `P1S13`->`S4365` (S-1/A Nos. 1-4 and Nos. 5-6) · `P1S14`->`S4366` (Creative/CTI 13G) ·
`P1S15`->`S4367` (six blank-primaryDocument index rows) · `P1S16`->`S4368` (harvest-mine dossier, part 2).

- Every citation cell in all nine registers was re-pointed to the global id; each `sources.csv` row prints its
  local alias inside `notes`.
- Part prose was **not** re-pointed: `_parts/` bodies are carried verbatim and a protected emission is not
  rewritten to satisfy a key. They resolve through the alias table in the `stage_1.md` merge note.
- RD-131 guard applied: **no four-digit token in the parts was treated as an id.** I scanned both parts for bare
  `\bS\d{3,6}\b` outside fenced blocks -- **0 occurrences in either part** -- so this volume carries no
  `S435`-class OCR price that could be mistaken for a citation, and none was minted.
- Id hygiene outside my paths, observed and reported, not touched: `id_mint.py --audit` prints **live collisions
  between Microsoft and Target** (`S4223`, `S4224`, `S4225` cited by both `company_011_microsoft` and
  `company_042_target`) -- RD-131's no-lock defect still open, for whoever owns those registers.

## 6. Duplicate keys checked across both parts in one pass

Run on the parsed emissions before writing, not against the existing registers:

- `source_id`: p1 `P1S01`-`P1S07`, p2 `P1S08`-`P1S16` -> **16 keys, 0 collisions across the parts.**
- `conflict_id`: p1 `P1K01`-`P1K07`, p2 `P1K08`-`P1K16` -> **16 keys, 0 collisions** (+ merge-minted `P1K17`).
- Claim records: p1 declares `P1-01`-`P1-27` (27), p2 declares `P1-28`-`P1-60` (32); **0 colliding
  declarations**, no duplicate inside a part, sequence continuous. Eight ids appear in both files' text
  (`P1-01/-02/-03/-10/-11/-12/-20/-27`); they are **citations** by part 2 to part 1 records, not second
  declarations -- established by parsing the declaration form (`P1-nn Claim:` at line start) rather than testing
  for presence, which is the measurement that would have invented a collision.
- Keyless registers have no primary key, so I tested each one's natural key (`date`+`metric`, `date_or_range`,
  `channel`, `gap`) for repeats across the parts. Result: **no exact duplicate row anywhere**; twelve
  same-subject pairs became collision groups G-01...G-12, every member kept and cross-referenced (table in
  `_MANIFEST.md`). Nothing was merged into a composite value, because that would have created a row neither pass
  emitted.

## 7. Gate run, findings, and one instrument-precision demonstration

Command as briefed: `python tools/gates.py --company-dir
founders_playbook/01_companies/company_016_nvidia --tier register` -> report captured at
`03_quality_control/nvidia_s1_gates.md`. **2 findings, 18 passes on the final run; both findings are
advisory-class, and neither was repaired by editing data.** (`--out` in this tool is a *directory* parameter that
would have created a folder named `nvidia_s1_gates.md`, so I captured stdout to the briefed path instead -- a
brief/tool naming mismatch, recorded rather than worked around silently.) An earlier run of the same command on
the same bytes printed **20 passes**, and the difference is not in this company's data: `tools/gates.py` was
patched by another agent mid-session (its `stage_docs()` now excludes `*_index.md` and `*claim_records.md` from
volume gating, and `gate_budgets()` separates the 60,000-word hard cap from the tier target, which the gate now
labels `advisory`). The two passes that left are `budget stage_1_index.md` and `keys stage_1_index.md` -- the
index is no longer graded as a narrative volume. Observed, reported, and `tools/` was not edited by me (shared
file, live callers).


**The tool moved under this pass; the captured report is the final run.** `tools/gates.py` was re-versioned by
another agent between my second and third runs (file mtime advanced mid-session; the new `stage_docs()` excludes
`*_index.md` and `*claim_records.md` from volume gating, citing Tesla 2026-09-30, and `gate_budgets()` now
separates the 60,000-word `HARD_CAP` defect from the tier cap, which is emitted as `advisory`). The final run
therefore reads **2 findings / 18 passes** -- the two lost passes are `budget stage_1_index.md` and
`keys stage_1_index.md`, which the re-versioned tool no longer grades an index as a volume. Same findings, same
data, fewer checks counting the index file: the report on disk is the post-change run. My own earlier line above
("2 findings, 20 passes") is superseded by this paragraph, and it is kept because the number was true of the
bytes and the tool at the moment it was measured -- which is the only way a later reader can see the tool move.
The re-version *helps*: the budget finding is now printed by the tool itself as "NOT a split mandate and NOT a
defect", which is RD-122's adjudication implemented.


| finding | one line |
|---|---|
| `advisory / stage_1.md` | 46,691 words over the register density target 8,000 -- the tool's own wording is "NOT a split mandate and NOT a defect"; adjudicated in section 2. |
| `quotes / ADVISORY` | 18 of 66 attributed spans unmatched (27 %) -- "treat as a triage list, NOT as defects". Advisory is not a defect (§15.6). |

**Evidence that the quotes finding is detector precision, not fabricated citation.** I re-ran the gate's own
`strip_html`/`_squash`/`REJECT_IN_QUOTE` path over the volume against the 33 held source documents (7,063,950
squashed chars indexed) and printed the failing fragment. The misses are not absent sentences:
(i) **ellipses and markdown emphasis inside a quotation** -- e.g. `CERTIFICATE OF INCORPORATION OF NVIDIA
**DELAWARE** CORPORATION ... IN WITNESS WHEREOF, this Certificate has been subscribed this ...`: the span is cut
at the `...` and the `**`, so a contiguous match against the filing text is impossible by construction;
(ii) **volume prose carried in quote marks** -- e.g. "the words visionary, prescient and legendary do not occur in
this volume" is this volume's hindsight-firewall statement, not a filing sentence;
(iii) **stitched quotations** where the author's connective words sit inside one span (the §Boundary 4 basis
rule, the §Boundary 5 restatement paragraph).
Meanwhile spans the gate flagged as unmatched fragments -- "the company typically pays for wafers", "nvidia s
primary source of competition is from companies that provide", "st is entitled to manufacture the riva128zx",
"on april 9 1998 the company was notified that sgi had filed" -- **do occur in the held bytes**. Two spans in the
sample genuinely did not match ("no officer or employee is bound by an employment agreement", "pay substantial
damages ... cease the manufacture, use and sale ..."), which is the mixed-list the gate says to triage rather
than repair. Most flagged spans sit inside protected `_parts/` slices, so the only alternative -- rewriting them
-- would have damaged emissions to quiet an advisory. **Data left alone.**

**Passes worth recording:** all nine registers width-clean (0 drift); `stage` vocabulary legal everywhere; every
`S####` token in every register `source_id` cell resolves in `sources.csv`; `keys` -- 16 source tokens in
`stage_1.md` all resolve, 2 in `stage_1_index.md`; `anchors` -- 18 declared, 18 register-cited, 0 orphans on
either side, and 6 ids read as backticked/range mentions rather than citations; `corrections` -- 4 retraction
ids, all four reach both the register layer and a stage volume; `budget` -- `stage_1_index.md` 1,125 words inside
target, `stage_1.md` the single advisory finding. `--tier auto` reads **T2** from this company's `CORRECTIONS.md`
and prints the same budget finding against 22,000: observed tool behaviour, not corrected here (the dossier
verdict is T3, and 8,000 is the figure I ran).

## 8. FETCH REQUEST

Declining the fetch is the correct behaviour (§15.1), and this pass held a web budget of **0**, which it spent on
nothing. These documents are script-reachable and are named for the orchestrator, not fetched here.

```
FETCH REQUEST: EDGAR, registrant NVIDIA CORP, CIK 1045810, window 1993-01-01..2001-12-31.
Six in-window accessions are INDEXED with a blank primaryDocument and are NOT stored under
company_016_nvidia/sources/sec/ (carried as S4367 in sources.csv, anchor U.118, timeline rows in both parts):
  1998-03-23  8-A12B  0001012870-98-000716
  1998-04-03  8-A12G  0001032210-98-000344
  1998-05-07  RW      0001012870-98-001200
  1998-05-07  RW      0001012870-98-001201
  1999-01-12  8-A12G  0001012870-99-000093
  1999-01-22  S-1MEF  0001012870-99-000186
Base URL form: https://www.sec.gov/Archives/edgar/data/1045810/<accession-nodash>/
Command when authorised: python tools/sec_intake.py auto 1045810 --company-dir
founders_playbook/01_companies/company_016_nvidia
Why it matters: the RW pair is the only filed event inside this stage whose subject the corpus cannot name, and
an 8-A thirteen days after the S-1 is a sequence question about the offering, not a null.
DECLINED BY THIS PASS: yes -- 0 web calls permitted, 0 made; this is script work (§15.1).

NOT FETCH-REQUESTABLE (no scripted route; recorded as UNTRIED in the volume instead):
  Wayback CDX for nvidia.com 1996-01-01..1999-01-21 -- family (b), six HTTP 503/504 with zero bodies,
    sources/wayback/ empty; needs a browser egress.
  One in-window periodical body -- HathiTrust /cgi/ls (status 0 for the scripted client) or Google Books
    all_pages items HAIAAAAAMBAJ (Maximum PC 2000-03), GAIAAAAAMBAJ (2000-04); Chronicling America is a
    wrong-path 404 per RD-128/RD-129, so it has never been tried as such.
  Family (e) documentary -- 1993 California certificate of incorporation; 1993 Series A purchase agreement and
    stubs at $0.50 (4,303,000 shares, net of $22,000 issuance costs); May 1995 NV1 launch collateral.
```

## 9. Unapplied residue, and what this pass did not examine

Left unapplied deliberately -- each is a correction the Stage-1 auditor owns, not a merge edit:
1. `P1-38` -- cited by p2 `decisions.csv` (the 1999-01-22 row) and p2 §K/§T prose; declared by neither part.
2. `P1G06`, `P1G08` -- cited in p1 prose; no emitted gap row carries either label (p1 gaps are unnumbered, p2
   gaps are addressed by `U.1nn`).
3. p1's §Boundary 4 column enumeration and conflict `P1K05` stay **as written inside the carried slice**; the
   supersession is printed in the register row, in the volume's inline marker and in `CORRECTIONS.md`. Emission
   text was not rewritten.
4. p1's `## Untried` -- see section 4. Not written by me.
5. `sources.csv` rows `S4358`, `S4359`, `S4368` are catalog-level/dossier carriers (tier column values 1 and 4 as
   emitted). They are provenance records, not evidence about the company; kept exactly as emitted because the
   parts cite them.
6. The line citations behind COR-01 and COR-02 (`S4355` l.1941-1985, the Statement of Stockholders Equity rows,
   the quarterly table) were **not re-opened** by this merge. If any fails, both corrections revert and the part-1
   readings stand -- `CORRECTIONS.md` names itself as the place that revert must be written.

Not examined by this pass, stated plainly: **no document under `sources/` was opened** (the brief's READ list named
the two parts, three research dossiers, Amazon as format exemplar and three tools), **0 web calls made**, the
XBRL/`facts` series is absent-by-script so the money series rests on the parts' hand reads, and family (e)
documentary is UNTRIED. The stage boundary (1993-04-05 -> 1999-01-21) was adopted as both parts fixed it; it was
not re-derived here.

## 10. Final measured state (re-read from disk after the last write)

| deliverable | measured |
|---|---|
| `stage_1.md` | **46,691 words** / 323,547 B (one volume, amber band, under the 60,000 hard cap); Volume 1 slice verbatim (594/594 long lines of p1 present), Volume 2 slice verbatim (1,156/1,156 long lines of p2 present); 4 `[MERGE 2026-09-30]` markers in Volume 1; exactly 1 anchor declaration (`U.101-U.118`); 18 distinct `U.1nn` anchors in the volume |
| `quantitative.csv` | WRITTEN 65 rows |
| `timeline.csv` | WRITTEN 37 rows |
| `sources.csv` | WRITTEN 16 rows (S4353-S4368) |
| `conflicts.csv` | WRITTEN 17 rows (P1K01-P1K17) |
| `data_gaps.csv` | WRITTEN 21 rows |
| `decisions.csv` | WRITTEN 7 rows |
| `validation.csv` | WRITTEN 11 rows |
| `failures.csv` | WRITTEN 11 rows |
| `channels.csv` | WRITTEN 9 rows |
| **register total** | **194 rows** = 192 emitted + 2 minted; 0 dropped, 0 folded, 0 refused, 0 width drift, `stage1` on every row |
| `stage_1_index.md` | 1,125 words / 7,201 B |
| `CORRECTIONS.md` | 1,645 words / 10,872 B; COR-01..COR-04, propagation to registers and volumes gate-checked |
| anchors <-> conflicts | 18 declared anchors, 18 register-cited, 0 orphans (gates `anchors` parity pass); `conflicts.csv` 17 rows -- 9 anchor-aliased (p2), 7 anchor-less (p1, truncated §U), 1 minted here |
| census after final write | conflicts 16 requested / **16 present / 0 missing**; the three AMBIGUOUS groups still listed by the tool (a schema-overlap limitation, resolved to 22 applied rows); `sources.csv` prints 16 "missing" purely because emission keys `P1S01`-`P1S16` were re-pointed to minted `S4353`-`S4368` -- the same artifact Microsoft's merged registers print (6 "missing", emission keys `D17`-`D24`). No row lost: 16 emitted = 16 on disk, each with its local alias in `notes`. |
| `_parts/` | p1 16,233 w / 115,586 B and p2 29,155 w / 199,359 B, each with a `SUPERSEDED 2026-09-30` footer appended (the only permitted writes to those paths) |


