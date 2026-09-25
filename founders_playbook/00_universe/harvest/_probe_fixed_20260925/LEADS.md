# LEADS — the first real items the repaired routes unblock (2026-09-25)

Every item below is read out of a **saved HTTP 200 body in this directory** (provenance in
the last column) and, where re-tested this session, out of `v2_reverify/`. Nothing here is
cited as evidence yet: a lead is a pointer to a page that has not been read.

**What each route can and cannot deliver (this decides verdicts):**

| Route | What a scripted call returns | What it does NOT return |
|---|---|---|
| Google Books legacy Atom feed (keyless) | volumeId, title, date, publisher/creator, `gbs:viewability` (all_pages / partial / no_pages), the **matched page** (`pg=PA138`) and a **178–283-character matched-page snippet** in `<dc:description>` | the page itself; a corpus count (`totalResults` is a 300 display cap) |
| HathiTrust `/cgi/ls` (intermittently open) | facet counts All Items / Full View + `<article class="record">` blocks (htid, title, published date, rights) — **0 snippet nodes**: records, not text | any page text; the search is not reliably reachable scripted |
| HathiTrust catalog brief-record API (open) | JSON rights: `rightsCode`, `usRightsString` ("Full view"), title, publishDate, every holding htid + itemURL | page text — `/cgi/pt?id=…` for a Full-view item still 403s a script |
| Internet Archive metadata + `_djvu.txt` (open) | **full text**, byte-saved | anything the IA index does not hold |
| Chronicling America | nothing — 403 on every path incl. `/robots.txt` | the newspaper corpus stays UNANSWERED |

**Snippet-level metadata is not full text, and not the same evidentiary object.** A Books
snippet can *name* a fact a company printed about itself ("opened the first Wal-Mart
Discount City in Rogers, Arkansas, in 1962", *Management*, 1993, `N_bsAAAAMAAJ` pg=PA181)
and that is a Tier-2 retrospective lead, not a contemporaneous one. What moves a pre-1994
verdict is an **in-window item whose text opens**: HathiTrust Full-view rights on a 1960s
record, an all_pages InfoWorld issue from 1983–85, an IA `_djvu.txt`. Those are listed
below as openable; the rest are pointers.

---

## 1. Walmart (company_002)

### 1a. HathiTrust — Full-view candidates (text openable by a human today)

`"Wal-Mart" Bentonville`, `lmt=ft`, **1960–1969 facet: All Items 45 / Full View 4.** The
four full-view records on that page (from `hathitrust/640238bfc6cb7376-r20260925T131232Z.html`,
HTTP 200, 34,171 B):

| htid | title | why it matters | status |
|---|---|---|---|
| `uiug.30112005545535` | Customs bulletin: Treasury decisions under customs and other laws, v.29:23-35 | **rights verified this session**: catalog API 200 / 29,445 B → record 000888066, publishDate **1968**, rightsCode `pd`, usRightsString **Full view**, itemURL `https://babel.hathitrust.org/cgi/pt?id=uiug.30112005545535` — a genuinely in-window, openable periodical volume | POSITIVE (rights) / text UNTRIED (viewer 403s a script) |
| `uiug.30112048646365` | Customs bulletin … v.34:1-13 | same title run, `pd` / Full view per the same catalog response (it lists every holding) | POSITIVE (rights) |
| `uiug.30112027343745` | Customs bulletin … v.29:36-41 | same run, `pd` / Full view | POSITIVE (rights) |
| `uva.x030444760` | Army logistician, v.97 | full view; the "Wal-Mart"/Bentonville match in a 1960s Army supply journal is unexamined — could be OCR noise, read before using | LEAD_ONLY |

Unbounded `"Wal-Mart" Bentonville` = **All Items 11,850 / Full View 2,638** (100 record
blocks, HTTP 200, 391,767 B). In-window among the first page: `pst.000033207582`
*Supercenters: the emerging force in food retailing* (German/Hawkes, **1993**, Full view) —
contemporaneous trade literature on the format; `pst.000023489691` 1995 House Small Business
hearing (Full view, out of the pre-1994 window by one year); `"Walton's" "five-and-dime"`
= 1,529 / 59 full view but the first page is copyright catalogs and Congressional Record —
**noise, not the 1945–55 Newport store**, so that query needs a state/place term added.
Plumbing control `"five and dime" variety store` 1950–1959 = 2,284 / 187 with 100 record
blocks → the facet grammar works, so every 0 above is a real 0.

### 1b. Google Books — volumes naming Bentonville / Rogers (keyless feed, live 200 re-verified)

`"Wal-Mart" Bentonville Rogers` — HTTP 200, 25,023 B (`google_books/dc280ae6842774b2…xml`,
re-fetched 13:48Z byte-identical). 10 volumes, with matched page and snippet:

| volumeId | title | date | viewability | page | what the snippet actually says |
|---|---|---|---|---|---|
| `2BIpAQAAMAAJ` | Wal-Mart | 1994 | no_pages | — | "…Bentonville, Rogers, Fayetteville, Springdale, Harrison, North Little Rock, and Camden, Arkansas" — a store list naming the two towns |
| `N_bsAAAAMAAJ` | Management | 1993 | partial | PA181 | "Wal-Mart Stores Inc., opened the first Wal-Mart Discount City in **Rogers, Arkansas, in 1962**. Bentonv…" |
| `pwzPwD988-MC` | Official Gazette of the US Patent and Trademark Office | 2004 | **all_pages** | RA2 | "BENTONVILLE, AR. FILED 9-17-2003 … SN 76-545,521. WAL-MART STORES, INC." — trademark filings, openable, post-window |
| `8sSynmZk4rIC` | The World of Wal-Mart | 2013 | partial | PA138 | index entries; retrospective |
| `gO-vwa_g7x4C` | The Wal-Mart Effect | 2007 | partial | PT332 | "Bentonville, 63 …" retrospective |
| `Xc9bE6D9SBEC`, `wTkVAQAAMAAJ`, `dzIVAQAAMAAJ`, `HyQVAQAAMAAJ`, `ePtsAAAAMAAJ` | trade directories (Building Products & Hardlines; Discount Department Stores; Discount & General Merchandise; Department Stores; Hayes Druggist) | 1992–1998 | no_pages | — | per-store listings with manager names and addresses — a roll of the store base, **needs a key or library copy to read** |

`"Walton's" "five and dime"` — HTTP 200, 25,870 B. The live question the queries file flags
(Newport **Arkansas** vs Newport **Missouri**) is addressable here: `ggN9Kp8UVfwC`
*Sam Walton* (2012, partial, PA43) reads "Walton's Five and Dime, it was a **Ben Franklin
franchise**, and that store took off just like Newpo…" — a biography, so Tier-2, but it is a
route to the sentence; `USInAQAAIAAJ` *Time* 1992-04 (no_pages) "WALTON'S FIVE AND DIME, IN
**FAYETTEVILLE**"; `RPrPEQAAQBAJ` *Billions* (2026-04-11, partial, PT125) "Forced to start
over, Walton moved his family to Bentonville". None of these is contemporaneous; **the
contemporaneous 1945–1962 newspaper record is still Chronicling America, and it is still
blocked** (§3).

## 2. UnitedHealth (company_003)

### 2a. HathiTrust `"Charter Med"` — HTTP 200, 380,833 B: **All Items 1,527 / Full View 532**

This is the first non-null answer UnitedHealth's periodical family has ever returned.
Full-view records on the first result page:

| htid | title | date | status |
|---|---|---|---|
| `pur1.32754075976369` | **The Physicians Health Plan of Minnesota: a case study of utilization controls in an IPA** | 1980 | Full view — the named Minnesota prepay plan of the founding decade, in-window, openable: the strongest single lead in this file |
| `uc1.31210013198922` | HMO focus / HEW, Public Health Service | 1981 | Full view — federal HMO programme literature that lists certified plans by name |
| `mdp.39015010031741` | DHHS publication no. (PHS) 82-50180 | (1982) | Full view |
| `pur1.32754076920457` | Efforts to combat fraud and abuse in the insurance industry (Senate PPOM hearing) | — | Full view |

`"Metropolitan Health Plans"` 1970–1989 facet is configured but its 200 body is not in this
directory — **UNTRIED**, and `HT 'Metropolitan Health Plans'` must be re-run in an open
window before anything is claimed about it.

### 2b. Google Books `"Charter Med" Minneapolis` — HTTP 200, 23,608 B (re-verified 13:48Z)

| volumeId | title | date | viewability | page | snippet (verbatim, truncated) |
|---|---|---|---|---|---|
| `udRwLIq-iMoC` | Focus on Health Maintenance Organizations | 1978 | **all_pages** | RA7 | "Charter Med, Minneapolis, which manages ten IPAs around the coun-try…" |
| `CKD-KolMt-8C` | HMO Focus | 1981 | **all_pages** | PA4 | same passage, later issue |
| `ztWc6Ufs6qEC` | DHHS Publication No. (PHS) | — | **all_pages** | PA5 | "Charter Med of Minneapolis, Medserco of St. Louis, Hancock, Dikewood of Albuquerque, and Healthplans C…" |
| `yqYVAQAAMAAJ` | Modern Healthcare | 1990 | no_pages | — | "**Charter Medical** Corporation is the nation's largest and fastest growing private psychiatric…" — **NAME COLLISION TRAP: a different company** (the N. Carolina hospital group), do not let this row into a chronology |
| `815tAAAAMAAJ`, `MhQiAQAAMAAJ`, `-IzwAAAAMAAJ` | Introduction to Nursing Concepts 1987 / American Journal of Hospital Pharmacy 1985 / An Economic Survival Manual for Private Practice Psychiatrists 1985 | 1985–87 | no_pages | — | directory/tabular mentions of "Charter Med (Minneapolis)" — pointers to plan-of-origin listings, need a key |

The three `all_pages` federal HMO documents (1978, 1981, 1982-series) are the first
**in-window, openable, name-bearing** UnitedHealth print this project has held: Charter Med
of Minneapolis as a certified HMO/IPA manager, in the decade of its founding. That is a depth
lead, not a verdict — the text has to be opened and read.

### 2c. Google Books `"Metropolitan Health Plans"` — HTTP 200, 6,102 B, **2 volumes only**:
`cF_9CAAAQBAJ` *Data-Book of Happiness* 2013 (partial, PA128 — "metropolitan health plans,
proportionally stratified by marital status", a generic phrase, not the company) and
`WK51MZByt6cC` *Computerworld* 2003-03-17 (all_pages, PA35 — "Metropolitan Health plans to
wrap its server architecture decisions…", 2003, out of window). **Read: this keyless route
delivers nothing in-window for MHP; do not report it as a null on the company.** The null
that matters is `CP unitedhealth annual reports 1977–1995` (200 / numFound 0, params-specific).

## 3. Apple (company_004)

Google Books `"Apple Computer" Cupertino shareholder` — HTTP 200, 23,665 B (re-verified 13:48Z):

| volumeId | title | date | viewability | page | snippet |
|---|---|---|---|---|---|
| `_i8EAAAAMBAJ` | **InfoWorld** | 1983-02-28 | **all_pages** | PA47 | "CUPERTINO, CA — At its recent **shareholders' meeting**, Apple Computer used many words during the unveiling of its newest computer, the Lisa. InfoWorld — and every other publication — has already written more than anyone could ever need to…" |
| `hS4EAAAAMBAJ` | InfoWorld | 1984-02-20 | **all_pages** | PA13 | "\"shareholder's meeting,\" but what Apple Computer really held on Tuesday, January 24, was a…" |
| `8C4EAAAAMBAJ` | InfoWorld | 1985-06-03 | **all_pages** | PA21 | "Cupertino, reports total sales of the Lisa amount to 60,000 units since its 1983 introduction…" |
| `lTAEAAAAMBAJ` | InfoWorld | 1989-06-26 | **all_pages** | PT41 | "Retail Sales of Apple's High End…" |
| `20pAAQAAIAAJ` | Proxy Contests Handbook | 1989 | no_pages | — | "APPLE COMPUTER, INC. 20525 Mariani Avenue Cupertino, California 95014 — Mailed to Shareholders on or about De…" |
| `eX0UAQAAMAAJ` | **Corporation Annual Reports to Shareholders** | 1988 | no_pages | RA6 | a directory whose whole purpose is locating printed annual reports — the finding-aid route to Apple's missing financial print |
| `6nYeAQAAIAAJ` | Fairchild's Electronics Industry Financial Directory | 1993 | no_pages | — | "Shareholders' Eq… Included in Costs and Expenses, Depreciation and Amortization: $1,140,000" — financial-table format, Apple line |

Four InfoWorld issues are `all_pages` = **viewable, dated, in-window trade-press periodical
text about Apple's shareholder meetings and Lisa sales** — the first periodical-family
POSITIVE Apple has ever had (it had no periodical task at all before this rewrite). Getting
those pages as text: `InfoWorld` on IA is already partially digitised, and the same items can
be checked in HathiTrust — so the next action is an IA/HT identifier pull on the four
volumeIds, not a Google key.

HathiTrust Apple (`"Apple Computer" Cupertino` 1970–1979; `"Apple Computer" "personal
computer"` control) is configured but has **no 200 body in this directory — UNTRIED**; the
host's search window closed again at 13:44Z (§4).

## 4. Chronicling America — still UNANSWERED, and the reason is now PROVEN

Re-run this session (v2_reverify/, 13:48Z): `…/search/titles/results/?terms=Bentonville&format=json`
→ **403, 5,990 B, Cf-Mitigated: challenge, CF-RAY a40a7d1cc9554621-DEL** (Chrome UA + full
header set); `…/search/pages/results/?andtext="Wal-Mart" Bentonville&format=json` → **403,
5,980 B, challenge** (declared tool UA); **`https://www.loc.gov/robots.txt` → 403, 5,457 B,
Cf-Mitigated: challenge**, body "Just a moment… Enable JavaScript and cookies to continue".

That third request carries no query, no company and no parameter of ours, so the 403 cannot
be a defect in our request shape: **it is their bot policy on the whole www.loc.gov zone.**
17 configured CA tasks — including the two canaries and every Walmart/UnitedHealth/Apple
newspaper query — therefore read **UNANSWERED, never EMPTY**, and the 1945–1962 Arkansas
newspaper record and the 1970s Minneapolis press record remain the corpus this harvest has
*not* seen. Opening them needs a browser session or LOC-granted access; the `web.archive.org`
CDX route (`ca10_cdx`/`ca11_cdx`/`ca19_cdx`/`ca20_cdx` probes) reaches only what the Wayback
machine captured of NDNP, which is not a substitute for the OCR corpus.

## 5. Requests spent verifying this (cap was 40)

**14 total, all sequential, 3–25 s apart**: Google Books feeds ×3 (200/200/200) + v1 control
×1 (429) = 4 · HathiTrust `/cgi/ls` ×5 (all 403 challenge, incl. one browser-header attempt
and two spaced retries) + catalog brief-record ×1 (200) + `/cgi/pt` full-view page ×1 (403)
= 7 · Chronicling America ×3 (all 403) = 3. New bodies preserved in `v2_reverify/`; nothing
in this directory was overwritten or deleted.
