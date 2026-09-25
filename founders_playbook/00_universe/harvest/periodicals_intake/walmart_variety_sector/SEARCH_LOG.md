# SEARCH LOG — target 1: WALMART / VARIETY-STORE SECTOR periodicals via Internet Archive

Agent: periodicals intake (route = Internet Archive, the one periodical host that works from this
machine). Run window **2026-09-25T06:40Z → 07:12Z**. Every row is one network request, listed in
`../_REQUEST_LEDGER.tsv` with timestamp, HTTP status and byte count. Nothing here was inferred:
`numFound` values are copied from the response bodies.

States, per the HARVEST README firewall — **POSITIVE** (retrieved, identifier given) ·
**EMPTY** (query answered 200 with the result shown; catalogue holds nothing for *those exact
params*) · **UNANSWERED** (the request failed; URL + status + bytes given) · **UNTRIED**
(deliberately not attempted; the call and the reason are stated).

## A. Trade titles the brief named

| # | Query as issued | numFound | State | What it means |
|---|---|---|---|---|
| A01 | `collection:("pub_chain-store-age") AND mediatype:(texts)` | **0** | EMPTY (this param form) | see C below |
| A05 | `collection:"pub_chain-store-age" AND mediatype:(texts)` | 0 | EMPTY | same, quoting variant |
| A06 | `collection:(pub_chain*) AND mediatype:(texts)` | 0 | EMPTY | prefix variant |
| B05 | `collection:(pub_chain-store-age)` | 0 | EMPTY | unfiltered |
| C01 | `identifier:(sim_chain-store-age*)` | 0 | EMPTY | SIM naming pattern tried against the one title that *is* SIM-digitised (Business Week) — CSA does not use it |
| G02 | `collection:(sim_microfilm) AND title:("chain store")` | 1 | EMPTY-for-issues | the single hit is the collection **node** `pub_chain-store-age` (mediatype=collection, its own metadata says `date 1974-2014`), which exposes **no child items in the search index** |
| A02 | `identifier:(chain-store-age*)` | 2 | POSITIVE (2 items) | `chain-store-age-fountain-restaurant-1947-maintenance-manual-1947` (1947) and `chain-store-age-steel-for-stores` (1963-04-01) — offprints, not issues. Confirms the pre-existing register (`company_002_walmart/sources/periodicals/ia_chain_store_age.json`, 29 items / 2 in window); no new in-window CSA text found |
| A03 | `title:("discount store news")` | 16 | EMPTY-for-window | 16 items = UIC microfilm **volume-level** records `micro_IA40706901_0406` … `micro_IA40706953_0486`, **1980-1995 only**; nothing 1961-1979 |
| A04 | `title:("discount merchandising")` | **0** | EMPTY | the other discount trade weekly is not on IA under this title |
| A17 | `title:("discount store") AND mediatype:(texts) AND YEAR:[1960 TO 1980]` | 4 | EMPTY-for-trade | 2 × ERIC/microform education records (1968), the 1980 DSN microfilm item, nothing trade |
| A08 | `title:("business week") AND YEAR:[1962 TO 1976]` | 66 | see A12/B04 | |
| A09 | `title:(businessweek) AND YEAR:[1962 TO 1976]` | 0 | EMPTY | one-word spelling is not indexed |
| A12 | `identifier:(sim_business-week*) AND YEAR:[1962 TO 1976]` | **52** | **POSITIVE** | the whole in-window Business Week holding = **annual index volumes**, 1962-1971 (several duplicate `_0/_1` bindings per year); **1972-1976: none** |
| A13 | `identifier:(sim_business-week*)` (all years) | **1,890** | POSITIVE-as-inventory | issue-level SIM scans exist **1929 → c. 1961** (e.g. `sim_business-week_1952-06-21_1190`, `sim_business-week_1960-05-14_1602`); after 1961 the series becomes index-only. So the pre-1962 trade press *is* on IA, and it is the only family that reaches Sam Walton's Newport/Ben-Franklin decade |
| B03 | `title:("ben franklin stores") OR title:("ben franklin shops")` | 2 | LEAD_ONLY | `gov.uscourts.ilnb.570852` "Ben Franklin Stores Inc" and `gov.uscourts.nmd.5661` "Nanez v. Ben Franklin Stores" — federal court docket items, **not** corporate print |
| A14 | `title:("ben franklin") AND mediatype:(texts) AND YEAR:[1945 TO 1980]` | 36 | EMPTY | all 36 are about Benjamin Franklin the person (1948 biography, 1956 portraits, NASA/DTIC). **Ben Franklin Stores' own print does not appear under a corporate-records identifier on IA** |
| A18 | `creator:("ben franklin stores")` | **0** | EMPTY | the productive `creator:` clause (it worked for Apple) returns nothing for this company |
| A15 | `(title:("variety store") OR title:("five and dime") OR title:("five and ten")) AND mediatype:(texts) AND YEAR:[1920 TO 1975]` | 25 | EMPTY | noise: *Five and Ten* novels/films, Woolworth biographies, ERIC follow-up studies, 2 CIA reading-room cables — the token-noise trap WR-17 warns about |
| C03 | `identifier:(pub_discount*) OR identifier:(pub_ben-franklin*) OR identifier:(pub_variety*)` | 1 | EMPTY | the one hit `pub_variety` is the show-business weekly *Variety* |
| C04 | `identifier:(sim_supermerch*) OR identifier:(sim_progressive-grocer*) OR identifier:(sim_variety*) OR identifier:(sim_national-discounters*)` | 3,127 | NOT-EVIDENCE | the 60 docs sampled are **all** `sim_variety_*` (entertainment trade). "variety" is a false friend here |

## B. The "chain statistical yearbook / trade directory" question (named the most valuable find)

| # | Query | numFound | State |
|---|---|---|---|
| C05 | `(title:("yearbook") OR title:("directory") OR title:("statistical")) AND (title:("retail") OR title:("chain store") OR title:("discount") OR title:("variety")) AND YEAR:[1950 TO 1976]` | **1** | **EMPTY** — the single hit is `employmentpopula00unit` (SMSA population changes, 1972). **No Chain Store Age statistical yearbook, no discount-store directory, no trade yearbook on IA for 1950-1976** |
| A10 | `title:("chain store") AND mediatype:(texts) AND YEAR:[1955 TO 1975]` | 1 | EMPTY (the 1963 "Steel for Stores" offprint) |
| A11 | `(creator:("bureau of the census") OR creator:("united states bureau of the census")) AND title:(chain)` | **0** | EMPTY — census chain-store series is **not** findable by `creator:` here |
| D02 | `title:("statistical report on retail") OR title:("retail food stores, drug stores") OR title:("monthly chain store sales")` | **0** | EMPTY |
| B01 | `title:("chain store sales") AND mediatype:(texts)` | 2 | POSITIVE **but wrong country** — see D below |
| A16 | `title:("census of business") AND YEAR:[1958 TO 1976]` | 21 | POSITIVE — 1958/1963/1967 Census of Business volumes incl. `1963censusofbusi12unse` |
| B02 | `identifier:(1963censusofbusi*)` | 35 | POSITIVE-as-inventory |
| D04 | `identifier:(1967censusofbusi*)` | **131** | **POSITIVE-as-inventory** — the 1967 Census of Business retail volumes, per-state ("Major Retail Centers in SMSA", "Retail Trade: Merchandise Line Sales") |
| D06 | `identifier:(1967censusofbusi*) AND title:(arkansas)` | 1 | POSITIVE — `1967censusofbusi674uns` "Major Retail Centers in SMSA. Arkansas". Missouri/Kansas/Oklahoma/Texas/Pennsylvania volumes are in the D04 set: **the five states of the Walton footprint, 1967, in one catalogue** |
| G01 | `collection:(periodicals) AND (title:(retail) OR title:(discount) OR title:(grocer) OR title:(chain) OR title:(merchandising)) AND mediatype:(texts)` | **989** | POSITIVE-as-inventory — the retail trade-press block of IA's periodicals collection: `sim_stores_*` (see C), `sim_merchandising-week_*` (Electrical Merchandising), `sim_progressive-grocer_1989_68_index`, `retail-business_1976-07_index` |
| D03 | `title:("chain stores") AND mediatype:(texts) AND YEAR:[1930 TO 1975]` | 14 | LEAD_ONLY — Lebhart *Chain Stores in America* 1859-1950/59/62 (3 editions), *Chain stores and legislation* 1939, price lists. Books, not the statistical serial |

## C. THE FIND — *STORES*, monthly of the National Retail Dry Goods Association

| # | Query | numFound | State |
|---|---|---|---|
| G05 | `identifier:(sim_stores*) AND YEAR:[1945 TO 1990]` | **205** | **POSITIVE (inventory) — complete monthly run 1945-1961**: exactly 12 items/year 1945-1957, 11/year 1958-1961, plus **annual index volumes 1970, 1971, 1972, 1974, 1975** (`sim_stores_1970_52_index` … `sim_stores_1975_57_index`). Title shifts inside the run: "The Bulletin of the National Retail Dry Goods Association" (1945-46, 1940s back-matter) → "Stores" (1947- ). Collection `pub_stores` / `sim_microfilm` / `periodicals` |

Retrieved and read in this pass (all HTTP 200, byte-exact vs metadata-declared size):

| identifier | item | text layer | state |
|---|---|---|---|
| `sim_stores_1960-01_42_1` | Stores Jan 1960 Vol 42 No 1 | 269,490 B / 38,238 words, `_djvu.txt` present | **POSITIVE** — `STORES_NRDGA_1960-1975_EXTRACT_discount_variety.txt` |
| `sim_stores_1970_52_index` | Stores 1970 Vol 52 Index | 16,985 B / 2,364 words | POSITIVE (same extract) — 0 discount/variety/Wal-Mart hits |
| `sim_stores_1974_56_index` | 1974 Vol 56 Index | 24,487 B / 3,527 words | POSITIVE — "The Discount Store Manager — MRI/duPont Study. Nov p. 26" |
| `sim_stores_1975_57_index` | 1975 Vol 57 Index | 18,054 B / 2,460 words | POSITIVE — "Could Nostalgia Reverse the Trend Toward Discount Retailing", Jan p. 40 / Feb p. 39 |

**Why it matters and what it does not settle.** IA holds the variety-chain sector's own monthly,
**issue by issue, for 1945-1961 — the nineteen years that EDGAR, web archives and the company's own
printed reports reach worst** (Wal-Mart's printed report run starts FY1972). It does **not** cover
1962-1969 (the founding decade): the monthly digitisation stops at 1961 and resumes only as annual
indexes in 1970-1975. Text layers verified present on one issue and three indexes; the other 201
issues were **not** individually probed — treat their layer presence as *expected, unproven*.

## D. Registered but deliberately not dumped (volume safety) — see `STUB_LEAD_oversize_items_registered_not_downloaded.md`

| item | what | why not dumped |
|---|---|---|
| `31761117266239` + `31761117266247` | "CHAIN STORE SALES AND STOCKS — DBS MONTHLY STATISTICS" | **CANADA**, Dominion Bureau of Statistics (Univ. of Toronto scan) — wrong country for a Wal-Mart verdict. Pulled once anyway to prove that: 821,429 B / 134,051 words, Jan 1964 → c. 1973, **OCR of the numeric tables is badly garbled** (`160,248 95,118 \| 104,344 + 9,7`, tail is unreadable). Recorded as a POSITIVE retrieval and an IRRELEVANCE finding |
| `1963censusofbusi12unse` | 1963 Census of Business, Retail Trade, Merchandise Line Sales, US/New England/Middle Atlantic v.1 pt.2 | text layer **6,620,933 B** (~1.1 M words), item 2,691,328,799 B — over the cap by ~18×. Page-level call recorded in the stub file |
| Business Week index text layers, all six years | 1962 / 1964 / 1966 = 1.27 MB, 1.29 MB, 1.18 MB; 1969/1970/1971 = 0.71/0.34/0.40 MB | pulled whole to scratch **outside the repo**, mined, ~6,500 words of topic blocks transcribed into `BUSINESSWEEK_INDEX_1964-1971_EXTRACT_discount_retail.txt` (1962 and 1966 appended as a second pass). Six years retrieved: 1962, 1964, 1966, 1969, 1970, 1971 |

## E. Honest negatives on content (searched, zero)

* Business Week annual indexes 1962, 1964, 1966, 1969, 1970, 1971 → **no "Wal-Mart" and no
  "Walton" entry**; the only `Walton` string in the four originally-pulled years is
  `1970: "G. H. Dreyfus, H. C. Walton p4, Aug.29"` (a person). No "Ben Franklin", no "five-and-dime".
* Stores 1960-01 → `Walton` 0, `Wal-Mart` 0, `Ben Franklin` 0, `variety store` 0, `Arkansas` 0
  (but `discount` 25, incl. the mandatory-functional-discount-bills editorial).
* Stores 1970/1974/1975 indexes → `Wal-Mart` 0, `Ben Franklin` 0, `variety` 0.
* 1962 and 1966 BW indexes were downloaded second (07:09Z) and are in the ledger. Their content
  test: `Wal-Mart` **0** in both years; `Walton` 1 in 1962 (`WALTON, William — Holiday Inns …
  p47, Jul.14`, a hotel man) and 0 in 1966; `discount` 88 in 1962 / 27 in 1966; `Ben Franklin` 0;
  `variety store` 0; `mass merchandising` 0. Their topic blocks are in the extract under
  "APPENDED SECOND PASS".

## F. UNTRIED (stated, with the call and the reason it waited)

1. `title:("chain store age executive") AND YEAR:[1975 TO 1990]` — the successor title; the 1980s
   `micro_IA*` records suggest the Executive edition is the only surviving spine. Reason: CSA's
   in-window decade (1962-75) already proved absent four different ways above.
2. The 201 unprobed *Stores* issues 1945-1961: per-issue `metadata/<id>` (201 requests) then
   `GET https://<server><dir>/<id>_djvu.txt` (201 requests) for ~7.8 M words. Reason: exceeds this
   intake's entire budget; the right next move is 12 issues (one per year) targeted at
   "Ben Franklin", "Walton", "variety store" + the association's annual statistical numbers.
3. `identifier:(sim_stores*) AND YEAR:[1962 TO 1969]` — cheap check that the 1962-69 gap is a scan
   gap and not a search artifact. Reason: budget was spent on Business Week 1962/1966 instead,
   which is the higher-value of the two.
4. Ben Franklin Stores prospectuses/10-Ks via `corporate_print` family (`creator:` +
   `report_terms`, 1948-1975) — this is the *filings* family, out of this brief's scope.
5. *Monthly Weather Review* — **explicitly excluded by the brief as irrelevant**; not queried, and
   no request spent.
