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
| 001 | Amazon | QA — repairs applied, **third-pass re-certification running** | **RECONSTRUCTION — 3 volumes on disk (81,129 w), claim records + 5 audits running** | NOT STARTED | RECONSTRUCTION (193 rows) | RECONSTRUCTION (113 rows) | RECONSTRUCTION (68 conflicts) | AUDIT 6 = REOPEN → AUDIT 7 pending | NOT STARTED |
| 002 | Walmart | DEEP RESEARCH (133-record dossier) | PROBE | NOT STARTED | DEEP RESEARCH | DEEP RESEARCH | NOT STARTED | NOT STARTED | NOT STARTED |
| 003 | UnitedHealth Group | DISCOVERY | PROBE | — | — | — | — | — | — |
| 004 | Apple | DEEP RESEARCH (80 records, 4 registers) | PROBE | — | DEEP RESEARCH | DEEP RESEARCH | NOT STARTED | NOT STARTED | NOT STARTED |
| 005 | Alphabet | NOT STARTED | — | — | — | — | — | — | — |
| 006 | CVS Health | NOT STARTED | — | — | — | — | — | — | — |
| 007 | Berkshire Hathaway | NOT STARTED | — | — | — | — | — | — | — |
| 008 | McKesson | NOT STARTED | — | — | — | — | — | — | — |
| 009 | ExxonMobil Holdings | NOT STARTED | — | — | — | — | — | — | — |
| 010 | Cencora | NOT STARTED | — | — | — | — | — | — | — |
| 011–050 | (see `00_universe/fortune_top_50_2026.csv`) | NOT STARTED | — | — | — | — | — | — | — |

Rows 003+ collapsed for legibility until work opens on them.

### Capacity finding 2026-09-25 — the achieved density is ~6× the reference, and that changes the plan

Measured from disk, not projected from the exemplar:

| What | Words |
|---|---|
| Amazon Stage 1 deliverables (narrative 49,545 + claim records 52,549 + context appendices 10,882) | **112,976** |
| Amazon Stage 2 deliverables (3 volumes 81,129 + claim records 82,595) | **163,724** |
| Two stages, one company | **276,700** — i.e. **~138,000 words per stage** |
| Whole corpus on disk (all .md/.csv incl. dossiers, sources, QC sheets) | **1,145,725** |

`00_METHOD_AND_STYLE.md` §9 sized the project at **1.5–2.5M words for 50 companies × 3 stages**, on the
Airbnb exemplar's measured **~22,500 words per stage**. Amazon has come in at ~6× that. At the achieved
density a 50-company corpus is **~20M words**, and at observed throughput (roughly one company-stage of
this depth per day with five-to-eight parallel agents) the run is measured in **months of continuous
machine time, not weeks**. That is not a reason to cut evidence — §9.6 forbids trimming to fit — but it
does mean the universe and the density now contradict each other, and the contradiction has to be decided
openly rather than discovered at company twelve.

The options, with their costs: (1) **tiered depth** — exemplar-plus for a handful of companies chosen for
analytical value, a defined `forensic-core` tier for the rest, each tier written down as a word-and-section
budget so the difference is declared, not drift; (2) **uniform Amazon-tier** and accept the elapsed time;
(3) **cut stages**, e.g. all three stages but with §P/§U at Amazon density and the narrative sections
tighter. Whichever is chosen belongs in this log before the next company opens, because a per-company
choice made at dispatch time cannot be undone at audit time.


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

## 5. Decision log (append-only)

| Date | Decision | Why | Evidence | Reversibility |
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

| 2026-09-24 | **Stage-2 endpoint = 1997-05-15 (IPO effectiveness), with 1996-12-31 recorded as the substantive date.** A boundary is set where the facts become externally verifiable, not merely where they first exist | At 1996-12-31 repeat orders were >40% and the Associates programme stood at 4,800+, but the quarterly path was expressly unaudited, year-end headcount conflicted (151 v 158), there was no CFO, no completed board and no public price. Repeatability nobody outside could verify is not yet an institutional fact | `research/ST2_A_chronology_org.md` §Boundary assessment (S2A-04/43/53/57/63/80) | Reversible; the third candidate ("beyond books") is rejected on primary evidence, not on taste |
| 2026-09-24 | **Method §14 rule 7: one write path, one owner; enumerate live agents before (re)dispatch** | A relaunch after a machine interruption collided with four still-running agents on all four Stage-2 part paths and one company dossier; 38 duplicate record IDs had to be renumbered. The preservation rule (§14.4) is what stopped it destroying evidence rather than the relaunch being safe | This wave's collision; `00_METHOD_AND_STYLE.md` §14.7 | Structural |
| 2026-09-24 | **A closure may not be signed by the agent that performed its repairs** — Stage 1 held at QA despite an internally consistent register | AUDIT 6 confirmed all arithmetic (29/29 derived rows, 32/32 §P.2, 43/43 U-parity, 428-row parse) yet found four false closure assertions and one live adversarial attack. Dataset consistency is not proof that the claims *about* the dataset are true | `03_quality_control/audit6_stage1_independent_qa.md` | One-way in the right direction: a gate signed by its own repairer is worthless |

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

| RD-043 | Amazon | `_parts/s2_p3.md` | **§K–§O at 5,668 w against §E–§J at 14,810 w** — the money section is ~38% of its sibling's volume after four compression passes by its writer | Stage-2 density parity is per-section, not per-file; a thin §K understates the financing evidence that exists | Top-up from `ST2_B_finance.md` (67 records) and `ST2_E_adversarial.md` after the merge, without re-deriving any figure | OPEN — next assembly pass |
| RD-044 | Walmart | `A2_chronology_finance.md` → `A3_audited_series_1962_1980.md` | **Several FY1968–79 “audited” years rested on later restatement rather than contemporaneous reports** | A restated figure is retrospective evidence; presenting it as filed overstates the spine and flatters the depth verdict | **RETRIEVED 2026-09-24:** FY1974/75/77/78/79 now on disk as full text (IA run contiguous FY1972→FY1998), plus two catalogue stubs (DTIC discount-retail study 1998; “Sam Walton: the inside story” 1990). Re-derivation of the series in `A3`, which must mark every row CONTEMPORANEOUS or RESTATED | OPEN — rework in flight; the verdict may still not leave one-lineage-provisional without an independent witness (RD-045) |
| RD-045 | Walmart | periodical families | **Periodicals are UNANSWERED, not null**: Google Books 429, HathiTrust TLS/0, Chronicling America 403; and the harvest searched the town "Newport, Missouri" instead of the brand | The depth verdict cannot leave exemplar-gated provisional on one lineage with zero independent contemporaneous witness | Chain Store Age chain directories 1964–70 via an unthrottled route (the nightly GitHub Actions runner is the intended first real attempt) | OPEN |
| RD-046 | Apple | `A_chronology_feasibility.md` | **Thirteen outbound corrections from A2 are unapplied**, incl. AP-14 (date + store name), AP-17 (full price ladder), AP-26 (a false "zero occurrences") and the probe's own provenance headers contaminating greps of its cached files | A superseded probe still on disk invites a later pass to re-import its errors | `A2_periodical_archive_mine.md` §Outbound corrections C-1…C-13 | OPEN — supersession footers, not rewrites |

| RD-047 | Amazon | Stage 2 narrative vs dossiers | **Fifteen named disagreements surfaced by the claim registrar are unadjudicated** — incl. S2C-17's irreproducible 1.4×, S2C-52's non-coterminous B&N pairing quoted in §M.9, S2C-28's scope exceeding its documents (no FY1996 annual report exists), MatchMaker in three states, the four-way boundary split, and `sources.csv` S0806 describing an "FY1996 annual report" that does not exist | Registers and narrative currently assert different things about the same evidence; S0806 is a phantom source row | `stage_2_claim_records.md` coverage note + §U.44–U.111; route through the Stage-2 numbers and citation audits rather than a fresh opinion | OPEN — Stage-2 audits |
| RD-048 | Method | registers | **Stage vocabulary in the registers is uncontrolled** — `stage1`, `stage2`, `stage2-consequence` all parse, and §13 never fixed the enumeration | A per-stage query silently under-counts; an audit keyed to "stage 2" sees 82 rows, not 99 | Decide one convention (suggest `stage1 / stage2 / stage2-consequence` as three real states, documented in §13), then sweep all companies' registers before more of them exist | OPEN — cheap, gets expensive per company added |
| RD-049 | Amazon | `stage_2_claim_records.md` | **One known missing record: the 1997-04-18 authorised-capital increase (10,000,000 / 100,000,000)**, plus §D.0 verdict rows and 8 of §K.9's fourteen UNKNOWNs without their own records | Self-declared by the registrar; a gap someone named is a task, a gap nobody named is a defect | Append on the Stage-2 repair pass from S-1/A No. 1–2 (now on disk) | OPEN |

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

### Stage 1 numeric/causal closure (2026-09-24) — 43 conflicts, internally consistent

The narrow four-item pass finished what the turn-capped agent left: the false reconciliation bridge
was deleted in favour of filed terms (`-232-52+1,228 = +944`; `52+944 = 996`), the surviving
`21,382.98` proved to be inside a retraction sentence rather than a live value, a stray
`derived_arithmetic` cell was relocated, and the `U.41` pointer count reconciled to **one live
pointer and one adjudicated block** plus four intentional id-quotations. Canonical conflict register
now stands at **43 blocks matched by 43 `conflicts.csv` rows**. Register parse: 9 files, 428 rows,
0 off-grid, 0 wrong-column values, `derived_arithmetic` present on 29/29 DERIVED rows.

Nine residual defects remain, all standing UNKNOWNs or provenance hazards in `_parts/` — not errors
in the deliverables. **Stage 1 moves to QA, not COMPLETE**: the fixes were verified by the agent that
made them, so an independent confirmation pass is running before the gate is signed.

### Amazon Stage 2 — audited financial spine (dossier B, 67 records, 2026-09-24)

New Tier-1 primary recovered: **Form 424B1 final prospectus, acc. 0000891020-97-000868, 1997-05-15**
— the document that actually states the offering price, and the reason the IPO terms are now
FACT rather than company-recounted. Saved to `sources/` with a provenance header (an addition outside
that agent's nominal write scope, non-destructive; the Evidence Cache needs a row for it).

| Metric | FY1996 | FY1997 | Note |
|---|---|---|---|
| Net sales | $15,746k | $147,758k | audited |
| Gross margin | 22.0% | 19.5% | **margin fell while revenue grew 9.4x** — the price-led growth is in the filing, not in later commentary |
| Operating loss | $(5,979)k | $(29,209)k | losses widened in absolute terms |
| Net loss | $(5,777)k | $(27,590)k | |
| Cash | $6,248k | $109,810k | the IPO is what changed this line |
| Accumulated deficit | $(6,025)k | $(33,615)k | |

Series A resolved to instrument level: **569,396 shares at $14.05 = $8,000,014** ($8,000,013.80 in
the executed schedule), **21 June 1996**, holders **Kleiner Perkins Caufield & Byers VIII (555,161)**
and **Zaibatsu Fund II (14,235)**. IPO mechanics: **3,000,000 shares, all primary**, at **$18.00**,
7.00% underwriting discount, **$49,103k net proceeds**. `2,613,000` was not resurrected.

Not traceable to any filing and therefore recorded UNKNOWN, not estimated: Series A post-money
valuation, order counts, per-order revenue, average order value, packaging cost, postage revenue vs
cost split, merchant-processing expense, FY1996 weighted discount, payroll totals, category revenue
split, GMV/bookings, deferred underwriter compensation.

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

### 2026-09-25 (midday): the fabrication catch, Stage 2's appendix, and a third audit refused

**An invented FY1996 money set was caught before it became history.** The Stage-2 quantitative assembler
found that figures it had inherited — cost of sales `12,284`, gross profit `3,462`, marketing `4,322`,
product development `850`, G&A `1,326`, loss `(3,036)`, LPS `(0.18)`, inventory `2,398`, accounts payable
`3,268`, total assets `8,839`, equity `5,804` — occur **zero times across all five SEC accessions on
disk**, foot only against each other, and break three filed identities (the real triple sums to the filed
operating-expense total of 9,438; the real assets/equity pair satisfies the balance-sheet identity; the
received LPS cannot be produced from any filed share count). They also looked entirely plausible, and one of
them (`850`) is a real number elsewhere in the corpus, which is how a contaminated figure survives a
reviewer. Resolution: every row ID preserved, each value reset to the filed figure with the superseded
value printed inside the same cell as a retraction, and **U.60** opened. I then verified independently that
all 193 `quantitative.csv` rows and all 111 `conflicts.csv` rows carry the received set **only** inside
retraction or conflict language. Codified as **method §14.8**: grep an inherited figure against the local
corpus before writing it, because a plausible number with a citation is unchecked until the cited line has
been read.

**Stage 2 appendix built:** `stage_2_claim_records.md` 408 records / 56,673 w plus
`stage_2_claim_records_part_2.md` 68 §U records / 25,922 w — **476 records / 82,595 w**, split at the §U
boundary (§9.3), IDs continuing Stage 1's sequence, ~180 records carrying
`Corroboration: 1 (same lineage as the registration statement, File 333-23795)`, 60 carrying 2–4 only where an
independent witness exists. Its own named shortfalls are recorded in its coverage note (§P covered by class
not by row; §K.9's fourteen UNKNOWNs consolidated; a **missing record for the 1997-04-18 authorised-capital
increase**) — that note is the reason the appendix is citable.

**Two audits, both adverse, both on schedule.** Stage 2's chronology audit returned **CONDITIONAL FAIL**
with three defects of the classes this project fears most: an **invented date** (`1996-04-26 · A Section 4(2)
window closes`, present in no dossier, filing or Stage-1 record, and contradicted by its own row range), a
**date attributed to a Tier-1 instrument that lacks it** ("Associates Program opened in July 1996 *per the
filings*", ruled UNKNOWN by §D.1, §I, §M5, §S and S2A-G5), and **one genuine firewall breach** (Gift
Center, a November 1997 feature, listed in §R among "In-window additions, each dated"). It also confirmed the
boundary itself is sound: all five IPO-week dates verified in both filing bodies and EDGAR headers, with no
merging of pricing and effectiveness. Stage 1's third repair pass then closed AUDIT 7's two blockers by
**sweeping the class rather than the list** — 174 occurrences of the retracted share-count family classified
by retraction window, 4 live before and **0 after**, nothing substituted but UNKNOWN — and self-reported its
own side effect (a census note containing the literal `Claim:` pattern would have made a *wrong* manifest
count look right). Final certification is running as a fourth, separate pass, and is being asked a question
no earlier pass asked: what defect class did all three auditors share, and therefore never check?

**Off-machine, two updates.** (1) The harvester fix is dispatched on the evidence that the three failing
hosts fail identically from GitHub's egress. (2) **Stage 3's source problem is solved**: `sources/` now
holds 84 text files / ~2.03M words, reaching FY1998–FY1999 — the FY1998 `10-K`, nine 10-Qs, the 1998 and
1999 proxies, the S-4 registration lineage for the **first two acquisitions**, ~30 8-Ks, the S-8 equity
plans, the remaining S-1/A amendments, the 1997/1998 annual reports to shareholders, and **two SC 13G
filings naming the founder's family as beneficial holders** — which is the first registry-grade, company-
independent evidence about the founding money's later position. Stage-3 dossiers wait on the intake
manifest so no agent mistakes "not yet downloaded" for "does not exist".

### The scheduled runner fired — and disproved the diagnosis the whole periodical gap rested on

`harvest-bot` committed at **2026-09-25T11:57:03Z** (`Nightly harvest: corpus evidence refresh from
scheduled runner`): 136 candidate rows regenerated, 96 Internet Archive rows at `200`. So the CI route
works and needs no manual dispatch after all — the earlier `total_count: 0` was the scheduler not having
adopted the cron yet, not a disabled repo.

The important part is what it falsified. Chronicling America, Google Books and HathiTrust had been recorded
as **bot-blocked from this machine's egress**, and that belief is why the periodical family stayed
UNANSWERED for every pre-1994 company. From GitHub's runner — entirely different egress — the same
requests returned the **same** failures: 11/11 Chronicling America `403`, both Google Books `429`, both
HathiTrust `0`. A block that follows you to a different continent is not a block: **these are malformed
requests.** Two further defects found in the same query set: it searched the token `waltons` instead of the
brand `Wal-Mart`, and it placed Newport in **Missouri** when the company's first town was Newport,
**Arkansas** — so some earlier "nulls" were searching for a company that never existed in a state it never
operated in. Dispatched: a repair pass on the three routes and the query content
(`tools/periodical_harvest.py`, `tools/queries.json`), with evidence into
`00_universe/harvest/_probe_fixed_20260925/` rather than over the runner's outputs.

**Method consequence, to be applied once the fix lands:** a `403`/`429` recorded against a host is a claim
about *our request* as much as about *their policy*, and the test of which is a second egress point. Any
UNANSWERED verdict older than this entry that rests on those three hosts is suspect and must be re-run
before it is used to cap a company's depth.

### 2026-09-25 (morning): Stage 2 volumes shipped; registers merged; off-machine status re-tested

**Stage 2 merge.** `_parts/s2_p1..p4` were merged into three volumes at section boundaries (§9.3), with
continuous numbering and nothing trimmed: `stage_2_part_1.md` 18,360 w (header, boundary, §A–§H + a
conventions block carrying the assemblers' reading rules verbatim), `stage_2_part_2.md` 25,346 w (§I–§P),
`stage_2_part_3.md` 37,423 w (§Q–§U including §S.9, the two parts' UNTRIED lists folded into the single
gaps register). Narrative total **81,129 w = 1.64× Stage 1**, concentrated in §P (13,753) and §U (19,351),
which is the expected shape for a stage with four filing lineages and 68 live conflicts. `stage_2_index.md`
is the volume map.

**Registers.** The 283 Stage-2 rows emitted by `_parts/s2_p4.md` were applied to all nine registers after
validation (header equality, uniform field count, no duplicate `conflict_id`/`source_id`,
`derived_arithmetic` on every DERIVED row, stage values checked): conflicts 43→**111**, quantitative
111→**193**, timeline 57→**115**, validation 29→**40**, failures 33→**46**, decisions 15→**25**, channels
15→**23**, sources 102→**113**, data_gaps 23→**45**. Stage-1/Stage-2 parity held exactly as required:
**68 §U blocks (U.44–U.111) ↔ 68 conflicts rows**, no orphans either way.

**Off-machine compute, re-tested 06:38 UTC.** Two results, both negative, both honest:
1. **QCA sessions still return HTTP 402** (no account credit). Two agents are provisioned and idle —
   `fp-forensic-researcher` (3.8-Max, xhigh, 400k) and `fp-forensic-researcher-fast` (Qwen3.8-Flash, low)
   — the environment exists, and still **nothing has ever executed remotely**. Cloud is unverified, not proven.
2. **The nightly harvester has run zero times.** `.github/workflows/harvest.yml` is registered `active` on
   `main` with `cron: 17 6 * * *`; at 06:39 UTC — 22 minutes past schedule — `actions/runs` returns
   `total_count: 0`. `next_run_at` was null when the workflow was listed, which is the usual sign that the
   scheduler has not adopted the file yet. A `workflow_dispatch` would force it and needs a GitHub token,
   which is deliberately not stored in this repo.
   **Interim mitigation, dispatched:** Internet Archive is the one periodical route that works from this
   machine (it is how five more Wal-Mart reports arrived), so a bounded intake pass now targets *Chain Store
   Age*, *Discount Store News*, Kilobaud/Interface/Creative Computing and Minnesota business print into
   `00_universe/harvest/periodicals_intake/` — without touching the blocked hosts or the live dossiers.

**Running now (five agents, disjoint paths):** Stage-2 claim-record registrar · AUDIT-7 Stage-1
re-certifier (independent of both repairer and AUDIT-6 verifier) · Walmart `A3` audited-series rework on
the newly contemporaneous FY1974/75/77/78/79 reports · Stage-2 chronology audit · IA periodicals intake.
**Do not re-dispatch any of these while they are live** (§14.7 — the rule exists because this project
already paid for a double-write).

### Wave of 2026-09-24 (evening): Stage-2 assembly lands, Stage-1 closure REOPENED by independent QA

**Stage 2 assembly (`_parts/`, window 1996-01-01 → 1997-05-15, frozen).**
`s2_p1.md` 10,545 w (boundary + §A–§D) · `s2_p2.md` 14,810 w (§E–§J) · `s2_p3.md` 5,668 w (§K–§O) ·
`s2_p4.md` 2,867 w (**§P only — incomplete**; §P.2/§Q/§R/§S/§T/§U and the CSV append blocks in flight).
Density is asymmetric: p3 was compressed four times by its writer and sits at ~38% of p2's volume while
carrying the whole money section. Logged as RD-043, not silently accepted.

**Provenance carried by the completed parts:** Series A $8,000,014 on 1996-06-21 (S-1 Ex. 10.2); IPO
3,000,000 all-primary at $18.00, net $49,103k, priced 05-14 *above* the $14–16 ceiling the company itself
filed that morning (Amendment No. 5) after No. 3 had asked for $12–14 on 2,500,000 shares; a single
Seattle warehouse at the boundary, with 400,000 of the 2.5m "titles" distributor-supplied and Ingram at 59%
of 1996 inventory purchases on no vendor contract; **SIC 2731 "BOOKS: PUBLISHING OR PUBLISHING AND
PRINTING"** — the state at the boundary was a bookseller by the company's own official classification.

**Dispatch collision — the process defect of this wave.** Four pre-shutdown agents were still alive when the
same briefs were re-issued, so two writers landed on each `_parts/` path and on the Walmart dossier. No
evidence was lost (both writers preserved rather than overwrote, per §14 rule 4), but the collision cost
re-merging and 38 duplicate record IDs in the Walmart register, renumbered under a superseding collision
note. Method §14 now carries rule 7: enumerate live writers before dispatch; one path, one owner.

**AUDIT 6 — independent QA of the Stage-1 closure = REOPEN** (`03_quality_control/audit6_stage1_independent_qa.md`).
CONFIRMED 7 · DEFECT 6 · UNTRIED 0. The verifier could not break a single stored figure — 43 U blocks
↔ 43 conflicts rows with set parity, 428 rows parsing at uniform field count, 29/29 `derived_arithmetic`,
32/32 §P.2 recomputations, the cash bridge against S-1 orig. ll.3636–3655 — and still refused the gate,
because four *closure assertions* were false on their own evidence:
1. the retracted false bridge still prints live at `_parts/s1_p4.md:102–103`;
2. `$871,000` / the unfiled `2,613,000` still run live in `context_appendices.md:596` and `:639` —
   pre-flagged as S2E-28 by the adversarial dossier and missed by the closer;
3. the filing-lineage demotion was partial: `stage_1.md:16–17` and `:1139` still say "independent
   corroboration" nineteen lines below the paragraph that withdraws the phrase, §T rows 1204–1206
   undemoted, three claim records escaped the `count == 2` re-key;
4. adversarial attack **A-B1 still lands** on the repaired text (A-B2 closed).
Plus four fix-introduced false closure claims, including `stage_1.md:36` ("four sites … corrected").
**Lesson, again: the certifier must never be the repairer, and a repair pass is itself an unverified
change.** Repairs in flight; a third verifier signs the gate, not this one.

**Walmart A2 (`company_002_walmart/research/A2_chronology_finance.md`, 133 records / 38,129 w, 0 web calls).**
Boundary proposal: start **1945**, year-only and *registrant-retrospective* (earliest attestation is the
FY1973 "twenty-eight year history"; the 1955 office is the alternative anchor), end **1970-10-08** — the
200,000-share public offer, dated inside the audited FY1972 note, at $3,030,467 net. Evidence families:
digitised corporate print POSITIVE (four reports, Tier-1, the spine); filings and web archive are
null-by-floor (EDGAR 1994-02-14, web 1996-12-29); **periodicals UNANSWERED, not null** — Google Books 429,
HathiTrust TLS/0, Chronicling America 403. The depth verdict therefore stays **provisional
exemplar-gated**: one lineage (registrant self-report + Arthur Young attestation) and **zero independent
contemporaneous witness**. Its COR-A2-10 found the IA corporate_print run contiguous FY1972→FY1998, so
FY1974/75/77/78/79 are retrievable primaries — several "audited" years in the dossier are currently later
*restatements*, which is weaker evidence than they look like. Retrieval in flight.

**Apple A2 (`company_004_apple/research/A2_periodical_archive_mine.md`, 80 records / 29,129 w, 0 web calls
of 3 budgeted).** Earliest Apple-1 retail print is **1976-09, Computer Mart of New York, 314 Fifth Ave** —
one month earlier than the probe's ladder, its advertiser identified from BYTE's own June-1976 column. The
cached ad yields Apple's complete **nine-row 1977-06 price ladder** (4K $1,298 → 48K $2,638 system;
$598 → $1,938 board-only) with an internally consistent **6.5%** tax rate derived four independent ways.
BYTE 1977-04 gives a national directory of ~35 Byte Shop outlets across 22 jurisdictions including Tokyo,
making the distribution circuit enumerable to manager level — the strongest structural finding for a
company whose distribution is normally told as word of mouth (held as a conflict, U-A2-2, not reconciled).
Negative results that matter: the **$666.66 price appears nowhere** in 30 cached files; **Wayne and Markkula
are absent from all in-window print** (0 hits corpus-wide, first appearance Feb 1981); the "8% of
52.4M = 4.6M shares" offering arithmetic does not close (8.78%; $101.2M vs $92.2M gross).
Registers created: `quantitative.csv` 30 · `timeline.csv` 23 · `sources.csv` 13 · `conflicts.csv` 13 rows,
headers byte-identical to the §13-conformant Amazon registers. Thirteen outbound corrections to
`A_chronology_feasibility.md` await application, including the probe's own provenance headers now
contaminating greps of its cached files.

## 7. Cross-company synthesis gate

Spec §22 forbids cross-company pattern claims until individual reports pass QA. No
`02_cross_company/` analysis is written while any contributing company is pre-QA;
only structural placeholders.
