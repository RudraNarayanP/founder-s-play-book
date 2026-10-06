# SEC submissions index -- TARGET CORP (CIK 0000027419, TGT)

Built by `tools/sec_intake.py` at 2026-09-25 19:42 UTC. 2628 filings enumerated

**What this file is, and what it is not.** It enumerates the EDGAR submissions this repository
retrieved for **CIK 0000027419 only**, from the SEC's own submissions endpoint, at the build time
stamped above. It is a convenience summary of `submissions.csv`, which is itself a derived copy of
the raw response (`raw_submissions_CIK0000027419.json`); the SEC's bytes are the record, and the raw
response is the one this repository opened (registered as `sources.csv` **S4217**, with the derived
set registered as **S4223**).

**It is NOT a source of truth about what exists.** A form is absent from EDGAR for this registrant
only if this list says so **and** the list's own floor permits a statement about the period asked
about: the earliest filing here is **1994-02-10**, which is where EDGAR's electronic record for this
CIK begins, not where the company's filing history begins, and it says nothing at all about any
**predecessor** CIK (the name-to-CIK lookups failed and stay open -- `data_gaps.csv` U.025, U.036).
Do not read a blank before 1994 as an absence of filings.

**How this file goes stale.** It is a point-in-time build: any filing made after the stamped UTC
time, and any field the intake tool discards (this copy carries no `formerNames`, no accession-level
document lists), is missing from it silently. Re-run `tools/sec_intake.py index --cik 27419` to
refresh; if the refresh changes the floor, the derived rows S4217/S4223 and gap U.036 must be
re-checked, not inherited. Grep `submissions.csv` for coverage questions about **this CIK from
1994-02-10 onward** -- and treat anything outside that perimeter as unanswered.

**Provenance and transport of these bytes** (added 2026-09-30 by the second repair pass,
certifier blocker B-4 / COR-20, so the register is not the only place the transport is stated).
Measured on disk this pass; nothing here is inherited from a prior report.

| file | bytes on disk | provenance sidecar | transport |
|---|---|---|---|
| `raw_submissions_CIK0000027419.json` (the raw SEC response, = `sources.csv` **S4217**) | 149,561 | **none** | UNSTAMPED — no sidecar records the TLS state of the retrieval, so this file attests to the response body only, not to how it was fetched |
| `submissions.json` (derived, = **S4223**) | 576,114 | **none** | UNSTAMPED |
| `submissions.csv` (derived; **2,628 data rows** + header, = **S4223**) | 237,026 | **none** | UNSTAMPED |
| `_INDEX.md` (this file, = **S4223**) | this build | **none** | UNSTAMPED |

**Where a sidecar does exist.** Every `.txt` carrier under `sources/corporate_print/` and
`sources/periodicals_csa_1963/` has a `.meta.json` sidecar recording a `transport` field: **15
layers, 10 `verified TLS` and 5 `UNVERIFIED TLS`** (the five unverified are FY1966, FY1967, FY1971,
FY1973, FY1974 — `data_gaps.csv` U.028; confidence on their rows is capped at Medium by U.037). Two
`sources/web_archive/cdx_*.txt` bodies carry **no** sidecar, so the status codes their rows discuss
(U.026) are unbacked by provenance — §14 rule 9. The sidecar absence on the four index bytes above is
recorded here rather than asserted elsewhere: these bytes are SEC-attested in content but this
repository has no fetch-transport record for them, so they may be cited for **what the SEC index
contains**, never as a TLS-verified retrieval.

## Earliest filing per form

| form | filed | accession | primary document |
|---|---|---|---|
| SC 13G | 1994-02-10 | 0000912057-94-000335 |  |
| DEF 14A | 1994-04-19 | 0000950131-94-000526 |  |
| 10-K | 1994-04-21 | 0000950131-94-000539 |  |
| 10-Q | 1994-06-10 | 0000950131-94-000998 |  |
| SC 13G/A | 1995-02-09 | 0000315066-95-001450 |  |
| 424B5 | 1995-02-28 | 0000950131-95-000459 |  |
| S-8 | 1995-11-06 | 0000950131-95-003057 |  |
| S-3 | 1996-01-23 | 0000950131-96-000128 |  |
| 8-K | 1996-02-08 | 0000950131-96-000332 |  |
| 10-K405 | 1996-04-18 | 0000950131-96-001615 |  |
| 8-A12B | 1996-09-12 | 0000950131-96-004492 |  |
| 305B2 | 1996-10-03 | 0000950131-96-004870 |  |
| 424B3 | 1997-08-28 | 0000912057-97-029393 |  |
| 8-A12B/A | 1999-05-18 | 0001047469-99-021400 |  |
| 424B2 | 1999-07-15 | 0001047469-99-027573 |  |
| S-3/A | 2000-08-03 | 0000912057-00-034475 | s-3a.htm |
| POS AM | 2001-04-30 | 0000912057-01-511369 | a2046940zposam.htm |
| NO ACT | 2002-04-01 | 9999999997-02-030313 | 9999999997-02-030313.paper |
| ARS | 2002-04-16 | 9999999997-02-023529 | 9999999997-02-023529.paper |
| 4 | 2003-06-03 | 0000027419-03-000014 | xslF345X01/primary_doc.xml |
| 5 | 2004-03-12 | 0000027419-04-000031 | xslF345X02/primary_doc.xml |
| 3 | 2004-05-13 | 0000027419-04-000044 | xslF345X02/primary_doc.xml |
| 4/A | 2004-06-17 | 0000027419-04-000062 | xslF345X02/primary_doc.xml |
| 3/A | 2004-06-18 | 0000027419-04-000063 | xslF345X02/primary_doc.xml |
| CORRESP | 2006-06-02 | 0001104659-06-039244 | filename1.htm |
| 11-K | 2006-06-22 | 0001104659-06-043180 | a06-14081_111k.htm |
| FWP | 2006-07-12 | 0001104659-06-046645 | a06-16029_1fwp.htm |
| UPLOAD | 2006-07-28 | 0000000000-06-035339 | filename1.pdf |
| 25 | 2007-01-04 | 0001104659-07-000544 | a07-1066_125.htm |
| S-3ASR | 2007-01-09 | 0001104659-07-001505 | a06-20241_1s3asr.htm |
| PRE 14A | 2007-03-19 | 0001104659-07-020462 | a07-3311_4pre14a.htm |
| SC 13D | 2007-07-16 | 0000902664-07-002284 | sc13d.txt |
| SC 13D/A | 2007-12-24 | 0000950136-07-008520 | file1.htm |
| CT ORDER | 2008-12-15 | 9999999997-08-048340 | filename1.pdf |
| DEFA14A | 2009-03-16 | 0001104659-09-017989 | a09-2081_2defa14a.htm |
| DFAN14A | 2009-03-17 | 0000950123-09-004779 | y01330dfan14a.htm |
| PREC14A | 2009-03-24 | 0001047469-09-003070 | a2191099zprec14a.htm |
| PRER14A | 2009-03-30 | 0001047469-09-003334 | a2192008zprer14a.htm |
| PREN14A | 2009-04-06 | 0000950123-09-006097 | y01431pren14a.htm |
| DEFC14A | 2009-04-21 | 0001047469-09-004379 | a2192439zdefc14a.htm |
| PRRN14A | 2009-04-21 | 0000950123-09-006920 | y01431r1prrn14a.htm |
| 10-K/A | 2010-03-18 | 0001047469-10-002408 | a2197369z10-ka.htm |
| 8-K/A | 2010-11-12 | 0001104659-10-057725 | a10-21051_18ka.htm |
| PX14A6G | 2012-06-04 | 0001214659-12-002536 | c64120px14a6g.htm |
| 10-Q/A | 2013-07-29 | 0001104659-13-057305 | a13-17284_110qa.htm |
| SD | 2014-06-02 | 0001104659-14-043078 | a14-13835_1sd.htm |
| S-8 POS | 2017-06-23 | 0001104659-17-041314 | a17-15645_5s8pos.htm |
| 144 | 2023-03-31 | 0001959173-23-000420 | xsl144X01/primary_doc.xml |
| SCHEDULE 13G/A | 2025-05-07 | 0000932471-25-000660 | xslSCHEDULE_13G_X01/primary_doc.xml |
| SCHEDULE 13G | 2026-04-30 | 0002100119-26-001095 | xslSCHEDULE_13G_X02/primary_doc.xml |

## UNANSWERED slices (never report these as absent)

(none)
