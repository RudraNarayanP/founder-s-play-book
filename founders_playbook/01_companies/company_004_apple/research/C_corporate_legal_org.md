# APPLE STAGE 1 — DOSSIER C: CORPORATE, LEGAL AND ORGANISATIONAL RECORD

Dataset: THE FOUNDER'S PLAYBOOK — forensic reconstruction of early company state.
Company: **Apple** (`company_004_apple`), Fortune-50 universe rank #4.
Stage: **1 — origin → first real-world test of the core hypothesis**, span **1975 → 1977-01-03**
(the span fixed by `A_chronology_feasibility.md`), with the far-side window **1977-01-03 →
1981-02** admitted only where a post-1977 document is the sole carrier of a Stage-1 fact, and
then tagged `RETROSPECTIVE SOURCE`.
Dossier type: **corporate / legal / organisational** — entity formation, ownership and capital,
governance and headcount, legal and regulatory posture, termination and abandonment.
Governing spec: `00_METHOD_AND_STYLE.md` §2 (hindsight firewall + record-selection null), §3
(claim classes, confidence, independence rule, **filing-lineage rule**), §4 (legal/access
boundary), §5 (tiers), §6 (time audit), §7 (line formats), §9 (file splitting), §13 (CSV
schemas), §14 (retrieval discipline rules 1–7).

**Hindsight-firewall statement for this dossier.** Nothing after 1981 is used here as evidence
that a 1975–77 corporate, legal or organisational choice was rational, and no later Apple
entity (Apple Corporation International, Apple One, the 2007 name change, the Nevada/Ireland/
Texas structures) is imported into the founding period. The 1980 IPO figures and the 1981 cap
table are admitted **only as contemporaneously printed statements with their own dates**, never
as validation of the partnership, of the January 1977 incorporation, or of a 45/45/10 split. No
psychological claim is made about Jobs, Wozniak or Wayne beyond what a dated document says. The
litigation history that later accumulated around the "Apple" name is **not** projected backwards
into 1976–77; where the record is silent about a dispute, this dossier says silent.

**Record-selection null (§2).** The corporate interior of Apple's first 21 months is unrecoverable
in a specific way that must be stated before any record below is read: the company that existed
from 1976-04-01 to 1977-01-03 filed **nothing** that this pass could locate — no charter, no
statement of information, no stock ledger, no payroll, no lease, no registration statement. What
survives of the period's paper is (i) one private contract that left the company in 1976 and
surfaced in a 2026 auction, and (ii) **third-party print** — a hobby magazine kept by Carl Helmers
and a volunteer club newsletter kept by its editors — which recorded the *market* presence of the
firm and almost none of its *legal* being. A reconstruction of Apple's Stage-1 corporate state is
therefore built from the archive of a bystander plus one auction lot, and reads as more solid than
it is. The winners kept the contract because it became valuable; nobody kept the bookkeeping.

**Confidence scale (§3).** High = 2+ independent origins or a primary document · Medium = one
reliable source · Low = conflicting, vague or retrospective-only · UNKNOWN = no evidence recovered.

**Class vocabulary (§3).** FACT / FOUNDER CLAIM (*contemporaneous* vs *retrospective memory*) /
CONTEMPORARY OBSERVATION / RETROSPECTIVE INTERPRETATION / INFERENCE / ESTIMATE / DERIVED / UNKNOWN.

**Cross-reference convention.** Records of the two existing Apple dossiers are cited as `AP-nn`
(`A_chronology_feasibility.md`) and `A2-nn` (`A2_periodical_archive_mine.md`) instead of being
re-derived. Where this dossier's reading differs from theirs, the divergence is stated in
`## Outbound corrections` and is **not** applied to their files.

---

## Scope and working method

**What was mined first (zero web requests).** The protected local archive
`company_004_apple/sources/` — read-only; nothing in it was created, deleted, moved, renamed or
tidied by this pass:

| Corpus | Files | Content | This dossier's use |
|---|---|---|---|
| `ia_byte_1976/` | 12 issues, BYTE Jan–Dec 1976, ~5.7 MB OCR | the whole of the partnership's trading year in third-party print | name forms, dealer/market presence, the documented absences |
| `ia_byte_1977/` | 4 issues, BYTE Apr–Jul 1977 | the corporation's own first printed voice | Wozniak's byline and address, Apple's own advertisements, price ladder, the Shepardson neighbour address |
| `ia_byte_1981/` | 2 issues, BYTE Dec 1980 and Feb 1981, 1.6–1.67 MB each | the far side: IPO terms, cap table, the Bandley Drive address, the trademark-notice corpus | ownership, capital, premises, mark claims |
| `ia_homebrew/` | 13 newsletters 1975-11-30 → 1977-01-19 + the 1977-02-16 Faire flyer | the milieu's own dated paper | who was named, when, and by whom |
| `10-K_FY1994_..._filed-1994-12-13.txt` | 240,556 B | the registrant's only digital founding sentence | entity-spine date + a documented absence of founding narrative |
| `apple1registry_stories.txt` | 49 KB, curated 2022 | retrospective custody of 1973/1976 artifacts | used only for §Termination, §Contradictions, provenance |
| `_RETRIEVAL_LOG.md` | retrieval provenance | URLs, access dates, dating routes, failed endpoints | cited rather than re-probed |

**Header-contamination control (mandatory, and the reason a naive grep here over-counts).** Every
text primary in `sources/` opens with a **five-line provenance header** prepended by the
chronology probe, and line 2 of every header contains the string `company_004_apple` — i.e. **the
corpus's own provenance metadata contains the search token "apple"**. A raw `grep -i apple`
therefore returns at least one false positive per file, which is exactly the defect recorded at
`A2-05` and which would inflate the Homebrew and 1976 nulls. All counts and all line citations in
this dossier were produced by discarding matches on lines **1–5** of each file
(`grep -n -i PATTERN FILE | awk -F: '$2+0>5'`), so every number quoted below is a
**body-only** count, and the line numbers given are the on-disk file's own line numbers
(header-inclusive), which is why they match the `AP-nn` citations.

Body-only control results of that rule on this dossier's own counts: `apple` in
`ia_homebrew/hcc0211.txt` (1976-12-10) and `hcc0213.txt` (1977-01-19) = **0 body hits** (1 raw hit
each, both header); `hcc0202.txt` (1976-02-29) = **1 body hit**; `hcc0204.txt` = 2;
`hcc0209.txt` = 2; BYTE 1976 issue-by-issue body counts = 0,1,0,0,0,2,3,0,6,1,5,3; BYTE 1977
Apr–Jul = 19, 79, 31, 31; BYTE Dec 1980 / Feb 1981 = 555 / 569. **The incorporation month
(1977-01) is empty of the company's name in the one in-window primary corpus that otherwise tracks
it month by month** — see C-19.

**Independence discipline applied.** Apple's own 1994 filing, Apple's own 1977 advertisement and
Apple's own 1980 advertisement are **company-side documents from one interest**: multiple
artifacts, not multiple witnesses, and never counted as corroborating each other. BYTE's editorial
matter (Helmers), BYTE's advertisements and the Homebrew newsletters are three different origins,
but a dealer advertisement that re-runs across months is **one campaign with a duration**, not
several corroborations. The FY1994 10-K and any later Apple annual report restating "incorporated
… January 3, 1977" are **the same corporate record** under the filing-lineage rule (§3) and are
counted as one source.

**Budget.** Web requests permitted: **12**. Spent as of this section: **0**. Everything below in
`## Findings` blocks C-01 … C-19 is local-corpus evidence or a citation of the two existing Apple
dossiers; the registry, patent and EDGAR items are appended after this write and are reported with
their request-by-request outcome, including failures, in `## Web budget and unanswered requests`.

---

## Findings

Format per §7 claim record. Records are `C-nn`, dated or documented as nulls, grouped by subject.

### 1 · Entity formation: the partnership, the corporation, and what each instrument says

C-01 Claim: Apple's Stage-1 opening is **two distinct dated legal events, not one "founding"**: a
partnership instrument dated **1976-04-01** and a corporate incorporation on **1977-01-03** under
California law, nine months apart, with no document in the retrieved record making one a
continuation of the other. — Date: 1976-04-01 (partnership); 1977-01-03 (corporation) — Source:
Apple Computer, Inc., Form 10-K FY1994 Item 1 (registrant's own sentence) + BYTE, February 1981
news column (non-company print) — Source date: 1994-12-13 / 1981-02 — URL:
https://www.sec.gov/Archives/edgar/data/320193/000032019394000016/0000320193-94-000016.txt ;
https://archive.org/details/byte-magazine-1981-02 — Archived: `sources/10-K_FY1994_acc-0000320193-94-000016_filed-1994-12-13.txt`
lines 132–133; `sources/ia_byte_1981/byte-1981-02.txt` line 48498 — Tier: 1 — Class: FACT —
Passage: "Apple, incorporated in 1977, reported profits of $11.7 million on sales of $117 million
for the fiscal year ending September 26, 1980." — Conf: High (the incorporation event; two
independent Tier-1 origins: AP-04 registrant text + this non-company column) · Low (the
succession mechanics between the two dates) — Corroboration: 2 independent origins for the
incorporation year; **0 independent origins for the 1976-04-01 date read directly — it reaches
this pass through AP-20's secondary auction reporting** — Conflicts: U-C-1. This dossier's
contribution over AP-04/AP-19 is the re-verbatim of the 1981 sentence and the statement that the
two dates are **different events of different legal character**, which the universe register's
single "founded" cell erases (AP-05, U-AP-1).

C-02 Claim: **The registrant's own account of its formation is one sentence long and contains no
partnership, no founders and no 1976.** A body-only grep of the complete FY1994 10-K submission
for `incorporat|partnership|Wayne|Wozniak|founded|founder|1976|1977` returns the state-of-
incorporation header (line 29, `STATE OF INCORPORATION: CA`), the one-sentence formation line
(lines 132–133), unrelated `incorporated by reference` boilerplate, and **zero** hits for
`Wozniak`, `Wayne` or `1976`. Apple's digital corporate record therefore **dates** the company and
never **narrates** it. — Date: 1994-12-13 (document); n/a for the absence — Source: full-text grep
of the FY1994 Form 10-K — Source date: 2026-09-24 (this pass) — URL: as C-01 — Archived: as C-01 —
Tier: 1 — Class: FACT (documented absence within a primary document) — Passage:
NO_VERBATIM_PASSAGE_RECORDED (negative finding) — Conf: High — Corroboration: 1 (independently
re-run of AP-05, same document — the re-run is a check, not a second witness) — Conflicts: None.
Consequence for every Apple dossier: **anything said about formation is sourced outside
Apple's filings**, and the "company's own account" that the brief asks for is not online.

C-03 Claim: The only known **dated 1976 instrument** is a three-page partnership agreement
allocating Jobs 45 / Wozniak 45 / **Wayne 10**, with Ronald Wayne's withdrawal documents attached,
sold at Christie's on 2026-01-23 for $2,515,000; this pass has **not** read the instrument or the
auction lot text, only AP-20's secondary reports of it. — Date: 1976-04-01 (document); 2026-01-23
(sale) — Source: ITechguides + Hypebeast reporting of the Christie's lot, as catalogued in AP-20 —
Source date: 2026-08-18 / 2025-11-26 — URL:
https://www.itechguides.com/apples-founding-papers-sell-for-2-515-million-after-earlier-4-million-estimate/
; https://hypebeast.com/2025/11/apple-computer-company-founding-contract-heads-to-auction —
Archived: none in `sources/` — Tier: 2/3 reporting of a Tier-1 artifact — Class: FACT (that a dated
agreement exists and was auctioned) / **UNKNOWN (its clauses, its signature block, its stated
business address)** — Passage: "The three-page 1976 partnership agreement." — Conf: High
(existence, sale date, price) · Medium (45/45/10) · UNKNOWN (text) — Corroboration: three secondary
reports of **one** event = one origin under §3; a document nobody in this pass has read —
Conflicts: U-C-1, U-C-4. **RESEARCH DEBT (§10):** the agreement's own words are the load-bearing
missing primary of this dossier; see `## Web budget`.

C-04 Claim: **1976 print never uses a corporate name for the firm.** Across all twelve BYTE 1976
issues and all 1976 Homebrew issues (body-only counts), the company appears as
**"Apple Computer Co"** (BYTE December 1976 line 1516, in Helmers' WESCON paragraph), as
**"Apple Computers"** (BYTE December 1976 line 29856; Homebrew `hcc0209` line 234, 1976-09-15 Faire
exhibitor list), and as **"the new Apple computer"** / **"the Apple Computer"** as a machine, never
as an entity — i.e. the *entity* named in 1976 is a trading style, not a registered corporation. —
Date: 1976-09 → 1976-12 (documents) — Source: BYTE Oct/Nov/Dec 1976; Homebrew Newsletter Vol 2 No 9,
1976-09-15 — Source date: 1976 — URL: https://archive.org/details/byte-magazine-1976-12 ;
https://archive.org/details/hcc0209 — Archived: `sources/ia_byte_1976/byte-1976-12.txt`,
`sources/ia_homebrew/hcc0209.txt` — Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage: "Products,
Apple Computers, Byte Inc., Call Computer," — Conf: High — Corroboration: 2 independent carriers
(Helmers' magazine; the club's own newsletter) — Conflicts: None. Extends `A2-74` from the name
forms to the legal question: **no 1976 document in this corpus evidences a corporation.**

C-05 Claim: **"Inc." enters the record in Apple's own printed voice, not in a registry document**:
the first corporate-styled self-identification recovered in this corpus is BYTE June 1977, in
Apple's own full-page advertisement and mail-order block — "Apple Computer Inc., 20863 Stevens Creek
Blvd., B3-C, Cupertino, California 95014" (lines 2412–2413, 2459–2460), repeated identically in July
1977 (lines 4117–4118, 4168–4169) — five months **after** the 1977-01-03 incorporation date and two
months after Wozniak still signed "Apple Computer Co" in his own May 1977 article (`byte-1977-05.txt`
line 6383). — Date: 1977-06 (document); 1977-05 for the older byline — Source: BYTE June/July 1977,
Apple Computer Inc. advertisement; BYTE May 1977 Wozniak byline — Source date: 1977-06 / 1977-07 /
1977-05 — URL: https://archive.org/details/byte-magazine-1977-06 ;
https://archive.org/details/byte-magazine-1977-07 — Archived: `sources/ia_byte_1977/` — Tier: 1
(primary advertising artifact) — Class: FACT (the advertisement exists and says this) — Passage:
"Mail to: Apple Computer Inc., 20863 Stevens Creek Blvd., B3-C, Cupertino, California 95014" —
Conf: High — Corroboration: 2 printings of one campaign (counted as **one** origin per §3,
duration two months) — Conflicts: U-C-1 (name form and date sequence). A "first corporate
self-identification in print" is a *marker of* incorporation, not proof of it: an advertisement can
say "Inc." whether or not a charter exists.

C-06 Claim: **The partnership-era name form kept legal life for years after the corporation
existed** — a third party's dated bibliographic citation in BYTE February 1981 (line 28345) refers
to a December 1979 Apple publication as **"Cupertino CA: Apple Computer Co, Dec 1979"**, while
advertisers inside the same issue write "Apple Computer Co." (line 45003, line 69814, line 81055),
"Apple Computers Inc." (line 23155), "APPLE COMPUTERS INC., SAN JOSE, CALIFORNIA" (line 28157) and
"the Apple Corporation" (`byte-1980-12.txt` line 5399; `byte-1981-02.txt` line 3033). — Date:
1979-12 (cited document); 1980-12 / 1981-02 (print) — Source: BYTE February 1981, article
reference list and third-party advertisements — Source date: 1981-02 — URL:
https://archive.org/details/byte-magazine-1981-02 — Archived: `sources/ia_byte_1981/byte-1981-02.txt`
— Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage: "CA: Apple Computer Co, Dec 1979." —
Conf: High (as to what the print says) — Corroboration: multiple documents, **one magazine** —
Conflicts: None. Legal reading: two years after incorporation the market still did not know, or
care, what the entity was; **trade-name usage is therefore weak evidence of corporate identity in
this period**, which is a caution against treating any later name form as a document.

C-07 Claim: **No charter, statement of information, incorporator filing or Utah/foreign-qualification
record for Apple was located by this pass** — the California Secretary of State entity file, which
AP-06 shows the company itself names as the charter registry, was **not reachable as data** within
this dossier's budget, and no Utah filing by the 1976–77 entity surfaced in any corpus. — Date:
n/a — Source: this pass's registry attempts, reported request-by-request in
`## Web budget and unanswered requests` — Source date: 2026-09-24 — URL: UNKNOWN — Archived: —
Tier: 1 route — Class: **UNKNOWN (untried → tried and not answered, as recorded there)** — Passage:
NO_VERBATIM_PASSAGE_RECORDED — Conf: UNKNOWN — Corroboration: 0 — Conflicts: None. Stated precisely
so that no later agent reads the absence of charter text as a searched-and-empty null.

### 2 · Ownership and capital

C-08 Claim: The **only dated document anywhere in this corpus that allocates Apple's equity** is a
48-line trade-press news column in BYTE February 1981, printed **after** the offering it describes,
which states that Jobs (25) and Wozniak (30) each held **8.3 million shares**, that **A. C.
Markkula (32)** also held **8.3 million**, that **Venrock Associates** held **3.8 million**, that
"significant blocks are held by several other venture capital concerns", and that **Xerox held
80,000 shares**. Verbatim block recovered in full this pass at `byte-1981-02.txt` lines 48491–48527.
— Date: 1980-12 (offering) / 1981-02 (publication) — Source: BYTE February 1981, p 212, "Apple
Stock Goes On Sale" — Source date: 1981-02 — URL: https://archive.org/details/byte-magazine-1981-02
— Archived: `sources/ia_byte_1981/byte-1981-02.txt` — Tier: 1 (contemporaneous trade-press report;
author of the unsigned column not identified — logged as a gap) — Class: FACT (as to what was
printed) / CONTEMPORARY OBSERVATION (as to the holdings) — Passage: "Steve Jobs, 25 years old, and
Steve Wozniak, 30 years old, the creators of the Apple computer, each hold 8.3 million shares." —
Conf: High that it was printed; **Medium that the figures are a restatement of the prospectus
rather than the author's arithmetic** — Corroboration: 1 (AP-18 is the same document, not a second
witness) — Conflicts: U-C-2 (the printed "8%" does not reconcile with the printed share count).
Column authorship unresolved; the cap table's *provenance* is therefore a chain of one unnamed
journalist back to a document nobody in this pass has read. That is the honest status of every
"early cap table" figure in this dossier.

C-09 Claim: **Equity value implied by the printed terms is a derived number, and the column itself
derives it loosely.** Arithmetic: 8.3M × $22 = **$182.6M** per founder, which the column renders as
"well over $100 million worth of stock" (lines 48512–48515 — correct but understated); offering
size 4.6M × $22 = **$101.2M** gross. — Date: 1980-12 — Source: DERIVED from C-08's printed inputs —
Source date: 1981-02 — URL: as C-08 — Archived: as C-08 — Tier: 1 inputs → derived — Class:
**DERIVED** — Passage: "That means that they own well over $100 million worth of stock." — Conf:
High (arithmetic on printed numbers) · Medium (that the printed numbers are right) — Corroboration:
0 (inputs are one document) — Conflicts: None. Per §8 no derived value is presented as observed;
per §6 the figure is a **primary-market offer value, not a wealth realisation, not market
capitalisation after trading, and not a company valuation**.

C-10 Claim: **No dated instrument in any corpus searched states any cash contribution by any
founder, nor any early valuation of the enterprise.** The candidate figures all fail the §3
independence test at this pass: the HP-65-for-$500 / VW-bus-for-$750 = $1,000 board-printing story
is a single 2006 autobiography repeated downstream (AP-32, corroboration **0 independent**); the
$15,000 working-capital loan is one founder's retrospective memory (AP-29); Wayne's "$800 up front
plus a later $1,500" for his withdrawal reaches this pass only through auction press coverage
(AP-20); Markkula's $91,000 guarantee / $250,000 / 26–28% terms appear in **no** retrieved document
(AP-175 line of the probe's Famous-claims table; "Markkula" occurs **exactly once** in the whole
cached corpus — see C-11). — Date: 1976 (claimed events) — Source: negative across `sources/` +
AP-20/29/32 — Source date: 2026-09-24 — URL: n/a — Archived: `sources/` — Tier: n/a — Class:
**FOUNDER CLAIM (retrospective memory)** for each figure; **UNKNOWN** for the underlying fact of who
put in what — Passage: "And Steve Jobs sold his VW bus for US$750." (registry quoting iWoz, quoted
in AP-32) — Conf: Low — Corroboration: 0 independent for every monetary figure in this paragraph —
Conflicts: U-C-3. This is the dossier's central negative and it is stated as a finding, not as a
caveat.

C-11 Claim: **A. C. Markkula appears exactly once in the entire cached corpus** — the single
February 1981 sentence at `byte-1981-02.txt` line 48516, "A C Markkula, 32 years old, who took
Apple from a garage operation to its current enviable position, also holds 8.3 million shares" —
and **never** in any 1976 or 1977 issue. — Date: 1981-02 — Source: BYTE February 1981 — Source
date: 1981-02 — URL: as C-08 — Archived: as C-08 — Tier: 1 — Class: CONTEMPORARY OBSERVATION (role
and holding, as printed) — Passage: "who took Apple from a garage operation to its current
enviable position" — Conf: Medium — Corroboration: 1 — Conflicts: None. Two readings must be kept
apart: (i) a man named Markkula held a founder-sized block by 1980-12 — contemporaneous; (ii) the
*garage-operation* characterisation is a 1981 retrospective gloss on 1976, and is the only place in
this corpus where that phrase is attached to Apple. It is Tier-1 evidence **of a 1981 opinion**,
not of a 1976 fact.

C-12 Claim: **Venrock Associates' 3.8 million shares is the only documentary trace of outside
venture capital in the founding period, and it is a holding reported after the offering, not a
round.** No amount, no date, no valuation, no certificate of investment and no partner's name
attaching to Apple appears in any retrieved text. — Date: 1981-02 (document) — Source: BYTE
February 1981 — Source date: 1981-02 — URL: as C-08 — Archived: as C-08 — Tier: 1 — Class: FACT
(as printed) / **UNKNOWN (the transaction behind it)** — Passage: "Venrock Associates, a venture
capital firm, holds 3.8 million shares." — Conf: Medium — Corroboration: 1 — Conflicts: None.
Xerox's 80,000 shares (same column) is the only other corporate holding named; it evidences **a**
shareholder, not a strategic investment, and no Xerox–Apple agreement was located.

### 3 · Governance, roles, headcount and premises

C-13 Claim: **No governance office is ever attached to any Apple principal in the cached corpus.**
The complete body-only name census for the founders across 16 BYTE issues and 13 newsletters is:
`byte-1976-12.txt:1516` (Steven Jobs, Apple Computer Co), `byte-1977-04.txt:2703-2770` (both
founders, as visitors), `byte-1977-05.txt:6381` (Wozniak as author), `byte-1981-02.txt:48509-48510`
(both, with ages and holdings) — and **no occurrence of "president", "vice president", "chairman",
"treasurer", "secretary", "board of directors" or "officer" anywhere in the corpus is joined to an
Apple name**. — Date: 1975-11 → 1981-02 (window searched) — Source: exhaustive body-only grep of
`sources/ia_byte_*` and `sources/ia_homebrew/` — Source date: 2026-09-24 — URL: n/a — Archived:
`sources/` — Tier: 1 (documented absence within these documents) — Class: FACT (the census) /
**UNKNOWN (the offices themselves)** — Passage: NO_VERBATIM_PASSAGE_RECORDED (negative finding) —
Conf: High for this corpus, **Medium as a general statement** (the corpus skips BYTE Aug 1977–Nov
1980 entirely, and trade press rarely printed officer lists) — Corroboration: 1 method —
Conflicts: None. Consequence: the earliest documented officer of Apple Computer, Inc. is **not**
establishable from any retrieved document; only the California SoS statement-of-information
successors or the 1980 prospectus can settle it.

C-14 Claim: **Apple's first employees are unnamed in every in-window document this pass holds.**
The corpus contains no job advertisement, no payroll line, no staff list and no named
non-founder Apple employee; "Apple employee #6" (Randy Wigginton) enters the record only through a
2022 curated registry page (AP-31), i.e. retrospective attribution with no payroll document behind
it. — Date: 1976 → 1981-02 (searched window) — Source: negative across `sources/`; AP-31 for the
competing retrospective — Source date: 2026-09-24 / 2022 — URL:
https://www.apple1registry.com/en/stories.html — Archived: `sources/apple1registry_stories.txt` —
Tier: 1 (absence) / 3 (the numbering claim) — Class: **UNKNOWN**, with the numbering claim as
RETROSPECTIVE INTERPRETATION — Passage: "Randy's brother, Ralph Wigginton, built the cases." —
Conf: High that the corpus is silent · Low on any employee sequence — Corroboration: 0 for the
numbering — Conflicts: None.

C-15 Claim: **Premises have a dated printed sequence and it is not the garage.** Apple's own
address of record is 20863 Stevens Creek Blvd, Bldg. B3-C, Cupertino 95014, telephone (408)
996-1010, printed in Wozniak's May 1977 byline (`byte-1977-05.txt:6385-6387`) and in Apple's own
June and July 1977 advertisements; by BYTE December 1980 the company's own advertisement gives
**"Apple Computer, 10260 Bandley Drive, Cupertino, CA 95014"** with toll-free numbers 800-538-9696 /
in California 800-662-9238 (`byte-1980-12.txt:4006-4010`, repeated `byte-1981-02.txt:1954-1957`).
**No 1976 print in the corpus places the company at any address, and no document names a Los Altos
premises.** — Date: 1977-05, 1977-06, 1980-12 (documents) — Source: BYTE May/June/July 1977 and
December 1980, Apple's own advertisements and byline — Source date: as listed — URL:
https://archive.org/details/byte-magazine-1977-05 ; …/byte-magazine-1977-06 ; …/byte-magazine-1980-12
— Archived: `sources/ia_byte_1977/`, `sources/ia_byte_1981/` — Tier: 1 (primary advertising
artifacts) — Class: FACT — Passage: "Apple Computer, 10260 Bandley Drive, Cupertino, CA 95014." —
Conf: High — Corroboration: 4 printings of 2 campaigns (counted as 2) — Conflicts: U-C-1 (place).
Supporting detail: the adjacent unit at **20823** Stevens Creek Blvd, Bldg C4-H, was Shepardson
Microsystems Inc, named in BYTE April 1977 line 35103 — a documented professional-park context for
Apple's 1977 address, independently noted at `A2-58`.

### 4 · Legal and regulatory posture

C-16 Claim: **By December 1980 third-party advertisers were asserting the APPLE mark as already
registered, and doing so in inconsistent ways**: a body-only census of the two far-side issues
recovered **47 advertisement lines** across BYTE December 1980 and February 1981 carrying a
trademark or trade-name notice naming Apple (line-level count; OCR fragmentation makes a clean
*advertiser* count impossible from the text layer, so 47 lines is the number this dossier will
defend and the number of firms is UNKNOWN) — "Apple II is a trademark of APPLE COMPUTER, INC" (`byte-1980-12.txt:4643`), "Apple is a registered trademark of Apple Computer, Inc."
(`:67216`), "Apple and Apple II are registered trademarks of APPLE COMPUTERS INC., SAN JOSE,
CALIFORNIA" (`:35646`), "Apple II, Apple II Plus, and Applesoft are trademarks of the Apple
Corporation" (`:5398-5399`), "TRS-80, APPLE and ATARI are trademarks ol Tandy, Apple Computer Co.,"
(`byte-1981-02.txt:45003`) — while **no Apple advertisement in BYTE 1976 or 1977 carries any
trademark or registration notice for the name** (body-only search of `ia_byte_1976/`,
`ia_byte_1977/` returns zero `apple` + mark/registered/copyright conjunctions). — Date: 1976 →
1980-12 (searched window) — Source: census of BYTE advertisements — Source date: 1976–1981 — URL:
as cited per file — Archived: `sources/ia_byte_*` — Tier: 1 — Class: **DERIVED** (the count: `grep -n -i apple <the two 1981 files> | awk -F: '$2+0>5' | grep -i -E "trademark|trade name|trade mark|regis.*mark|marco registrado"` → 47 lines) / FACT (each quoted line) — Passage: "Apple II is a registered trademark of Apple Computer Inc." — Conf: Medium (OCR damage affects several lines; each was inspected) · High
(that 1976–77 Apple print carries no mark notice) — Corroboration: many documents, one publication
family — Conflicts: None. Legal reading, capped deliberately: third-party notices prove **the mark
was believed protected by 1980**, they do not date the application or the registration, and the
1976–77 silence is *consistent with* an unregistered name but does not establish one. The register
itself is the only instrument that can settle this — see `## Web budget`.

C-17 Claim: **The name dispute between the computer company and the record company leaves no trace
in this corpus**: body-only searches of all 16 BYTE issues and 13 newsletters return **zero**
occurrences of `Apple Corps`, `Apple Records`, and zero occurrences of `infringe`, `injunction`,
`cease and desist` or `lawsuit` joined to Apple; the only "Beatles" string in the 1976 corpus is a
1976-08 software-piracy column reference to recorded music (`byte-1976-08.txt:1911`). — Date:
1975-11 → 1981-02 (window searched) — Source: exhaustive grep, method as in C-13/C-16 — Source
date: 2026-09-24 — URL: n/a — Archived: `sources/` — Tier: 1 (absence within these documents) —
Class: FACT (the census) — **not** a finding that no dispute existed — Passage:
NO_VERBATIM_PASSAGE_RECORDED (negative finding) — Conf: High for the searched months —
Corroboration: 1 — Conflicts: None. **Structural reason for the silence, stated so it is not
mistaken for a null:** the cached corpus contains **no BYTE issue between 1977-08 and 1980-11**, so
it cannot see 1978–79 at all, which is the period in which a record-company action against a
computer company would first have had to appear in trade print. The brief's demand for the
trademark dispute is therefore answered here as **locally unseeable, externally tried** — see
`## Web budget and unanswered requests`.

C-18 Claim: **Liability posture differs between the two Stage-1 entities and only one of the two
difference-makers is documented.** For the corporation: Apple Computer, Inc. was "incorporated
under the laws of the State of California" (C-01), which places it inside California corporate
law from 1977-01-03 — Tier 1, registrant's own text. For the partnership: the only direct statement
of its liability character is Ronald Wayne's retrospective account that "we'd founded the Apple
Computer 'Company,' [so] there was no 'corporate' protection if the business failed" (AP-29), plus
the observable fact that **no 1976 document in any retrieved corpus asserts limited liability for
the firm** (C-04). — Date: 1976-04-01 → 1977-01-03 — Source: AP-29 (first-party retrospective) +
the FY1994 10-K sentence + the 1976 corpus absence — Source date: 2022 / 1994-12-13 / 1976 —
URL: as cited — Archived: `sources/apple1registry_stories.txt`, `sources/10-K_FY1994_...txt` —
Tier: 1 / 3 — Class: FACT (the corporate side) / **FOUNDER CLAIM (retrospective memory)** (the
partnership side) / INFERENCE (that general liability was the partnership's posture) — Passage:
"there was no 'corporate' protection if the business failed" — Conf: High (corporation) ·
Low-Medium (partnership posture) — Corroboration: 1 each — Conflicts: None. **This is a firewall
point, not a moral:** the record does not show the partnership's exposure being *accepted* as a
calculated trade-off; it shows nobody writing about it.

### 5 · Termination and abandonment (mandatory section; not optimised for inspiration)

C-19 Claim: **The machine the company was formed around was withdrawn from its own advertising
within months of the corporation's first print.** Apple's June and July 1977 advertisements sell
the Apple II at $1,298 complete and a "board-only version … for the do-it-yourself hobbyist" at
$598 (`byte-1977-06.txt:1908-2110`; `byte-1977-07.txt:3892-4169`), while the **Apple-1 is offered
by the company in no advertisement anywhere in the cached corpus after May 1977**, and Wozniak's
own May 1977 article speaks of it in the past tense ("was designed late in 1975 and sold…"). The
first-party 1976 price of the Apple-1 was never printed by Apple in this corpus at all. — Date:
1977-06 → 1977-07 — Source: BYTE May/June/July 1977 — Source date: 1977 — URL: as C-05 — Archived:
`sources/ia_byte_1977/` — Tier: 1 — Class: FACT (printed offer corpus) / INFERENCE (that absence
from the maker's advertising equals withdrawal) — Passage: "The Apple-I, my first video oriented
single board computer, was designed late in 1975 and sold by word of mouth throughout California" —
Conf: Medium-High — Corroboration: 3 printings, one company — Conflicts: None. Records the same
termination as `A2-72` from the price side; the C-reading is that the **product line the partnership
was formed to sell ended inside the corporation's first advertised quarter**, with no announcement,
no discontinuation notice and no remaining-stock statement anywhere in print.

C-20 Claim: **The incorporation month is empty in the corpus that had been tracking the firm month
by month.** Homebrew's newsletters of 1976-12-10 (`hcc0211`) and 1977-01-19 (`hcc0213`) contain
**zero body-line occurrences of `apple`**, after five consecutive issues carrying it between April
and September 1976 — i.e. the founding period's best outside primary source goes quiet precisely
across 1976-12 → 1977-01, when the partnership became a corporation, and BYTE 1977 begins its Apple
coverage only in April. — Date: 1976-12 → 1977-01 — Source: body-only grep of `ia_homebrew/` (the
single raw hit per file is the corpus's own provenance header, excluded per method) — Source date:
2026-09-24 — URL: https://archive.org/details/hcc0211 ; https://archive.org/details/hcc0213 —
Archived: `sources/ia_homebrew/` — Tier: 1 (documented absence) — Class: FACT (the count) —
Passage: NO_VERBATIM_PASSAGE_RECORDED (negative finding) — Conf: High that these two issues are
silent · **not** that the company was inactive — Corroboration: 1 — Conflicts: None. Bound: the
newsletter is not a corporate record and did not report every entity every month; this is silence,
and it is logged so that nobody later mistakes the April 1977 resumption for a January event.

C-21 Claim: **Ronald Wayne's exit from the enterprise is invisible in the founding-era record**:
body-only census of `Wayne` across all 16 BYTE issues and 13 newsletters returns **23 hits, all
unrelated** — Dwayne Jeffries, Wayne Sewell, Fort Wayne IN, Wayne PA, Wayne State University, J
Wayne Reitz, "John Wayne epic", Wayne Green, and one club-press masthead — i.e. **zero occurrences
of Ronald Wayne**, in any spelling, in any in-window document this pass holds. — Date: 1975-11 →
1981-02 — Source: exhaustive body-only grep — Source date: 2026-09-24 — URL: n/a — Archived:
`sources/` — Tier: 1 (absence) — Class: FACT (the census) — Passage: NO_VERBATIM_PASSAGE_RECORDED —
Conf: High — Corroboration: independent re-run of `A2-52` / `A2-73` on the same corpus (a check,
not a second witness) — Conflicts: None. Legal consequence: the third 1976 signatory's
**withdrawal is documented nowhere in the period's press**; everything about it — the date, the
$800, the $1,500, and the litigation Wayne later initiated to cut his name from the partnership's
debts — rests on the auctioned withdrawal papers (unread) or on the court record (not reached by
this corpus). The 1981 column listing three 8.3M-share holders and no fourth name is the closest
in-window trace, and it is an *absence*, not a record of termination.

C-22 Claim: **A partnership instrument died inside the same window the corporation was formed, and
no document in any corpus searched records the mechanics of that supersession.** Nothing retrieved
states whether the 1976-04-01 agreement was terminated, assigned, absorbed or simply abandoned on
1977-01-03; whether the partnership's debts (if any) were assumed by the corporation; or whether
the three signatories received identical consideration. — Date: 1976-04-01 → 1977-01-03 — Source:
documented absence across `sources/`, AP-04/20, and the two registry attempts recorded in
`## Web budget` — Source date: 2026-09-24 — URL: n/a — Archived: — Tier: n/a — Class: **UNKNOWN** —
Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High that no such document surfaced — Corroboration:
0 — Conflicts: None. **This is the single most important unanswered legal question of Apple's
Stage 1**: the entity sequence in the brief's own words — who signed, who was left out and what
happened to what they signed — cannot be closed without the instrument and a charter record.

C-23 Claim: **Other abandoned paths visible in the period's print, carried so the section is not
only about departures:** (i) the maker's own 1976 advertising channel was never used — Apple placed
**no advertisement of its own in BYTE during 1976** (AP-22), and its first self-published BYTE
advertisement is June 1977 (C-05), so the partnership's market presence in its own year ran entirely
through dealers it did not control; (ii) the partnership-era name form "Apple Computer Co" is
abandoned by the company's own print from June 1977 while persisting in third-party citation to
1981 (C-04, C-06); (iii) the 1976 board-only product is absent from the maker's print after May 1977
(C-19). — Date: 1976 → 1977-07 — Source: AP-22 + C-05/C-19 census — Source date: 1976–1977 —
URL: as cited — Archived: `sources/ia_byte_1976/`, `ia_byte_1977/` — Tier: 1 — Class: FACT
(advertisement corpus) / INFERENCE (that non-use equals abandonment of a channel) — Passage:
"Mail to: Apple Computer Inc., 20863 Stevens Creek Blvd., B3-C, Cupertino, California 95014" —
Conf: Medium-High — Corroboration: 2 (different advertisers and years) — Conflicts: None. The
method's §2 point applies: these are the exits nobody printed, and they are recoverable only as
silences with a counted denominator.

### 6 · Provenance of the in-window "primary" material (a finding about the evidence, not the firm)

C-24 Claim: **The most-cited "in-window" Apple primary is not a record of Apple's entity at all, and
in one case not even a record of the club that printed it.** The April 1976 passage naming Wozniak —
"In April the APPLE 6502 system was our special guest. We are grateful to STEVE WOZNIAK for
providing transportation." — sits inside a section headed **"NOTES FROM THE NORTH"**, signed by the
**Sonoma County Micro Computer Club**, meeting at LO*OP Center in Cotati, i.e. reprinted
correspondence from a *different* club's letter, in which "an APPLE" appears in a list of machines
owned by that northern club alongside ALTAIRs, an IMSAI, a JOLT and two PDP-8s. — Date: 1976-04-30 —
Source: Homebrew Computer Club Newsletter Vol 2 No 4, lines 128–141 — Source date: 1976-04-30 —
URL: https://archive.org/details/hcc0204 — Archived: `sources/ia_homebrew/hcc0204.txt` — Tier: 1
(contemporaneous, self-dated) — Class: CONTEMPORARY OBSERVATION (of a northern club's inventory and
of Wozniak driving a machine to it) — Passage: "The SONOMA COUNTY MICRO COMPUTER CLUB is small but
powerful. We are a group of several ALTAIR* s , an IMSAI, a JOLT, two PDP-8's, an APPLE and some
others on order." — Conf: High — Corroboration: 1 document — Conflicts: None. This sharpens the
AP-24/AP-27 note into a rule for the dossier: **the sentence is evidence about the diffusion of the
Apple-1 board among hobbyists in April 1976, and about Wozniak as a named supplier of one, and it is
not evidence about the partnership's formation, its address, or its customers.**

C-25 Claim: **The one document that names Jobs and the company simultaneously predates the
corporation by two months and is a third party's off-hand remark**, not a filing or a press
release: Helmers' December 1976 editorial records conversations on the WESCON floor "last September"
with "Steven Jobs (Apple Computer Co)" and "Paul Terrell (Byte Shops)". — Date: 1976-09 (event) /
1976-12 (publication) — Source: BYTE December 1976 editorial — Source date: 1976-12 — URL:
https://archive.org/details/byte-magazine-1976-12 — Archived: `sources/ia_byte_1976/byte-1976-12.txt`
line 1516 — Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage: "my conversations with
entrepeneurs … Steven Jobs (Apple Computer Co) and Paul Terrell (Byte Shops) on the floor of the
WESCON show last September" — Conf: High — Corroboration: 1 witness; `A2-16` notes the same
parties' independence limits — Conflicts: None. **Survivorship caution (§2, §6):** the corpus's
founder-side "contemporaneous" record is dominated by one editor who knew both men personally
(AP-10, AP-15, `A2-31`); this dossier's corporate conclusions are drawn from the *advertising and
census* layer precisely because the editorial layer is a single relationship.

C-26 Claim: **A "Utah filing" route for the 1976–77 entity produced nothing and is recorded as
searched, not as assumed absent**: no document in any corpus examined by this pass names a Utah,
Delaware or Nevada Apple entity before 1990, and the only non-California jurisdiction appearing in
Apple's own digital corporate record is the state-of-incorporation field "CA" (FY1994 10-K line 29).
— Date: n/a — Source: FY1994 10-K + corpus grep + the registry attempts logged in `## Web budget` —
Source date: 1994-12-13 / 2026-09-24 — URL: as C-01 — Archived: `sources/10-K_FY1994_...txt` —
Tier: 1 (the field) — Class: FACT (what the digital record shows) / **UNKNOWN (what a paper Utah
corporations file might hold)** — Passage: "STATE OF INCORPORATION: CA" — Conf: Medium —
Corroboration: 1 — Conflicts: None. The hypothesis that Apple used a Utah registration — which
several 1970s small technology firms did for tax reasons — is **not supported by one document here
and has not been falsified against Utah's paper index**; both halves of that sentence are the
finding.

### 7 · The founding instrument as catalogued by the auction house (external pass)

The 1976-04-01 agreement could not be read directly; what follows is the **cataloguer's own lot
record**, retrieved as an archived copy of Christie's lot page for sale 24256. Under §5 an auction
catalogue is a commercial aggregator of a Tier-1 artifact: its **bibliographic and physical
description** (dates, page count, signature names, stated place) is the closest thing to the
document that this pass holds, and its **narrative essay** is Tier-3 restatement of memoir and
interview material. The two are classified separately in every record below and must not be merged
by any later pass.

C-27 Claim: **The founding instrument is a three-page typed document bearing three signatures, and
the only dated artifact in any corpus examined that names all three principals together.** Christie's
lot 242 describes it as: "THE APPLE COMPUTER COMPANY PARTNERSHIP AGREEMENT / JOBS, Steve (1955-2011),
WOZNIAK, Steve (b.1950), and WAYNE, Ronald (b.1934). Typed document signed ('Stephen G. Wozniak',
'steven p jobs' and 'Ronald Wayne'), [Mountain View, California] 1 April 1976. Three pages,
letter-sized paper. **With: Amendment letter to the above.** Typed document signed ('Stephen G.
Wozniak', 'steven p jobs' and 'Ronald Wayne'), **12 April 1976**. One page, letter-sized paper.
Together, four pages." — Date: 1976-04-01 (principal instrument); 1976-04-12 (amendment letter) —
Source: Christie's, Live Auction 24256 "We the People: America at 250", Lot 242, lot description —
Source date: sale 2026-01-23; page retrieved 2026-09-24 — URL:
https://www.christies.com/en/lot/lot-the-apple-computer-company-partnership-agreement-6570347/ —
Archived: retrieved as an archived copy via web.archive.org (122,082 B; **no local copy written —
`sources/` is read-only to this pass**, see Provenance note P-3) — Tier: 3 catalogue describing a
Tier-1 primary — Class: FACT (that a dated three-page typed instrument with three named signatures
and a one-page amendment of 12 April 1976 exists and was catalogued) / **UNKNOWN (the wording of
its clauses; the catalogue does not transcribe them)** — Passage: "Typed document signed … 1 April
1976. Three pages, letter-sized paper." — Conf: High (existence, page count, both dates, three
signatories) · UNKNOWN (clauses) — Corroboration: 1 cataloguer + the earlier Sotheby's 2011
custody event (C-31), which is the same object not a second witness — Conflicts: U-C-1 (place),
U-C-4 (Wayne's percentage and exit interval). **The material content this dossier cannot reach is
the clause text**: nothing retrieved states the capital-contribution, dispute-resolution or
dissolution terms the brief asks for, so every such statement in §1 and §5 of this file stays
UNKNOWN rather than being inferred from the amendment's existence.

C-28 Claim: **A second, separately dated 1976 instrument signed by all three men exists — the
"Amendment letter" of 12 April 1976 — eleven days after formation, and the catalogue states that on
that footing Wayne "withdrew from the partnership in exchange for $800": "However, just eleven days
later, wary of the financial risk, Wayne withdrew from the partnership in exchange for $800."** —
Date: 1976-04-12 — Source: Christie's lot 242, description and lot essay — Source date: 2026-01-23 —
URL: as C-27 — Archived: as C-27 — Tier: 3 (essay) describing Tier-1 (dated amendment) — Class:
FACT (an amendment letter of that date signed by all three exists in the lot) / **FOUNDER CLAIM
(retrospective memory)** for the $800 and the motivation, which the essay does not document —
Passage: "just eleven days later, wary of the financial risk, Wayne withdrew from the partnership in
exchange for $800." — Conf: High (the dated amendment) · Low (the consideration and its reasons) —
Corroboration: the eleven-day interval is **internally corroborated by the lot's own two dates**
(1 April → 12 April), which is the strongest single documentary point this pass adds anywhere —
Conflicts: U-C-4. Note the arithmetic basis, stated so no pass conflates it: 1 April to 12 April is
**11 days**, so the ubiquitous "12 days" (AP-20's "12 days" retelling) is a rounding of a dated
instrument, and the $800 figure appears here **without** the later $1,500 leg that AP-20 reports.

C-29 Claim: **The instrument allocated functions, not offices, and the allocation is quoted from the
catalogue: Wayne's responsibilities were listed as "Mechanical Engineering and Documentation",
Wozniak's as "Electrical Engineering", and Jobs's as "Electrical Engineering and Marketing."** —
Date: 1976-04-01 — Source: Christie's lot 242 lot essay — Source date: 2026-01-23 — URL: as C-27 —
Archived: as C-27 — Tier: 3 quoting a Tier-1 document it holds — Class: FACT (that the agreement
contains such designations, as read by the specialist who handled the lot) / UNKNOWN (the exact
clause form) — Passage: "Wayne's responsibilities were listed as 'Mechanical Engineering and
Documentation;' Wozniak's as 'Electrical Engineering;' and Jobs's as 'Electrical Engineering and
Marketing.'" — Conf: Medium — Corroboration: 1 — Conflicts: None. **This qualifies C-13**: the
absence of the words "president" or "vice president" in the period's print is not evidence that the
firm had no division of authority; the founding instrument recorded a functional split, and it put
**both** engineering and marketing on Jobs while giving Wayne the documentation function and
Wozniak the electrical design. It also shows the enterprise was organised as a **working
partnership of three named functions**, which is a governance fact, and that "Marketing" was a
labelled responsibility of a firm with, as yet, nothing of its own advertised (C-16, AP-22).

C-30 Claim: **The founding contract was drafted by the third partner and, on the catalogue's own
qualified word, without a lawyer**: "He helped mediate between the two Steves and drafted this
original partnership agreement (apparently cobbled together using prior examples to save the expense
of a lawyer)", with Wayne described as "a 41-year-old product designer he had met at Atari" who "had
prior experience founding a company". — Date: 1976-04-01 (claimed) — Source: Christie's lot essay —
Source date: 2026-01-23 — URL: as C-27 — Archived: as C-27 — Tier: 3 — Class: **RETROSPECTIVE
INTERPRETATION** (the essay cites no document for any of it; "apparently" is the cataloguer's own
hedge) — Passage: "drafted this original partnership agreement (apparently cobbled together using
prior examples to save the expense of a lawyer)" — Conf: Low — Corroboration: 0 — Conflicts: None.
Legal-posture relevance, kept inside its evidence: if the instrument was self-drafted from precedents,
the partnership was formed **outside any professional counsel**, which is consistent with (i) the
absence of any filed formation record, and (ii) the two-amendment-in-eleven-days pattern. That is a
mechanism statement about how the paper came to exist, not a claim about the founders'
sophistication; the "no lawyer" fact itself is unproven.

C-31 Claim: **The custody chain of the only surviving 1976 paper is public and has a second, earlier
auction event: "Provenance: Ronald G. Wayne (b.1934) sold via University Archives / anonymous owner;
sold at Sotheby's New York, 13 December 2011, lot 241 / acquired by the current owner at that
auction."** Christie's sale 24256 realised **USD 2,515,000** (page fields `price_realised:2515000.0`)
against `estimate_low:2000000.0 / estimate_high:4000000.0`, on sale date **2026-01-23**. — Date:
1976-04-01 (object); 2011-12-13 (first sale); 2026-01-23 (second sale) — Source: Christie's lot 242
description and machine-readable sale fields — Source date: 2026-01-23 — URL: as C-27 — Archived:
as C-27 — Tier: 3 (commercial registry of a Tier-1 object) — Class: FACT (the catalogue's own
stated data) — Passage: "sold at Sotheby's New York, 13 December 2011, lot 241" — Conf: Medium-High —
Corroboration: the $2,515,000 and 2026-01-23 now rest on the auction house's own page **and** on
AP-20's two secondary reports, but all three trace to one sale event (§3) — Conflicts: None.
**RESEARCH DEBT (§10), assigned:** Sotheby's New York lot 241 (2011-12-13) is a *separate* catalogue
produced fifteen years before the Christie's one, from the same object, and is the most likely place
to find transcribed clauses and images of both instruments. Route named, **not tried within this
pass's budget** (see `## Web budget and unanswered requests`), which is a gap and not a null.

C-32 Claim: **The same catalogue essay restates the Byte Shop transaction as documented fact —
"Terrell agreed to buy 50 Apple-1 computers for $500 each—but only if they were fully assembled, not
just kits" — and adds a working-capital figure that matches no other account: "a $5,000 loan secured
by selling Jobs's VW van and Wozniak's HP calculator", with the boards "hand-build[en] … in Jobs's
family garage (or his sister's bedroom—accounts vary)" and the machines retailing at "$666.66 … in
July of 1976".** — Date: 1976 (claimed events) — Source: Christie's lot essay — Source date:
2026-01-23 — URL: as C-27 — Archived: as C-27 — Tier: 3 — Class: **RETROSPECTIVE INTERPRETATION**,
and in the catalogue's own words a contested one ("accounts vary") — Passage: "Terrell agreed to buy
50 Apple-1 computers for $500 each—but only if they were fully assembled, not just kits." — Conf:
Low — Corroboration: **0 documents** — this is a 2026 restatement of the same memoir lineage the
probe found unsupported in 1976-77 print (AP-16, AP-29, U-AP-2). Conflicts: U-C-2, U-C-3. The
significance for this dossier is precisely negative: **the most authoritative-seeming public
custodian of Apple's founding paper states the first order's numbers without citing a document for
them**, so the "50 at $500" canon is still unsupported by any instrument after the deepest pass of
this project's Apple corpus, and its newest carrier is a lot essay written to sell the other three
pages.

C-33 Claim: **The catalogue independently fixes the corporate transition in month-terms — "His
investment helped Apple transition from a partnership of two into a formal corporation. In January
1977, Apple was officially incorporated" — and names Markkula as "the company's third co-founder".**
— Date: 1977-01 — Source: Christie's lot essay — Source date: 2026-01-23 — URL: as C-27 — Archived:
as C-27 — Tier: 3 — Class: RETROSPECTIVE INTERPRETATION — Passage: "In January 1977, Apple was
officially incorporated" — Conf: Medium (the month, because two earlier Tier-1 carriers give it:
AP-04's exact date and AP-19's 1981 "incorporated in 1977") · Low ("third co-founder" is an
interpretation with no documentary standing) — Corroboration: **not counted as a third witness** —
this sentence descends from the same popular-history lineage as the 10-K's date, not from a separate
record, so under §3 it adds nothing to AP-04/AP-19. Recorded to stop a later pass counting three
carriers as three sources. What it *does* add: a 2026 Americana specialist's firm statement that the
**partnership became the corporation by conversion, with the two remaining partners as the
converting parties** — a succession hypothesis matching C-22's blank.

C-34 Claim: **The place of formation, per the lot's own bibliographic line, is Mountain View — the
first bracketed place attached to the 1976-04-01 instrument anywhere in this project's record, and it
is not Los Altos.** The essay states the signing occurred "in Wayne's apartment in Mountain View" on
"Thursday, April 1st, 1976", and identifies Terrell's Byte Shop as "in Mountain View". — Date:
1976-04-01 — Source: Christie's lot 242 — Source date: 2026-01-23 — URL: as C-27 — Archived: as C-27
— Tier: 3 — Class: FACT (the catalogue states it) / **RETROSPECTIVE INTERPRETATION** (that the
document *says* Mountain View — the cataloguer's brackets signal an inference from the address
inside, which this pass has not seen) — Passage: "Typed document signed … [Mountain View,
California] 1 April 1976" — Conf: Medium — Corroboration: 1 — Conflicts: U-C-1. Combined effect on
the register's "1976-04-01, **Los Altos**" cell: Los Altos survives in this dossier only as the
*home* claimed by memoir (AP U-AP-1), never as a documentary place of formation; the 1977 address of
record is Cupertino (C-15); and the only 1976 places that appear in dated documents are **Mountain
View** (this catalogue) and **WESCON, Los Angeles** (C-25, an event not a premises).

### 8 · Registered intellectual property as entity evidence

C-35 Claim: **The earliest US patent application naming Apple as assignee is dated 1977-04-11 and is
filed by the corporation, not the partnership — i.e. the corporation appears as a property owner
three months after incorporation and the 1976 partnership appears as an IP owner not at all.**
Register results (assignee "Apple Computer", publications before 1982), inventor / priority = filing
date / grant: **US4136359A "Microcomputer for use with video display", Stephen G. Wozniak, filed
1977-04-11, granted 1979-01-23**; US4130862A "DC Power supply", Frederick R. Holt, filed 1978-02-01,
granted 1978-12-19; US4210959A "Controller for magnetic disc, recorder, or the like", Stephen G.
Wozniak, filed 1978-05-10, granted 1980-07-01; US4278972A "Digitally-controlled color signal
generation means", Stephen G. Wozniak, priority 1978-05-26, filed 1980-01-08, granted 1981-07-14;
USD268584S "Personal computer" (design), Steven P. Jobs, filed 1980-11-03, granted 1983-04-12. Two
returned records (US3699439A, US4055726A, John A. Turner / Automatic Radio Mfg Co) are **search
artifacts of the text query and are excluded**. — Date: 1977-04-11 (earliest Apple-assigned filing) —
Source: USPTO patent record as served by Google Patents search (aggregator of the register) — Source
date: retrieved 2026-09-24 — URL: https://patents.google.com/xhr/query?url=q%3D%22Apple%20Computer%22%20%26assignee%3DApple%20Computer%26before%3D19820101
— Archived: response held in this session only; **no local copy written** (see Provenance note P-3) —
Tier: 2 aggregator displaying Tier-1 register data — Class: FACT (dates, inventors, assignees as
returned) / INFERENCE (that the absence of a pre-1977 filing means the partnership filed nothing) —
Passage: "Microcomputer for use with video display … 1977-04-11 … Apple Computer, Inc." — Conf:
Medium-High — Corroboration: 1 register route, not exhaustive: the query returned 18 records in 2
pages and **page 2 was not read** (C-39) — Conflicts: None. Firewall note: the Apple-1 was never
patented, and this dossier draws **no** inference that the choice not to file was wise or foolish;
the finding is the legal fact that the partnership's product was unregistered while the
corporation's was.

C-36 Claim: **A named non-founder assigned work to the corporation by February 1978: Frederick R.
Holt is the inventor of record on US4130862A, assigned to Apple Computer, Inc., filed 1978-02-01** —
one of only three inventor names the register attaches to Apple before 1979, and the only one that is
neither Jobs nor Wozniak in that set. — Date: 1978-02-01 — Source: as C-35 — Source date: retrieved
2026-09-24 — URL: as C-35 — Archived: as C-35 — Tier: 2 (register via aggregator) — Class: FACT (the
record) / **INFERENCE** (that a written employment or assignment relationship existed, since an
assignment to a company by a non-founder requires one) — Passage: "DC Power supply … Frederick R.
Holt … Apple Computer, Inc." — Conf: Medium — Corroboration: 1 — Conflicts: None. Value and limit:
this is the **earliest dated public document naming any individual in a property relationship with
Apple other than its founders**, and it therefore does more for the first-employees gap (C-14) than
any retrospective "employee #n" numbering does — but it does not say Holt was an employee, when he
started, or what he was paid, and no payroll document was located anywhere in this project's Apple
corpus.

### 9 · The "Apple" name conflict with the record company

C-37 Claim: **Federal court records show the two Apple entities as opposing litigants, but the
earliest such docket this pass could reach was filed in 2003 — no docket, newsletter, advertisement
or filing from 1975-11 to 1981-02 evidences any objection to the computer company's use of the
name.** CourtListener's RECAP search for `"Apple Corps" "Apple Computer"` returns 24 records, the
earliest matching case being **Apple Computer, Inc. v. Apple Corps Limited, US District Court, N.D.
California, docket 5:03-cv-04560, filed 2003-10-08**; the parallel search for `"Apple Computer"
"Ronald Wayne"` returned only modern dockets (Escapex IP v. Google 2022; Robinson v. Apple 2025; and
similar), i.e. **no 1980 Wayne docket is in RECAP**. — Date: 2003-10-08 (the docket) — Source:
CourtListener v4 search API — Source date: retrieved 2026-09-24 — URL:
https://www.courtlistener.com/api/rest/v4/search/?type=r&q=%22Apple%20Corps%22%20%22Apple%20Computer%22
— Archived: response held in this session only (see Provenance note P-3) — Tier: 1 (court-record
index) — Class: FACT (the docket exists, and is post-window) — Passage: "Apple Computer, Inc. v.
Apple Corps Limited … 5:03-cv-04560 … 2003-10-08" — Conf: High (as to what the index holds) —
Corroboration: 1 index — Conflicts: None. **Time audit (§6):** this record is admitted *only* to
date the earliest reachable court event and to state that Stage 1 is empty of the dispute; it is not
evidence about 1976, and the fact that the 2003 action was brought **by the computer company** is
not read backwards as an earlier posture.

C-38 Claim: **The commonly stated origin of the record-company dispute — that Apple Corps objected
in 1978 or 1979 and that the two later settled over the name — is not supported by any document this
pass reached, and is recorded as UNVERIFIED, not as accepted and not as disproved.** The local corpus
cannot see the period at all (no BYTE issue between 1977-08 and 1980-11; C-17), the trademark register
was not reached (no application or registration number for the "APPLE" mark held by Apple Computer,
Inc. was obtained; the only in-window mark evidence is third-party advertising copy asserting
registration by 1980-12, C-16), and no pre-1990 docket surfaced in RECAP. — Date: 1977-08 → 1980-11
— Source: documented absence across the cached corpus plus the two register routes recorded as
unanswered in `## Web budget` — Source date: 2026-09-24 — URL: n/a — Archived: n/a — Tier: n/a —
Class: **UNKNOWN** — Passage: NO_VERBATIM_PASSAGE_RECORDED (negative finding) — Conf: High (that this
pass holds nothing) · UNKNOWN (whether a 1978-79 action existed) — Corroboration: 0 — Conflicts:
None. Named routes, **untried within budget**, that could settle it in one request each: (i) USPTO
TSDR for the earliest "APPLE" application by Apple Computer Inc (needs a serial or registration
number, obtainable from a TESS-class search this environment cannot drive); (ii) the 1991 settlement
agreement, which was filed under seal and later made public in the 2000s Apple Corps/Apple Computer
litigation and would recite the first assertion's date; (iii) **Kilobaud, Creative Computing and
InfoWorld 1978-79**, unmined in this project (AP-34), the likeliest contemporaneous print carriers.

### 10 · Registry and filing routes: request-by-request outcomes

C-39 Claim: **No charter, statement of information or incorporation-time registry document for Apple
Computer, Inc. was obtained by this pass; the routes were tried and each failed in a specific,
reportable way**, and one returned-page count in this dossier's own query was lost to a
parameter error of this pass. — Date: 2026-09-24 — Source: this pass's HTTP log, reproduced in
`## Web budget and unanswered requests` — Source date: 2026-09-24 — URL: n/a — Archived: n/a — Tier:
1 routes — Class: FACT (about the retrieval attempts, not about Apple) — Passage:
NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 — Conflicts: None. Specifically:
**California SoS** `bizfileonline.sos.ca.gov/api/BusinessSearch` returned **HTTP 200 but an
Imperva/Incapsula JavaScript challenge body (212 bytes, `noindex,nofollow`)** — the endpoint is alive,
the query is not answered, and AP-36's "endpoint alive, unexercised" now has its reason;
**OpenCorporates** v0.4 API returned **HTTP 401 "Invalid Api Token"**; **EDGAR** `browse-edgar`
company search returned **HTTP 503 "SEC.gov | File Unavailable"** and was *not* retried because the
question it would settle (is there a pre-1994 Apple registration statement in the electronic index?)
is **already answered from the locally archived 1,249-row submissions file** (AP-02, AP-21); the
**Internet Archive** full-text search for an Apple prospectus / registration statement / "initial
public offering" returned **6 items, none an Apple financial document**; and the Google Patents
query's **second result page returned an empty cluster because this pass passed `page=2` where the
endpoint is zero-indexed** — an 8-of-18-record remainder that is this dossier's own defect, logged
so a later pass reads page 1 (index 1) rather than concluding the set was complete.

---

## Web budget and unanswered requests

Twelve permitted; **thirteen attempts made, of which six produced substantive evidence and seven are
reported as failures, half-answers or my own parameter errors — the overrun is two attempts on failed
calls and it is recorded here rather than hidden.** Every row states the status code actually
received; none is written as "searched and empty" unless it was answered as empty.

| # | Request (endpoint / query) | Status received | What it bought | Verdict |
|---|---|---|---|---|
| 1 | `bizfileonline.sos.ca.gov/api/BusinessSearch?keyword=APPLE COMPUTER` | **HTTP 200**, 212 B Incapsula JS challenge, `noindex,nofollow` | Nothing; proved the "alive" endpoint of AP-36 is bot-gated | **UNANSWERED** |
| 2 | `api.opencorporates.com/v0.4/companies/search?q=apple computer&jurisdiction_code=us_ca` | **HTTP 401** `Invalid Api Token` | Nothing | **UNANSWERED** |
| 3 | CourtListener `type=r&q="Apple Computer" "Ronald Wayne"` | **HTTP 200**, 10 hits | All post-2008, none the 1980 Wayne matter | **ANSWERED — documented negative** (no Wayne docket in RECAP) |
| 4 | CourtListener `type=r&q="Apple Corps" "Apple Computer"` | **HTTP 200**, 24 hits | Earliest case `Apple Computer, Inc. v. Apple Corps Limited`, N.D. Cal., 5:03-cv-04560, filed 2003-10-08 | **ANSWERED** (C-37) |
| 5 | Google Patents XHR `assignee=Apple Computer & before=19820101` | **HTTP 200**, 18 total, page 0 read | Five Apple-assigned records with filing/grant dates and inventors (C-35/36) + two search artifacts excluded | **ANSWERED (partial)** |
| 6 | Internet Archive `advancedsearch` — Apple prospectus / IPO / registration statement | **HTTP 200**, 6 hits | None an Apple financial document | **ANSWERED — documented negative** |
| 7 | Google Patents XHR, page 2 | **HTTP 200**, empty cluster (`num_page:2`, out of range) | Nothing — my parameter error; endpoint is zero-indexed | **UNANSWERED, self-inflicted** (C-39) |
| 8 | EDGAR `cgi-bin/browse-edgar?action=getcompany&company=apple+computer&type=S-1&output=atom` | **HTTP 503** "File Unavailable" | Nothing; not retried because AP-02's archived index already settles the pre-1994 absence | **UNANSWERED** |
| 9 | WebSearch `"Christie's lot Apple Computer Company partnership agreement April 1 1976 Jobs Wozniak Wayne text clauses"` | gateway error `API Error 2001` | No query reached an index | **UNANSWERED (tool failure)** |
| 10 | WebSearch `"Apple Corps v Apple Computer trademark dispute 1978 first claim …"` | gateway error `API Error 2001` | ditto | **UNANSWERED (tool failure)** |
| 11 | WebSearch (short retry) `Christie's Apple 1976 partnership agreement lot Wayne withdrawal` | **success** | The Christie's lot URL and three secondary carriers | **ANSWERED** |
| 12 | WebFetch `https://www.christies.com/en/lot/…6570347/` | `fetch failed` (no HTTP status surfaced) | Nothing | **UNANSWERED** |
| 13 | curl `web.archive.org/web/2026id_/https://www.christies.com/en/lot/…6570347/` | **HTTP 200**, 122,082 B | The complete lot record: both 1976 instruments, three signatures, Mountain View, the duty allocation, the eleven-day withdrawal at $800, the provenance chain to Sotheby's 2011 lot 241, estimate $2–4M, realised $2,515,000 — **the highest-yield single request of this dossier** | **ANSWERED** |

**Not attempted at all, and named so the next agent does not read them as exhausted:** Sotheby's 2011
lot 241 catalogue; the Utah corporations index (no request spent — the brief's Utah question is
answered only in the negative by C-26, from Apple's own `STATE OF INCORPORATION: CA` field); USPTO
TSDR for the "APPLE" mark; Santa Clara County assessor/recorder (AP-36 recorded 403/000); Verisign
RDAP (no claim in this dossier needed a domain date, so it was correctly **not** spent on); SEC
Public Reference Room / National Archives request for the paper 1980 registration statement.

---

## Timeline

Corporate/legal events only; product and market events live in the A and A2 dossiers. Sources:
`C-nn` records of this file, `AP-nn` / `A2-nn` as marked.

| Date | Event | Class | Conf | Ref |
|---|---|---|---|---|
| 1971 | "Jobs and Wozniak met in 1971 through a mutual friend, Bill Fernandez" — catalogue narrative, no document | RETROSPECTIVE INTERPRETATION | Low | C-32 context |
| 1975-03-05 | "Wozniak attended the first meeting of the famous Homebrew Computer Club in a garage in Menlo Park" — catalogue claim; the cached club corpus begins 1975-11-30 and cannot verify it | RETROSPECTIVE INTERPRETATION (unverifiable locally) | Low | C-32 context |
| 1975 (late) | Apple I designed — Wozniak's own contemporaneous print claim | FOUNDER CLAIM (contemporaneous) | High as a claim | AP-16 / A2-25 |
| 1976-03 (catalogue) | Jobs "enlisted" Ron Wayne, "a 41-year-old product designer he had met at Atari", who "drafted this original partnership agreement" | RETROSPECTIVE INTERPRETATION | Low | C-30 |
| **1976-04-01** | **Three-page typed Apple Computer Company partnership agreement signed by Stephen G. Wozniak, steven p jobs and Ronald Wayne at [Mountain View], California; duties recorded: Wayne "Mechanical Engineering and Documentation", Wozniak "Electrical Engineering", Jobs "Electrical Engineering and Marketing"; Wayne 10%, balance split between the other two** | FACT (catalogue of a dated primary) | High that it exists and is so signed; Medium for the percentages and duties | C-27, C-29, C-34 |
| **1976-04-12** | **One-page "Amendment letter" signed by all three, 11 days after formation — the document that sits under Wayne's withdrawal "in exchange for $800"** | FACT (dated instrument) + FOUNDER CLAIM (consideration) | High (existence/date) · Low ($800) | C-28 |
| 1976-04-30 | Homebrew Newsletter Vol 2 No 4 prints a northern club's letter naming "an APPLE" and thanking "STEVE WOZNIAK for providing transportation" | CONTEMPORARY OBSERVATION | High | AP-24, **C-24** (provenance of that passage) |
| 1976-06-24 / 1976 (all year) | **No Apple-assigned patent application and no Apple trademark or registration notice appears anywhere in 1976 print** — the partnership registered nothing it is known to have | FACT (documented absence) / INFERENCE | Medium-High | C-16, C-35, C-17 |
| 1976-09-15 / 1976-12 | "Apple Computers" listed among Faire commitments; Helmers names "Steven Jobs (Apple Computer Co)" — the entity exists in trade print only as a trading style | CONTEMPORARY OBSERVATION | High | C-04, C-25 |
| 1976-12-10 → 1977-01-19 | Homebrew's two issues across the incorporation are silent on Apple (0 body hits) | FACT (counted absence) | High for these documents | C-20 |
| **1977-01-03** | **Apple Computer, Inc. incorporated under the laws of the State of California** — registrant's own sentence; "incorporated in 1977" independently in 1981 print | FACT | High | C-01, AP-04, AP-19 |
| 1977-04-11 | **Earliest patent application naming Apple Computer, Inc. as assignee** (US4136359A, Wozniak; granted 1979-01-23) — the corporation is a property owner within ~3 months of incorporation | FACT (register) | Medium-High | C-35 |
| 1977-05 → 1977-07 | Wozniak still signs "Apple Computer Co" (May); Apple's own June and July advertisements are the first corporate-styled self-identification, "Apple Computer Inc., 20863 Stevens Creek Blvd., B3-C, Cupertino", phone (408) 996-1010 | FACT | High | C-05, C-15 |
| 1978-02-01 | Frederick R. Holt files US4130862A assigning it to Apple Computer, Inc. — earliest dated record of a non-founder's assigned work | FACT / INFERENCE (relationship) | Medium | C-36 |
| 1979 (cited) | A third party's dated bibliography cites a December 1979 Apple publication as "Cupertino CA: Apple Computer Co" — the partnership-era name still in circulation two years after incorporation | CONTEMPORARY OBSERVATION | High | C-06 |
| 1980-11-03 | Steven P. Jobs files design patent USD268584S "Personal computer" (granted 1983-04-12) | FACT (register) | Medium-High | C-35 |
| 1980-12 (early) | 4.6M shares at $22, 8% of 52.4M, on sale; Apple's own advertisement now gives **10260 Bandley Drive, Cupertino** and an 800 number | FACT (as printed) | High | C-08, C-15, AP-18 |
| 1981-02 | Printed cap table: Jobs 8.3M, Wozniak 8.3M, **A. C. Markkula 8.3M**, Venrock 3.8M, Xerox 80,000; "Apple, incorporated in 1977"; 47 advertisement lines carrying trademark notices naming Apple, several in the wrong corporate form | CONTEMPORARY OBSERVATION / DERIVED | Medium-High | C-08, C-11, C-12, C-16 |
| 2003-10-08 | *Apple Computer, Inc. v. Apple Corps Limited*, N.D. Cal. 5:03-cv-04560 — earliest court record reaching the two firms' name conflict; **post-window, admitted only as the register's outer date** | FACT (docket) | High | C-37 |
| 2011-12-13 | Sotheby's New York lot 241 sells the 1976 instruments — the first public auction of the founding paper | FACT (catalogue) | Medium-High | C-31 |
| 2026-01-23 | Christie's sale 24256 lot 242: the four pages realised **USD 2,515,000** against a $2–4M estimate | FACT (catalogue fields) | High | C-27, C-31 |

---

## Data gaps

Each row states the route that could close it and who should walk it; §10 treats an unassigned
High-importance gap as an open debt, so every High row carries a follow-up task.

| Gap | Why missing | Importance | Best available evidence | Follow-up task |
|---|---|---|---|---|
| **Text of the 1976-04-01 agreement and the 1976-04-12 amendment letter** — capital contributions, dissolution and dispute clauses, whose address appears in the instrument | Held by a private buyer since 2026-01-23; never digitised by the auction house beyond the description read here | **HIGH** — the whole of §1 and §5 of this dossier | C-27/C-28/C-29 (catalogue's physical description + two quoted duty strings) | **GD-C1:** pull the **Sotheby's New York 2011-12-13 lot 241** catalogue entry (older, often fuller, independent of the 2026 essay) and any lot images; then the 1976 object's own letterhead via the Christie's specialist contact named on the lot page |
| **Original 1977 Articles of Incorporation and the first statement of information — who signed as incorporators, and the authorised share capital** | California SoS API is bot-gated (200 + JS challenge); no charter mirror reached | **HIGH** — closes the entity sequence and C-13's officer blank | C-01 (registrant date), AP-06 (the 10-K itself names the California SoS as the charter registry) | **GD-C2:** a records route that is not an API — SoS requested-copy form, a county-law-library microfilm hold, or the charter facsimile in a 1980s printed exhibit; note AP-36's earlier 200-on-the-endpoint probe |
| **The first officers of Apple Computer, Inc.** | No corporate document and no press statement in any retrieved source attaches an office to a name (C-13) | **HIGH** — §B/§N governance reconstruction | C-29 (functional duties in the partnership instrument); C-08 (1981 holdings, no offices) | **GD-C3:** the 1980 prospectus' "Management" table (paper route below) or the 1977 statement of information |
| **The 1980 registration statement / prospectus itself** | EDGAR's floor is 1994-01-26 (AP-02, AP-21); the paper document is not online; the Internet Archive prospectus query returned nothing relevant (C-39) | **HIGH** — the only plausible carrier of FY1976-77 accounts, the Markkula terms and the first-auditor identity | C-08/C-11/C-12 (a 1981 restatement of some of its contents, by an unnamed columnist) | **GD-C4:** SEC Public Reference Room / National Archives interfile request for Apple Computer, Inc.'s 1980 Form S-1 (state cost and latency); in parallel, test research-library and auction holdings for a prospectus facsimile |
| **Ronald Wayne's 1980 exit and any litigation attached to it** | Absent from the cached corpus entirely (C-21) and absent from RECAP for pre-1990 federal records (C-37) | **HIGH** — §Termination and the liability posture of the superseded partnership | C-28 (the dated amendment letter + the $800 in retrospective prose); AP-20/29 | **GD-C5:** N.D. Cal. / Santa Clara County Superior paper indices for 1980, and any published denial/settlement order; a case search by party name in a legal publisher, not a general web search |
| **Whether Apple Corps objected to the "Apple" name during 1976-79, and when** | The corpus is blind to 1977-08 → 1980-11 and the trademark register was not reached (C-17, C-38) | **HIGH** for the legal section; **MEDIUM** for Stage 1 as bounded (any 1978 action is outside the 1977-01-03 end date) | C-16 (mark notices by 1980-12), C-37 (2003 docket as the outer date) | **GD-C6:** USPTO TSDR for the earliest "APPLE" filing by Apple Computer Inc. (a serial/registration number is the blocker — obtain it from a TESS-class search or a register-derived index); mine **Creative Computing / InfoWorld / Kilobaud 1978-79** (AP-34: Kilobaud needs OCR first) |
| **Apple's FY1976 and FY1977 revenue; the first audited accounts** | No contemporaneous figure in any text found (AP-35) and no FY1976-77 column reached in this pass | **HIGH** — the "repeatable validation" rung | C-08's FY1978–80 series, printed 1981-02 | **GD-C7:** the paper prospectus' selected-financial-data table; failing that, a period IPO story in InfoWorld or The Wall Street Journal via a library database |
| **Any contract with a dealer, distributor or jobber; the Byte Shop's terms** | No invoice, cheque or agreement digitised anywhere in this project's Apple corpus | **HIGH** — first-customer and liability reconstruction | C-32 (a 2026 catalogue restating "50 at $500" without a document), AP-12/AP-14 (dealer stock in print), AP-30 (Terrell's 1976 Polaroids) | **GD-C8:** the Terrell photographic set at higher resolution, and a search for a 1976 seller's document in museum or sale holdings |
| Premises: who held the Cupertino lease at 20863 Stevens Creek Blvd B3-C, and when; the Crist Drive property's ownership | County assessor/recorder endpoints unreachable (AP-36: 403 / 000); no lease in any corpus | MED-HIGH | C-15 (the printed address sequence 1977 → 1980) | **GD-C9:** Santa Clara County recorder paper/microfilm indices; a records request rather than a portal query |
| Authorship and sourcing of the February 1981 IPO column that carries the only printed cap table | The column is unsigned in the OCR and this pass did not resolve its masthead attribution | MED — it is the root of every ownership figure in §2 | C-08 (the text), AP-18 | **GD-C10:** read BYTE Feb 1981's column masthead and editor credit (the file is on disk at `ia_byte_1981/byte-1981-02.txt`) and record who signed the department |
| The Google Patents result page 2 (8 of 18 pre-1982 records) | This pass's own parameter error (C-39) | MED | C-35's five Apple-assigned records | **GD-C11:** re-run with `page=1` (zero-indexed); also re-run with `assignee="Apple Computer Company"` to catch a partnership-era string |
| Whether a Utah (or other state) registration was used by the 1976-77 firm | Never tried beyond the negative at C-26; no Utah index queried | MED (the brief asks; no answer exists in this pass's set) | C-26 (`STATE OF INCORPORATION: CA`; no Utah string anywhere) | **GD-C12:** Utah Division of Corporations public index search for "Apple Computer" historical filings, with the request counted, not assumed |

---

## Contradictions

Format per §7: CLAIM A / CLAIM B / WHY THEY DIFFER / EVIDENCE WEIGHT / BEST-SUPPORTED
INTERPRETATION / RESIDUAL UNCERTAINTY / CONFIDENCE. None is reconciled by fiat; each is carried
forward for the merge.

U-C-1 **Where and when Apple began, and which beginning is the company's.**
CLAIM A: a partnership agreement signed **1 April 1976** by three named men at **[Mountain View],
California**, in Wayne's apartment per the catalogue (C-27, C-34). CLAIM B: **Apple Computer, Inc.
"was incorporated under the laws of the State of California on January 3, 1977"** — the registrant's
own sentence (C-01). CLAIM C: the universe feasibility register and general reference give
"1976-04-01, **Los Altos**, California" as the founding, and every popular account locates the
enterprise in a Los Altos garage. WHY THEY DIFFER: three distinct things — a private contract, a
public charter, and a family address — collapsed into one word. "Los Altos" is a *residence* claim
(Jobs's parents' house) attached to a *formation* event; the only 1976 place inside a dated document
described by this pass is Mountain View, and the first address the company itself published is
Cupertino (C-15). EVIDENCE WEIGHT: A and B are primary instruments or registrant text; C is
derivative, and the phrase "garage operation" appears in the retrieved record only in **1981 print**
(C-11) and in a 2026 lot essay that itself hedges, "Jobs's family garage (or his sister's bedroom —
accounts vary)" (C-32). BEST-SUPPORTED INTERPRETATION: formed as an unincorporated partnership at
Mountain View on 1976-04-01; converted to a California corporation on 1977-01-03; address of record
Cupertino from 1977-05; **no retrieved document places the firm's business at Los Altos, and the
residence claim should be reported as a residence claim.** RESIDUAL UNCERTAINTY: whether the
instrument's own letterhead says Mountain View (the cataloguer's brackets suggest his inference, not
the document's); whether the conversion was a legal continuation, an asset transfer or simply a new
entity (C-22 — no document either way). CONFIDENCE: High on both dates; Medium on place; **UNKNOWN
on succession mechanics.**

U-C-2 **Wayne's share and the length of his stay.**
CLAIM A: **10%** and **eleven days** — the catalogue states "Wayne received a 10% stake and the
remainder was split evenly", and its own two dates (1 April, 12 April) make the interval eleven days
(C-28). CLAIM B: the circulating canon of **12%** and **"12 days"** (AP-20's retellings, including
2024-26 press). WHY THEY DIFFER: 45/45/10 exhausts 100, so 12% cannot coexist with the equal split of
the remainder; the day-count is a rounding of a dated document upward to a memorable number.
EVIDENCE WEIGHT: A rests on the object's cataloguer reading the object, plus the arithmetic of two
dates on the lot line; B rests on no document and is refuted arithmetically by the split A itself.
BEST-SUPPORTED INTERPRETATION: **10%, withdrawn 11 days after formation, on a 1976-04-12 amendment
signed by all three.** RESIDUAL UNCERTAINTY: whether the 12 April amendment is Wayne's exit or some
other change — the catalogue calls it "Amendment letter to the above" without saying what it
amends; the essay's $800 is unsourced and AP-20 records a further $1,500 not present in the lot text.
CONFIDENCE: Medium-High on 10%; High that 12% is unsupported by any document; Low on consideration.

U-C-3 **What the first working capital was, and what it was for.**
CLAIM A: **$1,000** raised by selling an HP-65 calculator for $500 and a VW bus for $750 — iWoz
lineage (AP-32), for **board printing**. CLAIM B: a **$15,000 loan** (Wayne, AP-29), for **filling the
Byte Shop order**. CLAIM C: **"a $5,000 loan secured by selling Jobs's VW van and Wozniak's HP
calculator"** (Christie's lot essay, C-32), fusing A's objects with B's mechanism. WHY THEY DIFFER:
three tellings of one memory, each fitted to a different purpose, the newest of which merges the two
older ones — the classic signature of a story being tidied rather than sourced. EVIDENCE WEIGHT:
**zero documents in any of the three**; A is a single 2006 autobiography copied widely (independence
rule: one source), B is one partner's retrospective memory, C is an auction house's unattributed
essay and cannot be an independent witness to any of them. BEST-SUPPORTED INTERPRETATION:
**UNKNOWN — no amount is establishable.** The only defensible statement is that the enterprise needed
some cash to buy parts and that no bank or investor paper for it has surfaced. RESIDUAL UNCERTAINTY:
complete. CONFIDENCE: Low on all three; High that none is corroborated.

U-C-4 **Was there a first order, and on what terms?**
CLAIM A: the canon — Paul Terrell's Byte Shop ordered **50 Apple-1s at $500 each** in July 1976,
"fully assembled", restated as fact by the 2026 catalogue (C-32). CLAIM B: the documentary record —
Wozniak, writing in **May 1977**, says the Apple-I was sold "by word of mouth throughout California
and later nationwide through retail computer stores" and names **no order** (AP-16); Wayne says "a
large number" without a figure (AP-29); 1976 print proves only that independent dealers stocked the
board (AP-12/AP-14, A2-08); and **no price for the Apple-1 was printed in 1976 print at all**
(A2-23). WHY THEY DIFFER: A is preserved by memoir and now by a commercial catalogue with a
financial interest in the object; B is the surviving contemporaneous text, which is about the market
and not about the transaction. EVIDENCE WEIGHT: A has no document; B has dated print and is silent
precisely where A is specific. BEST-SUPPORTED INTERPRETATION: **an early wholesale relationship with
Terrell is very likely** (the two men appear as peers in December 1976 print; Terrell kept 1976
Polaroids of the founders showing him the machine) **but the unit count, the price, the date and any
payment are undocumented.** RESIDUAL UNCERTAINTY: high; this is the same conclusion AP-26 reaches at
U-AP-2, reached independently here from the lot essay rather than from the press. CONFIDENCE: Low.

U-C-5 **How solid is the only printed cap table?**
CLAIM A: BYTE February 1981's numbers — 4.6M shares, **8% of 52.4M**, $22, and the holdings at C-08 —
are treated by later accounts as prospectus-derived. CLAIM B: the printed figures do not close their
own arithmetic: 4.6 ÷ 52.4 = **8.78%**, not 8%, so either the share count, the percentage, or the
offer size is rounded or wrong, and the column is unsigned, so its source chain is invisible (C-08,
GD-C10; same defect recorded at A2-50). WHY THEY DIFFER: a secondary restatement of a primary
document reads as primary once it is quoted in print; rounding in a news column is not an error in
the prospectus but cannot be distinguished from one here. EVIDENCE WEIGHT: A is contemporaneous
Tier-1 press reporting a Tier-1 document it does not reproduce; B is arithmetic anyone can do.
BEST-SUPPORTED INTERPRETATION: report the terms **as printed, with the discrepancy stated**, and
resolve nothing until the paper prospectus is read; every derived value in §2 of this dossier is
labelled DERIVED for that reason (C-09). RESIDUAL UNCERTAINTY: the offer's true percentage, the
over-allotment treatment, and whether Markkula's 8.3M is a post-dilution or pre-dilution figure.
CONFIDENCE: Medium that the numbers were printed; Low that they are exact.

U-C-6 **When did the name become contested?**
CLAIM A: a well-attended account places Apple Corps' first objection in **1978**, with a long
sequence of disputes ending in a 1991 agreement. CLAIM B: **nothing in the retrieved record from
1975-11 to 1981-02 contains the dispute at all** (C-17), the earliest court record this pass reached
is a **2003** action *brought by Apple Computer against Apple Corps* (C-37), and the only mark
evidence inside the window is third-party advertising asserting registration by **1980-12** (C-16).
WHY THEY DIFFER: A is downstream legal-history summary; B is silence in a corpus with a structural
hole — the cached magazine run omits 1977-08 through 1980-11 entirely, so the corpus cannot see 1978
even if 1978 is full of it. EVIDENCE WEIGHT: neither side has an instrument here. BEST-SUPPORTED
INTERPRETATION: **UNKNOWN for Stage 1 and for Stage 2 as bounded**; the dossier's honest statement is
that the computer company's name was, in every document this project holds from 1976 to 1981,
*unopposed on the page*, and that this is a property of the corpus as much as of the world.
RESIDUAL UNCERTAINTY: the entire dispute history, and whether any 1976-77 objection was ever made and
settled privately, which would leave no trace at all in these four document families. CONFIDENCE:
Low; the routes to raise it are named at C-38 and GD-C6.

---

## Outbound corrections

For the orchestrator to apply to `A_chronology_feasibility.md` and `A2_periodical_archive_mine.md`.
**None is applied by this pass to either file.**

COR-C-01 → **AP-20 / U-AP-4 / Famous-claims table.** Wayne's stake and interval are now attached to a
dated second instrument: the Christie's lot record describes **two** 1976 documents — the agreement of
1 April and a **one-page "Amendment letter" of 12 April 1976 signed by Wozniak, Jobs and Wayne** — so
the "12%" retellings are unsupported and the "12 days" is a rounding of an eleven-day interval that
the lot's own dates fix. AP-20's "$800 up front plus a later $1,500" is not in the lot text, which
states only $800; keep both legs but stop sourcing them to one event.

COR-C-02 → **AP-20 / U-AP-1 / the universe register's "1976-04-01, Los Altos" cell.** The lot's
bibliographic place is **"[Mountain View, California]"**, with the essay putting the signing in
Wayne's Mountain View apartment. Los Altos is a *residence* claim about Jobs's parents' house and
should not be carried as the place of formation.

COR-C-03 → **AP-05 / "any founding narrative is sourced outside EDGAR".** Correct but now
insufficient: Apple's own FY1994 10-K contains **zero** body occurrences of `Wozniak`, `Wayne` or
`1976` — re-grepped in this pass — so the filing supplies a date and a state and no founding
*vocabulary* whatsoever. Worth stating in the merge so no agent expects a registrant account of
formation to exist digitally.

COR-C-04 → **AP-29 / U-AP-2 / U-AP-3 (the Byte Shop order and the working capital).** A new, and
apparently authoritative, carrier of "50 at $500" now exists (Christie's 2026 lot essay) — as does a
**third** capital figure, "$5,000", which fuses iWoz's sold objects with Wayne's loan mechanism.
Under §3 this is not corroboration: it is the same memoir lineage wearing a catalogue. The Famous
claims table should say that the canon has gained a commercial restatement and **no** document.

COR-C-05 → **AP-26 / A2-06 (the Homebrew 1975-11 → 1976-03 null).** Confirmed, with a new adjacent
null: the club's issues of **1976-12-10 and 1977-01-19 have zero body hits for `apple`** (1 raw hit
each, both the corpus's own provenance header). The incorporation month is therefore un evidenced in
the one in-window primary series that otherwise tracks the firm.

COR-C-06 → **AP-24 / A2-19 (the April 1976 Wozniak reference).** The passage sits under the heading
"NOTES FROM THE NORTH" and is written by, and about the inventory of, the **Sonoma County Micro
Computer Club** at LO*OP Center, Cotati — "We are a group of several ALTAIR* s , an IMSAI, a JOLT,
two PDP-8's, an APPLE". It is dated, first-hand and about Wozniak delivering a machine, but it is not
a Homebrew meeting report; AP-27's caution should be promoted into the citation itself.

COR-C-07 → **AP-13 / A2-14 (name forms, 1976).** Add the legal reading: 1976 print names the firm
only as a trading style ("Apple Computer Co", "Apple Computers"), so **no 1976 document in the corpus
evidences a corporation**, and the "Inc." form first appears in **Apple's own print in June 1977**,
five months after the registrant's incorporation date, while Wozniak's own May 1977 byline still reads
"Apple Computer Co".

COR-C-08 → **AP-18 / A2-49 (the February 1981 IPO column).** The column is **unsigned**; its author and
therefore its source chain are unidentified, and its own arithmetic fails (4.6M of 52.4M is 8.78%,
printed as 8%). Cap every ownership number that rests on it at **Medium** and label the ">$100M worth
of stock" line the magazine's own derived statement (8.3M × $22 = **$182.6M**).

COR-C-09 → **AP-31 (first employees / "employee #6").** There is now a *dated public record* to
prefer over retrospective numbering: **Frederick R. Holt** is inventor on a 1978-02-01 application
assigned to Apple Computer, Inc. (US4130862A). It does not establish employment, start date or
sequence, and "employee #n" claims must not be strengthened by it.

COR-C-10 → **AP-16 / A2-25 (Wozniak's "designed late in 1975").** The Christie's essay attaches a day
to the first working prototype — "On 29 June, he successfully tested his prototype" — citing a
**2025 interview**, and separately dates the Apple-1's retail price at "$666.66 … in July of 1976",
which contradicts Wozniak's own contemporaneous "price under $700 at the retail level" only if the
two are read as the same kind of statement (a manufacturer's sticker versus a published retail
ceiling). Both belong in U-AP-2/U-AP-3 territory as **retrospective**, not as new facts.

COR-C-11 → **method, §14 rule 6 (evidence families).** For Apple, a fifth family is now load-bearing
and should be named: **auction-house lot records**, whose machine-readable fields (estimate, realised
price, sale date, provenance chain) are primary for custody facts and Tier-3 for narrative. This
dossier's only new 1976 documentary content came from that family, and its direct URL could not be
fetched (WebFetch `fetch failed`) — the **archived copy succeeded**, which is the route to record for
other agents.

---

## Sources consulted

Provenance table per §7: `| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |`

| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| Apple Computer, Inc., Form 10-K FY1994, Item 1 (incorporation sentence; state-of-incorporation field; absence of founding vocabulary) | Regulatory filing | Primary | 1977-01-03 | 1994-12-13 | https://www.sec.gov/Archives/edgar/data/320193/000032019394000016/0000320193-94-000016.txt | 1 | High |
| BYTE, December 1976 (Helmers editorial naming Jobs; Faire exhibitor list) | Trade periodical | Primary (contemporaneous observation) | 1976-09 / 1976-12 | 1976-12 | https://archive.org/details/byte-magazine-1976-12 | 1 | High |
| BYTE, November 1976 (dealer advertisement; technical article) | Trade periodical | Primary | 1976-11 | 1976-11 | https://archive.org/details/byte-magazine-1976-11 | 1 | High |
| BYTE, October 1976 (Computer Fan advertisement) | Trade periodical | Primary | 1976-10 | 1976-10 | https://archive.org/details/byte-magazine-1976-10 | 1 | High |
| BYTE, April 1977 (Helmers' 1976-11-20 sighting; Shepardson Microsystems at 20823 Stevens Creek) | Trade periodical | Primary | 1976-11-20 / 1977-04 | 1977-04 | https://archive.org/details/byte-magazine-1977-04 | 1 | High |
| BYTE, May 1977 (Wozniak "System Description: The Apple-II", byline and address) | Trade periodical | Primary — **company-side** | 1977-05 | 1977-05 | https://archive.org/details/byte-magazine-1977-05 | 1 | High |
| BYTE, June and July 1977 (Apple Computer Inc. advertisement, price ladder, mail-order block) | Trade periodical | Primary — **company-side** | 1977-06 / 1977-07 | 1977-06 / 1977-07 | https://archive.org/details/byte-magazine-1977-06 ; …/1977-07 | 1 | High |
| BYTE, December 1980 (Apple advertisement at 10260 Bandley Drive; the trademark-notice corpus) | Trade periodical | Primary | 1980-12 | 1980-12 | https://archive.org/details/byte-magazine-1980-12 | 1 | High |
| BYTE, February 1981, p 212 "Apple Stock Goes On Sale" (unsigned column: terms, revenue series, cap table); article reference list citing "Apple Computer Co, Dec 1979" | Trade periodical | Primary (reporting), **secondary for the numbers it restates** | 1980-12 | 1981-02 | https://archive.org/details/byte-magazine-1981-02 | 1 | Medium-High |
| Homebrew Computer Club newsletters, 1975-11-30 → 1977-01-19 (`hcc0109`…`hcc0213`) incl. the 1976-04-30 "NOTES FROM THE NORTH" letter and the 1976-09-15 Faire list | Grassroots periodical | Primary | 1975-11 → 1977-01 | as dated | https://archive.org/details/hcc0204 ; …/hcc0209 ; …/hcc0211 ; …/hcc0213 | 1 | High |
| **Christie's, Live Auction 24256 "We the People: America at 250", Lot 242 — "The Apple Computer Company Partnership Agreement"** (description: two 1976 instruments, three signatures, Mountain View; essay: 10%, eleven days, $800, duty allocation, provenance to Sotheby's 2011 lot 241; fields: estimate $2–4M, realised $2,515,000, sale 2026-01-23) | Auction catalogue | Primary for the object's custody and physical description; **Tier-3 narrative** for the essay | 1976-04-01 / 1976-04-12 | 2026-01-23 | https://www.christies.com/en/lot/lot-the-apple-computer-company-partnership-agreement-6570347/ (retrieved via an archived copy, 2026-09-24) | 3 (of a 1) | Medium-High (description) · Low (essay) |
| **USPTO patent register via Google Patents search** — US4136359A, US4130862A, US4210959A, US4278972A, USD268584S (assignee "Apple Computer, Inc."; inventors Wozniak, Holt, Jobs) | Patent register (via aggregator) | Primary register data, aggregator-delivered | 1977-04-11 → 1980-11-03 | grants 1978-12-19 → 1983-04-12; retrieved 2026-09-24 | https://patents.google.com/xhr/query?url=q%3D%22Apple%20Computer%22%20%26assignee%3DApple%20Computer%26before%3D19820101 | 2 (of 1) | Medium-High |
| **CourtListener v4 search API** (RECAP) — `Apple Computer, Inc. v. Apple Corps Limited`, N.D. Cal. 5:03-cv-04560, filed 2003-10-08; and the negative Wayne search | Court-record index | Primary index | 2003-10-08 | retrieved 2026-09-24 | https://www.courtlistener.com/api/rest/v4/search/?type=r&q=%22Apple%20Corps%22%20%22Apple%20Computer%22 | 1 | High (as to the index) |
| Apple-1 Registry (A. Baqué), 2022 curation of the 1973 application, Terrell's Polaroids, Wayne's account, Koa cases, iWoz capital story | Curated registry | Secondary, retrospective | 1973 / 1976 | 2022 | https://www.apple1registry.com/en/stories.html | 3 | Low-Medium |
| ITechguides and Hypebeast coverage of the Christie's sale (as held in AP-20) | Web reporting | Secondary | 2026-01-23 | 2025-11-26 / 2026-08-18 | see AP-20 | 2/3 | Medium |
| Failed / unanswered routes: California SoS `bizfileOnline` API (200 + JS challenge), OpenCorporates (401), EDGAR `browse-edgar` (503), direct Christie's fetch (`fetch failed`), Internet Archive prospectus query (6 irrelevant hits), Google Patents page 2 (empty) | Registry and archive endpoints | n/a | n/a | 2026-09-24 | see `## Web budget and unanswered requests` | 1 routes | **UNANSWERED — not nulls** |

**Filing-lineage statement (§3).** One registration lineage is in play and it is **not** Apple's: the
FY1994 Form 10-K is a single registrant document and supplies a single founding fact (C-01/C-02); no
amendment or accession of Apple's own adds a second witness to it, and any later 10-K repeating
"January 3, 1977" is the **same corporate record** and must not be counted as corroboration. The 1980
registration statement, the document that *would* be a second witness to formation, is not in any
electronic lineage this project can reach (AP-02, AP-21, C-39).

---

## Provenance and method notes

**P-1 Nothing outside this file was created, modified, moved or deleted.** `sources/` was read
exclusively; the `_RETRIEVAL_LOG.md`, the `A_…` and `A2_…` dossiers and all `*.csv` registers were
left untouched. This file is the only output of this pass, and the only path it owns.

**P-2 Header exclusion, stated for reproduction.** Counts in this dossier come from
`grep -n -i PATTERN FILE | awk -F: '$2+0>5'` — the corpus's five-line provenance headers carry the
token `apple` in `company_004_apple` and would otherwise inflate every null. The rule and the
resulting per-file numbers are printed in `## Scope and working method`; the same trap is recorded
independently at `A2-05`, and this dossier's C-20 (the silent incorporation month) exists **only**
because the headers were excluded — with them, both January and December 1976 issues would appear to
mention Apple.

**P-3 No local copies were written of anything retrieved externally, and that is a deliberate
limit of this pass, not an oversight.** `sources/` is protected (§14 rule 4) and the Evidence
Registrar is not this agent. The three external payloads that matter — the Christie's lot record
(122,082 B), the Google Patents JSON (17,696 B + 3,405 B) and the CourtListener JSON (45,955 B +
86,471 B) — are therefore **not** in the archive, are quoted here only within the ≤40-word passage
limit, and should be restored by the registrar under the URLs in `## Sources consulted`. Until then
C-27 … C-31 are single-citation records and must not be described as corroborated.

**P-4 Independence accounting for the ownership block.** Everything in §2 rests on **one** unsigned
1981 column; the 2026 catalogue adds narrative, not equity data; the 10-K adds a date, not a cap
table. There is therefore **no independent second witness to any Apple ownership figure in the
period 1976-1981 in this dossier**, and no derived value in C-09 may be presented as observed. This
is the §2 record-selection null in its sharpest local form: what the winners' archive preserved for
Apple's first capital structure is a paragraph in a magazine.

**P-5 What this dossier can and cannot claim to be.** It is a **documentary reconstruction of the
legal shell**, and it is honest about the asymmetry: the *existence* and *dates* of two 1976
instruments and one 1977 charter are now well fixed, while their **contents** — clauses,
consideration, offices, share classes, capital — remain almost entirely unread. The instinct to fill
that interior from memoir is strong here precisely because the frame is solid; it is the failure this
section exists to prevent.

**P-6 Depth verdict contribution (§14 rule 6).** Four families were tried for this dossier:
**filings** (EDGAR — reaches 1994 only, already established), **periodicals** (rich, already mined
by A2), **court and registry records** (partially: one modern docket, three failed registry routes),
and **auction / documentary-sale records** (**the family that produced the only new 1976 evidence in
this pass**). A fifth family — the USPTO registers — produced the earliest dated instrument naming
the corporation as a property owner. Any future depth verdict for Apple should treat auction custody
and the patent register as first-class routes rather than colour, and should stop treating the EDGAR
and web-archive floors as the boundary of what is knowable about a 1976 company.

---

## CSV append rows

Headers copied verbatim from `company_001_amazon/{decisions,sources,conflicts,timeline}.csv`, which
are known-conformant to §13. **Rows only — the CSV files are not this pass's to write.** Every field
containing a comma is double-quoted. Source ids in this dossier's block are **`CS-nn`** (Apple's
`sources.csv` currently runs `A2S-01 … A2S-13`, so this prefix cannot collide), conflict ids are
**`U-C-n`**, claim refs are **`C-nn`**. Reuse, never redefine, an existing id.

### `decisions.csv` — append rows

```
company,stage,date,decision,state_before,information_available,unknowns,alternatives,constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref
Apple,1,1976-04-01,"Form as an unincorporated partnership, three signatories, rather than as a corporation","Wozniak had a working prototype tested in 1975; Jobs and Wozniak were employees of HP and Atari respectively; no company existed","A typed three-page agreement signed 1 April 1976 at [Mountain View] allocating Wayne 10 per cent with the remainder split evenly, and duties as Mechanical Engineering and Documentation / Electrical Engineering / Electrical Engineering and Marketing","Whether a corporation was considered and rejected, and on what advice; whose idea the split was; whether the agreement was drafted by a lawyer - the catalogue's 'apparently cobbled together ... to save the expense of a lawyer' is hedged inference","Continue informally with no instrument at all; engage counsel and incorporate immediately; sell the design rather than the machine","No capital, no counsel on the record, no credit history, no commercial paper of any kind in 1976 print, and two of the three signatories still employed elsewhere","A drafted-from-precedents instrument the partners could sign the same day","A trading partnership able to buy parts and sell boards","Amended within eleven days by a letter signed by all three, which the catalogue links to Wayne's withdrawal. RETROSPECTIVE framing for the motive.",CS-01,"Medium (existence and terms of the instrument) / Low (motive and the no-lawyer point)",C-27; C-28; C-29; C-30; U-C-2
Apple,1,1976-04-12,"Wayne leaves the partnership; the remaining two continue as sole partners against an amendment letter signed by all three","Three-partnership, 45/45/10, eleven days old","One-page 'Amendment letter to the above', typed, signed Wozniak / Jobs / Wayne, dated 12 April 1976, surviving in the same lot as the agreement","The consideration actually paid (catalogue states $800; other reporting adds a later $1,500); whether the letter terminated Wayne or changed something else; whether partnership debts were apportioned","Continuing as three; buying Wayne out later; winding up","Two remaining partners with no cash and a machine to sell","A withdrawal 'wary of the financial risk' is the catalogue's retrospective sentence, not a clause this pass read","A two-person partnership trading through dealers","Eleven days of exposure for the departing partner, and a surviving paper trail of four pages. RETROSPECTIVE framing.",CS-01,"High (the dated instrument exists) / Low (its terms and the money)",C-28; C-22; U-C-1; U-C-2
Apple,1,1977-01-03,"Incorporate in California as Apple Computer, Inc.","Unincorporated partnership of two, trading as 'Apple Computer Co' / 'Apple Computers' through dealers; the maker placed no advertisement of its own in 1976","One registrant sentence: 'incorporated under the laws of the State of California on January 3, 1977'; a 1981 press column independently dating incorporation to 1977","The incorporators' names, authorised capital, share classes and the first officers - no charter text reached","Staying a partnership; incorporating in another state; a Utah filing hypothesis (no document anywhere supports it)","Markkula's involvement is documented only as an 8.3M-share holding and a role, in 1981 print; the terms of his entry are undated","A corporate wrapper is what makes a later share issuance and an outside investor possible","A California corporation, address of record in Cupertino from May-June 1977","The corporation is named as patent assignee from 1977-04-11, three months after incorporation - the earliest dated instrument naming it as a property owner. RETROSPECTIVE outcome.",CS-02; CS-04; CS-05,"High (the fact and date of incorporation) / Low (everything interior to it)",C-01; C-05; C-26; C-35
Apple,1,1977-06,"Advertise as 'Apple Computer Inc.' and publish the corporate name, price and a mail-order address in the trade press","Company present in the market only through independent dealers and third-party print; no maker advertising in 1976","A June 1977 full-page BYTE advertisement plus a reprint in July: $1,298 complete, $598 board-only, 20863 Stevens Creek Blvd Bldg B3-C Cupertino, telephone (408) 996-1010","Whether the move to direct mail order was planned as a channel or a stopgap; the economics behind the two prices","Continuing dealer-only distribution","Wozniak still signed 'Apple Computer Co' one month earlier in the same magazine","Sell the machine as an appliance to non-hobbyists","The maker's own advertised voice begins with the Apple II and the corporate form","The Apple-1 vanishes from the maker's print at the same moment; no discontinuation notice was published anywhere. RETROSPECTIVE framing.",CS-03,"High (the advertisements exist as printed) / Medium (that they mark a deliberate channel change)",C-05; C-19; C-23
```

### `sources.csv` — append rows

```
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
CS-01,1,"The existence, dating, page count, signatories, stated place and amendment of the founding partnership instrument; Wayne's 10 per cent, the eleven-day interval and the $800; the three functional duties; the custody chain to Sotheby's 2011 lot 241 and the 2026 realised price","The Apple Computer Company Partnership Agreement - Christie's Live Auction 24256 'We the People: America at 250', Lot 242","Christie's (specialist Peter Klarnet, Americana)",Auction lot record,Primary for the object and its custody; Secondary (Tier-3) for the lot essay's narrative,1976-04-01,2026-01-23,2026-09-24,https://www.christies.com/en/lot/lot-the-apple-computer-company-partnership-agreement-6570347/,https://web.archive.org/web/2026id_/https://www.christies.com/en/lot/lot-the-apple-computer-company-partnership-agreement-6570347/,3,"FACT (description and sale fields) / RETROSPECTIVE INTERPRETATION (essay)",Medium-High (description) / Low (essay),"Independent of Apple's own filings and of the trade press, but the essay restates the memoir lineage and is NOT a second witness to the Byte Shop order, the $800 or the capital figures; the direct URL failed WebFetch and only the archived copy resolved","Typed document signed (Stephen G. Wozniak, steven p jobs and Ronald Wayne), [Mountain View, California] 1 April 1976. Three pages, letter-sized paper. With: Amendment letter to the above ... 12 April 1976","No local copy written - sources/ is read-only to this pass (Provenance note P-3). Machine-readable fields: estimate_low 2000000, estimate_high 4000000, price_realised 2515000, start_date 2026-01-23T15:00Z. FOLLOW-UP GD-C1: the Sotheby's 2011-12-13 lot 241 entry"
CS-02,1,"The date and jurisdiction of incorporation; the state-of-incorporation field; the complete absence of founding vocabulary in the registrant's own text",Form 10-K for the fiscal year ended 1994-09-30,Apple Computer Inc. (SEC registrant),Regulatory filing,Primary,1977-01-03,1994-12-13,2026-09-24 (this pass re-grepped the locally archived copy),https://www.sec.gov/Archives/edgar/data/320193/000032019394000016/0000320193-94-000016.txt,sources/10-K_FY1994_acc-0000320193-94-000016_filed-1994-12-13.txt (lines 29 and 132-133),1,FACT,High,"Single registrant document; any later 10-K repeating the same sentence is the SAME corporate record under the filing-lineage rule and must not be counted as corroboration. Re-grep here returned zero body hits for Wozniak, Wayne or 1976","Apple Computer, Inc. ('Apple' or the 'Company') was incorporated under the laws of the State of California on January 3, 1977.","Already registered in the A dossier as AP-04/AP-05; CS-02 exists so that this dossier's C-01/C-02/C-26 rows resolve. Do not re-define AP ids"
CS-03,1,"Apple's own first corporate-styled print, the price ladder and the Cupertino address of record; the Bandley Drive address by 1980-12; the third-party trademark-notice corpus; the 1981 IPO terms, revenue series and pre-IPO cap table","BYTE, June and July 1977 (Apple Computer Inc. advertisements); BYTE, December 1980 (Apple advertisement); BYTE, February 1981 p 212 'Apple Stock Goes On Sale'",BYTE Publications Inc / Carl Helmers,Trade periodical,Primary (advertising artifacts) and Secondary for figures it restates,1977-06; 1977-07; 1980-12; 1980-12,1977-06; 1977-07; 1980-12; 1981-02,2026-09-24 (local archive; retrieved to sources/ by the chronology probe on 2026-09-24),https://archive.org/details/byte-magazine-1977-06 ; .../1977-07 ; .../1980-12 ; .../1981-02,sources/ia_byte_1977/ ; sources/ia_byte_1981/,1,FACT (as printed) / CONTEMPORARY OBSERVATION (the figures),High (that it was printed) / Medium (that the figures are exact),"The Feb 1981 column is UNSIGNED: its source chain is unidentified and it is the ONLY carrier of any 1976-1981 ownership figure in this dossier, so no second witness exists to the cap table. Its own arithmetic fails: 4.6M of 52.4M is 8.78 per cent, printed as 8 per cent","Mail to: Apple Computer Inc., 20863 Stevens Creek Blvd., B3-C, Cupertino, California 95014 / Steve Jobs, 25 years old, and Steve Wozniak, 30 years old, the creators of the Apple computer, each hold 8.3 million shares","Cites C-05, C-08, C-11, C-12, C-15, C-16. Line numbers: byte-1977-06.txt 2412-2413 and 2459-2460; byte-1980-12.txt 4006-4010; byte-1981-02.txt 48491-48527 and 28345. FOLLOW-UP GD-C10: identify the column's author"
CS-04,1,"No pre-1994 Apple registration statement exists in the electronic index (so the 1980 prospectus is paper-only and the filing-lineage ceiling is 1994)",EDGAR submissions index CIK 0000320193 (1249 filings 1994-01-26 to 2015-07-25),US Securities and Exchange Commission,Regulatory index,Primary,1994-01-26,2026-09-24,2026-09-24,https://data.sec.gov/submissions/CIK0000320193-submissions-001.json,sources/EDGAR_submissions_CIK0000320193_001_1994-2015.json,1,FACT (documented absence within the index),High,"An index, not a narrative source; re-probing it burns budget without settling anything, which is why this pass's own browse-edgar attempt (HTTP 503) was NOT retried","filingCount 1249, filingFrom 1994-01-26, filingTo 2015-07-25","Registered in the A dossier as the basis of AP-02/AP-21; carried here only so C-39 resolves"
CS-05,1,"The earliest Apple-assigned US patent applications and their inventors (1977-04-11 Wozniak; 1978-02-01 Holt; 1978-05-10 Wozniak; 1980-11-03 Jobs design patent), i.e. the corporation named as property owner three months after incorporation and the partnership never named at all",USPTO patent records for US4136359A US4130862A US4210959A US4278972A USD268584S served by Google Patents search,United States Patent and Trademark Office (via Google Patents aggregator),Patent register,Primary register data delivered through an aggregator,1977-04-11 to 1980-11-03,"grants 1978-12-19 to 1983-04-12",2026-09-24,https://patents.google.com/xhr/query?url=q%3D%22Apple%20Computer%22%20%26assignee%3DApple%20Computer%26before%3D19820101,UNKNOWN,2,FACT (dates and assignees as returned) / INFERENCE (that the partnership filed nothing),Medium-High,"Register data is independent of every company-side and press account in this dossier - the only genuinely independent witness this pass found for the existence of the corporation as a legal person. Search is NOT a census: 18 hits in 2 pages, page 2 unread (parameter error), and the query's text requirement admitted two unrelated Turner / Automatic Radio records which are excluded","Microcomputer for use with video display - Stephen G. Wozniak - filing 1977-04-11 - grant 1979-01-23 - Apple Computer, Inc.","FOLLOW-UP GD-C11 (re-run page=1, plus assignee string 'Apple Computer Company') and GD-C6 (USPTO TSDR for the earliest APPLE mark, which this route cannot answer). No local copy written - see P-3"
CS-06,1,"The earliest federal court record reaching the computer company and the record company as opposing litigants is 2003-10-08, and no pre-1990 docket for either the name dispute or Ronald Wayne is in RECAP",CourtListener v4 RECAP search results,CourtListener / Free Law Project,Court-record index,Primary index,2003-10-08,2026-09-24,2026-09-24,https://www.courtlistener.com/api/rest/v4/search/?type=r&q=%22Apple%20Corps%22%20%22Apple%20Computer%22,UNKNOWN,1,FACT (as to what the index holds),High,"Independent of the company and of the press corpus, but its coverage floor is the RECAP archive, so it cannot see 1978-79 paper filings; the silence is a property of the index","Apple Computer, Inc. v. Apple Corps Limited - District Court, N.D. California - 5:03-cv-04560 - filed 2003-10-08","Time audit: post-window; admitted only as the outer date of the name conflict, never as evidence about 1976-77. The companion search for 'Apple Computer' 'Ronald Wayne' returned 10 modern dockets and no 1980 case"
CS-07,1,"Three registry/archive routes failed in reportable ways, so the charter, the Utah hypothesis and any digitised prospectus remain UNANSWERED rather than absent",Failed retrieval log - California SoS bizfileOnline API / OpenCorporates v0.4 / EDGAR browse-edgar / Internet Archive prospectus query,Various,Endpoint probe,n/a,2026-09-24,2026-09-24,2026-09-24,see the Web budget table in this dossier,UNKNOWN,1,FACT (about retrieval conditions),High,"Not a source of any fact about Apple; registered so that no later pass reads these as searched-and-empty","HTTP 200 with an Incapsula JS challenge (212 bytes) / HTTP 401 Invalid Api Token / HTTP 503 File Unavailable / 6 irrelevant items","A 403, 429, 503 or bot-challenge is never a null finding - method section 14 rule 6"
```

### `conflicts.csv` — append rows

```
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
Apple,1,U-C-1,Entity formation; Timeline,"A partnership agreement signed 1976-04-01 by Wozniak, Jobs and Wayne at [Mountain View], California, and amended 1976-04-12","Christie's Lot 242 description (dated primary instruments, unread text)",1976-04-01,"Apple Computer, Inc. was incorporated under the laws of the State of California on 1977-01-03; and the universe register and general reference give 'founded 1976-04-01, Los Altos'","Apple Form 10-K FY1994 Item 1; 00_universe feasibility register via Wikipedia",1994-12-13,"Three different legal events - a private contract, a public charter and a residence gloss - collapsed into the single word 'founded'. Los Altos is a claim about whose house, not about where a company was formed; the only 1976 place inside a dated document described anywhere in this project is Mountain View, and the first address the company itself published was Cupertino","A and B1 are primary; B2 is derivative and uncorroborated in every corpus searched. The 1981 phrase 'garage operation' is the earliest retrieved occurrence of the characterisation, and a 2026 catalogue hedges the very building: 'Jobs's family garage (or his sister's bedroom - accounts vary)'","Formed as an unincorporated partnership at Mountain View 1976-04-01; converted to a California corporation 1977-01-03; address of record Cupertino from May-June 1977; report Los Altos as a residence claim, never as a place of formation","Whether the agreement's own letterhead says Mountain View (the cataloguer's brackets suggest inference); whether the conversion was continuation, asset transfer or a fresh entity - NO document addresses succession","High on both dates; Medium on place; UNKNOWN on mechanics"
Apple,1,U-C-4,First customer; Money,"The Byte Shop ordered 50 Apple-1 boards at $500 each in July 1976, fully assembled, for resale at $666.66 - restated as fact by the 2026 auction catalogue","Christie's Lot 242 lot essay",2026-01-23,"No contemporaneous text names any founding order, any unit count or any Apple-1 price: Wozniak writes in May 1977 of sale 'by word of mouth throughout California and later nationwide through retail computer stores', Wayne says only 'a large number', and 1976 print proves dealer stock rather than a purchase","Wozniak in BYTE May 1977 (AP-16/A2-25); Wayne's account (AP-29); BYTE Oct-Nov 1976 advertisements (AP-12/AP-14, A2-08); the negative at A2-23",1977-05,"A vivid number preserved by memoir, now re-printed by a commercial custodian of the founding paper with an interest in the lot; the contemporaneous record is about the market and is silent precisely where the canon is specific","The canon has no document. The 2026 catalogue is NOT independent of it - it is the same memoir lineage in a lot essay, and it contradicts Wozniak's own printed price ceiling of 'under $700' with a sticker of $666.66 only if the two kinds of statement are conflated","An early wholesale relationship with Terrell is very likely (Terrell and Jobs appear as peers in December 1976 print; Terrell kept 1976 Polaroids of the founders showing him the machine); the units, price, date and payment remain undocumented","Everything quantitative. The strongest remaining hope is a seller's document (GD-C8), not another retelling","Low"
```

### `timeline.csv` — append rows

```
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
Apple,1,1976-04-01,"Three-page typed Apple Computer Company partnership agreement signed by Stephen G. Wozniak, 'steven p jobs' and Ronald Wayne; Wayne's stake 10 per cent with the remainder split evenly; duties recorded as Mechanical Engineering and Documentation (Wayne), Electrical Engineering (Wozniak), Electrical Engineering and Marketing (Jobs)",Ronald Wayne; Steve Jobs; Steve Wozniak,"[Mountain View], California",CS-01,"FACT (dated primary, as catalogued) / Medium for the percentages and duty strings",High (existence and signatures) / Medium (terms),U-C-1; U-C-2,"Christie's Lot 242. The instrument's CLAUSE TEXT has not been read by any pass of this project - existence and dates only. GD-C1"
Apple,1,1976-04-12,"One-page 'Amendment letter to the above' signed by all three, eleven days after formation; the catalogue links it to Wayne's withdrawal 'in exchange for $800'",Wozniak; Jobs; Wayne,"[Mountain View], California",CS-01,"FACT (dated instrument) / FOUNDER CLAIM, retrospective memory, for the consideration",High (document) / Low ($800),U-C-2,"The eleven-day interval is fixed by the lot's OWN two dates, not by any narrative: 1976-04-01 to 1976-04-12"
Apple,1,1976-12-10/1977-01-19,"Homebrew Computer Club newsletters - the only in-window primary series that had tracked the firm monthly - carry ZERO body-line references to Apple across the incorporation month",club editors Robert Reiling et al,Sunnyvale / Cupertino CA,CS-03,"FACT (documented absence, counted with the corpus's own provenance headers excluded)",High for these documents,U-C-1,"Only visible because header lines 1-5 were excluded - see Provenance note P-2 and A2-05. Silence, not refutation: the newsletter never reported every concern every month"
Apple,1,1977-04-11,"Earliest patent application naming Apple Computer, Inc. as assignee: US4136359A 'Microcomputer for use with video display', inventor Stephen G. Wozniak, granted 1979-01-23",Steve Wozniak; Apple Computer Inc; USPTO,United States,CS-05,FACT (register data),Medium-High (a non-exhaustive register query; page 2 unread),None,"Three months after incorporation the corporation appears as a PROPERTY OWNER in an independent federal record - the only non-company, non-press witness to its legal existence found by this pass. GD-C11 re-runs the search"
Apple,1,1978-02-01,"US4130862A 'DC Power supply' filed, inventor Frederick R. Holt, assigned to Apple Computer, Inc. - earliest dated public record naming any individual other than the founders in a property relationship with Apple",Frederick R. Holt; Apple Computer Inc,United States,CS-05,"FACT (register) / INFERENCE (an assignment implies an employment or contract relationship)",Medium,None,"Do not convert this into 'employee #n'; no payroll document exists anywhere in this corpus (C-14)"
Apple,1,1980-12,"4.6 million shares at $22 - printed as 8 per cent of 52.4 million shares - go on sale 'early in December 1980'; FY ended 1980-09-26 sales $117M, profit $11.7M; 1979 $5M on $48M; 1978 $7.8M and $793,497",Apple Computer Inc; underwriters; Steve Jobs (25); Steve Wozniak (30); A C Markkula (32); Venrock Associates; Xerox,Cupertino CA,CS-03,"FACT (as printed) / DERIVED for 4.6M x $22 = $101.2M and 8.3M x $22 = $182.6M",High that printed / Medium that exact,U-C-5,"The single carrier of every 1976-1981 ownership figure in this dossier, and it is UNSIGNED: no independent second witness exists (Provenance note P-4)"
Apple,1,1980-12,"Apple's own advertisement moves the address of record from 20863 Stevens Creek Blvd Bldg B3-C to 10260 Bandley Drive, Cupertino, and the phone from (408) 996-1010 to an 800 number",Apple Computer Inc,Cupertino CA,CS-03,FACT,High,None,"Premises sequence 1977-05 to 1980-12 is the only documented physical-host history available; no lease was located (GD-C9)"
Apple,1,2003-10-08,"OUT OF WINDOW, logged as the outer date of the name conflict only: Apple Computer, Inc. v. Apple Corps Limited filed in the Northern District of California, docket 5:03-cv-04560",Apple Computer Inc; Apple Corps Ltd,"San Jose / Oakland CA (N.D. Cal.)",CS-06,"FACT (court index), post-stage",High,U-C-6,"Firewall: the 2003 posture is not evidence about 1976-77 and the computer company brought THIS action. No docket earlier than this was found, and no 1978-79 origin of the dispute is verified by any document this pass reached (C-37, C-38)"
```

---

— end of dossier C —

