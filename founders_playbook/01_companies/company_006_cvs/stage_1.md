# FORENSIC LONGITUDINAL DATASET — CVS CORPORATION (CIK 0000064803, the Melville line), STAGE 1 (1963 recited — 31 DECEMBER 1996)

## MERGE RECORD (assembly, application, id map, geometry fix, anchor parity, five-family carry, carry-forward)

Merged 2026-10-07 by `merge-cvs` from the single part `_parts/s1_p1.md` (author `s1-cvs-p1`, 22,951 words as
emitted, §A–§U complete, 20 claim records CVS-A01…CVS-A20, 9 fenced register blocks = **126 rows**). **Section
letters, claim IDs, metric IDs and conflict numbering are the author's and were not renumbered** (method §9.3 —
numbering continues, it is never re-based). Nothing in the narrative was rewritten, trimmed, or re-tiered.
`_parts/s1_p1.md` stays **read-only** and is the emission of record; it carries no `SUPERSEDED` footer because
nothing in its prose required correction (the correction ledger for this operation is `CORRECTIONS.md`).

**What was moved out of the prose.** The part's nine fenced `csv` register blocks (126 rows) are register data,
not narrative (method §13): they were **applied** to the nine CSVs at this directory root, and the `## registers`
heading now points at that application instead of repeating the blocks. Their verbatim text survives at
`_parts/s1_p1.md` l.1124–l.1312. Claim records **are** narrative: all 20 (CVS-A01…CVS-A20) are carried below,
unchanged. The full assembly account — pre-write census, the validation/failures content adjudication, and the
id-mint audit — lives in `03_quality_control/cvs_s1_merge.md`.

**I am the merger; I did not audit and I do not certify.** The five-family table below restates the probe's
verdict as the part carried it; the tier was **not** re-decided.

### Register application (requested ↔ applied, measured on the bytes written)

| register | rows requested | rows applied | cols | key / integrity check |
|---|---|---|---|---|
| `sources.csv` | 18 | **18** | 18 | keys **S4431–S4448**, 0 duplicates |
| `quantitative.csv` | 29 | **29** | 12 | 0 off-width, 0 exact-duplicate rows |
| `timeline.csv` | 24 | **24** | 11 | `source_id` remapped PROV→global, 0 off-width |
| `data_gaps.csv` | 10 | **10** | 8 | S.1–S.10, 0 off-width |
| `conflicts.csv` | 10 | **10** | 15 | keys **U.01–U.10**, 0 duplicates, 1:1 with §U |
| `failures.csv` | 7 | **7** | 11 | adverse-signal block, adjudicated by content (see merge record) |
| `validation.csv` | 8 | **8** | 11 | validating-signal block, adjudicated by content |
| `decisions.csv` | 14 | **14** | 15 | 1 geometry fix (COR-02): row 1 emitted at 16 cols, trimmed to 15 by dropping one spurious `UNKNOWN`; no value moved |
| `channels.csv` | 6 | **6** | 11 | 0 off-width |
| **TOTAL** | **126** | **126** | — | **0 unapplied, 0 added by the merge** |

Headers are byte-identical to the corresponding Amazon conformant register headers; `stage` is the literal
`stage1` on all 126 rows; the width / duplicate-key / exact-duplicate-row pass was run **across every block of
this one operation together**: 0 off-width, 0 empty `source_id` cells, 0 duplicate rows across the nine, 0
duplicate keys in the two keyed registers.

### Provisional-to-global id map (the only place `PROV-CVS-01…18` bind; minted centrally)

`id_mint.py --audit` before minting: highest live block `company_023_gm S4423..S4430`, `next assignable: S4431`;
the live collision set named in the brief — **`S4222–S4229` shared by Microsoft and Target** — was deliberately
not allocated into. `id_mint.py --count 18 --company company_006_cvs --claim --agent merge-cvs` → **S4431…S4448**.

| local | global | carrier (source_title in `sources.csv`) |
|---|---|---|
| PROV-CVS-01 | **S4431** | Form 8-B12B, CVS Corporation (Successor to Melville Corporation), 1996-11-04 |
| PROV-CVS-02 | **S4432** | Term census over `sources/sec/*.txt` (36 files) — derived measurement |
| PROV-CVS-03 | **S4433** | Form S-4 (Revco D.S. Inc merger registration) — the only 1963 carrier, one lineage |
| PROV-CVS-04 | **S4434** | Form 10-K405 FY1996 — first annual report of the renamed registrant |
| PROV-CVS-05 | **S4435** | Drug Store News layer 1979-10-29→1980-10-13 (earliest held naming row) |
| PROV-CVS-06 | **S4436** | Drug Store News layer 1983-10-31→1984-10-29 (Con-sumer hyphen-healed row) |
| PROV-CVS-07 | **S4437** | Drug Store News layer 1989-11-06→1990-10-22 (md5-duplicate on corporate_print) |
| PROV-CVS-08 | **S4438** | Drug Store News layer 1990-11-05→1991-10-28 (Civic Drugs 1963 decoy) |
| PROV-CVS-09 | **S4439** | Drug Store News layer 1994-11-07→1995-10-23 (Peoples-name-erased row) |
| PROV-CVS-10 | **S4440** | DEF 14A (Melville proxy 1994-03-14) — compensation peer set |
| PROV-CVS-11 | **S4441** | Form 10-K FY1993 — the 1,284 / 1,081 filed segment estate |
| PROV-CVS-12 | **S4442** | Form 10-K FY1994 — CVS, Inc. RI + Pharmacare DE (SGML header absent) |
| PROV-CVS-13 | **S4443** | Form 10-K FY1995 — ~97,000 associates; Rye NY principal office |
| PROV-CVS-14 | **S4444** | Form 8-K Item 5 (Marshalls→TJX) — the $585m/$195m charge |
| PROV-CVS-15 | **S4445** | SC 13D by Melville, subject TJX /DE/ — third-party filing naming CVS persons |
| PROV-CVS-16 | **S4446** | DEF 14A (proxy) 2001-03-15 — director-employment-history 1963 decoy |
| PROV-CVS-17 | **S4447** | EDGAR submissions index CIK 64803 (2,968 rows) — the S-1/SB-2/10-A 0 / 8-B12B 1 census |
| PROV-CVS-18 | **S4448** | six annual index volumes (JAPHA / Pharmacy Times) — NULL by construction, 2 md5-dupes |

Re-minting was mechanical and complete: every `PROV-CVS-nn` token in every `source_id`-bearing cell (and in
compound cells) was replaced by its minted id; `PROV-CVS-nn` survives only in the read-only part and in the map
above. The narrative body and the claim records carry no source ids, so the mint touched no prose.

### Anchor ↔ conflict parity (measured)

10 declared anchors (`<!-- ANCHORS: U.01-U.10 -->`) ↔ 10 §U subsections ↔ 10 `conflicts.csv` rows
(`U.01…U.10`, 0 duplicates); after-write `merge_census.py` reads `conflicts.csv | requested 10 | present 10 |
missing 0`. **0 orphans in either direction.** No anchor was renumbered; U.01–U.10 are the author's ids.

### Five families as carried (not re-tiered; (b) and (e) stated UNTRIED as such)

**(a) SEC/EDGAR — TRIED–ANSWERED** (identity/S1d; S1a by recital only). **(b) Web archives — UNTRIED, 0 calls**
(no `sources/web_archive/`; `cdx_intake.py` never run for CIK 64803). **(c) Periodicals — TRIED–ANSWERED in
part; TRIED–UNANSWERED for Chronicling America; 57 candidates UNTRIED at the limit.** **(d) Digitised corporate
print — TRIED–UNANSWERED (year-faceted) and ZERO BYTES** (its 4 files are IA serial layers, 2 md5-duplicates of
(c); **not counted as a family — U.08**). **(e) Auction / museum / manuscript — UNTRIED, 0 calls, no query block
for `cvs`.** Families that counted for the dispatched window: **2 (a, c) ⇒ T2 core carried; S1a/S1b/S1c remain
T3 register.**

### The three spine carries (kept exactly as the part issued them)

1. **1996 = reincorporation-by-succession, not an IPO** (U.03; CVS-A01/A02/A03): 8-B12B filed 1996-11-04 names
   "CVS CORPORATION (Successor to Melville Corporation)", organised 1996-08-22 under Delaware law, triangular
   merger renaming the survivor "CVS New York, Inc."; **0 rows of S-1/S-1/A/SB-2/10-A in 2,968** is the proof.
2. **Corporate-print shelf is not family (d)** (U.08): four files are IA serial layers, two md5-duplicates of the
   periodicals shelf, so two families do not count and the window stays **T2** while S1a/S1b/S1c stay **T3**.
3. **U.10 supersedes the probe's naming lineage**: **6** *Drug Store News* rows **1980-01-21→1994-04-25** (OCR
   line-break-hyphen healing as the method) rather than 4 rows 1990-1994. "Founded in 1963" stays **COMPANY
   CLAIM, retrospective, Medium, one lineage**; the shoe-store / Jacksonville / Consumer-Value-as-1963-entity
   folklore is **UNKNOWN** with its route named.

---


## Header

# FORENSIC LONGITUDINAL DATASET — CVS CORPORATION (CIK 0000064803, the Melville line), STAGE 1 (1963 recited — 31 DECEMBER 1996)

**Company:** today's **CVS Health Corporation**, CIK **0000064803**. This volume does **not** write "CVS Health
(1963)". It writes **a New York shoe-and-specialty retailer called Melville, which on 1996-08-22 organised a Delaware
holding company and took its own CIK by succession** — and which, thirty-four years later, recited a 1963 founding of
its drugstore **business**. The argument is at `## boundary` and §B and is the single most consequential choice here.
**File:** Stage 1, part 1 of 2 — `Header`, `boundary`, **§A–§U** and the **register append blocks**. Claim records for
load-bearing claims live here too; the merged `stage_1.md` does not exist yet, so cross-references name the volume, not
the line: `(CVS S1 §U.07, part_1)`. Section letters, claim IDs, metric IDs and conflict numbering run continuously
across parts and are **never renumbered** to make a part look self-contained.
**Dossier this part is written against:** `research/A_chronology_feasibility.md` (probe `probe-cvs`, tier verdict) and
`research/A4_harvest_mine.md`, both re-measured before use. Where this part **supersedes** the probe it says so in
§U.10 and in `NOTES_cvs_p1.md`; it does not silently re-tier.
**Tier carried from the probe (§15.2):** whole dispatched Stage 1 window (1963-01-01→1996-12-31) = **T2 core**
(2 of 5 families return in-window Tier-1 text: (a) SEC, (c) periodicals); **S1a/S1b/S1c = T3 register**, **S1d = T2
core**. Per-stage tiers are the deliverable, so §K, §N and §U are written as registers, not as narrative, wherever the
window is empty.

**Stage definition:** origin → first real-world experiment → repeatable validation → scalable company formation. For a
**chain-retail registrant whose origin is recited rather than recorded**, §7's adaptation rule is applied as follows:
the four beats become *the founding act (here unrecorded), the format and estate (stores/pharmacies), the parent's
restructuring, and the corporate re-cut that made the brand the registrant*. The window **closes at 1996-12-31**
because that is the dispatched window edge **and** because the registrant's own legal form changes inside it
(1996-08-22 organisation; November 1996 rename) — the two reasons are different and are kept separate in §Boundary.

**Hindsight firewall (§2).** Nothing here treats the 2007 Caremark combination, the 2014 Express Scripts decision,
the 2018 Aetna acquisition or the Fortune-rank-6 present as evidence that a 1963 store opening, a 1990 Peoples
purchase or a 1996 reincorporation was wise, inevitable, or visible to anyone then alive. The words "destined",
"visionary" and "transformational" do not occur in this volume outside a quotation mark. The **present-state facts are
 quarantined**: Woonsocket, Rhode Island is the HQ *from the 1990s onward*, and the universe CSV carries **no
founding-date column at all** (verified by reading its header, §T.4) — so no Rhode Island facet of any search is
evidence about 1963, and two Chronicling America tasks built on exactly that fallacy are recorded in §S.
**Record-selection null (§2).** What is unrecoverable *because the survivor's archive is the one that was kept*:
**zero** held bytes record anyone deciding anything in 1963–1979 — no founder, no memo, no lease, no opening-day
report, no rejected option, no independent count behind any company self-report. The 1963 sentence is a *selected*
record: it appears because a 1997 merger registration needed a one-line business description. EDGAR reaches nothing
before **1994-02-10** for this CIK (2,968 indexed rows, 0 before 1994-01-01), and the paper-era filings of Melville —
a listed company since long before 1963 — live outside EDGAR entirely. See §S, and §T.5 for the 125 indexed rows that
carry no `primaryDocument`.

**Claim classes (§3):** FACT · FOUNDER/COMPANY CLAIM (labelled *contemporaneous* vs *retrospective*) ·
CONTEMPORANEOUS OBSERVATION · RESTATED · RETROSPECTIVE INTERPRETATION · INFERENCE · ESTIMATE/DERIVED · UNKNOWN.
**Confidence (§3):** **High** = 2+ independent origins or a primary document for its own year; **Medium** = one
reliable source, a retrospective-only primary, **or any claim resting solely on a layer fetched over UNVERIFIED TLS**
(all 18 periodical-side sidecars say `transport = "UNVERIFIED TLS — re-check before citing at High confidence"`, so
**no periodical citation in this volume is High**); **Low** = conflicting, vague, or retrospective-only with no
carrier; **UNKNOWN** = a finding, not a gap to fill or smooth.

**Three matching disciplines this volume is required to enforce, and does (§T.6).**
1. **`CVS` is a three-letter acronym and a medical abbreviation.** A bare `CVS` string is **not** a naming of this
   registrant. Entity adjacency is required: `CVS` hard against an identity word (`CVS Corporation`, `CVS Pharmacy,
   Inc.`, `CVS Stores`, `Consumer Value Stores (CVS)`, `CVS H.C., Inc.`). Measured effect: the held DSN layers carry
   **3–185 bare `CVS` occurrences per file but only 0–6 entity-adjacent ones** — e.g. `micro_IA40706948_0070`
   (1994 layer) 172 bare / 4 adjacent; `micro_IA40706918_0157` 18 bare / **0** adjacent; the JAPHA and *Pharmacy
   Times* index volumes **0 of each**. The class that produced this rule is on display in the same shelf: `1963` in
   the DSN layers is *another chain's* founding (`Civic Drugs in Dearborn, Mich. in 1963`, §U.06) and other
   companies' stock-table digits and copyright years.
2. **An index label is not a source.** `TIER1_CANDIDATE_TEXT` is a column in `sources/harvest_mine/_index.json`, and
   `classification` in `00_universe/harvest/candidates.csv`. Nothing in this volume counts a hit, a family or a tier
   from either. Rows below that label are cited as **pointers to bytes**, and every quotation used here was read in
   the held `.txt` itself at the stated line.
3. **One lineage is one source.** The 1997 **S-4**, its **S-4/A** and the merger **DEF 14A** print the *same*
   "Founded in 1963" sentence; they are **one** witness (3 files, 1 recital). Byte-identical files on two shelves are
   **one** document. A scanner is a carrier, not a second corroboration.

**How to read a value here.** Every figure carries the *legal person* it describes and the *basis* (chain vs segment
vs consolidated; fiscal vs calendar; nominal). A number that cannot be attributed to a named person in a held file is
written as UNKNOWN with the route that could name it.

---

STATUS: WRITTEN 2026-10-06

---

## boundary

**Windows are PROPOSED, labelled per RD-112, and each is measured against its own stage's carriers — never against
the company's whole history, and never against the search setting that produced it.**

| Stage | PROPOSED window | Boundary argued from | What the corpus on disk answers inside it |
|---|---|---|---|
| **S1a** origin as claimed | 1963-01-01 → 1968-12-31 | the only origin claim on the table is the registrant's own recited year | **(a) one recital, 34 years late** (1997 S-4 lineage, `Founded in 1963`), **year only**; 0 bytes for town, original name, business type, founder. **(b)(d)(e)** UNTRIED. **(c)** 0 in-window (oldest held issue-dated text is 1979-10-29). |
| **S1b** format shift, claimed | 1969-01-01 → 1979-12-31 | the asserted move from footwear to pharmacy — an assertion, not a dated record | **(c)** bytes exist (DSN issues dated **1979-10-29 → 1979-11-12**, 16 mastheads) but carry **0 `CVS`-bearing lines**; **(a)(b)(d)(e)** nothing. This window is retained as **argued-empty**: nothing held distinguishes "1963 shoe store" from "1979 goes drugs", because neither is in the bytes. |
| **S1c** chain formation under Melville | 1980-01-01 → 1989-12-31 | first continuous third-party naming of the estate | **(c) TRIED–ANSWERED**: entity + name-phrase rows issue-dated **1980-01-21, 1983-11-14, 1987-11-23, 1988-04-25** naming *Consumer Value Stores (CVS)*, *CVS Stores*, *Melville Corp., owner of CVS Stores*; 1989 estate 789 stores / 582 with pharmacies. **(a)** silent (EDGAR floor 1994-02-10). |
| **S1d** restructuring and succession | 1990-01-01 → 1996-12-31 | the registrant's own paper begins and its legal form changes inside the window | **(a) + (c) both answer**: 7 in-window Melville filings (1994-02-10 → 1996-04-08) plus the **8-B12B filed 1996-11-04** which organises the Delaware registrant on **1996-08-22**; DSN "CVS at a glance" boxes 1990-04-09, 1991-05-06, 1993-04-26, 1994-04-25 and the Peoples-acquisition story of 1990-09-24. |
| **Whole dispatched window** | 1963-01-01 → 1996-12-31 | — | 2 of 5 families ⇒ **T2 core**; S1a/S1b/S1c ⇒ **T3 register**. |

**What this boundary does NOT claim.** (i) Not that **1996 is an IPO.** Measured in the registrant's own EDGAR index of
2,968 rows: `S-1` **0**, `S-1/A` **0**, `SB-2` **0**, `10-A` **0**, `8-B12B` **1**. 1996 is a
**reincorporation-by-succession with a Section 12(b) successor registration**. Whether CVS equity was separately
floated in 1996 is UNKNOWN here (§S.3). (ii) Not that **1994-02-10 is when CVS "began filing"** — it is the earliest
*indexed* row for a CIK whose predecessor was listed for decades; pre-1994 silence is a measured **perimeter**, not a
null. (iii) Not that the **1996-12-31 close is an operational break** in the business: it is a search edge that happens
to coincide with a legal-form change. (iv) Not that the recited **1963 attaches to any legal person available on
disk** — §B.3 enumerates the fifteen CVS-bearing persons the bytes actually name, and none is dated 1963.
(v) Not that the **insurance or pharmacy-benefit legs belong in Stage 1 at all**: they are later, separately-dated
acts — `Pharmacare, founded in 1994` (own recital, §Q) is the only one with a date inside the window, `Caremark`
occurs **0 times in all 36 held SEC files**, and no insurance underwriter is named anywhere (§C.3, §U.05).

**Window hygiene note for the merge.** The intake windows on disk are **search parameters, not evidence**:
`harvest_mine.py WINDOWS["cvs"] = ("1963-01-01","1996-12-31")`, mirrored into `sources/harvest_mine/_index.json`
(`window ["1963-01-01","1996-12-31"]`, re-read at 2026-10-06 17:47: **candidates 70 / mined 12 / untried_by_limit 57**).
The two `NULL` corporate-print rows are year-faceted (`year_range [1960,1998]`), so they are a statement about our
parameter, not about the archive (RD-130).

STATUS: WRITTEN 2026-10-06

---

## A..U

**How §A–§U are written here, and why they are uneven.** The probe's per-stage tiers bind the prose: from **1990**
onward the narrative is evidence-bound and from **1994-02-10** it is bound to the registrant's *own* paper; for
**1963–1979 the deliverable is a register, not a narrative**, so §K, §N and §U carry UNKNOWN with the named route and
§C–§J state the empty window plainly rather than fill it. **A shoe store is not written anywhere in this volume** —
that sentence is a boundary test, not a stylistic choice: the dispatch brief asserted the folk origin, a brief is not
a carrier, and every element of it except the year is measured at **0** in the held bytes (§B.1, §U.01–U.02).
Document shorthands (`S96-8B12B`, `K96-405`, `DSN-8384`, …) are defined once in **§T**; line numbers appear only as
locators, never as addresses (§14 r12).

STATUS: WRITTEN 2026-10-06

## A. EXECUTIVE STATE SUMMARY (as of the window close, 1996-12-31)

At 31 December 1996 the registrant behind today's CVS Health was **a nine-month-old Delaware holding company that had
not yet finished becoming one**. `S96-8B12B` Item 1(a), as filed: *"CVS Corporation ('CVS' or the 'Registrant') was
organized as a corporation on August 22, 1996 under the laws of the State of Delaware"* [CVS-A01]. Its predecessor was
**Melville Corporation, a New York corporation** — a diversified specialty retailer that in FY1993 described itself as
*"one of the largest diversified specialty retailers in the United States"* (`K93` L147-149), sold apparel, footwear,
toys and home furnishings alongside drugs, and whose principal office was in **Rye, New York** (`K95` L177) while its
drugstore estate sat at **One CVS Drive, Woonsocket, Rhode Island** (`S96-8B12B` L85). The mechanism that joined them
was a **triangular merger**: a wholly-owned New York merger subsidiary, `CVS New York, Inc.`, merged into Melville;
Melville was the **Surviving Corporation** and was itself renamed **"CVS New York, Inc."**; the merger agreement is
dated as of **August 30, 1996** (`S96-8B12B` L136-150) [CVS-A02]. The registration instrument is
`8-B12B` — *"FOR REGISTRATION OF SECURITIES OF CERTAIN SUCCESSOR ISSUERS … FILED PURSUANT TO SECTION 12(b) OR (g)"*,
cover naming **"CVS CORPORATION (Successor to Melville Corporation)"**, state of incorporation *Delaware*,
I.R.S. Employer Identification Number *Applied For*, NYSE listing of $.01 par common (`S96-8B12B` L66-96) [CVS-A03].
**The EIN is the tell**: every stored filing through 1996 carries Melville's `04-1611460`; every 1997+ filing carries
CVS Corporation's `05-0494040` (§T.3) — **the same CIK, a different taxpayer**.

**The estate at the close** (registrant's own paper, `K96-405` Item 1, L158-170) [CVS-A04]: over **$5.5 billion**
revenue in 1996; **1,408 stores** in **14 states and the District of Columbia**, "most of which have pharmacies";
1996 **pharmacy sales $2.4 billion, +18.4%, 43.9% of total**; **front-store sales $3.1 billion, +9.3%, 56.1%**;
about **1,200 prescriptions filled per pharmacy per week**; **$573 total sales per square foot**, which the filing
calls top-performing in the chain drug industry. Separately recited (`K96-405` L469-475): **Pharmacare, founded in
1994**, the prescription-benefit-management subsidiary, managed healthcare services for **more than one million people**
at the end of 1996 [CVS-A05]. The chain's own rank is the registrant's words, 34 years after the claimed origin and
34 years before the present: *"Founded in 1963, CVS is the country's fifth largest drugstore chain in terms of store
count and sales volume, with approximately 1,400 stores and $5.5 billion in 1996 annual revenue"* (`S97-S4` L762-765)
[CVS-A06] — and the same filing's next paragraph dates the **name**: *"In November 1996 CVS changed its name from
Melville Corporation to CVS Corporation, reflecting its concentration on the chain drugstore business and the
completion of its restructuring program that was approved by its Board in 1995 following a strategic review initiated
in 1994"* (`S97-S4` L767-770) [CVS-A07].

**Still open at the close, on the held bytes.** The succession paper is an *application* ("Applied For", `Delaware
Applied For`, L80) and the proxy that carries the Proposal is dated **1996-10-07** (L120-127): the bytes on disk
**do not record the Effective Time actually occurring**. The registrant was mid-transaction: an **S-4 for the Revco
D.S., Inc. merger** was filed 1997-03-28 (`S97-S4`, Revco at 1925 Enterprise Parkway, Twinsburg, Ohio, ~2,600 stores,
$5.3 billion). The apparel and footwear legs were being sold or spun (`K95` L197-200 classifies footwear as
discontinued operations pending a 1996 spin; Marshalls sold to **TJX Companies, Inc. /DE/** — the only stored document
that names CVS-bearing persons in bulk is a **TJX** SC 13D, `D96-TJX`, filed 1996-04-08 by Melville as transferor,
which is exactly the mis-reading this volume refuses, §S.6).

**What the state summary cannot say.** It cannot say who founded anything, where, in what format, or under what name
in 1963; it cannot say the 1963 event was a pharmacy; it cannot say a legal person existing in 1963. Those are §B.1,
§C, §K and §U, and they are **UNKNOWN with named routes**, not silence.

**Anti-hagiography check (§2).** Read without the present, 1996-12-31 is a *re-cut of a shrinking department-store
holding company* mid-way through its largest acquisition, whose own paper spends more space on restructuring charges
and divestitures than on origins, and whose trade-name estate in FY1993 still included **Peoples, Standard Drug and
Austin Drug** beside CVS. Nothing in the held bytes makes the later position look foreseeable.

---

## B. FOUNDER / COMPANY STATE

### B.1 The founder: there is no founder in this record

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Founder named in any held byte | **UNKNOWN — no carrier.** Across **all 36** stored SEC files: `Kandel` **0**, `Lowell` **0**, `Consumer Value` **0**, `Jacksonville` **0**, `first store` / `first drugstore` **0**, `Newport` **0** | Term census over `sources/sec/*.txt` (normalised, case-insensitive, OCR-hyphen-healed) [CVS-A08] | **High** (that the bytes are silent) |
| Founder's own words | **None held.** No interview, deposition, letter or contemporaneous statement of any individual founder exists on any shelf in this company dir | Shelf census, §T.1 | High |
| A `FOUNDER CLAIM` class therefore | **Unavailable** for 1963. The only candidate class the 1963 year supports is a **corporate self-narrative, retrospective** — `RETROSPECTIVE SOURCE` tagged (§6) | `S97-S4` L762; class ruling carried from the probe §9.1 | High (the class); Medium (the date it asserts) |
| The "1963" that is **not** a founding | `P01` (DEF 14A, filed 2001-03-15) L436: *"consulting firm, since April 1998. From 1963 to March 1998, he was President of"* — a **director's employment history**. This is the single `1963` outside the S-4 lineage in the whole SEC shelf and it is **not** an origin | `P01` L436 [CVS-A09] | High — registered as **U.06** |

### B.2 The firm's state, as filed

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Legal form of the registrant | **CVS Corporation, a Delaware corporation, organised 1996-08-22** | `S96-8B12B` §1(a) L108-109 | High |
| Predecessor and mechanism | **Melville Corporation, a New York corporation**, "which will be the predecessor of the Registrant at the time of the succession"; reincorporation by triangular merger; survivor renamed **CVS New York, Inc.** | `S96-8B12B` §2(a) L115-116; L120-142 | High |
| Registration instrument | **8-B12B**, filed **1996-11-04**, Section 12(b)/(g) successor registration; NYSE; $.01 par | `S96-8B12B` L66-96 | High |
| Is there an IPO filing? | **No.** Measured in the registrant's own EDGAR index (2,968 rows): `S-1` **0**, `S-1/A` **0**, `SB-2` **0**, `10-A` **0**, `8-B12B` **1**. The only 1996 "initial public offering" named in the S-4 is somebody else's: *"initial public offering for CVS' former subsidiary, Linens 'n Things, Inc."* (`S97-S4` L3184) | `sources/_index/submissions_CIK0000064803.csv`; `S97-S4` | High — **U.03** |
| State of incorporation before | **New York** (Melville), self-described in its own 10-Ks | `K93` L147-149 | High |
| Name change | **EDGAR-recorded:** `MELVILLE SHOE CORP` → `MELVILLE CORP`, date of name change **1976-06-30**, printed in the header of every stored file; brand name change **November 1996** | headers; `S97-S4` L767 | High (the record of it) |
| Identity metadata | EDGAR `former_names` for CIK 64803: `MELVILLE CORP`, `CVS CORP`, `CVS/CAREMARK CORP`, `CVS CAREMARK CORP` — i.e. the modern brand is a **renaming of the shoe company's CIK**, and it is *metadata*, not document text | `sources/_index/_registrant_CIK0000064803.json` | High (as a fact about the index row); **not** evidence of any event |
| Headquarters | Registrant: **One CVS Drive, Woonsocket, RI 02895** (`S96-8B12B` L85; `K96-405` L172). Predecessor's principal office: **Rye, New York** (`K95` L177); Melville results were datelined **Harrison, N.Y.** in the trade press (`DSN-88`) | as cited | High |
| Employees | Melville consolidated **≈97,000** full and part-time "associates" at 1995-12-31. **No CVS-chain-only headcount is filed in-window** | `K95` L178 | High (consolidated); UNKNOWN (chain-only) |
| Segment shape, 1993 | Drug/HBC was **one of four-to-five retail legs**; its stores ran under the `"CVS", "Peoples", "Standard Drug" and "Austin Drug" trade names` and the segment was **≈38% of consolidated net sales** | `K93` L158-161, L249-263 | High |
| The estate's legal stack at FY1996 | Registrant → **CVS New York, Inc.** (NY) → **CVS Center, Inc.** (NH) → **CVS Pharmacy, Inc.** (RI, *"formerly known as CVS, Inc."*) and **CVS H.C., Inc.** (MN) → **Nashua Hollis CVS, Inc.** (NH) → **≈1,145** operating subsidiaries; plus **CVS of DC & VA, Inc.** (MD) and **Melville Realty Company, Inc.** (NY) | `K96-405` L8349-8376 | High |

### B.3 The fifteen persons the bytes actually name, and the 1963 question

`CVS, Inc.` (RI, `K94` subsidiary list) · `CVS Pharmacy, Inc.` (RI, renamed from CVS, Inc., `K96-405` L8368) ·
`CVS Center, Inc.` · `CVS H.C., Inc.` (MN) · `Nashua Hollis CVS, Inc.` (NH) · `CVS of DC & VA, Inc.` (MD) ·
`CVS Corporation` (DE, 1996-08-22) · `CVS New York, Inc.` (the renamed survivor **and** the merger subsidiary, the same
name used twice in one instrument) · `Peoples' Drug Stores, Incorporated` (MD) · `Standard Drug` · `Austin Drug` ·
`Pharmacare` / `Pharmacare Management Services, Inc.` (DE) · `Melville Corporation` (NY) · `Melville Shoe Corporation`
(the same CIK's former name) · `Melville Realty Company, Inc.` (NY).
**None is dated 1963 in any held byte, and none is described as the 1963 company.** The recital's grammar matters:
*"Founded in 1963, **CVS** is the country's fifth largest drugstore chain"* — the subject is a **chain**, a business,
not a corporate person, and the same document spends its next sentence renaming a **New York corporation**. Which
legal person "CVS" was in 1963 is **U.01**, the load-bearing conflict of this dossier, and the route that could close
it is named in §S (`R-1` was run; what it added is measured at §U.02 — still no named 1963 person).

STATUS: WRITTEN 2026-10-06

## C. ORIGINAL PROBLEM

### C.1 The 1963 problem — UNKNOWN, and the honest statement of it

**UNKNOWN.** No held byte states what problem the 1963 enterprise was answering, because no held byte names the 1963
enterprise at all. Measured across the 36 stored SEC files and the 18 periodical-side text layers: **0** occurrences
of a founding town in a CVS context, **0** of a founder, **0** of a first store, **0** of a business type attached to
1963 (§B.1). The dispatch brief's fuller story — a shoe-box retailer's origin, the spelled-out chain name as *the*
1963 entity, and the **Riverside–Newport** naming pair — is recorded here as **U.02** and is
**not** written as fact anywhere in this dossier. The route that could still name it is in §S.1–§S.2 (`R-1` **run**,
its yield measured; `R-3`, `R-4`, `R-5` **open**).

### C.2 The problem the registrant itself states, in-window — and it is a *scale* problem, not an origin one

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Stated problem | Achieving **critical mass** and geographic fit as the condition of competing at all: *"Achieving a critical mass in terms of store count and locating our stores in appropriate geographic markets is essential to competing effectively in the chain drugstore industry as well as with alternative distribution channels such as combination food/drug stores, mail order and mass merchandisers."* | `S97-S4` L784-787 [CVS-A10] | High (as filed words); Medium (as a motive — the registrant's own account of its own reason) |
| Stated response to consolidation | *"In light of the significant consolidation in the industry during 1996, CVS believed that, to accomplish its long-term objectives, it should explore opportunities for growth through strategic acquisitions meeting CVS' acquisition criteria."* | `S97-S4` L1579-1582 | High |
| Organic growth arithmetic filed | *"CVS acquired Peoples Drugs Stores in 1990 and Standard Drug Stores in 1994, and has added an average of 77 stores in each of the past five years through new store openings, relocations, and small acquisitions"* — note the filing's own spelling `Peoples Drugs Stores` | `S97-S4` L1575-1579 [CVS-A11] | High (filed words); the 5-year base period is the filing's, 1992-1996 |
| Parent-level problem it was also answering | Melville's 1994 **strategic review** → 1995 **Board-approved restructuring program** → 1996 completion and rename (`S97-S4` L767-770); 29 `restructur*` hits in `K96-405`; footwear classified **discontinued operations** pending a 1996 spin (`K95` L197-200); Kay-Bee agreed to be sold (`K95` L150-152) | as cited | High |
| What the problem was **not**, on this corpus | Not a pharmacy-innovation problem and not a health-benefit problem in 1963 terms: the only benefit-technology act in the window is `Pharmacare, founded in 1994`, whose stated job is plan design, formulary management, claims processing and generic substitution (`K96-405` L469-472) | as cited | High (as filed); U.05 for the lineage claim |

### C.3 Two legs the corpus does **not** support a Stage-1 claim about

**(i) Insurance.** The held bytes name **no insurance underwriter and no HMO** at any date. The only `insurance`
substance in the post-window 10-Ks is risk retention for the retailer's own liabilities: *"The Company is
self-insured for general liability, workers' [compensation]…"* (`K00` L1741; cf. `K99` L3357). The registrant's later
name-change metadata (`CVS/CAREMARK CORP`) and the eventual insurer leg are **out of window and out of corpus**; they
may not be back-dated into Stage 1. **(ii) The pharmacy-benefit line.** `Caremark` occurs **0 times in all 36 stored
SEC files**; the PBM leg inside the window is **Pharmacare**, separately dated **1994** by the registrant's own
recital, and the Medicare-facing content in the bytes is thin and late (a pharmacist-counselling line about
*"customers covered by Medicare"*, `K98` L599; Part D does not exist yet in-window). **Class: FACT as to what the
bytes say; UNKNOWN as to any earlier date for either leg.**

---

## D. FIRST EXPERIMENT

### D.1 The stage's first experiment is unrecorded

**UNKNOWN — and the null is measured, not assumed.** The window in which a first CVS experiment would sit (1963–1968)
has **0 bytes of any family** in this company directory: EDGAR floor 1994-02-10; oldest held periodical issue-date
**1979-10-29**; family (b) web archives and (e) auction/manuscript **UNTRIED, 0 calls**; family (d) **zero corporate
print** (§T.2). What could answer it is named in §S; nothing on disk does.

### D.2 The earliest held act that behaves like a first test — 1983, and it is a distribution decision

The oldest CVS-bearing **prose** in the corpus, issue-dated inside the file rather than by scan metadata:

> **Drug Store News, November 14, 1983**, headline `CVS weighs warehouse growth in three regions`, dateline
> **WOONSOCKET, R.I.**: *"Anticipating the opening of at least 50 new stores each year, Con-/sumer Value Stores (CVS)
> has announced tentative plans for the construction or lease of a 150,000-sq.-ft. bulk storage and promotional goods
> warehouse here."* — the OCR breaks the name across a hyphenated line; transcribed as printed at `DSN-8384`
> L1779-1794 [CVS-A12].

**Class: CONTEMPORANEOUS OBSERVATION** (third-party trade press, near the event, of a company announcement);
**Confidence: Medium, capped by transport (§Header)** — the sidecar says `UNVERIFIED TLS`. **What it demonstrates:**
by 1983 the chain named *Consumer Value Stores*, glossed **(CVS)**, was **headquartered in the same Rhode Island town
it still occupies**, planned **≥50 openings a year**, and had **outgrown two leased Woonsocket-area buildings**.
**What it does not demonstrate:** any founding, any predecessor format, any footwear connection, or that the estate
was then profitable — it is a warehouse decision, not an origin story. The **class distinction matters here**: this
is the only held row that spells the chain name *and* glosses it as CVS, which is exactly the naming evidence a
genealogy needs and exactly the row the probe's 1990-1994 window missed (§U.10).

### D.3 The scale test the filings do record, 1989→1996

| Beat | Filed / observed value | Carrier | Class |
|---|---|---|---|
| Estate, 1989 close | *"CVS ended the year with **789 stores, 582 with pharmacies**"*; plans to open 50 more in 1990 | `DSN-8990` L32990-32994 (issue 1990-04-09) | CONTEMPORANEOUS OBSERVATION, Medium |
| Chain sales, 1989 | *"CVS sales in 1989 totaled **$1.02 billion**. Peoples had $1.02 bil-…"* | `DSN-8990` L61811 (issue 1990-09-24) | CONTEMPORANEOUS OBSERVATION, Medium; **conflicts with the same paper's own box, U.04** |
| Acquisition test, 1990-09-17 | Melville, *"which operates **820-store CVS**"*, completed the purchase of **490-store Peoples Drug Stores** from Imasco Ltd. for **$325 million in cash**; the Peoples stores would *"keep their name"* | `DSN-8990` L61806-61817 (issue 1990-09-24) [CVS-A13] | CONTEMPORANEOUS OBSERVATION, Medium — corroborated in *scope* by the registrant's later one-line recital (`S97-S4` L1576), which gives the year only |
| Estate, FY1993 | **1,284** drug/HBC stores in **15 states + DC**, **1,081 with pharmacies**, **≈38%** of consolidated net sales | `K93` L249-263 | FACT, High |
| Estate, FY1996 | **1,408** stores in **14 states + DC**; $2.4 bn pharmacy / $3.1 bn front store; $573/sq ft | `K96-405` L158-170 | FACT, High |

**What was learned, narrowly:** that a chain could add ~500 stores and 1.3× revenue between 1989 and FY1993 while
remaining **one segment of a diversified New York parent**, and that buying a second chain's *name* as well as its
stores was possible (Peoples kept its name, then was renamed — `DSN-9495` L21684: *"the 400 former Peoples stores
(renamed CVS stores last year)"*, issue-dated inside the 1994-11→1995-10 layer, **Medium**). **What was NOT learned:**
unit economics of the 1963 format (no data), the durability of the acquired estate (segment store count *falls* from
1,284 in FY1993 to 1,408 in FY1996 only after adding States, and the trade boxes disagree), and whether the drug leg
could stand alone as a registrant — the question the 1996 succession was answering.

---

## E. PRODUCT RECONSTRUCTION (retail-format adaptation, §7)

**The offer, as the registrant filed it at FY1996** (`K96-405` L158-170): a drugstore whose **prescription business is
the minority of sales and the traffic engine** — pharmacy **43.9%** of total sales, front store **56.1%** — selling
*"a broad selection of health and beauty aids, greeting cards, photo processing services, cosmetics, convenience
foods, private label and seasonal items"*, in *"1,408 stores … most of which have pharmacies"* [CVS-A04]. **The
format as filed in 1993** (`K93` L265-266): *"These stores are considered 'destination' stores and are located
primarily in 'strip' shopping centers and freestanding units."* **Trade-name carriage**: the same estate ran under
four names in FY1993 — `"CVS", "Peoples", "Standard Drug" and "Austin Drug"` (`K93` L158-161) — so "the product" is
not one storefront; it is a **multi-name estate inside one segment**. **Density claims** (filed, company-measured, no
independent check): **~1,200 prescriptions per pharmacy per week**, *"significantly higher than the average community
pharmacy"*, and **$573 sales per square foot** (`K96-405` L167-170) — both are self-reported comparatives with no
filed denominator, recorded as such. **Third-party format parameters**: store size **8,800 square feet**, markets
*"Northeast and Mid-Atlantic states; Ohio, Michigan and California"* (`DSN-9091` at-a-glance box, issue 1991-05-06,
**Medium**). **The second product** — the PBM — is a service, not a store: *"plan design and administration, formulary
management, claims processing and generic substitution"* (`K96-405` L469-472), with the registrant's own
differentiation claim *"its proprietary Clinical [management system]"* appearing post-window (`K00` L226-233).

**E.1 What cannot be reconstructed.** No 1963–1979 product exists in any held byte: no price, no shelf, no first
private label, no first pharmacy license, no store count. The **1980** directory line — *`. CVS Stores, Woonsocket,
R.!. Baton Rouge, La.`* (`DSN-7980` L14496) — is the only 1980s row that places the chain in a **supplier/wholesaler
roster**, and its `R.!` is an OCR decoy for `R.I.`; it is cited as a pointer to a listing, **not** as a product
description. **Class: UNKNOWN, route named (§S.1, §S.2, §S.4).**

STATUS: WRITTEN 2026-10-06

## F. CUSTOMER

**Who the registrant says bought, in-window.** The FY1996 filing describes the store's two customers implicitly by its
two sales lines: prescription (**43.9%**) and front store (**56.1%**), with *"about 1,200 prescriptions a week"* per
pharmacy and *"most"* of 1,408 stores holding a pharmacy (`K96-405` L160-168). The **third-party** description of the
customer is the same estate's **geography**, not a count: *Markets: "11 Northeastern states, Ohio, Michigan and
Califor-"* (`DSN-8990`, issue 1990-04-09) and *Markets: "Northeast and Mid-Atlantic states; Ohio, Mich-igan and
California"* (`DSN-9091`, issue 1991-05-06). The PBM's customer is a different animal and the registrant names it:
Pharmacare *"provides **managed care providers** a full range of prescription benefit management services"* and at the
end of 1996 *"managed healthcare services for **more than one million people** through a preferred national pharmacy
network"* (`K96-405` L469-475) — **covered lives, not shoppers**, and a **separately dated act (1994)** (§C.3).

| Variable | Value | Source | Confidence |
|---|---|---|---|
| First customer | **UNKNOWN** — no carrier in any family. Nothing on disk names a 1963 transaction, customer, or receipt | Term census (§B.1) | High (that it is absent); routes §S.1, §S.4, §S.5 |
| Customer count / transactions | **UNKNOWN in-window.** No filed customer, order or prescription **total** exists for the chain; the only density figure is the per-store weekly average, self-reported | `K96-405` L167-169 | High (of the absence) |
| Second-party customer measure held | Two market-level **H&BA shopping surveys** — *"Where Chicago Consumers Prefer to Shop for H&BA"* and *"Where Atlanta Consumers Prefer to Shop for H&BA (% of consumers older than 14)"* — carry `CVS` in a column of chain names with **no legible percentages** | `DSN-8990` L6346-6347, L6395-6399 (layer 1989-11→1990-10) | **Low** — recorded, **not** used |
| Loyalty / retention, mail order, price response | **UNKNOWN.** No 1990s CVS loyalty, churn, basket or mail-order figure is on disk | — | High (of the absence) |

**F.1 Knowability (§7).** `KNOWABLE` in-period: the estate's state footprint, the pharmacy/front split, the covered-lives
count. `NOT KNOWABLE`: 1963–1979 customer identity, mix, or any unit-level economics — *because the archive that was
kept is the registrant's disclosure archive, which begins in 1994*. `UNKNOWN`: everything the folk story requires.

---

## G. SUPPLY / HOST SIDE (retail: supply chain and estate)

**Distribution, as third parties reported it.** Supporting *"at least 50 new stores each year"* in 1983 meant
**building a warehouse**: tentative plans for *"a 150,000-sq.-ft. bulk storage and promotional goods warehouse"* in
Woonsocket, to *"replace much of the storage space currently leased by CVS in two Woonsocket-area buildings"*
(`DSN-8384`, issue 1983-11-14) [CVS-A12]. Seven years later the same paper reports the outcome in one line: *"To
support this growth, CVS increased distribution capacity by [~]a 400,000-square-foot DC in New Jersey. That raised the
chain's warehousing footage to 2,075,000 square feet"* (`DSN-8990` L32996-32999, issue 1990-04-09; the bracketed word
is OCR corruption — the sentence is quoted **with** the defect and the figure stays **Medium**) [CVS-A14].

**The host/landlord leg is in the corporate stack, not the narrative.** At FY1996 the registrant's own subsidiary
tree puts real estate **under the operating pharmacy company**: *"CVS Pharmacy, Inc. (formerly known as CVS, Inc.) is
the parent corporation of Melville Realty Company, Inc., a New York corporation, which is the parent corporation of
Melville Realty Management Corporation, MREFC, Inc., Danbury MRC, Inc., MRC Manchester Devco, Inc., … MRC Staten
Island Devco, Inc."* (`K96-405` L8368-8373), and **`Nashua Hollis CVS, Inc.` is the parent of *"approximately 1,145
subsi[diaries] which were formed to operate specialty retail [stores]"*** (L8356-8357) [CVS-A15]. **INFERENCE, held
narrowly:** the estate's leases were carried in single-store or small-group holding entities under a New Hampshire
parent — a structure that shows up in the bytes only *after* the 1996 succession, and whose earlier history is not
recoverable from this corpus.

**Vendor and merchandise terms.** **UNKNOWN.** No stored in-window filing names a drug wholesaler, a supplier
concentration percentage, a distribution agreement, or credit terms for the CVS estate. The FY1993/FY1994 10-Ks
describe **segments and trade names**, not procurement; `K94`'s subsidiary list names operating persons, not contracts.
(Contrast is instructive, not evidence: a *sibling* dossier in this project could read vendor concentration out of an
S-1 in 1997 because that filing was a flotation document; **CIK 64803 filed no S-1** — §B.2 — so the disclosure that
would force the answer never happened.)

**Labour.** Melville consolidated **≈97,000 full and part-time associates** at 1995-12-31 (`K95` L178). **No
chain-level CVS headcount is filed in-window**, and no wage, benefit or pharmacist-staffing figure is held. The 1996
succession transferred *"all Melville employee and director stock-based benefits or compensation plans"* to CVS
(`S96-8B12B` L190-192) — a plan-level fact, not a headcount.

---

## H. MARKET (as knowable inside the period)

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Category position, registrant's own words, 1996 | *"the country's **fifth largest** drugstore chain in terms of store count and sales volume, with approximately 1,400 stores and $5.5 billion in 1996 annual revenue. CVS operates in 14 states along the **Northeastern seaboard and the District of Columbia**"* | `S97-S4` L762-765 [CVS-A06] | Medium (self-report, one lineage, 34 years after the claimed origin, and its **own** present-tense claim) |
| The number two, as filed in the same document | *"Revco is the country's **second largest** drugstore chain in terms of store count and **third** in terms of sales volume, with approximately 2,600 stores and $5.3 billion in annual revenues. Revco operates in 17 contiguous Midwestern, Eastern and Southeastern states"* | `S97-S4` L777-780 | High (as a filed description of a counterparty) |
| Channels the registrant treats as the market's real constraint | *"alternative distribution channels such as combination food/drug stores, mail order and mass merchandisers"* | `S97-S4` L786-788 | High (as words); Medium (as market share — no figure attached anywhere) |
| Industry state the registrant noticed | *"significant consolidation in the industry **during 1996**"* | `S97-S4` L1579-1580 | High |
| How the **parent** benchmarked itself in 1994 — the market as then knowable | Melville's own FY1993 proxy peer set: **Dayton Hudson, Edison Brothers, JC Penney, Longs Drug, Merry Go Round, Rite Aid, Sears, TJX, Toys R Us, U.S. Shoe, Walgreen, Woolworth** | `P94` (DEF 14A 1994-03-14) compensation peer list [CVS-A16] | **High — and decisive for the firewall**: in 1994 the registrant measured itself against **department stores and toy chains**, not against a health-services market. The drug leg was **38% of net sales** (`K93` L262-263). |
| Season | *"The Christmas holiday is the most significant seasonal selling period for the Company overall"*; peak periods for non-leather apparel and footwear coincide with Easter and back-to-school | `K95` L169-173 | High (consolidated, i.e. the parent's seasonality, not the chain's) |
| Category dollar size | **UNKNOWN.** No held byte states a U.S. chain-drug market size, growth rate, or share denominator in-window | — | High (of the absence); route §S.3 (`R-3` facet-free corporate print; almanac rows on disk are 1997-2020 and out of window, §S.7) |

**H.1 The knowability asymmetry this stage has to state plainly.** For the drug estate the market is
**KNOWABLE from 1980 onward** (third-party trade press naming the chain, its parent, its markets and its warehouse
decisions) and **KNOWABLE from 1994-02-10 on the registrant's own paper**. For **1963–1979 it is NOT KNOWABLE from
this corpus at all** — and the reason is mechanical: EDGAR's index for this CIK has **0 rows before 1994-01-01**, and
the oldest issue-dated press on disk is **1979-10-29**. That is a **perimeter**, not a claim that nothing existed.

---

## I. COMPETITION

**Inside the estate — competitors bought rather than beaten.** The FY1993 estate ran four trade names at once
(`"CVS", "Peoples", "Standard Drug", "Austin Drug"`, `K93` L158-161), because two chains had been absorbed:
*"CVS acquired Peoples Drugs Stores in **1990** and Standard Drug Stores in **1994**"* (`S97-S4` L1576-1577). The
trade press dates and prices the Peoples act more precisely than the registrant ever does: **490 stores, $325 million
in cash, completed Sept. 17, from Imasco Ltd. of Montreal**, with the acquired name kept (`DSN-8990`, issue
1990-09-24) [CVS-A13] — and then, four years later, the reversal: *"the 400 former Peoples stores (renamed CVS stores
last year)"* (`DSN-9495`) [CVS-A17]. **This is the competitive history the bytes actually support: consolidation by
purchase inside one parent, and the erasure of acquired names, 1990–1995.**

**Outside the estate.** The 1994 peer list (`P94`, §H) is the registrant's own enumeration of whom it watched;
within it, **Longs Drug, Rite Aid and Walgreen** are the drug chains and the rest are general retailers. The FY1996
filing's comparative is *"significantly higher than the average community pharmacy"* (`K96-405` L167-169) — an
unmeasured independent operator, no name, no figure. The trade press supplies two named **convenience-format**
observations the registrant never files: a 1988 row that *"Among newer entrants are
CVS, Walgreens and Long Is[-…]"* in a category context (`DSN-88` L6142-6143; the layer carries 220 dated mastheads
spanning **1987-11-09 → 1988-10-24** and the governing issue for this line was **not separately pinned** — recorded as
a limitation, not resolved) and a 1990/91 survey sentence listing
`CVS` beside `Osco`, `Walgreens`, `Rite Aid`, `Duane Reade` (`DSN-8990`, `DSN-9091`). Both are **Medium**, and both
are **brand-adjacency** rows, not entity-naming rows (§Header discipline 1).

**I.1 Two competitor rows that must not be laundered into CVS history.** (i) *"…just how far this company has come
since its founder opened **Civic Drugs in Dearborn, Mich. in 1963**"* (`DSN-9091` L40103-40105) — a **rival chain's
founding, in the same year, in the same shelf**. Any later pass that greps `1963 + founder + opened`
finds this sentence and will produce the wrong company. Registered as **U.06**. (ii) **Woolworth** appears 16 times
in the 1989/90 layer and 13 times in the 1985 layer because **Peoples was a Woolworth chain before Melville** — a
*third* lineage crossing the same words (§U.04 note).

**I.2 What competition cannot be said to have done.** Nothing in this corpus supports a claim that incumbents were
complacent, that the format was open, or that consolidation made a national chain inevitable. **Mechanism UNKNOWN**
for every such inference; the firewall (§2) applies.

STATUS: WRITTEN 2026-10-06

## J. TECHNOLOGY

**J.1 What the bytes actually hold.** No in-window filing names a system, a vendor, a protocol or a capitalised
technology programme for the store estate. What exists is **format-level** and **service-level**: *photo processing
services* inside the merchandise list (`K96-405` L163); the PBM's operating functions — *"plan design and
administration, formulary management, claims processing and generic substitution"* (`K96-405` L469-472); and, only
post-window, the registrant's own differentiation claim that what sets the PBM apart from other providers *"is its
proprietary Clinical [management] system"* (`K00` L226-233) — labelled **(PB)**. The trade press supplies one
adjacency-level line for the chain: *"Solid sales from the 400 former Peoples stores (renamed CVS stores last year),
gains in pharmacy sales, **new technology** and a shift to category management were the major [drivers]"*
(`DSN-9495` L21683-21687) — an unquantified phrase, recorded, **not** converted into a claim.

**J.2 The decoy that must be named here, because column layout manufactures it.** In the same 1990/91 layer, the
sentence *"Shoppers is emphasizing technology: Most of its stores have computerized accounting systems, and all stores
have…"* ends **three lines above** the heading `CVS at a glance` (`DSN-9091` L38070-38074). A reader — or a later
grep — that attributes the computerised-accounting sentence to CVS is reading a **rival chain's** paragraph across a
box rule. **This volume does not attribute it.** Registered in §T.6 as the class of defect the adjacency rule exists
to stop.

**J.3 Status.** 1963–1979 technology of the origin format: **UNKNOWN** (0 bytes; route §S.1/§S.4). In-window store
systems, pharmacy systems, PBM architecture: **UNKNOWN** as to supplier, cost, deployment date and effect.
**Mechanism UNKNOWN** for any claim that technology drove the 1989→1996 estate growth; the filed drivers are
acquisitions, openings, renamings and category management (`S97-S4` L1575-1579).

---

## K. MONEY / PERSONAL FINANCES — **register-shaped by tier** (§15.2: S1a/S1b/S1c are T3, so the money of the origin
window is delivered as an argumented gap, not as a narrative)

### K.1 The origin window, 1963–1979

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Founder's personal capital, salary, guarantees, side income | **UNKNOWN — and structurally so.** No founder exists in the record (§B.1); there is no `Certain Transactions`-style related-party disclosure because **no flotation instrument was ever filed** (`S-1`/`S-1/A`/`SB-2`/`10-A` = 0 of 2,968 rows) | `sources/_index/submissions_CIK0000064803.csv` | High (of the absence) |
| Opening cost, first lease, first inventory, first-year sales | **UNKNOWN.** No lease, no receipt, no ledger; families (b) and (e) **UNTRIED**; family (d) **zero bytes** | §T.1–T.2 | High (of the absence); routes `R-3`, `R-4`, `R-5` |
| Any 1963–1979 dollar attached to CVS anywhere on disk | **0.** The only `1963` digits in the press layers are other companies' stock quotes, copyright years, and **a rival's founding** (`DSN-8384` L917, L2313, L7199 — 10 `1963` hits in that layer, **0** of them this company; `DSN-9091` L40103-40105) | term census | High |

### K.2 The parent's money, 1994–1996 — filed, consolidated, and **not** the chain's

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Melville consolidated sales, 1994 | **$11.3 billion** | `K8-95` L236 | High |
| Marshalls' share of it, 1994 | **$2.8 billion**, from 495 stores in 40 states and Puerto Rico at 1995-09-30 | `K8-95` L234-236 | High |
| Marshalls sale price | **≈$550 million** = **$375,000,000 cash** + preferred with **$175,000,000** aggregate liquidation preference; agreement dated **1995-10-14**, announced 1995-10-16, **consummated 1995-11-17** | `K8-95` L196-200; `D96-TJX` L396-406 | High |
| Consideration's internal route | On or about **1996-03-15** Melville transferred the Series D/E preferred to **CVS Center, Inc.**, which transferred to **CVS H.C., Inc.**, which transferred to **Nashua CVS** | `D96-TJX` L474-477 [CVS-A18] | High |
| Cost of becoming a drugstore company | Q4-1995 **after-tax charge of $585 million** on completing the strategic review, **excluding** a previously announced **$195 million** estimated after-tax charge for the Marshalls divestiture; of the additional charge, **$230 million** for asset write-offs and severance | `K8-95` L408-414 [CVS-A19] | High |
| Debt capacity on file | Shelf registration for up to **$300 million** in debt securities including medium-term notes; *"No debt securities have been issued to date"* | `K95` L163-167 | High (FY1995 basis) |
| Drug segment's weight | drug/HBC stores = **≈38% of consolidated net sales**, FY1993 | `K93` L262-263 | High |
| Chain revenue at the close | *"over $5.5 billion in revenue in 1996"*: pharmacy **$2.4 bn** (+18.4%, 43.9%), front store **$3.1 bn** (+9.3%, 56.1%) | `K96-405` L158-167 | High |
| Peoples purchase, 1990 | **$325 million in cash** for 490 stores from Imasco Ltd.; CVS then operated 820 stores | `DSN-8990` L61806-61811 (1990-09-24) | **Medium** (TLS cap; the registrant's own recital gives the year but **no price**) |
| PBM scale at the close | Pharmacare *"managed healthcare services for more than one million people"* at end-1996 | `K96-405` L473-475 | High (filed, self-measured) |
| Dividend, borrowings, capex, segment profit for the **chain** | **UNKNOWN** in-window — no stored in-window filing carries a CVS-segment P&L; the FY1990–FY1992 annual reports are **not on disk** (EDGAR floor 1994-02-10) | §S.3 | High (of the absence) |

**K.3 What must never be done with the above.** The $11.3 bn, the $550 m and the $585 m are **Melville Corporation**
figures; the $5.5 bn, the 1,408 stores and the >1 m covered lives are **CVS Corporation** figures for the same year,
1996, from two different legal persons in one transition year. Any ratio built across the two rows is **DERIVED and
must be labelled as such**, and none is built in this volume.

---

## L. VALIDATION SIGNALS

| Date | Signal | Magnitude | What it demonstrated | What it did NOT demonstrate | Source | Confidence |
|---|---|---|---|---|---|---|
| 1980-01-21 | The chain appears by its spelled-out name in a competitive-roundup sentence in the national trade paper, described as **Rhode Island-based** | 1 row | By 1980 *Consumer Value Stores* was a named national-market participant with a home state | Any origin fact, any date before 1980 | `DSN-7980` L7662 | Medium |
| 1983-11-14 | Announced a **150,000-sq.-ft. own warehouse** to replace two leased buildings, planning **≥50 openings/yr** | estate infrastructure | The chain was investing in fixed distribution capacity rather than renting it — a scale commitment, not a start-up posture | Unit economics; that the plan was executed | `DSN-8384` L1779-1800 [CVS-A12] | Medium |
| 1989 close | **789 stores, 582 with pharmacies** in the estate; box markets = 11 Northeastern states + Ohio, Michigan, California | +73.5% pharmacies-of-stores (DERIVED: 582/789) | A **pharmacy-attached** format at ~3/4 of stores before the Peoples purchase | Consolidated or segment revenue; profit | `DSN-8990` L32990-32994, L33016-33020 | Medium |
| 1990-09-17 | A **second drug chain bought and kept its name** (490 Peoples stores, $325 m cash) | estate +62% (DERIVED: 490/789) | The parent was willing to buy scale in the drug leg, in cash | Whether the bought estate was accretive — no segment P&L on disk | `DSN-8990` L61806-61817 | Medium |
| FY1993 | **1,284 stores / 1,081 with pharmacies**, ≈38% of consolidated net sales | 84.2% pharmacy attach (DERIVED: 1,081/1,284) | Filed, audited-context confirmation that the drug leg was the largest single leg by attach, not yet by share | That the leg could stand alone as a registrant | `K93` L249-263 | High |
| 1995-11-17 | Marshalls, the biggest apparel leg ($2.8 bn of 1994 sales), **sold** | −$2.8 bn of sales legs | The parent was converting a diversified retailer into a drug-and-toys retailer for cash + preferred | That a pure drug company would earn more | `K8-95`, `D96-TJX` | High |
| 1996-08-22 → Nov | **Delaware holding company organised; predecessor survives as `CVS New York, Inc.`; name changed to CVS Corporation** | legal form | The brand had become the registrant — the condition for Stage 2 disclosure | Any operating improvement; also: **the bytes do not record the Effective Time** | `S96-8B12B` L108-142 | High |
| FY1996 close | **1,408 stores, $2.4 bn pharmacy (+18.4%), $573/sq ft, ~1,200 scripts/wk per pharmacy** | filed ratios | A density-and-productivity story the registrant chose to file at exactly the moment it needed to describe itself to bondholders and to Revco shareholders | Independent verification of the "vs community pharmacy" comparative, which has no filed denominator | `K96-405` L158-170 | High |

**L.1 The pattern, held to what the evidence can carry.** The signals that exist are **estate** signals — stores,
pharmacy attach, warehouses, acquisitions, divestitures, legal form. **There is no demand-side validation anywhere in
the corpus**: no customer count, no same-store sales, no market share, no repeat measure, in-window. For a chain
registrant, §7's adaptation (`stores / supply chain / same-store sales`) is therefore **half-answerable**: two of the
three exist, the third is a measured absence (§S.3).

---

## M. NEGATIVE SIGNALS AND FAILURES

| Date | Signal or failure | Magnitude | What it demonstrated | What it did NOT demonstrate | Source | Confidence |
|---|---|---|---|---|---|---|
| 1994 (self-reported) | A **strategic review was initiated** because the parent's shape needed answering | 1 sentence, retrospective | The diversified portfolio was not being treated as an asset by management itself | That diversification had failed in sales terms | `S97-S4` L767-770 | High (as a recital); Medium (as motive) |
| Q4-1995 | **$585 m after-tax charge**, plus a separate **$195 m** estimated charge for the Marshalls divestiture, plus **$230 m** of write-offs and severance | ≈$780 m of charges in one quarter across two announcements | Exiting legs was **expensive**, and the registrant filed the cost | Causation to the drug business's prospects | `K8-95` L408-414 [CVS-A19] | High |
| 1995-10-16 (filed) | Marshalls sale *"will reduce fourth quarter operating earnings, due to the significant amount of Marshalls' business done during the Christmas season"* | unquantified | A divestiture that **hurt** the current quarter's earnings by design | Any later outcome | `K8-95` L230-232 | High |
| FY1995 | Footwear reclassified **discontinued operations**; Kay-Bee agreed to be sold; Wilsons and *This End Up* marked for sale | three legs in exit | The parent the folk story needs — a shoe company — was **actively ceasing to be one** inside the window | That the drug leg was wanted for its own sake rather than as the only leg left | `K95` L150-152, L197-200; `K8-95` L399-404 | High |
| 1990-09-17 → 1995 | The bought name was **erased**: *"the 400 former Peoples stores (renamed CVS stores last year)"* | 400+ stores renamed | The chain's growth included the **deletion of acquired identities** — the estate's name-history is not a clean line | That Customers cared; no customer-side measure exists | `DSN-9495` L21683-21685 | Medium |
| whole window | **No failure of the origin enterprise is recorded anywhere.** No 1963–1979 closure, loss, bankruptcy, dispute or rebuffed expansion appears | 0 rows | Nothing — the silence is the finding | That none occurred. **Record-selection null (§2)** | §S.6 | High (of the silence) |
| **disclosure-side failure (this run's own)** | The fleet ledger `00_universe/_FLEET_INTAKE.tsv` still reports `pass2_status` **empty** / `pass2_docs 0`, while `sources/sec/_RUN.json` records a completed **1997-01-01..2006-12-31** pass with `stored 28`, `attempted 128`, `identity_ok **false**` and 6 `duplicate_slots` | 2 records disagreeing about reality | An intake record that no longer describes the corpus on disk (RD-134 class). **Reported, not repaired** — not this agent's file | That the bytes are wrong: the 36 stored files carry sidecars and are self-consistent | `_RUN.json`; `_FLEET_INTAKE.tsv` cvs row | High |

STATUS: WRITTEN 2026-10-06

## N. DECISIONS (registrant-level; **no founder decision exists in this corpus** — §B.1)

The unit that decides, on these bytes, is a **board and its officers**, not a founder. Each row below is a decision
*the record dates*; rationale is given only where the filing states it, and is marked as the filing's own account.
Full-width rows for `decisions.csv` are in `## registers`.

| Date | Decision | State before | Alternatives visible then | Rationale as filed | Confidence |
|---|---|---|---|---|---|
| 1994 | **Initiate a strategic review** of the diversified portfolio | Melville = drugs + apparel + footwear + toys/home, ≈$11.3 bn sales (1994) | none recorded — no rejected option survives | retrospective one-line recital | High (recital exists); Low (its motive) |
| 1995 | **Board approves the restructuring program** | review under way | — | *"its restructuring program that was approved by its Board in 1995"* (`S97-S4` L769) | High |
| 1995-10-14 | **Sell Marshalls** (495 stores, $2.8 bn of 1994 sales) to TJX for ≈$550 m = $375 m cash + $175 m convertible preferred | largest apparel leg inside the parent | take cash only? not recorded | *"an excellent opportunity for Marshalls… Melville shareholders will continue to benefit"* via the equity interest (`K8-95` L222-224) — the buyer's CEO quoted in the seller's 8-K | High |
| 1995-11-17 | **Consume the consideration as preferred stock, not cash out** | SPA signed | sell for cash and distribute | not stated; the standstill/registration agreement limits disposal (`D96-TJX` L429-448) | High (that it happened); UNKNOWN (why held) |
| 1996-03-15 | **Push the TJX preferred down the stack**: Melville → `CVS Center, Inc.` → `CVS H.C., Inc.` → `Nashua CVS` | preferred held at the parent | keep at parent | not stated — **four months before the Delaware company is organised**, the drug-side holding chain is loaded with the parent's best asset | High (filed sequence); **INFERENCE** as to purpose, held narrowly |
| 1996-08-22 | **Organise CVS Corporation under Delaware law** | New York parent, reincorporation proposal pending | remain in New York | charter/bylaw differences enumerated (`S96-8B12B` L195-212) | High |
| 1996-08-30 | **Sign the Agreement and Plan of Merger** (Melville, CVS, Merger Subsidiary) | Delaware entity exists on paper | direct re-domestication? not discussed | the triangular-merger mechanic is the proposal's own architecture (L136-150) | High |
| 1996-10-07 | **Mail the proxy** proposing the change of state and charter amendments | shareholders undecided | vote no | shareholder suffrage is the instrument, and this filing is *that* instrument, attached as Exhibit 2.1 | High |
| 1996-11-04 | **File Form 8-B12B** for the successor's §12(b) registration | NYSE-listed predecessor | float a new entity by S-1 | — | High. **Measured:** `S-1`/`S-1/A`/`SB-2`/`10-A` = **0** in 2,968 rows; `8-B12B` = **1** |
| Nov 1996 | **Rename Melville → CVS Corporation** | the brand was a subsidiary trade name | keep the parent name | *"reflecting its concentration on the chain drugstore business and the completion of its restructuring program"* (`S97-S4` L767-770) | High |
| 1997-03-28 | **Register the Revco merger on Form S-4** | post-rename single-line chain, ~1,400 stores, #5 | stay regional | *"Achieving a critical mass… is essential to competing effectively"* (`S97-S4` L784-787) | High |
| 1983-11-14 | **(Estate) build a 150,000-sq.-ft. own DC** rather than keep leasing two Woonsocket buildings | leased distribution | keep leasing | *"Anticipating the opening of at least 50 new stores each year"* (`DSN-8384`) | Medium (TLS) |
| 1990-09-17 | **Buy Peoples Drug (490 stores) for $325 m cash and keep its name** | 820-store chain | organic growth only | not stated by the registrant in-window; the press quotes the seller's motive (debt reduction) | Medium |
| 1994 | **Buy Standard Drug Stores**, then (by 1994-95) **rename the former Peoples stores to CVS** | multi-name estate | keep multiple names | not stated. *The registrant gives the years and no reasons* (`S97-S4` L1576-1577; `DSN-9495`) | High (dates); UNKNOWN (motive) |

**N.1 The one decision the corpus forbids writing.** There is **no recorded decision to found anything, to open a
first store, to choose a name in 1963, or to move from footwear to pharmacy.** `decisions.csv` therefore carries
**zero rows before 1980**, and that is a finding about the archive, not a gap in this table (§S.6).

---

## O. COUNTERFACTUAL OPPORTUNITIES (what was open *then*, stated without the present)

**O.1 The flotation route that was not taken.** The registrant reached the market as a **successor issuer** under
§12(b) rather than as a new registrant under §1 of the Securities Act — measurable, not interpretive: `8-B12B` = 1,
`S-1`/`S-1/A`/`SB-2`/`10-A` = **0** of 2,968. In 1996 the parent could have (i) spun the drug leg as a new
registrant with its own registration statement, (ii) floated it, or (iii) taken the succession path it took. Only
(iii) leaves bytes here. **Consequence for this dossier, and it is severe:** the disclosure genre that habitually
recites a founder's origin — the IPO prospectus — **never occurred for this company**. The 1963 sentence exists at
all because a *merger* registration needed two paragraphs of business description (§U.01's root).

**O.2 The name the registrant never printed.** The trade press called the chain **Consumer Value Stores** in
six issue-dated rows from **1980-01-21 to 1994-04-25**, twice with the gloss *"(CVS)"*, and twice with
*"Parent: Melville Corp."* The registrant's own filings, across **36 stored documents spanning 1994–2001**, print
`Consumer Value` **zero times**. The choice of which name entered the corporate record — and the loss of the
origin-era naming from all later legal identity — is a **real fork visible in the bytes**, and it is the reason this
dossier can carry the *name* only from a third party (§U.02, §U.10).

**O.3 The estate's own counterfactual, 1990–1995.** Keeping the Peoples name was an option the parent took and then
reversed (400+ renamed to CVS). The bytes show both states; **they do not show what either did to sales**, because no
chain-level revenue series is filed in-window (§S.3).

**O.4 What is NOT a counterfactual here.** No statement about missing a format, a region, a technology or an
acquisition target is supportable: the corpus holds no rejected option, no internal memo, and no contemporaneous
skeptic's case about CVS (contrast the Amazon exemplar, which has one). **Mechanism UNKNOWN**, and the firewall (§2)
forbids filling it.

---

## P. QUANTITATIVE METRICS TABLE

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| CVS-P01 | 1976-06-30 | Registrant name change MELVILLE SHOE CORP → MELVILLE CORP | 1976-06-30 | date | EDGAR header on all 36 stored files | 1994-02-10→2001-03-30 | High |
| CVS-P02 | 1989-12-31 | CVS stores | 789 | count | `DSN-8990` L32991 (1990-04-09) | 1990-04-09 | Medium |
| CVS-P03 | 1989-12-31 | CVS stores with pharmacies | 582 | count | `DSN-8990` L32991 | 1990-04-09 | Medium |
| CVS-P04 | 1989 | CVS chain sales | 1.02 | $ bn | `DSN-8990` L61811 (1990-09-24) | 1990-09-24 | Medium — **U.04** |
| CVS-P05 | 1989 | "CVS at a glance" Sales | 1.95 | $ bn | `DSN-8990` L33016 | 1990-04-09 | Medium — **U.04** |
| CVS-P06 | 1990-09-17 | Peoples Drug Stores acquired: stores / price | 490 / 325 | count / $ m cash | `DSN-8990` L61806-61809 | 1990-09-24 | Medium |
| CVS-P07 | 1993-12-31 | Drug/HBC stores, 15 states + DC | 1,284 | count | `K93` L249-251 | 1994-03-31 | High |
| CVS-P08 | 1993-12-31 | Drug/HBC stores with pharmacies | 1,081 | count | `K93` L252 | 1994-03-31 | High |
| CVS-P09 | 1993 | Drug/HBC share of consolidated net sales | ≈38 | % | `K93` L262-263 | 1994-03-31 | High |
| CVS-P10 | 1994 | Melville consolidated sales | 11.3 | $ bn | `K8-95` L236 | 1995-10-26 | High |
| CVS-P11 | 1994 | Marshalls sales (divested leg) | 2.8 | $ bn | `K8-95` L236 | 1995-10-26 | High |
| CVS-P12 | 1995-10-14 | Marshalls purchase price / cash / preferred | 550 / 375 / 175 | $ m | `K8-95` L198-200; `D96-TJX` L402-405 | 1995-10-26 / 1996-04-08 | High |
| CVS-P13 | 1995-12-31 | Melville after-tax restructuring charge, Q4-1995 (excl. $195 m Marshalls charge; incl. $230 m write-offs/severance) | 585 / 195 / 230 | $ m | `K8-95` L408-414 | 1995-10-26 | High |
| CVS-P14 | 1995-12-31 | Melville associates (full + part-time, consolidated) | ≈97,000 | count | `K95` L178 | 1996-03-29 | High |
| CVS-P15 | 1996-08-22 | Registrant organised, Delaware | 1996-08-22 | date | `S96-8B12B` §1(a) | 1996-11-04 | High |
| CVS-P16 | 1996-11-04 | Form 8-B12B successor registration | 8-B12B | form | `S96-8B12B`; index row `1996-11-04, 8-B12B, 0000950103-96-001174, primaryDocument EMPTY` | 1996-11-04 | High |
| CVS-P17 | 1996-12-31 | CVS stores, states + DC | 1,408; 14 + DC | count | `K96-405` L160 | 1997-03-31 | High |
| CVS-P18 | 1996 | CVS revenue / pharmacy / front store | >5.5 / 2.4 / 3.1 | $ bn | `K96-405` L158-167 | 1997-03-31 | High |
| CVS-P19 | 1996 | Pharmacy share of sales (+18.4%) / front-store share (+9.3%) | 43.9 / 56.1 | % | `K96-405` L164-167 | 1997-03-31 | High |
| CVS-P20 | 1996 | Scripts per pharmacy per week; sales per square foot | ≈1,200; 573 | count; $/sq ft | `K96-405` L167-170 | 1997-03-31 | High (filed); comparative is self-reported |
| CVS-P21 | 1996-12-31 | Pharmacare: covered lives | >1,000,000 | lives | `K96-405` L473-475 | 1997-03-31 | High (filed, self-measured) |
| CVS-P22 | 1994 | Pharmacare founded | 1994 | date | `K96-405` L469 | 1997-03-31 | High (that it is recited); Medium (the date, single source) |
| CVS-P23 | 1997-03-28 | Revco counterparty size: stores / revenue / states | ≈2,600 / 5.3 / 17 | count; $ bn | `S97-S4` L777-780 | 1997-03-28 | High (as filed description of another registrant) |
| CVS-P24 | 1963 | Any quantity of the origin enterprise | **UNKNOWN** | — | 0 carriers in 36 SEC files + 16 unique press/print docs | — | High (of the absence) |
| CVS-P25 | 1991-05-06 | Chain sales / store count / store size per trade box | 3.29 / 1,351 / 8,800 | $ bn; count; sq ft | `DSN-9091` L38081-38096 | 1991-05-06 | Medium; **the box's fiscal year is not printed in the layer** |
| CVS-P26 | 1993-04-26 / 1994-04-25 | Chain sales / store count per trade box | 3.63 / 1,221 and 3.95 / 1,284 | $ bn; count | `DSN-9293` L34095-34097; `DSN-9394` L39057-39059 | 1993-04-26; 1994-04-25 | Medium — **U.05** (1,284 equals the FY1993 four-name segment count) |

**P.1 Derived values, arithmetic shown (§8).** Pharmacy attach 1989 = 582 ÷ 789 = **73.8%**; FY1993 = 1,081 ÷ 1,284 =
**84.2%**; estate change 1989→FY1993 = 789 → 1,284 = **+62.7%** (but **scope changes** — see §U.05, so this is
reported and **not** used as growth); Peoples stores ÷ 1989 CVS stores = 490 ÷ 789 = **+62.1%** of estate added by
one purchase. **Every one of these mixes a third-party chain figure with a filed segment figure and is therefore
labelled ESTIMATE/DERIVED with a scope warning in `quantitative.csv`.**

STATUS: WRITTEN 2026-10-06

## Q. CHRONOLOGICAL MICRO-TIMELINE

Every row is a date **a held carrier prints**, with the legal person it attaches to. Rows with no carrier are written
as absence-rows, because that is what they are. (Full-width rows for `timeline.csv` are in `## registers`.)

| Date | Event | Actor / legal person | Location | Carrier | Class |
|---|---|---|---|---|---|
| **1963** | *"Founded in 1963, CVS is…"* — a **year only**: no town, no name, no format, no person | the **chain/business** described by a New York-born registrant | UNKNOWN | `S97-S4` L762 (+ identical in `S97-S4A`, `P97`) | **COMPANY CLAIM, RETROSPECTIVE** (34 yrs), Medium, **one lineage** |
| 1963 | **Absence-row:** 0 occurrences of `Consumer Value`, `Jacksonville`, `Newport`, `first store`, `Kandel`, `Lowell` in all 36 SEC files | — | — | term census | UNKNOWN, routes §S.1–§S.5 |
| **1976-06-30** | EDGAR-recorded name change `MELVILLE SHOE CORP` → `MELVILLE CORP` | the registrant itself | New York | header of all 36 stored files | FACT (identity record) |
| 1979-10-29 → 11-12 | **Absence-row:** oldest held press layer (16 dated mastheads) contains **0 `CVS`-bearing lines** | — | — | `DSN-7980` lines 365–5906 | FACT (measured null) |
| **1980-01-21** | First held naming: *"Rhode Island-based Adams Drug and **Consumer Value Stores**"* in a competitive roundup | the chain, name phrase | R.I. | `DSN-7980` L7662 | CONTEMPORANEOUS OBSERVATION, Medium |
| 1980 (dir.) | Directory line `. CVS Stores, Woonsocket, R.!. Baton Rouge, La.` — **pointer to a listing**, OCR `R.!` decoy | the chain estate | Woonsocket | `DSN-7980` L14496 | Low/observation; **not** used as a naming |
| **1983-11-14** | Warehouse decision printed with the gloss *Consumer Value Stores **(CVS)***; ≥50 openings/yr planned; WOONSOCKET dateline | the chain | Woonsocket, R.I. | `DSN-8384` L1779-1800 | CONTEMPORANEOUS OBSERVATION, Medium |
| **1987-11-23** | *"The **Melville Corp.**, owner of **CVS Stores** and Freddy's Deep Discount, reported sales and net income boosts…"* | parent + chain | Harrison, N.Y. | `DSN-88` L2827 | CONTEMPORANEOUS OBSERVATION, Medium |
| 1988-04-25 | Same construction for the year ended Dec 31 | parent + chain | Harrison, N.Y. | `DSN-88` L42601 | CONTEMPORANEOUS OBSERVATION, Medium |
| 1989-12-31 | Estate 789 stores / 582 pharmacies; box sales $1.95 bn; **news-story sales $1.02 bn for 1989** | chain | 11 NE states + Ohio, Michigan, California | `DSN-8990` L32990-33020, L61811 | observation, Medium; **U.04** |
| **1990-04-09** | *"CVS at a glance — **Name: Consumer Value Stores (CVS)** … **Parent: Melville Corp.**"* | chain as a named company | Woonsocket | `DSN-8990` L33004-33020 | observation, Medium |
| **1990-09-17** | Peoples Drug purchase **completed**: 490 stores, $325 m cash, from Imasco Ltd. (Montreal); CVS then 820 stores; name kept | Melville (buyer) | Rye, N.Y. dateline | `DSN-8990` L61806-61817 | observation, Medium; year corroborated by `S97-S4` L1576 |
| 1995-09-30 | Marshalls measured at the date the sale was agreed: **495 stores in 40 states and Puerto Rico**; TJX's own T.J. Maxx 571 stores | Melville's divested leg | Roseville, Minn. | `K8-95` L234-238 (filed 1995-10-26) | FACT, High |
| 1991-05-06 | Second at-a-glance box (1,351 stores, $3.29 bn, 8,800 sq ft; Peoples highlight) | chain | Woonsocket | `DSN-9091` L38081-38100 | observation, Medium |
| 1992-11→1993-10 | Layer dated; box of **1993-04-26** prints `Company name: Consumer Value Stores`, $3.63 bn, 1,221 stores | chain | Woonsocket | `DSN-9293` L34084-34097 | observation, Medium |
| **1993-12-31** | **First filed estate numbers on disk**: 1,284 drug/HBC stores, 15 states + DC, 1,081 with pharmacies, ≈38% of consolidated net sales | Melville's segment (4 trade names) | — | `K93` L249-263 (filed 1994-03-31) | FACT, High |
| **1994** | *Pharmacare, **founded in 1994*** — the PBM leg's own date, in the registrant's own recital | Pharmacare / Pharmacare Management Services, Inc. (DE) | — | `K96-405` L469 | FACT (recital), Medium (date, single source) |
| 1994 | Strategic review **initiated** | Melville board | — | `S97-S4` L770 | RESTATED |
| 1994 | Standard Drug Stores acquired | the chain | — | `S97-S4` L1577 | FACT (year only) |
| 1994-02-10 | **Earliest indexed EDGAR filing for CIK 64803** — SC 13G/A (Invesco), subject Melville Corp | Melville | — | index row + stored file | FACT; **perimeter, not a beginning** |
| 1995 | Restructuring program **approved by the Board** | Melville board | — | `S97-S4` L769 | FACT (recital) |
| **1995-10-14 / 10-16 / 11-17** | Marshalls **SPA signed / announced / consummated**: ≈$550 m = $375 m cash + $175 m preferred; 495 stores; $2.8 bn of 1994 sales; Q4-95 charges $585 m + $195 m | Melville ↔ TJX Companies, Inc. /DE/ (CIK 109198, formerly Zayre) | Roseville, Minn. / Rye, N.Y. | `K8-95` L110-116, L196-200, L408-414; `D96-TJX` L396-406 | FACT, High |
| 1996-03-15 | TJX preferred moved Melville → CVS Center → CVS H.C. → Nashua CVS | the CVS holding chain, pre-succession | — | `D96-TJX` L474-477 | FACT |
| 1996-04-08 | SC 13D filed **by Melville** naming the CVS-bearing holders — but its **subject is TJX**: this is the Marshalls consideration, not a CVS control filing | Melville as filer; TJX as subject | — | `D96-TJX` L22, L89, L100-102 | FACT; **reading it as CVS's own filing is the error** (§M) |
| **1996-08-22** | **CVS Corporation organised under Delaware law** — the registrant's own corporate form, 33 years after the claimed origin | CVS Corporation (DE) | — | `S96-8B12B` §1(a) L108-109 | FACT, High |
| **1996-08-30** | Agreement and Plan of Merger among **Melville, CVS, and Merger Subsidiary** (`CVS New York, Inc.`) | three persons | — | `S96-8B12B` L148-151 | FACT, High |
| 1996-10-07 | Proxy statement dated, proposing reincorporation N.Y. → Del. and charter amendments | Melville shareholders | — | `S96-8B12B` L120-127 | FACT, High |
| **1996-11-04** | **Form 8-B12B filed** — cover: *"CVS CORPORATION (Successor to Melville Corporation)"*, state *Delaware*, EIN *Applied For*, NYSE, $.01 par; header still MELVILLE CORP / NY / EIN 04-1611460 | predecessor filing on the successor's behalf | One CVS Drive, Woonsocket | `S96-8B12B` L66-96, L73-74 | FACT, High |
| **Nov 1996** | *CVS changed its name from **Melville Corporation** to **CVS Corporation*** | the same CIK 64803 | — | `S97-S4` L767 | FACT (recital); the **8-B12B is application-stage**, so the bytes do **not** record the Effective Time (§A, §S.5) |
| 1996-12-31 | **End-of-stage snapshot** — 1,408 stores, 14 states + DC, >$5.5 bn revenue, $2.4 bn pharmacy, >1 m Pharmacare lives, EIN now 05-0494040 in 1997 paper | CVS Corporation (DE) + estate | Woonsocket / Rye legacy | `K96-405` L158-170, L473-475 | FACT, High |
| 1997-03-28 | **S-4 for the Revco D.S., Inc. merger** filed — carries the only `Founded in 1963` sentence on disk | CVS Corp + Revco (Twinsburg, Ohio) | — | `S97-S4` L762, L772-780 | FACT (the filing); claim (the year) |
| 2001-03-15 | **Decoy row:** `P01` L436 *"From 1963 to March 1998, he was President of…"* — a director's employment history, the only post-S-4 `1963` in the SEC shelf | a named director | — | `P01` L436 | FACT; **not** a founding — **U.06** |

---

## R. END-OF-STAGE STRUCTURED SNAPSHOT (1996-12-31)

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Registrant, legal person | CVS Corporation, **a Delaware corporation organised 1996-08-22** | `S96-8B12B` §1(a) | High |
| Registrant, predecessor | Melville Corporation, a New York corporation, to become a wholly owned subsidiary and be renamed **CVS New York, Inc.** | `S96-8B12B` L115-142 | High |
| Registration posture | §12(b)/(g) **successor** registration on Form 8-B12B; NYSE; $.01 par; **no S-1 ever filed** | `S96-8B12B`; index census | High |
| Taxpayer identity | EIN `04-1611460` (Melville) → `05-0494040` (CVS): **same CIK, different taxpayer** | §T.3 sidecar/header census | High |
| Estate | **1,408 stores**, 14 states + DC, most with pharmacies; 4 trade names in FY1993 collapsed toward one | `K96-405`; `K93` | High |
| Revenue | **over $5.5 bn** 1996; pharmacy **$2.4 bn (+18.4%, 43.9%)**, front **$3.1 bn (+9.3%, 56.1%)**; **$573/sq ft** | `K96-405` L158-170 | High |
| Density | ≈**1,200 scripts per pharmacy per week** (self-compared to "the average community pharmacy", no denominator filed) | `K96-405` L167-169 | High (filed); the comparative is unverified |
| Segment weight in the parent, FY1993 | **≈38%** of consolidated net sales | `K93` L262-263 | High |
| Legs already exited or in exit | Marshalls **sold** 1995-11-17; Wilsons, *This End Up*, Kay-Bee **marked for sale**; footwear = **discontinued operations** | `K8-95`; `K95` | High |
| Benefit leg | **Pharmacare** (founded 1994): >1 m managed lives at end-1996; DE legal person | `K96-405` L469-475 | High / Medium on the date |
| Insurance leg | **None in the record** — no underwriter named; only self-insurance for liabilities (post-window) | §C.3 | High (of the absence) |
| Caremark leg | **`Caremark` = 0 occurrences in all 36 SEC files**; only EDGAR `former_names` metadata | §T.3 | High (of the absence in text) |
| People | No founder; no named CEO of the chain in-window except via the trade box (`Harvey Rosenthal, president and ceo, CVS`; `Thomas Ryan`), and officers in the parent's filings | `DSN-8990` L33013-33014; `DSN-9091` L38092-38093 | Medium |
| What Stage 2 begins with | A pending **Revco** registration (S-4, 1997-03-28) and a succession whose Effective Time is **not recorded in these bytes** | `S97-S4`; §S.5 | High |

---

## S. DATA GAPS

Matching `data_gaps.csv` rows in `## registers`; `importance` is the register's, and every High row carries a
follow-up task (§13).

| # | Gap | Why missing | Importance | Best available evidence | Follow-up task |
|---|---|---|---|---|---|
| S.1 | The **content** of the 1963 act: town, original name, format, founders, opening | The only carrier is a 34-year-late one-line recital in a merger registration; nothing earlier exists for this CIK in EDGAR (floor 1994-02-10) | **High** | `Founded in 1963` (`S97-S4` L762), one lineage, Medium | **`R-1` was RUN** (28 docs, 1997-2001 window) and **did not add a name, town or person** — so the next route is `R-3`/`R-4`/`R-5`, not more SEC grabs |
| S.2 | Which **legal person**, if any, was "CVS" in 1963 | 15 CVS-bearing persons named in-window (§B.3), none dated 1963 | **High** | `S96-8B12B` L108-109; `K96-405` L8349-8376 | `R-4` (CA `andtext:"Consumer Value Stores"`, no state facet, 1960-1980) + registry/ incorporation records of RI/MA for 1963 |
| S.3 | Chain-level revenue/profit **series** 1963–1992; same-store sales; customer counts | FY1990–FY1992 10-Ks are **not on disk**; paper-era filings live outside EDGAR; family (d) = **0 bytes** | **High** | 1989 press figures (two conflicting, §U.04); FY1993 filed segment share | `R-3` facet-free corporate print; EDGAR full-text search does not reach 1990 annual reports — a **manual accession enumeration** of CIK 64803 1990-1993 is the route |
| S.4 | Any 1963–1979 third-party text | Earliest held press is **1979-10-29**, and it carries 0 `CVS` lines; **57 candidates untried at the `--limit` cut** | **High** | 1980-01-21 naming row | `R-5`: run `harvest_mine.py` at a higher limit over the DSN/JAPHA/Pharmacy Times layers **1963-1979**, with entity adjacency required |
| S.5 | The **Effective Time** of the 1996 reincorporation/merger; the actual name-change filing date | The held 8-B12B is an **application-stage** instrument ("Delaware **Applied For**"; EIN "Applied For"); the 8-K that would record the effective date is **not on disk for Nov–Dec 1996** | **High** | proxy dated 1996-10-07; `S97-S4` L767 "In November 1996" | enumerate CIK 64803 **8-K/8-K(A) rows Oct–Dec 1996** from `submissions_CIK0000064803.csv` and `grab` them (add-only) |
| S.6 | Any internal deliberation, rejected option, dissent, contemporaneous skeptic's case, or **failure** of the origin enterprise | Winners' archive (§2 record-selection null); 1963-1979 has no corporate paper at all | Medium | filed *costs* of the 1994-96 restructuring (`K8-95` L408-414) | family (e) auction/manuscript **UNTRIED** and has **no query block** in `tools/queries.json` for `cvs` — that is the missing ask |
| S.7 | Category size and share denominators in-window | Google Books rows on disk are **1997-2020 almanacs/directories** and out of window; `TIER1_CANDIDATE` labels are index columns, not text | Medium | none | re-harvest with **in-window** US chain-drug yearbooks/directories 1963-1995, **facet-free** |
| S.8 | Family **(b) web archives** | **UNTRIED, 0 calls**; no `sources/web_archive/` shelf exists for this company; `tools/cdx_intake.py` is now on the tools shelf but was never run for CIK 64803 | Medium (S1d only: 1996-era CVS/Melville pages could carry estate copy) | none | CDX query for `cvs.com`/`melville.com` 1996-2001; **cannot** reach 1963-1979 by construction |
| S.9 | Vendor/supplier concentration, distribution contracts, lease terms of the chain | Never disclosed by this registrant in-window (no flotation document to compel it, §O.1) | Medium | the real-estate SPV stack (`K96-405` L8356-8373) | 10-K exhibit indices FY1993-FY1996 (only FY1993-95 are on disk) |
| S.10 | **Manifest/reality drift** in the intake record | `_RUN.json` now describes the 1997-2006 pass only (`stored 28`, `identity_ok false`, 6 duplicate slots); the in-window pass 1 survives as `_RUN.prev-20261006T121331Z.json`; `_FLEET_INTAKE.tsv` still says `pass2_status` empty / `pass2_docs 0` | Medium | 36 stored `.txt` each with its own sidecar (`http_status 200`, `sha1`) | fleet owner to re-key `_FLEET_INTAKE.tsv` **by window**, not to re-run intake |

STATUS: WRITTEN 2026-10-06

## T. SOURCE / PROVENANCE

**T.1 The SEC shelf, re-enumerated at close (§14 r11 — the corpus grew under this author).**
**36 `.txt`** + 36 sidecars under `sources/sec/`, decomposing exactly: **7** in-window pass-1 documents
(1,091,837 B, `_MANIFEST.prev-20261006T121331Z.csv`) + **28** forward-window documents (6,980,278 B, current
`_MANIFEST.csv`, `window 1997-01-01..2006-12-31`, `stored 28`, `attempted 128`, `skipped 97`, `unanswered 3`) +
**1** probe `grab` that is in neither manifest — the **8-B12B**, `0000950103-96-001174` (46,691 B, 6,142 words,
`http_status 200`). 7 + 28 + 1 = 36 ✓. Every cited row below was read in the held text at the stated line.

| Label | Accession · form · filed | Legal person / subject | Lineage class (§3) | Tier |
|---|---|---|---|---|
| `S96-8B12B` | 0000950103-96-001174 · **8-B12B** · 1996-11-04 | CVS Corporation (DE), filed by **Melville** as predecessor | **L-1** the succession registration itself (+ its Ex. 2.1 proxy and Appendix A merger agreement, same accession) | 1 |
| `K93` `K94` `K95` | 0000950110-94-000133 · 10-K · 1994-03-31 / 0000891092-95-000026 · 10-K · 1995-03-29 / 0000891092-96-000050 · 10-K · 1996-03-29 | **Melville Corporation (NY)** | **L-2** the parent's own annual series — three filings, one filer identity; **not** independent of each other for identity claims | 1 |
| `G94` `P94` `K8-95` `D96-TJX` | SC 13G/A 1994-02-10 / DEF 14A 1994-03-14 / 8-K 1995-10-26 / SC 13D 1996-04-08 | Melville as **filer**; `D96-TJX`'s **subject is TJX Companies, Inc. /DE/** (CIK 109198, formerly Zayre) | **L-2** for Melville; the 13D is a **third party's** filing about a different issuer — it names CVS-bearing persons only as the route of the Marshalls consideration | 1 |
| `S97-S4` `S97-S4A` `P97` | S-4 1997-03-28 / S-4/A 1997-04-17 / DEF 14A 1997-04-23 | CVS Corp (DE) + Revco D.S., Inc. | **L-3 = ONE lineage.** `Founded in 1963` appears **once per file, three files, identical sentence** — **one witness**, not three | 1 |
| `K96-405` `K98` `K99` `K00` `K01` | 10-K405 1997-03-31 / 10-K405 1998-03-31 / 10-K 1999-03-31 / 10-K 2000-03-31 / 10-K 2001-03-19 (+ its Ex-13/Ex-21/Ex-23) | CVS Corporation (DE) | **L-4** annual series; each is its own instrument, all trace to one corporate record; **FY1996 is the only one inside the window** | 1 |
| `B97` `B1-98` `S3-97` `K8-97` `G97` `D97` `K99A` `S99A*` `K8-01` `P01` `G00` | 1997-02→2001-03 | CVS Corp; `D97` subject **Revco**; `G97` subject **Linens 'n Things** | **L-5** prospectuses/offering papers of the same lineages as above | 1 |
| `DSN-7980` `DSN-8384` `DSN-85` `DSN-88` `DSN-8990` `DSN-9091` `DSN-9293` `DSN-9394` `DSN-9495` `DSN-95` | 10 Internet Archive serial text layers, *Drug Store News* (Lebhar-Friedman) | the **chain and its parent, named by a third party** | **L-6 = independent lineage.** Not the company's paper; this is what makes the *name* corroboration real (§3) — and it corroborates the **name only**, never the 1963 date | 3 |
| `JAPHA-81/83/86/90/91`, `PT-89` | 6 annual **index volumes** | — | **L-7 = textless.** An index has no article text: their `NULL` verdicts are **structural**, not findings about the past | 3 |

**T.2 Family (d): the `corporate_print` shelf contains no corporate print.** Measured: 4 `.txt`,
**all Internet Archive serial items** — 3 *Drug Store News* layers (`DSN-8384`, `DSN-85`, `DSN-8990`) and 1 JAPHA
annual index — each sidecar reading `route = download/<id>/<id>_djvu.txt (OCR text layer)` and each recorded in
`sources/harvest_mine/_index.json` with `family: "internet_archive"`. md5 de-duplication shows **2 of the 4 are
byte-identical to copies on the periodicals shelf** (`micro_IA40706934_0338`, the JAPHA 1983 index): 18 non-SEC
`.txt` → **16 unique documents**. **Family (d) has zero bytes**, and the two `NULL` corporate-print rows in
`00_universe/harvest/candidates.csv` are **year-faceted** (`year_range [1960,1998]`), so they are a statement about our
parameter, not about the archive. **Counting this shelf as family (d) would have manufactured a third answering family
out of a second family's bytes — the RD-130 error, inverted.** This volume counts **2 families**, as the probe did.
**Transport cap:** all 18 sidecars say `transport = "UNVERIFIED TLS — re-check before citing at High confidence"`;
every periodical claim here is therefore **Medium at best**.

**T.3 Identity cross-check, computed from the 36 headers** — the fact that makes §U.07 necessary.

| Era in the bytes | `COMPANY CONFORMED NAME` | `FORMER CONFORMED NAME` | EIN in text |
|---|---|---|---|
| 1994-02-10 → 1996-11-04 (8 docs) | **MELVILLE CORP** | MELVILLE SHOE CORP, name change **1976-06-30** | `04-1611460` |
| 1996-11-04 **8-B12B** | header still **MELVILLE CORP**, cover name **CVS CORPORATION (Successor to Melville Corporation)**, EIN *"Applied For"* | as above | `04-1611460` ×1 |
| 1997-02-07 → 2001-03-30 (24 docs) | **CVS CORP** | **MELVILLE CORP** *and* MELVILLE SHOE CORP, both printed | `05-0494040` |
| `K94` FY1994 10-K | **no SGML header parsed** — the probe's §8.8 defect, reproduced and confirmed here: identity taken from the body (*"Melville Corporation, a New York corporation"*; *"CVS, Inc., a Rhode Island corporation"*) and the form/date from `_MANIFEST.prev` | — | `04-1611460` |

**T.4 Universe row, read before use.** `00_universe/fortune_top_50_2026.csv` columns:
`rank, company, revenue_usd_millions, revenue_fiscal_year, profit_usd_millions, hq_city, hq_state, fortune_industry,
universe_source_url, verified_by_second_source, confidence, notes` — **no founding-date column**. The CVS row supplies
rank 6, revenue $402,067 m for the fiscal year ended 2025-12-31, profit $1,768 m, HQ Woonsocket, Rhode Island,
industry "Health Care: Pharmacy and Other Services". All four are **present-state** and none is evidence about 1963;
two Chronicling America tasks nonetheless facet on Rhode Island, which is recorded as a **query-design defect**, not a
null (§S.1, and the probe's §6.2).

**T.5 Index-layer defects found and not papered over.** (i) `sources/_index/submissions_CIK0000064803.csv`,
**2,968 rows**, `filingDate` 1994-02-10 → 2026-08-17, **0 rows before 1994-01-01**; the 1996-2000 rows carry
**no `primaryDocument`** — verified directly for the 8-B12B row (`1996-11-04, 8-B12B, 0000950103-96-001174, '', ''`),
so a document name must be **enumerated, never assumed**. (ii) `sources/sec/_RUN.json` now reports
`identity_ok: false` with 6 `duplicate_slots`, and describes only the 1997-2006 window; the in-window record survives
only as `_RUN.prev-20261006T121331Z.json` / `_MANIFEST.prev-…csv`. (iii) `00_universe/_FLEET_INTAKE.tsv` still says
`pass2_status` **empty** / `pass2_docs 0` — contradicted by (i)-(ii). **All three are reported to the merge; none was
"fixed" by this author, because none of those files is mine** (§14 r4).

**T.6 The decoys this volume had to clear before counting anything** (§Header discipline 1; all re-measured here).
`1963` in `DSN-8384` = **10 hits, 0 this company** (stock tables `Pay Less NW PAY 1963 1750…`, `Spectro Indus SPO 2275
1963…`, a `©1963` ad copyright). `1963` in `DSN-9091` L40103-40105 = **Civic Drugs, Dearborn, Mich., 1963** — a rival's
founding. `consumer value` in `DSN-88` = **5 hits, 0 of them the company** ("extra consumer value", a lighter;
"special consumer values"; "new consumer value combo", a shampoo). `JACKSONVILLE` = 1-6 hits per layer in **seven**
layers, with **no CVS context** and no way to tell FL from IL from a grep. `Woolworth` = 16 (1989/90 layer) and 13
(1985) — real, but belonging to **Peoples' prior owner**, a third lineage. `Riverside` in the SEC shelf = **8 hits,
all addresses** (`Two CVS Riverside Plaza`, `2 North Riverside Plaza`, plus the 1997 S-3/SC 13D/8-K address blocks);
`Newport` = **0 in all 36**. Bare-vs-adjacent `CVS`: **172/4** in `DSN-9394`, **185/6** in `DSN-9495`, **18/0** in
`DSN-85`, **0/0** in every index volume. **A `TIER1_CANDIDATE_TEXT` stamp in `harvest_mine/_index.json` was never
treated as a source** — the four rows promoted there (`cvs sales`, `cvs stores`) are *identity-word* promotions over a
retail estate, and `named_terms` is `[]` on **all 12 mined items**, i.e. the mine itself never promoted a name phrase.

---

## U. CONFLICTING EVIDENCE

<!-- ANCHORS: U.01-U.10 -->

### U.01 — Which legal person was "founded in 1963"?

**CLAIM A.** *Founded in 1963, CVS is the country's fifth largest drugstore chain…* — `S97-S4` L762 (1997-03-28,
registrant's own paper, repeated verbatim in `S97-S4A` and `P97`).
**CLAIM B.** *CVS Corporation ("CVS" or the "Registrant") was organized as a corporation on August 22, 1996 under the
laws of the State of Delaware*; and *Melville Corporation, a New York corporation… will be the predecessor of the
Registrant at the time of the succession* — `S96-8B12B` L108-109, L115-116.
**WHY THEY DIFFER.** A names a **business**; B names a **corporate person**. The listed person behind both is CIK
64803, whose own form (Melville, New York, renamed from Melville Shoe Corp on **1976-06-30**) **predates** 1963, while
its current Delaware form is dated **1996**. There is therefore no single "company" for 1963 to attach to.
**EVIDENCE WEIGHT.** Both Tier-1. B is contemporaneous and self-formative; A is retrospective by 34 years and, on this
corpus, **one lineage** (3 files, 1 sentence, no second witness anywhere: the FY1996 10-K405 prints `1963` **zero**
times).
**BEST-SUPPORTED INTERPRETATION.** 1963 is the recited founding of the **drugstore business** the registrant later
concentrated into — **not** the organisation of any legal person available on disk. The register entry for the origin
carries class `COMPANY CLAIM (retrospective)` with `conflict_ref = U.01`.
**RESIDUAL UNCERTAINTY.** Whether a 1963 corporation existed and was later absorbed: **UNKNOWN** (§S.2, `R-4`).
**CONFIDENCE:** Medium (the year); **High** (that the corpus attaches it to no person).

### U.02 — Is *Consumer Value Stores* the name of the 1963 entity?

**CLAIM A.** The folk origin: the 1963 company was *Consumer Value Stores*, a **shoe store**, opened at
**Jacksonville**, with a **Riverside–Newport** naming lineage — asserted in the dispatch brief and in general
literature, carried into the fleet's window parameter.
**CLAIM B.** Measured: `Consumer Value` = **0** in all 36 SEC files; `Jacksonville` = **0**; `Newport` = **0**;
`Riverside` = 8 and every one is an **address**; the name phrase exists **only** in the trade press, in six
issue-dated rows **1980-01-21 → 1994-04-25** that print it as the chain's **current** name, twice glossed
*"(CVS)"*, four times with *"Parent: Melville Corp."* — and **never with a date of foundation or a town of origin**.
**WHY THEY DIFFER.** A is inherited narrative; B is this corpus. The press rows are *contemporaneous naming*, not
*retrospective genealogy* — the genre that would carry an origin story is absent from every held file.
**EVIDENCE WEIGHT.** B, decisively: the naming lineage is **third-party, independent of the SEC record (§3)**, and it
is the **only** naming lineage on disk.
**BEST-SUPPORTED INTERPRETATION.** *Consumer Value Stores* is **established as the chain's name 1980–1994 with
Melville as parent**; its use in **1963** is **UNKNOWN**, as are the shoe-store character, Jacksonville, and the
Riverside–Newport construction. **No element of the folk story is written as fact in this volume.**
**RESIDUAL UNCERTAINTY.** The name could still be the 1963 name; only `R-4` (newspaper route under the correct
string) or `R-3`/`R-5` can reach it.
**CONFIDENCE:** High (that the corpus does not support A); **UNKNOWN** (the underlying fact).

### U.03 — Was 1996 an IPO?

**CLAIM A.** "1996 IPO/reorganisation boundary" — the frame carried in the fleet's dispatch and probe §1.3.
**CLAIM B.** Census of `submissions_CIK0000064803.csv` (2,968 rows): `S-1` **0**, `S-1/A` **0**, `SB-2` **0**,
`10-A` **0**, `8-B12B` **1** (1996-11-04). The instrument's own caption is *"FOR REGISTRATION OF SECURITIES OF CERTAIN
SUCCESSOR ISSUERS … FILED PURSUANT TO SECTION 12(b) OR (g)"*. The one "initial public offering" named in the 1997 S-4
is *"CVS' former subsidiary, Linens 'n Things, Inc."* (L3184) — **someone else's flotation, listed in a banker's
transaction table**.
**WHY THEY DIFFER.** A reads "the year CVS-named registrant paper begins" as flotation; B is the instrument class.
**EVIDENCE WEIGHT.** B, and it is not close: the absence of every flotation form on the registrant's own index row set
is a primary-record measurement, and `1996-11-04` `primaryDocument` is empty, so even the index hides the paper.
**BEST-SUPPORTED INTERPRETATION.** 1996 = **reincorporation-by-succession plus a §12(b) successor registration**.
**RESIDUAL UNCERTAINTY.** Whether any CVS equity was separately offered in 1996: `data_gaps` importance **High**
(§S.5); pre-EDGAR-era paper can be silent and still exist.
**CONFIDENCE:** High (census); Medium (the wider negative claim).

### U.04 — 1989 chain sales: $1.02 bn **or** $1.95 bn?

**CLAIM A.** *CVS sales in 1989 totaled $1.02 billion* — `DSN-8990` L61811, issue **1990-09-24**.
**CLAIM B.** *CVS at a glance … Sales: $1.95 billion / Stores: 789* — same document, L33004-33018, issue
**1990-04-09**.
**WHY THEY DIFFER.** Same publication, same chain, five months apart, 1.9× apart in value: one is a news story's
figure inside a purchase report, the other a survey box whose **basis is not printed in the OCR layer** (store sales
vs chain sales vs segment sales cannot be told apart from the bytes).
**EVIDENCE WEIGHT.** Equal, and both are **third-party**: the filed comparator (Melville's FY1989 10-K) **is not on
disk**, and EDGAR reaches nothing before 1994-02-10.
**BEST-SUPPORTED INTERPRETATION.** **Report both, adopt neither.** `quantitative.csv` carries P04 and P05 as separate
Medium rows, each with `conflict_ref = U.04`, and the narrative uses the **filed FY1993 share (≈38%)** instead.
**RESIDUAL UNCERTAINTY.** Not resolvable from this corpus at all. Route: `R-3` (facet-free corporate print could put
the FY1989 annual report on disk).
**CONFIDENCE:** Low (each value); **High** (that they conflict).

### U.05 — "Consumer Value Stores" the chain, or the four-name segment?

**CLAIM A.** `DSN-9293` L34084-34097 (issue 1993-04-26): *Company name: Consumer Value Stores … Parent: Melville
Corp. … Sales: $3.63 billion. Store count: 1,221.* `DSN-9394` L39047-39059 (issue 1994-04-25): same construction,
*$3.95 billion, 1,284 stores*.
**CLAIM B.** `K93` L249-263 (filed 1994-03-31): *"the Companies operated **1,284** prescription drugs, health and
beauty aids stores… under the names **"CVS", "Peoples", "Standard Drug" and "Austin Drug"**, 1,081 of which have
pharmacies"* — **the identical number, but scoped to four trade names.**
**WHY THEY DIFFER.** The trade box applies a **single company name** to what the filing shows as a **multi-name
segment**. "Chain" and "segment" are the same estate wearing two descriptions; the press name is not a legal person.
**EVIDENCE WEIGHT.** B is filed, dated and internally consistent; A is third-party, undated as to fiscal basis.
**BEST-SUPPORTED INTERPRETATION.** Read DSN's *Consumer Value Stores* rows as **the parent's drug estate under its
lead name**, and **never** as the 1963 company's estate. This also settles why the 1991 box's 1,351 stores exceeds the
FY1993 filed 1,284 (scope, not shrinkage — **no carrier explains it**).
**RESIDUAL UNCERTAINTY.** Whether DSN's sales line is chain-only or segment-wide: UNKNOWN.
**CONFIDENCE:** Medium.

### U.06 — The 1963s and the CVSs that are not this company

**CLAIM A (a grep).** Searching the held press for `1963`, `founder`, `opened`, `CVS` returns "hits".
**CLAIM B (a read).** Those hits are: **Civic Drugs, Dearborn, Mich., 1963** — *a rival chain's founding* (`DSN-9091`
L40103-40105); **10 `1963` strings** in `DSN-8384` that are stock quotes and copyright years; **`P01` L436**
*"From 1963 to March 1998, he was President of…"* — a **director's employment history**, and the only post-S-4 `1963`
in the SEC shelf; **`JACKSONVILLE`** 1-6 hits in seven layers with no CVS context; and bare `CVS`, which is also a
**medical abbreviation** and appears 0 times in the six JAPHA/*Pharmacy Times* index volumes and 18 times in
`DSN-85` with **0** entity-adjacent matches.
**WHY THEY DIFFER.** A matches strings; B requires **entity adjacency plus a named person**.
**EVIDENCE WEIGHT.** B — always. These five are this dossier's **standing negative controls**: any later pass that
reports a 1963 founding for CVS from a search hit has almost certainly landed on one of them.
**BEST-SUPPORTED INTERPRETATION / RESIDUAL / CONFIDENCE.** No 1963 event of the origin enterprise is in the press
shelf; **UNKNOWN** whether any such text exists, because **57 candidates are untried** (§S.4). Confidence in the
controls: **High**.

### U.07 — Same CIK, different taxpayer: is the registrant continuous with Melville?

**CLAIM A.** EDGAR identity for CIK 64803 is **continuous**: `former_names` = `MELVILLE CORP`, `CVS CORP`,
`CVS/CAREMARK CORP`, `CVS CAREMARK CORP`; every post-1997 file prints `FORMER CONFORMED NAME: MELVILLE CORP` **and**
`MELVILLE SHOE CORP` in its own header.
**CLAIM B.** Corporate law says a **new person**: organised **1996-08-22** in Delaware; Melville survives as a wholly
owned subsidiary **renamed "CVS New York, Inc."**; EIN moves `04-1611460` → `05-0494040` (§T.3) — a **different
taxpayer wearing the same CIK**.
**WHY THEY DIFFER.** Registration continuity follows the **listed equity** through a §12(b) succession; chartering and
tax identity are **new in 1996**.
**EVIDENCE WEIGHT.** Both Tier-1, both true at their own layer; the conflict is definitional, not evidentiary.
**BEST-SUPPORTED INTERPRETATION.** For disclosure purposes the registrant **is** Melville continued; for corporate-law
purposes it **is** a 1996 Delaware corporation. **Neither reading lets 1963 be the registrant's organisation date**,
which is why §A is written the way it is.
**RESIDUAL.** Whether Melville's pre-1976 shoe business ever carried the CVS brand: no carrier.
**CONFIDENCE:** High (both limbs); Medium (that no other reading exists in later paper).

### U.08 — The `corporate_print` shelf: family (d) or family (c)?

**CLAIM A.** A directory named `corporate_print`, a fleet record asserting "corporate print 8", and a mine that
promoted items from it ⇒ family **(d) digitised corporate print** is answering.
**CLAIM B.** Measured at byte level: its **4** files are *Drug Store News* serial layers and one JAPHA **annual
index**; all 4 sidecars read `route = download/<id>/<id>_djvu.txt (OCR text layer)`; all 4 are recorded in
`harvest_mine/_index.json` as `family: "internet_archive"`; **2 of the 4 are md5-identical to periodicals copies**;
after de-duplication the shelf contributes **0 unique documents** beyond family (c), and family (d) contributes
**zero bytes**.
**WHY THEY DIFFER.** A folder name and a stale count were treated as a corpus family; B asks what the bytes are.
**EVIDENCE WEIGHT.** B. **(d) is TRIED–UNANSWERED (facet), not answered, and not empty-by-nature.**
**BEST-SUPPORTED INTERPRETATION.** Report a **shelving/lineage defect** to the merge; count **2 families**, exactly as
the probe did. **This is the error this project keeps catching, and counting the shelf as print would have produced a
third family out of a second family's bytes.**
**RESIDUAL.** Whether bound CVS/Melville annual reports or house organs exist digitally: `R-3` facet-free, **UNTRIED**.
**CONFIDENCE:** High.

### U.09 — `CVS, Inc.` (RI) and `CVS Pharmacy, Inc.` (RI): one person or two?

**CLAIM A.** `K94` (FY1994 10-K) subsidiary list: *"CVS, Inc., **a Rhode Island corporation**"*.
**CLAIM B.** `K96-405` L8368: *"**CVS Pharmacy, Inc. (formerly known as CVS, Inc.)** is the parent corporation of
Melville Realty Company, Inc., a New York corporation…"*.
**WHY THEY DIFFER.** Nothing — they are the **same person at two dates**, and the later filing states the renaming in
a parenthetical.
**EVIDENCE WEIGHT.** B resolves A directly.
**BEST-SUPPORTED INTERPRETATION.** **RESOLVED:** `CVS, Inc.` → `CVS Pharmacy, Inc.`, Rhode Island, between FY1994 and
FY1996. Recorded as resolved because it is one of the few lineage questions this corpus can actually close — and it is
the **operating** person of the estate, which matters for §U.01 (the operating person is a **Rhode Island**
corporation, not the Delaware registrant and not a 1963 entity).
**RESIDUAL.** The **date** of the renaming is not filed in-window; the FY1995 10-K is on disk and was not searched to
the exclusion of every other exhibit.
**CONFIDENCE:** High.

### U.10 — Supersession: this pass beats the probe's own measurements

**CLAIM A (probe §9.4, §10.1).** *"Consumer Value Stores" → 4 in-window press hits, all **1990-1994***, and *"`founded`
/ `1963` = 0 occurrences"* as a statement about family (a).
**CLAIM B (this pass, at close).** With **OCR line-break-hyphen healing** and **in-file masthead issue-dating**: the
name phrase occurs in **6 rows across 5 unique documents**, issue-dated **1980-01-21, 1983-11-14, 1990-04-09,
1991-05-06, 1993-04-26, 1994-04-25**; `Founded in 19XX` across all 36 SEC files = **4** hits = **1963 × (3 files of one
lineage) + 1994 × 1**; the SEC shelf is now **36** files (7 + 28 + 1), not 7 or 10; the mine index reads
**70 candidates / 12 mined / 57 untried**.
**WHY THEY DIFFER.** A searched raw strings, so `Con-\nsumer Value Stores` (a hyphenated line break in the 1983 row)
was invisible, and A was written while the fleet lane was still adding bytes.
**EVIDENCE WEIGHT.** B — each row was read at its printed line with its issue date derived from the nearest preceding
masthead in the same file.
**BEST-SUPPORTED INTERPRETATION.** **Adopt B; change no tier.** The earliest naming is still **1980**, so S1a and S1b
stay **T3 register** and family (c) stays one family; what B changes is the **strength and reach of the naming
lineage**, which is exactly what §U.02's residual uncertainty turns on.
**RESIDUAL.** 57 untried candidates; the mine's own `named_terms` remains `[]` on all 12 mined items, so the naming
rows are **found by reading, not promoted by the tool** — a coverage warning for the merge.
**CONFIDENCE:** High (that the rows exist); Medium (that the set is complete).

STATUS: WRITTEN 2026-10-06

## CLAIM RECORDS — load-bearing claims only (T2 core, §15.2)

Format per §7. `Archived:` is a dash because no family-(b) capture exists for this company (§S.8, UNTRIED).
URLs are the retrieved forms recorded in each file's sidecar (`http_status 200`, `sha1` present); local held paths are
in §T.1/§T.2. Line numbers are locators only (§14 r12) — anchor on the claim ID.

CVS-A01 Claim: The registrant CVS Corporation was organised as a Delaware corporation on 1996-08-22 — Date:
1996-08-22 — Source: Form 8-B12B (Successor Issuers), CVS Corporation (Successor to Melville Corporation) — Source
date: 1996-11-04 — URL: https://www.sec.gov/Archives/edgar/data/0000064803/000095010396001174/0000950103-96-001174.txt
— Archived: — — Tier: 1 — Class: FACT — Passage: "CVS Corporation ('CVS' or the 'Registrant') was organized as a
corporation on August 22, 1996 under the laws of the State of Delaware." — Conf: High — Corroboration: 1 document;
the FY1996 10-K405 independently describes the same Delaware person — Conflicts: **U.01**

CVS-A02 Claim: Melville Corporation, a New York corporation, was the predecessor and survived the merger renamed CVS
New York, Inc. — Date: 1996-08-30 (agreement) — Source: Form 8-B12B §2 — Source date: 1996-11-04 — URL: as CVS-A01 —
Archived: — — Tier: 1 — Class: FACT — Passage: "Melville will be the surviving corporation (the 'Surviving
Corporation') in the Merger and will be renamed 'CVS New York, Inc.'" — Conf: High — Corroboration: 1 lineage
(`K96-405` L8349 lists the parent corporation of CVS New York, Inc.) — Conflicts: **U.01, U.07**

CVS-A03 Claim: The 1996 registration is a Section 12(b)/(g) successor registration, not a flotation — Date:
1996-11-04 — Source: Form 8-B12B cover — Source date: 1996-11-04 — URL: as CVS-A01 — Archived: — — Tier: 1 —
Class: FACT — Passage: "FOR REGISTRATION OF SECURITIES OF CERTAIN SUCCESSOR ISSUERS FILED PURSUANT TO SECTION 12(b)
OR (g) OF THE SECURITIES EXCHANGE ACT OF 1934" — Conf: High — Corroboration: 2 independent forms (the instrument text;
the EDGAR form census `S-1`/`S-1/A`/`SB-2`/`10-A` = 0 of 2,968 rows) — Conflicts: **U.03**

CVS-A04 Claim: At 1996-12-31 CVS Corporation operated 1,408 stores in 14 states and DC with over $5.5 bn 1996 revenue —
Date: 1996-12-31 — Source: FY1996 Form 10-K405, Item 1 — Source date: 1997-03-31 — URL:
https://www.sec.gov/Archives/edgar/data/0000064803/000095013597001475/0000950135-97-001475.txt — Archived: — —
Tier: 1 — Class: FACT — Passage: "CVS Corporation, a Delaware corporation ('CVS' or the 'Company'), is a leader in the
chain drug industry with over $5.5 billion in revenue in 1996." — Conf: High — Corroboration: 2 (10-K405 and the S-4
lineage give the same estate, one as filed figures and one as a merger description) — Conflicts: None

CVS-A05 Claim: Pharmacare, the PBM subsidiary, is recited as founded in 1994 — Date: 1994 — Source: FY1996 10-K405 —
Source date: 1997-03-31 — URL: as CVS-A04 — Archived: — — Tier: 1 — Class: FACT (the recital) / RESTATED (the date) —
Passage: "Pharmacare, founded in 1994, provides managed care providers a full range of prescription benefit management
services" — Conf: Medium — Corroboration: 1 (the FY1994 10-K names the legal person, not the date) — Conflicts:
**U.01** (a dated founding for a *later* leg, by contrast with the undated 1963 leg)

CVS-A06 Claim: The registrant's own paper recites a 1963 founding of the CVS chain — Date: 1963 (claimed) — Source:
Form S-4 (Revco D.S., Inc. merger registration), "The Companies" — Source date: 1997-03-28 — URL:
https://www.sec.gov/Archives/edgar/data/0000064803/000095010397000191/0000950103-97-000191.txt — Archived: — —
Tier: 1 — Class: **COMPANY CLAIM, RETROSPECTIVE SOURCE** (34 years late) — Passage: "Founded in 1963, CVS is the
country's fifth largest drugstore chain in terms of store count and sales volume" — Conf: **Medium** —
Corroboration: **1 lineage only** — the S-4, S-4/A and the merger DEF 14A print the identical sentence, and the FY1996
10-K405 prints `1963` zero times — Conflicts: **U.01, U.02, U.10**

CVS-A07 Claim: The name change from Melville Corporation to CVS Corporation occurred in November 1996 — Date: 1996-11 —
Source: Form S-4 — Source date: 1997-03-28 — URL: as CVS-A06 — Archived: — — Tier: 1 — Class: FACT (recital) —
Passage: "In November 1996 CVS changed its name from Melville Corporation to CVS Corporation" — Conf: High —
Corroboration: 2 (EDGAR `FORMER CONFORMED NAME` records; the 8-B12B cover) — Conflicts: **U.07** (the proxy of
1996-10-07 shows it was still *proposed* in October)

CVS-A08 Claim: No held SEC byte names a founder, a founding town, an original name or a first store — Date:
1994-02-10→2001-03-30 — Source: full-text term census over 36 stored files — Source date: measured 2026-10-06 —
URL: NO_VERBATIM_PASSAGE (negative measurement) — Archived: — — Tier: 1 — Class: **FACT (of absence)** — Passage:
NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 36 files, one index, re-run after the forward intake pass —
Conflicts: **U.02, U.06**

CVS-A09 Claim: The only post-S-4 `1963` in the SEC shelf is a director's employment history, not a founding — Date:
2001-03-15 — Source: DEF 14A (proxy) — Source date: 2001-03-15 — URL:
https://www.sec.gov/Archives/edgar/data/0000064803/000092701601001365/0000927016-01-001365.txt — Archived: — —
Tier: 1 — Class: FACT — Passage: "From 1963 to March 1998, he was President of" — Conf: High — Corroboration: 1 —
Conflicts: **U.06**

CVS-A10 Claim: The registrant states critical mass and geography as the condition of competing, naming food/drug
combos, mail order and mass merchandisers as the alternative channels — Date: 1997-03-28 — Source: Form S-4, "Our
Reasons for the Merger" — Source date: 1997-03-28 — URL: as CVS-A06 — Archived: — — Tier: 1 — Class: FACT (as filed
words); RETROSPECTIVE INTERPRETATION if used as motive — Passage: "Achieving a critical mass in terms of store count
and locating our stores in appropriate geographic markets is essential to competing effectively in the chain drugstore
industry" — Conf: High (text) / Medium (motive) — Corroboration: 1 lineage — Conflicts: None

CVS-A11 Claim: The chain grew by acquisition (Peoples 1990, Standard Drug 1994) plus an average of 77 openings a year —
Date: 1990, 1994 — Source: Form S-4 — Source date: 1997-03-28 — URL: as CVS-A06 — Archived: — — Tier: 1 —
Class: FACT (year-only) — Passage: "CVS acquired Peoples Drugs Stores in 1990 and Standard Drug Stores in 1994, and
has added an average of 77 stores in each of the past five years" — Conf: High — Corroboration: 2 lineages (the
independent trade press dates and prices the Peoples act) — Conflicts: **U.04, U.05**

CVS-A12 Claim: In 1983 the chain named Consumer Value Stores, glossed CVS, headquartered in Woonsocket, planned ≥50
stores a year and a 150,000-sq.-ft. own warehouse — Date: 1983-11-14 — Source: Drug Store News (Lebhar-Friedman),
"CVS weighs warehouse growth in three regions" — Source date: 1983-11-14 (in-file masthead) — URL:
https://archive.org/download/micro_IA40706915_0203/micro_IA40706915_0203_djvu.txt — Archived: — — Tier: 3 —
Class: CONTEMPORANEOUS OBSERVATION — Passage: "Anticipating the opening of at least 50 new stores each year, Con-sumer
Value Stores (CVS) has announced tentative plans for the construction or lease of a 150,000-sq.-ft. bulk storage and
promotional goods warehouse here." — Conf: **Medium — capped by UNVERIFIED TLS** — Corroboration: 1 (independent of
the SEC lineage, which never prints the name) — Conflicts: **U.02, U.10**

CVS-A13 Claim: Melville, operating an 820-store CVS, completed the 490-store Peoples Drug purchase from Imasco for
$325 million cash on 1990-09-17, keeping the Peoples name — Date: 1990-09-17 — Source: Drug Store News — Source date:
1990-09-24 (in-file masthead) — URL: https://archive.org/download/micro_IA40706934_0338/micro_IA40706934_0338_djvu.txt
— Archived: — — Tier: 3 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "Melville Corp., which operates 820-store CVS,
completed the acquisition of 490-store Peoples Drug Stores from Imasco Ltd. of Montreal Sept. 17. The purchase price
was $325 million in cash." — Conf: Medium (TLS) — Corroboration: 2 lineages for **the event**, 1 for **the price** —
Conflicts: **U.05**

CVS-A14 Claim: The chain's warehousing reached 2,075,000 sq ft after a 400,000-sq.-ft. New Jersey DC — Date:
1990-04-09 (reporting the prior year) — Source: Drug Store News, "CVS at a glance" survey — Source date: 1990-04-09 —
URL: as CVS-A13 — Archived: — — Tier: 3 — Class: CONTEMPORANEOUS OBSERVATION / ESTIMATE (OCR corruption in the
sentence) — Passage: "That raised the chain's warehousing footage to 2,075,000 square feet." — Conf: Medium —
Corroboration: 1 — Conflicts: None

CVS-A15 Claim: The estate's real estate and store-level entities sit under CVS Pharmacy, Inc. and Nashua Hollis CVS,
Inc. — Date: 1996-12-31 — Source: FY1996 10-K405 subsidiary list — Source date: 1997-03-31 — URL: as CVS-A04 —
Archived: — — Tier: 1 — Class: FACT — Passage: "CVS Pharmacy, Inc. (formerly known as CVS, Inc.) is the parent
corporation of Melville Realty Company, Inc., a New York corporation" — Conf: High — Corroboration: 1 filing;
SC 13D 1996-04-08 names the same holders at an earlier date — Conflicts: **U.09** (resolved)

CVS-A16 Claim: In 1994 the registrant benchmarked itself against general retailers, with three drug chains inside the
set — Date: 1994-03-14 — Source: Melville DEF 14A, compensation peer list — Source date: 1994-03-14 — URL:
https://www.sec.gov/Archives/edgar/data/0000064803/000095011094000065/0000950110-94-000065.txt — Archived: — —
Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION (the company's own in-period market definition) — Passage: "Dayton
Hudson, Edison Brothers, JC Penney, Longs Drug, Merry Go Round, Rite Aid, Sears, TJX, Toys R Us, U.S. Shoe, Walgreen
and Woolworth" — Conf: High — Corroboration: 1 — Conflicts: None

CVS-A17 Claim: The acquired Peoples name was erased: 400 former Peoples stores renamed CVS — Date: 1994 (as reported) —
Source: Drug Store News — Source date: within the 1994-11-07→1995-10-23 layer — URL:
https://archive.org/download/micro_IA40706951_0247/micro_IA40706951_0247_djvu.txt — Archived: — — Tier: 3 —
Class: CONTEMPORANEOUS OBSERVATION — Passage: "the 400 former Peoples stores (renamed CVS stores last year)" —
Conf: Medium — Corroboration: 1 lineage; scope conflicts with the filed segment counts — Conflicts: **U.05**

CVS-A18 Claim: On or about 1996-03-15 the TJX preferred was moved from Melville down the CVS holding chain — Date:
1996-03-15 — Source: SC 13D filed by Melville, subject TJX Companies Inc /DE/ — Source date: 1996-04-08 — URL:
https://www.sec.gov/Archives/edgar/data/0000064803/000095010396000813/0000950103-96-000813.txt — Archived: — —
Tier: 1 — Class: FACT — Passage: "Melville transferred all such shares of Series D Preferred Stock and Series E
Preferred Stock to CVS Center, Inc., which in turn transfereed all such shares to CVS H.C., Inc." (filing's own
misspelling of "transferred", twice) — Conf: High — Corroboration: 1 — Conflicts: **U.07**

CVS-A19 Claim: Exiting the non-drug legs cost an after-tax $585 m in Q4-1995, separate from a $195 m Marshalls charge —
Date: 1995-10-26 — Source: Melville 8-K, Item 5 — Source date: 1995-10-26 — URL:
https://www.sec.gov/Archives/edgar/data/0000064803/000095010395000374/0000950103-95-000374.txt — Archived: — —
Tier: 1 — Class: FACT — Passage: "the Company will record in the fourth quarter of 1995 an after-tax charge of $585
million. This charge excludes the previously announced estimated after-tax charge of $195 million for the divestiture
of Marshalls." — Conf: High — Corroboration: 1 accession, quoted from the press release attached to it — Conflicts:
None

**CVS-A20 Claim (recorded as a retraction-preventer).** The folk origin — 1963 shoe store, *Consumer Value Stores* as
the 1963 entity, Jacksonville, the Riverside–Newport naming — **is NOT claimed.** — Date: 1963 — Source: none held —
Source date: UNKNOWN — URL: NO_VERBATIM_PASSAGE — Archived: — — Tier: UNKNOWN — Class: **UNKNOWN** — Passage:
NO_VERBATIM_PASSAGE_RECORDED — Conf: UNKNOWN — Corroboration: 0 of 5 families carry it; 3 of 5 families are UNTRIED
or unanswered — Conflicts: **U.02, U.06**

---

---

## registers — Register rows applied to the nine CSVs (merge pass, 2026-10-07)

The nine `>>> REGISTER ROWS FOR MERGE <<<` blocks emitted by `_parts/s1_p1.md` (126 rows: quantitative 29 ·
timeline 24 · sources 18 · conflicts 10 · data_gaps 10 · decisions 14 · validation 8 · failures 7 · channels 6)
were applied verbatim to the nine CSVs at this directory root. Every `PROV-CVS-nn` cell was remapped to its
minted global id (S4431–S4448, table above); `source_id` values in `timeline.csv`/`decisions.csv`/
`validation.csv`/`failures.csv`/`channels.csv` carry the same minted ids. `decisions.csv` row 1 was trimmed from
16 to 15 columns by dropping one spurious `UNKNOWN` (COR-02) — no value added, moved, or changed. `timeline.csv`
carried `source_id` as a **per-row running counter** (`PROV-CVS-01…24`), not as a foreign key into the 18-row
`sources.csv`; cells `PROV-CVS-19…24` therefore mapped past the minted block to ids the merge never allocated,
and were repointed by the merge to the carrier each row's own note names (`S4445` for the 1996-03-15
TJX-preferred transfer / SC 13D; `S4431` for the 8-B12B succession rows) per **COR-04**. The counter values 01–18 happen to resolve as keys but are not
guaranteed to be the semantically-correct carrier (e.g. the 1987 DSN-88 layer behind timeline row 7 is not among
the emitted sources), so full semantic reconciliation of the column is left to the citation auditor and named in
`CORRECTIONS.md`; the merger did not silently re-key what the gate could not see. The blocks' verbatim text stays
in the part as the emission of record; they are not reprinted here (method §13).

**Register totals applied:** 126 rows on disk, **0 unapplied, 0 added by the merge**.

**Rows withheld by the author and kept in prose (not a merge drop):** the §T.5 manifest-drift note and the
§U.10 measurement-supersession narrative were held out of the schemas by the author; the merge left them as
prose. No register row this part owns was dropped.

**Not corrected, and why:** this merge issued no retraction of the author's claims. The corrections in
`CORRECTIONS.md` are key/propagation/schema entries (COR-01 id supersession, COR-02 the decisions width fix,
COR-03 the validation/failures block binding), not claim retractions; the probe's earlier census states
(36/6/29, 68/12/55) that §U.10 reports as stale are left visible, not deleted.

