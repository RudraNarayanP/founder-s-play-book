# A_chronology_feasibility.md

# A — Chronology feasibility probe: Citigroup (rank 24)

Owner: `probe-citigroup`. Stage-1 PROBE only. No volume, no registers, no certification.
Company dir (absolute): `E:\founder's playbook\founders_playbook\01_companies\company_024_citigroup`
All `sources/...` paths below are relative to that directory.

**CONFIDENCE CAP (binding on every line here).** Of the **7** Internet Archive sidecars
(`sources/**/*.meta.json`; **47** such files exist after this pass, 40 of them from `sources/sec/`),
**6 carry `"transport": "UNVERIFIED TLS -- re-check before citing at High confidence"`** — including
`nationalbanksofu00firs`, the 1812 carrier, and all five pre-existing layers. The single exception is
`nationalcitybank00nati_0_djvu.txt`, whose sidecar reads **`transport: verified TLS`** (it was fetched
without `--insecure`). Check command: per-file `json.load(...)['transport']` over
`sources/periodicals/*.meta.json` and `sources/corporate_print/*.meta.json`.
Nothing in this dossier is stated above Medium. Layer-level statements are checkable because the line
numbers are printed here, but for the 6 unverified layers the byte identity between a held layer and the
live archive item is asserted only as "as fetched".


**STATUS: WRITTEN** (sections 1-7 + `## Untried`).

---

## 0. Counts, each with the command that produced it

| count | value | command |
|---|---|---|
| files in the company dir before this pass | **12** | `find <dir> -type f \| wc -l` |
| distinct text layers before this pass | **5** (`.txt`, 3 of them one item ×2 paths + 1 CIA) | same, filtered `*.txt` |
| SEC docs now held | **45** files (85 incl. sidecars) | `python -c` glob `sources/sec/*` minus `.meta.json` |
| SEC bytes stored | **4,561,295 B / 299,302 words**, 40 documents | `python tools/sec_intake.py auto "Citigroup" --company-dir <dir>` run summary |
| filings enumerated | **29,667 rows**, 0 dropped for no accession, 0 without `primaryDocument` | same run; artefact `sources/_index/submissions_CIK0000831001.csv` |
| enumeration date span | **2024-04-17 → 2026-09-29** | min/max of `filingDate` over those 29,667 rows |
| harvest candidate rows for this slug | **111** of 2,598 | `csv.DictReader` over `founders_playbook/00_universe/harvest/candidates.csv` |
| candidate rows never mined | **105** | set-difference against `sources/harvest_mine/_index.json` item ids |
| layers fetched by this probe | **2** (`nationalcitybank00nati_0`, `nationalbanksofu00firs`) | `python tools/ia_text.py fetch --id <i> --company-dir <dir> --insecure` |

**CSV header enumerated before any field was read** (RD-124's rule 1). Actual header of
`00_universe/harvest/candidates.csv`, printed from `rows[0].keys()`:
`company, source_family, query, item_id, title, date_or_issue, url, snippet_or_hitcount, http_status, classification, retrieved_at`
— agrees with the brief's stated order.

**Two pre-existing counts are wrong and are corrected here, not inherited:**
1. `research/A4_harvest_mine.md` L5 says "**65 candidate rows** in the harvest index". Measured now:
   **111**. The A4 pass mined 6, so the untried remainder is **105**, not 58 (A4 L5).
2. A4 L21 says the entity vocabulary applied was `first national city bank` and `formerly known as` —
   i.e. **none of the eight vocabularies in this brief was ever grepped against the held bytes.** A4's
   three NULL verdicts (L26, L28, L29) are therefore NULLs *under that vocabulary*, and are not
   statements about the bytes. I re-grepped with all eight (command in §2).

---

## 1. What is in-window and held — everything cited here was opened

### 1a. The five layers that existed before this pass, re-grepped with the eight vocabularies

Command: per-file `re.sub(r'[^a-z0-9]+',' ',text.lower())` then `len(re.findall(re.escape(v), norm))`
over `sources/**/*.txt` for `v` in the eight vocabularies (punctuation → space, per RD-124 defect 2).

| file | bytes | what it actually is |
|---|---|---|
| `sources/corporate_print/CIA-RDP78-03985A000700030034-1_djvu.txt` | 3,780 as text | **0 hits on all eight vocabularies, and 0 on `new york`.** Read in full (214 lines). It is a CIA internal *personnel/travel-processing* survey: "…Duties and Responsibilities for the processing of Travelers" (L122-123), "13 positions in CM Travel…" (L105), signed by a Chief of Logistics and an Assistant Director (L179-185). OCR is badly degraded (L11-L31 are largely unrecognisable). The only legible date is the release stamp "Approved For Release 2002-06-26" (L1, L97); a candidate internal date "3 Jdi 1993" (L21) is **not readable enough to cite**. `Travelers` here means *people travelling*, not the insurer. **This is RD-124's bare-word class firing on a CIA artefact: it is classified `TIER1_CANDIDATE` in the harvest index and names no company at all.** |
| `sources/corporate_print/travelersaidsoci1921trav_djvu.txt` | 13,314 | "Travelers **Aid** Society of Boston, Inc. Annual Report 1921" (sidecar `title`). 17 hits `travelers aid`, **0** hits on every insurance/banking vocabulary. A charity for arriving passengers. **Not Travelers Insurance.** |
| `sources/periodicals/travelersaidsoci1921trav_djvu.txt` | 13,314 | **Byte-identical duplicate of the row above** — sha1 `680648c276fa…` for both, 608 lines each (hash command in §0). One item, two paths. It cannot be counted as two families, and the brief's "1921 Travelers-related volume" is this item. |
| `sources/periodicals/tassd_report_1915_djvu.txt` | 21,820 | "Travelers' Aid Society of **San Diego** Annual Report, 1915". 26 hits `travelers aid`, 0 on every banking/insurance vocabulary. Same false-ancestor class. |
| `sources/periodicals/micro_IA41153428_0048_djvu.txt` | 76,473 | **The one genuine ancestor naming in the pre-existing corpus.** L6 "The Travelers Insurance Companies Conference," L11 "**INSTITUTION Travelers Insurance Companies, Hartford, CT.**" L148 "conference held in New York in **February, 1982**", L2119 "Hartford, Connecticut 06115". It is a **U.S. Department of Education / ERIC reprint** (L75 "U.S. DEPARTMENT OF EDUCATION The Travelers") of a sponsored conference report on ageing. It carries **no incorporation date, no founding statement, no predecessor name** (grepped: 0 hits on `city bank`, `citicorp`, `citibank`, `1812`). It names the entity and its home city, at 1982. Nothing more. |

**Family attribution disagreement, recorded not resolved:** `sources/harvest_mine/_index.json` labels
items `travelersaidsoci1921trav`, `micro_IA41153428_0048` and `tassd_report_1915` as
`"family": "corporate_print"`, but the bytes sit under `sources/periodicals/` (two of them) —
and `travelersaidsoci1921trav` sits under **both**. A family verdict must be taken from the retrieval
route, not from the directory a file landed in.

### 1b. What the SEC intake put on disk, and what it proves

Registrant resolved: `identity: 'Citigroup' resolved to CIK 831001 (CITIGROUP INC) by name-exact`;
guard `ok`. Cover page of `sources/sec/0000950103-24-005422_0000950103-24-005422.txt` (read with line numbers):

```
L13 | COMPANY CONFORMED NAME:         CITIGROUP INC
L14 | CENTRAL INDEX KEY:              0000831001
L18 | STATE OF INCORPORATION:         DE
L19 | FISCAL YEAR END:                1231
L40 | FORMER COMPANY:
L41 | FORMER CONFORMED NAME:  TRAVELERS GROUP INC
L42 | DATE OF NAME CHANGE:    19950519
L44 | FORMER COMPANY:
L45 | FORMER CONFORMED NAME:  TRAVELERS INC
L46 | DATE OF NAME CHANGE:    19940103
L48 | FORMER COMPANY:
L49 | FORMER CONFORMED NAME:  PRIMERICA CORP /NEW/
L50 | DATE OF NAME CHANGE:    19920703
L52 | FILER:
L55 | COMPANY CONFORMED NAME:         Citigroup Global Markets Holdings Inc.
L56 | CENTRAL INDEX KEY:              0000200245
L60 | STATE OF INCORPORATION:         NY
```

The same chain is in `sources/_index/_registrant_CIK0000831001.json`, `former_names`:
`["CITIGROUP INC", "TRAVELERS GROUP INC", "TRAVELERS INC"]`.

Across all 45 stored SEC docs (whitespace-normalised grep):
**`city bank of new york` 0 · `national city bank` 0 · `citicorp` 0 · `travelers insurance` 0 ·
`city bank farmers` 0 · `american city bank` 0 · `first national city` 0 · `1812` 0**;
`travelers group` 14 (all of them this same cover-page FORMER COMPANY block); `citibank` 10
(underwriter/dealer references in 2024 prospectus supplements).

**This is the most consequential finding in the dossier.** The bytes that name today's registrant put it
on the **Primerica → Travelers Inc → Travelers Group → Citigroup** chain, and they do not name Citicorp,
Citibank-as-predecessor, or the 1812 City Bank at all. The 1812 line and the registrant line are, on held
evidence, **two different lineages that share a brand** — see §3.

### 1c. The two layers this probe fetched

**(i) `sources/periodicals/nationalcitybank00nati_0_djvu.txt` — 21,738 B, 500 lines — a FALSE NAMING, refuted by opening it.**
IA metadata title: "National City Bank of New York : annual meeting of shareholders, January 9, 1934";
metadata `year` **1856**. The layer is neither. Read at line level:
L1/L26 "ARTICLES OF ASSOCIATION", L15 "CITY OF NEW YORK", L20-21 "HOSFORD & CO., STATIONERS AND PRINTERS…
No. 6 G Wall Street", L23 imprint **"1 86 6."** (1866), L52-53 "The name of this Association shall be,
'**The National Bank, in the City of New York**'", L44-48 formed "pursuant to the provisions of the Act of
the Legislature of the State of New York, entitled 'An Act to authorize the business of Banking,'
**passed April 18, 1838**", L56-58 capital "**Fifteen Hundred Thousand Dollars**, divided into Thirty
Thousand Shares, of Fifty Dollars each", L91-94 commencing "the second day of January, one thousand eight
hundred and fifty-seven" and terminating "on and with the first day of January, one thousand *one* hundred
and fifty-seven" (internally contradictory — OCR-unreliable, **not usable as a date**), L406-409 directors
may "apply for, and accept, any Act or Acts of Incorporation for Banking purposes".
Grep on the opened layer: `national city` **0**, `city bank` **0**, `1934` **0**, `1812` **0**.
`list-files` returns **`"text_layers": 1`** — so there is no second pamphlet hiding behind the metadata title.
**Verdict: the item never names the lineage entity.** A `TIER1_CANDIDATE` whose *identifier itself*
(`nationalcitybank00nati_0`) is built from the wrong entity name — RD-121's "metadata is not evidence",
reproduced, and RD-124's trap one level higher up.
It is however the **only held state-charter-route artefact type**: printed articles of association under an
enumerated **New York State statute (1838)**, i.e. proof of what a New York charter document looks like
and where it lives — for a **different bank**.

**(ii) `sources/periodicals/nationalbanksofu00firs_djvu.txt` — 298,956 B, 11,337 lines — THE 1812 CARRIER.**
Fetched from `nationalbanksofu00firs` (IA copy of the 1910 volume that candidates.csv L723 flagged as
Google Books `wksuAAAAYAAJ`). Read at line level (whitespace-normalised; OCR double-spaces are why the
normalisation matters — see §2):
```
L29  | 1812-1910                                      (title page)
L32-34| The National City Bank / of New York           (title page)
L36  | MCMX                                           (1910)
L39  | The National City Bank of New York
L41  | Original Charter Dated 1812
L44-45| Capital Fully Paid $25,00(),0()0.  [OCR of $25,000,000]
L48-49| Surplus $25,000,000.
L52-53| Depository of the United States, / of the State and of the City of New York
L56  | James Stillman, Chairman of the Board           <- a ROLE, not a founder claim (RD-116)
L57  | F. A. Vanderlip, President                      <- a ROLE, not a founder claim (RD-116)
L226-227 | "The National City Bank of New York issues this a revised edition of the work"
L242-243 | "The National City Bank of New York is ambitious to be of the broadest possible service
           to the national banks of the country."
L5473-5476 | "Organized as the City Bank in 1812 with a capital of $500,000, this institution was,
             in 1865, converted into a national association under its present title."
L5481-5486 | "The capital of The National City Bank now stands at $25,000,000, and on June 30, 1910,
             the date of its latest statement, its combined capital, surplus and undivided profits were
             $30,741,636.36 and its deposits $243,808,089.16. Total resources, $308,889,343.64."
L5488-5490 | "Since December 21, 1908, The National City Bank has occupied the block facing on Wall,
             William, Hanover Streets and Exchange Place."
```
Contents list L256-300 supplies the **mechanism vocabulary of the era** with page numbers: "Detailed Steps
in Organization 1", "**CONVERSION OF STATE BANKS 17**", "Reorganization of Private Banks 21",
"Consolidation 22", "Extension of Corporate Existence 113", "Change of Name or Location 127",
"Liquidation 130". That is a carrier-backed frame for the 1812→1865 conversion without importing any date.

**One lineage, not three witnesses.** `L29`, `L39/L41` and `L5473` are three statements in **one document**;
and the three artefacts — Google Books `wksuAAAAYAAJ` (candidates.csv L723), IA `nationalbanksofu00firs`
(held), IA `nationalbanksofu00firsrich` (search hit) — are the **same 1910 work**, not two witnesses.
Corroboration count for the 1812 claim on held evidence: **1**.

---

## 2. The eight vocabularies, tested separately: which entity each names, and at what date

Grep command for the held-bytes column: as §1a (whitespace-normalised whole-text, then
`re.findall(re.escape(v), norm)`), run over **all 7 held layers** including the two fetched here.
Search column: `python tools/ia_text.py search --q '<title:"…" AND mediatype:(texts)>' --rows 3 --insecure`
— **no `YEAR:` facet anywhere, per RD-130.**

| vocabulary | hits in held bytes | what the held bytes say | what the live IA title route returns (numFound) | naming verdict |
|---|---|---|---|---|
| **"City Bank of New York"** (the 1812 entity) | **0** | Nothing. The only bare predecessor naming anywhere is L5473 of the 1910 volume, which prints "**the City Bank**", *not* "City Bank of New York". My first grep of the 1910 volume returned 0 for this phrase and that was **my own defect** — OCR double-spacing; re-measured with `\s+` collapse it returns **12 lines**, and all 12 are substrings of "**National** City Bank of New York" (proved at L2518-2519, where the phrase wraps across a line break: "…of The National / City Bank of New York…"). L5346 "The **city bank** is bound to feel itself…" is a **common noun** (a city-based correspondent bank) — the RD-124 trap live in this very file. | **22**, but every surfaced item is *National* City Bank or *First National* City Bank; 15 of 22 printed before the tool capped output at **6,001 bytes** | **NO NAMING of the 1812 entity, in held bytes or on the surfaced part of the title route.** UNKNOWN beyond that. |
| **"National City Bank of New York"** | 12 lines (1910 volume only) | **The registrant's *brand* ancestor, not its legal ancestor.** Named by its **own** 1910 publication (L226-227, L242-243) at **1910**, with a self-declared origin at L41 "Original Charter Dated 1812" and L5473-5476 (1812, capital $500,000 → 1865 conversion). | **22** (same set — the phrase is a substring; **not an independent second route**) | **RETURNS — one lineage, 1910.** |
| **"Citicorp"** | **0** | Absent from every held byte, including all 45 SEC files. | **115**, top hits are **U.S. Reports case captions** (`Citicorp Industrial Credit, Inc. v. Brock, 483 U.S. 27 (1987)`; `Citicorp Venture Capital… v. Committee of Creditors`, 2003) and `gov.uscourts.*` — litigation captions, no corporate print. | **UNANSWERED for the corporate-print sub-route** (title route surfaced court captions; `Citicorp annual report` title query → **numFound 0**, a title-only perimeter, not a corpus statement). No held naming of Citicorp at any date. |
| **"Travelers Insurance"** | 6 lines (1982 doc) | **The only ancestor that is on the registrant's own EDGAR name chain** — via `Travelers Inc` (1994-01-03) / `Travelers Group Inc` (1995-05-19). Named as "**The Travelers Insurance Companies**, Hartford, CT" at **1982** in a Dept-of-Education conference reprint. No date of formation, no predecessor, no merger language. | **240**, but the surfaced top hits are **1889 Bagehot works "published by the Travelers…"** (a travelers'-aid society publisher) and 1994 case captions (`New York State Conference of Blue Cross & Blue Shield Plans v. Travelers Insuran…`). `title:("travelers insurance") AND title:(annual)` → **numFound 0**. | **RETURNS (held, 1982) for the naming; RETURNS-NOTHING-WITH-PERIMETER (title-only, no YEAR facet) for Travelers annual reports.** |
| **"Travelers Group"** | 14 files (SEC cover pages) | **EDGAR's own identity block: this is a FORMER CONFORMED NAME OF THE REGISTRANT**, date of name change **1995-05-19** (L41-42). This is the strongest held statement in the corpus about the modern company's legal continuity. | **3** — all court captions (`Dubos Refinishers v. St. Paul Travelers Group`, `Hardy v. The Travelers Group`). | **RETURNS — 1995-05-19, registrant-level, filings family.** |
| **"Citibank"** | 10 hits / 6 SEC files, 2024 | Underwriter/dealer references in 424B2 filings; **no predecessor narrative, no founding claim.** | **1,515** — dominated by `gov.uscourts.*` captions (`Citibank, N.A. v. Brigade Capital Management`) and `LFAID0058 "Citibank Style"`. | **RETURNS at 2024 only (registrant's present subsidiary naming). UNTRIED for pre-1998 Citibank print.** |
| **"City Bank Farmers Trust"** | **0** | Absent from every held byte. | **9** — `citybankfarmerst02newy` / `03newy` (**1920**, "City bank farmers trust company, New York") and `City Bank Farmers Trust Co. v. McGowan, 323 U.S. 594 (1945)`. **Independently corroborated by another company's tree:** `company_047_boeing/sources/corporate_print/boeing1934_djvu.txt` **L118** and **L122** print "City Bank Farmers Trust Company, New York" and "The National City Bank of New York, New York" (same pair at boeing1935 L770/774, 1937 L5796/5800, 1938 L1012/1015, 1939 L992/995, 1940 L952/1264/1269). | **UNTRIED for this company** (bytes reachable by `ia_text.py fetch`, never fetched into company_024). The cross-company namings are **read-only pointers, not citigroup family evidence** — see §4 caveat. |
| **"American City Bank of Houston"** | **0** | Absent. | **0** on the title route. | **RETURNS-NOTHING-WITH-PERIMETER** (title-metadata only; the `text:` field in IA advancedsearch matches **ANNOTATIONS, not the OCR layer** — stated in all 7 sidecars — so a title zero is not a corpus-wide zero). |

**Which registrant does each name — stated plainly, because this is the failure the project keeps paying for:**
- **Travelers Group Inc / Travelers Inc / Primerica Corp /NEW/** name **CIK 0000831001, the present registrant**, at 1995-05-19 / 1994-01-03 / 1992-07-03 (`sources/sec/0000950103-24-005422_….txt` L40-50). This is a **NAME-CHANGE record, not a founding act**.
- **The National City Bank of New York** (1812 City Bank → 1865 conversion) names **a bank that is not this registrant on held evidence**; it is the *brand* ancestor. Its own CIK is not in any held byte; CIK 831001's former names do not include it.
- **Citigroup Global Markets Holdings Inc., CIK 0000200245, incorporated NY** (same file L55-60) — a **co-registrant** on the same 2024 prospectus, and the only held artefact showing a **New York-incorporated** entity in the family. Relevant to the state-charter route, but at 2024, not 1812.
- James Stillman (Chairman) and F. A. Vanderlip (President), 1910 volume L56-57: **roles, not founders.** Refused as founder claims per RD-116. (Vanderlip appears a second way in the candidate index — `vanderlipfrankar00amer`, 1953, "Vanderlip, Frank Arthur, **1909-1914 (President, National City Bank of New York…)**", an ANS correspondence collection. Also a role.)

---

## 3. The load-bearing question, answered from held bytes

> *Does the corpus hold ANY document naming City Bank of New York in 1812, or is the 1812 date carried
> entirely by later self-narrative?*

**Answer: the 1812 date was carried entirely by a tool constant, and is now carried by a 1910 self-narrative. It has no 1812 carrier and no carrier naming the entity as "City Bank of New York" at all.**

Three separate measurements, in the order I made them:

1. **Before this pass, nothing carried 1812.** `1812` occurs **0 times** in all 5 pre-existing held layers
   (line-scan command in §1a). The universe index (`00_universe/fortune_top_50_2026.csv`, the Citigroup row)
   carries **no founding-date column at all** — its header is
   `rank, company, revenue_usd_millions, revenue_fiscal_year, profit_usd_millions, hq_city, hq_state,
   fortune_industry, universe_source_url, verified_by_second_source, confidence, notes`.
   The date's **only** source in the repository was `tools/harvest_mine.py` **L60**:
   `"citigroup": ("1812-01-01", "1998-12-31"), "homedepot": …` — a **search parameter, not evidence**.
   The file's own header comment (L45-47) says the windows are "deliberately WIDE **where the founding date
   is itself unestablished in our corpus**", which is the tool admitting it.
2. **Still no 1812 document, and still no "City Bank of New York" naming**, after the two fetches (§2 row 1).
   The phrase never appears as the 1812 entity's name in any held byte; every match is the *National* City
   Bank substring or the common noun.
3. **But a carrier for the *claim* now exists, and it is self-narrative.** `sources/periodicals/nationalbanksofu00firs_djvu.txt`
   L41 "Original Charter Dated 1812" and L5473-5476 "Organized as the City Bank in 1812 with a capital of
   $500,000, this institution was, in 1865, converted into a national association under its present title",
   in a volume **issued by the bank itself** (L226-227), printed MCMX (L36).

So the 1812 date moves from **no carrier of any kind** to **one dated Tier-1 self-narrative carrier at 1910,
corroborated once, describing a charter it does not reproduce.** That is exactly the UnitedHealth pattern in
RD-116 ("still company self-narrative, but a dated Tier-1 carrier where A had none") — and the Target/B1
warning still binds: **a self-narrative at 1910 about 1812 is not a 1812 document**, and the 1865 conversion it
asserts is likewise asserted, not evidenced. The charter itself is a **New York State artefact** (§4 route (f)).

---

## 4. Family verdicts (a)-(e), plus (f) the state-charter route

Per RD-097, all five families were searched or explicitly recorded UNTRIED before any depth verdict.
`periodical_harvest.py` was **not run** (live merges race it on `candidates.csv`), so every route that tool
owns is reported UNTRIED with its command rather than as a null.

**(a) FILINGS / EDGAR — RETURNS, with a measured hard perimeter at 2024-04-17.**
45 files / 4,561,295 B stored. Registrant identity, former-name chain and the NY-incorporated co-registrant
all come from here (§1b) — this is the family that produced the dossier's most consequential finding.
But the **enumeration spans 2024-04-17 → 2026-09-29 only**, measured per source slice:

| slice (`source` column) | rows | from | to |
|---|---|---|---|
| `recent` | 13,445 | 2025-09-29 | 2026-09-29 |
| `CIK0000831001-submissions-001.json` | 2,006 | 2025-07-23 | 2025-09-26 |
| `-002` | 2,002 | 2025-04-30 | 2025-07-22 |
| `-003` | 2,007 | 2025-02-27 | 2025-04-29 |
| `-004` | 2,072 | 2024-12-26 | 2025-02-26 |
| `-005` | 2,002 | 2024-10-25 | 2024-12-23 |
| `-006` | 2,006 | 2024-08-20 | 2024-10-24 |
| `-007` | 2,075 | 2024-06-27 | 2024-08-19 |
| `-008` | 2,052 | 2024-04-17 | 2024-06-26 |

**The walk stopped because the tool stops, not because the archive does.** `tools/sec_intake.py` L183
`def submissions_index(cik, max_slices=8)` and L202 `for f in files[:max_slices]` — and the only caller,
L1240 `submissions_index(a.cik)`, **passes no `max_slices` and exposes no CLI flag for it**. For a filer at
~2,050 filings per ~9-week slice, 8 slices buy 2.5 years; reaching the 1998 merger needs dozens more.
The tool's own docstring (L184) still claims "the `recent` block stops ~2001" — stale for this filer.
So: **0 filings held in any of the three stage windows**, and pre-2024 EDGAR is **UNTRIED, not absent**.

**(b) WEB ARCHIVES (Wayback / live-web capture) — UNTRIED.** No tool in this repository reaches a
capture-timestamp index for this slug, and the probe ran **0 WebSearch/WebFetch** (brief). Per RD-097 the
family floor is ~1996-12-29 anyway, so it could not touch Stages 1-2, and Stage 3's 1998-11-30 merger sits
just inside it. **This is an untried family, never a null.**

**(c) PERIODICAL CORPORA (IA texts / HathiTrust / Google Books / Chronicling America) — RETURNS.**
The 1910 volume (298,956 B, L29/L41/L5473) and the 1982 Travelers reprint are held through this route;
12 IA title-route queries run this pass (§2 table). Sub-routes never touched for this slug:
HathiTrust (1 candidate row), Chronicling America (4 rows), Google Books text (15 rows — including
`wksuAAAAYAAJ`, whose page PA238 the harvester itself flagged) — **UNTRIED**, and the `periodical_harvest.py`
query block that owns them was deliberately not run. Output cap noted: the title-route search returned
**15 of 22** surfaced items before stdout was cut at 6,001 bytes, so "every surfaced item is a
National/First-National match" is a statement about **the surfaced 15**, not the 22.

**(d) DIGITISED CORPORATE PRINT — RETURNS, but thinner than the label suggests.**
Genuinely company-issued print held: **one item** (the 1910 volume, issued by the bank, L226-227) plus
**one sponsored-reprint** (1982 Travelers, L11). The three items that the harvest index calls
`corporate_print` and that were fetched earlier are **not this company's print**: a Boston travelers'-aid
society (1921), a San Diego travelers'-aid society (1915), and a CIA travel-processing memo — all
RD-124 false ancestors, and the 1921 one is byte-duplicated across two directories (§1a).
Untried corporate print: `Firs2314_1969_0` and `Firs2314_1967_0`, metadata-titled
"First National City Bank - Annual Report (1969)/(1967)" — **the highest-value unopened bytes for this slug**;
also `citibankralphnad00lein` (1973) which is **not** the id the harvester tried
(it tried `citibankralphnad0000unse`, HTTP 401 → correctly UNANSWERED), and `cia-readingroom-document-c`
(1960, "TRIP REPORTS FOR IGU TRAVELERS" — expected to be another bare-word artefact).

**(e) AUCTION / MUSEUM DOCUMENTARY SALE RECORDS — UNTRIED.** No tool reaches a sale-room or accession
catalogue for this slug; the probe ran no web calls. RD-097 and §14(6) make this family a tier input in its
own right (Apple, Walmart, Berkshire all moved on it). **Untried.**

**(f) NEW YORK STATE CHARTER ROUTE — UNTRIED, and it is the only route that can produce a non-self-narrative
1812 record.** An 1812 charter is a **state legislative act / Secretary of State filing**: not an SEC artefact
(family (a) floor 2024), not an IA item (families (c)/(d) reached only *printed* surrogates), not a web
capture. Held evidence for what such a document looks like is the **1838-Act articles of association**
(§1c item i, L44-48) — a same-state, same-institution-type carrier, eleven years before the 1865 conversion,
and for a different bank. No command in `tools/` reaches a New York State archive; the correct finding is
**UNTRIED with the route named** (`## Untried` U-6), not a null.

---

## 5. Per-stage tiers, measured against each stage's own window (RD-112)

A tier is issued **per stage**, never as a property of the company. "In-window" below means a **document
whose own printed/metadata date sits in that stage's window** and which carries a naming of a lineage
entity at Tier-1 strength — a 1910 retrospective about 1812 is **not** a Stage-1 document.

| stage | window | families returning in-window Tier-1 text | tier | §15.2 deliverable / budget |
|---|---|---|---|---|
| **Stage 1** | 1812-01-01 → 1865-12-31 | **0 of 5.** (a) floor 2024; (c)/(d) nearest held artefact is 1866 *and names a different bank*; (b),(e),(f) untried. | **T3** | short narrative + registers; §K, §N, §U still mandatory; **8k w/stage, ≈3-4 agent runs** |
| **Stage 2** | 1865-01-01 → 1977-12-31 | **1** — (c)/(d) the 1910 volume (self-issued, L41 + L5473-5476 + a 1910-dated financial statement at L5481-5486). One item; the same work across GB/IA copies is **one lineage**. (a) no, (b) untried, (e) untried. | **T3 (PROVISIONAL — may reach T2)** | as above, 8k w/stage; **flip condition:** `Firs2314_1967_0` + `Firs2314_1969_0` + `reprintofoctober00nati` (1912) + `pendingbankingle00nati` (1913) opened as corporate print *distinct from* the periodical route → 2 families → T2. |
| **Stage 3** | 1977-01-01 → 1998-12-31 | **1** — (c)/(d) the 1982 Travelers Insurance reprint (L6, L11, L148, L2119). (a) **fails this window too**, despite the 1998 merger being the registrant's actual birth: EDGAR holds nothing before 2024-04-17. | **T3 (PROVISIONAL)** | 8k w/stage, ≈3-4 runs; **flip condition:** pre-1998 EDGAR via the `files[]` walk past slice 008 (S-4/8-K for 1998-11-30) would make (a) a second family and this stage **T2 immediately** — the cheapest tier move in the corpus. |

**Planning tier = the minimum = T3** (≈3-4 agent runs per stage, 8k words per stage). Per RD-112, note
**which window** any future re-grade moved: a `Firs2314_*` fetch moves **Stage 2 only**; an EDGAR slice-fix
moves **Stage 3 only**; neither touches Stage 1, whose emptiness is structural (route (f)).

**Proposed windows (flagged as proposed, not applied).** The held record does not support one lineage across
1812-1998. It supports **two**, and they should be staged separately or Stage 1 will keep being written from
a 1910 pamphlet:
- **P-1 brand/ancestor line** — 1812 (asserted only) → 1865 (asserted) → **first evidenced document 1910**;
  proposed operating window **1900-1977**, i.e. where print actually exists. Stage 1 as briefed
  (1812-1865) should be authorised **UNKNOWN-first**, not narrative-first.
- **P-2 registrant line** — proposed window **1982-12-31 → 1998-12-31**, carriers: 1982 reprint (L11) →
  Primerica 1992-07-03 → Travelers Inc 1994-01-03 → Travelers Group 1995-05-19 (L42/L46/L50) → the 1998
  merger (name change **not present** in any held byte; see §6 Q2).
  Note EDGAR records **no 1998 former-name row at all** in this header — the chain stops at 1995-05-19 and
  the current name appears without a date. That absence is itself an open question, not a fact.

---

## 6. Load-bearing open questions

**Q1 — Which founding act has a carrier, and what kind of carrier is it?**
Only two candidate acts exist in the corpus: the **1812 charter** and the **1865 national conversion**.
Both are carried **only** by `nationalbanksofu00firs` L5473-5476 — a 1910 statement by the entity about
itself. **No third-party, no state, no contemporaneous carrier for either.** Still open: whether an 1812
New York charter survives anywhere a listed route can reach (U-6).

**Q2 — Which entity does each later name descend from, and *by what document*?**
- Per **family (a)**, `Citigroup Inc` descends from `Travelers Group Inc` ← `Travelers Inc` ←
  `Primerica Corp /NEW/` (L40-50), with **no 1998 date and no Citicorp row**. Document = EDGAR cover-page
  FORMER COMPANY block; note EDGAR records the **date SEC recorded the change**, which is not necessarily the
  corporate effective date — do not silently convert one into the other.
- Per **family (c)/(d)**, `The National City Bank of New York` descends from `the City Bank` (1812,
  $500,000) by the bank's own 1910 statement (L5473-5476).
- **The link between these two chains is held by NOTHING.** No byte names Citicorp; no byte says Citibank,
  National City Bank, or Citicorp is an ancestor, predecessor, or party to a merger of CIK 831001.
  Whether the 1998 merger put the *banking* line into the *Travelers* registrant or into a subsidiary
  (e.g. CIK 200245, the NY-incorporated co-registrant) is **UNANSWERED**. This is the single highest-value
  open question in the dossier and the classic founder-claim trap: **stitching the 1812 City Bank into
  CIK 831001's founding on brand continuity would be an invented claim.**
- `First National City Bank` (the post-1961 name) is named in held bytes only as an **adjudicated caption**,
  `First National City Bank of New York v. Internal Revenue Service`, `micro_IA40386420_0119`, 1959 in the
  index (metadata date; the case is cited 1959-1960 — **not opened, so do not date it**).

**Q3 — First real experiment.** **UNANSWERED.** No held byte describes any venture, product, branch,
acquisition or format attempt by any lineage entity. The 1910 volume's contents list (L256-300) supplies
*sector machinery* ("Conversion of State Banks 17", "Reorganization of Private Banks 21", "Consolidation 22")
which is **institutional context, not this entity's experiment** — RD-127's sector-vs-naming distinction.
Route: `Firs2314_1967/1969` annual reports (U-2) are the likeliest carriers.

**Q4 — First repeatable validation.** **UNANSWERED.** Nothing held shows a result repeating. One
*checkable* near-miss worth a later pass: the 1910 volume prints a **dated statement of position**
(L5482-5486, "on June 30, 1910… capital, surplus and undivided profits $30,741,636.36… deposits
$243,808,089.16… total resources $308,889,343.64") — the first *periodic disclosure* carrier found, and the
OCR of the title-page capital reads `$25,00(),0()0.` (L45) against a clean `$25,000,000.` at L5481/L49:
**a figure to be footed, not quoted** (RD-131's `S`-for-`$` class; here `(` for `0`).

**Q5 — First incurred failure, and the 1930s insolvency/reorganisation candidate.**
**UNANSWERED — and explicitly NOT imported from general history.** Measured over **21 held `.txt` layers**
(whole-text, whitespace-normalised, count per term):
`insolven` **20 — every one inside a 2024 SEC prospectus** (generic issuer/guarantor boilerplate);
`receivership` **0**; `in receivers` **0**; `failed bank` **0**; `bank failure` **0**; `reorganis` **0**;
`reorganiz` **16** (8 of them the 1910 volume's own machinery headings, e.g. contents "Reorganization of
Private Banks 21" at L264); `panic` **2**, `suspended` **1**, `depositors` **3**, `emergency` **3**, all four
in the 1910 volume; `1933` **28** but **all** are "1933 Act" Securities-Act references in SEC files;
`1932`/`1934`/`1935` **0**.
**No held byte names an insolvency, receivership or reorganisation EVENT for any lineage entity.**
The failure-adjacent text that does exist is **sector language inside a banking manual and is refused as
entity history**: L5340 "embarrassed from any cause"; L5346-5349 a city bank's care over accepting a
respondent's responsibility; contents "Liquidation 130" at L298; and the two `panic` lines —
**L2275 "THE panic of 1907 was followed by an …"** and **L2991 "a distressing panic ensued. President Van …"**
(a Van-Buren-era, i.e. 1837, passage). The volume's eight `1930` hits are **bond maturities, not years of
events** — "2% Consols payable after 1930" (L1245), "the 2 per cent Panama Canal Bonds" (L1626),
"2 per cent bonds of 1930, bought March 1," (L1950) — and reading them as dates would manufacture a 1930s
narrative out of a securities table.
Recording a 1930s bank failure as this lineage's incurred failure from memory would be exactly the
RD-127/RD-124 error; it stays UNKNOWN until a carrier is opened. Routes: U-2 (annual reports), U-5
(HathiTrust/periodical block), and the 1933-34 Comptroller-of-the-Currency / FDIC print a sector search
would surface.

**Q6 — Is the registrant's own birth (the 1998 merger) carried by anything?** **UNTRIED.** No held byte
mentions 1998-11-30, the merger, or an exchange ratio. The whole of Stage 3's most important event is
currently carried by the brief's own framing. Route: U-1.

---

## 7. What this probe refused to claim

1. **Refused: 1812 as a founding date of this registrant.** Kept as one 1910 self-narrative (L41/L5473) about
   a **different legal person** from CIK 831001 on held evidence. → §6 Q2.
2. **Refused: "Citigroup = Citicorp + Travelers, 1998" as a founding act.** No held byte names Citicorp; the
   registrant's former names are Travelers Group/Travelers Inc/Primerica.
3. **Refused the 1921 "Travelers" volume as an ancestor** — Travelers **Aid** Society of Boston; refused
   tassd_report_1915 likewise. Refused to count the byte-identical 1921 duplicate as two families.
4. **Refused the CIA document as a naming.** 0 hits on all eight vocabularies; "Travelers" = travellers.
   Also refused to date it (`3 Jdi 1993`, L21, unreadable; only the 2002-06-26 release stamp is legible).
5. **Refused `nationalcitybank00nati_0` as evidence** after opening it: 0 `national city` / 0 `city bank` /
   0 `1812` on its only layer, imprint 1866 (L23), entity "The National Bank, in the City of New York"
   (L52-53). Its `TIER1_CANDIDATE` label and its **identifier** are both metadata fictions.
6. **Refused the harvester's promoted-entity string as a printed quotation.** candidates.csv L723 records the
   matched entity as "**First National City Bank of New York**"; the query was
   `GB Citigroup / 'First National City Bank' annual report shareholder`, and the opened 1910 page prints
   "**The** National City Bank of New York". `first national city` = **0** hits in the volume.
   **The column echoes the query, not the page** — RD-124, confirmed on a Google Books row.
7. **Refused Stillman and Vanderlip (L56-57) as founders** — roles only (RD-116).
8. **Refused to date anything from `date_or_issue`** — index dates are scan/upload years (RD-121); ranked,
   never filtered. The 1856-vs-1866 mismatch on `nationalcitybank00nati_0` is the case in point.
9. **Refused to call pre-2024 EDGAR, Wayback, HathiTrust, Google Books text, Chronicling America, auction/museum,
   or the NY State charter "absent".** All UNTRIED; each has a command in `## Untried`.
10. **Refused the zero on "American City Bank of Houston"** as a corpus statement — title-metadata only, and
    IA `text:` matches annotations, not layers (all 7 sidecars).
11. **Refused `travelers insurance` numFound 240 / `citibank` numFound 1,515 as yield.** Top surfaced hits are
    1889 aid-society imprints and US Reports captions; **numFound is a search signal, never a count of
    evidence** (RD-121 rule 2).
12. **Refused to state a confidence above Medium** anywhere in this file (UNVERIFIED TLS in every sidecar).
13. **Refused to run `periodical_harvest.py`** (live merges) and refused to touch `tools/`, the log, or any
    other company's tree; the Boeing/Chevron/ExxonMobil namings in §2 are **read-only pointers** and are
    deliberately excluded from every family verdict and every tier here.
14. **Refused to mint source ids, write registers, or certify depth.** No volume authored.

## Untried

Every route below is a search never run, not a null. Commands are as corrected for this repository.

- **U-1 EDGAR pre-2024 (highest value / cheapest tier move — the 1998 merger itself).** Blocked in the CLI:
  `tools/sec_intake.py` L183 `submissions_index(cik, max_slices=8)`, L202 `files[:max_slices]`, caller L1240
  passes none. **Orchestrator action (tool change, not agent work):** expose `--max-slices` (or default to
  `len(files)`), then `python tools/sec_intake.py auto "Citigroup" --company-dir <dir> --from 1994-01-01 --to 1998-12-31 --max-docs 40`.
  Expect the 1998 S-4/8-K and Citicorp-era documents; **do not re-run `index` for another company without
  the CIK-keyed artefacts** (RD-098/RD-112 footgun — paths are already CIK-keyed here, and `legacy_copy_written: true`
  wrote an unkeyed `submissions.csv` alongside; note it).
- **U-2 Corporate print, First National City Bank annual reports (Stage 2 → could make it T2).**
  `python tools/ia_text.py fetch --id Firs2314_1969_0 --company-dir <dir> --insecure` and
  `python tools/ia_text.py fetch --id Firs2314_1967_0 --company-dir <dir> --insecure`;
  then `python tools/ia_text.py mine --company citigroup --limit 12` (via
  `python tools/harvest_mine.py --company citigroup --limit 12`) to clear the other **105** candidate rows.
  **Before grepping, add the eight §2 vocabularies to the slug's entity list** — A4 mined with
  `first national city bank` / `formerly known as` only (A4 L21), which is why three NULLs were recorded
  against bytes that had never been tested for `city bank`, `travelers insurance` or `1812`.
- **U-3 Nader-era critical print (third-party witness — the only *non-self-narrative* Stage 2 candidate).**
  `python tools/ia_text.py fetch --id citibankralphnad00lein --company-dir <dir> --insecure`
  (1973, "Citibank; Ralph Nader's Study Group report on First National City Bank"). Note the earlier 401
  was on a **different id**, `citibankralphnad0000unse` → that remains UNANSWERED, not NULL.
- **U-4 Bound-run enumeration before judging any IA item.**
  `python tools/ia_text.py list-files --id <identifier> --insecure` then
  `python tools/ia_text.py fetch --id <identifier> --file <layer> --company-dir <dir> --insecure`.
  A bound volume can hold one layer per year (1921's duplicate proves the path-collision half of this).
- **U-5 Periodical corpora whose query block this probe was forbidden to run.**
  **UNTRIED by policy:** `python tools/periodical_harvest.py …` was not executed (it races live merges on
  `candidates.csv`). HathiTrust: **1** candidate row; Chronicling America: **4** rows; Google Books text:
  **15** rows incl. `wksuAAAAYAAJ` page **PA238** (URL in candidates.csv L723:
  `https://books.google.com/books?id=wksuAAAAYAAJ&pg=PA238`). Re-check every faceted zero per RD-130 before
  any of them becomes a null.
- **U-6 New York State charter route — the only path to a non-self-narrative 1812 record.**
  No tool in `tools/` reaches it: `sec_intake.py` is floor-2024, `ia_text.py`/`harvest_mine.py` reach
  printed surrogates only. **Named as an intake gap for the orchestrator, not attempted:** an NYS
  Department of State / legislative charter lookup for "City Bank of New York", 1812, plus the 1838
  "Act to authorize the business of Banking" filings whose form is now held
  (`nationalcitybank00nati_0` L44-48). Until it exists, Stage 1 has **no reachable primary route** and the
  correct verdict is UNTRIED with this command gap recorded.
- **U-7 Auction / museum documentary sale records (family (e)).** Never searched for this slug; no tool and
  no web budget. Under §14(6)/RD-097 this family has flipped tiers before (Apple, Walmart, Berkshire).
- **U-8 Web archives (family (b)).** Never searched; floor ~1996-12-29, so it bears on Stage 3's 1998 merger
  only. No tool owns it in this repository.
- **U-9 CIA reading-room second item** `cia-readingroom-document-c` (1960, "TRIP REPORTS FOR IGU TRAVELERS"),
  expected to be a bare-word artefact — worth opening **only to confirm the class**, not as evidence.
- **U-10 Cross-company pointers already on disk (read-only; do NOT import into company_024 tiers).**
  Earliest namings of the ancestor entities anywhere in the repository, found by
  `Grep -i 'City Bank of New York|National City Bank of New York|City Bank Farmers Trust' founders_playbook/`:
  `company_047_boeing/sources/corporate_print/boeing1934_djvu.txt` **L118, L122** (1934) and siblings
  1935/1937/1938/1939/1940, plus `company_021_chevron/sources/periodicals/standard-oil-company-of-california-annual-report-1956_djvu.txt`
  **L3313** and `company_009_exxonmobil/.../1959` **L3211** (as "**First** National City Bank of New York",
  1956-1960). These are **transfer-agent / depository references inside other registrants' reports** — they
  name the entity at 1934-1960, which is earlier than anything in this company's tree, and they are the
  strongest existing proof that the lineage entity is attested by **third parties** decades before anyone
  here has opened one. They belong to live other-company trees: cite as leads, never as company_024 evidence.

## 8. Corrections taken on this pass (mine, caught by re-measuring)

- **"0 hits for `city bank of new york` in the 1910 volume" was false** and was my own instrument: I grepped
  raw lines with single spaces while the OCR prints double spaces. Re-run with `\s+` collapse → **12 lines**.
  Conclusion unchanged, but only because the 12 are *National* City Bank substrings (proved at L2518-2519,
  where the name wraps across a line break). RD-124 defect 2 and RD-131 both, in one error.
- **"7 of 7 sidecars carry UNVERIFIED TLS" was false**: 7 IA-era sidecars, **6** UNVERIFIED + 1 verified TLS
  (`nationalcitybank00nati_0`). Corrected in the confidence cap. The 1812 carrier is in the UNVERIFIED set.
- **The Q5 insolvency claim was asserted before it was measured.** It is now measured (21 `.txt` layers, term
  counts in Q5); the verdict held, but the original sentence had no command behind it, which is exactly the
  RD-127 class ("three of my absence claims were false"). Rewritten.
- **`nationalcitybank00nati_0`'s `list-files` result (`"text_layers": 1`) means the false naming cannot be
  rescued by another layer of the same item** — the metadata title refers to content the item does not hold.
- **Legacy copy confirmed, not assumed:** `sources/_index/submissions.csv` and
  `submissions_CIK0000831001.csv` are **byte-identical** (sha1 `7faa12502aae…`, 2,417,275 B each), so
  `legacy_copy_written: true` is duplication, not a divergent second registrant. Harmless today; it is the
  RD-098 shape to watch if another slug shares the directory.
- **Two A4 numbers were superseded, not inherited:** 65 candidate rows → **111**; 58 untried → **105**.
  A4's three NULLs are NULLs *under its two-term vocabulary*, and are recorded as such here (§0, §2).

