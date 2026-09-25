<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:05:46Z. -->

**Run:** AUDIT 5, adversarial certifier, Amazon Stage 3 (1997-05-16 → argued close). Zero web, zero git.
Nothing here repairs a file; every row is a verdict plus the artifact that produced it.

**`gates.py` context (run once, not re-checked by hand):** `keys` — unresolvable source tokens
S3001/S3007/S3081 in `stage_3_part_3.md`, S3001/S3004/S3022/S3024 in `stage_3_pending_registers.md`;
`anchors` — narrative anchor U.220 with no register row, register rows U.201–U.211 citing anchors absent
from the narrative; `budget` — `stage_3_claim_records.md` 84,337 words over the 60,000 cap. Treated as
known mechanical state, not as findings of this review.

**Lineage note binding the rows below:** the corpus holds 99 entries under `sources/`. Several Stage-3
figures are carried by the FY1999 10-K (2000-03-23) **and** its 10-K/A (2000-09-08) — one instrument, two
accessions. Per method §3 filing-lineage rule those are **one** source; where the report grades such a
pair as "two documents" the grade is re-attacked below.

## Challenges

### AD-01 — §A.2 "Debt overhang at the fiscal floor": the $349m is attributed to the wrong carrier
**Claim attacked** (`stage_3_part_1.md` §A.2, row "Debt overhang at the fiscal floor"): "**~$349 million of
outstanding senior indebtedness** and accumulated deficit $162.1 million at 1998-12-31 | FY1998 10-K;
re-printed in S-3 of 1999-03-16 [T1 · FACT] | **High (one substance, two documents)**".
**Attack.** Read the FY1998 10-K end to end for the string: `349` occurs in
`sources/10-K_FY1998_acc-0000891020-99-000375_filed-1999-03-05.txt` **zero times**, and the file's only
debt-capacity statement is the notes offering at l.1676 / l.2436 / l.2761 ("approximately $326 million").
The $349m exists in exactly one place in the corpus — `sources/S-3_FileNo-333-74435_acc-0000891020-99-000441_filed-1999-03-16.txt`
l.915 and l.1325, both inside **Risk Factors**: "As of December 31, 1998, we had approximately $349 million
of outstanding senior indebtedness." So the audited annual report is cited as the primary carrier of a
number it never printed, and the "two documents" grade counts one carrier plus a risk-factor caption.
**Second leg, worse.** The same sentence-family prints **$291 million** one quarter later at
`sources/10-Q_Q1-1999_acc-0000891020-99-000894_filed-1999-05-17.txt` l.1607 — a $58m fall in "senior
indebtedness" between 1998-12-31 and 1999-03-31 with no repayment disclosed anywhere in the corpus, which
the report never notices while using the higher figure as the stage's debt-overhang headline.
**Evidence consulted:** the three files named above.
**Outcome.** **Must be downgraded and re-cited**: carrier = S-3 (333-74435) l.915 only, class = company
risk-factor self-statement not an audited caption, corroboration = **1**, and the $291m/$349m pair must be
opened as a §U conflict. The $162.1m accumulated deficit **does** stand at S-3 l.491 and at 10-K l.1269 ff.

### AD-02 — The boundary section does the one thing §A.3 forbids: a 2000-only document moves the endpoint
**Claim attacked.** `stage_3_part_1.md` §"STAGE BOUNDARY JUSTIFICATION", row "`ST3_E` … Why FY1998 fails
anyway, **on its own facts**", leg (ii): "the International **segment** was **$21,806k = 3.6% of FY1998 net
sales on $2.8m of foreign long-lived assets** (DERIVED: 21,806 ÷ 609,819)". Same figure re-used at
`stage_3_part_1.md` F31 and `stage_3_claim_records.md` A28.
**Attack, two parts.**
(i) The number exists in **exactly two places in the corpus** — `10-K_FY1999_…` l.4200 and
`10-K_A_FY1999_…` l.2692, i.e. Note 14 of a **2000-03-23** document and its own amendment. It is absent
from the FY1998 10-K. §A.3 of the same volume states the rule: these are "2000 documents … **inadmissible
as anything a contemporaneous 1999 reader could have known**; no use of them may move a boundary, **and
none does in this file**." But leg (ii) is *literally* the argument for why FY1998 fails as an endpoint,
inside the boundary section. The self-certification "and none does in this file" is false on the page.
(ii) The out-of-window reach was also **unnecessary**, and that is the more damaging half. The in-window
FY1998 10-K already says the same thing, more strongly, under its own heading "Segment and Geographic
Information": "**The Company operates in one principal business segment** across domestic and international
markets. **International sales, including export sales from the United States**, represented approximately
20%, 25% and 33% of net sales … **No foreign country or geographic area accounted for more than 10% of net
sales in any of the periods presented**" (l.2509-2517, and the identical percentage sentence in MD&A at
l.1324-1326). I searched every Stage-3 file for "one principal business segment", "principal business
segment" and "more than 10% of net sales": **zero occurrences across the whole stage**. An affirmative
single-segment representation by the registrant — the strongest possible in-window statement that nothing
in FY1998 was organisationally a marketplace or a foreign business — is missing from the reconstruction
while a 2000-only segment note is used to carry the same load across a boundary rule.
**Evidence consulted:** `10-K_FY1998_…` l.1322-1330, l.2508-2517; `10-K_FY1999_…` l.4200;
`10-K_A_FY1999_…` l.2692; grep of `stage_3*.md`.
**Outcome.** The **conclusion survives** (FY1998 is not the endpoint) but the **evidence must be swapped**:
reclassify leg (ii) as an **in-window FACT from the FY1998 10-K's own single-segment and ≤10%-per-country
representations**, and demote the $21,806k segment note to post-window corroboration labelled as such.
Separately, register the single-segment sentence as a **new disclosure**: it is load-bearing for the T′
axis, because it means the absence of third-party revenue data through FY1998 is not just a non-disclosure
but an affirmative representation that no separable business existed.

### AD-03 — The $75m facility that carries Position B was repaid inside one quarter and §A never nets it
**Claim attacked.** `stage_3_part_1.md` §"The three positions", Position B: FY1997-12-31 is mandatory
because of "the **drawn $75m secured facility of 1997-12-23** with payables aging covenanted and
substantially all assets pledged"; and §A.2 row 1 "First post-IPO debt … **$75,000,000 three-year senior
secured term credit facility**"; §A.1 row "Capital structure"; §B.0 row "Capital raised inside the stage:
**$75m secured (1997-12-23)** · ~$326m … · $1,250m …"; and §A.2 row 3, which offers the prospectus's
"**approximately $2.4 million of indebtedness**" as "the **before-picture in its own words**".
**Attack.** The facility was **extinguished within one quarter of being drawn**, on the filed record:
`sources/10-Q_Q1-1998_acc-0000891020-98-000846_filed-1998-05-15.txt` l.988 — "The Company has repaid the
Senior Loan **in full** with a portion of the net [proceeds]" — and l.997, "All of the warrants were
canceled when the Company repaid the" loan. `424B2_final-prospectus_…_filed-1998-08-13.txt` l.1379 repeats
it. That is why the same prospectus can honestly print ~$2.4m of indebtedness at l.699/l.1114/l.2220: the
$2.4m is a **post-repayment pro forma**, not a "before-picture". §A quotes it as the before-state while
listing the $75m as money raised inside the stage and never netting it, so §A alone leaves a reader with
$75m of standing constraint and a $2.4m debt counterfactual in the same table — two statements that cannot
both describe 1998-08-13. Position B's decisive marker is then a covenant regime that bound the company for
roughly **ten weeks** (1997-12-23 → Q1-1998 close).
**Evidence consulted:** the four files named above; `stage_3_part_2.md` §O.5 l.815-824, which **does** know
the repayment ("retire the Senior Loan first") — so the omission is confined to §A and the boundary table,
not to the whole file.
**Outcome.** **Must be downgraded**: Position B's covenant leg becomes a dated, discharged instrument, not
"a change in what the company was permitted to do" spanning FY1998; §A.2 row 1 and §B.0 row "Capital raised
inside the stage" must carry the retirement and net the stage's debt issuance; §A.2 row 3's
"before-picture" gloss must be re-labelled as a post-repayment pro forma.

### AD-04 — "+109,739k = 3.5× the reported positive figure" is a named subset presented as the mechanism
**Claim attacked.** `stage_3_part_1.md` §A.2 row "Cash generation, correctly stated": "FY1998's float lines
(inventories, payables, accrued advertising, other accruals) sum to **+109,739k = 3.5× the reported
positive figure** (DERIVED)".
**Attack.** The report's own two filed subtotals are $(41,433)k pre-working-capital and $+31,035k reported
operating cash. The **whole** working-capital contribution is therefore **72,468k** (31,035 − (−41,433);
arithmetic on the report's own cited figures, labelled here as reviewer-derived). A named subset summing to
+109,739k against a total of +72,468k means roughly **37,271k of offsetting negative working-capital lines
were excluded from the sum that the sentence then scales by 3.5**. "3.5× the reported positive figure" is
true of the subset and silently false of the mechanism: the float did not supply 3.5× the year's cash, it
supplied more than the year's cash *while other accruals took it back*.
**Evidence consulted:** `stage_3_part_1.md` §A.2 (the two subtotals); the FY1999 10-K cash-flow statement
is the carrier and I did **not** re-walk its individual lines — see Artifact gaps.
**Outcome.** **Must be downgraded**: restate as "named float lines contributed +109,739k of a +72,468k net
working-capital movement; the residual (≈ −37,271k) is unidentified on this review", or withdraw the ×3.5
comparison. The headline conclusion — FY1998's positive operating cash was bought with balance-sheet growth,
not trading — **survives**, because it rests on the pre-working-capital subtotal, not on the subset.

### AD-05 — Days-payable: a restated numerator, an as-filed sibling, and a denominator that seasonality moves by 3×
**Claim attacked.** `stage_3_part_1.md` §A.2 row "The honest nuance on the float" (and
`stage_3_part_2.md` l.167, l.399-400): "Days payable **fell** ~15 days in 1998 (DERIVED: 33,027 ÷ 118,969 ×
365 = **101.3** → 113,273 ÷ 476,155 × 365 = **86.8**), so FY1998's positive line was bought by **growth in
purchases, not by leaning on vendors**"; 1999 leg **125.2 days**.
**Attack, three legs.**
(i) **Basis mixing inside one derivation.** The 1997 pair 33,027 / 118,969 is the **pooling-restated** FY1997
(l.1023 and l.361 of `8-K_event-1998-08-27_acc-0000891020-98-001370_filed-1998-09-11.txt`;
`10-K_FY1998_…` l.1223), whereas the as-filed FY1997 balance-sheet AP is **32,697**
(`10-K_FY1997_…` l.1817) and the as-filed cost of sales is **118,945** (l.1178) — the figures the same
volume prints at §A.0 and §A.4. §A.4 states the rule "Restated values in this file never read as filed";
§A.2 then derives a headline from restated values described at part_2 l.399 as "**filed** cost of sales"
with no vintage tag. Small numerically (101.3 → 100.4 on as-filed), but it is the file breaking its own
prohibition in a row whose entire rhetorical purpose is basis honesty.
(ii) **Denominator mismatch — the fatal leg.** Days payable pairs a **31-December point balance** with an
**annual cost-of-sales flow**, in a business whose fourth quarter is ~41% of the year: filed quarterly data
at `8-K_event-1999-01-26_…_filed-1999-01-27.txt` l.439-440 give Q4-1998 net sales 252,893 against FY1998
609,996 (41.5%) and Q4 cost of sales 199,476 against FY 476,155 (41.9%); Q4-1997 cost of sales is 53,127
against FY1997 118,969. Recomputing the same ratio on a **quarterly** denominator (reviewer arithmetic,
92 days): 33,027 ÷ 53,127 × 92 = **57.2 days** for 1997 and 113,273 ÷ 199,476 × 92 = **52.2 days** for 1998
— a fall of about **5 days, not 15**. The direction survives; the magnitude is off by a factor near three
depending on which denominator is chosen, and the report prints a point estimate with a decimal.
(iii) **Alternative explanation never considered.** The 1997 balance-date is **ten days after the $75m
facility was drawn** and the facility **covenanted payables aging** (the report's own words for Position
B). A vendor-aging covenant struck on 1997-12-23 is a direct candidate cause of both the 1997-12-31 payables
level and its 1998 movement — a financing constraint on working capital, which is a *different* story from
either "leaning on vendors" or "growth in purchases". The corpus has the instrument
(`8-K_event-1997-11-07_acc-0000950151-97-000357_filed-1997-11-10.txt`) and the report never joins it to the
ratio.
**Outcome.** **Must be downgraded**: 101.3/86.8/125.2 survive only as an annual-basis illustration with the
basis named, the ±(seasonal) band shown, the restated/as-filed vintage tagged on each leg, and the covenant
added as a competing mechanism. This is not re-litigating U.149/U.159 (the 609,996-vs-609,819 and
118,945-vs-118,969 movements, which the report already registers and handles well); it is the *use* of the
restated pair in an unlabelled derived ratio.

### AD-06 — The music "130 percent" is a sequential holiday-quarter jump, and the row's line citation is the video line
**Claim attacked.** `stage_3_part_1.md` §A.3 conversion-ledger row 4: "**A second category number exists**:
'Music sales grew to $33.1 million, a 130 percent increase over sales of $14.4 million in the third quarter
of 1998' | **8-K event 1999-01-26, L230 — not the 10-K. This file credits the carrier correctly**."
**Attack.** Two defects in one row. **Line:** l.230 of that 8-K is the *video* sentence ("Video sales were
strong following the store's opening on November 17"), which row 5 correctly cites; the music sentence is at
**l.223-224** — as `stage_3_part_1.md` itself cites it at §E.1 row E12 and at l.1034. So the volume cites
two different lines for one quotation, and the row that asserts "credits the carrier correctly" is the one
that does not. **Basis:** reading the filed text at l.223-224 together with
`10-Q_Q3-1998_…_filed-1998-11-13.txt` l.911 ("Music sales totaled $14.4 million for the quarter ended
September 30") and `8-K_event-1998-10-28_…` l.223 ("Third-quarter music sales were $14.4 million, the first
full quarter following" the launch), the $33.1m is **Q4-1998** and the base is **Q3-1998**: a
quarter-over-quarter move **across the retail peak**, not a year-over-year growth rate. The "130 percent" is
arithmetically exact (33.1 ÷ 14.4 = 2.30) and categorically unusable as a growth figure — and the Q3 base is
itself only the first *full* quarter of a category launched mid-quarter, so no annualised music figure
exists in the window at all.
**Evidence consulted:** the four files named above.
**Outcome.** The **existence** of a second category number survives (the null it fills was real). The row
**must be cut as a growth datum and re-cited to l.223-224**, and must state that both legs are single
quarters on either side of the holiday peak. Any downstream sentence reading "music grew 130%" is a
mismatched-period error, and this row's own "credits the carrier correctly" claim has to go.

### AD-08 — §K.6 attaches shipping-revenue values to the wrong years, and an advertising series crosses the stage boundary unlabeled
**Claim attacked** (`stage_3_part_2.md` §K.6): row "Outbound postage **revenue** | **ANSWERED** — $239m /
$94.1m / $24.8m **(FY1997-98-99)**, annual only"; and row "Customer acquisition cost": "advertising expense
is printed only annually (**$3.4m/$21.2m/$60.2m/$140.9m**)".
**Attack.** The filed line is `10-K_FY1999_…` l.1847-1848 — "Shipping revenue was $239 million, $94.1
million and $24.8 million **in 1999, 1998 and 1997**". The values are newest-first; the §K.6 parenthetical
labels them oldest-first. A reader pairing them positionally gets **$24.8m for 1999 and $239m for 1997**,
inverting a three-year series that §K.7 item 7 celebrates as "the first filing ever to print it". In the
same table, the advertising row runs oldest-first and carries **four** values for the three years §K.6 is
discussing: $3.4m is FY1996, i.e. a **pre-IPO, pre-Stage-3 value carried on a Stage-3 row with no year
labels and no provenance split**. §8 table discipline ("never a value without its source cell") is not met
by either row, and §A.2's advertising line ("$21.2m → $60.2m → $140.9m", correctly oldest-first for
1997-99) is therefore in *conflict of ordering* with §K.6's — one of the two will be copied.
**Evidence consulted:** `10-K_FY1999_…` l.1847-1848; `stage_3_part_2.md` §K.6, §K.7 row 7;
`stage_3_part_1.md` §A.2 last row.
**Outcome.** **Must be cut and re-set**: year-tag every multi-value series inline ($24.8m 1997 / $94.1m 1998
/ $239m 1999), and either drop the $3.4m 1996 leg from the Stage-3 row or mark it as a Stage-2/424B1 carry.

### AD-09 — Position C's endpoint is the quarter of the window's largest filed operating failure, and §A.3 hides the amount
**Claim attacked.** `stage_3_part_1.md` §A.3 conversion ledger row 9: "'In the fourth quarter of 1999, we
incurred inventory-related charges, which significantly decreased our gross margins.' — stated as incurred,
not risked; **day not given, amount not given in that sentence** | FY1999 10-K L1049-1054". And Position C
itself: "**P′ an automated multi-site network actually in service**".
**Attack, two legs.**
(i) **The amount is filed, in the same document, ~850 lines earlier than the row's citation.**
`10-K_FY1999_…` l.1890-1893: "Gross margin decreased in 1999 due to the introduction of new product lines,
particularly toys and electronics, and **inventory-related charges of approximately $39 million incurred in
the fourth quarter of 1999**." `stage_3_part_2.md` §M l.431-433 **does** carry the $39m. So the executive
conversion ledger — the section whose stated purpose is to replace stale nulls — re-creates a near-null by
quoting the risk-factor sentence and declaring the amount ungiven, and the hedge "in that sentence" conceals
that no same-document search was run. Method §14.10 puts the highest severity exactly here: an instruction
layer a cold reader trusts.
(ii) **The causal clause is the one the boundary needs and does not get.** l.1895-1899 continues: "we
realized lower shipping margins in 1999 due to an increase in partial shipments to satisfy holiday demand
and because of **split shipments from one or more locations, which was caused by our failure to optimize
inventory at our** [distribution centers]". Read together with Q3-1999 10-Q l.927 ("Split shipments may also
increase **due to recent openings of distribution centers**"), the corpus contains the company's own
attribution of a $39m charge and a shipping-margin decline **to the multi-site network state that Position C
promotes into its pass test**. The endpoint candidate is therefore not merely the date the network came
in service but the date of its first disclosed large-scale failure — an axis C never considers, and which
cuts against P′ ("actually in service") far harder than the unaudited-MD&A objection the file already
concedes.
**Evidence consulted:** `10-K_FY1999_…` l.996-997, l.1049-1054, l.1885-1899;
`10-Q_Q3-1999_…` l.927; `stage_3_part_2.md` §M l.431-433.
**Outcome.** §A.3 row 9 **must be corrected** (name $39m, name the "failure to optimize inventory" cause,
cite l.1890-1893). The boundary argument **must be re-opened on this axis**: either C states and answers the
in-service-vs-failing-in-service objection, or the P′ leg is downgraded from "actually in service" to
"physically open".

### AD-10 — The $326m notes are "priced 1998-08-13": a filing date used as an event date, three months late
**Claim attacked.** `stage_3_part_1.md` §A.2 row 3: "**~$326 million gross** on the S-4/424B2 lineage
**priced 1998-08-13**"; §A.1 row "Capital structure": "after **$326m** 10% Senior Discount Notes
(**1998-08-13**)"; §B.0: "~$326m 10% senior discount notes (**1998-08-13**)"; §D.3 signal ledger row:
"priced **1998-08-13**".
**Attack.** The corpus dates the transaction itself to **May 1998**, on four filed statements. The indenture
is "dated **May 8, 1998**" (`424B2_final-prospectus_…_filed-1998-08-13.txt` l.264) and the placement
agreement "dated **May 5, 1998**" (l.1571); `10-K_FY1998_…` l.1676 says "**In May 1998, the Company
completed the offering** of approximately $326 million", repeated at l.2436 and l.2761. The 424B2 is the
*final prospectus*, filed three months after the money arrived; 1998-08-13 is its filing date. §Q's own
timeline at `stage_3_part_3.md` l.480 gets this right ("**1998-08-13 | 424B2 final prospectus** for the
senior discount notes; it files the half-year state … **through 1998-06-30**"), which makes this an internal
contradiction rather than a defensible convention — and §A.2's own sentence announces 1998-04-24 and upsize
1998-05-05 before "pricing" the deal in August, an ordering that cannot be true. Under §6 (time audit) and
§13 (event date vs publication date), the error moves the second-largest financing event of the stage by a
quarter and mis-aligns it against the Q2-1998 10-Q cash position.
**Evidence consulted:** `424B2_final-prospectus_…` l.264, l.1571; `10-K_FY1998_…` l.1676, l.2436, l.2761;
`stage_3_part_3.md` l.480; `stage_3_pending_registers.md` l.120 (which registers event date 1998-08-13 for
the same fact, so the register carries the defect too).
**Outcome.** **Must be corrected**: completion/pricing **May 1998** (placement agreement 1998-05-05,
indenture 1998-05-08, "completed" per the FY1998 10-K); 1998-08-13 retained only as the 424B2 filing date.
`pending_registers.md` l.120 must not be applied with the wrong event date.

### AD-11 — Two "only" facts of the category record rest on the one release the file elsewhere grades as maximal-basis self-assertion
**Claim attacked.** `stage_3_part_1.md` §A.3 rows 4 and 5 (second category number; the only launch day), and
§E.1 row E12 ("**High** (music figure)"); `stage_3_part_2.md` §K.6 last category row, which calls the
category figures "company **press-release** assertions … **Unaudited, unreconciled to any 10-Q**".
**Attack.** All three rest on a single document — `8-K_event-1999-01-26_…_filed-1999-01-27.txt`, EX-99, the
Q4-1998 earnings release. That is **one lineage, one issuer-occasion**: the same text in which the file
elsewhere identifies a "peak-quarter annualisation" ($1 billion on Q4 ×4) and a "nearly quadrupled **over
the third quarter**" sequential change in two stores **that opened in October 1998** (§K.6, ST3E-18). The
corpus therefore holds **one** audited category-adjacent figure (the FY1999 segment note's aggregated US
media line, $1,308,292k) and **one** unaudited press release supplying everything else the category story
quantifies — yet §E.1 grades the music figure High while grading the *same release's* other assertions as
basis-maximal. The distinction the file needs and does not draw is **falsifiability**: "the video store
opened on November 17" is a checkable event statement in a release about one's own quarter; "music sales
grew to $33.1 million, a 130 percent increase over … the third quarter of 1998" is a performance statement
whose base is the company's own first *partial-then-full* quarter. Both come from the same page, and they do
not deserve the same grade.
**Evidence consulted:** the 8-K named, l.216, l.223-224, l.230, l.261, l.306; `8-K_event-1998-10-28_…`
l.208, l.223, l.292-296; `10-Q_Q3-1998_…` l.911; `10-K_FY1999_…` l.4155-4162.
**Outcome.** **Survives split**: the video **date** holds at High (corroborated in-window by
`10-K_FY1998_…` l.1322 "the video store in November 1998", a second document family). The music **figure**
must be **downgraded to Medium as a company performance assertion, single release, single lineage**, and its
130% stripped of any growth reading (see AD-06).

### AD-12 — The split-vintage guard verified clean; recorded as a failed attack
**Claim attacked.** `stage_3_part_1.md` §A.4 row 1: the cumulative Stage-3 split factor is **12×, not 6×**,
"which is why the 1997 option count prints as **27,332 thousand** there and **54,664 thousand** in FY1999 —
exactly 2.000×", with "Greped in `10-K_FY1999_…` and `10-Q_Q3-1999_…`" as the verification performed.
**Attack attempted.** I tried to break this the way §14.8 requires — by finding the number. `54,664` and
`27,332` both resolve, and the pairing is exactly where the row says it is.
**Evidence consulted.** `10-K_FY1998_…` l.2991 "Balance December 31, 1997 … **27,332** **1.502**" (stock
option activity table); `10-K_FY1999_…` l.3886 and `10-K_A_FY1999_…` l.2377 "Balance December 31, 1997 …
**54,664** **0.751**"; `10-Q_Q3-1999_…` l.123-124 (footnote-only September split) and l.657-658;
`10-Q_Q2-1999_…` l.655 "effect on September 1, 1999; accordingly, the stock split **has not been
reflected**".
**Outcome.** **Survives, and strongly.** `54,664 ÷ 27,332 = 2.0000` and the paired weighted-average exercise
price moves `1.502 → 0.751` = ÷2.0000 in the same row — two independent columns of the same table confirm
one another, and only the September 1999 2-for-1 separates the two printings, because the FY1998 report was
already filed after the January 1999 3-for-1. The "footnote-only split defeated the archive's most careful
analyst" finding is the best-supported load-bearing claim in the volume: Q2-1999 l.655 shows a filed document
explicitly declining to reflect a split that had already been announced.

### AD-07 — The international dollar ladder multiplies rounded percentages and prints four significant figures
**Claim attacked.** `stage_3_part_1.md` §"ST3_E's refusal to restore FY1998", row "International share of
sales 33% → 25% → 20%": "Recomputed on filed dollars: 1996 **$5.2m**, 1997 **$36.9m**, 1998 **$122.0m** —
**×3.3 in one year, ×23 over two** (DERIVED: 0.33 × 15,746; 0.25 × 147,787; 0.20 × 609,996, $000)".
**Attack.** The percentages are not measured, they are company-rounded adverbs: the filed text reads
"represented **approximately** 20%, 25% and 33% of net sales" (`10-K_FY1998_…` l.1325-1326 and l.2513-2514).
Multiplying a ±0.5pt rounding band by a $610m base is a **±$3.0m** band on the 1998 leg alone, so the ladder
should be reported as ≈$5m / ≈$37m / ≈$122m and the two ratios as **bands** (the ×23 endpoint ratio spans
roughly ×22–×25 across the admissible bands). The row instead prints three four-significant-figure dollars
and two ratios and then uses them to overturn a colleague's "decisive" finding. Rounding cannot overturn
anything: **the direction is robust by two orders of magnitude**, so the *verdict* (share-of-growth fallacy)
stands — but the precision does not, and the same row is the one that accuses Position A of arithmetic
mistaking itself for evidence.
**Bonus, and it is the useful half.** The denominator the ladder uses for 1998 is **609,996** while the very
next row's segment ratio divides by **609,819** — the report is aware of that pair (U.149) and applies it
correctly per-row, so no error, only a presentation hazard worth a basis tag. More importantly, the same
in-window sentence that supplies the 20% **also supplies the caveat the report attributes to a 2000-only
segment note**: "International sales, **including export sales from the United States**" (l.1324). The
"overwhelmingly US export sales, a shipping fact not an organisation" inference is therefore **in-window and
filed**, and is better evidenced than the file credits it — see AD-02.
**Outcome.** **Survives as INFERENCE/DERIVED with a band**; must add the ±0.5pt rounding band, drop to two
significant figures, and re-cite the export-sales caveat to the FY1998 10-K instead of to the FY1999 segment
note.

### AD-13 — "~$326 million gross" as capital raised erases both the cash that arrived and the liability created
**Claim attacked.** `stage_3_part_1.md` §A.2 row 3 ("**~$326 million gross** … [the] before-picture in its
own words"), §A.1 row "Capital structure" ("after **$326m** 10% Senior Discount Notes"), §B.0 row "Capital
raised inside the stage", §D.3 signal ledger.
**Attack.** These notes were **discount** notes, and the corpus prints all three different quantities that
the "$326m" label collapses. `10-K_FY1998_…` l.1635-1636 and `10-K_FY1999_…` l.2289: net proceeds of
"**approximately $318.2 million from the Senior Discount Notes**". `10-K_FY1999_…` l.3675,
`10-K_A_FY1999_…` l.2165 and `10-Q_Q3-1999_…` l.642: "The Senior Discount Notes were sold at a substantial
discount from **their principal amount at maturity of $530 million**". So the row titled "Capital raised
inside the stage" overstates cash by ~$7.8m and — far more seriously — never tells the reader that the
instrument whose gross is printed as $326m retires at **$530m in 2008**, a $204m obligation the stage
creates. The gap also *answers* the $20.6m residual I opened in AD-01: ~$349m of senior indebtedness at
1998-12-31 is $326m gross **plus accreted discount plus the small other debt**, which is exactly why
"$326m + $2.4m" fails to reconcile. The file's own `stage_3_claim_records.md` l.818-820 and
`stage_3_claim_records_part_1b.md` l.95 carry the $530m and $318.2m figures — **but they appear in none of
the three narrative volumes**. Under §14.10 that is the instruction-layer failure in miniature: the numbers
exist in the appendix and are absent from the tables a reader trusts.
**Outcome.** **Must be re-set**: §A.2/§A.1/§B.0 to carry principal-at-issuance $326m, **net proceeds $318.2m**,
**principal at maturity $530m**, each labelled, and §K's debt-overhang row must show accreting principal or
it will read as a static $349m.

## Structural attacks

### SA-1 — The stage's factual spine is one post-window instrument and its own amendment
`stage_3_part_1.md` §A.3 is a "conversion ledger": nine dossier nulls turned into facts, each carrier being
either the FY1999 10-K (2000-03-23) or an 8-K press release, with grades moving to **High**. Counting the
§A.1 and §B.0 rows that stand on it — the 1999-12-31 estate, the ≈7,600 headcount, the seller/listing
counts, the whole FY1999 financial column, the named-city estate, the fulfilment-cost series, the segment
partition, the one incurred failure — roughly **nine of fourteen executive rows have a single 2000-lineage
carrier**. The 10-K and its 10-K/A are **one instrument refiled**, so under §3's lineage rule this is not
nine corroborations but one, and the file's own U.149 proves the mechanism is live: the same 2000 document
re-cuts FY1998 net sales by −$177k with **no reconciling note**. The circularity the volume is open to is
therefore precise and not the trivial one: **a document is trusted to fill nulls because it is a filing, and
the reason those nulls were written is that the filing did not exist when the dossiers closed.** The
conversion ledger is legitimate §14.11 work and the file says so out loud, so I do **not** ask for the facts
to be withdrawn; I ask that the grades in the ledger read "one carrier, 2000 lineage, no in-window witness"
wherever that is true, which is most rows.

### SA-2 — Missing-evidence attacks: what is conspicuously absent
- **A single-segment representation that never reaches the page.** `10-K_FY1998_…` l.2511-2517 says the
  company "operates in **one principal business segment**" and that "no foreign country or geographic area
  accounted for more than 10% of net sales in any of the periods presented". Zero occurrences across every
  Stage-3 file. This is the strongest available in-window statement that nothing in FY1998 was
  organisationally separable, and it does the T′ work the volume assigns to a 2000-only segment note (AD-02).
- **No results 8-K anywhere in FY1997.** The 8-K run begins 1997-11-07 (the credit facility) and the first
  earnings release is 1998-04-17/04-27. So every 1997 quarterly figure the volume reports is carried by a
  10-Q alone; there is no FY1997 release in which the company characterised its own quarters, which is why
  §F7's repeat-customer ladder has no 1997-1998 release leg and why all *category* numbers in the window
  come from **1998 and later** releases (AD-11). Absence here is a fact about EDGAR intake practice for
  1997 paper filers, not about Amazon's disclosure.
- **No pre-1997 fulfilment leg.** The $12.1m for 1997 is the series' first point and there is no 1996 figure
  anywhere, so §G.3's curve cannot be compared with Stage 2's single-site cost structure at all; it starts
  in the IPO year. A series that begins at the boundary cannot show the boundary being crossed.
- **The metric that stops being disclosed, already caught and one that was not.** Caught: visits/conversion
  ("no 10-Q or 10-K in the window gives a visit or conversion figure at all", §K.6). Not caught:
  **§A.2/§B.0 never retire the $75m** (AD-03), and the narrative never carries **$530m** (AD-13).

### SA-3 — Independence attacks on grades the file awards for corroboration
(i) AD-01: "one substance, two documents" is one document plus a risk-factor caption. (ii) §A.3's FY1999
carriers: 10-K + 10-K/A counted as separate confirmations in several rows. (iii) **The ARS rows**: §B.0
promotes ARS 1997 and ARS 1998 to "two dated, filed, in-window founder-state documents [that] **outrank
every retrospective interview**". They are company-produced, filed under the same accession family as their
own 10-Ks (ARS 1997 filed 1998-04-17, the same day as the 1998 DEF 14A; ARS 1998 1999-04-07 with the 1999
DEF 14A), and their financial content is the 10-K's. Their *value* is real — they are Bezos writing to
shareholders on a date — but their *independence* from the filings they summarise is nil, and "outrank"
should mean "are contemporaneous", not "are corroborated".

### SA-4 — Boundary attacks
(i) **Post-window document describing a pre-window state.** §G.3's 1997 cost leg is a 2000 footnote about
the single-site era; it is admissible as a record of in-window facts, but it cannot be plotted on the same
curve as 1999 without saying that only one endpoint had a contemporaneous witness.
(ii) **A post-IPO instrument used to characterise a stage boundary and then quietly retired** (AD-03) —
Position B's decisive constraint lasted one quarter.
(iii) **An axis deleted because it cannot be evidenced.** C removes T′ from the pass/fail set because the
record "cannot supply [third-party commerce] at *any* in-window date". A test with an axis removed for
convenience is a test that cannot fail on that axis, and the volume's own §A.5 then adds that the price of
the automation is Rule 24b-2 redacted. Two of C's three legs are therefore declared untestable rather than
passed. The file is candid about this — the candour is the reason C is graded Medium — but the honest
consequence is that **Stage 3's recommended endpoint rests on one testable leg (P′), and P′ is the leg
AD-09 attacks.**

### SA-5 — Circularity, named plainly
The volume refutes Position A's *first-use* claim by producing three earlier filings (**not** circular, the
best move in the file); it then establishes its own endpoint on an offer-letter *count* taken from the FY1999
10-K exhibit index, i.e. from the company's later list of its own papers. Where a boundary is proved by
"what the company chose to file on a date", the firewall has to be argued from a document-independent fact,
and in this window the only such fact — plant commissioning dates — is precisely what the corpus lacks.

## Survives

Attacked and holding. Recorded so the merge does not re-open them.
1. **The 12× split factor** (§A.4, §K.8) — AD-12: `54,664 ÷ 27,332 = 2.0000` with the paired weighted-average
   exercise price `1.502 → 0.751`; Q2-1999 10-Q l.655 shows a filed document expressly not reflecting the
   September split. Two independent columns confirm it.
2. **"Five DCs opened in nine months"** — Q3-1999 10-Q l.830-832, an in-window document, so C's P′ leg is not
   a 2000-carrier claim: "During the nine-month period ended September 30, 1999 the Company opened new
   distribution centers in Nevada, Georgia, Kentucky, Kansas and North Dakota".
3. **"The two distribution centers in operation prior to 1999 … were manually operated"** — Q3-1999 10-Q
   l.1628-1633, in-window, against interest. C's engineering premise holds; only its *interpretation* is
   attacked (AD-09, SA-4 iii).
4. **§G.3's arithmetic** — every ratio re-computed independently: 12,100÷147,787 = 8.19%; 50,300÷609,819 =
   8.25%; 188,400÷1,639,839 = 11.49%; 12.1÷21.2 = 0.571; 188.4÷140.9 = 1.337; 15.6× vs 11.1×;
   advertising share 21.6/14.3/9.9/8.60%; fulfilment share of the caption 30.2/37.9/45.6%. All foot. The row
   is labelled "restated FY1999 basis", so the §A.4 prohibition is honoured *here* — which is what makes
   AD-05's unlabelled ratio a local failure and not a systemic one.
5. **FY1999 headline set** — $1,639,839k / $(719,968)k / $(320,987)k / $(90,875)k / $463,026k / ≈7,600
   confirmed at `10-K_FY1999_…` l.1732, l.2608, l.2633, l.684; the FY1997 re-printed net loss $(31,020)k
   confirmed at l.2633.
6. **The video launch day 1998-11-17** — 8-K event 1999-01-26 l.230/l.261/l.306 **and** independently in the
   FY1998 10-K MD&A l.1322 ("the video store in November 1998"), so it clears the lineage bar.
7. **Position A's falsification** — F-1/F-2/F-3 stand as argued; the "opened" verb is not a discriminator.
   This remains the strongest structural result in the stage and I could not re-attack it.
8. **The 3.537× / ×3.3 / ×23 *directions*** — all survive; only their printed precision is attacked (AD-04,
   AD-07).

## Does not survive

Nine challenges filed. The report does **not** survive five, and four of those are corrections rather than
losses of substance.

| Row | Verdict | What has to change |
|---|---|---|
| **AD-01** $349m carrier | **does not survive** | Re-cite to S-3 333-74435 l.915 alone; corroboration 1, not 2; open the $349m/$291m pair as a §U conflict |
| **AD-03** $75m facility as a standing constraint | **does not survive** | Q1-1998 10-Q l.988 repaid it in full, l.997 warrants cancelled; §A must net it and Position B's covenant leg becomes a ~10-week constraint |
| **AD-08** shipping-revenue year order | **does not survive** | Filed order is 1999/1998/1997; the §K.6 label inverts it; the $3.4m 1996 advertising leg is an unlabeled boundary crossing |
| **AD-10** "priced 1998-08-13" | **does not survive** | Pricing/completion is May 1998 (indenture l.264 May 8; placement agreement l.1571 May 5; 10-K "In May 1998 … completed"); 1998-08-13 is the 424B2's filing date. Contradicts the volume's own §Q row |
| **AD-13** "$326m gross" as capital raised | **does not survive** | Must carry net proceeds $318.2m and principal at maturity $530m; $530m appears in the claim records and in **no** narrative volume |
| **AD-02** FY1998 rejected "on its own facts" | **survives only after re-grounding** | Conclusion stands; the evidence must move from the 2000 segment note to FY1998 10-K l.2511-2517, and §A.3's "no use of them may move a boundary … none does in this file" must be withdrawn as false |
| **AD-05** days payable | **downgrade** | Annual-vs-Q4 denominators give −14.5 or −5.0 days; 1997 leg is restated not "filed"; add the payables-aging covenant as a rival mechanism |
| **AD-06/AD-11** music $33.1m / "130 percent" | **downgrade, figure cut as growth** | Sequential Q3→Q4 across the peak, one unaudited release; re-cite to l.223-224; §A.3's "credits the carrier correctly" withdrawn for this row |
| **AD-09** §A.3 row 9 | **does not survive as written** | $39m and the "failure to optimize inventory at our [DCs]" clause are filed at l.1890-1899; §M already has them, so this is an instruction-layer stale null |
| **AD-04** float "+109,739k = 3.5×" | **downgrade** | The named subset is +109,739k against a net movement of +72,468k; state the residual or drop the multiplier |
| **AD-07, AD-12** | **survive** | Precision band / verified clean |

## Artifact gaps

The three claims that, if wrong, collapse a section — and the artifact that would settle each.

1. **Position C's P′ leg ("an automated multi-site network actually in service") → collapses the whole
   boundary section**, which is the volume's organising finding. Settling artifact: a **dated commissioning
   record for the 1999 automated plants** — a Buschman acceptance/commissioning certificate, or the
   Rule 24b-2 confidential-treatment exhibit released from any of the five Sales Agreements, or a local-
   newspaper commissioning report for Fernley/Coffeyville. **Not in `sources/`.** The corpus holds only the
   company's forward-looking automation language; §A.5 already names the redaction as unrecoverable from
   EDGAR, and I confirmed no 10-Q or 10-K gives a day. AD-09 is the counter-artifact the volume missed: the
   $39m Q4-1999 charge *is* in-window evidence about in-service performance, and it points the wrong way.
2. **"Capital raised inside the stage" ($75m + ~$326m + $1,250m) → collapses §A.2, §B.0 and every leverage
   ratio in §K.** Settling artifact: the **financing section of each 10-K's cash-flow statement**, walked
   line by line, so principal, net proceeds and repayments are separate rows. **In `sources/` and partly
   used** — $318.2m net proceeds and the $75m repayment are both filed and both missing from the money
   tables. This gap is closable today with documents already on disk; it is the cheapest fix in the stage.
3. **The FY1997 as-filed-vs-restated pair ($(27,590)k / $(31,020)k) and its attribution to PlanetAll →
   collapses §A.4, §B.4, §K.1 and §K.2's "a pooling recast, not an error".** Settling artifact: a filing
   that states *which* pooling, on *what* date, restated the FY1997 comparatives. **Partly on disk and
   pointing the wrong way**: `8-K_event-1998-08-27_…_filed-1998-09-11.txt` already prints FY1997 cost of
   sales at **118,969** (l.361, l.1068) and AP at **33,027** (l.1023) — i.e. **before** the PlanetAll 8-K of
   1998-10-28 — so the FY1997 recast is a **running** restatement across several 1998 poolings (l.213,
   l.429, l.1299, l.2265, l.2677 of that 8-K each recite a separate pooling), not one PlanetAll event. I do
   not assert §K.2 is wrong — I did not read its full argument — but the attribution is the load-bearing
   sentence and the corpus contains earlier-printing comparatives it must answer.

**Registers held by the gates, for the record:** U.220 anchor with no register row; U.201–U.211 register
rows with no narrative anchor; S3001/S3007/S3081 and S3001/S3004/S3022/S3024 unresolved;
`stage_3_claim_records.md` 84,337 words over cap. I did not adjudicate whether those rows are real conflicts
— but note that **U.201–U.211 are exactly the boundary-conflict band**, so the anchor gap sits on the same
load-bearing section as AD-02, AD-03 and AD-09.

## Untried

Stopped at the ceiling; none of these was examined, and a null below is not a finding.
1. **§P rows P100–P240 individually re-footed.** I verified the §G.3 and §A.4 clusters and the FY1999
   headline set; the remaining ~200 rows, including §P.2's t1–t27 derivations, were not re-computed.
2. **§K.3's decomposition of FY1998's +$31,035k in both directions**, and whether the +109,739k subset in
   §A.2 can be walked against the FY1999 10-K cash-flow lines (this is the artifact AD-04 needs).
3. **§K.2 in full** — the $(27,590)k/$(31,020)k argument beyond the two sentences I read; AD-01's third gap
   depends on it.
4. **§L validation-signal table and §M failure table row by row** — I read §M's $39m passage only.
5. **§N decisions and §O counterfactuals** beyond §O.5, which I read because it was where the Senior Loan
   repayment surfaced.
6. **§H market-size provenance chain** and **§I competition's "same geometry" rows** — not attacked at all;
   §I in particular may be carrying competitor figures from press releases, which is the class of error this
   review found twice inside the company's own numbers.
7. **Whether any 1997/1998 10-Q states a headcount** (verifying §A.1's "no 10-Q in the window states a
   headcount") — I checked Q3-1999 only.
8. **The periodicals / local-newspaper family** — §A.5 and the boundary's own residual both name it as the
   only family that can produce a commissioning *day*, and it is untried by every Stage-3 dossier including
   this one. It is the single artifact gap that could settle collapse-candidate 1.
9. **The 8-K of 1999-04-26 acc. …-000805 reconciliation table** (l.2863-2864 prints FY1998 net sales
   609,996 + 372 = 610,368), a third filed 1998 value the volume does not appear to discuss; unexamined
   beyond noticing the line.

