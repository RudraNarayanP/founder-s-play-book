# A — Chronology feasibility probe · company_034_humana (Fortune rank 34)

STATUS: WRITTEN (owner `probe-humana`; appended in place, never rewritten by a sibling pass)

| line | value |
|---|---|
| Agent / claim | `probe-humana`, claimed via `tools/scaffold.py claim` at 2026-10-06T11:47:44Z |
| Budget | 85 tool calls; stop opening new routes at 70 |
| Web calls made | **0** (hard rule 1). No script that reaches the network was run by this probe — see `## Refusals` |
| Scripts NOT run (per brief) | `harvest_mine.py`, `periodical_harvest.py` |
| Gate | `python tools/gates.py --company-dir founders_playbook/01_companies/company_034_humana --checks csv,keys --fail-on substantive --out founders_playbook/03_quality_control/humana_s1_probe_gates.md` |
| Method read | `00_METHOD_AND_STYLE.md` §15, §14, §3, §7, §13; `MASTER_RESEARCH_LOG.md` RD-112, RD-124, RD-130, RD-134 |
| Registers invented | **none** (§13). This is a probe dossier, not a register |

## 0. Verdict in one paragraph

Tier verdict, per stage: Stage 1 = T3 register (PROVISIONAL); Stage 2 = T3 register (PROVISIONAL); Stage 3 = T3
register (intake-limited).

**Stage 1 (origin): T3 register, PROVISIONAL. Stage 2 (1984-1993): T3 register, PROVISIONAL. Stage 3
(1994-2001): T3 register, intake-limited.** Zero families return in-window Tier-1 text at Stages 1-2 and one
at Stage 3 (§5). The origin question is answered in the public record only by the registrant's own **forward
recitals**: eight separate annual-report accessions filed 1994-03-29 → 2001-03-30 print "Humana Inc. is a
Delaware corporation organized in 1961", and not one of them says what the 1961 corporation *did*. Every
held document that dates the health-benefits identity of this company dates it to **1983**, not 1961, and
**seven files across six accessions** call the 1961 entity "**a predecessor corporation**" in their
officer/director footnotes (line-wrap-tolerant count — a plain single-line grep reports five; see §3c).
EDGAR's own registrant metadata for CIK 0000049071 carries two **former names** — `EXTENDICARE INC` (name
change 1974-04-04) and `HERITAGE HOUSE OF AMERICA INC` (name change 1967-11-29) — a name-chain that begins
**six years after** the recited 1961 organization and attaches two nursing-home titles to the same CIK that
now prints "Humana Inc." That is the trap this probe was briefed to find, and it is present in the bytes.
Nothing in the local corpus supports "founded in 1961 **as a health insurer**", and nothing in the local
corpus mentions the instrument/humidity origin either (`humidity`, `hygrometer`, `humidistat` = **0 hits** in
all 26 held documents). The thin result is a **measured perimeter**, not a null: EDGAR's earliest indexed
Humana filing is 1994-02-01, so the company's own founding decade is unreachable by the filings family by
construction; of the four non-SEC families, two are UNTRIED, one is TRIED–UNANSWERED, and one returned a
per-parameter zero with 0 bytes on disk (see §4).

## 1. What is actually on disk (measured)

Enumeration command and output, run by this probe against `company_034_humana/sources/`:

```
$ find sources -maxdepth 1 -type d
sources ; sources/sec ; sources/_index ; sources/corporate_print

$ cd sources/sec && ls *.txt *.htm *.html | wc -l            -> 26
$ ls *.txt *.htm *.html | xargs wc -c | tail -1              -> 6052723 total
$ ls *.txt *.htm | wc -l                                     -> 23
$ ls *.txt *.htm *.html | sed -E 's/^([0-9]{10}-..-......).*/\1/' | sort -u | wc -l   -> 17 accessions
$ md5sum *.txt *.htm *.html | awk '{print $1}' | uniq -d     -> (empty: no byte-identical duplicates)
```

- **26 documents / 6,052,723 bytes / 17 accessions**, all under `sources/sec/`. `sources/sec/_RUN.json`:
  `"stored": 26, "unanswered": 5, "skipped": 81, "attempted": 112, "identity_ok": true`, `"window":
  "1985-12-31..2010-12-31"`, `"bytes": 6052723`.
- **The dispatch line "Local bytes: 23 sec" does not reproduce as a document count.** It is the
  `*.txt *.htm` glob above, which silently misses the three `.html` files this registrant's intake stored
  (`0000930661-00-000784-d1.html`, `0000930661-00-000839-d1.html`, `-d6.html`). The narrower claim this probe
  publishes: **26 stored documents, 3 of them `.html`.** A glob that looks like a count is RD-124's defect class.
- `sources/corporate_print/` **exists and contains 0 files** (`find sources/corporate_print -type f | wc -l`
  → `0`). No `sources/web_archive/` and no `sources/periodicals/` directory exists at all.
- Fleet harvest shelves, measured by this probe (`00_universe/harvest/`): `mine_bytes/` **0 files** (RD-124
  relocated 110 files here; it is now empty of anything attributable to this company); no filename anywhere
  under `harvest/` matches `*humana*` (case-insensitive `find` → 0 results). Only **2 distinct search-response
  objects** in the whole fleet corpus mention "Humana" (`internet_archive/02f1c54220ae80ab.json` and
  `4d71b715fead8b70.json`, both retrieved 2026-09-29T19:15Z) — and both are Solr **result listings**, not text.
  No Humana periodical or corporate-print **bytes** exist on this machine. The thinness is structural.

### 1a. The filings-family perimeter (measured against the index, not asserted)

```
$ python -c "... submissions.csv ..."
header: filingDate, form, accession, reportDate, primaryDocument, source
total rows 3466 ; min filingDate 1994-02-01 ; max 2026-09-03
in-window 1961-01-01..1985-12-31 rows: 0        distinct accessions in window: 0
rows before 1994-02-01: 0
per-source: CIK0000049071-submissions-002.json  466  min 1994-02-01  max 2002-08-30
            CIK0000049071-submissions-001.json 2000  min 2002-09-04  max 2018-02-26
            recent                              1000  min 2018-02-27  max 2026-09-03
```

The three archive slices are **contiguous** (no gap between 2002-08-30 and 2002-09-04) and
`sources/_index/_INDEX.md` §"UNANSWERED slices (never report these as absent)" prints **`(none)`**, while
`00_universe/_FLEET_INTAKE.tsv` records `slices_capped = no` for this slug. So RD-134's truncation defect is
**not** live here, and the pre-1994 silence is a **measured EDGAR perimeter** — the walk read everything and
everything starts at 1994-02-01. It is *not* evidence that Humana filed nothing; the company's paper-era
filings were never converted to EDGAR, and this probe may not claim otherwise either.
`_registrant_CIK0000049071.json` records `"registrant": "HUMANA INC"`, `"cik": "0000049071"`,
`"tickers": ["HUM"]`, `"guard": "ok"`, `"former_names": []` (the API's former-name array is **empty** even
though the filing headers print two former names — see §3b).

### 1b. Two quantifiers in the dispatch line that this probe could not reproduce

Hard rule 8: they are reported as measurements, not repeated as facts.

| dispatch figure | this probe's measurement | how it was produced |
|---|---|---|
| "23 sec" | 26 documents (`*.txt *.htm *.html`); 23 is the `*.txt *.htm` subset | glob missing 3 `.html` files |
| "148 accessions in window" | Not reproducible from `submissions.csv`. The Stage-1 window 1961-01-01→1985-12-31 has **0** rows; the recital pass's own window 1985-12-31→2010-12-31 has **1414** rows / 1414 accessions | `00_universe/_FLEET_INTAKE.tsv` stores `rc1/inwindow148/UNANS5` in `pass2_status`, which `tools/fleet_intake.py` (l.111-119) writes by regex-scraping `sec_intake.py`'s own printed summary, so 148 is **a tool's printed count for the recital window, after `sec_intake`'s form-key dedupe and `--max-docs 30` cut** — not an index count. This dossier cites 1414 as the index measurement and 26/5/81/112 as the run measurement, and does not use 148 as evidence of anything |

STATUS: WRITTEN.

## 2. Windows — PROPOSED by this probe (none inherited as evidence)

`00_universe/fortune_top_50_2026.csv` has **no founding-date column** (RD-112), which this probe enumerated
rather than assumed:

```
HEADER: rank, company, revenue_usd_millions, revenue_fiscal_year, profit_usd_millions, hq_city, hq_state,
        fortune_industry, universe_source_url, verified_by_second_source, confidence, notes
ROW 34: 34 | Humana | 129664 | fiscal year ended 2025-12-31 | 1188 | Louisville | Kentucky |
        Health Care: Insurance and Managed Care | … | SEC EDGAR 10-K XBRL: exact match … | High | …
```

The only date field on the rank-34 row is `revenue_fiscal_year` = "fiscal year ended 2025-12-31" — a *fiscal*
year, not a founding year (a substring test for `year` returns True on that column, which is precisely the
false positive Rule 6/§14 warn about, so the claim published here is "no founding-date column", not "no dates").
The row's `fortune_industry` value "Health Care: Insurance and Managed Care" is a **2025 sector label** and is
not evidence about 1961. The only 1961/1985 pair anywhere in this repo's tooling is a **harvester parameter**:

```
$ grep -n -i humana tools/harvest_mine.py
65:    "humana": ("1961-01-01", "1985-12-31"), "att": ("1885-01-01", "1984-12-31"),
```

Per §15.2/RD-112 that is a search setting, not a founding date. It is reported here as the origin of the
inherited bracket, and the bracket below is re-proposed on evidence.

| stage | window (PROPOSED) | on what evidence | what the window is *not* |
|---|---|---|---|
| **1 — origin and identity** | **1961-01-01 → 1983-12-31** | Start = the registrant's own earliest self-recited date, "organized in 1961" (§3a). End = the registrant's own earliest self-recited **business** date, "Since 1983, the Company has offered managed health care products" — the first year the held record lets the company attach its health-benefits identity to itself. Choosing 1983 rather than 1985 makes the boundary an evidenced discontinuity instead of a round number | NOT the founding of a health insurer. Nothing in the corpus dates an insurance identity to 1961 |
| **2 — managed-care build-out to the pure health plan** | **1984-01-01 → 1993-12-31** | Bracketed at the far end by a dated corporate act printed in the earliest held filing: "On March 1, 1993, the Company separated its acute-care hospital and managed care health plan businesses into two independent publicly-held companies (the 'Spinoff')" — the registrant's own hardest internal discontinuity, and the reason a 1961→1993 "early years" bracket would mix two companies | Filings reach this window only from 1994-02-01 (measured floor), so stage-2 *events* are in-window but their *documents* are one step behind |
| **3 — the health-plan company, 1994→** | **1994-01-01 → 2001-12-31** | Exactly the measured EDGAR floor forward; 26 documents held, earliest 1994-02-01 SC 13G | Not a "scaling" window in the folk sense; it is where the archive begins |

The inherited 1985 endpoint is **retained as an alternative** for Stage 1 because the one third-party item
this probe found with an in-window catalogue date is a 1984 court record (§3c); under either bracket, Stage 1
has 0 in-window documents on disk, so the tier does not move on that choice. A re-grade that does move a
verdict must, per RD-112, name which stage's window it moved — this dossier moves none.

STATUS: WRITTEN.

## 3. Carriers for the origin / predecessor question — what each one actually asserts

The briefed trap was: *"a 'founded 1961' date and a 'founded as a health insurer' claim are two different
assertions; find which one each carrier actually makes."* They are separable in these bytes, and **no held
carrier makes the second one.**

### 3a. Carriers that assert a 1961 ORGANIZATION (and are silent on the business)

All are `sources/sec/` files. "8 accessions / 9 files" below because the 2000 10-K is stored as a `.txt`
wrapper plus its `-d1.html` component — **one lineage, one source** (§3 independence rule), not two.

| carrier (stable label) | file | locator | verbatim | assertion made |
|---|---|---|---|---|
| 10-K FY1993, filed 1994-03-29 | `0000950123-94-000626_0000950123-94-000626.txt` | l.143-145 | "Humana Inc. is a Delaware corporation organized in 1961. Its principal executive offices are located at 500 West Main Street, Louisville, Kentucky 40202" | organization year + state **only** |
| 10-K405 FY1994, 1995-03-30 | `0000950123-95-000798_…txt` | l.97 | same sentence | idem |
| 10-K405 FY1995, 1996-03-29 | `0000950123-96-001406_…txt` | l.149 | same sentence | idem |
| 10-K FY1996, 1997-03-28 | `0000950131-97-002198_…txt` | l.149 | same sentence | idem |
| 10-K FY1997, 1998-03-31 | `0000950131-98-002266_…txt` | l.149 | same sentence | idem |
| 10-K405 FY1998, 1999-03-31 | `0000930661-99-000640_…txt` | l.154 | same sentence | idem |
| 10-K FY1999, 2000-03-30 | `0000930661-00-000839_…txt` (+ `-d1.html`) | l.626 | "…corporation organized in 1961. Its principal executive offices are located…" | idem |
| 10-K405 FY2000, 2001-03-30 | `0000950131-01-500403_d10k405.htm` | l.269 | same sentence, HTML-rendered | idem |

```
$ grep -o -i -- "organized in 1961" *.txt *.htm *.html | wc -l   -> 9   (8 accessions)
$ grep -o -i -- "founded in 1961" *.txt *.htm *.html | wc -l     -> 0
$ grep -o -i -- "humidit*" / "hygromet*" / "humidistat"          -> 0 hits in all 26 documents
$ grep -o -i -- "Busick|Nevens|Rains"                           -> 0 hits
```

**Reading.** The 1961 date is a **corporate-organization** recital repeated verbatim in the registrant's own
Item 1 boilerplate. It is one source class, not eight corroborations (§3). It carries no business content, so
it cannot settle whether the 1961 corporation was an instrument company or an insurer — and the word
"humana" as a humidity-measurement etymology appears **nowhere** in the held bytes (0 hits, measured above).

### 3b. The continuation carrier: EDGAR's own former-name chain on the same CIK

Measured: the block is printed in **15 of the 17 accessions** on disk (`grep -l 'FORMER CONFORMED NAME' *.txt
*.htm *.html` → 15 files, 15 distinct accessions; 15 `EXTENDICARE` lines total). The two accessions whose held
files lack it are `0000950123-95-000798` (10-K405 FY1994, whose single stored file carries no `<IMS-HEADER>`) and
`0000950131-01-500403` (10-K405 FY2000 — none of its four stored files do). Attached to the *FILED BY* block
whose conformed name is HUMANA INC / CIK 0000049071. Example,
`sources/sec/0000049071-94-000003_0000049071-94-000003.txt` l.45-70:

```
COMPANY CONFORMED NAME:  HUMANA INC
CENTRAL INDEX KEY:       0000049071
STANDARD INDUSTRIAL CLASSIFICATION: 8062
STATE OF INCORPORATION:  DE
FORMER COMPANY:  FORMER CONFORMED NAME: EXTENDICARE INC          DATE OF NAME CHANGE: 19740404
FORMER COMPANY:  FORMER CONFORMED NAME: HERITAGE HOUSE OF AMERICA INC  DATE OF NAME CHANGE: 19671129
```

This is the briefed "1990s-era registrant continuation naming a predecessor it acquired", and it is
**in direct tension with 3a**: the metadata chain begins **1967-11-29**, six years after the recited 1961
organization, and its two named predecessors are **nursing-home titles**, not a measurement-instrument
company and not an insurer. Meanwhile `_registrant_CIK0000049071.json` prints `"former_names": []` — the
EDGAR company-concept API returned an empty array while the filing headers print two former names, so the
two machine-readable views of the same registrant disagree, and neither can be used to settle the 1961
question. `Extendicare` and `Heritage House` appear **0 times in any body text** of the 26 held documents
(`grep -l -i` matches only header lines l.42-68) — the registrant never narrates these names; only the
plumbing does. SIC 8062 (`General Hospitals`) is itself a residue of an era no held document describes.

### 3c. Carriers that call the 1961 entity a PREDECESSOR

| carrier | file | locator | verbatim |
|---|---|---|---|
| DEF 14A 1994-03-29 | `0000950123-94-000627_0000950123-94-000627.txt` | l.379-380 | "(4) A director and chief executive officer of a predecessor corporation since 1961." |
| 10-K FY1993 | `0000950123-94-000626_…txt` | l.811 | "(1) Elected an officer of a predecessor corporation in 1961." |
| 10-K405 FY1994 | `0000950123-95-000798_…txt` | l.826 | "(1) Elected an officer of a predecessor corporation in 1961." |
| 10-K405 FY1995 | `0000950123-96-001406_…txt` | (same table) | idem — see the recount below |
| 10-K FY1996 | `0000950131-97-002198_…txt` | (same table) | idem |
| DEF 14A 2000-03-30 | `0000930661-00-000784_0000930661-00-000784.txt` | l.1451-1452 | "A director of a predecessor corporation since 1961." |
| 10-K FY1999 employment recital | `0000930661-00-000839_…txt` | l.8390-8392 | "WHEREAS, Jones is one of the original founders of Humana and served as Chairman of the Board of Directors of Humana … and/or Humana's Chief Executive Officer since 1961" |

Measured two ways, because the phrase is line-wrapped in the HTML carriers (§14 r8: an index-shaped count is not
a measurement of the bytes):

```
$ grep -o "predecessor corporation" *.txt *.htm *.html | wc -l      -> 5   (single-line matches only)
$ python -c "re.findall(r'predecessor\\s+corporation', text, re.I)" over all 26 docs
                                                                      -> 7 files / 7 hits / 6 accessions
   0000930661-00-000784.txt  +  …-d1.html   (2 files, 1 accession — "predecessor\n corporation")
   0000950123-94-000626.txt | 0000950123-94-000627.txt | 0000950123-95-000798.txt
   0000950123-96-001406.txt | 0000950131-97-002198.txt
```

The published figure is therefore **6 accessions / 7 files**, not 5: the naive single-line grep silently lost the
2000 proxy pair to a newline, which is the same class of defect as the `*.txt *.htm` glob in §1.

**This is the finding.** The registrant's Item 1 says *this* corporation was organized in 1961, while its own
director/officer footnotes — in the same filings, same years — say these people have been directors/officers
of "**a predecessor corporation**" since 1961. Both cannot be a plain statement of continuous identity, and
the filings never resolve it. Per §14 r5 and the four worked examples (Ford's Canadian layers, Citigroup's
1812, Boeing's "since 1916", Kroger's Great Western Tea), a predecessor naming is **not** the registrant's
origin, and here the registrant itself supplies the predecessor word. Class this as **RETROSPECTIVE
INTERPRETATION**, confidence **Low** on what the 1961 entity *was*, **High** only on the narrow fact that the
registrant has recited "organized in 1961" since at least 1994.

### 3d. Carriers dating the HEALTH-BENEFITS identity (never 1961)

| carrier | locator | verbatim | what it dates |
|---|---|---|---|
| 10-K FY1993 | `0000950123-94-000626_…txt` l.160 | "Since 1983, the Company has offered managed health care products which integrate financing and management with the delivery of health care services" | managed-care products, 1983 |
| 10-K405 FY1994 / FY1995 / 10-K FY1996 / FY1997 | l.111 / l.169 / l.174 / l.177 | "Since 1983, the Company has offered managed health care products…" | idem, 4 more accessions |
| 10-K405 FY1998 | `0000930661-99-000640_…txt` l.185-187 | "Since 1983, the Company has been a health services company that facilitates the delivery of health care services through networks of providers to its approximately 6.2 million medical members" | the *company's own health-services identity*, 1983 |
| 10-K FY1999 | `0000930661-00-000839_…txt` l.179 | "Since 1983 …" | idem |
| 10-K405 FY2000 | `0000950131-01-500403_d10k405.htm` l.274 | "Since 1983, the Company has been a health services company offering coordinated health insurance coverage" | **insurance** identity, 1983 — not 1961 |

Measured: `Since 1983` (line-wrap-tolerant, all 26 docs) → **10 occurrences / 9 files / 8 accessions**; the
single-line `grep -c` on the `.txt`+`.htm` subset reports 9 occurrences / 8 files, the missing hit being the
line-wrapped HTML component of the FY1999 10-K. **The only year this registrant ever
attaches to its own insurance/health-plan identity in the held record is 1983.** The 1961 recital and the
1983 recital sit two lines apart in the same Item 1 and are never reconciled in any held document.

Subsidiary naming for completeness: `sources/sec/0000950131-01-500403_dex21.txt` (Exhibit 21, 2001) lists the
Delaware/Florida/etc. subsidiaries under 2001 headings — `Humana Inc. - Doing Business As: H.A.C. Inc.;
Humana of Delaware, Inc.`, `Humana Health Insurance Company of Florida, Inc.`, `Humana Medical Plan, Inc.` —
brand-in-place naming, **not** an origin lineage (Rule 5). Frequency in held bodies:
`Humana Health Care Plans` ×71, `Humana Health Insurance Company o…` ×18, `Humana Health Plan of Texas` ×15.
`Humana Hospital Corporation` appears **0 times**; `Galen` (the spun-off hospital company) ×270.

STATUS: WRITTEN.

## 4. Five-family verdict (three states only; no untried family is reported as a null)

| family | state | what was run here, and the measurement | in-window Tier-1 text? | remedy named |
|---|---|---|---|---|
| **(a) SEC / EDGAR filings** | **TRIED–ANSWERED (forward recital only)** | Index walk read all 3 slices, no cap (`slices_capped=no`, `UNANSWERED slices: (none)`); perimeter measured 1994-02-01→2026-09-03, 3466 accessions; 26 documents / 6,052,723 B stored; 5 UNANSWERED, 81 SKIPPED, 131 in-window filings never enumerated (`_UNANSWERED.csv` last row) | **NO — 0 documents inside 1961→1983/1985.** Answered the *founding question* from 1994-2001 carriers (§3a-3d) | Orchestrator re-run `sec_intake auto` with `--max-docs` raised, over 1994-1999 (the paper-era gap is not closable by any tool) |
| **(b) Web archives** | **UNTRIED** | No `sources/web_archive/` directory exists (`find sources -maxdepth 1 -type d` → `_index`, `sec`, `corporate_print` only); no CDX attempt recorded anywhere for this slug; this probe ran 0 network calls | no | A Wayback/CDX pass run by the orchestrator. Note the ceiling is honest: archive-web coverage begins mid-1990s, so family (b) **cannot** answer Stage 1 under any bracket; it can answer late Stage 3 |
| **(c) Periodical corpora (CA / HathiTrust / Google Books / IA newspapers)** | **TRIED–UNANSWERED** | `00_universe/harvest/candidates.csv` holds **34 rows for `company=humana`** at the final re-read (was 32 at first read — the index grew under this probe, §9): 2 `chronicling_america` (`SKIPPED: global max-requests cap 600 reached`), 1 `google_books` (same cap), 1 `hathitrust` (`SKIPPED: hard stop: 5 consecutive failures (host halted)`), 26 `internet_archive` (22 `LEAD_ONLY`, 2 `TIER1_CANDIDATE`, 2 `UNANSWERED`), plus the 2 new `corporate_print` rows counted in (d). Every IA/CP row is now labelled `[FACET-FREE per RD-130]`, so the index records which question it asked. CA endpoint test `_CA_ENDPOINT_TEST.md`: **all 7 shapes CHALLENGED/403 — 0 ANSWERED shapes**. The 2 IA search responses are **listings**: `numFound=287` and `numFound=4`; **0 text bytes** of either are on this machine (`mine_bytes/` = 0 files; no `*humana*` filename in `harvest/`, re-checked 12:05Z) | no — no bytes at all | FETCH REQUEST 1; browser egress for CA; a re-dispatch of the two never-run HathiTrust/Google Books tasks |
| **(d) Digitised corporate print (annual reports, house organs, directories)** | **TRIED–ANSWERED per parameter, 0 bytes — and still NOT a corpus null** | Re-measured mid-write: the fleet `--facet-free` re-run fired for this company at **2026-10-06T12:04:08Z / 12:04:10Z** while this dossier was being written. `CP humana annual/shareholder print 1960-1995 … [FACET-FREE per RD-130]` → `LEAD_ONLY`, item `gov.uscourts.kywd.135623` **"In Re Humana Shareholder Derivative Action"** (collection `usfederalcourts`, `year=None`) — a federal-court docket shelved under `texts`, **not** corporate print. `CP humana corporate print by creator 1960-1995 [FACET-FREE per RD-130]` → `NULL`, tool text: *"EMPTY (proven null): numFound=0 FOR THESE EXACT PARAMS ONLY — per-param, never per-corpus"*. The two 2026-09-29 faceted rows (both `UNANSWERED`) remain in the index unchanged. `sources/corporate_print/` = **0 files** | no | FETCH REQUESTs 4-5: the title/brand routes for a Humana annual report or house organ have **never been asked** (only "annual/shareholder" free-text and a creator facet), and the one lead's text is not on disk |
| **(e) Auction / museum / manuscript** | **UNTRIED** | No route exists to attempt it: the five `source_family` values present for `humana` are `chronicling_america, corporate_print, google_books, hathitrust, internet_archive` (enumerated, not assumed); no manuscript/auction family in `candidates.csv`, `tools/queries.json` tasks, or `sources/` | no | A new task family, or a named repository query (Kentucky historical society / University of Louisville / Maryland Historical Society for the 1961 Baltimore start) dispatched by the orchestrator |

STATUS: WRITTEN.

## 5. Per-stage tiers (RD-112: each tier is that stage's own, never the company's)

| stage | window (PROPOSED, §2) | families returning **in-window Tier-1 text** | count | tier | provisional? |
|---|---|---|---|---|---|
| 1 — origin | 1961-01-01 → 1983-12-31 | **none.** (a) answered only from 1994-2001 carriers; (c)(d) 0 bytes; (b)(e) untried | 0 | **T3 register** | **PROVISIONAL** — family (c) is TRIED–UNANSWERED with 267 unlisted IA items and 0 bytes fetched, and family (d) was answered only **per parameter** (two param shapes asked; the title/brand shapes never were), so a T1/T2 could still arrive from periodical or corporate-print text; (b) and (e) untried cannot raise it for this window by construction |
| 2 — build-out | 1984-01-01 → 1993-12-31 | **none.** The earliest held document is 1994-02-01 (measured floor), so the whole decade is document-less even though it is event-rich and is *described* by the 1994 10-K's Spinoff recital | 0 | **T3 register** | **PROVISIONAL** — (c)/(d) could answer 1984-1993 trade press directly; a 1994+ filing already narrates it |
STATUS: WRITTEN.

## 6. Conflicts to be carried into `conflicts.csv` by the next pass (declared here, NOT invented as rows)

**U.1 — 1961 organization vs. a 1967 name-chain on the same CIK.**
CLAIM A: "Humana Inc. is a Delaware corporation organized in 1961" (10-K Item 1, 8 accessions, §3a).
CLAIM B: EDGAR registrant metadata on CIK 0000049071 prints former names `HERITAGE HOUSE OF AMERICA INC`
(name change 1967-11-29) then `EXTENDICARE INC` (1974-04-04) (§3b).
WHY THEY DIFFER: the metadata block records *conformed-name changes on the registration*, not the founding of
the business; a CIK can acquire names through a reorganization or a transferred registration without the
earliest-organized corporation carrying that name. EVIDENCE WEIGHT: A is the registrant's own sworn narrative
and appears in every annual report held; B is plumbing that the registrant never narrates (0 body-text hits
for either former name). BEST-SUPPORTED INTERPRETATION: publish 1961 as the **recited organization year of the
Delaware registrant**, class FACT (single lineage, confidence Medium at best), and publish the 1967/1974 chain
as a **separate, unresolved registrant-continuity question** — not as the origin. RESIDUAL UNCERTAINTY: whether
the 1961 corporation is the same legal person as the 1967/1974-named one, and what business either was in.
CONFIDENCE: Low on identity, High on "the record contains this tension".

**U.2 — "organized in 1961" vs. "a predecessor corporation since 1961" inside the same filings.** §3a vs §3c.
The Item 1 boilerplate asserts continuity; the officer/director footnotes assert a predecessor. One of the two
usages is loose drafting, and the held record never says which. Best-supported reading: 1961 attaches to *a*
corporate organization that people later called a predecessor; do not let the boilerplate retire the footnote.

**U.3 — 1961 vs. 1983 for the health-benefits identity.** §3a vs §3d. Not a real conflict in the bytes — the
registrant never dates insurance to 1961 — but it is the conflict **the folk founding story** creates, so it
must be registered: the earliest self-attached health-insurance identity in the record is 1983 (8 accessions),
and `Humana Health Insurance Company of Florida, Inc.`-style naming only appears in 1994-2001 documents.

STATUS: WRITTEN.

## Untried

Nothing here was attempted. Each is a route **not opened**, and none may be reported as a null by any later pass:

1. **Family (b) web archives — UNTRIED.** No `sources/web_archive/` path exists; no CDX/Wayback call for this
   slug anywhere in the repo. This probe made 0 network calls by rule, and `sec_intake.py`/`ia_text.py` both
   reach the network, so they were not run. Remedy: orchestrator runs a CDX pass; note the honest ceiling —
   web-archive coverage begins mid-1990s, so it cannot answer Stage 1 at all.
2. **Family (e) auction / museum / manuscript — UNTRIED.** No task family exists in `tools/queries.json` for
   any company's manuscript route and `candidates.csv` shows only the five IA/library families for `humana`.
   Remedy: a named route (University of Louisville / Filson Historical Society KY; Maryland Historical Society
   for a 1961 Baltimore start; SEC paper-era finding aids) must be authored before a verdict on (e) is possible.
3. **HathiTrust and Google Books bodies — UNTRIED at the item level.** One `hathitrust` row and one
   `google_books` row exist for `humana` and both are `SKIPPED` **before a request was made** (host halt, global
   600-request cap). A skipped query is not a zero result. Remedy: re-dispatch those two tasks only.
4. **The 287-item IA remainder — UNTRIED.** Only page 1 (20 rows) of the facet-free text listing is cached;
   267 items were never even listed, and the cached page is dominated by federal-court docket mirrors, so the
   real periodical remainder is unknown. Remedy: FETCH REQUEST 1.
5. **131 + 81 filings never enumerated/skipped by `--max-docs 30` — UNTRIED within the recital window.**
   `_UNANSWERED.csv` prints *"NOT-ENUMERATED: 131 in-window filings were never listed because --max-docs 30 was
   reached"* and `_RUN.json` prints `skipped: 81`. Remedy: FETCH REQUEST 3.
6. **The registrant's pre-1994 paper filings — no route exists.** EDGAR's floor for this CIK is measured at
   1994-02-01; the paper-era files (1961-1993) are not in EDGAR's electronic archive and no script in `tools/`
   reaches them. This is the single largest structural gap in this company's Stage-1 feasibility.

STATUS: WRITTEN.

## 7. FETCH REQUESTs (web budget 0 — these are emitted, not executed; every claim they bear is marked UNANSWERED)

```
FETCH REQUEST: 1
family:   (c) periodical corpora — Internet Archive full text
target:   IA advancedsearch, query `Humana (hospital OR insurance OR "health plan") AND mediatype:texts`
          response already cached at 00_universe/harvest/internet_archive/02f1c54220ae80ab.json
          (numFound=287, page 1 of 20 returned, retrieved 2026-09-29T19:15:36Z)
ask:      pages 2-15, EXCLUDING collection usfederalcourts/USGovernmentDocuments, returning
          identifier+title+date+year, then the text layer of any item whose date falls 1961-1993
why:      the only in-window third-party naming this probe can see is a court item; the periodical
          remainder of the 287 was never listed. Claim "trade press names Humana in 1961-1983" = UNANSWERED
destination: founders_playbook/01_companies/company_034_humana/sources/periodicals/ (§14 r9 — never %TEMP%)

FETCH REQUEST: 2
family:   (c) — the one genuine in-window entity naming visible in the index
identifier: micro_IA40385011_1273
title as catalogued: "General Hospitals of Humana, Inc. v. Arkansas Statewide Health Coordinating Coun"
date as catalogued: 1984-01-01 (collection microfiche / us-supreme-court)
ask:      `python tools/ia_text.py list-files micro_IA40385011_1273` then the text file
why:      would be the FIRST in-window (1961-1985) third-party document naming the Humana brand, and it
          names it attached to **hospitals**, which bears directly on U.1/U.2. Its catalogue `date` must be
          re-verified in the bytes before any use (RD-130/Disney: item dates can be uploader artefacts), and
          "General Hospitals of Humana, Inc." is a **subsidiary legal person**, not the registrant's origin
          (Rule 5). Claim = UNANSWERED until the bytes exist.

FETCH REQUEST: 3
family:   (a) SEC/EDGAR — the two accession families where a predecessor naming would appear
accessions: 0000950123-95-002354 (SC 14D1, 1995-08-16), 0000950123-95-000012 (SC 14D1/A, 1995-08-24),
            0001047469-98-027486 (DEFS14A, 1998-07-16), 0000049071-96-000004 (8-A12B/A, 1996-02-14)
command:  python tools/sec_intake.py auto "Humana Inc" --company-dir <dir> --from 1994-01-01 --to 1999-12-31 --max-docs 90
why:      `--max-docs 30` left 81 SKIPPED + 131 NOT-ENUMERATED filings in the recital window; the 1995-1998
            merger/re-registration paper is where an "acquired/f/k/a/formerly" sentence would be printed if
            one exists. Claim "the registrant narrates the Extendicare/Heritage House chain" = UNANSWERED
            (measured 0 body-text hits in the 26 documents held, which is a statement about 26 documents,
            not about the registrant's archive)

FETCH REQUEST: 4  [PARTLY SATISFIED by the live reharvest at 2026-10-06T12:04Z — remaining ask below]
family:   (d) digitised corporate print
asked already: both queries re-run with the YEAR facet removed. Result: one per-param numFound=0
          (`CP humana corporate print by creator 1960-1995 [FACET-FREE per RD-130]`, classification NULL,
          tool wording "FOR THESE EXACT PARAMS ONLY — per-param, never per-corpus") and one court-docket
          lead (FETCH REQUEST 5). `harvest_mine.py --company humana` has still NOT been run (brief excludes
          it; `mine_bytes/` measured 0 files at 12:05Z).
still ask: the param shapes never tried for this company — `title:(humana) AND mediatype:(texts)` unbounded;
          creator `Humana Inc.`; annual-report / house-organ title phrases ("humana" AND "annual report",
          "humana" AND employee magazine shapes). The claim "no digitised Humana corporate print exists"
          stays OFF: two parameter shapes are not the corpus.

FETCH REQUEST: 5
family:   (c)/(d) boundary — the only new naming lead tonight's facet-free run produced
identifier: gov.uscourts.kywd.135623
title as catalogued: "In Re Humana Shareholder Derivative Action" (W.D. Ky.; date_or_issue EMPTY, year=None,
          so the index cannot place it in any window)
command:  python tools/ia_text.py list-files gov.uscourts.kywd.135623 ; then --file on the complaint text
why:      Kentucky is the registrant's recited home state (10-K Item 1, Louisville 40202) and a shareholder
          derivative pleading is the class of third-party paper likeliest to recite, in its own factual
          background, how a 1961 corporation became a 1990s health plan. It is a COURT RECORD, not corporate
          print, and naming a defendant is not naming an origin (Rule 5). Claim UNANSWERED until bytes exist.
```

STATUS: WRITTEN.

## 8. What this probe refused to claim, and why

1. **Refused: "Humana was founded in 1961 as a health-insurance / health-benefits company."** Measured: 0 hits
   for `founded in 1961`, 0 hits for `1968`, 0 hits for `American Network`, and the only self-dated health
   identity is `Since 1983 …` (9 occurrences / 8 accessions). Publishing 1961-as-insurer would merge §3a's
   organization recital with §3d's business recital — §3's forbidden move.
2. **Refused: "Humana began as a humidity/measurement-instrument company."** Not because it is unlikely — it is
   the briefed origin story — but because **the held bytes contain 0 hits** for `humidit*`, `hygromet*`,
   `humidistat`, `Busick`, `Nevens`, `Rains`. An un-evidenced predecessor name is exactly Kroger's Great Western
   Tea / Boeing's "since 1916" failure in reverse: here the true story would be imported from outside the corpus
   and then look corroborated. Class: UNKNOWN, pending FETCH REQUEST 1-4.
3. **Refused to treat the 8 recital carriers as 8 corroborations.** They are one corporate-record lineage
   repeated across fiscal years (§3 filing-lineage rule); independence count = **1**, so the 1961 recital caps at
   what a single document supports.
4. **Refused to read EDGAR's former-name chain as the origin.** `EXTENDICARE INC` / `HERITAGE HOUSE OF AMERICA
   INC` are conformed-name events on a registration, they appear **only** in `<IMS-HEADER>` plumbing (0 body-text
   hits), and the API's own `former_names` array is empty for the same CIK — two machine views disagreeing is a
   conflict (U.1), not a fact.
5. **Refused to call the 2 `TIER1_CANDIDATE` harvest rows Tier-1 evidence.** Rule 6: one is
   `cultura-personal-y-ycultura-nacional / "Cultura personal y cultura nacional" (1964)` — a Spanish-language
   book in which *humana* is the ordinary feminine adjective "human", the RD-124 Apple/COSTCO decoy class
   exactly; the other is a US-supreme-court microfiche item whose catalogue `date` is unverified. Neither has
   bytes on disk. Neither counted in any tier.
6. **Refused: "EDGAR has nothing because Humana filed nothing before 1994."** The measured perimeter (3466
   accessions, floor 1994-02-01, no capped slices, `(none)` unanswered slices) says the archive ends there for
   this registrant — silence about early filings must travel with the measurement that explains it (RD-134).
7. **Refused to run any network script** (`sec_intake`, `ia_text`, `periodical_harvest`, `harvest_mine`): the
   brief fixes web calls at 0 and the two harvesters are explicitly excluded. Refusal is the correct behaviour,
   and the four routes it closes are listed as FETCH REQUESTs rather than as nulls.
8. **Refused to publish the dispatch line's "23 sec" and "148 accessions" as measurements** (§1b) — both
   reproduce only as tool/glob artefacts, and a narrower claim was available.

STATUS: WRITTEN.

## 9. Live-corpus notes (this dossier was written against a shelf that is moving)

- **`research/A4_harvest_mine.md` did not exist at any point in this run.** `ls research/` at 17:30 and again at
  17:35 local both return only `A_chronology_feasibility.md`; `test -f research/A4_harvest_mine.md` → NO. Nothing
  from it is quoted anywhere in this dossier — there is no mtime to note because there is no file, and the brief's
  warning that it "may be re-written under you tonight" is honoured by not citing it at all. If the mine writes
  one tonight, it supersedes §4 rows (c)/(d) only in the *bytes* it lands, and it must be re-read before any
  citation of it.
- `00_universe/harvest/candidates.csv` **moved under this dossier while it was being written**, measured twice:
  1,485,755 B / mtime 2026-10-06 17:19:41 local / 32 `humana` rows at the first read (17:30 local); then
  **1,879,741 B / mtime 2026-10-06 17:34:11 local / 34 `humana` rows** at the second read (17:35 local), the two
  new rows being the `[FACET-FREE per RD-130]` corporate-print pair retrieved `2026-10-06T12:04:08Z` and
  `12:04:10Z`. Family (c)'s IA/CA/GB/HT row counts are unchanged (26/2/1/1). `_MANIFEST.md` 337,660 B (17:19:41),
  `_CA_ENDPOINT_TEST.md` 2,159 B (17:19:41, all 7 shapes CHALLENGED), `_REMINE_RUN.log` **0 B** (17:14:06) — the
  reharvest is live and the *mine* has written nothing, so `research/A4_harvest_mine.md` cannot exist yet and
  §4(d) is stated from the index rows, not from mined bytes.
- Nothing cited in §4/§7 from that index is treated as evidence: it is a **listing** (Rule 6, "never cite an
  index column as evidence"), and every claim it gestures at is marked UNANSWERED with a FETCH REQUEST.
- `00_universe/harvest/mine_bytes/` measured **0 files** tonight although RD-124 relocated 110 files into it;
  this probe touched nothing there (hard rule 2, add-only, and this is not its path).
- **`tools/gates.py` itself was rewritten during this run** (mtime 2026-10-06 17:39:45 local, size 50,074 B):
  `issued_tier()` gained a `says` verdict-line regex and a new tie-break. Consequence recorded in §10. This
  probe wrote no file outside its own dossier and the one gate output path named in its brief (hard rule 2).
- Per §14 r11, nothing in `company_034_humana/sources/` arrived during this probe's run: the newest byte is
  `sources/sec/_RUN.json` built 2026-09-29T19:02:33Z, which predates this dossier, and all 26 documents are
  accounted for in §1 and §3.

STATUS: WRITTEN.

## 10. Gate

```
$ python tools/gates.py --company-dir founders_playbook/01_companies/company_034_humana \
    --checks csv,keys --fail-on substantive \
    --out founders_playbook/03_quality_control/humana_s1_probe_gates.md
Findings: 2 | Passes: 0     (both coverage-only: "no register CSVs at root or research/",
                              "no stage_*.md volumes found")
coverage 0 registers, 0 stage volumes, 26 source documents
```

`--fail-on substantive` is satisfied on every run: **0 substantive findings**; the 2 findings are a
freshly-probed company having no registers yet, which the tool itself labels "expected … NOT failing the exit
code" (exit=0). **`tools/gates.py` was rewritten under this probe** (mtime 2026-10-06 17:39:45 local, between
run 2 and run 3), and its tier-detector changed shape mid-flight, so all four runs are recorded:

```
run 1  11:47Z  before this dossier existed
   tier: exemplar (no tier stated in this company's research/ dossiers -- exemplar assumed)
run 2  12:05Z  after §5 was on disk, old detector
   tier: T3 (tier T3 from A_chronology_feasibility.md -- T1,T2,T3 also stated in this company's files
   (7 mentions); the most recent write wins, §15.2 regrade)
run 3  12:1xZ  same dossier, NEW detector (gates.py rewritten at 17:39:45 local)
   tier: T2 (tier T2 from A_chronology_feasibility.md -- T1/T2/T3 all mentioned in research/
   (20 mentions, 0 on a verdict line); … trust the dossier and tell me …)
run 4  12:2xZ  after §0 carried an explicit "Tier verdict, per stage: Stage 1 = T3 register …" line
   tier: T3 (tier T3 (a stated-verdict line) from A_chronology_feasibility.md -- T1/T2/T3 all mentioned
   in research/ (23 mentions, 3 on a verdict line))          Findings: 2 | Passes: 0 | 26 source documents
run 5+ final, close-out: tier T3 (a stated-verdict line), Findings: 2 | Passes: 0
   The mention counter is self-referential here — it read 23 / 3, then 32 / 12, then 34 / 14 as this section
   began quoting the detector's own output. **The tier label did not move once it had a stated-verdict line to
   read**, which is the point: the stability test is the `(a stated-verdict line)` flag, not the count.
```

**The finding is about the checker, not the company.** The rewritten `issued_tier()` only trusts a line that
matches its `says` regex **and** carries a `T[123]` token on the same line; a dossier that states its per-stage
tiers inside `## 5`'s heading-and-table construction (heading says "Per-stage tiers", the rows say "T3
register", never on one line) scores **0 verdict lines** and the detector falls through to its tie-break, the
**highest line index** — which in this dossier is a passing "could still arrive … T2" in §5's provisional note.
So a T3 dossier read as T2 for one edit, and the fix that made it read correctly was a **stated-verdict line in
§0**, not a change of finding. This dossier's issued tier is **T3 at all three stages** and never was T2. Two
things follow for whoever owns `gates.py`: (i) `says` should also fire on a table row whose subject column names
a stage, and (ii) RD-131's class is now demonstrated on a fresh file — **a mid-run tool rewrite can silently
change what a signed dossier says**, which is why this section quotes every run rather than the last one.
Output file: `founders_playbook/03_quality_control/humana_s1_probe_gates.md` — every run wrote the same path;
the file on disk is the final run's.

STATUS: WRITTEN.

## 11. The route most likely to change this verdict

**The Internet-Archive periodical remainder — FETCH REQUEST 1: re-page the facet-free text query whose
`numFound=287` was only ever listed 20 items deep, excluding the `usfederalcourts` collections, and put the text
layers of anything catalogued 1961-1983 into `sources/periodicals/`.** It is the only route that has already
returned a **positive** search answer for this company (`numFound=287`, `numFound=4`) while contributing **zero**
bytes to the corpus, and §14 r6 makes periodical text the one family carrying contemporaneous 1960s-1980s
evidence for exactly the window EDGAR measurably cannot reach. The corporate-print facet-free re-run this probe
had originally nominated for that role **fired mid-write at 12:04Z and narrowed rather than raised** — one
parameter shape came back a per-parameter zero and the other returned a Kentucky court docket — so corporate
print's residual upside now sits in the title/creator shapes never asked (FETCH REQUEST 4) plus
`harvest_mine.py --company humana`, which the orchestrator has not yet run for this slug. Second route: FETCH
REQUEST 2 (`micro_IA40385011_1273`), the only identified third-party document with an in-window catalogue date,
which names the brand attached to **hospitals** and bears directly on conflicts U.1/U.2. No route can make
families (b) or (e) count for Stage 1: a 1961-1983 origin has no web-archive coverage, and no
auction/museum/manuscript task has ever been authored for this company.

STATUS: WRITTEN — end of dossier.
