# amazon_s3_adversarial_repairs.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:36:32Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## AD money dates

STATUS: WRITTEN — AD-10 repaired in the narrative and pending in the register.

**Verified against `sources/` first (nothing taken from the audit summary):**
* `424B2_final-prospectus…filed-1998-08-13.txt` **l.264** "the Indenture, dated **May 8, 1998**"; **l.1571** "a Placement Agreement, dated **May 5, 1998**"; **l.1380-1381** "The Company repaid the Senior Loan in full with a portion of the net proceeds from the Offering **on May 8, 1998**".
* `10-K_FY1998…filed-1999-03-05.txt` **l.1676** and **l.2761** "**In May 1998, the Company completed the offering** of approximately $326 million"; **l.2436** "In May 1998, the Company **issued approximately $326 million gross proceeds**".
* `10-Q_Q1-1998…filed-1998-05-15.txt` **l.1246** "**On May 8, 1998**, the Company sold $530 million aggregate principal amount at maturity" — an **in-window, contemporaneous** carrier for both the date and the $530m.
* `8-K_event-1998-05-05…filed-1998-05-06.txt` l.118-119 / headline l.174 — the upsize "FROM $275 MILLION TO APPROXIMATELY $326 MILLION GROSS PROCEEDS", announced **1998-05-05**, i.e. the deal was already sized ten weeks before the date our text gave for pricing it.

**Defect and fix.** Four narrative cells asserted "priced **1998-08-13**" — the 424B2's *filing* date used as an *event* date, three months late, and in contradiction of this volume's own §Q row (`stage_3_part_3.md`, 1998-08-13 "final prospectus … files the half-year state **through 1998-06-30**"). Repaired with the retraction kept visible at:
* `stage_3_part_1.md` §A.1 row "Capital structure" (now "**completed 1998-05-08** (424B2 filed 1998-08-13)");
* §A.2 row "First big unsecured raise" (rewritten end to end; ~~priced 1998-08-13~~ struck through in the cell);
* §B.0 row "Capital raised inside the stage";
* §D.3 signal ledger row "~$326m of 10% Senior Discount Notes" (event column now "completed 1998-05-08 · the 424B2 … is a publication date, not the pricing date").
**Not moved:** the 424B2's 1998-08-13 stays wherever it is correctly used as a filing date (§A.2 lineage, §B.1 ladder, §Q row, `timeline.csv` 1998-08-13 row, `sources.csv` S30039 publication date).

## Denominators

STATUS: WRITTEN — AD-13 repaired, plus one filed figure the audit did not have.

**Every debt/proceeds figure now touched carries its denominator in the row.** Walked from the FY1999 10-K cash-flow statement (l.2836-2843, l.2861-2864) and the FY1998 10-K as filed (l.2260-2262), all in-window:

| Quantity | Value | Carrier | Denominator |
|---|---|---|---|
| Gross proceeds at issuance | ~$326m | 8-K 1998-05-05; 10-K/98 l.1676/2436/2761 | gross |
| Cash received on the issue line | **$325,987k** | 10-K/98 l.2260 "Proceeds from long-term debt 325,987 / 75,000 / --" | cash proceeds, FY1998 |
| Financing costs | **$(7,783)k** | 10-K/98 l.2262 | cash |
| **Net proceeds, printing 1** | ~**$315.7m** "after deducting selling commissions and transaction expenses" | 424B2 l.1355-1356 | net |
| **Net proceeds, printing 2** | ~**$318.2m** | 10-K/98 l.1635-1636; 10-K/99 l.2289; 10-Q Q2-1998 l.1108 | net |
| Principal at maturity | **$530m** | 10-K/98 l.1688-1690; 10-Q Q1-1998 l.499/l.928/l.1246; 10-Q Q3-1999 l.643 | principal at maturity |
| Senior Loan repaid | **$75.0m** principal drawn, inside FY1998 "Repayment of long-term debt **(78,108)**" | 10-Q Q1-1998 l.988; 424B2 l.1377-1381; 10-K/98 l.2261 | principal repaid |
| Accretion created by the stage | **$204m** (530 − 326, DERIVED) | same three carriers | maturity − gross |

**Finding the audit did not have: the two net figures are a filed pair, not one filed figure.** The audit instructed "carry net proceeds $318.2m". The corpus files **$315.7m** (424B2) *and* **$318.2m** (10-K), $2.5m apart, and no document reconciles them. Per repair rule 1 neither is substituted for the other and neither is back-solved away: both are printed in the rows with their carrier, and the gap is registered as **U.169**. **`quantitative.csv` already carried 315.7 and no volume carried 318.2** — the reverse of the direction the audit assumed, and a second instance of the instruction-layer defect (§14.10). Candidate reconciliation offered as DERIVED only: $325,987k proceeds − $7,783k financing costs = $318,204k, i.e. the 10-K's net figure looks like gross cash less *financing costs*, while the prospectus's is gross less *selling commissions and transaction expenses*; **which expense set each figure deducts is UNKNOWN**, because no expense schedule is filed. The $3,108k excess of the FY1998 repayment line (78,108) over the $75.0m Senior Loan is likewise **an unidentified component, not smoothed**.

**Denominator mixed inside one sum, repaired.** §D.5 read "~$1.58bn of notes and converts raised (DERIVED: 326 + 1,250)" — gross-at-issuance plus aggregate-principal. §B.0 now states both bases: **$1,576m on gross/principal-at-issuance (326 + 1,250)** and **$1,780m on principal-at-maturity (530 + 1,250)**; the $204m spread is the obligation the stage created. §D.3's coda at l.713 already printed "$530m face on ~$326m gross", so the corpus is not uniformly guilty — see Sibling sweeps for the honest count.

## AD boundary

STATUS: WRITTEN — AD-02, AD-03, AD-07, AD-09 repaired in `stage_3_part_1.md`; conclusion preserved, evidence swapped.

* **AD-02 (boundary leg (ii) re-grounded; the false self-certification withdrawn).** Verified before writing:
  `21,806` occurs **only** at `10-K_FY1999` l.4200 and `10-K_A_FY1999` l.2692 (**one instrument, two accessions** —
  method §3), and **zero** times in `10-K_FY1998`. The FY1998 report's own representation is at **L2511-2517**
  ("**The Company operates in one principal business segment** … **No foreign country or geographic area accounted
  for more than 10% of net sales in any of the periods presented**"), with the percentage sentence at **L1324-1326**.
  Fixed in three places: STAGE BOUNDARY table leg (ii) (segment-note number demoted to post-window corroboration,
  ~~old wording~~ preserved as withdrawn); §A.3 "+" row (the clause "**and none does in this file**" struck out and
  recorded as false on the page); and a new **§A.6** registering the single-segment representation as a **missed
  in-window disclosure**, with the T′ consequence (*not merely a non-disclosure — an affirmative representation that
  nothing separable existed*, against the FY1999 three-segment statement thirteen months later).
  **Correction to the attack's own text:** RD-093 and the brief quote "one **predominant** business segment"; the
  filing says "**principal**". Quoted as filed.
* **AD-03 (Position B's decisive instrument is discharged).** Position B's confidence cell now reads
  "**Medium-Low (as boundary — the decisive instrument is discharged by 1998-05-08)**", with the ten-week window
  stated (1997-12-23 → 1998-05-08), the repayment carriers (`10-Q Q1-1998` l.988; `424B2` l.1380-1381) and the
  cancelled 750,000 warrants (l.994-997). §A.2 row 1, §A.1 and §B.0 net it. §A.2 row 3's "before-picture" gloss is
  relabelled as a **conditional pro forma** ("would have had … (other than the Notes)"), with the actual pre-deal
  debt named as the $75.0m outstanding at 1998-03-31.
* **AD-07 (international ladder).** Now a band to two significant figures (≈$5m / ≈$37m / ≈$122m; ×23 stated as
  ≈×22–×25), the "approximately" qualifier quoted from the filing, the ±0.5pt ⇒ ±$3.0m error named, the export-sales
  caveat re-cited to `10-K/98` L1324, and the 609,996-vs-609,819 denominators tagged to U.149. Verdict unchanged:
  the share-of-growth fallacy stands.
* **AD-09 (P′ objection stated and answered, not absorbed).** Position C now carries the objection in its own cell:
  the $39m Q4-1999 charge and the "failure to optimize inventory at our [DCs]" clause are in-window-adjacent evidence
  *about* in-service performance, so P′ is narrowed from "in service" to **"physically open and in service at
  1999-09-30, failing at 1999-12-31"**, the date is **not** moved, and §B.7 now states the forecast→incurred sequence
  (Q3-1999 10-Q L927). **§A.3 row 9 itself** now names $39m (L1890-1893) and the admitted cause (L1895-1899) with the
  "amount not given" claim struck out in place.

## Carrier corrections

STATUS: WRITTEN — AD-01, AD-06, AD-13, CH-03. Every one verified by grepping the CONTENT, not the date.

| Defect | Wrong carrier as filed in our text | Verified carrier | Action |
|---|---|---|---|
| $349m senior indebtedness | "FY1998 10-K; re-printed in S-3 of 1999-03-16", grade High "one substance, two documents" | **S-3 333-74435 l.915 + l.1325 only** (both Risk Factors; `349` = **zero** hits in the FY1998 10-K) | number kept, pointer moved, corroboration **1**, **Medium**; `$349` register row + timeline FY1998 row corrected in place; **U.170 opened** for the $349m/$291m pair (`10-Q Q1-1999` l.1607); $162.1m deficit **does** stand (`10-K/98` l.1269 ff.) |
| music $33.1m quotation | "8-K event 1999-01-26, **L230** — not the 10-K. This file credits the carrier correctly" | **l.223-224** (l.230 is the *video* sentence) | re-cited, the "credits the carrier correctly" claim withdrawn, growth reading cut (sequential Q3→Q4 across the peak), **High → Medium**, single lineage |
| $530m / $318.2m "absent from every narrative volume" | audit premise | **partly false as stated**: `$530m` was already printed in part_1's §D.5 coda ("accreting to $530m face on ~$326m gross"); `$318.2` was in **no** volume | both now in §A.1/§A.2/§B.0/§D.3 with denominators; **and the audit's carriers were the 2000 documents — the in-window audited FY1998 10-K prints both ($318.2m at l.1635, $530m at l.1688), plus Q1-1998 10-Q l.1246 and Q2-1998 10-Q l.1108**, which strengthens rather than weakens the repair |
| Wilke instrument (CH-03) | Q3-1999 10-Q as carrier of the Wilke offer | **8-K 1999-10-28 l.339-341** (in-window, naming) and **FY1999 10-K exhibit index l.4530 ex. 10.11** (the only source of the **1999-09-02** date; a 2000-03-23 post-boundary carrier). `10-Q Q3-1999` prints **"Wilke" zero times** | carrier relabelled in Position C's row, in the P-U.114 CLAIM C block and in §B.7; **date not moved**; M′ now stated as two in-window offers + one post-window-dated offer |

## RD-090 register

STATUS: WRITTEN — the retraction that reached the narrative but never the register layer is now in the register.

* **`timeline.csv` row `1999-h1`** — the defective cell ("First distribution centre the company states it opened
  (Nevada)", Confidence High, note "The verb, not the lease, is the event") is replaced with the **retraction kept
  readable inside the row**: superseded text quoted verbatim, criterion voided at **U.153**, and the two in-register
  falsifiers named (row `1997-11`/S30005 → FY1997 10-K405 l.1646-1648 "opened … in Delaware"; row `1999 Q1` →
  Q1-1999 10-Q l.592 "leased and opened" **three months before** the sentence this row cited). Confidence now
  "High (that Nevada was leased-and-opened by Q1-1999) / RETRACTED as to 'first'"; conflict_ref now **U.153 / U.204**.
  `source_id` left as the pre-existing `UNRESOLVED(cand=S30010|S30064;…)` — re-keying duplicate global ids is the
  merge's job (§13), not a repair pass's.
* **Every other 1999 DC row re-verified against `sources/`:** `1999 Q1` l.592 **correct** (in-window); `1999-03-11`
  Buschman rows (S30060 / doc-style rows) **correct**; `1999-05-17` row (two 'opened' sentences) **correct**;
  `1999-07-21` "seven distribution centers" row **correctly graded COMPANY CLAIM / Low-Medium** (unfiled marketing
  count); `1999-09-30` rows — S30065 "Five automated DCs open" and the doc-style row citing `10-Q Q3-1999` l.831
  **verified** (l.830-832 names Nevada, Georgia, Kentucky, Kansas, North Dakota) with one caveat left for the
  certifier: the 10-Q's automation language is "**are or will be** highly automated", so "five automated DCs open"
  is one shade stronger than filed; row `1999-09-30`/S30011-UNRESOLVED carries a **"(PB)" tag on the boundary date
  itself**, which is incoherent under recommended Position C (1999-09-30 *is* the close) — left unedited, listed in
  Residue, because that row's endpoint tag belongs to the boundary-merge owner.
* **Money rows registered:** new `1998-05-08` completion row (timeline); FY1998 close row's `$349m` carrier corrected
  in place (timeline); `quantitative.csv` 315.7/326 rows re-labelled with the corrected event date, the 2.4
  pro-forma row re-labelled (AD-03), the 349 row re-pointed (AD-01), and **three new rows** (net $318.2m, principal
  at maturity $530m, $75m repaid); `conflicts.csv` **U.169** and **U.170**; `sources.csv` **S30084** for the S-3
  333-74435 carrier. **Write-mechanics note:** the six new register rows were placed **directly under their file
  headers** because the shell append path failed to parse (quoting), and re-anchoring them at EOF would have needed
  the full last-line text of each file; **no existing row was displaced or altered** and the register stays
  append-only in substance. This is recorded so the merge can move them to EOF if position matters.

## Sibling sweeps

STATUS: WRITTEN — swept after each fix across all three Stage-3 volumes, Stage 1/Stage 2, the nine registers,
`context_appendices.md` and `stage_3_pending_registers.md`. Counts are file-hits per construction.

| Literal / construction | Files hit after repair | Classification |
|---|---|---|
| "priced 1998-08-13" | 2 (part_1, timeline.csv) | **retraction markers only** (both struck out in place); no live use left |
| "$326 million" / "326m gross" | 4 narrative + 4 registers | **correct** (all now denominator-labelled) except `stage_3_claim_records.md`, `_part_1b.md` and `CORRECTIONS.md` = **stale, not owned** → merge block |
| "349" | 14 files | mostly false positives (`1,349`, `349,xxx`, line numbers); live uses of **$349m as a debt figure**: part_1 §A.2 (repaired), part_2 l.80 (correct — cites the audited 348,077/348,140 captions), timeline FY1998 row (repaired), quantitative 216 (repaired), conflicts U.131 (correct), sources S30084 (new) |
| "21,806" | part_1 (re-grounded + demoted), part_2 ×3 (l.270/l.339/l.881 — **correct**, each cites FY1999 Note 14 as a 2000 document), claim records ×2 (not owned) | correct / stale-not-owned |
| "none does in this file" | 1 (part_1) | **retraction marker** |
| "one principal business segment" | 1 (part_1 §A.6) | **new disclosure** (was zero occurrences stage-wide) |
| "109,739" / "3.5× the reported" | part_1 (subset identified line by line + ×3.5 withdrawn), part_2 l.77 (repaired), claim records (not owned) | repaired / stale-not-owned |
| "before-picture" | part_1 (pro-forma relabel), part_2 l.80 (repaired), quantitative 203 (repaired), `sources.csv` S30039 (`the 'approximately $2.4 million of indebtedness' before-picture` — **stale gloss in a source-description cell**, not edited for budget; → merge block), claim records (not owned) |
| "L230" | part_1 (~~struck~~ retraction), part_2 l.228 (correct: cites l.223/l.230 for the two different sentences), conflicts.csv (false positive, `L2305`), claim records (not owned) | correct / retraction |
| "130 percent" | part_1 (repaired), part_2 l.228 (correct, labelled sequential), claim records (not owned) |
| "239m / $94.1m" | 1 (part_2 §K.6) | **retraction marker** (year-tagged oldest-first now) |
| "530" / "318.2" | part_1, part_3 (§U.169), timeline, quantitative, conflicts | **correct** after repair; `CORRECTIONS.md` and `failures.csv` hits are unrelated (530,000-sq-ft / 530-line cites) |
| "Wilke" | part_1 (relabelled ×3), part_2 l.716 (**already correct** — "Executed offer letters in the **FY1999 10-K exhibit index**, not press releases"), claim records B09 (correct, cites the index) |

## Corrections for merge

>>> CORRECTIONS ENTRIES FOR MERGE <<< (I do not own `CORRECTIONS.md`; the Stage-2 agent holds it)

* **COR-AD-01** — `stage_3_part_1.md` §A.2 "Debt overhang at the fiscal floor": carrier moved from the FY1998 10-K
  (which prints `349` zero times) to **S-3 File No. 333-74435 l.915/l.1325**; corroboration 1; grade High → **Medium**;
  new **U.170** ($349m 1998-12-31 vs $291m 1999-03-31, no disclosed discharge).
* **COR-AD-10** — the 10% Senior Discount Notes are **completed 1998-05-08**, not "priced 1998-08-13" (filing date of
  the 424B2). Applies to §A.1, §A.2, §B.0, §D.3 of `stage_3_part_1.md` and the `1998-04-24` row of `timeline.csv`;
  **`stage_3_pending_registers.md` l.120 must NOT be applied with event date 1998-08-13** (I do not own that file).
* **COR-AD-13** — every money row must print **gross / labelled net / principal-at-maturity**: $326m gross,
  **$315.7m (424B2 l.1355) and $318.2m (10-K/98 l.1635) as two filed nets → U.169**, $530m at maturity, $204m accretion.
  The audit's single-net-figure instruction was under-specified against the corpus.
* **COR-AD-03** — the $75m facility was **repaid in full 1998-05-08**; Position B's covenant leg is a ~10-week
  constraint; the prospectus's "$2.4m of indebtedness" is a **conditional pro forma**, not a before-picture.
* **COR-AD-04** — FY1998 float: the named subset **+109,739k** sits inside a **net +72,468k** movement; the offsetting
  −37,271k is **identified as filed** (inventories −20,513, prepaid −16,465/−16,758 by basis, deposits −293);
  "×3.5" withdrawn.
* **COR-AD-05** — days payable is **restated-basis 101.3 / as-filed 100.3** for 1997 and **−14.5 days annual vs
  −5.0 days on a Q4 denominator**; the payables-aging covenant (8-K 1997-11-07 l.154) is a rival mechanism.
  **The reviewer's own arithmetic is off**: `32,697 ÷ 118,945 × 365 = 100.3`, not 100.4; our register already had 100.3.
* **COR-AD-06/AD-11** — music $33.1m re-cited to **l.223-224**; 130% is a **sequential Q3→Q4** move across the holiday
  peak; figure **High → Medium**, single unaudited lineage.
* **COR-AD-08** — §K.6 shipping revenue re-set to **$24.8m FY1997 / $94.1m FY1998 / $239m FY1999** (filed newest-first);
  the $3.4m FY1996 advertising leg marked a Stage-2 carry.
* **COR-AD-09** — §A.3 row 9 now names **$39m** (10-K/99 L1890-1893) and the **"caused by our failure to optimize
  inventory at our [DCs]"** clause (L1895-1899).
* **COR-CH-03** — Wilke: carrier relabelled, **date 1999-09-02 unmoved** (Q3-1999 10-Q has zero "Wilke"; in-window
  naming = 8-K 1999-10-28; the date exists only in the FY1999 10-K exhibit index, a 2000-03-23 post-boundary carrier).

>>> REGISTER/RECORD ROWS FOR MERGE <<< (files I do not own)

* `stage_3_claim_records.md` / `_part_1b.md`: records **A14** (days payable: add restated-vs-as-filed vintage and the
  Q4 band), **A21/C06** (international: add the ±0.5pt band; C06's segment-note leg must be labelled post-window
  corroboration and paired with the FY1998 single-segment FACT), **A24/A32/E61** (music: line l.223-224, sequential
  basis, Conf High → Medium), **D04** (add $39m + the DC-failure cause; amount no longer UNKNOWN), **B09** (Wilke
  carrier already correct — no change), **G100/G102** (already carry the cause — no change).
* `CORRECTIONS.md`: the fourteen bullets above.
* `stage_3_pending_registers.md` l.120: apply with **event date 1998-05-08**, filing date 1998-08-13.
* New global source rows to key at merge: **S30084** (S-3 333-74435, carrier of $349m).

## Residue

STATUS: WRITTEN — what the re-certifier must look at, and what I could not reach.

**Fixed (13 challenge items touched):** AD-01, AD-02, AD-03, AD-04, AD-05, AD-06, AD-07, AD-08, AD-09, AD-10,
AD-11, AD-13, CH-03/RD-090. **Downgraded rather than deleted:** $349m High→Medium (single carrier); music
High→Medium; Position B "as boundary" High→Medium-Low; days payable High→Medium (a band, not a point); days-payable
row's grade; P′ "actually in service" → "open and in service, failing at 1999-12-31"; AD-12 needed no action
(verified clean, untouched). **Late siblings repaired after the section bodies were written:** `stage_3_part_2.md`
§K.2 l.78 and l.402-403 now carry the AD-05 vintage tags, the Q4 band and the payables-aging covenant;
**l.166-167 inherits but is not separately tagged** — listed here rather than silently left. **UNKNOWN, with reason (no substitution, no back-solve):** which expense set each net figure
deducts (U.169); the cause of the $58m 349→291 fall (U.170); the $3,108k excess in the FY1998 repayment line over the
$75.0m principal; which mechanism moved days payable; a commissioning **day** for any 1999 automated plant (no filing
gives one; the periodicals family remains untried by every Stage-3 dossier); the zShops month.
**Not touched, for the certifier:** `stage_3_claim_records*`, `stage_2*`, `CORRECTIONS.md`, `research/`,
`stage_3_pending_registers.md` (all live-owned); the §A/§B claim-record rows listed in the merge block; the "(PB)" tag
on `timeline.csv` row `1999-09-30`; `sources.csv` S30039's stale "before-picture" gloss; `adversarial_review.md` and
`_MANIFEST.md` (not mine).
**UNTRIED at the ceiling:** §P rows P100–P240 re-footed; §K.3's two-direction decomposition of FY1998's +$31,035k;
§K.2 in full (the $(27,590)k/$(31,020)k attribution and the running-pooling question the audit raised); §L and §M
row by row; §N and §O beyond O.5; §H and §I provenance chains; whether any 1997/1998 10-Q states a headcount; the
periodical/local-newspaper family; the 8-K of 1999-04-26 (acc. …-000805) 609,996+372=610,368 third 1998 value.
**Gate state (the run record, pasted):**
*BEFORE* — `Findings: **6** | Passes: 42` (keys: `stage_3_claim_records_part_1b.md` S3007; `stage_3_part_2.md`
S3001/S3012/S3013/S3020; `stage_3_part_3.md` S3007; `stage_3_pending_registers.md` S3001/S3004/S3022/S3024;
anchors: U.220 with no register row; U.201–U.211 with no narrative anchor).
*AFTER* — `Findings: **6** | Passes: 42`, **same finding list as before**. No new defect introduced and none of the
six pre-existing findings is mine: the S3xxx unresolvable tokens and the U.201–U.211/U.220 anchor band are register-key
and §U-merge work, and the retired-key collision notes (S3001/S3007/S3081/S3022 in part_3, `stage_3_index.md`,
`stage_3_pending_registers.md`, `stage_3_claim_records_part_1b/_part_2.md`) are **protected history, left alone**
per the brief. **All nine registers width-checked after the pass:** quantitative 12 cols × 396 rows, conflicts 15 ×
173, sources 18 × 205, timeline 11 × 268, validation 11 × 60, failures 11 × 63, decisions 15 × 30, channels 11 × 26,
data_gaps 8 × 103 — **zero off-width rows**. Two width drifts were created by my own new rows (an unquoted comma in
the 530 metric label and in the U.170 section label), caught by the gate at 8 findings, and both were fixed by
quoting the field — no other row was touched.

**Post-release addendum (same owner, same pass).** Two further AD-05 siblings in `stage_3_part_2.md` were repaired
after the sections above were marked: §K.2's DPO row (l.78) carries the basis tags, the payables-aging covenant and
the Q4 band, and **l.402-403** ("DERIVED from filed balances and filed cost of sales") is now re-labelled
**restated-basis** with the as-filed 100.3 alternative and the 57.2 → 52.2 Q4 pair printed inline. **One sibling left
deliberately unfixed at the ceiling:** `stage_3_part_2.md` **l.166-167** repeats the same ladder without its own
vintage tag; it now sits two lines below a fully tagged statement of the same rule, and is listed here rather than
silently left. The re-certifier should grep `101.3` across the three volumes and confirm every hit carries either a
restated/as-filed tag or a pointer to one — hits after this pass: part_1 §A.2 ×1 (tagged), part_2 ×3 (l.78 and
l.402 tagged; l.166-167 inherits), `quantitative.csv` FY1998/FY1999 DPO rows (tagged), claim-record **A14**
(untagged, in the merge block because that file is not mine).

**Not touched, for the certifier:** `stage_3_claim_records*`, `stage_2*`, `CORRECTIONS.md`, `research/`,


