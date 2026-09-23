# WALMART SOURCES — RETRIEVAL LOG (append-only; never delete entries)

All retrieval on 2026-09-23 by Level-3 chronology/feasibility probe.
HTTP client: curl (Git Bash) and WebFetch. SEC access recipe: User-Agent
"FounderPlaybook Research AdminContact@example.com", Referer https://www.sec.gov/,
Accept-Encoding negotiated (compressed).

| File in this dir | Origin URL | Retrieved | What it is | Status |
|---|---|---|---|---|
| probe_EDGAR_submissions_001.json | https://data.sec.gov/submissions/CIK0001041694-submissions-001.json | 2026-09-23 | S3 NoSuchKey error page | NOT A SOURCE — 317 B error; retained as evidence that CIK 1041694 (7-digit) is wrong; correct CIK is 104169 |
| probe_EDGAR_submissions_002.json | https://data.sec.gov/submissions/CIK0001041694-submissions-002.json | 2026-09-23 | S3 NoSuchKey error page | NOT A SOURCE (same) |
| probe_EDGAR_submissions_current.json | https://data.sec.gov/submissions/CIK0001041694.json | 2026-09-23 | S3 NoSuchKey error page | NOT A SOURCE (same) |
| probe_SEC_tickers.json | https://www.sec.gov/files/company_tickers.json | 2026-09-23 | SEC ticker->CIK map | T1; yields cik_str 104169 / WMT / "Walmart Inc." |
| EDGAR_submissions_CIK0000104169.json | https://data.sec.gov/submissions/CIK0000104169.json | 2026-09-23 | Current filings block (2023-05-15 -> 2026-09-18) + pointer to historical blocks | T1 |
| EDGAR_submissions_CIK0000104169_002_1994-2012.json | https://data.sec.gov/submissions/CIK0000104169-submissions-002.json | 2026-09-23 | 1,409 filings, 1994-02-14 -> 2012-05-21 (flat-array legacy schema). OLDEST = 1994-02-14 SC 13G/A; oldest 10-K = 1995-04-27 acc 0000104169-95-000004 | T1 — establishes EDGAR has NO Walmart pre-1994 filings, incl. nothing from the 1970 IPO |
| probe_wayback_walmartcom_exact.txt | CDX: url=walmart.com&matchType=exact&from=1990&to=1999 | 2026-09-23 | 4 rows; earliest 19961229070003 www.walmart.com 200 | T1 index — earliest capture 1996-12-29 |
| probe_wayback_walmart_exact.txt | CDX: url=walmart.com&matchType=exact&from=1994&to=1999 | 2026-09-23 | identical rows (host normalised) | T1 index |
| probe_wayback_walmartcom_prefix1994.txt | CDX: matchType=prefix&from=1994&to=1994 | 2026-09-23 | HTTP 504 Gateway Time-out HTML | NOT evidence of absence; upstream failure, same trap as Amazon run — do not re-run prefix sweeps |
| EXTRACT_corporate_walmart_history_timeline.md | https://corporate.walmart.com/about/history | 2026-09-23 (WebFetch) | Dated company self-narrative extracts | see file |
| EXTRACT_pbs_2004_timeline.md | https://www.pbs.org/newshour/economy/business-july-dec04-timeline_08-20 | 2026-09-23 (WebFetch) | PBS NewsHour Aug-2004 Wal-Mart timeline extracts | see file |
| EXTRACT_scdigest_2012_timeline.md | https://www.scdigest.com/ASSETS/ON_TARGET/12-07-27-1.php | 2026-09-23 (WebFetch) | SCDigest 50-year supply-chain timeline extracts | see file |
| (not saved) vintagebentonville/walton-sam | https://www.vintagebentonville.com/walton-sam.html | 2026-09-23 | WebFetch summary only; page found unreliable (Newport "Arkansas" error) and uncited | record only |

WARNING FOR LATER AGENTS: EXTRACT_* files preserve quotations as returned by the
retrieval model; re-verify any verbatim passage against the live page before quoting in a
dossier. Raw .json/.txt files are byte-as-saved and citable directly.
NOT YET RETRIEVED (open leads, high value): 1962 opening flyer image (reddit vintageads);
FY1995 10-K business-section founding sentence (acc 0000104169-95-000004); Arkansas SoS
entity records; SEC Reference Room paper 1970 registration statement.
