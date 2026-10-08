# _MANIFEST — company_017_meta (Stage 1)

**Counts regenerated 2026-10-07** by the Stage-1 merge pass (`merge-meta`) with `wc -w` / `wc -c` on the bytes
**after the last write of this operation** (word = whitespace-delimited token, byte = file size). Every figure
below is a measurement, not a recollection: re-measure before publishing any of them again. The merge applied
**119 of the 142 rows the two parts emitted (99 + 43)** and **authored 1 further row** on the dispatch's explicit
instruction, so **120 rows are live**; the 23 emitted rows not carried as separate rows were **aliased into a
surviving row of the same subject, each named in
`03_quality_control/meta_s1_merge.md`**. No author row was deleted and no author cell overwritten.

## Which ceiling governs which file, and this volume's place under it

§9.1's hard upload constraint (500,000 words / 200 MB per file, whichever binds first) governs every file
including the restored evidence under `sources/` (57,731,064 B). §9.2's caps govern the stage volume. **Tier
cap is a density target, not a file limit (RD-122).**

| measure | value | against the T2 core target (22,000) | against §9.2 |
|---|---|---|---|
| combined emission (both parts, incl. register blocks) | **34,921 words** | 159% | 85% of the 40,000 soft target; 57% of the 60,000 hard cap |
| published `stage_1.md` (register blocks replaced by pointer lines; merge head, foot and COR table added) | **30,212 words / 197,633 B** | **137% — overage logged as ADVISORY** | 76% of the soft target; **50% of the 60,000 hard cap** |

**One volume.** The overage is what §9.2 makes it — advisory, **not a split mandate and not evidence to delete**
— and **nothing was trimmed.** The nine fenced register blocks were deliberately not reprinted in the volume:
`_parts/` is the emission of record, and a second copy of the same rows would read to `merge_census.py` as new
data.

## Tier — three numbers, all kept, and the one that governs

* **As dispatched:** **T1** (the wave table labelled `company_017_meta` T1; the same table was already corrected
  once for Dell on exactly this point).
* **As measured by the dossier:** **T2 core — 2 of the 5 families returned in-window Tier-1 text**
  (`research/A_chronology_feasibility.md` §Verdict: filings yes, legal yes at register level; web **UNANSWERED**
  on an archive.org outage, periodicals no in-window text, corporate print **UNQUERIED** by the consecutive-failure
  breaker, auction/museum **UNTRIED**). Both authors recorded the disagreement instead of re-tiering silently.
* **As read by the machine:** `tools/gates.py --tier auto` stamps **T1** off the dossier's own text
  (`tier: T1 (a stated-verdict line) from A_chronology_feasibility.md — T1/T2 all mentioned in research/
  (7 mentions, 2 on a verdict line)`), and the gate's own reader adds *"if the dossier's own text names a
  different tier, trust the dossier … this reader is not the authority on your finding."*

**The dispatch-label error is recorded, not smoothed: the registers and this manifest are written to T2 and the
dossier is the authority.** The merge gate was therefore run with `--tier core` passed **explicitly** (wave-plan
correction 3), which is the run that produced the advisory overage line above; the `--tier auto` run does not
grade the volume at all, because it thinks the target is 60,000.

## The `company` literal convention (register column 1) — stated because both parts used a different one

Part 1 wrote `Facebook Inc.` on all 99 rows; part 2 wrote `Meta` on all 43. The live registers are normalised
**carrier-faithfully: the literal is the registrant as printed in the document the row cites.**

* **`Facebook, Inc.`** — every row whose cited carrier is the 2012 registration lineage (S-1, S-1/A, 424B4), a
  filed exhibit of it, a 2004–2008 federal docket caption naming Facebook, Inc., or any event dated 2003–2012.
  This is the Stage-1 subject and what those instruments print.
* **`Meta Platforms, Inc.`** — on the **one row** whose cited carrier is that record itself: `data_gaps.csv` row 9
  (the undated 2021 renaming). Its carrier is `sources.csv` **S4501**, the EDGAR registrant record for CIK 1326801,
  which witnesses its own name history and nothing about 2004 — and which carries no `company` column at all, the
  `sources.csv` schema having none. `Meta Platforms, Inc.` exists in this corpus **nowhere else**, and it is
  **undated here**.
* **Bare `Meta` appears on no row.** Part 2's literal is superseded row by row (COR-08) and **neither part's prose
  was rewritten** — `_parts/` and the bodies inside `stage_1.md` keep whatever each author wrote.
* **No modern literal is allowed to date a 2004 instrument.** The 2005-05-06 `REGDEX` and 2008 `NO ACT` rows keep
  `Facebook, Inc.` with attribution **UNKNOWN**, because writing `Meta Platforms, Inc.` there would assert in a
  register the very attribution **U.3** forbids. Related trap recorded for auditors: the S-1's own `.meta.json`
  sidecar carries `"registrant": "Meta Platforms, Inc."` for a document filed 2012-02-01 by Facebook, Inc. — that
  is the register's current-name field, not the instrument's name.

## Provenance drift in the S-1 body — published here as required, **reported and not repaired**

`sources/sec/0001193125-12-034517_d287954ds1.htm` measures **2,657,075 bytes / sha1
`d749855af01f3d71ca1050f5f4f26d2064efc68f`** with mtime 2026-10-07 on disk, while its own sidecar
(`.meta.json`) and `_MANIFEST.csv` record **2,627,682 bytes / sha1 `bf14d10705701812c3be8ea3712583fed341ea09`,
fetched 2026-09-29T19:05:37Z**: the body was re-fetched and the sidecar was not rewritten. The 424B4's sidecar
**does** match its bytes (`sha1 f7fa2eb2…`), so the drift is specific to one file. **What this merge chose, and
why it chose it:** nothing. It rewrote **neither** the sidecar nor the bytes and did not touch `sources/` at all
(§14 rule 4); "fixing" a hash to agree with the bytes, or rolling bytes back to agree with a stale hash, would
destroy the only evidence that the drift exists. The merge **re-measured both hashes and both byte counts**
before writing this paragraph, published the fact as **`validation.csv` row 8** (the one row this merge authored
rather than applied), recorded it in `CORRECTIONS.md` **COR-04**, and left the intake owner's remedy named in
`data_gaps.csv` row 11. Every quotation in this dossier is read from **the current bytes at the path**, which is
what §14 rule 11 requires; the merge re-verified in those bytes the dorm sentence (1 hit), the two
"incorporated in Delaware in July 2004" statements (2 hits), `845&nbsp;million` (11 hits) and `July&nbsp;29, 2004`
in Ex-3.3.

## Deliverables (read these)

| File | Words | Bytes | Contents | Status |
|---|---|---|---|---|
| `stage_1.md` | **30,212** | 197,633 | merge head (tier, window, the seven carried findings, the `company` convention, anchor parity before/after) + **part 1's body verbatim** (§Header, §boundary, §A–§J, `## Untried` 11 routes, F-1…F-5) + **part 2's body verbatim** (§K–§U with §U.1–§U.8, claim records K01–T01) + register-application foot + the COR-01…COR-09 propagation table. Six `[MERGE 2026-10-07]` annotations sit **after** the sentences they supersede; no paragraph was deleted | **MERGED 2026-10-07**; **one volume**; over the T2 density target (advisory), half the hard cap |
| `sources.csv` | 2,265 | 18,316 | **15 × 18**, keys **S4495–S4509**; one registration lineage carried as one witness; 5 p2 rows aliased into p1's carriers, 4 p2 rows kept as their own family carriers | APPLIED 15/15 emitted 20 |
| `quantitative.csv` | 1,302 | 12,123 | **36 × 12**; the FY2007–FY2011 filed series, the 2011-12-31 / 2012-03-31 metric set (845 verified), headcount, P&E, IDC/comScore, the 2,000,000-share cure, plus p2's 6 void-sizing rows | APPLIED 36/36 |
| `timeline.csv` | 1,416 | 11,230 | **23 × 11**; 2003-04 allegation → 2004-07-29 recital (day, Medium) → 2004-07 (month, High) → the seven dockets → 2005–2012 instruments → 2012-05-18 window close | APPLIED 23/26 |
| `decisions.csv` | 701 | 5,184 | **5 × 15**; incorporate in Delaware; fund with family money; print the dorm sentence and not the litigants; proceed while an ownership claim was asserted; control at formation (UNKNOWN cells intact) | APPLIED 5/6 |
| `validation.csv` | 778 | 5,833 | **8 × 11**; 7 applied rows + **1 authored row (COR-04, the provenance drift)**; includes the earned null "NONE RECOVERABLE" | APPLIED 8 (7 + 1 authored) |
| `failures.csv` | 574 | 4,394 | **8 × 11**; the lapsed option, the copyright suit, FY2007/FY2008 losses, the EDGAR silence, contested ownership, the repudiated 2003 agreement, the disclosure failure | APPLIED 8/8 |
| `channels.csv` | 356 | 2,642 | **4 × 11**; advertising, platform developers, Pages, family financing — all four carry the origin-vs-2011 evidence-class split | APPLIED 4/4 (p2 emitted 0: **earned null, not padded**) |
| `conflicts.csv` | 3,055 | 20,467 | **8 × 15**; `U.1–U.8`, **one row per subject**; p1 canonical U.1–U.7 with p2's sentences folded and attributed; p2's U.8 alone | APPLIED 8/15 (7 aliased) |
| `data_gaps.csv` | 1,411 | 10,125 | **13 × 8**; every High-importance gap carries a follow-up task; row 11 is the byte-integrity record, row 12 the CDX route, row 13 founder capital | APPLIED 13/19 (6 aliased) |
| `stage_1_index.md` | — | — | volume map: section homes, anchor→register table, register counts, reading order | MERGED 2026-10-07 |
| `CORRECTIONS.md` | 2,142 | 14,689 | **COR-01…COR-09** + "Not corrected, and why" — id supersession, block binding, part 2's three refuted nulls, the provenance drift, the image inventory, the tier label, the conflict de-duplication, the company literal, what the merge authored | LIVING — append, never rewrite history |

**This register is not self-listed** — a file cannot publish its own final size.

Upload batch 1 = `stage_1.md`; batch 2 = the nine registers + index + corrections + this manifest; batch 3 =
`_parts/`, `research/`, `sources/`. **No file was shortened to meet a number** (§9.6).

## Intermediate emissions (`_parts/`) — retained, read-only, still the emission of record

| File | Words | Bytes | Why retained |
|---|---|---|---|
| `_parts/s1_p1.md` | **25,200** | 174,821 | part 1's whole emission: §Header, §boundary, §A–§J, 33 claim records, 99 register rows in 9 fenced blocks, anchors `U.1–U.7`, `## Untried` 11 routes, F-1…F-5. **Not edited by the merge** |
| `_parts/s1_p2.md` | **9,721** | 70,896 | part 2's whole emission: §K–§U (the §U body both parts' registers cite), 17 claim records, 43 register rows in 9 fenced blocks, anchors `U.1–U.8`. **Not edited by the merge**; its four superseded passages are annotated in the volume, not deleted here |
| `_parts/NOTES_meta_p1.md` | 2,739 | 18,404 | the author's log **and the merge's instruction sheet**: §10 and §12 hand over the conflict de-duplication, the `company` literal, part 1's canonical provenance and the outbound correction to part 2's day-level null — all three executed and recorded (COR-03, COR-07, COR-08) |
| `_parts/NOTES_meta_p2.md` | 1,654 | 11,421 | part 2's log: the anchor handoff, its own three probe corrections (two of which the bytes refuted — COR-03), its withheld `channels.csv` rows and FY2011 revenue row |

## Research dossiers (scope of record — not touched by the merge)

| File | Words | Bytes | Role |
|---|---|---|---|
| `research/A_chronology_feasibility.md` | 4,337 | 28,975 | **the authority for the tier and the five-family verdict**; issued T2 (2 of 5), the stage boundaries, the conflicts META-C1…C5 and the untried routes. Its "no EDGAR document can ever fix the founding day" is refuted by Ex-3.3 (COR-03) and the refutation is recorded here rather than by editing the dossier |
| `research/A4_harvest_mine.md` | 806 | 4,882 | the window carrier (`2003-01-01..2012-12-31`, deliberately wide) and the harvest-mine census |

## The five families, carried with their states distinct (no blocked family reported as absent)

| # | family | state | in-window Tier-1 text? | closing route |
|---|---|---|---|---|
| (a) | SEC / EDGAR filings | **TRIED–ANSWERED** (registrant-retrospective for the origin) | **YES** | F-4 (the 6 `UPLOAD`/`.paper` items), F-5 (the 5 `CORRESP`), the 9 in-window filings `_UNANSWERED.csv` says were never listed at `--max-docs 30` |
| — | legal records | **TRIED–ANSWERED at register level; UNTRIED for pleadings** | **YES** (register, not narrative) | **F-3** RECAP/PACER text — one of the two re-runs that would make this T1 |
| (b) | web archives | **TRIED–UNANSWERED** — the service refused 504/503; **not** a null, no capture disproved | NO | **F-1 stands.** `tools/cdx_intake.py` exists but **`tools/web_domains.json` has no meta slug**, so the family stays **UNANSWERED/UNTRIED at route level**: a provenance-sourced domain must be requested, never invented |
| (c) | periodical corpora | **TRIED–UNANSWERED** (CA 403 ×3, HathiTrust status 0 ×2); **metadata-only** for Google Books (22 rows, 1 in-window); **UNQUERIED** for internet_archive | NO | periodical re-run; a college/student-press corpus has **no configured route** (fleet-level gap) |
| (d) | digitised corporate print | **UNQUERIED** — task authored, killed by the consecutive-failure breaker | NO | `--source-family corporate_print --source-family internet_archive` re-run; "exists only in private hands" is **not licensed** |
| (e) | auction / museum / manuscript | **UNTRIED** — 0 calls; structurally no tool and no domain slug | NO | a scripted auction/museum pass; the probe declines it as the least informative family for a 2004 internet company |

**2 of 5 → T2 core.** Neither part nor this merge upgraded it. Two cheap re-runs (CDX once archive.org answers;
RECAP docket text for `1:04-cv-11923`) would make it genuinely T1, and the probe says so.

## Census of this operation (measured, not asserted)

| reading | before any write | after the final write |
|---|---|---|
| structured blocks parsed | 17 | 17 |
| rows requested | 142 | 142 |
| `conflicts.csv` present / missing | 0 / 15 | **15 / 0** — all 15 emitted `U.1–U.8` keys resolve onto **8 live rows**, which is the de-duplication proved by the tool rather than asserted by me |
| `sources.csv` present / missing | 0 / 20 | 0 / **20** — the 20 are the superseded local tags `P1S01…P1S11`, `P2SRC-1…9`; the minted ids `S4495–S4509` are the live keys (COR-01) |
| TOTAL missing keyed rows | 35 | **20** (all sources tags) |
| unattributed block-groups | 4 (`AMBIGUOUS:validation.csv,failures.csv`) | 4 — unchanged: a schema property of the two registers, adjudicated by reading and recorded (COR-02), not a missing row |
| unkeyed rows (no key column to match) | channels 4 · data_gaps 19 · decisions 6 · quantitative 36 · timeline 26 | same — all counted by row, and all on disk |
| third emission in `research/*.csv` | none: `research/` holds only the two dossiers | none |

## Gate and merge records

* `03_quality_control/meta_s1_merge.md` — the merge's live account: census before and after, the
  validation/failures adjudication, the conflict de-duplication, the `company` literal ruling, the id allocation,
  the fold list naming every unapplied row, and the byte measurements this merge took.
* `03_quality_control/meta_s1_gates_merge.md` (+ `.json`) — the gate run **after every write**, with
  `--tier core` passed explicitly: **Findings 2 | Passes 18**, both findings advisory — `quotes` "10 of 35 checked
  spans unmatched (29%) — treat as a triage list, NOT as defects" and `budget` "30212 words over the core (this
  volume's issued tier) density target 22000 — NOT a split mandate". Passing: `csv` for all nine registers
  (widths 18/12/11/15/11/11/11/15/8, 0 off-width, 0 empty cells), `*.source_id` all resolve, `keys` "15 source
  tokens all resolve", **`anchors` parity 8 narrative ↔ 8 register** and citation resolution,
  **`corrections` propagation "all 9 retraction(s) reach registers and volumes"**.
* The `--tier auto` run on the same bytes stamps **T1** and therefore reports **1 finding** (no budget advisory):
  the tier-label divergence is recorded above rather than argued with the tool.

## Open items this merge did NOT close (named, not dropped)

1. **F-1…F-5 all remain open exactly as the parts measured them**, and family (b) cannot be run as written: no
   meta slug in `tools/web_domains.json`, so a **provenance-sourced domain** must be supplied (a filing line that
   prints it) — never invented.
2. **The staging seam (U.7)** is unresolved on purpose: this merge recorded its own call (keep the dispatched
   2003→2012 window for Stage 1) and left the re-homing of the 2005–2012 material between Stage 1 and Stage 2 to
   the cross-company pass. Both bodies are published against the close they were written to.
3. **The Delaware certified copy (F-2)** is still the only route that converts the 2004-07-29 **recital** into a
   **record** and reaches the founding share structure; until then the day stays Medium and the authorised capital
   stays UNKNOWN with no substitute value.
4. **The provenance drift (COR-04)** is open with the intake owner, not with this archive: the remedy is a
   sidecar re-run for accession 0001193125-12-034517, which this pass was not authorised to perform.
5. **The image inventory (COR-05)** — 22 figure JPGs + 1 signature of 28 items, none stored — is measured from
   the held file list only; the accession was not re-listed from EDGAR by this pass.
6. **Nothing was audited or certified here.** Every count in this manifest is a measurement of the merge's own
   writes; an audit by a different agent must re-measure it, and the certifier must be neither author, merger,
   auditor nor repairer.
