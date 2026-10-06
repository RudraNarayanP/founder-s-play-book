# Tesla Stage 1 — audit 1 (independent)

Agent `tesla-s1-audit1`, 2026-09-30. Web calls: **0 made, 0 permitted.** Every object I could not reach is
named in a `FETCH REQUEST:` below. I wrote no register row, no volume line, and repaired nothing.
Read state on disk, not the merger's account of it: the merger's report is **largely accurate and in three
places confidently wrong**, and one of the three is a false null written into the instruction layer.

## VERDICT: **PASS-WITH-FINDINGS**

Stage 1 stands: 208 rows, one volume, anchors 23↔23, gate 2 findings / 0 substantive, tier T3 resolves as the
merger used it, the census's 44 "missing" rows are **proven** to be tool blindness rather than unapplied work,
and the 25-row third emission is fully attributed. But five defects are real, three of them substantive, and
BLOCKER-1 is the defect class this project keeps paying for: **a null recorded where held bytes answer it.**

---

## BLOCKERS (numbered, executable)

### BLOCKER-1 — the 2009-12-31 refundable-reservation balance is NOT unknown; four files and `COR-01` say so in the wrong direction

`conflicts.csv` row `U.23` states in `why_they_differ`: "no printed cell on disk gives a 2009-12-31 reservation
balance"; `CORRECTIONS.md` COR-01 concludes "the 2009-12-31 value is **UNKNOWN**"; `stage_1_index.md` repeats
it; the merge notes §7 repeat it. **Refuted by the bytes on this disk.**
`E:\founder's playbook\founders_playbook\01_companies\company_043_tesla\sources\sec\0001193125-10-149105_d424b4.htm`
prints: *"As of December 31, 2008, 2009 and March 31, 2010, refundable reservation payments in the amount of
$48.0 million, **$26.0 million** and $26.0 million (unaudited), respectively, were recorded as current
liabilities on the consolidated balance sheets."* The same triad ("December 31, 2008, 2009 and March 31, 2010")
occurs 24× in `-129878`, `-139143`, `-147655`, `-147850` and `-149105`; `$26.0 million` occurs 4× in
**`0001193125-10-068933` = S4370**, a row this register minted itself — and there it is explicitly bound to the
period-end: *"As of December 31, 2008 and 2009, refundable reservation payments in the amount of $48.0 million
and **$26.0 million**, respectively, were recorded as current liabilities on the consolidated balance sheets."*
`$24.8 million` occurs 4× in `ds1.htm` only and **0×** in every later printing — exactly what the volume's own
§P.2a table (line 1823) prints. So the 2009-12-31 balance enters the lineage at Amendment No. 1, is printed by
eight held documents, and `U.23`'s two figures are **adjacent period-ends of one filed series, not a conflict**.

Three aggravations:
1. The volume the merge assembled **contradicts the merge's own adjudication**: `stage_1.md` line 1770 prints
   "**$26.0m (2009-12-31)**" and line 1823 prints "The 424B4 prints $48.0m / $26.0m (2009-12-31) / $26.0m
   (2010-03-31)". The conflict row and COR-01 call that same value UNKNOWN.
2. COR-01's "settling route" is written as a **FETCH REQUEST** — "one read of
   `sources/sec/0001193125-10-149105_d424b4.htm` … settles it from bytes already on this disk". The route is
   local; §15.1 forbids fetching what a script can reach, and this needed no fetch at all. A 0-call budget is
   not a reason a local read was not done.
3. The decision the merge said it suppressed is still printed: `decisions.csv` row "2010 (month UNKNOWN) |
   Invert the reservation-deposit instrument" carries `actual_result` = "The liability holds flat at $26.0m
   from 2009-12-31 to 2010-03-31…" — the reading `U.23` says "is therefore not carried as a finding".

**Fix:** (a) add `quantitative.csv` row `2009-12-31 | refundable reservation liability | 26.0 | USD millions |
S4372 (and S4370) | FACT` with the Note sentence as carrier; (b) rewrite `U.23` `why_they_differ` /
`best_supported_interpretation` / `residual_uncertainty`: the supersession is still **declined** (24.8 is a
2009-09-30 datum, 26.0 is a 2009-12-31 and a 2010-03-31 datum — the two $26.0m prints are different
period-ends), and the real conflict is that the **original printing's 2009-09-30 balance disappears from the
lineage after Amendment No. 1**; the residual is the receipts/refunds flow, not the value; (c) supersede
COR-01's UNKNOWN wording with the printed sentence and its accession, per RD-125's rule that a correction must
quote the carrier; (d) re-label the `decisions.csv` flat-liability cell as carried-and-now-supported, or remove
the "not carried" claim from `U.23`.

### BLOCKER-2 — `validation.csv` row 4 puts an event at 2009-05 that every held carrier puts at 2009-11

Row: `2009-05 | First powertrain shipments to Daimler | src S4372 | FACT | High`. The bytes: `-149105` prints
*"In May 2009, we **formalized a development agreement** with Daimler"*, and, separately, *"We **began shipping
the first of these battery packs and chargers in November 2009** and started to recognize revenue for these
sales in the quarter ended December 31, 2009"* (the same sentence in `ds1.htm` and `-002906_ds1a.htm`). The
volume agrees with the bytes and not with the register: claim record **P1-28** ("shipped first in November
2009") and `timeline.csv` row `2009-11 | first battery packs and chargers shipped to Daimler | S4369`.

This is also the deliveries-vs-recognition trap: the shipments and the recognition are different quarters.
**Fix:** set the row's `date` to `2009-11` (carrier: the "began shipping" sentence, `S4372`), keep
`what_it_demonstrated`, and either fold the May-2009 agreement into its own validation row or cite the
"formalized a development agreement" sentence explicitly. Do not delete the row — RD-122's drift rule.

### BLOCKER-3 — three `quantitative.csv` rows cite a per-share figure the cited carrier does not print, across the May-2010 split boundary

Rows `2009-09-30 | Series A preferred as filed on the outstanding line`, `2009-09-30 | Series A class as
described…` (`… x $0.493 = $7499999`) and `2007-11 | Chairman of the board Series A conversion recorded out of
preferred` (`derived: 8000000 x $0.493 = $3944k against $3936k recorded; residual $8k unexplained`) all carry
`source = S4372` (424B4). Measured: `$0.493` occurs **5× in `ds1.htm`, 5× in `-068933`, 5× in `-099603` and
0× in `-149105`**; the 424B4 prints Series A at **`$0.49`**. On the carrier actually cited, 8,000,000 × $0.49
= **$3,920k**, so the "residual $8k" becomes **$16k**; on the S-1 original the residual is $8k. Meanwhile the
same equity line prints **8,000,000 common shares in `ds1.htm` and 2,666,666 in the 424B4** — the 1-for-3
reverse split effected May 2010, correctly registered as `U.13` and in the `timeline.csv` 2007-11 note. The
register therefore mixes two printings inside one derived cell and attributes the mixture to the wrong row.
**Fix:** re-point the three rows' `source` to `S4369/S4370/S4371` (where $0.493 prints) or keep `S4372` and
change the input to $0.49 with residual $16k; in either case state, in the same cell, which printing the
per-share figure is from and that the converted common count is split-adjusted (RD-125's basis rule: a cell
that changes basis must quote the carrier sentence that establishes it).

### BLOCKER-4 — `_MANIFEST.md` publishes sums that its own cells refute, and prints two sections twice

`_MANIFEST.md` Total row: **13,329 words / 111,343 bytes**. Recomputed from the nine files:
per-register words `3,732+1,756+1,862+3,152+1,604+841+372+536+468 = 14,323` (my `split()` count: **14,323**)
and bytes `29,716+15,749+15,189+22,274+11,565+6,329+3,121+4,232+3,768 = 111,943` (measured **111,943**).
Both published totals are transpositions of the values the same table prints — §14 rule 10 (the instruction
layer is the highest-severity home for a stale figure). Also: "## Intermediates and read-only evidence" and
"## Open research debt carried out of this merge" each appear **twice** (lines 48–69 and 71–92), and the first
copy ends with a table row glued onto prose ("…no High gap is unassigned.| Gate finding | **Findings: 2 |
Passes: 20** …"). **Fix:** correct both totals to 14,323 / 111,943, delete the duplicate pair, move the gate
finding into its own table.

### BLOCKER-5 — `timeline.csv`'s central empty interval is contradicted by three rows in the same file

Row: `2003-07-01 -> 2004-05 | no dated corporate act of any kind in the held corpus | S4369 | UNKNOWN | U.1`.
The same register carries, inside that interval, `2003-07 | 2003 Equity Incentive Plan adopted by the board and
approved by stockholders | S4369 | FACT`, `2004-03 | Straubel begins as Principal Engineer`, `2004-04 | Elon
Musk becomes Chairman; Kimbal Musk becomes a director`. The bytes date the first of these explicitly:
`ds1.htm` — *"Our board of directors adopted, and our stockholders approved our 2003 Equity Incentive Plan, or
the 2003 Plan, **in July 2003**"*. "Of any kind" is therefore false as written, and the row that carries the
silence is the row most likely to be quoted bare by the next pass. **Fix:** narrow the range to
`2003-08-01 -> 2004-02-28` **or** re-word to "no dated corporate act in the held corpus other than the three
rows this register carries at 2003-07, 2004-03 and 2004-04", and keep the notes' correct caveat ("not an
inference of inactivity — a property of a private company with no filing duty").

## FINDINGS (advisory; named so the repairer can decline them knowingly)

- **A1** `quantitative.csv` `2009-12-21 | EPA Certificate of Conformity obtained… | 275000 | USD penalty`:
  the date cell is the certificate date (2009-12-21, printed) while the value is the penalty agreed **in
  January 2010** (printed). Two facts, one row, date belonging to neither value. Split, or re-date to 2010-01.
- **A2** `2010-05 | Toyota private placement | 50000000 | derived "2941176 shares x $17.00 = $50000000"`:
  the product is **49,999,992**; the 424B4 prints "$50.0 million" (rounded) and `-11-149963` prints
  `49,999,992` exactly. Mark the cell rounded or use the filed exact figure.
- **A3** `failures.csv` last row `2008 -> 2010 | Memory layer: no document supports any specific near-collapse
  account` has `evidence_class UNKNOWN`, `what_it_demonstrated "Nothing"`. It is an evidentiary null, not an
  incurred operational failure, and `data_gaps.csv` already carries it. Check 3's reverse-misfile test fires on
  exactly one row of twenty; the merge inherited it from part 2's block ordering.
- **A4** Fold preservation is narrower than claimed. `sources.csv` row `S4369` says "aliased emissions survive
  here verbatim, **nothing dropped**"; measured, `relevant_passage` and `notes` do survive, but the aliased
  rows' `source_title` and `independence_note` do not: probe `S0006`'s "independent of the registrant narrative
  (sec registry enumeration)", probe `S0008`'s "Wayback CDX negative artefacts (504 Gateway Time-out; IA
  Temporarily Offline)" and probe `S0009/S0010`'s "Internet Archive advancedsearch responses (3 queries) and
  Google Books…" occur in **no register**. Soften the claim or restore the two columns inside the `MERGE[…]` tag.
- **A5** Three quoted spans are not verbatim, and one of them is nearly a different sentence:
  (i) `stage_1.md` line 2073 quotes "we cannot access all of these funds at once" — the 424B4 prints "We
  cannot, **however**, access all of these funds at once"; (ii) line 2008 quotes "**we** will correct the error
  in the three months ending June 30, 2010", splicing the Conclusion sentence ("…and will correct the error in
  the three months ending June 30, 2010") onto a first-person subject taken from another sentence;
  (iii) line 1168 quotes "competition from other luxury/performance automobile brands in our target market,
  including **Audi, BMW, Lexus and Mercedes**" — every held printing instead reads "we will face **competition
  from existing and future automobile manufacturers** in the **extremely competitive luxury sedan market**,
  including Audi, BMW, Lexus and Mercedes". "luxury/performance" and "in our target market" occur **0×** across
  all 83 held document bodies in `sources/sec/` (61 `.htm`, 19 `.txt`, 3 unreadable `.pdf`; the remaining 2 of
  the 85 files are `_MANIFEST.csv` and `_UNANSWERED.csv`); only the brand list is supported. Mark the elisions
  or quote the whole sentence; (iii) is the one item on this list that a repairer must not wave through as an
  OCR artifact — it is a paraphrase inside quotation marks.
- **A6** Published gate pass counts are not reproducible on today's tool: merger's report
  `03_quality_control/tesla_s1_gates.md/` = **2 findings / 20 passes**; my mandated run on the same bytes =
  **2 findings / 18 passes** (`03_quality_control/tesla_s1_gates_audit1.md`). Findings identical. RD-122's
  complaint, a second time — name the tier and the tool date whenever a pass count is published.
- **A7** Slice offsets in `tesla_s1_merge_notes.md` §1 and `_MANIFEST.md` are character offsets pointing at the
  injected `## Volume N` headings, not at the slices: Volume 1's byte-identical slice starts at **9,859**, not
  9,746; Volume 2's at **103,967**, not 102,736, and matches byte-for-byte except the part's trailing
  whitespace, which the merge replaced by its own rule/addendum. Substance holds; the addresses do not.
- **A8** `sources/wayback/cdx_tesla_com_2008_2011_founderish.json` is **0 bytes** with no sidecar status. The
  founder-is-CEO query's outcome is therefore unrecorded (null? error? never-run?) while `S4390`'s title claims
  "Wayback CDX rows" for a directory that holds no rows. See FETCH REQUEST FRA-1.
- **A9** `_MANIFEST.md` line 69 embeds a markdown table row inside a prose paragraph — malformed table, one row.

## CHECKS RUN, WITH THE ANSWER EACH RETURNED

**1. Merge integrity — the census's 44 "missing" rows are tool blindness, proven row-by-row.** Re-ran
`tools/merge_census.py --verbose`: 14 blocks, requested sources 28 / quantitative 61 / timeline 47 / conflicts
16 / data_gaps 16 / decisions 9 / channels 10 = 187, plus 2 AMBIGUOUS blocks of 9 and 11 rows = **207**, plus
the 25 rows in `research/*.csv` the tool cannot see (RD-127 defect 1, still unfixed) = **232 requested**, and
208 on disk. The 44 keyed misses are exactly `P1S01…P1S12`, `P2S01…P2S16`, `P1U-07/08/09`, `P2U-10…P2U-22`;
**all 44 print in the registers as dossier-local aliases** (`existing_keys()` reads only the key column, so a
post-mint alias in `notes` is invisible to it). Not one is unapplied. Fold arithmetic reconciles exactly per
register: sources 40→24 with 16 aliased into 8 groups; conflicts 22→23 with `U.23` minted; data_gaps 23→15 with
8 aliased; timeline 47→46; quantitative/decisions/channels/validation/failures 61/9/10/9/11 → unchanged.
Duplicate primary keys across the three emissions: **0** (40 provisional source ids and 22 conflict ids tested
in one pass, including part 1 × part 2 × probe); on disk 24 distinct `source_id`, 23 distinct `conflict_id`.
Content test of all 232 emitted rows against the registers: 222 land verbatim; the other 10 resolve to id
re-pointing inside cells (6) and to A4's two-column loss (4). Rows with no source block: none — `gates.py`
resolves every `source_id` token in all six registers that carry the column, and all 8 volume tokens.
Part bodies: Volume 1 byte-identical ✓, Volume 2 identical to the last non-whitespace byte ✓ (A7).

**2. The 25-row third emission — present and attributed.** Probe `research/sources.csv` S0001–S0012,
`conflicts.csv` U.1–U.6, `data_gaps.csv` 7 rows. All 12 source aliases print inside `sources.csv` rows
(S0001→S4372, S0002→S4369, S0003→S4371, S0004→S4375, S0005→S4376, S0006→S4377, S0007/S0008→S4390,
S0009/S0010→S4389, S0011→S4391, S0012→S4392); U.1–U.6 kept their ids and are cited from `timeline.csv`,
`data_gaps.csv` and `sources.csv`; 6 probe gaps fold, 1 survives. `_MANIFEST.md`'s "9 survive as their own
rows / 16 aliased" foots (6+2+1 = 9; 10+6 = 16; 9+16 = 25). Nothing untraceable.

**3. The validation/failures pair — the attribution survives, one row is a misfile.** All 20 rows of part 2's
two AMBIGUOUS blocks landed **cell-for-cell** (only `source_id` re-pointing and one `P2U-17`→`U.17` re-key in
a notes cell differ); block order A(9)/B(11) matches `validation.csv`/`failures.csv` exactly, and part 2's own
instruction list and close-out census both print `validation 9 · failures 11`. Content test: 9/9 validation
rows are positive signals (first revenue, first delivery, reservation demand, Daimler line, capacity→revenue,
first positive gross margin, DOE draw, syndicate distribution, offering executed) — **none describes an
incurred failure**; 10/11 failure rows are incurred failures (gross loss, layoffs, cancellations, repriced
notes, recall, EPA settlement, filed error, significant deficiency, missing cost-receipt data, equity deficit) —
**the 11th is A3**. Blocker-2 is the one validation row whose *event* is mis-dated.

**4. Numbers — 20+ arithmetic claims recomputed from the bytes they cite.** Footing: 14,742−3,458 = 11,284 ✓;
12,881/93,358 = 13.8% ✓ (geographic note; Americas 80,477 + Europe 12,881 = 93,358 ✓); 11,880,600 + 1,419,400
= 13,300,000 ✓; ×17.00 = 226,100,000 ✓; ×1.105 = 14,696,500 ✓; 11,880,600 × 15.895 = 188,842,137 ✓;
1,419,400 × 15.895 = 22,561,363 ✓; 20,886+26,945+45,527+18,585 = 111,943 ✓; (2,046)+2,101+7,699+1,781 = 9,535
✓ → 9,535/111,943 = 8.5% ✓; 1,275+4,341+2,030+506 = 8,152 ✓; 20,585+227 = 20,812 ✓; 6.3+19.7 = 26.0 ✓;
1,063−937 = 126 ✓; 160+154+96+103+45+88 = 646 ✓; 107,487−7,487 = 100,000 ✓ (set-aside cap, filed);
249+2,443 = 2,692 ≈ $2.7m ✓ (error letter); 45.4/465.0 = 9.8% ✓; 8,284+2,135+86+8+7 = 10,520 ✓; (18,585−45,527)
÷45,527 = −59% ✓; 45,419−29,920 = 15,499 ✓; 11,998 = 11,475+523 ✓; XBRL -199,714 / -253,523 / 111,943 / -55,740
✓ present in `xbrl_early_series.csv` with accession `0001193125-12-081990` (i.e. the rows' `source_date`
"UNKNOWN" is knowable from the cited file). **DOE trap: passes** — committed $465.0m and drawn $45.4m are kept
distinct, and the 424B4 itself prints "additional funds borrowed under our DOE Loan Facility **from April 1,
2010 through June 14, 2010 of $15.5 million**". **Deliveries-vs-recognition: one failure (BLOCKER-2)** —
324 is "delivered and recognized revenue on" ✓, 1,063/937 are "sold cumulatively" ✓, but the Daimler row
collapses agreement (May 2009) into shipment (November 2009). **Per-share-across-split: one failure
(BLOCKER-3)**, with the basis itself correctly registered at `U.13`. CONTEMPORANEOUS vs RESTATED: §M tags the
2010-on-2007/09 figures RESTATED ✓ and §P.2a's lineage table is consistent with the printings I measured.
Two cross-layer wording slips: `failures.csv` "Same debt repriced twice in **ten** months" at date range
2008-02→2008-12 versus volume §O.2(a) "twice inside **thirteen** months" — in Feb→Dec 2008 the record shows
one exchange; the second repricing is the Feb/Mar-2009 note issuance at $1.005 (60% discount). Recommend
`2008-02 -> 2009-03` in the register.

**5. Dates — every load-bearing table date has a carrier that prints it.** 2003-07-01 ✓ ("incorporated in the
state of Delaware on July 1, 2003", 12 held documents incl. `ds1.htm`); 2003-07 (Plan, "in July 2003") ✓;
2004-03 ("Principal Engineer, Drive Systems from March 2004 to May 2005") ✓; 2004-04 (Musk Chairman since
April 2004; Kimbal director since April 2004) ✓; 2004-05 (ACAP licence) ✓; 2005-07-11/2007-02-12/2007-04-13/
2007-04-19 exhibits ✓; 2007-11 conversion ✓; 2008-02 first delivery ("did not physically deliver our first
Tesla Roadster until February 2008") ✓; 2008-05 first store ✓; 2008 Q4 layoffs ("lay off approximately 60
employees and curtail our expansion plans") ✓; 2008-10 volume production ✓; 2009-03 prototype/2,000 reservations
✓; 2009-05 recall ~346 ✓; 2009-10 Tesla Rangers ✓; 2009-11 Daimler shipments ✓; 2009-12-21 certificate ✓;
2010-01-20 DOE ✓; 2010-05 1-for-3 split ✓; 2010-06-14 (12 stores; 45.4 drawn; IRA) ✓; 2010-06-24 (2,135 of
10,520 copies) ✓; 2010-06-28/29 ✓. The only date defect is the *silence* claim (BLOCKER-5). The 2008
near-failure is handled the right way: no filed date exists and the volume says so (§O.3), and I verified its
negative claims in the bytes — `going concern` **0**, `substantial doubt` **0** in the 424B4.

**6. Citations — sentences read, not pointers; and my matcher's error rate stated.** I opened the cited bytes
for every finding above. The quote gate's 16 flagged spans (15 unique) resolve as: **10 present verbatim in
held bytes** once tags and HTML entities are unfolded (the gate's raw-text matcher is defeated by `&rsquo;` /
`&#8220;` and by markup splitting the run — RD-131's class, exactly as the merge claimed; this group includes
the 2003-07-01 incorporation sentence, which is why the ADVISORY label on that gate is right); **2 are the
volume's own prose mis-extracted as quotations** ("until that edit happens a green anchors result means…",
"three held exhibits and only three are contemporaneous documents") — instrument artifacts, not defects;
**3 are A5's genuine fidelity defects**, of which A5(iii) is unsupported paraphrase inside quotes, not an
elision. My matcher's own error rate, measured honestly: before entity unfolding it wrongly called **6 of 15
(40%)** absent — `&rsquo;` renders as the word `rsquo` after tag-stripping and breaks the run — and after
fixing that it still very nearly passed A5(iii), because a graded probe that falls back to 20 characters
matched on the trivial words "competition from". Any probe shorter than ~35 characters is not evidence of a
quotation; that is why this list is 3 items and not the 16 the gate prints, and why I re-read each carrier
sentence whole before writing it down. No quotation was fabricated and no source row was minted for a phrase.

**7. Hindsight — evidence, mechanism, alternative, confidence.** §L.1 runs the anti-hagiography test on all
four temptations (IPO price, direct sales, reservation book, federal money) and names the mechanism UNKNOWN
where none is filed; §L.2 hands the firewall to the issuer's own risk factors; §L.3 refuses to read 2008
survival as resilience and names the selection asymmetry (we see 2008 only because the company survived long
enough to be required to describe it). §O.3 grades every closeness measure CLASS RETROSPECTIVE INTERPRETATION,
CONFIDENCE Low-to-UNKNOWN, no carrier, and §A.4's KNOWABLE/NOT KNOWABLE lists match what the bytes actually
fix. `decisions.csv` row 1's `actual_result` reaches past the stage edge ("the uncorrected $(55740)k comparative
later printed in the 10-K") without the §13 `RETROSPECTIVE` label — a vocabulary slip worth one word of fix, not
a firewall breach. No codas score the 2008 survival by what happened after.

**8. Family verdicts — checked against the sidecars, all five.** (a) filings TRIED–ANSWERED ✓.
**(b) web archives: the merger's "TRIED — UNANSWERED" is the right label for the wrong reason and the register
title overstates**: the directory holds 3 negative bodies (2× 504 HTML, 1× IA "Temporarily Offline" HTML) + **1
zero-byte file** (A8); the one CDX call that *answered* survives only as transcription in
`sources/wayback/README_retained_capture_evidence.md`, which itself says "treat as a LEAD". `S4390` is honestly
tagged "TRANSCRIBED NOT RE-FETCHED … a LEAD and not a carrier" ✓ but its `source_title` claims "CDX rows" for a
directory containing none. Not a dead route written as UNTRIED, and not a null — but the row title should read
"negative artefacts + transcribed CDX lead". **(c) periodicals TRIED at metadata / page text UNTRIED ✓
verified**: 3 IA `advancedsearch` bodies with numFound 0/0/6 and 6 items dated 2015–2018 ✓; HathiTrust body is
a Cloudflare "Just a moment…" with sidecar `http_status 403` ✓ UNANSWERED not null; Chronicling America body
likewise a 403 challenge ✓ (RD-129's 404-path caveat applies to the nightly runner's egress, not to this one).
Google Books: both feeds answered, **totalResults 300 each with 10 items returned** — the "post-window" reading
is a first-page statement and should say so (RD-127: pages past the first are not in any body here).
**(d) corporate print TRIED at metadata / items UNTRIED ✓**: numFound 2 = `tesla-logo` (dated 2003-07-01 — the
mis-dating trap the merge correctly refused) and `teslaroadster0000maur` (2008); creator-scoped numFound 0 ✓; no
text layer on disk ✓. **(e) documentary/auction UNTRIED entirely, never written as a null ✓.** Extra legal
family: CourtListener federal-only ✓ (`sources/legal/cl_*.json`, 2 bodies with sidecars), state registry
UNTRIED ✓. No family verdict is inverted, and no UNTRIED is written as a null; the one wording that overreaches
is `S4390`'s title.

## FETCH REQUEST: (0 web calls made; §15.1 — a script reaches these, I may not)

- **FRA-1** `tools/harvest_mine.py` / CDX re-query for `url=tesla.com&matchType=domain&from=2003&to=2009&fl=timestamp,original,statuscode`
  → bytes to `sources/wayback/`, **and** replace the 0-byte
  `sources/wayback/cdx_tesla_com_2008_2011_founderish.json` with a body plus a sidecar carrying `http_status`.
  Settles A8 and the LEAD status of `U.4`.
- **FRA-2** `tools/sec_intake.py grab 0001193125-10-068933` and `-149105` exhibit folders (FR-1 of the merge
  notes): the charter copy that would make 2003-07-01 a non-corporate-lineage date, and the balance-sheet column
  heads (BLOCKER-1 needs no fetch, but the flow data still does).
- **FRA-3** Binary re-fetch of the three staff UPLOAD PDFs (`0000000000-10-010920 / -10-019954 / -10-027152`,
  expected 125,766 / 47,907 / 39,093 B) — `S4386` stays UNANSWERED, not empty, until then.

## RE-MEASURED AFTER MY LAST WRITE (my only write is this file)

`stage_1.md` **53,553 words** / 370,566 B (single volume, 34 `##` sections; under the 60,000 hard cap) ·
`stage_1_index.md` **1,564** · `_MANIFEST.md` **1,652** · `CORRECTIONS.md` **1,475**, COR-01…COR-06 all present ·
registers **208 rows** = 24/61/46/23/15/9/9/11/10, widths 18/12/11/15/8/15/11/11/11, headers 9/9 byte-identical
to `company_001_amazon`'s · anchors **23 ↔ 23**, `conflicts.csv` U.1–U.23 one row each, 0 duplicate keys ·
ids S4369–S4392 (24) contiguous · `gates.py --tier T3`: **2 findings, 0 substantive** (advisory word-count,
ADVISORY quotes 16/58) and `--tier auto` resolves **T3** from `research/A_chronology_feasibility.md`, the tier
the merger used · `merge_census.py` re-run: 207 attributable + 25 in `research/` = 232 requested vs 208 applied,
`missing` still 44 (blindness, BLOCKER-free verdict on the census question). **Re-measured after my last write
again:** every figure above is unchanged (no corpus file was touched by this audit; my only write is this file,
**3,913 words / 26.9 KB**), and the check-6 tally is now 10 supported / 2 instrument artifacts / 3 fidelity
defects = the 15 unique flagged spans.
