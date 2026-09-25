# A_chronology_feasibility.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:07:20Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

STATUS: WRITTEN (probe-microsoft)

**Families returning confirmed in-window Tier-1 text: 0 of 5.** Families returning a strong in-window
lead that no one has opened yet: 2 — (c) periodicals, (d) corporate print. Families UNANSWERED: 2 —
(a) filings, (b) web archives. Families UNTRIED: 1 — (e) documentary.

Per §15.2 read literally, 0 qualifying families is **T3 register** (≤1), which implies **3-4 agent runs**,
an 8k-word-per-stage cap, and still-mandatory §K, §N, §U. That is the number this pass measured, and it
is the number I would defend if the probe had to be scored today.

**But the T3 label is not certifiable for this company, and dispatching 3-4 runs against it would be a
waste.** Both families that could decide Microsoft's tier were blocked by defects on the script side of
§15.1's division of labour, not by the absence of evidence: (a) enumerated only EDGAR's `recent` bucket,
1,002 rows spanning 2020-08-07 to 2026-09-17, with its two older slices 503-ing on the first build and
404-ing on the second; (c) was handed a `queries.json` containing 51 tasks for three other companies and
none for Microsoft, so the harvester planned 0 requests. Meanwhile the free shelf for 1975-1985 is
demonstrably present (545 hobbyist-serial items 1974-1982 with text layers; six in-window
Microsoft-authored artefacts in one 25-row sample). Walmart was mis-graded by a two-family probe; the
same error in reverse — under-grading on an outage and an unconfigured family — is the risk here.

**Recommendation: hold Microsoft ungraded for one scripted re-probe, and plan against T2 (6-9 agent
runs) provisionally, not T1.** Do not fund 15-20 runs on this evidence: T1 needs ≥3 families, and here
not even one has produced a single verified in-window sentence about the company. The re-probe cost is
near-zero agent budget: two script fixes plus the item-level OCR grep, then re-score.

| family | this pass | in-window Tier-1 text | tier weight |
|---|---|---|---|
| (a) filings | UNANSWERED (truncated enumeration, 503/404 conflict) | 0 docs (auto: "0 documents stored") | blocked, unknown |
| (b) web archives | UNANSWERED (CDX 503 x2, search hosts 200) | 0 | low regardless (§14.6) |
| (c) periodicals | LEAD_ONLY (545 serial items 1974-1982; `text:` index proven blind; 0 tasks configured) | 0 verified | decisive if fixed |
| (d) corporate print | LEAD_ONLY (creator-scoped null; 6 in-window authored rows unopened) | 0 verified | decisive if verified |
| (e) documentary | UNTRIED | 0 | unknown |

## Boundaries

STATUS: WRITTEN (probe-microsoft)

**Earliest defensible origin: UNKNOWN.** No document opened this session states one fact about the
company's beginning. The brief's window opens 1975-01-01 and the project's claimed origin sits inside it;
that is a claim on the intake sheet, not evidence, and §Boundaries must not launder it. The two dates
this session can actually defend are shelf dates, not story dates: the oldest in-window serial item seen
is dated **1975** (`197503PopularElectronics`, plus `popularelectroni08unse_2/_3` = October and November
1975), and the oldest row that is company-authored on its own face is dated **1981**
(`1981-microsoft-adventure`, "Brochure: Microsoft Adventure"). Neither has been read.

**Proposed Stage boundaries — provisional, density-derived, to be re-cut by the re-probe:**
- **Stage 1: 1975-01-01 → 1980** (provisional close at 1980 because that is where the company-authored
  metadata rows stop and start: nothing dated 1975-1980 was returned by the authored-material queries,
  the earliest such row is 1981). The whole stage rests on the periodical family and on documentary
  records, both currently unverified/untried. It cannot be written from filings, and it will not be
  written from web archives at all.
- **Stage 2: 1981 → 1985** (provisional; bracketed by the rows actually seen: 1981 brochure, 1982
  `MSDOS2FuturePlansForMSDOSByPaulAllen` and the 1982-06 sixteen-bit operating-systems piece, 1983
  `microsoft-multi-tool-word-brochure`, 1984 `multiplanusersgu0000schn` and `illustratedmulti0000stul`,
  inside a query bounded by YEAR:[1975 TO 1985]). Product print is real here, but note that four of the
  six rows are third-party or press books, not the registrant's own text.
- **Stage 3: 1986 → 1990** (provisional; the assigned window's tail, for which **nothing** was seen in
  any family — no filing enumerated, no artefact returned, no web capture attempted successfully).
  Stage 3 is currently the emptiest of the three despite being closest to the era where EDGAR should
  begin to answer, which is the clearest sign that the (a) truncation, not the archive, is the binding
  constraint.
- **Founder pre-history: UNKNOWN — keep, do not delete.** Nothing this session touches the founders
  before 1975-01-01, and the one adjacent artefact (a 1982 document row naming Paul Allen) says nothing
  about the origin. An inherited pre-history narrative must be filed as a claim awaiting a source, not
  promoted into §A.

## Conflicts

STATUS: WRITTEN (probe-microsoft)

- **C-1 — EDGAR older-slice status: 503 vs 404.** `sec_intake.py index --cik 789019` run twice minutes
  apart records `CIK0000789019-submissions-001.json` and `-002.json` as "UNANSWERED after 3
  tries (HTTP 503)" in the 19:09 UTC build and "UNANSWERED: HTTP 404" in the 19:10 UTC build. A 503 is a
  refusal; a 404 is an absence; the same two objects cannot be both, and the deciding evidence is the CSV:
  all 1,002 stored rows carry `source = recent`, i.e. the older-archive members were never parsed either
  way. Adjudication: unresolved, and the pre-2020 window stays UNANSWERED. Neither pass may be cited as
  "Microsoft has no filings before 2020".
- **C-2 — index hit vs bytes on disk.** The IA `text:` index says `197602-modern-data` contains
  "microsoft"; the item's downloaded OCR (261,075 B, 12,359 lines) contains the string **zero** times, and
  the item's own `description` field supplies the phrase. Adjudication: the bytes win. Consequence beyond
  this row: every `text:`-scoped census in families (c) and (d) — including numFound 500 and numFound 2 —
  is a claim about uploader annotations until an item is opened, and the earlier lesson from this project
  that "a null from one family is not a null" cuts both ways: a *positive* from that index is not a
  positive either.
- **C-3 — `facts` stdout vs the empty directory.** The facts step printed
  `.../sources\financials\xbrl_early_series.csv`; the directory exists and is empty. Two accounts of the
  same command; the file is the record. Substance unaffected (no XBRL reaches 1975-1990), but the tool
  reporting a path it did not write is a provenance defect for the next reader who trusts the log.
- **C-4 — outage scope.** `web.archive.org` answered 503 twice while `archive.org/advancedsearch.php`,
  `archive.org/metadata/` and `ia801807.us.archive.org` answered 200 in the same ten minutes. Any rerun
  plan should therefore treat family (b) as an independent, retryable host rather than assume the whole
  archive is down — the opposite conclusion would have suppressed the family (c)/(d) results entirely.

## Nulls

STATUS: WRITTEN (probe-microsoft)

Documented nulls, each one a specific query with a specific answer, so no later pass has to re-run it
blind:

- **N-1** creator-scoped digitised corporate print: `numFound 1`, and that row (`guide-to-data-access-objects`,
  1997) is outside the window → **no Microsoft annual-report run on the IA creator route**, i.e. the
  Walmart-shape asset is absent. Query saved at
  `sources/corporate_print/ia_q4_creator_microsoft_reports_1977_1998.json`. The bare title-scoped
  corporate-print variant was not run (budget) and must not be read as covered by this null.
- **N-2** `sources/financials/` is empty: no XBRL early-series file exists for 1975-01-01 → 1990-12-31.
- **N-3** `auto --from 1975-01-01 --to 1990-12-31 --max-docs 25` → "0 documents stored, 0
  skipped/unanswered": a **conditional** null over an enumeration that contains no rows before 2020-08-07.
  Not a statement that Microsoft filed nothing in the window.
  Corroborated by `sources/sec/_MANIFEST.csv`, which the auto step created with its header row and no
  document rows.
- **N-4** `grep -i microsoft` = 0 over the whole Modern Data February **1976** OCR layer: one sampled
  issue of one title is empty of the string. Not a corpus null — the 545-item shelf is unsampled beyond
  this one.
- **N-5** not a null, listed so it cannot be mistaken for one: the earliest capture of microsoft.com was
  **not measured** (C-4). Report family (b) as UNANSWERED until a CDX response is on disk.

## Untried

STATUS: WRITTEN (probe-microsoft)

Never attempted this pass, each with the one thing it needs:
1. `periodical_harvest.py` for Microsoft at all — needs a `microsoft` task block in `tools/queries.json`
   (0 occurrences of the word in the file today); then `--company microsoft` plans requests instead of 0.
2. **Item-level OCR search** inside the 545 hobbyist-serial items — the metadata route is proven blind
   (C-2), so this is the single highest-value untried item in the whole probe. Routes: bulk-download the
   ~40 most probable 1975-1982 issues and grep locally, or IA in-item search, or HathiTrust
   `field1=ocr` full-text search (recorded in `tools/periodical_harvest.py` as verified live for another
   company only with `--use-curl` plus an insecure-host exception).
3. HathiTrust catalog/full-view serial scan for the same titles — 0 requests spent this pass.
4. Google Books volume search — blocked by policy, not by absence: the harvester's own help records that
   keyless `books.googleapis.com` v1 "is quota-0 and answers 429", so it needs `--gb-key`.
5. Chronicling America newspapers 1975-1982 (Albuquerque/New Mexico and national coverage of the same
   events) — the config carries 17 Walmart CA tasks and the notes record a Cloudflare challenge from this
   box, so it needs the challenge handled by the orchestrator, not by an agent's web budget.
6. Family (e) in full: auction houses and museum collections online (see §Family e).
7. EDGAR full-text search / direct accession grab for 1994-1999 Microsoft filings — never reached, because
   the enumeration stopped in 2020 (C-1). Also untried: whether the registrant's oldest EDGAR-era text is
   a 10-K, a 13D/G or something else — the brief's fallback question, still open.
8. The 1989-1990 tail of family (d) under a **title**-scoped query, and any Microsoft-issued annual report
   sold or deposited as a separately catalogued item.

## Family a filings

STATUS: WRITTEN (probe-microsoft)

**Verdict: UNANSWERED — not NULL.** The scripted intake ran to completion and returned zero
in-window documents, but it never enumerated the years that contain the window, so nothing here is
an absence of evidence.

What the scripts actually returned, this session, 2026-09-26:

1. `sec_intake.py resolve --ticker MSFT` → `{"ticker": "MSFT", "cik": 789019, "name": "MICROSOFT CORP"}`.
2. `sec_intake.py index --cik 789019` → "1002 filings from MICROSOFT CORP (MSFT)". The index is the
   authority the method asks for, and it is truncated: every one of the 1,002 rows in
   `sources/_index/submissions.csv` carries `source = recent` (verified by counting the column), and
   the filing-date range of the whole file is **2020-08-07 → 2026-09-17**. Form counts in the file are
   dominated by insider forms (4 x744, 8-K x56, 144 x45, PX14A6G x37, 10-Q x18, 11-K x18) — the shape
   of a last-six-years slice, not of a registrant with filings from 1986/1994 forward.
3. `sources/_index/_INDEX.md` therefore reports an "earliest filing per form" table whose oldest row is
   a Form 4 filed **2020-08-07** and an oldest 10-K filed **2021-07-29**. There is no S-1 row, and there
   is also **no Schedule 13D/13G row from the 1990s, no 10-K from 1994-2020, and no pre-1994 row of any
   kind** — so the brief's fallback question ("is the earliest company-authored text a 13D/G or a later
   10-K?") **cannot be answered from this index**. The brief's general expectation stands as background
   only — EDGAR text coverage is thin before ~1994 — but it is not what this run measured, because this
   run measured nothing before 2020.
4. `sources/_index/_INDEX.md` "UNANSWERED slices (never report these as absent)": first build
   (stamped 2026-09-25 19:09 UTC) records `CIK0000789019-submissions-001.json` and `-002.json` as
   "UNANSWERED after 3 tries (HTTP 503)". A second build of the same command (19:10 UTC) records the
   **same two slices as "UNANSWERED: HTTP 404"**. The two passes disagree, which is exactly why neither
   may be read as an empty archive. See §Conflicts C-1.
5. `sec_intake.py facts --from 1975-01-01 --to 1990-12-31` printed
   `.../sources/financials/xbrl_early_series.csv`, but `sources/financials/` **contains no file** (verified
   by `ls`/`find` this session). No XBRL early series was written; the stdout line names a path, it is not
   evidence of content. Recorded in §Nulls N-2 as a tool artifact as much as a data null. (Expected in
   substance: XBRL company facts do not reach 1975-1990.)
6. `sec_intake.py auto --from 1975-01-01 --to 1990-12-31 --max-docs 25` → "auto: 0 documents stored,
   0 skipped/unanswered". Zero is the honest number **conditional on item 2**; the pipeline had no
   in-window accession to fetch. Documents downloaded by filings intake this run: **0**.

`FETCH REQUEST:` for the orchestrator (script work, not agent work): Microsoft's older EDGAR archive is
in the submissions JSON `filings.files` members, which this build of `sec_intake.py` did not reach — it
requested only page-suffixed variants of the single `recent` document and never a `files` entry, which is
why 100% of stored rows are `source = recent`. Either fix the pagination in `tools/sec_intake.py` or run a
one-off grab of the 1994-1999 accession set, then re-dispatch this company's filings family. Until then
§Family a stays UNANSWERED and must not be counted as a Tier-1-nulling result.

## Family b web

STATUS: WRITTEN (probe-microsoft)

**Verdict: UNANSWERED — a service outage, not an empty archive.** Two CDX attempts against
`web.archive.org`, this session: 00:45 and 00:48 local, `https://` and `http://`, both answered
**HTTP 503** with an 11,832-byte HTML banner titled "Internet Archive: Temporarily Offline" — not a
CDX JSON array, and not `[]`. Both bodies are kept as negative artifacts at
`sources/web_archive/cdx_microsoft_com_earliest_200.json` and
`.../cdx_microsoft_com_earliest_200_retry.json` (byte-identical), with a sidecar recording url,
status, bytes and the UNANSWERED call. **Earliest capture of microsoft.com: NOT ESTABLISHED.**

Note the asymmetry that makes this cheap to re-run: `archive.org/advancedsearch.php`,
`archive.org/metadata/` and the direct item server `ia801807.us.archive.org` all answered HTTP 200
minutes before and after, so only the CDX host is down. §14 rule 6 already records that web archives
carry nothing before the mid-1990s, so even an answered CDX could not reach Stage 1 for this company;
family (b) is a corroboration route for the 1990s tail at best, and its weight in the tier decision is
low regardless.

## Family c periodicals

STATUS: WRITTEN (probe-microsoft)

**Verdict: LEAD_ONLY — the shelf is proven in-window, the text is not yet.** This is the family the
brief correctly predicted would decide the tier, and it split into a strong positive and a hard
mechanical negative in the same pass.

*Positive (the corpus exists and is text-layered).* Internet Archive metadata search,
`title:("popular electronics") OR title:("byte magazine") OR title:(kilobaud) OR title:("compute!")`
AND `YEAR:[1974 TO 1982]` AND `mediatype:(texts)` → **numFound 545** (HTTP 200;
`sources/periodicals/ia_q2_hobbyist_serials_1974_1982.json`). In-window serial items appear directly in
the returned rows: `197503PopularElectronics` (Popular Electronics, March 1975, collection
`popularelectronicsmag`), `popularelectroni08unse_2` and `_3` (October and November 1975, `dlarc-library`),
`byte-magazine-1977-07` ("Byte Magazine Volume 02 Number 07", collection `byte-magazine`),
`Kilobaud197810` (collection `kilobaudmagazine`). These are the hobbyist titles the 1975-1980 story was
printed in, on a free, text-bearing route.

*Hard negative (the route cannot see inside them).* The same index's bare-term search is rewritten by IA
into a `text:` clause — Q1's own echo shows `(microsoft)` became
`(text:microsoft OR text:microsoft OR text__reviews:microsoft) AND year:[1975 TO 1985]`. Scoped to the
magazine collections, `text:microsoft AND collection:(popularelectronicsmag OR byte-magazine OR
kilobaudmagazine OR computermagazines) AND YEAR:[1975 TO 1979]` → **numFound 2**
(`1979-Fall-compute-magazine`, `197602-modern-data`). I then downloaded the full OCR of the second item —
HTTP 200, 261,075 bytes, 12,359 lines, kept at
`sources/periodicals/197602-modern-data_djvu.txt` — and `grep -i microsoft` over it returns **0
occurrences**. The match lives in the uploader's `description` field, verbatim from
`meta_197602-modern-data.json`: "Data processing existed long before Apple and Microsoft". Therefore:
**IA advancedsearch does not full-text search a magazine's OCR layer.** Every `text:`-scoped census in
this family, including Q1's numFound 500, counts catalogue annotations, not printed pages, and cannot be
cited as Tier-1 in-window periodical text.

*Why it stays LEAD_ONLY rather than NULL.* `periodical_harvest.py` — the script that owns this family —
plans **zero** Microsoft requests: `--company microsoft --dry-run` prints "PLANNED REQUESTS (0 tasks)",
because `tools/queries.json` carries tasks only for walmart (28), apple (8) and unitedhealth (15) and
**0 occurrences of "microsoft"** in the whole file. An unconfigured family is not a null.

`FETCH REQUEST:` (script work, 0 agent web budget): (1) add a `microsoft` task block to
`tools/queries.json` — hobbyist-serial queries for 1975-1982, then 1983-1990; (2) implement or route an
**item-level** OCR search, because metadata search is proven blind here: either bulk-download the ~40
most probable 1975-1982 issues from the 545 and grep them locally (the method that settled Q3 above,
~1 request per issue, 261 KB per issue), or use HathiTrust full-text search
(`babel.hathitrust.org/cgi/ls?field1=ocr;q1=...;a=srchls;lmt=ft`, which HARVEST_README records as proven
live for this project only with `--use-curl --insecure-hosts babel.hathitrust.org`). Candidate search
terms must include the hyphenated period form **the index itself does not tokenise the same way** —
query `Micro-Soft` as well as `Microsoft`, plus `Altair`, `Traf-O-Data`, `Gates`, `Paul Allen`, and the
MITS/Albuquerque place names.

## Family d corporate print

STATUS: WRITTEN (probe-microsoft)

**Verdict: LEAD_ONLY — no annual-report run (a real per-param null), but company-authored in-window
print is on the shelf.** The route that flipped Walmart's verdict does not flip this one: the
creator-scoped query `(creator:(microsoft) OR creator:("microsoft corp") OR creator:("the microsoft corp"))
AND (title:(annual) OR title:(report) OR title:(reports)) AND mediatype:(texts) AND YEAR:[1977 TO 1998]`
→ **numFound 1**, and that one row is `guide-to-data-access-objects`, "Visual Basic 5.0: Guide To Data
Access Objects & Crystal Reports", **1997** — a product manual, outside the window (HTTP 200;
`sources/corporate_print/ia_q4_creator_microsoft_reports_1977_1998.json`). There is no digitised
Microsoft annual-report run here equivalent to Wal-Mart's FY1972-FY1997 set. Recorded as a documented
null (§Nulls N-1); the title-scoped variant was not separately run because both forms share the clause
builder and the budget went to the OCR test above.

*The lead.* The broad Q1 result set (`text:microsoft AND YEAR:[1975 TO 1985] AND mediatype:(texts)`,
numFound 500, 25 rows sampled; `sources/periodicals/ia_q1_microsoft_1975_1985.json`) contains in-window
rows that are company-authored artefacts on their face, from the `title`/`year`/`collection` fields alone:
`1981-microsoft-adventure` ("Brochure: Microsoft Adventure", 1981, collections `readerservice`,
`folkscanomy_computer`), `MSDOS2FuturePlansForMSDOSByPaulAllen` (1982),
`16-Bit_Operating_Systems_A_Whole_New_Ball_Game_1982-06` (1982),
`microsoft-multi-tool-word-brochure` (1983, collection `opensource`), `multiplanusersgu0000schn`
("Multiplan user's guide", 1984, `internetarchivebooks`) and `illustratedmulti0000stul` (1984). Two of
these — a named-individual internal planning document and two product brochures — are the class of
artefact that can carry a Stage-1 origin claim at Tier 1 **if** their text layers and provenance check
out. None has been opened, so none is counted. Note also that `internetarchivebooks` rows are
`inlibrary`/`printdisabled`, i.e. borrow-restricted: §4's legal boundary applies before anyone plans to
read them in bulk, while `folkscanomy_*` and `opensource` items are ungated.

## Family e documentary

STATUS: WRITTEN (probe-microsoft)

**Verdict: UNTRIED.** No scripted route to auction or museum documentary records exists in
`tools/` (the harvester's families are chronicling_america, internet_archive, corporate_print,
hathitrust, google_books), and the web-call ceiling for this probe was consumed by the CDX outage and the
OCR test that produced the family-(c) finding. Nothing was attempted and nothing was found; the
difference matters and is being stated explicitly. What would settle it, for a later pass: the Apple
probe's precedent is that founding-era paper surfaces at auction rather than in EDGAR, so the queries
worth running are a partnership/licensing-document search ("Microsoft" 1975-1977 partnership agreement,
licence, cheque, or Altair-era correspondence) across the auction houses that sell computer history, and
a collections-online search at a computing museum for Microsoft-held manuscript material. Expect
bot-challenges on the commercial routes; museum collections APIs are the cheaper first move.

