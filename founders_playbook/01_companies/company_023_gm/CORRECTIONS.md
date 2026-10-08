# CORRECTIONS.md — company_023_gm (Stage 1)

Append-only provenance/correction register for the General Motors Stage-1 dossier, **seeded at the Stage-1
merge pass, 2026-10-07** (agent `merge-gm`). It exists because `data_gaps.csv` row **G-13** ("no
`CORRECTIONS.md` for this company — UNTRIED, and not this agent's file to write") names the QC/merge owner as
its owner and asks that it be seeded from **U.04, U.05, U.06, U.07 and U.09** — the five inherited premises the
author refuted or re-dated on held bytes. Nothing here re-tiers, re-dates, re-values, deletes or averages a
claim: the merge is not an audit and does not certify.

**Two classes, kept separate.** COR-01…COR-03 are *mechanical* merge corrections (key space, block attribution,
file geometry) — the only classes a merge may act on. COR-04…COR-09 are **registered, not applied**: they
record what the dossier's own §U conflict sections already conclude against inherited brief premises, so that a
later reader of a register cannot mistake a registered retraction for a live claim.

**Propagation rule (method §14.10).** Every `COR-nn` is printed in this file, **in the register layer**, and **in
a stage volume** (`stage_1.md`, MERGE RECORD §"Corrections seeded at merge"). A retraction that reaches only the
prose leaves `conflicts.csv` teaching the withdrawn form, which is the failure this project keeps paying for
(RD-059, RD-090, RD-105). Where a tag is propagated into a register, it was **appended to the end of an
existing `notes` / `residual_uncertainty` / `claim_supported` cell**: no value, date, metric, carrier key,
evidence class or confidence on any of the 114 applied rows was altered, and no row was folded or withheld.

---

## COR-01 — the provisional carrier keys `PROV-FH28 … PROV-A4MINE` are superseded by minted ids `S4423–S4430`

**What the author emitted.** Nine blocks with `source_id`/`source`/`claim_a_source`/`claim_b_source` cells
carrying dossier-local `PROV-*` tags, and an explicit instruction that the merge mints them centrally
(`_parts/s1_p1.md` l.614, l.572; `_parts/NOTES_gm_p1.md` §8).

**Correction applied.** `python tools/id_mint.py --count 8 --company company_023_gm --claim --agent merge-gm`
allocated **S4423–S4430**, contiguous and above the highest live id (`--audit`: 343 issued, range
`S0001–S4422`, `next assignable: S4423`). Every register cell was re-minted mechanically, compound references
included (`PROV-FH28 L9467` → `S4423 L9467`); **zero `PROV-*` tokens remain in any register** (regex over all
nine files). The narrative keeps the author's dossier-local labels (`FH28`, `AR37`, `NPSH29`, `DW20`,
`TRUCK31`, `CF95`, `A4`, `PROBE`) as reading keys, bound to the global space by the id map in `stage_1.md`.
**Why a correction, not a rename:** author-minted ids have collided in this project — `S4222–S4229` is cited
today by both `company_011_microsoft` and `company_042_target` — and a local key may not enter the global
register. Any `PROV-*` row found in a live GM register from now on is stale.

**Propagated to.** `sources.csv` S4423 `notes` · `stage_1.md` MERGE RECORD (id map + this tag list).

---

## COR-02 — the 6-row and 8-row emissions are bound to `validation.csv` and `failures.csv` respectively

**The ambiguity.** The two registers share a byte-identical 11-column header, so `tools/merge_census.py`
printed both blocks as `AMBIGUOUS:validation.csv,failures.csv` with "either |" content hints on all 14 rows —
before the merge and after it. That is a schema property of the tool, not a defect in the emission.

**Correction applied — by reading, in three independent checks.** (i) the part's markers name `validation.csv`
at l.747 and `failures.csv` at l.759; (ii) `_parts/NOTES_gm_p1.md` §8 states 6×11 and 8×11, and 6 + 8 = 14 =
the census's unattributed total, with no row in both groups; (iii) semantics — the 6 rows each report what
*validated* something (1908-10-01 exchange cleared; 1910-11 notes fully sold in advance; 1915-10-15 first cash
dividend on the common; 1915-10-01 voting-trust expiry; 1916-05 United Motors at $62; 1918-20 internal
self-financing), the 8 rows each report an *incurred* negative (portfolio abandonment but the Oakland; the
$600,000 Elmore unwind loss; the lapsed Ford option and Maxwell-Briscoe memorandum; the 21%→7.8% share
collapse; $12,531,013.19 of write-offs; the bankers' plant closures; the 1921-22 Sheridan/Scripps-Booth
liquidations; the lost Dodge bid). **No row was moved between the registers.**

**Propagated to.** `validation.csv` first row `notes` · `failures.csv` first row `notes` · `stage_1.md`.

---

## COR-03 — the claim-record appendix lives in `stage_1_claim_records.md`; the records themselves are unchanged

**What changed and what did not.** GM1-C01…GM1-C33 (33 records, 2,801 words) were relocated from
`_parts/s1_p1.md` l.570–l.608 to the companion deliverable `stage_1_claim_records.md` at the §U / claim-record
**section boundary** (method §9.1(3), §9.3), the cut the author named in `_parts/NOTES_gm_p1.md` §8 so the T2
target could be met without an evidence trim. Record ids, ordering, passages, tiers, confidences and
`Conflicts:` cells are byte-identical to the emission; `gates.py stage_docs()` counts the appendix as a
companion, not a narrative volume, so `stage_1.md` measures **20,192 words** against the 22,000-word T2 target.

**Propagated to.** `sources.csv` S4423 `claim_supported` · `stage_1.md` (pointer under §U) · this file.

---

## COR-04 — "General Motors went into receivership in 1910" is refuted on held bytes and must not be revived

**The withdrawn form.** An inherited brief premise, with **no carrier** in this corpus.

**What the bytes print.** The five `receiver(ship)` occurrences in `FH28` (S4423) attach to **other firms**:
Electric Vehicle Company 1907 (L2239); United States Motor Company forced into receivership in 1912 with
150+ controlled corporations liquidated (L2907-2914); Chrysler as "the only important producing enterprise that
is the product of a receivership" (L4329-4331); Lincoln Motor Company at a receiver's sale on 1922-02-04
(L7451-7453). For GM in 1910 the print is a **$15,000,000 first-lien note issue at 96 with a 20 per cent stock
bonus plus a voting-trust agreement that gave the syndicate complete control of the board** (L10230-10233,
L10264-10269): a change of control by contract, not a court receivership. GM's own receivership history is
**UNKNOWN on held bytes** — not absent from the record. Registered in `conflicts.csv` **U.04** and carried by
`failures.csv` (the 1910-15 relative collapse), `timeline.csv` (1910, 1912) and `data_gaps.csv` G-11.

**Limit.** The refutation is *of the premise on these bytes*. An unmentioned New Jersey equity proceeding
remains possible; U.04's `residual_uncertainty` says so and no pass may read the refutation as a null.

---

## COR-05 — "Durant was expelled from General Motors in 1916" is re-dated to two attested acts

**The withdrawn form.** "The 1916 expulsion of Durant", as one event with a court-of-memory author.

**What the bytes print instead** (`FH28` S4423, 1928, quoting 1915-1920): a **1910-11 loss of control** while
Durant is printed as *vice-president* under the bankers' board (L10190-10194); a **1915 restoration**, Durant
succeeding Charles W. Nash as president of the *General Motors Company* with Storrow, E. W. Clark and A. Strauss
leaving the board (L10976-10982); and a **resignation announced 1920-11-30** with Du Pont's succession
(L12465-12468), Durant himself calling it a sale (L12460-12465), du Pont's own report calling it a request for
management (L12478-12480), Storrow calling the 1915 move a taking. **1916 as an expulsion date is unattested in
this corpus.** Registered in `conflicts.csv` **U.05**, `timeline.csv` (1910, 1915, 1915-10-01, 1920-11-22,
1920-11-30) and `decisions.csv` (1920-11-30).

**Limit.** Whether the 1920 resignation also covered an ouster is unresolved; the three interested speakers are
kept disagreeing, not averaged.

---

## COR-06 — "the 1920 Fisher body merger" is four separate acts, none in 1920

**The withdrawn form.** A single 1920 merger.

**What the bytes print** (S4423): Fisher Body Corporation **incorporated in New York 1916-08-21** (L13204-13205);
a **60 per cent interest taken in 1919** for about $5,800,000 cash plus $21,851,000 of serial notes
(L11752-11764); the **cost-plus-17.6-per-cent body contract, also 1919** (L13220-13227); and the **absorption in
1926** by a spring-1926 agreement exchanging the 39.92 per cent minority for 664,720 GM common shares
(L13199-13202, L13232-13235). Registered as **four** rows — `timeline.csv` 1916-08-21 / 1919 / 1926,
`quantitative.csv` 1919, `channels.csv` 1919, `validation`/`failures` untouched — with **conflicts.csv U.06**
holding the 1920 claim and the refutation side by side.

---

## COR-07 — "Fiat of Canada", "Anderson", "Sheridan" and "the London branch" as 1926-28 GM acquisitions do not survive the byte test

**The withdrawn form.** Four acquisitions of 1926-28 named in the inherited brief.

**What the bytes print** (S4423): `Fiat` **0** occurrences, and the Canadian names in GM's own
securities-issued-for table are **McLaughlin Motor Car Co., Ltd.** (L9635-9637) and "Issued for Canadian
Chevrolet and McLaughlin Motor Companies" (L11566-11568); every **Anderson** hit is Ford's original stockholder
John W. Anderson (L6132, L5783, L7050); **Sheridan** is a GM **division organised 1920, producing 1,796 vehicles
in 1921, then liquidated and discontinued with Scripps-Booth** (L12793-12815) — a division, not an acquisition;
**London** hits are bibliographic imprints plus "the Explosives Trades, Ltd. (of London, England)" (L11995).
Verdict recorded in **conflicts.csv U.07** as *refuted / refuted / supported-with-correction / UNTRIED*, with
the Canadian and UK registry routes open as **G-09** and the 1921-22 Sheridan row in `timeline.csv` /
`failures.csv` tagged `(PB-proposed)`.

**Limit — this is the corpus-hazard half of the entry.** A 0-line adjacency count is a **floor, not a census**,
and the Canadian/UK registry family has never been queried for gm: the finding is *no carrier held*, never *no
such company*.

---

## COR-08 — an index label misreporting a year: `A4_harvest_mine.md` stamps `title:1918 / in-window` on a layer that prints 1937

**The withdrawn form.** `research/A4_harvest_mine.md` promotes the 197,373-byte item
`general-motors-annual-reports` as `? / title:1918 | in-window | TIER1_CANDIDATE_TEXT`, i.e. a Stage-1 carrier.

**What the layer prints.** L3-7 "**TWENTY-NINTH ANNUAL REPORT OF GENERAL MOTORS CORPORATION / YEAR ENDED
DECEMBER 31, 1937**"; L20-21 the annual meeting at Wilmington, Delaware, 1938-04-26; and its own sidecar URL
names the file **`gm1937_djvu.txt`** of a **multi-file item** of which only this member was fetched.

**Correction applied — at the use layer, not by editing the index.** `A4_harvest_mine.md` is another agent's
research emission and was **not** rewritten by this merge. Instead: the carrier is registered as **S4424**,
classed **`RESTATED / RETROSPECTIVE SOURCE`**, and every Stage-1 fact it carries (the 1908-09-16 / 1916-10-13
succession note at L5386-5387, the 1929 Holding Corporation, the April-1930 Management Corporation, the 1918
Bonus Plan) is tagged `RETRO` in `timeline.csv` and in the claim records; the mis-stamp itself is
**conflicts.csv U.09** ("the printed page wins", RD-121 class) with the residual "does the same item hold
genuine 1918-1920 reports?" kept live as **G-04** and as FETCH REQUEST 1 in `_parts/NOTES_gm_p1.md` §6.
**Why this is not a typo:** a harvester's `title:` metadatum and a `TIER1_CANDIDATE_TEXT` promotion can both
mis-date a document, and an "in-window" stamp that is wrong is a **corpus-level hazard** — it would have put a
1937 registrant record inside Stage 1 as contemporaneous evidence. Nothing in this dossier is dated from
either label.

**Propagated to.** `sources.csv` S4424 `notes` · `conflicts.csv` U.09 · `data_gaps.csv` G-04 · `stage_1.md`.

---

## COR-09 — the author's own over-claim "over all six held layers" is withdrawn: every naming count here is a line-wise floor

**What was withdrawn.** The part's first draft phrased its entity-adjacency counts (e.g. `General Motors of
Canada` = 0, `General Motors, Limited` = 0, `General Motors of New York` = 0) as holding "over all six held
layers". The author withdrew the phrasing on the same pass, because the counts are **line-wise counts over OCR
layers, which are floors, not censuses** (method §14.14; the `CF95` counts are the probe's and were not even
re-measured). The withdrawal is recorded in the dossier itself — the §B.2 caveat, repeated in §I.3 and §R.2 —
and in `_parts/NOTES_gm_p1.md` §8; the merge left the text in place and restates it in `stage_1.md`.

**Correction applied — none to the data.** No count was raised, lowered or re-measured by this pass; no zero was
promoted into an absence claim. U.07's and U.03's `residual_uncertainty` cells carry the limit, and the routes
that could settle it (G-01, G-09, G-10) are **UNTRIED**, not null.

**Propagated to.** `conflicts.csv` U.07 `residual_uncertainty` · `stage_1.md` MERGE RECORD ("Two GM carries the
merge kept instead of smoothing") · `quantitative.csv` first row `notes`.

---

## Not corrected, and why (recorded so the absence is a decision, not an oversight)

1. **No register row was folded, deduplicated, withheld or re-valued.** 114 rows requested, 114 applied; the
   only byte-level changes to any cell are the `PROV-*` → `S4423–S4430` re-mint (COR-01) and the append-only
   `COR-nn` annotations named above. Re-measured after writing: uniform widths, zero empty cells, zero duplicate
   keys, zero `PROV-*` tokens.
2. **`research/A4_harvest_mine.md` and `research/A_chronology_feasibility.md` were not edited.** They are other
   passes' emissions and own their own tier verdicts; COR-08 registers the mis-stamp where it can do good — the
   register layer and the dossier — rather than rewriting the index.
3. **The tier is not corrected.** Stage 1 stays **T2 core** as the probe issued it at
   `A_chronology_feasibility.md` §3. `gates.py --tier auto` reads **T3** because the verdict sits on a table row
   its "verdict line" heuristic cannot see; the budget check was run with **`--tier core` explicit** and the
   dossier was left alone. A future pass may fix the reader; a merge may not fix data to please a tool.
4. **The three dangling `§V` cross-references and the missing `## Untried` heading are not repaired here**
   (method §14 rule 4): they are named in `stage_1.md`'s MERGE RECORD and in
   `03_quality_control/gm_s1_merge.md` for the audit pass. The substance they point at exists in §S and in
   `_parts/NOTES_gm_p1.md` §5; the addresses do not.
5. **`sources/sec/` (85 files), `sources/harvest_mine/_index.json` and `candidates.csv` were not re-opened by
   this merge.** The earliest filingDate on the resolved registrant is 2009-07-16, which is the perimeter §S
   G-08 and S4429 already record; clearing the 319 NOT-ENUMERATED filings and the seven 503'd in-window items
   are FETCH REQUESTs for the orchestrator, not silent nulls.
