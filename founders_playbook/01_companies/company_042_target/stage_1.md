# stage_1.md -- THE DAYTON COMPANY (later Target Corporation), STAGE 1

MERGED VOLUME, single file, 2026-09-26 (merge pass `03_quality_control/target_s1_merge.md`, agent
`target-s1-merge`). Built by concatenating `_parts/s1_p1.md` (header block, boundary argument, sections
A-H) and `_parts/s1_p2.md` (sections I-U, claim records, register emissions) **in order, with no content
rewritten**. Split test (method 9.2): 36,954 words across the two parts, 37,000-ish merged -- inside the
40,000 soft target's amber band and far under the 60,000 hard cap, so **no 9.3 part-split is required**
and none was performed. Section numbering A-U is continuous; claim, metric, conflict and anchor ids were
never renumbered to make a part look self-contained.

## Stage 1 merge note (read before using the registers)

**Registers.** Nine registers now exist at the company root, 157 rows, headers byte-identical to Amazon's,
`stage1` on every row. Rows applied from three emissions, not two: volume 1 (47), volume 2 (79) and the
records dossier `research/B1_dayton_print_records.md` (65 rows, which both volumes presuppose) = 191
requested; **34 emissions were folded into 28 visible collision groups and 0 rows were refused**; every
folded row's distinct wording is retained inside the kept row. Full accounting: `stage_1_index.md` and the
merge sheet.

**Source ids are global from this volume onward.** `S4201`-`S4221` were minted centrally at merge (method
13: "source_id blocks are assigned centrally at merge, never per dossier") and the registers were re-pointed
to them (200 re-pointings). The prose of the two parts keeps citing the dossier-local carriers it was
written against (`B1S01`, `P1S01`, `P2S08`) and those strings are **retired, not deleted**: each is kept as
an alias in the `notes` cell of the global row that replaces it, and the whole map is in
`stage_1_index.md`. Per 14 rule 12 nothing here is addressed by line number.

**Anchors.** 14.4: section U's anchor set is **U.001-U.037, declared by volume 2 and unchanged**; volume 1
minted none, so no re-keying was needed. The registers cite exactly those 37 ids and nothing else: every
declared anchor has a register row (U.001-U.017 in `conflicts.csv`, U.018-U.037 in `data_gaps.csv`) and no
register row cites an undeclared one. Sixteen register cells that pointed at section U's *subsection
numbers* (U.0-U.5) were rewritten as block names, because a subsection number is not an anchor and does not
resolve.

**Corrections carried into this volume and the register layer** (full text in `CORRECTIONS.md`; the
`corrections` gate requires each id to reach both layers, and 47 register rows now carry one):
- **COR-01** the inherited "fiscal year = calendar year" premise is **refuted**: the layer labelled FY1965
  reports the year **ended 1966-01-29**. B1's Q20 is re-based by superseding note inside the same cell (its
  "1965" label is kept, not erased), the comparative 162,773,739 is dated 1965-01-30, and 37 quantitative
  rows gained an explicit `PERIOD BASIS: CONTEMPORANEOUS / RESTATED / MIXED` designation. Conflict **U.011**.
- **COR-02** the dispatch's floor date **1972-03-22** greps to zero bytes in this company directory; it is
  not evidence and is not written as a value. Conflict **K16**. Outbound: `MASTER_RESEARCH_LOG.md` line 1291
  still asserts it; that file belongs to another owner and was left untouched.
- **COR-03** the Brookdale/Roseville mis-citation trap (two 1962 openings, one document, one line apart).
  Conflict **K17**.
- **COR-04** volume 1's section-G claim that site **tenure** was UNKNOWN is **retracted**: the FY1966 notes
  print a land sale-and-leaseback at 225,000 annual rentals with the buildings mortgaged. Tagged in
  `data_gaps.csv` and the `annual_rentals_under_the_land_sale_and_leaseback` row.
- **COR-05** the FY1970 layer byte count 52,736 is withdrawn; disk and sidecar print **53,023**.
- **COR-06** eight emitted rows arrived with column drift (unquoted thousands/place commas) and were
  re-joined at the printed split point; no value altered.

---

>>> VOLUME 1 -- header block, boundary argument, sections A-H (from `_parts/s1_p1.md`) <<<

# FORENSIC LONGITUDINAL DATASET — THE DAYTON COMPANY (later Target Corporation), STAGE 1
## Volume 1 — sections Header, Boundary, A–H

## Header

STATUS: WRITTEN 2026-09-25

### Dataset, stage, and how to read this volume

*One document split for the file cap (method §9.3). Section letters, claim IDs, metric IDs and
conflict numbering run continuously across volumes: **§Header, §Boundary and §A–§H live here
(`_parts/s1_p1.md`); §I–§U and the claim-record appendix live in `_parts/s1_p2.md`.**
Cross-references of the form `(Target S1 §D.2, part_1)` name the volume. Nothing is renumbered to
make a part look self-contained. Tier **T2 core** (§15.2): §A–§U are evidence-bound, registers are
complete, and claim records exist for load-bearing claims only.*

**Dataset:** The Founder's Playbook — forensic reconstruction of what each company in the frozen
universe (`00_universe/`) looked like while its outcome was still unknown.
**Company (rank 42):** today's registrant **Target Corporation**, CIK 27419. This Stage-1 volume
does **not** write the company as "Target (1962)"; it writes **The Dayton Company at FY1965
narrating 1962** — the argument is at `## Boundary` below and is the single most consequential
choice in this dossier.
**Stage:** 1 of 3. **Span argued:** **1962 (the act narrated) inside FY1965 print (the document
that narrates it)**, opening on the discount entry and closing at the **1969 entity-name
changeover to Dayton Hudson Corporation** as evidenced by the FY1968/FY1969 mastheads. **Stage
definition:** origin → first real-world experiment → repeatable validation → scalable company
formation. For a retail chain the four beats are, per §7's adaptation rule, *the concept, the first
stores, the second-and-third-market proof, and the parent's capital and name change* — and all four
are inside this window. Post-boundary material is tagged `(PB)` wherever it is used.
**File:** part 1 of 2 for Stage 1.

**Hindsight firewall (§2).** Nothing here treats the 1978 acquisition of Marshall Field's, the 1991
national ranking of the discount-department-store category, the 1999-04-12 name change, or Target's
eventual position as the country's largest discount chain as evidence that a 1962 decision was
rational, that the department-store management was blind, or that the format was destined to
inherit the parent. The FY1999 report's own genealogy spread — which *is* a hindsight artefact, a
survivor drawing a line from its own founding to its own present — is used in this volume only as
evidence that the company told that story in 1999, never as evidence about 1902–1962. The words
"visionary", "prescient" and "revolutionary" (except inside a quotation mark, where they belong to a
1963 magazine and a 1965 newspaper survey) do not occur in this volume. Anti-hagiography test
applied per §2 to every coda.
**Record-selection null (§2).** Unrecoverable *because the survivor's archive is the one that was
kept*: no internal deliberation of any kind survives for 1962 — not a memo, not a rejected option,
not a dissent, not a feasibility study; **zero** held bytes record anyone deciding anything. No
independent count of any 1962 figure exists behind any company self-report. No 1962 price line, no
first-store lease, no opening-day report, no contemporaneous local newspaper account is held in any
of the five families this run reached. The FY1965 report is itself a *selected* record — the first
annual report a previously private company ever issued, written to make disclosure look like
confidence. See §A.3, §C.2 and §H.5.
**Confidence (§3):** **High** = 2+ independent origins or a primary document for its own year;
**Medium** = one reliable source, or a retrospective-only primary, or any claim resting solely on a
layer fetched over **UNVERIFIED TLS**; **Low** = conflicting, vague, retrospective-only with no
primary carrier; **UNKNOWN** = a finding, never a gap to fill or smooth.
**The single-lineage finding, stated once and enforced everywhere (§3 filing-lineage rule).**
Every positive statement about this company before 1994 is **print**, and the print that matters
here is **company self-narrative**: eleven consecutive stockholder reports FY1965→FY1975 from **one
digitised item**, one uploader, one reporting lineage, plus three later layers (FY1998/99/2000) from
the same item. FY1973's recap of 1969, FY1974's roster of 1962, and FY1999's genealogy spread are
the **same source in a later year**. Repetition across report years is **version evidence, never
corroboration**, and it is recorded in `independence_note` on every register row below. The only
independent in-window carrier held anywhere is one *Chain Store Age* number (April 1963) — and it
does not name the company once (§H.2). Consequently: **no retrospective recap carries a FACT about
a decision in this volume.** Recaps carry FACT-about-the-printing and
RETROSPECTIVE INTERPRETATION-about-the-event, in two separate records, always.
**ID scheme (§13, read before citing).** `P1-xx` claim records, `P1Sxx` source rows and `P1Qxx` /
`P1Tx` / `P1Dx` / `P1Vx` / `P1Fx` / `P1Cx` / `P1Kx` / `P1Gx` register rows in this volume are
**dossier-local**. Global `source_id` blocks are assigned **centrally at merge**; nothing here may
be treated as a global key. Inherited ids from `research/B1_dayton_print_records.md` (`B1-xx`,
`B1Sxx`, `Q1-Q20`, `K1-K9`, `N1-N7`) are reused with that provenance named, and are **not**
re-emitted as fresh rows where B1 already emitted them.

---

## Boundary

STATUS: WRITTEN 2026-09-25

**Geometry note.** This section enumerates the candidate Stage-1 subjects and dates, names the
document behind each, and states why each rival **fails** — it does not assert a boundary and then
defend it rhetorically. Three losers are named: a rejected registrant, a rejected pre-history leg,
and a rejected date convention. One of them (**K1**) is not resolved and is not resolvable from this
corpus; it stays live.

### 1. The entity question, and the genealogy that decides it

The dispatch premise — *Target opened in 1962 as a division of a dry-goods line, became
Dayton-Hudson, and readopted Target in 2000* — is **partially confirmed and partially unsupported**
by held bytes, and the confirmation does not come from filings. The lineage, read off the mastheads
in the documents themselves:

| Masthead as printed in the held bytes | Layer(s) | What its numbers are | Relation to today's registrant |
|---|---|---|---|
| **THE DAYTON COMPANY @ ANNUAL REPORT 1965** (L1 of the layer, under library-stamp OCR noise; balance-sheet head `THE DAYTON COMPANY AND RETALE SUBSIDIARIES`) | FY1965, FY1966 (`The Dayton Company.` at L184) | its own consolidated retail sales and the Target store estate it owned; `Target Stores, Inc.` named as its subsidiary | ancestor; **not** an EDGAR registrant on any held document |
| **Dayton Corporation** | FY1967 (masthead L1-2), FY1968 | parent-level group sales by operating group (Department / Discount and Hard Goods / Specialty) | ancestor |
| **Dayton Hudson Corporation** | FY1969 → FY1998 | corporation totals plus the Low-Margin-Store group | EDGAR `formerNames` for CIK 27419 carries **exactly one** entry: `DAYTON HUDSON CORP`, 1994-12-09 → 1999-04-12 |
| **We are Target Corporation.** | FY1999 → | modern registrant | own filings begin **1994-02-10** (SC 13G); first 10-K **1994-04-21** (FY1993) |

**Genealogy discipline, stated as a rule and applied on every line below.** A figure printed under
one masthead belongs to that masthead's line and is attributed to the **filing entity**, never to
"Target" as a free-floating corporation. Three consequences bind this volume:
(i) `formerNames` holds **one** entry, so the Dayton legs are **not** separate registrants on this
evidence — and equally **not** proven to have never filed (the name→CIK route 503'd; see §H.5,
UNANSWERED-1 and the U-7 route). Do not assume more names than EDGAR carries;
(ii) the FY1969 report's 1968 columns are the **merged** Dayton Hudson scope and may not be used as
corroboration of the FY1968 report's own Dayton Corporation figures (inherited conflict **K9**),
because they are different entities in the same table;
(iii) the uploader's file names in item `01-target-archive` label every year 1965-1998 as
`Dayton Hudson Corp (DH)`. **Text outranks filename** (inherited conflict **K3**): a register built
from the filenames would misdate the merger by four years. Every attribution below cites the
masthead, and where the masthead sits under OCR noise, the deeper line that carries it.

### 2. Why Stage 1 is The Dayton Company at FY1965 narrating 1962

| # | Candidate subject and boundary | Best document for it | Verdict |
|---|---|---|---|
| 1 | **The Dayton Company, FY1965 report, narrating its own 1962 entry into discount merchandising** | `sources/corporate_print/1965_dayton_hudson_djvu.txt` (48,050 B, verified TLS): `The Company entered the discount merchandising field in 1962 with Target Stores, Inc., which now has five stores in operation` | **ADOPTED.** Earliest entity whose own stockholder-facing text is held, inside the founding decade, speaking of the founding act in the **first person plural**. The 1962 event is *inside* this document's own narrative, so the boundary and the earliest carrier of the act coincide. |
| 2 | Target Corporation, 1962 | none | **REJECTED (loser 1).** Three years before the earliest held document of any family, and on the **wrong registrant**: Target's own filings start 1994-02-10 and its own name starts 1999. Writing "Target 1962" would attribute FY1965 Dayton Company numbers to a legal person that did not exist and import a brand into a filing line that EDGAR does not carry. |
| 3 | The Dayton Company / Goodfellow, 1902 (George Draper Dayton's dry-goods leg) | FY1999 genealogy spread only, plus one FY1965 sentence (§B.3) | **REJECTED (loser 2) as the Stage-1 frame; RETAINED at UNKNOWN as pre-history.** Resting Stage 1 here would put the whole section on a 1999 marketing timeline — the exact hindsight artefact §2 forbids. But the leg is **not deleted**: §B.3 keeps it on the record as company self-account with its dates unresolved, because deleting a company's claimed ancestry is as distorting as accepting it. |
| 4 | The FY1965 report as the *whole* stage (an archive boundary) | held item metadata: the OCR run is 1965→2024, nothing earlier (inherited N3/N7) | **REJECTED (loser 3, and explicitly).** FY1965 is the **document floor**, not the business boundary; it is chosen because the entity narrates 1962 *inside* it, not because the archive is empty before it. Saying "the stage is 1965-1975 because that is what survives" would silently convert a preservation accident into a history. |
| 5 | The 1969 merger as the opening event | FY1969 layer: `Dayton Hudson` ×36 | **REJECTED for Stage 1; ADOPTED as the Stage 1 → Stage 2 hand-off** (§6). The merger is the end of the entity that conceived the experiment, not the beginning. |

**A correction the brief required and the bytes forced.** The dispatch's "documented floor …
1972-03-22 in the retail sense" appears in **zero held bytes**: the string `1972-03-22`,
`1972/03/22` and `March 22, 1972` were grepped across the entire company directory
(`sources/`, `research/`, registers included) and returned **no matches**. Under §14 rule 8 a
received figure that appears nowhere is not evidence, so it is **not written** anywhere in this
volume; it is recorded here as a retraction with its route, and in the register block as
`P1K11`. What the bytes *do* support is a three-part floor, and the parts are different kinds of
floor: **document floor = FY1965** (catalog-level, proven from held item metadata, not inferred);
**event floor = 1962** attested only by that FY1965 retrospective and re-narrated by every later
report year of the same lineage; **registrant floor = 1994-02-10** (EDGAR index, 0 of 2,628 rows
earlier, no UNANSWERED slices — a real null, not a dead route).

### 3. Everything before 1994 is print, and print here is self-narrative

The evidentiary consequence of the previous two subsections is the discipline that shapes §C, §D
and §N: for this company, the founding decade is **not** documented by instruments but by **a
company's later account of itself, printed for its own shareholders**. Three rules follow, and they
are applied mechanically:

1. **One source however many years repeat it.** The 1962 origin is carried by FY1965 (contemporaneous
   with the *decade*, three-to-four years after the *act*) and then re-told by FY1973, FY1974 and
   FY1999. `independence_note` on every such row reads `one lineage; later print is version evidence`.
2. **A recap may not carry a FACT about a decision.** Where the record is a retrospective sentence,
   the volume files two claims: the *printing* is FACT (High, for its own year), the *event* is
   RETROSPECTIVE INTERPRETATION (Medium at best). §D.1 does this for the four 1962 stores; §B.2 does
   it for the founder question.
3. **Contemporaneous-and-favourable is not independent.** The FY1965 report quotes a *Minneapolis
   Star and Tribune* survey and prints its most flattering finding. The survey is Tier-2 and **not
   held**; its selection, framing and quotation are the company's. It is therefore recorded as
   second-hand CONTEMPORARY OBSERVATION with corroboration 0 (§F.1), not as third-party confirmation.

### 4. Basis of numerals — a correction to the inherited records file (conflict **P1K10**)

`research/B1_dayton_print_records.md` states: *"Fiscal year = calendar year in these reports."*
**Held bytes refute it, on the face of four layers** (read this session, exact locators in the
register block):

| Layer | What it prints for its own year-end |
|---|---|
| FY1965 | `Sales of the Company's retail operations totaled $186,166,671 during the fiscal year ended January 29, 1966` and `the preceding fiscal year ended January 30, 1965` |
| FY1967 | `For year ended January 28, 1967` (a subsidiary line) |
| FY1969 | `for the year ended February 1, 1969 (fiscal year 1968)` — the report's own label→date key |
| FY1970 / FY1971 / FY1974 | `For the year ended January 31, 1970`; `During the year ended January 29, 1972`; `the year ended February 1, 1975` |
| FY1975 | `FOR THE YEAR ENDED DECEMBER 31, 1975` |

**Ruling adopted by this volume.** A report labelled *1965* is a **52/53-week retail year beginning
in early February 1965 and ending 1966-01-29**; the label names the year in which the *majority* of
the period falls, and the year-end migrates between late January and early February. Therefore:
(a) every year-end store count in §A/§D is a count **at a late-January date in the following
calendar year**, not a 31-December count; (b) the FY1969 layer marks the **change to a
December-terminating presentation by FY1975**, so a series that spans FY1974→FY1975 changes basis
and must say so; (c) the phrase `early in 1962` in the FY1965 retrospective is **calendar** speech
about a store, and it falls in the **first months of fiscal 1961's successor**, which is exactly why
no month may be back-derived from a fiscal label. Confidence in this ruling: **High** — it rests on
five printed year-end dates in four layers, not on inference. This correction is *not* applied by
silently overwriting B1: B1's rows stand as emitted, and the merge carries `P1K10` against every row
whose `date` field is a bare year label.

### 5. The losers kept live

A boundary is only honest if what it throws away stays visible. Named, in the order a reader will
meet them:

- **K1 — who founded Target: two-sided, unresolved, and the held bytes decide neither.** Company
  print gives **roles** (`DOUGLAS J. DAYTON, President, Target Stores, Inc.`;
  `JOHN GEISSE, Vice President, Target Stores, Inc.`, FY1965 L1455-1456) and credits **the
  institution** with the act. Founder attribution exists only in unheld obituary/interview carriers
  (§B.2). The **loser in this conflict is the category "founder" itself**, as applied to 1962: no
  instrument of origination survives, so neither side can be settled at Tier 1 or Tier 2 from this
  corpus. Nothing is averaged, nothing is tie-broken, and the Geisse disappearance after FY1967 is
  carried as a **lead with a named route** (§H.5 UNTRIED-3), never as a conclusion about why he
  left.
- **K2 — the first-store date.** Year and place are held; the **month and day are UNKNOWN** — a
  month-name-with-1962 pattern returns **0 hits across all eleven founding-era layers** (inherited
  N1). The widely repeated `1962-07-01` has **no carrier held anywhere**: side B is UNVERIFIED, not
  disproved (§D.2).
- **K3 / filename-vs-text** and **K4 / when the parent became Target** (EDGAR `formerNames` "to"
  1999-04-12 vs the FY1999 masthead vs the dispatch's "2000"): recorded, both sides, `(PB)` where
  the 1999-2000 leg is used. Not resolved here.
- **P1K10 — fiscal-year basis**, above, which refutes an inherited dossier statement rather than
  inheriting it.
- **P1K11 — the 1972-03-22 floor in the dispatch**, grepped to zero and therefore not written.
- **The erased loser class.** Store openings in 1963 and 1964 appear in **no** held list; Target-**unit**
  dollars exist for **1967 only** in FY1962-FY1968; and the FY1969/FY1970/FY1971 five-year tables
  lost their numeric columns in OCR. Each is a finding about the record, logged in §H.5 and the
  gaps register — not a claim that the underlying facts did not happen.

### 6. Stage hand-offs and what the boundary refuses to claim

| Hand-off | Date claimed | Document | Status |
|---|---|---|---|
| Stage 1 opens | **1962**, month UNKNOWN | FY1965 layer, two independent sentences in one document (the entry sentence and the Roseville sentence) | FACT as to the printing; RETROSPECTIVE INTERPRETATION as to the act |
| Stage 1's repeatable-validation beat | **FY1966 → FY1968**: Denver (Oct 1966), Fridley + West St. Paul (Oct 1967), St. Louis (1968), 9 stores by FY1967, 11 by FY1968 | FY1966/FY1967 layers (UNVERIFIED TLS → Medium cap) | FACT for its own year, Medium |
| **Stage 1 → Stage 2** | **1969**, by document not by calendar day | FY1968 masthead `DAYTON CORPORATION` (one `Dayton-Hudson` mention = the pending merger) vs FY1969 masthead `Dayton Hudson` ×36; FY1970 report dates the merger as `the major event` of 1969 and names `The J. L. Hudson Company of Detroit` | **Strongest form available: a name changeover datable from the documents themselves. No day is claimed.** |
| Stage 2 → Stage 3 (context only, `(PB)`) | FY1998 last Dayton-Hudson report → FY1999 `We are Target Corporation`; EDGAR `formerNames` end 1999-04-12 | held FY1998/FY1999 layers + `sources/_index/raw_submissions_CIK0000027419.json` | `(PB)`, not evidence about Stage 1 |

**What this boundary explicitly does not claim:** that 1962 was Target's founding in any legal sense
(the operating unit was a **subsidiary**, `Target Stores, Inc.`, of a parent that had traded since
the dry-goods era it never dates in held print); that The Dayton Company was the registrant's
antecedent **in EDGAR terms** (it is not, and cannot be — the index has nothing before 1994-02-10);
that the FY1965 report is disinterested (it is the first report a previously private company ever
issued, and it says so); or that any held byte names the company before FY1965, because none does.

## A

STATUS: WRITTEN 2026-09-25

### A.1 Executive state summary — the entity's condition at the boundary, as the held print states it

Four columns only, per §8. Every value names the masthead that printed it; no value is "Target's".

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Reporting entity in the earliest held document | **The Dayton Company**, Minneapolis, Minnesota — a privately-owned operation issuing its **first public annual report** | P1-01 / FY1965 layer L159-166: `The projected growth of The Dayton Company requires that it expand beyond the concept of a privately-owned operation. To this end, we are issuing our first public Annual Report.` | **High** (primary, its own year) |
| Legal structure of the venture being staged | `Target Stores, Inc.`, a **subsidiary**; balance-sheet head prints `THE DAYTON COMPANY AND RETALE SUBSIDIARIES` (L757; `RETALE` is the layer's own OCR of `RETAIL`) | P1-02 / FY1965 L124-125, L757, L178-179 (`gains … from Target Stores, Inc.`) | **High** |
| Year of entry into discount merchandising | **1962**, month and day **UNKNOWN** | P1-03 / FY1965 L124, L397 | **FACT as to the printing; RETROSPECTIVE INTERPRETATION as to the act**; year High, day UNKNOWN (inherited N1: 0 month-with-1962 hits in 11 layers) |
| Estate at the FY1965 year-end (1966-01-29) | **5 Target stores**: four in the Minneapolis–St. Paul metropolitan area, one in Duluth | P1-04 / FY1965 L187-189, L400-401 | **High** |
| Estate as the same document prints it for the **following** year | 7 (FY1966, `889,000 square feet` of total retail area); 9 (FY1967, after Fridley + West St. Paul opened in October) | FY1966 L219; FY1967 L180-182 — **both UNVERIFIED TLS** | **Medium** (transport cap) |
| Parent's whole-company retail sales, fiscal year ended 1966-01-29 | **$186,166,671**, `an increase of 14 percent over sales of $162,773,739` | P1-05 / FY1965 L169-171 | **High** — and **not** a Target figure |
| Parent's net income, same year | **$7,128,981** vs `5,435,205` — printed as `a 31 percent gain` | P1-05 / FY1965 L172-173 | **High**; arithmetic verified: 186,166,671 ÷ 162,773,739 = 1.144; 7,128,981 ÷ 5,435,205 = 1.312 → both printed percents foot |
| Target's own dollars in FY1962–FY1968 | printed **once**, at **$86,901,007 for fiscal 1967, `an in-crease of 43 percent`** | FY1967 L769-771; inherited Q10/N4 | **Medium** (UNVERIFIED TLS; single lineage) |
| Named officers of the unit | `DOUGLAS J. DAYTON, President, Target Stores, Inc.`; `JOHN GEISSE, Vice President, Target Stores, Inc.`; `RICHARD KLEIN, Vice President and Controller and Assistant Secretary, Target Stores, Inc.` | P1-06 / FY1965 L1452-1459 | **High** as to **office**; **UNKNOWN** as to founder (§B.2) |
| Founder of Target | **UNKNOWN — two-sided and undecided** | §B.2; inherited K1 | **Low / UNKNOWN**; conflict record itself **High** |
| Independent carrier naming the company in 1962-1963, anywhere held | **0** — the one held in-window trade periodical (*Chain Store Age*, Apr 1963, 170,260 B) returns `Target` **0**, `Goodfellow` **0**, `Minnesota` **0** | §H.2; inherited N1-family null on held KB | **High** (that the null is real: layer ≫ 400 B threshold) |
| Anything dated before FY1965 in any family reached | **0 held bytes**; the item's OCR run is 1965→2024 | probe N3/N7, catalog-level from held metadata | **High** as a **document** null; pre-history is **UNKNOWN**, not nothing (§B.3) |

### A.2 The four 1962 stores **as the layer prints them** (transcription, not summary)

The FY1965 chronology spread is a two-column list whose halves interleave in OCR: the left column
carries the parent's Dayton's units and the right column the Target units, so a store and a year can
be pulled from neighbouring rows. Each string below is **transcribed exactly as the held bytes print
it** — including `ST.LOUIS PARK` without the space, and including no silent correction of any place
name. Where a later layer spells the same place differently, both spellings are kept and attributed.

| Printed line, verbatim from the FY1965 layer | Line locator | Reading |
|---|---|---|
| `© TARGET STORES, INC. 1962` | L725 | unit header + year; the `©` is OCR of a bullet/dingbat |
| `ro Pim: \| ROSEVILLE, MINNESOTA 1962` | L726 | Roseville, Minnesota, 1962 (`ro Pim:` is a mangled leader line) |
| `rT imme: «\| CRYSTAL, MINNESOTA 1962` | L729 | Crystal, Minnesota, 1962 |
| `Rech DAYTON'S, ROCHESTER 1954 y 1) imme \| DULUTH, MINNESOTA 1962` | L734 | **two columns on one line**: the parent's Rochester 1954 store, then **Duluth, Minnesota 1962** |
| `— KNOLLWOOD, ST.LOUIS PARK` / `= MINNESOTA 1962` | L737-738 | the **fourth** 1962 store, printed as `KNOLLWOOD, ST.LOUIS PARK MINNESOTA 1962` — transcribed, not corrected |
| `<= DAYTON'S, SOUTHDALE 1956 y <<sseximm x BLOOMINGTON, MINNESOTA 1965` | L741 | fifth Target store, 1965 (matches the prose at L187-189) |
| `'ei DAYTON'S, ST. PAUL 1963 jf ====cem_ ir DENVER, COLORADO 1966` / `ce SE: DAYTON'S, BROOKDALE 1966 / <=s==ceeim_ Tr DENVER, COLORADO 1966` | L745, L754 | the two Denver 1966 rows, i.e. `the sixth and seventh stores` of L126 |

**Class discipline on this table.** The pairing of *four* stores with *1962* is the FY1965 report's own
chronology, printed three years after the year it labels: **FACT about the FY1965 record**, and
**RETROSPECTIVE INTERPRETATION about 1962** (Medium, one lineage). The FY1966 prose spells the same
fourth place as `St. Louis Park` (L216) while the FY1965 chronology spells it `ST.LOUIS PARK` —
a **transcription** difference inside one lineage, recorded so no later pass treats one spelling as a
second attestation of a different store. **No held byte names the month, the day, the square footage,
the address or the opening-day takings of any 1962 store** (P1G3).

### A.3 What this stage is, and what it is not

**Is:** a reconstruction of one established department-store company's first discount experiment, as
that company itself reported it, year by year, to its own shareholders, from FY1965 to the year its
name changed. **Is not:** a history of a startup; a founder's account (no founder's words are held);
a story about a future chain; or a document trail from 1962, because the earliest document is four
years late and the earliest *independent* document in the window does not mention the company at all.
The record-selection null (§2) is restated at §C.2 and §H.5 and must be read with this table.

### A.4 Load-bearing claim records for §A

```
A01 Claim: The Dayton Company's first public annual report was issued for the year ended 1966-01-29 and states that its growth required it to expand beyond private ownership — Date: 1965 (report label) / year ended 1966-01-29 — Source: The Dayton Company, Annual Report 1965 — Source date: 1965 (compiled after Jan-1966; the FY1966 report is the first with an audit-style notes section) — URL: archive.org item 01-target-archive, per-year DjVuTXT layer — Local bytes: sources/corporate_print/1965_dayton_hudson_djvu.txt (48,050 B; verified TLS) — Archived: held locally — Tier: 1 — Class: FACT — Passage: "The projected growth of The Dayton Company requires that it expand beyond the concept of a privately-owned operation. To this end, we are issuing our first public Annual Report." — Conf: High — Corroboration: 0 independent (company self-account) — Conflicts: P1K10 as to the year-end basis
```
```
A02 Claim: The discount venture was a subsidiary, Target Stores, Inc., not a division and not a company named Target — Date: 1962-1965 — Source: FY1965 report — Source date: 1965 — Local bytes: 1965_dayton_hudson_djvu.txt L124-126, L178-179, L1455-1459 — Tier: 1 — Class: FACT — Passage: "The Company entered the discount merchandising field in 1962 with Target Stores, Inc., which now has five stores in operation with the sixth and seventh stores scheduled to open in 1966." — Conf: High — Corroboration: 0 independent — Conflicts: None (the dispatch's "division of a dry-goods line" is loose, not contradicted)
```
```
A03 Claim: Four Target stores carry opening year 1962 in the only held chronology: Roseville, Crystal, Duluth and Knollwood, St. Louis Park — the fourth transcribed exactly as the layer spells it — Date: 1962 — Source: FY1965 report, subsidiary/store chronology spread — Source date: 1965 — Local bytes: 1965_dayton_hudson_djvu.txt L725-738 — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION about 1962; FACT about the FY1965 print — Passage: "KNOLLWOOD, ST.LOUIS PARK / MINNESOTA 1962" — Conf: Medium — Corroboration: 0 independent (the FY1974 roster repeats the same lineage) — Conflicts: K7 (a roster parenthetical prints 1961 in FY1973 and 1967 in FY1974; OCR-corrupt, and NOT used to move 1962)
```
```
A04 Claim: No held byte in any family names the company before the FY1965 report, and the digitised run's own floor is FY1965 — a catalog boundary proven from held metadata, not an inference — Date: pre-1965 — Source: sources/ia_search/meta_01-target-archive.json (259,567 B) — Source date: 2026-09-26 (enumeration) — Tier: 1 for the metadata; the silence is not evidence — Class: UNKNOWN for 1902-1961; documented NULL for this corpus — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High (that the floor is real) — Corroboration: n/a — Conflicts: P1K11 (the dispatch's 1972-03-22 floor returns zero hits in held bytes and is not written)
```

## B

STATUS: WRITTEN 2026-09-25

### B.1 Founder / company state — the one held document that is contemporaneous with the decade

The **only** in-window document that names anyone at all is the FY1965 report's officer pages. They
are quoted complete, in the order printed, because their *structure* is the evidence: the family that
owns the parent, and the officers assigned to the new subsidiary, are two different lists.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Parent's Chairman | `DONALD C. DAYTON, Chairman of the Board` | P1-07 / FY1965 L1417 | **High** |
| Parent's President | `BRUCE B. DAYTON, President` | FY1965 L1418 | **High** — and load-bearing against one side of K1 (§B.2): in 1965 the operating head of the parent was **not** Douglas Dayton |
| Parent's Executive Vice Presidents | `KENNETH N. DAYTON`; `GEORGE D. DAYTON, II` | FY1965 L1420-1421 | **High** |
| Douglas J. Dayton, at parent level | `DOUGLAS J. DAYTON, Vice President` (of The Dayton Company) | FY1965 L1436 | **High** |
| Douglas J. Dayton, at unit level | `DOUGLAS J. DAYTON, President, Target Stores, Inc.` | FY1965 L1455 | **High** |
| John Geisse, at unit level, FY1965 | `JOHN GEISSE, Vice President, Target Stores, Inc.` | FY1965 L1456 | **High** |
| John Geisse, FY1966 / FY1967 | `JOHN GEISSE` under `target stores, inc.` (FY1966 L1456); `JOHN F. GEISSE / Senior Vice President and General Merchandise Manager` (FY1967 L1952) | FY1966/FY1967 layers, **UNVERIFIED TLS** | **Medium** |
| Geisse after FY1967 | **0 occurrences in the eight later founding-era layers** (FY1968→FY1975) — string `GEISSE\|Geisse` verified this session over all eleven layers: hits at 1965:1456, 1966:1456, 1967:1952 only | P1-08; extends inherited N3 from 6 layers to 11 | **High** as a count; **UNKNOWN** as to its meaning |
| Company state: ownership | private until FY1965 print; first public stock offering **late 1967** at 23 stores in five states | FY1970 L209-212 | **High** — corporation-level, **not** a Target-unit count |
| Company state: the reporting group's later name | the same dollars are printed as `Discount and Hard Goods Stores` (FY1968) and as `LOW MARGIN STORES` (FY1972 recap) | inherited entity-lineage key | **High**, and a denominator warning, not a finding about the unit |

### B.2 The founder question (K1), kept two-sided on purpose

**What held bytes settle — roles.** Company print from FY1965 names both men as officers of Target
Stores, Inc. (B.1). It **never** credits any person with the 1962 decision: the act is narrated by
the institution (`The Company entered the discount merchandising field in 1962 with Target Stores,
Inc.`) and the concept is stated impersonally (`Target Stores, Inc., was conceived with the knowledge
that …`). The FY1999 genealogy spread is the same construction with the same institutional subject.
So the company's own print supports a **third position that neither K1 side claims**: nobody founded
it; a company did.

**What held bytes do not settle — origination.** Side A, *Douglas Dayton as founder*, rests on a
*Twin Cities*/*St. Paul Pioneer Press* obituary of 2013-07-06 whose headline form is
`Target Stores founder Douglas Dayton, governor's uncle … dies` — **not held**, web lead only
(inherited `B1S12`). Side B, *John F. Geisse as the concept's originator, hired from outside the
Dayton chain*, rests on biographical pages (1920-09-01 → 1992-02-21) — **not held**, Tier-4 lead only
(inherited `B1S13`). Against each side, what the corpus *does* hold:

- Against **A** (if A means "Douglas Dayton ran the company that decided"): in FY1965 the parent's
  President was **Bruce B. Dayton**, and Douglas appears at parent level as one of many Vice
  Presidents (B.1). If A means "he was the first printed President of the unit", the bytes agree —
  and agree that this is an **office**, not an origin.
- Against **B** (if B means "Geisse invented and led it from the top"): the held listings put him at
  **Vice President** in the first year the unit's officers are printed, promoted to **Senior Vice
  President and General Merchandise Manager** by FY1967 — i.e. from the first printed year he owns
  **merchandising**, which is a real functional claim and *not* a chief-executive claim. The
  subsidiary's President in the same list is Douglas J. Dayton.
- **The Geisse disappearance is a lead, not a conclusion.** He is gone from the officer pages after
  FY1967 (0 hits FY1968→FY1975) while Douglas J. Dayton persists across the run. That pattern is
  consistent with departure, with a re-listing convention change, with the parent's reorganisation
  into Dayton Corporation (FY1967 masthead) and with the merger's executive reshuffle (FY1969) — and
  it is consistent with the founder narrative on side A being convenient *after* FY1967. **None of
  these is established.** The route that would settle it is named: P1G-UNTRIED-3 (§H.5) — Minnesota
  corporate Secretary of State records for Target Stores, Inc. and the *Star Tribune* / *Pioneer
  Press* personnel columns FY1967-FY1969, plus the two obituaries (UNTRIED-2).

**Adjudication, per §7's conflicting-evidence format, with no averaging.**
*CLAIM A:* Douglas Dayton founded Target (unheld 2013 newspaper headline, Tier-2 if fetched).
*CLAIM B:* John F. Geisse conceived the Target concept and headed it (unheld biography pages,
Tier-4). *WHY THEY DIFFER:* one credits ownership continuity and the office of President; the other
credits concept and merchandising execution; both are retrospective person-attributions for a
decision the company itself attributes to no person. *EVIDENCE WEIGHT:* **zero Tier-1 weight either
way** — no held carrier on either side, and the held carriers (officer pages) are **compatible with
both and sufficient for neither**. *BEST-SUPPORTED INTERPRETATION:* the venture was launched in 1962
by **The Dayton Company** as **Target Stores, Inc.**, with **Douglas J. Dayton printed as its
President and John Geisse printed as its merchandising officer from the first year either appears**.
*RESIDUAL UNCERTAINTY:* total as to who originated it; no instrument of origination survives, and
neither independent carrier has been fetched into `sources/documentary/`. *CONFIDENCE:* conflict
record **High**; either founder attribution **Low / UNKNOWN**.

### B.3 Founder pre-history kept on the record at UNKNOWN — not deleted, not believed

The probe concluded that the 1902/1908 pre-history is carried **only** by the FY1999 retrospective.
**Held bytes partially refute that, and the correction favours keeping the leg.** The FY1965 report —
in-window, verified TLS — already narrates the founding ancestry itself, at L110-115:

> `Dayton's was founded by George Draper Dayton, a southern Minnesota banker who bought a dry goods
> company in Minneapolis and established it, a few months later, in his new building on its present
> site. Acquisition of adjacent properties and a series of seven major expansions have culminated in a
> 12-story department store with 1,330,000 square feet of space.`

Three things follow, and all three are narrow:
1. There **is** a held carrier for a founder-shaped pre-history statement, and it is the same FY1965
   document that carries the Target entry — so the pre-history is not a 1999 invention, it is a
   1965 self-account. Class: **RETROSPECTIVE INTERPRETATION** (High that the sentence is printed).
2. It supplies **no year** for the dry-goods purchase, **no** `Goodfellow`, and **no** `1908` name
   change to Dayton Dry Goods Company. Those remain **UNKNOWN** and rest on the FY1999 spread alone
   (`George Dayton opens Goodfellows in down- / town Minneapolis …`), whose tick↔blurb pairing is not
   resolvable from the OCR (probe gap G4). `Goodfellow` and `\bDey\b` remain **0 hits across all
   eleven founding-era layers** (inherited N2).
3. It also shows the FY1965 report narrating **1962 twice, for two different units**:
   `Dayton Development Company opened Brookdale shopping center in 1962 in a northern suburb of
   Minneapolis` (L122-123) sits immediately above the Target sentence at L124, and the Roseville
   store is placed at L398 in `a suburb north of St. Paul`. **Both are true statements in one
   document and they are not the same 1962 event.** This adjacency is a live mis-citation trap and is
   flagged in the register: no later pass may quote L123 as though it dated a Target opening.
Founder pre-history therefore stands: **claimed by the company from FY1965 onward, dated at UNKNOWN,
unrelated to any held document before FY1965, and not a Stage-1 subject.**

### B.4 The company's own state of mind, in its own first public sentence

The FY1965 text that frames disclosure is the closest held approach to an internal state, and it is a
*published* posture, not a deliberation: `We arrived at the decision to make our figures public after
much deliberation. However, we feel disclosure will further growth possibilities, open expansion
opportunities, and give our management the challenge of operating in an atmosphere of public
scrutiny.` (L162-166). Read under §2, this is the company telling shareholders why it chose to be
readable; it is **not** evidence that the discount decision had been debated, and nothing in it
identifies who decided anything. §C.2 records what the absence costs.

### B.5 Load-bearing claim records for §B

```
B01 Claim: The Dayton Company's FY1965 report prints Douglas J. Dayton as President and John Geisse as Vice President of Target Stores, Inc., while printing Bruce B. Dayton as the parent's President — Date: 1965 — Source: FY1965 report, "Corporate Officers" and "Principal Officers of Subsidiaries" — Source date: 1965 — Local bytes: 1965_dayton_hudson_djvu.txt L1417-1421, L1436, L1452-1459 (verified TLS) — Tier: 1 — Class: FACT — Passage: "DOUGLAS J. DAYTON, President, Target Stores, Inc. JOHN GEISSE, Vice President, Target Stores, Inc." — Conf: High — Corroboration: 0 independent (FY1966/FY1967 re-listings are the same lineage) — Conflicts: U.K1 as to what these roles mean
```
```
B02 Claim: The string Geisse occurs in exactly three of the eleven founding-era layers — FY1965, FY1966, FY1967 — and zero times from FY1968 onward — Date: 1965-1975 — Source: grep over held bytes in sources/corporate_print/ (11 layers) — Source date: 2026-09-26 — Class: FACT about the print; UNKNOWN about the person's status — Passage: "JOHN F. GEISSE" (FY1967 L1952) — Conf: High (count); UNKNOWN (cause) — Corroboration: extends inherited N3 from six layers to eleven — Conflicts: None; recorded as a LEAD, not a conclusion
```
```
B03 Claim: Company print never credits any individual with the 1962 decision; the actor is the institution and the concept is stated impersonally — Date: 1962 (as narrated 1965) — Source: FY1965 report, Target Stores essay — Source date: 1965 — Local bytes: 1965_dayton_hudson_djvu.txt L388-394 — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION — Passage: "Target Stores, Inc., was conceived with the knowledge that, while there always will be room for full-service, quality department stores at the upper end of the merchandising scale, there also will be people who wish to take advantage of low margins and convenience shopping through the economies of mass merchandising." — Conf: High (that the text reads this way); the FY1999 spread is the same lineage — Conflicts: U.K1
```
```
B04 Claim: The FY1965 report itself narrates the company's dry-goods ancestry, naming George Draper Dayton as founder of Dayton's without a year — Date: pre-1902-1961 (undated) — Source: FY1965 report — Source date: 1965 — Local bytes: 1965_dayton_hudson_djvu.txt L110-115 — Tier: 1 for the printing; the events are unsourced — Class: RETROSPECTIVE INTERPRETATION / company self-account — Passage: "Dayton's was founded by George Draper Dayton, a southern Minnesota banker who bought a dry goods company in Minneapolis" — Conf: High (printing) / UNKNOWN (dates) — Corroboration: 0 independent; the FY1999 spread is the same lineage — Conflicts: corrects probe §Entity-question 4, which attributed the pre-history to FY1999 alone
```
```
B05 Claim: Before FY1965 the company was privately owned, and its own report frames the first public annual report and the later 1967 offering as the opening of its capital base — Date: 1965; late 1967 — Source: FY1965 report L159-166; FY1970 report L209-212 — Source date: 1965; 1970 (layer prints `April 16, 1971`) — Tier: 1 — Class: FACT (corporation level) — Passage: "When the Corporation made its first public stock offering in late 1967, it had 23 stores in five states." — Conf: High — Corroboration: 1 lineage — Conflicts: P1K10 (the offering is `late 1967`; month UNKNOWN; the FY1967 layer does not print it)
```

## C

STATUS: WRITTEN 2026-09-25

### C.1 The original problem, stated by the only entity that stated it

The company's own sentence of 1965 is the whole claim of the venture, and it is worth quoting exactly
because its grammar is the evidence — a **segment** argument, not a technology, not a supply-chain
argument, and not a claim to have invented anything:

> `Target Stores, Inc., was conceived with the knowledge that, while there always will be room for
> full-service, quality department stores at the upper end of the merchandising scale, there also will
> be people who wish to take advantage of low margins and convenience shopping through the economies
> of mass merchandising.` (FY1965 L388-394)

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Problem as stated | serve, in the same house, a second demand curve: low margin + convenience + mass-merchandising economics, which the full-service store by definition cannot price | P1-09 / FY1965 L388-394 | **High** that the company said it in 1965; **Medium** that this was the operating problem in 1962 (retrospective, one lineage) |
| Why an established department store cared | its own market is described as `heavily-competitive`, and the units that grew fastest were the new discount ones | FY1965 L176-184, L192-195 | **Medium** (self-selected favourable framing) |
| The stated proof it had already worked | `gains of 44 percent in sales and 100 percent in pre-tax profits in 1965 over the previous year` attributed to Target | P1-10 / FY1965 L179-181 | **Medium** — the dollars behind the percents are **not printed** anywhere held (inherited N4: no Target-unit sales for 1962-1966) |
| Second problem, structural | a privately-owned operation whose projected growth `requires that it expand beyond` that ownership | FY1965 L159-161 | **High** (its own year, its own sentence) |
| The problem the print never mentions | survival risk, losses, failed sites, price war, or any reason to expect the format to fail | all 11 layers | **UNKNOWN** — see C.2 |

### C.2 What is unrecoverable about the problem, and why that is a finding

No held byte records **anyone deciding** anything: no memo, no feasibility study, no rejected site,
no internal debate about cannibalising Dayton's, no dissent, no board minute. The FY1965 report's
`after much deliberation` refers to the **disclosure** decision, not the discount decision (§B.4), and
using it for the latter would be exactly the hindsight-plus-conflation error §2 forbids. Consequences
carried forward as a null rather than smoothed: the *alternatives* column of every Stage-1 decision
row is **UNKNOWN**; the *rationale* column may only quote the company's published framing, labelled
RETROSPECTIVE; and no claim in this volume may assert that the Dayton board saw the discount threat
to its own stores, because nothing printed in FY1965 says so and the one favourable sentence we have
was selected by the party with an interest in it. **This is the §2 record-selection null operating on
the origin problem**: the survivor's own first public report is the archive, and a first public report
is not a deliberation record.

### C.3 Knowability, for this stage (§7 format)

| Item | Status | Basis |
|---|---|---|
| That the parent entered discount merchandising, in 1962, as Target Stores, Inc. | **KNOWABLE** | FY1965 print, its own subsidiary |
| What format, at what margin policy, in how many stores by 1966 | **KNOWABLE** | FY1965-FY1967 print (some UNVERIFIED TLS → Medium) |
| Whether the discount move was defensive or opportunistic | **NOT KNOWABLE** from this corpus | no deliberation record survives; §C.2 |
| Who originated it | **UNKNOWN**, two-sided | §B.2, K1; no held carrier either way |
| The first store's month, day, size, address, sales | **UNKNOWN** | 0 hits across 11 layers (inherited N1) |
| The 1962-64 market size for discount retail in the Upper Midwest | **NOT KNOWABLE** from held bytes | the one trade paper that would carry it, *Discount Store News*, has **0 items** in the reachable corpus (probe N4); the held *Chain Store Age* layer names Target 0 times |

## D

STATUS: WRITTEN 2026-09-25

### D.1 The first experiment, and the printed sequence that makes it a sequence

| Date (basis) | Event, as printed | Stores at that year-end, printed | Source | Confidence |
|---|---|---|---|---|
| 1962, month UNKNOWN | first Target store opens at **Roseville**, `a suburb north of St. Paul` | — | FY1965 L397-398 | FACT (print) / RETROSPECTIVE (act); **High** / day **UNKNOWN** |
| 1962 | three further 1962 openings in the same chronology: **Crystal**, **Duluth**, **Knollwood, St. Louis Park** (spelling as printed) | **4** in the 1962 rows | FY1965 L725-738 | **Medium** (chronology pairing; column interleave) |
| 1963 | **no held layer enumerates a 1963 Target opening** | **UNKNOWN** | absence in 2 lists of 1 lineage | **UNKNOWN** — an absence in a list, not a statement (inherited gap) |
| 1964 | ditto; and the FY1965 report's comparative year is the year ended **1965-01-30** | **UNKNOWN** | absence + P1K10 | **UNKNOWN** |
| 1965 | Bloomington opens, `a southern suburb of Minneapolis`; `This brought the total number of Target stores to five.` | **5** (four Twin Cities + Duluth) | FY1965 L187-189, L400-401 | **High**; arithmetic check: 4 + 1 = 5 ✓ ties to the 1962 chronology rows |
| scheduled, printed 1965 | `Two more Target units are scheduled to be opened in Denver, Colorado, in the Fall of 1966, marking our first venture outside the Upper Midwest.` | plan, not actual | FY1965 L190-192 | **High** as a printed plan |
| 1966-10 | the two Denver stores open | **7** (`Total retail area of the seven Target stores now in operation is 889,000 square feet.`) | FY1966 L219, L355 | **Medium** (UNVERIFIED TLS); 5 + 2 = 7 ✓ |
| 1967-10 | Fridley and West St. Paul open, `numbers eight and nine`; `operated at a profit for the year after absorbing all pre-opening expenses` | **9** | FY1967 L180-182 with FY1966 L217-218 | **Medium** (UNVERIFIED TLS); 7 + 2 = 9 ✓ |
| 1968 | two openings in St. Louis | **11** — but this total is **a 1973 recap**, not a FY1968 sentence | FY1973 L564-565 (`Target has grown from 11 stores to 46 stores in five years.`), openings from FY1968 L688 | **Medium**; RESTATED, so never corroboration |

**What the sequence establishes and does not.** The printed counts are **internally consistent** with
the printed openings for 1962→1967 (4→5→7→9, each step matching a named opening). That is an
**INFERENCE about the coherence of one lineage's reporting**, not corroboration by a second source —
a company that repeats its own arithmetic agrees with itself. What the sequence does **not**
establish: any 1963 or 1964 opening (none printed), any within-year ordering, and any claim that the
1962 four all opened before the year's end (the year-end basis is late **January 1963** — §P1K10).

### D.2 The experiment's first unit, and what may not be said about it

The **first** Target store is Roseville, and that is the whole of the held fact. Not established and
not to be inferred: the opening day (see §Boundary 5, K2), the building's size, whether it was a
conversion or new construction, its lease terms, its first-week trade, whether it was profitable in
its first year, and what its name signalled to customers. **The first customer, the first transaction
and the first week are UNKNOWN**, and per §10 they are logged as research debt with a route
(UNTRIED-4: the *Star Tribune* / *Pioneer Press* 1961-08→1962-12 back-files and the Duluth *News
Tribune*; UNTRIED-1: the item's own 17 PDF legs, which are the cheapest remaining route to page-level
detail the OCR lost).

### D.3 Where the experiment stopped being local

Denver, October 1966, is the held first-market test outside the home metro, and FY1967 supplies the
result sentence the company chose to print about it: `In their first full year of operation, Target's
two Denver stores matched the initial performance of the Twin Cities Target stores.` (FY1967 L177-179,
**UNVERIFIED TLS → Medium**). Read as validation rather than as prophecy (§2), what this is: a
company's own report claiming, in its own second year of operation, that a distant store reproduced
the home format. What it is not: an independently audited unit result — no Denver-specific sales line
exists anywhere held.

## E

STATUS: WRITTEN 2026-09-25

### E.1 Product reconstruction — the format, from print that describes it while it was current

The richest held description is FY1966's (a **UNVERIFIED TLS** layer, so the block caps at Medium as a
whole; the FY1965 sentences inside the same frame are verified):

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Unit size, new construction | Denver pair `146,000 square feet in size`, `located on major thoroughfares in western and southeastern suburban Denver` | FY1966 L205 | **Medium** |
| Average estate size, FY1966 | **127,000 sq ft per store** — `derived_arithmetic: 889,000 ÷ 7 = 127,000` | derived from FY1966 L219 | **ESTIMATE, Low** (the layer prints neither an average nor a per-store breakdown) |
| Assortment | `a quarter-million items strongly centered on everyday shopping needs, displayed for mass impact` | FY1966 L206 | **Medium** |
| Price/quality policy | `selling first quality, nationally advertised goods on a low margin basis with full return privileges` | FY1966 L213-214 | **Medium** — this is the *merchandising contract* the concept claimed in §C |
| Leased-department load | `Only 11 percent of sales in Target stores are from leased departments. This does not include sales of the grocery departments, operated by Applebaum's.` | FY1965 L421-423 | **High** |
| Grocery | operated by **Applebaum's**, a named third party, inside Target stores, **excluded** from the 11 percent and from the basket figure below | FY1965 L423; FY1966 L214-215 (`excluding groceries`) | **High** that it is printed; **UNKNOWN** what share of trade it was |
| Format priorities, company's list | `domination of the market in the number and quality of products available; merchandising techniques which provide excitement in shopping; selection of prime traffic locations, and an outstanding food operation` | FY1965 L413-418 | **High** (its own year) |
| Space productivity, group basis | `1,577 thousand square feet` and `$120.16 sales per square foot` for **1968**, printed in the FY1972 five-year block under `LOW MARGIN STORES` | FY1972 L2374-2384 (inherited Q14) | **High** for the print; **RESTATED** for the year; **group, not Target alone** |

### E.2 The denominator that must travel with every product figure

Three different "products" are printed and two are conflated in secondary accounts. **Target** = the
chain (unit). **Discount and Hard Goods Stores / LOW MARGIN STORES** = the *reporting group*, which
also carried Lechmere hard goods (and, from 1971, acquired Lechmere stores) — FY1968's group revenue
of **$189,515,025** is 2.2× the Target unit's own printed FY1967 dollar of **$86,901,007**, and the
ratio is a warning, not a growth rate. **Corporation** = the parent, `3,628,600 square feet` of total
retail space and `$10,705,548` of capital expenditure in FY1967 — dividing Target's dollars by the
parent's square footage yields a meaningless number that looks like productivity. Any Stage-1 figure
without an explicit carrier-entity is treated as **defective** and left out of this volume rather than
guessed at.

### E.3 What cannot be reconstructed about the product, and the route

No held byte gives: any price or price index, any private-label or own-brand record, gross margin
**basis** (the word `low margin` is a positioning claim, not a percentage), SKU or category mix beyond
`quarter-million items` and `everyday shopping needs`, the store layout or the fixture spec, supplier
identity, or the share of trade taken by the two non-Target elements of the same estate (leased
departments and Applebaum's groceries). The cheapest route to several of these is **UNTRIED-1** — the
same item already holds **17 PDF legs for 1965-74**, i.e. page images the OCR pass dropped columns
from (inherited N5); re-reading them needs no new fetch and no web budget.

```
D01 Claim: The first Target store opened in Roseville, a suburb north of St. Paul, early in 1962; no month, day, size or address is printed in any held layer — Date: 1962, month UNKNOWN — Source: FY1965 report — Source date: 1965 — Local bytes: 1965_dayton_hudson_djvu.txt L397-398 (verified TLS) — Tier: 1 — Class: FACT as to year and place; UNKNOWN as to calendar day — Passage: "Since the first Target store was opened early in 1962 in Roseville, a suburb north of St. Paul, its identification as a quality discount operation has been firmly established." — Conf: High / day UNKNOWN — Corroboration: 0 independent — Conflicts: U.K2
```
```
E01 Claim: The Target format as printed is a large suburban single-level box carrying about a quarter-million everyday items at first-quality, nationally advertised, low-margin pricing with full return privileges, with roughly a tenth of sales in leased departments and groceries run by Applebaum's — Date: 1965-1966 — Source: FY1965 L413-423; FY1966 L205-219 — Source date: 1965; 1966 — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION by the operator (FACT about the print) — Passage: "selling first quality, nationally advertised goods on a low margin basis with full return privileges" — Conf: High (FY1965 lines) / Medium (FY1966 lines, UNVERIFIED TLS) — Corroboration: 0 independent — Conflicts: None
```
```
E02 Claim: Target-unit dollars exist for exactly one year of the first seven (1967, $86,901,007, +43 percent); every other founding-decade dollar in held print is group or corporation scope — Date: 1967 — Source: FY1967 report, Financial Review — Source date: 1967 — Local bytes: 1967_dayton_hudson_djvu.txt L769-771 (UNVERIFIED TLS) — Tier: 1 — Class: FACT / ESTIMATE for the implied 1966 base — Passage: "Target's sales were $86,901,007, an in-crease of 43 percent." — Conf: Medium — Corroboration: 0 independent (the FY1968 group line is a different denominator, same lineage) — Conflicts: None — derived_arithmetic: 86,901,007 ÷ 1.43 = 60,769,935, approximate to about $1m because the printed percent is rounded
```

## F

STATUS: WRITTEN 2026-09-25

### F.1 The customer, as far as print will let it be known

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Adoption, home county | `51 percent of women customers in Hennepin County shopped at a Target store in 1965` | P1-11 / FY1965 L404-407, quoting a *Minneapolis Star and Tribune* survey (`Retail Revolution 1955-1965`) | **Medium**, corroboration **0**. Second-hand CONTEMPORARY OBSERVATION selected by the company; **the survey itself is not held** |
| Third-party framing, same quotation | `When shopping at specific centers is considered, the most significant change is the emergence of Target as the leader.` | FY1965 L408-410 | **Medium**, same carrier, same independence problem |
| Basket | customers `spend an average of more than $7.50 per visit, excluding groceries. This compares with an industry average of $5.05.` | FY1966 L214-215 (**UNVERIFIED TLS**) | **Medium**, corroboration 0, and **the denominator of "industry average" is not named** — no carrier, no sample definition, no source |
| Who the concept was for | `people who wish to take advantage of low margins and convenience shopping through the economies of mass merchandising` | FY1965 L390-394 | **High** that the company wrote it; **Low** as a description of an actual customer, being a positioning sentence |
| Where the trade was | four of five 1965 stores in the Minneapolis–St. Paul metro, one in Duluth; the estate is explicitly suburban (`southern suburb of Minneapolis`, `suburb north of St. Paul`) | FY1965 L187-189, L397-401 | **High** |
| Customers, transactions, trip counts | **UNKNOWN** — no held byte prints a customer count, transaction count or market-share number that is not the company's own selection | all 11 layers | **UNKNOWN** |

### F.2 Independence problem, stated once for the whole section

Both quantitative customer facts in the table are **company-printed quotations of third parties**. One
is a newspaper survey quoted in a shareholder report; the other is an "industry average" with no
industry, method or carrier attached. Neither document exists on this machine. So the honest reading of
§F is: *by 1965-66 the company could print that a majority of women in its home county had shopped it,
and could print a basket above a stated-to-be-typical basket, and no independent artefact in the
corpus confirms either statement.* Under §5's Tier-4 rule each is a **lead** to be chased to the survey
and to the trade statistic (**UNTRIED-4**, **UNTRIED-1**); under §3 chasing them is the obligation, not
a disclaimer. And under §2 the *absence* of the customer's side is structural: customers, employees
and displaced competitors appear in this archive only when the company finds a number worth printing
about them.

### F.3 Claim records for §F

```
F01 Claim: The strongest held adoption evidence for 1962-1965 is a favourable third-party survey that survives only inside the company's own shareholder report, and the survey document is not held — Date: 1965 — Source: FY1965 report quoting the Minneapolis Star and Tribune — Source date: 1965 — Local bytes: 1965_dayton_hudson_djvu.txt L404-410 (verified TLS) — Tier: 1 for the page, Tier 2 for the survey (NOT HELD) — Class: CONTEMPORARY OBSERVATION (second-hand) — Passage: "discloses that 51 percent of women customers in Hennepin County shopped at a Target store in 1965." — Conf: Medium — Corroboration: 0 — Conflicts: None — Independence: the company selected, framed and printed the survey finding; the carrier cannot be audited from this corpus
```

## G

STATUS: WRITTEN 2026-09-25

### G.1 Supply and host side — for a chain of this era, the host is the parent's own balance sheet

The retail adaptation of the standard "supply/host" frame (§7) is *sites, capital and merchandise*. In
this company all three were inside one family of owned entities, which is why the held evidence for
"host side" is corporate-print rather than supplier records.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Site supply | the parent ran its own shopping-centre developer: **Dayton Development Company** — Southdale 1956 (`the first fully-enclosed, air-conditioned shopping center in the world` on its own account), Brookdale **1962**, Stage II 1966 to `857,000 square feet` | FY1965 L117-123, L198-203; FY1966 L225-231 | **High** FY1965 / **Medium** FY1966 (UNVERIFIED TLS) |
| The Target sites themselves | **part-owned, part-leased-back, and the notes pages say so.** FY1966: `The mortgage notes of a retail subsidiary bear interest at 6½% and are payable $52,764, including interest, quarterly. The net carrying amount of land, land improvements, buildings, fixtures and equipment pledged as collateral to the mortgage notes aggregates $3,611,368. Interim financing for two discount stores constructed in 1966 will be replaced by a first mortgage note in the approximate amount of $2,200,000 … Interim financing for land for these stores will be replaced in 1967 under terms of sale and leaseback arrangements which will require annual rentals of approximately $225,000.` (L804-809; percentages mangled by OCR, transcribed as read) | P1S02 L804-809 (**UNVERIFIED TLS**) | **Medium**. The reading is narrow but real: **the 1966 pair's buildings were to be mortgaged (held) and their land sold and leased back (not held)** |
| Construction finance, FY1965 | `The interim financing is for new construction. Upon completion and acceptance of the building, permanent long-term financing is to be provided by a first mortgage note in the amount of $7,500,000 at 5½%, payable in monthly installments of $50,000` (rate as read from the layer's `574%`), collateral pledged `$18,141,019`, and an interim financing of `$3,200,000` shown as `payable to the parent` | P1S01 L1170, L1228-1236 (**verified TLS**) | **High** — the parent financed the unit's construction as an intercompany payable |
| Land monetisation | `sale of commercial development land adjacent to the two centers for $1,771,355` in 1966 | FY1966 L228 | **Medium**; a corporation-level figure, **not** a Target figure |
| Credit supply | **Dayton Credit Company**, printed with year **1965** in the same subsidiary chronology, `HADLAI A. HULL, President, Dayton Credit Company` | FY1965 L722, L1463 | **High** |
| Merchandise supply | unnamed. The only merchandise-side parties printed anywhere in the founding decade are **`nationally advertised goods`** (a brand-supply posture) and **Applebaum's**, which ran groceries **inside** Target stores | FY1966 L213; FY1965 L421-423 | **Medium**; vendor identity **UNKNOWN** |
| People supply | no recruiting, training or staffing record in held print; the unit's three named officers at FY1965 are a family President, a VP (Geisse) and a VP/Controller (Klein) | FY1965 L1455-1459 | **High** for the list; headcount **UNKNOWN** |

### G.2 The capital ladder, in order, with each instrument kept separate

| Date (as printed) | Instrument | Scope | Source | Confidence |
|---|---|---|---|---|
| FY1965 print | **first public annual report** issued; the decision framed as necessary to growth | parent | FY1965 L159-166 | High |
| late 1967, month UNKNOWN | **first public stock offering**, at which point `it had 23 stores in five states` | **corporation**, not Target | FY1970 L209-212 (a 1970 report reciting 1967 — RESTATED) | High for the sentence, **Medium for `late 1967` as a date** |
| 1966 | `interim financing for two Target stores opened in Denver in October of 1966` | unit, mentioned in a note | FY1966 L355 | **Medium** (UNVERIFIED TLS) |
| 1969-07-15 | first public **debt** offering: `$25 million` sinking-fund debentures due 1994, priced to yield 7.80% | corporation | FY1969 L (inherited timeline row) | High |
| 1969-09-08 | common stock listed on the **NYSE**, same day as a new corporate symbol | corporation | FY1969 (inherited) | High |
| 1967 | capital expenditures `$10,705,548`; total retail space to `3,628,600 square feet` | **corporation** | FY1967 L189-192 | **Medium** (UNVERIFIED TLS) |

**Do not merge these rows.** The 1967 **stock** offering, the 1969 **debentures** and the 1965 **report**
are three different events of three different kinds, and the FY1970 sentence that supplies the first is
a *recap* printed on 1971-04-16 (the layer's own date line, L200), not a 1967 document. §6's fiscal
ruling applies again: a "1970" report signed in April 1971 is a 1971 carrier for 1970 facts.

### G.3 What §G cannot answer

Whether Target Stores, Inc. was capitalised by equity or wholly by intercompany payable at the parent's
option (the FY1965 note shows a `$3,200,000` interim financing `payable to the parent`, but no capital
account for the unit is legible in any held layer), what the 1962-65 Minnesota stores cost, the price at
which the 1966 land was sold in the leaseback, what rent the parent charged the unit for anything it
owned, whether Applebaum's paid or was paid, and every vendor term. The cheapest route to several of
these is **UNTRIED-1** — the same item already holds **17 PDF legs for 1965-74**, i.e. page images the
OCR pass dropped columns from (inherited N5); re-reading them needs no new fetch and no web budget.
**A self-correction recorded here rather than hidden:** an earlier draft of this section stated that
*no held line states who owned the Target land or buildings*. Two notes pages do state it, one in a
verified-TLS layer and one in the FY1966 layer, and they are now quoted in §G.1 — which is why the gap
below is narrowed to *cost and counterparty*, not *tenure*.

## H

STATUS: WRITTEN 2026-09-25

### H.1 The knowability frame for this market

The market in which the first Target stores opened is the least-documented object in Stage 1, and the
reason is corpus-shaped rather than history-shaped: the two families that could carry an in-window,
outside-the-company account of the discount market are **periodicals** (one held item, thin) and
**local newspapers** (none held, egress-limited). EDGAR contributes nothing (registrant floor
1994-02-10) and web archives contribute nothing (family ceiling mid-1990s, and the route 503'd).

### H.2 The one held independent in-window periodical, and its exact contribution

*Chain Store Age*, April 1963, `sources/periodicals_csa_1963/Chain_store_age_Steel_for_Stores_djvu.txt`
(170,260 B, verified TLS, 168,433 chars of OCR read at probe): a trade advertising section.

- Its market statement, verbatim: `the chains have felt the impact of two revolutions. Before the
  first—the shopping-center revolution—had run its course, the second—the discount store revolution
  —began to make itself felt.` (L4475-4479). Tier-1 **trade** text, in-window, **independent of the
  company**, and it establishes that the category the parent entered was being narrated in the trade
  press as a revolution *while* the first stores were opening.
- Its nulls, verified over held bytes: `Target` **0**, `Goodfellow` **0**, `Minnesota` **0**;
  `Dayton` **2** (both non-company: `DAYTON, OHIO`; `DAYTON—Scheduled for an October open-`),
  `Hudson` **3** (`HUDSON PLAZA`, `J. L. HUDSON REAL ESTATE CO.`, `Hudson House, Inc.`), `discount`
  **14**. The layer is ≫ 400 B, so **zero here is zero** (§14 rule 6), not a truncated read.
- Its ceiling: an April-1963 issue is nine-plus months after the launch and still does not name the
  chain, which is itself evidence about salience in the trade press — **not** evidence about trade.

### H.3 What the company said about its market, and how much weight it can bear

`the heavily-competitive Minneapolis-St. Paul metropolitan area, where its stores now dominate the
discount field` (FY1965 L192-194) and `its identification as a quality discount operation has been
firmly established` (L398) are the company's two market-position claims in the founding decade. Both
are **unquantified**, both are self-printed, and neither has any independent count behind it anywhere
in this corpus. They are recorded as **FOUNDER-CLAIM-adjacent corporate claims** —
RETROSPECTIVE INTERPRETATION, Medium at best, corroboration 0 — and are **not** used in §D or §L-facing
rows as proof of dominance. The word "dominate" belongs to the 1965 report, not to this dataset's voice.

### H.4 The honesty ledger — what is NULL, what is UNANSWERED, and what was never tried

**Documented NULLs over held bytes (7). These are findings, and they are reported as such.**

| ID | Null | Over what |
|---|---|---|
| N1 | 0 hits for any month-name-with-1962 pattern; `July` appears 10× across the run, never with a 1962 Target opening | 11 layers, 781,995 chars |
| N2 | `Goodfellow` 0 and `\bDey\b` 0 → **Dey Brothers is unestablished**, and the four EDGAR full-text zeros over 1940-1995 are an **index floor (corpus begins 2001)**, not a null on the entity | 11 layers + `sources/name_search/fts_*.json` |
| N3 | `GEISSE` = 3 hits total (1965/66/67), 0 from FY1968; `DOUGLAS J. DAYTON` = 18 — name-presence counts in officer lists, **not** founder evidence either way | 11 layers, re-verified this session |
| N4 | No held layer prints **Target-unit** sales for 1962-1966, 1968 or 1970-1972; only 1967's `$86,901,007` | 11 layers |
| N5 | FY1969/FY1970/FY1971 `Five Year Comparisons` blocks print row labels with **no numeric columns** — a **rendering** null on held bytes; the data may exist in the report's own tables | 3 layers |
| N6 | Probe's byte count for the FY1970 layer (52,736) disagrees with disk and sidecar (**53,023**) — provenance correction so no pass re-imports it | 1 layer + sidecar |
| N7 | Catalog-level: the item's OCR run is **1965→2024**; nothing before FY1965 exists in it. Plus `Discount Store News` **numFound 0** in the reachable corpus — a catalogue absence, not a text null | `sources/ia_search/meta_01-target-archive.json`, `q_dsn.json` |

**UNANSWERED — 5, all tool or egress limits; a 403/429/503 is never an absence.**
(1) EDGAR name→CIK browse: **HTTP 503 on all four terms**, bodies held at
`sources/name_search/*.atom` (7,747 B each) → a separate predecessor registrant is **neither ruled in
nor out**. (2) Wayback CDX for `target.com*` and `dhc.com*`: **503**, bodies held at
`sources/web_archive/cdx_*.txt` (11,832 B each) → the 1999-2000 readoption pages unreached.
(3) EDGAR full-text zeros 1940-1995: **index floor 2001**, and the no-date-restriction control query was
never run. (4) `ia_text.py search` returns field-less docs on this build and `ia_text.py fetch` 404s on
IA filenames containing spaces → enumeration had to be done by hand; **tool defects, evidence-neutral**.
(5) **Verified TLS failed** on the five layers fetched by the records pass
(`CERTIFICATE_VERIFY_FAILED … certificate has expired`), so FY1966/67/71/73/74 are **UNVERIFIED TLS**
and every claim resting only on them is **capped at Medium** — the cap is applied in §A, §D, §E, §G and
in every register row below, and **lifting it is a fetch, not a judgment**.

**UNTRIED — 8, each with the exact route that would settle it.** **U-1** the item's own **17 PDF legs**
(1965-74, 1976, 1985-86, 1990-91, 1994) → re-OCR to settle **K6** (the one-store 1971 difference),
**K7** (`Target (1961)*` vs `(1967)*`) and **N5**; highest value per call left on this company.
**U-2** fetch the two unheld K1 carriers (2013-07-06 obituary; a Geisse obituary, NYT 1992-02) into
`sources/documentary/` with sidecars → K1 becomes adjudicable instead of merely recorded.
**U-3** HathiTrust / Google Books for `Target Stores, Inc.` 1962-66 and Dayton Company reports
FY1955-FY1964 (needs a `target` task set in `tools/queries.json`, which does not exist, plus
`--use-curl`) → **the only route that can move the tier from T2 to T1**, and the only one that can put a
document before FY1965 on this machine. **U-4** *Star Tribune* / *Pioneer Press* 1961-08→1962-12 →
the only route to a **day**, i.e. to closing K2. **U-5** a **second carrier** for the same years
(independently digitised Dayton reports in `fund-and-stock-reports`) → the only route to *any*
corroboration, because all eleven layers are one uploader's item. **U-6** `sec_intake.py facts` and the
FY1993 10-K selected-data table → the Tier-1 bridge leg back toward the decade.
**U-7** EDGAR name→CIK for predecessor registrants on a working route, then a 1930-1985 index → until
it runs, "one registrant line" is EDGAR's limit, not a proof. **U-8** re-fetch the five UNVERIFIED-TLS
layers after the CA store is repaired → lifts the Medium cap on Q3-Q8, Q16-Q19 and the FY1974 roster.

**Carry-forward to §S (part_2 owns §S; do not renumber these).** Every null, UNANSWERED and UNTRIED
item above is a §S row by reference, and §S must inherit: the 7 nulls, the 5 UNANSWERED with their
held-artifact paths, the 8 UNTRIED with their routes, plus the two corrections this volume opens
(**P1K10** fiscal-basis, **P1K11** the 1972-03-22 figure grepped to zero) and the **FETCH REQUEST** in
the release note. §S adds no new numbering onto A-H ids.

```
G01 Claim: For this company the host side is internal: the parent owned its site developer, its credit arm and its own first public disclosure, and Target's land/lease relationship to them is not printed in any held layer — Date: 1965-1966 — Source: FY1965 L722, L1463, L117-123; FY1966 L225-231 — Source date: 1965; 1966 — Tier: 1 — Class: FACT for the entities named; UNKNOWN for the Target site holding — Passage: "EIGHTH STREET DEVELOPMENT CO. 1927 DAYTON CREDIT COMPANY 1965" — Conf: High / UNKNOWN as asked — Corroboration: 0 independent — Conflicts: None
```
```
H01 Claim: The one independent in-window periodical held anywhere on this machine narrates the discount revolution without naming the company once — Date: 1963-04 — Source: Chain Store Age (Steel for Stores advertising section), Apr-1963 — Source date: 1963-04 — Local bytes: sources/periodicals_csa_1963/Chain_store_age_Steel_for_Stores_djvu.txt L4475-4479 (verified TLS, 170,260 B) — Tier: 1 (trade) — Class: CONTEMPORARY OBSERVATION of the category; NULL for the company — Passage: "Before the first—the shopping-center revolution—had run its course, the second—the discount store revolution—began to make itself felt." — Conf: High (category), High (that the company is absent: 0 hits over 168,433 chars) — Corroboration: n/a — Conflicts: None
```
```
H02 Claim: Every Stage-1 market-position claim for 1962-1965 rests on the company's own unquantified self-description, with no independent count behind it anywhere in the corpus — Date: 1965 — Source: FY1965 report — Source date: 1965 — Local bytes: 1965_dayton_hudson_djvu.txt L192-194, L398 — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION / corporate self-claim — Passage: "where its stores now dominate the discount field" — Conf: Medium — Corroboration: 0 — Conflicts: None — §2 note: recorded as an absence of third-party measurement, not as a reason to doubt the store estate, which §A does establish
```

---

>>> REGISTER ROWS FOR MERGE <<<

*Emit-only. **No register CSV on this company was opened, created or edited by this pass** — there are
none at the company root or under `research/` yet, and a merge pass applies these. `stage` is the
controlled literal **`stage1`** on every row (§13). All `P1x` ids are **dossier-local**; global
`source_id` blocks are assigned centrally at merge. Where a row restates a carrier B1 already emitted,
that is said in `notes` so the merge keeps **one** row and aliases the other rather than double-counting
a lineage. `independence_note` on every corporate-print row carries the §3 lineage finding; a value of
`not_derived` in `derived_arithmetic` means the cell is intentionally non-empty.*

### sources.csv — `source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes`

```csv
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
P1S01,stage1,"A01 A02 A03 B01 B03 B04 B05 C01 D01 E01 F01 F02 G01 H01 H02","The Dayton Company Annual Report 1965 (OCR text layer)",The Dayton Company,corporate stockholder report,primary,"1962;1965",1965,2026-09-26,"archive.org item 01-target-archive, per-year DjVuTXT layer (exact URL in file sidecar)","sources/corporate_print/1965_dayton_hudson_djvu.txt (48,050 B; verified TLS)",1,"CONTEMPORANEOUS for 1965 / RETROSPECTIVE for 1962",High,"one lineage; FY1973, FY1974 and FY1999 re-narrate the same self-account, which is version evidence not corroboration","The Company entered the discount merchandising field in 1962 with Target Stores, Inc., which now has five","SAME DOCUMENT as B1S01 - merge keeps one source row and aliases. New passages established this session: L110-115 (George Draper Dayton dry-goods ancestry), L159-166 (first public annual report), L421-423 (11 percent leased, Applebaum's), L1417-1436 (parent officers incl. Bruce B. Dayton as President), L123 (Brookdale 1962 adjacency, see P1K12)"
P1S02,stage1,"A01 (year-end) E01 F01 G01 P1K10","Dayton Company Annual Report 1966 (OCR text layer)",The Dayton Company,corporate stockholder report,primary,1966,1966,2026-09-26,"archive.org item 01-target-archive per-year DjVuTXT layer","sources/corporate_print/1966_dayton_hudson_djvu.txt (43,364 B; UNVERIFIED TLS)",1,CONTEMPORANEOUS,Medium,"officer list and estate list repeat P1S01 - same lineage","customers spend an average of more than $7.50 per visit, excluding groceries. This compares with an industry average of $5.05","TRANSPORT UNVERIFIED TLS so capped at Medium. Duplicate carrier of B1S02. Also prints 146,000 sq ft Denver pair (L205), quarter-million items (L206), 889,000 sq ft across seven stores (L219), land sale 1,771,355 (L228)"
P1S03,stage1,"B01 B02 D01 E01 G01 G02","Dayton Corporation Annual Report 1967 (OCR text layer)",Dayton Corporation,corporate stockholder report,primary,1967,1967,2026-09-26,"archive.org item 01-target-archive per-year DjVuTXT layer","sources/corporate_print/1967_dayton_hudson_djvu.txt (45,200 B; UNVERIFIED TLS)",1,CONTEMPORANEOUS,Medium,"first layer whose masthead reads Dayton Corporation; its unit dollars are a different denominator from its corporation capex","JOHN F. GEISSE (L1952) / Senior Vice President and General Merchandise Manager","TRANSPORT UNVERIFIED TLS. Duplicate carrier of B1S03. New passages: L177-182 Denver first full year and October openings, L189-192 capex $10,705,548 and 3,628,600 sq ft, L1197 year ended January 28 1967"
P1S04,stage1,"B05 G02 P1K10","Dayton Hudson Corporation Annual Report 1970 (OCR text layer)",Dayton Hudson Corporation,corporate stockholder report,primary,"1967;1970",1970,2026-09-26,"archive.org item 01-target-archive per-year DjVuTXT layer","sources/corporate_print/1970_dayton_hudson_djvu.txt (53,023 B on disk and in sidecar; verified TLS)",1,"RESTATED for 1967; CONTEMPORANEOUS for 1970",High,"a 1971-dated carrier reciting 1967 is one lineage; its store counts are corporation-level not Target-unit","When the Corporation made its first public stock offering in late 1967, it had 23 stores in five states.","Duplicate carrier of B1S06. Layer prints its own date line April 16, 1971 at L200 and Joseph L. Hudson, Jr / Bruce B.Dayton / K.N. Dayton at L203. Byte-count correction N6 applies"
P1S05,stage1,"H01 / N1-family null",Chain Store Age - Steel for Stores (April 1963 advertising section),Chain Store Age,trade periodical,primary for the category,1963,1963-04,2026-09-26,"archive.org item chain-store-age-steel-for-stores, file Chain store age - Steel for Stores_djvu.txt (percent-encoded)","sources/periodicals_csa_1963/Chain_store_age_Steel_for_Stores_djvu.txt (170,260 B; verified TLS)",1,CONTEMPORARY OBSERVATION,High,"THE ONLY INDEPENDENT IN-WINDOW CARRIER HELD; it does not name the company once","Before the first—the shopping-center revolution—had run its course, the second—the discount store revolution—began to make itself felt.","Grep over 168,433 chars: Target 0, Goodfellow 0, Minnesota 0; Dayton 2 (non-company), Hudson 3, discount 14. Not emitted by B1 - a new carrier for the merge"
P1S06,stage1,"A04 / N7 / boundary floor","Item metadata listing for archive.org item 01-target-archive","Internet Archive (catalog metadata; uploader labels are not evidence)",catalog metadata,secondary,2026,2026-09-26,2026-09-26,"archive.org/metadata/01-target-archive","sources/ia_search/meta_01-target-archive.json (259,567 B)",1,"CATALOG-LEVEL NULL",High,"metadata proves the run is 1965-2024; it proves nothing about what the company did before 1965",NO_VERBATIM_PASSAGE_RECORDED,"61 DjVuTXT layers, none before FY1965; 17 Image Container PDF legs 1965-74/1976/1985-86/1990-91/1994 exist unopened (UNTRIED-1); uploader file names label 1965-1998 as Dayton Hudson Corp (DH) which K3 refutes"
P1S07,stage1,"Boundary 1 (registrant line and formerNames)",Target Corp submissions index and raw submissions JSON,U.S. Securities and Exchange Commission,regulatory index,primary,1994,1994-02-10,2026-09-26,"sec.gov submissions API CIK 0000027419","sources/_index/raw_submissions_CIK0000027419.json (149,561 B, HTTP 200); sources/_index/submissions.csv (2,628 rows); _INDEX.md",1,FACT,High,"the registrant's own index; it cannot witness anything before its own floor",NO_VERBATIM_PASSAGE_RECORDED,"formerNames carries EXACTLY ONE entry: DAYTON HUDSON CORP 1994-12-09 to 1999-04-12. Earliest filing 1994-02-10 (SC 13G), first 10-K 1994-04-21; 0 of 2,628 rows earlier; no UNANSWERED slices. The script's normalised copy discards formerNames - the raw fetch is the reason the fact is known"
P1S08,stage1,"H.4 UNANSWERED 1-3 / N2","Negative artifacts: EDGAR name-to-CIK 503 bodies, EDGAR full-text zero-hit responses, Wayback CDX 503 bodies","SEC / Internet Archive (error pages)",HTTP negative artifact,secondary,2026,2026-09-26,2026-09-26,"sec.gov/cgi-bin/browse-edgar (action=getcompany) x4 terms; efts.sec.gov search-index x4 terms; web.archive.org/cdx x2","sources/name_search/*.atom (7,747 B each x4); sources/name_search/fts_*.json (4 zero-hit responses); sources/web_archive/cdx_targetcom.txt and cdx_dhc.txt (11,832 B each)",3,NOT-ANSWERED,High,"an error page is a dead route, never an absence; the FTS zeros are an index floor that begins 2001",NO_VERBATIM_PASSAGE_RECORDED,"Kept deliberately so no later pass reads a 503 as a null. Predecessor-CIK question stays open (UNTRIED-7)"
```

### quantitative.csv — `company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes`

```csv
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
Target,stage1,1966-01-29,fiscal_year_end_of_the_FY1965_report,1966-01-29,date,P1S01 L169-171,1965,FACT,High,not_derived,"CONFLICT P1K10 CARRIER: a report labelled 1965 ends 1966-01-29, so bare-year labels in Q1-Q20 are fiscal not calendar years; the FY1969 layer prints the key explicitly (year ended February 1, 1969 = fiscal year 1968)"
Target,stage1,1965,parent_net_retail_sales_growth_printed,14,percent,P1S01 L169-171,1965,FACT as printed; DERIVED as a check,High,"186,166,671 / 162,773,739 = 1.1437, i.e. 14.4 percent, consistent with the printed 14","CONTEMPORANEOUS; whole company NOT Target; the FY1966 comparative 189,776,071 is net sales AND rentals, a different denominator"
Target,stage1,1965,parent_net_income,7128981,USD,P1S01 L172-173,1965,FACT as printed; DERIVED as a check,High,"7,128,981 / 5,435,205 = 1.3116, i.e. the printed 31 percent gain foots","CONTEMPORANEOUS; prior year is the fiscal year ended 1965-01-30"
Target,stage1,1965,target_sales_growth_printed,44,percent,P1S01 L179-181,1965,FOUNDER-CLAIM-adjacent corporate claim; the base dollars are unprinted,Medium,not_derived,"gains of 44 percent in sales and 100 percent in pre-tax profits in 1965 over the previous year; no held layer prints the Target-unit dollars behind either percent (null N4)"
Target,stage1,1966,target_store_average_retail_area,127000,square feet,P1S02 L219,1966,ESTIMATE,Low,"889,000 total retail area / 7 stores = 127,000","DERIVED and printed nowhere; the same layer prints 146,000 sq ft for each of the two new Denver units, so the average hides an estate range; UNVERIFIED TLS"
Target,stage1,1965,target_leased_department_share_of_sales,11,percent,P1S01 L421-423,1965,FACT,High,not_derived,"explicitly EXCLUDES sales of the grocery departments operated by Applebaum's, so it is a share of a narrower base than total store trade"
Target,stage1,1966,target_average_basket_excluding_groceries,7.50,USD per visit,P1S02 L214-215,1966,company-printed statistic with no method given,Medium,not_derived,"printed as more than $7.50 against an unattributed industry average of $5.05; neither the average's carrier nor the sample is named, so the comparison is one sentence deep"
Target,stage1,1965,hennepin_county_women_who_shopped_target,51,percent,P1S01 L404-407,1965,CONTEMPORARY OBSERVATION second-hand,Medium,not_derived,"a Minneapolis Star and Tribune survey quoted by the company inside its own shareholder report; the survey is NOT HELD, so the figure is one carrier deep and unauditable"
Target,stage1,1967,corporation_capital_expenditures,10705548,USD,P1S03 L189-192,1967,FACT,Medium,not_derived,"CORPORATION level, not Target; same sentence prints total retail space 3,628,600 sq ft, so Target dollars divided by this space would be a meaningless ratio; UNVERIFIED TLS"
Target,stage1,1965,first_mortgage_note_planned_for_new_construction,7500000,USD,P1S01 L1232-1236,1965,FACT,High,not_derived,"verified TLS; the layer prints the rate mangled as 574 percent; monthly installments of 50,000; collateral pledged to mortgage notes aggregates 18,141,019. This is the construction finance behind the store estate, not a Target operating figure"
Target,stage1,1965,interim_financing_payable_to_the_parent,3200000,USD,P1S01 L1170,1965,FACT,High,not_derived,"the parent financed the unit's construction as an intercompany payable; no capital account for Target Stores, Inc. is legible in any held layer, so this is a lender relationship not an equity one"
Target,stage1,1966,first_mortgage_note_planned_for_the_two_1966_discount_stores,2200000,USD,P1S02 L804-809,1966,FACT,Medium,not_derived,"UNVERIFIED TLS; interim financing for the two stores constructed in 1966 was to be replaced by this note, quarterly installments 62,000 for five years then 50,000 for twenty"
Target,stage1,1966,annual_rentals_under_the_land_sale_and_leaseback,225000,USD per year,P1S02 L808-809,1966,FACT,Medium,not_derived,"TENURE EVIDENCE: the LAND under the 1966 discount stores was to be sold and leased back in 1967 while the buildings were mortgaged, so the unit held its buildings and not its land at least at this site pair; the sale price of the land is not printed"
```

### timeline.csv — `company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes`

```csv
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
Target,stage1,1965-1966,"The Dayton Company issues its first public annual report and states that projected growth requires it to expand beyond private ownership",The Dayton Company,"Minneapolis, Minnesota",P1S01,FACT,High,P1K10,"the disclosure event that creates the whole founding-decade archive; report label 1965, year ended 1966-01-29"
Target,stage1,1962,"Dayton Development Company opens Brookdale shopping center in a northern suburb of Minneapolis - the same year and the same page range as the Target entry sentence",Dayton Development Company,"Brooklyn Center, Minnesota",P1S01,FACT,High,P1K12,"MIS-CITATION TRAP: L122-123 sits one line above L124 and is NOT a Target opening; Roseville is separately printed as a suburb north of St. Paul at L397-398"
Target,stage1,1971-04-16,"The FY1970 report carries its own printed date line and recites the late-1967 first public stock offering",Dayton Hudson Corporation,UNKNOWN,P1S04,RESTATED,High,None,"a 1971-dated carrier for a 1967 and a 1970 fact; RESTATED, so it is version evidence and never corroboration"
Target,stage1,1975-12-31,"The FY1975 report prints a 31-December year-end against late-January or early-February year-ends in FY1965-FY1974",Dayton Hudson Corporation,UNKNOWN,P1S01,FACT,Medium,P1K10,"basis migration inside the stage window; any FY1974 to FY1975 series changes denominator and must say so; read at probe level in the FY1974 and FY1975 layers"
```

*(B1's thirteen timeline rows already carry the estate and offering sequences; this volume emits four
rows and duplicates none of theirs.)*

### decisions.csv — `company,stage,date,decision,state_before,information_available,unknowns,alternatives,constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref`

```csv
company,stage,date,decision,state_before,information_available,unknowns,alternatives,constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref
Target,stage1,1962,"The Dayton Company enters discount merchandising through a separately named subsidiary, Target Stores, Inc.","department-store house plus a shopping-centre development arm; no discount operation","what the company later said it knew: that some shoppers want low margins and convenience; its own store-building capability","every internal input: no memo, no study, no dissent, no rejected option survives","UNKNOWN - no alternative is printed in any held layer, and a first public report printed three years later is not a deliberation record","private ownership of the parent; the format's capital appetite","the company's retrospective framing only: conceived with the knowledge that there also will be people who wish to take advantage of low margins and convenience shopping","four stores operating by the close of 1962 as the company itself prints them","UNKNOWN within the stage; the FY1965 print reports five stores and a 44 percent sales gain, which is the company's own account of the outcome","P1S01",Low,"B01 B02 B03 D01"
Target,stage1,1965,"Issue the company's first public annual report","privately owned; figures not public","projected growth; the option of staying private","who argued for it, what was weighed, what the much deliberation consisted of","UNKNOWN","none printed","parent-level: projected growth requires it to expand beyond the concept of a privately-owned operation","disclosure will further growth possibilities, open expansion opportunities, and put management under public scrutiny","the first public stock offering followed in late 1967 (RESTATED by a 1971-dated report) and NYSE listing in 1969-09-08, both labeled RETROSPECTIVE and both outside this decision's own evidence","P1S01",Medium,"B05 G02"
Target,stage1,1965,"Plan the first venture outside the Upper Midwest, at Denver, for Fall 1966","five stores, all in Minnesota","what the company printed as the test: dominance at home in a heavily-competitive metro","whether any other candidate market was considered","UNKNOWN","capital and construction lead time implied by the interim financing note that follows","we believe the success of Target in the Minneapolis-St. Paul metropolitan area provides an operational format which can do as well in other areas","two stores opened in Denver in October 1966, total estate seven","FY1967 prints that in their first full year the Denver stores matched the initial home performance - the company's own claim, no independent audit","P1S01 + P1S02 + P1S03",Medium,"D01 E01"
```

### validation.csv and failures.csv — `company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes`

```csv
company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes
Target,stage1,1965,"Target sales up 44 percent and pre-tax profit up 100 percent over the previous year","44 and 100 percent","that the company could print a doubling of unit profit in its own report for its own year","nothing: no dollars, no base, no store-level breakdown, no auditor and no outside count are held for the unit in this period","P1S01","CONTEMPORANEOUS corporate claim",Medium,"the only Target-unit dollar printed anywhere in FY1962-FY1968 is FY1967's 86,901,007"
Target,stage1,1965,"51 percent of women customers in Hennepin County shopped a Target store","51 percent of a county's women customers","adoption depth in the home metro, as reported by a newspaper survey the company chose to quote","market share, sales, whether the survey defined shopped as entered, or anything outside one county","P1S01","second-hand CONTEMPORARY OBSERVATION",Medium,"survey NOT HELD; one carrier deep (UNTRIED-4)"
Target,stage1,1967,"Two new stores opened in October and operated at a profit for the year after absorbing all pre-opening expenses","2 stores, profitable in year of opening","that the format paid back inside its first partial year on the company's own accounting statement","the margin, the dollar amount, or whether the statement is auditable outside the report","P1S03","CONTEMPORANEOUS",Medium,"UNVERIFIED TLS cap"
Target,stage1,1966-10,"First out-of-market test: two Denver stores open","2 stores, 146,000 sq ft","that the company could build and open away from home","repeatability beyond one market; FY1967's claim that Denver matched home performance is the company restating itself","P1S02 + P1S03","CONTEMPORANEOUS",Medium,"UNVERIFIED TLS; the first genuine outside-market result is a retrospective sentence in the next year's report"
Target,stage1,1962-1975,"ABSENCE OF ANY PRINTED FAILURE in the founding decade","0 held negatives FY1962-FY1971","nothing positive; it is a property of the archive","that the venture did not fail, stall, close a store or lose money - a first public report is a selected record","all layers","UNKNOWN - record-selection null",High,"the first held in-window negative is FY1972: low-margin group pretax fell to 9,222,000 from 13,749,000, attributed in print to Target performance and start-up costs; logged in failures.csv"
```

### channels.csv — `company,stage,channel,date_tested,why_tested,cost_or_effort,result,repeatability,source_id,confidence,notes`

```csv
company,stage,channel,date_tested,why_tested,cost_or_effort,result,repeatability,source_id,confidence,notes
Target,stage1,"home-metro suburban new store (Twin Cities)",1962,"first real-world expression of the low-margin convenience concept","UNKNOWN - no per-store cost is printed in any held layer","4 stores operating in 1962, 5 by FY1965, 9 by FY1967 - all as printed by the company","proven only inside one metropolitan market on the company's own evidence","P1S01",Medium,"the estate count is CONTEMPORANEOUS for 1965-67 and RETROSPECTIVE for the 1962 rows"
Target,stage1,company-built store outside the home market (Denver),1966-10,"test whether the format travels","interim financing is named in the FY1966 notes; the amount is not legible","7 stores at year-end; FY1967 claims the pair matched home performance","one out-of-market data point; the next market cluster is 1968-69 and is B1's ground","P1S02",Medium,"UNVERIFIED TLS"
Target,stage1,"third-operated grocery concession inside the unit (Applebaum's) plus 11 percent leased departments",1965,"non-owned merchandising capacity inside a low-price box","UNKNOWN - terms not printed","11 percent of Target sales are leased-department sales, and the printed basket figure excludes groceries","UNKNOWN - no later layer in the run restates the 11 percent","P1S01",High,"the only named third-party merchandise operator anywhere in the founding decade; vendor file is UNTRIED-1"
```

### conflicts.csv — `company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence`

```csv
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
Target,stage1,P1K10,"Boundary 4; every row of B1's quantitative block carrying a bare year","fiscal year equals calendar year in these reports","research/B1_dayton_print_records.md, Store and sales series preamble",2026-09-26,"the reports print late-January or early-February year-ends and one layer prints the key itself: year ended February 1 1969 is fiscal year 1968","held layers FY1965 L169-173, FY1967 L1197, FY1969 L1451, FY1970 L1743, FY1974 L3220",1965-1974,"a dossier statement inherited the label 1965 as if it were a 31-December observation; the documents date the year-end","the held bytes win outright - five printed year-end dates across four layers, verified TLS on three of them","a report labelled N is a 52/53-week retail year ending in late January or early February of N+1; year-end store counts are January counts, and the FY1974 to FY1975 leg changes basis","whether any B1 row silently compares a January-1966 count to a December-1965 market figure is unresolved until the merge re-keys each date field","High"
Target,stage1,P1K11,"Boundary 2 (dispatch premise)","the documented floor for naming the company in the retail sense is 1972-03-22",the Stage-1 dispatch brief,2026-09-26,"the string 1972-03-22 (and its two alternate forms) occurs in ZERO bytes anywhere in the company directory",grep over founders_playbook/01_companies/company_042_target/ entire tree,2026-09-26,"a received date with no carrier: §14 rule 8 test run and failed","no weight to side A - it is not present in any filing, layer, index or negative artifact on this machine","the floor this volume can defend is three different floors: FY1965 document floor, 1962 event floor carried only by retrospective print, 1994-02-10 registrant floor; the 1972-03-22 figure is NOT written","where the 1972-03-22 date came from is UNKNOWN; if a carrier exists it is outside this company directory and must be fetched before use","High (that it is unsupported)"
Target,stage1,P1K12,"A.2; D.1; B.3","Brookdale shopping center opened in 1962 in a northern suburb of Minneapolis - FY1965 L122-123",P1S01,1965,"the first Target store opened early in 1962 in Roseville, a suburb north of St. Paul - FY1965 L397-398",P1S01,1962,"two different 1962 openings by two different subsidiaries, printed one line apart in the same document, with near-identical directional geography","both are the same primary document and both are true; neither corroborates the other","the 1962 entry into discount merchandising is the Roseville store and its three chronology companions; Brookdale is the development arm's centre and must never be quoted as a Target opening","which later secondary accounts conflated the two, if any, is UNKNOWN","High"
```

*(K1-K9 are **already emitted** in `research/B1_dayton_print_records.md` and are **not** re-emitted; this
volume's §Boundary and §B.2 cite them by id and add nothing that would require a merge to choose between
two rows for the same conflict.)*

### data_gaps.csv — `company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task`

```csv
company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task
Target,stage1,"any document naming the company before FY1965, and every date in the 1902-1961 pre-history",the digitised run starts at FY1965 (catalog-proven P1S06) and no family reached an earlier document,High,"the FY1965 report's own ancestry sentence (P1S01 L110-115) and the FY1999 spread - both company self-account",Low,"UNTRIED-3: HathiTrust and Google Books for Dayton Company reports FY1955-FY1964 and Target Stores Inc. 1962-66; needs a target task set in tools/queries.json plus --use-curl. THE route to T1"
Target,stage1,"month and day of the first Target store, and its size, address and first-year trade","held text says only early in 1962; month-with-1962 search returns 0 over 11 layers (N1)",High,"P1S01 L397-398",High,"UNTRIED-4: Minneapolis Star Tribune and St Paul Pioneer Press 1961-08 to 1962-12, plus Duluth News Tribune; UNTRIED-1: the item's 1965 PDF leg for the chronology page"
Target,stage1,"a held independent carrier for either founder attribution (K1)","both carriers are web leads; no obituary text or interview transcript is on disk",High,"officer pages only: P1S01 L1452-1459 and P1S03 L1950-1956, which establish ROLES",High,"UNTRIED-2: fetch the 2013-07-06 Twin Cities obituary and a Geisse obituary into sources/documentary/ with sidecars via the harvest script, not an agent"
Target,stage1,"Target-UNIT sales for 1962-1966, 1968 and 1970-1972",the reports printed the discount-and-hard-goods GROUP for those years and unit dollars only for 1967 (N4),High,"P1S03 1967 unit sales 86,901,007; P1S04 group 189,515,025",Medium,"UNTRIED-1 re-OCR of the five-year table PDFs; UNTRIED-3 for a Dayton Corporation prospectus with divisional schedules"
Target,stage1,"whether a predecessor registrant ever filed (Dayton Company / Dayton Dry Goods / J. L. Hudson)",the EDGAR name-to-CIK route returned HTTP 503 on all four terms and the bodies are held as negative artifacts (P1S08),Medium,"EDGAR formerNames with exactly one entry, plus a complete-as-indexed 2,628-row history with no unanswered slices",Medium,"UNTRIED-7: name-to-CIK on a working route then sec_intake index --cik n --from 1930-01-01 --to 1985-12-31"
Target,stage1,"verified-TLS status of five layers (FY1966 FY1967 FY1971 FY1973 FY1974) and therefore the confidence ceiling on every row resting only on them","verified TLS failed with CERTIFICATE_VERIFY_FAILED on an expired local CA bundle; the fetch used --insecure",Medium,"sidecars on all five stamp transport UNVERIFIED TLS",High,"UNTRIED-8: repair the CA store, re-fetch the same five URLs, re-stamp; this is a script run, not research"
Target,stage1,"the 1999-2000 readoption leg and the company's own digital history page",Wayback CDX returned 503 twice and the bodies are held; the print legs cover the same event better,Medium (PB material only),"FY1998 layer naming www.dhc.com; FY1999 layer We are Target Corporation; EDGAR formerNames end date 1999-04-12",Medium,"UNTRIED-9: Wayback retry once Internet Archive answers 200, plus the readoption press release"
Target,stage1,"what the 1962-65 stores cost, the land sale price inside the 1967 leaseback, and who the merchandise vendors were","site TENURE is now partially established from the notes pages (buildings mortgaged, land leased back); cost, price and vendor terms are not printed legibly anywhere in the run",Medium,"P1S01 L421-423 (11 percent leased, Applebaum's), P1S01 L1170 and L1232-1236 (3,200,000 payable to the parent; 7,500,000 first mortgage), P1S02 L355 and L804-809 (2,200,000 mortgage and 225,000 annual rentals)",Medium,"UNTRIED-1: re-OCR the FY1965-FY1967 notes, lease and mortgage schedules from the item's own PDFs before any external fetch"
```

**Row count requested: 47** — sources 8 · quantitative 13 · timeline 4 · decisions 3 ·
**validation 4 + failures 1** (the two registers share one column list per §13; the fifth row in that
block, `ABSENCE OF ANY PRINTED FAILURE`, belongs in `failures.csv`, the other four in
`validation.csv`) · channels 3 · conflicts 3 · data_gaps 8. Every block was machine-checked this pass
for column drift and for empty cells: 0 misaligned rows, 0 empty cells. Four of the quantitative rows
were added **after** the §G notes pages were read, and one §G claim (site tenure UNKNOWN) was
retracted in the same pass that added them. B1's 65 rows are **not** duplicated here; the merge applies
both sets and aliases the five shared carriers named in `notes`.

**FETCH REQUEST (for the orchestrator to run with `tools/periodical_harvest.py` / `ia_text.py`, not for
an agent):** item `01-target-archive`, per-year **PDF** legs for FY1965, FY1966, FY1967, FY1969, FY1970,
FY1971, FY1973 → destination `sources/corporate_print_pdf/` with sidecars; purpose: settle **K6**, **K7**,
**N5** and the unit-versus-group columns this volume had to leave UNKNOWN. Second request: the two K1
obituary carriers → `sources/documentary/`. Third: a `target` task set in `tools/queries.json`
(HathiTrust, `--use-curl`) for Dayton Company reports FY1955-FY1964. This pass used **WEB BUDGET 0** and
fetched nothing.
---

>>> VOLUME 2 -- sections I-U, claim records and the register emissions (from `_parts/s1_p2.md`) <<<

## Part 2 assembly note (read before merging)

Volume 2 of Stage 1 (sections §I–§U). Sibling volume `_parts/s1_p1.md` owns the header block, the
boundary argument and §A–§H; nothing here restates them, and nothing here rewrites its path.

**Anchor padding.** At the time this volume was written, `_parts/s1_p1.md` was still a scaffold
skeleton (every section PENDING), so no §U anchor had been minted by the sibling pass. Per the
dispatch contract this volume therefore mints **zero-padded three digits, U.001–U.037, continuous,
one style, no gaps**, declared below for `gates.py` anchor parity. If p1 minted anchors after this
note was written, the merge re-keys this volume's block (U.101-up is the free range suggested) and
alias-maps rather than deleting.

    <!-- ANCHORS: U.001-U.037 -->

**Dossier-local ids used here and what they mean at merge.** `B1S01`–`B1S14` are the source ids
emitted by `research/B1_dayton_print_records.md`; `P2S01`–`P2S08` are new sources this volume
introduces; `P2-01`–`P2-10` are new claim records. All are dossier-local per method §13 and carry
**no** global-uniqueness claim; the register is the only place global ids live, and `source_id`
blocks are assigned centrally at merge.

**Boundary usage and `(PB)`.** The probe argues Stage 1 for **The Dayton Company at FY1965
narrating 1962**, with the Stage-1→Stage-2 hand-off at **1969**, the first year the report
masthead reads Dayton Hudson. Applied in this volume: every claim whose event date or evidence year
falls after 1969 carries `(PB)` (post-boundary) at the end of its line. FY1965–FY1968 print is
in-span; the FY1972/FY1973/FY1974 recap tables and everything from the 1999/2000 leg are `(PB)`
and are used only as consequences or as restatements, never as in-span observation.

**Citation form.** Stable label plus document path, never a line number (method §14 rule 12). A
citation reads `B1S01, sources/corporate_print/1965_dayton_hudson_djvu.txt, LEASES note`, where the
named part is a heading or table label printed in the document itself. Line numbers appearing in
the two research dossiers are **not** carried forward; they were used only to locate the text, which
was then re-read and quoted from the layer.

**What this volume found in the bytes that its own brief did not anticipate** (each is an anchor in
§U and a register row at the end, so the merge cannot lose it): the FY1965-titled layer reports a
fiscal year **ended 1966-01-29** and labels the same column both "1965" and "1966" inside one
document (**U.011** — this refutes the inherited dossier's premise that "fiscal year = calendar year
in these reports", and it re-bases every date in the store and sales series); a **LEASES note** and a
consolidated **Rentals** line exist at parent scope, so "no lease data" is wrong and "no per-store
lease terms" is right (**U.012**, §K); a Target Stores, Inc. **loss carry-forward available in 1964**
is printed in the tax note (**U.016**, §K/§M); the company calls itself a **privately-owned
operation** issuing its **first public Annual Report** in the same layer that a later report says
preceded its first public stock offering (**U.017**); the Target-unit growth rates (44% sales / 100%
pre-tax) and the parent growth rates (14% / 31%) are different denominators (**U.013**); the FY1966
"total retail area of the seven Target stores … 889,000 square feet" and the FY1974 roster's per-store
`(000)` column for the same seven units do not reconcile (**U.012**); the held *Chain Store Age* layer
prints **APRIL 1962** in one running foot inside an otherwise APRIL 1963 gather (**U.014**); and the
fourth 1962 store is printed **`KNOLLWOOD, ST.LOUIS PARK`** with no space after the abbreviation
(**U.015**), transcribed as printed throughout.

## I

### I.1 What the held record can say about competition

The company's own competitive claim is the only competition statement printed in the founding-decade
layers. Verbatim, as printed: `We believe the success of Target in the heavily-competitive
Minneapolis-St. Paul metropolitan area, where its stores now dominate the discount field, provides an
operational format which can do as well in other areas of the country.`
(`B1S01`, `sources/corporate_print/1965_dayton_hudson_djvu.txt`, "the people we serve" letter,
paragraph beginning "To increase our share of the market in the area we serve".)
Class **FOUNDER CLAIM — contemporaneous, self-asserted**; confidence **Medium** (a Tier-1 document,
but a claim about the writer's own market position with no independent count behind it — §2's
record-selection null applies: no third-party store census for 1965 is held).

A second self-description, more useful because it is behavioural rather than boastful: `The five
Target stores in Minnesota maintain a separate identity within The Dayton Company. Target has its own
management staff, its own buying organization, and freely competes for customers and employees.`
(`B1S01`, same layer, "Target Stores, Inc." essay.) Class **FACT** (that the entity published this
organisational description), confidence **High**. Its analytical content is that the declared
competitor set in 1965 included **the parent's own full-price house** — the framing of Target's
launch in the same essay is substitution within the company, not conquest outside it: `there also
will be people who wish to take advantage of low margins and convenience shopping through the
economies of mass merchandising` (`B1S01`, same essay). Class **RETROSPECTIVE INTERPRETATION**
(printed 1965/66 about a 1962 decision).

The one third-party competitive observation in the corpus reaches the reader **through the company**:
a `Minneapolis Star and Tribune` survey of suburban shopping habits titled `Retail Revolution 1955-1965`,
quoted inside the FY1965 report as disclosing `that 51 percent of women customers in Hennepin County
shopped at a Target store in 1965`, with the quoted conclusion `When shopping at specific centers is
considered, the most significant change is the emergence of Target as the leader.`
(`B1S01`, same layer, the paragraph following "There are now five Target stores"; claim record
`B1-07`.) Class **CONTEMPORARY OBSERVATION (second-hand)**; confidence **Medium**; independence
**zero** — the survey document is not held, the company selected it, and it is favourable to the
company. It is one carrier deep and cannot be audited. `(PB)` for the survey's own date-window
(1955-1965) which extends past the founding act.

### I.2 What is not establishable, and which route would establish it

No held document in this corpus enumerates the 1962 discount field by name. This volume did **not**
run a rival-name search across the eleven founding-era layers, so the absence of rival names is
recorded here as an **examination not performed**, not as a finding of absence: see §S (`U.021`,
`U.032`, `U.034`) for the routes that would settle it, including the negative result the probe *did*
run on held bytes — the one held trade-periodical leg, `sources/periodicals_csa_1963/
Chain_store_age_Steel_for_Stores_djvu.txt`, whose greps return `Target` **0**, `Goodfellow` **0**,
`Minnesota` **0** against `Hudson` **3**, `Dayton` **2** (both non-company: `DAYTON, OHIO` and a
`DAYTON—Scheduled for an October open-` item), `discount` **14**
(`A_chronology_feasibility.md`, "Family c periodicals"; NULL `N1`/`N5`).

What that one leg *does* contribute to the competition picture is the shape of the industry the
entity entered. It is an *Chain Store Age* April 1963 advertising gather ("Steel for Stores") whose
masthead list cites *Discount Store News*, and whose editorial phrase — `the second—the discount store
revolution` — puts discounting inside a named two-part industry transformation. Its company names are
the **Detroit line, not the Minneapolis line**: `HUDSON PLAZA`, `J. L. HUDSON REAL ESTATE CO.`,
`Hudson House, Inc.` Class **CONTEMPORARY OBSERVATION**; confidence **High** for what the layer
contains and **zero** for what it says about Target, because it says nothing. The trade paper that
would have carried a 1962 Target opening story has **0 items** in the reachable corpus
(`A_chronology_feasibility.md`, NULL `N4` — a catalogue absence, not a text null).

**Adaptation note (method §7).** For a 1962 retailer the standard "competition" frame — rival product
platforms — is replaced by rival **store estate and local market share**. A per-market competitor count
is UNKNOWN at Tier 1; the only held competitive geography is the company's own opening sequence
(§Q), whose logic is stated in print: expansion `in accordance with plans to expand into other
metropolitan areas which offer potential similar to that of the Twin Cities and Duluth`
(`B1S01`, "Target Stores, Inc." essay).

STATUS: WRITTEN 2026-09-25

## J

### J.1 Technology, adapted: store plant, merchandise control, and the accounting stack

Nothing in the held founding-decade record describes a product technology. What the documents do
disclose is the operating apparatus of a 1960s discount chain, and three of its four parts are
nameable from bytes.

**(a) Store plant and site engineering.** The FY1965 layer's plant references are all to the
full-price and centre side, not to Target: a `12,000 square foot auditorium in 1963, the country's
largest` and `Parking ramps with space for 825 cars` (`B1S01`, department-store and centre sections;
the auditorium sentence is truncated at its line end in OCR and is quoted as a fragment, not as a
complete statement). Class **FACT (as printed)**; confidence **Medium** (OCR truncation). The Target
side prints **area, count and location only** — see (d).

**(b) Merchandising method, stated by management as a technology.** `Merchandising techniques which
provide excitement in shopping; selection of prime traffic locations, and an outstanding food
operation` are listed by the company as essential to successful operation, alongside `domination of
the market in the number and quality of products available` (`B1S01`, "Target Stores, Inc." essay,
paragraph opening "Target management considers a number of factors"). Class **FOUNDER CLAIM —
contemporaneous** (management's own success criteria); confidence **Medium**; independence one.

**(c) Merchandise control and the accounting stack — the load-bearing technology disclosure.**
`Substantially all merchandise inventories on hand and in transit are priced at cost under the retail
method on the last-in, first-out basis`, and the layer prints the cost of that choice: inventories are
stated at `664,219 — 1966` and `431,573 — 1965` **less** than the amount that would have been
determined under the retail method without regard to LIFO (`B1S01`, MERCHANDISE INVENTORIES note).
Class **FACT**; confidence **High** (verified-TLS layer, audited statement). In the same document the
company reports that it `changed its method of accounting for depreciation for financial purposes
from accelerated to straight-line methods while continuing accelerated methods for income tax
purposes`, `reflected retroactively`, with the amounts printed: `$1,399,654` of income taxes at
January 30, 1965 reclassified from current to deferred, retained earnings at February 1, 1964
increased by `$938,934`, and net income for the year ended January 30, 1965 increased by
`$406,783` (`B1S01`, the note immediately preceding the cost-and-expense note). Class **FACT**;
confidence **High**.

The next year's layer reports the **same class of change with different numbers**: it `has decreased
net income for the year ended January 29, 1966 by $177,680 and has increased retained earnings at
January 30, 1965 by $37,665` (`B1S02`, `sources/corporate_print/1966_dayton_hudson_djvu.txt`,
notes). Class **FACT**; confidence **Medium** (`B1S02` is an UNVERIFIED-TLS layer, `U.028`).
These two statements are **not** a contradiction — they attach to different effective dates
(Feb 1 1964 vs Jan 30 1965) and different years — and this volume records that it **checked and did
not open a §U anchor for them**, which is the discipline the reverse of §14 rule 8: an apparent
conflict that the dates dissolve must not be minted either.

**(d) Store-plant quantitative technology, and its two bases.** The only Target-unit plant data in the
founding decade are `Total retail area of the seven Target stores now in operation is 889,000 square
feet.` (`B1S02`, the subsidiary-division narrative) and, nine years later, a per-store `(000)` column
in the FY1974 estate roster whose seven earliest rows sum to `722` for the same seven units
(`B1S10`, `sources/corporate_print/1974_dayton_hudson_djvu.txt`, LOW MARGIN STORES roster,
columns headed `(000) Opened`). The two do not reconcile and **no attempt is made here to reconcile
them**: the basis of the roster column (selling area vs total retail area) is not printed legibly in
the OCR, so a ratio between the two would be arithmetic on unknown denominators. See `U.012`; §K
refuses the division.

**(e) Credit machinery, dated to the day.** The FY1965 layer carries separate subsidiary statements for
a finance company `which commenced operations on January 15, 1966` and a deficit `from January 15,
1966 to January 29, 1966` (`B1S01`, NOTE A of the subsidiary statements). Class **FACT**; confidence
**High**. This is the earliest held date in the entire corpus attached to any operating act, and it
sits **inside** the same fiscal year as the 1962-origin narrative — a reminder that the layer's
"1965" is a fiscal wrapper, not a calendar year (`U.011`).

### J.2 The technology the record cannot supply

Store-systems detail (receiving, pricing, stock-location practice), headcount, wage structure and any
management-information capability are UNKNOWN: none is printed in any held founding-decade layer, and
this volume did not run a negative search for those terms, so they are logged as
**examination-not-performed gaps** in §S (`U.021`) rather than as documented nulls. The trade press
that carried the equipment story of the period is present in this corpus only as one 1963 advertising
gather whose searchable text names no Target plant decision — see `§I.2` and `U.014`.

STATUS: WRITTEN 2026-09-26 (stamped by scaffold; duplicate empty block from the scaffold skeleton removed by this volume's owner)

## K

### K.0 The rule this section writes under

A number is entered only if it is printed in a document held on this machine. Where a number is not
in a held document the cell reads **UNKNOWN** and names the gap and the route (`§S`, `§U`). Where a
figure is computed, the arithmetic is shown in the row and the row is classed **DERIVED** with
`derived_arithmetic`; **no per-store figure in this volume is produced by dividing a number from one
fiscal year by a count from another**, and the two places where that temptation is closest
(`$3,750,000` of facility commitments against two Denver stores; group revenue against Target-unit
counts) are named and refused below rather than quietly skipped.

### K.1 The founding act has no personal-money carrier

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Who funded the 1962 launch | UNKNOWN at Tier 1; the only funded actor named in held print is the parent company itself (`The Company entered the discount merchandising field in 1962 with Target Stores, Inc.`) — `B1S01`, `sources/corporate_print/1965_dayton_hudson_djvu.txt`, Financial Review | one company self-account | High that the text says this; UNKNOWN as to capital actually committed |
| Founder equity contributed | **UNKNOWN — no carrier exists in any held document**, and no search of any auction, museum or personal-estate corpus has been run (`U.030`, `U.032`) | — | UNKNOWN |
| Personal loan / guarantee | UNKNOWN, same basis | — | UNKNOWN |
| Company status at the moment of disclosure | `The projected growth of The Dayton Company requires that it expand beyond the concept of a privately-owned operation. To this end, … we are issuing our first public Annual Report.` — `B1S01`, opening letter (heading printed `o the people we serve`) | Tier-1 verified-TLS layer | High |
| Capital committed to the first store | UNKNOWN; the nearest held money statement is an **aggregate, whole-company, subsequent-events** figure (`U.013`) | `B1S01`, SUBSEQUENT EVENTS note | UNKNOWN |

The structural point, and it is the section's real finding: this company's first experiment was **an
internal division of a going concern that was not yet public**, so the record type that carries
"founder money" for the other companies in this dataset simply was never produced. The disclosure
decision is printed; the balance-sheet act it was meant to serve (a public stock offering) is dated by
a *different* report four years later (`When the Corporation made its first public stock offering in
late 1967, it had 23 stores in five states` — `B1S06`, FY1970 Operating Review; class **FACT**,
confidence **High**, event month UNKNOWN). See `U.017` for why those two statements are one sequence
and not a contradiction.

### K.2 What the founding-decade balance sheet actually printed (`B1S01`, financial statements and notes)

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Net retail sales, incl. leased departments, 12 months ended 1966-01-29 | `$186,166,671` (prior column `$162,773,739`, year ended 1965-01-30) | `B1S01`, Statement of Income + SALES note | High |
| Operating income | `$14,233,981` (prior `$9,616,914`) | `B1S01`, Statement of Income | High |
| Net income | `$7,128,981` (prior `$5,435,205`; printed growth `31 percent`) | `B1S01`, Statement of Income + EARNINGS note | High |
| EPS | `$1.99 during fiscal 1965`, restated prior year `$1.41`, `The increase was 41 percent` | `B1S01`, EARNINGS section | High |
| Cost of sales, buying **and occupancy**, combined | `$139,686,954` (current column) / `$123,584,592` (prior) | `B1S01`, note preceding MERCHANDISE INVENTORIES | High |
| Selling, general and administrative | `$31,256,511` / `$28,508,046` | `B1S01`, same note | High |
| Rentals (income-statement line) | `$2,088,720` / `$1,972,450` | `B1S01`, Statement of Income, deduction block | High |
| Long-term lease minimum annual rentals (aggregate) | `approximately $1,564,220`, `of which $626,683 is payable to unconsolidated subsidiaries`; `Most of these leases require the payment of real estate taxes and other expenses and, in certain instances, increased amounts based on percentage of sales.` | `B1S01`, LEASES note | High |
| Sinking fund notes | `$13,600,000` at `5% %` (as printed), maturing `$800,000` annually each January 31st 1965-1981, balance 1982-01-31 | `B1S01`, LONG-TERM DEBT note (1) | High |
| Mortgage notes | `$2,124,960` | `B1S01`, LONG-TERM DEBT note (2) | High |
| Commitments for additional facilities | `approximately $3,750,000` | `B1S01`, SUBSEQUENT EVENTS | High |
| Share structure actions | ten-for-one split approved at the February 1966 annual meeting; `stock dividend of one share … for each share outstanding after the stock split`, `transfer of $1,535,500 from retained earnings to Common Stock in March 1966` | `B1S01`, SUBSEQUENT EVENTS | High |
| Target-unit revenue, FY1962-FY1966 | **UNKNOWN** — one unit figure is printed in the whole founding decade, 1967's `$86,901,007` (`B1S03`), and none before it (NULL `U.021`) | — | UNKNOWN |
| Target-unit cost, margin, rent, wage, or build cost, any year | **UNKNOWN** — not printed at unit scope anywhere in the eleven layers | — | UNKNOWN |

Two refusals, stated rather than hidden. **(1)** The `$3,750,000` commitment is the consolidated
company's forward facility commitment and the two Denver stores are one line of that schedule;
`3,750,000 ÷ 2 = $1,875,000 per store` is **not** written anywhere in this volume, because the
numerator is whole-company (it covers Dayton's, the centres and the credit company's facilities too),
the denominator is a single subsidiary's opening plan, and the two statements carry different period
labels (`U.011`). **(2)** The rentals line `$2,088,720` and the LEASES-note `$1,564,220` are **not** an
inconsistency: the first is total rental expense for the year, the second is contractual minimum
rentals on long-term leases at a date. Both are parent-scope, and neither can be attributed to Target.
That is the whole of the lease evidence, and the honest form of the brief's "no lease terms" is:
**lease aggregates and clause types are printed at parent scope; lease terms per store, store-level
rent, and any Target-unit occupancy cost are not printed at all** — occupancy is welded into
`Cost of sales, buying and occupancy expenses` and cannot be separated by any held document.

### K.3 The five-year low-margin row, 1969-1973 `(PB)` — the closest the corpus comes to unit economics

From `B1S09`, `sources/corporate_print/1973_dayton_hudson_djvu.txt`, the `Five Year Comparisons —
Dayton Hudson Corporation and Subsidiaries` block, section heading printed `LOW MARGIN STORES`,
columns headed `1973 1972(*) 1971 1970 1969`. Row labels are OCR-corrupted; **values are transcribed in
column order exactly as printed**, with the decimal-position reading shown as an inference from the
same row's own percentage figures:

| Row (as printed) | 1973 | 1972 | 1971 | 1970 | 1969 | Src | Conf |
|---|---|---|---|---|---|---|---|
| `SOLS AMIS)` — Sales (millions) | $470.3 | $440.4 | $345.8 | $289.0 | $233.5 | B1S09 five-year block | Fact:High |
| Earnings before allocated interest and income taxes (millions), printed `$ 108 $ 13.3 $ 17.3 $ 12.8 $ 10.9` | 10.8* | 13.3 | 17.3 | 12.8 | 10.9 | B1S09 five-year block | Fact:High / *:Low |
| `POreehtt0. SObGS` — Percent to sales | 2.3% | 3.0% | 5.0% | 4.4% | 4.7% | B1S09 five-year block | Fact:High |
| Allocated interest (millions), printed `$ 42 $ 4A $ 36 $ 4.0 $31` | 4.2* | 4.4* | 3.6* | 4.0 | 3.1* | B1S09 five-year block | Fact:High / *:Low |
| Earnings before income taxes (millions), printed `$ 66 $ 9.2 $$. 137 $ 88 $ 78` | 6.6* | 9.2 | 13.7* | 8.8* | 7.8* | B1S09 five-year block | Fact:High / *:Low |
| `Percent to sales` | 1.4% | 2.1% | 4.0% | 3.0% | 3.3% | B1S09 five-year block | Fact:High |
| `NamiberF OF StOFES` — Number of stores | 50 | 50 | 34 | 27 | 19 | B1S09 five-year block | Fact:High |
| Total square feet (thousands) | 5,563 | 5,518 | 4,220 | 3,516 | 2,390 | B1S09 five-year block | Fact:High |
| `Sales persauara footy` — Sales per square foot | $84.54 | $79.81 | $81.94 | $82.18 | $97.70 | B1S09 five-year block | Fact:High |

The `Src`/`Conf` cells state the provenance of the **printed digits** (the layer and the confidence
that the layer says this). The block as a whole carries one further qualification, applied to every
cell: `B1S09` is an UNVERIFIED-TLS layer, so any claim resting on it alone is capped at **Medium**
(`U.028`), and the 1972 column is itself a restatement inside a 1973 report (`RESTATED`, §K.7).

`*` = decimal position restored by the row's own percentage check, shown as arithmetic and **not** as
an observed digit: `470.3 × 1.4% = 6.58 → "$ 66"`; `345.8 × 4.0% = 13.83 → "$. 137"`;
`233.5 × 3.3% = 7.71 → "$ 78"`. The whole block foots to its own sales row in all five columns
(`470.3 / 5.563 = $84.5`, `440.4 / 5.518 = $79.8`, `345.8 / 4.220 = $81.9`, `289.0 / 3.516 = $82.2`,
`233.5 / 2.390 = $97.7`), which is the reason this row and not the store counts is the strongest
unit-economics evidence held. Class **FACT as to the printed digits**, **DERIVED as to the decimal
restorations** (`derived_arithmetic` recorded in the register rows), confidence **Medium** for the
whole block because `B1S09` is an UNVERIFIED-TLS layer (`U.028`).

Three readings this row supports, and one it does not. It supports: **productivity fell as the estate
grew** (`$97.70 → $84.54` sales per square foot across 1969→1973, i.e. `−13.5%`; DERIVED from two
cells of one row, one basis); **the group margin compressed faster** (pre-tax `3.3% → 1.4%` of sales);
and **store count and square footage were reported together, for a reporting group, not for Target**
(`LOW MARGIN STORES` also carried the Lechmere hard-goods units — see `U.010`, and `B1S04`'s
`Discount and Hard Goods Stores` heading for the same units under the earlier name). It does **not**
support a Target per-store revenue for any year: the numerator is group, and the Target-unit
denominators in §P come from a different reporting object. Group per-store revenue **is** computable
within one column and is written once, as DERIVED: `233.5m ÷ 19 = $12.29m` (1969),
`440.4m ÷ 50 = $8.81m` (1972) — `(PB)`, group basis, `B1S09`, confidence **Medium**.

### K.4 Target's own profit history: one sentence, and it is a negative

The unit's earliest profitability statement in the corpus is a tax statement about losses. Explaining
why after-tax growth trailed pre-tax growth, the FY1965 layer prints: `The percentage increase in
after-tax earnings was somewhat less because of a substantial loss carry-forward available to Target
Stores, Inc., in 1964.` (`B1S01`, EARNINGS section.) Class **FACT**; confidence **High**; the
**magnitude is UNKNOWN** and is not printed anywhere in the eleven layers. Read against the same
document's growth claim — `The potential of Target is demonstrated by gains of 44 percent in sales and
100 percent in pre-tax profits in 1965 over the previous year` (`B1S01`, opening letter) — the held
record therefore contains a discount unit that was still carrying accumulated losses as of 1964 and,
two sentences apart from the same printer, a unit doubling its pre-tax profit. Those are not in
conflict; they are a small base and a fast year, and the base is not printed. See `U.013` (which
growth rate belongs to which entity) and `U.016` (the carry-forward sentence as the only unit-level
P&L statement before FY1967).

### K.5 What this section could not quantify, and why

Per-store build cost, per-store rent, wage or payroll structure, store-level selling-area cost, Target
inventory turn, Target gross margin, and Target revenue for 1962-1966 and 1968-1972 are all UNKNOWN at
Tier 1. The reason is a reporting-scope fact, not a retrieval failure: the entity reported **a
department-store company with a discount subsidiary**, and it printed the discount subsidiary in
**counts, locations, square feet and growth percentages**, reserving dollars for the reporting group
and for the consolidated company. This pass's own negative read is on record and reproducible: the
terms `payroll`, `wages` and `number of employees` return **no hits in the FY1965-FY1972 layers** and
first appear in the FY1974 layer (`payroll dollars`, real-estate discussion) and the FY1975 layer
(`occupancy expense, payroll, advertising and other expenses`; `payroll and non-payroll orented costs`
— the second word-group is OCR-corrupt and is quoted as printed), i.e. only after the Stage-1
hand-off. `(PB)`; class **FACT (negative on held bytes)**; confidence **Medium** (a term search is a
search for those strings, not a proof the data are unprinted elsewhere in the same pages).

### K.6 Where this differs from Amazon, Walmart and Apple

The three exemplars in this dataset each have a **personal-capital carrier** in Stage 1: a founder's
own savings, a family loan, or a sold asset, retold by the founder and quotable at Tier 1-2. This
company has none, and not because the search failed. Its founding act was a capital allocation inside
a private company that had not yet issued a public annual report (`B1S01`), so the documents that
would carry a personal-money story — a founder's interview about what he risked, a promissory note, a
partnership agreement — are outside the document class that survives for this entity. The second
difference is arithmetical: Amazon's and Walmart's early §K figures are **same-document ratios**
(dollars and denominators printed side by side), whereas here the dollars and the counts are attached
to **different reporting objects** (consolidated company / low-margin group / Target unit) in the same
paragraph, which is precisely the trap that makes a per-store Target revenue for 1969 look derivable
when it is not (`U.010`, `U.012`, `U.016`). The third is the fiscal-year trap: this company's own
cover-year and statement-year labels diverge by one (`U.011`), an error class that did not arise for
the exemplars because their early records are SEC filings with defined period ends and none exists
here before 1994-02-10 (`U.027`).

### K.7 As-filed vs restated, and which entity said it (applies to every row in §P)

`B1S01` is mastheaded in its own bytes as `THE DAYTON COMPANY @ ANNUAL REPORT 1965` and its balance
sheet is headed `THE DAYTON COMPANY AND RETAIL SUBSIDIARIES`; `B1S03` reads `Dayton Corporation`;
`B1S05` onward reads `Dayton Hudson Corporation`; `B1S11` carries the third-party provenance line
naming `ProQuest Historical Annual Reports` inside the FY1975 layer. The uploader's per-year file
names label **all** of these `Dayton Hudson Corp (DH)` and are wrong for the early years (`U.006`).
Every financial row in this volume therefore carries three stamps in the register: **masthead year**,
**entity name as printed**, and **CONTEMPORANEOUS / RESTATED / DERIVED**.

The restatement rules this volume applies:

1. A later report's recap of an earlier year is **one source in a later year**, never a second
   corroboration (§3 filing-lineage rule). `B1S09`'s 1968-1972 columns agreeing with `B1S04` and
   `B1S08` proves the company carried its own number forward, nothing more.
2. A restatement under a **wider consolidation** is a different entity's number. The 1968
   department-store column printed `582,923` (thousands) in `B1S05` is the merged Dayton Hudson
   scope; the same year's `223,276,791` printed in `B1S04` is Dayton Corporation alone. Both are
   correct for their own filer and neither corroborates the other (`U.010`).
3. **A retrospective recap can be the only carrier of a number at all.** `Target has grown from 11
   stores to 46 stores in five years.` is printed in `B1S09` (a 1973 report), and it is the only held
   statement of an eleven-store 1968 Target year-end count; it is used in §P as a **RESTATED** row,
   never as a contemporaneous 1968 observation, and never as independent evidence for the 1969/1970
   counts, which are DERIVED from it plus printed opening lists (`U.016`).

### K.8 Interpretive coda (§7 duty on takeaways)

What the founding decade's money record shows is a **store-count business reporting dollars at two
higher levels than the one the story is about**. The mechanism is printed, not inferred: the company's
own reporting groups (`Department Stores`, `Discount and Hard Goods Stores` later renamed
`Low Margin Stores`, `Specialty`) define the numerators, while Target is reported in units of estates
(`five stores`, `seven stores … 889,000 square feet`, `46 stores in nine states`). The consequence is
**structural** — the earliest discount economics recoverable for this company are productivity ratios
at group scope, not unit economics. The alternative explanation, that unit-level Target statements
existed but were not digitised in the item this corpus holds, is **not excluded by anything here**,
which is why `U.034` (a second carrier) and `U.032` (HathiTrust pre-1965 reports) are the highest-value
open routes rather than footnotes. Confidence in the mechanism: **High** (it is what the pages print).
Confidence that no unit-level statement exists anywhere: **UNKNOWN**.

## L

### L.1 Validation signals present in the record

| Date | Signal | Magnitude | What it demonstrated | What it did NOT demonstrate | Source | Confidence |
|---|---|---|---|---|---|---|
| 1962-1965 | Four stores in 1962 to five by the Bloomington opening, all in one metro plus Duluth | +1 store | the format repeated outside its opening suburb and to a second in-state city | demand outside Minnesota; unit profitability (`U.016`) | `B1S01`, store chronology spread + "Target Stores, Inc." essay | High |
| FY1965 | Parent-printed unit growth rates | `44 percent in sales and 100 percent in pre-tax profits in 1965 over the previous year` | the company chose Target's growth as its published proof of concept | absolute dollars (no unit base is printed); self-reported | `B1S01`, opening letter | Medium |
| 1965 | Third-party adoption figure, quoted by the company | `51 percent of women customers in Hennepin County shopped at a Target store in 1965` | local penetration as reported by a newspaper survey | causation, loyalty or margin; the survey itself is not held | `B1S01`, quoting `Retail Revolution 1955-1965` | Medium |
| 1965 | The operator's own read of the field | `its stores now dominate the discount field` in the Twin Cities | the belief that the home metro was validated | any independent count of the field; the sentence opens `We believe` | `B1S01`, opening letter | Medium |
| 1966-10 | First stores outside the Upper Midwest open | 2 Denver stores | the format travelled outside the home market | that it travelled profitably in the year of opening | `B1S02` (`…the interim financing for two Target stores opened in Denver in October of 1966`), planned in `B1S01` | High (plan) / Medium (actual, UNVERIFIED TLS) |
| 1967 | In-year profitable openings after absorbing pre-opening expense | 2 stores (Fridley, West St. Paul) | new-unit economics at the smallest scale the company reported | chain-wide economics | `B1S03`, store narrative | Medium (UNVERIFIED TLS) |
| 1967 | Target-unit sales printed for the first and only time in the decade | `$86,901,007`, `an in-crease of 43 percent` | one hard unit revenue datum, one year deep | a series — the 1966 base is DERIVED at best (`U.021`) | `B1S03`, Financial Review | Medium (UNVERIFIED TLS) |
| FY1966 | Whole-estate area statement | `Total retail area of the seven Target stores now in operation is 889,000 square feet.` | an average of ~127,000 sq ft per store across seven units, at **total retail area** basis | selling area, cost, or the FY1974 roster basis, which does not foot to it (`U.012`) | `B1S02` | Medium (UNVERIFIED TLS) |
| 1972 `(PB)` | Sixteen openings in seven months | 46 stores in nine states at year end | the replicability of the format at speed | that the speed was economic — the same report prints group pretax falling to `$9,222,000` from `$13,749,000`, attributed in print to Target performance and start-up costs | `B1S08` | High |

### L.2 The knowability line for this section

`KNOWABLE` in-period, from held print: store count, locations, opening sequence, the parent's own
consolidated income and capital structure, one unit revenue year. `NOT KNOWABLE` in-period from any
document this corpus holds: unit-level margin, cost of a store, and whether the discount field outside
Minnesota was as empty as the company's expansion sentence assumes. `UNKNOWN` and closeable: the 1966
base of the 43% figure (`U.021`), the magnitude of the Target loss carry-forward (`U.016`), and the
survey document behind the 51% figure (`U.032`).

STATUS: WRITTEN 2026-09-25

## M

### M.1 Failures and negatives the company printed about itself

| Date | Signal / failure | Magnitude | What it demonstrated | What it did NOT demonstrate | Source | Confidence |
|---|---|---|---|---|---|---|
| 1964 (tax attribute) | Target Stores, Inc. carried a loss forward into the group's tax computation | `a substantial loss carry-forward available to Target Stores, Inc., in 1964`; amount UNKNOWN | the discount unit had not yet earned out its start-up losses by the middle of its third year | how large the losses were, which years produced them, or when they ended | `B1S01`, EARNINGS section | High |
| FY1965 | An earnings-quality caveat printed by the company | `A factor in the 1965 earnings figures was a reduction in repair and maintenance expenses of approximately $1,130,000 from the 1964 level.` | part of the reported "record year" was lower maintenance spend, not higher trading | that the maintenance cut caused the earnings gain — the company writes `A factor`, not `the factor`; the causal weight is **UNKNOWN** | `B1S01`, EARNINGS section | High (existence) / Low (weight) |
| 1965 | Maintenance and repairs line falls year on year | `$763,572` against prior-year `$1,894,037` (columns as printed on the deduction block) | the direction of the figure above, in the audited statement itself | that the two printed digits are correctly aligned — the drop is larger than the narrative's `$1,130,000` explains, and OCR may have lost a digit (`U.018`) | `B1S01`, Statement of Income, deduction block | Medium |
| after FY1967 | The subsidiary's printed merchandising officer disappears from the officer pages | `GEISSE` = 3 hits in the whole founding run (FY1965, FY1966, FY1967), **0 from FY1968 onward** | that the man company print shows running merchandise left the printed frame within the founding decade | why — departure, promotion out of the listing, or a change of page structure are all unheld; the mechanism is UNKNOWN and is not evidence of failure | `B1S01`, `B1S02`, `B1S03` subsidiary-officer pages (NULL `U.020`) | High (count) / UNKNOWN (mechanism) |
| 1971 `(PB)` | One Target unit counted in the year's print is not countable in the later roster | 30 as printed for year-end 1971 vs 29 enumerable from the FY1974 estate roster | that the estate was not purely additive — something closed, merged, or dropped out of the list | what it was: the roster lists only units still operating in 1974, and one row may be OCR loss | `B1S07` vs `B1S10` (`U.008`) | Medium |
| 1969→1973 `(PB)` | Group productivity and margin decline | sales per square foot `$97.70 → $84.54` (`−13.5%`, DERIVED within one row); pre-tax margin to sales `3.3% → 1.4%` | that the growth decade was economically worse per unit of space than the year it opened with | that Target alone caused it — the row is the **group**, which also carried hard-goods units (`U.010`) | `B1S09`, Five Year Comparisons | Medium (UNVERIFIED TLS, `U.028`) |
| 1972 `(PB)` | Rapid opening programme acknowledged as a cost | group pretax `$9,222,000` vs `$13,749,000`, attributed in print to `Target performance and start-up costs` | the company itself linked the fastest expansion year to an earnings decline | the size of the start-up drag, which is not printed | `B1S08` | High |

### M.2 What is missing from the failure record, and why that is a finding

The estate lists in this corpus enumerate **openings with a year and an area** and print no closure,
no write-off and no rejected site. That is an observation about the **document class**, not about the
operations: a stockholder report is written to display growth, and this one was the company's **first
ever public issue of its figures** (`B1S01`, opening letter; see `U.017`), which makes selection
pressure at its maximum. This pass did not search the eleven layers for closure or impairment
language, so "no failure printed" is recorded in §S as an **examination not performed** (`U.021`),
while the record-selection null (§2) is stated positively in §A of volume 1 and is restated here only
because it changes what M.1 can be used to prove: **the negatives above are all items the company
chose to print**, which makes them unusually reliable and simultaneously a biased sample of the
decade's actual failures.

STATUS: WRITTEN 2026-09-25

## N

### N.1 Decisions reconstructable from the held record

Every rationale in the `Rationale` cell is the company's own printed sentence or its close paraphrase;
where nothing was printed the cell says so, because the alternative — supplying a motive the record
does not contain — is the exact failure §2 forbids.

| Date | Decision | State before | Information available | Unknowns | Alternatives | Constraints | Rationale | Expected result | Actual result | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1962 | Enter discount merchandising under a named subsidiary | A privately-owned department-store company; no discount operation | The company's later account of the market logic; no internal record of the decision is held | Who decided (person) — `U.001`; the month — `U.002`; the capital committed — §K.1 | UNKNOWN — no rejected option is printed anywhere in the corpus | Ownership by a single parent; no external capital in the held record | `there also will be people who wish to take advantage of low margins and convenience shopping through the economies of mass merchandising` | a second merchandise offer the parent can run separately | four stores open in 1962 (RESTATED roster, `U.016`) | `B1S01` "Target Stores, Inc." essay; `B1S10` roster `(PB)` | Medium (that the decision was taken and its shape); UNKNOWN as to originator |
| 1965 | Organise the unit as a **separate subsidiary with its own buying office inside the parent** | One department-store buying function | the printed description of the arrangement | whether this was contested internally — not printed | UNKNOWN | `The five Target stores in Minnesota maintain a separate identity within The Dayton Company. Target has its own management staff, its own buying organization, and freely competes for customers and employees.` | a distinct offer and a distinct P&L identity | in 1965 the unit is listed with named principal officers as `Target Stores, Inc.` | `B1S01` essay + subsidiary-officer page; `B1S03` | High (structure); Low (motive) |
| 1965-1966 | Open outside the home metro at all, and choose Denver | five stores, all Minnesota | the printed belief about format transferability and the printed similarity criterion | whether other candidate cities were weighed — not printed | Duluth (already opened 1962) shows the in-state pattern; alternatives UNKNOWN | capital commitment printed as `approximately $3,750,000 for additional facilities`, consolidated | `We believe the success of Target in the … Minneapolis-St. Paul metropolitan area, where its stores now dominate the discount field, provides an operational format which can do as well in other areas of the country.` | two Denver units in Fall 1966 | both opened October 1966 (`B1S02`, `(PB)` for the FY1966 actual only in that it post-dates the FY1965 statement) | `B1S01` opening letter; `B1S02` | High (plan and actual); Medium (rationale weight) |
| February 1966 | Make the company's figures public | `a privately-owned operation` that had never published | the company's own stated reasons | whether a share issue was already planned — the offering came later (late 1967, printed by a different report) | staying private, which the sentence names as the prior state | none printed | `we feel disclosure will further growth possibilities, open expansion opportunities, and give our management the challenge of operating in an atmosphere of public scrutiny` | growth and expansion options; management under scrutiny | the first public annual report is the document this dataset is built on | `B1S01` opening letter | High |
| February 1966 (annual meeting) | Ten-for-one stock split, then a 100% stock dividend | existing share structure | printed mechanics | motive for the timing — not printed | UNKNOWN | covenants in the sinking fund note agreements relating to `sale of receivables, working capital, dividends and other restricted payments` | not printed | not printed | retroactively reflected; `Earnings per common share were $1.99 during fiscal 1965 … Restated on the same basis, 1964 earnings per share were $1.41` | `B1S01`, SUBSEQUENT EVENTS + LONG-TERM DEBT note + EARNINGS | High (acts); UNKNOWN (rationale) |
| 1966-01-15 | Commence a separate receivables company | service charges handled inside the retail accounts | the commencement date and a two-week deficit printed in the subsidiary statements | why a separate entity — the reason is NOT printed in the layer | UNKNOWN | the same covenant line restricting `sale of receivables` | **mechanism UNKNOWN** — an INFERENCE that covenants motivated the structure is plausible and unproven; it is recorded as an inference and not as a reason | not printed | `The Company (which commenced operations on January 15, 1966) …` | `B1S01`, NOTE A of the subsidiary statements | High (existence/date); Low (motive) |
| late 1967 | First public stock offering | 1966 disclosure, still a small store estate | the corporation-level counts printed with it | month UNKNOWN | UNKNOWN | not printed | not printed | `it had 23 stores in five states` | (PB) by 1970-12: `125 stores in 20 states, along with 58 franchised outlets` | `B1S06` | High (that it happened); UNKNOWN (month, terms) |

### N.2 The decision record's structural hole

For Amazon, Walmart and Apple the decision layer is thick because founders kept talking: interviews,
letters and reminiscences supply alternatives considered and rejected. For this company the decision
layer is **one voice, printed once a year, for shareholders**, and the entity was privately owned at
the moment of the founding act. `Information available` and `Alternatives` are therefore UNKNOWN more
often than not, and that is a property of the archive, not of the company's records-management. This
volume does not read the silence as indifference: see `U.004` (the FY1965-only provenance of the 1962
story) and `U.030`-`U.034` (the routes that could still produce an independent carrier).

STATUS: WRITTEN 2026-09-25

## O

STATUS: WRITTEN 2026-09-25

### O.1 Counterfactuals the held record can and cannot name

**Nameable, and each with its firewall.** (i) The unit was organised as a separate subsidiary that
`freely competes for customers and employees` with its own parent (`B1S01`), so the counterfactual the
company *did not* pursue — folding discounting into the Dayton's brand and buying operation — is
visible only as the shape of what it chose; class **INFERENCE**, confidence **Medium**, and it is an
inference about an organisational fact, not about a deliberation. (ii) Growth was **self-built**: every
Target unit in the FY1974 estate roster is described by an opening year and an area, and no purchase of
an existing discount chain is named in any founding-decade layer this pass read (`B1S10`, `(PB)`);
whether acquisition was considered and rejected is UNKNOWN, and this pass ran no search for
acquisition language (`U.021`). (iii) Geography was chosen city-by-city against a stated criterion —
`metropolitan areas which offer potential similar to that of the Twin Cities and Duluth` — but the
cities *not* chosen cannot be enumerated from this corpus at all.

**Not nameable, and why.** The rejected-option layer is empty for the same structural reason as §N.2:
no minutes, no internal memorandum, and no founder interview is held or has been reached in any of the
five families, and the company was private at the founding act. Under §2's record-selection null, the
absence is reported as **what a survivor's archive does not keep**, not as evidence that options were
not weighed.

**Contrast with the three exemplars.** For Amazon the counterfactual set is recovered from founder
retelling (why books first, why not a physical chain); for Walmart from Sam Walton's own published
account of Rogers versus Bentonville; for Apple from the garage-and-HP-career narrative. Here the
equivalent question — *why Roseville, and what else was looked at* — has **no carrier of any class**,
and the honest answer at Stage 1 is: not establishable in the Stage-1 record, and probably not
establishable from any public document of this type (see `U.002`, `U.030`, `U.033`).

## P

### P.1 Note on dates and IDs

Metric IDs **continue B1's Q-series** (Q1-Q20 live in `research/B1_dayton_print_records.md`); no ID is
reused. Because of `U.011`, every row below from a cover-labelled "1965" report carries the **fiscal
period end** in its `Date` cell (`1966-01-29`), and the prior-series row B1 emitted as
`parent_net_retail_sales 1965 = 186,166,671` must be **re-dated to the year ended 1966-01-29** at
merge, with its comparative `162,773,739` re-dated from B1's `1964` to the year ended **1965-01-30**;
that correction is registered as a row in the §P merge block, not as a deletion.

### P.2 Metrics established on this pass

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| Q21 | 1966-01-29 | Net retail sales incl. leased departments (whole company) | 186,166,671 | USD | `B1S01`, Statement of Income + SALES note | 1966 (cover 1965) | High |
| Q22 | 1965-01-30 | Net retail sales, prior column | 162,773,739 | USD | `B1S01`, same | 1966 (cover 1965) | High |
| Q23 | 1966-01-29 | Operating income | 14,233,981 | USD | `B1S01`, Statement of Income | 1966 | High |
| Q24 | 1966-01-29 | Net income (`31 percent` gain printed) | 7,128,981 | USD | `B1S01`, Statement of Income + EARNINGS | 1966 | High |
| Q25 | 1966-01-29 | Earnings per common share, post split/dividend | 1.99 | USD/share (prior year restated 1.41; `The increase was 41 percent`) | `B1S01`, EARNINGS | 1966 | High |
| Q26 | 1966-01-29 | Cost of sales, buying and occupancy (combined, inseparable) | 139,686,954 | USD | `B1S01`, notes | 1966 | High |
| Q27 | 1966-01-29 | Selling, general and administrative expenses | 31,256,511 | USD | `B1S01`, notes | 1966 | High |
| Q28 | 1966-01-29 | Rentals, income-statement deduction line | 2,088,720 | USD | `B1S01`, Statement of Income | 1966 | High |
| Q29 | 1966-01-29 | Long-term leases: aggregate minimum annual rentals | 1,564,220 | USD (of which 626,683 payable to unconsolidated subsidiaries) | `B1S01`, LEASES note | 1966 | High |
| Q30 | 1966-02+ | Commitments for additional facilities (subsequent events, consolidated) | ~3,750,000 | USD | `B1S01`, SUBSEQUENT EVENTS | 1966 | High |
| Q31 | 1966-01-29 | Sinking fund notes outstanding | 13,600,000 | USD, `5% %` as printed | `B1S01`, LONG-TERM DEBT (1) | 1966 | High |
| Q32 | 1966-01-29 | Mortgage notes outstanding | 2,124,960 | USD | `B1S01`, LONG-TERM DEBT (2) | 1966 | High |
| Q33 | 1966-03 | Retained-earnings transfer on the 100% stock dividend | 1,535,500 | USD | `B1S01`, SUBSEQUENT EVENTS | 1966 | High |
| Q34 | 1966-01-29 / 1965-01-30 | LIFO reserve (inventories stated below retail-method non-LIFO cost) | 664,219 / 431,573 | USD | `B1S01`, MERCHANDISE INVENTORIES note | 1966 | High |
| Q35 | FY1965 | Target-unit sales growth, printed rate only | 44 | percent over previous year | `B1S01`, opening letter | 1966 | Medium (base not printed) |
| Q36 | FY1965 | Target-unit pre-tax profit growth, printed rate only | 100 | percent over previous year | `B1S01`, opening letter | 1966 | Medium (base not printed; cf. `U.016`) |
| Q37 | 1966-01-29 | Target stores in operation per the FY1966 area statement's own count | 7 | stores; `889,000 square feet` total retail area → 127,000 sq ft/store DERIVED | `B1S02` | 1967 (cover 1966) | Medium (`U.028`) |
| Q38 | 1969-01/1973 | Low-margin GROUP total square feet (thousands), `(PB)` | 2,390 / 3,516 / 4,220 / 5,518 / 5,563 | 1969→1973 in column order | `B1S09`, Five Year Comparisons | 1973 | Medium (`U.028`) |
| Q39 | 1969→1973 `(PB)` | Low-margin GROUP sales per square foot | 97.70 → 82.18 → 81.94 → 79.81 → 84.54 | USD/sq ft, 1969→1973 | `B1S09`, same block | 1973 | Medium |
| Q40 | 1969→1973 `(PB)` | Low-margin GROUP earnings before income taxes, percent to sales | 3.3% → 3.0% → 4.0% → 2.1% → 1.4% | percent, 1969→1973 | `B1S09`, same block | 1973 | Medium |
| Q41 | 1969→1973 `(PB)` | Low-margin GROUP pre-tax margin, DERIVED change | `84.54 / 97.70 − 1 = −13.5%` sales per sq ft; `1.4% − 3.3% = −1.9 pp` pre-tax margin | percent / pp | `B1S09`, one row, same basis | 1973 | Low (DERIVED, `derived_arithmetic` recorded) |
| Q42 | 1962 | Store areas of the four 1962 units, `(000)` column as printed `(PB)` | Roseville 68; Crystal 96; Duluth 96; Knollwood St. Louis Park 106 | thousands of sq ft (basis label OCR-corrupt) | `B1S10`, LOW MARGIN STORES roster | 1974 | Medium (RESTATED roster; `U.012`) |
| Q43 | 1966-01-15 | Dayton Credit Company commenced operations | 1966-01-15 | date | `B1S01`, NOTE A subsidiary statements | 1966 | High |
| Q44 | 1962-1965 | Target stores at year end, 1963 and 1964 | UNKNOWN | stores — no held layer prints a 1963/1964 count or opening | — | — | UNKNOWN (`U.021`) |

### P.3 Table coda

Fourteen of the twenty-four rows above are **whole-company or group** measures carrying a Target
label nowhere near them, and the two growth-rate rows (Q35, Q36) are the only unit-level financial
statements the founding decade yields before 1967's single revenue print. A reader who joins Q35 to
Q21 will produce a fictional Target P&L; the rows are deliberately unjoinable, and §K.1 names the cell
that is missing.

STATUS: WRITTEN 2026-09-25

## Q

### Q.1 Micro-timeline, in the order the documents hold it

Place names are **as printed** in the layer, including `ST.LOUIS PARK` without a space and the
`(000) Opened` roster form. Every line carries class · confidence · source; `(PB)` marks material
after the 1969 Stage-1→Stage-2 hand-off.

| Date (as held) | Event | Class · Conf · Source |
|---|---|---|
| 1962 (month and day UNKNOWN) | `the first Target store was opened early in 1962 in Roseville, a suburb north of St. Paul` | FACT (year, place) · High · `B1S01`, "Target Stores, Inc." essay; day UNKNOWN `U.002` |
| 1962 | Four units carry opening year 1962 in the company's own chronology spread: `ROSEVILLE, MINNESOTA`, `CRYSTAL, MINNESOTA`, `DULUTH, MINNESOTA`, `KNOLLWOOD, ST.LOUIS PARK … MINNESOTA` | RETROSPECTIVE INTERPRETATION (printed 1965/66) · Medium · `B1S01`, store chronology spread; cross-checked against `B1S10` roster (`PB`) `U.015` |
| 1962 | `The Company entered the discount merchandising field in 1962 with Target Stores, Inc.` | FACT · High · `B1S01`, Financial Review |
| 1963, 1964 | No Target opening or year-end count is printed in any held layer | UNKNOWN · `U.021` · absence in a list, not a statement |
| during 1965 | Bloomington, `a southern suburb of Minneapolis`, opens — `This brought the total number of Target stores to five.` | FACT · High · `B1S01` |
| FY1965 (year ended 1966-01-29) | Parent prints subsidiary officers: `DOUGLAS J. DAYTON, President, Target Stores, Inc.`; `JOHN GEISSE, Vice President, Target Stores, Inc.`; `RICHARD KLEIN, Vice President and Controller and Assistant Secretary, Target Stores, Inc.` | FACT · High · `B1S01`, Principal Officers of Subsidiaries page |
| FY1965 | `a substantial loss carry-forward available to Target Stores, Inc., in 1964` printed as the reason after-tax growth trailed pre-tax | FACT · High · `B1S01`, EARNINGS; `U.016` |
| FY1965 | Parent prints `gains of 44 percent in sales and 100 percent in pre-tax profits in 1965` for Target, against its own `14 percent` sales gain and `31 percent` net-income gain | FACT · High that printed; Medium as economics · `B1S01`; `U.013` |
| 1966-01-15 | `The Company (which commenced operations on January 15, 1966)` — Dayton Credit leg opens | FACT · High · `B1S01`, NOTE A subsidiary statements |
| 1966-01-29 | Fiscal period end of the layer this dataset calls FY1965 | FACT · High · `B1S01`, Statement of Income header; `U.011` |
| 1966-02 | Annual meeting approves a ten-for-one split; a 100% stock dividend is declared the same month; `a transfer of $1,535,500 from retained earnings to Common Stock in March 1966` | FACT · High · `B1S01`, SUBSEQUENT EVENTS |
| 1966-02 | `we are issuing our first public Annual Report` — the disclosure decision, dated by the document that is itself that report | FACT · High · `B1S01`, opening letter; `U.017` |
| 1966 (planned) | `Two more Target units are scheduled to be opened in Denver, Colorado, in the Fall of 1966, marking our first venture outside the Upper Midwest` | FACT (plan) · High · `B1S01` |
| 1966-10 | Two Denver stores open — `the interim financing for two Target stores opened in Denver in October of 1966` | FACT (actual) · Medium (UNVERIFIED TLS) · `B1S02` |
| 1966-10 + | Seven units in operation: `Total retail area of the seven Target stores now in operation is 889,000 square feet.` | FACT · Medium · `B1S02`; basis question `U.012` |
| 1967 | `Target stores for the Twin Cities—numbers eight and nine scheduled to open Fall, 1967.` → Fridley and West St. Paul open in October, profitable in the year of opening after pre-opening expense | FACT · Medium · `B1S02`, `B1S03` |
| 1967 | `DOUGLAS J. DAYTON / President`, `JOHN F. GEISSE / Senior Vice President and General Merchandise Manager` — the last year the name appears | FACT · Medium · `B1S03`; disappearance `U.001`, `U.020` |
| 1967 | `Target's sales were $86,901,007, an in-crease of 43 percent.` — the only Target-unit revenue printed in FY1962-FY1968 | FACT · Medium · `B1S03`; `U.021` |
| 1967-late | First public stock offering: `it had 23 stores in five states` (corporation level, printed in the FY1970 report; month UNKNOWN) | FACT · High · `B1S06` |
| 1968 | Masthead is `Dayton Corporation`; two St. Louis stores open; Target year-end total of eleven rests on a 1973 recap | FACT (openings) · High; recap · Medium · `B1S04`, `B1S09` |
| 1969 → | `Dayton Hudson Corporation` masthead; the merger with The J. L. Hudson Company; 1969-07-15 first public debt offering `$25 million … priced to yield 7.80 percent`; 1969-09-08 NYSE listing with a new corporate symbol | `(PB)` FACT · High · `B1S05`, `B1S06` |
| 1970 `(PB)` | `at the close of 1970 … it had 125 stores in 20 states, along with 58 franchised outlets` | FACT, corporation level · High · `B1S06` |
| 1971 `(PB)` | `At year's end, Target had 30 stores in 11 markets.` vs 29 countable in the FY1974 roster | FACT vs RESTATED · Medium · `B1S07`, `B1S10`; `U.008` |
| 1972 `(PB)` | 16 openings in seven months; 46 stores in nine states; group pretax `$9,222,000` from `$13,749,000`, attributed to Target performance and start-up costs | FACT · High · `B1S08` |
| 1973 `(PB)` | The only intact five-year low-margin row in the run: revenue, stores, square feet and sales per square foot for 1969-1973 | FACT/RESTATED · Medium · `B1S09`; §K.3 |
| 1974 `(PB)` | Estate roster under `LOW MARGIN STORES`, `Target (1967)*`, `Stephen L. Pistner, President`, columns `(000) Opened` | RESTATED roster · Medium · `B1S10`; `U.009` |
| 1994-02-10 / 1994-04-21 `(PB)` | The registrant's own electronic record begins: earliest filing SC 13G, first 10-K for FY1993 | FACT · High · `P2S06` |
| 1999-04-12 `(PB)` | EDGAR `formerNames` ends `DAYTON HUDSON CORP`; the FY1999 report heads itself `We are Target Corporation.` | FACT · High · `P2S06`, `B1S14`; `U.007` |
| 2013-07-06 `(PB)` | A newspaper obitury headlines `Target Stores founder Douglas Dayton … dies` — **not held**, lead only | NOT HELD · Low · `B1S12`; `U.001`, `U.031` |

STATUS: WRITTEN 2026-09-25

## R

### R.1 Structured snapshot at the Stage-1 boundary

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Entity at the boundary | `The Dayton Company` (FY1965, FY1966 print) → `Dayton Corporation` (FY1967, FY1968) → `Dayton Hudson Corporation` (FY1969) | mastheads read inside the layers: `B1S01`, `B1S03`, `B1S05` | High |
| Registrant continuity to the modern filer | One EDGAR line only, CIK 27419, with **exactly one** former name (`DAYTON HUDSON CORP`, 1994-12-09→1999-04-12); no Dayton, Goodfellow or Dey Brothers name exists there, and EDGAR holds no paper-era filings at all | `P2S06`, `sources/_index/raw_submissions_CIK0000027419.json` | High that EDGAR says this; **UNANSWERED** whether a separate predecessor registrant exists (`U.025`) |
| Retail estate at the last in-span count | 9 Target stores (1967), all Minnesota and Denver; 11 per a 1973 recap for 1968 | `B1S03`; `B1S09` `(PB)` | Medium |
| Geography | Minnesota (Twin Cities, Duluth) + Denver, Colo. — outside the Upper Midwest from 1966-10 | `B1S01`, `B1S02` | High |
| Legal form of the venture | A named subsidiary, `Target Stores, Inc.`, with its own president, buying organisation and controller | `B1S01` essay + officer page | High |
| Parent financial state at the boundary | Net retail sales `186,166,671`; operating income `14,233,981`; net income `7,128,981`; long-term debt `13,600,000` sinking fund + `2,124,960` mortgage | `B1S01` | High |
| Public status | Privately owned through the FY1965 layer's own description; first public annual report issued; first public stock offering late 1967 | `B1S01`; `B1S06` | High |
| Unit economics known at the boundary | Store counts, locations, opening dates to the year, one square-footage total, one unit revenue year (1967), two printed growth rates | `B1S01`-`B1S03` | Medium |
| Unit economics NOT known at the boundary | Per-store cost, per-store rent, occupancy, payroll, Target inventory, Target margin, Target result for 1962-66 and 1968 | §K.5 | UNKNOWN — named gaps |
| Who decided | UNKNOWN as to any person; the printed actor is the company | `B1S01`; `U.001` | High that print is silent on agency |
| When the first store opened | 1962, Roseville, month and day UNKNOWN | `B1S01`; `U.002` | High (year/place) UNKNOWN (day) |

### R.2 Boundary defence, stated as a test not a claim

The boundary is where the **documents** change hands, not where the story does: FY1969 is the first
layer printed under the Dayton Hudson masthead, and FY1968 is still `Dayton Corporation` with one
`Dayton-Hudson` mention of the pending merger. Anti-hindsight test applied to §R: everything above
would read the same if the discount venture had been written off by 1975 — the group row's own
productivity decline (`U.013`, §K.3) is the kind of fact that a failure would leave behind too. What
would **not** survive the test is any sentence that treats the 1962 subsidiary as the future Target
Corporation; the lineage is asserted backwards from a 1999 self-account (`B1S14`, `(PB)`) and is
recorded in §U, not in §R.

STATUS: WRITTEN 2026-09-25

## S

### S.1 Documented nulls (searches that ran, on bytes this machine holds)

| NULL | What was searched | Result | Anchor |
|---|---|---|---|
| Month-name with 1962 | any month within 25 characters of `1962`, plus the `1962 + 1st/first` form, across the eleven founding-era layers (781,995 chars of OCR); `July` appears 10 times in the run and never with a 1962 Target opening | **0 hits** | `U.018` |
| Predecessor names in print | `Goodfellow` and `\bDey\b` across all eleven founding-era layers | **0 hits each**; the sole `Goodfellows` attestation is the FY1999 retrospective | `U.019` |
| Geisse presence | `GEISSE` across the run | 3 hits (FY1965, FY1966, FY1967), **0 from FY1968 on**; `DOUGLAS J. DAYTON` 18 hits | `U.020` |
| Target-unit dollars | unit (not group) revenue, all eleven layers | printed **only** for 1967 (`$86,901,007`); none for 1962-66, 1968, 1970-72 | `U.021` |
| Five-year comparison columns | FY1969, FY1970, FY1971 `Five Year Comparisons` blocks | row labels present, **numeric columns lost in OCR**; FY1973's row survived intact | `U.022` |
| Byte-count discrepancy | FY1970 layer size | on-disk and sidecar both **53,023 B**; the probe's table printed 52,736 B | `U.023` |
| Catalog floor | text-layer listing of IA item `01-target-archive` | **1965→2024**; nothing before FY1965 exists in the item — a proven floor | `U.024` |
| Payroll / wages / headcount terms | `payroll`, `wages`, `number of employees` across the founding-decade layers, this pass | **no hits in FY1965-FY1972**; first appear FY1974 (`payroll dollars`) and FY1975 (`occupancy expense, payroll, advertising and other expenses`) `(PB)` | `U.028` |

### S.2 High-importance gaps, each with its follow-up route (no gap is left without one)

| Gap | Why missing | Importance | Follow-up |
|---|---|---|---|
| Who originated the 1962 decision | both independent carriers are web leads, not bytes | High | `U.031` |
| Month/day of the first opening | company text says `early in 1962` | High | `U.033` |
| Target-unit revenue and margin, 1962-1972 | the entity reported at group and company scope | High | `U.032`, `U.034` |
| Cost of a 1962-66 store | never printed; the nearest figure is a consolidated commitment | High | `U.030`, `U.032` |
| Any document before FY1965 | the item's OCR run starts at FY1965 (`U.024`) | High | `U.032` |
| Whether a predecessor registrant filed | EDGAR name search returned 503 | High | `U.036` |
| Verified provenance of five layers | local CA store expired; `--insecure` used | Medium | `U.037` |
| The missing 1971 unit (30 vs 29) | roster lists only units still open in 1974 | Medium | `U.030` |

### S.3 The record-selection null (§2)

What is unrecoverable **because the winners' archive is the one that was kept**: the internal
deliberation that created Target Stores, Inc. (no minutes, no memorandum, no founder interview is
held, and the company was private at the moment of the act); the rejected site and city candidates
behind Denver; the rejected merchandise and pricing options; any independent count of the 1962-65
discount field; and any third-party number behind every company-reported figure in §P — the 51%
survey is the only candidate and it survives only as a company's quotation of it. A Stage-1
reconstruction of this company therefore rests on **one voice describing its own youth to its own
shareholders, three years after the fact**, which is a Tier-1 document class and simultaneously the
weakest possible independence position (`U.004`).

### S.4 Examinations this pass did not perform (not nulls, not gaps in the record)

No search was run for: closure/impairment language in the founding layers; acquisition language;
rival-name mentions (Fedmark, Seiberling's, Martlin's, Two Guys, Topps, W. T. Grant, F. W. Woolworth);
employee-headcount tables; `Target` mentions in any periodical other than the one held leg; the item's
17 PDF image legs; HathiTrust, Google Books, auction or museum collections; local newspaper
back-files. Each is an **untried route** (`U.030`-`U.037`) or a §I/§J note, and none may be read as a
statement that the thing searched for does not exist.

STATUS: WRITTEN 2026-09-25

## T

### T.1 Provenance of every source this volume relies on

| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| `B1S01` The Dayton Company annual report, cover-year 1965, fiscal year ended 1966-01-29 | corporate stockholder report (OCR text layer) | primary | 1962; 1965; 1966 | 1966 (cover 1965) | local: `sources/corporate_print/1965_dayton_hudson_djvu.txt`; IA item `01-target-archive` | 1 | High (verified TLS) |
| `B1S02` the same line, cover-year 1966 (FY ended 1967-01-28) | corporate stockholder report | primary | 1966; 1967 | 1967 (cover 1966) | local: `sources/corporate_print/1966_dayton_hudson_djvu.txt` | 1 | Medium (**UNVERIFIED TLS**, `U.028`) |
| `B1S03` Dayton Corporation, cover-year 1967 | corporate stockholder report | primary | 1967 | 1968 (cover 1967) | local: `sources/corporate_print/1967_dayton_hudson_djvu.txt` | 1 | Medium (UNVERIFIED TLS) |
| `B1S04` Dayton Corporation, cover-year 1968 | corporate stockholder report | primary | 1968 | 1969 (cover 1968) | local: `sources/corporate_print/1968_dayton_hudson_djvu.txt` | 1 | High (verified TLS) |
| `B1S05` Dayton Hudson Corporation, cover-year 1969 `(PB)` | corporate stockholder report | primary; its 1968 column is RESTATED | 1969 | 1970 (cover 1969) | local: `sources/corporate_print/1969_dayton_hudson_djvu.txt` | 1 | High |
| `B1S06`-`B1S09` cover-years 1970-1973 `(PB)` | corporate stockholder reports | primary for their own year; `B1S09` also RESTATES 1969-1972 | 1970-1973 | 1971-1974 | local: `sources/corporate_print/197[0-3]_dayton_hudson_djvu.txt` | 1 | High (1970, 1972) / Medium (1971, 1973: UNVERIFIED TLS) |
| `B1S10` cover-year 1974 estate roster `(PB)` | corporate stockholder report | RESTATED retrospective roster | 1962-1973 | 1975 (cover 1974) | local: `sources/corporate_print/1974_dayton_hudson_djvu.txt` | 1 | Medium (UNVERIFIED TLS) |
| `B1S11` cover-year 1975 `(PB)` | corporate stockholder report, digitised through a licensed backfile | primary; names `ProQuest Historical Annual Reports` in the layer | 1975 | 1976 (cover 1975) | local: `sources/corporate_print/1975_dayton_hudson_djvu.txt` | 1 | Medium (cite the layer, not the company, as the scanner) |
| `P2S01` *Chain Store Age*, April 1963 "Steel for Stores" gather | trade periodical (OCR text layer, 170,260 B) | primary for the period; says nothing about the company | 1963 | 1963-04 | local: `sources/periodicals_csa_1963/Chain_store_age_Steel_for_Stores_djvu.txt` | 3 | High as to contents; **NULL** as to Target (`U.019` route) — one running foot prints `APRIL 1962` (`U.014`) |
| `P2S06` EDGAR submissions index for CIK 27419, including `formerNames` and the slice list | regulatory index JSON/CSV | primary record of the registrant line, silent before 1994-02-10 | 1994-02-10→ | retrieved 2026-09-25 | local: `sources/_index/raw_submissions_CIK0000027419.json`, `sources/_index/_INDEX.md`, `sources/_index/submissions.csv` (2,628 rows) | 1 | High |
| `P2S07` `sources/sec/_MANIFEST.csv` — header row only | intake manifest | negative artifact proving 0 documents stored for 1960-01-01→1985-12-31 | — | 2026-09-25 | local: `sources/sec/_MANIFEST.csv` | 1 | High (as a manifest, not as an absence) |
| `P2S02` EDGAR name→CIK browse responses, four terms | HTTP error bodies (7,747 B each) | **negative artifacts of a dead route** | — | retrieved 2026-09-25 | local: `sources/name_search/{dayton+hudson,dey+brothers,goodfellow,target+corporation}.atom` | 1 | UNANSWERED, not null (`U.025`) |
| `P2S03` EDGAR full-text search responses, four terms, 1940-1995 | API JSON, zero-hit | index-floor artifact: the corpus begins 2001 | — | retrieved 2026-09-25 | local: `sources/name_search/fts_*.json` | 1 | floor artifact, **never** an absence (`U.027`) |
| `P2S04` Wayback CDX responses for `target.com*`, `dhc.com*` | HTTP 503 bodies (11,832 B each) | negative artifacts | — | retrieved 2026-09-25 | local: `sources/web_archive/cdx_targetcom.txt`, `cdx_dhc.txt` | — | UNANSWERED (`U.026`) |
| `P2S05` IA item metadata listing for `01-target-archive` (259,567 B) | catalogue metadata | establishes the 1965→2024 layer run and the uploader's file labels | — | retrieved 2026-09-25 | local: `sources/ia_search/meta_01-target-archive.json` | 1 | High for the run; the per-year labels are **not** evidence (`U.006`) |
| `B1S12`, `B1S13` the two founder-credit carriers | newspaper obituary / biography pages | **NOT HELD** — lead only | 2013; 1992 | 2013-07-06; UNKNOWN | none; no bytes on this machine | 2 / 4 | Low; unusable as evidence (`U.001`, `U.031`) |
| `B1S14` FY1999 report genealogy spread `(PB)` | corporate stockholder report | self-account for 1902-1962 | 1902-1999 | 1999 | local: `sources/corporate_print/1999_annual_report_djvu.txt` | 1 | Low for the genealogy; tick↔blurb pairing unresolved |

### T.2 Independence ledger for this volume

`B1S01`-`B1S11` and `B1S14` are **one lineage** — the same company's reporting series, one uploader's
item — so no pair of them corroborates anything (§3 filing-lineage rule). `P2S01` is the only held
document of independent origin that touches the period, and its independent content about this company
is empty (`U.019`). `P2S02`-`P2S07` are regulatory/catalogue records of the registrant line, not of
1962. Consequence, stated plainly: **every load-bearing Stage-1 claim in this volume is
single-sourced**, and the confidence grades above are capped accordingly rather than by any doubt
about the digits.

STATUS: WRITTEN 2026-09-25

## U

### U.0 How to read this section

Conflicts are written in the §7 seven-field form (`CLAIM A / CLAIM B / WHY THEY DIFFER / EVIDENCE
WEIGHT / BEST-SUPPORTED INTERPRETATION / RESIDUAL UNCERTAINTY / CONFIDENCE`). The three other
categories the method requires §U to carry — documented **nulls**, **UNANSWERED** routes, and
**UNTRIED** routes — do not fit that form and are adapted to it under §7's "adapt, never delete"
rule, using `WHAT THE RECORD ASSERTS / WHAT WAS SEARCHED OR NOT / EVIDENCE WEIGHT / WHAT MAY AND MAY
NOT BE CONCLUDED / RESIDUAL UNCERTAINTY / CONFIDENCE / ROUTE`. **A null is a search that ran; an
UNANSWERED item is a route that failed; an UNTRIED route is work not done. None of the three is a
statement about the past, and nothing in this section says a company event "never happened" — the
formula used throughout is "not establishable in the Stage-1 record".**

Anchors are `U.001`-`U.037`, zero-padded three digits, minted continuously by this volume (see the
padding note in the assembly block). Conflicts U.001-U.017, documented nulls U.018-U.024, UNANSWERED
U.025-U.029, UNTRIED U.030-U.037.

**Conflicts considered and deliberately NOT minted** (recorded so a later pass does not re-open them
as fresh findings): the depreciation-method change amounts printed in `B1S01` and `B1S02` (different
effective dates, not a contradiction — §J.1c); the `$2,088,720` rentals line against the `$1,564,220`
lease-note minimum (expense for a period against contractual minimums at a date — §K.2); the parent's
`31 percent` net-income gain against Target's `100 percent` pre-tax gain (different entities —
`U.013` closes it as a labelling hazard, not as a conflict).

### U.1 Live conflicts

**U.001 — Who founded Target: Douglas Dayton, John F. Geisse, or the company (the probe's designated provenance conflict; live and unresolved).**
CLAIM A: `Target Stores founder Douglas Dayton, governor's uncle … dies` — *Twin Cities*/Pioneer Press
obituary, 2013-07-06 (`B1S12`, **not held**, lead only) `(PB)`. CLAIM B: John Francis Geisse
(1920-09-01→1992-02-21) is presented as the Target concept's originator and its first head, hired from
outside the Dayton chain (`B1S13`, **not held**, Tier-4 lead) `(PB)`. **Why they differ:** both are
retrospective obituary-genre assertions made decades later by different carriers, resting on different
institutional memories. **Evidence weight:** the held bytes settle **roles, not origination** — FY1965
prints `DOUGLAS J. DAYTON, President, Target Stores, Inc.` and `JOHN GEISSE, Vice President, Target
Stores, Inc.`; FY1966 prints Geisse as `Vice President and General Merchandise Manager`; FY1967 prints
`JOHN F. GEISSE / Senior Vice President and General Merchandise Manager` (`B1S01`, `B1S02`, `B1S03`,
officer pages). The 1962 act is narrated by the institution (`The Company entered the discount
merchandising field in 1962 with Target Stores, Inc.`) and the concept impersonally (`Target Stores,
Inc., was conceived with the knowledge that…`), and the FY1999 spread is likewise institutional
`(PB)`. The company **never credits any person** with the decision in any held layer. **Post-FY1967
Geisse leg:** `GEISSE` = 3 hits in the whole founding run and **0 from FY1968 onward** (`U.020`); the
departure is printed only as an absence from an officer page, with no reason, no date and no successor
named in the founding layers — `Stephen L. Pistner, President` appears only in the FY1974 roster
`(PB)` (`B1S10`). **Best-supported interpretation:** the venture was launched in 1962 by **The Dayton
Company** as **Target Stores, Inc.**, with Dayton printed as its President and Geisse as its
merchandising officer from the first year the company lists either; **no founder is settled**, and no
averaging or tie-break is applied here. **Residual uncertainty:** neither independent carrier exists as
bytes, so the conflict cannot be adjudicated at Tier 2 from this corpus either; and "founder" is not a
category these documents record. **Confidence:** that the conflict is unresolved — **High**; in either
founder attribution — **Low / UNKNOWN**.

**U.002 — The opening month and day of the first Target store.**
CLAIM A: `the first Target store was opened early in 1962 in Roseville, a suburb north of St. Paul`
(`B1S01`). CLAIM B: `1962-07-01`, in commonly repeated secondary accounts — **no carrier held anywhere
in this corpus**. **Why they differ:** side A is a held primary that states a year and a place and
refuses a month; side B is a precision the held record never produces. **Evidence weight:** a
month-name-with-1962 pattern search over 781,995 chars of OCR in eleven layers returned **0 hits**, and
`July` occurs ten times in the run and never with a 1962 Target opening (`U.018`). **Best-supported
interpretation:** 1962, Roseville, month UNKNOWN, day UNKNOWN — recorded as a partial date, not
promoted to a July date and not deleted. **Residual uncertainty:** whether any 07-01 carrier was ever
printed is itself UNKNOWN; only a newspaper or a lease/permit document can settle it.
**Confidence:** **High** that it is unresolved; **High** (year/place), **UNKNOWN** (day).

**U.003 — Which entity is the Stage-1 subject, and what its genealogy is.**
CLAIM A: the dispatch premise — a Target corporation founded 1962, with `Dey Brothers`, `Goodfellow`
and `Dayton-Hudson` as ancestors. CLAIM B: the held documents — `The Dayton Company` (FY1965, FY1966
text) → `Dayton Corporation` (FY1967, FY1968 mastheads) → `Dayton Hudson Corporation` (FY1969 onward) →
`Target Corporation` (FY1999), with **one** EDGAR name history: `DAYTON HUDSON CORP` 1994-12-09 →
1999-04-12 (`P2S06`). **Why they differ:** the premise is built from modern brand lineage and from
names EDGAR was searched with; the documents are what the entity printed each year. **Evidence weight:**
masthead evidence is documentary and outranks narrative; the EDGAR record is authoritative only for the
registrant line **from 1994-02-10**, and carries no paper-era filings at all (`U.027`). **Best-supported
interpretation:** Stage 1 is argued **for The Dayton Company at FY1965 narrating 1962**; the 1902-1961
leg is company self-account at UNKNOWN (`B1S14` `(PB)`), and no held document makes Dey Brothers or
Goodfellow an ancestor (`U.005`). **Residual uncertainty:** whether a separate predecessor registrant
ever filed is **UNANSWERED**, not settled (`U.025`, `U.036`). **Confidence:** **High** in the print
lineage; **Medium** that the lineage is the right Stage-1 frame.

**U.004 — The FY1965-only provenance of the 1962 story.**
CLAIM A: the 1962 launch is a documented fact. CLAIM B: the 1962 launch is documented **by one
document, three years after the fact, written by the actor for its own shareholders**, and every later
retelling in this corpus (`B1S09` `(PB)`, `B1S14` `(PB)`) is that same lineage repeating itself.
**Why they differ:** a fact and a single-source fact look identical in a corpus with one carrier.
**Evidence weight:** the item's own text-layer run begins at FY1965 — nothing before it exists in the
archive this machine holds (`U.024`), and the periodical leg is silent on the company (`U.019`).
**Best-supported interpretation:** keep the 1962 narrative at **FACT (single lineage)** for the act and
**Medium** for anything inside it that the report does not itself date, and keep founder pre-history at
UNKNOWN rather than deleting it. **Residual uncertainty:** whether any 1962-1964 document survives
anywhere is untested (`U.032`, `U.033`, `U.034`). **Confidence:** **High** in the provenance statement;
**Medium** in the events it carries.

**U.005 — The `Dey Brothers` premise.**
CLAIM A: Dey Brothers is a predecessor name (dispatch premise, and a name EDGAR was searched for).
CLAIM B: `\bDey\b` returns **0 hits** across all eleven founding-era layers, and the EDGAR full-text
zeros for `"Dey Brothers"`, `"Goodfellow"`, `"Dayton Hudson"`, `"Dayton Company"` over 1940-1995 come
from an index that begins in **2001** (`P2S03`). **Why they differ:** one side is a name circulating in
company histories; the other side is a search that **cannot answer** for the period. **Evidence
weight:** the null on held print is real (`U.019`); the EDGAR zero is an index-floor artifact and is
never cited as absence. **Best-supported interpretation:** the premise is **unestablished**, not
disproved; any later stage inheriting "Dey Brothers" as a fact must retraction-test it under §14 rule 8
before writing it. **Residual uncertainty:** a control full-text query with no date restriction was
never run (`U.027`). **Confidence:** **High** that it is unestablished.

**U.006 — Uploader label vs document text (which entity issued which number).**
CLAIM A: the IA item names every per-year file `Dayton Hudson Corp (DH)` from 1965 through 1998.
CLAIM B: the FY1965 masthead in bytes reads `THE DAYTON COMPANY @ ANNUAL REPORT 1965`, FY1967 reads
`Dayton Corporation`, and `Dayton Hudson` appears 0 times in FY1965. **Why they differ:** a single
uploader's folder convention applied backwards across 34 reporting years. **Evidence weight:** text
outranks filename; a register built on the file names would **misdate the 1969 merger by four years**
and would attribute Dayton Company numbers to a corporation that did not yet exist. **Best-supported
interpretation:** attribute every figure to the masthead that printed it, in every register row, as
done in §T and §P. **Residual uncertainty:** none material — the correction is procedural and is
applied throughout. **Confidence:** **High**.

**U.007 — When the parent became Target `(PB)`.**
CLAIM A: EDGAR `formerNames` ends `DAYTON HUDSON CORP` on **1999-04-12** (`P2S06`). CLAIM B: the FY1999
report heads itself `We are Target Corporation.` and states the name change; the dispatch premise says
**2000**. **Why they differ:** a filing-event date, a report-year label, and a division-level
readoption date. **Evidence weight:** EDGAR for the parent-level act; the held FY1999 print for the
marketing-level act; **no held document states the 2000 leg**. **Best-supported interpretation:** a
1999 parent-level change is documented; a 2000 division-level readoption is **unestablished in this
corpus** and is recorded as a conflict rather than resolved into a both-stages claim. **Residual
uncertainty:** which calendar act each source is dating. **Confidence:** **High** (1999), **Low** (2000).

**U.008 — Target store count at year-end 1971: 30 or 29 `(PB)`.**
CLAIM A: `At year's end, Target had 30 stores in 11 markets.` (`B1S07`, FY1971). CLAIM B: the FY1974
estate roster enumerates **five** units with opening year 1971, i.e. **29** cumulative (`B1S10`).
**Why they differ:** the roster lists only units still operating in 1974, so a closed, sold or renamed
unit disappears from it; one row may also be OCR loss. **Evidence weight:** both are company print of
one lineage, so neither corroborates the other; CONTEMPORANEOUS outranks RESTATED as a matter of
priority, not of arithmetic. **Best-supported interpretation:** report both — 30 as printed for 1971,
29 as roster-countable — with a one-unit difference whose mechanism is UNKNOWN. **Residual
uncertainty:** which store, and which document is at fault; only the PDF image leg can say (`U.030`).
**Confidence:** **Medium**.

**U.009 — The roster parenthetical for the Target unit: 1961 or 1967 `(PB)`.**
CLAIM A: `Target (1961)*` (`B1S09`, FY1973 subsidiary list). CLAIM B: `Target (1967)*` (`B1S10`, FY1974
roster, under the printed heading `LOW MARGIN STORES`). **Why they differ:** OCR corruption of a small
parenthetical inside a dense two-column list; both are far from the 1962 they might be read to
contradict. **Evidence weight:** neither is legible enough to carry a date claim. **Best-supported
interpretation:** **UNKNOWN (OCR-corrupt)**, and explicitly **not** used to move the 1962 opening in
either direction. **Residual uncertainty:** the original page (`U.030`). **Confidence:** **Low** in
both readings, which is the finding.

**U.010 — The 1968 department-store revenue: 223,276,791 or 582,923 `(PB)`.**
CLAIM A: `223,276,791` USD printed by **Dayton Corporation** for 1968 (`B1S04`). CLAIM B: `582,923`
USD thousands printed for 1968 inside the **Dayton Hudson** 1969 report (`B1S05`). **Why they differ:**
the 1969 column is the merged scope including The J. L. Hudson Company of Detroit; the figures are not
inconsistent, they are **different entities' 1968**. **Evidence weight:** each set foots to its own
scope; RESTATED is never corroboration of CONTEMPORANEOUS. **Best-supported interpretation:** print both,
each labelled with the filer whose report printed it; no merge of the two series. **Residual
uncertainty:** which consolidation date inside 1969 produced the wider column is not established by
these layers. **Confidence:** **High**.

**U.011 — Which year a "1965" report reports: the cover-year / fiscal-year divergence (new this pass; re-bases the inherited series).**
CLAIM A: the cover and the narrative use **1965** (`ANNUAL REPORT 1965`; `gains of 44 percent in sales
and 100 percent in pre-tax profits in 1965`; `Earnings per common share were $1.99 during fiscal 1965`).
CLAIM B: the statements inside the same document are headed `Fiscal Year Ended / January 29, January
30, / 1966 1965` and their notes label the current column **1966** (`Cost of sales, buying and
occupancy expenses were $139,686,954— 1966 and $123,584,592— 1965`). **Why they differ:** the entity
names a fiscal year by its starting calendar year in prose and by its ending year in the notes; the
period is the twelve months ended **1966-01-29**. The FY1966 layer proves the pattern is systematic, not
an OCR slip: it prints `during the fiscal year ended January 28, 1967 … $223,210,637` under a 1966
cover. **Evidence weight:** documentary — both labels are inside audited statements. **Best-supported
interpretation:** every row drawn from a cover-labelled layer carries the **fiscal period end** as its
date (done in §P), and the inherited series is corrected at merge: `186,166,671` belongs to the year
ended 1966-01-29 and `162,773,739` to the year ended 1965-01-30, **not** to "1965" and "1964". This
refutes the working premise carried in `research/B1_dayton_print_records.md` that "fiscal year =
calendar year in these reports". **Residual uncertainty:** the company's own convention for labelling
the next year's report is inferred from two layers; FY1968 onward was not tested for the same pattern
by this pass. **Confidence:** **High** (the divergence), **Medium** (its generalisability).

**U.012 — Two incompatible area bases for the same seven stores (new this pass).**
CLAIM A: `Total retail area of the seven Target stores now in operation is 889,000 square feet.`
(`B1S02`, cover-year 1966). CLAIM B: the FY1974 roster's per-store `(000)` column prints, for the same
seven units, `68 + 96 + 96 + 106 + 118 + 119 + 119 = 722` thousand (`B1S10`, `(PB)`). **Why they
differ:** most likely one is total retail area and the other selling area, but the roster's column label
is OCR-corrupt, so the difference in definition is **assumed to exist and cannot be named**. **Evidence
weight:** each is internally consistent within its own table; neither is arithmetic on the other.
**Best-supported interpretation:** report both, with the average (889,000 ÷ 7 ≈ 127,000 sq ft, DERIVED
from one sentence) and the roster's per-store figures **never mixed in one ratio or one series**.
**Residual uncertainty:** the roster column's basis; only the PDF page settles it (`U.030`).
**Confidence:** **Medium** that these are two bases; **High** that no single store-area figure is
establishable right now.

**U.013 — Which growth rate belongs to which entity (new this pass).**
CLAIM A: `gains of 44 percent in sales and 100 percent in pre-tax profits in 1965 over the previous
year`, printed as Target's (`B1S01`, opening letter). CLAIM B: the same document prints the company's own
consolidated gains as `14 percent` on sales and `a 31 percent gain` on net income, with pre-tax
`increased by 48 percent from 1964` (`B1S01`, SALES/EARNINGS). **Why they differ:** different reporting
objects in adjacent paragraphs of one document, and the probe's family-d table compressed both into a
single `44% sales / 100% pre-tax profit gains 1965 over 1964` row without saying which unit moved.
**Evidence weight:** both are company print; the Target pair is a **rate with no printed base**, so it
cannot be converted to dollars. **Best-supported interpretation:** keep the 44/100 pair labelled
**Target-unit, rate only, base UNKNOWN**, and the 14/31/48 set labelled **consolidated**; §P does this
(Q21-Q25 against Q35-Q36). **Residual uncertainty:** the Target dollar base for FY1964
(`U.021`). **Confidence:** **High**.

**U.014 — The date of the one held periodical leg (new this pass).**
CLAIM A: the layer is *Chain Store Age*, **April 1963**, as the probe dated it and as nearly every
running foot reads. CLAIM B: one foot in the same layer reads `CHAIN STORE AGE, APRIL 1962`.
**Why they differ:** OCR corruption, a bound-in gathering page, or a mixed scan — not distinguishable
from text alone. **Evidence weight:** the majority of feet, the side numbering (`E2`, `E8`, `E18`) and
the metadata all point to 1963-04. **Best-supported interpretation:** cite the leg as **April 1963**
and record the anomaly, because a 1962 date on this document would be the corpus's only contemporaneous
year-of-launch periodical and must not be silently created by a transcriber. **Residual uncertainty:**
the physical page. **Confidence:** **Medium**.

**U.015 — The fourth 1962 store's place name, as printed.**
CLAIM A: `KNOLLWOOD, ST.LOUIS PARK` / `MINNESOTA 1962` — the FY1965 chronology spread's own lineation,
with no space inside the abbreviation (`B1S01`). CLAIM B: `Knollwood,` / `St. Louis Park, Minn. 106
1962` — the FY1974 roster's normalised two-line form (`B1S10`, `(PB)`). **Why they differ:** typesetting
and OCR, not geography. **Evidence weight:** both name the same unit; the roster adds an area digit.
**Best-supported interpretation:** transcribe **as printed** in every quotation and register row
(`KNOLLWOOD, ST.LOUIS PARK`), never silently correct to "Knollwood, St. Louis Park", and record that
the unit is a shopping-centre site in St. Louis Park, Minnesota, i.e. the fourth of the four 1962
openings. **Residual uncertainty:** whether the opening preceded or followed the three named in the
essay's `Roseville … first` sentence — the chronology gives a year only. **Confidence:** **High** that
the print says this.

**U.016 — The 1969 and 1970 Target year-end counts are DERIVED, never printed; and the unit's earliest profit statement is a loss.**
CLAIM A: the register carries 1969 = 17 and 1970 = 24 Target stores. CLAIM B: no held layer prints a
Target year-end count for either year; 17 and 24 come from a **1973 recap base plus printed opening
lists** (`B1S09`, `B1S05`, `B1S07`), and the FY1974 roster independently enumerates 6 openings in 1969
and 7 in 1970, which is the same arithmetic performed on a different list. **Why they differ:** one side
is a derived count presented in a table of metrics, the other is the document class — the company
printed openings and a five-year recap, not a year-end unit census. **Evidence weight:** the derivation
is transparent and reproducible, and the group row's own store counts (19 in 1969, 27 in 1970, group
scope) are consistent with it; consistency is not printing. **Best-supported interpretation:** keep both
rows classed **DERIVED** with `derived_arithmetic` filled, never as observations; and record the unit's
own earliest financial sentence as `a substantial loss carry-forward available to Target Stores, Inc.,
in 1964` with **magnitude UNKNOWN** — the discount unit was still tax-shielded by losses at the
midpoint of its founding decade (`B1S01`). **Residual uncertainty:** any store that opened and closed
inside a single year would be invisible to both methods. **Confidence:** **Low** in the counts as
observations, **High** in the derivation as arithmetic.

**U.017 — "Privately-owned" in the same document that reports a public annual report, four years before an initial public offering.**
CLAIM A: `The projected growth of The Dayton Company requires that it expand beyond the concept of a
privately-owned operation. To this end, we are issuing our first public Annual Report.` (`B1S01`).
CLAIM B: the FY1970 report prints `When the Corporation made its first public stock offering in late
1967, it had 23 stores in five states` (`B1S06`, `(PB)` for the offering year). **Why they differ:** they
are **different acts by different bodies** — a disclosure decision taken while the company was
privately held, and a securities offering two years later — and the risk is a reader collapsing them
into one "went public in 1965" claim. **Evidence weight:** two documents of one lineage, each explicit.
**Best-supported interpretation:** the founding-decade sequence is **private company → first public
annual report (this layer) → first public stock offering (late 1967) → NYSE listing (1969-09-08,
`(PB)`)**; the exact status of the shareholding before late 1967 (closely held, preferred holders,
public quotes without an offering) is **not printed** and stays UNKNOWN. **Residual uncertainty:** what
"public" meant in the 1966 sentence, since the report was printed and distributed rather than filed.

### U.2 Documented nulls — searches that ran, on bytes held on this machine

**U.018 — No month of 1962 anywhere in the founding run.** WHAT THE RECORD ASSERTS: `early in 1962` is
the finest date the company ever printed for the first opening. WHAT WAS SEARCHED: a
month-name-within-25-characters-of-`1962` pattern plus the `1962 + 1st/first` form across the eleven
founding-era layers (781,995 chars). EVIDENCE WEIGHT: **0 hits**; `July` occurs 10 times in the run
(FY1965 lease notes, FY1968 Hudson's Oakland Mall, FY1969 debt, FY1971 Toledo, FY1975) and never with a
1962 Target opening. WHAT MAY BE CONCLUDED: the held company record does not date the day. WHAT MAY
NOT: that no newspaper dated it. RESIDUAL UNCERTAINTY: the layers are one company's print; §S.4 lists
the unsearched carriers. CONFIDENCE: **High** (the null). ROUTE: `U.033`.

**U.019 — Predecessor and founder names are absent from the founding-decade print.** WHAT THE RECORD
ASSERTS: a Dayton-line company describing itself. WHAT WAS SEARCHED: `Goodfellow` and `\bDey\b` across
all eleven layers (the probe tested six; this run covers eleven), plus the *Chain Store Age* April 1963
layer for `Target`, `Goodfellow`, `Minnesota`, `Dayton`, `Hudson`, `discount`. EVIDENCE WEIGHT:
**0/0** in the eleven; in the periodical `Target` **0**, `Goodfellow` **0**, `Minnesota` **0** against
`Hudson` **3** and `Dayton` **2** (both non-company), on a 168,433-char layer far above the 400-byte
threshold, so zero means zero. WHAT MAY BE CONCLUDED: the Goodfellow/Dey genealogy is not in the
founding print (`U.005`), and no contemporaneous trade text in this corpus mentions Target. RESIDUAL
UNCERTAINTY: other periodicals were never searched (`U.032`, `U.034`). CONFIDENCE: **High**. ROUTE:
`U.032`.

**U.020 — `GEISSE` is a three-year presence and then is gone.** WHAT THE RECORD ASSERTS: officer pages.
WHAT WAS SEARCHED: the string across the eleven founding-era layers. EVIDENCE WEIGHT: 3 hits (FY1965,
FY1966, FY1967), **0 from FY1968 onward**; `DOUGLAS J. DAYTON` 18 hits across the same run. WHAT MAY BE
CONCLUDED: a printed role appearing and a printed role disappearing, which is `U.001`'s strongest held
fact. WHAT MAY NOT: that the disappearance is a departure, a dismissal, a promotion out of the listing,
or an OCR omission — none is printed. RESIDUAL UNCERTAINTY: the FY1968 officer page's structure was not
compared line-for-line with FY1967's. CONFIDENCE: **High** (count) / **UNKNOWN** (meaning). ROUTE:
`U.030`.

**U.021 — The unit-level dollar hole.** WHAT THE RECORD ASSERTS: store counts and one revenue year.
WHAT WAS SEARCHED: every founding-era layer for Target-unit sales. EVIDENCE WEIGHT: the only unit
figure in FY1962-FY1968 is 1967's `$86,901,007`; nothing is printed for 1962-66, 1968 or 1970-72, and
the FY1965 tax note's loss carry-forward is the only other unit-level financial sentence. WHAT MAY BE
CONCLUDED: a Target unit economics series **cannot** be built from held print for most of the founding
decade, which is the §K.5 finding. WHAT MAY NOT: that the company lacked such figures internally.
RESIDUAL UNCERTAINTY: the `Five Year Comparisons` columns that OCR destroyed (`U.022`). CONFIDENCE:
**High**. ROUTE: `U.030`, `U.032`, `U.035`.

**U.022 — A rendering null, not an absence.** WHAT THE RECORD ASSERTS: the row labels of `Five Year
Comparisons` in FY1969, FY1970 and FY1971 exist with **no numeric columns**. EVIDENCE WEIGHT: the
FY1972 block prints some columns and FY1973's prints all five intact, which proves the data were
reportable. WHAT MAY BE CONCLUDED: the figures are absent **from the OCR**, not proven absent from the
reports. WHAT MAY NOT: any statement about the missing digits. RESIDUAL UNCERTAINTY: settled only by the
PDF leg or a ProQuest copy. CONFIDENCE: **High** that it is a rendering artifact. ROUTE: `U.030`.

**U.023 — The FY1970 byte count.** WHAT THE RECORD ASSERTS: the file on disk and its sidecar both say
**53,023 B**; the probe's table printed 52,736 B. EVIDENCE WEIGHT: the sidecar. WHAT MAY BE CONCLUDED:
the probe's table carries a transcription error, logged so no later pass re-imports it. RESIDUAL
UNCERTAINTY: none. CONFIDENCE: **High**. ROUTE: none needed; correct at merge.

**U.024 — The archive's own floor.** WHAT THE RECORD ASSERTS: item `01-target-archive` carries 61
DjVuTXT layers running **1965→2024**, gap-free from FY1965, with 17 PDF image legs for 1965-74 and
later years. EVIDENCE WEIGHT: held catalogue metadata (`P2S05`, 259,567 B). WHAT MAY BE CONCLUDED: this
is the reason FY1965 is the earliest held provenance for 1962 (`U.004`) — a **catalogue** fact, proven,
not inferred. WHAT MAY NOT: that no FY1964 report exists anywhere; no other carrier has been searched
(`U.032`, `U.034`). RESIDUAL UNCERTAINTY: the pre-1965 leg entirely. CONFIDENCE: **High** for the item.
ROUTE: `U.032`.

### U.3 UNANSWERED items — route or tool failure, never an absence

**U.025 — Whether any predecessor entity ever registered with the SEC.** WHAT WAS SEARCHED: EDGAR
name→CIK browse (`action=getcompany`) for `dayton+hudson`, `dey+brothers`, `goodfellow`,
`target+corporation`. RESULT: **HTTP 503 on all four**, bodies held as negative artifacts (7,747 B
each, `P2S02`). WHAT MAY AND MAY NOT BE CONCLUDED: the question is open; the EDGAR `formerNames` array
being one entry deep (`P2S06`) describes CIK 27419's own history, **not** the universe of registrants.
RESIDUAL UNCERTAINTY: total. CONFIDENCE: **UNANSWERED**. ROUTE: `U.036`.

**U.026 — Whether the company's own digital history exists in the web archive.** WHAT WAS SEARCHED:
Wayback CDX for `target.com*` (1996-2004) and `dhc.com*` (1996-2002). RESULT: **HTTP 503** twice, bodies
held (11,832 B each, `P2S04`). Even a live CDX could not reach 1962 — §14 rule 6 fixes this family's
floor in the mid-1990s — so it bears on K1/K4 provenance only. CONFIDENCE: **UNANSWERED**. ROUTE:
`U.037`-adjacent retry; the FY1999/FY2000 print layers cover the same event with better footing.

**U.027 — EDGAR full-text search's four zero-hit queries.** WHAT WAS SEARCHED: `"Dey Brothers"`,
`"Goodfellow"`, `"Dayton Hudson"`, `"Dayton Company"` restricted 1940-01-01→1995-12-31. RESULT: 0 hits
each (`P2S03`). INTERPRETATION: an **index floor** — the FTS corpus begins 2001 — and it must be
reported as a floor, never as a null on the entity, and never as evidence that the names were not used.
A control query with no date restriction has **not** been run. CONFIDENCE: **UNANSWERED**. ROUTE:
`U.035`, `U.036`.

**U.028 — Transport verification on five layers.** WHAT HAPPENED: verified TLS failed with
`CERTIFICATE_VERIFY_FAILED … certificate has expired` for `archive.org` on the FY1966, FY1967, FY1971,
FY1973 and FY1974 layers; the fetch completed with `--insecure` and every sidecar on those five stamps
`transport: UNVERIFIED TLS`. CONSEQUENCE: **every claim resting solely on those five layers is capped
at Medium**, which in this volume reaches Q3-Q8, Q16-Q19, the §K.3 five-year row, the §M productivity
rows and the FY1974 roster cross-check (`B1S02`, `B1S03`, `B1S07`, `B1S09`, `B1S10`). This is an
egress/trust-store defect, not an evidence result, and the bytes are readable and internally consistent.
CONFIDENCE: **UNANSWERED** (transport). ROUTE: `U.037`.

**U.029 — The intake tooling could not answer this brief, and two defects are live traps.** (a)
`ia_text.py search` returns `{"search": {"num": 1, "items": [{}]}}` for every query on this build
(the `fl[]`/`rows[]` repeated-parameter shape), which also disables `mine`; enumeration was done by
hand against the same endpoint (`P2S05`). (b) `ia_text.py fetch` 404s on any IA filename containing
spaces because `ocr_url()` does not percent-encode, and — the trap — `text_layer_names()` would have
returned the **largest** of the item's 62 text layers (a 2024 report) as one cached file for
`--id 01-target-archive`, so an agent running the briefed command would hold the wrong year while
believing it held FY1966. (c) `sec_intake.py index` discards `formerNames` and the slice list, the
single most useful registrant fact found. (d) `periodical_harvest.py` has **no task set for this
company** in `tools/queries.json` (49 tasks verified, none for Dayton/Goodfellow/Target). All four are
**tool defects for the orchestrator**, evidence-neutral, and reported rather than worked around.
CONFIDENCE: **UNANSWERED** (tooling). ROUTE: hand off to the orchestrator; `U.032`, `U.034`.

### U.4 UNTRIED routes — with the exact command or archive that would settle each

**U.030 — The 17 PDF image legs of the same item (highest value per call remaining).** Would settle
`U.008` (the one-store 1971 difference), `U.009` (`(1961)` vs `(1967)`), `U.012` (the area basis),
`U.020` (the FY1968 officer page) and `U.022` (the destroyed five-year columns). ROUTE: read the exact
per-year PDF filenames out of `sources/ia_search/meta_01-target-archive.json`, then
`https://archive.org/download/01-target-archive/<exact filename>` through `ia_text.get()`, into
`sources/corporate_print_pdf/` with sidecars, and re-OCR the roster and comparison pages. Alternative
archive: a **ProQuest Historical Annual Reports** copy of the FY1969-FY1974 reports (the service is
named inside the held FY1975 layer, `B1S11`), reachable through a subscribing library.
CONFIDENCE: untested. STATUS: **UNTRIED** — this pass ran no PDF leg.

**U.031 — A held independent primary for the founder conflict `U.001`.** Would turn a recorded
conflict into an adjudicated one. ROUTE: fetch the 2013-07-06 *Twin Cities*/St Paul Pioneer Press
Douglas Dayton obituary and a John F. Geisse obituary (the *New York Times* carries one dated
1992-02) into `sources/documentary/` with sidecars; **web budget for this volume is 0 calls**, so this
is a FETCH REQUEST for the orchestrator, naming the two carriers and the destination path, not a
retrieval this pass may perform. CONFIDENCE: untested. STATUS: **UNTRIED**.

**U.032 — The pre-1965 leg, in the two book corpora that reach it.** Would test `U.004`, `U.019`,
`U.021`, `U.024` and could lift the tier from T2 to T1. ROUTE: add a `target` task set to
`tools/queries.json` (editing `tools/` is outside this pass's write scope) and run
`python tools/periodical_harvest.py --company-dir founders_playbook/01_companies/company_042_target --query-set target_dayton_print_1955_1964 --use-curl`
(HathiTrust needs `--use-curl` per `tools/HARVEST_README.md`); Google Books needs `GOOGLE_BOOKS_API_KEY`,
which is absent. Targets: `Target Stores, Inc.` 1962-1966 mentions; Dayton Company reports
FY1955-FY1964; the Dayton's/Goodfellow genealogy in Minneapolis print. STATUS: **UNTRIED**.

**U.033 — The route to a day, `U.002`.** ARCHIVES: Minneapolis *Star Tribune* and *St. Paul Pioneer
Press* back-files for 1961-08 → 1962-12 (advertising and opening notices); the Sentinel microfilm of the
*Pioneer Press* held at the Minnesota Historical Society / Minnesota State Archives; MNHS collections
for Dayton's and Goodfellow ephemera. Chronicling America returns no Minnesota 1962 coverage for this
window per the probe, so it is a named dead end rather than an untried route. STATUS: **UNTRIED**.

**U.034 — A second carrier for the same years, to break the one-lineage ceiling of §T.2.** ROUTE:
Internet Archive advancedsearch restricted to `collection:(fund-and-stock-reports)` for independently
digitised Dayton Company / Dayton Corporation reports FY1962-FY1964, e.g.
`https://archive.org/advancedsearch.php?q=collection%3A%28fund-and-stock-reports%29+AND+title%3A%28dayton%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=50&output=json`
— noting the `fl[]` shape defect in `U.029`, so the call must be made directly rather than through
`ia_text.py search`. STATUS: **UNTRIED**.

**U.035 — The XBRL and first-10-K bridge.** ROUTE: `python tools/sec_intake.py facts --ticker TGT
--company-dir founders_playbook/01_companies/company_042_target`, and fetch accession
`0000950131-94-000539` (the FY1993 10-K filed 1994-04-21, the registrant's first, named in
`sources/_index/_INDEX.md`) for its five-year selected-data table reaching 1989. It is a `(PB)` leg but
the only Tier-1 electronic bridge. STATUS: **UNTRIED** (never invoked).

**U.036 — The predecessor-CIK question `U.025`.** ROUTE: retry the browse endpoint with a compliant
User-Agent — `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=dayton+dry+goods&type=&dateb=&owner=include&count=40`
and the same for `j.l. hudson`, `dayton company`, `dey brothers` — then, for any CIK returned,
`python tools/sec_intake.py index --cik <n> --from 1930-01-01 --to 1985-12-31`. Until this runs, "one
registrant line only" is the limit of the EDGAR record, **not** a proof that no predecessor filed.
STATUS: **UNTRIED** (blocked by 503 in the probe).

**U.037 — Re-verification of the five unverified layers `U.028`.** ROUTE: repair or bypass the stale
local CA store (`pip install --upgrade certifi`, or the harvest tools' documented `--use-curl`
fallback), re-fetch the same five per-year layers, and re-stamp their sidecars to
`transport: verified TLS`; until then Q3-Q8, Q16-Q19, the §K.3 row and the FY1974 roster stay under the
Medium cap. STATUS: **UNTRIED** by this pass (it holds no network budget).

### U.5 Coda: what this section is evidence of

Thirty-seven entries, of which seventeen are genuine conflicts, seven are searches that came back
empty, five are routes that failed or tools that are broken, and eight are work nobody has done yet. The
asymmetry is the finding: this company's Stage 1 is **document-rich and source-poor** — eleven
consecutive years of its own print, with a gap-free FY1965→FY1975 run, and not one independent carrier
for the act the whole volume is about. The correct summary of the 1962 founding is therefore not "the
record is thin" but "**the record is one voice**, and the routes that could produce a second have been
named rather than walked" (`U.004`, `U.031`, `U.032`, `U.033`). Everything in §P, §K and §R inherits
that ceiling, and no amount of confidence grading can raise it: the fix is `U.030`-`U.037`, in that
order of cost.

STATUS: WRITTEN 2026-09-25


## Claim records (P2 block — appendix extract for §I–§U)

Load-bearing claims established on this pass only; `B1-01`–`B1-12` live in
`research/B1_dayton_print_records.md` and are not repeated. IDs are dossier-local (`P2-nn`) and are
remapped centrally at merge (§13). `Passage:` is verbatim from held bytes, ≤40 words, as printed.

```
P2-01 Claim: The layer this corpus calls FY1965 reports a fiscal year that ended 1966-01-29, and labels the same column both 1965 and 1966 inside one document. — Date: 1966-01-29 — Source: The Dayton Company Annual Report 1965, SALES section — Source date: 1966 (cover 1965) — URL: local bytes sources/corporate_print/1965_dayton_hudson_djvu.txt — Archived: held locally — Tier: 1 — Class: FACT — Passage: "Net sales of The Dayton Company and retail subsidiaries during the fiscal year ended January 29, 1966, were $186,166,671, the largest in the Company's history." — Conf: High — Corroboration: 0 independent (pattern confirmed only inside the same lineage by B1S02, which prints a fiscal year ended January 28, 1967 under a 1966 cover) — Conflicts: U.011
P2-02 Claim: At the moment of the first public annual report the company described itself as privately owned and the report as its first public one. — Date: 1966 (cover 1965) — Source: The Dayton Company Annual Report 1965, opening letter — Source date: 1966 — URL: as P2-01 — Archived: held locally — Tier: 1 — Class: FACT — Passage: "The projected growth of The Dayton Company requires that it expand beyond the concept of a privately-owned operation." — Conf: High — Corroboration: 1 — Conflicts: U.017
P2-03 Claim: The parent printed Target-unit growth rates of 44 percent on sales and 100 percent on pre-tax profit for fiscal 1965, with no dollar base printed. — Date: FY1965 — Source: The Dayton Company Annual Report 1965, opening letter — Source date: 1966 — URL: as P2-01 — Archived: held locally — Tier: 1 — Class: FOUNDER CLAIM — contemporaneous, company-as-founder — Passage: "The potential of Target is demonstrated by gains of 44 percent in sales and 100 percent in pre-tax profits in 1965 over the previous year." — Conf: High (printed), UNKNOWN (base) — Corroboration: 0 — Conflicts: U.013, U.021
P2-04 Claim: Target Stores, Inc. still carried a loss forward into the group's 1964 tax computation, which is the earliest unit-level profit statement in the corpus. — Date: 1964 — Source: The Dayton Company Annual Report 1965, EARNINGS section — Source date: 1966 — URL: as P2-01 — Archived: held locally — Tier: 1 — Class: FACT (magnitude UNKNOWN) — Passage: "The percentage increase in after-tax earnings was somewhat less because of a substantial loss carry-forward available to Target Stores, Inc., in 1964." — Conf: High — Corroboration: 0 — Conflicts: U.016
P2-05 Claim: Lease economics are printed only at parent scope, as an aggregate minimum with percentage-of-sales clauses and a related-party component. — Date: 1966-01-29 — Source: The Dayton Company Annual Report 1965, LEASES note — Source date: 1966 — URL: as P2-01 — Archived: held locally — Tier: 1 — Class: FACT — Passage: "Long-term leases at January 29, 1966 require aggregate minimum annual rentals of approximately $1,564,220, of which $626,683 is payable to unconsolidated subsidiaries." — Conf: High — Corroboration: 0 — Conflicts: U.012
P2-06 Claim: The only held forward-cost figure near the founding decade is a consolidated facility commitment, not a store cost. — Date: 1966 (subsequent events) — Source: The Dayton Company Annual Report 1965, SUBSEQUENT EVENTS — Source date: 1966 — URL: as P2-01 — Archived: held locally — Tier: 1 — Class: FACT — Passage: "The Company and its subsidiaries have commitments in the amount of approximately $3,750,000 for additional facilities." — Conf: High — Corroboration: 0 — Conflicts: U.012
P2-07 Claim: The Dayton Company's separate receivables operation began on 1966-01-15 and opened at a loss. — Date: 1966-01-15 — Source: The Dayton Company Annual Report 1965, NOTE A of the subsidiary statements — Source date: 1966 — URL: as P2-01 — Archived: held locally — Tier: 1 — Class: FACT — Passage: "The Company (which commenced operations on January 15, 1966)" — Conf: High — Corroboration: 0 — Conflicts: None (motive UNKNOWN, §N.1)
P2-08 Claim: Seven Target units were in operation under cover-year 1966, with a stated total retail area. — Date: 1967-01-28 (period end) — Source: Dayton Company Annual Report 1966 — Source date: 1967 — URL: local bytes sources/corporate_print/1966_dayton_hudson_djvu.txt — Archived: held locally, transport UNVERIFIED TLS — Tier: 1 — Class: FACT — Passage: "Total retail area of the seven Target stores now in operation is 889,000 square feet." — Conf: Medium (capped by U.028) — Corroboration: 0 — Conflicts: U.012
P2-09 Claim: The FY1974 estate roster prints four units with opening year 1962, each with an area digit, and lists Knollwood under St. Louis Park. — Date: 1962, printed 1974 (PB) — Source: Dayton Hudson Corporation Annual Report 1974, LOW MARGIN STORES roster — Source date: 1975 (cover 1974) — URL: local bytes sources/corporate_print/1974_dayton_hudson_djvu.txt — Archived: held locally, transport UNVERIFIED TLS — Tier: 1 — Class: RESTATED INTERPRETATION (retrospective roster) — Passage: "Roseville, Minn. 68 1962 Crystal, Minn. 96 1962 Duluth, Minn. 96 1962 Knollwood, St. Louis Park, Minn. 106 1962" — Conf: Medium — Corroboration: 0 (same lineage as B1S01) — Conflicts: U.015, U.012, U.016
P2-10 Claim: One low-margin-group row, printed in FY1973, supplies revenue, store count, square footage and sales per square foot for 1969-1973 and foots to itself in all five columns. — Date: 1969-1973 (PB) — Source: Dayton Hudson Corporation Annual Report 1973, Five Year Comparisons — Source date: 1974 (cover 1973) — URL: local bytes sources/corporate_print/1973_dayton_hudson_djvu.txt — Archived: held locally, transport UNVERIFIED TLS — Tier: 1 — Class: RESTATED for 1969-1972, CONTEMPORANEOUS for 1973 — Passage: "LOW MARGIN STORES Sales (millions) $ 470.3 $ 440.4 $ 345.8 $ 289.0 $ 233.5" — Conf: Medium — Corroboration: 0 — Conflicts: U.010, U.013
P2-11 Claim: The company printed a maintenance-spend reduction as a factor in its own record fiscal-1965 earnings. — Date: FY1965 — Source: The Dayton Company Annual Report 1965, EARNINGS section — Source date: 1966 — URL: as P2-01 — Archived: held locally — Tier: 1 — Class: FACT — Passage: "A factor in the 1965 earnings figures was a reduction in repair and maintenance expenses of approximately $1,130,000 from the 1964 level." — Conf: High — Corroboration: 0 — Conflicts: U.018-adjacent (statement-of-income digits, §M.1)
P2-12 Claim: One running foot in the held April 1963 trade-periodical layer prints an April 1962 date. — Date: 1963-04 — Source: Chain Store Age, Steel for Stores gather — Source date: 1963-04 — URL: local bytes sources/periodicals_csa_1963/Chain_store_age_Steel_for_Stores_djvu.txt — Archived: held locally, verified TLS — Tier: 3 — Class: FACT (as printed) — Passage: "CHAIN STORE AGE, APRIL 1962" — Conf: Medium — Corroboration: 0 — Conflicts: U.014
```

>>> REGISTER ROWS FOR MERGE <<<

**No register CSV was opened, edited, moved or deleted by this pass.** These rows are emitted for the
merge to apply, in each target file's exact column order. `stage` is the controlled literal `stage1`
on every row. Every `source_id` here (`B1S..`, `P2S..`) is dossier-local and is remapped centrally at
merge; the merge must also apply the `U.011` re-dating of B1's Q20 row (186,166,671 → year ended
1966-01-29; 162,773,739 → year ended 1965-01-30) as a **superseding note inside the same cell**, not as
a deletion, per §14 rule 8.

### sources.csv (18 columns)

```csv
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
P2S01,stage1,P2-08 U.012,Q 'The Dayton Company' Annual Report 1966 (OCR text layer),The Dayton Company,corporate stockholder report,primary,1966;1967,1967,2026-09-26,archive.org item 01-target-archive per-year DjVuTXT layer (exact URL in file sidecar),held locally: sources/corporate_print/1966_dayton_hudson_djvu.txt,1,CONTEMPORANEOUS,Medium,same lineage as B1S01 - one source however many report years,'Total retail area of the seven Target stores now in operation is 889,000 square feet.','TRANSPORT UNVERIFIED TLS so capped at Medium (U.028); 43364 B; fiscal year ended 1967-01-28 under a 1966 cover (U.011)'
P2S02,stage1,U.025,U four EDGAR name-to-CIK browse responses returned HTTP 503,SEC EDGAR,negative artifact (error page),primary,1962-1999,UNKNOWN,2026-09-26,https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany (four company terms),held locally: sources/name_search/dayton+hudson.atom + dey+brothers.atom + goodfellow.atom + target+corporation.atom,1,UNANSWERED - dead route,UNANSWERED,not a source of facts and never citable as an absence,(no readable passage - 7747 B SEC error page each),UNANSWERED not null: a predecessor registrant was never ruled in or out (U.025; route U.036)
P2S03,stage1,U.005 U.027,U four EDGAR full-text-search responses with zero hits in 1940-1995,SEC EDGAR,API JSON (index-floor artifact),primary,1940-1995,UNKNOWN,2026-09-26,https://efts.sec.gov/LATEST/search-index?q=... (four terms; date range 1940-01-01 to 1995-12-31),held locally: sources/name_search/fts_*Dayton+Company*.json + fts_*Dey+Brothers*.json + fts_*Goodfellow*.json + fts_*Dayton+Hudson*.json,1,INDEX FLOOR - not a null,UNANSWERED,the FTS corpus begins 2001 so a zero here cannot describe 1940-1995,(no readable passage),never reportable as absence of the entity (U.027); unrestricted control query never run
P2S04,stage1,U.026,U two Wayback CDX responses returned HTTP 503,Internet Archive,negative artifact (error page),primary,1996-2004,UNKNOWN,2026-09-26,https://web.archive.org/cdx/search/cdx?url=target.com* and url=dhc.com*,held locally: sources/web_archive/cdx_targetcom.txt + cdx_dhc.txt,1,UNANSWERED - dead route,UNANSWERED,independent of the company but unreachable,(no readable passage - 11832 B offline body each),family b contributed 0 held bytes; even a live CDX cannot reach 1962 (U.026)
P2S05,stage1,U.006 U.024,'01-target-archive' item metadata listing,Internet Archive,catalogue metadata,primary,1965-2024,UNKNOWN,2026-09-26,https://archive.org/metadata/01-target-archive,held locally: sources/ia_search/meta_01-target-archive.json,1,CATALOG-LEVEL FACT,High,the only evidence for the 1965 to 2024 layer run,61 DjVuTXT layers listed with per-file names,proves the FY1965 floor (U.024) and proves the uploader labels are wrong (U.006); 259567 B
P2S06,stage1,U.003 U.007,EDGAR submissions index for CIK 0000027419 including formerNames and the slice list,SEC EDGAR,regulatory index JSON/CSV,primary,1994-02-10 to 2026-09-18,UNKNOWN,2026-09-26,https://data.sec.gov/submissions/CIK0000027419.json,held locally: sources/_index/raw_submissions_CIK0000027419.json + _INDEX.md + submissions.csv (2628 rows),1,REGISTRANT-LINE FACT,High,independent of the company,formerNames: DAYTON HUDSON CORP from 1994-12-09 to 1999-04-12,no document before 1994-02-10 and no UNANSWERED slices; silent on 1962 by construction
P2S07,stage1,U.027,sources/sec/_MANIFEST.csv header only,sec_intake.py,intake manifest,negative artifact,1960-01-01 to 1985-12-31,2026-09-26,2026-09-26,local: sources/sec/_MANIFEST.csv,local,1,MANIFEST OF AN EMPTY WINDOW,High,proves the route ran,0 documents stored,0 skipped/unanswered,never cite as absence of filings: EDGAR carries no paper-era filings at all
P2S08,stage1,P2-10 U.012,U 'Dayton Hudson Corporation' Annual Report 1973 five-year block (re-read this pass),Dayton Hudson Corporation,corporate stockholder report,primary,1969-1973,1974,2026-09-26,archive.org item 01-target-archive per-year DjVuTXT layer (exact URL in file sidecar),held locally: sources/corporate_print/1973_dayton_hudson_djvu.txt,1,RESTATED 1969-1972 / CONTEMPORANEOUS 1973,Medium,same lineage as B1S08/B1S09 - one source,'Number of stores 50 50 34 27 19' and 'Total square feet (thousands) 5,563 5,518 4,220 3,516 2,390',duplicate of B1S09 at merge; the row foots to itself in all five columns (section K.3); UNVERIFIED TLS
```

### quantitative.csv (12 columns) — new rows only, IDs continue B1's Q-series

```csv
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
Target,stage1,1966-01-29,parent_net_retail_sales_incl_leased_departments,186166671,USD,B1S01 Statement of Income and SALES note,1966,FACT,High,,"CONTEMPORANEOUS for the fiscal year ENDED 1966-01-29, printed under a cover labelled 1965 - this row SUPERSEDES the date on B1's Q20 for the same digits (U.011); whole company, NOT Target"
Target,stage1,1965-01-30,parent_net_retail_sales_incl_leased_departments,162773739,USD,B1S01 Statement of Income comparative column,1966,FACT,High,,"CONTEMPORANEOUS for the year ended 1965-01-30; re-dates B1's Q20 label of 1964 (U.011); printed growth 14 percent"
Target,stage1,1966-01-29,parent_operating_income,14233981,USD,B1S01 Statement of Income,1966,FACT,High,,"whole company; prior year 9,616,914"
Target,stage1,1966-01-29,parent_net_income,7128981,USD,B1S01 Statement of Income and EARNINGS note,1966,FACT,High,,"printed as a 31 percent gain over 5,435,205"
Target,stage1,1966-01-29,parent_eps_post_split,1.99,USD per common share,B1S01 EARNINGS section,1966,FACT,High,,"restated prior-year EPS 1.41; printed increase 41 percent; after ten-for-one split and 100 percent stock dividend"
Target,stage1,1966-01-29,parent_cost_of_sales_buying_and_occupancy_combined,139686954,USD,B1S01 notes,1966,FACT,High,,"OCCUPANCY IS FUSED INTO COST OF SALES AND BUYING: no held document separates occupancy, which is the named reason per-store economics are UNQUANTIFIABLE (section K.5)"
Target,stage1,1966-01-29,parent_sga_expense,31256511,USD,B1S01 notes,1966,FACT,High,,"prior year 28,508,046"
Target,stage1,1966-01-29,parent_rentals_expense_line,2088720,USD,B1S01 Statement of Income deduction block,1966,FACT,High,,"parent consolidated scope, NOT Target; not to be confused with the LEASES-note minimum (next row) - different definitions, not a conflict"
Target,stage1,1966-01-29,parent_long_term_lease_minimum_annual_rentals,1564220,USD approximately,B1S01 LEASES note,1966,FACT,High,,"of which 626,683 payable to UNCONSOLIDATED SUBSIDIARIES; some leases carry percentage-of-sales increases; no store-level rent is printed"
Target,stage1,1966-02-01,parent_commitments_for_additional_facilities,3750000,USD approximately,B1S01 SUBSEQUENT EVENTS,1966,FACT,High,,"consolidated, all divisions; the division by two Denver stores is DELIBERATELY NOT COMPUTED (section K.2 refusal 1)"
Target,stage1,1966-01-29,parent_sinking_fund_notes_outstanding,13600000,USD,B1S01 LONG-TERM DEBT note (1),1966,FACT,High,,"rate printed as 5 percent with a corrupted fraction (5% %); matures 800,000 annually each January 31 1965-1981, balance 1982-01-31; covenants restrict sale of receivables, working capital, dividends"
Target,stage1,1966-01-29,parent_mortgage_notes_outstanding,2124960,USD,B1S01 LONG-TERM DEBT note (2),1966,FACT,High,,"carrying cost of land/buildings/fixtures/equipment is printed in the following lines"
Target,stage1,1966-03-31,parent_stock_dividend_transfer_from_retained_earnings,1535500,USD,B1S01 SUBSEQUENT EVENTS,1966,FACT,High,,"one new common share per share outstanding after the ten-for-one split; declared February 1966, transferred March 1966"
Target,stage1,1966-01-29,parent_lifo_reserve,664219,USD,B1S01 MERCHANDISE INVENTORIES note,1966,FACT,High,,"inventories stated below the non-LIFO retail-method amount; prior year 431,573; LIFO retail method is the merchandise-control technology of record (section J.1c)"
Target,stage1,1965,target_unit_sales_growth_rate,44,percent over previous year,B1S01 opening letter,1966,FACT that it was printed; base UNKNOWN,Medium,,"RATE ONLY - the FY1964 Target dollar base is printed nowhere (U.021); do not apply to Q21 (U.013)"
Target,stage1,1965,target_unit_pretax_profit_growth_rate,100,percent over previous year,B1S01 opening letter,1966,FACT that it was printed; base UNKNOWN,Medium,,"against the same period's consolidated pre-tax gain of 48 percent - different entities (U.013)"
Target,stage1,1964,target_unit_loss_carryforward_available,magnitude UNKNOWN,USD,B1S01 EARNINGS section,1966,FACT of existence; UNKNOWN of amount,Medium,,"the only unit-level financial sentence before FY1967; the unit had not earned out start-up losses by 1964 (U.016)"
Target,stage1,1967-01-28,target_stores_total_retail_area,889000,square feet,B1S02 (fiscal year ended 1967-01-28),1967,FACT,Medium,,"seven stores in operation; basis is TOTAL RETAIL AREA and does not foot to the FY1974 roster column (U.012); UNVERIFIED TLS"
Target,stage1,1967-01-28,target_avg_retail_area_per_store,127000,square feet,B1S02 same sentence,1967,ESTIMATE,Medium,889,000 / 7 = 127,000,"DERIVED within one sentence, one basis, one year; NOT to be joined to any other year's count"
Target,stage1,1973-12-31,low_margin_group_total_square_feet,5563,thousands of square feet,B1S09 P2S08 Five Year Comparisons,1974,FACT,Medium,,"1969-1973 in column order: 2,390 / 3,516 / 4,220 / 5,518 / 5,563; GROUP scope (Target plus hard goods), (PB)"
Target,stage1,1973-12-31,low_margin_group_sales_per_square_foot,84.54,USD per square foot,B1S09 P2S08,1974,FACT,Medium,,"1969-1973: 97.70 / 82.18 / 81.94 / 79.81 / 84.54; (PB); the block foots: 470.3m/5,563k = 84.5"
Target,stage1,1973-12-31,low_margin_group_pretax_margin_pct_of_sales,1.4,percent of sales,B1S09 P2S08,1974,FACT,Medium,,"1969-1973: 3.3 / 3.0 / 4.0 / 2.1 / 1.4; (PB)"
Target,stage1,1973-12-31,low_margin_group_sales_per_sqft_change_1969_to_1973,-13.5,percent,B1S09 P2S08 one row one basis,1974,ESTIMATE,Low,84.54 / 97.70 - 1 = -0.1347,"DERIVED within one row and one basis, comparing two years of the SAME printed row (not a cross-year division of mismatched objects); (PB)"
Target,stage1,1969-12-31,low_margin_group_revenue_per_store_1969,12.29,USD millions,B1S09 five-year row,1974,ESTIMATE,Low,233.5 / 19 = 12.29,"GROUP basis NOT Target; same-column division only; (PB); the Target-unit equivalent is not computable from held print (U.021)"
Target,stage1,1972-12-31,low_margin_group_revenue_per_store_1972,8.81,USD millions,B1S09 five-year row with B1S08,1974,ESTIMATE,Low,440.4 / 50 = 8.81,"GROUP basis, same-column division, (PB); shows the direction of the productivity fall, not Target economics"
Target,stage1,1962-12-31,target_store_area_1962_openings,68;96;96;106,thousands of square feet (basis label OCR-corrupt),B1S10 roster (PB),1975,FACT as printed,Medium,,"Roseville 68; Crystal 96; Duluth 96; Knollwood St.Louis Park 106 as printed in FY1965; sum for the seven units to 1966 = 722 against B1S02's 889 (U.012)"
Target,stage1,1965-01-30,parent_maintenance_and_repairs,1894037,USD,B1S01 Statement of Income deduction block,1966,FACT,Medium,,"the following-year column prints 763,572, a fall larger than the narrative's 1,130,000 reduction explains - digit-level OCR doubt recorded in section M.1, not resolved"
```

### timeline.csv (11 columns) — new rows only

```csv
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
Target,stage1,1962,Four Target units carry opening year 1962 in the company's own chronology spread: Roseville, Crystal, Duluth and Knollwood St.Louis Park,Target Stores Inc and The Dayton Company,"Roseville, Crystal, Duluth, Knollwood St.Louis Park, Minnesota",B1S01,RETROSPECTIVE INTERPRETATION at three years' remove,Medium,K2 U.015,place names transcribed AS PRINTED including ST.LOUIS PARK with no space; the FY1974 roster agrees with the pairing (PB)
Target,stage1,1965,fiscal year of the layer labelled 1965 ends 1966-01-29 and the same column is labelled 1966 in the notes,The Dayton Company,Minneapolis,B1S01,FACT,High,U.011,this row is the re-basing key for the whole Q-series; refutes the inherited assumption that fiscal equals calendar
Target,stage1,1966-01-15,Dayton Credit Company commences operations and prints a two-week operating loss,The Dayton Company,Minneapolis,B1S01,FACT,High,None,earliest calendar-exact operating date anywhere in the held corpus
Target,stage1,1966-02,Annual meeting approves a ten-for-one stock split; a 100 percent stock dividend is declared the same month,The Dayton Company shareholders,Minneapolis,B1S01,FACT,High,None,transfer of 1,535,500 from retained earnings to Common Stock in March 1966
Target,stage1,1966,The company states it is moving beyond a privately-owned operation by issuing its first public annual report,The Dayton Company,Minneapolis,B1S01,FACT,High,U.017,disclosure decision; distinct from the first public stock offering of late 1967 printed by B1S06
Target,stage1,1967-01-28,Seven Target stores in operation with a stated total retail area of 889,000 square feet,Target Stores Inc,Denver Colo and Minnesota,B1S02,FACT,Medium,U.012,period end 1967-01-28 under a 1966 cover (U.011); UNVERIFIED TLS (U.028)
Target,stage1,1973-12-31,The only intact five-year low-margin row in the run prints revenue stores square footage and sales per square foot for 1969-1973,Dayton Hudson Corporation,Minneapolis,B1S09,RESTATED 1969-1972 / CONTEMPORANEOUS 1973,Medium,K9 U.010 U.013,(PB); the row foots to itself in all five columns
Target,stage1,1974,The estate roster prints the Target unit as (1967) under Stephen L. Pistner as President with a per-store area column,Dayton Hudson Corporation,Minneapolis,B1S10,RESTATED roster,Medium,K6 K7 U.009 U.012,(PB); the 1962 rows carry areas 68/96/96/106 which do not foot to the FY1966 total of 889,000
```

### conflicts.csv (15 columns) — one row per §U conflict anchor

```csv
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
Target,stage1,K1,U.001 section U.1 and section B, Douglas Dayton is the founder of Target Stores, Twin Cities / Pioneer Press obituary (NOT HELD),2013-07-06,John F. Geisse originated and headed the Target concept,Geisse biography pages (NOT HELD),UNKNOWN,company print names both as officers from FY1965 and credits neither with the decision,held bytes settle ROLES only and GEISSE disappears from the officer pages after FY1967 while Dayton remains,no founder is settled and no averaging is applied,neither independent carrier exists as bytes so the conflict is unadjudicable from this corpus,Low
Target,stage1,K2,U.002 section U.1 and section D,The first Target store opened early in 1962 in Roseville,The Dayton Company Annual Report 1965,1962,The first Target store opened 1962-07-01,commonly repeated secondary accounts with NO carrier held,UNKNOWN,side A is a held primary that refuses the month; side B is precision the held record never produces,a month-with-1962 search returns zero over 781995 chars in eleven layers,keep 1962 Roseville with month and day UNKNOWN,whether any 07-01 carrier was ever printed is UNKNOWN,High that it is unresolved
Target,stage1,K3,U.003 and U.006 section U.1,the 1965 file is a Dayton Hudson Corp report (uploader filename),item 01-target-archive file labels,UNKNOWN,the 1965 masthead in bytes reads THE DAYTON COMPANY ANNUAL REPORT 1965,held layer opening lines,1965,the uploader label is applied to every year 1965-1998 regardless of the entity inside,text outranks filename; a register built on filenames would misdate the 1969 merger by four years,attribute every figure to the masthead that printed it,none material - procedural and applied throughout,High
Target,stage1,K4,U.004 section U.1,the 1962 launch is documented,The Dayton Company Annual Report 1965,1962, the 1962 launch is documented by one carrier three years after the fact,archive catalogue metadata (P2S05) and the FY1965 run floor,2026-09-26,the item's text layers begin at FY1965 so no earlier provenance is held,fact and single-source fact look identical in a one-carrier corpus,keep the act at FACT and everything inside it at Medium; keep founder pre-history at UNKNOWN rather than deleting it,whether any 1962-64 document survives anywhere is untested,High
Target,stage1,K5,U.005 section U.1,Dey Brothers is a predecessor name,dispatch premise and an EDGAR search term,UNKNOWN,Dey returns zero hits across all eleven founding-era layers,held layers,1965-1975,the premise circulates in company histories while the EDGAR zeros come from a post-2001 index,the print null is real; the EDGAR zero is a floor and cannot answer,unestablished not disproved; any later stage inheriting it must retraction-test under rule 8,a control query with no date restriction was never run,High that it is unestablished
Target,stage1,K4b,U.007 section U.1 (PB),EDGAR ends DAYTON HUDSON CORP on 1999-04-12,raw submissions JSON,1999-04-12,The name changed in 2000,dispatch premise,2000,a parent-level filing date versus a division-level readoption versus a report-year label,EDGAR is authoritative for the parent act; no held document states the 2000 leg,1999 parent change is documented and the 2000 leg stays a conflict,which act each source dates,High for 1999 and Low for 2000
Target,stage1,K6,U.008 section U.1 (PB),Target had 30 stores at year-end 1971,Dayton Hudson Annual Report 1971,1971,the FY1974 roster enumerates 29 cumulative,Dayton Hudson Annual Report 1974,1974,the roster lists only units still operating in 1974 and a row may be OCR loss,both are one lineage so neither corroborates the other; CONTEMPORANEOUS outranks RESTATED as priority only,report both with a one-unit difference of UNKNOWN mechanism,which store and which document is at fault,Medium
Target,stage1,K7,U.009 section U.1 (PB),The Target unit carries parenthetical year 1961,Dayton Hudson Annual Report 1973,1973,the same unit carries 1967,Dayton Hudson Annual Report 1974,1974,OCR corruption of a small parenthetical in a dense two-column list,neither is legible enough to carry a date claim,UNKNOWN and explicitly not used to move 1962,only the original page settles it,Low
Target,stage1,K8,U.011 section U.1 (NEW - re-bases the series),The layer is the 1965 annual report,cover label and narrative prose,1965,the statements inside it are for the fiscal year ended January 29 1966 and the notes call that column 1966,held statement headers and notes,1966,the entity names a fiscal year by its starting calendar year in prose and by its ending year in the notes,documentary: both labels sit inside audited statements; the pattern repeats under the 1966 cover (period ended 1967-01-28),every row carries the fiscal PERIOD END as its date and B1's Q20 labels are corrected at merge as a superseding note,whether FY1968 onward follows the same pattern was not tested by this pass,High
Target,stage1,K9,U.010 section U.1 (PB),1968 department-store revenue was 223276791 USD,Dayton Corporation annual report,1968,the 1968 department-store column is 582923 USD thousands,Dayton Hudson annual report,1969,the later column is the merged scope including The J L Hudson Company of Detroit,RESTATED is never corroboration of CONTEMPORANEOUS and each set foots to its own scope,print both each labelled by its filer,which 1969 consolidation date produced the wider column is not established,High
Target,stage1,K10,U.012 section U.1 (NEW),Seven Target stores total 889000 square feet of retail area,Dayton Company annual report cover-year 1966,1967,the same seven units sum to 722 thousand in the estate roster,Dayton Hudson annual report cover-year 1974,1975,two different area bases (total retail area versus an OCR-corrupt column label),each is internally consistent within its own table and neither is arithmetic on the other,report both and never mix them in one ratio or series; the seven-store average is stated only as 889000/7 DERIVED,only the PDF page names the roster basis,Medium
Target,stage1,K11,U.013 section U.1 (NEW),Target grew 44 percent in sales and 100 percent in pre-tax profit,annual report cover-year 1965 opening letter,1965,the company grew 14 percent in sales and 31 percent in net income,same document SALES and EARNINGS sections,1965,different reporting objects in adjacent paragraphs of one document,both are company print; the Target pair is a rate with no printed base,label the 44/100 pair Target-unit rate-only base UNKNOWN and the 14/31/48 set consolidated,Target's FY1964 dollar base is printed nowhere,High
Target,stage1,K12,U.014 section U.1 (NEW),The held trade-periodical leg is April 1963,running feet and item metadata,1963,one running foot reads CHAIN STORE AGE APRIL 1962,held layer,1962,OCR corruption or a bound-in gathering page,majority of feet plus side numbering plus metadata point to 1963-04,cite 1963-04 and record the anomaly so no transcriber creates the corpus's only launch-year periodical,what the physical page says,Medium
Target,stage1,K13,U.015 section U.1 (NEW),The fourth 1962 store is printed KNOLLWOOD ST.LOUIS PARK MINNESOTA 1962,annual report cover-year 1965 chronology spread,1965,the same unit is printed Knollwood St Louis Park Minn 106 1962,annual report cover-year 1974 roster,1975,typesetting and OCR rather than geography; the abbreviation loses its space in the earlier print,both name the same unit and the roster adds an area digit,transcribe as printed in every quotation and register row and never silently correct the place name,whether this opening preceded or followed Roseville is not printed,High
Target,stage1,K14,U.016 section U.1 (NEW),Target had 17 stores in 1969 and 24 in 1970,derived counts carried in the register,1969-1970,no held layer prints a Target year-end count for either year,held layers,1969-1973,the counts come from a 1973 recap base plus printed opening lists and the FY1974 roster's own opening lists,derivation is transparent and reproducible and the group counts (19 and 27) are consistent with it but consistency is not printing,keep both rows classed DERIVED with derived_arithmetic filled and never as observations,a store opening and closing inside one year is invisible to both methods,Low as observations and High as arithmetic
Target,stage1,K15,U.017 section U.1 (NEW),The company was privately owned and this was its first public annual report,annual report cover-year 1965 opening letter,1965,The first public stock offering came in late 1967 with 23 stores in five states,annual report cover-year 1970,1970,two different acts: a disclosure decision while private and a securities offering two years later,both documents are explicit and of one lineage,record the sequence private - first public report - first public offering - NYSE listing 1969-09-08 (PB),what public meant in the 1966 sentence since the report was printed not filed,High on the sequence and Medium on the characterisation
```

### data_gaps.csv (8 columns) — nulls U.018-U.024, UNANSWERED U.025-U.029, UNTRIED U.030-U.037

```csv
company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task
Target,stage1,U.018 month and day of the first Target opening,held company text says only early in 1962 and a month-with-1962 search over 781995 chars in eleven layers returned zero,High,B1S01 essay sentence stating early in 1962 in Roseville,High,U.033 Star Tribune and St Paul Pioneer Press 1961-08 to 1962-12 and the Sentinel microfilm at MNHS or the Minnesota State Archives
Target,stage1,U.019 no contemporaneous periodical mention of Target or of the Goodfellow and Dey names,only one periodical leg is held and it is an advertising gather,High,Chain Store Age April 1963 greps Target 0 Goodfellow 0 Minnesota 0 Hudson 3 Dayton 2,High,U.032 HathiTrust and Google Books task set plus U.034 a second carrier
Target,stage1,U.020 why GEISSE leaves the officer pages after FY1967,company print records offices and never reasons,High,three GEISSE hits FY1965 FY1966 FY1967 and zero after against eighteen DOUGLAS J. DAYTON hits,High,U.030 PDF officer pages and U.031 the Geisse obituary
Target,stage1,U.021 Target-unit revenue for 1962-1966 1968 and 1970-1972,reports printed the group and the company and named Target dollars only for 1967,High,86901007 for 1967 (B1S03) and the 44/100 percent rate pair (B1S01),Medium,U.030 U.032 U.035
Target,stage1,U.022 numeric columns of the Five Year Comparisons blocks in FY1969 FY1970 FY1971,OCR dropped the figures leaving row labels,Medium,FY1973's equivalent row survives intact and foots in all five columns,Medium,U.030 re-OCR the PDF legs or obtain a ProQuest copy
Target,stage1,U.023 the FY1970 layer byte count disagreed between the probe table and the disk,transcription error in the probe table,Low,disk and sidecar both 53023 B,High,none needed - correct at merge and log the count
Target,stage1,U.024 no document before FY1965 exists in the held item,archive catalogue floor,High,item metadata listing 61 layers running 1965 to 2024,High,U.032 HathiTrust for Dayton Company reports FY1955-FY1964 and U.034 an independently digitised carrier
Target,stage1,U.025 whether any predecessor entity ever registered with the SEC,EDGAR name-to-CIK returned HTTP 503 on all four terms,High,one-entry formerNames array for CIK 27419 only,UNKNOWN,U.036 retry browse-edgar for dayton dry goods j.l. hudson dayton company dey brothers then sec_intake index on any CIK returned
Target,stage1,U.026 the company's own digital history pages in the web archive,Wayback CDX returned HTTP 503 twice,Medium,FY1999 and FY2000 print layers cover the same event,Medium,U.037 retry CDX once Internet Archive answers 200 and fetch snapshots with sidecars
Target,stage1,U.027 EDGAR full-text-search zeros for the four predecessor terms over 1940-1995,index floor - that corpus begins 2001,Medium,held zero-hit JSON responses,UNKNOWN,run an unrestricted control query with no date filter and record the hit counts as a floor test
Target,stage1,U.028 transport unverified on five layers (FY1966 FY1967 FY1971 FY1973 FY1974),verified TLS failed with CERTIFICATE_VERIFY_FAILED certificate has expired so --insecure was used,Medium,all five sidecars stamp transport UNVERIFIED TLS,High,U.037 repair or update the local CA store then re-fetch the same five URLs and re-stamp the sidecars
Target,stage1,U.029 intake tooling cannot enumerate or address this item's per-year layers,ia_text.py search returns field-less docs; ia_text.py fetch 404s on filenames containing spaces and would otherwise return the largest layer (2024) for --id 01-target-archive; sec_intake index discards formerNames; periodical_harvest has no target task set,High,enumeration by hand against the same endpoints with responses held under sources/ia_search/,High,hand the four defects to the orchestrator as TOOL DEFECTS not evidence and re-run intake once fixed
Target,stage1,U.030 the 17 PDF image legs of item 01-target-archive were never fetched,not attempted inside this pass's zero web budget,High,item metadata enumerates the PDFs for 1965-74 1976 1985-86 1990-91 1994,UNKNOWN,fetch per-year PDFs into sources/corporate_print_pdf/ with sidecars and re-OCR the roster five-year and officer pages; alternatively a ProQuest Historical Annual Reports copy
Target,stage1,U.031 no held independent primary for the founder conflict,both carriers are web leads,High,officer pages B1S01 B1S02 B1S03 which establish roles only,High,FETCH REQUEST to the orchestrator: 2013-07-06 Twin Cities or Pioneer Press Douglas Dayton obituary and a 1992-02 Geisse obituary into sources/documentary/ with sidecars
Target,stage1,U.032 book corpora never searched for the pre-1965 leg and for Target Stores Inc 1962-1966,periodical_harvest has no task set for this company and Google Books needs an absent API key,High,HathiTrust reaches 1950s-1960s print and is the route most likely to lift the tier from T2 to T1,UNKNOWN,add a target task set to tools/queries.json then run periodical_harvest with --use-curl for HathiTrust and GOOGLE_BOOKS_API_KEY for Google Books
Target,stage1,U.033 local newspaper back-files never searched,not attempted; Chronicling America has no Minnesota 1962 coverage for the window,High,trade press and company print only,UNKNOWN,Star Tribune and St Paul Pioneer Press 1961-08 to 1962-12 and the Sentinel microfilm at the Minnesota Historical Society or the Minnesota State Archives
Target,stage1,U.034 no second carrier for the same reporting years,all eleven layers are one uploader's item so every Stage-1 record is one lineage,High,IA collection fund-and-stock-reports may hold independently digitised Dayton reports,UNKNOWN,advancedsearch on collection fund-and-stock-reports for dayton company per-year items called directly because ia_text.py search is broken on this build
Target,stage1,U.035 XBRL and the FY1993 10-K never fetched,sec_intake facts never invoked and the first 10-K never retrieved,Medium,accession 0000950131-94-000539 is enumerated in the held index,UNKNOWN,run sec_intake facts for TGT and fetch accession 0000950131-94-000539 for its five-year selected data reaching back to 1989
Target,stage1,U.036 predecessor-CIK index routes never run,blocked by the 503s recorded at U.025,High,none - the question is open,UNKNOWN,browse-edgar action getcompany for dayton dry goods j.l. hudson dayton company dey brothers then sec_intake index --cik n --from 1930-01-01 --to 1985-12-31
Target,stage1,U.037 the five unverified layers never re-verified under trusted transport,stale local CA store,Medium,readable bytes with UNVERIFIED TLS sidecars,High,upgrade certifi or use the documented --use-curl fallback then re-fetch the same five URLs and re-stamp before any of Q3-Q8 Q16-Q19 or section K.3 is cited at High
```
