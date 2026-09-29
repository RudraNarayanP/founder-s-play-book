# A_chronology_feasibility.md — Boeing (rank 47) Stage-1 PROBE

Company dir: `founders_playbook/01_companies/company_047_boeing`. Owner: `probe-boeing`
(`scaffold.py claim --path … --agent probe-boeing`, run first; the positional
`auto "Boeing"` form in the dispatch brief is not accepted — see *Defects*).
Origin window under test: **1916-01-01 → 1940-12-31**, verbatim from `tools/harvest_mine.py:71`
(`"boeing": ("1916-01-01", "1940-12-31")`).
Web budget consumed: **0 WebSearch / 0 WebFetch**. Every count below carries the command that
produced it. `## Untried` is a section, not a footnote.

---

## Verdict

**Stage 1 (1916-01-01 → 1940-12-31): TIER 2 (core).** Two of the five families return in-window
Tier-1 text — **(d) digitised corporate print** and **(c) periodical / digitised government-print
corpora** — one returns **nothing with a named perimeter** (a), and two are **untried** (b, e).
Chronicling America is **unanswered**, not null (§14 rule 6 as amended by RD-097: a depth verdict
needs all five families searched, and an untried family may not be reported as a null).

**I would not claim T1 for Stage 1, and I would not claim T3 either.** The T2 grade is a floor
sitting on a live upgrade path, not a ceiling: the two untried families are precisely the two that
carry 1916-1925 material for an aircraft company (auction/museum documentary records; air-regulatory
and patent files), and one of them plausibly holds the only surviving first-decade document.

The probe's honest headline is **not** "the archive is empty before 1994". It is: **Boeing's origin
window has in-window primary text, and that text contradicts the folk founding date at the level of
which legal entity it attaches 1916 to.** See *Load-bearing open questions*.

| stage | window used for this measurement | tier | §15.2 budget implied |
|---|---|---|---|
| **Stage 1** | 1916-01-01 → 1940-12-31 (repo-recorded) | **T2 core** | 6–9 agent runs, 22k words/stage |
| **Stage 2** | 1941-01-01 → 1993-12-31 (**probe-proposed**, RD-112) | **T3 register, PROVISIONAL** | 3–4 runs, 8k words/stage |
| **Stage 3** | 1994-01-01 → 2026-09-01 (**probe-proposed**) | **T2 core, PROVISIONAL** | 6–9 runs, 22k words/stage |

RD-112 requires naming which window a tier was measured against, and there is **no Stage-2 or Stage-3
window recorded for this company anywhere in the repo** (verified: `grep -n "boeing" tools/harvest_mine.py`
returns one line, one range; `00_universe/fortune_top_50_2026.csv` carries no stage fields — header
enumerated: `rank, company, revenue_usd_millions, revenue_fiscal_year, profit_usd_millions, hq_city,
hq_state, fortune_industry, universe_source_url, verified_by_second_source, confidence, notes`).
So Stage 2/3 windows above are **cut on measured corpus boundaries, not on company history**:
1994-03-15 is the observed EDGAR floor for CIK 0000012927 and 1978 is the last year of the held
annual-report run. Whoever assembles Stage 2 or 3 may re-cut these spans, but must **re-measure the
tier against the new span** rather than inherit the number.

---

## What is in-window and held

Held corpus at close-out (command: `python - <<` walk over `sources/`, excluding `.meta.json`):

| folder | files | bytes | what it is |
|---|---|---|---|
| `sources/sec/` | 37 documents (+37 sidecars) | 8,033,015 | EDGAR filings, **1994-03-15 → 2002-03-22** |
| `sources/_index/` | 7 | 2,477,941 | submissions enumeration, 4,026 filings |
| `sources/periodicals/` | 5 (+5 sidecars) | 5,963,131 | 4 Internet Archive OCR layers, all in-window or mixed |
| `sources/corporate_print/` | 7 (+7 sidecars) | **137,518** | **Boeing Airplane Company annual reports, FY1934-FY1940** |
| **total** | | **16,650,160** | |

**In-window (1916-1940) and actually held, by document:**

1. `sources/corporate_print/boeing1934_djvu.txt` — 12,430 B — *Boeing Airplane Company and
   Subsidiary Companies, annual report*, with a letter "To the Stockholders of Boeing Airplane
   Company" as of **December 31, 1934**.
2. `…/boeing1934a_djvu.txt` — 6,122 B; `boeing1935` — 16,394 B; `boeing1937` — 20,844 B;
   `boeing1938` — 23,332 B; `boeing1939` — 25,088 B; **`boeing1940` — 33,308 B**.
3. `sources/periodicals/dc_circ_1934_6287_boeng_air_transp_v_farley_djvu.txt` — 625,596 B —
   *Boeing Air Transport v. Farley* (D.C. Cir. 1934) record, containing the Postmaster General's
   1927 air-mail bid and award papers.
4. `sources/periodicals/micro_IA40386008_0350_djvu.txt` — 493,539 B — *Edelman v. Boeing Air
   Transport, Inc.*, 289 U.S. 249 (1933) record.
5. Two **negative** holds, kept as evidence of what the sweep covered:
   `sim_aviation-week-space-technology_1916-08-01_1_1_djvu.txt` (149,954 B) and
   `munitionsindustr1114unit_djvu.txt` (4,594,867 B) — see (c).

**Entity-naming counts across the 12 held in-window text files** (command: the `re.escape` count
loop over `corporate_print/*.txt` + `periodicals/*.txt`, case-insensitive substring):
`Boeing Air Transport` **145**, `Boeing Airplane Company` **61**, `Boeing Aircraft Company` **51**,
`"since 1916"` **1**, `W. E. Boeing` **5** (all in the 1934 court record), `Hubbard` 19.
Two cautions written into this dossier rather than hidden: `Westhoff` and `Pacific Airplane` count
**0** in every held byte, and the raw counters for `William` (497), `Treat` (86) and `1917` (408) are
**substring noise**, not namings — 403 of the `William` hits and all 406 `1917` hits sit in the
munitions volume that contains **zero** occurrences of "Boeing". This is RD-124's rule applied to my
own counting: a matched string is a lead; only a read line is evidence.

---

## Family (a) — filings (EDGAR): RETURNS NOTHING WITH PERIMETER for Stage 1

Route run (the brief's positional form is rejected by the tool; working form is flag-based):

```
python tools/sec_intake.py auto --ticker BA \
  --company-dir founders_playbook/01_companies/company_047_boeing
```

Tool's own reported state (from the run's stdout, retained at `/tmp/sec_boeing.log`, and
`sources/sec/_RUN.json`):

- **Registrant `BOEING CO`, CIK 0000012927**, tickers `['BA','BA-PA']`; `index: registrant guard = ok
  -- slug token(s) ['boeing'] match registrant 'BOEING CO'`. RD-098's wrong-CIK clobber did not bite.
- **4,026 filings enumerated**; **0 rows dropped for no accession, 85 without primaryDocument**.
- **Earliest indexed filing: 1994-03-15 (DEF 14A)**; latest 2026-09-01
  (command: `python -c` min/max over `sources/_index/submissions_CIK0000012927.csv`, header
  enumerated first: `filingDate, form, accession, reportDate, primaryDocument, source`).
- **Rows dated before 1941-01-01: 0.** Rows before 1995-01-01: **7**, all 1994
  (`1994-03-15 DEF 14A, 1994-03-17 10-K, 1994-03-22 S-8, 1994-05-13 10-Q, 1994-06-28 11-K,
  1994-08-09 10-Q, 1994-11-07 10-Q`). **This is the §14.6 floor measured on Boeing, and it is a
  perimeter with a date, not a wall without one.**
- **No S-1 exists.** Zero rows with form `S-1` in 4,026; the earliest registration-type forms are
  `S-4` (1996-10-29, 1997-06-20, 1998-05-13 …), which are merger forms, not origin documents.
- **Held vs indexed:** 37 documents / **8,033,015 B** / 936,454 words stored, against 4,026 indexed.
  `auto` reported: `360 accessions in window, 27 directories opened, 41 document slots planned,
  40 kept under --max-docs 40, 1 skipped past the cut` and the identity check
  `stored(37) + unanswered(4) + skipped(40) = 81 vs attempted(81) -> OK`.
  `_MANIFEST.csv` is the held list (37 rows; earliest held filingDate **1994-03-15**, latest
  **2002-03-22**; command: header-enumerated read of `sources/sec/_MANIFEST.csv`).
- **4 UNANSWERED, which are not nulls:** three document slots returned S3 `NoSuchKey` 404s
  (`0000315066-00-000163/0001.txt`, `0000012927-01-000004/0001.txt`, `/0002.txt`) and the run
  reported `UNANSWERED NOT-ENUMERATED: 333 in-window filings were never listed because --max-docs 40
  was reached`. So 333 accessions' documents are **unknown to this run**, not absent.
- `python tools/sec_intake.py selftest` → **`selftest: 42 checks, 0 failing`** (re-run and verified
  this pass, not inherited from the brief).

## Family (b) — web archives: UNTRIED

No script in this repository reaches the Wayback CDX API. Command that establishes it:
`grep -rn "wayback\|cdx\|web.archive" tools/*.py` → the only hit is a *comment*
(`tools/periodical_harvest.py:6`). Web budget for this pass was 0. §14.6 puts the family's floor in
the mid-1990s, so this family cannot bear on Stage 1 and bears on Stage 3 only — see *Untried* #1.

## Family (c) — periodical corpora: RETURNS for Stage 1, with two content-verified nulls

`python tools/harvest_mine.py --company boeing --limit 8` printed **`{}`**, exited 0 and **wrote no
`research/A4_harvest_mine.md`** — because all 8 Boeing rows in the candidate index have an empty
`item_id` (see *Defects* D-4). The family therefore had to be worked directly:

```
python tools/ia_text.py search --q '<entity phrase>' --rows N --insecure
python tools/ia_text.py fetch  --id <identifier> --company-dir <this company> --max-mb M --insecure
```

**Match classes actually obtained, read as RD-124 requires:**

| item | held bytes | entity result | class |
|---|---|---|---|
| `dc_circ_1934_6287_boeng_air_transp_v_farley` | 625,596 | `Boeing Air Transport` ×112, `Boeing Airplane Company` ×16, `W. E. BOEING` signature blocks ×5, one sworn affidavit | **TIER1_CANDIDATE_TEXT** |
| `micro_IA40386008_0350` (Edelman, 1933) | 493,539 | `Boeing Air Transport` ×33; "deliver the mail to the employee of the Boeing Company" | **TIER1_CANDIDATE_TEXT** |
| `munitionsindustr1114unit` (Senate, 1934) | 4,594,867 | **`Boeing` ×0, `Seattle` ×0** | **NULL — content-verified** |
| `sim_aviation-week-space-technology_1916-08-01_1_1` | 149,954 | **`boeing` ×0** in 149,286 chars | **NULL — content-verified** |
| `boeingairplanecompanyannualreports` (item-level layer) | 99,175 | 1976 report only; `1916/1934/1935/1937/1940` each ×0 | **BARE_WORD_MATCH** — out-of-window |

The two NULLs are **not** a null about the world, and the controls prove the text layers are live, so
the absence is about the item, not about the reader: in the munitions volume `Senate` occurs 68×,
`aircraft` 16×, `Wright` 10×, `Curtiss` 1×; in the 1916 *Aviation* issue the string "August 1, 1916"
occurs repeatedly. **Perimeter:** of the 47 texts items IA's metadata returned for
`Boeing AND mediatype:texts AND year:[1916 TO 1940]`, this pass opened **3**.

**A methodological finding that matters fleet-wide: Internet Archive `advancedsearch` matches
METADATA fields, not full text.** Proof by experiment: the 1916 *Aviation* issue was returned by a
query containing "Boeing" and its held OCR layer contains **zero** occurrences of "Boeing". Every
`numFound` figure in this dossier is therefore a *lead count*, never a naming count. It is also why
`ia_text.py`'s own `classify()` stamped that file `TIER1_CANDIDATE` (see *Defects* D-3).

## Family (d) — digitised corporate print / annual reports: RETURNS — this is the family that moved Boeing, as it moved Walmart

Internet Archive item `boeingairplanecompanyannualreports`, titled *"Boeing Airplane Company Annual
Reports: 1934–1935, 1937–1978"*, description "The annual financial reports for the Boeing Airplane
Company from 1934, 1935, and from 1937 through 1978". `ia_text.py fetch` on it returned **only** the
item-level `<id>_djvu.txt` — the **1976** report (99,175 B, 0 hits for any in-window year), which
reads exactly like "the corporate print is out of window". Enumerating the item's file list showed
**46 per-year `*_djvu.txt` layers**, years 1934, 1935, 1937-1978 (no 1936; extra parts 1934a, 1941a).
Seven in-window layers were then downloaded with provenance sidecars, **137,518 B**, into
`sources/corporate_print/` (D-2; the fetch used the module's own `get()`/`ocr_url()`, and each
sidecar's `via` field records that this is the per-file route, not `ia_text fetch`).

What those bytes say, quoted (all reads are from `sources/corporate_print/`):

- **FY1934, L146-152:** *"Submitted herewith are the consolidated financial statements of your
  corporation and its subsidiary companies as of December 31, 1934. The profit and loss account dates
  from September 1, 1934, at which time your company acquired certain of the assets of the United
  Aircraft & Transport Corporation. It will be recalled that **your company was formed for the purpose
  of acquiring these assets upon the dissolution of United Aircraft & Transport Corporation.**"*
- **FY1934, L154-160:** *"Your company owns 100% of the stock of Boeing Aircraft Company and of The
  Stearman Aircraft Company. … **Boeing Aircraft Company, a Washington corporation, has been engaged
  in the manufacture of aircraft since 1916.** … Its plant is located at Seattle, Washington."*
- **FY1935, L794-802 (page headed "PROGRESS"):** *"THE FIRST BOEING PLANE— A TWO-PLACE TRAINER
  SEAPLANE. … 1916"*, then *"BOEING FLYING BOAT OPERATED IN THE FIRST U. S. CONTRACT AIR MAIL
  SERVICE"*, *"MB-3A—ARMY PURSUIT PLANE. 1921-22"*, *"FB-5 … 1926-27"*, *"40-B4—FOUR-PASSENGER MAIL
  PLANE. 1929"*, *"80-A—TRI-MOTORED … PIONEER PULLMAN OF THE AIR"* … — a company-authored model
  chronology beginning at 1916.

**Lineage discipline (§5 filing-lineage rule, RD-097):** both 1916 statements are the same
company's own reports — **one lineage, two document years.** Strength: *company self-narrative*.
It is not two corroborations, and it is not third-party. Caveat on the 1935 page: the caption→year
pairing is inferred from OCR reading order and two years render garbled (`1 Q 1 Q` for the 1919
flying-boat entry, `199 9 If)` for the 80-A), so **the chronology's later rungs are not quotable from
these bytes.**

## Family (e) — auction or museum documentary records: UNTRIED

No scripted route exists — `queries.json`'s five Boeing tasks use families
`chronicling_america, internet_archive, hathitrust, google_books, corporate_print` only (verified by
walking the JSON: 8 boeing tasks, indices 387-394). The nearest thing to an attempt this pass made is
a metadata sweep for archival vocabulary on IA — `"Pacific Aero Physics"` **0**, `"William E. Boeing"
papers` **0**, `"Boeing" "flight log" 1910-1930` **0**, `"Boeing" museum collection aircraft 1919`
**0**, `"B&W" seaplane Boeing 1916` **0**, `"Pacific Aero Products"` → 5 rows, all post-2019 annual
reports (loose AND matching, not a naming). **That is a search of the wrong catalogue, not a null in
the world**: auction and museum documentary records were never reached, and they are the family that
carries founders' papers, logbooks and stock certificates for pre-1930 companies. See *Untried* #2.

## Fifth avenue — air-registry, aeronautical authority, NLRB and patent records: PARTLY OPENED (by accident of the IA route)

This avenue produced real in-window material through Internet Archive's government-document scans,
which is why it is reported as partly opened rather than untried:

- **1934 D.C. Circuit record** contains the **Postmaster General's air-mail contract file for Route
  A.M. 18**, which is the regulatory record this company's first decade turns on: bids "submitted and
  opened … on **January 15, 1927**: (a) **Boeing Airplane Company and Edward Hubbard**, Georgetown
  Station, Seattle, Washington, at the rate of **$1.50 per pound** for the first thousand miles and
  15 cents per pound for each additional 100 miles; (b) Western Air Express, Inc., $2.24 …;
  (c) Stout Air Services, Inc., $2.64 …; (d) Columbia Air Liners, $4.47 per pound" (L376-393); and
  "on or about **February 1, 1927**, the then Postmaster General … awarded the contract … to Boeing
  Airplane Company and Edward Hubbard **as being the lowest qualified bidder**", with a
  **$500,000** performance bond (L395-408, OCR renders the bond `500,0Q0`).
- Same record, **sworn by the founder**: L1916 *"I, W. E. Boeing, as President of Boeing Air
  Transport, Inc., a corporation, making this affidavit for and in behalf of said corporation…"*,
  plus signature blocks `By W. E. BOEING` at L1707, L1741, L1904 and a sealed L1931.
- **1933 Supreme Court record** (`Edelman v. Boeing Air Transport, Inc.`) naming the carrier 33×.

**Still untried inside this avenue:** Aeronautics Branch / CAB series, NLRB case registers, and patent
records — commands in *Untried* #3-5.

## Chronicling America — the route itself, per RD-128

All 8 Boeing rows in the fleet candidate index are **`classification=UNANSWERED` with `http_status`
empty and `item_id` empty** (command: the `csv.DictReader` dump over
`founders_playbook/00_universe/harvest/candidates.csv`, header enumerated:
`company, source_family, query, item_id, title, date_or_issue, url, snippet_or_hitcount, http_status,
classification, retrieved_at`; index total **2,598 rows**). So **the query block is thin — a null
from it is not a null about the world**, and there is nothing here to call TIER1 or BARE_WORD at all.

`python tools/ca_endpoint_probe.py --help` executed the probe, which reported **7 of 7 endpoint shapes
`CHALLENGED 403 Cloudflare bot challenge`** from this machine and printed
`wrote founders_playbook\00_universe\harvest\_CA_ENDPOINT_TEST.md`. Two consequences, stated plainly:

1. **CA remains UNANSWERED for Boeing.** RD-128 established that the nightly route 404s from CI (a
   wrong path, fixable) and that 403-from-here cannot discriminate a path; the discriminating verdict
   has to come from CI egress and has not landed.
2. **I overwrote a shared instruction-layer file with a local-egress result** by running the wired
   tool. Its new mtime is this run's (2026-09-29T18:05:27Z). Nothing was deleted and I did not edit
   `tools/`, but the nightly run must be allowed to re-establish it. Recorded here so no later reader
   mistakes that file for a CI verdict.

---

## Load-bearing open questions — as the held bytes actually leave them

1. **Founding date and founding act.** **UNKNOWN**, and the corpus does not merely under-determine it,
   it **splits it in two**: the FY1934 report says *this* company (Boeing Airplane Company, the
   addressee, CIK 12927's namesake) "was formed for the purpose of acquiring these assets" with an
   account "dating from September 1, 1934", while "since 1916" is attached to a **different legal
   person — "Boeing Aircraft Company, a Washington corporation"** held 100% by the first. So the
   held in-window documents support **1934 as the registrant's own formation** and **1916 as the
   predecessor operating company's** — one company-lineage, two entities. No 1916-1925 document of any
   family is held, so the founding **day**, the founding **instrument**, and the original **name**
   remain UNKNOWN. Nothing in `candidates.csv`, `sources/` or EDGAR names a July 15, 1916 date;
   `grep`-equivalent: the `1916` counts above (`since 1916` = 1 corpus-wide).
2. **Who is credited by which document.** Company self-narrative (FY1934, FY1935) credits a
   **corporate** origin with no personal name. **Third-party judicial text credits a person and a
   partnership**: the 1927 mail contract was awarded to "**Boeing Airplane Company and Edward
   Hubbard**", and by 1933-34 the carrier's president swearing affidavits is "**W. E. Boeing**".
   **`Westhoff` occurs zero times in every held byte** and both `Pacific Airplane` /
   `Pacific Aero Physics` returned zero IA metadata rows — so the co-builder and the 1916 entity name
   are entirely absent from held evidence, and **any chronology that names them is importing
   folklore, not our corpus** (§14 rule 8).
3. **First real experiment.** **UNKNOWN.** The nearest held thing is a 1935 commemorative caption
   ("THE FIRST BOEING PLANE— A TWO-PLACE TRAINER SEAPLANE / 1916"), which is a retrospective picture
   page ~19 years after the fact, with an OCR-inferred caption↔year pairing. Not an experiment
   account; usable only as *the company's own 1935 claim about 1916*.
4. **First repeatable validation.** **This one is answerable, and answerable from third-party
   paper**: a competitive federal contract, priced against three named rivals, awarded "on or about
   February 1, 1927" to Boeing Airplane Company and Edward Hubbard "as being the lowest qualified
   bidder", with a $500,000 performance bond — and operated: the 1933 record's affidavit evidence
   describes mail actually handled by "the Boeing Company" on the route. This is the strongest
   load-bearing fact the probe produced and it is **not** company self-narrative.
5. **First incurred failure.** Only candidate in held bytes is corporate-performance negative rather
   than operational: FY1934's account of **Boeing Aircraft of Canada** — "practically dormant during
   the period under review. Little or no aircraft work has been done and the business enjoyed has
   been largely repairs of small boats, fishing craft and other types of marine work" (L161-167).
   The litigation in which *Boeing Air Transport* is the **appellant** losing below (D.C. Cir. 1934)
   is a second failure-shaped structure in-window. Neither has been read through to a finding.
   **No sweep for 1916-1940 failures has been done.**

## Conflicts the registers must carry

- **C-1 (blocking for Stage 1's §B):** 1934 formation vs 1916 "since" — same document, adjacent
  paragraphs, different entities. Do not resolve by picking the older date.
- **C-2:** 1916 appears in held bytes exactly twice, both in the company's own reports (FY1934 L158,
  FY1935 L802) → **one lineage**; the "×2" must not be booked as two independent corroborations.
- **C-3:** the only "1916" in the 1934 court record is a **citation decoy** — *Hulton v. Hulton*
  (1916) 2 K.B. 642 — and the "1919"s are *Chicago & N.W. R. Co. v. Ochs*, 249 U.S. 416 (1919).
  A year-string match in a legal file is not a company date (RD-124's lesson in a new corpus).

## Defects observed on this pass (recorded, not routed around silently)

- **D-1 (dispatch brief).** `python tools/sec_intake.py auto "Boeing" --company-dir …` exits 2:
  `unrecognized arguments: Boeing`. Working form is `auto --ticker BA --company-dir …`. Briefs should
  carry the flag form for every company.
- **D-2 (`ia_text.py fetch`, highest-cost defect found).** For a **multi-file** IA item, `fetch()`
  resolves only the item-level `<id>_djvu.txt` and never enumerates per-file layers. On Boeing that
  delivered the **1976** report for an item whose 1934-1978 per-year layers were sitting in the same
  item — i.e. the tool manufactures a false "corporate print is out of window". A reader who trusted
  `grep` after `fetch` would have graded family (d) NULL. RD-127's class: an assumed file shape
  producing an absence claim.
- **D-3 (`ia_text.py classify`).** `classify()` returns `TIER1_CANDIDATE` on *any* regex hit, so a
  file with 0 occurrences of the company word was stamped TIER1 on 40 date-string matches. The
  RD-124 entity/identity-word logic exists in `harvest_mine.py` and **not** here; the tier classes in
  this dossier were therefore produced by my own counted reads, not by `classify()`.
- **D-4 (`harvest_mine.py`).** `--company boeing --limit 8` printed `{}`, exited 0, and wrote **no**
  `research/A4_harvest_mine.md`, because the 8 candidate rows have empty `item_id`. A no-op that
  prints `{}` reads like "mined, nothing found"; it should print the reason and the count of
  unmineable rows.
- **D-5 (selftest).** `sec_intake.py selftest` = **42/0**; nothing bit this pass (guard = ok,
  identity check OK, nameless rows 0). No intake defect to report beyond D-1's argument shape.

## Untried

Each item is a search **never run**, not a null. Commands are for the orchestrator (they need a web
call budget this pass did not have).

1. **Family (b) web archives** — no tool in `tools/` reaches CDX. Command:
   `curl -s "http://web.archive.org/cdx/search/cdx?url=boeing.com&output=json&limit=5&from=1996&to=1999"`.
   Bears on Stage 3 only; expected floor mid-1990s.
2. **Family (e) auction / museum documentary records** — no source-family exists in `queries.json`.
   Command once one is added: `python tools/periodical_harvest.py --company boeing --source-family
   auction --max-requests 12 --out /tmp/boeing_auction`. Target: the 1916-1929 paper class (Boeing /
   Westhoff correspondence, B&W seaplane logs, original stock certificates of Pacific Airplane and
   Boeing Airplane Company) — **the single route most likely to change the Stage-1 verdict.**
3. **Aeronautical-authority series** — Aeronautics Branch / ICC / CAB annual and contract reports,
   1926-1938, which should carry the A.M. 18 award file independently of the litigation copy.
   Command: `python tools/ia_text.py search --q '"Aeronautics Branch" annual report commerce 1927'
   --rows 10 --insecure` then `fetch` + count "Boeing" **per held byte** (not per metadata hit).
4. **NLRB case registers** — no route from here. Command: `python tools/ia_text.py search --q '"Boeing
   Airplane Company" NLRB decisions 1935-1940' --rows 10 --insecure`.
5. **Patent records** — no route from here. Command: `curl -s
   "https://search.patentsview.org/api/v1/query/?q=%7B%22where%22:%7B%22inventor_last_name%22:%22Boeing%22%7D%7D"`
   (1 request; establishes whether a first-decade inventor record exists at all).
6. **The 44 unopened in-window IA items** — `python tools/ia_text.py mine --q 'Boeing AND
   mediatype:texts AND year:[1916 TO 1940]' --pattern "Boeing Airplane|Boeing Air Transport|Pacific
   Airplane|Westhoff|Hubbard" --company-dir
   founders_playbook/01_companies/company_047_boeing --max-mb 25 --insecure`. Note: `mine` fetches at
   most `min(rows,8)` items, so this needs 6 invocations to clear the 47.
7. **The remaining 39 corporate-print layers (1941-1978) of the same item** — the same per-file route
   used for D-2, changing the year list to `['1941','1941a','1942',…,'1978']`. This is the single
   cheapest move on the board for **Stage 2**, which is currently graded T3 only because that sweep
   has not been run.
8. **HathiTrust and Google Books for Boeing** — 1 candidate row each in `candidates.csv`, both
   UNANSWERED with no item id. Commands: `python tools/periodical_harvest.py --company boeing
   --source-family hathitrust --max-requests 8` (then read the bodies, per RD-127's finding that four
   HathiTrust bodies already on disk had never been opened).
9. **Chronicling America** — awaiting the CI verdict from `tools/ca_endpoint_probe.py` in the nightly
   workflow; not re-runnable to a verdict from this machine (7/7 403).

## Gate run at close

```
python tools/gates.py --company-dir founders_playbook/01_companies/company_047_boeing \
  --checks csv,keys --fail-on substantive
```

Result: **Findings 2 | Passes 0**, exit code 0, and both findings are coverage-only —
`coverage/registers` ("no register CSVs at root or research/ -- csv/anchors gates DID NOT RUN") and
`coverage/narrative` ("no stage_*.md volumes found"). The gate's own footer says these are
"expected for a freshly probed company, and NOT failing the exit code unless --fail-on all".
**This is not a passing gate and must not be reported as one**; it is the pre-authoring state.
The same run counted **49 source documents**, which reconciles exactly with this probe's own tally
(37 SEC + 5 periodical + 7 corporate-print = 49), so the intake is fully enumerated.

## Coverage note — what this pass did not examine

Did not read the 37 stored SEC documents' contents (they post-date Stage 1 by 54 years); did not open
the 4.59 MB munitions volume beyond the counted greps and control words; sampled 2 of 47 in-window IA
text items and 3 per-file corporate-print layers of 7 held (all 7 were held, 3 read in detail); did
not enumerate IA items past `rows=6` for any query; did not check whether the `1934a` part duplicates
`1934`; wrote nothing outside `company_047_boeing/` except the side effect disclosed under Chronicling
America; created no volume, no registers, no certification, and no `sources.csv`/`conflicts.csv`.
