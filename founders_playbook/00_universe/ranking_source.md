# Ranking Source Dossier — 2026 Fortune 500, Top 50 (frozen universe)

Level-3 Universe Clerk. Retrieval date for everything in this file: **2026-09-23**.
Rule applied throughout: only URLs listed in the Retrieval log were read, and nothing is
asserted that is not in one of them. `UNKNOWN` is used wherever evidence was not recovered.

---

## Edition confirmed

**Edition: the 2026 Fortune 500 — the 72nd annual list. Publication date: June 3, 2026.**

The full top-50 ordering previously established by the team was **independently confirmed, all 50
ranks, against the publisher's own data**. No rank differs.

Evidence is the embedded machine-readable dataset on Fortune's live ranking page
(`https://fortune.com/ranking/fortune500/`, HTTP 200). The page's `__NEXT_DATA__` JSON carries a
`franchiseSearch.items` array of **1,000 ranked records**, each with `rank`, `name` and a `data`
object containing `Revenues ($M)`, `Profits ($M)`, `Headquarters City`, `State`, `Industry`,
`Sector`, `Employees`, `Market Value ($M)` and rank-change flags. Rows 1–50 in
`fortune_top_50_2026.csv` were produced by filtering that array on `rank <= 50` — **no manual
transcription of names or numbers occurred**, and the financial columns the team had been missing
are present in that payload.

Page-level metadata retrieved: `canonicalUrl = /ranking/fortune500/2026`, `year = "2026"`,
`databaseId = 507`, `dateGmt = 1780477822` (**2026-06-03T09:10:22Z**),
`modifiedGmt = "2026-06-03 05:10:23"`.

Second, independent confirmation of the top ten and the edition, from the Fortune-issued press
release reproduced on Yahoo Finance, dated **June 3, 2026**:

> "NEW YORK, June 3, 2026 /PRNewswire/ -- Today, Fortune announced the Fortune 500™ ranking for
> 2026, the 72nd year of the iconic annual list of the largest corporations in the United States,
> ranked by revenue for the 2025 fiscal year."
>
> "Amazon has dethroned Walmart as No. 1 on the Fortune 500, ending the retailer's 13-year reign
> atop the list."
>
> "Alphabet moved up two spots to No. 5 on the Fortune 500"
>
> "THE TOP TEN COMPANIES ON THE 2026 FORTUNE 500 LIST ARE: Amazon, Walmart, UnitedHealth Group,
> Apple, Alphabet, CVS Health, Berkshire Hathaway, McKesson, Exxon Mobil, Cencora"

That release's top-ten sequence matches ranks 1–10 of the embedded dataset exactly (including
Alphabet at 5, McKesson at 8, Cencora at 10). It also gives list-level context used in the CSV:
"$21.0 trillion (up 5%) in revenues, $2.1 trillion (up 12%) in profits, and $55 trillion (up 19%)
in market value, while employing 30.5 million people worldwide" and "The revenue threshold for
making the Fortune 500 list was $7.5 billion this year."

### DISCREPANCY — recorded, not smoothed

**Wikipedia's "Fortune 500" article contains a table headed "Fortune 500 list of 2026" that
disagrees with Fortune's own ordering at five of the first twenty ranks, and disagrees on one
revenue figure by roughly $44 billion.** Retrieved raw (HTTP 200, 210,502 bytes,
`oldid=1372037153`, page "last edited on 29 August 2026, at 23:56 (UTC)"). Its rows 5–20 read:

| Rank | Wikipedia table | Fortune's own data | Fortune revenue |
|---|---|---|---|
| 5 | McKesson Corporation, $403.4bn | Alphabet (Google) | $402,836M |
| 6 | Alphabet Inc., $402.8bn | CVS Health | $402,067M |
| 7 | CVS Health, $402.1bn | Berkshire Hathaway | $371,444M |
| 8 | Berkshire Hathaway, $371.4bn | **McKesson** | **$359,051M** |
| 12 | Costco, $275.2bn | **JPMorgan Chase** | **$280,345M** |
| 19 | Chevron, $189.0bn | **Bank of America** | **$191,567M** |
| 20 | Ford Motor, $187.3bn | Chevron | $189,031M |

Why the Wikipedia table is treated as erroneous rather than as a competing account:

1. **McKesson's revenue.** Fortune's ranking figure is $359,051M, and McKesson's own 10-K XBRL
   `RevenueFromContractWithCustomerExcludingAssessedTax` for the fiscal year ended **2025-03-31**
   is **$359,051M** — an exact match. Wikipedia's $403.4bn matches neither source.
2. **Internally inconsistent.** Wikipedia's own table omits JPMorgan Chase ($280,345M) and Bank of
   America ($191,567M) entirely, although those revenues exceed several figures Wikipedia does
   list (Costco $275.2bn; Chevron $189.0bn). A revenue-ranked list cannot legitimately skip them.
3. **Its citation points at the prior edition.** The table's reference is listed as
   *"Fortune 500 List of Companies **2025**", retrieved Aug 3, 2026*.
4. The article carries the maintenance banner *"This article needs to be updated … (July 2026)"*.

**Resolution: Fortune's ordering is retained for all 50 rows**, on the publisher's own data plus
McKesson's 10-K. Wikipedia is used in this dossier only where named explicitly. Ranks 21–50 do not
appear in the Wikipedia article at all, so no comparison was possible there.

---

## Methodology as stated by the publisher

All quotes below are verbatim from the `franchise.methodology` array embedded in
`https://fortune.com/ranking/fortune500/` (retrieved 2026-09-23). Fortune structures the
methodology as titled sections; section names are theirs.

**Overview**
> "Companies are ranked by total revenues for their respective fiscal years. Included in the
> survey are companies that are incorporated in the U.S., operate in the U.S., and file financial
> statements with a government agency. This includes private companies and cooperatives that file
> a 10-K or a comparable financial statement with a government agency, and mutual insurance
> companies that file with state regulators. It also includes companies that file with a
> government agency but are owned by private companies, domestic or foreign, that do not file such
> financial statements. Excluded are private companies not filing with a government agency;
> companies incorporated outside the U.S.; and U.S. companies consolidated by other companies,
> domestic or foreign, that file with a government agency. Also excluded are companies that failed
> to report full financial statements for at least three-quarters of the current fiscal year.
> Percent change calculations for revenue, net income, and earnings per share are based on data as
> originally reported. They are not restated for mergers, acquisitions, or accounting changes. The
> only changes to the prior years' data are for significant restatement owing to reporting errors
> that require a company to file an amended 10-K."

**Revenues** (this is the definition-and-consolidation statement the task asked for)
> "Revenues are as reported, including revenues from discontinued operations when published. If a
> spin-off is on the list, it has not been included in discontinued operations. Revenues for
> commercial banks include interest and noninterest revenues. Revenues for insurance companies
> include premium and annuity income, investment income, and capital gains or losses, but exclude
> deposits. Revenue figures for all companies include consolidated subsidiaries and exclude excise
> taxes. Data shown are for the fiscal year ended on or before Jan. 31, 2026. Unless otherwise
> noted, all figures are for the year ended Dec. 31, 2025."

**Profits**
> "Profits are shown after taxes, extraordinary credits or charges, cumulative effects of
> accounting changes, and noncontrolling interests (including subsidiary preferred dividends), but
> before preferred dividends of the company. Figures in parentheses indicate a loss. Profit
> declines of more than 100% reflect swings from 2024 profits to 2025 losses. Profits for real
> estate investment trusts, partnerships, and cooperatives are reported but are not comparable with
> those of the other companies on the list because they are not taxed on a comparable basis.
> Profits for mutual insurance companies are based on statutory accounting."

**Employees**
> "The figure shown is a fiscal year-end number as published by the company in its annual report.
> Where the breakdown between full- and part-time employees is supplied, a part-time employee is
> counted as one-half of a full-time employee."

**Credits**
> "This Fortune 500 Directory was prepared under the direction of list editor Scott DeCarlo. Income
> statement and balance sheet data provided by the companies were reviewed and verified against
> published earnings releases, 10-K filings, and annual reports by accounting specialist Rhona
> Altschuler and research analyst Aris Stavropoulos. We used data provided by LSEG and S&P Global
> Market Intelligence to calculate total return and market capitalization."

Points the task asked to check, restated against the quoted text:

- **Incorporation / operation requirement: both.** A company must be *incorporated in the U.S.*,
  *operate in the U.S.*, *and* file financial statements with a government agency. Companies
  incorporated outside the U.S. are excluded; U.S. companies consolidated by another filing company
  are excluded.
- **Public reporting, not public ownership.** Privately held companies and cooperatives are
  included if they file; mutual insurers qualify via state-regulator filings. "Publicly reporting
  revenue" is the operative condition, not listing on an exchange.
- **Fiscal-year basis: fiscal 2025 — confirmed twice.** The methodology fixes the window as
  "the fiscal year ended on or before Jan. 31, 2026," with a default of the year ended
  Dec. 31, 2025; the June 3, 2026 press release states the list is "ranked by revenue for the 2025
  fiscal year." Both agree. Company-level exceptions are recorded in the CSV (e.g. McKesson's
  ranked year ended 2025-03-31; Nvidia's ended 2026-01-25).
- **Revenue definition:** as reported, including discontinued operations where published,
  including consolidated subsidiaries, excluding excise taxes; bank revenues = interest +
  noninterest revenues; insurance revenues = premiums/annuity income + investment income + capital
  gains or losses, excluding deposits. Spin-offs on the list are *not* inside discontinued
  operations.
- **Restatement policy:** percent changes use data "as originally reported"; prior-year data is
  changed only for a restatement requiring an amended 10-K.

---

## Retrieval log

Every network retrieval made in this pass, and what it yielded. Retrieval date for all:
**2026-09-23** (all via direct HTTP with a desktop or descriptive agent User-Agent).

| # | URL retrieved | Result | What it yielded |
|---|---|---|---|
| 1 | `https://fortune.com/ranking/fortune-500/` | **404** | Dead guess; not used. |
| 2 | `https://fortune.com/ranking/f500/2026/` | **404** | Dead guess; not used. |
| 3 | `https://fortune.com/ranking/fortune500/` | **200**, 1,386,785 B | **PRIMARY SOURCE.** Embedded `__NEXT_DATA__` → `franchiseSearch.items` (1,000 records): rank, name, `Revenues ($M)`, `Profits ($M)`, `Headquarters City`, `State`, `Industry`, `Sector`, Employees, Market Value, "Global 500" flag, "Founder is CEO" flag, rank-change flags. Also `franchise.methodology` (8 titled sections, quoted above), `franchise.description`, `franchise.highlightedCompanies`, `franchise.dateGmt` = 2026-06-03T09:10:22Z, `year` = 2026, `canonicalUrl` = `/ranking/fortune500/2026`. |
| 4 | `https://fortune.com/ranking/global500/` | **200**, 760,758 B | 2026 Global 500 franchise: `year` = 2026, `dateGmt` = **2026-07-28T08:00:00Z**, description text (quoted in the change log), and the top 500 records (ranks 1–6 extracted). |
| 5 | `https://en.wikipedia.org/wiki/Fortune_500` | **200**, 210,502 B | Confirmed sections History / Methodology / Influence / Overview. Contains a 20-row table headed "Fortune 500 list of 2026" that **contradicts** Fortune (see Edition confirmed). Cites *"Fortune 500 List of Companies 2025"*. Banner: article needs updating (July 2026). `oldid=1372037153`, last edited 2026-08-29 23:56 UTC. Used only as the dissenting source; no CSV field is sourced from it. |
| 6 | `https://finance.yahoo.com/markets/stocks/articles/amazon-claims-no-1-spot-100000251.html` | **200**, 860,048 B | Fortune-issued PR Newswire release, **June 3, 2026**. Confirms publication date, 72nd year, "revenue for the 2025 fiscal year", Amazon/No. 1, the 13-year Walmart streak, Alphabet at No. 5, the top ten by name, list totals, $7.5bn cutoff. Independent of Fortune's own site copy. |
| 7 | `https://www.sec.gov/files/company_tickers.json` | **200**, 800,821 B, 10,461 records | Authoritative name→CIK resolution for all registrants used below. Found "AMAZON COM INC" = CIK 1018724 and confirmed **State Farm is absent** from the SEC company index. |
| 8 | `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json` — 49 CIKs (all 50 companies except State Farm) | **200** (one per company) | 12-month `us-gaap` facts ending on or before 2026-01-31: `Revenues`, `RevenueFromContractWithCustomerExcludingAssessedTax`, `RevenueFromContractWithCustomerIncludingAssessedTax`, `SalesRevenueNet`, plus `NetIncomeLoss` / `ProfitLoss`. Basis for the exact-match corroboration on 38 revenue rows and 48 profit rows. |
| 9 | `https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/<TAG>.json` — tags `InterestIncomeOperating`, `InterestAndDividendIncomeOperating`, `NoninterestIncome`, `Revenues`, `NetIncomeLoss`, `RevenueFromContractWithCustomerExcludingAssessedTax` for CIKs 19617, 70858, 831001, 354950, 310522, 1534701, 1510295, 1026214, 886982, 72971, 895421, 1035002, 2115436, 1140859 | **200** (404 where a registrant uses no such tag — recorded, not filled) | Bank/GSE revenue components; Home Depot and Cencora periods outside the first window. |
| 10 | `https://data.sec.gov/api/xbrl/companyfacts/CIK0000034088.json` (Exxon Mobil Corp, legacy registrant) | **200** | `Revenues` 2025-12-31 = **332,238.0M** and `NetIncomeLoss` = **28,844.0M** — both equal to Fortune's ExxonMobil Holdings figures exactly. Needed because the new holding-co registrant (2115436) returned no comparable annual facts. |
| 11 | Same companyfacts endpoint for CIKs 886982, 895421, 310522, 1026214 | **200** | Full tag dumps used to identify the components summing exactly to Fortune's Goldman ($80,373 + $44,724 = $125,097) and Morgan Stanley ($59,063 + $60,599 = $119,662) figures, and Freddie Mac ($129,820 + $1,868 = $131,688). |
| 12 | `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=...&type=10-K&count=8` | **503** / no parseable rows | Attempted filing-period cross-check for Cencora and Home Depot; superseded by #9, which answered both. Not cited for any claim. |
| 13 | `https://data.sec.gov/submissions/CIK0001018068.json` | **200**, but entity = "AVIS GREGORY M" | Discarded: a CIK recalled from memory was wrong. Corrected by the lookup in #7. Logged because it is the reason all CIKs in this run were resolved by name lookup rather than recollection. |
| 14 | `https://en.wikipedia.org/w/api.php?action=query&...&titles=<50 titles>` | **200**, body = *"You are making too many requests to the API."* | Discarded; no data taken. |
| 15 | `https://en.wikipedia.org/w/index.php?title=<Article>&action=raw` — 50 company articles (Amazon (company), Walmart, UnitedHealth Group, Apple Inc., Alphabet Inc., CVS Health, Berkshire Hathaway, McKesson, ExxonMobil, Cencora, Microsoft, JPMorgan Chase, Costco, The Cigna Group, Cardinal Health, Nvidia, Meta Platforms, Elevance Health, **Centene Corporation** (the bare "Centene" title returned a 33-byte stub), Bank of America, Chevron Corporation, Ford Motor Company, General Motors, Citigroup, Home Depot, Fannie Mae, Kroger, Verizon, Phillips 66, Marathon Petroleum, StoneX Group Inc., State Farm, Freddie Mac, Humana, AT&T, Goldman Sachs, Comcast, Wells Fargo, Morgan Stanley, Valero Energy, Dell Technologies, Target Corporation, Tesla, Inc., The Walt Disney Company, Johnson & Johnson, PepsiCo, Boeing, United Parcel Service, RTX Corporation, FedEx) | **200**, 49 articles full + Centene | The sole evidence base for the Feasibility register's earliest-origin dates, founder names and origin-structure flags (spin-off / holding-company / GSE / Blue Cross / merger-of / renamed markers read from each infobox and body). |

Not retrievals: two web searches were run to *locate* a dated news account of the No. 1 change; they
surfaced the June 3, 2026 Yahoo/PR-Newswire item (#6, subsequently retrieved) and a
2026-07-29 republication of the Global 500 story. Nothing is cited from the search results
themselves.

---

## Corroboration status

| Column | Source of record | Second source | Count |
|---|---|---|---|
| `rank`, `company` | Fortune's embedded dataset | PR Newswire release for ranks 1–10 by name; ranks 11–50 single-source | 10 corroborated / 40 single-source |
| `revenue_usd_millions` | Fortune's embedded dataset | SEC 10-K XBRL | **38** exact to a single tagged figure; **7** exact as the sum of two tagged components (JPMorgan, Bank of America, Citigroup, Freddie Mac, Goldman Sachs, Wells Fargo, Morgan Stanley); **5 not corroborated** (Fannie Mae residual 551; Phillips 66 +4,184; Marathon +2,523; Valero −6,748; State Farm has no SEC record) |
| `revenue_fiscal_year` | Period end of the matched SEC 10-K fact | same SEC filing | **49** confirmed; **1** UNKNOWN (State Farm) |
| `profit_usd_millions` | Fortune's embedded dataset | SEC 10-K XBRL `NetIncomeLoss`/`ProfitLoss` | **48** exact; **2** not corroborated (Ford: −8,182 vs −8,162; State Farm: no SEC record) |
| `hq_city`, `hq_state` | Fortune's embedded dataset | Wikipedia infobox | **23 of 50** city strings match directly; for the rest the infobox stores a building or campus name ("Apple Park", "Blackstone Plaza", "270 Park Avenue") so no string comparison was possible — this is a comparison failure, not a contradiction. **One real disagreement: PepsiCo** (Fortune "Purchase" vs infobox "Harrison", New York). State agrees in every comparable case. |
| `fortune_industry`, sector | Fortune's embedded dataset (`Industry`, `Sector`) | none — these are Fortune's own editorial labels | **50 of 50 single-source by nature**; no external source can define Fortune's taxonomy |

**How many companies rest on a single source?** For the ranking-critical numeric columns, one:
**State Farm (rank 32)** — no SEC filings exist for it, so its revenue, profit and fiscal-year basis
rest on Fortune alone (confidence `Medium`). **Five further rows are only half-corroborated**:
Fannie Mae (26), Phillips 66 (29), Marathon Petroleum (30) and Valero (40) have exact profit
corroboration but no exact revenue corroboration, and Ford (22) has exact revenue corroboration but
no exact profit corroboration. All five are held at `Medium`. The remaining **44 rows** have both
financial columns reconciled to the company's own 10-K to the dollar and carry confidence `High`.

Independence note, per house method: Fortune's ranking page and Fortune's press release are **one
source, not two**, for the ranking itself. They were used for different purposes — the page for the
data, the release for the publication date and stated fiscal basis — and SEC 10-K data is the
genuinely independent check on the numbers.

---

## Universe change log

**This list is frozen for this research run.** The 50 rows in
`E:\founder's playbook\founders_playbook\00_universe\fortune_top_50_2026.csv` constitute the
research universe. Later reports may not add, drop, re-rank or restate a company; if a source
disagreements, it is recorded against the frozen row.

Edition frozen: **2026 Fortune 500 (72nd annual list), published June 3, 2026, ranking fiscal-2025
revenue.**

### The No. 1 change in this edition — Amazon overtakes Walmart

Fortune's own page description (retrieved 2026-09-23):
> "The Fortune 500, in its 72nd year, ranks the biggest U.S. companies by revenue. And this year,
> for the first time in more than a decade, it has a new No. 1, as Amazon ends Walmart's 13-year
> winning streak."

Fortune's company highlight blocks on the same page:
> Amazon: "Amazon, which debuted on the Fortune 500 in 2002, snared the top spot on the strength of
> 12% year-over-year revenue growth. It also posted record profits as its juggernaut AWS
> cloud-services business expanded its margins."
>
> Walmart: "Walmart fell to No. 2 after 13 years at No. 1. Doug McMillon, the CEO who presided over
> most of that streak, retired in January. But the giant retailer's earnings hit an all-time high
> last year, and its share price has soared as well."

Dated second source (June 3, 2026, same day as publication):
> "Amazon has dethroned Walmart as No. 1 on the Fortune 500, ending the retailer's 13-year reign
> atop the list. The e-commerce and cloud giant surpassed $700 billion in revenue in 2025 with a 12%
> year-over-year jump, marking a stunning rise for a company that debuted at No. 492 just over two
> decades ago. While Walmart fell to No. 2 for the first time since 2012…"

The gap: Amazon $716,924M vs Walmart $713,163M — **$3,761M**, i.e. 0.5% of Walmart's revenue.
Amazon's rank-change field is `+1` ("Gained in Rank" = yes). Both companies' figures match their
own 10-Ks exactly.

**Unresolved disagreement inside Fortune's own copy.** The Fortune 500 page and the press release
say **13 years** (Walmart No. 1 from 2013 through 2025; "first time since 2012"). The Global 500
page, published 2026-07-28, says **12-year run**. Fortune's F500 highlight text says Walmart "fell
to No. 2 after 13 years at No. 1." Both statements are recorded; the clerk did not reconcile them,
and neither is used for any CSV field.

### Global 500 consequence

From `https://fortune.com/ranking/global500/` (2026 edition, page dated 2026-07-28T08:00:00Z):
> "The corporations on our annual list of the world's 500 largest companies combined to generate
> $43.1 trillion in revenue in 2025, up 3.2% from the previous year. Together, they employ 70.2
> million people, and their revenue represents more than one-third of the world's GDP. The Global
> 500 earned $3.39 trillion in profit in its most profitable year ever. **Amazon topped our annual
> ranking of the biggest companies in the world by revenue, ending Walmart's 12-year run.** AI
> chipmakers Nvidia and Taiwan Semiconductor leaped, respectively, 38 spots to No. 28, and 44 spots
> to No. 82. The semiconductors and electronic components industry's rise also brought
> Netherlands-based ASML onto the list at No. 45."

Retrieved Global 500 top six (same page's dataset): 1 Amazon $716,924M; 2 Walmart $713,163M;
3 State Grid $555,371.4M (Beijing); 4 UnitedHealth Group $447,567M; 5 Saudi Aramco $445,528.7M
(Dhahran); 6 Apple $416,161M. So the U.S. swap propagated to the global list with the same
ordering, and every company in our frozen top 50 also carries Fortune's `Global 500 = yes` flag.
Nothing beyond this is claimed: the source states the streak ended but gives no further consequence
for Walmart's or Amazon's subsequent global position, and no independent second source for the
Global 500 change was retrieved in this pass (the 2026-07-29 republication was located by search
but not read).

---

## Known data-quality caveats

1. **Wikipedia's 2026 table is wrong in five places** (see Edition confirmed) and must not be used
   as a corroboration source for ranks; its own citation points to the 2025 edition and the article
   carries a needs-updating banner.
2. **Fortune's revenue basis is not GAAP "revenue".** For banks it equals interest + noninterest
   revenues (verified exactly for seven names); for insurers it includes investment income and
   capital gains/losses but not deposits. Cross-checking a Fortune bank revenue against a company's
   net-revenue XBRL tag will always "fail" — that failure is definitional, not an error, and is
   recorded per-row in the notes rather than resolved silently.
3. **Three refiner revenues could not be reconciled to a single tagged figure**: Phillips 66
   (+4,184), Marathon Petroleum (+2,523), Valero (−6,748 vs the assessed-tax-inclusive tag).
   Fortune's methodology excludes excise taxes; the direction of the Valero gap is consistent with
   that, the direction of the Phillips 66 / Marathon gaps is not explained by anything retrieved.
   Both values are shown in the row notes; the ranking figures are Fortune's.
4. **Ford's profit disagrees with the only tagged 12-month figure by $20M** (Fortune −8,182 vs
   `ProfitLoss` −8,162). No `NetIncomeLoss` figure was returned for the period, so the difference
   (plausibly noncontrolling interests, which Fortune's stated definition deducts) is **not
   established**. Marked `Medium`.
5. **Fannie Mae's revenue leaves a $551M residual** that was not attributable to a specific XBRL
   tag. Marked `Medium`.
6. **State Farm is entirely single-source**: a mutual insurer with no SEC filings, so no independent
   financial check exists; and Fortune states mutual-insurer profits use **statutory accounting**,
   i.e. not comparable with the GAAP profits of the other 49 rows.
7. **Precision is inconsistent across the dataset.** Three rows carry decimals — Cencora
   ($321,332.8 / $1,554.2), StoneX ($132,378.2 / $305.9), State Farm ($132,311.6 / $12,937.7).
   For Cencora and StoneX the decimals are not an artifact: their 10-K XBRL values
   ($321,332.819M, $132,378.2M) match to the dollar. State Farm's decimals have no external check.
8. **Home Depot breaks Fortune's own stated cutoff.** Its ranked fiscal year ended **2026-02-01**,
   one day after the "fiscal year ended on or before Jan. 31, 2026" rule in the methodology, and
   both its revenue and profit match the 10-K exactly. The rule as printed is therefore not the rule
   as applied. Recorded, not corrected.
9. **Fiscal years are genuinely heterogeneous** — ranked periods end on 2025-03-31 (McKesson),
   2025-05-31 (FedEx), 2025-06-30 (Microsoft, Cardinal Health), 2025-08-31 (Costco), 2025-09-27
   (Apple, Disney), 2025-09-30 (Cencora, StoneX), 2025-12-27/-28 (PepsiCo, J&J), 2026-01-25
   (Nvidia), 2026-01-30 (Dell), 2026-01-31 (Walmart, Kroger, Target), 2026-02-01 (Home Depot).
   Any later cross-company comparison of "2025" must respect these differing period ends.
10. **ExxonMobil Holdings has no filing history under its own registrant.** Fortune's name reflects
    a corporate reorganization; the new registrant (CIK 2115436) returned no comparable annual
    XBRL facts, so corroboration ran through the legacy Exxon Mobil Corp registrant (CIK 34088).
    Treat any pre-reorganization legal-continuity claim as unverified.
11. **HQ city and industry labels are single-source by construction** (they are Fortune's editorial
    fields). One substantive conflict found: PepsiCo, Purchase vs Harrison, New York.
12. **Two ranks differ from Fortune's own name forms elsewhere:** the press release writes
    "Exxon Mobil" where the dataset writes "ExxonMobil Holdings"; the dataset's rank 5 label is
    "Alphabet (Google)". Fortune's dataset spelling was used in the CSV.
13. **Retrieval-time risk.** Fortune's page is dated 2026-06-03 but carries live editorial
    modules (its article grid included items dated up to 2026-09-22, i.e. four months after
    publication). The numbers were read from the ranking payload, not from those modules, but a
    later re-fetch of the same URL may not return an identical payload. This file is the record of
    what was returned on 2026-09-23.
14. **No 10-K document was opened directly.** Corroboration used SEC's machine-readable XBRL
    endpoints, which report company-filed values with accession metadata; the underlying filing text
    was not read. That is a weaker check than reading the report, and is stated as such.

---

## Feasibility register

Purpose: a data-feasibility note on how far back usable public evidence for the founding/early
period appears to reach. **Not a judgment about the companies.**

Evidence basis for this register, stated once: earliest-origin dates, founder names and the
origin-structure flags below come from the retrieved Wikipedia article for each company
(URL form `https://en.wikipedia.org/wiki/<Title>`, `action=raw`, retrieved 2026-09-23 — item 15 of
the Retrieval log). That is a Tier-2/3 aggregator. **None was chased to incorporation registries,
county filings or founding-era documents in this pass**, so every date here is a *feasibility
pointer*, not an established fact, and carries confidence `Low–Medium` until a Level-2 lead chases
it. Second, publisher-side signal available for all 50 rows: Fortune's own
`Founder is CEO` field, retrieved as part of item 3 — it reads **yes for exactly four of the 50**:
Nvidia (16), Meta Platforms (17), Dell Technologies (41), Tesla (43). Flags reported per row:
`spin=n` = count of "spin-off" references in the article body; `gse` = described as a
government-sponsored enterprise; `BC` = Blue Cross/Blue Shield lineage; `hold` = described as a
holding company; `mrg` = article describes a merger-of formation.

### A. Founder-era history directly reachable — single founder, continuous entity (11)

| Rank | Company | Earliest documented origin (source: that company's Wikipedia article) | Feasibility note |
|---|---|---|---|
| 1 | Amazon | 1994-07-05, Bellevue, Washington; founder Jeff Bezos | Founder identified in the retrieved article; entity continuous. Well inside the electronic-filing era; Fortune's own text independently places its Fortune 500 debut at 2002 (rank 492 per the June 3, 2026 release). |
| 2 | Walmart | 1962-07-02, Rogers, Arkansas; founders Sam Walton, Bud Walton | Two-founder origin, continuous entity; origin decade pre-dates EDGAR, so early years rest on archival/press material — not checked this pass. |
| 4 | Apple | 1976-04-01, Los Altos, California; founders Steve Jobs, Steve Wozniak, Ronald Wayne | Three named founders including a third who is usually forgotten in origin stories — a documented asymmetry available at the outset. |
| 11 | Microsoft | 1975-04-04, Albuquerque, New Mexico; founders Bill Gates, Paul Allen | Named founders and a founding location outside the eventual HQ state; continuous entity. |
| 13 | Costco | 1983-09-15, Seattle; founders James Sinegal, Jeffrey Brotman | Founder-era fully inside the modern record. Any earlier warehouse-club ancestry is not stated in the retrieved infobox and was not checked. |
| 16 | Nvidia | 1993-04-05, Sunnyvale, California | Founder list is rendered as a template in the infobox and was **not extracted → founders UNKNOWN here**. Fortune independently flags `Founder is CEO = yes`. |
| 17 | Meta Platforms | 2004-02-04, Cambridge, Massachusetts | Founder list not extracted → UNKNOWN; `Founder is CEO = yes` per Fortune. Founded at a different place than its HQ city (Menlo Park). |
| 19 | Centene | 1984; founder Elizabeth "Betty" Brinn | Named founder with a continuous entity. Bare title "Centene" returned only a 33-byte stub; the "Centene Corporation" article was used instead. |
| 25 | Home Depot | 1978-02-06, Marietta, Georgia; founders Bernard Marcus, Arthur Blank, Ron Brill, Pat Farrah, Ken Langone | Five named founders — the richest multi-founder origin record in this universe. |
| 37 | Comcast | 1963-06-28, Tupelo, Mississippi; founder Ralph J. Roberts | Named founder; HQ city differs from founding city. Article carries 32 "spin-off" references, all relating to later units, not the origin. |
| 50 | FedEx | 1971-05-05, Little Rock, Arkansas; founder Frederick W. Smith | Named founder; founded in a state other than its HQ state — a real relocation event available to Stage 1. |

### B. Founder-era reachable, but the origin is dual-named or the entity was later renamed (6)

| Rank | Company | Earliest documented origin | Feasibility note |
|---|---|---|---|
| 3 | UnitedHealth Group | Infobox lists **two** origins: 1974 (as CharterMed) and 1977 (as UnitedHealthCare); founder Richard T. Burke | Founder named, but the company's own record offers two founding dates. Which one a "founding" report uses is a decision, not a fact. |
| 6 | CVS Health | 1963, Lowell, Massachusetts; founders Stanley P. Goldstein, Sidney Goldstein, Ralph P. Hoagland III | Named founders; "CVS Health" is a later identity (renaming markers present in the article). Modern insurance/pharmacy lineage not traced. |
| 15 | Cardinal Health | 1971; founder Robert D. Walter | Named founder. Article contains 9 "spin-off" references; their relevance to the origin was **not verified**. |
| 34 | Humana | 1961-08-18 **as Extendicare Inc.**, Louisville, Kentucky; founders David A. Jones Sr., Wendell Cherry | Founder-era record exists but sits under a different company name; `mrg`/rename markers present. |
| 40 | Valero Energy | 1980-01-01; founder William Greehey | Named founder, but 4 "spin-off" references and 1 merger reference indicate the ranked entity's relationship to that 1980 origin is not simple. **Not verified.** |
| 43 | Tesla | 2003-07-01, San Carlos, California | Founder list rendered as a template, **not extracted → founder attribution UNKNOWN on retrieved evidence**, even though Fortune flags `Founder is CEO = yes`. A lead must resolve attribution from primary material; the register deliberately records the gap rather than assuming. |

### C. Pre-World-War-II or 19th-century origins — evidence exists but is archival, not filing-based (11)

For all of these the "founder's early period" is more than 60 years before the electronic-filing
record, so Stage 1 evidence must come from registries, local press, trade directories and company
histories. The retrieved articles supply the pointer, not the proof.

| Rank | Company | Earliest documented origin | Note |
|---|---|---|---|
| 8 | McKesson | 1833, New York City (article: "1833; 193 years ago") | Oldest origin in the universe; founder field is a list template, **not extracted**. |
| 21 | Chevron | **No `founded` param in the retrieved infobox.** Article prose gives Pacific Coast Oil, with 1879 appearing 13 times, and states Standard Oil acquired Pacific Coast Oil in 1900 for $761,000 | The origin is a Standard Oil branch, not a founder's venture; a clean founder-playbook reading is probably not available. |
| 22 | Ford Motor | 1903-06-16, Detroit, Michigan; founder Henry Ford | Single named founder with an unusually rich documentary record (the article cites a National Park Service historic-landmark nomination for the Ford Piquette Avenue Plant). 2 spin-off references. |
| 27 | Kroger | 1883, Cincinnati, Ohio; founder Bernard Kroger | Named founder, continuous name. |
| 36 | Goldman Sachs Group | 1869 | Pre-Civil-War origin; described as a holding company (`hold`), so the ranked registrant is far younger than 1869. Founder field is a list template, **not extracted**. |
| 39 | Morgan Stanley | 1935; founders Henry Sturgis Morgan, Harold Stanley | Named founders and an explicit two-family naming origin; 5 spin-off references and a merger reference connect it to a J.P. Morgan parent, **not verified**. |
| 44 | Walt Disney | 1923-10-16 | Ranked registrant is the holding company (`hold`), younger than the 1923 origin. Founder field is a list template, **not extracted**. |
| 45 | Johnson & Johnson | 1886-01, New Brunswick, New Jersey | 8 spin-off references; founder field is a list template, **not extracted**. |
| 47 | Boeing | 1916-07-15, Seattle; founder William E. Boeing | Named founder with a dated founding. |
| 48 | United Parcel Service | 1907-08-28, Seattle, as the **American Messenger Company**; founder James E. Casey | Founder-era record exists under a different name and city role than today's Atlanta HQ. |
| 46 | PepsiCo | **Two origins: 1902-12-24** New Bern, North Carolina (as the Pepsi-Cola Company; founder Caleb Bradham) **and 1965-06-08** (as PepsiCo) | Dual origin: a 1902 drugstore-creation line and a 1965 merger-era corporate identity, 9 spin-off references. |

### D. Origin structurally ambiguous — successor, merger, spin-off or reorganization entity (19)

For these, the ranked company's own founding date is **not** the interesting origin, and the
"founder" either does not exist or belongs to an ancestor that is not the registrant. Treat the
origin as a contested object requiring a documented inheritance chain before any Stage-1 claim.

| Rank | Company | What the retrieved article gives | Ambiguity |
|---|---|---|---|
| 5 | Alphabet (Google) | 2015-10-02, `hold`, `mrg` | The ranked entity is the holding-company formation. Google's own 1998 origin **is not in the retrieved article → UNKNOWN here**; a lead must fetch the Google article separately. |
| 7 | Berkshire Hathaway | 1839 **as Valley Falls Company**; founder Oliver Chace; `hold`, `mrg`, 1 spin-off | Two unrelated origins in one row: an 1839 textile mill founder and a 20th-century investment vehicle. The latter is not dated in the retrieved text → UNKNOWN. |
| 9 | ExxonMobil Holdings | 1999-11-30, `mrg`; founder field names Lucio Noto and Lee Raymond with a cited book about the Exxon–Mobil merger | A merger-era registrant sitting on top of Standard Oil ancestors (not retrieved → UNKNOWN), **plus** a further reorganization evidenced by the new SEC registrant carrying no filing history (caveat 10). |
| 10 | Cencora | 2001-08-28 **(merger of AmeriSource Health and Bergen Brunswig)**; no founder field | Inherited/merged origin, then renamed; the deeper Bergen Brunswig ancestry was not retrieved → UNKNOWN. |
| 12 | JPMorgan Chase | 2000-12-01; an inline editorial comment in the wikitext states the article "is about the company formed in 2000 following the merger of Chase Manhattan Corporation and J.P. Morgan & Co." | Explicitly a merger successor; both ancestors' origins not retrieved → UNKNOWN. |
| 14 | Cigna Group | 1982 **(merger of CG and INA)**, `hold` | Ancestry of both parents not retrieved → UNKNOWN. |
| 18 | Elevance Health | 1946 (mutual Hospital Insurance Inc. and Mutual Medical Insurance Inc.) and 2004 (merger of Anthem and WellPoint Health Networks); `BC`, `hold` | Mutual-insurance origin, a Blue Cross/Blue Shield lineage marker, and a 2004 merger — three candidate "origins" in one row. |
| 20 | Bank of America | 1998 **(via the merger of BankAmerica & NationsBank)**, `hold` | The 1998 merger is the registrant's origin; the Amadeo Giannini ancestry implied by "BankAmerica" is not in the retrieved text → UNKNOWN. |
| 23 | General Motors | **1908-09-16 (original company) and 2009-07-10 (present company)**, citing a Delaware division-of-corporations name search; founder William C. Durant | The article itself distinguishes the original from the present company: the ranked entity is a 2009 successor with a 1908 name. |
| 24 | Citigroup | 1998-10-08, `hold`, 7 spin-off references | Merger-era registrant; both ancestors' origins not retrieved → UNKNOWN. |
| 28 | Verizon Communications | 1983-10-07, citing a SEC restated-certificate exhibit; 5 spin-off references | The registrant's own certificate is dated 1983 — i.e. the ranked name is not the origin. Bell-system ancestry not retrieved → UNKNOWN. |
| 29 | Phillips 66 | 1927 (brand & original company, Bartlesville, Oklahoma) **and** 2012-05-01 (company, Houston); founders Lee Eldas Phillips and Frank Phillips; 8 spin-off references | A 1927 brand name attached to a 2012 registrant. The 2012 parent company is **not named in what was retrieved → UNKNOWN**. |
| 30 | Marathon Petroleum | 2009-11-09; 6 spin-off references; no founder field | Registrant date present, origin story is a spin-off whose parent is not identified in the retrieved text → UNKNOWN. |
| 31 | StoneX Group | 1924, `hold`, renamed marker, no founder field | A 1924 origin under a name the company no longer uses; the intervening identity is not in the retrieved text → UNKNOWN. |
| 35 | AT&T | Infobox gives 1983-10-05/1983-10-07 (article's own citation is an SEC certificate exhibit for **AT&T Inc.**, formerly Bell Atlantic); founders listed as Zane Edison Barnes and Edward Whitacre; 10 spin-off references, `hold` | The most name-inherited entity in the universe: a 1983 registrant wearing a 1983-dispersed brand, with Bell System ancestry not retrieved → UNKNOWN. |
| 38 | Wells Fargo | Infobox lists three dates: 1929-01-24 (as Northwest Bancorporation), April 1983 (as Norwest Corporation), November 2, 1998 (as Wells Fargo & Company); founders credited to Henry Wells and William Fargo "(Wells Fargo Bank)" | The registered entity's own three dates belong to a Minnesota bank chain, while the credited founders belong to a different, older bank. Textbook structural ambiguity. |
| 41 | Dell Technologies | 2016-09-07; founder Michael Dell; `mrg` | Ranked registrant formed 2016, not 1984. Michael Dell's original venture is **not dated in the retrieved article → UNKNOWN**. |
| 42 | Target | 1902-06-24 (corporation) and 1962-05-01 (first Target store); founders George Dayton (corporation), Douglas Dayton and John Geisse (store) | Corporate origin and brand origin 60 years apart with different named people; the ranked name is the younger one. |
| 49 | RTX | 2020-04-03; founder field credits Vannevar Bush, Laurence K. Marshall and Charles G. Smith "(as American Appliance Company, later Raytheon in 1922)" and Frederick Rentschler "(as United Technologies in 1934)" | A 2020 registrant carrying two 20th-century founder lines with three and one named founders respectively. |

### E. No founder at all — created by statute (2)

| Rank | Company | Earliest documented origin | Note |
|---|---|---|---|
| 26 | Fannie Mae | 1938; `gse` (government-sponsored enterprise marker present), `hold`; no founder field | There is no founder's early period to recover. Origin evidence is legislative/administrative, and the retrieved article supplies only the year 1938 — the enabling instrument was **not retrieved → UNKNOWN**. |
| 33 | Freddie Mac | 1970; `gse`; no founder field | Same structure: a congressionally chartered entity, origin by statute. Enabling act not retrieved → UNKNOWN. |

### F. Special case (1)

| Rank | Company | Note |
|---|---|---|
| 32 | State Farm Insurance | 1922-06-07; founder George J. Mecherle — a single named founder and a usable 1922 origin. But it is a **mutual insurer with no SEC filings at all** (confirmed by its absence from the SEC company index), and its ranked financials are on a statutory-accounting basis. The founder-era narrative is feasible; any *financial* evidence chain for the early years must come from state-regulator filings and company publications, none of which was retrieved → UNKNOWN. |

### Register summary

- **Founder-era history plausibly recoverable from public evidence (single founder, continuous
  entity):** 17 companies — group A (11) plus group B (6).
- **Origin predates the electronic-filing record; evidence is archival (19th-century/1900–1946):**
  11 companies (group C).
- **"Origin" structurally ambiguous — successor, merger, spin-off, renaming or re-registered
  entity:** 19 companies (group D). This is the largest group, and it is where hindsight
  contamination is most likely: the ranked company's own birthday is often the wrong event.
- **No founder exists:** 2 companies (group E).
- **Feasible narrative, restricted financial evidence channel:** 1 company (group F).
- Groups overlap by design only where stated: group C rows 21, 36, 39, 44, 45, 46 also carry
  successor/holding-company markers, and group D rows 7, 18, 29, 38 also carry pre-WWII origins.
- **Every date in this register is a Wikipedia-sourced pointer at `Low–Medium` confidence.** No
  incorporation record, county registry, charter text or founding-era document was retrieved in
  this pass. `UNKNOWN` marks each place a founder list was a template that was not extracted, each
  un-retrieved ancestor company, and each un-retrieved statutory instrument.
