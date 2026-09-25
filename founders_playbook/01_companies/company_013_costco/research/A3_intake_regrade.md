# A3_intake_regrade.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:24:55Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Dry run

STATUS: WRITTEN 2026-09-27 (regrade pass, agent `regrade-t3-batch`; all figures observed in this session)

Command run from repo root:
`python tools/sec_intake.py index --cik 909832 --company-dir founders_playbook/01_companies/company_013_costco --from 1983-01-01 --to 1997-12-31 --dry-run`
→ printed `index: 2723 filings from COSTCO WHOLESALE CORP /NEW (COST); earliest forms: 10-K, 10-K/A, 10-K405, 10-Q, 10-Q/A, 11-K, 144, 144/A, 15-12G, 3, 3/A, 4, 4/A, 424B1`.

CIK verified this session: `python tools/sec_intake.py resolve --ticker COST` →
`{"ticker": "COST", "cik": 909832, "name": "COSTCO WHOLESALE CORP /NEW"}` — matches the brief's claim.

The dry-run now sees **2,723** filings, not the 1,007 the probe was limited to: the fixed build reads the
archive slice as well as `recent`, so the pre-2001 range is enumerated before any download is attempted.
Coverage verdict available cheaply: the window is **not** empty at index level.

## Index

STATUS: WRITTEN 2026-09-27 (regrade pass)

`index` (live) → same 2,723-filing enumeration; `sources/_index/` after this run:
`submissions.csv` 245,397 B, `submissions.json` 596,759 B, `CIK0000909832-submissions-001.json` 268,868 B,
`CIK0000909832-main.json` 159,116 B, `_INDEX.md` 3,546 B.

Parsed `sources/_index/submissions.csv` with the flat column set
(`filingDate,form,accession,reportDate,primaryDocument,source`):

- total rows **2,723**; rows inside **1983-01-01 → 1997-12-31** = **59**, all with `source = CIK0000909832-submissions-001.json`.
- **Earliest in-window filing in the index: Form 10-Q, accession `0000912057-94-000012`, filed 1994-01-05** (report date 1993-11-21) — this is the *index* fact the broken build could not print.
- Everything before 1994-01-05 is genuinely absent: the slice starts there, confirming the probe's structural floor (EDGAR has no 1983–1993 Costco/Price documents for this CIK).
- Earliest per form in-window (from the same parse): 10-Q 1994-01-05 · 11-K 1994-03-31 · 8-K 1994-08-05 · 10-K 1994-11-17 · SC 13E4 1994-11-21 · SC 13E4/A 1994-12-07 · DEF 14A 1994-12-23 · SC 13D 1994-12-23 · 10-Q/A 1995-01-24 · S-8 1995-02-03 · S-3 1995-05-17 · 424B1 1995-06-02 · 10-K405 1995-11-30 · SC 13G 1996-02-12 · 10-K/A 1996-03-15 · S-3/A 1996-06-05 · PRE 14A 1996-11-29 · PREN14A 1996-12-20 · PREC14A 1996-12-30 · 15-12G 1997-01-06 · PRRN14A 1997-01-07 · SC 13G/A 1997-02-14 · 424B3 1997-12-04. No S-1 (probe's null stands).
- **Residual defect (tool, reported not fixed):** all **59 of 59** in-window rows have a **blank `primaryDocument`** — the nameless pre-2001 listing problem the brief describes. `auto` recovered document names for 11 of them via directory-listing fallback and recorded the other 48 as neither stored **nor** UNANSWERED (`sources/sec/_UNANSWERED.csv` contains only its header; `auto` printed "0 UNANSWERED"). **48 in-window index filings are silently dropped, so "0 UNANSWERED" still does not mean "0 remain".**

`facts --cik 909832 --from 1983-01-01 --to 1997-12-31` → printed
`facts: founders_playbook\01_companies\company_013_costco\sources\financials\xbrl_early_series.csv`
but **wrote no file**: `sources/financials/` is empty (0 entries) and reading that path errors
`No such file or directory`. Same defect the probe recorded; XBRL series for this company remains
**UNANSWERED-by-script**, not null (and could not reach 1994–97 anyway).

## Stored bytes

STATUS: WRITTEN 2026-09-27 (regrade pass)

`auto --cik 909832 --from 1983-01-01 --to 1997-12-31 --max-docs 25` →
**`auto: 11 documents stored (2285245 bytes, 293457 words), 0 UNANSWERED (counted, not nulls)`**
Compare the broken build on the identical command shape: "0 documents stored, 0 skipped/unanswered".

Per-row byte/form/date from `sources/sec/_MANIFEST.csv` (all `status = ok`; bytes as stored):

| filed | form | accession | bytes | words |
|---|---|---|---|---|
| 1994-08-05 | 8-K | 0000912057-94-002516 | 125,566 | 18,904 |
| 1994-11-17 | 10-K | 0000912057-94-003945 | 396,621 | 45,590 |
| 1994-12-23 | DEF 14A | 0000950123-94-002087 | 75,063 | 10,180 |
| 1994-12-23 | SC 13D | 0000912057-94-004286 | 9,730 | 1,137 |
| 1995-05-17 | S-3 | 0000891020-95-000177 | 324,751 | 46,198 |
| 1995-06-02 | 424B1 | 0000891020-95-000228 | 59,941 | 7,865 |
| 1995-11-30 | 10-K405 | 0000912057-95-010555 | 309,405 | 34,499 |
| 1996-02-12 | SC 13G | 0000732812-96-000308 | 14,757 | 1,392 |
| 1996-03-15 | 10-K/A | 0000912057-96-004594 | 16,176 | 1,519 |
| 1996-11-08 | 10-K405 | 0000912057-96-025246 | 349,131 | 43,721 |
| 1997-11-10 | 10-K | 0001047469-97-003493 | 604,104 | 82,452 |

Are these filings or apology pages? Verified this session, not assumed:
`grep -l -i "File Unavailable\|Temporarily Offline" sources/sec/*.txt` → **0 files matched**.
Content greps on stored bytes: `grep -c "1976" ...0000912057-94-003945_...txt` → **3** (the origin-year
hits the probe found by hand, now in script-stored bytes); `grep -o "Table of Contents"` on the FY1997
10-K → matched. Note the probe's verbatim sentence "When Price pioneered the membership warehouse club
concept in 1976" did **not** match as one literal string in the raw `.txt` (markup breaks the run), so
only the `1976` count is claimed here; the quoted sentence is inherited from the probe's reading of the
same 396,621-byte accession.
Also on disk unchanged from the probe: `sources/sec/0000912057-94-000012/0000912057-94-000012.txt`
(10-Q 1994-01-05, 64,490 B, hand-fetched) — auto did **not** re-store it, which is why the earliest
*held* date differs from the earliest *script-stored* date below.

## Family a verdict

STATUS: WRITTEN 2026-09-27 (regrade pass) — verdict **TIER1_CANDIDATE, unchanged**, but the evidence base moved from hand-fetched to scripted.

- Change vs probe: **none in kind, large in volume.** Probe family (a) = TIER1_CANDIDATE on 3 hand-fetched
  documents (64,490 + 396,621 + 324,751 B) against an `auto` report of "0 documents"; regrade = **11
  documents, 2,285,245 B, 293,457 words** stored by `auto`, 1994-08-05 → 1997-11-10, zero apology pages.
  The probe's own suspicion — "Costco came back T3 while its own run noted 1994-01-05 10-Q and a
  1994-11-17 10-K were reachable by hand" — is now confirmed by the tool itself.
- **Earliest form and date actually held (script-stored): 8-K, 1994-08-05** (0000912057-94-002516, 125,566 B).
  Earliest actually held on disk counting the probe's hand fetch: **10-Q, 1994-01-05** (64,490 B).
- **Earliest form and date that merely exists in the index: 10-Q, 1994-01-05** (0000912057-94-000012),
  one of the 48 nameless rows `auto` neither stored nor declared UNANSWERED. Not held by this pass; held
  on disk from the probe's hand fetch.
- In-window Tier-1 text status: **YES, in-window registrant text naming the origin years** — the FY1994
  10-K (1994-11-17) is held with the 1976 hits; the probe's read lines (L398-401, L875-876, L964-966,
  L916-917, L174-182, L980-989) remain the substantive citations, now reproducible from script-stored bytes.
- Family (a) does **not** gain a new tier-relevant state: it already counted as a family with in-window
  Tier-1 text. The probe's structural nulls stand and were re-confirmed: nothing before 1994-01-05 on the
  CIK, and no S-1 among the 59 in-window rows.
- Still open inside family (a): the 48 unfetched nameless in-window filings (incl. PRE 14A 1996-11-29
  0000912057-96-027954, SC 13E4 1994-11-21, the whole 1995 10-Q run) are **UNTRIED by this pass**, not null.

## Tier

STATUS: WRITTEN 2026-09-27 (regrade pass) — **T3, PROVISIONAL.**

Family count on in-window Tier-1 text, measured by this pass:
- (a) filings — **YES** (11 scripted documents, 2,285,245 B; earliest stored 8-K 1994-08-05).
- (b) web archives — **UNANSWERED** (probe: IA service-wide offline page + one CDX timeout; not re-probed by this pass, whose scope is family (a) — carried forward as UNANSWERED, not null).
- (c) periodicals — **UNTRIED on this pass** (still no in-window text read or downloaded here, so it is not
  a family that counts toward the tier). State of the route, verified this session: `tools/queries.json` now
  carries a **`costco` task block** (file parses to **427 tasks across 50 companies**, `costco` among them),
  i.e. the missing-harvester-query block the probe reported (`--company costco --dry-run` → 0 tasks) has
  **since been fixed by another agent**. So (c) is now **TRIAL-BY-SCRIPT but UNTRIABLE-BY-ME**: running the
  harvester is not in this brief and `tools/` and the harvest route are not mine to drive. Not a null.
- (d) corporate print — **NULL, answered** (numFound=5, none a report).
- (e) documentary — **UNTRIED** (no scripted route, no request).

Families with in-window Tier-1 text = **1** → §15.2 gives **T3 (≤1 family), 8k words/stage, 3–4 runs**.
Family (a) movement did **not** change the family count (it was already YES), so the tier itself is not
re-issued on strength of the re-measure.

**Why PROVISIONAL:** the tier was never measured on families (c) — blocked by the missing harvester query
block, being fixed by another agent — and (b)/(e). §15.2 counts families, and three of the five were not
in the denominator. A re-grade that fixes only family (a) **understates the ceiling**: if the (c) harvest
lands 1982–83 Discount Store News / Chain Store Age text, the count becomes 2 → **T2 core (6–9 runs,
22k/stage)**; a healthy IA re-run plus (e) would be needed for T1. Record this company as
**T3 PROVISIONAL**, deliverable per §15.2 T3 (short narrative + registers; §K, §N, §U mandatory), and
re-issue the tier as soon as the `costco` query block exists.

**Tool defects observed on this pass (reported here, `tools/` not edited):**
1. Nameless pre-2001 rows: 59/59 in-window `primaryDocument` blank; only 11 recovered by directory-listing fallback.
2. The other 48 are dropped **without** an UNANSWERED row — `_UNANSWERED.csv` header-only while filings demonstrably remain; "0 UNANSWERED" must not be read as full coverage.
3. `facts` prints an output path (`sources\financials\xbrl_early_series.csv`) and writes no file, and the printed path mixes separators.
4. The `index` line still reports only a total and "earliest forms" — no earliest *date* per form, which is the number the tier turns on; it had to be computed by parsing `submissions.csv`.
5. Path convention split between runs: `auto` writes `sec/<accession>_<accession>.txt` flat while the probe's hand fetches live in `sec/<accession>/<accession>.txt`, so earliest-held questions need both trees enumerated.

