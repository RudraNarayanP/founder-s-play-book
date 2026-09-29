# Disney (company_044) — Stage-1 chronology-feasibility dossier (PROBE)

Written by `probe-disney`. **This is a probe artefact: it carries no volume, no registers, no
certification.** Origin window per `tools/harvest_mine.py` `WINDOWS`: **disney = ("1923-01-01",
"1945-12-31")"** — verified by reading the dict at `tools/harvest_mine.py` (line of the `WINDOWS`
assignment; `"disney": ("1923-01-01", "1945-12-31")`).

Web budget used: **0 WebSearch, 0 WebFetch.** Every byte below was reached through
`tools/sec_intake.py`, `tools/ia_text.py`, `tools/harvest_mine.py` or files already on disk.

---

## 1. Measured state at intake (verified, not inherited)

| item | value | command that produced it |
|---|---|---|
| `candidates.csv` rows for disney | **8**, all `classification = UNANSWERED` | `python -c "import csv;rows=list(csv.DictReader(open('founders_playbook/00_universe/harvest/candidates.csv',encoding='utf-8-sig')));print(len(rows));print([r for r in rows if 'disney' in (r.get('company') or '').lower()])"` → 2,598 total rows, 8 disney |
| candidates.csv header (enumerated before any field was read by name — RD-124) | `company, source_family, query, item_id, title, date_or_issue, url, snippet_or_hitcount, http_status, classification, retrieved_at` | same command, `print(list(rows[0].keys()))` |
| all 8 rows carry `item_id = ""`, `title = ""`, `url = ""`, `http_status = ""` | so **there is nothing to mine**; the queries were authored and never sent | inspection of the 8 rows above |
| `snippet_or_hitcount` on 7 of 8 rows | `SKIPPED: global max-requests cap 600 reached` | same |
| `snippet_or_hitcount` on the 1 `hathitrust` row | `SKIPPED: hard stop: 5 consecutive failures (host halted)` | same |
| `retrieved_at` on all 8 | `2026-09-29T13:09:40Z` | same |
| `sources/corporate_print/` at probe start | **empty** (`ls -la` showed `.` and `..` only) | `ls -la founders_playbook/01_companies/company_044_disney/sources/corporate_print` |
| dossier / volume / registers at probe start | none (`find` returned only `research/`, `sources/`, `sources/corporate_print`, `_parts/`) | `find founders_playbook/01_companies/company_044_disney -type f -o -type d` |
| `tools/queries.json` disney block | **EXISTS — 8 tasks** | `python -c "import json;q=json.load(open('tools/queries.json',encoding='utf-8'));t=q['tasks'];print(len(t));print(len([x for x in t if 'disney' in json.dumps(x).lower()]))"` → 427 tasks, 8 disney |

**Brief correction (the brief's own conditional).** The brief said: "If `tools/queries.json` has no
real disney block, say so — UNTRIED, not empty." It **does** have a real block: 8 tasks, including
entity-vocabulary forms (`"Walt Disney Productions" OR "Disney Brothers"`, and an
`IA exhibition/film trade press` task naming `Variety`, `Film Daily`, `Exhibitors Herald`, `Fortune`).
So family (c) is **configured-but-unsent**, not unconfigured. That is a different finding from the
Costco case in RD-112 (where the block itself was missing), and it is reported as such in §3(c).

---

## 2. Family (a) — FILINGS: the floor

### 2.1 The briefed command does not run

`python tools/sec_intake.py auto "Walt Disney" --company-dir founders_playbook/01_companies/company_044_disney`
→ `sec_intake.py: error: unrecognized arguments: Walt Disney`. `auto` takes **no positional**
(`python tools/sec_intake.py auto --help` lists only `--cik/--company-dir/--ticker/--from/--to/…`).
Recorded, not worked around silently: **DEFECT A-1 — the dispatch-brief command form for
`sec_intake.py auto` is wrong**; the runnable form is by `--ticker` or `--cik`.

### 2.2 What the intake actually found

`python tools/sec_intake.py selftest` → **`selftest: 42 checks, 0 failing`** (verified twice;
`… selftest 2>&1 | grep -c "PASS"` → `42`). Brief's claim confirmed.

`python tools/sec_intake.py resolve --ticker DIS`
→ `{"ticker": "DIS", "cik": 1744489, "name": "Walt Disney Co"}`

`python tools/sec_intake.py auto --ticker DIS --company-dir founders_playbook/01_companies/company_044_disney`
→ 1,141 filings enumerated; registrant guard `ok` (slug token `disney` matches `Walt Disney Co`);
window used `1900-01-01..2030-12-31` (from `sources/sec/_RUN.json`);
**40 documents stored, 25,839,637 bytes, 1,095,551 words**; identity `stored(40)+unanswered(1)+skipped(0)=41 vs attempted(41) -> OK`;
`nameless_rows 0`; `_SKIPPED.csv` 85 B (header only); plus
`UNANSWERED (120 filings): UNANSWERED NOT-ENUMERATED: 120 in-window filings were never listed because --max-docs 40 was reached`.

Field checks (header enumerated first: `filingDate, form, accession, reportDate, primaryDocument, source`):

```
python -c "import csv;rows=list(csv.DictReader(open('founders_playbook/01_companies/company_044_disney/sources/_index/submissions.csv',encoding='utf-8-sig')));print(len(rows));print('S-1:',[r for r in rows if r['form'].strip()=='S-1']);print('in-window:',len([r for r in rows if r['filingDate']<='1945-12-31']))"
```
→ **1,141 filings; S-1 rows: `[]` (no S-1 exists); in-window (≤ 1945-12-31) rows: 0.**
Earliest filing in the whole index: **2018-06-25, form `S-4`**, accession `0001193125-18-201596`,
primary `d770960ds4.htm` (`sources/_index/_INDEX_CIK0001744489.md`, "Earliest filing per form").

### 2.3 The registrant trap is live, and it is the RD-098 class

`sources/_index/submissions.json` → `cik 0001744489`, `registrant "Walt Disney Co"`,
`former_names ["TWDC Holdco 613 Corp", "TWDC Holdco 613 Corp."]`. **CIK 1744489 is the 2018 Fox-holding
shell that later took the operating name — it is not the registrant that existed in 1923-1945.**
Its EDGAR floor is 2018-06-25, so `auto` reporting "40 documents stored" over a 1900-2030 search
window says nothing at all about the origin era. Enumerating other Disney-named registrants
(`https://www.sec.gov/cgi-bin/browse-edgar?company=disney&…&action=getcompany`, saved to
`sources/sec/registrar_search/disney_company_search_20260929.html`): 8 registrants match `DISNEY`
(0001311661 Disney Anthea; 0001157676/7/8 DISNEY CAPITAL TRUST I/II/III; **0000029082 DISNEY
ENTERPRISES INC, SIC 7812 SERVICES-MOTION PICTURE & VIDEO TAPE PRODUCTION, CA**; 0001402178 Disney
Enterprises, Inc.; 0001418456 Disney Francis R; 0001234300 DISNEY ROY E), and `company=WALT+DISNEY`
returns 4 more (0000926480 WALT DISNEY CO CA; 0001744489; 0001004224 WALT DISNEY CO /CA/ /TA;
0001001039 TWDC Enterprises 18 Corp.).

Registrant-name searches for the origin-era entity forms — run through `sec_intake.http_get` on the
same index, flattened and read:

| name queried | registrants returned |
|---|---|
| `Walt Disney Productions` | **0** |
| `Disney Brothers` | **0** |
| `Laugh-O-Gram` | **0** |
| `Buena Vista Distribution` | **0** |

Those four are **NULLs over a live index**, not unanswered: the route answered and the answer is that
no EDGAR registrant carries those names. (Per RD-124, this is *not* a bare-word naming: these are
quoted registrant-name phrases against a name index.)

### 2.4 DEFECT A-2 — `data.sec.gov/submissions/CIK*.json` 404s on registrants that demonstrably have filings

`python -c "import sec_intake as s;[print(s.cik10(str(c)), s.http_get('https://data.sec.gov/submissions/%s.json'%s.cik10(str(c)))[0]) for c in (29082,926480,1004224,1001039,1402178)]"`
→ **all five `404 NoSuchKey`.** Yet `browse-edgar?action=getcompany&CIK=0000926480` returns **13 rows**
and `CIK=0000029082` returns a populated list (`3`, `3/A`, … 2020). So `sec_intake index --cik`
terminates at "submissions fetch failed: HTTP 404 NoSuchKey" for registrants the legacy index says
exist — the RD-112 "0 documents reads like an empty archive" class, arriving one stage earlier.
Recorded, not worked around. Consequence for this dossier: **the adjacent-registrant enumeration
below rests on `browse-edgar`, which `tools/` does not otherwise use.**

All 13 rows of CIK 0000926480 (`WALT DISNEY CO CA`) are `NO ACT` / **`[Paper]` No Action Letter**,
accessions `9999999997-*`, film number `132-02319`, size 1 KB, dated **2001-12-18 → 2006-11-24**,
i.e. **zero in-window**. Saved to `sources/sec/registrant_probe/browse_edgar_CIK0000926480.html`
(15,086 B). This is the proof-of-shape that SEC paper-era filings *do* appear in the EDGAR index as
`[Paper]` accessions with no retrievable full text — so the brief's hypothesis ("Disney's 1940s
listing history may have left very early paper registered with the SEC rather than EDGAR") is
**testable in form**, and on the four CIKs reachable from this machine it returns **no 1923-1945 row**.

### 2.5 Family (a) verdict

**Returns-nothing-in-window, with a stated perimeter.** Perimeter = EDGAR electronic floor for the
ticker-resolved registrant **2018-06-25**; EDGAR full-text floor ~2001 fleet-wide (§14 rule 6);
no S-1 for any Disney registrant reachable here; pre-1994 registered paper is held in the SEC Public
Reference Room and **no script in `tools/` can reach it** (see `## Untried`, item U-6).
Bytes held from family (a): **40 documents / 25,839,637 B / 1,095,551 words**, all ≥ 2018-06-25.

---

## 3. Family-by-family verdicts, all five searched (§14 rule 6, RD-097's rule)

### (a) Filings — **returns-nothing-in-window** (perimeter above).
Command: `python tools/sec_intake.py auto --ticker DIS --company-dir founders_playbook/01_companies/company_044_disney`
plus the `submissions.csv` scan in §2.2. **Not** a null about the world: the registrant reached is the
2018 shell, and 120 in-window filings of *that* registrant are UNANSWERED (`--max-docs 40`).

### (b) Web archives — **untried**.
No script in `tools/` performs archive-wall/archive-list retrieval (grep over `tools/*.py` for
`web.archive|archive-wall|cdx` returns no route). §14 rule 6 fixes the family's floor at the
mid-1990s, so it cannot bear on 1923-1945; it *can* bear on the later stages. Command in `## Untried`.

### (c) Periodical corpora — **split verdict, and the split is the finding.**
* **Authored-but-unsent (8/8 rows UNANSWERED).** The disney block exists in `tools/queries.json` (8
  tasks) and every one of its `candidates.csv` rows is `SKIPPED: global max-requests cap 600 reached`
  (7) or `SKIPPED: hard stop: 5 consecutive failures (host halted)` (1 HathiTrust). **A query that was
  never sent is not a null.** At the *fleet-harvester* level this family is **UNTRIED**.
* **Direct Internet Archive advancedsearch, run by this probe through `tools/ia_text.py`.** Nine
  queries, each with its own return count (all `allow_insecure=True`; every fetch stamped
  `ok-INSECURE (unverified TLS: re-check before High)`):

  | query | n | in-window? |
  |---|---|---|
  | `"Walt Disney Productions" AND mediatype:texts AND YEAR:[1923 TO 1945]` | **10** | yes — 8 of the 10 carry a 1923-1945 `year` |
  | `"Disney Brothers Studio" AND mediatype:texts` | **23** | 1 (`001.-walt-disney-company`); the rest are FY1987-FY2025 annual reports and 2004-2010 Disney-licensed books |
  | `"Walt Disney, Inc." AND mediatype:texts` | **1** | undated — `gov.uscourts.dcd.250536` *ANDERSON v. WALT DISNEY INC.* |
  | `"Roy O. Disney" AND mediatype:texts` | **1** | no — `bc-1988-11-14` Broadcasting Magazine, 1988 |
  | `"Laugh-O-Gram" AND mediatype:texts` | **0** | — **a NULL over a live IA index** |
  | `(title:(Variety) OR title:("Film Daily") OR title:("Motion Picture Herald") OR title:("Exhibitors Herald")) AND "Disney" AND mediatype:texts AND YEAR:[1923 TO 1945]` | **1** | no — `MichaelEisnerAddressToVarietyAndSchroedersBigPictureConferenceVerbalSpeech_201401` (2014) |
  | `(title:(Variety) OR … ) AND "Disney" AND mediatype:texts` (unbounded) | **1** | same 2014 item |
  | `"Walt Disney Productions" AND (collection:(periodicals) OR collection:(magazine_rack)) AND YEAR:[1920 TO 1950]` | **1** | the annual-report container only |
  | `"Steamboat Willie" AND mediatype:texts AND YEAR:[1928 TO 1946]`; `"Motion Picture Herald" AND Disney AND mediatype:texts`; `"Film Daily" AND Disney AND mediatype:texts AND YEAR:[1925 TO 1946]`; `title:("Exhibitors Herald Project") AND Disney` | **0 each** | — |
* **Held Google Books bodies (bytes already on disk, so a real null is available here).**
  `grep -rli disney founders_playbook/00_universe/harvest/google_books/` → **7 XML bodies**; each
  contains **exactly 1** `disney` occurrence, all incidental BusinessWeek prose (`dc:date 1999-02-22`,
  "Home Depot ranked higher than Walt Disney"; `dc:date 1995`, "helped Disney CEO Michael Eisner take
  home $636.9 million"). **NULL for in-window on that route** — and the RD-124 class exactly: a naming
  of the *word* inside unrelated print, never Tier 1 for Disney.
* **Chronicling America — UNANSWERED, per RD-128 and per this brief's instruction.** The two CA rows
  in `candidates.csv` are `SKIPPED: global max-requests cap 600 reached` (never sent), and our CA path
  returns **404** from CI and **403** here — a wrong-path client defect whose verdict has **not landed**
  for disney (a `404` means the route was never tried, so no CA zero here may be read as absence).
  `tools/ca_endpoint_probe.py` exists (mtime 2026-09-29 23:22) but no CA response body for disney is on
  disk. **Every CA count for this company stays UNANSWERED.**
* **HathiTrust — UNANSWERED** (1 row, `SKIPPED: hard stop: 5 consecutive failures (host halted)`).

**Verdict sentence:** family (c) is **partially answered** (IA advancedsearch: 14 query shapes run, 1
in-window container returned, 4 real zeros) and **predominantly untried** (all 8 authored fleet tasks
unsent; CA, HathiTrust, Google Books-by-name, and every off-IA periodical corpus unreached).
**This is not a null and must not be recorded as one.**

### (d) Digitised corporate print / annual reports — **RETURNS IN-WINDOW TIER-1 TEXT.**
`python tools/harvest_mine.py --company disney --limit 10` printed **`{}`** and wrote **no
`research/A4_harvest_mine.md`, no `sources/harvest_mine/`** — verified by
`ls -la founders_playbook/01_companies/company_044_disney/research/`. Cause, read from the tool
(`tools/harvest_mine.py` ≈ line 344): the per-slug candidate filter is
`classification.startswith(("TIER1","LEAD"))`; all 8 disney rows are `UNANSWERED`, so `sub` is empty
and the slug `continue`s. **DEFECT D-1: a company whose candidates are all UNANSWERED silently
disappears from the run summary** — the tool prints `{}` with no `UNTRIED`/`UNANSWERED` line, unlike
its own no-directory branch (`… print("UNTRIED -- no company directory yet …` ≈ line 435). Recorded,
not worked around; it means **the family (d) result below was obtained by direct
`tools/ia_text.py` route, not by the mine.**

The item that moves this company's tier:

```
identifier 001.-walt-disney-company   "The Walt Disney Company Annual Reports"
collection   fund-and-stock-reports + periodicals + magazine_rack
item-level   date 1923-10-16 · year 1923 · addeddate/publicdate 2023-02-17
             scanner "Internet Archive HTML5 Uploader 1.7.0" · uploader wwittler@hotmail.com
files        795 entries; ~80 primary annual-report PDFs
             FY1944, 1945, 1951, 1955, 1958-1965 (unbroken), 1966-1973, 1974-1985, 1987-1989, 1991-2025
```
`python -c "import ia_text as ia,json;d=json.loads(ia.get('https://archive.org/metadata/001.-walt-disney-company',allow_insecure=True)[1]);print(len(d['files']))"`

**RD-121 applies with force here.** The item's `date`/`year` **1923-10-16 / 1923** is an
**uploader/serial artefact** — `addeddate` and `publicdate` are both `2023-02-17`, and `year=1923`
sits on a container whose earliest *document* is FY1944. It was used to **rank**, never to filter, and
it is **not** evidence of a 1923 document. Any reader who takes `year 1923` as "we hold a 1923 Disney
paper" has mis-read the field.

Held bytes fetched into `sources/corporate_print/` (nothing under `sources/` deleted or moved):

| file | bytes held | IA-reported size | sidecar |
|---|---|---|---|
| `DIS_AR_1944_walt_disney_productions_djvu.txt` | **20,634 chars** | 20,857 B (`_djvu.txt`) | `…txt.meta.json` (url, `http_status 200`, `note ok-INSECURE`, bytes_held, `ia_item`, `ia_file`, `report_year 1944`, `retrieved_at`, `retrieved_by`) |
| `DIS_AR_1945_walt_disney_productions_djvu.txt` | **3,102 chars** | 3,145 B | same schema, `report_year 1945` |

Both are the OCR text layer of `Walt Disney Company (DIS) Annual Report (1944|1945) Walt Disney
Productions[_…]`, i.e. **the registrant is printed as *Walt Disney Productions*.** The 1945 layer is
badly degraded (3,102 chars for a whole report); the 1944 layer is usable (20,634 chars).

**Naming counts in the held 1944 layer** (regex over held bytes; run
`python -c "import re;t=open('…/DIS_AR_1944_walt_disney_productions_djvu.txt',encoding='utf-8').read();…"`):
`Walt Disney Productions` **1** · `Roy O. Disney` **1** · `Disney` **7** · `Disney Brothers` **0** ·
`Laugh-O-Gram` **0** · `Ub Iwerks` **0** · `Charles Mintz` **0** · `Buena Vista` **0** · `reissue` 1 ·
`distribution` 1 · `fiscal year` 1.

What the held bytes actually say (verbatim, OCR mojibake preserved; **this is a company
self-narrative — one publisher lineage, so it corroborates nothing outside itself**):

* Opening line: `ANNUAL REPORT / For Employees / For the Fiscal Year Ended September 30, 1911`.
  **The year as OCR'd reads 1911, which cannot be the report year.** The printed year-end is
  **UNKNOWN** until the page image is read (`…_text.pdf` 2,987,018 B source PDF / `_jp2.zip` exist).
* The report's stated purpose is that "Your Labor-Management Committee … suggested this report to set
  forth clearly the plain facts about the company's affairs", and it directs employees to
  "the company's **Annual Report to Stockholders**" via "the Personnel Department, EXTENSION 871".
  → **The stockholder-facing FY1944 report is asserted by the held bytes to exist and is NOT held.**
* A chronology headed `YEARS OF PROGRESS` prints, verbatim: `Walt Disney began work in animation in
  Kansas City.` / `1923‑Walt ond Roy Disney set up shop in Hollywond.` / `1926‑Built Hyperion Avenue
  Studios.` / `1928%‑Mickey Mo… synchronized with sound. Mickey Mouse in "Steamboat Willie,"` /
  `1930‑First international distribution comtract‑comic strip started.` / `1932‑First use of
  threeeolor Technicolor in "Flowers a…` (truncated by OCR) / `…Preferred stock isswed… 1200
  employees… "Fantasia" released` / `1941‑Deeember 8 war work started -completed "Keluctant Dragon"
  and "Dumbe"‑Group to South America preliminar…` / `1944‑"Snow White" reissue‑ "The Three
  Caballeros" completed, world premiere Mexico City, December 21.` / `1M45‑Twe…`
* `DIRECTORS AND OFFICERS`: `WALTER E. DISNEY President, Director & Executive Producer`; `ROY O.
  DISNEY Executive Vice-President, Director & General Business Manager`; `GUNTHER R. LESSING
  Vice-President, Director & General Legal Counsel`; `JONATHAN B, LOVELACE Director`; `GEORGE E. JONES
  Director`; `PAUL L, PEASE Assistant Treasurer & Comptroller`; `PAUL C. SCANLON Assistant Secretary &
  Auditor`; `FRANKLIN WALDHEIM Assistant Secretary & Eastern Legal Counsel`; `Walt Disney Productions,
  2400 Alameda Ave. Burbank, California`.
* The FY1945 layer's only readable sentences: `…holders of the new secures now hove the some kind of
  ownership x the Disney family, which previously bel il he commen stock` signed `WALT DISNEY`, then
  `STATEMENT OF FINANCIAL CO…`, `CAPITAL. owe by 1700 secs of … Somber 27, 145 and repre…`,
  `…Cost~Expenses and Profit…`, `OFFICERS AND DIRECTORS`. → a **capital/ownership-distribution event
  in FY1944-45, in the registrant's own words, addressed to employees.** Values are unreadable and
  **must not** be transcribed from this layer.

**Which entity's print exists — the §15.2 sentence a tier verdict must carry.** Held in-window
corporate print exists for **`Walt Disney Productions` only (FY1944, FY1945)**. For the 1923
**Disney Brothers Studio** partnership there is **no held byte** (its name appears only as a search
term; the 23-row `"Disney Brothers Studio"` return is FY1987-FY2025 print plus licensed books), and
for the 1921-23 **Laugh-O-Gram** registrant the IA text index returns **0**. The 1928/1932
reorganisations are likewise unrepresented by any held document. **A Stage-1 tier for Disney is a tier
for the tail of the window, not for the founding act.**

### (e) Auction / museum documentary records — **untried.**
No script in `tools/` reaches an auction house, museum, or library special-collection catalogue
(`grep -rni "auction|sotheby|christie|museum|special collection" tools/*.py` hits only prose in
`tools/_tmp_b_dossier_csv_fix.py` and docstrings). Unlike most of the 50, Disney has serious archival
presence, so this family is the one whose *absence of tooling* costs this company the most; naming the
routes is therefore part of the deliverable, not filler. Commands in `## Untried`.

---

## 4. Per-stage tiers (RD-112: a tier is per stage, against that stage's own window)

**Window provenance.** Stage 1 = **1923-01-01 → 1945-12-31**, taken from `tools/harvest_mine.py`
`WINDOWS["disney"]` — the only Stage-1 boundary established anywhere in this repository for rank 44.
**Stage 2 and Stage 3 boundaries are UNKNOWN**: no dossier, volume or register for company_044 exists
yet, and the founding act itself is contested (§5). Rather than invent a boundary, the two later rows
below are measured against **the two spans our holdings actually speak to**, labelled as
*probe-proposed ranges*, not certifications. A Stage-1 author must re-cut them.

| stage | window | families returning in-window Tier-1 text | tier (§15.2) | run budget it implies |
|---|---|---|---|---|
| **Stage 1** | 1923-01-01 → 1945-12-31 (per `WINDOWS`) | **(d) only** — 2 documents, one publisher lineage. (a) nothing in-window; (b) untried; (c) 14 query shapes answered with no in-window naming beyond (d)'s own container, 8 fleet tasks unsent; (e) untried | **T3 REGISTER — PROVISIONAL** | **8k w/stage, 3-4 runs.** §K, §N, §U still mandatory at this tier |
| **Stage 2** | *probe-proposed* 1946 → 1993 (print-only era; uncut by any register) | **(d) only as measured** — FY1951, 1955, 1958-1965, 1966-1973, 1974-1985, 1987-1989, 1991-1993 locatable in the same container, **0 downloaded** | **T3 REGISTER — PROVISIONAL**, and the cheapest T2 in the corpus | T3 = 8k/3-4; if 12-15 of those layers are mined and one more family answers → **T2, 22k w/stage, 6-9 runs** |
| **Stage 3** | *probe-proposed* 1994 → 2026 (EDGAR era) | **(a) YES** — 1,141 filings enumerated, 40 docs / 25,839,637 B / 1,095,551 words held, floor 2018-06-25 (S-4); **(d) YES** — FY1994-FY2025 annual reports locatable in `001.-walt-disney-company` | **T2 CORE as measured** (2 families) | **22k w/stage, 6-9 runs**; T1 (60k, 15-20) becomes arguable only once (b) web archives is tried and the 1994-2017 filing gap is closed |

**Why Stage 1 is PROVISIONAL and not a settled T3.** §14 rule 6 forbids a depth verdict before all five
families are searched; here (b) and (e) were never reached at all, and (c)'s eight *authored* queries
were never sent. This is the Costco precedent (RD-112: "T3 **PROVISIONAL**: family (c) went untried")
one notch stronger, because here the query block **exists** and execution died on a global
max-requests cap. And it is the Walmart/Apple lesson reversed: for those two, periodicals **raised**
the tier; here periodicals are exactly the family the origin window needs and the one the machine has
never actually queried for disney.

---

## 5. Load-bearing open questions (each stated with what would settle it)

1. **The founding act and its date: 1923 vs 1928 vs 1932.** The held bytes credit **1923**, in the
   company's own voice: `1923‑Walt ond Roy Disney set up shop in Hollywond`, preceded by `Walt Disney
   began work in animation in Kansas City`. That is a **self-narrative in a 1944 employee report** —
   one lineage, dated 21 years after the event it dates. **Who is credited by which document:** the
   FY1944 report credits *Walt and Roy Disney jointly* with the 1923 act, and credits 1928 to *Mickey
   Mouse/Steamboat Willie* and 1932 to *three-colour Technicolor* — **the 1928 entry names neither Ub
   Iwerks nor Charles Mintz** (`Ub Iwerks` 0 hits, `Charles Mintz` 0 hits in the held bytes), and
   **no held document of ours names a distributor at all** (`Buena Vista` 0 hits; the only
   distribution line is the retrospective `1930‑First international distribution comtract`).
   Settled only by: a **partnership/corporation document** for Disney Brothers Studio (1923) and for
   the 1928/1932 reorganisations — family (e) or (a)-paper, both unreached.
2. **Which registrant each stage belongs to.** Measured: EDGAR carries **no registrant** named
   `Walt Disney Productions`, `Disney Brothers`, `Laugh-O-Gram` or `Buena Vista Distribution` (§2.3).
   Held in-window print exists **only** for `Walt Disney Productions` (FY1944-45). So a Stage-1
   verdict that says "Disney's founding is documented" would be false: **the registrants of 1923, 1928
   and 1932 have zero held bytes between them.**
3. **The first real experiment.** The 1944 chronology asserts a 1928 sound-synchronisation first and a
   1932 three-colour first, but both are retrospective labels in a self-narrative, and the 1932 line is
   **OCR-truncated** mid-title. Whether a contemporaneous document records an experiment (as opposed to
   a marketing claim) is **UNKNOWN**; `"Steamboat Willie" AND mediatype:texts AND YEAR:[1928 TO 1946]`
   returned **0**, so IA's text index gives us nothing contemporaneous either.
4. **The first repeatable validation.** Best in-window candidate from held bytes: `1944‑"Snow White"
   reissue` — a **reissue** is a company deciding an asset can be sold a second time, which is the
   closest thing to a repeatability signal the corpus holds; and `1930‑First international distribution
   comtract`, which is an external counterparty's willingness to pay. Both are one line each in a
   self-narrative. **No numbers are readable for either.** UNKNOWN pending the stockholder reports.
5. **The first incurred failure — expected to be distribution/receivables, not technical.** The held
   FY1945 layer describes a capital event in the registrant's own words (`holders of the new secures
   now hove the some kind of ownership x the Disney family, which previously bel il he commen stock`,
   signed `WALT DISNEY`), and the FY1944 layer prints `…Preferred stock isswed… 1200 employees…`.
   That points at a **1944-45 stock/capital re-arrangement and an employee-facing communication about
   it** — the receivables/capital leg the brief predicts, and the reason the employee report exists at
   all (a "Labor-Management Committee" report is a response to friction, and 1941-45 is the strike and
   war-production era: `1941‑Deeember 8 war work started`). But the FY1945 layer yields **no readable
   figure, no counterparty, no date** (`Somber 27, 145` is not a date I will transcribe). **The first
   incurred failure is UNKNOWN, and I refuse to date it.**
6. **The fiscal-year convention.** Printed as `For the Fiscal Year Ended September 30, 1911` in a
   document catalogued as FY1944. The month-day is plausible for the era; **the year as held is
   certainly an OCR artefact.** Whether Disney's FY ended 30 September through 1923-1945 is UNKNOWN
   and must be settled from the page image, not from this layer, because a wrong year-end silently
   mis-dates every series a later stage builds.
7. **The 1994-2017 filing hole.** Family (a)'s floor is 2018-06-25 for the only registrant this
   machine can enumerate, while the print container holds FY1994-FY2017 reports. Something filed; the
   operating registrant's CIK is unresolved here (DEFECT A-2). Stage 3's tier is hostage to that.

---

## 6. Single route most likely to change the verdict

**The stockholder-facing annual reports inside `001.-walt-disney-company` — starting with the FY1944
and FY1945 `_text.pdf` / `_jp2.zip` page layers — not more searching.** Concretely:
`https://archive.org/download/001.-walt-disney-company/Walt%20Disney%20Company%20(DIS)%20Annual%20Report%20(1944)%20Walt%20Disney%20Productions_text.pdf`
(the 1944 item has **no** `_text.pdf` in its file list, but 1945 and 1951 do — verified in the
metadata dump), plus the FY1951/1955/1958-1965 layers.

Why this route and not the periodicals, given §14 rule 6? Because it is **already held at the index
level, needs no unanswered endpoint, is entity-bearing by construction (the filename carries the
registrant name), is in-window, and is the only route that could turn questions 5 and 6 from UNKNOWN
into dated, quantified claims.** It converts family (d) from 2 degraded layers to a ~15-document
series spanning 1944-1965 — which is what makes Stage 2 the cheapest T2 in the corpus.
**The periodical block is the other half of the answer and is the bigger prize:** sending the 8
authored disney tasks would be the first time family (c) is actually queried for this company, and a
trade-press naming of the 1923 partnership or the 1932 feature decision is the only thing that can
move **Stage 1** (as opposed to Stage 2) at all. Apple (RD-097) moved a tier exactly this way.

---

## 7. What I refuse to claim

* **No founding date as fact.** 1923 is what the company's own 1944 employee report prints; I will not
  promote a self-narrative to a founding record, and the 1928/1932 alternatives are not adjudicated by
  anything on disk.
* **No `1911` fiscal year**, no `1700 secs`, no `Somber 27, 145` date, and no figure of any kind from
  the FY1945 layer. Those are OCR noise, and RD-124/§14 rule 8 forbid writing a number that the cited
  line does not cleanly print.
* **No "Disney has no pre-1945 filings."** Family (a) returned nothing *in-window for the registrant
  this machine can enumerate*, on a path that DEFECT A-2 shows is blind. That is a perimeter.
* **No null from Chronicling America or HathiTrust for this company.** RD-128: a route that 404s (or,
  here, is SKIPPED at a request cap) has never been tried. Both disney CA rows and the HathiTrust row
  are **UNANSWERED**.
* **No Tier-1 label on any of the 14 IA query returns taken as a group.** Metadata `num` is a search
  signal, not evidence (RD-121 rule 2). Only the two downloaded `_djvu.txt` layers are held bytes, and
  only they are cited above.
* **No naming-wall claim for "Disney".** Per RD-124, `disney` is a surname and a merchandising word;
  the two held layers were selected on the quoted registrant phrase `Walt Disney Productions`, and the
  BusinessWeek `disney` hits in the held Google Books bodies are explicitly **rejected** as namings of
  this registrant.
* **No Stage-2/Stage-3 boundary is certified.** Both ranges in §4 are probe-proposed; §14 forbids a
  probe inventing a stage line the corpus has not established.
* **No register, volume, census, merge-request block or certification.** A probe writes none of these.

---

## 8. Defects recorded (not worked around)

| id | defect | evidence |
|---|---|---|
| **A-1** | `sec_intake.py auto` accepts **no positional company name**; the briefed command errors `unrecognized arguments: Walt Disney` | §2.1 |
| **A-2** | `data.sec.gov/submissions/CIK*.json` → **404 NoSuchKey** for 5 registrants that `browse-edgar` shows have 13-40+ rows; `index --cik` stops there, so a live registrant reads as an empty archive | §2.4 (RD-098/RD-112 class) |
| **D-1** | `harvest_mine.py --company disney --limit 10` prints `{}` and writes **no dossier and no `sources/harvest_mine/`** when every candidate row is `UNANSWERED`; the slug `continue`s before the UNTRIED branch. Silent, and the family-(d) tier finding had to be reached outside the mine | §3(d); `tools/harvest_mine.py` ≈ L344 vs L435 |
| **C-1** | The 8 authored disney periodical tasks were never sent — 7× `SKIPPED: global max-requests cap 600 reached`, 1× `SKIPPED: hard stop: 5 consecutive failures (host halted)`. The global cap is starving individual companies | §1, §3(c) |
| **Q-1** | `001.-walt-disney-company` carries `year 1923` / `date 1923-10-16` on a container whose earliest document is FY1944, **and** `ocr_detected_script "Arabic"` + `page_number_confidence 0` + `pdf_degraded invalid-jp2-headers`. RD-121's scan-year field, plus a whole-item OCR-quality warning that must travel with every quotation from these layers | §3(d) |
| — | `sec_intake.py selftest` **42 checks, 0 failing**; `auto` identity `40+1+0 = 41 vs 41 -> OK`; `nameless_rows 0`. No intake defect beyond A-1/A-2 | §2.2 |

---

## 9. `## Untried`

Each item is a search never run, with the command that would run it. Nothing here is a null.

1. **Family (c), all 8 authored disney periodical tasks — the single highest-value execution gap.**
   `python tools/periodical_harvest.py --company disney --max-requests 200 --insecure`
   (then: `python tools/harvest_mine.py --company disney --limit 10 --min-year 1923-01-01 --max-year 1945-12-31`)
2. **Family (c), trade press by corpus-scoped query rather than IA `title:` field** (my 4 shapes
   returned 0-1 and are *not* the family's answer):
   `python tools/periodical_harvest.py --company disney --source-family internet_archive --max-requests 120 --insecure`
3. **Family (c), HathiTrust** (1 row, host-halted): `python tools/periodical_harvest.py --company disney --source-family hathitrust --max-requests 60 --insecure`
4. **Family (c), Google Books by registrant phrase** (the 7 held bodies are BusinessWeek prose, not a
   Disney query): `python tools/periodical_harvest.py --company disney --source-family google_books --max-requests 60 --insecure`
5. **Family (c), Chronicling America — held at UNANSWERED until RD-128's path verdict lands.**
   Run the wired probe first: `python tools/ca_endpoint_probe.py`
   ; only after it reports a working shape: `python tools/periodical_harvest.py --company disney --source-family chronicling_america --max-requests 120`
6. **Family (a), SEC paper-era registered records for 1923-1945** (no script reaches them;
   `tools/` has no Public-Reference / `[Paper]`-accession route): record as
   `FETCH REQUEST:` — enumerated `browse-edgar` action=getcompany&CIK=0000029082|0000926480|0001004224&type=S-1&count=100 oldest-first, plus SEC industry-index 7812 filings 1934-1945. **Declining the fetch is correct behaviour (§15.1).**
7. **Family (a), the operating registrant that filed FY1994-FY2017 print** (DEFECT A-2 blocks it):
   `python tools/sec_intake.py index --cik 29082 --company-dir founders_playbook/01_companies/company_044_disney`
   once the `data.sec.gov` 404 has a `browse-edgar` fallback.
8. **Family (d), the rest of the held container** — the stockholder-facing layers and the FY1951-1965
   series: `python tools/ia_text.py fetch --insecure --company-dir founders_playbook/01_companies/company_044_disney --id 001.-walt-disney-company --pattern "Disney" --max-mb 20`
   (per-file `…_text.pdf` layers must be pulled by filename via `ia_text.ocr_url`; the item-level
   `…_djvu.txt` is the *wrong* text layer for a multi-report container — that is why the 1944/1945
   pulls in §3(d) used `ocr_url(ident, fname)`. Add a `--file` option to `ia_text fetch` rather than
   re-improvising.)
9. **Family (d), the FY1944 page image** — the only way to settle the fiscal year and read figures:
   `python tools/ia_text.py fetch --insecure --company-dir founders_playbook/01_companies/company_044_disney --id 001.-walt-disney-company --max-mb 12`
   (the FY1944 `_text.pdf` is **absent** from the file list; `_jp2.zip` 2,978,742 B and the source PDF
   2,987,018 B are present).
10. **Family (b), web archives** — no tool exists; §14 rule 6 floors the family at ~mid-1990s, so it
    bears on Stage 3 only. `FETCH REQUEST:` for an archive-list route in `tools/`.
11. **Family (e), auction / museum / library special collections** — no tool exists; Disney is the
    company in the 50 for which this hurts most. `FETCH REQUEST:` for (i) Library of Congress
    Motion Picture, Broadcasting & Recorded Sound Division collection search; (ii) the Walt Disney
    Archives / California State Library, North Hollywood `disneyparks`/`ucla` finding aids; (iii) an
    animation-estate documentary-sale calendar. Each reachable as an HTML catalogue the existing
    `sec_intake.http_get`/`ia_text.get` plumbing could carry with a sidecar. **Until a script exists
    this stays UNTRIED, not absent.**
12. **`00_universe/harvest/_probe_fixed_20260925/` HathiTrust bodies** — held bytes never read for any
    Disney phrase: `python -c "import glob,re;[print(p,len(re.findall('Disney',open(p,encoding='utf-8',errors='replace').read(),re.I))) for p in glob.glob('founders_playbook/00_universe/harvest/_probe_fixed_20260925/**/*.htm*',recursive=True)]"`

---

## 10. Close-out accounting (§14 rule 11: sources re-enumerated at close)

`find founders_playbook/01_companies/company_044_disney/sources -type f | wc -l` and the per-family
tally are reproduced by:

```
python - << 'PY'
import os
b='founders_playbook/01_companies/company_044_disney/sources'
for d in sorted(os.listdir(b)):
    p=os.path.join(b,d)
    if os.path.isdir(p):
        fs=[f for f in os.listdir(p) if os.path.isfile(os.path.join(p,f))]
        print(d, len(fs), sum(os.path.getsize(os.path.join(p,f)) for f in fs), 'B')
PY
```

Measured at close (command above, `os.walk` variant):

| folder | files | bytes |
|---|---|---|
| `sources/_index` | 7 | 668,740 B |
| `sources/corporate_print` | 4 | 26,188 B |
| `sources/sec` (+ `registrant_probe` 1 / 15,086 B, `registrar_search` 1 / 7,606 B) | 87 | 25,883,620 B (+22,692 B) |
| **TOTAL under `sources/`** | **98 files** | **26,601,240 B** |

`corporate_print` holds exactly the 4 artefacts this probe added:
`DIS_AR_1944_walt_disney_productions_djvu.txt` **21,739 B on disk / 20,634 chars read** (the mojibake
makes bytes > chars; IA-reported `_djvu.txt` size 20,857 B) + its `.meta.json` (562 B), and
`DIS_AR_1945_walt_disney_productions_djvu.txt` **3,326 B / 3,102 chars** + its `.meta.json`.

Everything new under `sources/` this pass arrived from this probe and is named above: `sec/`
(EDGAR intake + `registrar_search/` + `registrant_probe/`), `corporate_print/` (2 report layers + 2
sidecars), `_index/` (registrant-keyed). **Nothing under `sources/` was deleted, moved or pruned**;
`tools/`, `MASTER_RESEARCH_LOG.md` and every other company directory were left untouched; no git
command was run; **0 WebSearch / 0 WebFetch**.

**Unexamined, stated plainly.** Not read: the 40 held EDGAR documents (all ≥2018, none in Stage 1);
the FY1944 source PDF and `_jp2.zip`; every report from FY1951 onward in the container; the
`_probe_fixed_20260925/` HathiTrust bodies; `tools/periodical_harvest.py`'s per-family internals;
`RESUME_HANDOFF.md`; the other 49 companies.
