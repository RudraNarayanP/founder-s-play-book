# A_chronology_feasibility.md

> **CANONICAL VERDICT NOTICE (dated 2026-10-06, per RD-112 convention + RD-124 r10).** The `## Verdict`
> section below is the **2026-09-25** probe volume, left intact and superseded in part. The live verdict for
> this company is **`# RE-GRADE 2026-10-06`** near the end of this file: **Stage 1 = T2 core** (was T3),
> Stage 2 = T2 core, family (a) TRIED–ANSWERED with 676,058 B of filing bytes now on disk, and the entity's
> founding date settled by the registrant's own charter at **1978-06-29, Delaware, as `M. B. Associates
> Incorporated`**. A cold reader who stops at the first `## Verdict` will report **T3** — which is what the
> gate's own tier reader did on 2026-10-06 and printed as a disagreement. Read the re-grade.


<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:41:07Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

**Tier: T3 (register tier) as measured, and T3 measured on a deliberately under-mined single family —
recommend dispatching at T3 with two funded gates, and expect T2.** Families returning in-window Tier-1
text (§15.2): **one — family c (periodicals).** (a) EDGAR: floor **1994-04-19** proven, and the window
1978-01-01→1992-12-31 returns **0 of 3,077** rows with **no unanswered slices**, so the electronic record
is a genuine null for the founding era, not a blocked route; but no filing *bytes* were reached at all, so
family a supplies a boundary and no text. (b) web: floor **1996-11-05**, null by construction. (d) corporate
print: **searched and empty** — 0 hits for Home Depot in IA's `annualreports` collection, 0 in its EDGAR
collection, no bound report, no prospectus; the one 1999 reported book is **HTTP 401 gated**; the founders'
own books did not surface. (e) documentary: one **Tier-2** dated third-party statement, an **unread** company
PDF, an auction route that surfaced nothing, and untried registrars. **Implied agent budget per §15.2: 3–4
runs** (8k words/stage), registers + narrative bound to held bytes.

**The archival-floor question this probe was dispatched to answer, answered plainly:** for a 1978-founded,
1987-listed retailer the *pre-EDGAR floor is not the binding constraint*. Home Depot's founding period is not
paper-only and it is not unrecoverable — it sits in **weekly trade print that is already digitised, already
free, and already on this machine's disk**, and it says things no filing could: that the company was a
**four-unit Atlanta chain by 1979**, that the trade called its founder **"former discounter Bernie Marcus"**
in **March 1980**, that its real-estate mechanism was **taking ~55,000 sq ft in the collapsing Treasure Island
chain**, and that by **August 1987** competitors were adjoining its stores and hiring its managers. Fourteen
claim records (HD-01…HD-14, HD-15…HD-17) were produced from **three reels out of 41 enumerated**. The tier is
low because **one family answered**, not because the archive is quiet — and §15.2's family count cannot be
inflated by depth inside a family. That is why this verdict is T3 *with named escalation*, and why the
register tier must not be read as "little to know": at T3 the deliverable should sit at the **top** of the
8k-word band, trade-print-led, and the fleet must be told the interior of 1980–1990 is reconstructable.

**Two gates, both cheap, each worth a tier step.** (G1) **Bound printed annual reports FY1988–FY1993** via
`periodical_harvest.py --source-family corporate_print` and HathiTrust: Home Depot's fiscal year ends
**31 January** (proved from the 1994 index rows), so FY1988 is the first listed-company report and its
five-year selected data would carry **audited FY1983–1987** figures — audited in-window financials from a
pre-EDGAR company. If G1 lands, families a-or-d + c ⇒ **T2 core**, and the dossier stops being
trade-print-alone. (G2) **The unread date-lists**: `THD Timeline.pdf` (raw bytes, PDF text extraction) and
the 1994 DEF 14A / FY1994 10-K bytes (the `sec_intake.py grab` route is broken for pre-1996 accessions —
404/503 on all three tries). G2 does not raise the tier by itself but converts HD-22/HD-23 from
"retrospective, unread" into a documented company lineage. **T1 (exemplar) is reachable only through the
two routes left entirely untried here** — state registrars (Colorado 1978 / Georgia 1978-79 entities) and
name-indexed auction/museum catalogues — and neither should be promised before it is attempted.

**What this company cannot support, stated as a deliverable rather than a failure:** no date inside
1978, no first-store date, no IPO date/price/proceeds, no founder pre-history dates, no founding capital
table. Every one of those is either retrospective-only or absent from held bytes, and §15.4 is satisfied by
naming them, not by filling them. **Confidence of the verdict overall: Medium** — capped because 38 of 41
enumerated reels, all of HathiTrust/Google Books, all registrars, and every filing byte remain unreached;
raised above the UHG probe's Medium only because the family that reversed Walmart's verdict was actually
queried here and its null is real rather than assumed.

STATUS: WRITTEN 2026-09-25

## Family a filings

**Status: boundary PROVEN, in-window text PROVEN ABSENT (electronic record), retrospective
attestation UNANSWERED (document route blocked).**

Registrant resolved by script: `sec_intake.py resolve --ticker HD` →
`{"ticker": "HD", "cik": 354950, "name": "HOME DEPOT, INC."}`. Index built by
`sec_intake.py index/auto`: **3,077 filings enumerated**, written to
`sources/_index/{submissions.csv, submissions.json, _INDEX.md}`. That index file is the
authoritative statement of what exists; it reports **"(none)" under "UNANSWERED slices"**, so the
floor below is index-confirmed and not a blocked probe.

EDGAR floor and the phase-in gap (this is the probe's central negative finding):

| fact | value | evidence |
|---|---|---|
| earliest filing on EDGAR | **1994-04-19, DEF 14A**, acc `0000907098-94-000015`, period 1994-01-30 | `sources/_index/submissions.csv` row 2 |
| earliest annual report | **1994-04-22, 10-K**, acc `0000354950-94-000001`, FY ended **1994-01-30** | same, row 3 |
| earliest 10-Q | 1994-06-06, acc `0000354950-94-000003` | same |
| first 10-K405 | 1995-04-20, acc `0000354950-95-000002` | same |
| first 8-A of any kind | **8-A12B 1996-09-24** — a 1996 listing event, NOT the 1987 IPO | `_INDEX.md` earliest-per-form table |
| S-1 / S-1/A / 424B1 anywhere in 3,077 rows | **none** | earliest-per-form table lists no registration statement form |
| filings dated 1978-01-01 → 1992-12-31 | **0** | `auto --from 1978-01-01 --to 1992-12-31` → "0 documents stored, 0 skipped/unanswered" |

Consequence, stated as the case requires: Home Depot's IPO (1987, per the universe line — *not yet
independently proven by this probe*) sits **seven years below the EDGAR floor**, and the founding
window 1978–1987 sits **sixteen years** below it. Every Home Depot SEC document for 1978–1993 —
including the 1987 registration statement and prospectus, the 1987–1993 10-Ks, and any Section 16
filings of Marcus, Blank and Langone — is **SEC paper**, reachable only through the Public Reference
Room / National Archives still-file route, not through EDGAR. This is the same floor shape as Walmart
(1994-02-14) and UnitedHealth (1995-02-02); Home Depot's is **1994-04-19**, and — unlike UnitedHealth
— this registrant has **no predecessor CIK and no electronic row before the floor**, so EDGAR cannot
date the founding, the 1979 first store, the IPO, or the founders' pre-history at all.

**UNANSWERED, not null:** whether the earliest *electronic* documents retrospectively narrate
1978–1987 (a "founded in 1978 / opened its first warehouse-style store in 1979" Item 1 paragraph,
or a 1994 proxy biography of Marcus/Blank — the exact device that gave UnitedHealth its only Tier-1
founding-window facts). No filing **bytes** were reached on this run:

  - `sec_intake.py grab --accession 0000354950-94-000001` → `{"file": "index-headers.txt", "status": "HTTP 404"}`
  - `sec_intake.py grab --accession 0000354950-95-000002` → `"UNANSWERED after 3 tries (HTTP 503)"`
  - `sec_intake.py grab --accession 0000907098-94-000015` → `"HTTP 404"`
  - manual `…/Archives/edgar/data/354950/000035495094000001/index.json` → **HTTP 503** (retried, verified and unverified TLS)

`sources/sec/_MANIFEST.csv` therefore holds a header row and **0 stored documents** — the directory is
empty of evidence and must not be read as "nothing exists".

> FETCH REQUEST: (orchestrator runs `sec_intake.py`, not an agent)
> 1. `grab --ticker HD --company-dir founders_playbook/01_companies/company_025_homedepot --accession 0000354950-94-000001` (FY1994 10-K — Item 1 history paragraph, Item 6 five-year selected data reaching FY1990 at best)
> 2. same, `--accession 0000354950-95-000002` (FY1995 10-K405)
> 3. same, `--accession 0000907098-94-000015` (1994 DEF 14A — founder/officer biographies "since 1978")
> 4. `facts --ticker HD --from 1990-01-01 --to 1994-12-31` (XBRL frames will be empty pre-2002; expect null)
> 5. Paper route, no script exists: 1987 S-1/424B1 and FY1987–FY1990 10-Ks at SEC Public Reference Room — Stage-1 fleet must treat these as *requested*, not assumed.

Records:

HD-01 Claim: The SEC registrant for Home Depot is EDGAR CIK 0000354950, conformed name "HOME DEPOT, INC.", ticker HD — Date: ongoing — Source: `sec_intake.py resolve --ticker HD` (EDGAR company_tickers) — Source date: 2026-09-26 (retrieval) — URL: https://www.sec.gov/files/company_tickers.json — Archived: sources/_index/submissions.json, sources/_index/_INDEX.md — Tier: 1 — Class: FACT — Passage: `"ticker": "HD", "cik": 354950, "name": "HOME DEPOT, INC."` — Conf: High — Corroboration: 1 authoritative registry — Conflicts: None.

HD-02 Claim: Home Depot's entire electronic SEC record begins **1994-04-19** with a DEF 14A (acc 0000907098-94-000015, period 1994-01-30); the earliest annual report is the 10-K filed 1994-04-22 (acc 0000354950-94-000001) for the fiscal year ended **1994-01-30** — Date: 1994-04-19 — Source: EDGAR submissions bulk slice CIK0000354950-submissions-002.json — Source date: 2026-09-26 — URL: https://data.sec.gov/submissions/CIK0000354950-submissions-002.json — Archived: sources/_index/submissions.csv — Tier: 1 — Class: FACT — Passage: `1994-04-19,DEF 14A,0000907098-94-000015,1994-01-30` / `1994-04-22,10-K,0000354950-94-000001,1994-01-30` — Conf: High — Corroboration: 2 (submissions.csv + _INDEX.md earliest-per-form table, same source slice) — Conflicts: None.

HD-03 Claim: **No Home Depot filing dated in the founding window 1978-01-01 → 1992-12-31 exists on EDGAR** — 0 of 3,077 enumerated rows, and no S-1/S-1/A/424B1 form appears at all; the slice enumeration reported no unanswered slices, so this is a proven null over the electronic record rather than a failed route — Date: null interval 1978–1992 inclusive — Source: `sec_intake.py auto --from 1978-01-01 --to 1992-12-31` + `_INDEX.md` — Source date: 2026-09-26 — URL: n/a (index) — Archived: sources/_index/_INDEX.md — Tier: 1 — Class: FACT (documented absence, electronic record only) — Passage: `auto: 0 documents stored, 0 skipped/unanswered`; `## UNANSWERED slices → (none)` — Conf: High — Corroboration: 1 index, 2 commands — Conflicts: None. **Scope limit:** this proves nothing about the paper SEC record, which is where the 1987 registration statement lives.

HD-04 Claim: The first 8-A on the registrant's EDGAR history is an **8-A12B of 1996-09-24**, i.e. a 1996 listing, not the 1987 IPO — so the electronic record carries no trace of the 1987 listing event — Date: 1996-09-24 — Source: `_INDEX.md` earliest-per-form table — Source date: 2026-09-26 — URL: n/a — Archived: sources/_index/_INDEX.md — Tier: 1 — Class: FACT — Passage: `| 8-A12B | 1996-09-24 | 0000950144-96-006549 |` — Conf: High — Corroboration: 1 — Conflicts: None. (The 1987 NYSE listing itself remains UNPROVEN here — see Boundaries.)

HD-05 Claim: Whether the FY1994/FY1995 filings retrospectively state the 1978 founding and 1979 first store — the device that produced UnitedHealth's only Tier-1 founding-window facts — is **UNANSWERED on this run**: every accession-document route returned 404 or 503 and zero filing bytes are held — Date: n/a — Source: `sec_intake.py grab` ×3 + manual index.json attempt — Source date: 2026-09-26 — URL: https://www.sec.gov/Archives/edgar/data/354950/000035495094000001/index.json — Archived: NO BYTES HELD (sources/sec/_MANIFEST.csv has header only) — Tier: n/a (route failure) — Class: UNKNOWN — Passage: `"accession": "0000354950-94-000001", "file": "index-headers.txt", "status": "HTTP 404"`; `0000354950-95-000002 → UNANSWERED after 3 tries (HTTP 503)` — Conf: High (that the probe failed), UNKNOWN (content) — Corroboration: 1 — Conflicts: None. **Tool note for the fleet:** `sec_intake.py grab` resolves the primary document through an accession-directory request that fails for pre-1996 accessions; early-EDGAR documents for this company need the `--file` form or a directory listing that survives 503.

STATUS: WRITTEN 2026-09-25

## Family b web

**Status: NULL for the founding window, and NULL-by-construction rather than NULL-by-blockade.
Contributes zero families to the tier count. Route caveats listed.**

`web.archive.org/cdx/search/cdx?url=homedepot.com&matchType=exact&from=1990&to=2000` returns its first
row at **1996-11-05T23:28:03**, `http://www.homedepot.com:80/`, HTTP 200, **1,149 bytes**. The `www.`
query returns the identical first capture, so bare-host and `www.` are **one test, not two** (the CDX
host is normalised — the same trap the Walmart probe recorded). Rows and provenance are preserved in
`sources/EXTRACT_web_documentary_20260926.md` §3.

What that fixes: the earliest archived Home Depot web artifact sits **9 years after the asserted 1987
IPO and 18 years after the asserted 1978 founding**, and it is a 1.1 KB placeholder — not a window into
the founding period. Combined with family a's floor (1994-04-19) the shape is the one §14 rule 6
predicted: the archival families (EDGAR ~1994, web ~1996) both begin **after** the period this company
is being probed for, which is exactly why the verdict here must rest on trade print, not on them.

Records:

HD-06 Claim: The earliest Wayback capture of homedepot.com (any host form) is **1996-11-05**, HTTP 200, 1,149 bytes; no capture exists in the index for 1990–1996, and therefore none can exist for 1978–1987 — Date: 1996-11-05 — Source: Wayback CDX API, exact-url queries for `homedepot.com` and `www.homedepot.com` — Source date: 2026-09-26 (retrieval) — URL: http://web.archive.org/cdx/search/cdx?url=homedepot.com&matchType=exact&from=1990&to=2000&fl=timestamp,original,statuscode,length&limit=12 — Archived: sources/EXTRACT_web_documentary_20260926.md §3 — Tier: 1 (index-confirmed negative for pre-1996) — Class: FACT — Passage: `19961105232803 http://www.homedepot.com:80/ 200 1149` — Conf: High — Corroboration: 1 (the two host forms are the same test, not independent) — Conflicts: None.

HD-07 Claim: **No first-party web artifact of any kind can evidence 1978–1987** for this company; family b is closed as a documented null for the window, and no agent should spend another call on it except to reach 1996–2000 archived self-narrative pages (which would be retrospective) — Date: n/a — Source: HD-06 — Source date: 2026-09-26 — URL: n/a — Archived: as HD-06 — Tier: 1 (documented absence over a queried index) — Class: FACT (absence) — Passage: NO_VERBATIM_PASSAGE_RECORDED (negative finding) — Conf: High — Corroboration: 1 — Conflicts: None.

HD-08 Claim: **Method warning written as a record** — family b was queried with `matchType=exact` only. **`matchType=prefix` sweeps were NOT run** (Amazon and Walmart runs both recorded HTTP 504 capacity failures on fat prefix sweeps; a 504 is UNANSWERED, never absence). Sub-paths that could hold founding-period company narrative (`/corporatehistory`, `/about`, `/news`, `/pdfs/THD Timeline.pdf` variants) are UNTRIED — the single company timeline PDF reached by this probe returned unreadable raw PDF bytes and is recorded in family e/d as FETCHED-NOT-READ — Date: n/a — Source: this probe's query log — Source date: 2026-09-26 — URL: see Untried — Archived: sources/EXTRACT_web_documentary_20260926.md §2 — Tier: n/a — Class: UNKNOWN (untried route) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High (that it is untried) — Corroboration: 0 — Conflicts: None.

STATUS: WRITTEN 2026-09-25

## Family c periodicals

**Status: THE FAMILY THAT CARRIES THIS COMPANY. Tier-1-grade in-window text is HELD, dated to the
issue, and quotable verbatim. 3 of 41 enumerated reels mined — the yield is a floor, not a measure.**

This is the family §14 rule 6 said EDGAR and web archives cannot see, and it behaved exactly as the
Walmart/Apple/Target precedents predicted. Internet Archive holds microfilm-derived OCR layers of the
three trade titles the brief named. Enumeration (catalogue rows, `sources/EXTRACT_web_documentary_20260926.md` §4):

| run | reels enumerated | years | held & grepped by this probe |
|---|---|---|---|
| Discount Store News (DSN) | 11 | **1980–1990** continuous | 1980 (1,987,023 B), 1987 (1,700,633 B) |
| Chain Store Age (Executive / Supermarkets / General Merchandise / GM Trade) | 20 | 1980–1990 | 1986 Executive (223,991 B) |
| National Home Center News | 10 | 1982–1990, 1992 | none (UNTRIED) |
| Building Supply Home Centers (= the "Building Supply Digest" line) | 1 | 1988 index volume only | none |

**Boundary the enumeration itself sets: no DSN or Chain Store Age reel is catalogued for 1978 or 1979.**
The founding two years are not in this digitised run, so the earliest reachable contemporaneous trade
print for Home Depot is **DSN 1980** — which already describes the chain as four units deep. Whether a
1979 reel exists on other shelves (HathiTrust, commercial DBs, Atlanta dailies) is UNTRIED.

Detector proof (§15.5, applied to retrieval before trusting a null): the identical
fetch→grep machinery returned **2 hits** in the DSN 1980 layer, **4 hits** in the DSN 1987 layer, and
**0 hits** in the Chain Store Age 1986 layer over 218 KB of held bytes. A zero here is a zero, not a
broken detector; but note the 1986 CSA layer is the thinnest of the three (218 KB vs 1.7–2.0 MB), so
its null is weak and is reported as such below.

### Records (HD-09 … HD-17)

Format per §7. Tier label tension stated once and then applied consistently: §5 places trade
publications at Tier 3, while §14 rule 6 grants that in-window contemporaneous periodical text *is*
the Tier-1 evidence class for the pre-1994 period. These records are written as
`1 (§14r6) / 3 (§5)` and counted toward the tier verdict on the §14 rule 6 reading, because the
alternative reading would count Walmart's own flipped corpus as nothing.

HD-09 Claim: By **1979** ("last year" in a 1980 issue) Home Depot was **a four-unit home-center chain in Atlanta** — the earliest contemporaneous description of the company recovered anywhere on this run, and it is a chain, not a single store — Date: 1980-03-10 (source issue); refers to 1979 — Source: Discount Store News, Vol. 19, 1980-03-10 issue (microfilm reel micro_IA40706901_0406) — Source date: 1980-03-10 — URL: https://archive.org/download/micro_IA40706901_0406/… (OCR layer; reel-level metadata `date: 1980`, issue pinned by running heads at layer lines 18803 and 19175) — Archived: sources/periodicals/micro_IA40706901_0406_djvu.txt (+ .meta.json sidecar), 1,987,023 B, verified TLS — Tier: 1 (§14r6) / 3 (§5) — Class: CONTEMPORARY OBSERVATION — Passage: "Last year, the Home Depot, a four-unit home center chain in Atlanta, founded by former discounter Bernie Marcus, took advantage of Treasure Island's decision to roll back the size of its stores" — Conf: High — Corroboration: 1 in-period (no independent second witness yet; the 2016 GHS statement is a different lineage, see U-1) — Conflicts: **U-1** (year/place of founding), **U-4** (two stores at opening vs four units).

HD-10 Claim: The same item names the founder as **Bernie Marcus and only Marcus**, and characterises him as a **"former discounter"** — the sole in-window attestation of founder pre-history found by this probe; it corroborates the pre-history *shape* (Marcus came from discount retailing) without naming the employer, the dates, or the firing story — Date: 1980-03-10 — Source: as HD-09 — Source date: 1980-03-10 — URL: as HD-09 — Archived: as HD-09 — Tier: 1 (§14r6) / 3 (§5) — Class: CONTEMPORARY OBSERVATION — Passage: "founded by former discounter Bernie Marcus" — Conf: High — Corroboration: 1 — Conflicts: **U-2** (one founder named in-period; two or three in every later telling). **Founder pre-history therefore stays at UNKNOWN, not deleted:** which discount chain, from when, on what terms, and what ended it are all unattested in held bytes.

HD-11 Claim: Home Depot's founding real-estate mechanism is dated in-period: it **became a tenant of the financially troubled Treasure Island chain** after that chain "roll[ed] back the size of its stores," obtaining **"approximately 55,000 sq. ft. of space at each location"** — a section-D "first experiment" fact of a kind the filings families cannot supply — Date: 1979 (event), 1980-03-10 (source) — Source: as HD-09 — Source date: 1980-03-10 — URL: as HD-09 — Archived: as HD-09 — Tier: 1 (§14r6) / 3 (§5) — Class: CONTEMPORARY OBSERVATION — Passage: "The arrangement, which gave The Home Depot approximately 55,000 sq. ft. of space at each location, has thus far been a happy one." — Conf: High — Corroboration: 1 — Conflicts: None. **Caution for the dossier:** 55,000 sq ft is the *Treasure Island rollback* footprint, NOT necessarily the size of the June 1979 stores; a later pass that writes "the first stores were 55,000 sq ft" would be importing this figure into the wrong event.

HD-12 Claim: The company was speaking to the trade by early 1980 through a **named district manager, Bill Kent** ("It's a natural relationship"), i.e. an identifiable company officer existed within ~7 months of the asserted opening date; his hire date and title history are unrecorded — Date: 1980-03-10 — Source: as HD-09 — Source date: 1980-03-10 — URL: as HD-09 — Archived: as HD-09 — Tier: 1 (§14r6) / 3 (§5) — Class: CONTEMPORARY OBSERVATION (original interview fragment in trade press) — Passage: "'It's a natural relationship,' said Bill Kent, district manager" — Conf: High (that the quote ran), UNKNOWN (Kent's tenure dates) — Corroboration: 1 — Conflicts: None.

HD-13 Claim: By **1987-08-10** the trade press treated Home Depot as a fixed point of the warehouse-format landscape: a Sports Authority opening is described as adjoining "other warehouse-type operations like Home Depot, Office Depot and Builders Square," and an executive is identified as "formerly of Atlanta-based home improvement warehouse Home Depot" — Date: 1987-08-10 — Source: Discount Store News, reel micro_IA40706924_0308, issue pinned by running heads at layer lines 53725 and 54209 — Source date: 1987-08-10 — URL: https://archive.org/download/micro_IA40706924_0308/… — Archived: sources/periodicals/micro_IA40706924_0308_djvu.txt (+ sidecar), 1,700,633 B — **transport UNVERIFIED TLS (`--insecure` used: the verified route died with `SSL: CERTIFICATE_VERIFY_FAILED … certificate has expired`)** — confidence capped at Medium on this layer per tool policy — Tier: 1 (§14r6) / 3 (§5) — Class: CONTEMPORARY OBSERVATION — Passage: "other warehouse-type opera- tions like Home Depot, Office Depot and Builders Square" (OCR line-wrap preserved as held) — Conf: Medium — Corroboration: 1 — Conflicts: None.

HD-14 Claim: In the same issue Home Depot is named as a **manager-supply source for rival formats** — "present store managers have come from Price Club, Home Depot and HomeClub" — first-party-shaped evidence of the training/organisation diffusion that the later "culture" literature asserts — Date: 1987-08-10 — Source: as HD-13 — Source date: 1987-08-10 — URL: as HD-13 — Archived: as HD-13 — Tier: 1 (§14r6) / 3 (§5) — Class: CONTEMPORARY OBSERVATION — Passage: "Club, Home Depot and Home-" … "agers have come from Price" (OCR broken lines, held bytes) — Conf: Medium — Corroboration: 1 — Conflicts: None.

HD-15 Claim: The same 1987 issue carries a competitor's **market-sizing recollection about Atlanta** — "When we were about to open our first [home center] stores in Atlanta, we added up the total home center business in the market and asked how much of this will we have to take over to make a profit… we quickly realized that we couldn't make it even" — spoken by a Sports Authority principal about *his own* earlier venture, not about Home Depot's founding, and tagged **RETROSPECTIVE SOURCE** inside an in-period document — Date: 1987-08-10 (source); recollection of an unstated earlier year — Source: as HD-13 — Source date: 1987-08-10 — URL: as HD-13 — Archived: as HD-13 — Tier: 1 (§14r6) / 3 (§5) — Class: RETROSPECTIVE INTERPRETATION (speaker's own memory, 1987) — Passage: "we added up the total home center business in the market and asked how much of this will we have to take over to make a profit" — Conf: Medium — Corroboration: 1 — Conflicts: None. **Do not** let a later pass attach this sentence to Marcus/Blank: the held text does not say it was Home Depot's founders who said it.

HD-16 Claim: **NULL, honestly bounded —** Chain Store Age Executive 1986 (223,991 B held) contains **zero** occurrences of "Home Depot"; and in the DSN 1987 reel the founders' surnames return only false positives (`Marcus` → "Nieman Marcus" once; `Blank` → "blank videotape"/"blanketing"; `Langone` → 0). So: trade print **names the chain long before it names the founders** — a method finding, since a founder-name search across these reels will mislead — Date: 1986 (CSA), 1987 (DSN) — Source: `ia_text.py grep` over held layers — Source date: 2026-09-26 — URL: n/a — Archived: sources/periodicals/micro_IA40706921_0149_djvu.txt, micro_IA40706924_0308_djvu.txt — Tier: 1 (documented absence in held bytes) — Class: FACT (absence) — Passage: `NULL -- 218 KB of OCR held, zero hits` — Conf: Medium (the 1986 layer is 8× thinner than the DSN layers; one reel-year is not a coverage verdict on a 20-reel run) — Corroboration: 1 — Conflicts: None.

HD-17 Claim: **The 1987 IPO is not mentioned in the held 1986–1987 DSN bytes**: "Home Depot" occurs 4 times, none of them about an offering; the reel's `going public` hits belong to other chains (Schuck's "considering going public—perhaps as early as next year"; Western Auto "went public as an independent concern"; Fred Meyer's share-count note "shares issued in going public"), and a year-in-review passage records "Wall Street's fascination with both types of discounters saw a handful of privately held chains turn to the stock market to fuel their expansion" — this is the **in-period IPO context** for Home Depot's 1987 listing, but not evidence of the listing itself, whose date, price and proceeds remain UNDOCUMENTED on this run — Date: 1987-08-10 (and 1986-11-10 issue heads within the same reel) — Source: `ia_text.py grep` patterns `initial public offering`, `going public`, `public offering`, `shares of stock` over held bytes — Source date: 2026-09-26 — URL: as HD-13 — Archived: as HD-13 (+ EXTRACT §6) — Tier: 1 (§14r6) / 3 (§5) — Class: CONTEMPORARY OBSERVATION (context) + UNKNOWN (HD's own IPO) — Passage: "Wall Street's fascination with both types of discounters saw a handful of privately held chains turn to the stock market to fuel their expansion" — Conf: Medium — Corroboration: 1 — Conflicts: **U-3**. Note the reel spans at least 1986-11-10 → 1987-10-12 by its own filenames, so it *covers* the asserted September 1987 IPO window and still does not tie Home Depot to an offering in the passages grepped; the whole reel (72,064 lines) was not read.

STATUS: WRITTEN 2026-09-25

## Family d corporate print

**Status: SEARCHED — and it came back empty for Home Depot, which is a real finding rather than the
Walmart case. One genuine in-window-bearing route is left UNANSWERED (a 401) and one is UNTRIED
(HathiTrust). This family does NOT currently contribute Tier-1 text, and the whole T3→T2 step hangs on it.**

Per §14 rule 6 and the Walmart/Target reversals, no "paper-only" sentence appears in this file until a
book and bound-corporate-print corpus had actually been queried. It was, six ways, against the Internet
Archive metadata index (queries verbatim in the run log; catalogues, not content):

| query | numFound | relevant to HD corporate print |
|---|---|---|
| `collection:(annualreports) AND ("Home Depot")` | **0** | none |
| `title:("Home Depot") AND ("annual report")` | 2 | both are **accounting textbooks** that use HD's FY2003 / FY2007 report as a teaching exhibit (`isbn_9780071117524`, `collegeaccountin0000john_c7e8`) — out of window, but they prove HD's printed reports circulated as documents |
| `(Home Depot) AND (collection:edgar)` | **0** | IA holds no EDGAR-sourced HD filings |
| `title:("Home Depot") AND year:[1987 TO 1996]` | 2 | a 1995 hobby magazine and a 1995 TV ad asset — no report |
| `"Home Depot, Inc."` (all fields) | 385 | mostly modern court records (`gov.uscourts.…` v. The Home Depot) and textbooks; no 1980s print |
| `title:("Home Depot") AND (history)` | 7 | one useful: **`insidehomedepoth0000rous` — Chris Roush, *Inside Home Depot: how one company revolutionized an industry*, McGraw-Hill, 1999** |

The founders' own retail histories — the class the brief said to query explicitly — were queried and did
**not** surface in IA's public index: `creator:("Marcus, Bernie")` → numFound 1 (`isbn_9784478360484`, a
foreign-language imprint, fields mangled in output, **not inspected**); `title:("Home Transformation")` →
7 irrelevant hits; `title:("Beyond the Build")` → 2 irrelevant (a 2015 Aspen Institute cyber report and a
3D-print file); `"Handy Dan"` (the asserted founder pre-history employer) → 2 irrelevant (Thingiverse).
Google Books' keyless v1 route is known dead from the UnitedHealth run (`HTTP 429 … quota_limit_value: 0`)
and was **not** re-attempted; the legacy Atom feed and HathiTrust were **not** attempted at all.

Records:

HD-18 Claim: **Home Depot has no bound corporate print (annual report, shareholder report, prospectus, 10-K) in Internet Archive's public collections** — 0 hits in the `annualreports` collection and 0 in the EDGAR-sourced collection over a searched index — so the family that flipped Walmart's verdict to exemplar **does not exist for this company at this endpoint** — Date: n/a — Source: `advancedsearch.php` queries as tabled above — Source date: 2026-09-26 — URL: https://archive.org/advancedsearch.php?q=collection:(annualreports)+AND+("Home+Depot") — Archived: sources/EXTRACT_web_documentary_20260926.md §4 (enumeration method) — Tier: 1 (documented absence over a queried index) — Class: FACT (absence, endpoint-bounded) — Passage: NO_VERBATIM_PASSAGE_RECORDED (negative finding; `numFound: 0`) — Conf: Medium-High — Corroboration: 4 independent query shapes, 1 endpoint — Conflicts: None. **Endpoint limit:** HathiTrust, Google Books, and physical bound runs (Georgia Tech, Fulton County Public Library, SEC Reference Room) were NOT queried.

HD-19 Claim: The one **structurally decisive** corporate-print target this probe could name is the **first printed annual reports of the public company** — Home Depot's fiscal year ends **January 31**, so FY1988 (ended 1988-01-31) is the first report of the listed entity, and its five-year selected-data table would carry **audited FY1983–1987** figures, i.e. audited in-window financials of a pre-EDGAR company. None of this is held: it is an **argument about where evidence must be, not evidence** — Date: n/a — Source: fiscal-year convention read from EDGAR (`10-K … 1994-04-22, period 1994-01-30`; `10-Q` periods 1994-05-01, 1994-07-31, 1994-10-29 in `sources/_index/submissions.csv`) — Source date: 2026-09-26 — URL: n/a — Archived: sources/_index/submissions.csv — Tier: 1 (for the fiscal-calendar inference only) — Class: INFERENCE — Passage: `1994-04-22,10-K,0000354950-94-000001,1994-01-30` — Conf: Medium — Corroboration: 1 index + the Jan-31 pattern across 4 rows — Conflicts: None. **Action:** this is the single highest-yield FETCH REQUEST the fleet can issue (FY1988–FY1993 reports via `periodical_harvest.py` `corporate_print` family and HathiTrust).

HD-20 Claim: The best in-window-adjacent **reported book** on the company exists on IA as a catalogue record but its text layer is **lending-gated**: `insidehomedepoth0000rous` (Roush 1999, McGraw-Hill) → text-layer fetch returned **HTTP 401 twice**, 0 bytes held — UNANSWERED, not a null; a 1999 reported book would carry interviewed 1978–1987 recollections and possibly quoted prospectus figures — Date: n/a — Source: `ia_text.py fetch --id insidehomedepoth0000rous` — Source date: 2026-09-26 — URL: https://archive.org/metadata/insidehomedepoth0000rous — Archived: NO BYTES (sources/periodicals/ holds no file for this id) — Tier: 2 (would be Tier 2 as evidence, reported book) — Class: UNKNOWN — Passage: `"status": "UNANSWERED -- no text layer resolved (… HTTP 401)"` — Conf: High (that the route failed) — Corroboration: 0 — Conflicts: None.

HD-21 Claim: Accounting textbooks on IA reproduce **Home Depot's FY2003 and FY2007 annual reports** as teaching exhibits, which shows printed HD reports are embedded in secondary print and reachable — but both are **16+ years past the window** and cannot be used as founding-period evidence; recorded as a lead only — Date: 2005 / 2009 (imprints) — Source: IA search rows `isbn_9780071117524`, `collegeaccountin0000john_c7e8` — Source date: 2026-09-26 — URL: https://archive.org/details/isbn_9780071117524 — Archived: none (enumeration only) — Tier: 3 — Class: UNKNOWN (out of window; lead only) — Passage: "Financial Accounting with '03 Home Depot Annual Report" — Conf: High (that the records exist) — Corroboration: 1 — Conflicts: None.

STATUS: WRITTEN 2026-09-25

## Family e documentary

**Status: THIN AND MOSTLY UNTRIED. One dated third-party statement (Tier 2, 2016) recovered; the
auction route searched to nothing; the two routes that could actually produce Tier-1 founding documents
— state registrars and the physical marker's sponsor — were not attempted. No document in this family
is in-window.**

Records:

HD-22 Claim: The **Georgia Historical Society** states (2016-07-20) that "Bernie Marcus and Arthur Blank founded The Home Depot in 1978" and that the founders "opened the first two Home Depot stores on June 22, 1979, in Atlanta, Georgia" — the only third-party statement recovered that carries a founding year, an opening date, a store count and both founders' names together; it is 37 years retrospective and therefore **cannot fix the date, only corroborate a lineage** — Date: source 2016-07-20, about 1978 and 1979-06-22 — Source: georgiahistory.com, "A State of Innovation: Home Depot" — Source date: 2016-07-20 — URL: https://www.georgiahistory.com/a-state-of-innovation-home-depot/ — Archived: sources/EXTRACT_web_documentary_20260926.md §1 (verbatim + retrieval stamp; raw page bytes not retained) — Tier: 2 — Class: RETROSPECTIVE INTERPRETATION — Passage: "opened the first two Home Depot stores on June 22, 1979, in Atlanta, Georgia" — Conf: Medium — Corroboration: **1 independent lineage** (a historical society is not in the company's own citation chain) — Conflicts: **U-1** (its 1978/1979 pair vs DSN 1980's single-year "last year … four-unit chain in Atlanta"), and the 22 June date is unverified against any 1979 witness.

HD-23 Claim: The company's own canonical date list — **`THD Timeline.pdf` on corporate.homedepot.com** — was reached and **could not be read**: the fetch returned raw PDF source with metadata date `D:20200220124640-05'00` and no extractable text. So the artifact that most retail dossiers in this dataset were built on (the Walmart probe's spine was exactly such a page) is present for Home Depot and **UNREAD**, and its contents must not be assumed to match either HD-22 or the 1980 trade print — Date: file dated 2020-02-20 by its own metadata, about 1978–2020 — Source: corporate.homedepot.com PDF — Source date: retrieved 2026-09-26 — URL: https://corporate.homedepot.com/sites/default/files/THD%20Timeline.pdf — Archived: sources/EXTRACT_web_documentary_20260926.md §2 (failure recorded; **no bytes retained**) — Tier: 1 artifact / retrospective company self-narrative — Class: UNKNOWN (contents) — Passage: `Input is raw PDF code. No Home Depot timeline visible. Metadata date: "D:20200220124640-05'00"` — Conf: High (that it is unread) — Corroboration: 0 — Conflicts: None yet. > **FETCH REQUEST:** pull this PDF to `sources/corporate_print/` with a sidecar and run a PDF text extraction; it is the cheapest unresolved date-list in the probe.

HD-24 Claim: The **auction / documentary sale-record family produced nothing for Home Depot**: two targeted searches for founding-era documents (incorporation papers, first-store records, founder correspondence) coming up for sale returned company pages, a historical-marker release, an AJC anniversary piece and Tier-4 social/scribd retellings — **no sale record, no accession list, no lot** — Date: n/a — Source: WebSearch ×2 (2026-09-26), queries preserved in the run log — Source date: 2026-09-26 — URL: n/a — Archived: sources/EXTRACT_web_documentary_20260926.md — Tier: n/a — Class: FACT (documented absence over these endpoints only) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Low-Medium — Corroboration: 1 endpoint class (a general web index) — Conflicts: None. **Why this null is weaker than it looks:** the Apple probe's founding documents surfaced via *name-indexed auction houses and museum catalogues*, none of which was queried here (see Untried). Home Depot's 1978–1979 paperwork is also corporate rather than founder-domestic, so the auction-route prior is genuinely lower — but that is an argument, not a search.

HD-25 Claim: The founders' **own first-person accounts exist as retrievable public artifacts** — the company published (2018-01-02) a page on Arthur Blank's NPR *How I Built This* appearance, and Ken Langone's telling circulates in a 2026 business-news retelling — which under §5 ("original interviews and transcripts") are **Tier-1 artifacts carrying FOUNDER CLAIM content about 1978–1979**. None was opened on this run, so the canonical pre-history sequence (both founders leaving Handy Dan, the decision to start a warehouse-format home-improvement chain, Ken Langone's and Pat Farah's capital roles) is **UNTESTED here and must be kept at UNKNOWN rather than deleted** — Date: 2018 / 2026 (sources), about 1978 — Source: corporate.homedepot.com news page; biggo.com retelling — Source date: 2018-01-02; 2026-09-13 — URL: https://corporate.homedepot.com/news/history/arthur-blank-featured-nprs-how-i-built-podcast ; https://finance.biggo.com/news/20f131ccf11d5253 — Archived: not retained (surfaced by search, titles only) — Tier: 1 (transcript, if opened) / 4 (the retelling) — Class: FOUNDER CLAIM (retrospective) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: Low — Corroboration: 0 independent — Conflicts: U-2. **Note the asymmetry that matters for the dossier:** in-window trade print names **one** founder (HD-10); every retrospective source names two or three. Which founders, in what roles, with what money, is the founding-window question the corpus can actually answer only from interviews — all retrospective, so all §6-tagged.

Status of the registry sub-route (part of this family, **UNTRIED**): the 1978 **Colorado** Secretary of State record (if the asserted Denver incorporation is real) and the **Georgia** Secretary of State charter, plus **Fulton County** deed/lease records for the June 1979 sites and the Treasure Island properties (HD-11). These are the only class of record that can date the entity independently of both the company and the trade press, and nothing on this run has asked them.

STATUS: WRITTEN 2026-09-25

## Boundaries

Company row verified against the local corpus before use (§14 r8): `00_universe/fortune_top_50_2026.csv`
line 26 — `25, Home Depot, 164683, fiscal year ended 2026-02-01, 14156, Atlanta, Georgia, Specialty
Retailers: Other … SEC EDGAR 10-K XBRL: exact match on revenue and profit`. Rank, revenue and the
**fiscal-calendar shape** are therefore Tier-1 corroborated; the brief's "founded 1978" and "IPO 1987"
are **not** in that CSV and are **not** proved by this probe.

Refinement to HD-19 before anyone reuses it: the 10-K/10-Q `reportDate` values in the index are
**1994-01-30, 1995-01-29, 1994-05-01, 1994-07-31, 1994-10-29** — i.e. the year-end is the **Sunday nearest
31 January**, not 31 January itself. The first listed-company annual report should therefore cover the year
ended **1988-01-31** (a Sunday) — to be confirmed against the report, not asserted from convention.

| Stage | Start | End | Boundary the corpus can defend — **the document named for each date** | Confidence |
|---|---|---|---|---|
| **1 — formation and the warehouse format proved out** | **1978 (labelled, unproved)** — earliest *witness* is HD-22 (Georgia Historical Society, 2016) saying "founded … in 1978"; the earliest **in-window document naming the company** is **Discount Store News, 1980-03-10** (HD-09), which already describes a **four-unit Atlanta chain** | **1987-08-10** as the last in-window trade witness *held* (HD-13/14/15/17), or **1988-01-31** (FY-end) if the FY1988 printed report is reached via gate G1 | Start is **archive-arbitrary, not company-arbitrary**: nothing on this run dates an event inside 1978 — no filing (floor 1994-04-19, HD-02/03), no web artifact (floor 1996-11-05, HD-06), no reel before 1980 (family c enumeration). End at 1987-08-10 is *also* archive-arbitrary and must be flagged as such; the boundary the record **should** create is the IPO, and the IPO is unattested here (U-3). Recommend Stage 1 end at **FY1988 (year ended 1988-01-31)** only if G1 lands, because that is when audited in-window numbers first exist. | Start: **Low** (retrospective-only) · first dated witness: **High** · End: **Low–Medium** |
| **2 — public company, provincial to national** | **1987 (asserted) → provable floor 1994-04-19**. The honest opening of Stage 2 is the **EDGAR floor**, not the IPO, until the 1987 S-1/424B1 is reached | FY1994 boundary (year ended **1994-01-30**, the first 10-K on EDGAR, HD-03) | Documents: DSN reels 1987–1990 and Chain Store Age 1987–1990 (18 unmined reels, enumerated in EXTRACT §4) carry the 1987–1993 interior; EDGAR carries nothing before 1994-04-19 (**HD-02**), and the first XBRL-free 10-K (acc 0000354950-94-000001, period 1994-01-30) is the first hard filing — but its bytes are unreached (**HD-05**). | Medium at the EDGAR end; **Low** at the 1987 end |
| **3 — the EDGAR era** | **1994-04-19** (DEF 14A, acc 0000907098-94-000015) — the only stage boundary in this company's whole history that a machine can enumerate rather than infer | out of this probe's scope | The phase-in date is a documentary discontinuity: from here every claim can be keyed to an accession. | **High** |

**Fit against spec §6 (origin → first real-world experiment → repeatable validation → scalable formation).**
Retail is the §7-adapted frame: the unit of the experiment is a **store and its real-estate deal**, not a
prototype. Unusually for a pre-1994 company here, **§6 is answerable in its middle**, not just its ends: the
*first experiment* has a dated trade-print mechanism (**HD-11**: ~55,000 sq ft taken at each Treasure Island
location, 1979, reported 1980-03-10) and *repeatable validation* has one too (**HD-09**: four units operating
by 1979, i.e. the format survived its second site). **Origin** (1978, Denver-vs-Atlanta, who put in what) and
**scalable formation** (the 1984–1987 store-count and sales ramp, the IPO) are **not** answerable on held
bytes — the former needs registrars/interviews, the latter needs either the mined 1981–1986 DSN/CSA reels or
the FY1988 printed report. So Stage 1 as dispatched must be **boundary-weak at the start, mechanism-strong
in 1979–1980, and silent on 1981–1986** unless a reel-mining run is funded; a §6-shaped narrative that
quietly fills 1981–1986 from company lore would be the failure mode to avoid.

**Founder pre-history is kept, at UNKNOWN.** The only in-window fragment is four words — "**former
discounter**" (HD-10) — which supports "Marcus came from discount retailing" and nothing else. The
Handy Dan employment, the same-day-firing sequence, the "within an hour" decision, Ken Langone's and
Pat Farah's roles, and the **Denver 1978 incorporation** are all retrospective-or-absent on this run and
must be carried into Stage 1 as a labelled preamble with `Class: FOUNDER CLAIM (retrospective)` or
`UNKNOWN`, never deleted and never promoted to fact. Note in passing that a 1987-08-10 DSN passage has a
retailer principal describing how *his* first Atlanta home-centre stores were sized (HD-15): the surname
Farah appears in the founding lore and the same surname appears in in-period print — the held text gives
**no** link between them, and any future pass that makes one is inventing it.

STATUS: WRITTEN 2026-09-25

## Conflicts

Register entries for §U of the dossier. Every one of these is a **live** conflict created by this probe,
not a inherited one; none is resolved here.

U-1 **When and where was it founded, and is "1978" even the founding of the trading company?**
(a) This brief's own line: "founded 1978" — provenance unverified by this probe. (b) Georgia Historical
Society, 2016-07-20 (HD-22): "founded The Home Depot in **1978**" and "opened the first two Home Depot
stores on **June 22, 1979**, in Atlanta, Georgia". (c) Discount Store News, **1980-03-10** (HD-09), the only
*in-window* witness: describes "**a four-unit home center chain in Atlanta, founded by former discounter
Bernie Marcus**" and dates its Treasure Island tenancy to "**last year**" (= 1979). / **WHY THEY DIFFER:**
"1978" is almost certainly an **entity/formation** year and 1979 the **trading** year, but no held document
says so; (b) is a 2016 retrospective and (c) never mentions 1978 at all. A 37-year-later third party and a
contemporaneous trade weekly are **different lineages** (the historical society does not cite DSN, and DSN
predates it), so this is a genuine independence pair — rare at this depth. / **EVIDENCE WEIGHT:** (c) Tier-1
per §14 r6 but silent on founding; (b) Tier-2, dated, specific, retrospective; (a) unsourced input. /
**BEST-SUPPORTED READING:** *trading began in 1979 on a four-unit footing by that year's end, in Atlanta;
the 1978 date is an incorporation event that no document on this run ties to a state or a day.* /
**RESIDUAL:** the exact opening date, the number of stores at opening (2 vs 4, see U-4), and the 1978 entity
all UNKNOWN; the Denver-vs-Atlanta question is not even raised by the held bytes (it lives in family e's
**untried** registrars). / **CONFIDENCE:** High for 1979 four units; **Low** for 1978; UNKNOWN for a day.

U-2 **How many founders does the record name?** (a) DSN 1980-03-10: **"founded by former discounter Bernie
Marcus"** — one founder, no co-founder, no investor. (b) GHS 2016: **"Bernie Marcus and Arthur Blank"**. (c)
Later retellings add **Ken Langone** (and, in some, Pat Farah) — surfaced by search in 2018 and 2026 items,
none opened (HD-25). / **WHY THEY DIFFER:** the contemporaneous item names the man the trade knew as the
operator; the commemorative record names the pair, then the money. Nothing here proves an error in either —
but a dossier that writes "co-founders Marcus and Blank founded the chain in 1979" would be attributing to
1979–80 a formulation that first appears in held bytes in **2016**. / **EVIDENCE WEIGHT:** (a) in-period,
Tier-1-per-§14r6; (b) Tier-2 retrospective; (c) Tier-4/1-artifact-pending. / **BEST-SUPPORTED:** the company
was **identified with Marcus** in its own trade press by March 1980; Blank's and Langone's roles are
**unattested in-window** on this run and belong to the retrospective layer. / **RESIDUAL:** who founded what,
when each joined, and who supplied the capital — UNKNOWN. / **CONFIDENCE:** High on what each source says;
**Low** on any merged list.

U-3 **The 1987 IPO — asserted by the brief, absent from every held byte.** (a) Input line: "IPO 1987".
(b) EDGAR: no registration statement, no 424B, no 8-A before 1996; floor 1994-04-19 (HD-02, HD-04). (c) DSN
reel covering 1986-11-10 → 1987-10-12 names Home Depot **4 times, never in connection with an offering**,
while the same reel discusses other chains going public (HD-17). / **WHY THEY DIFFER:** (c) is *not* evidence
against the IPO — one weekly cannot be assumed to have covered it, and the reel was grepped not read. But the
probe must report the asymmetry honestly: **the single load-bearing date that would end Stage 1 has no witness
of any kind on this run**, in-period or retrospective. / **BEST-SUPPORTED:** UNKNOWN. / **RESIDUAL:** IPO date,
exchange, share price, share count, proceeds, and the founders' post-IPO stakes. / **CONFIDENCE:** the
assertion is **not** usable in Stage 1 as a fact; if a dossier needs the boundary it must cite a reached document.

U-4 **Two stores or four at the end of 1979?** DSN 1980 (HD-09): "a four-unit home center chain … Last year".
GHS 2016 (HD-22): "opened the first two Home Depot stores on June 22, 1979". / **WHY THEY DIFFER:** trivially
reconcilable (two in June, four by December) — but **the reconciliation is this probe's inference, not either
source's statement**, and it is exactly the kind of smooth merge that becomes a false chronology downstream. /
**BEST-SUPPORTED:** ≥4 units operating by early 1980; the June-1979 opening is unverified in-window. /
**CONFIDENCE:** Medium on four-by-1980; Low on the June pair; the *interval* (which units opened when) UNKNOWN.

U-5 **Conflation risk written as a conflict so the merge does not create one.** The "**approximately 55,000
sq. ft.**" figure (HD-11) belongs to the **Treasure Island rollback sites** reported in March 1980. Any later
pass that attaches it to "the first Home Depot stores" would be a **fabricated attribute**, and the same trap
exists for the 1987 "Atlanta-based home improvement warehouse" descriptor (HD-13), which is a 1987 description
of a 1987 company and says nothing about the 1979 buildings. / **CONFIDENCE in the warning:** High.

STATUS: WRITTEN 2026-09-25

## Nulls

Split three ways, because collapsing them is how corpora get falsely closed (§15.1). **EMPTY** = queried and
provably nothing. **UNANSWERED** = a route failed (403/404/429/503/401/TLS) and says nothing about content.
**UNTRIED** = see next section; never counted as a null anywhere in this file.

| # | Query / call | Endpoint | Class | Result and what it does *not* prove |
|---|---|---|---|---|
| N-1 | `auto --from 1978-01-01 --to 1992-12-31` on 3,077 filings | EDGAR submissions index | **EMPTY** | 0 rows. Proves the *electronic* record is absent 1978–1992 (index reports "(none)" unanswered slices). Proves nothing about SEC **paper**, where the 1987 S-1 lives. |
| N-2 | `grep 'home depot'` over `micro_IA40706921_0149_djvu.txt` | Internet Archive OCR layer, 223,991 B held | **EMPTY (weak)** | 0 hits in Chain Store Age Executive 1986. One thin reel of a 20-reel run; **not** a statement that CSA ignored the company. Detector proof: same tool got 2 and 4 hits in the DSN layers. |
| N-3 | `grep 'Marcus|Blank|Langone'` over DSN 1987 layer | held bytes, 1,700,633 B | **EMPTY for founders** | "Marcus" → *Nieman Marcus* only; "Blank" → *blank videotape*/**blanketing**; "Langone" → 0. Proves the founders are **not nameable by surname** in this print class — a search-design null, useful to the fleet. |
| N-4 | `collection:(annualreports) AND ("Home Depot")`; `(Home Depot) AND (collection:edgar)` | IA advancedsearch | **EMPTY** | numFound 0 / 0. Home Depot bound corporate print is absent **from IA's public collections**. Does not reach HathiTrust, Google Books, or bound library runs — the gate G1 route. |
| N-5 | `title:("Home Transformation")`; `title:("Beyond the Build")`; `"Handy Dan"`; `creator:("Marcus, Bernie")` | IA advancedsearch | **EMPTY (3) / INSPECTED-NO (1)** | The founders' own retail histories and the asserted prior employer do **not** surface in IA's index; `creator:` returned 1 foreign ISBN whose fields were never inspected. "The founders wrote nothing findable" is **not** a licensed conclusion — HathiTrust/Books were not asked. |
| N-6 | Wayback CDX exact root, `from=1990&to=2000`, both host forms | web.archive.org | **EMPTY** | Earliest capture 1996-11-05. Two forms = one test. No prefix sweep, no sub-paths (N/U-7). |
| N-7 | WebSearch ×2 for founding documents at auction / for the pre-history | general web index | **EMPTY (endpoint-bounded)** | Zero sale records. A web index is not an auction-house name index; Swann/Heritage/Potter and museum accessions were never queried. Do not report "no Home Depot documents exist at auction". |
| N-8 | `grab` accessions `0000354950-94-000001`, `0000907098-94-000015`; manual `…/index.json` | www.sec.gov/Archives | **UNANSWERED** | HTTP 404 / 404 / 503. **No filing bytes at all** are held for this company; `sources/sec/_MANIFEST.csv` is header-only and is a **negative artifact**, not evidence of absence. |
| N-9 | `fetch --id insidehomedepoth0000rous` (Roush 1999) | IA download route | **UNANSWERED** | HTTP 401 ×2 (lending-gated). The one in-window-bearing reported book is unread, not unavailable. |
| N-10 | `fetch --id micro_IA40706924_0308` (DSN 1987), **verified** TLS | IA download route | **UNANSWERED then RESOLVED** | Failed with `SSL: CERTIFICATE_VERIFY_FAILED: certificate has expired`; succeeded on the retry with **`--insecure`**. Disclosed: the 1987 layer's transport is **unverified**, so HD-13…HD-17 carry **Conf ≤ Medium** by tool policy until re-checked. Same fallback used for the Roush attempt. |
| N-11 | `ia_text.py search/mine` as shipped | IA advancedsearch via tool | **UNANSWERED (tool defect)** | The tool builds `fl[]` as a **Python list** into `urlencode` without `doseq`, so `advancedsearch` returns rows with **no fields** (`items: [{}]`) and `mine` fetches nothing. Worked around by querying `fl=identifier,title,year` (comma form) directly and then using the sanctioned `fetch`/`grep` for all bytes. **Report to the owner; do not let another probe read a `mine` zero as a null.** |
| N-12 | `WebFetch` of `THD Timeline.pdf` | corporate.homedepot.com | **UNANSWERED** | Returned raw PDF source, no text, metadata `D:20200220…`. The company's date list is **unread**; HD-23 must not be cited as though it had been read. |

STATUS: WRITTEN 2026-09-25

## Untried

Never counted as nulls above. Ordered by expected Tier-1 yield per call — **the single biggest gap in this
probe is item 1, which is also the cheapest thing on earth to do.**

1. **38 of 41 enumerated reels are un-mined** (identifiers in `sources/EXTRACT_web_documentary_20260926.md` §4):
   Discount Store News **1981, 1982, 1983, 1984, 1985, 1986, 1988, 1989, 1990**; Chain Store Age **all 20 reels**
   (Executive / Supermarkets / General Merchandise / GM Trade editions, 1980–1990) — only one thin CSA reel was
   held; **National Home Center News all 10 reels (1982–1990, 1992)**, which is the title *most* likely to carry
   Home Depot as its own subject rather than as a discounter's neighbour. Each `fetch`+`grep` is one script call
   with a sidecar into `sources/periodicals/`. **This is where the 1981–1986 store-count and sales ramp — the whole
   interior of Stage 1/2 — sits.** The probe's 14 held-bytes records came from 3 reels; a mining run should be
   expected to multiply that, not to be gated by it.
2. **Zero-network mining of bytes already on disk.** 2.2 MB across three layers, grepped for four patterns.
   Un-tried patterns on held bytes: `Treasure Island`, `home center` near `Atlanta`, `warehouse sale`, `DIY`,
   advertised **prices**, opening-day/advertiser mentions, and every store-town name. A dossier agent can settle
   several §D/§E/§F questions without touching the network at all.
3. **Gate G1 — bound corporate print elsewhere:** HathiTrust (`periodical_harvest.py --source-family
   corporate_print`/`hathitrust`, with a `homedepot` block added to `queries.json` — an **owner file, not this
   probe's to edit**), and the legacy Google Books Atom feed (keyless v1 JSON is dead per the UHG run).
   Target: **first printed annual reports FY1988–FY1993** (five-year selected data ⇒ audited FY1983–87), plus
   any bound 1987 prospectus copy. This is the route that flipped Walmart and Target; here it is merely unasked.
4. **Gate G2 — the date-lists and the filing bytes:** re-fetch `THD Timeline.pdf` with a PDF text extractor
   (HD-23); retry the 1994/1995 accession route for the FY1994 10-K's history paragraph and the 1994 proxy's
   officer biographies (`sec_intake.py grab --file` form, or after the directory-listing bug is fixed —
   N-8/HD-05). Also **`facts`** for the 1990–94 window (expect EMPTY: no XBRL pre-2002, so it cannot rescue
   the window).
5. **Registrars and courts — the only records that can date the entity independently of the company and the
   trade press:** **Colorado** SoS (the asserted 1978 Denver formation), **Georgia** SoS charter,
   **Fulton County** (GA) deed/lease indices for the June-1979 sites, and — the sharp one nobody has thought of —
   **Treasure Island's own collapse**: the chain described as "financially troubled" in March 1980 was the
   landlord of Home Depot's first expansion units, so **its bankruptcy/reorganization file (NARA or the
   reporting district's paper docket) should name Home Depot as a tenant in a court record**, which is Tier-1
   and third-party and dated. Untried entirely.
6. **Auction and museum routes by name, not by web search:** Swann, Heritage, Potter & Moore, Reiter's and the
   trade-paper auction catalogues; and the **Georgia Historical Society** (which sponsored the physical marker —
   its holdings/accessions are the nearest thing to a documentary archive of this founding that this probe
   located) plus **Atlanta History Center**, the **AJC/Kenan Research Center morgue** for 1979 clipping files,
   and Home Depot's own corporate archive (a request route, not a fetch). N-7's null covers **none** of these.
7. **1978–1979 issues of the same titles at other holders** (the IA run starts at 1980): HathiTrust, Gale/
   ProQuest trade-press backfiles, and the 1979 Atlanta daily coverage of an opening — the closest thing to this
   company's equivalent of Walmart's 1962 flyer.
8. **Wayback beyond the root:** `matchType=prefix` (expect 504 = UNANSWERED, do not re-run fat sweeps), and the
   **1996–2001 sub-paths** of corporate/news pages — the earliest *archived* company self-narrative of the
   founding, which is the Walmart probe's single most-used document type and is unreadable here (N-12).
9. **Founder paper trails:** Home Depot insider CIKs exist only from 2003 in this index (`3`, `4`, `5` forms) —
   the **1987–1993 Section 16 filings of Marcus/Blank/Langone are paper**, and the 1987 IPO's lockup/ownership
   table lives in the unread prospectus. Nothing in the money-and-control question (§K) is reachable without
   item 3 or item 5.

STATUS: WRITTEN 2026-09-25

---
---

# RE-GRADE 2026-10-06 — probe-homedepot (Stage-1 feasibility retry after RD-135)

**Convention followed (RD-112):** the 2026-09-25 volume above is left **intact**, not deleted or rewritten.
This block is the re-grade against working intake, and it names which of the prior records it supersedes.
Nothing under `sources/` was deleted, moved or "cleaned" by this pass; bytes were only **added**
(`sources/sec/` went from 0 stored documents to 4).

**Headline, one sentence:** family (a) went from **0 bytes held** (HD-05, "UNANSWERED — the document route
is broken") to **4 documents / 676,058 bytes** on disk, and the first thing those bytes say is the fact this
whole company was missing — **the registrant's own Restated Certificate of Incorporation, which dates the
entity to 29 June 1978 and names it, at birth, `M. B. Associates Incorporated`** — which converts the brief's
"two founding years" trap from a coin-flip into a **refuted variant with a carrier**.

## R0. Intake state measured on disk (what the retry actually produced)

Enumerated first, read second (§14 r3; rule 3 of the shared brief). Every row below is a measurement from
`find -printf` / `md5sum` / `python csv.DictReader`, run 2026-10-06.

| artefact | mtime | bytes | md5 | state |
|---|---|---|---|---|
| `sources/_index/_INDEX_CIK0000354950.md` | Oct 6 17:24 | 4,081 | — | **canonical index EXISTS** (built 2026-10-06 11:44 UTC) |
| `sources/_index/submissions_CIK0000354950.csv` | Oct 6 17:24 | 285,227 | `d989943d…` | 3,077 rows; header `filingDate,form,accession,reportDate,primaryDocument,source` |
| `sources/_index/submissions_CIK0000354950.json` | Oct 6 17:24 | 661,035 | `566435b5…` | slice payloads |
| `sources/_index/_registrant_CIK0000354950.json` | Oct 6 17:24 | 536 | — | `"guard": "ok"`, `"csv_sha1": "fa7e61ed887073c4d349aa11a43231aa8487cc11"`, `rows_without_primaryDocument: 72` |
| `sources/_index/quarantine/CIK0000354950/submissions_CIK0000354950.csv` | Sep 30 | 285,227 | `d989943d…` | **byte-identical to the canonical CSV → ONE document, two shelves** (§3, rule 4) |
| `sources/_index/quarantine/…/_registrant_CIK0000354950.json` | Sep 30 | 1,050 | `acf99fa0…` | `"guard": "quarantine"`, reason: *"no slug token ['homedepot'] appears in registrant name 'HOME DEPOT, INC.'"* — the RD-135 false refusal, preserved |
| `sources/_index/{_INDEX.md,submissions.csv,submissions.json}` | Sep 26 01:13 | 3,727 / 288,305 / 685,319 | `9ff1c35a…` / `697b6fd6…` | pre-fix legacy copies, **not deleted by this pass** (their int-typed `cik` is what now breaks the tool — R6 D1) |
| `sources/sec/_MANIFEST.csv` | Sep 26 01:13 | 40 | — | header only: `accession,file,path,bytes,words,status` |
| **`sources/sec/_RUN.json`** | **absent** | — | — | **does not exist and cannot exist while D1 stands** — it is written only by `auto`, which dies before the fetch stage |

Answers to the two questions the brief asked:

1. **The canonical index does exist**, keyed by CIK, with the guard passing: `_INDEX_CIK0000354950.md`
   prints `Registrant guard: **ok** -- slug token(s) ['homedepot'] match registrant 'HOME DEPOT, INC.'` and
   `3077 filings enumerated; 0 submissions rows dropped for carrying no accession; 72 rows carry no
   primaryDocument (paper-era shells -- fetchable as <accession>.txt)`. **RD-135's de-spaced-slug fix is
   confirmed working on this registrant**, so no `index` re-run was needed and none was performed.
2. **What EDGAR answers about the founding window is unchanged and now reproduced twice.** Both walks print
   the same perimeter — the Sep-26 pre-fix index and this pass's walk both enumerate **3,077** rows, min
   `filingDate` **1994-04-19**, max 2026-09-22, and a header-enumerated field read over the canonical CSV
   returns **`rows before 1993-07-01: 0`**. This pass printed `walk: 2 slices (2 fetched, 0 failed), 3077
   filing rows, date perimeter 1994-04-19 -> 2026-09-22` — **2 slices**, so RD-134's 8-slice cap was *never
   binding* for this registrant and the prior probe's floor was never a truncation artefact. The floor is
   re-graded **CONFIRMED**, not provisional (the RD-134 caveat that "every filings-family verdict before
   tonight is provisional" is **discharged for this company**).

**Stale instruction-layer record (RD-124 r10 — a retraction is not finished until it reaches the files that
tell agents what to believe).** `00_universe/_FLEET_INTAKE.tsv` row 38 still reads
`rc2/inwindow0/UNANS0 … 1994-04-19 … identity guard refused the write … REFUSED`, and
`_IDENTITY_FIX.log:11,14` still prints that refusal for CIK 354950. Both are **pre-fix states** and are now
contradicted on disk (guard `ok`, canonical index present, 4 documents stored). Owner action, not mine:
row 38's `pass1_status`/`note`/`state` need a dated correction, or the next dispatcher will re-refuse this
company straight out of the resume table. **This probe did not edit the TSV.**

## R1. Verdict, re-graded

**Stage 1: T2 CORE (was T3). Families counted: (a) and (c).** The tier now turns on the RD-112 boundary case
the convention has still not decided, and the decision is printed rather than averaged:

> **Counting decision (mine to make, stated so it can be attacked).** Family (a) returns **in-window FACTS
> carried in a constitutive legal instrument** — the registrant's own charter, filed as Exhibit 3.1 — but
> **no in-window DOCUMENT**, because the EDGAR floor is 1994-04-19. Under the Ford precedent (RD-134, the
> recital route: "for a pre-1960 company here the founding sentence can only live in a filing the company's
> own window excludes") and the shared brief's own instruction to run a forward window, that instrument
> counts. Under a strict document-in-window reading it does not, and Stage 1 is **T3 on one family (c)
> alone**. Both readings are reported here; the fleet should dispatch on **T2 core, cap 22k w/stage**, and
> know that the alternative reading is defensible. What the second reading cannot do is keep the T3 label
> the 2026-09-25 probe issued, because that probe issued T3 while family (a) was recorded as **UNANSWERED** —
> and an unanswered family is not a null either. **The 2026-09-25 T3 was therefore never a measurement of a
> quiet archive: it was a measurement of our own broken downloader** (RD-112's Costco/Dell class arriving
> here from the opposite direction — a probe *under*-tiering because its tool failed silently).

**No family was inflated.** (b) web, (d) corporate print and (e) documentary are **UNTRIED on this pass**
(web budget 0; the two harvesters were forbidden by the brief) and are recorded as UNTRIED below, never as
nulls; the 2026-09-25 measurements for them are **inherited and labelled as inherited**.

| stage (PROPOSED window) | tier now | families returning text usable *about* that window | provisional because |
|---|---|---|---|
| **1 — entity to scalable formation**, **1978-06-29 → 1988-01-31** | **T2 core** (was T3) | **(a)** charter + proxy/10-K recitals + FY1989–93 series; **(c)** DSN 1980 four-unit Atlanta / "former discounter Bernie Marcus" / Treasure Island ~55,000 sq ft | (d) untried this pass; no in-window SEC document exists; the 1981–1987 interior is still un-mined print |
| **2 — listed company, provincial to national**, **1988-02-01 → 1994-01-30** | **T2 core** (unchanged) | **(a)** FY1989→FY1994 selected data in EX-13 of two filings + 264/340 store counts + Aikenhead's/Waban 1993–94 expansion; **(c)** DSN/CSA 1988–1990 reels enumerated (18 unmined) | every number is *about* the window but filed after it; no in-window 10-K or 8-K exists |
| **3 — the EDGAR era**, **1994-04-19 →** | **T2 measured / T1 reachable — indicative only, not this probe's stage** | **(a)** 4 documents held here, 3,077 enumerated; **(b)** index-confirmed floor 1996-11-05 *(inherited, not re-measured)* | (c) in-window reels unmined; (d)/(e) untried this pass |

**Per §15.2 the implied agent budget for Stage 1 rises from 3–4 runs to 6–9 runs.** The 2026-09-25 file's
"recommend dispatching at T3 … expect T2" is now **executed**: the expectation is a measurement, and the
dossier should sit in the **upper part of the 22k band**, filings-led on the entity question and
trade-print-led on everything the filings do not say.

STATUS: WRITTEN 2026-10-06

## Five-family verdict table (this pass, 2026-10-06)

Three states only, per the shared brief: TRIED–ANSWERED / TRIED–UNANSWERED (remedy named) / UNTRIED.

| family | state this pass | what it returned | remedy if unanswered / untried |
|---|---|---|---|
| **(a) SEC / EDGAR filings** | **TRIED–ANSWERED** (was TRIED–UNANSWERED at HD-05) | 4 documents, 676,058 B, 84,014 words: FY1994 10-K (162,266 B), 1994 DEF 14A (60,533 B), FY1995 10-K405 (216,512 B), FY2000 10-K (236,747 B). Includes the Restated Certificate of Incorporation. **0 in-window documents; floor 1994-04-19 re-confirmed.** | R6-D1 (`auto` crash) and R6-D2 (`grab` enumeration crash) are owner one-liners; **68 paper-era `.txt` shells** remain fetchable, one call each |
| **(b) web archives** | **UNTRIED this pass**; inherited: floor 1996-11-05, null-by-construction for 1978–1987 (HD-06/07) | nothing new | an orchestrator CDX run (a probe has 0 web calls); `matchType=prefix` and the 1996–2001 `/about`–`/history` sub-paths still untried (HD-08) |
| **(c) periodical corpora** | **TRIED–ANSWERED** (bytes already on disk; the two harvesters were **not** run, per brief) | the same 3 held layers re-grepped: DSN 1980 = **2** hits, CSA 1986 = **0**, DSN 1987 = **4**; the HD-09 passage re-verified verbatim at l.19008–19015 | 38 of 41 enumerated reels unmined; `periodical_harvest.py --facet-free` is the next-pass route |
| **(d) digitised corporate print** | **UNTRIED this pass** (harvesters forbidden); inherited: searched-and-empty at the IA endpoint (HD-18, N-4) | **indirect advance:** family (a) now *proves* the printed annual reports exist and what they contain — Item 6 of two 10-Ks incorporates by reference the "**Ten Year Selected Financial and Operating Highlights**" of the AR | HathiTrust + bound AR runs **FY1988–FY1993**: the AR embedded in the FY1994 shell prints **only the FY1989–FY1993 columns** (measured, HD-A9), so the **FY1984–FY1988 columns live only in the printed report** |
| **(e) auction / museum / manuscript** | **UNTRIED this pass** (0 web calls); inherited: one 2016 GHS statement, unread company PDF, auction route searched to nothing (HD-22/23/24) | the registrant's own ownership table (HD-A6) partly substitutes for what this family was to settle about money | name-indexed auction/museum catalogues; registrars — **now sharpened to one question: the Delaware charter file for `M. B. Associates Incorporated`, 29 June 1978** |

STATUS: WRITTEN 2026-10-06

## R2. Family a — what the registrant's own filings say (records HD-A1 … HD-A12)

Line numbers are **locators only** (§14 r12); address these records by their ID. All four documents are
HTTP 200 with `.meta.json` sidecars recording url/sha1/bytes/words (`sources/sec/`). Tier: **1** for every
record below (SEC filing). Independence is scored per the §3 **filing-lineage rule**: the 1994 proxy, the
FY1994/FY1995/FY2000 10-Ks and the Exhibit 3.1 charter are **all one lineage** — the registrant's own
corporate record — so a fact repeated in three of them is corroborated **once**, not three times.

HD-A1 Claim: The registrant `HOME DEPOT, INC.` was **originally incorporated on 29 June 1978 under the name
`M. B. Associates Incorporated`**, per its own Restated Certificate of Incorporation — the only dated
birth-certificate of the entity recovered anywhere in this corpus, and the carrier that supersedes HD-22's
undated "founded … in 1978" — Date: 1978-06-29 — Source: Exhibit 3.1 (EX-3.1), Restated Certificate of
Incorporation of The Home Depot, Inc., as amended, filed inside acc **0000354950-95-000002** (FY1995 10-K405,
filed 1995-04-20) — Source date: 1995-04-20 (filing); 1978-06-29 (event) — URL:
https://www.sec.gov/Archives/edgar/data/0000354950/000035495095000002/0000354950-95-000002.txt — Archived:
`sources/sec/0000354950-95-000002_0000354950-95-000002.txt` (216,512 B, sha1 `7ab587647a…`), locator l.1074-1075 —
Tier: 1 — Class: FACT (event date stated by the entity's own constitutive instrument; the instrument itself
is a **RETROSPECTIVE SOURCE** for anything earlier than its own date, §6) — Passage: "(Originally
incorporated on June 29, 1978 under the name M. B. Associates Incorporated)" — Conf: **High** —
Corroboration: **1 lineage** (the FY2000 seal article, HD-A8, is the same lineage) — Conflicts: **U-1**
(resolved on the incorporation leg), **U-6**.

HD-A2 Claim: The corporation is and was a **Delaware** corporation — registered office 1209 Orange Street,
Wilmington, New Castle County; registered agent The Corporation Trust Company — so no held EDGAR document
supports a **Georgia or Colorado** original jurisdiction for the registrant, and the lore's "Denver
incorporation" has **no carrier here** — Date: 1995-04-20 (as filed) — Source: as HD-A1, EX-3.1 SECOND
clause; and FY1994 10-K cover `STATE OF INCORPORATION: DE` — Source date: 1995-04-20 / 1994-04-22 — URL:
as HD-A1 — Archived: as HD-A1 + `sources/sec/0000354950-94-000001_0000354950-94-000001.txt` (162,266 B,
sha1 `27379a5d6e…`), locators l.26, l.67, l.1078-1083 — Tier: 1 — Class: FACT — Passage: "The address of the
Corporation's registered office in the State of Delaware is 1209 Orange Street, in the City of Wilmington,
in the County of New Castle." — Conf: High — Corroboration: 1 lineage, 3 documents — Conflicts: none
in-hand; **the registrar question is narrowed, not answered** (Untried item 5): a Delaware charter file for
`M. B. Associates Incorporated` would be the independent third-party twin of HD-A1.

HD-A3 Claim: The registrant's own documents date the **business's start** only by the ambiguous word
**"inception"**: Marcus "has been its Chairman of the Board of Directors and Chief Executive Officer … since
its **inception in 1978**"; Blank "has been President, Chief Operating Officer ('COO') and a director … since
its **inception in 1978**"; Brill "joined The Home Depot as its Controller in 1978" — Date: 1978 (event,
undated within the year); carriers 1994-04-19 and 1994-04-22 — Source: 1994 DEF 14A acc
**0000907098-94-000015** (60,533 B, sha1 `ae98898b76…`) l.381-384, l.409-415; FY1994 10-K l.350, l.365,
l.375-378 — Source date: 1994-04-19 / 1994-04-22 — URL:
https://www.sec.gov/Archives/edgar/data/0000354950/000090709894000015/0000907098-94-000015.txt — Archived:
`sources/sec/0000907098-94-000015_0000907098-94-000015.txt` — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION
(16 years after the event) — Passage: "since its inception in 1978" — Conf: High (that the registrant says
this) — Corroboration: 1 lineage — Conflicts: **U-6** (the word "inception" is doing work the charter does
not license: it can be read as entity formation *or* as trading start, and the filings never disambiguate
it; HD-A1 pins **incorporation**, nothing in family (a) pins **trading**).

HD-A4 Claim: **The registrant names THREE co-founders, not two** — Bernard Marcus, Arthur M. Blank and
Kenneth G. Langone — and does so in 1994, 1995 and 2000 — Date: about 1978; carriers 1994-04-19, 1995-04-20,
2000-04-21 — Source: 1994 DEF 14A l.381-384 ("is, together with Mr. Bernard Marcus and Mr. Kenneth G.
Langone, a co-founder of the Company"), l.409, l.419; FY1995 10-K405 l.423, l.436-437; FY2000 10-K acc
**0000950144-00-005338** (236,747 B, sha1 `dd20c968ec…`) l.881-891 — Source date: as listed — URL:
https://www.sec.gov/Archives/edgar/data/0000354950/000095014400005338/0000950144-00-005338.txt — Archived:
`sources/sec/0000950144-00-005338_0000950144-00-005338.txt` — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION —
Passage: "Mr. Blank … is, together with Mr. Bernard Marcus and Mr. Kenneth G. Langone, a co-founder of the
Company." — Conf: High (registrant's position) / **Medium** (the historical fact — one lineage, 16 years
late) — Corroboration: **1 lineage; 8 `co-founder` occurrences across the 4 documents** (measured:
`grep -i -o "co-founder" *.txt | wc -l` → 8) — Conflicts: **U-2** (now a **three-carrier** conflict: one
in-period witness naming one man, the 2016 commemorative naming two, the registrant naming three).

HD-A5 Claim (the brief's trap (2), answered with **roles, not founder adjectives**): the registrant's filings
state each principal's **office and its start date** — **Marcus**: Chairman of the Board, and Chairman + CEO
from inception 1978 until 1997, when the CEO title passed to Blank; **Blank**: President, COO and a director
from inception 1978, named President and CEO in 1997; **Langone**: a director since 1978, "for at least the
past five years" Chairman, CEO, President and Managing Director of **Invemed Associates, Inc.**, an NYSE
member investment-banking/brokerage firm — i.e. an **outside director whose day job was not the company**;
**Ronald M. Brill** (the fourth man, never called a co-founder in any held document): Controller 1978 →
Treasurer 1980 → VP-Finance 1981 → SVP and CFO 1984 → director 1987 → EVP and CFO 1993 → EVP and Chief
Administrative Officer 1995 — Date: 1978–2000 (offices) — Source: as HD-A4; FY2000 10-K l.881-899; FY1994
10-K l.350, l.375-378; 1994 DEF 14A l.381-384, l.419-425 — Source date: 1994-04-19 / 1994-04-22 / 1995-04-20 /
2000-04-21 — URL: as HD-A1/HD-A4 — Archived: as above — Tier: 1 — Class: FACT about what the company states
of its offices; RETROSPECTIVE for 1978–1987 — Passage: "Mr. Brill joined The Home Depot as its Controller in
1978, was elected Treasurer in 1980, Vice President-Finance in 1981, Senior Vice President and Chief
Financial Officer in 1984, and elected as a director in 1987." — Conf: High — Corroboration: 1 lineage —
Conflicts: **U-2**. **Standing instruction for the dossier:** a Stage-1 §B/§N may not write "the three
founders ran the company". On the registrant's own record two men held operating offices, one held a
directorship at an outside bank, and the earliest in-window witness (HD-10) names **one** man as founder.

HD-A6 Claim: The third co-founder's documented relationship to the company is a **paid advisory contract**,
not founding capital: Langone, then Chairman and President of Invemed, sat on the Compensation Committee
during fiscal 1993, and "The contract provides for the Company to pay Invemed an annual consulting fee of
**$100,000**" for "investment banking consulting services", cancelable on 60 days' notice — Date: fiscal 1993
disclosure, proxy of 1994-04-19 — Source: 1994 DEF 14A l.493-501 ("Compensation Committee Interlocks and
Insider Participation"); FY1994 10-K l.771 lists the Invemed contract among the exhibits — Source date:
1994-04-19 — URL: as HD-A3 — Archived: as HD-A3 — Tier: 1 — Class: FACT — Passage: "which provides investment
banking consulting services to the Company under a written contract which is cancelable by either party upon
sixty days written notice. The contract provides for the Company to pay Invemed an annual consulting fee of
$100,000." — Conf: High — Corroboration: 1 lineage, 2 documents — Conflicts: **U-7** (new: this evidences an
*ongoing* paid relationship in 1993 and is routinely mis-read downstream as proof that Langone supplied the
1978 capital; the 1978 money has **no carrier** in any held byte — the §K founding cap table stays UNKNOWN).

HD-A7 Claim: The **only ownership figures EDGAR holds** for the principals: Marcus **14,819,019** shares /
**3.30 %**; Blank **8,349,952** / **1.86 %**; Langone **4,600,000** / **1.02 %**, with footnotes recording
family, foundation and trust holdings — Date: the 1994 proxy's record date, about the fiscal-1993 position —
Source: 1994 DEF 14A l.238-240 with notes (3)(4)(5) — Source date: 1994-04-19 — URL: as HD-A3 — Archived: as
HD-A3 — Tier: 1 — Class: FACT (for 1994) — Passage: "Bernard Marcus (3) 14,819,019 3.30 / Arthur M. Blank (4)
8,349,952 1.86 / Kenneth G. Langone (5) 4,600,000 1.02" — Conf: High — Corroboration: 1 — Conflicts: none.
**Do not** read these as founding-era stakes: they are post-listing and post-split (the July 1992
three-for-two and April 1993 four-for-three stock dividends are stated in the FY1995 tables) and 16 years
after the capital was raised.

HD-A8 Claim: The founding story the filings tell is **entity-first, not store-first**: across all four held
documents `first two stores` occurs **0** times, `opened its first` **0**, `Handy Dan` **0**, `napkin` **0**,
`Treasure Island` **0**, and **`1979` occurs 3 times — every one of them a hiring date** ("Mr. Mercer joined
the Company in 1979 as an Assistant Store…"); the only founding-era mark the company engraves on itself is
its **seal** — "the words and figures '**Incorporated 1978 Delaware**' across the center" — Date: carriers
1994-04-19 → 2000-04-21 — Source: measurement over `sources/sec/*.txt` (`for pat in "first two stores"
"opened its first" "Handy Dan" "napkin" "Treasure Island" "Langone" "co-founder" "1979" "June 29, 1978"
"M. B. Associates"; do grep -i -o "$pat" *.txt | wc -l; done` → **0, 0, 0, 0, 0, 40, 8, 3, 1, 1**), plus
FY2000 10-K EX-3.1 ARTICLE VIII l.2632 — Source date: as listed — URL: n/a (local grep) — Archived: all four
`.txt` files + sidecars — Tier: 1 — Class: FACT (documented absence **over these four documents only**) —
Passage: "It shall be circular in form and shall have engraved upon it the name of the Corporation arranged
in a circle and the words and figures 'Incorporated 1978 Delaware' across the center of the space enclosed." —
Conf: High — Corroboration: 1 lineage — Conflicts: **U-1** (this measurement kills the "1979 = incorporation"
variant and leaves the *trading* year with **no** EDGAR carrier at all).

HD-A9 Claim: **The earliest fiscal year inside any held EDGAR byte is fiscal 1989**, and family (a) cannot
number the founding decade: EX-13 of the FY1994 10-K carries a table titled "**Ten Year Selected Financial
and Operating Highlights**" whose **printed columns stop at fiscal 1989** — net sales **$2,758,535K**, **118**
stores, **10,424,000** sq ft, **17,500** employees, **12** states, EPS **.32** — while the FY1995 10-K405's own
EX-13 prints fiscal **1990–1994** only (measured: `2,758,535` appears **0** times in the FY1995 file; the
FY1994 table block contains exactly **one** pre-1989 year token, and it is the "1984" of a 53-week footnote,
not a data column) — Date: fiscal 1989 (ended January 1990 on this registrant's Sunday-near-31-January
year-end) — Source: FY1994 10-K acc 0000354950-94-000001 EX-13 l.1339-1420; FY1995 10-K405 EX-13 l.2626-2660;
Item 6 of each incorporates the Annual Report by reference (10-K94: "for the fiscal years **1988-1993**";
10-K95: "**1989-1994**") — Source date: 1994-04-22 / 1995-04-20 — URL: as HD-A1 — Archived: as HD-A1 +
`0000354950-94-000001_…txt` — Tier: 1 — Class: FACT for the printed columns; the FY1988 figures below are a
**narrative aside**, not a column — Passage: "From the end of fiscal 1988 to the end of fiscal 1993, the
Company increased its store count by an average of approximately 22% per year (from 96 to 264 stores) and
increased the total store square footage by an average of approximately 26% per year (from 8,216,000 to
26,383,000 total square feet)." — Conf: High — Corroboration: 1 lineage — Conflicts: none. **Consequence for
family (d):** the printed FY1994 annual report *by its own title* holds ten years — fiscal **1984–1993** —
and the EDGAR rendition of it is missing the **FY1984–FY1988** half. That is now a measured gap with a named
carrier, not a hope: the FY1988 **96 stores / 8,216,000 sq ft** pair is the single earliest founding-decade
number EDGAR offers, and it survives only inside a growth-rate sentence.

HD-A10 Claim (trap (3), demonstrated rather than warned about): **the same fiscal year, in the same table,
was restated between two consecutive 10-Ks** — fiscal-1993 **long-term debt** is **841,992** (`$000`) in the
FY1994 10-K's EX-13 and **874,048** in the FY1995 10-K405's EX-13 (**+32,056**, **+3.8 %**), and the derived
long-term-debt-to-equity ratio moves **29.9 % → 31.1 %** while **stockholders' equity stays 2,814,100** and
**total assets stay 4,700,889** in both (arithmetic shown: 841,992 ÷ 2,814,100 = 29.92 %; 874,048 ÷ 2,814,100
= 31.06 %) — Date: fiscal year ended 1994-01-30; carriers 1994-04-22 and 1995-04-20 — Source: FY1994 10-K
l.1378, l.1381; FY1995 10-K405 l.2656, l.2659 — Source date: as listed — URL: as HD-A1 — Archived: as HD-A1 —
Tier: 1 — Class: **ESTIMATE / DERIVED** for the delta and the ratio check (this probe's arithmetic over filed
figures); FACT for the two debt values — Passage: `Long-term debt 50.9 841,992 843,672 270,575 530,774
302,901` / `Long-term debt 26.6 23.6 983,369 874,048 843,672 270,575 530,774` — Conf: High — Corroboration:
1 (the point is the **divergence**, not the agreement) — Conflicts: **new U-8**. **Standing instruction:** a
Home Depot figure quoted from a 1990s filing is **RESTATED** until matched against the filing of that year;
nothing dated 1994 or later can be labelled CONTEMPORANEOUS for a founding-decade event. The contemporaneous
class for the founding decade would be a 1979–1987 paper document, which EDGAR cannot supply at all (floor
1994-04-19, HD-02/03 re-confirmed this pass).

HD-A11 Claim: What the filings do give Stage 2 is a **clean anchor at the top of the window**: at fiscal-1993
year-end the company ran **264 stores in 23 states**, ~26,383,000 sq ft, averaging ~100,000 sq ft enclosed
per store, with fiscal 1994 at **340 stores / 35,133,000 sq ft**; the first expansion outside the Sunbelt
began "**in late fiscal 1988**"; fiscal-1993–1994 turned Canadian through **Aikenhead's** (75 % interest
bought from the Molson Companies, seven stores operating plus three scheduled) and the **Waban/HomeBase**
purchase of seven non-operating Chicago-area sites — Date: 1994-04-22 / 1995-04-20 (carriers) — Source:
FY1994 10-K l.138-145, l.440-520; FY1995 10-K405 l.600-611 — Source date: as listed — URL: as HD-A1 —
Archived: as HD-A1 — Tier: 1 — Class: FACT (contemporaneous for the fiscal year each filing reports;
RETROSPECTIVE for the "late fiscal 1988" clause, which is a 1994 sentence about 1988) — Passage: "At fiscal
year end the Company's three operating divisions--Western, Southeast and Northeast--had 264 stores in 23
states with an aggregate total of approximately 26,383,000 square feet of selling space." — Conf: High —
Corroboration: 1 lineage (the FY1995 confirmation of 264 is the same lineage) — Conflicts: none. The
concentration measurement is the corpus's only in-file answer to "was it national yet": "**68 %** being
concentrated in California, Georgia, Texas, Florida and Arizona" (FY1994 10-K l.476-478).

HD-A12 Claim: **The FY1994 10-K `.txt` shell is the whole accession, not just the form** — 7 concatenated
documents (`<TYPE>10-K`, EX-10, EX-11, EX-13, EX-21, EX-23, EX-24; measured `grep -c "<DOCUMENT>"` → **7**),
which is why the annual-report financial exhibit and the subsidiary list are on disk in one file; EX-21 names
**`M B Food Service, Inc.` (Delaware)** beside Home Depot U.S.A., Home Depot International, Homer II/III/TLC,
Homerlease and Services, Inc. — Date: 1994-04-22 — Source: FY1994 10-K l.43, l.1190, l.1244, l.1333, l.2735,
l.2789, l.2836; EX-21 l.2751-2776 — Source date: 1994-04-22 — URL: as HD-A1 — Archived: as HD-A1 — Tier: 1 —
Class: FACT — Passage: "M B Food Service, Inc. Delaware" — Conf: High — Corroboration: 1 — Conflicts: none.
**Why this record exists:** a surviving "M B" name in the 1994 subsidiary list shares initials with the 1978
charter name (`M. B. Associates Incorporated`, HD-A1). **That is a lead about a name, not a finding** — no
held document says they are the same entity or that one continues the other, and §14 r5 forbids treating a
shared initial as lineage. Any later pass linking them must first produce a charter amendment or a certificate
of merger.

STATUS: WRITTEN 2026-10-06

## R3. Family c — re-verified in the held bytes; no harvester was run

The brief forbade `harvest_mine.py` and `periodical_harvest.py` on this pass, so family (c) was advanced
**zero-network**, over bytes already on disk (2,260,561 B across three OCR layers, each with its
`.meta.json` sidecar).

HD-C1 Claim: The 2026-09-25 periodical measurements **reproduce exactly**: `grep -c -i "home depot"` returns
**2** hits in `micro_IA40706901_0406_djvu.txt` (DSN 1980), **0** in `micro_IA40706921_0149_djvu.txt` (Chain
Store Age Executive 1986), **4** in `micro_IA40706924_0308_djvu.txt` (DSN 1987) — and the load-bearing HD-09
sentence is re-read **in the bytes**, at locators l.19008-19015: "Last year, the Home Depot, a four-unit home
center chain in Atlanta, founded by former dis- counter Bernie Marcus, took advantage of Treasure Island's
decision to roll back the size of its stores and became a tenant of the financially troubled …" — Date:
1980-03-10 (issue) about 1979 — Source: `sources/periodicals/*_djvu.txt` — Source date: retrieved
2026-09-26, re-grepped 2026-10-06 — URL: n/a (local) — Archived: the three layers as held — Tier: 1 (§14 r6) /
3 (§5) — Class: CONTEMPORANEOUS OBSERVATION — Passage: as quoted, OCR line-wrap preserved as held — Conf:
High (HD-09 re-confirmed) — Corroboration: 1 in-period, unchanged — Conflicts: **U-1, U-2, U-4** (all still
live; family (a) did not resolve the trading year).

HD-C2 Claim: Two **negative** measurements sharpen what family (c) can and cannot be asked to do:
`grep -c -i "treasure island"` returns **3 / 0 / 0** over the same three layers (the mechanism exists only in
the DSN 1980 reel), and `grep -n -i "home depot.*197[89]|197[89].*home depot"` over all three layers returns
**nothing — 0 lines** — i.e. **the held trade print never puts the company's name next to a founding year**.
So the "1978" and the "1979" both come to this dossier from outside family (c): HD-A1 (charter, 1978) and
HD-22 (GHS 2016, 1978 + 22 June 1979). — Date: 1980/1986/1987 layers — Source: local grep, commands as printed
— Source date: 2026-10-06 — URL: n/a — Archived: as HD-C1 — Tier: 1 (documented absence in held bytes) —
Class: FACT (absence, three reels only) — Passage: NO_VERBATIM_PASSAGE_RECORDED (negative finding) — Conf:
High — Corroboration: 1 — Conflicts: none.

HD-C3 Claim (re-read A4 before quoting it, per the brief — done, and it says something nobody has counted):
`research/A4_harvest_mine.md` + `sources/harvest_mine/_index.json` record a fleet-mine pass over window
**1978-01-01..1990-12-31** with **13 candidate rows, 6 items mined, 6 untried at the `--limit`**, and **all 6
mined items UNANSWERED — `HTTP 503`, 0 bytes each** (`Wpo8v92NgjoC`, `KQUKFmw0BkAC`, `ZbBkDAAAQBAJ`,
`vYlFDAAAQBAJ`, `k7HWONIo88YC`, `98ktCgAAQBAJ`). Counts on that page: `TIER1_CANDIDATE_TEXT` **0**,
`VARIANT_TERM_HIT` **0**, `BARE_WORD_MATCH` **0**, `NULL` **0**, `UNANSWERED` **6**. Crucially A4's own line
reads: "**name phrases**: none; **other quoted terms** (predecessors, siblings, trade titles): none" — so
for this slug the RD-124 entity classifier had **no vocabulary at all**; a successful fetch would still have
been judged on the bare word `home depot`. **This is an intake gap, not a corpus null** — the correct label
for the fleet-mine shelf is TRIED–UNANSWERED (6 × 503) *with an empty entity vocabulary*, and the remedy is
a `homedepot` query block carrying the phrases this probe can now name for free: `M. B. Associates`,
`Treasure Island`, `Bernie Marcus`, `Arthur Blank`, `Ken Langone`, `Ronald Brill`, `Home Depot Atlanta`, plus
the predecessor-format titles already enumerated. The six 503 identifiers are listed for the orchestrator in
R8; their scan/title dates (1999–2016) are digitisation years and place none of them in the window.

STATUS: WRITTEN 2026-10-06

## R4. Boundaries, re-graded (per-stage, per RD-112; every window PROPOSED)

`00_universe/fortune_top_50_2026.csv` header enumerated before any field was read (rule 3): `rank, company,
revenue_usd_millions, revenue_fiscal_year, profit_usd_millions, hq_city, hq_state, fortune_industry,
universe_source_url, verified_by_second_source, confidence, notes` — **there is no founding-date column**, so
nothing below is inherited from the universe file. Row 25 (case-insensitive match, 50 data rows total):
`25 | Home Depot | 164683 | fiscal year ended 2026-02-01 | 14156 | Atlanta | Georgia | Specialty Retailers:
Other | … | SEC EDGAR 10-K XBRL: exact match on revenue and profit | High`. That row corroborates rank,
money and — usefully for this probe — the **fiscal-calendar shape**: FY2026 ended **2026-02-01**, a Sunday,
matching the 1994–2000 `reportDate` values in the canonical index (1994-01-30, 1995-01-29, 1996-01-28,
1997-02-02, 1998-02-01, 1999-01-31, 2000-01-30). **The year-end is the Sunday nearest 31 January**, which is
why any Stage boundary expressed as "January 31" must be written as a fiscal-year label, not a date.

| stage | window (PROPOSED) | what changed this pass | the carrier for each edge | confidence |
|---|---|---|---|---|
| **1 — entity, format, proof** | **1978-06-29 → 1988-01-31** | **the start edge now has a dated legal carrier** — it was "Low, retrospective-only" (Boundaries table, 2026-09-25) and is now Tier-1 | Start: **HD-A1**, EX-3.1 to acc 0000354950-95-000002, "(Originally incorporated on June 29, 1978 …)". End: **no listing carrier exists** — the earliest fiscal boundary family (a) can name is fiscal-1988 year-end, from the narrative aside "from 96 to 264 stores" (**HD-A9**); trading start (1979) rests on HD-C1/HD-22 | Start **High** · trading year **Low-Medium** · End **Low** (asserted 1987 listing unattested, U-3) |
| **2 — listed, provincial to national** | **1988-02-01 → 1994-01-30** (fiscal years, not calendar) | family (a) supplies **numbers for the whole window** for the first time (fiscal 1989→1993 columns; 1990→1994 in the next filing) | Start = fiscal-1988 end (**HD-A9**). End = the FY1994 10-K's own period, **1994-01-30** (canonical index row 3, HD-02 re-confirmed) | Start **Medium** · End **High** |
| **3 — the EDGAR era** | **1994-04-19 →** | unchanged, and now demonstrably not a truncation artefact (walk printed 2 slices of 2; 3,077 rows reproduced) | The measured floor itself: DEF 14A acc 0000907098-94-000015 (**HD-02**) | **High** |

**Why the Stage-1 end stays 1988-01-31 instead of an IPO date.** The listing event has **no carrier of any
kind on this machine** (HD-03, HD-17, U-3 all re-confirmed; this pass added no in-window document). FY1988 is
chosen because it is the earliest boundary that family (a) can *name with a number* rather than with lore,
and because it sits within one fiscal year of the asserted listing. It is a **documentary convenience, not a
proven transformation**, and the dossier must say so: the alternative — ending Stage 1 at the IPO — is a
**FETCH REQUEST** (R8), not a finding.

**§6 fit, re-stated with the new carriers.** *Origin* now has an entity answer (1978-06-29, Delaware,
as `M. B. Associates Incorporated`) and **no** answer on who raised what — the money question is untouched by
family (a) and remains HD-25's retrospective layer plus UNKNOWN. *First experiment* keeps its trade-print
mechanism (HD-11, ~55,000 sq ft at each Treasure Island rollback site, 1979 reported 1980) and gains nothing
from EDGAR, which does not mention Treasure Island (**0** occurrences, HD-A8). *Repeatable validation* gains
one EDGAR-adjacent anchor it did not have: the company's own later statement that the format had reached
**96 stores / 8,216,000 sq ft by fiscal-1988 end** (**HD-A9**) — a 1994 sentence about 1988, so RESTATED by
filing date, but the earliest self-reported scale in the electronic record. *Scalable formation* (the
listing, the post-listing capital structure) is still unanswerable from held bytes except for the 1994
ownership percentages (**HD-A7**) and the split history, which are end-state, not formation.

**Nothing in the founding decade is now numbered — and that is the finding to hand the fleet.** The single
founding-decade number family (a) yields is **fiscal 1989** (118 stores, $2.76 bn, 17,500 employees), a
decade after incorporation, obtained from a table whose *title* promises ten years. Every 1979–1987 store
count, every first-year sales figure, and the 1987 offering itself remain outside EDGAR's reach by
measurement, not by assumption.

STATUS: WRITTEN 2026-10-06

## R5. Conflicts updated (U-1 … U-8); none is closed except where a carrier closed it

**U-1 — RE-GRADED, incorporation leg RESOLVED; trading leg still OPEN.** The 2026-09-25 statement "no
document on this run ties [1978] to a state or a day" is **superseded**: the registrant's own Restated
Certificate of Incorporation ties the entity to **29 June 1978, Delaware, as `M. B. Associates Incorporated`**
(HD-A1, HD-A2). / **WHY THEY DIFFER:** the brief's circulating pair ("1978 = the Atlanta opening and the
merger of two other home-improvement businesses"; "1979 = incorporation") is **refuted on its second half**
by the charter — incorporation is 1978, not 1979 — and its first half has **no carrier in family (a)**: the
held filings contain **0** occurrences of `first two stores`, **0** of `opened its first`, **0** of any
merger-of-predecessors language, and `1979` only as a hiring date (HD-A8). The *trading* year rests on two
non-EDGAR lineages: DSN 1980 ("Last year … a four-unit home center chain in Atlanta", HD-C1) and GHS 2016
("first two … stores on June 22, 1979", HD-22). / **BEST-SUPPORTED READING:** one legal person born
**1978-06-29 in Delaware under a shell name**; trading in Atlanta in **1979** at four units by that year's
end; **what happened between June 1978 and the first store opening is a documented blank**, and that blank —
not the year fight — is the real Stage-1 origin question. / **RESIDUAL:** the rename from `M. B. Associates
Incorporated` to `The Home Depot, Inc.` (date and instrument unheld), whether `M B Food Service, Inc.`
(HD-A12) is related, and the "two other home-improvement businesses" element (carrierless → FOUNDER CLAIM or
UNKNOWN). / **CONFIDENCE:** **High** for 1978-06-29 incorporation; **Low-Medium** for 1979 trading; **UNKNOWN**
for a first-store day.

**U-2 — RE-GRADED, now three carriers, still unresolved as a count.** In-period DSN 1980 names **one**
founder ("founded by former discounter Bernie Marcus", HD-10); the registrant names **three** co-founders in
1994, 1995 and 2000 (HD-A4, 8 `co-founder` occurrences measured); the 2016 commemorative names **two**
(HD-22). / **WHY THEY DIFFER:** the trade named the operator it knew; the company's proxy names the pair plus
the banker, because by 1994 that was the legally relevant founding group and the proxy's job is to disclose
directors, not to settle history. / **EVIDENCE WEIGHT:** the EDGAR formulation is **one lineage 16 years
late**; the DSN line is **in-window but single**. Nothing proves either wrong. / **BEST-SUPPORTED:** record
**roles** (HD-A5) rather than a founder list; Marcus and Blank as operating principals from "inception",
Langone as director + outside investment banker paid $100,000/yr by contract (HD-A6); a fourth early man,
Brill, is a 1978 hire, **not** a founder in any held document. / **RESIDUAL:** the napkin/epiphany folklore —
`napkin` **0** occurrences in held filings and no carrier anywhere in this corpus — stays **FOUNDER CLAIM or
UNKNOWN, never FACT**. / **CONFIDENCE:** High on each carrier's words; **Medium** on the merged three-name
list (single lineage); Low on any two-name list.

**U-3 — UNCHANGED and now better bounded.** The 1987 listing still has **no carrier on disk**: EDGAR floor
1994-04-19, first 8-A is an 8-A12B of 1996-09-24 (HD-04), the held DSN 1987 reel never ties the company to an
offering (HD-17), and this pass's four filings add nothing (they are all post-1994 and none mentions a 1987
offering). The Stage-1 end therefore cannot be dated by the event that should define it. / **CONFIDENCE:** the
assertion is unusable as a fact.

**U-4 — UNCHANGED (2 stores at opening vs 4 units by year-end).** Still reconcilable only by this probe's
inference; the charter (HD-A1) does not touch store counts. / **CONFIDENCE:** Medium on four-by-1980; Low on
the June pair; the interval UNKNOWN.

**U-5 — UNCHANGED and reinforced.** The ~55,000 sq ft figure (HD-11) is the **Treasure Island rollback
footprint**, reported March 1980; the filings' own **store average of ~100,000 sq ft enclosed** at fiscal-1993
(HD-A11) is a 1993 fact and must not be back-dated onto the first stores. Two numbers, two decades, one
temptation.

**U-6 — NEW: "inception" is not "incorporation" and not "opening".** The registrant's own word for its start
is **"inception in 1978"** (HD-A3), used for Marcus and Blank; the charter's word is **"originally
incorporated"** (HD-A1); the trade print's word is **"founded"** (HD-10); the commemorative's words are
"founded … in 1978" plus "opened the first two … stores on June 22, 1979" (HD-22). / **WHY THEY DIFFER:** four
different verbs for one origin, and only one of them (the charter) is a legal instrument with a day. /
**BEST-SUPPORTED:** quote the verb, never paraphrase it — a dossier that writes "the company was founded in
1978" and then "opened in 1978" has smuggled the trading date into the entity date. / **CONFIDENCE:** High in
the warning.

**U-7 — NEW: money.** Langone's documented role in the held record is **outside director + paid adviser
($100,000/yr, HD-A6)**, which the folklore converts into "the banker who put up the founding money"; the
1994 ownership percentages (HD-A7) are post-split, post-listing. **No held document carries the 1978–79
capital table at all**, so §K's founding-capital question is UNKNOWN with a named remedy (the 1987 S-1/424B,
paper). / **CONFIDENCE:** High that the gap exists.

**U-8 — NEW, and the trap (3) demonstration made concrete: the same fiscal-1993 figure differs between two
consecutive 10-Ks** — long-term debt **841,992 → 874,048** (`$000`) and the debt-to-equity ratio **29.9 % →
31.1 %**, with equity and assets identical (**HD-A10**). / **WHY THEY DIFFER:** reclassification between the
fiscal-1994 filing and the fiscal-1995 filing (the filings do not say which line moved or why; the FY1995
row is labelled "Long-term debt, excluding…" in its balance sheet at l.3473, the FY1994 shell at l.2203
reads "Long-term debt," — a one-line difference in the balance-sheet caption is the visible trace). /
**EVIDENCE WEIGHT:** both are Tier-1, same registrant, same fiscal year. / **BEST-SUPPORTED INTERPRETATION:**
for any figure a dossier takes from a 1990s Home Depot filing, the **filing of that fiscal year wins**, and
the later repetition must be labelled **RESTATED**; where only the later filing exists for a year, the figure
is second-hand even though the document is primary. / **RESIDUAL:** the cause of the +32,056 is not stated in
the held bytes. / **CONFIDENCE:** High on the divergence (both strings quoted from disk); UNKNOWN on cause.

STATUS: WRITTEN 2026-10-06

## R6. Two live tool defects this pass walked into, with their exact reproduction (no code was touched)

Both blocked the scripted route and both are one-line owner fixes. Recorded here rather than in a tool file
because this probe owns one path only.

**D1 — `sec_intake.py` cannot complete `index` or `auto` for this company.** Reproduced twice
(2026-10-06, this pass and — by artefact evidence — the 2026-10-06 fleet retry before me):
```
python tools/sec_intake.py auto "Home Depot, Inc." --company-dir founders_playbook/01_companies/company_025_homedepot --from 1994-01-01 --to 1996-12-31 --max-docs 20
identity: 'Home Depot, Inc.' resolved to CIK 354950 (HOME DEPOT, INC.) by name-exact
walk: 2 slices (2 fetched, 0 failed), 3077 filing rows, date perimeter 1994-04-19 -> 2026-09-22
AttributeError: 'int' object has no attribute 'strip'   [tools/sec_intake.py:1275 → :445]
```
Cause: `write_index()`'s back-compat guard reads the **legacy** `sources/_index/submissions.json` and does
`(json.load(open(legacy)).get("cik") or "").strip()` — and the Sep-25 legacy copy stores **`"cik": 354950`**
as an **int** (measured: `keys ['cik','company','ticker','built','count','filings']`, `cik repr 354950`,
`built 2026-09-25T19:43:31Z`), so `.strip()` raises `AttributeError`, which the surrounding
`except (ValueError, OSError)` does not catch. **Effect:** the walk succeeds, the CIK-keyed artefacts are
written, and the command dies before planning or fetching anything — which is precisely why
`sources/sec/_RUN.json` does not exist, why `sources/sec/_MANIFEST.csv` is still header-only, and why the
fleet logged "0 documents stored" for a registrant whose EDGAR record is 3,077 rows deep. **Remedy:** coerce
with `str(...)` and catch `AttributeError`. **Scope:** every company whose legacy `submissions.json` predates
the CIK-keyed rewrite — i.e. the Sep-25/26 intake cohort, not just this one.
**Disclosure (rule 2, add-only):** the crashed run **re-wrote** this company's own canonical CIK-keyed
artefacts (`_INDEX_CIK0000354950.md`, `submissions_CIK0000354950.csv/.json`, `_registrant_CIK0000354950.json`;
mtimes moved 17:14 → 17:24) with content that reproduces them — `csv_sha1` is **unchanged**
(`fa7e61ed887073c4d349aa11a43231aa8487cc11`) and the row count is still 3,077, so the enumeration is
**idempotent** across the Sep-30 quarantine run, the Oct-6 fleet retry and this pass. The legacy
`submissions.csv` / `_INDEX.md` / `submissions.json` were **not** modified (mtimes still Sep 26 01:13) and
nothing was deleted. The only field the re-write dropped is the final `meta["paths"]` / `legacy_copy_written`
bookkeeping, which the crash prevented — a later successful `auto` restores it.

**D2 — `grab` without `--file` is dead for every company.** Reproduced on two accessions:
```
python tools/sec_intake.py grab "Home Depot, Inc." --company-dir … --accession 0000354950-94-000001
ValueError: too many values to unpack (expected 2)   [tools/sec_intake.py:1324]
```
Cause: `main()` unpacks `listing, lnote = doc_listing(...)` while `doc_listing` (l.490) documents and returns
**three** values `(items, note, form)` — the RD-130 enumeration rework left an arity mismatch. **Effect:** no
agent or orchestrator can enumerate an accession's documents through the tool, so the pre-2001 nameless-
directory problem RD-130 describes has no working front door, and the "which file is the real one" question
is unanswerable by script. **Remedy:** unpack three.

**What worked instead, and should become the sanctioned paper-era route:** `grab --accession <acc> --file
<accession>.txt`. It bypasses `write_index` entirely, and it is exactly what the new index recommends
("72 rows carry no `primaryDocument` (paper-era shells -- fetchable as `<accession>.txt`)"). All four held
documents arrived that way, HTTP 200, `url_form: padded-cik/nodash-dir`, with sidecars. **Caveat the merge
must see:** those four files are on disk but are **not** in `_MANIFEST.csv` (only `auto` writes the manifest),
so the shelf reads as empty to any tool that counts the manifest. Enumerate `sources/sec/*.meta.json` (4
rows: 162,266 + 216,512 + 60,533 + 236,747 B = **676,058 B**, **84,014 words**) or fix D1 and re-run.

STATUS: WRITTEN 2026-10-06

## R7. `## Untried` — this pass only. None of these is a null.

Ordered by expected Tier-1 yield per call.

1. **68 more paper-era `.txt` shells, one call each, no fix required** (72 rows without `primaryDocument`
   minus the 4 held). The named prizes for Stage 1/2: FY1996 10-K `0000354950-96-000002.txt`, FY1997 10-K
   `0000950144-97-004508.txt`, FY1998 10-K `0000950144-98-005045.txt`, FY1999 10-K405
   `0000950144-99-004643.txt`, the 1997 **S-4** `0000950144-97-000625` + S-4/A (Builders Square — a merger
   registration statement is the one EDGAR document class that routinely narrates the acquirer's own history),
   the 1996 **8-A12B** `0000950144-96-006549` and **424B4** `0000950144-96-006629`, the 1995 **S-8**
   `0000354950-95-000003` (option/stock-plan history often recites early grants), and the 1997–98 **SC 13G**
   rows naming Marcus/Blank/Langone.
2. **The fix of D1**, which turns item 1 from 68 hand-run commands into one `auto --max-docs 30` pass over
   1994–2000 — and writes the `_RUN.json` and `_MANIFEST.csv` this company still lacks.
3. **The FY1984–FY1988 half of the "Ten Year Selected Financial and Operating Highlights" table** — proved to
   exist by its own title (HD-A9) and absent from the EDGAR rendition. Carriers: the **printed FY1994 annual
   report** (and FY1988–FY1993 reports) via family (d), or possibly a separate document inside accession
   0000354950-94-000001 that only D2's fix can enumerate. This is the shortest path to **audited founding-
   decade numbers** anywhere in the corpus.
4. **38 of 41 enumerated periodical reels unmined** (identifiers in EXTRACT §4): DSN 1981–1986, 1988–1990;
   Chain Store Age all 20; National Home Center News all 10 (the title most likely to treat Home Depot as its
   own subject). Plus the zero-network patterns on the 2.2 MB already held that nobody has tried:
   `Treasure Island` (3 hits found by chance in the 1980 reel — worth reading around), Atlanta/GA place
   names, advertised prices, advertiser-name lists, `home center` near `Atlanta`.
5. **Registrars — now one sharp question instead of three vague ones:** the **Delaware** Division of
   Corporations charter file for `M. B. Associates Incorporated`, incorporated 29 June 1978, and its
   amendment/renaming to `The Home Depot, Inc.` (the rename date is the missing bridge between HD-A1 and the
   1979 trading evidence). Georgia SoS and the asserted **Colorado/Denver** layer are now **lower** prior:
   nothing in the registrant's own record mentions either. Fulton County (GA) lease indices for the 1979
   sites and **Treasure Island's** own creditor/bankruptcy docket (the chain described as "financially
   troubled" in March 1980 was the landlord) remain untried and remain the only third-party dating route.
6. **Family (b) and (e) as whole families**: CDX prefix sweeps and 1996–2001 `/about`–`/history` sub-paths;
   name-indexed auction/museum catalogues (Swann, Heritage, Potter & Moore, Reiter's), Georgia Historical
   Society accessions (it sponsored the physical marker), Atlanta History Center, AJC morgue for 1979
   clipping files, and Home Depot's own corporate archive as a request route. All UNTRIED this pass
   (0 web calls, harvesters forbidden).
7. **The six 503'd fleet-mine identifiers** in A4 (`Wpo8v92NgjoC`, `KQUKFmw0BkAC`, `ZbBkDAAAQBAJ`,
   `vYlFDAAAQBAJ`, `k7HWONIo88YC`, `98ktCgAAQBAJ`) — a retry, not a null; and `homedepot`'s **empty entity
   vocabulary** in the harvester's `queries.json` (HD-C3), an owner file this probe may not edit.
8. **The unread date-lists still unread:** `THD Timeline.pdf` (HD-23) and Roush's 1999 *Inside Home Depot*
   (HD-20, HTTP 401 lending-gated).

STATUS: WRITTEN 2026-10-06

## R8. FETCH REQUESTs (orchestrator runs the script; a probe does not fetch)

```
FETCH REQUEST — sec_intake (needs D1 fixed for lines 3-5; line 2 works today via --file)
 1. enumerate then grab, acc 0000354950-94-000001 — is there a separate EX-13/annual-report document beyond
    the concatenated shell? (blocked by D2; the shell holds 7 documents and its ten-year table stops at 1989)
 2. grab --accession 0000354950-96-000002 --file 0000354950-96-000002.txt   (FY1996 10-K, fiscal 1995 data)
    grab --accession 0000950144-97-004508 --file 0000950144-97-004508.txt   (FY1997 10-K)
    grab --accession 0000950144-99-004643 --file 0000950144-99-004643.txt   (FY1999 10-K405)
 3. auto --from 1994-01-01 --to 2000-12-31 --max-docs 40   (paper-era sweep; writes _RUN.json + _MANIFEST)
 4. grab --accession 0000950144-97-000625 --file 0000950144-97-000625.txt   (S-4, Builders Square — acquirer's
    own history narrative is the likeliest EDGAR carrier for a founding-decade store/sales sequence)
 5. facts --from 1994-01-01 --to 2002-12-31  (expect EMPTY: no XBRL before 2002; report as measured, not null)
FETCH REQUEST — periodical_harvest / corporate_print (forbidden on this pass)
 6. --source-family corporate_print, facet-free, for "Home Depot" annual reports FY1988-FY1993 (HathiTrust +
    IA); target the FY1994 report's Ten Year table columns fiscal 1984-1988 (HD-A9).
 7. retry the six 503'd A4 identifiers after adding a homedepot entity-vocabulary block (HD-C3).
FETCH REQUEST — paper, no script exists
 8. 1987 registration statement / prospectus and FY1987-FY1990 10-Ks, SEC Public Reference Room / NANA.
    This is the only CONTEMPORANEOUS class of document for the founding decade's numbers and for the listing
    boundary (U-3). Until it is held, Stage 1's end date and §K stay UNKNOWN.
 9. Delaware Division of Corporations: charter file, M. B. Associates Incorporated, incorporated 1978-06-29,
    plus the amendment changing the name to The Home Depot, Inc. (independent third-party twin of HD-A1).
```

## R9. What I refused to claim, and why

- **The first store(s), their date, and their count.** `first two stores` and `opened its first` measure **0**
  in the held filings; DSN 1980 says four units by 1979 but never mentions an opening; only GHS-2016 gives a
  day. A day needs a carrier; the day is 2016 folklore, so the opening stays **UNKNOWN** and HD-22's
  "June 22, 1979" is not promoted.
- **The napkin / the single visionary's epiphany / the same-day-firing story.** `napkin` 0, `Handy Dan` 0 in
  held bytes; the only in-window founder descriptor is four words — "former discounter" (HD-10). Recorded as
  **FOUNDER CLAIM (retrospective)** material for the dossier's preamble, never as fact, and the "idea
  originated in 1978 with two men and a banker" formulation is now demonstrably a **1994** formulation
  (HD-A4), not a 1978–80 one.
- **"1979 is the incorporation year."** Refuted by the registrant's own charter (HD-A1) and by the seal article
  "Incorporated 1978 Delaware" (HD-A8). Not claimed even as an alternative reading.
- **The merger of two other home-improvement businesses.** Real or not, **no carrier in family (a) or (c) on
  disk**. Recorded as the U-1 residual with a named remedy (R8-8, R8-9); not asserted.
- **Founding capital, the 1978–79 cap table, the IPO price/proceeds, and the founders' original stakes.** The
  1994 ownership percentages are post-listing, post-split and 16 years late (HD-A7); the Invemed contract
  proves an *ongoing* paid relationship, not the 1978 money (U-7). §K stays UNKNOWN.
- **Any founding-decade store count or sales figure.** Family (a) yields nothing before **fiscal 1989**
  (HD-A9), and the FY1988 anchor survives only inside a growth-rate aside; I did not let a nice number in for
  1979–1986.
- **A third counting of family (d) or (e) toward the tier.** Both are UNTRIED this pass and are written as
  UNTRIED, not as nulls, notwithstanding the inherited 2026-09-25 searches.
- **The 1987 listing as the Stage-1 boundary.** Unattested in every held byte (U-3); the boundary is proposed
  at FY1988 for a documentary reason and labelled as such.

## R10. The route most likely to change this verdict

**One sentence:** *fetching the printed **FY1988–FY1993 annual reports** (family d — HathiTrust/bound runs,
R8-6), because family (a) has now **proved by its own title** that the FY1994 report contains a Ten-Year
Selected Financial and Operating Highlights table reaching **fiscal 1984** while the EDGAR rendition prints
only **fiscal 1989–1993** — so that one shelf is simultaneously the fastest path to audited founding-decade
numbers, the fastest path to a third counted family and a **T1-capable Stage 1**, and the only place the
1981–1987 store-count ramp exists in a company-written form.*

Runner-up, and cheaper: the D1/D2 one-liners plus `grab --file <accession>.txt` over the remaining **68**
paper-era shells (R7-1, R7-2) — that cannot raise the family count (same lineage) but it converts several
"UNANSWERED" rows in this file into carriers, and it is the fix that makes the intake state honest
(`_RUN.json`, a populated `_MANIFEST.csv`, a corrected `_FLEET_INTAKE.tsv` row 38).

STATUS: WRITTEN 2026-10-06

---

### Report block (this pass)

- **Path:** `founders_playbook/01_companies/company_025_homedepot/research/A_chronology_feasibility.md`
  (2026-09-25 volume preserved; RE-GRADE 2026-10-06 appended; word count in the gate sheet).
- **Bytes added to the archive:** `sources/sec/` 0 → **4 documents / 676,058 B / 84,014 words** (+4 sidecars).
  Nothing deleted, moved or renamed anywhere under `sources/`.
- **Records minted:** HD-A1…HD-A12, HD-C1…HD-C3 (15 new claim records); conflicts U-1 and U-2 re-graded,
  U-6/U-7/U-8 opened; three prior records superseded on their central point (HD-05's route failure, HD-19's
  "no in-window financials", HD-22's standing as the only dated founding carrier).
- **Per-stage tiers:** Stage 1 **T2 core** (was T3), Stage 2 **T2 core**, Stage 3 **T2 measured / T1
  reachable** (indicative, not this probe's stage). Families counted for Stage 1: **(a) + (c)**.
- **Five-family verdict:** (a) TRIED–ANSWERED · (b) UNTRIED (inherited: floor 1996-11-05) · (c)
  TRIED–ANSWERED (re-verified in held bytes) · (d) UNTRIED (with a proved-but-unheld target) · (e) UNTRIED.
- **Coverage note — what was NOT examined:** 68 of 72 paper-era shells; 38 of 41 periodical reels; all of
  HathiTrust/Google Books/bound library runs; all registrars and courts; auction/museum catalogues; the Wayback
  index (no re-run); the company's own PDF date-list; the 1999 Roush book; `harvest_mine`/`periodical_harvest`
  (forbidden by the brief). No `facts`/XBRL pass was run this time (expected empty pre-2002; named in R8-5).
- **Two owner bugs:** `sec_intake.py:445` int-`cik` crash (blocks `auto`/`index` for the Sep-25 intake cohort)
  and `sec_intake.py:1324` `grab` arity crash (blocks accession enumeration). Both reproduce; neither was
  patched by this probe.
- **Instruction-layer sweep owed:** `_FLEET_INTAKE.tsv` row 38 and `_IDENTITY_FIX.log` still assert a refusal
  that disk now contradicts (RD-124 r10).

