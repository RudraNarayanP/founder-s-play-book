# Alphabet (Google Inc.) — Stage 1: the origin block, 1998-01-09 to 2001

<!-- ANCHORS: U.017-U.036 -->

**Dataset:** The Founder's Playbook, company 005 (Alphabet Inc., registrant Google Inc., CIK 1288776), Stage 1. **Tier T1 exemplar** (method §15.2), so the per-file cap is 60,000 words. **Canonical structured data is the nine CSV registers at this directory root** — the fenced `csv` blocks printed below are the parts' emissions, carried verbatim as provenance. **DO NOT RE-APPLY THOSE BLOCKS: they are already applied, 180 requested rows into 169 register rows (11 folded, 0 refused), and a second application would double-count them.**

## Stage 1 merge note

**Geometry (method §9.2/§9.3, arithmetic stated).** The two part bodies measure 20,855 and 35,677 words (145,481 B and 244,114 B) once each part's filename H1 and part 1's stale `SCAFFOLDED … nothing written yet` banner are dropped (−41 w and −15 w: 257 B and 102 B); as emitted, `_parts/s1_p1.md` is 20,896 w (not the 21,629 w my brief reported) and `_parts/s1_p2.md` 35,692 w, so **56,588 w combined — above §9.2's 40,000 soft target, inside the 40,000-60,000 amber band, and 3,412 w below the 60,000 hard cap for a T1 company, and the built volume lands 2,642 w below it**. §9.2 permits an amber stage to finish as one file and §9.3 triggers a split only *at* the cap, so this stage is merged as the single volume `stage_1.md` (**57,358 w / 395,186 B** as built) and no `stage_1_part_n.md` geometry is used. The two-part alternative was rejected on three grounds: it would put the §9.3 test to a file that has not hit the cap; a split between §F and §G would strand the boundary argument (part 1) from its one correction (part 2 §J.0 / U.024), which sit on either side of the only clean section boundary; and one volume keeps both part bodies provably intact. **§A–§U numbering is continuous and nothing was renumbered** (§9.3), and §9.6 forbids trimming evidence to fit a limit, which is why no content was cut to buy margin.

**Carried stale prose, named not edited.** Part 1's Header still prints `**File:** part 1 of 3 for Stage 1.`; the corpus has two parts and this pass built one volume. The sentence sits inside a protected byte slice, so it is corrected here rather than rewritten there, and §9.3 forbids renumbering a part to make a carried volume look self-contained.

**What was applied.** 180 register rows from two emissions — 70 in `_parts/s1_p1.md` (§Header, §Boundary, §A–§F) and 110 in `_parts/s1_p2.md` (§G–§U) — into nine registers as **169 rows: 11 folded into 11 listed collision groups, 0 refused**. `tools/merge_census.py` attributed only 157 of them and printed the `validation.csv`/`failures.csv` pair as `AMBIGUOUS:validation.csv,failures.csv` (9 rows + 14 rows): the two schemas share all 11 column names, so no header-overlap matcher can separate them (**RD-132**). Those 23 were attributed by the rows' own leading `notes` tags — 13 `validation`, 10 `failures`, 0 dropped. The census also reads `_parts/*.md` and fenced `csv` only, so `research/` was searched by hand for a fourth emission (**RD-122/RD-131**): `B1_filing_records.md`, `A_chronology_feasibility.md`, `A2_periodical_settlement.md` and `A4_harvest_mine.md` contain **zero** fenced blocks — B01–B43 are claim records and U-1–U-16 hyphen-form keys, cited and aliased in register `notes`, never rows to apply.

**Ids.** 21 global source ids, **S4332–S4352**, allocated through the locked `tools/id_mint.py --claim` (above the highest live id; recorded in `00_universe/_ID_BLOCKS.tsv` against `company_005_alphabet` / `alphabet-s1-merge`) — not from a snapshot of free ranges, which is how RD-132's near-collision happened. Checked against the live register corpus and the registry before application: 0 collisions. The retired dossier-local keys `P1SRC01`–`P1SRC11` / `P2SRC01`–`P2SRC11` stay printed in the `notes` cell of the row that replaces them and inside every `MERGE[...]` marker (**COR-07**).

**Anchors.** Part 1 minted and declared **none** (zero `U.n` tokens in `_parts/s1_p1.md`); part 2 declares **U.017–U.036 (20)**, which is therefore the union, restated in the machine comment above. The upstream dossiers' hyphen-form keys (`U-1`–`U-16`) are a different namespace and are not anchors. Register-cited anchors: exactly 20 distinct, **U.017–U.030 in `conflicts.csv`, U.031–U.036 in `data_gaps.csv`** → parity 20 narrative ↔ 20 register, 0 undeclared, 0 uncovered.

**Corrections on this pass: COR-01 … COR-08** (full text in `CORRECTIONS.md`, each tagged into the register rows that carried the withdrawn claim): COR-01 the probe's Q1-1999 close and the 1996-2004 harvest window, both refuted at §Boundary; COR-02 the records dossier's single-file-number lineage map; COR-03 part 1's 'no cost figure before 2003 / no carrier' leg; COR-04 refusal (iii)'s 'no money quantum' half; COR-05 the undated rescission ceiling; COR-06 the tool-blind shared register blocks; COR-07 the retired local source keys; COR-08 two carried citation defects (a line range that stops mid-sentence, a byte count the disk contradicts).

## Volume 1 — origin block (Header, Boundary, §A–§F)

*Carried byte-identically from `_parts/s1_p1.md`; its 24 claim records `P1A01`–`P1F04` and 8 emission blocks are intact below.*

## Header

STATUS: WRITTEN 2026-09-26

### Dataset, stage, and how to read this volume

*One document split for the file cap (method §9.3). Section letters, claim IDs, metric IDs and
conflict numbering run continuously across volumes: **§Header, §Boundary and §A–§F live here
(`_parts/s1_p1.md`); §G–§U and the claim-record appendix continue in the later passes.** Cross-references
of the form `(Alphabet S1 §D.2, part_1)` name the volume. Nothing is renumbered to make a part look
self-contained.*

**Dataset:** The Founder's Playbook — forensic reconstruction of what each company in the frozen universe
(`00_universe/`) looked like while its outcome was still unknown.

**Company (rank 5):** today's registrant is "Alphabet Inc." (GOOGL/GOOG, CIK 1652044); the registrant this
Stage-1 volume writes is **Google Inc., CIK 1288776**, a Delaware corporation whose EDGAR enumeration
begins 2001-03-12 (a paper REGDEX row) and whose first registration statement is dated 2004-04-29. What
CIK 1652044 is to CIK 1288776 is **UNKNOWN on held bytes** and is not assumed anywhere in this volume
(inherited conflict U-2, `research/A_chronology_feasibility.md`). **Tier: T1 exemplar** (§15.2), issued for
this stage by the probe and read on its own terms: "T1 from the IPO end, thin at the founding end."
**File:** part 1 of 3 for Stage 1.

**Stage:** 1 of 3. **Span adopted:** **1998-01-09 → 2001 (year-granular; the closing day is UNKNOWN)**,
i.e. documented pre-entity invention under a third party's ownership, through incorporation, the first
public prototype, the first licensed product, the replacement of the founding revenue model, and the
company's own first stated profitable year. The argument, the five rejected rival geometries and the
harvest-window correction are at `## Boundary`. **Stage definition (§7):** origin → first real-world
experiment → repeatable validation → scalable company formation. For a two-sided advertising business the
four beats are *the ranking invention, the publicly visible prototype, the first paying licence, and the
day the company stopped selling search results wholesale to a handful of sites* — and all four have a
dated carrier inside this window. Post-boundary material is tagged `(PB)` wherever it is used, and the
largest single body of held evidence in this dossier (the 2004 registration lineage, plus a 2004 customer
contract) is **retrospective with respect to almost all of Stage 1**; it is a 2004 document about 1998-2001,
tagged `RETROSPECTIVE SOURCE` per §6 on every record it carries.

**Hindsight firewall (§2).** Nothing here treats the 2004 offering, the later Alphabet holding-company
reorganisation, or any post-2001 outcome as evidence that a 1998-2001 decision was rational, that the
licensing model was obviously dead, or that ranking quality was destined to be the product. The patent's
Background section is read as a 1998 statement of what one inventor thought the problem was, not as a
preview of the company. The founders' 2004 letter is read as a 2004 statement, not as a 1998 one. The words
"visionary", "genius", "inevitable" and "disruptive" do not occur in this volume outside quotation marks
that belong to someone else. Anti-hagiography test applied per §2 to every coda: each of §A.4, §B.6, §C.5,
§D.5, §E.5 and §F.6 states what would still have been true if the company had failed in 2003.
**Record-selection null (§2).** Unrecoverable *because the survivors' archive is the one that was kept*:
no internal deliberation of 1998-2001 survives in any of the five families this run reached — not a memo,
not a rejected option, not a dissent, not a feasibility study, not a price list; **zero** held bytes record
anyone at Google deciding anything in the window except in retrospect, in a document drafted to sell
shares. The first licensee is unnamed in every held document. There is no independent count of queries,
index size, traffic or users for 1998-2001 anywhere in the corpus. The one dated operating record of the
founding period that is not the company's own prose — the Stanford licence — has its **money fields
redacted under confidential treatment** (`[***]`), so the earliest surviving non-company document about
Google's first year withholds precisely the numbers. And the whole 1998-2001 money picture rests on two
annual revenue totals printed by the issuer in 2004 **outside the auditor's attested band** (§K inherits
this from the records dossier's B15). See §A.4, §C.4, §D.4, §F.5.

**Confidence (§3):** **High** = 2+ independent origins, or a primary document speaking for its own date;
**Medium** = one reliable source, or a retrospective-only primary, or any claim resting solely on a layer
fetched over **UNVERIFIED TLS**; **Low** = conflicting, vague, or retrospective-only with no primary
carrier; **UNKNOWN** = a finding, never a gap to fill or smooth.

**The two-lineage finding, stated once and enforced everywhere (§3 filing-lineage rule).** Two lineages
dominate this dossier and neither may be counted twice.
1. **LIN-REG** — the 2004 registration text: nine held accessions plus the **unheld** 424B4. Under §3 these
   are **one source**, and a figure appearing in all nine is one source nine times. **This pass found that
   the lineage is not even one file number** (see §Boundary.4, conflict **P1CNF01**): the held printings carry
   two Securities Act registration numbers with **independent amendment counts**, and the auditors' own
   consent inside the later-numbered printings still incorporates the earlier one. The lineage therefore
   stays one *instrument* for independence purposes — no held document says a second registration statement
   was filed on new facts — but it is **no longer correct to describe it as "one instrument under file no.
   333-117934"**, which is what the records dossier asserts.
2. **LIN-FOUNDER** — the founders' own account (the letter, and every later company history page tracing to
   it), printed inside LIN-REG and reprinted since. Zero independence.
Outside both lineages this company has exactly **four** dated carriers on disk: the patent grant record
(1998-01-09 priority), the Wayback capture (1998-11-11 18:45:51), one third-party consumer-magazine issue
(2000-07, held over UNVERIFIED TLS), and one executed customer contract held by a government archive
(2004-11, `(PB)`). Two of those four are inside the Stage-1 window. That is the whole independent base,
and it is reported as the finding rather than repaired.

**ID scheme (§13, read before citing).** Claim records in this volume are **`P1<SectionLetter><nn>`**
(`P1A01`, `P1B04`). Register rows carry a **three-letter register tag so they can never collide with a
section's claim records**: sources `P1SRCxx`, quantitative `P1QTNxx`, timeline `P1TMLxx`, decisions
`P1DECxx`, validation `P1VALxx`, failures `P1FAIxx`, channels `P1CHNxx`, conflicts `P1CNFxx`, data gaps
`P1GAPxx`. All `P1x` ids are **dossier-local**; global `source_id` blocks are assigned **centrally at
merge** and nothing here is a global key. **Later passes continue both schemes unchanged** (claim records
`P2G01…`, `P3I01…`; registers `P2SRC01…`, `P3QTN01…`) and must not re-base them. Conflict records already
minted upstream are cited by their local ids (`B07`, `B15`, `U-7`) and are **not** re-emitted as fresh
rows. **Conflict numbering:** `research/A_chronology_feasibility.md` minted U-1..U-5 and
`research/B1_filing_records.md` minted U-6..U-16; this volume mints **P1CNF01..** locally and *proposes*
U-17 onward for the merge to mint — a dossier may propose an id, never assume one (RD-123).

---

## Boundary

STATUS: WRITTEN 2026-09-26

**Geometry note.** This section enumerates the candidate openings, closings and search windows, names the
document behind each, and states why each rival **fails** — it does not assert a boundary and then defend
it rhetorically. Five losers are named. One of them (**P1CNF01**, the registration-number question) is not
resolved and is not resolvable from held bytes; it stays live.

### 0. The brief's "1996-2004" is a harvest window, not a stage window

The dispatch framing — *Alphabet's origin window is 1996-2004 (search engine founding through IPO)* — is
the range over which sources were **mined** (`research/A4_harvest_mine.md` applies
`1996-01-01 .. 2004-12-31` and says so: "deliberately WIDE where the founding date is itself
unestablished"). RD-112's standing ruling is that a stage is measured against **its own** window, "never
against the probe's search range", and it was written because that exact conflation moved a tier verdict.
Reading 1996-2004 as Stage 1 would (i) open the stage on a year with **no dated carrier of any kind** and
(ii) close it at the offering, making Stage 1 the whole filed life of the company to date and leaving
Stages 2 and 3 no distinct question. Both are rejected below. What the wide window *does* legitimately
supply is the mining perimeter, and it is honoured: nothing in the mine's 1996-1997 stretch was dropped
for being out of stage — there was nothing in it to drop (**0** entity-bearing items across the four items
the mine reached, 1 bare-word match, 2 NULLs, 1 UNANSWERED).

### 1. The opening: what is documented before the company

| Candidate opening | Best carrier on disk | Verdict |
|---|---|---|
| **1998-01-09** — U.S. patent 6,285,999 filed; assignee Leland Stanford Junior University; inventor Lawrence Page | grant record `sources/patents/us6285999.html` (398,323 chars of tag-stripped text read this pass) + executed licence recital (`B04`) | **ADOPTED.** Earliest date in the corpus fixed by a third party's register, independent of the founders' narrative. Kept **outside** the company (§B.1) because at this date the registrant did not exist. |
| **1996** — the Stanford docket year | licence recital: invention "as described in Stanford Docket S96-213" (`B05`) | **REJECTED (loser 1) as a dated opening; RETAINED as an undated inference.** The year is read out of a numbering convention by the reader, not printed as an event by any held document. §B.2 keeps the 1996 leg on the record at UNKNOWN, because deleting the only hint of the invention's gestation is as distorting as dating it. |
| **1998-09** — incorporation "in California in September 1998" | S-1 Corporate Information (`B01`, `B02`), plus two internal anchors that presuppose it: the 1998 Stock Plan "adopted by our board of directors in September 1998" (`B24`) and the licence Original Agreement "effective December 1, 1998" (`B06`, `B29`) | **ADOPTED as the entity opening**, at month granularity. The **day is UNKNOWN** and the popular day-level date is unsupported in this corpus (inherited U-7). Not upgraded by repetition: three printings of one sentence are one sentence. |
| **1998-11-11** — first public evidence of a service | Wayback capture of `http://google.com:80/`, 212 B (`B07`) | **ADOPTED as the experiment boundary**, not as the origin. A *terminus ante quem*: it bounds the origin from above and says nothing about who founded what, when, or why. |

### 2. The closing: five candidates, one adopted

| # | Candidate Stage-1 close | Evidence for it | Verdict |
|---|---|---|---|
| 1 | **2001 (year only)** — "We became profitable in 2001 following the launch of our Google AdWords program" | S-1 (LIN-REG), `B03`; plus the Q1-2000 introduction of Premium Sponsorships and the Q4-2000 launch of AdWords (§D.3, text read this pass) | **ADOPTED.** The first closing where §7's fourth beat — *scalable company formation* — has a dated carrier rather than a later commentary: by the end of it the company had a self-service revenue mechanism that did not require a sales conversation per customer, and it had, on its own account, stopped losing money. Day-level close is **UNKNOWN**; "2001-12-31" is a calendar convention, not an event, and is labelled as such wherever a date is needed. |
| 2 | **Q1 1999** — first WebSearch licensing | S-1; the probe's own recommendation (its B2) | **REJECTED (loser 2); recorded as a live disagreement with the probe dossier, not smoothed.** It would end Stage 1 *before* any evidence of the fourth beat, and would throw the window's only two quantified operating facts — FY1999 $220 thousand and FY2000 $19,108 thousand net revenues (`B11`) — outside the stage while keeping the sentences that explain them inside it. The probe argued its split before the 2004 lineage had been read; this pass had read it. |
| 3 | **2004-08-19** — the 424B4 | `_index/submissions.csv` enumeration | **REJECTED (loser 3).** The RD-112 error: a search range read as a stage. Also an evidentiary illusion — the 424B4 is **not held on disk** (re-verified this pass: no accession `-143377` among the 127 files under `sources/`), so the offering's own document is absent from the corpus that would close on it. |
| 4 | **2003-08 / 2003-10-13** — Delaware reincorporation; Stanford licence restated | S-1 ("In August 2003, we reincorporated in Delaware"); exhibit `dex1010.htm` (`B29`) | **REJECTED (loser 4) as the close; ADOPTED as a later-stage internal discontinuity.** A re-domiciliation on the path to an offering is a *legal* event, not the formation of a scalable business, and it post-dates the company's own stated profitability by two years. Retained at §B.4 because a single "Google Inc." framing hides a real CA-1998 → DE-2003 break in registrant identity. |
| 5 | **2002-12** — AdSense-era platform shift; Overture suit filed 2002-04 | `B39`, `B41` | **REJECTED (loser 5) as too late to be Stage 1 and too thin to be its own boundary**: the suit's filing month is one carrier's refinement of another carrier's year (inherited U-16), and 2002 is the year the *gross-versus-net presentation question* begins (inherited U-9), which is an accounting event visible only in a 2004 document, not a formation event in 2002. |

### 3. What the boundary refuses to claim

Four statements this volume will not make, whatever they cost it:
(i) **no founding day**; (ii) **no first customer**; (iii) **no pre-IPO funding round** — the closest the
corpus comes is a *valuation recital* (`B30`: "a Eight Million Dollars ($8,000,000) post-money valuation")
inside a counterparty's agreement, and a valuation is not a date, not an amount raised, and not a round
this dossier can name; (iv) **no IPO price or sale date** — `$121.50` is an *assumed* price in a
registration statement (`B28`), and the document that would carry the real one is unheld.

### 4. A carrier-level correction to the inherited lineage map

The records dossier opens: *"a single registration statement of Google Inc. (CIK 1288776, file no.
333-117934 / 000-50726), filed as an S-1 on 2004-04-29 and re-filed as S-1/A eight times"*. Reading the
SGML header and cover page of each of the nine held `.txt` submissions this pass, that string does not
reproduce: five of the eight registration-statement printings carry **`333-114984`**, two carry
**`333-117934`**, and one of the `333-117934` printings styles itself **"Amendment No. 1"** while a
*later-dated* `333-114984` printing styles itself **"Amendment No. 5"**. The amendment counts therefore
restart under the second number, and the two series interleave by date. Full enumeration, carrier by
carrier, is at **P1CNF01** and in the carrier table under `## Register rows for merge`; the reading this volume
adopts — and the only reading held bytes
support — is that this is one developing registration statement known to EDGAR under two Securities Act
numbers, because the Ernst & Young consent printed inside the `333-117934` printings incorporates by
reference *"the Registrant's registration statement on Form S-1, as amended (File No. 333-114984),
initially filed with the Securities and Exchange Commission on April 29, 2004"*: an auditor's own words
tying the two numbers to one statement and one initial filing date. Whether SEC re-numbered the statement
or the registrant opened a parallel number is **UNKNOWN**. What is not UNKNOWN is that the dossier's
file-number premise and its "eight amendments" count are wrong as printed, and that its inherited U-6 —
which left the 2004-08-04 form-label anomaly at Low confidence — had the answer inside its own row set: a
fresh number begins exactly at that accession.

## A

STATUS: WRITTEN 2026-09-26

### A.1 Executive state summary — the registrant's condition across the stage, as held bytes state it

**The sentence this stage has to earn.** Between the earliest dated artifact and the adopted close, the
thing in the record changes kind three times: it is **a third party's invention** (1998-01-09, Stanford's,
one named inventor), then **a public prototype with no legal person attached to it in any held document**
(1998-11-11), then **a licensing company** (Q1 1999), then **an advertising company** (Q1 2000 mechanism,
Q4 2000 self-service mechanism, 2001 self-stated first profitable year). Every one of those four
characterisations has a carrier in `sources/`; none of them is imported from the 2004 outcome.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Earliest dated artifact bearing on the company | 1998-01-09, U.S. patent 6,285,999 filed (app. US09/004,827) | `sources/patents/us6285999.html`; recital in `sources/sec/0001193125-04-105564_dex1010.htm` | High |
| Owner of the priority technology at that date | Leland Stanford Junior University — **not** the company, **not** the inventors | same two carriers | High |
| Named inventor on the priority document | Lawrence Page (one name) | `sources/patents/us6285999.html` | High |
| Legal entity | "incorporated in California in September 1998"; **day UNKNOWN** | S-1 Corporate Information and Note 1 (records B01, B02) | Medium |
| Registrant continuity | California 1998 → Delaware August 2003 `(PB)`; CIK 1288776; relation to CIK 1652044 UNKNOWN | S-1; `_index/` (records B01; inherited U-2) | High for DE-2003, UNKNOWN for the bridge |
| First public evidence a service existed | 1998-11-11 18:45:51, `http://google.com:80/`, HTTP 200, 212 B | `sources/wayback/google_19981111_raw.html` + `cdx_retry.json` | High |
| What that page said the product was | "Google Search Engine Prototype"; "Might-work-some-of-the-time-prototype that is much more up to date" | same | High |
| Where the two services lived on that date | prototype at `google.stanford.edu`; the "more up to date" one at `alpha.google.com` (both as hrefs in the page's own markup) | same — **new finding, §E.2** | High as to the markup; INFERENCE as to what it implies about hosting |
| First licensed product and date | "WebSearch", "in the first quarter of 1999" | S-1 (record B03) | Medium; quarter granularity only |
| First named licensee | **UNKNOWN** — no held document of any family names one | — | — |
| First executed contract with an outside institution | Stanford licence Original Agreement "effective December 1, 1998" | `dex1010.htm` §1.1 (records B06, B29) | High |
| Founding revenue model, in the issuer's own words | "Our original business model consisted of licensing our search engine services to other web sites." | S-1 "How We Generate Revenue" — **new text, §D.3** | Medium |
| Replacement mechanism and its dates | Q1 2000 Premium Sponsorships (direct sales, paid per ad displayed) → Q4 2000 Google AdWords (self-service) | same paragraph — **new text, §D.3** | Medium |
| First stated profitable year | "We became profitable in 2001" | S-1 (record B03) | Medium — self-report, year granularity |
| Money in window | FY1999 net revenues $220 thousand; FY2000 $19,108 thousand (`$ thousands` as filed: 220 / 19,108) | S-1 Summary Consolidated Financial Data (record B11) | Medium — **outside the auditor's attested band**, which starts at 2001 (record B15) |
| Operating detail 1998-2000 (costs, headcount, users, cash) | **UNKNOWN**; no carrier | record B18 | — |
| Headcount | **UNKNOWN for every date in this window**; first carrier is 1,907 at 2004-03-31 `(PB)` | S-1 "People" (record B17) | — |
| Customer concentration | "No customer accounted for greater than 10% of net revenues in 2001, 2002 and 2003" | S-1 audited notes — **new text, §F.3** | High (audited) but the window's first year is a bound, not a count |
| Independent third-party characterisation inside the window | July 2000 consumer magazine ranks Google **4th** in a search round-up: "Our new favorite for general searches… uses proprietary technology to ensure that the first hits you get for your search are the best" | `sources/periodicals/yahoo-internet-life-magazine-july-2000_djvu.txt` l.11026-11036 | Medium — UNVERIFIED TLS, and Tier-3 press under §5 |
| Periodical corroboration of the *founding* | **NONE**: 0 hits for the founders' names across every held periodical byte | `research/A2_periodical_settlement.md`; record B10 | High as to the null |

### A.2 What kind of company this was at the close of the stage

By the end of 2001, on the evidence held and nothing else: **one Delaware-not-yet, California entity, two
founders listed as its officers, a technology it did not own, an annual report line of $86.4 million of
net revenues `(PB figure)`, no disclosed customer relationship that mattered more than a tenth of its
money, no named first licensee, a self-described switch from selling search to selling advertising, and a
patent suit against its main ad mechanism already on foot since April 2002** — the last item being the
first thing in this dossier that shows the model it had just adopted was contestable by a competitor.
That description is deliberately unflattering-adjacent: it is what a reader in 2001-12-31 could have said,
and it is close to the floor of what this corpus can support.

### A.3 What the state summary cannot say

Three absences that a reader will expect and that this corpus cannot supply at any tier: **no user, query,
traffic or index number for any date inside the stage from any carrier other than a 1998 patent
background describing somebody else's search engine** (§C.3, P1QTN02/P1QTN03); **no dated funding event**;
**no internal voice**. The 2004 filings are rich about 2003 and empty about 1999, and the emptiness is
structural: an issuer describes what its underwriters need described.

### A.4 Coda, and the firewall test (§7 line-format duty, §15.4)

**Mechanism, as far as evidence reaches:** the company's revenue base changed kind twice inside the window
(wholesale licensing → advertised search → self-service advertised search), and each change is dated by the
issuer in quarter-or-year granularity only. **Alternative explanation not excluded:** the same disclosure
is compatible with the licensing business having remained the larger share of revenue well past Q1 2000 —
FY1999's $220 thousand and FY2000's $19,108 thousand are totals without a split by model, and no held line
apportions them. **Anti-hagiography test:** if Google had failed in 2003, §A.1 would still read as
plausible, because it asserts no destiny — the ranking invention, the prototype's self-labelled
unfinishedness, the licensing start, the mechanism switch and the unaudited early totals are all statements
about the record, and the word "inevitable" appears nowhere in this section. Confidence in the section as a
whole: **Medium**, capped by LIN-REG dependence (a 2004 self-report) for everything except the two
registry/archive rows.

### A.5 Load-bearing claim records for §A

P1A01 Claim: The earliest dated artifact bearing on this company is a patent filed by a third party's
inventor, and it names one inventor. — Date: 1998-01-09 — Source path:
`sources/patents/us6285999.html` (398,323 chars tag-stripped, read this pass) — Source date: 2001-09-04
(grant); priority filing 1998-01-09 — URL: patents.google.com/patent/US6285999B1/en — Archived: as path —
Tier: 1 — Class: FACT (registry record) — Passage: "STANFORD has an assignment of 'Improved text searching
in hypertext systems' developed by Lawrence Page" is the licence's recital of the same object; the grant
record itself carries filing date 1998-01-09, application US09/004,827, assignee Leland Stanford Junior
University — Conf: High — Corroboration: 2 independent (registry + executed bilateral licence recital) —
Conflicts: None (this is the B04/B05 pair; not re-emitted).
independence_note: registry custody is outside the founders' narrative; the two dates agree across the two
carriers.

P1A02 Claim: On the earliest date any independent party recorded a public Google service, the company's own
page described the product as unfinished and located the "up to date" variant on a different host from the
prototype. — Date: 1998-11-11 18:45:51 — Source path: `sources/wayback/google_19981111_raw.html` (212 B) +
`sources/wayback/cdx_retry.json` + `.sidecar.json` — Source date: 1998-11-11 — URL:
web.archive.org/web/19981111184551id_/http://google.com/ — Archived: as path — Tier: 1 (archived company
page) — Class: CONTEMPORANEOUS OBSERVATION — Passage: "Google Search Engine Prototype …
Might-work-some-of-the-time-prototype that is much more up to date." — Conf: High — Corroboration: 1
independent artifact (archive crawl; not authenticated by the company) — Conflicts: None.
independence_note: **the two anchor targets — `http://google.stanford.edu` and `http://alpha.google.com/` —
appear in the page markup and were not reported in either upstream dossier**, both of which quote only the
visible text. See §E.2 and P1SRC04; this is an addition to record B07, not a repetition of it.

P1A03 Claim: The company's own filed description of its founding revenue mechanism is a licensing business,
and it dates the replacement of that mechanism to two quarters of 2000. — Date: 1999-Q1 → 2000-Q4 — Source
path: `sources/sec/0001193125-04-073639_0001193125-04-073639.txt`, "How We Generate Revenue" — Source date:
2004-04-29 — URL: sec.gov/Archives/edgar/data/0001288776/000119312504073639/0001193125-04-073639.txt —
Archived: as path — Tier: 1 — Class: FOUNDER CLAIM (retrospective self-description of mechanism, filed in a
document about the offering) — Passage: "Our original business model consisted of licensing our search
engine services to other web sites. In the first quarter of 2000, we introduced our first advertising
program." (32 words) — Conf: Medium — Corroboration: 1 lineage (LIN-REG; 9 printings, one instrument) —
Conflicts: None; §A.4 names the alternative reading.
independence_note: same lineage as B01; no independent carrier of the mechanism sequence exists in any
family.

---

## B

STATUS: WRITTEN 2026-09-26

### B.1 Pre-entity state: an invention owned by somebody else

The company's story in this corpus does not begin with the company. It begins with a patent application
filed **1998-01-09** — roughly eight months before the filing date the same company later gave for its own
incorporation — whose assignee is **Leland Stanford Junior University** and whose sole named inventor is
**Lawrence Page**. The grant record read this pass carries the title *"Method for node ranking in a linked
database"*, application US09/004,827, publication 2001-09-04. This leg is **kept and kept separate**: it
is pre-history, §Boundary.1, and the S-1's framing sentence ("The first version of the PageRank technology
was created while Larry and Sergey attended Stanford University, which owns a patent to PageRank") is the
company's own retrospective gloss on it, not an independent record of it.

### B.1a Two dated strings in the same held bytes that neither upstream dossier reported

Re-reading the grant record's own metadata block this pass, two lines matter to the boundary and to an
inherited UNKNOWN, and neither appears in `research/A_chronology_feasibility.md` or
`research/B1_filing_records.md` although both files cite this exact artifact:

1. **"Prior art date 1997-01-10."** The record prints a **1997** date ahead of the 1998-01-09 filing date,
   and immediately disclaims it: *"(The priority date is an assumption and is not a legal conclusion.
   Google has not performed a legal analysis and makes no representation as to the accuracy of the date
   listed.)"* So the corpus contains a **1997 leg that is neither a dated event nor absent** — it is a
   rendering of a priority claim by the host that publishes it. This is exactly the question B1 left open
   in its U-14 residual ("whether '2017' reflects a priority claim to 1997 — UNKNOWN"): the company's
   statement that *"The PageRank patent expires in 2017"* is one year short of the 2018-01-09 anticipated
   expiration also printed in these bytes, and a 1997 priority date is the obvious candidate explanation for
   both. **This volume does not adopt 1997 as the opening.** What it does is record the string, its
   disclaimer, and the arithmetic it would explain (P1CNF07), because a dossier that cites a document for
   two of its dates and ignores a third has not read it.
2. **"2017-12-05 Assigned to GOOGLE LLC reassignment GOOGLE LLC CHANGE OF NAME Assignors: GOOGLE INC."**
   The same held page therefore carries a **dated assignment event in which the registrant now called
   GOOGLE LLC is recorded as GOOGLE INC.'s successor by name change**, with the patent's anticipated
   expiration printed as 2018-01-09 — the registry's own arithmetic running from a 1998-01-09 filing. It is
   `(PB)` and far outside Stage 1, and it is about a patent's assignee chain rather than about an EDGAR
   registrant, so it **cannot** settle inherited U-2 (whether CIK 1288776 continues or CIK 1652044 is a new
   2015 entity), which stays **UNKNOWN**. What it does supply is the first on-disk, third-party-dated trace
   of the renaming question that both upstream dossiers named as their single largest open item while the
   line sat in a file they had already opened — and therefore a pointer for the merge: run the assignment
   route (USPTO PatentCenter / assignment search) before any later pass asserts anything about the
   2004-to-today registrant bridge.

**Two host-level disclaimers bind every date in this sub-section**: the same page warns that its priority
date, its legal status and its assignee list are each *assumptions that the host has not legally analysed*.
The **filing date 1998-01-09** is not weakened by that (it is the application's own printed filing date and
is independently recited in the executed licence, B04), and the **inventor and original-assignee fields**
are read here at the strength their disclaimer requires: High for inventor=Page, Medium-High for
assignee=Stanford (corroborated by the counter-signed licence).

### B.2 The single-inventor asymmetry, and the names the patent does credit

The earliest dated, registry-verified, non-company document in this dossier names **one** inventor. The
second founder appears in the patent specification not as an inventor but in an acknowledgment:

> "For support in reducing the present invention to practice, the inventor acknowledges Sergey Brin, Scott
> Hassan, Rajeev Motwani, Alan Steremberg, and Terry Winograd."

Three things follow, and one does not. **(i)** The sentence is dated by a filing, not by memory: it was in
the record from 1998-01-09 onward, and no later company narrative controls it. **(ii)** It names four
people beyond Brin who are absent from every founding account this corpus holds — an advisor (Winograd),
a Stanford faculty member (Motwani), and two engineers (Hassan, Steremberg) — which is the closest the
held record comes to a list of who participated. **(iii)** The word "inventor" is singular and the
acknowledged contribution is "support… in reducing the present invention to practice", which is patent
language for help in making it work. **(iv) What does NOT follow:** that Brin's role was minor, or that the
company was Page's alone. U.S. inventorship is a legal determination about a particular set of claims, not
a census of a project, and the company's own filed statement names both founders ("our founders Larry Page
and Sergey Brin", "Sergey and I founded Google"). **This asymmetry is therefore recorded as a fact about
one document's authorship and an UNKNOWN about the venture**, and §B.7 carries it that way. The trap named
in this project's own evidence notes — *roles recorded as founders* — runs in both directions, and a
patent's inventor list is not a licence to demote anyone.

### B.3 Company state in the window: what can be said, and how thinly

**Officers.** Page: CEO from "September 1998" to July 2001 and CFO from September 1998 to July 2002; Brin:
board member "since our inception in September 1998", "our President" from September 1998 to July 2001,
President of Technology from July 2001. Every one of those dates is anchored in the same sentence-cluster
to "our inception in September 1998" (records B22, B23), so they inherit that sentence's confidence
ceiling rather than raising it. Two consequences worth stating plainly: the same person held CEO and CFO
simultaneously through the whole founding stretch, and both founders held the offices *President* and
*CEO* before either was used to the title in later folklore — the corpus has no "CEO Larry Page in 1999"
statement that does not also carry "and CFO".

**Premises.** The only pre-HQ address in the corpus is in an executed agreement, not a memory: the 2003
licence recites Google's then "principal place of business at 2400 Bayshore Parkway, Mountain View, CA
94043" (record B35), while the S-1 four months later gives 1600 Amphitheatre Parkway. The dated-by-contract
address outranks the dated-by-prospectus one for 2003; nothing in the corpus gives an address for
1998-1999 at all.

**Employment and retention.** Two lines read this pass are the most useful anti-hagiography material in
LIN-REG for this section, because they are disclosures *against* interest: "All of our executive officers
and key employees are at-will employees, and we do not maintain any key-person life insurance policies",
and, in the risk factors, "The initial option grants to many of our senior management and key employees
are fully vested. Therefore, these employees may not have sufficient financial incentive to stay with us."
Both are 2004 statements about a 2004 state, so they are `(PB)` for the window — but they are the only
held evidence that the company's own account of its founding team contains a retention problem, and they
bear directly on §B.2's single-inventor finding without either side needing to be believed about 1998.

**Registrant genealogy.** California September 1998 → Delaware August 2003 → the 2004 registration under
CIK 1288776, whose printings disagree about the state of incorporation (inherited U-13: an 8-K cover
printing "California" beside an EDGAR header and a body both saying DE — the stale form field, not a
competing fact). The relationship between CIK 1288776 and today's GOOGL registrant CIK 1652044 remains
**UNKNOWN on held bytes** (inherited U-2); this volume uses "Google Inc." for the registrant and never
"Alphabet" except when naming today's ticker holder.

**Equity priced in cents.** The one equity price point inside the window is `B24`'s companion figure —
6,623,731 Class B options outstanding at 2004-03-31 at a weighted-average exercise price of **$0.29** —
plus the recital that the same plan was "adopted by our board of directors in September 1998". A board
cannot adopt a plan before it exists, so the plan is a second internal anchor on September 1998; and the
plan shares "were not exempt from registration or qualification under federal and state securities laws"
(record B25), which is the company's own admission that its earliest compensation was legally defective
(up to "$34 million plus statutory interest" of rescission exposure). That is the negative signal this
section is required to carry, and it survives from the same document as the founders' letter.

### B.4 Founder state, and what no held document supplies

No held document of any of the five families records either founder's education, degree status, or
departure from it. The strings "graduate" and "PhD" return **0 occurrences** in the 348,683 words of the
original S-1 (verified this pass; the probe's N-2 found the same for "graduate student"), so the standard
line "two Stanford PhD students founded Google" is **not attestable anywhere in this dossier**. What the
corpus does have is one sentence in LIN-REG — "The first version of the PageRank technology was created
while Larry and Sergey attended Stanford University" — which says they *attended*, and one patent whose
assignee is the university. The founders' prior and concurrent status as students is therefore recorded as
**UNKNOWN — no carrier in held bytes**, not as a settled fact and not as a refutation.

### B.5 The motive sentence, and the discipline around it

"Sergey and I founded Google because we believed we could provide a great service to the world—instantly
delivering relevant information on any topic." Classified FOUNDER CLAIM (retrospective), zero
corroboration, High confidence *that they said it in 2004* and Low as history (inherited U-4, record B08).
This volume adds one carrier-level observation about it: the letter in the original S-1 is **signed "Larry
Page Sergey Brin"** at the foot, so the dossier's attribution of its voice to Brin alone is a reading of
the "Sergey and I" idiom, not a fact about the document; the instrument records both founders as its
signatories. Confidence in the signature line: High (it is printed). This matters because the motive
sentence is the most-quoted line in the corpus, and a pass that attributes it to one founder while the
carrier carries two is manufacturing a difference the document does not make.

### B.6 Coda (§7: interpretive prose carries the same duty as tables)

The company in this window is documented as a **licensed-technology entity with defective early paper**:
it did not own its founding IP (Stanford did, and Google paid for it in equity and in a redacted royalty),
it could not register the shares it used to pay its first insiders, and its earliest public statement about
its own product was that the thing might work some of the time. **Mechanism:** the equity-for-licence
arrangement (record B30: a stock grant "equivalent to [***]% equity … after the round of investor
financing which resulted in a Eight Million Dollars ($8,000,000) post-money valuation"; B31: shares issued
to Stanford 1999-04-14, part transferred by Stanford to the two inventors 2000-04-17) is the only documented
route by which the founders' personal holdings appear in any dated instrument in this corpus — i.e. the
earliest *documentary* equity reaching them reaches them **through Stanford's grant, not through a
purchase**. **Alternative explanation not excluded:** the recital is Stanford-side drafting in a document
Google also signed, it says nothing about other issuances, and every share number in it is redacted, so
"the founders' first equity came from the licence" may be an artefact of which document survived.
**Confidence: Medium** for the recital, **UNKNOWN** for the inference about total early ownership.
**Firewall test:** a 1998-2001 company whose IP was licensed, whose equity paper was defective, and whose
first documented personal share grant came from a university transfer reads as a fragile start; none of it
predicts 2004.

### B.7 Load-bearing claim records for §B

P1B01 Claim: The founding technology's earliest dated public record credits one inventor and separately
acknowledges five named helpers, including the second founder. — Date: 1998-01-09 — Source path:
`sources/patents/us6285999.html` (specification text, "Detailed Description" preamble) — Source date:
2001-09-04 (grant); content filed 1998-01-09 — URL: patents.google.com/patent/US6285999B1/en — Archived:
as path — Tier: 1 (registry) — Class: FACT as to the document's contents; INFERENCE as to participation —
Passage: "For support in reducing the present invention to practice, the inventor acknowledges Sergey
Brin, Scott Hassan, Rajeev Motwani, Alan Steremberg, and Terry Winograd." (26 words) — Conf: High (that the
text says it) / Low (as any conclusion about who founded what) — Corroboration: 1 carrier —
Conflicts: None admissible; §B.2 states the boundary of the reading.
independence_note: outside LIN-REG and outside LIN-FOUNDER; a registry document that no company PR
controlled. Single carrier, so the record is capped at High-for-the-text / nothing-for-the-inference.

P1B02 Claim: The prior-art problem the inventor himself identified was that existing engines returned
hundreds of irrelevant results and were gameable by spam, and the acknowledged fix-approach was to rank by
extrinsic citation structure rather than by content. — Date: 1998-01-09 — Source path:
`sources/patents/us6285999.html`, "Background of the Invention" and "Summary" — Source date: 2001-09-04 —
URL: as P1B01 — Archived: as path — Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION (of the technical
problem, by its claimant) — Passage: "searches typically return hundreds of irrelevant or unwanted
documents which camouflage the few relevant ones" / "this measure of relevancy is vulnerable to
'spamming' techniques" / "Rather than determining relevance only from the intrinsic content of a document…
a method consistent with the invention determines importance from the extrinsic relationships between
documents" (three short quotations from one document) — Conf: High — Corroboration: 1 carrier —
Conflicts: None.
independence_note: not LIN-REG; the passage is a 1998-01-09 filing, and unlike the S-1 it was written
before the company had an incentive to describe its origin. Caveat per §6: this is a fact about an
invention and its author's diagnosis, not about a company's strategy.

P1B03 Claim: No held document attests that either founder held or abandoned a doctorate, and the popular
"two Stanford PhD students" framing is unsupported in this corpus. — Date: window 1996-2001 — Source path:
`sources/sec/0001193125-04-073639_0001193125-04-073639.txt` (full-text search: "graduate" 0, "PhD" 0 over
348,683 words), plus all `sources/periodicals/*` (founders' names 0 hits) — Source date: 2004-04-29 —
URL: — — Archived: as paths — Tier: 1 (the carrier searched) — Class: **UNKNOWN** — Passage:
NO_VERBATIM_PASSAGE_RECORDED — Conf: High (as to the absence in held bytes) — Corroboration: n/a —
Conflicts: None; this is a coverage statement, not a refutation.
independence_note: a search result, and it bounds only what this corpus holds. The route that could answer
it (Stanford University Archives / technical-report series) is listed in `## Untried`, item 3.

P1B04 Claim: The company disclosed in its own registration text that its first insider equity was legally
defective and that key people might leave. — Date: 2004-04-29 (disclosure), speaking to 1998-09 onward —
Source path: `sources/sec/0001193125-04-073639_0001193125-04-073639.txt`, "Risk Factors" and
"Employee Benefit Plans" — Source date: 2004-04-29 — URL: as B01 — Archived: as path — Tier: 1 —
Class: FACT (the disclosure) / FOUNDER CLAIM (the state it describes) — Passage: "Shares issued and options
granted under our 1998 Stock Plan and our 2003 Stock Plan were not exempt from registration or
qualification under federal and state securities laws"; "The initial option grants to many of our senior
management and key employees are fully vested. Therefore, these employees may not have sufficient
financial incentive to stay with us." — Conf: High that both are printed — Corroboration: 1 lineage
(22 occurrences of "rescission offer" in the same instrument) — Conflicts: None.
independence_note: same lineage as B25; recorded here because the retention-risk sentence is **new to this
pass** and is the second disinterested-against-interest disclosure in the same document. A company's own
filing is not independent of the company, even when it is candid.

P1B05 Claim: The held grant record also prints a 1997 prior-art date and a 2017/2018 expiry pair that no
upstream dossier reported, and its publisher disclaims the priority field as an assumption. — Date:
1997-01-10 (prior art date as rendered) / 1998-01-09 (filing) / 2018-01-09 (anticipated expiration) —
Source path: `sources/patents/us6285999.html`, metadata block — Source date: 2001-09-04 (grant) — URL:
patents.google.com/patent/US6285999B1/en — Archived: as path — Tier: 1 (registry copy, host-generated
field) — Class: FACT (the strings are printed on the held page) / **UNKNOWN** (whether a 1997 priority
claim exists as a legal matter) — Passage: "Prior art date 1997-01-10" / "(The priority date is an
assumption and is not a legal conclusion.)" / "Inventor Lawrence Page" — Conf: High that the page prints
them; Low for 1997 as history — Corroboration: 0 for the 1997 leg; 2 for the 1998-01-09 filing date
(registry plus the counter-signed licence recital) — Conflicts: **P1CNF07**; bears on inherited U-14.
independence_note: the registry is independent of both founder lineages, but a host's automated priority
field is a derived rendering and not a certified record, so this record carries printed strings and not a
date of the world. The same page's 2017-12-05 "Assigned to GOOGLE LLC ... CHANGE OF NAME Assignors:
GOOGLE INC." line is `(PB)` and does not settle the registrant bridge (inherited U-2 stays UNKNOWN).

## C

STATUS: WRITTEN 2026-09-26

### C.1 The problem, stated at the time by the person who worked on it

One document in this dossier states the original problem **while the company did not yet exist**, in the
genre where an author has an incentive to understate rather than dramatise the difficulty: the specification
of the patent filed 1998-01-09. Its "Background of the Invention" is not a mission statement, and that is
exactly why it is the load-bearing text for this section. Its diagnosis, in order:

1. **Scale had outrun the method.** *"Due to the developments in computer technology and its increase in
   popularity, large numbers of people have recently started to frequently search huge databases. For
   example, internet search engines are frequently used to search the entire world wide web."*
2. **A quantified anchor for what "huge" then meant.** *"Currently, a popular search engine might execute
   over 30 million searches per day of the indexable part of the web, which has a size in excess of 500
   Gigabytes."*
3. **The failure mode, named as a user experience rather than a market opportunity.** *"Large databases of
   documents such as the web contain many low quality documents. As a result, searches typically return
   hundreds of irrelevant or unwanted documents which camouflage the few relevant ones."*
4. **Why the obvious fixes fail.** Narrowing the search is itself lossy: *"each constraint introduced by
   the user increases the chances that the desired information will be inadvertently eliminated from the
   search results."*
5. **Why the incumbent ranking heuristics were not a solution.** Ranking by recency or term position
   *"provides search results that are better than with no ranking at all"* but the results *"still have
   relatively low quality"*, and — the sharpest line in the document — *"when searching the highly
   competitive web, this measure of relevancy is vulnerable to 'spamming' techniques that authors can use
   to artificially inflate their document's relevance in order to draw attention to it or its
   advertisements. For this reason search results often contain commercial appeals that should not be
   considered a match to the query."*
6. **And it credits the field, by name, with getting there first.** The background cites the *"Hyperlink
   Search Engine, developed by IDD Information Services, (http://rankdex.gari.com/)"*, which *"uses
   backlink information … to assist in identifying relevant web documents"*, and traces the underlying
   anchor-text idea to *"the World Wide Web Worm (Oliver A. McBryan, GENVL and WWWW: Tools for Taming the
   Web, First International Conference on the World Wide Web, CERN, Geneva, May 25-27, 1994)"*, before
   adding that *"citation counting is a simple method for determining the importance of a document by
   counting its number of citations, or backlinks."*

The proposed answer, in the same document's own words, is not "better search" in the abstract: it is a
change of **evidence** — *"Rather than determining relevance only from the intrinsic content of a document,
or from the anchor text of backlinks to the document, a method consistent with the invention determines
importance from the extrinsic relationships between documents. Intuitively, a document should be important
(regardless of its content) if it is highly cited by other documents. Not all citations, however, are
necessarily of equal significance. A citation from an important document is more important than a citation
from a relatively unimportant document."*

**Two readings this constrains immediately.** The problem as filed in 1998 is a *precision/recall* problem
inside a technical community, and the document claiming it names **prior implementations of the same
family of idea** — including a working commercial-ranked engine and a 1994 conference paper. Whatever the
company later became, the founding problem was not a discovery that nobody else had noticed links.

### C.2 The problem, restated in 2004 for people buying shares

LIN-REG states the same object as a corporate purpose: *"Our mission is to organize the world's information
and make it universally accessible and useful"*, three times in the original S-1, followed by *"We serve
three primary constituencies: Users … Advertisers … Web sites"*, and by the self-assessment *"We maintain
the world's largest online index of web sites and other content, and we make this information freely
available to anyone with an Internet connection."* Class: **FOUNDER CLAIM / corporate self-description**,
Tier 1 by document authority and zero by independence; "world's largest" is an unquantified superlative with
no measurement, no source and no comparison basis anywhere in the corpus, and no held document measures it.

The one *mechanism* claim in LIN-REG worth separating from the mission prose is a causal statement about
growth: *"We have found that offering a high-quality user experience leads to increased traffic and strong
word-of-mouth promotion."* It is the company asserting, in 2004, that quality caused traffic caused
word-of-mouth. No held document tests any link in that chain; §L (later pass) inherits the problem, and
this section records only that the chain is **asserted, not evidenced**.

### C.3 The scale number and where it may be used

The patent's *"over 30 million searches per day"* and *"in excess of 500 Gigabytes"* are the only
in-window quantities in the whole dossier that describe the **problem space** rather than the company, and
they are inside a registry document independent of both founders' lineages. Three basis labels travel with
them, and none may be dropped: (i) they describe **"a popular search engine"**, unnamed — no held document
identifies which, so the figure cannot be attributed to Google, to AltaVista, to Yahoo or to GoTo; (ii) the
metric is **searches executed**, not users, sessions or queries per capita; (iii) the web-size figure is
the **"indexable part"**, not the whole web, and "in excess of" is a floor not an estimate. Used as an
industry denominator in §H or §I, P1QTN02 and P1QTN03 are strong Tier-1 in-window anchors; used as a Google
number they are a category error, and this volume says so in the register's `notes` cell so a later merge
cannot lose the warning.

### C.4 What is unrecoverable about the problem, and why that is the finding

Nothing in the corpus records the problem **as it was experienced before it was written down**. There is no
lab notebook, no Stanford technical report, no email, no grant proposal, no prototype spec, no rejected
alternative. Consequently the dossier cannot answer the three questions §10's research-debt triggers name
for a founding period: **(a)** whether the ranking idea or the web-crawling scale was the harder problem,
**(b)** whether any other approach (anchor-text matching, citation counting, directory browsing) was tried
and abandoned — the patent's background mentions those three as *others'* methods, which is not evidence
that anyone at Google tried them, and **(c)** whether the motivation was technical, commercial or academic;
the 1998 document is silent on commerce, and the 2004 letter is silent on technique, so the two carriers
answer different questions and cannot be merged. **All three stay UNKNOWN**, and the reason they stay
UNKNOWN is a preservation fact (nobody kept an unpublished 1998 lab record), not a search failure — which
is §2's record-selection null and the reason it appears in §A as well as here.

### C.5 Knowability for this stage (§7 format)

- **KNOWABLE:** the technical problem as its author framed it, at a fixed 1998-01-09 date, with named prior
  art and a quantified scale anchor; the existence of a ranking-quality market complaint in 2000 print from
  an unaffiliated magazine (§E.3); the company's own 2004 statement of purpose and constituency list.
- **NOT KNOWABLE:** which problem the company *worked on first*; whether the diagnosis was Page's,
  Brin's or the group's; whether the "spamming" concern or the "low quality" concern drove the design;
  whether any commercial problem existed before Q1 1999; and the founders' education status (§B.4).
- **UNKNOWN:** the answer to every one of (a)-(c) in §C.4, plus any 1998-2001 count of users, queries,
  index size or traffic, and the identity of the "popular search engine" behind the 30-million figure.

### C.6 Coda (§7: prose carries the table's duty)

**Mechanism, as far as evidence reaches:** the founding problem is documented as a *ranking-evidence*
change — score documents by the scores of the documents pointing at them — proposed against a background
in which three competing evidence sources (content, anchor text, raw citation count) were already
described and found wanting. **Alternative explanation not excluded:** a patent specification states the
problem in the shape that makes the claims novel, so §C.1's ordering of failures may be drafting
architecture rather than a 1998 engineer's experience; the acknowledgment sentence (§B.2) is the only hint
of a real lab process, and it names support, not deliberation. **Confidence:** High for what the document
says; **Medium** for reading it as the company's problem, since at 1998-01-09 there was no company.
**Firewall test:** nothing in §C requires the ranking idea to have been good. A reader in 1998 could
legitimely have concluded that the field had already tried link-based ranking twice, in 1994 and at
RankDex, and that a third attempt was unremarkable — and that reading is compatible with every held line.

### C.7 Load-bearing claim records for §C

P1C01 Claim: The problem the founding technology addressed was stated, with numbers and named prior art, in
a document filed before the company existed. — Date: 1998-01-09 — Source path:
`sources/patents/us6285999.html`, "Background of the Invention" + "Summary" — Source date: 2001-09-04
(grant); content filed 1998-01-09 — URL: patents.google.com/patent/US6285999B1/en — Archived: as path —
Tier: 1 — Class: CONTEMPORANEOUS OBSERVATION (technical state of the art, by a participant) — Passage:
"searches typically return hundreds of irrelevant or unwanted documents which camouflage the few relevant
ones" (14 words) — Conf: High — Corroboration: 1 carrier — Conflicts: None.
independence_note: outside LIN-REG and LIN-FOUNDER. Caveat: a patent background is advocacy for novelty, so
the *ordering* of prior-art failures is capped at Medium (§C.6).

P1C02 Claim: The scale of the problem as known to the inventor in January 1998 was quantified as tens of
millions of searches per day against an indexable web measured in hundreds of gigabytes, and the search
engine so described was not Google. — Date: 1998-01 — Source path: as P1C01 — Source date: 2001-09-04 —
URL: as P1C01 — Archived: as path — Tier: 1 — Class: FACT as to what the filing prints; the referent of
"a popular search engine" is **UNKNOWN** — Passage: "Currently, a popular search engine might execute over
30 million searches per day of the indexable part of the web, which has a size in excess of 500 Gigabytes."
(31 words) — Conf: High (printed) / Low (as an industry measurement — one document, no method, no source
given) — Corroboration: 0 — Conflicts: None.
independence_note: registry custody; but the figure is unsourced inside its own carrier, so it is one
unsourced assertion in a Tier-1 wrapper and is carried as an **ESTIMATE** in the register, never as an
observed statistic.

P1C03 Claim: The company's filed statement of purpose, and its claim to hold the largest index, are
self-description with no measurement anywhere in the corpus behind them. — Date: 2004-04-29 (statement),
about 1998-2004 — Source path: `sources/sec/0001193125-04-073639_0001193125-04-073639.txt` — Source date:
2004-04-29 — URL: as B01 — Archived: as path — Tier: 1 — Class: FOUNDER CLAIM / corporate self-claim —
Passage: "Our mission is to organize the world's information and make it universally accessible and
useful." / "We maintain the world's largest online index of web sites and other content" — Conf: Medium
that the sentences are the company's settled self-description (3 occurrences of the mission clause in the
first printing); **Low** for "world's largest" as a measurable claim — Corroboration: 1 lineage —
Conflicts: None; no independent index measurement exists in any family to compare with.
independence_note: same lineage as B01. An unquantified superlative printed in a prospectus is a
self-claim about others' holdings as much as about its own, and the corpus holds no other index count for
any year in the stage.

P1C04 Claim: The prior-art link-ranking systems the founding patent names are dated, attributed and, in one
case, commercially live at the filing date. — Date: 1994 (Web Worm paper) and pre-1998-01-09 (RankDex) —
Source path: `sources/patents/us6285999.html` — Source date: 2001-09-04 — URL: as P1C01 — Archived: as
path — Tier: 1 — Class: FACT (the citations are printed in the filing) — Passage: "The idea of associating
anchor text with the page the text points to was first implemented in the World Wide Web Worm (Oliver A.
McBryan, GENVL and WWWW: Tools for Taming the Web, First International Conference on the World Wide Web,
CERN, Geneva, May 25-27, 1994)." (44 words; the parenthetical citation is the source's own) — Conf: Medium
— Corroboration: 0 (the cited 1994 paper is **not held**; only its citation is) — Conflicts: None.
independence_note: one carrier's reference list. Recorded because it is the only dated competitor-state
evidence inside the opening of the window, and because §I must not write "no one had ranked by links
before Google" — the corpus's own priority document would refute it.

---

## D

STATUS: WRITTEN 2026-09-26

### D.1 The candidate "first experiments" in the record, ranked by what carries them

| Candidate experiment | Dated by | Carrier and class | Verdict for §D |
|---|---|---|---|
| The 1996-docket invention ("Improved text searching in hypertext systems") | **undated**; year inferred from the docket string | licence recital, `B05`; INFERENCE | **Admitted as pre-experiment work**, not as an experiment: no held record shows anything being tried, only a docket and a filing. |
| A publicly reachable search service running on a Stanford-hosted machine | **1998-11-11 18:45:51**, HTTP 200 | Wayback CDX + 212-byte page; CONTEMPORANEOUS OBSERVATION | **ADOPTED as the stage's first experiment.** It is the only candidate with an external, non-company timestamp, and it is a *service responding to the public* rather than a claim about an idea. |
| A second, "more up to date" service on a different host, on the same day | same capture | same page's second href, `http://alpha.google.com/` | **ADOPTED as part of the same experiment** (§D.2). A single page advertising an alternative to itself is documented A/B behaviour, not a narrative flourish. |
| The first paid licence of the technology | **effective 1998-12-01** | executed bilateral agreement, `B06`/`B29`; FACT | **ADOPTED as the first commercial transaction**, not as the first experiment: the counterparty here is the university that owned the IP, i.e. the company paying for the right to use the invention. |
| The first licensed product sale | **Q1 1999** | S-1 single sentence, `B03`; FOUNDER CLAIM, quarter granularity | **ADOPTED as the validation marker (§Boundary.2, rejected loser 2), with no customer named.** |
| A beta-evaluation programme with an institutional customer | 2004-11 `(PB)` | Google-authored form contract held by a third-party archive | **Excluded from Stage 1 as post-boundary**, retained here because §D.4 needs it: it is the only held document showing *how* this company tested a product with a customer, and it is 3-6 years after the window it would illuminate. |

### D.2 The experiment as the archived page reconstructs it

The entire product evidence for the founding date is **four lines of HTML**, and it is more informative than
its word count suggests:

> `<h1>Welcome to Google</h1>`
> `<a href="http://google.stanford.edu">Google Search Engine Prototype</a>`
> `<a href="http://alpha.google.com/">Might-work-some-of-the-time-prototype that is much more up to date.</a>`

Four observations, each bounded by the bytes. **(i)** The page is a **pointer page**, not a search page: it
contains no form, no input element and no search box in any of its 212 bytes, so what was captured at
18:45:51 on 1998-11-11 is an index to a service, not the service. Any statement of the form "the Google
homepage in November 1998 looked like X" is unsupported by this artifact, and this volume does not make
it. **(ii)** The prototype is **located at Stanford** by the page's own href
(`google.stanford.edu`) — contemporaneous, non-narrative corroboration of the licence recital's
"predecessor in interest" framing and of the S-1's "created while Larry and Sergey attended Stanford",
from a third source that neither of them controls. **(iii)** The "much more up to date" alternative is at
`alpha.google.com`, i.e. **on Google's own emerging domain rather than the university's**, and the register
records the *name* `alpha` as a fact of the markup, not as a claim about what later became a product tier.
**(iv)** The self-labelling is doubled and honest: one link says "Prototype", the other says
"Might-work-some-of-the-time". Whatever the company later claimed about quality, its earliest surviving
public statement about its own product was a **reliability caveat**. That is §D's negative signal, it is
independent of every founder narrative, and it is carried in `failures.csv` (P1FAI01) rather than being
narrated away.

**What the page cannot support:** no date of first availability, no user count, no index size, no
hardware/host description, no funding statement, no name of an operator, and no assertion that a company
rather than two students and a university ran it. The gap between "a public hostname answered on
1998-11-11" and "Google launched" is not closed by anything in this corpus.

### D.3 The second experiment: testing how to get paid

Three dated mechanism experiments sit inside the window and all three come from one paragraph of LIN-REG,
so they are one source describing three states:

1. **Wholesale licensing** — *"Our original business model consisted of licensing our search engine
   services to other web sites."* Started, on the same document's earlier sentence, in Q1 1999 (record
   B03).
2. **Direct-sale advertising, priced per display** — *"In the first quarter of 2000, we introduced our
   first advertising program. Through our direct sales force we offered advertisers the ability to place
   text-based ads on our web sites targeted to our users' search queries under a program called Premium
   Sponsorships. Advertisers paid us based on the number of times their ads were displayed on users'
   search results pages, and we recognized revenue at the time these ads appeared."*
3. **Self-service advertising** — *"In the fourth quarter of 2000, we launched Google AdWords, an online
   self-service program that enables advertisers to place targeted text-based ads on our web sites."*

Two structural readings belong to §D rather than §L. **First, the pricing basis is disclosed and it is not
the later one:** the first ad mechanism was paid **per impression**, and the corpus's only statement about
performance-based pricing comes in the next clause of the same paragraph about AdWords customers
*"originally"* paying on display. A pay-per-click mechanism is **not evidenced in this window** by any
held document, so any later-stage narrative that Google found performance pricing at the start is
unsupported here. **Second, the experimental sequence has a visible logic the filings do not claim:**
wholesale licensing scaled by partner sites and yielded a small revenue share; direct-sale advertising
required a sales force; self-service removed the sales constraint. **Mechanism, asserted as a reading and
not as a record:** the 2001 profitability claim (B03) follows the self-service launch by about a year.
**Alternative explanation not excluded, and it is the strong one:** FY2001's $86,426 thousand of net
revenues is dominated by whatever mix the filing never itemises, and "following" is a conjunction, not a
cause — the corpus contains no revenue split by mechanism for any year.

### D.4 What the first experiment did not demonstrate

It did not demonstrate demand: no query log, no count, no named licensee, no price for the licence sales.
It did not demonstrate a company: the only dated legal act near it is a **payment obligation to a
university** (1998-12-01) whose cash amount is redacted (`[***]` "license issue royalty … upon signing"),
so even the first contract records that money moved and not how much. It did not demonstrate a product
category: the 2000-07 magazine (§E.3) ranks Google **fourth**, which is contemporaneous third-party
evidence that the service worked and equally evidence that it was not the market leader while the
mechanism experiments were running. And it did not demonstrate a repeatable acquisition channel — the only
channel statement in the corpus ("strong word-of-mouth promotion", §C.2) is a 2004 assertion with no
measurement and no experiment attached.

### D.5 Coda and firewall (§7)

**Mechanism:** the documented sequence is *invent → publish on a university host → put a second,
different host next to it → licence the technology to pay for the right to use it → sell the results of it
wholesale → sell advertising against it directly → sell advertising against it self-service*. Every arrow
is dated by a carrier and named in the register; none of them is an inference about why. **Alternative
explanation for the two-host page, not excluded:** the page may simply be a student's index of two
machines he had access to, and "Might-work-some-of-the-time" may be a joke, a disclaimer, or an accurate
description of an under-provisioned box. Reading it as a deliberate A/B test would import a product
discipline the corpus does not otherwise show until `(PB)` 2004, which is why P1TML04 says *two services were
reachable* and not *the company ran an experiment*. **Firewall test:** a reader who knew nothing of 2004
would look at §D and see a prototype that admitted it might not work, hosted on someone else's machines,
whose first contractual act was to pay a university for patent rights, and whose fourth-ranked position in
a 2000 magazine round-up preceded its first profitable year by one year. That reader would not be wrong.

### D.6 Load-bearing claim records for §D

P1D01 Claim: The earliest publicly archived Google page advertised two different search services on two
different hosts and labelled its own product unfinished. — Date: 1998-11-11 18:45:51 — Source path:
`sources/wayback/google_19981111_raw.html` (212 B) — Source date: 1998-11-11 — URL:
web.archive.org/web/19981111184551id_/http://google.com/ — Archived: as path; sidecar
`.sidecar.json` records the 14-digit capture timestamp and the source CDX file — Tier: 1 (archived company
page) — Class: CONTEMPORANEOUS OBSERVATION — Passage: "Google Search Engine Prototype …
Might-work-some-of-the-time-prototype that is much more up to date." (10 words of visible text, plus two
hrefs) — Conf: High — Corroboration: 1 independent artifact (archive crawl) — Conflicts: None.
independence_note: fully independent of LIN-REG. It is a *terminus ante quem* for a public service; it says
nothing about founding, motive, or who operated the hosts. **The hrefs are the new content this pass adds
to record B07**, which quoted only the visible text.

P1D02 Claim: The service described as current was on the company's own emerging hostname while the
prototype was on a Stanford hostname. — Date: 1998-11-11 — Source path: as P1D01 — Source date: 1998-11-11 —
URL: as P1D01 — Archived: as path — Tier: 1 — Class: FACT (the markup prints) / INFERENCE (that the two
hosts were differently provisioned or differently managed) — Passage: `href="http://google.stanford.edu"`
and `href="http://alpha.google.com/"` — Conf: High as to the strings; **Low** as to any interpretation —
Corroboration: 1 for the markup; the `google.stanford.edu` leg is indirectly supported by the licence's
Stanford assignment recital (`B05`) — Conflicts: None.
independence_note: no second carrier of `alpha.google.com` exists in the corpus. `research/A_chronology_
feasibility.md` attempted a CDX query for `google.stanford.edu` and received HTTP 503
(`wayback/cdx_stanford.json`, kept as a negative artifact), so the Stanford host's own capture history is
**UNANSWERED, not absent**.

P1D03 Claim: The company dated its first licensed product to Q1 1999 and its first advertising mechanism to
Q1 2000, and named its original model as wholesale licensing. — Date: 1999-Q1; 2000-Q1; 2000-Q4 — Source
path: `sources/sec/0001193125-04-073639_0001193125-04-073639.txt`, "How We Generate Revenue" — Source date:
2004-04-29 — URL: as B01 — Archived: as path — Tier: 1 — Class: FOUNDER CLAIM (retrospective mechanism
history) — Passage: "In the fourth quarter of 2000, we launched Google AdWords, an online self-service
program that enables advertisers to place targeted text-based ads on our web sites." (26 words) —
Conf: Medium — Corroboration: 1 lineage; 0 independent — Conflicts: None, but see P1D04 for the pricing
basis this record bounds.
independence_note: same lineage as B03. Quarter granularity cannot carry a day, and no held contract, price
list or press notice names a first licensee or a first advertiser.

P1D04 Claim: The first advertising mechanism was paid for by impressions, not by clicks, and the corpus
contains no pay-per-click evidence inside the stage. — Date: 2000-Q1 → 2000-Q4 — Source path: as P1D03 —
Source date: 2004-04-29 — URL: as P1D03 — Archived: as path — Tier: 1 — Class: FACT (the sentence prints)
+ a bounded negative — Passage: "Advertisers paid us based on the number of times their ads were displayed
on users' search results pages, and we recognized revenue at the time these ads appeared." (27 words) —
Conf: Medium-High — Corroboration: 1 lineage — Conflicts: None.
independence_note: a *limit* on the record rather than a claim about the world: it establishes that the
held text prices by display, and that Overture/GoTo's per-click channel is separately evidenced in the
periodical family (`research/A2_periodical_settlement.md`: a 2000-07 magazine reporting "I went to
GOTO.COM to compare online prices"), which is a competitor's mechanism and not Google's.

## E

STATUS: WRITTEN 2026-09-26

### E.1 What "the product" means in this corpus, and why the answer changes four times

A reconstruction of Google's product across 1998-2001 has to hold four different things apart, because the
holders of the evidence never use one word for them:

| Layer | Held name(s) | Earliest carrier in this corpus | What the carrier actually documents |
|---|---|---|---|
| The ranking method | the invention, "node ranking in a linked database"; "PageRank" | patent US 6,285,999, filed 1998-01-09 | **claim 1:** "assigning a score to each of the linked documents based on scores of the one or more linking documents" — a scoring algorithm, no interface, no index, no latency |
| The public search service | "Google Search Engine Prototype" / the site at google.com | Wayback capture 1998-11-11 | a **212-byte pointer page with no search form**; the service itself is not in the bytes |
| The licensed product sold to other sites | **Google WebSearch** | S-1, "began licensing our WebSearch product in the first quarter of 1999" | a licence line, priced nowhere in the corpus; the word appears 6 times in the first printing |
| The advertising mechanisms | Premium Sponsorships (Q1 2000) → **Google AdWords** (Q4 2000) → **Google AdSense** (first printing 2004) | S-1 "How We Generate Revenue" | the sequence and the **pricing basis**, which the mechanism history in records B36-B41 does not carry |
| The enterprise appliance | **Google Search Appliance** ("GSA"), "a complete software and hardware solution" | S-1 (2004) `(PB)`; an executed customer contract for pre-release versions 4.2 and 4.4 (2004-11) `(PB)` | a physical product line, and — uniquely — a **named third party evaluating it under a 60-day trial** |

Two reconstruction rules follow and are applied in every row below. **(i)** The patent is not the product:
claim 1 describes a scoring step over "a plurality of linked documents", and no held document from inside
the window says the public site ran that claim, at that scope, on a given index size. The gap between
*patented method* and *shipped search engine* is where every "Google's algorithm from day one" sentence in
the popular record lives, and this corpus does not close it. **(ii)** The 2004 filings describe the
**2004** product with 1998-2001 dates attached; anything read out of them about the window is
`RETROSPECTIVE SOURCE` (§6) and inherits LIN-REG's single-lineage ceiling.

### E.2 The one primary description of the product while it was young — and its two hostnames

The 1998-11-11 page yields the only **contemporaneous** product description in the corpus, and the useful
part is markup that no upstream dossier transcribed (§D.2). Repeating it as a table, because it is the
entire evidentiary base for "what Google was in 1998":

| Element | Value as held | Confidence |
|---|---|---|
| Heading | "Welcome to Google" | High (212 bytes, one capture) |
| First link text | "Google Search Engine Prototype" | High |
| First link target | `http://google.stanford.edu` | High (string present in the bytes) |
| Second link text | "Might-work-some-of-the-time-prototype that is much more up to date." | High |
| Second link target | `http://alpha.google.com/` | High (string present) |
| Search form / input element | **absent from the bytes** | High as to this capture; **UNKNOWN** as to the service |
| Date of first availability of any of it | **UNKNOWN** | — |
| Query volume, index size, response time, result count in 1998 | **UNKNOWN** — no carrier in any family | — |

The `google.stanford.edu` target is the load-bearing string: it is the only in-window artifact that places
the running service **on university infrastructure**, and it does so without anyone's later account. The
`alpha.google.com` target is recorded and **not interpreted** (§D.5).

### E.3 What an outsider could see, and how much that is worth

One held periodical names Google inside the window: *Yahoo Internet Life*, July 2000, whose "Search the Web,
Part II" round-up lists it fourth of the engines reviewed:

> `4, GOOGLE` / `[google.com]` / *"Our new favorite for general searches. Unlike other search engines,
> Google uses proprietary technology to ensure that the first hits you get for your search are the best."*
> (held lines 11027-11036; the issue also carries `GOOGLE [google.com]` at l.2079 and `Searches conducted at
> Google.com` at l.5196 — 5 lines mention it in 16,052)

**What this evidences:** that by 2000-07 an unaffiliated consumer magazine (a) reached google.com, (b)
judged its top-of-results quality better than its competitors', and (c) attributed the difference to
undisclosed "proprietary technology" — an independent third party observing *the same ranking claim* the
patent filed in 1998. **What it does not evidence:** the founding, the founders, the company's age, any
traffic figure, and any paid product: the same issue prices and describes a **competitor's** commercial
channel (`GOTO.COM [goto.com]`, l.2927), and "AdWords" appears in **no** held periodical byte. This is the
corpus's only independent in-window observation of the product, it is **Tier-3 press** under §5, and it was
fetched over **UNVERIFIED TLS** (`research/A2_periodical_settlement.md`), which caps it at Medium
throughout. Its companion finding is the null: across every held periodical byte the founders' names appear
**zero** times, so the *company* is uncorroborated by print even where the *product* is.

### E.4 The appliance contract: what a customer was actually given, and what it was asked to do

A Google-drafted **Beta Evaluation Agreement** for "Google Search Appliance™ Pre-release Version 4.2 and
4.4", held and published by the U.S. government's own reading room, is the single most concrete product
document in `sources/` — and it is **outside the stage** (`(PB)`, dated November 2004, the day-of-month
OCR-degraded to `f19"j`). It is summarised here because it is the only held text that defines a Google
product down to its return policy, and because it shows the **beta mechanism** §D.1 needs in order not to
guess:

- **What is licensed:** "certain proprietary computer programs in binary executable form only … and the
  proprietary computer hardware in which the Software is installed"; Software + Hardware = "Appliance";
  Appliance + Documentation = "Product", a definition that *"expressly excludes any search results produced
  by the Appliance."*
- **What the customer may do with it:** *"limited to solely testing the Appliance internally in a
  non-production environment for the sole purpose of providing Google with feedback on the Product's
  usability and functionality"*, on servers "owned by Evaluator or operated on its behalf" — so the
  deliverable flowing **from** the customer **to** Google is feedback, not money.
- **The term and the exit:** a "sixty (60) day period (the 'Evaluation Period'), commencing on the date of
  shipment"; return within ten business days of termination; if the Appliance is not returned within thirty
  days of expiry, "Google may invoice You Google's then current fee for the Appliance"; the customer may
  quit "at any time"; Google may end the whole Beta Program when it "determines in its sole discretion that
  it is impractical to continuing offering the Beta Program in light of the feedback received".
- **What is deliberately unreadable:** the licence is *"further limited to using the Appliance to index no
  more [than] … documents"* — the cap number is destroyed in OCR (`no more whan foouments` in the held
  text), so the trial's size ceiling is **UNKNOWN with a stated cause**, not unsearched.

Two independent-document consequences: the registrant's legal name and Mountain View address print in a
counterparty's archive exactly as filed, and the enterprise product line the S-1 describes in prose exists
in the world as a shipped box with a 60-day clock on it. Neither supports a founding claim; both are worth
having as the (PB) far edge of Stage 1's product picture.

### E.5 What cannot be reconstructed about the product, and the route

No UI of any year survives (the only held page is a pointer page); no index size for any Google date; no
result-quality measurement; no feature chronology 1998-2001; no price for WebSearch or for the first
AdWords listings; no count of anything. The two routes that could still move this are the **wayback ladder
for 1999-2001** (`research/A_chronology_feasibility.md` Untried item 6 — later captures of google.com and
the unanswered `www`/`google.stanford.edu` CDX queries) and the **seven further in-window Yahoo Internet
Life issues** enumerated but not fetched (`research/A2_periodical_settlement.md` Untried item 3). Neither
was run by this pass, and neither is a null: see `## Untried`.

### E.6 Coda (§7)

**Mechanism:** the documented product history of this window is a *method* (1998-01-09 registry), a
*publicly reachable service on someone else's host* (1998-11-11 bytes), a *licensed product line* (Q1 1999,
issuer's word), and *two successive advertising mechanisms* (2000-01, 2000-10) — with the appliance and
the self-serve network both arriving after the boundary. **Alternative explanation not excluded:** the
2004 filings may have retro-fitted names onto things that had none — "WebSearch" as a product label and
"Premium Sponsorships" as a program name are attested only in 2004 prose, and no 1999-2001 document uses
either string anywhere in the corpus. **Confidence:** High for the three artifacts, Medium for the 2004
sequence, **UNKNOWN** for everything about how the thing actually behaved. **Firewall test:** an investor
reading only §E in mid-2001 could see a search site a magazine liked, an enterprise product that did not
yet exist, a licensed engine with no published price, and an advertising program that had changed its
pricing basis once. Nothing in that list is a bet on a category winner.

### E.7 Load-bearing claim records for §E

P1E01 Claim: The founding patent's operative claim is a scoring method over linked documents, and it makes
no statement about a search engine, an index, or a user-facing product. — Date: 1998-01-09 (filed) /
2001-09-04 (granted) — Source path: `sources/patents/us6285999.html`, claim 1 — Source date: 2001-09-04 —
URL: patents.google.com/patent/US6285999B1/en — Archived: as path — Tier: 1 — Class: FACT (registry text) —
Passage: "assigning a score to each of the linked documents based on scores of the one or more linking
documents" (15 words) — Conf: High — Corroboration: 1 carrier — Conflicts: None; the record bounds rather
than supports any product claim.
independence_note: outside LIN-REG and LIN-FOUNDER. §6 caveat: a claim's scope is a legal fact about an
invention, not evidence about a shipped product.

P1E02 Claim: An unaffiliated magazine ranked Google fourth among reviewed engines in July 2000 and
attributed its advantage to unstated proprietary ranking technology. — Date: 2000-07 — Source path:
`sources/periodicals/yahoo-internet-life-magazine-july-2000_djvu.txt` l.11026-11036 — Source date:
2000-07-01 (item metadata) — URL: archive.org item `yahoo-internet-life-magazine-july-2000` — Archived: as
path, 361,043 B — Tier: 3 — Class: CONTEMPORARY OBSERVATION — Passage: "Unlike other search engines, Google
uses proprietary technology to ensure that the first hits you get for your search are the best." (23 words;
OCR joins "othersearch" in the held bytes) — Conf: **Medium — capped by UNVERIFIED TLS** — Corroboration:
1 independent carrier — Conflicts: None.
independence_note: the corpus's only independent in-window product observation. Note the OCR line-break
artefact and that A2's held-line range (11027-11033) stops mid-sentence; the quotation above is re-grepped
from the bytes this pass. Consumer magazines review products, not registrants: this corroborates the
service, never the founding.

P1E03 Claim: The only held document defining a Google product down to usage limits and return terms is a
customer-facing beta contract preserved by the customer, and it is post-boundary. — Date: 2004-11 (day
UNKNOWN; `f19"j` in the OCR) — Source path: `sources/ia/cia_1487901_djvu.txt` (16,235 B held) — Source
date: 2004-11-19 (IA item date; may be the CREST release date, not the execution date) — URL:
archive.org item `cia-readingroom-document-0001487901` — Archived: as path + `.sidecar.json` — Tier: 1 —
Class: FACT (executed bilateral form contract; Google-authored form, third-party custody) — Passage: "The
term of the license granted herein shall be for a sixty (60) day period (the 'Evaluation Period'),
commencing on the date of shipment of the Appliance" (24 words) — Conf: High on the clause; Low on the day
— Corroboration: 2 documents, **1 author** (the S-1's GSA description is the same registrant's prose, so it
corroborates the product line's existence and not the contract's terms) — Conflicts: None.
independence_note: not LIN-REG, but not independent of Google's drafting either; its independence is
custodial (the counterparty published it). `(PB)` for every Stage-1 use, and it must not be used to
backdate the beta mechanism into 1998-2001.

P1E04 Claim: The trial's document-indexing ceiling is illegible in the held bytes, so the size limit of the
only Google product contract on disk is unknowable from this corpus. — Date: 2004-11 — Source path: as
P1E03 — Source date: 2004-11 — URL: as P1E03 — Archived: as path — Tier: 1 — Class: **UNKNOWN** —
Passage: "This license is further limited to using the Appliance to index no more [OCR: whan foouments]" —
Conf: High that the string is corrupt; **UNKNOWN** for the value — Corroboration: n/a — Conflicts: None.
independence_note: an OCR degradation, not an absence of record. The route to the number is the CREST page
image for the same item, which no pass has opened; listed in `## Untried`.

---

## F

STATUS: WRITTEN 2026-09-26

### F.1 Who the customer is, in the issuer's own taxonomy — and the trap in it

The S-1 opens by naming **three constituencies**: *"We serve three primary constituencies: Users …
Advertisers … Web sites"*. For a marketplace-shaped business the §7 adaptation rule requires the paying
side and the supplying side to be separated before any "customer" number is used, and Google's own framing
blurs them deliberately: **users pay nothing and supply attention; web sites in the Google Network pay
nothing and supply inventory; advertisers pay**. Meanwhile the *first* customers of the stage — the Q1 1999
WebSearch licensees — were neither users nor advertisers but **other websites buying a search engine**, a
category the same document later folds into the sentence quoted at §D.3. The dataset therefore carries
three distinct customer populations with three different evidence bases, and never sums them:

| Customer type | In-window evidence | Named? | Quantified? |
|---|---|---|---|
| Licensees of WebSearch (B2B search buyers) | one sentence, 2004 prose | **no** | no price, no count, no renewal |
| Advertisers (Premium Sponsorships → AdWords) | mechanism dates and **pricing basis**, 2004 prose | no individual named | no count; per-impression basis stated |
| Google Network member sites (inventory suppliers, paid a share) | 2004 prose, `(PB)` series | no | traffic-acquisition-cost series exists **only from 2002** (record B41) |
| Users (non-paying) | 2000-07 magazine; 2004 prose | n/a | **no count anywhere in the window** |
| Institutional trial customers | 2004 contract `(PB)` | yes — the customer is the counterparty of a published form agreement | 60-day term; no fee unless the box is not returned |

### F.2 The first customer question, answered the only honest way

§10's trigger list names "the first customer is unknown" as a research-debt condition, so it is stated
rather than papered over: **the first customer of Google is UNKNOWN in this corpus at every level of
granularity — name, industry, contract date and price.** What the record actually contains is the two
earliest *commercial* documents of any kind held for this entity, and neither is a customer relationship:

1. **1998-12-01** — the Original Agreement between Stanford and "Google Inc., a California corporation",
   under which Google obtained the right to use the patented technology. Google here is the **licensee and
   payer** (record B06/B29; the cash component is redacted `[***]`).
2. **1999-04-14** — Google issues shares **to Stanford** as part of the licence consideration, "equivalent
   to [***]% equity of issued shares after the round of investor financing which resulted in a Eight
   Million Dollars ($8,000,000) post-money valuation" (records B30-B31). Stanford is here a **recipient of
   equity**, not a purchaser of a product.

The inference this blocks is worth naming because it is the popular story: the earliest documented external
party to receive value from Google is a university it was **paying**, and the earliest documented equity
event is compensation **for technology**, not a sale of stock to a customer or a venture fund. Any
"Google's first customer was …" sentence in this dossier is an unattested gloss on a single line reading
"we began licensing our WebSearch product in the first quarter of 1999".

### F.3 The one audited customer statement, and the year it does not cover

Inside the audited band the filing makes a **negative** disclosure about customers: *"No customer accounted
for greater than 10% of net revenues in 2001, 2002 and 2003 or in the three months ended March 31, 2003 and
2004."* This pass reached it in the notes to the consolidated financial statements, which makes it the
only customer-side statement in the corpus inside **Ernst & Young's attested band** (records B15). Three
things must travel with it:
- **It is a bound, not a count.** "<10%" against FY2001 net revenues of $86,426 thousand caps any single
  customer at roughly $8.6 million — a **DERIVED** figure, printed nowhere, and computed on a revenue base
  whose *label* changed mid-lineage (inherited U-9); the arithmetic is recorded in P1QTN05 and labelled.
- **It says nothing about 1999 or 2000**, the two years that carry the window's only revenue numbers. The
  customer structure of the first two revenue years is **UNKNOWN**.
- **It coexists with an opposite-shaped concentration.** In the same instrument, *"The Company's revenues
  are principally derived from online advertising"* and the single largest named relationship is with
  **Yahoo** — simultaneously the largest named customer and the largest named competitor, terminated
  effective July 2004 (records B36-B38). Both statements are true in one document because they measure
  different things: no *customer* reached 10%, while one *channel* (search distribution through a portal)
  had been the company's most important commercial relationship for four years. Conflating them is the
  error this subsection exists to prevent, and P1CNF02 carries the pair as a bound-versus-channel conflict
  rather than resolving either.

### F.4 How customers were acquired, and the threshold that reveals the segment

Two acquisition facts are documented; both are `(PB)` and both are worth having because they are the
earliest mechanism evidence anywhere in the corpus. First, the **free-inclusion rule**: *"We do not accept
payment for inclusion or ranking in them"* and *"Inclusion and frequent updating in our index are open to
all sites free of charge"* — a deliberate decision **not to sell** the thing every competitor sold (the
patent's own background calls paid inclusion the source of "commercial appeals that should not be
considered a match to the query", §C.1). Second, a **segment threshold** in the AdSense description: *"For
web sites with more than 20 million page views per month, we provide customization services"* — the only
quantified customer-sizing rule in the held filing text, and the only place in the corpus where the
company's own arithmetic reveals how it tiered its supplying side. Neither document is independent of
LIN-REG; the 20-million figure is a 2004 policy statement, not a window measurement, and no held 1999-2001
text uses the phrase "page views" as a threshold at all.

### F.5 Data gaps for this section (full rows in `data_gaps.csv` below)

The first licensee's identity; the count of advertisers at any date; churn or renewal of any kind; the
price of a WebSearch licence; the revenue split by customer type for any year; whether any 1998-2001
customer paid anything at all. All **UNKNOWN**, all with a named route: the Q1 1999-2001 customer rows
exist only if a contract or a periodical surfaces them, and the periodical family has been tried for the
founding window and returned **0** hits on the founders' names across every byte held
(`research/A2_periodical_settlement.md`, record B10).

### F.6 Coda (§7)

**Mechanism:** the documented customer history is *pay a university for the right to exist technically →
licence the engine to websites → sell ad inventory directly through a sales force → sell it self-service →
pay the network's sites most of the money their ads earn*. **Mechanism for the earliest step, stated
plainly:** Google's first *outflow* was to Stanford, and its first documented *inflow* — $220 thousand of
FY1999 net revenues — has no customer attached to it in any held document. **Alternative explanation not
excluded:** the "<10% no customer" disclosure could be satisfied by a customer base already large in 2001
and by one that was tiny and fragmented; the bound is identical in both worlds and cannot distinguish
them. **Confidence:** High for the two Stanford dates, Medium for the mechanism sequence, **UNKNOWN** for
every customer identity. **Firewall test:** a company whose first recorded payment is a royalty, whose
first revenue has no name attached, and whose only early concentration statistic is an inequality, is not a
company whose customer story reads backwards from 2004.

### F.7 Load-bearing claim records for §F

P1F01 Claim: The only audited customer-side statement in the corpus is a concentration ceiling, and it
begins in 2001. — Date: 2001-01-01 → 2003-12-31 — Source path:
`sources/sec/0001193125-04-073639_0001193125-04-073639.txt`, notes to consolidated financial statements —
Source date: 2004-04-29 — URL: as B01 — Archived: as path — Tier: 1 — Class: FACT (audited-band disclosure
by the issuer; the auditor's report covers 2001-2003) — Passage: "No customer accounted for greater than
10% of net revenues in 2001, 2002 and 2003 or in the three months ended March 31, 2003 and 2004." (29
words) — Conf: High — Corroboration: 1 lineage; Ernst & Young's report is the only independent attestation
inside it (record B15) — Conflicts: None on the sentence; P1CNF02 on what it is compatible with.
independence_note: same lineage as B01, but inside the auditor's band, which is why it outranks the
window's unaudited revenue numbers for customer-structure inference. It remains a **bound**, and a bound is
not a count.

P1F02 Claim: The earliest external value flowing from Google flowed to a university as licence
consideration, not from a customer. — Date: 1998-12-01 (Original Agreement); 1999-04-14 (share issuance) —
Source path: `sources/sec/0001193125-04-105564_dex1010.htm` §§1.1, 8.1 — Source date: 2003-10-13
(effective); filed 2004-06-21 — URL:
sec.gov/Archives/edgar/data/0001288776/000119312504105564/dex1010.htm — Archived: as path — Tier: 1 —
Class: FACT (executed bilateral agreement; counter-signatory is the Board of Trustees of the Leland
Stanford Junior University) — Passage: "On April 14, 1999, GOOGLE issued [***] shares … of Series A
Preferred Stock to STANFORD." — Conf: High on the dates; **UNKNOWN** on every quantity (redacted under
confidential treatment) — Corroboration: 2 parties to 1 instrument; 1 held document — Conflicts: inherited
U-8 (what "September 1998" incorporation means against a 1998-12-01 licence).
independence_note: records B06/B29/B30/B31 already carry this carrier; **the customer-reading is new to
this pass** and is the reason P1F02 exists — the corpus's first financial outflow direction is documented,
and it is not a sales pipeline.

P1F03 Claim: The largest in-window commercial relationship was with a company the filing also names as a
primary competitor, and Google ended it. — Date: 2000-06 → 2004-07 `(PB termination)` — Source path: as
P1F01, "Competition" — Source date: 2004-04-29 — URL: as P1F01 — Archived: as path — Tier: 1 — Class: FACT
— Passage: "Since June 2000, Yahoo has used, to varying degrees, our web search technology on its web site
to provide web search services to its users. We have notified Yahoo of our election to terminate our
agreement, effective July 2004." — Conf: High — Corroboration: 1 lineage, three mentions of the same
relationship (records B36-B38) counted as one — Conflicts: P1CNF02 (customer concentration "<10%" vs.
channel dependence).
independence_note: same lineage as B36; the only external witness to the June-2000 start is a periodical
that does not name the arrangement (§E.3), so independence is nil and the three mentions are one source.

P1F04 Claim: The company's earliest documented public-facing commercial policy was a decision not to sell
index inclusion. — Date: 2004-04-29 (statement); applicability to 1998-2001 **UNKNOWN** — Source path: as
P1F01, the "user commitments" passage — Source date: 2004-04-29 — URL: as P1F01 — Archived: as path —
Tier: 1 — Class: FOUNDER CLAIM (a 2004 statement of principle) + FACT that the commitment is printed —
Passage: "Our search results will be objective and we will not accept payment for inclusion or ranking in
them." / "Inclusion and frequent updating in our index are open to all sites free of charge." — Conf:
High that the sentences are printed (each recurs across printings of one instrument) — Corroboration: 1
lineage — Conflicts: None; but §C.1's patent background shows the paid-inclusion model the sentence
rejects was the visible industry norm, which is the strongest available context for it.
independence_note: same lineage as B01. Note the boundary this record must not cross: a 2004 published
commitment is not evidence about a 1999 pricing practice, and the corpus holds no 1999-2001 price list or
inclusion policy to compare.

---

## Register rows for merge


>>> REGISTER ROWS FOR MERGE <<<
STATUS: WRITTEN 2026-09-26

*Emit-only. **No register CSV on this company was opened, created or edited by this pass** — there are none
at the company root or under `research/`, and a merge pass applies these. `stage` is the controlled literal
**`stage1`** on every row (§13 register vocabulary); numeric stage values are not used anywhere below. All
`P1x` ids are **dossier-local** (Header, "ID scheme"). Where a row rests on a carrier the records dossier
`research/B1_filing_records.md` already emitted (`B01`-`B43`), that is said in `notes` so the merge keeps
**one** source row and aliases the other rather than counting nine printings of one registration statement
as nine corroborations. **Row addressing for the registers whose §13 schema has no id column:** quantitative and timeline rows carry their dossier-local tag as the first characters of the `notes` cell (`P1QTN01 - `, `P1TML01 - `), data-gap rows carry it as the first characters of the `gap` cell (`P1GAP01 - `), and decision rows are addressed by (date, decision) in block order, which is what the `P1DECnn` tokens in the sources `claim_supported` cell mean. Sources rows carry `source_id` and conflict rows carry `conflict_id`, both from this volume. Rows carrying `(PB)` in `notes` are post-boundary evidence retained because a
Stage-1 section uses them; they may not be pulled inside the stage's own series.*

**Carrier table for P1CNF01** — read this pass from the SGML header block and cover page of each held
`.txt` submission under `sources/sec/` (the form/amendment labels below **replace** the lineage map in
`research/B1_filing_records.md`, whose "file no. 333-117934" premise and "S-1/A eight times" count do not
reproduce):

| Accession | Header form | SEC FILE NUMBER | Cover self-style |
|---|---|---|---|
| -04-073639 (2004-04-29) | S-1 | 333-114984 | "As filed … April 29, 2004" |
| -04-093053 (2004-05-21) | S-1/A | 333-114984 | Amendment No. 1 |
| -04-105564 (2004-06-21) | S-1/A | 333-114984 | Amendment No. 2 |
| -04-115812 (2004-07-09) | **8-K** | 000-50726 | (separate instrument; Exchange Act number) |
| -04-116608 (2004-07-12) | S-1/A | 333-114984 | Amendment No. 3 |
| -04-124025 (2004-07-26) | S-1/A | 333-114984 | Amendment No. 4 |
| -04-131481 (2004-08-04) | **S-1** | **333-117934** | "As filed … August 4, 2004" — no amendment number |
| -04-134174 (2004-08-06) | S-1/A | **333-117934** | **Amendment No. 1**; cover prints "Registration No. 333-117934" |
| -04-135503 (2004-08-09) | S-1/A | 333-114984 | **Amendment No. 5** |
| -04-138034 (2004-08-11) | S-1/A | **not readable — index page only held** | UNTESTED: a coverage hole, not an absence |
| -04-143377 (2004-08-19) | 424B4 | — | **NOT HELD** (re-verified: absent from all 127 files on disk) |

### sources.csv — `source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
P1SRC01,stage1,"P1A01 P1B01 P1B02 P1B05 P1C01 P1C02 P1C04 P1E01 P1TML01 P1QTN01 P1QTN02 P1QTN08","US 6,285,999 B1 - Method for node ranking in a linked database",Lawrence Page (inventor); Leland Stanford Junior University (assignee),patent grant record,primary,"1998-01-09;2001-09-04",2001-09-04,2026-09-26,patents.google.com/patent/US6285999B1/en,"sources/patents/us6285999.html (+ .sidecar.json)",1,FACT as to the document contents,High,OUTSIDE both founder lineages: a registry document no company PR controlled; the same dates are independently recited in the executed Stanford licence,searches typically return hundreds of irrelevant or unwanted documents which camouflage the few relevant ones,"398,323 chars tag-stripped read this pass. New content this pass: the Background section's named prior art (RankDex/IDD; Web Worm, McBryan 1994), the quantified scale anchor, the acknowledgment sentence naming five helpers, and claim 1. Records B04/B05 used only the two dates and are not re-emitted. NEW STRINGS read off this page by the earlier passes that never quoted them: Prior art date 1997-01-10 (host-disclaimed as an assumption), Inventor Lawrence Page (single name), Original Assignee Leland Stanford Junior University (host-disclaimed as possibly inaccurate), 2018-01-09 Anticipated expiration, and 2017-12-05 Assigned to GOOGLE LLC change of name Assignors GOOGLE INC. See P1CNF07 and B.1a."
P1SRC02,stage1,"P1A02 P1D01 P1TML03","Wayback CDX response, bare host google.com (ascending, limit 3)",Internet Archive,crawl index,primary,1998-11-11,2026-09-25,2026-09-26,web.archive.org/cdx/search/cdx?url=google.com,"sources/wayback/cdx_retry.json (+ .sidecar.json)",1,FACT,High,third-party crawl record; independent of the registrant,"[[""timestamp"",""original"",""statuscode""],[""19981111184551"",""http://google.com:80/"",""200""]]","3 duplicate rows for the same capture in the held response; the 14-digit timestamp is the date carrier. Two further CDX queries (www variant, google.stanford.edu) returned HTTP 503 and are P1SRC11, not this row."
P1SRC03,stage1,"P1A02 P1D01 P1D02 P1E02 P1TML03 P1TML04 P1QTN03 P1VAL01 P1FAI01","Archived google.com front page, capture 19981111184551",Google (unattributed page),archived company page,primary,1998-11-11,1998-11-11,2026-09-26,web.archive.org/web/19981111184551id_/http://google.com/,sources/wayback/google_19981111_raw.html (212 B) + .sidecar.json,1,CONTEMPORANEOUS OBSERVATION,High,fully independent of the registration lineage; unauthenticated by the company,WELCOME TO GOOGLE / GOOGLE SEARCH ENGINE PROTOTYPE / MIGHT-WORK-SOME-OF-THE-TIME-PROTOTYPE THAT IS MUCH MORE UP TO DATE.","THE TWO HREFS (http://google.stanford.edu and http://alpha.google.com/) ARE IN THE BYTES AND WERE NOT REPORTED by the probe dossier or by record B07, which quoted visible text only. That is this pass's addition to B07; merge keeps one source row carrying both passages."
P1SRC04,stage1,"P1A03 P1C03 P1D03 P1D04 P1F01 P1F03 P1F04 P1QTN05 P1QTN07 P1TML02 P1TML06 P1TML08..P1TML14 P1VAL03..P1VAL06 P1DEC02..P1DEC05 P1CHN01..P1CHN05",Google Inc. Form S-1 registration statement (initial printing),Google Inc.; Ernst & Young LLP (auditor; 2001-2003 only),securities registration statement,primary,"1998-09;1999-Q1;2000-Q1;2000-Q4;2001;2003-12-31",2004-04-29,2026-09-26,sec.gov/Archives/edgar/data/0001288776/000119312504073639/0001193125-04-073639.txt,"sources/sec/0001193125-04-073639_0001193125-04-073639.txt (5,719,779 B; 348,683 words tag-stripped)",1,FOUNDER CLAIM for anything about 1998-2001 / FACT for the instrument's own contents and the audited band,Medium,LIN-REG: this accession plus its eight re-printings plus the unheld 424B4 are ONE source (method 3). Counted once. The auditor's report is the only independent attestation inside it and stops at 2001.,"Our original business model consisted of licensing our search engine services to other web sites. In the first quarter of 2000, we introduced our first advertising program.","New text read this pass and NOT in records B01-B43: the mechanism-sequencing paragraph (Premium Sponsorships, display pricing, AdWords Q4-2000, cost-per-click from Q1-2002), the three-constituencies taxonomy, the mission clause, the no-customer-over-10-percent audited note, the free-inclusion commitments, the 20-million-page-views customization threshold, the GSA paragraph, and the two against-interest employment lines."
P1SRC05,stage1,"P1CNF01","SEC-filed header and cover pages of the nine held registration printings",U.S. Securities and Exchange Commission (header block) / Google Inc. (covers),filing metadata,primary,"2004-04-29;2004-08-04;2004-08-06;2004-08-09",2004-08-09,2026-09-26,sec.gov/Archives/edgar/data/0001288776/,sources/sec/*.txt (9 accessions; the carrier table above is the extract),1,FACT,High,SEC's own header block plus the registrant's own cover page printed on the instrument; the two agree with each other and disagree with the inherited dossier,Amendment No. 5 to Form S-1 (File No. 333-114984) / Amendment No. 1 to Registration Statement (File No. 333-117934),DEFECT AGAINST RECORDS DOSSIER B1_filing_records.md LINEAGE MAP: its premise 'file no. 333-117934 / 000-50726 ... re-filed as S-1/A eight times' does not reproduce. Two Securities Act numbers with independent amendment counts; see P1CNF01. Accession -138034 is index-page-only so its number is UNTESTED.
P1SRC06,stage1,"P1F02 P1TML02-adjacent P1TML05 P1TML07 P1TML12 P1DEC01 P1VAL02","Exhibit 10.10, Amended and Restated License Agreement between Stanford and Google Inc.",Board of Trustees of the Leland Stanford Junior University and Google Inc.,executed bilateral agreement,primary,"1998-12-01;1999-04-14;2000-04-17;2003-10-13",2004-06-21,2026-09-26,sec.gov/Archives/edgar/data/0001288776/000119312504105564/dex1010.htm,sources/sec/0001193125-04-105564_dex1010.htm,1,FACT (executed agreement; the counterparty had its own reasons to keep dates straight),High,inside EDGAR for custody but NOT LIN-REG narrative: Stanford co-signed. Records B04-B06 B26 B29-B31 B35 already emit this carrier - merge keeps ONE source row and aliases.,"On April 14, 1999, GOOGLE issued [***] shares ... of Series A Preferred Stock to STANFORD.","New reading this pass (P1F02): the DIRECTION of value flow - Google's first documented external issuance was TO a university for technology, which bounds the first-customer question at F.2. All money and share quantities are redacted [***] under confidential treatment."
P1SRC07,stage1,"P1E02 P1QTN04 P1VAL04","Yahoo Internet Life, Search the Web Part II round-up",Yahoo Internet Life (consumer technology monthly),trade/consumer periodical OCR,secondary,2000-07,2000-07-01,2026-09-26,archive.org item yahoo-internet-life-magazine-july-2000,"sources/periodicals/yahoo-internet-life-magazine-july-2000_djvu.txt (361,043 B; 16,052 lines)",3,CONTEMPORARY OBSERVATION,Medium,THE ONLY INDEPENDENT IN-WINDOW CARRIER OF THE PRODUCT IN THE WHOLE CORPUS; it names no founder no company and no founding event,"Unlike other search engines, Google uses proprietary technology to ensure that the first hits you get for your search are the best.","UNVERIFIED TLS per research/A2_periodical_settlement.md, so capped at Medium. OCR artifact in the bytes: 'othersearch'. A2's cited line range (11027-11033) stops mid-sentence; the passage above is re-grepped from held lines 11026-11036. 'google' occurs on 5 lines of 16,052."
P1SRC08,stage1,"P1E03 P1E04 P1QTN06","Google Inc. Beta Evaluation Agreement, Google Search Appliance Pre-release Version 4.2 and 4.4",Google Inc. (form author); Central Intelligence Agency (evaluator and publishing custodian),executed form contract in third-party archive,primary,2004-11,2004-11,2026-09-26,archive.org item cia-readingroom-document-0001487901,"sources/ia/cia_1487901_djvu.txt (16,235 B measured this pass; the probe reported 16,305 B) + .sidecar.json",1,FACT,High,Google-authored form but held and published by the counterparty so custody is independent of the company; NOT LIN-REG,"The term of the license granted herein shall be for a sixty (60) day period (the 'Evaluation Period'), commencing on the date of shipment of the Appliance","(PB) FOR EVERY STAGE-1 USE - Nov 2004, three years past the close. Day-of-month OCR-degraded to f19/j. The indexing ceiling is OCR-destroyed (P1E04). Byte-count discrepancy against the probe's own metadata noted for the merge census."
P1SRC09,stage1,"P1A01 P1GAP05 P1GAP06","Google Inc. submissions index (6,407 filings, zero unanswered slices) and earliest-per-form enumeration",U.S. Securities and Exchange Commission,regulatory index,secondary,"2001-03-12;2004-04-29;2004-08-19;2005-03-30",2026-09-25,2026-09-26,sec.gov submissions API CIK 0001288776,sources/_index/submissions.csv; _index/_INDEX.md; _index/submissions.json,1,FACT,High,the registrant's own SEC index; it witnesses filing acts and nothing before them,NO_VERBATIM_PASSAGE_RECORDED,"Establishes that a 424B4 exists at 2004-08-19 in the enumeration and is NOT held on disk (re-verified this pass across all 127 files), and that no 424B1 appears in 6,407 rows (inherited U-1). Index rows are filing facts, not evidence of content."
P1SRC10,stage1,"P1B03 P1GAP01 P1GAP04","Held periodical corpus as a negative-result carrier (Network World 1998-03-30 and 1999-05-10; Network World 1999-01; Yahoo Internet Life 2001-09 and 2002-01)",various publishers,periodical OCR searched,secondary,1998;1999;2001;2002,2026-09-26,2026-09-26,archive.org (per-file metadata sidecars),"sources/periodicals/ (6 text items; 1,201,506 B settled by A2 plus 2 later arrivals from the fleet harvester)",3,FACT about the search / UNKNOWN about the event,High,a documented null over bytes rather than an unsearched gap: founders' names 0 hits; the harvester's own verdicts for the later items are NULL and BARE_WORD_MATCH,NO_VERBATIM_PASSAGE_RECORDED,"RD-14 rule 11 accounting: bub_gb_chwEAAAAMBAJ (266,428 B), yahoo-internet-life-magazine-january-2002 (285,579 B) and -september-2001 (338,899 B) arrived in sources/ AFTER the A2 dossier closed and are cited here for the first time. The single September-2001 hit is 'BS letter of the alphabet' (mine l.2252) - a BARE_WORD_MATCH under RD-124, not a naming of this company."
P1SRC11,stage1,"P1D02 P1GAP04 P1GAP08","Negative artifacts kept deliberately: Wayback CDX 503 bodies (bare host twice, www variant, google.stanford.edu) and the USPTO tmsearch 405 response",Internet Archive; U.S. Patent and Trademark Office,HTTP error bodies,secondary,2026,2026-09-25,2026-09-26,web.archive.org/cdx (4 queries); tmsearch.uspto.gov/api-v1-0-0/tmsearch,"sources/wayback/cdx_bare.json, cdx_www.json, cdx_stanford.json; sources/uspto/uspto_tm_google.json",3,NOT-ANSWERED,High,an error page is a dead route and never an absence,NO_VERBATIM_PASSAGE_RECORDED,"The google.stanford.edu CDX query 503'd, so that host's own capture history is UNANSWERED - material to P1D02 and P1CNF06, which rely on the href string rather than on any capture of the host itself. Trademark serial history therefore UNTRIED (probe N-2)."
```

### quantitative.csv — `company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
Alphabet (Google Inc.),stage1,1998-01,indexable_web_size_stated_in_the_priority_filing,500,gigabytes (floor: in excess of),P1SRC01,2001-09-04,ESTIMATE,Low,not_derived,"P1QTN01 - A January-1998 inventor's unsourced scale anchor. NOT a Google figure and NOT an observation: no method, no source and no measurement basis is given inside the carrier. Usable as an industry denominator only."
Alphabet (Google Inc.),stage1,1998-01,searches_per_day_by_an_unnamed_popular_engine,30000000,searches per day (floor),P1SRC01,2001-09-04,ESTIMATE,Low,not_derived,"P1QTN02 - The referent is 'a popular search engine' - unnamed - so this may not be attributed to Google, AltaVista, Yahoo or GoTo. The only in-window quantity about the PROBLEM rather than the company."
Alphabet (Google Inc.),stage1,1998-01-09,patent_named_inventors_on_the_priority_document,1,named inventors,P1SRC01,2001-09-04,FACT,High,not_derived,"P1QTN03 - Inventor: Lawrence Page. Sergey Brin appears in the specification only in the acknowledgment sentence. The bound this puts on the founder narrative is carried as P1CNF03, not as a number."
Alphabet (Google Inc.),stage1,1998-11-11,size_of_the_earliest_archived_public_page,212,bytes,P1SRC03,1998-11-11,FACT,High,not_derived,"P1QTN04 - Whole-page size as held, sidecar-confirmed. The evidentiary point is what is ABSENT: no form, no input element, no query count - see D.2."
Alphabet (Google Inc.),stage1,2000-07,google_rank_in_a_third_party_search_roundup,4,position among engines reviewed,P1SRC07,2000-07-01,CONTEMPORARY OBSERVATION,Medium,not_derived,"P1QTN05 - UNVERIFIED TLS and Tier-3 press. An editorial ranking, not a market share; the review's total engine count is not legible in the held lines."
Alphabet (Google Inc.),stage1,2001-12-31,derived_ceiling_on_any_single_customers_fy2001_revenue,8642600,USD,P1SRC04,2004-04-29,DERIVED,Medium,"10 percent of FY2001 net revenues of 86,426 thousand = 8,642.6 thousand","P1QTN06 - DERIVED and printed nowhere. FY2001's revenue value is identical on both sides of the mid-lineage presentation change (inherited U-9), which is itself evidence the gross/net reclassification did not touch 2001."
Alphabet (Google Inc.),stage1,2004-11,search_appliance_beta_evaluation_period,60,days,P1SRC08,2004-11,FACT,High,not_derived,P1QTN07 - (PB). Commences on shipment; extendable in Google's sole discretion; return within ten business days of termination. Retained because it is the only held document quantifying any Google commercial term - and it is three years outside the stage.
Alphabet (Google Inc.),stage1,2004-04-29,network_member_pageviews_threshold_for_customization,20000000,page views per month,P1SRC04,2004-04-29,FACT (policy statement),Medium,not_derived,"P1QTN08 - (PB) policy. The only quantified customer-sizing rule in the held filing text; no in-window document uses 'page views' as a threshold at all, so it cannot be read backwards to 1999-2001."
```

### timeline.csv — `company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
Alphabet (Google Inc.),stage1,1998-01-09,U.S. patent 6285999 filed (app. US09/004827); assignee Stanford; inventor Page,Lawrence Page; Leland Stanford Junior University,Palo Alto / Stanford CA,P1SRC01,FACT,High,inherited U-3,"P1TML01 - PRE-ENTITY. The registrant did not exist at this date, so this row is pre-history, kept and labelled (method 2). Corroborated by the licence recital: two carriers, one of them the counterparty."
Alphabet (Google Inc.),stage1,1996,Stanford docket S96-213 carries a 1996 year in its numbering,Lawrence Page; Stanford,Stanford CA,P1SRC06,INFERENCE,Low,inherited U-7 family,P1TML02 - NOT A DATED EVENT. The year is read out of a docket-number convention; no held document dates any 1996 act. The founders'-letter arithmetic (record B09) is compatible with 1996 and proves nothing. Retained so the leg is not silently deleted.
Alphabet (Google Inc.),stage1,1998-09,incorporated in California; day UNKNOWN,Larry Page; Sergey Brin,Mountain View CA,P1SRC04,FOUNDER CLAIM,Medium,inherited U-7,P1TML03 - Company self-report filed 5.6 years after the event; three internal repetitions in one instrument are one sentence. Two independent anchors presuppose the month: the plan adoption (B24) and the licence (P1TML05).
Alphabet (Google Inc.),stage1,1998-11-11T18:45:51,earliest archived public page at google.com returns HTTP 200,unattributed operator; Internet Archive crawler,Mountain View / Stanford CA,P1SRC02,CONTEMPORANEOUS OBSERVATION,High,P1CNF06,"P1TML04 - A terminus ante quem for the origin and the upper bound of the stage's opening. The date form is the CDX 14-digit capture string, not an inference."
Alphabet (Google Inc.),stage1,1998-11-11,two search services were publicly reachable on two hosts: google.stanford.edu (labelled Prototype) and alpha.google.com (labelled much more up to date),unattributed,Stanford University and google.com,P1SRC03,FACT as to the markup / INFERENCE as to what the two hosts were,Medium,P1CNF06,"P1TML05 - Recorded as two services reachable, NOT as 'the company ran an A/B test' - see D.5. The Stanford-host CDX query 503'd, so that host's own capture history is UNANSWERED (P1SRC11)."
Alphabet (Google Inc.),stage1,1998-12-01,Original License Agreement between Stanford and Google Inc. effective,Stanford Board of Trustees; Google Inc. a California corporation,Stanford / Mountain View CA,P1SRC06,FACT,High,inherited U-8,"P1TML06 - Earliest entity-level documentary date in the corpus. Google is the LICENSEE AND PAYER here, which is the point of P1F02: the first documented external value flow is outward, to a university."
Alphabet (Google Inc.),stage1,1999-Q1,began licensing the WebSearch product,Google Inc.,Mountain View CA,P1SRC04,FOUNDER CLAIM,Medium,None,"P1TML07 - Stage 1's validation marker. No licensee named, no price, no count, no contract on disk. Quarter granularity cannot carry a day."
Alphabet (Google Inc.),stage1,1999-04-14,Google issued Series A Preferred Stock to Stanford as licence consideration,Google Inc.; Stanford,Mountain View / Stanford CA,P1SRC06,FACT,High,None,"P1TML08 - Quantities redacted [***]. The recital ties the grant to a round with an eight-million-dollar post-money valuation - a valuation, not a date and not an amount raised."
Alphabet (Google Inc.),stage1,2000-Q1,introduced the first advertising program (Premium Sponsorships) sold through a direct sales force,Google Inc.; advertisers,Mountain View CA,P1SRC04,FOUNDER CLAIM,Medium,P1CNF04,P1TML09 - Priced per ad DISPLAYED with revenue recognised on display. The mechanism pivot of the stage; no independent carrier exists.
Alphabet (Google Inc.),stage1,2000-06,Yahoo began using Google web search technology on its site to varying degrees,Google Inc.; Yahoo Inc.,Sunnyvale / Mountain View,P1SRC04,FOUNDER CLAIM (self-report of a bilateral arrangement),Medium,inherited U-15,P1TML10 - Record B36's carrier. Largest named customer and largest named competitor at once; the financial trace is the warrant liability at B16. Corroboration counted ONCE despite three mentions in the lineage.
Alphabet (Google Inc.),stage1,2000-07,an unaffiliated consumer magazine ranked Google fourth among reviewed engines and praised its top-result quality,Yahoo Internet Life (third party),USA,P1SRC07,CONTEMPORARY OBSERVATION,Medium,None,P1TML11 - The only independent in-window observation of the product anywhere in the corpus. UNVERIFIED TLS cap.
Alphabet (Google Inc.),stage1,2000-04-17,Stanford transferred part of its grant to the two inventors,Stanford; Lawrence Page; Sergey Brin,Stanford CA,P1SRC06,FACT,High,None,P1TML12 - The earliest documented personal equity reaching either founder arrives through the university's transfer and not a purchase. All share numbers redacted.
Alphabet (Google Inc.),stage1,2000-Q4,launched Google AdWords as an online self-service advertising program,Google Inc.; advertisers,Mountain View CA,P1SRC04,FOUNDER CLAIM,Medium,P1CNF04,P1TML13 - Removes the per-customer sales conversation from the revenue mechanism. The stage's fourth beat at the operating level; the year-granular profitability claim follows.
Alphabet (Google Inc.),stage1,2001,we became profitable in 2001 - the issuer's own first profitable year,Google Inc.,Mountain View CA,P1SRC04,FOUNDER CLAIM (year granularity),Medium,None,"P1TML14 - ADOPTED STAGE-1 CLOSE. FY2001 is inside the auditor's band (B15), so the revenue figure for that year is attested while the sentence about profitability is not. No day or month is recoverable."
Alphabet (Google Inc.),stage1,2002-Q1,(PB) AdWords offered exclusively on a cost-per-click basis,Google Inc.; advertisers,Mountain View CA,P1SRC04,FOUNDER CLAIM,Medium,P1CNF04,P1TML15 - Immediately post-boundary and included precisely because it bounds what the window can say: no pay-per-click evidence exists INSIDE Stage 1.
Alphabet (Google Inc.),stage1,2002-04,(PB) Overture Services patent suit filed against the AdWords program,Yahoo/Overture; Google Inc.,USA,P1SRC04,FACT (disclosed legal event),High,inherited U-16,P1TML16 - Post-boundary by one quarter; retained because it is the first documented attack on the mechanism adopted inside the window (A.2). Record B39's carrier.
```

### decisions.csv — `company,stage,date,decision,state_before,information_available,unknowns,alternatives,constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date,decision,state_before,information_available,unknowns,alternatives,constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref
Alphabet (Google Inc.),stage1,1998-12-01,license the ranking technology from Stanford rather than own it,the invention belonged to the university and no company had existed three months earlier,patent filed 1998-01-09 assigned to Stanford; the company needed rights to use it,whether ownership was ever sought and what an unlicensed alternative would have cost,UNKNOWN - no held document records a rejected alternative,"Stanford's ownership of US 6285999; later, exclusivity bounded at 2011-09-04",UNKNOWN - no document records the deliberation,obtained the right to use the technology,paid in equity plus a redacted royalty; RETROSPECTIVE,P1SRC06,Medium,P1F02
Alphabet (Google Inc.),stage1,UNKNOWN (a 2004 statement of practice),keep index inclusion and re-crawling free and refuse payment for ranking,competitors sold inclusion and frequent updating,1998 patent background already called paid results commercial appeals that should not be considered a match,when the commitment began and whether it cost revenue,UNKNOWN - no carrier of the decision inside the window,competitor practice of paid inclusion and the company's own ranking claims,the commitment is printed in 2004; its 1998-2001 origin is not recorded,relevant results and user trust,UNKNOWN - no revenue figure is attributable to the policy,P1SRC04,Medium,P1F04
Alphabet (Google Inc.),stage1,1998-11-11,two services were published on two different hosts (a Stanford host and alpha.google.com) instead of one,a prototype on a university host,public reachability of both,who operated either host and whether the split was deliberate,UNKNOWN,university infrastructure and hostname availability,UNKNOWN - the page is a pointer page and not a decision record,a second service that was much more up to date would be reachable,UNKNOWN - no in-window measurement of either host,P1SRC03,Low,P1D02
Alphabet (Google Inc.),stage1,2000-Q1,introduce direct-sale advertising priced per display alongside engine licensing,revenue came only from licensing sites,search traffic and advertiser interest; FY1999 revenue of $220 thousand,how many customers the licensing model had and which came first,UNKNOWN - no alternative named in the corpus,a direct sales force,not recorded - rationale UNKNOWN,an additional revenue stream,Premium Sponsorships ran until 2004-01-01 (PB); RETROSPECTIVE,P1SRC04,Medium,P1D03
Alphabet (Google Inc.),stage1,2000-Q4,replace the sales-gated program with a self-service program (AdWords),ad inventory was sold through a direct sales force,display-based pricing already in use,whether the sales constraint or the pricing drove the change,UNKNOWN,self-service onboarding and billing infrastructure,not recorded - rationale UNKNOWN,advertisers could buy without a sales conversation,"FY2001 net revenues 86,426 thousand and the company's own statement that it became profitable in 2001, , both from the same instrument, RETROSPECTIVE",P1SRC04,Medium,P1D03
```

### validation.csv and failures.csv — `company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes
Alphabet (Google Inc.),stage1,1998-11-11,a public hostname answered an unrelated crawler with a search-service index page,1 capture; HTTP 200; 212 bytes,a service existed and was reachable by a party with no relationship to the company,users and demand and uptime and quality; nor that a company rather than a university project operated it,P1SRC03,CONTEMPORANEOUS OBSERVATION,High,P1VAL01 - the stage's first external signal
Alphabet (Google Inc.),stage1,1998-12-01,an institution executed a contract naming Google Inc. as a California corporation and as a counterparty,1 executed bilateral agreement,a legal person existed and could contract and had a technical need worth paying for,revenue or product readiness; nor that any customer existed,P1SRC06,FACT,High,P1VAL02 - earliest entity-level documentary date in the corpus
Alphabet (Google Inc.),stage1,1999-Q1,the first licensed product generated the first recorded revenue,FY1999 net revenues $220 thousand (unaudited band),someone paid for something,who and how many and at what price and whether it repeated,P1SRC04,FOUNDER CLAIM,Medium,P1VAL03 - one annual total with no split; outside the auditor's attested band (B15)
Alphabet (Google Inc.),stage1,2000-07,an unaffiliated magazine placed Google fourth among reviewed engines and praised its top results,rank 4 of the engines reviewed; 5 mentioning lines in 16052,external usable-quality judgement existed independently of the company,market leadership or share or traffic; nor any corroboration of the founding,P1SRC07,CONTEMPORARY OBSERVATION,Medium,P1VAL04 - UNVERIFIED TLS; Tier-3 press under method 5
Alphabet (Google Inc.),stage1,2000-Q1 to 2000-Q4,two revenue mechanisms were built and replaced within twelve months,2 program launches in 4 quarters,the organisation could change its business model twice without stopping,that either mechanism worked - no revenue is attributable to either one,P1SRC04,FOUNDER CLAIM,Medium,P1VAL05 - the stage's real validation signal is the ability to pivot and not a unit-economics result
Alphabet (Google Inc.),stage1,2001,the issuer stated the company became profitable,year-granular; FY2001 net revenues 86426 thousand,first self-stated profitable year,causation (following the launch of AdWords is a conjunction) nor which mechanism produced the margin,P1SRC04,FOUNDER CLAIM,Medium,"P1VAL06 - FY2001 IS inside the auditor's band (B15), which is why this row is Medium and not Low: the number is attested and the sentence is not"
Alphabet (Google Inc.),stage1,1998-11-11,the company's own public page labelled its product a prototype that might work some of the time,1 page; 2 self-labelled services,contemporaneous admission that the product was presented as unfinished and unreliable,"that the product actually failed, or any measurement of how often it worked",P1SRC03,CONTEMPORANEOUS OBSERVATION,High,P1FAI01 - recorded because the admission is independent of every later quality narrative
Alphabet (Google Inc.),stage1,1998-09 to 2004,shares and options issued under the 1998 and 2003 Stock Plans were not registered or exempt,exposure up to $34 million plus statutory interest,the company's earliest equity compensation was legally defective on the company's own admission,that any payment was made; how many holders were affected; whether rescission was accepted,P1SRC04,FACT (self-disclosed against interest),High,"P1FAI02 - record B25's carrier, counted once"
Alphabet (Google Inc.),stage1,2002-04,(PB) a competitor sued the AdWords program for patent infringement,1 suit; patent US 6269361; settled 2004-08-09 with a perpetual licence and mutual releases,post-boundary by one quarter: the mechanism adopted in 2000 was contestable by a competitor within two years,any in-window operational failure of the company,P1SRC04,FACT (disclosed legal event),High,P1FAI03 - (PB) TAG BINDING: records B39 and inherited U-16
```

### channels.csv — `company,stage,channel,date_tested,why_tested,cost_or_effort,result,repeatability,source_id,confidence,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,channel,date_tested,why_tested,cost_or_effort,result,repeatability,source_id,confidence,notes
Alphabet (Google Inc.),stage1,wholesale licensing of the search engine to other websites,1999-Q1,the only model the company states it started with,price UNKNOWN - no customer licence fee appears in any held document,FY1999 net revenues $220 thousand and FY2000 $19108 thousand; no customer named,UNKNOWN - the count of licensees is never disclosed,P1SRC04,Medium,P1CHN01 - the two revenue points are totals and cannot be attributed to this channel alone
Alphabet (Google Inc.),stage1,direct sales force selling text ads per display (Premium Sponsorships),2000-Q1,licensing did not monetise the traffic the company describes,a sales force per customer,program terminated effective 2004-01-01 in favour of a single cost-per-click structure (PB),NOT scalable by the company's own later action - it replaced it,P1SRC04,Medium,P1CHN02 - the termination is the only evidence of the company's own judgment about this channel
Alphabet (Google Inc.),stage1,self-service advertising (AdWords),2000-Q4,remove the per-customer sales conversation,advertiser-side only; internal cost undisclosed,FY2001 net revenues $86426 thousand and the issuer's own first profitable year (same instrument),UNKNOWN - no advertiser count at any date in the window,P1SRC04,Medium,P1CHN03 - causation is asserted by the issuer and not evidenced (D.3)
Alphabet (Google Inc.),stage1,free index inclusion for all sites (a supply-side channel and not a revenue channel),UNKNOWN inside the window; printed 2004-04-29,draw the whole web onto the index without selling placement,foregone paid-inclusion revenue,not measured anywhere in the corpus,not measured,P1SRC04,Low,P1CHN04 - a 2004 statement of a practice whose 1998-2001 applicability is UNKNOWN
Alphabet (Google Inc.),stage1,word-of-mouth promotion,never dated and never measured,asserted by the company as the reason quality paid,undisclosed,the assertion itself is the only record: offering a high-quality user experience leads to increased traffic and strong word-of-mouth promotion,UNKNOWN,P1SRC04,Low,"P1CHN05 - THE CORPUS'S ONLY ACQUISITION-CHANNEL CLAIM CARRIES ZERO EVIDENCE, which is a finding and not a gap"
```

### conflicts.csv — `company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
Alphabet (Google Inc.),stage1,P1CNF01,Header; Boundary.4,"LIN-REG is ONE registration statement under 'file no. 333-117934 / 000-50726', re-filed as S-1/A eight times",research/B1_filing_records.md lineage map,2026-09-25,"the held printings carry TWO Securities Act numbers (333-114984 and 333-117934) with INDEPENDENT amendment counts: a later-dated 114984 printing styles itself Amendment No. 5 while an earlier-dated 117934 printing styles itself Amendment No. 1",P1SRC05,2004-04-29 to 2004-08-09,one dossier asserted a file number taken from an EDGAR full-text search response while the instrument's own header and cover pages print two numbers and two competing counts,"the printed instrument outranks an index response; but the auditor's consent inside the 117934 printings incorporates 'the Registrant's registration statement on Form S-1, as amended (File No. 333-114984), initially filed April 29, 2004', which ties both numbers to one statement",ONE developing registration statement known under two Securities Act numbers; the lineage stays ONE source for method 3 purposes and this row does not license counting two instruments,whether SEC re-numbered the statement or the registrant opened a parallel number; and what accession -138034 prints (index page only held),"High as to the enumerated printings; UNKNOWN as to the cause"
Alphabet (Google Inc.),stage1,P1CNF02,F.3,No customer accounted for greater than 10 percent of net revenues in 2001 2002 and 2003,P1SRC04 audited notes,2004-04-29,"The company's most important commercial relationship was with Yahoo, which used its search technology from June 2000 and had the agreement terminated effective July 2004",P1SRC04 Competition (record B36),2004-04-29,one measures customers against a revenue denominator while the other measures a distribution channel that carried traffic and brand rather than a disproportionate share of billings,both are the issuer's own words in one instrument; the audited note additionally sits inside the auditor's band,BOTH TRUE AND NON-COMPETING: no single CUSTOMER exceeded 10 percent while one CHANNEL was strategically decisive. A 'less than 3 percent of net revenues' bound (inherited U-15) is fully compatible with Yahoo mattering enormously.,the dollar contribution of the Yahoo arrangement is nowhere disclosed,High
Alphabet (Google Inc.),stage1,P1CNF03,B.2; E.1,The company was founded by two people who together created the technology: 'our founders Larry Page and Sergey Brin' and 'Sergey and I founded Google',P1SRC04 letter and Management,2004-04-29,The earliest dated registry-verified non-company document names ONE inventor (Page) and lists Brin among five people acknowledged for support in reducing the present invention to practice,P1SRC01,1998-01-09,a legal determination about one claim set versus a company's later account of its own origin; also a snapshot taken before any assignment or inventorship correction,the registry outranks the narrative for AUTHORSHIP OF THE PATENT; the narrative is the only carrier of the venture's self-description,BOTH STAND. Inventorship is not a census of a project and founder status is not a patent-law category; the corpus cannot say what Brin did before 1998-12-01,whether any document exists that would establish or refute joint inventive contribution; Stanford-side records are unqueried,Medium
Alphabet (Google Inc.),stage1,P1CNF04,D.3; F.1,Google's advertising business was built on performance pricing from the beginning (a common later telling; no carrier in this corpus),no carrier,UNKNOWN,The first two mechanisms were priced by DISPLAY - advertisers paid on the number of times ads appeared and AdWords customers 'originally paid us based on the number of times their ads appeared'; cost-per-click became exclusive only in 2002-Q1,P1SRC04 How We Generate Revenue,2004-04-29,a later structure projected backwards over the instrument's own succession of pricing bases,only one side is carried by any held document at all,"INSIDE STAGE 1 THE PRICING BASIS IS DISPLAY, and the cost-per-click mechanism is post-boundary (2002-Q1)",what share of FY2001 revenue came from display-priced versus any early click-priced inventory - never disclosed,High
Alphabet (Google Inc.),stage1,P1CNF05,D.2; E.2,Early growth came from a high-quality experience producing word-of-mouth promotion,P1SRC04,2004-04-29,The company's own earliest surviving public statement described its product as a Might-work-some-of-the-time-prototype,P1SRC03,1998-11-11,"a retrospective causal claim versus a contemporaneous self-labelled disclaimer, five and a half years apart and by different hands",the 1998 page is independent of the 2004 narrative and is the nearer witness to how the product was presented at the time,BOTH ARE TRUE OF THEIR OWN DATES; the 2004 sentence cannot be used as a description of the 1998 state of mind,whether the 1998 wording was a joke a disclaimer or an accurate engineering statement,Medium
Alphabet (Google Inc.),stage1,P1CNF06,D.1; D.2; B.3,The archived 1998-11-11 service is the company's first product (the registration statement's first-person framing: 'We were incorporated... we began licensing'),P1SRC04 (record B01/B03),2004-04-29,The archived page places the prototype at google.stanford.edu and offers a second service at alpha.google.com with no corporate identification anywhere in its 212 bytes,P1SRC03,1998-11-11,an issuer's later first-person plural describing an infrastructure that pre-dates its own first documented contracting by three weeks,an archive capture is independent of the narrative; the narrative is the only carrier of entity attribution,AN ENTITY THAT DID NOT YET EXIST IN ANY DOCUMENT CANNOT BE ESTABLISHED AS THE OPERATOR OF THE 1998-11-11 SERVICE FROM THAT SERVICE'S OWN BYTES. Stage 1 keeps both and attributes the capture to 'unattributed'.,who operated either host and whether the California corporation existed when the capture was made (claimed for September 1998 but first evidenced 1998-12-01),Low
Alphabet (Google Inc.),stage1,P1CNF07,Boundary.1; B.1a; C.1,"The dossier's opening leg is 1998-01-09, the patent's filing date, and the pre-history is fixed there (probe B0; records B04/B34)",research/A_chronology_feasibility.md; P1SRC01,1998-01-09,"The same held bytes print a PRIOR ART DATE of 1997-01-10 and an anticipated expiration of 2018-01-09, and the S-1 says the patent expires in 2017",P1SRC01; P1SRC04 (record B34),1997-01-10;2004-06-21,a host-rendered priority date disclaimed as an assumption versus an application filing date versus a company prose statement of term; the three measure different things and only one is legally operative,the filing date is attested twice (registry plus counter-signed licence) and outranks everything else; the 1997 string outranks nothing because its own publisher disclaims it; the registry's 2018-01-09 outranks the company's '2017' (inherited U-14 sides confirmed),"OPENING STAYS 1998-01-09. A 1997 priority claim is the best single explanation of the company's own 'expires in 2017' sentence and of a one-year arithmetic gap, but the carrier of the 1997 date is an automated rendering, not a certified record, so it cannot move the boundary.","whether a 1997 provisional or earlier application exists and what it claims - UNTRIED: fetch the USPTO PatentCenter / Global Dossier event history and the assignment chain for US09/004,827",Medium
```

### data_gaps.csv — `company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task
Alphabet (Google Inc.),stage1,P1GAP01 - identity of the first WebSearch licensee and of any named 1998-2001 customer,no held document of any of the five families names one; contracts of this vintage reach the corpus only as filed exhibits and none was filed,High,one sentence: 'We began licensing our WebSearch product in the first quarter of 1999' (P1SRC04),UNKNOWN,run EDGAR full-text for 'WebSearch' over 1999-2004 and fetch the counterparty-side 10-K text; queue as a scripted intake and not as agent web work (method 15.1)
Alphabet (Google Inc.),stage1,P1GAP02 - day-level founding date,the California entity's formation date lives with the California Secretary of State which no pass has queried; the S-1 gives a month only,High,'incorporated in California in September 1998' plus two month-anchored internal rows (B24 plan adoption; P1TML05 licence),UNKNOWN,queue a California SoS entity-lookup task; until then no day may be printed anywhere including the popular 1998-09-04 (inherited U-7)
Alphabet (Google Inc.),stage1,P1GAP03 - whether either founder held or abandoned a doctorate,0 occurrences of 'graduate' and 'PhD' across 348683 words of the first S-1 printing and across every held periodical byte,Medium,'created while Larry and Sergey attended Stanford University' (P1SRC04),UNKNOWN,Stanford University Archives and the Stanford technical-report series (probe Untried item 7) - UNTRIED and not absent
Alphabet (Google Inc.),stage1,P1GAP04 - any user query traffic or index-size figure for 1998-2001,the company disclosed none before it had to and no third-party measurement was reached by any family this pass used,High,the 1998 patent background's 'over 30 million searches per day' describes SOMEONE ELSE'S engine (P1QTN02),UNKNOWN,a 1999-2001 wayback capture ladder for google.com plus the still-503 www and google.stanford.edu CDX routes (P1SRC11) and the 7 unfetched in-window Yahoo Internet Life issues
Alphabet (Google Inc.),stage1,P1GAP05 - pre-IPO financing: rounds dates amounts investors,no document of any family states a financing date and the one valuation is a licence recital,High,"'a round of investor financing which resulted in a Eight Million Dollars ($8,000,000) post-money valuation' (P1SRC06; record B30)",UNKNOWN,run the probe's standing FETCH REQUEST: sec_intake auto --cik 1288776 --from 2004-08-01 --to 2006-12-31 to land the 424B4 and read its plan-of-distribution and pre-IPO-sales tables; plus PACER for the 1998 Stock Plan rescission matters
Alphabet (Google Inc.),stage1,P1GAP06 - the registration statement's file-number history (P1CNF01),two Securities Act numbers print in parallel across the held printings and no held document explains the second,Medium,the header and cover enumeration in the carrier table above,High,"query the EDGAR file-number route for both 333-114984 and 333-117934 and fetch accession -138034's text, which is index-page-only on disk"
Alphabet (Google Inc.),stage1,P1GAP07 - the GSA trial's document-indexing ceiling and the executed day of the month,OCR destroyed both in the only held copy (a corrupted date glyph and the phrase 'no more whan foouments'),Low,"the surrounding sentences, which are legible",UNKNOWN,page-image route for CREST item 0001487901 - a digitisation limit reachable only off the image layer and not off the text layer
Alphabet (Google Inc.),stage1,P1GAP08 - what CIK 1652044 (today's Alphabet) is to CIK 1288776,the one archive slice that would carry the pre-2023 history answered HTTP 404 in the probe's run,Medium,the two enumerations side by side in sources/_index/,UNKNOWN,retry index --cik 1652044 until the slice answers (inherited U-2; probe Untried item 4)
Alphabet (Google Inc.),stage1,P1GAP09 - the interior of the period: any decision memo rejected option internal failure or contemporaneous internal voice,no internal document of 1998-2001 survives in or was reached by any of the five families,High,nothing; method 2's record-selection null is the answer and not a gap to fill,UNKNOWN,recorded as a permanent null with its stated cause: this is a preservation fact about a survivor's archive. Family (e) documentary and auction records remain UNTRIED (see below).
```

---

#


---

## Volume 2 — channels, competition, scaling, money, closing blocks (§G–§U)

*Carried byte-identically from `_parts/s1_p2.md`; its 56 claim records `P2G01`–`P2U01`, §U anchor set and 8 emission blocks are intact below.*

## Header (part 2)

STATUS: WRITTEN 2026-09-29 (alphabet-s1-p2)

**Continuity.** This is volume 2 of the same document as `_parts/s1_p1.md` (method §9.3). Section letters,
claim-record ids and register-row ids **continue**; nothing here renumbers, re-opens or edits part 1. Part 1
carries §Header, §Boundary and §A–§F, **23 claim records `P1A01`–`P1F04`** and **70 register rows across nine
registers**, and adopts the stage span **1998-01-09 → 2001 (year-granular; closing day UNKNOWN)** with five
rejected rival geometries named at its `## Boundary`. This volume writes **§G–§U**, the `P2…` claim records,
and the register rows the merge still has to apply.

**Ids (part 1, Header "ID scheme", honoured exactly).** Claim records here are `P2<SectionLetter><nn>`
(`P2G01`, `P2J07`). Register rows carry the three-letter register tag with the `P2` volume prefix: sources
`P2SRCnn`, quantitative `P2QTNnn`, timeline `P2TMLnn`, decisions `P2DECnn`, validation `P2VALnn`, failures
`P2FAInn`, channels `P2CHNnn`, conflicts `P2CNFnn`, data gaps `P2GAPnn`. All are **dossier-local**; global
`source_id` blocks are minted centrally at merge (§13). Part 1's `P1CNF01`–`P1CNF07` conflict keys are **not**
re-minted. **Anchor space:** the upstream dossiers minted `U-1`–`U-5` (`research/A_chronology_feasibility.md`)
and `U-6`–`U-16` (`research/B1_filing_records.md`) in hyphen form; part 1 proposed "U-17 onward" for the merge
to mint and minted none itself. This volume mints the dot form **`U.017`–`U.036`** (§U), declares them in a machine
comment so the parity gate needs no guess (§15.5), and cites no anchor it does not declare. A
dossier may propose; only the merge re-keys.

**Tier and boundary are taken from part 1, not re-argued.** Company_005 is **T1 exemplar** for Stage 1 (§15.2:
≥3 of five corpus families return in-window Tier-1 text), read on the probe's own gloss — "T1 from the IPO end,
thin at the founding end". The span, its five rejected rivals and its four refusals (no founding day, no first
customer, no pre-IPO round, no IPO price) are at part 1 `## Boundary`; this volume works inside them and
**adds one correction to refusal (iii)** at §J.1, which is a finding about a carrier part 1 did not read, not a
re-opening of the geometry.

**What this pass actually opened.** Every citation below is a byte this pass read on this disk, in this run:
`sources/sec/0001193125-04-073639_0001193125-04-073639.txt` (5,719,779 B, the 2004-04-29 initial printing),
`…-04-105564_….txt` (2,791,396 B, Amendment No. 2), `…-04-135503_….txt` (4,675,485 B, **Amendment No. 5,
2004-08-09** — the fullest held printing and the carrier of most figures below), `…-04-134174_ds1a.htm` (the
cover-only stub amendment), `…-04-115812_d8k.htm` (the 8-K), `…-04-116608_dex2101.htm` (the subsidiary list),
`sources/periodicals/yahoo-internet-life-magazine-{july-2000, september-2001, january-2002, march-2002}_djvu.txt`,
the four `bub_gb_*` Network World text layers and their `.meta.json` sidecars,
`sources/financials/xbrl_early_series.csv`, `research/A4_harvest_mine.md`, and the two upstream dossiers'
record rows. **Reading layer:** filings were read through a tag-stripping pass (`<[^>]+>` and SGML numeric
character references removed, whitespace collapsed); where an apostrophe or quotation mark disappears because
it was an encoded entity, it is restored silently inside a quotation and never elsewhere. Line numbers are
locators, not addresses (§14 rule 12); passages are quoted verbatim from the layer described.

**Confidence (§3, part 1's wording carried).** High = 2+ independent origins or a primary document speaking
for its own date; Medium = one reliable source, or a retrospective-only primary, or anything resting on a layer
fetched over **UNVERIFIED TLS** (every periodical sidecar here says so); Low = conflicting, vague, or
retrospective-only with no primary carrier; **UNKNOWN is a preferred answer, never a hole to fill**.

---

## G

STATUS: WRITTEN 2026-09-29

### G.1 What a "channel" means for a two-sided business, and why the standard frame needed adapting

The §7 default frame (retail → stores; SaaS → pilots) does not fit this model, so the adapted equivalent is
stated: a channel here is a route by which **one of two distinct customers** was acquired — the *demand side*
(an advertiser paying money) and the *supply side* (a web site giving Google its index, or later taking a share
of an ad fee). The filing text names both populations and names a third: licensees, who bought the engine
itself. Three supply/demand routes are dated inside the window; a fourth (the AdSense revenue-share network) is
dated 2003 and is therefore `(PB)`; and the route the company later credited with acquiring its users has no
date, no carrier and no measurement at all.

### G.2 The dated routes, each with its carrier

| Route | Date on the record | Carrier and what it says | Basis / class |
|---|---|---|---|
| Wholesale licensing of the engine to other web sites | "in the first quarter of 1999"; first revenue "in 1999" | S-1 "How We Generate Revenue"; "We first derived revenue from our online search business in 1999" (Amendment No. 5) | issuer self-report, quarter granularity; FOUNDER CLAIM |
| Direct sales force selling text ads **per display** (Premium Sponsorships) | "In the first quarter of 2000" | same paragraph: "Through our direct sales force we offered advertisers the ability to place text-based ads…" | FOUNDER CLAIM |
| Self-service advertising (Google AdWords) | "In the fourth quarter of 2000, we launched Google AdWords, an online self-service program" | same paragraph; and "AdWords is also available through our direct sales force" (2004 text) | FOUNDER CLAIM |
| Advertising services as a revenue line | "…and from our advertising services in 2000" | Risk Factors, Amendment No. 5 | FOUNDER CLAIM |
| The Google Network / AdSense revenue share | 2003 onward `(PB)`; "the thousands of third-party web sites that comprise our Google Network" | Prospectus Summary; Facilities/MD&A | FOUNDER CLAIM, post-boundary |
| Free index inclusion | no date; printed 2004-04-29 | "Inclusion and frequent updating in our index are open to all sites free of charge." | part 1 §F.4 (P1F04); 1998-2001 applicability UNKNOWN |
| Word of mouth | no date, no measurement | "We have found that offering a high-quality user experience leads to increased traffic and strong word-of-mouth promotion." | FOUNDER CLAIM with zero corroborating carrier (part 1 P1CHN05) |

The **cost side of acquisition is now quantified where part 1 said it was not.** The 2004-04-29 printing's
Summary Consolidated Financial Data prints a Sales and marketing line for every year of the window: **1999
$1,677 thousand; 2000 $10,385 thousand; 2001 $20,076 thousand** (in thousands, calendar year ended 12-31,
1999-2000 outside the auditor's attested band which starts at 2001). Against net revenues of $220 and $19,108
thousand this is a ratio the record states without comment: **§G.4**. A company that later attributes its user
acquisition to word of mouth was, on its own filed numbers, spending several times its revenue on sales and
marketing in the two years it claims to have been acquiring users. Nothing in the corpus says which of those
dollars bought users and which bought advertisers, and no held document disaggregates the line — that split is
**UNKNOWN**, and it stays UNKNOWN rather than being inferred.

### G.3 First customer acquisition: what the record reaches and where it stops

Part 1 answered the first-customer question as **UNKNOWN** and perimetred it (§F.2). This pass ran the same
searches against the printings part 1 did not read and the answer does not move: **no held document names a
Google customer, licensee, advertiser or network member with an in-window start date earlier than 2000-06
(Yahoo, `(PB)` termination)**. What this pass *does* add is four adjacent facts that tighten the perimeter:

1. **The smallest unit of the sales motion is named.** "Advertisers with more extensive needs and budgets can
   request strategic support services, which include an account team of experienced professionals"; "AdWords is
   available on a self-service basis with email support"; "field sales offices in 11 countries" (Business,
   Amendment No. 5, 2004). All `(PB)` in date, but they are the only held description of *how a customer was
   actually acquired*, and they describe a hybrid: self-service intake with a paid account team above it.
2. **A sizing rule for who got bespoke treatment exists, and it is a 2004 rule.** "more than 20 million page
   views a month" was the threshold at which network/portal customization was offered (part 1 P1QTN08). No
   in-window document uses a page-view threshold at all.
3. **The enterprise route is documented only by a government test form, three years late.** The CIA-held Beta
   Evaluation Agreement for the "Google Search Appliance Pre-release Version 4.2 and 4.4" gives a 60-day
   evaluation period commencing on shipment, with the appliance returnable within ten business days
   (part 1 §E.4; P1SRC08). It is `(PB)` (2004-11) and it is the only executed Google commercial instrument in
   the corpus other than the Stanford licence. It evidences the *form* of an enterprise sales motion (evaluate
   before you buy), not its introduction date: **when the appliance channel opened is UNKNOWN.**
4. **Customer-side concentration is bounded, and the bound is audited.** "No customer accounted for greater
   than 10% of net revenues in 2001, 2002 and 2003" (audited notes) and, in the same instrument, the network
   dependence stated separately: advertising and other revenues from **one** Google Network member, "America
   Online, Inc., primarily through our AdSense programs, accounted for approximately 15%, 16% and 13% of our
   revenues in 2002, 2003 and in the six months ended June 30, 2004". Two percentages, two different
   denominators of relationship — a customer bound on the *billings* side and a channel share on the *traffic*
   side. Both `(PB)` for the window's first three years, and both the issuer's own words inside the auditor's
   band for 2002-2003.

**The honest summary of §G:** the corpus shows a company that changed *how it sold* three times inside the
window and left no record of who bought. Every acquisition fact after the mechanism sentence is 2004 print
about a 2004 business, retrospectively applied to a company whose first licensee is still nameless.

### G.4 Derived quantity, arithmetic printed (§8: never a derived value labelled as observed)

Sales and marketing expense as a multiple of net revenues, from one table in one instrument:
`1,677 / 220 = 7.62×` (1999); `10,385 / 19,108 = 0.54×` (2000); `20,076 / 86,426 = 0.23×` (2001).
Cost of revenues plus sales and marketing as a share of revenue: 1999 `(908+1,677)/220 = 11.75×`. All three are
**DERIVED, Medium**: the inputs are printed, the arithmetic is shown, the interpretation is not — a ratio of a
cost line to a revenue line in a year with $220 thousand of revenue measures a company that had not yet
converted anything into revenue, and nothing more.

### G.5 Coda and firewall (§7 duty on interpretive prose)

**Mechanism as far as evidence reaches:** each new route removed an intermediary between Google and the payer —
a licensee became an advertiser, an advertiser's purchase order became a self-service click-through campaign —
and the only dated evidence for that pattern is the issuer's own mechanism paragraph in a 2004 document.
**Alternative explanation not excluded:** the sales-and-marketing ratios above are equally compatible with
advertiser-side acquisition dominating the spend while user acquisition was genuinely unpaid, or with
public-relations and brand spend unrelated to either; the corpus cannot disaggregate the line, so it does not
claim to. **Anti-hagiography test:** had the company failed in 2003, §G would still read plausibly — a
three-times-changed revenue route, a nameless first customer, an acquisition claim with no measurement, and an
expense line larger than revenue are the ordinary shape of an unsuccessful early two-sided business, not of a
destined one. Confidence for the section as a whole: **Medium**, capped by LIN-REG; the two audited percentage
statements are the strongest rows because they sit inside the attested band, and the press-derived items are
**Medium** on the UNVERIFIED-TLS cap.

### G.6 Load-bearing claim records for §G

*(appended at the end of this volume with §H–§U, per part 1's convention of a claim record block per section —
see `P2G01`–`P2G08`.)*

---

## H

STATUS: WRITTEN 2026-09-29

### H.1 The field as the registrant printed it

The Competition section of Amendment No. 5 (2004-08-09) is the fullest in-corpus statement of the field, and it
names four kinds of rival rather than a league table:

> "We face competition from other Internet companies, including web search providers, Internet advertising
> companies and destination web sites that may also bundle their services with Internet access. In addition to
> Microsoft and Yahoo, we face competition from other web search providers, **including companies that are not
> yet known to us**."

Three further printed elements matter. **(a) The size comparison is made against itself:** "Both Microsoft and
Yahoo have more employees than we do (in Microsoft's case, currently more than 20 times as many). Microsoft also
has significantly more cash resources than we do." **(b) The competitor set changes kind mid-sentence:** Yahoo is
described as "an increasingly significant competitor, having acquired Overture Services, which offers Internet
advertising solutions that compete with our AdWords and AdSense programs, as well as the Inktomi, AltaVista and
AllTheWeb search engines" — the same Yahoo that "Since June 2000… has used, to varying degrees, our web search
technology". **(c) The ad-mechanism competition is named as a patent claim, not a market share:** the Overture
suit (filed April 2002, `(PB)`) "claims that the patent relates to Overture Services' own bid-for-ad placement
business model and its pay-for-performance technologies."

None of this is independent. All of it is LIN-REG, one instrument, and it is a 2004 description of a 2004 field
written by a company that had just become contestable in court. Its value for Stage 1 is bounded and stated:
**it tells us which rivals a registrant was willing to put its name against in an SEC document, and nothing
about who was winning in 1999.**

### H.2 The field as an unaffiliated magazine printed it, in window

Four issues of *Yahoo Internet Life* (Ziff Davis) are held as text layers. Two of them are in window.

- **July 2000** (part 1 §E.3, P1SRC07): Google ranked **4th** in a search round-up, "Our new favorite for general
  searches… uses proprietary technology to ensure that the first hits you get for your search are the best".
  Across the same issue "go to"/GoTo-adjacent strings occur on 12 lines and "excite" on 8, "lycos" on 4,
  "looksmart" on 2; "altavista", "overture", "findwhat", "fast search" and "direct hit" occur on **0** lines.
- **September 2001** (in window; 338,899 B, 14,518 lines; 7 lines contain "google"): a sites listing prints
  `NETSCAPE | LYCOS | lycos.com | EXCITE | excite.com | ALTAVISTA | altavista.com | LOOKSMART | looksmart.com |
  GOOGLE | google.com` (l.14171) — the magazine's own ordering places Google in the same class as five portal-era
  engines; a review fragment reads "GOOGLE [google.com] If we had bet money on…" (l.8459); a quote reads
  "Google searches on one thing or another, That is going to be the real long-term benefit of the Net. Some kids
  who aren't even out of high school know…" (l.8809); and a joke column asks "How many Republicans does it take
  to do a Google search?" (l.12864) — the name used as a verb phrase in consumer print inside the stage window,
  which is the closest thing this corpus holds to an organic-adoption measurement and is not a measurement.
- **January 2002** (one month past the close, `(PB)`; 285,579 B, 11,934 lines; 10 "google" lines): "'Googling,'
  the act of plugging the names of prospective mates into the Google [google.com] search … emerged this year as
  crucial dating insurance. Unconfirmed reports of 'counter-Googling'…" (l.5643-5648, OCR-degraded), and the
  rival mechanism described at length: "many of these search results come from one place: Overture
  [overture.com] (formerly known as GoTo.com), a rare dot-com success that's always been up-front about the
  yellow pages-like service it provides. In fact, each pay-for-placement search result at Overture includes a
  disclosure that tells you exactly how much the advertiser forked over for that position." (l.5600-5620 region).
- **March 2002** `(PB)`: "POWER SEARCH WITH GOOGLE" and "Google: Advanced Search Operators
  [google.com/help/operators.html]" (l.3922, l.3962) — third parties teaching the product's power-user surface.

Two nulls belong to this section as loudly as the hits. **"paid inclusion" occurs on 0 lines across all four
issues** (and no variant `pay…inclusion` line either), so the held press corpus cannot corroborate the paid-
placement controversy the filings describe; and **all four held *Network World* issues — 1998-03-30, 1998-06-22,
1999-01-11, 1999-05-10, 68,059 lines and 1,414,577 bytes measured this pass — contain 0 lines matching "google"
in any case.** The IT-industry trade press that part 1's dossier treated as a searched family returned no naming
of this company at the exact moment of its founding, and that is a measured absence over bytes, not a gap.

### H.3 The field as the inventor described it, 1998-01-09

The patent's Background (part 1 §C.1, P1SRC01) is the only *contemporaneous* statement of the field inside the
window, and it is a statement of the problem, not of a rivalry: "searches typically return hundreds of
irrelevant or unwanted documents which camouflage the few relevant ones", with commercial relevance
disclaimed: search result quality judged against "a popular search engine" handling "over 30 million searches
per day" — an engine the document does not name (P1QTN02). Where the filing's 2004 competition paragraph names
companies, the 1998 patent names techniques. Reading one into the other is the hindsight error this section
exists to refuse.

### H.4 Paths visible in the record and not taken

"Paths not taken" is the weakest category in this corpus because rejected options are precisely what a survivor
does not print (§2 record-selection null). What follows is therefore not a list of Google's rejections but a
list of **mechanisms visible in the same period whose non-adoption by Google is documented**, each with its
carrier, and each stating how far the evidence reaches.

| Mechanism, visible in period | Where it is visible | What proves Google did not take it | Reach of the claim |
|---|---|---|---|
| Selling inclusion or ranking in a search index | 1998 patent background (part 1 §C.1); July 2000 press round-up | the printed commitment: "we will not accept payment for inclusion or ranking in them" (2004) | the **commitment is dated 2004**; a 1999-2001 price list is EMPTY (searched, none held) and the commitment's in-window applicability is UNKNOWN |
| Auctioned bid-for-placement (Overture/GoTo's mechanism) | Jan 2002 press description above; Overture's own patent US 6,269,361 as pleaded in the suit | Google's first two mechanisms were priced **per display**, not per bid ("Advertisers paid us based on the number of times their ads were displayed") | non-adoption is inferable from the pricing basis; a decision record refusing the auction model does not exist in any family |
| Staying a wholesaler of search results to portals | the 1999 licensing model itself; the Yahoo arrangement from 2000-06 | the issuer's own mechanism paragraph: "Our original business model consisted of licensing… In the first quarter of 2000, we introduced our first advertising program" | the change is dated; **the reason is not** — rationale UNKNOWN (part 1 P1DEC04) |
| Keeping the terminated direct-sale program | Premium Sponsorships (2000-Q1) | the company replaced it with self-service inside four quarters and terminated it effective 2004-01-01 `(PB)` | the termination is the company's own judgment about its channel; it is `(PB)` and retrospective |
| Becoming a bundled "destination" or access-bundled site | Competition paragraph's own framing ("destination web sites that may also bundle their services with Internet access") | Google describes itself as competing *with* them, and holds no access-bundle carrier | an absence of carrier, not a decision: class INFERENCE, Low |

### H.5 Coda and firewall

**Mechanism:** the filed competitive frame is asymmetric by construction — a registration statement describes
rivals large enough to matter to underwriters and omits whatever was not material in 2004, while the held
consumer press describes whatever an editor tested that month. Neither is a market. **Alternative explanation
not excluded for every row above:** non-adoption may reflect *inability* (no auction inventory, no billing
infrastructure, no sales capacity) rather than a choice; nothing in the corpus distinguishes them, so no row
claims a choice. **Anti-hagiography test:** if this company had failed in 2003, §H would still be true — it was
a fourth-choice engine in one magazine's July-2000 round-up, unnamed in four years of the IT trade press it
ought to have appeared in, and sued in 2002 by the rival whose mechanism it did not copy. Confidence: **Medium**
for the press rows (UNVERIFIED TLS, Tier-3 under §5), **Low** for every "path not taken" row, because a
non-decision cannot be primary-documented.

### H.6 Claim records

See `P2H01`–`P2H07`.

---

## I

STATUS: WRITTEN 2026-09-29

### I.1 The scaling decision, stated as the record states it

Part 1's boundary adopts the close at "2001 (year-granular)" on the strength of the issuer's own sentence
("We became profitable in 2001", P1TML14) and of two mechanism launches in 2000 (§D.3, part 1). Read against
the hiring and infrastructure evidence this pass collected, the scaling act inside the window is not a headcount
event — headcount inside the window is **UNKNOWN** — but a **role** event: the company installed, in
1999-05 → 2001-07, a sales executive, an engineering executive, an outside chief executive and two venture
directors, and it did so before the first year it calls profitable.

| Act | Date on the record | Carrier (all LIN-REG unless noted) | Class / confidence |
|---|---|---|---|
| 1998 Stock Plan adopted by the board | September 1998 | Employee Benefit Plans ("Our 1998 Stock Plan was adopted by our board of directors in September 1998") | FOUNDER CLAIM (month); Medium — part 1 B24 anchor |
| Omid Kordestani, SVP of Worldwide Sales and Field Operations | since **May 1999**; prior: "Vice President of Business Development at Netscape" 1995-1999 | Management bio | FOUNDER CLAIM (month); Medium. The dated arrival of a professional sales function, from a rival-adjacent portal-era company |
| L. John Doerr joins the board | since **May 1999**; "General Partner of Kleiner Perkins Caufield & Byers… since August 1980" | Management bio | FOUNDER CLAIM (month); Medium |
| Michael Moritz joins the board | since **May 1999**; "General Partner of Sequoia Capital, a venture capital firm, since 1986" | Management bio | FOUNDER CLAIM (month); Medium |
| Wayne Rosing, VP of Engineering | since **November 2000**; prior CTO of Caere Corporation 1996-11 → 2000-04 | Management bio | FOUNDER CLAIM (month); Medium |
| Eric Schmidt, Chairman of the board **from March 2001**; Chief Executive Officer **since July 2001** | March 2001 / July 2001; prior: Chairman of Novell April 1997-November 2001, its CEO to July 2001 | Management bio | FOUNDER CLAIM (months); Medium. The single largest documented scaling act in the window and the only one with two dates |
| Schmidt's option exercise and its financing | **September 28, 2001**: full recourse promissory note ~**$4.3 million**, secured by 14,331,708 Class B shares, interest **7.38%** compounded semi-annually; repaid in full 2004-04-28 | Certain Relationships and Related Party Transactions, "Indebtedness of Management" | FACT (executed instrument described by the counterparty-registrant); Medium — one lineage, no instrument copy held |
| First office outside the United States | "We opened our first office outside the U.S. in **2001**" | Risk Factors | FOUNDER CLAIM (year); Medium |
| AdWords self-service launch | fourth quarter 2000 | §D.3 / part 1 P1TML13 | FOUNDER CLAIM; Medium |

Two properties of this table must be stated rather than smoothed. **First**, every date is a *month* or a *year*
inside a 2004 document: none is a day-level act, and the corpus holds no appointment letter, board minute,
offer memo or org chart. **Second**, the window's own headcount is unrecoverable — the first headcount the corpus
prints is **1,907 at March 31, 2004** ("At March 31, 2004, we had 1,907 employees, consisting of 596 in research
and development, 961 in sales and marketing and 350 in general and administrative"), and Amendment No. 5 moves
the same sentence to **2,292 at June 30, 2004 (705 / 1,141 / 446)** while quietly adding a qualifier the April
printing did not carry: employees "…**, except temporary employees and contractors**, are also equityholders",
against April's unqualified "All of Google's employees are also shareholders". A re-filed instrument that
narrows its own equity-ownership claim is a lineage-internal revision; it is recorded at **U.028**, not smoothed.

### I.2 Infrastructure acts, and the boundary of what "infrastructure" can mean here

Nothing in the corpus describes the 1999-2001 machine room. The word "data centers" appears only in 2004 print:
"We operate data centers in several domestic and international locations" (Business, April printing),
"We operate data centers in the United States and the European Union pursuant to various lease agreements and
co-location arrangements" (August printing), and, as forward statement rather than history, "In 2004, we expect
to spend substantial amounts to purchase or lease data centers and equipment and to upgrade our technology and
network infrastructure… This expansion is going to be expensive and complex and could result in inefficiencies
or operational failures" (Risk Factors). Server counts, bandwidth, index size, cost per query: **UNKNOWN**, and
no family this pass reached supplies them.

The earliest *quantified* infrastructure commitments the corpus holds all sit at 2003-12-31, one year past the
close, and are labelled `(unaudited)` in the instrument: guaranteed minimum revenue share payments
**$477.0 million** (of which $205.1 million due within 12 months), operating lease obligations **$146.7
million**, capital lease obligations **$7.4 million** ($6.6 million principal plus $0.8 million interest,
through October 2005), purchase obligations **$11.9 million**, total contractual obligations **$644.5 million**
(in millions; table basis "Payments due by period"). Facilities at the same date: "We lease approximately
**506,000 square feet** of space in our headquarters in Mountain View, California under a lease that expires in
2012", plus named leased offices in 23 cities from Amsterdam to Zurich. The August 2004 sublease exhibits inside
accession -073639 (dex1002/dex1003) print the landlord-side geometry of the same estate — "Four buildings
including **506,317 square feet** of Rentable Area" — which is the second time in this dossier that a real
estate document contradicts a prose summary by a rounding. The prose figure is 506,000; the exhibit figure is
506,317; both are Google's own, and the exhibit is the primary instrument.

Group structure at the same late date: Exhibit 21.01 (filed 2004-07-12) lists **15 named wholly-owned
subsidiaries** — the operating national entities (Australia, Canada, France SARL, Germany GmbH, Ireland
Holdings, Ireland Limited, Italy S.R.L., Japan KK, Korea LLC, Netherlands BV, Netherlands Holdings BV, India
Private Limited, Spain SL, Switzerland GmbH, UK Limited) plus Google International LLC, Google LLC, and four
acquired corporations named as entities: **Applied Semantics, Inc.; Kaltix Corporation; Neotonic Software
Corporation; Orkut.com LLC**. All `(PB)`; retained because §Q needs to say what the platform became, and because
the acquired-corporation list is the earliest held naming of growth-by-acquisition as a *legal* act.

### I.3 What the scaling evidence does not show

The corpus cannot date a management layer, a hiring wave, a first office move, a first server purchase, or the
point at which the company stopped being two people and a contractor: no headcount line, no facilities line and
no payroll line exists for 1998-09 → 2001-12 except the officer titles in §I.1. **In-window cash is now
recoverable, in-window people are not** (§J.1), and the asymmetry is worth naming: a registration statement is
built to prove liquidity and control, not to enumerate a workforce that was not yet a risk factor. The one
in-window internal-capability claim with any structure attached is the founder's letter's "20% of their time"
policy, and it is a 2004 statement about a later company: "Many of our significant advances have happened in
this manner. For example, AdSense for content and Google News were both prototyped in 20% time." Nothing
supports its application to 1999-2001 — the two products it names are 2003 and 2002 respectively `(PB)`.

### I.4 Coda and firewall

**Mechanism:** the documented scaling acts are *role appointments and one dated financing instrument attached to
an appointment*, which is what a filing is obliged to disclose; headcount and plant are the parts it was not.
**Alternative explanation not excluded:** the March/July 2001 chief-executive arrival may have been forced by
investors, by the founders' own preference, or by the collapse of the licensing market; the instrument says none
of these, so §P records the rationale as UNKNOWN rather than adopting the standard telling. **Anti-hagiography
test:** an 18-month sequence of outside-hire dates, an executive borrowing $4.3 million from the company he had
just joined, and an unaudited 2003 obligation table totalling $644.5 million reads as a normal scaling company,
not as a destined one. Confidence: **Medium** throughout, capped by single-lineage LIN-REG; **High** only for
the exhibit-versus-prose 506,000/506,317 discrepancy, which is two documents saying different things on this
disk and both readable.

### I.5 Claim records

See `P2I01`–`P2I09`.

---

## J

STATUS: WRITTEN 2026-09-29

### J.0 Correction to part 1's Boundary refusal (iii)

Part 1's `## Boundary` §3 refuses to name "no pre-IPO funding round" and says "the closest the corpus comes is a
*valuation recital*" (`$8,000,000` post-money, inside the Stanford licence). Against the printings part 1 read
that is true. Against the printings this pass read it is **not the closest thing**: the MD&A liquidity paragraph
of the 2004-04-29 printing — repeated verbatim in Amendment No. 2 and Amendment No. 5 — states an **aggregate
amount of private equity money taken in**. The refusal of a *round* (date, subscribers, price per round) stands;
the statement that the corpus holds no money quantum for the pre-IPO period is retracted here, in the same pass
that read it (§14 rule 8). The retraction is carried into the registers as `P2CNF08`/`U.024` and as the
`P1GAP05` supersession note.

### J.1 The one aggregate, and the cash ladder

> "Since inception, we have financed our operations primarily through internally generated funds, **private sales
> of preferred stock totaling $37.6 million** and the use of our lines of credit with several financial
> institutions." — Liquidity and Capital Resources, identical in -073639 (2004-04-29), -105564 and -135503.

Basis: cumulative from September 1998 inception to the reporting date; company-prepared; inside the auditor's
attested band only for the years 2001-2003, and the sentence itself is narrative, not a statement line. It is
**the only total the corpus prints for pre-IPO equity financing**. No round is dated, no subscriber is named
against an amount, and no per-round price is printed outside §J.3. Three printings carrying it are one lineage:
corroboration = 1.

The same paragraph prints a period-end cash ladder that reaches into the window: "At December 31, 2003, we had
**$334.7 million** of cash, cash equivalents and short-term investments, compared to **$146.3 million and $33.6
million at December 31, 2002 and 2001**, respectively" (Amendment No. 5 adds the June 30, 2004 figure of $548.7
million). **$33.6 million at 2001-12-31 is an in-window balance**, stated by the issuer, of a defined aggregate
(cash *plus* equivalents *plus* short-term investments — not cash alone), at period end, in millions rounded to
one decimal. It is the nearest the corpus comes to a dated money fact about the stage close, and it is part 1's
P1GAP-adjacent "no operating detail for 1998-2000" partly repaired — while headcount, cost per unit and users
for those years stay absent. Unused letters of credit at 2003-12-31: "approximately $12.2 million" `(PB)`.

### J.2 The preferred ladder, as filed

The capitalization note (Amendment No. 5) prints eight series, in thousands of shares, at two period ends, with
an aggregate liquidation preference:

| Series | 2002-12-31 authorised / issued | 2003-12-31 authorised / issued | Aggregate liquidation preference |
|---|---|---|---|
| A | 15,360 / 15,360 | 15,360 / 15,360 | (combined $40,815 thousand) |
| A-1 | — | 15,360 / 15,360 | |
| B | 50,651 / 49,823 | 50,445 / 49,823 | |
| B-1 | — | 50,651 / 50,445 | |
| C | 10,000 / 5,249 | 9,149 / 6,479 | |
| C-1 | — | 10,000 / 9,149 | |
| D | — | 7,437 / 7,437 | |
| D-1 | — | 7,437 / 7,437 | |
| Totals | 166,896 / 70,432 | 164,782 / 71,662 | **$40,815 thousand** |

Basis: thousands of shares; legal rather than as-if-converted; the "-1" series pairs appear at 2003-12-31
against their un-suffixed parents at 2002-12-31, which is the **2003 Delaware reincorporation's recapitalisation
visible in a share column** (part 1 §B.4's CA→DE break, now with a documentary trace) — read that as an
INFERENCE, Medium, because no held note explains the suffix. Each preferred share converts automatically into
one Class B common share at the offering closing; every share and per-share figure in the instrument is
"retroactively restated to reflect the stock split as if such split had taken place at the earliest date
presented", the splits being "In February and June 2003… separate two-for-one stock splits" plus "other splits
in prior years" that are **not dated**. That last clause is the reason no pre-2003 per-share figure in this
dossier may be called contemporaneous (§S).

### J.3 The one priced share sale inside the window

Two dated price data points exist for the window, both from related-party disclosures rather than from a
financing note:

- **2001-07-13 — Series C preferred stock, 426,892 shares, purchase price printed as $999,994.51, at
  "$2.3425 per share"** (Certain Relationships and Related Party Transactions; buyer Eric Schmidt). Derived
  check, shown per §8: `426,892 × 2.3425 = 999,994.51` — the printed total and the printed unit price foot
  exactly. So the Series C price inside the window is $2.3425 per share **as applied to one officer's
  purchase**, not as published for a round; whether other purchasers paid it is UNKNOWN.
- **1998 Plan option pricing at the other end of the ladder:** "At June 30, 2004, options to purchase a total of
  6,295,431 shares of Class B common stock were outstanding under the 1998 Stock Plan at a **weighted average
  exercise price of $0.29 per share**", and Schmidt's separate option was exercisable at **$0.30**. Basis:
  weighted average across a plan, at a post-boundary date, for grants beginning 1998-09. It is a founding-era
  price *aggregate*, not a founding-era price.

**No term sheet, no stock purchase agreement, no investors' rights agreement and no signature page is held for
this company.** The brief for this volume named the Nvidia analogue — Ex-4.3's counterparty signature pages
reciting a 1994-12-19 original IRA and naming the holders — and asked for Alphabet's equivalent. Measured
against held bytes, it does not exist here: **"Sutter Hill" and "Khosla" return 0 occurrences** across the three
printings read (4.68M, 5.72M and 2.79M bytes), and "Sequoia" returns only (i) a director biography, (ii) a
beneficial-ownership footnote, and (iii) fund-name enumerations. **What the Alphabet record can actually cite is
a 2004 registrant's own list of which funds were 5% holders after an offering it had not yet priced** — not
instrument text, not signature pages, and not a round. That is stated as the finding.

### J.4 Investors the record names, and the strength of each naming

| Named holder | Where named | What it proves | What it does not |
|---|---|---|---|
| "Entities affiliated with Kleiner Perkins Caufield & Byers" | Principal Stockholders table, Amendment No. 5 | an affiliated group held a 5%+ block as stated by the registrant in 2004 | which entities, when they bought, at what price |
| "Entities affiliated with Sequoia Capital" | same | as above; footnote enumerates "Sequoia Capital VIII… Sequoia International Technology Partners VIII(Q)… CMS Partners LLC… Sequoia 1997" | the amount invested |
| L. John Doerr; Michael Moritz | Management, "since May 1999" | two venture general partners were directors from 1999-05 | that their firms' money arrived in that month |
| Yahoo! Inc. | Principal Stockholders; Legal Proceedings; "a warrant held by Yahoo to purchase **3,719,056 shares**"; "2,700,000 shares of Class A common stock issued to Yahoo! Inc. in connection with a settlement" | a customer, a competitor and a warrant holder at once; the warrant's existence is also carried by the balance sheet line "Redeemable convertible preferred stock warrant $13,871" at 2004-03-31 (part 1 B16) | the warrant's original exercise terms, and the 2004 settlement is `(PB)` |
| Board of Trustees of the Leland Stanford Junior University | Exhibit 10.10 (executed bilateral instrument) | shares of Series A Preferred were issued to Stanford 1999-04-14, quantity `[***]`, tied by recital to a round with an $8,000,000 post-money valuation | any cash amount, any share count, any date of the round |
| Eric Schmidt | Related-party note | a named individual paid $999,994.51 for Series C on 2001-07-13 and borrowed ~$4.3M from the company on 2001-09-28 | that he is a venture investor rather than an officer |
| Gilad Elbaz | Principal Stockholders (1,046,834 Class A shares, 7.0%) | a named individual holding block appears in the table | his role, in the held text of this pass (a former officer; the corpus here does not say so in the lines read) |

### J.5 What the ladder cannot do

The instrument's own dilution and capitalization geometry is post-boundary: the pro forma balance sheet at
2004-06-30 gives cash and short-term investments **$548,687 thousand actual / $2,215,334 thousand pro forma as
adjusted** at "an assumed initial public offering price of $121.50 per share", total assets
1,328,022 / 2,994,669, total stockholders' equity 1,016,999 / 2,683,646, deferred stock-based compensation
(352,815), and 39,695,863 Class A plus 231,523,780 Class B shares outstanding after the offering. The $121.50 is
**an assumption printed to compute dilution**, and part 1's Boundary §3 (iv) is right: the document carrying the
actual price — the 424B4 of 2004-08-19 — is **not held**. Nothing in §J is a valuation of the company inside the
window; the only valuation ever printed for the window is the licence's `[***]`-adjacent $8,000,000 recital, and
a recital written by a counterparty's lawyers about a round they did not price is evidence that the number was
agreed, not that it was worth it.

### J.6 Coda and firewall

**Mechanism:** the money facts that survive are (i) one cumulative equity total, (ii) one period-end cash
ladder reaching 2001-12-31, (iii) one priced share purchase dated inside the window, and (iv) a named-fund
ownership table dated 2004; there is no per-round record. **Alternative explanation not excluded:** $37.6
million could be concentrated in one 2003 round or spread across five; the preferred ladder's *pattern* of
authorised-versus-issued movement is the only structural hint and it is 2002-base-year onwards, so the window's
first three years are unilluminated. **Anti-hagiography test:** a company that funded itself on $37.6 million of
preferred, $33.6 million of period-end cash and bank letters of credit, whose chief executive borrowed from it
to buy his options, and whose earliest dated share price is an officer's $2.3425, is an ordinary 2001 venture
business. Confidence: **Medium** on every LIN-REG row; **High** only where a figure foots arithmetically against
another printed figure in the same instrument (the $2.3425 × 426,892 check; the ladder's 2001/2002/2003
monotonicity), and those checks are printed in §M with their arithmetic.

### J.7 Claim records

See `P2J01`–`P2J08`.

---

## K

STATUS: WRITTEN 2026-09-29

**Three verdicts are used in this section and must not be collapsed.** **EMPTY** = a route was run against a
defined perimeter and returned nothing (a finding). **UNANSWERED** = the route refused, 4xx/5xx'd, or returned
zero bytes (no finding either way). **UNTRIED** = never attempted in this or any earlier pass (a debt, listed
with its command in `## Untried`). Part 1's P1SRC11 already establishes that four Wayback CDX queries 503'd and
that the USPTO trademark route 405'd: those stay UNANSWERED and are not re-listed as nulls.

### K.1 What this volume tried and could not settle

| # | Question | Verdict | What was searched / why it stops |
|---|---|---|---|
| 1 | Identity of the first licensee or any in-window customer | **EMPTY** (perimeted again this pass over the two printings part 1 did not read) | no document of any family names one; the audited note gives a ceiling, not a list |
| 2 | Founding day | **EMPTY**, and remains so | the day lives with the California Secretary of State, unqueried by every pass to date (part 1 P1GAP02); no held carrier prints it |
| 3 | Dates, amounts and subscribers of the pre-IPO rounds | **EMPTY** as to per-round data; one cumulative total now exists ($37.6M, §J.1) | no stock purchase agreement or term sheet is held; the F-pages carry Google's preferred *totals*, not its round history |
| 4 | Headcount, users, queries, index size, servers for 1998-09 → 2001-12 | **EMPTY** for people/users/plant; **partly settled** for money (cash at 2001-12-31) | the 2004 income statement prints costs but no operating statistic; XBRL supplies nothing in window (§K.3) |
| 5 | What the venture investors paid and when | **EMPTY**; the only in-window price is an officer's purchase at $2.3425 | the beneficial-ownership table's column geometry is not recoverable from the tag-stripped layer (§K.4) |
| 6 | Whether Google considered an auction/bid model before 2002 | **EMPTY** — no internal document of any kind survives | §2 record-selection null; the only adjacent evidence is the rival's patent pleading |
| 7 | Whether the 1998 prototype was operated by the company or by Stanford | **EMPTY** and unresolvable from held bytes | part 1 P1CNF06; the `google.stanford.edu` CDX query 503'd, so even that host's capture history is UNANSWERED |
| 8 | The actual IPO price and first trading day | **UNANSWERED by custody** — the 424B4 (2004-08-19) exists in the enumeration and is **not held on disk** | re-verified again this pass across all 131 files under `sources/`; the fetch is a scripted intake job, not agent web work (§15.1) |
| 9 | What CIK 1652044 (Alphabet) is to CIK 1288776 (Google) | **UNANSWERED** | the archive slice answering it HTTP 404'd in the probe's run (part 1 P1GAP08) |
| 10 | The file-number history of the registration statement | **EMPTY as to cause** | two Securities Act numbers print across the held printings with independent amendment counts (part 1 P1CNF01, unresolved and still unresolved); accession -138034 is index-page-only, so its number is **UNTESTED**, a coverage hole not an absence |
| 11 | Whether the "20% time" policy existed inside the window | **EMPTY** | the sentence is 2004 and its two named products are 2002/2003 `(PB)` |
| 12 | Whether the rescission exposure was ever paid | **EMPTY** inside the stage | only the offer and its computed ceiling are printed |

### K.2 Two internal-geometry problems that limit §J and §M

**(a) The beneficial-ownership table cannot be used by this pass.** In the 2004-04-29 printing the 5%-stockholders
rows print `KPCB Holdings Inc. 23,893,800` and `Sequoia Capital 23,893,800` — the *same* figure against both
names; in Amendment No. 5 the same section prints `Entities affiliated with Kleiner Perkins Caufield & Byers
21,043,711` and `Entities affiliated with Sequoia Capital 23,893,800`. Both readings are of the same multi-column
table (Class A / Class B / % of class / % of voting power / shares being offered, several times over) whose
column boundaries are carried by markup this pass stripped. **Verdict: UNANSWERED on the held layer** — no share
count from that table is used as a quantity anywhere in this volume, and the discrepancy is filed as `U.026`
rather than resolved. The correct route is a table-aware parse of the exhibit's HTML, which is scripted work.

**(b) The MD&A percentage-of-revenues table does not reconcile.** The August printing's ratio table prints
headers `Year Ended December 31 | Three Months Ended | Six Months Ended June 30` over seven value columns; the
absolute table above it foots exactly to its own totals (checked: `14,228+16,500+20,076+12,275+12,383 = 75,462`
for 2001) but the ratio rows cannot be matched column-for-column from the stripped text
(`Cost of revenues 16.5 | 29.9 | 42.7 | 48.4 | 46.6 | 36.5 | 47.5`). **Every percentage in §M is therefore taken
from the absolute table or from a prose sentence, never from the ratio table.** Verdict on the ratio table:
UNANSWERED as presented.

### K.3 The XBRL family, measured rather than assumed

`sources/financials/xbrl_early_series.csv` holds **one data row**: `StockholdersEquity, USD, , 2006-12-31,
17039840000, 2009, FY, 10-K, , CY2006Q4I, 0001193125-10-030774`. It is a 2010-filed 10-K's frame value for a
2006 instant — five years past the close — and its own `fy` (2009) and `end` (2006-12-31) fields disagree.
**Verdict: the XBRL family returns nothing for Stage 1** (EMPTY, with the cause named), and the row is recorded
here so no later pass mistakes an empty series for an unsearched one. A secondary observation for the tool
owner: a "financials" sidecar whose `start` cell is blank while `end` carries the period instant, with `fy`
pointing at the frame's filing year rather than the reported year, will mislead any reader who trusts the column
names — reported as a defect, not worked around.

### K.4 What a reader will expect that this corpus does not contain

No internal Google document of 1998-2001 exists in any of the five families (part 1 Header, record-selection
null; re-confirmed by this pass's searches over the printings part 1 did not read). No pricing sheet, no
advertiser list, no licensee list, no office lease dated inside the window, no board minute, no org chart, no
photograph, no product screenshot other than 212 bytes of HTML. The corpus's whole in-window non-company
evidence base is unchanged in kind from part 1's count — a patent register entry, an archive capture, and
consumer press — **with periodical coverage now extended by three issues and four Network World numbers**
(§H.2), which strengthens the null rather than the narrative.

### K.5 Coda

**Mechanism:** every item above fails for one of two reasons — the company was not yet required to say it, or the
party that would have said it never entered the record. **Alternative explanation not excluded:** none is
needed; these are custody facts. **Confidence:** the section makes no positive claim, so its confidence
statement is about completeness: the searches reported EMPTY were run against named files and named terms, and
the routes not run are in `## Untried` with their commands.

---

## L

STATUS: WRITTEN 2026-09-29 — the hindsight firewall, stated as a refusal list

### L.1 What this volume is explicitly NOT claiming

1. **Not claiming the licensing model was failing.** FY1999 revenue $220 thousand and FY2000 $19,108 thousand are
   totals with no split by mechanism; the first mechanism split any held document prints is the 2004 sentence
   "Advertising revenues made up 77%, 94%, 97% and 98% of our revenues in 2001, 2002, 2003 and in the six months
   ended June 30, 2004" — which begins **at the stage's closing year** and says nothing about 1999-2000.
2. **Not claiming the advertising pivot caused profitability.** "We became profitable in 2001 following the
   launch of our Google AdWords program" is a conjunction, not a mechanism (part 1 P1VAL06). This volume adds
   the filed losses that make the sentence meaningful — net loss `(6,076)` and `(14,690)` thousand for 1999 and
   2000, net income `6,985` thousand for 2001 — and still does not assert causation, because stock-based
   compensation of `12,383` thousand in 2001 exceeds the reported net income, so on what basis "profitable" was
   concluded is itself unresolved (§S.4; `U.022`).
3. **Not claiming the rivals named in 2004 were the rivals that mattered in 1999.** The Competition section is a
   2004 field. The in-window independent field, per §H.2, is a magazine that ranked Google fourth in July 2000
   and listed it beside Netscape, Lycos, Excite, AltaVista and LookSmart in September 2001.
4. **Not claiming user adoption from press verb-usage.** "do a Google search" (Sep 2001) and "'Googling'…
   emerged this year" (Jan 2002) are language evidence, not adoption measurement. No query, visit or user count
   exists in the corpus for any in-window date.
5. **Not claiming the venture firms funded the founding.** The record dates their *directors* to May 1999 and
   their *blocks* to 2004. Between those two dates the corpus prints nothing about Sequoia's or Kleiner Perkins'
   money. Any "Sequoia funded Google in 1999" sentence is unsupported here and is not written here.
6. **Not claiming the Stanford licence was the company's only technology right, or that the exclusivity terms
   inside the window match the 2003 restated agreement.** The held exhibit is the amended and restated instrument.
7. **Not claiming a first office, a first server, a first hire below officer level, or a first employee.**
   Headcount inside the window is UNKNOWN; the 1998 Stock Plan's existence is not a hiring count.
8. **Not claiming the 1998 prototype's two hostnames mean an A/B test** (part 1 §D.5, P1CNF06) and not claiming
   `alpha.google.com` was a company asset.
9. **Not claiming the IPO was good for the company or its users.** Nothing in §J-§Q evaluates the offering.
10. **Not treating Applied Semantics' audited numbers as Google's.** They are in the same file. §M refuses them
    explicitly.

### L.2 Where the corporate timeline is company self-narrative

Every dated beat of the Stage-1 story except three is the issuer's own retrospective prose, printed in one
2004 instrument: **incorporation (September 1998), WebSearch licensing (1999-Q1), Premium Sponsorships
(2000-Q1), AdWords (2000-Q4), first profitable year (2001)** are LIN-REG/LIN-FOUNDER self-report at month-or-year
granularity. The three non-self-narrative dates are: **1998-01-09** (a registry entry naming another party's
inventor), **1998-11-11 18:45:51** (an unrelated crawler's capture), **1998-12-01 / 1999-04-14 / 2000-04-17**
(an executed bilateral instrument co-signed by a university). Everything in §G, §H, §I and §J of this volume sits
in the first category. That is not a reason to discount it — a filing is a legally signed statement — but it is
a reason to cap it at Medium and to refuse to call any of it contemporaneous.

### L.3 The record-selection null, restated for the sections this volume writes

§I can name four executives' arrival months and cannot name one rank-and-file hire; §J can name a cumulative
$37.6 million and cannot name a round; §G can describe three sales mechanisms and cannot name a customer; §O can
quote the company admitting that "most risky projects fizzle" and cannot cite a single project it killed. The
archive kept what a securities lawyer needed and what a journalist printed, and it kept neither completely.

### L.4 Anti-hagiography test, applied to this volume

Would §G–§U still read as plausible if Google had failed in 2003? Tested per section (§G.5, §H.5, §I.4, §J.6,
§M.5, §O.5, §Q.4): each asserts a record property — mechanism changes with quarter-level dates, unaudited
totals, a fourth-place ranking in a consumer magazine, four outside appointments, one aggregate of private
money, one priced officer purchase, one rescission ceiling, one patent suit — and none asserts that these facts
pointed anywhere. The words "inevitable", "visionary" and "disruptive" appear nowhere in this volume outside
quotation marks belonging to someone else, and the only superlative this pass found in the company's own 2004
copy ("a rare dot-com success") belongs to a magazine writing about a competitor.

---

## M

STATUS: WRITTEN 2026-09-29

**Basis discipline.** Every row states: carrier (the file on this disk), basis (fiscal vs calendar — this
company reports calendar years ended December 31; period-end vs average; gross vs net vs face; thousands vs
millions), and **CONTEMPORANEOUS** (the document's own date is the event's date) vs **RESTATED** (a later
document restating an earlier period) vs **RETROSPECTIVE NARRATIVE** (a later document describing an earlier
state in prose). §8's four cells are present in every row (Variable = Metric, Value, Source, Confidence).

### M.1 Numbers inside the stage window

| ID | Date | Metric | Value | Unit | Carrier (file, this pass) | Source date | Basis | Class | Conf |
|---|---|---|---|---|---|---|---|---|---|
| P2QTN01 | 1999-12-31 | net revenues | 220 | $ thousands | `sources/sec/…-04-073639_….txt` Summary Consolidated Financial Data | 2004-04-29 | calendar year ended 12-31; **net** presentation; unaudited band | FOUNDER CLAIM (restated narrative) | Medium |
| P2QTN02 | 2000-12-31 | net revenues | 19,108 | $ thousands | same table | 2004-04-29 | as above | as above | Medium |
| P2QTN03 | 2001-12-31 | net revenues | 86,426 | $ thousands | same table, identical in -135503 | 2004-04-29 / 2004-08-09 | calendar year; **identical on both sides of the gross/net change** | FACT (auditor's band covers 2001) | High |
| P2QTN04 | 1999-12-31 | net loss | (6,076) | $ thousands | 073639 selected data | 2004-04-29 | calendar year; unaudited band; before the auditor's report | FOUNDER CLAIM | Medium |
| P2QTN05 | 2000-12-31 | net loss | (14,690) | $ thousands | same | 2004-04-29 | as above | FOUNDER CLAIM | Medium |
| P2QTN06 | 2001-12-31 | net income | 6,985 | $ thousands | same; identical in -135503 | 2004-04-29 | calendar year; **inside** the auditor's band | FACT (attested figure, retrospective carrier) | High |
| P2QTN07 | 2001-12-31 | income from operations | 10,964 | $ thousands | same | 2004-04-29 | calendar year | FACT (band) | High |
| P2QTN08 | 1999 / 2000 / 2001 | sales and marketing expense | 1,677 / 10,385 / 20,076 | $ thousands | same | 2004-04-29 | calendar year; unaudited 1999-2000 | FOUNDER CLAIM / FACT band split | Medium |
| P2QTN09 | 1999 / 2000 / 2001 | cost of revenues | 908 / 6,081 / 14,228 | $ thousands | same | 2004-04-29 | calendar year; **net** presentation | FOUNDER CLAIM | Medium |
| P2QTN10 | 1999 / 2000 / 2001 | research and development | 2,930 / 10,516 / 16,500 | $ thousands | same | 2004-04-29 | calendar year | FOUNDER CLAIM | Medium |
| P2QTN11 | 1999 / 2000 / 2001 | general and administrative | 1,221 / 4,357 / 12,275 | $ thousands | same | 2004-04-29 | calendar year | FOUNDER CLAIM | Medium |
| P2QTN12 | 2000 / 2001 | stock-based compensation | 2,506 / 12,383 | $ thousands | same row; **the 1999 cell is blank in the filed table** | 2004-04-29 | calendar year; positions recovered by footing | DERIVED | Medium |
| P2QTN13 | 2001-12-31 | cash, cash equivalents and short-term investments | 33.6 | $ millions | -135503 Liquidity and Capital Resources | 2004-08-09 | **period-end**; a three-part aggregate, not cash alone | FOUNDER CLAIM (inside band) | Medium |
| P2QTN14 | 1998-09 → 2004 | private sales of preferred stock, cumulative | 37.6 | $ millions | 073639 / -105564 / -135503, identical sentence | 2004-04-29 → 2004-08-09 | **cumulative since inception**, not a year; one lineage | FOUNDER CLAIM | Medium |
| P2QTN15 | 2001-07-13 | Series C preferred purchase, 426,892 shares | 999,994.51 (at $2.3425/share) | $ | 073639 Certain Relationships | 2004-04-29 | transaction price; officer purchase, not a published round price | FACT (single-lineage) | Medium |
| P2QTN16 | 2001-09-28 | CEO promissory note principal / rate | ~4.3 million at 7.38% semi-annual compounding | $ | 073639 "Indebtedness of Management" | 2004-04-29 | principal amount, "approximately"; secured by 14,331,708 Class B shares | FACT (single-lineage) | Medium |
| P2QTN17 | 1998-09 → 2004-06-30 | 1998 Stock Plan options outstanding / WAEP | 6,295,431 / $0.29 | shares / $ per share | -135503 Employee Benefit Plans | 2004-08-09 | weighted-average across the plan; **restated for un-dated prior splits** | FACT (as filed) | Medium |
| P2QTN18 | 2001 | advertising share of revenues | 77 | percent | -135503 MD&A | 2004-08-09 | percent of that year's revenues; the balance is licensing, enterprise search, appliance and other | FOUNDER CLAIM (band year) | Medium |
| P2QTN19 | 2001 | first office outside the U.S. opened | 1 (event, year-granular) | — | -135503 Risk Factors | 2004-08-09 | company self-report, year only | FOUNDER CLAIM | Medium |
| P2QTN20 | 1998-09 → 2001-12 | **headcount, users, queries, index size, servers** | **UNKNOWN** | — | no carrier in any family | — | — | UNKNOWN | — |

### M.2 Numbers that bound the window from outside (retained as consequences, `(PB)`)

FY2002 347,848 (net, April printing) versus 439,508 (gross, August printing); FY2003 961,874 versus 1,465,934 —
same table, different presentation; the deltas `439,508 − 347,848 = 91,660` and `1,465,934 − 961,874 = 504,060`
appear identically in cost of revenues (`131,510 − 39,850` and `625,854 − 121,794`), so **the reclassification is
margin-neutral to the dollar** (DERIVED, High as arithmetic, Medium as interpretation: the moved amount is the
corpus's inference, the two presentations are filed). Also `(PB)`: cash $146.3M (2002) and $334.7M (2003);
headcount 1,907 (2004-03-31) → 2,292 (2004-06-30); advertising share 94% (2002) → 97% (2003) → 98% (H1-2004);
international revenue 22% (2002) → 29% (2003); Yahoo agreement <3% of FY2003 revenues and <2% of H1-2004; AOL
~15%/16%/13% of revenues 2002/2003/H1-2004; contractual obligations at 2003-12-31 (unaudited, in millions)
477.0 guaranteed minimum revenue share / 146.7 operating leases / 7.4 capital leases / 11.9 purchase
obligations / 1.5 other = 644.5 total; 506,000 sq ft (prose) versus 506,317 sq ft (sublease exhibit);
18,681,260 employee options granted in 2003; rescission ceiling $34M (April) revised to $25.9M (August);
Yahoo warrant 3,719,056 shares and $13,871 thousand warrant liability at 2004-03-31.

### M.3 Counts this pass made over bytes (High permitted: these are measurements, not print facts)

`0001193125-04-073639_…txt` 5,719,779 B; `…-135503_…txt` 4,675,485 B, 153,452 words after stripping;
`…-105564_…txt` 2,791,396 B; the four Network World layers 1,414,577 B and 68,059 lines with **0** lines
matching "google" case-insensitively; YIL September 2001 338,899 B / 14,518 lines / 7 google-lines; YIL January
2002 285,579 B / 11,934 lines / 10; YIL March 2002 258,574 B / 10,156 lines / 10; YIL July 2000 361,043 B /
16,051 lines / 5; "Sutter Hill" and "Khosla" **0** occurrences in all three printings; "8,000,000" **0**
occurrences in the S-1 text (it exists only in the Exhibit 10.10 recital).

### M.4 Numbers refused, with the reason

| Refused value | Where it is visible | Why refused |
|---|---|---|
| Applied Semantics, Inc. FY2002 balance sheet: total assets $6,218 thousand; cash $1,953 thousand; Series B redeemable convertible preferred $5,394 thousand; accumulated deficit $(5,748) thousand | the F-pages inside accession -135503, E&Y report dated 2003-06-20 | **a different registrant's audited statements filed inside Google's registration statement.** A grep for "Series A-1", "capital lease", "liquidation preference" returns these rows first. Not Google, not the window. |
| `KPCB 21,043,711` / `Sequoia 23,893,800` post-offering blocks | beneficial-ownership tables, both printings | column geometry unrecoverable from the stripped layer; the two printings disagree on the KPCB figure (§K.2a) |
| the MD&A ratio table (`16.5 / 29.9 / 42.7 / 48.4 / 46.6 …`) | -135503 | column set does not reconcile (§K.2b) |
| `[8,153]` beside "Searches conducted at Google.com" | YIL July 2000 l.5196 | the number's unit, basis and list membership are illegible in the held OCR; a number that cannot be attached to a definition is not a quantity |
| any "queries per day" for 1998-2001 | nowhere | EMPTY; the 30-million figure in the 1998 patent describes **another** engine (part 1 P1QTN02) |
| the $121.50 assumed IPO price as a market fact | -135503 pro forma | an assumption printed to compute dilution (part 1 Boundary §3 iv) |

### M.5 Coda and firewall

**Mechanism:** the window's money picture is now: revenue, cost lines, a bottom line, and a period-end cash
figure for the closing year — all printed in 2004 about 1999-2001. **Alternative explanation not excluded:** the
2001 "profitability" could be read as a per-share, operating, or GAAP-net phenomenon; the corpus supports the
GAAP-net reading (net income 6,985) and shows why the sentence is contestable (SBC 12,383 exceeds it), without
resolving what management meant. **Anti-hagiography:** every row here is a filed figure with its basis; none is
a growth-rate boast. Confidence: **High** only inside the auditor's band and for this pass's own byte counts.

---

## N

STATUS: WRITTEN 2026-09-29

**Rule applied:** a row is CONTEMPORANEOUS when the carrier's own date is the event's date; RETROSPECTIVE when a
later document describes an earlier state; RESTATED when a later document re-presents an earlier *number* under
changed conventions (splits, presentation). All of §G–§J's carriers date from 2004, so the default for this
volume is retrospective; the rows below say which claims escape that and how far.

| Row / claim | Carrier date | Event date | Verdict | Note |
|---|---|---|---|---|
| P1A01/P1SRC01 patent filing 1998-01-09 (part 1) | grant record printed 2001-09-04; recital 1998-12/2003-10 | 1998-01-09 | **CONTEMPORANEOUS** (registry) | the only founding-era date that is not the company's prose |
| 1998-11-11 capture (part 1 P1SRC03) | 1998-11-11 | same | **CONTEMPORANEOUS** | 212 B; unauthenticated |
| 1998-12-01 / 1999-04-14 / 2000-04-17 Stanford dates (part 1 P1SRC06) | executed instrument, filed 2004-06-21 | 1998-2000 | **CONTEMPORANEOUS in content, PB in custody** | co-signed by a third party; the held copy is the 2003 restatement |
| July 2000 magazine ranking (part 1 P1SRC07) | 2000-07 | 2000-07 | **CONTEMPORANEOUS** | UNVERIFIED TLS caps it at Medium |
| Sep 2001 press listing and verb usage (`P2H03`) | 2001-09 | 2001-09 | **CONTEMPORANEOUS** | the only in-window independent naming of the service besides July 2000 |
| Network World 1998-1999 zero-Google census (`P2H04`) | 1998-03/06, 1999-01/05 | same | **CONTEMPORANEOUS null** | a measurement over contemporaneous bytes |
| incorporation September 1998; WebSearch 1999-Q1; Premium Sponsorships 2000-Q1; AdWords 2000-Q4; profitable 2001 | 2004-04-29 | 1998-2001 | **RETROSPECTIVE NARRATIVE** | issuer self-report; five beats, no carrier at the time |
| FY1999/FY2000 revenue and cost lines | 2004-04-29 | 1999/2000 | **RESTATED (figures) inside a retrospective carrier**, unaudited band | the numbers are company-prepared for those years |
| FY2001 revenue / net income / operating income | 2004-04-29 | 2001 | **RESTATED carrier, ATTESTED figure** | inside the E&Y band (part 1 B15) |
| FY2002/FY2003 revenue presented net then gross | 2004-04-29 → 2004-08-09 | 2002/2003 | **RESTATED twice within one lineage** | the presentation change is the reason; §M.2 |
| cash at 2001-12-31 $33.6M | 2004-08-09 | 2001-12-31 | **RETROSPECTIVE** (prose citing a period end) | not a statement line in the table read |
| $37.6M cumulative preferred | 2004-04-29 | 1998-09 → 2004 | **RETROSPECTIVE aggregate** | spans beyond the window; cannot be cut at 2001 |
| Series C $2.3425 / 2001-07-13; CEO note 2001-09-28 | 2004-04-29 | 2001 | **RETROSPECTIVE carriers of executed transactions** | related-party disclosure, not the instruments |
| officer arrival months (1999-05, 2000-11, 2001-03, 2001-07) | 2004-04-29 / 2004-08-09 | 1999-2001 | **RETROSPECTIVE** | biographies; no appointment document held |
| 1998 Stock Plan adopted September 1998 | 2004-04-29 | 1998-09 | **RETROSPECTIVE**, month-level | corroborated only by the plan's own existence |
| "first office outside the U.S. in 2001" | 2004-08-09 | 2001 | **RETROSPECTIVE**, year-level | no address, country or headcount |
| 20% time; AdSense for content; Google News | 2004-04-29 | 2002-2004 `(PB)` | **RETROSPECTIVE**, and outside the window | §I.3 |
| rescission ceiling $34M → $25.9M | 2004-04-29 → 2004-08-09 | 1998-09 → 2004 exposure | **CONTEMPORANEOUS disclosures about a window-long defect** | the defect's start (1998 grants) is in-window; the revision is not |
| Overture suit filed April 2002; settled 2004-08-09 | 2004-08-09 | 2002 / 2004 | **CONTEMPORANEOUS as to the filing act**, `(PB)` for the window | part 1 P1FAI03 |
| subsidiary list (15 entities) | 2004-07-12 exhibit | 2004 | **CONTEMPORANEOUS**, `(PB)` | §I.2 |
| Applied Semantics FY2002 balance sheet | 2003-06-20 audit | 2002 | CONTEMPORANEOUS **to a different registrant** | §M.4 refusal |

**N.1 Coda.** Nineteen of the twenty-one rows above are retrospective or restated. The volume's four
contemporaneous anchors are one registry entry, one crawl, one executed bilateral instrument filed late, and
three magazine issues — and two of the three magazines are outside the window. That ratio, not the word count,
is the honest description of Alphabet Stage 1's evidence base.

---

## O

STATUS: WRITTEN 2026-09-29

**Evidence-class rule applied in this section.** A *risk factor* is a forecast, not an event; an *admission* is
the company speaking against itself; a *filed loss* is an attested or company-prepared number; a *silence* is a
measured absence. Each row below carries its class, and no forecast is written as though it happened.

### O.1 Failures the record carries, with class

| # | Failure / adverse fact | Date or period | Carrier | Evidence class | Conf |
|---|---|---|---|---|---|
| O-1 | The company lost money in each of its first two full reported years: net loss `(6,076)` and `(14,690)` thousand on net revenues of `220` and `19,108` thousand | FY1999, FY2000 | 073639 Summary Consolidated Financial Data | FACT as to the figures, company-prepared and **outside the auditor's band** | Medium |
| O-2 | Its own first public page called the product unreliable: "Might-work-some-of-the-time-prototype" | 1998-11-11 | part 1 P1SRC03 | CONTEMPORANEOUS self-description (no company signature on the page) | High |
| O-3 | Equity it had been granting since 1998 was issued unlawfully: "Shares issued and options granted under our 1998 Stock Plan and our 2003 Stock Plan were **not exempt from registration or qualification** under federal and state securities laws and we did not obtain the required registrations or qualifications" | 1998-09 → 2004 | 073639 Risk Factors; -135503 same passage | FACT, self-disclosed **against interest** | High |
| O-4 | The remedy's size moved inside one instrument: exposure "up to $34 million plus statutory interest" (April) → "up to $25.9 million, which includes statutory interest" (August) | 2004-04-29 → 2004-08-09 | both printings | FACT (revision visible in the lineage) — see `U.021` | High as to the two prints |
| O-5 | The rescission price was set below the offering's indicated value: repurchase "at a weighted average price of **$2.86**, while our current estimated initial public offering price is **between $108.00 and $135.00**" | 2004-08-09 | -135503 Rescission Offer | FACT (both figures printed in one sentence) | Medium |
| O-6 | A mechanism was built and superseded inside four quarters: Premium Sponsorships (2000-Q1, direct sales, priced per display) → AdWords self-service (2000-Q4) | 2000 | 073639 "How We Generate Revenue" | FOUNDER CLAIM; the *why* is UNKNOWN (part 1 P1DEC05) | Medium |
| O-7 | The core ad mechanism was contested in court by the rival that owned the model: Overture's suit, filed **April 2002**, on U.S. Patent No. 6,269,361, "claims that the patent relates to Overture Services' own bid-for-ad placement business model" | 2002-04 `(PB)` | 073639 / -135503 Legal Proceedings | FACT (disclosed legal event) | High |
| O-8 | **Adverse judgments on the advertising practice itself:** "A court in France has held us liable for allowing advertisers to select certain trademarked terms as keywords. We have appealed this decision."; in Germany "one court preliminarily reached a similar conclusion… while another court held that we are not liable"; "We are litigating similar issues in other cases in the U.S., France, Germany and Italy" | undated in the held text (the policy change is "recently") | -135503 Risk Factors | FACT (a disclosed adverse outcome) + FORECAST ("we may be subject to more trademark infringement lawsuits… could result in a loss of revenue") | High that it is disclosed; **UNKNOWN** as to dates of the French/German decisions |
| O-9 | Third-party copyright assertions against named in-window products: "features of certain of our products, including **Google WebSearch, Google News and Google Image Search**, violate their copyright" | product names as filed 2004 | -135503 | FACT that notices are disclosed; class of claims undated | Medium |
| O-10 | Growth admitted to be straining the organisation: "We have experienced, and continue to experience, rapid growth in our headcount and operations, which has placed, and will continue to place, significant demands on our management, operational and financial infrastructure" | 2004 statement about 2002-2004 | -135503 Risk Factors | FOUNDER CLAIM (self-report of strain), `(PB)` for the window | Medium |
| O-11 | Unreliability acknowledged structurally, not hypothetically: "Some of our systems are not fully redundant, and our disaster recovery planning cannot account for all eventualities"; "Some of our data centers are located in areas with a high risk of major earthquakes" | 2004 | -135503 Risk Factors | FORECAST / disclosed condition — **not an incident**; no outage is reported anywhere in the corpus | High that the sentences are printed |
| O-12 | Failure without a name: "Most risky projects fizzle, often teaching us something"; "Some of our past bets have gone extraordinarily well, and others have not" | 2004-04-29 | founders' letter | FOUNDER CLAIM, retrospective, **no project identified** — the corpus contains zero named killed projects | Medium |
| O-13 | The company's own judgment on a channel: "Because we sometimes cancel agreements that perform poorly, we do not expect to make all of these minimum revenue share payments" | 2004 | -135503 MD&A | FOUNDER CLAIM, `(PB)`; the only held statement about killing a commercial relationship | Medium |
| O-14 | Inexperience admitted at the scale-act it was making: "We do not have a great deal of experience acquiring companies and the companies we have acquired have been small" | 2004 `(PB)` | -135503 Risk Factors | FOUNDER CLAIM against interest | Medium |
| O-15 | The stage's independent quality witness ranked Google **fourth** | 2000-07 | part 1 P1SRC07 | CONTEMPORANEOUS OBSERVATION (Tier-3, UNVERIFIED TLS) | Medium |

### O.2 Near-deaths the record does **not** support

Searched across both the April and August printings for the vocabulary of an existential crisis and measured the
result: **"going concern" 0 occurrences; "substantial doubt" 0; "restructuring" 0; "layoff" 0.** There is no
cash-crash disclosure, no covenant breach, no emergency financing, no fire-sale language, and no account of a
moment when the company nearly ended. Two consequences, stated as the corpus requires:

1. A Stage-1 "near-death" narrative for Alphabet has **no carrier in this record at all** — and because the 1999
   and 2000 columns are company-prepared and outside the attested band, the absence of distress language in a
   2004 document about 1999-2000 is weak evidence even of the absence of distress. **Class UNKNOWN**, verdict
   EMPTY (searched, perimeted on the terms listed).
2. The one documented moment at which the company's *mechanism* could have been taken away is `O-7`, and it is
   one quarter past the close — which is exactly why part 1's boundary keeps it `(PB)` and why this volume
   treats 2002 litigation as the boundary's own witness rather than as a stage event.

### O.3 Coda and firewall

**Mechanism:** the failures the record carries are financial (two loss years), legal-at-the-edges (unregistered
equity, adverse foreign trademark rulings, a contested ad patent), and operational-admission (non-redundant
systems, strain from growth) — all disclosed by one party in one document type at one date, 2004. **Alternative
explanation not excluded:** the loss years may understate or overstate the operating reality; the unaudited
band means no third party has attested them. **Anti-hagiography:** none of O-1…O-15 reads differently if the
company died in 2003; several (O-3, O-7, O-8, O-11) are the kinds of facts that kill companies. Confidence:
**High** for the self-disclosed against-interest rows, **Medium** for the founder-claim rows, **UNKNOWN** for
O-2's question.

---

## P

STATUS: WRITTEN 2026-09-29

§7's decision format is used; `actual_result` may reference post-stage outcomes only when labelled RETROSPECTIVE.

| Date | Decision | State before | Information available then | Unknowns | Alternatives (documented?) | Constraints | Rationale | Expected result | Actual result | Evidence | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2000-Q4 | Replace a sales-gated ad program with a self-service one | Ads sold per display by a direct sales force since 2000-Q1 | the existence of a sales force; FY1999 revenue `220` thousand | which constraint (cost, reach, speed) drove it | **not documented** — no alternative is named in any held text | billing, onboarding, support capacity | UNKNOWN — the instrument states sequence, never motive | advertisers buy without a sales conversation | FY2001 net income `6,985` thousand, same instrument | RETROSPECTIVE; LIN-REG | Medium |
| 2001-03 → 2001-07 | Install an outside chief executive (Chairman of the board from March 2001; CEO from July 2001) | two founders as Presidents of Technology / Products; no CEO | that a Novell chairman-CEO was available; that the company had lost money in each reported year | who proposed it; whether the founders resisted | **not documented** | board composition; investor directors since 1999-05 | UNKNOWN in the corpus | an experienced public-company operator at the helm | he joined and the company's first positive net income year is 2001 | RETROSPECTIVE biography in a 2004 filing | Medium |
| 2001-09-28 | The new CEO funded his option exercise with a company loan (~$4.3M, 7.38%, secured by 14,331,708 Class B shares) | option granted at $0.30 | the exercise price and the share count | why the company financed rather than required cash; the alternative (no exercise, or cash) | **not documented** | Delaware/contract law; the 1998/2003 plans' terms | not recorded — UNKNOWN | the executive holds equity immediately | note repaid in full 2004-04-28 | RETROSPECTIVE (`(PB)` outcome) — the transaction itself is in-window | Medium |
| 2001 (year) | Open the first office outside the United States | one-country operation | nothing about the choice of country | which country, which city, how many staff | **not documented** | UNKNOWN | UNKNOWN | international reach | international revenue later 22%→29% of total (2002→2003) `(PB)` | FOUNDER CLAIM, year-granular | Low-Medium |
| UNKNOWN (printed 2004-04-29) | Refuse payment for index inclusion or ranking | paid inclusion was the visible industry practice (1998 patent background) | the practice existed and was commercially successful | when the commitment began; what it cost | **documented as the industry alternative**, not as Google's rejected option | the ranking method's credibility | the commitment's own words: "we will not accept payment for inclusion or ranking in them" | relevant results and user trust | UNKNOWN — no revenue figure is attributable to the policy | part 1 P1DEC02; 2004 statement of practice | Medium |
| 2000-06 → (terminated 2004-07 `(PB)`) | Sell engine wholesale to the largest portal while building a retail ad business | licensing was the founding model | Yahoo's traffic; FY2000 revenue `19,108` thousand | whether the deal was priced as distribution or as credibility | the alternative — refuse the portal — is not documented as considered | dependence capped by economics, not intent: "This agreement with Yahoo accounted for less than 3% of our revenues for the year ended December 31, 2003" | not recorded | distribution of the index at scale | the arrangement was terminated `(PB)` | FOUNDER CLAIM; part 1 P1F03, P1CNF02 | Medium |
| 2004 `(PB)` | Price the offering by auction rather than by the traditional underwriter-set method | "no public market for our stock" | the traditional model, named as the alternative in the same sentence | how much the auction would raise | **documented as an explicit alternative:** "The auction process being used… **differs from methods that have been traditionally used** in most other underwritten initial public offerings in the U.S." | underwriter economics; the master order book | the filing describes the mechanism, not the motive | price and allocation "determined by an auction process conducted by us and our underwriters" | outside the stage | LIN-REG, `(PB)`, retained because it is the corpus's only decision row with a printed alternative | Medium |

### P.1 What this table refuses

Every in-window row has **rationale UNKNOWN** except where the instrument itself supplies one, and the
instrument supplies none. Part 1's §Boundary already records that no internal document of 1998-2001 survives in
any family; §P is therefore a table of *acts with dates and no motives*. The single row with a documented
alternative (`2004`, the auction) is post-boundary, which is itself the finding: **inside the window, the record
preserves choices without choices-not-taken; only after the company had lawyers did it start naming them.**

---

## Q

STATUS: WRITTEN 2026-09-29

**Format duty (§7 / RD-034):** each entry states evidence, mechanism, alternative explanation and confidence,
and no entry uses the later outcome as the reason for the earlier act.

1. **The revenue mechanism changed kind twice, and the customer relationship changed with it.** Evidence:
   1999-Q1 licensing → 2000-Q1 direct-sale display advertising → 2000-Q4 self-service. Mechanism (as far as the
   record reaches): each step removed an intermediary from the sale. Alternative explanation not excluded: the
   steps may reflect whoever happened to be hired (a sales SVP from May 1999) rather than a design. Confidence:
   **Medium**, single lineage.
2. **The pricing basis, not the product, is what the window fixes.** Inside the window advertisers paid *per ad
   displayed*; cost-per-click exclusivity is 2002-Q1 `(PB)` ("we have only a short operating history with our
   cost-per-click advertising model, which we launched in 2002"). Evidence: two sentences, one instrument.
   Alternative: some early click-priced inventory may have existed and is undisclosed. Confidence **High** as to
   what is printed, **UNKNOWN** as to mix. This is part 1's `P1CNF04` now corroborated by a second passage from
   the Risk Factors, still one lineage (no upgrade to High).
3. **The company stopped being legible to itself.** From FY2001, revenue lines are attested and the bottom line
   turns positive (`6,985` thousand); the corpus simultaneously gains a full cost stack for 1999-2001 and
   *still* has no headcount, user or traffic figure. Mechanism: securities disclosure, not management
   reporting, is the source. Confidence: **High** for the attested years.
4. **Distribution became a dependency the audited notes could measure.** Advertising and other revenue from one
   network member (AOL) ran 15%/16%/13% of revenues 2002/2003/H1-2004 `(PB)`, while no *customer* exceeded 10%
   in 2001-2003. What changed: a business that sold to many small advertisers became a business that also paid
   many large publishers — the guaranteed minimum revenue share obligations of **$477.0 million** at 2003-12-31
   are the balance-sheet trace of that shift, and none of it exists inside the window. Confidence: **High**
   (audited band) for the percentages, **Medium** for the causal framing.
5. **A mechanism adopted in-window was attacked out-of-window, and the attack changed the accounting.** The
   Overture suit (2004 settlement, `(PB)`) produced a **non-cash charge of "between $260 million and $290
   million"** with a tax benefit of $100–115 million, and "The charge will result in a **net loss for us** in the
   three months ending September 30, 2004" — the first disclosed net loss after the stage's first profitable
   year. Mechanism: settle-in-shares, expense the shares. Alternative: the loss is an artifact of post-warrant
   share issuance, not of operations. Confidence: **High** that the sentences are printed, `(PB)` for every use.
6. **The competitive field as printed in 2004 is not the field as experienced in 1999, and the record now shows
   both.** Evidence: the S-1's named rivals versus a September-2001 magazine listing Google beside Netscape,
   Lycos, Excite, AltaVista and LookSmart, and a January-2002 description of Overture's per-placement price
   disclosure. Mechanism: different observers, different denominators. Confidence: **Medium** (UNVERIFIED TLS).
7. **The founders' own account of how they learned is the weakest kind of evidence this corpus holds.** "Most
   risky projects fizzle, often teaching us something" is a 2004 statement of a policy, with no named project,
   no date, and no in-window application. What changed because of what happened cannot be built on it; this
   volume records the sentence and declines the inference. Confidence: **Low**.

### Q.1 Coda

Every "because" in §Q is a conjunction in one document plus arithmetic on another column of the same document.
No entry needs the 2004 outcome to be true, and none is made stronger by it.

---

## R

STATUS: WRITTEN 2026-09-29

Live conflicts this volume opens, each left two-sided and carried in §U and in `conflicts.csv`. Part 1's
`P1CNF01`–`P1CNF07` remain open and are **not** re-emitted here; `U.017`–`U.036` are this volume's keys.

| Key | Conflict, stated both ways | Weight | Best-supported reading | Residual |
|---|---|---|---|---|
| `U.017` | part 1 §A.1/§A.3 and inherited record B18: "operating detail 1998-2000… **UNKNOWN; no carrier**" — versus a full statement of operations for FY1999-FY2001 printed in the same lineage this pass read | the printed table outranks the asserted absence | B18 is **refuted for costs and the bottom line**; it survives for headcount, users, queries, cash-by-year and 1998 | whether the earlier passes read the Summary Financial Data table's later columns or only its revenue line |
| `U.018` | "We became profitable in 2001" versus net income `6,985` thousand against stock-based compensation `12,383` thousand in the same year | both are the issuer's own figures, one instrument | profitability on a GAAP net-income basis is supported; the *economic* reading is contested inside the same table | which measure the sentence means — **UNKNOWN**, and the corpus does not resolve it |
| `U.019` | part 1 §A.4's alternative explanation ("the licensing business may have remained the larger share past Q1 2000") versus "Advertising revenues made up 77%… in 2001" | a printed percentage beats a stated possibility | the alternative is **closed for 2001** (advertising was 77% of that year) and remains open for 1999-2000, where no split is printed | the 2001 non-advertising 23% is not decomposed by licensee |
| `U.020` | FY2002/FY2003 revenue printed twice in one lineage: 347,848 / 961,874 (net) versus 439,508 / 1,465,934 (gross) | identical totals, identical bottom line | one instrument re-presented its revenue basis between 2004-04-29 and 2004-08-09; the reclassification is margin-neutral to the dollar (`91,660` and `504,060` move in both lines) | which basis the *in-window* years would take under the later convention — FY2001 is identical either way, so 1999-2000 are untestable |
| `U.021` | rescission exposure "up to $34 million" (April) versus "up to $25.9 million" (August) | same instrument family, both printed | a revision inside one lineage; neither figure is an incurred cost | the driver of the $8.1M difference is not stated |
| `U.022` | the 8-K cover prints "GOOGLE INC. … **California** 0-50726" (2004-07-09) while the S-1 printings of April-August 2004 print "Delaware" and the SGML header prints STATE OF INCORPORATION: DE | the SGML header and the prospectus covers agree; the 8-K cover disagrees | the 8-K's cover field is stale or form-carried, not a re-domiciliation; part 1's CA-1998 → DE-2003 break stands | whether a California-period Exchange Act registrant record was simply never updated — UNKNOWN on held bytes |
| `U.023` | Google's registration statement contains another issuer's audited founding-era numbers (Applied Semantics, Inc., E&Y report 2003-06-20) with series names that grep-match Google's own | both are real; only one is Google's | no Applied Semantics figure may be read as a Google figure; recorded so the next pass cannot repeat the near-miss | none — the attribution is certain from the F-page headers |
| `U.024` | part 1 §Boundary.3(iii): the valuation recital is "the closest the corpus comes" to pre-IPO money, versus "private sales of preferred stock totaling **$37.6 million**" | the printed aggregate is closer than a recital | part 1's refusal of a *round* survives; its claim that no money quantum exists is superseded | round-by-round allocation inside the $37.6M — EMPTY |
| `U.025` | part 1 §Boundary.3(iv): "no IPO price… `$121.50` is an assumed price" versus a held printing that prints an estimated range "between **$108.00 and $135.00**" | the range is a filed statement; the assumption is arithmetic on it | `(108.00+135.00)/2 = 121.50`: the assumed price is the **midpoint of the filed range**, so the two agree; the actual clearing price remains unavailable because the 424B4 is not held | the auction's final price and date — **UNANSWERED by custody** |
| `U.026` | beneficial-ownership: KPCB prints 23,893,800 (April, against both KPCB and Sequoia) versus 21,043,711 (August) | neither reading is verifiable without the table's markup | **no quantity taken from that table in this volume**; column geometry is unrecoverable from the stripped layer | which column each figure sits in — UNANSWERED on the held layer |
| `U.027` | "strong word-of-mouth promotion" versus sales-and-marketing expense of `1,677`/`10,385`/`20,076` thousand against revenue of `220`/`19,108`/`86,426` thousand | both are the issuer's own | the acquisition claim is unsupported as stated; the expense line shows paid acquisition activity, with no split between user-side and advertiser-side | what the money bought — UNKNOWN |
| `U.028` | "At March 31, 2004… 1,907 employees… **All of Google's employees are also shareholders**" versus "At June 30, 2004… 2,292 employees… All of Google's employees, **except temporary employees and contractors**, are also equityholders" | both inside one lineage | a claim narrowed and renamed between printings; the window's headcount remains UNKNOWN | whether the change is substance or drafting — UNKNOWN |
| `U.029` | the April and June printings capitalise a ten-vote class "Class A Senior common stock… 162,565,747 shares"; the August printing does not carry the class | all three are the same registrant | the class was redesigned before the offering — the 8-K of 2004-07-09 "implements certain changes with respect to Google's dual class common stock structure" — so the disappearance has a documented legal act, not a lost round | whether any money changed hands in the redesign — the corpus does not say |
| `U.030` | the MD&A percentage table's seven value columns cannot be matched to its headers | measurement failure, not a factual dispute | ratio-table values are excluded from §M | recoverable only from a table-aware parse of the exhibit HTML |

---

## S

STATUS: WRITTEN 2026-09-29

### S.1 The reporting basis, established from the instrument's own header

The SGML header block of accession -073639 prints: `COMPANY CONFORMED NAME: Google Inc.`, `CENTRAL INDEX KEY:
0001288776`, `IRS NUMBER: 770493581`, `STATE OF INCORPORATION: DE`, **`FISCAL YEAR END: 1231`**, `SEC ACT: 1933
Act`, `SEC FILE NUMBER: 333-114984`, `PUBLIC DOCUMENT COUNT: 33`, and a `BEGIN PRIVACY-ENHANCED MESSAGE`
signature block wrapping the submission. So: **fiscal year = calendar year ending December 31** for this
registrant, and no fiscal/calendar mismatch of the kind that moved Target's FY1965 leg (a defect class this dossier does not have) exists here. Every year figure in §M is a calendar-year total; period-end figures (cash,
obligations) are December-31 instants.

### S.2 Presentation bases that differ inside one instrument

1. **Net versus gross revenue.** The April printing labels the line **"Net revenues"** and reports FY2002 `347,848`
   and FY2003 `961,874` thousand; the August printing labels the same line **"Revenues"** and reports `439,508`
   and `1,465,934`. FY1999-FY2001 print identically under both labels (`220 / 19,108 / 86,426`). Any table
   mixing the two bases is wrong by $91,660K (2002) and $504,060K (2003).
2. **Thousands versus millions.** The statement tables are "(in thousands, except per share data)"; the
   liquidity prose and the contractual-obligations table are in millions ("$334.7 million", "(in millions)
   (unaudited)"). This volume's §M rows carry the unit cell in the source's own scale and never convert.
3. **(unaudited) is a table label, not only a caveat.** The Summary/Selected Consolidated Financial Data table is
   headed "(unaudited)" *in its own column band*, including the 2001-2003 columns that the auditor's report does
   cover (part 1 B15: E&Y audited "at December 31, 2002 and 2003, and for each of the three years in the period
   ended December 31, 2003"). A figure can therefore be both attested-in-substance and unaudited-as-presented;
   §M marks such rows by band, not by the label.
4. **Retroactive restatement for splits.** "In February and June 2003, the Company effected separate two-for-one
   stock splits. In addition, the Company effected other splits in prior years" — and all share and per-share
   amounts "have been retroactively restated… as if such split had taken place at the earliest date presented".
   **The prior splits are undated**, so every per-share figure for 1999-2001 (`(0.14)`, `(0.22)`, `0.07` basic)
   and every share count (`42,445` basic shares for 1999) is a **restated** number: the corpus cannot recover the
   as-issued 1999 share count. §N labels these RESTATED.
5. **A blank cell is not a zero.** The stock-based-compensation row of the 2004-04-29 table prints six values
   across seven period columns; footing the totals locates the missing value at **FY1999**
   (`908+2,930+1,677+1,221 = 6,736` = the printed total). The same shape recurs in "Provision for income taxes",
   where two leading period columns are empty. Neither is a zero and neither is written as one.
6. **The capitalization table is in thousands of shares, legal basis** (`15,360 / 50,651 / 10,000 / 7,437`
   authorised; `70,432` issued at 2002-12-31; `71,662` at 2003-12-31; aggregate liquidation preference `$40,815`
   thousand at 2004-03-31), against a preferred note elsewhere printing `71,662,432` shares as an exact total —
   the same number at two scales, which is a basis trap, not a conflict.
7. **Second instrument, same registrant.** The 8-K of accession -115812 is filed under Exchange Act file number
   `000-50726` (its cover prints `0-50726`) and is **not** part of the Securities Act lineage; under §3 it is one
   source of its own, and it witnesses one act (the 2004-07-06 charter amendment adopted 2004-06-25), nothing
   about 1998-2001.

### S.3 Record-selection null for this section (§2)

No internal management report, budget, forecast, board pack or auditor workpaper for 1998-2001 exists in any
family. The reporting history the corpus holds begins where the auditor's band begins (2001) and where the
underwriter's need begins (2004). What the company knew about its own early costs, and what it chose not to file,
are unrecoverable — which is why §O's "no going-concern language" is a statement about 2004 disclosure, not
about 1999 solvency.

### S.4 Coda

**Mechanism:** every basis problem above is detectable only by reading two printings of one instrument, which is
what this pass did; part 1's single-printing read could not see any of them. **Confidence:** High for the header
fields and the footing checks (they are arithmetic on held bytes), Medium for the interpretation of the
presentation change.

---

## T

STATUS: WRITTEN 2026-09-29 — the independence ledger, per §3

### T.1 The lineages that actually exist

| Key | Lineage | Members on this disk | Independence | What it can settle alone |
|---|---|---|---|---|
| **LIN-REG** | Google's 2004 Securities Act registration statement, printed nine times across two SEC file numbers, plus the unheld 424B4 | 9 `.txt` accessions held (part 1's carrier table) + exhibits; this pass opened -073639, -105564, -135503, -134174's stub cover, and exhibits dex2101/dex1002/dex1003/dex1010 | **one source**; every figure in §G-§J is this lineage whether it appears in one printing or three | the registrant's own numbers, its self-dated chronology, its related-party transactions, its risk admissions |
| **LIN-FOUNDER** | the founders' letter and every later company history tracing to it, printed inside LIN-REG | inside -073639/-135503 (Letter from the Founders) | **zero** independence from LIN-REG; it is LIN-REG's own front page | nothing beyond "the founders said this in 2004" |
| **LIN-E&Y** | Ernst & Young LLP's reports and consents | dex2301/dex2302 in several accessions; the report covering 2001-2003; **a second E&Y report for a different registrant (Applied Semantics, FY2002, 2003-06-20)** inside the same lineage | the only attestation inside LIN-REG, and it **starts at 2001**; the Applied Semantics report is independent *of Google* but attests *another company* | the audited band; the unaudited band's limits |
| **LIN-PATENT** | US 6,285,999 grant record + the executed Stanford licence recital (Exhibit 10.10) | `sources/patents/us6285999.html`; `sources/sec/…-105564_dex1010.htm` | **independent**: a register entry plus a co-signed bilateral instrument (Stanford had its own reasons to keep dates right) | 1998-01-09 filing; single named inventor; assignee Stanford; the 1998-12-01/1999-04-14/2000-04-17 sequence |
| **LIN-ARCHIVE** | the Internet Archive capture and its CDX index | `sources/wayback/google_19981111_raw.html` (212 B) + `cdx_retry.json`; four sibling CDX queries 503'd | **independent**: an unrelated crawler's record | that a service answered on 1998-11-11 18:45:51 and what its page said |
| **LIN-PRESS** | *Yahoo Internet Life* July 2000, September 2001, January 2002, March 2002; four *Network World* issues (1998-03-30, 1998-06-22, 1999-01-11, 1999-05-10) | `sources/periodicals/*_djvu.txt` + `.meta.json` | **independent of the company** in origin; **Tier-3** in §5 terms; every layer fetched over **UNVERIFIED TLS** | the field as third parties saw it; the company's absence from IT trade press; the name's verb use |
| **LIN-GSA** | the CIA-held Beta Evaluation Agreement (2004-11) | `sources/ia/cia_1487901_djvu.txt` | Google-authored form but **custodied by the counterparty**; `(PB)` | the form of an enterprise evaluation, three years late |
| **LIN-SEC-INDEX** | the submissions enumeration and file-number metadata | `sources/_index/*` | the SEC's own index; witnesses filing acts only | that a 424B4 exists at 2004-08-19 and is not held |
| **LIN-OTHERREG** | Applied Semantics' audited statements; the four acquired corporations in Exhibit 21.01 | inside -135503 F-pages; `dex2101.htm` | different registrants, filed by Google — usable as **competitor/counterparty** context only | nothing about Google's own early state (§M.4) |

### T.2 What counts as corroboration here, and what does not

**Not corroboration:** the same $37.6 million sentence in three printings (one lineage); "Google Inc." in an S-1
cover and in a magazine (the magazine is independent, the two covers are not each other); a figure repeated in
the Prospectus Summary and the MD&A; two digitised copies of one magazine issue (Microsoft's `D17`/`D09`
problem, and the same discipline applies to the four Network World numbers — they are four issues, hence four
observations of *silence*, but one family). **Corroboration:** the patent's filing date appearing both in a
registry document and in a co-signed licence recital (two origins); the 1998-11-11 capture's markup versus the
2004 narrative (independent, and they disagree — `P1CNF06`); a byte count measured by this pass against the same
file's sidecar.

### T.3 Lineage-internal deltas this pass produced (why they matter for the merge)

Five changes inside one instrument family were found by reading more than one printing: the rescission ceiling
(`U.021`), the revenue presentation basis (`U.020`, `S.2.1`), the headcount sentence and its ownership
qualifier (`U.028`), the disappearance of a ten-vote share class (`U.029`), and the appearance of an IPO price
range that was not in the April printing (`U.025`). None is a second source. All five are evidence that **a
register row keyed to "the S-1" without a printing date is under-specified**, and the merge should carry the
accession and date in every `sources.csv` row touching LIN-REG (part 1's P1SRC04 already names the accession).

### T.4 Coda

Four of the nine lineages can carry an in-window fact, and only LIN-PATENT and LIN-ARCHIVE do it without the
company's own voice. Everything else is LIN-REG, which is why §L.2 caps the volume at Medium.

---

## U

STATUS: WRITTEN 2026-09-29

<!-- ANCHORS: U.017-U.036 -->

**Anchor declaration and numbering policy.** `U-1`–`U-5` belong to
`research/A_chronology_feasibility.md`; `U-6`–`U-16` belong to `research/B1_filing_records.md`; part 1 minted
`P1CNF01`–`P1CNF07` and proposed "U-17 onward" for the merge. **This volume mints `U.017`–`U.036` and no other
anchors**, in the padded dot form the parity gate reads, and every one is cited by at least one register row
below. Part 1's `P1CNFnn` keys are *not* re-minted here; if the merge folds them into the same space, the
declared machine comment at the head of this section is the authoritative set (§15.5, Target's merge precedent). Each entry is left two-sided;
none is closed by counting copies of one lineage. §7's conflicting-evidence field set is used.

**U.017 — "no carrier for 1998-2000 operating detail" versus a printed statement of operations for those years.**
- CLAIM A: part 1 §A.1 (`Operating detail 1998-2000 (costs, headcount, users, cash) | UNKNOWN; no carrier`) and inherited B18 (`no headcount, revenue, user or cost figure exists in the held corpus for 1998, 1999's operating detail, or any month before 2003`).
- CLAIM B: the 2004-04-29 printing's Summary Consolidated Financial Data prints, for FY1999 and FY2000, cost of revenues, R&D, sales and marketing, G&A, stock-based compensation, total costs, operating loss, interest, pre-tax loss, net loss, basic and diluted loss per share, and the share counts (`U.017` rows in §M.1, `P2QTN04`–`P2QTN12`).
- WHY THEY DIFFER: an absence claim written against a partial read of one table.
- EVIDENCE WEIGHT: B is the bytes; A is a census statement about bytes.
- BEST-SUPPORTED INTERPRETATION: **B18 is refuted for costs and the bottom line, and survives for headcount, users, queries and year-by-year cash.** The retraction is the point of the record, not a re-grading of difficulty.
- RESIDUAL UNCERTAINTY: whether the earlier passes read only the revenue row of the same table.
- CONFIDENCE: High (this pass read the table in two printings and footed it).

**U.018 — what "profitable in 2001" means when stock-based compensation exceeds the profit.**
- CLAIM A: "We became profitable in 2001 following the launch of our Google AdWords program."
- CLAIM B: the same instrument's table prints FY2001 net income `6,985` thousand **and** FY2001 stock-based compensation `12,383` thousand.
- WHY THEY DIFFER: A is a characterisation; B is the arithmetic behind it.
- EVIDENCE WEIGHT: one lineage, both statements inside it.
- BEST-SUPPORTED INTERPRETATION: the claim is true on a GAAP net-income basis and contestable on any cash or pre-SBC reading; the corpus does not say which basis the sentence intends.
- RESIDUAL UNCERTAINTY: management's definition — **UNKNOWN**.
- CONFIDENCE: Medium.

**U.019 — the 2001 mechanism mix is printed, and it closes part 1's open alternative.**
- CLAIM A: part 1 §A.4: the disclosure "is compatible with the licensing business having remained the larger share of revenue well past Q1 2000… no held line apportions them."
- CLAIM B: "Advertising revenues made up 77%, 94%, 97% and 98% of our revenues in 2001, 2002, 2003 and in the six months ended June 30, 2004."
- WHY THEY DIFFER: A was written from the printing that carried the chronology; B is in the MD&A of a later printing.
- EVIDENCE WEIGHT: B is a printed percentage in the auditor's band for 2001.
- BEST-SUPPORTED INTERPRETATION: **for 2001 the alternative is closed** (advertising 77%, everything else 23%); for 1999-2000 nothing is printed and A's caution still governs those years.
- RESIDUAL UNCERTAINTY: the composition of the 23% (engine licences, enterprise search, appliance, other).
- CONFIDENCE: High as to 2001; the closure is stated for that year only.

**U.020 — one lineage, two revenue bases for the same years.**
- CLAIM A (2004-04-29): "Net revenues… 347,848… 961,874" for FY2002/FY2003.
- CLAIM B (2004-08-09): "Revenues… 439,508… 1,465,934" for the same years.
- WHY THEY DIFFER: a gross-versus-net presentation change for traffic-acquisition/revenue-share costs between printings.
- EVIDENCE WEIGHT: both filed; cost of revenues moves by exactly the same amounts (`131,510−39,850 = 91,660`; `625,854−121,794 = 504,060`), and income from operations is unchanged.
- BEST-SUPPORTED INTERPRETATION: **the reclassification is margin-neutral and the choice of basis, not the business, moved the top line.**
- RESIDUAL UNCERTAINTY: what the in-window years would look like under the gross basis; FY2001 is identical either way, 1999-2000 untestable.
- CONFIDENCE: High as to arithmetic, Medium as to cause.

**U.021 — the rescission ceiling moves inside one instrument family.**
- CLAIM A: April 2004 printing — "aggregate payments… of up to $34 million plus statutory interest".
- CLAIM B: August 2004 printing — "up to $25.9 million, which includes statutory interest".
- WHY THEY DIFFER: the exposure is computed from a price, and the price the computation used changed.
- EVIDENCE WEIGHT: both are the registrant's own words in the same lineage.
- BEST-SUPPORTED INTERPRETATION: a re-estimate, not two independent measures; **part 1's B25 figure (`$34M`) must be dated to its printing** when the merge keys it.
- RESIDUAL UNCERTAINTY: neither figure is an incurred cost; no evidence of acceptance rates is held.
- CONFIDENCE: High.

**U.022 — a California cover on a Delaware registrant, three weeks before the prospectus that says Delaware.**
- CLAIM A: the 8-K (accession -115812, report dated 2004-07-06) prints "GOOGLE INC. … (State or other jurisdiction of incorporation or organization) **California** 0-50726".
- CLAIM B: every S-1 printing's cover and header block prints Delaware / `STATE OF INCORPORATION: DE`, and the S-1 says "we reincorporated in Delaware in August 2003".
- WHY THEY DIFFER: an Exchange Act cover carried from the registrant's earlier California state-of-incorporation record versus a Securities Act cover drawn from the current charter.
- EVIDENCE WEIGHT: the S-1 covers plus the SGML header agree; the 8-K cover disagrees alone.
- BEST-SUPPORTED INTERPRETATION: a stale cover field, not a re-domiciliation; part 1's CA-1998→DE-2003 break is unaffected, and **no stage conclusion changes** — but the ledger must record that the corpus's second instrument disagrees about the registrant's own state.
- RESIDUAL UNCERTAINTY: whether EDGAR's registrant record still carried California in July 2004 — **UNKNOWN**, route UNTRIED (§Delaware/California SoS, `## Untried`).
- CONFIDENCE: Medium.

**U.023 — another company's audited founding-era numbers sit inside Google's own filing.**
- CLAIM A: a grep of the held printings returns "Series A-1 convertible preferred stock… liquidation preference of $500", "total assets $6,218", "cash and cash equivalents $1,953", "accumulated deficit (5,748)" — figures that look like a 2002 balance sheet of the registrant.
- CLAIM B: the same pages are headed "Applied Semantics, Inc. BALANCE SHEET" and are attested by an Ernst & Young report dated June 20, 2003 for the year ended December 31, 2002.
- WHY THEY DIFFER: one registrant's registration statement carries a second registrant's audited statements because of an April 2004 acquisition `(PB)`.
- EVIDENCE WEIGHT: B is explicit in the F-page headers.
- BEST-SUPPORTED INTERPRETATION: **no Applied Semantics figure is a Google figure**; the trap is recorded so no later pass re-imports it (RD-124/RD-125 class: a text hit that is not a naming).
- RESIDUAL UNCERTAINTY: none for attribution; the file's own headers settle it.
- CONFIDENCE: High.

**U.024 — the corpus does hold a pre-IPO money quantum, and part 1 said it did not.**
- CLAIM A: part 1 §Boundary.3 — "no pre-IPO funding round — the closest the corpus comes is a *valuation recital*".
- CLAIM B: "Since inception, we have financed our operations primarily through internally generated funds, **private sales of preferred stock totaling $37.6 million** and the use of our lines of credit…" (identical in three printings).
- WHY THEY DIFFER: A was written against the printings part 1 opened; B is in the MD&A liquidity paragraph of the same accession part 1 *did* open, in a region it did not quote.
- EVIDENCE WEIGHT: B is printed.
- BEST-SUPPORTED INTERPRETATION: **the refusal of a named, dated round stands; the absence of a money quantum is retracted.** $37.6 million is cumulative from 1998-09 to a 2004 reporting date and cannot be cut at the stage close.
- RESIDUAL UNCERTAINTY: per-round dates, subscribers and amounts — EMPTY.
- CONFIDENCE: High as to the sentence, Medium as to what it implies.

**U.025 — the offering price: assumed, ranged, and still unavailable.**
- CLAIM A: part 1 §Boundary.3(iv) — "`$121.50` is an *assumed* price in a registration statement" and no sale price is recoverable.
- CLAIM B: the August printing prints "our current estimated initial public offering price is **between $108.00 and $135.00**", and `(108.00+135.00)/2 = 121.50`.
- WHY THEY DIFFER: the April printing carries no range (the cover field is blank), the August printing does; the assumed price is arithmetic on the range.
- EVIDENCE WEIGHT: both are LIN-REG printings; the range is a filed statement of expectation, not a transaction.
- BEST-SUPPORTED INTERPRETATION: **part 1's refusal of the actual IPO price stands** — the 424B4 of 2004-08-19 is enumerated and not held — but the range is now citable as a filed fact `(PB)`.
- RESIDUAL UNCERTAINTY: the clearing price, the auction's allocation, and the first trade — UNANSWERED by custody.
- CONFIDENCE: High for the arithmetic check; Medium for the reading.

**U.026 — the beneficial-ownership table cannot be measured off the held layer.**
- CLAIM A: the April printing's 5%-holders rows print KPCB `23,893,800` and Sequoia `23,893,800`.
- CLAIM B: the August printing's rows print "Entities affiliated with Kleiner Perkins Caufield & Byers" `21,043,711` and "Entities affiliated with Sequoia Capital" `23,893,800`.
- WHY THEY DIFFER: two printings, and a multi-column table whose column boundaries are carried by markup this pass stripped.
- EVIDENCE WEIGHT: neither reading is verifiable without the exhibit's HTML table structure.
- BEST-SUPPORTED INTERPRETATION: **no ownership-table figure is used as a quantity in this volume**; the row is kept so the next pass does not quietly use one.
- RESIDUAL UNCERTAINTY: which column each number sits in — UNANSWERED on the held layer; a table-aware parse is UNTRIED.
- CONFIDENCE: Medium that the two strings print as quoted; nothing higher.

**U.027 — the acquisition story versus the acquisition invoice.**
- CLAIM A: "We have found that offering a high-quality user experience leads to increased traffic and strong word-of-mouth promotion." (part 1 P1CHN05: the corpus's only acquisition-channel claim, with zero evidence).
- CLAIM B: sales-and-marketing expense `1,677` thousand in 1999 against `220` thousand of net revenue (`7.62×`), `10,385` thousand in 2000 (`0.54×`), `20,076` thousand in 2001 (`0.23×`).
- WHY THEY DIFFER: A is a causal self-description written in 2004; B is a filed expense line.
- EVIDENCE WEIGHT: both are LIN-REG; B has the auditor's band from 2001 only.
- BEST-SUPPORTED INTERPRETATION: the company paid for sales and marketing at multiples of revenue while attributing user acquisition to unpaid word of mouth; **the corpus cannot split the line by target**, so it states both and infers neither.
- RESIDUAL UNCERTAINTY: what the money bought; whether any of it was user-acquisition spend — UNKNOWN.
- CONFIDENCE: Medium.

**U.028 — the employee-ownership sentence narrowed between printings.**
- CLAIM A: April 2004 — "At March 31, 2004, we had 1,907 employees… **All of Google's employees are also shareholders**."
- CLAIM B: August 2004 — "At June 30, 2004, we had 2,292 employees… All of Google's employees, **except temporary employees and contractors**, are also equityholders."
- WHY THEY DIFFER: a date roll plus an inserted exclusion and a renamed noun, in one instrument family.
- EVIDENCE WEIGHT: both printed; neither attested to a period inside the stage.
- BEST-SUPPORTED INTERPRETATION: a substance-narrowing (an excluded population appears) or a drafting correction — the corpus cannot choose; recorded so no later pass quotes the April sentence as the company's position.
- RESIDUAL UNCERTAINTY: the window's headcount remains UNKNOWN either way.
- CONFIDENCE: High that the strings differ; Low as to why.

**U.029 — a ten-vote share class that exists in one printing and not in the next.**
- CLAIM A: April and June 2004 printings capitalise "Class A Senior common stock, $0.001 par value, ten votes per share: 300,000 shares authorized, 162,566 issued and outstanding" (`211` mentions in the April text, `10` in the June).
- CLAIM B: the August printing's pro forma language converts only "all outstanding shares of our preferred stock", and the class does not appear.
- WHY THEY DIFFER: a pre-offering recapitalisation between printings.
- EVIDENCE WEIGHT: the 8-K of 2004-07-09 bridges them — the Second Amended and Restated Certificate "implements certain changes with respect to Google's dual class common stock structure", adopted by the board and stockholders on June 25, 2004.
- BEST-SUPPORTED INTERPRETATION: **a documented legal act explains a lineage-internal change**; and because "Senior" is a voting class rather than a financing, it must not be read as an unstated round (§14 rule 8 trap class).
- RESIDUAL UNCERTAINTY: who held the class and what they received — the corpus says the holders were reclassified share-for-share and does not name them.
- CONFIDENCE: Medium-High for the bridge (two instruments, one act), `(PB)` throughout.

**U.030 — the MD&A ratio table's columns cannot be matched to its values.**
- CLAIM A: the table presents seven value columns under three header groups, and its first cost row reads `16.5 | 29.9 | 42.7 | 48.4 | 46.6 | 36.5 | 47.5`.
- CLAIM B: the absolute table above it reconciles to the dollar (2001 `14,228/86,426 = 16.5`; 2002 `29.9`; 2003 `42.7`), leaving two columns (`48.4`, `46.6`) without an identifiable period.
- WHY THEY DIFFER: a presentation/measurement problem in the stripped layer, not a dispute between sources.
- EVIDENCE WEIGHT: the absolute table foots; the ratio table does not resolve.
- BEST-SUPPORTED INTERPRETATION: **ratio-table values are excluded from §M and from every register row of this volume.**
- RESIDUAL UNCERTAINTY: recoverable only from a table-aware parse of the exhibit HTML — UNTRIED.
- CONFIDENCE: High as to the measurement failure.

**U.031 — the first licensee: re-searched, still nameless.**
- CLAIM A: "We began licensing our WebSearch product in the first quarter of 1999."
- CLAIM B: no document in LIN-PATENT, LIN-ARCHIVE, LIN-PRESS or LIN-GSA names a licensee, and the audited note gives only a ceiling ("no customer accounted for greater than 10% of net revenues in 2001, 2002 and 2003").
- WHY THEY DIFFER: nothing — B is the absence of what A presupposes.
- EVIDENCE WEIGHT: A is one lineage; B is a measured search across five families.
- BEST-SUPPORTED INTERPRETATION: **EMPTY** (searched, perimeted), carried forward from part 1 P1GAP01 with this
  pass's additional printings searched; the product name "Google WebSearch" is independently confirmed by the
  copyright-claim sentence quoted at `P2O05` (a 2004 naming of a 1999 product).
- RESIDUAL UNCERTAINTY: counterparty-side filings of 1999-2001 have never been full-text searched for "WebSearch" — see `## Untried`.
- CONFIDENCE: High as to the null.

**U.032 — round dates, subscribers and per-round amounts.**
- CLAIM A: the corpus holds an aggregate (`$37.6M`), a ladder of authorised/issued series at 2002-12-31 and 2003-12-31, one priced officer purchase (2001-07-13 at `$2.3425`), and one post-money recital (`$8,000,000`).
- CLAIM B: no held document dates a round, names its subscribers against an amount, or gives a pre-2001 share price.
- WHY THEY DIFFER: they do not; the pair defines the limit.
- EVIDENCE WEIGHT: one lineage plus one exhibit.
- BEST-SUPPORTED INTERPRETATION: **EMPTY** as to per-round structure; the ladder's series names are the only structural trace and their first observation year is 2002 `(PB)`.
- RESIDUAL UNCERTAINTY: whether a purchase-agreement exhibit exists in EDGAR and was never requested — **UNTRIED**.
- CONFIDENCE: High as to the null.

**U.033 — headcount, users, queries, index size and plant inside the window.**
- CLAIM A: the S-1 prints headcount only at 2004-03-31 and 2004-06-30; international revenue share only from 2002.
- CLAIM B: no family supplies any in-window operating statistic, and the XBRL series holds exactly one row, for 2006-12-31 (§K.3).
- WHY THEY DIFFER: they do not.
- EVIDENCE WEIGHT: measured across nine held printings/families this pass and part 1's searches.
- BEST-SUPPORTED INTERPRETATION: **EMPTY**, with the cause on the record: a private company disclosed nothing until an offering required it.
- RESIDUAL UNCERTAINTY: third-party measurement services of 1999-2001 (Jupiter, Nielsen//NetRatings, SearchEngineWatch) were never attempted — UNTRIED.
- CONFIDENCE: High as to the null.

**U.034 — the trade-press silence as an evidence-shape finding.**
- CLAIM A: the company's 2004 account places it at the centre of search by 1999-2000.
- CLAIM B: four *Network World* issues spanning 1998-03-30 to 1999-05-10 — 1,414,577 bytes, 68,059 lines, measured this pass — contain **zero** lines matching "google" in any case, and the consumer magazine that did name it ranked it fourth in July 2000.
- WHY THEY DIFFER: A is retrospective self-narrative; B is a census over contemporaneous third-party bytes.
- EVIDENCE WEIGHT: B is independent and countable; A is one lineage.
- BEST-SUPPORTED INTERPRETATION: both stand; the silence limits how far the founding story can be pushed into 1998-1999 press, and it is **not** evidence the service was bad — only that the IT trade press this corpus holds did not print it.
- RESIDUAL UNCERTAINTY: other trade titles (Ziff's own *Internetworld*, *Wired*, *US Today* local papers) UNTRIED; UNVERIFIED TLS caps B at Medium even though it is a count.
- CONFIDENCE: High for the count, Medium for its meaning.

**U.035 — the UNANSWERED set: routes that refused rather than returned nothing.**
- CLAIM A: several questions in §K are unresolvable *from held bytes*.
- CLAIM B: for four of them the retrieval itself failed: the **424B4 (2004-08-19) is enumerated and not held**; accession **-138034 is index-page-only** so its file number is UNTESTED; four Wayback **CDX queries returned HTTP 503** (part 1 P1SRC11), including the `google.stanford.edu` host history; the **USPTO tmsearch route 405'd**; and the CIK 1652044 archive slice **404'd** (part 1 P1GAP08).
- WHY THEY DIFFER: they do not — the entry exists to keep refusals out of the null count.
- EVIDENCE WEIGHT: n/a.
- BEST-SUPPORTED INTERPRETATION: **these are UNANSWERED, not EMPTY**, and each has a scripted fix (`sec_intake.py auto`, a CDX retry, an index retry).
- RESIDUAL UNCERTAINTY: none about status; everything about content.
- CONFIDENCE: High as to each failure mode, which is recorded in the sidecars.

**U.036 — the UNTRIED set: what this pass did not attempt.**
- CLAIM A: §K's perimeted nulls imply the searches were run.
- CLAIM B: seven routes were not run by any pass in this corpus: California and Delaware entity registries, EDGAR full-text for counterparty filings naming "WebSearch", the USPTO assignment/prosecution dossier for US09/004,827, PACER for the rescission-related matters, the remaining *Yahoo Internet Life* issues 1999-2001, third-party audience measurement print for 1999-2001, and a table-aware HTML parse of the ownership and ratio tables.
- WHY THEY DIFFER: an untried family is not a null (RD-124's rule, §14 rule 6).
- EVIDENCE WEIGHT: n/a.
- BEST-SUPPORTED INTERPRETATION: **the tier verdict for this stage rests on three families that returned text (filings, web archive, periodicals) and is silent about two (documentary/auction records, registries) that remain UNTRIED.**
- RESIDUAL UNCERTAINTY: named with commands in `## Untried`.
- CONFIDENCE: High as to what was not done.

---

## Claim records for §G–§U

STATUS: WRITTEN 2026-09-29

**Carrier shorthand used in these records** (every path is under
`founders_playbook/01_companies/company_005_alphabet/`): **P-A** = `sources/sec/0001193125-04-073639_0001193125-04-073639.txt`
(S-1 as filed 2004-04-29, 5,719,779 B, **a concatenated multi-document submission: its text contains both the
prospectus and its 33 exhibits**); **P-B** = `…-04-105564_….txt` (Amendment No. 2, 2004-06-21); **P-C** =
`…-04-135503_….txt` (Amendment No. 5, 2004-08-09, the fullest held printing); **P-D** = `…-04-115812_d8k.htm`;
**P-E** = `…-04-116608_dex2101.htm`; **P-F** = `…-04-134174_ds1a.htm`; **P-G** = `…-04-105564_dex1010.htm`
(Stanford licence); **P-H/P-I/P-J/P-K** = `sources/periodicals/yahoo-internet-life-magazine-{september-2001,
january-2002, march-2002, july-2000}_djvu.txt`; **P-L** = the four `sources/periodicals/bub_gb_*_djvu.txt`
*Network World* layers (1998-03-30, 1998-06-22, 1999-01-11, 1999-05-10); **P-M** =
`sources/financials/xbrl_early_series.csv`. P-A/P-B/P-C are **one lineage** (LIN-REG): corroboration is counted
once however many of them print a figure, and each record names the printing so the merge can date its rows.

P2G01 Claim: The company's own filed chronology puts first search revenue in 1999 and first advertising revenue
in 2000, and calls its click-based model a 2002 launch. — Date: 1999 (first search revenue); 2000 (first
advertising revenue); 2002 (cost-per-click launch, `(PB)`) — Source path: P-C, Risk Factors — Source date:
2004-08-09 — URL: sec.gov/Archives/edgar/data/0001288776/000119312504135503/0001193125-04-135503.txt —
Archived: as path — Tier: 1 — Class: FOUNDER CLAIM (retrospective; printed in a document about the offering) —
Passage: "We first derived revenue from our online search business in 1999 and from our advertising services in
2000, and we have only a short operating history with our cost-per-click advertising model, which we launched in
2002." (33 words) — Conf: Medium — Corroboration: 1 lineage (LIN-REG; P-A/P-B/P-C are one instrument) —
Conflicts: U.018.
independence_note: same lineage as part 1's P1SRC04; the sentence adds a second dated first (1999 search
revenue) to the paragraph part 1 quoted, and is an addition to that carrier, not a new source.

P2G02 Claim: The held record describes the sales motion as a hybrid — self-service intake with email support, a
direct sales force above it, and field offices in eleven countries — and every one of those descriptions is 2004
copy about a 2004 business. — Date: 2004-08-09 (statement); applicability to 1998-2001 UNKNOWN — Source path:
P-C, Business — Source date: 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FOUNDER CLAIM +
FACT that the sentences are printed — Passage: "AdWords is available on a self-service basis with email support.
Advertisers with more extensive needs and budgets can request strategic support services, which include an
account team of experienced professionals…" (25 words) — Conf: Medium — Corroboration: 1 lineage — Conflicts:
None; §G.3 item 1.
independence_note: same lineage as P1SRC04; `(PB)` for every use inside the stage.

P2G03 Claim: The advertising platform paid most of each network click fee away to third-party publishers, and
the company states that as a revenue design rather than a cost. — Date: 2003 → 2004 `(PB)`; nothing in-window —
Source path: P-C, Prospectus Summary — Source date: 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 —
Class: FOUNDER CLAIM — Passage: "When a user clicks on an ad displayed on a web site of a Google Network
member, we retain only a small portion of the advertiser fee, while most of the fee is paid to the Google
Network member." (32 words) — Conf: Medium — Corroboration: 1 lineage; the balance-sheet trace is the guaranteed
minimum revenue share obligation of $477.0 million at 2003-12-31 (P2G08) — Conflicts: U.020 (the same economics
drive the gross/net presentation change).
independence_note: one lineage; corroborating obligation table is the **same instrument's** MD&A, so counted
once.

P2G04 Claim: One network member, AOL, accounted for a mid-teens share of revenues while no single customer
exceeded a tenth — a channel dependence and a customer ceiling printed in the same document. — Date: FY2002,
FY2003, H1-2004 — Source path: P-C, MD&A / audited concentration note — Source date: 2004-08-09 — URL: as P2G01 —
Archived: as path — Tier: 1 — Class: FACT (the AOL percentages sit in the auditor's band for 2002-2003; the
concentration note is audited) — Passage: "advertising and other revenues generated from one Google Network
member, America Online, Inc., primarily through our AdSense programs, accounted for approximately 15%, 16% and
13% of our revenues in 2002, 2003 and in the six months ended June 30, 2004" (29 words) — Conf: High for the
band years — Corroboration: 1 lineage, two notes (concentration ceiling recorded at P1F01) — Conflicts: part 1
P1CNF02, which this record does not re-open.
independence_note: same lineage as P1F01; the pair is what makes the reading possible, and it is still one
issuer's voice.

P2G05 Claim: The first mechanism split any held document prints for the closing year puts advertising at 77% of
revenues, which closes part 1's alternative explanation for 2001 only. — Date: FY2001, FY2002, FY2003, H1-2004 —
Source path: P-C, MD&A — Source date: 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FACT
(inside the auditor's band from 2001) — Passage: "Advertising revenues made up 77%, 94%, 97% and 98% of our
revenues in 2001, 2002, 2003 and in the six months ended June 30, 2004." (22 words) — Conf: High —
Corroboration: 1 lineage — Conflicts: **U.019**.
independence_note: same lineage as P1A03; this is a new passage from a printing part 1 did not open, not a second
source.

P2G06 Claim: In the two years the company says it acquired users by word of mouth, its filed sales-and-marketing
expense exceeded its net revenue in 1999 by 7.6× and was 54% of revenue in 2000. — Date: FY1999, FY2000, FY2001 —
Source path: P-A, Summary Consolidated Financial Data — Source date: 2004-04-29 — URL:
sec.gov/Archives/edgar/data/0001288776/000119312504073639/0001193125-04-073639.txt — Archived: as path — Tier: 1
— Class: FACT (1999-2000 company-prepared, outside the attested band; 2001 inside it) + **DERIVED** for the
ratios — Passage: "Sales and marketing 1,677 10,385 20,076" (row as printed; "(in thousands, except per share
data) (unaudited)") — Conf: Medium — Corroboration: 1 lineage — Conflicts: **U.027**.
independence_note: the arithmetic `1,677/220 = 7.62×`, `10,385/19,108 = 0.54×`, `20,076/86,426 = 0.23×` is this
pass's, from two rows of one table; the table's own "(unaudited)" label spans the attested years too (see §S.2.3).

P2G07 Claim: The supply side of the business is described as un-monetised by design: the company indexed the web
and sent traffic to sites it had no commercial relationship with. — Date: 2004-08-09 (statement); 1998-2001
applicability UNKNOWN — Source path: P-C, Business ("Web Sites") — Source date: 2004-08-09 — URL: as P2G01 —
Archived: as path — Tier: 1 — Class: FOUNDER CLAIM + FACT that it is printed — Passage: "Google provides a
significant amount of traffic to web sites with which we have no business relationship." (15 words) — Conf:
Medium — Corroboration: 1 lineage; consistent with, but not evidenced by, the free-inclusion commitment at
P1F04 — Conflicts: None.
independence_note: same lineage; the commitment and this sentence are two places in one instrument where the
absence of a paid-supply model is stated, and they remain one source.

P2G08 Claim: The company's own account of the network channel includes cancelling it: minimum revenue share
commitments were large, and management stated it would not honour all of them. — Date: 2003-12-31 (obligations),
statement 2004-08-09 — Source path: P-C, MD&A contractual obligations table and following paragraph — Source date: 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FACT (a filed table labelled
"(unaudited)") + FOUNDER CLAIM for the cancellation sentence — Passage: "Guaranteed minimum revenue share
payments $ 477.0 … Because we sometimes cancel agreements that perform poorly, we do not expect to make all of
these minimum revenue share payments." (24 words) — Conf: Medium — Corroboration: 1 lineage; H1-2004 reduction
to $27.5 million printed in the same paragraph — Conflicts: None; `(PB)` throughout.
independence_note: same lineage; retained because it is the only held statement about terminating a
customer/partner relationship, and it is three years past the close.

P2H01 Claim: The registrant's filed competitive frame names four kinds of rival and explicitly admits it cannot
enumerate them. — Date: 2004-08-09 (statement); field dates 1998-2004 — Source path: P-C, Competition — Source date: 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FOUNDER CLAIM — Passage: "In addition to
Microsoft and Yahoo, we face competition from other web search providers, including companies that are not yet
known to us." (20 words) — Conf: Medium — Corroboration: 1 lineage — Conflicts: None; §H.1.
independence_note: same lineage as P1SRC04; the phrase "not yet known to us" is the filing's own limit on the
section's completeness and is quoted so no later pass treats §H.1 as a census.

P2H02 Claim: The filing measures itself against Microsoft on the one axis a registration statement cannot fudge —
headcount — and states the multiple. — Date: 2004-08-09 (statement); the compared period is 2003-2004 `(PB)` —
Source path: P-C, Competition — Source date: 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class:
FOUNDER CLAIM (comparative self-measure, unverifiable without Microsoft's own filing) — Passage: "Both Microsoft
and Yahoo have more employees than we do (in Microsoft's case, currently more than 20 times as many)." (18
words) — Conf: Medium — Corroboration: 1 lineage; testable only against Microsoft's own filings, not held here —
Conflicts: None.
independence_note: same lineage; if a later pass checks it against Microsoft CIK 731, that comparison — not this
sentence — is the corroboration.

P2H03 Claim: Inside the stage window an unaffiliated consumer magazine listed Google in the same set as Netscape,
Lycos, Excite, AltaVista and LookSmart, and used the name as a verb in a joke column. — Date: 2001-09 —
Source path: P-H (`sources/periodicals/yahoo-internet-life-magazine-september-2001_djvu.txt`, 338,899 B, 14,518
lines) l.14171, l.12864, l.8809 — Source date: 2001-09 — URL: archive.org item
yahoo-internet-life-magazine-september-2001 — Archived: as path + `.meta.json` — Tier: 3 — Class: CONTEMPORANEOUS
OBSERVATION — Passage: "NETSCAPE LYCOS | lycos.com EXCITE | excite.com ALTAVISTA | altavista.com LOOKSMART |
looksmart.com GOOGLE | google.com" (list rendering) and "How many Republicans does it take to do a Google
search?" (9 words) — Conf: Medium (UNVERIFIED TLS per sidecar) — Corroboration: 1 independent publisher; part 1's
July-2000 issue is a **different issue of the same title**, so this is two observations by one masthead, not two
corroborations — Conflicts: None; §H.2.
independence_note: wholly outside LIN-REG and LIN-FOUNDER; OCR rendering of the list is degraded (no column
headers survive), so the list's purpose is stated as a listing, not a ranking.

P2H04 Claim: The IT trade press that this corpus holds across the founding moment does not name the company at
all — a measured absence over 68,059 lines. — Date: 1998-03-30, 1998-06-22, 1999-01-11, 1999-05-10 — Source path: P-L (four `sources/periodicals/bub_gb_*_djvu.txt` layers: 307,686 + 536,111 + 266,428 + 304,352 B =
1,414,577 B) — Source date: as listed per `.meta.json` — URL: archive.org download routes in the sidecars —
Archived: as path — Tier: 3 — Class: FACT about the search / **UNKNOWN about the event** — Passage:
NO_VERBATIM_PASSAGE_RECORDED (there is no line to quote: 0 matches for "google", case-insensitive, in all four
layers) — Conf: High as to the count; **no confidence is permitted about why** — Corroboration: four issues, one
title, one family — Conflicts: **U.034**.
independence_note: a documented null over bytes, distinct from an unsearched gap; *Network World* is one masthead,
so four numbers is four observations of one family's silence and not four independent silences.

P2H05 Claim: The rival mechanism Google did not adopt is described, in window-adjacent press, as a priced
placement service with public disclosure and a syndication network. — Date: 2002-01 `(PB)` — Source path: P-I
(`…january-2002_djvu.txt`) — Source date: 2002-01 — URL: archive.org item yahoo-internet-life-magazine-january-2002
— Archived: as path — Tier: 3 — Class: CONTEMPORANEOUS OBSERVATION — Passage: "each pay-for-placement search
result at Overture includes a disclosure that tells you exactly how much the advertiser forked over for that
position." (19 words) — Conf: Medium (UNVERIFIED TLS) — Corroboration: 1 publisher; the S-1's separate
description of Overture's model (P2O04's patent pleading) is LIN-REG, so not a second origin — Conflicts: None;
§H.4.
independence_note: outside both founder lineages; `(PB)` by one month and used only to show what the alternative
mechanism looked like to a contemporary observer.

P2H06 Claim: The field changed kind when a customer bought its wholesalers, and the filing dates the purchases. —
Date: 2002-2003 `(PB)`; statement 2004-08-09 — Source path: P-C, Competition — Source date: 2004-08-09 — URL: as
P2G01 — Archived: as path — Tier: 1 — Class: FOUNDER CLAIM — Passage: "Yahoo has become an increasingly
significant competitor, having acquired Overture Services… as well as the Inktomi, AltaVista and AllTheWeb search
engines." (24 words) — Conf: Medium — Corroboration: 1 lineage; Yahoo's own filings are not held — Conflicts:
part 1 P1CNF02 (customer versus channel), not re-opened.
independence_note: same lineage as P1F03; the same instrument simultaneously describes Yahoo as a user of
Google's technology and as a competitor, which is the section's structural point.

P2H07 Claim: The held consumer-press corpus cannot corroborate the paid-inclusion controversy at all: the term
does not occur in it. — Date: 2000-07, 2001-09, 2002-01, 2002-03 — Source path: P-H, P-I, P-J, P-K — Source date:
per issue — URL: archive.org items as above — Archived: as path — Tier: 3 — Class: FACT about the search —
Passage: NO_VERBATIM_PASSAGE_RECORDED (0 lines matching "paid inclusion" or `pay…inclusion` across 52,659 lines
of the four issues) — Conf: High as to the count — Corroboration: one masthead — Conflicts: None; the paid-
inclusion norm rests on the 1998 patent background (part 1 §C.1), not on press.
independence_note: a perimeted null; the searched terms and line counts are stated so the next pass can extend
the perimeter rather than repeat it.

P2I01 Claim: A professional worldwide sales function is dated to May 1999 by the registrant's own biography
copy, and its head came from a portal-era rival's business-development chair. — Date: 1999-05 — Source path:
P-A/P-C, Management — Source date: 2004-04-29 / 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class:
FOUNDER CLAIM (retrospective biography, month granularity) — Passage: "Omid Kordestani has served as our Senior
Vice President of Worldwide Sales and Field Operations since May 1999. Prior to joining us, from 1995 to 1999,
Omid served as Vice President of Business Development at Netscape." (29 words) — Conf: Medium — Corroboration: 1
lineage; Netscape's side of the biography is not held — Conflicts: None.
independence_note: same lineage as P1SRC04; the corpus holds no appointment letter, so the month is
company-asserted.

P2I02 Claim: Both venture-firm general partners appear on the board from the same month, which is the earliest
date the corpus attaches to either firm in any capacity. — Date: 1999-05 — Source path: P-A, Management — Source date: 2004-04-29 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FOUNDER CLAIM — Passage: "Michael Moritz
has served as a member of our board of directors since May 1999. Michael has been a General Partner of Sequoia
Capital, a venture capital firm, since 1986." (24 words) — Conf: Medium — Corroboration: 1 lineage; Doerr's
parallel sentence ("since May 1999", Kleiner Perkins) is the same instrument, so two rows and one source —
Conflicts: **U.024, U.032** (board dates are not funding dates).
independence_note: same lineage; this record exists precisely to bound what the board date can carry — see §L.1
item 5.

P2I03 Claim: The engineering leadership change inside the window is dated to November 2000, the same quarter as
the self-service launch, and the corpus cannot say whether the two are related. — Date: 2000-11 — Source path:
P-C, Management — Source date: 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FOUNDER CLAIM —
Passage: "Wayne Rosing has served as our Vice President of Engineering since November 2000." (14 words) — Conf:
Medium — Corroboration: 1 lineage — Conflicts: None; the coincidence is not a mechanism and is not written as
one.
independence_note: same lineage; the adjacent AdWords date comes from P1TML13, one lineage, so no corroboration
count is raised by pairing them.

P2I04 Claim: The stage's largest documented scaling act carries two dates and one prior employer, all from the
registrant's own copy. — Date: Chairman from 2001-03; Chief Executive Officer from 2001-07 — Source path: P-A,
Management — Source date: 2004-04-29 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FOUNDER CLAIM —
Passage: "Eric Schmidt has served as our Chief Executive Officer since July 2001 and served as Chairman of our
board of directors from March 2001 to April 2004." (26 words) — Conf: Medium — Corroboration: 1 lineage;
Novell's own filings are not held — Conflicts: None; §P row 2 (rationale UNKNOWN).
independence_note: same lineage; the March/July gap is the only in-window evidence that the arrival was staged,
and it is company prose.

P2I05 Claim: The new chief executive bought his equity with money borrowed from the company, in a dated,
quantified, secured transaction inside the window. — Date: 2001-09-28 (note dated); repaid 2004-04-28 `(PB)` —
Source path: P-A, Certain Relationships and Related Party Transactions, "Indebtedness of Management" — Source date: 2004-04-29 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FACT (a related-party transaction
disclosed against interest, though the instrument itself is not held) — Passage: "Eric Schmidt… delivered to us a
full recourse promissory note dated September 28, 2001 in the aggregate principal amount of approximately $4.3
million secured by shares of Class B common stock." (33 words) — Conf: Medium — Corroboration: 1 lineage, two
places in it (the Management discussion and the related-party note) counted once — Conflicts: None.
independence_note: same lineage; rate detail "7.38% per annum, compounded semi-annually" is printed in the same
paragraph and is the corpus's only in-window interest rate.

P2I06 Claim: International expansion has an in-window date and nothing else. — Date: 2001 (year only) — Source path: P-C, Risk Factors — Source date: 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FOUNDER
CLAIM — Passage: "We opened our first office outside the U.S. in 2001 and have only limited experience with
operations outside the U.S." (20 words) — Conf: Medium — Corroboration: 1 lineage; no subsidiary or lease carrier
inside the window (P2I09's list is 2004) — Conflicts: None.
independence_note: same lineage; the Exhibit 21.01 subsidiary list post-dates this sentence by three years and
cannot corroborate it.

P2I07 Claim: The corpus's earliest headcount statement is 2004, and the same sentence re-appears three months
later with a new number, a new date and an added exclusion. — Date: 2004-03-31; 2004-06-30 — Source path: P-A and
P-C, Employees — Source date: 2004-04-29 / 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class:
FACT (a company count) — Passage: "At June 30, 2004, we had 2,292 employees, consisting of 705 in research and
development, 1,141 in sales and marketing and 446 in general and administrative." (28 words) — Conf: Medium —
Corroboration: 1 lineage — Conflicts: **U.028**.
independence_note: same lineage twice; the April printing's "1,907… All of Google's employees are also
shareholders" and the August printing's narrowed "except temporary employees and contractors… are also
equityholders" are one source disagreeing with itself.

P2I08 Claim: Held infrastructure facts are all 2003-2004, and the prospectus prose and the lease exhibit
disagree about the size of the headquarters by 317 square feet. — Date: 2003-12-31 (lease and obligations),
statement 2004 — Source path: P-C Facilities; sublease text inside P-A (exhibit content of the concatenated
submission) — Source date: 2004-04-29 / 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FACT —
Passage: "We lease approximately 506,000 square feet of space in our headquarters in Mountain View, California
under a lease that expires in 2012." / "Four buildings including 506,317 square feet of Rentable Area" (27
words) — Conf: High (two documents on this disk, both readable) — Corroboration: 1 lineage, but two instrument
types (prospectus prose and an executed sublease) — Conflicts: **U.026**-adjacent; recorded as P2CNF10.
independence_note: the sublease is an executed contract but its custody here is inside LIN-REG, so it does not
leave the lineage; the rounding difference is nonetheless the strongest kind of finding available here because it
is two printings against each other.

P2I09 Claim: The corporate body that scaled is legible only in 2004: fifteen national subsidiaries and four
acquired corporations, named in an exhibit. — Date: 2004-07-12 `(PB)` — Source path:
`sources/sec/0001193125-04-116608_dex2101.htm` — Source date: 2004-07-12 — URL:
sec.gov/Archives/edgar/data/0001288776/000119312504116608/dex2101.htm — Archived: as path — Tier: 1 — Class: FACT
(registrant's own exhibit; a filing act, not a history) — Passage: "Google Inc., a Delaware corporation List of
wholly-owned subsidiaries… Applied Semantics, Inc., a California Corporation Kaltix Corporation… Orkut.com LLC"
(21 words) — Conf: High as to the list — Corroboration: 1 instrument — Conflicts: **U.023** (one named subsidiary
has audited statements in the same lineage that are not Google's).
independence_note: inside LIN-REG for custody; usable for the *legal* shape of the group and for nothing about
1998-2001.

P2J01 Claim: The corpus does contain a pre-IPO money total — $37.6 million of private preferred sales since
inception — and it contains no round. — Date: cumulative 1998-09 → 2004 — Source path: P-A, P-B, P-C, Liquidity
and Capital Resources — Source date: 2004-04-29 → 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 —
Class: FOUNDER CLAIM (a self-reported cumulative total) — Passage: "we have financed our operations primarily
through internally generated funds, private sales of preferred stock totaling $37.6 million and the use of our
lines of credit with several financial institutions." (26 words) — Conf: Medium — Corroboration: 1 lineage, three
printings — Conflicts: **U.024** (supersedes part 1's "closest is a valuation recital").
independence_note: the sentence is identical in all three printings, which is replication; no bank, investor or
auditor statement of the same total is held.

P2J02 Claim: The stage close has a period-end cash figure: $33.6 million at December 31, 2001, in a three-part
aggregate. — Date: 2001-12-31 — Source path: P-C (and P-B) Liquidity and Capital Resources — Source date:
2004-06-21 / 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FACT (inside the auditor's band,
reported in prose) — Passage: "compared to $334.7 million, $146.3 million and $33.6 million at December 31,
2003, 2002 and 2001, respectively" (15 words) — Conf: Medium — Corroboration: 1 lineage — Conflicts: **U.017**
(the same paragraph supplies what part 1 said had no carrier).
independence_note: same lineage; "cash, cash equivalents and short-term investments" is the aggregate named, and no
cash-only figure for any window date exists in the corpus.

P2J03 Claim: The preferred ladder exists as filed only from 2002, and its liquidation preference at the
offering's eve is $40,815 thousand. — Date: 2002-12-31, 2003-12-31, 2004-03-31 — Source path: P-C capitalization
note and Cash and Capitalization — Source date: 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class:
FACT (legal share counts, thousands of shares) — Passage: "Series A 15,360… Series B 50,651 49,823… Series D
7,437 7,437 166,896 70,432 164,782 71,662 $ 40,815" (row as printed) — Conf: Medium — Corroboration: 1 lineage —
Conflicts: **U.029, U.032**.
independence_note: same lineage; the "-1" series pairing appears only at the later date, which is how §J.2 reads
the 2003 reincorporation, as an INFERENCE.

P2J04 Claim: One share price inside the window is documented to four decimals because an officer bought at it:
$2.3425, 426,892 Series C shares, $999,994.51 total, on July 13, 2001. — Date: 2001-07-13 — Source path: P-A,
Certain Relationships and Related Party Transactions — Source date: 2004-04-29 — URL: as P2G01 — Archived: as path
— Tier: 1 — Class: FACT (a related-party transaction table) + DERIVED check — Passage: "Eric Schmidt 7/13/01
Series C preferred stock 426,892 $ 999,994.51" (table row) — Conf: Medium — Corroboration: 1 lineage — Conflicts:
**U.032**.
independence_note: same lineage; the arithmetic `426,892 × 2.3425 = 999,994.51` is printed as a price elsewhere in
the same sentence and foots exactly, which is the only reason the row is Medium rather than Low.

P2J05 Claim: Founding-era equity was priced in pennies and the rescission offer was priced at $2.86 against an
indicative offering price of $108.00–$135.00, in one sentence. — Date: 2004 (statement); grants from 1998-09 —
Source path: P-C, Rescission Offer; Employee Benefit Plans — Source date: 2004-08-09 — URL: as P2G01 — Archived:
as path — Tier: 1 — Class: FACT — Passage: "our rescission offer will offer to repurchase shares and options at a
weighted average price of $2.86, while our current estimated initial public offering price is between $108.00 and
$135.00." (28 words) — Conf: Medium — Corroboration: 1 lineage; the $0.29 weighted average exercise price of the
1998 Plan is the same instrument — Conflicts: **U.025**.
independence_note: same lineage; the 1998 Plan's "weighted average exercise price of $0.29 per share" is a
plan-wide average over six years of grants and is not a founding-day price.

P2J06 Claim: Two venture organisations are named as 5%+ holders in the filing, and neither is named in an
instrument that says what it paid or when. — Date: 2004-04-29 / 2004-08-09 (statements) — Source path: P-A and
P-C, Principal Stockholders and its footnotes — Source date: as listed — URL: as P2G01 — Archived: as path — Tier:
1 — Class: FOUNDER CLAIM; **no quantity from these rows is used** — Passage: "Includes 21,654,952 shares held by
Sequoia Capital VIII; 1,433,624 shares held by Sequoia International Technology Partners VIII(Q); 477,872 shares
held by CMS Partners LLC…" (25 words) — Conf: Low — Corroboration: 1 lineage — Conflicts: **U.026**.
independence_note: same lineage; the footnote names funds but attaches no date, amount or agreement to any of
them, which is exactly the gap §J.3 records.

P2J07 Claim: Alphabet has no counterpart to the Nvidia Ex-4.3 signature pages in this corpus: the two investor
names the brief expected are absent from every held filing text. — Date: search run 2026-09-29 over P-A (5,719,779
B), P-B (2,791,396 B), P-C (4,675,485 B) — Source path: as listed — Source date: n/a — URL: n/a — Archived: as
path — Tier: 1 — Class: FACT about the search / UNKNOWN about the events — Passage: NO_VERBATIM_PASSAGE_RECORDED
("Sutter Hill" 0 occurrences; "Khosla" 0 occurrences; "Sequoia" appears only in a director biography, an
ownership footnote and fund-name lists) — Conf: High as to the counts — Corroboration: three printings, one
lineage — Conflicts: **U.032, U.036**.
independence_note: a perimeted null over named files and named terms; the absence of a purchase agreement here is
not evidence none exists in EDGAR — that route is UNTRIED and is in `## Untried`.

P2J08 Claim: Bank credit, not venture money, is the second financing leg the filing admits, and a customer was
also a warrant holder. — Date: 2003-12-31 (letters of credit); warrant June 2000 → June 2003 issuance → 2004
settlement — Source path: P-A / P-C Liquidity; Legal Proceedings; Prospectus Summary — Source date: 2004-04-29 /
2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FACT (disclosed instruments and amounts) —
Passage: "At December 31, 2003, we had unused letters of credit for approximately $12.2 million." / "a warrant
held by Yahoo to purchase 3,719,056 shares of our stock in connection with a June 2000 services agreement" (23
words) — Conf: Medium — Corroboration: 1 lineage; the warrant's balance-sheet trace ($13,871 thousand at
2004-03-31, part 1 B16) is the same instrument family — Conflicts: part 1 P1CNF02; U.032.
independence_note: same lineage; "in connection with a June 2000 services agreement" is the only held sentence
tying an equity instrument to an in-window commercial act, and the underlying agreement is not held.

P2K01 Claim: The document that would settle the offering price is enumerated and not held, re-verified a second
time in this run. — Date: 2004-08-19 — Source path: `sources/_index/submissions.csv` + directory census of all
131 files under `sources/` — Source date: 2026-09-29 — URL: sec.gov CIK 0001288776 index route — Archived: as
path — Tier: 1 — Class: FACT about custody — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High —
Corroboration: index enumeration plus a disk listing — Conflicts: **U.025, U.035**.
independence_note: an index row is a filing fact, not content; the fetch is scripted work under §15.1, not agent
web work, and is listed with its command in `## Untried`.

P2K02 Claim: The XBRL family returns nothing for this stage, and the one row it holds disagrees with itself. —
Date: row's `end` 2006-12-31, `fy` 2009, form 10-K, accession 0001193125-10-030774 — Source path:
`sources/financials/xbrl_early_series.csv` (header + 1 row) — Source date: 2026-09-26 (file) — URL: EDGAR frames —
Archived: as path — Tier: 1 — Class: FACT about the file — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High —
Corroboration: n/a — Conflicts: **U.033**; reported to the tool owner as a defect (§K.3).
independence_note: a machine-generated series, independent of the company's prose, but five years past the close
and internally inconsistent in its period fields.

P2L01 Claim: Four of the five beats of the stage story are company self-narrative and only one is not. — Date:
1998-01-09 (registry); 1998-11-11 (crawl); 1998-12-01/1999-04-14/2000-04-17 (executed licence); the rest 2004
printings — Source path: as part 1 §Boundary and §L.2 — Source date: 1998-2004 — URL: as cited — Archived: as path
— Tier: 1 — Class: INFERENCE over the ledger (§T) — Passage: "We were incorporated in California in September
1998 and reincorporated in Delaware in August 2003. We began licensing our WebSearch product in the first quarter
of 1999." (29 words) — Conf: High that this is the distribution of evidence — Corroboration: n/a (a census, not
an event) — Conflicts: None.
independence_note: the sentence is LIN-REG; the registry and archive dates are not, and §L.2 keeps them apart.

P2L02 Claim: The corpus holds no distress language of the kinds that mark a near-death, and that limits what
§O can say rather than what happened. — Date: search run 2026-09-29 over P-A and P-C — Source path: as listed —
Source date: n/a — URL: n/a — Archived: as path — Tier: 1 — Class: FACT about the search / UNKNOWN about the
events — Passage: NO_VERBATIM_PASSAGE_RECORDED ("going concern" 0, "substantial doubt" 0, "restructuring" 0,
"layoff" 0 in both printings) — Conf: High as to the counts — Corroboration: two printings, one lineage —
Conflicts: **U.033, U.036**.
independence_note: a 2004 filing's silence about 1999 is weak evidence about 1999, and §O.2 says so rather than
concluding the company was comfortable.

P2M01 Claim: The revenue presentation changed inside one instrument family, and the change moved no money to the
bottom line. — Date: FY2002, FY2003, as printed 2004-04-29 and 2004-08-09 — Source path: P-A and P-C Summary
Consolidated Financial Data — Source date: as listed — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FACT
+ **DERIVED** — Passage: "Net revenues $ 220 $ 19,108 $ 86,426 $ 347,848 $ 961,874" (row as printed in P-A) —
Conf: High for the arithmetic, Medium for the interpretation — Corroboration: 1 lineage, two printings —
Conflicts: **U.020**.
independence_note: the derivation `439,508 − 347,848 = 91,660 = 131,510 − 39,850` and
`1,465,934 − 961,874 = 504,060 = 625,854 − 121,794` is this pass's and is printed in §M.2.

P2M02 Claim: A blank cell in a filed table is not a zero: the 1999 stock-based-compensation column is empty and
the total foots without it. — Date: FY1999, as printed 2004-04-29 — Source path: P-A Summary Consolidated
Financial Data — Source date: 2004-04-29 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: DERIVED —
Passage: "Stock-based compensation 2,506 12,383 21,635 229,361…" (row as printed, six values across seven period
columns) — Conf: Medium — Corroboration: 1 lineage — Conflicts: None; §S.2.5.
independence_note: the footing `908+2,930+1,677+1,221 = 6,736` equals the printed total-costs line, which locates
the missing value at the 1999 column rather than inventing one.

P2M03 Claim: Every per-share and share-count figure for the window is a restated number, because undated prior
splits were retroactively applied. — Date: splits February 2003, June 2003, "other splits in prior years" (undated)
— Source path: P-C, Note on stock splits / capitalization note — Source date: 2004-08-09 — URL: as P2G01 —
Archived: as path — Tier: 1 — Class: FACT — Passage: "In addition, the Company effected other splits in prior
years. All references to… common stock and preferred stock shares and per share amounts including options and
warrants… have been retroactively restated" (26 words) — Conf: High — Corroboration: 1 lineage — Conflicts:
**U.018** (the per-share basis of "profitable" is one of the things the restatement touches).
independence_note: same lineage; this is why §N marks the 1999-2001 per-share rows RESTATED rather than
contemporaneous.

P2N01 Claim: Read as a set, this volume's dated claims are almost entirely retrospective, and the count is the
finding. — Date: census of this volume's §N table — Source path: §N table (all carriers above) — Source date:
2026-09-29 — URL: n/a — Archived: n/a — Tier: n/a — Class: INFERENCE over the volume's own ledger — Passage:
NO_VERBATIM_PASSAGE_RECORDED — Conf: High as to the tally (19 of 21 rows retrospective or restated) —
Corroboration: n/a — Conflicts: None.
independence_note: a self-audit, not evidence; it exists so the merge can check that no `stage1` register row was
labelled CONTEMPORANEOUS without one of the four qualifying carriers.

P2O01 Claim: The company's first two full reported years were loss-making, and the loss in the second year was
77% of the revenue that accompanied it. — Date: FY1999, FY2000 — Source path: P-A Summary Consolidated Financial
Data — Source date: 2004-04-29 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FACT (company-prepared,
outside the attested band) + DERIVED ratio — Passage: "Income (loss) from operations (6,516) (14,737) 10,964…
Net income (loss) $ (6,076) $ (14,690) $ 6,985" (row as printed) — Conf: Medium — Corroboration: 1 lineage —
Conflicts: **U.017, U.018**.
independence_note: same lineage; the ratio `14,690 / 19,108 = 0.77` is this pass's arithmetic.

P2O02 Claim: The company disclosed, against its own interest, that a decade-defining practice — paying people in
equity — had been conducted unlawfully since the plan's adoption. — Date: 1998-09 → 2004 (period affected);
disclosed 2004-04-29 — Source path: P-A Risk Factors; Rescission Offer (and P-C) — Source date: 2004-04-29 /
2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FACT (self-disclosed against interest) —
Passage: "Shares issued and options granted under our 1998 Stock Plan and our 2003 Stock Plan were not exempt from
registration or qualification under federal and state securities laws and we did not obtain the required
registrations or qualifications." (31 words) — Conf: High — Corroboration: 1 lineage; part 1 P1FAI02 carries the
same carrier, so no new count — Conflicts: **U.021**.
independence_note: same lineage as P1FAI02; this record exists to date the exposure language to its printing,
because the two ceilings differ (U.021).

P2O03 Claim: Adverse court outcomes on the advertising practice itself are disclosed, undated, across three
jurisdictions, and the company said the practice would draw more suits. — Date: undated in the held text; policy
change "recently" as of 2004-08-09 — Source path: P-C, Risk Factors — Source date: 2004-08-09 — URL: as P2G01 —
Archived: as path — Tier: 1 — Class: FACT (disclosed adverse judgments) + FOUNDER CLAIM forecast — Passage: "A
court in France has held us liable for allowing advertisers to select certain trademarked terms as keywords. We
have appealed this decision." (21 words) — Conf: High that it is disclosed; **UNKNOWN** for the dates of the
decisions — Corroboration: 1 lineage — Conflicts: None; §O-8.
independence_note: same lineage; no court record is held, and PACER for the French/German/US matters is UNTRIED
(`## Untried`).

P2O04 Claim: The mechanism adopted inside the window was patented by a rival and litigated one quarter after the
close, and the settlement bought a perpetual licence with shares. — Date: suit filed 2002-04; settled 2004-08-09
`(PB)` — Source path: P-C Legal Proceedings — Source date: 2004-08-09 — URL: as P2G01 — Archived: as path — Tier:
1 — Class: FACT (disclosed legal event) — Passage: "Overture will dismiss its patent lawsuit against us and has
granted us a fully-paid, perpetual license to the patent that was the subject of the lawsuit" (24 words) — Conf:
High — Corroboration: 1 lineage; part 1 P1FAI03 and B39 carry the same carrier — Conflicts: inherited U-16 (the
filing month is one carrier's refinement of another's year), not re-minted.
independence_note: same lineage as P1FAI03; the settlement's expense ("between $260 million and $290 million" in
non-cash charge, producing a "net loss… in the three months ending September 30, 2004") is `(PB)` and is used only
at §Q item 5.

P2O05 Claim: Third parties asserted copyright violations against products whose names date to the window —
WebSearch among them — and the corpus holds no response or resolution. — Date: notices undated; statement
2004-08-09 — Source path: P-C, Risk Factors — Source date: 2004-08-09 — URL: as P2G01 — Archived: as path — Tier:
1 — Class: FACT that notices are disclosed; the assertions themselves are third-party claims — Passage: "features
of certain of our products, including Google WebSearch, Google News and Google Image Search, violate their
copyright" (21 words) — Conf: Medium — Corroboration: 1 lineage — Conflicts: None; the "Google WebSearch" naming
is the second held use of the product name part 1 relied on at P1TML07.
independence_note: same lineage; the claimants are not named in the held text, so no counterparty record exists to
check.

P2O06 Claim: Unreliability is admitted structurally in 2004 copy, and no incident is reported anywhere in the
corpus. — Date: statement 2004-04-29 / 2004-08-09; in-window outages UNKNOWN — Source path: P-C, Risk Factors —
Source date: 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FORECAST / disclosed condition —
**not** evidence of an event — Passage: "Some of our systems are not fully redundant, and our disaster recovery
planning cannot account for all eventualities." (16 words) — Conf: High that it is printed; nothing is claimed
about occurrences — Corroboration: 1 lineage — Conflicts: None.
independence_note: same lineage; §O's class rule forbids converting this into a failure event, and the corpus
offers no outage log, press report or status page either way.

P2O07 Claim: The only failure admission in the founders' letter identifies no project, which is why §O cannot
list a killed product. — Date: 2004-04-29 — Source path: P-A / P-C, Letter from the Founders — Source date:
2004-04-29 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FOUNDER CLAIM (retrospective, unattributed to
any project) — Passage: "Most risky projects fizzle, often teaching us something. Others succeed and become
attractive businesses." (13 words) — Conf: Medium — Corroboration: 1 lineage; LIN-FOUNDER for content —
Conflicts: None; §O-12.
independence_note: the letter is printed inside LIN-REG, so the two lineages are one custody; no named project is
recoverable from any family.

P2P01 Claim: No in-window decision in this corpus comes with a recorded rationale, and that is a property of the
archive rather than of the reading. — Date: all window rows of §P — Source path: §P table; part 1 P1DEC01-P1DEC05
— Source date: 2004-04-29 / 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: INFERENCE over the
decision ledger — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High as to the census — Corroboration: n/a —
Conflicts: None; §2 record-selection null.
independence_note: the ledger contains no internal document because none survives (§K.4); the finding is about
preservation, not about competence.

P2P02 Claim: The only held decision row with a printed alternative is the auction choice, and it is
post-boundary. — Date: 2004 (statement) `(PB)` — Source path: P-A and P-C, The Auction Process — Source date:
2004-04-29 / 2004-08-09 — URL: as P2G01 — Archived: as path — Tier: 1 — Class: FOUNDER CLAIM — Passage: "The
auction process being used for our initial public offering differs from methods that have been traditionally used
in most other underwritten initial public offerings in the U.S." (27 words) — Conf: Medium — Corroboration: 1
lineage, both printings — Conflicts: None; §P row 7.
independence_note: same lineage; the sentence names the alternative it departed from, which is why it is the
table's only documented-alternative row.

P2Q01 Claim: Inside the window the advertiser's price basis was display, not click, and the filing says the click
model began in 2002. — Date: 2000-Q1 → 2001-12-31 (display basis); 2002-Q1 exclusive cost-per-click `(PB)` —
Source path: P-A "How We Generate Revenue"; P-C Risk Factors — Source date: 2004-04-29 / 2004-08-09 — URL: as
P2G01 — Archived: as path — Tier: 1 — Class: FOUNDER CLAIM — Passage: "Advertisers paid us based on the number of
times their ads were displayed on users' search results pages, and we recognized revenue at the time these ads
appeared." (25 words) — Conf: Medium — Corroboration: 1 lineage, two printings — Conflicts: part 1 **P1CNF04**
(unchanged; this record adds the Risk-Factors sentence to the same conflict, not a new source).
independence_note: same lineage; the two sentences are one instrument's account of one mechanism.

P2Q02 Claim: A settlement of a suit over an in-window mechanism produced a quarter-level net loss after the
stage closed, which is the record's clearest example of the model's contestability. — Date: three months ending
2004-09-30 `(PB)` — Source path: P-C, Legal Proceedings — Source date: 2004-08-09 — URL: as P2G01 — Archived: as
path — Tier: 1 — Class: FACT (a preliminary estimate disclosed by the registrant) — Passage: "The charge will
result in a net loss for us in the three months ending September 30, 2004." (17 words) — Conf: Medium (the
estimate is expressly "preliminary… subject to further review and may change materially") — Corroboration: 1
lineage — Conflicts: None; §Q item 5.
independence_note: same lineage; it is quoted as a consequence of the stage's mechanism choice, and the
"RETROSPECTIVE / (PB)" label is carried into `P2TML` rows below.

P2S01 Claim: The fiscal basis is settled by the instrument's own header, so no fiscal-versus-calendar ambiguity of
the kind this project has hunted elsewhere exists in this dossier. — Date: header field, as filed 2004-04-29 —
Source path: P-A SGML header block (`FISCAL YEAR END: 1231`) — Source date: 2004-04-29 — URL: as P2G01 —
Archived: as path — Tier: 1 — Class: FACT (regulator's header data) — Passage: "FISCAL YEAR END: 1231" / "STATE
OF INCORPORATION: DE" / "SEC FILE NUMBER: 333-114984" / "PUBLIC DOCUMENT COUNT: 33" — Conf: High —
Corroboration: SEC header plus registrant covers, one instrument — Conflicts: **U.022**.
independence_note: the header is the SEC's own block, independent of the registrant's prose, which is why this row
is High; part 1's P1SRC05 already mints the header as a carrier and this pass adds the fiscal-year field to it.

P2S02 Claim: A table labelled "(unaudited)" contains years the auditor did audit, so band and label must be
tracked separately. — Date: FY2001-FY2003 — Source path: P-A and P-C Summary Consolidated Financial Data header
band; P-C "Experts" (E&Y scope, part 1 B15) — Source date: 2004-04-29 / 2004-08-09 — URL: as P2G01 — Archived: as
path — Tier: 1 — Class: FACT + INFERENCE (that the label spans attested columns) — Passage: "(in thousands,
except per share data) (unaudited)" — Conf: High — Corroboration: 1 lineage; the auditor's report is the only
independent attestation inside it — Conflicts: **U.019**, **U.018**.
independence_note: same lineage as B15; the point is presentational and it caps how §M words every early-year
figure.

P2T01 Claim: Nine lineages exist for this company and only four can carry an in-window fact. — Date: ledger as of
2026-09-29 — Source path: §T.1 (all carriers) — Source date: n/a — URL: n/a — Archived: as path — Tier: n/a —
Class: INFERENCE over the provenance ledger — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High as to the
inventory — Corroboration: n/a — Conflicts: **U.023, U.035, U.036**.
independence_note: this is §T's own census, part 1's two founder-lineages plus seven more, two of which
(LIN-SEC-INDEX, LIN-OTHERREG) witness custody or another registrant and cannot witness Google's early state.

P2T02 Claim: Reading more than one printing of one instrument produced five lineage-internal deltas, which means a
register row keyed to "the S-1" without an accession date is under-specified. — Date: 2004-04-29 → 2004-08-09 —
Source path: P-A/P-B/P-C/P-D/P-F — Source date: as listed — URL: as P2G01 — Archived: as path — Tier: 1 — Class:
FACT (each delta is two readable strings) — Passage: "up to $34 million" (April) versus "up to $25.9 million,
which includes statutory interest" (August) (14 words) — Conf: High — Corroboration: n/a (a lineage property, not
an event) — Conflicts: **U.020, U.021, U.025, U.028, U.029**.
independence_note: no delta is a second source; each is the same instrument changing, and §T.3 states the merge
rule they imply.

P2U01 Claim: This volume's anchor space is exactly U.017–U.036, declared, and every anchor is cited by a register
row. — Date: 2026-09-29 — Source path: this file, §U and `## Register rows for merge` — Source date: 2026-09-29 —
URL: n/a — Archived: n/a — Tier: n/a — Class: INFERENCE (a self-declaration for the parity gate) — Passage:
NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: n/a — Conflicts: None; upstream `U-1`–`U-16` are not
re-minted and part 1's `P1CNFnn` keys are carried unchanged.
independence_note: a bookkeeping record, filed so the merge can check declared-versus-cited anchor sets without
re-reading §U's prose.

---

## Register rows for merge

>>> REGISTER ROWS FOR MERGE <<<
STATUS: WRITTEN 2026-09-29 (alphabet-s1-p2)

*Emit-only. **No register CSV on this company was opened, created or edited by this pass** — there are none at
the company root or under `research/`; the merge owns those files. `stage` is the controlled literal `stage1` on
every row (§13 vocabulary, RD-048/RD-075); no numeric stage value appears anywhere below. Headers are copied from
the §13 schemas and match `company_001_amazon/<name>.csv` column-for-column, so drift cannot originate here.*

**Merge instructions, read before applying.**
1. **One lineage, one row.** All filing-text rows below are **LIN-REG**, the same instrument part 1 registered as
   `P1SRC04`. This pass read three printings (2004-04-29, 2004-06-21, 2004-08-09) and found five *internal*
   deltas (`U.020`, `U.021`, `U.025`, `U.028`, `U.029`). `P2SRC01`/`P2SRC02` are registered **only because a
   dated printing is required to resolve those deltas**; the merge may fold them into one LIN-REG row with the
   passages unioned — it may **not** let either raise any corroboration count. A second digitised copy is a
   replication, never a corroboration (§3, RD-127).
2. **Continue, do not re-base.** Row ids continue part 1's scheme with the `P2` volume prefix. Part 1's 70 rows
   are **not** re-emitted; where a row here addresses the same carrier (e.g. `P2GAP01` on the first licensee) the
   note says "carries forward `P1GAP01`" so the merge aliases rather than duplicates.
3. **Row addressing for the registers whose §13 schema has no id column.** quantitative and timeline rows carry
   their dossier-local tag as the first characters of `notes` (`P2QTN01 - `, `P2TML01 - `); data-gap rows carry it
   inside `gap`; decision rows are addressed by (date, decision) in block order and referenced by `P2DECnn`
   tokens in §P. **`conflicts.csv` rows are keyed to the §U anchors** (`U.017`–`U.030`) so anchor parity
   resolves; the volume-local keys `P2CNF01`–`P2CNF14` are printed inside the `section` cell.
4. **Anchor coverage.** `U.017`–`U.030` are cited by `conflicts.csv`; `U.031`–`U.036` are cited by
   `data_gaps.csv`; several are also cited in quantitative and timeline notes. Every declared anchor has a
   register row and no register row cites an anchor outside `U.017`–`U.036` (upstream `U-1`–`U-16` hyphen keys
   are not re-minted here).
5. **`(PB)` binding.** Rows carrying `(PB)` in `notes` are post-boundary evidence retained because a Stage-1
   section uses them; they may not be pulled inside the stage's own series. `stage1` is their stage *claim*, not
   their date.
6. **`derived_arithmetic` is non-empty on every DERIVED/ESTIMATE row and carries `not_derived` on FACT rows**, so
   no cell is blank; every cell containing a comma is quoted (Target's COR-06 drift class, avoided at source).
7. **Nine registers, 110 rows**: sources 11 · quantitative 32 · timeline 16 · decisions 5 · validation 7 ·
   failures 7 · channels 6 · conflicts 14 · data_gaps 12. Validation and failures share one column list per §13
   and are emitted as **one fenced block**, exactly as part 1 did; the merge must attribute them by row content
   (RD-127's known AMBIGUOUS-by-schema pair).

### sources.csv — `source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
P2SRC01,stage1,"P2G01 P2G02 P2G03 P2G04 P2G05 P2G07 P2G08 P2H01 P2H02 P2H06 P2I03 P2I07 P2I08 P2J02 P2J03 P2J05 P2K01 P2M01 P2M02 P2M03 P2N01 P2O03 P2O04 P2O05 P2O06 P2Q01 P2Q02 P2S02 P2T02 U.017 U.018 U.019 U.020 U.021 U.024 U.025 U.026 U.027 U.028 U.030","Google Inc. Form S-1, Amendment No. 5 (accession 0001193125-04-135503; header file number 333-114984)",Google Inc.; Ernst & Young LLP (auditor 2001-2003),"securities registration statement, later printing of an instrument already registered",primary,"2001;2002;2003;2003-12-31;2004-03-31;2004-06-30",2004-08-09,2026-09-29,sec.gov/Archives/edgar/data/0001288776/000119312504135503/0001193125-04-135503.txt,"sources/sec/0001193125-04-135503_0001193125-04-135503.txt (4,675,485 B; 153,452 words tag-stripped read this pass)",1,FOUNDER CLAIM for anything about 1998-2001 / FACT for the instrument's own contents and the audited band,Medium,"SAME INSTRUMENT AS P1SRC04 (LIN-REG). Registered separately ONLY because five lineage-internal deltas require a dated printing: revenue presentation basis, rescission ceiling, IPO price range, employee-count sentence, Class A Senior class. NO corroboration count may rise from this row.","Advertising revenues made up 77%, 94%, 97% and 98% of our revenues in 2001, 2002, 2003 and in the six months ended June 30, 2004.","New text this pass and NOT in part 1 or records B01-B43: the MD&A mechanism-mix sentence, the AOL single-network-member percentages, the contractual-obligations table, the Facilities paragraph, the officers' arrival months, the Indebtedness of Management note, the rescission price/range sentence, the trademark-judgment disclosure, the copyright-claim sentence, the cancellation sentence, and the Applied Semantics F-pages."
P2SRC02,stage1,"P2G06 P2J01 P2J02 P2J03 P2J04 P2J08 P2L02 P2M01 P2M02 P2O01 P2O02 P2Q01 P2S01 P2S02 P2T02 U.017 U.018 U.021 U.024 U.027 U.029","Google Inc. Form S-1 as filed (accession 0001193125-04-073639) and Amendment No. 2 (0001193125-04-105564)",Google Inc.,"securities registration statement, initial and second printings (concatenated multi-document submissions)",primary,"1999;2000;2001;2002-12-31;2003-12-31;2004-03-31",2004-04-29,2026-09-29,sec.gov/Archives/edgar/data/0001288776/000119312504073639/0001193125-04-073639.txt,"sources/sec/0001193125-04-073639_0001193125-04-073639.txt (5,719,779 B) + sources/sec/0001193125-04-105564_0001193125-04-105564.txt (2,791,396 B)",1,FACT for the instrument's own contents; FOUNDER CLAIM for 1998-2001 history,Medium,SAME INSTRUMENT AS P1SRC04. The .txt is a CONCATENATED submission (PUBLIC DOCUMENT COUNT 33): prospectus text and executed-exhibit text share one file with no delimiter this pass could find,"Since inception, we have financed our operations primarily through internally generated funds, private sales of preferred stock totaling $37.6 million and the use of our lines of credit with several financial institutions.","CARRIER WARNING for every later pass: because prospectus and exhibits are concatenated in one file, a grep cannot tell a Google figure from an acquired company's audited figure (see U.023 and P2SRC05). The April printing prints 'Net revenues', a $34 million rescission ceiling, 1,907 employees with no exclusion, and 211 mentions of Class A Senior common stock; all four differ from the August printing."
P2SRC03,stage1,"P2I09 P2T01 U.022 U.029","Form 8-K, report dated 2004-07-06 (accession 0001193125-04-115812), Second Amended and Restated Certificate of Incorporation",Google Inc.; U.S. Securities and Exchange Commission,exchange act report (a separate instrument under Commission file number 0-50726),primary,2004-07-06,2004-07-09,2026-09-29,sec.gov/Archives/edgar/data/0001288776/000119312504115812/d8k.htm,"sources/sec/0001193125-04-115812_d8k.htm (13,031 B; 2,158 chars tag-stripped)",1,FACT (a filing act; it witnesses one charter amendment and nothing before 2001),High,"NOT part of LIN-REG: an Exchange Act instrument (file 0-50726) under the same CIK. One source of its own under method 3","GOOGLE INC. … (State or other jurisdiction of incorporation or organization) California 0-50726 … This Second Amended and Restated Certificate of Incorporation implements certain changes with respect to Google s dual class common stock structure","Bridges U.029 (the Class A Senior class disappears between the June and August printings) and opens U.022 (its cover prints California while every S-1 printing prints Delaware and the SGML header prints DE). Approved by the board and stockholders on June 25, 2004."
P2SRC04,stage1,"P2I09 U.023","Exhibit 21.01, List of Subsidiaries of Registrant (accession 0001193125-04-116608)",Google Inc.,filing exhibit,primary,2004-07-12,2004-07-12,2026-09-29,sec.gov/Archives/edgar/data/0001288776/000119312504116608/dex2101.htm,"sources/sec/0001193125-04-116608_dex2101.htm (11,061 B; 834 chars tag-stripped)",1,FACT (the registrant's own list of its legal body),High,inside LIN-REG for custody; the list is a filing act and cannot witness the period,"Google Inc., a Delaware corporation List of wholly-owned subsidiaries … Google Ireland Holdings Limited … Applied Semantics, Inc., a California Corporation Kaltix Corporation, a Delaware Corporation Neotonic Software Corporation … Orkut.com LLC","(PB) 2004-07-12, three years past the close. 15 named national subsidiaries plus Google International LLC, Google LLC, and four acquired corporations. Used only for the legal shape of the group and to name the acquired entities whose financial statements sit in the same lineage (U.023)."
P2SRC05,stage1,"P2J07 P2T01 P2T02 U.023 U.036","Cover-only stub amendment (accession 0001193125-04-134174) and the Applied Semantics Inc. F-pages inside the registration lineage","Google Inc.; Applied Semantics, Inc.; Ernst & Young LLP","amendment cover text; a second registrant's audited statements filed inside the first registrant's instrument",primary,2004-08-06,2004-08-06,2026-09-29,sec.gov/Archives/edgar/data/0001288776/000119312504134174/ds1a.htm,"sources/sec/0001193125-04-134174_ds1a.htm (2,703,821 B) + accession -135503 F-37 to F-53",1,FACT about the documents; NO Google inference available,High,"The Applied Semantics statements are a DIFFERENT registrant's audited data (E&Y report dated June 20, 2003). Independent of LIN-REG narrative in origin, but usable only as counterparty context, never as a Google figure.","Please note that we are filing this amendment solely for the purpose of providing the disclosure contained in the section entitled Supplemental Notes Regarding the Rescission Offer on page i of this Registration Statement.","TWO FINDINGS. (1) Accession -134174's primary document is a COVER-ONLY stub whose entire purpose is the rescission supplemental note, with an 11,678,671 Class A / 17,174,245 Class B share split printed on it. (2) U.023: the same lineage carries Series A-1/A-2/A-3 preferred, total assets 6,218 and accumulated deficit (5,748) that belong to Applied Semantics, not Google."
P2SRC06,stage1,"P2H03 P2H07 U.034","Yahoo Internet Life, September 2001 issue",Yahoo Internet Life / Ziff Davis,periodical OCR text layer,secondary,2001-09,2001-09,2026-09-29,archive.org item yahoo-internet-life-magazine-september-2001,"sources/periodicals/yahoo-internet-life-magazine-september-2001_djvu.txt (338,899 B; 14,518 lines; 7 lines matching google)",3,CONTEMPORANEOUS OBSERVATION,Medium,"Independent of the company and inside the stage window; UNVERIFIED TLS per its .meta.json sidecar, which caps it at Medium","NETSCAPE LYCOS | lycos.com EXCITE | excite.com ALTAVISTA | altavista.com LOOKSMART | looksmart.com GOOGLE | google.com","Also carries l.12864 'How many Republicans does it take to do a Google search?' (name used as a verb phrase in window) and l.8809 'Google searches on one thing or another…'. The list's column headers are destroyed by OCR, so it is cited as a listing and NOT as a ranking. The fleet harvester mined this issue as BARE_WORD_MATCH on the term 'alphabet' - see the A4 defect note in this volume's report."
P2SRC07,stage1,"P2H05 U.034","Yahoo Internet Life, January 2002 issue",Yahoo Internet Life / Ziff Davis,periodical OCR text layer,secondary,2002-01,2002-01,2026-09-29,archive.org item yahoo-internet-life-magazine-january-2002,"sources/periodicals/yahoo-internet-life-magazine-january-2002_djvu.txt (285,579 B; 11,934 lines; 10 lines matching google)",3,CONTEMPORANEOUS OBSERVATION,Medium,Independent publisher; one month past the close so every use is (PB),each pay-for-placement search result at Overture includes a disclosure that tells you exactly how much the advertiser forked over for that position,"The corpus's only contemporaneous description of the mechanism Google did not adopt; it also prints 'Googling' as a verb (l.5643) with 'counter-Googling' reported unconfirmed. 7 lines match overture and 12 match the go-to pattern."
P2SRC08,stage1,"P2H07 U.034","Yahoo Internet Life, March 2002 issue",Yahoo Internet Life / Ziff Davis,periodical OCR text layer,secondary,2002-03,2002-03,2026-09-29,archive.org item yahoo-internet-life-magazine-march-2002,"sources/periodicals/yahoo-internet-life-magazine-march-2002_djvu.txt (258,574 B; 10,156 lines; 10 lines matching google)",3,CONTEMPORANEOUS OBSERVATION,Medium,Independent publisher; (PB) by two months; UNVERIFIED TLS cap,POWER SEARCH WITH GOOGLE / Google: Advanced Search Operators [google.com/help/operators.html],"Third-party instruction in the product's power surface: the earliest held evidence of a user-education route to acquisition. 0 hits for 'paid inclusion' in this and the three sibling issues (U.034 perimeter)."
P2SRC09,stage1,"P2H04 P2L02 U.034","Network World, four issues spanning 1998-03-30 to 1999-05-10, as a negative-result carrier",Network World / IDG,periodical OCR text layers searched,secondary,1998-03-30;1998-06-22;1999-01-11;1999-05-10,1999-05-10,2026-09-29,archive.org items bub_gb_fBsEAAAAMBAJ bub_gb_Qx4EAAAAMBAJ bub_gb_chwEAAAAMBAJ bub_gb_VA0EAAAAMBAJ,"sources/periodicals/bub_gb_fBsEAAAAMBAJ_djvu.txt 304,352 B + bub_gb_Qx4EAAAAMBAJ 307,686 B + bub_gb_chwEAAAAMBAJ 266,428 B + bub_gb_VA0EAAAAMBAJ 536,111 B = 1,414,577 B; 68,059 lines; 0 lines matching google",3,FACT about the search / UNKNOWN about the event,Medium as to meaning; the count itself is High,Four issues of one masthead: four observations of one family's silence and NOT four independent silences. Searched case-insensitively over all held lines.,NO_VERBATIM_PASSAGE_RECORDED,"A measured absence at the founding moment: the IT trade press this corpus holds never prints the company's name. Extends part 1's P1SRC10 row (which recorded the same family as searched for the founders' names). Verdict EMPTY, not UNANSWERED: the bytes were reached and read."
P2SRC10,stage1,"P2K02 U.033","XBRL early-period financial series for CIK 1288776",U.S. Securities and Exchange Commission (machine-generated frames),machine-readable financial series,secondary,2006-12-31,2010,2026-09-29,sec.gov XBRL frames for StockholdersEquity,"sources/financials/xbrl_early_series.csv (header + 1 data row)",1,FACT about the file / UNKNOWN about the window,High,Machine data independent of the company's prose; it reaches nothing in Stage 1 and its own period fields disagree,NO_VERBATIM_PASSAGE_RECORDED,"Row as held: StockholdersEquity USD (blank start) end 2006-12-31 value 17039840000 fy 2009 fp FY form 10-K frame CY2006Q4I accn 0001193125-10-030774. DEFECT REPORTED NOT WORKED AROUND: fy=2009 against end=2006-12-31 and an empty start, in a file named 'early_series'. The family's verdict for Stage 1 is EMPTY with the cause named."
P2SRC11,stage1,"P2I08 U.026","Master and sublease exhibit text inside accession 0001193125-04-073639 (Whitehall / Amphitheatre estate, Mountain View)",Google Inc. as subtenant; WXIII/AMPHITHEATRE REALTY LLC and The Goldman Sachs Group as landlord-side parties,executed real-estate instruments filed as exhibits,primary,2003;2004,2004-04-29,2026-09-29,sec.gov/Archives/edgar/data/0001288776/000119312504073639/,"sources/sec/0001193125-04-073639_dex1002.htm (159,645 B) and _dex1003.htm (336,713 B); the operative text was read from the concatenated submission P2SRC02",1,FACT (executed instruments; the counterparty is a landlord with its own reasons),High,Inside LIN-REG by custody but they are contracts not prospectus prose; they do not corroborate any 1998-2001 operating claim,"G. Sublease Premises: Four buildings including 506,317 square feet of Rentable Area, as initially described in Exhibit A to the Master Lease","The exhibit figure (506,317) contradicts the prospectus prose (approximately 506,000, P2SRC01). (PB) for Stage 1: the estate post-dates the window; retained because it is the only held quantification of physical plant and because the prose-versus-exhibit discrepancy is a carrier-level finding."
```

### quantitative.csv — `company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
Alphabet (Google Inc.),stage1,1999-12-31,net_revenues_fy1999,220,USD thousands (calendar year; NET presentation; company-prepared outside the auditor's band),P2SRC02,2004-04-29,FOUNDER CLAIM,Medium,not_derived,"P2QTN01 - printed in a table whose own header band reads (in thousands, except per share data) (unaudited). The figure part 1 cited at P1A01/B11 was never registered as a quantity."
Alphabet (Google Inc.),stage1,2000-12-31,net_revenues_fy2000,19108,USD thousands (calendar year; NET presentation; company-prepared),P2SRC02,2004-04-29,FOUNDER CLAIM,Medium,not_derived,P2QTN02 - identical value in the August printing so the year is not presentation-sensitive; the mechanism split for this year is printed NOWHERE in the corpus
Alphabet (Google Inc.),stage1,2001-12-31,net_revenues_fy2001,86426,USD thousands (calendar year; identical under both presentations; inside the auditor's band),P2SRC01 and P2SRC02,2004-08-09,FACT (attested figure in a retrospective carrier),High,not_derived,"P2QTN03 - the stage's closing-year revenue. Part 1's A.2 labelled this same figure (PB): it is IN window, since the adopted close is 2001 (year-granular). Reported as a part 1 mislabel, not re-numbered."
Alphabet (Google Inc.),stage1,1999-12-31,net_loss_fy1999,-6076,USD thousands (calendar year; unaudited band),P2SRC02,2004-04-29,FOUNDER CLAIM,Medium,not_derived,P2QTN04 - refutes part 1 record B18 that no cost or bottom-line figure exists for 1999 (U.017). Income (loss) from operations was (6516) and total costs 6736 in the same columns
Alphabet (Google Inc.),stage1,2000-12-31,net_loss_fy2000,-14690,USD thousands (calendar year; unaudited band),P2SRC02,2004-04-29,FOUNDER CLAIM,Medium,not_derived,"P2QTN05 - operating loss (14737); the loss is 0.77 of that year's net revenues, arithmetic at P2QTN31"
Alphabet (Google Inc.),stage1,2001-12-31,net_income_fy2001,6985,USD thousands (calendar year; inside the auditor's band),P2SRC01 and P2SRC02,2004-08-09,FACT (attested),High,not_derived,"P2QTN06 - the first positive bottom line the corpus holds and the arithmetic floor under the issuer's sentence 'We became profitable in 2001'. Contestable on any pre-SBC basis: same-year stock-based compensation was 12,383 (U.018)"
Alphabet (Google Inc.),stage1,2001-12-31,income_from_operations_fy2001,10964,USD thousands (calendar year; audited band),P2SRC02,2004-04-29,FACT (attested),High,not_derived,P2QTN07 - total costs and expenses 75462 against net revenues 86426 in the same row set
Alphabet (Google Inc.),stage1,1999;2000;2001,sales_and_marketing_expense,1677 / 10385 / 20076,USD thousands (calendar years; unaudited 1999-2000),P2SRC02,2004-04-29,FACT (company-prepared rows),Medium,not_derived,P2QTN08 - the acquisition-cost leg of U.027: the corpus's only quantification of paid acquisition effort inside the window
Alphabet (Google Inc.),stage1,1999;2000;2001,cost_of_revenues,908 / 6081 / 14228,USD thousands (calendar years; NET presentation),P2SRC02,2004-04-29,FACT (company-prepared rows),Medium,not_derived,P2QTN09 - the same row prints 39850 / 121794 for FY2002 / FY2003 in the April printing and 131510 / 625854 in the August printing (U.020)
Alphabet (Google Inc.),stage1,1999;2000;2001,research_and_development_expense,2930 / 10516 / 16500,USD thousands (calendar years),P2SRC02,2004-04-29,FACT (company-prepared rows),Medium,not_derived,P2QTN10 - research and development alone was 13.3x FY1999 net revenues; the ratio is carried at P2QTN31 and no causal reading is licensed here
Alphabet (Google Inc.),stage1,1999;2000;2001,general_and_administrative_expense,1221 / 4357 / 12275,USD thousands (calendar years),P2SRC02,2004-04-29,FACT (company-prepared rows),Medium,not_derived,P2QTN11 - the corpus cannot isolate the corporate cost of the unregistered-equity problem (U.021) inside this line
Alphabet (Google Inc.),stage1,2000;2001,stock_based_compensation,2506 / 12383,USD thousands (calendar years),P2SRC02,2004-04-29,DERIVED (column assignment),Medium,14228+16500+20076+12275+12383 = 75462 = printed total costs FY2001; 6081+10516+10385+4357+2506 = 33845 = printed total FY2000,P2QTN12 - the row prints SIX values across SEVEN period columns; footing the totals locates the gap at FY1999. A blank cell is not a zero and is not written as one (S.2.5)
Alphabet (Google Inc.),stage1,1999;2000;2001,total_costs_and_expenses,6736 / 33845 / 75462,USD thousands (calendar years),P2SRC02,2004-04-29,FACT (as printed),Medium,not_derived,P2QTN13 - FY1999 total costs exceed FY1999 net revenues by 30.6x; the ratio arithmetic is carried at P2QTN31
Alphabet (Google Inc.),stage1,1999;2000;2001,net_income_loss_per_share_basic,-0.14 / -0.22 / 0.07,USD per share (calendar years; RETROACTIVELY RESTATED for splits),P2SRC02,2004-04-29,FACT as printed / RESTATED in basis,Medium,not_derived,"P2QTN14 - 'the Company effected other splits in prior years' are undated, so as-issued per-share figures are unrecoverable (U.018). The diluted pair is (0.14) / (0.22) / 0.04"
Alphabet (Google Inc.),stage1,1999;2000;2001,weighted_shares_basic,42445 / 67032 / 94523,thousands of shares (restated basis),P2SRC02,2004-04-29,FACT as printed / RESTATED in basis,Medium,not_derived,"P2QTN15 - restated share counts, NOT the shares legally outstanding at the time. Diluted 2001 is 186776 thousand"
Alphabet (Google Inc.),stage1,2001-12-31,cash_equivalents_and_short_term_investments,33.6,"USD millions (period-end; a three-part aggregate, NOT cash alone)",P2SRC01,2004-08-09,FACT (inside the attested band; reported in prose),Medium,not_derived,"P2QTN16 - the nearest dated money fact to the stage close. The same sentence gives 146.3 at 2002-12-31 and 334.7 at 2003-12-31, both (PB)"
Alphabet (Google Inc.),stage1,1998-09 to 2004-06-30,private_sales_of_preferred_stock_cumulative,37.6,USD millions (CUMULATIVE since inception; not a year; not a round),P2SRC01 and P2SRC02,2004-04-29 to 2004-08-09,FOUNDER CLAIM,Medium,not_derived,P2QTN17 - supersedes part 1 Boundary 3(iii) on the narrow question of whether ANY money quantum exists for the pre-IPO period (U.024). Three printings are one lineage
Alphabet (Google Inc.),stage1,2001-07-13,series_c_preferred_purchase_by_the_chief_executive,426892 shares at 2.3425 = 999994.51,USD (transaction price; officer purchase),P2SRC02,2004-04-29,FACT (related-party table) + DERIVED check,Medium,426892 x 2.3425 = 999994.51,P2QTN18 - the only per-share price the corpus prints for an in-window date. Whether other purchasers paid it is UNKNOWN (U.032)
Alphabet (Google Inc.),stage1,2001-09-28,chief_executive_promissory_note_principal_and_rate,4.3 million at 7.38 percent,USD millions; percent per annum compounded semi-annually,P2SRC02,2004-04-29,FACT (disclosed related-party instrument; copy not held),Medium,not_derived,"P2QTN19 - 'approximately' is the filing's own hedge. Secured by 14,331,708 Class B shares; the option exercise price was 0.30; the note was repaid in full 2004-04-28 (PB)"
Alphabet (Google Inc.),stage1,2004-06-30,options_outstanding_under_the_1998_stock_plan,6295431 at weighted average exercise price 0.29,shares; USD per share,P2SRC01,2004-08-09,FACT (as filed; restated for splits),Medium,not_derived,"P2QTN20 - a plan-wide average across 1998-09 to 2004 grants, NOT a founding-day price; the observation date is (PB) while the plan's adoption (September 1998) is in window"
Alphabet (Google Inc.),stage1,2004-08-09,rescission_repurchase_price_versus_estimated_offering_price,2.86 versus a range of 108.00 to 135.00,USD per share (weighted average repurchase price; indicative range),P2SRC01,2004-08-09,FACT,Medium,(108.00+135.00)/2 = 121.50 = the assumed price printed elsewhere in the same printing,P2QTN21 - resolves where the 121.50 assumption came from and closes part 1 Boundary 3(iv) only halfway: the range is filed; the clearing price is not held (U.025)
Alphabet (Google Inc.),stage1,2002-12-31;2003-12-31,preferred_stock_issued_and_aggregate_liquidation_preference,70432 then 71662 shares issued; 40815 aggregate liquidation preference,thousands of shares; USD thousands,P2SRC01,2004-08-09,FACT (legal share counts),Medium,not_derived,P2QTN22 - eight series (A A-1 B B-1 C C-1 D D-1); the -1 pairs appear only at 2003-12-31 which is how B1 reads the 2003 reincorporation (INFERENCE Medium); Series D has no 2002 column at all
Alphabet (Google Inc.),stage1,2001;2002;2003;2004-06-30,advertising_share_of_revenues,77 / 94 / 97 / 98,percent of that period's revenues,P2SRC01,2004-08-09,FACT (band years; company statement for H1-2004),Medium,not_derived,P2QTN23 - the first mechanism split any held document prints begins at the CLOSING YEAR and closes part 1 A.4's alternative explanation for 2001 only (U.019)
Alphabet (Google Inc.),stage1,2002;2003;2004-06-30,revenue_share_from_one_network_member_aol,15 / 16 / 13,"percent of revenues (advertising and other, primarily AdSense)",P2SRC01,2004-08-09,FACT (band years),Medium,not_derived,P2QTN24 - (PB) for every Stage-1 use. Sits against the audited note that no CUSTOMER exceeded 10 percent in 2001-2003; the two measure different relationships (part 1 P1CNF02)
Alphabet (Google Inc.),stage1,2003-12-31,guaranteed_minimum_revenue_share_obligations,477.0 of which 205.1 due within 12 months,USD millions (table labelled unaudited; payments due by period),P2SRC01,2004-08-09,FACT (as filed),Medium,not_derived,P2QTN25 - (PB). Same table: operating leases 146.7 capital leases 7.4 purchase obligations 11.9 total 644.5. The company states it will not honour all of them
Alphabet (Google Inc.),stage1,2004-03-31;2004-06-30,employees,1907 then 2292 (705 research and development / 1141 sales and marketing / 446 general and administrative at the later date),persons (period-end counts),P2SRC01 and P2SRC02,2004-04-29 / 2004-08-09,FACT (company count),Medium,not_derived,P2QTN26 - (PB) both dates. April says ALL employees are shareholders; August excludes temporary employees and contractors (U.028). No in-window headcount exists anywhere
Alphabet (Google Inc.),stage1,2003-12-31,headquarters_leased_area_prose_versus_exhibit,506000 versus 506317,square feet,P2SRC01 and P2SRC11,2004-04-29 / 2004-08-09,FACT (two documents on this disk),High,506317 - 506000 = 317,P2QTN27 - (PB). The clearest carrier-level finding available: the prospectus prose rounds against its own executed sublease exhibit
Alphabet (Google Inc.),stage1,1998-03-30 to 1999-05-10,google_naming_lines_in_four_network_world_issues,0 of 68059 lines,lines matched (case-insensitive) over 1414577 bytes,P2SRC09,1999-05-10,FACT (a count measured this pass),High,not_derived,P2QTN28 - a measured absence in the IT trade press across the founding moment (U.034). NOT an absence of the company: the 1998-11-11 archive capture proves a public service existed
Alphabet (Google Inc.),stage1,2001-09,google_naming_lines_in_the_september_2001_consumer_issue,7 of 14518 lines,lines matched,P2SRC06,2001-09,FACT (a count measured this pass); the namings themselves are CONTEMPORANEOUS OBSERVATION,Medium,not_derived,P2QTN29 - UNVERIFIED TLS cap. Sibling counts measured the same way: January 2002 10 of 11934; March 2002 10 of 10156; July 2000 5 of 16051
Alphabet (Google Inc.),stage1,2002-12-31;2003-12-31,revenue_presentation_delta_within_one_lineage,91660 and 504060,USD thousands (revenue and cost of revenues move identically),P2SRC01 and P2SRC02,2004-04-29 to 2004-08-09,DERIVED,High,439508-347848 = 91660 = 131510-39850; 1465934-961874 = 504060 = 625854-121794,P2QTN30 - the gross/net reclassification is margin-neutral to the dollar (U.020); income from operations and net income are identical under both bases
Alphabet (Google Inc.),stage1,1999;2000;2001,sales_and_marketing_to_net_revenue_ratio,7.62 / 0.54 / 0.23,times revenue (dimensionless),P2SRC02,2004-04-29,DERIVED,Medium,1677/220 = 7.62; 10385/19108 = 0.54; 20076/86426 = 0.23,"P2QTN31 - set against the company's word-of-mouth acquisition claim (U.027). The expense line is not disaggregated between user-side and advertiser-side spend, so the ratio licenses no causal reading"
Alphabet (Google Inc.),stage1,2000-06;2003-06;2004-08-09,yahoo_warrant_and_settlement_share_counts,3719056 warrant shares; 1229944 issued on conversion; 2700000 issued at settlement,shares,P2SRC01,2004-08-09,FACT (disclosed instruments; the warrant agreement is not held),Medium,not_derived,"P2QTN32 - (PB) except the June 2000 origin of the arrangement. The balance-sheet trace at 2004-03-31 is a 13871 USD-thousand warrant liability (part 1 B16, same lineage)"
```

### timeline.csv — `company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
Alphabet (Google Inc.),stage1,1999-05,"a senior vice president of Worldwide Sales and Field Operations was in post, and two venture general partners were in the board room",Omid Kordestani; L. John Doerr; Michael Moritz; Google Inc.,Mountain View / Palo Alto CA,P2SRC02,FOUNDER CLAIM (retrospective biography; month granularity),Medium,None,"P2TML01 - the earliest dated organisational act the corpus holds after incorporation. Kordestani came from Netscape business development 1995-1999; Doerr of Kleiner Perkins; Moritz of Sequoia. Three rows, ONE lineage, one instrument."
Alphabet (Google Inc.),stage1,2000-11,a new Vice President of Engineering was in post,Wayne Rosing; Google Inc.,Mountain View CA,P2SRC01,FOUNDER CLAIM (month granularity),Medium,None,P2TML02 - same quarter as the AdWords launch at part 1 P1TML13. The coincidence is recorded and is NOT asserted as a mechanism.
Alphabet (Google Inc.),stage1,2001-03,an outside chief executive joined the board as Chairman,Eric Schmidt; Google Inc.; the board,Mountain View CA,P2SRC02,FOUNDER CLAIM (month),Medium,None,"P2TML03 - the stage's largest documented scaling act, first leg. Prior: Chairman of Novell from April 1997."
Alphabet (Google Inc.),stage1,2001-07,the same outside executive became Chief Executive Officer,Eric Schmidt; Larry Page; Sergey Brin,Mountain View CA,P2SRC02,FOUNDER CLAIM (month),Medium,None,P2TML04 - second leg. The four-month Chairman-then-CEO gap is the only held evidence that the transition was staged rather than sudden.
Alphabet (Google Inc.),stage1,2001-07-13,the new chief executive bought 426892 shares of Series C convertible preferred stock at 2.3425 per share,Eric Schmidt; Google Inc.,Mountain View CA,P2SRC02,FACT (related-party table; instrument copy not held),Medium,U.032,P2TML05 - the only dated priced equity transaction inside the window. Total printed 999994.51 and the product foots exactly.
Alphabet (Google Inc.),stage1,2001-09-28,the company financed its own chief executive's option exercise with a secured full-recourse note,Eric Schmidt; Google Inc.,Mountain View CA,P2SRC02,FACT (disclosed related-party transaction),Medium,None,"P2TML06 - approximately 4.3 million USD at 7.38 percent per annum compounded semi-annually, secured by 14331708 Class B shares; repaid in full 2004-04-28 (PB). The exercise itself covered Class B at 0.30."
Alphabet (Google Inc.),stage1,2001,first office outside the United States opened,Google Inc.,country UNKNOWN,P2SRC01,FOUNDER CLAIM (year granularity),Medium,None,"P2TML07 - the corpus holds no country, city, address, lease or headcount for this act; Exhibit 21.01's national subsidiaries post-date it by three years."
Alphabet (Google Inc.),stage1,2001-12-31,the stage closes on the company's own first positive bottom line: net income 6985 USD thousands,Google Inc.; Ernst & Young LLP (attesting auditor for FY2001),Mountain View CA,P2SRC01 and P2SRC02,FACT (attested figure; retrospective carrier),High,U.018,"P2TML08 - ADOPTED STAGE-1 CLOSE (part 1 Boundary 2 candidate 1), now with its arithmetic. The issuer's sentence 'We became profitable in 2001' is a characterisation; this row is the filed figure. Closing DAY remains UNKNOWN."
Alphabet (Google Inc.),stage1,2001-09,an unaffiliated consumer magazine printed Google beside Netscape Lycos Excite AltaVista and LookSmart and used the name as a verb,Yahoo Internet Life (third party),USA,P2SRC06,CONTEMPORANEOUS OBSERVATION,Medium,U.034,"P2TML09 - the corpus's only in-window independent naming of the service besides the July 2000 round-up and the 1998 capture. OCR destroyed the list's headers, so it is a listing and not a ranking."
Alphabet (Google Inc.),stage1,2000-07,searches conducted at Google.com appeared as an item in a magazine list whose basis is illegible,Yahoo Internet Life (third party),USA,P1SRC07,CONTEMPORANEOUS OBSERVATION,Low,None,"P2TML10 - the adjacent figure [8153] is NOT used: its unit, basis and list membership are unreadable in the held OCR (S.4 refusal). Carrier is part 1's P1SRC07; this row adds the second naming line, not a new source."
Alphabet (Google Inc.),stage1,1998-03-30 to 1999-05-10,the IT trade press that this corpus holds never printed the company's name,Network World (four issues),USA,P2SRC09,FACT about the search / UNKNOWN about the event,High as to the count; none as to the cause,U.034,"P2TML11 - a silence row, kept so the founding narrative cannot be pushed into 1998-1999 trade print. 0 of 68059 lines matched 'google' case-insensitively."
Alphabet (Google Inc.),stage1,2002-01,"the rival mechanism's economics were described in consumer print: per-placement price, public disclosure, syndication to AOL EarthLink Lycos and others",Yahoo Internet Life (third party); Overture (formerly GoTo.com),USA,P2SRC07,CONTEMPORANEOUS OBSERVATION,Medium,None,P2TML12 - (PB) by one month. Retained as the nearest contemporary account of the path NOT taken (H.4).
Alphabet (Google Inc.),stage1,2002-04,(PB) Overture Services sued over the AdWords mechanism; Overture also claimed the patent covered its own bid-for-placement model,Yahoo/Overture; Google Inc.,USA,P2SRC01,FACT (disclosed legal event),High,inherited U-16,P2TML13 - post-boundary by one quarter; the corpus's only documented attack on an in-window mechanism. Part 1 P1FAI03 carries the same carrier and this row does not duplicate the corroboration count.
Alphabet (Google Inc.),stage1,2003-06,(PB) 1229944 shares were issued to Yahoo on a warrant conversion provision and the two parties began to dispute the count,Google Inc.; Yahoo Inc.,Mountain View / Sunnyvale CA,P2SRC01,FACT (disclosed transaction and dispute),Medium,None,"P2TML14 - the warrant's origin sentence ties it to a June 2000 services agreement, which is in window; the issuance and the dispute are not."
Alphabet (Google Inc.),stage1,2004-07-06,"(PB) Google filed a Second Amended and Restated Certificate implementing dual-class changes, adopted by its board and stockholders on June 25 2004",Google Inc.; Delaware Secretary of State,Wilmington DE / Mountain View CA,P2SRC03,FACT (a filing act),High,U.022 U.029,P2TML15 - the legal act that explains why the Class A Senior ten-vote class disappears from the August printing. Its cover prints California as the state of incorporation.
Alphabet (Google Inc.),stage1,2004-08-06,(PB) an amendment was filed whose sole content was a rescission supplemental note,Google Inc.,Mountain View CA,P2SRC05,FACT (the stub says so on its face),High,U.021,"P2TML16 - carrier-level evidence of how the rescission problem was handled: a whole amendment carrying only that note, with 11678671 Class A and 17174245 Class B shares printed on its cover."
```

### decisions.csv — `company,stage,date,decision,state_before,information_available,unknowns,alternatives,constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date,decision,state_before,information_available,unknowns,alternatives,constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref
Alphabet (Google Inc.),stage1,2001-03 then 2001-07,"install an outside chief executive, two founders ran the company as Presidents of Technology and Products",two founders as Presidents of Technology and Products; two loss years as filed; two venture directors in post since 1999-05,whether the founders resisted and who proposed it,UNKNOWN - no appointment document or board minute exists in any family,UNKNOWN - no rejected alternative is recorded; the status quo of founder leadership is the implicit alternative,board composition; the 1998/2003 stock plans; Novell's own chairman transition,not recorded - UNKNOWN,an experienced operator in the chair,first positive filed net income in the same calendar year 2001 - RETROSPECTIVE,P2SRC02,Medium,P2I04
Alphabet (Google Inc.),stage1,2001-09-28,finance the incoming chief executive's option exercise with a company loan,option grants outstanding at 0.30 per share,the exercise price and share count; the note terms as disclosed,why the company lent rather than requiring cash,UNKNOWN - no alternative is recorded; the corpus does not even record that alternatives were considered,Delaware law and the plan terms,not recorded - UNKNOWN,the executive holds equity at once,note repaid in full 2004-04-28 (PB) - RETROSPECTIVE,P2SRC02,Medium,P2I05
Alphabet (Google Inc.),stage1,2001,open the first office outside the United States,one-country operation,nothing about the choice of country in any held document,country city and headcount at opening,UNKNOWN - no alternative market is named,UNKNOWN,not recorded - UNKNOWN,international reach,INTERNATIONAL REVENUE LATER 22 PERCENT IN 2002 AND 29 PERCENT IN 2003 (PB) - RETROSPECTIVE,P2SRC01,Low,P2I06
Alphabet (Google Inc.),stage1,UNKNOWN (printed 2004-08-09),cancel network agreements that underperform rather than honour the guaranteed minimums,"guaranteed minimum revenue share commitments of 477.0 million USD, and the practice of guaranteeing minimums at all",the obligations table and the company's own statement of practice,how many agreements were cancelled and when the practice began,UNKNOWN - the alternative of honouring all commitments is visible in the contract form itself,contract terms; the company states it holds a right to cancel at any time,not recorded - UNKNOWN,payment only for productive inventory,this row's ACTUAL RESULT IS (PB) AND IS THE SAME SENTENCE AS THE EVIDENCE - RETROSPECTIVE,P2SRC01,Medium,P2G08
Alphabet (Google Inc.),stage1,2004 (PB),price the offering by auction instead of the traditional underwriter-set method,no public market for the stock; the traditional U.S. method as the named alternative,the master order book; the underwriters,what the auction would raise and how allocations would fall,DOCUMENTED AS AN EXPLICIT ALTERNATIVE: the filing states the method 'differs from methods that have been traditionally used',underwriter economics; the registrant states price and allocation are determined by the auction,the mechanism is described; the motive is not recorded,price and allocation set by bidding,the 424B4 carrying the outcome is NOT HELD - the outcome of this decision is outside this corpus,P2SRC01 and P2SRC03,Medium,P2P02
```

### validation.csv and failures.csv — `company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes
Alphabet (Google Inc.),stage1,1999-05,two venture general partners and a worldwide sales SVP were in post at the same month,3 named individuals in one month,an organisational layer existed before the first profitable year,"the amount of money raised, who subscribed, or that either firm had invested",P2SRC02,FOUNDER CLAIM (retrospective biography),Medium,P2VAL01 - the earliest dated organisation signal in the corpus; U.024/U.032 keep it from being read as a funding event
Alphabet (Google Inc.),stage1,2000,advertising services produced revenue for the first time,first advertising revenue year (no amount attributable to the mechanism),a second revenue mechanism existed at all,which mechanism produced FY2000's 19108 USD thousands; FY2000 was still a net loss of (14690),P2SRC02,FOUNDER CLAIM,Medium,P2VAL02 - the company's own sentence pairs the two firsts; the split by mechanism is unprinted until 2001 (U.019)
Alphabet (Google Inc.),stage1,2001-07-13 and 2001-09-28,the incoming chief executive bought in and borrowed to buy in,426892 preferred shares at 2.3425 and a 4.3 million USD note,an outside executive took priced equity risk in the window,"the quality of his decision, the company's solvency, or that other buyers paid 2.3425",P2SRC02,FACT (disclosed related-party transactions),Medium,P2VAL03 - the window's only priced equity event
Alphabet (Google Inc.),stage1,2001-12-31,the first positive bottom line in the corpus,net income 6985 USD thousands on net revenues 86426 (audited band),the company finished a profitable year inside the stage,that the advertising mechanism caused it; that the profit survives an SBC-inclusive reading (same-year SBC 12383),P2SRC01 and P2SRC02,FACT (attested figure),High,P2VAL04 - the stage-close signal. Causation remains the issuer's conjunction (part 1 P1VAL06) and U.018
Alphabet (Google Inc.),stage1,2001-09,a third-party magazine printed the company inside the established engine set and used its name as a verb,7 naming lines in 14518,external public awareness of the name inside the window,"share, traffic, users or quality ranking; the list headers are destroyed by OCR",P2SRC06,CONTEMPORANEOUS OBSERVATION,Medium,P2VAL05 - UNVERIFIED TLS cap; the strongest independent in-window adoption witness this corpus holds
Alphabet (Google Inc.),stage1,2001,the first office outside the United States opened,1 office; country UNKNOWN,a geographic extension of the operating footprint,"market traction, revenue, or even which market",P2SRC01,FOUNDER CLAIM (year granularity),Medium,P2VAL06 - the only in-window expansion act with a date and nothing else
Alphabet (Google Inc.),stage1,2004-08-09 (PB),the company settled the patent attack on its in-window mechanism with a perpetual licence and shares,2700000 shares; a non-cash charge estimated at 260-290 million USD,that the mechanism adopted in 2000-2001 was contestable and could be licensed,any in-window failure; the settlement's adequacy; the final charge (expressly preliminary),P2SRC01,FACT (disclosed settlement and preliminary estimate),Medium,P2VAL07 - (PB) tag binding; retained as a consequence of the stage's own choice (Q.5)
Alphabet (Google Inc.),stage1,1999-12-31,the company's first full reported year closed at a net loss,net loss (6076) USD thousands on net revenues 220,that the founding model did not pay for itself,any causal story about why; and it is outside the auditor's attested band,P2SRC02,FACT (company-prepared),Medium,P2FAI01 - the number that part 1 record B18 said had no carrier (U.017)
Alphabet (Google Inc.),stage1,2000-12-31,the second full reported year lost more than the first,net loss (14690) USD thousands; operating loss (14737),scaling did not stop the losses,the losses were fatal; no going-concern language exists in the corpus to test that (P2FAI07),P2SRC02,FACT (company-prepared),Medium,P2FAI02 - loss equal to 0.77 of that year's net revenues
Alphabet (Google Inc.),stage1,1998-09 to 2004,equity compensation was issued without the registration or exemption the law required,"options and shares under the 1998 and 2003 plans; ceiling up to 34 million USD (April printing), 25.9 million USD (August)",the company's earliest pay practice was legally defective on its own admission,"that any payment was made, how many holders were affected, or whether the offer was accepted",P2SRC01 and P2SRC02,FACT (self-disclosed against interest),High,P2FAI03 - part 1 P1FAI02's carrier; U.021 dates the two ceilings to their printings
Alphabet (Google Inc.),stage1,UNKNOWN (disclosed 2004-08-09),courts in two jurisdictions ruled against the keyword-advertising practice and more suits were expected,"1 adverse judgment (France, appealed); mixed German outcomes; cases in the U.S., France, Germany and Italy",the monetisation mechanism adopted in the window was unlawful in at least one market,any in-window date or revenue effect; the policy change is 'recent' in 2004 copy,P2SRC01,FACT (disclosed adverse outcomes) + FOUNDER CLAIM (forecast),Medium,P2FAI04 - dates UNKNOWN because the filing does not give them; PACER UNTRIED
Alphabet (Google Inc.),stage1,UNKNOWN (disclosed 2004-08-09),third parties asserted that Google WebSearch Google News and Google Image Search infringed copyright,3 named products; claimants unnamed,the in-window product line drew third-party IP assertions,"any merits, date or outcome",P2SRC01,FACT that notices are disclosed,Medium,P2FAI05 - the sentence is also the corpus's second naming of the product 'Google WebSearch' (part 1 P1TML07)
Alphabet (Google Inc.),stage1,1998-11-11 to 2004,unreliability was admitted structurally but no incident is reported anywhere in the corpus,'not fully redundant'; 'cannot account for all eventualities'; earthquake-risk data centers,the company knew its plant was exposed,"that anything failed: NO outage, incident or downtime figure exists in any family",P2SRC01,FORECAST / disclosed condition - NOT an event,High that it is printed,P2FAI06 - class discipline: a risk factor is not a failure (O.1 rule)
Alphabet (Google Inc.),stage1,1998-09 to 2001-12-31,ABSENCE OF ANY PRINTED DISTRESS: no going-concern language and no restructuring or layoff vocabulary exists in the held filings,"0 occurrences of 'going concern', 'substantial doubt', 'restructuring', 'layoff' in both printings searched",nothing - an absence of disclosure is not a disclosure of absence,that the company was solvent or comfortable in 1999; the silence is 2004 print about 2004 obligations,P2SRC01 and P2SRC02,"UNKNOWN (a measured silence, not a finding about the event)",High as to the counts,P2FAI07 - the Stage-1 near-death narrative has NO carrier; recorded so no later pass invents one (O.2)
```

### channels.csv — `company,stage,channel,date_tested,why_tested,cost_or_effort,result,repeatability,source_id,confidence,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,channel,date_tested,why_tested,cost_or_effort,result,repeatability,source_id,confidence,notes
Alphabet (Google Inc.),stage1,direct sales force selling text ads per display and later servicing large advertiser budgets,"field sales offices in 11 countries and named offices in 23 cities by 2004; the force itself is dated 2000-Q1",to monetise traffic that licensing did not monetise,a sales organisation per customer; cost per acquisition UNKNOWN,"Premium Sponsorships ran from 2000-Q1 and were terminated effective 2004-01-01 (PB); the force later sold AdWords too","NOT self-scaling: the company built a self-service route in the same year it staffed this one",P2SRC01 and P2SRC02,Medium,"P2CHN01 - extends part 1's P1CHN02 with the 2004 field structure; one lineage, no new corroboration"
Alphabet (Google Inc.),stage1,self-service advertising with email support (AdWords),2000-Q4 launch; support structure described 2004-08-09,remove the per-customer sales conversation,advertiser-side cost only; internal cost undisclosed,FY2001 net income 6985 USD thousands in the closing year (same instrument),UNKNOWN - no advertiser count exists at any in-window date,P2SRC01,Medium,"P2CHN02 - the corpus's only evidence of the channel's shape (self-service plus optional account team) is (PB) description applied to an in-window launch"
Alphabet (Google Inc.),stage1,the AdSense revenue-share network: third-party web sites carrying Google ads,"2003 onward (PB); the network is 'thousands of third-party web sites' as of 2004",extend advertiser reach beyond the company's own sites,"most of each fee is paid to the member; guaranteed minimums of 477.0 million USD at 2003-12-31 (PB)","one member, AOL, was 15/16/13 percent of revenues 2002-2003/H1-2004","structurally repeatable but concentration-prone on the supply side",P2SRC01,Medium,"P2CHN03 - every datum is (PB); retained because it is the mechanism the in-window self-service program grew into (Q.4)"
Alphabet (Google Inc.),stage1,enterprise evaluation: a time-boxed appliance beta,60-day evaluation period per the held form (2004-11; PB),to sell search capability to institutions rather than audiences,"60 days, return within ten business days, Google's sole discretion to extend","no in-window enterprise revenue, customer or date exists",UNKNOWN,P1SRC08,High that the form says it; UNKNOWN for the channel's start,P2CHN04 - carrier is part 1's P1SRC08 (CIA-custodied Google form); this row adds only the channel reading and must not re-count the document
Alphabet (Google Inc.),stage1,un-billed traffic to web sites with no business relationship (the free-inclusion supply route),"no date in the corpus; the commitment is printed 2004-04-29",to make the index complete without buying content,foregone paid-inclusion revenue; crawling and storage cost (never quantified in window),"no measurement of the traffic the company says it gives away: 'a significant amount' is the only quantifier","assumed repeatable; unmeasured",P2SRC01 and P2SRC02,Low,"P2CHN05 - the supply-side channel is the one part 1's P1CHN04 named; this row adds the 'no business relationship' sentence and the explicit unmeasured verdict"
Alphabet (Google Inc.),stage1,third-party user education: magazines teaching the product's operators and listings,"1999-2003 press cycles; specific instances July 2000, September 2001, March 2002",not sought by Google - observed by third parties,none attributable to Google (no spend line is disaggregable),"the name appearing in a magazine list beside five established engines; an operators tutorial",UNKNOWN - the corpus cannot tell whether Google influenced any of it,P2SRC06 and P2SRC08,Medium,"P2CHN06 - the only acquisition route in this corpus with an INDEPENDENT carrier; recorded so the word-of-mouth claim (U.027) has a rival that is at least observable"
```

### conflicts.csv — `company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
Alphabet (Google Inc.),stage1,U.017,"P2CNF01; M.1; O.1; K.1","part 1 A.1 and record B18: operating detail for 1998-2000 is UNKNOWN with NO carrier, and no cost figure exists before 2003",_parts/s1_p1.md and research/B1_filing_records.md,2026-09-26,"the 2004-04-29 printing prints a full statement of operations for FY1999 and FY2000: costs by line, operating loss, net loss, per-share and share counts",P2SRC02,2004-04-29,"an absence asserted over a corpus versus a table inside that same corpus that was read only for its revenue row",the printed table outranks the census statement about it,"B18 and part 1 A.1 are REFUTED for costs and the bottom line; they SURVIVE for headcount, users, queries, index size and year-by-year cash",whether the earlier passes read only the revenue line of the same table,High
Alphabet (Google Inc.),stage1,U.018,"P2CNF02; L.1; M.1","We became profitable in 2001 following the launch of our Google AdWords program",P2SRC01 and P2SRC02,2004-04-29,the same table prints FY2001 net income 6985 and FY2001 stock-based compensation 12383,P2SRC02,2004-04-29,a characterisation versus the arithmetic underneath it,both are the issuer's own figures in one instrument,"profitable is true on a GAAP net-income basis and contestable on any pre-SBC or cash basis; the sentence does not say which it means",which basis the sentence intends - UNKNOWN,Medium
Alphabet (Google Inc.),stage1,U.019,"P2CNF03; A.4 carried forward; Q.1","part 1 A.4: the disclosure is compatible with licensing remaining the larger share of revenue past Q1 2000 and no held line apportions revenue",_parts/s1_p1.md,2026-09-26,"Advertising revenues made up 77%, 94%, 97% and 98% of our revenues in 2001, 2002, 2003 and in the six months ended June 30, 2004",P2SRC01,2004-08-09,a stated possibility versus a printed percentage in a region of the lineage part 1 did not quote,B is printed and inside the auditor's band for 2001,"FOR 2001 the alternative is CLOSED (advertising 77 percent). For 1999-2000 nothing is printed and A's caution still governs those years",the composition of the 2001 non-advertising 23 percent,High as to 2001
Alphabet (Google Inc.),stage1,U.020,"P2CNF04; S.2.1; M.2","Net revenues 347848 (FY2002) and 961874 (FY2003), labelled NET",P2SRC02,2004-04-29,"Revenues 439508 (FY2002) and 1465934 (FY2003), same instrument family",P2SRC01,2004-08-09,a presentation change for traffic-acquisition and revenue-share costs between printings of one registration statement,"both filed; income from operations and net income are identical under both",the reclassification is MARGIN-NEUTRAL to the dollar: the same 91660 and 504060 move in revenue and in cost of revenues,what the in-window years would show under the gross basis; FY2001 is identical either way so 1999-2000 are untestable,High as to arithmetic
Alphabet (Google Inc.),stage1,U.021,"P2CNF05; O.1 row O-4; T.3","rescission exposure: aggregate payments of up to 34 million USD plus statutory interest",P2SRC02,2004-04-29,aggregate payments to the holders of these shares and options of up to 25.9 million USD which includes statutory interest,P2SRC01,2004-08-09,the exposure is computed from prices and the prices the computation used differed,a revision inside one lineage,"one instrument family re-estimating a contingent liability; part 1's B25 value must be dated to its printing when the merge keys it",the driver of the 8.1 million USD difference is not stated; neither figure is an incurred cost,High
Alphabet (Google Inc.),stage1,U.022,"P2CNF06; S.1; S.2.7","Form 8-K cover: GOOGLE INC. … State or other jurisdiction of incorporation California 0-50726",P2SRC03,2004-07-09,every S-1 printing cover prints Delaware and the SGML header prints STATE OF INCORPORATION: DE,P2SRC01 and P2SRC02,2004-04-29 to 2004-08-09,an Exchange Act registrant cover carried from the earlier California record versus a Securities Act cover drawn from the current charter,"the S-1 covers plus the SEC header agree against one 8-K cover",a stale or form-carried field and not a re-domiciliation; part 1's CA-1998 to DE-2003 break stands unaltered,whether EDGAR's registrant record still showed California in July 2004 - UNKNOWN; registry route UNTRIED,Medium
Alphabet (Google Inc.),stage1,U.023,"P2CNF07; M.4; T.1","a 2002 balance sheet with Series A-1/A-2/A-3 preferred, total assets 6218, cash 1953 and accumulated deficit (5748) appears in the held registration text",P2SRC05 and P2SRC01,2003-06-20 (audit date),the same pages are headed Applied Semantics Inc. BALANCE SHEET and are attested by an Ernst Young report for that company,P2SRC05,2003-06-20,one registrant's filing carrying a second registrant's audited statements after an April 2004 acquisition,the F-page headers are explicit,NO Applied Semantics figure is a Google figure and none may be read as one,attribution is settled; what remains unknown is nothing,High
Alphabet (Google Inc.),stage1,U.024,"P2CNF08; J.0; K.1","part 1 Boundary 3(iii): no pre-IPO funding round; the closest the corpus comes is a valuation recital",_parts/s1_p1.md,2026-09-26,private sales of preferred stock totaling 37.6 million USD since inception,P2SRC02,2004-04-29,a claim about absence versus a printed aggregate in a region of the lineage not quoted by the earlier pass,the printed aggregate is closer than a recital,THE REFUSAL OF A NAMED AND DATED ROUND STANDS; the claim that no money quantum exists is RETRACTED,per-round dates subscribers and amounts - EMPTY,High as to the sentence
Alphabet (Google Inc.),stage1,U.025,"P2CNF09; J.5; M.2","part 1 Boundary 3(iv): no IPO price; 121.50 is an assumed price in a registration statement",_parts/s1_p1.md,2026-09-26,our current estimated initial public offering price is between 108.00 and 135.00 (August printing only; the April cover range field is blank),P2SRC01,2004-08-09,an assumption for dilution maths versus a filed indicative range,"(108.00+135.00)/2 = 121.50, so the two are consistent and the assumption's source is now known",part 1's refusal of the ACTUAL price stands: the 424B4 of 2004-08-19 is enumerated and NOT held,the clearing price and first trade - UNANSWERED by custody,High for the arithmetic
Alphabet (Google Inc.),stage1,U.026,"P2CNF10; K.2a; I.2","the April printing's 5 percent rows print KPCB Holdings 23893800 and Sequoia Capital 23893800, the same figure against both names",P2SRC02,2004-04-29,the August printing prints Entities affiliated with Kleiner Perkins Caufield & Byers 21043711 and Entities affiliated with Sequoia Capital 23893800,P2SRC01,2004-08-09,two printings of a multi-column beneficial-ownership table whose column boundaries are carried by stripped markup,neither reading is verifiable without the exhibit's table structure,NO ownership-table figure is used as a quantity in this volume; the row exists to stop a later pass quietly using one,which column each number sits in - UNANSWERED on the held layer; a table-aware parse is UNTRIED,Medium that the strings print as quoted
Alphabet (Google Inc.),stage1,U.027,"P2CNF11; G.2; G.4","We have found that offering a high-quality user experience leads to increased traffic and strong word-of-mouth promotion",P2SRC01 and P2SRC02,2004-04-29,sales and marketing expense of 1677 / 10385 / 20076 USD thousands against net revenues of 220 / 19108 / 86426 in the same years,P2SRC02,2004-04-29,a causal self-description written in 2004 versus a filed expense line,B has the auditor's band from 2001 and is arithmetic-free; A is unmeasured,the company paid for sales and marketing at multiples of revenue while attributing user acquisition to unpaid word of mouth; the line cannot be split by target,what the money bought - UNKNOWN,Medium
Alphabet (Google Inc.),stage1,U.028,"P2CNF12; I.1","At March 31 2004 we had 1907 employees … All of Google's employees are also shareholders",P2SRC02,2004-04-29,At June 30 2004 we had 2292 employees … All of Google's employees except temporary employees and contractors are also equityholders,P2SRC01,2004-08-09,a date roll plus an inserted exclusion and a renamed noun inside one instrument family,both printed; neither attests a stage period,a substance-narrowing or a drafting correction - the corpus cannot choose; the April sentence must not be quoted as the company's position,the window's headcount remains UNKNOWN either way,High that the strings differ and Low as to why
Alphabet (Google Inc.),stage1,U.029,"P2CNF13; J.2; S.2","Class A Senior common stock, ten votes per share, 300000 authorised and 162566 issued and outstanding (211 mentions in the April text, 10 in the June)",P2SRC02,2004-04-29 and 2004-06-21,the August printing converts only all outstanding shares of our preferred stock and does not carry the class,P2SRC01,2004-08-09,a pre-offering recapitalisation between printings of one instrument,bridged by a held document: the 8-K of 2004-07-06 implements changes to the dual class structure,a documented legal act explains the disappearance; and because Senior is a VOTING class it must not be mis-read as an unstated financing round,who held the class and what they received beyond share-for-share reclassification,Medium-High for the bridge and (PB) throughout
Alphabet (Google Inc.),stage1,U.030,"P2CNF14; K.2b; M.4","the MD&A ratio table prints seven value columns under three header groups beginning 16.5 29.9 42.7 48.4 46.6 36.5 47.5",P2SRC01,2004-08-09,the absolute table above it reconciles to the dollar for 2001 2002 and 2003 leaving two columns without an identifiable period,P2SRC01,2004-08-09,a presentation and measurement problem in the tag-stripped layer,not a dispute between sources,the ratio table is EXCLUDED from every quantity in this volume,its geometry is recoverable only from a table-aware parse of the exhibit HTML - UNTRIED,High as to the measurement failure
```

### data_gaps.csv — `company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task
Alphabet (Google Inc.),stage1,P2GAP01 - U.031 identity of the first licensee and of any named in-window customer (carries forward P1GAP01),no document of any of the five families names one; this pass re-ran the search over the two printings part 1 did not read,High,one sentence 'We began licensing our WebSearch product in the first quarter of 1999' plus the audited no-customer-over-10-percent ceiling and the product name in the copyright sentence,UNKNOWN,EDGAR full-text search for 'WebSearch' and 'Google Inc.' over 1999-2004 counterparty filings - scripted intake not agent web work; command in ## Untried
Alphabet (Google Inc.),stage1,P2GAP02 - U.032 per-round dates subscribers and amounts inside the 37.6 million USD aggregate,no stock purchase agreement term sheet or investors rights agreement is held for this company; 'Sutter Hill' and 'Khosla' return 0 occurrences in three printings,High,"the aggregate sentence, the eight-series ladder at 2002 and 2003-12-31, one priced officer purchase at 2.3425 on 2001-07-13, and the 8000000 post-money recital in the Stanford exhibit",UNKNOWN,run sec_intake auto for CIK 1288776 with a 2004-08-01 to 2006-12-31 window to land the 424B4 and its Exhibit 4 series; command in ## Untried
Alphabet (Google Inc.),stage1,P2GAP03 - U.033 headcount users queries index size and plant for 1998-09 to 2001-12,the company disclosed none before it had to; no third-party measurement was reached; the XBRL family holds one row for 2006-12-31,High,officer arrival months only plus 'We opened our first office outside the U.S. in 2001',UNKNOWN,third-party audience measurement print for 1999-2001 (Jupiter Nielsen//NetRatings SearchEngineWatch) is UNTRIED; a 1999-2001 Wayback capture ladder for google.com is still UNTRIED
Alphabet (Google Inc.),stage1,P2GAP04 - U.034 why the IT trade press this corpus holds never named the company 1998-1999,a silence over bytes cannot carry a cause,Medium,0 of 68059 lines across four Network World issues 1998-03-30 to 1999-05-10,UNKNOWN,extend the periodical perimeter to other titles and the seven unheld Yahoo Internet Life issues 1999-2001; command in ## Untried
Alphabet (Google Inc.),stage1,P2GAP05 - U.030 the column geometry of the MD&A ratio table and of the beneficial-ownership tables,tag-stripping destroys column boundaries in a five-megabyte concatenated submission,Medium,the absolute table foots exactly and is used instead; every ratio-table value is refused,UNKNOWN,a table-aware HTML parse of ds1a/ds1.htm exhibit tables (csv-reading the row and column structure rather than flattening tags); command in ## Untried
Alphabet (Google Inc.),stage1,P2GAP06 - U.035 the actual initial public offering price and first trading day,the 424B4 dated 2004-08-19 is enumerated in the index and is NOT held on disk; re-verified twice this pass over 131 files,High,the filed estimated range 108.00 to 135.00 in the August printing and the assumed 121.50 midpoint,UNKNOWN,python tools/sec_intake.py auto 1288776 --company-dir founders_playbook/01_companies/company_005_alphabet (scripted; do not fetch by hand)
Alphabet (Google Inc.),stage1,P2GAP07 - U.022 the registrant's own state-of-incorporation record history,one held instrument prints California and the lineage prints Delaware; no registry source has been queried,Medium,the 8-K cover field and the S-1 covers side by side,UNKNOWN,California and Delaware Secretary of State entity lookups - UNTRIED by every pass; command in ## Untried
Alphabet (Google Inc.),stage1,P2GAP08 - the dates and outcomes of the French German and US trademark cases over keyword advertising,the filing discloses the rulings without dating them and no court record is held,Medium,'A court in France has held us liable for allowing advertisers to select certain trademarked terms as keywords. We have appealed this decision.',UNKNOWN,PERLEX or PACER docket search for Google trademark and patent matters 2002-2004 - UNTRIED
Alphabet (Google Inc.),stage1,P2GAP09 - whether any rescission offer was accepted and what it cost,only the offer and its computed ceilings are printed,Medium,up to 34 million USD in the April printing and 25.9 million USD in the August with a 2.86 weighted average repurchase price,UNKNOWN,PACER for the rescission-related matters and later filings for the outcome - UNTRIED; both ceilings are (PB) statements
Alphabet (Google Inc.),stage1,P2GAP10 - U.036 the invention's own gestation and inventorship history,a 1997 priority-date string on the patent page is host-disclaimed and no USPTO event history is held,Medium,1998-01-09 filing date attested twice (registry plus co-signed licence recital),UNKNOWN,the USPTO Global Dossier and assignment chain for application US09/004827 - UNTRIED; this is the route that could move the stage opening
Alphabet (Google Inc.),stage1,P2GAP11 - the identity and terms of the counterparty behind the 2001-07-13 Series C round other than the officer buyer,the related-party table names the buyer not the issuer of the round,High,426892 shares at 2.3425 per share totalling 999994.51,UNKNOWN,read the Exhibit 4 and 10 series of the 424B4 once intake lands it (P2GAP06) - UNTRIED as a set
Alphabet (Google Inc.),stage1,P2GAP12 - the interior voice of the period: any memo rejected option dissent or feasibility study,nothing of 1998-2001 survives in or was reached by any family; this pass found no new internal document in the two printings it opened,High,nothing; method 2's record-selection null is the answer and not a gap to fill,UNKNOWN,recorded as a permanent null with its cause; family (e) documentary and auction records remain UNTRIED (carried from part 1 P1GAP09 and not re-minted)
```

---

## Untried

STATUS: WRITTEN 2026-09-29

**Nothing below was attempted by this pass.** Each is a route, with the command or query that would attempt it.
None may be reported as a null, and none was dropped because it looked unpromising: seven other agents are live
and §15.1 assigns document retrieval to scripts, not to this dossier.

1. **The 424B4 (2004-08-19), and the exhibit series that travels with it.** `python tools/sec_intake.py auto
   1288776 --company-dir founders_playbook/01_companies/company_005_alphabet` — this is the single highest-value
   untried route in the dossier: it would settle U.025 (the clearing price), P2GAP02/`P2GAP11` (the round paper,
   the Alphabet analogue of Nvidia's Ex-4.3 signature pages), and part 1 P1GAP05.
2. **Accession 0001193125-04-138034's text** (index page only on disk, so its Securities Act file number is
   UNTESTED and it is the gap that could resolve part 1's P1CNF01): `python tools/sec_intake.py auto 1288776
   --company-dir founders_playbook/01_companies/company_005_alphabet` with that accession, or the direct
   `…/Archives/edgar/data/1288776/000119312504138034/` listing.
3. **EDGAR full-text search for counterparty filings naming the first licensee.** `python tools/ia_text.py` is the
   wrong tool; the route is `sec_intake` against each candidate licensee's CIK plus a full-text query for
   `WebSearch` over 1999-01-01..2001-12-31. Never run by any pass (P2GAP01).
4. **California and Delaware Secretary of State entity records for Google Inc.** Never queried by any pass. This
   is the only route that can move the founding **day** from UNKNOWN (part 1 P1GAP02) and it is also the route
   that would resolve U.022. Registry queries are not web-search work; they are a scripted or hand-filed lookup,
   and no such lookup exists in this repository's tool set — **a tool gap, named as such.**
5. **USPTO Global Dossier / assignment chain for application US09/004,827 (patent 6,285,999).** Would test the
   1997-01-10 prior-art-date string the patent host disclaims (part 1 P1CNF07) and any earlier provisional — the
   only evidence that could move the stage opening earlier than 1998-01-09. Command shape: `curl`-equivalent
   fetch of the PatentCenter event history, or an intake script entry; **not run.**
6. **PACER / PERLEX docket retrieval** for (a) the Overture patent suit filed April 2002, (b) the French, German
   and US keyword-trademark matters, (c) the rescission-offer aftermath. None attempted; all three would move
   U.021, P2GAP08 and P2GAP09 from disclosure-level to record-level evidence.
7. **A table-aware parse of the registration statement's exhibit tables** (beneficial ownership; the MD&A ratio
   table; the capitalization note). A row-and-column CSV read of `ds1.htm`'s table markup instead of tag
   flattening. Would resolve U.026 and U.030. `python tools/gates.py` has no such capability and no script in
   `tools/` does this — **reported as an intake gap, not worked around by hand.**
8. **The remaining *Yahoo Internet Life* issues 1999-01 through 2001-12 and the four sibling issues already
   identified as missing from the held set** (the mine covers 6 of 8 held items and none of the unheld ones):
   `python tools/periodical_harvest.py --task alphabet` — note that the harvester's Alphabet query block uses the
   bare slug `alphabet` as the company word, which RD-124 forbids; **until that block names `google`, `Google
   Inc.`, `google.com`, `Page` and `Brin`, a harvest verdict for this company is about the word 'alphabet' and
   must not be read as a naming census.** Reported to the tool owner; not patched here.
9. **Third-party audience-measurement print for 1999-2001** (Jupiter Media Metrix, Nielsen//NetRatings,
   SearchEngineWatch rankings) and the trade journals that carried them: never searched by any pass in this
   corpus. The only route to an in-window user, query or traffic number (P2GAP03).
10. **A 1999-2001 Wayback capture ladder for google.com** and retries of the four CDX queries that returned HTTP
    503 (bare host twice, `www`, and `google.stanford.edu`): `web.archive.org/cdx/search/cdx?url=…` per
    `sources/wayback/` sidecars. Those five failures are UNANSWERED, not nulls (U.035), and the Stanford-host
    history would bear directly on part 1's P1CNF06.
11. **The CIK 1652044 archive slice** that 404'd in the probe's run (inherited U-2, part 1 P1GAP08):
    `python tools/sec_intake.py index --cik 1652044 --company-dir founders_playbook/01_companies/company_005_alphabet`
    — still untried by this pass.
12. **Documentary and auction records (family (e) of §14 rule 6).** Never attempted for this company at any
    stage; carried forward from part 1 P1GAP09 as the family whose absence caps the founding-end tier.
13. **Microsoft's own filings** to test the "more than 20 times as many employees" claim at P2H02: not fetched
    (another company's directory is not this pass's to write, and the comparison is the registrant's assertion,
    not a held fact).
14. **Stanford University Archives and the Stanford technical-report series** (the docket-number convention read as 96-213 in the licence recital, the
    doctoral status of both founders — part 1 P1GAP03): never attempted.
15. **The 1998-12-01 Original Agreement itself** (the licence held on disk is the 2003-10-13 restatement; the
    original's money fields, if they exist outside a confidential-treatment grant, are unretrieved): no attempt
    at the SEC confidential-treatment applications index.

---

## Coverage note for this pass

Sections written: Header(part 2), **G H I J K L M N O P Q R S T U**, claim records, register rows, Untried.
Claim records on disk: **56** (`P2G01`–`P2G08`, `P2H01`–`P2H07`, `P2I01`–`P2I09`, `P2J01`–`P2J08`,
`P2K01`–`P2K02`, `P2L01`–`P2L02`, `P2M01`–`P2M03`, `P2N01`, `P2O01`–`P2O07`, `P2P01`–`P2P02`,
`P2Q01`–`P2Q02`, `P2S01`–`P2S02`, `P2T01`–`P2T02`, `P2U01`). Anchors declared **U.017–U.036 (20)**; anchors
cited by register rows: the same 20. Registers emitted: **110 rows in 9 registers** (see the block counts,
verified by line count before reporting). Files opened and cited: the three registration printings named in the
Header plus the 8-K, the stub amendment, Exhibit 21.01, the sublease exhibit text, seven periodical layers with
their sidecars, and the XBRL series. Files **not** opened by this pass and therefore **not** cited: the Stanford
licence exhibit (used only through part 1's rows), the Wayback capture bytes (used through part 1), the patent
grant record (used through part 1), `research/A2_periodical_settlement.md` and `research/A_chronology_feasibility.md`
(read for their record keys, not mined for new text).




