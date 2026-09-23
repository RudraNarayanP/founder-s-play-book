# Audit Sheet — Amazon (company_001_amazon) · Stage 1 · AUDIT 3 (Numbers) · Run 2026-09-23
Auditor: Level-3 Numbers Auditor (independent of producer: **yes** — this agent wrote no part of `stage_1.md` or the CSVs)
Scope as briefed: `stage_1.md` §P (incl. §P.2) and §R for cross-foot; `quantitative.csv` (all 105 data rows);
secondarily the numeric cells of `timeline.csv`, `validation.csv`, `failures.csv`, `channels.csv`, `decisions.csv`,
`data_gaps.csv`, `sources.csv`. **`context_appendices.md` NOT audited** (concurrent edit by another agent).
**`conflicts.csv` NOT in the brief and not audited** except where its U-refs were already quoted in §P — coverage note.
Repairs were **not** applied: defect register → `01_companies/company_001_amazon/_parts/NUMBER_DEFECTS.md`.

Reference primaries re-read this pass (`.../company_001_amazon/sources/`): S-1 (orig.)
acc. 0000891618-97-001309 (1997-03-24); S-1/A No. 3 acc. 0000891020-97-000755; S-1/A No. 5 acc.
0000891020-97-000839 (1997-05-14); 10-K405 FY1997 acc. 0000891020-98-000448 (1998-03-30).

| Audit | Result | Items checked | Failures found | Actions taken | Residual risk |
|---|---|---|---|---|---|
| 3 Numbers | **FAIL** (repairs required; no figure in the report was edited by this auditor) | 64 §P rows + 24 §P.2 derivations + 8 §R snapshot rows + 105 `quantitative.csv` rows (15 of them `stage2-consequence`) + 169 numeric cells across the six secondary CSVs + 14 filing verifications | **31 defect rows: 9 HIGH · 15 MEDIUM · 7 LOW** | Per-check findings below; every derivation recomputed and printed; 5 new cross-foots recovered from the audited statements (2 of them retire a declared UNKNOWN); defects registered for the repair pass | The register cannot be signed COMPLETE until the 9 HIGH rows are repaired and the two recoverable figures (in-window round split; 1995 share count) are entered |

---

## CHECK 1 — BASIS — **FAIL (9 unlabeled / mislabeled bases; the spine's basis statements hold)**

Verified correct: §P's header basis block (net sales = shipment basis, net of discounts, **including outbound S&H**,
never GMV/bookings/orders) is the filing's own definition — S-1 (orig.) l.1433–1435 *"Net sales are comprised of
the selling price of books and other merchandise sold by the Company, net of returns, as well as outbound shipping
and handling charges"*; "visits (not 'hits')" ✓ l.450; titles *advertised* ≠ sourceable ≠ stocked ✓; audited vs
company-self-measured vs third-party-estimate classes kept apart ✓; company-vs-segment is a non-issue (Amazon
reported one segment; no segment figure appears anywhere) ✓; nominal-vs-adjusted: every money row is nominal
pre-2000 dollars and 17 `quantitative.csv` rows say so explicitly ✓.

**Fiscal-vs-calendar — the protocol's own premise is wrong, and the dataset is right.** `AUDIT_PROTOCOLS.md`
AUDIT 3.1 tells the auditor to note "Amazon's Nov–Oct fiscal year pre-1996 and calendar switch after". No such
change exists in the four primaries: EDGAR header `FISCAL YEAR END: 1231` in the original S-1 (l.44), No. 3
(l.44), No. 5 (l.44) and the 10-K405 (l.45); 10-K405 Item 6 columns are `YEARS ENDED DECEMBER 31 / 1997 1996
1995` plus `FOR THE PERIOD FROM JULY 5, 1994 (INCEPTION) TO DECEMBER 31, 1994` (l.1163–1186); the only
"references herein to 'fiscal year'" definition in the 1998 file is a credit-agreement cross-reference
(l.4375), not a period change. §P's statement — FY = calendar, **except** the 179-day 1994 stub — is therefore
**correct**; no dataset row is infected by the protocol's Nov–Oct premise. The 1995 "fiscal" nuance that *does*
matter is the Subchapter S → C election at 1995-03-31, which the register handles (P12, §R Capital) ✓.
**Action: report the false premise to the orchestrator (protocol text, not dataset).**

Basis defects:
1. **`quantitative.csv` r7 / `timeline.csv` r11 / §Q l.903 — 4,800,000 option-plan reserve carries a 1994-09-15
   date with no basis label.** The reserve foots to the *1997* restated option population: 3,052,974 outstanding
   + 110,640 available + 1,636,386 exercised = **4,800,000 exactly** (S-1 orig. l.2707–2711), i.e. the printed
   figure is post-4:1-and-3:2, not the 1994 as-adopted reserve (÷6 → 800,000).
2. Same rows: **"a $0.1717 floor strike"** is not a plan term. The filing gives only an observed range — *"exercise
   prices ranging from $0.1717 to $4.00 per share"* (l.2709) — as of 1997-02-28; director grants are separately
   required to be *"not less than the fair market value"* (l.3874). A 1997 observation is labelled as 1994 plan
   architecture.
3. **`quantitative.csv` r66 cumulative capex 80,000 = 28 + 52** is a **cash-paid** sum (Purchases of equipment)
   compared implicitly with the **accrual** gross equipment cost of 81,000 (Note 2, l.3797–3803). The $1,000 gap
   is a basis difference (and rounding in thousands); neither row says so.
4. **P22 / `quantitative.csv` r36 trading period.** Value "≈5.5 months" against its own stated span
   `1995-07-01 → 1995-12-31`, which is 184 days = **6.0 months**; `decisions.csv` r12 says "~26-week trading
   year" (= 6.0 months) while §R says "≈5.5 months" in five rows. One quantity, two values, no derivation.
5. **§R l.965 "~$21,000 average net sales per trading week (DERIVED)"** — basis-dependent: 511,000 ÷ (5.5 × 4.345
   weeks) = $21,383, but 511,000 ÷ (184/7) = $19,440. No arithmetic in §P.2, no `quantitative.csv` row.
6. **P60 / `quantitative.csv` r97 ">$16,000,000 cumulative"** — unit cell "USD" without the basis: this is
   *cumulative net sales through 1996-12-31 on the same ship basis* (orig. l.447–448 *"Through December 31, 1996,
   Amazon.com had sales of more than $16 million"*), not GMV and not a period's revenue. Ties to audited: FY1994
   0 + FY1995 511 + FY1996 15,746 = 16,257 → ">$16 million" ✓ (cross-foot passes).
7. **P49 / `quantitative.csv` r80** numerator is ship-basis revenue *including outbound S&H*; denominator is IDC's
   *"total value of goods and services purchased over the Web"* (orig. l.1772–1774). The row flags the
   denominator's geography but not the numerator/denominator mismatch.
8. **P50 unit cell "counts"** for `50 states / >45 countries` — these are markets-served counts, not customers,
   orders or accounts; the metric label says "geographic reach claimed" but the unit field invites the customer
   reading the row elsewhere warns against.
9. **P30 / `quantitative.csv` r49 EPS $(0.02)** labelled "split-restated share basis" ✓, but the 10-K405's same-year
   $(0.02) is on a **different** base and is captioned *"Pro forma basic and diluted loss per share"* over
   **14,394** thousand shares (l.1191–1194) versus the S-1's **18,780** thousand (orig. l.3505–1322). Two
   denominators, one value cell, no note.

## CHECK 2 — PROVENANCE — **FAIL (5 mis-attributions/wrong nulls; COR-14.1 and COR-12 rows pass)**

Passes verified line-by-line:
- **COR-14.1 (P60/P61 re-keyed to the original S-1) is correctly executed.** The December-1996 trio is
  original-only — orig. l.447–450 *"Through December 31, 1996 … more than $16 million to approximately 180,000
  customer accounts … Average daily visits (not "hits") have grown from approximately 2,200 in December 1995 to
  approximately 50,000 in December 1996"*; No. 3 l.334–337 and No. 5 l.336–339 carry the superseding
  March-1997 trio ($32 million / 340,000 accounts / 80,000 visits) ✓. And **`151` occurs zero times in No. 3 and
  No. 5** (literal `\b151\b` search returned no hits in either file) while orig. l.667 reads *"…from January 1,
  1996 to December 31, 1996, the Company expanded from 11 to 151 employees"* and l.2364 *"As of December 31,
  1996, the Company employed 151 full-time employees."*
- **The employee rows are not in conflict and are not reconciled anywhere.** 11 at 1995-12-31 (No. 3 l.797, No. 5
  l.796 *"From December 31, 1995 to March 31, 1997, the Company expanded from 11 to 256 employees"*), the same 11
  at 1996-01-01 in the original (corroboration), 151 at 1996-12-31, 158 at 1996-12-31 (10-K405 l.729 — Item 1's
  *Management of Potential Growth*, **not** Item 6: cite the location), 256 at 1997-03-31. **No row collapses any
  two of them**; `quantitative.csv` r71 and r96 state the rule and §R l.948 follows it ✓ COR-12 satisfied.
  The 10-K405 does disclose no 1995 headcount (only l.516 *614 full-time employees* at 1997-12-31) ✓ struck as a
  co-source correctly.
- COR-11.1 ✓ ($511k cited to the S-1, not Sheff); COR-10 ✓ ($1,007,000 / 23 / $0.3333 quoted verbatim,
  orig. l.4301–4302 *"aggregate of 3,021,000 shares of Common Stock to 23 investors for a consideration of
  approximately $.3333 per share, or an aggregate of $1,007,000"*; No. 5 l.4663 reads "23 purchasers" — the
  register keeps both wordings); COR-14.2 ✓ (string `245,572` appears nowhere as a figure; §A l.23–25 and §P.2
  d23 carry the rejection); COR-09 ✓ (2,300% / 16-July / $12,000–$14,000 / $50,000-each / ~$5M-20% / parental
  $150,000–$250,000 / Bulgaria / Post stake / money-back guarantee all appear only in retired-claim or legend
  context, with the required nulls).
- Contemporaneous vs retrospective tagging: audited 1994-95 figures filed in 1997 are tagged `RETROSPECTIVE
  SOURCE describing an in-window state` ✓ (r8, r37, §R, timeline r42).

Provenance defects:
1. **`quantitative.csv` r83's null is false.** "no share count and no valuation" — the audited balance sheet files
   *"Issued and outstanding shares — **14,555,244** and 15,900,237 at December 31, 1995 and 1996"* (orig.
   l.3455–3457) and *"As of February 28, 1997, there were 17,008,158 shares"* (l.2978). The Stage-1 share count at
   the boundary is **evidenced and missing from §P entirely**; the *valuation* conclusion may stay UNKNOWN.
2. **An in-window priced issuance exists in every version and is in no row.** Item 5 ¶3 (orig. l.4293–4295; No. 5
   l.4656–4658): *"On August 7, 1995, the registrant issued 42,000 shares of Common Stock to one investor
   [No. 5: "who is an employee"] for a consideration of approximately $.1287 per share, or an aggregate of
   $5,408."* This is a **third 1995 price point below the February price**, so `quantitative.csv` r28's note "Two
   private sales at two prices inside one year" and `timeline.csv` r39's "second and third internal price points"
   are wrong counts, and the residual-investigator's frame in d8 never sees a fully disclosed $5,408 component.
3. **The residual's stated composition is contradicted by the audited statement of stockholders' equity.** d8,
   `quantitative.csv` r31/r33 and `data_gaps.csv` r11 all say the CY1995 line "commingles share sales, option
   exercises and advances", making option money an excuse for the unnamed residual. The equity statement (orig.
   l.3555–3573) prices 1995 option exercises at **$—**: *Sale of common stock … 4,235,244 shares … 1,122*;
   *Advances received for common stock … 150*; *Exercise of common stock options … 120,000 … —*. So CY1995 equity
   cash = $1,122,000 of share sales + $150,000 of advances for shares not yet issued, and no option cash at all.
4. **§P03 vs `quantitative.csv` r4 cite different versions for the same 10,200,000.** Both statements are in both
   versions (orig. l.2848 Certain Transactions and l.4280; No. 5 l.3078/4642), so this is a completeness
   asymmetry, not an error — but the CSV's 1997-05-14-only citation for a figure that exists on 1997-03-24
   understates the corroboration and invites a future re-key.
5. **§R l.947 "not CEO until May 1996"** is right (10-K405 Item 10 dates the CEO title from May 1996), but the
   S-1's own Certain Transactions sentence calls him *"the President, Chief Executive Officer and Chairman of the
   Board"* while describing the July 1994 purchase (orig. l.2847–2849). The row must cite the Item 10 officer
   table, not the S-1 spine, or a future auditor will read the two as a conflict.

## CHECK 3 — ARITHMETIC — **FAIL (3 wrong results, 1 inverted note; 21 of 24 derivations recompute clean)**

Recomputed every `derived_arithmetic` cell (24 §P.2 items + 22 CSV derivations + the §R pair). Verbatim results:

| id | stated | recomputed | verdict |
|---|---|---|---|
| d1 | 10,000 ÷ 1,700,000 = $0.005882 | 0.0058824 | **PASS** |
| d2 | 10,000 ÷ 10,200,000 = $0.00098; "differ by a factor of exactly 6 = 4:1 × 3:2" | 0.00098039; 10,200,000 ÷ 1,700,000 = 6.000 | **PASS** |
| d3 | 5 Jul → 31 Dec 1994 = 26+31+30+31+30+31 = 179 | sum = 179 ✓ (inclusive-of-inception reading = 180; convention unstated) | **PASS** (LOW note) |
| d4 | 582,528 × 0.1717 = **$100,019.06** | **$100,020.0576** | **FAIL — wrong by exactly $1.00** |
| d5 | 847,716 × 0.1717 = $145,552.83 | $145,552.8372 | PASS (cent truncation, LOW) |
| d6 | (0.3333 − 0.1717) ÷ 0.1717 = +94.1% | 0.94118 → +94.1% (on the filing's exact ⅓ price: +95.2%) | **PASS** (sensitivity unstated) |
| d7 | 100,019 + 145,553 + 49,995 = $295,567 "(dossier rounding: $295,568)" | corrected inputs sum to **$295,567.89 → $295,568** | **FAIL — the note is inverted: $295,568 is the accurate value, $295,567 the artifact of d4** |
| d8 | 1,272,000 − 295,568 = $976,432 | 976,432 | **PASS** as arithmetic (see Checks 1/6 on precision and composition) |
| d9 | 102 ÷ 511 = 19.96% | 19.961% | PASS |
| d10 | 200 + 171 + 35 = 406, tying to the filed total | 406 = filed `Total operating expenses 406` (orig. l.3497–3499) | **PASS + tie confirmed** |
| d11 | 304 ÷ 511 = $0.595 | 0.5949 | PASS |
| d12 | **198 ÷ 511 = 38.75%** vs MD&A "approximately 39%" | **38.7476%**; with the inputs' own ±0.5 thousand the band is **38.61–38.88%** | **PASS on arithmetic, FAIL on rendered precision → 38.7%** (see Check 6) |
| d13 | 232 + 52 = $284,000 | 284 ✓; the MD&A files the components (orig. l.1666, l.1674) but never the sum, so DERIVED is the right class | **PASS** |
| d14 | 52 − 232 − 52 + 1,228 = 944; 52 + 944 = $996 | ties to the audited *Net increase in cash 944* and *end of year 996* (orig. l.3653–3657) | **PASS + tie confirmed** |
| d15 | 81 − 24 = $57 | 57 ✓, and **new tie**: depreciation 5 (1994) + 19 (1995) = 24 = the filed accumulated depreciation | **PASS + tie** |
| d16 | 0 + 17 = $17,000 inventory, "the balance is inferred from movements" | 17 ✓, but the balance sheet **files** *Inventories … 17* at 1995-12-31 (orig. l.3429) | **PASS arithmetically; wrong evidence class (see Check 2/6)** |
| d17 | 17 ÷ 511 = 3.33% | 3.3268% | PASS (render 3.3%) |
| d18 | 511,000 ÷ 11 = $46,455 | 46,454.5 → 46,455 ✓ (rounding stated, denominator caveat stated) | **PASS** |
| d19 | 511,000 ÷ 318,000,000 = 0.161% | 0.1607% | PASS |
| d20 | 2,500,000 − 400,000 = 2,100,000; 1,000,000 ÷ 400,000 = 2.5× "across different years" | ✓ and the mixed-year warning is present | **PASS** |
| d21 | 996 ÷ 284 = 3.51 years | 3.507 | PASS |
| d22 | 1,007,000 ÷ 23 = $43,783 | 43,782.61 → 43,783 ✓, correctly labelled a mean, not a cheque | **PASS** |
| d23 | 100,019 + 145,553 ≈ $245,573 | on corrected inputs $245,572.89 → $245,573 ✓ (and 1,430,244 × 0.1717 = $245,572.89) | PASS (input chain wrong via d4) |
| CSV r93 | **3,021,000 × $0.3333 ≈ $1,006,999** | **$1,006,899.30** | **FAIL — wrong by $99.70** |

**The two figures the brief singled out, in words.**

- **$1,007,000.** Multiplying the filing's displayed price gives **3,021,000 × $0.3333 = $1,006,899.30**, i.e.
  $100.70 *below* the disclosed aggregate; `quantitative.csv` r93's "$1,006,999" is neither (miskeyed digits).
  The difference is **not** an error in the filing and **not** a coincidence: `$.3333` is the filing's four-decimal
  display of exactly one third — $1,007,000 ÷ 3,021,000 = 0.3333333… and 3,021,000 ÷ 3 = 1,007,000 with no
  remainder. The **aggregate is the exact disclosed quantity and the per-share price is the rounded one**, so the
  cross-check must run division (aggregate ÷ shares → $0.33̄), not multiplication; multiplying a rounded price
  always undershoots by 3,021,000 × $0.0000333… ≈ $100.70. Fix: replace the row's value with **$1,006,899.30**
  *or* re-express the check as $1,007,000 ÷ 3,021,000 = $0.3333 (displayed), stating that the aggregate governs.
- **38.7%.** 198 ÷ 511 = **38.7476%**. Both inputs are filed in thousands (orig. l.3722 *$198,000*; l.1435
  *$511,000*), so each carries ±$500 and the ratio's honest band is **38.61–38.88%**. The correct rendering is
  **≈38.7%** (one decimal), with the MD&A's own words — *"International sales represented approximately 39% and
  33% of net sales in 1995 and 1996"* (l.1437–1439) — as the source's precision. "38.75%" is arithmetically
  faithful to the printed thousands but not to their rounding; the independent 1996 check confirms the MD&A's
  rounding direction (5.1 ÷ 15.746 = 32.4% → "approximately 33%").

New reconciliations recovered this pass (all from the audited statements; all currently absent from the register):
- 1995 balance sheet foots end-to-end: 996 + 17 + 14 = 1,027 current assets; + 57 equipment = **1,084 total
  assets** ✓; 99 + 8 = **107** current liabilities; 1,027 − 107 = **920 working capital** ✓;
  1,075 + 150 − 248 = **977 equity** ✓; 107 + 977 = **1,084** ✓ (orig. l.3427–3467).
- Accumulated-deficit roll-forward: (52) + (303) + **107** = **(248)** = the filed *Accumulated deficit* at
  1995-12-31 (l.3461) → the register's "cumulative losses since inception $355,000" is **not** the filed deficit.
- CY1995 equity cash: 1,122 (share sales, after applying $50 of 1994 advances) + 150 (new advances) = **1,272** ✓.
- 1995 share issuance: 10,200,000 founder + **4,235,244** sold + 120,000 exercised = **14,555,244** ✓; plus
  840,534 + 504,459 = **15,900,237** at 1996-12-31 ✓.
- **The in-window slice of the $1,007,000 program is recoverable, not UNKNOWN:** 4,235,244 − 582,528 − 847,716 −
  42,000 = **2,763,000** program shares subscribed in 1995 (Alberg's 150,000 included) → at the filing's exact
  ⅓ price ≈ **$921,000 inside Stage 1**, ≈ $86,000 (258,000 shares) in 1996 — and the consideration ties to the
  filed equity line: 245,573 + 5,408 + 921,000 = **$1,171,978 → filed $1,172** ✓.
- The 23 purchasers decompose in **S-1/A No. 5 only** (l.4665–4668): *Alberg 150,000 + two founder-related
  investors 60,000 + 20 unaffiliated investors 2,811,000* → 3,021,000 ✓ and 1 + 2 + 20 = 23 ✓.
- Series A: 569,396 × $14.05 = **$8,000,013.80** → the Item 5 aggregate **$8,000,014** ✓ (P62's "≈ 8,000,000"
  hides an exact tie).
- Quarterly FY1996: 875 + 2,230 + 4,173 + 8,468 = **15,746** ✓ (brief's figure confirmed; orig. l.355, l.1302).
- 1994 stub: 60 (equity) + 44 (notes) − 24 (operating) − 28 (investing) = **52** closing cash ✓; 38 + 14 + 0 =
  **52** operating expense ✓; 10 + 50 − 52 = **8** equity ✓.
- MD&A control total: *"private sales of Common Stock … through December 31, 1996, totaled $1.6 million"* (orig.
  l.1663–1665) = 60 + 1,272 + 231 = 1,563 ✓.

## CHECK 4 — CROSS-FOOT §P → §R → `quantitative.csv` — **FAIL (4 disagreements; the §P↔§R spine otherwise holds)**

§P ↔ §R: net sales 511,000 ✓; gross margin 19.96% ✓; operating loss (304,000) ✓; marketing 39.1% ✓; cash
996,000 ✓; working capital 920,000 ✓; equity 977,000 ✓; LT obligations 0 ✓; inventory ≈17,000 ✓; equipment
73,000 + 8,000 ✓ (ties P37's 81,000); employees 11 at 1995-12-31 ✓ (P42 / r71 / §R l.948 identical wording, all
three citing No. 3 + No. 5 with the original as corroboration); visits 2,200 ✓; titles >1,000,000 and 10–40% ✓;
shipping $3.00 + $0.95 ✓; 59% flagged FY1996 ✓; $1,272,000 / $295,568 / ≈$976,432 ✓; $44,000 repaid ✓.

Disagreements found:
1. **Miguel A. Bezos cash** — §P14 `≈100,020` vs `quantitative.csv` r22 `100019` vs §P.2 d4 `$100,019.06` vs
   `timeline.csv` r21 `about $100,020` vs `validation.csv` r13 `~$100,020`. Recomputation: **$100,020.06**. §P,
   timeline and validation are right; the CSV value cell and d4 are wrong.
2. **Named-related-party total** — §P19 `295,568` vs §P.2 d7 `= $295,567` (offered as the "dossier rounding").
   Recomputation: **$295,567.89 → $295,568**; §P19, `quantitative.csv` r32, §R l.958 and `data_gaps.csv` r10 all
   carry 295,568 ✓, so d7's total is the outlier. (Separately: on the filing's exact ⅓ price for Alberg the total
   is $295,572.89 — the row should state which price convention it uses; ±$5 is the only honest precision.)
3. **Cumulative losses** — `quantitative.csv` r52 `355,000`, §K l.545 `$(355,000)`, §M l.628 `$(355,000)`,
   `failures.csv` r7 `$355,000` — none of the four appears in §P, and all four stand against the **audited
   $(248,000)** accumulated deficit that the same filing prints next to the 996/1,084/977 columns they cite.
4. **Inventory evidence class** — §P39 `DERIVED … $0 opening`, `quantitative.csv` r67 `DERIVED`, `validation.csv`
   r20 `DERIVED (cash-flow movement)` vs the audited balance-sheet line *Inventories … 17* that §P35's own
   Selected-Financial-Data citation covers. Same number, three files, wrong class in all three.
Also structural: **7 `quantitative.csv` rows have no §P twin** (r7 plan reserve, r11 38,000 and r12 14,000 stub
components, r18 1994 $60,000, r34 $40,000 Nov-1995 loan, r66 cumulative capex, r70 AP +83, r81 IDC $318m) while
no §P row lacks a CSV twin — the §P↔CSV sets are one-directional, which is how the 355,000 error reached three
other files without passing through the §P.2 arithmetic gate.

## CHECK 5 — UNIT AND CURRENCY HYGIENE — **PASS with 3 defects (no new transposition found; the 15 consequence rows are correctly fenced)**

- **Thousands vs millions.** The filings state everything in thousands — orig. l.1297 *"(IN THOUSANDS, EXCEPT PER
  SHARE DATA)"*, and the tables print `511`, `15,746`, `406`, `1,272`. §P and the CSV convert correctly and
  consistently (511,000 / 15,746,000 / 1,272,000) with the unit cell carrying USD ✓; P59 even keeps the filed
  "(thousands)" for the quarterly series ✓. No row mixes the two (no "$511 million", no bare `511` in USD).
- **Transposition hunt.** All numeric rows were compared with the filing's digits: `15,746` ✓, `1,272` ✓,
  `345,525` ✓, `8,000,014` ✓ (the appendices' `$8,000,140` form appears **nowhere** in the audited files),
  `2,012,772` ✓, `3,021,000` ✓, `582,528 / 847,716 / 42,000 / 150,000 / 569,396 / 4,800,000 / 4,235,244` ✓,
  `996 / 920 / 1,084 / 977 / 107 / 76 / 52 / 16 / 8` ✓, `409 / 102 / 200 / 171 / 35 / 406 / 304 / 303 / 198 /
  232 / 284 / 83 / 81 / 73 / 24 / 57 / 17 / 2,200 / 64,333 / 17,008,158` ✓, `$14.05`, `$0.1287`, `$0.1717`,
  `$0.3333`, `$0.6666`, `$1.3333` ✓. **Three transposition-class errors found, all in derived products, not in
  quoted filings:** $100,019.06 (for $100,020.06), $1,006,999 (for $1,006,899.30), and $145,552.83 (for
  $145,552.84).
- **Nominal marking.** 17 `quantitative.csv` rows state "nominal 1994/1995 dollars" ✓; the §P header does not
  carry a global nominal statement → LOW (a single sentence in §P's basis block would close it).
- **Post-boundary values in Stage-1 rows.** All **15** `stage2-consequence` rows were tested: r91–r94 (the
  1995-12-06 → 1996-05-16 program and its average), r95 FY1996 net sales, r96 151/158/256, r97 Dec-1996
  accounts/sales, r98 59% FY1996, r99–r102 1997-03 title figures, r103 June-1996 Series A, r104 Dec-1996 visits,
  r105 1997-03 repeat-purchase. Each carries `stage = stage2-consequence`, a post-boundary date and an in-notes
  warning; **none is presented as a Stage-1 metric**, and no 1996/1997 value has leaked into a `stage1` row of
  that file. Two caveats: (i) r91–r94 date the program **1995-12-06**, inside Stage 1, which is right for the
  window's opening but means the *stage* field, not the date field, is doing the fencing work — keep it that way;
  (ii) **`validation.csv` r26–r28 carry 1996-12-31 / 1997-03 / 1996 values (180,000 accounts; >40% of orders;
  $15,746,000) with `stage = stage1`**, relying on prose ("POST-BOUNDARY consequence") that a machine query
  will not read. That is the one place a post-boundary figure sits in a Stage-1 field; it should become
  `stage2-consequence` to match `quantitative.csv`'s convention.

## CHECK 6 — PRECISION LAUNDERING — **FAIL (2 material, 9 style)**

Material:
- **`quantitative.csv` r33 `976432`** — the §P cell hedges (`≈976,432`) but the CSV value cell carries six
  significant figures built from inputs filed to the nearest thousand and a $295,568 subtotal whose own inputs
  are rounded prices; on rounding alone the residual spans ≈$974,900–$977,900. Render **≈$976,000 (±$1,000)**
  and keep the identity caveat. (The brief's named example, confirmed.)
- **P39/r67/validation-r20 "≈$17,000"** is laundered in the *opposite* direction — an audited filed line
  (`Inventories … 17`) dressed as an inference with a tilde, which weakens it. State **$17,000 (FACT, audited)**.
Style (LOW unless noted): **38.75% → ≈38.7%** (MEDIUM, source said "approximately"); 19.96% / 39.1% / 3.33% /
0.595 / 0.161% / 94.1% (MEDIUM→LOW: one decimal, or quote the MD&A's "approximately 20%", "39%"); **$46,455**
(→ ≈$46,000/person — the row's own denominator caveat is good practice and should be kept); "$100,020.06" and
"$145,552.84" cents-level outputs of rounded filing prices (state ≈ and the convention); d3's 179 days
(day-count convention unstated); P32's `30,000` "Advertising expense" where the filing says the company
*"incurred advertising expense of $30,000"* (l.3734–3736) — incurred ≠ expensed is a real basis word.

Discipline that **passed**: the rounded memoir figures are not laundered — `$1.1M / 22 friends and family at
$50,000 each` appears only inside the told-vs-filed row (§A l.198, §K l.586, `failures.csv` r30) and is explicitly
retired; `$12,000 / $14,000` first weeks, `2,300%`, `July 16, 1995`, the `~$5M / 20%` valuation and the parental
`$150,000 / "almost $250,000"` are all tagged legend/untraced with their 2018/2025 lineages; `~300 invited users`
and `$27.95` carry Low/retrospective classes; the two-decimal `$43,783` is correctly fenced as a mean, not a
cheque; UNKNOWN is used rather than a false precise value in P52–P54, r83–r90.

---

## Claims cut or downgraded (proposed to the repair pass — **not applied by this auditor**)
| Claim ref | Was | Now | Why | Evidence applied |
|---|---|---|---|---|
| `quantitative.csv` r93 (cross-check of the placement) | $1,006,999 as a DERIVED "≈" product | delete the row, or $1,006,899.30 with a pointer that the aggregate ÷ shares = $0.3333 displayed | product miskeyed; the real lesson is that ⅓ is exact | S-1 (orig.) l.4301–4302 |
| §P14 / `quantitative.csv` r22 / §P.2 d4 | ≈$100,020 / $100,019 / $100,019.06 | **$100,020** (state the price-rounding caveat) | recompute; three of five carriers already right | orig. l.2863–2864; No. 5 l.3094 |
| §P19 / §P.2 d7 | $295,567 vs "dossier rounding $295,568" | **$295,568**, convention stated (⅓ for Alberg → $295,573) | note inverted | orig. l.3555–3573 tie |
| §K l.545, §M l.628, `quantitative.csv` r52, `failures.csv` r7 | cumulative losses $(355,000) | audited **accumulated deficit $(248,000)** at 1995-12-31; keep $355 only as "sum of the two loss years, before the $107,000 S-election reclass" | 52 + 303 − 107 = 248 | orig. l.3461, l.3571, l.3715 |
| `quantitative.csv` r83 (valuation row) | "no share count and no valuation" | valuation may stay UNKNOWN; delete the share-count null and **add** 14,555,244 shares outstanding at 1995-12-31 | balance sheet files it | orig. l.3455–3457 |
| §K l.549, §P51, §R l.958, `quantitative.csv` r91 | in-window part of $1,007,000 UNKNOWN | **DERIVED ≈$921,000 (2,763,000 shares)**, ≈$86,000 post-boundary, arithmetic shown | ties to the filed $1,172 consideration and $1,272 cash lines | orig. l.3555–3573 + l.4287–4302; No. 5 l.4648–4668 |
| §P39, r67, `validation.csv` r20 | ≈$17,000 DERIVED | **$17,000 FACT (audited)** | balance-sheet line exists | orig. l.3429 |
| `quantitative.csv` r7, r20 / `timeline.csv` r11 / §Q l.903 | 4,800,000 at 1994-09-15; "$0.1717 floor strike" | label the reserve **1997 split-restated basis**; re-express $0.1717 as the lowest price outstanding at 1997-02-28 | reserve foots to the 1997 population | orig. l.2701–2711 |
| §P22, r36, `decisions.csv` r12, §R (5 rows) | ≈5.5 months vs ~26 weeks | one stated convention (Jul-1995 month-level → 5.5–6.0) with the range shown; recompute §R's per-week figure | 184 days = 6.0 months | orig. l.343–346 caption, l.1377 |
| `validation.csv` r26–r28 | stage = stage1 with 1996/1997 values | stage = `stage2-consequence` | field must carry the fence the prose already states | — |

## Research debt opened by this audit
| RD id | Section | Debt | Assigned | Status |
|---|---|---|---|---|
| RD-019 (new) | K / P | Enter the August 7, 1995 issuance (42,000 sh @ ≈$0.1287 = $5,408; No. 5 adds "who is an employee") as a Stage-1 priced-money row and re-count the 1995 price points; test whether it belongs in the 23 or separately | Numbers repair pass | OPEN |
| RD-020 (new) | K / P / S | Replace the "in-window portion UNKNOWN" with the DERIVED ≈$921,000 split (arithmetic in this sheet) and re-open RD-003's roster question only for the residual 198,000 unaffiliated shares | Company Lead (money) | OPEN — **RD-003 may be partially closed**: it is CLOSED for the total and count, and the in-window split is now derivable |
| RD-021 (new) | P / R / S | Add the audited 1995-12-31 share count (14,555,244) and the A5-only purchaser decomposition (150,000 / 60,000 / 2,811,000; 1 + 2 + 20) to §P and `quantitative.csv`; correct the accumulated-deficit figure in four files | Numbers repair pass | OPEN |
| RD-022 (new) | T (protocol) | Fix `03_quality_control/AUDIT_PROTOCOLS.md` AUDIT 3.1: Amazon has no Nov–Oct fiscal year and no 1996 change — EDGAR FYE 1231 in all four filings; the only period structure in play is the 179-day 1994 stub | Master Orchestrator | OPEN (protocol text, not dataset) |
| RD-023 (new) | S | `sources.csv` S0804 cites accession 0000891020-97-000868, which is **not** in the restored primary set; its quoted figures ($32m / 340,000 / 80,000 / Time citation) are retrievable in No. 3/No. 5 — re-key the numeric rows or restore the document; `S0806`'s URL field is empty (§13: an empty cell is a defect) | Evidence Registrar | OPEN |

## Sign-off
Stage status: RECONSTRUCTION → ADVERSARIAL REVIEW → **QA (AUDIT 3 = FAIL, 31 defect rows registered: 9 HIGH ·
15 MEDIUM · 7 LOW)** → COMPLETE blocked until the 9 HIGH rows are repaired. Repairs are **not** applied here: an
auditor editing what it audits is itself a defect. Machine-readable register:
`01_companies/company_001_amazon/_parts/NUMBER_DEFECTS.md`.
