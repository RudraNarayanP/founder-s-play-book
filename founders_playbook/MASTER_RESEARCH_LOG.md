# MASTER RESEARCH LOG — THE FOUNDER'S PLAYBOOK

Owner: Master Orchestrator (Level 1). Append-only for decisions; status table may be edited
in place. This file is the single authority on what is frozen, what is running, and what
changed. Never silently replace a company, a stage boundary, or a figure — log it here.

---

## 1. Run parameters

| Item | Value |
|---|---|
| Run start | 2026-09-23 |
| Universe source | Fortune 500, 2026 edition (72nd annual list; publication window early June 2026 per contemporaneous coverage) |
| Universe size | Top 50 by revenue, frozen |
| Reference exemplar | Airbnb forensic longitudinal dataset, Stage 1–3, ~32.6k words / 4,203 lines, provided as attachment (not stored in repo) |
| Method document | `00_METHOD_AND_STYLE.md` |
| Upload constraint | 500,000 words or 200 MB per individual source file, whichever first → split per §9 of method doc |
| Evidence standard | Public sources only; every claim classified + confidence-rated; Tier-1 anchored |

## 2. Universe freeze

Top-50 ordering for the 2026 edition was retrieved from fortune.com's structured ranking
data on 2026-09-23: ranks 1–50 captured; financial columns were **not** present in the
static HTML, so revenue/profit/HQ/industry are being filled by a dedicated universe-clerk
workstream with independent confirmation of the ordering.

Noted for the log: this edition changes the #1 position — Amazon over Walmart.
Walmart's fall from #1 also reportedly affects the Global 500 top spot; treated as
separate and pending source confirmation, not assumed.

Freeze rule: if any company must later be replaced (e.g. data proves the retrieved ordering
was wrong for this edition), record old → new, reason, and the source that forced the change.

Full data: `00_universe/fortune_top_50_2026.csv`, methodology and caveats in
`00_universe/ranking_source.md`.

### Universe status — COMPLETE (2026-09-23 16:12)

50/50 rows present; **49 fully populated, 1 carrying an explicit UNKNOWN** (State Farm's
fiscal-year basis — a mutual insurer with no SEC filing, so its figures are Fortune-only).
Confidence: 44 High, 6 Medium.

Verification method, stated precisely: revenue was tied to SEC EDGAR 10-K XBRL to the dollar on
**45 of 50** rows (38 by single-tag exact match, 7 by exact sum of reported components) and
profit on **48 of 50**; the remainder rest on Fortune's own publication alone. No figure was
hand-transcribed — all came from the structured `__NEXT_DATA__` payload inside fortune.com's
ranking pages, which carries all 1,000 records with financial columns.
The fiscal-year end date is recorded per company (Walmart's FY ends 2026-01-31, which is why it
still qualifies for the 2026 list; Amazon's ends 2025-12-31).

Ordering was independently confirmed for **all 50 ranks** with no discrepancy against Fortune's
own data; edition confirmed as the 2026 list (72nd), published 2026-06-03, on a fiscal-2025
basis, confirmed twice (methodology text + same-day release).

Recorded rather than smoothed:
- Methodology quotes are verbatim from Fortune's embedded `franchise.methodology` array
  (`ranking_source.md` §DISCREPANCY).
- **Wikipedia's 2026 table contradicts Fortune at ranks 5, 8, 12, 19, 20**, and gives McKesson
  $403.4bn where Fortune lists $359,051M — McKesson's own 10-K supports Fortune, and
  Wikipedia's citation points at the *2025* edition. Both readings are on file; Fortune wins on
  evidence, not on authority.
- **Fortune disagrees with itself** on Walmart's streak length: 13 years (Fortune 500 text) vs
  12-year run (Global 500 text). Logged as an unresolved internal conflict.
- **Home Depot's ranked fiscal year ended 2026-02-01, one day past Fortune's stated cutoff** —
  kept at rank 25 as published, with the boundary irregularity noted.

### Feasibility register — governs how "Stage 1" is defined per company

`ranking_source.md` §Feasibility register classifies all 50 by how far usable public evidence
for the founding period reaches:

| Class | Count | Meaning for stage boundaries |
|---|---|---|
| A. Single founder, continuous entity | 11 | Standard Stage 1 applicable as written |
| B. Founder-era reachable, later renamed / dual-named | 6 | Stage 1 starts at the original venture; name change logged |
| C. Pre-WWII or 19th-century origins | 11 | Evidence is archival, not filing-based; expect LOCAL-level confidence and larger UNKNOWN blocks |
| D. Successor / merger / spin-off / reorganization | 19 | **No single founding moment exists** — Stage 1 must be defined as the origin of the *operating business* that later became the ranked entity, with the corporate-prehistory gap stated explicitly |
| E. Created by statute, no founder | 2 | Fannie Mae, Freddie Mac: the founder-state section (spec §C) has no referent; Stage 1 becomes the authorizing act plus first underwriting operations |
| F. Special case | 1 | Handled individually, logged |

**Methodological ruling queued (applies when such a company is reached, does not affect
Amazon):** for Class D and E, the spec's founder-centric sections are re-anchored to the
decision-making body or programme that first behaved like a company, and the substitution is
declared at the top of that stage file rather than hidden. 19 of 50 companies are Class D, so
this is the majority case, not the exception — the framework adapts to them rather than the
reverse (spec §19, §31).

## 3. Research status table

Statuses: `NOT STARTED` · `DISCOVERY` · `DEEP RESEARCH` · `RECONSTRUCTION` ·
`ADVERSARIAL REVIEW` · `QA` · `COMPLETE`

| # | Company | Stage 1 | Stage 2 | Stage 3 | Quant | Sources | Adversarial | QA | Final |
|---|---|---|---|---|---|---|---|---|---|
| 001 | Amazon | DEEP RESEARCH | NOT STARTED | NOT STARTED | DEEP RESEARCH | DEEP RESEARCH | DEEP RESEARCH | NOT STARTED | NOT STARTED |
| 002 | Walmart | DISCOVERY | PROBE | NOT STARTED | NOT STARTED | NOT STARTED | NOT STARTED | NOT STARTED | NOT STARTED |
| 003 | UnitedHealth Group | DISCOVERY | PROBE | — | — | — | — | — | — |
| 004 | Apple | DISCOVERY | PROBE | — | — | — | — | — | — |
| 005 | Alphabet | NOT STARTED | — | — | — | — | — | — | — |
| 006 | CVS Health | NOT STARTED | — | — | — | — | — | — | — |
| 007 | Berkshire Hathaway | NOT STARTED | — | — | — | — | — | — | — |
| 008 | McKesson | NOT STARTED | — | — | — | — | — | — | — |
| 009 | ExxonMobil Holdings | NOT STARTED | — | — | — | — | — | — | — |
| 010 | Cencora | NOT STARTED | — | — | — | — | — | — | — |
| 011–050 | (see `00_universe/fortune_top_50_2026.csv`) | NOT STARTED | — | — | — | — | — | — | — |

Rows 003+ collapsed for legibility until work opens on them.

## 4. Active workstreams — Company 001 Amazon, Stage 1

Stage 1 working boundary (provisional, to be justified by evidence, not assumed):
**1993 idea formation → ~late 1995**, i.e. through the first months in which real outside
customers transacted. The boundary is a hypothesis until section B/U evidence defends it.

| Level-3 agent | Scope | Output file | Status |
|---|---|---|---|
| A Corporate Historian | Idea→incorporation→launch chronology, premises, first staff | `research/A_corporate_historian.md` | RUNNING |
| B Founder Forensics | Bezos's state at the time, household, network, capital access | `research/B_founder_forensics.md` | RUNNING |
| C Market Agent | Web/book market conditions 1990–95, growth-figure provenance | `research/C_market_environment.md` | RUNNING |
| D Customer + Distribution | First orders, channels, trust, early demand | `research/D_customers_distribution.md` | RUNNING |
| E Ops + Finance | Supply/fulfilment workflow, Stage-1 money | `research/E_supply_ops_finance.md` | **FAILED-THEN-RELAUNCHED** 16:07: completed 110 tool calls but exhausted budget before writing the dossier (a known failure mode). Retained its local Tier-1 downloads (`_scratch/s1a_full.txt` = Amazon.com Form S-1, May 1997; `sheff.txt` = David Sheff's 1994 Wired interview; `lat.txt` = LA Times profile). Replacement agent ordered to **write the file first and fill it progressively** so a partial dossier always exists |
| F Technology | Original system, archived pages, manual steps | `research/F_technology.md` | RUNNING |
| G Adversarial | Attack the canonical origin story | `research/G_adversarial.md` | RUNNING |
| Universe Clerk | Freeze top-50 + financial columns | `00_universe/*` | RUNNING |
| H Legal/IP + Organization | Name/trademark record, contracts, sales-tax posture, people and headcount register | `research/H_legal_organization.md` | RUNNING (wave 1.5) |
| I Environment Context | Macro/capital, household tech, catalog precedent, book-trade structure, institutional support, payments/fraud, press climate, skeptic's case | `research/I_environment_context.md` | RUNNING (wave 1.5) |

Assembly geometry for the ~22.5k-word exemplar stage (split per method §9.3 so no file
approaches the 500k-word / 200 MB ceiling):
`stage_1.md` (narrative A–U, ~7–9k) + `stage_1_claim_records.md` (~10k) +
`context_appendices.md` (~5k) + seven schema'd CSVs (method §13) + `_MANIFEST.md`.

Assembly plan once dossiers return: Company Lead consolidates dossiers → the three files
above → CSVs → five audits (`03_quality_control/AUDIT_PROTOCOLS.md`) → status update.

### Source-numbering blocks (Phase 1 merge keys)

Global per-company source IDs are allocated in fixed blocks so dossier merges cannot collide.
`sources.csv` is append-only; an ID is never redefined.

| Block | Owner | Range |
|---|---|---|
| A Corporate Historian | `research/A_*` | S0001–S0199 |
| B Founder Forensics | `research/B_*` | S0200–S0399 |
| C Market Environment | `research/C_*` | S0400–S0599 |
| D Customers/Distribution | `research/D_*` | S0600–S0799 |
| E Ops/Finance | `research/E_*` | S0800–S0999 |
| F Technology | `research/F_*` | S1000–S1199 |
| G Adversarial | `research/G_*` | S1200–S1399 |
| Universe Clerk | `00_universe/` | S1400–S1499 |
| H Legal/Organization | `research/H_*` | S1500–S1599 |
| I Environment Context | `research/I_*` | S1600–S1699 |
| Wave-2 gap-fill agents | `research/J_*`, `K_*` … | S1700+ |

### Wave-1 returns — anchored facts driving assembly

`C_market_environment.md` **COMPLETE 2026-09-23 16:47** (75 records, 45-row metrics table,
22 timeline events, 15 gaps, 6 contradiction blocks, plus a failed-retrieval log — null results
recorded as findings). Facts that now fix other agents' premises:

- **The S-1 is filed 1997-03-24** (EDGAR). It states incorporation in Washington **July 1994**
  and **selling from July 1995**, with **~2,200 average daily visits in Dec 1995**. This is the
  spine of the Stage-1 boundary argument: the first real-world commercial test is complete inside
  1995, and Dec-1995 traffic is the earliest audited-scale signal of it.
- **Assortment arithmetic** (the claim that made "infinite shelf" real, and its limit): 2.5M
  titles offered, but only **up to 400,000 sourceable from distributors**, who stocked up to
  350,000; **Ingram = 59% of 1996 purchases**; a large superstore carried ~130,000. So the
  novelty was *order-by-order access to a distributor file*, not owning a big inventory.
- **Payments friction was credit, not capability** — best new finding: Bezos **personally
  guaranteed a Seafirst Bank merchant account from Nov 1994 and a Wells Fargo bankcard account
  from July 1995**. Card acceptance online existed; a two-person startup got it on a founder's
  personal guarantee. This belongs in sections J, K and N.
- Postal context contemporaneous with launch: **59 FR rate notice effective 1995-01-01** —
  Priority Mail $3.00 flat for 1–2 lb nationwide; Parcel Post 2 lb $2.56–2.95; Express
  $10.50–15.00. Feeds the per-order unit economics with a dated basis.
- Web scale measured, not folklore: **Netcraft Dec 1996 = 603,367 responding sites**;
  **IDC = $318M of Web purchases in 1995**; CERN's late-1992 server list was self-declared
  incomplete. Competition as it stood: **B&N's own 10-K (1997-05-02)** — 431 superstores,
  60k–175k titles, "1.2 million books in print", world's largest direct-mail book supplier,
  **AOL exclusivity from March 1997**.
- **Unresolved conflict for section U:** US book market ~$26bn (Euromonitor 1996) vs ~$11bn
  on another basis — flagged, not reconciled. Also untraced after a full pass: 1993–95 host and
  user counts, online-service subscriber figures, returns rate, Bowker in-print count,
  independent-bookstore and book-club sizing, Book Stacks launch facts (its lone source mis-names
  the founder), NetMarket/First Virtual "first transaction" claims, and SSL's 1994–95 status.
  Each is a documented null, so no section may lean on it.

`A_corporate_historian.md` **COMPLETE 2026-09-23** (98 records, 15,757 words). The chronology is
now anchored in surviving primary instruments, not retelling:

| Date | Fact | Evidence |
|---|---|---|
| 1994-07-05 | Founding instrument survives as an SEC exhibit: Bezos subscribed **1,700,000 shares of "Cadabra, Inc., a Washington corporation" for $10,000** | S-1 Ex. 10.12 (filed 1997-03-24) — Tier 1, the founding itself |
| 1994-09-25 | `relentless.com` domain created | Verisign RDAP; independently corroborates Kaphan's "Relentless" naming memory |
| 1994-11-01 | `amazon.com` domain created — ~8 months before any recorded sale | RDAP |
| 1994-10 / 1994-11 | Shel Kaphan starts (S-1 bio: VP R&D "From October 1994"); Paul Davis "a month later" (Kaphan) | Tier 1 + Tier 2 |
| 1995-02 → 1995-03-31 | First **priced** outside money at **$0.1717/share** (father); S-election terminated with **$107,000 cumulative losses** | filings — the Stage-1 valuation and burn floor in one datum |
| 1995-07 | "**began selling books on its Web site in July 1995**" | Four-way: S-1 ×2, NYT 1999-03-14, aboutamazon. **No primary supports the popular "July 16"** |
| 1995-10-22 / 1995-11 | Earliest dated *outside* evidence of the live store | Tallahassee Democrat; Knight-Ridder (both via aggregator — print originals to be chased) |
| 1995-12-31 | **Stage-1 endpoint: $511K net sales, ~2,200 daily visits, 11 employees** | S-1 audited data — the boundary now has a number attached |

**Two folklore claims are now dead on primary evidence and belong in section U, not the
narrative:** (a) the second candidate name **"Cadamia" appears zero times** in the 1.44 MB
filing — it is unsupported, while "Cadabra" is documented by signature; (b) the "first sale"
(a $27.95 Wainwright title) is a **company legend with conflicting book titles** across its own
tellings, so section D must present it as legend with its variants, not as the first transaction.

**Also established:** A's independent query confirms the Wayback root index holds **nothing on
amazon.com before 1998-12-12 (a 302)** — RD-006 is now corroborated by two separate retrieval
attempts, so section E will be written from audited filing text plus 1995–96 press that quotes
the live site, and will state plainly that no in-window homepage artifact is available.

### Orchestrator triangulation — Stage-1 revenue spine verified at source

Dossier summaries were re-checked directly against `_scratch/s1_orig.txt` (Form S-1) rather than
accepted on report. Result, with line references for the audit trail:

- **Net sales: 1994 = $0 (audited, shown as "--"); 1995 = $511K; 1996 = $15,746K.**
  S-1 lines 338, 1285, 3472 (selected data) and 1416 verbatim: *"Net sales grew from $511,000
  in 1995 to $15.7 million in 1996."* Class FACT, Tier 1, Confidence High.
- **1996 quarterly net sales: $875K / $2,230K / $4,173K / $8,468K** (line 1525) — these sum to
  exactly 15,746, confirming they are the four quarters of fiscal 1996 and giving section Q a
  ramp rather than a single annual number: **Q1→Q4 1996 = 9.7× growth.**
- The $511K figure A used as the Stage-1 endpoint is therefore sound, but it is **calendar/fiscal
  1995 revenue as audited in 1997** — a retrospective filing describing an in-window fact. Section
  P and L must label it that way, and the 1994 zero is itself evidence: **the entity recorded no
  revenue for a full year after incorporating.**

Consequence for the boundary argument: Stage 1 can end at 1995-12-31 with an audited number
attached ($511K net sales, ~2,200 daily visits, 11 employees) — a stronger justification than the
exemplar's Stage-1 endpoint, which rested on press counts.

### Wave-1 returns (cont.) — E and J

`E_supply_ops_finance.md` **COMPLETE** (98 records, 139 KB). Stage-1 money is now audited rather
than remembered:

- **FY1995 net sales $511,000** (E&Y-audited, S-1 selected data + MD&A) — self-corroborating: Note 1's
  international sales of $198,000 is 38.7% against MD&A's "approximately 39%". Revenue booked on
  shipment including outbound shipping/handling; **only ~5.5 months of trading in 1995**.
- **$1,272,000 of common-equity cash raised in CY1995**; separately **$10,000 founder subscription and
  $44,000 notes payable** that tie exactly to Bezos's July and November 1994 interest-free loans
  ($15K + $29K), repaid during 1995 → **zero debt at 1995-12-31**.
- **11 employees, $81,000 gross equipment, ~$17,000 inventory at 1995-12-31** (risk factors + notes).
- **Untraceable to primary evidence, so section K/O must say so:** the "$1.1M from 22 friends and
  family at $50,000 each" structure, the ~$5M/20% valuation, the identity of the residual ~$976,000 (band, +/-$1,000)
  of purchasers, Kleiner Perkins's post-money valuation, Bezos's 1994–95 salary, the merchant-account
  guarantee amounts, distributor discount and payable terms, and every weekly/monthly sales curve.

`J_archive_artifacts.md` **COMPLETE** (46 records). Resolves RD-006 and, in doing so, redirects it:

- **No in-window archived amazon.com page exists.** Established three ways: `matchType=exact`
  1994–1997 → `[]`; availability API for 1996-06-01 → **1999-08-28 01:49:13**; Wayback's own
  nearest-resolver for 1995 and 1996 targets → **1998-12-12 01:25:32**, a bare 302 and not a page.
- **Two honest corrections to my own brief:** the `prefix` queries did **not** return nulls, they
  **504'd** — so absence of deep-path 1996 captures is *unanswered*, not proven; and `www.` vs bare
  host is **one** test, not two, since the host is normalised out of the urlkey. My "corroborated by
  two independent queries" claim in RD-006 was therefore overstated and is now restated this way.
- **The product can still be evidenced from artifacts, just not from the Wayback Machine.** Tier-1
  in-window documents found: **Amazon press release 1995-10-04, "World's Largest Bookseller Opens on
  the Web"** (>1M titles, search engine, online ordering, UPS/Airborne, 10–40% discounts, reader
  contributions, with a Bezos quote), and **press release 1996-06-14** ("1.1 million titles"; search
  and browse, email services, web-based credit-card payment, direct shipping). These let section E be
  written from the company's own dated public description rather than from memory.
- **A better artifact than any snapshot:** the S-1 carries the figure caption **"[PICTURES OF THE
  COMPANY'S WELCOME, SEARCH, REVIEW AND ORDERING WEB PAGES]"** — the images themselves are graphics
  files in the EDGAR accession, lost in ASCII conversion. Recovering them yields the only surviving
  visual record of the 1995–96 product. **Dispatched.**
- **1M vs 2.5M title conflict resolved:** ~1M is the in-window (1995–96) claim; 2.5M is 1997-only.
  Section E must not carry the later number backwards.
- Top unread lead carried forward: **Fortune, 1996-12-09, "Amazon: The Next Big Thing Is a
  Bookstore?"**

`D_customers_distribution.md` **COMPLETE** (82 records) — the demand side, and the run's best
in-window artifact:

- **Amazon's own press release of 3–4 October 1995**: in the "first four weeks of operation" the firm
  "shipped books to customers in **all 50 states and more than 45 countries**"; acquisition credited to
  **Netscape's "What's New" and Yahoo's "What's Cool"**; **10–40% discounts**; ordering by toll-free
  phone, fax and email; **nine mailboxes**; and Bezos personally guaranteeing the merchant account. This
  is a **company self-report** — it establishes what Amazon told the public in October 1995, which is
  not the same as verifying the shipments.
- S-1 language fixes the start: *"commenced offering products for sale on its Web site in July
  1995… from inception through July 1995 the Company had no sales."* FY1995 marketing spend $200,000.
  1996: $15.7m, 180,000 accounts, 100+ countries, **>40% repeat purchase** — all **post-boundary**,
  usable only as the consequence of the transition, never as Stage-1 evidence.
- **A new conflict for U, not in any brief:** the October PR's "first four weeks of operation" implies
  operations from roughly early September, while the S-1 says selling commenced July 1995. Either
  "commenced offering" and "shipped/operated" are different events or the self-report compresses the
  ramp. Section U must carry both; section L must not treat the states-and-countries figure as
  independent corroboration.
- **Failed primary tracing, recorded as nulls:** the "16 July 1995" first-sale date; the
  "$12,000/$14,000 in the first weeks" (only 2005 and 2025 sources); *"shipped our first book in
  August 1995"* — **absent from all five SEC documents searched**; Wainwright's 3-Apr-1995 Hofstadter
  order (Tier 2, one interview cycle, contradicts every company statement); the "first two months /
  $20,000 a week" figure; the Bulgaria floppy-disk order; the "A-for-directory-order" naming story;
  any Washington Post ownership stake; any 1995 money-back or security guarantee claim.

### Assembly fleet dispatched (2026-09-23)

Six Level-2/Level-3 consolidation agents now build the stage from dossiers on disk —
`_parts/s1_p1.md` (header + A–D), `_parts/s1_p2.md` (E–J), `_parts/s1_p3.md` (K–O),
`_parts/s1_p4.md` (P–U), `_parts/s1_claims_AJ.md` + `_parts/s1_claims_KU.md` (the claim-record
appendix, renumbered per section with `[src: dossier-id]` traces for auditability), and
`context_appendices.md` (environment appendices A–J). Budget totals to ~22.5k words, matching the
exemplar's measured Stage-1 geometry. Consolidation adds no facts: every cell carries its source,
tier, class and confidence, and dossier disagreements are routed to U rather than resolved.

### Late dossier — H integrated by a dedicated pass

`H_legal_organization.md` **COMPLETE** (61 records, 40 explicit UNKNOWNs, 60 Tier-1 passages) but
it finished **after** the K–O and E–J leads were briefed, so its material cannot be assumed
present in `_parts/s1_p2.md` / `s1_p3.md`. Rather than let late evidence silently go unmerged, a
single integration lead writes `_parts/s1_p3b_H_addendum.md` for splicing into K, G, J, Q, S and U.

What only H establishes, and what it changes:

- **The friends-and-family round has paper.** Four **in-window Shareholder's Agreements** — father,
  mother's trust, **Kaphan (1995-08-08)** and **Alberg (1995-11-26)** — plus a Kaphan ISO effective
  **1994-10-24** under a **1994** option plan, and **Subchapter C elected 1995-03-31** "with the
  consent of its stockholders". The founding instrument re-verified from **Ex. 10.12** with
  restrictive legend and stop-transfer order. This is the primary-document route to RD-003, where
  the popular "$1.1M from 22 investors at $50,000" still has no traceable source.
- **Supply fragility, stated by the filing:** Ingram — **59% of 1996 purchases** — supplied under
  **no long-term contract**. Stage 1's core assumption was a distributor that could stop at any
  time. Goes to G and M.
- **The name dispute is not establishable.** "AMAZON" applied **1995-10-23** (SN 75008413, Cl. 042),
  registered 1997-07-15, with **no opposition and no cancellation**; both S-1s disclose **zero pending
  proceedings** as of 1997-03-24, and the first assertion of a conflict is **B&N's January 1997
  letter — after the window**. "Cadabra" appears once, "Cadamia" never, and **no name-change statement
  exists anywhere** in the filings, which converts RD-008's outer bound into a documented null.
- **Payments posture is broader than the Seafirst guarantee** already credited: personal guarantees on
  Seafirst (Nov 1994–Dec 1996), the Wells Fargo bankcard account (from Jul 1995) **and company cards
  from Apr 1995**; sales tax collected **only in Washington, with no reserve**.
- **Internal document error found:** Ex. 10.13 recites a **"Delaware corporation"** while dated
  **1995-02-09** — impossible for a Washington corporation, logged as conflict **C-H1** rather than
  corrected away.

### Consolidation returns and geometry check

| Part | Content | Words (`wc -w`) | Notes |
|---|---|---|---|
| `_parts/s1_p1.md` | header, boundary table, A–D | 4,129 | ~3,700 excl. table delimiters |
| `_parts/s1_p2.md` | E–J | 4,825 | 96 table rows; caught the accession error independently |
| `_parts/s1_p4.md` | P–U | 10,337 | 63 P-rows + 21 printed derivations, 37 events, 46 dedup'd sources, 9 conflicts |
| `_parts/s1_claims_AJ.md` | claim records B–J | 26,235 | 288 records tracing 381 source docs; 92 are deduplicated merges; 156 records carry `Conflicts: U.n`; 46 keyed U items |
| `context_appendices.md` | appendices A–J | 8,527 | UNKNOWN-leaning in E (payments) and G (institutional support) |

Running total ≈ **54,000 words** with three parts still writing. This is roughly **2.4× the
exemplar's 22.5k-word Stage-1 geometry**, and the excess is in evidence, not prose: verbatim
passages, independence notes and per-cell tier/class/confidence attribution are carried on every
record. Two leads exceeded their word targets and were **allowed to** rather than cutting content —
method §9.6 says the limit governs file geometry, never research depth. No part approaches the
60,000-word hard cap, so no further splitting is required; the manifest will record it all.

**Merge obligations, in priority order:**
1. Apply `CORRECTIONS.md` COR-01…COR-11 (the three leads that ran before COR-10/11 cannot have
   applied them — the money section K and section E's "images pending" clause are the known cases).
2. Integrate the H addendum's six splice blocks, then check the 23-investor/$1,007,000 disclosure
   replaced E's claim wherever E's wording survived into p3.
3. Reconcile the four keyed U registers (p4's 9 + claims_AJ's 46 + p1/p2's cross-lead items) into
   **one** numbering; `Conflicts: U.n` references must resolve in the merged file or they are defects.
4. Emit the seven CSVs from P/Q/R/S/T plus the decisions and validation tables (task 3), with
   `claim_ref` pointing into the merged appendix.

### Coverage defect found and closed by structure, not by trimming

`_parts/s1_claims_KU.md` **COMPLETE** (144 records, 19.3k words, U.1–U.13 all resolving, 13 sources
flagged `restoration pending`). Its lead then reported the thing a summary would have hidden:
`claims_AJ` emitted **288 of the 738+ available records** and explicitly deferred, among others,
**the entire G dossier — all 38 adversarial challenges.**

Handling, and why:

1. **The deferral was not silently accepted, and the fix was not to bloat the appendix.** The
   method already requires `adversarial_review.md` as a standalone per-company deliverable (§20
   item 11), so G's challenges are being built into that file with element-by-element verdicts
   (well supported / contested / unsourced folklore), including the challenges that *fail* — which
   is the audit's positive output. Nothing was dropped to fit a length target; the material moved to
   where it belongs.
2. **One apparent dossier contradiction turned out to be a class distinction, not a conflict.**
   Appendix record J10 asserts the first site was "built in C using basic libraries from NCSA … on
   top of Oracle" while dossier F's summary says language/OS/database are UNKNOWN. Read the citation:
   the source is **Shel Kaphan's 2011 interview (GeekWire)**, Conf Medium-High, already cross-
   referenced to a conflict id. F's UNKNOWN means *no in-window document establishes the stack*. Both
   are correct, so §J states the stack as **engineer recollection from 2011** and keeps the in-window
   documentary silence as the finding. Relabeling either one would have been the error.
3. **Canonical conflict numbering is now owned by one agent.** `_parts/U_CONCORDANCE.md` maps p4's 9,
   claims_AJ's 46 and claims_KU's 13 onto one spine (U.1–U.13 plus genuinely distinct additions),
   adjudicated by substance rather than wording. The claim-record appendix is rewritten against that
   map afterwards, so every `Conflicts: U.n` reference resolves or is flagged as a defect.
4. Recorded honestly: a 738-record appendix would be ~70k words and breach the 60k per-file cap, so
   the dossiers remain the archival evidence layer under their own IDs, referenced by the merged
   appendix's `[src: …]` traces. That is a *file-geometry* decision (§9.3), not a depth decision.

| 2026-09-23 | **Run mode changed to PARALLEL across companies** (Walmart probe started while Amazon Stage 1 finishes repair), superseding strict one-company-at-a-time sequencing | User instruction on 2026-09-23 to parallelize and to move execution off the local machine. Amazon's boundary and evidence spine are already fixed, so overlap no longer risks re-work on the pilot | User instruction | Reversible; each company's folders stay independent |
| 2026-09-23 | **Cloud execution blocked, not abandoned.** No QCA MCP server is connected and no `QODER_ACCESS_TOKEN`/`QODER_PAT`/`QCA_MCP_PAT` is configured locally; `E:\founder's playbook` is **not a git repository**, so a remote agent has no route to the 80 files / 5.4 MB evidence base | Remote agents cannot see verified primary documents that exist only on this machine; re-deriving them remotely would discard the audit trail | Needs (a) a locally configured PAT — never pasted into chat — and (b) either a git remote to carry `founders_playbook/` or file upload as QCA resources | BLOCKED ON USER |

## 4A. Parallel execution map

| Company | Class (feasibility register) | Stage 1 status | Notes |
|---|---|---|---|
| 001 Amazon | A — single founder, continuous entity | **QA** (2026-09-24, Stage-1 closure pass: numeric closure verified and finished, the five AUDIT-4 causal sites closed with U.43 appended, the filing-lineage rule applied) — prior state, retained as history and not rewritten: *repair passes running (numbers); audits 1, 2, 4 returned, 4 failed-then-repaired* | Evidence base local: 4 filings + 11 dossiers, ~1.02M words repo; a 424B1 landed in `sources/` on 2026-09-24 unused and unregistered (RD-027). Closure sheets: `03_quality_control/amazon_s1_numeric_closure_final.md`, `amazon_s1_causal_lineage_closure.md`. **§3's status table is the orchestrator's and still reads `DEEP RESEARCH` for 001 Stage 1 — left un-corrected deliberately; that table is not this pass's row to rewrite** |
| 002 Walmart | A, but origins predate 1962 entity | **Verdict REVERSED → EXEMPLAR, gated** (643-line retest, 26 records). The original probe had said forensic-core on an untested premise | 13 in-window Tier-1 items, incl. audited FY1968-73 sales/store series and a 1970-02-01 pooling note; IA carries the printed annual-report run FY1972-1997 with text layers | Fleet gated on four named escalation targets (paywalled Arkansas/trade newspaper full text, the 1962 opening flyer, Arkansas SoS entity records, a 1970 prospectus facsimile) and on paper archives |
| 003 UnitedHealth | Successor/merger origin — probe to confirm | **Probe wrote nothing (3rd write-late failure) but saved 55 primaries; mining-only completion pass running** | Predecessor EDGAR searches (Chartermed, Metropolitan Health Plans, Paxon), a 1998 S-4, FY1999 10-K, DEF 14As 1996-2000, Wayback captures from 1997-02-18, Google Books hits. Its well-documented formation material is likely 1990s, not 1970s |
| 004 Apple | A, single founders, continuous entity | **Probe complete → EXEMPLAR depth, gated.** 38 records, 11,208 words, 49 files / 9.5 MB | S1 **1975 → 1977-01-03** (CA incorporation per Apple's own 1994 10-K, corroborated in 1981 print); S2 1977 → 1980-12 IPO (4.6M shares, 8% of 52.4M, $22 - BYTE Feb 1981); S3 1980-12 → 1985 untested. Excluded: no EDGAR text before 1994-01-26, no pre-1994 web artifact, no 1976 sales figure, Markkula terms and Wayne's 10%-vs-12% unresolved |
| 002 Walmart (retest) | A, pre-1962 origins | **VERDICT UNDER RETEST** - the forensic-core call rested on two of four corpus families and missed digitised periodicals, the very thing that made Apple exemplar-capable | Fast-tier retest across Internet Archive / HathiTrust / Google Books trade and general periodicals 1945-1970 plus auction and finding-aid records; may raise or confirm the rating || 002 Walmart (retest result) | A | **The family that flipped it was digitised bound CORPORATE PRINT, not periodicals.** Method now: probe five families - filings, web archives, periodical corpora, **digitised annual reports / corporate print**, auction and museum records | Still untried: Google Books/HathiTrust (429), Chronicling America + Arkansas print (403 bot-block), IA `inside.php` (positive control failed → its nulls are void). No Walmart founding document in public sale records |


**Recommended boundaries (from the probe, to be defended or overturned by the fleet):**
Stage 1 **1950 → 1970-10-01 IPO** (the 1950 start is Low confidence, memoir/Tier-3 only; the IPO is the
one hard documentary boundary the record actually creates). Stage 2 1970-10 → FY1979/80, where the paper
10-K era begins. Stage 3 1980 → 1992, provisional.

### Archival reality check — the constraint that governs most of the universe

Walmart's Tier-1 floor for 1962–1970 is nearly bare, and the reasons are general:

- **EDGAR carries essentially nothing before 1994.** Walmart's index begins **1994-02-14**; its first
  available 10-K is acc. 0000104169-95-000004. That is not a Walmart artifact — electronic filing
  coverage for most registrants starts in the mid-1990s, so **any company whose formative period ends
  before ~1994 has no searchable primary filing trail for it.**
- **No web artifact before the mid-1990s** (Walmart: earliest 1996-12-29; Amazon's Stage 1 already
  proved the same limit from the other direction — no archived page before 1998-12-12, and that a 302).
- **Zero contemporaneous press surfaced through open web search** for the 1950–1970 period.
- What survives is dated but weakly sourced: the company's own uncited timeline (which is citable as
  self-narrative — its **documented silence on pre-1962 history is itself a finding**), 2004/2012
  retrospectives, and the 1992 memoir.

Consequence, stated plainly: **exemplar depth is achievable for the Amazon-class cases and impossible
for most of the pre-1990s cohort without padding the file with lore** — which the method forbids
(§42/§43). Applying it there would manufacture a document that looks like research.

**Four targets carry all the upside for Walmart**, and until one lands the fleet stays off: paywalled
or archival newspaper full text (Arkansas Gazette, Southwest Record, national trade press), the original
1962 opening flyer, Arkansas Secretary of State entity records, and a 1970 prospectus facsimile.
Untried avenues with real potential: Hagley Museum and Library business collections, archive.org's
digitized annual-report and trade-journal runs, and university special collections — paper archives are
where this period's evidence lives.

Rule for parallel waves: a company may start only when its probe has returned a depth verdict, so that
exemplar density is spent where archives can support it rather than padded with retelling.

## 5. Decision log (append-only)| Date | Decision | Why | Evidence | Reversibility |
|---|---|---|---|---|
| 2026-09-23 | Research order = Fortune 2026 rank order, starting Amazon (#1) | Spec §0 freezes universe then reconstructs each company independently; rank order keeps the log auditable | `00_universe/fortune_top_50_2026.csv` | Reversible; no data dependency |
| 2026-09-23 | One file per company per stage; 60k-word hard cap; split only at section boundaries | 500k-word/200MB per-source ceiling; projected 1.5–2.5M-word dataset cannot be one document. Word budget set far below the ceiling so no file approaches it | Method doc §9 | Structural; re-splitting later is cheap, merging is not |
| 2026-09-23 | Airbnb exemplar treated as format/method reference only, not project data | User instruction: it is an example of the standard, and is not stored in the repo | User instruction 2026-09-23 | n/a |
| 2026-09-23 | Dossiers written per specialist, then consolidated by a Company Lead | Parallelism per spec §5; keeps provenance attributable to the retrieving agent instead of reconstructed from memory | Method doc §7 | Reversible |
| 2026-09-23 | **Sequencing = one company through all 3 stages, fully audited, then the next** (Amazon → Walmart → UnitedHealth → …) | User choice, deep-research Phase 0 | User answer 2026-09-23 | Change requires re-opening stage boundaries of the current company |
| 2026-09-23 | **Depth = exemplar depth, measured not guessed: ~22,500 words per company stage** — narrative A–U ≈7,150 + claim-record appendix ≈10,410 + environment context ≈5,005 | User chose exemplar depth; the Airbnb reference file's actual geometry is 32,579 words total, of which Stage 1 block = 22,565 words (measured 2026-09-23). Supersedes my earlier 8–14k estimate | Exemplar §word counts, measured | Reversible; drives file splitting |
| 2026-09-23 | **Output = repo files only.** No QMind / external knowledge-base imports unless explicitly requested; `_MANIFEST.md` keeps files upload-ready | User answer 2026-09-23 | User answer 2026-09-23 | One-way only if the 500k-word ceiling is later hit by an external consumer |
| 2026-09-23 | **Stage 1 start re-based from 1993 to 1994** (first anchor 1994-07-05, the surviving founding instrument); spring-1994 ideation retained but re-classed as retrospective; 1993 kept as founder pre-history with `UNKNOWN` | AUDIT 1 (chronology) = **CONDITIONAL FAIL**: every load-bearing date verified against the restored filings with **0 date errors** and **0 untagged time-travel**, but the 1993 start has **no source at all**, and §Q's header contradicted its own rows. Spec §6 requires the boundary to be the earliest *defensible* origin, not the earliest claimed one | `03_quality_control/amazon_s1_audit1_chronology.md`; founding instrument S-1 Ex. 10.12; domain records 1994-09-25 / 1994-11-01 | **Reversible** — if a 1993-dated primary document surfaces, the boundary moves back and this row is amended |
| 2026-09-23 | Company 001 stays Amazon | User confirmed rank-order start; richest Stage-1 archive in the top 10 (S-1, 1995–96 press, Wayback, reported books) | User answer 2026-09-23 | Reversible |
| 2026-09-23 | Format reconciliation: the playbook A–U structure carries the deep-research skill's mandatory parts — A ≡ TL;DR/Executive Summary, H+I ≡ Status Quo, M+U+G(adversarial) ≡ Critical Assessment, T ≡ Bibliography, claim records ≡ Source Extracts, audits ≡ Methodology. No duplicate `DEEP_RESEARCH_*.md` is generated for companies | Two structures for the same evidence would drift apart; the forensic format is the stricter superset | Method doc §7 + skill output rules | Reversible; documented here |
| 2026-09-23 | **Merge normalization: narrative tables revert to the exemplar's 4-column geometry** `\| Variable \| Value \| Source \| Confidence \|`, with a compact source token carrying tier and class inline (e.g. `S-1 orig., 1997-03-24, §History of the Enterprise [T1 · FACT]`), and the heavy metadata — verbatim passage, full URL, independence note, `[src: …]` traces — living in the claim-record appendix | The parts currently repeat per-cell metadata in both places, which is why the narrative hit 22,577 words against the exemplar's 7,150. Method §8 mandates the 4-column form. This is editorial normalization, **not** evidence reduction: nothing is dropped, duplication is relocated | Reversible; re-widening the tables costs only reformatting |

## 6. Open research debt

Every item is a named follow-up task, not a disclaimer. Populated after QA.

| ID | Company | Section | Debt | Trigger | Assigned | Status |
|---|---|---|---|---|---|---|
| RD-001 | Amazon | D/P | "First sale" date and buyer have competing accounts | Conflicting founder accounts | dossier D + G | OPEN |
| RD-002 | Amazon | H | Web-growth percentage that motivated the plan: provenance and what it measured | Unsourced metric repeated widely | dossier C + G | **CLOSED as untraced** — the circulating "2,300 percent" figure appears **nowhere in the S-1**, no in-window instance was retrieved, and it survives only in Tier-4 modern retellings. Classified FOUNDER CLAIM with provenance unestablished; section H must state that, not repeat the number as history |
| RD-003 | Amazon | K/O | Friends-and-family round amount, date, participants vs later retelling | Founder-claim density | dossier E + B | **CLOSED with primary numbers — see COR-10.** Both filings disclose **3,021,000 shares to 23 investors at ~$0.3333 = $1,007,000** (subscriptions 1995-12-06 → 1996-05-16, so mostly **post-boundary**), plus an earlier **$345,525 at ~$0.1717**. Per-investor amounts and the roster of 23 are **not** disclosed; four in-window Shareholder's Agreements name father, mother's trust, Kaphan and Alberg. The legend's "$1.1M from 22 at $50,000 each" is near-but-wrong and is retired |
| RD-004 | Amazon | I | Predecessor online book sellers, what was actually novel | Possible missing competitors | dossier C + G | OPEN |
| RD-005 | Universe | — | Financial columns absent from static fortune.com HTML | Tier-1 gap | universe clerk | **CLOSED** — retrieved from Fortune's embedded data payload; 45/50 revenues XBRL-verified |
| RD-006 | Amazon | E, F, T | **No in-window archived amazon.com page in evidence.** The cached Wayback capture is 2006-05-22; the Seattle Times item is 2005 and the LA Times item 1997-07-20 — none are Stage 1 | Early product described from memory, not artifact | retrieve a 1996 capture (wayback CDX for amazon.com, earliest snapshots) and record its timestamp + page inventory | **OPEN — highest priority** |
| RD-007 | Amazon | E | Distinguish which cached documents are contemporaneous vs retrospective before any claim cites them | Time-audit contamination risk | cache annotated 2026-09-23; F agent re-checking timestamps | OPEN |
| RD-008 | Amazon | B, Q | **Cadabra → Amazon rename date unknown.** WA Secretary of State unreachable (`corqs.access.wa.gov` failed; OpenCorporates 401); bounded only to 1994-11 → 1995-07 | Tier-1 corporate record gap | wave-2: Washington State Archives, newspaper trade notices, USPTO/EUIPO predecessor filings, the 1995-11-01 domain date as terminus | OPEN |
| RD-009 | Amazon | C, N | **No 1994 "roadmap"/notebook located in any retrieved record.** The document that supposedly drove the decision is asserted everywhere, evidenced nowhere so far | Central to the origin claim; the most-cited artifact with no citation | **RESOLVED at evidence-rung 3 — founder description only.** Rungs 1 and 2 are empty: no artifact, no page image, no facsimile, no auction or finding aid, and **not one quoted sentence of the document**. Earliest description: **LA Times 1997-07-20** ("pecked out a business plan on his laptop"); earliest first-person: **Sheff, spoken 1999 / published 2000**. The strings "91 pages", "the roadmap" and "Future of Computer Stores" return **zero hits** across the 1.44 MB S-1, the FY1997 10-K and every cached file; external hits are Facebook and LinkedIn only. Wikipedia's 1994-founding assertion cites **only Stone 2013** — a single-source lineage, not corroboration | **CLOSED — section C must state the legend's genealogy, not the legend** |
| RD-010 | Amazon | B | Bezos's actual last day at D. E. Shaw; Bellevue and SoDo addresses and their dates | Sequencing of quit → move → incorporate | wave-2: DE Shaw tenure via contemporaneous notice, county assessor/recorder records, HistoryLink footnotes | OPEN |
| RD-011 | Amazon | D, L | Earliest outside store evidence (Tallahassee Democrat 1995-10-22; Knight-Ridder Nov 1995) currently **aggregator-sourced** | A High-confidence validation signal cannot rest on a reprint | wave-2: pull the print edition page/clip or the newspaper's own archive; record citation chain | OPEN |
| RD-012 | Amazon | D, U | "First sale" legend: $27.95 Wainwright title, **conflicting titles across tellings**; "July 16" launch date has no primary support | Famous-anecdote verification (§30) | dossier G + D; present as legend with variant list, launch stated as "July 1995" | OPEN — already framed for U |
| RD-013 | Amazon | B, C, E, F, K | **Orchestrator-introduced source-label error:** the evidence cache described `sheff.txt` as "Sheff's 1994 interview"; it is a **1999 interview published 2000**. Four agents were briefed against the wrong label | Would have converted a retrospective into contemporaneous founder evidence — the exact contamination §18 exists to stop | **Audit run 2026-09-23: 0 of ~195 Sheff-citing records carry the bad date.** Dossier B caught it from the file's own header, logged it as its first finding (B-01), and corrected the cache line unprompted | **CLOSED — no contamination; label fixed at source** |
| RD-014 | Amazon | all | **Evidence-base destruction:** the adversarial agent deleted the shared `_scratch` folder on completion, destroying every downloaded primary | Provenance re-verification for Audits 2–3 | Method §14 rules 4–5 added (agents may touch only their own output file; `sources/` is read-only); Evidence Registrar restoring documents to `company_001_amazon/sources/` — **S-1 restored (301,685 B, EDGAR accession 0000891020-97000839)** | PARTIALLY CLOSED — 10-K, HistoryLink, Mosaic, Sheff still to restore |
| RD-015 | Amazon | B, D | **MacKenzie Tuttle appears nowhere in the S-1 or the 1997 10-K** — an established null against the popular co-founder/early-employee narrative | Founder-state section; survivorship of a spouse's contribution in later telling | dossier B (133 records); re-test against later filings and primary registry records in Stage 2 | OPEN — recorded as null, not as absence of fact |
| RD-016 | Amazon | I, U | **Discount-era conflict:** Amazon's own press release 1995-10-04 claims **10–40% discounts**, while the S-1 dates deep discounting of featured titles to **March 1997**, and dossier I concludes Stage 1 must be judged on selection and convenience rather than price war | Changes the business-model reading of Stage 1 — a "price disruptor from day one" framing would be anachronistic | dossier D + I; section U carries both; do not resolve without the pricing-program text in the original S-1 vs S-1/A No. 5 | **OPEN — escalate at merge** |
| RD-017 | Amazon | H | The **~$11bn** narrow-basis book-market figure cited in the conflict register **was never retrieved**; only Euromonitor's ~$26bn has a source in hand. `Fortune` 1996-12-09 remains unread (404 paywall) | A conflict cannot be recorded as live if one side is uncited | section U must present this as *one sourced figure plus an untraced counter-claim*, not as a two-sided dispute | OPEN |
| RD-018 | Amazon | J | 1994–95 US **household internet-access share is unestablished** (NTIA/CPS gives 18.6% for 1997, 26.2% for 1998; home PC ownership 24.1% in 1994). Also untraceable: "6.8% of households online in 1994", and Gale's basis-less $211bn 1990 mail-order figure | The adoption baseline that every origin story leans on | documented null; section H uses PC ownership as the proxy and says so | OPEN |
| RD-019 | Amazon | appendix | **2 `Conflicts:` references unmappable at appendix merge** — G04 and G11 cited `U.38` from claims_AJ's local 46-item key, which the canonical register never defined | Every cross-reference must resolve; an unresolved key hides evidence | Resolved on substance by the orchestrator 2026-09-23: both records dispute whether the distributor's "within hours" shipment was quantified, which is exactly canonical **U.39 "Observed fulfilment speed and damage"**. References rewritten to U.39; the original flag retained in the coverage note rather than erased | **CLOSED — 0 unmapped** |
| RD-020 | Amazon | header, C, Q | **The 1993 stage start had no documentary support whatsoever** — asserted in the briefs, absent from the record | Stage boundary must be defensible (spec §6), and the audit's own pass condition is month-precise sourced boundaries | AUDIT 1 (2026-09-23) → **boundary re-based to 1994**, first anchor the 1994-07-05 founding instrument; 1993 retained as founder pre-history with row confidence `UNKNOWN`; spring-1994 ideation re-classed retrospective | **CLOSED** (reversible if a 1993 primary surfaces) |
| RD-021 | Amazon | Q | **§Q's header span contradicted its own rows** (header 1994-07-05 vs rows dated 1993 and 1994-02) | Internal inconsistency in the chronology deliverable | Fixed in the same AUDIT 1 repair pass: header/scope note re-based; pre-anchor 1994 rows kept and tagged retrospective, not deleted | **CLOSED** |
| RD-022 | Amazon | K, O | **AUDIT 2's own "$245,572 parental money in the filings" claim is unverified** — the number appears nowhere in the original S-1, S-1/A No. 5 or the 10-K405 | The auditor must not be exempt from the rule it enforces; adopting it would launder a new unsourced figure into the report | Rejected pending evidence (COR-14.2); COR-09 stands: $150,000/$250,000 untraced, $250,000 traces to a 2018 LA Times inference | OPEN — needs the document and line, or it dies |
| RD-023 | Amazon | D, F, I, Q | **Detail-misattribution cluster:** nine mailboxes, toll-free, fax and e-mail ordering were credited to the 1995-10-04 press release, which contains none of them | A dated artifact cited for content it lacks undermines an otherwise Tier-1 source | Re-attributed by COR-13 (original S-1 l.2174/2179–2180; fax → Knight Ridder Nov 1995, Medium); repair agent propagating | IN REPAIR |
| RD-024 | Method | all | **An orchestrator-authored correction was wrong and had to be superseded by audit.** COR-03 declared "11 employees at 1995-12-31" imprecise; the amendments file exactly that date | If my corrections are not auditable, they are just authority | **CLOSED** — COR-12 supersedes COR-03 with the two filed sentences quoted side by side; standing lesson: a correction is a claim, and claims get tested | CLOSED 2026-09-23 |

| RD-025…RD-028 | — | — | **Numbering collision, recorded rather than tidied:** AUDIT 4 assumed AUDIT 2 had consumed RD-024–RD-028, but the register assigned AUDIT 2's items RD-022–RD-024. These four slots are therefore **unassigned**; the audit's sheets cite RD-029–RD-034, which are registered verbatim below so log and sheet agree | Ids must be unique and stable; renumbering history would break every existing reference | Fixed convention: **ids are allocated only by appending, never reused or renumbered**, and a sheet may not pre-assign ids into the register's space | CLOSED (convention recorded) |
| RD-029 | Amazon | H, D.1, F.2, R | **Directory-placement efficacy is unresolved** — and C-01's outcome-dependent sentence must not be "fixed" by restoring a claim the evidence cannot carry: chase a dated *independent* record of the 1995 Netscape "What's New" / Yahoo "What's Cool" listings (directory archives, a dated third-party index) | The single most-cited acquisition mechanism of the stage is attested only by the company itself | wave-2 archive agent; until then §D.1's `UNKNOWN (effect of each)` governs and §H says "claimed by the company, effect unmeasured" | OPEN |
| RD-030 | Amazon | E.2, K.5, M.5, U.24 | **Could a two-person Washington firm have obtained a company-only merchant account in Nov 1994?** The file's most load-bearing unasked counterfactual: it decides whether Bezos's personal guarantee was credit rationing, founder convenience, or standard practice | Without it, §K implies a constraint the record never priced | search 1994–95 acquirer underwriting practice for internet resellers, Small Business Administration/press reporting of the period; if none, record as UNKNOWN and remove the implication | **OPEN — highest analytic value** |
| RD-031 | Amazon | F.2, appendices H | **1995 press-coverage effect, separated by year.** The two dated 1995 outside items are Tier-4 reprints; establish what is observable about 1995 coverage independent of Amazon's own account | Prevents "press drove demand" from importing 1996–97 dynamics | chase print originals (Tallahassee Democrat 1995-10-22, Knight Ridder Nov 1995) per RD-011 | OPEN |
| RD-032 | Method | A, S | **Propagate the survivorship control into the deliverable** — the record-selection null existed only in `adversarial_review.md` §5 | A reconstruction of a survivor can be hindsight-clean in wording and still selection-biased in content | **APPLIED 2026-09-23** — `00_METHOD_AND_STYLE.md` §2 now carries a "Record-selection null" requirement for §A and §S of every stage file; Amazon's stage file must adopt it in repair | CLOSED for method; OPEN for the file |
| RD-033 | Amazon | appendices | **Companion-file boundary and figure drift:** appendices still carry the pre-re-base boundary (C-16), a mislabelled "Stage-1 capital raised" row (C-15), and **$8,000,140 where the filing says $8,000,014** at two sites (C-17) | A transposed digit in a capital figure is exactly what AUDIT 3 exists to catch; the label error misplaces post-boundary money inside Stage 1 | repair agent: regenerate appendices against the re-based boundary, relabel, correct both figures against the original S-1 | OPEN — assigned to repair |
| RD-034 | Method | §7 | **The template left interpretive codas unpoliced** — five of seven causal failures lived in "so what" paragraphs, which §16 covered for tables only | Recurrence risk across 49 remaining companies if unfixed | **APPLIED 2026-09-23** — §7 now requires evidence–mechanism–alternative–confidence in every coda, with "mechanism UNKNOWN" permitted; appendices' five codas still need repair | CLOSED for method; OPEN for the file |

| RD-035 | Amazon | stage_1 N-04, N-05, N-06 | **Three causal claims still standing in `stage_1.md` §N**, handed over by the appendix sweep because that agent's write scope excluded the stage file | Same defect class that failed AUDIT 4 condition 2 | Details in `03_quality_control/amazon_s1_hindsight_repairs2.md` §Logged for next pass | **OPEN — next repair pass** |
| RD-036 | Amazon | stage_1 §H l.463 | **"card entry frightened buyers"** — a new unsupported causal claim found during the sweep | Would import 2020s payment-psychology into 1995 framing | same note | **OPEN — next repair pass** |
| RD-037 | Amazon | validation.csv r9 | **A causal claim inside a dataset cell**: "could earn editorial distribution" | CSVs are evidence tables, not argument surfaces; an inference in a `magnitude`/`notes` field escapes the §16 mechanism rule | same note | **OPEN — next repair pass** |
| RD-038 | Amazon | `_parts/s1_p2.md` | The intermediate part mirrors an appendix claim that was fixed only in the deliverable | Parts are the merge's audit trail; a stale claim there invites re-import by a future consolidation pass | same note — amend additively with a supersession marker, do not rewrite silently | OPEN — low priority |
| RD-039 | Amazon | data_gaps.csv | Gap register does not yet carry RD-035/036 rows | §13 requires every High-importance gap to carry a follow-up task, and these now have one | Reconcile in the same pass as RD-037 | OPEN |


**Additions logged 2026-09-24 by the Stage-1 closure pass — ids allocated by appending only; RD-035, RD-036 and
RD-037 above are NOT re-keyed, and the collision the final audit sheet records (the recheck's three debts
re-using those ids) is handed to the orchestrator unsolved.**

| ID | Company | Section | Debt | Trigger | Assigned | Status |
|---|---|---|---|---|---|---|
| RD-040 | Amazon | §H, §D.1, §O.7; `validation.csv`; §U spine | Directory- and press-driven conversion in 1995 unadjudicated and unrouteable; five causal sites carrying the tags the file already prints | AUDIT 4 condition 1 FAIL; AUDIT 5 A-B2 | Company Lead (edit) — Hindsight Auditor (re-confirm) | **CLOSED as to the five sites and the routing (2026-09-24)**: §H l.463 rewritten, §D.1's existence clause re-tagged as company-claimed, `validation.csv` r9 re-keyed, §O.7's differentiator list re-named with placement removed, **U.43 appended** and the three stale `→ U.41` pointers re-pointed; `conflicts.csv` gains row U.43. **AUDIT 4 has NOT re-confirmed it — a repair is not a pass** |
| RD-041 | Amazon (recurs across 49 companies) | `stage_1.md` header, §G.3, §J, §T, §U.1; 22 claim records; `conflicts.csv` U.1/U.8/U.9 | One registration lineage counted as two corroborations | AUDIT 5 A-B1 vs method §3 | Method owner + Evidence Registrar | **PARTLY CLOSED (2026-09-24)** — the header ruling is written, both narrative sites and the §T doctrine row are capped, 22 records re-keyed to `Corroboration: 1 (same lineage as S0801)` with 2 left at 2 on stated grounds, and no confidence moved (§3 grants High on a primary document alone). **OPEN:** `sources.csv` `independence_note` for S0803/S0805, `context_appendices.md` §F, and the Walmart/Apple/UnitedHealth re-audit. §3 itself already carries the rule (the brief calls it "new"; the method file was amended at commit `0fedd44`, so this pass applied it and wrote no method text) |
| RD-042 | Amazon | `data_gaps.csv`; this log §6; `context_appendices.md` §J | Register mirror not closed: no survivorship row, RD-035/036/037 id collision, RD-027 unresolved | Method §13 (High-importance gap without a clean follow-up id) | **Orchestrator** | **OPEN — High.** Not touched: de-colliding ids means re-keying another agent's debts, and the survivorship row is a register-mirror decision. **Note that RD-027 is now actionable:** a 424B1 (`acc. 0000891020-97-000868`, 266,755 B, 35,054 w) appeared in `sources/` at 17:00 on 2026-09-24, during this closure. This pass **read none of it, cited none of it and claimed no verdict from it** — a file that arrives while you are closing a stage is evidence for the next pass, not for this one, and it is registered here only so its arrival is not lost |

### Archive route discovered mid-run — the EDGAR floor is not the last word

The Walmart probe concluded that pre-1994 origins cannot carry exemplar depth, because EDGAR starts
~1994 and web archives mid-90s. The **Apple probe is now contradicting the pessimistic half of that
inference**: it is retrieving **Byte magazine's 1976 issues in full text from Internet Archive**
(`company_004_apple/sources/ia_byte_1976/`, twelve issues, plus a 1977 run). Contemporaneous trade
journalism is a **Tier-1 primary source class that the EDGAR floor argument silently ignored.**

Consequences, to be tested rather than assumed:

1. Walmart's forensic-core verdict was reached **without checking digitised trade-press corpora**
   (Saturday Evening Post back files, Retailing Today / Daily News Record, Arkansas periodicals on
   archive.org and HathiTrust). If those land, its depth verdict is revisable upward — the verdict was
   correct on the evidence examined, and the evidence examined was too narrow.
2. The probe brief is being amended for the remaining companies to make **Internet Archive /
   HathiTrust periodical search a mandatory step** before any depth verdict, alongside EDGAR and CDX.
3. This is a lesson about null results generally: a null from one corpus family is not a null. The
   Amazon run already learned it with `matchType=prefix` returning 504 (unanswered) rather than empty
   (proven); this is the same error in a different costume.

### Amazon Stage 2 — boundary evidence (dossier A, 98 records, 2026-09-24)

Recommended end boundary: **1997-05-14/15**, on the offering sequence rather than on the later
fame of the event. Amendment No. 3 (1997-05-09) set a **$12–14** range; Amendment No. 5
(1997-05-14, that same morning) raised it to **$14–16** with a 20% upsize; Amazon's own
1997-05-14 release reports the price at **$18.00 on 3,000,000 shares** — above its own ceiling,
cleared in five days. That is external pricing behaviour, not management self-description, so
it qualifies as evidence of institutionalisation under spec §6 while staying inside the firewall.

Alternative tested and rejected: **1996-12-31** (repeat orders >40%, 4,800 Associates members) —
rejected because the FY1996 quarterlies are explicitly **unaudited** and the year-end headcount
conflicts (151 vs 158 across documents).

Two substantive corrections the dossier settled: Bezos became **CEO on the 1996-05-28 merger
signature page** (President→CEO on a single instrument), and the Delaware reincorporation was
agreed 1996-05-28 but **effected 1996-06-18** — which bears on Stage 1's impossible
"Delaware corporation" recital of 1995-02-09 (conflict C-H1). And the "move beyond books"
reading of this stage **fails**: the music store shipped 1998-06, and the FY1997 10-K still
describes Amazon as the leading online retailer of **books**.

Open gaps carried: no Tier-1 event between 1997-05-15 and November (the 1997 10-Qs were never
opened); the first trading day and day-one price are unproven; outages are an admitted condition
with no dates or magnitudes.

### Recurrence note — the write-late failure is structural, not a fluke

As of 2026-09-24 the "researched everything, wrote nothing" failure has recurred **three times** despite
§14: twice with wave-1 dossiers, now with the UnitedHealth probe (469-word skeleton, 1 record, but **55
source files saved to disk**). The mitigations that worked: (a) saving primaries to `sources/` as you go,
which made the loss recoverable, and (b) relaunching a **mining-only agent** against the local files with a
4-search budget instead of re-running the original brief. Fast-tier agents that end with a "now writing"
sentence and an empty file should be treated as **partially succeeded**: keep the evidence, redo the
write-up.

### Number-round status after two repair passes

+94.1% (not +95.2%), the true third **$871,000** (not the back-solved $871,024), composition
**$976,408**, and **43% original / 41% S-1/A No. 5** as a version discrepancy — all established from
the original S-1 by line (l.2864, l.4301–4302, l.985–988, l.2919, l.1055–1062, l.3149, l.3535/3546/3645).
The second repair pass validated its CSVs **by planting the previously-dropped defect in a copy and
confirming the detector caught it** — the strongest verification step taken so far. A residual sweep is
chasing stale copies that survived outside that agent's write scope (known survivors: `stage_1.md`
§S and §U.8, `data_gaps.csv` r11, `context_appendices.md` ~l.596, `_parts/NUMBER_DEFECTS.md` r43), and
**both audit gates still need their independent re-verification — a repair is not a pass.**

## 7. Cross-company synthesis gate

Spec §22 forbids cross-company pattern claims until individual reports pass QA. No
`02_cross_company/` analysis is written while any contributing company is pre-QA;
only structural placeholders.
