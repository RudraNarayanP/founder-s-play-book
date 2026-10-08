# CORRECTIONS — company_017_meta, Stage 1 (living file: append, never rewrite history)

Maintained by the Stage-1 merge pass (`merge-meta`, 2026-10-07). Every entry names the withdrawn or superseded
text, the bytes that withdrew it, and **where the correction reached** (register cell and volume) — the gate
mechanically checks that each `COR-nn` id appears in both layers. Nothing in `_parts/` was edited; the parts are
the emission of record and are read-only to the merge.

## COR-01 — global id supersession (author-minted keys retired)

`P1S01…P1S11` (part 1) and `P2SRC-1…P2SRC-9` (part 2) were **dossier-local provisional tags**, never live keys
(RD-123: ids minted by authors have collided). This merge minted the block **`S4495 … S4509`** with
`tools/id_mint.py --count 15 --company company_017_meta --claim --agent merge-meta`, allocated above every live
id (audit before minting: 383 issued ids, range `S0001–S4462`; `S4222–S4229` collide across
`company_011_microsoft` and `company_042_target`, so no id was taken from that neighbourhood and no gap was
re-entered). The full map is published in `stage_1.md` §"Global id block and the local-tag map" and re-keyed
**inside every cell of every register** that cited a local tag (including prose cells such as
`independence_note` that named sibling tags). **Reach:** `sources.csv` all 15 rows; `stage_1.md` head and foot.

## COR-02 — `validation.csv` / `failures.csv` block binding

Both parts' validation and failure blocks are **unattributable by schema**: the two registers share a
byte-identical 11-column header, so `merge_census.py` printed p1's 6-row and 5-row groups and p2's 2-row and
3-row groups as `AMBIGUOUS:validation.csv,failures.csv`. Adjudicated by reading, three ways, in
`03_quality_control/meta_s1_merge.md`: the block headings name their target, the counts match both author logs
(validation 6 + 2, failures 5 + 3), and the content is unambiguous (positive existence signals vs adverse
signals). No row moved between the two registers as a result — the ambiguity was a tool limit, not a data defect.
**Reach:** `validation.csv` row 1 and `failures.csv` row 1; `stage_1.md` foot.

## COR-03 — part 2's three byte-level nulls refuted by the stored filings (their paragraphs kept, not deleted)

Part 2, which never opened Exhibit 3.3, published three propositions the bytes contradict. All three are
superseded **inside the same sentences**, with `[MERGE 2026-10-07]` annotations at four places in `stage_1.md`
(§K.2, §K.5, §Q.1, §U.1, §U.4, §U.6) and in the register cells below:

1. **"There is no certificate-of-incorporation exhibit … and none anywhere in `sources/`"; "the day-level
   incorporation date [is] unobtainable from EDGAR permanently"; §U.1 CONFIDENCE "UNKNOWN (day)."** Refuted:
   `sources/sec/0001193125-12-175673_d287954dex33.htm` (Ex-3.3, S-1/A of 2012-04-23, fetched 2026-09-29) recites
   *"The date of filing its original Certificate of Incorporation with the Secretary of State was July 29, 2004,
   under the name TheFacebook, Inc."* **Posture after correction:** EDGAR fixes the day at the registrant's own
   recital, in an **unexecuted form** (`Dated:` line and signature block blank; the bytes print
   `July&nbsp;29,&nbsp;2004`, which is why a literal grep misses it) — so the day is **Medium**, not High and not
   UNKNOWN, and the **Delaware registry (F-2) stays the upgrade route**. The probe's "no EDGAR document can ever
   fix the founding day" is refuted by the same find; the S-1 *accession* 0001193125-12-034517 genuinely carries
   only `d287954dex231.htm`, which is where the probe and part 2 both read from.
2. **"(The `845 million` MAU figure the probe cited was not found in the held S-1 text and is therefore not
   asserted here.)"** Refuted: the S-1 prints `845&nbsp;million` **eleven times** — *"We had 845 million MAUs as
   of December 31, 2011, an increase of 39% as compared to 608 million MAUs as of December 31, 2010."* Part 1's
   row (emitted unverified, "the merge must re-verify") is **verified**; confidence stays **Medium** (one
   company-internal count inside one registration lineage, and a 2011 restatement).
3. **"the corpus contains no `thirty days` string at all (`thirty days` = 0 hits)"** Refuted: exactly **1** hit,
   in `d287954dex102.htm` (the 2005 Stock Plan), and it is an **option-exercise window**; `30 days` = **71** in
   raw bytes / 73 after tag-and-entity stripping, across 19 documents. **The adjudication is unchanged and this is
   the point:** no occurrence is a growth statement, so the 2004 growth claim has **no carrier and gets no
   substitute number**.
   Related narrowing carried from part 1: `Saverin` is not absent from the corpus — it occurs **exactly once**
   (Ex-10.16A, `S4499`) as the defined title *"the Saverin Agreement"*; part 2's 0-hit census holds only for the
   two documents it cited.
**Reach:** `conflicts.csv` U.1 / U.4 / U.6 (`best_supported_interpretation`, `confidence`); `quantitative.csv`
2011-12-31 MAU row; `timeline.csv` 2004-07-29 and 2004-07 rows; `sources.csv` S4496, S4497; `data_gaps.csv` row 2;
`stage_1.md` §K.2, §K.5, §Q.1, §U.1, §U.4, §U.6 and the head's findings list.

## COR-04 — provenance drift in the S-1 body, **reported, not repaired**

`0001193125-12-034517_d287954ds1.htm` measures **2,657,075 bytes / sha1 `d749855af01f3d71ca1050f5f4f26d2064efc68f`**
with mtime 2026-10-07 on disk, while its own sidecar and `_MANIFEST.csv` record **2,627,682 bytes / sha1
`bf14d10705701812c3be8ea3712583fed341ea09`, fetched 2026-09-29T19:05:37Z** — the body was re-fetched without the
sidecar being rewritten. The 424B4's sidecar **does** match (`f7fa2eb2…`), so the drift is specific to one file.
**Choice and reason, stated as required:** this merge rewrote **neither** side. `sources/` is a protected archive
and §14 rule 4 forbids a merge tidying it; and a hash "fixed" to match the bytes would destroy the only evidence
that the drift exists, while bytes rolled back to match a stale hash would replace the document every quotation in
this dossier was read from. The merge **re-measured both hashes and published the mismatch** as a
`validation.csv` row (the one row this merge authored rather than applied, on the dispatch's explicit instruction)
and in `_MANIFEST.md`. Every quotation rests on the current bytes at the path (§14 rule 11).
**Reach:** `validation.csv` row 8; `sources.csv` S4496 (`notes`); `data_gaps.csv` row 11; `_MANIFEST.md`;
`stage_1.md` head.

## COR-05 — the accession's image inventory, measured against the held file list

The probe and part 1 print **"26 `g287954g*.jpg` figures"**; part 2 prints **"23 JPGs + a signature image"**. The
held `_index/S1_accession_filelist.txt` lists **28 items, of which 23 are JPGs: 22 `g287954g*.jpg` figures plus
`g287954zuckerberg_sig.jpg`** — so the "26" is not reproducible from held bytes and part 2's phrasing
double-counts the signature. **Reported, not repaired:** the accession itself was not re-listed from EDGAR by this
pass, and no `sources/` write is a merge's to make. The OCR route's object is therefore **22 figure images (1
signature image)**, none of which is stored.
**Reach:** `sources.csv` S4506 (`notes`); `data_gaps.csv` row 1 (`follow_up_task`); `stage_1.md` foot.

## COR-06 — the dispatch tier label (T1) is wrong for this company; the dossier's measured T2 governs

The wave table dispatched `company_017_meta` at **T1**, and `tools/gates.py --tier auto` read that label off the
dossier and stamped **T1**. `research/A_chronology_feasibility.md` measures **T2 core: 2 of 5 families returned
in-window Tier-1 text** — filings yes, legal yes at register level, web **UNANSWERED** (CDX 504/503), periodicals
no in-window text, corporate print **UNQUERIED** (breaker), auction/museum **UNTRIED**. Per the standing rule the
wave plan now carries (*the probe's measured tier governs, not the label*; the same correction Dell's author
forced), **the registers and this manifest are written to T2** and the dossier remains the authority. Both authors
wrote at T1 *section density* while reporting the measured 2 of 5, and said so in their logs rather than
re-tiering silently. The gate was re-run for the budget check with **`--tier core` passed explicitly**, which is
the wave plan's correction 3, and the fact is recorded here.
**Reach:** `conflicts.csv` U.7 (`residual_uncertainty`); `sources.csv` S4504 (`notes`); `stage_1.md` head.

## COR-07 — conflict de-duplication: 15 emitted rows → 8 rows, one per subject

Both volumes emitted `conflicts.csv` rows keyed `U.1–U.7` (part 1 seven, part 2 eight, part 2 having adopted part
1's taxonomy verbatim and added `U.8`), which is **seven duplicate `conflict_id` primary keys** and fails the `csv`
key gate. Resolution, per §14 rule 7's recovery rule: **one row per subject, one id, 8 rows.** Part 1's rows are
**canonical for U.1–U.7** — they are the rows carrying the Ex-3.3 recital (U.1), the "Saverin Agreement" narrowing
(U.4), the `thirty days`/`30 days` census (U.6) and the window carriers (U.7), none of which part 2 read;
**U.8 is part 2's alone** and applied unaltered. **No part-2 row was deleted:** every genuinely additive sentence
is appended inside the canonical row, prefixed `[p2's U.n row, <column> …]`, and where part 2's cell asserts
something the bytes refute, the assertion is printed **as superseded with the refuting measurement named** (see
COR-03). **No anchor was renumbered** and part 1's `§U.n` cross-references resolve unchanged; parity is 8 narrative
anchors ↔ 8 register rows.
**Reach:** `conflicts.csv` all 8 rows (`best_supported_interpretation`); `stage_1.md` head §"Anchor ↔ register
parity".

## COR-08 — the `company` literal normalised carrier-faithfully

Part 1 wrote `Facebook Inc.` on 99 rows, part 2 wrote `Meta` on 43; a key-matching join would read them as two
subjects. Convention adopted and published in `_MANIFEST.md`: **the registrant as the cited document prints it.**
`Facebook, Inc.` for every row whose carrier is the 2012 registration lineage, a filed exhibit, a 2004–2008 federal
docket caption or any event dated 2003–2012; **`Meta Platforms, Inc.` only on the two rows whose carrier prints
that literal** — **one row only**, `data_gaps.csv` row 9 (the undated renaming); its carrier is `sources.csv`
S4501, the EDGAR registrant record, and `sources.csv` has no `company` column at all. Verified on the written
bytes, after the final write: `Facebook, Inc.` on **104** rows, `Meta Platforms, Inc.` on **1**, bare `Meta` on **0**; the
remaining **15** live rows are `sources.csv`, whose schema carries **no** `company` column (120 rows in all).
**Bare `Meta` is used on no row.** The 2005 `REGDEX` rows keep `Facebook, Inc.` with attribution **UNKNOWN**,
because a modern literal on an unattributed 2005 index row would write into the register the attribution U.3
forbids. Note for auditors: the S-1 sidecar's own `registrant` field prints "Meta Platforms, Inc." for a 2012
document filed by Facebook, Inc. — that is the register's current-name field, not the instrument's name. Neither
part's **prose** was rewritten. **Reach:** all nine registers, column 1; `stage_1.md` head.

## COR-09 — the two things this merge authored, and the ten cells it conformed

Declared because a merge that quietly adds rows is indistinguishable from one that invents them.
**(a) One `validation.csv` row was authored, not applied** — the COR-04 provenance-drift row, which the dispatch
explicitly requires in `validation.csv`; part 1 carried the same fact only as a `data_gaps` row and a source note.
So **120 rows are live against 142 emitted: 119 applied + 1 authored**, and 23 emitted rows were aliased (named in
full in `03_quality_control/meta_s1_merge.md`). **(b) Ten empty cells conformed, no value invented:**
`sources.csv` rows for `S4508`/`S4509` (the CDX and harvest negative artifacts) had empty `event_date` /
`publication_date`, filled `UNKNOWN (no capture: the service refused)` / `n/a (negative artifact, never
published)`; all six part-2 `quantitative.csv` rows had empty `derived_arithmetic`, filled with part 1's controlled
literal `not_derived`. Each fill carries the marker `[MERGE FILL: p2 left this cell empty; no value invented]`.
No UNKNOWN in either part's emission was replaced with a value, and `channels.csv` was **not** padded: part 2's
zero-row block is an earned null and the register carries part 1's four rows only.
**Reach:** `validation.csv` row 8; `sources.csv` S4508, S4509; `quantitative.csv` rows 31–36; `stage_1.md` foot.

## Not corrected, and why

1. **The window divergence (U.7) is a live architecture conflict, not an error.** The dispatched dossier window
   2003-01-01 → 2012-12-31 and the probe's July-2004 Stage-1 close are both documented readings; part 1 wrote to
   one and part 2 to the other, and both bodies are published unaltered with their own labels. This merge recorded
   its staging call (keep the dispatched window for Stage 1; hand the 2005–2012 re-homing to the cross-company
   pass) in U.7 and in `stage_1.md` head; it did **not** re-stage the company, delete part 2's out-of-window
   labels, or move any row between stages.
2. **The tier overage is advisory.** 34,921 emitted words against a 22,000-word T2 target and a 60,000-word hard
   cap: one volume, logged, **nothing trimmed** (§9.2/§9.3). An overage is not evidence to delete.
3. **The `sources/` archive was not touched at all** — no sidecar rewritten (COR-04), no accession re-listed
   (COR-05), no file pruned, moved or "tidied" (§14 rule 4). **0 web calls were made by this merge**, so no
   Tier-4 material entered the dossier and family (b) stays exactly as the probe left it: **UNANSWERED, not a
   null.** Part 1's F-1 fetch request stands, and because `tools/web_domains.json` carries **no meta slug**,
   family (b) remains UNANSWERED/UNTRIED at route level: a provenance-sourced domain must be requested, never
   invented. Family (e) is UNTRIED for every company, structurally, and stays so here.
4. **`_parts/s1_p1.md` and `_parts/s1_p2.md` were not edited** (§14 rule 7). Their fenced register blocks remain
   the emission of record; the volume carries pointer lines instead of copies so that
   `tools/merge_census.py` cannot read the same rows twice.
5. **The 2004 launch, its month, its day, its first user, its first customer, its first ad price and any 2004–2006
   figure remain UNKNOWN with the routes named.** Withdrawing February and "thirty days" licenses no substitute:
   no replacement value was written anywhere in the registers or the volume.
