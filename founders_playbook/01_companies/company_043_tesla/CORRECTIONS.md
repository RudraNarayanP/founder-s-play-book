# Provenance Corrections Register — Tesla (company_043_tesla)

Standing list of attribution, dating and counting corrections established **at or after** the two Stage-1
author passes and verified against the bytes held under this company's `sources/` (read in place; **0 web
calls on every pass that produced these entries**). The Stage-1 merge pass (`tesla-s1-merge`, 2026-09-30)
opened this file; Tesla had none before, because it had no registers and no volume. **Repair pass 1**
(`tesla-repair-1`, 2026-09-30, **0 web calls made, 0 permitted**) did not add an attribution correction to the
record: it **retracted COR-01's own conclusion**, which was a false null written into the instruction layer
against bytes already on this disk.

**Rule (§14 rule 10, enforced by `gates.py --checks corrections`).** Every `COR-nn` here must appear (i) in at
least one register row and (ii) in at least one stage volume that carried the withdrawn text. Both are
satisfied for COR-01…COR-06: the register homes are named in each entry, and the whole set is propagated in
the "Corrections applied at merge" block at the foot of `stage_1.md`. **COR-07** (repair pass 1) is propagated
the same way: the "Stage-1 repair pass 1" block at the foot of `stage_1.md` and the register cells named in its
own "Lands in" line.

**A repair pass is not a certifier (§15.6, AUDIT-rule 1).** Nothing here is signed off by the agent that wrote
it: COR-01's re-grade and COR-07 await re-certification by a **different** agent.

**Supersede, don't erase.** No emission was deleted. Where a statement is withdrawn, the superseded wording is
printed inside the correction and inside the surviving register row, tagged `MERGE[…]`.

---

## COR-01 — part 2's supersession of part 1's refundable-reservation figure is declined (it supersedes a different date) — **RE-GRADED ON REPAIR 2026-09-30; the merge's own "UNKNOWN" conclusion is WITHDRAWN here**

**Withdrawn:** the assertion in `_parts/s1_p2.md`'s quantitative emission that the $26.0m refundable reservation
liability at **2010-03-31** "SUPERSEDES the 2009-09-30 $24.8m figure part 1 carried from the original printing",
together with the derived reading in part 2's channels and decision rows that the liability "holds flat at
$26.0m from **2009-12-31** to 2010-03-31".

**Why.** Both parts print two figures attached to two different period-ends: part 1's $24.8m is a
**2009-09-30** unaudited nine-month balance-sheet date (`S4369`, the 2010-01-29 printing); part 2's $26.0m is a
**2010-03-31** date (`S4372`, 424B4). Neither emission registers a carrier for a **2009-12-31** balance, and
part 2's own §G.4/§P.2 cells use 2009-12-31 as though it were the same datum as its 2010-03-31 figure. A
supersession across two different measurement dates is not a correction, and the merge could not settle it
against the filing because the web budget was **0 calls and 0 were made**.

**Both dated figures stand.** $24.8m at 2009-09-30 and $26.0m at 2010-03-31 are carried; **the 2009-12-31
value is UNKNOWN**, and the "flat liability across the deposit-policy inversion" reading is **not carried as a
finding**.

**WITHDRAWN BY THIS REPAIR PASS (2026-09-30, `tesla-repair-1`); the sentence above is kept printed because a
retraction is itself a claim.** The clause "**the 2009-12-31 value is UNKNOWN**" is **false as written** and the
clause "**not carried as a finding**" is withdrawn with it. The bytes this merge already held print the value:

* `sources/sec/0001193125-10-068933_ds1a.htm` (**S4370**, Amendment No. 1, filed 2010-03-29) — *"As of December
  31, 2008 and 2009, refundable reservation payments in the amount of $48.0 million and $26.0 million,
  respectively, were recorded as current liabilities on the consolidated balance sheets."* The same body binds
  $26.0m to **2009-12-31** in four separate sentences, including *"As of December 31, 2009, we had an aggregate
  of $26.0 million in refundable reservation payments for the Tesla Roadster and the Model S."*
* `sources/sec/0001193125-10-149105_d424b4.htm` (**S4372**, 424B4) — *"As of December 31, 2008, 2009 and March
  31, 2010, refundable reservation payments in the amount of $48.0 million, $26.0 million and $26.0 million
  (unaudited), respectively, were recorded as current liabilities on the consolidated balance sheets."*
* Measured on this disk 2026-09-30: **11 held document bodies across 8 accessions** print a sentence binding
  $26.0m to 2009-12-31; `$24.8 million` occurs **4× in `ds1.htm` and 0× in every other held body**.
* **Recounted 2026-10-06 (`tesla-residuals`, certifier item B2\*):** the figure in the preceding bullet is the
  **2010 registration lineage only**, not the corpus. Measured again, tag-stripped, sentence by sentence across
  `sources/sec/`: **15 held bodies across 11 accessions** bind $26.0m to 2009-12-31. The three additions are the
  two unregistered 2011 printings `-11-149963` (txt + htm) and `-11-157135` — *"As of December 31, 2009, 2010 and
  March 31, 2011, reservation payments in the amount of $26.0 million…"* — and, the one that matters, the
  **registered FY2010 10-K `S4375`** (`0001193125-11-054847_d10k.htm`), which binds the same value inside a
  **different instrument family**: *"As of December 31, 2010 and 2009, reservation payments in the amount of
  $30.8 million and $26.0 million, respectively, were recorded as current liabilities on the consolidated balance
  sheets."* The auditor's "eight held documents" and this row's former "11 bodies / 8 accessions" are the same
  accession/document conflation counted at different depths; neither may be published bare. No value, date or
  adjudication in COR-01 changes — the 2009-12-31 balance was filed, and is now filed **twice over** in lineage
  terms.

So the two $26.0m prints are **different period-ends of one filed series** (2009-12-31 and 2010-03-31), and the
$24.8m is a third period-end (2009-09-30) that **disappears from the lineage after Amendment No. 1**. The
supersession in part 2 remains **DECLINED** — that half of COR-01 is untouched, because a supersession across
different measurement dates is still not a correction. What changes is that `U.23` is re-graded from a value
conflict to a period-end pair, the value is minted as its own `quantitative.csv` row at 2009-12-31, and the
flat 2009-12-31 → 2010-03-31 statement is **carried as supported** in `decisions.csv` row 1 while its causal
reading stays unproven (no gross receipts/refunds flow was ever filed).

**Lands in (as merged):** `conflicts.csv` row `U.23` (new anchor, minted at merge, declared in `stage_1.md` §U
addendum); `quantitative.csv` row "Refundable reservation liability", 2010-03-31; `stage_1.md` Volume 1 §F.2
against Volume 2 §G.4, §J.3, §P.2.

**Lands in (after this repair, 2026-09-30):** `conflicts.csv` row `U.23` re-graded; `quantitative.csv` **new row
2009-12-31 refundable reservation liability $26.0m** plus the repaired tags on the two 2010-03-31 rows;
`decisions.csv` row 1 (`actual_result` re-labelled carried-and-supported); `stage_1.md` merge header, §U anchor
`U.23`, the COR-01 line of the corrections block, and the "Stage-1 repair pass 1" section at its foot;
`stage_1_index.md` §Anchor ranges and decision 5; `_MANIFEST.md`.

**Settling route (FETCH REQUEST, not performed here):** the 424B4 balance-sheet column heads at
`0001193125-10-149105/d424b4.htm` — one read of `sources/sec/0001193125-10-149105_d424b4.htm` for the
reservation-liability line at 2009-12-31 and 2010-03-31 settles it from bytes already on this disk.

**This "FETCH REQUEST" label was itself an error and is retired (2026-09-30 repair).** The route it names is a
**local read** — the sentence it says it would find is in the file whose path the entry prints, and in seven
others. §15.1 reserves fetching for documents a script cannot reach; nothing here needed fetching, and the 0-call
web budget is not a reason a local read went undone. Only the **flow** data (receipts and refunds between the
three period-ends) still needs a fetch, and it stays open in `U.23` and `data_gaps.csv`.

---

## COR-02 — accession `0001193125-10-099603` is Amendment No. 2, not "S-1/A No. 3"

**Withdrawn:** part 1's register title for `S4371` ("S-1/A No. 3 primary document ds1a.htm acc
0001193125-10-099603"), repeated from the probe dossier (`research/sources.csv` `S0003`, "third amendment").

**Basis (all held bytes):** the response letter filed **inside** that accession (`filename13.htm`,
`S4382`) is captioned as the response for Amendment No. 2; the PricewaterhouseCoopers consent at `dex231.htm`
(`S4380`) consents to the use of a report "in this **Amendment No. 4**" and the 2010-06-28 accession captions
itself **AMENDMENT NO. 8**. Ordinals taken from listing order among held amendments produce exactly this
error. **RD-126's rule — take an instrument's date from the filing index, never from a filename or listing
order — extends to ordinal instrument identity**, and part 2 adjudicated it as `conflicts.csv` `U.19`.

**Not a dating change:** the filing date 2010-04-29 is unaffected, and so is the load-bearing finding — this is
the printing in which "one of our founders" first appears. The claim record `P1-12`/`P2-54` is re-labelled, not
re-dated.

**Lands in:** `sources.csv` row `S4371` (and its aliased probe row `S0003`, folded here); `conflicts.csv`
`U.19`; `stage_1.md` Volume 1 §B.2 and Volume 2 §N.3.

---

## COR-03 — "nothing EDGAR-dated 2003–2008" is superseded in form by the 2005–2009 REGDEX band

**Withdrawn:** the probe's §Verdict wording, repeated into its `S0006` register row and its claim record `F10`:
"Nothing EDGAR-dated 2003–2008: earliest submission in the 1,750-filing window slice is Form D **2009-04-09**."

**Measured (`research/A3_intake_regrade.md`, §Index, against `sources/_index/submissions.csv`):** the earliest
in-window row is **Form REGDEX, accession `9999999997-05-006484`, filed 2005-02-17**, and the band runs to
**12 REGDEX/REGDEX/A rows from 2005-02-17 to 2009-01-12**, every one a SEC-generated `9999999997-*` paper
accession with a `.paper` primary document, **none held by either pass**.

**Sustained in substance:** 2003 and 2004 are genuinely empty on CIK 1318605, REGDEX entries carry **no
company-authored narrative**, and the earliest **company-authored** document remains the S-1 of 2010-01-29.
The null is about **content**, not about **rows**; "EDGAR is empty for the first five and a half years" must be
restated as "empty of company documents 2003–2004, then SEC paper registration entries 2005–2009". The
founder-attribution conclusion — one documentary voice, two datable layers — is untouched.

**Lands in:** `sources.csv` row `S4377` (EDGAR submissions slice, which absorbs the probe `S0006`, part 1's
`P1S09`, part 2's `P2S13` and `P2S15`); `stage_1.md` Volume 1 §Header record-selection null and §Boundary.

---

## COR-04 — the contemporaneous-instrument count moved from three to nine; the 2003–2004 silence did not

**Withdrawn:** part 1's §E.2 statement, carried into `U.18` as claim A, that "three held exhibits and only three
are contemporaneous documents of the period they describe".

**Measured on the enlarged intake:** **nine** held instruments plus **five** readable letters dated inside the
window and spanning 2005-07-11 → 2010-06-25 — Lotus glider supply (2005-07-11, `S4373`), Hull lease (2006-08-16
"dated for reference purposes only", `S4388`), Taiway (2007-02-12), Polytec Holden (2007-04-13), Chroma ATE
(2007-04-19) (`S4387`), Stanford lease (2009-08-06, `S4373`), DOE Loan Arrangement and the Midland pledge and
security agreement (both 2010-01-20, `S4379`), plus the counsel, company and underwriter letters of
2010-04-29 → 2010-06-25 (`S4382`–`S4385`, `S4383`).

**Survives intact:** **none of the nine is dated 2003 or 2004**, so part 1's substantive finding — the origin
void between the 2003-07-01 incorporation and the 2004-03/04 role dates — is unharmed by the larger intake, and
the four supply agreements carry confidential-treatment redactions on their face, so the in-window cost base is
**EMPTY by design, not by search failure**.

**Lands in:** `sources.csv` row `S4387`; `conflicts.csv` `U.18`; `stage_1.md` Volume 1 §E.2 and Volume 2 §N.1.

---

## COR-05 — the FY2009 full-year figures ARE in the registration lineage (Amendment No. 1, 2010-03-29)

**Withdrawn:** part 1's quantitative note that "the FY2009 full-year figure is NOT in the S-1, which carries
only 9M2009", and the related note on its XBRL row that FY2009 reaches us only from 2011-vintage periodic
reports.

**Correct:** both statements are true of the **2010-01-29 original printing** and false of the **lineage**.
Amendment No. 1 (`0001193125-10-068933`, 2010-03-29, `S4370`) adds the audited FY2009 statements: `111943`
occurs 0 times in the original S-1 and 5 times there, and `55740` 0 → 8. The FY2009 revenue and net loss are
therefore carried in **registration-lineage** instruments as well as in the XBRL series, and the row that said
otherwise is corrected rather than deleted.

**Consequence for independence:** this does **not** create a second voice. The lineage is one registrant
(§3 filing-lineage rule); what changed is the **date of the earliest carrier** for FY2009 money, which moves
from a 2011 periodic report to a 2010-03-29 amendment — 21 days before the offering.

**Lands in:** `quantitative.csv` row "FY2009 revenue and net loss as reprinted post-IPO" (2009-12-31) and
`timeline.csv` row 2010-03-29; `stage_1.md` Volume 1 §A.3/§D.1 and Volume 2 §J.1.

---

## COR-06 — the held-corpus denominator, measured once so three printed counts stop disagreeing

**Withdrawn as printed:** part 1's "76 documents across 24 accessions"; the re-grade's "76 documents,
59,479,299 bytes … across 28 accessions"; part 2's "85 documents / 33 distinct accessions / 59,900,392 B".

**Measured by this merge on the written bytes** (`sources/sec/`, sidecars and `_MANIFEST.csv`/`_UNANSWERED.csv`
excluded): **83 documents across 32 distinct accessions, 59,881,144 B**. `sources/sec/_MANIFEST.csv` carries
**76 rows across 25 accessions** and omits exactly seven items — the **3 corrupted SEC-staff UPLOAD PDFs**
(`0000000000-10-010920/-019954/-027152`, the text-mode-destroyed bytes at `S4386`) and the **4 CORRESP letters**
(`0001193125-10-135111`, `-145972`, `-145981`, `-147594`, i.e. `S4383`–`S4385`) — which is why the regrade's
`auto` run printed **0 UNANSWERED while leaving 269 in-window index rows at 28 fetched accessions**: "0
UNANSWERED" is not coverage and is not a null for the rest.

**Reconciliation:** 85 (part 2) = 83 documents + `_MANIFEST.csv` + `_UNANSWERED.csv`; 76 = the manifest's own
row count; 24/25/28/32/33 are accession counts taken over different inclusion rules, not different corpora. No
claim in the volume depends on which denominator is quoted, and every register row now names the measured one.

**Settlement debt handed on (not fixed here, reported per §14):** `tools/sec_intake.py` writes binary
documents in text mode (the three PDFs carry 23,268 / 13,489 / 10,637 U+FFFD sequences and yield 0 text from
two extractors; they contain no image objects, so only a binary re-fetch can recover them — they are
**UNANSWERED**, not empty) and its `grab --accession` form without `--file` invents `index-headers.txt` and
404s. Also reported, unfixed: `merge_census.py` cannot attribute a `validation.csv`/`failures.csv` pair
(RD-132), and it globs `_parts/*.md` only, so it never saw the probe's 25 rows.

---

## COR-07 — the register-layer corrections taken on repair pass 1 (2026-09-30, `tesla-repair-1`)

**Withdrawn:** four statements that the registers printed and the held bytes do not. Each is kept visible in the
cell that carried it; none was deleted.

1. **`validation.csv` — "2009-05 | First powertrain shipments to Daimler".** Withdrawn as to its date. The cited
   carrier prints the two acts separately: *"In May 2009, we formalized a development agreement with Daimler as a
   result of which we performed specified research and development services"* and *"We began shipping the first of
   these battery packs and chargers in November 2009 and started to recognize revenue for these sales in the
   quarter ended December 31, 2009."* The row now reads **2009-11**; the May-2009 agreement is recorded inside the
   same row's carrier note rather than as a new row. The volume was already right (claim record `P1-28`,
   `timeline.csv` row 2009-11), so this is a register-vs-volume contradiction resolved **against the register**.
2. **`quantitative.csv` — three rows citing `$0.493` to `S4372`.** Withdrawn. `0.493` occurs **5× in `ds1.htm`
   (S4369), 5× in `-068933_ds1a.htm` (S4370) and 5× in `-099603_ds1a.htm` (S4371)** and **0× in
   `-149105_d424b4.htm`**, which prints Series A at *"valued at $0.49 per share"* and in its preferred table as
   *"Series A $ 0.001 $ 0.49 7,213,000 7,213,000 $ 3,556 $ 3,549 \*"*. The rows are re-pointed to the carriers that
   print their inputs, and both derivations are now stated on their own basis: 8,000,000 × $0.493 = $3,944k against
   the recorded $3,936k (**residual $8k**, S4369 basis) versus 8,000,000 × $0.49 = $3,920k (**residual $16k**,
   S4372 basis). One cell's product was also simply mis-keyed: 15,213,000 × $0.493 = **$7,500,009**, not the
   $7,499,999 printed. Split basis stated in each cell: the common side is 8,000,000 in the January printing and
   2,666,666 in the 424B4 (*"converted 8,000,000 shares of Series A convertible preferred stock to 2,666,666
   shares of common stock"*), the 1-for-3 reverse split effected May 2010, basis registered at `U.13`; preferred-side
   counts are unadjusted by design.
3. **`timeline.csv` — "2003-07-01 -> 2004-05 | no dated corporate act of any kind in the held corpus".** Withdrawn
   as to its range and its absoluteness: three rows of the same register fall inside it (2003-07, 2004-03, 2004-04),
   and `S4369` dates the first — *"Our board of directors adopted, and our stockholders approved our 2003 Equity
   Incentive Plan, or the 2003 Plan, in July 2003"*. The window is narrowed to **2003-08-01 -> 2004-02-29** and the
   "not an inference of inactivity" caveat is preserved.
4. **`sources.csv` `S4369` — "aliased emissions survive here verbatim, nothing dropped"; and `S4390`'s title
   "Wayback CDX rows".** Both withdrawn as overstatements. Measured: the aliased probe rows' `relevant_passage` and
   row notes do survive, but their `source_title` and `independence_note` text occurs **0× in all nine registers**
   (strings tested: "independent of the registrant narrative", "sec registry enumeration", "504 Gateway Time-out",
   "IA Temporarily Offline", "Internet Archive advancedsearch responses"). And `sources/wayback/` holds **no CDX
   response body**: 3 negative HTML artefacts, 1 zero-byte JSON whose 473-byte sidecar records no `http_status`, and
   one answering CDX call that survives only as transcription in `README_retained_capture_evidence.md`.

**Also taken on this pass, as narrow re-labellings rather than retractions:** the EPA row is dated to the penalty's
own month (2010-01) with the certificate date preserved in its note; the Toyota placement cell now states that
$50.0m is the prospectus's **rounded** print while the filed product is **$49,999,992**; the `failures.csv`
memory-layer row is labelled an evidentiary null and the `data_gaps.csv` row it claimed to point at is minted
(the pointer "logged open in data_gaps" had been false); and `failures.csv`'s "twice in ten months" at
2008-02 → 2008-12 is corrected to **thirteen months / 2008-02 -> 2009-03**, matching Volume 2 §O.2(a).

**Two corrections to the auditor's own sheet, recorded because a correction is itself a claim:** (i) audit §A5(iii)
measured "in our target market" as occurring **0× across held bodies** — it occurs **56×** (4× in each prospectus
printing, always about **brand recognition**, never about competition), so the defect stands but its stated basis
does not; (ii) audit §BLOCKER-1 said "$24.8 million occurs 4× in ds1.htm only" ✓ but "printed by **eight held
documents**" counts **accessions** — measured, it is **11 bodies across 8 accessions** *[restated 2026-10-06 by
`tesla-residuals`, B2\*: that 11/8 pair is the **2010 registration lineage only**; the whole of `sources/sec/`
measures **15 bodies across 11 accessions**. The auditor's error is confirmed — it counted accessions and called
them documents — but the replacement figure published here was itself short, and neither number may be quoted
bare. See the COR-01 recount above]*.

**Lands in:** `validation.csv` (Daimler row), `quantitative.csv` (the three per-share rows, the Toyota row, the EPA
row), `timeline.csv` (the narrowed silence row), `failures.csv` (two rows), `data_gaps.csv` (new row),
`sources.csv` (`S4369`, `S4390`), and the "Stage-1 repair pass 1" section of `stage_1.md`.
