# A_chronology_feasibility.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:41:07Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

STATUS: PENDING

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

STATUS: PENDING

## Family b web

STATUS: PENDING

## Family c periodicals

STATUS: PENDING

## Family d corporate print

STATUS: PENDING

## Family e documentary

STATUS: PENDING

## Boundaries

STATUS: PENDING

## Conflicts

STATUS: PENDING

## Nulls

STATUS: PENDING

## Untried

STATUS: PENDING

