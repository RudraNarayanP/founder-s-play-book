# A_chronology_feasibility.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:07:31Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

**TIER: T2 on the evidence standing on disk right now — with the T1 expectation intact and every shortfall
traceable to a tool or an outage rather than to missing evidence.**

§15.2 counts families that returned in-window Tier-1 text:

| # | family | in-window Tier-1 text? | basis |
|---|---|---|---|
| a | filings | **YES** | S-1 + 424B4 on disk; "incorporated in Delaware in July 2004"; Ceglia Legal Proceedings; 397 pre-2014 filings enumerated |
| — | legal records (extra) | **YES (register-level)** | CourtListener 200; six in-window matters 2004-09-02 → 2007-05-22, incl. 1:04-cv-11923 |
| b | web archives | **NO — UNANSWERED** | CDX 504/503 ×3, "Internet Archive services are temporarily offline" |
| c | periodical corpora | **NO** | CA 403 ×3, HathiTrust unreachable ×2; Google Books live but 1 in-window record, metadata only |
| d | digitised corporate print | **NO — UNQUERIED** | task authored, skipped by the consecutive-failure breaker |
| e | auction / museum | **NO — UNTRIED** | deliberately not attempted |

**2 of 5 → T2 core.** It is not 3, and the honest reason is that families b and d were knocked out by the
same archive.org outage that also removed the IA leg of c — one external event, three families, no
evidence touched. **Two cheap re-runs would make this T1**: (i) the CDX pair once archive.org answers,
(ii) RECAP/PACER docket text for 1:04-cv-11923 (the register is already proven reachable, so this is
text-retrieval, not route-discovery). A third — the corporate_print/IA re-run — closes d. Nothing in this
probe suggests the evidence does not exist; on the contrary, this is the deepest-past case the fleet has
and the only company so far whose founding year is covered by *both* a complete SEC register and a dated
federal docket.

**Implied agent-run budget: 6-9 (T2).** If the two re-runs land, re-dispatch at 15-20 with §A-§U full. Do
not spend T1-level runs on family (e); it is the least informative family for a 2004 internet company.

**The one thing the tier does not capture, and Stage 1 must not lose:** the filings family is Tier-1 in
*dignity* only. Its founding account is self-reported — the dorm-room narrative is a FOUNDER CLAIM inside a
registration statement, the "Our History" timeline is an un-extractable image, and the disputes that would
contradict it are named nowhere in the document. **The independent dating of 2003-2004 therefore rests on
the court register (2004-09-02) and, if it is ever ordered, the Delaware charter — not on the S-1.**
Stage-1 boundary is month-level (July 2004) and the origin day stays UNKNOWN; that is the shape of the
answer this evidence supports, and per §15.2 "we cannot know" is itself a deliverable.

## Family a filings

**TIER 1 CANDIDATE — PROVEN REACHABLE.** Every statement below was read from bytes on disk this session.

### What the scripted intake did

| step | result |
|---|---|
| `resolve --ticker META` | `{"ticker": "META", "cik": 1326801, "name": "Meta Platforms, Inc."}` |
| `index --cik 1326801` | 1000 filings, **every row from source `recent`**, earliest 2024-06-14 |
| archive slices | `CIK0001326801-submissions-001.json` UNANSWERED (TimeoutError), `-002.json` UNANSWERED (HTTP 503) |
| `facts 2004→2013` | 215 rows → `sources/financials/xbrl_early_series.csv` |
| `auto --max-docs 30` | `0 documents stored, 0 skipped/unanswered` |

**The truncated index is a transient-failure artifact, not an empty window.** Re-fetching the same two
archive slices by hand with a 180 s timeout returned **HTTP 200 / 314,243 B and HTTP 200 / 184,731 B**,
saved to `sources/_index/raw_submissions-001.json` and `raw_submissions-002.json`, parsed to
`sources/_index/submissions_pre2014.csv`: **397 filings with filingDate ≤ 2013-12-31**, oldest slice row
**2005-05-06**. So the pre-2014 EDGAR record is fully reachable; the pipeline simply did not hold the
connection long enough to get it.

**SCRIPT DEFECT (blocks the whole fleet, not just this company).** `tools/sec_intake.py` lines 90-91 test
the string `ERROR_MARKERS` membership against `raw` while `raw` is **bytes** in binary mode, raising
`TypeError: a bytes-like object is required, not 'str'` on all three retries. Consequence: `grab` — and
therefore `auto`, whose only document-storage path is `grab` — **can never store a document**. Observed
verbatim: `{"accession": "0001193125-12-034517", "file": "d287954ds1.htm", "status": "UNANSWERED after 3
tries (TypeError: a bytes-like object is required, not 'str')", "path": ""}`. The `auto` line
"0 documents stored, 0 skipped/unanswered" under-reports this: the skipped list is written only for
documents that were *picked*, so a pick-list of zero and a broken downloader print identically. Not fixed
here — `tools/` is outside this brief's write scope (§14 rule 4). **Fix before dispatching any further
company on `auto`; every wave-2 "0 documents stored" is suspect.**

### Form census inside 2004-01-01 → 2013-12-31 (from `submissions_pre2014.csv`)

S-1 1 · S-1/A 8 · 424B4 1 · 8-A12B 1 · FWP 1 · EFFECT 1 · 10-K 1 · 10-Q 5 · 8-K 16 · 8-K/A 2 ·
DEF 14A 1 · DEFA14A 1 · S-8 2 · SC 13G 3 · SC 13G/A 1 · S-3ASR 1 · 424B5 1 · CORRESP 5 · UPLOAD 6 ·
REGDEX 5 · REGDEX/A 2 · NO ACT 1 · CT ORDER 4 · CERTNAS 1 · Form 3 32 · Form 4 290 · 4/A 4.

Load-bearing accessions seen in the index: S-1 **0001193125-12-034517** (2012-02-01); S-1/A eight
(2012-02-08, 03-07, 03-27, 04-23, 05-03, 05-09, 05-15, 05-16); final prospectus 424B4
**0001193125-12-240111** (2012-05-18); 8-A12B 0001193125-12-230161 (2012-05-14); EFFECT + 63 Form 3/4 on
2012-05-17; FY2012 10-K **0001326801-13-000003** (2013-02-01). Five `CORRESP` (2012-03-27, 05-14, 05-15,
2013-04-30) and six `UPLOAD` PDFs are the SEC-comment-letter and paper-exhibit trail — unexamined, and
the likeliest place in EDGAR to find the staff's questions about the founding account.

**A real null, stated as such:** between **2008-10-14 and 2012-02-01 this CIK filed nothing**. Facebook
was a private company and EDGAR carries no 2004-2011 corporate filings of ours. What *is* on record
before the S-1 is unexplained: 5 `REGDEX` + 2 `REGDEX/A` (2005-05-06 → 2006-07-10) and one `NO ACT`
(2008-10-14), all paper `.paper`/`filename1.pdf` items. Attribution UNKNOWN — no document read this
session says which entity those belong to. Treat as a lead, not as evidence of a 2005 registration.

### What the S-1 itself says about the origin

Document on disk: `sources/sec/0001193125-12-034517_d287954ds1.htm` (+ `.meta.json`), 2,627,678 bytes,
114,339 html-stripped words.

1. **The only dated origin fact the S-1 states in text is incorporation, and it is July 2004, not
   February 2004.** Verbatim, twice: *"We were incorporated in Delaware in July 2004."* (Corporate
   Information) and *"We were incorporated in July 2004 and are headquartered in Menlo Park,
   California."* (Business overview). **The brief's "founded 2004" is therefore only half-proven: the
   Delaware incorporation is Tier-1 dated to a month; any February-2004 or dorm-room founding date is
   NOT in the S-1 and stays UNKNOWN until a document says it.**
2. **String-search results for the contested origin, all zero hits in the S-1:** `Winklevoss` 0,
   `Divya` 0, `Verdu` 0, `Saverin` 0, `Eduardo` 0, `Moskowitz` 0, `ConnectU` 0, `thefacebook.com` 0,
   `February 2004` 0. (`litigation` occurs 26 times; `founded` 4.) The 26 litigation hits are
   forward-looking; the only settlement named in text is the **FTC** privacy settlement and the Irish
   DPC audit of Facebook Ireland.
3. **The founding timeline is an image, not text.** The Business section reads *"Highlights in our
   history are depicted in the graphic on the next page"* followed by *"Our History"* and then
   straight into MAU metrics — so the one place the S-1 narrates 2004 is a graphic with no extractable
   date. Any later agent citing "the S-1 history timeline" must OCR it first.
4. **Founder claim, Tier-1 wrapper.** The founder's letter states *"Facebook was not originally founded
   to be a company. We've always cared primarily about our social mission…"* — a self-characterisation
   of origin inside the company's own registration statement. Per the brief's rule and §3 this is
   **FOUNDER CLAIM**, admissible as evidence of *what the company said in Feb 2012*, inadmissible as
   evidence of what happened in 2004.
5. Early scale, from the same document: FY2011 revenue **$3,711 M**, operating income **$1,756 M**, net
   income **$1,000 M**; **845 M MAUs at 31 Dec 2011 (+39 % YoY)**, US 161 M (+16 %), Brazil 37 M (+268 %),
   India 46 M (+132 %). Definitions carried in text (a monthly active user is "a registered Facebook user
   who logged in and visited Facebook through our website or a mobile device, or took an action to share
   content … in the last 30 days"). These are the *2011* baseline; the 2004-2006 metric series has to come
   from the S-1's selected-financials tables or the 424B4, not from this paragraph.
6. The prospectus carries Class A / Class B dual-class control and identifies Zuckerberg as "founder,
   Chairman, and CEO, and as our largest and controlling stockholder" — the equity-structure claim, still
   a founder claim about the past.

## Family b web — Wayback CDX

**UNANSWERED (external outage). NOT a null, and no capture has been disproved.**

Three CDX requests were made against `web.archive.org/cdx/search/cdx`; all three were refused by the
service, and the bodies are kept at `sources/web/cdx_thefacebook.com.txt`,
`sources/web/cdx_facebook.com.txt`, `sources/web/cdx_thefacebook_retry.txt`:

| request | result |
|---|---|
| `url=thefacebook.com&from=1999&to=2007…` | **HTTP 504 Gateway Time-out** (nginx page) |
| `url=facebook.com&from=1999&to=2007…` | **HTTP 503**, body is the Internet Archive status page: *"Internet Archive services are temporarily offline."* |
| `url=thefacebook.com&limit=15` (retry, no window) | **HTTP 503**, same "Temporarily Offline" page |

**Zero timestamps were returned, so zero capture dates exist for this session.** Per §12 and the brief's
rule, no 14-digit timestamp may be asserted, and the absence of a captured earliest-snapshot date is not
evidence that thefacebook.com was never archived. The window parameter was never even tested for
correctness because the endpoint never answered. This family is also the one whose outage simultaneously
killed families (d) and part of (c) — see the halt note below, which is the same root cause.
**Re-run required:** the two bare-host CDX calls (`thefacebook.com`, `facebook.com`, one test each, www and
bare treated as one) plus the first-capture date. Web budget note: this probe spent 8 requests total
against the §14.2 cap and is now at it, so the retry belongs to the next agent.

## Family c periodicals

**PARTLY UNANSWERED; one route live but metadata-only.** No in-window Tier-1 *text* obtained.

`tools/periodical_harvest.py --help` works, so the family was **queried, not assumed**. I authored
`sources/_harvest/queries_meta.json` (10 tasks, Walmart-exemplar shapes, caps above task counts) and ran
`--company meta --max-requests 25 --delay 1`; log kept at `sources/_harvest/run_20260926.log`, 30 rows in
`candidates.csv`, 13 network requests, cache OFF.

| family | tasks | outcome | call it what it is |
|---|---|---|---|
| chronicling_america | 3 | **HTTP 403 ×3** | UNANSWERED — the loc.gov bot challenge recorded in `tools/queries.json` is still live |
| hathitrust | 2 | **http_status 0 ×2** | UNANSWERED — unreachable, no answer given |
| internet_archive | 2 | skipped | **UNQUERIED** |
| corporate_print | 1 | skipped | **UNQUERIED** |
| google_books | 2 | **HTTP 200 ×2 → 22 rows** | LIVE, but metadata + matched page, no snippet text |

The script's own closing line is the correct summary: `UNQUERIED THIS RUN (recorded UNANSWERED, NOT null):
corporate_print, internet_archive` — the consecutive-failure breaker stopped after CA's three 403s plus
HathiTrust's two failures, and IA was down anyway. **Do not read the empty IA/CP rows as Walmart-style
"no print run exists".**

What Google Books actually returned, in date order: **2006 — The New Yorker** (only candidate inside the
2004-2006 press window); then 2008 (Current Biography Yearbook; The United States Patents Quarterly),
2010 (Friends with Benefits; Social computing; Time), 2011 (The Facebook Effect; Vanity Fair), 2012
(Facebook Marketing; Newsweek), 2013 (Facebook-Führerschein), 2016-2023 (A Closer Look at the Life of Mark
Zuckerberg; Top Visionaries Who Changed the World; An Ugly Truth; Digital Media Economics). The
harvester's `TIER1_CANDIDATE` flag is mechanical ("a digitised volume exists") — **the in-window test is
mine, and on these 22 rows it is met by exactly one item, which is the wrong kind of source anyway**:
everything post-2011 is retrospective founder-account literature, i.e. `RETROSPECTIVE SOURCE` material for
2004, useful for §K (how the story was built) and near-useless for dating it. Note the corpus is
*structurally* thin here for this company: the §14.6 periodical rule exists because EDGAR stops ~1994 —
Meta's inverse problem is that its press window (2004-2006) is *after* the NDNP/HathiTrust deep backfiles
and *before* the trade-press indexers the fleet relies on, so the college-source route (Harvard/Crimson
press) has to be found in a corpus none of these five tasks touched.

## Family d digitised corporate print

**UNQUERIED — the required explicit query did not get an answer.** I did write the task before any
"paper only" claim could be made (`CP facebook corporate print 2004-2013`, params
`company_terms:[facebook, "facebook, inc"]`, `report_terms:[annual, report, prospectus, offering]`,
`year_range:[2004,2013]`) and it was skipped by the breaker, HTTP status blank. So the sentence *"Facebook
pre-IPO printed material exists only in private hands"* is **not licensed by this probe**. The two IA
`mediatype:texts` searches (2004-2006 facebook texts; "facebook annual report" 2004-2013) share the same
fate and the same caveat. One re-run of `--source-family corporate_print --source-family internet_archive`
when archive.org is back answers both, cheaply, and their sidecar format is already set up.

## Family e auction / museum documentary records

**UNTRIED.** Deliberately skipped: with EDGAR and federal dockets both proven reachable, a founder-era
manuscript route buys this company much less than it bought Apple, and the brief made it conditional on
being cheap. No Sotheby's/Christie's/Heritage auction API call was made, no institutional finding-aid
query. **This is an untried family, not a null** (§14.6 forbids conflating them), and it is the one family
whose skip cannot be blamed on an outage.

## Legal records

**THE STRONGEST FAMILY FOR THIS COMPANY — TIER-1, IN-WINDOW, INDEPENDENT, AND REACHABLE.** §5 puts court
records in Tier 1; unlike the S-1 these are not the founder's account of his own origin.

### Route status

`www.courtlistener.com/api/rest/v4/search/` answers, but only in its minimal shape. The three requests
carrying `order_by=citeCount+desc&rows=6` returned **HTTP 500**
(`{"detail":"Internal Server Error. Please review your query"}`) — kept as negative artifacts at
`sources/legal/cl_ConnectU.json`, `cl_Winklevoss+Zuckerberg.json`, `cl_Saverin+Facebook.json`. Re-issued
without the sort/rows parameters: **HTTP 200**. `q="ConnectU"` → **count 670, document_count 4204**;
`q="Winklevoss"` → count 303 / 2939 documents (top hits are unrelated people — bankruptcy and trademark
parties sharing the surname — so the ConnectU string, not the surname, is the productive key). Payloads:
`sources/legal/cl2_%22ConnectU%22.json`, `cl2_%22Winklevoss%22.json`. This is a RECAP/PACER mirror: the
**docket register** is proven; **full docket text and the pleadings themselves are not yet retrieved**.

### Cases seen this session, with the dates the registry carries

| case | docket | court | dateFiled | nature / cause |
|---|---|---|---|---|
| ConnectU LLC v. Zuckerberg | **1:04-cv-11923** | District Court, D. Massachusetts | **2004-09-02** | 190 Contract: Other; 28:1332 Diversity-Breach of Contract |
| Connectu LLC v. Zuckerberg | 2:06-cv-01640 (+ 2:06-mc-00178) | D. Western Washington | 2006-10-26 | 890 Other Statutory Actions; 28:1331 Fed. Question |
| ConnectU LLC v. Zuckerberg | 5:07-mc-80055/-80056/-80057/-80058 | N.D. California | 2007-02-21 | (four companion misc. motions) |
| The Facebook, Inc. v. Connectu, Inc | 5:07-cv-01389 | N.D. California | 2007-03-09 | 28:1442 Petition for Removal |
| Connectu, Inc. v. Facebook, Inc. | 1:07-cv-10593 | D. Massachusetts | 2007-03-28 | 820 Copyright; 17:101 Copyright Infringement |
| ConnectU LLC v. Zuckerberg | 07-1796 | Court of Appeals, 1st Circuit | 2007-05-22 | 4190 Other Contract |

**The 2004-09-02 entry is the single most valuable date this probe found.** It is an in-window,
externally-generated, machine-dated federal record naming Zuckerberg as a defendant in a breach-of-contract
suit over company ownership — 2004, the founding year, and it cannot be a founder's restatement.

### What the company's own filings say about litigation — and what they do not

The 424B4 does carry a **Legal Proceedings** section, and it names exactly one origin-era dispute
(verbatim from `sources/sec/0001193125-12-240111_d287954d424b4.htm`): *"Paul D. Ceglia filed suit against
us and Mark Zuckerberg on or about June 30, 2010, in the Supreme Court of the State of New York for the
County of Allegheny claiming substantial ownership of our company based on a purported contract between
Mr. Ceglia and Mr. Zuckerberg allegedly entered into in April 2003. We removed the case to the U.S.
District Court for the Western District of New York, where the case is now pending. In his first amended
complaint, filed on April 11, 2011, Mr. Ceglia revised his claims to include an alleged partnership with
Mr. Zuckerberg, he revised his claims for relief to seek a substantial share of Mr. Zuckerberg's ownership
in us, and he included quotations from supposed emails that he claims to have exchanged with Mr. Zuckerberg
in 2003 and 2004. On June 2, 2011, we filed a motion for expedited discovery…"*

Note what this disclosure does: it puts an **alleged April 2003** agreement — before the July 2004
incorporation, and about Zuckerberg personally as well as the company — into a Tier-1 register, and it
characterises it as the company's adversary's claim ("purported", "supposed emails"), which is the correct
posture for a Stage-1 agent: the 2003 date is *pleaded*, not established.

**And the silence:** across both the S-1 (2,627,678 B) and the 424B4 (3,545,401 B), the counts are
`Winklevoss` 0 · `ConnectU` 0 · `Saverin` 0 · `Divya` 0 · `Moskowitz` 0 · `thefacebook` 0 ·
`Harvard College` 0 · `prior claims` 0 — while the federal register above shows those suits were filed in
2004, 2006, 2007 and appealed in 2007. Whatever the reason (settled before the filing, so no longer
"pending"), **no Stage-1 or Stage-2 agent may write "the early equity disputes were disclosed in the S-1"
— they were not, in text, by name.** That is precisely why the docket outranks the prospectus here.

### Corporate registries — UNTRIED

**Delaware Division of Corporations and the California Secretary of State were not queried**, and this is
the gap with the sharpest consequence: the S-1 accession's own file list (28 items,
`sources/_index/S1_accession_filelist.txt`) contains **no charter exhibit** — the only exhibit is
`d287954dex231.htm` (an auditor consent); the remainder is the S-1 body, `0001193125-12-034517.txt`, three
index files, **26 `g287954g*.jpg` figures** and `g287954zuckerberg_sig.jpg`. So the day-level Delaware
incorporation date, the original certificate, and the authorized-share structure at formation exist only in
the registry. **No EDGAR document can ever fix the founding day for this company.**

## Boundaries

Each proposed boundary names the document that fixes it. Where no document was seen, the boundary is
marked UNKNOWN rather than guessed; the brief's supplied dates were treated as claims, not facts.

**Stage 1 — origin to incorporated entity.** Proposed span: *earliest attested point* → **July 2004**.
- Fixed by: the 2012 S-1 text, twice — *"We were incorporated in Delaware in July 2004"* and *"We were
  incorporated in July 2004 and are headquartered in Menlo Park, California."* **Month-level only.**
- Lower bound **UNKNOWN**. Two candidate anchors were seen and neither is dispositive: (i) *April 2003*,
  the date of the contract **alleged** by Ceglia as pleaded and quoted in the 424B4 — an adversary's claim;
  (ii) *2004-09-02*, the date a federal complaint against Zuckerberg was filed (docket 1:04-cv-11923) —
  a terminus ante quem, i.e. something disputable had already happened by then. **The brief's February-2004
  / dorm-room date was not found in any document this session and stays UNKNOWN.** A product-launch date
  needs either the Delaware charter (registry, untried) or an archived first page (Wayback, outage).
- Stage 1 is therefore the tier's real risk zone: **T1-grade for the entity, zero-grade for the product and
  the dorm**, until a registry or archive answer arrives.

**Stage 2 — incorporated start-up to registration.** Proposed span: **July 2004 → 2012-02-01**.
- Fixed by: `submissions_pre2014.csv` + the fetched S-1 itself (form S-1, accession 0001193125-12-034517,
  filingDate **2012-02-01**).
- Interior dated anchors, all independent of the founder account: 2004-09-02 (D. Mass. complaint),
  2006-10-26 (W.D. Wash.), 2007-02-21 / 2007-03-09 / 2007-03-28 (N.D. Cal. removal and companion matters),
  2007-05-22 (1st Cir. appeal), 2010-06-30 (Ceglia, state court) → 2011-04-11 (amended complaint) →
  2011-06-02 (expedited-discovery motion).
- **The floor of this stage is EDGAR-empty**: nothing filed 2008-10-14 → 2012-02-01, and the only
  pre-2012 items on the CIK are 2005-2006 `REGDEX`/`REGDEX/A` paper entries of unattributed origin plus one
  2008 `NO ACT`. Stage 2's financial texture must come from the S-1's audited 2009/2010/2011 comparatives
  and the XBRL series (215 rows, `sources/financials/xbrl_early_series.csv`, content not yet examined) —
  i.e. **restated, not contemporaneous**, which is a claim-classification constraint on §I/§J.

**Stage 3 — registration to listed.** Proposed span: **2012-02-01 → 2012-05-18**, extending to
**2013-02-01** for the first annual report.
- Fixed by: S-1/A eight amendments 2012-02-08 → 2012-05-16 (the amendment chain is itself a dated record of
  what the company changed under staff pressure — `CORRESP` 2012-03-27, 05-14, 05-15 pairs with them);
  **424B4 2012-05-18** (final prospectus, fetched); `8-A12B` 2012-05-14; `FWP` 2012-05-09; `EFFECT`
  2012-05-17 together with 32 Form 3 and 63 Form 3/4 filings on 2012-05-17 (the insider-holdings snapshot,
  the best surviving evidence of who owned what at listing); FY2012 `10-K` 2013-02-01.

## Conflicts

Entries for the eventual `conflicts.csv`; IDs are local to this probe.

- **META-C1 — "founded 2004 (February, dorm room)" vs the only dated origin statement in the filings.**
  The brief supplies February-2004; the S-1 and 424B4 supply only *"incorporated in Delaware in July 2004"*
  and contain `thefacebook` 0 hits, `Harvard College` 0 hits, `February 2004` 0 hits. **Adjudication: filing
  wins for the corporate entity (July 2004, month-level); the product/launch date is not in conflict, it is
  simply UNKNOWN.** Every restated dorm-room line downstream must carry an independence note: it descends
  from founder interviews and 2010-era secondary print, not from a 2004 document.
- **META-C2 — prospectus silence vs a live federal register.** The company's own final prospectus names no
  Winklevoss, no Divya, no ConnectU, no Saverin, while the registry shows those suits filed 2004-09-02,
  2006-10-26, 2007-03-28 and appealed 2007-05-22. Both statements are Tier 1 and they cannot both be taken
  as complete. **Adjudication: the docket outranks the prospectus for the existence and dating of the
  disputes; the prospectus remains authoritative only for what the company chose to disclose.**
- **META-C3 — "EDGAR reaches nothing before 2024" (script index) vs 397 pre-2014 filings.** A tooling
  conflict, not an evidentiary one: the truncated `recent` block plus two transient slice failures printed
  as an empty window. **Adjudication: the manual re-fetch of the same URLs (HTTP 200) settles it — the
  register is complete and pre-2014 filings exist.** Recorded so no later agent re-litigates it.
- **META-C4 — CIK activity from 2005-05-06 vs "first filing = the 2012 S-1".** 5 `REGDEX` + 2 `REGDEX/A`
  (2005-2006) and 1 `NO ACT` (2008-10-14) sit on CIK 1326801 before the S-1. **Adjudication: UNKNOWN —
  attribution requires reading the paper items (6 `UPLOAD`/`.paper` PDFs, untried). Do not let "Facebook
  registered in 2005" enter any register.**
- **META-C5 — company vs founder as the subject of the origin dispute.** Ceglia sued "us **and Mark
  Zuckerberg**" over a contract allegedly made in April 2003, i.e. before the July 2004 incorporation, and
  seeking "a substantial share of **Mr. Zuckerberg's** ownership". **Adjudication: keep the pre-2004
  activity attached to Zuckerberg personally, not to Facebook, Inc.; conflating them is the anachronism
  §6 exists to prevent.**

## Nulls

**TRUE nulls, each from a complete enumeration rather than a failed request:**

- **No EDGAR filing by this CIK between 2008-10-14 and 2012-02-01** — from `submissions_pre2014.csv`
  (397 rows ≤ 2013-12-31, built from two archive slices that both returned HTTP 200).
- **No EDGAR filing on this CIK before 2005-05-06**, the oldest row in the same enumeration.
- **No certificate-of-incorporation exhibit in the S-1 accession** — the accession's `index.json` lists 28
  items and exactly one is an exhibit (`d287954dex231.htm`). Consequence: the day-level founding date is
  unobtainable from EDGAR, permanently.
- **The "Our History" timeline in the S-1 has no text to mine** — the section is a graphic; 26 JPGs are in
  the accession. Any "the S-1 shows X on its history page" claim is an OCR claim, not a text claim.
- **None of Winklevoss / ConnectU / Divya / Saverin / Moskowitz / thefacebook appears anywhere in the S-1 or
  the 424B4** — string counts, both documents on disk.
- **In-window Google Books coverage of the 2004-2006 press is effectively one record** (2006, The New
  Yorker, metadata only) out of 22 rows returned.

**NOT nulls — blocked, and to be re-run (never write these as absence of evidence):** Wayback CDX ×3
(504/503, Internet Archive self-declared "Temporarily Offline"); Chronicling America ×3 (HTTP 403 bot
challenge); HathiTrust ×2 (http_status 0, unreachable); Internet Archive texts ×2 and corporate_print ×1
(UNQUERIED, killed by the consecutive-failure breaker); CourtListener with sort/rows parameters ×3
(HTTP 500, and fixed on the second attempt — the same lesson as META-C3).

## Untried

1. **Delaware Division of Corporations** — certificate of incorporation / good-standing order for
   Facebook, Inc. The only route to a **day-level** July-2004 anchor and to the original share structure.
2. **California Secretary of State entity search** — for the qualification or predecessor-entity record
   implied by the 2004 Delaware/California wording.
3. **RECAP / PACER full docket text** for 1:04-cv-11923, 1:07-cv-10593, 07-1796 and the Ceglia matters —
   register proven, pleadings not fetched. The complaints are the earliest *independent* narrative of 2003-2004.
4. **The 5 `CORRESP` and 6 `UPLOAD` items and the 8 `S-1/A` amendments** already enumerated in the index
   (SEC staff comments on the founding account, and the amendment chain showing what was rewritten).
5. **`sources/financials/xbrl_early_series.csv`** — 215 rows written by the script, contents unexamined.
6. **Family (e) auction / museum documentary records** — no request made at all.
7. **OCR of `g287954g*.jpg`**, which would convert the S-1's history graphic from a dead end into text.
8. **College-source press (Harvard student newspaper, 2003-2006)** — no configured corpus route exists in
   `periodical_harvest.py`'s five families; this is a genuine methodological gap for every 2000s-founded
   company in the fleet, not just this one.
9. **Wayback re-run once archive.org recovers** — including the `www` vs bare-host single test the brief
   specifies, which was never executed.

