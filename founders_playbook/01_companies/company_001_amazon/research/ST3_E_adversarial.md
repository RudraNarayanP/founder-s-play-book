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
(**99 directory entries**, of which 90 are `.txt` filings and artifacts: 4 × 10-K family including the
**FY1999 10-K and 10-K/A that arrived at 19:55, after every other Stage-3 dossier closed**, 8 × 10-Q,
25 × Form 8-K + 1 × 8-K/A, 2 × ARS, 2 × DEF 14A + 2 × PRE 14A, 13 × S-1 lineage, 6 × S-3, 4 × S-4 lineage,
9 × S-8, 3 × POS AM + 1 POS AMI, 2 × SC 13G, 1 × 8-A12G, 3 × 424B, plus the Stage-1/2 web artifacts, the
HistoryLink essay and the intake manifest). Every attack is run by reading the named line of the named file,
and every recomputation uses only figures printed in that corpus, with the arithmetic shown.
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
**Preliminary finding (worked through at ST3E-28):** what survives without any
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

### ST3E-11 — DISCOVERY THAT CHANGES THE EVIDENTIAL BASE: the FY1999 Form 10-K and its amendment are on disk and no Stage-3 dossier read them

**Claim attacked:** three load-bearing statements across Stage 3 —
- ST3_A C7: "UNTRIED as a candidate. It is the retrieval window's edge, not a finding; **the FY1999 annual
  report is one catalogue row plus one fetch away** and no boundary may rest on a document not read";
  ST3_A G-08: "FY1999 Form 10-K … **not fetched** … Cheapest high-value retrieval available to the project."
- ST3_C data gaps: "the FY1999 10-K is **not in `sources/`**"; "Whether any third-party shop/listing count
  existed for zShops … **the FY1999 10-K (2000) is the next document that might quantify it; outside the
  local corpus**."
- ST3_A G-11: "zShops / auctions seller counts, GMV, take rate — **Never disclosed in any filing in the
  set**."
**Finding.** Two documents are present in `sources/`:
`10-K_FY1999_acc-0000891020-00-000622_filed-2000-03-23.txt` (307,278 bytes) and
`10-K_A_FY1999_acc-0000891020-00-001638_filed-2000-09-08.txt` (173,340 bytes). Both carry a filesystem
timestamp of **19:55**, i.e. after ST3_A (19:49), ST3_C (19:47) and ST3_B (19:49) were last written. The
corpus is therefore **99 files, not 97** — and the "zero occurrences across 97 local files" negatives cited
by ST3_C (OC-1) and by my own brief were computed over a set that has since grown by two of the most
informative documents in the whole saga.
**What they settle or partly settle, on their face (all Tier 1, audited, same registrant lineage):**
Item 1's launch-date table and segment discussion, Note 14's segment data, the consolidated statements, and
the exhibit index (attacked
individually below). The consequences recorded in this file: ST3E-12 (marketplace scale now quantified),
ST3E-13 (seller-side counts exist), ST3E-14 (the launch-date table conflicts with the Q3 1999 10-Q),
ST3E-15/16 (the acquisitions ledger, priced), ST3E-17 (a fourth headcount date and a third basis),
ST3E-18 (three more executive offer letters, two dated September 1999), ST3E-19 (the FY1998 figures moved
again), ST3E-20 (international: which 20% is which).
**Verdict: LANDED, and it is the pass's most consequential finding.** Every Stage-3 "the record does not
show X" sentence must be re-run against 99 files before any Stage-3 text is signed. This is §14 rule 6's
point inverted: the gap was not un-retrievable, it was un-retrieved, and the dossiers wrote the *absence of
a document* as if it were a *limit of the record*.
**Status qualifier, because an auditor will use it the other way:** the FY1999 10-K is dated **2000-03-23**,
outside Stage 3's window, so it is not in-window knowledge and cannot itself move a boundary (method §2).
It is used here only as a **record of in-window facts** — the same standing Stage 2 gave to a later filing
that recites an earlier event — and every place it is used for that purpose says so.

### ST3E-12 — "Axis T is proved present but not material": the materiality answer exists, and it is not favourable to the boundary

**Test.** Whether the third-party/marketplace stream can be sized at all, and what its size implies.
**Finding.** FY1999 10-K Note 14 (L4182-4206) reports a third segment, **"Early-Stage Businesses and
Other"**, containing "electronics, software, video games, toys and home improvement" **plus** the "US
Marketplace Services … Amazon.com Auctions, zShops and sothebys.amazon.com": revenues **$163,804k**, gross
**loss $(7,801)k**, segment loss **$(242,148)k** for 1999; and Item 1 states "Amazon.com had no revenue from
this segment in previous years" (L375-377).
**Consequence for ST3_A.** (i) Axis T is *not* sizeable at 1999-06-30 from any window document — that
concession stands. (ii) But the first available measurement of the whole new-business aggregate, for the year
in which the recommended endpoint sits, is **10.0% of net sales at a negative gross margin and a segment loss
5.7× the FY1998 company-wide net loss**. A boundary whose transactional leg is "third-party commissions now
inside net sales" is, on the only audited quantification ever filed of that group, a **loss-making
adjunct**, not a scaled transaction business. (iii) The segment note also proves the *company* considered
these businesses separately reportable only from **1999** (first adoption of Statement of Financial
Standards No. 131) — i.e. its own internal management structure was not segment-divisible before that year.
**Verdict: LANDED.** Not as a refutation of the endpoint but as a demolition of the *weight* ST3_A's Axis T
carries in the "all three axes pass simultaneously" argument.

### ST3E-13 — "no seller-side count exists anywhere": one does, and it is dated Q4 1999

**Claim attacked:** ST3_C data gap — "Whether any third-party shop/listing count existed for zShops …
outside the local corpus"; ST3_A G-11 — "zShops / auctions seller counts … never disclosed."
**Finding.** FY1999 10-K L348-350: "During the fourth quarter of 1999, these marketplace services surpassed
a combined **1 million registered users and 1.5 million listings**."
**Verdict: LANDED as a null that was false, but the null is nearly as tight as it looks.** The count is
(i) "registered users", not sellers, still no GMV and no take rate; (ii) dated to a quarter, not a day;
(iii) *after* both candidate endpoints, so it cannot rescue the Q2 1999 Axis T leg; (iv) a company
self-report in its own Item 1. The correct Stage-3 statement is: "the only seller-side quantity in the
record is a combined registered-user and listing count for Q4 1999, undisclosed by service and unverified."

### ST3E-14 — the launch ledger: the FY1999 10-K dates zShops to **October 1999**, contradicting the Q3 1999 10-Q's "late September 1999"

**Claim attacked.** ST3A-54 (and ST3C-37/38, M-37): zShops "introduced" in "**late September 1999**", cited
as the strongest form of the marketplace's operating evidence at C5 (1999-09-30).
**Finding.** FY1999 10-K Item 1's launch table (L265-284) prints: `Auctions March 1999 · Electronics July
1999 · Toys July 1999 · zShops October 1999 · Home Improvement November 1999 · Software November 1999 ·
Video Games November 1999 · sothebys.amazon.com November 1999`, and internationally `UK and German Music
October 1999 · UK and German Auctions November 1999 · UK and German zShops November 1999`. The Q3 1999 10-Q
had said "In late September 1999, the Company introduced three e-commerce innovations: zShops…". Two
documents of one registrant differ by a month on the date of the marketplace proper, and the later, audited
annual document is the one that pushes it **outside** the 1999-09-30 quarter.
**Verdict: LANDED as a conflict, not as a resolution.** The dossiers must record the discrepancy; C5's
"decisive" marketplace leg loses a month it did not have. Note also that the same table is the *only*
document in the corpus that dates a launch list exhaustively — a Stage-3 asset neither dossier used.

### ST3E-15 — Attack on the acquisitions narrative, part 1: what the record actually supports about **what was bought**

**Claim attacked:** the folk list, and both dossiers' acquisition clusters.
**Test.** Grep every name against all 99 files, then read the audited acquisition note.
**Finding — evidenced, with dates and amounts:**
| Target | Instrument on record | Filed price as accounted | Consideration actually issued |
|---|---|---|---|
| Bookpages (UK), Telebook (DE, via ABC Bücherdienst), Internet Movie Database | 8-K acc. …000694 event 1998-04-17/24, Item 9 Reg S: "540,066 shares"; 10-Q Q2-1998 Note "Acquisitions" L478-492 | "aggregate purchase price of the three acquisitions, plus related charges, was approximately **$55 million**" (FY1999 10-K L3321-3326) | "common stock **and cash**"; "an aggregate of approximately **6.4 million shares**" (same) — post-split vintage of the S-3's resale registration |
| Junglee Corp. | 8-K acc. …001352/001210 (merger plan EX-2.1); S-3 333-65091 | purchase method, "**approximately $180 million**", substantially all to goodwill/intangibles, ~3-year life (FY1999 10-K L3330-3337) | ~1.6m shares at announcement (Q2-1998 10-Q L787-800) = ~9.4m post-split — "approximately **9.4 million shares** … and assumed all outstanding options and warrants" |
| PlanetAll (Sage Enterprises, Inc., MA) | 8-K acc. …001370; EX-2.2 | **pooling of interests — no purchase price at all** (FY1998 10-K; 8-K 1998-10-28 L278-288) | ~0.8m shares pre-split |
| Exchange.com (**e-Niche Incorporated**; operates Bibliofind, MusicFile), Accept.com (via ADC Acquisitions,
Inc.), Alexa Internet (via AI Acquisition, Inc.), LiveBid.com (agreed 1999-04-12) | four 8-Ks 1999-04-26 → 1999-06-11 + four S-8s within 24h of each closing; Q1-1999 10-Q Note 7 "approximately $645 million, mostly in … common stock" | Alexa alone: "**approximately $250 million purchase price**", "4,369,884 shares", "substantially all … allocated to goodwill and other purchased intangibles", amortised over "**lives averaging approximately three years**" (FY1999 10-K L3277-3287) | see ST3E-16 for the aggregate |
| **Tool Crib (home-improvement catalogue/online assets)** and **Back to Basics (toy catalogue retailer)** | **no 8-K in the corpus**; disclosed only in the FY1999 10-K: completed **1999-10-01** and **1999-11-08** | "approximately **$112 million aggregate purchase price**, of which approximately **$105 million** was allocated to goodwill and other purchased intangibles", ~4-year lives | "a total of **1,514,612 shares**" (L3289-3299) |
| "additional immaterial acquisitions during 1999" | none filed | "totaling **$44.1 million**" | "**200,370 shares**" (L3297-3300) |
| sothebys.amazon.com | FY1999 10-K L341-347, L284: launched **November 1999**; no 8-K; legal-entity form unclear in this corpus | UNKNOWN | UNKNOWN |
**Finding — not evidenced at all:** the strings "WarehouseDirect", "Warehouse Direct", "Internet Mail",
"IMail", "Allaire", "LiveBid" and "Exchange.com" were tested individually across the corpus; results and
classification are in `## Unsourced or folklore claims`; the Exchange.com entry is separately corrected
against the instruction layer at ST3E-31.

**Verdict: LANDED (expansion of the evidenced list, not contraction of the folk list).** Two of the folk
list's entries are in fact filed and priced; ~$156m of 1999 acquisitions appear in **no Stage-3 dossier at
all**; and the total of the *recorded* consideration is not the sum of the *announced* values (ST3E-16).

---

## Attacks that landed

Twenty-three attacks landed. Ordered by the damage they do to the Stage-3 story, not by the order found.

| # | Attack | Severity | What must change |
|---|---|---|---|
| ST3E-17 | The verb "opened" is used of a distribution centre in the **FY1997 10-K (1998-03-30)** and in the **ARS 1998**, and a DC is "leased and opened" in the **Q1 1999 10-Q (1999-05-17)**. Axis P's stated discriminator does not discriminate; applied literally it passes at the window's opening | **Critical** | Drop the verb test; re-ground Axis P on automation + number of sites in service (`## Boundary challenge`) |
| ST3E-31 | `MASTER_RESEARCH_LOG.md` states that `Exchange.com` returns **zero occurrences** across the corpus; it occurs **113 times in 11 files**, including an 8-K headline "AMAZON.COM ACQUIRES EXCHANGE.COM" that ST3_A itself quotes | **Critical — instruction layer** | Rewrite the log sentence; sweep any register that inherited "Exchange.com: absent" (OC-203) |
| ST3E-11 | The FY1999 10-K and 10-K/A are now on disk; every Stage-3 sentence of the form "the record does not show X" was written over 97 files and must be re-run over 99 | **Critical** | Re-run all negatives; this pass re-ran the twelve that carry weight |
| ST3E-32 | ST3_C OC-1 attributes the phantom "S-4s carry WarehouseDirect/Internet Mail" premise to `STAGE3_INTAKE_MANIFEST.md`, which contains none of those strings and has no such section | **High** | Re-address the correction to the agent briefs and the master log; do not edit the manifest (OC-204) |
| ST3E-21 | FY1998's +$31,035k operating cash flow sits **inside a printed audited subtotal of −$41,433k**; the subtotal is negative in 1996, 1997, 1998 and 1999; FY1999 operating cash flow is **−$90,875k**, inside Stage 3's nominal window | **High** | "First positive operating cash flow" is removed from validation.csv as a signal (OC-205) |
| ST3E-20 | Advertising's fall to 9.9% of net sales is a decomposition effect: **marketing and sales rose to 25.2% of net sales in 1999** because fulfilment inside it grew from 8.25% to 11.49% of sales; advertising is partly non-cash barter ($54.4m of securities received) and the caption's classification was under accounting-board review | **High** | No efficiency claim; report the three movements separately (OC-206) |
| ST3E-16 | Up to **$85.4m of the 1999 "acquisition price" is employment-contingent compensation**, per the audited note; announced stock-value headlines are not prices; audited 1999 share consideration was **$774.4m** against the announced ~$645m | **High** | Rewrite the acquisitions ledger and M-24 |
| ST3E-15 | Two ~$156m of 1999 acquisitions (Tool Crib, Back to Basics) and two further target companies (InnerLinx, Convergence) appear in the corpus and in **no Stage-3 dossier** | **High** | Add to timeline.csv / acquisition cluster |
| ST3E-25 | "The only filed post-IPO executive hiring package in the whole set" is false: **four offer letters** are listed, three dated **September 1999**, and the Galli letter's operative version is the **1999-09-30 amendment and restatement** | **High** | Axis M moves to Q3 1999 |
| ST3E-05/22 | "International share fell 33→25→20%" is a **share-of-growth fallacy** (international dollars grew 7.1× then 3.3×); but the *operating* international segment was only **$21.8m = 3.6% of FY1998 sales** with **$2.8m** of foreign fixed assets | **High (both ways)** | Replace the argument; keep the conclusion |
| ST3E-06 | The "8 names → 7 names" officer contraction is a disclosure artefact, and ST3_A's own U.206 says so | **Medium-High** | Remove from C1/C3/recommendation |
| ST3E-28 | Every demand-side quantity in Stage 3 is issuer-counted; what survives the set-aside is the financial, legal and capital spine | **Medium-High (framing)** | Section-level rewrites in `## What Stage 3 may not claim` |
| ST3E-24 | Headcount basis changed at each of the three filed dates; a third now exists (7,600 FT **and PT** at 1999-12-31) | **Medium** | Extend the series with an explicit basis label per row |
| ST3E-12 | The only audited quantification of the new businesses (Early-Stage Businesses and Other, FY1999): revenue $163.8m, **gross loss $7.8m, segment loss $242.1m** | **Medium** | Axis T's weight reduced to nil for materiality |
| ST3E-35 | The 10-K/A restated cash equivalents for **all periods**; FY1998's "change in cash" flips from **+23,685 to −38,536** | **Medium** | Basis-label every cash row inherited from Stage 2 |
| ST3E-13/14/19 | Three "no such figure exists" nulls were false (music $33.1m Q4-1998; video opened **1998-11-17**; 1m marketplace users / 1.5m listings) and one date moved (zShops October vs late September) | **Medium** | Patch gaps, timeline, and the launch ledger |
| ST3E-18 | The "$1 billion run rate" **does** have its basis stated in the corpus ("Based on fourth quarter sales"), contrary to the note carried into Stage 3 | **Medium (provenance, favourable)** | Correct the note; label as peak-quarter annualisation |
| ST3E-26 | "InnerLint" is **InnerLinx Technologies**; the string in ST3_A occurs nowhere | **Low-Medium** | Name fix |
| ST3E-27 | FY1998 net sales printed $609,996 and $609,819; FY1997 gross profit $28,813/$28,818 | **Low-Medium** | Vintage conflict, print both |
| ST3E-01/02/03/04 | The three boundary legs, individually: priority wrong, weight wrong, single-document | **High as a set** | See `## Boundary challenge` |
| ST3E-29 | Four silences classified (convention / convention+null / convention+mild pull / convention) | **Framing** | Never let a null become a conclusion |
| ST3E-37 | Hindsight contamination in the *choice of axes*, not in the prose | **§2 finding** | State the selection in §A/§S |

## Attacks that failed (and the evidence that held)

**ST3E-F1 — "The personal guarantees vanished, so they were probably released, or hidden."** Failed. I
re-ran the search independently: "Seafirst" post-1997-05-15 occurs once, in a lease's late-rent interest
benchmark (10-Q Q1 1998 L14378); "Wells Fargo" occurs nowhere after the 1997 registration lineage; the
proxies' "Certain Transactions" carry only the Cook/Stonesifer Series A purchases and the Dalzell relocation
loan (repaid 1998-10-23). The guarantees, their dates and the **Subrogation Agreement dated 1996-06-19**
(S-1 orig. EX-10.27) sit entirely in the pre-IPO lineage. **What held** is the *documented null*; and it is
stronger than ST3_B recorded in one respect — the S-1 dates each guarantee separately, so the Seafirst
guarantee had already run from November 1994 **to December 1996**. Status remains UNKNOWN-with-searches-
recorded. An attack that would have converted the silence into a finding is the one this pass most expected
to land, and the record refused it.

**ST3E-F2 — "The FY1998 close should be restored as the endpoint."** Failed as a reversal, though three of
ST3_A's four reasons for rejecting it failed first (ST3E-05, 06, 07). The candidate is defeated on evidence
ST3_A did not deploy: the company's own statement that both pre-1999 distribution centres were **manually
operated** and that it "ha[d] no previous experience with automated distribution centers"; the International
segment at **3.6% of FY1998 net sales**; a filed operating network of four buildings of which the largest was
200,000 sq ft; an officer body still headed by one man holding three offices, with **no COO, no separate
finance chief, and a board that did not change size**; and the negative pre-working-capital cash subtotal
(ST3E-21). **Held.**

**ST3E-F3 — "The advertising figures are not real (they are marketing dressed up)."** Failed. The note is a
discrete audited disclosure in three consecutive annual reports — "$3.4 million, $21.2 million and $60.2
million" and, in the FY1999 10-K, "$140.9 million, $60.2 million and $21.2 million" — and the two vintages
**agree** on the overlapping years. What survived is the *interpretation* attack (ST3E-20), not the number.

**ST3E-F4 — "Bookpages/Telebook/IMDB are folklore retellings that the filings never dated."** Failed hard.
The dates are in a **filed 8-K under Item 9 (Regulation S)** with the share figure (540,066), and the
settlement dates appear in a second instrument (S-3 333-65091) reciting the Telebook merger of 1998-04-24.
The retrospectives are the *worse* carriers here, not the only ones.

**ST3E-F5 — "ST3_C's quotations are paraphrases."** Failed. I re-read a sample against the named lines
(FY1998 10-K L339, L346-348, L386, L420-424, L803-805, L1085, L1324-1326; 10-Q Q1 1999 L592, L636-637,
L1810-1813; 10-Q Q2 1999 L822-824, L852-854; 10-Q Q3 1999 L801-806, L830-833, L1624-1635; ARS 1997 L229-231;
ARS 1998 L106, L137-140, L157-160; 8-K 1999-01-26 L192-195, L226-236). Each string located at or within one
line of the citation, including the odd hyphenation and mid-sentence breaks the dossier flags in advance.
That is unusually good discipline and this review records it as such.

**ST3E-F6 — "The Q2 1999 10-Q's auctions-revenue sentence proves third-party scale."** Attacked from the
other direction — that it is *evidence the marketplace was working* — and failed as stated: it proves
recognition, not volume (ST3E-02, ST3E-34).

**ST3E-F7 — "Stage 3 used the S-4s as corroboration of acquisitions."** Failed: both dossiers had already
caught it (ST3A-47, ST3C-20/21). No new damage available; the *attribution* of the error, however, is wrong
(ST3E-32).

**ST3E-F8 — "The 6.2 million / 16.9 million account series is contradicted somewhere."** Failed. Nothing on
disk contradicts it; it is cumulative, self-defined and unchanged in definition except at the "inclusive of
Auctions" point. The attack yields a provenance downgrade (ST3E-28), not a conflict.

**ST3E-F9 — "The dossiers' negative claims are unreliable because they searched a stale corpus."** Failed on
test. The load-bearing negatives were re-run over **99** files here and held as re-verified absences:
`gross merchandise`/GMV (0 hits), any Associates commission rate or expense (0), and the marketplace-contract
readings. The corpus growth changes one thing — the two FY1999 documents — and ST3E-11/13/14/15/19/23/24/25/26
are precisely the places where a "the record does not show X" sentence met a document that shows it. Every
other null is now safer than before, because it has been searched twice.

**ST3E-F10 — Stage 2's retractions are not re-litigated, and none is restored here.** The `$871,000` /
`$976,408` leg, the `2,613,000` share base, the wrongly-attributed founding town and the auditor's own
fabricated number were withdrawn in earlier passes; nothing in Stage 3's documents, including the
two new FY1999 filings, re-imports them.

## Unsourced or folklore claims

Classification per method §3 and §5. **FOLK** = circulates without a carrier in this corpus. **AGREED-ONLY**
= the window's documents record agreement, not closing. **SELF-REPORT** = carried only by the party with an
interest. **CONTRADICTED** = a document on disk says otherwise. **PROJECT-ERROR** = an assertion made by this
project's own files.

| Claim | First dated appearance (in this corpus) | Class | Verdict |
|---|---|---|---|
| "Amazon's first acquisitions were WarehouseDirect and Internet Mail (internet.com)" | **none** — 0 occurrences in 99 files | FOLK, and the S-4 attribution is **CONTRADICTED** (333-55943 names no target; 333-56723 is a notes exchange) | Not usable in Stage 3 as an Amazon acquisition fact. External primary trace required; **UNTRIED** |
| "Allaire was an Amazon acquisition" | **none** — 0 occurrences | FOLK | Same. (Allaire appears in period accounts as an *investment*, not an acquisition — nothing here supports either form) |
| "The five 1999-03-11 Sales Agreements are the marketplace's merchant contracts" | `_EVIDENCE_CACHE.md` L467 (cache row, now struck); **two agent briefs** | **PROJECT-ERROR**, disproved by the exhibit bodies | Corrected; the cache records the correction |
| "The intake manifest carried the phantom S-4 premise" | `ST3_C` OC-1 attributes it to `STAGE3_INTAKE_MANIFEST.md` | **PROJECT-ERROR (a correction aimed at the wrong file)** | ST3E-32 / OC-204 |
| "`Exchange.com` returns zero occurrences" | `MASTER_RESEARCH_LOG.md` L823 | **PROJECT-ERROR**, disproved by 11 files / 113 hits | ST3E-31 / OC-203 |
| "InnerLint" (as a target) | `ST3_A` ST3A-50 | **PROJECT-ERROR** (transcription): the plan is "INNERLINX TECHNOLOGIES STOCK OPTION PLAN" | ST3E-26 |
| "Headcount is filed at exactly two dates" | `ST3_A` ST3A-18 | true of the form families it searched; **stale** at the corpus | ST3E-24 |
| "The Q2 1999 10-Q is the first filing in the corpus that uses 'opened'" | `ST3_A` C4 | **CONTRADICTED** three ways | ST3E-17 |
| "zShops launched late September 1999" | 10-Q Q3 1999 L801 (1999-11-15) vs FY1999 10-K launch table "October 1999" | FACT-of-disclosure, **CONFLICTED** | ST3E-14; keep both, cite both |
| "Amazon became the number one online music seller / video seller / 3rd largest US bookseller / No. 1 in the UK and Germany" | 10-Q Q3 1998; FY1998 10-K L345-350; 8-K 1998-04-27; 8-K 1999-01-26 | SELF-REPORT, ranking source never named | Class as company assertion; never as market fact |
| "Word of mouth remains the most powerful customer acquisition tool we have" | ARS 1997 L197-200 (1998-04-17) | FOUNDER/COMPANY CLAIM, contemporaneous; **no measurement exists anywhere** | ST3_C already refuses the virality reading; keep refusing it |
| "$1 billion revenue run rate" | 8-K 1999-01-26 L192-195 **with** basis; ARS 1998 L106 **without** | ESTIMATE/DERIVED on a stated basis (Q4 × 4) | ST3E-18; label the seasonality |
| "Nearly quadrupled" (UK+Germany) | 8-K 1999-01-26 L226-228; ARS 1998 L137-140 | SELF-REPORT, no absolute value, quarter-over-quarter for stores open ~1 quarter | Object corrected: not "international sales" |
| "8 million pre-registered, experienced online buyers" | 8-K 1999-03-30 headline | SELF-REPORT; the same number measures the service being sold | ST3E-28 |
| "Media Metrix: 90th → top 20"; "≈16% of Web users"; "117.8m adults / 60% brand recognition"; "Forrester $43bn → $1.3tn" | ARS 1997 L213; FY1998 10-K L223-228; 8-K 1999-10-28 L248-251 | Third-party **quoted by the issuer**; underlying reports absent from the corpus | Tier 2/3 at best; **one source quoted once** |
| "The Associates program drove growth" | 4,800+ (Stage 2) → >140,000 (8-K 1998-10-28) → ~200,000 (FY1998 10-K) → 430,000 (FY1999 10-K, at **2000-02-29**) | SELF-REPORT enrolment; economics unmeasured at every date | Enrolment curve only; no causal claim |
| "Amazon had no merchant/bank agreements on file" | verified across 99 exhibit indices | documented null; **disclosure convention**, not absence of arrangements | ST3E-29(iv) |
| "GeoCities was acquired" | name appears in a press-release list only (8-K 1998-08-03) | NAME-ON-A-LIST | Not an acquisition claim |
| HistoryLink essay items ("E-Toys", "B&N $2 billion in 1996", "ABA lost 1,200 stores 1991-97", "official launch 16 July 1995", "$12,000 of orders in the first two days") | `historylink-essay-23230…txt`, posted **2025-04-07** | RETROSPECTIVE, Tier 2→4, its own sources are Brad Stone (2013) and Brandt (2011) | Excluded from every Stage-3 table; ST3_C's use-note already says so |
| "1-Click launched on <date>" | no carrier in the corpus at any date | **UNANSWERED** | ST3E-33(3) |

## Single-lineage claims

Per method §3, each of these is **one source** however many accessions repeat it. They are not refuted here —
they are capped. Any Stage-3 row marked "Corroboration: High (multiple filings)" on one of these lines is
mis-scored.

| Claim | Printings | Lineage | Independence that exists |
|---|---|---|---|
| Net sales / cost of sales / expenses / cash flows FY1996-FY1998 | 10-K405 FY1997, 10-K FY1998, 10-K FY1999, 10-K/A FY1999, S-3 1999-03-16, 8-K releases | one registrant, four+ accessions | **the auditor's report** (Ernst & Young, dated 1999-01-22 / 2000-03-[x]) — a genuinely separate signatory, though appointed by the company |
| "614 full-time" / "approximately 2,100" / "approximately 7,600 FT and PT" | one 10-K each | one lineage each; **three bases** | none |
| Cumulative accounts 1.5m → 6.2m → 8.4m → 10.7m → 13.1m → 16.9m | 10-Ks, 10-Qs, ARSs, 8-Ks | one registrant | none |
| Repeat-order percentages | 8 carriers, ≥4 bases | one registrant | none |
| Music $14.4m (Q3 1998) and $33.1m (Q4 1998) | one 8-K each | one registrant, unaudited | none — and never repeated in an annual report |
| Associates 140,000 / 200,000 / 430,000 | 8-K, 10-K, 10-K | one registrant | none |
| The Q2 1999 "opened a new distribution center in Nevada" + Galli appointment | 10-Q Q2 1999; restated in 10-Q Q3 1999 | **one corporate record, two accessions** — ST3_A already labels this correctly at ST3A-59 and should be credited for it | none |
| The $1.25bn convert | 8-K 1999-02-03 + EX-4.1/4.2 in the same accession; recited in Q3 1999 10-Q | one transaction, one lineage | the indenture's counterparty (Bank of New York as trustee) appears in the instrument |
| The five Buschman Sales Agreements | five exhibits, one standard form, five incorporated proposals | **one instrument family** | none |
| S-4 333-55943 shelf growth 5m → 15m → 30m | original + S-4/A + POS AM ×2 + POS AMI | **one registration statement** — capability evidence, and ST3_A says so | none |
| Bookpages/Telebook/IMDB dates | 8-K 1998-05-01 Item 9; S-3 333-65091; Q2 1998 10-Q note; FY1998 10-K | one registrant, four accessions | **the acquired entities' own existence** as separate legal persons (Bookpages Limited, England; Telebook, Inc., Florida; ABC Bücherdienst) is third-party-verifiable in principle, and not in this corpus |
| Founder stake 9,885,000 = 41.3% | SC 13G 1998-02-17 | **the holder's own filing under his own signature** — a different duty from the registrant's, still self-report | partially independent: a Schedule 13G is signed by the *holder*, and a false statement there is actionable against the holder, not the issuer |
| Wal-Mart / Intimate Bookshop litigation | FY1998 10-K Item 3, 10-Q Q2 1998 | reported **by a defendant** | a court record would be independent; **none is in the corpus** — UNTRIED (PACER/CLERK route never attempted) |
| Competitor rosters (CDnow, N2K, eBay, Yahoo! Auctions, Columbia House, barnesandnoble.com) | 424B3, 10-Qs, FY1998 10-K | one registrant's selection of whom to name as rivals | a competitor's own filing would be independent; **no competitor filing is on disk** |
| Segment note FY1999 | one 10-K | one lineage, audited as part of the statements | the auditor |

**The single most important lineage point for Stage 3's conclusion.** There is **no independent witness
anywhere in the corpus to a *quantity*.** Independence in this archive exists only for *events, instruments
and signatures* — a merger plan, a lease, an indenture, a proxy vote, an auditor's date, a holder's 13G. That
is the structural reason Stage 3 can prove that the company *did* things and cannot prove that they *worked*.

---

## Attack ledger, continued (ST3E-16 … ST3E-37)

*(The summary sections above were appended mid-pass and split this ledger in two. Record numbers continue;
nothing is renumbered. Every record in both halves is cross-referenced from `## Attacks that landed`.)*

### ST3E-16 — Attack on "for how much": the announced headline is not the purchase price, and up to $85.4m of the 1999 price is salary

**Test.** Compare every announced consideration figure used by the dossiers against the audited
consideration in the FY1999 10-K's statements of cash flows and Note.
**Arithmetic (all inputs filed; DERIVED where noted).**
- Supplemental cash-flow disclosure, FY1999 10-K L2875: "**Stock issued in connection with business
  acquisitions … $774,409 (1999) / $217,241 (1998) / $-- (1997)**" ($ thousands).
- Against that: Q1-1999 10-Q Note 7 announced the four then-contemplated deals at "approximately **$645
  million**, mostly in … common stock" (ST3C-27). The audited 1999 stock consideration is **$129.4m higher**
  than the announced four-deal figure (DERIVED: 774,409 − 645,000 = 129,409), because it also carries Tool
  Crib, Back to Basics and the $44.1m of "immaterial" deals. The announced figure is therefore *not* the
  year's acquisition cost and must not be re-used as one.
- FY1998: announced Junglee+PlanetAll "aggregate value of approximately **$280 million**" (Q2-1998 10-Q
  L787-800) against audited "**$217,241**" of stock issued in 1998 and a recorded Junglee purchase price of
  "approximately **$180 million**", with PlanetAll **pooled** — i.e. carrying no purchase price at all.
  The $280m is an announcement-date market-value-of-stock statement at an undisclosed reference price, and
  ST3_C already says so (ST3C-36 conflict note); what must be added is that **no component of the $280m is
  an accounting price**, because the two deals were accounted for by two different methods.
- **The decisive new fact:** FY1999 10-K L3307-3319: "In connection with certain acquisitions, the Company
  has conditioned a portion of the overall consideration on the **continued tenure of key employees**. Under
  generally accepted accounting principles, a portion of this amount is accounted for as **compensation
  rather than as a component of purchase price** … a maximum of **$85.4 million** in additional
  consideration relating to the Company's acquisitions for 1999 may be recorded as **compensation expense**
  … Amounts will be 'earned' based on tenure of certain employees and will be recognized as expense over a
  period of **12-36 months**."
**Reading.** Up to **$85.4m of what Stage 3 will call 1999's acquisition price is retention pay**, and
Amazon said so in its audited note. No Stage-3 dossier carries this sentence; the ~$645m figure circulates
in ST3_C §Metrics M-24 as "the 1998/1999 'values' are stock-price-weighted, not cash" — which is *weaker*
than the truth.
**Verdict: LANDED.**
*(ST3E-17 … ST3E-27 follow in sequence. The interim marker that stood here during drafting is retired; it
carried no evidence, and the record numbers were never reused.)*

### ST3E-17 — THE DECISIVE BOUNDARY ATTACK: the verb "opened" is in the FY1997 annual report, so Axis P's stated discriminator does not discriminate

**Claim attacked.** ST3_A, candidate C4, Axis P: PASS because this is "**the first filing in the whole corpus
that uses 'opened'**", and again in the recommendation: "Stage 2's rule — the filing's own words govern —
points at 1999-06-30, where the **verb changes to 'opened'**".
**Finding — three earlier occurrences, all in the local corpus, all Tier 1:**
1. **FY1997 Form 10-K, filed 1998-03-30, MD&A L1647-1649:** "In November 1997 the Company **opened** a
   200,000-square-foot distribution center in Delaware and expanded its Seattle distribution center to
   85,000 square feet." — an *annual report*, on an audited document family, using the past tense of
   opening a distribution centre, for a facility **twice the size of the whole Seattle warehouse estate**.
2. **ARS 1998, filed 1999-04-07, L160:** "We **opened** distribution and customer service centers in the
   U.K. and Germany, and in early 1999, announced the lease of a highly-mechanized distribution center of
   approximately 323,000 square feet in Fernley, Nevada." — the company's signed shareholder letter uses
   "opened" for two *foreign* DCs and, in the same sentence, keeps Fernley in the *announced-lease* column.
   The distinction ST3_A credits to the Q2 1999 10-Q is drawn identically, and eleven weeks earlier, in the
   ARS.
3. **10-Q Q1 1999, filed 1999-05-17, L592 and L915:** "A new distribution center was leased and **opened** in
   Nevada during the quarter" / "During the first quarter, the Company leased and opened a distribution
   center in …"
**Consequence.** Applied as written, the test places Axis P's first pass at **1997-12-31** — the date of the
Duenas-era, two-site, single-category company ST3_A marks "FAILS" at C1. A criterion that passes at the
window's opening and again at its middle is not a criterion. The dossier must either abandon the verb test
or re-ground it, and the re-grounding is available in its own material: **automation and number of sites in
service**, not the word "opened".
**Verdict: LANDED — the strongest single finding of this pass.** Confidence High; strings quoted verbatim
from the cited files.

### ST3E-18 — Attack on the "nearly quadrupled" / "$1 billion run rate" pair: one is under-read by Stage 3, the other is mis-recorded as unlabelled

**Claim attacked.** ST3A-14: the ARS 1998 is "the filed source for '6.2 million' cumulative customers and
the **'$1 billion revenue run rate' self-description**", and the brief's framing "the $1bn run rate on an
**unstated basis**". Also ST3A-30/ST3E-05's handling of "nearly quadrupled".
**Finding (a) — the basis IS stated, in the carrier that precedes the ARS.** 8-K event 1999-01-26, EX-99,
filed 1999-01-27, L192-195: "Net sales for the fourth quarter were **$252.9 million**, an increase of 283
percent over net sales of $66.0 million for the fourth quarter of 1997. **Based on fourth quarter sales**,
Amazon.com has achieved a $1 billion annualized sales level three and one-half years after opening for
business." Recomputation (DERIVED): 252.9 × 4 = **$1,011.6m**, consistent with "$1 billion".
So the claim is arithmetic on a filed quarterly figure, and the basis — the fourth quarter, annualised — is
printed. The ARS sentence ("exited 1998 with a $1 billion revenue run rate") is the *unsourced-in-context*
version of a *sourced* release. Stage 3 must not record it as an unstated-basis boast.
**Finding (b) — what the basis makes it worth.** Fourth quarter is the company's own declared seasonal peak:
FY1999 10-K L598-601 (Item 1 "SEASONALITY"), repeated in MD&A at L840-843, "Internet usage generally declines during the summer. Sales in the traditional
retail book, music, DVD/video, toy, electronics and home improvement industries usually increase
significantly in the fourth calendar quarter". Annualising the peak quarter is a *maximal* basis. The same
corpus supplies the check: Q1 1999 net sales $293,643k (10-Q Q2 1999 six-month $608,019k − Q2 $314,377k),
Q2 1999 $314,377k — both *above* the annualised $252.9m, so the run rate understated the following two
quarters. **The arithmetic is therefore not "false" in either direction; it is a seasonal-quarter
annualisation whose sign happened to be conservative.** Class: ESTIMATE/DERIVED with a stated basis, not
founder boasting.
**Finding (c) — "nearly quadrupled".** The string's carrier is the same release, L226-228: "**Combined sales
in the U.K. and Germany** nearly quadrupled **over the third quarter**", repeated at ARS 1998 L137-140 with
the comparator attached, and explained at L288: "Customer response to the launches drove a near-quadrupling
of combined sales…". It is (i) a Q3→Q4 1998 sequential change in two stores that opened in October 1998, so
"the third quarter" contains almost none of them; (ii) a *combined* figure with no absolute value; (iii) not
an international-sales statement at all. Where the brief describes "nearly quadrupled international" as a
company count, the correct object is "UK + Germany store sales, one quarter over the preceding quarter".
**One external check exists and it is consistent, which is not the same as corroboration:** the FY1999 10-K's
segment note puts the whole International segment at **$21,806k for FY1998** (L4200). A Q4 figure roughly
four times Q3 for two stores opened in October fits inside $21.8m for the year. Order-of-magnitude
consistency from a later audited document; no independent count.
**Verdict: LANDED on the record-keeping (both figures are mis-described in Stage 3), FAILED as a refutation
of either figure.** Status for both: **only ever asserted by the party with an interest — but arithmetically
checkable, and not contradicted by anything filed.**

### ST3E-19 — "the only category number in the record": there are at least two, and one launch has a day

**Claim attacked.** ST3_C data gaps: "the company reported one consolidated net-sales line and **only ever
gave one category number (music, $14.4m, in a press release)**"; and "Day-level dating of every 1998-99
category launch … **filings give months; releases give the Seattle dateline only**".
**Finding.** Same 8-K of 1999-01-26, L230-236: "Music sales grew to **$33.1 million**, a 130 percent increase
over sales of $14.4 million in the third quarter of 1998"; and "Video sales were strong following the store's
**opening on November 17**." The video store's launch day — 1998-11-17 — is the only category-launch day in
the corpus, and it is in a document ST3_C lists as read (the 1998-10-28 release is cited; the 1999-01-26
release appears in ST3_A's record set but its EX-99 body was not mined for these strings).
**Verdict: LANDED.** Two corrections to ST3_C's gap table, and one new dated fact for the timeline register.

### ST3E-20 — Attack on the growth arithmetic: advertising's falling share of sales is a decomposition effect inside a line whose other component grew faster

**Claim attacked.** The framing (brief; and ST3_B §U2(c) "marketing efficiency … each dollar of advertising
was attached to more than twice the revenue in 1998 that it was two years earlier") that advertising falling
from 21.6% to 9.9% of net sales while rising 18× in dollars evidences efficiency.
**Recomputation, all inputs filed.**
- Advertising expense (notes): FY1996 **$3.4m**, FY1997 **$21.2m**, FY1998 **$60.2m** (FY1997 10-K L2188;
  FY1998 10-K L2459-2461 — re-verified here), FY1999 **$140.9m** (FY1999 10-K L3107-3109).
- Net sales as restated in the FY1999 10-K: **$147,787 / $609,819 / $1,639,839** (L2610).
- Advertising ÷ net sales: 1997 **14.3%**, 1998 **9.87%**, 1999 **8.60%**. Absolute growth 1996→1999:
  140.9 ÷ 3.4 = **41.4×**; 1998→1999: **2.34×**.
- Fulfilment costs **inside the same "marketing and sales" caption** (FY1999 10-K L1969-1972): **$12.1m
  (1997) → $50.3m (1998) → $188.4m (1999)** = 15.6× in two years, against net sales 11.1×.
  Fulfilment ÷ net sales: 8.19% → 8.25% → **11.49%**.
- Marketing and sales ÷ net sales as printed by the company: **27.1% (1997) → 21.8% (1998) → 25.2% (1999)**
  (FY1999 10-K L1960), i.e. **the composite line rose 3.4 points in the same year advertising's share fell
  1.3 points.**
**Reading.** The advertising ratio fell because the *denominator* was being pulled up by the first-party
merchandise base, while the money the company actually spent to serve each customer moved from advertising
into fulfilment. The company's own MD&A says precisely this: "Marketing and sales expenses increased as a
percentage of net sales in 1999 … primarily due to increases in fulfillment expenses associated with our
expansion of our distribution center network and customer service staff" (L1980-1984), and its forward
sentence — "we expect that fulfillment costs will decline as a percentage of sales in the future" — is a
**declaration of an efficiency that had not yet occurred**.
**Two further contaminants.** (i) FY1999 supplemental cash flow prints "**Equity securities of other
companies received for non-cash revenue for advertising and promotional services … $54,402**" (L2884-2885)
and accrued advertising moved **+$42,382 (1999)** vs +$9,617 (1998) — advertising in this period is partly a
barter and accrual object, not a cash-media object. (ii) The FY1999 note warns that accounting-standard
setters were then reviewing "the financial statement classification of … **fulfillment and order processing
costs**" by e-commerce companies "including Amazon.com" (L1993-2000) — i.e. the line whose ratio is being
praised was, on the company's own statement, about to be re-cut.
**Verdict: LANDED.** "Advertising efficiency" may not be stated as a scaling signal. What the filings support
is: *advertising per dollar of sales fell; cost to serve per dollar of sales rose; the line containing both
rose in 1999.* Confidence High (every input printed, arithmetic shown).

### ST3E-21 — Attack on "first positive operating cash flow": the audited statement prints the pre-working-capital subtotal, and it is negative in every year of the window

**Claim attacked.** ST3A-35: "FY1997 is already positive at $687k, so 'first year of positive operating cash
flow' is FY1997, not FY1998; FY1998's $31,035k is the year it becomes material" — and the briefer's
proposition that +$31.0M inside +$78.7M of payables may not be a validation signal.
**Finding — this is not an inference; it is a printed line, in the FY1999 10-K.** L2829-2845:
"Net cash **used** in operating activities before changes in operating assets and liabilities …
**(320,987) / (41,433) / (26,160)**" for 1999 / 1998 / 1997, and changes in operating assets and liabilities
"**+230,112 / +72,468 / +26,847**", giving "(90,875) / +31,035 / +687".
Cross-foot against the FY1998 10-K's own statement (L2226-2247, re-read here): net loss (124,546) +
depreciation and amortisation 9,692 + deferred-compensation amortisation 2,386 + non-cash merger/acquisition
costs 47,065 + non-cash interest 23,970 = **(41,433)** ✓; plus inventories (20,513), prepaid (16,465),
deposits (293), accounts payable **+78,674**, accrued advertising **+9,617**, other liabilities and accrued
expenses **+21,448** = **+72,468** ✓; total **+31,035** ✓. The three supplier/customer-float lines alone sum
to **+109,739**, i.e. **3.5× the reported positive operating cash flow.**
**Days-payable check, because "the float did the work" needs a rate, not just a level.** Accounts payable
balances (FY1998 10-K L1971; FY1999 10-K L2561): **$33,027 (1997) → $113,273 (1998) → $463,026 (1999)**.
Cost of sales (FY1999 10-K income statement L2608): **118,969 / 476,155 / 1,349,194**.
DERIVED DPO = AP ÷ COGS × 365: 1997 = 33,027/118,969 × 365 = **101.3 days**; 1998 = 113,273/476,155 × 365 =
**86.8 days**; 1999 = 463,026/1,349,194 × 365 = **125.2 days**.
**Honest reading of the two directions.** The float that turned FY1998 positive is real and decisive — trading
cash generation was **negative $41.4m**. But the *terms* did **not** stretch in 1998: days payable **fell**
by ~15 days, so the incremental $78.7m was purchased by growth in purchases, not by leaning on vendors —
which is a weaker version of "supplier float is doing the work" and a *stronger* version of "this is
scale-dependent working-capital behaviour". The stretch arrives in **1999** (+38 days, and
$463m of payables against a $719.97m net loss), and in 1999 operating cash flow is **negative $90.9m**.
**Verdict: LANDED.** "First positive operating cash flow" may not be carried as a Stage-3 validation signal
at any date: (i) it is FY1997's, not FY1998's, on the level; (ii) the audited pre-working-capital subtotal is
negative in 1996, 1997, 1998 and 1999; (iii) it reverses inside Stage 3's own nominal window. Class:
INFERENCE rebutted by a printed FACT. Confidence High.

### ST3E-22 — Attack on "international share fell, therefore the geographic-expansion candidate fails": the two 20%s are different objects, and the smaller one is the one that matters

**Test.** Find any filed quantity that isolates the overseas *operations* from export sales.
**Finding.** FY1999 10-K Note 14 gives the *customer-location* measure and the *segment* measure side by
side: "Sales to customers outside of the US represented approximately **22%, 20% and 25%** of net sales for
the years ended December 31, 1999, 1998 and 1997" (immediately after the segment tables), **and** segment
revenues: International segment **$167,743k in 1999 (L4189) and $21,806k in 1998 (L4200)**, with "no revenue for this
segment in 1997". DERIVED: the International segment is **3.6% of FY1998 net sales** (21,806 ÷ 609,819) and
**10.2% of FY1999** (167,743 ÷ 1,639,839); segment loss $(25,498)k in 1998 and $(79,223)k in 1999. Long-lived
assets held in foreign countries: **$2.8m (1998) → $9.4m (1999)**.
**Reading.** Two independent corrections, one either side of the argument:
(i) **ST3_A's "decisive" argument is unsound** (ST3E-05): a falling *share* is not a falling business.
(ii) **But C3's failure on the international leg is stronger than ST3_A knew**: the actual overseas
operating organisation at the FY1998 close was 3.6% of revenue and $2.8m of foreign fixed assets — the
20% figure it was arguing about is overwhelmingly **US export sales**, which is a shipping fact, not an
organisation. ST3_A attacked the wrong number and got the right verdict by accident.
**Verdict: LANDED as an argument swap** (record both; the conclusion at C3 is unaffected and better
supported).

### ST3E-23 — Attack on the Associates programme: the enrolment series is real, the economics are absent, and the only *new* count is outside the window

**Claim attacked.** Stage 3's treatment of 140,000 → ~200,000 enrolments as a demand-side signal.
**Test.** Search every document, including the two new ones, for any rate, expense or attributable revenue.
**Finding.** FY1999 10-K L542-545 is the only additional statement: "We extend our market presence through our
**Associates Program**, which enables associated Web sites to make products available to their audiences
with **order fulfillment by Amazon.com**. As of **February 29, 2000**, approximately **430,000** Web sites
have enrolled in the Associates Program." That is (i) a *post-window* measurement date, in a filing for
FY1999 — the annual report gives no Associates number at its own 1999-12-31 date; (ii) still a count of
*enrolments*, not of sites that sent an order; (iii) still no commission rate, no commission expense, no
attributable revenue or order share. The FY1999 10-K's expense captions show no line into which an
Associates fee could be seen (they are marketing and sales, technology and content, G&A, stock-based
compensation, amortisation of goodwill, merger-related costs).
**Classification of the silence.** Not evidence of absence, not evidence of size: it is a **disclosure
convention** — a fee programme whose expense was not separately material to a company of that size need not
be broken out under Item 601(b)(10)/Rule 3-01 materiality practice — compounded by the method §2
record-selection null, since the counterparty side (portal economics) was never Amazon's to file.
**Verdict: HELD as a fact and DOWNGRADED as a signal.** Stage 3 may print the enrolment series labelled
"self-reported enrolments, yield unmeasured"; it may not use any of it as validation.

### ST3E-24 — Attack on the headcount spine: a third filed date now exists and the basis changed at every one of them

**Claim attacked.** ST3A-18 (recorded as a documented null): "**no 10-Q, 8-K, ARS or proxy** [states a
headcount] … Filed headcount therefore exists at **exactly two dates** inside Stage 3."
**Finding.** True as to form family — and now incomplete as to the corpus. FY1999 10-K Item 1 EMPLOYEES,
L684-686: "As of **December 31, 1999**, the Company employed approximately **7,600 full-time and part-time
employees**. The Company also employs independent contractors and temporary personnel." So the *filed*
headcount series inside the Stage-3 span is 1997-12-31 = **614 full-time**; 1998-12-31 = **approximately
2,100 employees** (no basis qualifier); 1999-12-31 = **approximately 7,600 full-time and part-time** — three
dates, **three different measurement bases**, the widest of them last. ST3A-17's own warning ("not a
like-for-like measurement") applies squared across the third point: 2,100 → 7,600 is 3.6× on a basis that
has been *widened* to name part-timers explicitly.
**Verdict: LANDED** as an incompleteness, and it strengthens rather than weakens the scale story — which is
exactly why it must be reported: 614 → ~7,600 across the window, with the intermediate steps not comparable
to each other and no third-party count anywhere behind any of them.

### ST3E-25 — Attack on "the only filed post-IPO executive hiring package in the whole set"

**Finding.** FY1999 10-K exhibit index L4525-4533 lists **four**: "10.9+ **Offer Letter of Employment to
Joseph Galli, Jr. dated June 23, 1999, as amended and restated September 30, 1999**"; "10.10+ Offer Letter of
Employment to **Warren C. Jenson dated September 4, 1999**, as amended and restated September 30, 1999";
"10.11+ Offer Letter of Employment to **Jeff Wilke, dated September 2, 1999**"; "10.12+ Offer Letter of
Employment to **Richard Dalzell, dated August 13, 1997**."
**Consequences for the boundary.** (i) ST3A-58/ST3A-59's uniqueness claim is false on the corpus. (ii) The
June 23 instrument ST3_A's Axis M rests on was **amended and restated on 1999-09-30** — the operative
contract is a Q3 document. (iii) Two further senior operating hires are dated **September 1999**, including
**Jeff Wilke**, whose appointment is not in any Stage-3 dossier. (iv) The FY1999 10-K's officer biographies
give the *calibre* the dossiers could not: Galli "joined Amazon.com in June 1999 as President and Chief
Operating Officer. From 1980 until June 1999, Mr. Galli held a variety of positions with **The Black and
Decker Corporation, culminating as president of Black and Decker's Worldwide Power Tools and Accessories**.
As president, he supervised the marketing, sales, manufacturing, engineering, finance, MIS, purchasing and
product service departments"; Jenson was "**Chief Financial Officer and Executive Vice President for Delta
Air Lines** from April 1998 to September 1999" and before that "Chief Financial Officer and Senior Vice
President for the National Broadcasting Company".
**Verdict: LANDED against ST3_A's stated evidence, and it moves the managerial axis to September 1999.** The
best version of Axis M is *not* "one startup hired a COO in June"; it is "between September 1999 and
December 1999 the company filed three offer letters for operating executives drawn from a Fortune-100
manufacturer, the CFO's office of a major airline, and (Wilke) an operations background — and amended and
restated the first within 90 days." That cluster is at **C5**, not **C4**.

### ST3E-26 — Attack on the acquisition ledger's names: "InnerLint" is not in the corpus; and a further 1999 acquisition sits unread in an S-8

**Finding.** ST3A-50 lists the 1999 target plans as "**InnerLint**, e-Niche, Alexa, Accept.com". The S-8
File No. 333-78651 registers the "**INNERLINX TECHNOLOGIES STOCK OPTION PLAN**"; the string "InnerLint"
returns **zero occurrences** in all 99 files. Separately, S-8 File No. 333-88825, filed **1999-10-12**,
registers the "**CONVERGENCE CORPORATION STOCK OPTION PLAN**", whose footnote (1) reads "Pursuant to an
Agreement and Plan of Merger dated as of **August 23, 1999**" — a fifth 1999 target-Company merger in the
record, named in no Stage-3 dossier, with no 8-K on disk. The FY1999 10-K mentions Convergence only inside
the auditor's consent listing its registration statements (L5503).
**Verdict: LANDED** (name correction + an omitted acquisition in the acquisition cluster). Method §14 rule 8
in miniature: a plausible counterparty name with a file number attached, printed nowhere.

### ST3E-27 — Attack on the FY1998 comparatives: the "restated once" problem is a restated *twice* problem

**Finding.** FY1998 net sales are printed as **$609,996** thousand in the FY1998 10-K and as **$609,819**
thousand in the FY1999 10-K's income statement, MD&A table and segment note — a **$177k** movement with no
reconciling note in either document. FY1997 gross profit appears as **$28,813** in one vintage and
**$28,818** in the FY1999 10-K (L2612); FY1997 cost of sales as **$118,969** (L2608). ST3_C's U-C4 records a
$29k FY1997 discrepancy between two audited statements; the pattern now has three instances across two
years, all small, all unexplained, all in the same direction of "the later document prints a different
number for the earlier year".
**Verdict: LANDED as a register conflict.** No ratio in Stage 3 changes materially — but a dataset that
quotes "$609,996" as *the* FY1998 net sales figure without the second vintage is quoting one printing of a
restated line as if it were the fact.
*(The drafting placeholder that stood here is retired; ST3E-28 follows and the number was not reused.)*

### ST3E-28 — The self-measurement inventory: what Stage 3's demand side is made of, and what is left when it is set aside

**Test.** Take every Stage-3 quantity and ask who counted. Then set aside all counts made by the issuer or
quoted by the issuer from a source that is not in the corpus, and list what remains load-bearing.
**Finding — the self-counted set, with its worst defect named.**
| Quantity | Carriers | What is missing from every carrier |
|---|---|---|
| Cumulative customer accounts 1.5m → 6.2m → 8.4m → 10.7m → 13.1m → 16.9m | FY1997/FY1998 10-Ks, 10-Qs, 8-K releases, both ARSs | a definition of "account"; whether an account is a person; no active/paid-customer measure at any date; basis changes to "inclusive of Auctions" at 1999-06-30 (ST3C-41) |
| Repeat-order share (>46/58/64%, >60%, 66%, 70%, >72%, 73%) | ARSs, 10-K, 10-Qs, releases | a definition of "repeat" or "order"; a look-back window; **the order total itself** |
| Orders | none — only percentages of orders | an absolute order count anywhere in 99 files |
| "Number one online music seller", "No. 1 online video", "3rd largest bookseller in the US", "No. 1 online bookseller in the UK and Germany" | 10-Ks and releases, always the issuer | comparator set, unit, ranking source; ST3C-46 records that the "3rd largest" claim names **no source in the release** |
| ~200,000 / 430,000 Associates | FY1998 10-K, FY1999 10-K | rate, expense, attributable revenue, attrition, duplicates (ST3E-23) |
| 8 million / 10.7 million "pre-registered, experienced online buyers" | 8-K 1999-03-30 | the count is the same cumulative-account number used to measure the service's success (ST3C-58 independence note) — self-referential |
| 1 million registered marketplace users, 1.5 million listings | FY1999 10-K only | per-service split; sellers vs buyers; GMV; any transaction count |
| Traffic/reach: Media Metrix 90th → top 20; ~16% of Web users; 117.8m/60% brand recognition | ARS 1997, FY1998 10-K, 8-K 1999-10-28 | the underlying reports are **not in the corpus**; the issuer chose which third-party number to print |
| Market size $43bn → $1.3tn | FY1998 10-K quoting Forrester | the report, the definition of "purchased over the Web", and the forecast method |
| Distribution capacity 285,000 sq ft (1997); "more than four times" (1999); ~4.0m sq ft added (1999) | ARS 1997, 8-K 1999-10-28, FY1999 10-K | no lease instrument pairs to the claimed totals; the ratios are the issuer's |
**Finding — what survives the set-aside, and it is not a small set:** every line of the audited statements
FY1996-FY1999 (net sales, cost of sales, gross profit, the six expense captions, net loss, EPS, share counts,
balance-sheet items, cash flows including the pre-working-capital subtotal); the auditor's report and its
two dates; every lease, merger plan, indenture, offer letter and registration instrument with its date and
counterparty; the subsidiary list on EX-21.1 and the named acquisition vehicles; the proxy compensation
tables, board-meeting counts and authorised-capital votes; the SC 13G blocks; the SIC cover-page strings; the
two lawsuits as pleaded by a defendant; the segment note (which is *management's own* disaggregation but is
audited as part of the statements); and the FTC information request (FY1999 10-K L1642-1645).
**Verdict — the deliverable of this record.** Stage 3's **supply, capital and legal** spine is document-based
and survives; its **demand** side is 100% issuer-counted and survives only as "the company reported". No
demand-side figure in Stage 3 is *contradicted* by anything on disk. Every one of them is *only ever asserted
by the party with an interest*, and in several cases the interest is compounded: the same number is used to
advertise the marketplace and to grade it. Those two statements must appear in the same sentence in the final
text; "unverified" alone is not enough, and "false" is not supportable.

### ST3E-29 — Attack on the record's silence: four nulls, three different kinds of null

**(i) Headcount filed at two dates (now three).** 10-Qs carry no "Employees" item — Item 2 is Properties and
Item 3 Legal Proceedings; the employees item lives in the annual report. So the absence of a quarterly
headcount is a **disclosure convention**, not a gap in the company's record and not evidence that the number
was unknown internally. It is nonetheless fatal to *this dataset's* use of it: no in-window reader could
measure headcount growth between 31 December and 31 December. Classification: **convention**; and now stale
as a count (ST3E-24).

**(ii) The Associates programme has no rate, expense or attributable revenue anywhere.** This is the hardest
of the four to classify honestly. A fee paid to referral sites is an operating cost; it would have been
disclosed if separately material under the then-applicable Rule 3-01/Item 302 practice, and it was subsumed
in "marketing and sales". So the silence is compatible with *any* size — including a programme large enough
to matter but too small to break out. The FY1999 10-K's expense captions still show no such line.
Classification: **materiality convention plus record-selection null** — the counterparty's side (a portal's
referral revenue) was never Amazon's to file, and no portal filing is in this corpus. It is **not** evidence
the programme was immaterial, and **not** evidence it was material. Any sentence in Stage 3 that reads the
200,000 count as *either* is unsupported.

**(iii) The personal guarantees: unmentioned after 1997-05-15.** Re-verified independently here, and it holds:
"Seafirst" occurs post-IPO **once**, in a lease clause using the bank's prime rate to price late rent
(10-Q Q1 1998 L14378) — no related-party content; the three guarantees and their June 19, 1996 Subrogation
Agreement (S-1 orig. EX-10.27, L18487-18622) sit only in the 1997 registration lineage. Two refinements this
pass adds:
- The S-1's own related-party note is **dated on each guarantee**: "From November 1994 **to December 1996**,
  Mr. Bezos personally guaranteed the obligations of the Company under a merchant account with Seafirst Bank.
  Since July 1995 … a bankcard merchant account with Wells Fargo Bank. Since April 1995 … company credit
  cards" (L2852-2857). So **one of the three was already over before the IPO**, and only two remained
  outstanding at the window's opening. Stage 3's "the personal guarantees" plural is therefore imprecise as
  filed.
- Item 404 would ordinarily carry a *continuing* related-party indemnity. Its absence from the FY1997 and
  FY1998 10-Ks (which route Item 13 to the proxies, whose "Certain Transactions" contains only the
  Cook/Stonesifer purchases and the Dalzell relocation loan) is **weak affirmative evidence of release**, and
  the S-1's forward undertaking ("intends to secure releases of all of Mr. Bezos' guarantees as soon as
  possible following the closing") is the reason to expect one.
Classification: **convention plus a mild pull toward one reading**, which must be written as a pull, not a
finding. Status stays **UNKNOWN — searched, not untried**; the EDGAR route is exhausted and no bank or
merchant counterparty document is available from any family.

**(iv) No merchant or bank agreement ever filed.** Verified: no exhibit index in the corpus offers a
merchant-services or card-processing agreement; the S-1's own exhibit set runs EX-2.1 → EX-27.1 with the
Subrogation Agreement as its only bank-facing paper (and that is Bezos's recourse against Amazon, not the
banks' contract). Meanwhile the *same* companies' exhibit indices do carry ordinary-course **equipment**
contracts (the five Buschman Sales Agreements) and building leases. That asymmetry is instructive: what got
filed as "material" was what the company was **spending** on, not how it was being **paid**.
Classification: **disclosure convention (Item 601(b)(10) material-definitive-agreement test)**, and it is the
reason the marketplace's contractual trace genuinely does not exist in the public record. It is *not*
evidence that Amazon had no agreements with third-party sellers beyond the click-through terms it described.

**Verdict: HELD on all four, with three reclassified.** None of the four nulls may be written as a
conclusion; all four may be written as **documented properties of the disclosure regime**, which is a finding
about 1990s e-commerce reporting rather than about Amazon.

### ST3E-30 — Folklore trace 1: the "first acquisitions" list, one name at a time

| Name in circulation | Occurrences in `sources/` (fixed-string, case-insensitive) | Earliest dated carrier in the corpus | Class |
|---|---|---|---|
| **Bookpages Limited** | 11 files / 63 hits | 8-K event 1998-04-17, filed 1998-05-01, Item 9 Reg S ("Bookpages Limited (England, April 17 1998)") | **FACT** — dated, priced within "approximately $55 million" aggregate |
| **Telebook, Inc.** | 16 files / 98 | same 8-K; S-3 333-65091 L222-235 (merger of a wholly owned subsidiary "with and into Telebook, Inc., a Florida corporation", 1998-04-24) | **FACT** |
| **Internet Movie Database** | 30 files / 46 (also "IMDb" 18 files) | same 8-K ("Internet Movie Database Limited") | **FACT**, and its stated *purpose* is dated: "a key underpinning for Amazon.com's eventual entry into online video sales" (8-K 1998-04-27 EX-99.3 L397-402) |
| **Junglee Corp.** | 35 files / 387 | 8-K event 1998-08-03 (merger plan EX-2.1); closing 8-K 1998-08-12 | **FACT**, recorded at ~$180m |
| **PlanetAll / Sage Enterprises** | 30 files / 288 | 8-K event 1998-08-03 EX-2.2; closing 8-K 1998-08-27 | **FACT**, pooled, no price |
| **Exchange.com (e-Niche Incorporated)** | **11 files / 113** | 10-Q Q1 1999 Note 7 (1999-05-17) and 8-K acc. …000717 filed 1999-04-27, headline "ACQUIRES EXCHANGE.COM, ADDING MORE THAN 12 MILLION BOOK AND MUSIC ITEMS" | **FACT** — and see ST3E-31: the instruction layer says this name appears **zero** times |
| **Accept.com** | 12 files / 147 | 8-K event 1999-06-09; S-8 333-80495 "ACCEPT.COM FINANCIAL SERVICES CORP 1998 STOCK PLAN" | **FACT** |
| **Alexa Internet** | 28 files / 228 | merger agreement dated 1999-04-24 (S-8 333-80491 fn 1); 8-K event 1999-06-08 | **FACT**, ~$250m, and an **FTC information request** attaches to it (FY1999 10-K L1642-1645) |
| **LiveBid.com, Inc.** | 8 files / 22 | 10-Q Q1 1999 Note 7: "On April 12, 1999, the Company announced that it agreed to acquire LiveBid.com, Inc." | **AGREED-ONLY in the window's quarterly record** — no closing 8-K names it; no S-8 named for it; the FY1999 10-K does not price it separately |
| **InnerLinx Technologies** | via S-8 333-78651 plan title, merger agreement dated 1999-03-30 | S-8 filed 1999-05-17 | **FACT as a plan registration**; not named in ST3_A (which calls it "InnerLint") and not in ST3_C |
| **Convergence Corporation** | S-8 333-88825 plan title, merger agreement dated 1999-08-23 | S-8 filed 1999-10-12 | **FACT as a plan registration**; absent from ST3_A, ST3_B and ST3_C's acquisition clusters |
| **Tool Crib** / **Back to Basics** | 2 files each | FY1999 10-K Note (completed 1999-10-01 and 1999-11-08; ~$112m aggregate) | **FACT, but only in a document dated after the window** — no in-window 8-K |
| **sothebys.amazon.com** | 1 file | FY1999 10-K launch table, November 1999 | **FACT of existence; its legal form (acquisition, licence or JV) is UNKNOWN** in this corpus |
| **WarehouseDirect** / **Warehouse Direct** | **0 / 0** | none | **FOLKLORE — no carrier in the corpus at any tier** |
| **Internet Mail** / **IMail** | **0 / 0** | none | **FOLKLORE — no carrier** |
| **Allaire** | **0 / 0** | none | **FOLKLORE — no carrier** |
| **Blue Nile** | 0 | none | FOLKLORE (not in Stage 3) |
| **GeoCities** | 4 files / 5 hits | press-release mention only (8-K 1998-08-03 L5879 per ST3_C §Provenance) | **NAME-ON-A-LIST**; not an acquisition claim, and Stage 3 must not let it become one |
**Note on method for this table.** Counts are fixed-string, so "Exchange.com" does **not** include the
"Exchange Commission" false positives that a naive pattern produces: a case-*insensitive dot-as-any-char*
search returns 598 hits in 94 files for that name. Anyone re-running this table must use a literal match, or
they will reproduce the error recorded at ST3E-31.

### ST3E-31 — **A landed error in the instruction layer: the master log states that Exchange.com has zero occurrences**

**Carrier:** `founders_playbook/MASTER_RESEARCH_LOG.md`, Stage-3 wave entry (L821-827):
"And **the S-4 lineages carry no named acquisition**: `WarehouseDirect`, `Internet Mail`, `Allaire`,
`Exchange.com` return **zero occurrences across all 97 local files** … The folk acquisition list is
agreed-only or absent. Recorded as RD-056/RD-057."
**Disproof.** "Exchange.com" occurs **113 times in 11 files** (fixed-string), including the headline of
8-K acc. 0000891020-99-000717, filed 1999-04-27: "AMAZON.COM ACQUIRES EXCHANGE.COM, ADDING MORE THAN 12
MILLION BOOK AND MUSIC ITEMS …"; Note 7 of the Q1 1999 10-Q; the Q2 and Q3 1999 10-Qs; and both FY1999
annual documents. ST3_A itself quotes that headline at ST3A-33, so the log's sentence **contradicts the
dossier it is summarising**.
**Why this is the dangerous class of defect.** The log is the file a cold reader trusts. An agent obeying it
would move a dated, priced, closed, HSR-cleared acquisition into the folklore column and delete it from the
ledger — the mirror image of the fabricated-number incident the project has already retracted. The three
names that really are absent (WarehouseDirect, Internet Mail, Allaire) got swept into one list with a name
that is present, and the list form is what makes the error travel.
**Verdict: LANDED — highest severity in this pass.** Correction issued at OC-203; the sentence must be
rewritten there, and any downstream register that inherited "Exchange.com: absent" must be swept.

### ST3E-32 — Folklore trace 2: corrections aimed at a document that never made the claim

**Claim attacked.** ST3_C OC-1 opens: "**(to `sources/STAGE3_INTAKE_MANIFEST.md` §'first acquisitions'…)** The
manifest's premise that 'the two S-4 lineages carry the first acquisitions (WarehouseDirect and Internet Mail)'
is not supported by the local corpus … Action: **re-point the manifest's acquisition row**."
**Disproof.** `sources/STAGE3_INTAKE_MANIFEST.md` contains **no occurrence** of "Warehouse", "WarehouseDirect",
"Internet Mail", "IMail", "Allaire", "Buschman" or "Sales Agreement", and has **no section headed "first
acquisitions"**; its headings are §1-§9 plus an orchestrator addendum, and its acquisition content is limited
to correct rows (e.g. L496, the Bookpages/Telebook/IMDB 8-K). The false premise is in **the agent briefs and
the master log**; the manifest is not its carrier. The `_EVIDENCE_CACHE.md` row that *did* carry the parallel
Sales-Agreement error (L467) has already been corrected on 2026-09-25 and says so, naming "two agent briefs".
**Consequence.** Executing OC-1 as written would have the merge edit an instruction file to remove a claim it
never made — manufacturing a correction, which §14 rule 10's incident shows is how stale claims survive: the
repair is applied to the wrong file and the real carrier stays live.
**Verdict: LANDED** against ST3_C's correction layer (the substantive part of OC-1 — the S-4 finding — is
correct and re-affirmed here at ST3E-15/OC-204).

### ST3E-33 — Folklore trace 3: two claims in circulation that the corpus positively contradicts, and one it merely fails to support

1. **"Amazon's first acquisitions were WarehouseDirect and Internet Mail, registered on the 1998 S-4s."**
   Contradicted, not merely unsupported: S-4 333-55943 registers "up to 5,000,000 shares … principally in
   connection with the acquisition, directly or indirectly, of entities" with **no target named**
   (ST3A-46/ST3C-20), and S-4 333-56723 is the 10% Senior Discount Notes exchange (ST3C-21). The resale S-3
   333-65091 names Telebook, Junglee and Sage/PlanetAll. Class: **FOLKLORE, positively contradicted as to the
   instrument**, and the two named companies are absent from the corpus altogether.
2. **"The five 1999-03-11 Sales Agreements are the marketplace's merchant contracts."** Contradicted by the
   exhibit bodies: "made by and between Amazon.com, Inc. … (hereinafter called 'Purchaser'), and **The
   Buschman Company**, an Ohio corporation (hereinafter called 'Seller')" (10-Q Q1 1999 EX-10.1 L1810-1813),
   covering Fernley Phases I–II and three undetermined "Site A/B/C" proposals. Class: **error, now corrected
   in the cache**; two agents found it independently, which is the only reason it is safe to call settled.
3. **"1-Click's launch date is in the filings."** Not contradicted — simply nowhere. The FY1999 10-K carries
   the *patent* (US 5,960,411 was granted September 1999, outside the window's documents but inside the
   FY1999 10-K's disclosure) and the phrase "1-Click technology", and ST3C-48 is honest that "No local
   document dates the day 1-Click went live." Class: **UNANSWERED**, correctly so. It stays in the record only
   as an absence, and Stage 3 must not let the FY1999 10-K's repeated "1-Click" mentions be read as a date.
### ST3E-34 … ST3E-40 — see `## Single-lineage claims`

### ST3E-34 — Attack on Axis T's exact words: the Q2 1999 sentence is narrower than ST3_A's paraphrase, and the paraphrase is what carries the argument

**Finding.** 10-Q Q2 1999 L852-854, verbatim: "…handling charges. **Net sales also include auctions revenue,
which is comprised of placement fees and sales commissions on closed auctions.**" The Q3 1999 filing widens
it: "commissions from auctions **and zShops** transactions, which includes placement fees, sales commissions
and fees from **payment service** transactions" (ST3C-40). ST3_A's C4 cell renders the Q2 sentence as
"third-party *fees and commissions* are inside the reported revenue line".
**Why the difference matters.** Placement fees are earned **whether or not anything sells** — they are
listing revenue, not transaction revenue, and they are the least "marketplace-validated" money a trading
platform can take. ST3_A's paraphrase ("fees and commissions") erases that; the filed words are the argument.
Also: nothing in the sentence shows the fees are *third-party-seller* commissions in a economically meaningful
sense — a "closed auction" commission could be taken on Amazon-adjacent inventory.
**Verdict: LANDED as a precision requirement; not a refutation.** Record the quotation, not the gloss.

### ST3E-35 — Attack on the cash series Stage 2 handed forward: a September 2000 amendment restated every cash number in the window

**Finding.** `10-K_A_FY1999_acc-0000891020-00-001638_filed-2000-09-08.txt`, Explanatory Note L94-101: this
amendment "REFLECTS CERTAIN CHANGES PREVIOUSLY REPORTED IN OUR QUARTERLY REPORT ON FORM 10-Q FOR THE PERIOD
ENDED JUNE 30, 2000. IN THAT FORM 10-Q, WE **MODIFIED OUR ACCOUNTING POLICY RELATING TO THE CLASSIFICATION OF
CASH EQUIVALENTS**, AND ACCORDINGLY WE HAVE REVISED ITEMS 6, 7, 7A AND 8 AND THE FINANCIAL DATA SCHEDULE IN
THIS REPORT. THE AGGREGATE TOTAL OF CASH EQUIVALENTS AND MARKETABLE SECURITIES HAS NOT CHANGED."
**Consequences, quantified from the amendment itself.**
| Item | Original basis (FY1998 10-K / FY1999 10-K) | Amended basis (10-K/A) |
|---|---|---|
| Cash at 1997-12-31 | $1,876k | cash and cash equivalents **$110,119k** |
| Cash at 1998-12-31 | $25,561k | **$71,583k**; marketable securities restated to $301.9m (was $347.9m) |
| Change in cash, FY1998 | **+23,685** (an increase) | **(38,536)** — a **decrease** |
| Net cash used in investing, FY1998 | (261,777) | (323,998) |
| Operating cash flow, FY1998 / subtotal | +31,035 / (41,433) | **+31,035 / (41,433) — unchanged** |
**Reading.** The reclassification does **not** touch the finding at ST3E-21 (the pre-working-capital subtotal
is identical in both documents, which independently corroborates that attack across two accessions). It does
silently invalidate any Stage-2 or Stage-3 row that prints "$1,876" or "$25,561" as *the* cash figure without
saying on which basis, because a September 2000 amendment restates the same five years on a different one —
and it flips the **sign** of FY1998's change-in-cash. Note also the manifest's own warning about this
accession: the 10-K/A's primary document carries **no SEC header block**, so its period must be cited from
the submissions index, not from the document.
**Verdict: LANDED** as a vintage conflict and an instruction-layer risk. Class: FACT (about the documents);
the underlying FY1998 liquidity position is **one fact described on two bases**, not two facts.

### ST3E-36 — Attack on the "nearly 4× management depth" reading of the ARS 1998 sentence

**Claim attacked.** ARS 1998 L157-158 (ST3_C M-31): "In 1998 our employee base grew from approximately 600 to
over 2,100, and **we significantly strengthened our management team**."
**Test.** Ask whether any *document* supports the second clause at 1998-12-31.
**Finding.** The documents support something narrower and interesting: the FY1998 10-K's officer table creates
a function the FY1997 table did not have — "Jimmy M. Wright … **Vice President and Chief Logistics Officer**.
From 1985 to 1998, Mr. Wright held a variety of logistics management positions with Wal-Mart Stores, Inc.,
**most recently as Vice President of Distribution**" (L1026-1028) — while dropping a "Vice President of
Publisher Affairs" and a "Vice President of Business Development" from the *listed* roster. Read as a set of
**instruments and titles**, the 1998 change is a **re-specification of the officer body toward physical
operations**, not a headcount of managers; read as ST3_A reads it (a count going 8 → 7) it is a contraction;
read as the ARS reads it ("significantly strengthened") it is a self-assessment.
**Verdict: HELD against ST3_A's "contraction" framing, DOWNGRADED against the ARS's "strengthened" framing.**
What the record supports: one logistics chief recruited from a named incumbent, one new CIO already in place
since August 1997, one VP of Operations gone since April 1998 with **no named successor** (ST3A-38), a CFO
unchanged since December 1996, and a board of five that did not change size in the window (ST3_A, Governance
table: "No change in board size across 1997-98, **which is itself a finding against C3**"). A company whose
board did not grow while it tripled its staff is a legitimate observation in either direction; the dossier
may not use the officer table as a scaleometer at all.

### ST3E-37 — Attack on the hindsight hygiene of Stage 3's own framing

**Test (method §2 anti-hagiography):** would these sections still read as plausible if Amazon had failed in
2001?
**Finding.** Mostly yes, and the dossiers deserve credit: ST3_C's header explicitly excludes the later fates
of WarehouseDirect/PlanetAll/Accept.com/zShops; ST3C-02/04 refuse to grade the "#1" claims; ST3C-49 refuses
the word-of-mouth/virality reading; ST3_A refuses IPO/run-rate/valuation as endpoints under §7. Three
residual contaminations, all subtle and all in the *selection* rather than the prose:
1. **Endpoint selection by retrospective salience.** The three axes ST3_A chose (a DC opened, commissions
   recognised, a COO hired) are the three things that *later* became the famous Amazon story — the fulfilment
   network, the marketplace, the professional management. Nothing in the 1999 record told a reader which
   dimensions would matter; the same record is at least as eloquent about dimensions that did **not** become
   decisive (the Associates channel, the acquired local sites, the auction format, the 4,800→200,000 enrolment
   curve). A test chosen for its future resonance is a §2 violation even when each leg is documented.
2. **Silent selection among acquisitions.** The dossiers give full weight to the deals that survived into the
   famous story and one line each to the ones the record cannot price (LiveBid: agreed, never closed in the
   window's quarterly text, never priced in the FY1999 note). That asymmetry is exactly what the record
   supports, so it is not an error — but it must be *named* as selection, per §2's record-selection null.
3. **The "$1 billion run rate" as an achievement rather than an annualisation.** Fixed at ST3E-18.
**Verdict: LANDED as a §2 finding on the boundary test's construction** (see `## Boundary challenge`), which
is the honest form of the complaint: not that the facts are hindsight, but that the *choice of which facts
define scalability* is.
### ST3E-38 … ST3E-40 — retired as placeholders

*(ST3E-38/39/40 were reserved for register checks; that work is reported inside `## Contradictions with
ST3_A and ST3_C` and `## Outbound corrections` rather than as separate attack records. The numbering is left
gapped, not reused, per §9.3's rule that identifiers never get renumbered to look tidy.)*

---

## Boundary challenge

### The test, corrected

ST3_A's three axes are the right shape and the wrong instruments. Re-grounded on this pass's documents:

- **P′ — an automated, multi-site fulfilment network actually in service.** Not the verb "opened"
  (ST3E-17 falsifies that as a discriminator); not a lease; not an announcement. The test the record can
  answer is *automation* plus *plurality*, and the company itself supplied both terms: pre-1999 its two
  plants "were manually operated" and it had "no previous experience with automated distribution centers"
  (10-Q Q3 1999 L1624-1635).
- **T′ — third-party commerce that is more than a definitional line in net sales.** The record cannot supply
  this at **any** date in the window (ST3E-02, ST3E-12, ST3E-34). It must be removed from the pass/fail set
  and carried as a documented non-disclosure.
- **M′ — an operating management beneath the founder, evidenced by executed instruments rather than by
  titles in a compliance table.** ST3_A used a name-count (ST3E-06) and a single offer letter that was
  superseded (ST3E-25).

### Candidates re-run

| # | Candidate | P′ | T′ | M′ | Verdict under the corrected test |
|---|---|---|---|---|---|
| C1 1997-12-31 | Two sites, both manual, one category | **FAIL** (no automated plant; the Delaware opening is itself an "opened" sentence — which is why the old P test passed here wrongly) | FAIL | FAIL (founder holds President+CEO+Chairman; no COO; board of five unchanged) | **FAILS, now for the right reason** |
| C2 1998-06-30 | Network unchanged; music only just launched | FAIL | FAIL | FAIL (roster identical to 1997-12-31) | **FAILS** — ST3_A's rejection is sound and untouched by this review |
| **C3 1998-12-31** | Seattle 93,000 + New Castle 200,000 + Regensburg 32,000 + Slough 41,000, **all manual**; Fernley leased only; international **segment** $21.8m = 3.6% of sales, $2.8m of foreign fixed assets; 4.13× sales, ~2,100 staff, $8.5m rent | **FAIL** on automation, PASS on plurality of *buildings* | FAIL (own-inventory retail only) | FAIL/PASS split: a Chief Logistics Officer from Wal-Mart is a structural addition; but no COO, CFO unchanged since 1996, board unchanged, and **operating cash generation was −$41.4m before working capital** | **STILL FAILS — but ST3_A's three stated reasons must be withdrawn** (share-of-growth fallacy, officer-count, boilerplate intent sentence) and replaced by the manual-plant admission, the segment size, and the negative cash subtotal. The auditor's version of ST3_A's case would not survive cross-examination; this version does |
| C4a **1999-03-31** | First automated plant **filed as opened** (Q1 1999 10-Q, filed 1999-05-17) — one site | **PASS, first time** | FAIL — auctions revenue exists and is called "minimal" by the same document | FAIL — no COO; CFO unchanged | **FAILS on M′**, but it is now the earliest date on which P′ passes, so any argument that the boundary turns on physical operation lands here, not at 1999-06-30 |
| C4 **1999-06-30** (recommended) | One automated site (Nevada), five announced | PASS but **not first** — the leg is redundant | FAIL as materiality (definition only, "minimal" the quarter before, segment gross **loss** in FY1999) | **PASS on one instrument only**, and that instrument was amended and restated 1999-09-30 | **DOES NOT SURVIVE AS REASONED.** It is not the earliest date on any axis it claims to be first at; its P leg is a re-recital, its T leg is a definition, and its M leg is a superseded draft of a contract whose final version is a Q3 document |
| **C5 1999-09-30** | Five opened in nine months, all automated; the sixth (Coffeyville KS, via Amazon.com.ksdc, Inc.) leased 1999-04-12; the Q3 filing names the states and prices nothing | **PASS** — plurality *and* automation | FAIL/PASS: auctions commissions recognised; zShops now **disputed as to month** (Q3 10-Q "late September" vs FY1999 10-K "October 1999") | **PASS, decisively** — three executed senior operating offers dated within 30 days (Galli amended/restated 09-30; Wilke 09-02; Jenson 09-04), a President/COO in post for a quarter, a new CFO, and the S-4 acquisition shelf at 30,000,000 shares since 1999-08-06 | **SURVIVES as the earliest date on which P′ and M′ are *simultaneously* satisfied by executed instruments rather than by narrative** — which is what ST3_A asked of its own test and did not get at C4 |
| C5b 1999-12-31 | Eight new DCs, ~4.0m sq ft, ten in total (named by city); first segment reporting; first marketplace user/listing counts | PASS | PASS (segment revenue $163.8m — at a gross loss) | PASS | **Only on a document filed 2000-03-23**, i.e. outside the window and outside what any contemporaneous reader had; admissible as *state at the date*, inadmissible as the *moment of transition* |

### Which survives

**C5, 1999-09-30 substantive / 1999-11-15 disclosed.** The recommended 1999-06-30 does **not** survive the
challenge — not because the wrong thing was chosen, but because the stated reasons for choosing it are
individually falsifiable on documents already in the archive. Under the corrected test the two axes that can
actually be evidenced converge: the automated network is plural by Q3 1999, and the operating management
beneath the founder is executed-by-instrument in September 1999. ST3_A already called C5 "the confirmation
date" and recommended it to anyone "requiring a conservative endpoint"; this pass finds the opposite —
C5 is the *earliest* date that survives, and C4 is the conservative-looking one that does not.

Two honest costs of moving to C5. (i) The window then includes **no** post-boundary items that ST3_A tagged
`(PB)`, so its 13 post-boundary tags are voided and its "post-boundary discipline" section must be rewritten
around 1999-10-01 → 1999-12-31 (Tool Crib, Back to Basics, Convergence, the September splits, the Q3 results
release, zShops if the October date is preferred). (ii) A Q3 endpoint rests on an **unaudited** quarterly MD&A
for the physical claim, exactly as ST3A's own confidence note concedes for Q2 — so the confidence label should
stay **Medium**, not Medium-High.

### What evidence would settle it

Ranked by whether it exists and could be obtained:
1. **The prices in the five Buschman contracts** (Rule 24b-2 redacted). They convert "a DC opened" into "$X of
   materials-handling automation commissioned for site Y" — the single best available proxy for whether the
   network was *engineered* rather than *leased*. Route: SEC release-order files for Rule 24b-2 grants, or
   Pinnacle Automation's own filings. **UNTRIED, non-EDGAR.**
2. **A dated commissioning record per site** — certificate of occupancy, a local-newspaper opening story, a
   trade-journal plant profile. That is the **periodicals family**, untried for this window by all four
   Stage-3 dossiers, and it is the only family that can produce a *day*. Method §14 rule 6 says no depth
   verdict is available until it is searched; the boundary is a depth verdict.
3. **Quarterly (not annual) segment revenue.** Impossible: FAS 131 segments were first reported for FY1999 and
   only annually. The materiality leg of T′ cannot be closed from public evidence for 1999. **UNANSWERABLE.**
4. **Section 16 Forms 3/4/5**, to date the officer cluster from the other side (the registrar's own open item;
   also the route to the founder's 540,000-share delta). **UNTRIED.**
5. **An internal organisation chart or a manager's own contemporaneous statement** — e.g. what Galli's or
   Wright's remit was in their words. **NOT KNOWABLE** from this corpus; would be Tier 3/4 at best.

**Until (1) or (2) is obtained, the boundary is a judgement about which two of three axes the project will
accept as evidence, and it should be labelled as such rather than as a finding.**

---

## What Stage 3 may not claim

Prohibitions, each traceable to a record above. If any of these appears in the merged Stage-3 text, the
boundary or the ledger has not been corrected.

1. That the Q2 1999 10-Q is the first filing to report a distribution centre as **opened** (ST3E-17), or that
   the verb "opened" marks the transition at all.
2. That third-party commissions were **material** at any date in the window, or that their recognition proves
   a transaction business (ST3E-02, ST3E-12, ST3E-34). The record proves a line item and a loss.
3. That "the first filing in the corpus" style arguments may be made without re-running the search over
   **99** files (ST3E-11).
4. That FY1998 was "the first year of positive operating cash flow" in any sense that implies the business
   funded itself (ST3E-21). FY1997 was positive; FY1998's pre-working-capital cash generation was
   **negative $41.4m**; FY1999's was negative $321.0m and its operating cash flow **negative $90.9m**.
5. That advertising became more **efficient** because its share of net sales fell (ST3E-20). The line
   containing it rose as a share of sales in 1999.
6. That Exchange.com, Accept.com, Alexa, LiveBid, e-Niche or InnerLinx are **folklore** (ST3E-15, ST3E-31) —
   and equally, that Tool Crib, Back to Basics or Convergence may be cited from a **March 2000** document as
   things a 1999 reader could see (ST3E-11's time-audit flag).
7. That any acquisition "worked", or that any of them was an **integrated success**: the record supports
   completion, consideration, goodwill lives of 2-4 years, and one FTC information request (Alexa). Nothing
   supports outcome — and a two-year amortisation life is a statement about expected duration, not a result.
8. That a **declining international share** shows the overseas expansion failed, or that a **tripling of
   international dollars** shows it succeeded (ST3E-05, ST3E-22). The filed operating measure is the segment:
   $21.8m (1998) on $2.8m of foreign fixed assets.
9. That 6.2m / 10.7m / 16.9m "customers", the repeat percentages, "8 million buyers", 140,000/200,000/430,000
   Associates, "1 million registered users / 1.5 million listings", the Media Metrix and Opinion Research
   figures, or the Forrester market size measure anything the company did not define (ST3E-28). They are
   self-reports; **they are not known to be false**, and no count outside the registrant exists.
10. That 614 → 2,100 → 7,600 is a **growth rate**. Three dates, three bases, contractors excluded from all
    three, no interim point anywhere (ST3E-24).
11. That the officer table's size measures management depth (ST3E-06, ST3E-36).
12. That "$645 million" / "$280 million" / "$55 million" are **prices paid** without the two qualifications:
    stock-value-at-announcement, and up to **$85.4m of 1999's consideration reclassified as compensation**
    (ST3E-16).
13. That the silence on the guarantees, the Associates rate, merchant agreements or headcount is **evidence
    of anything except a disclosure regime** (ST3E-29). Each stays UNKNOWN with the searches named.
14. That $1,876k / $25,561k are "cash" without a basis label (ST3E-35): a September 2000 amendment restates
    all five years on a modified definition and **reverses the sign** of FY1998's change in cash.
15. Any use of the FY1999 10-K as evidence of what was knowable **before** 2000-03-23 (ST3E-11), or of the
    HistoryLink essay, the Sheff interview, or "Get Big Fast" as in-window carriers.
16. That the boundary rests on evidence "simultaneously satisfying three axes" (ST3E-01/04/37) — the axes
    were not independent, and two of the three legs were not first.

---

## Contradictions with ST3_A and ST3_C

New IDs are allocated in the **U.220 block** (ST3_A holds U.201-U.211, ST3_C holds U-C1…U-C12; the live
`conflicts.csv` register runs to U.113). Format per method §7.

**U.220 — first use of "opened" for a distribution centre**
**CLAIM A (ST3_A, C4 and Recommendation):** the Q2 1999 10-Q (1999-08-16) is "the first filing in the whole
corpus that uses 'opened'". **CLAIM B:** FY1997 10-K L1647 (1998-03-30) "In November 1997 the Company opened a
200,000-square-foot distribution center in Delaware"; ARS 1998 L160 (1999-04-07) "We opened distribution and
customer service centers in the U.K. and Germany"; 10-Q Q1 1999 L592/L915 (1999-05-17) "leased and opened".
**WHY THEY DIFFER:** A searched 10-Qs for the word and read the 10-K's Item 2 instead of its MD&A; B searched
past tense of the opening verb across all 99 files. **EVIDENCE WEIGHT:** B is the filed text of documents A
cites elsewhere. **BEST-SUPPORTED INTERPRETATION:** A is withdrawn; the past-tense opening verb is not a
discriminator anywhere in this window. **RESIDUAL UNCERTAINTY:** none on the strings; the boundary question
reopens (see `## Boundary challenge`). **CONFIDENCE:** High.

**U.221 — Axis T's materiality**
**A (ST3_A C4):** commissions "inside the reported revenue line" = PASS, with the concession that magnitude is
undisclosed. **B (FY1999 10-K Note 14; Q1 1999 10-Q L636-637):** the group containing all new businesses,
including the marketplace, shows revenue $163.8m, **gross loss $7.8m**, segment loss $242.1m for FY1999, and
the company had already called auction revenue "minimal". **WHY THEY DIFFER:** A grades a *definition*; B
grades an *amount*. **EVIDENCE WEIGHT:** B is audited; A is MD&A prose. **BEST:** Axis T is not pass/fail-able
in this window. **RESIDUAL:** the quarterly split of the FY1999 segment is not obtainable. **CONF:** High.

**U.222 — "the only filed post-IPO executive hiring package"**
**A (ST3A-58):** one, the Galli offer letter. **B (FY1999 10-K EX index 10.9+-10.12+):** four, of which three
are dated September 1999 and the Galli instrument's operative form is the **1999-09-30 amendment and
restatement**. **WHY:** A's search space was documents dated inside the window; the exhibit list is in a
March 2000 filing. **BEST:** the executive cluster is a Q3 1999 event, not a Q2 one. **RESIDUAL:** whether
Wilke held an executive-officer title in-window is not shown (his name first appears in an FY1999 officer
table). **CONF:** High.

**U.223 — zShops' month** — **A:** 10-Q Q3 1999 L801, "In late September 1999". **B:** FY1999 10-K launch
table, "zShops **October 1999**". **WHY:** a period-end recital vs an annual ledger; the Q3 10-Q was filed
1999-11-15, the 10-K 2000-03-23. **WEIGHT:** both the registrant; the annual table is exhaustive and internally
consistent (it also dates UK/German marketplace extensions that no 10-Q dates). **BEST:** record the conflict,
print both, and stop using "late September" to make a Q3-1999 endpoint argument. **RESIDUAL:** the day is
unobtainable. **CONF:** High that they differ.

**U.224 — FY1998 net sales** — **A:** $609,996 (FY1998 10-K). **B:** $609,819 (FY1999 10-K, three places).
Extends ST3_C's U-C4 ($147,758 vs $147,787) into a pattern: **$28,813 vs $28,818** (FY1997 gross profit) and
**$118,969 vs $118,974** implied cost of sales. **BEST:** treat the later printing as the restated comparative,
keep both vintages, never average, and never cite a ratio's denominator without saying which vintage produced
it. **CONF:** High.

**U.225 — cash basis** — **A:** FY1998 change in cash **+$23,685** (FY1998/FY1999 10-K). **B:** FY1998 change in
cash and cash equivalents **−$38,536** (10-K/A, filed 2000-09-08, revising Items 6/7/7A/8). **WHY:** the cash-
equivalents policy was modified mid-2000 and all periods restated. **BEST:** both are correct on their own
basis; every Stage-2 cash row needs a basis label and a pointer to the amendment. **RESIDUAL:** no
Stage-2/Stage-3 file currently flags this. **CONF:** High.

**U.226 — the Kentucky "both opened and announced" puzzle (ST3_A U.204)** — **B now available:** the FY1999
10-K names **two** Kentucky sites, Campbellsville and Lexington, and six US 1999 openings against the Q3
10-Q's five states: five states = six sites. **BEST:** ST3_A's U.204 is resolved in favour of "two distinct
Kentucky facilities", and its instruction "report as filed, do not smooth" was correct discipline; the
resolution came from a document nobody had read. **CONF:** Medium-High (ST3_D reaches the same reconciliation
independently, in a second dossier, on the same lines).

**U.227 — attribution of the Buschman and S-4 errors** — **A (ST3_C OC-1/OC-2):** the premises belonged to
`STAGE3_INTAKE_MANIFEST.md`. **B:** the manifest contains none of the strings and no such section; the
Sales-Agreement premise is in `_EVIDENCE_CACHE.md` L467 (already struck there), and the S-4 premise is in the
agent briefs and `MASTER_RESEARCH_LOG.md`. **BEST:** re-address both corrections. **CONF:** High.

**U.228 — the "spouse and brother" 13G row** — ST3_B's ST3B-14 still describes the 1998-02-13 filers as
"Jacklyn Gise Bezos and Miguel Bezos (**spouse and brother**)"; ST3_A's COR-102 established from the form
itself that "Miguel A. Bezos is the **spouse** of Jacklyn Gise Bezos" and that both are the founder's parents.
Re-verified here against the SC 13G text. **BEST:** ST3_B carries a superseded description in a live dossier;
the correction has not reached it. **CONF:** High.
---

## Data gaps

Each row states whether the gap is **retrievable**, **conventional** (the record never had to contain it), or
**unknowable**; High-importance gaps carry a follow-up task, per §13.

| Gap | Why missing | Importance | Best available evidence | Confidence the gap is real | Follow-up |
|---|---|---|---|---|---|
| E-G01. Price of the automation that made the network "scalable" | Rule 24b-2 confidential treatment on all five Buschman contracts | **High — it is the boundary's missing quantity** | Contract structure, dates, counterparty, site assignment; rental expense $270k→$2.1m→$8.5m; FY1999 fixed-asset purchases $287.1m (FY1999 10-K L2867) | High | **RD-ST3-E1:** SEC Rule 24b-2 release-order files; Pinnacle Automation / Buschman corporate filings. **UNTRIED, non-EDGAR** |
| E-G02. A dated commissioning event for any 1999 distribution centre | no filing gives a day | **High** | "opened … during the quarter"; "In late September 1999"; city names only from 2000-03-23 | High | **RD-ST3-E2:** **periodicals + local-newspaper back files (Fernley NV, Coffeyville KS, Campbellsville/Lexington KY, McDonough GA, Grand Forks ND) — family 3, untried by all four Stage-3 dossiers**; then certificates of occupancy from the five county recorders |
| E-G03. Magnitude of third-party commissions at any in-window date | never disaggregated | **High** | Q1 1999 "minimal"; Q2 1999 definition; FY1999 segment $163.8m revenue / $242.1m loss | High | **RD-ST3-E3: UNKNOWABLE** from the filings (quarterly segments were never filed for 1999). Close the task as unknowable, not as un-tried |
| E-G04. Any quantity behind the Associates programme | never disclosed | **High** | enrolment counts at four dates, 1996→2000-02-29 | High | **RD-ST3-E4:** portal-side or press periodicals for a commission rate; the **only** route is family 3, same probe as E-G02 |
| E-G05. Fate of LiveBid.com and of the "immaterial acquisitions" totalling $44.1m | no in-window closing document; the FY1999 note groups them | Medium | Q1 1999 Note 7 agreement; FY1999 10-K "additional immaterial acquisitions during 1999 totaling $44.1 million" | High | **RD-ST3-E5:** check the Q2/Q3 1999 8-K bodies for a LiveBid closing; otherwise record as AGREED-ONLY forever |
| E-G06. Convergence Corporation: what it was, what it cost | registered only as a plan title on an S-8 | Medium | S-8 333-88825, merger agreement 1999-08-23 | High | **RD-ST3-E6:** target's own country registry (NZ Companies Office) — a non-EDGAR family, **UNTRIED** |
| E-G07. Section 16 movement for 1997-1999 | absent from the enumerated catalogue slice | **High** | proxies only | Medium-High | **RD-ST3-E7** = the registrar's open item (slice `-001`), not this pass's |
| E-G08. Court records for Wal-Mart, Intimate Bookshop, the B&N suit | no litigation file in the corpus | Medium | the defendants' own Item 3 text | High | **RD-ST3-E8:** PACER / Middle District of Arkansas / Washington federal indexes, **UNTRIED**; the Intimate Bookshop dismissal is dated only by Amazon's own sentence |
| E-G09. Release of the personal guarantees | not in the SEC record, proven | High | S-1 lineage + the Q1 1998 lease clause | High | **CLOSED for EDGAR** (manifest §3(b), ST3E-29(i)). Bank-side records are not public. Keep **UNKNOWN** |
| E-G10. Whether any of the 1998-99 acquisitions achieved what they bought for | outcomes were never disclosed in-window and are outside the firewall | **High for the analysis, unanswerable for the evidence** | goodwill lives (2-4 years), the FTC request on Alexa, the segment loss | High | Do not close. Any "it worked" sentence is a §2 violation, not a gap |

**Record-selection null for this pass (§2).** What is unrecoverable about 1997-1999 *because the winner's
archive is the one that was kept*: no internal organisation chart beneath the four filed officers; no rejected
site, category or acquisition (the corpus shows a launch ledger and nothing else — there is no document in
which Amazon explains what it decided **not** to do); no independent count of a customer, an order, a listing
or a square foot; no seller's account of what a marketplace commission cost or earned; no employee's account
of what a manual plant versus an automated one was like to run; and no press coverage that did not have the
company's own release in front of it. A Stage-3 reconstruction built on this archive will read as a sequence
of disclosed successes unless the null is printed beside the successes.

---

## Sources consulted

| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| `sources/10-K_FY1999_acc-0000891020-00-000622_filed-2000-03-23.txt` | filing (10-K) | Primary, registrant; **new to this pass, on disk since 19:55** | FY1999 | 2000-03-23 (index); header prints 20000329 | local; sec.gov/Archives/edgar/data/1018724/000089102000000622/0000891020-00-000622.txt | 1 | High — used for state at 1999-12-31 only, never as in-window knowledge |
| `sources/10-K_A_FY1999_acc-0000891020-00-001638_filed-2000-09-08.txt` | filing (10-K/A) | Primary | FY1999 restated | 2000-09-08 | local | 1 | High; **carries no SEC header block** — period established by the submissions index only |
| `sources/10-K_FY1997_…`, `sources/10-K_FY1998_…` | filings | Primary | FY1997, FY1998 | 1998-03-30, 1999-03-05 | local | 1 | High |
| `sources/10-Q_Q2-1997, Q3-1997, Q1-Q3-1998, Q1-Q3-1999` (8) | filings | Primary | 1997-06-30 … 1999-09-30 | 1997-08-14 … 1999-11-15 | local | 1 | High; **Q1 and Q2 1999 read specifically against the boundary** |
| `sources/8-K_*` (25 Form 8-K + 1 Form 8-K/A) | filings incl. EX-99 releases | Primary | 1997-11-07 … 1999-10-28 | as filed | local | 1 | High for the documents; **release figures unaudited** |
| `sources/ARS_1997_…`, `sources/ARS_1998_…` | shareholder letters | Primary, company-authored | — | 1998-04-17, 1999-04-07 | local | 1 | High that written; **self-serving → FOUNDER/COMPANY CLAIM class** |
| `sources/DEF14A_1998, DEF14A_1999, PRE14A_1998, PRE14A_1999` | proxies | Primary | — | 1998-04-17, 1999-04-07 | local | 1 | High; **the PREs are the same two instruments as the DEFs — two lineages, not four carriers** |
| `sources/S-3_*`, `S-4_*` (2 lineages), `POSAM/POSAMI`, `424B2/B3`, `S-8_*` (9) | registrations | Primary | 1997-06-06 … 1999-10-12 | as filed | local | 1 | High; each lineage = one source |
| `sources/SC13G_jeffrey-bezos…`, `SC13G_jacklyn-gise-bezos-miguel-bezos…` | holder filings | Primary, signed by the **holder** | 1997-12-31 measurement | 1998-02-17, 1998-02-13 | local | 1 | High; partially independent of the registrant |
| `sources/S-1_original_…` (EX-10.27 Subrogation Agreement l.18487-18622; related-party note l.2848-2862) | registration | Primary | 1996-06-19 | 1997-03-24 | local | 1 | High |
| `sources/STAGE3_INTAKE_MANIFEST.md` (§3(b), §3(c), orchestrator addendum) | project intake record | Secondary (internal) | — | 2026-09-25 19:56 | local | — | High; **three rows are load-bearing here** |
| `research/_EVIDENCE_CACHE.md` (L467, corrected row) | project cache | Secondary | — | 2026-09-25 | local | — | High for the correction, not for the struck claim |
| `research/ST3_A`, `ST3_B`, `ST3_C`, `ST3_D` dossiers | sibling dossiers | Secondary (this project) | — | 2026-09-25 | local | — | Read as the claims under attack; ST3_D's independent discovery of the FY1999 10-K credited at U.226 |
| `MASTER_RESEARCH_LOG.md` L805-827 | instruction layer | Secondary | — | 2026-09-25 | local | — | **carrier of the false negative at ST3E-31** |
| `adversarial_review.md` (Stage 1), `research/ST2_E_adversarial.md` | prior adversarial passes | Secondary | — | — | local | — | Format and precedent only |
| **Web: 0 of 8 WebSearch, 0 of 8 WebFetch spent.** No gap in this pass was bought with a request; the two a request might move (E-G01, E-G02) are non-EDGAR families | — | — | — | — | — | — | — |

---

## Provenance and method notes

**Lineage discipline.** Every document cited is Amazon's own except the two SC 13Gs (holder-signed) and the
auditor's consents and report dates (a separate signatory, company-appointed). Nothing in this pass is
corroborated by a competitor's filing, a court record, or an unaffiliated dataset, because none is on disk.
Where two accessions of one registrant recite one event (the Q2 and Q3 1999 10-Qs on Galli) the corroboration
count is **one** — the rule ST3_A itself applies at ST3A-59, and applies correctly.

**§14 rule 8, grep-before-write, applied to my own inherited figures.** Every number taken from ST3_A/ST3_C/
ST3_B was re-located on disk before being written: the $85.4m compensation carve-out; $774,409k and $217,241k
of stock consideration; the −$41,433k subtotal; $140.9m advertising; $188.4m fulfilment; 27.1/21.8/25.2%; the
$163,804k / $(7,801)k / $(242,148)k segment triple; $21,806k international; $2.8m/$9.4m foreign long-lived
assets; 7,600 employees; 430,000 Associates; the four offer letters; the InnerLinx and Convergence plan
titles; the $33.1m music quarter; "November 17"; and the three "opened" sentences. All print at the cited
lines. **Three figures inherited from the brief were wrong and are corrected** (COR-202): the corpus is 99
directory entries, not 97; "26 8-Ks" is 26 files in the 8-K family (25 Form 8-K + 1 8-K/A); and "**4 proxies**"
counts 4 *files* that are **2 lineages** — treating them as four carriers would reproduce exactly the error
§3's filing-lineage rule exists to prevent.

**What the dossiers got right, since the honesty of what is left standing is also graded.** ST3_A's
U.201-U.211 contradiction block, its refusal of the IPO / run-rate / valuation endpoints under §7, its ST3A-17
warning that 614→2,100 is not like-for-like, its decision to report Kentucky twice rather than smooth it, and
its "same corporate record, two accessions" treatment of the Galli recital are better practice than this
review had to reach. ST3_C's quotations survived a line-by-line re-read (ST3E-F5) and its hindsight exclusions
were pre-declared rather than retrofitted. ST3_B's §U1 table of quantities never printed anywhere is the
closest thing in Stage 3 to a proper knowability ledger, and its personal-guarantee null survived a fully
independent re-test (ST3E-F1). The failures cluster in two places only: **priority claims** ("the first
filing that…", "the only…", "never disclosed…"), and **one instruction-layer negative that is simply false**.

**Corpus drift during the pass.** `ST3_D_tech_ops.md` was written at 20:04, while this file was being built,
and independently reached the same headline discovery — that the FY1999 10-K and 10-K/A sit in `sources/` and
are cited zero times by the other three dossiers. That is **project-internal** corroboration of an
*observation*, not of any historical fact: two agents reading one document is one source (§3). It does mean
the finding is not an artefact of this reviewer's search pattern. I have not edited ST3_D and do not own it.

**§14 rule 6, four families.** Filings: rich, and the only family used by all four Stage-3 dossiers. Web
archives: Stage 2's documented CDX null before 1998-12-12 is carried, not re-probed. Periodical corpora:
**UNTRIED by every Stage-3 dossier**, and it is the family that could date a plant commissioning or price a
referral programme. Auction/museum documentary: **UNTRIED** and immaterial to this period. A depth verdict on
1997-1999 is therefore **not** available; the correct status is *filings-rich, page-level web-null,
periodicals-untried* — and per ST3E-11 the dossiers' repeated "the record does not show X" sentences are
claims about **one family**, not about the record.

**On the ethics of this pass's own method.** Two attacks here (ST3E-05/22, ST3E-20) succeed by *pairing* two
figures the dossiers held apart, and one (ST3E-18) reports against the dossier's interest by finding that a
company claim was better-labelled than Stage 3 supposed. That is the trade this role is paid for: a review
that only finds faults in one direction is a review with a thesis, and a thesis is not an audit.

**Length and file geometry.** This file overshot the 6,000-11,000-word target and now runs **21,044 words at
~136 KB**. §9.6 forbids trimming evidence to fit, so nothing has been cut to flatter the target; the merge
should split at a section boundary per §9.3 (natural cuts: before `## Boundary challenge`, before
`## Sources consulted`), keeping record numbers continuous across parts. This pass's own failure mode was
record-accumulation between writes, twice (the drafting markers retired at ST3E-17/ST3E-28 are that record).

---

## Outbound corrections

Corrections owed to other files. Nothing here deletes or rewrites another agent's text; each is an explicit
instruction to the merge. **§14 rule 10 binds: each must reach the instruction layer named, not only the
corpus where the value appears.**

**COR-201 → `MASTER_RESEARCH_LOG.md`, Stage-3 wave entry (L821-827). [CRITICAL]** Delete `Exchange.com` from
the list of names said to "return zero occurrences across all 97 local files". The name occurs **113 times in
11 files**, including the headline of 8-K acc. 0000891020-99-000717 ("AMAZON.COM ACQUIRES EXCHANGE.COM, ADDING
MORE THAN 12 MILLION BOOK AND MUSIC ITEMS"), Q1 1999 10-Q Note 7, and ST3_A's own ST3A-33. Correct the file
count to 99 and state the matching method (a case-insensitive `Exchange.com` pattern also matches "Exchange
Commission"; fixed-string matching is required). Then sweep `conflicts.csv`, `data_gaps.csv`, `sources.csv` and
`timeline.csv` for any row inheriting "Exchange.com: absent" and reset it to FACT with its 8-K citation.
RD-056/RD-057 must be **amended**, not merely appended to.

**COR-202 → the Stage-3 adversarial brief (instruction layer).** Three tasking statements are stale: "Stage
3's **two** completed dossiers" (four exist — A, B, C, D; B was on disk when this pass started, D appeared
during it); "**4 proxies**" as independent carriers (2 lineages); "**97 local files**" (99). The brief's own
self-report — "my own brief repeated a phantom S-4 acquisition lineage before any dossier existed" — is
confirmed and extended: the manifest never carried it either (COR-204).

**COR-203 → `research/ST3_A_chronology_org.md`.** (a) Withdraw C4's Axis P cell and the Recommendation's "the
verb changes to 'opened'" (U.220). (b) Withdraw or relabel the "8 names → 7" contraction used at C1, C3 and in
"the argument against this recommendation" — U.206 already forbids it (ST3E-06). (c) Re-ground ST3A-30's
"decisive against geographic expansion" on the International **segment** ($21,806k = 3.6% of FY1998 net sales;
$2.8m foreign long-lived assets) instead of the 33/25/20 share series (ST3E-22). (d) ST3A-58's "only filed
post-IPO executive hiring package" → **four** instruments, three dated September 1999, Galli's operative form
amended and restated 1999-09-30 (U.222). (e) ST3A-50 "InnerLint" → **InnerLinx Technologies**; add **Convergence
Corporation** (S-8 333-88825, merger agreement 1999-08-23) to the acquisition clusters (ST3E-26). (f) Correct
ST3A-14's note that the "$1 billion revenue run rate" lacks a stated basis — the basis is printed in the 8-K of
1999-01-26 (ST3E-18). (g) U.204 (Kentucky) may be closed as **two** facilities, Campbellsville and Lexington,
on the FY1999 10-K's Item 1 list, cross-citing ST3_D's independent reconciliation (U.226). (h) Re-run and
restate as **stale** — not as limits of the record — the "not on disk"/"never disclosed in any filing in the
set" statements at G-03, G-04, G-08, G-11 and candidate C7.

**COR-204 → `research/ST3_C_product_market.md`.** (a) **OC-1's addressee is wrong:** `sources/STAGE3_INTAKE_
MANIFEST.md` contains no "first acquisitions" section and none of the strings OC-1 attributes to it; re-address
the correction to the agent briefs and the master log, and **do not edit the manifest** (U.227, ST3E-32).
(b) "Only ever gave one category number (music, $14.4m)" → add **$33.1m** of Q4-1998 music sales (8-K
1999-01-26). (c) "Day-level dating … does not exist" → **the video store opened November 17** (same release).
(d) "Whether any third-party shop/listing count existed … outside the local corpus" → **answered**: 1 million
registered marketplace users and 1.5 million listings, Q4 1999, FY1999 10-K, with ST3E-13's four caveats.
(e) M-24's consideration row must carry the **$85.4m compensation carve-out** and the audited $774,409k /
$217,241k stock-consideration figures (ST3E-16). (f) Add the zShops month conflict as U-C13 (U.223).
(g) Re-run ST3C-20/ST3C-35's "zero occurrences across all 97 local files" at 99 files and state the matching
method, per ST3E-30's note.

**COR-205 → `research/ST3_B_finance.md`, `validation.csv`, `quantitative.csv`.** (a) Remove "first positive
operating cash flow" as a validation signal at any date; substitute the **printed** pre-working-capital
subtotals (1997 −$26,160k; 1998 −$41,433k; 1999 −$320,987k) and FY1999's operating cash flow of
**−$90,875k** (ST3E-21). (b) Add the DPO series 101.3 / 86.8 / 125.2 days with its arithmetic, which
*qualifies* the supplier-float reading rather than confirming it. (c) Basis-label every inherited cash figure
and flag the 10-K/A restatement (FY1998 change in cash **+23,685 → −38,536**; U.225). (d) ST3B-14's "spouse and
brother" → "the founder's parents, spouses of each other" (ST3_A COR-102, re-verified here; U.228).
(e) Pair §U2(c)'s marketing-efficiency figure with the fulfilment series and the 1999 rise in marketing and
sales as a share of net sales (ST3E-20).

**COR-206 → the Stage-3 merge and the boundary decision.** This pass recommends **1999-09-30 substantive /
1999-11-15 disclosed** in place of 1999-06-30, on the corrected axes P′/M′ with T′ removed from the pass/fail
set, confidence **Medium**, and with `## Boundary challenge`'s five settling-evidence items labelled UNTRIED or
UNKNOWABLE as each is. If the orchestrator keeps 1999-06-30, the reason must be restated without the three
legs this pass falsified — which on present evidence means resting it on one superseded offer letter, and the
dossier should then say so in those words.

**COR-207 → `data_gaps.csv` and `RESUME_HANDOFF.md` / `_MANIFEST.md` (instruction layer).** Add E-G01…E-G10
with the follow-up tasks exactly as labelled, and correct every row asserting the FY1999 10-K is unobtainable
("not in `sources/`", "one catalogue row plus one fetch away"): the fetch has happened, and the remaining work
is **reading**, a different and cheaper task. **Record, so it is not repeated:** the highest-value retrieval
available to this company's Stage 3 was completed by an orchestrator at 19:55 and **no dossier agent was
re-run over it** — the gap was not informational but a scheduling gap, and §14 rule 7 (one path, one owner) is
the reason it could open. The repair is a standing rule, not a one-off edit: **any corpus addition must
trigger a re-run of every prior "the record does not show X" claim in the affected stage.**
