# A_chronology_feasibility.md — UNITED PARCEL SERVICE (company_048_ups, rank 48), Stage-1 PROBE

Agent: `probe-ups` · Written 2026-09-30 · Method: `00_METHOD_AND_STYLE.md` §3, §5, §6, §13, §14, §15.2 ·
RD-112 (per-stage tiers), RD-124 (fake Tier-1 detectors), RD-130 (YEAR-facet nulls), RD-134 (capped EDGAR walks).
Web calls made by this probe: **0**. Every number below is a command this probe ran against bytes on disk,
and the command is printed with it.

**VERDICT TOKEN (for `gates.py issued_tier`): Stage 1 = T3 register**, provisional only as to families
(b), (c) and (d) — see §3.

---

## 0. Measured state at probe start (verified, not inherited)

| shelf | files on disk | bytes | what it is |
|---|---|---|---|
| `sources/sec/` | 29 stored documents, 20 distinct accessions | 6,446,114 B (834,795 w) | EDGAR full-submission text, 1999-07-21 → 2001-02-05 only |
| `sources/corporate_print/` | **0** | 0 B | empty directory |
| `sources/periodicals/` | directory absent | — | never populated |
| `sources/web_archive/` | directory absent | — | never populated (cf. `company_011_microsoft`, `company_042_target`, which have one) |
| auction / museum / manuscript | no such shelf anywhere in `01_companies/` | — | `find . -maxdepth 3 -type d \( -iname "*auction*" -o -iname "*museum*" -o -iname "*manuscript*" \)` → **0 results** |

EDGAR enumeration, measured from `sources/_index/submissions.csv` (header enumerated first:
`filingDate, form, accession, reportDate, primaryDocument, source`):

```
rows: 3215 · distinct accessions: 3215 · perimeter: 1999-07-21 -> 2026-09-03
rows w/o filingDate: 0 · pre-1961 rows: 0
accessions inside 1960-12-31 -> 2006-12-31 (the recital pass's own range): 869
```

`_registrant_CIK0001090727.json`: `registrant: UNITED PARCEL SERVICE INC`, `cik 0001090727`,
`former_names: []` (empty as retrieved — recorded as a field state, **not** as proof the registrant never
changed name; the POS AM in §1.4 shows a name/person change that this field does not carry).

Fleet intake state, `00_universe/_FLEET_INTAKE.tsv`, row `ups`:

```
pass1_status rc0/inwindow0/UNANS0   pass1_docs 0      (window 1907-01-01..1960-12-31)
pass2_status rc1/inwindow257/UNANS2 pass2_docs 29     (recital window 1960-12-31..2006-12-31)
filing_floor 1999-07-21 · slices_capped no · state DONE
```

**RD-134 consequence, applied:** `slices_capped = no` means this registrant's archive was walked to the
last slice (the tool's own counter, not an inference), so "the filings answer nothing in-window" is here a
measured perimeter and **not** the eight-slice artefact that voided the pre-RD-134 filings verdicts. UPS is
therefore one of the companies whose filings-family verdict survives tonight's re-grade unchanged.

`tools/sec_intake.py` self-accounting for the recital pass (`sources/sec/_RUN.json`):
`attempted 80 = stored(29) + unanswered(2) + skipped(49)` → identity `OK`. The 49 skipped rows split,
measured from `sec/_SKIPPED.csv`:

```
python -c "... NAMELESS / beyond ..."  ->  NAMELESS 48 · BEYOND 1 · NAMELESS_BYTES 5,263,923
```

48 of the 49 are **pre-2001 nameless directory items** (index listed an item with an empty name; no URL
buildable), and exactly 1 is `SKIPPED beyond --max-docs 30`. `sec/_UNANSWERED.csv` carries 2 rows: one
404 (FETCH REQUEST FR-1, §4) and one `UNANSWERED NOT-ENUMERATED: 237 in-window filings were never listed
because --max-docs 30 was reached`.

**Unreconciled, recorded rather than explained away:** the state file's `inwindow257` does not reproduce
from the index. `sec_intake.py` l.1354-1356 prints `visited + unvisited`, i.e. its **planned candidate
stream after per-form de-duplication**, not the raw accession count (869 measured above). No de-duplication
this probe could reconstruct from `submissions.csv` yields 257 — nearest attempts: by `(form, primaryDocument
[:12])` = 322, by `(base-form, primaryDocument[:12])` = 303, by `(base-form, reportDate)` = 230. This is
RD-116's "15-row delta" class handed back to the intake owner, and §0 publishes no reconciliation of it.

STATUS: WRITTEN

---

## 1. The two founding dates, carrier by carrier (the assigned trap, answered as measured)

The brief asked which carrier prints which date and which legal person it refers to. Answer, in the order
the bytes allow.

### 1.1 Family (a) prints **one** founding date: 1907. 1919 prints zero times.

```
grep -o -i "1907" *.txt | wc -l   -> 19        (in 10 of the 29 stored documents)
grep -o -i "1919" *.txt | wc -l   ->  0
grep -o -i "191 9" *.txt | wc -l  ->  0     (tag-split form)
grep -o -i "nineteen" *.txt | wc -l -> 0   (spelled form)
grep -o -i "American Messenger" *.txt | wc -l -> 0
grep -o -i "Seattle Railway" *.txt | wc -l    -> 0
grep -o -i "Railway Express" *.txt | wc -l    -> 0
grep -o -i "Puget Sound" *.txt   | wc -l      -> 0
grep -o -i "1916|1911|Incorporated 19|incorporated in 19" -> 0 each
```

So within the EDGAR family the trap has a clean measured answer: **the 1919 leg has no carrier here at
all** — not in the S-1, not in either S-4/A, not in the final prospectus, not in the FY1999 10-K. 1919 is a
claim this probe has never *seen*, and it stays a claim of the untested families until someone opens them
(§5). Any dossier that writes "1907 and 1919 are the two candidate dates, both supported" will be writing a
date that no held byte prints.

### 1.2 The 1907 recital, and the person that speaks it

Earliest and best carrier — the original S-1, filed 1999-07-21, accession 0000950103-99-000661:

- `sources/sec/0000950103-99-000661_0000950103-99-000661.txt:2121-2122` —
  *"We were founded in 1907 by James E. Casey in order to provide private messenger and delivery services in
  the Seattle, Washington area."*
- same file `:1153` — *"Since the founding of our company in 1907, we have successfully established a vast
  and reliable global transportation infrastructure…"*
- same file `:2122-2127` — *"Over the past 92 years, we have expanded our small regional parcel delivery
  service into a global company… Casey fostered the development of our employee ownership culture when he
  initiated employee stock ownership in 1927."*

The sentence is reproduced with recomputed arithmetic across the whole 1999 registration family and then the
first annual report — measured: `92 years` ×13 and `founded` ×10 in the held bytes:

| carrier (file) | form · filed | line | what it prints |
|---|---|---|---|
| `0000950103-99-000661_…txt` | S-1 · 1999-07-21 | 2121, 1153 | "founded in 1907 by James E. Casey", Seattle |
| `0000931763-99-002191_…txt` | S-1/A · 1999-07-29 | 2133-2134 | same sentence, name kept |
| `0000950103-99-000662_…txt` | S-4 · 1999-07-21 | 2581-2582 | same sentence, name kept |
| `0000931763-99-002518_…txt` | S-4/A · 1999-09-01 | 2741 | 1907 + "92 years", **name dropped** |
| `0000931763-99-002638_…txt`, `…-002672_…txt` | S-4/A · 1999-09-17, 09-22 | 2772, 2768 | 1907 + "92 years", no name |
| `0000940180-99-001230_…txt`, `…-001306_…txt` | S-1/A · 1999-10-20, 11-05 | 2556, 2517 | 1907 + "92 years", no name |
| `0000940180-99-001334_…txt` | **424B4 (final prospectus) · 1999-11-10** | 2390-2391, 1269 | *"We were founded in 1907 to provide private messenger and delivery services"* — **no founder named** |
| `0000931763-00-000749_…txt` | 10-K FY1999 · 2000-03-30 | 161-162 | "founded in 1907 … **Over the past 93 years**" |
| `0000931763-99-002518_…txt` | S-4/A · 1999-09-01 | 343-346 | employee-facing letter: *"UPS is a very special company. For 92 years, spanning almost the entire 20th century, UPS has been primarily owned by its employees and managed by its owners."* |

**Independence, per §3:** all ten carriers sit in 20 accessions of one 1999-2001 registration-and-first-report
programme, and the founding sentence is one maintained string whose tail ("92 years" → "93 years") is
recomputed by the same drafter each year. **Family (a) is ONE lineage for the origin question.** The name
"James E. Casey" appears 3 times in 6.4 MB (`grep -o "James E. Casey" *.txt | wc -l → 3`) and drops out of
the document the public actually received (424B4).

### 1.3 Which legal person "we" is — the registrant discloses it itself

The same S-1, in its own audited balance-sheet note (Deloitte, Atlanta, 1999-07-20), page F-31:

- `0000950103-99-000661_…txt:6818-6824` — *"ORGANIZATION AND PURPOSE—United Parcel Service, Inc. (the
  "Company") was **incorporated in Delaware on July 15, 1999** to become a wholly-owned subsidiary of United
  Parcel Service of America, Inc. ("UPS"). Subject to the approval of the shareowners of UPS, a wholly-owned
  subsidiary of the Company will merge with UPS, and all of the outstanding common stock of UPS will be
  exchanged for new Class A common stock of the Company."* Its balance sheet is printed immediately above at
  `:6809-6814`: **`BALANCE SHEET / July 19, 1999 / ASSETS--Cash …… $100 / SHAREOWNER'S EQUITY--Common stock
  subscribed …… $100`**, with the auditor's signature block and dateline (`/s/ Deloitte & Touche LLP`,
  `Atlanta, Georgia`, `July 20, 1999`) at `:6798-6801`.
- `0000940180-99-001334_…txt:178-187` (424B4) — *"we use the terms "UPS," "we," "us" and "our" to refer to
  United Parcel Service, Inc. or United Parcel Service of America, Inc. when the distinction between the two
  companies is not important. When the distinction … is important … "Old UPS" to refer to United Parcel
  Service of America, Inc. and "New UPS" to refer to United Parcel Service, Inc. On October 25, 1999, the
  shareowners of Old UPS approved a merger of Old UPS with New UPS's wholly owned subsidiary, UPS Merger
  Subsidiary, Inc."*
- Every cover page in the corpus declares the filer as `COMPANY CONFORMED NAME: UNITED PARCEL SERVICE INC ·
  CENTRAL INDEX KEY 0001090727 · STATE OF INCORPORATION: DE` (measured at `0000950103-99-000661:21-24`,
  `0000940180-99-001334:24`, `0000931763-00-000749:26`), with `IRS NUMBER 582480149` — a Georgia-series EIN —
  and business address 55 Glenlake Parkway NE, Atlanta.

**Therefore:** the 1907 sentence is spoken in the first person by a legal person **six weeks old at the date
it was filed**, which the same document tells the reader is a Delaware holding company created to absorb the
older operating company. The registrant is candid about it; the method still has to classify the recital as
`RETROSPECTIVE INTERPRETATION` about 1907 (§3, §6), Tier 1 **as to what the company states**, and cap
corroboration at "one company lineage" — confidence Medium for *"the registrant's filings print 1907"*,
Low/UNKNOWN for *"a firm began operations in Seattle in 1907"*, and UNKNOWN for what legal act, if any, the
1907 event was.

The brief's premise that "the modern registrant is a Delaware continuation from the 1980s-90s" is
**corrected by the bytes**: no 1980s or 1990s entity event is recited anywhere in the held corpus; the only
printed Delaware incorporation date is 1999-07-15, and the merger that installed it closed 1999-11-15 (§1.4).
Dates 1985 and 1988 do occur in the bytes (×254, ×226) but this probe did not read them as entity events —
they sit in the 2001 SC 13D / 8-K exhibit sets in a context this probe declines to characterise without
quoting it.

### 1.4 The Georgia leg is not printed either

`grep -o -i "Georgia corporation" *.txt | wc -l → 0`. Every one of the 185 `Georgia` occurrences is an
address or dateline (`GEORGIA 30328`, `Atlanta, Georgia … July 20, 1999`), plus three governing-law clauses
of an employee stock plan (`0000931763-99-002518:10159` *"governed by the internal laws of the state of
Georgia"*). By 2000-03-15 the POS AM calls the **operating** company Delaware too:
`0000931763-00-000523:171-178` — *"…by United Parcel Service, Inc., a Delaware corporation ("UPS"), which is
the successor to United Parcel Service of America, Inc., a Delaware corporation ("UPS of America") following
a statutory merger effective November 15, 1999 for the purpose of changing UPS of America's organizational
structure."*

Consequence for the chronology question: **family (a) can never settle the state-level legal history of the
1907/1919 persons**, because it never states an incorporation for either of them before 1999-07-15. That
route is a charter/registry route, not a filing route (§5).

### 1.5 The founder-plus-partner story has no carrier in the held bytes — and one measured decoy

- `grep -o -i "co-founder" | wc -l → 0`; `grep -o -i "classmat" → 0`; `grep -o -w "Ryan" → **0`
  (case-sensitive word, across all 6.4 MB).
- The case-**insensitive** version returns 1 hit, and it is a decoy worth recording as such:
  `0000950144-01-001493_g66574sc13d.txt:599` — `Michael G. Bryant   Senior Vice President and Treasurer -
  UPS Capital Corporation`, where the substring `ryan` lives inside a surname printed 51 years after the
  founding. This is RD-124/§14-rule-6 in the wild: the second-most-obvious grep for UPS's co-founder finds
  an executive in a 2001 Schedule 13D.
- `grep -o -i "Stanford" | wc -l → 10`, of which the S-1 instance is a director's credential:
  `0000950103-99-000661:3281` — *"Carolina at Chapel Hill and an M.B.A. from Stanford University. Ann is
  also on…"*. A "Stanford classmate" framing of the 1907 start has **no carrier** here in any form.
- `grep -o -i "borrowed" → 5`, all five in debt covenants (`…for borrowed money, or under any reimbursement
  obligation…`, `0000931763-00-000523:1000`). The folk "borrowed starting fund" detail is unsupported by
  every held byte, not contradicted by them.

**What this probe therefore records:** the SEC family supports a **single-founder** recital (Casey), and even
that only inside the original registration documents; the two-man version of the origin — which is the
version Stage 1 will want, because a founder-plus-partner start is a different channel/decision structure
than a solo one — is, on tonight's corpus, an **UNTESTED claim whose only admissible local carrier is a
1999 restatement.**

STATUS: WRITTEN

---

## 2. The five family verdicts (stated as returns, never as hopes)

Three states only: TRIED–ANSWERED / TRIED–UNANSWERED (tool or network refused; remedy named) / UNTRIED.

| family | state | what it returned | does it return in-window (1907-01-01→1960-12-31) Tier-1 text? |
|---|---|---|---|
| (a) SEC / EDGAR | **TRIED–ANSWERED** | 3,215 accessions enumerated, floor 1999-07-21, 29 docs / 6,446,114 B stored, full uncapped walk; the founding recital in 10 files | **NO — 0 documents in-window.** The in-window pass stored 0 (`pass1 rc0/inwindow0/UNANS0`), which is a measured perimeter, not silence |
| (b) web archives | **UNTRIED** | 0 calls by any agent on this company; no `sources/web_archive/`; no task for any company in `tools/queries.json` | NO |
| (c) periodical corpora | **split across 6 routes: 3 UNTRIED, 1 TRIED–UNANSWERED, 1 TRIED decoy-only, 1 TRIED–ANSWERED narrow null** | see §2.1 | NO |
| (d) digitised corporate print | **TRIED–UNANSWERED** | 19 items labelled `TIER1_CANDIDATE`, every one a bare-word `ups` decoy; 0 bytes on disk; the creator-scoped task returned `numFound=0` **under a YEAR facet** | NO |
| (e) auction / museum / manuscript | **UNTRIED** | no shelf exists anywhere in `01_companies/`; no query vocabulary | NO |

**Families returning in-window Tier-1 text: 0 of 5.** Per §15.2, ≤1 family ⇒ **T3 register** — and the
count is 0, so the tier is stated at the floor rather than argued upward.

### 2.1 Family (c) route by route, from `00_universe/harvest/candidates.csv` (48 `company=ups` rows, retrieved 2026-09-29T13:09Z→19:15Z)

| route (query label as recorded) | rows | state | measurement |
|---|---|---|---|
| `CA 'United Parcel Service' Atlanta Georgia 1900-1975` | 1 | **UNTRIED** | snippet `SKIPPED: global max-requests cap 600 reached` — the request was never issued |
| `CA 'United Parcel Service' messenger/delivery firm 1900-1975 (no state filter; NAME-VARIANT HYPOTHESIS on the 'of America' registrant form)` | 1 | **UNTRIED** | same cause |
| `GB 'United Parcel Service' annual report member` | 1 | **UNTRIED** | same cause (global cap) |
| `HT 'United Parcel Service' common carrier (unbounded; ERA UNREFINED-WIDE)` | 1 | **TRIED–UNANSWERED** | `SKIPPED: hard stop: 5 consecutive failures (host halted)` — network refusal, remedy = re-run behind egress |
| `IA UPS periodical text 1900-1975 (wide, un-refined) [FACET-FREE per RD-130]` | 20 rows: 19 `LEAD_ONLY` + 1 `TIER1_CANDIDATE` | **TRIED–UNANSWERED for the entity question** | 16 of the 20 are `usfederalcourts` docket pages (*Branch v. United Parcel Service*, *Union de Tronquistas … v. United Parcel Service*, *United States v. Search of UPS parcel 1Z0A648R…*, *Intellectual Ventures II LLC v. United Parcel Service*) and the index carries **no date for any of those 16** (`date_or_issue` empty in all 16 rows), so this probe states their shape — PACER-style `gov.uscourts.*` item ids, patent-assertion and parcel-search matters — not a decade. None would be an origin record in any case (§14 r5: naming a company is not naming its origin). The one promoted item is *Hong Kong Daily Press 1930-01-07* (`NPDP19300107`), a newspaper whose connection to this registrant is unverified and whose bytes are not held. Root cause is in `tools/queries.json`: the task text is `("United Parcel Service" OR UPS) (delivery OR parcel OR messenger)` — the bare `UPS` is RD-124's exact decoy generator |
| `IA trucking/transport trade press 1910-1980 [FACET-FREE per RD-130]` — `(title:("Motor Transport") OR title:("Traffic World") OR title:("American Trucking")) AND "United Parcel"` | 1 | **TRIED–ANSWERED, narrow null** | `EMPTY (proven null): numFound=0`. Read it at its width: **zero in three named titles under a "United Parcel" phrase constraint**, 1910-1980. It is not a null for the delivery trade press, and not a null for the 1907-1909 years the query starts at 1910 |

### 2.2 Family (d): nineteen "Tier-1 candidates", zero of them this company

`CP ups annual print 1919-1985 (wide, un-refined …)` returned 19 items stamped `TIER1_CANDIDATE`
(`http_status 200`). Their titles, as indexed:

*"(EST PUB DATE) REPORT RE EXPLOITATION AND FOLLOW **UPS** (HANDWRITTEN)"* (CIA Reading Room, 1954) ·
*Blow-**ups** on Resurfaced Concrete Pavements* (1976) · *Idea-Mapping: … Simulating the "**Ups**" and
"Downs" of Reading Comprehension"* (ERIC, 1982 ×2) · *The 1979 Southeastern Virginia Urban Plume Study
(SEV-**UPS**)* (NASA, 1980/81/85 ×4) · ***UPS** MEMBER PAPERS* (CIA Reading Room, 1972) · *USSR Report:
… JPRS-**UPS**-84-057* (1985) · *Control-Motion Studies of the PBM-3 Flying Boat in Abrupt Pull-**ups*** ·
*…mock-**ups** in the development of Orbital Replaceable Units* · *Tabulated Pressure Coefficients…* ×3 ·
*Vistazos Intimos De Puebla…* ×2.

Not one is a United Parcel Service document; not one is corporate print in the sense the family name
promises (NASA/CIA/ERIC government and academic shelves). This is RD-124's Apple-`APPLE` finding reproduced
on this company's own slug, and it is why the brief's instruction — never report these as a null and never
as a find — holds both ways. **MD5 check was not applicable: no bytes of any of the 19 were downloaded to
`sources/corporate_print/` (0 files), so there is nothing to de-duplicate and nothing to cite.** The
companion task `CP ups corporate print by creator 1919-1985` returned `numFound=0` **with
`year_range [1919, 1985]` attached**, and the index itself records the RD-130 remedy: *"UNANSWERED, not a
null: … Re-run the same query with year_range removed."*

STATUS: WRITTEN

---

## 3. Per-stage tiers (§15.2), each measured against its own window (RD-112)

**No window below is inherited from the universe or from a harvester parameter.** The universe header,
measured (`head -1 00_universe/fortune_top_50_2026.csv`):
`rank,company,revenue_usd_millions,revenue_fiscal_year,profit_usd_millions,hq_city,hq_state,fortune_industry,universe_source_url,verified_by_second_source,confidence,notes` —
**there is no founding-date column**. The UPS row carries `hq_city Atlanta · hq_state Georgia`, and RD-116's
trap fires here exactly as it did at Eden Prairie: **Atlanta is the 1999 registrant's mailing address in
these bytes** (`55 GLENLAKE PARKWAY NE`, `Atlanta, Georgia … July 20, 1999`, `GEORGIA 30328`), while the
founding sentence in the same corpus names **Seattle**. Neither locality may be read off the CSV.

Two search settings already encode two different founding assumptions, and per RD-112 both are parameters,
not evidence:

- `tools/harvest_mine.py` l.72: `"ups": ("1907-01-01", "1960-12-31")` — this is the window the fleet intake
  used as pass 1, and the source of the "window candidate" in this probe's brief.
- `tools/queries.json`, ups tasks: `corporate_print` `year_range [1919, 1985]` (two tasks), `internet_archive`
  `[1900, 1975]` and `[1910, 1980]`, `chronicling_america` `date1 1900 / date2 1975`.
  **The fleet's own tooling is simultaneously asking "did UPS begin in 1907, 1900, 1910, 1919 or 1926-ish?"**
  A later pass that reads a harvest dossier's window as a found date would import all five.

What the corpus itself periodises — the only dated company events recited in the held bytes: 1907 founding
(§1.2), **1927** employee stock ownership (`0000950103-99-000661:2127`; `1927` ×19, `employee stock
ownership` ×29), 1983 OPL spin-off and 1988 FAA operating certificate (both in the S-1/10-K, in
*"In 1983, UPS spun off OPL by paying a special dividend to its shareowners"*, *"In 1988, the FAA granted us
an operating certificate"*). Everything else matching `In 19xx` is a director's biography.

| stage | window (PROPOSED) | families with in-window Tier-1 text | tier | provisional? |
|---|---|---|---|---|
| **Stage 1** origin → first repeatable validation | **1907-01-01 → 1960-12-31** | **0 of 5** — (a) stored 0 documents and 0 pre-1961 accessions on a full uncapped walk; (b) UNTRIED; (c)/(d) returned no in-window text of any provenance; (e) UNTRIED | **T3 register** | **yes**, and the reason is named: (b) and (e) have no query block at all, and (c)/(d) were queried only through shapes RD-124/RD-130 already proved unreliable for this slug |
| Stage 2 network build-out | 1961-01-01 → 1985-12-31 | 0 of 5 | **T3 register** | yes — no family has been tried at this window at all; the fleet's CP window (1919-1985) overlaps it but returned only decoys |
| Stage 3 employee-ownership → public formation | 1986-01-01 → 1999-12-31 | **1 — family (a)**: 10 accessions dated 1999-07-21 → 1999-11-10 are in-window and Tier-1 (the whole IPO lineage: 4,636,581 B of the 6,446,114 B held) | **T3 register**, T2 only if a second family answers | not provisional as to (a); provisional as to everything else |
| (planning tier for the company) | — | — | **minimum of the stages = T3** | per RD-116's convention |

**Boundary honesty on Stage 1's end date.** 1960-12-31 has no carrier: nothing in the corpus argues that
anything about this company's formation ended in 1960. The single in-window dated event that *does* have a
carrier is 1927 (employee stock ownership), and a Stage-1 boundary at 1927 would at least be a recited one.
This probe keeps 1960-12-31 because the brief handed it and because the measured verdict (0 families in
either window) does not change with it, and flags the boundary itself as an open question for Stage-1
authorship rather than silently endorsing a filename.

**What T3 buys, stated plainly.** Every tier emits `sources.csv`, `conflicts.csv`, `data_gaps.csv` and an
UNTRIED list (§15.2), and §K money, §N decisions and §U conflicts remain mandatory. For UPS Stage 1 that is
the correct shape: the corpus can state what the registrant says about 1907 and can prove the legal
architecture of 1999 in detail, and it cannot support a reconstruction of a 1907-1927 venture at any density.
A T1/T2 Stage 1 for this company is **not reachable from any family tonight**, and would require family (c)
or (d) to answer — see §6's closing sentence.

STATUS: WRITTEN

---

## 4. Load-bearing questions, the carrier that could settle each, and FETCH REQUESTs

| # | question | best carrier now | class / confidence | what would settle it |
|---|---|---|---|---|
| Q1 | What founding date does the registrant print, and who does it name? | S-1 `0000950103-99-000661:2121` (and 9 more, §1.2) | FACT that the recital exists — **High** | none needed; it is closed |
| Q2 | Did anything begin in Seattle in 1907? | no carrier; one retrospective lineage (the 1999 registration family) | RETROSPECTIVE INTERPRETATION — **Low** | family (c)/(d) in-window naming; or the county/charter route in §5 |
| Q3 | Was there a partner, and was the start a two-person venture? | **0 carriers.** `co-founder` 0; case-sensitive `Ryan` 0; the single `ryan` hit is inside "Michael G. **Bryan**t" in a 2001 SC 13D (`g66574sc13d.txt:599`) | UNKNOWN — nothing to grade | a 1907-1920 naming of both operators in periodical or print bytes; §5 route R3 |
| Q4 | Where did the money to start come from? | 0 carriers; `borrowed` ×5 are all covenant text ("indebtedness for borrowed money") | UNKNOWN | same as Q2/Q3; no script route |
| Q5 | Which legal person is the registrant, and since when? | S-1 `:6818-6824` (incorporated in Delaware on **1999-07-15**, $100 of cash at 1999-07-19, per the audited balance sheet at `:6809-6814`); 424B4 `:178-187` (Old UPS / New UPS / UPS Merger Subsidiary, approved 1999-10-25); POS AM `0000931763-00-000523:171-178` (statutory merger effective **1999-11-15**) | FACT — **High**, and **two independent-looking carriers are one lineage** (§3): all three are the same registration file family | closed |
| Q6 | What person did the 1907 sentence attach to — the Georgia operating company or the Delaware one? | 424B4 `:178-183` says the prospectus uses "we" for **either** company "when the distinction … is not important" | INFERENCE from the registrant's own definitional note — **Medium**: the recital is deliberately ambiguous as to person | the "Old UPS" chain of title; not obtainable from filings (§1.4) |
| Q7 | **Does any carrier anywhere print 1919, and which person would it name?** | **no local carrier at all** (0 × `1919`, §1.1) | not claimable | §5 route R1 (facet-free corporate print) and R5 (EDGAR 2006→2026 forward sweep) |
| Q8 | What legal act, if any, produced the 1907 operation (partnership? corporation? name change?) | 0 in family (a); `American Messenger` / `Seattle Railway` / `Puget Sound` all 0 | UNKNOWN | registry/manuscript family (e), UNTRIED — §5 R7 |

### FETCH REQUESTs (no script this probe may run reached these; refusing is the correct behaviour)

```
FETCH REQUEST: FR-1
  registrant: UNITED PARCEL SERVICE INC (CIK 0001090727)
  accession:  0000950109-00-004026   form 424B1, filed 2000-09-25
  document:   0001.txt  (index primaryDocument)
  failure:    404 NoSuchKey on all three path forms, measured verbatim in sources/sec/_UNANSWERED.csv
  ask:        enumerate the accession and fetch the real item under whatever name it now carries
  state of the claim: PARTLY ANSWERED LOCALLY, so this is not a missing document. The accession's
              full-submission text WAS stored (`sources/sec/0000950109-00-004026_0000950109-00-004026.txt`,
              172,863 B, 24,665 w) and `grep -c -i "founded|1907"` on it returns **0** — it is a
              debt-securities prospectus supplement with no business/history section. UNANSWERED is
              therefore confined to one question: whether the 404'd `0001.txt` is the same bytes already
              held. No founding claim rests on it.
```

```
FETCH REQUEST: FR-2
  scope:      48 pre-2001 NAMELESS directory items across **15 accessions** (measured from
              sources/sec/_SKIPPED.csv), 5,263,923 declared bytes, concentrated in the S-1/S-4/A and 10-K
              directories, largest:
              586,913 B in 0000931763-99-002518 · 598,288 B in 0000931763-99-002638 ·
              595,121 B in 0000931763-99-002672 · 457,605 B in 0000940180-99-001230 ·
              457,367 B in 0000940180-99-001306 · 442,855 B in 0000950103-99-000662 ·
              420,147 B in 0000950103-99-000661 · 256,806 B in 0000931763-00-000749
  ask:        confirm whether each is already inside the full-submission <accession>.txt this run stored.
              One direction of that answer is already demonstrated: the "92 years" employee letter is
              readable in the stored full submission of 0000931763-99-002518 at l.343, so an unnamed
              directory item in these accessions is not by itself missing content.
  claim left UNANSWERED: none load-bearing. Recorded because RD-112 defect 2 (nameless rows must be
              counted, never vanish) requires the number on the table: 48 items, 15 accessions, 5.26 MB.
```

```
FETCH REQUEST: FR-3  (script-reachable; barred to this probe by brief and by §15.1)
  route:      python tools/sec_intake.py auto "United Parcel Service" \
                --company-dir founders_playbook/01_companies/company_048_ups \
                --from 2006-12-31 --to 2026-09-03 --max-docs 30
  why:        the fleet's recital pass stops at 2006-12-31, so 2007-2026 is enumerated in the index
              (3,215 accessions to 2026-09-03) but never read. This is the cheapest Tier-1 test of Q7:
              does any later UPS filing print 1919, or a predecessor name, or a second founder?
              grep target: 1919 / "American Messenger" / Ryan / predecessor
```

STATUS: WRITTEN

---

## 5. `## Untried` — one command per route, and the defect each route repairs first

A route not run is never a null. Nine named routes, in the order that would change this dossier most:

- **R1 — family (d), the RD-130 remedy, unfaceted.**
  `python tools/periodical_harvest.py --company ups --facet-free`
  *not run (barred by brief).* This is the re-run of `CP ups corporate print by creator 1919-1985` with
  `year_range` removed; the recorded zero was **a statement about our own parameter** (RD-130). Family (d)
  is the only family that has ever flipped a tier in this project — Walmart, Target, Boeing (46 layers),
  Kroger (104 layers / 10,070,024 B) — and UPS was a private, employee-owned company that printed reports to
  its member-owners for most of the window, which is the exact profile where bound corporate print is the
  *only* surviving in-window carrier.
- **R2 — family (d), phrase-scoped not slug-scoped.**
  `python tools/harvest_mine.py --company ups --limit 12 --max-mb 25` *not run (barred by brief).*
  The existing 48 candidate rows were classified with `ups` as an entity word (RD-124). RD-133's
  `universe_names()`/`ALIAS` fix makes `ups` resolve to **United Parcel Service** words, so a re-mine is a
  different question from the one already answered. Also fix in the same pass: `tools/queries.json`'s
  internet_archive task, whose `("United Parcel Service" OR UPS)` is the decoy generator itself.
- **R3 — family (c), the route the brief named and this probe did not run: the delivery trade press, by
  title.** The only trade-press task on file is bound to three titles (`Motor Transport`, `Traffic World`,
  `American Trucking`) at 1910-1980 and returned `numFound=0` **facet-free** — a real but narrow null. Not
  tried: the messenger/courier and municipal-street-railway trade titles of 1907-1920, the Pacific-Northwest
  commercial press, and any **house organ** — the S-4/A's employee letter (§1.2) shows the genre exists in
  the company's own voice, yet the CP task's `report_terms` are only `annual/report/reports/member/director`,
  so an employee magazine is structurally invisible to family (d) as queried.
- **R4 — family (c), Chronicling America.** Two tasks exist with the full entity phrase and a name-variant
  hypothesis (`'United Parcel Service of America' OR 'United Parcel'`) and **neither was ever issued**
  (`SKIPPED: global max-requests cap 600 reached`). Remedy: a per-company run under a raised cap. For a
  1907 Seattle start this is the highest-value in-window periodical route, and it is currently reported as
  UNTRIED, not as empty.
- **R5 — family (a) forward.** FR-3 above: `sec_intake auto --from 2006-12-31 --to 2026-09-03`.
- **R6 — family (b), web archives. UNTRIED, 0 calls by anyone.** `sources/web_archive/` does not exist for
  this company though it exists for `company_011_microsoft` and `company_042_target`, and
  `tools/queries.json` has **no web-archive task for any company** (measured: the family list for ups is
  exactly `chronicling_america, corporate_print, google_books, hathitrust, internet_archive`). RD-133's
  NR-1 defect therefore is live here too in the opposite direction — this dossier can truthfully write
  UNTRIED because no sidecar with an `http_status` exists under that path.
- **R7 — family (e), auction / museum / manuscript. UNTRIED fleet-wide, not just here.** No such shelf
  exists under `01_companies/` (measured in §0) and `queries.json` has no vocabulary for it. For Stage 1 the
  specific documents worth naming: a Washington-state / Seattle charter or licence record for the 1907
  operator, the Georgia Secretary of State charter file for the operating company, and ICC / motor-carrier
  permit records — the third-party contemporaneous paper that could date an entity without asking the
  company.
- **R8 — Google Books.** Task exists (`GB 'United Parcel Service' annual report member`), never issued
  (global cap). UNTRIED.
- **R9 — HathiTrust.** Issued, refused by the host (`5 consecutive failures`), TRIED–UNANSWERED. Remedy:
  re-run behind the runner's egress path (`tools/ca_endpoint_probe.py` precedent), not a re-query of a null.

STATUS: WRITTEN

---

## 6. What this probe refused to claim, defects returned, and the verdict's weak point

**Refused, and why:**

1. **"UPS was founded in 1907" as a FACT of Stage 1.** Refused. The strongest held carrier is a 1999
   registration statement naming a company six weeks old as "we" (Q5, Q6); §3's independence rule makes the
   ten 1999-2000 reproductions **one** lineage, and the "92 years"→"93 years" tail proves the sentence is
   maintained, not remembered. Class `RETROSPECTIVE INTERPRETATION`; confidence Low for the event, High only
   for the existence of the recital.
2. **Choosing between 1907 and 1919, or dating the company's law to 1919.** Refused. 1919 prints **zero**
   times in every held byte, so there is no second leg to weigh — and a probe that "resolved" the tension
   would be inventing a carrier. Recorded instead as Q7 with two named routes (R1, R5).
3. **The founder-plus-partner story in any form.** Refused: `co-founder` 0, case-sensitive `Ryan` 0, and the
   one substring hit is a 2001 officer's surname. The two-person origin is UNKNOWN here, not unlikely.
4. **Treating the 19 `TIER1_CANDIDATE` corporate-print rows as family (d) answering.** Refused (RD-124). All
   nineteen are `ups`/`UPS` as an English word or as a foreign-affairs and NASA acronym, on CIA/NASA/ERIC
   shelves; promoting them would have manufactured a Tier-1 evidence family and, per RD-124, is precisely
   "a broken detector reporting success".
5. **Treating `numFound=0` (the faceted CP creator zero, or the three-title trade-press zero) as a family
   null.** Refused: the first is UNANSWERED with its remedy named (RD-130), the second is a null at exactly
   its query width (§2.1).
6. **The brief's "Delaware continuation from the 1980s-90s".** Not adopted. The bytes print one Delaware
   incorporation, 1999-07-15, and one statutory merger effective 1999-11-15; nothing in the corpus supports
   a 1980s-90s registrant-side entity event, and §1.3 says so with line numbers rather than repeating the
   premise.
7. **Atlanta-as-birthplace, and any date from the CSV.** Refused: `fortune_top_50_2026.csv` has no
   founding-date column (measured), and its `hq_city Atlanta` is the 1999 filer's mailing address.
8. **The 4,330-vs-4,315 style of delta in §0's `257`.** Not reconciled, not guessed; published as
   unreconciled with the three de-dup hypotheses this probe did test.

**Record-selection null (§2), stated for the period rather than for the company:** whatever a 1907-1927
delivery outfit wrote internally is unrecoverable here for a structural reason, not a retrieval failure —
UPS was privately and employee-owned until 1999, so there was no *obligation* to file, and the archive that
survived is the company's own self-narrative plus its 1999 registration. There is no contemporaneous
third-party count of 1907 parcels, capital, or headroom in any family this probe can see, and the single
seed-money anecdote the brief mentions has **0** occurrences in 6.4 MB. Any Stage-1 reconstruction that
reads as well-evidenced for 1907-1927 is reading a survivor's own pamphlet.

**Defects returned to the orchestrator (not evidence):**

- D-1 `tools/queries.json`, ups internet_archive task embeds bare `UPS` in an OR with the entity phrase →
  RD-124 decoy generator; 19 of 20 promoted items across families (c)/(d) for this slug are word-matches.
- D-2 `tools/queries.json` corporate_print task carries `year_range [1919, 1985]`, i.e. **a candidate
  founding date is baked into a retrieval parameter**, and the facet then produced the zero RD-130 says it
  produces. Separately, `harvest_mine.WINDOWS["ups"]` starts at 1907 while CP starts at 1919 — the same
  company is being searched under two incompatible origin assumptions tonight.
- D-3 No `corporate_print` task can find a **house organ** (`report_terms`: annual/report/reports/member/
  director). The S-4/A employee letter is the in-corpus proof that this genre carries the company's own
  lineage claim.
- D-4 Families (b) and (e) have **no query vocabulary for any company**, so every dossier's "UNTRIED" for
  them is a tool gap, not a research choice. This is the Costco situation in RD-112 generalised.
- D-5 `sec_intake` auto: 48 nameless pre-2001 items and 1 not-enumerated row on a registrant whose
  directories are 4-12 items each; FR-2 asks for the containment check. The `257 vs 869` counter mismatch
  (§0) is the same de-dup opacity.
- D-6 `0000950109-00-004026/0001.txt` 404 on three path forms (FR-1) — one *named* primary document
  unreachable, though the same accession's full submission is held and answers the only question this probe
  had for it. Recorded as an intake path defect, not an evidence gap.
- D-7 For the record: `gates.py` before this file existed printed `tier: exemplar (no tier stated in this
  company's research/ dossiers — exemplar assumed)`. After it, the same command prints
  `tier: T3 (tier T3 from A_chronology_feasibility.md …)`, so the budget gate no longer grades a T3 register
  company against a 60k cap (RD-112's convention, mechanically enforced).

**Gate.** `python tools/gates.py --company-dir founders_playbook/01_companies/company_048_ups --checks
csv,keys --fail-on substantive --out founders_playbook/03_quality_control/ups_s1_probe_gates.md` →
`Findings: 2 | Passes: 0`, both findings **coverage-only** (`no register CSVs at root or research/ —
csv/anchors gates DID NOT RUN`; `no stage_*.md volumes found — keys/anchors gates DID NOT RUN`), exit not
failed under `--fail-on substantive`, and it counted `29 source documents`. Expected for a freshly probed
company with no registers yet (RD-117's state); no defect found, and none claimable — the gates had no
input.

**Five-family verdict, in one line each:** (a) TRIED–ANSWERED, 0 in-window documents, 1 retrospective
founding recital in 10 files · (b) UNTRIED, 0 calls, no vocabulary · (c) of six routes: 3 UNTRIED
(Chronicling America ×2, Google Books — all `SKIPPED: global max-requests cap 600 reached`), 1
TRIED–UNANSWERED (HathiTrust, host halted), 1 TRIED and answered only with decoys (IA periodical), 1 narrow
proven null (IA trade press: three named titles, 1910-1980, "United Parcel") · (d) TRIED–UNANSWERED, 19/19
decoys, 0 bytes, its one zero faceted · (e) UNTRIED, no shelf anywhere. **In-window Tier-1 families: 0. Stage 1 = T3 register.**

STATUS: WRITTEN

---

## 7. Hand-off

Single file written: `founders_playbook/01_companies/company_048_ups/research/A_chronology_feasibility.md`.
Nothing added to `sources/`, `_index/`, or `00_universe/harvest/` (§14 r2, r4 — this probe read only).
Sections 0-6 all marked WRITTEN above; this file's own claim is released in the same pass as this report.
Not examined by this probe: the 237 in-window filings the recital pass never listed, the whole 2007-2026
EDGAR tail, the 869-accession recital window beyond the 20 accessions stored, and every byte of families
(b), (c), (d), (e).

**The route most likely to change this verdict is R1 — the facet-free re-run of the corporate-print creator
query (`periodical_harvest.py --company ups --facet-free`) — because its recorded `numFound=0` is the exact
YEAR-facet artefact RD-130 proved manufactures corporate-print nulls, and family (d) is the only family that
has ever raised a tier in this project, for a company that was private, employee-owned and printing to its
own member-owners for the whole of the window Stage 1 needs.**

STATUS: WRITTEN
