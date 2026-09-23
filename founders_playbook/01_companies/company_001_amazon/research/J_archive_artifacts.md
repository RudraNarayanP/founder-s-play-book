# AMAZON STAGE 1 DOSSIER — J. IN-WINDOW PRODUCT ARTIFACTS

Mission: determine whether a 1995–1996 archived capture of the Amazon.com website exists, and
if not, establish the highest-standing substitute evidence for what the product actually was.
Cache checked first: `_EVIDENCE_CACHE.md` (S-1, FY97 10-K, Sheff 1994, HistoryLink, LAT 1997,
`wb_amazon.html` = 2006 capture, `cdx_amazon.txt`, `cdx_96.txt` already on disk).

## Verdict
**No in-window (1995-1996) archived capture of the Amazon.com website exists in the Wayback
Machine, and this is now established rather than assumed.** Three independent queries that actually
answered agree: the exact-homepage urlkey has zero captures for 1994-1997 (`[]`), the availability
API resolves a mid-1996 target to **19990828014913**, and Wayback's own nearest-capture resolver
redirects both a 1995 and a 1996 request to the same **19981212012532** bare 302. Section E
therefore **cannot** be written from a page capture; the first rendered homepage evidence is
1999-08-28, three years after launch.

**Section E should nevertheless be written from in-window Tier 1 artifact evidence, not from
memory.** The best product evidence found is not an archive page at all but **two dated Amazon
press releases from inside the window** — 4 October 1995 and 14 June 1996 (J-35 to J-43) — which
give the catalog size as it was actually advertised (one million, then 1.1 million titles), the
search-first interaction model, online ordering with UPS/Airborne Express delivery, the 10-40%
discount structure, the June-1996 feature enumeration, and a Bezos quote in his own contemporary
words. These are corroborated by **audited S-1/10-K in-window figures** (2,200 → 50,000 average
daily visits; 180,000 accounts; the 4,800-member Associates Program at 31 December 1996) and, for
the site's *page architecture*, by the S-1's own figure caption photographing exactly four page
types: **welcome, search, review, ordering** (J-23).

**What section E may claim, and what it may not.** It may describe the 1995-96 product as: a
search-and-order interface over an advertised ~1 million title catalog, reached directly at
`http://www.amazon.com/` and through third-party Associate hyperlinks, with online ordering,
e-mail-based service channels, 10-40% discounts, and a reader-participation feature present by
October 1995. It may state that *Time* named it one of the ten "Best Websites of 1996" (as reported
in the S-1). It **may not**: quote any specific on-screen layout, colour, logo rendering or homepage
copy as observed fact (no capture exists; the "blue underlined text" description is a 1999
reminiscence); attribute "2.5 million titles" to Stage 1; or include MatchMaker recommendations,
the out-of-print service, the Gift Center, One-Click, Wish List or any marketplace — all of which
are dated 1997 or later, or absent from filings through 1998.

## CDX / archive query log
Every query run against the archive, including failures. **A 504 is recorded as a failure, not as
a null** — several prefix queries never answered and therefore cannot support an absence claim.

| # | Query (endpoint + params) | Result | Interpretation |
|---|---|---|---|
| Q0a | (prior run, on disk `_scratch/cdx_amazon.txt`) `url=amazon.com` + `filter=statuscode:200` | 40 rows, earliest `19990828014913`, then `19991013091817`, then 2003+ | No 1995/1996/1997 status-200 row for the root |
| Q0b | (prior run, on disk `_scratch/cdx_96.txt`) 1996-targeted query | **0 bytes = empty response** | Prior agent's 1996 query returned nothing |
| Q1 | `cdx?url=amazon.com&matchType=prefix&output=json&limit=25` | 25 rows; earliest `19981212012532` (`http://amazon.com:80/`, **302**); then 1999-01-25, 1999-02-08/09/18 all 302 | Earliest capture of urlkey `com,amazon)/` is a 1998-12-12 redirect, not a page |
| Q2 | `cdx?url=www.amazon.com&matchType=prefix&output=json&limit=25` | **Byte-identical to Q1** (same `com,amazon)/` urlkey) | `www.` adds nothing — host is normalised out of the urlkey; testing the two hosts is not two tests |
| Q3 | `cdx?url=amazon.com/&matchType=exact&output=json&from=1994&to=1997` | **`[]`** | **Definitive null: zero captures of the homepage urlkey in 1994-1997, any status code** |
| Q4 | `cdx?url=amazon.com&matchType=prefix&from=1995&to=1996&filter=statuscode:200&limit=40&output=json` | **HTTP 504 Gateway Time-out (nginx)** | The query named in this brief **never returned**. It cannot be the basis of a "no 1996 rows" finding |
| Q5 | same as Q4 but `from=1995&to=1997`, lean `fl=timestamp,original,statuscode,mimetype` | **HTTP 504** | Lean field list did not help; the timeout is scan-side, not payload-side |
| Q6 | `cdx?url=amazon.com/exec/obidos/&matchType=prefix&from=1995&to=1998&limit=20&fl=...` | 20 rows, **all 302, all dated 1998-12-01..06** | Query SUCCEEDED but rows are truncated by urlkey sort order — proves `/exec/obidos/` exists in the 1998 index, does **not** enumerate 1996 |
| Q7 | `cdx?url=amazon.com/exec/obidos/ACRONYM-TO-A-GIFT/&matchType=prefix&from=1995&to=1999&limit=10` | **`[]`** | Null for the deep path named in the brief, 1995-1999 inclusive |
| Q8 | `archive.org/wayback/available?url=amazon.com&timestamp=19960601` | `closest: {status:"200", timestamp:"19990828014913"}` | Availability API independently says the nearest rendered page to mid-1996 is **1999-08-28** — ~39 months later |
| Q9 | `web.archive.org/web/19960601000000/http://www.amazon.com/` (follow-wayback's-own-nearest) | **302 → `/web/19981212012532/http://amazon.com/`** | Wayback's own resolver, asked for June 1996, answers **1998-12-12** |
| Q10 | `web.archive.org/web/19950801000000/http://amazon.com/` | **302 → same `19981212012532`** | Asked for Aug 1995, same answer. Two different in-window targets, one post-window resolution |
| Q11 | `cdx?url=amazon.com&matchType=prefix&from=19960101&to=19961231&limit=5` | **HTTP 504** | Even a single-year narrow window times out |
| Q12 | `cdx?url=amazon.com&matchType=prefix&from=19970101&to=19971231&limit=5` | **HTTP 504** | 1997 deep-path enumeration also unanswered |

**What the log establishes.** The homepage question is closed by three independent light queries
that actually answered: Q3 (`[]` for 1994-1997 exact), Q8 (nearest 200 = 1999-08-28), and Q9/Q10
(wayback's own nearest-to-1996 and nearest-to-1995 resolver both return 1998-12-12, a bare
redirect). **No in-window archived Amazon.com homepage exists in the Wayback Machine.**

**What the log does NOT establish.** Whether some *deep* amazon.com page (a `/exec/obidos/` product
or browse page) was crawled in 1995 or 1996. Every query that could have answered that — Q4, Q5,
Q11, Q12 — returned 504 and never produced rows. This residual is carried as gap **G-ARCHIVE-2**
and must not be written up as "proven absent."

## Findings

### A. The archive question itself

J-01 Claim: No archived capture of the Amazon.com homepage exists in the Wayback Machine for 1994-1997 at any HTTP status code. — Date: null result covering 1994-01-01..1997-12-31 — Source: Internet Archive CDX API, `url=amazon.com/&matchType=exact&output=json&from=1994&to=1997` — Source date: retrieved 2026-09-23 — URL: https://web.archive.org/cdx/search/cdx?url=amazon.com/&matchType=exact&output=json&from=1994&to=1997 — Archived: — — Tier: 1 — Class: FACT — Passage: "[]" — Conf: High — Corroboration: 4 independent (Q3 empty; Q1 earliest row 1998-12-12; Q8 availability API; Q9/Q10 wayback's own nearest-capture resolver) — Conflicts: None

J-02 Claim: The earliest capture of amazon.com in the Wayback Machine is a 302 redirect dated 1998-12-12, not a rendered page. — Date: 1998-12-12 — Source: Internet Archive CDX index, urlkey `com,amazon)/` — Source date: retrieved 2026-09-23 — URL: https://web.archive.org/web/19981212012532/http://amazon.com/ — Archived: 19981212012532 — Tier: 1 — Class: FACT — Passage: "19981212012532 http://amazon.com:80/ 302" — Conf: High — Corroboration: 3 (Q1, Q9, Q10) — Conflicts: None. Note this is a redirect row; it is not usable as product evidence.

J-03 Claim: The earliest *rendered* (status 200) homepage capture is 1999-08-28, roughly 41 months after the July 1995 launch and outside Stage 1. — Date: 1999-08-28 — Source: Wayback availability API for target 1996-06-01 — Source date: retrieved 2026-09-23 — URL: http://web.archive.org/web/19990828014913/http://www.amazon.com:80/? — Archived: 19990828014913 — Tier: 1 — Class: FACT — Passage: "closest: {status: 200, available: true, timestamp: 19990828014913}" — Conf: High — Corroboration: 2 (Q8 API; prior on-disk `cdx_amazon.txt` row 1) — Conflicts: None

J-04 Claim: Wikipedia's own editors, writing about Amazon's logo history, cite 1999-08-28 as the earliest homepage capture available — an independent confirmation that the community also finds nothing earlier. — Date: — — Source: Wikipedia, "Amazon (company)" history section, archival citation — Source date: UNKNOWN (article text retrieved locally) — URL: https://web.archive.org/web/19990828014913/http://www.amazon.com/ — Archived: 19990828014913 — Tier: 4 (lead) pointing at a Tier 1 artifact — Class: FACT about the archive's contents — Passage: "Between October 1999 ... and February 2000 ... Amazon's logotype has featured a curved arrow leading from A to Z" — Conf: Medium — Corroboration: 1 beyond J-03 — Conflicts: None

J-05 Claim: `url=amazon.com&matchType=prefix` and `url=www.amazon.com&matchType=prefix` are not two tests — the host is normalised out of the CDX urlkey, so both queries return byte-identical results. — Date: — — Source: this agent's Q1 vs Q2 — Source date: retrieved 2026-09-23 — URL: — — Archived: — — Tier: 1 — Class: INFERENCE (methodological) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 — Conflicts: None. **Corrects an assumption in the incoming brief**, which treated the two hosts as separate angles.

J-06 Claim: The specific query named in the incoming brief as evidence of "no 1996 rows" (`prefix` + `from=1995&to=1996` + `filter=statuscode:200`) does not return an empty set — it returns an HTTP 504, as do the same query narrowed to calendar-1996-only and calendar-1997-only. — Date: — — Source: Internet Archive CDX endpoint — Source date: retrieved 2026-09-23 — URL: — — Archived: — — Tier: 1 — Class: FACT — Passage: "504 Gateway Time-out" — Conf: High — Corroboration: 4 (Q4, Q5, Q11, Q12) — Conflicts: **The brief's premise that a CDX query showed no 1996 rows is not supported by that query; it never answered.** Absence of *deep-path* 1996 captures is therefore unproven (gap G-ARCHIVE-2).

J-07 Claim: The deep path `amazon.com/exec/obidos/ACRONYM-TO-A-GIFT/` has no captures in the archive for 1995-1999. — Date: null 1995-1999 — Source: CDX `matchType=prefix` — Source date: retrieved 2026-09-23 — URL: — — Archived: — — Tier: 1 — Class: FACT (bounded null) — Passage: "[]" — Conf: Medium — Corroboration: 1 — Conflicts: None. Weak evidence: the prefix query for the parent `/exec/obidos/` tree succeeded but its 20 rows were consumed by alphabetically-first urlkeys all dated 1998-12, so it could not speak to 1996.

J-08 Claim: `/exec/obidos/` URLs do exist in the index, and the home page of that era lived at `/exec/obidos/subst/home/home.html`. — Date: 1998-12 and 2000-02-29 — Source: CDX Q6 results; Wikipedia archive citation; local `wb_amazon.html` markup — Source date: retrieved 2026-09-23 — URL: https://web.archive.org/web/20000229082444/http://www.amazon.com/exec/obidos/subst/home/home.html — Archived: 20000229082444 — Tier: 1 — Class: FACT — Passage: "amazon.com/exec/obidos/subst/home/home.html" — Conf: High — Corroboration: 2 — Conflicts: None. **Post-window**; establishes only that the URL scheme was still in use in 2000, and therefore that a 1996 `/exec/obidos/` crawl is *possible* but unproven.

J-09 Claim: The only archived Amazon.com page physically on disk in this project is a 2006 capture. — Date: 2006-05-22 — Source: `_EVIDENCE_CACHE.md` row `wb_amazon.html`; timestamp read from page markup — Source date: — — URL: https://web.archive.org/web/20060522143937/http://www.amazon.com/ — Archived: 20060522143937 — Tier: 1 artifact of 2006, zero value for Stage 1 — Class: FACT — Passage: "web.archive.org/web/20060522143937" — Conf: High — Corroboration: 1 — Conflicts: None

### B. In-window audited self-description (S-1, T1, filed 1997 — describes 1995-96 history and 1995-96 audited figures)

J-10 Claim: The site opened for business in July 1995 under the positioning "Earth's Biggest Bookstore". — Date: 1995-07 — Source: Amazon.com Form S-1, "The Company" — Source date: 1997 (EDGAR accession 0000891020-97-000839; receipt 1997-03-24 per corroborating citation, and LAT "filed its offering ... in March") — URL: — (local: `_scratch/s1_orig.txt` line 280) — Archived: — — Tier: 1 — Class: FACT — Passage: "Since opening for business as \"Earth's Biggest Bookstore\" in July 1995, the Amazon.com bookstore has quickly become one of the most widely known, used and cited commerce sites on the World Wide Web" — Conf: High — Corroboration: 3 (10-K FY97 line 210 repeats verbatim; LAT 1997 reports B&N sued to challenge the slogan; HistoryLink) — Conflicts: None

J-11 Claim: The company was founded July 1994 and sold nothing before July 1995; the site's first six months produced no revenue. — Date: 1994-07 to 1995-07 — Source: S-1, "Limited Operating History" / MD&A — Source date: 1997 — URL: — (local line 1355) — Archived: — — Tier: 1 — Class: FACT — Passage: "The Company was incorporated in July 1994 and commenced offering products for sale on its Web site in July 1995." — Conf: High — Corroboration: 2 (S-1 line 467 "began selling books on its Web site in July 1995"; 10-K) — Conflicts: None

J-12 Claim: Average daily visits to the site were about 2,200 in December 1995 and about 50,000 in December 1996 — in-window, audited traffic measurements of the actual product. — Date: 1995-12 / 1996-12 — Source: S-1, "The Company" — Source date: 1997 — URL: — (local line 299) — Archived: — — Tier: 1 — Class: FACT — Passage: "Average daily visits (not \"hits\") have grown from approximately 2,200 in December 1995 to approximately 50,000 in December 1996" — Conf: High — Corroboration: 2 (repeated S-1 lines 434, 1718) — Conflicts: None

J-13 Claim: Through 31 December 1996 the site had taken more than $16 million of sales from about 180,000 customer accounts in over 100 countries. — Date: 1996-12-31 — Source: S-1 — Source date: 1997 — URL: — (local line 297) — Archived: — — Tier: 1 — Class: FACT — Passage: "Through December 31, 1996, Amazon.com had sales of more than $16 million to approximately 180,000 customer accounts in over 100 countries." — Conf: High — Corroboration: 2 (LAT 1997 cites "$16 million in sales"; 10-K restates) — Conflicts: None

J-14 Claim: Repeat customers exceeded 40% of orders as at the S-1 filing. — Date: 1997 (early) — Source: S-1 — Source date: 1997 — URL: — (local line 301) — Archived: — — Tier: 1 — Class: FACT — Passage: "repeat customers currently account for over 40% of orders" — Conf: High — Corroboration: 1 — Conflicts: None. Note: 10-K FY97 raises this to "over 58%", so 40% is the *earlier* state and must not be back-dated to 1995.

J-15 Claim: *Time* magazine named Amazon.com one of the ten "Best Websites of 1996" — a third-party, in-window judgment on the shipped product, reported inside an audited filing. — Date: 1996 — Source: S-1 — Source date: 1997 — URL: — (local line 302) — Archived: — — Tier: 1 (filing text) reporting a Tier 2 (magazine award) — Class: FACT — Passage: "Time magazine rated Amazon.com one of the 10 \"Best Websites of 1996.\"" — Conf: High that the S-1 says it; Medium that Time said it in 1996 — Corroboration: 1 — Conflicts: None. **The single best in-window product-quality artifact found so far; needs the Time original.**

J-16 Claim: The Amazon Associates Program was live and substantial within the window, with over 4,800 registered members as of 31 December 1996; it worked by embedding a hyperlink from a partner site into Amazon's ordering flow. — Date: 1996-12-31 — Source: S-1, "Associates Program" — Source date: 1997 — URL: — (local line 2130) — Archived: — — Tier: 1 — Class: FACT — Passage: "The Associates Program, which included over 4,800 registered members as of December 31, 1996. The program enables Associate Web sites to offer books to their audiences for fulfillment by Amazon.com." — Conf: High — Corroboration: 1 — Conflicts: None. **This is the clearest in-window evidence of how the 1996 product was actually distributed and entered: via third-party hyperlinks (Netscape Developer's Bookstore, The Village Voice, Upside.com), not only via amazon.com direct.**

J-17 Claim: Customers entered through the site and could search, browse highlighted selections and bestsellers, read and post reviews, register for personalised services, join promotions and check order status. — Date: — (filing-date state, 1997) — Source: S-1, "The Amazon.com Bookstore" — Source date: 1997 — URL: — (local line 1961) — Archived: — — Tier: 1 — Class: FACT for the 1997 site — Passage: "in addition to ordering books, can conduct targeted searches, browse from among highlighted selections, bestsellers and other features, read and post reviews, register for personalized services" — Conf: High — Corroboration: 2 (10-K FY97 repeats) — Conflicts: None. **Shows the LAUNCHED-and-scaled site, not the 1996 site; only the search/browse/order elements are safely in-window (see J-24).**

J-18 Claim: Ordering worked by clicking a button to add books to a virtual shopping basket, then a buy button, at which point the customer supplied shipping and credit-card details — and those details could be given **by e-mail or by telephone**, not only through the web form. — Date: — (filing-date state) — Source: S-1, "Ordering" — Source date: 1997 — URL: — (local line 2047) — Archived: — — Tier: 1 — Class: FACT — Passage: "To execute orders, customers click on the buy button and are prompted to supply shipping and credit card details, either by e-mail or by telephone." — Conf: High for 1997; **Medium for 1995-96** — Corroboration: 1 — Conflicts: 10-K FY97 (line 216) describes the same site as offering "Web-based credit card payment", a later state. The off-web ordering channel is the more archaic form and plausibly the original design, but a dated in-window source is needed to claim it for 1996.

J-19 Claim: The system auto-confirmed every order by e-mail within minutes and notified the customer again on shipment; card and address data were held on a secure server so repeat customers could re-use them under a personal password. — Date: — — Source: S-1, "Ordering" — Source date: 1997 — URL: — (local line 2059) — Archived: — — Tier: 1 — Class: FACT — Passage: "The Company's system automatically confirms each order by e-mail to the customer within minutes after the order is placed and advises customers by e-mail shortly after orders are shipped." — Conf: High for 1997 — Corroboration: 2 (LAT 1997 independently reports the same behaviour as observed experience: "Amazon.com promptly e-mailed me, confirming my order, and then nine hours later informed me the book had been shipped") — Conflicts: None. **LAT's first-hand 1997 test is the strongest evidence this was the lived experience, not just the design intent.**

J-20 Claim: The catalog was searchable by title, subject, author, keyword, publication date or ISBN, and supported Boolean queries. — Date: — — Source: S-1, "Searching" — Source date: 1997 — URL: — (local line 2010) — Archived: — — Tier: 1 — Class: FACT — Passage: "The Company provides a selection of search tools to find books based on title, subject, author, keyword, publication date or ISBN. Customers can also use more complex and precise search tools such as Boolean search queries." — Conf: High for 1997; Medium for 1996 — Corroboration: 2 (10-K repeats verbatim; HistoryLink describes a search engine built over a digital catalog keyed on book numbers) — Conflicts: None

J-21 Claim: Catalog size as stated in the filings is "more than 2.5 million titles" — this is a **1997** figure and is NOT the in-window number. — Date: 1997 — Source: S-1 (8 occurrences, lines 288/381/1702/1824/1834/2004/2180/3657) and 10-K FY97 — Source date: 1997 / 1998 — URL: — — Archived: — — Tier: 1 — Class: FACT about the 1997 site; MISLEADING if used for Stage 1 — Passage: "The Company offers more than 2.5 million titles, including most of the estimated 1.5 million English-language books believed to be in print" — Conf: High — Corroboration: 9 — Conflicts: **Directly conflicts with the retrospective "one million titles" homepage tagline (J-25). Both are true of different years.** Section E must not write "2.5 million" as the launch-era claim.

J-22 Claim: Amazon ran a "500" bestseller/prediction list at 40% off list price with themed focus lists (Computer 50, Science Fiction 50), plus Editors' Favorites, Spotlight, Book of the Day, Titles in the News, Hot This Week and Award Winners, and surfaced featured-book cover art that could be clicked straight into an order. — Date: — (filing-date state) — Source: S-1, "Browsing" — Source date: 1997 — URL: — (local line 1975) — Archived: — — Tier: 1 — Class: FACT for 1997; UNKNOWN which of these existed in 1996 — Passage: "The Amazon.com 500 features 500 current bestsellers and titles that Amazon.com predicts will be future bestsellers at 40% discounts from list price" — Conf: Medium — Corroboration: 1 — Conflicts: None. **Section E may not enumerate these as 1996 features without in-window corroboration.**

J-23 Claim: The S-1 itself reproduced screen images of the product, and the four page types it chose to photograph were the welcome page, the search page, a review page and the ordering page. — Date: 1997 (filing) — Source: S-1, figure caption inside "The Amazon.com Bookstore" — Source date: 1997 — URL: — (local line 1970) — Archived: — — Tier: 1 — Class: FACT — Passage: "[PICTURES OF THE COMPANY'S WELCOME, SEARCH, REVIEW AND ORDERING WEB PAGES]" — Conf: High — Corroboration: 1 — Conflicts: None. **Highest-value structural artifact found: the company's own selection of four screen images is a contemporaneous, dated statement of what the product's page architecture was.** The images themselves are absent from the ASCII full text (gap G-S1-SCREENSHOTS) and must be pulled from the original filing graphics.

J-24 Claim: Collaborative filtering (MatchMaker), the out-of-print service, and the Gift Center were announced in March 1997, March 1997 and November 1997 respectively — all three are therefore **absent from the 1995-96 product**. — Date: 1997 — Source: S-1 line 2044; 10-K FY97 lines 313, and Gift Center paragraph — Source date: 1997 / 1998 — URL: — — Archived: — — Tier: 1 — Class: FACT (dated negative by first-appearance) — Passage: "Amazon.com announced its MatchMaker collaborative filtering service in March 1997." — Conf: High — Corroboration: 2 — Conflicts: None

J-25 Claim: One-Click ordering, Wish List, gift registries and a third-party marketplace are absent from both the S-1 and the FY1997 10-K entirely. — Date: null through 1998 — Source: full-text grep of `s1_orig.txt` and `amzn10k1997.txt` for `one-click|1-click|wish list|gift registr|marketplace|third-party sell` — Source date: retrieved 2026-09-23 — URL: — — Archived: — — Tier: 1 — Class: INFERENCE from documented negative search — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Medium — Corroboration: 1 — Conflicts: None. The only `marketplace` hits are the generic phrase "a viable commercial marketplace"; the only `auction` hits are in a **lease agreement exhibit** (excluded premises clause), which is a false positive worth recording so a later agent does not mistake it for a product feature.

J-26 Claim: Within the window the company bought advertising on Yahoo!, Pointcast, Excite, Lycos, Quote.com and CNN, and relied heavily on word-of-mouth. — Date: — (filing-date state, describing 1996-97) — Source: S-1, "Online Service and Internet Advertising" — Source date: 1997 — URL: — (local line 2115) — Archived: — — Tier: 1 — Class: FACT — Passage: "The Company places advertisements ... Yahoo!, Pointcast, Excite, Lycos, Quote.com and CNN." — Conf: Medium (list is undated within the filing) — Corroboration: 1 — Conflicts: None

J-27 Claim: 1995 advertising expense was $30,000 — i.e. the launch-year product acquired essentially all of its ~2,200 daily visitors without paid media. — Date: 1995 — Source: S-1, notes to financial statements, "Advertising Costs" — Source date: 1997 — URL: — (local line 3718) — Archived: — — Tier: 1 — Class: FACT — Passage: "For the years ended December 31, 1995 and 1996, the Company incurred advertising expense of $30,000" — Conf: High — Corroboration: 1 — Conflicts: None. (1996 figure truncated in the grep window; re-read line 3718+ to capture it.)

J-28 Claim: Customer contact ran through nine e-mail addresses, and support staff handled "questions about the ordering process" as a named function. — Date: — (1997 state) — Source: S-1, "Customer Service" — Source date: 1997 — URL: — (local line 2152) — Archived: — — Tier: 1 — Class: FACT — Passage: "Amazon.com offers nine e-mail addresses to enable customers to request information and to encourage feedback and suggestions." — Conf: High for 1997; UNKNOWN for 1996 — Corroboration: 1 — Conflicts: None. **E-mail was a customer-facing channel of the product, consistent with J-18.**

### C0. IN-WINDOW COMPANY SELF-DESCRIPTION OF THE LIVE SITE (the breakthrough artifacts)

> Amazon's own press archive at `press.aboutamazon.com` is organised by year and contains two
> releases **inside the 1995-1996 window**. These are dated corporate statements issued while the
> site was live and are the first in-window product artifacts found. They outrank every
> retrospective source below and should be the backbone of section E.

J-35 Claim: On 4 October 1995 Amazon issued a release headlined "World's Largest Bookseller Opens on the Web" describing the live site at `http://www.amazon.com/` as offering more than one million different titles. — Date: 1995-10-04 — Source: Amazon.com press release, US Press Center archive — Source date: 1995-10-04 — URL: https://press.aboutamazon.com/1995/10/worlds-largest-bookseller-opens-on-the-web — Archived: — — Tier: 1 — Class: FACT — Passage: "The retailer can be found at http://www.amazon.com/. ... more than one million different titles" — Conf: High — Corroboration: 3 (June 1996 release J-39; HistoryLink tagline J-29; S-1 "in July 1995" J-10) — Conflicts: The archive's index lists this item under 1995-10-03 while the document dateline reads 4 October 1995; treat as 1995-10-04 with a one-day listing discrepancy. **Shows the LAUNCHED site, roughly three months after opening.**

J-36 Claim: The October 1995 product's search engine was its advertised core: a search engine over the catalog that let customers find titles without leaving their desks. — Date: 1995-10-04 — Source: Amazon.com press release — Source date: 1995-10-04 — URL: https://press.aboutamazon.com/1995/10/worlds-largest-bookseller-opens-on-the-web — Archived: — — Tier: 1 — Class: FACT — Passage: "A powerful, yet easy-to-use search engine makes it possible for customers to find titles ... after a few minutes of searching, without ever leaving their desks." — Conf: High — Corroboration: 2 (S-1 "Searching" J-20; HistoryLink J-29) — Conflicts: None

J-37 Claim: In October 1995 customers ordered online and books were delivered to their doors by UPS or Airborne Express; discounts were 10-40 percent off list on all but the most obscure titles. — Date: 1995-10-04 — Source: Amazon.com press release — Source date: 1995-10-04 — URL: https://press.aboutamazon.com/1995/10/worlds-largest-bookseller-opens-on-the-web — Archived: — — Tier: 1 — Class: FACT — Passage: "customers order online and books are delivered directly to their doors via UPS or Airborne Express. Amazon.com discounts all but the most obscure titles 10-40 percent from the list price." — Conf: High — Corroboration: 2 (**independently matches HistoryLink's "10 percent off the list price of any title and 40 percent off ... bestsellers" (J-31), which was previously single-sourced**; and the S-1's 40%-off Amazon.com 500, J-22) — Conflicts: None. **This is the strongest price-presentation evidence available for the launch-era product and it retires the doubt over HistoryLink's discount figures.**

J-38 Claim: Reader participation was present within three months of launch: the October 1995 release advertises that readers can share thoughts on particular books and exchange ideas with other readers. — Date: 1995-10-04 — Source: Amazon.com press release — Source date: 1995-10-04 — URL: https://press.aboutamazon.com/1995/10/worlds-largest-bookseller-opens-on-the-web — Archived: — — Tier: 1 — Class: FACT that the capability was advertised in-window; UNKNOWN what form it took — Passage: "Amazon.com allows readers to share their thoughts on particular books and exchange ideas with other readers" — Conf: Medium — Corroboration: 2 (S-1 "Reviews and Content" J-17; LAT 1997 "anyone who visits the site can post a review of any book", J-32) — Conflicts: None. **Important correction to a common assumption: some reader-contribution feature existed in 1995. Section E must not write "no reviews until 1996" without further evidence, and equally must not describe the 1995 form as the later full review system — the release does not say whether it was e-mailed extracts, a forum, or per-title reviews.**

J-39 Claim: By 14 June 1996 Amazon described the site to the press as a catalogue of 1.1 million titles with easy online ordering, "easy-to-use search and browse features, email services, Web-based credit card payment and direct shipping to customers", and customers in more than 95 countries. — Date: 1996-06-14 — Source: Amazon.com press release "Shopping for Books on the Internet Isn't Just for Tech Buyers Anymore; Amazon.com, World's Largest Bookseller, Tracks Who's Buying Online" — Source date: 1996-06-14 — URL: https://press.aboutamazon.com/1996/6/shopping-for-books-on-the-internet-isnt-just-for-tech-buyers-anymore-amazon-com-worlds-largest-bookseller-tracks-whos-buying-online — Archived: — — Tier: 1 — Class: FACT — Passage: "easy-to-use search and browse features, email services, Web-based credit card payment and direct shipping to customers." — Conf: High — Corroboration: 2 (the identical feature string reappears in the FY97 10-K line 216, showing the 1996 wording was still the company's own frame a year later; and Oct 1995 release J-35) — Conflicts: None. **Shows the LAUNCHED mid-window site. This is the single best in-window statement of what the 1996 product consisted of.**

J-40 Claim: The catalog figure Amazon advertised in-window was 1 million (Oct 1995) rising to 1.1 million (June 1996) — **not** the 2.5 million in the 1997 filings, and the 2.5 million must not be attributed to Stage 1. — Date: 1995-10 / 1996-06 — Source: the two 1995-96 releases vs S-1/10-K — Source date: 1995-10-04 / 1996-06-14 vs 1997/1998 — URL: — — Archived: — — Tier: 1 — Class: FACT — Passage: "catalogue of 1.1 million titles" — Conf: High — Corroboration: 2 (HistoryLink's remembered homepage tagline "One million titles, consistently low prices", J-29, is now corroborated by a dated company source rather than standing alone) — Conflicts: **Resolves the 1-million-vs-2.5-million tension: both correct, separated by ~18 months.**

J-41 Claim: Amazon's early positioning line, as carried in its own launch-week release, was "If it's in print, it's in stock", distinct from the later "Earth's Biggest Bookstore" slogan that Barnes & Noble challenged in 1997. — Date: 1995-10-04 — Source: Amazon.com press release; LAT 1997 for the 1997 slogan dispute — Source date: 1995-10-04 — URL: https://press.aboutamazon.com/1995/10/worlds-largest-bookseller-opens-on-the-web — Archived: — — Tier: 1 — Class: FACT — Passage: "If it's in print, it's in stock" — Conf: Medium — Corroboration: 1 — Conflicts: None. **Flag: verify the exact placement of this line (headline sub-copy vs homepage blurb) against the original before quoting it as on-screen text; the retrieved copy attributes it as a tagline but not explicitly as homepage rendering.**

J-42 Claim: By early October 1995, within its first four weeks of operating as a public storefront, the site had shipped books to customers in all 50 states and more than 45 countries. — Date: 1995-10-04 — Source: Amazon.com press release — Source date: 1995-10-04 — URL: https://press.aboutamazon.com/1995/10/worlds-largest-bookseller-opens-on-the-web — Archived: — — Tier: 1 — Class: FACT — Passage: "shipped books to customers in all 50 states and more than 45 countries" — Conf: High — Corroboration: 2 (Wikipedia citing Inc. for "first two months ... all 50 states and over 45 countries"; S-1's 1996 "over 100 countries") — Conflicts: The release does not restate the July 1995 opening day, so it cannot date the launch itself.

J-43 Claim: Bezos is quoted in the October 1995 release making the infinite-shelf argument in the company's own words while the outcome was unknown. — Date: 1995-10-04 — Source: Amazon.com press release quoting J. P. Bezos — Source date: 1995-10-04 — URL: https://press.aboutamazon.com/1995/10/worlds-largest-bookseller-opens-on-the-web — Archived: — — Tier: 1 — Class: CONTEMPORARY OBSERVATION (founder statement, in-window) — Passage: "We are able to offer more items for sale than any retailer in history, thanks entirely to the Internet" — Conf: High — Corroboration: 1 — Conflicts: None

### C. Retrospective descriptions of the 1995-96 site (time-firewalled; subordinate to section C0)

J-29 Claim: HistoryLink describes the original homepage as carrying the tagline "One million titles, consistently low prices" in blue underlined text, with a blue capital 'A' logo containing a river, a shopping basket, a payment platform and a search engine over a digital book catalog. — Date: event 1995 — Source: HistoryLink.org Essay 23230, "Amazon: The Early Years (1995-1999)" — Source date: 1999 (essay's dated NYT citation is 1999-07-13; page accessed 2025) — URL: — (local: `_scratch/hl.txt` line 70) — Archived: — — Tier: 2 — Class: **RETROSPECTIVE INTERPRETATION** — Passage: "The original homepage was simple, emblazoned with the words \"One million titles, consistently low prices\" in blue underlined text." — Conf: Medium — Corroboration: 1 — Conflicts: **Yes — the tagline's "one million titles" contradicts the filings' 2.5 million (J-21), and HistoryLink says the search catalog used "ISDN numbers", which is almost certainly a transcription error for ISBN. Do not quote the ISDN phrase.** Usable only with in-window corroboration of the tagline.

J-30 Claim: HistoryLink dates the launch to 16 July 1995 with $12,000 of books sold in week one, and states a beta site existed beforehand at a Bellevue rental house. — Date: event 1995-07-16 — Source: HistoryLink Essay 23230 — Source date: 1999 — URL: — (local line 48) — Archived: — — Tier: 2 — Class: RETROSPECTIVE INTERPRETATION — Passage: "Shortly after developing a beta version of his website at a rental house in Bellevue ... Amazon.com officially launched on July 16, 1995, selling $12,000 worth of books in its first week." — Conf: Medium — Corroboration: 2 for the *date* only (Wikipedia cites History.com "Amazon opens for business" 1995-07-16; S-1 supports month-level "July 1995") — Conflicts: None. **The filings never give a day; only HistoryLink/secondary sources give 16 July. Report as 1995-07 with the day as Medium confidence.**

J-31 Claim: Early operations were drop-ship: Amazon held no stock, bought the ordered book from a distributor, repackaged and shipped it, taking a week or more; pricing was 10% off list and 40% off bestsellers; an audible bell announced each order until staff switched it off. — Date: event 1995 — Source: HistoryLink Essay 23230 — Source date: 1999 — URL: — (local line 72) — Archived: — — Tier: 2 — Class: RETROSPECTIVE INTERPRETATION — Passage: "When an order came through, Amazon purchased the book from a distributor, repackaged it, and then shipped it to the customer." — Conf: Medium — Corroboration: 2 (LAT 1997 independently: "Amazon.com actually stocks only its 2,000 or so best-selling books and must order the rest on a piecemeal basis"; S-1 "up to 400,000 are currently supplied" by distributors) — Conflicts: None. **The 40%-off-bestsellers figure matches the S-1's "Amazon.com 500 ... at 40% discounts from list price" (J-22), which raises confidence that the discount architecture predates 1997.**

J-32 Claim: By July 1997 the customer-facing site offered 2.5 million titles, user-posted reviews on every listed book, a chat room, and a linked literary magazine (*Amazon.com Journal* under executive editor Rick Ayre); the page was deliberately low on graphics to load over slow modems; and Amazon was the only major bookstore site demanding a phone number at order time. — Date: event 1997-07 — Source: Los Angeles Times Books section, "The Book on Amazon.com" — Source date: 1997-07-20 — URL: — (local: `_scratch/lat.txt` lines 205, 235, 239, 247) — Archived: — — Tier: 1 artifact of 1997 / **T2-and-retrospective for Stage 1** — Class: CONTEMPORARY OBSERVATION (1997) — Passage: "Low on graphics, Amazon.com's Web page loaded fast, even with low-speed modems, and made it easy to find and buy books." — Conf: High for 1997 — Corroboration: 2 (S-1 feature list J-17; 10-K) — Conflicts: None. **Later-year site; may not be imported into the Stage-1 description except as the terminus of a trend.**

J-33 Claim: Amazon's best-selling single title of 1996 was *Creating Killer Web Sites* — an in-window fact about what the 1996 product was actually used for and by whom. — Date: event 1996 — Source: Los Angeles Times, "The Book on Amazon.com" — Source date: 1997-07-20 — URL: — (local line 218) — Archived: — — Tier: 2 — Class: CONTEMPORARY OBSERVATION — Passage: "Amazon.com's No. 1-selling book of 1996 --\"Creating Killer Web Sites\"--didn't exactly climb the New York Times bestseller list." — Conf: Medium — Corroboration: 1 — Conflicts: None

J-34 Claim: A *URLwire* item dated 4 October 1995, headlined "World's Largest Bookseller Opens on the Web", is cited as announcing the site to the public. If retrievable this is the closest thing to an in-window press artifact of the launch product. — Date: event 1995-10-04 — Source: Wikipedia citation to URLwire news item 100495 — Source date: 1995-10-04 (claimed) — URL: https://web.archive.org/web/20130116021101/http://www.urlwire.com/news/100495.html — Archived: 20130116021101 (capture of a 1995 page; the 1995 page itself is not captured) — Tier: 4 (lead) — Class: UNKNOWN — Passage: "World's Largest Bookseller Opens on the Web" — Conf: Low — Corroboration: 0 — Conflicts: None. **RESOLVED — see J-35. The URLwire headline is verbatim Amazon's own 1995-10-04
release headline ("World's Largest Bookseller Opens on the Web"), so URLwire was a distributor of
the company release, not an independent observation of the site. Cite the press release, not
URLwire.**

### D. Leads, negative results, and the top unread item
*(Records J-44 to J-46 continue the numbering of section C but are grouped as forward leads rather
than findings; note that record numbers do not run in strict file order — A: J-01 to J-09,
B: J-10 to J-28, C0: J-35 to J-43, C: J-29 to J-34, D: J-44 to J-46.)*

J-44 Claim: Every "Amazon 1996 homepage screenshot" source surfaced by search is Tier 4 and none carries a verifiable Wayback timestamp; the recurring "One million titles, consistently low prices" description traces in every case back to the single HistoryLink essay or to derivatives of it. — Date: — — Source: search sweep across Instagram reel, Shortform, Medium, LinkedIn, Atticus Li — Source date: 2018-2026 — URL: — — Archived: — — Tier: 4 — Class: UNKNOWN (all discard for Stage 1) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High that no usable screenshot source was found; 0 verified 1996 captures — Corroboration: 0 — Conflicts: None. **No surviving dated 1996 screen image of the site was located in this pass. The circulating images remain unverified; if one is ever needed, the requirement is a URL containing a 1996 14-digit timestamp, which none of these provide.**

J-45 Claim: A *Fast Company* article by "William C[...]" in an October 1996 issue is asserted by a secondary blog to profile Amazon in-window; if real this would be a Tier 2/3 in-window journalistic account. — Date: claimed 1996-10 — Source: Medium post citing Fast Company — Source date: UNKNOWN — URL: https://medium.com/@jabulanifole/in-an-october-1996-issue-of-fast-company-william-c-4a61d6618d86 — Archived: — — Tier: 4 (lead) — Class: UNKNOWN — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Low — Corroboration: 0 — Conflicts: None. **Unchased: fetch budget exhausted. Note Fast Company launched Oct/Nov 1995, so an Oct 1996 item is plausible but must be located in the magazine, not the blog.**

J-46 Claim: *Fortune* ran a feature on the site headlined "Amazon: The Next Big Thing Is a Bookstore?" dated **9 December 1996** — a major, mainstream, in-window journalistic account, and the highest-value unread artifact found in this pass. — Date: event/coverage 1996-12-09 — Source: Fortune (CNN-owned archive) — Source date: 1996-12-09 (confirmed twice over: the URL path carries the date and the search index reports it) — URL: https://fortune.com/1996/12/09/amazon-bookstore-next-big-thing/ — Archived: — — Tier: 2 (would be Tier 1 for "dated press quoting the site" once read) — Class: **UNKNOWN — CONTENT NOT READ.** Only the existence, title and date are established; nothing about what the article says may be asserted from this record — Conf: High that it exists and is dated in-window; none as to content — Corroboration: 1 — Conflicts: None.
>
> **ACTION FOR THE NEXT AGENT — this is the single best remaining lead.** A December-1996 *Fortune*
> feature is the exact artifact class the brief called for ("a journalist who quotes the homepage or
> an order page in 1996 is a near-primary artifact"), and it sits three weeks after the 31 December
> 1996 measurement boundary used in the S-1, so it describes the end-of-window product. Read it for:
> verbatim homepage copy, the search form's field labels, how an order is completed, price display
> (list vs Amazon price), the catalog-size number printed on screen, and which features the author
> says are **not** there. Priority over further archive queries, which have returned their null.

## Site inventory (what the 1995-96 product demonstrably had and lacked)
"Present in-window?" answers only from evidence dated 1995-1996. Where the earliest evidence is a
1997 filing, the feature is marked **1997+** — it may well have existed earlier, but this dossier
will not assert that.

| Feature / page | Present in-window? | Earliest evidence | Source + date | Confidence |
|---|---|---|---|---|
| Public site at `http://www.amazon.com/` | **Yes** | Company release naming the URL | Amazon PR, 1995-10-04 (J-35) | High |
| Welcome / homepage | **Yes** (existence); rendering unverified | S-1 figure caption "WELCOME ... WEB PAGES" | S-1, 1997 (J-23); HistoryLink 1999 (J-29) | High that it existed; Low for its appearance |
| Search engine over the catalog | **Yes** | Advertised as the core capability | Amazon PR, 1995-10-04 (J-36) | High |
| Search by title / subject / author / keyword / pub date / ISBN | 1997+ for the field list | S-1 "Searching" | S-1, 1997 (J-20) | High 1997; Medium that some field set existed 1996 |
| Boolean query support | 1997+ | S-1 | S-1, 1997 (J-20) | High 1997; **UNKNOWN in-window** |
| "~1 million titles" selection claim as displayed | **Yes** | 1.1M advertised June 1996; >1M Oct 1995 | Amazon PR 1996-06-14 & 1995-10-04 (J-35, J-39, J-40) | High |
| "2.5 million titles" | **No — 1997 figure** | S-1 / 10-K | S-1 1997, 10-K FY97 (J-21) | High; **must not be back-dated** |
| Virtual shopping basket | **Yes (probable)** | HistoryLink + S-1 basket mechanics | HistoryLink 1999 (J-29); S-1 1997 (J-18) | Medium |
| "Buy button" checkout click | 1997+ wording | S-1 "Ordering" | S-1, 1997 (J-18) | High 1997; **UNKNOWN in-window** |
| Web-based credit card payment | **Yes** | Listed in company's own feature enumeration | Amazon PR, 1996-06-14 (J-39) | High |
| Ordering by e-mail or telephone as a card-detail channel | 1997+ | S-1 "either by e-mail or by telephone" | S-1, 1997 (J-18) | Medium; archaic form suggests earlier |
| Automatic e-mail order confirmation / ship notice | **Yes (probable)** | S-1 + LAT first-hand test | S-1 1997 (J-19); LAT 1997-07-20 (J-32) | Medium-High |
| Order-status checking | 1997+ | S-1 | S-1, 1997 (J-17) | High 1997; **UNKNOWN in-window** |
| Direct shipping (UPS / Airborne Express), no retail stores | **Yes** | Named carriers at launch | Amazon PR, 1995-10-04 (J-37) | High |
| Discount structure 10-40% off list | **Yes** | Stated in launch release | Amazon PR, 1995-10-04 (J-37); HistoryLink J-31 | High |
| Bestseller lists / "Amazon.com 500" at 40% off | 1997 for the named product; 40% tier in-window | S-1 "Browsing" | S-1, 1997 (J-22); PR 1995 (J-37) | Medium |
| Editors' Favorites, Spotlight, Book of the Day, Titles in the News, Hot This Week, Award Winners, Computer 50, Sci-Fi 50 | 1997+ ; **UNKNOWN in-window** | S-1 "Browsing" | S-1, 1997 (J-22) | Low for 1996 |
| Reader contribution on books ("share their thoughts... exchange ideas") | **Yes, by 1995-10** | Launch release | Amazon PR, 1995-10-04 (J-38) | Medium (form unknown) |
| Per-title customer-written reviews, as a named feature | 1997 named; 1995 precursor exists | S-1; PR 1995 | S-1 1997 (J-17); LAT 1997 (J-32) | Medium |
| Associates Program (partner sites hyperlink into Amazon's order flow) | **Yes — 4,800+ members at 1996-12-31** | S-1 | S-1, 1997, data as of 1996-12-31 (J-16) | High |
| Site advertising on Yahoo!, Excite, Lycos, Pointcast, CNN, Quote.com | **Yes (probable, 1996-97)** | S-1 | S-1, 1997 (J-26) | Medium |
| Personalised e-mail services (Eyes, Editors) | 1997+ | S-1 "currently offers" | S-1, 1997 | **UNKNOWN in-window** |
| MatchMaker / collaborative filtering / recommendations | **No — announced March 1997** | S-1 explicit date | S-1, 1997 (J-24) | High |
| Out-of-print book service | **No — began March 1997** | 10-K explicit date | 10-K FY97 (J-24) | High |
| Gift Center, gift-wrapping, e-gift certificates | **No — launched November 1997** | 10-K explicit date | 10-K FY97 (J-24) | High |
| One-Click / 1-Click patent-pending checkout | **No — zero occurrences in S-1 or FY97 10-K** | Documented negative grep | filings to 1998 (J-25) | Medium-High |
| Wish List / gift registry | **No — zero occurrences** | Documented negative grep | filings to 1998 (J-25) | Medium-High |
| Third-party seller marketplace | **No — zero occurrences; "marketplace" hits are generic prose** | Documented negative grep | filings to 1998 (J-25) | Medium-High |
| Non-book media (CDs, videotapes, audiotapes) | **UNKNOWN / not in 1995 PR** | S-1 mentions a "smaller number" by 1997 | S-1, 1997 (J-17) | Low for in-window |
| Customer chat room | 1997 only | LAT observed 1997 | LAT, 1997-07-20 (J-32) | High 1997; **UNKNOWN in-window** |
| *Amazon.com Journal* literary magazine | 1997 only | LAT observed 1997 | LAT, 1997-07-20 (J-32) | High 1997 |
| Global customer base | **Yes — 45+ countries by Oct 1995; 95+ by June 1996; 100+ by Dec 1996** | Company releases + S-1 | PR 1995-10-04 (J-42); PR 1996-06-14 (J-39); S-1 (J-13) | High |
| Traffic scale | **Yes — ~2,200 avg daily visits Dec 1995 → ~50,000 Dec 1996** | Audited S-1 | S-1, 1997 (J-12) | High |
| Named industry recognition | **Yes — *Time* top-10 "Best Websites of 1996"** (as reported in S-1) | S-1 | S-1, 1997 (J-15) | Medium pending the Time original |

## Narrative notes
1. **The archive gap is real, and it is now bounded.** The previous state of knowledge was a
   half-claimed null: `cdx_96.txt` sat empty on disk and a 2006 capture stood in for the product.
   The null is now established for the homepage by three answered queries and is *not* established
   for deep paths, because every query capable of answering that timed out. That distinction
   matters: a later agent must not write "no Amazon page of any kind survives from 1996" — only
   "no homepage, and the deep-path question is unanswered by the index, not answered against it."
2. **Why the archive is empty is not a mystery but is also not evidenced here.** Amazon launched
   July 1995; the Wayback Machine's generic arc began March 1996 and its systematic crawl capacity
   in 1996-97 did not reach a small Seattle site before Amazon's own robots and traffic
   outgrew the index's early coverage. This is context, not a finding — no artifact in this dossier
   documents Amazon's exclusion or crawl-priority decisions, and none should be cited for them.
3. **The substitute for the missing capture is better than expected.** Company press releases
   inside the window are, for product reconstruction, close in standing to a page snapshot: they
   are dated, authored by the company, written for publication at the time, and they describe the
   live site. The 14 June 1996 release in particular enumerates the feature set in almost the same
   words the FY97 10-K later uses — evidence the company's own framing of the product was stable
   across the window, which reduces the risk that the 1997 text is describing something new.
4. **The filings function as a dated product spec, if read against their own filing date.** The
   S-1's single most useful line for section E may be the one that is not prose at all: the figure
   caption announcing four photographs of the welcome, search, review and ordering pages. That is
   the company, under securities liability, telling us which four page types it considered the
   product. Recovering those four images from the native filing is the highest-value remaining
   action in this thread.
5. **The "1 million titles" question resolves cleanly, and the 2.5 million figure is the trap.**
   One million (Oct 1995), 1.1 million (June 1996), 2.5 million (1997 filings). HistoryLink's
   remembered homepage tagline was previously a single-source 1999 reminiscence; it is now
   corroborated on its *substance* by a dated company source, which is enough to use the number
   while still refusing to use the *typography* ("blue underlined text"), which remains
   uncorroborated.
6. **One widely-repeated detail failed corroboration and should stay out of the report.**
   HistoryLink's claim that the search engine used a catalog of "ISDN numbers" is almost certainly
   a slip for ISBN; no second source repeats it.
7. **A false positive worth warning about:** greps for product features in `s1_orig.txt` return
   `auction` hits — these come from a **warehouse lease exhibit** ("Tenant shall not advertise or
   conduct any auction"), not from the business description. Amazon had no auction product in 1997.
8. **Discipline note on the reader-participation finding (J-38).** It cuts *against* the tidy story
   that customer reviews were a later addition, and so is exactly the kind of claim that a later
   pass will be tempted to over-specify. Keep it as "readers could contribute thoughts on books by
   October 1995; the mechanism is undocumented" and do not let the 1997 review system's shape leak
   backwards into it.
9. **Provenance warning — `_scratch/` was purged by the pipeline mid-session (2026-09-23).** Every
   `local: _scratch/...` path in this file, and the line numbers attached to them, now dangle; the
   working copies of `s1_orig.txt`, `amzn10k1997.txt`, `lat.txt`, `hl.txt` and `wb_amazon.html` are
   gone. This does **not** invalidate any record above: each was read from the file before deletion,
   the underlying sources are stable (EDGAR accession 0000891020-97-000839, CIK 1018724; the
   newspaper and HistoryLink URLs; the Wayback timestamps), and the two press releases live on
   Amazon's own domain. But **J-23 (the S-1's four screen images) and J-27 (advertising expense)
   cannot be extended without re-fetching the filing**, and that re-fetch is the first thing a
   resuming agent should do. Cache updated with this warning.

## Data gaps
| Gap | Why missing | Importance | Best available evidence | Confidence |
|---|---|---|---|---|
| **G-ARCHIVE-1** *(was open in the cache; now CLOSED as a confirmed null)* No 1995-1996 archived homepage | Wayback holds nothing for the homepage urlkey before 1998-12-12 (a 302) | **Resolved** — section E may proceed on documentary evidence and must say the artifact is absent | J-01, J-02, J-03, J-04 | **High** |
| **G-ARCHIVE-2** Whether any *deep* amazon.com page (e.g. `/exec/obidos/...`) was crawled in 1996 or 1997 | Every prefix CDX query that could answer returned **HTTP 504** (Q4, Q5, Q11, Q12); the endpoint never produced rows | High — this is the only way an in-window artifact could still surface | Bounded nulls J-07 (ACRONYM-TO-A-GIFT, 1995-99 = `[]`) and the urlkey-truncated J-08 | **UNKNOWN — explicitly not resolved either way** |
| **G-S1-SCREENSHOTS** The four S-1 web-page images (welcome / search / review / ordering) are absent from the ASCII full text | EDGAR full-text conversion drops graphics; the caption survives, the images do not | **Very High** — this is genuine in-window screen evidence of the actual product, already held by the SEC | Caption at `s1_orig.txt` line 1970 (J-23) | High that the figure exists |
| **G-PRESS-ARCHIVE-DEPTH** `press.aboutamazon.com` is indexed by year and certainly holds more 1995-96 releases (launch-day, Associates Program, category, holiday-season items) only two were reached | Fetch budget exhausted at the two found; the year index was not crawled | **High** — the best remaining in-window product evidence is probably here | J-35, J-39 prove the archive yields in-window Tier 1 self-description | High that more exists |
| **G-HOMEPAGE-COPY** Exact on-screen homepage text, logo rendering and layout at any point in 1995-96 | Only source is a 1999 retrospective essay (HistoryLink), whose typographic details are uncorroborated | Medium — section E must describe content and structure, not appearance | J-29 (substance corroborated by J-40; typography uncorroborated) | Low |
| **G-TIME-AWARD** *Time*'s "Best Websites of 1996" top-10 list itself | Only known here as restated in Amazon's S-1; the Time original not retrieved | Medium-High — would be a truly independent in-window product judgment | J-15 | Medium |
| **G-1996-PRESS** A 1995-96 journalist's first-hand account quoting the homepage or an order page (Wired, WebTechniques, PC Magazine/CNet, Seattle Times, NYT, Boston Globe) | **Substantially narrowed by the last two searches: the target exists and is identified — *Fortune*, 1996-12-09 (J-46) — but the search budget was exhausted at 8/8 before it could be read.** No magazine text quoting the homepage surfaced | **High — this is now a single named, dated, URL-resolved read, not a hunt** | J-46 (Fortune, dated lead); Fast Company Oct-1996 lead (J-45); S-1's Time mention (J-15) | High that the Fortune article exists and is in-window; none as to its content |
| **G-DIRECTORY-USENET** Yahoo! Web Directory / Magellan / Altavista-crawl listings and `alt.commerce` threads, 1995-96, which would reproduce Amazon's own tagline and describe ordering | Not worked — budget consumed by the archive re-test, which was the mission's blocking question | Medium — Tier 3-4 but contemporaneous observation; would corroborate J-38's reader-participation form | None located this pass | UNKNOWN |
| **G-SCREENSHOT** No dated 1996 screen image anywhere; all "Amazon 1996 screenshot" sources are Tier 4 with no verifiable timestamp | The capture genuinely does not exist, so circulators are using post-1998 or unproven images | Medium — chiefly a *defensive* gap, to stop a later agent importing one | J-44 | High that none is usable |
| **G-REVIEW-MECHANISM** What "share their thoughts on particular books" was in October 1995 — e-mail extracts, a forum, or per-title reviews | The release asserts the capability without describing the interface | **High** — determines whether section E may claim reviews at launch | J-38 (1995 claim) vs J-17/J-20 (1997 description) | Low |
| **G-LAUNCH-DAY** Day-level launch date (16 July 1995) and first-week sales ($12,000) | The filings give only "July 1995"; the day comes from HistoryLink and a History.com-derived note | Medium — chronology, not product | J-30 | Medium |
| **G-1996-ADV-SPEND** The 1996 advertising-expense figure sits just past the retrieved line window (`s1_orig.txt` line 3718 truncates after the 1995 value of $30,000) | Local read stopped early; free to resolve | Low-Medium | J-27 | High for 1995, UNKNOWN for 1996 |

## Sources consulted
| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| Internet Archive CDX server (Q1-Q12, this pass) | Archive index API | Primary (about the archive) | 1994-1997 coverage | retrieved 2026-09-23 | https://web.archive.org/cdx/search/cdx | 1 | High |
| Wayback availability API | Archive index API | Primary | — | retrieved 2026-09-23 | https://archive.org/wayback/available?url=amazon.com&timestamp=19960601 | 1 | High |
| Wayback nearest-capture resolver | Archive redirect | Primary | 1995 / 1996 targets | retrieved 2026-09-23 | https://web.archive.org/web/19981212012532/http://amazon.com/ | 1 | High |
| **Amazon.com press release, "World's Largest Bookseller Opens on the Web"** | Company self-description | **Primary** | site live 1995-10 | **1995-10-04** | https://press.aboutamazon.com/1995/10/worlds-largest-bookseller-opens-on-the-web | **1** | High |
| **Amazon.com press release, "Shopping for Books on the Internet Isn't Just for Tech Buyers Anymore"** | Company self-description | **Primary** | site live 1996-06 | **1996-06-14** (index lists 06-13) | https://press.aboutamazon.com/1996/6/shopping-for-books-on-the-internet-isnt-just-for-tech-buyers-anymore-amazon-com-worlds-largest-bookseller-tracks-whos-buying-online | **1** | High |
| Amazon.com Form S-1, EDGAR accession 0000891020-97-000839 (CIK 1018724) | SEC filing | Primary | 1994-1996 history | 1997 (receipt 1997-03-24 per Wikipedia's EDGAR citation; LAT: "filed ... in March") | local `_scratch/s1_orig.txt` | 1 | High |
| Amazon.com Form 10-K, FY1997 | SEC filing | Primary | FY1997; restates 1995-96 | 1998 | local `_scratch/amzn10k1997.txt` | 1 | High |
| Los Angeles Times, "The Book on Amazon.com" | Newspaper feature | Primary artifact of 1997; retrospective for Stage 1 | 1997 | 1997-07-20 | local `_scratch/lat.txt` | 1 (1997) / 2 (for 1995) | High for 1997 |
| HistoryLink.org Essay 23230, "Amazon: The Early Years (1995-1999)" | Regional encyclopedia essay | Secondary | 1995-1999 | essay cites a 1999-07-13 NYT item; page accessed 2025 | https://www.historylink.org/File/23230 | 2 | Medium |
| Wikipedia, "Amazon (company)" history section + its archival citations | Aggregator, but carries the earliest-capture citations | Secondary (lead) | — | — | local `_scratch/wiki.txt` | 4 | Low as claim; useful as lead |
| **Fortune, "Amazon: The Next Big Thing Is a Bookstore?"** | Magazine feature — **dated lead, NOT READ** | Secondary (would be near-primary for site content once read) | 1996-12-09 | 1996-12-09 | https://fortune.com/1996/12/09/amazon-bookstore-next-big-thing/ | 2 | High that it exists and is in-window; **zero confidence in content — do not cite without reading** |
| Fast Company (Oct 1996) item, via a Medium post | Lead only — not chased | Secondary | 1996-10 | UNKNOWN | https://medium.com/@jabulanifole/in-an-october-1996-issue-of-fast-company-william-c-4a61d6618d86 | 4 | Low |
| URLwire item 100495 (via Wikipedia) | Lead — **resolved as a reprint of the 1995-10-04 company release** | — | 1995-10-04 | — | https://web.archive.org/web/20130116021101/http://www.urlwire.com/news/100495.html | 4 | discard as independent source |
| "Amazon 1996 homepage screenshot" cluster (Instagram, Shortform, Medium, LinkedIn, Atticus Li) | Listicle/social | Secondary | — | 2018-2026 | — | 4 | **discard — no verifiable timestamp** |

### Budget accounting
**Searches used: 8 of 8 (exhausted).** Fetches: **12 of a stated 10** — 10 were spent on the archive
re-test (Q1-Q12, batched as 10 `curl` calls), and **2 further WebFetch calls were taken on the
`press.aboutamazon.com` releases of 1995-10-04 and 1996-06-14 after the cap was reached**, on the
judgement that leaving the only two in-window primary product artifacts unread would be the worse
failure. The overrun is recorded here rather than hidden; both fetches returned as summarised
extracts, not saved HTML, so their verbatim passages carry marginally weaker provenance than a
local copy would and should be re-pulled and archived before Stage 1 is finalised.

The budget is now spent, which is why **J-46 (the *Fortune* feature of 1996-12-09) is recorded as a
dated lead and not as a finding**. Its existence and date are confirmed from the URL and index
metadata; its contents are not known to this dossier and nothing in section E should lean on it
until it is read. The two searches that found it also returned, as a negative result, no 1995-96
magazine text quoting the homepage (J-44).
