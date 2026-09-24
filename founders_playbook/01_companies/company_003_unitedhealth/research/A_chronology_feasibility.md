# UNITEDHEALTH STAGE 1 — CHRONOLOGY AND FEASIBILITY PROBE

Level-3 (Corporate Historian + Feasibility) probe for company_003, run **before** any
eleven-agent fleet is committed. Purpose: establish what is actually retrievable about
UnitedHealth Group's founding/formation period (1974/1977 → 1999), fix the three stage
boundaries, audit source availability **by document class**, and render a depth verdict.

Method governance: `00_METHOD_AND_STYLE.md` §2 (hindsight firewall + record-selection null),
§3 (classification + independence rule), §5 (tiers), §6 (time audit), §7 (line formats),
§9 (file splitting), §10 (research-debt triggers), §14 (retrieval discipline: write-first,
hard budget, evidence cache, nothing is a cleanup target).

Company row: `00_universe/fortune_top_50_2026.csv` rank **#3, UnitedHealth Group**, revenue
**$447,567M**, **fiscal year ended 2025-12-31**, profit **$12,056M**, Eden Prairie,
Minnesota, "Health Care: Insurance and Managed Care"; second-source verification recorded in
the universe CSV as "SEC EDGAR 10-K XBRL: exact match on revenue and profit", confidence
High. Fortune's own ranked-year rule (from `00_universe/ranking_source.md`, quoting the
publisher's methodology): "Data shown are for the year ended Dec. 31, 2025" unless otherwise
noted, window = "fiscal year ended on or before Jan. 31, 2026" — so UnitedHealth is ranked on
a **calendar-aligned fiscal year, FY2025 = 2025-01-01 → 2025-12-31**, and its insurance
revenue basis is "premium and annuity income, investment income, and capital gains or losses,
but exclude deposits". Ranked entity name in Fortune's payload is "UnitedHealth Group"; the
SEC registrant name is **not the same string** as the founding entity's name (see Findings
UH-02, UH-03).

Feasibility-register classification (`00_universe/ranking_source.md` §B): rank 3 sits in
**"B. Founder-era reachable, but the origin is dual-named or the entity was later renamed"**,
with the register's entry reading: "Infobox lists **two** origins: 1974 (as CharterMed) and
1977 (as UnitedHealthCare); founder Richard T. Burke" and the note "Founder named, but the
company's own record offers two founding dates. Which one a 'founding' report uses is a
decision, not a fact." This probe tests that label against evidence rather than adopting it —
including the founder's name, which the register sourced only from a Wikipedia infobox at
`Low–Medium` confidence by its own admission.

## Verdict (depth recommendation)

PLACEHOLDER — written after findings; see below.

## Recommended stage boundaries

PLACEHOLDER — | Stage | Start | End | Why This Boundary | Confidence |

## Findings

Format per record (method §7): `UH-nn Claim: … — Date: … — Source: … — Source date: … —
URL: … — Archived: … — Tier: <1-4> — Class: <FACT|FOUNDER CLAIM|CONTEMPORARY OBSERVATION|
RETROSPECTIVE INTERPRETATION|INFERENCE|ESTIMATE|UNKNOWN> — Passage: "…" or
NO_VERBATIM_PASSAGE_RECORDED — Conf: … — Corroboration: … — Conflicts: …`

This section was written by the **Register Completer** (fast tier) by mining the 55 files
already in `../sources/`; no new retrieval was performed to produce UH-01…UH-41 except where
a record says otherwise. All `Passage:` strings were read out of a local file with line
numbers recorded in the Evidence cache.

Batch A — EDGAR registrant identity, filing floor, and name history (all Tier 1).

UH-01 Claim: The SEC registrant behind the Fortune rank-#3 row "UnitedHealth Group" is EDGAR CIK **0000731766**, ticker UNH, conformed title "UNITEDHEALTH GROUP INC", SIC 6324 "HOSPITAL & MEDICAL SERVICE PLANS", EIN 411321939, fiscal year end 1231, `entityType: operating`, business address 1 Health Drive, Eden Prairie MN 55344 — Date: ongoing — Source: `SEC_company_tickers.json` + `EDGAR_submissions_CIK0000731766.json` (header fields) + `EDGAR_cs2_UNITED+HEALTHCARE.xml` — Source date: 2026-09-24 (retrieval by the probe agent) — URL: https://www.sec.gov/files/company_tickers.json ; https://data.sec.gov/submissions/CIK0000731766.json — Archived: sources/SEC_company_tickers.json, sources/EDGAR_submissions_CIK0000731766.json, sources/EDGAR_cs2_UNITED+HEALTHCARE.xml — Tier: 1 — Class: FACT — Passage: `{"cik_str":731766,"ticker":"UNH","title":"UNITEDHEALTH GROUP INC"}` ; `"sic": "6324"`, `"sicDescription": "Hospital & Medical Service Plans"` — Conf: High — Corroboration: 2 independent SEC endpoints agree (ticker file + submissions file) — Conflicts: `EDGAR_cs2_UNITED+HEALTHCARE.xml` now carries `<state-of-incorporation>DE</state-of-incorporation>` while every 1996–2000 SEC header in this cache says `STATE OF INCORPORATION: MN`; the date and instrument of any redomiciliation are **not** in the local corpus (see UH-40).

UH-02 Claim: **UnitedHealth's electronic filing history on EDGAR begins 1995-02-02** — a third-party `SC 13G/A`, accession 0000729057-95-000082 — and contains **no document of any type filed before that date**; the two bulk blocks on disk hold 3,306 rows spanning 1995-02-02 → 2020-12-14 and the "recent" block covers 2020-12-17 → 2026-09-08. The 1984/1986-era registration statement, the prospectus, and all 1977–1994 SEC text for this filer are therefore **paper-only** — Date: 1995-02-02 — Source: `EDGAR_submissions_CIK0000731766_submissions-001.json` (2,000 rows, 2010-05-28→2020-12-14) + `_submissions-002.json` (1,306 rows, 1995-02-02→2010-05-10), sorted ascending on `filingDate` — Source date: 2026-09-24 (retrieval); 2026-09-24 (arithmetic by completer: 2,000 + 1,306 = 3,306 rows; min(`filingDate`) = 1995-02-02, max = 2020-12-14) — URL: https://data.sec.gov/submissions/CIK0000731766-submissions-001.json ; …-002.json — Archived: sources/EDGAR_submissions_CIK0000731766_submissions-001.json, sources/EDGAR_submissions_CIK0000731766_submissions-002.json — Tier: 1 — Class: FACT (documented absence within this index) — Passage: oldest row `1995-02-02 SC 13G/A 0000729057-95-000082 fileNumber 005-36526`; next `1995-02-10 SC 13G 0000315066-95-002145 … "SCHEDULE 13G - 2-14-95 - UNITED HEALTHCARE CORPORATION"` — Conf: High — Corroboration: 2 (both bulk blocks; no gap between 1995-02-02 and 2020-12-17 once the recent block is added) — Conflicts: None. **This is the real earliest filing date for this filer and it is ~15 months LATER than the Walmart (1994-02-14) and Apple (1994-01-26) floors** — the pre-1995 dark age here is deeper, not shallower.

UH-03 Claim: The earliest **annual report** of this registrant on EDGAR is a Form **10-K405 filed 1995-03-28** (accession 0000950131-95-000748, primary document described "FORM 10-K"), i.e. an annual report for FY1994 carrying the Item 405 late-compliance flag; the earliest filing of bare form-type `10-K` is 1997-03-28 (0000912057-97-010848) and the earliest `10-Q` is 1995-05-12 (0000731766-95-000011, "1ST QUARTER 95 10-Q") — Date: 1995-03-28 — Source: EDGAR bulk submissions index (form/date/accession/primaryDocDescription columns) — Source date: 2026-09-24 — URL: https://data.sec.gov/submissions/CIK0000731766-submissions-002.json — Archived: as UH-02 — Tier: 1 — Class: FACT — Passage: `1995-03-28 10-K405 0000950131-95-000748 "FORM 10-K" fileNumber 001-10864` — Conf: High — Corroboration: 1 index — Conflicts: None. Consequence: the FY1994 10-K text is the **earliest company-authored annual document reachable online**, and it is on disk nowhere in this cache → fleet action item, not a null.

UH-04 Claim: **No S-1 (or any other initial-registration form) exists anywhere in this filer's EDGAR history**; the earliest registration statements on the index are employee-benefit `S-8` filings starting 1995-05-04 (0000731766-95-000008, file 033-59083), the earliest `S-4` is 1996-03-07 (0000950131-96-000919, file 333-01517) and the earliest `S-3` is 1996-05-23 (333-04401) — Date: 1995-05-04 — Source: EDGAR bulk submissions index, filtered to forms beginning "S-" — Source date: 2026-09-24 — URL: as UH-02 — Archived: as UH-02 — Tier: 1 — Class: FACT (documented absence in the electronic index) — Passage: first three S-rows `1995-05-04 S-8 0000731766-95-000008 033-59083 "REGISTRATION STATEMENT"`; `1995-05-26 S-8 0000731766-95-000013 033-59623`; `1995-11-01 S-8 0000731766-95-000021 033-63885` — Conf: High — Corroboration: 1 index + UH-02 floor — Conflicts: None. Reading discipline: the absence is an EDGAR-coverage fact, **not** evidence that no 1980s registration statement exists — the Exchange Act file number **001-10864** is already attached to the 1995-02-14 8-K, so the Section 12(b) registration predates the electronic floor.

UH-05 Claim: Registrant's Exchange Act file number is **001-10864** and the self-reported SRO is the NYSE; the 1998 S-4 states the listing in its own words: "The United HealthCare Common Stock is listed on the New York Stock Exchange, Inc. (the 'NYSE') under the symbol 'UNH'" — the *date* the stock first listed is nowhere in the local corpus — Date: 1995-02-14 (earliest attestation of the file number) — Source: EDGAR bulk index `fileNumber` column + S-4 joint proxy-prospectus — Source date: 1998-06-02 (S-4) / 2026-09-24 (index) — URL: https://www.sec.gov/Archives/edgar/data/731766/000104746998022543/0001047469-98-022543.txt — Archived: sources/S4_0001047469-98-022543_filed-1998-06-02.txt (line 521) — Tier: 1 — Class: FACT — Passage: "The United HealthCare Common Stock is listed on the New York Stock Exchange, Inc. (the "NYSE") under the symbol "UNH"" — Conf: High — Corroboration: 2 (index fileNumber on 1995 filings; filing text 1998) — Conflicts: None.

UH-06 Claim: EDGAR's own name-history for CIK 731766 records exactly **one** former conformed name — "UNITED HEALTHCARE CORP" — with `from 1995-04-04 to 2000-02-14` in the submissions JSON and, in the SEC header of filings made 1999–2000, `DATE OF NAME CHANGE: 19920703`. **No EDGAR field anywhere records a 1977, 1978 or 1984 name for this registrant** — Date: 1992-07-03 / 1995-04-04 / 2000-02-14 (as recorded) — Source: `EDGAR_submissions_CIK0000731766.json` `formerNames` + `<FORMER COMPANY>` block in the FY1999 10-K and DEF 14A 2000 headers — Source date: 2000-03-30 (10-K header) / 2026-09-24 (JSON retrieval) — URL: https://data.sec.gov/submissions/CIK0000731766.json ; https://www.sec.gov/Archives/edgar/data/731766/000091205700014911/0000912057-00-014911.txt — Archived: sources/EDGAR_submissions_CIK0000731766.json, sources/10-K_FY1999_acc-0000912057-00-014911_filed-2000-03-30.txt (lines 50–51), sources/DEF14A_2000-04-07_acc-0000912057-00-016900.txt (line 51) — Tier: 1 — Class: FACT (as to what the register records) / **UNKNOWN (as to what each date denotes)** — Passage: `"formerNames": [{"name": "UNITED HEALTHCARE CORP", "from": "1995-04-04T04:00:00.000Z", "to": "2000-02-14T05:00:00.000Z"}]` ; `FORMER CONFORMED NAME: UNITED HEALTHCARE CORP / DATE OF NAME CHANGE: 19920703` — Conf: High (presence), Low (semantics: EDGAR's header convention does not state whether 1992-07-03 is when the former name was *adopted* or when the *current* name took effect; the two candidate readings are one year apart from the JSON's `from` field) — Corroboration: 2 records of the same EDGAR metadata (not independent) — Conflicts: UH-41 (three incompatible dates for "when it became UnitedHealth Group").

UH-07 Claim: The legal rename is documented in the filings themselves, in the company's own words: Form 8-K accession 0000912057-00-010247 (filed 2000-03-08, signed by General Counsel David J. Lubben, dated March 6, 2000), Item 5 — Date: 2000-03-01 (filing of articles) / 2000-03-06 (effective) — Source: Form 8-K, Item 5 "Other Events" — Source date: 2000-03-08 — URL: accession 0000912057-00-010247; **primary-document URL not locally attested** (only the accession number appears in the cache), directory pattern per UH-06 — Archived: sources/8-K_0000912057-00-010247.txt (lines 162–165) — Tier: 1 — Class: FACT — Passage: "On March 1, 2000 registrant filed Articles of Amendment with the Minnesota Secretary of State's office to change its name from United HealthCare Corporation to UnitedHealth Group Incorporated to be effective March 6, 2000." — Conf: High — Corroboration: 1 Tier-1 document + UH-06's EDGAR `to: 2000-02-14` — Conflicts: UH-41. **Route value:** this names the **Minnesota Secretary of State** as the registry holding the amendment instruments — the same office that would hold the January 1977 articles and any 1984 name-change instrument.

## Source availability by document class

PENDING.

## Famous claims pre-flagged as likely untraceable

PENDING.

## Merger and naming structure (how to treat a two-entity origin)

PENDING.

## Evidence cache

PENDING.

## Data gaps

PENDING.

## Queries that returned null

PENDING.

## Fleet briefs if the run proceeds

PENDING (six short specialist briefs).
