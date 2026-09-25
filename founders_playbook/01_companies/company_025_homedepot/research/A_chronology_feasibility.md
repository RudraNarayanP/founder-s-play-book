# A_chronology_feasibility.md

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

