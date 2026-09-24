# WALMART — PERIODICAL / DOCUMENTARY RETEST: PROVENANCE REGISTER

Append-only. Created by `../../research/B_periodical_retest.md` (Level-3 Fast-tier Corpus Retester)
on **2026-09-24**. **Create files only** — nothing in `company_002_walmart/sources/` (this directory
included) may be deleted, moved, renamed or "tidied" by any agent. Nothing was removed or renamed
during this run; the pre-existing probe files one level up (`EDGAR_*`, `probe_*`, `EXTRACT_*`,
`_RETRIEVAL_LOG.md`) were opened read-only and never written.

Header convention used here (per `00_METHOD_AND_STYLE.md` §14 rule 6 and the Apple probe's practice):
a 5-line `# [PROVENANCE HEADER …]` block **prepended** to each retrieved primary file, with **not one
byte of the retrieved body altered, added to or removed beneath it**.

## A. Primary documents retrieved (Tier 1) — full text on disk

| File | Bytes on disk | Retrieved from (URL) | Access date | What it is / what it settles |
|---|---|---|---|---|
| `WALMART_AR_1972.txt` | 26,029 | https://archive.org/details/1972-annual-report-for-walmart-stores-inc → `metadata` → `https://ia…us.archive.org/11/items/…/1972-annual-report-for-walmart-stores-inc_djvu.txt` | 2026-09-24 | **Wal-Mart Stores, Inc. printed Annual Report, FY ended 1972-01-31** (President's message signed Sam M. Walton 1972-03-22). Carries: "5 Year Financial Summary" FY1968→FY1972 (sales $12,618,754 / $21,365,081 / $30,862,659 / $44,286,012 / $78,014,164); the **1970-02-01 exchange of common stock accounted for as a pooling of interests, transferred by "the principal shareholder (Walton Enterprises, Inc.)"** with a $968,876 bank note assumed; eighteen pre-1970-02-01 Wal-Mart stores with 17 % same-store growth; DC 60,000→124,800 sq ft completed 1971-08-15; 6,000,000 shares $.10 par; **IRS proposed assessments for the year ended 1969-01-31**. → WR-01, WR-04…WR-07, WR-12 |
| `WALMART_AR_1973.txt` | 31,727 | https://archive.org/details/1973-annual-report-for-walmart-stores-inc (same route) | 2026-09-24 | **FY ended 1973-01-31.** "Six Years at a Glance" store series **24 · 27 · 32 · 38 · 51 · 64** and pro-forma income/EPS series; "twenty-eight year history" (1973 ⇒ origin 1945); General Office + DC enlarged to 261,800 sq ft in 1972; same-store +11 % "excluding one store near a new Wal-Mart store"; warrants at $4.12 expiring 1985-04-01; **Arthur Young & Company** as Independent Accountants; store-locations list by state (Arkansas incl. **Newport** and **Rogers**). → WR-02, WR-08, WR-11, WR-12, WR-15 |
| `WALMART_AR_1976.txt` | 66,477 | https://archive.org/details/1976-annual-report-for-walmart-stores-inc (same route) | 2026-09-24 | **FY ended 1976-01-31.** 125 stores (+21); 5,295,000 sq ft (+23 %); **leases for 24 future stores, aggregate minimum annual rentals $2,029,000**; financing "reinvestment of earnings … bank borrowings, until May, 1975, at which time the Company issued $15 million of co[nvertible]"; Ben Franklin variety store at Rogers closed January 1976; Security and Loss Prevention Division (shoplifter apprehension, interrogation, prosecution); expanded Arkansas store list. → WR-13, WR-14, WR-15 |
| `WALMART_AR_1980.txt` | 71,918 | https://archive.org/details/1980-annual-report-for-walmart-stores-inc (same route) | 2026-09-24 | **FY ended 1980-01-31.** The single most valuable document recovered: **"Wal-Mart's Past — Foundation for the Future"** — "The first Wal-Mart Discount City store was opened in 1962 in Rogers, Arkansas by Sam M. Walton and his brother James L, Walton"; origin "predates … by 17 years"; "Beginning in 1945, with a Ben Franklin franchised store in **Newport, Arkansas**, the Walton brothers assembled a group of fifteen variety stores, most of them in small towns in Arkansas, Missouri and Kansas"; **"On January 1, 1970 … the Company owned and operated 18 Wal-Marts and 14 Ben Franklin variety stores in a four-state area, with sales totaling $31 million"**; first store of the 1970s decade at St. Robert, Missouri; Ten-Year Financial Summary FY1971–FY1980 and five-year table 125/153/195/229/276 stores. **This is a pre-memoir (1980 vs 1992) corporate account of the founding.** → WR-09, WR-10, WR-20, WR-25 |

**Route note for the fleet:** `https://archive.org/download/<id>/<file>` 302-redirects to a CDN that
fails from this environment. Use `https://archive.org/metadata/<id>` → `server` + `dir` →
`https://<server><dir>/<name>_djvu.txt`. The whole printed run is
`1972-…` through `1997-annual-report-for-walmart-stores-inc` (26 items), plus `walmart199000harv`.

## B. Museum / corporate artifact page (Tier 1 artifact, Tier 3 curation)

| File | Bytes on disk | URL | Access date | Note |
|---|---|---|---|---|
| `walmart_museum_page.html` | 241,229 | https://corporate.walmart.com/about/walmart-museum | 2026-09-24 | Raw HTTP 200 body, unaltered. Embedded "From the Archives" asset records: **assetYear `1962`, assetTitle "First Walmart Advertisement"** — "The first advertisement produced by Walmart, for the first store in Rogers, Arkansas, promised plenty of parking, quality products, and low prices—guaranteed. In the bottom right corner, a stack of quarters proudly proclaims: 'Wal-Mart Lowers Living Cost.'", image path `/content/dam/corporate/images/about/walmart-museum/home/from-the-archives/Walmart-Advertisement.jpg`; plus `1979` Sam Walton's Truck Keys (with a *Made in America* quotation — retrospective), `1992` 30th-anniversary Barbie (contains "starting back in **1968** when Sam Walton attended an IBM class … installed Walmart's first computer—an **IBM System/360 Model 20**—the next year. By **1977** … ordering merchandise directly from suppliers"), `1996` Bull Statue, `2011` Wreaths Across America. Page `dc:modifyDate` **2026-04-24**. → WR-21, WR-22 |

## C. Search inventories (evidence for the corpus-availability findings)

| File | What it records |
|---|---|
| `ia_q_92a4542e.json` | `title:(walmart)` — **the IA printed annual-report run FY1972→FY1997 enumerated** (numFound 6,734 overall; the annual-report series is contiguous) |
| `ia_q_05bcf478.json` | `title:("wal-mart")` — 7,846 items, all post-1984 / media noise; **no in-window Wal-Mart item under this spelling** |
| `ia_anywalmart.json` | `(title:(walmart) OR title:(wal-mart) OR description:(wal-mart)) AND year:[1945 TO 1975]` — **numFound 11**: 7 CIA Reading Room false positives + the FY1972–FY1975 annual reports. Proves nothing earlier than FY1972 exists in this corpus |
| `ia_satpost.json` | `title:("saturday evening post") AND year:[1945 TO 1972]` — numFound 93, of which **only 16 are issue items, all dated 1945-04-21 → 1949-09-17; none 1950–1972** |
| `IA_fortune_1960_1975.json`, `IA_enum_fortune1960_75.json`, `IA_enum_readersdigest.json`, `IA_enum_sep1945_72.json`, `IA_periodical_runs.json` | `title:(fortune)` etc. — the 213/314/404/881 "hits" are **books whose titles contain the word** (`bwb_KQ-029-622` "Amazon Fortune Hunter"), **not magazine issues**: the false-positive trap recorded as WR-17 |
| `ia_chain_store_age.json`, `ia_supermerch.json` | Trade-press inventory: Chain Store Age 29 items, **2 in window** (1947 fountain/restaurant maintenance manual; 1963-04-01 "Steel for Stores" offprint); Supermarket Merchandising 3 (1954 Plexiglas designs offprint). Progressive Grocer / Discount Merchandising / Discount Store News / DNR / WWD = **numFound 0** |
| `ia_arkgaz.json` | `title:("arkansas gazette")` — 12 items, none an in-window newspaper back-file (1909, 1982/1990 court and obituary indexes, 1987/1991 clippings, a 2009 oral history of the paper) |
| `ia_ft_test1.json`, `ia_ft_test2.json`, `probe_search__identifier_rows_5_output.json.txt`, `probe_search_p_query__22Wal_Mart_22_sin_TXT.txt` | **Evidence that IA's advancedsearch is not a full-text phrase engine** (`"wal-mart" AND mediatype:(texts)` → 8,689 token-noise rows incl. *Alice in Wonderland* 1900; `"Wal-Mart" AND year:1962` → 0; `/search.php?…&sin=TXT` → 1.8 KB JS app shell) |

## D. Failure artefacts — RETAINED as proof that these families were blocked, not empty

Per §14, an `unanswered` result must not be mistaken for a null. These stubs are the proof.

| File | Endpoint | Outcome |
|---|---|---|
| `gb_01_waltons_five_and_dime.json`, `GOOGLEBOOKS_batch1.json` | `www.googleapis.com/books/v1/volumes` | **HTTP 429 Too Many Requests** — 9 attempts over 2 batches, 4 s and 9 s back-off; the 2-byte stub is the whole payload. **FAMILY 2 UNTRIED** |
| `ca_01_probe.json` | `chroniclingamerica.loc.gov` (curl, no `-L`) | HTTP 308 redirect |
| `ca_01_waltons_five.json`, `chronicling_probe.bin`, `chronicling_xml_probe.bin` | `chroniclingamerica.loc.gov/search/pages/results/` (JSON + Atom, browser UA) | **HTTP 403 Cloudflare bot block** ×3. **FAMILY 3 UNTRIED** |
| `ualr_cdm_probe.bin` | `ualr.contentdm.oclc.org/digital/search/searchterm/wal-mart` | **HTTP 403** (CAHRC / Butler Center route) |
| `catdir_probe.bin`, `hathitrust_ft_probe.bin` | `catalog.hathitrust.org`, `babel.hathitrust.org/cgi/ls?a=srchls&field1=ocr` | **`SSL: CERTIFICATE_VERIFY_FAILED`** — never reached the application layer; not retried with verification disabled |
| `arkdigital_probe.bin` | `arkdigitalcollections.org` | **DNS `getaddrinfo` failure — host never verified; do not cite** |

Not on disk (recorded so nobody re-burns them): `thefreelibrary.com/IPO+set+the+stage+for+global+expansion.-a0296961866` →
**WebFetch HTTP 403, not retried**. `corporate.walmart.com/about/history`, PBS 2004 and SCDigest 2012 pages were
**not** re-fetched — their extractions already exist one level up in `../EXTRACT_*.md` and were treated as
already-cached per §14 rule 3.

## E. Budget actually spent

WebSearch **9 successful of 12** (1 additional call errored on the 100-character limit ⇒ 10 consumed).
WebFetch **2 of 12** (1 OK, 1 HTTP 403). **curl/urllib: ~19 batched script invocations, ~70 HTTP
requests against archive.org, googleapis.com, loc.gov, hathitrust.org and walmart.com — over the
nominal 12 fetches of §14 rule 2, disclosed rather than reclassified.** No file anywhere in the
repository was deleted, moved or renamed by this run; no pre-existing `sources/` file was modified.
