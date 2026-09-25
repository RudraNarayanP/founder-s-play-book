# A_chronology_feasibility.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:07:23Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

**TIER VERDICT: T3 (register) by the literal rule of 00_METHOD_AND_STYLE.md 15.2, with a named
upgrade path to T2 -- and the tier understates this corpus, so the qualifier is part of the verdict.**

Families returning **in-window Tier-1 text**, counted as the table counts them:

| family | verdict | in-window Tier-1 text? |
|---|---|---|
| (a) filings | TIER1_CANDIDATE | **yes** -- 6 accessions, 376k html-stripped words, day-level inception, three named co-founders, audited 1993-97 money series, signed exhibits |
| (b) web archives | **UNANSWERED** | no -- six CDX requests, HTTP 503/504, zero bodies, so no 14-digit timestamp exists |
| (c) periodical corpora | **LEAD_ONLY** | no -- 17 scripted tasks, 145 candidate rows, but no article body read; the two routes that hold 1995-1999 US trade press (HathiTrust, Chronicling America) returned status 0 and 403 |
| (d) digitised corporate print | **NULL in-window, explicitly queried** | no -- numFound 0 for report-scoped shapes; the one item holds FY2005-2026 |
| (e) documentary | **UNTRIED** | no route implemented; see `## Family e documentary` |

**1 of 5 -> T3: short narrative + registers, 8k words/stage cap, 3-4 agent runs, and section K /
section N / section U still mandatory.** "We cannot know" is a deliverable here: the founding
*documents* of 1993 (California certificate, Series A purchase agreement) are outside every family
this probe could reach, so origin stays a founder claim plus an audited header, not a signed
article.

But record the shape honestly, because it is not the usual T3 (thin corpus): this is **one deep
family and four families that were blocked, not empty**. Nvidia was founded in 1993 and registered in
1998, so it sits just past the EDGAR full-text-era boundary the method file warns about -- unlike
pre-1994 companies, everything missing here is missing for **access reasons** (egress blocks, a
tool bug, no budget left), not because the record does not exist. The 1999 prospectus did carry the
founders' own account of 1993-1995 in Tier-1 text, exactly as the brief predicted -- as a founder
claim in its own filing, one lineage, which is why families (c) and (e) still decide the tier.
The strongest non-narrative material found is *inside* family (a): the signed Ex-3.1 Delaware
certificate (Feb 1998), the counterparty-signed Second Amended and Restated Investors' Rights
Agreement of August 19, 1997 (Ex-4.3, "by and among NVIDIA CORPORATION, a California corporation"),
and the Amahl sublease of February 2, 1995 as twice amended -- third-party dates, no company prose.

**T2 upgrade condition (cheap, two probes):** a browser-egress Wayback CDX answer (1 request) AND one
in-window periodical body read (HathiTrust in an open window, or the Google Books
`all_pages` Maximum PC 2000-03/04 items) => 2 families with in-window Tier-1 text => T2, 6-9 runs.

**Every tier deliverable still owed by this company:** `sources.csv`, `conflicts.csv`,
`data_gaps.csv`, and this UNTRIED list.


## Family a filings

STATUS: WRITTEN — verdict **TIER1_CANDIDATE**

Route: `tools/sec_intake.py` (CIK 1045810, NVIDIA CORP). Index rebuilt to full history:
**2,487 filings enumerated**, earliest in window **1998-03-06**, **69 filings filed
1993-01-01..2001-12-31**. `sources/_index/submissions.csv` is the coverage record.

**Hard coverage boundary seen, not assumed:** the earliest Nvidia accession on EDGAR is
**S-1 filed 1998-03-06 (0001012870-98-000618**, File No. 333-47495 per the FY1999 10-K405).
Nothing is filed for 1993-1997, so every 1993-1997 date below is a **retrospective statement
inside a 1998-1999 document** — Tier-1 text, but one lineage (the company, its underwriters,
and KPMG as auditor of the incorporated statements).

Documents on disk (all under `sources/sec/`, sidecars `.meta.json`, rows in `_MANIFEST.csv`;
pre-2001 accessions have no `primaryDocument`, so the complete-submission `.txt` was grabbed):

| doc | filed | bytes | words (html-stripped) |
|---|---|---|---|
| 0001012870-98-000618.txt (S-1) | 1998-03-06 | 856,608 | 122,698 |
| 0001012870-98-003234.txt (S-1/A) | 1998-12-23 | 682,998 | 95,502 |
| 0001012870-99-000100.txt (S-1/A) | 1999-01-13 | 425,132 | 57,257 |
| 0001012870-99-000192.txt (424B4 IPO prospectus) | 1999-01-22 | 394,333 | 53,525 |
| 0000929624-99-000772.txt (10-K405, FY to 1999-01-31) | 1999-04-29 | 214,347 | 27,626 |
| 0001012870-00-001346.txt (10-K405, FY to 2000-01-30) | 2000-03-13 | 199,535 | 25,182 |

`facts` route: `sources/financials/xbrl_early_series.csv` written with **0 rows** — a documented
null (us-gaap companyfacts carry no Nvidia value with `end` in 1993-2001).

### Tier-1 text actually read this session

- **Inception, exact:** "the period from inception (**April 5, 1993**) to December 31, 1993 ...
  derived from audited financial statements ... audited by KPMG Peat Marwick LLP" (424B4,
  Summary Financial Data note; same header in the 1998-03-06 S-1). Founding brief's "1993"
  is therefore PROVEN to day-level, but through the company's own registration statement.
- **Incorporation:** "NVIDIA was incorporated in California in April 1993 and reincorporated in
  Delaware in April 1998" (424B4). 1998-03-06 S-1 wording: "incorporated in California in April
  1993 and **intends to reincorporate** in Delaware prior to the closing of this offering" —
  version difference, not conflict.
- **Founders (three, named, identical formula in all four registration docs):** "Jen-Hsun Huang
  co-founded the Company in April 1993 and has served as President, Chief Executive Officer and a
  member of the Board ... since its inception"; "Chris A. Malachowsky co-founded the Company in
  April 1993 and has been Vice President, Engineering ... since that time"; "Curtis R. Priem
  co-founded the Company in April 1993 and has been Chief Technical Officer ... since that time".
  Pre-founding employment also stated: Huang, LSI Logic 1985-1993 (AMD 1983-1985); Malachowsky,
  Sun Microsystems 1987-April 1993 (HP 1980-1986); Priem, Sun 1986-January 1993, GenRad 1984-1986.
  **Fortune's "Founder is CEO" flag is corroborated for Huang by Tier-1 text** (co-founder + CEO
  in the same sentence) — but from the same single lineage.
- **Development stage / first product:** "Since its inception in April 1993 through the end of
  1994, NVIDIA was in the development stage and was primarily engaged in product development and
  product testing. The Company introduced its first product, the **NV1, in May 1995**" (both S-1
  and 424B4). NV1 was targeted to the game-console market; "By the end of 1996, the PC industry
  had broadly adopted Microsoft's Direct3D and Silicon Graphics Inc.'s ... OpenGL 3D APIs. As a
  result, the Company experienced a significant reduction in revenue from sales of the NV1 and
  stopped selling the NV1 in the first quarter [1997]".
- **Second/third generation products:** "the RIVA 128, RIVA128ZX and RIVA TNT graphics processors,
  which the Company began shipping commercially in **August 1997, March 1998 and July 1998**"
  (S-1/A 1998-12-23, S-1/A 1999-01-13, 424B4 — three-generation agreement).
- **Money series (424B4/S-1 selected data, $000):** revenue 1993 `-0-`, 1994 `-0-`, 1995 `1,182`,
  1996 `3,912`, 1997 `29,071`, 9mo-to-1997-09-28 `5,537`, 9mo-to-1998-10-25 `92,700`; net loss
  1993 `(484)`, 1994 `(1,361)`, 1995 `(6,377)`, 1996 `(3,077)`, 1997 `(2,691)`; total assets
  1993 `1,786`, 1994 `5,450`, 1995 `6,793`; accumulated deficit "$14.0 million" at 1997-12-31
  (S-1) vs "$17.1 million" at 1998-10-25 (424B4). FY to 1999-01-31 total revenue `158,237`;
  FY to 2000-01-28(?) total revenue `374,505` (10-K405 filed 2000-03-13).
- **Capital line, dated to the year:** "In 1993, the Company sold 4,303,000 shares of Series A
  preferred stock at $0.50 per share, net of $22,000 of issuance costs. In 1994, ... 2,390,831
  shares of Series B ... at $1.80 per share, net of $57,000 ... In 1995, ... 416,667 shares of
  Series B" (identical in the 1998 S-1, both S-1/As, 424B4 and the 1999-04-29 10-K405 notes).
  Later round: "On July 22, 1998 and August 14, 1998, we sold Convertible Subordinated Notes to
  three investors for an aggregate purchase price of $11.0 million. On January 15, 1999, the
  Notes were automatically converted into an aggregate of 1,571,429 shares" (10-K405 FY1999).
- **Governance as a proxy for the 1993 round:** "Tench Coxe has been a director ... since June
  1993" (Sutter Hill Ventures), "Mark A. Stevens has served as a director ... since June 1993"
  (Sequoia Capital), "Harvey C. Jones, Jr. ... since November 1993" — i.e. outside VC board
  seats by June 1993, weeks after incorporation, in the company's own filing.
- **Headcount series:** "As of December 31, 1997, the Company had 92 employees as compared to 42
  employees as of December 31, 1996" (1998 S-1); "As of October 25, 1998, the Company had 184
  employees as compared to 71 employees as of September 28, 1997" (S-1/A + 424B4); "117 full-time
  employees engaged in research and development" (10-K405 FY1999); "214 full-time employees engaged
  in research and development as of January 30, 2000, compared to 117 ... as of January 31, 1999"
  (10-K405 filed 2000-03-13).
- **Customer concentration (independent-ish market validation, filed):** "Sales to STB accounted
  for 63% and sales to Diamond accounted for 31% of our total revenue for the year ended December
  31, 1997. Sales to STB accounted for 35%, ... Diamond 27%, ... Creative 13% and ... Intel 12%
  ... for the year ended January 31, 1999."
- **IPO date, filed:** "We commenced our initial public offering on **January 21, 1999** pursuant
  to a Registration Statement on Form S-1 (File No. 333-47495). The managing underwriters ...
  Morgan Stanley & Co., Hambrecht & Quist and Prudential Securities" (10-K405 filed 2000-03-13);
  424B4 filed 1999-01-22; price range "$7.00 AND $9.00" in the 1998-12-23 and 1999-01-13 S-1/As,
  blank ("BETWEEN $ AND $") in the 1998-03-06 S-1.
- **Address trail:** "1226 Tiros Way, Sunnyvale, California 94086" (1998-03-06 S-1) → "3535 Monroe
  Street, Santa Clara, California 95051" (424B4) — Tier-1 relocation marker between drafts.
- **Award-count claim inflation (useful for the founder-claim audit):** "over 40 awards from
  recognized industry publications" (1998-03-06 S-1) → "over 180 awards" (424B4).
- **Litigation in the validation window:** S3 patent-infringement suit over "RIVA 128, 128ZX and
  TNT graphics processors", three US patents, sought treble damages and an injunction
  (10-K405 filed 2000-03-13).

### Two `sec_intake.py` defects hit on this run (not corpus nulls — tool facts)

1. `submissions_index()` builds archive-slice URLs as
   `https://www.sec.gov/Archives/edgar/data/<cik>/CIK...-submissions-001.json` → **HTTP 404**,
   recorded in `_INDEX.md` as an UNANSWERED slice. The same file returns **HTTP 200** at
   `https://data.sec.gov/submissions/<name>`. Uncorrected, `index` silently caps at the 1,000
   most recent filings (NVDA: earliest 2020-09-03) and `auto --from 1993 --to 2001` would
   download **zero** documents for any company with >1,000 filings. Worked around this run by
   re-running the script's own `http_get/_as_records/write_index/grab` functions with the correct
   host; no shared file edited.
2. `grab()` is **dead on arrival**: `ERROR_MARKERS` mixes `str` and `bytes` entries, so
   `if marker in raw` with `raw` bytes raises `TypeError: a bytes-like object is required, not
   'str'` on every document (three tries each), returning status "UNANSWERED". Patched only in
   memory (`ERROR_MARKERS` re-encoded to bytes) for this run. This explains empty `sources/sec/`
   trees on other companies and should be fixed before the next wave.
3. Reading oddity to resolve in Stage 1, not a claim: the 424B4 selected-data table carries a
   "**one month ended January 26, 1997**" column next to stated December-31 fiscal years
   1993-1997 and a fiscal-year change "effective January 31, 1998"; the text I read does not
   explain the 1-month column.

## Family b web

STATUS: **UNANSWERED** -- not a null, and not evidence of absence.

`web.archive.org/cdx/search/cdx` was asked for the earliest `nvidia.com` captures in three query
shapes over two rounds, once through the scripted client and once through the fetch tool:
(1) `?url=nvidia.com&fl=timestamp,original,statuscode,mimetype&filter=statuscode:200&limit=6`;
(2) the same with no status filter and `limit=4`; (3) `?url=nvidia.com/&...&to=1998&limit=8`.
Answers received: HTTP **503**, **503 Service Temporarily Unavailable**, **503** in round one
(~19:16-19:17 UTC), then **503**, **504 Gateway Time-out** in the retry round (19:19 UTC), then
**503** through the second egress (19:20 UTC). Six requests, zero bodies.

Consequence, stated as the rule requires: **no 14-digit timestamp was returned, so no capture date
may be written for nvidia.com at any tier.** Nothing was saved under `sources/wayback/` because the
transport raised before any body arrived (there is no negative artifact to keep); the six lines
above are the whole record of the attempts, and 3 web-budget events were spent, as briefed.

Why this family cannot settle this company even once it answers: a Wayback capture of nvidia.com
begins around 1996-97 at the earliest, so it can corroborate the **product** era (NV1/RIVA naming,
the Sunnyvale-to-Santa Clara address, the self-description the company put on its own site) and
**cannot** reach 1993-1995. Its real value here is an independently dated snapshot of the company's
own origin text, not the founding date.

Re-run cost to settle it: one CDX request from a browser egress
(`fl=timestamp&filter=statuscode:200&limit=5&collapse=digest`), then one capture fetch.


## Family c periodicals

STATUS: **LEAD_ONLY** -- family queried live, but no in-window Tier-1 text read yet.

Scripted with `tools/periodical_harvest.py` (the brief names this as Nvidia's independent-
corroboration family). Configs are mine and stay in this dossier's folder
(`research/_harvest_queries_nvidia*.json`); the shared `tools/queries.json` held **zero** Nvidia
tasks before this probe (its 49 tasks are walmart 26 / unitedhealth 15 / apple 8). Three passes,
17 tasks, 20 network requests, response cache OFF. Evidence and index:
`sources/harvest/<family>/<sha1>.*` + `.meta.json` sidecars, `sources/harvest/candidates.csv`
(**145 rows**), `_MANIFEST.md` (17 bodies).

| route | HTTP | rows | what came back |
|---|---|---|---|
| `google_books` legacy volumes feed (2 tasks) | 200 | 11 TIER1_CANDIDATE, 6 LEAD_ONLY | real trade-press leads, below |
| `internet_archive` advancedsearch (5 tasks) | 200 | 8 TIER1_CANDIDATE, 98 LEAD_ONLY, 1 NULL | software manuals, CD-ROMs, US-court dockets |
| `hathitrust` `/cgi/ls` full text (1) | **status 0, 0 bytes** | 1 UNANSWERED | blocked for this scripted client (README: intermittent by design) |
| `chronicling_america` page search (1) | **403, 6,339 B challenge body saved** | 1 UNANSWERED | their policy, not our bug (same body shape proven in HARVEST_README) |

In-window leads, copied from the response bodies, none opened:
- **Maximum PC 2000-03** (`HAIAAAAAMBAJ`) and **2000-04** (`GAIAAAAAMBAJ`), Google Books
  `viewability=all_pages`, matched pages PT44 / PA20; Google's snippet: "Nvidia TNT-2 Vanta 16MB AGP
  3D Graphics Accelerator ... Microsoft Windows 98, 2nd Edition". US consumer-magazine text inside
  the window, but a system spec listing, not founding narrative.
- **Game.EXE 1997-09** (`Game.EXE_09_1997`), **XIO3 Garden City Atari Computer Enthusiasts
  Newsletter Nov/Dec 1995** (row date 1995-11-01), **LEVEL CD-ROM Romania 04/99-06/99** (1999-03/04/05)
  -- 1995-1999 hits, but non-US or enthusiast tier; none is yet a citable sentence about 1993-1995.
- Retrospective, out of window: "Video Games in 100 Objects" (Simon and Schuster) snippet
  "accelerator, was released in 1995 and was capable of processing both 2D and 3D video".

Judgment: the tool's `TIER1_CANDIDATE` label is a pointer heuristic -- on this run it fired on a
2026 Packt book, a 2017 IBM Redbook and a French graphics-card manual -- so it is **not** accepted as
a tier. No article body was read, therefore family (c) supplies **leads, not text**, and the US trade
press of 1995-1999 that would independently corroborate the founding sits exactly behind the two
blocked routes. That is this company's biggest gap.


## Family d corporate print

STATUS: **NULL for the founding window, queried explicitly** -- "paper only" is NOT asserted.

Eight `corporate_print` searches (three query shapes) plus five `internet_archive` searches, all
HTTP 200. Report-word-scoped searches (title AND annual/report/shareholder/prospectus,
mediatype texts, YEAR 1994-2001, and the same `creator`-scoped) returned **numFound 0** -> rows
`NULL`. Re-scoped WITHOUT report terms (the trap HARVEST_README warns about), 1993-2003, title- and
creator-scoped: exactly **one** item, hit by all three shapes -- **`01.-nvidia-annual-reports`**,
"NVIDIA Corporation Annual Reports", collections `fund-and-stock-reports`, `periodicals`,
`magazine_rack`. Carried to text availability (`archive.org/metadata/01.-nvidia-annual-reports`,
HTTP 200, body `sources/harvest/corporate_print/a73668dd7bed4099.json`; server
`ia800507.us.archive.org`, dir `/22/items/01.-nvidia-annual-reports`): the 22 `_djvu.txt` layers run
**Annual Report 2005 through 2026** only; the container file `01. NVIDIA Annual Reports_djvu.txt` is
**16 bytes**. Nothing FY1993-FY2001 is digitised there.

**Trap for the next agent:** that item's IA metadata `date` is **1993-04-05**, identical to the S-1
inception date and plainly a scrapeware artifact, not a document date. An automated reader would
have written "a 1993 Nvidia annual report exists at Internet Archive". It does not: the company was
private until January 1999, and its first annual report is the 10-K405 for FY ended 1999-01-31,
already under `sources/sec/`. Residual value of this family here is low by construction -- the
FY1999-FY2001 printed reports are the same documents as the 10-K405s.


## Family e documentary

STATUS: **UNTRIED** (never queried, therefore not a null).

`tools/periodical_harvest.py` implements no route: HARVEST_README lists family 4 (auction / museum /
special collections) as "**(not implemented)**" and says it "is unqueried by this tool -- no
read-only public API was verified. It stays UNANSWERED and must be reported as such, not as a null."
The brief conditioned this family on cheapness; the CDX 503s in `## Family b web` consumed the web
budget and anything further needs a browser pass.

What only this family can decide: (1) **a 1993 California Articles/Certificate of Incorporation of
NVIDIA CORPORATION** -- the S-1 files only the **Delaware** certificate of February 1998 (Ex-3.1),
bylaws (Ex-3.2) and the form of Amended & Restated certificate (Ex-3.3); the 1993 California
document is described in narrative but **not filed**, so "incorporated in California in April 1993"
rests on the company's own assertion. (2) **The 1993 Series A purchase agreement / certificate
stubs** at $0.50 (4,303,000 shares, net of $22,000 issuance costs, per the filed notes) with
counterparty signatures -- the only way to name who funded the founding rather than infer it from
the June 1993 Sequoia/Sutter Hill board seats. (3) Founder-era artefacts (the Huang/Malachowsky/
Priem agreement, the original business plan, May 1995 NV1 launch collateral) for Stages 1-2.


## Boundaries

Every boundary below is fixed by a document already on disk in `sources/sec/`; names in brackets.
Fiscal caution: years 1993-1997 ended December 31, and "effective January 31, 1998, the Company
changed its fiscal year-end financial reporting period to a 52- or 53-week year ending on the last
Sunday in January. The Company elected not to restate its previous reporting periods ending December
31" [424B4] -- the two series are not additive without the transition period.

**Stage 1 -- origin: 1993-04-05 to first outside capital by June 1993.**
Opens on "the period from inception (**April 5, 1993**) to December 31, 1993 ... derived from audited
financial statements ... audited by KPMG Peat Marwick LLP" and "NVIDIA was incorporated in California
in April 1993" plus the three identical "co-founded the Company in April 1993" bios (Huang
President/CEO, Malachowsky VP Engineering, Priem CTO) [S-1 0001012870-98-000618, 424B4
0001012870-99-000192]. Closes not on prose but on governance and money facts in the same filing:
Coxe (Sutter Hill) and Stevens (Sequoia) "have been a director ... since June 1993", and "In 1993,
the Company sold 4,303,000 shares of Series A preferred stock at $0.50 per share, net of $22,000 of
issuance costs". FY1993 as filed: revenue `-0-`, net loss `$(484)K`, cash `$1,605K`, total assets
`$1,786K`. Still UNKNOWN: the day the founders agreed, and the Series A closing date -- the 1993
constitutive and purchase documents are not filed anywhere in EDGAR.

**Stage 2 -- first real product: development stage 1993-94, NV1 in May 1995, NV1 exit Q1 1997.**
"Since its inception in April 1993 through the end of 1994, NVIDIA was in the development stage and
was primarily engaged in product development and product testing. The Company introduced its first
product, the **NV1, in May 1995**" [S-1 and 424B4, verbatim identical]. First revenue, 1995:
`$1,182K` total (`$1,103K` product + `$79K` royalty), gross loss `$(367)K`. End fixed by "By the end
of 1996, the PC industry had broadly adopted Microsoft's Direct3D and Silicon Graphics Inc.'s ...
OpenGL 3D APIs. As a result, the Company experienced a significant reduction in revenue from sales of
the NV1 and stopped selling the NV1 in the first quarter [1997]". Independent-dated corroboration
inside the same accession: the filed **Amahl sublease dated February 2, 1995**, amended March 1, 1995
and effective as of September 1, 1995, for 34,251 rentable sq ft "charged as 33,026".

**Stage 3 -- repeatable validation: RIVA 128 ships August 1997 to growth proved in the prospectus.**
"the RIVA 128, RIVA128ZX and RIVA TNT graphics processors, which the Company began shipping
commercially in **August 1997, March 1998 and July 1998**" -- three generations agree [S-1/A
0001012870-98-003234, S-1/A 0001012870-99-000100, 424B4]. The inflection is filed, not asserted:
nine months to 1998-10-25 revenue `$92,700K` vs `$5,537K` a year earlier; "184 employees as of
October 25, 1998 as compared to 71 employees as of September 28, 1997"; still loss-making through
it (operating loss `$(3,900)K` over those nine months, accumulated deficit $17.1M at 1998-10-25);
customer mix then in the FY1999 annual report -- "STB 35%, Diamond 27%, Creative 13%, Intel 12%" of
FY1999 revenue against "STB 63% ... Diamond 31%" for calendar 1997 [10-K405 0000929624-99-000772].

**Stage 4 -- scalable company: IPO 1999-01-21 onward, with third-party filings and later audits.**
"We commenced our initial public offering on **January 21, 1999** pursuant to a Registration
Statement on Form S-1 (File No. 333-47495). The managing underwriters ... Morgan Stanley & Co.,
Hambrecht & Quist and Prudential Securities" [10-K405 0001012870-00-001346]; 424B4 filed 1999-01-22;
stockholder written consents 1999-01-06; the $11.0M convertible subordinated notes of July 22 and
August 14, 1998 auto-converted into 1,571,429 shares on January 15, 1999. Scale: revenue `$158,237K`
(FY to 1999-01-31) -> `$374,505K` (FY2000 selected table); R&D staff 117 -> 214; R&D spend $7.1M
(1997) -> $25.1M (FY1999) -> $47.4M (FY2000). Adversity filed in the same stage: the S3 patent suit
over RIVA 128/128ZX/TNT. Upgrade path for the tier: the two blocked periodical routes for 1995-1999
US trade press and the untried documentary route (`## Untried`).


## Conflicts

**X1 -- FY1997 audited figures changed inside the registration (material; adjudicate in Stage 1).**
Selected data in the 1998-03-06 S-1 prints gross profit (loss) for 1993-97 as
`-- -- (367) 874 **7,845**` and operating loss as `(506) (1,351) (6,470) (2,993) **(2,560)**`, net
loss `(484) (1,361) (6,377) (3,077) (2,691)`. The 1998-12-23 S-1/A, the 1999-01-13 S-1/A and the
424B4 all print `**7,827**` gross profit and `**(3,459)**` operating loss for the same calendar 1997
with identical revenue (`29,071`) and identical 1993-96 rows. Something moved about **$899K of FY1997
operating expense** between draft and final. Do not carry a "1997 operating loss" figure into any
register until the FY1997 statements and notes in both accessions are read and one is named canonical.
The 424B4 net-loss row was not read to its end this pass, so nothing is claimed about FY1997 net loss.

**X2 -- Delaware reincorporation: February vs April 1998 (a signed document contradicts the prose).**
Narrative [424B4]: "reincorporated in Delaware in **April 1998**". Filed exhibit [same corpus, S-1
Ex-3.1]: "CERTIFICATE OF INCORPORATION OF NVIDIA DELAWARE CORPORATION ... The undersigned, a natural
person (the Sole Incorporator) ... **February, 1998** by the undersigned who affirms that the
statements made herein are true and correct. ____ Mitchell R. Truelock, Sole Incorporator". A
constitutive document beats prose: the Delaware entity appears formed **February 1998**, i.e. before
the March 6 1998 filing that already lists it as Exhibit 3.1, with the operative charter possibly
effective April 1998. Resolve against Ex-3.3 (Amended & Restated) and the 424B4 capitalisation
footnotes. This is the highest-value conflict found.

**X3 -- The same year's headcount is stated three ways (mis-citation trap, not a contradiction).**
"92 employees" as of 1997-12-31 vs "42" as of 1996-12-31 [1998 S-1]; "184 employees as of October 25,
1998 as compared to 71 employees as of September 28, 1997" [S-1/A + 424B4]; "117 full-time employees
engaged in research and development" [FY1999 10-K405]; "214 ... as of January 30, 2000, compared to
117 ... as of January 31, 1999" [FY2000 10-K405]. Different measurement dates and populations
(total vs R&D). Any register row must carry date and population; never write "1997 headcount" bare.

**X4 -- The registrant's own award count quadruples across two drafts of one registration.**
"over 40 awards from recognized industry publications" [1998-03-06 S-1] -> "over 180 awards" [424B4,
ten months later, same sentence frame]. Both are unverified marketing claims (classify FOUNDER CLAIM);
the escalation itself is evidence about the telling, not about awards.

**X5 -- An unexplained "one month ended January 26, 1997" column sits beside stated December-31
fiscal years 1993-1997** [424B4 footnote: data for "the one month ended January 26, 1997 and the
nine months ended September 28, 1997 are derived from unaudited financial statements included
elsewhere in this Prospectus"]. Unexplained in the text read; not usable as a fiscal-year date.


## Nulls

Each is a query that ran and answered -- not an untried route:
1. **EDGAR holds no Nvidia document for 1993-1997.** 2,487 filings enumerated; earliest is the S-1 of
   **1998-03-06**; 69 in-window filings, none earlier. Structural (private company), so 1993-1995 can
   only ever be retrospective text inside 1998-99 filings plus families (c)/(e).
2. **XBRL early series: 0 rows** -- `sources/financials/xbrl_early_series.csv` written empty for
   1993-01-01..2001-12-31; companyfacts carry no value with an end date in the window.
3. **`corporate_print` in-window: numFound 0** for both report-term shapes, and the single item found
   holds FY2005-FY2026 text with a 16-byte container layer (see `## Family d corporate print`,
   including the false 1993-04-05 metadata date it produced).
4. **IA collection-scoped periodical searches:** `nvidia AND collection:periodicals AND
   mediatype:texts` returned only the annual-report item; `"nv1" nvidia AND mediatype:texts` returned
   **NULL**; no US 1995-1999 trade-magazine issue surfaced by any of the five IA queries.
5. **Two 1998-05-07 `RW` (withdrawal) accessions exist but were not fetched** --
   `0001012870-98-001200`, `0001012870-98-001201`: indexed, unread. A withdrawal in the same month as
   an S-1 amendment is an event, not a null, and Stage 1 must open it.


## Untried

Nothing here may be quoted as absence; each line is a route with a named cost. In cost order:

1. **`FETCH REQUEST` for the script, 0 web calls -- third-party lineages already inside EDGAR.**
   In-window, indexed in `sources/_index/submissions.csv`, never downloaded: **SC 13G 1999-08-06**
   (`0001012870-99-002654`), **SC 13G x3 / SC 13G/A x2 of 2000-02-14** (`0001012870-00-000731`,
   `-000730`, `-000760`, `0001012870-01-000837`, `-000828`, `0000315066-01-000613`),
   **SC 13G 2000-10-10** (`0000315066-00-001238`), **SC 13G 2001-04-30**
   (`0000898430-01-500300`), the 10-Qs of 1999-06-15 / 1999-09-10 / 1999-12-10 / 2000-06-14 /
   2000-09-13 / 2000-12-08, the **1998-05-07 RW x2**, the S-1/As of 1998-04-24, 1998-06-08,
   1998-07-27 and 1999-01-20, and the **10-K405 of 2001-04-27 with its 10-K405/A of 2001-05-25**.
   SC 13D/G filers are *other institutions describing Nvidia* -- the cheapest independent lineage the
   method asks for, already inside family (a). Run `sec_intake.py grab` per accession only after the
   two defects in `## Family a filings` are fixed.
2. **Exhibit bodies inside the accessions already on disk (local, free, highest yield).**
   `0001012870-98-000618.txt` is a complete submission and demonstrably holds Ex-3.1/3.2/3.3, Ex-4.3
   and the Amahl sublease; the earlier investors'-rights agreements, prior subleases and the 1993
   equity-plan documents have not been extracted page by page. Stage 1 should be written from these.
3. **Browser-egress Wayback CDX + the earliest nvidia.com capture** (2 requests) -- the only route to
   a company self-description dated between 1996 and the IPO.
4. **HathiTrust `/cgi/ls` in an open window, then the unconditionally-open catalog API for a known
   htid** (HARVEST_README 3) -- the route to 1995-1999 US trade-journal text on the NV1 and RIVA 128.
5. **Chronicling America from a browser egress** -- 403 re-confirmed this run (6,339-byte challenge
   body kept at `sources/harvest/chronicling_america/03e30a3768a0e367.*`); the canary shape exists
   for exactly this test.
6. **Google Books page reading, not feed reading** -- Maximum PC 2000-03 (`HAIAAAAAMBAJ`) and 2000-04
   (`GAIAAAAAMBAJ`) report `viewability=all_pages`; opened pages give in-window US magazine text.
7. **Family (e) documentary** -- 1993 California certificate, 1993 Series A purchase agreement and
   certificate stubs, May 1995 NV1 launch collateral, pre-founding 1992-93 partnership agreement.
   No scripted route; needs special collections and sale records by hand.
8. **`tools/gates.py` not run** -- this file is a probe verdict with a source index, not a dossier
   with registers, so the mechanical gates have nothing to check yet.


