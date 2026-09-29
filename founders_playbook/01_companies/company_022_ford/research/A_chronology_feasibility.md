# A_chronology_feasibility.md — FORD MOTOR (company_022_ford, rank 22), Stage-1 PROBE

Owner: `probe-ford` (claimed via `python tools/scaffold.py claim --path founders_playbook/01_companies/company_022_ford/research/A_chronology_feasibility.md --agent probe-ford`).
Origin window per the brief: **1903-01-01 → 1945-12-31**. Stage windows used for tiering (brief-assigned):
**Stage 1 = 1903-01-01 → 1918-12-31**, **Stage 2 = 1919-01-01 → 1945-12-31**.
Web budget this pass: **0 WebSearch, 0 WebFetch.** All bytes below were reached through `tools/sec_intake.py`,
`tools/ia_text.py`, `tools/harvest_mine.py` and read locally. `tools/periodical_harvest.py` was NOT run (live
merges on `candidates.csv`); every family it owns is reported UNTRIED, never null.

Confidence cap notice: **every Internet Archive layer in `sources/corporate_print/` and `sources/periodicals/`
carries the sidecar line `transport = UNVERIFIED TLS -- re-check before citing at High confidence`**
(command: `python -c "import json,glob;[print(f, json.load(open(f)).get('transport')) for f in glob.glob('founders_playbook/01_companies/company_022_ford/sources/*/*.meta.json')]"`).
Therefore **no IA-held byte is cited above Medium on this pass.** EDGAR sidecars record `http_status: 200`
through verified TLS (`sources/sec/*.meta.json`), so filings are not capped by transport — only by the §3
filing-lineage rule.

---

## 0. Measured state at probe start (verified, not inherited)

| item | measured | command |
|---|---|---|
| company dir | `founders_playbook/01_companies/company_022_ford` | `ls founders_playbook/01_companies \| grep ford` |
| files under `sources/` before this pass | 22 (17 text layers + sidecars + `_index.json`) | `find <dir> -type f \| wc -l` |
| harvest-mine dossier present at start | `research/A4_harvest_mine.md`, 6 items mined, all `TIER1_CANDIDATE_TEXT` on `ford motor` | Read |
| `candidates.csv` Ford rows | **124** — `corporate_print` 62, `internet_archive` 39, `google_books` 18, `chronicling_america` 4, `hathitrust` 1 | `python -c "import csv;rows=[r for r in csv.DictReader(open('founders_playbook/00_universe/harvest/candidates.csv',encoding='utf-8-sig')) if r['company']=='ford'];print(len(rows))"` |
| header enumerated before any field was read | `company, source_family, query, item_id, title, date_or_issue, url, snippet_or_hitcount, http_status, classification, retrieved_at` | `python -c "import csv;print(list(csv.DictReader(open('founders_playbook/00_universe/harvest/candidates.csv',encoding='utf-8-sig')).__iter__().__next__().keys()))"` |
| Ford query blocks in `tools/queries.json` | **8 tasks** (2 chronicling_america, 2 internet_archive, 1 hathitrust, 1 google_books, 2 corporate_print) — so family (c) was *queried*, which per RD-112 means it is not "untried-for-want-of-a-block", only unrun/blocked | `python -c "import json;t=json.load(open('tools/queries.json',encoding='utf-8'))['tasks'];print(len([x for x in t if x.get('company')=='ford']))"` |
| no `web_archive` family task exists | 0 rows for ford under any `web_archive` `source_family` (families above are the only ones present) | same `candidates.csv` filter, `Counter(r['source_family'])` |

**Window discrepancy, recorded not resolved.** The brief states the origin window as `1903-01-01 -> 1945-12-31`;
`tools/harvest_mine.py` WINDOWS line 59 reads `"ford": ("1903-01-01", "1950-12-31")`, and the harvester's own
dossier prints 1903-01-01..1950-12-31 (command: `grep -n '"ford"' tools/harvest_mine.py`). Three held layers
(1948, 1949, 1950) sit **inside the tool's window and outside the brief's Stage-2 window**. They are listed
below as `1946+` and excluded from Stage-2 tier counting. This is RD-131's "check the measurement, not the
assumption"; the orchestrator must set the ceiling, not this probe.

---

## 1. What is in-window and held (opened, with line numbers)

Held corpus after this pass: **535,608 unique bytes** across 24 distinct text layers
(command: `python -c "import glob,os;d={os.path.basename(f):f for f in glob.glob('founders_playbook/01_companies/company_022_ford/sources/*/_djvu.txt')+glob.glob('founders_playbook/01_companies/company_022_ford/sources/*/*_djvu.txt')};print(len(d),sum(os.path.getsize(v) for v in d.values()))"`).
Two sub-corpora, and **they name different legal persons.**

### 1.1 The McGill layers name the Canadian company, not the registrant — 16 layers, 200,350 B

`McGillLibrary-6355xx` items on disk (16 distinct identifiers; 4 duplicated across `corporate_print/` and
`periodicals/`): 635585, 635589, 635590, 635591, 635593, 635594, 635595, 635596, 635598, 635602, 635605,
635607, 635608, 635611, 635612, 635613. Every one is headed

* `sources/periodicals/McGillLibrary-635602-36479_djvu.txt` **l.1** `FORD MOTOR COMPANY OF CANADA,` ·
  **l.3** `[Incorporated under the Dominion Companies Act]` · **l.4** `WINDSOR ... ONTARIO` · **l.28**
  `FORD MOTOR COMPANY OF CANADA, LIMITED`
* `sources/periodicals/McGillLibrary-635608-36497_djvu.txt` **l.4**, **l.18**, **l.29** same entity; **l.21-22**
  `NOTICE OF ANNUAL MEETING / April 12th, 1945`; **l.31** meeting "at the head office of the Company, at
  Windsor, Ontario, on the 30th day of April, 1945"; **l.43-46** "Only registered owners of class 'B' shares are
  entitled to vote."

Term census over all held IA bytes (command:
`python - <<'EOF'` glob+regex count, printed in this pass):

| string | occurrences in held IA layers |
|---|---|
| `Ford Motor Company of Canada` | 64 |
| `Ford Motor Company` (all forms) | 74 |
| `Ford Motor Car Company` | **0** |
| `Henry Ford Company` | **0** |
| `Dockwether` | **0** |
| `Cadillac` / `Cadiac` | **0** / **0** |
| `Muddison` | **0** |
| `Dodge` | **0** |
| `Dearborn` / `Michigan` (in the 1920-1944 layers) | 0 / 0 (the 1950 layer carries both — see 1.4) |
| `1903` / `1902` / `1901` / `1899` / `1908` | **0 / 0 / 0 / 0 / 0** |
| `Model T` / `moving line` / `assembly line` | **0 / 0 / 0** |
| `consent decree` / `Decree` / `anti-trust` | **0 / 0 / 0** |

The only persons named are **Henry Ford** and **Edsel B. Ford** in *Canadian* board roles, and they are named as
officers of the Canadian company, not as founders of anything:

* 635585 (fiscal year ending **July 31st, 1920**; l.18-25) **l.42** `HENRY FORD, President`, **l.46**
  `EDSEL B. FORD, Third Vice-President`; **l.130-136** Balance July 31 1919 `5,270,061.48`, Dividends `1,750,000.00`,
  `Capital Stock Issued 7,000,000.00`; **l.201-202** "Sales for the year covered **55,616 cars**, including all
  models exclusive of Tractors, as against 39,112"; **l.205** "For the season of 1920-21 we are planning to
  produce **75,000 cars**"; **l.218-219** "There are eight branches … the Saskatoon Branch having been
  transferred to Regina"; auditors' certificate dated **l.113** `September 18th, 1920`.
* 635591 (year ended **December 31st, 1927**) **l.17** `YEAR ENDED DECEMBER 3ist, 1927`, **l.17-21**
  `EDSEL B. FORD, President`, `W. R. CAMPBELL, Vice-President`, `HENRY FORD` listed among directors.
  Combined with 635589/635590 (July-31 years 1925 and 1926, l.37-40 and l.28-31: Henry Ford President,
  Edsel Second Vice-President), the held run shows the **Canadian** presidency moving Henry Ford → Edsel B. Ford
  between FY1926 and FY1927, and the **Canadian fiscal year moving from July 31 to December 31 between 1926 and
  1927** — an accounting-basis change inside Stage 2, evidenced, not inferred.
* 635593 (1929) **l.295**: "By-law No. 2 at the Special General and Annual Meeting held March 26th, 1929,
  **Supplementary Letters Patent were granted amending the capital structure of the Company**" — the only
  corporate-act language in any held layer, and it is the Canadian company's own.
* 635607 (year ended December 31st, 1943) **l.422-424**: "the Directors record the death of **Mr. Edsel B. Ford on
  May 26th, 1943**. Mr. Ford became a Director and Vice-President of the Company on **October 31st, 1919**, was
  elected President on December 12th, 1927 …". This is Edsel Ford's only in-window appearance, and it is as an
  officer of the **Canadian** company. Bare `Edsel Ford` occurs **0** times in the stored EDGAR bytes; `Edsel B.
  Ford II` (a different, later person) occurs **81** times in 17 of 33 stored filings.

### 1.2 The contested founding names are absent from every held byte, EDGAR included

Command: `python -` regex census over `sources/sec/*` (33 stored docs) and over the IA layers, both printed this
pass. `Dodge` = **0** in EDGAR; `Dockwether|Piquette|Cadillac|Dodge Brother|Muddison` = **0** in EDGAR and **0** in
IA. `consent decree` in EDGAR = 2 hits, both modern (`0000037996-00-000019_...txt` l.1740 — a DOJ/EPA Econoline
decree; `0000037996-99-000009_...txt` l.1923 — an OFCCP "partial consent decree"). **The 1919 consent decree has
no carrier in this corpus.**

### 1.3 The registrant's own founding sentence IS held — and it names two entities and two dates

Found in the stored EDGAR bytes (`sources/sec/`), the identical corporate self-narrative:

> "Ford was incorporated in Delaware in 1919 and acquired the business of a Michigan company, also known as Ford
> Motor Company, incorporated in 1903 to produce automobiles designed and engineered by Henry Ford."

Carriers, with line numbers (same sentence, four accessions, one lineage per §3):

| file:line | instrument (from `sources/_index/_INDEX_CIK0000037996.md`) |
|---|---|
| `sources/sec/0000950124-95-002993_0000950124-95-002993.txt` **l.704-706** and **l.1999-2001** | S-4, filed 1995-09-19 |
| `sources/sec/0000950124-95-003444_...txt` (2 occurrences) | S-4/A, filed 1995-10-27 |
| `sources/sec/0000950124-95-003512_...txt` (2 occurrences) | 424B3, filed 1995-11-13 |
| `sources/sec/0000950124-00-003950_ex99-2.txt` (2 occurrences) | exhibit to a 2000 accession |
| `sources/sec/0000037996-94-000005_...txt` **l.177-178** | 10-K, filed 1994-03-21 |
| `sources/sec/0000037996-96-000007_...txt` **l.193** | 10-K405, filed 1996-03-19 |
| `sources/sec/0000037996-00-000019_...txt` **l.187-188** | 10-K, filed 2000 — variant wording: "Ford Motor Company was incorporated in Delaware in 1919. **We acquired the business of a Michigan company**, also known as Ford Motor Company, incorporated in 1903 to produce **and sell** automobiles …" |

Counts (same command as §1.2): `incorporated in Delaware in 1919` **15 occurrences / 11 of 33 stored docs**;
`incorporated in 1903` **14 / 10 docs**; `Michigan company` **16 / 12 docs**; `Henry Ford` **25 / 15 docs**.
Registrant metadata everywhere: `Delaware`, IRS EIN `38-0549190`, `One American Road / The American Road,
Dearborn, Michigan` (e.g. `0000037996-94-000005_...txt` header block; 204 `Dearborn` hits in stored EDGAR bytes).

**What that settles and what it does not.** It gives Stage 1/Stage 2 a dated Tier-1 *carrier* for the founding
claim, and it settles the entity question in the direction the brief predicted: **the registrant is the 1919
Delaware corporation; the 1903 Michigan company is a predecessor whose business was acquired.** It does not
supply a 1903 document, a 1919 document, the New Jersey antecedent, the Dodge-buyout, or the consent decree, and
it is a **76-to-97-year-late company self-narrative** (`RETROSPECTIVE SOURCE`, §6). One lineage, so §3 caps it:
corroboration count = 1, not 11.

### 1.4 Company-authored US print, in-window for Stage 1, reached this pass (all UNVERIFIED TLS)

Fetched by `python tools/ia_text.py mine --q '"Ford Motor Company" (Detroit OR Dearborn OR automobile) AND mediatype:texts AND YEAR:[1903 TO 1918]' --rows 8 --pattern "Ford Motor Compan" --company-dir <dir> --insecure`
→ search reported **numFound = 42**, page returned 8, and the run printed "**8 items: 4 TIER1_CANDIDATE, 3
NULL/LEAD, 1 UNANSWERED — UNANSWERED items are NOT evidence of absence**". 34 of 42 were never attempted
(`--rows 8`), so family (d)/(c) depth here is a page, not a census.

* **`sources/periodicals/ford-manual-1914_djvu.txt`** — 123,897 B, 5,494 lines. Title page **l.53** "of Ford
  Cars", **l.60**, **l.66** `Ford Motor Company`, **l.68** `Detroit, Michigan, U. S. A.`, **l.70** `1914`;
  **l.102** "six thousand Ford service stations distributed". Company-authored, in-window (Stage 1), and it names
  the **US** entity with its city. `incorporat`/`1903` = 0 hits in this file.
* **`sources/periodicals/fordmotorcoprofitsharing_djvu.txt`** — 47,093 B, 1,650 lines. **l.52-54** `FORD MOTOR
  COMPANY / DETROIT MICHIGAN U.S.A`; **l.92** "The day shift at the Ford Motor Company"; **l.103** "T HE plan of
  the Ford Motor Company, in increasing the income of its employes above the regular going wage"; **l.115** "The
  Company has organized a staff of men, whose"; **l.257-260** "All persons employed on or after **October 23rd,
  1914**, will not be permitted to share in profits until they have been in the Company's employ six months";
  **l.301** "The Ford Motor Company hopes through its profit-sharing"; **l.822-823** "home **before the
  inauguration of the profit-sharing plan, January 12th, 1914**"; **l.839-840** "The same employe's present
  quarters, **fourteen months after** receiving a share of the profits"; **l.973-982** "a 'Ford Profit-Sharer'
  may, at the age of 50, retire from active work and continue to receive **$5.00 per day** … which, with his
  daily wage, pays him $5.00 per day. $50.00 per month was banked for the first 4 years …".
* Two further IA copies of the **same work**: `helpfulhintsadvi1915ford_djvu.txt` (54,244 B) and
  `helpfulhintsadvi0000ford_djvu.txt` (55,055 B). These are **one source, not three** (§3 filing-lineage rule).
  The 1915 copies carry the anniversary table the first copy's tail lacks:
  **l.1403-1405** "**Records compiled January 12th, 1915, just one year after the Profit-sharing Plan was
  inaugurated**, give some very interesting figures"; **l.1410-1424** a January-1914 vs January-1915 comparison
  (`Number of Employes 13,251 → 14,255`; `Amount in Banks $990,418.00 → $3,040,301.00`; `Total Amount of Life
  Insurance 2,471,003.00 → 0,493,709.00` — the second value is an OCR drop of a leading digit and must NOT be
  footed; `Total Value of Homes Owned 408,230.00 → 933,524.00`; `Homes on Contract 3,282,311.00 → 8,807,159.00`);
  **l.1434-1437** "In January 1915, **3,531, or 25% of the men employed**, were new men, most of whom had been out
  of work a long time, and had not yet served their six months probationary period, in order to qualify for a
  share of the profits."
  `helpfulhintsadvi0000ford_djvu.txt` **l.11** `1915`; **l.424** "**Americanization Day, July 5th, 1915.** The
  parade of **6000 Ford employes** through Campus Martins, Detroit".
* **`sources/periodicals/FordMotorCompanyInstallssiroccoHeatingVentilatingAndCoolingSystem_djvu.txt`** — 16,338 B
  (third-party trade pamphlet, not company print). **l.99** "Ford Plant"; **l.104** "branch Canadian plants of the
  Ford Motor Co."; **l.121** "It is well known that the Ford plant at Detroit is the largest"; **l.314-315**
  "machinery would never have turned out a Ford car a minute — yes, and **a Ford car every 45 seconds — nearly
  1500 automobiles**"; **l.1456** `DETROIT`. A byte-identical 16,338 B copy sits under
  `..._541_djvu.txt`. **Its date is contested by our own metadata:** `candidates.csv`/IA catalogue fields give
  one copy **1914** and the other **1904** while the layers carry no printed imprint date, and the 45-seconds /
  1,500-a-day throughput claim is not compatible with 1904. **Publication date UNKNOWN; do not cite as 1904.**
* `sources/periodicals/3282_SWODA_djvu.txt` — **77 B**, one caption line: "A 6,000 HORSE POWER GAS-STEAM ENGINE.
  THERE ARE SEVEN OF THESE AT FORD S." A caption, not a document; recorded as a lead only.
* `sources/periodicals/cihm_90487_djvu.txt` — 22,216 B, a 1917 CIHM microform "Ford manual"; **0** lines matching
  `Ford Motor Comp`. NULL on this registrant's naming, at this pattern only.
* **1946+ (inside the tool window, outside Stage 2 by the brief):** `McGillLibrary-635612-36512_djvu.txt` (year
  ended December 31st 1949, 35,191 B) **l.1083-1085**: "Effective May 1st, 1949, a new relationship agreement
  replaced that which had been in effect between Ford of Canada and **the Ford Motor Company of the United States**
  since **the original incorporation of the Canadian company in 1904**"; **l.1089** "over the preceding 45 years";
  **l.455-462** "In 1919 Ford of Canada had **2,869 employees**, the average hourly rate was **71½¢** … In 1949
  Ford of Canada had **14,257 employees**, the average hourly rate was **$1.29**".
  `McGillLibrary-635613-36515_djvu.txt` (1950, 29,511 B) **l.273** "53 vehicles from **Ford Motor Company,
  Dearborn**"; **l.959** "Mr. D. S. Harder, Vice President–Manufacturing, **Ford Motor Company, Dearborn,
  Michigan**"; **l.336** "first came to work in the machine shop in the spring of 1919".
  These two are the **only held IA lines that name the US parent as a separate legal person with a town** — and
  they are outside the Stage-2 window as briefed.

### 1.5 Stage-2 (1919-1945) held Canadian layers, opened — the only in-window narrative material

* 635595 (year ended December 31st, **1931**, 6,146 B — **held in `corporate_print/` only and never mined by
  `harvest_mine.py`; the harvester's table omits it**, so nothing before this pass had read it): **l.4**
  `East Windsor, Ontario`; **l.30** `EDSEL B. FORD, Chairman of the Board`; **l.32** `HENRY FORD` (director);
  **l.61-69** "Net loss from the operations of the Canadian Factory and Branches for the year ended December 31st,
  1931 after all charges for manufacturing, selling and … expenses including depreciation : **$1,668,630.21**;
  Less: Dividends Received from Affiliated Companies 283,873.02 — **1,384,757.19**"; **l.196-197** output
  "30,890 units"; **l.234-239** "the first semi-annual dividend … $0.60 per share was paid … June 20th, 1931.
  Inasmuch as the operations of the Company were adversely affected as a result of prevailing world conditions,
  **it was not considered advisable to make a further dividend distribution during the year**"; **l.151-157**
  capital stock authorized 1,900,000 Class "A" + 100,000 Class "B", issued 1,588,960 A + 70,000 B; **l.123-124**
  auditors "Ford Motor Company of Canada, Limited"; dated **l.256** "April 5th, 1932".
* 635596 (1932, 5,352 B): **l.64-70** net loss from operations **$5,206,736.59**; **l.207** output 25,218 units;
  **l.123-124** audited sentence; **l.256** "April 3rd, 1933".
* 635598 (1934, 9,659 B): entity head l.7/29/56; **l.465** "in the Statement of Earned Surplus incorporated in the
  Annual" — the only occurrence of `incorporated` besides 635602 l.3.
* 635602 (1938, 9,512 B): **l.3** the Dominion Companies Act line; **l.399-401** "investment in shares of **Ford
  Motor Company of India, Limited**, now amounts to $1,434,364.89 and in **Ford Motor Company of Malaya, Limited**,
  $418,848.30"; **l.388-392** "tools pertaining to 1939 models … charged against operations in 1939".
* 635605 (**1941**, 18,359 B): **l.218** "Reduction in contract prices of vehicles sold to His Majesty['s]
  Government"; **l.475** contract with "Majesty's Government in the United Kingdom"; **l.484**, **l.580** "War
  Contracts Depreciation Board"; **l.520** "the costs of material and labour in 1941 models for the domestic";
  **l.529** "used for production for war purposes"; **l.552-553** "To assist in the fulfilment of government
  contracts, advances have been made by the government"; **l.588** "Canadian Government additional machinery and
  equipment".
* 635608 (**1944**, 14,069 B): **l.525** "Net profit for the year was $3,144,516, equivalent to $1.89 per share
  and 2 per cent of the total volume of sales"; **l.531-538** "The aggregate value of products shipped during 1944
  was $157,339,425, being $24,044,345 less than in 1943. **This reduction in output was attributable to a
  work-stoppage of three weeks' duration in the early part of 1944 as the result of a strike by employees**; also
  to suspension of operations for one week … and to the continuation in 1944 of the lower schedule of production
  established about midyear in 1943 **owing to scarcity of labour**"; **l.541-542** "Automotive units shipped
  during the year totalled 65,528 in comparison with 79,602"; **l.563-564** "a Finding and Direction of the
  **National War Labour Board** in respect of services performed in 1943"; **l.572-577** excess-profits-tax
  adjustment against the 1936-1939 standard period; **l.594-596** "Advances from the **Dominion Government** were
  $7,124,029 lower".

**Read §1.5 as the register must.** Every number above is a **Ford Motor Company of Canada, Limited** number.
None of them is a US-registrant Stage-2 metric, and the 1944 three-week strike is **not** Ford Motor Company's
"first incurred operational failure" — it is the Canadian subsidiary's. Writing it into the registrant's chronology
would be the Kroger Great-Western-Tea / Boeing-1916 error run backwards.

---

## 2. The five family verdicts (stated as returns, never as hopes)

Verdict vocabulary: **RETURNS** / **RETURNS-NOTHING-WITH-PERIMETER** / **UNANSWERED** / **UNTRIED** (RD-097: an
untried family is UNTRIED, never a null; RD-130: a year-faceted zero is about our parameter).

### (a) Filings — `RETURNS (a founding sentence) / RETURNS-NOTHING-WITH-PERIMETER (any in-window record)`

`python tools/sec_intake.py auto "Ford Motor" --company-dir <dir>` resolved identity cleanly — "identity: 'Ford
Motor' resolved to CIK 37996 (FORD MOTOR CO) by name-exact", registrant guard `ok` — enumerated **4,445 filings**,
and stored **33 documents / 8,386,844 B / 986,660 words**, with **8 UNANSWERED** (each a `NoSuchKey` 404 on three
path forms, recorded as UNANSWERED, not NULL), **140 SKIPPED** past `--max-docs 40`, and the tool's own line:
"**595 in-window filings were never listed because --max-docs 40 was reached**". Identity arithmetic printed
`stored(33) + unanswered(8) + skipped(140) = 181 vs attempted(181) -> OK`.
**Perimeter:** earliest indexed `filingDate` is **1994-01-20** (SC 13D/A); `10-K` floor 1994-03-21. Command
`python -c "import csv;rows=list(csv.DictReader(open('<dir>/sources/_index/submissions_CIK0000037996.csv',encoding='utf-8-sig')));print(len(rows),min(r['filingDate'] for r in rows));print(sum(1 for r in rows if r['filingDate'][:4].isdigit() and 1903<=int(r['filingDate'][:4])<=1945))"`
→ `4445 1994-01-20 0`. So **zero filings exist in either stage window**, and nothing in family (a) can date a
Stage-1 or Stage-2 event; what it can do is carry the registrant's own founding sentence (§1.3).
Note the tool's own default: `--from 1900-01-01 --to 2030-12-31` (`tools/sec_intake.py` l.1193-1194), so "618
accessions in window" is **that** window, not the origin window — a phrase a later agent must not inherit.

### (b) Web archives — `UNTRIED`

No scripted route exists (`tools/` holds no CDX/Wayback tool; `queries.json` carries no `web_archive` task for
ford; `candidates.csv` has no `web_archive` row for ford — commands in §0). Structurally this family cannot reach
1903-1945 (fleet floor mid-1990s, §14.6), but "cannot reach" is a reason to record UNTRIED, not to record a null.
Command in `## Untried`.

### (c) Periodical corpora — `UNANSWERED` for every route that would carry pre-1919 print; `UNTRIED` for the
pages that were never opened

Rows and states, from `candidates.csv` (header enumerated in §0):

| route | Ford rows | state |
|---|---|---|
| `chronicling_america` | 4 | 2 `UNANSWERED` (blank `http_status`) + 2 `ERROR`/`404` → **UNANSWERED, never NULL**; queries were `CA 'Ford Motor' Dearborn Detroit Michigan 1900-1960` ×2 and `CA 'Ford Motor Car Company' Michigan 1900-1930 (NAME-VARIANT HYPOTHESIS)` ×2 |
| `hathitrust` | 1 | `UNANSWERED`, blank `http_status`; query `HT 'Ford Motor Company' Dearborn automobile` |
| `google_books` | 18 | 200-status metadata rows only, dated years `1922, 1925, 1971, 1975, 1985, 1988, 1995, 2005, 2006, 2012, 2014, 2016, 2020` + one blank; the feeds endpoint returns no snippet text → **text UNTRIED** |
| `internet_archive` | 39 | metadata leads only until this pass; `mine` reached 8 of **numFound 42** in-window items and fetched them |

`tools/periodical_harvest.py` — the script that would run the CA/HT/GB bodies — **was not run by order** (it races
live merges on `candidates.csv`). So the whole periodical-text block is **UNTRIED-BY-ORDER**, and the RD-127
lesson was checked rather than inherited: `00_universe/harvest/_probe_fixed_20260925/` **does** hold HathiTrust,
Chronicling America, Google Books and internet_archive bodies (plus `_RECORDS.tsv`, 363 record blocks), but every
sidecar in `hathitrust/` attributes its body to a **Walmart** query
(`q1=%22Wal-Mart%22 Bentonville`, `q1="five and dime" variety store`) — command:
`python -c "import json,glob;[print(json.load(open(f))['url'][:150]) for f in sorted(glob.glob('founders_playbook/00_universe/harvest/_probe_fixed_20260925/hathitrust/*.meta.json'))[:6]]"`.
A `grep -ci ford` over `hathitrust/_RECORDS.tsv` returns **2**, and both are substring matches inside unrelated
titles (no Ford query, no Ford record); `_REQUEST_LEDGER.tsv` returns **0**. So **no Ford full-text body exists in
this repository** — which is an untried route, not a null.

### (d) Digitised annual reports / corporate print — `RETURNS`, with the entity caveat as the finding

Two distinct sub-corpora on disk:
1. **16 McGill layers, 200,350 B, all Ford Motor Company of Canada, Limited, 1920-1950** (years held: 1920, 1925,
   1926, 1927, 1929, 1930, 1931, 1932, 1934, 1938, 1941, 1943, 1944, 1948, 1949, 1950). Confirmed by
   `python tools/harvest_mine.py --company ford --limit 12 --insecure` →
   `{"ford": {"window": ["1903-01-01","1950-12-31"], "candidates": 118, "mined": 12, "bytes": 156878, "entity_naming": 12, "variant_term": 0, "bare_word_only": 0, "null": 0, "unanswered": 0}}`.
   **Every one of the 12 is the Canadian company.** The candidate pool behind them is 62 `corporate_print` rows and
   **62 of 62 carry `Canada` in the title** (command and full year list in §6.1 below) — the digitised bound run
   that flipped Walmart, Target, Boeing and Kroger is, for Ford, a run of **the wrong legal person**, and it does
   not reach back before 1920.
2. **US-entity company print, in-window Stage 1:** the 1914 Ford Manual (123,897 B), three copies of the 1915
   profit-sharing pamphlet (47,093 + 54,244 + 55,055 B), the Sirocco trade pamphlet (16,338 B ×2, date contested).
   This is where the registrant's own founding decade finally has a carrier — but it carries the **$5/profit-sharing
   plan and the product**, not the incorporation.

### (e) Auction / museum documentary sale records — `UNTRIED`

No script reaches them and the web budget is 0. The Apple precedent (surviving founding documents at auction) and
the brief's warning (§14.6) both say this family is not to be counted as a null. Command in `## Untried`.

---

## 3. Per-stage tiers (§15.2), measured against each stage's own window (RD-112)

| stage | window used | families returning **in-window Tier-1 text naming an entity that the stage is about** | tier | §15.2 deliverable / cap | ≈ runs |
|---|---|---|---|---|---|
| **1 — origin** | 1903-01-01 → **1918-12-31** | **one**: (d) US company-authored print held in-window — 1914 Ford Manual, 1915 profit-sharing pamphlet (×3 copies, one lineage), contested-date Sirocco pamphlet. (a) answered but out-of-window (floor 1994-01-20); (b) UNTRIED; (c) UNANSWERED (CA/HT/GB) + UNTRIED pages; (e) UNTRIED. The 16 McGill layers do **not** count here: the earliest is FY1920 | **T3 register — PROVISIONAL** | short narrative + registers; §K, §N, §U mandatory; **8k w/stage** | **3–4** |
| **2 — scaling** | 1919-01-01 → **1945-12-31** | **one-and-a-quarter**: (d) answers in-window but with the **Canadian affiliate's** record (1920, 1925, 1926, 1927, 1929, 1930, 1931, 1932, 1934, 1938, 1941, 1943, 1944 = 13 layers inside the window). Strictly by entity, **zero** held lines name the US registrant in 1919-1945 — the parent-naming lines are 1949/1950 (§1.4). (a) out-of-window; (c) UNANSWERED; (b),(e) UNTRIED | **T3 register — PROVISIONAL**; T2 **only** if a US-entity carrier lands in-window | **8k w/stage** (not 22k) | **3–4** |
| — 1946-1950 material | not a briefed stage | 3 Canadian layers + the parent-naming lines | belongs to a **proposed Stage 3**, tier unassessed here | — | — |

**Both tiers are PROVISIONAL in the RD-112 sense** (Costco/Dell precedent): family (c) has query blocks that were
never run, family (b) has no route at all, family (e) was never touched, and 34 of the 42 in-window IA items are
unattempted. A tier may not be finalised while an untried family exists; it may only be reported as the tier the
*held* corpus supports today.

**Proposed windows to flag for the orchestrator (none is mine to set):**
1. **The Stage-1 boundary is the problem, not the tier.** If the registrant is the 1919 Delaware corporation — as
   its own S-4 and 10-K state (§1.3) — then a Stage 1 dated 1903-01-01→1918-12-31 is a window whose first sixteen
   years belong to **a different legal person** (the Michigan company, itself the successor of earlier Ford
   ventures). Either Stage 1 is re-cut at **1919-01-01 → 1928** (registrant's own incorporation → first hard
   held-year series) with 1903-1918 carried as *predecessor ancestry*, or the corpus keeps the brief's cut and
   the volume must say so in every §A line. **Precedent binding here: Target's 1902 Dayton ancestry was retained
   at UNKNOWN against a probe's assertion, and Berkshire's predecessor name came only from a 1958 court record
   nobody had opened.** My recommendation is the second until a 1903-era or 1919-era document is on disk.
2. `tools/harvest_mine.py` WINDOWS end for ford (**1950-12-31**) vs the briefed origin window end (**1945-12-31**).
   One or the other is stale; three held layers fall in the gap.
3. A **Stage-3 window** beginning at the measured EDGAR floor **1994-01-20**, and the unbridgeable gap 1946-1993
   for this company (no filings, and the Canadian print run reaches only 1950 on the rows we hold; 1968 appears in
   candidates.csv and is unmined).

---

## 4. Load-bearing questions, each with the carrier that could settle it

1. **Which founding act has a carrier, and which entity does it name?** Held answer: the **only** carrier is the
   registrant's own 1994-2000 boilerplate (§1.3) and it names **two** acts — Delaware 1919 (the registrant) and
   Michigan 1903 (a predecessor whose *business* was acquired). Class `FOUNDER CLAIM`/company self-narrative,
   `RETROSPECTIVE SOURCE`, Conf **Medium** (one lineage, verified TLS, 76-97 years late). **No 1903 document and no
   1919 document is held.** The 1899 Ford & Dockwether and 1901 Henry Ford Company hypotheses have **0 hits in
   every held byte and 0 hits in the IA index queries run this pass** (`"Henry Ford Company"` numFound=1 — a 2013
   biography; `Dockwether` numFound=0; `"Ford Motor Car Company"` numFound=0 both faceted and unfaceted; `Muddison`
   numFound=0; `"Dodge Brothers" AND "Ford Motor"` faceted 1903-1920 numFound=0) — **but each of those zeros is a
   statement about the Internet Archive annotation/`text:` index, not about the printed record** (sidecar line:
   "the `text:` field in advancedsearch matches ANNOTATIONS, not this layer"). Verdict for those names:
   **UNANSWERED via (c) full-text; UNTRIED via CA/HT/GB.**
2. **Who is credited, by which document?** Henry Ford is credited *by the registrant itself* as the designer —
   "to produce automobiles **designed and engineered by Henry Ford**" (§1.3, l.706). In held third-party/company
   print, Henry Ford and Edsel B. Ford appear **only as officers of Ford Motor Company of Canada, Limited**
   (§1.1). No held document credits a Dodge, a Leland/Cadillac, or an A. J. Muddison. Any credit beyond Henry Ford
   is currently **UNKNOWN**.
3. **First real experiment.** Best held candidate: the **profit-sharing / $5-a-day plan**, dated by the company's
   own print as inaugurated **January 12th, 1914** (`fordmotorcoprofitsharing` l.822-823; the 1915 copies'
   anniversary framing l.1403-1405). It is in-window Stage 1, company-authored, Tier-1 class, **Conf Medium**
   (UNVERIFIED TLS; three copies = one lineage). Open: whether the plan counts as "the first real experiment" for
   a *product* company or as an internal-labour experiment; the Model T (1908) and the moving line (1913) have **no
   held carrier** (`Model T` 0 hits, `moving line` 0, `assembly line` 0 in the McGill layers; the 3 EDGAR `Model T`
   hits are the case-insensitive substring `model t` inside interest-rate boilerplate — read at
   `sources/sec/0000037996-00-000019_0000037996-00-000019.txt` **l.3643**: "We use a **model to** assess the
   sensitivity of our earnings … The **model re**calculates earnings"; the SWODA photo items *titled* "At The End Of The Assembly Line" (1917),
   "Moving Conveyors Hasten The Motor Assembly" (1917), "Ford Motor Plant And A Single Day's Output" (1918) are
   **metadata leads with 77 B or no text layer held** — UNTRIED, not evidence.
4. **First repeatable validation.** Only two candidates have held bytes: (i) the plan's own **before/after table**
   compiled one year later (l.1403-1424: employees 13,251 → 14,255; bank balances $990,418 → $3,040,301), a company
   self-report with no independent count behind it (§2 record-selection null); (ii) the Sirocco pamphlet's
   throughput claim "a Ford car every 45 seconds — nearly 1500 automobiles" (l.314-315), third-party print whose
   **date is contested (1914 vs 1904) and therefore UNKNOWN**. Neither may be promoted to FACT without a second,
   independent carrier. Everything else — Model T adoption, 1913 line, $5 day as an external event — is
   **UNTRIED**, and the brief's demand that they be "evidenced, not assumed" is honoured by not claiming them.
5. **First incurred operational failure.** Strictly by entity, **none is held for the US registrant**. Held
   candidates, all Canadian: the 1931 **net loss of $1,384,757.19** (operating loss $1,668,630.21) with the
   **dividend cut after June 20th, 1931** (635595 l.61-69, l.234-239), the 1932 loss widening to **$5,206,736.59**
   (635596 l.64-70), and the **1944 three-week work-stoppage from a strike by employees** plus the 1943
   labour-scarcity production cut (635608 l.531-538, l.541-542). The 1919 consent decree — the brief's expected
   answer — has **0 carriers** (§1.2) and must stay UNTRIED.
6. **First real conflict with the state.** Held: nothing for the registrant. For the Canadian company, 1941-1944
   state *contracting* rather than conflict — "His Majesty's Government" contract-price reduction (635605 l.218),
   **Dominion Government advances** (635605 l.552-553; 635608 l.594-596), a **National War Labour Board Finding and
   Direction** (635608 l.563-564), excess-profits tax provisions (635608 l.572-577). These are the registrant's
   *affiliate* facing a *foreign* state. The 1941-42 unionising wave and the 1945 labour actions (brief-named) have
   **no held carrier and no UNANSWERED route tried** — they sit in `## Untried` and nowhere else.
7. **Entity attribution for the register.** Every row must carry an `entity_named` value. The register the merge
   will need has three distinct persons in it already: **Ford Motor Company (Delaware, 1919 — the registrant)**,
   **Ford Motor Company (Michigan, 1903 — predecessor, business acquired)**, **Ford Motor Company of Canada,
   Limited (Dominion Companies Act, "original incorporation … in 1904" per its own 1949 report l.1085)**, plus
   **Ford Motor Company of India, Limited**, **of Malaya, Limited**, **of Australia**, **of New Zealand Limited**,
   **Ford Motor Company Limited (Dagenham, England)** — the last six are affiliates named *by* the Canadian
   company, in-window, and are third-party namings of *other* Ford entities, never of the registrant's founding.
8. **Accounting basis.** Canadian year-end moved **July 31 → December 31 between FY1926 and FY1927** (635589/635590
   vs 635591 l.17); the 1920 report's own tax/fiscal mismatch is printed at 635585 l.195-200. Any Stage-1/Stage-2
   series crossing 1926-27 must carry a basis line, and the `1932-7-31` style titles in `candidates.csv`
   contradict the printed `YEAR ENDED DECEMBER 31st, 1932` — **item-metadata dates are unreliable for this
   registrant family** (RD-121).

---

## 5. Untried (one command per route)

1. **(c) Chronicling America, Detroit/Dearborn press 1903-1918 — UNANSWERED (403-challenge zone / 404s).** Do not
   run `periodical_harvest.py` (races live merges). Runner-less command, then hold under
   `sources/periodicals/CA/`:
   `curl -s "https://chroniclingamerica.loc.gov/search/pages/results/?andtext=%22Ford%20Motor%22%20Dearborn&date1=1903&date2=1918&dateFilterType=yearRange&state=Michigan&format=json&rows=20"`
   (a 403-with-challenge header keeps the family UNANSWERED; only a 200 with rows answers it).
2. **(c) HathiTrust full text — UNANSWERED (1 row, blank status).** Rights first, then text:
   `curl -s "https://babel.hathitrust.org/cgi/ls?q1=%22Ford%20Motor%20Company%22%20Dearborn;a=srchls;anyall1=phrase;field1=ocr;rqn=1"`
   → parse to `_RECORDS.tsv` as RD-127 did for Walmart, then
   `python tools/ia_text.py fetch --id <htid-copyable-layer> --company-dir <dir>` where a Full-view layer exists.
   The Ford side of `_probe_fixed_20260925/hathitrust/` does not exist (verified: that directory holds Walmart
   bodies only).
3. **(c) Google Books — UNTRIED at text level (18 metadata rows; feeds returns no snippet).**
   `python tools/ia_text.py search --q '"Ford Motor Company" Dearborn' --rows 20 --insecure` is IA, not GB; the GB
   route needs `curl -s "https://www.googleapis.com/books/v1/volumes?q=%22Ford+Motor+Company%22+Dearborn+1903+1919&maxResults=20"`
   → 429/zero-byte = UNANSWERED, not NULL.
4. **(d) finish the in-window IA page — 34 of 42 items unattempted, and the un-mined candidates are where the
   US-entity print is.** Highest-value un-mined `item_id`s already in `candidates.csv` (all `TIER1_CANDIDATE`,
   metadata-level only): `henryfordletter00ford` ("Henry Ford letter to Judge R.A. Parker, dated Dearborn,
   Michigan", 1923), `bub_gb_4K82efXzn10C` ("My Life and Work", 1922 — a retrospective founder text *usable only* as
   `RETROSPECTIVE SOURCE`), `financialhistory00seltz` ("A financial history of the American automobile industry",
   1928 — third-party, the likeliest independent carrier of the 1903-vs-1919 entity story),
   `fordmotorcartruc01manl` (1917), `2911_SWODA` ("Ford Motor Co., Detroit, Mich.", 1915), `3241/3242/3243_SWODA`
   (1918), `3289_SWODA` ("Moving Conveyors Hasten The Motor Assembly", 1917), `triumphanidea...` (1934 ×2).
   Command: `python tools/ia_text.py mine --q '"Ford Motor Company" (Detroit OR Dearborn OR automobile) AND mediatype:texts AND YEAR:[1903 TO 1918]' --rows 42 --pattern "Ford Motor Compan" --company-dir founders_playbook/01_companies/company_022_ford --insecure`
   (or raise `harvest_mine.py --limit`: `python tools/harvest_mine.py --company ford --limit 40 --min-year 1903 --max-year 1918 --insecure`).
5. **(d) the rest of the Canadian bound run — 118 candidate rows, 12 mined, 93 untried at the `--limit`**
   (`grep -n "candidate rows in the harvest index" research/A4_harvest_mine.md` → line 5).
   Command: `python tools/harvest_mine.py --company ford --limit 40 --insecure` — **but only after the entity
   question is settled**, because every mined item so far is the wrong legal person; a 1907-1919 Canadian layer,
   if the run reaches back that far, is still not the registrant's founding record.
6. **(b) web archives — no scripted route exists.** `curl -s "http://web.archive.org/cdx/search/cdx?url=ford.com&output=text&fl=timestamp,original,statuscode&limit=40&from=1996&to=2004"`
   → store under `sources/web_archive/`. Zero in-window value for 1903-1945; recorded so the family is queried, not
   guessed at.
7. **(e) auction / museum documentary records — UNTRIED, no scripted route, 0 web budget.** Dispatch needs either
   a web budget or a new script (Heritage/Bonhams lot search + The Henry Ford / Benson Ford Research Center
   finding aids for 1903-1919 Ford Motor Company documents and the Dodge-era papers).
8. **(a) the 595 EDGAR filings `--max-docs 40` never enumerated** — all post-1994 and therefore all outside both
   stage windows; command: `python tools/sec_intake.py index --company-dir <dir>` then re-`auto` with `--from
   1994-01-01 --to 1994-12-31 --max-docs 120` only if a Stage-3 pass needs them.

---

## 6. Defects returned for the orchestrator (not evidence), and what this probe refuses to claim

**Defects / findings for the tools and the fleet index:**
1. **The digitised corporate-print run for ford is the wrong legal person, end to end.** **62 of 62**
   `corporate_print` candidate rows carry `Canada` in the title (command:
   `python -c "import csv;rows=[r for r in csv.DictReader(open('founders_playbook/00_universe/harvest/candidates.csv',encoding='utf-8-sig')) if r['company']=='ford' and r['source_family']=='corporate_print'];print(len(rows),sum('Canada' in (r['title'] or '') for r in rows));print(sorted({r['date_or_issue'][:4] for r in rows}))"`),
   and the indexed years are **1920-1921, 1923-1950 and 1968** — i.e. the bound run never reaches back to
   1903-1919 at all. **Fourteen** indexed years inside the tool window are still **unmined**, twelve of them inside
   the Stage-2 window (**1921, 1923, 1924, 1928, 1933, 1935, 1936, 1937, 1939, 1940, 1942, 1945**), plus **1946,
   1947** and **1968**: the family that flipped Walmart, Target, Boeing and Kroger is, for Ford, a run of **the
   wrong legal person**. `queries.json`'s CP task `company_terms` never includes a `-of-Canada`
   exclusion or a "Michigan"/"New Jersey"/"Delaware" discriminator, so a deeper `--limit` mines more of the same
   wrong entity.
2. **`harvest_mine.py` left `McGillLibrary-635595-36458` (FY1931, 6,146 B) unmined and unlisted** while it sat in
   `corporate_print/` — a held-but-invisible layer containing that sub-corpora's largest single Stage-2 loss
   statement. A `--limit` cut hides bytes already on disk; report them.
3. **Two byte-identical IA copies carry different catalogue years (1904 / 1914)** for the Sirocco pamphlet, and
   `candidates.csv` `date_or_issue` for all McGill rows is the scan/title year while the printed year-end differs
   (RD-121 restated for this company).
4. **`tools/sec_intake.py` default `--from 1900-01-01 --to 2030-12-31`** makes its own "in window" print
   incompatible with the company's briefed origin window; the printed line "618 accessions in window" is not a
   statement about 1903-1945. Consider printing the window literals next to the count.
5. **No `web_archive` family exists in `queries.json` at all** (fleet-wide), so family (b) will read as absent for
   every old company.
6. **`tools/harvest_mine.py` WINDOWS ford end (1950-12-31) vs the brief's 1945-12-31** — one is stale (§0).

**Refused on this pass (each with the reason):**
- Refused to call **1903 the founding of the registrant**, and refused to call **1919 the founding of Ford Motor
  Company** — the held sentence supports "the registrant was incorporated in Delaware in 1919 and acquired the
  business of a Michigan company incorporated in 1903" and nothing about which act is *the* founding of the company
  the dataset is about. Class: `U.`-level conflict, unresolved, Conf **Low**.
- Refused to treat any McGill layer as the registrant's record; refused to use the 1931/1932 losses, the 1944
  strike, the 1920 output of 55,616 cars, or the 1919→1949 employee series as Ford Motor Company (US) numbers.
- Refused to date the Sirocco pamphlet at 1904, and refused its "Ford car every 45 seconds" as evidence of the
  1913 moving line.
- Refused to claim the **1919 consent decree**, the **1941-42 unionising wave**, the **1945 labour actions**, the
  **Ford & Dockwether** 1899 partnership, the **Henry Ford Company** 1901, **Cadillac**'s derivation, the **A. J.
  Muddison** plant, **John and Horace Dodge**'s role, or **Edsel Ford**'s role at the US company — **0 carriers in
  held bytes**, and every index that returned 0 is an annotation index, not a full-text one. All are UNANSWERED or
  UNTRIED, never NULL.
- Refused to count the three IA copies of the 1915 pamphlet, or the eleven EDGAR occurrences of the founding
  sentence, as more than **one source each** (§3).
- Refused to cite any IA-held passage at **High** confidence (UNVERIFIED TLS sidecars).
- Refused to run `tools/periodical_harvest.py`, `tools/gates.py --checks` beyond the briefed two, and any
  WebSearch/WebFetch; wrote no volume, no register, no certification, and moved/deleted nothing under `sources/`.

GATE (context only, run before reporting):
`python tools/gates.py --company-dir founders_playbook/01_companies/company_022_ford --checks csv,keys --fail-on substantive`

STATUS: WRITTEN 2026-09-30
