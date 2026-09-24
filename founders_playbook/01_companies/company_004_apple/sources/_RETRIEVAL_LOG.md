# APPLE — RETRIEVAL LOG (Level-3 chronology/feasibility probe, 2026-09-24)

Append-only. Every file in this directory carries a provenance header or is described here.
**Create files only — nothing in this directory may be deleted, moved, renamed or tidied.**

## EDGAR (Tier 1)

| File | Retrieved from (URL) | Access date | What it is |
|---|---|---|---|
| `EDGAR_company_tickers.json` | https://www.sec.gov/files/company_tickers.json | 2026-09-24 | SEC registry; establishes Apple Inc. = CIK 0000320193 / AAPL |
| `EDGAR_submissions_CIK0000320193.json` | https://data.sec.gov/submissions/CIK0000320193.json | 2026-09-24 | current submissions block (1,000 rows, 2015-07-27 → present) + pointer to bulk file 001 |
| `EDGAR_submissions_CIK0000320193_001_1994-2015.json` | https://data.sec.gov/submissions/CIK0000320193-submissions-001.json | 2026-09-24 | **Apple's complete pre-2015 electronic filing history: 1,249 filings, 1994-01-26 → 2015-07-25.** No S-1, no 1980 prospectus, nothing before 1994-01-26 |
| `10-K_FY1994_acc-0000320193-94-000016_filed-1994-12-13.txt` | https://www.sec.gov/Archives/edgar/data/320193/000032019394000016/0000320193-94-000016.txt | 2026-09-24 | **Apple's earliest digital annual report** (FY ended 1994-09-30), 240,556 B. Contains the incorporation sentence (1977-01-03, California) at lines ~130-135 and the exhibit index citing paper-era 1988-1991 filings at ~3175-3190 |
| `EDGAR_10-K_FY1994_acc0000320193-94-000016_index.json` | https://www.sec.gov/Archives/edgar/data/320193/000032019394000016/index.json | 2026-09-24 | accession directory listing |
| `probe_edgar_fts_*.json` (6 files) | https://efts.sec.gov/LATEST/search-index?q=… | 2026-09-24 | EDGAR full-text-search coverage probes. 2001 = 3,081 hits; 1994-96 = 0; 1999-2000 = 0; pre-1994 Apple-scoped = 0; positive control `q=test` = 10,000+ ⇒ **FTS floor is 2001-01-01**; the zeros are index coverage, not absence |

## Wayback CDX (Tier 1 index)

| File | Queries | Result |
|---|---|---|
| `probe_wayback_APPLE.md` | `apple.com` / `www.apple.com` exact 1993-1999; `www.apple.com` exact 1990-1993; `applecomputer.com` 1993-2001; `apple2.org` 1994-2005; `wozniak.com` 1995-2005 | apple.com root earliest **1996-10-22**; **empty result set for 1990-1993**; applecomputer.com earliest 1996-12-19; apple2.org 1998-04-29; wozniak.com 1998-12-07. `matchType=prefix` sweeps deliberately NOT run (504 = unanswered, per Amazon-run lesson) |

## Contemporary trade press, full OCR text (Tier 1) — Internet Archive

Retrieved via `https://archive.org/metadata/<id>` then `https://<server><dir>/<name>_djvu.txt`
(the `https://archive.org/download/...` form 302s to a CDN node that returned 404 in this run —
**route note for the fleet: use the metadata→items-server form**).

| Local file(s) | Internet Archive identifier | Issue | Cited as |
|---|---|---|---|
| `ia_byte_1976/byte-1976-01..12.txt` | `byte-magazine-1976-01` … `-12` | BYTE, January–December 1976 (Vol 1) | ~5.7 MB; the twelve 1976 issues, exhaustively grepped |
| `ia_byte_1977/byte-1977-04/05/06/07.txt` | `byte-magazine-1977-04` … `-07` | BYTE, April–July 1977 | Wozniak's own May 1977 "System Description: The Apple-II"; Helmers' April 1977 sighting; Apple's June 1977 $1,298/$598 advertisement |
| `ia_byte_1981/byte-1980-12.txt`, `byte-1981-02.txt` | `byte-magazine-1980-12`, `byte-magazine-1981-02` | BYTE, December 1980 and February 1981 | Feb 1981 p 212 "Apple Stock Goes On Sale" = the IPO terms + pre-IPO revenue/profit series + Venrock/Markkula/Xerox shareholdings |

## Homebrew Computer Club newsletters (Tier 1, in-window primary)

`ia_homebrew/hccNNNN.txt` — identifiers `hcc0109`(1975-11-30), `hcc0110`(1975-12-31),
`hcc0201`(1976-01-31), `hcc0202`(1976-02-29), `hcc0203`(1976-03-31), `hcc0204`(1976-04-30),
`hcc0205`(1976-05), `hcc0206`(1976-06-09), `hcc0207`(1976-08-04), `hcc0209`(1976-09-15),
`hcc0211`(1976-12-10), `hcc0213`(1977-01-19), `hcccf`(1977-02-16 West Coast Computer Faire flyer).
Full run enumerated: 32 items, Vol 1 No 1 (1975-03-15) → Vol 2 No 21 (1977-12-01).
**Earliest Apple trace in the club's own printed record: `hcc0204`, 1976-04-30.**

## Artifact registries, auction coverage, secondary

| File | URL | Access date | Note |
|---|---|---|---|
| `apple1registry_stories.html` / `.txt` | https://www.apple1registry.com/en/stories.html | 2026-09-24 | Achim Baqué's Apple-1 Registry: Jobs's 1973 job application (Charterfields, March 2021, US$222,400), Paul Terrell's 1976 Polaroids of the first Apple-1 showing at the Byte Shop, Ronald Wayne's own written account, Koa-wood Byte Shop cases, four "thought to be lost" 1976 document copies. Stories dated Feb 2022 → Aug 2022 = **retrospective curation of primary artifacts** |
| (no local copy) | https://www.itechguides.com/apples-founding-papers-sell-for-2-515-million-after-earlier-4-million-estimate/ | 2026-09-24 | Christie's sale of the 3-page 1976 partnership agreement, 2026-01-23, $2,515,000 |
| (no local copy) | https://hypebeast.com/2025/11/apple-computer-company-founding-contract-heads-to-auction | 2026-09-24 | Pre-sale lot detail: signed 1976-04-01; Jobs 45 / Wozniak 45 / Wayne 10; estimate $2–4M |
| (fetch failed, recorded) | https://news.artnet.com/art-world/apple-contract-constitution-christies-sale-2720751 | 2026-09-24 | **HTTP 403 Forbidden — do not retry this URL** |
| (no local copy) | https://guides.loc.gov/this-month-in-business-history/april/apple-computer-founded | 2026-09-24 | Tier-2 institution page, created 2008-04, updated 2023-04; sources = Brashares 2001, Britannica 2021, Mergent 2020; **no contemporaneous sourcing** |

## Kilobaud / InfoWorld / Creative Computing availability (untested bodies)

`title:(infoworld)` = 120 IA items (Google Books ids `bub_gb_*`); `title:(creative+computing)` =
555 items; `title:(kilobaud)` = 159 items, but `Kilobaud197606`, `Kilobaud197610`, `Kilobaud197612`
have **no `_djvu.txt` text layer** → scans only, require OCR before full-text mining.

## Public-record endpoints probed (reachability only)

`https://bizfileonline.sos.ca.gov/api/BusinessSearch` → HTTP 200 in 0.17 s (endpoint alive; entity
search not exercised — needs an interactive/POST query).
`https://www.sccgov.org/sites/ore/Pages/home.aspx` → **HTTP 403**.
`https://vcrea.sccacc.org/` (Santa Clara County recorder) → **HTTP 000, connection failed / unanswered**.

## Budget actually spent (this probe)

WebSearch **10/10 (exhausted)**. WebFetch **5/10 used**: Library of Congress guide page; artnet
(**HTTP 403**, not retried); itechguides (Christie's result); hypebeast (pre-sale lot detail);
apple1registry.com stories page. All magazine, EDGAR and CDX retrieval was done with `curl` /
`urllib` against documented public endpoints, not counted as WebFetch. **No file in this directory
was deleted, moved or renamed.**
