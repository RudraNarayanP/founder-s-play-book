# A_chronology_feasibility.md — MARATHON PETROLEUM (company_030), Stage-1 PROBE

**Probe agent:** `probe-marathon` (claimed with `python tools/scaffold.py claim --path
founders_playbook/01_companies/company_030_marathon/research/A_chronology_feasibility.md --agent probe-marathon`).
**Scope:** chronology feasibility only. This pass writes **no volume, no registers, no ids, no certification**
(probe contract, §15.1). **Web budget used: 0 WebSearch / 0 WebFetch.** Every number below is printed beside the
command or the byte that produced it.
**Scripts deliberately NOT run:** `harvest_mine.py`, `periodical_harvest.py` (per brief; the fleet reharvest of
RD-134 is a live writer on the same harvest root). `sec_intake.py` was also not run — reason in §11 D1, which is
a refusal, not an oversight.
**A4 re-read before quoting:** `research/A4_harvest_mine.md`, mtime **2026-09-29 23:40:26 +0530**
(`stat -c '%n %y' …`); it is quoted below only as a pointer to files, never as evidence, per its own banner.

## 0. Measured state at probe start (verified, not inherited)

| item | measured this pass | how |
|---|---|---|
| files in company dir before I wrote anything | **81** = 79 under `sources/` (55 sec, 8 corporate_print, 8 periodicals, 7 `_index`, 1 `harvest_mine/_index.json`) + 2 in `research/` (A4 and my claimed file) | `find company_030_marathon -type f \| wc -l` |
| brief's "25 sec, 8 corporate print, 8 periodicals" | reproduces as **file counts**; as **documents** the two non-SEC shelves hold **6**, not 8 | md5 in §3 |
| SEC store | 25 documents / **8 accessions**, all filingDate **2011**; `_SKIPPED.csv` 1 line, `_UNANSWERED.csv` 1 line (header only) = 0 rows; `_RUN.json`: `attempted 25, stored 25, unanswered 0, skipped 0, nameless_rows 0, identity_ok true, bytes 9,744,622, words 490,655` | `cat sources/sec/_RUN.json` |
| EDGAR index (registrant) | **1,884 filings enumerated, 0 rows dropped for no accession, 0 rows without primaryDocument, UNANSWERED slices: (none)**, perimeter **2011-01-25 → 2026-09-01**, `former_names: []`, guard `ok` (slug token ['marathon'] matches registrant 'Marathon Petroleum Corp', CIK 0001510295) | `sources/_index/_INDEX_CIK0001510295.md`, `_registrant_CIK0001510295.json` |
| index copies | `submissions.csv` and `submissions_CIK0001510295.csv` are **byte-identical** (`md5sum` → both `6a99d864…`): ONE document, two shelves, never two corroborations | `md5sum` |
| harvest root, marathon rows | **80** exact-match rows on `company == "marathon"`; `A4_harvest_mine.md` said 34 candidates — **the index more than doubled after that mine ran** (fleet reharvest 2026-09-29T19:11Z) | `python -c "…if r['company']=='marathon'"` |
| marathon query block | **exists**: 8 tasks in `tools/queries.json` (`chronicling_america` 2, `internet_archive` 2, `corporate_print` 2, `hathitrust` 1, `google_books` 1) → family (c) is **TRIED**, not provisional (RD-112's Costco/Nvidia distinction) | `python -c "import json; [t for t in json.load(open('tools/queries.json'))['tasks'] if t['company']=='marathon']"` |
| universe row | rank 30, `Marathon Petroleum`, FY2025 revenue, Findlay Ohio; **no founding-date column anywhere in the CSV** (header enumerated: `rank,company,revenue_usd_millions,revenue_fiscal_year,profit_usd_millions,hq_city,hq_state,fortune_industry,universe_source_url,verified_by_second_source,confidence,notes`) | `head -1 00_universe/fortune_top_50_2026.csv` |

**Headers enumerated before any field was read (RD-124 rule).** `sources/_index/submissions.csv` =
`filingDate, form, accession, reportDate, primaryDocument, source`. `00_universe/harvest/candidates.csv` =
`company, source_family, query, item_id, title, date_or_issue, url, snippet_or_hitcount, http_status,
classification, retrieved_at`. `sources/sec/_MANIFEST.csv` = `rank, slot, cik, accession, file, path, bytes,
words, status, form, filingDate, url, why, listing`. No `query_label`, no `period_or_date`, no `source_query`.

STATUS: WRITTEN

## 1. First the identity question, because every tier below depends on it

This company's trap is a **2011 separation from an older parent**, and the held bytes decide it rather than the
tradition. Four carriers, all Tier-1 by §5, all read in the bytes:

**C1 — the charter itself.** `sources/sec/0001193125-11-170720_dex31.htm` (Restated Certificate of Incorporation,
Exhibit 3.1 to the 8-K filed **2011-06-22**, event 2011-06-16), **l.18-19**:

> "The name of the Corporation is Marathon Petroleum Corporation, **originally incorporated under the name of MPC
> Holdings Inc.** The original certificate of incorporation of the Corporation was filed with the Secretary of
> State of the State of Delaware **on November 9, 2009**."

**C2 — the registrant's own registration statement.** `sources/sec/0001193125-11-013935_dex991.htm` (Information
Statement, Exhibit 99.1 to Form 10-12B filed **2011-01-25**), **l.9781** (five further printings at l.743, 2636,
6178, 11483, 23785 — one lineage, §3):

> "We are currently a wholly owned subsidiary of Marathon Oil. Our company was **incorporated in Delaware on
> November 9, 2009, in connection with an internal restructuring.** Following the spin-off, we will be an
> independent, publicly traded company. **Marathon Oil will not retain any ownership interest in our company.**"

**C3 — the S-4.** `sources/sec/0001193125-11-253290_d234219ds4.htm` (filed 2011-09-21), **l.862**, under the
heading *Corporate Information*, repeats "Our company was incorporated in Delaware on November 9, 2009."

**C4 — the spin date from the registrant's own mouth.** `sources/sec/0001193125-11-289701_d249339dex991.htm`
(Q3-2011 results release, Ex-99.1 to the 8-K filed 2011-11-01), **l.1430**: "…the 356 million (basic) and 358
million (diluted) shares outstanding **as of the June 30, 2011 spin-off date**…"

So the legal person this dossier is about is **a Delaware corporation incorporated 2009-11-09 as MPC Holdings
Inc., first President-of-MPC appointment April 2010, registered on Form 10 2011-01-25, distributed by Marathon
Oil on 2011-06-30.** C2 also fixes the earliest in-window act of *this* person: l.11924, "He assumed
responsibility as President of Marathon Petroleum Company LP in September 2001 and **as President of MPC in
April 2010**."

**And the 1887 tradition is measurably absent from every held byte.** `grep -r -c -- "1887" sec/ corporate_print/
periodicals/` returns **exactly one file: `sec/_RUN.json`** — the intake tool's own window parameter. In document
bytes, `1887` = **0 occurrences**; `1889` = **0**; `Colorado Oil` = **0**; `Ohio Oil` = **0**. Counted by
occurrence, not by line, over the flattened text of `0001193125-11-013935_dex991.htm` (649,283 chars after tag
strip) and across all 25 stored SEC files. **In this corpus the year 1887 exists only as a search setting** —
which is RD-112's sentence, demonstrated on this company rather than warned about.

The two ancestor-adjacent strings that *do* appear in the SEC bytes are not 19th-century either:
* **USX / United States Steel** — 5 and 5 occurrences in C2, **all of them director biographies** ("He joined
  United States Steel Corporation (later renamed USX Corporation) in 1965…"), plus one unrelated sitting U.S.
  Steel board seat. **None is a history recital.** The Form 10 does not trace MPC to USX at all.
* **"Predecessor"** — used in its accounting sense only: l.11923 names the operating predecessor explicitly:
  "Marathon Petroleum Company LP (which, together with its predecessor entities, **including Marathon Ashland
  Petroleum LLC**, we refer to as 'Marathon Petroleum Company LP')", and the Selected Financial Data note fixes
  "Predecessor" at **June 30, 2005** ("On June 30, 2005, Marathon Oil acquired the remaining 38 percent ownership
  interest in the entity now known as Marathon Petroleum Company LP… periods prior to and including June 30, 2005
  are referenced as 'Predecessor'"). **A "Predecessor" column in MPC's filings is a re-basing date, not an
  ancestor** — the register must never let it become one.

STATUS: WRITTEN

## 2. Family (a) — SEC/EDGAR: **TRIED–ANSWERED** (and it is the only family that answers for this registrant)

RD-134's fix is verified as having run: `_INDEX_CIK0001510295.md` prints **no `walk: CAPPED` line**, enumerates
1,884 filings with "0 rows dropped", and its "UNANSWERED slices" section reads `(none)`. So this company's
filings-family verdict is **not** one of the pre-RD-134 provisional ones.

Measured perimeter, from `sources/_index/submissions_CIK0001510295.csv` (1,884 rows, `tail -n +2 … | cut -d, -f1 |
cut -c1-4 | uniq -c`): 2011 **119** · 2012 109 · 2013 126 · 2014 148 · 2015 131 · 2016 120 · 2017 125 · 2018 175 ·
2019 129 · 2020 114 · 2021 112 · 2022 105 · 2023 113 · 2024 103 · 2025 85 · 2026 70. **Rows with filingDate <
2011-01-25: 0.**

That zero is a **registrant** floor, not EDGAR's floor: 2011-01-25 is the Form 10 that created the CIK, and the
company did not exist before 2009-11-09. Reporting it as "EDGAR reaches nothing before 1994" would be wrong in
both directions here — it is not a tool limit and it is not a silence, it is a birth.

Earliest-per-form (from `_INDEX_CIK0001510295.md` l.15-39): `10-12B` 2011-01-25 · `10-12B/A` 2011-03-29 · `8-K`
2011-06-22 · `S-4` 2011-09-21 · `424B3` 2011-10-07 · `POSASR` 2011-12-07 · `SC 13D` 2012-01-19 · **`10-K`
2012-02-29** (report date 2011-12-31) · `ARS` 2012-03-14 · `DEF 14A` 2012-03-14 · `11-K` 2012-06-26 · `424B5`
2014-09-02 · `S-4/A` 2018-07-05 · `425` 2018-04-30 · `SC TO-I` 2021-05-17. **No S-1 exists** (a Form 10 spin
registration is this registrant's founding instrument).

**What is actually held vs what exists:** 25 documents across 8 accessions, **every one filed in 2011**
(`tail -n +2 sec/_MANIFEST.csv | cut -d, -f9,10` → 2011-01-25 ×3, 2011-06-22 ×3, 2011-09-21 ×4, 2011-10-06 ×4,
2011-10-31 ×2, 2011-11-01 ×3, 2011-11-14 ×2, 2011-12-07 ×4 — 8 lineages). **0 documents stored for 2012-2026**,
i.e. 1,765 indexed filings are unread. That is an intake perimeter, and §7 treats it as one.

**The recital route did not need a second pass, and this is worth flagging for the fleet.** RD-134 built
`fleet_intake.py` to run a forward pass "when the in-window pass stores nothing"; for marathon the state file
(`00_universe/_FLEET_INTAKE.tsv`) reads `pass1 rc0/inwindow8/UNANS0 · 25 docs · filing_floor 2011-01-25 ·
slices_capped no · DONE` and **`pass2_status` is blank**. The forward pass was correctly skipped, because for a
2009/2011 spin the founding sentence is inside the very first in-window filing — C1–C3 are all 2011 documents
reciting a 2009 date. A 2011 spin-off is therefore the inverse of the Ford case: the recital is not in a 1990s
filing, it is in the registrant's own first registration statement, at l.9781.

STATUS: WRITTEN

## 3. Family (c) — periodical corpora: **TRIED; ANSWERED for ancestors and decoys, UNANSWERED for every text route that could name this registrant**

The query block exists (§0), so this family counts as tried. Its sub-corpora split, and the split is the verdict:

* **(c1) Internet Archive periodical sweep — searched, and the promoted pile is not this company.**
  The 2026-09-29T19:11 facet-free re-run of `IA Marathon Petroleum / Marathon Oil periodical text 1900-2015`
  returned 22 fresh rows: **17 `LEAD_ONLY`** whose `snippet_or_hitcount` collection list is
  `['usfederalcourts', 'USGovernmentDocuments', 'government-documents']`, and **5 `TIER1_CANDIDATE`** whose
  collections are `citycouncilordinances/cityclerk/cityoffortwayne/americana`, `larc/university_of_alberta_libraries/toronto`
  and `booksbylanguage_arabic/booksbylanguage/fav-bunglebare/fav-jack_kemp507`. **Read the collections before
  reading the label:** a Fort Wayne city-council ordinance, an Alberta larceny digest and an Arabic-language book
  are the *race*, the *place* and the *newspaper* senses of "marathon" — RD-124's bare-word class arriving under a
  promoted label, exactly as A4's banner warns ("a `TIER1_CANDIDATE` label in a harvest index can be an artefact
  of the query text echoing").
  The genuinely relevant IA items are the **~17 `micro_IA403856xx / micro_IA403850xx` U.S. Reports caption pages**
  (*Hunt Oil Co. v. Marathon Oil Co.*, 376 U.S. 910 (1964); *Tenneco West, Inc. v. Marathon Oil Co.*, 474 U.S. 845
  (1985); *Mobil Corp. v. Marathon Oil Co.*, 455 U.S. 982 (1982); *Marathon Oil Co. v. Babbitt*, 528 U.S. 819
  (1999) …). Those are third-party **court records** naming *Marathon Oil Company* — a different legal person from
  the registrant, so per the brief they are ancestor evidence, not origin evidence; but they are an **independent
  lineage** (§3) which no company self-narrative touches, and they are the only carriers in the whole corpus that
  put the ancestor name in front of a date assigned by someone other than the company.
  Also in the promoted pile: `internationaldir0000unse_o5t3` — **International Directory of Company Histories 2010,
  Vol 109** — the single item most likely to recite a founding year, and it is **in-window (2010)** for the window I
  propose in §7. The mine reached no bytes for it: `sources/harvest_mine/_index.json` records `UNANSWERED -- no
  text layer resolved (UNANSWERED after 3 tries (HTTP 403))`. **UNANSWERED, remedy = FR-1.**
* **(c2) Chronicling America — TRIED–UNANSWERED, and the queries are pointed at the wrong century.** All 4 marathon
  CA rows are failures of the endpoint, not of the archive: 2 × `SKIPPED: hard stop: 5 consecutive failures (host
  halted)` (2026-09-26T09:45Z) and 2 × `ERROR`/HTTP **404** (2026-09-29T13:08Z). The landed fleet verdict
  `00_universe/harvest/_CA_ENDPOINT_TEST.md` (2026-09-29T18:05Z) is binding: **7 of 7 shapes CHALLENGED/403,
  "ANSWERED shapes: none … no CA zero may be cited as a null."** Second, and independent of the block: both CA
  queries target `Marathon Petroleum … 1980-2015` and `Marathon Oil / Midwest Oil … 1900-2011` — **there is no CA
  query at all for the registrant's own 2009-11-09 → 2011-06-30 window**, so even a working endpoint could not
  answer Stage 1 as I have defined it.
* **(c3) HathiTrust — TRIED–UNANSWERED.** 1 task, `SKIPPED: hard stop: 5 consecutive failures` (2026-09-29T13:08Z).
* **(c4) Google Books — searched; catalogue answered, text unreachable, and the leads are the ancestor's.**
  12 rows: **11 `LEAD_ONLY`, all `viewability=no_pages`**, plus 1 `TIER1_CANDIDATE` (`kMeudoDQwpUC`, 2003, *Annual
  Report of the Foreign-Trade Zones Board*) which resolved no text layer (`HTTP 503`) and is a decoy anyway. The
  no_pages leads are the interesting part and **not one of them is a Marathon Petroleum document**:
  `XuEVAQAAMAAJ` *Annual Report — United States Steel Corporation* 1984 · `wqDtAAAAMAAJ` US Steel 1983 ·
  `c6HtAAAAMAAJ`/`CV0VAQAAMAAJ` *Annual Report* 1988/1984 · **`oAdZAAAAYAAJ` *Marathon Annual Review* 1991** ·
  `N2-FAAAAIAAJ` *Financial Times International Business Yearbook* 1977 · `BC0sAQAAIAAJ` *Oil and Petroleum Year
  Book* 1964 · `4UO6AAAAIAAJ` *Oil and Gas International Year Book* 1988 · `UOtK5t0TYzsC`/`5tNPVxHHAc4C` Mines
  Ministry reports 1963/1965. The 1983/1984 US Steel reports and the 1991 *Marathon Annual Review* are **the
  parent's print, i.e. ancestor-stage carriers**; they answer nothing about a corporation created in 2009.

**What is physically held, and what it names.** The brief's "8 corporate print, 8 periodicals" is a file count;
md5 over all 8 `.txt` shows **two byte-identical cross-shelf duplicates**, so the number of *documents* is 6
(rule 4: check md5 before counting a corroboration):

| held document (distinct) | bytes | md5 | `Marathon` | `Marathon … Oil Company` | `Marathon Petroleum Corporation` |
|---|---|---|---|---|---|
| `periodicals/marathon-automotive-service-guide-1964_djvu.txt` | 933,253 | `9b16f8b2` | 1 | **1** (OCR: `Marathon Oll Company`, l.130) | 0 |
| `corporate_print/gov.gpo.fdsys.CHRG-105hhrg45026_djvu.txt` *(same bytes also on `periodicals/`)* | 828,591 | `48cb46ce` | 82 | 2 (l.236, 2458-2462) | 0 |
| `corporate_print/gov.gpo.fdsys.CHRG-107shrg89115_djvu.txt` | 176,664 | `ea5cce00` | 2 | 2 (l.3462) | 0 |
| `corporate_print/cia-readingroom-document-cia-rdp87t00685r000200400003-1_djvu.txt` *(also on `periodicals/`)* | 132,576 | `b9f285a3` | 1 | 0 (**decoy**, l.3963) | 0 |
| `periodicals/cia-readingroom-document-cia-rdp84-00898r000300060004-4_djvu.txt` | 82,411 | `281adc81` | 1 | 0 (l.351, "discovered by Marathon Oil in 1971") | 0 |
| `corporate_print/cia-readingroom-document-cia-rdp89-01114r000100020067-1_djvu.txt` | 3,769 | `e6966818` | 1 | 0 (l.115 `Marathon 071`, a list entry) | 0 |

**`Marathon Petroleum Corporation` occurs 0 times in all six** (measured by `re.findall` over the decoded bytes).
Three of these need re-labelling by class, because they are the three the mine got wrong:

1. **The 1964 guide is not a bare word — it is an OCR-degraded naming of the ancestor.** A4 scored it
   `BARE_WORD_MATCH, entity hits 0`. The bytes say otherwise at **l.130**: `4 éprodoen of Marathon Oll Company
   which ard the sole property of that compony. Printed in U.S.A.` — i.e. "A product of Marathon Oil Company …
   Printed in U.S.A." The entity phrase is present; `Oil` prints as `Oll`, so a phrase grep for `marathon oil`
   cannot see it (rule 6's OCR class, in the opposite direction: a decoy-shaped miss, not a decoy-shaped hit).
   It is still **not the registrant** — 1964 pre-dates the corporation by 45 years — but it is company-published
   print naming *Marathon Oil Company*, and it is the only self-published Marathon print on this disk.
2. **The 1986 CIA item promoted by the string `marathon petroleum` is a foreign company.** A4 quoted l.3963 and I
   re-read it: `Marathon Petroleum pipelines near Munich. | 25X11`, inside a declassified 1986 *Terrorism Review*
   (IA scan 1986-12-01; A4 flagged the scan/title 1986/2004 mismatch). A German-named Marathon pipeline is the
   same-brand / different-legal-person class of rule 5. **It may not be cited as a naming of MPC or of Marathon
   Oil Company, and it is excluded from every tier count below.**
3. The `rdp89-01114` item (3,769 B) is a 1973 President's Commission on Personnel Interchange letter to the CIA
   with an attached partial list of participating companies; `Marathon 071` is a list row and `Standard Oil` occurs
   once. It was **never mined** (absent from A4's 6). A directory entry naming a company is not an origin (rule 5);
   kept as a held negative artifact.

STATUS: WRITTEN

## 4. Family (d) — digitised corporate print: **TRIED–UNANSWERED twice, and the shelf labelled "corporate_print" contains no corporate print**

The two `corporate_print` tasks for marathon changed classification **without the archive changing at all**, which
is RD-130 measured live on this company:

| run | rows | classification | text of the row |
|---|---|---|---|
| 2026-09-29T13:08Z | 2 | **NULL** | `EMPTY (proven null): numFound=0 FOR THESE EXACT PARAMS ONLY — per-param, never per-corpus; the family stays open…` |
| 2026-09-29T19:11Z (facet-free reharvest, `_FACETFREE_RUN.log`) | 2 | **UNANSWERED** | `UNANSWERED, not a null: numFound=0 WITH A YEAR FACET. Bound print runs are frequently catalogued with year=None… Re-run the same query with year_range removed` |

The 19:11 rows supersede the 13:08 rows for the same two queries
(`CP marathon + predecessor annual/shareholder print 1920-2015 (wide, un-refined)` and
`CP marathon corporate print by creator 1920-2015`). **Family (d) is therefore an open question, not a null.**
One honesty check: the FETCH log tags the IA query `[FACET-FREE per RD-130]` but tags neither CP query, while the
CP responses still diagnose a year facet — so the facet may not in fact have been stripped for `corporate_print`
on this run. Reported as an observation (§11 D4), not as a fix.

**And the shelf label is a lie.** `sources/corporate_print/` holds 4 text files; classifying them by their own
heads: `PRESIDENT'S COMMISSION ON PERSONNEL INTERCHANGE` (1973 letter), `Declassified … CIA-RDP87T00685 …
Directorate of Intelligence Terrorism Review` (1986), `AUTHENTICATED U.S. GOVERNMENT INFORMATION … OVERSIGHT
HEARINGS ON ROYALTY-IN-KIND` (1997), `S. Hrg. 107-980 THE TENNESSEE VALLEY AUTHORITY` (2002). **0 of 4 are
corporate print.** So: **no annual report, no shareholder letter, no house organ and no bound directory layer of
either MPC or Marathon Oil Company is held anywhere on disk.** Since the parent's own print exists as Google Books
leads at `no_pages` (§3 c4), the corporate-print family is blocked by a text route, not by an archive.

STATUS: WRITTEN

## 5. Family (b) — web archives: **UNTRIED**

* No shelf: `ls -d 01_companies/*/sources/web_archive` matches **only** `company_011_microsoft` and
  `company_042_target`; marathon has none, and `find company_030_marathon -type d` returns `_parts`, `research`,
  `sources/{_index,corporate_print,harvest_mine,periodicals,sec}`.
* No scripted route: `grep -rl "web.archive.org\|cdx" tools/*.py` → **no files** (enumerated `tools/`:
  `ca_endpoint_probe, company_status, fleet_intake, gates, harvest_mine, ia_text, id_mint, merge_census,
  periodical_harvest, scaffold, scaffold_company, sec_intake`). Fleet `queries.json`'s 427 tasks use **5 family
  labels only** (`chronicling_america, corporate_print, google_books, hathitrust, internet_archive`) — there is no
  `web_archive` task to leave unrun.
* 0 manual calls, per hard rule 1. **UNTRIED, and it is the family with the most room here**: a registrant born in
  2011 lives entirely inside the web-archive era, and `marathonpetroleum.com` press/investor pages from 2011-06-30
  forward would be Tier-1 "archived company pages" per §5. This is also the family Microsoft's audit mis-wrote
  (RD-134 NR-1), so I record the measurement rather than the bare word: **no sidecar carrying an `http_status`
  exists under any marathon web-archive path, because no such path exists.**

STATUS: WRITTEN

## 6. Family (e) — auction / museum / manuscript: **UNTRIED**

Same geometry: no family label in the harvester, no script, no shelf, and the web budget Apple's precedent used is
set at 0. Structurally untried for this company. Substantively it is the *ancestor* family with room — an 1887
Colorado/Ohio incorporation paper, a Marathon Oil bond coupon or an Ohio Oil Company ledger could still arrive in an
ancestor-stage window — whereas nothing in (e) could bear on a Delaware corporation whose original certificate was
filed 2009-11-09 and whose recital I have at C1 l.18-19.

STATUS: WRITTEN

## 7. Per-stage tiers — windows PROPOSED by me, each bounded by a carrier, not by a filename

RD-112 governs: **a tier is measured against that stage's own window.** The window the pipeline handed me is
`tools/harvest_mine.py` `WINDOWS["marathon"] = ("1887-01-01", "2011-12-31")` (read at line 63 of the file, not
inherited from the brief). It is a **search setting**, and its own span shows it is incoherent as a stage: it
begins 122 years before the registrant existed and ends six months after it was already public, mixing a
19th-century ancestor with a 2011 spin-off. I replace it with three registrant windows plus one labeled ancestor
window. Every bound below names the carrier that fixes it.

| stage | PROPOSED window | what the window is | families returning in-window Tier-1 text | tier | §15.2 deliverable |
|---|---|---|---|---|---|
| **1 — origin of this legal person** | **2009-11-09 → 2011-06-30** | charter filing (C1 l.19) to distribution date (C4 l.1430) | **(a) only** — C1, C2, C3 all in-window | **T3 register** | short narrative + registers; §K §N §U mandatory; 8k w/stage; **3-4 runs** |
| **2 — first independent years** | **2011-07-01 → 2013-12-31** | day after spin to the first full post-spin reporting cycle (earliest `10-K` 2012-02-29; earliest `DEF 14A`/`ARS` 2012-03-14) | **(a) partial** — 6 of the 8 held accessions are in-window (S-4 2011-09-21; 8-Ks 2011-10-06/10-31/11-01/11-14/12-07); **0 bytes for 2012-2013 although 235 filings are indexed there** | **T3 PROVISIONAL — intake artefact, do not dispatch** (JPMorgan's Stage-3 reading, RD-134) | none until a forward `auto` + `facts` pass runs |
| **3 — mature scale** | **2014-01-01 → 2026-09-01** | index ceiling; `424B5` 2014-09-02, `S-4/A` 2018-07-05, `SC TO-I` 2021-05-17 sit inside it | **(a) indexed-only** (1,520 rows); (b)/(c)/(d)/(e) silent or untried | **T3 PROVISIONAL — intake artefact** | none on current bytes |
| *(ancestor lineage — NOT a stage of this company)* | 1887-01-01 → 2011-06-29, label `ANCESTOR-LINEAGE (Colorado/Marathon Oil Co. → The Ohio Oil Co. → USX → Marathon Oil Corp; name inherited by the 2009 corporation)` | the tradition's proper home; every claim here must name which ancestor | **(c) answers with in-window namings of the ancestor** — 1964 l.130, CIA-1983 l.351, GPO-1997 l.236/2458, GPO-2002 l.3462 — plus court-caption leads (c1); **(d) UNANSWERED**; **(a) structurally cannot answer** (the CIK is born 2011) | **T2 core PROVISIONAL**, and only if the orchestrator accepts a lineage register as a deliverable | predecessor-name register rows; `00_METHOD_AND_STYLE.md` §13 forbids inventing them |

**Tier arithmetic, stated plainly.** For the registrant's Stage 1 exactly **one** family returns in-window Tier-1
text → ≤1 family → **T3** by §15.2. I am reporting the rule, not flattering it, and the uncomfortable half is
this: **Stage 1 is the best-documented origin one could ask for, and it is still T3.** The incorporation date, the
original name, the state, the restructure that created it, the person who ran it from April 2010 and the
distribution date are all settled from a Tier-1 charter recital plus the first registration statement. A T3
*tier* here measures **family breadth, not doubt** — the same shape as Kroger's "uncomfortable part", arriving from
the opposite direction (Kroger: rich print, one family; here: conclusive filings, one family).

**§3's independence cap also applies and must travel with the tier.** C1, C2, C3 and C4 are four accessions and
**one corporate record**: the registrant describing itself. Nothing outside the lineage repeats the 2009-11-09
date on this disk, so origin confidence is capped at what a single self-filing supports (Medium under §3, not
High) until a Delaware Secretary of State paper file, a court record, or an unrelated 2011 directory prints it.
**No pre-2011 date in this dossier is a claim about the registrant** — C1's "November 9, 2009" is the only
pre-2011 date that is, and it is a 2011 document making a 2009 claim about itself.

**Provisional markers, named as the rule requires:** Stage 2 and Stage 3 tiers are provisional **on intake**, not
on evidence. Families (c) and (d) are non-provisional *as tries* (the query block exists, 8 tasks) but provisional
*as answers* (CA, HathiTrust, Google Books and corporate print all returned tool-level failures, not corpus
zeros).

**Route most likely to change this verdict:** **resolve the HTTP 403 on `internationaldir0000unse_o5t3`
(International Directory of Company Histories 2010, Vol 109) — FR-1.** It is the only in-window (2010) non-SEC
item in the whole corpus for this slug; a signed third-party history entry plus its Source Material note would put
a **second family** inside a 2009-2011 window for the first time — and separately would turn the 1887 claim into a
dated claim made by someone other than the company.

STATUS: WRITTEN

## 8. Five-family verdict table (the contract's table; three states only)

| family | state | what it answered | what it could not answer, and why |
|---|---|---|---|
| **(a) SEC/EDGAR filings** | **TRIED–ANSWERED** | The registrant's whole origin set: incorporated Delaware **2009-11-09** as **MPC Holdings Inc.** (C1 l.18-19), restructured-creation wording (C2 l.9781), President from **April 2010** (C2 l.11924), Form 10 **2011-01-25**, charter restated **2011-06-16** (8-K 170720), **spin-off date 2011-06-30** (C4 l.1430), and the accounting-"Predecessor" cut at **2005-06-30** with the named predecessor **Marathon Ashland Petroleum LLC** (C2 l.11923). Perimeter 2011-01-25 → 2026-09-01, 1,884 rows, 0 UNANSWERED slices, 25 docs / 8 lineages held. | Anything before 2009-11-09 (the CIK did not exist), and anything in 2012-2026 (indexed but 0 bytes stored). All four carriers are one corporate record → §3 independence cap. |
| **(b) web archives** | **UNTRIED** (0 attempts, 0 calls) | nothing | no `sources/web_archive/` shelf, no `web_archive` family among the 427 harvest tasks, `grep -rl "web.archive.org\|cdx" tools/*.py` → no files. Remedy: the CDX FETCH REQUEST in §12 / wire a scripted route. **Not a null.** |
| **(c) periodical corpora** | **TRIED** — split: **ANSWERED (as ancestor/decoy evidence)**, **UNANSWERED on every route that could reach text naming this registrant** | 6 distinct held documents, all pre-2011, **0 naming `Marathon Petroleum Corporation`**; 1997 GPO hearing names Marathon Oil Company 4× (l.236, 2458-2462); 2002 GPO 2× (l.3462); 1964 guide names `Marathon Oll Company` (OCR) at l.130; 1983 CIA weekly 1× (l.351); 1986 CIA item is a **Munich pipeline decoy**; 1973 commission letter is a list row. | CA 403/404 endpoint block (fleet verdict: no CA zero may be cited as a null); HathiTrust host halted; Google Books 11 leads at `no_pages`; the IA `internationaldir…2010` in-window item 403s. **Also a query defect: no CA/GB/Hathi query addresses 2009-2011 at all.** |
| **(d) digitised corporate print** | **TRIED–UNANSWERED** (tool refused, remedy named) | nothing about any Marathon entity — the 4 files on the shelf labelled `corporate_print` are 2 CIA reading-room items and 2 GPO hearings (**0 corporate print, measured by their own heads**) | Both CP queries returned `numFound=0` under a **YEAR facet**, reclassified UNANSWERED per RD-130 at 2026-09-29T19:11Z, superseding the 13:08 NULL rows. Remedy: re-run with `year_range` removed; and the reachable parent print (USX 1983/84, *Marathon Annual Review* 1991) is a Google Books `no_pages` wall → FR-2. |
| **(e) auction / museum / manuscript** | **UNTRIED** | nothing | no family label in the harvester, no script, web budget 0. Room exists only for the ancestor stage; nothing in (e) can bear on a 2009 Delaware incorporation whose recital is already held. |

**Counted toward Stage-1 tier: family (a) alone → 1 family → T3.** Provisional families: none counted; (d) is the
one whose re-run could add a second family to a registrant window, together with (c1)'s 403'd in-window item.

STATUS: WRITTEN

## 9. Load-bearing open questions, each with the carrier that could settle it

1. **Which legal person is Fortune rank 30?** ANSWERED, and the answer is not the tradition: CIK 0001510295,
   Delaware, incorporated **2009-11-09 as MPC Holdings Inc.** (C1). Open only as to *corroboration outside the
   lineage* — carrier: a Delaware Secretary of State certificate copy (no script reaches it), or the 2010
   `International Directory` entry (FR-1).
2. **Does any carrier make a pre-2011 date about this registrant?** NO, measured: `1887` = 0 occurrences in all
   held document bytes; the sole hit is `sec/_RUN.json`'s own window parameter. So every 1887/1889/Ohio-Oil/USX
   sentence in later volumes is an **ancestor claim** until a carrier names the 2009 corporation. Carrier for the
   ancestor claim: FR-1, FR-2, FR-3.
3. **What did MPC actually do between 2009-11-09 and 2011-06-30 (its own Stage-1 "first experiment")?** Held
   bytes answer partly: it was a shell for an "internal restructuring" (C2 l.9781), Heminger President from April
   2010 (C2 l.11924), the RM&T business transferred at distribution, no retained ownership (C2). Open: the
   restructure's own papers (Form 10-12B/A 2011-03-29, CORRESP 2011-06-02, UPLOAD 2011-02-22 — indexed, **not
   stored**). Carrier: `sec_intake` on accession `0001193125-11-081500` and `0001193125-11-157190`.
4. **First real-world "experiment" for a refiner is not a product test but an asset transfer** — the separation and
   distribution agreement, the transition services agreement and the tax sharing agreement are the operative
   instruments (Form 10 exhibit index, `0001193125-11-013935_d1012b.htm`: Forms 2.1/3.1/3.2/4.1/10.1/10.2/10.3/10.4,
   all starred = **not filed with the Jan-25 document**). Open: which of them were later filed (10-12B/A, or the
   8-Ks of 2011-06-22/2011-07-01). Carrier: index rows exist; bytes do not.
5. **The naming wall.** `Marathon Petroleum Corporation` occurs 0 times in all 6 held non-SEC documents and 6
   times in C2's own bytes. Earliest third-party naming of the registrant is therefore **UNKNOWN on this corpus**,
   and the first family likely to break it is (b) web archives (2011 press pages), not periodicals — the periodical
   sweeps stop at 2015 but their marathon rows are dominated by court captions and pre-2011 items.
6. **"Predecessor" is a trap the register must not fall into.** The Selected Financial Data column labelled
   PREDECESSOR (C2, l.2636-area) is a **purchase-accounting re-basing at 2005-06-30** tied to Marathon Oil's
   acquisition of the remaining 38% of the entity then renamed Marathon Petroleum Company LP. It is not an origin,
   and no timeline row may inherit a predecessor date from that column header.
7. **Post-spin operating scale (Stage 2):** the Q3-2011 release (C4) prints 356m/358m shares as of the spin date
   and per-segment income; the receivables purchase agreement exhibits (8-K 2011-10-06, dex101/dex102) and the
   2011-12-07 POSASR are held. Open: the FY2011 10-K itself (2012-02-29) — **not stored**, and it is the single
   document that would let Stage 2 be tiered on bytes rather than on an index.

STATUS: WRITTEN

## 10. `## Untried` — one command each, in the order I would spend them

1. **`internationaldir0000unse_o5t3` (2010, in-window) — the 403.** `python tools/ia_text.py
   list-files internationaldir0000unse_o5t3` then `python tools/ia_text.py internationaldir0000unse_o5t3 --file
   <the _djvu.txt it lists>` (the mine guessed one filename three times; listing first is the fix RD-130 recorded
   for `grab`). **Highest value on this list.**
2. **Corporate print re-run without the year facet** (remedy the tool itself names):
   `python tools/periodical_harvest.py --company marathon --facet-free` — **not run by this probe** (brief forbids
   it; the fleet reharvest is a live writer on the same root).
3. **Forward EDGAR pass for Stage 2/3 bytes:** `python tools/sec_intake.py auto --cik 0001510295 --company-dir
   founders_playbook/01_companies/company_030_marathon --from 2011-07-01 --to 2013-12-31 --max-docs 30` — and the
   XBRL series `facts … --from 2011-06-30 --to 2013-12-31`. Declined here for the D1 reason.
4. **The 27 → (now) ~58 IA candidate rows the mine never opened** (`harvest_mine/_index.json`:
   `candidates 34, mined 6, untried_by_limit 27`, against 80 rows in `candidates.csv` today). Route: a mine re-read
   after the reharvest settles, not by this probe.
5. **Family (b) web archives entirely** — no route exists in `tools/`; needs either a wired CDX task or the §12 FR-4.
6. **Family (e) entirely** — no label in the harvester, and the web budget is 0.
7. **The 2,378 other indexed filings** (1,884 minus the 8 accessions / 25 documents stored). Indexed ≠ read.

STATUS: WRITTEN

## 11. Defects returned for the orchestrator (not evidence), and what this probe refuses to claim

**D1 — I declined the scripted network run, and it is a protection, not a refusal of work.** `sec_intake.py auto`
against this `--company-dir` rebuilds `sources/sec/_RUN.json`, `_MANIFEST.csv`, `_PLAN.csv`, `_SKIPPED.csv` and
`_UNANSWERED.csv`. Those are the artefacts that record **tonight's measured 25-doc / 8-accession / floor
2011-01-25 in-window pass** (the state the orchestrator's own brief quotes back). Running a forward pass would
overwrite that measurement with a different window's run, in a directory the fleet intake file marks `DONE`, while
the overnight fleet lanes are live. Rule 2 says add, never clean; the only way to add here without clobbering is a
tool that keys `_RUN.json` by window (it keys by company-dir). Handed back as a tool request, with FR-5 spelled
out. **Siblings should note this is exactly why Phillips 66 (`rank 29`, the other 2011 spin in this tail) shows
`REFUSED` in `_FLEET_INTAKE.tsv`.**

**D2 — RD-134's index growth, measured on this slug.** `harvest_mine/_index.json` counted **34** candidates;
`candidates.csv` now holds **80** marathon rows. Any dossier that quotes A4's "34 / 6 mined / 27 untried" is
quoting a stale census. Correct current figures: 80 rows · `internet_archive` 59 · `google_books` 12 ·
`chronicling_america` 4 · `corporate_print` 4 · `hathitrust` 1.

**D3 — RD-130's class, live and self-correcting on this company.** The same two `corporate_print` queries were
written **NULL** at 13:08Z and **UNANSWERED** at 19:11Z (§4 table). The fleet's corpus-level "no corporate print
for marathon" is therefore not a finding; it is a parameter.

**D4 — the facet-free rewrite may not have reached `corporate_print`.** In `_FACETFREE_RUN.log` the IA fetch line
carries `[FACET-FREE per RD-130]`; neither CP fetch line does, yet the CP responses still report a YEAR facet as
the cause of the zero. Either the tag or the params are inconsistent for CP tasks. Not fixed by me (a `tools/`
edit is outside this brief).

**D5 — RD-124's detector is wrong in BOTH directions on this slug.** A4 stamped the 1964 service guide
`BARE_WORD_MATCH, entity hits 0`, yet l.130 prints `Marathon Oll Company` — OCR broke the phrase, so the phrase
grep missed a real naming. And A4 stamped the CIA 1986 item `TIER1_CANDIDATE_TEXT` promoted by
`marathon petroleum`, which the bytes resolve to a **Munich pipeline**, a different legal person. One miss, one
false promotion, same item set. Also: `Marathon` occurs 82 times in the 1997 GPO hearing but only 4 of those
lines are the company (A4's "word hits 81 / entity hits 4" reproduces), which is the ratio to remember before
anyone counts a word.

**D6 — the `corporate_print` shelf label is cosmetic.** 4 files, 0 corporate print (§4). A tier count that read
shelf names instead of file heads would credit family (d) with four carriers and move this company to T1. It has
zero.

**D7 — stale relocation ledger.** `00_universe/harvest/_RELOCATED_MINE_BYTES.tsv` has **8 marathon rows** pointing
at `00_universe/harvest/mine_bytes/marathon/…`, and `ls mine_bytes` returns **0 entries** (the whole directory is
empty, not just this slug's). The same 4 identifiers exist in the company shelves. Nothing was deleted by this
pass and I moved nothing; the ledger and the directory now disagree, which is an attribution hazard for the next
mine re-read (RD-124's "who owns these bytes" question).

**D8 — `former_names: []` vs the charter.** EDGAR's registrant record for CIK 1510295 reports no former names,
while C1 l.18 recites "originally incorporated under the name of **MPC Holdings Inc.**" A name-based search for
MPC Holdings will not find this registrant, and a probe that trusts EDGAR's former-names list would conclude the
corporation was born with the Marathon name. (Same family as the memory note "CIK-is-not-the-brand".)

**D9 — the gate's own tier reader is ambiguous on this file, so the canonical string is stated once, plainly.**
`gates.py` reported `tier: T3 (… T2,T3 also stated in this company's files (7 mentions); the most recent write
wins, §15.2 regrade)`. Every T2 token lives in §7's last row, which is labeled
`ancestor lineage — NOT a stage of this company`. **Canonical registrant tiers for this company: Stage 1 = T3;
Stage 2 = T3 PROVISIONAL (intake artefact); Stage 3 = T3 PROVISIONAL (intake artefact).** No re-grade is due. A
2011-spin registrant is the first case in this fleet whose dossier legitimately carries two tier vocabularies, so
the gate should read a declared canonical line rather than "most recent write wins" — handed back as a tool
observation, and the reason this paragraph exists.

**Refused claims (each would be an invention today):**
* **No founding date of 1887, 1889 or any 19th-century year for this registrant.** `1887` = 0 occurrences in held
  documents (§1). If a later volume needs the tradition it must cite an ancestor and say so.
* **No "MPC was renamed from Marathon Oil Company" or "the old registrant became MPC" claim.** The bytes show the
  opposite polarity for CIK 1510295 (a new 2009 corporation, MPC Holdings Inc., receiving a contributed business).
  Whether the *old* Marathon Oil accession chain later became MPC's is **not settled by anything on this disk** —
  the index floor is 2011-01-25 and `former_names` is empty — so the registrant-predecessor question is left
  OPEN, not guessed.
* **No tier for the *company*.** Only per stage (RD-112): Stage 1 T3; Stages 2 and 3 T3 **PROVISIONAL on intake,
  do not dispatch**; the ancestor window is reported as a labeled non-stage.
* **No counting of the 6 held non-SEC documents as registrant evidence** — 0 name `Marathon Petroleum Corporation`;
  and no counting of the Munich pipeline at all.
* **No High confidence on the origin from four carriers** — one corporate record (§3), so Medium until a
  non-lineage carrier repeats 2009-11-09.
* **No unverified-TLS elevation:** every held non-SEC sidecar reads `"transport": "UNVERIFIED TLS -- re-check
  before citing at High confidence"` (measured: `keys: bytes, fetched, identifier, note, route, transport, url`),
  so nothing from families (c)/(d) is cited at High here.
* **No volume, no registers, no ids, no certification** — probe contract.

**Close-out enumeration (§14 rule 11).** `find sources -type f | wc -l` = **79**, fully accounted: **55** under
`sources/sec/` (25 stored documents + 25 provenance sidecars + 5 ledgers `_MANIFEST.csv`, `_PLAN.csv`,
`_RUN.json`, `_SKIPPED.csv`, `_UNANSWERED.csv`), **8** `corporate_print/` (4 text + 4 sidecars), **8**
`periodicals/` (4 text + 4 sidecars), **7** `_index/` (2 `_INDEX.md`, 2 csv, 2 json, 1 registrant json), **1**
`harvest_mine/_index.json`. Company-wide `find … -type f` was **81** at probe start (79 sources + 2 research
files), which is the §0 figure. **Nothing was deleted, moved or renamed by this pass**; the only file I wrote is
`research/A_chronology_feasibility.md`. Items that arrived during the run and were accounted for rather than
ignored: the fleet reharvest rows at `candidates.csv` 2026-09-29T19:11Z (D2/D3), `_CA_ENDPOINT_TEST.md`
2026-09-29T18:05Z (§3 c2), `_FACETFREE_RUN.log` (§4/D4), `_FLEET_INTAKE.tsv` (§2/D1). The empty
`mine_bytes/` directory is reported, not repaired (D7).

**Tool calls used by this probe: 66 of an 85 budget (stop rule 70 respected; no new route opened after it).**

STATUS: WRITTEN

## 12. FETCH REQUESTs (no script on this machine reaches these; refusing is the correct behaviour, not a gap)

FR-1 is the highest-value unmet route in this dossier; FR-2/FR-3 serve the ancestor window; FR-4 is the only
route to family (b); FR-5 is a scripted run this probe declined for the reason given in §11 D1.

```
FETCH REQUEST: internet_archive identifier `internationaldir0000unse_o5t3`
  International Directory of Company Histories 2010, Vol 109 (IA date 2010-01-01 = IN-WINDOW for Stage 1)
  mine status: "UNANSWERED -- no text layer resolved (UNANSWERED after 3 tries (HTTP 403));
               tried internationaldir0000unse_o5t3_djvu.txt"   (sources/harvest_mine/_index.json)
  ask: the Marathon Oil Company entry (and any Marathon Petroleum Corporation entry) + its Source Material note
  hold under: company_030_marathon/sources/periodicals/ with a sidecar naming the route
  why it matters: the only in-window non-SEC carrier candidate; could add family (c) to a Stage-1 window
```
```
FETCH REQUEST: google_books volumes at viewability=no_pages (ancestor stage, family (d))
  oAdZAAAAYAAJ "Marathon Annual Review" 1991 · XuEVAQAAMAAJ "Annual Report - United States Steel Corporation" 1984
  · wqDtAAAAMAAJ US Steel 1983 · N2-FAAAAIAAJ FT International Business Yearbook 1977
  · BC0sAQAAIAAJ Oil and Petroleum Year Book 1964 · 4UO6AAAAIAAJ Oil and Gas International Year Book 1988
  ask: text for the Marathon/USX entries — officer lists, segment history, any founding-year sentence
  why it matters: these are family (d)'s only known in-window carriers; (d) is UNANSWERED only because no page is
  reachable, and digitised corporate print is the family that has flipped tiers in this project (Walmart, Target,
  Boeing, Kroger)
```
```
FETCH REQUEST: internet_archive U.S. Reports caption pages (ancestor stage, third-party/independent lineage)
  micro_IA40385601_1436 (Hunt Oil Co. v. Marathon Oil Co., 1964) · micro_IA40385605_1089 (Marathon Oil Co. v. Bruce,
  1971) · micro_IA40385018_0456 (Tenneco West v. Marathon Oil Co., 1985) · micro_IA40385004_1226 ·
  micro_IA40385003_1813 · micro_IA40386005_0932 (Marathon Oil Co. v. Babbitt, 1999)
  ask: caption/party pages only (small) — they date the ANCESTOR name by a non-company hand
  why it matters: the only route that breaks the single-lineage cap on the ancestor story (never on the 2009 origin)
```
```
FETCH REQUEST: wayback CDX (family (b) is UNTRIED; no scripted route exists in tools/)
  url=marathonpetroleum.com&output=text&fl=timestamp,original,statuscode&MIME=web, 2011-06-30 → 2013-12-31
  ask: spin-off press releases / investor pages, held under sources/web_archive/ with http_status sidecars
  why it matters: the only family that could reach MPC's own first-year self-presentation outside its filings
```
```
FETCH REQUEST (scripted, but declined by this probe — see §11 D1 for the reason):
  python tools/sec_intake.py auto --cik 0001510295 --company-dir
    founders_playbook/01_companies/company_030_marathon --from 2011-07-01 --to 2013-12-31 --max-docs 30
  plus: python tools/sec_intake.py facts --cik 0001510295 --company-dir … --from 2011-06-30 --to 2013-12-31
  why: 235 indexed filings in the Stage-2 window, 0 bytes held; Stage 2's tier is an intake artefact until this runs
```

STATUS: WRITTEN

STATUS: WRITTEN

## 13. Gate result for this pass

```
python tools/gates.py --company-dir founders_playbook/01_companies/company_030_marathon \
  --checks csv,keys --fail-on substantive \
  --out founders_playbook/03_quality_control/marathon_s1_probe_gates.md
→ Findings: 2 | Passes: 0 | exit 0 under --fail-on substantive
   coverage | registers  | no register CSVs at root or research/ -- csv/anchors gates DID NOT RUN
   coverage | narrative  | no stage_*.md volumes found -- keys/anchors gates DID NOT RUN
   coverage summary: 0 registers, 0 stage volumes, 33 source documents
```
Both findings are **coverage-only** (the gate had no input), which is the expected pre-authoring state for a
freshly probed company — the probe contract forbids this pass from creating registers or volumes. The gate's own
"33 source documents" is its de-duplicated count of held files; my §3 count of **6** distinct non-SEC documents is
the same rule applied after md5 (2 cross-shelf duplicates), and §2's **8 lineages** is the same rule applied to
SEC accessions. Nothing in this run edited a protected file; the one file written outside `research/` is the
gate's own `--out` sheet, named in the brief.

STATUS: WRITTEN
