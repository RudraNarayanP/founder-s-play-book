# PERIODICALS INTAKE — MANIFEST

Area: `founders_playbook/00_universe/harvest/periodicals_intake/`
Agent: evidence registrar (periodicals intake). Created **2026-09-25**, run window
**06:40Z → 07:16Z**. Nothing outside this directory was written.

## 1. Why this area exists and what direction it writes in

Method `00_METHOD_AND_STYLE.md` §14 rule 6 requires **four corpus families** before a company may be
rated anything other than exemplar-capable: filings, web archives, **periodical corpora**, and
auction/museum records. Three routes to periodicals fail from this machine with bot challenges —
**Chronicling America HTTP 403, HathiTrust TLS/0-results, Google Books HTTP 429** — while
**Internet Archive works**: it delivered Wal-Mart's printed annual reports and, in this pass, six
Business Week index volumes, seven Minnesota Medicine index volumes, five trade-magazine text
layers and a census inventory. `.github/workflows/harvest.yml` exists to retry the blocked hosts
from unblocked egress; it has not fired yet.

So this area is the **unblocked route's intake only**. It writes in one direction:

* **WRITES HERE** — the 18 files listed in §6.
* **NEVER TOUCHED** — `company_002_walmart/sources/periodicals/` (concurrently read by another
  agent), any `research/*.md`, any register CSV, `MASTER_RESEARCH_LOG.md`, `candidates.csv`,
  `harvest/_MANIFEST.md`, `queries.json`, `periodical_harvest.py`. Nothing anywhere was deleted,
  moved, renamed or tidied (§14 rule 4). Pre-existing files were opened read-only.
* Raw response bodies — **21 text layers totalling 8.17 MB** (largest 1.29 MB) and **77 catalogue
  JSONs** (48 search + 29 item metadata) — were kept in an **OS scratch directory outside the
  repository**, and are represented here by identifier, byte count, character offset and the
  verbatim passages selected. Nothing bulk was written into the repo: the largest artifact here is
  44,966 B.

## 2. Request accounting (the budget the brief set)

**100 network requests spent of the 120 hard cap.** All sequential, `2.5 s` per-request delay,
UA `FoundersPlaybook-periodicals-intake/1.0 (…contact: research@example.org)`, TLS verification ON.

| | count |
|---|---|
| HTTP 200 | **99** |
| HTTP 0 (TLS `CERTIFICATE_VERIFY_FAILED`, 0 bytes) | **1** |
| 429 / 503 / retry-after events | **0** — no back-off was ever armed into action; nothing was blind-retried |
| `advancedsearch.php` queries | 48 |
| `metadata/<identifier>` calls | 29 |
| `_djvu.txt` text-layer GETs | 22 (21 + the 1 TLS-failed `download/` experiment) |
| hosts contacted | `archive.org` **79** (48 search + 29 metadata + the 1 failed `download/` test) · **21** text-layer GETs spread over **20 distinct** `ia*.us.archive.org` / `ia6*.us.archive.org` item servers |

Every request is one row of **`_REQUEST_LEDGER.tsv`** (UTC timestamp · status · bytes · URL · note).
That file is the re-walk proof for everything below.

## 3. State table — target → state (the four states kept distinct)

### Target 1 · Walmart / variety-store sector

| route | state | evidence |
|---|---|---|
| **Business Week annual indexes, 1962/1964/1966/1969/1970/1971** | **POSITIVE** | `sim_business-week_1962_index` (1,273,570 B), `_1964_index_0` (1,286,804), `_1966_index_0` (1,177,551), `_1969_index_0` (711,758), `_1970_index_0` (336,463), `_1971_index_0` (397,185) — all HTTP 200, byte-exact vs metadata. → `walmart_variety_sector/BUSINESSWEEK_INDEX_1964-1971_EXTRACT_discount_retail.txt` (filename says 1964-1971; the file now also carries an appended 1962 + 1966 second pass — **not renamed, per rule 4**) |
| **Business Week SIM run (whole series)** | **POSITIVE (inventory)** | `identifier:(sim_business-week*)` → numFound **1,890**; issue-level scans **1929 → c.1961**; 1962-1976 = 52 items, **index volumes only**; **no 1972-1976 at all** (EMPTY on that param form) |
| **\*Stores\* / NRDGA monthly** | **POSITIVE** | `identifier:(sim_stores*) AND YEAR:[1945 TO 1990]` → numFound **205 = complete monthly run 1945-1961** + annual indexes 1970/71/72/74/75. Retrieved: `sim_stores_1960-01_42_1` (269,490 B), `_1970_52_index` (16,985), `_1974_56_index` (24,487), `_1975_57_index` (18,054). → `walmart_variety_sector/STORES_NRDGA_1960-1975_EXTRACT_discount_variety.txt` |
| **Census of Business 1963 / 1967 (the "chain statistical" family)** | **POSITIVE (inventory), content UNTRIED** | 35 + **131** items; Arkansas `1967censusofbusi674uns`, Missouri `…6727unse`, Kansas/Oklahoma/Texas in-set. Probed one: `1963censusofbusi12unse` text layer **6,620,933 B / item 2.69 GB** → registered, not dumped |
| Chain Store Age | **EMPTY** (5 independent param forms) | `collection:"pub_chain-store-age"` 0 · `collection:(pub_chain*)` 0 · `collection:(pub_chain-store-age)` 0 · `identifier:(sim_chain-store-age*)` 0 · `collection:(sim_microfilm) AND title:("chain store")` → the one hit is the **collection node** `pub_chain-store-age` (mediatype=collection, own metadata `date 1974-2014`, **no indexed children**). 2 offprints only: `chain-store-age-steel-for-stores` (1963), `…-fountain-restaurant-1947-…` |
| Discount Store News | **EMPTY for the window** | `title:("discount store news")` → 16 items, **all** UIC microfilm year-records 1980-1995 (`micro_IA40706901_0406` … `_IA40706953_0486`) |
| Discount Merchandising | **EMPTY** | `title:("discount merchandising")` → 0 |
| **Trade directory / "chain statistical" yearbook 1964-1970, as such** | **EMPTY** | `C05` (yearbook/directory/statistical × retail/chain/discount/variety, 1950-76) → **1** irrelevant hit; `title:("chain store") AND YEAR:[1955 TO 1975]` → 1 (the 1963 offprint); `title:("statistical report on retail") OR … OR title:("monthly chain store sales")` → **0**; `creator:("bureau of the census") AND title:(chain)` → **0** |
| Ben Franklin Stores' own print | **EMPTY** | `creator:("ben franklin stores")` → **0**; `title:("ben franklin") …YEAR:[1945 TO 1980]` → 36, all about Benjamin Franklin; `title:("ben franklin stores") OR title:("ben franklin shops")` → 2, both **court docket** items (`gov.uscourts.ilnb.570852`, `gov.uscourts.nmd.5661`) = LEAD_ONLY |
| Canada's chain-store statistics (found by accident) | **POSITIVE but OUT OF SCOPE** | `31761117266239` "CHAIN STORE SALES AND STOCKS — DBS MONTHLY STATISTICS", 821,429 B / 134,051 words, Jan-1964 bound run; Dominion Bureau of Statistics (Ottawa); numeric-table OCR garbled. Registered in the stub file so it is not re-burnt |
| *Monthly Weather Review* | **UNTRIED — by instruction** | the brief declares it irrelevant; **0 requests spent** |

### Target 2 · Apple / microcomputer sector (only NEW titles or NEW years, as required)

| title | state | what is new |
|---|---|---|
| **BYTE** | **POSITIVE** | **NEW YEARS 1975 (4 issues), 1978, 1979 (12 each), 1980 ×11, 1981 ×11, 1982-1995; 8 new 1977 months.** numFound 230. Retrieved: `byte-magazine-1977-09` (860,344 B / 135,895 words) and `byte-magazine-1975-09` (443,605 B / 63,757 words). Held years **not** re-downloaded |
| **Kilobaud** | **POSITIVE (NEW TITLE)** | numFound **179**, 1977-1984. Layer proved on `Kilobaud197701` → **`Kilobaud 1977-01_djvu.txt` 746,892 B** (amends the house note that Kilobaud is scan-only — that holds for the probed 1976 items, not 1977+) |
| **Interface Age** | **POSITIVE (NEW TITLE)** | numFound **99**, 1975-1983. Layer proved on `InterfaceAge197910` → `Interface Age 1979-10_djvu.txt` **643,138 B**. `InterfaceAge197610` → **UNANSWERED** (metadata HTTP 200 / 2-byte `{}`) |
| **Creative Computing** | **POSITIVE (NEW TITLE)** | numFound **197**, 1974-1985. Retrieved `CreativeComputing_v03n06_NovDec1977` (691,621 B / 100,162 words) → 3 "Apple" hits, **no Apple review**; extract shipped |
| **Popular Electronics** | **POSITIVE (inventory), layer UNTRIED** | numFound **144**, 1974 ×16 / 1975 ×24 / 1976 ×29 / 1977 ×25 / 1978 ×26. No `metadata/<id>` spent → text-layer presence unknown, asserted nowhere |
| BYTE 1975-09 content test | **EMPTY (documented negative)** | 0 "Apple" occurrences in the first issue ever published (Sept 1975) |

### Target 3 · UnitedHealth Group (company_003)

| route | state |
|---|---|
| ***Minnesota Medicine* annual indexes 1974-1980** | **POSITIVE — all seven retrieved** (`sim_minnesota-medicine_1974_57_index` 56,258 B · 1975 35,570 · 1976 33,240 · 1977 31,793 · 1978 19,672 · 1979 32,452 · 1980 28,680; HTTP 200 each, byte-exact). → `unitedhealth_minnesota/MINNESOTA_MEDICINE_INDEX_1974-1980_EXTRACT_hmo_debate.txt`. Yields dated HMO entries at pp 797 (1979), 77 / 231 / 391 (1980), a Physicians Health Plan interview at p 665 (1978), PL 93-641 at p 511 (1976) |
| *Minnesota Medicine* **issues** in 1968-1986 | **EMPTY** — `identifier:(sim_minnesota-medicine*) AND YEAR:[1968 TO 1986]` → 19 items = **index volumes only**, one per year, unbroken; issue scans on this route stop at 1963 |
| Company-name presence in those 7 volumes | **EMPTY** — grep of full layers: `Burdic` 0 · `Charter Med` 0 · `Metropolitan Health` 0 · `United Health` 0 · `prepaid` 0 · `closed panel` 0 |
| *Abstracts of Health Care Management Studies* (health-management trade serial) | **POSITIVE (inventory), content UNTRIED** — SIM annual indexes vol 4 (1968) → vol 22 (1986), **one per year, unbroken** |
| *Medical Economics* annual indexes | **POSITIVE (inventory), UNTRIED** — numFound 25, 1970-1985 |
| Minnesota business press 1974-1980 | **EMPTY** — 6 hits across seven magazine titles, none in window except the 1979 book `landofgiantshist0000lars`; `creator:("health planning council of minnesota")` → **0** |
| 1975-06 HMO feasibility study `preliminaryfeasi00char` | **POSITIVE then KILLED** — metadata shows "**on the Monterey Peninsula**", collection `navalpostgraduateschoollibrary`: a California specimen, not Charter Med |
| DHEW/HCFA HMO directories & statistics | **EMPTY for the window** — 14 hits, all 1983-1991 S/HMO demonstration reports; directory forms → 2 hits, 2007 and 2018 |
| Chronicling America (Minneapolis/St. Paul dailies) | **UNTRIED this pass, 0 requests** — still the 403-blocked route; the nightly runner's job |
| Google Books / HathiTrust | **UNTRIED, 0 requests** — 429 / TLS. **Family 3 remains UNANSWERED for company_003, and a verdict must say so, not "empty"** |

## 4. The two finds most likely to change a depth verdict

1. **`*Stores*` (National Retail Dry Goods Association), complete monthly run 1945-1961 — 205
   digitised issues with text layers.** This is periodical print, in-window, sector-owned and
   monthly across precisely the nineteen years in which every other family this project owns is
   silent: EDGAR stops ~1994, web archives ~mid-1990s, and Wal-Mart's own printed report run starts
   FY1972. Sam Walton's Newport/Missouri Ben-Franklin decade is *inside* this run. One issue was
   read (Jan 1960, 38,238 words, 25 "discount" hits including a presidential editorial on the
   mandatory functional-discount bills), and it proved the class is retrievable and legible.
   Twelve targeted issues (one per year 1950-1961) is a bounded, ~24-request job that could add a
   new family of contemporaneous Tier-1 records to company_002's earliest period.
2. **Business Week's own annual indexes for 1962-1971 (six of them retrieved and read).** They are
   the finding aid the blocked families cannot supply right now: dated, paginated citations to the
   discount-industry coverage of Wal-Mart's founding decade — *"Discounters strive to ride out storm:
   fast-growing $6-billion industry…"*, *"Discount store dropouts" p101 Oct.6 1962*, *"Shake-out among
   discounters seen as chain files in bankruptcy" p83 Oct.27 1962*, *"Nielsen survey shows an increase
   in the number of mass merchandisers" p100 May 16 1964*, *"Small town greets the discounters" p90
   Oct.3 1964*, *"How Kresge became top discounter" (cover) p62 Oct.24 1970*. Each is a resolvable
   pointer into the same SIM binding family. It is the route by which Walmart's 1962-1971 sector
   environment stops being inferred from the company's own later account.

**Near-miss worth naming:** for UnitedHealth the analogous structural find is the *unbroken* annual
index run of *Minnesota Medicine* (1968-1986) and of *Abstracts of Health Care Management Studies*
(1968-1986). Seven volumes were read; they yield the profession's HMO debate with dates and pages
but never the company's name — so the verdict can now say *what* surrounded UnitedHealthCare's
founding, independently, while the company-specific witness is still not in hand.

## 5. The single biggest hole this pass could not reach

**The 1962-1975 trade-press of the variety/discount sector itself — *Chain Store Age*, *Discount
Store News*, *Discount Merchandising* and any "chain statistical" yearbook — is not digitised with
text on Internet Archive (proved five ways, all EMPTY), and the three hosts that plausibly hold it
(Chronicling America, HathiTrust, Google Books) are exactly the ones that challenge this machine.**
Everything the sector's own trade press would say in Wal-Mart's founding decade therefore remains
**UNANSWERED, not empty**: it is the one gap where a positive result would most change company_002's
depth verdict and where no local route exists. The 1945-1961 *Stores* run and the 1962-1971 Business
Week indexes now reachable on IA are the partial substitute, not the answer. The nightly
`harvest.yml` runner from unblocked egress remains the only way to close it.

## 6. File inventory (18 files; sizes on disk at write time)

```
periodicals_intake/_MANIFEST.md                                        this file
periodicals_intake/_REQUEST_LEDGER.tsv                                 25,456 B   100 request rows
periodicals_intake/walmart_variety_sector/SEARCH_LOG.md                12,651 B   every query + state
periodicals_intake/walmart_variety_sector/STUB_LEAD_oversize_items_registered_not_downloaded.md  8,999 B
periodicals_intake/walmart_variety_sector/BUSINESSWEEK_INDEX_1964-1971_EXTRACT_discount_retail.txt 44,966 B (~6,500 words, 6 index years)
periodicals_intake/walmart_variety_sector/STORES_NRDGA_1960-1975_EXTRACT_discount_variety.txt     8,017 B (~1,100 words)
periodicals_intake/walmart_variety_sector/ia_businessweek_index_run_1962-1971.json       2,886 B   selected fields only
periodicals_intake/walmart_variety_sector/ia_chain_store_age_and_discount_store_news.json 2,228 B
periodicals_intake/walmart_variety_sector/ia_census_business_and_chain_store_stats.json  3,687 B
periodicals_intake/apple_microcomputer_sector/SEARCH_LOG.md                             7,789 B
periodicals_intake/apple_microcomputer_sector/BYTE_1977-09_EXTRACT_apple2_ad_and_editorial.txt 9,110 B (~1,290 words)
periodicals_intake/apple_microcomputer_sector/CREATIVECOMPUTING_1977-11_EXTRACT_apple_mentions.txt 6,471 B (~820 words)
periodicals_intake/apple_microcomputer_sector/ia_byte_run_1975-1995_by_issue.json       3,111 B
periodicals_intake/apple_microcomputer_sector/ia_kilobaud_interfaceage_creativecomputing_popelectronics.json 2,693 B
periodicals_intake/unitedhealth_minnesota/SEARCH_LOG.md                                11,381 B
periodicals_intake/unitedhealth_minnesota/MINNESOTA_MEDICINE_INDEX_1974-1980_EXTRACT_hmo_debate.txt 11,694 B (~1,600 words)
periodicals_intake/unitedhealth_minnesota/ia_minnesota_medicine_sim_run.json            3,308 B
periodicals_intake/unitedhealth_minnesota/ia_medical_economics_sim_run.json             3,059 B
```
Largest artifact 44,966 B / ~6,500 words — an order of magnitude under the volume-safety line.
Naming follows the house conventions: `ia_<slug>.json` for catalogue inventories,
`<PUB>_<years>_EXTRACT_<subject>.txt` for bounded text with a `# [PROVENANCE HEADER …]` block,
`STUB_LEAD_<slug>.md` for registered-not-downloaded leads.

## 7. Route facts re-verified from this machine (for the next agent's benefit)

* `https://archive.org/advancedsearch.php?q=…&fl[]=…&rows=…&page=1&output=json` — 48/48 HTTP 200.
  **`identifier:(<prefix>*)` is the workhorse clause** for periodical runs: it is what surfaced the
  1,890-item Business Week, 205-item *Stores* and 131-item Census families in one request each.
  `collection:(<pub_x>)` works (proved on `pub_business-week`) and returns 0 for a collection whose
  children are not indexed — **so `collection:` 0 does not mean "no issues exist", it means "not
  indexed as members"**, which is exactly the Chain Store Age situation.
* `https://archive.org/metadata/<id>` — 29/29 HTTP 200, but **three returned 2 bytes (`{}`) for
  identifiers that the search index had just returned**. Treat `{}` as UNANSWERED for that item; do
  not convert it into "not digitised".
* `https://archive.org/download/<id>/<file>` — **fails here, reproduced:** TLS
  `certificate has expired`, 0 bytes. The metadata → `<server>` + `<dir>` → file route returned the
  same object at HTTP 200 one request later. Do not ship `download/` in any new query config.
* Text-layer file names **contain spaces** (`Kilobaud 1977-01_djvu.txt`,
  `Interface Age 1979-10_djvu.txt`) and **do not always begin with the identifier**
  (`1975_09_BYTE_00-01_The_Worlds_Greatest_Toy_djvu.txt`). Any layer-detection code keying on the
  identifier prefix will wrongly report "no text layer". URL-encode with `quote()`.
* No rate limiting observed at 2.5 s spacing across 100 requests, including 22 bulk text GETs of
  17 KB-1.29 MB. Byte counts matched each item's metadata-declared size every time — that equality
  is what lets this register say "complete retrieval" rather than assume it.

## 8. Traps found (add to `queries.json` known-traps if these forms are ever shipped)

1. **`sim_variety_*` is *Variety*, the show-business weekly** — 3,127 items, zero to do with variety
   stores. Any "variety store" harvest that falls back to `identifier:` prefix matching will pull
   entertainment trade press into a retail dossier.
2. **"Walton" is a decoy twice over**: 1962 BW index `WALTON, William — Holiday Inns … p47, Jul.14`
   and 1970 BW index `H. C. Walton p4, Aug.29`. Neither is the Arkansas family. Both were checked in
   context before being recorded.
3. **`title:("ben franklin")` returns the Founding Father** — 36 items, none corporate. The company
   is only reachable through court-docket identifiers.
4. **A `numFound` from an OR-chain is not a per-title count.** `C04`'s 3,127 is one title's total;
   the 60 documents returned were all `sim_variety_*`. Counts quoted per-title in this area come
   from single-clause queries.
5. **Index volumes are not the journal.** Six Business Week indexes and seven Minnesota Medicine
   indexes prove the *serials* exist and are OCR'd; they do not prove the cited issues are readable,
   and for 1962-1975 BW the issues demonstrably are not on IA.
