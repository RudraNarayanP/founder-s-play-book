# AMAZON STAGE 2 — E. ADVERSARIAL REVIEW

**Scope under attack:** THE FOUNDER'S PLAYBOOK, Amazon.com (company_001), Stage 2 = 1996-01-01 → first hard
evidence of repeatability, with the May 1997 IPO as the candidate boundary.
**Reviewer role:** Level-3 Adversarial. Objective is to break the Stage-2 reconstruction *before* it is written.
**Evidence base actually retrieved for this review:** the four local filings in
`E:\founder's playbook\founders_playbook\01_companies\company_001_amazon\sources\` — original S-1
(acc. 0000891618-97-001309, filed 1997-03-24), S-1/A No. 3 (0000891020-97-000755, 1997-05-09), S-1/A No. 5
(0000891020-97-000839, 1997-05-14), 10-K405 FY1997 (0000891020-98-000448, filed 1998-03-30) — read by
`grep -n` line-addressed, plus Stage-1's `research/` dossiers and `CORRECTIONS.md` (COR-03/COR-12, COR-04,
COR-09, COR-10, COR-11, COR-13, COR-14). Web evidence is marked by retrieval date.
**Standing rules honoured:** accession labels follow COR-01 (0000891020-97-000839 is **S-1/A No. 5**, never
"the S-1"); nothing in COR-09's do-not-launder list is reintroduced as fact; headcount dates follow **COR-12
(superseding COR-03)**; the 1995 press release is credited only with what **COR-13** proves it contains.

Key for classes: **FACT** = filed/contemporaneous document says it; **DERIVED** = arithmetic on filed lines;
**FOUNDER CLAIM** = founder statement about the founder's own firm; **SELF-MEASUREMENT** = company reporting
about the company, unaudited as to method; **RETROSPECTIVE** = post-window account of window events;
**SPECULATION** = challenge I could not evidence; excluded from the record's weight.

---

## Challenges

### S2E-01 — "1997 was the breakthrough" vs the loss that *grew* faster than the fear

- **Standard narrative.** The IPO year is the year Amazon "made it": $147.8M of sales, a listed ticker,
  national brand — therefore the model had broken through.
- **Challenge.** A breakthrough year is defined by the *rate of change of the shortfall*, not the size of the
  storefront. FY1997 was a year in which the net loss quintupled while the gross margin *fell*.
- **Earliest source of the popular claim.** Amazon's own "Year in Review"/IR self-narrative tradition and
  contemporaneous IPO coverage; the local in-window articulation of the triumph framing is the S-1/A
  Summary: "The Company has grown rapidly since first opening its bookstore."
- **Founder-originated?** Partly — the growth framing is company-issued; the "breakthrough" gloss is later
  popular retelling.
- **Contradicting / qualifying evidence.**
  10-K405 FY1997, Item 6 Selected Financial Data (filed 1998-03-30), local
  `10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` l.1177-1192,
  https://www.sec.gov/Archives/edgar/data/1018724/0000891020-98-000448.txt —
  verbatim: `Net sales............................................  $147,758   $15,746   $   511      $    --` /
  `Gross profit.........................................    28,813     3,459       102           --` /
  `Loss from operations.................................   (29,209)   (5,979)     (304)         (52)` /
  `Net loss.............................................  $(27,590)  $(5,777)  $  (303)     $   (52)`.
  Same document l.1402-1403: `Gross margin..............................     19.5%                 22.0%                  20.0%`
  and l.1409-1411: `The Company's gross margin decreased due to a combination of lower prices and lower overall
  shipping margins, partially offset by improvements in product cost.`
  Marketing and sales alone were $38,964K = **26.4% of net sales** (l.1434-1435) against a **19.5% gross margin**:
  the 1997 unit economics did not cover the cost of being known.
- **Class.** FACT (+ DERIVED ratio).
- **Confidence in the challenge.** **High** — every figure is in one audited statement in one filing.
- **Best-supported reconstruction.** 1997 is a demand breakthrough and a **unit-economics reversal**: revenue
  ×9.4, operating loss ×4.9, gross margin down 2.5 points from a 1996 peak, with marketing cost 1.35× the
  entire gross margin. Stage 2 may call 1997 a scaling success; it may not call it a breakthrough in the sense
  of the business working.

### S2E-02 — the "positive" 1997 operating cash flow is supplier credit, and the 10-K says so in so many words

- **Standard narrative.** By 1997 Amazon was generating cash; negative working capital was a clever
  float-generating trick, evidence the model worked even while it lost money.
- **Challenge.** Whatever the rhetoric, the audited statement shows FY1997 operating cash of +$3.5M is
  *entirely* the accounts-payable increase; strip it and operations consumed ≈$26M. A model whose cash
  generation is a payables balance is a model whose survival is a **credit decision taken by someone else**.
- **Earliest source of the popular claim.** The float/negative-working-capital framing appears in Amazon's own
  1997 prospectus language about "high inventory turnover, lack of investment in expensive retail real estate
  and reduced personnel requirements give it meaningful structural economic advantages" (S-1/A No. 5 l.332-334).
- **Founder-originated?** Yes — company-authored.
- **Contradicting or qualifying evidence.**
  10-K405 FY1997, MD&A Liquidity (1998-03-30), local l.1544-1549,
  https://www.sec.gov/Archives/edgar/data/1018724/0000891020-98-000448.txt — verbatim:
  `Net cash provided by operating activities of $3.5 million for the year ended December 31, 1997 was primarily
  attributable to increases of $29.8 million in accounts payable, $5.1 million in other accrued expenses and
  $2.9 million in accrued advertising, plus $4.7 million in depreciation and amortization, largely offset by a
  net loss of $27.6 million and increases of $8.4 million in inventories…`
  Statement of Cash Flows, l.2044 (`Accounts payable… 29,845 2,753 99`) and l.2048-2049
  (`Net cash provided by (used in) operating activities… 3,522 (1,735) (232)`).
  **DERIVED:** 3,522 − 29,845 = **−$26,323K** of operating cash excluding the payables build.
  And the lenders priced that exact risk: 10-K l.858-868 `IMPACT OF LOAN FACILITY. On December 23, 1997, the
  Company borrowed $75 million pursuant to a three-year senior secured term credit agreement… financial
  covenants require the Company to, among other things, maintain a minimum cash balance, maintain certain
  levels of earnings or losses before interest, taxes, depreciation and amortization, **limit its accounts
  payable aging** and limit its capital and acquisition expenditures.`
- **Class.** FACT + DERIVED.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** At the close of Stage 2 the company's cash engine was a $29.8M payables
  balance that its own new secured lenders found dangerous enough to covenant. The correct Stage-2 finding is
  not "negative operating cash" (it was nominally positive) but "**positive operating cash purchased from
  vendors on open terms, and formally re-priced by banks on 1997-12-23**".

### S2E-03 — $79,000 of working capital at the last balance-sheet date before the IPO

- **Standard narrative.** The IPO gave Amazon the capital it needed; pre-IPO it was already self-sustaining.
- **Challenge.** At the last balance-sheet date printed in the IPO document — **1997-03-31**, six weeks before
  the final prospectus — working capital was **seventy-nine thousand dollars** on $16.0M of quarterly sales:
  0.5% of one quarter's revenue. A single
  bad week of order returns, one distributor tightening terms, or one seasonal payable spike would have
  exhausted it. That is not a company that had outgrown fragility; it is a company one invoice cycle from
  halting.
- **Earliest source of the popular claim.** Retrospective IPO tellings (e.g. Stone 1997 / subsequent
  business-press recapitulation) — none of which carry a balance sheet.
- **Founder-originated?** No.
- **Contradicting evidence.**
  S-1/A No. 5, SUMMARY FINANCIAL DATA (filed 1997-05-14; balance-sheet date 1997-03-31), local
  `S-1A-No5_acc-0000891020-97-000839_filed-1997-05-14.txt` l.395-399,
  https://www.sec.gov/Archives/edgar/data/1018724/0000891020-97-000839.txt — verbatim:
  `Cash and cash equivalents.............................................................   $ 7,162       $ 48,162` /
  `Working capital.......................................................................        79         41,079` /
  `Total assets..........................................................................    11,722         52,722` /
  `Stockholders' equity..................................................................     2,763         43,763`.
  Quarterly net sales at the same date: `16,005` (l.379). Accumulated deficit `$(9,063)` thousand
  (Capitalization l.1258) — **DERIVED:** the deficit was **3.28× remaining book equity** (9,063 ÷ 2,763), and
  ≈77% of the ≈$11.8M of contributed capital the two lines imply. This review does **not** claim "deficit
  exceeded paid-in capital"; only the 3.28×-of-equity form is supported.
  Version check: the same construction appears in the original S-1 (1997-03-24); the March-31-1997
  balance-sheet date is common to both, so the figure is not an artefact of one accession.
  **⚠ Amended when the 424B1 was restored (acc. 0000891020-97-000868, 1997-05-15):** the *actual* column is
  identical in both documents (`Working capital… 79`), but the **pro-forma** column moves with the price —
  424B1 l.277-279 gives `79 → **49,449**`, `11,722 → 61,092`, `2,763 → 52,133` at the actual **$18.00**, where
  No. 5's `41,079 / 52,722 / 43,763` were computed on its **assumed $15.00**. Cite the 424B1 for the post-IPO
  position and No. 5 only for the assumption it ran on. **The load-bearing number of this record — $79K — is
  unaffected**, and the 424B1's own five-year column repeats it as the fourth period (424B1 l.1290:
  `(16)  920  2,270  79`, i.e. 1994 / 1995 / 1996 / Mar-31-1997), which independently confirms the
  1996-12-31 = $2,270K reading used in S2E-34.
- **Class.** FACT (the number) / DERIVED (the ratios) / INFERENCE (the fragility claim, but drawn from the
  company's own risk language in S2E-04).
- **Confidence in the challenge.** **High** on the number; **Medium-High** on the counterfactual.
- **Best-supported reconstruction.** The IPO was not the reward for a solved problem; it *was* the working
  capital. Pre-IPO Amazon had $7,162K cash, $2,763K book equity and $79K of working capital. Write this into
  Stage 2 explicitly, because a smooth narrative will silently move from 1996's $6.2M year-end cash to 1998's
  $109.8M and skip the gap.

### S2E-04 — what the registration statement itself said would kill the company (the company's own words, 1997-05-14)

- **Standard narrative.** The risks were routine IPO boilerplate; the market's own confidence is the real
  signal.
- **Challenge.** Read against the 1996-97 record, three disclosed risks are not boilerplate — they are
  load-bearing dependencies the reconstruction tends to treat as background.
- **Earliest source of the popular claim.** Post-hoc IPO histories that treat the risk section as a legal
  formality.
- **Founder-originated?** No — registrant-authored, counsel-driven.
- **Contradicting / qualifying evidence.** S-1/A No. 5, RISK FACTORS, 1997-05-14, local l.946-961:
  `RELIANCE ON CERTAIN SUPPLIERS. The Company purchases a substantial majority of its products from two major
  vendors, Ingram and Baker & Taylor, Inc. ("B&T"). Ingram is the single largest supplier and accounted for 59%
  of the Company's inventory purchases in 1996. The Company carries minimal inventory and relies to a large
  extent on rapid fulfillment from these and other vendors. **The Company has no long-term contracts or
  arrangements with any of its vendors that guarantee the availability of merchandise, the continuation of
  particular payment terms or the extension of credit limits.**`
  l.737-746: `RISK OF SYSTEM FAILURE; SINGLE SITE AND ORDER INTERFACE… Substantially all of the Company's
  computer and communications hardware is located at a single leased facility in Seattle, Washington… **The
  Company does not presently have redundant systems or a formal disaster recovery plan** and does not carry
  sufficient business interruption insurance…`
  l.796-803: `From December 31, 1995 to March 31, 1997, the Company expanded from 11 to 256 employees. **The
  majority of the Company's senior management joined the Company within the last five months**, and some
  officers have no prior senior management experience at public companies… In particular, the Company intends
  to hire a Chief Information Officer…`
  l.903-906: `In particular, **the Company has encountered difficulties in attracting a sufficient number of
  qualified software developers** for its Web site and transaction-processing systems…`
  Cross-check on the same headcount sentence: original S-1 (1997-03-24) phrases the identical count as
  "from January 1, 1996 to December 31, 1996, the Company expanded from 11 to 151 employees" — **COR-12** rules
  both filed and both correct; neither may be substituted for the other.
- **Class.** FACT.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** At the IPO the firm was: one supplier at 59% on no contract, one building,
  no disaster recovery, a senior team averaging under five months' tenure, no CIO, and self-reported difficulty
  hiring the engineers its story requires. Every one of those is a *failure-plausible* condition, and every one
  is disclosed by the company on a date inside the window.

### S2E-05 — the distributor dependence did **not** improve with scale: 59% (1996) → 58% (1997)

- **Standard narrative.** Growth diversified the supply base; by the end of Stage 2 Amazon had outgrown its
  single-supplier vulnerability.
- **Challenge.** One point, on a purchase base roughly nine times larger, in a year when the company claims to
  have been buying "some" inventory "directly from publishers". The dependency is structural, not a start-up
  artefact.
- **Earliest source of the popular claim.** Not sourced; inferred by later tellings.
- **Founder-originated?** No.
- **Contradicting evidence.** 10-K405 FY1997 l.382-390 (1998-03-30):
  `Although the Company carries its own inventory (some of which is purchased directly from publishers), it also
  relies on rapid fulfillment from major distributors and wholesalers… Ingram is the Company's single largest
  supplier and accounted for 58% and 59% of the Company's inventory purchases in 1997 and 1996, respectively.`
  and l.845-848: `The Company has no long-term contracts or arrangements with any of its vendors that guarantee
  the availability of merchandise, the continuation of particular payment terms or the extension of credit
  limits.` Note the *change of model language*: the S-1 versions say "The Company carries **minimal**
  inventory" (S-1/A No. 5 l.2377; original S-1 l.2188); the FY1997 10-K deletes "minimal" and substitutes
  "Although the Company carries its own inventory". The cash-flow statement prices that change: inventories
  −$8,400K in 1997 vs −$554K in 1996 (l.2041).
- **Class.** FACT + DERIVED.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** Stage 2 ends with Amazon **less** per-order and **more** inventory-holding
  than it started, and with the same ~58% single-distributor exposure, still uncontracted. The Stage-1
  mechanism (own nothing, buy per order off a distributor file) had already begun to dissolve *inside* the
  window, and no long-term supply agreement replaced it.

### S2E-06 — the company's own supplier was also arming its competitors, and said so

- **Standard narrative.** Amazon's access to the Ingram file was a private advantage.
- **Challenge.** The prospectus describes the distributor as a *public utility that helps everyone*, including
  the entrants Amazon had to beat. Access to Ingram is not a moat if the same Ingram "helps establish and
  operate online sites for booksellers".
- **Earliest source of the popular claim.** Retrospective platform narratives; no in-window document supports
  exclusivity.
- **Founder-originated?** No.
- **Contradicting evidence.** S-1/A No. 5, COMPETITION risk factor, 1997-05-14, l.620-627:
  `These competitors include (i) various online booksellers and vendors of other information-based products such
  as CDs and videotapes, including Book Stacks Unlimited, Inc., a subsidiary of CUC International, Inc. ("CUC"),
  and other small entrants, including entrants into narrow specialty niches, **that may be aided by partnering
  with existing distributors, such as Ingram Book Group ("Ingram"), that help establish and operate online sites
  for booksellers**…`
- **Class.** FACT.
- **Confidence in the challenge.** **High** that the disclosure exists and is company-authored; **Medium** on
  how much competitive harm it actually caused in 1996-97 (unquantified anywhere on the record).
- **Best-supported reconstruction.** Distributor file access was a *purchasable input* available to every
  entrant by Amazon's own description. Stage 2 must not list it as an Amazon-owned asset; it belongs on the
  liability side, because the same supplier's willingness was the whole fulfilment model (S2E-05).

### S2E-07 — "Category expansion proves the model was repeatable": the filings call it **intended**, never launched

- **Standard narrative.** Amazon extended the book model into music/video in the IPO era, demonstrating
  transferability.
- **Challenge.** In every document inside the window, music and video are (a) **planned**, (b) **a competitor's
  business**, or (c) a handful of SKUs inside a "titles" definition engineered to absorb them. Nothing
  purchasable can be dated to 1996-97 on retrieved evidence.
- **Earliest source of the popular claim.** The June-1998 music announcement and later category-expansion
  histories, back-projected.
- **Founder-originated?** Yes (company strategy statements).
- **Contradicting / qualifying evidence.**
  S-1/A No. 5, 1997-05-14, l.490-493 — the definition: `As used herein, "titles" offered by the Company means
  the number of items offered in the Company's catalog and includes primarily books **but also a small number of
  CDs, videotapes and audiotapes**.`
  10-K405 FY1997, 1998-03-30, l.235-236: `**The Company intends over time to expand its catalog into other
  information-based products, such as music.**`
  10-K l.291-294 (the "2.5 million" searchable catalog): `including most of the estimated 1.5 million
  English-language books believed to be in print, more than one million out-of-print titles believed to be in
  circulation and **a small number of CDs, videotapes, audiotapes and other products**.`
  10-K l.745-756 (the killer): `**The Company may not benefit from the first-mover advantage that it
  experienced in the online book market and gross margins attributable to new business areas may be lower than
  those associated with the Company's existing business activities.**`
  And the S-1/A No. 5 forward-looking wrapper, l.505-510, marks all of it: `…other statements including words
  such as "anticipate," "believe," "plan," "estimate," "expect" and "intend"… constitute forward-looking
  statements.`
- **Class.** FACT (about what the documents say) — the *narrative* is CATEGORY ERROR, not a factual mistake.
- **Confidence in the challenge.** **Very high**; this is the cleanest, most checkable finding in the review.
- **Best-supported reconstruction.** Through 1997-12-31 the only *dated, purchasable* expansions on the record
  are the **out-of-print service (began March 1997)** and the **Gift Center (launched November 1997)**, both
  inside books. Music is *intent* at the FY1997 close. A capability claim that rests on the word "intends"
  should be written as an intention, dated, and left there.

### S2E-08 — the selection claim repeats Stage 1's offered-vs-obtainable gap, and the company quantified it: **400,000 of 2.5 million**

- **Standard narrative.** "Earth's Biggest Bookstore" — 2.5 million titles — proved the model's core advantage
  was infinite selection, and selection proves repeatability.
- **Challenge.** The IPO document states the fillable fraction. Of the 2.5M titles *offered*, at most 400,000
  were obtainable from the distributors the whole model ran on; the remaining ~2.1M were listings whose
  sourcing fell to a manual "special order group". Selection was a **catalogue fact**, not a **stock fact** —
  the same offered/obtainable gap Stage 1 established for 1995, now with the company's own numbers.
- **Earliest source of the popular claim.** Amazon's own marketing line "Earth's Biggest Bookstore" (in-window,
  10-K l.227: `Since opening for business as "Earth's Biggest Bookstore" in July 1995`), and the "2.5 million
  titles" figure that per **COR-04** is a 1997 marketing number which must not be back-projected into Stage 1.
- **Founder-originated?** Yes.
- **Contradicting or qualifying evidence.** S-1/A No. 5, WAREHOUSING AND FULFILLMENT, 1997-05-14, l.2385-2388:
  `accounted for 59% of the Company's inventory purchases in 1996. **Of the more than 2.5 million titles offered
  by the Company, up to 400,000 are currently supplied by book distributors and wholesalers, including Ingram
  and B&T.**`
  Version-safety tested: the identical sentence is at original S-1 l.2197 (1997-03-24) and S-1/A No. 3
  l.2397 (1997-05-09) — **three independent 1997 printings of the same registration**, so the line is not an
  amendment artefact.
  The pricing page confirms which titles the discount actually covered: 10-K405 l.1414-1416 —
  `the Company offers **20% and 30% discounts on more than 400,000 titles**, with featured titles discounted at
  40% and certain "special value" editions discounted up to 89%` — i.e. the discount sits on the ~16% of the
  catalog that could be reliably sourced, and the famous "40% off" is featured titles only (cf. S-1/A No. 5
  l.1522-1523: `In March 1997, the Company began discounting the Amazon.com 500 and other featured books by 40%
  from list price.`).
  And availability, in the company's voice, S-1/A No. 5 l.2268-2273: `Some of the Company's titles are
  available for immediate shipment, others are available for shipment within 48 to 72 hours and the remainder of
  in-print titles are generally available within **four to six weeks, although some titles may not be available
  at all**. Out-of-print titles generally are available in **two to six months**, although some titles may not
  be available at all.`
  10-K405 l.335-342 restates it for year-end 1997 with a *different* out-of-print promise:
  `Out-of-print titles generally are available in **one to three months**, although some titles may not be
  available at all.`
- **Class.** FACT; the "four to six weeks"/"may not be available at all" clause is the company's own
  qualification of its own headline.
- **Confidence in the challenge.** **Very high.**
- **Best-supported reconstruction.** In 1997 a customer ordering a random title from the advertised 2.5M was,
  for ~2.1M of them, issuing a *sourcing request* with a multi-week-to-multi-month expected wait and an
  explicit chance of failure. A searcher who wants a moat from "selection" must first show the selection was
  *obtainable*; the registrant itself could not. **A Stage-2 defect to flag:** the "up to 400,000 of 2.5
  million" disclosure appears in all three 1997 registration documents and is **absent from the FY1997
  annual report** — the number vanished the year the company stopped having to certify it in an offering.

### S2E-09 — Barnes & Noble did not sleep; it sued, in the Southern District of New York, on 1997-05-12

- **Standard narrative.** The incumbents were asleep until Amazon forced them online; the 1997 IPO proves the
  market chose the newcomer.
- **Challenge.** The most direct refutation is inside Amazon's own IPO filing, filed two days later: the
  largest bookstore chain in America had already gone to law to define what Amazon is, and its pleaded theory
  was precisely the "selection is not stock" point of S2E-08.
- **Earliest source of the popular claim.** General "disruption" retellings from the 2000s onward.
- **Founder-originated?** No.
- **Contradicting evidence.** S-1/A No. 5, Notes to Financial Statements, Note 5 Contingency (Unaudited),
  1997-05-14, l.4409-4415, https://www.sec.gov/Archives/edgar/data/1018724/0000891020-97-000839.txt:
  `On May 12, 1997, Barnes & Noble, Inc. filed suit against the Company in the United States District Court for
  the Southern District of New York alleging that **the Company has made false advertising claims because it is
  not a "bookstore" and does not physically warehouse most of the titles it offers.** The complaint seeks
  compensatory and punitive damages, and injunctive and other equitable relief. The Company is evaluating
  Barnes & Noble, Inc.'s claims and intends to defend against them vigorously.`
  Reinforced in the same document's risk section, l.1015-1016: `**The Company has received notice of alleged
  claims by B&N.**`
  Same filing, MANAGEMENT bios, l.2727-2731: `SCOTT E. LIPSKY. Mr. Lipsky joined the Company in July 1996 as
  Vice President of Business Expansion. **From March 1994 to July 1996, Mr. Lipsky served as Chief Information
  Officer of Barnes & Noble, Inc., a national trade bookstore chain, and Chief Technology Officer of Barnes &
  Noble College Bookstores, Inc.**`
- **Class.** FACT.
- **Confidence in the challenge.** **Very high** for the suit and the hire (both are audited/attested filing
  text); **Medium** for what B&N's site was doing (see S2E-10, external).
- **Best-supported reconstruction.** B&N was (i) running an online bookstore, (ii) hiring Amazon's future
  business-development VP as its CIO up to July 1996, and (iii) litigating Amazon's advertising on 1997-05-12
  — three days before the final prospectus. Incumbent inattention is not on the record for this window.

### S2E-10 — Amazon's own prospectus listed the incumbents' 1996-97 moves, in the present tense

- **Standard narrative.** (as above)
- **Challenge.** The registrant's competition section is a list of things competitors had *already done*, and
  it is written in the completed aspect: "has launched", "has a relationship", "has begun selling".
- **Earliest source of the popular claim.** Later asymmetry-of-vigilance storytelling.
- **Founder-originated?** No — but it is company-authored, and against its own interest, which is why it
  carries weight.
- **Contradicting evidence.** S-1/A No. 5, COMPETITION, 1997-05-14, l.632-644:
  `…retail vendors of books, music and videotapes, including large specialty booksellers, with significant brand
  awareness, sales volume and customer bases, such as **Barnes & Noble, Inc. ("B&N") and Borders Group, Inc.
  ("Borders"). Both B&N and Borders have announced their intention to devote substantial resources to online
  commerce in the near future. B&N, specifically, has launched a Web site to sell books online and has a
  relationship with AOL through which B&N offers a broad selection of titles at discounted prices. Simon &
  Schuster also has begun selling a number of books through an online site.**`
  And the resources asymmetry, same document l.653-662: `Many of the Company's current and potential competitors
  have longer operating histories, larger customer bases, greater brand recognition and significantly greater
  financial, marketing and other resources than the Company… **Certain of the Company's competitors may be able
  to secure merchandise from vendors on more favorable terms**…`
  10-K405 FY1997 (1998-03-30) l.444-454 adds the capital dimension: competitors include `publishers,
  distributors and retail vendors of books, music and videotapes, including **Barnes & Noble, Inc., Bertelsmann
  AG** and other large specialty booksellers and integrated media corporations…`
- **Class.** FACT.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** By the IPO the field was: CUC-owned Book Stacks Unlimited, B&N live with
  an AOL relationship, Simon & Schuster selling direct, Borders publicly committed, and Bertelsmann's money
  now visible behind B&N. Amazon's own words: `Barriers to entry are minimal, and current and new competitors
  can launch new sites at a relatively low cost` (l.618-619). Stage 2 must not describe 1997 as an uncontested
  field.

### S2E-11 — the incumbent's counter-move that Amazon could not answer: capital, and Amazon's own backer

> **⚠ PART-WITHDRAWN — see `## Attacks that failed`, F-1.** The "capitalised at an order of magnitude above
> Amazon's IPO" leg of this record rested on the Bertelsmann–bn.com investment, which the retrieved source dates
> to **1998**, not 1997. **That leg is withdrawn.** What survives on retrieved evidence is the KPCB/Doerr
> relationship, which is filed, dated and in-window, and the November-1997 Bookstore.com event, which remains
> **unverified** and must not be printed unless D-5 closes.

- **Standard narrative.** Amazon's 1997 lead over the incumbents was decisive.
- **Challenge (surviving form).** The one 1997 fact that cuts against "Amazon had no answer to the incumbents'"
  capital position is not on Amazon's balance sheet at all: the general partner of its own Series A holder sat on
  its board, and the same firm was, within the window, financing bookselling ventures alongside chains. Stage 2
  cannot describe the 1997 capital race as Amazon-versus-everyone unless it can show the shared-backer fact is
  immaterial.
- **Earliest source of the popular claim.** Not on the in-window record — this is missing from the
  reconstruction, not wrong in it.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence (local, filed, in-window).** S-1/A No. 5, CERTAIN TRANSACTIONS,
  1997-05-14, l.3059-3069: `Since the inception of the Company in July 1994, the Company has issued shares of
  Preferred Stock in private placement transactions as follows: 555,161 and 14,235 shares of Series A Preferred
  Stock at $14.05 per share to **Kleiner Perkins Caufield & Byers VIII** and **KPCB Information Sciences Zaibatsu
  Fund II**, respectively… **L. John Doerr, a director of the Company, is a general partner of KPCB VIII
  Associates**, which is a general partner of Kleiner Perkins Caufield & Byers VIII and KPCB Information
  Sciences Zaibatsu Fund II.` Principal-stockholders note, l.3167-3171, repeats the holding as
  `3,315,966 shares and 85,410 shares of Common Stock issuable upon conversion of Series A Preferred Stock`.
  The 1998 escalation (Bertelsmann/bn.com) is dated **1998** by the retrieved source and is therefore *outside*
  Stage 2 — see S2E-23 and F-1.
- **Class.** FACT for the KPCB/Doerr component; **UNVERIFIED-EXTERNAL** for the Bookstore.com component.
- **Confidence in the challenge.** **Medium** — downgraded from the draft. The filed half is solid; the
  competitor-financing half is not established and is left as a named retrieval task (D-5).
- **Best-supported reconstruction.** If D-5 closes, the sentence for Stage 2 is: Amazon raised $49.1M net in
  May 1997 while its own board seat was held by the general partner of firms funding competing book sites. If it
  does not close, the correct text is only the filed KPCB/Doerr relationship, which stands on its own.

### S2E-12 — "The IPO validated it": the prospectus says the offering was for *visibility and credibility*, and disclosed $13.20 of instant dilution

- **Standard narrative.** A priced, oversubscribed NASDAQ IPO is third-party validation of the business.
- **Challenge.** Fundraising is a *price*, not a *verdict*, and the registrant's own stated purpose for the
  offering is capital plus credibility — not proof of model repeatability. The one hard number the document
  puts on buyer value is negative: immediate dilution.
- **Earliest source of the popular claim.** The underwriter pop-up on 1997-05-15/16 and every retelling since.
- **Founder-originated?** Company-authored purpose statement; the "validation" gloss is the market's.
- **Contradicting or qualifying evidence.**
  S-1/A No. 5, USE OF PROCEEDS, 1997-05-14, l.1192-1199: `The principal purposes of this offering are to obtain
  additional capital, to create a public market for the Common Stock, to facilitate future access by the Company
  to public equity markets, and **to provide increased visibility and credibility in a marketplace where many of
  the Company's current and potential competitors are or will be publicly held companies.** The Company has **no
  specific plan** for the net proceeds of this offering.`
  Dilution, l.1173-1177: `IMMEDIATE AND SUBSTANTIAL DILUTION. The initial public offering price is substantially
  higher than the book value per outstanding share… purchasers in this offering will suffer an **immediate and
  substantial dilution of $13.20 per share** in the net tangible book value…`
  **⚠ Amended per S2E-19 (424B1 restored):** $13.20 is the **S-1/A No. 5** figure, computed on the *assumed*
  $15.00 price. In the **424B1 final prospectus dated 1997-05-15**, at the actual $18.00 price, the same line
  reads `**$15.85 per share**` (424B1 l.1053-1057). Likewise the pro-forma-as-adjusted **working capital** at
  1997-03-31 is **$49,449K** in the 424B1 (l.277), not the **$41,079K** printed in No. 5 at the $15.00
  assumption. Cite the 424B1 for both, or the record understates the dilution buyers took by $2.65 a share and
  the capital they gave the company by $8.4M.
  Control, l.1054-1066: `…the outstanding Common Stock will be beneficially owned approximately **41% by
  Jeffrey P. Bezos**… and 10% by members of Mr. Bezos' family… an aggregate of approximately **51% of the
  outstanding voting power**… the Bezos family will be able to (i) elect, or defeat the election of, the
  Company's directors…` — the public bought a minority position in a controlled company.
  Actual proceeds, 10-K405 FY1997 Item 5, l.1124-1134: `The Company's registration statement… for its initial
  public offering… became effective on **May 14, 1997**. Offering proceeds, net of aggregate expenses of
  approximately $4.9 million, were **$49.1 million**. The Company has used approximately $9.6 million… for
  working capital… approximately $7.2 million for the purchase or installation of machinery and equipment and
  approximately **$32.3 million for the purchase of temporary investments**…`
  Traction as actually disclosed at pricing, S-1/A No. 5 l.473-484: `Through March 31, 1997, Amazon.com had
  sales of more than $32 million to approximately 340,000 customer accounts… **Growth rates experienced to date
  are not sustainable. The Company incurred net losses of $5.8 million and $3.0 million in the fiscal year ended
  December 31, 1996 and the quarter ended March 31, 1997, respectively.**`
- **Class.** FACT.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** The offering bought capital, a ticker, and — at the actual $18.00 price —
  **$49,449K** of pro-forma working capital and **$52,133K** of book equity at the same 1997-03-31 balance-sheet
  date (424B1 l.277-279; **amended**, superseding the $41,079K / $43,763K figures computed at No. 5's assumed
  $15.00), and 2/3 of the cash sat in temporary investments at the FY1997 close. What it did not produce is any
  third-party statement that the model repeated: the traction the market bought was
  *cumulative* ($32M since July 1995), and the same paragraph told buyers the rate could not hold.

### S2E-13 — "Amazon's advantage was technology": the word "patent" does not appear in the IPO prospectus's own IP section

- **Standard narrative.** Amazon won because its software — search, recommendations, the order pipeline — was
  years ahead of everyone else's.
- **Challenge.** No 1996-97 document retrieved for this review supports a technology-*advantage* claim, and the
  IPO prospectus is affirmatively against it. The registrant's proprietary-rights section in the final
  prospectus is titled **TRADEMARKS AND PROPRIETARY RIGHTS** and lists trademarks, copyrights, trade dress and
  trade secrets — the word "patent" appears **zero times** in S-1/A No. 5 and zero times in S-1/A No. 3. The
  first claim of patent *applications* anywhere in the corpus is in the FY1997 annual report, filed
  1998-03-30. Whatever the engineering was, the company did not tell investors in 1997 that it owned protectable
  technology.
- **Earliest source of the popular claim.** Post-1999 retellings built backward from the 1997-09-12 "1-Click"
  application / US 5,960,411 (Stage-1 dossier F, record F-80a) — an artifact that post-dates the IPO.
- **Founder-originated?** No — this is the analyst/press gloss.
- **Contradicting or qualifying evidence.**
  S-1/A No. 5, TRADEMARKS AND PROPRIETARY RIGHTS, 1997-05-14, l.984-987: `The Company regards its copyrights,
  service marks, trademarks, trade dress, trade secrets and similar intellectual property as critical to its
  success, and relies on trademark and copyright law, trade secret protection and confidentiality and/or
  license agreements…` — no patent in the enumeration.
  10-K405 FY1997, INTELLECTUAL PROPERTY, 1998-03-30, l.479-492: `The Company regards its **patents**,
  copyrights, service marks, trademarks, trade dress, trade secrets, proprietary technology… In addition, the
  Company **has filed U.S. and international patent applications covering certain of its proprietary
  technology.**`
  Negative-control check performed so this record is not over-read: the string "patent" does occur 6 times in
  the **original** S-1, but all six are inside a reprinted investor agreement's boilerplate representation
  (Exhibit, l.7687-7700: `2.9 Patents and Trademarks. The Company has sufficient title to and ownership of all
  trade secrets, and, to its knowledge, copyrights, information, proprietary rights and processes, patents,
  trademarks…`), and A3/A5 carry only 2 documents against the original's 38 (per COR-04's document arithmetic).
  **The zero-count in A3/A5 is a document-scope artefact, not a deletion** — the defensible statement is about
  what the business section *claims*, not what the amendments omit.
  **STRENGTHENED when the 424B1 final prospectus was restored (1997-05-15):** the string "patent" occurs
  **0 times** in the 424B1 in its entirety (`grep -c` → 0), and its proprietary-rights section is titled
  `TRADEMARKS AND PROPRIETARY RIGHTS. The Company regards its copyrights, service marks, trademarks, trade
  dress, trade secrets and similar intellectual property as critical to its success, and relies on trademark and
  copyright law, trade secret protection…` (424B1 l.864). So the scope-artefact objection no longer applies:
  **the complete document that investors actually bought on — including its exhibits-indexed prospectus text —
  contains no patent claim of any kind.** The technology-moat reading is now falsified by the strongest
  available in-window document, not merely unsupported.
- **Class.** FACT + documented negative search.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** Through the IPO, Amazon's disclosed IP position was brand + trade secret.
  A Stage-2 that wants a technology moat must produce a 1996-97 document that asserts one; none is in the four
  filings.

### S2E-14 — in the same prospectus the company says its technology strategy is to **buy**, not build

- **Standard narrative.** Proprietary systems were the differentiator.
- **Challenge.** The registrant's stated technology policy in all three 1997 registration documents is the
  opposite: license whatever is commercially available, build only the residue.
- **Earliest source of the popular claim.** Retrospective engineering mythology; **COR-06** already
  establishes that the Stage-1 stack is documented only in engineer recollection (Sheff 1999/2000; Kaphan quoted
  2011 via a 2025 essay).
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.** S-1/A No. 5, TECHNOLOGY, 1997-05-14, l.2403-2409:
  `The Company has implemented a broad array of site management, search, customer interaction,
  transaction-processing and fulfillment services and systems using a combination of its own proprietary
  technologies and commercially available, licensed technologies. **The Company's current strategy is to license
  commercially available technology whenever possible rather than seek internally developed solutions.**`
  Version-safety: identical at original S-1 l.2217 and S-1/A No. 3 l.2418.
  The catalog itself is bought, not built: 10-K405 l.298 — `**The Company licenses some of its catalog and other
  information from third parties.**` (S-1/A No. 5 l.2209-2210 says the same.)
  Security is bought: S-1/A No. 5 l.915-916 — `The Company relies on encryption and authentication technology
  licensed from third parties to provide the security and authentication necessary to effect secure transmission
  of confidential information`.
  And the FY1997 10-K **softens** the same sentence — l.407-410: `The Company's current strategy is to focus its
  development efforts on creating and enhancing the specialized, proprietary software that is unique to its
  business and to license commercially developed technology for other applications where available and
  appropriate.` The clause "whenever possible rather than seek internally developed solutions" is gone by
  1998-03-30. **That is a change of self-presentation inside the reconstruction window and must be cited by
  date, not blended.**
- **Class.** FACT.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** In 1996-97 Amazon's own words describe an integrator, not a technology
  leader. What is genuinely proprietary in the filings is an *order-routing* application (S2E-15), not a stack.

### S2E-15 — the one "technology" claim the filings actually support is a **procurement router**, and its capacity ceiling is the 400,000

- **Standard narrative.** Sophisticated technology filled orders at scale.
- **Challenge.** Strip the adjectives and the disclosed invention is: sort each incoming order into (a) titles a
  distributor can ship within hours over an electronic interface, or (b) everything else, which goes to people.
  That is a commercial routing rule whose value depends on someone else's interface, and it is capped by the
  number of titles the interfaces cover.
- **Earliest source of the popular claim.** Later platform narratives.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.** S-1/A No. 5, WAREHOUSING AND FULFILLMENT, l.2390-2399:
  `The Company utilizes automated interfaces for sorting and organizing its orders… **The Company's proprietary
  software selects the orders that can be filled quickly via electronic interfaces with vendors, and forwards
  remaining orders to its special order group.** Under the Company's arrangements with its distributors,
  electronically ordered books often are shipped by the distributor within hours of receipt of an order from
  Amazon.com… The Company has developed customized information systems and dedicated ordering personnel that
  specialize in sourcing hard-to-find books. **The Company currently processes all sales through its warehouse in
  Seattle.**`
  And the internal control weakness the same filing admits, l.700-716: `The Company uses an internally developed
  system for its Web site, search engine and substantially all aspects of transaction processing… **The system is
  not integrated with the remainder of the Company's accounting and financial systems.**… the Company's current
  management information system… is inefficient with respect to traditional accounting-oriented reporting and
  requires a significant amount of manual effort to prepare information for financial and accounting reporting.
  **This may make it difficult for management to obtain accurate financial statements and reporting information
  on a timely basis.**`
- **Class.** FACT.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** The real 1996-97 technical asset was the vendor interface plus the human
  fallback. The company itself disclosed that the same system could not produce timely accounting information —
  which is the strongest available argument against reading "technology advantage" into this window, because the
  firm could not measure itself with it.

### S2E-16 — the most-cited Amazon innovations were **not live** inside the window

- **Standard narrative.** Collaborative filtering and one-click made the site unmatchable in 1996-97.
- **Challenge.** Recommendations were *promised*; one-click was not yet applied for. Both are dated *after* the
  IPO by the company's own text.
- **Earliest source of the popular claim.** 2000s innovation retrospectives.
- **Founder-originated?** No.
- **Contradicting evidence.** S-1/A No. 5, 1997-05-14, l.2247-2248: `**Collaborative Filtering. Amazon.com
  intends to add a collaborative filtering service** to its personalized service offerings in the future.`
  Repeated as intent at l.2072 and l.2348. Stage-1 record F-80a dates the ordering patent application
  (US 5,960,411) to **1997-09-12**, four months after the offering.
- **Class.** FACT + RETROSPECTIVE projection.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** The defensible in-window feature set is: search over a licensed file,
  e-mail notification (Eyes/Editors), reviews, and a nine-address customer-service e-mail queue (S-1/A No. 5
  l.2363). Personalisation-as-moat is a 1998-99 story wearing a 1997 date.

### S2E-17 — what actually drove 1996-97 demand was bought traffic, and the company named the vendors

- **Standard narrative.** Growth came from the product.
- **Challenge.** The growth mechanism is disclosed as paid placement and referral economics: banner
  advertising on named aggregators, print advertising, a commission-paying Associates program, and $6.1M of
  1996 marketing spend on $15.7M of sales. The reconstruction's "word-of-mouth" inheritance is contradicted by
  an audited expense line.
- **Earliest source of the popular claim.** Sheff's 1999/2000 narrative preamble: `He launched the website in
  July 1995 and **advertised by word of mouth**` (local `sheff-playboy-interview_…txt` l.25) — a retrospective
  founder-adjacent account.
- **Founder-originated?** Indirectly (company-favourable framing in a founder interview).
- **Contradicting or qualifying evidence.** S-1/A No. 5, MARKETING AND PROMOTION, l.2320-2333:
  `The Company places advertisements on various high-profile and high-traffic conduit Web sites, including
  **CNET, Yahoo!, Pointcast, Excite, Lycos, Quote.com and CNN**. These advertisements usually take the form of
  banners…` and `…print advertising in specialized and general circulation newspapers and magazines, such as
  **The New York Times Book Review and Wired**… as part of the "What's New" and "What's Cool" sections of
  Netscape and Yahoo!, respectively.`
  l.2335-2344: `Associates Program, which includes **several thousand enrolled members**… The Associate…
  **receives a commission for certain orders**. Prominent Associate sites include Netscape Developer's Bookstore,
  The Village Voice and Upside.com.`
  MD&A, l.1533-1537: `Marketing and sales expenses increased from $200,000 in 1995 to **$6.1 million in 1996**.
  Marketing and sales expenses as a percentage of net sales were **39% in each of 1995 and 1996**… primarily
  attributable to expansion of the Company's **online and print advertising**, public relations and other
  promotional expenditures…` — **DERIVED: $6,090K on $15,746K of 1996 net sales = 38.7%** (10-K405 l.1434-1435).
  10-K405 l.1444-1445 attributes the 1997 increase partly to `expenses associated with **Internet aggregator
  promotional relationships**`.
- **Class.** FACT + DERIVED.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** 1996-97 demand was bought at roughly 39 cents per revenue dollar. The
  repeatable thing demonstrated in the window is that **money spent on aggregation placement converted into
  orders** — a marketing result, not a technology result.

### S2E-18 — Amazon's disclosed dependency was on the *gatekeepers*, and it said they could charge it out of existence

- **Standard narrative.** Being first on the Web was itself the advantage.
- **Challenge.** The prospectus identifies browsers and online services as potential toll-collectors standing
  between Amazon and its customers — the same commercial relationship S2E-17 says generated the demand. The
  "channel" was never owned.
- **Earliest source of the popular claim.** Not applicable — the refuting evidence is the company's own.
- **Founder-originated?** No.
- **Contradicting evidence.** S-1/A No. 5, COMPETITION, l.676-678: `In addition, **companies that control access
  to transactions through network access or Web browsers could promote the Company's competitors or charge the
  Company a substantial fee for inclusion.**`
  And l.673-675: `client-agent applications that select specific titles from a variety of Web sites may channel
  customers to online booksellers that compete with the Company.`
  Compare 10-K405 l.470-471, a year later: `"shopping agent" technologies will permit customers to quickly
  compare the Company's prices with those of its competitors.`
- **Class.** FACT.
- **Confidence in the challenge.** **High** that the disclosure exists; **Medium** on realised harm in-window.
- **Best-supported reconstruction.** Amazon's 1997 customer acquisition ran through parties it neither
  contracted with nor controlled, and its own filing priced that as a survival risk.

### S2E-19 — the IPO price is filed, but **not in the document everyone cites**: $18.00 is in the 424B1 of 1997-05-15, while S-1/A No. 5 of 1997-05-14 still says $14-16

> **AMENDED 2026-09-24 after the Form 424B1 final prospectus was restored to `sources/`**
> (acc. 0000891020-97-000868, filed and dated **1997-05-15**). My first draft of this record asserted that "$18"
> and "$54,000,000" were **not filed anywhere**. That was wrong and is corrected below: both are on the 424B1
> cover. What survives — and what matters — is the **citation** rule. See failed attack **F-10**.

- **Standard narrative.** "Amazon IPO'd at $18 in May 1997 and raised $54 million" — usually cited to "the S-1".
- **Challenge.** The number is right and the citation is wrong. S-1/A No. 5, filed the day *before* the
  prospectus, still prices the deal at **$14.00-$16.00** and computes every proceeds, capitalisation and dilution
  figure at an assumed **$15.00**. Anyone citing accession 0000891020-97-000839 for "$18" or "$54M" is citing a
  document that says neither. The final terms live in a **fifth** accession that was not in the original
  evidence set.
- **Earliest source of the popular claim.** Two, and they now agree: the **424B1 final prospectus, dated
  May 15, 1997** (filed), and Amazon's press release of **May 14, 1997** (company-issued):
  `SEATTLE, WA (May 14, 1997) … offering of 3,000,000 shares of its Common Stock at a price of $18 per share.
  Deutsche Morgan Grenfell Inc. is acting as lead manager… Alex. Brown & Sons Incorporated and Hambrecht & Quist
  are acting as co-mangers… NASDAQ: AMZN` — retrieved 2026-09-24,
  https://press.aboutamazon.com/1997/5/amazon-com-inc-announces-initial-public-offering-of-3-000-000-shares-of-common-stock
- **Founder-originated?** Company-issued.
- **Contradicting or qualifying evidence.**
  **FILED FINAL TERMS** — 424B1 cover table, 1997-05-15, l.124-125, local
  `424B1_final-prospectus_acc-0000891020-97-000868_filed-1997-05-15.txt`,
  https://www.sec.gov/Archives/edgar/data/1018724/0000891020-97-000868.txt :
  `Per Share  $18.00  $1.26  $16.74` / `Total(3)  $54,000,000  $3,780,000  $50,220,000`, with footnote
  `(2) Before deducting expenses estimated at $850,000, payable by the Company` and l.1066-1070
  `the net proceeds… at the initial public offering price of $18.00 per share, are estimated to be approximately
  **$49.4 million** (approximately $56.9 million if the… over-allotment option is exercised in full)`.
  **Still in No. 5, now superseded:** `It is currently estimated that the initial public offering price will be
  **between $14.00 and $16.00 per share**` (l.224-228); `assuming an initial public offering price of **$15.00**
  … approximately **$41.0 million**` (l.1186-1189); registration-fee table `3,450,000 shares $16.00 $55,200,000`
  (l.173).
  **Actual, as later reported:** 10-K405 l.1125-1127 `became effective on May 14, 1997. Offering proceeds, net of
  aggregate expenses of approximately $4.9 million, were **$49.1 million**` — **DERIVED:** the estimate $49.4M and
  the reported $49.1M differ by $0.3M, and the 10-K's "$4.9 million of aggregate expenses" *includes* the
  $3.78M underwriting discount, so the two expense figures are on different bases. Never mix them.
  **Dilution changes with the price** — No. 5 at $15.00 assumed: `$13.20 per share` (l.1176-1177); 424B1 at
  $18.00: `**$15.85 per share**` (l.1056). Both are in the corpus; only the second is the price buyers paid.
- **Class.** FACT (all three documents) + DERIVED (the reconciliation).
- **Confidence in the challenge.** **High**, and now anchored to the right document.
- **Best-supported reconstruction.** Four carriers, four jobs: **424B1 (1997-05-15)** for price, size, discount,
  proceeds and final dilution; **press release (1997-05-14)** for the underwriter line-up; **10-K405** for
  effectiveness (1997-05-14) and the *actual* $49.1M net; **S-1/A No. 5 (1997-05-14)** only for the $14-16 range,
  the $15.00 assumptions and everything computed off them. Add **acc. 0000891020-97-000868 to COR-01's table** —
  the corrections register currently lists four filings and should list five.

### S2E-20 — "repeat customers account for over 40% of orders": self-measured, undated, denominator-free, and it moves when nobody is looking

- **Standard narrative.** A 40% repeat rate in 1997 proves customers stuck, which proves the model repeated.
- **Challenge.** Every load-bearing property of that sentence fails. It is a company statement about the
  company; it is anchored to no measurement period ("currently"); the denominator ("orders") is undefined and
  never reconciled to any filed quantity; and the *same* clause reads 58% eighteen months later with no
  explanation. A percentage a firm reports about itself, with no method, is an assertion — not evidence of
  retention.
- **Earliest source of the popular claim.** Amazon's own registration statements.
- **Founder-originated?** Yes (registrant-authored, unaudited).
- **Contradicting or qualifying evidence.**
  Original S-1, 1997-03-24, l.315-320: `Through December 31, 1996, Amazon.com had sales of more than $16 million
  to approximately 180,000 customer accounts in over 100 countries… and **repeat customers currently account for
  over 40% of orders.**`
  S-1/A No. 5, 1997-05-14, l.336-340 (and l.473-479): `Through March 31, 1997… more than $32 million to
  approximately 340,000 customer accounts… and **repeat customers currently account for over 40% of orders.**`
  → **the number did not move for six months while the account base nearly doubled**, and neither document
  defines "repeat customer", "orders", or the look-back window.
  10-K405 FY1997, 1998-03-30, l.243-244: `**Repeat customers currently account for over 58% of orders.**`
  Counter-arithmetic the narrative suppresses: if repeat customers are ~40% of orders, **~60% of 1996-97 orders
  came from people who had not ordered before** — consistent with a rented, first-time, search-driven traffic
  stream (S2E-17), not with a retention engine.
  Related undefined denominator, same 10-K l.241-243: `Through December 31, 1997, the Company had sales of more
  than **$164 million** to approximately **1.5 million customer accounts**` — **cumulative since July 1995**,
  against FY1997 sales of $147.8M; 1.5M is a *registered-accounts* count with no stated activity test, and
  "$164M cumulative" less "$15.7M (1996)" less "$0.5M (1995)" implies ≈$147.8M for 1997, i.e. the cumulative
  figure adds nothing that the annual figure does not, and must not be quoted as if it did.
- **Class.** SELF-MEASUREMENT; the 60%-first-time inference is DERIVED.
- **Confidence in the challenge.** **High** on the attribution defects; **Medium-High** on the counter-read
  (the company never publishes the complement).
- **Best-supported reconstruction.** Stage 2 may report: "the company disclosed >40% of orders from repeat
  customers in three 1997 registrations and >58% in its FY1997 annual report; no definition, period or
  denominator is given anywhere; there is no independent measurement." Any stronger retention statement is
  laundering.

### S2E-21 — "average daily visits grew from 2,200 to 80,000": a self-counted number the prospectus felt obliged to caveat

- **Standard narrative.** Traffic growth proves demand.
- **Challenge.** It is the company counting its own servers, on no audit basis, at two dates it chose — and the
  parenthetical "(not 'hits')" is itself an admission that the industry's traffic metrics were being gamed.
  Nothing ties visits to orders, so no conversion claim is available.
- **Earliest source of the popular claim.** Amazon's registration statements.
- **Founder-originated?** Yes.
- **Contradicting or qualifying evidence.** S-1/A No. 5 l.337-339: `Average daily visits **(not "hits")** have
  grown from approximately 2,200 in December 1995 to approximately 80,000 in March 1997`. Original S-1 l.316-318:
  the same series ending `approximately 50,000 in December 1996`. No conversion rate, order count, or
  visits-to-orders ratio appears in any of the four filings (searched for `average order`, `orders received`,
  `conversion`).
- **Class.** SELF-MEASUREMENT.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** Report the series as company-asserted traffic, note that the filings never
  publish an order count anywhere in the 1996-97 record, and treat "traffic" and "demand" as different claims.

### S2E-22 — the only third-party endorsement in the IPO document is a magazine list, and the company **disowned** the two flattering claims in circulation

- **Standard narrative.** Independent validation in 1997: Time named them a best site, DEC said they were
  growing 3,000% a year, the press said they could be profitable at will.
- **Challenge.** Time's "Best Websites of 1996" is the *only* third-party praise the prospectus cites, and it is
  an editorial list, not a market test. The two loud external claims were **expressly disclaimed by the
  registrant in its own IPO document**, one of them a claim about the founder's own statement. Any Stage-2
  sentence that deploys either is deploying a number Amazon told investors not to rely on.
- **Earliest source of the popular claim.** (a) Digital Equipment Corporation advertisement, 1997, quoted inside
  the S-1/A; (b) an April 1997 newspaper article reporting Bezos — and the local HistoryLink essay (published
  2025-04-07) reproduces the (b) quote verbatim as settled fact, l.108: `"We are not profitable. We could be.
  It would be the easiest thing in the world to be profitable. It would also be the dumbest…"` attributed to
  `"Payoff is Still Elusive …"`, The New York Times, 1997.
- **Founder-originated?** (b) yes — a Bezos quotation; (a) no — a vendor's advertisement.
- **Contradicting or qualifying evidence.** S-1/A No. 5, RISK FACTORS — RECENT AND CONTINUING PUBLICITY,
  1997-05-14, l.756-776: `RECENT AND CONTINUING PUBLICITY… For example, **in April 1997, a newspaper article
  stated that the Company's President said that the Company is not yet profitable -- although it easily could
  be** -- because of massive investment in advertising across the Internet and refinement of its marketing
  techniques… **The Company's view, however, is that it will incur substantial losses for the foreseeable
  future.** In addition, **a recent advertisement by Digital Equipment Corporation states that the Company is
  growing at a rate of 3,000% per year. In fact, the Company's sales are now growing at a slower rate** and the
  Company believes that its historical sales growth rates are not sustainable… In addition, **this advertisement
  states that the Company is the world's most prosperous online bookstore. The Company, however, has incurred
  significant losses to date**…` and l.781-788: `**Neither the Company nor any of the Underwriters have
  confirmed, endorsed or adopted these third-party statements**… they are disclaimed by the Company and the
  Underwriters. Accordingly, **prospective investors should not rely on such third-party statements**…`
  Same-document version check: the identical passage is at S-1/A No. 3 l.759 — two printings, one lineage
  (relevant to S2E-28).
  The third-party praise actually filed, S-1/A No. 5 l.340-341: `**Time magazine rated Amazon.com one of the 10
  "Best Websites of 1996."**`
- **Class.** FACT.
- **Confidence in the challenge.** **Very high.**
- **Best-supported reconstruction.** The company contradicted "could be profitable easily" and "3,000% growth"
  in its own prospectus. Stage 2 should *cite that contradiction* — it is far more informative about 1997 than
  either claim, and it is the single best in-window answer to the victory narrative.

### S2E-23 — the incumbent that mattered had its own e-commerce arm running before the IPO closed, with $11.9M of sales the same year

- **Standard narrative.** The incumbents were asleep until 1998-99; Amazon had the field to itself.
- **Challenge.** Barnes & Noble was live in March 1997 as the exclusive AOL bookseller, had its own site two
  months later, and booked $11.9M of online sales in 1997 — 8% of Amazon's $147.8M, on roughly one quarter of
  operating time and with a chain Amazon could not buy. "Asleep" is not the condition; the condition is
  "later, funded, and willing to sue".
- **Earliest source of the popular claim.** Post-2010 disruption retellings; also a real in-window
  distortion — Amazon's own prospectus says B&N "have announced their **intention** to devote substantial
  resources", which is weaker than what B&N had already done (S2E-10).
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.**
  Encyclopedia.com, "Barnesandnoble.Com" (International Directory of Company Histories, secondary, tier 3),
  retrieved 2026-09-24, https://www.encyclopedia.com/economics/encyclopedias-almanacs-transcripts-and-maps/barnesandnoblecom
  — verbatim: `entered the world of online bookselling in March 1997 as the exclusive bookseller on America
  Online (AOL)`; `Two months later the company set up its own Web site for online purchases`; `Sales at
  barnesandnoble.com doubled in each of 1997's first three quarters, and reached $11.9 million that year`.
  Amazon-side corroboration of the AOL relationship, S-1/A No. 5 l.641-643 (1997-05-14): `B&N, specifically, has
  launched a Web site to sell books online and **has a relationship with AOL** through which B&N offers a broad
  selection of titles at discounted prices.`
  The 1998 escalation (out of window, listed only to date the trend): `German media conglomerate Bertelsmann AG
  agreed to invest $200 million in the online bookseller for a fifty percent interest`; `For 1998
  barnesandnoble.com reported sales of $61.8 million and a net loss of $83.1 million`.
  **Correction issued during this review:** my first draft of this record treated the Bertelsmann investment as
  a 1997 event (see S2E-11, which was written before this retrieval, and `## Attacks that failed` F-1). The
  retrieved source dates it to **1998**. The 1997-sufficient core of the attack is the March-1997 AOL launch,
  the May-1997 own-site launch, the $11.9M of 1997 sales, and the 1997-05-12 lawsuit — all of which stand.
- **Class.** FACT (Amazon-side, tier 1) + TIER-3 SECONDARY for B&N's own dates and sales.
- **Confidence in the challenge.** **High** on the existence and sequence of B&N's moves; **Medium** on the
  $11.9M figure until it is chased to a B&N filing. **Action for the Company Lead: verify the March-1997 AOL
  launch and $11.9M against Barnes & Noble's own FY1997 10-K before printing.**
- **Best-supported reconstruction.** Amazon's 1997 lead was real and large, but it was a lead over an incumbent
  that had already entered, not over an incumbent that had not noticed.

### S2E-24 — Borders incorporated its online business in 1997, and a price war against Amazon was announced in the press in August 1997

- **Standard narrative.** No one competed with Amazon on price or scale in 1996-97.
- **Challenge.** Contemporaneous reporting shows a named competitor cutting prices *explicitly to take share from
  Amazon* three months after the IPO — and the "40% off" Amazon is remembered for was matched, not invented.
- **Earliest source of the popular claim.** Not applicable — this is an omission, not an error.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.**
  Chicago Tribune, "CUC International" (company-news column), **published August 28, 1997**, retrieved
  2026-09-24, https://www.chicagotribune.com/1997-08-28/cuc-international-2/ — verbatim: CUC's unit
  `Wednesday unveiled price cuts to take market share from Amazon.com Inc. and Barnes & Noble Inc.` and would
  `increase discounts to 40 percent off the suggested retail price for hardcover books`. (CUC International is
  the same parent Amazon's own prospectus named for **Book Stacks Unlimited**: S-1/A No. 5 l.623-624.)
  Borders: Encyclopedia.com, "Borders Group, Inc.", retrieved 2026-09-24,
  https://www.encyclopedia.com/social-sciences-and-law/economics-business-and-labor/businesses-and-occupations/borders-group-inc
  — `1997: Borders Online, Inc. created to establish electronic sales operations`; `Borders.com launched in
  1998`; `unofficial debut on the Web in May 1998`. Same source's revenue lines are internally inconsistent
  (`Sales in 1996 reached more than $2 billion`; `1997 sales of $1.95 billion`) and **must not be printed
  without chasing Borders' own 10-K**.
  Amazon's own filing, S-1/A No. 5 l.634-636: `Both B&N and Borders **have announced their intention** to devote
  substantial resources to online commerce in the near future.`
- **Class.** FACT for the Amazon-side citations; TIER-3 SECONDARY for the competitor dates.
- **Confidence in the challenge.** **Medium-High**; the Chicago Tribune item is contemporaneous and specific,
  the Borders chronology is secondary.
- **Best-supported reconstruction.** By the second half of 1997 Amazon faced (i) a chain-owned online store with
  an AOL distribution deal, (ii) a bookseller chain that had incorporated an online subsidiary, and (iii) an
  established online competitor owned by a diversified services group running a discount campaign aimed at it by
  name. This belongs in Stage 2's consequence column, not in a 1998 coda.

### S2E-25 — which of Amazon's 1997 advantages were actually defensible

- **Standard narrative.** Brand, selection, technology and switching costs.
- **Challenge.** Tested one by one against the in-window record, three of the four fail; and the one that
  survives is not the one the story emphasises.
- **Earliest source of the popular claim.** Composite of company strategy language and later retelling.
- **Founder-originated?** Partly.
- **Contradicting or qualifying evidence (the four tests, all local):**
  **Brand** — partially defensible, but *rented*: the only brand asset in the filings is the mark and the media
  position, and the prospectus itself says brand awareness is something *competitors* have more of (S-1/A No. 5
  l.653-655). `announcements of … changes in the market valuations of other Internet… companies … many of which
  are beyond the Company's control` (l.1082-1090) is the company saying its own brand value was market-condition
  dependent.
  **Selection** — not defensible: `Of the more than 2.5 million titles offered by the Company, up to 400,000 are
  currently supplied by book distributors and wholesalers` (S2E-08), and the file itself is licensed from third
  parties (10-K405 l.298).
  **Technology** — not defensible in-window: no patent claim in the prospectus (S2E-13); strategy is to license
  (S2E-14); collaborative filtering not yet shipped (S2E-16); no CIO and admitted developer-hiring difficulty
  (S2E-04).
  **Switching costs** — weakest of all: `The Company does not have long-term employment agreements with any of
  its key personnel`; `no long-term contracts or arrangements with any of its vendors`; and on the customer side
  the only stickiness disclosed is a stored password — `The personal password allows repeat customers to
  automatically access their previously provided shipping and credit card information` (S-1/A No. 5 l.2261-2263)
  — against an explicitly-foreseen comparison tool: `client-agent applications that select specific titles from a
  variety of Web sites may channel customers to online booksellers that compete with the Company` (l.673-675).
  **What does survive:** (i) the *aggregated* fillable long tail — 400,000 sourceable titles in one searchable
  place was still ~3× a superstore and no competitor is shown to have it on this record; (ii) the volume-based
  purchase position with distributors that a 58% share of Ingram's online-book channel implies (S-1/A No. 5
  l.948-949; 10-K405 l.388-389); (iii) **the negative-working-capital float itself**, which was a real cost
  advantage while suppliers extended it and is precisely what the December 1997 covenants began to cap
  (S2E-02).
- **Class.** FACT for each quoted item; **INFERENCE** for the ranking.
- **Confidence in the challenge.** **High** on the individual findings; **Medium** on the overall verdict,
  because "defensible" requires a counterfactual none of these documents can supply.
- **Best-supported reconstruction.** Amazon's defensible 1997 assets were commercial and positional — aggregated
  long-tail availability, purchase volume, supplier float — not technical, and two of the three were
  contingent on third parties' continued willingness.

### S2E-26 — the 1996/1997 headcount sentences are a **basis** minefield, and two SEC filings disagree about the same date

- **Standard narrative.** "11 employees in 1995, 151 by the IPO, 614 by 1997" — a clean ramp.
- **Challenge.** (a) Per **COR-12** the *original S-1* anchors "11 → 151" to **1996-01-01 → 1996-12-31** while
  the *amendments* anchor "11 → 256" to **1995-12-31 → 1997-03-31**: both filed, neither interchangeable, and a
  Stage-2 that says "11 employees at the end of 1995" must cite **No. 3/No. 5**, not the original. (b) The
  styling changes with the accession — 151 is "full-time", 256 is not. (c) Most importantly, **the FY1997 10-K
  and the original S-1 state different headcounts for the identical date 1996-12-31: 158 vs 151.** That is not a
  different-date artefact; it is two filings disagreeing, and COR-11(2) left it unresolved because it assumed any
  158 came from elsewhere. It does not: **it comes from a filing.**
- **Earliest source of the popular claim.** The filings themselves.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.**
  Original S-1, 1997-03-24 (quoted in COR-12's table and COR-03): `…from January 1, 1996 to December 31, 1996,
  the Company expanded from 11 to 151 employees` and `As of December 31, 1996, the Company employed **151
  full-time** employees.`
  S-1/A No. 5, 1997-05-14, l.796: `From December 31, 1995 to March 31, 1997, the Company expanded from **11 to
  256 employees**`; l.2577: `As of March 31, 1997, the Company employed **256 employees**` — no "full-time".
  10-K405 FY1997, 1998-03-30, l.728-729: `The Company's employee base has similarly expanded, growing from
  **158 employees as of December 31, 1996** to 614 employees as of December 31, 1997`; l.516: `As of December
  31, 1997, the Company employed **614 full-time employees**.`
  Note the 10-K also silently *drops* the "11" anchor entirely.
- **Class.** FACT; the reconciliation ("part-time/editorial temporaries included in 158") is
  **UNRESOLVED-CONFLICT**, not fact — the filings give no bridge.
- **Confidence in the challenge.** **High** — this is a same-date, two-document numerical contradiction on the
  record.
- **Best-supported reconstruction.** Stage 2 must print: `151 (S-1 original, "full-time", 1996-12-31)` **and**
  `158 (10-K405, 1996-12-31)` as an open conflict with no bridge, and cite COR-12 for the 1995-12-31/1996-01-01
  basis. Picking one silently is the defect the corrections register exists to catch.

### S2E-27 — the registration lineage is being counted as corroboration **again**, one level down

- **Standard narrative.** "Confirmed in three filings."
- **Challenge.** COR-01/COR-02 caught the accession mix-up; the subtler version of the same error is still
  available: the original S-1, No. 3 and No. 5 are **one registration statement (File No. 333-23795) printed
  four times**, and any fact that appears identically in all of them has **one** witness. I tested every
  load-bearing fact in this review for version-safety precisely so the Company Lead cannot triple-count it.
- **Earliest source of the popular claim.** Internal dossier practice, already corrected once (COR-01).
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.** Header identity across the amendments: original S-1 `SEC FILE
  NUMBER: 333-23795`; S-1/A No. 5, 1997-05-14 l.49 `SEC FILE NUMBER: 333-23795` and l.79 `REGISTRATION
  333-23795` — same registration, same counsel (Perkins Coie / Wilson Sonsini, l.127-133), same auditor consent
  (Ernst & Young, EX-23.1, per the retrieval header l.6). Version-safety results from my own string checks:
  `up to 400,000` — 3 occurrences (one sentence, three printings); `license commercially available technology
  whenever possible` — 3; `repeat customers currently account for over 40% of orders` — 3 (original + A5 twice);
  the DEC/`3,000%` disclaimer — 2 (No. 3 + No. 5). **Examples where the filings genuinely disagree, and are
  therefore worth two citations:** 151 vs 158 at 1996-12-31 (S2E-26); 40% vs 58% repeat share; "out-of-print …
  two to six months" (A5 l.2272) vs "one to three months" (10-K l.343); "carries minimal inventory" (A5 l.2377)
  vs "Although the Company carries its own inventory" (10-K l.383); 43% post-IPO Bezos stake (original S-1) vs
  **41%** (S-1/A No. 5) — already registered in the supersession note at
  `research/E_supply_ops_finance.md` l.562, and correct.
- **Class.** FACT + METHOD RULE.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** "Appears in all three 1997 registrations" = **one** Tier-1 source with three
  printings. Where two of them disagree, say so; where they agree, do not multiply the corroboration count.

### S2E-28 — `2,613,000` is still circulating inside this project, and there is a fresh instance of the same disease in the IPO numbers

- **Standard narrative.** (internal) The 2,613,000/$871,000/$871,024 chain was retracted, so it is dealt with.
- **Challenge.** It is dealt with in `stage_1.md`, `conflicts.csv`, `quantitative.csv` and `data_gaps.csv` — and
  **not** in `context_appendices.md`, which still presents `$871,000 … (2,613,000 ÷ 3 = $871,000 exactly)` as a
  live component of the capital raised, in the same cell that recites the retraction of the *earlier* plug. A
  Stage-2 author mining the appendices will launder a retracted figure straight back into the spine.
- **Earliest source of the popular claim.** Internal (AUDIT 3 / number_repairs2 lineage).
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.**
  `context_appendices.md` l.596, verbatim: `≈$976,000 un-named = $5,408 (1995-08-07 employee purchase) + $150,000
  advances for unissued shares + **$871,000** unaffiliated program shares (2,613,000 × the filing's exact ⅓ =
  2,613,000 ÷ 3 = $871,000 exactly) − $50,000 of 1994 advances applied = **$976,408**…`
  Against `stage_1.md` l.1449-1452: `**$871,024**, a back-solved balancing plug … then … **$871,000** =
  2,613,000 ÷ 3 … **Both numbers rested on the same unfiled denominator** … `2,613,000` occurs in **none** of the
  four restored documents`. `conflicts.csv` U.8 RETRACTED-FIGURE RECORD: `THIS ROUND RETRACTS THE CHAIN AND
  SUBSTITUTES NO THIRD NUMBER`. Also `context_appendices.md` l.639 still describes `only ~$871,000 of it is
  anonymous share money`.
  **Independent re-test performed for Stage 2:** `grep -c "2,613,000"` across the four filings in `sources/` →
  **zero occurrences** (consistent with the register). Same test on the derived figures this review uses:
  `13.20` (dilution), `400,000`, `79` (working capital), `29,845` (AP), `75 million` (loan) are all *directly
  present* in the filing text at the lines cited above — no derivations on unfiled denominators are load-bearing
  anywhere in this document except where explicitly labelled DERIVED from two filed lines.
- **Class.** FACT (about this project's own files).
- **Confidence in the challenge.** **Certain.**
- **Best-supported reconstruction.** Apply COR-14's discipline to `context_appendices.md` §Capital row and l.639:
  strike the $871,000/2,613,000/$976,408 composition, leave the three filed legs totalling $105,408, and mark the
  balance UNKNOWN. Until that is done, **Stage 2 must draw no capital figures from context_appendices.md.**

### S2E-29 — the 1995 press release is still being credited with things it does not contain; the correct in-window carriers are the S-1 and a **local** telephone number

- **Standard narrative.** "By 1996 Amazon had nine mailboxes, a toll-free number and fax ordering, announced in
  its launch release."
- **Challenge.** **COR-13** proved the release contains none of the mailbox/toll-free/fax/e-mail-order details.
  For Stage 2 the corresponding facts are *filing* facts with a twist worth stating: the "nine" are **nine
  e-mail addresses**, not mailboxes; the toll-free line exists in the text but the only number the registrant
  prints anywhere is a **Seattle local** number; and fax ordering is not in the filings at all.
- **Earliest source of the popular claim.** Original S-1's Customer Service section (1997-03-24), restated in the
  amendments; then a 2025 essay restyling it. HistoryLink l.93ff and the widely-circulated "how people ordered in
  1995" posts are downstream.
- **Founder-originated?** Company-issued.
- **Contradicting or qualifying evidence.** S-1/A No. 5, 1997-05-14, l.2363-2369: `**Amazon.com offers nine
  e-mail addresses** to enable customers to request information and to encourage feedback and suggestions…
  **Amazon.com also offers a toll-free line for customers who are reluctant to enter their credit card numbers
  through the Web site.**` (identical at original S-1 l.2174 and l.2179-2180, per COR-13's line citations).
  The only telephone number the registrant prints: cover l.108 and l.118 and Summary l.488 —
  `(206) 622-2335` / `Its telephone number at that location is (206) 622-2335` — **not** a toll-free prefix.
  The 1995 press release's own number, per COR-13, is likewise `(206) 622-2335`.
  And ordering *method*, S-1/A No. 5 l.2255-2259: `To execute orders, customers click on the buy button and are
  prompted to supply shipping and credit card details, **either by e-mail or by telephone**.` — no fax, no mail.
- **Class.** FACT.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** Correct carriers: nine e-mail addresses and a toll-free line → original S-1
  (1997-03-24) / S-1/A No. 5 (1997-05-14); "customers order online, optionally by e-mail or telephone" → same;
  fax ordering → Knight Ridder, Nov 1995, Medium (COR-13) and nothing more.

### S2E-30 — the retrospective-quote trap is live for Stage 2 in three specific sentences

- **Standard narrative.** Quotable founder lines about 1996-97.
- **Challenge.** Every founder-state quote available for 1996-97 in this corpus is post-window, and two of the
  three carry **present-tense** constructions that read as if uttered in the window. If Stage 2 quotes any of
  them without its real date, it commits the COR-06 error at a new date range.
- **Earliest source of the popular claim.** Listed per sentence below.
- **Founder-originated?** Yes.
- **Contradicting or qualifying evidence.**
  **(a) Sheff/Playboy — conducted 1999, published 2000.** Local `sheff-playboy-interview_…txt` retrieval header
  l.7: `Publication / issue date : conducted 1999; published 2000 (Playboy)`. The dangerous present tenses are
  l.141 and l.145: `Bezos: … I mean, **in the scheme of things, we are still a tiny company**.` and
  `Bezos: **We are big for an Internet company but tiny for a real-world company.**` — a 1999 utterance that
  fits 1996-97 sentiment perfectly, which is exactly why it gets recycled. Also l.31, the writer's own
  retrospective market judgement: `Amazon.com's valuation based on its stock price was **ten times higher than
  that of Barnes and Noble**… it shot up from $18 a share to $100 a share a year later.`
  **(b) HistoryLink Essay 23230 — published 2025-04-07** (per COR-07), carrying 1996-97 *motive* claims with no
  citation: l.93 `It was 1996, and with money pouring in, Bezos adopted the ethos: **Get Big Fast**.`;
  l.90 `Doerr **was impressed by Bezos's energy and technical knowledge**… $8 million for a 13 percent stake in
  Amazon, which they valued at $60 million`; l.102 `write-ups about Amazon in the media got the attention of
  executives at Barnes & Noble, who **initiated a meeting with Amazon**… discussed Barnes & Noble's plan to
  launch its own website and possible ways the companies could partner`; l.111 `Amazon went public for $18 a
  share on **May 15, 1997**, and was **valued at $429 million**`.
  **(c) A 2011 engineer interview, relayed by a 2025 essay** (Stage-1 record F-62, sourced inside
  `historylink-essay-23230…txt`): the account of who built the first site.
  Cross-checks that show the trap is real: **(b) l.111's date conflicts with the company's own documents** — the
  press release is datelined **May 14, 1997** and the 10-K405 says the registration `became effective on May 14,
  1997`; May 15 is the first *trading* day. And **(b) l.114's capital claim is not the window's** — `Through a
  high-yield bond, the company brought on $326 million` does not correspond to any in-window financing; the
  retrieved FY1997 record shows instead a **$75 million senior secured term loan on 1997-12-23** plus
  **$49.1M** of IPO proceeds. A Stage-2 built on this essay would misdescribe the capital structure outright.
- **Class.** RETROSPECTIVE / FOUNDER CLAIM for all of it; **FACT** only for the document-dates themselves.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** For 1996-97 founder reasoning the honest line is COR-06's, extended forward:
  **no contemporaneous founder-state interview is known for 1996-97 either.** The only in-window founder words on
  the record are (i) the 1995-10-04 release quotation and (ii) the April 1997 newspaper report of Bezos **that
  the company itself disavowed** in the prospectus (S2E-22). Both are publicity, not recovered intention.

### S2E-31 — "$429 million valuation", "1996 sales of $15.7M proves traction", "1.5M customers": three numbers Stage 2 will be tempted to print, and their real status

- **Standard narrative.** 1997: valued at $429M, $15.7M of 1996 sales, 1.5M customers.
- **Challenge.** Each is defensible only with a label the narrative omits. The valuation is a *derivation* from
  a price times a share count that the final prospectus printed at a **different** price; the "$15.7M" is a
  nine-and-a-half-month-old number by IPO day; and "1.5M customers" is a registered-account count published in
  1998 about 1997.
- **Earliest source of the popular claim.** HistoryLink 2025 (l.111) for $429M; the 10-K405 for $1.5M; the S-1
  MD&A for $15.7M.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.**
  $429M: **DERIVABLE but not filed** — S-1/A No. 5 l.348 `Common Stock to be outstanding after this offering…
  23,858,702 shares`; 23,858,702 × $18 = $429.5M. **Amended after the 424B1 was restored:** the 424B1 carries
  **both** inputs in a single document — the $18.00 price on its cover (l.124-125) and the same
  `23,858,702 shares` in its Summary (l.228) — so the figure is now one-step arithmetic on one filing rather than
  cross-document. It is still **not filed as a valuation**, and it is still a *market-capitalisation-at-pricing*
  number, not a "company value" the registrant asserted. But the earlier objection (that it required pairing a
  No. 5 share count with a press-release price that No. 5 contradicted) is **withdrawn**; see failed attack
  **F-11**. Against: at No. 5's own $15.00 assumption the identical arithmetic gives **$357.9M**, so the figure is
  price-dependent and must always be printed as "× $18.00".
  $15.7M: `Net sales grew from $511,000 in 1995 to $15.7 million in 1996` (S-1/A No. 5 l.1507-1508) — true, and
  by the 1997-05-14 prospectus it had been superseded in-text three times over: Q1-1997 alone was `$16,005`
  thousand (l.379), i.e. **one quarter ≈ the whole of 1996**.
  1.5M customers: 10-K405 l.241-243, cumulative, and the same sentence's `sales of more than $164 million` is
  cumulative too (see S2E-20's subtraction).
- **Class.** DERIVED / FACT-with-stale-basis.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** Print $429M only as `23,858,702 shares (S-1/A No. 5) × $18 (press release
  1997-05-14) = ≈$429M market capitalisation at pricing — DERIVED, not filed`, and never let "$15.7M" appear
  beside "1997" without the Q1-1997 $16.0M next to it.

### S2E-32 — the quarterly record shows the loss accelerating *as* revenue scaled, which the annual framing hides

- **Standard narrative.** 1997's annual loss is a growth cost.
- **Challenge.** The unaudited quarterly table inside the same prospectus shows loss per quarter rising with each
  quarter's revenue through the whole window. If scale were producing operating leverage, the loss/share line
  would flatten; it steepens.
- **Earliest source of the popular claim.** Not applicable.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.** S-1/A No. 5, Selected Financial Data (unaudited quarterly columns),
  l.374-385: net sales `875 | 2,230 | 4,173 | 8,468 || 16,005` and net loss `(331) | (767) | (2,380) | (2,299) ||
  (3,038)` for Q1/Q2/Q3/Q4 1996 and Q1 1997; loss per share `(0.02) | (0.03) | (0.10) | (0.10) | (0.13)`.
  **DERIVED:** loss as % of that quarter's sales = 37.8% (Q1-96), 34.4% (Q2), 57.0% (Q3), 27.1% (Q4), 19.0%
  (Q1-97) — the ratio improves, the **dollars** never stop growing, and Q4-1996's apparent improvement is a
  Christmas quarter the same prospectus flags as structurally unrepresentative: `sales in the traditional retail
  book industry are significantly higher in the fourth calendar quarter of each year than in the preceding three
  quarters` (l.607-609). Any "run-rate" computed off Q1-1997 or Q4-1996 is a category error the filing itself
  warns against; and the filing adds the general warning `period-to-period comparisons of its operating results
  are not necessarily meaningful and should not be relied upon as an indication of future performance`
  (l.547-551).
- **Class.** FACT + DERIVED.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** Stage 2 should show the quarterly table, not just the annuals, and should
  state that the company disclaimed its own run-rates in writing.

### S2E-33 — the revenue line contains the customer's shipping payment, so every "average order" figure is inflated by postage

- **Standard narrative.** Unit economics proved themselves in 1996-97.
- **Challenge.** "Net sales" is defined to include **outbound shipping and handling charges paid by customers**,
  while cost of sales includes **inbound** as well as outbound shipping. So revenue and margin are already
  mixed with a postal pass-through, and Stage 2 cannot compute an order value or a shipping-subsidy claim from
  these lines without saying so.
- **Earliest source of the popular claim.** Analyst practice; not on the in-window record.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.** S-1/A No. 5 MD&A l.1505-1507: `Net sales are comprised of the selling
  price of books and other merchandise sold by the Company, **net of returns, as well as outbound shipping and
  handling charges.**` l.1513-1515: `Cost of sales consists primarily of the costs of merchandise sold to
  customers and **outbound and inbound shipping costs.**` 10-K405 l.1406-1408 repeats both definitions and
  attributes the 1997 margin fall partly to `lower overall shipping margins` (l.1410).
  Also relevant to any "quality of demand" claim: revenue is **net of returns**, but **no returns figure appears
  in any of the four filings** (searched), while returns are listed as a driver of variability: `(xi) the level of
  merchandise returns experienced by the Company` (S-1/A No. 5 l.599).
- **Class.** FACT.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** Report the accounting definitions beside every 1996-97 economics number, and
  treat shipping as a first-order term in the story, not a footnote — it is where the 1997 margin went.

### S2E-34 — BOUNDARY ATTACK (i): Stage 2 should end at **1996-12-31**, not at the IPO

- **Standard narrative.** Stage 2 ends at the May 1997 IPO.
- **Challenge — the strongest case available.** The IPO is a *financing* event on a *capital-markets* calendar.
  Everything the stage is supposed to establish — repeatability — is on the record twelve weeks earlier, in the
  only period with a complete audited year: (a) FY1996 net sales $15,746K against FY1995's $511K, a full year
  after a partial one; (b) **1996 is the first complete post-launch year**, so 1995 ($511K, $920K working
  capital) and 1996 ($15,746K, $2,270K working capital, $6,248K cash) are the first pair whose comparison means
  anything — 1995 covers only ~6 months of selling (S-1/A No. 5 l.1449: `opening of the Amazon.com bookstore in
  July 1995 through December 31, 1995`), so every 1995-vs-1996 growth number in the window is partly an
  artefact of the elapsed-time difference rather than a rate of demand;
  (c) `Ingram … accounted for 59% of the Company's inventory purchases in 1996` — the supply arrangement is
  measurable for a whole year; (d) `11 to 151 employees` across exactly CY1996; (e) the repeat-purchase and
  traffic series both close at December 1996. The IPO then belongs to Stage 3 as a *consequence*.
  **A further argument for this boundary was drafted and withdrawn on checking:** that 1996 was the first year in
  which the same seasonal cycle could be compared with a prior one (Q4-1995 vs Q4-1996). It is not available —
  the quarterly table in S-1/A No. 5 (l.374-385) begins at **Q1 1996**, so no Q4-1995 column exists in any
  retrieved document, and there is therefore **no two-Christmas comparison anywhere inside the window.** Recorded
  as failed attack **F-9**; note that this withdrawal *weakens* the 1996-12-31 case and, by the same reasoning,
  removes the seasonal-repeat argument from every boundary option.
- **Earliest source of the framing.** Project convention, not a source.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.** Supporting: S-1/A No. 5 l.379/l.1507 (FY1996 $15,746K), 10-K405
  l.1211 (`Working capital (deficiency)… 93,517 2,270 920 (16)` — the 1996-12-31 entry is **$2,270K**, with
  $920K at 1995-12-31 and $(16)K at 1994-12-31 — **a caution for this attack: on the 10-K's basis, 1996 year-end
  working capital is $2,270K, not the $920K that belongs to 1995.** The columns must be read in order), l.388-389
  (59% in 1996), original S-1 (11→151 across CY1996).
  Against: the FY1996 audited year was *published* only in 1997, so the "evidence" and the "event" share a
  document; and the window's richest operating facts — the 400,000-of-2.5M fill ratio, the out-of-print service,
  the Gift Center, the $75M loan, the B&N suit — all sit **after** 1996-12-31.
- **Class.** ARGUMENT on FACT evidence.
- **Confidence in the challenge.** **Medium-High** as a boundary claim; **high** that it is the most defensible
  alternative to the IPO.
- **Best-supported reconstruction.** 1996-12-31 is the right end of *Stage 2a* (repeat year) but truncates the
  repeatability test before anyone outside the company could observe it.

### S2E-35 — BOUNDARY ATTACK (ii): Stage 2 should end at **1997-12-31** (or 1998-03-30), because that is the first date at which the model was externally tested

- **Standard narrative.** (as above)
- **Challenge.** Repeatability is not demonstrated by a company's own prospectus but by third parties who can
  walk away. Two such tests happen inside 1997 and after the IPO: the **1997-12-23 $75M senior secured term
  loan**, underwritten by lenders who imposed covenants on cash balance, EBITDA, **accounts-payable aging** and
  capital spending (10-K405 l.858-868) — i.e. sophisticated outsiders who saw the float model as the risk and
  priced it; and the **audited FY1997 annual report** itself (1998-03-30, filed as **10-K405**, a late-filing
  delinquency form per COR-01). On this reading the IPO is noise and the year-end is the signal.
- **Earliest source of the framing.** Project convention.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.** Supporting: as cited, plus `Long-term debt, net of current portion…
  76,702` at 1997-12-31 against `--` in every prior year (l.1213), and the warrant sweetener: `the Company
  issued warrants to purchase a total of 750,000 shares… The warrants will be canceled if the Company repays the
  Loan… The exercise price for the warrants is $52.11 per share` (l.1142-1152) — lenders needed equity upside to
  lend, which is not the behaviour of a bank backing a proven model.
  Against: 1997-12-31 pulls the FY1998 events (music store 1998-06-11, the 1998 stock collapse) toward the
  boundary, and the delinquent filing form (10-K**405**) means the annual report's own reliability is qualified
  by its lateness — which cuts against using it as a boundary marker.
- **Class.** ARGUMENT on FACT evidence.
- **Confidence in the challenge.** **Medium-High.**
- **Best-supported reconstruction.** This is the strongest *alternative* boundary, and its real virtue is that it
  forces Stage 2 to carry the December-1997 loan, which the IPO boundary tends to drop.

### S2E-36 — BOUNDARY ATTACK (iii): if "repeatability" is the test, the boundary is **1998-06-11** — and the IPO fails the test

- **Standard narrative.** The IPO is the first hard evidence of repeatability.
- **Challenge.** A stage boundary should mark the thing the stage is about. Stage 2 is about *repeatability*, and
  the first hard, dated, public evidence that the model repeated in a second category is the **music store
  opening**, which is thirteen months after the IPO: `SEATTLE, Wa (June 11, 1998) … "expanded Earth's Biggest
  BookstoreSM today to include music" … "more than 125,000 music titles" … "It's a music discovery machine"`.
  Until then, every expansion statement in the record is the word "intends". If Stage 2 stops at the IPO, it
  stops **before** the claim it is supposed to certify.
- **Earliest source of the popular claim.** N/A.
- **Founder-originated?** Company-issued press release.
- **Contradicting or qualifying evidence.** Supporting: press release retrieved 2026-09-24,
  https://press.aboutamazon.com/1998/6/amazon-com-opens-music-store-provides-a-whole-new-way-to-discover-music
  (indexed 1998-06-10, **datelined 1998-06-11** — cite both, per COR-11(4)'s two-date rule); against the IPO as
  boundary, S-1/A No. 5's own purpose statement (S2E-12) and 10-K405 l.235-236 (`intends … such as music`).
  Counter-consideration for Stage 2's *near-death* variant: the same essay that supplies the 1998-2000 collapse
  narrative also shows the 1998 turn (l.114-120) — but the first in-window signal of that vulnerability is the
  December-1997 covenant package (S2E-35), so 1998's fragility is already legible at 1997-12-31.
- **Class.** FACT + ARGUMENT.
- **Confidence in the challenge.** **Medium** as a boundary recommendation, **High** that the IPO cannot
  *itself* be evidence of category repeatability.
- **Best-supported reconstruction.** Keep the boundary inside 1997, but do not let the IPO stand in for
  repeatability; if repeatability is the certification, the certification is unissued in 1997.

### S2E-37 — THE CASE THAT THE IPO IS THE RIGHT BOUNDARY (argued on the evidence, not the calendar)

- **Challenge to my own attacks.** Three properties make 1997-05-14/15 the best single cut available. (1) **It
  converts self-report into attestation.** Everything before is company narrative; the registration statement is
  signed, audited (Ernst & Young consent, EX-23.1, on the No. 5 accession) and carries Securities Act liability —
  which is precisely why the *uncomfortable* facts in this review (400,000 of 2.5M; 59% one supplier, no
  contract; $79K working capital; $13.20 dilution; the DEC disclaimer) are all findable there. (2) **It is a
  real resource discontinuity.** Working capital $79K actual → $41,079K pro-forma-as-adjusted at the same
  balance-sheet date (S-1/A No. 5 l.397); cash $7,162K → $48,162K; long-term obligations $0 before and after
  (l.1244). No operating event in the window changes the balance sheet by that multiple. (3) **It is externally
  observable and uniquely dated** — `became effective on May 14, 1997` (10-K405 l.1125), pricing announced
  `SEATTLE, WA (May 14, 1997) … at a price of $18 per share` (press release), and the **prospectus itself is
  dated and filed 1997-05-15** (424B1, acc. 0000891020-97-000868: `prospectus dated May 15, 1997`) — whereas
  1996-12-31 is a fiscal convention and 1998-06-11 belongs to the next stage's subject matter.
  **Refinement forced by the 424B1:** the boundary is best expressed as a **three-date cluster**, not a day —
  **1997-05-14** (registration effective + pricing announced), **1997-05-15** (final prospectus dated/filed, and
  the first trading day). Any Stage-2 sentence that picks one date without saying which event it means is
  ambiguous, and the popular "May 15 IPO" is defensible **only** for the prospectus date and the trading day —
  which retroactively *vindicates* the HistoryLink essay's "May 15" (W-2) on that one point while leaving its
  "$429 million" and "Get Big Fast" items unsourced.
- **Class.** ARGUMENT on FACT evidence.
- **Confidence.** **High.**
- **Best-supported reconstruction.** Adopt the IPO, **dated 1997-05-14 for pricing/effectiveness with 1997-05-15
  as first trading day, cited to the press release and the FY1997 10-K respectively** — and treat "the model
  repeated" as a claim Stage 2 *does not close*, deferring it to Stage 3 with the December-1997 loan as the
  hinge.

### S2E-38 — ADJUDICATION, and which position rests on the weakest document

- **Ruling.** Stage 2 ends at the IPO (1997-05-14/15) as the *boundary*, with **1997-12-31 as a mandatory
  sub-endpoint that Stage 2 must narrate anyway** (FY1997 audited close + the $75M covenant loan), because on
  the evidence the IPO is a resource discontinuity and **not** a repeatability certification.
- **Weakest-document audit of this review's own conclusions.**
  1. **S2E-35/S2E-36's boundary cases rest on the FY1997 10-K405** — a form filed **late** with a delinquency
     cover (COR-01: "form **10-K405**, not a plain 10-K"). Its FY1997 loss, cash-flow, 58%-repeat, 614-employee
     and 158-headcount numbers are all inside it. It is audited, but the *form* is the corpus's weakest
     load-bearing document, and the 151-vs-158 conflict is inside it (S2E-26).
  2. **S2E-23/S2E-24 (competitor moves) rest on tier-3 encyclopedia company histories** and one 1997 newspaper
     column — my weakest retrieval by design (web budget), and explicitly flagged for verification against B&N's
     and Borders' own filings.
  3. **S2E-19's $18 rests on a company press release** — contemporaneous and primary, but self-issued.
  4. **S2E-30's B&N-meeting claim rests on a 2025 essay** and is therefore excluded from the record as evidence,
     listed only as folklore.
- **Class.** METHOD.
- **Confidence in the challenge.** **High** as a ruling; the caveats are the point.
- **Best-supported reconstruction.** Say out loud in the Stage-2 text that the boundary marker and the
  repeatability test are different events, and that the strongest year-end evidence sits in a document the
  company filed late.

### S2E-39 — nothing in the record measures whether orders were filled

- **Standard narrative.** Amazon's service was famously good, which is why it grew.
- **Challenge.** Across four filings covering 1995-1997 there is **no order count, no fill rate, no cancellation
  rate, no backorder rate and no returns figure** — the four quantities that would show whether the advertised
  catalogue converted. The only related disclosures are warnings. That is not a neutral silence: the company
  could measure it and did not publish it, while competitors' suits and press anecdotes went the other way.
- **Earliest source of the popular claim.** Customer-service mythology; Stage-1 record F-58 (HistoryLink's
  order-bell anecdote) is the folk version.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.** Documented nulls from my greps of the four filings: no `order fill`,
  no `unfilled`, no `cancel`-rate line; `(ii) the Company's ability to manage inventory and fulfillment
  operations` and `(xi) the level of merchandise returns experienced by the Company` appear only as
  variability factors (S-1/A No. 5 l.587, l.599); the fulfilment quality statement is a promise — `The Company
  seeks to provide rapid and reliable fulfillment… and intends to continue to improve its availability and
  fulfillment in the future` (l.2278-2280); and the price escalation mechanism proves estimates were wrong often
  enough to warrant a procedure: `If a hard-to-find book is discovered to have a price higher than an estimate
  previously provided to the customer, the Company notifies the customer and seeks approval for sale at the
  higher price` (l.2276-2278).
- **Class.** DOCUMENTED NULL + FACT.
- **Confidence in the challenge.** **High** for the null (four filings searched); the "not neutral" reading is
  **INFERENCE**.
- **Best-supported reconstruction.** Stage 2 must state that order-level fulfilment performance in 1996-97 is
  **unquantified in the primary record**, and go get it from complaint archives or press (see `## Data gaps`,
  D-1, which I searched and did not find).

### S2E-40 — the dispute trail thins exactly when it should thicken: the B&N suit disappears between filings

- **Standard narrative.** Legal challenges to Amazon were trivial.
- **Challenge.** A claim disclosed in an audited filing's notes on 1997-05-14 is **not carried into Item 3 of
  the FY1997 annual report**, which reports no pending material litigation at all. Either it resolved quietly —
  which is itself a fact Stage 2 should date — or it fell below a materiality threshold set by the same company.
- **Earliest source of the popular claim.** Not applicable.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.** Present: S-1/A No. 5 Note 5, l.4409-4415 (S2E-09). Absent: 10-K405
  Item 3, l.1085-1092: `From time to time, the Company is subject to legal proceedings and claims in the
  ordinary course of business… **The Company currently is not aware of any legal proceedings or claims that the
  Company believes will have, individually or in the aggregate, a material adverse effect**…` — and the FY1997
  10-K contains **no** reference to the B&N suit (grep for "Barnes" in that document returns only the two
  competitor lists at l.445 and l.652).
  Also absent from the in-window record: **any dispute with a publisher or distributor.** Searched for in all
  four filings; nothing. What exists is the dependency language (S2E-05) and the forward-looking "maintain and
  expand its relationships with various distributors and publishers" (S-1/A No. 5 l.810-812).
- **Class.** DOCUMENTED NULL + FACT.
- **Confidence in the challenge.** **High** that the disclosure pattern changed; **unknown** why.
- **Best-supported reconstruction.** Stage 2 should carry "B&N v. Amazon filed 1997-05-12; **not** disclosed in
  the FY1997 annual report; disposition undetermined on retrieved evidence" and chase the outcome (PACER/press).
  The later pattern is instructive and out-of-window: by October 1999 **Amazon** was the plaintiff over a
  one-click patent (`Amazon Sues Big Bookseller Over System For Shopping`, The New York Times, 1999-10-23,
  https://www.nytimes.com/1999-10-23/business/amazon-sues-big-bookseller-over-system-for-shopping.html), and the
  B&N history records `Its suit claimed that barnesandnoble.com's Express Checkout system violated its patent` —
  i.e. the technology moat appears as litigation only in 1999, twelve months of patent pendency after the
  1997-09-12 application. Cite as consequence, never as window evidence.

### S2E-41 — "growth proves the market chose them": the filing's own international and margin trend points the other way on one dimension

- **Standard narrative.** Global demand validated the model.
- **Challenge.** International share **fell** through the window — 39% (1995) → 33% (1996) → 25% (1997) — even
  as international *reach* ("over 100 countries", "over 150 countries") expanded. The growth that mattered in
  1996-97 was domestic, and the international mix is precisely where shipping cost sits.
- **Earliest source of the popular claim.** Marketing language ("worldwide"), plus the country-count lines.
- **Founder-originated?** Company-issued.
- **Contradicting or qualifying evidence.** S-1/A No. 5 MD&A l.1510-1511: `International sales represented
  approximately **39% and 33% of net sales in 1995 and 1996**, respectively.` 10-K405 l.244-245:
  `International sales represented **25% of net sales in 1997 and 22% of sales in the quarter ended December 31,
  1997.**` And `No foreign country accounted for more than 10% of revenue` (l.247). Country-count growth
  (`over 100 countries` → `over 150 countries`) is a breadth measure, not a revenue measure; the two must not be
  used for each other.
- **Class.** FACT + DERIVED trend.
- **Confidence in the challenge.** **High** on the numbers; **Medium** on the shipping-cost inference (the
  filings do not break margin down by geography, though they do name `lower overall shipping margins`, S2E-33).
- **Best-supported reconstruction.** 1996-97 growth was US-weighted; the "global bookstore" is a reach statistic.
  Print the three-year international series next to the country counts.

### S2E-42 — the 4,000%/3,000% growth folklore has an in-window paper trail, and it runs through a vendor advertisement, not a filing

- **Standard narrative.** "Amazon grew 4,000% in 1995/1996."
- **Challenge.** COR-09 already bars "2,300%". Stage 2's exposure is the *adjacent* number: **3,000%**, which is
  real, in-window, and worthless as evidence — it is a **Digital Equipment Corporation advertisement**, quoted
  and rejected inside Amazon's own prospectus. The filed arithmetic gives something quite different: FY1996
  growth of **2,981%** on net sales ($15,746K ÷ $511K − 1) and FY1997 of **838%** — so the folklore is not far
  off for 1996, and the story is not that the number is wrong but that **it was a vendor's headline and the
  registrant disclaimed the trend, not the digit.**
- **Earliest source of the popular claim.** DEC advertisement, 1997 (quoted at S-1/A No. 5 l.767-771); Sheff's
  1999/2000 narrative carries the compounded version (`an 841 percent growth from the year before`, l.25).
- **Founder-originated?** No — vendor-originated, company-disclaimed.
- **Contradicting or qualifying evidence.** S-1/A No. 5 l.767-771 (quoted in S2E-22); the filed series at
  l.379; **DERIVED** 15,746/511 = 30.8× (1995→1996) and 147,758/15,746 = 9.4× (1996→1997) — note Sheff's "841
  percent" matches the 10-K's 9.4× and so is *accurate*, which is exactly why retrospective prose is dangerous
  here: it gets the arithmetic right and the causation wrong.
- **Class.** FACT + DERIVED.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** Cite growth from the filed revenue lines; if 3,000% appears at all, appear
  it with the company's own rejection attached.

### S2E-43 — the fulfilment milestone Stage 2 is missing: November 1997, and the sentence that ends the asset-light story

- **Standard narrative.** Amazon stayed asset-light throughout the window; that is why it could out-price
  bookstores.
- **Challenge.** The window contains an explicit, dated reversal of that model, disclosed as a *plan to keep
  doing it*: a 200,000-square-foot distribution centre opened in **November 1997**, and an announced intention
  to **keep increasing merchandise inventory** in order to fix the availability problem S2E-08 documents. The
  Stage-1 mechanism (own nothing, buy per order) is not carried intact to the end of Stage 2, and if the stage
  is cut at the IPO that reversal falls out of the reconstruction entirely.
- **Earliest source of the popular claim.** The "asset-light infinite shelf" reading of Amazon, which is
  supported by the pre-IPO text (`The Company carries minimal inventory`, S-1/A No. 5 l.2377) and by later
  platform mythology.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.** 10-K405 FY1997 MD&A, 1998-03-30, l.1646-1653:
  `**In November 1997 the Company opened a 200,000-square-foot distribution center in Delaware and expanded its
  Seattle distribution center to 85,000 square feet.** The Company may establish one or more additional
  distribution centers within the next 12 months, which would require it to commit to lease obligations, stock
  inventories, purchase fixed assets and install leasehold improvements. **In addition, the Company has
  announced plans to continue to increase its merchandise inventory in order to provide better availability to
  customers and achieve purchasing efficiencies.**`
  Item 2 Properties, l.1069-1075: `…principal administrative, engineering, marketing and customer service
  facilities total approximately **88,000 square feet**… warehousing and merchandising operations are housed in
  an approximately **85,000-square-foot facility in Seattle**… and in a **200,000-square-foot facility located in
  New Castle, Delaware** under a lease that expires in October 2002.`
  Against the pre-IPO text, S-1/A No. 5 FACILITIES l.2591-2600: `…facilities total approximately **42,400 square
  feet**… warehousing and merchandising operations are housed in an approximately **50,000-square-foot facility**
  in Seattle… The Company does not own any real estate.`
  **DERIVED:** warehousing square footage 50,000 (May 1997) → 285,000 (Dec 1997) = **5.7× in seven months**;
  and the inventory cash outflow of **$8,400K** in 1997 vs **$554K** in 1996 (l.2041).
- **Class.** FACT + DERIVED.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** Stage 2's true operational climax is not 1997-05-14 but the
  November-1997/December-1997 pair: the company answered its own availability problem with buildings, stock and
  a secured loan. Write the model as *changing*, not as *proven*.

### S2E-44 — what was actually purchasable on a date, and the one flagship program whose date is not in the record at all

- **Standard narrative.** 1996-97 saw Amazon ship out its product roadmap: Associates, the 500, out-of-print,
  gifting.
- **Challenge.** Only three of those are dateable **from an in-window document**, and the most-cited one —
  the Associates Program — is **never dated anywhere in the four filings**. Its familiar "July 1996" comes from
  a company self-narrative archived in **2007** (Stage-1 record F-69). A stage that lists 1996 launches must
  either date them from the record or mark them undated; importing the 2007 timeline as a 1996 source is a
  COR-07-class error.
- **Earliest source of the popular claim.** Amazon corporate history timeline (corporate-ir.net), Wayback
  capture **2007-10-27**: `July 1996 — Launches Amazon.com Associates Program.`
- **Founder-originated?** Yes (company self-narrative, retrospective).
- **Contradicting or qualifying evidence.** Dated **in-window** (10-K405 / S-1/A No. 5):
  `In **March 1997**, the Company began discounting the Amazon.com 500 and other featured books by 40% from list
  price` (S-1/A No. 5 l.1522-1523);
  `Amazon.com began offering an **out-of-print book service in March 1997**` (S-1/A No. 5 l.2282-2283; restated at
  10-K405 l.329-330);
  `In **November 1997**, Amazon.com launched its **Gift Center**` (10-K405 l.323);
  `**In November 1997** the Company opened a 200,000-square-foot distribution center` (l.1646).
  Undated in-window: `The Company extends its market presence through its Associates Program, which includes
  several thousand enrolled members` (S-1/A No. 5 l.2335-2336) — grep of every `Associates` occurrence in all
  four filings returns **no launch date**.
  Still intent at the FY1997 close: `intends to add a collaborative filtering service` (l.2247);
  `intends over time to expand its catalog into other information-based products, such as music` (10-K l.235-236).
  First hard out-of-window proof of the second category: press release datelined **June 11, 1998**
  (`expanded Earth's Biggest BookstoreSM today to include music`, `more than 125,000 music titles`), retrieved
  2026-09-24, https://press.aboutamazon.com/1998/6/amazon-com-opens-music-store-provides-a-whole-new-way-to-discover-music
  — index date 1998-06-10, dateline 1998-06-11: cite both, per COR-11(4)'s two-date rule.
- **Class.** FACT + DOCUMENTED NULL.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** The dated 1996-97 expansion list is exactly four items — Amazon.com 500
  pricing (March 1997), out-of-print service (March 1997), Gift Center (November 1997), second distribution
  centre (November 1997). **All four are book-adjacent or book-infrastructure.** None demonstrates a repeated
  *category*, and the earliest category test is 1998-06-11.

---

### S2E-45 — CONSOLIDATED FINDING: what made failure still entirely plausible at the end of Stage 2

- **Standard narrative.** By the end of Stage 2 Amazon had crossed over; the risk story is about whether growth
  was too fast, not whether the firm survived.
- **Challenge.** Set out as a single checklist of in-window, dated conditions, all of which are individually
  fatal-looking and none of which the record resolves inside the window. Failure at 1997-12-31 required only one
  of the following, and the company had all of them at once.
- **Earliest source of the popular claim.** The retrospective "1997 = the year Amazon became Amazon" framing,
  available in any post-2010 IPO anniversary piece; within this corpus, the nearest in-window articulation is the
  S-1/A No. 5's own growth preamble (l.473-476).
- **Founder-originated?** No.
- **Contradicting or qualifying evidence — the eight conditions, all in-window:**
  1. **Solvency was rented, not owned.** $79K working capital at 1997-03-31 (S2E-03); operating "cash" of +$3.5M
     in 1997 composed of +$29.8M payables (S2E-02); accumulated deficit $33.6M at 1997-12-31 against $28.5M of
     book equity (10-K l.1214, l.1837).
  2. **One supplier, no contract, after a year of scale.** Ingram at 58% of 1997 purchases (was 59% in 1996),
     `no long-term contracts or arrangements with any of its vendors that guarantee the availability of
     merchandise, the continuation of particular payment terms or the extension of credit limits` (S2E-05).
  3. **The promise was still only ~16% fillable.** 400,000 distributor-supplied of >2.5M offered (S2E-08), and
     the fix announced for 1998 was to `continue to increase its merchandise inventory` (S2E-43) — capital the
     company did not have pre-IPO.
  4. **Unit economics went backwards.** Gross margin 22.0% (1996) → 19.5% (1997), with marketing at 26.4% of
     sales; the company had forecast the decline in May 1997 (`will reduce gross margins below those experienced
     during 1995 and 1996`, S-1/A No. 5 l.1526-1528).
  5. **Single point of physical failure, unmitigated.** `Substantially all of the Company's computer and
     communications hardware is located at a single leased facility in Seattle… does not presently have redundant
     systems or a formal disaster recovery plan` (S2E-04); `The Company currently processes all sales through its
     warehouse in Seattle` (S-1/A No. 5 l.2398-2399) — only partly relieved by the November-1997 Delaware site.
  6. **A management team measured in months.** `The majority of the Company's senior management joined the
     Company within the last five months` (as of 1997-05-14); no CIO; no long-term employment agreements; no key
     person insurance; and admitted difficulty hiring the engineers the story needs.
  7. **Distribution was rented too.** Demand bought from Yahoo!/CNET/Excite/Lycos/Pointcast/Quote.com/CNN, with
     the company itself naming the risk that those gatekeepers `could promote the Company's competitors or charge
     the Company a substantial fee for inclusion` (S2E-17, S2E-18).
  8. **And the new money came with a handler.** 1997-12-23: $75M senior secured, covenants on minimum cash,
     EBITDA, **accounts-payable aging** and capex, plus 750,000 warrants at $52.11 that cancel on early
     repayment; `The Company's ability to generate planned future revenues, and therefore its ability to comply
     with the Loan covenants, may be affected by events beyond its control. If the Company were unable to satisfy
     the Loan covenants, the lending institutions would be entitled to exercise their remedies, including the
     right to declare all principal and interest immediately due and payable. If the Company were unable to make
     such payment… **the lending institutions could foreclose on the Company's assets, substantially all of which
     are pledged as security for the Loan**` (10-K l.875-884); dividends prohibited (l.1119-1120). **At the close
     of Stage 2, essentially every asset the company owned secured a three-year loan.**
- **Class.** FACT (each item) + INFERENCE (the aggregation).
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** What Stage 2 legitimately establishes is that **demand and revenue
  repeated**, and that by 1997-12-31 the company had bought a year of survival with IPO cash and secured debt.
  What it does not establish is that the *economics* repeated: at the boundary the model was still
  supplier-credit-financed, still single-vendor, still one-building, still 16% reliably fillable, still losing
  more dollars every quarter, still run by a five-month-old management team, and now additionally subject to
  lender covenants. **Failure remained not merely possible but arithmetically live; the difference between 1996
  and 1997 is the size of the hole and the length of the runway, not the sign of the result.** The honest Stage-2
  verdict is that the repeatability claim transfers to Stage 3 and is tested there by the 1998 category
  launches, not the 1997 ticker.

---

### S2E-46 — two stock splits inside the window make every per-share figure basis-dependent, and nothing in the record warns the reader

- **Standard narrative.** 1996-97 price and share figures can be compared directly across documents.
- **Challenge.** There were **two** splits in the window — four-for-one effective **1996-11-23** and
  three-for-two effective **1997-04-18** — so a 1995 per-share price, a 1996 private-placement price and the
  May-1997 IPO price sit on **three different bases** unless restated. Stage 2 will be tempted to line up
  "founder shares at $0.001", "Series A at $14.05" and "IPO at $18" as a single ascending price series. That
  series is meaningless as printed, and the correction that makes it meaningful is the company's restatement
  convention, not arithmetic the reader can invent.
- **Earliest source of the popular claim.** Financial-press IPO retrospectives that print unadjusted price
  ladders.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.** S-1/A No. 5, Note 6 Subsequent Events, l.4440-4443:
  `On **April 18, 1997**, the Company effected a **three-for-two common stock split**… The accompanying
  financial statements **have been restated** to reflect the three-for-two common stock split.`
  Note (pre-IPO), l.4172-4174: `On **November 23, 1996**, the Company effected a **four-for-one common stock
  split**. The accompanying financial statements have been restated to reflect this stock split.`
  Cover/summary caveats, l.299-301: `…the conversion of the Company's Preferred Stock into **six shares of
  Common Stock** upon the closing of this offering, (iii) gives effect to a **four-for-one stock split** of the
  Company's… Common Stock…` and l.4638-4639: `a four-for-one stock split… effective November 23, 1996 and a
  **three-for-two stock split**…`
  10-K405 Note, l.2443-2456: `In **June 1996**, the Company issued **569,396 shares of Series A convertible
  preferred stock at a price of $14.05 per share**. In **January and February 1997**, the Company sold an
  additional **5,000 shares of Series A preferred stock at $40 per share**. …at a rate of **six shares of common
  stock for one share of preferred**… all of the preferred stock outstanding was converted into an aggregate of
  **3,446,376 shares of common stock**.` — **DERIVED check:** $14.05 × 569,396 = **$8,000,014** and
  $40 × 5,000 = **$200,000**, reproducing exactly the two aggregates COR-10 flagged as *outside Stage 1*; both
  are **inside Stage 2**, and 574,396 × 6 = 3,446,376 confirms the ratio. **Caveat this review will not resolve:**
  whether the printed $14.05 / $40 are on the pre-split or restated basis is not stated, so **no cross-year
  per-share price ladder may be published** until that is settled (D-16).
- **Class.** FACT + DERIVED; the ladder is **BLOCKED PENDING**.
- **Confidence in the challenge.** **High** on the trap; **Low** on any attempted fix without the pre-split
  documents.
- **Best-supported reconstruction.** Print the splits as two dated events in the Stage-2 chronology (they belong
  there anyway — they are the 1996-97 capital calendar), and refuse the price-ladder sentence.

### S2E-47 — control was conditional: the founder's own shares were repurchaseable until **June 21, 1999**

- **Standard narrative.** Through the IPO Bezos controlled Amazon outright and unconditionally.
- **Challenge.** He did hold ~41-51% of the vote (S2E-12), but the June-1996 Series A that brought KPCB on also
  put **the founder's own common stock under a repurchase right at $0.001**, lapsing over 36 months to
  **June 21, 1999**. Stage 2's "consolidated founder control" line should carry that condition, because it is
  evidence of what the outside money actually demanded in 1996 — and it is a documentable fact that the
  reconstruction will otherwise smooth out.
- **Earliest source of the popular claim.** N/A — this is an omission.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.** S-1/A No. 5, l.4176-4181: `In conjunction with the sale of Series A
  preferred stock in **June 1996**, **the Company's founder granted the Company a right to repurchase 612,000
  shares of common stock held by him at the original purchase price of $0.001 per share if his employment
  terminates under certain circumstances. The Company's right of repurchase lapses ratably over the 36-month
  period ending June 21, 1999. At December 31, 1996, 510,000 shares held by the founder were subject to
  repurchase** under this agreement.` Employees were bound similarly: l.4196-4198 `Shares issued upon exercise of
  options that are unvested are subject to **repurchase by the Company upon termination of employment or
  services**`, and options under the 1994 Plan `become exercisable immediately and vest at the rate of 20% after
  year one…`
- **Class.** FACT.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** Amazon's 1997 control structure was founder-majority **and**
  founder-retention-contingent. Say both.

### S2E-48 — employee departures: no count exists, but the filings show the retention device, and one search is a real null

- **Standard narrative.** The 1996-97 team stayed together and scaled.
- **Challenge.** The primary record contains **no** attrition, resignation or departure figure for 1996-97 — so
  any Stage-2 sentence about the team's continuity is unsupported either way. What the filings do give is the
  machinery built because departures were expected (S2E-47) and the option-reservation arithmetic that a wave of
  departures would show up in.
- **Earliest source of the popular claim.** Founder-team continuity stories in retrospective accounts.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence.** Documented null across all four filings: no termination, attrition or
  resignation statistics. Present instead: `15,688,925` shares / `72.3%` held by all directors and executive
  officers as a group of **14 persons** (S-1/A No. 5 l.3160-3161 — **DERIVED: 14 people held 72.3% before the
  offering**), `4,800,000 shares… reserved under the 1994 Plan` (l.4188) and `6,000,000 shares… reserved` under
  the 1997 Plan (l.4421), and the 1997-02 adoption of that plan (Note 6, l.4420). External search for
  1996-97 departures: **SEARCHED-NULL** (1 query; results returned only 2022-present attrition stories).
- **Class.** DOCUMENTED NULL.
- **Confidence in the challenge.** **High** on the null.
- **Best-supported reconstruction.** Record "no departure data exists for 1996-97 in the primary record" as a
  finding, and use the repurchase/option machinery as the *inferior* but real evidence that retention was a live
  design problem.

### S2E-49 — the launch/first-sale chain has to be re-dated in Stage 2, and Stage 2's own record is cleaner than Stage 1's

- **Standard narrative.** "Amazon launched in July 1995 and sold its first book on July 16, 1995."
- **Challenge.** The first-sale date is **barred** (COR-09), and Stage 2 does not need it — but Stage 2 inherits a
  related 1997-specific trap: the annual report's launch phrasing is *not* the same sentence as the prospectus's,
  and the two are quotable for different things. If Stage 2 writes "opened for business in July 1995" it should
  cite the 10-K; if it writes "commenced offering products for sale" it should cite the prospectus; and the
  "first book title" story is a **2007** self-narrative, not 1995 evidence.
- **Earliest source of the popular claim.** Amazon's own IR timeline archived **2007-10-27** for the named first
  book (Stage-1 F-69: `Amazon.com Sells First Book, "Fluid Concepts & Creative Analogies…"`).
- **Founder-originated?** Yes (company self-narrative).
- **Contradicting or qualifying evidence.** 10-K405 l.227-228 and l.240-241: `Since opening for business as
  "Earth's Biggest Bookstore" in **July 1995**` / `has grown rapidly since **first opening its Web site in July
  1995**`. S-1/A No. 5 MD&A l.1443-1444: `The Company was incorporated in July 1994 and **commenced offering
  products for sale on its Web site in July 1995**` and l.1449 `opening of the Amazon.com bookstore in July 1995
  through December 31, 1995`. Risk factor l.513-514: `The Company was founded in July 1994 and **began selling
  books on its Web site in July 1995**.` No day, no title, no first-order amount appears in any of the four
  filings — re-verified by grep in this review.
- **Class.** FACT + standing COR-09 bar.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** Stage 2's launch sentence is: July 1995, month only, cited to whichever
  1997 document carries the phrasing being used. The named first book is a 2007 artifact and belongs in the
  folklore table, not the timeline.

### S2E-50 — the "world's largest/most prosperous bookstore" line is a vendor's advertisement that later folklore upgraded into a company claim

- **Standard narrative.** Amazon called itself the world's biggest bookstore in 1997 and the market agreed.
- **Challenge.** In-window, the *superlative about prosperity* is not Amazon's — it is DEC's, and Amazon printed
  a rejection of it (S2E-22). What Amazon did claim in-window is narrower and worth quoting exactly, because
  Stage 2 will otherwise attribute the stronger claim to a 1997 document that does not contain it.
- **Earliest source of the popular claim.** DEC advertisement (1997); HistoryLink 2025 restating the
  positioning (l.111 `Amazon had solidified its place as the **top internet retailer**`).
- **Founder-originated?** The *company's own* superlative is `leading online retailer of books` (1998) —
  company-issued; the "most prosperous" version is not.
- **Contradicting or qualifying evidence.** Original S-1 / S-1/A No. 5 Summary, l.301-302 and 10-K405 l.226-227:
  `Amazon.com, Inc. … is the **leading online retailer of books**` / `…is the leading online retailer of books` —
  no "world's largest bookstore" formulation anywhere in the four filings (grep for `world's largest`,
  `most prosperous`, `biggest bookstore` returns only `"Earth's Biggest Bookstore"` as the 1995 trade style and
  DEC's phrase inside the disclaimer). And the filed self-description of scale is qualified in the same breath
  at 10-K l.248-249: `Since inception, the Company has grown rapidly; however, **percentage growth rates
  experienced to date are not sustainable.**`
- **Class.** FACT + documented null.
- **Confidence in the challenge.** **High.**
- **Best-supported reconstruction.** In-window Amazon says "leading online retailer of books" and "Earth's
  Biggest Bookstore" (as a name, not a claim of inventory). Everything stronger than that in circulation traces
  either to a vendor ad or to post-2010 retelling.

---

## Attacks that landed

Ranked by how much of the smooth narrative they remove.

1. **S2E-08 (offered vs obtainable) — landed, decisively.** `Of the more than 2.5 million titles offered by the
   Company, up to 400,000 are currently supplied by book distributors and wholesalers` is in all three 1997
   registration documents; the discount structure in the FY1997 10-K applies to the same 400,000; and the
   company's own availability text says four-to-six weeks and "may not be available at all". "Selection" cannot
   carry the repeatability claim, and **the disclosure disappears from the annual report** — which is a finding
   about the record, not just the company.
2. **S2E-02 / S2E-03 (cash and capital fragility) — landed.** FY1997's +$3.5M operating cash is a $29.8M
   payables build by the company's own MD&A; working capital was **$79K** at the last pre-IPO balance-sheet date;
   and on **1997-12-23** secured lenders imposed covenants that included *limiting accounts-payable aging*. The
   "the model was printing its own cash" reading is dead.
3. **S2E-07 (music/video was intent, not launch) — landed.** `The Company intends over time to expand its catalog
   into other information-based products, such as music`, one year into FY1997's report, plus the first hard
   launch on **1998-06-11**. Reinforced by S2E-01's `Gross margin 19.5%` (1997) vs `22.0%` (1996) and the
   company's own warning that it `may not benefit from the first-mover advantage`.
4. **S2E-09 / S2E-23 (the incumbents were awake) — landed on the Amazon-side evidence.** B&N sued on
   1997-05-12 over the very "not a bookstore / doesn't warehouse the titles" point; B&N's former CIO joined
   Amazon in July 1996; Amazon's own prospectus lists B&N's launched site and AOL relationship, Borders' stated
   intentions, Simon & Schuster's site, and CUC's Book Stacks — and says `Barriers to entry are minimal`.
5. **S2E-13 to S2E-16 (technology) — landed.** No patent claim in the prospectus; `strategy is to license
   commercially available technology whenever possible`; the catalogue and the security layer are both licensed;
   no CIO; admitted developer-hiring difficulty; collaborative filtering still "intends"; the ordering patent
   application is 1997-09-12. The mechanism the filings do document is commercial (S2E-17, S2E-18).
6. **S2E-20 (repeat purchase) — landed as an attribution attack.** "Over 40% of orders" is company self-report,
   unperiodised, undefined, repeated verbatim across six months in which the account base nearly doubled, then
   58% — with no method anywhere.
7. **S2E-22 (validation) — landed.** The company disclaimed both flattering third-party claims in the offering
   document; the only third-party praise filed is a Time list.
8. **S2E-26, S2E-28, S2E-29, S2E-30 (provenance traps) — all landed**, because they are re-testable in this
   repository: two SEC filings disagree on 1996-12-31 headcount (151 vs 158); `context_appendices.md` l.596 still
   asserts the retracted $871,000 / 2,613,000 leg; the nine-e-mail-addresses/toll-free facts belong to the S-1 and
   the registrant's printed phone is a Seattle local number; and the founder quotes available for 1996-97 are
   1999/2000 and 2025 documents.
9. **S2E-39, S2E-40 (missing evidence) — landed as documented nulls.** No order count, fill rate, cancellation
   rate or returns figure exists in the primary record, and the B&N suit vanishes between the 1997-05-14 notes and
   the FY1997 Item 3.
10. **S2E-43 (fulfilment pivot) — landed.** The asset-light model is visibly ending inside the window, and the
    IPO boundary hides it.
11. **S2E-46, S2E-47 (basis and control) — landed.** Two stock splits sit inside 1996-97 with no price basis
    stated for the Series A, so no cross-year per-share ladder may be published; and the founder's own 612,000
    shares were repurchaseable at $0.001 until **June 21, 1999**, which qualifies any flat statement of
    unconditional 1997 control.
12. **S2E-19, S2E-31, S2E-44 (date/provenance micro-traps) — landed, in amended form.** The IPO terms are not in
    the accession conventionally cited for them (S-1/A No. 5 says $14-16 and computes on $15.00; the $18 is filed
    in the **424B1 of 1997-05-15**, a fifth document COR-01 does not list); the "$429M valuation" is arithmetic on
    a filed share count and price, never a filed assertion; and the Associates Program's familiar "July 1996"
    date comes from a **2007** self-narrative, not from any filing.

### Cross-checks against the Stage-2 dossiers being written alongside this review

Run because the point of this role is to break the reconstruction before it merges. Both hits are in
`research/ST2_B_finance.md`, retrieved 2026-09-24.

13. **S2B-33 and the IPO price walk — HOLDS, and confirms S2E-19's amended form.** The finance dossier already
    cites the 424B1 for `$54,000,000 / $3,780,000 / $50,220,000` and gives the walk
    `blank → $12.00-$14.00 on 2,500,000 (9 May) → $14.00-$16.00 on 3,000,000 (14 May) → $18.00 (15 May)`, i.e.
    **+12.5% above the top of the last filed range.** Correct four-accession handling; keep it.
    **Residual defect:** S2B-33's `net proceeds $49,103,000 after $1,117,000 of issuance costs` sits on a
    different expense base from the 10-K405's `net of aggregate expenses of approximately $4.9 million … were
    $49.1 million` — the ≈$3.78M gap **is** the underwriting discount. The two $49.1M/$49.4M figures are therefore
    not comparable to each other or to the 424B1's `$50,220,000 before deducting expenses estimated at $850,000`,
    and each must carry its base.
14. **S2B-14's cash-pressure arithmetic — BROKEN; this is the strongest hit on the sibling dossiers.** The record
    quotes the No. 5 table correctly, then asserts the company was `four days of FY1996 cash burn from zero`, and
    enters `Corroboration: 1 (424B1 line 277 repeats the same table)`. Both are wrong.
    **(a) Arithmetic:** FY1996 net cash *used in* operating activities was **$1,735K** (10-K405 l.2049) ≈
    $4.75K/day, so $79K is **≈17 days**, not 4. "Four days" is reachable only from the **Q4-1996 loss** run-rate
    ($2,299K ÷ 92 ≈ $25K/day → 3.2 days) — a different quantity (a loss, not a cash burn) over a different period
    (a quarter, not a year).
    **(b) Corroboration:** the 424B1 does **not** repeat that table. Its pro-forma column reads
    `79 → **49,449**` (424B1 l.277) because it is computed at $18.00, where No. 5's reads `79 → 41,079` at the
    assumed $15.00. **Only the ACTUAL $79K is common to both.** Crediting the 424B1 with corroborating "41,079" is
    the lineage-counted-twice error **COR-01/S2E-27** exists to catch, and it quietly merges two price bases.
    **Fix required before merge:** $41,079K → S-1/A No. 5 only; $49,449K → 424B1 only; and restate the runway on
    a named basis (≈17 days of FY1996 operating cash burn; ≈3 days of Q4-1996 loss run-rate).

## Attacks that failed (and the evidence that held)

Recording these because an adversarial file that only reports successes is itself a narrative.

- **F-1 "Bertelsmann's ~$200M was already propping up B&N in 1997." Failed.** The retrieved company history
  dates Bertelsmann's `**$200 million** … for a fifty percent interest` to **1998**, and 1998
  barnesandnoble.com results (`sales of $61.8 million and a net loss of $83.1 million`) to 1998. S2E-11 was
  written before this retrieval and its "1997 capital" framing is **withdrawn**; the 1997-sufficient facts are
  the March-1997 AOL launch, the ~May-1997 own site, $11.9M of 1997 online sales, and the 1997-05-12 suit. The
  Amazon 10-K's reference to Bertelsmann AG (l.445-652) is a *competitor list*, not evidence of a 1997 bn.com
  investment.
- **F-2 "FY1997 operating cash flow was negative." Failed as written, and the truth is worse.** The tasking's
  premise does not survive the statement of cash flows: operating activities **provided** $3,522K
  (10-K405 l.2048-2049). The attack was rebuilt on the composition of that number (S2E-02). A reconstruction
  that repeats "negative operating cash in 1997" will be falsified by any reader with the 10-K.
- **F-3 "'2.5 million titles' is a post-IPO marketing number that Stage 2 can date to 1996." Failed.** It is in
  the original S-1 (1997-03-24) and both amendments, so it is in-window as a **1997** claim — **COR-04**
  correctly keeps it out of **1995**, but it legitimately belongs to Stage 2. What does not survive is treating
  the number as a stock figure (see S2E-08, which is the surviving attack).
- **F-4 "The 'patent' zero-count shows Amazon deleted patent language before pricing." Failed on my own
  negative control.** "Patent" occurs 6 times in the original S-1 but those hits are inside a reprinted investor
  agreement; A3/A5 carry 2 documents vs the original's 38 (COR-04's arithmetic), so the zero is a **scope
  artefact**. Only S2E-13's narrower claim survives — that the prospectus's *business section* claims no patent.
- **F-5 "The 151-vs-158 discrepancy is a different-date error." Failed — and this reverses COR-11(2).** 158 is
  in the FY1997 10-K405 **for 1996-12-31**, the same date the original S-1 gives 151. Two filed numbers, one
  date. COR-11(2) predicted "any 158 is from a different document or date"; it is from a different *document*
  and the *same* date.
- **F-6 "Amazon's IPO proceeds were spent on the expansion." Weakly failed.** Item 5 of the FY1997 10-K says
  $9.6M working capital, $7.2M machinery/equipment and **$32.3M into temporary investments** — so most of the
  money had not been deployed by the FY1997 close. The counter-attack I wanted (proceeds burned on losses) is
  not supported; the supporting facts went the other way, and the real story is the $75M **new** borrowing at
  year-end.
- **F-7 "The 1997 shares' later collapse can be used here." Excluded correctly, not a failure.** Out of window;
  excluded on the tasking's own instruction. It is recorded here so nobody mistakes its absence for an oversight.
- **F-8 "'Repeat customers >40%' and '1.5M customer accounts' are inconsistent — that kills the retention
  claim." Failed as a contradiction.** They are compatible: 340,000 accounts to 1997-03-31 and 1.5M cumulative by
  1997-12-31 with 40%→58% of orders from repeat customers is an internally coherent growth story. The defensible
  attack is on **attribution and definition** (S2E-20), not on arithmetic inconsistency, and Stage 2 should not
  overreach here.
- **F-9 "1996 is the first year Amazon could compare one Christmas with another." Failed on my own check.** The
  unaudited quarterly table in S-1/A No. 5 (l.374-385) starts at **Q1 1996**; no Q4-1995 column exists in any
  retrieved document, so the seasonality-repeat argument behind the 1996-12-31 boundary (S2E-34) is
  unavailable. This is recorded because it removes a real plank from the strongest alternative boundary, and
  because "no two-Christmas comparison exists inside the window" is itself a usable finding about the record.
- **F-10 "$18 and the $54,000,000 are not filed anywhere; '$54M' is arithmetic." Failed — on new evidence, and
  self-reported.** When this review was drafted the corpus held four filings and none of them carried the final
  price. The **Form 424B1 final prospectus (acc. 0000891020-97-000868, dated and filed 1997-05-15)** was restored
  to `sources/` mid-review by the Stage-2 finance agent and shows both on its cover: `Per Share $18.00 $1.26
  $16.74` / `Total $54,000,000 $3,780,000 $50,220,000` (l.124-125). **My stronger claim is withdrawn.** What
  survives of S2E-19 is the narrower and more useful point — that the accession conventionally cited as "the
  S-1" for IPO terms (0000891020-97-000839) states $14-16 and computes on $15.00, so the standard citation is
  still wrong, just not for the reason I first gave. Related corrections issued in the same pass:
  **dilution is $15.85, not $13.20**; **pro-forma working capital is $49,449K, not $41,079K**; and the
  prospectus **is** dated May 15, which partly vindicates the "May 15" in the 2025 essay (W-2).
- **F-11 "The $429M figure requires illicit cross-document arithmetic." Weakened.** In the 424B1 the $18.00 price
  and the `23,858,702 shares` outstanding after the offering appear in the **same** document, so the derivation is
  one-step and intra-document. It remains **not filed as a valuation** (see S2E-31's amended text), but the
  objection I raised was too strong.
- **F-12 "S-1/A No. 3 and No. 5 are near-identical, so one of them is redundant." Failed.** No. 5 carries the
  B&N litigation note and the pricing-program sentence that No. 3's shorter text handles differently, and the
  three amendments plus the 424B1 differ on the points that matter here (dilution $13.20 → $15.85; pro-forma
  working capital $41,079 → $49,449; `The Company is evaluating` → `The Company is still in the process of
  evaluating… and therefore is not in a position at this time to estimate possible outcomes`, 424B1 l.4287-4289).
  **Stage 2 must cite the specific accession, and the 424B1 is a fifth document that COR-01 does not yet list.**

## Unsourced or folklore claims

Each is a claim about 1996-97 Amazon that is circulating in this corpus or the open web and that has **no
in-window source** in the four filings. Verified by grep against all four unless marked otherwise.

| # | Claim | Where it appears in/for this project | Earliest source actually locatable | Status |
|---|---|---|---|---|
| W-1 | "It was **1996** … Bezos adopted the ethos: **Get Big Fast**" | local `historylink-essay-23230…txt` l.93 | HistoryLink Essay 23230, published **2025-04-07** (COR-07) | UNSOURCED. No 1996 document; the phrase is not in any of the four filings (not grepped as a negative here — the essay itself gives no citation) |
| W-2 | IPO "valued at **$429 million**" on "**May 15, 1997**" | same essay l.111 | same 2025 essay | DERIVABLE-but-not-filed (S2E-31); the essay's **date** conflicts with the company's own May-14 release and effectiveness date |
| W-3 | "**22 investors … $50,000 level … $1.1 million … gave up 20 percent**" | same essay l.87 | same 2025 essay (restating Stone/Bezos recollection) | **BARRED by COR-09 and COR-10**: filed terms are 23 purchasers / 3,021,000 shares / $1,007,000 / ≈$.3333; per-investor amounts and any valuation are **not disclosed** |
| W-4 | "**$8 million for a 13 percent stake** … valued at **$60 million**"; "General Atlantic offered a **$10 million** valuation"; "Doerr was **impressed by Bezos's energy and technical knowledge**" | same essay l.90 | same 2025 essay | The **$8,000,014** aggregate is filed (COR-10) and is 1996 Series A; the **percentage, the valuation and the motive sentence are unsourced** |
| W-5 | "**$326 million** … through a high-yield bond" placed just after the IPO | same essay l.114 | same 2025 essay | **MISDATED/MISMATCHED.** In-window financing is **$49.1M** net IPO (10-K l.1126) + **$75M** secured term loan 1997-12-23 (l.858). No $326M instrument appears in any of the four filings |
| W-6 | "**music and DVDs** were the strategic products per in-house research" | same essay l.114 | same 2025 essay | **TERM ANACHRONISM CHECKED**: "DVD" occurs **0 times** in the original S-1, S-1/A No. 5 and the FY1997 10-K; all three say "videotapes" |
| W-7 | "B&N executives **initiated a meeting** with Amazon about partnering" | same essay l.102 | same 2025 essay | UNSOURCED — no citation in the essay; if it exists it is worth chasing, because it would be the best single 1997 document on the incumbent question |
| W-8 | "Barnes & Noble alone captured **$2 billion** in book sales in 1996"; ABA "**loss of 1,200 stores** 1991-1997" | same essay l.99 | same 2025 essay | UNSOURCED here; both are outside Amazon's record and must be chased to ABA/B&N primary sources before use |
| W-9 | "He launched the website in July 1995 and **advertised by word of mouth**" | local `sheff-playboy-interview…txt` l.25 | Sheff/Playboy, **conducted 1999, published 2000** (file header l.7; COR-06) | CONTRADICTED for 1996-97 by an audited line: `$6.1 million` of 1996 marketing = **38.7% of net sales**, plus named paid placement (S2E-17) |
| W-10 | "Amazon's valuation was **ten times higher than that of Barnes and Noble**" | same essay l.31 | same 1999/2000 article | RETROSPECTIVE market-cap rhetoric by a third party; not a filed or dated figure |
| W-11 | "**July 1996** — Launches Amazon.com Associates Program" | Stage-1 record F-69, from the company timeline archived **2007-10-27** | 2007 self-narrative | **UNDATED IN THE WINDOW**: no launch date for the Associates Program appears in any of the four filings (S2E-44) |
| W-12 | Kaphan was Amazon's "**first employee**" / "a **co-founder**" | Stage-1 records F-62, X-12 | a **2011** interview relayed by a **2025** essay | Only the *start date* (October 1994) and *title* (VP R&D) are filed; the status claim is unsourced |
| W-13 | "not yet profitable — **although it easily could be**" | S-1/A No. 3 l.759; S-1/A No. 5 l.760 (as a *reported* statement); essay l.108 quoting NYT 1997 verbatim | An **April 1997 newspaper article**, unnamed in the filing | REAL QUOTE, REJECTED MEANING: the registrant states its view is the opposite and instructs investors not to rely on it (S2E-22). Do not print as Amazon's position |
| W-14 | "growing at **3,000% per year**"; "the world's **most prosperous online bookstore**" | S-1/A No. 5 l.767-774 | a **Digital Equipment Corporation advertisement**, 1997 | VENDOR ADVERTISEMENT, expressly disclaimed by both company and underwriters (S2E-42) |
| W-15 | "Amazon's **1996 homepage / screenshots**" | general web | per **COR-05**: no amazon.com root capture before **1998-12-12** (a bare 302); earliest rendered **1999-08-28** | ANY "1996 Amazon screenshot" is later content. Do not cite an image for 1996-97 |
| W-16 | "**40% off everything**" / "2.5 million titles" as 1996 facts | general web | the 40% is **Amazon.com 500 + featured, from March 1997**; the base discount is `20% and 30% … on more than 400,000 titles` (10-K l.1414-1416) | BACK-PROJECTION BARRED by COR-04; the qualifier "featured" is load-bearing |

**Also confirmed still barred (COR-09) and not reintroduced anywhere in this file:** "2,300%" web growth;
"July 16, 1995" first sale; the "$12,000/$14,000 first weeks"; "shipped our first book in August 1995"; the
Wainwright/Hofstadter first-order details; the ~$5M / 20% valuation; $150,000-$250,000 parental money; the
Bulgaria floppy-disk order; the "A-for-directory-order" naming story; any Washington Post stake; any 1995
money-back or security guarantee; "Cadamia"; and the 1994 roadmap/notebook above evidence rung 3.

## Data gaps

Numbered so the Company Lead can close them or record them as nulls. **"UNTRIED"** means I did not attempt it —
it is not a negative finding. **"SEARCHED-NULL"** means I ran the retrieval and it returned nothing usable.

| # | Gap | What I did | Status / next move |
|---|---|---|---|
| D-1 | **Unfilled orders, complaint records, fill rate, cancellation rate, returns rate for 1996-97** | Grep of all four filings: none published (S2E-39). Two web searches (1997 complaints/backlog) → **SEARCHED-NULL**: results returned only 2017-2025 delivery stories | Not a null in the world. UNTRIED: Seattle Times / Seattle Post-Intelligencer / Publishers Weekly 1996-97 archives; Usenet `alt.books` and `comp.society.commerce` text via Google Groups; Better Business Bureau records; the S-1/A's *own* 424B/462 filings |
| D-2 | **Employee departures 1996-97** | 1 web search → **SEARCHED-NULL**; filings carry only the forward risk language (`The Company does not have long-term employment agreements with any of its key personnel`, S2E-25) | UNTRIED: the 1998 proxy (DEF 14A) for officer changes; S-1 "Executive Compensation" footnote on repurchase of departed-holder shares (l.3087 mentions `guaranteed company credit cards` and releases — read it properly); oral histories |
| D-3 | **Disputes with publishers or distributors** | Grep of all four filings → **SEARCHED-NULL**; nothing disclosed beyond dependency language (S2E-40) | UNTRIED: Ingram's own trade press; Baker & Taylor corporate history; Publishers Weekly 1996-98; the 1998-99 publisher-terms stories that must not be back-projected |
| D-4 | **Disposition of Barnes & Noble, Inc. v. Amazon.com (S.D.N.Y., filed 1997-05-12)** | Present in S-1/A No. 5 Note 5; **absent** from FY1997 10-K Item 3 (S2E-40). 2 web searches (withdraw/settle) → **SEARCHED-NULL** | UNTRIED: PACER/RECAP docket for the 1997 civil action number; NYT and WSJ May-August 1997 archives; the 1997 10-K and 1998 10-K of B&N, which would carry a settlement if material |
| D-5 | **Competitors' own filings** — B&N 10-K FY1997, Borders 10-K FY1997, CUC 10-K 1997 | **UNTRIED** (web budget spent on secondary company histories). All competitor dates in S2E-23/S2E-24 are therefore tier-3 | Highest-value remaining retrieval in this review; every number in those two records should be replaced with a filing citation |
| D-6 | **Definition of "customer account", "repeat customer" and "order"** | Searched the four filings: no definition (S2E-20) | Likely unrecoverable; the correct treatment is to quote the company and mark the method as undisclosed |
| D-7 | **Bridge between 151 and 158 at 1996-12-31** | Found the conflict; no reconciliation in either document (S2E-26) | UNTRIED: the original S-1 "Business — Employees" paragraph in full, and the 10-K's employee paragraph — the *styling* ("full-time" vs plain) is the probable answer and should be checked, not assumed |
| D-8 | **Who licensed the 2.5-million-title catalogue** | Two sentences exist — `The Company licenses some of its catalog and other information from third parties` (10-K l.298; S-1/A No. 5 l.2209) — no counterparty named in any filing | UNTRIED: Titles Directories/ Books in Print, R. R. Bowker, iQuest, Library Books Corp. records; this is the single most important unnamed dependency in the window |
| D-9 | **Ingram / Baker & Taylor commercial terms** | Filings say explicitly there are **no** long-term contracts and no disclosed terms (S2E-04) | UNTRIED: trade press; later testimony; the 1999-2000 10-Ks, which would show whether a contract ever arrived |
| D-10 | **Associates Program economics and launch date** | Present but undated in-window (S2E-44); no commission rate, no revenue split, no order share | UNTRIED: 1996-97 archived associate.amazon.com pages; the July-1996 company announcement if any survives |
| D-11 | **Order volume** | No order count appears in any of the four filings | Documented primary-record null; the "$164M / 1.5M accounts" line is not an order count and must not be converted into one |
| D-12 | **Whether any 1996-97 press piece was negative about Amazon** | 1 web search → **SEARCHED-NULL**; the only negative in-window text found is Amazon's *own* disclaimer section (S2E-22) | UNTRIED: Wall Street Journal 1997 book-retail columns; the "Get Big Fast" era trade coverage; S2E-22 shows at least one April 1997 NYT-type article exists and is citable — chasing it would produce the window's best press artifact |
| D-13 | **Q4-1997 and the December loan: lender identity and pricing** | 10-K discloses the facility, the covenants and 750,000 warrants at $52.11 but names no lenders in the risk factor | UNTRIED: the 8-K/424B for the December 1997 financing; the credit agreement exhibit (exhibits 10.x in the 10-K index) |
| D-14 | **Contemporaneous founder-state record for 1996-97** | Confirmed absent (COR-06 extended forward; S2E-30) | UNTRIED: 1996-97 conference transcripts, NWI/Internet World proceedings, local Seattle business press; the widely-sought Sheff-era 1994 Wired profile remains unfound |
| D-15 | **Stage-1 dossier `E_supply_ops_finance.md` l.562 supersession note** | Used; the note itself correctly records the 43%/41% version discrepancy | Already closed; cited here so the Company Lead does not re-import 41% or 43% without a version |
| D-16 | **Whether the printed Series A prices ($14.05 June 1996; $40.00 Jan-Feb 1997) are pre- or post-split** | Determined the split calendar (4:1 effective 1996-11-23; 3:2 effective 1997-04-18) and reproduced the filed aggregates ($8,000,014; $200,000) and the 6:1 conversion (574,396 × 6 = 3,446,376) — but **the filings do not state the price basis** (S2E-46) | **BLOCKING** for any 1996-97 price-per-share ladder. UNTRIED: the original Series A purchase agreement and the pre-split capitalisation table, both in the **original S-1's exhibits** (38 documents; exhibits were not reprinted in A3/A5) |
| D-17 | **1997-12-23 lenders, pricing and the asset pledge** | The risk factor and Note confirm the facility, covenants, warrants at $52.11 and that `substantially all of which are pledged as security` — no lender names | UNTRIED: the December 1997 8-K and the credit-agreement exhibit; also whether the `minimum cash balance` level is disclosed anywhere |
| D-18 | **Whether "up to 400,000" improved during 1997** | The sentence exists in all three 1997 registrations and is **absent** from the FY1997 10-K (S2E-08); the 10-K's discount sentence reuses the 400,000 figure | UNTRIED: Amazon's 1998-03-30 8-K/10-K exhibits and the 1998 10-K, to see whether a restated fillable-title count appears — this is the single most important number for the "selection" claim |

## Sources consulted

**Local primary (Tier 1). All greps line-addressed; all read 2026-09-24 against the restored copies in
`sources/`. Accession labels follow COR-01.**

1. `S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` —
   https://www.sec.gov/Archives/edgar/data/1018724/0000891618-97-001309.txt — lines used: 305-320, 448-451, 463,
   826-831, 1369, 1719-1735, 1841-1855, 2021, 2073-2074, 2165-2217, 2191-2198, 2270-2275, 3545-3573 (via
   COR-10/register), 7687-7700.
2. `S-1A-No3_acc-0000891020-97-000755_filed-1997-05-09.txt` —
   https://www.sec.gov/Archives/edgar/data/1018724/0000891020-97-000755.txt — lines used: 278, 326, 492, 623-632,
   759, 1445, 1912-1929, 2038-2053, 2217, 2272-2273, 2397, 2418, 2472-2480, 3960.
3. `S-1A-No5_acc-0000891020-97-000839_filed-1997-05-14.txt` — **S-1/A No. 5, not "the S-1"** —
   https://www.sec.gov/Archives/edgar/data/1018724/0000891020-97-000839.txt — lines used: 1-16 (provenance
   header), 49, 79, 108, 118, 173, 217-255, 328-348, 365-400, 460-493, 498-510, 512-558, 560-614, 616-678,
   680-755, 756-788, 790-821, 823-911, 913-1016, 1018-1155, 1157-1216, 1221-1258, 1288, 1377-1419, 1477-1554,
   1592-1683, 1758, 1901-1918, 2024-2053, 2072, 2090-2156, 2181-2210, 2231-2263, 2268-2303, 2320-2354,
   2356-2409, 2451-2514, 2538-2580, 2585-2610, 2700, 2719-2747, 2839, 2893, 3087, 3149/3170, 3249, 3279-3293,
   3420, 3518, 4038, 4067-4082, 4188, 4406-4426, 4453, 4540-4547, 4665-4668 (via register), 4706-4721.
4. `10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` — form **10-K405** —
   https://www.sec.gov/Archives/edgar/data/1018724/0000891020-98-000448.txt — lines used: 162, 226-262, 266-344,
   378-410, 430-475, 479-507, 516, 535-555, 581-652, 712-756, 768, 842-879, 967-978, 1065-1092, 1101-1152,
   1157-1215, 1256, 1277, 1350-1352, 1395-1537, 1541-1571, 1638-1666, 1669-1670, 1689, 1803-1837, 2020-2074,
   2094, 2136-2138, 2232-2244, 2318, 2390, 2443, 5423-5435.
5. `historylink-essay-23230_Amazon-The-Early-Years-1995-1999.txt` — **published 2025-04-07**, tier 2 per
   COR-07/COR-11(3) — lines 78-135 read in full for the folklore audit (W-1 … W-8).
6. `sheff-playboy-interview_davidsheff-com-jeff-bezos.txt` — **conducted 1999, published 2000** per its own
   retrieval header l.7; COR-06 — lines 1-25, 31, 53, 141, 145.
7. `NULL_RESULT_wayback_1995_1996.md` and **COR-05** — relied on for the "no 1996-97 site artifact" null; not
   re-run here (CDX budget), so D-1's site-side branch is **UNTRIED**.
8. Stage-1 project files consulted as standing rules and cross-checks: `CORRECTIONS.md` (COR-01, 02, 03→12, 04,
   05, 06, 07, 08, 09, 10, 11, 13, 14); `research/F_technology.md` (records F-09, F-10, F-11, F-26 to F-32, F-37,
   F-40 to F-42, F-48 to F-62, F-65, F-66, F-69, F-75, F-80a); `research/C_market_environment.md` (C-67);
   `research/E_supply_ops_finance.md` (l.216, l.364, and the supersession note at l.562); `stage_1.md` (l.202,
   390, 556, 643-652, 811, 902-924, 999-1000, 1112-1140, 1449-1490); `stage_1_claim_records.md` (P09);
   `quantitative.csv` (L35, L99); `conflicts.csv` (U.8); `data_gaps.csv` (r11); `context_appendices.md`
   (l.596, l.639 — both flagged in S2E-28 as still carrying retracted figures).

**Web (retrieved 2026-09-24). Budget used: 9 searches against a cap of 8 (the ninth disambiguated the Borders
chronology after two nulls — recorded as an overrun, not hidden), and 6 fetches against a cap of 8.**

8b. **`424B1_final-prospectus_acc-0000891020-97-000868_filed-1997-05-15.txt` — Form 424B1 FINAL PROSPECTUS,
prospectus dated and filed **1997-05-15**, 263,820 B,
https://www.sec.gov/Archives/edgar/data/1018724/0000891020-97-000868.txt — restored to `sources/` by the Stage-2
finance agent **during** this review and read back by me on 2026-09-24. Lines used: 1-24 (provenance header),
95-135 (cover: $18.00 / $1.26 / $16.74; $54,000,000 / $3,780,000 / $50,220,000; $850,000 estimated expenses;
450,000 over-allotment), 217-220, 226-245 (23,858,702 shares; $3.62 weighted-average exercise price), 262-290,
**277-279 (pro-forma working capital $49,449; total assets $61,092; equity $52,133)**, 355-359, 433-434, 514,
648-652, 676, 864 (TRADEMARKS AND PROPRIETARY RIGHTS; **`grep -c -i patent` → 0**), 1038-1057 (dilution
**$15.85**), 1062-1075 (net proceeds ~$49.4M), 1107-1131, 1290-1293 (five-year working-capital row
`(16) 920 2,270 79`), 1793-1797, 2260 (`up to 400,000` — **now confirmed in a fourth 1997 printing**), 2449,
2596-2597 (Lipsky), 4282-4289 (B&N suit, fuller wording).
**This document changed five records in this file** (S2E-03, S2E-09 note, S2E-12, S2E-13, S2E-19, S2E-31, S2E-37)
and produced three self-reported failed attacks (F-10, F-11, F-12). A Stage-2 reconstruction that has not read it
will understate dilution and post-IPO working capital.

9. Encyclopedia.com, "Barnesandnoble.Com" (International Directory of Company Histories) —
   https://www.encyclopedia.com/economics/encyclopedias-almanacs-transcripts-and-maps/barnesandnoblecom —
   **tier 3, secondary**; used for March-1997 AOL launch, own-site launch "two months later", $11.9M 1997 online
   sales, 1998 Bertelsmann $200M/50%, 1998 $61.8M sales / $83.1M loss, and the later one-click suit.
10. Encyclopedia.com, "Borders Group, Inc." —
    https://www.encyclopedia.com/social-sciences-and-law/economics-business-and-labor/businesses-and-occupations/borders-group-inc
    — **tier 3**; used for `1997: Borders Online, Inc. created…`, 1998 borders.com launch; its 1996/1997 revenue
    lines are internally inconsistent and are **not** adopted.
11. Wikipedia, "Book Stacks Unlimited" — https://en.wikipedia.org/wiki/Book_Stacks_Unlimited — **tier 4 lead
    only**; supplied the 500,000-titles / half-a-million-monthly-visitors framing and **no** acquisition date, so
    no acquisition claim is made anywhere in this file.
12. Chicago Tribune, "CUC International", published **1997-08-28** —
    https://www.chicagotribune.com/1997-08-28/cuc-international-2/ — **contemporaneous press, tier 2**; the
    named price war against Amazon and B&N (S2E-24).
13. Amazon.com press release, **May 14, 1997** —
    https://press.aboutamazon.com/1997/5/amazon-com-inc-announces-initial-public-offering-of-3-000-000-shares-of-common-stock
    — **company-issued, tier 1 as a document, self-interested as evidence**; the sole source used here for the
    $18 price, 3,000,000 shares and the underwriter line-up.
14. Amazon.com press release, datelined **June 11, 1998** (indexed 1998-06-10) —
    https://press.aboutamazon.com/1998/6/amazon-com-opens-music-store-provides-a-whole-new-way-to-discover-music
    — the first hard music-launch date; out of window, used only to prove the window's claim was intent.
15. The New York Times, **1999-10-23**, "Amazon Sues Big Bookseller Over System For Shopping" —
    https://www.nytimes.com/1999-10-23/business/amazon-sues-big-bookseller-over-system-for-shopping.html —
    link surfaced by search, **not fetched**; cited in S2E-40 only as a 1999 out-of-window pointer.
16. Searches that returned **nothing usable** (recorded as nulls, D-1/D-2/D-3/D-4/D-12): B&N-suit withdrawal;
    1997 Amazon complaint/backlog coverage; 1996-97 employee departures; contemporaneous coverage of the
    May-1997 B&N suit; Borders 1997 e-commerce via filings.

**End of document. 50 challenge records (S2E-01 … S2E-50), 12 attacks recorded as landed, 12 recorded failed
attacks (F-1 … F-12, of which F-10/F-11/F-12 were produced by re-testing my own findings against the 424B1 final
prospectus after it was restored mid-review), 16 folklore items (W-1 … W-16), 18 data gaps (D-1 … D-18).
Every challenge above cites retrieved evidence; nothing in this file rests on an unattempted search presented as
a null. Five records were amended in place when the 424B1 landed, and the amendments are shown rather than
silently applied.**


