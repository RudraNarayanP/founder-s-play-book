# FORENSIC LONGITUDINAL DATASET — JOHNSON & JOHNSON, STAGE 1 (PROPOSED WINDOW 1886*–87 → 1904-12-31)

**Volume 1 of 1 — Header, Stage boundary, sections A–U, claim records and the register application record. Tier T2 core — PROVISIONAL (inherited, not re-tiered).**

## MERGE RECORD (assembly, application, id map, folds, anchor parity, carry-forward)

Merged 2026-10-07 by `merge-jnj` from the single part `_parts/s1_p1.md` (author `s1-jnj-p1`, **32,410 words**
as emitted, §A–§U complete, 23 claim records, 12 conflict anchors). **Section letters, claim ids and conflict
keys are the author's and were not renumbered** (method §9.3 — numbering continues, never re-based). Nothing in
the narrative was rewritten, trimmed, re-tiered or merged away. `_parts/` is **read-only** to this pass: the
part file was read, not edited, and carries no merge footer here (the merge-log record of supersession lives
in `03_quality_control/jnj_s1_merge.md`). The correction ledger for this operation is `CORRECTIONS.md`.

**What was moved out of the prose.** The part's nine fenced `csv` register blocks (**102 rows**) are register
data, not narrative (method §13); they were applied to the nine CSVs at this root and the `## registers` heading
now points at that application instead of repeating the blocks. Their verbatim text survives at
`_parts/s1_p1.md` l.1304–l.1474. Claim records **are** narrative: all 23 stay inline in their §X.3 subsections.

### Register application (requested ↔ applied, measured on the bytes written)

| register | rows requested | rows applied | cols | key / integrity check |
|---|---|---|---|---|
| `sources.csv` | 16 | **16** | 18 | keys S4463–S4478, 0 duplicates |
| `quantitative.csv` | 21 | **21** | 12 | 0 duplicate row texts |
| `timeline.csv` | 18 | **18** | 11 | 0 duplicate row texts |
| `decisions.csv` | 8 | **8** | 15 | 0 duplicate row texts |
| `validation.csv` | 7 | **7** | 11 | bound by content (see below) |
| `failures.csv` | 5 | **5** | 11 | bound by content (see below) |
| `channels.csv` | 4 | **4** | 11 | 0 duplicate row texts |
| `conflicts.csv` | 12 | **12** | 15 | keys U.001–U.012, 0 duplicates |
| `data_gaps.csv` | 11 | **11** | 8 | 0 duplicate row texts |
| **TOTAL** | **102** | **102** | — | **0 unapplied, 0 folded, 0 added by the merge** |

Every header is **byte-identical** to the corresponding Amazon conformant register header (asserted by string
equality against `company_001_amazon/<name>` before writing), `stage` is the literal **`stage1`** on all 102 rows
(never a bare number), and the width/duplicate-key pass was run **across every block of this one operation
together, not per block**: 0 rows off-header-width, 0 empty cells, 0 duplicate keys in the two keyed registers.
Rows were re-serialised through `csv.writer` (LF, UTF-8, no BOM, trailing newline, RFC-4180 quoting) so no
register can be shifted by an unquoted comma. **The author withheld no register row, and the merge applied every
requested row; there is no unapplied row to name.**

**Reconciling the requested total (a defect found at merge, not a row to delete).** The part's `## registers-part-2`
line reads "16+21+18+8+7+5+4+12+11 = **101**". That per-register breakdown is authoritative — it matches this
application table and the `merge_census.py` request side **exactly** (sources 16, quantitative 21, timeline 18,
decisions 8, validation 7, failures 5, channels 4, conflicts 12, data_gaps 11) — but the nine numbers **sum to
102, not 101**: the `= 101` is an arithmetic slip in the author's own tally. The merge applied all **102** emitted
rows and did **not** drop a real row to reach the headline figure (cutting evidence to fit a number is forbidden,
method §9.6). The task's "101 requested" is the same mis-sum; the honest count against the per-register request
is **102 applied, 0 unapplied**.

### Provisional-to-global id map (the only place `P1Sxx` bind; minted centrally)

Minted with `python tools/id_mint.py --count 16 --company company_045_jnj --claim --agent merge-jnj` →
**S4463 … S4478** (contiguous, 16 ids, claimed in `00_universe/_ID_BLOCKS.tsv`). The `--audit` before the mint
read a lower `next assignable` value than the block it returned, because by the time this mint ran a **concurrent
merge** had already taken the intervening block, so the tool allocated strictly **above the highest live id** and
returned S4463–S4478 — this is the coordination the tool exists to provide, and no gap (including the
`S4222–S4229` Microsoft/Target collision the task names) was re-entered or touched. Register rows carry the
minted globals; the narrative keeps the author's local tags and is keyed by this table.

| local | minted |
|---|---|
| `P1S01` | **S4463** |
| `P1S02` | **S4464** |
| `P1S03` | **S4465** |
| `P1S04` | **S4466** |
| `P1S05` | **S4467** |
| `P1S05b` | **S4468** |
| `P1S06` | **S4469** |
| `P1S07` | **S4470** |
| `P1S08` | **S4471** |
| `P1S09` | **S4472** |
| `P1S10` | **S4473** |
| `P1S11` | **S4474** |
| `P1S12` | **S4475** |
| `P1S13` | **S4476** |
| `P1S14` | **S4477** |
| `P1S15` | **S4478** |

| `P1S05b` | **S4468** | (American Druggist Vol XLI, the `b`-suffixed second Vol-1902 volume — one distinct row) |

**Folds applied: none.** No row was folded into another, no register was deduplicated on similarity, and no
`P1Sxx` lineage was minted twice — 16 rows → 16 contiguous ids. The two house-print volumes (P1S01/P1S02) and
the two Vol-1902 Druggist volumes (P1S05b/P1S07) stay **separate carrier rows** because the dossier's whole
argument is the L1-vs-L2 lineage split; keeping them apart is the finding, not a duplication to collapse.

**`validation.csv` vs `failures.csv` — adjudicated by content, the reason recorded.** The two registers share a
byte-identical 11-column header, so the census reports the pair `AMBIGUOUS` and cannot bind them (expected, not a
defect). The author emitted them as **two separate fenced blocks under distinct `### validation.csv` /
`### failures.csv` headings**; the merge bound each block on that heading **and** on row content: the 7-row block
is positive demonstration signals (outsider-reported 1896 capacity addition, the 1897 self-publish, the price
compact, the branch opening, the marriage gloss) → `validation.csv`; the 5-row block is adverse/record-selection
signals (the lost stamp-tax determination, the imitation bill, the broken price ring, the illegible price cut, and
the ABSENCE-OF-ANY-ESTABLISHED-FAILURE null) → `failures.csv`. Bound to first-row `notes` cells and logged as
`CORRECTIONS.md` **COR-02**. The content split is a HINT for the reader, not proof; the block headings are the
authority.

**Anchor parity, proven by the census, not asserted.** The part declares twelve anchors **U.001–U.012** and
writes a §U section for each; `conflicts.csv` carries exactly twelve rows keyed U.001–U.012. `merge_census.py
--verbose` re-run after the final write reads `conflicts.csv | requested 12 | present 12 | missing 0`. The
`sources.csv` line still lists the sixteen `P1Sxx` tags as missing keyed rows — the **expected residue of a
central mint** (S4463–S4478 are present; the local tags live only in the read-only part and in the map above).
1:1 anchors↔conflicts parity holds with no orphan and no unanchored row.

**Two things carried, not averaged.** (i) **The origin stays a range inside a retrospective.** `1886-*87 (the date
of the formation of the firm)` is written as a range — the asterisk is OCR and `1886-'87` occurs **0 times in
held bytes** — and the company's *later* collapse of that range into the single year 1886 plus the corporate leg
(`began in business in 1886; in 1887 they became a corporation`) is the **finding**, carried at **U.001/U.002**.
Brothers are **roles only**: 0 founder-adjacency lines across three tests, 0 "three brothers", no Band-Aid
(**U.005**). (ii) **The three self-supersessions survive the merge unchanged** — a "not found" line-bound
incorporation regex defeated by a line-broken two-column sentence (**U.002**), `asepsissecunduma00john` authorship
printed on its own title page (**U.004**), and `redcrossnotes01` dated ≥1919 by its own copyright legs, pushing
the retrospective lag past 33 years (**U.006**); plus the `americandruggis07` L45597 **locator/classification
defects** — a New York Red Cross incorporator, not a company naming (**U.009/U.010**). None was smoothed over.
**Stage 1 window** is the author's **1886*–87 → 1904-12-31**; the harvester's 1886→1960 bracket is rejected as a
retrieval setting, not a boundary (**§Boundary 4; U.012**).

**Carry-forward.** `## FIVE FAMILIES`, `## Untried` (U1–U10) and the FETCH REQUEST routes FR-1…FR-4 are carried
below **verbatim** from the part, together with `## What this pass refused to claim`. Family (d) stays
**TRIED–ANSWERED, richest and self-narrative (504 of 642 namings)**; (c) is **the independent one**; (b) and (e)
stay **UNTRIED** — (b) because `tools/web_domains.json` has no `jnj` domain (no route, never a null), (e) because
no auction tool exists at all. **`data_gaps.csv` follow-up cells carry FR-1…FR-4** and the UNTRIED routes U6/U7;
the tier is **T2 core — PROVISIONAL**, inherited not re-tiered (**U.008/U.012**).

**Counts.** Words and bytes of this volume, rows per register and the late-arrival accounting
(**15 layers / 23,308,643 B / 642 namings vs the probe's 14 / 23,275,060 / 619**) are published live in
`_MANIFEST.md` (method §9.6), `wc`-measured after the last write. **32,410 words is above the T2 22,000 density
target and under the §9.2 60,000 hard cap — kept as ONE volume, the overage logged as advisory, nothing trimmed**
(`gates.py --tier core`; `--tier auto` cannot read a table-row verdict, so the explicit tier was passed).

### Corrections issued at merge — `CORRECTIONS.md` COR-01…COR-04 (propagation, not rewriting)

| id | what it binds | register cell(s) carrying it | this volume |
|---|---|---|---|
| **COR-01** | dossier-local `P1Sxx` keys are superseded in the live registers by the minted ids **S4463–S4478**; no register row may keep a `P1Sxx` `source_id` | `sources.csv` S4463 `notes` | the id map above; §T, §U and the claim records keep the local tags as reading keys, bound by that table |
| **COR-02** | the 7-row and 5-row emissions are bound to `validation.csv` and `failures.csv` on row content — the two registers share a header, so the census cannot bind them and must not be read as leaving them unassigned | `validation.csv` first row `notes`; `failures.csv` first row `notes` | the adjudication paragraph above; §L and §M |
| **COR-03** | the late-arrival accounting and the harvest-NULL-vs-bytes finding (U.011) are preserved at merge and must not be lost when the probe's 14/619 figures are superseded by 15/642 | `quantitative.csv` census row `notes`; `timeline.csv` 1970 row `notes` | §T, `## FIVE FAMILIES` and `_MANIFEST.md` |
| **COR-04** | three `quantitative.csv` `source_date` cells that read bare `UNCONFIRMED` are aligned to the carrier's own established publication date, **`UNCONFIRMED (>=1919)`** (U.006) — the merge added the year the dossier's finding supplies and removed nothing | the three cotton-estimate rows `source_date` + `notes` | the MERGE RECORD note above; §D, §P, §T |

**No COR entry re-tiers, re-dates, re-values or deletes anything.** No row was folded: **102 emitted, 102
applied.** The annotations above are appended to existing cells and change no value.

---

## Header

STATUS: WRITTEN 2026-10-07

### Dataset, stage, tier, and how to read this volume

*One document split for the file cap (method §9.3). Section letters, claim IDs, metric IDs and conflict
numbering run continuously across volumes.* **§Header, §Boundary, §A–§U and the register append blocks
live here (`_parts/s1_p1.md`).** Cross-references of the form `(J&J S1 §U.004, part_1)` name the volume.
Nothing is renumbered to make a part look self-contained. **Tier: T2 core — PROVISIONAL**, issued by the
Stage-1 probe (`research/A_chronology_feasibility.md` §4, RD-112) against the search bracket
1886-01-01 → 1960-12-31 on the strength of **two** families returning in-window Tier-1 text ((c) periodical
corpora, (d) digitised corporate print). T2 deliverable = evidence-bound §A–§U, full registers, and claim
records **for load-bearing claims only** (§15.2). I do not re-tier: two families is two families, and I
found no third in-window family on this pass — but I did move one verdict inside the tier's evidence base
(§U.008, §Boundary 5).

**Dataset:** The Founder's Playbook — forensic reconstruction of what each company in the frozen universe
(`00_universe/`) looked like **while its outcome was still unknown** (§1).
**Company (rank 45):** the modern registrant **JOHNSON & JOHNSON**, CIK 0000200406, ticker JNJ
(`sources/_index/_registrant_CIK0000200406.json`). **This volume does not write the registrant.** What it
writes is *the firm of Johnson & Johnson as named in print between 1886 and 1904*, because that is the
earliest subject any held document witnesses and no held instrument of origination connects it to the
present legal person. The §Boundary section argues this; it is the single most consequential choice here.

**Stage definition (§7):** origin → first real-world experiment → repeatable validation → scalable company
formation. Adapted for a **late-nineteenth-century pharmaceutical manufacturer** the four beats are:
*the product and its process, the factory and its imprint, the institutional adoption series, and the
corporate leg* — and all four are inside the proposed window. A section that does not fit the model is
answered with the adapted equivalent plus the reason (§7 adaptation rule); none was deleted.

**Hindsight firewall (§2).** Nothing here treats the later existence of Band-Aid (held bytes: **0 lines**),
Listerine as a J&J property (13 lines, **none** naming a proprietor), the 1951 Metrix surgical-suture
line, the Tylenol franchise, Janssen Pharmaceuticals, the 1944 New Brunswick stock exchange listing, or the
registrant's eventual position as the world's largest healthcare company as evidence that an 1886–1904
decision was rational, that the plaster trade was obviously ripe, or that asepsis was destined to win.
Every §Boundary and §R judgment is defensible from bytes dated inside the proposed window. The words
"visionary", "prescient" and "inevitable" do not occur in this volume outside a quotation mark in which
they belong to the 1897–1919 house print itself. Anti-hagiography test applied per §2 to every coda.
**Post-boundary material is tagged `(PB)` wherever used**, including all 26 SEC bodies on disk (earliest
accession 0000950110-94-000059) and the registrant's 1970 annual report layer.

**Record-selection null (§2, AUDIT 4 / RD-032).** Unrecoverable *because the survivor's archive is the one
that was kept*, and restated in §S: **no instrument of origination survives in this corpus** — no charter,
no partnership article, no stock list, no ledger, no payroll, no order book, no internal memo, no rejected
option, no dissent. What was kept is (i) the company's **own house print**, written to sell antiseptic
method to pharmacists, and (ii) **trade press** written to keep pharmacists informed of each other. No
held byte gives a revenue, a capital figure, a profit, a wage or a headcount number. No independent count
of any quantified claim exists behind a single company self-report in this window. And one class of
evidence is absent by construction rather than by accident: the **filing floor is 1994-03-10** and the
**registrant's own domains were first captured 1996-10-18**, so both digital families that settle every
post-1994 company here are unreachable at any depth for Stage 1 — the probe's §3(a)/(b) measurement holds,
and I re-measured the filing floor (0 rows with `filingDate` ≤ 1960-12-31 of 3,371; §T).

**Confidence (§3):** **High** = 2+ independent **origins** or a primary document for its own year.
**Medium** = one reliable source; a retrospective-only primary; **or any claim resting solely on a layer
fetched over UNVERIFIED TLS**. **Low** = conflicting, vague, or retrospective-only with no primary carrier.
**UNKNOWN** = a finding, never a gap to fill, and never a guess: each UNKNOWN names the route that could
settle it. **TRANSPORT CAP, applied mechanically:** every one of the 15 OCR layers carries
`"transport": "UNVERIFIED TLS -- re-check before citing at High confidence"` in its sidecar (fleet default
on a machine with a stale CA store). Therefore **no statement resting only on those layers is cited at
High in this volume**, including the founding-range sentence and the 1887 corporate leg. That is a property
of our transport, not of the record, and it is a `data_gaps` row with a script remedy, not a doubt about
the print.

**The single-lineage finding, stated once and enforced everywhere (§3 filing-lineage rule).** Two lineages
carry this window, and the difference between them is the whole evidentiary argument:
*L1 — company house print.* `redcrossnotes00johngoog` (masthead leg "1897-1898 and 1899-1900", L72),
`redcrossnotes01johngoog` (same series; in-bytes copyright legs **1914, 1915, 1919**),
`asepsissecunduma00john` (1897), `johnsonsfirstai00unkngoog` (copyright leg 1901; a "1903" line),
`modernmethodsofa00john` (own date UNCONFIRMED) and `belladonnaastud00incgoog` (contribution by the firm's
president, in a multi-author volume). These are **one publisher speaking about itself**, and the 1910-layer
says so out loud: *"In one of their publications Johnson & Johnson have reviewed some of the stages in
their history from which the following is abstracted"* (L5737-5740) — house print **quoting house print** is
one source, however many volumes repeat it.
*L2 — third-party trade press.* `americandruggis07` (Vol XXVIII, Jan–Jun **1896**), `americandruggis13`
(Vol XL, Jan–Jul **1902**), `americandruggis01` (Vol XLI, Jul–Dec **1902**), `americandruggis26`
(Vol XLIV, Jan–Jun **1904**), `americandruggis29` (Vol XLV, Jul–Dec **1904**), and `bub_gb_A9IAAAAAYAAJ`.
This is a genuinely different origin, and it is the only family that can corroborate L1. Where L2 confirms
L1 the confidence is stated as two lineages; where only L1 speaks, `independence_note` says
`one lineage (company house print); L2 silent`, and the row is capped.
**Consequence enforced mechanically:** no retrospective sentence in L1 carries a **FACT** about the event it
describes. Each such sentence is filed as **two** records — the *printing* (FACT, for its own year) and the
*event* (RETROSPECTIVE INTERPRETATION) — exactly as §Boundary 3 and §B.1 apply it.

**ID scheme (§13, read before citing).** `A01…U01` claim records and `P1Sxx / P1Qxx / P1Txx / P1Dxx /
P1Vxx / P1Fxx / P1Cxx / P1Gxx` register rows in this volume are **dossier-local**. Global `source_id` blocks
are minted **centrally at merge** via `tools/id_mint.py`; the register `source_id` column below is therefore
left provisional (`P1Sxx`) by design, not by omission. Conflict keys are `U.001…U.0nn` and every one has its
§U anchor written here, for the 1:1 parity the merge proves. **Probe-local ids (`§5.1`, `l.9283`, `N1`) are
re-derived from bytes in this volume and not inherited**: every line number cited below was re-read this pass
against the file on disk, because the probe's locators proved partly unreliable (§U.009, §U.010).

**Entity-naming discipline (the rule that shapes every line of this volume).** `jnj` and `Johnson` alone are
**severe** noise: `Johnson` is among the most common English surnames, `Johnson Building` is a street address,
`Johnson County` is a jurisdiction, and the period **1886–1904 contains a direct naming-collision competitor
whose own trade name ends in "& Johnson" — Seabury & Johnson of East Orange, N. J.** Every naming asserted
here is therefore a **full entity string** (`Johnson & Johnson` / `Johnson and Johnson`, case-insensitive,
regex `Johnson\s*&\s*Johnson|Johnson and Johnson`) read on the same line as, or within ±6 lines of, the fact
claimed, and the line is printed. Four measured traps, all run this pass:
* **`alphabetfirstth00goog` — 126 lines containing "New Brunswick", 0 lines naming the company.** A Canadian
  volume (Dominion of Canada statistics, L108 date leg "1897."). The probe's count holds; the place name is
  worthless without the entity string beside it.
* **`ErnestFairfield` — 1888, 0 namings.** Pulled by the same query as the company print.
* **`Seabury & Johnson` appears in naming-adjacent position in `americandruggis29` L4868, L26436, L33726-33727
  and `americandruggis01` L46097** — a competitor listed beside J&J, and in the L26436 case the two firms are
  parties to the *same* price agreement. Never collapse them; both are named in full in every row below.
* **`Robert Wood Johnson` in `americandruggis07` L45597 is not a Johnson & Johnson naming at all.** The line
  belongs to a paragraph announcing that "the New York Red Cross has been incorporated", of which he is listed
  as an **incorporator**; I verified that **no** entity naming occurs within ±25 lines of it. The probe filed
  this line under "held in-window naming lines", which is a misattribution (U.010), and the collision risk is
  live because the company's own house organ and cotton are branded *Red Cross*.
**Measured corpus state on this pass** (re-enumerated per §14 rule 11, because `sources/` grew after the
probe): **15 OCR layers / 23,308,643 B / 642 entity-naming lines**, plus 26 SEC bodies (4,671,102 B,
1994–1999, all `(PB)`), plus 7 `_index` artefacts. The probe measured 14 layers / 23,275,060 B / 619 lines.
**The delta is one late-arriving layer, `John0851_1970` (33,583 B, fetched 2026-10-06, 23 naming lines),**
and its arrival matters for a second reason: the harvest index (`research/A4_harvest_mine.md`) records that
same item as **NULL — 0 word hits, 0 entity hits**, while its bytes carry 23 namings. A label outranked by
the file it describes is RD-124 in live form; recorded at U.011 and in the defect list.

## Boundary

STATUS: WRITTEN 2026-10-07

**Geometry note.** This section enumerates candidate Stage-1 subjects and windows, names the **document**
behind each, and states why each rival **fails**. It does not assert a boundary and then defend it
rhetorically. The search bracket `1886-01-01 → 1960-12-31` printed at the head of
`research/A4_harvest_mine.md` is **a harvester's retrieval setting, not a history**: it was chosen wide
*because* the founding date was unestablished, so that the evidence which could establish it would not be
silently discarded. Nothing below adopts it as a stage window. Windows here are **proposed against
carriers** — each edge is a document that exists on disk, with its own printed date leg.

### 1. The origin finding, written as what it actually is

**The best held statement of this company's origin is a range inside a retrospective, not a year.**
Verbatim, from the company's own bound house print (`redcrossnotes00johngoog`, masthead leg "1897-1898 and
1899-1900"), under the printed heading `PIONEERS.`:

> *"In the years previous to 1886-\*87 (the / date of the formation of the firm of / Johnson & Johnson)
> antisepsis had made / but little progress."* — `redcrossnotes00johngoog` L9281–9286

**OCR fidelity, read before this line is quoted anywhere else.** The bytes print `1886-*87` with an
asterisk; the `*` stands where an apostrophe or dash was typeset. Writing `1886-'87` is **our reading of the
artefact, not the bytes**; the literal string `1886-'87` occurs **zero** times in held bytes (verified this
pass). Quote the asterisk form or mark the substitution. The same rule binds every quotation below — e.g.
the First Aid price prints as `sells for $6.0U` (L2405) and the copyright leg as
`OopyrlRht, 1901, by JohriHon k Johnson` (L158).

That sentence does four things at once, and each constrains a different section:
1. It gives the origin as a **two-year range**, "1886-\*87", written **11–14 years after** the event by the
   firm itself. Class: **RETROSPECTIVE INTERPRETATION**, Medium at best (retrospective + UNVERIFIED TLS).
2. It names the **act** as "formation of the **firm**" — a firm, not a corporation and not a product launch.
3. It is **anonymous as to persons**: no founder, no brother, no name appears inside the formation clause.
4. It is **not contradicted** by anything held — and that is not the same as being corroborated. It has **one
   lineage**.

**A second, better-dated leg was found on this pass, and the probe's "not found" verdict is superseded.**
The later volume of the same house print states the corporate formation the probe reported as absent:

> *"Johnson & Johnson began in business in 1886; in 1887 they became a corporation."* —
> `redcrossnotes01johngoog` L5717–5719

The probe tested `Johnson\s*&\s*Johnson[^.]{0,60}incorporat|incorporat[^.]{0,60}Johnson\s*&\s*Johnson` over
all layers and got **0 lines**; I reproduced that **0** exactly. The zero is an artefact of requiring the
name and the corporate word on the **same line** of a **two-column OCR** — the sentence here breaks
`in 1886; in 1887 they became a corpo-` across a line end. The finding is therefore **both**: the adjacency
regex returns zero, and the statement exists. Recorded as **U.002** and as a probe-verdict correction, not
as a quiet improvement.

**So the company's own retrospective yields three inconsistent precisions, all in one lineage:**
`"1886-*87 … formation of the firm"` (L1 vol 00) → `"began in business in 1886; in 1887 they became a
corporation"` (L1 vol 01) → `"They entered into business in 1886, just at the time when cotton was gaining
general notice by the surgeon"` (L1 vol 01, L4652-4653). **The single-year 1886 is the collapse of a range,
in the second telling, 27+ years after the event.** This dossier writes the range as the finding and treats
"1886" as a *company claim in a later form of its own self-narrative*, never as a verified date.
And the **earliest dated third-party placement of the firm in existence** is a 1904 obituary notice in the
trade press — *"In 1887 he engaged with Johnson & Johnson and remained in their service until his death"*
(`americandruggis29` L33894-33895, Vol XLV, Jul–Dec **1904**): L2, in-window, independent of L1, placing a
man in the firm's employment by 1887 — **which corroborates the later year of the range and does nothing for
the earlier one**.

### 2. Candidate subjects and windows, with the document behind each

| # | Candidate Stage-1 subject and window | Best held document for it | Verdict |
|---|---|---|---|
| 1 | **"The registrant Johnson & Johnson, founded 1886"** — the brief's premise | none | **REJECTED (loser 1).** No held instrument of origination of any kind exists (§Header record-selection null), the EDGAR index carries **0 of 3,371** rows at or before 1960-12-31 and **no** form beginning `S-1`, and **the string `1886` occurs 0 times in all 26 SEC bodies on disk** (4,671,102 B, 1994–1999, counted this pass). The registrant's own filings print **no founding year at all**. Writing the stage as the registrant's would import a legal identity backward across 108 years with no document. |
| 2 | **The 1887 New Jersey corporation** | `redcrossnotes01` L5718 (retrospective); `belladonnaastud00incgoog` L184-185 *"President Johnson & Johnson Corporation"*; `redcrossnotes00` L50003 *"which corporation petitions the court"* | **REJECTED as the subject; RETAINED as a leg of it.** The 1887 date rests on one retrospective sentence in one lineage, the New Jersey charter is **not held**, and the only 1890s namings give an entity *form* rather than an incorporation *record*. It is the **scalable-formation beat** of the stage (§R), not the stage's opening. |
| 3 | **The firm of Johnson & Johnson, 1886-\*87 → 1904-12-31, as named in print** | L1 founding-range passage + L2 dated carriers at 1896 / 1902 / 1904 | **ADOPTED.** Earliest subject any held document names, inside the decade its own acts are said to have occurred, and it is witnessed by a **second lineage** whose volume dates are printed on the title pages. All four §7 beats are documented inside it by carriers I re-read this pass. |
| 4 | **1886 → 1960** (the harvester's bracket) | n/a — a retrieval setting | **REJECTED and stated why.** Held bytes carry **no in-window document at all between 1905 and 1960** except `redcrossnotes01`'s own copyright legs (**1914 / 1915 / 1919**) and the 1904 Druggist volumes; the next company voice on disk is the **1970 annual report** (`John0851_1970`, `(PB)`). Extending the stage to 1960 would make the window an artefact of a search query while adding no carrier to settle anything — the §14-rule-6 mistake of reading a retrieval default as a period. |
| 5 | **1886 → 1919** (last in-bytes company copyright) | `redcrossnotes01` L27247/L29055 `COPYRIGHT, 1919, BY JOHNSON & JOHNSON` | **REJECTED as the close; ADOPTED as the Stage-1 → Stage-2 hand-off** (§6). 1914–1919 print is a *later telling of the origin* — the volume that carries the "began in 1886; became a corporation in 1887" sentence is itself of that period, i.e. **32–33 years** after the event rather than 11–14. Making the retrospective the stage would convert the archive's accident into the boundary. |
| 6 | **The antiseptic-dressing invention as the opening act, "1886"** | `redcrossnotes00` L40615-40628 *"the greatest improvement of all was in or about the year 1886. We invented a system of machinery…"* | **REJECTED as a dated act; ADOPTED as the first-experiment beat at an UNDATED process.** "in or about the year 1886" is the company hedging its own date, and the invention is described without a place, a first sale or a witness. §D keeps it as one company talking about its own past. |

### 3. The registrant is not the subject, and the imprint says so

`modernmethodsofa00john` — the earliest company-authored **naming with an address** anywhere in held bytes —
prints *"Published by JOHNSON & JOHNSON, New York."* (L96) and *"JOHNSON & JOHNSON, 25 Cedar Street, New
York."* (L1402), and its price-list heads read *"PRICE LIST— JOHNSON & JOHNSON— NEW YORK"* (L1459, L1616).
That layer contains **0 lines with "New Brunswick"**. The New Brunswick factory appears only in the later
house print (*"to visit our factory at New Brunswick"*, `redcrossnotes00` L6741, L6749; *"Messrs. Johnson
<& Johnson, New Brunswick, N. J."*, L12771) and in third-party print by **1896** (*"their factory at New
Brunswick, N. J."*, `americandruggis07` L14592-14595). So the sequence the bytes support is:
**a New York printing/publishing address → a New Brunswick, N.J. factory named by outsiders in 1896.**
Two complications are kept visible rather than smoothed: the same early layer also prints
*"JOHNSO]^ & JOHNSON, / 23 Cedar St., New York."* (L3226-3228, a Papoid advertisement, i.e. **23 and 25 Cedar
Street in one undated document**), and **the date of that layer is itself unconfirmed** — the catalogue
metadata says 1888, the library call number OCR prints `RD131 J63 / 1891` (L3403-3414), while the newest
work its own text cites is dated *"Feb., 1888"* (L2445). **The move from New York to New Brunswick is
UNKNOWN: no held document dates it** (§S gap; route named).

### 4. What this boundary proposes, in one table

| Leg | Proposed date | Carrier and printed date leg | Lineage | Class |
|---|---|---|---|---|
| Stage 1 opens | **1886\*–87**, month and day UNKNOWN | `redcrossnotes00` L9283-9285 (vol. masthead 1897–1900) | L1 | FACT about the 1897–1900 printing; **RETROSPECTIVE INTERPRETATION** about the act |
| Earliest independent placement of the firm in existence | **by 1887** | `americandruggis29` L33894 (Vol XLV, Jul–Dec 1904) | **L2** | CONTEMPORARY OBSERVATION *of the 1904 printing*; RETROSPECTIVE for 1887, but from a **different origin than L1** |
| First real experiment (process/product) | **1886 or 1887 as printed, 1888 at earliest verifiable** | `modernmethodsofa00john` (metadata 1888 / call number 1891 / cites Feb 1888) + `redcrossnotes00` L40619 | L1 | UNKNOWN date; FACT for the printing |
| Corporate leg | **1887 claimed; UNCHARTERED in evidence** | `redcrossnotes01` L5718 | L1, retrospective 27–33 yrs | RETROSPECTIVE INTERPRETATION, Medium-capped by TLS |
| First dated institutional demand | **1898 (the Cuban campaign)** | `johnsonsfirstai00unkngoog` L2464-2466 (copyright 1901) | L1 | FACT for the 1901 printing; the count itself is uncorroborated |
| First dated outsider witness of scale | **1896 (Jan–Jun)** | `americandruggis07` L94 + L14592-14600 | **L2** | CONTEMPORARY OBSERVATION, Medium (TLS) |
| Stage 1 closes | **1904-12-31** | last dated naming carrier held: `americandruggis29` Vol XLV Jul–Dec 1904 | **L2** | the boundary is the **carrier floor**, and is proposed not asserted (§6) |

### 5. Losers kept live

A boundary is only honest if what it throws away stays visible. Named, with the route that could reopen each:
- **U.001 — the origin as a range vs the origin as a year.** L1 says both, in different volumes, 11–14 and
  27–33 years after the event. Not resolved; the range is written as the finding.
- **U.002 — "the incorporation question stays OPEN, and no NJ charter is in the corpus"** (probe §5.1) versus
  the held sentence *"in 1887 they became a corporation"*. The probe's *charter* half is unaffected — **no New
  Jersey charter is held** — but its *not found* half is superseded. The merge must not carry "no
  incorporation statement exists" as a Stage-1 fact.
- **U.003 — the New York / New Brunswick imprint sequence**, including 23 vs 25 Cedar Street and the
  undated move.
- **U.004 — the date of `modernmethodsofa00john`** (1888 metadata vs "1891" call number vs its own citations
  to Feb 1888).
- **U.005 — "no document in the corpus calls anyone a founder"** (probe §5.2), which I re-measured two ways
  and which **holds** (§B.2), against the brief's three-brothers premise. The brothers' **roles** are held;
  their **foundership** is not, and no held line names three of them.
- **U.006 — the `1910` date stamped on `redcrossnotes01` by the probe**, which the layer's own copyright legs
  (1914, 1915, 1919) contradict. The layer's bound date is **UNCONFIRMED**, and because that layer carries
  both the 1887 corporate leg and the cotton-consumption figures, the *lag* on three load-bearing claims
  moves from 24 years to 33+.
- **U.007 — the 7,000 cabinets / 370,000 packets series**, company-counted with no independent denominator.
- **U.008 — the tier's own evidence base.** The probe issued T2 **provisional** because JNJ had *zero*
  metadata candidates and its two families rested on ad-hoc scripted probes. `sources/sec/` now holds
  **26 filing bodies** (arrived 2026-09-30, after the probe reported "SEC document bytes held: 0"). I
  record the change and **do not re-tier**: every one of those bodies is 1994+ and therefore `(PB)`; family
  (a) is still a documented in-window null, so the family count for Stage 1 is still **2**, and the tier
  stands. What changed is that the probe's §2 inventory is stale, which §T states.
- **U.009 / U.010 / U.011 — locator and label defects in inherited records** (probe line numbers that
  belong to a different layer than the one the probe named; the `americandruggis07` L45597 misattribution;
  the harvest index's `NULL` on `John0851_1970` against 23 namings in its bytes). Registered so the merge
  cannot rebuild them from the probe alone.
- **The erased loser class.** No revenue, capital, wage, headcount **number**, dividend or cost figure exists
  in held bytes; no first customer, no first hospital, no first order; no recall, seizure or condemnation of
  this firm's goods; no failure of the firm's own choosing recorded anywhere. Each is a finding about the
  record, logged in §S and the gaps register — **not** a claim that the underlying facts did not happen, and
  not a smooth-ascent narrative either (§2 hindsight firewall cuts both ways: §M and the `failures` register
  are answered with the absence named, not with silence).

### 6. Hand-offs, and what this boundary refuses to claim

| Hand-off | Claim | Status |
|---|---|---|
| Stage 1 → Stage 2 | opens with **1905** print or with the registrant's own paper trail, whichever a carrier supports | **PROPOSED, NOT SET.** Family (c) is 99% unopened (795 American Druggist items exist, 5 volumes are on disk) and the 44 *Pharmaceutical Era* items including **1887** have never been fetched; the 1914–1919 house-print legs are the nearest held carry-over. The probe declared Stage 2/3 windows **not settable** from held evidence (RD-112) and measurement supports that: I will not date a hand-off to a document I have not read. |
| Stage 2/3 territory (`(PB)`) | 1970 annual report layer; EDGAR floor 1994-03-10; first 10-K 1994-04-01; web floor 1996-10-18 | `(PB)`, cited only as the *absence* of early company accounting, never as evidence about 1886–1904 |

**What this boundary explicitly does not claim:** that Johnson & Johnson was founded in 1886 (the best held
statement is a range inside a retrospective, and the second-earliest is a *single year* produced by that
retrospective's own later telling); that any person founded it (§B.2 — **zero** held lines put a
founder-word beside a naming, measured two ways); that the three brothers named in the dispatch brief ever
appear in held bytes as a group (**0** lines contain "three brothers"; **0** lines contain a brother-word
within ±3 lines of a naming; **0** lines name `James Wood`; **0** name `Miles Stone`; **0** name `Fargher`);
that the 1887 corporation is the registrant (no charter, no lineage document held); that `Red Cross Notes`,
`Red Cross Cotton` and the *New York Red Cross* charity that incorporated with a Robert Wood Johnson on its
list are the same thing (they are not — U.010); or that any family's zero is a null except where the route
**answered** (§S, §H, and the five-family report).

## A

STATUS: WRITTEN 2026-10-07

### A.1 Executive state summary — the entity's condition at the proposed close, as the held print states it

At **1904-12-31** the subject of this volume was a plaster-and-antiseptic-dressing manufacturer named
**Johnson & Johnson** of **New Brunswick, N. J.**, described by outside trade print in the same year as
*"the manufacturing firm of Johnson & Johnson, New Brunswick, N. J."* (`americandruggis26` L61540, Vol XLIV,
Jan–Jun **1904**) and as *"manufacturers of medicines and surgical supplies, of New Brunswick"*
(`americandruggis13` L6219, Vol XL, Jan–Jul **1902**). Two facts about its condition are **witnessed by the
second lineage** and are therefore the strongest things in this dossier: it had **added a four-story building
to its New Brunswick factory** (reported Jan–Jun **1896**, `americandruggis07` L14592-14600), and it **stood
in a named relationship with three specific competitors** in a plaster price agreement made "some five or six
years ago" — i.e. c. 1898–99 — and in a **rate war** reported in August **1904** (`americandruggis29`
L26432-26450, L33715-33740).

Its own print at the same moment states scale **only in words**: employees *"numbering many hundreds"* and
direct customers *"numbering many thousands"* (`redcrossnotes00` L4103-4105); *"Upwards of seven thousand
Johnson's First Aid Cabinets are in use in manufacturing establishments"* and *"370,000 were supplied by
order of the United States Government to the Army and Navy"* in the Cuban campaign (`johnsonsfirstai00…`
L2397, L2464-2466, copyright 1901). **Every one of those figures is L1 — one company talking about itself —
and not one has an independent denominator anywhere in held bytes** (§L, U.007).

**What is not known about the firm at 1904, and matters:** its **capital**, its **sales**, its **profit**,
its **ownership**, its **legal form as a document**, the **date it moved** from the Cedar Street New York
imprint to New Brunswick, whether the 1887 "corporation" is the same person as the "firm" of 1886-\*87, the
name of anyone who founded it, its **first customer**, and whether anyone outside the firm ever counted its
goods. §K, §P and §S answer these at `UNKNOWN` with the route that could settle each.

**Is:** a reconstruction of what two lineages of print — the firm's own house organ and the druggists' trade
press — say about a New Jersey surgical-dressing manufacturer between its narrated start and 1904.
**Is not:** a history of a founding (no instrument of origination survives here); a founder's account (no
founder's words are held, and the closest thing to one is an **anonymous** first-person passage, §B.3); a
story about a future healthcare giant; or a document trail from 1886, because the earliest held naming of
the firm is **1896** at the latest-datable remove and the earliest held company print is itself written
**11–14 years after** the act it narrates.

### A.2 The state of the archive, since for this company it *is* part of the state

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Entity namings held | **642 lines across 15 OCR layers / 23,308,643 B** | regex sweep this pass; per-layer table §T | High (a count of bytes I read) |
| Where the namings live | **504 of 642 (78%) in the two house-print volumes**; 100 in five Druggist volumes; 23 in a 1970 annual report `(PB)`; 15 in the four earliest pamphlets/manuals | §T per-layer counts | High |
| Two layers returned by the query with **zero** namings | `alphabetfirstth00goog` (126 "New Brunswick", 0 namings) and `ErnestFairfield` (1888, 0 namings) | sweep this pass | High — RD-124 by measurement |
| SEC document bytes held | **4,671,102 B in 26 bodies, accessions 1994-03-10 → 1999**, plus `_UNANSWERED.csv` and `_SKIPPED.csv` | `sources/sec/_RUN.json` (window `1960-12-31..2006-12-31`, attempted 149, stored 26) | High; all `(PB)` |
| `1886` inside the registrant's own filings | **0 occurrences** in all 26 bodies | counted this pass | High — the modern registrant prints no founding year |
| Filing rows at or before 1960-12-31 | **0 of 3,371**; no form beginning `S-1`; earliest 1994-03-10 DEF 14A | `sources/_index/` (re-measured §T) | High (a documented null, route answered) |
| Web-archive floor for the registrant's own domains | **1996-10-18** (`www.jnj.com`), 1998-01-26 (`johnsonandjohnson.com`) | probe §3(b) CDX, answered with HTTP 200 | Medium — two URLs probed, not the archive |
| Trade press actually opened | **5 of 795** American Druggist items; **0 of 44** *Pharmaceutical Era* items incl. **1887** | probe §3(c) numFound (metadata-level) | High (a count of what is on this disk) |

### A.3 Load-bearing claim records for §A

```
A01 Claim: Outside, dated trade print names the firm as a New Brunswick manufacturing concern twice in 1902-1904 — Date: 1902 and 1904 — Source: American Druggist and Pharmaceutical Record, Vol XL (Jan-Jul 1902) and Vol XLIV (Jan-Jun 1904) — Source date: 1902; 1904 — Local bytes: sources/periodicals/americandruggis13unkngoog_djvu.txt L6215-6226 and americandruggis26unkngoog_djvu.txt L61540 (UNVERIFIED TLS) — Tier: 1 (trade) — Class: CONTEMPORARY OBSERVATION — Passage: "manufacturers of medicines and surgical supplies, of New Brunswick" — Conf: Medium — Corroboration: 1 independent lineage (L2, and L2 does not derive from L1) — Conflicts: None
```
```
A02 Claim: The firm's own print at the turn of the century states its scale only as uncounted words — Date: 1897-1900 — Source: Red Cross Notes (house print, masthead leg 1897-1898 and 1899-1900) — Source date: 1897-1900 — Local bytes: redcrossnotes00johngoog_djvu.txt L4103-4105 — Tier: 1 — Class: FACT about the printing; the headcount and customer counts are ESTIMATE-free words, no number is printed — Passage: "our employees, number-ing many hundreds; to our direct patrcms, numbering many thousands" — Conf: Medium (TLS cap) — Corroboration: 0 independent — Conflicts: None, but see U.007 for the one place a number is printed
```
```
A03 Claim: The registrant's own SEC filings print no founding year at all — Date: 1994-1999 (PB) — Source: 26 stored EDGAR bodies for CIK 0000200406 — Source date: retrieved 2026-09-30 — Local bytes: sources/sec/*.txt (4,671,102 B) — Tier: 1 — Class: FACT (a count of 0 occurrences of "1886") — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: n/a — Conflicts: U.008 (the probe's "SEC document bytes held: 0" is now stale; the tier is unchanged because the bodies are all post-window)
```
```
A04 Claim: For this company the archive state is itself a finding: 78% of all held namings are the company speaking about itself — Date: 1897-1919 — Source: per-layer naming counts taken this pass — Source date: 2026-10-07 (enumeration) — Tier: n/a — Class: INFERENCE from measured counts — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High (arithmetic on lines I read: 246+258 of 642) — Corroboration: n/a — Conflicts: None; it is the reason no §D/§E/§L claim in this volume may rest on L1 alone and carry High
```

## B

STATUS: WRITTEN 2026-10-07

### B.1 Founder / company state — what held print prints about persons

The dispatch's premise is **three brothers**. Held bytes do not contain it, and the distinction between a
**role printed in a document** and a **founder** is the discipline this section exists to enforce.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Persons named in the formation sentence | **none.** *"the date of the formation of the firm of Johnson & Johnson"* carries no actor | `redcrossnotes00` L9283-9285 | High (of the absence, over held bytes) |
| The firm printed as a **plural person** | *"Messrs. Johnson <& Johnson, New Brunswick, N. J."* (57 `Messrs. Johnson` lines in this layer); *"The Johnsons had done pioneer work in the manufacture of pharmaceutical plasters with an India rubber base"* | `redcrossnotes00` L12771; `redcrossnotes01` L5748 | Medium (TLS cap; **High** that neither names an individual) |
| Robert Wood Johnson — office against the company | *"Making Belladonna Plasters," ROBERT WOOD JOHNSON, Manufacturing Chemist, President Johnson & Johnson Corporation."* — a **contributor list line**, in a multi-author volume | `belladonnaastud00incgoog` L184-185 | Medium (TLS + the volume's own date is only bounded ≥1893 by its citation of the 1893 Pharmacopoeia; sidecar carries no year) |
| Robert Wood Johnson — second, differently typeset | a two-column advertisement reading `: Robert Wood Johnson,` `: CHEMIST,` `: President Johnson & Johnson:` | `belladonnaastud00incgoog` L2246 ff. | Medium — the column interleaving is why this must be read as *one* man's title, twice printed in one volume |
| Robert Wood Johnson — outside the company record | listed as an **incorporator of the New York Red Cross**, a charity corps, in the same trade paper | `americandruggis07` L45590-45597 (Vol XXVIII, Jan–Jun 1896) | **High that the line is not a J&J naming** — 0 entity namings within ±25 lines (U.010) |
| A later "Robert W. Johnson (Johnson & Johnson)" | a marriage paragraph: *"Roberta Wood Johnson, daughter of Robert W. Johnson (Johnson & Johnson), was married to Robert Carter Nicholas, of New Brunswick, N. J., at Christ Church, New Brunswick, on Wednesday evening, November 9. Mr. Johnson's present to the bride was $100,000 in securities."* | `americandruggis29` L69115-69119 (Vol XLV, Jul–Dec 1904; the dateline puts it in the November 1904 issue) | Medium; **identity with the 1894 "Robert Wood Johnson" is an INFERENCE** (naming variant + shared New Brunswick), not a held equation |
| James Wood Johnson | **0 lines** (`James\s+Wood`, 15 layers, 23,308,643 B) | sweep this pass | High (of the absence over held bytes); **not** a finding about the record |
| Edward Ford Johnson | **0 lines** under `Edward Johnson` / `Ford Johnson` as a person of this firm; 11 hits on the loose pattern are unrelated (a place, a title, a different surname run) | sweep this pass | High (absence); Low (what the 11 hits are) |
| Miles Stone / Earle Dickson / Fargher | **0 / 0 / 0 lines** | sweeps this pass | High (absence over held bytes only — 5 of 795 Druggist items are on disk) |
| "Three brothers" | **0 lines** in the whole corpus, naming-adjacent or not | sweep `Three\s+Brothers\|three brothers` | **High** — the three-brothers story has **no in-window carrier here** |
| Brother-word beside a naming | **0 lines** with `brother` on the naming line; **0 lines** with `brothers` within ±3 lines of a naming (160 corpus-wide `brothers` lines are all unrelated firms: "Lea Brothers", "Walter Boake & Brothers" etc.) | sweeps this pass | High — and it is why §B.2's verdict is not a quote-absence but a measured one |
| Company state: legal form as *printed* | "firm" (1897–1900 print) → "Corporation" (1893+ print) → "which corporation petitions the court" (1897–1900 print) → "manufacturing firm" (1904, outsider print) | `redcrossnotes00` L9284, L50003; `belladonnaastud00…` L185; `americandruggis26` L61540 | High (that the print varies); **UNKNOWN** (which person is which) |
| Company state: who is speaking | the press is the firm's own: *"Red Cross Notes is the title of a periodical issued by Johnson & Johnson, of New Bruns\*wick, N. J."* and *"issued … from the laboratories of Johnson & Johnson"* | `redcrossnotes00` L42165, L40401 | Medium |

### B.2 The founder question, measured rather than quoted

**No held document calls anyone a founder, and I re-measured that two ways before writing it.** An exact-line
test — a line containing both an entity naming and `founder|founding|founded` — returns **0 lines** over all
15 layers. A widened test — the same words within ±2 lines of a naming — returns **1 line**, and it is not
about the firm: *"Plasters U. S. P. was established by the work of Messrs. Reynolds and Caspari at the
solicitation of Johnson & Johnson"* (`redcrossnotes00` L27083), a **committee** sentence. A third test
(`three brothers`, `brother(s)` beside a naming) returns **0**. Therefore:

* The company's print attributes the origin **to the firm and to a family plurality** ("the firm of Johnson &
  Johnson"; "The Johnsons"; "Messrs. Johnson & Johnson") and to **an office** (President, Manufacturing
  Chemist), never to a founder.
* The brief's three brothers are therefore **not written as founders here**, and — because no held line names
  them as a set — **not written as three at all**. The single held personal fact is a **role**: Robert Wood
  Johnson printed as *Manufacturing Chemist, President* against *Johnson & Johnson Corporation* in a
  1893-or-later multi-author volume, corroborated in a **different** lineage only in 1904 by a society
  paragraph that calls him "(Johnson & Johnson)" and puts him in **New Brunswick**.
* **A role in a document is not a founding claim** (§ rule 4). This is not a quibble: the project has already
  caught twelve companies having their predecessor's date imported into a registrant's origin. Here the same
  discipline applies to *persons*.
* **What would settle it, named as a route:** a New Jersey charter or partnership record (no tool reaches it,
  §S); the *Pharmaceutical Era* 1886–1895 volumes (44 items, 0 fetched); the remaining 790 American Druggist
  items (a New Brunswick or Philadelphia correspondence column naming the principals is exactly the kind of
  text those volumes carry). Until one exists, §B's answer is *"the firm, the family plurality, and one
  printed office-holder"* and the class is **FACT about the printings / UNKNOWN about the persons**.

### B.3 The nearest thing to a founder's own voice is anonymous

The house print contains a first-person **singular** account of the firm's start, and it is unattributed:

> *"When I started Johnson & Johnson in the making of this article the cotton then in use was yellow and
> dirty … the greatest improvement of all was in or about the year 1886. We invented a system of machinery by
> which cotton could be carded and rolled automatically with a layer of tissue paper between each layer of
> cotton … cotton had never been prepared in this way before, and it opened the new era."*
> — `redcrossnotes00johngoog` L40603-40628

Three narrow observations, all needed before anyone quotes this as a founder memoir. (i) The "I" is
**never named** in the passage: it sits inside a signed-or-not article under the headings
`COMMERCIAL ABSORBENT COTTON.` / `COTTON USED IN SURGERY IN THE UNITED STATES` (L40528-40562), between a
consumption table and a trade commentary; the **switch from "I" (L40603) to "We" (L40615, L40619, L40630)**
within nine lines means the pronoun is unstable even as a voice. (ii) The date it attaches to the invention
is hedged by the speaker — *"in or about the year 1886"* — which is the company's own uncertainty about its
own origin story. (iii) Being in the firm's own periodical makes it **L1**, i.e. it is the **same lineage**
as the "PIONEERS" passage and cannot corroborate it. Class: **RETROSPECTIVE INTERPRETATION**, with the
speaker **UNKNOWN**; the *printing* is FACT for 1897–1900.

### B.4 The firm's own account of its strategy at entry, which is the best "founder state" held

> *"They concluded when they entered the field that rather than contest for the trade of others already
> established they would create a place for themselves and then attempt to fill it; they would strive to
> supply commodities new in use and purpose, or which …"* — `redcrossnotes01` L5751-5760, under the printed
> heading `IN THE BEGINNING`, itself introduced as an abstraction from *"one of their publications"* (L5737).

This is a **decision statement with an institutional subject and no person** — the house print explaining
why the firm did not enter the established plaster trade head-on. §N uses it as the one rationale in the
corpus that is the company's own; §O uses it as the counterfactual it explicitly rejected. It is
**RETROSPECTIVE**, in a layer whose own date is unconfirmed (U.006), and it is **self-narrative in its second
hand** — one volume abstracting another. Confidence: Medium, single lineage.

### B.5 Load-bearing claim records for §B

```
B01 Claim: No held line in any lineage calls any person a founder of Johnson & Johnson — Date: 1886-1904 — Source: 15 OCR layers, 23,308,643 B — Source date: swept 2026-10-07 — Tier: 1 for the bytes; the silence is not evidence — Class: FACT (of the measured absence) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High (three separate tests: same-line 0, +-2-line 1 non-company hit, brother-tests 0) — Corroboration: n/a — Conflicts: U.005
```
```
B02 Claim: The one office printed against the company's name is Robert Wood Johnson, Manufacturing Chemist and President, and it is printed in a contributor list, not a history — Date: 1893 or later (bounded by the volume's own citation of the 1893 Pharmacopoeia) — Source: belladonnaastud00incgoog (multi-author volume; sidecar carries no year; probe asserted 1894) — Source date: UNKNOWN(year)-bounded — Local bytes: L184-185, L2246 ff. — Tier: 1 — Class: FACT about the printing; the office-holding is CONTEMPORARY OBSERVATION if the volume is of the decade — Passage: "ROBERT WOOD JOHNSON, Manufacturing Chemist, President Johnson & Johnson Corporation." — Conf: Medium (TLS cap + unconfirmed volume date) — Corroboration: 0 for the office; 1 separate lineage (americandruggis29 L69115, 1904) only for a man of a variant name in the firm's trade — Conflicts: U.005, and the volume-date leg of U.004's class
```
```
B03 Claim: The house print's first-person account of starting the firm is anonymous, internally unstable between "I" and "We", and hedges its own date — Date: 1897-1900 printing of an event "in or about the year 1886" — Source: redcrossnotes00johngoog L40603-40628 — Source date: 1897-1900 — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION; speaker UNKNOWN — Passage: "When I started Johnson & Johnson in the making of this article the cotton then in use was yellow and dirty" — Conf: Low (retrospective, single lineage, unstable speaker, TLS) — Corroboration: 0 — Conflicts: U.001 (it hedges the range it is being used to date)
```
```
B04 Claim: "The Johnsons" and "Messrs. Johnson & Johnson" are the only plural-person forms the company ever uses of its own origin, and they name no individuals — Date: 1897-1919 — Source: redcrossnotes00 L12771 and 56 further Messrs. Johnson lines; redcrossnotes01 L5748 — Source date: 1897-1900; UNCONFIRMED volume date leg (U.006) — Tier: 1 — Class: FACT about the printings; RETROSPECTIVE INTERPRETATION about who they were — Passage: "The Johnsons had done pioneer work in the manufacture of pharmaceutical plasters with an India rubber base." — Conf: Medium — Corroboration: 1 lineage only — Conflicts: U.005 (the dispatch's three named brothers have no held carrier)
```

<!-- NEXT: C, D, E -->

## C

STATUS: WRITTEN 2026-10-07

### C.1 The original problem, stated by the only two lineages that state it

| Variable | Value | Source | Confidence |
|---|---|---|---|
| The problem as the firm itself framed it | the **supply** of antisepsis, not the idea of it: hospital dressings worked; outside them the market's goods did not. *"While the dressings prepared by a few leading hospitals and immediately used gave good results, dressings obtainable by the great bulk of practitioners who were forced to rely upon the manufacturers were for the most part wholly unreliable, and in consequence the truth of Listerism was hampered for the lack of…"* | `redcrossnotes00` L9288-9295 | Medium (TLS; retrospective 1897–1900 for a state of things it describes as pre-1886) |
| The response claimed | *"To meet this want Johnson & Johnson devised a system of dressings made to fill the demand of the best surgical practice."* | `redcrossnotes00` L9300-9302 | Medium; **L1 only** |
| Mechanism named in the same print | a **process** invention in packaging, not in chemistry: machinery that carded and rolled cotton with a tissue-paper layer between each layer, so the surgeon could take what he needed from a roll instead of a wad | `redcrossnotes00` L40619-40625; restated in `redcrossnotes01` L4658-4663 | Medium; single lineage, restated |
| Why that mechanism was worth anything | the firm quantifies the market it entered: absorbent cotton used in surgery was *"possibly a little over two hundred pounds"* in 1886, *"in 1898 … estimated at three million pounds"*, and *"somewhere from six to ten million"* "at the present time" | `redcrossnotes01` L4666-4676 | Low (unattributed estimates, L1, retrospective, TLS) — **ESTIMATE class, arithmetic not shown because none is** |
| Facts knowable in-period by an outsider | the plaster trade was crowded and secretive: *"In 1886 there were quite as many plaster makers as there are today. Plasters of the diachylon and pitch type were in use."* | `redcrossnotes01` L5744-5747 | Medium (L1, retrospective) |
| What the problem was **not**, in held print | not a retail-format problem, not a distribution problem, not a financing problem, not a consumer-awareness problem. No held line frames it as any of those. The framing is **manufacture and trust in a sterile article of commerce** | silence across 642 naming lines | High (that no held line so frames it) |

### C.2 What is unrecoverable about the problem, and why that is a finding

No **contemporaneous** (1886–1890) statement of the problem exists in this corpus at all: the earliest
company-authored naming is a layer whose own date is contested (1888 / 1891 / "cites Feb 1888"), and the
earliest *dated* statement of "the years previous to 1886-\*87" is 1897–1900 print looking back 11+ years.
Every account of the problem is therefore **an argument the firm was making in the 1890s about the 1880s**,
in a periodical whose stated purpose was to inform employees and customers about *"our new products, new
methods, new issues of pamphlets"* (`redcrossnotes00` L4106-4108). The record-selection null applies with
full force: the trade press of 1886–1890 — *Pharmaceutical Era* (44 items, incl. 1887 volumes, **0 fetched**)
and the other 790 American Druggist items — is where an independent statement of the same problem would
live, and none has been opened. **UNKNOWN, route named** (§S gap G-1, §Untried U1–U2).

### C.3 Knowability, for this stage (§7 format)

* **KNOWABLE in-period:** that absorbent cotton and antiseptic dressings were becoming a trade article; that
  plaster making was crowded; that a manufacturer could advertise process superiority to pharmacists; that a
  government contract existed during the 1898 campaign (only as the firm's own sentence).
* **NOT KNOWABLE in-period:** whether the "wholly unreliable" characterisation of competitors' dressings was
  tested by anyone but the firm; whether any hospital bought from it before 1898; what the firm's capacity or
  capital was.
* **UNKNOWN now, from this corpus:** everything in §K's money rows, the 1887 charter, the move date, the
  first customer, the first failure.

## D

STATUS: WRITTEN 2026-10-07

### D.1 The first real experiment, as an undated process inside dated print

The held record supports **a sequence of acts**, not a dated experiment, and the acts are:

| # | Act, as the print states it | Carrier and its date | Lineage | Class |
|---|---|---|---|---|
| 1 | Entering a crowded trade by **not** contesting established plasters: *"rather than contest for the trade of others already established they would create a place for themselves and then attempt to fill it"* | `redcrossnotes01` L5752-5755 (vol. date UNCONFIRMED, 1914+ copyrights) | L1 | RETROSPECTIVE INTERPRETATION |
| 2 | Inventing **machinery** to card and roll cotton with alternate tissue-paper wrappings, *"in or about the year 1886"* | `redcrossnotes00` L40615-40628 (1897–1900 print) | L1 | RETROSPECTIVE INTERPRETATION; the hedged date is the company's own |
| 3 | Publishing a **price list** of antiseptic surgical supplies under a New York imprint — including silk and catgut sutures *"which we furnish"*, an instrument/needle/suture outfit, and *"PRICE LIST— JOHNSON & JOHNSON— NEW YORK"* | `modernmethodsofa00john` L534-546, L1390-1391, L1402, L1459 | L1 | FACT for the printing; date of the printing UNCONFIRMED (U.004) |
| 4 | Printing, for surgeons, **how to keep a wound clean** — *"the practical application of the art of asepsis to the preparation of surgical dressings"*, with a priced kit: *"ASEPTIC ARMAMENTARIUM.— Price $5.00."* | `asepsissecunduma00john` L119-135, L1366 — **1897**, printed on its own title page | L1 | FACT (1897); first-person plural *"our laboratories"* |
| 5 | A **capacity** act witnessed by outsiders: *"Johnson & Johnson have been compelled to add a four-story building, hitherto unoccupied, to their factory at New Brunswick, N. J."* | `americandruggis07` L14592-14595 (Vol XXVIII, **Jan–Jun 1896**) | **L2** | CONTEMPORARY OBSERVATION, Medium (TLS) |

**What the sequence does not do:** date the first experiment. The only act with a printed year on the page
that records it is **#5, 1896**, and it is an expansion, not an origin. The two acts that *describe* the
first experiment (#2, #3) sit in layers whose own dates are 1897–1900 and contested-1888/1891. **The first
real experiment's date, place and first customer are UNKNOWN** (probe §5.3 holds under my re-measurement).

**The premise the dispatch supplied is not satisfied either.** If the expected "first experiment" is a
**plaster bandage or a suture product**, held bytes support the **dressing/cotton process** and a suture
**line listed in a price list**, and nothing else: no held line names a first hospital, a first surgeon, or
a first institutional purchase (the earliest institutional claim is the 1901-published Army and Navy sentence,
§L). `suture` appears in 12 layers; in the earliest company print it is a **catalogue item the firm furnishes**
(L536), not an invention event.

### D.2 Assessment, with mechanism named

The experiment, as held print describes it, was a **manufacturing-and-trust experiment rather than a product
experiment**: the claimed novelty is in *how the article is put up* (a roll with separable layers) and *how
it is kept sterile* (the firm's "laboratories", its aseptic method, its printed instructions), and the
commercial vehicle is the **price list sold through druggists**. The mechanism that would make it work is
legible in the same print: a pharmacist-facing periodical that explains asepsis and then prices the kit
(`redcrossnotes00` L40401, L4106-4108; `asepsissecunduma00john` L1366). **Alternative explanation, required
by §16:** the same outcome — a leading share in surgical dressings — is explicable without the cotton-roll
invention, by the 1896 factory expansion, by advertising (the outsider in 1896 attributes a *"boom"* to
*"generous, and, at the same time, judicious and novel advertising methods"*, `americandruggis07`
L14596-14599), or simply by being early into a category whose whole demand curve was shifting (200 lb → 3M
lb). **The corpus cannot separate these**, because it holds no sales figure at any date. Confidence in the
causal claim *"the process invention created the position"*: **Low**, and it is the firm's own claim in all
five of its printings.

### D.3 Load-bearing claim records for §D

```
D01 Claim: The earliest dated third-party witness of the firm's physical plant is an 1896 trade-press report that it added a four-story building to its New Brunswick factory — Date: Jan-Jun 1896 — Source: American Druggist, Vol XXVIII — Source date: 1896 — Local bytes: americandruggis07unkngoog_djvu.txt L94 (volume leg), L14592-14600 — Tier: 1 (trade) — Class: CONTEMPORARY OBSERVATION — Passage: "Johnson & Johnson have been compelled to add a four-story building, hitherto unoccupied, to their factory at New Brunswick, N. J." — Conf: Medium (TLS cap; otherwise High: independent lineage, dated title page) — Corroboration: 1 independent lineage (L2 vs L1) — Conflicts: None
```
```
D02 Claim: The firm's own account puts the decisive improvement in packaging machinery "in or about the year 1886", i.e. hedges the date it is being used to establish — Date: event 1886-ish; printing 1897-1900 — Source: Red Cross Notes — Source date: 1897-1900 — Local bytes: redcrossnotes00johngoog_djvu.txt L40615-40628 — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION — Passage: "the greatest improvement of all was in or about the year 1886. We invented a system of machinery by which cotton could be carded and rolled automatically with a layer of tissue paper between each layer of cotton" — Conf: Low (retrospective, hedged by its own author, single lineage, TLS) — Corroboration: 0 independent — Conflicts: U.001
```
```
D03 Claim: The first experiment is documented as a process plus a priced kit, never as a first sale, first customer or first institution — Date: 1886-1897 — Source: modernmethodsofa00john; asepsissecunduma00john — Source date: UNCONFIRMED (1888 metadata / 1891 call number); 1897 — Local bytes: modernmethods… L534-546, L1390-1391, L1459; asepsis… L119-135, L1366 — Tier: 1 — Class: FACT for the printings; UNKNOWN for the event chronology — Passage: "ASEPTIC ARMAMENTARIUM.— Price $5.00." — Conf: Medium (the 1897 layer carries its own printed year) — Corroboration: 0 — Conflicts: U.004
```

<!-- NEXT: E, F, G -->

## E

STATUS: WRITTEN 2026-10-07

### E.1 Product reconstruction, from print that describes it while it was current

The reconstruction is unusually good for an 1880s company — because the company printed **catalogues** — but
the printed year that anchors it is **1897**, not 1886.

| Item as the print names it | What the bytes add | Carrier (lineage, date) | Confidence |
|---|---|---|---|
| **Absorbent cotton, rolled with alternate tissue-paper wrappings** — the claimed origin article | the mechanism: *"carded and rolled automatically with a layer of tissue paper between each layer of cotton, the object being to keep the several layers separate and apart for convenience in handling and use"* | `redcrossnotes00` L40619-40625 (L1, 1897–1900) | Medium; retrospective |
| **"Red Cross" cotton**, in characteristic **blue cartons** with a red cross device | the *litigated* description of the packaging, from the firm's own bill of complaint: *"put up in blue cartons of characteristic appearance"*, imitated *"in the month of -July, 1899"* | `redcrossnotes00` L49983-49997 (L1, 1897–1900 print of an 1899 filing) | Medium — and the **only** held description of a package as a trade dress asset |
| **Antiseptic dressings, ligatures and sutures** — silk ("Chinese twist" and braided), catgut, silkworm gut, silver; *"chromicized catgut sutures (after Macewen's formula), 10 feet"* | a **price list** with the imprint: *"PRICE LIST— JOHNSON & JOHNSON— NEW YORK"*; first-person supply: *"which we furnish for silk sutures"* | `modernmethodsofa00john` L534-546, L1390-1391, L1459 (L1, date UNCONFIRMED) | Medium for the printing; the item list is the strongest product evidence in the corpus, and its date is the weakest |
| **The Aseptic Armamentarium** — a surgeon's kit | *"ASEPTIC ARMAMENTARIUM.— Price $5.00."* on a 1897 title page reading `JOHNSON & JOHNSON / ASEPTIC LABORATORIES / NEW BRUNSWICK, NEW JERSEY / 1897 / COPYRIGHT, 1897.` | `asepsissecunduma00john` L119-135, L1366 (L1, **1897**) | Medium-High for 1897 (own printed year; TLS caps it) |
| **Johnson's First Aid Cabinet** and **Johnson's Accident Case** (its predecessor) | *"sells for $6.0U"* [bytes: **$6.00**], *"the original Johnson's Accident Case"* → Cabinet lineage; contents listed item by item | `johnsonsfirstai00unkngoog` L2405, L2409-2411, L2438-2458 (L1, copyright **1901**) | Medium |
| **Digestive tablets / Papoid preparations** — non-surgical line | *"The Prices of Papoid Preparations Have Been Reduc?d… Johnson's Digestive Tablets, former price, $1.25 for 100; now SW per dozen bottles"* (the new price is **OCR-corrupt**) | `redcrossnotes00` L13340-13344 (L1, 1897–1900) | Medium (the fact of a cut); **UNKNOWN** (the new price) |
| **Vino-Kola-fra and other proprietary preparations** | an outsider's account of a *"boom"* driving factory expansion | `americandruggis07` L14596-14599 (L2, 1896) | Medium |
| **Disinfecting fluids, fumigators** | retail *"fifty cents"*, *"ten cents a bottle"*, *"ten cents a box"* | `johnsonsfirstai00unkngoog` L4147-4152, L5257 (L1, 1901) | Medium |

### E.2 The denominator that must travel with every product figure

Every price above is a **catalogue retail price to the druggist or consumer**, not revenue, not margin, not a
quantity sold. `derived_arithmetic` is therefore `not_derived` on all of them, and no price may be multiplied
by any adoption count in §L to produce a sales figure: **the 7,000 cabinets and the $6.00 price are the same
company's same sentence-family, and the 370,000 packets have no price attached in any held line** (an
arithmetic trap the merge must not fall into — recorded so a later pass does not "estimate revenue" from it).

### E.3 What cannot be reconstructed

The **first** product is not separable from the **first advertised** product; no held line dates a first sale
of anything; no formula, yield, output or defect rate is printed; the *composition* of the cotton improvement
is described mechanically but never dated precisely; and the suture line cannot be dated to the decade at
all, because the only layer that lists it (U.004) has three candidate years. **UNKNOWN**, route: the
*Pharmaceutical Era* 1886–1895 fetch and a re-OCR of `modernmethodsofa00john`'s cover (U.004's remedy).

## F

STATUS: WRITTEN 2026-10-07

### F.1 The customer, as far as two lineages will let it be known

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Who is addressed | the **pharmacist**, twice over: the house organ is a druggist-facing periodical (*"Red Cross Notes is the title of a periodical issued by Johnson & Johnson, of New Bruns\*wick, N. J."*), and the firm's stated intent is to inform *"our employees … to our direct patrons"* | `redcrossnotes00` L42165, L4100-4105 | Medium |
| Who buys the method | *"thousands of railroad, mining and factory surgeons, as well as those connected with fire, police and municipal departments"* | `johnsonsfirstai00unkngoog` L2385-2387 (1901) | Medium; **L1 self-report, no count** |
| Institutions named as users | *"several of our chief Railroad Systems as a shop first aid equipment"*; *"Boards of Education in many cities have placed this cabinet in the public schools and adopted Johnson's First Aid Manual as a text book"* | `johnsonsfirstai00unkngoog` L2398-2400 (OCR-mangled at the verbs) | Medium; L1; **no system or city is named** |
| Government as customer | *"(In the Cuban campaign 370,000 w^ere supplied by order of the United States Government to the Army and Navy)"*; and *"similar to those supplied by Johnson & Johnson to the U. S. Government for the use of the Army and Navy"* | `johnsonsfirstai00unkngoog` L2464-2466, L2369-2371 | Medium for the printing; **0 independent** for the count (U.007) |
| Named individual customers | **none held.** Not one named surgeon, hospital or firm is recorded as a purchaser in any held line | sweep | High (of the absence over held bytes) |
| The channel to the end user | the **druggist**: *"if not obtainable through druggistSj interested parties are invited to communicate direct with the makerB"* | `johnsonsfirstai00unkngoog` L2405-2406 | Medium |

### F.2 The independence problem, stated once for §F

Every customer-side sentence in the corpus is the company describing its own customers, **except** the 1896
outsider report (§D.1 #5) and the 1902–1904 trade-press items, which describe the firm's **salesmen and
litigation**, not its buyers. No held third-party line names a J&J customer. So §F is **one-sided by
construction**, and the honest statement is: *the customer base of this company before 1905 is documented
only by the company's own claims about it.*

### F.3 Claim records for §F

```
F01 Claim: The only institutional-purchase claim held for the window is a company-published figure of 370,000 first-aid packets supplied by U.S. Government order during the Cuban campaign (1898) — Date: 1898 event; 1901 printing — Source: Johnson's First Aid Manual — Source date: copyright 1901 (bytes: "OopyrlRht, 1901, by JohriHon k Johnson"), a "1903" line at L89 — Local bytes: johnsonsfirstai00unkngoog_djvu.txt L2464-2466 — Tier: 1 — Class: FACT for the 1901 printing; RETROSPECTIVE INTERPRETATION for 1898 — Passage: "In the Cuban campaign 370,000 w^ere supplied by order of the United States Government to the Army and Navy" — Conf: Medium (TLS cap) — Corroboration: 0 independent; the route to one is an ordnance/Quartermaster record, untried and unreached by any tool here — Conflicts: U.007
```
```
F02 Claim: No held line, in either lineage, names a first customer, first hospital or first purchaser — Date: 1886-1904 — Source: 15 layers / 642 naming lines — Source date: swept 2026-10-07 — Tier: n/a — Class: FACT (of the measured absence) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: n/a — Conflicts: None; it triggers §10's "first customer is unknown" research-debt and is logged as gap G-4
```

## G

STATUS: WRITTEN 2026-10-07

### G.1 Supply / host side — for a manufacturer of this era the host is the factory and the freight

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Factory of record | **New Brunswick, N. J.** — *"to visit our factory at New Brunswick"*; 99 lines contain the place name in this one layer, **64 of them with "N. J." beside it** | `redcrossnotes00` L6741, L6749; counts this pass | Medium |
| First dated outsider confirmation of the factory | **1896**: *"their factory at New Brunswick, N. J."*, with a four-story addition *"hitherto unoccupied"* | `americandruggis07` L14592-14595 | Medium (**L2**) |
| Publishing/printing capacity in-house | *"Red Cross Notes is issued somewbat regularly from the laboratories of Johnson & Johnson"*; a leaflet series issued *"from the press of Johnson & Johnson"*, *"probably once a month"* | `redcrossnotes00` L40401, L4097-4100 | Medium — the firm owns its own media channel |
| Labour | *"our employees, number-ing many hundreds"* — **a phrase, not a number**; no payroll, wage or shift line exists | `redcrossnotes00` L4103 | Medium (of the printing); **UNKNOWN** (of the count) |
| Distribution arm | a **city-salesman network** witnessed by the trade press in 1896–1904: named representatives in New York, Philadelphia, Cincinnati, Detroit, Chicago; *"whose city salesmen report every day at noon and compare notes"* | `americandruggis01` L67215, L6972, L61049-61050, L14890; `americandruggis13` L8044, L8078, L8086, L37227; `americandruggis26` L61540 | Medium (**L2**, several dated volumes) |
| Branch premises | Philadelphia: *"Johnson & Johnson, of New Brunswick, have taken the building recently vacated by Geo. D. Feidt & Co. at 54 Arch street"* → then *"On the 16th inst. Johnson & Johnson formally opened their new office at 514 Arch street"* (Vol XLI, Jul–Dec **1902**), still trading from the *"Johnson Building, 514 Arch street"* in Vol XLV (**1904**) | `americandruggis01` L14890, L61049; `americandruggis29` L13001 | Medium; **the day-month of the opening is "the 16th inst." with the month unresolved in OCR → UNKNOWN** |
| Imprint before New Brunswick | New York, 25 (and 23) Cedar Street, on the firm's own price lists | `modernmethodsofa00john` L1402, L3226-3228 | Medium; date contested (U.004) |
| Raw material dependency | cotton — the firm's own table makes the category's consumption the thing to watch (1878 / 1888 / 1898 columns: *"Absorbent cotton, lbs. 5,000 250,000 3,000,000"*, with the first row OCR-mangled) | `redcrossnotes00` L40564-40576 | Low (OCR-corrupt table; L1; unattributed) |
| Host of the standard | the **U.S. Dispensatory** and the **Pharmacopoeial** revision cycle, into which the firm claims its plaster method was taken (§L) | `belladonnaastud00incgoog` L2431-2433 | Medium (author's own footnote = L1-adjacent claim inside a multi-author volume) |

### G.2 What §G cannot answer

No supplier is named for cotton, silk or glass; no freight, warehousing or terms-of-trade line exists; no
capacity figure (spindles, tons, square feet of the J&J factory) is printed anywhere; and the **relationship
between the New York publishing house and the New Brunswick works** — one firm, two places, which leg carried
which function — is **UNKNOWN** (U.003). The route that would name them: the 1886–1895 *Pharmaceutical Era*
volumes, and New Jersey incorporation/assessment records (no tool reaches these; §Untried).

### G.3 Claim record for §G

```
G01 Claim: By 1902 the firm had taken and formally opened a Philadelphia city office, and the trade press had named its city salesmen in five markets by 1904 — Date: 1902 (office); 1896-1904 (salesmen) — Source: American Druggist Vol XLI and Vol XL, Vol XLIV, Vol XLV — Source date: 1902; 1902; 1904 — Local bytes: americandruggis01 L14890, L61049-61050; americandruggis13 L8044-8086; americandruggis26 L61540; americandruggis29 L13001 — Tier: 1 (trade) — Class: CONTEMPORARY OBSERVATION — Passage: "On the 16th inst. Johnson & Johnson formally opened their new office at 514 Arch street" — Conf: Medium (TLS) — Corroboration: 2 independent dated volumes of one trade lineage; 1 lineage total (L2) — Conflicts: None; note that L2 is one publication, so volume-to-volume repetition is NOT two witnesses (§3)
```

<!-- NEXT: H, I, J -->

## H

STATUS: WRITTEN 2026-10-07

### H.1 The knowability frame for this market

For 1886–1904 the market is knowable **only as the firm and the trade press describe it**: there is no
national statistical account of surgical-dressing consumption in this corpus, no census-of-manufactures line,
and no third-party market-size statement. The one quantified series held is the company's own.

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Category demand curve, as printed by the firm | absorbent cotton in surgery: *"possibly a little over two hundred pounds"* (1886) → *"estimated at three million pounds"* (1898, at the time of the Spanish War) → *"somewhere from six to ten million"* "at the present time" | `redcrossnotes01` L4666-4676 | **Low**, ESTIMATE class, unattributed, L1, TLS — but it is the *only* demand series held |
| The same market as a table | a three-column consumption table headed `1878 1888 1898` for raw cotton, absorbent cotton, bandages, gauze, lint and "misc. dressings"; the absorbent-cotton row reads `5,000 250,000 3,000,000` lbs | `redcrossnotes00` L40564-40576 | **Low** — the row above it is OCR-mangled (`"Haw cotton, lbs x,ooo 5,ooo 20,000"`), so the table's column mapping is itself partly reconstructed |
| Number of producers | *"a new industry, with nearly a dozen producers, some of whom are able to turn out several tons of cotton and miles upon miles of gauze and bandages in a single day"* | `redcrossnotes00` L40583-40586 | Medium (L1, but a **structural** statement, not a boast) |
| Price direction | the firm prints its **own price cuts** (*"The Prices of Papoid Preparations Have Been Reduc?d"*), and lot terms (`$10.00 lots … 20 per cent`) | `redcrossnotes00` L13340-13343, L8315-8319 | Medium for the fact of reduction; **UNKNOWN** for the new price (OCR) |
| Category maturity at entry | *"In 1886 there were quite as many plaster makers as there are today."* | `redcrossnotes01` L5744 | Medium; L1 retrospective |
| Where the market was **actually** measured by an outsider | the trade press reports **rates, cuts and market behaviour** rather than totals — see §I | `americandruggis29` L26425-26450 (1904) | Medium (**L2**) |

### H.2 The one held independent in-window series, and its exact contribution

The 1896 *American Druggist* report of a **four-story factory addition forced by demand** (§D.1 #5) is the
single best independent market datum in this dossier: it is outsider print, it has a printed volume date, it
names the entity in full, and it attributes the act to *compulsion* ("have been compelled to add") rather
than to ambition. Its contribution is bounded, though: it demonstrates **capacity growth in 1896**, not
market size, not share, and not profitability. **What it did not demonstrate is the whole of §K.**

### H.3 The honesty ledger for §H

* **TRIED–ANSWERED (NULL):** no market-size carrier independent of L1 exists in held bytes (searched for
  consumption, poundage, "per annum", "aggregate" beside namings).
* **TRIED–ANSWERED:** `Listerine` — **13 lines** in held bytes, all in the trade press, and **0 of them name
  Johnson & Johnson as proprietor** (e.g. *"Listerine toilet soap, which sells at $12 a gross to the trade"*).
  A product appearing in the trade press is a lead about a product, not a naming of this registrant (RD-124).
  The probe's §5.6 measurement reproduces exactly.
* **UNTRIED:** the 44 *Pharmaceutical Era* volumes; the other 790 American Druggist items; any government
  series (no tool in `tools/` reaches a 1900-era manufacturing census).
* **UNANSWERED:** Chronicling America — all seven endpoint shapes `CHALLENGED` (403) from this egress per
  `00_universe/harvest/_CA_ENDPOINT_TEST.md`; no CA count for jnj may be reported as a null.

## I

STATUS: WRITTEN 2026-10-07

### I.1 Competition, with a naming collision that must never be smoothed

| Competitor as the record names it | What is held, and where | Lineage / date | Confidence |
|---|---|---|---|
| **Seabury & Johnson**, of East Orange, N. J. | a **party to the plaster price agreement** with J&J c. 1898–99 and a **defendant** in J&J's own bill of equity over the Red Cross device and simulated blue cartons; also listed on a druggists' association slate | `americandruggis29` L26436-26438, L33726-33728 (L2, 1904); `redcrossnotes00` L50006-50009 (L1, 1897–1900); `americandruggis01` L46097 (L2, 1902) | Medium — and **the single most dangerous string in this corpus**: a firm whose name ends "& Johnson", trading in the same commodity, in the same state |
| **J. Ellwood Lee Company**, of Conshohocken, Pa. | party to the same agreement; reported as **starting the 1904 price cut** that broke it | `americandruggis29` L26437-26438, L33735-33738 | Medium (L2) |
| **Bauer & Black**, of Chicago | party to the same agreement; reported as **meeting the cut** | `americandruggis29` L26438, L33739-33740 | Medium (L2) |
| "a few leading hospitals" | preparing their own dressings and doing it well — the firm's own framing of the quality benchmark it entered against | `redcrossnotes00` L9288-9290 | Medium (L1) |
| unnamed plaster makers | *"quite as many plaster makers as there are today"*, of *"the diachylon and pitch type"* | `redcrossnotes01` L5744-5747 | Medium (L1) |
| **both "& Johnson" firms in one sentence** | the trade press lists them **adjacent** at L4868 and L26436, so any grep that truncates at "& Johnson" attributes one firm's acts to the other | `americandruggis29` L4868 | High (a hazard, not a claim) |

### I.2 The plaster combine, which is the best in-window competition evidence in the corpus

> *"PLASTER COMBINE DISRUPTED? … Philadelphia, August 17.— It is reported that there has been a disruption in
> the business arrangements made some five or six years ago between the various manufacturers of plasters. At
> that time the following firms agreed to maintain prices: Johnson & Johnson, of New Brunswick, N. J.; Seabury
> & Johnson, of East Orange, N. J.; J. Ellwood Lee Company, of Conshohocken, Pa. and Bauer & Black, of Chicago.
> All other goods may have been cut, but these firms held strictly to the prices agreed upon … The so-called
> 'plaster trust,' which in reality, was nothing more than an agreement between the various plaster
> manu…"* — `americandruggis29` L26425-26450, **Vol XLV, July–December 1904**

And its sequel, in the next issue of the same paper: *"a number of firms a few years ago entered into an
agreement to maintain prices on plasters. These firms were parties to the compact … However, the agreement,
or 'understanding,' as some are pleased to term it, is now a thing of the past. It seems to be a case of
'every one for himself and the devil take the hindmost,' as one manufacturer put it … The present rate war,
according to statements made the other day, started last month when the J. Ellwood Lee Company … offering a
material reduction in prices."* — L33715-33740.

**Four consequences, each a finding rather than a decoration:**
1. **The firm is named by outsiders inside a market-structure story**, which is the second lineage doing work
   no house print can do (§3 independence).
2. It **dates the firm's market position** without dating its origin: a price agreement *"some five or six
   years ago"* from an August-1904 dateline places J&J among **four named plaster manufacturers c. 1898–99** —
   contemporaneous with, and independent of, L1's 1886-\*87 claim.
3. It is the corpus's best **negative signal** outside the company's own voice: by 1904 the price structure
   the firm had joined is in open **rate war** (§M).
4. It is an **antitrust-vocabulary hazard** for later passes: the trade paper itself calls it a *"so-called
   'plaster trust'"* and then denies the word ("in reality, nothing more than an agreement"). This volume
   quotes both halves and **adjudicates neither**: no suit, consent decree or indictment naming Johnson &
   Johnson is held anywhere. **The 1898–99 agreement is documented; its legality is not.**

### I.3 Claim records for §I

```
I01 Claim: Outside trade print names Johnson & Johnson as one of four plaster manufacturers that agreed to maintain prices around 1898-1899 and reports that agreement in open disruption by August 1904 — Date: agreement c.1898-1899; report 1904-08-17 and the following issue — Source: American Druggist and Pharmaceutical Record, Vol XLV — Source date: Jul-Dec 1904 — Local bytes: americandruggis29unkngoog_djvu.txt L26425-26450 and L33715-33740 — Tier: 1 (trade) — Class: CONTEMPORARY OBSERVATION — Passage: "At that time the following firms agreed to maintain prices: Johnson & Johnson, of New Brunswick, N. J." — Conf: Medium (TLS; the dateline gives the month, the volume the half-year) — Corroboration: 2 issues of one L2 lineage; 1 independent lineage — Conflicts: None; see U.007 for the gap between an outsider naming a market act and naming a firm's scale
```
```
I02 Claim: The corpus contains a competitor whose trade name ends in "& Johnson", requiring full-string entity adjacency in every later pass on this company — Date: 1897-1904 — Source: americandruggis29 L4868, L26436-26438; americandruggis01 L46097; redcrossnotes00 L50006 — Source date: 1904; 1902; 1897-1900 — Tier: 1 — Class: FACT (a property of the record, not of the market) — Passage: "L. W. De Zeller and W. M. Davis, of Seabury" — Conf: High — Corroboration: n/a — Conflicts: None
```

## J

STATUS: WRITTEN 2026-10-07

### J.1 Technology, as a firm's own process print

| Variable | Value | Source | Confidence |
|---|---|---|---|
| The core technical claim | **sterility maintained through manufacture and packaging**, not a new molecule: *"In the publications issued from the Johnson & Johnson laboratories the many methods … employed for cotton sterilization have b…"* | `redcrossnotes00` L38862 | Medium (L1) |
| The process print itself | *"The following pages give in brief the methods [by] which surgical dressings are prepared in our laboratories"* — a company publishing its own method as marketing | `asepsissecunduma00john` L141-143 (**1897**, own title page) | Medium-High for 1897; **first-person plural, company-authored** |
| The machine | carding-and-rolling with alternate tissue-paper wrappings, *"automatically"* | `redcrossnotes00` L40619-40622 | Medium; undated by its own author ("in or about") |
| The chemistry the firm sells on | bichloride-of-mercury dosing (*"one to one thousand"*), camphenol antiseptic wash, carbolised petrolatum, antiseptic tablets, "Red Cross Aseptic Catgut" | `johnsonsfirstai00…` L1056, L2440-2444, L2798; `redcrossnotes00` L31825 | Medium |
| A technical contribution attributed to the firm's president | *"Making Belladonna Plasters"* — and the claim that **his method was adopted into a standard reference**: *"Mr. Johnson's method of making was incorporated into the 16th edition of the United States Dispensatory (see Emplastra page 555), and was also described in detail in various pharmaceutical journals. [M]r. Johnson was the first to lift the veil of secrecy that covered the making of india rubber plasters, and to give the pharmaceutical profession the full benefit of his discovery and experience"* | `belladonnaastud00incgoog` L184-185, L2431-2435 (volume date ≥1893, UNCONFIRMED) | Medium (an **author's own footnote** — self-claim inside a multi-author volume); **not verified against the Dispensatory, which is not held** → §L, U.007 |
| Failure mode the firm describes in its own trade | **product instability**: raw-rubber plasters deteriorate with heat, light and oxygen — *"inan hour's sunlight a plaster is hopelessly ruined"* | `belladonnaastud00incgoog` L2418-2428 | Medium; and it is the closest thing to a **known defect class** in held print (§M) |
| What is not reconstructible | no machine maker is named, no patent number appears in any held line, no yield, no throughput, no defect rate, no factory layout, and the **relationship between the cotton-roll claim and the 1896 building** is inference, not evidence | sweep; §S gap | High (of the absence) |

**Coda (§16 duty).** The technical story the print supports is narrow and defensible: by **1897** the firm was
publishing its aseptic method **as an advertisement for its own goods**, in its own print, from its own
laboratories, under a trade device (the Red Cross) it was already litigating to protect. The mechanism from
method to position is **plausible but unmeasured here**: with no sales figure and no defect data, print cannot
show that sterility assurance produced adoption rather than accompanying a category whose demand was rising
by two orders of magnitude (§H.1). Alternative explanation available in held bytes: **advertising**, which the
1896 outsider explicitly credits (L14596-14599). Confidence in the causal sentence: **Low**; mechanism named
(`method → printed instruction → druggist purchase`) but **untested**.

<!-- NEXT: K, L -->

## K

STATUS: WRITTEN 2026-10-07

### K.1 Money and personal finances — the honest answer is a table of what is not there

| Variable | Value | Source | Confidence |
|---|---|---|---|
| Capital, capitalisation, shares, par value | **UNKNOWN** — no held line in any lineage prints a capital figure. The single corpus line on the subject is generic: *"maintained for the purpose of paying dividends or solely for the…"* (`redcrossnotes01` L15654), which is a comment, not this firm's finance | sweep for `capital stock\|shares of stock\|dividend\|organized under` across all 15 layers: **3 lines, none a J&J figure** | High (of the measured absence) |
| Revenue, sales, profit, cost of goods | **UNKNOWN at every date in the window.** No held line prints any of them for this entity | sweep | High |
| Retail prices that *are* printed | First Aid Cabinet `$6.0U` [**$6.00**, bytes]; Aseptic Armamentarium **$5.00**; disinfecting fluid **50 cents / 10 cents a bottle**; *"ten cents a box"*; digestive tablets former price **$1.25 for 100**, then **OCR-corrupt**; lot terms **$10.00 lots, 20 per cent**; rubber **$1.25 to $2.25** | `johnsonsfirstai…` L2405, L4147-4152, L5257; `asepsissecunduma…` L1366; `redcrossnotes00` L13343, L8315-8319; `modernmethodsofa00john` L1455 | Medium; **catalogue prices, not revenue** (§E.2 denominator) |
| A price **cut** the firm announced | *"The Prices of Papoid Preparations Have Been Reduc?d"* — new figure illegible | `redcrossnotes00` L13340-13343 | Medium (the fact); **UNKNOWN** (the amount) |
| A **tax** loss, third-party | stamp taxes assessed under *"the act of June 13, 1898, relating to proprietary medicines"*; the Commissioner **decided against** the firm; four suits aggregating **$40,800** brought by Johnson & Johnson against the Collector of Internal Revenue for Newark district, *"They sue for the money paid out for the stamps."* | `americandruggis13` L6215-6226 (Vol XL, Jan–Jul **1902**) | Medium; **L2**, and the only money figure in this dossier that an outsider printed |
| Family/personal capital of a principal | *"Mr. Johnson's present to the bride was $100,000 in securities"* — a marriage paragraph naming *"Robert W. Johnson (Johnson & Johnson)"*, of **New Brunswick** | `americandruggis29` L69115-69119 (Nov **1904**) | Medium; L2; **this is not company capital** and must never be entered as such (it is a personal transfer reported in a trade weekly) |
| Wages, payroll, hours | **UNKNOWN**; only *"employees, numbering many hundreds"* | `redcrossnotes00` L4103 | Medium (the phrase) |
| Public issuance/registration | **nothing**: no in-window instrument of any kind, and the registrant's filing history begins **1994-03-10** (`(PB)`); **the string `1886` occurs 0 times in the 26 stored filing bodies** | `sources/_index`, `sources/sec` | High |

### K.2 What a reader may not conclude from K.1

The absence of money is **not** evidence of a small business, of self-financing, or of an unremarkable
financial record — it is evidence that **a private nineteenth-century manufacturer published no accounts and
no archive of its accounts has been reached**. §10's research-debt trigger fires: *"a financial figure looks
inconsistent / funding history is incomplete"* cannot even be evaluated here. The named routes are: New
Jersey Secretary of State charter and assessment records (no tool), the firm's own later annual print
(`John0851_1970` is the earliest company annual report on disk and is `(PB)`), and *Pharmaceutical Era*
advertising columns, which in this era carried capital and dividend notices for incorporated druggists' firms.

### K.3 Claim record for §K

```
K01 Claim: The only outsider-printed money datum for the firm in the window is adverse: stamp taxes assessed under the 1898 proprietary-medicines act, decided against the firm by the Commissioner of Internal Revenue, and sued out in four actions aggregating $40,800 — Date: suits noticed 1902; tax act 1898-06-13 — Source: American Druggist and Pharmaceutical Record, Vol XL — Source date: Jan-Jul 1902 — Local bytes: americandruggis13unkngoog_djvu.txt L6215-6226 — Tier: 1 (trade) — Class: CONTEMPORARY OBSERVATION — Passage: "The suits are brought for stamp taxes assessed upon various preparations made by the plaintiffs, under the act of June 13, 1898, relating to proprietary medicines." — Conf: Medium (TLS) — Corroboration: 1 independent lineage — Conflicts: None; the aggregate $40,800 is a claim amount, NOT a loss amount, and the firm's own later account of the same period prints nothing about it
```

## L

STATUS: WRITTEN 2026-10-07

### L.1 Validation signals, in the §7 validation format

| Date | Signal | Magnitude | What it demonstrated | What it did NOT demonstrate | Source | Confidence |
|---|---|---|---|---|---|---|
| c. **1893 or later** (volume date unconfirmed) | A principal of the firm is printed as **authoritative in his trade**: a named contribution on plaster making, by the firm's President, in a multi-author professional volume | 1 contribution; 1 office | that the firm had technical standing the profession printed | that the firm sold anything, or to anyone | `belladonnaastud00incgoog` L184-185 | Medium |
| same volume | **the author's own footnote**: his method *"was incorporated into the 16th edition of the United States Dispensatory"*, and he *"was the first to lift the veil of secrecy"* | 1 adoption claim, page 555 cited | that the firm **claimed** standardisation; and that it claimed it in a professional venue | **anything about the adoption** — the Dispensatory is not held, and no independent line confirms it | L2431-2433 | **Low** (self-claim, unverified against the cited edition) |
| **1896** Jan–Jun | An outsider reports the firm **"compelled to add a four-story building"** to its New Brunswick factory | +1 building, 4 stories, previously unoccupied | capacity growth, witnessed by a second lineage, with a demand rationale | sales, share, profitability, or how long the boom lasted | `americandruggis07` L94, L14592-14600 | Medium |
| **1897** | The firm publishes **its own aseptic method** with a priced kit, from *"our laboratories"*, under a New Brunswick, New Jersey title page | $5.00 kit | that the process was formalised and marketable by 1897 | adoption, or that competitors could not do the same | `asepsissecunduma00john` L119-135, L1366 | Medium-High for 1897 (TLS caps it at Medium) |
| **1898** (Cuban campaign) | *"370,000 were supplied by order of the United States Government to the Army and Navy"* | 370,000 packets | the firm's own claim of a government-scale order | the order, the count, or the period — **no denominator, no contract, no record** | `johnsonsfirstai…` L2464-2466 | Medium (of the 1901 printing); **UNKNOWN** (of the fact) |
| **1898–99** (reported 1904) | Named by outsiders as one of **four firms holding plaster prices** in a four-firm market | 4 named firms | that J&J was one of a handful of manufacturers big enough to be listed with its competitors — **the strongest status datum in this dossier** | that the agreement was lawful, durable, or that J&J joined willingly | `americandruggis29` L26432-26438 (L2) | Medium |
| **1899** (July, in a filing narrative) | The firm sues over **imitation of its packaging** — *"in the month of -July, 1899, the defendants devised cartons which were unnecessary imitations"* | 1 bill in equity | that the firm's **trade dress** had market value worth litigating — a demand-side signal the company did not intend to send | the outcome of the suit, or whether the imitation succeeded | `redcrossnotes00` L49989-50009 (L1) | Medium (L1, self-published legal narrative) |
| **1901** (copyright) | **7,000+** First Aid Cabinets *"in use in manufacturing establishments"*; adoption by *"several of our chief Railroad Systems"*; Boards of Education placing the cabinet in public schools and adopting the Manual as a textbook | 7,000 cabinets, uncounted institutions | the firm's own account of institutional reach | every institutional fact in the sentence; no school, system or establishment is named | L2397-2400 | Medium (printing); **0 independent** (fact) |
| **1902** | A **Philadelphia office formally opened** at 514 Arch street; trade print reports *"city salesmen report every day at noon"* | 1 branch, 5+ named cities of representation | a distribution system outside the home state, dated by outsiders | that the branch was profitable | `americandruggis01` L61049, L67215 | Medium |
| **1904** Nov | A trade weekly records the marriage of the **daughter of "Robert W. Johnson (Johnson & Johnson)"**, of New Brunswick, with a **$100,000 securities** gift | $100,000 (personal) | that the firm's principal family was locally prominent enough for the trade press to gloss the name with the **company in parentheses** — i.e. the name *was* the brand by 1904 | company capital, or that the man is the 1893–94 President (naming variant) | `americandruggis29` L69115-69119 | Medium |

### L.2 The repeatable-validation verdict, held tightly

The best validation evidence in this dossier is **not** the company's own numbers; it is the **four outsider
datums** — 1896 (compelled building), 1896/1902/1904 (a named city-salesman network and a branch office),
1902 (a suit in its own name in the New Jersey revenue district), and 1904 (a four-firm price agreement plus
a name-gloss in a marriage paragraph). Together they establish that by **1896–1904** the firm was a
multi-state, institutionally-selling manufacturer recognised by name by its own trade. **None of them
validates the 1886-\*87 origin claim**, which remains single-lineage and retrospective; and the
quantified adoption series (370,000 / 7,000) has **no independent count anywhere in reach** (U.007): the
route is a *Pharmaceutical Era* or ordnance/Quartermaster record, and no tool in `tools/` reaches the latter.

### L.3 Claim records for §L

```
L01 Claim: The strongest repeatable-validation datum held is an independent 1896 report that demand compelled a four-story factory addition at New Brunswick — Date: Jan-Jun 1896 — Source: American Druggist Vol XXVIII — Source date: 1896 — Local bytes: americandruggis07unkngoog_djvu.txt L94, L14592-14600 — Tier: 1 — Class: CONTEMPORARY OBSERVATION — Passage: "have been compelled to add a four-story building, hitherto unoccupied, to their factory at New Brunswick, N. J." — Conf: Medium (TLS cap on an otherwise High, independent, self-dated carrier) — Corroboration: 1 independent lineage; L1 silent on the building — Conflicts: None
```
```
L02 Claim: The firm's claim that its plaster method was taken into the United States Dispensatory is a self-claim resting on a page citation to a work not held — Date: volume >=1893, UNCONFIRMED — Source: belladonnaastud00incgoog, author's footnote — Source date: UNKNOWN — Local bytes: L2431-2433 — Tier: 1 for the printing; the adoption is unverified — Class: FOUNDER-CLAIM-adjacent self-claim, RETROSPECTIVE as to 1880s method — Passage: "Mr. Johnson's method of making was incorporated into the 16th edition of the United States Dispensatory (see Emplastra page 555)" — Conf: Low — Corroboration: 0 — Conflicts: U.007
```
```
L03 Claim: The quantified adoption series (370,000 government packets; upwards of 7,000 cabinets) is one lineage recounting itself, with no institution named — Date: 1898 events; 1901 printing — Source: johnsonsfirstai00unkngoog — Source date: 1901 — Local bytes: L2464-2466, L2397-2400 — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION / corporate self-claim — Passage: "Upwards of seven thousand Johnson's First Aid Cabinets are in use in manufacturing establishments." — Conf: Medium for the printing, UNKNOWN for the counts — Corroboration: 0 independent — Conflicts: U.007
```

<!-- NEXT: M, N, O -->

## M

STATUS: WRITTEN 2026-10-07

### M.1 Negative signals and failures actually held

| Date | What the record holds | Lineage | Class | Confidence |
|---|---|---|---|---|
| **1898** onward | **An adverse administrative determination and a tax cost.** Stamp taxes assessed on the firm's preparations under the act of June 13, 1898; the firm argued they were not taxable; *"the matter was referred to the Commissioner of Internal Revenue, who decided against them. They sue for the money paid out for the stamps."* Four suits, aggregating **$40,800** claimed | **L2** | CONTEMPORARY OBSERVATION of a real adverse outcome | Medium |
| **1899 (July)** | **Imitation of the firm's goods** — the market's verdict that its packaging was the valuable thing: *"the defendants devised cartons which were unnecessary imitations in size and shape, and in color of interior wrappings, and 'sold the said simulated packages bearing labels consisting in part of a red cross as and for Red Cross Cotton, and as and for the cotton of Johnson & Johnson'"*, characterised in the firm's own bill as *"acts essentially unfair, inequitable and fraudulent, and to the great loss and injury of Johnson & Johnson"* | **L1** (self-published narrative of its own filing) | FACT about the printing; the suit's **outcome is UNKNOWN** | Medium |
| **c. 1898–99 → 1904** | **The price structure broke.** By August 1904 the four-firm plaster agreement is reported in *"open disruption"*, a *"rate war"*, *"every one for himself and the devil take the hindmost"* | **L2** | CONTEMPORARY OBSERVATION | Medium — margin pressure on a named party, with no J&J income figure to measure it against |
| **1897–1900** | **The firm printed its own price cut** on a product line ("Papoid Preparations"), new figure OCR-corrupt | L1 | FACT of the printing | Medium (fact), **UNKNOWN** (amount) — a cut is a signal, and the print does not say why |
| **in the 1893+ volume** | **A defect class described by the maker**: raw-rubber plasters ruined by heat, light and oxygen — *"inan hour's sunlight a plaster is hopelessly ruined"*; *"a cheap, poorly made plaster often has the requisite of keeping unchanged"* (i.e. good ones fail while bad ones pass) | L1-adjacent | CONTEMPORARY OBSERVATION of a product limitation | Medium |
| **in the UNCONFIRMED-date volume (1914+ copyrights)** | A second defect-and-fix narrative: *"Dampness causes a decomposition of the elements of the mustard, the essential oil is released or destroyed, and the plasters rendered useless. Johnson & Johnson accomplished a solution of the difficulties in the preparation of mustard plasters. A moisture-proof and easily opened package has been produced … a round spun metal tube, seamless…"* | **L1** | FACT for the printing; **RETROSPECTIVE/undated** as to when | Medium (printing); Low (date) |
| **1904** | Being **named in the same sentence as a "plaster trust"** in the trade press, whatever the paper's own denial of the word | L2 | CONTEMPORARY OBSERVATION of reputation exposure | Medium; **no legal consequence is held** |

### M.2 What is *not* held, and the difference it makes

**No recall, seizure, condemnation, destruction of goods, fire, factory accident, refusal of a contract,
bankruptcy, default, closed branch or withdrawn product** appears in any held line for this firm. Verified
by a negative-word sweep (`recall|seizure|adulterat|misbrand|fraud|infringement|\bsued\b|lawsuit|damages|
injunct|counterfeit|withdraw|burned|destroyed|bankrupt`) within ±3 lines of every naming, run twice: the
**loose** pattern (bare `sued`, which also matches "iss**ued**") returns **29** lines and 24 of them are that
artefact; the **word-boundary-correct** sweep returns **5** — *"damages"* once (the stamp-tax suits),
*"fraud"* once (the Red Cross imitation bill), *"destroyed"* once (the decomposition of **mustard oil** in a
plaster, not the destruction of a firm's goods), and *"sued"* twice, both inside `form a fair-sued
communiiy in themselves` — an OCR garble of "fair-sized community" in a house-print piece about the
**operatives** (*"The operatives of Johnson & Johnson … only bright, clean, healthy people could prepare
surgically clean dressings"*, `redcrossnotes01` L8096-8104). **Nothing else.** So the correct §M statement is
the probe's, sharpened: **the first incurred failure of this company is not established** (probe §5.5), and
the two real negatives held are (i) an **adverse tax determination the company then litigated** and (ii) **a
price war it was named inside**. Neither is a collapse; both are more than "nothing happened".

**The §15.2 rule bites here:** failure is the claim class most likely to live in an **unopened** volume.
Trade print of this era carries condemnation notices, pure-food-and-drugs enforcement lists, assignment
(insolvency) notices and coroners' reports in the back matter, and **790 of 795 American Druggist items and
44 of 44 *Pharmaceutical Era* items are unopened**. Recording §M as "two adverse datums, no failure
established, 99% of the searchable corpus unopened" is the deliverable; a smoother sentence would be false.

### M.3 Claim records for §M

```
M01 Claim: The corpus holds a dated, third-party record of an adverse determination against the firm and the firm's decision to sue over the money it paid — Date: act 1898-06-13; suits noticed by Jan-Jul 1902 — Source: American Druggist Vol XL — Source date: 1902 — Local bytes: americandruggis13unkngoog_djvu.txt L6215-6226 — Tier: 1 — Class: CONTEMPORARY OBSERVATION; FACT that the suits were noticed — Passage: "who decided against them. They sue for the money paid out for the stamps." — Conf: Medium — Corroboration: 1 lineage (L2) — Conflicts: None; the suits' OUTCOME is UNKNOWN and is a §S gap
```
```
M02 Claim: The firm's own print records that a competitor imitated its Red Cross cotton packaging in July 1899 and that it petitioned a court of equity against Seabury & Johnson — Date: imitation July 1899; print 1897-1900 — Source: Red Cross Notes — Source date: 1897-1900 — Local bytes: redcrossnotes00johngoog_djvu.txt L49975-50010 — Tier: 1 — Class: FACT for the printing of a bill's narrative; the events charged are the complainant's own allegations, so RETROSPECTIVE/advocacy as to fact — Passage: "acts essentially unfair, inequitable and fraudulent, and to the great loss and injury of Johnson & Johnson" — Conf: Medium (that the narrative was printed); UNKNOWN (whether the court agreed) — Corroboration: 0 independent — Conflicts: None; note the entity is called "which corporation" in this same passage, feeding U.002
```
```
M03 Claim: No recall, seizure, fire, default, closed branch or product withdrawal by this firm is recorded in any held line; the word-boundary negative sweep returns 5 lines, of which 2 are the tabled matters (stamp-tax suits; the Red Cross imitation bill) and 3 are OCR artefacts about mustard oil and a "fair-sued [fair-sized] community" of operatives — Date: 1886-1904 — Source: 15 layers, 642 naming lines — Source date: swept 2026-10-07 — Tier: n/a — Class: FACT (of the measured absence over held bytes); the record itself is 99% unopened — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High (of the sweep); UNKNOWN (of the underlying history) — Corroboration: n/a — Conflicts: None; logged as gap G-7 and UNTRIED U2
```

## N

STATUS: WRITTEN 2026-10-07

### N.1 Decisions, in the §7 decisions format, attributed to a **firm** not a founder

Every row below is sourced to print, and the actor column records what the print actually says. Where the
print's subject is "the firm", "they", "The Johnsons" or an anonymous "I", **no person is substituted** —
that substitution is precisely the defect §14 and the Morgan Stanley/Cigna/AT&T history were written to stop.

| Date | Decision | State before | Information available | Unknowns | Alternatives | Constraints | Rationale (in the print's own words) | Expected result | Actual result | Evidence | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **1886-\*87** (as narrated 1897–1900) | Enter the surgical-dressing trade rather than contest established plaster trade: *"create a place for themselves and then attempt to fill it"* | a crowded plaster market; the firm's rubber-plaster background | what only the firm says it knew | who decided; what else was weighed; whether any alternative was considered | UNKNOWN — **no alternative is printed except the one it says it rejected** | private firm; a category whose goods were made by hospitals themselves | *"rather than contest for the trade of others already established"* | *"commodities new in use and purpose"* | UNKNOWN within the stage; the nearest outsider datum is the 1896 forced expansion | `redcrossnotes01` L5752-5760 (L1, vol. date UNCONFIRMED) | **Low** as an event; Medium as a printing |
| **"in or about 1886"** | Build **machinery** to roll cotton with separable layers instead of selling wads | wads, packed loosely | the firm's own account of the old article's defects (*"yellow and dirty … not absorbent"*) | who designed it, what it cost, when it was installed, whether anyone else could copy it | UNKNOWN | its own capital, unknown | to *"keep the several layers separate and apart for convenience in handling and use"* | *"it opened the new era"* | category demand rose over the same period (§H), which the print then uses as proof | `redcrossnotes00` L40603-40628 (L1) | **Low** (single lineage, hedged date, unstable narrator) |
| **1887** (as narrated) | **Become a corporation** | a firm | none held | which persons; under what state's law; with what capital | UNKNOWN | UNKNOWN | not printed | UNKNOWN | only the sentence that it happened | `redcrossnotes01` L5718 | **Low** — the single most consequential unresolved decision in the stage (U.002) |
| **by 1896** | Invest in **capacity** at New Brunswick (add the four-story building) | a factory the trade press already describes as the firm's | an outsider reports the *cause*: the Vino-Kola boom plus *"judicious and novel advertising"* | whether the firm chose it or was forced by a landlord/lease; what it cost | UNKNOWN | capital, unknown | the trade's own verb: *"have been compelled to add"* | supply | the 1904 price war suggests the category later over-supplied itself | `americandruggis07` L14592-14600 (**L2**) | **Medium** — the only decision-shaped fact this dossier holds from an independent lineage |
| **1897** | **Publish the method** (print the aseptic process as a company document, with a priced kit) | methods kept as trade secrecy; the firm's own author claims to have *"lift[ed] the veil of secrecy"* | its laboratories, its device | how much detail rivals gained | UNKNOWN | secrecy was the trade norm | to convert process into a **credibility asset** sellable to pharmacists | demand for the method and the goods together | by 1897–1900 it is running its own monthly periodical for employees and patrons | `asepsissecunduma00john` L141-150; `belladonnaastud…` L2433-2435 | Medium |
| **1899** | **Litigate the Red Cross device and package dress** against Seabury & Johnson | imitation in the trade | its own bill's allegations | the forum's decision; whether it won | UNKNOWN | a competitor's copy | protection of *"characteristic appearance"* | exclusion | UNKNOWN (no outcome held) | `redcrossnotes00` L49975-50010 | Medium (that it sued); UNKNOWN (result) |
| **1898–1902** | **Pay the stamp taxes under protest and sue the Collector** | assessed taxes | the statute (act of 1898-06-13), the Commissioner's adverse decision | the firm's own accounting of the amounts | UNKNOWN | non-payment risked licence | recovery of *"the money paid out for the stamps"* | repayment | UNKNOWN (no outcome held) | `americandruggis13` L6215-6226 (**L2**) | Medium |
| **1902** | **Open a Philadelphia city office** (514 Arch street) | city-salesman representation only | the trade's report of the opening and of salesmen *"reporting every day at noon"* | cost, staffing, terms | UNKNOWN | keep to the mail-order and druggist route | UNKNOWN — no rationale printed | wider reach | still trading from the "Johnson Building" in 1904 | `americandruggis01` L61049; `americandruggis29` L13001 (**L2**) | Medium |

**Coda (§16).** The only decision in this table that **both lineages** touches is capacity: the firm prints
what the trade press reported in 1896. Everything else about the origin rests on a single company's later
telling of itself. Mechanism is nameable for two of them (publish-the-method → credibility → druggist
purchase; litigation → protection of a device that outsiders already found worth copying), and the alternative
explanation for the firm's rise — advertising, category growth, and being one of only four firms able to hold
prices — is available in held print. Confidence that the origin decisions caused the position: **Low**.

## O

STATUS: WRITTEN 2026-10-07

### O.1 Counterfactual opportunities, framed only from what the print itself puts in play

| Opportunity | Held evidence that it was live in-period | Why the corpus cannot say it was taken or missed | Class |
|---|---|---|---|
| **Contest the established plaster trade directly** | the firm prints that it considered and refused it: *"rather than contest for the trade of others already established"* | The refusal is the company's own retrospective account of an option it says it rejected; **no independent record shows the option existed as a choice anyone weighed** | RETROSPECTIVE INTERPRETATION |
| **Sell to hospitals instead of druggists** | *"dressings prepared by a few leading hospitals and immediately used gave good results"* — hospital self-manufacture is printed as the quality benchmark | No held line shows the firm ever bid a hospital, and none shows a competitor doing so through the trade | INFERENCE, Low |
| **Keep the plaster method secret** (the trade norm it says it broke) | *"[Mr. Johnson] was the first to lift the veil of secrecy that covered the making of india rubber plasters"* | A self-claim in his own footnote; whether rivals' methods were in fact secret is untestable here | self-claim, Low |
| **Stay a firm rather than become a corporation** | the print distinguishes "the firm of Johnson & Johnson" (1886-\*87) from "they became a corporation" (1887) | No charter, no capital, no shareholders, no motive; the corporate leg exists in this corpus **only as a sentence** | RETROSPECTIVE INTERPRETATION, Low (U.002) |
| **Ride the government channel** | *"supplied … to the U. S. Government for the use of the Army and Navy"*; *"an improvement on the regular Army packet and … particularly adapted to times of peace and to factory injuries"* | The pivot from war packet to peacetime cabinet is the firm's own marketing sentence; no contract, no award, no competitor for the order is held | self-claim, Medium as printing, UNKNOWN as decision |
| **Hold prices with the combine** | named as a party to the 1898–99 agreement, and as a sufferer when it broke in 1904 | Whether the firm renewed, resisted or exploited the rate war is not printed anywhere; its own price cut on Papoid is undated and unexplained | CONTEMPORARY OBSERVATION of the compact; **UNKNOWN** of the firm's choice |

### O.2 What this section deliberately does not do

It does **not** invent an opportunity the firm "should have" taken (no held line names a rejected option, a
missed market or an internal debate — **zero** bytes record anyone deciding anything, §Header), and it does
not use the company's later history (Band-Aid 1920–21, `(PB)`, **0 lines held**) as proof that any 1898
choice was farsighted. The anti-hagiography test is met by the emptiness itself: **a reconstruction that
could not name a single rejected alternative is the honest output for this archive**, and that fact is a
`data_gaps` row (G-8), not a paragraph of speculation.

<!-- NEXT: P, Q, R -->

## P

STATUS: WRITTEN 2026-10-07

### P.1 Quantitative metrics table

Every row is a quantity that **appears in held bytes**. Nothing here is computed from another row except
where the `derived` note says so, and **no revenue, capital, profit or wage figure exists to be tabulated**
(§K). `Conf` carries the UNVERIFIED-TLS cap (§Header).

| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |
|---|---|---|---|---|---|---|---|
| Q01 | 1886 | absorbent cotton used in surgery, firm's own estimate | ~200 | pounds | P1S02 `redcrossnotes01` L4666-4668 | vol. date UNCONFIRMED (1914+ copyrights) | Low (ESTIMATE, L1, unattributed) |
| Q02 | 1898 | the same, "at the time of the Spanish War", firm's estimate | ~3,000,000 | pounds | P1S02 L4668-4671 | UNCONFIRMED | Low (ESTIMATE) |
| Q03 | "at the present time" (of the printing) | the same, firm's estimate | 6,000,000–10,000,000 | pounds | P1S02 L4674-4676 | UNCONFIRMED | Low (ESTIMATE; band as printed) |
| Q04 | 1878 / 1888 / 1898 | absorbent cotton consumption row of the firm's table | 5,000 / 250,000 / 3,000,000 | pounds | P1S01 `redcrossnotes00` L40564-40576 | 1897-1900 | Low (adjacent row OCR-corrupt; column mapping partly inferred) |
| Q05 | 1898 (Cuban campaign) | first-aid packets supplied by U.S. Government order | 370,000 | packets | P1S03 `johnsonsfirstai…` L2464-2466 | 1901 (copyright leg) | Medium (printing) / UNKNOWN (fact, 0 independent) |
| Q06 | by 1901 | First Aid Cabinets in use in manufacturing establishments | "upwards of 7,000" | cabinets | P1S03 L2397 | 1901 | Medium (printing) / UNKNOWN (fact) |
| Q07 | 1901 | First Aid Cabinet retail price | 6.00 | USD | P1S03 L2405 (bytes `$6.0U`) | 1901 | Medium |
| Q08 | 1897 | Aseptic Armamentarium price | 5.00 | USD | P1S04 `asepsissecunduma…` L1366 | 1897 (own title page) | Medium-High→**Medium** (TLS) |
| Q09 | 1901 | disinfecting fluid, retail | 0.50 (large) / 0.10 (small, per bottle) | USD | P1S03 L4147-4152 | 1901 | Medium |
| Q10 | 1897-1900 | digestive tablets, **former** price | 1.25 per 100 | USD | P1S01 `redcrossnotes00` L13343 | 1897-1900 | Medium (the new price is OCR-corrupt: **UNKNOWN**) |
| Q11 | 1897-1900 | trade lot terms, plain gauze bandages / ligatures | 10.00 per lot, 20 per cent terms | USD | P1S01 L8315-8319 | 1897-1900 | Medium |
| Q12 | 1902 | four suits brought by the firm against the Internal Revenue Collector, Newark district, aggregate claimed | 40,800 | USD | P1S07 `americandruggis13` L6215-6218 | Jan-Jul 1902 (Vol XL) | Medium (**claim amount, not loss**) |
| Q13 | 1904-11-09 | personal marriage gift recorded in trade print, "Robert W. Johnson (Johnson & Johnson)" | 100,000 | USD in securities | P1S09 `americandruggis29` L69115-69119 | Jul-Dec 1904 (Vol XLV) | Medium (**not company capital**; §K) |
| Q14 | 1896 | factory capacity act | +1 building, 4 stories | buildings | P1S06 `americandruggis07` L14592-14595 | Jan-Jun 1896 (Vol XXVIII) | Medium (L2, independent) |
| Q15 | 1897-1900 | employees, as the firm words it | "many hundreds" | persons (unquantified) | P1S01 L4103 | 1897-1900 | Medium for the phrase; **no number is printed** |
| Q16 | c. 1898-99 | named plaster manufacturers holding prices | 4 | firms | P1S09 L26436-26438 | 1904 (report) | Medium (L2; the "five or six years ago" is the paper's own rounding) |
| Q17 | 1897-1900 | producers in the new cotton-dressing industry | "nearly a dozen" | firms (unquantified) | P1S01 L40583 | 1897-1900 | Medium for the phrase |
| Q18 | 1902 | Philadelphia branch office | 514 Arch street | address (a datum, not a number) | P1S05 `americandruggis01` L61049-61050 | Jul-Dec 1902 (Vol XLI) | Medium |
| Q19 | corpus measure | entity namings / layers / bytes held | 642 / 15 / 23,308,643 | lines / files / bytes | this pass; §T | 2026-10-07 | High (a count of bytes read) |
| Q20 | corpus measure | shares of those namings: house print vs trade press vs `(PB)` | 504 / 100 / 23 | lines | §T per-layer counts | 2026-10-07 | High — **DERIVED: 246+258=504; 11+11+7+9+19+1=58 plus 23+1+15+… see §T; the 504/100/23 split is the sum of the per-layer table** |

**Record-selection null for §P (§2):** the absence of money rows is not a modest business; it is the shape of
a survivors' archive built from **advertising print and trade journalism**, in which no account of a private
New Jersey manufacturer's finances was ever printed. Any later pass that "reconstructs" 1886–1904 revenue
from Q05×Q07 or Q06×Q07 is committing an arithmetic forgery: **the cabinet count and the packet count are the
same firm's unsourced self-reports, and no price attaches to the government packets.**

## Q

STATUS: WRITTEN 2026-10-07

### Q.1 Chronological micro-timeline (dated where a carrier dates it; every other row is a printing)

| Date (or range) | Event | Actors | Location | Carrier / class |
|---|---|---|---|---|
| **1886-\*87** | "the date of the formation of the firm of Johnson & Johnson" — as the company prints it, 11–14 years late, in a range | the firm (no person named) | not stated in the sentence | `redcrossnotes00` L9283-9285 · RETROSPECTIVE |
| **in or about 1886** | cotton carding/rolling machinery with tissue-paper interlayers "invented", per the same print | anonymous "I"/"We" | not stated | `redcrossnotes00` L40615-40628 · RETROSPECTIVE |
| **1886** | "began in business in 1886" (second telling, single year) and "quite as many plaster makers as there are today" | "Johnson & Johnson"; "The Johnsons" | not stated | `redcrossnotes01` L5717, L5744 · RETROSPECTIVE |
| **by 1887** | a salesman "engaged with Johnson & Johnson and remained in their service until his death" | the firm | not stated | `americandruggis29` L33894 (1904) · **L2**, obituary retrospective |
| **1887** | "in 1887 they became a corporation" | they | not stated | `redcrossnotes01` L5718 · RETROSPECTIVE; **no charter held** |
| **date UNCONFIRMED (1888 metadata / "1891" call number / cites Feb 1888)** | the firm publishes a surgical method and a **price list** under a New York imprint, 25 and 23 Cedar Street, listing sutures it "furnishes" | JOHNSON & JOHNSON | **New York** | `modernmethodsofa00john` L96, L534-546, L1402, L1459 · FACT of printing (U.004) |
| **≥1893** | "Making Belladonna Plasters" printed by *ROBERT WOOD JOHNSON, Manufacturing Chemist, President Johnson & Johnson Corporation*; author's footnote claims adoption into the 16th U.S. Dispensatory | RWJ; the Corporation | not stated | `belladonnaastud00incgoog` L184-185, L2431-2435 · CONTEMPORARY (role), self-claim (adoption) |
| **Jan–Jun 1896** | outsiders report the firm **"compelled to add a four-story building"** to its New Brunswick factory; the same volume records **Robert Wood Johnson as an incorporator of the New York Red Cross** (a different body — U.010) | the firm; RWJ | New Brunswick, N. J.; New York | `americandruggis07` L94, L14592-14600, L45590-45597 · **L2 CONTEMPORARY** |
| **1897** | the firm publishes its aseptic method from "our laboratories", New Brunswick, with the $5.00 Aseptic Armamentarium; the same year's house print announces the 24-page book *Asepsis Secundum Artem* "recently issued by Johnson & Johnson, New Brunswick. N. J." | the firm | New Brunswick | `asepsissecunduma00john` L119-135, L1366; `redcrossnotes00` L6586 · FACT |
| **1897-1900 print** | "PIONEERS" passage; the Red Cross suit narrative; the "many hundreds" of employees notice; the Papoid price cut | the firm | New Brunswick | `redcrossnotes00` L9281-, L49975-, L4103, L13340- |
| **July 1899** | defendants alleged to have "devised cartons which were unnecessary imitations"; J&J petitions equity against Seabury & Johnson over the Red Cross symbol | complainant/defendant | New Brunswick / East Orange | `redcrossnotes00` L49989-50010 · L1 self-published legal narrative; **outcome UNKNOWN** |
| **1898 (Cuban campaign)** | "370,000 supplied by order of the United States Government to the Army and Navy" | the firm | U.S. Army and Navy | `johnsonsfirstai…` L2464-2466 (printed 1901) · self-report, 0 independent |
| **Jan–Jul 1902** | four suits, $40,800 aggregate, against the Collector of Internal Revenue, Newark district, over 1898-act stamp taxes decided against the firm | the firm; Herold | New Brunswick / Newark, N. J. | `americandruggis13` L6215-6226 · **L2 CONTEMPORARY** |
| **Jul–Dec 1902** | "On the 16th inst. [month UNKNOWN] Johnson & Johnson formally opened their new office at 514 Arch street", Philadelphia | the firm | Philadelphia | `americandruggis01` L61049-61050 · **L2 CONTEMPORARY** |
| **1901 printing; 1903 line** | First Aid Manual: 7,000 cabinets, railroad systems, boards of education, $6.00 price, Accident-Case lineage | the firm | New Brunswick | `johnsonsfirstai…` L158, L89, L2397-2411 · self-report |
| **August 17, 1904** and the next issue | "PLASTER COMBINE DISRUPTED?" — the four-firm price agreement of "five or six years ago" reported in open rate war | J&J; Seabury & Johnson; J. Ellwood Lee; Bauer & Black | New Brunswick / East Orange / Conshohocken / Chicago | `americandruggis29` L26425-26450, L33715-33740 · **L2 CONTEMPORARY** |
| **November 9, 1904** | marriage of "Roberta Wood Johnson, daughter of Robert W. Johnson (Johnson & Johnson)", at Christ Church, New Brunswick; $100,000 in securities | the Johnson family | New Brunswick | `americandruggis29` L69115-69119 · **L2**, name glossed with the firm |
| **1904 (Vol XLIV)** | described by outsiders as *"the manufacturing firm of Johnson & Johnson, New Brunswick, N. J."* | the firm | New Brunswick | `americandruggis26` L61540 · **L2**; the proposed stage close |
| **1914 / 1915 / 1919** | copyright legs inside the second house-print volume — **the volume that carries the 1887 corporate sentence** | the firm | New Brunswick | `redcrossnotes01` L5640, L10219, L27247, L29055 · U.006 |
| **(PB) 1970** | the earliest company **annual report** on disk contains **0 occurrences of "1886"** and 23 namings, and places works at Washington Crossing, N.J. | the registrant | New Brunswick / NJ | `John0851_1970` L7, L387 · `(PB)`, and the §Header late-arrival note |

## R

STATUS: WRITTEN 2026-10-07

### R.1 End-of-stage structured snapshot, at the proposed close (1904-12-31)

| Dimension | State at the close | Strongest held carrier | Class / confidence |
|---|---|---|---|
| Legal person | A **firm** named Johnson & Johnson in 1886-\*87 and, per its own later print, **a corporation from 1887**; called *"which corporation"* in its own 1899 bill and *"the manufacturing firm"* by outsiders in 1904. **No charter held; the identity of the 1887 corporation with the present registrant is unestablished.** | `redcrossnotes00` L50003; `americandruggis26` L61540 | FACT of the printings; **UNKNOWN** of the person (U.002) |
| Place | **New Brunswick, N. J.** as factory and name-of-Record; a **New York** publishing imprint in the earliest company print; a **Philadelphia** city office since 1902 | `americandruggis07` L14595; `modernmethods…` L1402; `americandruggis01` L61049 | Medium; move date UNKNOWN (U.003) |
| Product | Antiseptic surgical dressings, absorbent cotton in rolled form, ligatures and sutures, plasters (rubber, belladonna, mustard), first-aid cabinets and cases, digestive/Papoid and kola preparations, disinfectants | `modernmethods…` L534-546, L1390-1391; `asepsis…` L1366; `johnsonsfirstai…` L2366-2411 | Medium |
| Trade position | one of **four named manufacturers** able to hold plaster prices c. 1898–99, in a category the firm itself counts at "nearly a dozen" cotton-dressing producers; a **four-story** factory addition reported by outsiders in 1896 | `americandruggis29` L26436-26438; `redcrossnotes00` L40583 | Medium (L2) |
| Demand | a category whose surgical-cotton consumption the firm's own print puts at ~200 lb (1886) → ~3,000,000 lb (1898); institutional reach claimed at 370,000 government packets and 7,000+ cabinets | `redcrossnotes01` L4666-4671; `johnsonsfirstai…` L2397, L2464 | Low–Medium, **all L1 except the 1896 building** (U.007) |
| Distribution | a city-salesman network named in five markets 1896–1904; druggist retail route; direct-to-customer invitation when the druggist is dry; own printing press and monthly house organ | `americandruggis01` L67215, L6972; `johnsonsfirstai…` L2405-2406; `redcrossnotes00` L40401 | Medium |
| Money | **UNKNOWN at every level that matters** — no capital, revenue, profit, wage or dividend line exists anywhere in held bytes; the only outsider-printed amounts are a **tax claim ($40,800)** and a **personal gift ($100,000)** | `americandruggis13` L6217; `americandruggis29` L69118 | High (of the absence) |
| People | one office printed (President / Manufacturing Chemist, 1893-or-later) and one plural family form ("The Johnsons", "Messrs. Johnson & Johnson"); **no founder**; **no brothers as a set**; an anonymous first-person narrator | `belladonna…` L184-185; `redcrossnotes01` L5748; `redcrossnotes00` L40603 | High (of what the print says and omits) |
| Failure | an adverse tax determination under protest and litigation; a competitor's imitation of its packaging; a broken price structure by 1904; **no established first failure** | as §M | Medium |
| What was still open at the close | whether the 1887 corporate leg was the registrant's ancestor; whether the combine's collapse cut its margin; whether the government channel continued; what any of it was worth | — | UNKNOWN by design (§S) |

### R.2 The stage's four beats, scored honestly against the §7 definition

* **Origin** — documented as a **range in a retrospective**, not an event with a document (§Boundary 1). Beat:
  **attested once, by the subject, late.**
* **First real experiment** — documented as a **process and a priced catalogue**, undated, in a layer whose own
  date is contested (§D.1 #3). Beat: **reconstructed, not dated.**
* **Repeatable validation** — the strongest beat here, and its strength comes from **L2**: 1896 capacity,
  1902–04 branch and salesman network, 1902 litigation in its own name, 1904 inclusion in a four-firm price
  structure. Beat: **witnessed by outsiders at four separate dated points.**
* **Scalable company formation** — the 1887 corporate sentence plus a named factory estate and a national
  sales organisation. Beat: **half-witnessed**: the *scale* is outsider-printed, the *formation* is
  self-printed, and the legal instrument connecting them **is not held anywhere**.

**Anti-hagiography check (§2):** this dossier would read the same if the firm had failed in 1906. It names a
broken price ring (§I), an adverse tax finding and a copycat (§M), no financial record at all (§K), and one
company's own retrospective as the only source for its beginning (§Boundary). Nothing in it treats survival
as demonstrated by 1904 — **the 1904 carriers show a firm that had reached scale, not one that had secured
it.**

<!-- NEXT: S, T, U -->

## S

STATUS: WRITTEN 2026-10-07

### S.1 Data gaps, each with the route that could close it

| # | Gap | Why missing | Importance | Best available evidence | Confidence | Follow-up task |
|---|---|---|---|---|---|---|
| G-1 | **Any 1886–1895 carrier at all**, contemporaneous with the narrated origin | the archive holds 5 of 795 American Druggist items (earliest volume on disk is 1896) and **0 of 44** *Pharmaceutical Era* items, which include the founding decade | **High** | the 1904 retrospective placement ("In 1887 he engaged with Johnson & Johnson"), the 1896 outsider factory report | Low that the origin year can be fixed from what is on this machine | `ia_text.py mine` on `title:("Pharmaceutical Era") AND mediatype:texts AND YEAR:[1886 TO 1895]`, dest `sources/periodicals/` (FETCH REQUEST FR-1) |
| G-2 | **The instrument of origination**: NJ charter, partnership article, or 1887 incorporation record | no tool in `tools/` reaches New Jersey state records; nothing in EDGAR predates 1994 | **High** | only the sentence "in 1887 they became a corporation" (`redcrossnotes01` L5718) and the printed form "Corporation" (1893+) | **UNKNOWN** | a route must be **built**, not run: no command exists; record as tooling debt (UNTRIED U7) |
| G-3 | **Any financial figure** — capital, revenue, profit, wages, dividend | a private 19th-century manufacturer published no accounts and none were digitised here | **High** | catalogue prices only (§P Q07–Q11) | **UNKNOWN** | corporate_print family: a J&J prospectus or report pre-1920 via `periodical_harvest.py --family corporate_print --company jnj` (FR-2) |
| G-4 | **The first customer / first institutional purchase** | house print names categories, never buyers; trade print names salesmen, never purchases | **High** | the 1901 Army-and-Navy sentence and "railroad systems / boards of Education" (unnamed) | **UNKNOWN** | Druggist correspondence columns 1896–1910 (FR-1 covers the route); no ordnance-record tool exists |
| G-5 | **Date of the New York → New Brunswick move** and of the 23-vs-25 Cedar Street change | the only layer with the New York imprint has three candidate dates (U.004) | Medium | `modernmethods…` L96/L1402/L3228; `redcrossnotes00` L6741 | **UNKNOWN** | re-OCR the cover/call-number pages of `modernmethodsofa00john` (FR-3) |
| G-6 | **Outcome of the two legal matters** — the Red Cross imitation suit and the $40,800 stamp-tax suits | company print gives the complaint; trade print gives the notice; no court record is held | Medium | `redcrossnotes00` L49975-50010; `americandruggis13` L6215-6226 | **UNKNOWN** (that they exist is FACT) | a New Jersey / federal court record route — no tool; UNTRIED |
| G-7 | **Any incurred failure of the firm** | 99% of the searchable periodical corpus is unopened; negatives of this era live in enforcement notices and assignment columns | **High** | the adverse tax finding and the broken price ring (§M) | **UNKNOWN** | FR-1 plus a faceted full-text pass for `recall/seizure/condemnation` **with entity adjacency** |
| G-8 | **Any rejected option or internal deliberation** | nothing of the kind was ever printed | **High** (it is the §2 record-selection null) | the firm's one retrospective statement of an alternative it says it refused | **UNKNOWN** | unclosable from this archive; state it and move on |
| G-9 | **Whether `Earle Dickson`, Band-Aid, Listerine or the three brothers belong to this window at all** | 0 lines each in held bytes; the held window is 1886–1904 print and Band-Aid is a 1920–21 product (`(PB)`) | Medium | measured absences (§Header, §B.1) | **UNKNOWN**, and 0 of 795 later Druggist items opened | FR-1 extended to 1920–1935 with `Dickson` + `New Brunswick` adjacency |

**Nothing in §S is reported as empty because it was not attempted.** TRIED–ANSWERED nulls, UNANSWERED routes
and UNTRIED doors are separated in the five-family report and in `## Untried` below, per §15 rule 5.

## T

STATUS: WRITTEN 2026-10-07

### T.1 Source / provenance table

`Conf` is capped at Medium throughout the L1/L2 print rows: every sidecar on every one of these files reads
`"transport": "UNVERIFIED TLS -- re-check before citing at High confidence"` (§Header). Access dates are the
sidecar `fetched` values. **`source_id` values are dossier-local; the merge mints globals centrally.**

| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| **P1S01** `redcrossnotes00johngoog` — *Red Cross Notes*, bound leg `1897-1898 and 1899-1900` (L72) | company house print, 1,311,274 B, **246 namings** | Primary (self-narrative) | 1886-\*87 claimed; 1899 suit; 1897-1900 print | 1897–1900 | archive.org/download/redcrossnotes00johngoog/…_djvu.txt | 1 | Medium |
| **P1S02** `redcrossnotes01johngoog` — same series, later leg; in-bytes copyrights **1914 / 1915 / 1919**; 831,850 B, **258 namings** | company house print | Primary (self-narrative, quoting P1S01's series) | 1886/1887 claimed | **UNCONFIRMED** (≥1919) | …/redcrossnotes01johngoog/… | 1 | Medium; date U.006 |
| **P1S03** `johnsonsfirstai00unkngoog` — *Johnson's First Aid Manual*; 316,901 B, 23 namings; `1903` at L89, `OopyrlRht, 1901, by JohriHon k Johnson` at L158 | company manual | Primary | 1898/1901 claims | 1901 (copyright leg) | …/johnsonsfirstai00unkngoog/… | 1 | Medium |
| **P1S04** `asepsissecunduma00john` — title page `JOHNSON & JOHNSON / ASEPTIC LABORATORIES / NEW BRUNSWICK, NEW JERSEY / 1897 / COPYRIGHT, 1897`; 60,103 B, 10 namings | company manual | Primary | 1897 | **1897, self-printed** | …/asepsissecunduma00john/… | 1 | Medium-High (own date) |
| **P1S05** `modernmethodsofa00john` — "Modern Methods of Antiseptic Wound Treatment"; 131,924 B, 16 namings; NY imprint, price lists, suture line | company pamphlet | Primary | 1880s | **UNCONFIRMED**: metadata 1888, call number "1891", own citations reach Feb 1888 | …/modernmethodsofa00john/… | 1 | Low–Medium (U.004) |
| **P1S05b** `americandruggis01unkngoog` — Vol **XLI, July to December 1902** (L74); 3,348,636 B, 11 namings | third-party trade periodical | Secondary but **independent origin** | 1902 office opening | 1902 | …/americandruggis01unkngoog/… | 1 (trade) | Medium |
| **P1S06** `americandruggis07unkngoog` — Vol **XXVIII, January to June 1896** (L94); 3,440,679 B, 11 namings | third-party trade periodical | Independent | 1896 factory addition; 1896 Red Cross incorporator list | 1896 | …/americandruggis07unkngoog/… | 1 (trade) | Medium |
| **P1S07** `americandruggis13unkngoog` — Vol **XL, January to July 1902** (L88-99); 2,749,231 B, 7 namings | third-party trade periodical | Independent | 1902 stamp-tax suits | 1902 | …/americandruggis13unkngoog/… | 1 (trade) | Medium |
| **P1S08** `americandruggis26unkngoog` — Vol **XLIV, January to June 1904** (L98); 3,004,067 B, 9 namings | third-party trade periodical | Independent | 1904 "manufacturing firm" | 1904 | …/americandruggis26unkngoog/… | 1 (trade) | Medium |
| **P1S09** `americandruggis29unkngoog` — Vol **XLV, July to December 1904** (L111); 3,290,185 B, 19 namings | third-party trade periodical | Independent | 1887 employment claim; 1904 combine; 1904 marriage | 1904 | …/americandruggis29unkngoog/… | 1 (trade) | Medium |
| **P1S10** `belladonnaastud00incgoog` — multi-author belladonna volume; 200,699 B, 8 namings; contributor line L184-185; footnote L2431-2435 | professional volume containing a firm contribution | **Mixed**: the volume is third-party, the plaster footnote is the author's own | ≥1893 | year UNCONFIRMED (probe asserted 1894; sidecar carries none) | …/belladonnaastud00incgoog/… | 1 | Medium |
| **P1S11** `bub_gb_A9IAAAAAYAAJ` — 3,585,302 B, **1 naming**; `alphabetfirstth00goog` — 741,218 B, **0 namings, 126 "New Brunswick"**; `ErnestFairfield` — 262,991 B, **0 namings**, "1888." | noise/negative-control layers | n/a | n/a | 1888 / 1897 / unverified | as above | 3 | High **as controls**: they are kept to prove the adjacency rule, not cited as evidence |
| **P1S12** `John0851_1970` — 1970 annual report, 33,583 B, **23 namings**, 0 occurrences of "1886"; fetched **2026-10-06** | company annual report | Primary, **(PB)** | 1970 | 1970 | …/John0851_1970/… | 1 | Medium; **late arrival, §Header; harvest index calls this layer NULL (U.011)** |
| **P1S13** EDGAR submissions index — `sources/_index/submissions.csv` + `_CIK0000200406.csv` (744,798 B JSON pair) | regulatory index | Primary (metadata) | — | built 2026-09-29 | sec.gov submissions API, CIK 0000200406 | 1 | **High**: re-measured this pass — **3,371 rows, earliest 1994-03-10, latest 2026-09-10, 65 forms, 0 forms beginning `S-1`, 0 rows ≤ 1960-12-31, 134 rows with no `primaryDocument`**. Duplicate generic/CIK-keyed pair = RD-098 corruption vector |
| **P1S14** `sources/sec/` — **26 bodies, 4,671,102 B**, accessions 0000950110-94-000059 → 0000950123-99-006049, plus `_UNANSWERED.csv`, `_SKIPPED.csv`, `_RUN.json` (window `1960-12-31..2006-12-31`, attempted 149, stored 26, guard ok) | SEC filing bodies | Primary, **all `(PB)`** | — | 1994–1999 | sec.gov | 1 | High; **`1886` occurs 0 times in them**; arrived 2026-09-30, after the probe (U.008) |
| **P1S15** `tools/web_domains.json` | tool ledger | n/a | — | read 2026-10-07 | local | n/a | **High that no `jnj` slug exists in it** → scripted family (b) is **UNTRIED**, whatever the probe's ad-hoc CDX floor measured |

### T.2 Provenance findings that bind the merge

1. **Two lineages, not fourteen files.** P1S01–P1S05/P1S10 are **one publisher**; the 1896–1904 Druggist
   volumes are **one publication**. Counting corroboration across P1S01 and P1S02 (vol 01 abstracts vol 00's
   own series, L5737-5740) is forbidden by §3 and `independence_note` says so on every row.
2. **Item-level dates come from the printed volume legs, not from metadata** (P1S05b–P1S09). Every sidecar
   carries `identifier,url,fetched,bytes,route,note,transport` and **no year at all** — which is why the probe
   could assert "1910" and "1888" and why this volume had to read title pages to date anything (U.004, U.006).
3. **Locators are labels, not addresses** (§14 rule 12). Line numbers in §T/§U/§P are this pass's re-reads of
   the files on disk; where they differ from the probe's, the difference is registered (U.009), not silently
   corrected.
4. **Negative artefacts are held on purpose:** the two zero-naming layers (P1S11) and the 24 "issued"-false-
   positive lines of §M's loose sweep are retained so no later pass reads an absence as a null about history.

## U

STATUS: WRITTEN 2026-10-07

*Conflicting evidence, §7 format. Every anchor below is registered 1:1 in the `conflicts` block at the end of
this volume; no conflict is registered without its anchor, and no anchor is declared without a row.*

### U.001 — Is the origin a two-year range or the single year 1886?
*CLAIM A:* "1886-\*87 (the date of the formation of the firm of Johnson & Johnson)" — `redcrossnotes00`
L9283-9285, printed 1897–1900. *CLAIM B:* "Johnson & Johnson **began in business in 1886**" / "They entered
into business in 1886" — `redcrossnotes01` L5717-5718, L4652-4653, printed ≥1919. *WHY THEY DIFFER:* the same
publisher, twice; the second telling **drops the range** and asserts the earlier single year, 32+ years after
the event, in a volume whose own date is unconfirmed. *EVIDENCE WEIGHT:* **equal and identical** — both are
L1, so neither can corroborate the other; the range is the **earlier** form and the single year the **later**.
*BEST-SUPPORTED INTERPRETATION:* write the origin as **a range inside a retrospective**, and write the
collapse of that range into "1886" as a **property of the company's self-narrative**, not as new evidence.
The only independent datum, the 1904 obituary placing a salesman with the firm **in 1887**, supports the
*later* year of the range. *RESIDUAL UNCERTAINTY:* total as to the year; complete as to month and day.
*CONFIDENCE:* **Medium** in the finding (that the record is a range-in-a-retrospective, High); **Low** in any
single year.

### U.002 — Does a corporate-formation statement exist, or was the incorporation question "not found"?
*CLAIM A* (probe §5.1, inherited): "tested directly and **not found** … 0 lines … The incorporation question
stays OPEN, and no NJ charter is in the corpus." *CLAIM B* (this pass): *"in 1887 they became a corporation"*
— `redcrossnotes01` L5718, plus "President Johnson & Johnson **Corporation**" (1893+) and "which **corporation**
petitions the court" (1897–1900). *WHY THEY DIFFER:* the probe's regex demanded the entity string and the
word "incorporat" **on one line within 60 characters**; the held sentence breaks across a line in two-column
OCR. I reproduced the probe's **0** exactly and then found the statement by searching the verb phrase instead
of the adjacency. *EVIDENCE WEIGHT:* the bytes outrank the regex — **A is superseded as to "not found"; A
stands in full as to "no NJ charter is in the corpus."** *BEST-SUPPORTED INTERPRETATION:* a **corporate leg is
asserted by the company in 1887**, single-lineage and retrospective; **no instrument establishes it**, and no
held document connects that corporation to CIK 200406. *RESIDUAL UNCERTAINTY:* which state, which persons,
what capital, whether the 1886 firm and the 1887 corporation are the same legal person at all.
*CONFIDENCE:* **High** that the sentence exists and that no charter exists; **Low** in the leg itself.

### U.003 — Where was the firm, at the start?
*CLAIM A:* a **New York** imprint — "Published by JOHNSON & JOHNSON, New York." / "25 Cedar Street, New
York." / "PRICE LIST— JOHNSON & JOHNSON— NEW YORK", with **0 New Brunswick lines in the whole layer**.
*CLAIM B:* a **New Brunswick, N. J.** factory — "to visit our factory at New Brunswick" (L6741), "Messrs.
Johnson & Johnson, New Brunswick, N. J." (L12771), and the outsider's 1896 "their factory at New Brunswick,
N. J." *WHY THEY DIFFER:* not a contradiction but a **sequence with no dated hinge**, complicated by the same
early layer also printing **"23 Cedar St."** in a Papoid advertisement. *EVIDENCE WEIGHT:* B is witnessed by
**both** lineages (1896 L2 + 1897–1900 L1); A by one lineage whose date is contested. *BEST-SUPPORTED
INTERPRETATION:* a New York publishing/selling house printed first, a New Brunswick works named by 1896, and
**the move is UNDATED in this corpus**. *RESIDUAL UNCERTAINTY:* whether the two Cedar Street numbers are an
error, a move within New York, or two imprints; whether New York was the firm's seat at all in 1886.
*CONFIDENCE:* Medium.

### U.004 — What year is `modernmethodsofa00john`?
*CLAIM A:* **1888** (catalogue metadata, per the probe). *CLAIM B:* **"1891"** — the library call number
`RD131 J63 / 1891 … RD 131 J63 1891 C.I` (L3403-3414). *CLAIM C (this pass):* the layer's **own text cites
work dated "Feb., 1888"** (L2445) and repeatedly 1887, giving a **terminus post quem of Feb 1888** and no
terminus ante quem at all. *WHY THEY DIFFER:* metadata is a catalogue record, the call number is a later
library stamp, and the contents are the only in-document evidence. *EVIDENCE WEIGHT:* **C outranks both
labels** — it is the document speaking — while proving nothing about the *layer's* printing year. *A side the
probe did not test:* this layer contains **0** lines with "New Brunswick", so if 1891 were right the New
York/New Brunswick sequence (U.003) shifts by three years. *BEST-SUPPORTED INTERPRETATION:* **date
UNCONFIRMED, ≥1888-02**, cited only as "the earliest company print", never as an 1886–88 first experiment.
*RESIDUAL UNCERTAINTY:* the whole thing; a re-OCR of the cover is the remedy (FR-3). *CONFIDENCE:* High that
it is unresolved.

### U.005 — Founder vs role vs family plurality
*CLAIM A* (dispatch premise): three brothers founded the firm. *CLAIM B* (held bytes): **no** held line
calls anyone a founder (three separate tests, §B.2), **no** line names three brothers, **no** line names
`James Wood` or `Miles Stone`; one **office** is printed (RWJ, Manufacturing Chemist, President), the origin
is otherwise attributed to **"the firm"** and to a plural **"The Johnsons"/"Messrs. Johnson & Johnson"**, and
the nearest first-person account is **anonymous**. *WHY THEY DIFFER:* A is the modern company story; B is
what the 1886–1904 print actually contains, and the brothers' story needs a carrier from a later decade that
this corpus does not hold. *EVIDENCE WEIGHT:* **B, on the held bytes; A has zero carriers here** — and B
cannot be read as disproving A, only as failing to support it. *BEST-SUPPORTED INTERPRETATION:* **roles, not
founders**; keep the three brothers as a **claim with no in-window carrier**, and never write "founder" for
a man the print calls "President". *RESIDUAL UNCERTAINTY:* who originated the firm is UNKNOWN; G-1/G-2 are
the routes. *CONFIDENCE:* High in the finding; Low in any person-level statement.

### U.006 — Is the second house-print volume 1910?
*CLAIM A:* the probe's table: `redcrossnotes01johngoog | 1910`. *CLAIM B:* the layer's own in-bytes copyright
legs **"COPYRIGHT 1914 BY JOHNSON & JOHNSON"**, **1915**, **1919 ×2**; its only full date stamps are **1917 ×2**;
its first 120 lines carry **no** volume-year leg at all. *WHY THEY DIFFER:* the probe's "1910" is not carried
by any byte I can find. *EVIDENCE WEIGHT:* **B** — printed copyright legs beat a dossier label. *BEST-
SUPPORTED INTERPRETATION:* the volume is **≥1919**, so the founding and corporate sentences it carries are
**33+ years** after the event rather than 24, and the "1910" date must not be inherited. *RESIDUAL
UNCERTAINTY:* an exact bound date; whether earlier issues are bound into the same volume. *CONFIDENCE:* High
that 1910 is unsupported.

### U.007 — Are the adoption and status figures evidence, or one company's self-report?
*CLAIM A:* 370,000 government packets; "upwards of seven thousand" cabinets; adoption by "several of our chief
Railroad Systems" and by Boards of Education; "pioneers and leaders"; the method "incorporated into the 16th
edition of the United States Dispensatory"; "consumption … six to ten million pounds". *CLAIM B:* the
independent print gives **no** count of any of these — it gives a factory addition (1896), a city-salesman
network (1896–1904), a branch opening (1902), a tax suit (1902) and a four-firm price ring (1904).
*WHY THEY DIFFER:* A is **advertising and house print**; B is **trade journalism**, which in this era reports
what firms *do* rather than what they *sell*. *EVIDENCE WEIGHT:* A is single-lineage and unverifiable here
(the Dispensatory itself is **not held**; the cabinet count has **no denominator**); B is multi-dated and
independent but silent on volume. *BEST-SUPPORTED INTERPRETATION:* the validation beat rests on **B**, and
A's numbers are recorded in the registers with `evidence_class` RETROSPECTIVE/self-claim, `confidence` capped,
and `independence_note` = `one lineage (company house print); L2 silent`. **No arithmetic may combine A's
counts with A's prices** (§E.2). *RESIDUAL UNCERTAINTY:* every magnitude in the stage. *CONFIDENCE:* High in
the treatment; the figures themselves stay Low–Medium/UNKNOWN.

### U.008 — Did this company have any SEC document bytes at all?
*CLAIM A* (probe §2): "**SEC document bytes held: 0.** Only the index exists; no accession body was fetched."
*CLAIM B* (this pass): `sources/sec/` holds **26 filing bodies, 4,671,102 B**, accessions 1994-03-10 → 1999,
plus `_RUN.json` (attempted 149, stored 26) and `_UNANSWERED.csv` / `_SKIPPED.csv`. *WHY THEY DIFFER:* the
bodies arrived **2026-09-30**, the day after the probe. *EVIDENCE WEIGHT:* **B**, by enumeration
(§14 rule 11). *BEST-SUPPORTED INTERPRETATION:* **the tier does not move.** All 26 bodies are `(PB)`; family
(a) is still an in-window **NULL** (0 of 3,371 rows ≤ 1960-12-31, re-measured); Stage 1 still has **two**
families returning in-window Tier-1 text, so **T2 core — PROVISIONAL** stands. What changes is that the
probe's inventory is stale and its §7 harvest-block reasoning ("no accession body") no longer describes the
directory. *RESIDUAL UNCERTAINTY:* the 22 unanswered/skipped slots are UNANSWERED, not null. *CONFIDENCE:*
High.

### U.009 — Whose line numbers are they?
*CLAIM A* (probe §3(c)): `americandruggis29` l.36865 and l.25490 as held naming lines. *CLAIM B* (this pass):
those two passages are at `americandruggis**07**` L36865 and L25490; a29's own naming lines are elsewhere
(L33894, L26436, L69115, L4868, L13001). *WHY THEY DIFFER:* a layer/column mix-up in inherited notes.
*EVIDENCE WEIGHT:* the bytes, re-read twice. *BEST-SUPPORTED INTERPRETATION:* **this volume's locators are
canonical for its own citations**, and the probe's are cited only as its own record. *RESIDUAL UNCERTAINTY:*
any other pass that quoted the probe's locators. *CONFIDENCE:* High.

### U.010 — Is that "Robert Wood Johnson" a Johnson & Johnson line?
*CLAIM A* (probe §3(c)): `americandruggis07` l.45597 — "Robert Wood Johnson. The objects of" — filed under
**"Held in-window naming lines"**. *CLAIM B* (this pass): the passage reads *"the New York Red Cross has been
incorporated. Among the incorporators are Mrs. Charles H. Raymond … Robert Wood Johnson. The objects of the
Red Cross, as stated in its certificate of incorporation, are: To establish a corps of physicians, surgeons,
and nurses…"* and **no entity naming occurs within ±25 lines**. *WHY THEY DIFFER:* the line names a **person**,
not the registrant, in a **charity** context, in a corpus where the company's own organ and cotton are branded
**Red Cross**. *EVIDENCE WEIGHT:* **B** — the adjacency rule in §Header decides. *BEST-SUPPORTED
INTERPRETATION:* it is a real 1896 personal record for a man of that name and a useful lead on his civic
network, **not** a founding or naming carrier; it may be cited only as "a Robert Wood Johnson among the
incorporators of the New York Red Cross, 1896", never as J&J print. *RESIDUAL UNCERTAINTY:* whether the two
men (1894 President; 1896 incorporator) are one person — plausible, unestablished. *CONFIDENCE:* High that
the probe's classification is wrong.

### U.011 — Is the 1970 layer a NULL?
*CLAIM A* (`research/A4_harvest_mine.md`): `John0851_1970` — 33,583 B, **0 word hits, 0 entity hits**,
verdict **NULL**. *CLAIM B:* its bytes carry **23 lines** matching the entity pattern and it is a
**company-authored 1970 annual report** ("1970 ANNUAL REPORT", L7; 23 "Johnson & Johnson" lines; 5 "New
Brunswick" lines, 4 with N. J.). *WHY THEY DIFFER:* the harvester's matcher is term-list and case-bound; the
item's own OCR header reads `Gohmson=folon`, so a naming can be present in the body and invisible to the
promoted-by column. *EVIDENCE WEIGHT:* **B** — RD-124's own rule, a label is checkable, not trusted. *BEST-
SUPPORTED INTERPRETATION:* the harvest index under-reports namings for this slug and its **NULL counts cannot
be used to bound coverage**; and the item remains **(PB)** for Stage 1 in any case — where it *is* load-
bearing is that **the earliest company annual report on disk prints no founding year at all** (0 occurrences
of "1886"). *RESIDUAL UNCERTAINTY:* how many of the 12 "UNANSWERED" harvest rows are actually answerable.
*CONFIDENCE:* High.

### U.012 — Was the 1886–1904 record "rich" or is richness an artefact of what survived?
*CLAIM A:* the probe's framing that this window holds more in-window company voice than Walmart or Target
(494 naming lines in two volumes). *CLAIM B:* those 494 lines are **one publisher's own periodical**, and the
independent record for the founding decade is **0 lines** (the earliest L2 volume on disk is 1896; 1887
*Pharmaceutical Era* items exist but were never fetched). *WHY THEY DIFFER:* A counts lines, B counts
**independent origins**. *EVIDENCE WEIGHT:* both are true and they measure different things — which is the
tier's actual problem: **§15.2 counts families, and a family that is 99% unopened is not a family that
answered.** *BEST-SUPPORTED INTERPRETATION:* keep **T2 core — PROVISIONAL**, and keep the reason the tier is
provisional attached to every merge of this company: two families returned, one of them almost unopened, the
richest family being self-narrative. *RESIDUAL UNCERTAINTY:* whether FR-1 produces a contemporaneous
third-party founding witness, which would harden (c) and could move the tier. *CONFIDENCE:* High in the
statement; the tier itself stays provisional.

<!-- NEXT: registers -->

## Register rows for merge — APPLIED TO THE NINE CSVs (merge pass, 2026-10-07)

The part's nine fenced `csv` register blocks (**102 rows**) are register data, not narrative (method §13).
They were **applied** to the nine CSVs at this directory root; the full requested↔applied accounting, the
header-conformity check, the duplicate-key pass and the provisional-to-global id map are in the **MERGE
RECORD** at the top of this volume. **No row was folded, trimmed or renumbered** and `source_id` values in
the CSVs now carry minted globals **S4463–S4478**; the prose above and below keeps the author's dossier-local
`P1Sxx` tags, bound by that map. The verbatim block text survives read-only at `_parts/s1_p1.md` l.1304–l.1474.
Claim records are narrative and are **not** moved: all **23** load-bearing records (T2 tier, §15.2) stay inline
in §A.3, §B.5, §D.3, §F.3, §G.3, §I.3, §K.3, §L.3 and §M.3 above.

## registers-part-2

STATUS: WRITTEN 2026-10-07

**Rows emitted, per register (the merge applies 101 rows in total from this volume):**
`sources` **16** · `quantitative` **21** · `timeline` **18** · `decisions` **8** · `validation` **7** ·
`failures` **5** · `channels` **4** · `conflicts` **12** · `data_gaps` **11**.
**Rows withheld on purpose:** none from the nine registers, but (i) no `sources` row was emitted for any of
the noise items beyond P1S11's single control row, because a row per noise file would inflate the register
with carriers that name nobody; (ii) no quantitative row was emitted for the `1886` occurrences in
`alphabetfirstth00goog` or any other zero-naming layer — those are 163 lines of unrelated Canadian and
American history and are **evidence of nothing about this company**; (iii) the harvest index's 12 candidate
rows (`research/A4_harvest_mine.md`) are **not** emitted as sources rows — a `TIER1_CANDIDATE` label or a
NULL stamp is never a source (§3), and one of its NULL verdicts is now contradicted by bytes (U.011).
**Every §U anchor U.001–U.012 is written in the narrative above and has exactly one conflicts row: 12 and
12, 1:1 parity.** Claim records for load-bearing claims: **A 4 · B 4 · D 3 · F 2 · G 1 · I 2 · K 1 · L 3 ·
M 3 = 23 records**, one per fenced block in the sections (T2 tier records load-bearing claims only, §15.2);
sections C, E, H, J, N, O, P, Q, R, S, T, U are answered in tables and prose with their evidence carried on
the register rows rather than duplicated as records.

## FIVE FAMILIES, AS MEASURED ON THIS PASS

| Family | In-window state | Verdict class |
|---|---|---|
| **(a) Filings** | 3,371 rows enumerated and **re-measured this pass** (earliest 1994-03-10, latest 2026-09-10, 65 forms, **0 forms beginning `S-1`, 0 rows ≤ 1960-12-31**); 26 filing bodies now on disk (4,671,102 B) but **every one `(PB)`**; `1886` occurs **0 times** in them | **TRIED–ANSWERED — documented in-window NULL** (route answered, so the zero is a statement about the record). Unanswered sub-slice: 134 rows with no `primaryDocument`, plus `_UNANSWERED.csv`/`_SKIPPED.csv` slots = UNANSWERED, not null |
| **(b) Web archives** | `tools/web_domains.json` contains **no `jnj` slug** (verified by grep this pass), so `tools/cdx_intake.py` has never been run for this company and writes an UNTRIED record for it. The probe's *ad-hoc* urllib CDX floor (www.jnj.com 1996-10-18; johnsonandjohnson.com 1998-01-26) is recorded as a **floor measurement, two URLs, not the archive** | **UNTRIED as a scripted family** (per the dispatch's rule, because no jnj domain is cited in `web_domains.json`); and in-window **impossible by construction** for the registrant's own domains — 36 years past the window's close |
| **(c) Periodical corpora** | 5 American Druggist volumes held and read (1896, 1902 ×2, 1904 ×2), **47 naming lines** with printed volume legs; **790 of 795 items unopened; 44 of 44 *Pharmaceutical Era* items unopened**; Chronicling America `CHALLENGED` on all 7 endpoint shapes | **TRIED–ANSWERED (in-window Tier-1 text returned)** + **UNTRIED** at 99% of the corpus + **UNANSWERED** for CA (never a null) |
| **(d) Digitised corporate print** | 6 company-authored layers read to the line: house organ ×2, 1897 manual, contested-date pamphlet, first-aid manual, belladonna contribution volume; **504 of the corpus's 642 namings**; plus the `(PB)` 1970 annual report | **TRIED–ANSWERED — the richest family, and it is self-narrative** (U.012) |
| **(e) Auction / museum documentary** | no tool: `tools/HARVEST_README.md` family 4 is *"(not implemented) … no read-only public API was verified"*; **no command exists to run**; one museum artefact exists repo-wide, at Walmart, never for jnj | **UNTRIED — has no tool** (a statement about us, not about the record). Highest-value unopened door for an 1886 company |

## Untried

*Per §15 rule 5: nothing below is a null. Each names the command or the missing tool.*

* **U1 — fleet harvest for jnj, the 8 written tasks never executed.** `python tools/periodical_harvest.py
  --company jnj` then `python tools/harvest_mine.py --company jnj --limit 20`. This is the cheapest way to
  convert the probe's provisional tier into a fleet-documented one.
* **U2 — the other 790 American Druggist items** (1890–1905 especially) and **all 44 *Pharmaceutical Era*
  items, including the 1887 volumes**: see FR-1. The founding decade itself is unopened print.
* **U3 — `Earle Dickson` / Band-Aid at item level** (full text never searched; metadata answered 0 for the
  phrase): `python tools/ia_text.py search --q '"Dickson" AND "New Brunswick" AND mediatype:texts AND
  YEAR:[1920 TO 1935]' --insecure`.
* **U4 — the New Jersey charter / Secretary of State record.** No command exists in `tools/`. **UNTRIED,
  no route**, and it is the only thing that can convert the 1887 corporate sentence into an instrument.
* **U5 — HathiTrust for the J&J phrase**: never measured for this slug; no body for the slug in the repo.
* **U6 — court records** for the two litigations held (the Red Cross equity bill; the $40,800 stamp-tax
  suits): no tool reaches them.
* **U7 — auction/museum documentary (family e)**: needs a tool, not an agent.
* **U8 — the TLS repair**: re-fetch all 15 layers over a verified CA store and re-stamp the sidecars; until
  then every row in this volume is capped at Medium by our transport, not by the record.
* **U9 — `cdx_intake.py` for a jnj domain**, which first requires a sourced domain string in
  `tools/web_domains.json` (a filing line or dossier line, never an invented name). `www.jnj.com` is printed
  inside the 1994+ SEC bodies on disk, so the provenance requirement is satisfiable by a script run.
* **U10 — the EDGAR document bodies 1994–1999 already fetched were never read for Stage-1 purposes beyond the
  `1886` count** (0 occurrences), and 22+ slots remain in `_SKIPPED.csv`/`_UNANSWERED.csv`: `(PB)` work for
  Stages 2–3, listed so nobody mistakes it for an in-window gap.

## FETCH REQUESTs

```
FETCH REQUEST: FR-1 — route `tools/ia_text.py mine` — query 'title:("Pharmaceutical Era") AND
mediatype:texts AND YEAR:[1886 TO 1895]' --pattern 'Johnson\s*&\s*Johnson|Johnson and Johnson|New Brunswick'
--company-dir founders_playbook/01_companies/company_045_jnj --rows 8 --max-mb 10 ; SECOND LEG same tool on
'title:("American Druggist") AND mediatype:texts AND YEAR:[1890 TO 1896]' with the same pattern — destination
`sources/periodicals/` with sidecars — purpose: obtain a CONTEMPORANEOUS third-party naming of the firm inside
the founding decade, which is the only thing that can test the 1886-*87 range against an outside witness and
harden family (c) from ad-hoc probe to fleet-documented. Not an agent task (§15.1: no agent brief may include
retrieval a script can reach). WEB BUDGET FOR THIS PASS USED: 0.
```
```
FETCH REQUEST: FR-2 — route `tools/periodical_harvest.py --family corporate_print --company jnj` (the block's
own `CP jnj annual/shareholder print 1886-1980` task, which the harvest ran as SKIPPED, never as answered) —
destination `sources/corporate_print/` with sidecars — purpose: any pre-1920 J&J shareholder or prospectus
print, which is the only class of document that could supply §K's missing capital, share and dividend series.
```
```
FETCH REQUEST: FR-3 — route `tools/ia_text.py` re-fetch of item `modernmethodsofa00john` — specifically the
cover / title / call-number pages — destination `sources/periodicals/` (replace by new sidecar, do not delete
the existing layer: protected archive) — purpose: settle **U.004** (1888 vs 1891 vs a Feb-1888 terminus post
quem), on which the dating of the earliest company print, the suture price list, and therefore the whole
first-experiment chronology depends.
```
```
FETCH REQUEST: FR-4 — route `tools/cdx_intake.py` AFTER a `jnj` entry with provenance is added to
`tools/web_domains.json` (the domain string is printed in the 1994+ SEC bodies under `sources/sec/`, so the
ledger's provenance rule is satisfiable) — window 1996-2004 — destination `sources/web_archive/` — purpose:
convert family (b) from UNTRIED to a measured state for Stages 2–3. Useless for Stage 1 and requested only
so the next stage does not inherit the same blank.
```

## What this pass refused to claim, and why

1. **That Johnson & Johnson was founded in 1886.** Refused: the strongest held statement is a **range inside a
   retrospective**, and the single-year form is the *later* telling of the same lineage (U.001).
2. **That any person founded it, or that three brothers exist in the record.** Refused: three separate
   measures return 0 (founder-word adjacency, brother adjacency, `three brothers`), `James Wood` and
   `Miles Stone` are 0-line names here, and a printed office is not an origin (U.005).
3. **That the 1887 corporation is the registrant's ancestor.** Refused: no charter, no instrument, and 0 rows
   in EDGAR before 1994-03-10 (U.002).
4. **That `redcrossnotes01` is a 1910 volume** (U.006) or that `modernmethodsofa00john` is 1888 (U.004) — both
   inherited labels contradicted or unsupported by the bytes.
5. **That `belladonnaastud00incgoog` is 1894.** Refused as a date: the sidecar carries no year and my own
   bound is only ≥1893 from its citations.
6. **That the 370,000 / 7,000 / Dispensatory-adoption figures are corroborated** (U.007), or that any of the
   §P prices may be multiplied by any §L count.
7. **That `americandruggis07` L45597 names this company** (U.010), that the `New Brunswick` place-name in the
   Canadian layer means anything (adjacency rule), or that Listerine/Band-Aid/Earle Dickson belong to this
   window (0 proprietor namings / 0 lines).
8. **That the harvest index's `NULL` on `John0851_1970` is a null** (U.011), or that any Chronicling America
   zero is a null (all 7 shapes CHALLENGED = UNANSWERED).
9. **That the tier should move.** Refused: I re-tiered nothing. Two families returned in-window Tier-1 text;
   the new SEC bodies are all `(PB)`; **T2 core — PROVISIONAL stands**, and the disagreement is logged here
   rather than enacted silently (U.008, U.012).

**What I did NOT examine:** I did not open any of the 26 SEC filing bodies beyond machine-counting them for
`1886`/`New Brunswick` (they are `(PB)`); I did not read the 790 unopened American Druggist items, the 44
*Pharmaceutical Era* items, any HathiTrust record, any auction or museum holding, or any court record; I did
not touch the EDGAR `_SKIPPED.csv` slots; I did not examine `00_universe/` for the company's universe
metadata; and I did not read Amazon's content beyond the §7/§13 shapes, which are format, never data.

*End of part 1. Conflicts referenced but unresolved here live at `(J&J S1 §U, part_1)` — anchors U.001–U.012,
all written in this volume.* **Path owned by this pass: `founders_playbook/01_companies/company_045_jnj/_parts/
s1_p1.md`; log at `_parts/NOTES_jnj_p1.md`; gate at `03_quality_control/jnj_s1_gates_p1.md`.** No other file
on this company was created, modified or deleted by this pass, and nothing under `sources/` was touched.
