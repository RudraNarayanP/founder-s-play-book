# A_chronology_feasibility.md — KROGER (company_027), Stage-1 PROBE

**Probe agent:** `probe-kroger` (path claimed via `python tools/scaffold.py claim --path
founders_playbook/01_companies/company_027_kroger/research/A_chronology_feasibility.md --agent probe-kroger`).
**Date:** 2026-09-26 (probe run). **Scope:** chronology feasibility only. **This pass writes no volume, no
registers, and issues no certification** (probe contract). **Web budget used: 0 WebSearch / 0 WebFetch** —
every number below comes from a local script or a local byte, and the command that produced it is printed
beside it.

**Stage-1 window under test: 1883-01-01 → 1960-12-31**, taken from `tools/harvest_mine.py` `WINDOWS`, verified
by reading the file rather than the brief: line 61 reads
`"fanniemae": ("1938-01-01", "1970-12-31"), "kroger": ("1883-01-01", "1960-12-31"),`.

## 0. Measured state at probe start (verified, not inherited)

| item | measured | command |
|---|---|---|
| authored work in company dir | none (`find … -type f` returned nothing but my own claimed file) | `find founders_playbook/01_companies/company_027_kroger -type f` |
| directory layout | `research/`, `sources/corporate_print/` (empty), `_parts/` | `find company_027_kroger -type d` |
| kroger rows in harvest index | **28** (exact-match on the `company` column) | see §1 |
| index total | 2,598 rows (RD-128 recorded 2,043 → the nightly runner has added ~555 since) | `python -c "…len(rows)"` |
| universe row | rank 27, HQ Cincinnati, Ohio, FY ended 2026-01-31, Food and Drug Stores | `founders_playbook/00_universe/fortune_top_50_2026.csv` |

**Header enumerated before any field was read (RD-124 rule).** The real columns of
`founders_playbook/00_universe/harvest/candidates.csv` are:
`company, source_family, query, item_id, title, date_or_issue, url, snippet_or_hitcount, http_status,
classification, retrieved_at`. There is no `company_slug`, no `query_label`, no `date`.

**Counting key correction.** A substring search of whole rows for `kroger` returns **29**, not 28: the extra
row belongs to `jpmorgan` and matches only on its `title` value `Fortune`… (i.e. an unrelated row reached by my
own loose grep). Exact-match `company == "kroger"` gives **28**, which is the brief's figure and the correct one.
RD-124 in miniature, caught before it became a count in a dossier.

## 1. Harvest-index census (28 rows, verified twice)

```
python -c "import csv; rows=[r for r in csv.DictReader(open('founders_playbook/00_universe/harvest/candidates.csv',encoding='utf-8',newline='')) if r['company']=='kroger']; print(len(rows))"
```
→ **28**. The brief's figure reproduces on an exact `company`-column match. Distribution (same command,
counting `classification` / `source_family`):

* class: `TIER1_CANDIDATE` 12 · `LEAD_ONLY` 7 · `NULL` 4 · `UNANSWERED` 3 · `ERROR` 2
* family: `google_books` 19 · `chronicling_america` 4 · `corporate_print` 2 · `internet_archive` 2 · `hathitrust` 1

**Per RD-121 this index is a search signal, not evidence.** All 19 `google_books` rows are Google volume ids;
`tools/harvest_mine.py --company kroger --limit 10 --insecure` proves it: **19 candidates, 10 mined, 0 bytes,
10 UNANSWERED, 0 entity-naming** (its own JSON summary; dossier written to `research/A4_harvest_mine.md`). 7
candidate items were **left untried at the `--limit`** — an un-run search, not a null.

**RD-124 is live on this company, measured not asserted.** `creator:("Kroger") AND mediatype:(texts)` returns
**205 items**, the top of them Thomas Mann's *Tonio Kröger*, *Timm Kröger* (1906), a 1909 Kröger & Schwencke
wholesale nursery price list, a 1960 USDA Shorthorn cattle catalog and a 1983 BLM reservoir report — a surname,
a novella and a fruit of a different spelling. Any `kroger`-only match is a lead about a *word*.

STATUS: WRITTEN 2026-09-26

## 2. Family (d) — digitised corporate print / annual reports: **RETURNS in-window Tier-1 text**

This is the family that flipped Walmart and Target, and it flips Kroger — but not the way the index says.

**2.1 The bound run exists, and the fleet's "proven null" is a schema artifact.** The fleet `corporate_print`
tasks for kroger are recorded as `NULL` — "EMPTY (proven null): numFound=0 FOR THESE EXACT TERMS". Reproducing
the fleet query verbatim and then removing only its year facet:

| query | result |
|---|---|
| `(title:(kroger) OR title:("kroger company") OR title:("kroger grocery")) AND (title:(annual) OR title:(report) OR title:(reports) OR title:(shareholder) OR title:(stockholder)) AND mediatype:(texts)` **`AND YEAR:[1900 TO 1990]`** | `ok (0 rows matched of 0)` |
| the same query **without** the year facet | `ok (1 rows matched of 1)` → `krogercoannualreports`, "The Kroger Company Annual Reports: 1925–2007, 2009–2015", **`year = None`** |

The item has **no `year` field**, so `YEAR:[1900 TO 1990]` filters it out. The two kroger `corporate_print`
NULL rows are therefore **not proven nulls**; they are the RD-127 class exactly — an absence asserted by a
query shape rather than by a corpus. Command: `cd tools && python -c "import ia_text; print(ia_text.search(q, rows=8, allow_insecure=True))"` for each `q` above.

**2.2 The collection boundary is itself a finding** (the RD-097 test, run the way it was run for Walmart):

```
python -c "import ia_text,json,re,collections; s,b,n=ia_text.get('https://archive.org/metadata/krogercoannualreports',allow_insecure=True); ..."
```
→ HTTP 200, collection `['annual-reports-archive','journals']`, **695 files, 104 OCR text layers,
10,070,024 B**; per-layer names are `kroger<YYYY>[a|b]_djvu.txt`; **years present 1925…2007 continuous,
2009…2015**; `GAPS_IN_1925_1960 = []`; **BYTES_1883_1924 = 0**; `BYTES_1925_1960 = 935,867`; no layer is
under 400 B (so a zero over any fetched layer is a NULL, not UNANSWERED, per `ia_text.classify`).

So: **FY1930 print exists. FY1883–FY1924 print does not exist on this route.** The founding decade is a
perimeter of the collection, not of my effort.

**2.3 Bytes held by this probe** (`find` + `os.path.getsize`, command in §0 header of `sources/corporate_print/`
sidecars): **10 text layers, 634,225 B** — 8 company-print layers **259,425 B** (`kroger1925` 3,748 · `kroger1925a`
28,394 · `kroger1929` 8,229 · `kroger1930` 31,888 · `kroger1932a` 138,333 · `kroger1940` 15,033 · `kroger1950`
13,591 · `kroger1960` 20,209) plus 2 court layers **374,800 B**. Every file carries a `.meta.json` sidecar with
`transport: UNVERIFIED TLS` (the `--insecure` route this machine requires), which caps confidence below High per
§14 and the Target probe's precedent.

**2.4 What those bytes say (verbatim, with line numbers; OCR soft-hyphens normalised, no words added).**

*The founding act — the company's own history chapter in its own report:*
`kroger1932a_djvu.txt` **L424-426**: "In 1882, Mr. B. H. Kroger opened his first store in Cincinnati under the
name of the Great Western Tea Company with a cash capital of $722; his rent was $40 per month. Successful from
the beginning — a profit being earned the first year — another store was opened the second year."
**L429-430**: "until in 1902 the number of stores had reached 40 and the sales volume $1,750,610. At this time
the company was incorporated as the" → **L446-447** (after a page break): "Kroger Grocery and Baking Company
under the laws of Ohio, with Mr. B. H. Kroger as president." The chapter is titled "Early History and
Incorporation" (L422), and its table-of-contents entry is "II Early History and Incorporation.6" (L1099 area).

*Corroboration from a second report year:* `kroger1925a_djvu.txt` **L309**: "C OMMENCING with one store in 1882,
the history of the company"; **L114**: "(Incorporated April, 1902)"; **L2689-2690**: "The Kroger business was
founded by B. II. Kroger in 1882 and was conducted under the name of 'B. H. Kroger' until April, 1902"
(`B. II.` is OCR for `B. H.`). `kroger1925_djvu.txt` **L328/333/341**: "B. H. Kroger, President" /
"B. H. Kroger, Jr., Treasurer" — founder-family governance.

**⇒ The window start in `tools/harvest_mine.py` (1883-01-01) is one year LATER than the company's own printed
founding (1882), and `1883` occurs 0 times in held print while `1882` occurs 3 times** (command in §2.6). The
folk date and the corpus disagree, and the corpus is older.

*First incurred operational failure — store-format, not financing, as expected of a grocer:*
`kroger1930_djvu.txt` **L240-241** (raw OCR, including its mangled date token `January 3/^9317`, which I read as
1931 but do not silently repair): "31, 1929, and the number of our stores, 5165 on January 3/^9317 a decrease of
410 stores or 7.35 per cent of the total number"; **L236**: "A careful survey indicated a duplication of
service by many of our smaller stores"; **L252**: "Plans for expansion by an orderly process of opening new
stores in desirable…"; **L263**: "similar remodelling of stores is planned for 1931"; **L301**: "**Cash losses
from hold-up robberies of our stores reached serious proportions**"; **L310**: new safes "in all our stores";
**L331**: "On January 3, 1931, there were in operation, 2770 stores in different States and…". Note L331 vs
L240: **the same report prints 5,165 and 2,770 for the same date** — an internal conflict the authoring pass
must adjudicate (it is probably a successor/predecessor or "in operation vs total" distinction; I do not resolve
it here). Also **L186**: "Industry. In volume of sales and number of stores, it ranks second in the nation."
And the 1930 reorganisation: **L343** "organized on November 22, 1930, and is operating successfully."
Late-window format evidence: `kroger1960_djvu.txt` **L489**: "smaller stores were closed and 52 stores remodeled.
At year end there were 1,372 food stores in…" and **L553**: "was in receivership at the time it was purchased".

*Self-narrative caution:* these are the company's own reports. "One lineage, re-iterated" is company
self-narrative, not independent corroboration (RD-097's Kentucky/Arkansas ruling). 1925a and 1932a are two
printings of the same corporate story.

**2.5 The accounting-basis trap (RD-125's class), documented straight from print:**
`kroger1925` "year ended December 31, 1925" · `kroger1929` "FOR THE YEAR ENDED DECEMBER 31, 1929" ·
`kroger1930` "**year ending January 3, 1931**" · `kroger1932a` "year ending January 2, 1932" · `kroger1940`
"FOR THE FISCAL YEAR 1940, **ENDING DECEMBER 28, 1940**" / "beginning December 31, 1939 and ending December 28,
1940", sales "$258,115,025 (52 weeks)", net income "$4,607,126, or $2.51 per share after preferred dividends" ·
`kroger1950` "Year Ended December 30, 1950" + L588 "the company adopted the Iast-in-first-out method of
inventory valuation" with L592 "a reduction of approximately $1,302,000" · `kroger1960` balance sheet
"December 31, 1960 and January 2, 1960". **At least three year-end basis changes inside the window**
(Dec-31 → early-Jan → late-Dec 52-week → Dec-31). No Stage-1 series may be footed across those boundaries
without restating the basis.

**2.6 Naming chronology, and what my own pattern could not prove.** Masthead forms in held layers: 1925 · 1929 ·
1930 · 1932 · 1940 print "Kroger Grocery (and|&) Baking"; 1950 and 1960 print "**Kroger Co.**". The short form's
earliest appearance among held bytes is therefore 1944–1950, but my detector matched `Kroger Co` inside
`Kroger Company` in the 1925a and 1930 layers too, so **the exact rename date is UNKNOWN on this pass** and the
104-layer run is the carrier that can fix it. Hypothesis check: `Big Star` **0** hits, `Yuengling` **0** hits,
`Great Western Tea` **1** hit across all held print (command: python re-count over
`sources/corporate_print/*_djvu.txt`) — the successor-name routes the index hypothesised for kroger are **not
borne out by held bytes**, and the printed predecessor name is *Great Western Tea Company*.

**2.7 Sub-carrier: in-window court and government-document print, same corpus, Tier 1 by §5.** Of the 22 IA items
matching `title:("Kroger") AND mediatype:(texts) AND year:[1880 TO 1960]`, **exactly 3 name this registrant** and
19 are Mann novellas, German shipyards ("Neptun und Kroger", 1947–48 CIA), a nursery price list and a cattle
catalog: `dc_circ_1934_6195_us_ex_rel_kroger_grocery_baking_co_v_icc` (1934) and
`micro_IA34806415_2343` = *Kroger Grocery & Baking Co. v. United States*, 323 U.S. 777 (1944), plus
`micro_IA34806415_2499` = *Estate of Kroger v. Commissioner*, 324 U.S. 866 (1945) (not fetched). Both fetched:
**287,558 B** (24 "Kroger") and **87,242 B** (23 "Kroger"). The 1934 record is a **supply-side** document —
"at Cincinnati, and, among other things was and is at all…", "Cincinnati, Ohio, numerous carloads of ordinary
livestock", "Cincinnati Union Stock Yard Company", "The Cleveland, Cincinnati, Chicago and St. Louis Rail[road]"
(L290-583) — i.e. the meat-procurement rail/stock-yard tariff chain behind a grocer that ran "1 abattoir"
(1925a L361-362). The 1944 brief names "The Kroger Grocery & Baking Company, three subsidiar[ies]" (L314).

STATUS: WRITTEN 2026-09-26

## 3. Family (a) — filings: **searched and ANSWERED, and the answer is out-of-window** (returns-nothing-with-perimeter)

The brief's command does not run: `sec_intake.py auto "Kroger"` → `error: unrecognized arguments: Kroger`
(`auto` takes `--cik`/`--ticker`, no positional name). Recorded rather than routed around. Working route:

```
python tools/sec_intake.py resolve --ticker KR
  → {"ticker": "KR", "cik": 56873, "name": "KROGER CO"}
python tools/sec_intake.py index --cik 56873 --company-dir founders_playbook/01_companies/company_027_kroger
  → index: 4126 filings from registrant 'KROGER CO' (CIK 0000056873, tickers ['KR'])
  → registrant guard = ok -- slug token(s) ['kroger'] match registrant 'KROGER CO'
  → 0 rows dropped for no accession, 287 without primaryDocument (both counted in the artefacts)
```

Header enumerated before any field was read: `filingDate, form, accession, reportDate, primaryDocument, source`.
From `sources/_index/submissions_CIK0000056873.csv`, **4,126 rows**: **earliest 1994-01-07**, latest 2026-09-28;
forms `4` 2,649 · `8-K` 337 · `424B5` 202 · `5` 202 · `10-Q` 98 · `11-K` 65 · `10-K` 33 · `S-8` 30;
**`S-1` count = 0**; **rows before 1961 = 0**; before 1940 = 0.

**Docs and bytes held vs indexed:** this pass ran `index` only — metadata held (`submissions.json` 882,362 B,
`submissions.csv` 378,617 B, `_INDEX_CIK0000056873.md` 4,120 B, `_registrant_*.json` 885 B); **0 filing documents
fetched, 0 B of filing text**, which costs Stage 1 nothing because 0 indexed filings are in-window.
RD-098's guard fired correctly and RD-112's five sub-defects did not recur on this route.

Per RD-112 the verdict is per stage: **family (a) is a hard null for Stage 1 (1883–1960) but a full carrier for
Stage 3**, and EDGAR's floor here (1994-01-07) is later than Kroger's own print floor by 69 years.

STATUS: WRITTEN 2026-09-26

## 4. Family (c) — periodical corpora: **split verdict — answered-perimeter for Stage 1, carriers already on disk for Stage 2/3, and two routes UNANSWERED**

`tools/queries.json` **does** carry a kroger block (so this family is **TRIED**, not untried — the brief's
contingency does not apply): tasks 235–242, i.e. 2 × chronicling_america, 2 × internet_archive, 1 × hathitrust,
1 × google_books, 2 × corporate_print. Command:
`python -c "import json,collections; d=json.load(open('tools/queries.json',encoding='utf-8')); print(collections.Counter(t['source_family'] for t in d['tasks'] if t['company']=='kroger'))"`.
Fleet-wide the file has 427 tasks over 5 families — there is **no sixth family label at all**, which is why (b)
and (e) below are structurally untried.

* **(c1) Internet Archive trade journals — searched, and the zero is about the COLLECTION, not the company.**
  The kroger rows record `numFound=0` for the "Progressive Grocer back-file sweep 1900-1970" and the
  "Chain Store Age / Stores 1900-1990" sweep. I tested the carriers themselves rather than trusting the zeros:
  `title:("Progressive Grocer") AND mediatype:(texts)` → **16 items, years 1982–1995, 0 of them in 1880–1960**;
  `title:("chain store age") AND mediatype:(texts)` → **27 items, years 1947, 1963, 1980–1995; exactly 1
  in-window (1963 — the copy Target already holds)**. So the grocery trade back-file the probe was told to use
  as the realistic pre-1960 carrier **is not in the IA texts corpus at all before 1962.** This is a
  returns-nothing-with-perimeter verdict, and the perimeter is the collection.
* **(c2) Chronicling America — UNANSWERED, and now the landed verdict says why.** The probe wired into the
  nightly workflow has reported: `founders_playbook/00_universe/harvest/_CA_ENDPOINT_TEST.md`
  (2026-09-29T18:05:27Z): **7 of 7 candidate shapes `CHALLENGED` / HTTP 403 Cloudflare; "ANSWERED shapes:
  none … no CA zero may be cited as a null."** My 4 kroger CA rows (2 UNANSWERED `SKIPPED: hard stop`,
  2 `ERROR`/404 with saved bodies) therefore stay **UNANSWERED**. Note the probe's test query was
  `"Wal-Mart" Bentonville`, not a Kroger phrase, so the verdict establishes the *endpoint*, not the corpus.
* **(c3) HathiTrust — UNANSWERED.** 1 row, `SKIPPED: hard stop: 5 consecutive failures`; and `ia_text.py`'s own
  header records that this machine's stale CA store blocks the HathiTrust host, with `INSECURE_HOSTS` not
  covering it. Never tried to text.
* **(c4) Google Books — leads returned, text UNREACHABLE by any script here.** 19 rows, 12 stamped
  `TIER1_CANDIDATE` with `viewability=all_pages` and a matched page (e.g. `NNn52klcXpsC` 1905 *Commercial and
  Financial Chronicle* p. RA15; `GEA_AQAAMAAJ` 1901 p. PA67; `PvyrwBlrrQUC` 1940 *Standard Corporation
  Descriptions* (S&P) p. PA1486 "Cincinnati, Ohio Joseph…"; `BajGB4fFBk0C` 1929 *The Northwestern Miller*
  p. PA1001; `nYAwAQAAMAAJ` 1914 *Annual Report of the Attorney General* [Ohio] p. PA541). These are the most
  promising in-window namings in the whole index — **and four of them are probably not namings of this
  registrant at all**: `7ZFBAQAAMAAJ` (1921), `FeFLAQAAMAAJ` (1922), `7McuAQAAIAAJ` and `OWW2v9FmTekC` (1925) are
  all **Ohio Building and Loan Association** annual reports, two of them matched at the *identical* page PA219,
  which is the signature of an officer surnamed Kroger, not a grocery company (RD-124). Out-of-window scholarly
  titles (2014 textbook, 1998 *Shelf Life*, 2017 *From Head Shops to Whole Foods*) sit in the same promoted pile.
  `harvest_mine` fetched 0 of 10 (all Google ids) → **10 UNANSWERED, 0 B**, so **no periodical text for this
  company has ever been held**.
* **(c5) Periodical text naming Kroger is already on disk in this corpus — but post-1960.** Corpus-wide grep of
  held `sources/periodicals*` bytes (1,202 candidate files) → **19 files contain "Kroger"**, headed by
  `company_006_cvs/sources/periodicals/micro_IA40706918_0157_djvu.txt` (1,494,549 B; 93 "Kroger", 22 entity-form)
  and `micro_IA40706951_0247_djvu.txt` (1,573,592 B; "The Kroger Co., Cincinnati $758 808 1,295 62%", "The Kroger
  Company includes sales through its corporate stores and subsidiary divisions"). IA metadata dates those items:
  **`Drug Store News`, date=1985 and date=1995** (`year=None` again — the same facet trap). Read-only grepping of
  siblings' bytes; nothing was written outside my own paths. **Verdict: family (c) cannot carry Stage 1, and does
  carry Stage 2/3 today.**

STATUS: WRITTEN 2026-09-26

## 5. Family (b) — web archives: **UNTRIED** (and structurally irrelevant to Stage 1)

No script reaches a web archive: `grep -rn "web.archive\|wayback\|cdx" tools/*.py` matches only a docstring line
in `periodical_harvest.py`, and `queries.json` has no `web_archive` family among its 427 tasks. Sibling companies
hold such bytes only because probes made them **by hand** (`company_002_walmart/sources/probe_wayback_*.txt`,
`company_005_alphabet/sources/wayback/`, `company_042_target/sources/web_archive/`), and my brief sets the web
budget at 0. So: **an untried family, reported as untried, never as a null.** Substantively it cannot touch
1883–1960 — the fleet's own measured web-archive floor is 1996-12-29 (RD-097) — but the rule is not
"cannot matter", it is "was it tried", and it was not.

## 6. Family (e) — auction / museum documentary records: **UNTRIED**

Same geometry: no scripted route exists in `tools/`, and the fleet's only precedent is Apple's probe spending web
budget on auction coverage (`Christie's 2026-01-23 lot`, `apple1registry`, Charterfields). At 0 WebSearch/WebFetch
this pass did nothing of the kind. For a company whose founding decade has **zero print in the collection**
(§2.2), (e) is the family with the most room to surprise — a ledger page, a store photograph, a bond coupon or
an incorporation document could still arrive in-window. **Untried, not empty.**

STATUS: WRITTEN 2026 (probe) — 2026-09-26

## 7. Per-stage tiers and the §15.2 run budget each implies

Tiers are issued **per stage against that stage's own window** (RD-112), counted as **families returning
in-window Tier-1 text** (§15.2), never as print volume inside one family.

| stage | window used | families returning in-window Tier-1 text | tier | §15.2 deliverable / cap | ≈ agent runs |
|---|---|---|---|---|---|
| **1 — origin** | **1882/1883 → 1960-12-31** | **(d) only** — 104-layer bound corporate-print run (8 layers held, 259,425 B) + 2 in-window court records (374,800 B), same carrier corpus. (a) answered-but-out-of-window; (b), (e) untried; (c) carrier absent pre-1962 | **T3 register** | short narrative + registers; §K, §N, §U mandatory; 8k w/stage | **3–4** |
| **2 — scaling** | 1961-01-01 → 1993-12-31 (proposed; the day after the Stage-1 window closes and the day before EDGAR's floor — both ends come from measured records, not ambition) | **(d)** print continuous 1961–1993 (33 years in the same run) **+ (c)** *Drug Store News* 1985/1995 already held (3.1 MB) → **2 families** | **T2 core** | evidence-bound §A–§U, full registers, records for load-bearing claims; 22k w/stage | **6–9** |
| **3 — national/mature** | 1994-01-07 → 2015-12-31 (EDGAR floor measured above; print ceiling is the bound run's last year) | **(a)** 4,126 filings indexed + **(d)** print 1994–2007, 2009–2015 + **(c)** held trade text → **3 families** | **T1 exemplar** | §A–§U full, claim records, 9 registers; 60k w/stage | **15–20** |

**The uncomfortable part of that table, said plainly.** Stage 1 here is *not* thin: one family carries a
continuous 36-year in-window corporate archive with a self-narrated founding, an incurred store-closure program,
supply-side litigation and a documented accounting-basis history — far more than Walmart's Stage 1 ever held
(nine reports, floor FY1972). §15.2 nonetheless counts *families*, so the honest verdict is **T3**, and the only
things that can raise it are a second family answering in-window, or the orchestrator deciding that print depth
should count. I am not making that rule change; I am reporting that the rule, applied as written, gives T3.

**Route most likely to change the Stage-1 verdict:** not more print. Either (e) auction/museum documentary (the
only family with genuine room, because the collection is silent 1883–1924) or a **HathiTrust/Google-Books text
route that actually resolves bytes** — 12 promoted in-window GB leads sit unreachable today. Removing the
`YEAR` facet fleet-wide (§2.1) does not change *this* company's tier — it changes the *evidence base*, and it
will change other companies' verdicts.

STATUS: WRITTEN 2026-09-26

## 8. Load-bearing open questions (each with the carrier that could settle it)

1. **Founding date and founding act — which document says what?** The corpus says **1882** (1932a L424; 1925a
   L309, L2689) as the opening of the first store, and **April 1902, Ohio** as the incorporation act (1925a L114,
   L2690; 1932a L429-447). The fleet index says **1883**, and `1883` appears 0 times in held print. Open: the
   *calendar day* of 1882, whether the Great Western Tea Company was a proprietorship or an entity, and whether
   an Ohio incorporation record antedates April 1902. Carrier: the remaining 96 layers of the bound run (esp.
   1926–1929, 1931, 1933–1939) + an Ohio secretary-of-state paper file (no script reaches it).
2. **Who is credited, by which document?** Held print credits **Mr. B. H. Kroger** as founder and first
   president (1932a L424, L447), and shows **B. H. Kroger, Jr.** as Treasurer (1925 L333) — a founder-family
   succession question the volume must handle as *company self-narrative*, one lineage. **W. H. Albers**, then
   first vice-president, speaks in a 1927 passage quoted at 1932a L465-466 — the earliest named operating
   executive in held bytes. The Lehman Brothers circular of **1927-12-15** appears as a footnote at 1932a
   L497-498 (275,000 no-par shares at $70): a money-side primary hiding inside a history chapter.
3. **First real-world experiment.** Held print answers it: one store, Cincinnati, 1882, named Great Western Tea
   Company, **$722 cash capital, $40/month rent** (1932a L424-426). Open: whether any document nearer 1882 than
   1925 survives — if not, the founding is a **43-years-retrospective company claim** and must be tagged
   `RETROSPECTIVE SOURCE` per §6.
4. **First repeatable validation.** 1932a L426-430 gives the company's own sequence: profit in year one → second
   store in year two → 40 stores and $1,750,610 sales by 1902. Open: whether the 40-store figure is
   company-reported only (the table's own source line, 1932a L416, reads "Data assembled from New York Stock
   Exchange listing applications and annual reports of company") and whether any independent carrier repeats it.
5. **First incurred operational failure — store-format/supply, as the brief expected, and held bytes have two.**
   (i) FY1930-31 contraction: **410 stores closed, "7.35 per cent of the total"**, "duplication of service by many
   of our smaller stores", a remodelling programme, and **"Cash losses from hold-up robberies of our stores
   reached serious proportions"** (1930 L236-241, L263, L301-310). (ii) 1960: "smaller stores were closed and 52
   stores remodeled", 1,372 food stores at year end, and an acquired company "in receivership at the time it was
   purchased" (1960 L489, L553). Open: which the volume treats as *the* first incurred failure, and whether
   1930's internal **5,165 vs 2,770** store conflict (same report, same date, L240 vs L331) is a scope difference
   or an error — do not foot a store series across it unadjudicated.
6. **Accounting basis.** At least three year-end changes inside the window (§2.5) plus the FY1950 LIFO adoption
   ("a reduction of approximately $1,302,000"). Any Stage-1 metric must carry its own basis line.
7. **Entity naming changeover.** "Kroger Grocery and Baking Company" (1925–1940 held) → "Kroger Co." (1950, 1960,
   and the 1944 brief). Exact rename date **UNKNOWN** on this pass; my own pattern conflated `Kroger Co.` with
   `Kroger Company`. Carrier: layers 1941–1949.
8. **Supply-side structure.** 1925a L361-362 prints "7 bread-baking plants, 3 cracker bakeries, 4 cake bakeries,
   1 abattoir, and also warehouses"; the 1934 ICC record documents the Cincinnati livestock/stock-yard tariff
   chain ("Cincinnati Union Stock Yard Company", L518-535). Open: whether vertical bakery/abattoir integration is
   the moat or the burden — the two are argued from different documents and belong in §U.

STATUS: WRITTEN 2026-09-26

## 9. Untried (one command each)

* **(b) web archives — no scripted route exists.** Wire one, then run:
  `curl -s "http://web.archive.org/cdx/search/cdx?url=kroger.com&output=text&fl=timestamp,original,statuscode&limit=40"`
  → hold under `sources/web_archive/`. Fleet `queries.json` has no `web_archive` family among its 427 tasks.
* **(e) auction / museum documentary records.** Needs the web budget this contract denies (Apple's precedent was
  a WebFetch route). Dispatch: a lot-search against Heritage/Christie's plus Cincinnati Museum Center / MoHRA
  finding aids for *Great Western Tea Company*, *B. H. Kroger*, *Kroger Grocery and Baking* 1882–1930.
* **(c) Chronicling America, Kroger-specific.** Re-run only after `CA_BASE` is fixed:
  `python tools/ca_endpoint_probe.py --help` first (my read of the landed verdict: 7/7 shapes 403, "ANSWERED
  shapes: none"). Until then every Kroger CA zero is UNANSWERED.
* **(c) HathiTrust text** (1 skipped task, TLS-blocked here): add `babel.hathitrust.org` to
  `ia_text.INSECURE_HOSTS` — a `tools/` edit I am forbidden to make — then
  `python tools/ia_text.py search --q 'Kroger grocery Ohio' --insecure`.
* **(c) Google Books full text for the 12 promoted in-window leads.** No reachable route from this repo; prove
  the wall again with `python tools/harvest_mine.py --company kroger --limit 20 --insecure` (expect `bytes: 0`).
* **(d) the other 94 in-window print layers of the bound run** (not fetched at this pass's limit). Per layer:
  `python -c "import ia_text; s,b,n=ia_text.get(ia_text.ocr_url('krogercoannualreports','kroger1931_djvu.txt'),allow_insecure=True)"`
  — or fix `ia_text.fetch` to address sub-files (defect D2).
* **(d) 7 harvest candidate rows left unmined by `--limit 10`**: `python tools/harvest_mine.py --company kroger
  --limit 20 --insecure`.
* **(a) documents behind the 4,126 indexed filings** (0 fetched by this pass; a Stage-3 need, not Stage 1):
  `python tools/sec_intake.py auto --cik 56873 --company-dir founders_playbook/01_companies/company_027_kroger --from 1994-01-07 --to 1999-12-31`.

STATUS: WRITTEN 2026-09-26

## 10. Defects returned for the orchestrator (not evidence), and what this probe refuses to claim

**D1 — the `YEAR` facet manufactures nulls over corporate print.** Fleet `corporate_print` tasks append
`YEAR:[1900 TO 1990]`; bound annual-report items carry `year=None`, so they are filtered out and written as
"EMPTY (proven null)". Proven on kroger: 0 rows with the facet, 1 without (§2.1). 103 `corporate_print` tasks
fleet-wide share the shape. Fix site is `tools/periodical_harvest.py`; I did not edit it.
**D2 — `ia_text.py fetch` cannot address sub-files of a bound run** (it writes one `<id>_djvu.txt` per *item*),
so a 104-layer run is reachable only per sub-file. I scripted that through the tool's own `get`/`ocr_url`, wrote
10 layers + sidecars into `sources/corporate_print/`, and stamped each sidecar with the route — Target-probe
precedent, not a new convention.
**D3 — the brief's intake command is wrong**: `sec_intake.py auto "Kroger"` → `unrecognized arguments: Kroger`.
Correct form is `resolve --ticker KR` then `index/auto --cik 56873`.
**D4 — the landed CA verdict probed a Walmart phrase** (`"Wal-Mart" Bentonville`), so it settles the endpoint
and no Kroger question.
**D5 — `harvest_mine`'s kroger pass applied an empty entity vocabulary** ("name phrases: none", "other quoted
terms: none" in `research/A4_harvest_mine.md`): the quoted terms are not extracted from rows like
`GB 'Kroger' annual report shareholder Cincinnati`. Moot here because 0 bytes were reached, but a
zero-promotion classifier is indistinguishable from a no-results classifier — RD-124's exact lesson, still live.
**D6 — duplicate index rows**: `nYAwAQAAMAAJ` appears twice, once `LEAD_ONLY` (`no_pages`) and once
`TIER1_CANDIDATE` (`all_pages`, p. PA541). The index must not be counted as two items.
**D7 — index growth during the run**: `candidates.csv` 2,598 rows (RD-128 recorded 2,043); the nightly runner is
a live writer on a file this dossier counts from.

**Refused claims (each would be an invention today):**
* No founding **day**, and no resolution of 1882 vs 1883 — the conflict and the two printings are recorded, not adjudicated.
* No store-count series: 2,856 / 5,165 / 2,770 / 4,884 / 1,372 are company-printed figures whose scope I have not
  adjudicated (1930 contradicts itself within one report, §8.5), and RD-127's composite-cell lesson says a
  grep-shaped assumption is not a reading. **The volume must re-read each in context before any register row.**
* No "Big Star" / "Yuengling" successor-name lineage: 0 hits in held bytes; the index's hypothesis is unsupported
  and the printed predecessor name is *Great Western Tea Company*.
* No claim that the four Ohio Building-and-Loan `TIER1_CANDIDATE` rows name this registrant — a surname is the
  likelier reading (two match at the identical page PA219), and promoting them would manufacture Tier 1.
* No claim that any periodical, web archive or auction record supports Stage 1: two families were never tried;
  two answered empty for reasons belonging to the collection or to a block, not to Kroger.
* No tier for the *company* (only per stage, RD-112); **no volume, no registers, no certification** from a probe.
* Nothing from the unverified-TLS layers at High confidence until re-checked on a verified channel (§2.3).

**Close-out enumeration (§14 rule 11).** `sources/` holds **28 files / 634,225 B of text layers** (10 layers + 10
sidecars + EDGAR index artefacts + `harvest_mine/_index.json`), all written by this pass or by `tools/` itself;
**nothing was deleted or moved**. Counts re-measured at close with the §1 and §2.3 commands. The only files that
arrived mid-run other than mine are the fleet's own (`candidates.csv` 23:20, `_CA_ENDPOINT_TEST.md` 23:35), both
cited above rather than ignored.

**Gate command for this company (coverage findings on a fresh company are the expected pre-authoring state):**
`python tools/gates.py --company-dir founders_playbook/01_companies/company_027_kroger --checks csv,keys --fail-on substantive`


