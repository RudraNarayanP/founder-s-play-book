# A_chronology_feasibility.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:18:46Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

STATUS: WRITTEN

**TIER: T1 (exemplar-capable) — three of five families return in-window Tier-1 text, which is the
§15.2 threshold exactly, and the third one is the weakest of the three.**

| family | verdict | in-window Tier-1 text on disk |
|---|---|---|
| (a) filings | **TIER1_CANDIDATE** | S-1 2004-04-29 (367,767 words read), S-1/A lineage, 8-K, the Stanford patent-licence exhibit, the Overture litigation disclosure — 41 files / 10 accessions / 13 MB |
| (b) web archives | **TIER1_CANDIDATE** | google.com captured **19981111184551**; the capture's 212 bytes retrieved and read |
| (c) periodicals | **UNTRIED** | none — harvester has 0 Alphabet tasks |
| (d) corporate print | **TIER1_CANDIDATE** | CIA CREST Google Inc. beta-evaluation agreement, text layer downloaded (16,305 B), Nov 2004 |
| (e) documentary | **UNTRIED** | none — not attempted, budget choice |

**Implied agent-run budget: 15-20 runs, 60k words/stage cap** (§15.2 T1 row). I would plan against
the **lower half** of that band and say why: the T1 qualification rests on three families, and
(d) supplies one document dated 2004 — inside the window but at its far edge, doing nothing for the
1998-2003 origin stretch. Read the tier as **"T1 from the IPO end, thin at the founding end."** The
founding period is currently supported by exactly two independent artifacts — a patent filing
(1998-01-09) and an archive capture (1998-11-11) — plus one founder-claim document (the S-1). Family
(c), if configured, is the swing item: if it returns 1998-2003 contemporaneous text the tier holds
without qualification; if it returns nothing after a real try, the dossier stays T1 but Stage 1
should be written to the **T2 word cap (22k)** on its own merits rather than padding to 60k, since
§15.4 makes a missed length target legitimate and §10's research-debt triggers would otherwise fire
against a corpus that cannot support it.

**Why the brief's own framing nearly cost the project this company.** The instruction correctly
warned that the 2004 filer is "Google Inc." and not "Alphabet", but the *identifier* the scripted
pipeline reaches from the ticker — CIK 1652044 — returns a registrant whose enumerated history
starts 2023-06-29. Indexing it produced "0 documents stored, 0 skipped/unanswered" for 1998-2006,
which is precisely the shape of a documented absence. It took one EDGAR full-text search to produce
**"Google Inc. (CIK 0001288776)"**, whose CIK is *three digits away* from CIK 1288779, which belongs
to **Covenant Advantage Fund LLC** — the adjacent-number trap that turned the first `index` call into
an overwrite of this company's `_INDEX.md` with another entity's filings. Two lessons for the
playbook's method file, both cheap: resolve a legacy registrant by full-text search on its
**name**, never by CIK adjacency or by ticker-to-CIK for the renamed parent; and treat
`0 documents stored, 0 skipped/unanswered` from `auto` as an UNANSWERED signal, never as a null.

**Deliverable status:** this file is a tier verdict plus a source index, not a narrative. The five
gaps that must close before Stage 1 drafting (in priority order) are in *Untried* items 1, 4, 5, 3, 6.

## Entity question

STATUS: WRITTEN

**Settled: the EDGAR route for this company is one CIK, and the "obvious" second CIK is a
different company entirely.** Verified this session by `tools/sec_intake.py`:

| Test | Result as returned by the script |
|---|---|
| `resolve --ticker GOOGL` | `{"ticker": "GOOGL", "cik": 1652044, "name": "Alphabet Inc."}` |
| `resolve --ticker GOOG` | `{"ticker": "GOOG", "cik": 1652044, "name": "Alphabet Inc."}` |
| `index --cik 1288779` | `2 filings from Covenant Advantage Fund LLC` — REGDEX 2004-04-26, REGDEX/A 2008-06-03 |

CIK 1288779 is a 2004-vintage identifier whose first filing is dated 2004-04-26 — the exact
vintage one expects of the 2004 registrant — and it is **not** Google. Any probe that assumed a
"Google-era CIK" adjacent to Alphabet's and indexed it would have received two REGDEX rows,
reported "no S-1, no 10-K, no 10-Q", and produced precisely the false null this project has been
fooled by before. It is recorded here as a **negative artifact**, not as a null about Google.

**Consequence on disk, worth repeating:** that misfire overwrote
`sources/_index/_INDEX.md` of this company with Covenant Advantage Fund's index (its header read
`SEC submissions index -- Covenant Advantage Fund LLC (CIK 0001288779, )`). Re-running
`index --cik 1652044` restored the Alphabet index (header `Alphabet Inc. (CIK 0001652044, GOOGL)`,
1013 filings). A second CIK into the same `--company-dir` is a destructive act even when the CIK
is wrong; nothing was deleted, the correct index was re-materialised.

**AMENDED below after the first draft, which reported the entity chain as wholly UNKNOWN.**
The draft was written against one CIK and was then contradicted by evidence; the correction is kept
in place of the original wording rather than silently overwritten.

**Settled by document: the 2004 registrant is "Google Inc.", and its CIK is 1288776.** EDGAR
full-text search on the *name* (HTTP 200) returned `"display_names":["Google Inc.  (CIK 0001288776)"]`
with `file_num 333-117934`, `biz_locations Mountain View, CA`, `inc_states DE`. Indexing that CIK
gave **6407 filings, zero unanswered slices**, earliest S-1 2004-04-29 — so the brief's premise
about the *name* of the early filer is **confirmed**, and the brief's two dates are confirmed as
filing dates (1998-09 as incorporation month per the S-1's own text; the offering lineage runs
S-1 2004-04-29 → 424B4 2004-08-19).

**NOT settled: what CIK 1652044 (GOOGL/GOOG, "Alphabet Inc.") is to CIK 1288776.** Both names are
live in the pipeline; 1652044's history before 2023-06-29 sits in the one archive slice that
answered 404, so the 2015 event cannot be read from anything on disk. Two structures remain open —
the Google registrant was renamed and a second CIK was opened, or a new holding registrant was
created in 2015 and Google's own CIK continued filing. **UNKNOWN.** This matters beyond tidiness: a
dossier that indexed only 1652044 would conclude "Google never filed an S-1", and the brief's
instruction not to treat its dates as established is what caught it. The 424B1-vs-424B4 point and
the 1998 month-vs-day point are two further instances of the same correction (see *Conflicts* U-1).

## Family a filings

STATUS: WRITTEN — SUPERSEDES the first draft of this section, which reported this family as
UNANSWERED. It is now **TIER1_CANDIDATE**; the UNANSWERED finding is retained below because it is
a true finding about the *Alphabet* CIK, and it is the reason the entity question had to be solved.

### a.1 The route that did not work, and why it is kept

`index --cik 1652044` (Alphabet Inc., GOOGL/GOOG) returned **1013 filings, every row
`source = recent`, spanning 2023-06-29 → 2026-09-16**, and `_INDEX.md` recorded:

> `CIK0001652044-submissions-001.json` — UNANSWERED: HTTP 404

The script *does* follow archive slices (`sec_intake.py:110-135`, `max_slices=8`; its comment
records that the `/Archives/edgar/data/<cik>/` form 503/404s and "made `index` silently stop at
2020"), so the slice was requested and did not answer. Earliest-per-form on that CIK: 144 and 4
2023-06-29, 10-Q 2023-07-26, 10-K 2024-01-31, DEF 14A 2024-04-26, 8-A12B 2025-05-14 — **no S-1, no
424B1/424B4, nothing before June 2023**. That is an unanswered stretch of ~19 years of a registrant
that certainly filed through it, not an absence. `auto` on that CIK over the 1998-2006 window
returned `0 documents stored, 0 skipped/unanswered`, which is consistent (nothing in-window existed
*in that candidate set*) and must not be read as "the 2004 filing is gone".

### a.2 The route that worked

EDGAR full-text search (`https://efts.sec.gov/LATEST/search-index?q="Google Inc."&forms=S-1&
startdt=2004-01-01&enddt=2004-12-31`, HTTP 200, 123 hits) named the 2004 registrant and its CIK:

> `"display_names":["Google Inc.  (CIK 0001288776)"], "file_num":["333-117934"],
> "biz_locations":["Mountain View, CA"], "inc_states":["DE"]`

`index --cik 1288776` → **6407 filings, ZERO unanswered slices**, earliest per form:

| form | filed | accession | primary doc |
|---|---|---|---|
| REGDEX | 2001-03-12 | 9999999997-04-020668 | (SEC paper item) |
| 10-12G | 2004-04-29 | 0001193125-04-074059 | d1012g.htm |
| **S-1** | **2004-04-29** | **0001193125-04-073639** | **ds1.htm** |
| S-1/A | 2004-05-21 | 0001193125-04-093053 | ds1a.htm |
| 8-K | 2004-07-09 | 0001193125-04-115812 | d8k.htm |
| 10-Q | 2004-08-16 | 0001193125-04-141838 | d10q.htm |
| **424B4** | **2004-08-19** | 0001193125-04-143377 | d424b4.htm |
| **10-K** | 2005-03-30 | 0001193125-05-065298 | d10k.htm |
| DEF 14A | 2005-04-08 | 0001193125-05-072803 | ddef14a.htm |

**The brief's expected artifact is a 424B1. The index shows a 424B4 at 2004-08-19 and no 424B1
anywhere in 6407 filings.** A probe that had requested "the 424B1" by name would have returned a
documented null against a real document (see *Conflicts* U-1).

`auto --cik 1288776 --from 1998-01-01 --to 2006-12-31 --max-docs 30` put **41 document files across
10 accessions, 13 MB** into `sources/sec/`, each with a `.meta.json` sidecar. It was killed at my
590 s ceiling before writing `_MANIFEST.csv` (header row only), and the tenth accession
(0001193125-04-138034) contributed only its index page.

### a.3 What the S-1 says about 1998 — FOUNDER CLAIM in a Tier-1 wrapper

From `0001193125-04-073639_0001193125-04-073639.txt` (full submission text; 367,767 words
tag-stripped, searched this session):

- Corporate Information: *"We were incorporated in California in September 1998. In August 2003, we
  reincorporated in Delaware. Our principal executive offices are located at 1600 Amphitheatre
  Parkway, Mountain View, California 94043"* — **month-level, not day-level**; there is no founding
  day in this document.
- *"We began licensing our WebSearch product in the first quarter of 1999. We became profitable in
  2001 following the launch of our Google AdWords program."*
- Founders' letter (Brin's voice): *"Sergey and I founded Google because we believed we could
  provide a great service to the world—instantly delivering relevant information on any topic."*
- *"The first version of the PageRank technology was created while Larry and Sergey attended
  Stanford University, which owns a patent to PageRank. We hold a perpetual license to this patent.
  In October 2003, we extended our exclusivity period to this patent through 2011."*
- *"While we developed much of our ranking technology after the company was formed, PageRank was
  developed at Stanford University with the involvement of our founders, and was therefore published
  as research."*

**Lineage accounting.** S-1 (073639) + its amendments (093053, 105564, 116608, 124025, 131481,
134174, 135503) + the 424B4 (once fetched) are **ONE source**: one registration statement's
developing text. Nine accessions on disk must never be counted as nine corroborations of the
founding date. Independent corroboration for 1998 comes only from outside the lineage — see
*Registrations and trademarks* (patent US 6,285,999, filed 1998-01-09, assignee Stanford) and
*Family b* (google.com captured 1998-11-11).

Two in-lineage items are nonetheless separate *documents* for other claims, because they are
executed agreements or disclosed third-party acts rather than the company's narrative:
accession **105564** carries the Stanford–Google license text (*"STANFORD's U.S. Patent 6,285,999
filed January 9, 1998 and issued September 4, 2001... the Exclusive period for U.S. Patent 6,285,999
expires on September 4, 2011"*), and accession **135503** discloses litigation (*"Overture Services,
Inc., against us in April 2002 asserting that certain services infringed Overture's U.S. Patent
No. 6,269,361... we denied that we infringed the patent and alleged that the patent was invalid and
unenforceable"*, settled with a perpetual licence and mutual releases).

### a.4 XBRL

`facts --cik 1652044 --from 1998-01-01 --to 2006-12-31` printed a path and **wrote no file**
(`sources/financials/` was empty; contrast `company_017_meta`, where the file exists) — script
non-delivery, reported as such. Re-run on the correct CIK wrote **1 row**:
`StockholdersEquity, USD, end 2006-12-31, 17,039,840,000, fy 2009, form 10-K, accn
0001193125-10-030774, frame CY2006Q4I`. That is a 2006 balance restated inside a 2010 filing:
**RETROSPECTIVE SOURCE** under §6, and it establishes nothing about 1998-2003. Structurally,
in-window XBRL is a documented near-null.

**FETCH REQUEST (script-run, not agent web work):**
`auto --cik 1288776 --company-dir founders_playbook/01_companies/company_005_alphabet --from 2004-08-01 --to 2006-12-31 --max-docs 40`
to land the 424B4 (0001193125-04-143377), the FY2004 10-K (0001193125-05-065298), the FY2005/FY2006
10-Ks and the 10-Qs, then re-run to complete `_MANIFEST.csv`. Also `index --cik 1652044` retried
until `CIK0001652044-submissions-001.json` answers — that slice is what settles the 2015 renaming
question in *Entity question*.

## Family b web

STATUS: WRITTEN — **TIER1_CANDIDATE** (one in-window capture, returned; host intermittently
refusing, so coverage is incomplete).

Wayback CDX, `https://web.archive.org/cdx/search/cdx?url=google.com&fl=timestamp,original,statuscode
&limit=3&output=json`:

- Attempts 1 and 2 (`cdx_bare`, `cdx_www`): **HTTP 503**, body = IA "Temporarily Offline"
  maintenance page (11,832 bytes each). Retained as negative artifacts
  (`wayback/cdx_bare.json`, `wayback/cdx_www.json`, `.sidecar.json` records the 503). A 503 is
  UNANSWERED, and this project has been fooled by exactly this before.
- Attempt 3, bare host: **HTTP 200**, `wayback/cdx_retry.json`:
  `[["timestamp","original","statuscode"],["19981111184551","http://google.com:80/","200"], ...]`

**The trustworthy date is the 14-digit timestamp: 19981111184551 = 1998-11-11 18:45:51** — earliest
ascending CDX row for the bare host, statuscode 200. This is the single best in-window, non-filing,
non-founder artifact for the origin boundary: an unauthenticated third party (the archive) recorded
google.com publicly serving pages on that date. It is a *terminus ante quem*, not a founding date.

Fetched the capture itself: `https://web.archive.org/web/19981111184551id_/http://google.com/` →
HTTP 200, **212 bytes**, `wayback/google_19981111_raw.html` (+ sidecar with the capture timestamp and
the source CDX file). Full visible text:

> "Welcome to Google — Google Search Engine Prototype — Might-work-some-of-the-time-prototype —
> that is much more up to date."

Self-description as a *prototype* is contemporaneous and matters for the boundaries: on 1998-11-11
the company's own public page labelled the product unfinished. No experiment date, no user count,
no funding statement is recoverable from a 212-byte page.

**Unanswered within this family (do not report as absent):**
- `www` variant earliest capture — 503 on attempt 1 and again on the closing retry
  (`wayback/cdx_www.json`, still 503). The bare/www test is therefore **only half done**; I do not
  claim the two hosts share an earliest capture, and I do not claim `www.google.com` lacked an
  earlier one.
- Any capture *earlier* than 1998-11-11: `limit=3` ascending returned 1998-11-11 as first, which is
  a real earliest for this query shape, but `from=`/`to=` slices and the Stanford-host queries
  (`google.stanford.edu`, 503 — `wayback/cdx_stanford.json`) went unanswered.

## Family c periodicals

STATUS: WRITTEN — **UNTRIED.** Not a null, and not an error: the route exists, is the right route,
and has no Alphabet query loaded.

`python tools/periodical_harvest.py --help` confirms the tool supports both a company selector and
family selection (`--company COMPANY`, `--source-family FAMILY` repeatable, `--insecure-hosts`,
`--cache-dir` now off by default). It was then run for real, in dry-run so no request was spent:

| command | output |
|---|---|
| `periodical_harvest.py --company google --dry-run` | `PLANNED REQUESTS (0 tasks):` `Families: {}` `Companies: {}` |
| `periodical_harvest.py --company alphabet --dry-run` | identical: **0 tasks** |

The reason is in `tools/queries.json`: `tasks` is a list of 49 entries whose `company` values are
exactly **{walmart, apple, unitedhealth}** (verified by reading the file this session). The file's
own `_comment` says *"Add future companies by editing THIS data, not periodical_harvest.py"* — but
`tools/queries.json` is shared configuration that no probe may rewrite under §14 rule 4 (only files
named in the brief), so the addition is handed to the orchestrator rather than done here.

**What would be needed to close this family** (a config task, not a research task): Alphabet tasks
mirroring the apple/walmart shape across all six configured source families
(`chronicling_america`, `chronicling_america_ocr`, `internet_archive`, `corporate_print`,
`hathitrust`, `google_books`), with per-source caps raised to cover the new task count — the caps
note in `queries.json` warns that a cap below the task count writes `SKIPPED: per-source cap
reached` rows, i.e. it manufactures the unqueried-family-as-null error §14 rule 6 forbids. Queries
should carry the hyphen-free brand, the founders' names, the Stanford + PageRank pair, and a
`1998-2006` decade facet; the "paper only" presumption must not be asserted until this runs.

Prior status of the endpoints, from `tools/HARVEST_README.md` (read this session, not re-derived):
HathiTrust Babel **positive but intermittent** (200 five times in one window, 403-challenged in the
next, same URL bytes); Google Books legacy Atom feed **positive keyless**; the whole
`www.loc.gov` zone **answers a Cloudflare bot challenge to scripted clients**, so Chronicling
America rows are UNANSWERED by construction. For a 1998-2006 subject this family is less decisive
than it was for Walmart or Apple — those companies' origin decades were print-only, whereas
Google's sits inside the web-archive era that Family b already reaches. It is still the difference
between T1 and T1-plus, and it is where independent (non-company) text about 1998-2003 would come from.

## Family d corporate print

STATUS: WRITTEN — **TIER1_CANDIDATE.** Queried, as instructed, *before* any "paper only" assertion.

Internet Archive advancedsearch (`archive.org/advancedsearch.php`, HTTP 200 both times,
`ia/ia_corporate_print.json`, `ia/ia_annual_reports.json` + sidecars):

1. `q=title:(google) AND creator:("Google Inc.") AND mediatype:(texts)` → `numFound: 6`, and the
   docs are **off-target** (a 2011 Chrome offline installer, a 2014 Google Books item, a 2016
   election item). The phrase quoting collapsed to `&quot;` server-side; recorded as a badly-formed
   query, not a finding about Google's print corpus.
2. `q=(title:(google annual report) OR title:(google inc)) AND mediatype:(texts) AND YEAR:[1995 TO 2006]`
   → `numFound: 5`, all five in the **CIA Reading Room** collection:
   `cia-readingroom-document-0001487900/1487901/1487902` "GOOGLE INC. BETA EVALUATION AGREEMENT",
   `-0001487903` "MISC RE GOOGLE INC. ACCOUN[TS]", `-0001487896` "MEMO TO SHARON LEVY FROM DELETED
   RE AWARD".

Opened one of them. `archive.org/metadata/cia-readingroom-document-0001487901` → HTTP 200, 16 files,
**text layer present**: `0001487901_djvu.txt` (`ia/cia_1487901_metadata.json`). Downloaded it —
HTTP 200, **16,305 bytes**, `ia/cia_1487901_djvu.txt` + sidecar. Opening lines, verbatim (OCR
artefacts intact):

> "GOOGLE INC. — BETA EVALUATION AGREEMENT — Google Search Appliance™ Pre-release Version 4.2 and
> 4.4 — This Beta Evaluation Agreement ... is entered into this f19"j day of [November], 2004, by
> and between Google inc., 1600 Amphitheatre Parkway, Mountain View, California 94043 ("Google")
> and [the Central Intelligence Agency] ("Evaluator" or "You"). By accepting this Agreement You
> enroll in the Google beta program..."

This is a **Google Inc.-authored form document, held and published by a third party**, which is
what makes it evidence rather than founder narrative: it independently confirms the registrant's
legal name and address as filed in the S-1, and it documents an institutional beta-programme
mechanism the filings do not describe. Two honest limits: the day-of-month is OCR-degraded
(`f19"j` — read as 19 November 2004, confidence Low), and IA's `date`/`year` for the item is
2004-11-19/2004, which may be the CREST release date rather than the execution date.

**Documented null on these params:** `numFound=5` for 1995-2006 with **zero items dated 1998-2003**.
Google's earliest surviving print in this corpus is IPO-era. Pre-IPO corporate print (1998-2003
marketing collateral, price lists, decks) returned nothing here — a null on this query only, since
`corporate_print` in the harvester has never been run for Alphabet (Family c) and no
prearchive/annualreports-class corpus was queried.

## Family e documentary

STATUS: WRITTEN — **UNTRIED**, deliberately, on budget. No auction or museum request was issued:
the two candidates (a sale-record search for pre-IPO Google ephemera; an institutional
manuscript/university-archives search) are the kind of host that answers this project with a
bot-challenge, and a challenge bought here would have been paid out of the same budget that bought
the entity resolution, the 6407-filing index, the S-1 text and the patent check. Recording it
UNTRIED is the honest state, not a null. **What would settle it:** a harvester task or a scripted
single query against auction-sale JSON and Stanford University Archives finding aids (the latter is
the realistic home of 1998-era primary material — lab notebooks, the Stanford license file, the
1998 stock plan paperwork the S-1 says was defectively issued).

## Registrations and trademarks

STATUS: WRITTEN — patent side **CLOSED with independent verification**; trademark side **UNTRIED,
no serial obtained**; one registration route **UNANSWERED**.

**Patent — settled from two independent directions, neither a founder account.**
The S-1 lineage exhibit (accession 0001193125-04-105564) states: *"STANFORD's U.S. Patent 6,285,999
filed January 9, 1998 and issued September 4, 2001"* and *"the Exclusive period for U.S. Patent
6,285,999 expires on September 4, 2011"*. Checked against the grant record
(`https://patents.google.com/patent/US6285999B1/en`, HTTP 200, 1.8 MB, `patents/us6285999.html`):
**Filing date 1998-01-09, Publication date 2001-09-04, Application number US09/004,827, Assignee
Leland Stanford Junior University, Inventor Lawrence Page, status Expired - Lifetime.** The two
sources agree on both dates.

This is the load-bearing item of the whole probe. The PageRank patent **was filed 1998-01-09, about
eight months before the S-1's own "incorporated in California in September 1998"** — so the
technology's documented priority date precedes the registrant's existence, and the assignment to
Stanford (not to Google, not to the inventors) is what the S-1 means by "which owns a patent to
PageRank. We hold a perpetual license." Consequences for the chronology: (i) the founder
pre-history is **not** a founder claim — it is a dated public registration record, and must be kept,
not deleted; (ii) any Stage-1 narrative that opens the company's story with the patent must label
it as pre-entity work under a third party's ownership; (iii) the licence's exclusivity expiry
(2011-09-04) is a documented constraint the founders' own prospectus discloses.
Caveat, §6: the patent's dates are facts about an *invention*, not about a *company*.

**Trademark — UNTRIED.** The brief's route is "USPTO TSDR by serial number", and the serial is the
key that was not obtained: the original S-1 full text (367,767 words) returns **0 hits** for
`Serial No`, `U.S. Patent No`, `Patent No.`, and the only trademark statement in it names marks
without numbers (later lineage text: *"Our registered trademarks include: AdSense, AdWords, Blogger,
Froogle, Gmail, I'm Feeling Lucky and PageRank"*). I attempted the USPTO search API directly:
`POST https://tmsearch.uspto.gov/api-v1-0-0/tmsearch` filtered on applicant "GOOGLE INC" →
**HTTP 405 MethodNotAllowed** (S3-style XML error; `uspto/uspto_tm_google.json` kept as a negative
artifact). A 405 is a wrong-route response, so this is **UNTRIED/UNANSWERED, never a null** — the
route needs the current TSDR/TESS form or a serial number read out of a document (the FY2004 10-K's
intellectual-property section is the likely source; it is on the FETCH REQUEST list). The trademark
questions this bears on — when "Google" was first filed as a mark, and by whom — are **UNKNOWN**,
and notably the 1998 California entity is the candidate filer, which is a different proposition from
"the S-1 says we were incorporated in September 1998".

## Boundaries

STATUS: WRITTEN

Four boundaries, each pinned to a document that is on disk and was read this session. Where the
corpus gives only month- or quarter-granularity, the day is stated UNKNOWN rather than invented, and
where the only evidence is the company's own prospectus the boundary is labelled founder claim.

**B0 — Pre-entity prior art. Fixed at 1998-01-09. Confidence High.**
Document: patent US 6,285,999 (application US09/004,827), *filed 1998-01-09*, assignee Leland
Stanford Junior University, inventor Lawrence Page — verified at the grant record
(`patents/us6285999.html`) and independently by the filed license exhibit
(`...04-105564...txt`: *"STANFORD's U.S. Patent 6,285,999 filed January 9, 1998"*).
**Keep this leg and do not fold it into the company's origin**: at this date the registrant did not
exist. Everything before B0 is UNKNOWN, and the corpus on disk does not reach it.

**B1 — Company origin. Lower-bounded September 1998; upper-bounded 1998-11-11 18:45:51. Confidence High as to month, day UNKNOWN.**
Fixing document (a): S-1 Corporate Information, *"We were incorporated in California in September
1998"* — the company's own account, filed, **FOUNDER CLAIM class** (Tier-1 wrapper, one source).
Fixing document (b), independent of (a): Wayback capture `19981111184551` of `http://google.com:80/`
(CDX HTTP 200) and its page bytes (`wayback/google_19981111_raw.html`, 212 B) which read
*"Welcome to Google ... Search Engine Prototype ... Might-work-some-of-the-time-prototype"*.
The two are different in kind: (a) states incorporation, (b) proves a public service existed by a
moment no founder narrative controls. **The gap between B0 and B1 is where the S-1 itself puts the
work** (*"The first version of the PageRank technology was created while Larry and Sergey attended
Stanford University"*), and the exact founding day, the incorporation filing date with the
California Secretary of State, and the first server location are all **UNKNOWN — no document on
disk speaks to them.** The brief's "Founded 1998" is corroborated at month level; the brief's date
was not adopted on trust.

**B2 — First real experiment → repeatable validation: Q1 1999. Confidence Medium; exact date UNKNOWN.**
Sole fixing document: S-1, *"We began licensing our WebSearch product in the first quarter of 1999."*
This is still the lineage's own account, and quarter-granularity cannot support a day. What would
upgrade it: a dated first license contract, or periodical text (Family c, untried), or the archived
customer/partner pages. Note that the 1998-11-11 page self-describes as a *prototype*, so the corpus
does support "prototype at B1 → licensed product by B2" without importing hindsight. Funding between
B1 and B2 is **NOT EVIDENCED on disk**: the S-1 discloses a *1998 Stock Plan* whose shares "were not
exempt from registration or qualification under federal and state securities laws" (a negative
signal that survives from the same document), but no early outside-round date appears in anything read here.

**B3 — Scalable company. Three separate pins, none of them the founders' letter.**
- Profitability: S-1, *"We became profitable in 2001 following the launch of our Google AdWords
  program"* — year-granularity, founder-claim class; the FY2004 10-K (requested, not yet on disk)
  is what would put numbers under it.
- Registered-entity transition: *"In August 2003, we reincorporated in Delaware"* (S-1) — a genuine
  legal discontinuity, CA 1998 → DE 2003, which the brief's single "Google Inc." framing hides.
- Going public: the **filed lineage**, not prose — 10-12G and S-1 both 2004-04-29, first S-1/A
  2004-05-21, final prospectus-type item **424B4 filed 2004-08-19**, first post-IPO 10-K filed
  2005-03-30 (all from `_index/_INDEX.md`, 6407-filing enumeration). **The actual share-sale date
  is UNKNOWN on disk**: the 424B4 was not fetched before my ceiling, and the brief's "IPO 2004" is
  therefore proven as a *filing* fact only.
- Constraint introduced at B3 and disclosed in-lineage: the Stanford licence exclusivity ends
  2011-09-04 (*"...expires on September 4, 2011"*, exhibit 105564), and the Overture patent suit
  (filed April 2002, US 6,269,361) settled with a perpetual paid-up licence plus mutual releases
  (135503) — evidence that competitive IP pressure predates the IPO.

**Stage split I would defend at dossier stage:** Stage 1 = B0..B2 (1998-01 → Q1 1999, pre-entity
invention through first licensing, with the pre-entity leg explicitly labelled as Stanford's);
Stage 2 = B2..B3-profitability (Q1 1999 → 2001, unproven day at each end); Stage 3 = 2001 →
2004-08-19 (scaling to the offering). If the FETCH REQUESTs below return the 424B4 and FY2004 10-K,
Stage 3's end date firms from month to day; if they do not, Stage 3 must end at "the 2004-08-19
424B4 filing" and say so.

## Conflicts

STATUS: WRITTEN

| # | CLAIM A | CLAIM B | WHY THEY DIFFER | EVIDENCE WEIGHT | BEST-SUPPORTED INTERPRETATION | RESIDUAL UNCERTAINTY | CONF |
|---|---|---|---|---|---|---|---|
| U-1 | Brief: the IPO prospectus is a **424B1** | Index of 6407 filings: earliest **424B4** 2004-08-19, no 424B1 in any form row | Form family used for a registered offering differs from the assumption; the index is generated from SEC's own enumeration | Script index outranks a briefing line | The lineage ends in a **424B4** | A 424B1 could exist unenumerated only if the enumeration were incomplete — this CIK's enumeration had **zero unanswered slices** | High |
| U-2 | Brief: "registrant was **renamed** Alphabet in 2015, so the 2004 filer is Google Inc." | On disk: the 2004 filer is Google Inc. at **CIK 1288776** (6407 filings), while GOOGL/GOOG both resolve to **CIK 1652044** "Alphabet Inc." (1013 filings, nothing before 2023-06-29) | The brief's premise about the *name* is right; its implicit premise about the *identifier* is not — two CIKs are in play | Both sides are script output | Two registrant records exist and the pre-2023 link between them is **untested**, because 1652044's one listed archive slice answered 404 | Whether 1288776's history continues past 2015, and whether 1652044 is a renamed continuation or a new 2015 entity — **UNKNOWN** | Low |
| U-3 | S-1: incorporated "September 1998" | Patent: PageRank filed **1998-01-09**, assigned to Stanford | Invention predates incorporation; the company's origin story and the technology's origin story have different dates | Patent is independently verifiable and third-party-held; the month statement is the company's own | Both true, non-competing: pre-entity research under Stanford ownership, then a California company in Sept 1998, then a Delaware reincorporation Aug 2003 | Whether any Google *service* existed before Sept 1998 — earliest archive capture on disk is 1998-11-11 | Medium |
| U-4 | S-1 founders' letter: *"Sergey and I founded Google because we believed we could provide a great service to the world"* | No on-disk document states a motive | A stated motive is not a fact about the world | Founder claim, Tier-1 wrapper, zero corroboration | Record as **FOUNDER CLAIM**, never as causation; the admissible surrounding facts are the dated patent, the capture and the licence | Residual by classification, not by evidence | n/a |
| U-5 | Family b attempt 1/2: HTTP **503** "Internet Archive: Temporarily Offline" | Family b attempt 3: HTTP 200 with the 1998 capture | The host intermittently refuses; nothing about the query changed | Same host, same URL form, opposite outcomes ⇒ the 503 carried **no** information | Treat every 503/403/405 here as UNANSWERED; retry budget, never absence | `www.google.com` and `google.stanford.edu` still unanswered as of last attempt | High |

## Nulls

STATUS: WRITTEN — documented nulls only, each bounded by the params that produced it.

| # | Statement of the null | Exactly what it does NOT mean |
|---|---|---|
| N-1 | Alphabet CIK 1652044's index contains **no filing before 2023-06-29** and no S-1/424B/10-K older than 2024 | Not "Alphabet has no pre-2023 filings": its single listed archive slice 404'd ⇒ UNANSWERED |
| N-2 | In the original S-1 full text (367,767 words) the strings **BackRub**, **graduate student**, **Serial No**, **U.S. Patent No**, **Patent No.** occur **zero** times | Not "the S-1 omits the trademark portfolio" — the numbers appear, if anywhere, in later amendments/exhibits not yet fetched |
| N-3 | IA corporate-print query `(title:(google annual report) OR title:(google inc)) AND mediatype:(texts) AND YEAR:[1995 TO 2006]` → numFound **5**, **none dated 1998-2003** | Not "no pre-IPO Google print exists" — `corporate_print`/`hathitrust`/`google_books` were never run for this company |
| N-4 | XBRL for CIK 1288776, window 1998-2006 → **1 row** (`StockholdersEquity` 17,039,840,000 USD at 2006-12-31, from a 2010 filing, frame CY2006Q4I) | Not "Google's early finances are unrecoverable" — the filed S-1/10-K statements carry them and are in-window primaries; and this row is a **RETROSPECTIVE SOURCE** |
| N-5 | `facts --cik 1652044 --from 1998-01-01 --to 2006-12-31` wrote **no file**; `sources/sec/_MANIFEST.csv` has **zero data rows** | Not "intake failed for this company" — 41 document files across 10 accessions (13 MB) are on disk with sidecars; the manifest write was cut off at the tool ceiling |
| N-6 | Day-level founding date; the first customer of the Q1 1999 WebSearch licence; the angel-round dates; the IPO share-sale date; any 1998-2003 first-party print | These are **UNKNOWN**, i.e. the project's deliverable, not a defect. None may be filled from a founder account without the FOUNDER CLAIM tag |

## Source index

STATUS: WRITTEN

All paths relative to `founders_playbook/01_companies/company_005_alphabet/sources/`. **114 files,
14 MB**, every fetched item with a sidecar (`.meta.json` for script-fetched filings, `.sidecar.json`
for the curl fetches). Failed requests are kept as negative artifacts, deliberately.

| Artifact | Path | What it proves | Tier | Status |
|---|---|---|---|---|
| S-1 full submission, 5.7 MB, 367,767 words | `sec/0001193125-04-073639_0001193125-04-073639.txt` (+ dex1001/1002/1003) | "incorporated in California in September 1998"; "reincorporated in Delaware" Aug 2003; "began licensing our WebSearch product in the first quarter of 1999"; "became profitable in 2001"; founders' letter | 1 (founder claim for origins) | read |
| S-1/A 2004-05-21 | `sec/0001193125-04-093053_*.txt` | lineage leg | 1 | on disk, unread |
| S-1/A carrying Stanford licence text | `sec/0001193125-04-105564_*.txt`, `..._dex1010.htm` | "STANFORD's U.S. Patent 6,285,999 filed January 9, 1998 and issued September 4, 2001"; exclusivity expires 2011-09-04 | 1 | read |
| S-1/A 2004 (further) | `sec/0001193125-04-116608`, `-124025`, `-131481`, `-134174` (`ds1a.htm`), `-135503`, `-138034` (index page only) | lineage legs; 135503 discloses the Overture suit (April 2002, US 6,269,361) and settlement | 1 | 135503 read |
| 8-K 2004-07-09 | `sec/0001193125-04-115812_*.txt`, `_d8k.htm` | earliest 8-K in window | 1 | on disk, unread |
| Google Inc. submissions index, 6407 filings, 0 unanswered slices | `_index/_INDEX.md`, `_index/submissions.csv`, `_index/submissions.json` | earliest-per-form: S-1 2004-04-29, 10-12G 2004-04-29, 424B4 2004-08-19, 10-K 2005-03-30; **no 424B1 exists** | index (not itself evidence) | canonical |
| Alphabet CIK 1652044 index, 1013 filings, ≥2023-06-29 | `_index/_INDEX_alphabet_1652044.md`, `_index/submissions_alphabet_1652044.csv` | the 404 archive slice; the false-null trap | index | preserved copy |
| XBRL early series, **1 row** | `financials/xbrl_early_series.csv` | StockholdersEquity 17,039,840,000 USD at 2006-12-31, from a 2010 10-K | 1, retrospective | read |
| EDGAR full-text search response, 123 hits | `edgar_fts/fts_s1_2004.json` | `"Google Inc. (CIK 0001288776)"`, file_num 333-117934, Mountain View CA, inc DE | 1 | read — resolved the entity question |
| Wayback CDX, bare host, HTTP 200 | `wayback/cdx_retry.json` | earliest google.com capture **19981111184551**, statuscode 200 | 1 (archive) | read |
| Earliest archived google.com page, 212 B | `wayback/google_19981111_raw.html` | "Welcome to Google … Search Engine Prototype … Might-work-some-of-the-time-prototype" | 1 (archived company page) | read |
| CDX **503** negative artifacts (3 files) | `wayback/cdx_bare.json`, `wayback/cdx_www.json`, `wayback/cdx_stanford.json` | host intermittently offline ⇒ UNANSWERED, not absent; www + Stanford routes still open | n/a | retained |
| IA corporate-print searches, HTTP 200 | `ia/ia_corporate_print.json` (numFound 6, off-target query), `ia/ia_annual_reports.json` (numFound 5, all CIA CREST 2004, none 1998-2003) | family-(d) reachability + the N-3 null | 3 (finding aid) | read |
| CIA CREST item metadata | `ia/cia_1487901_metadata.json` | text layer `0001487901_djvu.txt` exists; item date 2004-11-19 | 3 | read |
| Google Inc. beta-evaluation agreement text, 16,305 B | `ia/cia_1487901_djvu.txt` | third-party-held Google Inc. form contract, Google Search Appliance pre-release 4.2/4.4, address matches S-1 | 1 | read |
| Patent grant record US 6,285,999 B1, 1.8 MB | `patents/us6285999.html` | filing **1998-01-09**, publication 2001-09-04, app US09/004,827, assignee Leland Stanford Junior University, inventor Lawrence Page | 1 (registry) | read |
| USPTO tmsearch **HTTP 405** | `uspto/uspto_tm_google.json` | trademark route refused this form; not an absence | n/a | retained |
| `_MANIFEST.csv` — header only, 0 rows | `sec/_MANIFEST.csv` | the `auto` run was cut at its ceiling before writing it; 42 document files did land | n/a | negative artifact |

**Two intake imperfections stated plainly, for the next agent:** (1) Alphabet's
`_index/submissions.json` was overwritten by the Google run and only the `.csv` and `_INDEX.md`
copies were preserved — re-run `index --cik 1652044` into a scratch company-dir if the raw JSON for
that CIK is needed. (2) `sec/_MANIFEST.csv` is empty despite 42 files present, so file-level
provenance for the filings lives in the per-file `.meta.json` sidecars, not in the manifest.

## Untried

STATUS: WRITTEN — the honest remainder. Nothing below is evidence of absence.

1. **Family c, periodical corpora — entirely UNTRIED.** `--company google` and `--company alphabet`
   both return `PLANNED REQUESTS (0 tasks)`; `tools/queries.json` carries tasks only for
   walmart/apple/unitedhealth. Needs an orchestrator config task (all six source families, caps
   raised above the new task count). This is the one family that could push the verdict from the
   minimum T1 to a comfortable one, and the one that might reach 1998-2003 independently.
2. **Family e, auction / museum documentary records — UNTRIED** (budget decision, recorded in that section).
3. **USPTO trademark — UNTRIED.** TSDR needs a serial number; none was obtained. One API form tried,
   HTTP 405, kept as a negative artifact. Next form to try: the current TSDR case-status route once a
   serial is read out of the FY2004 10-K IP section, or the USPTO assignment/search UI JSON.
4. **The 2004→2015 entity bridge — UNTESTED.** CIK 1652044's archive slice retry, plus CIK 1288776's
   post-2015 rows (is "GOOGLE INC." still filing there, and under what name?). Answers
   `0001193125-04-074059` (10-12G) and the Alphabet 2015 8-K/10-K side. This is the single largest
   open item, because it decides whether the dossier's registrant spine is one CIK or two.
5. **Unfetched in-window filings on a CIK that enumerates them**: 424B4 (2004-08-19), 10-Q (2004-08-16),
   FY2004 10-K (2005-03-30), FY2005/FY2006 10-Ks, DEF 14A 2005, and the S-1/A amendments between
   2004-05-21 and 2004-08-19 — FETCH REQUEST in *Family a*.
6. **Wayback `www` variant and Stanford hosts — UNANSWERED (503), not absent**; no attempt at
   in-window captures of google.com later than 1998-11-11 (a 1999/2000 ladder would pin the
   prototype→product transition that B1/B2 currently take from the S-1's mouth).
7. **Not searched at all:** California Secretary of State (the 1998 entity), Delaware (2003), court
   PACER for the Overture and warrant disputes, Stanford news/technical-report archives, the
   1998 Stock Plan defect litigation, and any non-English press.

