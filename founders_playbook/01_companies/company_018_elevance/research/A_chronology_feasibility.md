# A_chronology_feasibility.md

# A_chronology_feasibility.md — Elevance Health, Inc. (Fortune rank 18) — Stage-1 feasibility PROBE

Owner: `probe-elevance` (claim released at close, see §10). Built on bytes already under `sources/` plus
two scripted `sec_intake.py` routes. **Web calls made by this agent: 0.** No register row, source id, or
volume was written; nothing under `sources/` was deleted, moved or renamed. `harvest_mine.py` and
`periodical_harvest.py` were NOT run (fleet lanes own those files tonight) — the mine output read here is
`research/A4_harvest_mine.md` (re-read in full before quoting) and `sources/harvest_mine/_index.json`.

Company / registrant as established before any window is judged:
EDGAR **CIK 0001156039**, current name **Elevance Health, Inc.**, ticker ELV. EDGAR's own former-name list on
that single CIK: `Anthem, Inc.`, `WELLPOINT, INC`, `WELLPOINT INC`, `ANTHEM INC`
(`sources/_index/_registrant_CIK0001156039.json` l.9-14) — **names without dates**. The registrant's own
first stored filing prints its cover as `ANTHEM, INC.` / `Indiana` / `120 Monument Circle, Indianapolis,
Indiana 46204` (`sources/sec/0000950130-01-503971_ds1.txt` l.29-39).

## 1. Verdict (one line per stage, RD-112)

| stage (PROPOSED window) | tier | families that counted | provisional? |
|---|---|---|---|
| W-A origin `1944-01-01 → 1955-12-31` | **T3 register** | none (0) | **PROVISIONAL** — (b),(e) UNTRIED; (c) three routes died or never used the predecessor names |
| W-B consolidation+rename `1985-01-01 → 2000-12-31` | **T3 register** | (a) only | PROVISIONAL — (b),(e) UNTRIED |
| W-C public formation `2001-01-01 → 2004-12-31` | **T3 register, deepest of the three** | (a) only | PROVISIONAL — (b) UNTRIED and (a) is cut at `--max-docs 30` |

Tier rule applied literally (§15.2): ≥3 families with **in-window Tier-1 text** → T1; 2 → T2; ≤1 → T3. No
family returned in-window Tier-1 text for W-A. One family (a) did for W-B and W-C. Nothing here is a T2/T1
claim, and no tier is a property of the company: **Elevance is T3 at its origin and stays T3 through 2004 on
tonight's corpus, while the same CIK is the richest kind of filing registrant after 2001.**

STATUS: WRITTEN

## 2. The window I was handed, and what I did to it

The intake ran on `1944-01-01 → 2014-12-31` (`sources/sec/_RUN.json` `"window"`, and `A4_harvest_mine.md`
l.3, which labels the same span "deliberately WIDE"). That is **70 years** and it is a *search setting*, not
evidence: `00_universe/fortune_top_50_2026.csv` carries no founding-date column, so the 1944 lower bound and
the 2014 upper bound both came from outside the corpus.

Measured against the bytes, the inherited span is wrong at both ends and cannot be a Stage-1 window:

- **Its upper bound is a naming event, not an outcome of the origin.** 2014-12-31 brackets the *Anthem*
  re-rename (2014) which is post-origin and post-scaling; nothing about W-A's evidence depends on it.
- **Its lower bound is the only date in the corpus that has a carrier** — and that carrier is a 2001 filing
  (57 years late). `grep -c -i "1944" sources/sec/0000950130-01-503971_ds1.txt` = **1**.
- **The registrant's EDGAR footprint starts 57 years after that lower bound**: 2,625 filings enumerated,
  earliest row `2001-08-16`, latest `2026-09-10`, and **0 rows before 2001-08-16** (measured over
  `sources/_index/submissions_CIK0001156039.csv`).

So I split it into three stages and judged each on its own evidence, all labelled **PROPOSED**:

- **W-A `1944-01-01 → 1955-12-31`** — origin window. Basis: the carrier speaks to 1944 (formation as Mutual
  Hospital Insurance, Inc.) and 1946 (Mutual Medical Insurance Inc. incorporated), then jumps to 1985; the
  first-decade extension to 1955 is declared as convention, not evidence, and I record that **no byte on disk
  carries any 1947-1984 event for this registrant**.
- **W-B `1985-01-01 → 2000-12-31`** — consolidation and the *Anthem* naming (1985 Associated Insurance
  Companies → 1993 Southeastern Mutual → 1995 Community Mutual → 1996 renamed Anthem Insurance Companies →
  1997 BCBS Connecticut → 1999/2000 purchases). Chosen because those are the recital's own next event and the
  filing prints genuine in-window FY1996-2000 series inside it.
- **W-C `2001-01-01 → 2004-12-31`** — the registrant's own first EDGAR era: `newly-formed Indiana holding
  company`, S-1 filed 2001-08-16, prospectus dated 2001-10-29, 424B4 filed 2001-10-30; ends where the WellPoint
  merger era begins (date NOT established here, see §8).

Naming events **outside every stage window and therefore not origins**: `WellPoint` (2004/05), `Anthem`
(2014), `Elevance Health` (2022). None of them is printed as a naming event by any stored in-window byte.

STATUS: WRITTEN

## 3. The finding: which layer is the registrant, and which are ancestors

The chain has four candidate layers and the corpus separates them cleanly.

**(1) Registrant = the Indiana Anthem line.** CIK 1156039's own first filing defines the speaking "we"
precisely, and it is a continuity move that a Stage-1 probe must not read as incorporation:

> l.274-280 — *"References to the term 'Anthem Insurance' refer to Anthem Insurance Companies, Inc., an
> Indiana insurance company. References to the term 'Anthem' refer to Anthem Insurance and its direct and
> indirect subsidiaries before the demutualization, and to **Anthem, Inc., a newly-formed Indiana holding
> company**, and its direct and indirect subsidiaries, including Anthem Insurance, after the
> demutualization … References to the terms 'we,' 'our,' or 'us,' refer to Anthem, before and after the
> demutualization."*

So: **the legal person that files is the newly-formed 2001 Indiana holding company; the 1944 date it recites
belongs to a converted mutual that became its subsidiary** (l.431-437: *"Anthem Insurance will convert from a
mutual insurance company into a stock insurance company … the converted Anthem Insurance will become a
wholly-owned subsidiary of Anthem, Inc."*). This is Ford's polarity (RD-134: the later entity is the
registrant, the earlier one the ancestor) with a holding-company wrapper added.

**(2) The 1940s mutual lineage — attested, but only by the registrant's own retrospective voice:**

> l.5856-5867 — *"We were formed in 1944 under the name of Mutual Hospital Insurance, Inc., commonly known as
> Blue Cross of Indiana. In 1946, Mutual Medical Insurance Inc., also known as Blue Shield of Indiana, was
> incorporated as an Indiana mutual insurance company. In 1985, these two companies merged under the name
> Associated Insurance Companies, Inc. In 1993, Southeastern Mutual Insurance Company … Blue Cross and Blue
> Shield of Kentucky, was merged into us. In 1995, Community Mutual Insurance Company … was merged into us.
> We changed our name to Anthem Insurance Companies, Inc. in 1996."*

`grep -rn -i "formed in 1944" sources/sec/ | wc -l` = **11**, but those 11 files are **one registration
lineage** (S-1 2001-08-16, S-1 2001-10-01, five S-1/A, 424B4 2001-10-30 — 8 accessions, all 2001). Under §3
that is **ONE source**, so the 1944 origin is single-sourced and its confidence is capped; the repeated counts
are refilings, not corroboration.

**(3) The WellPoint layer is a peer/absorbed company on the registrant's own 2001 word, not its ancestor.**
Measured over all 30 stored SEC documents: `WellPoint` occurs on **2 lines**, both inside one accession
(0000950131-01-503866: exhibit 10.18 l.634 and that accession's full-submission copy l.14326), and both in a
*competitor* list — *"ANTHEM 2001-2003 LONG-TERM INCENTIVE PLAN — LIST OF PEER GROUP COMPANIES: 1. Humana
2. **Wellpoint Health Networks** 3. HealthNet 4. Cigna 5. Aetna 6. Trigon 7. United Healthcare"*. In 2001 the
brand the registrant later wore was another company's name in its own pay-benchmark table. `Blue Cross and
Blue Shield of Kansas City` occurs **0** times in the 30 stored documents; `Blueprint for Health` **0**. That
the same CIK later carries the name `WELLPOINT, INC` (undated EDGAR metadata) supports — as **INFERENCE,
Low** — that the Indiana registrant adopted an absorbed company's name; it does not prove which legal person
survived, and no stored byte prints the event or its date (§8).

**(4) The Elevance layer is a naming event only.** `Elevance` occurs **1** time in the 30 stored documents and
it is not a name: `sources/sec/0000950130-01-503971_dex1022.txt` l.3337 — *"The Panel shall be the judge of
the **relevance** and materiality of the evidence offered"* (an arbitration-clause word; RD-124's bare-word
class). The brand is post-2014; finding it in print after 2014 documents a rename, not an origin.

**Decoys found while measuring families (c)/(d)** (hard rule 5 — three, all inside this company's own bytes):
- `sources/periodicals/Well4302_2003_djvu.txt` l.7 `www.wellpointsystems.com`; 47 occurrences of "WellPoint",
  **0** of "Blue Cross" (`grep -c -i "blue cross" sources/periodicals/Well4302_2003_djvu.txt` = **0**), **0** of
  "Anthem". It is the **2003 annual report of WellPoint Systems Inc., a software company** — same brand,
  different legal person, and the only WellPoint print on disk.
- `sources/periodicals/2006MoFinExamBlueCrossBlueShieldofKC_djvu.txt` head: *"REPORT OF THE ASSOCIATION
  FINANCIAL EXAMINATION OF BLUE CROSS AND BLUE SHIELD OF KANSAS CITY AS OF DECEMBER 31, 2004"* (Missouri
  Department of Insurance). Genuine Tier-1 regulator print — of the **KC layer**, outside W-A/W-B, printing
  **0** occurrences of `Anthem`, `1944`, `1946` or `Mutual Hospital` (G8 below).
- `sources/periodicals/cia-readingroom-document-cia-rdp79-00999a000200010009-6_djvu.txt` — a 1973 CIA
  quantum-parapsychology document; its single mine hit (`A4_harvest_mine.md` l.36 — "elevance of quantum",
  item line 1543) is the BARE_WORD_MATCH the classifier already refused to promote.

STATUS: WRITTEN

## 4. Carriers for the origin / predecessor question (file + line)

| # | carrier (paths under `company_018_elevance/`) | line | what it carries | class |
|---|---|---|---|---|
| C1 | `sources/sec/0000950130-01-503971_ds1.txt` | 29-39 | registrant name, state, domicile as filed (ANTHEM, INC. / Indiana) | FACT |
| C2 | `sources/sec/0000950130-01-503971_ds1.txt` | 274-280 | "newly-formed Indiana holding company"; "we" spans the demutualization | FACT (the definition itself) |
| C3 | `sources/sec/0000950130-01-503971_ds1.txt` | 431-437 | mutual→stock conversion; converted Anthem Insurance becomes a subsidiary | FACT |
| C4 | `sources/sec/0000950130-01-503971_ds1.txt` | 5856-5877 | **the 1944 origin recital** and the 1946/1985/1993/1995/1996/1997/1999/2000 chain | RETROSPECTIVE INTERPRETATION by the registrant (Tier-1 document, dated 2001) |
| C5 | `sources/sec/0000950131-01-503652_ds1.txt`, `sources/sec/0000950131-01-503917_d424b4.txt` | 6944 / 6914 | the same recital refiled | **same lineage as C4 — not corroboration** |
| C6 | `sources/sec/0000950130-01-503971_ds1.txt` | 1788 | Indiana demutualization-law hearing, 2001-10-02 | FACT |
| C7 | `sources/sec/0000950131-01-503917_d424b4.txt` | 119 | "Prospectus dated October 29, 2001" | FACT |
| C8 | `sources/sec/0000950131-01-503917_d424b4.txt` | 26, 417, 9891 | ESU stock purchase date **2004-11-15 printed in a 2001 document** | forward contractual date, NOT an event (§6) |
| C9 | `sources/sec/0000950131-01-503866_dex1018.txt` (+ that accession's `.txt`) | 634 / 14326 | "Wellpoint Health Networks" as a **peer-group company** | FACT that the two layers were separate in 2001 |
| C10 | `sources/sec/0000950130-01-503971_dex1022.txt` | head, 3337 | Exhibit 10.22 **Blue Cross License Agreement**; and the "relevance" decoy | FACT (licensing relationship) |
| C11 | `sources/sec/0000950130-01-503971_dex21.txt` | 217-218, 4149, 5528-5536 | layer map of subsidiaries/bylaws: Ohio mutual, BCBS Connecticut, AHP-KY, Community Insurance Company | FACT |
| C12 | `sources/_index/_registrant_CIK0001156039.json` | 9-14 | EDGAR former names, **no dates** | index metadata — not a date carrier |
| C13 | `sources/sec/0000950130-01-503971_ds1.txt` | 5892-5905 | membership by state at Dec 31 **1996-2000**: real in-window W-B series printed inside a 2001 filing | FACT (in-window content) |
| C14 | `sources/periodicals/2006MoFinExamBlueCrossBlueShieldofKC_djvu.txt` | head | Missouri financial examination of BCBS of Kansas City as of 2004-12-31 | FACT about the **KC layer**, not the registrant |
| C15 | `sources/periodicals/Well4302_2003_djvu.txt` | 7 | WellPoint **Systems** Inc. 2003 annual report (software) | DECOY |

STATUS: WRITTEN

## 5. Five-family verdict

| family | state | measured basis | in-window Tier-1 text for W-A / W-B / W-C |
|---|---|---|---|
| **(a) SEC / EDGAR** | **TRIED–ANSWERED** | walk uncapped: 2,625 filings enumerated, **0 UNANSWERED slices** (`sources/_index/_INDEX_CIK0001156039.md` l.4, l.65-67); perimeter **2001-08-16 → 2026-09-10**, **0 rows before the floor**; 30 docs / 11,194,109 B / 1,474,784 words stored from **8 accessions, one registration lineage** (`_RUN.json`); `_UNANSWERED.csv` records **120 in-window filings never listed** at `--max-docs 30` | **no / yes / yes** (W-B and W-C: filed content inside the window; W-A: only a 2001 recital about 1944) |
| **(b) web archives** | **UNTRIED** (not a null) | `sources/` contains only `_index, corporate_print, harvest_mine, periodicals, sec` — no `web_archive/` dir; and **0 of 3,802** rows in `00_universe/harvest/candidates.csv` carry `source_family` = web archive (fleet-wide, so nobody has queried it for anyone) | no / no / no — **route open** |
| **(c) periodical corpora** | **TRIED, split by route** — Internet Archive **TRIED–ANSWERED (nothing entity-bearing)**; Chronicling America **TRIED–UNANSWERED**; HathiTrust **TRIED–UNANSWERED**; Google Books **TRIED–LABELS ONLY, no bytes** | 51 elevance rows in `candidates.csv`: IA 34, CP 7, GB 5, CA 4, HT 1. CA rows read `SKIPPED: hard stop: 5 consecutive failures (host halted)` and two later `http_status 404 … UNANSWERED: saved:chronicling_america/cfbf881a…json`; HT row is the same host-halt; the mined IA set (A4 l.25-30) = 4 NULL + 1 BARE_WORD + 1 UNANSWERED, and A4 l.21 shows the vocabulary was only `elevance health`, `formerly known as`, `wellpoint formerly known as` — **the names the recital actually supplies were never searched** | no / no / no |
| **(d) digitised corporate print** | **TRIED–ANSWERED (nothing origin-bearing)**, one row still open | CP rows: 1 NULL (`numFound=0` for those exact params only), **1 UNANSWERED with a YEAR facet** (RD-130's class — a faceted zero is never a corpus null), 4 LEAD_ONLY, 1 TIER1_CANDIDATE whose bytes are the 2006 Missouri examination of BCBS **of Kansas City**. `grep -rn "1944\|1946\|Mutual Hospital" sources/periodicals/ sources/corporate_print/ \| wc -l` = **0** | no / no / no |
| **(e) auction / museum / manuscript** | **UNTRIED** (not a null) | no rows, no bytes, no tool run tonight | no / no / no — **route open** |

**Family double-count check (hard rule 4).** The context line handed to me ("6 corporate print, 10
periodicals") counts *files including sidecars*. The shelves hold **5 distinct text documents**, and
`md5sum` proves **3 of them are byte-identical across the two shelves** (`2006MoFinExamBlueCrossBlueShieldofKC`,
`Well4302_2003`, `cia-readingroom-document-…`) — same URL in both `.meta.json` files
(`https://archive.org/download/<id>/<id>_djvu.txt`). Families (c) and (d) therefore **share 3 of their 5
items**; only `comparisonofqual00blue` (1997 CMS/HCFA-line quality comparison, 582,047 B) and
`analysisevaluati2004wolc` (2004 Montana employee-benefit-plan claims audit) are shelf-exclusive. No
corroboration may be counted from a cross-shelf pair.

STATUS: WRITTEN

## 6. Measurements (every quantifier above, with its command)

Run from `founders_playbook/01_companies/company_018_elevance/`:

- `grep -c -i "1944" sources/sec/0000950130-01-503971_ds1.txt` → **1**
- `grep -rn -i "formed in 1944" sources/sec/ | wc -l` → **11** (one lineage; see §3(2))
- `grep -rn -i "wellpoint\|Elevance" sources/sec/*.txt` → **3 lines total**: `dex1022.txt:3337` ("relevance"),
  `0000950131-01-503866_0000950131-01-503866.txt:14326` and `…_dex1018.txt:634` ("Wellpoint Health Networks")
- `grep -c -i "blue cross" sources/periodicals/2006MoFinExamBlueCrossBlueShieldofKC_djvu.txt` → **14**;
  same test on `Well4302_2003_djvu.txt` → **0**
- `grep -rn "1944\|1946\|Mutual Hospital" sources/periodicals/ sources/corporate_print/ | wc -l` → **0**
- Python re-enumeration of `sources/_index/submissions_CIK0001156039.csv` (header first, per hard rule 3:
  `['filingDate','form','accession','reportDate','primaryDocument','source']`) → 2,625 rows; rows with
  `1944-01-01 ≤ filingDate ≤ 2014-12-31` = **1,722** (all distinct accessions); rows before 2001-08-16 = **0**;
  in-window forms present = 41; in-window `10-K` family 13, `S-1` family 10, `S-4` family 9.
- Year content inside the primary S-1 (tag-stripped): 1993 ×11, 1994 ×3, 1995 ×8, **1996 ×17, 1997 ×22,
  1998 ×145, 1999 ×338, 2000 ×379**, 1985 ×1, 1944 ×1, 1946 ×1 — the basis for calling W-B in-window-answered
  while W-A is not.

**One inherited number does not reproduce, and I am not silently fixing it.** The context line said
"128 accessions in window". The tool's own arithmetic is 8 stored accessions + 120 never-listed = **128**
(`_UNANSWERED.csv`: *"120 in-window filings were never listed because --max-docs 30 was reached"*), so 128 is
the size of the *selection stream*, not of the window. Re-implementing the documented selection rule
(`_RUN.json` `selection_order`) over the same index gives **227** filings in the stream, not 128. The gap is
a `sec_intake.py` question for the tool owner; it is not evidence about the company, and no tier here depends
on which of the two is right — under either reading, **1,722 in-window accessions exist and 8 were opened.**

STATUS: WRITTEN

## 7. Per-stage tier reasoning (RD-112, no wording tricks)

- **W-A 1944-1955 → T3 register, PROVISIONAL.** 0 families returned in-window Tier-1 text. EDGAR's floor is
  57 years late and the periodical/print families were queried with a brand the company did not yet have. The
  origin is *attested* (C4) but not *corroborated*: one lineage, retrospective voice, 57 years after the event,
  and the "founded 1944" sentence is a naming-lineage claim by the registrant about an entity that is not the
  filing legal person. Provisional because (b) and (e) are UNTRIED and CA/HT died mid-run.
- **W-B 1985-2000 → T3 register, PROVISIONAL.** 1 family (a) in-window-answered: the filing carries
  FY1996-2000 tables (C13) and the merger/rename recital that fixes 1985 and 1996 as naming events *inside*
  the window. Nothing else reaches it. A 1990s managed-care trade press would plausibly name "Anthem Insurance
  Companies" — that is family (c) still open, un-judged because tonight's vocabulary never contained the name.
- **W-C 2001-2004 → T3 register (deepest of the three), PROVISIONAL.** 1 family (a) but strong: the
  registrant's own registration lineage in full, including the Blue Cross License Agreement (C10) and the
  peer-group list that names Wellpoint Health Networks as a competitor (C9). It stays T3 only because (b) is
  UNTRIED — a CDX pass over anthem.com 2001-2004 is the obvious second family for an IPO-era window, and per
  §15.2 an untried family may not be counted, in either direction.

STATUS: WRITTEN

## 8. What I refused to claim, and why

1. **"Elevance was founded in 1944."** Refused as a founding fact. The only carrier is the registrant's own
   2001 recital (C4/C5, one lineage, 57 years late), and the sentence's subject in 1944 is *Mutual Hospital
   Insurance, Inc.*, which by the filing's own definition became a **subsidiary** of the filing person (C3).
   What is claimable: **FACT** that the registrant's registration statement recites a 1944 formation as Mutual
   Hospital Insurance, Inc.; **RETROSPECTIVE INTERPRETATION** of the continuity; **UNKNOWN** for any
   contemporaneous 1944 record (none reached).
2. **Any date for the WellPoint, second-Anthem, or Elevance renames.** `resolve --ticker WLP` returned
   `{"ticker": "WLP", "cik": null, "name": null}` (delisted, unmapped) and EDGAR's former-name list is
   undated; no stored byte prints a renaming. Dates from memory would be exactly the defect §14 r8 exists for.
   Marked UNANSWERED with FR-1.
3. **Which legal person survived the 2004 Anthem/WellPoint combination.** Stated only as INFERENCE, Low
   (§3(3)). The registrant's 2001 bytes make WellPoint a peer, which is evidence of separateness, not of
   direction.
4. **That BCBS of Kansas City is an ancestor of this registrant.** It is, at most, the ancestor of a *brand*
   the registrant later wore; the local Tier-1 print naming it (C14) is a Missouri examination of a different
   corporate person, and the only WellPoint print bytes on disk are a software company's (C15).
5. **"The company filed nothing before 2001."** Refused. The measured claim is narrower: **0 rows in the
   enumerated index for CIK 1156039 before 2001-08-16**, with EDGAR's own paper-era floor at 1993-94 fleet-wide
   — so pre-2001 activity by *other* registrant identities (Anthem Insurance Companies, WellPoint Networks)
   would sit under other CIKs and has never been enumerated here (FR-2). Reporting it as silence is the RD-134
   error.
6. **Families (b) and (e) as nulls.** Both UNTRIED; per the shared brief an untried family may never be
   reported as a null, and Microsoft's NR-1 shows how a dead route written as an unattempted one poisons the
   one route that could raise a tier.
7. **`TIER1_CANDIDATE` labels as evidence.** The IA row for the CIA reading-room item and the Google Books
   rows (4 × `TIER1_CANDIDATE`, matched page PA546 of a Plural Publishing title) carry **0 stored bytes**;
   they are pointers, not text (hard rule 6), and the one elevance `TIER1_CANDIDATE` whose bytes *are* on disk
   mined to NULL against entity terms.
8. **Corroboration across the 11 recital files, or across the two shelves.** Both refused: same registration
   lineage (§3) and md5-identical cross-shelf duplicates (rule 4).

STATUS: WRITTEN

## Untried

- **(b) web archives — entirely.** 0 calls. Remedy: CDX pass over `anthem.com`, `wellpoint.com`,
  `bcbskc.org`, `elevancehealth.com` 1996-2014 → would be a second family for W-C and possibly W-B.
- **(e) auction / museum / manuscript — entirely.** 0 queries run. Remedy: an intake agent on mutual-era
  plan souvenir/annual-report lots; nothing here can substitute.
- **(c) Chronicling America and HathiTrust — died, not answered.** CA: 4 rows (2 host-halt SKIPPED, 2 ×
  `http_status 404` with saved response JSON); HT: 1 host-halt row. Remedy: re-run after host recovery using
  `tools/ca_endpoint_probe.py` fallback, with the query text `"Mutual Hospital Insurance" OR "Blue Cross of
  Indiana" OR "Associated Insurance Companies"` over **1944-1960** — not the 2022 brand.
- **(c) Internet Archive — 17 of 24 candidates left unmined by `--limit`** (A4 l.5); plus
  `wellpointsystemi00grif` (scan date 1950-01-01) whose text layer returned HTTP 401 after 3 tries
  (`sources/harvest_mine/_index.json` l.71-78) — it is the one local item whose scan date is inside W-A.
- **(c)/(d) for the Indiana layer at all.** Every query tonight searched `elevance health`,
  `wellpoint formerly known as`, `formerly known as` (A4 l.21). Nothing searched the names the registrant
  actually held in 1944-1996, nor Indiana Department of Insurance examination reports (the Missouri analogue
  proves the genre is digitised, `missouristatepublications` collection).
- **(a) 120 in-window filings never listed** at `--max-docs 30`, including the earliest annual reports the
  index proves exist: `10-K405` 2002-03-25 and `10-K` 2003-03-07 (`_INDEX_CIK0001156039.md` l.23, l.30) —
  W-C's own first annual reports were opened at 0 bytes.
- **(a) the forward recital pass** (2005-2015 window) that would carry the registrant's later account of its
  own origin. Not run here because it overwrites the in-window intake state (§9 note).

STATUS: WRITTEN

## 9. FETCH REQUESTs (web calls by this agent: 0; these are script routes for the orchestrator)

- **FR-1 — the renaming carriers.** Registrant CIK 0001156039, accessions in `2004-08-01 → 2006-03-31`:
  the merger-completion 8-K and the FY2004 10-K, which are the documents that must print
  *"formerly known as … changed its name to WellPoint, Inc."* and settle which legal person survived.
  `python tools/sec_intake.py auto "Elevance Health, Inc." --company-dir founders_playbook/01_companies/company_018_elevance --from 2004-08-01 --to 2006-03-31 --max-docs 12`
  **CAUTION for whoever runs it:** `auto` rewrites `sources/sec/_RUN.json`, `_MANIFEST.csv`, `_PLAN.csv`,
  `_SKIPPED.csv`, `_UNANSWERED.csv`, which tonight hold the in-window intake record the orchestrator measured;
  snapshot them or give the tool a per-run tag first. I did not run it for that reason, and the shared brief's
  recital-route instruction is therefore recorded as UNANSWERED here rather than satisfied by an overwrite
  (hard rule 2).
- **FR-2 — the ancestor-registrant route.** Enumerate `WellPoint, Inc.`, `WellPoint Networks, Inc.`,
  `Anthem Insurance Companies, Inc.` as separate registrants (`sec_intake.py index "…"`), so their own pre-2001
  / own-era recitals can be compared to C4. Needs an out-dir decision, since artefacts key on CIK.
- **FR-3 — `wellpointsystemi00grif`** (Internet Archive, scan date 1950-01-01, HTTP 401 after 3 tries):
  `python tools/ia_text.py list-files wellpointsystemi00grif` then `python tools/ia_text.py wellpointsystemi00grif --file <name>`.
  Expect a title-collision check against WellPoint **Systems** (C15) before anything is read as lineage.
- **FR-4 — predecessor-vocabulary re-harvest** (facet-free, per RD-130) over 1944-1960 and 1985-2000 on
  `Mutual Hospital Insurance` / `Blue Cross of Indiana` / `Associated Insurance Companies` /
  `Anthem Insurance Companies` / `Blue Cross and Blue Shield of Kansas City` — owned by the fleet lanes'
  `periodical_harvest.py --company elevance --facet-free`; deliberately not run here.
- **FR-5 — Google Books item `n2FMEQAAQBAJ` matched page PA546** (4 TIER1_CANDIDATE rows, 0 bytes stored):
  fetch the page and confirm or kill the word-sense decoy.
- **FR-6 — CDX pass** for `anthem.com` / `wellpoint.com` / `bcbskc.org`, 1996-2014 (family (b)).
- **FR-7 — Indiana / Kentucky / Ohio insurance-department financial examinations** of the Indiana and Kentucky
  plans (the analogue of C14), 1940s-1960s, which is the only realistic Tier-1 in-window carrier for W-A.

STATUS: WRITTEN

## 10. Gate, claim release, and the route that could change this

- Gate command run as briefed: `python tools/gates.py --company-dir founders_playbook/01_companies/company_018_elevance --checks csv,keys --fail-on substantive --out founders_playbook/03_quality_control/elevance_s1_probe_gates.md`
  → **exit 0; Findings 2 / Passes 0; substantive findings 0.** Both findings are coverage-only and are true of
  a freshly probed company: *"no register CSVs at root or research/ -- csv/anchors gates DID NOT RUN"* and
  *"no stage_*.md volumes found -- keys/anchors gates DID NOT RUN"*; the gate also counted *43 source documents*
  and derived `tier: T3` from this file, agreeing with §1 and §7. Nothing in this dossier depends on the gate
  passing a register it does not yet exist to check.
- **Path + word count:** `founders_playbook/01_companies/company_018_elevance/research/A_chronology_feasibility.md`,
  **4,179 words** at release (`wc -w`), 12 sections, every one marked with its own WRITTEN status line.
- Claim on this path was taken with `python tools/scaffold.py claim --path … --agent probe-elevance` and is
  released with `release --done` before this report is sent (hard rule 9).
- Registers: none written. No `sources.csv` / `timeline.csv` / row ids invented by this probe (§13).
  Handoff to merge: C1-C15 are dossier-local carriers; the 1944 recital must enter as
  `evidence_class = RETROSPECTIVE INTERPRETATION / independence_note = same lineage as C4`, never as a
  corroborated founding.

STATUS: WRITTEN

## 11. Route most likely to change the verdict

One sentence: **a facet-free family-(c)+(d) re-run against the registrant's *own predecessor vocabulary*
("Mutual Hospital Insurance", "Blue Cross of Indiana", "Associated Insurance Companies") over 1944-1960 —
FR-4 plus FR-7 — is the route most likely to change this verdict,** because digitised print is the family that
has flipped tiers in this project (RD-130: Walmart, Target, Boeing, Kroger), every 1944-1960 route that could
have answered is currently recorded as TRIED–UNANSWERED (host-halt / 401 / YEAR-facet) rather than a null, and
a single in-window Tier-1 naming would move W-A from 0 counted families to 1 and start a real argument for T2.

STATUS: WRITTEN


