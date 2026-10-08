# A_chronology_feasibility.md — CARDINAL HEALTH (company_015_cardinal, Fortune rank 15), Stage-1 PROBE

Owner: `probe-cardinal`, claimed with
`python tools/scaffold.py claim --path founders_playbook/01_companies/company_015_cardinal/research/A_chronology_feasibility.md --agent probe-cardinal`.
Product of this pass: **what the public record can and cannot support about this company's origin and early
years, plus a per-stage density tier.** No register row, no volume, no id is minted here (§13).

**Web budget: 0 WebSearch, 0 WebFetch.** Everything below was reached through local bytes plus two scripts
(`tools/sec_intake.py`, `tools/gates.py`). `tools/harvest_mine.py` and `tools/periodical_harvest.py` were **not
run, by order**; the harvest state quoted for those two families is read off `00_universe/harvest/candidates.csv`
and `sources/harvest_mine/_index.json`, and is therefore **a pointer to a file, never evidence** (§14, hard rule 6).

## Windows (all PROPOSED; none is evidence)

`00_universe/fortune_top_50_2026.csv` has **no founding-date column** — enumerated before any field was read
(command in §0): `rank, company, revenue_usd_millions, revenue_fiscal_year, profit_usd_millions, hq_city,
hq_state, fortune_industry, universe_source_url, verified_by_second_source, confidence, notes`. The rank-15 row
gives `hq_city = Dublin`, `hq_state = Ohio`, `fortune_industry = "Wholesalers: Health Care"`,
`revenue_fiscal_year = fiscal year ended 2025-06-30` — a 2026 housekeeping record, not an origin claim.

| proposed stage | window | why this boundary, and what it is *not* |
|---|---|---|
| **Stage 1 — origin / predecessor** | **1971-01-01 → 1979-12-31** | Opens on the only 1971 date the corpus prints (a director-since column reading "1971", DEF 14A l.243, whose own header says the column counts "the Company **or the Company's predecessor in interest**", l.222-223) and closes on the registrant's own repeated "formation of the Company in 1979" (10-K l.2597; 10-K l.454; DEF 14A l.334). **Both endpoints come from filings that post-date them by 15-24 years** (§6 RETROSPECTIVE SOURCE). Neither is a founding *document*. |
| **Stage 2 — Cardinal Distribution build-out** | **1980-01-01 → 1994-02-06** | Terminates on the day before the only in-window corporate act with a held instrument: the Whitmire combination completed 1994-02-07 (8-K l.107-108). |
| **Stage 3 — combination → named, listed wholesaler** | **1994-02-07 → 1995-12-31** | The only stage whose window EDGAR actually fills: measured floor **1994-02-09**, 55 in-window accessions, 10 of them on disk. |

`tools/harvest_mine.py` l.55 carries `"cardinal": ("1971-01-01", "1995-12-31")` — **identical to the brief's
candidate window**, so unlike Ford's probe there is no tool-vs-brief window conflict to hand up. It is still only
a search setting (RD-112), which is why the three sub-windows above are proposed rather than inherited.

STATUS: WRITTEN (header, windows)

**TIER VERDICT ISSUED BY THIS PROBE: T3 register, provisional, for all three proposed stages** — the tier verdict
line for Stage 3 is `T3 register, filings-carried` (one family: SEC/EDGAR). Per-stage detail in §3, five-family
verdict in §2, route that could change it in §7.

---

## 0. Measured state at probe start (verified tonight, not inherited)

| item | measured | how |
|---|---|---|
| files under the company dir | **51** | `find … -type f \| wc -l` |
| stored EDGAR documents | **10 / 1,713,053 B / 216,400 words** | `sources/sec/_RUN.json` + `python` byte sum, §1 |
| accessions they cover | **10 distinct accessions**, filingDates 1994-02-11 → 1995-10-10 | `sources/sec/_MANIFEST.csv` (header enumerated: `rank, slot, cik, accession, file, path, bytes, words, status, form, filingDate, url, why, listing`) |
| indexed filings for the registrant | **2,612 rows; earliest `filingDate` 1994-02-09; rows before 1994-02-09 = 0** | `python -c` over `sources/_index/submissions.csv`; header `filingDate, form, accession, reportDate, primaryDocument, source` |
| in-window (1971-01-01 → 1995-12-31) indexed rows | **55 rows = 55 accessions**; stored 10, `_SKIPPED.csv` 45, `_UNANSWERED.csv` 0 | same CSV + `sources/sec/_SKIPPED.csv` |
| registrant identity guard | **`ok`** — `CARDINAL HEALTH INC`, CIK 0000721371, ticker CAH, former names `CARDINAL HEALTH INC`, `CARDINAL DISTRIBUTION INC`; `count 2612`, `rows_dropped_no_accession 0`, `rows_without_primaryDocument 167` | `sources/_index/_registrant_CIK0000721371.json` |
| fleet intake state | `cardinal … rc0/inwindow10/UNANS0`, docs 10, `filing_floor 1994-02-09`, `slices_capped = no`, `state DONE`, **pass-2 (recital-forward) column EMPTY** | `grep -n cardinal 00_universe/_FLEET_INTAKE.tsv` (header: `slug company dir pass1_status pass1_docs pass2_status pass2_docs filing_floor slices_capped note state`) |
| non-SEC local bytes | **8 files on 2 shelves = 5 distinct documents** (3 md5 pairs) | `md5sum` group, §1.6 |
| harvest-mine dossier | `research/A4_harvest_mine.md`, **4,709 B, 57 lines, mtime 2026-09-30 01:35:52 +0530**, re-read in full this pass before quoting | `stat -c '%n \| %s bytes \| mtime %y'` |
| cardinal rows in the fleet index | **53**, of which **43 carry an `item_id`** and 10 are query-level outcome rows | `python -c` over `00_universe/harvest/candidates.csv`; header `company, source_family, query, item_id, title, date_or_issue, url, snippet_or_hitcount, http_status, classification, retrieved_at` |
| cardinal query blocks in `tools/queries.json` | **8 tasks** (2 chronicling_america, 2 internet_archive, 1 hathitrust, 1 google_books, 2 corporate_print) → family (c) was *queried*, so its gaps are blocked/unrun, never "no block existed" | `python -c` filter on `tasks[].company` |
| `sources/web_archive/`, `sources/auction/` | **do not exist** (only `_index, corporate_print, harvest_mine, periodicals, sec`) | `ls sources/` |
| `00_universe/harvest/mine_bytes/` | **empty** — no orphan cardinal bytes outside the company dir | `ls -la` |

**The A4 count, re-footed.** `sources/harvest_mine/_index.json` records `candidates 44, mined 12,
untried_by_limit 31`. 12 + 31 = **43** = tonight's `item_id`-bearing row count, so `mined` and `untried` are
counted in items while `candidates` counts **44**, one more: the google_books **FEED SUMMARY** row (blank
`item_id`, snippet `FEED SUMMARY: 10 volume(s) returned, totalResults=300 (Google's display cap, NOT a corpus
count)`) is inside `candidates` but is not an item. A 1-row base mismatch, not a lost document; reported so the
merge does not inherit "44". Nothing arrived during this probe that A4 had not seen: max `retrieved_at` for
cardinal is **2026-09-29T19:08:44Z**, i.e. ~57 min before A4's own mtime (§14 r11 accounted for).

STATUS: WRITTEN (§0)

## 1. What is held, opened, and actually says — the EDGAR set (file:line throughout)

All ten stored documents are the **registrant's own instruments or filings about it**, keyed to CIK 0000721371
with guard `ok`. That matters for the brief's trap: inside `sources/sec/`, **entity attachment is guaranteed by
the accession→CIK mapping, not by the word `cardinal`**. Nothing below is a bare-word hit. (The five non-SEC
layers are the opposite case and are quarantined in §1.6.)

Term census over the 10 stored SEC files (command: python `str.count`/`re` census printed this pass over
`sources/sec/*_0000*.txt`; occurrences then number-of-docs):

| string | occ. | of 10 docs | reading |
|---|---|---|---|
| `Cardinal Health` | 99 | 9 | the registrant's post-1994 name, attached |
| `Cardinal Distribution` | 22 | 5 | its own former legal name, attached |
| `Cardinal` (any case) | 1,315 | 10 | inflated by subsidiary names (§1.5) — **do not use as a naming count** |
| `cardinal` (lower case, exact) | **0** | **0** | the bird/adjective/surname sense is absent from the filings entirely |
| `Hult` | **0** | **0** | the founder name credited in the company's later self-narrative occurs **zero times in every stored filing** |
| `founded` | **0** | **0** | no founding verb anywhere in the held set |
| `formation of the Company` | 1 | 1 | DEF 14A l.334. The 10-K's parallel at l.2703-2704 is **the same words split across a line break**, so a space-delimited count understates the phrase by one — re-measure on joined text before publishing any count of it |
| `1971` | 2 | 1 | both inside one proxy table column (§1.3) |
| `1979` | 7 | 3 | the registrant's formation year (§1.3) |
| `predecessor in interest` | 1 | 1 | the proxy column definition (§1.4) |
| `Dublin` | 28 | **10** | present in **every** stored document — see §1.5b |
| `Cleveland` | 2 | 2 | **both are outside counsel's address** (§1.5b) |
| `Delaware` | 113 | 6 | not the registrant's state of incorporation — §1.5c |
| `Ohio` | 141 | 9 | registrant is "an Ohio corporation" (10-K l.3981, l.5678) |
| `drug wholesal*` | 35 | 7 | the business descriptor, e.g. 10-K l.232 "its core drug wholesaling activities" |
| `pharmaceutical wholesal*` | 2 | 2 | |
| `Whitmire` | 654 | 9 | the 1994-02-07 combination dominates the set |
| `Behrens` / `Humiston-Keeling` / `PharmPak` / `PRN Services` / `NSS` | 85 / 13 / 10 / 11 / 5 | 5 / 5 / 5 / 3 / 2 | the acquired stack, §1.5a |
| `hospital supply` / `Syca*` / `New Albany` / `San Diego` / `Anchor` / `Kinmed` | **0** | **0** | named hypotheses with **no carrier in this corpus**; UNTRIED, not false |

### 1.1 The rename has two dates in the same corpus, and EDGAR's own name field lags the event

Machine header block, `sources/sec/0000950152-94-000897_0000950152-94-000897.txt` (**l.43** `STREET 1: 655 METRO
PLACE SOUTH`, and the FORMER-COMPANY block at **l.50** `FORMER CONFORMED NAME: CARDINAL DISTRIBUTION INC`); the
identical `DATE OF NAME CHANGE: 19920703` line occurs in **7 of the 10** stored documents and the string
`FORMER CONFORMED NAME: CARDINAL DISTRIBUTION INC` in **7 of 10** (command: `grep -h -A2 "FORMER CONFORMED NAME"
*.txt | sort | uniq -c`). But **3** stored filings are still conformed under the old name, with **no** former-name
block at all:

| accession | filed | form | `COMPANY CONFORMED NAME` |
|---|---|---|---|
| 0000950130-94-000205 | 1994-02-11 | 8-K | **CARDINAL DISTRIBUTION INC** |
| 0000820027-94-000086 | 1994-02-14 | SC 13G | **CARDINAL DISTRIBUTION INC** |
| 0000950109-94-000279 | 1994-02-17 | 424B2 | **CARDINAL DISTRIBUTION INC** |
| 0000914185-94-000018 | 1994-02-17 | SC 13D | CARDINAL HEALTH INC + former name, date 19920703 |

So within a six-day span EDGAR's own conformed-name field straddles the change, and the body text of the 8-K
filed 1994-02-11 is headed `CARDINAL HEALTH, INC.` while its IMS header says `CARDINAL DISTRIBUTION INC`. The
**narrative** date is different again: `sources/sec/0000950152-94-000897_…txt` **l.171-172** — *"Prior to February
7, 1994, the Company was known as Cardinal Distribution, Inc."* — and the 424B2 body prints
`sources/sec/0000950109-94-000279_…txt` **l.63** `(TO PROSPECTUS DATED JUNE 1, 1993)`, **l.68**
`[LOGO CARDINAL HEALTH, INC. APPEARS HERE]`, **l.70** `(FORMERLY KNOWN AS CARDINAL DISTRIBUTION, INC.)`, i.e. a
February-1994 document describing itself as already renamed while referencing a **June 1 1993 base prospectus
that is not in EDGAR at all for this CIK** (floor 1994-02-09).

**Register consequence (do not resolve it here):** the rename has **three** candidate datings attached to this
registrant — **1992-07-03** (SEC conformed-name metadata, 7 docs), **1994-02-07** (the registrant's own 10-K
sentence, tied to the Whitmire completion), and **between 1993-06-01 and 1994-02-17** (the 424B2's self-description
plus the conformed-name lag). A `timeline.csv` row for "renamed to Cardinal Health" must be a §U conflict with
`confidence = Low`, not a date.

### 1.2 The only formation statement the corpus prints is the registrant's own, and it is 1979

* `sources/sec/0000950152-94-000897_0000950152-94-000897.txt` (10-K, FY ended 1994-06-30, filed 1994-09-02)
  **l.2596-2597**: *"Robert D. Walter has been a Director, Chairman of the Board and Chief Executive Officer of the
  Company **since its formation in 1979** and has served as a director and officer of certain of the Company's
  subsidiaries since their formation or acquisition by the Company."*
* `sources/sec/0000950152-95-002183_0000950152-95-002183.txt` (10-K, filed 1995-09-21) **l.453-454**: the same
  sentence, verbatim, one year later.
* `sources/sec/0000950152-94-001030_0000950152-94-001030.txt` (DEF 14A, filed 1994-10-14) **l.333-334**: *"Mr.
  Moritz served as an officer of various subsidiaries of the Company **from the formation of the Company in 1979**
  to July 1994."*
* Same 10-K **l.2703-2704** (Moritz bio): *"Secretary of the Company from the formation of the Company in 1979 to
  July 1994"*; and **l.2597**'s companion at **l.2680** for John F. Havens ("1979").

That is **one lineage** (§3): three accessions, one corporate self-record, all written **15 years after** the year
they recite. It supports the class `FOUNDER CLAIM / retrospective memory` — more precisely a company
self-narrative — at Conf **Medium**. It supports the sentence "the registrant states it was formed in 1979." It
does **not** state *what* was formed in 1979 (no state, no instrument, no charter, no consideration, no
co-founders), and it is **silent on 1971**.

### 1.3 The 1971 date exists — but only inside a column that is defined to cover a predecessor

`sources/sec/0000950152-94-001030_0000950152-94-001030.txt` (DEF 14A) **l.222-223**, the table's own definition:
*"… the year in which each first became a Director of the Company **or the Company's predecessor in interest** …"*.
Inside it, **l.243**: `Robert D. Walter (2)..... 49  Chairman and Chief Executive Officer of  1971  1994`, and a
second `1971` at **l.297** (a directorship-since value for a outside-partner director). `DIRECTOR SINCE 1979` for
Havens (**l.237**) sits in the same column.

Read exactly: **the registrant's proxy says some of its directors have served since 1971, under a column that
expressly allows the 1971 service to belong to "the Company's predecessor in interest"** — while the 10-K says the
Company was *formed* in 1979. That pair is the whole origin problem in two lines, and it is the RD-124 shape:
**the 1971 is a naming attached to an undefined predecessor, not to a dated act.** No held document prints that
predecessor's legal name; `predecessor` occurs 3 times in the stored set total — once here, twice in the S-4
talking about **Medicine Shoppe International, Inc.**'s own predecessor (`0000950123-95-002827_…txt` l.5103,
l.5137), a 1995 target, not a 1971 ancestor.

STATUS: WRITTEN (§1.1-1.3)

### 1.4 The one origin *act* with a held instrument is a 1993-1994 merger, not a founding

* `sources/sec/0000950130-94-000205_0000950130-94-000205.txt` (8-K, filed 1994-02-11) **l.107-110**: *"On February
  7, 1994, the Registrant announced that it completed its merger of a wholly-owned subsidiary with and into
  Whitmire Distribution Corporation."* The same document names the vehicle **`Cardinal Merger Corp`** (1 occurrence)
  and files *restated supplemental consolidated financial statements … prepared under the pooling of interests
  method* for **Cardinal Health, Inc. and Whitmire Distribution Corporation**, with balance sheets at
  **March 31 1992, March 31 1993 and December 31 1993** and earnings for FY ended March 31 **1991, 1992, 1993** —
  auditors' consents from **Deloitte & Touche** (**l.144**) and **Arthur Andersen & Co.** (**l.145**).
  ⇒ The held record therefore contains **audited statement years 1991-1993 of the registrant itself** — the
  earliest in-window *numbers* anywhere in this corpus, and they are the registrant's under its former name
  (restated on a pooled basis *with* Whitmire, which is a basis caveat, not a different company).

**(a2) The build-out is dated and priced — five acquisitions, four of them before Stage 2's close.** Note 3
"ACQUISITIONS", `sources/sec/0000950130-94-000205_…txt` (**l.866**-sqq.), restated in the FY1994 10-K's own note
(`0000950152-94-000897_…txt` l.1702, l.1709; growth attribution l.722-725):

| date | target (verbatim descriptor) | place | consideration | method | carrier |
|---|---|---|---|---|---|
| 1990-06-18 | Ohio Valley-Clarksburg, Inc., "a drug wholesaler" | Wheeling, West Virginia | **cash $27,125,000** | purchase | 8-K l.867-873 |
| 1991-10-15 | Chapman Drug Company, "a drug wholesaler" | Knoxville, Tennessee | **cash $16,800,000** | purchase | 8-K l.880-885; 10-K l.1709 |
| 1993-04-14 | *(not an acquisition)* repurchase of all 580,157 common shares | — | shares retired | — | 8-K l.1691 |
| 1993-05-04 | Solomons Company, "a wholesale drug distributor" | Savannah, Georgia | **849,358 common shares** ($18,006K per 10-K l.1283) | purchase | 8-K l.887-892; 10-K l.1702 |
| 1993-12-17 | PRN Services, Inc., "a distributor of pharmaceuticals and medical supplies to oncologists and oncology clinics" | — | **236,626 common shares** | pooling | 8-K l.894-900; 10-K l.241 |
| 1993-10-11 → 1994-01-27 → 1994-02-07 | Agreement and Plan of Reorganization → Cardinal + Whitmire shareholders approved → merger of **Cardinal Merger Corporation** with and into Whitmire effective | — | ≈**5,442,000** Cardinal common + ≈**1,488,000** newly authorized Class B + ≈**1,377,000** options converted | pooling | 8-K l.902-915; 10-K l.1647, l.3458, l.3996, l.3999 |

**What that settles and what it does not.** It gives Stage 2 a **Tier-1, dated, third-party-audited sequence of
acquisitions** — a real "repeatable validation → scalable formation" spine with cash/share consideration and named
cities — and it establishes the business as **drug wholesaling rolled up company by company**, which is exactly
the shape the brief predicted. What it does **not** do is reach the 1980s or 1971: the earliest acquisition with a
carrier is **1990-06-18**, and nothing before it is held. Class `FACT` (primary document, verified TLS sidecars:
`sources/sec/*.meta.json` record `http_status 200`), Conf **High** on each dated act individually, but
**corroboration = 1** across the 8-K/10-K pair because both are the registrant's own filings for the same
transaction set (§3 filing-lineage rule), and every figure carries the basis note *pooled-with-Whitmire
supplemental presentation* (§6).

* `sources/sec/0000950152-94-000897_…txt` **l.3981**: a merger agreement dated **October 11, 1993** "by and among
  **CARDINAL DISTRIBUTION, INC., an Ohio corporation** …"; **l.5678** `HEALTH, INC., an Ohio corporation formerly
  known as Cardinal [Distribution, Inc.]`; **l.7895** an employment agreement with "**Cardinal Distribution, Inc.,
  an Ohio corporation** (the 'Employer'), Robert D. [Walter]"; and the subsidiary-stack exhibit list at l.3897,
  l.5598, l.5916, l.6613-6696 (the *Cardinal Distribution, Inc. Stock Incentive Plan* and *Directors' Stock Option
  Plan*, twice amended).
* `sources/sec/0000950123-95-002827_…txt` (S-4, filed 1995-10-10, Reg. No. 33-63283) — the second acquisition
  instrument: **l.145** `common stock, $.01 par value, of **Medicine Shoppe International, Inc. ("MSI")**`,
  **l.255** merger of a Cardinal subsidiary "with and into MSI", **l.438** "wholly owned subsidiary of Cardinal
  Health, Inc., an Ohio corporation", **l.1165** "Common Shares, which are issued by an Ohio corporation".

**What Stage-1/2 may use.** The held set proves a *growth-by-acquisition* pattern with dated instruments running
**1990-06-18 → 1991-10-15 → 1993-05-04 → 1993-10-11 (agreement) → 1993-12-17 → 1994-01-27 (approval) → 1994-02-07
(completion) → 1995-10-10 (MSI S-4)**, plus pooled FY1991-1993 audited statements. It proves **nothing** about
1971-1979 except by the recitals in §1.2/§1.3 — and the earliest dated acquisition is **eleven years after the
1979 formation the same registrant recites**, so the company's own account leaves 1979-1990 undocumented in this
corpus. That gap, not a shortage of paper, is the Stage-1/Stage-2 finding.

### 1.5 The two traps the brief predicted, measured

**(a) "built from an early-1970s purchase" — the acquisitions are real, named and held; the *purchase* is not.**
The 10-K's own subsidiary roll-call, **l.165-168**: *"Cardinal Mississippi, Inc. ('Mississippi'); Humiston-Keeling,
Inc. ('H-K'); Behrens Inc. ('Behrens'); National PharmPak Services, Inc. ('PharmPak'); National Specialty Services,
Inc. ('NSS'); and PRN Services, Inc. ('PRN'). These separate operating subsidiaries are sometimes collectively
referred to as the 'Cardinal Health' companies."* — six operating names, five of them third-party families.
**The roll-call actually begins four lines earlier, at l.160**, and the full list is the single best piece of
Stage-2 evidence in the corpus: *"…operating subsidiaries: Whitmire Distribution Corporation; James W. Daly, Inc.;
Ellicott Drug Company; Cardinal Syracuse, Inc.; Marmac Distributors, Inc.; Bailey Drug Company; Ohio
Valley-Clarksburg, Inc.; Chapman Drug Company; Solomons Company; Cardinal Florida, Inc.; Cardinal Mississippi,
Inc.; Humiston-Keeling, Inc.; Behrens Inc.; National PharmPak Services, Inc.; National Specialty Services, Inc.;
and PRN Services, Inc."* — **16 names, of which only three carry the `Cardinal` brand** (Syracuse, Florida,
Mississippi) and thirteen keep the acquired family's own name. That is the acquisition-built-distributor
signature, printed by the registrant itself, and it is also the **naming wall**: thirteen of the sixteen names are
searchable words an entity-anchored query has never been run against (`Daly`, `Ellicott`, `Marmac`, `Bailey`,
`Ohio Valley-Clarksburg`, `Chapman`, `Solomons`, `Humiston-Keeling`, `Behrens`, `PharmPak`, `NSS`, `PRN`) —
`grep -c -i "ellicott\|marmac\|humiston" tools/queries.json` → **0**.
(`Mississippi` 6 hits / 2 docs; `Behrens` 85; `Humiston-Keeling` 13; `PharmPak` 10; `PRN Services` 11; `NSS` 5),
and 10-K **l.5761** "Shares originally issued to the **Behrens Stockholders**" (stock-financed acquisition). No held
document prints an acquisition date for any of them, and none prints a 1971-1979 predecessor name. Also note the
`Cardinal, Inc.` naming pattern (`Cardinal Merger Corp.`, `Cardinal Mississippi, Inc.`) is a **brand applied to
many legal persons**, so a "Cardinal X, Inc." hit is *not* a hit on the registrant: the register's `entity_named`
column must distinguish at least **Cardinal Health, Inc. (Ohio, the registrant) / Cardinal Distribution, Inc. (the
same registrant before the rename) / Cardinal Merger Corp. (Delaware, a wholly-owned vehicle) / Cardinal
Mississippi, Inc. / Cardinal Health 200 / Cardinal Health 110, LLC** (the last two appear only in the fleet index's
court-docket rows, §2(c)).

**(b) "a move of home city" — not evidenced in-window, and the obvious lead is a decoy.**
`Dublin` occurs **28 times in all 10 stored documents**: 10-K FY1994 cover **l.87-89** `655 METRO PLACE SOUTH,
SUITE 925, DUBLIN, OHIO 43017`; FY1995 10-K **l.70-72** same; 8-K/SC 13D/S-3/424B1/DEF 14A headers same
(`STREET 1: 655 METRO PLACE SOUTH`, `CITY: DUBLIN`, `STATE: OH`, `ZIP: 43017`, phone `6147618700`); S-3
**l.511** *"Cardinal's principal executive offices are located at 655 Metro Place [South]…"*; 424B1 **l.380**
same; DEF 14A **l.174**; 10-K **l.382** *"principal executive offices consist of leased office space located at 655
Metro [Place South]…"*. **The earliest stored filing (1994-02-11) is already in Dublin**, and so is the 2026
universe row (`hq_city = Dublin`). Both `Cleveland` hits are **outside counsel, not the company**: S-3 **l.118**
`CLEVELAND, OHIO 44114` inside the "Copies to:" block under `BAKER & HOSTETLER … 3200 NATIONAL CITY CENTER`, and
10-K **l.5469-5470** `with a copy to Baker & Hostetler, 3200 National City Center, Cleveland, Ohio 44114-3485`;
S-3 l.1982 *"We have acted as counsel to Cardinal Health, Inc., an Ohio corporation"*. The only in-window sentence
about a headquarters **moving** is a covenant about the *target* staying put — S-4 **l.3105-3108** and **l.5976-5977**
*"HEADQUARTERS AND NAME … Cardinal intends to cause the Surviving Corporation to (i) retain its corporate and
business headquarters in St. Louis County"*. ⇒ **Verdict: the domicile question is UNANSWERED by held bytes.**
A pre-1994 city, if one existed, can only be reached by paper or by the missing 1993-06-01 prospectus (§5).

**(c) `Delaware` ×113 is not a re-domicile.** Sampled contexts (command in §1's census block) attach Delaware to
**`Cardinal Merger Corp., a Delaware corporation and a wholly-owned [subsidiary]`**, to MSI-side parties
(`Apollo Advisors, L.P., a Delaware limited partnership`), and to boilerplate comparison captions ("Section 203 of
the Delaware Law", "Comparison with Delaware Law", indemnification). The registrant is **"an Ohio corporation"**
in **7** distinct held lines (§1.4). Do not write a Delaware re-incorporation into Stage 1 from this corpus.

### 1.6 The five non-SEC layers are bare-word matches, and three of them are the same file twice

`md5sum` grouping of `sources/periodicals/*_djvu.txt` + `sources/corporate_print/*_djvu.txt` (command run this
pass) returns **5 distinct documents in 8 files**: `cardinaldividear00noto` (41,687 B),
`micro_IA41152927_0526` (186,841 B) and `NASA_NTRS_Archive_19850020263` (6,495 B) each sit **byte-identically on
both shelves** — sidecars show the same URL fetched twice, `corporate_print/` on 2026-09-26T09:57Z and
`periodicals/` on 2026-09-29T17:53Z. Per hard rule 4 these are **one document, not two families**, and the
brief's "6 corporate print + 10 periodicals" is therefore **3 print files with 0 print-unique content** and 5
periodical files. Entity census over all five: **`Cardinal Health` = 0 and `Cardinal Distribution` = 0 in every
one of them**, while lower-case/any-case `cardinal` runs 24-100 hits each. What the word actually denotes, from
A4's verbatim sample lines (and re-read in the bytes tonight): **a Cessna 177B Cardinal airplane**
(`NASA_NTRS_Archive_19740006639` l.28, l.57, l.105), **cardinal spline curves** (`NASA_NTRS_Archive_19850020263`
l.1, l.9, l.41), the **Cardinal Divide area** water-quality survey of Alberta (`cardinaldividear00noto` l.1, l.50,
l.52 — its own `date_mismatch: true`, scan 1998 vs title 1995), and the **Cardinal Principles Report**, an
1903-era educational classic reprinted as ERIC microfiche (`micro_IA41152927_0526` l.8, l.22, l.29;
`ERIC_ED073079` l.30, l.43, l.50 — **two copies of one work**, per §3). This is RD-124's APPLE-acronym class
arrived at by a different noun: the harvest index still labels **6** of these rows `TIER1_CANDIDATE`
(`candidates.csv`, `classification` column) and the fixed classifier promoted **0** of them
(`sources/harvest_mine/_index.json`: every item `"verdict": "BARE_WORD_MATCH", "entity_hits": 0`).
**Not one held periodical or print byte names this registrant.** Their value to the dossier is as a
*negative control* for the naming test, and nothing else.

STATUS: WRITTEN (§1.4-1.6)

## 2. The five-family verdict (every family gets a state; an untried family is never a null)

States: **TRIED–ANSWERED** / **TRIED–UNANSWERED** (tool or network refused; remedy named) / **UNTRIED**.

| family | state | what came back, and the measurement that says so |
|---|---|---|
| **(a) SEC / EDGAR filings** | **TRIED–ANSWERED**, and the only family that answers **in-window** anywhere on this company | 2,612 indexed accessions; measured floor **1994-02-09**; `rows before 1994-02-09 = 0`; **55** in-window accessions (1971-01-01→1995-12-31) across 21 forms; **10 stored / 1,713,053 B / 216,400 words**; `_UNANSWERED.csv` 0 rows; `_SKIPPED.csv` **45** slots never opened (`--max-docs 30` cut + one-doc-per-filing selection), incl. the in-window **424A 1994-08-26** and **8-A12B 1994-08-19**. `slices_capped = no` in `00_universe/_FLEET_INTAKE.tsv`, so this is a **measured perimeter**, not a capped walk (RD-134). The pre-1994-02-09 silence is EDGAR's own floor, **not** "the company filed nothing" — Cardinal Distribution was a registrant from at least **1993-06-01** (the base prospectus date printed in the 424B2, §1.1) and it had a Commission file number **0-12591** (10-K FY1994 header) and file **33-62198** (8-K l.110-112) that pre-date the EDGAR record. |
| **(b) web archives** | **UNTRIED** | 0 calls; `sources/web_archive/` **does not exist**; `tools/queries.json` has no `web_archive` task for cardinal (8 tasks, families enumerated in §0); `candidates.csv` has **0** `web_archive` rows for cardinal. Nothing was attempted, so nothing may be reported as empty. RD-131's NR-1 open defect applies exactly: this state is held honest only by my care, because no gate checks it. Even if run, the fleet's web-archive onset is mid-1990s, so it cannot reach Stage 1/2 and could only ever reach the last ~18 months of Stage 3. |
| **(c) periodical corpora** | **TRIED–UNANSWERED** (3 of 5 routes refused; 2 answered with zeros or out-of-window namings) | Per route, from `00_universe/harvest/candidates.csv` (53 cardinal rows, header enumerated in §0): **chronicling_america** — 2 queries, each `UNANSWERED` "SKIPPED: hard stop: 5 consecutive failures (host halted)" **plus** one `ERROR`/`404` that saved a negative artifact (`chronicling_america/5baca6e0fb17f3c5-r20260929T130143Z.json`, `…/2abf9b5a140ba73b-…`); the second CA query is a *name-discovery* one (`"formerly known as" Cardinal health`, 1900-1998) — refused, so the predecessor-name question has **no** CA answer either way. **hathitrust** — 1 query, `UNANSWERED`, same host-halt. **google_books** — 17 rows, `http_status 200` at metadata level only, **0 bytes** reached the corpus; 6 rows carry the index label `TIER1_CANDIDATE` (Computerworld 2004; *Introduction to Health Care Delivery* 2012; *Kiplinger's* 2010; **The Corporate Directory of US Public Companies 1994** and **1995**; *Signal* 2005) and the feed summary line reads `totalResults=300 (Google's display cap, NOT a corpus count)`. **internet_archive** — the entity-anchored `"Cardinal Health" AND mediatype:texts AND YEAR:[1970 TO 1998]` returned **1** item (International Directory of Company Histories 1997, out-of-window, 0 bytes); its `[FACET-FREE per RD-130]` re-run returned **20** rows, of which **19 are `gov.uscourts.*`** docket mirrors naming `Cardinal Health, Inc.` / `Cardinal Health 200, LLC` / `Cardinal Health 110, LLC` (e.g. *Terlecky v. Cardinal Health*, *HARRISON COUNTY, INDIANA v. CARDINAL HEALTH, INC.*) — a **naming attached to this entity**, but litigation text from the 2000s-2010s, i.e. out-of-window and 0 bytes held; the trade-press title query `(title:("Drug Store News") OR title:("Chain Drug Marketing") OR title:("Healthcare Financial Management")) AND Cardinal …` printed `EMPTY (proven null): numFound=0` **both with and without** the YEAR facet — the only genuinely answered periodical route, and it says nothing about the *entity* because it was run with the bare word `Cardinal`. **Mined bytes:** `sources/harvest_mine/_index.json` records 12 mined / 31 untried-by-limit and verdict `BARE_WORD_MATCH` with `entity_hits: 0` on **all 5** held layers (§1.6). |
| **(d) digitised corporate print** | **TRIED–UNANSWERED**, with the cause measured | `corporate_print/` holds **3 files and 0 print-unique documents**: all three are md5-identical to their `periodicals/` twins (§1.6, hard rule 4). Of the 2 CP tasks in `tools/queries.json`, the wide one (`company_terms: ["\"cardinal health\"", "cardinal", "\"cardinal health inc\""]`) returned 6 items and **every one is a bare-word decoy** (Cessna Cardinal flight-test report; cardinal spline curves; Alberta *Cardinal Divide* survey; *São Paulo growth and poverty*; ERIC *Cardinal Principles Report* ×2); the creator-scoped one returned `NULL` for un-faceted params and `UNANSWERED` ("numFound=0 **WITH A YEAR FACET**. Bound print runs are frequently catalogued with year=None") for faceted params — RD-130's class, still live on one of this company's two CP routes. **No annual report, shareholder report or house organ of Cardinal Health or of Cardinal Distribution is on disk.** Quantifier check for the route I say is missing: `grep -c -i "cardinal distribution" tools/queries.json` → **0** (against `grep -c -i cardinal tools/queries.json` → **23**). |
| **(e) auction / museum / manuscript** | **UNTRIED** | 0 calls, no scripted route, no directory, no index rows. For an Ohio company founded in the 1970s the natural deposit candidates (Ohio History Connection; Western Reserve Historical Society; a university special-collections business-paper holdings; and the company's own archive) were never queried, and §14 r6 forbids calling that a null. |

**Families that counted, per §15.2:** Stage 3 → **(a) only**. Stages 1 and 2 → **none**. Provisional for all
three because (b), (e) are UNTRIED and (c), (d) are UNANSWERED with named remedies.

STATUS: WRITTEN (§2)

## 3. Per-stage tiers (§15.2), each measured against that stage's own window (RD-112)

| stage | proposed window | families returning **in-window Tier-1 text naming this registrant** | tier | deliverable / cap | ≈ runs |
|---|---|---|---|---|---|
| **1 — origin / predecessor** | 1971-01-01 → 1979-12-31 | **0.** (a) answers only from 1994-02-09; its 1979 and 1971 sentences live in documents filed 15-24 years after the events, so they are carriers, not in-window returns (Ford precedent, §1.3 of that dossier); (c) CA/HT refused, GB/IA 0 bytes, mined bytes all bare-word; (d) 0 print-unique bytes; (b),(e) UNTRIED | **T3 register — PROVISIONAL** | short narrative + registers; §K, §N, §U mandatory; **8k w/stage** | 3-4 |
| **2 — Cardinal Distribution build-out** | 1980-01-01 → 1994-02-06 | **0 on the filing-date reading; 1 on the reporting-period reading** — the 8-K of 1994-02-11 *is* an in-window document for Stage 3 but its contents are FY1991-FY1993 statements and the dated 1990/1991/1993 acquisitions (§1.4a2), i.e. Stage-2 facts in a Stage-3 carrier | **T3 register — PROVISIONAL** (T2 **only** if the orchestrator rules that a document reporting the stage's own fiscal years counts as in-window **and** a second family answers) | 8k w/stage | 3-4 |
| **3 — combination → named, listed wholesaler** | 1994-02-07 → 1995-12-31 | **1 — (a) filings**: 10 stored accessions, 1,713,053 B, entity-attached by CIK guard `ok`, carrying dated acts (1994-02-07 completion; 1994-02-07 rename narrative; 1994-08-19 8-A12B NYSE registration indexed though not stored; 1995-10-10 MSI S-4), the Dublin principal-executive-offices statement (S-3 l.511), the 16-name operating-subsidiary roll-call (10-K l.160-168) and the drug-wholesaling descriptor (35 hits / 7 docs) | **T3 register, filings-carried** — the density inside a T3 cap is high (216,400 words of primary text), but §15.2 counts **families**, not bytes, and only one answers | 8k w/stage | 3-4 |

**The RD-112 boundary case, stated for the orchestrator rather than decided here.** RD-126 left Costco's
question open: "measured against Stage 1's own window, family (a) yields in-window *text* but **no in-window
document**, which is the RD-112 boundary case the convention has not yet decided." Cardinal is Costco's
**mirror image**: for Stages 1-2 it has *no in-window document* at all (floor 1994-02-09) but in-window
**periods** reported inside later documents (FY1991-1993 statements, 1990-1993 acquisition notes); and for
Stage 3 it has in-window documents whose most load-bearing sentences are out-of-window recitals. Whichever way
the convention is ruled, Cardinal's Stage 1 does not reach T2, because no ruling puts a *second family* into
that window; but Stage 2's tier **does** turn on it, so the ruling is worth making before dispatch.

**Boundaries I propose and what would move them.**
1. Stage 2's end (1994-02-06) is arbitrary by five days against the 8-K's filing date; the *event chain* it
   reports starts **1993-10-11** (Reorganization Agreement). Cutting Stage 2 at **1993-10-11** and starting
   Stage 3 there would put the whole Whitmire chain into Stage 3 and leave the 1990-1993 acquisition notes
   unambiguously in Stage 2 — cleaner than my cut, and it is the orchestrator's call, not this probe's.
2. Stage 1's 1971 endpoint should be recorded as `UNKNOWN`, not `1971`, in `timeline.csv` until a carrier names
   the predecessor. If the convention wants a Stage-1 window that is defensible from **held** documents only,
   the honest window is **1979 → 1990-06-18** (formation recital → first dated acquisition with a carrier), with
   1971-1978 carried as predecessor ancestry at `UNKNOWN` — the Target-1902 / Berkshire-predecessor treatment.
3. Nothing bridges **1979-1990** and **1994-02-09** in EDGAR at all, so this company's chronology gap is
   *paper-shaped*: it must be filled from (c)/(d) or from the missing 1993-06-01 prospectus (§5 FETCH REQUEST).

STATUS: WRITTEN (§3)

## 4. The origin / predecessor question — every carrier found, file and line

| # | question | carrier (file : line) | verbatim | class / date-relation | tier-1? | verdict |
|---|---|---|---|---|---|---|
| 1 | When was the registrant formed? | `sources/sec/0000950152-94-000897_…txt` **l.2596-2597**; `sources/sec/0000950152-95-002183_…txt` **l.453-454**; `sources/sec/0000950152-94-001030_…txt` **l.333-334** | "since its formation in 1979" | FACT that the registrant *says* 1979; **RETROSPECTIVE SOURCE** (15 yr late); one lineage | Tier-1 doc, out-of-window recital | **ANSWERED as a company claim, 1979; the act itself UNANSWERED** (no charter, no state, no consideration, no co-founders) |
| 2 | What is the 1971, and whose is it? | `sources/sec/0000950152-94-001030_…txt` **l.222-223** (column definition) + **l.243** (Walter 1971), **l.297** (second 1971) | "the year in which each first became a Director of the Company **or the Company's predecessor in interest**" | CONTEMPORARY OBSERVATION *of the 1994 board roster*; the 1971 is an inference by column definition | Tier-1 doc | **UNANSWERED as to the predecessor's identity.** No held document names it (`predecessor` = 3 hits, one here + 2 about MSI's own predecessor) |
| 3 | Who founded it? | **no carrier.** `Hult` = 0 occurrences / 0 of 10 docs; `founded` = 0; the only founder-adjacent names are **Robert D. Walter** (55 hits / 6 docs, always as "Director, Chairman and CEO … since its formation in 1979" and as the counterparty "Employer" in an Ohio-corporation employment agreement, 10-K **l.7895**) and **John F. Havens**/**Michael E. Moritz** (1979) | — | — | — | **UNKNOWN.** Refused: naming any founder for Stage 1. Walter is credited *with a role at the formation*, which is not a founding claim (J&J precedent in RD-130: "a title … is a role, not a founding claim") |
| 4 | What was the registrant called before? | 10-K **l.50** (`FORMER CONFORMED NAME: CARDINAL DISTRIBUTION INC`), **l.77** ("(formerly known as Cardinal Distribution, Inc.)"), **l.171-172**, **l.5678**, **l.7895**; 424B2 **l.70**; 8-K header (`COMPANY CONFORMED NAME: CARDINAL DISTRIBUTION INC`) + body title block **l.80**; `DATE OF NAME CHANGE: 19920703` in **7 of 10** docs | "Prior to February 7, 1994, the Company was known as Cardinal Distribution, Inc." | FACT, entity-attached by CIK | Tier-1, in-window | **ANSWERED** — the former legal name is `Cardinal Distribution, Inc.`, an Ohio corporation. The **date** of the rename is a §U conflict with three candidate datings (§1.1) |
| 5 | Where was it based, and did it move? | 10-K cover **l.87-89**; FY1995 10-K **l.70-72**; S-3 **l.511**; 424B1 **l.380**; DEF 14A **l.174**; 10-K **l.382**; 8-K/SC 13D/S-4 headers; S-4 **l.3105-3108**, **l.5976-5977** (MSI headquarters-retention covenant) | "655 METRO PLACE SOUTH, SUITE 925, DUBLIN, OHIO 43017" | FACT for 1994-02-11 onward | Tier-1, in-window | **ANSWERED from 1994-02-11 only. Any earlier city: UNANSWERED** — both `Cleveland` hits are outside counsel (S-3 **l.118**, 10-K **l.5469-5470**), so the "moved city" lead is a decoy (§1.5b) |
| 6 | First dated corporate act in the build-out | 8-K **l.867-873** (1990-06-18 Ohio Valley-Clarksburg, $27,125,000 cash), **l.880-885**, **l.887-892**, **l.894-900**, **l.902-915**; 10-K **l.1702**, **l.1709**, **l.3981**, **l.1647** | see §1.4a2 table | FACT, audited primary document | Tier-1, Stage-2 periods in a Stage-3 document | **ANSWERED from 1990-06-18 forward**; 1979-1990 has **no carrier** |
| 7 | What was the business? | 10-K **l.176-178** ("The Company distributes products to hospitals, drug stores, alternate care centers, and the pharmacy departments of supermarkets and mass merchandisers located throughout the continental United States"); **l.232** "its core drug wholesaling activities"; **l.283** "Savannah, Georgia based drug wholesaler"; supplier concentration **l.179-182** (largest ≈7% of net sales; five largest ≈29%, FY1994) | — | FACT | Tier-1, in-window | **ANSWERED** for 1994; the descriptor "full-service wholesaler" also at 8-K **l.663** |
| 8 | Is the naming phrase attached to *this* entity in the non-filing record? | **No.** `Cardinal Health` = 0 and `Cardinal Distribution` = 0 occurrences in all 5 held non-SEC layers (§1.6); in the fleet index the only entity-attached non-filing namings are 19 `gov.uscourts.*` docket rows, out of window, 0 bytes | "FOR A CESSNA CARDINAL" (l.28) / "A NATURAL BIAS APPROACH TO CARDINAL SPLINE CURVES" (l.1) / "CARDINAL DIVIDE AREA BASELINE SURVEY" (l.1) / "Cardinal Principles Report" (l.30) | — | — | **Bare-word class, reported separately and never counted.** RD-124's test applied: 5 documents, 250 `cardinal` hits between them, **0** namings of this registrant |

STATUS: WRITTEN (§4)

## 5. `## Untried` — one route per line, with the command that would run it

1. **(c) Chronicling America — TRIED–UNANSWERED (host halted ×2, then 404 ×2).** Remedy: probe the endpoint, then
   re-run the two existing tasks (`CA 'Cardinal Health' Dublin Ohio 1970-1998`; `CA NAME-DISCOVERY '"formerly known
   as" Cardinal health'`, 1900-1998): `python tools/ca_endpoint_probe.py` then
   `python tools/periodical_harvest.py --company cardinal --facet-free` (**not run this pass, by order**). Store
   under `sources/periodicals/`. A 403-with-challenge keeps the family UNANSWERED; only a 200 with rows answers it.
2. **(c) HathiTrust — TRIED–UNANSWERED (1 task, host halted).** Same remedy, and it needs a **new task** on the
   former legal name: `q1="Cardinal Distribution"` (healthcare / wholesale / Ohio), unbounded era per RD-130's
   no-YEAR-facet rule.
3. **(c) Google Books text — UNTRIED at body level** (17 metadata rows, 0 bytes). Six indexed items are worth
   bytes because two of them are *directory entries for the window's own end years*:
   `vYlFDAAAQBAJ` (*The Corporate Directory of US Public Companies 1994*, matched page PA298) and
   `ZbBkDAAAQBAJ` (…1995, PA297). **Discipline first:** a directory entry naming a company is **not** the
   registrant's origin (hard rule 5), so these are leads for address/officer/name confirmation only.
4. **(c) The 31 periodical items `harvest_mine.py` left under its `--limit`** (its own
   `untried_by_limit: 31`; and the 20 court-docket rows from the RD-130 facet-free reharvest are among the rows
   never opened). Route: `python tools/ia_text.py list-files internationaldir0018unse` then
   `python tools/ia_text.py internationaldir0018unse --file <djvu.txt>` for the one IA item the faceted entity
   query returned (International Directory of Company Histories, 1997 — **out-of-window**, and a retrospective
   tertiary company history, so it can settle the *story* at Tier-3 `RETROSPECTIVE SOURCE` and cannot raise any
   in-window tier).
5. **(c) Trade-press back-files under the entity's own name, not the bare word.** The existing task searched
   `title:("Drug Store News") OR title:("Chain Drug Marketing") …) AND Cardinal`; it printed
   `numFound=0` faceted **and** facet-free. Re-cut the query with the quoted phrases the filings themselves
   supply — `"Cardinal Health"`, `"Cardinal Distribution"` — and add the thirteen acquired-company names from
   10-K l.160-168 as `VARIANT_TERM` candidates. **UNTRIED as posed.**
6. **(d) Digitised corporate print on the pre-1994 legal name — UNTRIED.** No task in `tools/queries.json`
   contains `Cardinal Distribution` (measured: `grep -c -i "cardinal distribution" tools/queries.json` → **0**,
   vs `grep -c -i cardinal tools/queries.json` → **23**), and `harvest_mine.py`'s entity vocabulary for this slug
   was `name phrases: [cardinal health]` only (A4 l.21), so even a held *Cardinal Distribution, Inc. annual
   report* would have classified as `VARIANT_TERM_HIT` at best. **This is the route most likely to change the
   verdict** (RD-130: this family flipped Walmart, Target, Boeing and Kroger).
7. **(d) The registrant's own 1994/1995 annual reports as print** — the 10-K texts are held as SGML, but no
   shareholder-report layer is. Query `creator:"Cardinal Health"` / `creator:"Cardinal Distribution"` un-faceted.
8. **(b) Web archives — UNTRIED, 0 calls, no scripted route.** CDX for the corporate domain and for the Ohio
   trade-press sites; store under `sources/web_archive/` (which does not exist yet). Fleet floor is mid-1990s, so
   the in-window value is limited to the last ~18 months of Stage 3 — recorded so the family is queried, not
   guessed at.
9. **(e) Auction / museum / manuscript — UNTRIED.** No tool reaches it and the web budget is 0. Needs an
   orchestrator decision or a new script (Ohio History Connection and Western Reserve Historical Society business
   collections; university business-history archives for Ohio wholesalers 1971-1990; documentary-sale records for
   distributor archives, the precedent that made Apple exemplar-capable).
10. **(a) The 45 in-window filing slots never opened** (`sources/sec/_SKIPPED.csv`), including **424A
    1994-08-26** and **8-A12B 1994-08-19** — both in-window and both capable of carrying an organization/history
    paragraph the stored set lacks. **Blocked by a tool defect, so it is UNANSWERED, not UNTRIED** — see the
    FETCH REQUESTs.

### FETCH REQUEST: (script refused; bytes are not on disk; claim stays UNANSWERED)

```
FETCH REQUEST 1 -- in-window prospectus with a probable "Organization/The Company" history section
  registrant : CARDINAL HEALTH INC (CIK 0000721371; conformed at the time as CARDINAL DISTRIBUTION INC)
  accession  : 0000950152-94-000876   form 424A   filed 1994-08-26   (in window; `_SKIPPED.csv` slot)
  wanted     : primary document of the accession, full text
  why        : the stored 10-K/DEF 14A recite 1979 and 1971 but no history section; a 424A for a common-share
               offering normally prints one. It is the likeliest in-window carrier of the 1971-1979 predecessor.
  route tried: python tools/sec_intake.py grab "CARDINAL HEALTH INC" --company-dir
               founders_playbook/01_companies/company_015_cardinal --accession 0000950152-94-000876
               -> ValueError at tools/sec_intake.py l.1324 (see §6 defect 2). NOT run as `auto`: `auto`
               overwrites sources/sec/_RUN.json and _MANIFEST.csv, which are the fleet intake's provenance
               record for the stored 10 (hard rule 2, add-only).
  claim state: UNANSWERED

FETCH REQUEST 2 -- the base prospectus the stored 424B2 supplements
  reference  : "PROSPECTUS SUPPLEMENT (TO PROSPECTUS DATED JUNE 1, 1993)" (424B2 l.63)
  wanted     : the 1993-06-01 base prospectus (shelf file no. 33-62198, cited at 8-K l.110-112); if EDGAR holds
               nothing for this CIK before 1994-02-09, this is a full-text-search or paper route, not a script
               route -- mark it UNTRIED-by-tool and record the measured floor 1994-02-09.
  claim state: UNANSWERED

FETCH REQUEST 3 -- NYSE registration and the transition report
  accessions : 0000950152-94-000863 (8-A12B, filed 1994-08-19); 0000950152-94-000153 (10-C, filed 1994-02-16)
  why        : 8-A12B dates the listing event for Stage 3; a Form 10-C/transition instrument is the standard
               carrier of state of incorporation and organisational history.
  claim state: UNANSWERED (same broken `grab` route)
```

STATUS: WRITTEN (§5)

## 6. Defects returned for the orchestrator, and what this probe refused to claim

**Defects (each measured, none is evidence about the company).**

1. **`tools/sec_intake.py grab` is dead in the water, fleet-wide.** Ran
   `python tools/sec_intake.py grab "CARDINAL HEALTH INC" --company-dir founders_playbook/01_companies/company_015_cardinal --accession 0000950152-94-000876`
   → identity resolved cleanly (`'CARDINAL HEALTH INC' resolved to CIK 721371 … by name-exact`) then crashed:
   `ValueError: too many values to unpack (expected 2)` at **l.1324** (`listing, lnote = doc_listing(a.cik, a.accession)`)
   while `doc_listing` (l.490) documents and returns a **3-tuple** — `(items, note, form)` — and the *other* call
   site, **l.916**, unpacks three correctly. RD-130 hardened `grab`'s 404 behaviour and left the arity broken, so
   **no probe can add one in-window document without running `auto`**, and `auto` overwrites
   `sources/sec/_RUN.json`, `_MANIFEST.csv`, `_SKIPPED.csv` (l.1371-1385) — i.e. it destroys the fleet intake's
   provenance record for the 10 stored documents. Hard rule 2 forbids that, which is why §5 went out as FETCH
   REQUESTs. **This blocks the recital route for every company in the fleet, not just this one.**
2. **The mine's own counts mix bases by one.** `sources/harvest_mine/_index.json`: `candidates 44, mined 12,
   untried_by_limit 31` — but 12 + 31 = 43 = tonight's `item_id`-bearing cardinal rows, and the 44th is the
   google_books **FEED SUMMARY** row with a blank `item_id`. Report the item count (43) to the merge.
3. **13 of the 53 cardinal rows in `candidates.csv` carry the label `TIER1_CANDIDATE`; the fixed classifier
   promoted 0 of them.** (`Counter(r['classification'])` → `LEAD_ONLY 31, TIER1_CANDIDATE 13, UNANSWERED 4,
   NULL 3, ERROR 2`.) A 100% false-promotion rate on this slug, and the cause is in our own query file: the
   corporate_print task ships **the bare token** in both places —
   `company_terms: ["\"cardinal health\"", "cardinal", "\"cardinal health inc\""]`,
   `name_patterns: ["cardinal health", "cardinal health inc", "cardinal"]` — so the family's hits are leads about
   *a word* by construction (RD-124). Single-word slugs need the bare token dropped from `name_patterns`.
4. **The entity vocabulary never uses the registrant's documented former name.** `Cardinal Distribution` occurs
   **22 times in 5 stored filings**, and the intake's own `_registrant_CIK0000721371.json` lists
   `former_names: [CARDINAL HEALTH INC, CARDINAL DISTRIBUTION INC]` — yet
   `grep -c -i "cardinal distribution" tools/queries.json` → **0**, and A4's entity list was
   `name phrases: cardinal health` + `other quoted terms: formerly known as`. **A tool that already holds the
   former name is querying without it.** Recommend `harvest_mine.py` / `queries.json` build the entity vocabulary
   from `_registrant_*.json` `former_names` rather than only from the slug and query text. The same gap covers the
   thirteen acquired names printed at 10-K l.160-168 (`grep -c -i -E "ellicott|marmac|humiston" tools/queries.json`
   → **0**).
5. **RD-130's YEAR facet is still live on one of this company's two corporate-print tasks** — the creator-scoped
   zero is recorded `UNANSWERED, not a null: numFound=0 WITH A YEAR FACET`, while the same task's un-faceted run
   recorded a `NULL`. `--facet-free` stripped the IA entity task (its reharvest rows are labelled
   `[FACET-FREE per RD-130]`) but the CP `year_range` parameter still reaches one route.
6. **RD-131's NR-1 is undecidable by machine and this dossier proves it.** Families (b) and (e) are reported
   **UNTRIED** on the strength of three negative measurements in §0 (no `web_archive`/auction directory; 0 rows in
   `candidates.csv`; 0 tasks in `queries.json`), not on a gate. The gate's own verdict vocabulary cannot tell
   "never attempted" from "attempted and refused", and tonight `gates.py` printed
   `tier: exemplar (no tier stated in this company's research/ dossiers -- exemplar assumed)` before this file
   existed — an assumption that would have graded a T3 company at exemplar depth.
7. **Universe CSV, re-confirmed:** `fortune_top_50_2026.csv` has no founding-date column (12 headers, §0). Its
   `hq_city = Dublin / hq_state = Ohio` is a **2026** record; on this company it happens to agree with the 1994
   header, but it is not evidence that Dublin was the origin city, and no probe should treat it as such.

**Refused on this pass, each with the reason it was refused.**

- **Refused to date the founding.** The corpus offers `1979` (a company recital written 15 years late, three
  accessions of one lineage) and `1971` (a director-since value under a column defined to cover "the Company's
  predecessor in interest"). Neither is a founding instrument, so Stage 1's origin year is **UNKNOWN** and 1971 is
  recorded as a *claim to test*, not a date. Class: `FOUNDER CLAIM / retrospective memory`, Conf **Low** for the
  events, **Medium** for "the registrant says 1979".
- **Refused to name a founder.** `Hult` = **0 occurrences in all 10 stored filings**, `founded` = 0, `hospital
  supply` = 0, `Syca*` = 0. Robert D. Walter appears 55 times but always **with an office** ("Chairman and CEO …
  since its formation in 1979", employment-agreement counterparty), which is a role, not a founding claim (RD-130's
  J&J ruling).
- **Refused to promote a single non-SEC byte.** The 5 held IA layers are **BARE_WORD_MATCH with `entity_hits: 0`**;
  they are reported in their own class (§1.6, §4 row 8) and were **not counted** in any tier. The 13
  `TIER1_CANDIDATE` index labels were not treated as evidence (hard rule 6).
- **Refused to count the `corporate_print/` shelf as a family.** All three files are md5-identical to
  `periodicals/` twins (hard rule 4) → **0 print-unique documents**, so family (d) cannot be "tried and answered"
  on bytes; it is TRIED–UNANSWERED.
- **Refused to treat the three duplicate EDGAR recitations as corroboration**, and refused to treat the
  8-K/10-K acquisition-note pair as two lineages: same corporate record, `corroboration = 1` (§3).
- **Refused to read `Delaware` (113 hits) as a re-domicile** — sampled contexts are `Cardinal Merger Corp., a
  Delaware corporation and a wholly-owned [subsidiary]`, MSI-side parties, and statute boilerplate; the registrant
  is "an Ohio corporation" in 7 held lines. **Refused to read `Cleveland` (2 hits) as a former headquarters** —
  both are Baker & Hostetler's address. **Refused the `St. Louis County` sentence** as a Cardinal domicile datum:
  it is a covenant that the *target* stay put.
- **Refused to date the rename.** Three candidate datings are attached to this registrant (1992-07-03 SEC
  conformed-name metadata in 7 of 10 docs; "prior to February 7, 1994" narrative; and the bracket
  1993-06-01 → 1994-02-17 implied by the 424B2 self-description and the conformed-name lag). Published as a §U
  conflict at Conf **Low**, not as a timeline date.
- **Refused to use the FY1991-1993 figures as Cardinal-Distribution-standalone**: they are the registrant's
  *restated supplemental pooled* statements with Whitmire (auditors Deloitte & Touche / Arthur Andersen), so any
  register row needs that basis note (§6 of the method: numerals carry their basis).
- **Refused to call the pre-1994-02-09 EDGAR silence a null**: it is a measured floor of a registrant that
  demonstrably filed paper-era documents (file numbers 0-12591 and 33-62198; a base prospectus dated 1993-06-01).
- Refused all web calls (0 used); refused to run `harvest_mine.py` and `periodical_harvest.py` (by order);
  refused to re-run `auto` (would clobber `_RUN.json`/`_MANIFEST.csv`); moved, renamed and deleted nothing under
  `sources/` — **the crash in §6.1 wrote no file, and this dossier plus the briefed gate report are the only two
  files this pass touched** (verified: company-dir file count 51 = 50 pre-existing + this file, and `sources/sec/`
  still holds exactly 10 `.txt` documents with their sidecars and 5 state files).

STATUS: WRITTEN (§6)

---

## 7. Gate, and the report the contract asks for

GATE run as briefed:
`python tools/gates.py --company-dir founders_playbook/01_companies/company_015_cardinal --checks csv,keys --fail-on substantive --out founders_playbook/03_quality_control/cardinal_s1_probe_gates.md`
→ `Findings: **2** | Passes: 0`, both `coverage`-only — `no register CSVs at root or research/ — csv/anchors gates
DID NOT RUN` and `no stage_*.md volumes found — keys/anchors gates DID NOT RUN` — with the tool's own line
"coverage-only findings … are **NOT failing the exit code unless --fail-on all**"; exit 0. `--fail-on substantive`
did not fire, which is the correct result for a probe that writes no registers (§15.4). Re-run after this dossier
landed, and the reader picked the tier up from it rather than assuming it:
`tier: T3 (tier T3 from A_chronology_feasibility.md — T2/T3 all mentioned in research/ (13 mentions, 0 on a verdict
line); if the dossier's own text names a different tier, trust the dossier and tell me, because this reader is not
the authority on your finding)`, same 2 coverage findings, exit 0. (That reader also counts `18 source documents`,
which is not the same base as §0's file census — noted, not reconciled here.)

**Verdict in one table.**

| stage | window (PROPOSED) | tier | families that counted | provisional because |
|---|---|---|---|---|
| 1 origin/predecessor | 1971-01-01 → 1979-12-31 | **T3 register** | none | (b),(e) UNTRIED; (c),(d) UNANSWERED; 45 filing slots unreached; RD-112 boundary case unresolved |
| 2 build-out | 1980-01-01 → 1994-02-06 | **T3 register** | none on a filing-date reading; (a) on a reporting-period reading | same, plus the stage-boundary ruling |
| 3 combination → named, listed wholesaler | 1994-02-07 → 1995-12-31 | **T3 register, filings-carried** | **(a) only** — 10 accessions / 1,713,053 B / 216,400 w | one family is one family; T2 needs a second |

**Route most likely to change the verdict:** a **facet-free, entity-anchored corporate-print/periodical re-run
against the registrant's documented former legal name `Cardinal Distribution`** — the string the stored filings
print 22 times, the intake's own `former_names` field already carries, and that **0 of the 8 `queries.json` tasks
and 0 of the mine's name-phrases ever used** (`grep -c -i "cardinal distribution" tools/queries.json` → **0**).
One digitised *Cardinal Distribution, Inc.* annual report or trade-press naming in 1979-1993 would put a second
family into Stage 2's window and move it from T3 to T2, and it would be the first *document*, rather than a
recital, to bridge the decade the company's own filings leave blank.

STATUS: WRITTEN (§7 — complete)

Written by `probe-cardinal`, 2026-10-06. Release:
`python tools/scaffold.py release --path founders_playbook/01_companies/company_015_cardinal/research/A_chronology_feasibility.md --agent probe-cardinal --done`

<!-- APPEND -->
