# AMAZON STAGE 3 — D. TECHNOLOGY AND OPERATIONS

**Dataset:** THE FOUNDER'S PLAYBOOK — forensic reconstruction, Company 001 Amazon.com, Inc. (CIK 1018724).
**Stage:** 3 (technology and operations). **Opening: 1997-05-16** — the first day on which periodic filings,
not a registration statement, govern. **Endpoint under argument:** this dossier works to **1999-12-31** and
says so; the last company document in the local corpus is Form 10-Q for Q3 1999 (acc. 0000891020-99-001938,
filed 1999-11-15), so everything asserted about **1999-10-01 → 1999-12-31** rests on filings made on or
before 1999-11-15 plus the 8-K of 1999-10-28. The FY1999 10-K (filed March 2000) is **not in the local
corpus** and no fourth-quarter-1999 operational figure in this dossier may be cited to a filing.
**Stage definition (method §7):** the section set this dossier owns is **§J Technology** and the operations
half of **§G/§L** — the physical network, the systems estate, the labour that runs both, and the constraint
that bounded them. Method §7's "adapt, never delete" applies: for a 1997-99 online retailer the validation
signal is not pilots or ARR but **throughput, capacity, and whether a filed instrument exists for the site
the company says it opened**.
**Hindsight-firewall statement (method §2):** nothing below is evidence that Amazon would scale. The
1997-99 filings record a company that repeatedly told investors it might **over-expand**, that it had **no
previous experience with automated distribution centers**, and that its new sites might **fail to operate
properly** in its first peak season. Those sentences are the contemporaneous state of the art here and are
quoted rather than glossed. The 1999 network is treated as **a build-out in progress**, which is a
different claim from a network in operation; the distinction is the spine of this dossier.
**Record-selection null (method §2):** the surviving archive is a **winner's disclosure record**, dense on
capital markets and near-silent on engineering. There is **no** archived amazon.com page for 1995, 1996 or
1997 (Stage-2 null, standing), and no filing in the window names the first system's language, operating
system, database or server hardware — those survive only as recollection. Internal architecture documents,
rejected site candidates, capacity tests, outage logs and any **independent** count of engineers are
unrecoverable because they were never public. Where this dossier reports a null it is a documented null,
not an inference of absence.
**Confidence scale:** High (2+ independent sources or primary document) · Medium (one reliable source) ·
Low (conflicting/vague/retrospective-only) · UNKNOWN.
**Filing-lineage rule (method §3):** each accession is one source; the FY1998 10-K and its ARS, a 10-Q and
its exhibits, an S-8 and its amendments, a POS AM and its parent S-3 are **one lineage**. Repetition across
a lineage is restatement, not corroboration. Where the same operational sentence appears in an 8-K exhibit
that reproduces a 10-Q, that is flagged.

**Sibling discipline:** `ST3_A_chronology_org.md` (chronology, headcount, premises) and
`ST3_C_product_market.md` (categories, supply, channels) are complete and are **not** re-argued here. Three
of their corrections are inherited and applied in every section: (i) the five "Sales Agreement" exhibits
dated 1999-03-11 are **materials-handling equipment purchase contracts** (Amazon as Purchaser; The Buschman
Company, Ohio, an affiliate of Pinnacle Automation Company, Inc. as Seller) covering **Fernley Phase I/II**
and three "Standard Proposal" contracts for **"Site A/B/C" still "yet to be determined"**, prices redacted
under Rule 24b-2 — they are **not** marketplace or merchant contracts, and the intake manifest's label is
wrong; (ii) the **S-4 lineages do not carry the first acquisitions** — `WarehouseDirect`, `Internet Mail`,
`Allaire` and `Exchange.com` return zero occurrences across the local corpus, and the acquisitions the
filings actually evidence are Bookpages and Telebook (instruments 1998-04-17/1998-04-24), IMDB, Junglee
(1998-08-12) and PlanetAll/Sage Enterprises (1998-08-27); (iii) **Ingram is 58% for FY1997 and
"approximately 60%" for FY1998** and the vendor-dependence sentence relaxes from "any of its vendors" to
"**most of our vendors**" between the FY1997 and FY1998 reports, with inventories at
**$8,971K → $29,501K**.

---

## Findings

**ST3D-01**
— Date: 1997-12-31 (state as filed) — Source: Form 10-K405 FY1997, acc. 0000891020-98-000448, filed 1998-03-30, MD&A — Source date: 1998-03-30 — URL: https://www.sec.gov/Archives/edgar/data/1018724/000089102098000448/0000891020-98-000448.txt — Archived: `../sources/10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` L1647-1648 — Tier: 1 — Class: FACT — Passage: "opened a 200,000-square-foot distribution center in Delaware and expanded its\nSeattle distribution center to 85,000 square feet." — Conf: High — Note: **the first filed use of the verb "opened" for a second distribution centre**, and it carries a square footage for both sites. The Seattle figure moves the Stage-2 "~50,000 sq ft" (S2D-06) to 85,000 inside seven months — the Q3-1997 10-Q had only declared an expansion "by approximately 35,000 square feet" (L857), and 50,000 + 35,000 = 85,000 exactly. **Derived check closes.**

**ST3D-02**
— Date: 1998-06-30 — Source: Form 10-Q Q2 1998, acc. 0000891020-98-001313, filed 1998-08-14, Liquidity — Source date: 1998-08-14 — Archived: `../sources/10-Q_Q2-1998_acc-0000891020-98-001313_filed-1998-08-14.txt` L1125-1126 — Tier: 1 — Class: FACT — Passage: "distribution center capacity in the United Kingdom and expanded its\nSeattle distribution center to 93,000 square feet." — Conf: High — Note: Seattle DC = **93,000 sq ft** by mid-1998. Series as filed: 50,000 (1997-05) → 85,000 (FY1997 report) → 93,000 (Q2-1998). The FY1998 10-K Item 2 restates 93,000 for 1998-12-31, so **no filing in the window puts Seattle above 93,000 sq ft**, which bounds the growth of the original site at 1.86x across 31 months.

**ST3D-03**
— Date: 1998-09-11 — Source: Form 8-K event 1998-08-27, acc. 0000891020-98-001370, filed 1998-09-11, reproduced MD&A — Source date: 1998-09-11 — Archived: `../sources/8-K_event-1998-08-27_acc-0000891020-98-001370_filed-1998-09-11.txt` L882-884 — Tier: 1 — Class: FACT (restatement) — Passage: "200,000-square-foot distribution center in Delaware and expanded its\nSeattle distribution center to 85,000 square feet. The Company may establish one\nor more additional distribution centers within the next 12 months, which would require" — Conf: High — Note: **lineage flag.** This is the FY1997 MD&A paragraph reproduced inside an 8-K exhibit; it is not a second observation of the Delaware opening. Counted once.

**ST3D-04**
— Date: 1998-12 (instrument) / 1998-12-31 (state) — Source: Form 10-K FY1998, acc. 0000891020-99-000375, filed 1999-03-05, Item 2 PROPERTIES — Source date: 1999-03-05 — URL: https://www.sec.gov/Archives/edgar/data/1018724/000089102099000375/0000891020-99-000375.txt — Archived: `../sources/10-K_FY1998_acc-0000891020-99-000375_filed-1999-03-05.txt` L1068-1070 — Tier: 1 — Class: FACT — Passage: "In December 1998, the Company leased an\napproximately 323,000-square-foot distribution facility in Fernley, Nevada under\na lease that expires in 2009." — Conf: High — Note: the spine site of this dossier. **At the 1998 close Fernley was an instrument, not an operation** — the same Item 2 says it "is expected to begin operations in 1999". One lease of 323,000 sq ft is **larger than Seattle (93,000), New Castle (200,000), Regensburg and Slough combined (32,000 + 41,000)**: 323,000 vs 366,000 = 88% of the entire then-operating estate in a single un-opened building (derived).

**ST3D-05**
— Date: 1999-01-01 → 1999-03-31 — Source: Form 10-Q Q1 1999, acc. 0000891020-99-000894, filed 1999-05-17, Liquidity — Source date: 1999-05-17 — Archived: `../sources/10-Q_Q1-1999_acc-0000891020-99-000894_filed-1999-05-17.txt` L592-593 — Tier: 1 — Class: FACT — Passage: "A new distribution center was leased and opened in Nevada during the\nquarter." — Conf: High — Note: **the Fernley opening, dated by instrument-free filing language to Q1 1999** (i.e. between 1999-01-01 and 1999-03-31; no filing gives a day). This is the only filed Nevada "opened" sentence for the quarter in which it happened.

**ST3D-06**
— Date: 1999-03-31 (and events after) — Source: Form 10-Q Q1 1999, MD&A/Overview — Source date: 1999-05-17 — Archived: `10-Q_Q1-1999...txt` L915-917 — Tier: 1 — Class: FACT — Passage: "During the first quarter, the Company leased and opened a distribution center in" — Conf: High — Corroboration: L592-593 (same document, one lineage — restatement, not independence) — Note: the same sentence continues that the Company "leased distribution centers in Kansas and Germany and is entering into leases for" further sites — i.e. **within the quarter that Fernley opened, three more sites were already committed**, two of them abroad. Read with ST3D-11 this is the build-out-in-progress claim in the company's own words.

**ST3D-07**
— Date: 1999-06-30 — Source: Form 10-Q Q2 1999, acc. 0000891020-99-001426, filed 1999-08-16 — Source date: 1999-08-16 — Archived: `../sources/10-Q_Q2-1999_acc-0000891020-99-001426_filed-1999-08-16.txt` L822-824 — Tier: 1 — Class: FACT — Passage: "the Company opened a new\ndistribution center in Nevada and announced additional new distribution centers\nto be located in Kansas, Georgia, Kentucky, Germany and the UK." — Conf: High — Note: **the verb the filing itself chooses**, and it is different for the two groups: *opened* (Nevada) vs *announced* (five sites). ST3_A-24 establishes the same sentence as the pivot of the chronology dossier; it is recorded here because the operations claim depends on it, with no independence claimed across the two dossiers.

**ST3D-08**
— Date: 1999-09-30 — Source: Form 10-Q Q3 1999, acc. 0000891020-99-001938, filed 1999-11-15, MD&A — Source date: 1999-11-15 — Archived: `../sources/10-Q_Q3-1999_acc-0000891020-99-001938_filed-1999-11-15.txt` L831-832 — Tier: 1 — Class: FACT — Passage: "distribution centers in Nevada, Georgia, Kentucky, Kansas and North Dakota and\nannounced additional new distribution centers to be located in Kentucky, Germany" — Conf: High — Note: the **five-opened / three-announced** state at the last filed date in the window, repeated in the same document at L1628-1629. Second Kentucky site is announced while a first Kentucky site is already counted as open — a detail that defeats any attempt to read the announced list as a superset of the opened list.

**ST3D-09**
— Date: 1999-09-30 — Source: Form 10-Q Q3 1999, Risk Factors — Source date: 1999-11-15 — Archived: `10-Q_Q3-1999...txt` L1628-1633 — Tier: 1 — Class: FACT — Passage: "opened distribution centers in Nevada, Georgia, Kentucky, Kansas and North\nDakota and announced plans to open new distribution centers in Kentucky, Germany\nand the United Kingdom. These distribution centers are or will be highly\nautomated and we have no previous experience with automated distribution\ncenters, as the two distribution centers in operation prior to 1999, in\nWashington and Delaware, were manually operated." — Conf: High — Note: **the single most important operational sentence in the window.** The company states on the record that (a) the pre-1999 estate was **manually operated**, (b) the 1999 estate was **automated or intended to be**, and (c) it had **no prior experience** operating the second kind. Filed as of 1999-09-30 with the first peak season still ahead (L1638-1639). This is the opposite of a claim of proven scalability.

**ST3D-10**
— Date: 1999-07-21 — Source: Form 8-K event 1999-07-21, acc. 0000891020-99-001224, filed 1999-07-22 (Amazon.co.uk premises release) — Source date: 1999-07-22 — Archived: `../sources/8-K_event-1999-07-21_acc-0000891020-99-001224_filed-1999-07-22.txt` L316-322 — Tier: 1 — Class: FACT (that the claim was made) + COMPANY CLAIM (the capacity arithmetic) — Passage: "seven distribution centers nationwide--more than 10 times the distribution" — Conf: High on the sentence; **Low-Medium on the "10 times"** — Note: a **company-asserted multiple** inside a press release furnished on Form 8-K, not an audited capacity measurement; no filing states a throughput figure for any site, and no independent count exists in the archive (method §2 record-selection null). Continues at L322 "feet in size, will provide Amazon.co.uk with a major distribution center to" — the UK site announcement. To be read against ST3D-08/09: by 1999-07-21 the company is publicly counting **seven** US DCs while its own 10-Q counted five as opened in the nine months to 1999-09-30.

**ST3D-11**
— Date: 1999-06-30 and 1999-09-30 — Source: Form 10-Q Q2 1999 L1277; Form 10-Q Q3 1999 L1338 — Source date: 1999-08-16 · 1999-11-15 — Archived: `10-Q_Q2-1999...txt` L1277; `10-Q_Q3-1999...txt` L1338 — Tier: 1 — Class: FACT — Passage: "systems, including temporary power outages at distribution centers, delayed transportation of" — Conf: High — Note: **the closest thing to a filed outage statement in the window** — power outages at distribution centres and delayed transportation appear as named failure modes inside the controls/operations discussion of two consecutive 10-Qs. Whether either was **experienced** or only **enumerated** is not resolvable from the line; the surrounding sentence is being read before this record is used in narrative (see `## Failure and constraint`). No dated Amazon outage, with duration or order loss, appears in any document in the corpus — Stage 2's null (S2D-63) stands, extended: **also no outage in 1997-99.**

**ST3D-12**
— Date: 1999-03-11 (instruments) — Source: Form 10-Q Q1 1999, EX-10.1–10.5 "Sales Agreement" (five exhibits) — Source date: 1999-05-17 — Archived: `../sources/10-Q_Q1-1999_acc-0000891020-99-000894_filed-1999-05-17.txt` (exhibit set; exhibit-index lines being verified this pass) — Tier: 1 — Class: FACT — Passage: UNKNOWN (verbatim lines to be appended with exhibit numbers) — Conf: pending — Note: **inherited correction applied** — these are The Buschman Company materials-handling **equipment purchase contracts** for Fernley Phase I / Phase II plus three "Standard Proposal" sites "yet to be determined", prices redacted under Rule 24b-2. They are the equipment instruments of the automation claim in ST3D-09 and are evidence of a build-out in progress, **not** of a network in operation and **not** of marketplace or merchant contracting.

**ST3D-13**
— Date: 1999-03-11 (instrument) — Source: Form 10-Q Q1 1999, EX-10.1 "SALES AGREEMENT, DATED MARCH 11, 1999", acc. 0000891020-99-000894, filed 1999-05-17 — Source date: 1999-05-17 — URL: https://www.sec.gov/Archives/edgar/data/1018724/000089102099000894/0000891020-99-000894.txt — Archived: `../sources/10-Q_Q1-1999_acc-0000891020-99-000894_filed-1999-05-17.txt` L1783-1798 — Tier: 1 — Class: FACT — Passage: "This Sales Agreement, hereinafter called \"Sales Agreement,\" made by and\nbetween Amazon.com, Inc., a Delaware corporation (hereinafter called\n\"Purchaser\"), and The Buschman Company, an Ohio corporation (hereinafter called\n\"Seller\"), constitutes the agreement of the parties as follows:" — Conf: High — Note: **the intake manifest's "marketplace-contract" label is wrong and this is the instrument that proves it.** Amazon is the *buyer of machines*; the counterparty is a materials-handling manufacturer. Nothing in the exhibit concerns third-party sellers, merchants, commissions or payments.

**ST3D-14**
— Date: 1999-01-18 (proposal) / 1999-03-11 (contract) — Source: Form 10-Q Q1 1999, EX-10.1 §A "CONTRACT DOCUMENTS" — Source date: 1999-05-17 — Archived: `10-Q_Q1-1999...txt` L1810-1811 — Tier: 1 — Class: FACT — Passage: "1. The Phase I Fernley, Nevada Proposal for Amazon.com, Inc. dated\nJanuary 18, 1999" — Conf: High — Note: **the equipment for Fernley was specified on paper six weeks before the contract and while the building was still "expected to begin operations in 1999"** (ST3D-04). Phase I therefore dates to 1999-01-18, not to the Fernley opening — the machine estate has its own chronology, independent of the lease chronology, and the two must not be merged.

**ST3D-15**
— Date: 1999-03-11 — Source: Form 10-Q Q1 1999, EX-10.2 (Phase II) §A — Source date: 1999-05-17 — Archived: `10-Q_Q1-1999...txt` L3520 — Tier: 1 — Class: FACT — Passage: "1. The Phase II Fernley, Nevada Proposal for Amazon.com, Inc. dated" — Conf: High — Note: **Phase II is contracted in the same filing as Phase I**, i.e. the company committed to a second expansion of the same site within the same instrument set, before Phase I equipment had been accepted. Contract structure is the evidence; no filing dates Phase II's completion inside the window.

**ST3D-16**
— Date: 1999-02-05 (proposal) / 1999-03-11 (contracts) — Source: Form 10-Q Q1 1999, EX-10.3, EX-10.4, EX-10.5 §A — Source date: 1999-05-17 — Archived: `10-Q_Q1-1999...txt` L5470-5473 · L7313-7316 · L9175 — Tier: 1 — Class: FACT — Passage: "1. The Standard Proposal for Amazon.com, Inc. dated February 5, 1999," … "purposes hereof such proposal shall apply to \"Site A\" yet to be determined" — Conf: High — Corroboration: "Site B" at L7316 and "Site C" at L9175 — same accession, one lineage — Note: **three contracts for sites the company could not yet name**, signed on one day under one price structure. This is the strongest single document-level proof in the corpus that the 1999 network was a *programme in progress* rather than a built estate: the vendor contracts were standardised and executed ahead of site selection by at least two months (1999-02-05 proposals → Q2/Q3 openings).

**ST3D-17**
— Date: 1999-03-11 — Source: Form 10-Q Q1 1999, EX-10.2 OPTIONS page — Source date: 1999-05-17 — Archived: `10-Q_Q1-1999...txt` L3443-3458 — Tier: 1 — Class: FACT — Passage: "Add gravity flanker conveyor to second side of existing powered\ntake-away on the third level of the 8 existing pick module fingers." — Conf: High — Note: **the only machine description in the window that is specific enough to read as engineering rather than as boilerplate** — a gravity flanker conveyor, a powered take-away, a third level, "8 **existing** pick module fingers". The word "existing" inside an *option* to the Phase II proposal shows Phase I equipment was already installed or committed to configuration by 1999-03-11, and the option is marked "[X]   ACCEPTED" (L3453). Selection of an add-on is dated evidence of a build-out in mid-course.

**ST3D-18**
— Date: 1999-03-11 — Source: Form 10-Q Q1 1999, exhibit index and legend — Source date: 1999-05-17 — Archived: `10-Q_Q1-1999...txt` L1660-1669 (index; repeated at L1754-1763) · L1678-1680 · L2245 · L3458 — Tier: 1 — Class: FACT — Passage: "**    Contains omitted, confidential material, which material has been filed" … "under Rule 24b-2, promulgated by the SEC under the Securities Exchange Act" — Conf: High — Note: **the price of the automation is not in the public record.** Exhibit numbers 10.1-10.5 are all the Buschman set; the redaction marker "[*]" and the legend appear at L2245, L2310, L2942, L3388, L3481, L4008 and throughout, and the option price prints as "TOTAL ADD TO BASE PRICE    $[*]" (L3458). **Any dollar figure for the Fernley automation is therefore UNKNOWN from the instruments**; only the accounting consequence survives (ST3D-27 onward). This is a documented EMPTY, not an unfetched number.

**ST3D-19**
— Date: 1999-03-11 — Source: Form 10-Q Q1 1999, EX-10.2 installation notes — Source date: 1999-05-17 — Archived: `10-Q_Q1-1999...txt` L5400-5402 · L5406-5408 — Tier: 1 — Class: FACT — Passage: "Installation services are based on using nonunion labor during regular\n        working hours. Buschman uses overtime labor, as applicable, to make any\n        tie-ins that would affect operations." — Conf: High — Note: **contractual labour terms for the build-out**, and the only filed evidence of how the new machines were put in: non-union installation crews, with overtime reserved specifically for tie-ins "that would affect operations". The same page states "This price is a total price for the conveyor system. The equipment being\n        manufactured and stored, based on the blanket order, will be applied and\n        the price deducted as necessary." (L5406-5408) — a **blanket order**, i.e. equipment manufactured and warehoused against future sites, which is the procurement shape of a network being built faster than sites are chosen.

**ST3D-20**
— Date: 1999-03-11 — Source: Form 10-Q Q1 1999, Buschman exhibit set (EX-10.1 through EX-10.5), searched for capacity language — Source date: 1999-05-17 — Archived: `10-Q_Q1-1999...txt` (full-text term search, this session) — Tier: 1 — Class: UNKNOWN (documented absence within the instruments) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High for absence-in-document, Medium for absence-in-fact — Note: the five exhibits contain **no throughput guarantee, no orders-per-hour figure and no completion date** in the public text. The only "per hour" string in the whole Q1-1999 filing is an air-handling specification, "C to give 4 air rotations per hour shall be completed on or" (L11150) — ventilation, not capacity. **The scalability claim of the 1999 network is therefore not quantified anywhere in the instruments that built it.**

**ST3D-21**
— Date: 1998-12-31 → 1999-09-30 — Source: Form 10-K FY1998 Item 2 L1068-1070; Form 10-Q Q1-1999 L592-593; Q2-1999 L822-824; Q3-1999 L831-832, L1628-1629 — Source date: 1999-03-05 · 1999-05-17 · 1999-08-16 · 1999-11-15 — Archived: as cited in ST3D-04/05/07/08 — Tier: 1 — Class: DERIVED (from filed statements) — Passage: see ST3D-04, -05, -07, -08 — Conf: High — Note: **the count of distribution centres filed as OPENED inside the window is: Delaware (1997), Nevada/Fernley (Q1-1999), Georgia, Kentucky, Kansas, North Dakota (all by 1999-09-30) = six**, plus Seattle operating throughout; Regensburg and Slough are filed as operating foreign sites. Announced-but-not-open at the last filed date: Kentucky (second), Germany, United Kingdom. Arithmetic: five opened in the nine months to 1999-09-30 (Q3-1999 L831-832 list) + New Castle (1997) = six new sites opened, against **one** site opened across the company's whole life before this window.

**ST3D-22**
— Date: 1999-06-30 → 1999-09-30 — Source: Form 10-Q Q3 1999, MD&A — Source date: 1999-11-15 — Archived: `10-Q_Q3-1999...txt` L927 — Tier: 1 — Class: FACT — Passage: "Split shipments may also increase due to recent openings of distribution centers" — Conf: High — Note: **the first filed operational *cost* of the multi-site network.** Once inventory is spread across sites, one customer order can become two parcels; the company flags it as a margin and shipping-quality issue, not a benefit. Read with ST3D-23 this is the operational constraint the build-out created, and it is disclosed within one quarter of the openings.

**ST3D-23**
— Date: 2000-03-23 (filing) / 1999-12-31 (state) — Source: Form 10-K FY1999, acc. 0000891020-00-000622, filed 2000-03-23 — Source date: 2000-03-23 — URL: https://www.sec.gov/Archives/edgar/data/1018724/000089102000000622/0000891020-00-000622.txt — Archived: `../sources/10-K_FY1999_acc-0000891020-00-000622_filed-2000-03-23.txt` — Tier: 1 — Class: FACT (that the document exists on disk and is unmined) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Note: **the FY1999 10-K and the FY1999 10-K/A (acc. 0000891020-00-001638, filed 2000-09-08) are present in `sources/` and are cited zero times across `ST3_A_chronology_org.md`, `ST3_B_finance.md`, `ST3_C_product_market.md`, `_EVIDENCE_CACHE.md` and `CORRECTIONS.md`** (verified by string count for "10-K_FY1999", "acc-0000891020-00-000622" and "2000-03-23": 0 hits in each). This dossier therefore closes Stage 3 **at 1999-12-31 on audited evidence**, and hands the discovery back to the siblings as an outbound correction. **Time-audit flag (method §6):** the document post-dates the window; it is admissible for *state at 1999-12-31* and inadmissible as anything a contemporaneous observer could have read before 2000-03-23. Every FY1999-based record below carries that flag.

**ST3D-24**
— Date: 1999 (fiscal year) — Source: Form 10-K FY1999, Item 1 "WAREHOUSING, INVENTORY, FULFILLMENT AND DISTRIBUTION" — Source date: 2000-03-23 — Archived: `10-K_FY1999...txt` L568-573 — Tier: 1 — Class: FACT — Passage: "We significantly expanded our US distribution infrastructure in 1999 with\nthe addition of new distribution facilities in Fernley, Nevada; Coffeyville,\nKansas; Campbellsville, Kentucky; Lexington, Kentucky; McDonough, Georgia; and\nGrand Forks, North Dakota. We also opened two new international distribution\ncenters, one in the UK and one in Germany. On an aggregate basis, these eight\nnew distribution centers comprised approximately four million square feet of" — Conf: High — **Time-audit: filed after the window** — Note: **the first filing in the corpus that names the new sites by city**, converting ST3D-08's anonymous "Georgia, Kentucky, Kansas and North Dakota" into McDonough GA, Campbellsville KY, Lexington KY, Coffeyville KS, Grand Forks ND. Six US + two international = eight new, ~4.0M sq ft (company's own aggregate).

**ST3D-25**
— Date: 1999-12-31 — Source: Form 10-K FY1999, Item 1 — Source date: 2000-03-23 — Archived: `10-K_FY1999...txt` L576-580 — Tier: 1 — Class: FACT — Passage: "The new distribution centers also give us\nmore control over the distribution process and facilitate our ability to deliver\nmerchandise to customers on a reliable and timely basis. We now have a total of\n10 distribution centers, including our facilities in Seattle, Washington, and\nNew Castle, Delaware." — Conf: High — Time-audit: filed after the window — Note: **the closing state of the network: ten distribution centres**, of which eight opened during 1999. The 8→10 arithmetic is the company's own; the four pre-existing sites it must include (Seattle, New Castle, Slough, Regensburg) are only partly enumerated, so the count is **internally unverifiable from this document alone**: 8 new + 2 named = 10 leaves no room for the UK/German legacy sites named at L1610-1617. **See Contradictions U.D4.**

**ST3D-26**
— Date: 1999-12-31 — Source: Form 10-K FY1999, Item 2 PROPERTIES — Source date: 2000-03-23 — Archived: `10-K_FY1999...txt` L1596-1608 — Tier: 1 — Class: FACT — Passage: "eight distribution centers located in Seattle, Washington; New Castle, Delaware;\nFernley, Nevada; Lexington, Kentucky; Campbellsville, Kentucky; McDonough,\nGeorgia; Coffeyville, Kansas and Grand Forks, North Dakota. These distribution\ncenters comprise a total of approximately 3.8 million square feet." — Conf: High — Time-audit: filed after the window — Note: **the US estate at the endpoint, in one filed sentence, with square footage and lease expiries** (Seattle October 2000, Delaware October 2002, "the remaining distribution center leases expire from 2008 through 2015"; US offices ~730,000 sq ft; "The Company does not own any real estate."). Arithmetic to hold against ST3D-24: the same document prices **eight US sites at ~3.8M sq ft** and **eight new sites (six US + two European) at ~4.0M sq ft** — two different "eights", so neither figure may be quoted as "the network" without saying which eight.

**ST3D-27**
— Date: 1999-12-31 → 2000-04 — Source: Form 10-K FY1999, Item 2 — Source date: 2000-03-23 — Archived: `10-K_FY1999...txt` L1610-1617 — Tier: 1 — Class: FACT + FACT (forward commitment) — Passage: "including approximately 121,000 square feet of office space in Germany\nand the UK and a distribution center in each country with a combined 690,000\nsquare feet of available space. The UK subsidiary will begin leasing an\nadditional 500,000 square feet of distribution center space in Marston Gate,\nEngland in April 2000." — Conf: High — Time-audit: filed after the window — Note: **the endpoint of the build-out lies outside the window**: the largest announced UK site (500,000 sq ft, Marston Gate, lease to March 2025) begins leasing **April 2000**. German DC at Bad Hersfeld, lease to December 2009 (L1615-1617). Stage 3's "scalable network" claim therefore ends with a site not yet held.

**ST3D-28**
— Date: 1999-12-31 — Source: Form 10-K FY1999, Item 1 "Customer Service" — Source date: 2000-03-23 — Archived: `10-K_FY1999...txt` L559-564 — Tier: 1 — Class: FACT — Passage: "centers located in Seattle and Tacoma, Washington; Slough, England; Regensburg,\nGermany; and Grand Forks, North Dakota. We plan to open additional customer\nservice centers in Huntington, West Virginia and The Hague, Netherlands in 2000." — Conf: High — Time-audit: filed after the window — Note: **the service estate is a separate geography from the fulfilment estate** — Tacoma (not a DC site) and Grand Forks (a DC site) both host customer service; five centres at the date, two more planned for 2000. Also filed: "We have automated certain tools used by our\ncustomer service staff and have plans for further enhancements." (L559-560) — customer-service automation is claimed as *partial* ("certain tools") with enhancement pending.

**ST3D-29**
— Date: FY1997 / FY1998 / FY1999 — Source: Form 10-K FY1999, Statements of Cash Flow — Source date: 2000-03-23 — Archived: `10-K_FY1999...txt` L2852 — Tier: 1 — Class: FACT + DERIVED — Passage: "Purchases of fixed assets..................................     (287,055)     (28,333)      (7,603)" — Conf: High — Note: **the money trail of the physical network, in one filed row, in thousands of dollars: $7,603K (1997) → $28,333K (1998) → $287,055K (1999).** Derived: 1998/1997 = 3.73x; 1999/1998 = 10.13x; 1999/1997 = 37.8x; FY1999 alone is **8.0x the two prior years combined** (287,055 ÷ (7,603 + 28,333 = 35,936) = 7.99). Printed with the arithmetic so no later reader mistakes a 1999 spend rate for the company's historical norm.

**ST3D-30**
— Date: 1998-12-31 / 1999-12-31 — Source: Form 10-K FY1999, Note "Fixed Assets" — Source date: 2000-03-23 — Archived: `10-K_FY1999...txt` L3487-3496 — Tier: 1 — Class: FACT + DERIVED — Passage: "Construction in progress...............................    83,290       1,760" — Conf: High — Time-audit: filed after the window — Note: **the single hardest number for this dossier's central claim.** Gross fixed assets 43,585 → **366,977** (8.42x) in one year, but **$83,290K of it sat in construction in progress at 1999-12-31** (derived: 83,290 ÷ 366,977 = 22.7% of the estate not yet in service and therefore not yet depreciating), against $1,760K a year earlier. **A fifth of the money spent on the network was still not operational at the endpoint** — which is exactly the difference between a build-out in progress and a network in operation. "Leased assets" also moves 442 → **52,374** (118.5x, derived), i.e. the new machine estate is being financed, not bought; and the Company "capitalized approximately $3.4 million of interest during the\nyear ended December 31, 1999" (L3500-3501), the first capitalised-interest figure in the corpus.

**ST3D-31**
— Date: 1997-12-31 / 1998-12-31 — Source: Form 10-K FY1997 Note (L2294-2308) vs Form 10-K FY1998 Note (L2738-2753) — Source date: 1998-03-30 / 1999-03-05 — Archived: `10-K_FY1997...txt` L2300-2308; `10-K_FY1998...txt` L2745-2753 — Tier: 1 — Class: FACT + DERIVED — Passage: "Computers and equipment.....................................  $ 7,118    $1,031" (FY1997) vs "Computers and equipment...........................  $33,061    $7,562" (FY1998, 1997 column) — Conf: High — Note: **the FY1997 gross fixed-asset total is printed twice, differently**: 12,899 (FY1997 10-K, incl. leased assets 362) vs 13,490 in the FY1998 10-K's 1997 column (leased assets 442) — derived difference **+$591K gross, +$461K net** (9,265 vs 9,726), with no reconciling note in the corpus. Also from the FY1998 note: **purchased software is flat 4,560 → 4,547 (−13) while computers and equipment quadruples 7,562 → 33,061 (4.4x, derived) and leasehold improvements go 926 → 5,535 (6.0x, derived)**. The 1998 investment was in hardware and buildings, **not** in licensed or capitalised software.

**ST3D-32**
— Date: FY1997 / FY1998 / FY1999; quarters of 1999 — Source: FY1997 10-K L2037; FY1998 10-K L2232; FY1999 10-K L2820; 10-Q Q1/Q2/Q3-1999 L324/L299/L314 — Source date: 1998-03-30 · 1999-03-05 · 2000-03-23 · 1999-05-17 · 1999-08-16 · 1999-11-15 — Archived: as cited — Tier: 1 — Class: FACT + DERIVED — Passage: "  Depreciation and amortization of fixed assets............       36,806        9,421        3,442" — Conf: High — Note: **depreciation is the shadow the systems estate casts on the P&L, and it is the only continuous filed series for infrastructure spend in the window.** As filed ($000): FY1997 3,388 (own printing) / 3,442 (restated); FY1998 9,692 (own) / 9,421 (restated in FY1999); FY1999 36,806. Quarterly 1999 cumulative as filed: 5,223 → 13,325 → 22,935 (10-Qs), so single quarters are **Q1 5,223; Q2 8,102; Q3 9,610; Q4 13,871 (derived: 36,806 − 22,935)**. Q4 alone exceeds all of FY1998 (13,871 vs 9,421 = 1.47x, derived) — the assets placed in service in the run-up to the first automated peak season. **Both years print twice with different values; see Contradictions U.D1.**

**ST3D-33**
— Date: 1999-12-31 — Source: Form 10-K FY1999, "EMPLOYEES" — Source date: 2000-03-23 — Archived: `10-K_FY1999...txt` L684 — Tier: 1 — Class: FACT — Passage: "As of December 31, 1999, the Company employed approximately 7,600 full-time" — Conf: High — Time-audit: filed after the window — Note: **a third filed headcount date exists**, so the documented null at ST3_A-18 ("filed headcount exists at exactly two dates, 1997-12-31 and 1998-12-31") is true of *filings made inside the window* but not of the *endpoint state*. Derived series as filed: 614 full-time (1997-12-31) → ~2,100 all-basis (1998-12-31) → ~7,600 full-time (1999-12-31); 7,600/2,100 = 3.62x, 7,600/614 = 12.4x (basis caveat inherited from ST3A-17 — 1998 is not stated as full-time). Outbound correction issued.

**ST3D-34**
— Date: 1999 (year) — Source: Form 10-K FY1999, Risk Factors — Source date: 2000-03-23 — Archived: `10-K_FY1999...txt` L1049-1054 — Tier: 1 — Class: FACT (retrospective statement of an incurred charge) — Passage: "In the fourth quarter of 1999, we incurred inventory-related charges, which significantly decreased our gross margins. A failure to optimize inventory\nat our distribution centers will harm our shipping margins by requiring us to\nmake partial shipments from one or more locations. In addition, we may\nexperience a decline in our shipping margins due to complimentary upgrades and\nsplit-shipments necessary to ensure timely delivery for the holiday season." — Conf: High — Time-audit: filed after the window, describing an event inside it — Note: **the only operational failure in the window that the company states it actually incurred rather than merely risked.** It is not dated to a day and the charge amount is not given in this sentence. It is the direct fulfilment cost of the multi-site network forecast by ST3D-22 (Q3-1999 split-shipment warning): partial shipments from one or more locations, complimentary upgrades, split-shipments — the network's first peak produced markdowns and shipping-margin erosion.

**ST3D-35**
— Date: 1999-12-31 — Source: Form 10-K FY1999, Risk Factors — Source date: 2000-03-23 — Archived: `10-K_FY1999...txt` L1026-1032 · L1059-1062 — Tier: 1 — Class: FACT — Passage: "highly automated, and we have had limited experience with automated distribution\ncenters." — Conf: High — Note: **the second relaxation of an experience claim in this dossier's own corpus.** Q3-1999 said "we have no previous experience with automated distribution centers" (ST3D-09); the FY1999 report six weeks later says "limited experience", and re-asserts that the two pre-1999 sites "are manually operated" (L1027-1028). The same page keeps the failure options open — "our new automated distribution centers may fail to operate\nproperly, which will interfere with our ability to meet customer demand" (L1061-1062) — and discloses a labour constraint, "we may be unable to adequately staff our distribution and customer service centers during these peak\nperiods" (L1059-1060). Also filed here: "We are not experienced in coordinating and\nmanaging distribution operations in geographically distant locations." (L1028-1029) and the over-expansion warning L1029-1032.

**ST3D-36**
— Date: 1997-05-14 → 1999-12-31 — Source: Form 10-K FY1999 Item 1 vs S-1/A No. 5 (S2D-05) — Source date: 2000-03-23 vs 1997-05-14 — Archived: `10-K_FY1999...txt` L582-594 — Tier: 1 — Class: FACT + INFERENCE — Passage: "our proprietary software selects the orders that can be filled via\nelectronic interfaces with vendors and, in some cases, forwards the remaining\norders to our special orders group." — Conf: High — Note: **the order-routing design described at the IPO is still the design three and a half years later**, in nearly the same words, including the manual residual ("special orders group … consists of trained ordering personnel who\nspecialize in hard-to-find products", L587-589) and the distributor dependency ("electronically ordered products often are shipped to us by the distributor within hours of a receipt of an order from us", L589-591). Inference (mechanism stated, magnitude UNKNOWN): automation was installed in the *buildings*, not in the *sourcing* — the company still did not own what it could not fill from inventory. The FY1999 sentence adds the consequence: "With the addition of\nnew distribution centers and product lines, we are required to carry increased\nlevels of inventory" (L591-594).

**ST3D-37**
— Date: 1999-12-31 — Source: Form 10-K FY1999, Item 1 Summary — Source date: 2000-03-23 — Archived: `10-K_FY1999...txt` L209-217 — Tier: 1 — Class: COMPANY CLAIM (self-assessment) — Passage: "technology leader, having developed electronic commerce innovations such as\n1-Click technology, personalized shopping services, easy-to-use search and\nbrowse features, secure payment protections and wireless access to our stores." — Conf: Medium (the claim is filed; the ranking is not evidenced) — Note: the capability inventory as the company described it at the endpoint. Each element is separately dated in this corpus: 1-Click appears in the 8-Ks from **1999-01-05** (see ST3D-44), personalisation traces to the 1997 lineage (S2D-30), search to Junglee (ST3D-45). **No independent technical benchmark for any of the four exists in the archive.**

---

## Fulfilment build-out

To be filled: one row per site — dated instrument / filed opening statement / size / status (operating · committed · announced).

---

## Systems and capability table

To be filled.

---

## Technical labour, as filed and as unknowable

To be filled. Headcount is filed at exactly two dates in the window (ST3_A-15/16/17/18); the null is documented, not filled in.

---

## Operations metrics

To be filled.

---

## Failure and constraint

To be filled.

---

## Timeline

To be filled.

---

## Data gaps

To be filled — EMPTY / UNANSWERED / UNTRIED kept distinct.

---

## Contradictions

To be filled.

---

## Sources consulted

To be filled.

---

## Provenance and method notes

To be filled.

---

## Outbound corrections

To be filled.

---

## CSV append rows

To be filled.
