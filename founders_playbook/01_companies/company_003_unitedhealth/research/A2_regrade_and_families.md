# A2 — UNITEDHEALTH GROUP (rank 3) RE-GRADE AND FIVE-FAMILY PROBE

PROBE agent `probe-unitedhealth`, run 2026-09-25/26 (UTC timestamps on every artefact).
Purpose: **re-measure** the old provisional verdict in `A_chronology_feasibility.md` (UH-01…UH-45) on
working tooling, family by family per §14 rule 6, and issue a **per-stage** tier per §15.2 as amended by
the RD-112 ruling (a tier is measured against that stage's own window, never against the probe's search
range). This file does not restate A's verdict; it re-runs the routes A could not run.

**Transport disclosure (mandatory).** The first harvest run used `--insecure` (this machine's stale CA
store). Because unverified bytes cap at Medium, the three families that answered at all were **re-run
without `--insecure`** at 21:04 UTC and returned HTTP 200 with verified TLS (`google_books`,
`corporate_print`, `internet_archive`); two evidence files were versioned beside the earlier copies.
`chronicling_america` and `hathitrust` were not re-testable (403, below). All citations below are to
bytes held under `sources/`; nothing is asserted from a search-result rendering that was not in a
saved response body.

## Verdict per stage

Per RD-112 the tier is a property of a **stage window**, not of the company. Windows used are the ones
proposed in the Boundaries section (they are the windows this probe can defend with documents).

| Stage | Window graded against | Families returning **in-window Tier-1 text** | Families tried but null / unanswered / untried | **Tier** | §15.2 cap | §15.2 agent runs |
|---|---|---|---|---|---|---|
| **1 — origin** | 1974?–1993-12-31 | **(c) periodicals = 1** (Google Books feed: 1978 federal serial + 1981 reprint naming "Charter Med, Minneapolis"; undated DHHS serial) | (a) NO for this window — earliest held/ indexed text is 1995-02-02, it post-dates the window (the Dell shape); (b) NO — first-party web floor 1996-12-27; (d) **documented NULL** (2 queries, HTTP 200, `numFound:0`); (e) **UNTRIED** (no verified endpoint, no query block); (c) on Chronicling America + HathiTrust **UNANSWERED** (403) | **T3 register** | 8k words/stage | 3–4 |
| **2 — scale-up on the record** | 1995-01-01–1998-12-31 | **(a) filings** (4 documents newly held, 713,127 B / 86,729 words; 22 index rows 1977-01-01→1995-12-31 of which 17 are 1995) and **(b) web archives** (1996-12-27 root, 1997-02-18 `/about` tree, 1999-01-25 — the 1996–97 captures fall inside this window) | (c) NO in-window periodical (GB in-window rows are 1990, 1994, 1995 and are false-positive titles); (d) window of the CP queries stopped at 1995 → 1996-98 **UNTRIED**; (e) **UNTRIED** | **T2 core** | 22k words/stage | 6–9 |
| **3 — enterprise formation and the rename** | 1999-01-01–2000-03-06 | **(a) filings** (FY1999 10-K, DEF 14A 2000-04-07, 8-K 0000912057-00-010247 all held) and **(b) web** (held capture `wb_19991128085132…about_index.html`, plus the 1999-01-25 `unitedhealthgroup.com` CDX row) | (c) 1996-01-01→2000 periodical window **UNTRIED** (every query block in `tools/queries.json` for this company stops at 1985/1995); (d) **UNTRIED** for this window; (e) **UNTRIED** | **T2 core** (T1 reachable: 1999-2000 trade press is dense and EDGAR FTS sees it) | 22k words/stage | 6–9 |

**Company planning tier = the minimum across stages = T3 (register).** That is the number the fleet may
budget against; it does **not** downgrade Stages 2 and 3, which are dispatched at T2.

**Is the old provisional verdict overturned?** **Partly — overturned on the reason, confirmed on the
number.** A recommended "forensic-core (~6,000 words) for Stage 1 … not the exemplar", with confidence
capped at Medium because the one class that could move it (digitised periodicals) was answered by a
Google Books **HTTP 429** and nothing else. That premise is now dead: the 429 is **answered** (HTTP 200,
23,604 B of feed held) and the periodical family returned **in-window Tier-1 candidates** for 1978 and
1981 — the first contemporaneous text for this company's founding window that has ever been held in this
dossier. But one family is one family: §15.2 counts families, not items, so Stage 1 sits at **T3**, not
exemplar and not forensic-core. The old verdict's *size* call survives; its *evidence base* does not, and
its "not one word may assert that contemporaneous 1974-90 coverage does not exist" discipline is now
**fulfilled rather than merely promised** — coverage exists, and it says Charter Med was in Minneapolis
managing IPAs.

STATUS: WRITTEN 2026-09-25
## Family a filings

Re-measured with `python tools/sec_intake.py resolve --ticker UNH` → `{"ticker": "UNH", "cik": 731766,
"name": "UNITEDHEALTH GROUP INC"}`, then `auto --ticker UNH --company-dir <dir> --from 1977-01-01 --to
1995-12-31`.

* **Index:** `index: 4330 filings from UNITEDHEALTH GROUP INC (UNH)`. A local join of the three held
  index files (`EDGAR_submissions_CIK0000731766.json` recent block + `_submissions-001.json` +
  `_submissions-002.json`) yields **4,315 rows**. The 15-row delta is **UNANSWERED** (RD-112's silently
  dropped nameless-row defect), not a null.
* **Earliest form and date in the index** (ascending): `1995-02-02 SC 13G/A 0000729057-95-000082`, then
  `1995-02-10 SC 13G`, `1995-02-14 8-K 0000950131-95-000333`, `1995-02-14 SC 13G/A` ×2,
  `1995-03-15 PRE 14A`, `1995-03-17 8-K/A`, `1995-03-28 10-K405 0000950131-95-000748`,
  `1995-03-31 DEF 14A 0000950131-95-000820`, `1995-04-04 SC 13G/A`, `1995-05-04 8-K` / `S-8`.
* **Earliest form and date HELD:** also **1995-02-02 SC 13G/A** — there is now **no gap** between the
  index floor and the held floor. `auto` stored **4 documents / 713,127 B / 86,729 words, 0 UNANSWERED**;
  `_UNANSWERED.csv` is header-only (68 B). Held under `sources/sec/`: `0000729057-95-000082` (SC 13G/A),
  `0000950131-95-000333` (8-K), `0000950131-95-000748` (10-K405, 521,735 B), `0000950131-95-000820`
  (DEF 14A, 112,968 B), each with a `.meta.json` sidecar and a `_MANIFEST.csv`.
* **The known starting fact is CONFIRMED and sharpened.** The floor is 1995-02-02 and it is a third-party
  SC 13G/A, filed by **The Prudential Insurance Company of America**, Prudential Plaza, Newark NJ (held
  bytes, lines 130-141), issuer address given as **Minnetonka, MN 55343** (line 128), CUSIP 910581107.
  Its own ownership fields are blank: `ITEM 1(11) PERCENT OF CLASS … Not Applicable` (line 116) — a blank
  field, **not** a stake, and unusable as evidence of holdings. **No S-1 or S-1/A exists anywhere in the
  4,315 indexed rows** (prefix filter returned `[]`), so A's "no initial registration in the electronic
  record" is re-measured and stands.
* **What is genuinely new: the earliest company-authored origin sentence is now held, four years earlier
  than A could reach.** FY1994 Form 10-K405 (filed **1995-03-28**), line 168: *"United HealthCare
  Corporation is a Minnesota corporation, incorporated in January 1977. Unless the context otherwise
  requires, the terms "UHC" and "Company" refer to United HealthCare Corporation and its subsidiaries.
  The Company's executive offices are located at 300 Opus Center, 9900 Bren Road East, Minnetonka,
  Minnesota 55343"*. A's earliest instance of that sentence was the FY1998 10-K of 1999-03-31 (UH-09).
* **Same document, same proxy, governance facts pushed back to 1995.** DEF 14A filed **1995-03-31**,
  lines 358-363: *"Mr. Burke has been a member of the Company's Board of Directors since the Company's
  inception and was its Chief Executive Officer until February 1988. Mr. Burke was Chief Executive Officer
  of Physicians Health Plan of Minnesota, now part of Medica, a large HMO managed by the Company, from
  1977 to August 1987. … Mr. Burke is also a director of Education Alternatives, Inc. and First Cash, Inc.
  Mr. Burke is currently retired from active business pursuits."* Director table gives `Richard T. Burke
  51 Director` with columns **Name / Age / Position only** — there is **no "DIRECTOR SINCE" column in the
  1995 proxy**, so the `DIRECTOR SINCE 1977` datum (A's UH-13 tie-breaker) is still only reachable from
  the 1999/2000 proxies. Auditor-since-1981 recurs at line 1649 ("since 1981").
* **Financial floor unchanged.** The FY1994 10-K405 carries **no numbers either**: Item 6, Item 7 and
  Item 8 incorporate the "Annual Report to Shareholders for the fiscal year ended December 31, 1994" by
  reference (lines 1187-1210) — the same by-reference trap A found in FY1999 (UH-22). The earliest
  company-authored **figures** therefore remain FY1993, from the 1998 S-4 (A/UH-21, bytes held at
  `sources/S4_0001047469-98-022543_filed-1998-06-02.txt`; **not re-opened in this session**).
* **In-window row census** (1977-01-01→1995-12-31, 22 rows): 8-K ×6, SC 13G/A ×4, S-8 ×3, 10-Q ×3,
  8-K/A ×2, SC 13G, PRE 14A, 10-K405, DEF 14A ×1 each. **17 of the 22 are 1995-only; 1977-1994 = 0 rows.**
* **Verdict for family (a):** for **Stage 1 the answer is a documented NULL-by-date** (nothing exists in
  the electronic record inside the window) — not a null about the past, since file number 001-10864 is
  already attached to 1995 filings, so a §12(b) registration predates the floor on paper (A/UH-04).

STATUS: WRITTEN 2026-09-25
## Family b web

**Carried, not re-probed** (0 web calls spent here; the CDX route is scripted, not agent-run, and my
remaining budget went to the families that decide the tier). Status from held bytes on disk: earliest
first-party capture **1996-12-27 12:26:52, HTTP 200, 784 B** at `www.unitedhealthcare.com` root; the
`/about` tree crawled **1997-02-18** (three page bodies held, incl. `wb_19970218070514…over.html.html`
whose text is *"United HealthCare is a national leader … since 1974"* and, lower on the same page, *"For
more than 20 years"*); `unitedhealth.com` floor 1998-12-02; `unitedhealthgroup.com` floor 1999-01-25;
`wb_19991128085132…about_index.html` held. Consequence: family (b) is **out-of-window for Stage 1** and
**in-window for Stages 2 and 3**. Known cache-integrity trap preserved from A/UH-45: the file named
`probe_wayback_uhgcom_prefix_allpaths.txt` contains **no `uhg.com` rows at all** (all 4,656 rows are
`unitedhealthgroup.com`) — so that host is **UNTRIED, not null**, and it stays on the Untried list with a
command. Naming caution for later agents, which is exactly the "misnamed host = false null" risk in the
brief: three different hosts answer three different questions (`unitedhealthcare.com` = the 1996-97 brand
story; `unitedhealthgroup.com` = the group brand's live date; `uhg.com` = unknown).

STATUS: WRITTEN 2026-09-25
## Family c periodicals

**This is the family that decided the re-grade.** `python tools/periodical_harvest.py --company
unitedhealth --out sources/periodicals/HARVEST_A2 --max-requests 45 --insecure` ran all 15 query blocks
registered for this company in `tools/queries.json` (5 chronicling_america, 4 internet_archive, 2
hathitrust, 2 google_books, 2 corporate_print), 15 requests, 46 candidate rows, 15 evidence files +
sidecars, then a verified-TLS re-run of the three live families (8 requests, 47 rows, 17 files).

Per-family outcome of the run (the tool's own tallies, this egress, cache OFF):

```
chronicling_america  tasks=5 fetched=5 http={'403':5} rows={'UNANSWERED':5}   HOST HALTED: www.loc.gov
hathitrust           tasks=2 fetched=2 http={'403':2} rows={'UNANSWERED':2}
google_books         tasks=2 fetched=2 http={'200':2} rows={'LEAD_ONLY':8,'TIER1_CANDIDATE':3,'NULL':1}
internet_archive     tasks=4 fetched=4 http={'200':4} rows={'NULL':2,'LEAD_ONLY':20,'TIER1_CANDIDATE':1}
```

* **Google Books is ANSWERED (the old 429 is gone).** `sources/periodicals/HARVEST_A2/google_books/
  897cacbf3eb39aa4.xml`, HTTP 200, 23,604 B, feed title `Search results for "Charter Med" Minneapolis`,
  **10 occurrences of "Charter Med" in the held body**. In-window entries, all with `view_all_pages`:
  1. `dc:date 1978`, `dc:creator United States. Office of Health Maintenance Organizations`, matched page
     `RA7`: *"… Charter Med , Minneapolis , which manages ten IPAs around the coun- try . " Certainly
     lenders will look more fa- vorably on HMOs managed by us or some- one like us in terms of their
     willingness to put up money . ""* — contemporaneous 1978 federal-agency serial naming **Charter Med
     of Minneapolis as a manager of IPA-model HMOs**. This is the first in-window contemporaneous text
     ever held for this company's origin.
  2. `dc:date 1981`, title `HMO Focus`, page `PA4`: **the identical passage**. Under §3 this is **one
     lineage, not two witnesses** — a reprint or shared copy.
  3. undated `DHHS Publication No. (PHS).`, page `PA5`: *"… Charter Med of Minneapolis , Medserco of St.
     Louis , Hancock , Dikewood of Albuquerque , and Healthplans Corporation of Nashville . For - Profit
     HMOs Currently , 46 for - profit plans are in operation , 25 of which are federally…"* — a for-profit
     HMO-manager cohort list. **Date UNKNOWN**: it must not be pushed into the 1970s.
* **Two false positives to reject, logged so nobody re-imports them:** the `Metropolitan Health Plans`
  query's "TIER1_CANDIDATE" rows are a 2013 Springer book (`Data-Book of Happiness`, PA128, "metropolitan
  health plans, proportionally stratified by marital status") and a 2003 `Computerworld` item (PA35) —
  neither is the corporate entity. And a 1990 `Modern Healthcare` row, *"Charter Medical Corporation is
  the nation's largest and fastest growing private psychiatric / acute care provider … MINNEAPOLIS, MN"*
  is **a different Minnesota company** — the classic Charter-Med/Charter-Medical naming trap.
* **The `Metropolitan Health Plans` route therefore returned nothing that touches the alleged 1984 naming
  dispute.** That is an answer on this endpoint pair (Google Books), and it is the first time the dispute
  story has been tested against a periodical corpus at all.
* **Internet Archive: two different nulls must not be conflated.** The harvest's IA tasks returned HTTP
  200 with `numFound: 0` for `"charter med" … YEAR:[1971 TO 1985]` and for `metropolitan health plans`
  (`b23e6760fc44a7fc.json`, `fecdd35bbab49069.json`, 425 B and 433 B) plus 20 LEAD_ONLY metadata rows.
  But per `tools/ia_text.py`'s own docstring, **advancedsearch `text:` matches an item's annotations, not
  its OCR pages** — so those zeros are **NOT coverage nulls**. I confirmed the same shape independently
  (`numFound 0` for `"charter med" AND mediatype:texts`, and `numFound 0` for
  `title:("focus on health maintenance organizations")`, i.e. the 1978 serial is not on IA under that
  title). **The download-the-OCR-layer-then-grep route — the only route that can prove an IA periodical
  null — is UNTRIED**, and is the top item on the Untried list.
* **Chronicling America and HathiTrust are UNANSWERED, not null:** `www.loc.gov` hard-stopped after 5
  consecutive **403**s (bot challenge); `babel.hathitrust.org` 2× **403** (same stale-CA artefact the
  tool documents). Raw challenge bodies are held (5 × ~6.3 KB and 2 × ~6 KB of HTML). This machine's
  egress cannot clear them; **awaiting runner egress** (nightly GitHub Actions).

STATUS: WRITTEN 2026-09-25
## Family d corporate print

**A documented NULL on a correctly-shaped query — and a still-open naming hole.** Both tasks returned
HTTP 200 verified-TLS with the executed query echoed inside the response, and `numFound: 0`:
`(title:unitedhealth OR title:"united health care" OR title:"charter med" OR title:"metropolitan health
plans") AND (title:annual OR title:reports OR title:shareholder OR title:stockholder) AND
mediatype:texts AND year:[1977 TO 1995]` → `{"numFound":0,"docs":[]}`; and
`(creator:"united health care" OR creator:unitedhealth OR creator:"united health systems") AND
mediatype:texts AND year:[1971 TO 1995]` → `{"numFound":0,"docs":[]}`.
Files: `sources/periodicals/HARVEST_A2/corporate_print/66cf5198d8b39c00.json`, `bc2fe717779012f4.json`.
The query shape is the one **verified** by the Walmart reference hit in `tools/queries.json`
(`_corporate_print_reference_exemplar`, `numFound=27`, 1972 FY report fetched to 23,989 B of OCR), so
this is a real negative about **Internet Archive's corporate-print holdings for these strings** —
unlike A, which had no corporate-print result at all to report. Three limits, stated plainly: (i) the
name set is built only from strings I have seen in held bytes (`unitedhealth`, `"united health care"`,
`"charter med"`, `"metropolitan health plans"`, `"united health systems"`) — the registrant's own
**1995-era legal name string "United HealthCare Corporation"** was never tried as a `creator:` term, and
the FY1994 filing shows the house naming family uses `HealthPlan`/`Health Plans` variants (`United Health
Plans New England, Inc.`, `Physicians HealthPlan of North Carolina`) which no query used; (ii) the window
stops at 1995, so 1996-1998 is untested; (iii) the by-reference trap makes the missing object precisely
identifiable — the **Annual Report to Shareholders for FY1994** exists as a document (the 10-K405 names
it, its auditor's report pages 22-32, and its "Financial Highlights" section) and is **not held anywhere
in this dossier**. Corporate print for Stages 2 and 3 therefore stays **UNTRIED**, not null.

STATUS: WRITTEN 2026-09-25
## Family e documentary

**UNTRIED — and the reason is named, not an absence I measured.** `tools/queries.json` carries 15 tasks
for `unitedhealth` across exactly five source families (`chronicling_america`, `internet_archive`,
`hathitrust`, `google_books`, `corporate_print`); there is **no auction/museum/museum-collection task
block for this company, and no endpoint for that family has been verified for it**. Per §14 rule 6 and
§15.1 an untried family is reported untried and never folded into a null, and per §15.1 no agent may
improvise an unverified endpoint. The Apple precedent (founding documents surviving at auction) makes
this the family most likely to add Stage-1 Tier-1 artefacts — a 1977-88 certificate, a stock certificate,
a Hennepin County Medical Society or PHPMN contract, a Warburg Pincus-era document — and it is also the
family whose absence caps this probe's completeness claim. Its first action is a query-block authoring
task for the orchestrator, not a fetch.

STATUS: WRITTEN 2026-09-25
## Entity and naming question

The brief's three candidate answers resolve to **three different questions**, and one of A's strings is
now falsified:

1. **What the register holds.** `sources/EDGAR_submissions_CIK0000731766.json` re-read this session:
   top-level `"formerNames":[{"name":"UNITED HEALTHCARE CORP","from":"1995-04-04T04:00:00.000Z","to":
   "2000-02-14T05:00:00.000Z"}]`, current `name: UNITEDHEALTH GROUP INC`, `entityType: operating`. **One
   former name only; no EDGAR field records any 1977, 1978 or 1984 name.** Documented null, re-measured.
2. **What the company's own words hold.** Earliest held: 1995-03-28 — *"United HealthCare Corporation is a
   Minnesota corporation, incorporated in January 1977"*. The Fortune row's name, "UnitedHealth Group",
   is legal only from **2000-03-06** (8-K 0000912057-00-010247, held), i.e. anachronistic by ~23 years.
3. **The predecessor name in contemporaneous print — NEW ANSWER.** The 1978 federal serial spells it
   **"Charter Med , Minneapolis"** and describes it as managing ten IPAs; the undated DHHS serial spells it
   **"Charter Med of Minneapolis"**. Neither the 1978 nor the 1981 nor the DHHS snippet uses "CharterMed"
   as one word, and none names a founder, a year of establishment, or a corporate suffix. So: **the
   founding-window name to search is the two-word "Charter Med", not "CharterMed"** — which matters
   mechanically, because A's only periodical probe (`googlebooks_chartermed.json`) and the EDGAR company
   search (`EDGAR_companysearch_CHARTERMED.xml`) both used the one-word form, and the earlier "Charter Med"
   FTS test (A/UH-29) returned 8 hits that belonged to other filers. A single-token misnomer produced
   exactly the false null the brief warned about.
4. **"Healthplan" vs "Health Plan" — A's negative is now too strong.** A/UH-40 reported that the local
   corpus contained no `United Healthplan`. Held bytes now show `Physicians HealthPlan/SM/ of North
   Carolina`, `United Health Plans New England, Inc./SM/`, `Share/SM/ Health Plan of Illinois` and
   footnote *"Medica includes the combined operations of the health plans previously known as Physicians
   Health Plan/SM/ of Minnesota and Share/SM/, both of which were provided management services by the
   Company"* (FY1994 10-K405, lines 270-341). Whether the exact string `United Healthplan` occurs in the
   four newly-held documents is **not yet tested** — one-command item, in the Untried list.
5. **Geography is a naming question too, and the brief's premise fails.** Founded **in Eden Prairie** is
   unsupported anywhere: the earliest held company text places executive offices at *300 Opus Center, 9900
   Bren Road East, Minnetonka, Minnesota 55343* (1995-03-28), and the earliest held third-party filing
   gives the issuer as *Minnetonka, MN 55343* (1995-02-02). **Eden Prairie (1 Health Drive, 55344) is the
   live EDGAR business address only**; the date of any move is **UNKNOWN**, and the 1977 locality is
   **UNKNOWN** (1978 print says only "Minneapolis" for Charter Med). Any Stage-1 sentence locating the
   founding in Eden Prairie is anachronistic on this evidence. The 1977 founding year itself remains
   unverified to the month: A's `DIRECTOR SINCE 1977` column is still only reachable from 1999/2000
   proxies, since the newly-held 1995 proxy has no such column.

STATUS: WRITTEN 2026-09-25
## Boundaries

| Stage | Proposed boundary | Document that fixes it (held bytes unless noted) | Confidence |
|---|---|---|---|
| 1 start | **1977-01** (registrant's own incorporation month) | FY1994 Form 10-K405, filed 1995-03-28, line 168 — now the earliest instance of the sentence, four years earlier than A's earliest | High that the company said it under liability in 1995; Medium that January 1977 is the event date; **the day is UNKNOWN** |
| 1 preamble | **1974 — labelled "asserted, not dated by any in-window document"** | Contemporaneous 1978 serial establishes that **a Minneapolis firm called Charter Med existed by 1978 and managed ten IPAs** (held GB feed). The 1974 start date itself still rests only on the 1996-97 web page ("since 1974") and the 2022 Star Tribune | **UNKNOWN** for 1974 as a founding date; **High** for "Charter Med of Minneapolis existed in 1978 as an HMO manager" — that pair is the new, honest formulation |
| **1 end / 2 start** | **1994-12-31 / 1995-01-01** — moved **one year later** than A's 1993-12-31 | Fixed by a document rather than by an archive edge: the FY1994 10-K405 (filed 1995-03-28) is the first company-authored document reporting **on** a full year inside the record, and the EDGAR index floor is 1995-02-02 with 17 of the 22 pre-1996 rows inside 1995 alone. Stage 1 therefore ends at the close of the last year narrated by a held first-party document | High for the 1995-01-01 opening of the filing era; **Medium for the split itself — it is a decision, flagged as such** |
| 1 internal marker | **1987-08** (PHPMN CEO ends) and **1988-02** (United CEO ends), two separate dated events | DEF 14A filed 1995-03-31, lines 358-362 — earliest held statement of both | High as registrant statements; the *motive* ("bitter public dispute") remains Tier-2 only |
| 2 end / 3 start | **1998-12-31 / 1999-01-01** | Unchanged from A: FY1998 10-K (held) is the first annual document written under the "UnitedHealth Group" brand while the conformed name is still UNITED HEALTHCARE CORP; corroborated by the 1999-01-25 `unitedhealthgroup.com` CDX row (held index, page body not retrieved) | High (documents) / Medium (that a brand year may bound a stage) |
| 3 end | **2000-03-06** | Form 8-K 0000912057-00-010247 (held): Articles of Amendment filed 2000-03-01 with the **Minnesota Secretary of State**, effective 2000-03-06, "from United HealthCare Corporation to UnitedHealth Group Incorporated" | High |
| **UNKNOWN, deliberately unfilled** | IPO/first public offering date; the 1984 rename; the "UnitedHealth Group" brand-adoption date; the Minnetonka→Eden Prairie move; the MN→DE redomiciliation; the semantics of EDGAR's `19920703`; whether Charter Med was purchased, merged or abandoned | No held document dates any of these | stays **UNKNOWN** |

STATUS: WRITTEN 2026-09-25
## Conflicts

1. **When did it become "UnitedHealth Group"?** — unchanged and still live: 8-K 2000-03-08 says effective
   2000-03-06; EDGAR metadata says former name UNITED HEALTHCARE CORP from 1995-04-04 to 2000-02-14 with
   header `DATE OF NAME CHANGE: 19920703`; Wikipedia says 1998. Best reading: legal 2000-03-06, brand
   1998-99. Residual: what `19920703` records — **UNKNOWN**.
2. **NEW, supersedes an availability claim in A:** A/UH-03 and UH-09 treated the FY1994 annual report and
   the 1995 proxy-era origin sentence as unreachable ("the earliest company-authored annual document … is
   on disk nowhere in this cache"). It is now held. A's *counts* of Tier-1 origin attestations (UH-08…10,
   12, 14, 15) are therefore all **re-datable to 1995-03-28 / 1995-03-31**. This is a supersession of
   record-availability, not of the 1977 fact.
3. **NEW:** A/UH-40's "no `Healthplan` anywhere in the local corpus" vs held FY1994 10-K405 lines 270-341
   showing `Physicians HealthPlan of North Carolina`, `United Health Plans New England`, `Share Health
   Plan of Illinois`, plus the Medica footnote. Resolution: A's statement was true of the 55 files then on
   disk and is false of the corpus now; the exact string `United Healthplan` remains untested.
4. **NEW:** the brief's "HQ is Eden Prairie, founded 1977" vs held bytes placing executive offices in
   **Minnetonka** in both the earliest company filing (1995-02-02, line 128) and the earliest annual
   report (1995-03-28, line 168). Eden Prairie is attested only as the **current** address. Adjudication:
   Eden Prairie may not be used for any pre-move year; move date UNKNOWN.
5. **NEW:** the 1978 quotation ("Certainly lenders will look more favorably on HMOs managed by us…") is
   **unattributed in the bytes I hold**. The Star Tribune's 2022 narrative would make Burke the likely
   speaker, but no held line names him. Attribution = **UNKNOWN**; do not put Burke's name in quotation
   marks around this sentence.
6. **1978 vs 1981 duplicate text** (`Focus on HMOs` / `HMO Focus`) — same passage, so counted as **one
   lineage** under §3; the second must not be tallied as corroboration.
7. **Charter Med (Minneapolis, HMO manager) ≠ Charter Medical Corporation (Minneapolis, 1990 psychiatric /
   acute-care operator)** — a live identity-conflict risk on every future "Charter" query in this file's
   window. Also: `EDGAR_cs2_UNITED+HEALTHCARE.xml` still says `state-of-incorporation DE` while every
   1996-2000 header says MN (A/UH-43), unresolved.
8. **Index-row delta 4330 vs 4,315** — reported as a tooling conflict (RD-112 class), so that no later
   agent treats 15 silently-dropped rows as an absence.

STATUS: WRITTEN 2026-09-25
## Nulls

* **Documented nulls (endpoint answered, empty result, bytes held):** no S-1/S-1/A in 4,315 indexed rows;
  corporate print `numFound:0` ×2 (HTTP 200, verified TLS, query echoed); EDGAR `formerNames` carries no
  pre-1995 name; `IA advancedsearch` `numFound:0` for `"charter med" AND mediatype:texts` and for
  `title:("focus on health maintenance organizations")`; `sec_intake` `_UNANSWERED.csv` header-only
  (0 unanswered rows in 1977-1995); Google Books `Metropolitan Health Plans` query produced only
  non-entity titles (no support for the naming-dispute story on that endpoint).
* **Null-by-date, not null-by-existence:** 1977-12-31→1995-01-31 holds **zero** electronic SEC rows for
  this CIK; the paper record behind it (initial registration, 1980s proxies, annual reports 1977-93) is
  **NOT SEARCHED**, and file number 001-10864 proves a pre-1995 §12(b) registration exists somewhere.
* **FALSE-null warnings carried and extended:** IA `text:` matches **annotations**, so every IA zero above
  is a metadata null and not a coverage null; a Google Books **snippet** is a search-index rendering, so
  the 1978 item is `TIER1_CANDIDATE` — the page itself is not held; `uhg.com` is untested despite a
  filename claiming it.
* **UNANSWERED (never reported as absence):** Chronicling America ×5 (403), HathiTrust ×2 (403),
  `fts_ipo1984.json` (HTTP 500 in A, not re-run), 15 index rows unaccounted.
* **UNTRIED:** family (e) entirely; corporate print 1996-2000; periodicals 1996-2000; IA download-and-
  grep; Minnesota Secretary of State; the paper FY1994 Annual Report to Shareholders.

STATUS: WRITTEN 2026-09-25
## Untried

Each line is settleable by the exact command shown; none may be written as an absence until it runs.

1. **Periodical full text on IA (the only real coverage test of family c on that host).**
   `python tools/ia_text.py mine --q 'title:("modern healthcare") AND mediatype:texts AND year:[1977 TO 1990]' --pattern 'Charter Med|United HealthCare|Physicians Health Plan' --company-dir founders_playbook/01_companies/company_003_unitedhealth --rows 8 --max-mb 12`
   — and the same against any serial whose title is first located by `ia_text.py search`.
2. **Hold the 1978 page itself (converts `TIER1_CANDIDATE` → held Tier-1 text, the single highest-value
   follow-up).** `FETCH REQUEST:` Google Books volume `udRwLIq-iMoC` (Focus on Health Maintenance
   Organizations, US Office of Health Maintenance Organizations, 1978), page `RA7`, and
   `ztWc6Ufs6qEC` page `PA5` (undated DHHS/PHS) — requires a full-view page route plus a
   HathiTrust/IA instance hunt; orchestrator decision, and the reason a nightly runner with clean egress
   is worth funding.
3. **Chronicling America and HathiTrust, awaiting runner egress.**
   `python tools/periodical_harvest.py --company unitedhealth --source-family chronicling_america --source-family hathitrust --out founders_playbook/01_companies/company_003_unitedhealth/sources/periodicals/HARVEST_CA_HT`
   in the GitHub Actions nightly (403 from this machine's IP; bodies of the challenges are held).
4. **Corporate print, re-run with the names actually used by the company and the missing window.**
   `python tools/periodical_harvest.py --company unitedhealth --source-family corporate_print --out founders_playbook/01_companies/company_003_unitedhealth/sources/periodicals/HARVEST_A2b`
   after editing the block's `company_terms` to add `"united healthcare corporation"`, `"united health plans"`, `"physicians health plan"` and extending `year_range` to `[1971, 2000]` — the `creator:` trap that flipped Walmart and Target is name-token sensitivity, and this company's name tokens changed twice.
5. **The exact-string test left open in Conflicts 3.** Local, zero network:
   `grep -c "United Healthplan" founders_playbook/01_companies/company_003_unitedhealth/sources/sec/*.txt`
6. **`uhg.com` CDX (misnamed file, never actually probed).**
   `http://web.archive.org/cdx/search/cdx?url=uhg.com&matchType=prefix&output=text&fl=timestamp,original,statuscode,length&limit=200`
   — run through the scripted CDX route, saved with a sidecar into `sources/`.
7. **Family (e) auction / museum documentary — needs a query block before a run** (§15.1: no agent
   improvises an unverified endpoint). Action: add an `auction_documentary` task family for `unitedhealth`
   to `tools/queries.json` covering 1977-1990 certificates, PHPMN/Hennepin contract documents and Warburg
   Pincus-era ephemera; then `python tools/periodical_harvest.py --company unitedhealth --source-family auction_documentary --out <dir>`.
8. **Minnesota Secretary of State entity file** — the registry named by the company's own 8-K. It is the
   single route that can date the 1984 rename, confirm January 1977 to a day, and say whether "Charter
   Med" (1974/1978) was ever incorporated in Minnesota or consolidated into the 1977 corporation. No
   scripted route exists; **web budget required, so it is handed back, not declined silently.**
9. **Burke's own Section 16 paper trail at CIK 0000905023** (metadata held in
   `sources/periodicals/burke.json`, insider CIK confirmed by A/UH-31): `python tools/sec_intake.py
   resolve --cik 905023` then `index` / `auto` over 1984-1995 — the only route to the claimed 1987-88
   Warburg Pincus stock sale.
10. **Re-open the held 1998 S-4 line for FY1993** to make the financial floor session-verified rather than
    inherited: `grep -n "3,115" sources/S4_0001047469-98-022543_filed-1998-06-02.txt`.

STATUS: WRITTEN 2026-09-25
