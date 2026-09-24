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

### S2E-03 — $79,000 of working capital three days before the IPO filing

- **Standard narrative.** The IPO gave Amazon the capital it needed; pre-IPO it was already self-sustaining.
- **Challenge.** At the last balance-sheet date printed in the IPO document, working capital was
  **seventy-nine thousand dollars** on $16.0M of quarterly sales — 0.5% of one quarter's revenue. A single
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
  (Capitalization l.1258) — the company had burned **more than three times** its entire paid-in capital.
  Version check: the same construction appears in the original S-1 (1997-03-24); the March-31-1997
  balance-sheet date is common to both, so the figure is not an artefact of one accession.
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

- **Standard narrative.** Amazon's 1997 lead over the incumbents was decisive.
- **Challenge.** The two moves that matter on this axis both went against Amazon inside the window: B&N's
  online venture was capitalised at an order of magnitude above Amazon's entire IPO, and it was assembled with
  Kleiner Perkins Caufield & Byers — the KPCB that was Amazon's own preferred-stockholder. (External
  verification pending; see Sources and Attacks-that-failed.)
- **Earliest source of the popular claim.** Not on the in-window record at all — this is missing from the
  reconstruction, not wrong in it.
- **Founder-originated?** No.
- **Contradicting or qualifying evidence (local first).** The filings do carry the KPCB link: S-1/A No. 5
  l.3170 lists `Byers VIII and KPCB Information Sciences Zaibatsu Fund II, respectively` among principal
  stockholders/affiliated funds; the FY1997 10-K names Bertelsmann AG as a competitor with `significant brand
  awareness, sales volume and customer bases` (l.445-652). The dated 1997 transactions themselves must come
  from the competitors' own filings — retrieval attempted, see `## Sources consulted` and `## Data gaps`.
- **Class.** FACT for the local components; **EXTERNAL-VERIFICATION-PENDING** for the transaction amounts.
- **Confidence in the challenge.** **Medium** until the dated competitor filings are retrieved; then High.
- **Best-supported reconstruction.** If it holds, the right sentence for Stage 2 is: Amazon raised $49.1M net
  in May 1997 and, within seven months, its rival's online subsidiary was capitalised by a German media group
  and a Silicon Valley firm Amazon shared — so the IPO's "validation" was immediately outbid.

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
- **Best-supported reconstruction.** The offering bought capital, a ticker, and ~$41.0M of pro-forma working
  capital (S-1/A No. 5 l.397), and 2/3 of the cash sat in temporary investments at the FY1997 close. What it
  did not produce is any third-party statement that the model repeated: the traction the market bought was
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

### S2E-19 — the IPO was priced at **$14-16** in the document that contains the final prospectus text; **$18** is not in it

- **Standard narrative.** "Amazon IPO'd at $18 in May 1997 and raised $54 million" — usually cited to "the S-1".
- **Challenge.** Both numbers are outside the document they get cited to, and neither is filed: the range in
  S-1/A No. 5 (filed 1997-05-14, the same day the pricing was announced) is **$14.00-$16.00**, and every
  proceeds/capitalisation/dilution computation in that document assumes **$15.00**. "$18" is from the pricing
  press release; "$54,000,000" is arithmetic. This is the project's classic lineage error in a new costume.
- **Earliest source of the popular claim.** Amazon press release, **May 14, 1997**: `SEATTLE, WA (May 14, 1997)
  … offering of 3,000,000 shares of its Common Stock at a price of $18 per share. Deutsche Morgan Grenfell Inc.
  is acting as lead manager… Alex. Brown & Sons Incorporated and Hambrecht & Quist are acting as co-mangers…
  NASDAQ: AMZN` — retrieved 2026-09-24,
  https://press.aboutamazon.com/1997/5/amazon-com-inc-announces-initial-public-offering-of-3-000-000-shares-of-common-stock
- **Founder-originated?** Company-issued.
- **Contradicting or qualifying evidence.** S-1/A No. 5, cover, 1997-05-14, l.217-228: `3,000,000 SHARES COMMON
  STOCK… It is currently estimated that the initial public offering price will be **between $14.00 and $16.00
  per share.**` Registration-fee table, l.173: `3,450,000 shares  $16.00  $55,200,000`. Use of proceeds,
  l.1186-1189: `assuming an initial public offering price of **$15.00 per share**, are estimated to be
  approximately **$41.0 million** (approximately $47.3 million if the… over-allotment option is exercised in
  full)`. Actual net, per the FY1997 10-K l.1126-1127: `Offering proceeds, net of aggregate expenses of
  approximately $4.9 million, were **$49.1 million**.` Registration effectiveness, same document l.1125:
  `became effective on **May 14, 1997**`.
- **Class.** FACT; the "$54M" is DERIVED.
- **Confidence in the challenge.** **High** — and this one is cheap to fix, so there is no excuse for it in the
  Stage-2 text.
- **Best-supported reconstruction.** Cite three documents with three jobs: the **price and size** to the
  1997-05-14 company press release, the **effectiveness date** and the **$49.1M net** to the FY1997 10-K405, and
  the **$14-16 range and the $15.00 assumptions** to S-1/A No. 5. Never cite 0000891020-97-000839 for "$18" or
  for "$54 million".

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
