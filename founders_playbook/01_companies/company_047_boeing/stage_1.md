# FORENSIC LONGITUDINAL DATASET — BOEING (company_047_boeing), STAGE 1

## MERGE RECORD (assembly, geometry decision, application, id map, validation/failures binding, anchor parity, five-family table, carry-forward)

Merged 2026-10-07 by `merge-boeing` from the single part `_parts/s1_p1.md` (author `s1-boeing-p1`, **44,732
words** as emitted, §A–§U complete, `## Untried` written, 24 claim records, anchors `U.001–U.017` 1:1 with 17
conflict rows, **211 register rows** across nine registers). **Section letters are the author's and were not
renumbered** (method §9.3 — numbering continues, it is never re-based): Header, Stage boundary, §A–§U, the
claim-record appendix and `## Untried` + `## FETCH REQUEST` appear below in the order and with the labels the
part gave them. Nothing in the narrative was rewritten, trimmed, re-tiered or merged away.
`_parts/s1_p1.md` stays **read-only** and is the emission of record; the merge appended to it a
`SUPERSEDED 2026-10-07` **footer** and edited nothing above it — the footer supersedes the **placement and
key-space** of the register emission (the 211 rows now live in the CSVs at this directory root; the
provisional `P1SRC01–P1SRC19` source keys are superseded there by the minted ids **S4510–S4528**), not one
word of the narrative, which required no correction. No `CORRECTIONS.md` was issued: the merge made no
retraction, re-dating, re-valuing or deletion — only a central re-key (map below) and the binding of the two
shared-schema registers (both documented here and in `03_quality_control/boeing_s1_merge.md`).

### Geometry decision — ONE volume, not split (recorded and reasoned)

The part measures **44,732 words**: above the §15.2 T2 density target of 22,000 words/stage, **below the
§9.2 hard cap of 60,000 words/file**. The author's NOTES §4 offered a split at a section boundary
(Header+boundary+A–O / P–U+claim records / registers). **Decision: do not split.** Three reasons, stated so
a later reader is not tempted to "fix" the overage by cutting evidence (method §9.6 — the limit governs file
geometry, never research depth): (1) after the merge the nine fenced register blocks (211 rows) are **applied
to the CSVs and moved out of the prose**, so `stage_1.md` itself is materially smaller than the part; the
narrative volume stays under the 60,000-word hard cap with margin. (2) The whole T2 deliverable (§A–§U, claim
records, full registers) fits one file; there is no §9.2 defect to repair. (3) A split only at a section
boundary, never renumbered, buys nothing here and would add a volume-map to maintain without removing the
advisory. **The overage is logged as ADVISORY, nothing was trimmed.** The tier is **T2 core**: `gates.py
--tier auto` mis-stamps **T3** because its reader counts tier mentions rather than reading the verdict line
(a table-row verdict the auto-reader cannot see — the standing hazard named in `_AUTHOR_WAVE_PLAN.md`), so
the budget check was run with **`--tier core` passed explicitly**, and that is recorded here rather than the
prose being edited to satisfy the tool.

### What was moved out of the prose

The part's nine fenced `csv` register blocks (211 rows) are register data, not narrative (method §13): they
were **applied** to the nine CSVs at this directory root, and the `## Register rows for merge` heading below
now points at that application instead of repeating the blocks. Their verbatim text survives at
`_parts/s1_p1.md` l.1401–l.1698 (read-only). Claim records **are** narrative: all 24 of them
(P1A01…P1S02) appear below, unchanged.

### Register application (requested ↔ applied, measured on the bytes written)

| register | rows requested | rows applied | cols | key / integrity check |
|---|---|---|---|---|
| `sources.csv` | 19 | **19** | 18 | keys S4510–S4528, 0 duplicates |
| `quantitative.csv` | 75 | **75** | 12 | 0 duplicate row texts |
| `timeline.csv` | 42 | **42** | 11 | 0 duplicate row texts |
| `conflicts.csv` | 17 | **17** | 15 | keys U.001–U.017, 0 duplicates |
| `data_gaps.csv` | 18 | **18** | 8 | 0 duplicate row texts |
| `decisions.csv` | 11 | **11** | 15 | 0 duplicate row texts |
| `validation.csv` | 13 | **13** | 11 | 0 duplicate row texts (bound by content, see below) |
| `failures.csv` | 9 | **9** | 11 | 0 duplicate row texts (bound by content, see below) |
| `channels.csv` | 7 | **7** | 11 | 0 duplicate row texts |
| **TOTAL** | **211** | **211** | — | **0 unapplied, 0 added by the merge** |

Every header is **byte-identical** to the corresponding Amazon conformant register header (compared by string
equality against `company_001_amazon/<name>`); `stage` is the literal `stage1` on all 211 rows (never a bare
number, and the post-boundary `(PB)` rows keep `stage1` with the `(PB)` flag in their `notes` cell only, so
they are not pulled into the stage's own evidence series); and the width and duplicate-key pass was run
**across all nine blocks in one operation**, not per block: **0** rows off-header-width, **0** duplicate keys
in the two keyed registers, **0** `source_id` tokens that fail to resolve against `sources.csv` across
timeline/decisions/validation/failures/channels. Rows are written at the header's width with every field that
can contain a comma quoted, so no register can be shifted by one field.

### Provisional-to-global id map (the only place `P1SRC01–P1SRC19` bind; minted centrally)

Minted with `python tools/id_mint.py --count 19 --company company_047_boeing --claim --agent merge-boeing` →
**S4510 … S4528** (contiguous, 19 ids). The tool allocated **above the highest live id** (PepsiCo held the top
issued block `S4479`–`S4494`; registry claims extended to `S4509`), so no gap is re-entered and no number
another company holds is reused. The registry's known collision — `S4222–S4229` cited by both
`company_011_microsoft` and `company_042_target` — sits **below** this range and was not touched; Cigna's block
(`S4407`–`S4422`) is also below it. Live register rows carry the minted ids; the narrative below keeps the author's local `P1SRCnn`
tags as reading keys and is bound by this table. Only `P1SRCnn` (source-register keys) was re-keyed;
`P1QTNnn / P1TMLnn / P1GAPnn / P1DECnn / P1VALnn / P1FAInn / P1CHNnn` and the claim-record tags are
dossier-local row ids with no global counterpart and are preserved verbatim.

| local | minted | carrier |
|---|---|---|
| P1SRC01 | **S4510** | FY1934 stockholder report (12,430 B) — the only `since 1916` in the corpus; one corporate lineage |
| P1SRC02 | **S4511** | FY1935 report (16,394 B) — sole `July 22`/`anniversary`; PROGRESS chronology; the non-footing 1935 share pair (U.007) |
| P1SRC03 | **S4512** | FY1937 report (20,844 B) — column-interleaved; fragments only; **no quantitative row emitted** (see withheld rows) |
| P1SRC04 | **S4513** | FY1938 report (23,332 B) — the tested mis-quotation of FY1934 (U.008); T.W.A. termination |
| P1SRC05 | **S4514** | FY1939 report (25,088 B) — management-change date; quotes a 1939-11-24 letter that is NOT held |
| P1SRC06 | **S4515** | FY1940 report + notice + proxy + separate C$ Canadian statements (33,308 B) — boundary year |
| P1SRC07 | **S4516** | `boeing1934a` — undated **Hamilton Metalplane advertisement**, not a report (U.014; report count = six, not seven) |
| P1SRC08 | **S4517** | *Boeing Air Transport v. Farley*, D.C. Cir. 1934 record (625,596 B) — A.M. 18 bid/award; three-way date conflict (U.004) |
| P1SRC09 | **S4518** | *Edelman v. Boeing Air Transport* record (493,539 B) — a **Wyoming gasoline-tax** suit; federal mail clerk's testimony (U.016) |
| P1SRC10 | **S4519** | Senate munitions-industry print 1934 (4,594,867 B) — negative control, `Boeing` 0; corpus's only `antitrust` occurrence |
| P1SRC11 | **S4520** | *Aviation* issue 1916-08-01 (149,954 B) — negative control, `Boeing` 0 in 149,286 chars |
| P1SRC12 | **S4521** | Internet Archive item file list (46 per-year layers) — carrier for the Stage-1 end boundary; a FILE census ≠ DOCUMENT census |
| P1SRC13 | **S4522** | FY1945 report (46,004 B) — `(PB)`; still "Boeing Airplane Company", no origin recital; bounds the renaming below |
| P1SRC14 | **S4523** | FY1976 item-level layer (99,175 B) — `(PB)`; prints "The Boeing Company"; sidecar url/filename mismatch (merge hazard) |
| P1SRC15 | **S4524** | 12 × NASA NTRS layers (2,553,319 B) — out of window; cited only for the modern name's third-party printings |
| P1SRC16 | **S4525** | EDGAR SGML `FORMER COMPANY` header, `DATE OF NAME CHANGE: 19730725` — 26 mechanical printings of ONE registry record (U.009) |
| P1SRC17 | **S4526** | Form S-4 (1996-10-29) + S-4/A (1998-05-13) — `(PB)` registrant's own "originally incorporated in Washington in 1916 … reincorporated in Delaware in 1934" |
| P1SRC18 | **S4527** | Held EDGAR set (33 .txt, 7,170,562 B) + submissions index (4,026 rows) — perimeter carrier; `_MANIFEST.csv` regression reported not fixed |
| P1SRC19 | **S4528** | Probe + harvester dossiers (`A_chronology_feasibility.md`, `A4_harvest_mine.md`) — a **carrier of commands/counts, not a witness** |

**Folds applied: none.** No row was folded into another, no register was deduplicated on similarity, and no
`P1SRC` lineage was minted twice. Per method §3: the seven corporate-print layers (S4510–S4515, S4522, S4523)
are **one institution's own reports — one lineage, counted once for corroboration**; S4525 is **one registry
record re-printed 26 times, not 26 corroborations**; S4526 is **two registration lineages, one copied
sentence, not two**; the md5 census over the 25 non-SEC files returned **25 distinct digests**, so no two
shelves hold one document. 19 rows → 19 contiguous ids.

### `validation.csv` ↔ `failures.csv` binding (adjudicated by content; the census cannot separate them)

The two registers **share the same 11-column schema** (`signal_or_failure` in both), so `merge_census.py`
reports them as `AMBIGUOUS:validation.csv,failures.csv` and cannot bind them — this is the standing hazard in
`_AUTHOR_WAVE_PLAN.md`. They were adjudicated **by row content**, and the reasoning is **printed in-cell**
(appended to each row's `notes`): the 13 rows of the part's `### validation.csv` block are **positive
validation signals** (each `notes` cell carries a `P1VALnn` tag and describes an award, a certificate, a
repaid facility, backlog inflection or the first profit); the 9 rows of the `### failures.csv` block are
**incurred losses or attestation limits** (each carries a `P1FAInn` tag and describes a destroyed prototype,
a dormant subsidiary, a booked overrun, a terminated contract, a capital write-off, a wage shock or an audit
scope limit). The binding is deterministic on the `P1VALnn`/`P1FAInn` prefix and confirmed by reading the
`what_it_demonstrated`/`what_it_did_not_demonstrate` cells; the two sets are disjoint and complete (13 + 9 =
the 22 the author emitted). Full reasoning and the per-row list are in `03_quality_control/boeing_s1_merge.md`.

### Anchor ↔ conflict parity (proven by re-running the census, not asserted)

The part declares `<!-- ANCHORS: U.001-U.017 -->` and writes §U.001–§U.017 below. After applying the blocks,
`python tools/merge_census.py --company-dir <this dir> --verbose` reads `conflicts.csv | requested 17 |
present 17 | missing 0`: all seventeen declared anchors U.001–U.017 exist as register keys, 1:1 with the
seventeen `U.nn` sections in §U, with no eighteenth row and no unanchored row. The same run's `sources.csv`
line still lists the nineteen `P1SRC01–P1SRC19` tags as "missing keyed rows" — the expected residue of a
central mint (the minted ids S4510–S4528 are present; the local tags live only in the read-only part and in
the map above). The `validation.csv`/`failures.csv` pair remains `AMBIGUOUS` to the census by schema, not by
data.

### Five-family table (Stage 1, 1916-01-01 → 1940-12-31), inherited from the probe, tier NOT re-graded

| family | verdict for Stage 1 | what returns / why not |
|---|---|---|
| (a) EDGAR filings | **RETURNS NOTHING in-window; perimeter named** | earliest indexed filing 1994-03-15 `DEF 14A` (CIK 0000012927); **no S-1 exists** in 4,026 filings; the only origin voice is the 1996/1998 S-4 boilerplate `(PB)` |
| (b) web archives | **UNTRIED (now REACHABLE, still cannot bear on Stage 1)** | `tools/cdx_intake.py` exists since 2026-10-06, so the probe's "no script reaches CDX" is stale; the family floor is mid-1990s vs a 1916-1940 window (§14.6) — Stage-1-relevant regardless |
| (c) periodical / digitised government print | **RETURNS** (in-window, with two content-verified NULLs) | D.C. Cir. 1934 air-mail record + the 1933 Wyoming record carry Tier-1 federal/judicial text; *Aviation* 1916-08-01 (`Boeing` 0) and the Senate munitions volume (`Boeing` 0) are live negative controls |
| (d) digitised corporate print | **RETURNS** — the family that moved Boeing | FY1934–FY1940 audited stockholder reports, 137,518 B; **six** in-window company reports (the `1934a` layer is a Hamilton advertisement, not a report) |
| (e) auction / museum / manuscript | **UNTRIED, structurally** | no source-family in `queries.json`, no tool reaches a finding aid; the single route most likely to change the verdict (it is the only family that can carry an **instrument** rather than a recital) |

**Stage 1 = T2 core.** Two of five families return in-window Tier-1 text ((c) and (d)); one returns nothing
with a named perimeter ((a)); two are untried ((b), (e)). Families (b) and (e) are precisely the two that
could carry 1916-1925 documentary material, so the T2 grade is a floor on a live upgrade path, not a ceiling.
The tier is inherited unchanged from `research/A_chronology_feasibility.md`; this merge did not re-tier.

### The four items this merge carried because Boeing is the corpus's sharpest registrant-identity case

1. **Five namings, no held byte conjoining any two** (§B.3, §U.001): (i) FY1934 attaches "since 1916" to
   **Boeing Aircraft Company, a Washington corporation** owned 100% by the addressee; (ii) the **federal
   record** (S4517) calls the 1927 contracting party "**Boeing Airplane Company, Incorporated** … under the
   laws of **Washington**" — an in-window name collision, not a retrospective recital; (iii) FY1938 prints
   "organized in **August, 1934**"; (iv) the `1934a` layer is an **undated Hamilton Metalplane advertisement**,
   so "one item, one layer per year" is a **file census, not a document census**, and the count is **six
   audited reports, not seven**; (v) **Boeing Air Transport, Incorporated**, a third Washington corporation by
   1927-04-29. The author's refusal of the **1960 renaming** is kept as a Stage-1 non-fact (EDGAR prints a
   conformed-name change of 1973-07-25 for one registry record re-printed 26 times; no held byte prints 1960
   as a renaming act).
2. **The origin day is DERIVED and stated as such** (§B.1, §U.003, S4511): FY1935's "the twentieth anniversary
   of this subsidiary will occur July 22 of this year" → **1916-07-22** by subtraction (1936 − 20), Medium,
   one lineage. `July 22, 1916` occurs **0** times; **July 15 is unheld, not contradicted**. The A.M. 18 award
   date stays **three-valued inside one volume** (Jan 29 / "on or about Feb 1" / contract dated 1 Feb) at
   **U.004** — not reconciled.
3. **Withheld rows are evidence of damage, not laziness**: **all FY1937 figures and all FY1936 quantities**
   were withheld because the FY1937 layer is column-interleaved/unreadable and the FY1936 layer is **absent**
   from the archive item. They appear as `data_gaps.csv` rows **P1GAP16 / P1GAP05 / P1GAP08** and as
   `FETCH REQUEST #3` / `#4`, and were **never back-solved from neighbours**. `quantitative.csv` carries **0**
   FY1937 income/balance rows by design (see §P "Rows withheld").
4. **Antitrust motive is UNTRIED, not denied** (§C.1, §U.010): three printings say tax / simplification /
   industry trend, and "antitrust" has **0 Boeing-adjacent witnesses** (its single corpus occurrence is in the
   munitions volume where "Boeing" occurs 0 times). `mechanism UNKNOWN` is kept on the 1934–38 acts and on the
   §N "new management saved Boeing" coda.

### `gate_quotes` research-index gap (known limitation, carried not "fixed")

`gate_quotes` indexes only `sources/**`; a quotation of the author's own `research/*.md` dossiers can never
match, so this merge carries **one permanent false advisory** (the `_AUTHOR_WAVE_PLAN.md` "three corrections"
item 3), exactly as Cigna did. The volume quotes held `sources/` bytes for every load-bearing passage; any
research-dossier quotation is reported, not edited to silence the gate.

### Carry-forward

`## Untried` (11 items) and the **FETCH REQUEST #1–#5** routes are carried verbatim below. Register homes:
`data_gaps.csv` follow-up tasks carry FETCH REQUESTs **#2, #3, #4** explicitly; **#1** (family-(a) recital
completion) and **#5** (charter records — the only route to U.001–U.003 as acts) have **no dedicated
`data_gaps.csv` row** because the author emitted none; their homes are `## Untried` #9/#10 below and the
`residual_uncertainty` cells of `conflicts.csv` U.001–U.003, and they are named here rather than dropped.
Family states stay distinct in every file: **TRIED–ANSWERED (null)**, **TRIED–UNANSWERED** (tool/network
refused; remedy named), **UNTRIED** (never attempted, 0 web calls by the author). Words and rows are published
live in `_MANIFEST.md` (method §9.6), re-measured with `wc` after the last write of this operation.

---

# FORENSIC LONGITUDINAL DATASET — BOEING (company_047_boeing), STAGE 1

**Company:** The Boeing Company (EDGAR registrant `BOEING CO`, CIK 0000012927; tickers `BA`, `BA-PA`).
Stage-1 subject of narrative: **Boeing Airplane Company** and its operating subsidiaries as they appear in
the company's own stockholder print 1934-1940, plus the federal air-mail record 1927-1934. This dossier does
**not** treat the modern registrant and the 1916-attached corporation as one person (see §boundary, §U.001).

**File:** Stage 1, part 1 of 1 — Header, Stage boundary, sections **A–U**, claim records, register rows.
Owner `s1-boeing-p1` (`tools/scaffold.py claim`, 4 section slots). Written 2026-10-06/07 against the held
corpus as re-enumerated on this pass.

**Tier (inherited, not re-graded):** **T2 core** for Stage 1, per `research/A_chronology_feasibility.md`
("Verdict": two of five families return in-window Tier-1 text — (c) periodical/government print and
(d) digitised corporate print). §15.2 deliverable for T2: evidence-bound §A–§U, full registers, claim
records for load-bearing claims only, 22k words/stage cap. This pass does not re-tier and does not claim
T1: the third family that would move Boeing to T1 (e, auction/museum documentary) is still UNTRIED.

**Stage definition used:** from the earliest date any held document attaches to any Boeing-named legal
person, through the close of the last fiscal year for which the company's own audited stockholder report is
held — **1916 (as printed, day derived: see §U.003) → 1940-12-31**. It ends with a first audited profit, not
with a validated business, and the year after it the company stops publishing detail.

**Hindsight firewall:** Nothing here treats the 1941-1945 war production boom, the B-29/707/747 line, the
1997 McDonnell Douglas merger or today's registrant as evidence that a 1927 bid, a 1934 formation or a
1937-1940 development loss was rational, obviously profitable, or a step toward anything. The anti-
hagiography test was applied section by section: §D, §L and §M are written so that they still read as
plausible for a firm that had gone insolvent in 1941 — which on the held FY1939 numbers (deficit
$3,471,686.29 eliminated against paid-in capital on/around September 30, 1939) was the condition three
months before the 1940 recovery. Post-boundary documents (the FY1945 and FY1976 layers, the 1996/1998 SEC
recitals, EDGAR header fields) are used only where a Stage-1 section needs them and are marked **(PB)** and
`RETROSPECTIVE SOURCE` (§6) wherever used; they are not counted as in-window witnesses and not counted in
the tier.

**Confidence scale** (method §3): **High** — 2+ independent sources or a primary document. **Medium** — one
reliable source, or an approximate date corroborated later. **Low** — conflicting, vague, or
retrospective-only. **UNKNOWN** — not established. Repeated copies of one origin story are **one** source.

**ID scheme (all dossier-local, §13):** `P1<SEC><nn>` — `P1A01`… narrative claim records by section letter;
`P1QTNnn` quantitative rows; `P1TMLnn` timeline rows; `P1SRCnn` sources rows; `P1CNFnn` conflicts;
`P1GAPnn` data gaps; `P1DECnn` decisions; `P1VALnn` validation; `P1FAInn` failures; `P1CHNnn` channels.
§U conflict anchors are `U.001`…`U.017` and are declared below. `source_id` cells are **provisional**
(`P1SRCnn` or blank): the merge mints global ids via `tools/id_mint.py`.

**Quotation convention:** passages are taken from the held Internet Archive OCR text layers and the held
EDGAR `.txt` files with (i) line breaks and column reassembly normalised, (ii) the OCR soft-hyphen join
character `¬` closed up, (iii) the OCR quote glyphs `\u2500`/`` rendered as `'` or `"`. Anything reassembled
across interleaved columns — which is unavoidable in `boeing1937_djvu.txt` — is flagged **COLUMN-REASSEMBLED**
at the point of use. Line numbers are locators only (§14.12); addresses are the stable label
(`FY1934 §"To the Stockholders" ¶2`, `dc_circ Bill ¶7`, `FY1940 Note 3`, `U.004`).

**Measured corpus this pass (re-enumerated; §14 rule 11):** 25 held text files — 7
`sources/corporate_print/*.txt` (137,518 B), 18 `sources/periodicals/*.txt` (6,845,616 B), 33
`sources/sec/*.txt` (7,170,562 B); md5 census over the 25 non-SEC text files returned **25 distinct
digests — no byte-identical duplicates**, so no two shelves hold one document. Post-probe arrivals not
examined by the probe and accounted for here: the FY1945 corporate-print layer (46,004 B, `…__boeing1945_
djvu.txt`, fetched 2026-09-29T18:39:57Z), 12 `NASA_NTRS_Archive_*` layers (fetched 2026-09-30/2026-10-06),
`sources/harvest_mine/_index.json` and `research/A4_harvest_mine.md`. The 12 NASA layers are all out of
window and are cited only as carriers of the modern name (§U.016).

<!-- ANCHORS: U.001-U.017 -->

STATUS: WRITTEN

---

## STAGE BOUNDARY JUSTIFICATION

| Stage | Start | End | Why This Boundary (carrier named) | Confidence |
|---|---|---|---|---|
| **1** (measured) | 1916 — printed only as a year; day-month **derived** `1916-07-22` (see U.003) | **1940-12-31** | The end is the best kind of boundary this corpus can offer: a **held, audited fiscal cut**. `sources/corporate_print/boeing1940_djvu.txt` is the company's own report for the year ended December 31, 1940, signed by P. G. Johnson 1941-03-08, with Allen R. Smart & Co.'s report dated 1941-03-06, and it is the **last in-window layer of the IA item** `boeingairplanecompanyannualreports`, whose per-year file list runs 1934, 1934a, 1935, 1937-1978 (46 text layers, one per year; **no 1936**, extra parts 1934a and 1941a). The start is **not** measured from a held instrument: no document of any family printed 1916-1925 is held (families a/e unanswered-or-untried, c/d negative-tested), so the start stays a printed year attached to a **different legal person** than the report addressee. | High (end, and that the item has no in-window layer after 1940); **UNKNOWN (start as a date of an act)** |
| 1 — search bracket actually used | 1916-01-01 | 1940-12-31 | `tools/harvest_mine.py:71` `"boeing": ("1916-01-01", "1940-12-31")`, quoted by the probe. **This is a search setting, not evidence** (RD-112): the repo records no founding date for this company, and `00_universe/fortune_top_50_2026.csv` carries no founding-date column. Kept as the harvest perimeter; not adopted as the stage perimeter. | High (that it is a parameter) |
| **2** (alternative cut proposed, PROVISIONAL) | 1941-01-01 | **1978-12-31** | Cut on **measured corpus carriers**, not on company history: (i) the same IA item's per-year corporate print runs to 1978 and the per-file route used in the probe demonstrably works — the first company-issued layer fetched after the boundary, `boeing1945_djvu.txt`, landed at **46,004 B** on its own path; (ii) 1978 is where that print run stops. The probe's alternative Stage-2 span (1941-01-01 → 1993-12-31, PROVISIONAL, T3) is left standing as the repo state; **whichever span is used, §15.2/`RD-112` requires the tier to be re-measured against it** — my 1941→1978 span is a print-availability span, not a history span. | n/a — proposal |
| **3** (alternative, PROVISIONAL) | 1979-01-01 | 2026-09-01 | Opens where the corporate-print carrier runs out and EDGAR does **not** yet run (held SEC `.txt` earliest 1994-03-15, `DEF 14A`, accession `0000012927-94-000001`; latest held 2002). The probe's Stage-3 floor of 1994-03-15 is the measured EDGAR perimeter; 1979-1993 is a **print-and-filing gap**, not a quiet period. | n/a — proposal |

**What the Stage-1 boundary does NOT claim.**
(i) It does **not** claim 1916 is the registrant's birth. The held FY1934 report attaches "since 1916" to
"Boeing Aircraft Company, a Washington corporation" which the same page says is **100%-owned** by the
addressee, while saying of the addressee itself: "your company was formed for the purpose of acquiring
these assets upon the dissolution of United Aircraft & Transport Corporation" (U.001, U.002).
(ii) It does **not** claim the year-end 1940 is an operational break: the 1940 profit is disclosed on the
same page as an accounting change that created $163,000 of it, and 1941 begins with the company printing
"Federal Government regulations prohibit the publishing of further detailed information."
(iii) It does **not** claim the corpus is complete inside the window: the item has no 1936 layer, the probe
opened 3 of 47 in-window IA text items, and 333 SEC accessions were never enumerated (`--max-docs 40`).
(iv) It does **not** resolve which of the five held Boeing namings is the registrant's own legal ancestor
(§U.001, §B.3, §T).
(v) It does **not** carry the 1934-38 reorganisation's *motive* into the window as antitrust: "antitrust"
occurs 0 times adjacent to any Boeing naming in the 25 held text files, and the single occurrence anywhere
is in `munitionsindustr1114unit_djvu.txt`, a volume in which "Boeing" occurs 0 times (U.010).

STATUS: WRITTEN

---

## A. EXECUTIVE STATE SUMMARY

**State at 1940-12-31, as the company's own audited print states it.** Boeing Airplane Company was a
listed, Seattle-headed corporation with one direct subsidiary, Boeing Aircraft Company (Seattle), which in
turn owned Boeing Aircraft of Canada Limited (Vancouver, B.C.); the Wichita operation was no longer a
subsidiary but a **division** of the parent, "Stearman Aircraft Division", the properties of The Stearman
Aircraft Company having been taken over in 1938 (FY1938; FY1939 prints the three plant locations as
Boeing Aircraft Company — Seattle, Washington; Boeing Airplane Company, Stearman Division — Wichita,
Kansas; Boeing Aircraft of Canada Limited — Vancouver, B. C.). Audited, domestic-only (the Canadian
subsidiary was excluded from consolidation in 1940 "due to exchange restrictions"): gross sales
$19,390,718.32; net profit for the year $374,655.29 after $188,811.53 of federal and state income tax
provision; total assets $33,668,885.35; cash $11,330,223.92 plus a restricted $685,329.98 of unexpended
United States advance payments; capital stock 1,250,000 authorised at $5.00 par, **1,081,673¾ issued and
outstanding** plus **780¼ shares still to be issued upon presentation of United Aircraft & Transport
Corporation certificates for exchange**; paid-in surplus $4,507,270.96; accumulated **deficit**
$303,520.30 carried forward; unfilled U.S. orders $196,522,446, "an increase of $174,392,821 over unfilled
orders at the close of the year 1939"; employment 8,420 at Seattle (+2,449), 1,762 at Wichita (+1,258),
704 at Vancouver (+388), with "in excess of 20,000 employees in all divisions" anticipated at the 1941 peak.
**P1A01, P1A02, P1A03 — FACT (audited), confidence High, one lineage (FY1940).**

**The registrant's origin, stated as the split the bytes actually show.** Two in-window company documents
name the 1916 year, and both attach it to a **subsidiary**: FY1934 ("Boeing Aircraft Company, a Washington
corporation, has been engaged in the manufacture of aircraft since 1916 … Its plant is located at Seattle,
Washington") and FY1935, whose final picture page opens a company-authored model chronology at "THE FIRST
BOEING PLANE— A TWO-PLACE TRAINER SEAPLANE. 1916" and whose text says "**The twentieth anniversary of this
subsidiary will occur July 22 of this year**". The same FY1934 report says of the addressee that its profit
and loss account "dates from September 1, 1934" and that it "was formed for the purpose of acquiring these
assets upon the dissolution of United Aircraft & Transport Corporation"; FY1938 dates the addressee's
organisation to a month, "At the time the company was organized in August, 1934". So the held in-window
print supports **August/September 1934 as the reporting company's own formation** and **1916 as a
different corporation's standing**. **P1A04 — FACT of what the documents print; the identity question is
UNKNOWN (U.001, U.002, U.003).**

**Founder absent from the held governance.** "Westhoff" occurs **0** times in every held byte, "Pacific
Airplane"/"Pacific Aero" **0**, "B & W" **0**, "Montreal" **0**. W. E. Boeing appears in the corpus only in
the 1934 D.C. Circuit air-mail record — as **president of a different corporation**: "I, W. E. Boeing, as
President of Boeing Air Transport, Inc., a corporation, making this affidavit for and in behalf of said
corporation" and in four `By W. E. BOEING` signature blocks. He is named in **none** of the board or officer
lists of any of the seven held corporate-print layers; those name C. L. Egtvedt, G. W. Carr, C. N. Monteith,
H. E. Bowman, J. P. Murray, W. M. Allen, and after 1939 P. G. Johnson. **P1A05 — FACT (of absence) over
held bytes; NOT proof of absence of role in the world (§S).**

**What was still broken at the boundary.** The company's own print states it: a Clipper inventory reserve
of $640,000.00 and an estimate that "the Company may sustain a further loss subsequent to December 31,
1940, in the approximate amount of $500,000.00 in the further performance of the option contract";
$3,471,686.29 of accumulated deficit wiped against paid-in surplus at 1939-09-30; a live joint-and-several
guaranty of United Aircraft & Transport Corporation's liabilities, still being provided for six years later
at $81,500.00; a management body (Local Union No. 751 / IAM) whose wage terms had just added
"approximating eighteen per cent" to labour cost and were re-openable at July 1, 1941; and the Canadian
subsidiary's 6% cumulative preferred dividends in arrears C$231,730.00.

**Evidence class present in-window.** Tier-1: seven company-authored audited stockholder reports (FY1934,
1934a non-report brochure, 1935, 1937-1940) with two independent audit firms' reports (Allen R. Smart &
Co. for the domestic companies — Seattle in 1936 and 1941, Los Angeles in 1935 — and Riddell, Stead,
Graham & Hutchison for the Canadian subsidiary, Vancouver, 1941-02-14); a federal appellate record with a
notarised founder affidavit and a municipal airport lease; a Supreme Court record from Wyoming. Tier-3:
`sim_aviation-week-space-technology_1916-08-01_1_1` (149,954 B) and `munitionsindustr1114unit`
(4,594,867 B) — both **content-verified NULLs for this company** (Boeing ×0 in each; "August 1, 1916"
printed repeatedly in the first, "Senate" 68× / "aircraft" 16× in the second).

**Unknown at Stage 1, in the company's own words' silence:** the founding day, the founding instrument, the
original corporate name, the identity of any co-builder, the first flight, the first customer, the first
incorporated capital, the 1916-1925 accounts, the 1929 step-up into United Aircraft & Transport
Corporation as an act, the date of the name change to "The Boeing Company", and whether the 1934 reorganisation
was a reincorporation or a purchase.

STATUS: WRITTEN

---

## B. FOUNDER / COMPANY STATE

### B.1 The founder as the held bytes state him

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Name form in held bytes | "W. E. Boeing"; the corpus never prints "William E. Boeing" in full outside the D.C. record's signature/affidavit context | `dc_circ_1934_…_djvu.txt` affidavit + 4 signature blocks (case-insensitive `W. E. Boeing` = 1 in 25 held text files; the signature blocks render uppercase `W. E. BOEING`) | High (as printed) |
| Office held, dated in-window | President of **Boeing Air Transport, Inc.** — the affiant's own statement, on behalf of that corporation, as "Sub-Contractor" on the route named | dc_circ, Certificate of the Oath of Mail Contractor and Carriers required by law; signature block `BOEING AIR TRANSPORT, INC., By W. E. BOEING, President, Sub-Contractor` | High (that it was sworn); Medium (the date of the oath itself is OCR-destroyed: "Signed this  day of-, 19") |
| Office held by the reporting company | **Not printed in any of the seven held corporate-print layers as an office or directorship of Boeing Airplane Company or Boeing Aircraft Company (1934, 1935, 1937, 1938, 1939, 1940) or of the 1934a brochure** | Negative over `corporate_print/*.txt` board and officer lists; FY1934 lists Allen, Bowman, Carr, Egtvedt, Kirk, Monteith, Nelson, Schmitz and officers Egtvedt/Carr/Murray/Bowman; FY1940 proxy lists nine directors with share counts and none named Boeing | High (of absence in held bytes); **not** evidence of absence in the world (§S, P1GAP04) |
| Personal capital, personal finances, education, departure | **UNKNOWN.** No held in-window byte states any figure for him, any shareholding by him, or any transaction with him | Absence across all 25 non-SEC text files and the 33 held SEC files | High (that nothing is held); route in `## Untried` #2 (family e) |
| The 1916 anniversary as the company states it | "The twentieth anniversary of **this subsidiary** will occur July 22 of this year" — the report for FY1935, signed March 9, 1936, i.e. anniversary **1936-07-22**; 1936 − 20 = **1916-07-22** (DERIVED: `1936 − 20 = 1916`) | FY1935, §"Boeing Aircraft Company", first paragraph | High (that the sentence prints); **Medium** for the derived day (company self-narrative, one lineage, retrospective); the full string `July 22, 1916` occurs **0** times in the corpus |

### B.2 The reporting company's state, in-period

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Stated formation purpose and date | "your company was formed for the purpose of acquiring these assets upon the dissolution of United Aircraft & Transport Corporation"; account "dates from September 1, 1934"; net assets taken "at August 31, 1934"; FY1935 prints "**On August 31, 1934, the date of reorganization**"; FY1938 prints "At the time the company was organized in **August, 1934**" | FY1934 stockholder letter ¶1 + balance-sheet footnote **; FY1935 contingent-liability note; FY1938 §Sales Prospects | High (four printings, **one lineage**: the company's own reports — §3 caps this at one corporate record stated four times) |
| State of incorporation of the reporting company | **Not printed** in any of the seven in-window layers. A later registrant recital prints "reincorporated in Delaware in 1934" | FY1934-40 as held; `(PB)` SEC S-4 as filed 1996-10-29, Item 1 boilerplate, and S-4/A as filed 1998-05-13 | High (that in-window print is silent); Medium for the (PB) recital — 2 accessions, **one repeated boilerplate sentence, not two corroborations**; U.001 |
| Governance at the boundary | President and General Manager P. G. Johnson (compensation $20,000 "during the last fiscal year"); Chairman C. L. Egtvedt ($20,000); VPs J. Earl Schaefer, James P. Murray; Secretary-Treasurer Harold E. Bowman ($0 stock); aggregate remuneration of directors and officers **$92,355**; counsel Todd, Holman, Sprague & Allen paid **$18,000** (Company) and **$18,750** (Boeing Aircraft Company) | FY1940 Proxy Statement, solicited for the meeting of April 15, 1941 | High (filed/printed proxy, SEC-regulated disclosure) |
| Founder-name shareholding at the boundary | Directors' beneficial holdings printed: Johnson 2,500; Egtvedt 5,833; Allen 205; Bowman **0**; Corbet 100; Laudan 319; Minshall 25; Pigott 100; Schmitz 150 shares. **Sum 9,384 of 1,081,673½ shares issued = 0.87%** (DERIVED: `2500+5833+205+0+100+319+25+100+150 = 9,384`; `9,384 / 1,081,673.75 = 0.8676%`) | FY1940 Proxy Statement + FY1940 balance sheet caption | High (printed) / High (arithmetic, shown) |
| Officers' pay at the first in-window report | "The officers, numbering four, are not paid any salaries. They are all actively engaged in the management of the subsidiary Boeing Aircraft Company" | FY1934, ¶ preceding the sign-off | High — and it is **against interest** for a holding-company officer to print that he is unpaid, which is why the 1940 disclosure of paid subsidiary offices is a real change, not a continuity |
| Employees | 1940: Seattle 8,420; Wichita 1,762; Vancouver 704 (DERIVED total 10,886; implied 1939 close 5,971 / 504 / 316, DERIVED total 6,791 from the printed increases). 1934: **UNKNOWN**, no headcount printed | FY1940 §Personnel | High (1940); **UNKNOWN** (1934-1939 counts) — the increase figures are printed but the base-year totals are not, so every 1934-1939 headcount curve in the literature is non-primary by construction |
| Premises | Addressed in the 1934 report as an entity whose transfer agent and registrar are New York institutions (City Bank Farmers Trust Company; The National City Bank of New York) and whose general counsel is a Seattle firm; first printed street address of the Company: **200 West Michigan Street, Seattle, Washington** (1941 notice of annual meeting); plant land at Boeing Field "approximately twenty-eight acres" bought in 1935; Plant No. 2 "originally built in 1936 and 1937" | FY1934/FY1935 back matter; FY1940 notice + §Plant Facilities | High (as printed); the 1934-1936 *address* is UNKNOWN |
| The name "Boeing" in the company's own product speech | "its slogan — 'Boeing Builds Tomorrow's Airplanes Today'" (of the **subsidiary**, FY1935) | FY1935 §Boeing Aircraft Company ¶1 | High — and note the referent: the slogan is claimed for Boeing Aircraft Company, not for the registrant |

### B.3 The person-chain the held namings actually draw

Each act below is a person, and a name is not a person. Five distinct Boeing namings are printed in held
bytes; the corpus never prints a sentence that ties any two of them into one corporate history.

| # | Naming as printed | State / place as printed | Earliest held witness | What the held bytes DO prove | What they do NOT |
|---|---|---|---|---|---|
| 1 | **Boeing Aircraft Company** | "a Washington corporation"; "Its plant is located at Seattle, Washington" | FY1934 | That a Washington corporation by this name was 100% held in 1934 and that the company itself dated its aircraft manufacture from 1916 | Its formation date, its formation instrument, its original name, or that the registrant is it |
| 2 | **Boeing Airplane Company** (report addressee) | Seattle; New York transfer agent/registrar; state of incorporation never printed | FY1934 | That a corporation by this name was formed to acquire UATC assets in 1934 and issued 521,883 shares under the Plan of Reorganization approved 1934-06-20 | That it is the 1916 corporation re-named, re-incorporated, or a new person that bought assets — U.002 |
| 3 | **Boeing Airplane Company, Division of United Aircraft and Transport Corp.**, Milwaukee, Wisconsin | Milwaukee (Hamilton Metalplane brochure) | undated layer held as `boeing1934a_djvu.txt` | That the *name* "Boeing Airplane Company" was printed as a **division subordinate to UATC**, at Milwaukee, on a product brochure bound into the same IA item | The brochure's date (nothing printed); that this division and the 1934 company are the same person — U.001b, and see §T on item homogeneity |
| 4 | **Boeing Airplane Company, Incorporated, of Seattle, Washington, a corporation duly organized and existing under the laws of the State of Washington** | Seattle, Washington | dc_circ, Route-Certificate recital concerning the 1927 contract | That a federal record recited a **Washington** corporation of this name as contracting party with Edward Hubbard on the 1st day of February, 1927 | That that Washington corporation is #1 (called "Boeing Aircraft Company" by the FY1934 report) or #2 — U.001, the direct in-window name collision |
| 5 | **Boeing Air Transport, Incorporated** | "of Seattle, Washington" / "of Washington"; a corporation "duly organized and existing under the laws of the State of Washington" | dc_circ (recital placing it by 1927-04-29) | That a third Washington corporation existed by April 29, 1927 and took the AM-18 service as sub-contractor; that it was the appellant in the 1934 D.C. matter and a plaintiff in the Wyoming gasoline-tax record | Any relationship to #1/#2/#4 stated in the bytes; and its later fate is **not printed** in held bytes |
| — | **The Boeing Company** (modern) | Delaware; Seattle | EDGAR header field, `(PB)` | `FORMER CONFORMED NAME: BOEING AIRPLANE CO` with `DATE OF NAME CHANGE: 19730725`, printed in **26 of 33** held SEC `.txt` files | Any 1960 renaming: `1960` in the FY1976 layer refers only to the 727 programme start; the FY1945 layer still prints "Boeing Airplane Company" and contains **no** origin recital (`1916` ×0, `since 19` ×0, `incorporat*` ×0). U.009 |

**P1B01–P1B12.** Classes: FACT of what each document prints; the identity links are UNKNOWN, and the two
later recitals are `(PB)` / `RETROSPECTIVE SOURCE`.

STATUS: WRITTEN

---

## C. ORIGINAL PROBLEM

### C.1 The problem the company itself set, in-period

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Stated problem | That aircraft manufacture is only viable through repeated unamortised new-model spending: "the officers of your companies are convinced, based upon their many years of experience, that the manufacture of aircraft can be successfully carried on only by spending fairly substantial sums in the development of new models in those fields which hold forth promise of producing future business" | FY1934, stockholder letter ¶7 | High (printed, signed by C. L. Egtvedt, March 4, 1935); the **experience** claim is RESTATED self-assertion, undated and uncorroborated |
| Its 1938 restatement, and the quotation defect inside it | FY1938 quotes its own 1934 report: "The 1934 report stated, '. . . the officers ... are convinced ... that the manufacture of aircraft can be successfully carried on only by spending substantial sums in the development of new models . . .'" — against the held FY1934 bytes the quotation is **not verbatim**: "fairly substantial" has become "substantial", and "based upon their many years of experience" and the "in those fields which hold forth promise of producing future business" clause are dropped inside ellipses | FY1938 §Sales Prospects vs FY1934 ¶7 (both held) | High (both printings are held, so the discrepancy is measured not inferred). **U.008** — a within-lineage ellipsis-quotation that quietly upgrades its own earlier hedged claim |
| Mechanism the company names for the 1934-38 structural acts | Tax and administrative simplification, and an industry trend — **not** antitrust and **not** regulation: FY1934 "In order to simplify management and taxation problems"; FY1937 (**COLUMN-REASSEMBLED**) "in line with the current trend toward the elimination of holding companies and the simplification of corporate structures"; FY1935 "Such a step will result in some saving in taxes. However, this consolidation will not result in a saving of management costs, as the officers … have served without compensation" | FY1934 ¶6, FY1935 ¶ preceding the loss discussion, FY1937 col. right, FY1938 | High (printed) / the *sufficiency* of that motive is UNKNOWN — "holding compan*" occurs exactly **1** time in the 25 held text files and "antitrust" **0** times adjacent to any Boeing naming. U.010 |
| The problem as a customer problem | Not stated. No held in-window byte identifies a first customer, a first order, or a demand hypothesis in the founder's words. The nearest in-window customer-side statement is a **product-catalogue** claim in the 1940 report: the three military types "available for the program of national defense being undertaken by our government" (FY1938) and Pan American's option exercise (FY1939/40) | FY1938 §Sales Prospects; FY1939 §Unfilled Orders | High (printed); FOUNDER-STATEMENT class: absent entirely |
| Facts knowable in-period about the market the firm entered | The federal air-mail contract system, priced per pound and awarded on competitive bid, is quantified **inside this corpus**: the four bids on Route A.M. 18 opened January 15, 1927 and the awarded rate $1.50 per pound for the first thousand miles and 15 cents per pound for each additional 100 miles; and by the early 1930s the same record reproduces a Post Office rate of "nine cents per pound" on a United Aircraft-controlled route | dc_circ Bill ¶6, ¶7; dc_circ brief passage re Varney / A.M. 32 | High (federal record, third-party paper); Medium for reading it as "the market" — it is one route |

### C.2 The genealogy of the "since 1916" line — this replaces the legend

The folk chronology (a 1916 certificate, a co-builder, an initial capital figure, a first flight) has **no
held witness at all**. What the corpus holds instead is one company-authored sentence family.

| Rung | What exists in held bytes | Document date | Class / strength | Conflicts |
|---|---|---|---|---|
| 1 — 1916 instrument | **Nothing found.** No certificate, articles, charter, deed, ledger, letter, logbook or sale record of 1916-1925 in any family; `1916` occurs 1 time in each of FY1934 and FY1935 and 1 time in dc_circ (where it is *Hulton v. Hulton*, (1916) 2 K.B. 642 — a citation decoy), 40 times in the 1916 *Aviation* issue's date strings and 107 times in a munitions volume containing 0 occurrences of "Boeing" | — | UNKNOWN; the route that could name it is `## Untried` #2 (family e) and #6 (44 unopened IA items) | U.003, U.011 |
| 2 — 1916 self-claim | FY1934 L157-158 and FY1935 L802, both inside **one lineage** (the company's own reports, two document years, one corporate record) | 1935-03-04 / 1936-03-09 | RESTATED, company self-narrative, retrospective at ~19-20 years' remove; corroboration = **1**, not 2 | U.001, C-2 in the probe |
| 3 — day-month | FY1935's anniversary sentence, year derived by subtraction | 1936-03-09 | DERIVED arithmetic shown; Medium | U.003 |
| 4 — third-party witness to the *company's standing*, not to 1916 | The 1927 award and operating record: a competitive federal contract, four named bidders, a $500,000 performance bond, service commenced July 1, 1927, and a **federal mail-transfer clerk's** sworn testimony that he delivers "the mail to the employee of the Boeing Company" at Cheyenne | 1927 → 1931-34 record | FACT (federal and municipal paper, independent of the company's print); this is the strongest load-bearing fact the corpus supports and it is **not** self-narrative | U.004, U.005, U.016 |
| 5 — later registrant recital | "Boeing was originally incorporated in Washington in 1916 and was reincorporated in Delaware in 1934" | 1996-10-29 and 1998-05-13, `(PB)` | RETROSPECTIVE INTERPRETATION by the issuer about its own origins, 62 and 64 years after the printed year; retained only because §U.001 requires both sides | U.001 |

**Problem vs narrative.** The documented Stage-1 problem is narrow and industrial: whether a company whose
own capital came out of another corporation's dissolution could keep winning per-pound federal contracts
and absorb the development cost of aircraft large enough to need new factories. Every element of the famous
origin story that is *not* in that sentence set is recorded here as UNKNOWN rather than as a weaker version
of the claim. **INFERENCE, held narrowly:** the FY1934 report's decision to state "since 1916" **inside the
first report of the newly formed holding company**, immediately after stating that it was formed to acquire
assets, is best read as an act of reassurance to shareholders of a company with no operating history of its
own — mechanism stated, alternative explanation (accounting necessity: the acquired asset values had to be
described) available, confidence Low, and no hindsight used.

STATUS: WRITTEN

---

## D. FIRST EXPERIMENT

**What the corpus allows.** No held in-window document describes a first flight, a first sale, a first
customer or a first built machine. `## Untried` #2 (auction/museum/manuscript) is the route that could, and
until it is run this section is written around the earliest experiment the corpus *does* witness: a
**priced competitive bid for a federal air-mail contract and the operation of that route**.

### D.1 Route A.M. 18: bid, award, bond, commencement (1926-11-15 → 1927-07-01)

| Variable | Value | Source | Confidence |
|---|---|---|---|
| What was tested | Whether an aircraft operator could offer to carry the mail between Chicago and San Francisco, by designated points, at a stated price per pound, against three named rivals, and then perform | dc_circ, Bill of Complaint ¶¶6-8 and the Route-Certificate record (Exhibit C family) | High (federal record) |
| Advertisement | "Bids for this route were requested by public advertisement dated November 15, 1926." | dc_circ, court's statement of facts for Route AM-18 (record p. 46 region) | High |
| Bids opened | January 15, 1927, in accordance with Section 425 of Title 39 U.S.C. Bidders printed: "(a) **Boeing Airplane Company and Edward Hubbard**, Georgetown Station, Seattle, Washington, at the rate of $1.50 per pound for the first thousand miles and 15 cents per pound for each additional 100 miles; (b) **Western Air Express, Inc.**, at the rate of $2.24 per pound the first 1,000 miles, and 22.4 cents for each additional 100 miles; (c) **Stout Air Services, Inc.**, at the rate of $2.64 per pound the first 1,000 miles, and 26.4 cents for each additional 100 miles; (d) **Columbia Air Liners**, at the rate of $4.47 per pound." | dc_circ, Bill ¶6 | High (printed); Medium on the OCR-damaged digits ("15^", "e^ch", "pdr") — all four rates are legible and mutually ordered |
| DERIVED spread | Winner's first-thousand-mile rate vs best rival: `2.24 − 1.50 = $0.74 per pound`, i.e. the Boeing-Hubbard bid was **33.0% below** the next bid on the first 1,000 miles (`1.50 / 2.24 = 0.6696`). Against the weakest: `4.47 − 1.50 = $2.97`, a 2.98× multiple | same | High (arithmetic shown); ESTIMATE only as to what the spread meant competitively |
| Award | Two dates print, **inside one held volume**: the verified bill says "on or about **February 1, 1927**, the then Postmaster General … awarded the contract … to Boeing Airplane Company and Edward Hubbard as being the lowest qualified bidder tendering sufficient guarantees for faithful performance in accordance with the terms of the advertisement"; the route-certificate recital says the same parties "on the **1st day of February, 1927**, duly entered into a contract with the United States"; and the court's statement of facts says "The contract was awarded **under date of January 29, 1927**, to Boeing Airplane Company and Edward Hubbard, as the lowest responsible bidders" | dc_circ Bill ¶7; Exhibit route-certificate recital; court's facts (record p. 46 region) | High (all three strings are held); **Low** for the award day — U.004; wording difference "lowest qualified bidder" / "lowest responsible bidders" is U.005 |
| Guarantee | "The Boeing Airplane Company and Edward Hubbard duly filed a performance bond in the amount of **$500,0Q0** as required by Sections 426 and 427 of Title 39" — OCR renders the final digit; read with the same form held for a rival carrier, "PACIFIC AIR TRANSPORT, [seal.] By VERN C. GORST, President. By C. H. GREEN, Secretary. VERN C. GORST, [seal.] Surety." | dc_circ Bill ¶7; bond form in the same record | High (that a $500,000-class bond is printed and that the OCR digit is destroyed); Medium as to the exact figure |
| Sub-contracting (the operating act) | "Thereafter on April 29, 1927, and prior to the time for the commencement of the service on Route A. M. 18, which was to begin July 1, 1927, the said contract be[came]…" and "**The said contract was duly sublet to Boeing Air Transport, Inc.**" — a second corporation interposed between the bidder and the flying, existing by April 29, 1927 | dc_circ Bill ¶8; court's facts | High (printed) — this is the first dated appearance of a *third* Boeing-named person in the corpus (B.3 row 5) |
| Commencement | "Performance under the contract commenced July 1, 1927, and has continued to date." Each such contract "was for a term of four years from the [date]" | dc_circ, court's facts | High |
| Did it actually operate? Third-party test | Sworn testimony at the Wyoming trial, from a witness called for the plaintiff whose own words identify him: "I am Transfer Clerk on behalf of the United States Government at the air field at Cheyenne and know what mail is handled by plaintiff through that field." Cross-examination: "**I deliver the mail to the employee of the Boeing Company.**" He quantifies the traffic: the Rock Springs pouch "with its contents averages a pound and four ounces in weight. The pouch with its lock weighs thirteen ounces"; "runs from one letter to twelve by each plane. Twelve would be a very large amount." | `micro_IA40386008_0350_djvu.txt`, Statement of Evidence filed Oct. 14, 1931 under Federal Equity Rule 75(b), lodged with the Clerk Aug. 20, 1931 | High that the testimony is in the record; **the witness's surname is OCR-destroyed** ("Testimony of Huan CorrmMan") and is recorded as UNKNOWN, not guessed. A U.S. government employee describing an airline as the deliverer of the mail is the best independent performance evidence held |
| The same source shows how small "success" was | One to twelve letters per plane on the Rock Springs leg, a pouch averaging 1¼ lb | as above | High — and it is the antidote to reading the 1927 award as validation of a business |

### D.2 The 1934-1940 development cycle as a sequence of incurred experiments

The held corporate print describes six build-and-prove cycles inside the window, each with a named machine,
a stated test and a stated consequence. These are the company's own account of its experiments (FACT as to
what is printed; Medium as to the event, being single-carrier self-narrative).

| Date (as printed) | Experiment | What the company states happened | Source |
|---|---|---|---|
| 1934 (four months) | Post-formation survival of the acquired operating companies | Losses "due to unsettled conditions in the industry", "additional labor and material costs on contracts taken by the operating subsidiaries prior to the passage of the National Industrial Recovery Act", and development spending on new designs | FY1934 | High |
| 1935 (Aug competition) | **Model 299**, "four-engined, all metal, bombardment airplane", "designed, constructed, tested and delivered in less than one year"; flown Seattle→Dayton "an airline distance of 2,040 miles, in nine hours" | Destroyed: "After approximately two months of inspection and testing, the airplane was totally destroyed by an unfortunate accident just prior to the final flight test and evaluation for the competition. This eliminated the airplane from the competition…" → then "the award of an order for thirteen airplanes and spares" | FY1935 | High (printed); the cause of the accident is **not stated** — U/M section at §M |
| 1936-1938 | **Model 314 "Clipper"** flying boat, six built in 1938; first flight "early in the summer" 1938; "lengthy and comprehensive tests by the company and by officials of the **Civil Aeronautics Authority**"; then "the Civil Aeronautics Authority issued an Approved Type Certificate for the Clippers" | Certification gate cleared; 4 delivered by 1939-01-01, 2 more scheduled before July 1; **cost overrun** booked (see §K, §M) | FY1938 | High |
| 1938-1940 | **Model 307 "Stratoliner"**, first of ten flew "just prior to the close of 1938"; cabin supercharging/heating/ventilating installed for "high altitude and Civil Aeronautics Authority tests"; by FY1939 under CAA test "for a period of more than three months", "A temporary certificate of air worthiness has been granted" | Deliveries to Pan American and Transcontinental & Western Air expected before 1940-07-01; final certificate pending review of engineering data in Washington, D.C. | FY1938, FY1939 | High |
| 1938-1939 | **Stearman attack-bomber**, entered "in a competition scheduled to be held in March, 1939"; "The airplane was substantially complete at December 31" | The company states in the same breath that "the sales prospects of which cannot yet be evaluated" | FY1938 | High (printed); outcome UNKNOWN — the 1936 and (legible) 1939 competition results are not printed |
| 1940 | **Great Britain twin-engine bomber** contract; **Emergency Plant Facilities** contracts with the United States (Oct 1940) | "a construction contract was let on May 24, 1940, for 667,000 square feet gross additional factory space"; the Government "agrees to reimburse the companies for the cost of the facilities in sixty equal monthly installments" | FY1940 | High |

**Assessment (D.3).** The 1927 experiment is the only Stage-1 event witnessed by paper that the company did
not write, and it establishes four things no later self-narrative can: that a named pair of bidders — a
corporation and an individual, Edward Hubbard — won a federal route on price against three named rivals;
that a performance bond was posted; that a separate operating corporation was interposed before service
began; and that a federal mail clerk handled the traffic. It establishes nothing about scale, cost,
durability or profit, and the same record shows the mail volume on one leg running one to twelve letters per
flight. The 1935-1940 experiments are, by contrast, all self-narrated, but they are audited-adjacent: the
failures they describe are the same items the accountants priced (the $488,068.14 and $640,000.00 Clipper
provisions, the $368,580.58 Stratoliner cost increase), which is why §M can be written from them. Mechanism
for the 1927 win is **UNKNOWN** from held bytes — the record prices the bid and names the bond, and does not
say why a manufacturer and a man were the lowest qualified bidders.

STATUS: WRITTEN

---

## E. PRODUCT RECONSTRUCTION

**Frame note (§7).** Amazon-style product reconstruction does not apply: this is a **certification-gated
capital-goods manufacturer**, so the artefacts are aircraft types, the analogue of a release is an Approved
Type Certificate, the analogue of a specification sheet is the Department of Commerce type-certificate
specification table, and the analogue of a roadmap is the company's own picture-page chronology. The
sections below are the adapted equivalents, and the standard frame is abandoned only where the bytes force it.

### E.1 The company's own model chronology (FY1935, final page, headed "PROGRESS")

Rungs whose year is unambiguously printed in the held layer, in the order printed:

| Year as printed | Machine, as captioned | Note |
|---|---|---|
| **1916** | "THE FIRST BOEING PLANE— A TWO-PLACE TRAINER SEAPLANE." | The only 1916 object-naming in held bytes; ~19 years after the fact, in a picture caption; the company's own 1935 claim about 1916, **not** an experiment account |
| 1921-22 | "MB-3A—ARMY PURSUIT PLANE." | |
| 1926-27 | "FB-5—CARRIER-TYPE NAVY FIGHTER." | |
| 1927-28 | "F3B-1—NAVY CARRIER FIGHTER, WITH AIR-COOLED ENGINE." | |
| 1929 | "40-B4—FOUR-PASSENGER MAIL PLANE." | The year 1929 is printed against a four-passenger mail plane, and 1929 is also the year this corpus cannot date for the United Aircraft & Transport step (§N, U.010) |
| 1933-35 | "2 81 —P-2 6-A—SINGLE SEATER ALL-METAL FIGHTER." and "247-I)—HIGH-SPEED ALL-METAL TWIN-ENGINE COMMERCIAL TRANSPORT." | Designations themselves OCR-damaged (`2 81`, `247-I)`) |

Rungs whose year is **not** legible and are therefore **not quotable**: the flying-boat entry ("BOEING FLYING
BOAT OPERATED / IN THE FIRST U. S. CONTRACT / AIR MAIL SERVICE." with `1 Q 1 Q`), the 80-A tri-motor
("`80-A—TRI-MOTORED 199 9 If)`", "PIONEER PULLMAN OF A… THE AIR"), the Army P12-C / Navy F4B-2 pairing
(`1 9 ^ 0— ^ 1`), the Monomail with retractable landing gear (`i Q 1 1 XJ`), the B-9A twin bomber
(`1 9 } 1 1 9`), and the 299 entry ("299—FOUR-ENGINED BOEING BOMBER, THIRTEEN OF WHICH ARE NOW UNDER
CONSTRUCTION." with `i g T r`). Caption↔year pairing across the page is an **OCR reading-order inference**;
the probe warned this and the warning is kept. **U.011** records the counting/measurement discipline.

**The caption↔document trap.** The flying-boat caption claims operation "IN THE FIRST U. S. CONTRACT AIR
MAIL SERVICE". The held federal record places the company's first contract operation on **July 1, 1927**
under Route A.M. 18, awarded in Jan/Feb 1927 — and the same record lists earlier carriers on other routes
(A.M. 3 National Air Transport, A.M. 4 Western Air Express, A.M. 5 Boeing Air Transport, A.M. 8 Pacific Air
Transport). Nothing in the held bytes establishes that the aircraft in the 1935 picture was the aircraft of
the "first" contract service, and the word "first" is used in a superlative register typical of a
commemorative page. Class: **RETROSPECTIVE INTERPRETATION**; do not use as an operational datum.

### E.2 Products with legible in-window specification or contract print

| Product | What is printed about it | Source | Note on identity |
|---|---|---|---|
| Hamilton Metalplane **H-15** ("Wasp" engined) and **H-47** ("Hornet" engined) landplanes; "Manufactured under Dept. of Commerce Approved Type Certificate"; H-15: Cabin Monoplane, eight seats, span 54'5", wing area 387 sq ft, length 34'8", empty 3,312 lb, useful load 2,408 lb, gross 5,750 lb, high speed 135 MPH, cruise 115, landing 50, climb 950 FPM, fuel 110 gal, range 675 mi, 21 gal/hour, single-wheel control; H-47: gross 5,750 lb, high speed 145, cruise 125, landing 55, fuel 140 gal, range 600 mi, 24 gal/hour | `boeing1934a_djvu.txt` (undated brochure; footer reads "DIVISION / BOEING AIRPLANE COMPANY / Division of United Aircraft and Transport Corp. / Milwaukee, Wisconsin") | **Not a Boeing product** and **not a report**: a Hamilton Metalplane advertisement bound into the annual-report item. Internal inconsistencies: the H-15's specification block is headed "Specifications for H-45"; the cabin text offers "Six passengers with pilot and navigator" against "No. of seats—Eight". See §T item-homogeneity defect and U.014 |
| **Model 299** four-engine all-metal bombardment airplane | "designed, constructed, tested and delivered in less than one year"; Seattle→Dayton non-stop 2,040 miles in nine hours; destroyed before final evaluation; "an order for thirteen airplanes and spares" | FY1935 | Type name not printed (the YB-17 designation is absent from held bytes) |
| **Model 314 "Clipper"** | "the largest commercial airplane in the world today, designed for transoceanic passenger, mail and express service"; six built 1938, CAA type certificate, 4 delivered by 1939-01-01 + 2 before July 1; six more under option, ordered 1939 by Pan American for 1941 delivery; 1940 inventory provision $640,000.00 and estimated further loss ≈$500,000 | FY1938, FY1939, FY1940 | Prices "substantially in excess" on the option six vs the six delivered in 1939 (FY1939) |
| **Model 307 "Stratoliner"** | "the first commercial airplane able to offer the comfort of normal atmosphere to passengers when flying at altitude"; ten under construction 1938; first flight end-1938; 1939 cost increase $368,580.58 attributed to "modifications in these aircraft as a result of extensive flight tests"; undelivered units for Pan American and T.W.A.; eight in the 1939 backlog (3 Pan Am, 5 TWA) | FY1938, FY1939 | The T.W.A. contract was **terminated** in 1938 and re-negotiated; U.017 class material at §M |
| **Flying Fortress** (four-engine bombardment) | 39 delivered/under contract 1938; two USAAC contracts printed with values: **$9,928,895 entered into in August of 1937** and **$8,426,190 entered into in September, 1939**; ~75% of the first contract delivered between 1939-09 and 1940-03-01; Wichita began making parts of it in 1940 | FY1938, FY1939, FY1940 | The word "Fortress" is in the company's own print from 1938 |
| **Stearman primary trainer** | "the standard primary training plane for the U.S. Army Air Corps"; Navy contract for 41 trainers in 1934 ("the first government contract enjoyed by this subsidiary"), completed, plus 20 more; an Army Air Corps competition win giving an initial order for 26, "the first order ever received by the subsidiary from this department of the Government"; 55 delivered in 1938 (mostly USAAC, balance Philippine Army); +36,500 sq ft and new foundry/heat-treat buildings 1939; 1,762 employees 1940 | FY1934, FY1935, FY1938, FY1939, FY1940 | **Wichita naming check**: every trainer statement is attached to Stearman / Stearman Division / Wichita, never to the Seattle company |
| **Boeing Aircraft of Canada product** | "planes of English design" under Canadian-government contract (1937-38); 1940 "two-engine flying boats and a substantial quantity of airplane parts"; a new ~200,000 sq ft plant "being built and equipped by the Canadian Government and leased to the Company" | FY1937, FY1938, FY1940 | **Montreal naming check: "Montreal" occurs 0 times in held bytes**; every Canadian statement is printed at **Vancouver, B.C.**, and the Canadian audit report is signed in Vancouver |

### E.3 Process and capacity, reconstructed

FY1940 prints the physical build-out with dates and areas: Plant No. 2 "originally built in 1936 and 1937";
construction contract **May 24, 1940** for 667,000 sq ft gross; second contract **October 15, 1940** covering
about 974,000 sq ft gross "with 140 days allocated for completion", giving Plant No. 2 approximately
1,776,000 sq ft and "the total area of the three plants in Seattle approximately 2,344,500 square feet";
Wichita +142,000 sq ft early 1940 and a further 420,000 sq ft contracted **October 16, 1940** (140 days) for
a Wichita total near 740,000 sq ft, on "land purchased adjacent to the existing Stearman plant". Machinery
procurement at "both Seattle and Wichita" is stated to be "comparable". Advance payments: progress payments
against work in process of $6,921,223.20, and a restricted cash caption reading in full "Cash—Unexpended
balance of payments advanced by the United States on a particular contract, restricted for use on and
securing performance of such contract" ($685,329.98). **P1E01–P1E09 — FACT (company print, audited
adjacency); corroboration 1 lineage.**

STATUS: WRITTEN

---

## F. CUSTOMER

**Frame note (§7).** For an industrial capital-goods firm the customer questions are: who contracted, at
what price basis, with what payment terms, on what concentration, and what recourse each had. The held
bytes answer these for 1934-1940 and not at all for 1916-1933; "first customer" for the 1916 corporation is
UNKNOWN.

| Variable | Value as printed | Source | Confidence |
|---|---|---|---|
| Named customers, 1934-1940 | **United States Navy Department** (41 Stearman trainers, 1934; 20 more, 1935); **United States Army Air Corps** (Stearman trainers as standard primary; Model 299 competition; 39 Fortresses; contracts of 1937-08 $9,928,895 and 1939-09 $8,426,190; options for more four-engine aircraft outstanding at 1939-12-31); **Pan American Airways** (six Clippers 1939, plus options for six more for 1941; three Stratoliners); **Transcontinental & Western Air, Inc.** (five Stratoliners in the 1939 backlog after a 1938 termination of the original six); **Government of the Dominion of Canada** (planes of English design, then two-engine flying boats and parts); **Great Britain** ("a contract with Great Britain to produce a quantity of twin-engine bombers", 1940); foreign trainers "to the Argentine, Mexico and the Philippine Constabulary" (1935); in 1937-38 contracts "by the Corps, the Philippine Army, the Brazilian Army Air Corps and the Argentine Ministry of Marine" | FY1934-FY1940; FY1937 (**COLUMN-REASSEMBLED**, the customer list survives in a right-hand column) | High (each naming is printed with an entity-adjacent verb); Medium for FY1937's list, whose column position leaves "the Corps" unnamed |
| **First customer of the 1916 company** | **UNKNOWN.** No held byte names a purchaser before 1927. The earliest purchaser-in-fact anywhere in the corpus is the **United States** as air-mail contractor (bid opened 1927-01-15; contract entered 1927-02-01 or awarded 1927-01-29; service from 1927-07-01) — and the contracting party named is "Boeing Airplane Company and Edward Hubbard", a corporation plus an individual | dc_circ; `## Untried` #2, #6 remain the routes | High (that nothing earlier is held) |
| Price basis | Per pound for mail (1927: $1.50/lb first 1,000 miles, 15¢/lb each additional 100 miles). For aircraft: fixed contract prices stated in aggregate dollars only; **no unit price, no per-airplane price is printed anywhere in the held corporate print for 1934-1940**. FY1939 does print a price *direction*: "The six Clippers under order are at prices substantially in excess of the prices obtained for the six Clippers delivered in 1939." | dc_circ ¶6; FY1939 | High; and this is a hard limit on §P: no unit economics of any airplane can be computed from this corpus |
| Payment terms / working-capital mechanics | Progress payments deducted inside the inventory caption ($6,921,223.20 against work in process at 1940-12-31; $89,364.15 at 1935-12-31); "substantial advance payments on contracts made by both the United States and Great Britain"; restricted cash held against a specific contract; Emergency Plant Facilities loans whose bank recourse runs "solely to the payments which are to be made by the Government"; Emergency reimbursement "in sixty equal monthly installments commencing with the completion of the facilities" | FY1935, FY1940 incl. Note 3 | High |
| Concentration | Not disclosed. FY1940 gives a customer-class split of **deliveries** (not of receivables or orders): $14,754,875 United States Army; $718,355 United States Navy; $3,917,488 "other customers" — which **foot exactly** to audited gross sales of $19,390,718.32 (DERIVED: `14,754,875 + 718,355 + 3,917,488 = 19,390,718`), giving Army 76.1%, Navy 3.7%, other 20.2% (arithmetic shown; see §P row P1QTN21). No customer-over-X-percent note of the kind later filings carry is printed in-window | FY1940 §Accomplishments vs FY1940 P&L | High (both legs printed); the exact reconciliation is a genuine cross-check between narrative and statement, not a plausibility |
| Customer recourse against the company | The T.W.A. termination runs **both ways**: "a termination by Boeing of its contract with Transcontinental & Western Air, Inc., covering the manufacture and sale of six Stratoliners. A down payment of $397,500 was retained as security against possible damages. At a later date Transcontinental & Western Air, Inc., likewise contended that the contract was terminated and that it intended to claim damages. The companies are now negotiating for a settlement" | FY1938 | High — and note the double: **each party asserted the contract was at an end**, so the held print does not establish who terminated, only that both claimed it |
| Company recourse against customers | Guaranty fund and joint-and-several liability inherited from the 1934 dissolution (FY1934, FY1935) and still provisioned at 1940-12-31 ($81,500.00 "Provision for Contract Guaranty Replacement", and a matching P&L charge) | FY1934, FY1935, FY1940 | High |

STATUS: WRITTEN

---

## G. SUPPLY / HOST SIDE

**Frame note.** The spec's "host side" maps here onto **subcontract, plant, labour and finance hosts** — the
parties whose capacity the company rented. All four are printed in-window; none of them is a supplier
price list, which the corpus does not contain.

| Host | What the bytes print | Source | Confidence |
|---|---|---|---|
| **Sub-contractors** | An asset caption "Advances to Sub-contractors 201,897.00" at 1940-12-31 — the only in-window witness to a subcontract tier; no named sub-contractor appears anywhere in the seven corporate-print layers | FY1940 balance sheet | High (of the caption); **UNKNOWN** (who) |
| **Plant host (public)** | The Canadian subsidiary's 1940 expansion: "a new plant of some 200,000 square feet of floor area, **being built and equipped by the Canadian Government and leased to the Company** for the production of flying boats" | FY1940 | High |
| **Plant host (federal, domestic)** | Emergency Plant Facilities contracts, October 1940: Boeing Aircraft Company to construct and acquire at Seattle at estimated cost ≈$7,625,000.00, Boeing Airplane Company through the Stearman Division at Wichita ≈$3,625,000.00; the Government "agrees to reimburse the companies for the cost of the facilities in sixty equal monthly installments commencing with the completion of the facilities"; Note 3 fixes the ceilings "limited to $3,625,765.22 and $7,627,032.13 respectively, plus interest during the construction period on funds expended"; termination options to retain on payment of cost less fixed depreciation or an agreed price | FY1940 §Financing of Emergency Plant Facilities; Note 3 | High. At 1940-12-31 "the companies had expended $3,033,461.35 … against which borrowings had been made in the total amount of $2,240,445.62" (DERIVED: unexpended head-room against the two ceilings is not computable because the ceilings belong to separate parties — stated, not plugged) |
| **Research host** | "The University of Washington, in Seattle, now has under construction a large high-speed wind tunnel… The Boeing Aircraft Company has entered into a rental contract with the University for part-time use of this tunnel" | FY1935 | High — the earliest in-window externally-owned test infrastructure named in the corpus, and it is a **rental**, so capability was hired, not owned |
| **Labour host / counterparty** | "During 1940 Boeing Aircraft Company concluded a new agreement with **Aeronautical Mechanics Local Union No. 751** and the **International Association of Machinists**, affiliated with the American Federation of Labor. This agreement became effective **August 1, 1940**, and continues to **July 1, 1942**. Either party may, at its option, initiate negotiations for the adjustment of wage rates, overtime rates and vacation privileges as of July 1, 1941." And its cost: "Wage rate increases approximating eighteen per cent resulted from the new Union Agreement previously mentioned. This increased labor cost is reflected in the added costs of the 'Clippers.'" | FY1940 §Management, §Financial Statements | High. **This is the corpus's substitute for the untried NLRB family** (`## Untried` #4): the union, the dates and the wage percentage are printed by the employer; the board's case history is not held |
| **Finance hosts** | 1934-35: New York transfer agent and registrar (City Bank Farmers Trust Company; The National City Bank of New York). 1939-40: a "$5,500,000" loan syndicate "in which the **Reconstruction Finance Corporation** had agreed to participate", arranged February 1940, drawn $4,740,000.00 at March 1, 1940, guaranteed by the parent, "mortgages … placed upon the plants, machinery, equipment and certain other property", "the proceeds of aircraft contracts have been assigned"; the named lender in the FY1939 notes is "**The Pacific National Bank of Seattle**"; 1940: emergency-loan agreements with **The National City Bank of New York** to $4,000,000 (Company) and $8,000,000 (Subsidiary), notes "payable on or before July 1, 1946"; the 1935 balance sheet already shows "Note Payable—Bank 6,000.00" and 1938 shows "Bank Overdrafts 3,037.83" | FY1934, FY1935, FY1938, FY1939 (notes), FY1940 §Financing + Note 3 | High for each printed item; **Medium** that the Pacific National Bank line and the RFC line describe the same facility (adjacent in the FY1939 print, never conjoined in a sentence by the document itself) |
| **Materials / equipment** | FY1939 prints buildings erected "to house the heat treating, anodizing, forming and foundry units of the plant" at Wichita (in-house process capability). FY1940: "Purchased Materials and Parts, at substantially the lower of cost or market 3,063,971.83" and a comparable machine-tool procurement programme at both Seattle and Wichita. No vendor, no commodity price, no lead time appears in held bytes | FY1939, FY1940 | High of what prints; the supply *market* (engines, aluminium) is **UNKNOWN** and is a named gap (P1GAP11) — note that the FY1934a brochure's Pratt & Whitney "Wasp"/"Hornet" engine namings belong to a Hamilton advertisement, not to a Boeing purchase record (entity adjacency fails) |
| **Intellectual host** | Balance-sheet "INTANGIBLES: Patents" is carried **$9,142.93 gross with an equal reserve** in both FY1934 and FY1935 — i.e. the company's own audited print carries patents at zero net. "Royalty and License Fees" appears as an other-income line of **$10,607.37** in FY1940. Patent records are UNTRIED (`## Untried` #5) | FY1934, FY1935, FY1940 | High (printed); the patent portfolio's size is UNKNOWN and the audited line is the only held quantitative handle |

STATUS: WRITTEN

---

## H. MARKET (AS KNOWABLE IN-PERIOD)

**Method note.** Everything below is limited to what a 1940 reader of **this corpus** could know. No
later market size, no jet age, no "obviously huge" — and no imported industry statistics either: the probe
verified that the only non-Boeing periodical holds are negative for this company.

| Question a 1940 investor could ask | What the held bytes let him answer | Source |
|---|---|---|
| Who pays for aircraft, and on what instrument? | Two payers appear: a federal department contracting per pound for mail and by aggregate dollar contract for aircraft (with options), and foreign governments / domestic airlines ordering types. The mail instrument is quoted in full — public advertisement, sealed bids opened on a stated day, award to "the lowest qualified bidder tendering sufficient guarantees", a performance bond under Sections 426 and 427 of Title 39, a four-year term, and a route **certificate** issued in substitution for a contract under the Act of April 29, 1930 | dc_circ Bill ¶¶6-8; Exhibit C route certificate; Act quotation | High |
| Can the payer take the contract away? | Yes, and in-window it did. The 1934 record's bill of complaint attacks "the purported order of the defendant, dated **February 9, 1934**, purporting to annul the contracts for the carrying of air mail therein designated", alleging it "is illegal and void because beyond the authority, power or jurisdiction of the defendant, and because it is unconstitutional in that it results in depriving the plaintiff of its property without due process of law and constitutes an illegal taking of its property without just compensation". The same record reproduces a Post Office rate of "nine cents per pound" on a United Aircraft-controlled route where the award had been at a higher rate. The **outcome is not in the held volume** (see below) | dc_circ, Bill of Complaint ¶ ~(early paragraphs); brief passages | High (that the annulment order and the constitutional theory are printed); **UNKNOWN (adjudicated result)** |
| Is the payer's policy a risk to the manufacturer? | The company's own print says so twice: FY1934 attributes losses to "unsettled conditions in the industry" and to "additional labor and material costs on contracts taken by the operating subsidiaries **prior to the passage of the National Industrial Recovery Act**"; FY1938 reports that the British and Canadian air ministries decided "future contracts for airplane manufacture incident to the British and Canadian rearmament programs shall be placed only with companies controlled by British or Canadian nationals", which the company reads as making it "desirable to dispose of this subsidiary to Canadian interests" | FY1934; FY1938 | High — a **nationality-control rule** is a documented market exit for one of the three plants |
| How large is demand? | Only measurable through the company's own backlog, which the print does supply at six dates: $774,242.82 (1935-01-01), $6,141,203.23 (1935-12-31), $14,112,298.49 (1937-12-31), $14,894,918.47 (1938-12-31), $14,664,991.73 (1939-03-01), $23,002,574 (1939-12-31) and $196,522,446 (1940-12-31, "United States" units only). There is **no** industry total, no national expenditure and no capacity figure anywhere in the held bytes | FY1935, FY1938, FY1939, FY1940 | High (backlog is a printed company figure); no independent count exists behind it (§2 record-selection null) |
| Who else is in it? | Named in the same record and print: Western Air Express, Stout Air Services, Columbia Air Liners (1927 rivals on A.M. 18); Pacific Air Transport, National Air Transport, Varney Air Lines, Northwest Airways, Kohler Aviation, Pennsylvania Airlines, Eastern Air Transport, American Airways (route list in the 1934 record); Transcontinental & Western Air and Pan American Airways as customers; and the manufacturer's own subsidiaries as competitors inside one group — the 1934 management agreement recites that the Operating Companies "are each controlled through stock ownership by the United Aircraft & Transport Corporation, a corporation of the State of Delaware, and are engaged in operating air transport lines, **none of which competes with any of the others** and which together constitute a single connected system" | dc_circ route schedule; management-agreement recitals; FY1938 | High (printed with entity adjacency); U.010 for what the group structure implies |
| What does the company say about its own position? | "Your companies have been leaders in design and quality of manufacture" (FY1934); "recognized as being the finest in their respective classes in the world" (FY1938); "the most effective weapon for national defense possessed by the air forces of this country" (FY1938); "no equal among present day military aircraft" of the 299 (FY1935); and "the United System has flown over 65 million miles, a greater mileage than has been flown…" (a pleading in the 1934 record). **All of these are self-reports with no independent count** | FY1934, FY1935, FY1938; dc_circ | High (that they were printed); **UNKNOWN (that any is true)** — and the 65-million-mile claim is an *advocate's* figure inside litigation paper, which is the weakest possible provenance for a mileage total |

**Record-selection null (§2, stated in §A and §S as required).** What a 1940 reader could *not* know, and
what no later archive has kept: the rejected internal options at each 1934-38 reorganisation step (the
directors' papers are not held and family (e) is untried); any contemporaneous count behind every
"leaders"/"finest"/"65 million miles" claim; the internal cost structure of the Clipper and Stratoliner
programmes except as it surfaced in loss provisions; the result of the March 1939 Army attack-bomber
competition; and — decisively for Stage 1 — the adjudication of the very suit the corpus holds: the
`dc_circ` volume is the **record and briefs**, and a search of its 625,596 bytes for a disposition string
(`decree affirmed/reversed`, `judgment affirmed`) returns **0**. The D.C. Circuit's decision is therefore
UNANSWERED-with-named-route, not lost (§S, `## Untried` #6).

STATUS: WRITTEN

---

## I. COMPETITION

**Discipline applied first.** Every competitor naming below was required to be **entity-adjacent** — a
company name attached to a verb of competing, contracting, bidding or owning — before it was promoted. The
noise candidates and their dispositions:

| Candidate string | Raw occurrences (held bytes) | Disposition after reading the line |
|---|---|---|
| `West` | 33 in dc_circ; 50 in the Edelman volume; 6 in corporate print (1938-40) | **Noise, except one.** In dc_circ every `West` resolves to "105 West Adams Street, Chicago", "Pennsylvania v. West Va.", "West River Bridge Co. v. Dix", "State of West Virginia". In Edelman the party is **Harry R. Weston**, State Treasurer of Wyoming (succeeded William H. Edelman; the Attorney General's appearance is "for defendants Edelman and Weston"), and other hits are public-land descriptions ("Range 105 West of the Sixth Principal Meridian"). In corporate print `West` is "Transcontinental & Western Air, Inc." and "200 West Michigan Street". **No George West, no B & W, appears anywhere.** U.015 |
| `Green` | 6 in dc_circ; 12 in Edelman | **Noise.** dc_circ: "By C. H. GREEN, [seal.] Secretary" of **PACIFIC AIR TRANSPORT** (a rival carrier's bond form) and the citation "*Greenhow* v. Poindexter". Edelman: "J. A. Greenwood, Attorney General of the State of Wyoming" and "the present Green River water supply system". U.015 |
| `C & F` / `-Foundry` | `C & F` = **0** in all 25 files | The only "…& Foundry…" naming in the window is **"Pacific Car & Foundry Company"** in the FY1940 proxy statement, whose president sits on Boeing Airplane Company's board — a **Seattle interlock**, not an aircraft competitor. U.015, and see §J/§B on the OCR decoy for that director's first name |
| `Hubbard` | 15 in dc_circ; 1 in the 1916 Aviation issue | dc_circ's Hubbard is **Edward Hubbard**, the co-bidder and co-contractor — a real, entity-adjacent naming. The 1916 issue's single hit is "J. F. Hubbard" inside a printed roster of names, not Edward. U.011 |
| `Montreal` | **0** in all 25 files | Nothing in the corpus names a Montreal plant. The Canadian layer is printed at **Vancouver, B.C.** in 1934, 1939 and 1940, and the Canadian auditors sign in Vancouver. U.015 |

### I.1 Competitors actually named, with the act attached

| Rival | Act the bytes attach | Source | Confidence |
|---|---|---|---|
| Western Air Express, Inc. | Bid $2.24/lb first 1,000 miles, 22.4¢/100 miles, on A.M. 18, opened January 15, 1927 — i.e. **the next bid above the winner** | dc_circ Bill ¶6(b) | High |
| Stout Air Services, Inc. | Bid $2.64 / 26.4¢ on the same route | ¶6(c) | High |
| Columbia Air Liners | Bid $4.47/lb | ¶6(d) | High |
| Pacific Air Transport | Operated A.M. 8 (Seattle–San Diego via San Francisco, 1,238 miles); its corporate bond form and officers (Gorst president, Green secretary) appear in the same record | dc_circ route schedule; bond form | High |
| National Air Transport, Varney Air Lines, Northwest Airways, Kohler Aviation, Pennsylvania Airlines, Eastern Air Transport, American Airways | Each printed against a numbered A.M. route in the 1934 record's route schedule | dc_circ | High |
| Varney Air Lines / United Aircraft — an ownership dispute *about* competition | A party's rebuttal in the record: "The fact is that **United Aircraft did not own Varney Air Lines in August, 1929. It was not until June 28, 1930**, almost a year thereafter, that United Aircraft acquired any portion of the stock thereof" — rebutting an assertion attributed to "Senator Black" that the A.M. 32 award "was consolidated with another route of United Air Lines July 1, 1930" | dc_circ, brief passage | High (printed); **this is the corpus's only direct witness to a contested date in the United Aircraft accretion sequence, and it is an advocate's sentence, not a finding** — U.010, and the reason §N cannot date the 1929 act |
| Stearman vs Boeing — the same group, different plants | FY1934 prints Stearman as "specialized in trainer types" at Wichita while Boeing Aircraft Company at Seattle made "both military and commercial aircraft"; FY1938 prints the Stearman Division delivering "most of which were primary training planes for the U.S. Army Air Corps"; FY1940 splits the National Defense work "in the field of fast, long range, four-engine bombardment types which the Company at Seattle has pioneered, and in the field of primary training planes produced at Wichita" | FY1934/38/40 | High — the competition that is documented in-window is **between the company's own two plants for the same defence budget**, and by 1938-40 the two are one company, so the rivalry is an allocation question, not a market question |
| Transcontinental & Western Air, Inc. | Customer **and** counterparty in a termination fight, with a claim of damages running both ways | FY1938 | High; see §M |

**Assessment.** The held record lets a competitor be named only where a bid, a route number, a bond or a
contract attaches it. On that test the 1927 field is four named firms at four prices — a genuinely
independent, non-company quantification of competitive distance, and the only one Stage 1 has. The 1934-40
field is not quantified at all in this corpus: no market shares, no rival costs, no competing type's
performance. Where the corporate print asserts leadership ("no equal among present day military aircraft"),
the assertion is single-sourced to the maker and unpriced, and §H's record-selection null applies to it. The
absence of any *manufacturer* competitor — Curtiss, Lockheed, Douglas, North American — from all 25 held
text files is itself a measurement (`Curtiss` ×1 in the munitions volume, whose `Boeing` count is 0; the rest
do not appear), and it is why §I cannot be graded better than Medium at stage level: the competitive set for
1934-40 contracts is **UNTRIED**, not empty (`## Untried` #3, #6, #8).

STATUS: WRITTEN

---

## J. TECHNOLOGY

**No engineering document is held for the first two decades.** The held technical record starts in FY1935
and is entirely company-authored; nothing in the corpus is a test report, a drawing, a stress record or a
patent specification.

| Technology claim | What the bytes print | Source | Class / confidence |
|---|---|---|---|
| All-metal construction as a corporate line | The FY1935 chronology captions carry the words "ALL-METAL" for the B-9A and the 247/S-307-era types, and "SINGLE SEATER ALL-METAL FIGHTER"; FY1935 calls the 299 "four-engined, all metal, bombardment airplane". The **Hamilton** brochure makes the metal argument at length and at advertising heat: "Its enthusiastic acceptance in every field of air transportation has been a splendid tribute to its advanced design … to the greater strength, safety and service of Hamilton all-metal construction", "constructed entirely of metal … non-corrosive alclad duralumin … because metal has proven its superiority in every respect over other materials" | FY1935; `boeing1934a` | FACT that it is printed. **Entity adjacency fails for the brochure**: the metal claim belongs to Hamilton Metalplane, a division advertisement, not to Boeing Aircraft Company — do not read it as Boeing's own technical assertion. U.014 |
| Pressurisation | Model 307 described as "the first commercial airplane able to offer the comfort of normal atmosphere to passengers when flying at altitude"; the supercharging, heating and ventilating systems installed after the initial test programme | FY1938 | FACT of the printed claim; the superlative "first" is RESTATED company speech, corroboration 0 |
| Certification as the gating technology | Repeated, and dated by sequence not by number: CAA tests "lengthy and comprehensive" on the Clipper, then "the Civil Aeronautics Authority issued an Approved Type Certificate"; the Stratoliner under CAA test "for a period of more than three months", "A temporary certificate of air worthiness has been granted… the final certificate will issue as soon as the engineering data has been reviewed by the Authority in Washington, D. C."; and FY1940's Clipper provision cannot even be finalised "until after the first one has been test flown and **licensed by the Civil Aeronautics Bureau**" | FY1938, FY1939, FY1940 | High — and note the **agency-name drift in-window**: "Authority" (1938-39) to "Bureau" (1940), the 1940 Civil Aeronautics Act restructuring, printed but never explained by the company. No antitrust or ATTA word is attached to it (U.010) |
| In-house process technology | Wichita buildings "to house the heat treating, anodizing, forming and foundry units of the plant" (1939) | FY1939 | High |
| Hired research capacity | the University of Washington high-speed wind tunnel, "rental contract … for part-time use" (FY1935) | FY1935 | High |
| Research organisation | "During the year 1939 important additions were made to the technical, aerodynamic and flight research departments and a new factory manager has been appointed"; FY1940: "Contemplated expansion in Engineering, Research and Aerodynamics has been effected in 1940" | FY1939, FY1940 | High (printed) |
| Development cost as a design constraint | FY1934 books development into the loss: "this development expense has accounted for a substantial part of the losses indicated" ($74,922.68 of "Engineering and Development Expense" in the four months). FY1938 quotes its own 1937 report for the rule: "By reason of the large development cost of new model aircraft, it is necessary, in order to meet competitive prices, that such cost be absorbed by the sale of a substantial quantity of aircraft of that model." FY1940 **changes the accounting** so that "certain general, administrative and research expenses were charged to work in process" | FY1934 P&L; FY1938; FY1940 Note 1 + auditors | High — the engineering story and the accounting story are the same story here, and §K keeps the arithmetic |
| Patents | Net zero on the balance sheet in both FY1934 and FY1935 ($9,142.93 gross, $9,142.93 reserve); FY1940 books "Royalty and License Fees" income of $10,607.37 | FY1934, FY1935, FY1940 | High; portfolio size UNKNOWN, `## Untried` #5 (patents) is the route |

**What the 1936 gap costs the section.** The item has **no 1936 layer**, so the year in which the Clipper and
Stratoliner design work is most likely to have been described — and the year the "since 1916" subsidiary was
renamed/reorganised around — is unheld. This is reported as a **measured absence in the carrier**, not as an
absence in history: the file list of the IA item was enumerated by the probe (46 per-year text layers: 1934,
1935, 1937-1978 plus the 1934a and 1941a extra parts), and 1936 is not among them. Route: `FETCH REQUEST` #4.

STATUS: WRITTEN

---

## K. MONEY / PERSONAL FINANCES

### K.1 Personal finances of the founder

**UNKNOWN in every element.** No held byte prints W. E. Boeing's capital, salary, shareholding, loans,
guarantees, departure terms or any transaction with him. The only money attached to a person in the 1927
record is the **$500,000** performance bond posted jointly by the corporation and Edward Hubbard — a
guarantee obligation, whose split between them, and whose indemnification, are not printed. George Westhoff
and any 1916 capitalisation return **0 occurrences** across all 25 non-SEC text files. The routes that could
answer this are family (e) and the unopened 1916-1925 IA items (`## Untried` #2, #6). Personal finance is a
**T2 mandatory section**, and it is delivered here as a named void, not omitted.

### K.2 Company money, 1934-1940 (all audited-adjacent, all one lineage of company print)

| Year | Gross sales | Total charges | Operating result | Other income | Income deductions | **Net** | Accumulated deficit at year-end |
|---|---|---|---|---|---|---|---|
| 4 mo to 1934-12-31 | $1,116,627.32 | $1,352,374.24 | $(235,746.92) | $23,751.52 | $13,981.75 | **$(225,977.15)** | $(225,977.15) |
| 1935 | $1,236,517.77 | $1,587,528.18 | $(351,010.41) | $20,649.09 | $3,438.30 | **$(333,799.62)** | $(514,121.40) |
| 1937 | **not legible** (column-interleaved OCR; only fragments survive — see below) | | | | | | |
| 1938 | not tabulated in this pass | | | | | **$(554,957.96)**, "equivalent to **77c per share** on the number of shares outstanding at the end of the year" | |
| 1939 | | | | | | **$(3,284,073.84)**; of which $(2,606,106) for 1939-01-01→09-30 (printed in the 1939-11-24 stockholder letter) | deficit at 1939-09-30 **eliminated against paid-in surplus, $3,471,686.29** |
| 1940 (domestic, Canada excluded) | $19,390,718.32 | $18,858,972.22 | **$531,746.10** | $100,701.51 | $68,980.79 | **$374,655.29** after $188,811.53 tax provision | $(303,520.30) |

**Footing tests run on the held numbers (each arithmetic performed on this pass; a failure would have been
registered as a conflict):** FY1934 `1,352,374.24 − 1,116,627.32 = 235,746.92` ✓; `235,746.92 − 23,751.52 +
13,981.75 = 225,977.15` ✓; balance side `2,609,415.00 + 885,043.58 = 3,494,458.58` and `+ 200,390.12`
of liabilities/reserves foots to `3,694,848.70` as printed ✓. FY1935 `1,213,382.77 + 35,279.49 + 249,213.41 +
3,500.00 + 86,152.51 = 1,587,528.18` ✓; earned-surplus roll `225,977.15 + 333,799.62 − 45,655.37 =
514,121.40` ✓; total assets `= 3,535,825.11` ✓. FY1940 `19,390,718.32 − 18,858,972.22 = 531,746.10` ✓;
`531,746.10 + 100,701.51 − 68,980.79 = 563,466.82` ✓; `− 188,811.53 = 374,655.29` ✓; surplus roll
`677,966.92 + 208.67 (additional federal income tax for 1938) − 374,655.29 = 303,520.30` ✓; paid-in roll
`917,203.71 + 3,590,067.25 = 4,507,270.96` ✓; capital-stock caption `1,081,673.75 × $5.00 = $5,408,368.75`
**exact** ✓ and `780.25 × $5.00 = $3,901.25` **exact** ✓; total `21,812,419.07 + 2,240,445.62 + 9,616,020.66
= 33,668,885.35` ✓, where `9,616,020.66 = 5,412,270.00 + 4,507,270.96 − 303,520.30` (the year's earned
balance is a **deficit** and is subtracted; the caption prints it as "Earned Surplus (Deficit)").

**Two cross-document ties that carry real weight (DERIVED, arithmetic shown):**
1. **The 1940 profit is exactly the last-quarter-1939 loss.** FY1939 prints the 9-month loss $(2,606,106)
   and the full-year loss $(3,284,073.84) → Q4 1939 = `3,284,073.84 − 2,606,106 = 677,967.84`. FY1940's
   opening deficit is `677,966.92`. The two agree to **$0.92** — which is exactly what the printed 9-month
   figure's missing cents could account for. Interpretation: the 1939-09-30 deficit elimination left nothing
   but the fourth quarter's loss on the books, so **every dollar of 1940 "recovery" starts from a zeroed
   surplus account**, and the accumulated deficit was not earned back by 1940-12-31. Confidence High on the
   arithmetic; Medium on the interpretation (it is an inference from two printings of one company).
2. **The share count implied by two independent captions.** FY1938's "77c per share" on a $554,957.96 loss
   implies ≈**720,700** shares (`554,957.96 / 0.77`). Building the register from the printed issuances gives
   `521,883 (reorganisation total) + 173,424 (1937 rights: 163,847 + 9,577) + 26,273.5 (1938 warrant exercise)
   = 721,580.5`, i.e. `$554,957.96 / 721,580.5 = $0.769` → prints as 77¢ ✓. FY1940 independently implies the
   same base: 360,496 shares offered on a **one-for-two** rights basis implies `720,992` held before the
   offering. Three captions, one share register, agreement within ~0.08%. Confidence High(DERIVED).
   FY1940 also proves the fee arithmetic exactly: `360,496 × ($16 − $5) = 3,965,456.00`;
   `3,965,456.00 − 375,388.75 = 3,590,067.25` ✓ against the printed paid-in addition, and
   `360,496 × 16 = 5,767,936.00 − 5,392,547.25 (net proceeds printed) = 375,388.75` ✓ — the issue expense is
   printed twice, in two different statements, and agrees.

**Capital structure events, printed.** Plan of Reorganization of United Aircraft & Transport Corporation
"approved by the stockholders of that company under date of June 20, 1934", providing that Boeing Airplane
Company issue **521,883** shares of $5.00 par (authorised 600,000) to be distributed to UATC holders "upon
surrender of their stock certificates in the latter company for cancellation"; 442,402½ outstanding and
79,480½ still to be issued at 1934-12-31; 491,365½ and 30,517¾ at 1935-12-31 (**U.007** — this pair does not
foot to 521,883, see below). **28,946½ shares issuable jointly with shares of United Air Lines Transport
Corporation and United Aircraft Corporation** on exercise of UATC stock purchase warrants "if exercised on or
before November 1, 1938"; the warrants did expire in-window, and FY1938 prints "During the year 1938 Boeing
Airplane Company issued 26,273½ shares of capital stock (or scrip certificates) upon the exercise of stock
purchase warrants of United Aircraft & Transport Corporation, which expired on November 1, 1938. The Company
received a total of $445,038.77 for this stock, representing approximately $16.94 per share" — the implied
price foots: `445,038.77 / 26,273.5 = 16.939` ✓. Authorised capital: 600,000 (1934-35) → **800,000**
(implied, printed as the *from* figure at 1939) → **1,250,000 approved at a special stockholders' meeting
December 29, 1939**. The intermediate increase is not printed in any held layer (P1GAP08). Rights offering
May 1940, one share per two held at $16.00; net proceeds $5,392,547.25 applied `$4,740,000.00 repayment of
secured bank loan + $652,547.25 additional working capital` ✓; and FY1940 can state "There are now no
encumbrances upon any of the properties, plants, machinery, or equipment of the Companies" — then, in the
same report, disclose the new emergency-facility borrowing which re-encumbers by assignment of Government
payments. **P1K01–P1K14.**

**U.007 stated precisely.** FY1935's two share sub-captions read `491,365½ issued and outstanding` and
`30,517¾ … still to be issued`; their sum is **521,883¼**, not the printed total **521,883**. One of the two
fraction glyphs is OCR-damaged (the layer renders halves as `%` and quarters as `^4`). FY1934's pair
(`442,402½ + 79,480½ = 521,883`) foots exactly, and FY1940's pair (`1,081,673¾ × $5 = $5,408,368.75`) foots
exactly, so the failure is local to the 1935 layer. **No third number is substituted.** What stands: the
521,883 total, corroborated in both years; and the 1935 split, whose exact halves/quarters are UNKNOWN.

**Money that is a void, named:** no unit price of any airplane; no cost of the 299 programme; no wage bill
except as a percentage (18%, 1940); no dividend ever paid in-window (the only dividends the print discusses
are the **Canadian subsidiary's** 6% cumulative preferred, "paid to December 1, 1930", in arrears $24.50 per
share at 1934-12-31 (total $8,207.50 on 335 shares) and $30.50 per share at 1935-12-31 (total $10,217.50),
"for which no provision has been made", and C$231,730.00 in arrears at 1940-12-31); and no 1916-1933
financial statement of any kind.

STATUS: WRITTEN

---

## L. VALIDATION SIGNALS

Ordered by evidential independence, not by chronology. The strongest signals in this dossier are the ones
the company did not write.

| Date | Signal | Magnitude | What it demonstrated | What it did NOT demonstrate | Source | Confidence |
|---|---|---|---|---|---|---|
| 1927-01-15 → 07-01 | Won a federal air-mail contract against three priced rivals; bond filed; service commenced | $1.50/lb vs $2.24 next bid; $500,000 bond; four-year term | That a Washington corporation and an individual could be the "lowest qualified bidder tendering sufficient guarantees" on a transcontinental route | Revenue, cost, survivability, or that the bidder is the registrant. The award **date itself** is in conflict (U.004) | dc_circ Bill ¶¶6-8 | High |
| 1931 (trial) | A United States government mail-transfer clerk at Cheyenne delivers the mail "to the employee of the Boeing Company" and states the traffic (1-12 letters/flight; pouch ≈1¼ lb) | one to twelve letters | That the operation was real enough for a federal officer to handle its pouches at Cheyenne, and that the Wyoming defendants **admitted** in the record that the plaintiff "is a corporation authorized to do business in Wyoming" | Volume, viability, or interstate-commerce legality — that was the litigated question | Edelman record, Statement of Evidence | High |
| 1931-10-14 → 1932 | The Tenth Circuit **reversed in part** the district court and directed a writ enjoining the Wyoming gasoline tax on fuel "purchases completed outside the State of Wyoming and then brought into that state and used in the planes of appellant in interstate commerce" | a judicial restraint of a state tax on the carrier's fuel | That the carrier's operations were judicially characterised as interstate commerce — an outside court's finding, not a company claim | The Supreme Court's later disposition is **not printed** in the held volume (0 hits for `289 U.S.`); so the final outcome is UNKNOWN | Edelman record | High (CCA text in record); UNKNOWN (certiorari result) |
| 1934-08/09 | The company is formed **and** acquires operating assets out of another corporation's dissolution | 521,883 shares issued to UATC holders | That public holders of a dissolved group received paper in a going concern with three plants — the market's verdict on the group, at the moment of separation | Value: the paper's own first account was a **loss** period | FY1934 | High |
| 1935 | Backlog at 1935-12-31 = $6,141,203.23 vs $774,242.82 at 1935-01-01 | **7.93×** (DERIVED `6,141,203.23 / 774,242.82`) | Order intake inflecting inside one year, printed in the same letter as a further loss | Cash, margins, or delivery — the year still lost $(333,799.62) | FY1935 | High |
| 1935 | Stearman wins the Army Air Corps trainer competition (initial order 26) — "the first order ever received by the subsidiary from this department of the Government" | 26 airplanes | A **second, different** federal customer adding the Wichita plant, after the Navy order of 1934 | Dollars; and the Seattle company's standing | FY1935 | High |
| 1937-08 → 1939-09 | Two four-engine bombardment contracts, $9,928,895 (Aug 1937) and $8,426,190 (Sept 1939) | $18,355,085 combined (DERIVED) | A military programme with two successive awards, and options outstanding at 1939-12-31 | Profit: FY1939 books $232,774.90 of loss "on four-engine bombardment aircraft" | FY1939 | High |
| 1938 | Civil Aeronautics Authority issues an **Approved Type Certificate** for the Clippers after "lengthy and comprehensive tests by the company and by officials of the Civil Aeronautics Authority" | certificate granted | A regulator's independent acceptance of the largest commercial airplane yet built in the U.S., in the company's own print | Recoverability of its cost: the same report charges $488,068.14 | FY1938 | High |
| 1939 | Pan American exercises options for six additional Clippers, "at prices substantially in excess of the prices obtained for the six Clippers delivered in 1939" | 6 units, higher price | A repeat customer and a **rising** price — the only in-window price-direction signal in the corpus | Amount of the increase (not printed) | FY1939, FY1940 | High |
| 1939-12-29 | Stockholders approve an increase in authorised capital from 800,000 to 1,250,000 shares | +450,000 shares | Owners' willingness to dilute themselves into a deficit year | Whether they were asked as investors or as rescuers — both readings fit | FY1939, FY1940 | High |
| 1940-02 → 05 | A $5,500,000 RFC-participating facility is arranged (drawn $4,740,000 at 1940-03-01) and then **repaid in full** from a rights issue that is **oversubscribed by the underwriters' taking 88,248 of 360,496 shares** | $5,392,547.25 net raised | Two independent-money validation events in five months: state-adjacent credit granted, then retired with private cash | Cost of either; and whether the underwriters' take was a subscription failure — the same pattern recurs from 1937 (9,577 of 173,424) | FY1939, FY1940 | High |
| 1940-10 | Emergency Plant Facilities contracts: the Government agrees to fund ≈$7,625,000 + ≈$3,625,000 of plant and reimburse over 60 months | ~$11,250,000 of capacity (DERIVED `7,625,000 + 3,625,000`) | That the state will capitalise this manufacturer's factory space — a change in who bears capex | Terms of the successor contracts; and note the ceilings differ from the estimates (Note 3: $7,627,032.13 / $3,625,765.22) | FY1940 | High |
| 1940-12-31 | First audited net profit, $374,655.29, and deliveries $19,390,718.32 that "exceeded the total deliveries during the preceding three years" | 76.1% Army of deliveries (DERIVED) | Survival into a positive result | Quality of the result: **$163,000 of the pre-tax profit is attributed by the auditors to the change in accounting policy**, and the year's inventory still carried a $640,000 provision with "a further loss … in the approximate amount of $500,000.00" expected after the boundary. The accumulated deficit was still $(303,520.30) | FY1940 + Note 1 + auditors | High (all printed) — U.012 |
| 1940 | "Backlog $196,522,446 … Federal Government regulations prohibit the publishing of further detailed information." | 8.5× the 1939 figure (DERIVED against the FY1940-implied 1939 base, not the FY1939-printed base — U.006) | Demand sufficient to be classified | Anything at all about its composition: **the disclosure regime closes inside the window**, which is why no 1941 curve can be built from company print | FY1940 | High |

STATUS: WRITTEN

---

## M. NEGATIVE SIGNALS / FAILURES

**What "failure" means in this corpus, and its limits.** No sweep for 1916-1940 operational failures has
been done, and nothing in-window records a crash list, a delivery default, a bid loss or a field breakdown.
The failures below are of two kinds only: **(i) incurred losses the company itself priced**, and **(ii) lost
positions the company itself conceded**. Both are single-lineage (company print), which is stated at each
row. The probe's candidate — Boeing Aircraft of Canada's dormancy — is retained as row M2.

| # | Failure, as the bytes state it | Magnitude printed | What it demonstrates | What it does not | Src |
|---|---|---|---|---|---|
| M1 | **Model 299 prototype destroyed.** "After approximately two months of inspection and testing, the airplane was totally destroyed by an unfortunate accident just prior to the final flight test and evaluation for the competition. **This eliminated the airplane from the competition** since all the requirements set forth in the Government circular advertisement could not be completed." | one airframe; elimination from a competition the report says the machine otherwise had "no equal" in | That losing the only prototype is, by the company's own account, disqualifying regardless of performance — a capital-goods failure mode with no software analogue | Cause of the accident; the rival that won; the cost of the airframe; whether "thirteen airplanes and spares" was a consolation award or an independent requirement (the report says the design "merited" it) | FY1935 |
| M2 | **Boeing Aircraft of Canada dormant and mis-made.** "has been practically dormant during the period under review. Little or no aircraft work has been done and the business enjoyed has been largely repairs of small boats, fishing craft and other types of marine work." Estimated liquidation loss "not in excess of $200,000.00"; preferred dividends unpaid since December 1, 1930; minority capital wiped (`Total Capital Stock $34,241.53` against `Minority Proportion of Deficit 34,241.53`) | $200,000 exposure; C$231,730.00 dividends in arrears by 1940 | That a subsidiary acquired in the 1934 split was an aircraft company in name doing boat repair; and that the minority's equity had been consumed | Whether the 1939 decision to keep operating ("After careful study … your directors concluded that it was advisable, for the time being, to continue the operations") was right — the report itself says "It is too early to predict" | FY1934, FY1935, FY1940 |
| M3 | **Clipper cost overrun, booked twice.** 1937: costs "were more than its proportionate realizable value. The same was true of the 'Clipper' project on account of such increased labor costs" (**COLUMN-REASSEMBLED**). 1938: "costs at December 31 were in excess of proportionate sales price and such excess costs were more than the company could reasonably expect to recover through future sales of this model airplane or design rights" → reserve **$488,068.14**. 1940: provision **$640,000.00** "to reduce inventory of flying boats to estimated proportionate sales value" plus an expected further ≈**$500,000.00** | $488,068.14 + $640,000.00 (+≈$500,000.00 forecast) | That the flagship product of 1938-39 — "the largest commercial airplane in the world" — was sold below cost and the company said so in its own report in three consecutive document years | Whether the Clipper programme was a mistake: the report also prints the option six at "prices substantially in excess" | FY1937/38/40 |
| M4 | **Stratoliner programme loss and a terminated customer contract.** "a controversy developed which resulted in a termination by Boeing of its contract with Transcontinental & Western Air, Inc., covering the manufacture and sale of six Stratoliners. A down payment of $397,500 was retained as security against possible damages. At a later date Transcontinental & Western Air, Inc., likewise contended that the contract was terminated and that it intended to claim damages." Then 1939: "an increase in the estimated cost to complete the Stratoliners in the amount of $368,580.58 … this additional loss arose primarily because of modifications in these aircraft as a result of extensive flight tests" | $397,500 retained; $368,580.58 added cost | A lost commercial order at the same time as a re-work cost escalation caused by the company's **own flight testing** | Who was right: **each party asserted the contract was terminated**, so the bytes do not fix the breaching party; and the settlement's terms are not printed | FY1938, FY1939 |
| M5 | **Bombardment rework loss.** "losses incurred on four-engine bombardment aircraft in the amount of $232,774.90, of which $74,734.05 is reflected in an inventory reserve … Increases in cost … were largely due to rework and making up of shortages of parts and payments to labor for overtime necessary to meet delivery schedules" | $232,774.90 on a $9,928,895 contract (2.3%, DERIVED) | Late delivery economics on a military contract printed by the seller: shortage of parts, rework, scheduled overtime | Whether the customer waived or assessed anything — no penalty or credit is printed | FY1939 |
| M6 | **Accumulated deficit eliminated against capital.** FY1940's own equity caption dates it: "after elimination of earned surplus (deficit) at September 30, 1939, by transfer to paid-in surplus in an amount of **$3,471,686.29**" | $3,471,686.29 of shareholders' capital written off against losses | That five years of the company's own print had consumed its paid-in surplus to the point of a formal capital write-off — the balance-sheet face of failure, in a window that opened with a loss year | Insolvency risk as it was then judged: no going-concern language is printed, and the auditors' reports are scope-limited (below) | FY1940 |
| M7 | **Wage shock twice in four years, admitted as a contract-cost driver.** 1937: "On July 1, 1937, however, it became necessary to increase wages materially in excess of any wage rates previously contemplated" (**COLUMN-REASSEMBLED**), with the same page attributing overrun partly to it. 1940: "Wage rate increases approximating eighteen per cent resulted from the new Union Agreement… This increased labor cost is reflected in the added costs of the 'Clippers.'" | "materially in excess" (1937, unquantified); ≈18% (1940) | That labour cost was twice a named cause of booked losses, and that a union agreement is printed by the employer as a **cost**, not as a risk of stoppage | Any stoppage, any dispute, any NLRB proceeding: **0 occurrences**, and the family is UNTRIED | FY1937, FY1940 |
| M8 | **Disclosure and control failures that are the company's, not the market's.** (a) Audit scope: every held report says "we did not make a detailed audit of the transactions"; FY1940 escalates to "by methods, at times, and to the extent we deemed appropriate". (b) Two comparability breaks printed in one page: Canada deconsolidated in 1940 ("Due to exchange restrictions") and the cost-capitalisation change (Note 1) that the auditors say raises pre-tax income by $163,000. (c) A contingent guaranty inherited from the dissolved UATC still provisioned six years later at $81,500.00 against FY1935's estimate that the company's share of the anticipated deficiency "will be required to contribute approximately $15,000.00" | $163,000 of a $563,466.82 pre-tax profit = **28.9%** (DERIVED); guaranty estimate $15,000 → provision $81,500 (5.4×, DERIVED) | That the only "recovery" in the window is documented on statements whose audit scope, consolidation basis and capitalisation policy all moved in the same year — and that an inherited liability of the 1929 group grew rather than ran off | That the numbers are wrong: they foot (§K) and the auditors state they "present fairly". The defect is **comparability and attestation depth**, not arithmetic | FY1934/35/38/39/40 |
| M9 | **Litigation posture as a failure-shaped structure.** Boeing Air Transport is the **appellant/plaintiff** in both held court records: attacking the Postmaster General's February 9, 1934 annulment order as unconstitutional, and suing Wyoming officers over a gasoline tax. The 1934 volume is a record and briefs; **its disposition is not in the bytes** | two matters; $500,000-class bonds; a claim of takings | That the operating carrier's contract tenure was contested at the highest level of the postal-legislative fight of 1934, and that the company was the party bearing the cost of contesting it | Outcome of either at final appeal (U/M above), and whether Boeing Air Transport survived the 1934 separation at all — **no held byte prints its end** | dc_circ, Edelman |

STATUS: WRITTEN

---

## N. FOUNDER / MANAGEMENT DECISIONS

**Whose decisions.** No held in-window byte records a decision by W. E. Boeing. The decision-makers the
bytes name are C. L. Egtvedt (President through the FY1938 report, signed 1939-03-15; then Chairman),
P. G. Johnson (President from 1939-09-09), and a board whose members are printed in 1934, 1935 and 1940.
`actual_result` cells that postdate the boundary are labelled `RETROSPECTIVE` (§13).

| Date | Decision | State before | Information available | Unknowns | Alternatives | Constraints | Rationale (as stated) | Expected result | Actual result | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1934-06-20 → 08-31 | Take the separate-persons route out of the UATC dissolution: a new corporation issues 521,883 shares to UATC holders and acquires "certain of the assets" | A stockholder group of a dissolved Delaware holding company; three operating plants in two countries | The approved Plan of Reorganization; the guaranty of UATC's "all liabilities known and unknown"; the warrant tail (28,946½ shares issuable jointly with two other companies) | Whether the 1916 Washington corporation was continued, renamed or bought; who negotiated; whether any alternative partition was proposed | Take no separate existence; remain unincorporated assets; buy stock instead of assets | "for the purpose of acquiring these assets upon the dissolution"; a joint-and-several guaranty shared by net worth 14.1155 / 55.0728 / 30.8117% | Not stated for the formation act; the stated rationale attaches to the **next** act (simplify management and taxation) | A going concern with an operating subsidiary | A company whose first four months lost $225,977.15 and whose profit-and-loss account "dates from September 1, 1934" | FY1934 letter ¶1, footnotes *, **; FY1935 note | High (that the act is printed); UNKNOWN (motive) |
| 1934 (in the first report) | Keep the two-layer structure **on the table** rather than collapse it at once: "the Board of Directors have under consideration the advisability of Boeing Airplane Company acquiring the assets of Boeing Aircraft Company and possibly of The Stearman Aircraft Company, thereby eliminating these subsidiaries" | Parent + 2 direct subsidiaries + a Canadian third layer | The officers' unpaid status at the parent; the parent's only expenses being "taxes, legal and auditing expenses, fees of transfer agent and registrar and the cost of stock certificates" | Which order, which tax effect, whether Stearman would go first | Keep the layering indefinitely; sell Stearman; merge into an airline | Tax and administration | "In order to simplify management and taxation problems" | Fewer filings, less duplication | Stearman first (1938), the aircraft company second (intended 1936, still pending as an intention in 1938, not printed as completed inside the window) | FY1934; FY1935 ("It is probable that, during the year 1936, Boeing Airplane Company will acquire all the assets of Boeing Aircraft Company"); FY1938 | High |
| 1935-12 | Buy ~28 acres adjoining Boeing Field instead of buying an existing factory | Small volume, large multi-engine trend | "the increased operating efficiency demonstrated by large multi-engined aircraft has established a trend"; "Present plans call for the construction of a modern assembly building during the year" | Cost; whether the airport relationship mattered | Build elsewhere; lease; defer | "These plans for improved facilities will not require additional capital" | Assemble "large aircraft in a most efficient manner", with "rail and waterway connections" | A new assembly building | Plant No. 2 built 1936-37 and then doubled out from under it in 1940 | FY1935; FY1940 | High |
| 1935 | **Rent** the University of Washington wind tunnel part-time rather than build one | No in-house aerodynamic laboratory | The tunnel "now has under construction"; a rental contract "for part-time use" | Rental cost (not printed); queue risk | Build; go without; use a government lab | Capital scarcity implied by a loss year | "an excellent laboratory for advanced aerodynamic research and testing", "of great assistance … in the development of advanced design" | Access to high-speed testing | FY1939 prints "important additions … to the technical, aerodynamic and flight research departments" — hired capability becoming owned staff | FY1935, FY1939 | High |
| 1936 (not held) | The decision to build the Clipper and Stratoliner lines, and the authorised-capital step from 600,000 to 800,000 shares, both fall in the **missing 1936 layer** | — | — | Everything about it | — | — | **Not reconstructible.** Recorded as a decision-void with a named route (`FETCH REQUEST` #4), not as an absence of decision | — | — | carrier file list | n/a |
| 1937 (May) | Fund the company by a **rights issue to existing holders** rather than new outside equity: 173,424 shares total, 163,847 taken on exercise of "rights", 9,577 "taken up by the underwriters" (**COLUMN-REASSEMBLED** for the tail) | Loss years 1934-35, a deficit carried into 1937 | The 1934-35 print of the deficit; the transfer-agent/registrar apparatus already in New York | Subscription rate by holder; the rights price (not printed in the legible fragments) | Bank borrowing (the company was borrowing by 1938-39); a private placement; retrenchment | A four-engine programme about to be priced at "a contract price" that then had to absorb wage increases | Not stated in the legible columns | Cash without a new controlling holder | 5% of the issue taken up by underwriters — the same pattern repeated in 1940 at 24.5% (DERIVED `88,248 / 360,496`) | FY1937 (fragments), FY1940 | Medium (fragments) / High for 1940 |
| 1938 | Take Stearman out of corporate form and run Wichita as a **division** | Stearman profitable as a corporation since at least 1937-38 | The 1934-35 intention; Stearman's own profit record | Whether Stearman holders accepted; tax computation | Keep it a subsidiary; sell it | "as proposed in last year's annual report" | Eliminate a layer | The Stearman Division is still a division at the boundary and its Wichita output is doubled in 1940 under federal contract | FY1937 (COL-REASSEMBLED), FY1938, FY1940 | High |
| 1938 | Keep **Boeing Aircraft of Canada** in operation instead of liquidating it, having earlier estimated a ≤$200,000 loss | Dormant, doing boat repair, minority wiped | The rearmament opportunity; the "management was changed and the operating overhead was substantially reduced"; unfilled orders at a multi-year high | Whether reduction of overhead was sufficient; the boat work's margin | Liquidate; sell to Canadian interests; keep as dormant | 6% preferred arrears; later a **nationality rule** | "After careful study … it was advisable, for the time being, to continue"; the same report admits "It is too early to predict" | Turnaround | A small profit in 1937 — "its first since 1929" — then 1938's nationality restriction makes disposal "desirable", a 1940 Canadian-government-built plant, and arrears of C$231,730.00 still unpaid at the boundary | FY1935, FY1937, FY1938, FY1940 | High |
| 1939-09-09 | **Replace the management.** "The present management of your Company undertook its duties on September 9, 1939." | A nine-month loss of $2,606,106; a stockholder letter written on 1939-11-24 about "the condition of your companies as of September 30, 1939"; delivery schedules out of line with contractual obligations | The backlog figures, the Clipper/Stratoliner cost position, the CAA's hold on the Stratoliner certificate | Who was replaced, by whom, on what terms; whether Egtvedt's move to Chairman was the same act; the board's minutes are not held | Bankruptcy-adjacent retrenchment; sale; a technical rather than managerial fix | A deficit about to be written off against paid-in surplus; delivery dates owed on $9,928,895 and $8,426,190 contracts | Stated objective: "to bring delivery schedules into line with contractual obligations" | On-time delivery and a production study | FY1940: "Satisfactory progress has been made toward the management objectives set forth in the Annual Report for 1939. The production rate has been substantially increased"; deliveries exceed the prior three years combined; first profit | FY1939, FY1940 | High (act and date); **Low** for causation — see the caution below |
| 1939-12-29 | Increase authorised capital 800,000 → 1,250,000 and hold rights in reserve | A deficit of $3,471,686.29 about to be eliminated against paid-in surplus | The $5,500,000 facility then being arranged | Whether the authorisation was for the rights or for an acquisition; "No definite program has been adopted by the Directors" | Borrow more against the plants; sell the Canadian subsidiary | Mortgages and assigned contract proceeds were already the bank's terms | To have the share authority ready "as conditions make such an offering advisable" | Optionality | Used within five months (May 1940, 360,496 shares, net $5,392,547.25), and the borrowed money repaid | FY1939, FY1940 | High |
| 1940 (May → Oct) | Retire the encumbrance, then take the **Government's** plant money instead of the bank's | Mortgaged plants, assigned contract proceeds, $4,740,000 drawn | The rights proceeds; the emergency-facility terms; advance payments from "both the United States and Great Britain" | Whether other firms were offered the same terms (not in corpus) | Keep the bank loan; fund expansion on the rights cash alone; refuse the program | 60-month reimbursement; bank recourse "solely to the payments … to be made by the Government"; notes payable on or before July 1, 1946 | "In order to assist in expediting the National Defense program" | Unencumbered plants and expansion cash | "There are now no encumbrances upon any of the properties…" plus a new $3,033,461.35 of emergency expenditure funded to $2,240,445.62 by year-end | FY1940, Note 3 | High |
| 1940 | Change the accounting so that allocated general, administrative and engineering-research cost sits **in work in process** | Cost charged to profit and loss "directly" in prior years, i.e. in loss years | The inventory rule "not permitted to exceed its proportionate sales value"; ~$163,000 quantified | Whether an outside adviser required or permitted it; the comparability note the company does not write | Keep the old policy | The auditors state the change, its amount and its direction in their own report | "This change has had the desirable effect of having the Profit and Loss statement reflect the true cost of a project in the same period in which the income therefrom is taken up" | Matching | First reported profit, $163,000 of 563,466.82 pre-tax attributable to it (28.9%, DERIVED) — **U.012** | FY1940 Note 1 + auditors' report | High |

**Causal caution (§14.10, RD-034, applied to my own coda).** The 1939-09-09 management change and the 1940
recovery are adjacent in the print, and the print itself places the new management's objectives and their
"progress" in the same report as the first profit. That adjacency is **not** a demonstrated mechanism: the
held bytes also show, in the same two reports, an $8.4m new contract in September 1939, a rights issue and
loan repayment in May 1940, emergency plant contracts in October 1940, advance payments from two
governments, and an accounting change worth $163,000. Any of those alone could produce the reported result.
**Mechanism UNKNOWN; best-supported reading: the recovery is order-intake- and finance-driven, with
management change an enabling condition whose contribution cannot be isolated from this corpus (INFERENCE,
Low-Medium).** A hindsight reading — "new management saved Boeing" — is refused here on the held evidence,
and would fail the anti-hagiography test because it is unverifiable from anything a 1940 reader had.

STATUS: WRITTEN

---

## O. COUNTERFACTUAL OPPORTUNITIES

**Rule applied.** Each route below is stated as an option **visible inside the window**, with the byte that
makes it visible, and with its outcome recorded as UNKNOWN or `(PB)`. No route is graded by what actually
happened later.

| Route | What made it visible in-period | What the bytes say the company did | What is knowable about the fork |
|---|---|---|---|
| **Stay in carriage, not manufacture.** The 1927 contract was won by the manufacturer and flown by a separate carrier (Boeing Air Transport, sublet April 29, 1927), and the 1930 Act's route-certificate system converted contracts into ten-year certificates in the hands of the operators | dc_circ Bill ¶8; the Exhibit-C certificate; the 1934 record's schedule of A.M. routes held by named carriers | The corpus holds **no** document in which Boeing Airplane Company (1934-40) carries mail; the carrier line is visible only in litigation paper | The trade-off is measurable on one leg: 1-12 letters per flight and a $1.50/lb rate — i.e. the carriage option was a low-volume postal franchise, not a passenger business. Whether a manufacturing firm could have kept both is **not addressed by any held byte**; U.001's unresolved identity question is partly why: the corpus cannot say which person gave it up |
| **Sell the Canadian plant in 1938 instead of keeping it.** FY1938 prints that the British and Canadian air ministries would place rearmament contracts "only with companies controlled by British or Canadian nationals" and that "it appears desirable to dispose of this subsidiary to Canadian interests. Steps toward that end have been taken." | FY1938 §Boeing Aircraft of Canada Limited | Disposal is asserted as "steps taken"; the FY1940 print still describes Boeing Aircraft of Canada Limited as a **wholly-owned subsidiary** of Boeing Aircraft Company, now with a Government-built leased plant and C$231,730 in preferred arrears | **Measured non-completion inside the window**: the disposal the 1938 report announced is not done by the 1940 report. Whether "steps" were taken and abandoned, or blocked, is UNKNOWN; the nationality rule's later effect on Canadian production is `(PB)` |
| **Refuse or re-price the Clipper.** 1938 books $488,068.14 because excess cost exceeded anything recoverable "through future sales of this model airplane **or design rights**"; 1940 books $640,000.00 more and forecasts ≈$500,000.00 further, while separately noting the option six were priced "substantially in excess" of the delivered six | FY1938, FY1939, FY1940 | The programme continued and Pan American exercised its option | The bytes give the company one genuine alternative it names itself — selling **design rights** instead of aeroplanes — and one statement of why it is hard: "The Clipper … because of its size and cost, naturally has a comparatively limited market." Whether any design-rights sale occurred is UNKNOWN (0 mentions of a completed sale) |
| **Merge into the airline group rather than out of it.** The 1934 split created a manufacturer with a $15,000 share of an "anticipated deficiency" and a joint guaranty with the two airline-side companies | FY1934 footnote; FY1935 contingent-liability note | Stayed separate and paid: guaranty provision $81,500.00 at 1940-12-31 | The counterfactual is only visible as a **cost of separation** in the print; nothing in the corpus states a preference for it. Outcome of the guaranty after 1940: `(PB)` and not examined |
| **Do not take the emergency-plant contracts.** Their terms are printed in Note 3 in full, including the 60-month reimbursement ceiling, the interest-during-construction add-on, the termination options, and bank recourse confined to Government payments | FY1940, Note 3 | Taken in October 1940; $3,033,461.35 expended by December 31 | A firm choice with printed terms is rare in this window and this is the one. The alternative (self-funded expansion) is named in the FY1935 page "These plans for improved facilities will not require additional capital". Whether the terms were better than the bank's is **uncomputable from held bytes** — no interest rate is printed |
| **Bank on exports.** FY1934 writes off the cost of a foreign-market study "Currently", because "Upon the dissolution of that company your subsidiaries were left without any foreign representation"; FY1935 reports "a limited number of airplanes were sold" abroad and Stearman trainers to Argentina, Mexico and the Philippine Constabulary; FY1937 prints an English-design contract from the Canadian government and customers in the Philippine Army, Brazilian Army Air Corps and Argentine Ministry of Marine; FY1940 prints a Great Britain bomber contract | FY1934, FY1935, FY1937, FY1938, FY1940 | Continued export selling, rising in importance to a national-government contract | This is the one counterfactual that was **taken, not declined** — and its in-window scale is $3,917,488 of "other customers" out of $19,390,718 (20.2%, DERIVED) at the boundary. The bytes do not separate foreign military from foreign government from civilian, so the composition of that 20.2% is UNKNOWN |

STATUS: WRITTEN

---

## P. QUANTITATIVE METRICS TABLE

**Denominators stated at the head (§6):** all dollar figures are **nominal U.S. dollars of the printed year**,
taken from the company's consolidated stockholder reports, **not** inflation-adjusted and **not** segmental
except where a year's basis is labelled "domestic only" (FY1940) or "Canadian dollars" (FY1940 Canada).
Fiscal years are the company's (calendar-year ends). "Contract price" figures are aggregate contract values,
never revenue. A `UNKNOWN` value means no held byte prints it. Confidence follows §3.

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| P1QTN01 | 1934-09-01 | Start of the reporting company's own profit-and-loss account | 1934-09-01 | date | FY1934 letter ¶1 | 1935-03-04 | High |
| P1QTN02 | 1934-08-31 | Date of the reorganisation / net-assets-acquired | 1934-08-31 | date | FY1934 capital-surplus caption; FY1935 "the date of reorganization" | 1936-03-09 | High |
| P1QTN03 | 1934-06-20 | UATC Plan of Reorganization approved by its stockholders | 1934-06-20 | date | FY1934 footnote ** | 1935-03-04 | High |
| P1QTN04 | 1934-12-31 | Gross sales, less discounts/returns/allowances (4 months, consolidated incl. Canada) | 1,116,627.32 | USD | FY1934 P&L | 1935-03-04 | High |
| P1QTN05 | 1934-12-31 | Net loss (4 months) | (225,977.15) | USD | FY1934 P&L | 1935-03-04 | High |
| P1QTN06 | 1934-12-31 | Engineering and development expense (4 months) | 74,922.68 | USD | FY1934 P&L | 1935-03-04 | High |
| P1QTN07 | 1934-12-31 | Total assets | 3,694,848.70 | USD | FY1934 balance sheet | 1935-03-04 | High |
| P1QTN08 | 1934-12-31 | Cash | 1,102,284.90 | USD | FY1934 balance sheet | 1935-03-04 | High |
| P1QTN09 | 1934-12-31 | Shares issued or to be issued / outstanding | 521,883 / 442,402½ | shares | FY1934 capital-stock caption + footnote ** | 1935-03-04 | High (total); Medium (the ½, OCR fraction) |
| P1QTN10 | 1934-12-31 | Parent ownership of operating subsidiaries | 100 | % of stock, Boeing Aircraft Co and Stearman | FY1934 letter ¶2 | 1935-03-04 | High |
| P1QTN11 | 1934-12-31 | Parent ownership of Boeing Aircraft of Canada Ltd | 92.62 % common; 90.43 % preferred | % | FY1934 letter ¶3 | 1935-03-04 | High |
| P1QTN12 | 1934 | Stearman's first government contract | 41 trainers | airplanes | FY1934 letter ¶5 | 1935-03-04 | High |
| P1QTN13 | 1916 | "has been engaged in the manufacture of aircraft since 1916" — of **Boeing Aircraft Company**, a Washington corporation, Seattle plant | 1916 | year (printed) | FY1934 letter ¶3 | 1935-03-04 | High (that it prints); **the year is not attached to the report addressee** |
| P1QTN14 | 1935-01-01 | Unfilled orders | 774,242.82 | USD | FY1935 | 1936-03-09 | High |
| P1QTN15 | 1935-12-31 | Unfilled orders | 6,141,203.23 | USD | FY1935 | 1936-03-09 | High |
| P1QTN16 | 1935 | Backlog growth ratio (DERIVED) | 7.93 | × | `6,141,203.23 / 774,242.82` | 1936-03-09 | High (arithmetic shown) |
| P1QTN17 | 1935-12-31 | Gross sales / operating loss / net loss | 1,236,517.77 / (351,010.41) / (333,799.62) | USD | FY1935 P&L | 1936-03-09 | High |
| P1QTN18 | 1935-12-31 | Accumulated deficit | (514,121.40) | USD | FY1935 surplus account | 1936-03-09 | High |
| P1QTN19 | 1935 | Recoverable engineering and development costs charged to expense in the prior year, deducted on the surplus roll | 45,655.37 | USD | FY1935 consolidated earned surplus account | 1936-03-09 | High |
| P1QTN20 | 1935-07-22 | Twentieth anniversary of the 1916 subsidiary (**day printed; year DERIVED `1936 − 20`**) | 1935-07-22 stated as "July 22 of this year" | date | FY1935 §Boeing Aircraft Company ¶1 | 1936-03-09 | **Medium (DERIVED)**; U.003 |
| P1QTN21 | 1940 | Deliveries by customer class: Army / Navy / other | 14,754,875 / 718,355 / 3,917,488 | USD | FY1940 §Accomplishments | 1941-03-08 | High; sums to gross sales exactly (DERIVED check) |
| P1QTN22 | 1940-12-31 | Employment Seattle / Wichita / Vancouver, with printed increases | 8,420 (+2,449) / 1,762 (+1,258) / 704 (+388) | persons | FY1940 §Personnel | 1941-03-08 | High; 1939 implied totals 5,971 / 504 / 316 (DERIVED) |
| P1QTN23 | 1937-12-31 / 1938-12-31 / 1939-03-01 | Unfilled orders | 14,112,298.49 / 14,894,918.47 / 14,664,991.73 | USD | FY1938 §Unfilled Orders | 1939-03-15 | High |
| P1QTN24 | 1939-12-31 | Unfilled orders (all units incl. Canada, per FY1939 print) | 23,002,574 | USD | FY1939 §Unfilled Orders | 1940 | High |
| P1QTN25 | 1939-12-31 | Unfilled orders implied by FY1940 (U.S. units only) | 22,129,625 | USD | DERIVED `196,522,446 − 174,392,821` | 1941-03-08 | High (arithmetic); **conflicts with P1QTN24 by 872,949 — U.006** |
| P1QTN26 | 1940-12-31 | Unfilled orders, U.S. units | 196,522,446 | USD | FY1940 §Business in Hand | 1941-03-08 | High; composition withheld by regulation |
| P1QTN27 | 1938 | Net loss and per-share equivalent | (554,957.96) / 0.77 per share | USD / USD per share | FY1938 opening paragraph | 1939-03-15 | High |
| P1QTN28 | 1938 | Clipper reserve | 488,068.14 | USD | FY1938 | 1939-03-15 | High |
| P1QTN29 | 1938 | Warrant-exercise issue: shares, proceeds, implied price | 26,273½ / 445,038.77 / ≈16.94 | shares / USD / USD per share | FY1938 §Changes in Capital Structure | 1939-03-15 | High; `445,038.77/26,273.5 = 16.939` ✓ |
| P1QTN30 | 1939-01 / 1939-03 | Domestic bank loans: peak and reduced | 2,900,000 (Jan 1939 peak) → 2,030,000 (Mar 2, 1939) | USD | FY1938 §Bank Loans | 1939-03-15 | High |
| P1QTN31 | 1939-09-30 | Earned deficit eliminated against paid-in surplus | 3,471,686.29 | USD | FY1940 capital caption | 1941-03-08 | High |
| P1QTN32 | 1939-09-30 / 1939-12-31 | Net loss 9 months / full year / implied Q4 | (2,606,106) / (3,284,073.84) / (677,967.84 DERIVED) | USD | FY1939 letter (11-24 letter quoted) and P&L; FY1940 opening deficit 677,966.92 | 1940 / 1941-03-08 | High; the $0.92 tie is shown in §K |
| P1QTN33 | 1939 | Stratoliner estimated cost increase / bombardment loss / its inventory-reserve part | 368,580.58 / 232,774.90 / 74,734.05 | USD | FY1939 | 1940 | High |
| P1QTN34 | 1937-08 / 1939-09 | Four-engine bombardment contract values | 9,928,895 / 8,426,190 | USD | FY1939 §Deliveries, §Unfilled Orders | 1940 | High |
| P1QTN35 | 1939-11-24 / 1940-02 / 1940-03-01 | RFC-participating facility applied for / arranged / drawn | 5,500,000 authorised ceiling / completed / 4,740,000.00 drawn | USD | FY1939 §Bank Loan; FY1940 §Financing | 1940 / 1941-03-08 | High |
| P1QTN36 | 1939-12-29 | Authorised capital increase approved | 800,000 → 1,250,000 | shares | FY1939 §Increased Capitalization; FY1940 §Financing | 1940 / 1941-03-08 | High |
| P1QTN37 | 1940-05 | Rights issue: offered / from rights / from underwriters / price / net proceeds / expense | 360,496 / 272,248 / 88,248 / 16.00 / 5,392,547.25 / 375,388.75 | shares / USD per share / USD | FY1940 §Financing, paid-in surplus account, Note (1937 counterpart 163,847 + 9,577 = 173,424) | 1941-03-08 | High; all four arithmetic ties in §K foot |
| P1QTN38 | 1940-10 | Emergency Plant Facilities estimated costs and Note-3 ceilings | ≈7,625,000 + ≈3,625,000; limited to 7,627,032.13 + 3,625,765.22 plus construction-period interest | USD | FY1940 §Financing of Emergency Plant Facilities; Note 3 | 1941-03-08 | High |
| P1QTN39 | 1940-12-31 | Emergency expenditure / related bank borrowing / authorised bank ceilings | 3,033,461.35 / 2,240,445.62 / 4,000,000 (Company) + 8,000,000 (Subsidiary) | USD | FY1940; balance sheet; Note 3 | 1941-03-08 | High |
| P1QTN40 | 1940-12-31 | Gross sales / operating profit / pre-tax / tax / net (domestic only) | 19,390,718.32 / 531,746.10 / 563,466.82 / 188,811.53 / 374,655.29 | USD | FY1940 P&L | 1941-03-06 (auditors) | High |
| P1QTN41 | 1940 | Pre-tax income attributable to the accounting change | 163,000.00 ( = 28.9% of 563,466.82, DERIVED) | USD / % | FY1940 Note 1 and auditors' report | 1941-03-06 | High (both state it) — U.012 |
| P1QTN42 | 1940-12-31 | Clipper inventory provision / forecast further loss beyond the boundary | 640,000.00 / ≈500,000.00 | USD | FY1940 P&L caption; Note 1 | 1941-03-08 | High |
| P1QTN43 | 1940-12-31 | Cash / restricted cash / progress payments against WIP / total assets / equity | 11,330,223.92 / 685,329.98 / 6,921,223.20 / 33,668,885.35 / 9,616,020.66 (after deficit) | USD | FY1940 balance sheet | 1941-03-08 | High |
| P1QTN44 | 1940-12-31 | Capital stock caption | 1,081,673¾ issued and outstanding = 5,408,368.75; 780¼ to be issued for UATC certificates = 3,901.25 | shares / USD | FY1940 balance sheet | 1941-03-08 | High; both captions foot to $5.00 par exactly, which is why these fractions **are** trusted where the FY1935 pair (U.007) is not |
| P1QTN45 | 1940-12-31 | Contract-guaranty provision (UATC legacy) / P&L charge | 81,500.00 / 81,500.00 | USD | FY1940 balance sheet and P&L | 1941-03-08 | High; against FY1935's ≈15,000 estimate (DERIVED ratio 5.4×) |
| P1QTN46 | 1940-12-31 | Canadian subsidiary, in **Canadian dollars** | net profit 10,347.06; total assets 787,272.39; notes payable to bank 242,000.00; advances from U.S. affiliated companies 129,304.42; preferred dividends in arrears 231,730.00 | CAD | FY1940 separate Canadian statements | 1941-02-14 (Riddell, Stead, Graham & Hutchison) | High; **currency-labelled and NOT consolidated** — a second, different audit firm attests it |
| P1QTN47 | 1940-12-31 | Director shareholdings / aggregate officer-director remuneration / counsel fees | 9,384 of 1,081,673¾ = 0.868% (DERIVED) / 92,355 / 18,000 + 18,750 | shares / USD | FY1940 Proxy Statement and balance-sheet caption | 1941-03 | High |
| P1QTN48 | 1927-01-15 | Four A.M. 18 bids, ordered | 1.50 (Boeing Airplane Co & Hubbard) / 2.24 (Western Air Express) / 2.64 (Stout) / 4.47 (Columbia Air Liners) | USD per pound, first 1,000 miles | dc_circ Bill ¶6 | 1934 record | High; winner 33.0% below next bid (DERIVED) |
| P1QTN49 | 1927 | Performance bond | 500,000 (OCR `500,0Q0`) | USD | dc_circ Bill ¶7 | 1934 record | Medium (final digit destroyed); Sections 426, 427 of Title 39 cited |
| P1QTN50 | 1931 (trial) | Mail actually tendered at Cheyenne for Rock Springs | 1 to 12 letters per flight; pouch with contents ≈1 lb 4 oz; pouch with lock 13 oz | counts / weight | Edelman, Statement of Evidence (federal transfer clerk) | 1931-10-14 lodging | High |
| P1QTN51 | 1934-04 (Act) / 1930-10-21 (certificate) | Statutory basis and date of the route certificate in substitution | Act approved April 29, 1930; certificate issued October 21, 1930 | dates | dc_circ Exhibit C and the ¶17 amendment recital | 1934 record | High |
| P1QTN52 | 1934-02-09 | Postmaster General's order "purporting to annul the contracts for the carrying of air mail therein designated" | 1934-02-09 | date | dc_circ Bill of Complaint | 1934 record | High (that the order and the pleading date are printed); the adjudication is UNKNOWN |
| P1QTN53 | 1929-08 / 1930-06-28 | Contested United Aircraft acquisition dates (an advocate's sentence, not a finding) | "did not own Varney Air Lines in August, 1929 … not until June 28, 1930" | dates | dc_circ brief passage | 1934 record | Medium — party assertion in litigation paper; U.010 |
| P1QTN54 | 1936-1937 | Plant No. 2 original construction | "originally built in 1936 and 1937" | years | FY1940 §Plant Facilities | 1941-03-08 | High (printed); the 1936 report itself is not held |
| P1QTN55 | 1940-05-24 / 10-15 / 10-16 | Construction contracts let, Seattle (667,000 sq ft), Seattle (≈974,000 sq ft, 140 days), Wichita (420,000 sq ft, 140 days) | areas in square feet | sq ft | FY1940 §Plant Facilities | 1941-03-08 | High; totals stated as ≈1,776,000 (Plant 2) / ≈2,344,500 (three Seattle plants) / ≈740,000 (Wichita) |
| P1QTN56 | 1973-07-25 | **EDGAR conformed-name change from "BOEING AIRPLANE CO"** — `(PB)`, retained only for U.009 | printed in 26 of 33 held SEC `.txt` files | date | SEC SGML header block, `FORMER COMPANY:` field | 1994-03-15 → 2002 | High (that the field prints 26 times); Medium as to what the field proves (a registry change date, not necessarily the corporate act) |
| P1QTN57 | 1996-10-29 / 1998-05-13 | `(PB)` recital: "Boeing was originally incorporated in Washington in 1916 and was reincorporated in Delaware in 1934" | 2 accessions, one boilerplate sentence | statement | S-4 (acc. 0000950123-96-006004) and S-4/A (acc. 0000891020-98-000905) | 1996, 1998 | Medium as a recital; **not** evidence of the 1916 act; U.001 |

**Rows withheld from §P and why:** every FY1937 income-statement and balance-sheet figure. The FY1937 layer
renders two-column text and rotated table columns as interleaved garbage (`C/2`, `os`, `3*`, `CD` on
thousands of lines), so no FY1937 amount can be read at the confidence the table requires except the two
fragments quoted in §K/§N (163,847 + 9,577 rights shares) and the tax provision `65,423.20 + 2,046.33 =
67,469.53` ✓. **Withholding is not absence**: FY1937 net result, sales and assets are
**UNANSWERED-in-this-layer**, and the remedy is a re-OCR or page-image pass (`FETCH REQUEST` #3).

STATUS: WRITTEN

---

## Q. CHRONOLOGICAL MICRO-TIMELINE

Precision rule: a date enters only where a held byte prints it. "(DERIVED)" marks a day or year obtained by
arithmetic on printed dates, with the arithmetic in §K/§P.

| Date | Event | Actors | Place | Class / src |
|---|---|---|---|---|
| 1916 | "since 1916" — manufacture of aircraft by **Boeing Aircraft Company, a Washington corporation** | Boeing Aircraft Company | Seattle, Washington | RESTATED company self-claim (FY1934); U.001 |
| 1916 (DERIVED: `1936 − 20`) | Twentieth-anniversary day of that subsidiary falls **July 22** | same | same | DERIVED from FY1935; U.003 |
| 1916 | Company-authored picture chronology opens: "THE FIRST BOEING PLANE— A TWO-PLACE TRAINER SEAPLANE" | Boeing Airplane Company (report author) | — | RETROSPECTIVE INTERPRETATION (FY1935 final page) |
| 1921-22 / 1926-27 / 1927-28 / 1929 | MB-3A Army pursuit; FB-5 carrier-type Navy fighter; F3B-1 Navy carrier fighter, air-cooled; 40-B4 four-passenger mail plane | the 1916 subsidiary, as claimed in 1935 | — | RESTATED, years legible (FY1935); the flying-boat/80-A/P12-C/Monomail/B-9A/299 rungs are not quotable |
| 1926-11-15 | Public advertisement requesting bids for Route A.M. 18 | Post Office Department | Washington, D.C. | FACT (dc_circ) |
| 1927-01-15 | Bids opened under Section 425 of Title 39: Boeing Airplane Company and Edward Hubbard $1.50/lb; Western Air Express $2.24; Stout Air Services $2.64; Columbia Air Liners $4.47 | four bidders | Georgetown Station, Seattle for the winners | FACT (dc_circ Bill ¶6) |
| 1927-01-29 | "The contract was awarded under date of January 29, 1927 … as the lowest responsible bidders" | Postmaster General | — | FACT of the string; conflicts with 1927-02-01 → U.004 |
| 1927-02-01 | "on or about February 1, 1927, the then Postmaster General … awarded the contract … as being the lowest qualified bidder"; route certificate recital: the parties "on the 1st day of February, 1927, duly entered into a contract" | Boeing Airplane Company, Incorporated, of Seattle, "a corporation duly organized and existing under the laws of the State of Washington"; Edward Hubbard | Chicago → San Francisco route | FACT (dc_circ Bill ¶7 + Exhibit recital) |
| 1927 (undated in the held form) | Performance bond filed, $500,0Q0 | Boeing Airplane Company and Edward Hubbard | — | FACT (OCR digit destroyed) |
| 1927-04-29 | "Boeing Air Transport, Incorporated, of Seattle, Washington, a corporation duly organized and existing under the laws of the State of Washington" appears as an existing person; the contract "was duly sublet to Boeing Air Transport, Inc." | BAT | Seattle | FACT (dc_circ ¶8 and certificate) |
| 1927-07-01 | "Performance under the contract commenced July 1, 1927, and has continued to date." | BAT | A.M. 18 | FACT (dc_circ); W. E. Boeing sworn as BAT's president, oath undated in bytes |
| 1929 | (a) 40-B4 four-passenger mail plane year on the company's own chronology; (b) the United Aircraft & Transport step, whose date **no held byte prints as an act**; (c) a party's later assertion in the 1934 record disputes the ownership date of Varney (Aug 1929 vs June 28, 1930) | — | — | **The 1929 act is UNKNOWN**; U.010, P1GAP02 |
| 1930-04-29 | Act "to Amend the Air Mail Act of February 2, 1925, … Further to Encourage Commercial Aviation", §2: certificates in substitution for surrendered contracts | Congress | Washington, D.C. | FACT (quoted in dc_circ Exhibit C) |
| 1930-10-21 | Route certificate issued to Boeing Air Transport, Incorporated | PMG | — | FACT (dc_circ ¶17 amendment recital) |
| 1931-08-20 / 10-14 | Statement of Evidence lodged with the clerk / filed on appeal to the Tenth Circuit | Boeing Air Transport (plaintiff); Edelman, Weston, Cheyenne, Rock Springs (defendants) | Wyoming | FACT (Edelman record) |
| 1931-1932 | Tenth Circuit reverses in part and directs a writ against the Wyoming gasoline tax on out-of-state fuel used in interstate commerce; certiorari granted (No. 571, October Term 1932) | CCA 10th; then U.S. Supreme Court | Cheyenne / Rock Springs / Washington | FACT of the record; **final disposition not printed in held bytes** |
| 1934-02-09 | Postmaster General's order "purporting to annul the contracts for the carrying of air mail therein designated"; Boeing Air Transport sues, pleading unconstitutional taking | PMG Farley; BAT | Washington, D.C. | FACT of pleading; outcome UNKNOWN |
| 1934-06-20 | UATC stockholders approve the Plan of Reorganization | UATC holders | — | FACT (FY1934 footnote **) |
| 1934-08 | "At the time the company was organized in August, 1934" — month-level formation print for the report addressee | Boeing Airplane Company | Seattle | FACT of the statement; U.002 |
| 1934-08-31 | "the date of reorganization"; net assets taken | — | — | FACT (FY1935 note; FY1934 surplus caption) |
| 1934-09-01 | Consolidated profit-and-loss account begins | — | — | FACT (FY1934) |
| 1934-12-31 | First report: 4-month loss $(225,977.15); 100% of Boeing Aircraft Company and Stearman; 92.62%/90.43% of the Canadian company; Canada "practically dormant"; Stearman's first Navy contract (41 trainers) | Egtvedt, President | Seattle / Wichita / Vancouver | FACT (FY1934, audited by Allen R. Smart & Co., Los Angeles, 1935-03-02) |
| 1935-03-04 | FY1934 report signed | C. L. Egtvedt | — | FACT |
| 1935-07-22 (DERIVED) | Twentieth anniversary of the 1916 subsidiary | — | — | DERIVED; U.003 |
| 1935-08 | Model 299 submitted to the Government "in a competition for bombardment airplanes last August" | Boeing Aircraft Company | Seattle → Dayton | FACT (FY1935); the type's 12-hour 2,040-mile non-stop ferry is printed |
| 1935 (late) | 299 destroyed in an accident before the final flight test; elimination from the competition; order for 13 airplanes and spares received | — | Dayton area / Washington | FACT of the account; cause UNKNOWN |
| 1935-12 | ~28 acres adjoining Boeing Field acquired; UW wind-tunnel rental contract | — | Seattle | FACT (FY1935) |
| 1936-03-09 | FY1935 report signed; auditor's certificate dated 1936-02-26 (Seattle) | Egtvedt; Allen R. Smart & Co. | — | FACT — **and note the audit firm's place changes between 1935 (Los Angeles) and 1936 (Seattle)** |
| 1936 | **No report layer exists in the item** (1936 absent from the 46-layer file list) | — | — | Measured carrier absence; `FETCH REQUEST` #4 |
| 1936-1937 | Plant No. 2 "originally built in 1936 and 1937" | Boeing Aircraft Company | Seattle | FACT (retold in FY1940) |
| 1937-05 (May) | Rights issue to stockholders; 163,847 of 173,424 taken on exercise, 9,577 by underwriters (**COLUMN-REASSEMBLED**) | board; underwriters | — | FACT (fragments); U.014 |
| 1937-07-01 | "it became necessary to increase wages materially in excess of any wage rates previously contemplated" | Boeing Aircraft Company | Seattle | FACT (fragments); M7 |
| 1937-12-31 | Backlog $14,112,298.49; Canada "showed a small profit for the year, its first since 1929"; English-design contract from the Canadian government; Clipper "largest airplane ever constructed in the United States" | — | Vancouver / Seattle | FACT with column-caveat |
| 1938 | Stearman properties taken over; becomes the Stearman Aircraft Division; 55 airplanes delivered; T.W.A. Stratoliner contract terminated with $397,500 down payment retained; six Clippers, ten Stratoliners, 39 Fortresses in manufacture; CAA type certificate for the Clipper; $488,068.14 reserve; bank borrowing; British/Canadian nationality rule announced | Egtvedt | Wichita / Seattle / Vancouver | FACT (FY1938) |
| 1939-03-01 / 03-15 | Backlog 14,664,991.73 / FY1938 report signed | — | — | FACT |
| 1939-03 | Stearman attack bomber "substantially complete" and entered in an Army competition scheduled March 1939 | Stearman Division | Wichita | FACT that it is printed; **result UNKNOWN** |
| 1939-08 | Second four-engine bombardment contract talks: contract of 1937-08 ($9,928,895) delivering at last; a further contract entered **September 1939** for $8,426,190 | USAAC; Boeing Aircraft Company | Seattle | FACT (FY1939) |
| 1939-09-09 | "The present management of your Company undertook its duties on September 9, 1939." | P. G. Johnson succeeding C. L. Egtvedt as President | — | FACT; causation Low (see §N) |
| 1939-09-30 | Accumulated deficit of $3,471,686.29 eliminated against paid-in surplus | — | — | FACT (printed in FY1940's equity caption) |
| 1939-11-24 | Letter to stockholders on the companies' condition as of 1939-09-30; a $5,500,000 loan with RFC participation applied for | management | — | FACT; the letter itself is **not held** (quoted inside FY1939) |
| 1939-12-29 | Special stockholders' meeting: authorised capital 800,000 → 1,250,000 | holders | — | FACT (FY1939, FY1940) |
| 1939 (Q4) | Deliveries resume in volume: ~75% of the 1937 bombardment contract completed between 1939-09 and 1940-03-01; Boeing Air Transport's successor types under CAA test >3 months; temporary certificate of airworthiness granted to the first Stratoliner | — | Seattle / Washington, D.C. | FACT (FY1939) |
| 1940-02 | RFC-participating facility arranged | Pacific National Bank of Seattle (named in the notes); RFC | — | FACT; Medium that the two printings describe one facility |
| 1940-03-01 | $4,740,000.00 drawn | Boeing Aircraft Company | — | FACT |
| 1940-05 | Rights offering, 1-for-2 at $16.00; 360,496 offered; 272,248 on rights; 88,248 to underwriters; net $5,392,547.25; $4,740,000 loan repaid in full; "There are now no encumbrances…" | holders, underwriters | — | FACT (FY1940) |
| 1940-05-24 | Seattle construction contract, 667,000 sq ft, for the Great Britain twin-engine bomber programme | Boeing Aircraft Company | Seattle | FACT |
| 1940-08-01 | Union agreement effective (Local 751 / IAM, AFL), to 1942-07-01, wage re-opening at 1941-07-01; wage increase "approximating eighteen per cent" | Boeing Aircraft Company; the unions | Seattle | FACT |
| 1940-10 | Emergency Plant Facilities contracts with the United States: Seattle ≈$7,625,000 (Boeing Aircraft Company), Wichita ≈$3,625,000 (Stearman Division); 60-month reimbursement | the two companies; the United States | — | FACT (FY1940 + Note 3) |
| 1940-10-15 / 10-16 | Second Seattle contract (≈974,000 sq ft, 140 days) / Wichita contract (420,000 sq ft, 140 days, on purchased land) | — | Seattle / Wichita | FACT |
| 1940-12-31 | Boundary state: gross sales $19,390,718.32; net profit $374,655.29 (of which $163,000 from the accounting change); backlog $196,522,446 with publication barred by federal regulation; 10,886 employees; deficit still $(303,520.30) | — | Seattle / Wichita / Vancouver | FACT (audited) |
| 1941-02-14 / 03-06 / 03-08 / 03-21 / 04-15 | Canadian auditors' report (Vancouver); domestic auditors' report (Seattle); FY1940 report signed (Johnson); notice of annual meeting issued (record date 1941-03-21); meeting at 200 West Michigan Street | two audit firms; P. G. Johnson; H. E. Bowman | Vancouver / Seattle | FACT — these four dates are **post-boundary acts of an in-window report** and are used only to date the documents, never as Stage-1 events |

STATUS: WRITTEN

---

## R. END-OF-STAGE STRUCTURED SNAPSHOT (1940-12-31)

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Legal persons named as part of the group | Boeing Airplane Company (report author); Boeing Aircraft Company, wholly owned, Seattle; Stearman Aircraft Division of the parent, Wichita; Boeing Aircraft of Canada Limited, wholly owned by Boeing Aircraft Company, Vancouver | FY1939 plant schedule; FY1940 opening paragraph | High |
| Which of them is the registrant | **UNKNOWN / contested.** Two readings are held: (i) a company formed August 1934 to acquire assets of a dissolved group; (ii) `(PB)` a 1996 recital of one person "originally incorporated in Washington in 1916 and … reincorporated in Delaware in 1934" | FY1934/35/38; S-4 1996 | U.001, U.002 — the dossier's central conflict, unresolved on held evidence |
| Own name on the securities register | "BOEING AIRPLANE CO" until an EDGAR conformed-name change printed as **1973-07-25** `(PB)`; the 1916 name and the 1934 name are not tied by any held byte | SEC header field, 26 of 33 held files | High (of printing) / Medium (of legal meaning); U.009 |
| Capital | 1,250,000 authorised at $5.00 par; 1,081,673¾ issued and outstanding; 780¼ shares still to be issued against **United Aircraft & Transport Corporation** certificates presented for exchange; paid-in surplus $4,507,270.96; accumulated deficit $(303,520.30) | FY1940 balance sheet | High — and the 780¼ shares are the single best held witness that the 1929 group's register was still feeding this company's register six years after its dissolution |
| Listed / regulated | Transfer agent and registrar in New York since 1934; "Complying with New York Stock Exchange requirements" (FY1935 depreciation-rate note); proxy solicitation "Pursuant to the regulations of the Securities and Exchange Commission" (FY1940 proxy statement, for a 1941 meeting) | FY1934, FY1935, FY1940 | High (printed) — note the sequence: NYSE compliance language in 1935, an SEC-regulation proxy in 1941, and no Exchange Act registration document of any kind in the corpus |
| Production system | Three plants, ≈2,344,500 sq ft at Seattle (three plants), ≈740,000 sq ft at Wichita, ~200,000 sq ft Government-built leased plant at Vancouver under way; 10,886 employees; peak of "in excess of 20,000" anticipated for 1941 | FY1940 | High |
| Order book | $196,522,446 (U.S. units), composition legally withholdable; a further "additional new business … during 1941, for delivery in 1942 and 1943" anticipated | FY1940 | High (figure) / **NOT KNOWABLE** (composition) |
| Products in hand | Four-engine bombardment types (Fortress lineage, with parts now made at Wichita); primary trainers (Stearman); two-engine flying boats and airplane parts for the Canadian Government; six Clippers under option for 1941 delivery; Stratoliner deliveries completed at Seattle in 1940; a Great Britain twin-engine bomber programme | FY1940 | High |
| Money position | Cash $11,330,223.92 + restricted $685,329.98; no encumbrances on properties (after repaying $4,740,000); emergency-facility borrowing $2,240,445.62 with bank recourse confined to Government payments; advance payments from the United States and Great Britain | FY1940 | High |
| First profit, and its quality | Net $374,655.29; $163,000 of pre-tax income attributed by the auditors to a change of accounting policy; consolidation basis changed the same year (Canada excluded); a $640,000 provision and a forecast further loss of ≈$500,000 on the option Clippers | FY1940, Note 1, auditors | High — **U.012** |
| Open liabilities inherited | Joint-and-several guaranty of UATC's known and unknown liabilities, provisioned $81,500.00 (against a 1935 estimate of ≈$15,000 for the company's 14.1155% share); Canadian preferred arrears C$231,730.00 | FY1934, FY1935, FY1940 | High |
| Labour | One union agreement, effective 1940-08-01 to 1942-07-01, wage re-openable 1941-07-01, ≈18% increase attributed to it | FY1940 | High; disputes/relations history UNKNOWN (NLRB family untried) |
| Validation held | Two contracts, a type certificate, an exercised option at higher prices, an oversubscribed-by-underwriters rights issue, an RFC-participating loan arranged and then retired, and a federal mail clerk's testimony from 1931 | §L | mixed confidence per row |
| What the archive cannot tell anyone at this date | Every 1916-1933 fact; every rejected alternative at the 1929, 1934, 1938-39 forks; the founders' personal finances; the outcome of the two held lawsuits; the composition of the 1940 backlog; unit economics; the origin of the name "Boeing" in the corporate mind | §S | — |

STATUS: WRITTEN

---

## S. DATA GAPS

**Every gap below names the route that could close it** (§13: a High-importance gap without a follow-up task
is an open research-debt violation). `UNTRIED` means never attempted by any pass; `UNANSWERED` means a tool
or network refused; `TRIED–ANSWERED (null)` means searched over held bytes with a measured result.

| Gap | Why missing | Importance | Best available evidence | Confidence | Follow-up task |
|---|---|---|---|---|---|
| **The 1916-1925 record is absent from every family** — no instrument, no name of the original corporation, no first flight, no first customer, no capital | Families (a) EDGAR floor 1994-03-15, (b) web archives mid-1990s, (c)/(d) returned in-window text only from 1927 onward, (e) never reached | **High** | FY1934's "since 1916" (self-claim, attached to a subsidiary) and FY1935's anniversary sentence | High (that nothing is held) | `## Untried` #2 (auction/museum/manuscript — the route most likely to change the verdict) and #6 (44 unopened in-window IA items) |
| **Which legal person the 1916 year belongs to, and whether it is the registrant** | The two readings are printed in different carriers and no held byte conjoins them | **High** | FY1934 ¶3; FY1935 ¶1; dc_circ route-certificate recital ("Boeing Airplane Company, Incorporated, of Seattle, Washington, a corporation duly organized and existing under the laws of the State of Washington"); `(PB)` 1996/1998 recital | U.001 is the conflict record | Charter/registry search: Washington Secretary of State and Delaware Division of Corporations — **no tool in `tools/` reaches either**; a web budget is required |
| **The 1929 United Aircraft & Transport step as an act** — date, instrument, what was exchanged, what happened to the 1916 company's name | The only in-window witnesses are indirect: the 1934 guaranty and share-exchange captions, the 1934 management agreement reciting UATC as "a corporation of the State of Delaware", and one **party assertion** in the 1934 record | **High** | FY1934 footnotes *, **; dc_circ recitals and brief passage | Medium (that UATC controlled the operators); UNKNOWN (the 1929 act itself) | Aeronautics Branch / ICC and Delaware charter series (`## Untried` #3); the munitions volume's aircraft hearings were read only as counted greps |
| **The 1936 report is not in the IA item** | The item's per-year layers are 1934, 1934a, 1935, 1937-1978 | Medium-High (it is the year the Clipper/Stratoliner decisions and the 600,000→800,000 capital step most likely appear) | FY1940's "originally built in 1936 and 1937"; FY1935's forecast of a 1936 asset acquisition | High (that the layer is absent from the enumerated file list) | `FETCH REQUEST` #4 — re-enumerate the item's file list to confirm 1936 is absent rather than un-listed |
| **No adjudicated outcome for either held lawsuit** | Both volumes are records/briefs; no reporter volume is held | **High** for the litigation's meaning in-window | dc_circ: 0 hits for a disposition string; Edelman: 0 hits for `289 U.S.`, but the Tenth Circuit's own text is reproduced | High (of the null over held bytes) | Reporter citation pass (F.2d / U.S. Reports) — web budget required; `FETCH REQUEST` #2 |
| **Founder's personal finances, role, departure** | No held byte names him as an officer/director of the reporting companies, or states any figure | **High** (§K is mandatory at every tier) | dc_circ affidavit + signature blocks only | High (of absence in held bytes) | Family (e); the same route |
| **FY1937 financial statements** | Column-interleaved OCR destroys the tables | Medium | Only 4 legible fragments | n/a — **UNANSWERED by this layer**, not absent from the world | `FETCH REQUEST` #3 (page images or re-OCR) |
| **Unit prices, margins, per-airplane economics for 1934-1940** | Never printed; only aggregate contracts, backlog and customer-class delivery totals | High | FY1940's delivery split, which foots to gross sales | High (of absence) | Contract files (Aeronautics Branch/CAB/contract series), untried |
| **Headcount 1934-1939** | Only 1940 counts and 1940 increases are printed | Medium | FY1940 §Personnel | High | Same as above; company employment records untried |
| **Competitive set for 1934-40 aircraft contracts** | No rival manufacturer is named in any held in-window file (`Curtiss` ×1 in a volume containing 0 "Boeing") | High | 1927 four-bidder field only | High | `## Untried` #3/#6/#8 |
| **Certification specifics** — certificate numbers, dates, weights | The company prints that certificates issued, not which | Medium | FY1938 (Clipper ATC), FY1939 (Stratoliner temporary C of A) | High (of the events) | Civil Aeronautics authority series, untried |
| **The date the company became "The Boeing Company"** | `(PB)` EDGAR prints a conformed-name change of 1973-07-25; the FY1945 layer still prints "Boeing Airplane Company" and the FY1976 layer prints "The Boeing Company"; no held byte prints a renaming act or the year 1960 as such | **High** for Stage-2 boundary design | header field, 26 printings | U.009 | The 39 unopened 1941-1978 corporate-print layers — the cheapest move on the board, per-file route already proven by the 46,004 B FY1945 fetch |
| **Whether Boeing Air Transport, Inc. survived 1934** | Nothing printed | Medium-High (it is the operating arm of the 1927 win) | dc_circ only | High (of silence) | United Air Lines / Delaware records, untried |
| **Any wage dispute, stoppage or board case** | Only the employer's own 1940 agreement is printed | Medium | FY1940 §Management | High | NLRB case registers, `## Untried` #4 |
| **The record-selection null itself (§2)** | Winners' archive: no rejected option, no internal minute, no contemporaneous third-party count behind any self-reported "leaders"/"65 million miles"/"finest in their classes" claim | **High**, structural | — | — | Only an untried family (e) or a non-company archive could supply the counter-record |

STATUS: WRITTEN

---

## T. SOURCE / PROVENANCE TABLE

| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| `sources/corporate_print/boeing1934_djvu.txt` (12,430 B) — *Boeing Airplane Company and Subsidiary Companies, Report to Stockholders, Four Months Ended December 31, 1934*, signed C. L. Egtvedt 1935-03-04; audited Allen R. Smart & Co., **Los Angeles**, 1935-03-02 | digitised corporate print (company report) | Primary | 1934-12-31 | 1935-03 (print) | archive.org/download/boeingairplanecompanyannualreports/boeing1934_djvu.txt | 1 | High that it is the company's own print; **unverified TLS** per its sidecar (`ok-INSECURE`) → capped at Medium-High until re-checked |
| `boeing1934a_djvu.txt` (6,122 B) — **Hamilton Metalplane advertising brochure**, undated; footer "DIVISION / BOEING AIRPLANE COMPANY / Division of United Aircraft and Transport Corp. / Milwaukee, Wisconsin" | digitised trade print inside the same IA item | Primary (as an artefact), **not** a company report | UNKNOWN | UNKNOWN | …/boeing1934a_djvu.txt | 3 | High that it is not a report; U.014 |
| `boeing1935_djvu.txt` (16,394 B) — FY1935 report, signed 1936-03-09; auditors' certificate **Seattle** 1936-02-26; final page "PROGRESS" chronology | company report | Primary | 1935-12-31 | 1936-03-09 | …/boeing1935_djvu.txt | 1 | High |
| `boeing1937_djvu.txt` (20,844 B) — FY1937 report | company report | Primary | 1937-12-31 | 1938 | …/boeing1937_djvu.txt | 1 | **Layer degraded**: two-column + rotated-table interleaving; only fragments readable (see §P withheld rows) |
| `boeing1938_djvu.txt` (23,332 B) — FY1938 report, signed 1939-03-15 | company report | Primary | 1938-12-31 | 1939-03-15 | …/boeing1938_djvu.txt | 1 | High |
| `boeing1939_djvu.txt` (25,088 B) — FY1939 report, signed **P. G. Johnson**; contains the 1940-02/03-01 loan updates and quotes the 1939-11-24 stockholder letter | company report | Primary | 1939-12-31 | 1940 | …/boeing1939_djvu.txt | 1 | High — and note the 1939-11-24 letter itself is **not held**, only quoted |
| `boeing1940_djvu.txt` (33,308 B) — FY1940 report + notice of annual meeting (1941-03-21) + proxy statement + domestic statements + separate Canadian statements in C$; auditors 1941-03-06 (Seattle), Canadian auditors 1941-02-14 (Vancouver) | company report + proxy | Primary | 1940-12-31 | 1941-03-08 | …/boeing1940_djvu.txt | 1 | High |
| `sources/periodicals/dc_circ_1934_6287_boeng_air_transp_v_farley_djvu.txt` (625,596 B) — *Boeing Air Transport, Inc. et al. v. Farley*, D.C. Circuit 1934: bill of complaint, exhibits (Route A.M. 18 bid papers, contract and bond forms, the 1930 route certificate and its ¶17 amendment), the sub-contract and founder's oath, briefs | digitised government / judicial print | Primary (record), Secondary (advocate's briefs) | 1927-1934 | 1934 | archive.org/download/dc_circ_1934_6287_boeng_air_transp_v_farley/…_djvu.txt | 1 | High for the federal papers it contains; **no disposition in the volume**; unverified TLS |
| `micro_IA40386008_0350_djvu.txt` (493,539 B) — *Edelman v. Boeing Air Transport, Inc.* record: pleadings, stipulations, Statement of Evidence (lodged 1931-08-20, filed 1931-10-14), CCA opinion text, petition for certiorari (No. 571, October Term 1932), municipal airport contracts with Cheyenne and Rock Springs | judicial print | Primary (record) | 1930-1932 | 1932-33 | archive.org/download/micro_IA40386008_0350/… | 1 | High; the case is a **Wyoming gasoline-tax** matter, not an air-mail matter — see U.016; unverified TLS |
| `sim_aviation-week-space-technology_1916-08-01_1_1_djvu.txt` (149,954 B) | trade periodical | Secondary | 1916-08-01 | 1916-08-01 | archive.org/download/sim_… | 3 | **Content-verified NULL**: `Boeing` 0 occurrences in 149,286 chars (re-measured this pass); 40 `1916` hits are date strings; 1 `Hubbard` hit is "J. F. Hubbard" in a roster |
| `munitionsindustr1114unit_djvu.txt` (4,594,867 B) — Senate munitions-industry volume, 1934 | government print | Secondary | 1934 | 1934 | archive.org/download/munitionsindustr1114unit/… | 2 | **Content-verified NULL** for this company: `Boeing` 0, `Seattle` 0 (re-measured); controls `Senate` 68, `aircraft` 16, `Wright` 10; the corpus's only `antitrust` occurrence is here |
| `boeingairplanecompanyannualreports__boeing1945_djvu.txt` (46,004 B) — **first company-issued layer fetched to its own path by the per-file route**, FY1945 report | company report | Primary | 1945-12-31 | 1946 | archive.org/download/boeingairplanecompanyannualreports/boeing1945_djvu.txt | 1 | **(PB)** — and measured: `1916` ×0, `since 19` ×0, `incorporat*` ×0, `The Boeing Company` ×0; still "Boeing Airplane Company" ×5 |
| `boeingairplanecompanyannualreports_djvu.txt` (99,175 B) — item-level layer = the **FY1976** report | company report | Primary | 1976-12-31 | 1977 | sidecar `url` field reads `…/boeing1976_djvu.txt` while the file is saved under the item-level name | 1 | **(PB)**; `1916` ×0; "The Boeing Company" ×2 (Touch Ross & Co. report, Vancouver/Seattle); the layer's only `since 19` is "first order from United since 1967" |
| 12 × `NASA_NTRS_Archive_*_djvu.txt` (2.55 MB aggregate) | government/technical periodical | Secondary | 1952-1977 | 1973-2005 | archive.org items per sidecars | 3 | **Out of window for Stage 1.** All are `TIER1_CANDIDATE_TEXT` or `BARE_WORD_MATCH` in `research/A4_harvest_mine.md`; entity hits are 1970s-80s divisions ("Boeing Vertol", "Boeing Aerospace", "Boeing Commercial Airplane Company"). Cited only for U.016 (the modern name's third-party printings) |
| 33 × `sources/sec/*.txt` (7,170,562 B), 1994-03-15 → 2002 | EDGAR filings + SGML header blocks | Primary (as to their own contents) | 1994-2002 | same | sec.gov CIK 0000012927 | 1 | **(PB) for every Stage-1 claim** except the two recitals (U.001, U.009) and the header field; earliest held `DEF 14A` acc. 0000012927-94-000001 |
| `sources/_index/submissions_CIK0000012927.csv` (4,026 rows) | regulatory index | Secondary | — | 2026-10-07 | EDGAR submissions | 1 | **Index rows are filing facts, not evidence of content** (§3) |

**Provenance defects observed on this pass (recorded, not routed around):**

1. **The IA item is not homogeneous.** `boeingairplanecompanyannualreports` has 46 per-year text layers, so
   "one item, one layer per year" is a correct **file** census but a wrong **document** census: `boeing1934a`
   is a Hamilton Metalplane advertisement, not a second 1934 report. Any chronology built from filenames
   without reading the first page will mis-file an advertisement as a filing. (This resolves the probe's open
   question "did not check whether the 1934a part duplicates 1934" — **it does not; it is a different
   document type**.)
2. **Sidecar `url`/filename mismatch** on the FY1976 layer (saved as the item-level name, fetched from
   `boeing1976_djvu.txt`) — a merge-census hazard.
3. **`sources/sec/_MANIFEST.csv` now contains a header row and 0 data rows** (`wc -l` = 1), although the
   probe recorded 37 rows and 33 `.txt` documents plus 37 sidecars are on disk. The manifest was rewritten
   after the probe (directory mtimes 2026-10-07T02:37). I did **not** modify it (§14 rule 4). Reported to the
   orchestrator as an intake-state regression: the held-SEC list is currently unenumerated on disk, so
   "which 33 files are held and what forms they are" must be re-derived from filenames.
4. **OCR name decoys resolved inside one held file.** FY1940's proxy statement prints
   "**FAUL** PIGOTT is President of Pacific Car & Foundry Company", while the same file's Board of Directors
   page prints "**PAUL** PIGOTT … Seattle, Washington". The F/P substitution is therefore demonstrable
   **within one document**, and I record the name as printed in the proxy and note the board-page witness;
   I do not silently correct either. Similarly FY1939 renders the auditors as "**Align** R. Smart & Co."
   where four other layers print "Allen R. Smart & Co."
5. **Audit-scope language is not a clean opinion** in any held year: "we did not make a detailed audit of
   the transactions" (1934, 1935, 1938-39 pattern), escalating in FY1940 to "by methods, at times, and to the
   extent we deemed appropriate", plus explicit non-contrast disclosure that the 1940 basis excluded Canada
   and re-capitalised $163,000. Every §P figure is therefore audited-adjacent, not audited-clean.

STATUS: WRITTEN

---

## U. CONFLICTING EVIDENCE

**Anchors U.001-U.017 are declared in the Header block.** Each has at least one register row in
`conflicts.csv`; parity is the merge's to prove. Format per §7: CLAIM A / CLAIM B / WHY THEY DIFFER /
EVIDENCE WEIGHT / BEST-SUPPORTED INTERPRETATION / RESIDUAL UNCERTAINTY / CONFIDENCE.

### U.001 — Which person "1916" is the registrant's, and whether it is the registrant's at all
**CLAIM A** (in-window, company print): the 1916 date belongs to *another* corporation — "Boeing Aircraft
Company, a Washington corporation, has been engaged in the manufacture of aircraft since 1916", 100% owned by
the report's addressee, which "was formed for the purpose of acquiring these assets upon the dissolution of
United Aircraft & Transport Corporation" (FY1934); FY1935 repeats the anniversary for "this subsidiary".
**CLAIM B** (`(PB)`, the registrant's own later boilerplate): "Boeing was originally incorporated in
Washington in 1916 and was reincorporated in Delaware in 1934" — one continuous person (1996 S-4; 1998 S-4/A).
**CLAIM C** (in-window, federal record, and the sharpest): the 1927 contract party is recited as "**Boeing
Airplane Company, Incorporated**, of Seattle, Washington, a corporation duly organized and existing under the
laws of the **State of Washington**" — i.e. the *name* the 1934 report reserves to the newly formed
(Seattle, New York-transfer-agent) company is used in 1927 of a **Washington** corporation, while the 1934
report attaches 1916 to a corporation named **Boeing Aircraft Company**.
**WHY THEY DIFFER.** Three different carriers use two similar names for two or three persons, across a
1929-1934 partition in which names were reused by the separated pieces. A is the company describing its own
formation, 8 months after it; B is the same institution describing itself 62 years later, compressed; C is a
federal pleading quoting a 1927 contract. None is a charter.
**EVIDENCE WEIGHT.** A and C are in-window Tier-1; A is self-narrative (one lineage, two document years — the
"×2" is not two corroborations, per the probe's C-2). B is a retrospective recital and cannot witness a
1916 act. C is third-party paper but is *naming* a party, not describing an incorporation.
**BEST-SUPPORTED INTERPRETATION.** The held bytes support: **1916 is a year a Boeing-named Washington
manufacturing corporation was operating; 1934 is the year the reporting company began; and no held document
says the two are one person.** The dossier therefore writes the origin as a **split**, never as "founded
1916", and never as "founded 1934" either — the second is only the reporting company's own start.
**RESIDUAL UNCERTAINTY.** Whether "Boeing Aircraft Company" (1934 print) is the renamed survivor of the
1927 "Boeing Airplane Company", or whether the 1934 holding took the older name while the operating company
took the newer one — both are consistent with the bytes and **neither is testable from them**. Routes:
Washington and Delaware charter records; family (e).
**CONFIDENCE.** High that the conflict is real and unresolved; **UNKNOWN** for the resolution.

### U.002 — The reporting company's own formation date
FY1934 "formed … upon the dissolution", account "dates from September 1, 1934", net assets taken "at August
31, 1934"; FY1935 "On August 31, 1934, **the date of reorganization**"; FY1938 "organized in **August,
1934**". Four printings, one lineage, mutually consistent at month level, none at day level, and none states
an incorporation act. **Best reading:** formation in August 1934 with accounting effect from September 1,
1934. **Residual:** the day, the state, and the filing of the certificate are UNKNOWN (not printed in any of
the seven layers). **Confidence** High (month), Medium (the 09-01 accounting start is a fiscal convention, not
an act).

### U.003 — The 1916 day-month
FY1935: "The twentieth anniversary of this subsidiary will occur July 22 of this year" (report signed
1936-03-09) → **1916-07-22** by subtraction. Against this: the string `July 22, 1916` occurs **0** times and
the string `since 1916` once, in FY1934; **no held byte of any family prints 1916-07-15** (the folk date in
the brief's framing) — that date is *unheld*, not contradicted. **Why they differ** — a self-narrated
anniversary is not a charter; an anniversary can mark a first flight, a first contract, a renaming or a
partnership. **Best-supported:** the company in 1936 believed the subsidiary's birthday was July 22, and it
printed it because shareholders would test it. **Residual:** what event July 22, 1916 marks. **Confidence**
Medium (derived, single lineage, retrospective at 20 years).

### U.004 — Award date of Route A.M. 18, inside one volume
**A**: "awarded **under date of January 29, 1927**" (court's statement of facts; repeated in a brief: "Route
No. 18 was awarded under date of January 29, 1927"). **B**: "on or about **February 1, 1927**, the then
Postmaster General … awarded the contract" (verified Bill ¶7). **C**: the parties "on the **1st day of
February, 1927**, duly entered into a contract" (route-certificate recital). **Why they differ:** a 1934
pleading's paraphrase of an award memorandum versus the executed contract's own date; "on or about" is the
pleader's hedge. **Weight:** all three strings are in one held Tier-1 volume — so this is a **within-carrier**
conflict and cannot be resolved by adding the same record again. **Best reading:** the instrument is dated
February 1, 1927 and the departmental award action is stated elsewhere as January 29, 1927; the
certificate-of-award date is not resolvable from this volume. **Residual:** which date a registry would
record. **Confidence** High (that all three print); Low (single true date).

### U.005 — "lowest qualified bidder" vs "lowest responsible bidders"
Same award, two wordings, both inside the dc_circ volume (Bill ¶7; court's facts). **Why they differ:** the
statute's standard (Sections 425-427 of Title 39) is being recited in two registers — a pleading and a
judicial summary — and one is plural because it names the corporation and Hubbard together. **Weight:**
third-party federal paper either way. **Best reading:** the award rested on being lowest **and**
tendering sufficient guarantees, and the singular/plural difference is not a substantive conflict.
**Residual:** whether "qualified" and "responsible" were different statutory tests at the time — no held byte
quotes the standard. **Confidence** Medium.

### U.006 — The 1939-12-31 backlog, two ways
**A**: FY1939 prints unfilled orders at 1939-12-31 of **$23,002,574**, "your Company and its subsidiaries",
including "approximately $900,000 (Canadian dollars)" of the Dominion of Canada contract. **B**: FY1940
prints unfilled orders "under contract to the Company's units **in the United States**" at 1940-12-31 of
$196,522,446, "an increase of $174,392,821 over unfilled orders at the close of the year 1939" — implying a
1939 base of **$22,129,625** (DERIVED), **$872,949** below A. **Why they differ:** scope, not arithmetic —
B is domestic-only, and A includes a Canadian item of ≈C$900,000; the gap's size matching that item's size is
suggestive, and the currencies are **not** the same, so it is not a reconciliation. **Weight:** both are the
company's own printings; they are one lineage, and B additionally post-dates the 1940 deconsolidation of
Canada. **Best-supported interpretation:** report both figures with their scope labels; do **not** average,
do not restate A onto a domestic basis, and do not treat the near-match to the Canadian item as proof.
**Residual uncertainty:** whether the entire $872,949 is the Canadian contract, and what exchange rate the
company would have used; the FY1940 note never says. **Confidence** High (both figures printed), Low (any
single reconciled number — none is offered).

### U.007 — FY1935's share sub-captions do not foot
`491,365½ + 30,517¾ = 521,883¼ ≠ 521,883`. **Why they differ:** OCR fraction glyphs (halves rendered `%`,
quarters `^4`) are destroyed in this layer; the FY1934 pair (`442,402½ + 79,480½ = 521,883`) and the FY1940
pair (`1,081,673¾ × $5.00 = $5,408,368.75`) both foot exactly, so the defect is local. **Weight:** audited
caption, one printing. **Best reading:** the total 521,883 stands (printed in FY1934 and FY1935 and footed
there); the 1935 split is **UNKNOWN** at the fraction. **No third number is substituted.** **Confidence**
High (total), Medium (the split's whole-share part).

### U.008 — The 1938 report mis-quotes the 1934 report
FY1938 puts in quotation marks, with ellipses, a sentence it attributes to "The 1934 report stated". Against
the held FY1934 bytes the quotation changes "fairly substantial" to "substantial", deletes "based upon their
many years of experience", and drops the qualifying clause about "those fields which hold forth promise of
producing future business". **Why they differ:** a restatement compressed for effect — a hedge removed inside
ellipsis marks. **Weight:** both documents held on one shelf; the discrepancy is measured, not inferred, and
no outside source is involved. **Best-supported interpretation:** cite FY1934 for the hedged sentence and
record FY1938's version as a **restatement with a strengthened claim**; do not use FY1938's quotation as the
1934 text. **Residual:** whether other in-print quotations of earlier reports elsewhere in the seven layers
are also non-verbatim — only this one was checked against a held original (the FY1937 quotation in FY1938,
"By reason of the large development cost…", is attributed to a report whose legible columns are damaged, so
it **cannot** be tested). **Confidence** High.

### U.009 — The renaming date
**A**: EDGAR's registrant header prints `FORMER CONFORMED NAME: BOEING AIRPLANE CO`,
`DATE OF NAME CHANGE: 19730725` — **26 printings** across 33 held filings (1994-03-15 → 2002). **B**: the
brief's framing that the renaming happened in **1960**; no held byte supports 1960 (the FY1976 layer's two
`1960` occurrences are the 727 programme start; `renamed`/`changed its name` = 0 in both post-boundary
layers; FY1945 still prints "Boeing Airplane Company" ×5 and has no origin recital). **Why they differ:** one
is a securities-registry field recording when the conformed name on the registrant's entry changed; the other
is a corporate-history claim about a charter act; a company may change its name on its charter years before
the registry's conformed-name record reflects it, or the field may be recording a later administrative
change. **Weight:** A is Tier-1 registry data re-printed mechanically (one record, many printings — **not 26
corroborations**); B is unheld. **Best-supported interpretation:** "The registrant's EDGAR conformed name
changed from BOEING AIRPLANE CO on 1973-07-25; the corporate act and its date are UNKNOWN, bounded by held
print to after FY1945 and by/at FY1976." **Residual:** the whole 1946-1976 range; the 39 unopened layers
would close it. **Confidence** High (A's printing), Low (A as the act).

### U.010 — Motive for the 1934-38 structural reorganisation
**A**: the company states tax and administrative simplification, three times (FY1934 "to simplify management
and taxation problems"; FY1937 **COLUMN-REASSEMBLED** "in line with the current trend toward the elimination
of holding companies and the simplification of corporate structures"; FY1938 "Your directors intend, as soon
as it is deemed practical, to further simplify the corporate structure"). **B**: the framing in the dispatch
brief treats the 1934-38 reorganisation as antitrust-driven. **WHY THEY DIFFER:** B is a later historical
account of federal policy pressure; A is the issuer's own stated reason in a document written to
stockholders. **EVIDENCE WEIGHT:** "antitrust" occurs **0** times adjacent to any Boeing naming in all 25
held text files (its one occurrence anywhere is in a volume where "Boeing" occurs 0 times); "Sherman Act" 0;
"Public Utility" 0; "income protection" 0; "Pujo" 0. Nothing in-window connects the split to antitrust
enforcement, and the one regulatory instrument the corpus does print is a **postal** statute (the Act of
April 29, 1930, quoted in the route certificate) and the February 9, 1934 annulment order.
**BEST-SUPPORTED INTERPRETATION:** record the split's *stated* motive as tax/simplification/industry trend;
record any antitrust motive as **UNTRIED** — a motive the corpus does not reach, not a motive the corpus
denies. **RESIDUAL UNCERTAINTY:** the whole question of why UATC was dissolved; the company's own
1934 letter says only that the company "was formed for the purpose of acquiring these assets upon the
dissolution", which is a description, not a cause. **CONFIDENCE** High (that the bytes contain no antitrust
motive); UNKNOWN (the actual motive).

### U.011 — Counting basis, and what a "name count" can prove
The probe reported, case-insensitively and over 12 files, `Boeing Air Transport` 145 / `Boeing Airplane
Company` 61 / `Boeing Aircraft Company` 51. This pass re-measured with **case-sensitive exact-phrase** counts
over the 25 held non-SEC text files: **89 / 43 / 61**. **Why they differ:** case, file population (12 vs 25),
and the probe's own warning that raw counters include substring noise. **Evidence weight:** neither is a
naming census — a matched string is a lead, and only a read line is evidence (RD-124). Demonstrated in this
corpus: `William` 497 in the probe's raw counter vs 403 of them sitting in a volume containing no "Boeing";
`1917` 408 vs 406 in that same volume; `ATTA` matching hundreds of times as a substring in unrelated OCR;
`West` 33/50 in the two court volumes resolving to street names, state names, case citations and a **Weston**;
`Green` 6/12 resolving to a rival carrier's secretary, a Wyoming attorney-general and a river; `Montreal` 0;
`B & W` 0; `Westhoff` 0. **Best-supported interpretation:** registers carry **read-line namings** with their
entity adjacency quoted; every count published in a dossier states its command and its file population.
**Residual:** whether a case-insensitive census would surface a naming this one missed — possible; the
method note in the sources register says which rows are case-insensitive. **Confidence** High (both
measurements are reproducible).

### U.012 — The 1940 profit, three descriptions
**A**: management: "Operations of the domestic companies resulted in a net profit… of $374,655.29", the first
in the window, with deliveries in 1940 exceeding "the total deliveries during the preceding three years", and
the accounting change described as having "the desirable effect" of matching cost and income. **B**: the
auditors, same document: the change means "the net income before income taxes for the year then ended … are
approximately $163,000.00 more than they would have been had the former accounting principles been
maintained", plus "The principle of consolidation … was changed for the year 1940 in that the Canadian
Subsidiary … is excluded". **C**: the company's own Note 1: a $640,000.00 Clipper provision and "It is
estimated that the Company may sustain a further loss subsequent to December 31, 1940, in the approximate
amount of $500,000.00". **Why they differ:** not in fact but in framing; all three are consistent on the
numbers and all are in one document. **Evidence weight:** the issuer's narrative and its auditors'
qualifications carry equal authority here precisely because the auditors wrote the number themselves.
**Best-supported interpretation:** report the first profit as **$374,655.29 net, of which $163,000 pre-tax is
attributable by the auditors to a change of policy (28.9% of pre-tax income, DERIVED), on a basis that also
excluded Canada and still carried a $(303,520.30) accumulated deficit and a forecast further Clipper loss.**
**Residual:** whether the change was permitted, required, or chosen; the auditors state it without endorsing
it. **Confidence** High.

### U.013 — W. E. Boeing's presence in the record
**A**: the founder is the corpus's only sworn personal voice — the D.C. record's oath and four signature
blocks, as President of **Boeing Air Transport, Inc.** **B**: he is absent from every governance list in all
seven corporate-print layers, including the two that name the subsidiary's president (Egtvedt, 1934) and the
one that prints nine directors with their share counts (1940). **Why they differ:** they describe different
corporations — A is the air-transport person, B the manufacturer/holding persons — and the corpus contains no
byte that connects the two roles. **Weight:** A is Tier-1 sworn; B is Tier-1 self-print. Neither contradicts
the other. **Best-supported interpretation:** "a person of the founder's name is documented as an officer of
one Boeing corporation in the 1927-34 air-mail record, and is not documented as an officer or director of the
reporting companies or their operating subsidiaries in 1934-40." **Residual:** his role, shareholding and
any departure terms — **UNKNOWN**, family (e). **Confidence** High (both legs), UNKNOWN (the synthesis).

### U.014 — Document identity inside one archive item
`boeing1934a_djvu.txt` is a **Hamilton Metalplane advertising brochure**, undated, whose footer reads
"DIVISION / BOEING AIRPLANE COMPANY / Division of United Aircraft and Transport Corp. / Milwaukee,
Wisconsin", and whose internal data conflict with themselves ("Specifications for **H-45**" heading the
**H-15** table; "No. of seats—**Eight**" against "Six passengers with pilot and navigator may he
accommodated"). **Why this is a conflict, not a curiosity:** the name "Boeing Airplane Company" appears here
attaching to a **Milwaukee** division subordinate to UATC, which is a **third** referent beside U.001's two —
and it is undated, so it cannot be placed in the chronology at all. **Weight:** one artefact, primary as an
artefact, worthless as a dating witness. **Best-supported interpretation:** hold it as evidence that the
*name* was used of a UATC division, date UNKNOWN, and exclude it from every count of "reports held" (this
dossier counts **six** in-window company reports, not seven). **Residual:** the brochure's year; whether it
was bound with the reports by the company, a library or the digitiser. **Confidence** High (that it is not a
report); UNKNOWN (date).

### U.015 — The four noise families and what each actually resolves to
`Boeing`, `West`, `Green`, `C & F` were declared noise sources in the dispatch brief; this pass tested each.
**West** → street addresses ("105 West Adams Street, Chicago", "200 West Michigan Street"), case names
("Pennsylvania v. West Va.", "West River Bridge Co. v. Dix", "West Virginia"), a carrier
("Transcontinental & **Western** Air"), public-land meridians, and — the dangerous one — the Wyoming
defendant **Harry R. Weston**. **Green** → "C. H. GREEN, Secretary" of **Pacific Air Transport**, the
citation *Greenhow v. Poindexter*, "J. A. Greenwood, Attorney General of the State of Wyoming", and the
"Green River water supply". **C & F** → 0 occurrences; the only nearby naming is **Pacific Car & Foundry
Company**, whose president sits on the board (proxy print "FAUL PIGOTT", board print "PAUL PIGOTT" — a same-
document OCR witness, §T defect 4). **Boeing** → 816 raw occurrences across the 25 held files, of which the
in-window *corporate* namings are 61 (Airplane) + 18 (Aircraft) + 33 (Canada) + 89 (Air Transport) as read
lines, and the remainder are the modern registrant, NASA 1970s divisions, and 71 in the FY1945 layer.
**Best-supported interpretation:** no naming is promoted without the entity word adjacent to a verb of being,
acting or contracting, and a place check (Wichita / Seattle / Vancouver) — **Montreal names nothing in this
corpus**. **Residual:** the OCR-garbled first name of the Pacific Car & Foundry director is recorded as
printed. **Confidence** High.

### U.016 — "The Boeing Company" and "Boeing Company" as names, and the 1933 record's real subject
**A**: 25 occurrences of "The Boeing Company" and 64 of "Boeing Company" exist in held bytes, which would
licence a careless reader to date the modern name into the window or to treat the Wyoming record as an
air-mail record. **B**: the 25 "The Boeing Company" hits are in 1970s NASA layers and the FY1976 report — all
out of window; and in the 1933 Wyoming volume "Boeing Company" is a **defined term of a municipal airport
lease**: the corporation "authorized to transact business within the State of Wyoming, hereinafter called
'Boeing Company,' party of the second part", used by the **federal mail transfer clerk** in testimony ("I
deliver the mail to the employee of the Boeing Company"). The volume itself is a **Wyoming gasoline-tax**
suit against the State Treasurer and the Cities of Cheyenne and Rock Springs, in which the Tenth Circuit
reversed in part on the out-of-state-fuel question; its air-mail content is incidental. **Why they differ:**
a contract's shorthand and a digitiser's anachronism, neither of which is a corporate naming event.
**Weight:** Edelman's "Boeing Air Transport" ×28 is real; its "Boeing Company" is a lease definition.
**Best-supported interpretation:** registers cite the Edelman volume as (i) evidence that a Washington
corporation operated an "airplane line extending from Chicago … to San Francisco" under municipal lease at
Cheyenne and Rock Springs, and (ii) a third-party federal employee's testimony of mail handling — **not** as
evidence about the registrant's origin and **not** as an air-mail contract record. **Residual:** the final
Supreme Court disposition, unprinted. **Confidence** High.

### U.017 — Who terminated the T.W.A. Stratoliner contract
**A** (FY1938): "a **termination by Boeing** of its contract with Transcontinental & Western Air, Inc." with
"a down payment of $397,500 … retained as security against possible damages". **B** (same sentence family):
"At a later date Transcontinental & Western Air, Inc., **likewise contended that the contract was
terminated** and that it intended to claim damages." **Why they differ:** both parties asserted termination,
and the report — written by the party that kept the money — is the only account held. **Weight:** one
audited-adjacent self-report; no counter-party document, no docket. **Best-supported interpretation:** the
bytes establish a dispute and a retained $397,500, not a breacher. **Residual:** settlement terms (the report
says only that the companies "are now negotiating" and that a settlement "would involve a purchase … of an
undetermined number of Stratoliners"); whether the eight Stratoliners in the 1939 backlog (5 to T.W.A., FY1939)
are that settlement — **plausible and unproven**; the two reports never join the sentences. **Confidence**
High (facts), UNKNOWN (fault and outcome).

STATUS: WRITTEN

---

## CLAIM RECORDS APPENDIX (part 1: sections Header, boundary, A-U)

**T2 tier rule applied (§15.2):** records for load-bearing claims only. Twenty-four records cover the claims that
carry the dossier's argument; rows in §P/§Q whose claim is a single printed figure are carried by the
registers instead of a record each. `Corroboration` counts **independent origins** (§3), not printings.
`Archived` names the shelf the bytes sit on. All `URL:` values are the provenance-sidecar URLs as recorded
at fetch; all sidecars carry `ok-INSECURE` / `UNVERIFIED TLS`, which caps confidence where noted.

P1A01 Claim: At 1940-12-31 the reporting group was Boeing Airplane Company with one direct wholly-owned
subsidiary (Boeing Aircraft Company, Seattle), its Wichita operation as a division, and a Canadian
subsidiary held by the subsidiary (Vancouver, B.C.) — Date: 1940-12-31 — Source: Boeing Airplane Company and
Subsidiary Companies, Report to Stockholders, Year Ended December 31, 1940 — Source date: 1941-03-08 —
URL: https://archive.org/download/boeingairplanecompanyannualreports/boeing1940_djvu.txt — Archived:
sources/corporate_print/boeing1940_djvu.txt (33,308 B) — Tier: 1 — Class: FACT — Passage: "The Boeing
Airplane Company embraces Boeing Aircraft Company, a wholly-owned subsidiary located at Seattle, Washington"
— Conf: High — Corroboration: 1 (also stated in FY1939; same lineage) — Conflicts: None.

P1A02 Claim: The company's first audited profit was $374,655.29 on gross sales of $19,390,718.32 for 1940
— Date: 1940-12-31 — Source: FY1940 Consolidated Profit and Loss Statement (domestic) — Source date:
1941-03-06 (auditors) — URL: as P1A01 — Archived: same file — Tier: 1 — Class: FACT (audited-adjacent; the
certificate is scope-limited) — Passage: "NET PROFIT FOR YEAR (Note 1) $374,655.29" — Conf: High —
Corroboration: 1 — Conflicts: U.012.

P1A03 Claim: Unfilled orders of U.S. units reached $196,522,446 at the boundary and their composition was
thereafter legally withholdable — Date: 1940-12-31 — Source: FY1940 §Business in Hand — Source date:
1941-03-08 — URL: as P1A01 — Archived: same — Tier: 1 — Class: FACT — Passage: "Federal Government
regulations prohibit the publishing of further detailed information." — Conf: High — Corroboration: 1 —
Conflicts: U.006.

P1A04 Claim: The held in-window company print attaches "since 1916" to a **different** corporation from the
report's addressee — Date: 1934-12-31 (statement) — Source: FY1934 letter to stockholders ¶3 — Source date:
1935-03-04 — URL: https://archive.org/download/boeingairplanecompanyannualreports/boeing1934_djvu.txt —
Archived: sources/corporate_print/boeing1934_djvu.txt (12,430 B) — Tier: 1 — Class: FACT of the printing;
the identity inference is UNKNOWN — Passage: "Boeing Aircraft Company, a Washington corporation, has been
engaged in the manufacture of aircraft since 1916." — Conf: High — Corroboration: 1 lineage (repeated FY1935
— same corporate record) — Conflicts: U.001, U.003.

P1A05 Claim: The names Westhoff, Pacific Airplane/Pacific Aero, "B & W" and Montreal occur zero times in the
25 held non-SEC text files, and Boeing occurs zero times in both negative-control periodicals — Date:
measured 2026-10-07 — Source: this pass's counts over `corporate_print/*.txt` + `periodicals/*.txt` —
Source date: 2026-10-07 — URL: local corpus — Archived: — Tier: 1 (of the bytes measured) — Class: FACT (of
absence over held bytes; §2 record-selection null applies) — Passage: NO_VERBATIM_PASSAGE_RECORDED —
Conf: High — Corroboration: 1 measurement, command stated in `research/NOTES` — Conflicts: U.011, U.015.

P1B01 Claim: The reporting company was formed to acquire assets of a dissolving corporation and its own
account began 1934-09-01 — Date: 1934-08-31 / 1934-09-01 — Source: FY1934 letter ¶1 — Source date: 1935-03-04
— URL: as P1A04 — Archived: same — Tier: 1 — Class: FACT — Passage: "your company was formed for the purpose
of acquiring these assets upon the dissolution of United Aircraft & Transport Corporation." — Conf: High —
Corroboration: 1 lineage (FY1935/38 printings of the same fact) — Conflicts: U.002.

P1B02 Claim: A federal record recites the 1927 mail-contract party as a Washington corporation named Boeing
Airplane Company, Incorporated, of Seattle — Date: 1927-02-01 (contract) — Source: Boeing Air Transport, Inc.
v. Farley (D.C. Cir. 1934), route-certificate recital — Source date: 1934 — URL:
https://archive.org/download/dc_circ_1934_6287_boeng_air_transp_v_farley/dc_circ_1934_6287_boeng_air_transp_v_farley_djvu.txt
— Archived: sources/periodicals/…djvu.txt (625,596 B) — Tier: 1 — Class: FACT (recital, third-party paper) —
Passage: "a corporation duly organized and existing under the laws of the State of Washington" — Conf: High —
Corroboration: 1 — Conflicts: U.001, U.004.

P1B03 Claim: W. E. Boeing is documented in-window only as an officer of a **different** Boeing corporation,
under oath — Date: 1927-1934 record; oath's own date OCR-destroyed — Source: dc_circ, Certificate of the
Oath of Mail Contractor and Carriers — Source date: 1934 — URL: as P1B02 — Archived: same — Tier: 1 —
Class: FOUNDER CLAIM (contemporaneous, sworn) — Passage: "I, W. E. Boeing, as President of Boeing Air
Transport, Inc., a corporation, making this affidavit for and in behalf of said corporation" — Conf: High —
Corroboration: 1 — Conflicts: U.013.

P1B04 Claim: The 1935 report prints a twentieth-anniversary day for the 1916-attached subsidiary — Date:
anniversary falls 1936-07-22; year DERIVED — Source: FY1935 §Boeing Aircraft Company ¶1 — Source date:
1936-03-09 — URL: https://archive.org/download/boeingairplanecompanyannualreports/boeing1935_djvu.txt —
Archived: sources/corporate_print/boeing1935_djvu.txt (16,394 B) — Tier: 1 — Class: RESTATED /
RETROSPECTIVE INTERPRETATION, with DERIVED arithmetic — Passage: "The twentieth anniversary of this
subsidiary will occur July 22 of this year." — Conf: Medium — Corroboration: 1 — Conflicts: U.003.

P1C01 Claim: The company's stated operating problem was unamortisable new-model development cost — Date:
1934-12-31 — Source: FY1934 letter ¶7 — Source date: 1935-03-04 — URL: as P1A04 — Archived: same — Tier: 1 —
Class: FACT of the statement; the conviction behind it is self-asserted — Passage: "the manufacture of
aircraft can be successfully carried on only by spending fairly substantial sums in the development of new
models" — Conf: High — Corroboration: 1 — Conflicts: U.008.

P1D01 Claim: Route A.M. 18 was competitively bid on 1927-01-15 with four named bidders at four prices, and
the Boeing-Hubbard bid was lowest — Date: 1927-01-15 — Source: dc_circ, Bill of Complaint ¶6 — Source date:
1934 — URL: as P1B02 — Archived: same — Tier: 1 — Class: FACT (federal record, independent of company print)
— Passage: "(a) Boeing Airplane Company and Edward Hubbard, Georgetown Station, Seattle, Washington, at the
rate of $1.50 per pound for the first thousand miles and 15 cents per pound for each additional 100 miles" —
Conf: High — Corroboration: 2 origins (pleading and the court's own statement of facts) — Conflicts: U.004,
U.005.

P1D02 Claim: The route was performed, and a U.S. government mail clerk testified to handing its mail to the
carrier's employee at Cheyenne — Date: 1927-07-01 onward; testimony lodged 1931-08-20 — Source:
Edelman v. Boeing Air Transport record, Statement of Evidence; and dc_circ court's facts — Source date:
1931 / 1934 — URL: https://archive.org/download/micro_IA40386008_0350/micro_IA40386008_0350_djvu.txt —
Archived: sources/periodicals/micro_IA40386008_0350_djvu.txt (493,539 B) — Tier: 1 — Class:
CONTEMPORANEOUS OBSERVATION (third-party federal employee, sworn) — Passage: "I deliver the mail to the
employee of the Boeing Company." — Conf: High — Corroboration: 2 origins (this testimony and dc_circ's
"Performance under the contract commenced July 1, 1927") — Conflicts: U.016 (the name form).

P1E01 Claim: The company's own picture chronology opens at a 1916 two-place trainer seaplane — Date: page
printed 1936 for FY1935 — Source: FY1935 final page, "PROGRESS" — Source date: 1936-03-09 — URL: as P1B04 —
Archived: same — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION (company-authored, ~20 years after) —
Passage: "THE FIRST BOEING PLANE— A TWO-PLACE TRAINER SEAPLANE." + "1916" — Conf: Medium — Corroboration: 1 —
Conflicts: U.003 (and the non-quotable later rungs, §E.1).

P1F01 Claim: Deliveries at the boundary foot exactly to the audited gross sales by customer class — Date:
1940 — Source: FY1940 §Accomplishments and P&L — Source date: 1941-03-08 — URL: as P1A01 — Archived: same —
Tier: 1 — Class: FACT plus DERIVED cross-check (`14,754,875 + 718,355 + 3,917,488 = 19,390,718`) — Passage:
"aircraft of the value of $14,754,875. were delivered to the United States Army" — Conf: High —
Corroboration: 1 document, two internal statements agreeing — Conflicts: None.

P1G01 Claim: The Government agreed in October 1940 to reimburse plant construction over sixty months, with
Note-3 ceilings of $3,625,765.22 and $7,627,032.13 — Date: 1940-10 — Source: FY1940 §Financing of Emergency
Plant Facilities; Note 3 — Source date: 1941-03-08 — URL: as P1A01 — Archived: same — Tier: 1 — Class: FACT —
Passage: "the Government agrees to reimburse the companies for the cost of the facilities in sixty equal
monthly installments commencing with the completion of the facilities." — Conf: High — Corroboration: 1 —
Conflicts: None.

P1J01 Claim: Certification by the federal aviation authority gated the two commercial types in-window — Date:
1938 (Clipper ATC), 1939-40 (Stratoliner temporary C of A) — Source: FY1938, FY1939 — Source date: 1939-03-15
/ 1940 — URL: …/boeing1938_djvu.txt; …/boeing1939_djvu.txt — Archived: sources/corporate_print/ (23,332 B;
25,088 B) — Tier: 1 — Class: FACT — Passage: "the Civil Aeronautics Authority issued an Approved Type
Certificate for the Clippers" — Conf: High — Corroboration: 1 lineage — Conflicts: None.

P1K01 Claim: The accumulated deficit was written off against paid-in surplus at 1939-09-30 for $3,471,686.29
— Date: 1939-09-30 — Source: FY1940 capital-stock-and-surplus caption — Source date: 1941-03-08 — URL: as
P1A01 — Archived: same — Tier: 1 — Class: FACT — Passage: "after elimination of earned surplus (deficit) at
September 30, 1939, by transfer to paid-in surplus in an amount of $3,471,686.29" — Conf: High —
Corroboration: 1 — Conflicts: U.012 (context).

P1K02 Claim: The May 1940 rights issue raised net $5,392,547.25 and retired the secured bank loan in full,
unencumbering the plants — Date: 1940-05 — Source: FY1940 §Financing — Source date: 1941-03-08 — URL: as
P1A01 — Archived: same — Tier: 1 — Class: FACT plus DERIVED (`360,496 × $16 = $5,767,936`; expense
`$375,388.75` printed in two statements and agreeing) — Passage: "There are now no encumbrances upon any of
the properties, plants, machinery, or equipment of the Companies." — Conf: High — Corroboration: 1 document,
two internal printings — Conflicts: None.

P1L01 Claim: The company's backlog inflected 7.93× during 1935 while the year still lost money — Date:
1935-01-01 → 12-31 — Source: FY1935 — Source date: 1936-03-09 — URL: as P1B04 — Archived: same — Tier: 1 —
Class: FACT plus DERIVED — Passage: "Unfilled Orders, December 31, 1935. 6,141,203.23" — Conf: High —
Corroboration: 1 — Conflicts: None.

P1M01 Claim: Boeing terminated (or disputed) a six-Stratoliner contract with Transcontinental & Western Air
in 1938 and retained a $397,500 down payment, with T.W.A. asserting a damages claim — Date: 1938 — Source:
FY1938 §Boeing Aircraft Company — Source date: 1939-03-15 — URL: …/boeing1938_djvu.txt — Archived:
sources/corporate_print/ — Tier: 1 — Class: FACT of the company's account; fault UNKNOWN — Passage: "A down
payment of $397,500 was retained as security against possible damages." — Conf: High (printed) / Low (who
breached) — Corroboration: 1 (no counter-party document held) — Conflicts: U.017.

P1M02 Claim: The Model 299 prototype's destruction eliminated the airplane from an Army bombardment
competition, and thirteen were later ordered — Date: 1935 (competition 1935-08; order late 1935) — Source:
FY1935 §Boeing Aircraft Company — Source date: 1936-03-09 — URL: as P1B04 — Archived: same — Tier: 1 —
Class: FACT of the account; cause UNKNOWN — Passage: "This eliminated the airplane from the competition
since all the requirements set forth in the Government circular advertisement could not be completed." —
Conf: High (printed) / Medium (event, single carrier) — Corroboration: 1 — Conflicts: None.

P1N01 Claim: The company's management changed on an explicit date, mid-crisis — Date: 1939-09-09 — Source:
FY1939 §Management — Source date: 1940 — URL: …/boeing1939_djvu.txt — Archived: sources/corporate_print/
(25,088 B) — Tier: 1 — Class: FACT — Passage: "The present management of your Company undertook its duties on
September 9, 1939." — Conf: High — Corroboration: 1 — Conflicts: None (caution on causation is in §N's coda).

P1S01 Claim: EDGAR's registrant header dates the conformed-name change from BOEING AIRPLANE CO to
1973-07-25, in 26 of the 33 held filings — Date: 1973-07-25 (field) — Source: SEC SGML header `FORMER
COMPANY:` block, held accessions 1994-03-15 → 2002 — Source date: varies per accession — URL:
https://www.sec.gov/Archives/edgar/data/12927/ (per-file paths in `sources/sec/`) — Archived: sources/sec/
(7,170,562 B, 33 `.txt`) — Tier: 1 — Class: FACT (of the field's printing); what it proves is bounded —
Passage: "FORMER CONFORMED NAME: BOEING AIRPLANE CO DATE OF NAME CHANGE: 19730725" — Conf: High (printing) /
Low (as the corporate act) — Corroboration: **1 record, 26 mechanical printings — not 26 sources** —
Conflicts: U.009.

P1S02 Claim: The registrant's own later recital collapses the chain into one person — Date: 1996-10-29 and
1998-05-13 — Source: Form S-4 (acc. 0000950123-96-006004) and S-4/A (acc. 0000891020-98-000905) — Source
date: as filed — URL: sec.gov/Archives/edgar/data/ per accession — Archived: sources/sec/ — Tier: 1 —
Class: RETROSPECTIVE INTERPRETATION `(PB)`, `RETROSPECTIVE SOURCE` (§6) — Passage: "Boeing was originally
incorporated in Washington in 1916 and was reincorporated in Delaware in 1934." — Conf: High (it is filed);
Low (as to the 1916 act) — Corroboration: 1 corporate self-description in 2 accessions — Conflicts: U.001.

---

## REGISTER ROWS FOR MERGE — applied to the nine CSVs at this directory root; not repeated here

Per method §13 the nine fenced `csv` register blocks are register data, not narrative. All **211** rows
(sources 19 · quantitative 75 · timeline 42 · conflicts 17 · data_gaps 18 · decisions 11 · validation 13 ·
failures 9 · channels 7) were **applied to the CSVs at the company root** and are the register layer of record
for this stage. The verbatim emission (header + rows, `P1SRCnn` provisional keys) survives read-only at
`_parts/s1_p1.md` l.1401–l.1698; the `P1SRCnn`→`S4510–S4528` re-key is bound by the id map in the MERGE
RECORD at the head of this file. `validation.csv`/`failures.csv` are bound by content (see the binding
paragraph at the head). **Rows withheld, named not dropped:** every FY1937 income-statement and balance-sheet
figure and all FY1936 quantities — layer condition / layer absent (`data_gaps.csv` P1GAP16, P1GAP05,
P1GAP08; `FETCH REQUEST #3`, `#4`).

---

## Untried

Each item is a search **never run**, not a null. Commands are for the orchestrator; every one needs a web
budget this pass did not have (web calls used by this pass: **0**).

1. **Family (e) auction / museum / manuscript documentary records** — no source-family exists in
   `queries.json`; nothing in `tools/` reaches a finding aid, an auction house or a museum collection. Target:
   the 1916-1929 paper class (correspondence, logbooks, original certificates of the 1916 corporation, the
   B&W-class artefacts). Command once the family is added:
   `python tools/periodical_harvest.py --company boeing --source-family auction --max-requests 12 --out /tmp/boeing_auction`.
   **This is the route most likely to change the Stage-1 verdict**, because it is the only family that can
   carry an instrument rather than a recital.
2. **Chronicling America** — the probe's endpoint probe returned 7/7 `CHALLENGED 403 Cloudflare` from this
   machine and cannot discriminate a path from here; not re-run by this pass (web 0). State: TRIED–UNANSWERED
   as to the route; UNTRIED as to Boeing's queries. Remedy: the nightly CI run, per RD-128.
3. **HathiTrust and Google Books for Boeing** — never opened by this pass; the probe recorded one
   UNANSWERED candidate row each. Command: `python tools/periodical_harvest.py --company boeing --source-family
   hathitrust --max-requests 8`, then read the bodies (RD-127).
4. **Aeronautics Branch / ICC / CAB series, 1926-1938** — would carry the A.M. 18 award file independently of
   the litigation copy and could settle U.004. Command: `python tools/ia_text.py search --q '"Aeronautics
   Branch" annual report commerce 1927' --rows 10 --insecure` then `fetch` and count namings **per held byte**.
5. **NLRB case registers, 1935-1940** — §G/M currently hold only the employer's own union statement;
   `python tools/ia_text.py search --q '"Boeing Aircraft Company" NLRB decisions 1935-1940' --rows 10 --insecure`.
6. **Patents** — nothing tried: `curl -s "https://search.patentsview.org/api/v1/query/?q=…inventor_last_name…"`
   (one request) establishes whether a first-decade inventor record exists at all.
7. **The 44 unopened in-window IA text items** — the probe opened 3 of 47 that advancedsearch returned for
   `Boeing AND mediatype:texts AND year:[1916 TO 1940]`. Command as the probe wrote it (`ia_text.py mine`,
   ≥6 invocations because `mine` fetches at most `min(rows,8)`).
8. **The 39 unopened corporate-print layers 1941-1978** — would close U.009 (the renaming date) and is the
   cheapest move on the board for Stage 2; the per-file route is already proven by the 46,004 B FY1945 fetch.
9. **Washington and Delaware charter/registry records** — the only route to U.001/U.002; **no tool in
   `tools/` reaches either**.
10. **Reporter volumes for the two held cases** — the only route to U.004's adjudicated context and to
    P1GAP06.
11. **The 1936 corporate-print layer's non-existence was never re-verified** — see P1GAP05 / `FETCH REQUEST` #4.

**FETCH REQUESTs emitted by this pass** (orchestrator runs the scripts; §15.1 — declining the fetch is the
correct behaviour, and this pass declined it):

```
FETCH REQUEST #1 — family (a), recital completion
  registrant CIK 0000012927; enumerate all 4,026 filings and fetch the earliest DEF 14A / 10-K per year
  1994-2002 (already held) PLUS any 1934-1960-era predecessor print available on EDGAR (none expected);
  specifically needed: the earliest filing carrying a corporate-history paragraph, to bound U.001.
  reason: only 2 of 33 held files carry the 1916/1934 recital; more printings of one boilerplate add nothing.
FETCH REQUEST #2 — reporter volumes
  Boeing Air Transport v. Farley (D.C. Cir. 1934) decision text, and 289 U.S. 249 (1933) opinion.
  reason: dispositions are 0-hit nulls over the held records (P1GAP06); needed for §H and §L confidence.
FETCH REQUEST #3 — boeing1937_djvu.txt page images or re-OCR
  item boeingairplanecompanyannualreports, file boeing1937_djvu.txt (20,844 B held, column-interleaved).
  reason: FY1937 financial statements are UNANSWERED-in-layer (P1GAP16), including the rights price.
FETCH REQUEST #4 — re-enumerate the item's file list
  python tools/ia_text.py list-files boeingairplanecompanyannualreports
  reason: confirm 1936's absence from the 46 layers rather than inherit the probe's enumeration (P1GAP05).
FETCH REQUEST #5 — charter records (no scripted route)
  Washington Secretary of State and Delaware Division of Corporations: Boeing Aircraft Company /
  Boeing Airplane Company / Pacific Airplane Corporation, 1916-1934.
  reason: the only evidence class that can settle U.001-U.003 as acts rather than recitals.
```

STATUS: WRITTEN

---

*End of part 1 (the whole of Stage 1 for this company as a single volume). Cross-references use the form
`(Boeing S1 §U.001)`. Unresolved conflicts are listed here, not deferred: U.001 which person 1916 is the
registrant's; U.002 formation as reincorporation or purchase; U.003 the 1916 day; U.004-U.005 the award date
and standard of Route A.M. 18; U.006 the 1939 backlog on two bases; U.007 the FY1935 share fractions; U.008 a
non-verbatim self-quotation; U.009 the renaming date; U.010 the reorganisation's motive; U.011 counting basis;
U.012 the quality of the first profit; U.013 the founder's presence; U.014 document identity inside one
archive item; U.015 the four noise families; U.016 what "Boeing Company" means in the 1933 record; U.017 who
terminated the T.W.A. contract.*

