# STUB LEADS — oversized Internet Archive items FOUND by this pass and deliberately NOT dumped

Created by the periodicals intake agent, 2026-09-25. Naming follows the convention already used in
`company_002_walmart/sources/periodicals/` (`STUB_LEAD_<slug>.md`): registered, sized, and left one
polite GET away, with the exact call recorded. **Nothing here was downloaded into the repository**;
the sizes are the `_djvu.txt` byte counts declared by each item's own `archive.org/metadata/<id>`
response (verified HTTP 200 this pass).

The governing constraint: do not write an artifact approaching 60,000 words (a ~400 KB text layer)
or 200 MB into a single file. Every item below is above that line, or a family of such items.

## 1. *Stores* — National Retail Dry Goods Association monthly, 1945-1961 (201 unprobed issues)

| field | value |
|---|---|
| inventory query | `identifier:(sim_stores*) AND YEAR:[1945 TO 1990]` → HTTP 200, **numFound 205** |
| coverage proved | 12 issues/yr 1945-1957, 11/yr 1958-1961 (Jul-Aug combined from 1958); annual index volumes 1970, 1971, 1972, 1974, 1975 |
| probe done | `sim_stores_1960-01_42_1` → metadata HTTP 200 → text layer **269,490 B / 38,238 words**, collection `pub_stores`/`sim_microfilm`/`periodicals`, scanner microfilm01.cebu.archive.org |
| extrapolation | ~201 issues × ~270 KB ≈ **54 MB of text, ~7.8 M words**. A single year (12 issues) ≈ 650 KB / 90,000 words |
| **the call to make instead** | per issue: `https://archive.org/metadata/sim_stores_<YYYY>-<MM>_<vol>_<iss>` → `server`+`dir` → `GET https://<server><dir>/sim_stores_<YYYY>-<MM>_<vol>_<iss>_djvu.txt` (identifiers verbatim from the 205-doc body; issue-level identifiers seen: `sim_stores_1945-06_27_6`, `sim_stores_1946-07_28_7`, `sim_stores_1947-11_29_11`, `sim_stores_1948-01_30_1`, `sim_stores_1949-10_31_10`, `sim_stores_1950-…`, `sim_stores_1955-05_37_5`, `sim_stores_1956-05_38_5`, `sim_stores_1956-08_38_8`, `sim_stores_july-august-1958_40_7`, `sim_stores_july-august-1959_41_7`, `sim_stores_1959-02_41_2`, `sim_stores_1960-01_42_1`, `sim_stores_1960-02_42_2`, `sim_stores_1960-06_42_6`, `sim_stores_1961-09_43_8`) |
| **recommended first twelve** | one issue per year 1950-1961, chosen at the *annual statistical/directory number* if the issue contents list marks one; grep each for `Walton`, `Wal-Mart`, `Ben Franklin`, `variety store`, `five-and-ten`, `discount house`, `Arkansas`, `Missouri`, `Kansas`, `Oklahoma` |
| why it is worth the budget | it is the only periodical corpus found this pass that is **monthly, in-window, sector-owned and text-layered for 1945-1961** — the nineteen years in which EDGAR, web archives and Wal-Mart's own printed report run (FY1972+) are all silent |

## 2. 1963 / 1967 Census of Business — the chain-statistical series (per-state retail detail)

| field | value |
|---|---|
| inventory queries | `identifier:(1963censusofbusi*)` → 35 items; `identifier:(1967censusofbusi*)` → **131 items**; `title:("census of business") AND YEAR:[1958 TO 1976]` → 21 |
| probed | `1963censusofbusi12unse` "1963 Census of Business. Retail Trade. Summary Statistics. Merchandise Line Sales. United States New England, Middle Atlantic v.1 pt.2" → text layer **6,620,933 B** (~1.1 M words), item total **2,691,328,799 B** (2.69 GB), collections `CensusBureauLibrary`/`fedlink`/`americana` |
| the in-window state volumes | `1967censusofbusi674uns` = Major Retail Centers in SMSA, **Arkansas**; `1967censusofbusi6727unse` = Retail Trade Merchandise Line Sales, **Missouri**; also Kansas (`…6718unse`, `…6717uns`), Oklahoma (`…6737uns`), Texas (`…6744uns`), Louisiana/Tennessee/Mississippi equivalents inside the 131-doc set |
| **the call to make instead** | per state volume: `metadata/<id>` → `<server><dir>/<id>_djvu.txt`, then **slice to the "Variety stores" / "Shopping goods stores" lines**, not the volume: expected size 0.5-6.6 MB per volume. Keep to a few thousand words per intake artifact, exactly as `STORES_NRDGA_1960-1975_EXTRACT_discount_variety.txt` does |
| what it would settle | an independent, government-published count of variety/shopping-goods stores and their sales **by state and by standard metropolitan area, for 1963 and 1967** — the denominator that Wal-Mart's own reports never printed and that no filing family carries |
| caution | these are *census* volumes: kind-of-store definitions, not company definitions. They bound the sector, they do not name Sam Walton |

## 3. Business Week — the pre-1962 issue run (the largest untouched block found)

| field | value |
|---|---|
| inventory query | `identifier:(sim_business-week*)` → HTTP 200, **numFound 1,890** |
| proved shape | issue-level SIM scans **1929 → c. 1961** (e.g. `sim_business-week_1933-01-11`, `sim_business-week_1945-06-16_824`, `sim_business-week_1946-06-08_875`, `sim_business-week_1952-06-21_1190`, `sim_business-week_1954-07-31_1300`, `sim_business-week_1956-09-29_1413`, `sim_business-week_1959-10-10_1571`, `sim_business-week_1960-05-14_1602`, `sim_business-week_1960-08-06_1614`); **1962 onward = annual index volumes only** (52 items in 1962-1976, none after 1971) |
| size class | one 1962 index = 1.27 MB / 196,549 words; a weekly issue of the same era is the same order → **~25,000-40,000 words per issue at minimum**; ~1,840 issue items |
| **the call to make instead** | do NOT bulk-pull. The economical move: pick the issues that the *retrieved 1962-1971 indexes* cite (each citation is headline + page + month/day), resolve them to `sim_business-week_<YYYY>-<MM>-<DD>_<issue>` by title, and pull only those 5-20 issues, slicing each to the cited page's passage |
| entries already converted into that form | 1962: "Discounters strive to ride out storm: Fast-growing **$6-billion industry** is facing a major …" ; "Discount store dropouts # p101, Oct.6"; "Shake-out among discounters seen as chain files in bankruptcy p83, Oct.27"; "Discounter caught in cash bind: Grayson-Robinson's plight … p169, Aug.18"; "Discount house puts on airs: Korvette moves in on fashionable New York shopping street (with cover) p72, Feb.10"; 1964: "Nielsen survey shows an increase in the number of mass merchandisers # p100, May 16"; "Small town greets the discounters: Gamble-… p90, Oct.3"; "The old five-and-ten spreads new wings: Woolworth branches out into mass merchandising p58, Nov.14"; 1970: "How Kresge became top discounter (with cover, chart and illus) p62, Oct.24"; "Retail stores get scarcer # p60, Oct.3"; 1971: "France: The French go wild over discount stores p40, Nov.20" |

## 4. Chain Store Sales and Stocks (CANADA) — found, sized, and set aside as out-of-scope

| field | value |
|---|---|
| identifiers | `31761117266239`, `31761117266247` — "CHAIN STORE SALES AND STOCKS — DBS MONTHLY STATISTICS", Dominion Bureau of Statistics, Ottawa; catalogue no. 63-001; collections `uoftgovpubs`/`robarts`/`governmentpublications`; item total **676,301,744 B** (28 files) |
| retrieved | `31761117266239_djvu.txt`, HTTP 200, **821,429 B / 134,051 words** at 2026-09-25T06:57:37Z (Vol. 17 No. 1 = January 1964; year-token census of the layer: 1964 ×61, 1965 ×52, 1966 ×64, 1967 ×52, 1968 ×73, 1969 ×77, 1970 ×92, 1971 ×61, 1972 ×61, 1973 ×58, i.e. a bound 1964→c.1973 run) |
| **state** | POSITIVE retrieval, **IRRELEVANT content** for a Wal-Mart verdict — Canadian chain retail, definition quoted from the item: "a retail chain is defined as 'an organization operating four or more retail stores in the same kind of business under the same legal ownership'". Its numeric tables OCR badly (`Grocery and combination …… 160,248 95,118 | 104,344 + 9,7`) and the back matter is largely unreadable |
| why registered not dumped | a US analogue is the item actually wanted (see SEARCH_LOG §B: `title:("statistical report on retail")`, `title:("monthly chain store sales")`, `creator:("bureau of the census") AND title:(chain)` — **all three EMPTY on IA**), and this item is 134,051 words of the wrong country |
| do-not-re-burn note | if a Canadian chain comparator is ever needed, the page-level call is `metadata/31761117266239` → `ia801603.us.archive.org/0/items/31761117266239/31761117266239_djvu.txt` → slice "Table 1 … kind of business" for the month required |

## 5. UnitedHealth — Medical Economics annual indexes 1970-1985 (found, not pulled)

`title:("medical economics") AND YEAR:[1970 TO 1985]` → HTTP 200, **numFound 25**, one index volume per
year (`sim_medical-economics_1977_54_index`, `_1980_57_index`, `_1983_60_index`, …). Same route and
same size class as the Minnesota Medicine indexes that *were* pulled (20-56 KB each, 19-56 k
characters, ~2,800-8,200 words). **The call:** `metadata/<id>` → `<server><dir>/<id>_djvu.txt` for
1975-1982, grep `HMO`, `prepaid`, `UnitedHealth`, `Burdick`, `Minnesota`. Left UNTRIED because the
Minnesota Medicine set — the closer witness to a Minnesota HMO — consumed that part of the budget.
