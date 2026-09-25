# AMAZON STAGE 3 — E. ADVERSARIAL REVIEW

**Dataset:** THE FOUNDER'S PLAYBOOK — forensic reconstruction, Company 001 Amazon.com (CIK 1018724).
**Stage:** 3 (adversarial). **Window under attack: 1997-05-16 → 1999-12-31**, the span Stage 2's boundary
fixed and the two/three Stage-3 dossiers worked inside.
**Target of this review:** `research/ST3_A_chronology_org.md` (boundary 1999-06-30 substantive /
1999-08-16 disclosed), `research/ST3_C_product_market.md` (category, supply, competition, market), and —
since it was on disk when this pass ran and is not named in my brief — `research/ST3_B_finance.md`, which
this review also attacks. Registers under review: `conflicts.csv`, `data_gaps.csv`, `quantitative.csv`,
`sources.csv`, and `sources/STAGE3_INTAKE_MANIFEST.md`.
**Stage definition tested here (method §6):** the earliest defensible point at which the company had become
a **materially scalable operating organisation rather than a promising startup**.
**Hindsight firewall (method §2):** nothing below uses the 2000 collapse, the later marketplace's size, or
Amazon's eventual dominance as evidence. Where I know a later fate (PlanetAll, Accept.com, zShops, the
Fernley site), it is excluded, not down-weighted. Several attacks here work *because* the later fate is
excluded: they ask what the 1999 record alone can carry.
**Independence and filing-lineage (method §3):** every downgrade below is a **provenance** downgrade, not a
refutation. An element may be true *and* folklore; the verdict column says which.
**Confidence scale:** High (2+ independent sources or primary document) · Medium (one reliable source) ·
Low (conflicting/vague/retrospective-only) · UNKNOWN.

**Scoring convention used in every record.**
- **LANDED** — the dossier's claim, as written, does not survive; text must change.
- **HELD** — I attacked and the document defended it.
- **DOWNGRADE** — the claim survives as a fact about the record but loses evidential weight (single lineage,
  self-report, or convention-of-silence).
- **UNANSWERED / UNTRIED** — no document found; stated with status, never converted into a conclusion.

---

## Working method and budgets

**Method.** Local mining only against `founders_playbook/01_companies/company_001_amazon/sources/`
(97 files: 2 × 10-K, 8 × 10-Q, 24 × 8-K + 1 × 8-K/A, 2 × ARS, 2 × DEF 14A + 2 × PRE 14A, 13 × S-1 lineage,
6 × S-3, 4 × S-4 lineage, 9 × S-8, 3 × POS AM, 2 × SC 13G, 1 × 8-A12G, 3 × 424B, plus the Stage-1/2 web
artifacts and the intake manifest). Every attack is run by reading the named line of the named file, and
every recomputation uses only figures printed in that corpus, with the arithmetic shown.
Method §14 rule 8 was applied before writing any inherited figure: each number taken from ST3_A or ST3_C
was re-grepped against `sources/` here, and where it did not print, it is reported as such below rather
than repeated. Counts in **my own brief** were checked the same way and two of them are wrong; see
`## Outbound corrections` OC-201/OC-202 — an adversarial pass that exempts its own instructions is not
adversarial.

**Web budget: 0 of 8 WebSearch, 0 of 8 WebFetch spent.** This pass found no gap that a web request could
settle: the surviving gaps (Buschman redacted prices, Rule 24b-2 release orders, Section 16 forms, the
FY1999 10-K, the periodicals family) are either EDGAR-catalogue tasks for the registrar or the four-family
work §14 rule 6 assigns to a retrieval pass, not to an adversarial one. Each is recorded as **UNTRIED** in
`## Data gaps` with the reason it was not bought.

**Turn budget.** ~90 turns; wrote first, appended after each source, per §14 rule 1.

---

## Attacks

Records are numbered `ST3E-nn`. Each states the claim attacked, the document it was tested against, the
recomputation where one applies, and the verdict.

### ST3E-01 — Attack on the boundary's Axis P: the "first filing that says *opened*" is not the Q2 1999 10-Q

**Claim attacked** (ST3_A, candidate C4 row): the Q2 1999 10-Q is "**the first filing in the whole corpus
that uses 'opened'**", converting a leased facility into an operating one — presented as the reason Axis P
passes at 1999-06-30.
**Test.** Search every 10-Q and 8-K on disk for the past tense of the company putting a distribution centre
into service.
**Finding.** The Q1 1999 10-Q, acc. 0000891020-99-000894, filed **1999-05-17** — a document ST3_C read and
ST3_A did not — states, verbatim: "A new distribution center was leased and opened in Nevada during the
quarter." ST3_C carries it as ST3C-28 and ST3C-43. So the first *filed* use of "opened" is a document dated
three months earlier than the endpoint it is supposed to justify, reporting the quarter ended 1999-03-31.
**Consequence.** Under the dossier's own capability / declaration / operation test, Axis P passes at
**1999-03-31**, not 1999-06-30. Either the test is applied inconsistently or the Q2 1999 sentence is doing
no work: the Q2 1999 10-Q's Nevada statement ("During the six months ended June 30, 1999 the Company opened
a new distribution center in Nevada") is a *re-recital* of an event the same company had already reported as
complete. It is the same corporate record, one accession later.
**Verdict: LANDED** (as an error of priority, and it moves the boundary's own evidence a quarter earlier).
Confidence High; the two quoted strings are on disk at the cited files.

### ST3E-02 — Attack on the boundary's Axis T: "commissions recognised" proves presence, and the same lineage calls the amount *minimal*

**Claim attacked** (ST3_A, C4): third-party fees and commissions are "inside the reported revenue line" at
Q2 1999 — Axis T passes; the dossier then concedes "the magnitude is nowhere disclosed".
**Test.** Ask what the immediately preceding document in the same lineage says about the magnitude of the
same revenue stream, and whether any 1999 filing quantifies it.
**Finding.** The Q1 1999 10-Q: "The Company launched Amazon.com Auctions late in the quarter ended
March 31, 1999. Revenue related to auction services was minimal." ST3_C, ST3C-25/M-29. No filing in the
corpus disaggregates auctions or zShops revenue at any date (ST3_A G-04, ST3_C data gaps, ST3_B U1). The
Q3 1999 10-Q defines net sales as including "commissions from auctions and zShops transactions" **and**
warns that the popularity of those services "may vary over time due to perceived" demand (ST3_A ST3A-55).
**Corroborating arithmetic against the claim.** Gross margin on the filed quarterly data runs
Q1 1999 22.1% → Q2 1999 21.5% → Q3 1999 19.8% (ST3_B §U2(a)). A commission stream carries no merchandise
cost; if commissions were material to net sales, the mechanical effect is *upward* on the blended margin.
The blended margin fell for two quarters straight through the period Axis T is supposed to pass. The
company's own stated cause is first-party mix ("music and video gross margins are lower than book gross
margins"; toys and electronics from July 1999). That is consistent with the third-party line being present
and immaterial — which is what "minimal" said.
**Verdict: LANDED in part.** Axis T cannot carry boundary weight at 1999-06-30: it is a *definition*
change with no amount, one quarter after the same registrant called the same stream minimal. The dossier's
own limitation clause ("presence, not materiality") is correct; what must change is the table's verdict
cell, which reads PASS and is then used as one of three simultaneous legs of the recommendation. Recorded
as **DOWNGRADE of Axis T from PASS to PASS-on-definition-only**.

### ST3E-03 — Attack on the boundary's Axis M: a single offer letter is not an operating organisation

**Claim attacked** (ST3_A, C4): "a President/COO sits *between* the founder and the operating business",
documented by the "Offer Letter of Employment to Joseph Galli, dated June 23, 1999" filed as EX-10.1 —
"the only filed post-IPO executive hiring package in the whole set".
**Test.** (i) Is an offer letter evidence that a management structure exists, or evidence of an intention to
employ one person? (ii) Is there any second document in the window showing what Galli ran, or that the
structure beneath him existed? (iii) Is a hire of one executive not exactly what a promising startup does?
**Finding.** The instrument proves the appointment and the board seat; ST3_A's own data gaps show that
**no 8-K announced either the COO or the CFO change** (ST3A-59), that the successor to the departed VP of
Operations is **UNKNOWN** (ST3A-38), and that the person who signed as principal financial officer between
Covey and Jenson "is not named to a title in any filing on disk" (ST3A-59). The corpus therefore documents
*the top of a structure* and not the structure. Nothing in the window files an organisation chart, a
divisional reporting line, or a segment view — and none was required (method §2 record-selection null).
**Counter-consideration, recorded because it partially defends the dossier:** the Q2 1999 10-Q is also the
first document in which a second officer signs the filing in person (Galli, L2303) and in which the founder
is described as "founder and CEO" with someone else as President and COO. That is a real change in the
filed governance description, not merely a personnel event.
**Verdict: DOWNGRADE, not refuted.** Axis M at 1999-06-30 rests on **one document about one person**. Since
ST3E-01 removes Axis P's priority and ST3E-02 removes Axis T's weight, the recommended date is pinned to
this single leg — which is the finding the auditor will make first. Confidence High that the corpus contains
nothing further; Medium that this matters (see `## Boundary challenge`).

### ST3E-04 — Attack on the *test itself*: are "opened / commissions / officer" materially scalable, or three ordinary corporate events?

**Claim attacked:** the framing of the Stage-3 endpoint as reached when those three things are simultaneously
documented.
**Test.** Ask of each whether it is *distinguishing* — i.e. would a merely promising startup also pass it?
- *A distribution centre filed as opened.* Any company that has raised money and outgrown one building
  opens a second. New Castle was opened in November 1997 (ARS 1997, "the launch of our second distribution
  center in Delaware in November", ST3C-50) and that fact was not offered as a boundary. Fernley's opening
  is not categorically different in kind; the difference is one of square footage, which the filings do not
  align to the opening verb.
- *Commissions recognised.* A definitional MD&A sentence, unquantified (ST3E-02).
- *An officer hired.* One person (ST3E-03).
**What the record does hold that is *not* an ordinary startup event** — and which the dossiers under-use:
(i) the company's own admission that through 1998 it had run **only manually operated** warehouses: "These
distribution centers are or will be highly automated and we have no previous experience with automated
distribution centers, as the two distribution centers in operation prior to 1999, in Washington and
Delaware, were manually operated" (10-Q Q3 1999, L1624-1635, ST3C-42) — a company-measured statement that
the *pre-1999* organisation had never operated the kind of plant it was claiming as scale; (ii) five
separately incorporated single-purpose operating entities appearing on the record with dated instruments —
Amazon.com.ksdc, Inc. (Kansas lease 1999-04-12), Amazon.com Auctions, Inc., ADC Acquisitions, Inc.,
AI Acquisition, Inc. (ST3A-33, ST3C-24) — i.e. the *legal* skeleton of a multi-entity operating group;
(iii) an acquisition-currency shelf raised 5,000,000 → 15,000,000 → 30,000,000 shares inside one lineage
(ST3A-49); (iv) rental expense $270,000 → $2.1M → $8.5M, audited (ST3A-26).
**Verdict: LANDED as a test defect.** The three chosen legs are individually non-distinguishing; two
distinguishing facts (the manual-to-automated admission, and the subsidiary/incorporation spine) sit in the
same dossiers and were not promoted into the test. `## Boundary challenge` re-runs the candidates under the
corrected test.

### ST3E-05 — Attack on the FY1998-close rejection, argument 3: "international share *fell* 33% → 25% → 20%" is a share-versus-flow argument and does not say what ST3_A uses it to say

**Claim attacked** (ST3A-30, note): "**decisive against** the 'geographic expansion' boundary candidate on
revenue terms … the international mix declined by 13 percentage points".
**Test.** Recompute the dollar flows behind the percentages, using only the filed annual net-sales figures
and the filed percentages (FY1998 10-K L1324-1326 and L1222/L1309).
**Arithmetic (DERIVED).** 1996: 0.33 × 15,746 = **$5.2m**. 1997: 0.25 × 147,787 = **$36.9m** (×7.1). 1998:
0.20 × 609,996 = **$122.0m** (×3.3 on 1997). Whole-company growth 1997→1998 = 4.13×.
**Reading.** The international *business* tripled in one year and grew 23-fold over two. Its *share* fell
because the US base grew faster, and because the two local stores (Amazon.co.uk, Amazon.de) opened only in
October 1998 — a full quarter of the measurement year. A declining share of a faster-growing total is not
evidence against scale; it is arithmetic. ST3_A uses it as a decisive fact against C3, which it cannot bear.
**Verdict: LANDED** as a defective argument against C3 — but see ST3E-06/07/08: the candidate still fails,
for reasons the dossier did not use.

### ST3E-06 — Attack on the FY1998-close rejection, argument 2: the officer table "contracting from eight names to seven" is a disclosure artefact

**Claim attacked** (C3 row, Axis M): "the executive-officer table **shrinks from 8 names to 7** … no COO
exists" — used as a FAIL on the managerial axis.
**Test.** Read what the two tables actually are, and read ST3_A's own contradiction entry.
**Finding.** The Item 401(b)/Part I "Executive Officers" list names officers *at the filing date*; the
Summary Compensation Table names people who were officers at year-end or would have ranked among the top
four (Item 402(a)(3)(iii)). ST3_A's own U.206 records that Aposporos is absent from the FY1998 table yet is
paid $142,083 for 1998 in the 1999 proxy as "Vice President of Business Development" — the title the FY1998
table gives to Shriram — and the entry ends: "Do not describe the officer roster as simply '8 then 7'
without noting that a ninth person holding a listed officer's title was still being paid." The dossier
wrote that caution and then used "8 then 7" as a boundary-carrying FAIL twice (C1 row, C3 row, and again in
the "argument against this recommendation").
**Verdict: LANDED.** A name-count in a compliance table is not a measure of management depth and may not
carry an endpoint. Also a self-inflicted inconsistency inside ST3_A.

### ST3E-07 — Attack on the FY1998-close rejection, argument 1: the 10-K's "intends to establish one or more additional distribution centers" — verbatim check, and what it does and does not prove

**Claim attacked** (C3 row, Axis P): the FY1998 10-K "still says 'The Company intends to establish one or
more additional distribution centers within the next 12 months'", so the network is unfinished.
**Test.** Locate the sentence, its section, and the sentences around it.
**Finding.** Verified as printed in the FY1998 10-K's Property/lease-commitment discussion; it is a forward
statement inside Item 2, sitting next to Item 2's *completed* list of facilities then housing operations.
The sentence proves only that more was planned; every filing in the window also states that more is planned
(the Q2 1999 sentence the boundary relies on announces five more sites in the same breath as the Nevada
opening). If "an intention to grow" disqualifies a date, no date in the window qualifies, because the
company never stopped announcing sites.
**Verdict: LANDED as reasoning, HELD as conclusion.** The intent sentence cannot by itself reject C3. What
does reject C3 is ST3C-42 (nothing automated was yet operating) plus the C3 row's own finding that Fernley
was "leased only".

### ST3E-08 — Re-test of candidate C3 (1998-12-31) at full strength, on the good arguments rather than ST3_A's bad ones

**Claim tested:** that Stage 3 could close at the FY1998 audited cut — the only audited date in the window,
carrying 4.13× net sales, ~2,100 filed employees, $609,996k of sales against $60.2m of advertising, four
operating sites on two continents, two UK/German subsidiaries on EX-21.1, SIC 5961, the first *materially*
positive operating cash flow, a $326m note issue, authorised capital 100M→300M, rental expense up 4× in a
year, and two Wal-Mart divisional VPs hired.
**Strongest version of the case.** A board that meets eight times, an officer team recruited from the largest
physical retailer in the category, 2,100 people, and an audited statement that the company now houses
merchandising operations in four buildings in three countries, is not a promising startup. The
"intends to establish" sentence and the falling international share — the two arguments ST3_A actually
made — are both unsound (ST3E-05, ST3E-07), and ST3_A's own U.206 dissolves the officer-count argument
(ST3E-06). On the dossier's stated reasoning, C3 was not defeated.
**The document that defeats it, which ST3_A had but did not use.** "we have no previous experience with
automated distribution centers, as the two distribution centers in operation prior to 1999, in Washington
and Delaware, were manually operated" (10-Q Q3 1999 L1624-1635). This is the company, in an SEC filing,
describing the state of the operating network *before* 1999 as two manual plants. Against the Stage-3 test
— materially scalable operation, not headcount — a two-manual-site network is a distribution business, not
a scalable operating organisation, and 1998's cash shape is supplier float (ST3E-11).
**Also fatal to C3 as an "earliest" date:** the FY1998 10-K was filed 1999-03-05, i.e. after the Q1 1999
10-Q's subject period closed; the endpoint's own evidence base is not available at its own date.
**Verdict: C3 still FAILS, but the rejection must be re-grounded.** The auditor's version of this will be:
"the dossier rejected the strongest rival using a share-of-growth fallacy, a table-name count it had itself
retracted elsewhere, and a forward-looking sentence that appears in every filing in the window."

### ST3E-09 — Attack on the company's self-measurement, general form: which Stage-3 claims collapse if every self-report is set aside?

**Claim attacked:** the demand-side spine of Stage 3 — cumulative customer accounts, repeat-order share,
visit/reach percentages, Associates enrolment, "number one" rankings, "3rd largest bookseller", the $1bn
run rate, brand recognition, DC capacity, and the market size — nearly all of which ST3_A/ST3_C already
label as company counts.
**Test.** Set aside every assertion whose only carrier is the issuer or a third party quoted by the issuer,
and inventory what remains load-bearing.
**Preliminary finding (detailed in `## Attacks that landed` A-6):** what survives without any
company-as-witness sentence is a *financial and legal* spine — audited net sales, cost of sales, expense
lines, balance-sheet items and cash flows for FY1996-FY1998; the lease and merger instruments with their
dates and parties; the share counts in the S-3/S-4/S-8 accessions; the proxy compensation and
authorised-capital votes; the SC 13G blocks (holder-signed); the auditor's report and its dates; the two
lawsuits as pleaded by a defendant; and the SIC cover-page strings. What does **not** survive is *every*
customer-, seller-, order-, visit- or associate-level quantity, and therefore the entire demand side of the
marketplace story, and the entire "the model was validated by customers" reading.
**Key distinction this pass is graded on:** none of this is evidence the numbers are **false**. Each is
evidence that only the party with an interest ever said it, that no denominator or definition is published,
and that no counter-count exists because none was ever required. The two statuses are carried separately in
every record below.

### ST3E-10 … ST3E-30 — reserved, appended below as each source is read

*(Sections to be filled: the $1bn run-rate recomputation, the advertising-ratio recomputation, the
operating-cash-float recomputation, the acquisitions ledger, the silence classifications, the folklore
traces, and the register checks.)*
