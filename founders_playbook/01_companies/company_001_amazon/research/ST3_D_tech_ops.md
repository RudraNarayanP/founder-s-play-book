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
