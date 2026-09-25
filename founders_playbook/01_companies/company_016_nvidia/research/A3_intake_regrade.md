# A3_intake_regrade.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:33:33Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Dry run

STATUS: WRITTEN 2026-09-27 (regrade pass, agent `regrade-t3-batch`; all figures observed in this session)

`python tools/sec_intake.py resolve --ticker NVDA` → `{"ticker": "NVDA", "cik": 1045810, "name": "NVIDIA CORP"}`
— the brief's CIK claim is confirmed. Window used everywhere below: **1993-01-01 → 2001-12-31**.

`python tools/sec_intake.py index --cik 1045810 --company-dir founders_playbook/01_companies/company_016_nvidia --from 1993-01-01 --to 2001-12-31 --dry-run`
→ `index: 2487 filings from NVIDIA CORP (NVDA); earliest forms: 10-K, 10-K/A, 10-K405, 10-K405/A, 10-Q, 10-Q/A, 13F-HR, 144, 144/A, 3, 4, 4/A, 424B2, 424B4`.

Nvidia is the case where the broken build hurt least, because its EDGAR floor (1998-03-06) is close to the
nameless pre-2001 era's edge and the probe had already rebuilt the index by hand: **2,487 filings** was the
probe's number and is still the number. The dry-run therefore flagged no new coverage; the change this pass
delivers is in *stored documents*, not in enumeration.

## Index

STATUS: WRITTEN 2026-09-27 (regrade pass)

Live `index` run (no `--dry-run`) → identical enumeration; `sources/_index/submissions.csv` re-written.
Parsed this session (`filingDate,form,accession,reportDate,primaryDocument,source`):

- total rows **2,487**; rows inside **1993-01-01 → 2001-12-31** = **69** (matches the probe's "69 filings").
- **Earliest in-window index filing: Form S-1, accession `0001012870-98-000618`, filed 1998-03-06.** Nothing
  exists in the index for 1993–1997, which re-confirms the probe's hard boundary: every 1993-1997 date in
  this company's dossier is a retrospective statement inside a 1998-99 document, and that is structural,
  not a fetch failure.
- **30 of 69** in-window rows carry a **blank `primaryDocument`** (the nameless pre-2001 listing defect); the
  other 39 are named, which is why Nvidia's intake survived the broken build better than Costco's.
- Earliest per form in-window: S-1 1998-03-06 · 8-A12B 1998-03-23 · 8-A12G 1998-04-03 · S-1/A 1998-04-24 ·
  RW 1998-05-07 · 424B4 1999-01-22 · S-1MEF 1999-01-22 · S-8 1999-03-23 · 10-K405 1999-04-29 ·
  DEF 14A 1999-05-17 · 10-Q 1999-06-15 · SC 13G 1999-08-06 · SC 13G/A 2000-02-14 · S-3 2000-03-29 ·
  S-3/A 2000-04-20 · DEFR14A 2000-06-08 · 424B2 2000-09-19 · S-3MEF 2000-09-26 · 8-K 2000-09-28 ·
  425 2000-12-18 · S-4 2001-01-26 · S-4/A 2001-02-13 · 10-K405/A 2001-05-25 · 8-K/A 2001-05-31 · PRE 14A 2001-06-01.

`facts --from 1993-01-01 --to 2001-12-31` → printed
`facts: founders_playbook\01_companies\company_016_nvidia\sources\financials\xbrl_early_series.csv` and
**wrote nothing**: `sources/financials/` exists but lists **0 files**. The probe recorded that same path as a
written 0-row CSV; the file is not there now and this pass did not delete it (no cleanup performed by this
agent). Treat the XBRL series as **absent / UNANSWERED-by-script** and re-derive the 1993-97 money series
only from the audited headers inside the held documents.

## Stored bytes

STATUS: WRITTEN 2026-09-27 (regrade pass)

`auto --cik 1045810 --from 1993-01-01 --to 2001-12-31 --max-docs 25` →
**`auto: 31 documents stored (7942444 bytes, 1094459 words), 15 UNANSWERED (counted, not nulls)`**, tool
exit code **1** = "partial (some UNANSWERED)" per `sec_intake.py`'s own exit-code contract — correct for a
partial, not a crash.

Probe comparison: **6 documents / ~2.77 MB** (probe's table) → **31 documents / 7,942,444 B**, i.e. the
S-1 lineage is now complete (S-1 + 6 S-1/A), and the 1999–2001 run (424B4, 10-K405s, DEF 14A, SC 13G, S-3,
424B2, 8-K) is on disk with exhibit-level documents.

Earliest / latest held, from `sources/sec/_MANIFEST.csv` (31 rows, all `status ok`):
first row **1998-03-06 S-1 0001012870-98-000618, 856,608 B, 122,698 words**; last rows 2001-11-30 S-3
`0001012870-01-503009` (4 docs: 39,231 + 2,422 + 566 + 43,529 B). In between, by date: S-1/A 1998-04-24
564,104 · S-1/A 1998-06-08 440,312 · S-1/A 1998-07-27 626,995 · S-1/A 1998-11-20 590,627 · S-1/A 1998-12-23
682,998 · S-1/A 1999-01-13 425,132 · S-1/A 1999-01-20 424,134 · **424B4 1999-01-22 394,333** · 10-K405
1999-04-29 214,347 · DEF 14A 1999-05-17 94,006 · SC 13G 1999-08-06 14,950 · 10-K405 2000-03-13 199,535 ·
S-3 2000-03-29 840,718 · 424B2 2000-09-19 337,729 · 8-K 2000-09-28 98,996 · SC 13G 2000-10-10 14,683 ·
10-K405 2001-04-27 (4 docs: 220,744 / 257,011 / 208,813 / 115,260) · SC 13G 2001-04-30 20,499 + 22,321 ·
8-K 2001-05-03 7,887 + 12,831 · DEF 14A 2001-06-25 84,887 + 86,236.

Are the stored bytes filings? Verified this session:
`grep -l -i "File Unavailable\|Temporarily Offline\|NoSuchKey" sources/sec/*.txt` → **0 files matched**.
Content greps: `grep -o "April 5, 1993" sources/sec/0001012870-99-000192_*.txt` (424B4) → **3 hits**;
`grep -o "inception" sources/sec/0001012870-98-000618_*.txt` (S-1) → **5 hits**. The day-level inception
statement the probe read is present in script-stored bytes.

The **15 UNANSWERED** rows (`sources/sec/_UNANSWERED.csv`, 16 lines = header + 15) are all one failure mode:
guessed document name `0001.txt` (and `0002/0003/0005/0006.txt`) resolved against
`padded-cik/nodash-dir`, `bare-cik/nodash-dir`, `bare-cik/dashed-dir` → `404 <Error><Code>NoSuchKey</Code>`
on accessions 0001012870-00-004830, -00-005003, -00-005072 (×4), 0000315066-00-001238,
0001012870-01-000269 (×4), -01-000538. **Defect, not absence:** for at least 0001012870-00-004830 and
-00-005003 the *same accession* was also stored successfully as `<accession>.txt` (see manifest), so the
UNANSWERED rows over-count real gaps — they are failed guesses about accessions that were in fact fetched.
Accessions 0001012870-00-005072, -01-000269 and -01-000538 appear **only** as UNANSWERED: genuinely not held.

## Family a verdict

STATUS: WRITTEN 2026-09-27 (regrade pass) — verdict **TIER1_CANDIDATE, unchanged**; volume and lineage completeness improve.

- **Change vs probe: none in verdict, large in coverage.** Probe family (a) = TIER1_CANDIDATE on 6 documents
  (2.77 MB) enumerated against a hand-rebuilt index; regrade = **31 documents, 7,942,444 bytes, 1,094,459
  words** stored by `auto` with the index built by the tool itself. In-window Tier-1 text was already YES and
  remains YES.
- **Earliest form and date actually held: S-1, 1998-03-06** (0001012870-98-000618, 856,608 B) — now reached by
  `auto`, not by hand.
- **Earliest form and date merely existing in the index: S-1, 1998-03-06** — the *same* accession; for Nvidia
  there is no index-only gap at the front of the window (unlike Costco, whose earliest index row 10-Q
  1994-01-05 was never stored by the script).
- Structural null re-confirmed, not inherited: the index has **zero rows before 1998-03-06**, so the 1993
  founding (inception "April 5, 1993") can only ever be registrant-retrospective in family (a). Probe's
  "one lineage" caveat (company, underwriters, KPMG as auditor of incorporated statements) survives intact.
- Family (a) **does not change the family count**: it was 1 of 5 before, it is 1 of 5 now.
- New in-window material the probe did not have and Stage 1 should now use: the 1998-11-20 and 1999-01-20
  S-1/A amendments, FY2000 and FY2001 10-K405 exhibit sets (`dex21.txt`, `dex45.txt`, `dex46.txt` — subsidiary
  and consent lists, third-party-signed), the 1999-05-17 DEF 14A, and the 2000-03-29 S-3 (840,718 B).
- Still UNTRIED inside family (a): the 3 named-but-unfetched in-window forms visible in the index — 10-Q
  (earliest 1999-06-15, none stored), SC 13G/A (2000-02-14), S-4 / S-4/A (2001-01-26 / 2001-02-13),
  10-K405/A (2001-05-25), 8-K/A, PRE 14A, RW, 8-A12B/8-A12G — plus the three accessions above. Not nulls.

## Tier

STATUS: WRITTEN 2026-09-27 (regrade pass) — **T3, unchanged; NOT re-issued, and no PROVISIONAL flag on family-(c) grounds.**

Families with in-window Tier-1 text, as measured by the probe and re-checked against this pass's scope:
- (a) filings — **YES** (31 documents, 7.94 MB, day-level inception text confirmed inside stored bytes).
- (b) web archives — **UNANSWERED** (probe: six CDX requests, HTTP 503/504, zero bodies; not re-probed here —
  this brief's scope is family (a) only). Not a null.
- (c) periodical corpora — **LEAD_ONLY, and NOT blocked by a missing query block**: `tools/queries.json`
  parses to **427 tasks across 50 companies, `nvidia` among them**, and the probe ran **17 scripted tasks /
  145 candidate rows**. Its null was *access* (HathiTrust status 0, Chronicling America HTTP 403) plus no
  budget to read a body — not config. So the "untried because of a missing harvester query block" condition
  in my brief **does not hold for this company**, and that is why the tier is not marked provisional on that
  ground (contrast `company_013_costco`, where it did hold at probe time and the tier is PROVISIONAL).
- (d) digitised corporate print — **NULL, answered** (numFound 0 for report-scoped shapes; the one item holds
  FY2005-2026).
- (e) documentary — **UNTRIED** (no scripted route exists in `tools/` for auction/museum records; not attempted).

§15.2: 1 family with in-window Tier-1 text → **T3 (register), ≤1 family, 8k words/stage, 3–4 runs**.
Family (a) movement did not change the count, so **the tier is not re-issued**; the probe's T3 stands on
stronger bytes. The probe's own **T2 upgrade condition** is unchanged and still cheap: one browser-egress
Wayback CDX answer **and** one in-window periodical body read (HathiTrust in an open window, or the Google
Books `all_pages` Maximum PC 2000-03/04 items) → 2 families → T2 (6–9 runs, 22k/stage). Nothing in this
re-grade closes or strengthens either half of that test; it only removes any doubt that family (a) is real.

Caveat kept honest: family (b) UNANSWERED and family (e) UNTRIED mean the ceiling is still not measured —
this is a statement about reach, exactly as §14 rule 6 requires.

**Tool defects observed on this pass (reported, `tools/` not edited):**
1. `facts` prints a path and writes no file; `sources/financials/` is empty.
2. UNANSWERED rows count *guessed* document names (`0001.txt` etc.) for accessions whose `<accession>.txt`
   was fetched successfully in the same run → the "15 UNANSWERED" is an over-count; a reader must reconcile
   `_UNANSWERED.csv` against `_MANIFEST.csv` before believing any gap.
3. Manifest schema drift: the pre-existing `sources/sec/_MANIFEST.csv` had header
   `accession,file,path,bytes,words,status,label`; `auto` rewrote it to
   `...,form,filingDate,url,listing`. Anything that read the old columns (my first parse) breaks.
4. 30/69 in-window rows still nameless in the index; recovery of names depends on directory-listing fallback,
   which is why `--max-docs 25` yielded 31 docs (multi-document accessions) rather than a clean cut.

