# NVIDIA — Stage 1 (1993 inception – 1999 IPO) — merged volume

**Merged file, one volume.** Assembled by the Stage-1 merge pass on 2026-09-30 (agent `nvidia-s1-merge`) from
`_parts/s1_p1.md` (Header, Boundary, §A–§F, claim records `P1-01`–`P1-27`, 91 emitted register rows) and
`_parts/s1_p2.md` (§G–§U, claim records `P1-28`–`P1-60`, 101 emitted register rows, the §U anchor block and the
eleven-route `## Untried` list). Section letters, claim numbers and conflict numbers run continuously and are
**not renumbered**; each part body below is carried in full, in part order, cut at section boundaries. Nothing
was trimmed, summarised or reordered. The two `_parts/` files stay on disk as emitted and are read-only apart
from the `SUPERSEDED 2026-09-30` footers this merge was authorised to append. Word and byte counts of every
file are in `_MANIFEST.md`; the volume index, anchor map and register arithmetic are in `stage_1_index.md`.

## Stage 1 merge note

**Tier and budget.** Nvidia is **T3 register** (§15.2). The probe (`research/A_chronology_feasibility.md`)
found in-window Tier-1 text in **one of five families** — (a) filings; (b) web archives is UNANSWERED (six CDX
requests, HTTP 503/504, zero bodies, `sources/wayback/` empty); (c) periodicals is LEAD_ONLY (17 scripted
tasks, 145 candidate rows, no body read; HathiTrust status 0, Chronicling America 403); (d) digitised corporate
print is NULL in-window (the one entity-bearing item holds FY2005–FY2026 layers and a 16-byte container); (e)
documentary is UNTRIED. `research/A3_intake_regrade.md` re-confirmed the verdict on 31 stored documents
(7,942,444 B) and **did not re-issue it**, so this pass inherits T3 and runs `gates.py --tier register`. The
tier cap is 8,000 words per stage and the carried bodies are far larger, because both parts were dispatched at
exemplar density against a T3 verdict. Per RD-122 and §9.6 that is a dispatch-budget overshoot, not an evidence
defect: **nothing is trimmed to quiet a gate and nothing is re-tiered on word count.** Against §9.2 file
geometry the merged volume sits in the amber 40,000–60,000 band, which is explicitly allowed to finish the
stage as one file, so no §9.3 split was made and none is owed. The probe T2 upgrade condition — one
browser-egress Wayback CDX answer **and** one in-window periodical body read — remains untested, so the tier is
not lifted and the ceiling is still unmeasured.

**Coverage limit — part 1 is truncated, and that is not a clean merge.** `_parts/s1_p1.md` ends after its own
register row-count footer with a horizontal rule and a single stray `#`, the first keystroke of a heading never
written. Its assigned scope (Header, Boundary 1–7, §A–§F, eight register blocks) is complete, and no table or
paragraph is cut mid-way, which is why the merge can carry it verbatim. What is **absent** is the `## Untried`
block part 1 promises at L123, L459, L523, L590 and L639 and which its emitted rows cite by item number
(`UNTRIED-1`, `UNTRIED-3/4/5/6`, `UNTRIED-7`, item 10 — eight `data_gaps.csv` follow-up cells and conflict
`P1K07`). Part 1 also planned a third volume (`p3 = Q–U + appendix`) that was never dispatched; part 2 took
§G–§U, so no narrative section is missing, but the separate claim-record appendix never exists — records are
inline per section in both parts. **This merge did not reconstruct the unwritten block.** Part 2 eleven-route
`## Untried` is carried forward as the volume register of untried routes and re-numbers them with part 1 item
numbers in parentheses; the missing part-1 numbering is recorded as COR-03 in `CORRECTIONS.md`, in
`_MANIFEST.md`, in `03_quality_control/nvidia_s1_merge_notes.md`, and as a `data_gaps.csv` row minted here.

**Id minting (central: `tools/id_mint.py --count 16 --company company_016_nvidia --claim --agent
nvidia-s1-merge`).** The block **S4353–S4368** is claimed in `00_universe/_ID_BLOCKS.tsv` for this company,
allocated above the highest live id and never into a gap. A four-digit token in the parts is **not**
automatically an id — the corpus already carries an OCR price that reads like one (RD-131), and no such token
was minted here. The parts used dossier-local carrier ids; the alias table is:
`P1S01`→`S4353` (S-1, filed 1998-03-06) · `P1S02`→`S4354` (S-1/A No. 5, 1998-12-23) · `P1S03`→`S4355` (424B4
final prospectus) · `P1S04`→`S4356` (FY1999 10-K405) · `P1S05`→`S4357` (EDGAR submissions index) ·
`P1S06`→`S4358` (stored-document manifest census) · `P1S07`→`S4359` (harvest-mine dossier, part 1 read) ·
`P1S08`→`S4360` (S-1/A No. 1) · `P1S09`→`S4361` (No. 2) · `P1S10`→`S4362` (No. 3) · `P1S11`→`S4363` (No. 4,
the great revision) · `P1S12`→`S4364` (No. 5, 1999-01-13) · `P1S13`→`S4365` (No. 6, 1999-01-20) ·
`P1S14`→`S4366` (Creative/CTI Schedule 13G) · `P1S15`→`S4367` (six blank-primaryDocument index rows) ·
`P1S16`→`S4368` (harvest-mine dossier, part 2 read).
Every citation cell in all nine registers was re-pointed to the global id. The local ids inside part 1 and part
2 prose are left untouched — a protected emission is not rewritten to satisfy a key — and they resolve through
this table and through the `notes` alias printed on each `sources.csv` row. Claim tags (`P1-nn`), gap tags
(`P1Gnn`) and conflict tags (`P1Knn`) are dossier-local labels, not global ids, and stay exactly as emitted.

**Register arithmetic.** 192 rows emitted (91 + 101) → **192 carried, 0 dropped, 0 refused**, plus 2 rows minted
by this merge (`conflicts.csv` `P1K17`; one `data_gaps.csv` coverage row) = **194 rows on disk**. Twelve
collision groups were found across the two emissions and every pair was **kept and cross-referenced rather than
folded**, because in each case the part-2 row adds a fact instead of restating one; the list is in
`_MANIFEST.md`. `merge_census.py` could not attribute 22 of the 192 rows (`AMBIGUOUS:validation.csv,
failures.csv`, identical 11-column schemas): **11 rows went to `validation.csv` and 11 to `failures.csv`**,
attributed by content — part 1 footer declares rows 1–5 and 6–10 of its combined block, and part 2 emits two
separate blocks whose rows are respectively positive signals and loss classes, matching its own §Q and §H/§O/§R
inventories. The evidence table is in the merge notes file. One date-column value was normalised (a
`channels.csv` `date_tested` cell carrying the prose "never tested within the stage"): the wording is preserved
verbatim in that row `notes` cell and the cell reads `UNKNOWN` — **COR-04**, the RD-122 precedent.

**Cross-part contradictions — both kept, a conflict row each, a marked site.**
1. `P1K05` (part 1 §Boundary 4) held that the one month ended January 26, 1997 corresponds to **no column** in
   the summary table and is therefore unusable. Part 2 `P1K16` / anchor `U.110` refutes the premise from the
   header row itself: nine columns, two of them one-month columns, both with values (revenue 190, net loss
   (522)). Marked at the §Boundary 4 sentence; `P1K05` keeps its text with the supersession printed inside it.
   **COR-01.**
2. `P1K01` (part 1 §Boundary 5) left the ~$899K movement of calendar-1997 expense unexplained and named the
   deferred-compensation route a mechanism candidate only, explicitly not a finding. Part 2 `P1K08` / `U.101`
   turns it into an identity (grant 2,100→4,277; amortisation 62→961; 961 − 62 = 899; allocated 18 / 471 / 410).
   Marked at §Boundary 5. The same pairing retires the part-1 statement that the first profitable quarter
   amount was not read: it is now read, 1,424. **COR-02.**
3. A contradiction **inside part 2**: two rows of one emission each assert the first profitable reported period
   (quarter ended 1997-12-31 at 1,424 against one month ended January 31, 1998 at 1,347). Neither emission row
   was edited; `P1K17` was minted to hold the reading — first profitable QUARTER, and first profitable AUDITED
   TRANSITION MONTH.
4. Part 1 §Boundary 3 and §D.4 cite the missing `## Untried` — marked at both sites and at the end of Volume 1.

**Anchors and conflicts tie.** §U declares eighteen anchors, `U.101`–`U.118`; all eighteen are cited by at least
one register row and no register row cites an undeclared anchor, so parity is 18 ↔ 18 with 0 undeclared and 0
uncovered. `conflicts.csv` carries 17 rows: seven from part 1 (`P1K01`–`P1K07`), nine from part 2
(`P1K08`–`P1K16`, each aliased to its anchor in §U as part 2 declares) and the merge-minted `P1K17`. **The seven
part-1 conflicts have no §U anchor**, because the part-1 anchor block is the section the truncation removed;
minting anchors for them would be writing text part 1 never wrote, so the gap is recorded instead (COR-03, and
`stage_1_index.md`).

**Residue not applied by this pass.** Claim record `P1-38` is cited by part 2 (the 1999-01-22 row of
`decisions.csv` and §K/§T prose) but is **declared in neither part**; the sequence `P1-28`…`P1-60` otherwise
runs complete with no duplicate declaration anywhere across the two parts (27 + 32 declarations, 0 collisions).
Part 1 prose cites `P1G06` and `P1G08`, and no emitted `data_gaps.csv` row carries either label. Both are left
exactly as emitted and handed to the Stage-1 auditor as outbound corrections; a merge may not invent a claim
record to fill a citation.

**Carry-forward.** Part 2 `## Untried` — eleven routes, each with its cost and its part-1 cross-reference —
follows Volume 2 below and is the volume register of untried routes. Every tier owes one (§15.2). Two of those
routes are the whole difference between T3 and T2, and this company ceiling is therefore still unmeasured.

---

# VOLUME 1 — carried verbatim from `_parts/s1_p1.md` (Header, Boundary, §A–§F, emission)

# NVIDIA — Stage 1 (1993 inception – 1999 IPO)

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-26T11:05:19Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Header

STATUS: WRITTEN 2026-09-26 (agent `nvidia-s1-p1`; every passage quoted here was opened in this session)

### Dataset, stage, and how to read this volume

*One document split for the file cap (method §9.3). Section letters, claim IDs, metric IDs and conflict
numbering run continuously across volumes: **§Header, §Boundary and §A–§F live here (`_parts/s1_p1.md`);
§G–§U and the claim-record appendix are owed by later volumes of this stage.** Cross-references of the
form `(Nvidia S1 §D.2, part_1)` name the volume. Nothing is renumbered to make a part look self-contained.
Tier **T3 register** for the **origin stage** specifically (RD-112: a tier is per stage, measured against
that stage's own window): short narrative + registers, §K/§N/§U still mandatory in later parts, 8k-word
planning budget. Per RD-122 the cap is a dispatch budget, not a limit on written evidence; nothing is
trimmed to fit it.*

**Dataset:** The Founder's Playbook — forensic reconstruction of what each company in the frozen universe
(`00_universe/`) looked like while its outcome was still unknown.
**Company (rank 16):** today's registrant **NVIDIA CORPORATION**, CIK 1045810 (EDGAR conformed name in the
held 1999 accession is `NVIDIA CORP/CA`, `STATE OF INCORPORATION: CA`, `FISCAL YEAR END: 1231` — header
metadata that lags the documents it files; see §Boundary 5).
**Stage:** 1 of 3. **Span:** **1993-04-05 (inception, as the audited statement period labels it) →
1999-01-21 (the date on the final prospectus; filed 1999-01-22, closing "on or about January 27, 1999").**
**Stage definition:** origin → first real-world experiment → repeatable validation → scalable company
formation. For consumer-technology silicon (§7 adaptation rule) the four beats are *the architecture bet,
the first taped-out product and its abandonment, the second product that sold, and the capital and public
market that made the firm self-financing* — all four sit inside this window. Post-1999 material is tagged
`(PB)` wherever it is used, and `(PB)` is a label on the evidence, never a licence to narrate an outcome
backwards.
**File:** part 1 of 3 for Stage 1 at this tier (p1 = Header/Boundary/A–F; p2 = G–P; p3 = Q–U + appendix).

**Hindsight firewall (§2).** Nothing here treats the RIVA 128's commercial result, the 1999 listing, or any
later position of the registrant as evidence that the NV1 architecture bet was rational, that its
abandonment in 1996 proves the founders were right the first time, or that the console market was ever
"obviously" the wrong target. The NV1 decision is reconstructed from what the registrant itself could say
in 1998 about what it then knew, and from dated contracts, not from what happened after. Anti-hagiography
test applied per §2 to every coda: each is written so that it would still read as plausible if the company
had failed in 2001. The words "visionary", "prescient" and "legendary" do not occur in this volume; the
registrant's own marketing sentence "MAKING FANTASY REALITY AND REALITY FANTASTIC" (424B4 cover artwork
description) is quoted only as evidence of what the company chose to print in January 1999.
**Record-selection null (§2).** Unrecoverable *because the survivor's archive is the one that was kept*:
**no Nvidia document of any kind exists on EDGAR before 1998-03-06** (this pass re-measured the index:
2,487 rows, `min filingDate = 1998-03-06`, 69 rows in 1993-01-01..2001-12-31 — measured, not inherited).
Therefore every word about 1993–1997 in a Tier-1 carrier is a **statement made in 1998–99 about 1993–97**,
and the only non-narrative exceptions are contracts the company filed as S-1 exhibits in 1998 (a 1994/1995
investors'-rights lineage; a 1995 sublease) which survive because they had to be filed, not because anyone
kept a record of the founding. What is gone and unrecoverable at this reach: the internal deliberation
behind the NV1 architecture, the rejected alternatives, any contemporaneous measure of how close the firm
came to running out of money, the identities of the 1993 Series A purchasers, and **any independent count
behind any 1993–1997 figure** — every one of those numbers traces to one company's audited statements as
recited by one company's own registration statement. See §A.3, §D.4, §F.2, §B.5.
**Confidence (§3):** **High** = a primary document for its own year, or 2+ independent origins; **Medium** =
one reliable source, or a retrospective-only primary; **Low** = conflicting, vague, or retrospective-only
with no primary carrier; **UNKNOWN** = a finding, never a gap to fill or smooth.
**The single-lineage finding, stated once and enforced everywhere (§3 filing-lineage rule).** The whole
in-window Tier-1 corpus of this company is **one registration lineage and its offspring**: the S-1 of
1998-03-06, its amendments, the 424B4 of 1999-01-22 (which *is* the amended registration statement, not a
second document), the FY1999 and FY2000 10-K405s, and the S-3 of 2000 — all one registrant, one auditor
(KPMG Peat Marwick LLP, renamed KPMG LLP between drafts), one set of underwriters, and in the 424B4's case
underwriters' counsel reproducing the company's text. **Counting the S-1, an S-1/A and the 424B4 as three
corroborations is the error this rule exists to stop.** Repetition across drafts is **version evidence** —
it tells us what the company changed, not what is independently true — and it is recorded as such in
`independence_note` on every row below. The only third-party-signed in-window carriers held anywhere are
inside the same accessions: Ex-4.3 (investors' rights, counterparty signature pages) and Ex-10.11 (Amdahl
sublease). Consequently: **no statement about a 1993–1995 decision in this volume carries a FACT class
sourced only from narrative prose**; those statements are FOUNDER CLAIM or RETROSPECTIVE INTERPRETATION
about the event, and FACT about the printing.
**ID scheme (§13, read before citing).** `P1-xx` claim records and `P1Sxx`/`P1Qxx`/`P1Tx`/`P1Dx`/`P1Vx`/
`P1Fx`/`P1Cx`/`P1Kx`/`P1Gx` register rows here are **dossier-local**. Global `source_id` blocks are assigned
centrally at merge; nothing here is a global key. `research/A_chronology_feasibility.md` and
`research/A3_intake_regrade.md` are prior passes' dossiers, cited as dossiers and never counted as a
second source; where this pass re-measured one of their figures and got a different answer, the correction
is named in §Boundary 6 and in a conflict row, and their number is not carried forward silently.

## Boundary

STATUS: WRITTEN 2026-09-26

**Geometry note.** This section enumerates the candidate Stage-1 subjects and dates, names the held document
behind each, and says why each rival **fails** — it does not assert a boundary and then defend it
rhetorically. Three losers are named below and one of them (the identity of the entity at the open) is only
partly resolved and stays live.

### 1. The entity question: which corporation is this stage about

| Instrument as printed in held bytes | Dated | What it establishes | Stage-1 status |
|---|---|---|---|
| S-1 cover page: "NVIDIA CORPORATION (EXACT NAME OF REGISTRANT AS SPECIFIED IN ITS CHARTER) — CALIFORNIA (PRIOR TO REINCORPORATION) … DELAWARE (AFTER REINCORPORATION)" | filed 1998-03-06 | the registrant filed as a **California** corporation with a Delaware reincorporation *prospective* at the filing date | the Stage-1 subject is the **California** NVIDIA Corporation |
| Ex-4.3 recital: "by and among NVIDIA CORPORATION, **a California corporation** (the 'Company')" | made and entered into as of **August 19, 1997** | a counterparty-signed instrument naming the California entity mid-stage | the entity that raised the 1993–1997 money |
| Ex-3.1 "CERTIFICATE OF INCORPORATION OF NVIDIA **DELAWARE** CORPORATION … IN WITNESS WHEREOF, this Certificate has been subscribed this **23rd day of February, 1998**", Sole Incorporator **Mitchell R. Truelock, Cooley Godward LLP** | 1998-02-23 | the Delaware vehicle was **formed in February 1998**, three weeks before the S-1 that lists it as an exhibit | end-of-stage consequence, not a Stage-1 actor |
| Ex-3.1 Exhibit A "AMENDED AND RESTATED CERTIFICATE OF INCORPORATION OF NVIDIA CORPORATION", execution line "this ____ day of ______________, 1998", signed Jen-Hsun Huang (President and CEO), attested Geoffrey Ribar (Secretary) | **blank date** | in the March 1998 filing the post-offering charter is still a **form**, not an executed instrument | conflict P1K02 |
| 424B4: "NVIDIA was incorporated in California in April 1993 and reincorporated in Delaware in April 1998" | 1999-01-22 | the company's own retrospective statement of both legs | FOUNDER/registrant claim about the events; FACT about the printing |

**Rule applied on every line below.** A figure printed in a 1998–99 registration statement belongs to the
**California** entity's account of itself. Where this volume says "the Company" it means NVIDIA Corporation
(California) through the reincorporation and the surviving registrant thereafter; the Delaware leg is a
consequence, is labelled as such, and is never used to date the 1993 act.

### 2. Candidate Stage-1 windows and why each rival fails

| # | Candidate open/close | Best held document | Verdict |
|---|---|---|---|
| 1 | **1993-04-05 → 1999-01-21** (inception statement-period label → the date printed on the final prospectus) | S-1 Summary Financial Data header "PERIOD FROM INCEPTION (APRIL 5, 1993) TO DECEMBER 31, 1993"; 424B4 cover dated "January 21, 1999", filed 1999-01-22 | **ADOPTED.** The open is the earliest date any held Tier-1 carrier attaches to this company, and it is a *statement-period* date (audited-header form), not a prose assertion; the close is the first date on which the company's own capital structure became publicly priced. |
| 2 | open at the founders' agreement, or at the first payroll | none | **REJECTED — unestablishable at this reach.** No held document dates the agreement to found, the first office, or the first employee. Recorded as UNKNOWN (P1G01), not as a smaller window. |
| 3 | close at the first profitable quarter (quarter ended 1997-12-31) | S-1 risk factor: "Although the Company generated net income in the quarter ended December 31, 1997, it incurred significant losses in each other quarter of fiscal 1997 and in each quarter of its prior fiscal years" | **REJECTED as a boundary, kept as a signal.** The registrant's own nine-month-to-1998-10-25 figures are still an operating **loss** of $(3,900)K, so a single profitable quarter is not a stage change; and choosing it would let a later outcome name the boundary. |
| 4 | close at the NV1 abandonment (first quarter of 1996) | S-1 and 424B4, identical sentence: "stopped selling the NV1 in the first quarter of 1996" | **REJECTED.** That is Stage 1's own mid-point, not its end — the firm continued to exist, raise (1997 Series D) and ship (RIVA128) afterwards inside this window. |

### 3. Where the record physically stops — measured, not assumed

This pass re-enumerated the index and the stored corpus itself rather than inheriting the dossier numbers:
`sources/_index/submissions.csv` = **2,487 rows, `min filingDate = 1998-03-06`, 69 rows inside
1993-01-01..2001-12-31, 30 of them with a blank `primaryDocument`**; `sources/sec/_MANIFEST.csv` = **31 stored
documents, first row 1998-03-06 S-1 `0001012870-98-000618`, 856,608 B**; `sources/financials/` and
`sources/wayback/` are **empty directories** (verified by listing). Consequence, stated as §14 rule 6
requires: **EDGAR family (a) is the only family with in-window Tier-1 text for this stage, and its floor is
1998-03-06, so the first five years of the stage are registrant-retrospective by construction.** That is a
finding about reach, not about the company. Family (b) web archives is **UNANSWERED** (empty directory — no
bytes, no negative artifact); (c) periodicals and (d) corporate print returned **no in-window naming**
(A4: 1 entity-bearing item, `01.-nvidia-annual-reports`, whose text layers run FY2005–FY2026); (e)
documentary is **UNTRIED**. See `## Untried`.
> **[MERGE 2026-09-30 | COR-03] The route block cited here was never written: part 1 ends after its register footer with a stray hash character. The routes are carried by the eleven-route list in part 2 and by the probe dossier, both present in this volume, and nothing was reconstructed in place of part 1.**

### 4. Basis of numerals — the rule that governs every quantity in this volume

Years 1993–1997 are **calendar years ending December 31**. The 424B4 prints: "effective January 31, 1998,
the Company changed its fiscal year-end financial reporting period to a 52- or 53-week year ending on the
last Sunday in January. The Company elected not to restate its previous reporting periods ending December
31", and adds that "the first and fourth quarters of fiscal 1999 are 12- and 14-week periods". Therefore:
(i) a "1997" figure and a "fiscal 1999" figure are **different bases and are not additive without the
transition month**; (ii) the audited transition month is printed as "the one month ended **January 31,
1998**"; (iii) the same prospectus once prints "the selected statement of operations data for the one month
ended **January 26, 1997** … are derived from unaudited financial statements" — a date that appears **nowhere
else** in the document and corresponds to **no column** in its own summary table (columns are: inception stub
1993, 1994, 1995, 1996, 1997, nine months to 1997-09-28, nine months to 1998-10-25). This volume writes that
string as printed, records the period it denotes as **UNKNOWN**, and does not use it (P1K05).
> **[MERGE 2026-09-30 | COR-01 | conflict P1K16 | anchor U.110] The premise in the sentence above is REFUTED by the bytes part 2 read: the summary-table header prints NINE columns, two of them one-month columns, and the January 1997 column carries revenue 190 and net loss (522) (carrier S4355, l.1941-1985). The printed string stays; the no-column statement does not travel forward.**
Every quantity in the registers carries **carrier** (which accession, which table), **basis** (calendar vs
fiscal, period-end vs average, gross vs net, total-company vs unit), and **CONTEMPORANEOUS vs RESTATED**.
"Restated" here has one specific in-corpus meaning: the same registration lineage printed a different number
for the same calendar year in a later draft (§5).

### 5. CONTEMPORANEOUS / RESTATED test, run on the held bytes

The 1998-03-06 S-1 and the 1998-12-23 S-1/A print, for the same audited calendar years:

| Calendar year | S-1 1998-03-06 | S-1/A 1998-12-23 = 424B4 | Movement |
|---|---|---|---|
| 1997 total revenue | 29,071 | 29,071 | none |
| 1997 gross profit | **7,845** | **7,827** | −18 |
| 1997 operating loss | **(506) (1,351) (6,470) (2,993) (2,560)** row → 1997 = **(2,560)** | **(3,459)** | −899 of expense |
| 1997 net loss | **(2,691)**, LPS $(.21) | **(3,589)**, LPS $(.28) | −898 |
| 1993–1996 rows | (484) (1,361) (6,377) (3,077) net loss | identical | none |

Both drafts present the 1995–1997 statement-of-operations rows as derived from statements **audited by KPMG
Peat Marwick** ("as of December 31, 1996 and 1997, and for each of the years in the three-year period ended
December 31, 1997, have been included in the Registration Statement in reliance upon the report of KPMG Peat
Marwick LLP"), and **no note in any held draft explains the change**. The 1997 column therefore travels in
this corpus as **RESTATED** and the March figures as superseded-draft, and P1K01 keeps the difference open
rather than averaging it. A mechanism candidate exists inside the same lineage — "the Company recorded
deferred compensation of $4.3 million … in 1997" and "we recorded deferred compensation of $4.3 million in
1997 and $361,000 in the one month ended January 31, 1998" — but it is an **INFERENCE, not a finding**: no
held text links the two, and the $4.3M gross figure does not equal the $898K net movement.
> **[MERGE 2026-09-30 | COR-02 | conflict P1K08 | anchor U.101] The mechanism named above as a candidate only is now an arithmetic identity inside the same lineage: grant 2,100 -> 4,277, amortisation 62 -> 961, and 961 - 62 = 899, allocated 18 to cost of revenue, 471 to research and development, 410 to selling, general and administrative (S4355, Statement of Stockholders Equity plus the quarterly table). What remains UNKNOWN is why the grants were re-measured, not how the movement is composed.**

### 6. Corrections this pass took on its own dispatch premises and on the prior dossiers

Four inherited statements failed against the bytes; each is corrected here and reaches the registers.
1. **"NV1 stopped being sold in the first quarter of 1997" — REFUTED.** Both the 1998-03-06 S-1 and the
   424B4 print "stopped selling the NV1 in the first quarter of **1996**", and the Results of Operations
   section independently says the console-targeted products "were discontinued in **1996**". The probe's
   bracketed "[1997]" is withdrawn; the 1996 date is used everywhere in this volume.
2. **"Amahl sublease of February 2, 1995" — REFUTED on both name and date.** Ex-10.11 is a "Sublease
   Agreement, dated **February 16, 1995**, between **Amdahl Corporation** and the Company, as amended on
   March 1, 1995 and September 1, 1995"; the sublet space is approximately **29,100 rentable square feet,
   charged as 27,875**, at Base Rent **$28,432.50 monthly / $341,190.00 annually**, Rent Commencement Date
   March 1, 1995, term thirty months. The probe's **34,251 / 33,026** pair is also real — it is the
   *expanded* figure from a later amendment ("increased to an aggregate size of approximately 34,251 rentable
   square feet … charged as 33,026 rentable square feet"). Both pairs are carried, each with its own date.
3. **"Nothing is claimed about FY1997 net loss" — now claimed, and it moved too** (see §5): the 1997 net loss
   changed from $(2,691)K to $(3,589)K across the lineage, which is a larger finding than the probe's
   operating-expense-only description.
4. **The probe's X2 Delaware conflict is refined, not adopted.** The 1998-02-23 executed certificate and the
   April 1998 prose are not in contradiction; the operative fact is that the charter that would govern the
   post-offering company was still a **blank-dated form** in the March 1998 filing (P1K02).

### 7. Post-boundary convention

Anything after 1999-01-21 is `(PB)`. `(PB)` material may be used in this corpus only to (i) date a silence,
(ii) name a route, or (iii) show what the company later said about the window — always labelled
RETROSPECTIVE SOURCE. The FY1999 10-K405's IPO sentence, the FY2000 figures, and the 2000–01 8-K/S-4 leg are
`(PB)` for Stage-2/Stage-3 use and are excluded from every Stage-1 conclusion here.

## A

STATUS: WRITTEN 2026-09-26

### A.1 The company as it stood at the close of the stage, on the last day the window allows

The condition of the firm at the moment its equity was first priced, all of it from the final prospectus
(424B4, filed 1999-01-22, prospectus dated January 21, 1999) and the December 1998 amendment:

* **It sold something, and it had sold nothing for most of its life.** Total revenue by calendar year:
  1993 `$--`, 1994 `$--`, 1995 `$1,182K`, 1996 `$3,912K`, 1997 `$29,071K`; then nine months to 1997-09-28
  `$5,537K` against nine months to 1998-10-25 `$92,700K`. **Two of its first years produced literally zero
  revenue** and the third produced $1.2M — this is the state, not a rhetorical prelude.
* **The turn is quarterly, and it is one product.** "Product revenue increased from less than $100,000 in
  the first two quarters of 1997 to $5.2 million and $22.1 million in the third and fourth quarters of 1997,
  respectively. This increase was due to sales from the RIVA128 graphics processor, which was introduced in
  August 1997."
* **It was still loss-making on any full-period view.** Calendar 1997 (final version) net loss `$(3,589)K`;
  the nine months to 1998-10-25 net loss `$(3,532)K` on operating loss `$(3,900)K`; accumulated deficit
  `$(17,074)K` at 1998-10-25 versus "approximately $14.0 million" at 1997-12-31.
* **It had no bank debt and small cash.** "As of December 31, 1997, the Company had $6.5 million in cash and
  cash equivalents and **no outstanding bank indebtedness**"; cash and equivalents $12,461K at 1998-10-25,
  pro-forma-as-adjusted $49,721K after the offering.
* **It had been financed privately, and thinly.** "Since inception, the Company has financed its operations
  primarily through private sales of convertible preferred stock totaling **$19.7 million** and, to a lesser
  extent, equipment lease financing and proceeds received from the exercise of employee stock options."
* **It was 184 people, and its controls said so.** "As of October 25, 1998, the Company had 184 employees as
  compared to 71 employees as of September 28, 1997"; "The Company's financial and management controls,
  reporting systems and procedures are **very limited** and will need to be upgraded significantly."
* **One year earlier it was 92 people, 62 of them engineers**; the year before that, 42.
* **It depended on two customers and one factory.** "Sales to STB and Diamond accounted for 63% and 31%,
  respectively, of the Company's total revenue in 1997" (94% between two buyers); "Substantially all of the
  Company's products currently are manufactured by ST in Crolles, France pursuant to a strategic
  collaboration agreement", with TSMC "recently established" as a second source "on a purchase order basis",
  and "in December 1997, the Company experienced low manufacturing yields at ST."
* **It went public small and with no history of public price.** 3,500,000 shares, **all sold by the Company**;
  28,595,976 shares to be outstanding after the offering; "Prior to this offering, there has been no public
  market for the Common Stock"; Nasdaq symbol NVDA; underwriters Morgan Stanley & Co. Incorporated,
  Hambrecht & Quist, Prudential Securities; closing "on or about January 27, 1999". The assumed price in the
  December 1998 amendment's pro-forma footnote is **$8.00 per share**; the **March 1998 S-1's equivalent
  footnote prints a literal blank** — "an assumed initial public offering price of $ per share".

### A.2 The company as it stood at the open of the stage

This is the honest version, and it is almost entirely negative. What any held Tier-1 carrier says about
April 1993 is: (i) an audited statement period labelled "from inception (April 5, 1993) to December 31,
1993"; (ii) three sentences that each co-founder "co-founded the Company in April 1993"; (iii) "In 1993, the
Company sold 4,303,000 shares of Series A preferred stock at $0.50 per share, net of $22,000 of issuance
costs"; (iv) for that stub period, revenue `$--`, gross profit `--`, operating loss `$(506)K`, net loss
`$(484)K`, total assets `$1,786K`, on 6,784 weighted shares. **Not one held document records anyone deciding
to found the company, anywhere it was decided, or who bought the Series A.** Outside directors were seated
within weeks — Coxe and Stevens "since June 1993", Jones "since November 1993" — which is the only sign of
outside capital arriving inside the founding year, and it is a governance sentence in the company's own
1998 filing.

### A.3 What this stage is not

It is not a story about a future winner, and three specific anti-readings must be blocked. **(a)** The zero
revenue of 1993–1994 is not "patience": the same filings show a company that had to raise money in 1993,
1994, 1995 and twice in 1997 to keep existing, and that priced its 1997 round **below** its 1995 round.
**(b)** The NV1's abandonment is not evidence that the founders saw the PC market correctly in 1993; the
registrant's own sentence gives the reason as an external standard-settling — "By the end of 1996, the PC
industry had broadly adopted Microsoft's Direct3D and Silicon Graphics Inc.'s ('SGI's') OpenGL 3D APIs. As a
result, the Company experienced a significant reduction in revenue from sales of the NV1" — and that sentence
places its stated cause *after* its stated effect (see P1K03), so it cannot carry the causality it appears to
carry. **(c)** Nothing in the window is a market-size fact: the only market statements in held in-window text
are the registrant's own unquantified self-descriptions ("the Company believes…", "over 40 awards", later
"over 180 awards"), and no independent count of the 3D-graphics market for 1993–1998 exists anywhere in this
corpus. The record-selection null in §Header applies with full force to §A.2: the surviving archive is the
winner's, and for 1993–1995 it survives only as the winner's own later recollection.

### A.4 Load-bearing claim records for §A

P1-01 Claim: The registrant's own audited statement-period label puts its inception at 1993-04-05. — Date: 1993-04-05 — Source path: sources/sec/0001012870-98-000618_0001012870-98-000618.txt (Form S-1, Summary Financial Data) — Source date: 1998-03-06 — Tier: 1 — Class: FACT about the audited header; FOUNDER CLAIM / retrospective registrant statement about the event — Passage: "PERIOD FROM INCEPTION (APRIL 5, 1993) TO DECEMBER 31, 1993" — Conf: High for the printing, Medium for the event date (one lineage, no constitutive document held) — Corroboration: 1 (424B4 repeats the same lineage) — Conflicts: None
P1-02 Claim: The company reported zero revenue in calendar 1993 and calendar 1994 and first revenue in 1995. — Date: 1993, 1994, 1995 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt (424B4 Summary Financial Data) — Source date: 1999-01-22 — Tier: 1 — Class: FACT as printed; basis = calendar years ended Dec 31, audited stub for 1993 — Passage: "Total revenue........... $ -- $ -- $ 1,182 $ 3,912 $29,071 $ 5,537 $92,700" — Conf: High (audited-header figures) — Corroboration: 1 lineage — Conflicts: None
P1-03 Claim: Since inception the company had financed operations mainly by private preferred sales totalling $19.7 million, and at 1997-12-31 held $6.5M cash with no bank indebtedness. — Date: 1997-12-31 — Source path: sources/sec/0001012870-98-000618_0001012870-98-000618.txt (Liquidity and Capital Resources) — Source date: 1998-03-06 — Tier: 1 — Class: FACT (registrant's own MD&A) — Passage: "the Company has financed its operations primarily through private sales of convertible preferred stock totaling $19.7 million" — Conf: Medium — Corroboration: 1 (same lineage; no lender or bank record held) — Conflicts: None
P1-04 Claim: Two customers took 94% of calendar-1997 revenue (STB 63%, Diamond 31%). — Date: calendar 1997 — Source path: sources/sec/0001012870-98-000618_0001012870-98-000618.txt (Risk Factors; Customer Concentration) — Source date: 1998-03-06 — Tier: 1 — Class: FACT as disclosed; the underlying sales are unauditable outside the filing — Passage: "Sales to STB and Diamond accounted for 63% and 31%, respectively, of the Company's total revenue in 1997." — Conf: High for the disclosure — Corroboration: 1 lineage — Conflicts: None
P1-05 Claim: Headcount was 42 at 1996-12-31, 92 at 1997-12-31 (62 in engineering), 71 at 1997-09-28 and 184 at 1998-10-25. — Date: four separate period-end dates — Source path: sources/sec/0001012870-98-000618 (S-1) and sources/sec/0001012870-98-003234 (S-1/A 1998-12-23) — Source date: 1998-03-06 / 1998-12-23 — Tier: 1 — Class: FACT, with population and date carried — Passage: "As of December 31, 1997, the Company had 92 employees, 62 of whom were engaged in engineering" — Conf: High — Corroboration: 1 lineage, several drafts (version evidence only) — Conflicts: P1K04 (date/population mismatch trap)
P1-06 Claim: The calendar-1997 loss column changed inside one registration lineage between the March 1998 S-1 and the December 1998 amendment (gross profit 7,845→7,827; operating loss (2,560)→(3,459); net loss (2,691)→(3,589); LPS (.21)→(.28)) with no explanatory note in any held draft. — Date: 1998-03-06 → 1998-12-23 — Source path: sources/sec/0001012870-98-000618 and sources/sec/0001012870-98-003234 — Source date: 1998-12-23 — Tier: 1 — Class: FACT about the two printings; the reason is UNKNOWN — Passage: "Net loss................ (484) (1,361) (6,377) (3,077) (2,691)" / "Net income (loss)....... (484) (1,361) (6,377) (3,077) (3,589)" — Conf: High (both tables read this session) — Corroboration: 1 lineage — Conflicts: P1K01

## B

STATUS: WRITTEN 2026-09-26

### B.1 The three founders, exactly as the registrant described them, and nothing beyond it

The 1998-03-06 S-1's Management section, "Certain information regarding the Company's executive officers,
key employees and directors **as of February 28, 1998** is set forth below", carries three sentences of the
same shape:

* "Jen-Hsun Huang co-founded the Company in April 1993 and has served as President, Chief Executive Officer
  and a member of the Board of Directors of the Company **since its inception**." Age 35.
* "Chris A. Malachowsky co-founded the Company in April 1993 and has been Vice President, Engineering for
  the Company since that time." Age 38.
* "Curtis R. Priem co-founded the Company in April 1993 and has been Chief Technical Officer for the Company
  since that time." Age 38.

That is the entire founding-act evidence for three people, in one document, three times, in the company's
own voice. **The Fortune dataset flag "founder is CEO" is therefore corroborated for Huang only in the weak
sense that the same registrant sentence names him co-founder and CEO together** — and that sentence is one
lineage, printed 1998–1999 about 1993.

**Ages are as of 1998-02-28 and are not to be moved into 1993.** A reader who wants the founders' ages at
founding must derive them: 35 − (1998 − 1993) = **about 30 for Huang, about 33 for Malachowsky and Priem at
April 1993**, each ±1 year because no held document gives a birth date. That arithmetic is an
ESTIMATE/DERIVED row (P1Q22), is printed nowhere, and is not a fact about the founding.

### B.2 The pre-founding positions, which are the only 1980s facts in evidence

* Huang: "From 1985 to 1993, Mr. Huang was employed at LSI Logic Corporation, a computer chip manufacturer,
  where he held a variety of positions, most recently as Director of Coreware business unit responsible for
  LSI's 'system-on-a-chip' strategy." (An earlier AMD leg is recorded in the prior probe dossier but was
  **not read by this pass** and is therefore not written here.)
* Malachowsky: "From 1987 until April 1993, Mr. Malachowsky was a Senior Staff Engineer for Sun
  Microsystems, Inc. … From 1980 to 1986, Mr. Malachowsky was a manufacturing design engineer at
  Hewlett-Packard Company."
* Priem: "From 1986 to January 1993, Mr. Priem was Senior Staff Engineer at Sun Microsystems where he
  architected the GX graphics products, including the world's first single chip GUI accelerator. From 1984 to
  1986, Mr. Priem was a hardware engineer at GenRad, Inc."

Two observations, both INFERENCE and both carrying their alternative: the two technical founders left **the
same employer's graphics group** (Sun, Priem to January 1993 and Malachowsky to April 1993), which is
consistent with a common origin for the product idea; the alternative explanation — that the three met
elsewhere and the Sun overlap is coincidence — is not excluded by any held text, because **no held document
describes how the company came to be proposed at all.** Priem's stated prior work ("the world's first single
chip GUI accelerator") is the company's own characterization of a third party's product and is quoted as
such, not adopted.

### B.3 Who put money in, and what the instruments actually prove

The equity ladder is stated once and identically in the lineage: "In 1993, the Company sold 4,303,000 shares
of Series A preferred stock at $0.50 per share, net of $22,000 of issuance costs. In 1994, the Company sold
2,390,831 shares of Series B preferred stock at $1.80 per share, net of $57,000 of issuance costs. In 1995,
the Company sold 416,667 shares of Series B preferred stock at $1.80 per share. In 1995, the Company sold
750,000 shares of Series C preferred stock at $6.67 per share, net of $14,000 of issuance costs. On **August
19 and September 12, 1997**, the Company sold an aggregate of 1,438,812 shares of **Series D** preferred
stock at **$5.26** per share, net of $30,000 of issuance costs."

Three things follow, and one does not:
* **The 1997 round was priced 21% below the 1995 round** ($5.26 vs $6.67 per share; derived, P1Q13) while
  the company was still loss-making. That is an in-period, filed price fact about how hard the middle years
  were, and it needs no retrospective narrative to support it.
* **The company had outside board seats within two months of the filing date.** Coxe (Sutter Hill Ventures,
  "a general partner of the general partner") and Stevens (Sequoia Capital, "a general partner … since March
  1993") "since June 1993"; Harvey C. Jones, Jr. "since November 1993".
* **It does not follow that the 1993 Series A was bought by those firms.** The Series A purchasers are
  **not named in any held document** (P1G02). Sequoia and Sutter Hill appear as *signatory parties* of the
  1997 investors'-rights instrument, whose own recital shows it descends from an "Investors' Rights Agreement
  dated as of **December 19, 1994** … amended by Amendment Number One as of **January 23, 1995** and by
  Amendment Number Two as of **July 5, 1995**" — so the earliest documentary naming of these investors inside
  the window is **December 1994**, not 1993. Attributing the 1993 round to them would be exactly the promoted
  inference this corpus forbids.
* **The counterparty-signed Ex-4.3 signature pages are the closest thing to a 1993–1997 primary document
  held anywhere.** They list, among the shareholders: JAFCO entities (Japan Associated Finance Co., Ltd.,
  JAFCO G-5 Investment Enterprise Partnership, U.S. Information Technology Investment Enterprise
  Partnership); eight Sequoia vehicles; Sutter Hill Ventures; ANVEST, L.P. signed by G. Leonard Baker, David
  R. Golob, James C. Gaither, Ronald L. Perkins and **Tench Coxe**; **Harvey C. Jones, Jr.** and **William J.
  Miller** in person; Worldview Technology Partners I, L.P.; Itochu Corporation and Itochu Technology, Inc.;
  **Sega Enterprises, Ltd.**; Leland Stanford Junior University; Tow Partners; Genstar Investment Corporation;
  Wells Fargo Bank as trustee for several named individuals; Jones Living Trust; Wythes Living Trust; Harris
  Barton; Thomas vardell; David L. Anderson; Marshall A. and Claudia L. Smith; Joanne C. Knight. The Company
  signed "By: **Jen-Hsun Huang, President**". **This page names *who the shareholders were as of August 19,
  1997*; it does not allocate any of them to a 1993 series** (no schedule was read that does so).

**The Sega point, made carefully because it is where folklore usually enters.** The famous account of Sega
rescuing the company is **not carried by any held byte**: "$5 million" and "5,000,000" in a cash-rescue
sense, and any "days of cash" phrasing, return **0 hits** in the S-1; Sega appears in Nvidia's in-window
Tier-1 record **only as a party entitled to financial information and inspection** under a 1997 shareholders'
agreement. What the filings do support is that Sega was an equity-holder in 1997 and that the company's
first products were console-market products whose development it later ceased. That is the ceiling of the
held evidence, and the rest is a recorded **FOUNDER CLAIM with no carrier** (P1G03), not a fact.

### B.4 Company state around the founders: control, dependence, and what was *not* insured

* "Prior to this offering, there has been no public market for the Common Stock of the Company." All 3,500,000
  offering shares were sold **by the Company**.
* Beneficial ownership as printed in the 424B4: "Entities associated with Sequoia Capital VI … 3,095,902
  13.2% 10.8%"; "Jen-Hsun Huang … 3,100,000 13.1" (the after-offering percentage was not read by this pass —
  see P1S04 note). So the largest named holder and the CEO were within ~1 point of each other pre-IPO;
  **no held document shows a founder controlling a majority**, and the register does not assert one.
* Founder dependence is stated as risk, not glory: "The loss of the services of any of its executive
  officers, technical personnel or other key employees, particularly Jen-Hsun Huang, the Company's President
  and Chief Executive Officer, would have a material adverse effect on the Company's business…" and, in the
  same paragraph, "The Company does **not** have 'key person' life insurance policies on any of its
  employees." That absence is a hard, checkable fact about how thinly the company protected itself.
* Employment was at will: "no officer or employee … is bound by an employment agreement, and the
  relationships of such officers and employees with the Company are, therefore, at will."
* Facilities were subleased, not owned: 432 Lakeside Drive, Sunnyvale, from Amdahl Corporation, term thirty
  months from March 1995, at $341,190 annual base rent (§Boundary 6.2). The registrant's address of record
  moves inside the window: "1226 Tiros Way, Sunnyvale" (1998-03-06 S-1) → "3535 Monroe Street, Santa Clara"
  (424B4).

### B.5 What cannot be said about the founding, and why it stays UNKNOWN

Not merely unknown at present but **structurally unreachable inside the one family that answered**: the
1993 California certificate of incorporation is **not filed** (the S-1 files only the Delaware certificate of
February 1998, the Delaware bylaws, and a form of amended charter), so "incorporated in California in April
1993" rests on the company's own assertion; the Series A purchase agreement and certificate stubs are not
held; the founders' own contribution (cash, IP, or neither) is nowhere stated; and no interview, memoir or
trade-press body inside the window is on disk. **This is the finding.** It is recorded as a null about reach
(§3 of Boundary), and every origin sentence in §B that outruns a 1998 printed assertion is labelled
accordingly.

### B.6 Load-bearing claim records for §B

P1-07 Claim: Three named individuals are recorded as co-founders, and the CEO is one of them. — Date: April 1993 (as asserted) — Source path: sources/sec/0001012870-98-000618 (Management) — Source date: 1998-03-06 — Tier: 1 — Class: registrant FOUNDER CLAIM, retrospective to 1993; FACT about the 1998 printing — Passage: "Jen-Hsun Huang co-founded the Company in April 1993 and has served as President, Chief Executive Officer and a member of the Board of Directors of the Company since its inception." — Conf: Medium — Corroboration: 1 lineage (the same three sentences recur in the S-1/As and 424B4) — Conflicts: None
P1-08 Claim: Ages of the officers and directors were stated as of February 28, 1998: Huang 35, Malachowsky 38, Priem 38, Coxe 40, Jones 45, Miller 52, Seawell 50, Stevens 38. — Date: 1998-02-28 — Source path: sources/sec/0001012870-98-000618 (Management table) — Source date: 1998-03-06 — Tier: 1 — Class: FACT (self-reported, as of a named date) — Passage: "Certain information regarding the Company's executive officers, key employees and directors as of February 28, 1998 is set forth below." — Conf: High — Corroboration: 1 lineage — Conflicts: None
P1-09 Claim: Outside venture directors were seated from June 1993, within two months of the inception date. — Date: 1993-06 — Source path: sources/sec/0001012870-98-000618 (Management bios) — Source date: 1998-03-06 — Tier: 1 — Class: FACT as disclosed about a 1993 event, carried by a 1998 document — Passage: "Tench Coxe has been a director of the Company since June 1993." — Conf: Medium (retrospective-only; the board record itself is not held) — Corroboration: 1 lineage — Conflicts: None
P1-10 Claim: The 1997 preferred round was priced at $5.26 per share against $6.67 for the 1995 round — a down price. — Date: 1997-08-19 and 1997-09-12 — Source path: sources/sec/0001012870-98-000618 (Note 3 Stockholders' Equity) — Source date: 1998-03-06 — Tier: 1 — Class: FACT for each price; the down-round characterization is DERIVED (P1Q13) — Passage: "the Company sold an aggregate of 1,438,812 shares of Series D preferred stock at $5.26 per share, net of $30,000 of issuance costs." — Conf: High — Corroboration: 1 lineage — Conflicts: None
P1-11 Claim: Sega Enterprises, Ltd. was a party to a counterparty-signed Nvidia shareholders' agreement effective August 19, 1997, with contractual financial-information and inspection rights. — Date: 1997-08-19 — Source path: sources/sec/0001012870-98-000618 (Exhibit 4.3, Second Amended and Restated Investors' Rights Agreement, §§2.1–2.2 and signature pages) — Source date: 1998-03-06 — Tier: 1 — Class: FACT (third-party-signed instrument inside a Tier-1 accession) — Passage: "The Company will furnish the following reports (i) to Sega Enterprises, Ltd., (ii) to Itochu Corporation and Itochu Technology, Inc." — Conf: High — Corroboration: 1 (the instrument's own counterparty signatures are its independence; it is not company prose) — Conflicts: None
P1-12 Claim: No held in-window document states that Sega paid the company any sum, and the company had no bank debt at 1997-12-31. — Date: 1997-12-31 — Source path: sources/sec/0001012870-98-000618 (whole-document grep for "Sega", "$5 million", "weeks of cash") — Source date: 1998-03-06 — Tier: 1 — Class: FACT about the absence in this corpus; NOT a finding that no such payment existed — Passage: "As of December 31, 1997, the Company had $6.5 million in cash and cash equivalents and no outstanding bank indebtedness." — Conf: High as to the corpus, UNKNOWN as to the event — Corroboration: 1 — Conflicts: None
P1-13 Claim: The registrant stated it carried no key-person life insurance on any employee while naming the CEO's loss as a material adverse effect. — Date: 1998-03-06 — Source path: sources/sec/0001012870-98-000618 (Risk Factors) — Source date: 1998-03-06 — Tier: 1 — Class: FACT as disclosed — Passage: "The Company does not have 'key person' life insurance policies on any of its employees." — Conf: High — Corroboration: 1 lineage — Conflicts: None

## C

STATUS: WRITTEN 2026-09-26

### C.1 The problem, stated by the only entity that stated it

The registrant's self-description at the top of its own business section: "NVIDIA designs, develops and
markets 3D graphics processors and related software that provide high performance interactive 3D graphics to
the mainstream PC market", with the strategy sentence: "The Company's strategy to achieve this objective
includes focusing on the mainstream PC market, targeting leading OEM customers, extending its technological
leadership in 3D graphics and increasing its market share by leveraging strategic alliances."

The **problem as the company framed it in 1998** is the sentence that matters for Stage 1, because it is the
only statement of the original problem in Tier-1 text, and it is retrospective: "The NV1 was developed **in
the absence of industry standards** with the goal of establishing the Company's proprietary NV technology as
a 3D graphics standard." The company's own account of its founding problem was therefore *not* "make a fast
chip" but **become the standard** in a market that had no standard yet — and the very next sentence names
what happened to that framing: "By the end of 1996, the PC industry had broadly adopted Microsoft's Direct3D
and Silicon Graphics Inc.'s ('SGI's') OpenGL 3D APIs. As a result, the Company experienced a significant
reduction in revenue from sales of the NV1…"

**Who set the problem is UNKNOWN and stays UNKNOWN.** No held document records a founding hypothesis, a
business plan, a rejected alternative framing, or any disagreement among the three named co-founders about
the target market. The only in-window statement of intent available to this corpus is the company's
1998–99 explanation of what it had been doing — which is the definition of a retrospective interpretation.

### C.2 What the problem was *not*, on this evidence

The corpus does not support the following, and they are named so no later pass smuggles them in: that the
founders identified the PC 3D market in 1993 (their first product was "targeted primarily to the **game
console** market"); that any customer demand existed before a product did (revenue was `$--` in 1993 and
1994); that the company had any market share to lose when the NV1 was discontinued; or that the APIs which
later "broadly adopted" were known in 1993 to be the route (Direct3D and OpenGL are named only in the 1996-
and 1997-dated framing sentences). The 1998 filing does say the company believed its products "provide a
simpler and lower cost graphics solution relative to competing solutions, including multi-chip or multi-board
2D/3D graphics subsystems" — a company assertion about architecture economics, with no cost comparison, no
pricing table and no third-party benchmark anywhere in the held bytes.

### C.3 Knowability, for this stage (§7 format)

* **KNOWABLE:** inception period label (1993-04-05); incorporation state (California, per the registrant's own
  cover-page entry "CALIFORNIA (PRIOR TO REINCORPORATION)"); the three names and their roles; the preferred
  ladder with dates, share counts, prices and issuance costs; the first product name and its market
  description; the fiscal-year series of revenue and losses 1993–1997; headcount at four dates; the two-customer
  concentration of 1997; the manufacturing dependency; the subleased premises; the terms on which the
  company described the NV1's end.
* **NOT KNOWABLE from the one family that answered, and unreachable without new routes:** who bought the
  Series A; who the first paying customer was; what the founders contributed; whether the company ever came
  within weeks of stopping; what the NV1 cost to develop and to build; what its price to a customer was; how
  many units of anything shipped; what alternatives were rejected; how the 3D market was sized by anyone
  other than the company describing it.
* **UNKNOWN with a named route:** the last nine items above are all reachable in principle through family
  (c) periodicals, family (e) documentary records, or the unfetched in-window accessions listed in
  `## Untried`. UNKNOWN here is a claim about this corpus's reach, not about the past.

### C.4 Claim records for §C

P1-14 Claim: The registrant described its original problem as establishing its proprietary NV technology as the 3D graphics standard in a market without standards. — Date: 1993–1995 (as later stated) — Source path: sources/sec/0001012870-98-000618 (Business) — Source date: 1998-03-06 — Tier: 1 — Class: RETROSPECTIVE INTERPRETATION about the 1993-94 intent; FACT about the 1998 statement — Passage: "The NV1 was developed in the absence of industry standards with the goal of establishing the Company's proprietary NV technology as a 3D graphics standard." — Conf: Medium — Corroboration: 1 lineage — Conflicts: P1K03
P1-15 Claim: The company's first product was aimed at the game console market, not the PC 3D market it later described as its problem. — Date: 1995-05 — Source path: sources/sec/0001012870-98-000618 (Business) — Source date: 1998-03-06 — Tier: 1 — Class: FACT as disclosed — Passage: "The NV1 was a multimedia accelerator that provided 3D graphics, video and audio for interactive multimedia, and was targeted primarily to the game console market." — Conf: High — Corroboration: 1 lineage — Conflicts: None
P1-16 Claim: No held document records a founding hypothesis, business plan or rejected alternative. — Date: window-wide — Source path: sources/ (whole-corpus enumeration; `sources/wayback/` and `sources/financials/` empty) — Source date: 2026-09-26 — Tier: 1 — Class: FACT about this corpus; NOT a claim that none exists — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High as to the corpus — Corroboration: 0 — Conflicts: None
---
## D

STATUS: WRITTEN 2026-09-26

### D.1 The first real-world experiment was a product, and it took the company two years to have one

The registrant's own periodisation, verbatim and identical in the March 1998 S-1 and in the final prospectus:
"Since its inception in April 1993 through the end of 1994, NVIDIA was **in the development stage** and was
primarily engaged in product development and product testing. The Company introduced its first product, the
NV1, in May 1995."

"Development stage" is a defined accounting status with an evidentiary consequence, not a metaphor: for the
1993 stub and 1994 the company reported **no revenue at all**, an operating loss of `$(506)K` and `$(1,351)K`
respectively, and total assets of `$1,786K` at 1993-12-31 and `$5,450K` at 1994-12-31. The experiment's cost
is visible only as that loss and as the two private rounds that funded it (1993 Series A at $0.50; 1994
Series B at $1.80 — i.e. the price of the company's paper **tripled** between the founding year and the
second year, which is the only in-window market test of the idea that the filings preserve).

### D.2 The one piece of non-narrative evidence that the experiment had a paying sponsor

Accrued liabilities carry, at both 1996-12-31 and 1997-12-31: "**Advances on development agreement …
$2,500 … $2,500** (in thousands)", and the cash-flow discussion attributes the 1995→1996 improvement in
operating cash use ("Net cash used in operating activities was **$6.1 million in 1995, $300,000 in 1996** and
$1.2 million in 1997") to "a smaller operating loss and **higher deferred contract funding** in 1996". So
some counterparty had committed $2.5M to a development programme that was still sitting on the balance sheet
as an advance two years later, and contract funding — not sales — is what the company itself named as the
reason its cash burn fell in 1996. **The counterparty is not named in any held text this pass read**
(P1G04); a console-partner explanation is a lead, not a finding.

### D.3 The experiment failed, inside the window, on the company's own numbers

"stopped selling the NV1 in the **first quarter of 1996**" / "These products were discontinued in 1996 due to
their proprietary standards and market changes" / "The Company also **ceased development of the NV2**, a
product designed for a game console platform, and began developing the RIVA128 graphics processor."

The filed trace of that failure is measurable and is the strongest contemporaneous evidence in the stage:
revenue fell from `$3,912K` (1996) after the NV1 was pulled, the **largest loss of the window is 1995's
`$(6,377)K` net loss / `$(6,470)K` operating loss**, gross profit was **negative** in 1995 `$(367)K`, and the
company's 1997 round priced at $5.26 against $6.67 in 1995. The second experiment — RIVA128 — is dated in
the same lineage: introduced August 1997, "The Company first generated revenue from sales of its current 3D
graphics processor product **in the third quarter of 1997**", product revenue `$5.2M` then `$22.1M` in Q3 and
Q4 1997.

### D.4 The near-death firewall — where a recollection must not be promoted

This is the classic promotion site, so it is handled as a rule rather than as prose. **Held in-window Tier-1
evidence for distress (all CONTEMPORANEOUS, all one lineage):** zero revenue in 1993 and 1994; negative gross
profit in 1995; a $6.4M operating loss in 1995; a down-priced 1997 round; "$6.5 million in cash … and no
outstanding bank indebtedness" at 1997-12-31; "The Company incurred losses in each quarter from inception
through the third quarter of 1997 and in each year"; an accumulated deficit of $14.0M then $17.1M; a
"very limited" control environment; and a going-forward capital risk factor.
**NOT held, and not to be written as fact:** any statement that the company was weeks from closing, any cash
runway figure, any named rescue payment, any founder's account of the moment. Searches of the S-1 for "$5
million", "5,000,000" in a rescue sense, "weeks of cash", "days of cash", "ran out of money", "bankrupt"
returned **no in-window narrative at all**; Sega appears only as a 1997 contract party (§B.3). A retrospective
founder recollection of near-death exists in the popular record — this corpus **does not hold it**, and the
route to it is `## Untried` items 3–6, with the explicit instruction that whatever is fetched must be
classified **FOUNDER CLAIM / retrospective memory**, dated to the interview, never to 1995.
**What the distress evidence cannot show, either way:** that the company was, on any given day, within reach
of stopping. The filings show a firm that was repeatedly short of money and repeatedly refinanced; they do
not measure proximity to failure, and §M (later volume) inherits that limit.

### D.5 Claim records for §D

P1-17 Claim: The company spent April 1993 through December 1994 in the development stage with no revenue and shipped its first product in May 1995. — Date: 1993-04 → 1995-05 — Source path: sources/sec/0001012870-98-000618 (Business; Summary Financial Data) — Source date: 1998-03-06 — Tier: 1 — Class: FACT as disclosed about a period the same document's audited stub covers — Passage: "Since its inception in April 1993 through the end of 1994, NVIDIA was in the development stage and was primarily engaged in product development and product testing. The Company introduced its first product, the NV1, in May 1995." — Conf: High (for the disclosure) — Corroboration: 1 lineage — Conflicts: None
P1-18 Claim: A $2.5M "advance on development agreement" sat in accrued liabilities at 1996 and 1997, and the company attributed its lower 1996 cash burn to higher deferred contract funding. — Date: 1996-12-31 and 1997-12-31 — Source path: sources/sec/0001012870-98-000618 (Note 2 Accrued Liabilities; MD&A Liquidity) — Source date: 1998-03-06 — Tier: 1 — Class: FACT — Passage: "Advances on development agreement........................... $2,500 $2,500" — Conf: High — Corroboration: 1 lineage — Conflicts: None
P1-19 Claim: The NV1 was pulled from sale in Q1 1996 and the NV2 console project was cancelled, on the company's own account of the reason. — Date: 1996 Q1 (cessation), 1996 (discontinuation stated) — Source path: sources/sec/0001012870-98-000618 and sources/sec/0001012870-99-000192 (identical sentence) — Source date: 1998-03-06 / 1999-01-22 — Tier: 1 — Class: FACT about the events as disclosed; the causal sentence is RETROSPECTIVE INTERPRETATION — Passage: "The Company also ceased development of the NV2, a product designed for a game console platform, and began developing the RIVA128 graphics processor." — Conf: High for the cessation, Medium for the cause — Corroboration: 1 lineage, two drafts (version evidence) — Conflicts: P1K03
P1-20 Claim: No held in-window document records the company as weeks from failure, and the cash-rescue folklore has no carrier in this corpus. — Date: window-wide — Source path: sources/sec/ (grep of the S-1 and 424B4 for the rescue phrasings listed in §D.4) — Source date: 2026-09-26 — Tier: 1 — Class: FACT about the corpus; UNKNOWN about the event — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High as to the corpus — Corroboration: 0 — Conflicts: None

## E

STATUS: WRITTEN 2026-09-26

### E.1 What the products were, on the only description held

| Product | Held description | Dated in-window | Status of the description |
|---|---|---|---|
| **NV1** | "a multimedia accelerator that provided 3D graphics, video and audio for interactive multimedia, … targeted primarily to the game console market … developed in the absence of industry standards with the goal of establishing the Company's proprietary NV technology as a 3D graphics standard" | introduced **May 1995**; sales stopped **Q1 1996** | registrant's own retrospective account, in audited-stub-covered years |
| **NV2** | "a product designed for a game console platform" — development **ceased** | by 1996 | the only sentence about it anywhere held; it never existed as a revenue line |
| **RIVA128** | "designed to deliver a highly immersive, interactive 3D experience … provides superior processing power at competitive prices and is **architected to take advantage of mainstream industry standards such as Microsoft's Direct3D API**. The highly integrated design … combines high performance 3D and 2D graphics on a single chip and provides a simpler and lower cost graphics solution relative to competing solutions, including multi-chip or multi-board 2D/3D graphics subsystems" | introduced **August 1997**; first commercial shipment and first revenue of the current line **Q3 1997** | registrant claim, with the architecture statement checkable against the console-era sentence above |
| **RIVA128ZX / RIVA TNT** | named as successors in the same family | shipments began **March 1998 / July 1998** | registrant claim |

**The architecture reversal is the single most informative product fact in the window, and it is the
registrant's own.** The 1993–1995 bet was a **proprietary** standard ("establishing the Company's proprietary
NV technology as a 3D graphics standard"); the 1997 product was architected **to a third party's standard**
("architected to take advantage of mainstream industry standards such as Microsoft's … Direct3D API"). Both
sentences are in one document. What the document does **not** contain is any account of who made that
reversal, when it was decided, or what it cost — so the reversal is a FACT about the two designs and
UNKNOWN as a decision (§N's problem, in part 2).

### E.2 How it was built, and who owned the risk

"Substantially all of the Company's products currently are manufactured by **ST in Crolles, France** pursuant
to a strategic collaboration agreement (the 'ST Agreement')", and "the Company has **recently established a
relationship with TSMC as a second semiconductor manufacturer**. The Company obtains manufacturing services
from both ST and TSMC **on a purchase order basis**, and neither ST nor TSMC has any obligation to provide
the Company with any specified minimum quantities of product." The risk allocation is stated as the
company's own: "the Company typically pays for wafers, which may or may not have any functional products.
Accordingly, **the Company bears the financial risk until production is stabilized**… The Company typically
begins wafer production in advance of stabilized yields. Failure to stabilize yields … would materially
adversely affect the Company's revenue, gross profit and results of operations. **For example, in December
1997, the Company experienced low manufacturing yields at ST.**" The same agreement ran the other way: "The
ST Agreement also grants ST a worldwide license to sell the RIVA128 and RIVA128ZX graphics processors.
**Royalty revenue from sales of the RIVA128 graphics processor by ST represented 6% of the Company's total
revenue in 1997.**" And on the trade name itself: "The Company and ST Microelectronics, Inc. have filed
jointly for trademark protection for RIVA128."

This is a fabless company before the term was routine: no fab, no inventory commitment from its supplier, a
supplier licensed to resell its product, and a named yield disaster in the quarter the company first made
money. The **second source at TSMC** is the company's answer to the dependency risk factor, "because the lead
time needed to establish a strategic relationship with a new manufacturing partner could be several months,
there is no readily available alternative source of supply for any specific product."

### E.3 What cannot be reconstructed about the product, and the route

Not derivable from any held byte: unit volumes for anything; the NV1's bill of materials, die, clock rates,
price to a customer, or its software/driver stack; how many titles or which console platform NV2 was aimed at
(it says only "a game console platform"); whether any NV1 inventory was written off (a candidate component of
P1K01's movement, named as a question not an answer); per-product revenue split between 1995's product and
royalty lines; and any third-party measurement of "high performance" — the only validation numbers held are
the company's own award counts, which **quadruple across the lineage**: "over 40 awards from recognized
industry publications" (1998-03-06) → "over 180 awards" (1999-01-22), in the same sentence frame (P1K06).
The route to product detail is family (c) trade press and family (b) archived product pages, both untried or
unanswered at this reach (`## Untried` 3, 5, 6).

### E.4 Claim records for §E

P1-21 Claim: The company's first product line was proprietary-standard by design and its second was architected to Microsoft's Direct3D, in the same document. — Date: 1995-05 / 1997-08 — Source path: sources/sec/0001012870-98-000618 (Business) — Source date: 1998-03-06 — Tier: 1 — Class: FACT for each product's stated architecture; the decision behind the change is UNKNOWN — Passage: "The RIVA128 graphics processor … is architected to take advantage of mainstream industry standards such as Microsoft's Direct3D API." — Conf: High — Corroboration: 1 lineage — Conflicts: None
P1-22 Claim: Substantially all products were manufactured by ST Microelectronics at Crolles, France, with TSMC newly added as a second source on purchase orders, and the company bore wafer risk until yields stabilised. — Date: as of 1998-03-06 — Source path: sources/sec/0001012870-98-000618 (Business—Manufacturing; Risk Factors) — Source date: 1998-03-06 — Tier: 1 — Class: FACT as disclosed — Passage: "Accordingly, the Company bears the financial risk until production is stabilized." — Conf: High — Corroboration: 1 lineage; no ST-side document held (a genuine independence gap) — Conflicts: None
P1-23 Claim: The company reported low manufacturing yields at ST in December 1997, the quarter of its first net income. — Date: 1997-12 — Source path: sources/sec/0001012870-98-000618 (Risk Factors) — Source date: 1998-03-06 — Tier: 1 — Class: FACT (self-disclosed negative; a contemporaneous in-window failure) — Passage: "For example, in December 1997, the Company experienced low manufacturing yields at ST." — Conf: High — Corroboration: 1 lineage — Conflicts: None
P1-24 Claim: The registrant's own award count rose from "over 40" to "over 180" across ten months of one registration lineage. — Date: 1998-03-06 → 1999-01-22 — Source path: sources/sec/0001012870-98-000618 and sources/sec/0001012870-99-000192 — Source date: 1999-01-22 — Tier: 1 — Class: FOUNDER CLAIM / corporate marketing claim, both versions unverified — Passage: "has enabled the Company's customers to receive over 40 awards from recognized industry publications, including PC Magazine, PC Computing, PC World, Computer Gaming World, PC Games and CNET." — Conf: Low (as to awards; High as to the escalation) — Corroboration: 1 lineage — Conflicts: P1K06
---
## F

STATUS: WRITTEN 2026-09-26

### F.1 Who the customer was, in the company's own structure

The registrant states its channel plainly: "The Company has only a **limited number of customers** and its
sales are highly concentrated. The Company **primarily sells its products to add-in board manufacturers**,
which incorporate graphics products in the boards they sell to PC OEMs." Demand, on the company's own
accounting, came from a design cycle two steps away: "Sales to add-in board manufacturers primarily are
dependent on achieving **design wins** with leading PC OEMs", and "The Company's future success will depend
in large part on achieving design wins, which entails having its existing and future products chosen as the
3D graphics processors for hardware components or subassemblies designed by PC OEMs and add-in board
manufacturers."

The concentration numbers, on the calendar-year basis the stage uses: **1997 — STB 63%, Diamond 31%** (two
customers, 94% of revenue). By the 424B4 the described base is wider and is a different statement about a
different date: products "used by **six of the top ten PC OEMs**—Compaq, Dell, Gateway, IBM, Micron and
Packard Bell NEC as well as by leading motherboard manufacturers such as Intel and leading add-in board
manufacturers such as ASUSTeK, Canopus, Creative, Diamond, ELSA and Leadtek", against the March 1998 S-1's
"**five** of the top ten PC OEMs in the United States--Compaq … Dell … Gateway 2000 … Micron … and Packard
Bell NEC". The five→six change inside ten months is **version evidence** about the customer list, not
corroboration of any single sale.

Two further customer facts, both filed against the company's interest rather than for it: "**Substantially
all of the Company's sales are made on the basis of purchase orders rather than long-term agreements.** As a
result, the Company may commit resources to the production of products without having received advance
purchase commitments from customers"; and the design-win dependency was forward-looking and unhedged — "the
Company's upcoming RIVA128ZX graphics processor **must** be designed into PC OEMs' and add-in board
manufacturers' products in order for the Company to achieve any significant revenue from" it.

### F.2 Independence problem, stated once for the whole section

Every customer name, percentage, and OEM-count statement above comes from **one lineage**: the company's own
registration documents. **No held in-window document from a customer side exists in this corpus** — not an
STB or Diamond purchase record, not an OEM announcement, not a trade-press design-win report. The one
customer-adjacent instrument that *is* third-party-signed, Ex-4.3, is an **investor** agreement (it names
Sega, Itochu, Worldview as shareholders), not a sales contract, and must not be read as customer evidence. A
second independence gap of the same kind sits in §E: ST's side of the strategic collaboration agreement is
nowhere held, so the manufacturing relationship is known only from the company's description of it. The
cheapest routes to an independent carrier are named in `## Untried`: the 1999 SC 13G accessions (institutions
describing Nvidia), the unfetched 10-Qs, and the two blocked periodical families.

### F.3 The first customer is UNKNOWN, and stays so

No held document identifies who bought the first NV1 or booked the first RIVA128 order, in what month, or for
what quantity; the 1995 revenue line is a single total (`$1,182K`), not a customer. **The §10 research-debt
trigger "the first customer is unknown" is therefore open on this company and is written into `data_gaps.csv`
as P1G05 with a follow-up task, not smoothed over with the 1997 concentration percentages**, which describe a
later and entirely different commercial state.

### F.4 Claim records for §F

P1-25 Claim: Two customers accounted for 94% of calendar-1997 revenue, and sales ran through add-in board manufacturers to PC OEMs on purchase orders. — Date: calendar 1997 — Source path: sources/sec/0001012870-98-000618 (Risk Factors) — Source date: 1998-03-06 — Tier: 1 — Class: FACT as disclosed — Passage: "Substantially all of the Company's sales are made on the basis of purchase orders rather than long-term agreements." — Conf: High — Corroboration: 1 lineage — Conflicts: None
P1-26 Claim: The registrant's stated OEM adoption went from five of the top ten (March 1998) to six of the top ten (January 1999) in one registration lineage. — Date: 1998-03-06 → 1999-01-22 — Source path: sources/sec/0001012870-98-000618; sources/sec/0001012870-99-000192 — Source date: 1999-01-22 — Tier: 1 — Class: FOUNDER CLAIM / corporate marketing statement; the version change is FACT — Passage: "NVIDIA's products are used by five of the top ten PC OEMs in the United States--Compaq Computer Corporation ('Compaq'), Dell Computer Corporation ('Dell'), Gateway 2000, Inc. …" — Conf: Medium — Corroboration: 1 lineage — Conflicts: None
P1-27 Claim: No held in-window document from any customer, OEM or supplier side exists, so every §F quantity is single-lineage. — Date: window-wide — Source path: sources/ (whole-corpus enumeration; 31 sec documents, 0 supplier/customer documents) — Source date: 2026-09-26 — Tier: 1 — Class: FACT about the corpus — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High as to the corpus — Corroboration: 0 — Conflicts: None

## Register rows for merge


>>> REGISTER ROWS FOR MERGE <<<
STATUS: WRITTEN 2026-09-26

*Emit-only. **No register CSV on this company was opened, created or edited by this pass** — there are none
at the company root (`company_status`: T3, 0 volumes, 0 register rows) and a merge applies these. `stage` is
the controlled literal **`stage1`** on every row (§13). All `P1x` ids are **dossier-local**; global
`source_id` blocks are minted centrally at merge, and per RD-123 nothing here assumes an id. `independence_note`
carries the §3 lineage finding on every registration row: **the S-1, its six amendments, the 424B4 and the
10-K405s are one registration lineage under SEC File No. 333-47495 and count as ONE source, however many
bytes are on disk.** A value of `not_derived` in `derived_arithmetic` means the cell is intentionally
non-empty. Every quantitative row names its carrier, its basis (calendar vs fiscal, gross vs net, period-end
vs weighted-average, total company vs line) and CONTEMPORANEOUS vs RESTATED.*

### sources.csv — `source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
P1S01,stage1,"P1-01 P1-04 P1-05 P1-07 P1-08 P1-09 P1-10 P1-11 P1-12 P1-13 P1-14 P1-15 P1-17 P1-18 P1-21 P1-22 P1-23 P1-25 P1-26","Form S-1 registration statement, NVIDIA Corporation (California), File No. 333-47495","NVIDIA Corporation; counsel Cooley Godward; auditors KPMG Peat Marwick LLP",securities registration statement,primary,1998-03-06,1998-03-06,2026-09-26,"EDGAR accession 0001012870-98-000618 (SEC File No. 333-47495; FILM 98559482)","sources/sec/0001012870-98-000618_0001012870-98-000618.txt (856,608 B; 122,698 words per _MANIFEST.csv)",1,"MIXED: CONTEMPORANEOUS for 1995-1997 audited figures / registrant-retrospective for 1993-1994 prose",High,"THE SPINE. One lineage with P1S02, P1S03, P1S04; repeats across drafts are version evidence only. Contains third-party-signed exhibits (Ex-3.1, Ex-4.3, Ex-10.11) which are the only non-company prose in-window","PERIOD FROM INCEPTION (APRIL 5, 1993) TO DECEMBER 31, 1993","Earliest Nvidia document on EDGAR; index min filingDate equals this date (P1S05). Cover prints CALIFORNIA (PRIOR TO REINCORPORATION) / DELAWARE (AFTER REINCORPORATION)"
P1S02,stage1,"P1-06 P1-05","Form S-1/A Amendment No. 5 (as filed), NVIDIA Corporation","NVIDIA Corporation",securities registration statement amendment,primary,1998-12-23,1998-12-23,2026-09-26,"EDGAR accession 0001012870-98-003234","sources/sec/0001012870-98-003234_0001012870-98-003234.txt (682,998 B)",1,"RESTATED for calendar 1997 vs P1S01; CONTEMPORANEOUS for the nine months to 1998-10-25",High,"SAME LINEAGE AS P1S01 - never counted as corroboration of it","Operating income (loss)................. (506) (1,351) (6,470) (2,993) (3,459) (4,911) (3,900)","Carries the assumed IPO price of $8.00 per share in footnote (4) where P1S01 prints a literal blank; also the 1998-10-25 headcount of 184"
P1S03,stage1,"P1-01 P1-02 P1-13 P1-24 P1-26","Final IPO prospectus, Form 424B4, NVIDIA Corporation","NVIDIA Corporation; underwriters Morgan Stanley & Co. Incorporated, Hambrecht & Quist, Prudential Securities",statutory prospectus,primary,1999-01-21,1999-01-22,2026-09-26,"EDGAR accession 0001012870-99-000192 (SEC File No. 333-47495; FILM 99509941)","sources/sec/0001012870-99-000192_0001012870-99-000192.txt (394,333 B)",1,"RESTATED 1997 column (matches P1S02); CONTEMPORANEOUS for the nine months to 1998-10-25; registrant-retrospective for 1993-95 narrative",High,"SAME LINEAGE AS P1S01/P1S02. It IS that registration statement, printed final - counting it as a second or third source is the error §3 names","NVIDIA was incorporated in California in April 1993 and reincorporated in Delaware in April 1998.","Cover date January 21, 1999 = the stage close. Header metadata still reads STATE OF INCORPORATION: CA and FISCAL YEAR END: 1231 after the Delaware/January-year changes (see §Boundary 5)"
P1S04,stage1,"§Boundary 4 basis rule; P1Q19","Annual Report on Form 10-K405 for the fiscal year ended January 31, 1999","NVIDIA Corporation; audited by KPMG LLP",periodic annual report,primary,1999-01-31,1999-04-29,2026-09-26,"EDGAR accession 0000929624-99-000772","sources/sec/0000929624-99-000772_0000929624-99-000772.txt (214,347 B)",1,"(PB) for Stage 1 - used only to fix the fiscal-basis rule and the transition-month label, never as Stage-1 narrative",Medium,"Same registrant lineage as P1S01; a LATER audit of the same calendar 1997 year, so it is version evidence about the 1997 column, not independence","the statement of operations data for the years ended December 31, 1996 and 1997, the one month ended January 31, 1998, and the year ended January 31, 1999","Opened this session for the basis question only. FY1999 customer-mix percentages quoted in the probe dossier were NOT re-read by this pass and are not carried"
P1S05,stage1,"§Boundary 3; P1G07","EDGAR submissions index for CIK 0001045810 (NVIDIA CORP)","U.S. Securities and Exchange Commission",regulatory index,primary,1998-03-06,2026-09-23,2026-09-26,"data.sec.gov submissions (via tools/sec_intake.py index)","sources/_index/submissions.csv (2,487 rows; columns filingDate,form,accession,reportDate,primaryDocument,source)",1,FACT-about-the-index,High,"The registrant's own index; it cannot witness anything before its own floor. Measured this pass, not inherited","min filingDate = 1998-03-06; 69 rows in 1993-01-01..2001-12-31; 30 of the 69 have a blank primaryDocument","EDGAR floor is the structural boundary of this stage. Nameless pre-2001 rows are a listing defect, not absence"
P1S06,stage1,"§Header corpus census; P1G07","Stored-document manifest and empty family directories","tools/sec_intake.py output plus this session's directory listing",provenance census,secondary,2026-09-26,2026-09-26,2026-09-26,"local","sources/sec/_MANIFEST.csv (31 rows, all status ok; 7,942,444 B total per research/A3_intake_regrade.md); sources/financials/ (empty); sources/wayback/ (empty)",1,CATALOG-LEVEL OBSERVATION,High,"proves what this pass can cite; proves nothing about the company",NO_VERBATIM_PASSAGE_RECORDED,"Two of the five families are empty directories: (b) web archives UNANSWERED with no negative artifact kept, (a) XBRL series UNANSWERED-by-script because tools/sec_intake.py facts prints a path and writes no file"
P1S07,stage1,"§Boundary 3 families (c)/(d); P1G10","Harvest-mine dossier for this company","tools/harvest_mine.py output, read by this pass",internal dossier,secondary,2026-09-26,2026-09-26,2026-09-26,"local","research/A4_harvest_mine.md; research/A_chronology_feasibility.md; research/A3_intake_regrade.md",4,LEAD ONLY - never counts in a tier verdict,Medium,"A dossier is not a source. Cited here so the merge can see which family verdicts this pass inherited rather than measured","01.-nvidia-annual-reports | 1993-01-01 | in-window | 911,128 | 200 | 8 | nvidia corporation | TIER1_CANDIDATE_TEXT","The item's own text layers run FY2005-FY2026 (probe), and its IA metadata date 1993-04-05 is a scrapeware artifact - the probe's trap note is carried forward unchanged"
```

### quantitative.csv — `company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
Nvidia,stage1,1993,total_revenue,0,USD thousands,P1S01 Summary Financial Data,1998-03-06,FACT as printed,High,not_derived,"CONTEMPORANEOUS audited statement period; basis = inception 1993-04-05 to 1993-12-31 (8 months 26 days), calendar-year column thereafter. Prints as $ --"
Nvidia,stage1,1994,total_revenue,0,USD thousands,P1S01 Summary Financial Data,1998-03-06,FACT as printed,High,not_derived,CONTEMPORANEOUS; calendar year ended 1994-12-31
Nvidia,stage1,1995,total_revenue,1182,USD thousands,P1S01 Summary Financial Data,1998-03-06,FACT as printed,High,not_derived,"CONTEMPORANEOUS and identical in P1S03; the product/royalty split of this 1,182 was not read by this pass and is recorded as P1G09"
Nvidia,stage1,1996,total_revenue,3912,USD thousands,P1S01 Summary Financial Data,1998-03-06,FACT as printed,High,not_derived,"CONTEMPORANEOUS; note this is the year the NV1 was pulled from sale in Q1, so 3,912 is mostly a run-off figure"
Nvidia,stage1,1997,total_revenue,29071,USD thousands,P1S01 and P1S02 and P1S03,1999-01-22,FACT as printed,High,not_derived,"CONTEMPORANEOUS; the one 1997 line that does NOT move across the lineage, which is why the loss movements below are an expense-side story"
Nvidia,stage1,1997,net_loss,3589,USD thousands,P1S02 and P1S03,1999-01-22,"RESTATED (final); basis calendar year",High,not_derived,"CANONICAL 1997 net loss for this corpus. P1K01"
Nvidia,stage1,1997,net_loss_as_first_filed,2691,USD thousands,P1S01,1998-03-06,SUPERSEDED-DRAFT,High,not_derived,"Kept as the March 1998 printing, NOT as a value to carry. The row exists so the movement is auditable"
Nvidia,stage1,1997,operating_loss,3459,USD thousands,P1S02 and P1S03,1999-01-22,"RESTATED; basis calendar year",High,not_derived,"March draft printed (2,560); movement = 899 of additional operating expense, unexplained in any held note. P1K01"
Nvidia,stage1,1997,gross_profit,7827,USD thousands,P1S02 and P1S03,1999-01-22,RESTATED,High,not_derived,"March draft printed 7,845; a 18 difference, i.e. the restatement is overwhelmingly below the gross line"
Nvidia,stage1,1995,gross_profit,367,USD thousands negative,P1S01 and P1S03,1998-03-06,FACT,High,not_derived,"CONTEMPORANEOUS; the only year in the window the company sold product at a NEGATIVE gross margin, and it is the largest net loss of the stage (6,377)"
Nvidia,stage1,1997-12-31,cash_and_equivalents,6551,USD thousands,P1S01 Balance Sheet Data,1998-03-06,"CONTEMPORANEOUS, period-end",High,not_derived,"MD&A rounds it to $6.5 million and adds no outstanding bank indebtedness"
Nvidia,stage1,1998-10-25,cash_and_equivalents,12461,USD thousands,P1S03 Balance Sheet Data,1999-01-22,"CONTEMPORANEOUS, period-end",High,not_derived,"As-adjusted after the offering 49,721; that column is a PRO FORMA, never to be used as an observed balance"
Nvidia,stage1,1997-12-31,total_assets,25038,USD thousands,P1S01 Balance Sheet Data,1998-03-06,"CONTEMPORANEOUS, period-end",Medium,not_derived,"P1S03 prints 25,039 for the same date and equity 6,897 where P1S01 prints 6,896 - a $1K drift inside one lineage, recorded rather than reconciled"
Nvidia,stage1,1998-10-25,accumulated_deficit,17074,USD thousands,P1S03 Capitalization,1999-01-22,"CONTEMPORANEOUS, period-end",High,not_derived,"Against approximately $14.0 million at 1997-12-31 in P1S01; the two are 9.8 months apart and are not one series"
Nvidia,stage1,1993,series_a_preferred_gross_proceeds,2151500,USD,DERIVED from P1S01 Note 3,1998-03-06,DERIVED,High,"4,303,000 shares x $0.50 = 2,151,500 gross; net of $22,000 issuance costs = 2,129,500","Gross vs net stated separately because the filing gives only the net qualifier"
Nvidia,stage1,1997,series_d_preferred_gross_proceeds,7568151,USD,DERIVED from P1S01 Note 3,1998-03-06,DERIVED,High,"1,438,812 shares x $5.26 = 7,568,151 gross; net of $30,000 = 7,538,151","Sold on two dates, 1997-08-19 and 1997-09-12, as one aggregate tranche"
Nvidia,stage1,1997-09-12,series_d_price_vs_series_c,0.79,ratio,P1S01 Note 3,1998-03-06,DERIVED,High,"$5.26 / $6.67 = 0.7886, i.e. 21.1% BELOW the 1995 Series C price","A filed price fact, not a narrative: the fourth round was priced below the third while the company was still loss-making"
Nvidia,stage1,1994,series_b_price_vs_series_a,3.6,ratio,P1S01 Note 3,1998-03-06,DERIVED,High,"$1.80 / $0.50 = 3.6x the founding round's price","The only in-window market test of the idea between 1993 and 1995 that the filings preserve"
Nvidia,stage1,1997-12-31,private_preferred_total_stated_vs_ladder_sum,19700000,USD,P1S01 MD&A and Note 3,1998-03-06,FACT and DERIVED check,High,"Sum of the five stated round grosses = 2,151,500 + 4,303,496 + 750,001 + 5,002,500 + 7,568,151 = 19,775,648 gross; less stated issuance costs of 123,000 = 19,652,648, i.e. the filed $19.7 million foots against the ladder to under $50K","Internal arithmetic consistency only - same lineage, so it corroborates nothing outside the filing. It does show the ladder is COMPLETE: no unnamed round is needed to reach $19.7M"
Nvidia,stage1,1997-09-28,employees,71,headcount at period-end,P1S02 and P1S03,1999-01-22,CONTEMPORANEOUS,High,not_derived,"Population = total employees at a fiscal period-end, NOT a calendar year-end and NOT average"
Nvidia,stage1,1997-12-31,employees,92,headcount at period-end,P1S01 Employees,1998-03-06,CONTEMPORANEOUS,High,not_derived,"62 engineering + 30 sales/marketing/operations/administrative. Do not write 1997 headcount bare: 71 at 1997-09-28 and 92 at 1997-12-31 are both 1997. P1K04"
Nvidia,stage1,1998-10-25,employees,184,headcount at period-end,P1S02 and P1S03,1999-01-22,CONTEMPORANEOUS,High,not_derived,Compare 42 at 1996-12-31 (P1S01)
Nvidia,stage1,1997,customer_concentration_top_two,94,percent of total revenue,P1S01 Risk Factors,1998-03-06,FACT as disclosed,High,"STB 63% + Diamond 31% = 94% of calendar-1997 revenue","Two add-in board manufacturers, not two end customers; STB and Diamond are the buyers, PC OEMs are the design wins behind them"
Nvidia,stage1,1997,royalty_revenue_from_ST,6,percent of total revenue,P1S01 Risk Factors,1998-03-06,FACT as disclosed,High,not_derived,"ST was simultaneously manufacturer, licensee and reseller of RIVA128 - one counterparty wearing three hats"
Nvidia,stage1,1997-12-31,net_income_first_profitable_quarter,stated,qualitative,P1S01 Risk Factors,1998-03-06,FACT as disclosed,Medium,not_derived,"Exact wording: the Company generated net income in the quarter ended December 31, 1997 while incurring significant losses in each other quarter of 1997; no quarterly dollar amount was read by this pass"
Nvidia,stage1,1997-09-30,product_revenue_quarter,5.2,USD millions,P1S01 MD&A,1998-03-06,FACT as printed,High,not_derived,"Q3 1997, from less than $100,000 in each of the first two quarters of 1997; Q4 1997 22.1 million"
Nvidia,stage1,1998-10-25,mandatorily_convertible_notes,11000,USD thousands,P1S03 Capitalization,1999-01-22,"CONTEMPORANEOUS, period-end",High,not_derived,"Converted automatically into 1,571,429 common shares on 1999-01-15 per the same footnote; the note's own pricing was not read"
Nvidia,stage1,1999-01-21,ipo_shares_offered,3500000,shares,P1S03 The Offering,1999-01-22,FACT,High,not_derived,"All sold by the Company (primary); 28,595,976 shares to be outstanding after the offering. No IPO price per share was read by this pass - P1S02's pro forma assumes $8.00 and P1S01's equivalent footnote is a literal blank"
Nvidia,stage1,1995-03-01,sublease_base_rent_annual,341190,USD per year,P1S01 Ex-10.11,1998-03-06,CONTEMPORANEOUS contract term,High,not_derived,"$28,432.50 monthly; 432 Lakeside Drive, Sunnyvale; sublessor Amdahl Corporation, landlord Oakmead Investments (a general partnership); term 30 months to 1997-08-31"
Nvidia,stage1,1995-02-16,sublet_space,29100,rentable square feet charged as 27875,P1S01 Ex-10.11,1998-03-06,CONTEMPORANEOUS contract term,High,not_derived,"A later amendment expands to approximately 34,251 rsf charged as 33,026; the two pairs are different dates of one premises and must never be averaged"
```

### timeline.csv — `company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
Nvidia,stage1,1993-04-05,"Inception, as the audited statement-period label prints it","NVIDIA Corporation (California)","Sunnyvale, California",P1S01,FACT about the audited header; registrant-retrospective about the event,High,None,"The earliest date any held Tier-1 carrier attaches to this company. Nothing in the corpus dates the decision to found (P1G01)"
Nvidia,stage1,1993,"Sold 4,303,000 Series A preferred shares at $0.50, net of $22,000 of issuance costs","the Company; purchasers UNNAMED",UNKNOWN,P1S01,FACT as disclosed,Medium,None,"Year-only date per §13 partial-date rule. Purchaser identities are P1G02 and are the single highest-value gap in the stage"
Nvidia,stage1,1993-06,"Tench Coxe (Sutter Hill Ventures) and Mark A. Stevens (Sequoia Capital) become directors","Coxe; Stevens",UNKNOWN,P1S01,registrant-retrospective FACT as disclosed,Medium,None,"Weeks after inception; the only sign of outside capital inside the founding year. bios also date Stevens's Sequoia general-partnership appointment to March 1993"
Nvidia,stage1,1993-11,"Harvey C. Jones, Jr. becomes a director","Jones",UNKNOWN,P1S01,registrant-retrospective,Medium,None,Jones also appears as a personal signatory on the 1997 Ex-4.3 shareholder pages
Nvidia,stage1,1994,"Sold 2,390,831 Series B preferred shares at $1.80, net of $57,000","the Company; Sequoia and Sutter Hill named as parties to the December 1994 agreement they descend from",UNKNOWN,P1S01,FACT as disclosed,Medium,None,"Price 3.6x the 1993 round"
Nvidia,stage1,1994-12-19,"Original Investors' Rights Agreement entered into - the earliest in-window date attached to named outside investors anywhere held","the Company; JAFCO, Sequoia and Sutter Hill entities, others",UNKNOWN,P1S01,FACT (recital in a counterparty-signed instrument),High,None,"Recited inside Ex-4.3 (1997). The instrument itself of 1994 is NOT held; only its recital and its successors' signature pages are"
Nvidia,stage1,1995-01-23,"Amendment Number One to the Investors' Rights Agreement","the Company and the Shareholders",UNKNOWN,P1S01,FACT (recital),High,None,Same recital chain
Nvidia,stage1,1995-02-16,"Sublease Agreement with Amdahl Corporation for 432 Lakeside Drive, Sunnyvale; amended 1995-03-01 and 1995-09-01","NVIDIA Corporation; Amdahl Corporation; landlord Oakmead Investments","Sunnyvale, California",P1S01,CONTEMPORANEOUS contract,High,None,"Third-party-dated facility evidence. The exhibit's defined-terms header prints label/value drift, so roles are taken from the operative paragraphs"
Nvidia,stage1,1995-05,"First product, the NV1, introduced","the Company","Sunnyvale, California",P1S01 and P1S03,FACT as disclosed,High,None,"Two years and one month after inception. No launch collateral, datasheet or press item is held (P1G09)"
Nvidia,stage1,1995,"Sold 416,667 further Series B shares at $1.80 and 750,000 Series C at $6.67 net of $14,000","the Company",UNKNOWN,P1S01,FACT as disclosed,Medium,None,"The Series C price is the 1995 peak against which the 1997 down round is measured"
Nvidia,stage1,1996-03-31,"NV1 sales stopped in the first quarter of 1996; NV2 console development ceased; RIVA128 development began","the Company",UNKNOWN,P1S01 and P1S03,FACT as disclosed,High,P1K03,"DISPATCH-PREMISE CORRECTION: the probe dossier rendered this quarter as 1997. Both held drafts print 1996"
Nvidia,stage1,1997-08-19,"Second Amended and Restated Investors' Rights Agreement executed; Company signed by Jen-Hsun Huang, President","the Company and the Shareholders including Sega Enterprises, Ltd., Itochu, Worldview Technology Partners I, JAFCO, Sequoia and Sutter Hill entities",UNKNOWN,P1S01,FACT (third-party-signed instrument),High,None,"The single best documentary carrier of the private period in the corpus"
Nvidia,stage1,"1997-08-19; 1997-09-12","Sold 1,438,812 Series D preferred shares at $5.26, net of $30,000 - priced 21% below the 1995 Series C","the Company",UNKNOWN,P1S01,FACT as disclosed,High,None,"Filed price fact about how hard the middle years were; needs no retrospective narrative"
Nvidia,stage1,1997-08,"RIVA128 graphics processor introduced; commercial shipment and first revenue of the current product line in the third quarter of 1997","the Company; ST Microelectronics as manufacturer and licensee","Sunnyvale, California",P1S01,FACT as disclosed,High,None,"Company assertion of a first-in-family design; no independent launch coverage held"
Nvidia,stage1,1997-12,"Low manufacturing yields at ST, the quarter the company first reported net income","the Company; ST Microelectronics","Crolles, France",P1S01,FACT (self-disclosed negative),High,None,"The only incurred operational failure inside the window on this evidence"
Nvidia,stage1,1998-01-31,"Fiscal year-end changed to a 52/53-week year ending the last Sunday in January; prior December-31 periods not restated","the Company",UNKNOWN,P1S03 and P1S04,FACT,High,P1K05,"Every 1993-1997 figure in this volume sits on the pre-change calendar basis"
Nvidia,stage1,1998-02-23,"Certificate of Incorporation of NVIDIA Delaware Corporation subscribed by sole incorporator Mitchell R. Truelock of Cooley Godward LLP","Truelock","Wilmington, Delaware",P1S01,FACT (executed constitutive document),High,P1K02,"A shell for a reincorporation announced as prospective; the operative amended charter in the same filing is still a blank-dated form"
Nvidia,stage1,1998-03-06,"Form S-1 filed, File No. 333-47495; offering price in its own pro forma footnote left blank","the Company; underwriters named in later drafts","Sunnyvale, California",P1S01 and P1S05,FACT,High,None,"EDGAR floor for this registrant and the end of the structural silence"
Nvidia,stage1,1998-05-07,"Two Form RW (registration withdrawal) filings appear in the index in the same month as an amendment","the Company",UNKNOWN,P1S05,FACT-about-the-index only,Medium,P1G10,"Indexed, never fetched; an unexplained withdrawal inside the stage and the clearest example of a named UNTRIED event, not a null"
Nvidia,stage1,1998-10-25,"Period-end used for the last Stage-1 balance sheet and headcount (184 employees); mandatorily convertible notes of $11.0M outstanding","the Company",UNKNOWN,P1S02 and P1S03,CONTEMPORANEOUS,High,None,"The last measured state inside the window"
Nvidia,stage1,1999-01-21,"Final prospectus dated; 3,500,000 primary shares; Nasdaq symbol NVDA; closing on or about 1999-01-27","the Company; Morgan Stanley, Hambrecht & Quist, Prudential Securities",UNKNOWN,P1S03,FACT,High,None,"STAGE 1 CLOSES HERE. Everything after is (PB)"
```

### decisions.csv — `company,stage,date,decision,state_before,information_available,unknowns,alternatives,constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date,decision,state_before,information_available,unknowns,alternatives,constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref
Nvidia,stage1,1993,"Build a proprietary 3D standard rather than design to an emerging published API","no product, no revenue, three founders and a $0.50 preferred round","that no 3D industry standard yet existed; that its own technology could become one; the founders' prior work on single-chip graphics accelerators at Sun","who decided, what was weighed, what was rejected - nothing in any held document","NONE PRINTED in any held in-window document","a founding round priced at $0.50 per share and whatever the founders themselves contributed, which is not stated anywhere held","the company's own later framing only: developed in the absence of industry standards with the goal of establishing the Company's proprietary NV technology as a 3D graphics standard","a proprietary standard adopted as the market's","The NV1 was introduced in May 1995 and its sales stopped in the first quarter of 1996; the company ceased NV2 development and re-architected to Direct3D - all stated by the registrant in 1998",P1S01,Low,"P1-14 P1-15 P1-17"
Nvidia,stage1,1996,"Abandon the console-targeted line and re-architect to Microsoft's Direct3D for the mainstream PC","NV1 sales collapsing; NV2 in development; a $3,912K calendar year about to end","that the PC industry had by the end of 1996 broadly adopted Direct3D and OpenGL, per the company's own sentence","the decision date, the internal debate, the cost already sunk in the cancelled NV2, whether any alternative platform was considered","whether staying on the proprietary path was ever costed; no alternative is printed","cash used in operations of $6.1M in 1995 and $300K in 1996; total assets of $5,525K at 1996-12-31; a $2,500K development advance still on the balance sheet","the market had chosen APIs and the company had no other product line","a single-chip 3D and 2D part competitive on price that OEMs would design in","RIVA128 introduced August 1997; first revenue of the current line in Q3 1997; product revenue $5.2M then $22.1M in Q3 and Q4 1997 - inside the stage, not (PB)",P1S01 and P1S03,Medium,"P1-19 P1-21"
Nvidia,stage1,1997-09-12,"Raise the Series D at $5.26 per share, below the 1995 Series C price of $6.67","loss-making on every full period; two customers at 94% of 1997 revenue; the new product shipping weeks earlier","its own cash position and burn as reported: $1.2M used in operations in 1997, $6.5M held at year-end, no bank indebtedness","how much was sought, how much the negotiation moved, who set the price, whether a higher price was attempted","UNKNOWN - no competing financing path is printed in any held in-window document","no collateral base beyond a subleased facility; equipment lease financing is named as a minor source","no rationale for the price is printed anywhere in the corpus","funding to reach volume production before the next product generation","completed: 1,438,812 shares sold on two dates for $7,568,151 gross, net of $30,000; the company then sold $11.0M of mandatorily convertible notes in 1998 and filed the S-1 on 1998-03-06",P1S01 and P1S03,Medium,"P1-10"
```

### validation.csv and failures.csv — `company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes
Nvidia,stage1,1994,"Series B priced at $1.80 against the 1993 round's $0.50","3.6x the prior price","that one set of outside investors paid materially more for the same company in year two","anything about customers, product or market - a private price between related instruments, in the company's own recital",P1S01,CONTEMPORANEOUS as disclosed (retrospective as to 1993),Medium,"the strongest validation signal for 1993-94 available at this reach, and it is a financing fact not a demand fact"
Nvidia,stage1,1995-05,"First product shipped","NV1; revenue of $1,182K in 1995","that the company could take a design from concept to a saleable part","whether anyone wanted it: the same document records gross profit of $(367)K in 1995 and the product's withdrawal in Q1 1996",P1S01,CONTEMPORANEOUS,High,"a negative-margin first year is the recorded result, not a footnote"
Nvidia,stage1,1997-09-30,"First revenue from the re-architected product line","$5.2M in Q3 1997 from under $100K in each of the two prior quarters","that the pivot sold, in volume, immediately","durability, margin, or independence from two buyers; and it says nothing about whether the design wins would repeat",P1S01,CONTEMPORANEOUS,High,"the quarterly table in P1S01 exists and was not read past the sentence quoted; the four-quarter 1997 detail is UNTRIED item 1"
Nvidia,stage1,1997-12-31,"First net income in a quarter","one quarter of 1997, amount not read by this pass","that unit economics could turn positive at existing scale","that the company was profitable - the year printed a net loss of $(3,589)K and the nine months to 1998-10-25 still printed an operating loss of $(3,900)K",P1S01,CONTEMPORANEOUS,Medium,"the quarterly dollar figures behind this sentence were not read by this pass; the S-1's own quarterly table exists and is UNTRIED item 1""deliberately not used as a stage boundary (§Boundary 2, candidate 3)"
Nvidia,stage1,1997-08-19,"Counterparty-signed investors' rights agreement with named institutional and strategic holders","signatories include JAFCO, eight Sequoia vehicles, Sutter Hill Ventures, ANVEST, Worldview, Itochu, Sega Enterprises Ltd","that identifiable third parties had enforceable equity rights in the private company and contracted for information and inspection","who bought the 1993 round, what they paid per holder, or whether any signatory was a customer",P1S01,"CONTEMPORANEOUS, third-party signed",High,"the only in-window document in this corpus that is not company prose"
Nvidia,stage1,1995,"Gross margin negative on its only product year","gross loss $(367)K on revenue $1,182K","that the first commercial attempt lost money on every unit sold at the reported level","whether the cause was price, yield, or inventory write-down - none is printed",P1S01,CONTEMPORANEOUS,High,"candidate component of the 1997 restatement question; kept as a question"
Nvidia,stage1,1996-03-31,"First product discontinued and second product cancelled","NV1 sales stopped; NV2 development ceased","that the company's founding architectural bet failed inside three years of shipping","that the founders were right to change course, and when the change was decided; the filing's own causal sentence puts adoption after the withdrawal",P1S01 and P1S03,CONTEMPORANEOUS,High,P1K03
Nvidia,stage1,1997-12,"Manufacturing failure at the sole supplier","low yields at ST Microelectronics","that the company's whole supply position was single-threaded at the moment it first earned money","the dollar cost, which is not printed",P1S01,CONTEMPORANEOUS self-disclosed,High,"the only incurred operational failure inside the window"
Nvidia,stage1,1997,"Customer concentration","STB 63% and Diamond 31% of revenue","extreme dependence on two buyers on purchase orders rather than contracts","that those buyers were secure, or that the concentration was not about to change (the FY1999 mix is (PB))",P1S01,CONTEMPORANEOUS,High,"both percentages are the company's own disclosure for calendar 1997; no customer-side confirmation of either figure is held anywhere in the corpus"
Nvidia,stage1,1997-09-12,"Down-priced equity round","Series D at $5.26 vs Series C at $6.67","that at least one 1997 financing cleared below the 1995 price","why, and whether more was sought than obtained",P1S01,CONTEMPORANEOUS,Medium,"the single most useful filed datum against reading the middle years as inevitable"
```

### channels.csv — `company,stage,channel,date_tested,why_tested,cost_or_effort,result,repeatability,source_id,confidence,notes`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,channel,date_tested,why_tested,cost_or_effort,result,repeatability,source_id,confidence,notes
Nvidia,stage1,"add-in board manufacturers as direct customers",1995,"the only route to PC OEM sockets without a sales organisation","UNKNOWN - no channel cost is broken out in any held draft","94% of calendar-1997 revenue through two AIB houses (STB, Diamond)","UNKNOWN within the window; the FY1999 four-customer mix is (PB) and is not used here",P1S01,Medium,"sales are on purchase orders, not agreements, so the channel is re-won every quarter by the company's own account"
Nvidia,stage1,"the manufacturer as licensee and reseller (ST Microelectronics)",1997,"to convert capacity into distribution at the same time","royalty-based, rate not printed","ST sales of RIVA128 generated 6% of total revenue in 1997 and the two parties jointly filed the RIVA128 trademark","single counterparty; also the sole manufacturing source, so the channel and the supply risk are one exposure",P1S01,High,"the most distinctive channel fact in the window and the least corroborated - ST's side is not held"
Nvidia,stage1,"PC OEM design wins as the demand mechanism",1997,"because AIB sales follow OEM choices","UNKNOWN - engineering and FAE effort is not separated","products used by five of the top ten US PC OEMs (March 1998 draft) and six plus Intel as a motherboard maker (January 1999 draft)","UNKNOWN; the company states the RIVA128ZX must be designed in to produce significant revenue at all",P1S01 and P1S03,Medium,"five-to-six is version evidence about the marketing sentence, not about a new customer"
```

### conflicts.csv — `company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
Nvidia,stage1,P1K01,"A.1; A.4 P1-06; §Boundary 5","Calendar 1997 net loss was $(2,691)K, operating loss $(2,560)K, gross profit $7,845K, and both drafts present the 1995-1997 rows as audited by KPMG Peat Marwick","P1S01 Summary Financial Data",1998-03-06,"Calendar 1997 net loss $(3,589)K, operating loss $(3,459)K, gross profit $7,827K, revenue unchanged at $29,071K","P1S02 and P1S03",1999-01-22,"The same audited year's expense rows moved by ~$899K of operating expense between two drafts of one registration lineage while every revenue and 1993-1996 row stayed identical. No note in any held draft explains it","Both are the same instrument at two dates. The later one is the one that was declared effective and sold, and the FY1999 10-K405 carries the later basis forward, so side B outranks side A","Carry $(3,589)K / $(3,459)K / $7,827K as canonical and keep the March printings in the register as SUPERSEDED-DRAFT rows so the movement stays auditable. A $4.3M 1997 deferred-compensation charge is a named MECHANISM CANDIDATE, marked INFERENCE, because $4.3M does not equal the $898K net movement and no text links them","whether the change was an audit adjustment, a reclassification into cost of sales vs operating expense, or a stock-compensation true-up is UNKNOWN. The 1997 balance sheet also drifted $1K on two lines, which is unreconciled",High
Nvidia,stage1,P1K02,"§Boundary 1","NVIDIA reincorporated in Delaware in April 1998","P1S03",1999-01-22,"The Delaware certificate of incorporation was subscribed 23 February 1998, and the amended and restated charter attached to the March 1998 S-1 has an execution date left blank (this ____ day of ______, 1998)","P1S01 Exhibits 3.1 and 3.1-A",1998-03-06,"The probe recorded this as a February-vs-April contradiction. Re-read this pass, it is a sequence, not a conflict: formation of the vehicle and effectiveness of the swap are different acts","The executed 1998-02-23 certificate is a constitutive document and outranks prose; the blank-dated form proves the reincorporation was incomplete at filing, exactly as the March cover states (CALIFORNIA PRIOR TO REINCORPORATION / DELAWARE AFTER REINCORPORATION)","The Delaware vehicle was formed 1998-02-23; the California company remained the registrant on 1998-03-06; the swap and the A&R charter became operative later in 1998. April 1998 is the company's own date for the operative step and is recorded as registrant-retrospective","the operative date of the reincorporation and of the share exchange is UNKNOWN from held bytes; the stockholder written consents of 1999-01-06 recorded in the probe dossier were not re-read here",High
Nvidia,stage1,P1K03,"C.1; D.3; E.1","By the end of 1996 the PC industry had broadly adopted Direct3D and OpenGL, and as a result the company experienced a significant reduction in NV1 revenue","P1S01 and P1S03, identical sentence",1998-03-06,"The company stopped selling the NV1 in the first quarter of 1996","same sentence, same two documents",1998-03-06,"The stated cause is dated after the stated effect: an industry condition recognised by the end of 1996 cannot alone explain a withdrawal executed by March 1996","Neither side is a rival claim; they are one sentence that cannot carry the causality it asserts. The ordering anomaly survives across every draft of the lineage, so it is not a transcription artifact of this pass","The registrant's retrospective causal account is usable as an in-period company belief and NOT as evidence that the standard-settling caused the withdrawal. Whatever reduced NV1 sales was underway before 1996-03-31; Direct3D and OpenGL adoption is dated by the company itself to later in that year","whether the withdrawal was driven by demand, by a platform/customer decision, by inventory, or by a design defect is UNKNOWN; no held document says",High
Nvidia,stage1,P1K04,"A.1; B.4","92 employees at 1997-12-31 and 42 at 1996-12-31","P1S01",1998-03-06,"184 employees at 1998-10-25 and 71 at 1997-09-28","P1S02 and P1S03",1999-01-22,"Four different measurement dates inside two adjacent fiscal regimes, one of them a fiscal period-end the company switched on 1998-01-31","Not a contradiction at all - a mis-citation trap. Both are true of the dates each names","Every headcount row in this volume carries its own date and population (total vs the separate R&D-only counts in later filings, which are (PB) for our purposes and were not read here)","none on the figures; the risk is entirely in how they get quoted",High
Nvidia,stage1,P1K05,"§Boundary 4","The audited transition period is the one month ended January 31, 1998","P1S03 and P1S04",1999-01-22,"The same prospectus also prints selected statement of operations data for the one month ended January 26, 1997 as derived from unaudited statements","P1S03 footnote",1999-01-22,"A one-month period dated 1997 appears in a footnote while the document's own summary table carries no such column and the audited transition month is dated a year later","The dated-1998 form appears in two independent documents (the prospectus and the FY1999 annual report); the dated-1997 form appears once, with no matching column","Treat January 31, 1998 as the transition month. Record the January 26, 1997 string verbatim, use it for nothing, and note that a mis-set year in the footnote is the most likely reading - itself an INFERENCE","what period the footnote denotes is UNKNOWN; it may be a typographical error in the filing, and this corpus cannot see the compiler's intent",Medium
Nvidia,stage1,P1K06,"E.3","The Company's products have received over 40 awards from recognized industry publications","P1S01",1998-03-06,"over 180 awards, same sentence frame, same publication list","P1S03",1999-01-22,"A 4.5x escalation of an unverifiable marketing count in ten months of one registration lineage","Neither is auditable; no award list, certificate or publication is held. The escalation is the finding, not either number","Both are FOUNDER CLAIM / corporate marketing statements and are classified as such wherever they appear. Any inference of product-quality trajectory drawn from the change is inadmissible in this corpus","how many actual awards existed at either date is UNKNOWN",Medium
Nvidia,stage1,P1K07,"§Boundary 6 (all four)","Dossier premises: NV1 sold until Q1 1997; sublease with Amahl dated 1998-02-02 over 34,251/33,026 rsf; 1997 net loss not claimed","research/A_chronology_feasibility.md",2026-09-25,"Held bytes: NV1 sales stopped Q1 1996; sublease with Amdahl Corporation dated February 16, 1995 over 29,100 rsf charged as 27,875 (later amended to 34,251/33,026); 1997 net loss moved from (2,691) to (3,589)","P1S01 and P1S03",1998-03-06,"A prior pass's bracketed reconstruction and mis-transcriptions were inherited into the dispatch brief for this pass as premises","The documents outrank the dossier outright; every correction above is a first-hand read of stored bytes in this session","Register-level: dossier prose is not evidence, and a bracketed year that fills a gap in a quoted sentence is the most dangerous single artefact of a reading pass. This conflict row exists so the merge does not carry the older numbers forward","whether other probe readings not re-checked by this pass (FY1999 customer mix, RW withdrawal, convertible-note dates) are accurate is UNTESTED here and named in Untried",High
```

### data_gaps.csv — `company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task`


>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task
Nvidia,stage1,"the date, place and terms of the founders' agreement to start the company, and the first office and first employee",no held document of any family records the founding act itself; the constitutive 1993 California instrument is not filed on EDGAR,High,"three identical registrant sentences placing the co-founding in April 1993, and the audited statement period beginning 1993-04-05",Low,"UNTRIED-7 family (e) documentary: California Secretary of State business search for NVIDIA Corporation 1993, and Santa Clara County records"
Nvidia,stage1,identity of the 1993 Series A purchasers at $0.50,not stated in any held document; the investors' rights agreement held only descends from a December 1994 original,High,"Sequoia and Sutter Hill partners seated on the board from June 1993 and named as signatories from December 1994",Medium,"UNTRIED-1 unfetched in-window accessions and UNTRIED-7; do not infer purchasers from board seats"
Nvidia,stage1,any carrier for the near-death / cash-runway recollection,"zero hits in the S-1 and 424B4 for the rescue phrasings listed in §D.4; no interview or trade-press body of 1995-1999 is held",High,"the filed distress facts only: zero revenue 1993-94, negative 1995 gross margin, $6.4M 1995 operating loss, down-priced 1997 round, $6.5M cash at 1997-12-31",Medium,"UNTRIED-3/4/5/6 periodicals and Wayback. Whatever is fetched must be classified FOUNDER CLAIM / retrospective memory and dated to the interview"
Nvidia,stage1,"counterparty and terms behind the $2,500K advance on development agreement and the higher deferred contract funding of 1996",the balance-sheet line and the MD&A sentence are held; the underlying contract is not,High,"Advances on development agreement $2,500 at 1996-12-31 and 1997-12-31 (P1S01 Note 2)",Medium,"re-read the exhibit tables of every held S-1/A for a development agreement with a named counterparty; this is the cheapest unmined fact in the stage"
Nvidia,stage1,who the first paying customer was and what the first order was,"revenue is printed only as annual and quarterly totals; no customer-level sale, invoice or press release is held",High,"STB 63% / Diamond 31% for calendar 1997, which describes a later commercial state entirely",Low,"UNTRIED-4/5/6; the §10 research-debt trigger first customer is unknown is OPEN on this company"
Nvidia,stage1,"the 1993 California certificate of incorporation, bylaws, and the Series A purchase agreement and stubs",only the Delaware instruments of 1998 were filed,High,"the S-1 cover's CALIFORNIA (PRIOR TO REINCORPORATION) entry and the Ex-4.3 recital NVIDIA CORPORATION a California corporation",Medium,UNTRIED-7 family (e) documentary; this gap is what keeps the origin a founder claim rather than a signed article
Nvidia,stage1,"an XBRL or machine-readable early financial series",tools/sec_intake.py facts prints a path and writes no file; sources/financials/ is empty (verified by listing this session),Medium,"the audited headers inside P1S01/P1S03, which this pass transcribed by hand",High,"re-run facts after the script defect is fixed; until then every financial figure in this volume is a hand read and should be re-checked by the merge against the same line"
Nvidia,stage1,"a customer-side or supplier-side document, and any independent count behind any 1993-1997 figure","every in-window figure traces to one registration lineage; the ST agreement, the console relationship and the AIB purchases are known only from Nvidia's own description",High,"the two third-party-signed exhibits inside P1S01 (Ex-4.3 signature pages; Ex-10.11 sublease)",High,"UNTRIED-1 the SC 13G accessions of 1999-08-06 and 2000-10-10 (institutions describing the company, already inside family (a)) and UNTRIED-3/4/5/6"
Nvidia,stage1,"in-window product detail: unit volumes, prices, NV1 die/datasheet, NV2's platform, the 1995 product/royalty split",no datasheet or trade-press body is held; the only award counts are the company's own marketing claims,Medium,"the product sentences in §E.1 and the quarterly revenue split in §A.1",Medium,UNTRIED-4/5/6 periodical and Wayback routes; UNTRIED-2 the unfetched S-1/A amendments whose exhibits may carry them
Nvidia,stage1,"what the two 1998-05-07 RW withdrawals withdrew",indexed in P1S05 and never fetched,Medium,"the index rows alone: form RW, 1998-05-07, two accessions",Low,"UNTRIED-1: fetch and read them. A withdrawal inside a live registration is an event, not a null"
```

**Row count requested: 91** — sources 7 · quantitative 30 · timeline 21 · decisions 3 ·
**validation 5 + failures 5** (one shared column list per §13; rows 1–5 are `validation.csv`, rows 6–10
`failures.csv`) · channels 3 · conflicts 7 · data_gaps 10. Every block was written from a line opened in this
session; nothing was carried from a dossier without re-reading it, and the four places where the dossier and
the bytes disagree are P1K07. **No row here assumes a global `source_id` (RD-123): minting is the merge's.**
Every block was re-parsed through a CSV reader after writing: 0 rows with column drift, 0 empty cells,
`stage` = `stage1` on all 91 rows (§13 register vocabulary).

---

#

> **[MERGE 2026-09-30 -- END OF VOLUME 1] Part 1 stops here, mid-heading, at 15,962 words as emitted. Header, Boundary 1-7 and sections A-F are present and complete; the untried-route block its prose presupposes is absent (COR-03, and the data_gaps.csv row minted by this merge). Volume 2 begins at the next line with the part 2 title and carries sections G-U, its register emission and the eleven-route list.**

---

# VOLUME 2 -- carried verbatim from `_parts/s1_p2.md` (sections G-U, the emission blocks and the untried list)

# NVIDIA — Stage 1 (1993 inception – 1999 IPO) — part 2: §G–§U

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-29T17:56:19Z; claimed by agent nvidia-s1-p2. -->

## Header (part 2)

STATUS: WRITTEN 2026-09-26 (agent `nvidia-s1-p2`; every passage quoted here was opened in this session, and
each is cited by accession file and line so the next reader can re-find it without re-grepping the corpus)

**What this volume is.** Part 2 of Stage 1, continuing `_parts/s1_p1.md` (Header, Boundary, §A–§F, 27 claim
records `P1-01`…`P1-27`, 91 register rows). Section letters, claim-record numbers and register tags run
**continuously**: this volume writes **§G–§U**, its own load-bearing claim records (`P1-28` onward), and a
second emission of register rows for merge. Nothing in part 1 is renumbered, re-titled or edited here; where
this pass's bytes contradict part 1, the contradiction is written as a conflict row in §R and a correction
note, never as a silent overwrite. **Volume plan change:** part 1's header projected "p2 = G–P; p3 = Q–U +
appendix". The dispatch for this pass assigns **§G–§U to this volume**, so a p3 is no longer assumed for the
narrative; the claim-record appendix continues to be written inline per section, as in part 1, under the
same `P1-nn` series. Cross-references keep part 1's form: `(Nvidia S1 §D.4, part_1)`.

**Frame note (§7 "adapt, never delete").** The §7 template letters do not map one-to-one onto a fabless
silicon supplier, and the dispatch brief for this volume re-assigns them deliberately: §G answers the
template's *Customer*/**Supply-and-host** boundary as **channels** (who sold, who bought, who financed, and
through what intermediaries); §H answers *Market as knowable in-period* plus **Competition**; §I answers
*Supply/host side* as **scaling decisions**; §J answers *Money*; §K is the template's **Data gaps**; §L is the
hindsight firewall; §M is the **quantitative table** with carrier and basis carried on every figure; §N is
the **time audit**; §O is **Negative signals/failures**; §P is **Founder decisions with documented
alternatives**; §Q is **consequences and the end-of-stage snapshot**; §R continues the **conflicting
evidence** series part 1 opened; §S is the **fiscal/reporting basis** section the 52/53-week change makes
mandatory for this registrant; §T is the **provenance and independence ledger**; §U is this volume's anchor
block. The template's *Technology* slot is answered inside §E (part 1) and §I here, because for this company
the architecture choice and the manufacturing choice are one decision recorded in one document.

**Standing rules inherited and enforced here (§3 filing-lineage rule; RD-124; RD-127).** (i) The S-1 of
1998-03-06, its six amendments held on disk, the 424B4 of 1999-01-22 and the FY1999 10-K405 are **one
registration lineage**: seven stored drafts of one instrument under SEC File No. 333-47495. Repetition across
them is **version evidence**, never corroboration. (ii) A digitised second copy of the same document is a
replication, not a second source. (iii) Dates for an instrument come from the **filing index**
(`sources/_index/submissions.csv`, whose columns are `filingDate,form,accession,reportDate,primaryDocument,
source` — enumerated before use, per RD-124's fourth-pass lesson) and from the stored `_MANIFEST.csv`
(`accession,file,path,bytes,words,status,form,filingDate,url,listing`), **never** from a filename or listing
order. (iv) A text hit is not a naming: the one entity-bearing periodical item in this company's dossier is
classified `TIER1_CANDIDATE_TEXT` by the harvester and carries text layers of FY2005–FY2026 (part 1 §
Boundary 3), so it is cited here as a pointer, never as in-window evidence. (v) Every value below carries
**carrier** (which accession, which table, which line) and **basis** (calendar vs fiscal, total vs product
revenue, audited vs unaudited, period-end vs weighted-average). (vi) EMPTY means searched and perimeted;
UNANSWERED means bytes were not reached (403/404/429/zero); UNTRIED means never attempted — and the three
states are kept distinct everywhere in this volume.

**Hindsight firewall statement for this volume (§2).** Nothing here treats the RIVA128's revenue turn, the
1999 listing, or the registrant's later position as evidence that the 1993 proprietary-standard bet, the
1996 abandonment, the 1997 down round, the 1998 foundry migration, or the customer-financed notes were
correct or inevitable. The two named paths not taken in §H and §P are written from what the company could
say in 1998–99 and from dated contracts, not from what happened. Post-1999-01-21 material is `(PB)`, may be
used only to date a silence, name a route, or show what the company later said, and is labelled
RETROSPECTIVE SOURCE at each use. The words "visionary", "prescient" and "legendary" do not occur.
**Record-selection null, restated for these sections:** the corpus is one survivor's registration file. What
the archive therefore cannot show is the *rejected* option in any of these decisions, the internal argument
for any of them, any competitor's contemporaneous view of Nvidia, any customer's own sales record, and any
independent count behind any 1993–1998 figure. §K and §T carry that null item by item rather than once.

---

## G

STATUS: WRITTEN 2026-09-26

**§10 trigger status.** Part 1 left the research-debt trigger "the first customer is unknown" OPEN
(`(Nvidia S1 §F.3, part_1)`, `data_gaps.csv` row P1G05). This pass re-tested it against held bytes rather
than inheriting it, and the trigger **remains open but is materially narrower**: the corpus does name who
took nearly all of the company's first two revenue years, and it does not name who placed the first order.
The searches are recorded below as an EMPTY with its perimetre, which is a different statement from
UNANSWERED and from UNTRIED.

### G.1 The channel the company itself described, in its own word

The final prospectus states the route in one sentence, in the Business section under *Sales and Marketing*
(424B4, filed 1999-01-22, l.3295-3312): "The Company's distribution strategy is to work with a relatively
small number of leading add-in board manufacturers that have relationships with a broad range of major PC
OEMs and/or strong brand name recognition in the retail channel. Currently, the Company sells the RIVA family
of graphics processors **directly to add-in board manufacturers**, such as ASUSTeK, Canopus, Creative,
Diamond, ELSA, Leadtek and STB, which in turn sell boards with the RIVA128 graphics processor to leading
OEMs, such as Compaq, Dell, Gateway, IBM, Micron and Packard Bell NEC, to retail outlets, such as BestBuy and
CompUSA, and to a large number of system integrators." The *Manufacturing* section repeats the same chain
from the shipping end: the Company "performs incoming quality assurance and ships them to its add-in board
manufacturer customers … **from its location in Santa Clara**. The add-in board manufacturers then produce
boards, combine NVIDIA software with their own software and ship the product to the retail and system
integrator market" (l.3405-3413).

Four things are visible in that text and are worth naming precisely, because they are the whole of the
in-window channel evidence. **(1) The channel has four positions, not two:** Nvidia → AIB manufacturer → (OEM
∥ retail ∥ system integrator) → end user, and Nvidia's own contract boundary is the first arrow. **(2) The
demand mechanism is one step further out than the sale:** "Sales to add-in board manufacturers primarily are
dependent on achieving design wins with leading PC OEMs" (part 1 §F.1), and design cycles are stated as
external timing: "the Company's add-in board manufacturers and major OEM customers typically introduce new
system configurations as often as twice per year, typically based on spring and fall design cycles" (S-1/A
1998-11-20, l.1029-1033). **(3) There is no distributor.** In every draft this pass read, including the final
prospectus, the revenue-recognition note prints: "Revenue from product sales is recognized upon shipment, net
of an allowance for anticipated returns. **While the Company has not yet sold products through distributors**,
the Company's policy on sales to distributors will be to defer recognition of sales and related gross profit
until the distributors resell the product" (424B4 l.5599-5602; the same four lines are in the S-1/A of
1998-03-06, 1998-11-20 and every draft between). That is a contemporaneous negative with real weight: at the
stage boundary the company had a written policy for a channel it had not yet used. A search for
`consignment`, `DKE`, `Ingram`, `Microsys` and `value-added reseller` across the held in-window accessions
returns nothing; the word `backlog` returns nothing in the 424B4. **(4) The company called itself fabless
before the term was routine** — "The Company has a 'fabless' manufacturing strategy" (l.3374) — and §I shows
what that did to its cost base.

### G.2 Who bought, in percentages the registrant filed against its own interest

The concentration series is now complete across the stage on held bytes, and it is the single strongest
correction this pass contributes to part 1, which recorded only 1997:

| Period | Basis as printed | Who, and how much | Carrier |
|---|---|---|---|
| 1993, 1994 | total revenue | no customers at all: revenue `$--` in both years | S-1 1998-03-06 Summary Financial Data (part 1 P1-02) |
| 1995 | "total revenue" (MD&A) / revenue (Note) | **Diamond 86%** | S-1/A 1998-03-06 l.1926-1927; Note F-13 l.5202-5204 |
| 1996 | "total revenue" / revenue | **Diamond 82%** | same two carriers |
| 1997 | "total revenue" | **STB 63% + Diamond 31% = 94%** | S-1/A 1998-03-06 l.961, l.2823; 424B4 l.3310 |
| 1997 | "product revenue … of the Company's 1997 revenue" | STB 63% / Diamond 31% — **same numbers, different stated base** | 424B4 Note F-13 l.5202-5204 |
| nine months ended 1998-10-25 | "total revenue" | **STB 40%, Diamond 28%, Creative 12%** (80% across three AIB houses) | 424B4 l.3311-3313 |
| 1997 year-end | accounts receivable | **"three customers accounted for all accounts receivable in 1997"**; "Although the Company has not experienced any bad debt write-offs to date" | S-1/A 1998-03-06 l.2322-2326 |

Two readings of that table are admissible and one is not. Admissible: the company sold into a market with a
handful of viable buyers, and the identity of the dominant buyer changed between 1996 and 1997 from Diamond
to STB. Admissible: the 1998 nine-month mix is *less* concentrated than 1997 while still being 80% across
three firms, which is what an added third AIB relationship (Creative) looks like. **Not admissible:** reading
the two printed bases as one. The MD&A sentence says the percentages are of **total** revenue; the Note says
they are **product revenue** as a share of 1997 revenue. For calendar 1997 the filing itself gives total
revenue $29,071K and product revenue $27,280K (424B4 Selected Financial Data l.1950-1954), so STB at "63% of
total" is $18,315K while STB at "63% of product" is $17,186K — a 4.5-point difference in the denominator that
no held note reconciles. Recorded as U.107, and every channel percentage in the register carries which of the
two bases its own sentence states.

### G.3 The channel also lent the company money, and the corpus says so in one sentence

Part 1 recorded the $11.0M "mandatorily convertible notes" line in the capitalization table and the fact that
they converted into 1,571,429 shares on 1999-01-15, and did not identify the holders. The Note does. Under
*Mandatorily Convertible Notes* (424B4 l.5825-5846): "**Convertible subordinated non-interest bearing notes
were issued to three major customers in July and August 1998 for a total of $11.0 million.** The notes are
subordinated to certain senior indebtedness." The conversion mechanism is printed in full: automatic
conversion at closing of a firm-commitment underwritten IPO yielding **gross proceeds of at least $10.0
million before December 31, 1998**, at **90% of the public offering price**; failing that, automatic
conversion **on January 15, 1999 at $7.00 per share**; and on a change of control before that date, at 90% of
the as-converted acquisition price.

Consequences for §G, stated with their mechanism and their confidence:
* **At the moment the company was scaling hardest, three of the buyers in §G.2 were also its lenders** —
  Class FACT (the registrant's own note, in an audited-note set), Confidence High *as to the printing*, and
  the holders' identities are **UNKNOWN** (the note says "three major customers"; no schedule names them).
  Confidence that the three are the same three AIB houses whose 40/28/12 split the same prospectus prints for
  the same nine months: **INFERENCE, Low**, because the note never uses the word "add-in board manufacturer"
  and no held text links the two lists. The alternative reading — that one of the three is a PC OEM or a
  different buyer — is not excluded by anything in the corpus.
* **The instrument is a channel fact, not only a financing fact.** Interest-free paper taken from customers,
  subordinated to senior lenders, convertible at a discount to the offering price, is a distribution
  relationship priced as a loan. The company's own liquidity narrative names the other two credit
  relationships in the same register: "the Company has financed its operations primarily through private sales
  of convertible preferred stock totaling $19.7 million and, **to a lesser extent, equipment lease financing
  and proceeds received from the exercise of employee stock options**" (424B4 l.2752-2758), and the capital
  account carries `Line of credit … 5,000` at 1998-10-25 against `--` at every earlier date, in the current-
  liabilities block, so it is a drawn borrowing and not a commitment (l.5227). So the 1998 credit stack is:
  customers $11.0M, a $5.0M drawn line, capital leases with non-current obligations of $1,891K at 1997-12-31
  and $2,032K at 1998-10-25 (current portions $1,434K and $1,843K) and $4,515K of gross future minimum payments
  at the last date (l.5229-5232, l.6187-6200), and nothing else.
* **It did not make the company bank-financed.** The March draft's sentence "no outstanding bank
  indebtedness" at 1997-12-31 (part 1 P1-03) survives this: the 1998 paper is customer paper and lease paper.
  What the corpus does *not* hold is any bank document, any loan agreement, or the line's terms.

### G.4 What the first two revenue years actually were, and the one sentence that settles part of §D (part 1)

Part 1's §D.2 found a $2,500K "advance on development agreement" in accrued liabilities with an unnamed
counterparty and recorded the console-partner explanation as "a lead, not a gap" (P1G04). The bytes answer
more than that. Two sentences, one in the Overview and one in Results of Operations (424B4 l.2223-2236,
repeated at l.2323-2334, and already present in the 1998-03-06 S-1): "The Company developed **the NV2 under
contract with a third party** and recorded a credit to research and development of **$2.0 million in 1995 and
$3.0 million in 1996**. Also, as part of a strategic collaboration agreement with ST, the Company received
contract funding in support of research and development and marketing efforts for the RIVA128 and RIVA128ZX
graphics processors. Accordingly, the Company recorded $2.0 million in 1996 and approximately $2.3 million in
1997 as a reduction primarily to research and development, and, to a lesser extent to sales, general and
administrative expenses." And the revenue-side sentence: "**All of the Company's revenue in 1995 and 1996 was
derived from the sale and license of the NV1**, and substantially all of the Company's revenue in 1997 … was
derived from the sale and license of the RIVA family" (424B4 l.2078-2082; S-1/A 1998-03-06 l.1907-1912).

So, as fact: (i) the cancelled second product was **a contracted, customer-funded development**, not an
internal experiment — which is the strongest in-window evidence in this corpus that a console-era counterparty
paid real money for Nvidia's work, and it is filed in the company's own voice with amounts and years; (ii)
the 1995–1996 revenue that Diamond took 86%/82% of was **sale *and license*** revenue, so the earliest named
customer relationship includes a technology licence, not only chips; (iii) reported R&D in these years is
**net of contract credits**, which changes the reading of the R&D series (see §M and §S). The counterparty is
still not named — the sentence says "a third party" — and Sega, the obvious candidate in the popular account,
appears in the in-window record only as an equity party entitled to information and inspection (part 1
P1-11, P1-12). This pass re-checked that: `Sega` occurs in the 1998-03-06 S-1 **only** inside Exhibit 4.3's
notice and signature provisions (l.9028, l.9069, l.9525, l.9793), **zero** times in the 424B4, and **zero**
times in the FY1999 10-K405. The named-counterparty question therefore stays a gap with a carrier that is now
one step closer: the gap is "who is the third party named in the NV2 contract", not "does a paid development
contract exist".

### G.5 The searches that returned nothing, perimeted

EMPTY (searched, this session, over the seven held in-window drafts and the 424B4, counts recorded):
`first customer` 0 · `initial customer` 0 · `first order` 0 · `first purchase` 0 · `first shipment` 0 ·
`customer since` 0 · `NV1 was sold` 0 · `sold the NV1 to` 0 · `no customer accounted` 0 · `backlog` 0 ·
`consignment` 0 · `DKE` 0 · `Ingram` 0 · `value-added reseller` 0 · `weeks of cash`/`days of cash` (part 1's
§D.4 set, re-run) 0. Nothing in this list is a finding about the past; each is a finding about this corpus.
UNANSWERED: `sources/wayback/` and `sources/financials/` are empty directories (verified by listing in part 1
§Boundary 3 and again here), so no archived page and no machine-readable financial series exists to search.
UNTRIED: the trade-press and documentary routes in `## Untried`.

**The honest §G verdict on the §10 trigger.** The first customer is **UNKNOWN** and stays UNKNOWN, but the
question is now narrower than part 1 left it, and the narrowing is itself the deliverable: whoever bought the
first NV1 is inside the set that produced $1,182K of 1995 revenue under a "sale and license" structure, of
which one named buyer took 86%, and the company's own text says the transaction type was a licence as well as
a sale. The follow-up task is not "find the first customer" — it is "find a 1995 document that names an NV1
purchaser", and the only families that could hold one are (c) periodicals and (e) documentary, both of which
this corpus did not reach.

### G.6 Claim records for §G

P1-28 Claim: At the stage boundary the company sold directly to add-in board manufacturers and had not yet used distributors. — Date: 1999-01-22 (and in every draft from 1998-03-06) — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.3295-3312 and l.5599-5602 — Source date: 1999-01-22 — Tier: 1 — Class: FACT as disclosed; the negative is a company statement about its own channel — Passage: "While the Company has not yet sold products through distributors, the Company's policy on sales to distributors will be to defer recognition of sales and related gross profit until the distributors resell the product." — Conf: High — Corroboration: 1 lineage (present in all seven held drafts — version evidence only) — Conflicts: None
P1-29 Claim: Diamond accounted for 86% of 1995 and 82% of 1996 revenue; STB 63% and Diamond 31% of 1997; STB 40%, Diamond 28% and Creative 12% of the nine months ended October 25, 1998. — Date: 1995, 1996, 1997, 1998-10-25 — Source path: sources/sec/0001012870-98-000618_0001012870-98-000618.txt l.1926-1928, l.2823-2826; sources/sec/0001012870-99-000192 l.3310-3313 — Source date: 1998-03-06 / 1999-01-22 — Tier: 1 — Class: FACT as disclosed; the underlying sales are unauditable outside the filing — Passage: "sales to STB, Diamond and Creative accounted for 40%, 28% and 12%, respectively, of the Company's total revenue in the nine months ended October 25, 1998" — Conf: High as to the disclosure — Corroboration: 1 lineage — Conflicts: U.107
P1-30 Claim: $11.0 million of non-interest-bearing subordinated convertible notes were issued to three major customers in July and August 1998, convertible at 90% of the IPO price on a qualifying offering or at $7.00 per share on January 15, 1999. — Date: 1998-07 and 1998-08 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.5825-5846 (Note 3, Mandatorily Convertible Notes) — Source date: 1999-01-22 — Tier: 1 — Class: FACT (audited-note text) — Passage: "Convertible subordinated non-interest bearing notes were issued to three major customers in July and August 1998 for a total of $11.0 million." — Conf: High — Corroboration: 1 lineage; no note instrument, no counterparty signature held — Conflicts: U.109
P1-31 Claim: The cancelled NV2 was developed under contract with a third party, funded $2.0M in 1995 and $3.0M in 1996 as a credit to research and development, and all 1995-1996 revenue came from the sale and licence of the NV1. — Date: 1995, 1996 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.2223-2236 and l.2078-2082 — Source date: 1999-01-22 — Tier: 1 — Class: FACT as disclosed; the counterparty's identity UNKNOWN — Passage: "The Company developed the NV2 under contract with a third party and recorded a credit to research and development of $2.0 million in 1995 and $3.0 million in 1996." — Conf: High for the funding, Medium for treating it as the $2,500K advance in the balance sheet (no held sentence links them) — Corroboration: 1 lineage, present already in the 1998-03-06 draft — Conflicts: U.112
P1-32 Claim: Three customers accounted for all accounts receivable at the end of 1997, and the company reported no bad-debt write-offs to that date. — Date: 1997-12-31 — Source path: sources/sec/0001012870-98-000618_0001012870-98-000618.txt l.2322-2326 — Source date: 1998-03-06 — Tier: 1 — Class: FACT as disclosed — Passage: "The Company's accounts receivable are highly concentrated and three customers accounted for all accounts receivable in 1997." — Conf: High — Corroboration: 1 lineage — Conflicts: None
P1-33 Claim: Sega appears in the whole held in-window corpus only as a party to the Exhibit 4.3 shareholders' agreement, and not once in the final prospectus or the FY1999 annual report. — Date: window-wide — Source path: sources/sec/0001012870-98-000618 (l.9028, l.9069, l.9525, l.9793); sources/sec/0001012870-99-000192; sources/sec/0000929624-99-000772 — Source date: 2026-09-26 (this pass's grep) — Tier: 1 — Class: FACT about this corpus, NOT a finding that Sega paid or did not pay the company — Passage: "(i) to Sega Enterprises, Ltd., (ii) to Itochu Corporation and Itochu Technology, Inc." — Conf: High as to the corpus — Corroboration: 0 — Conflicts: None

---

## H

STATUS: WRITTEN 2026-09-26

### H.1 The field, as the registrant was obliged to print it

Part 1's §C.3 recorded that "no independent count of the 3D-graphics market for 1993–1998 exists anywhere in
this corpus". That stands. What part 1 did **not** use is the one place where the registrant had to describe
the field with names: the *Competition* section and the risk factors built on it. These are Tier-1, dated,
in-window, and they are the market-as-knowable evidence for §H.

The 1998-03-06 S-1 lists the field in five categories (l.755-769): "NVIDIA's primary source of competition is
from companies that provide or intend to provide 3D graphics solutions for the mainstream PC market. These
include (i) new entrants … such as **Intel** Corporation, (ii) suppliers of graphics add-in boards that utilize
their internally developed graphics chips, such as **ATI** Technologies, Inc. and **Matrox** Electronic Systems
Ltd., (iii) suppliers of 2D graphics chips that are introducing 3D functionality … such as **S3** Incorporated
and **Trident** Microsystems, Inc., (iv) companies that have traditionally focused on the professional market
… including **3Dlabs** Inc., Ltd. and **Real3D**, and (v) companies with strength in the interactive
entertainment market, such as **Chromatic** Research, Inc., **3Dfx** Interactive, Inc. and **Rendition**, Inc."
The final prospectus (l.727-746) keeps the architecture, drops Chromatic (now acquired), and adds **SGI,
Evans and Intergraph** to the professional tier and **VideoLogic** to the integrated-3D tier.

Named in the same section, with dates, are four competitive facts the corpus does not otherwise contain:
"In **February 1998**, Intel announced the introduction of the **i740**, a 3D graphics accelerator that is
targeted at the mainstream PC market. Intel has significantly greater resources than the Company…" (S-1/A
1998-03-06 l.771-774, and the identical paragraph recurs in every later draft — the `i740` count is 6 in all
nine files); "ATI recently acquired Chromatic Research Inc., a media processor company"; "**Micron, one of
the Company's OEM customers, acquired Rendition, Inc.**, a 3D graphics accelerator company, to explore
embedded DRAM applications in the graphics arena"; and "**3Dfx**, a 3D graphics company and a competitor of
the Company, recently announced the execution of an acquisition agreement with **STB Systems, Inc.** ('STB'),
an add-in board manufacturer and significant customer of the Company. The Company expects that as a result of
the pending acquisition, sales to STB will be reduced significantly from prior levels, and that STB may no
longer continue to be a significant customer of the Company" (424B4 l.747-762). And the structural sentence:
"The market for 3D graphics processors is **highly fragmented and undergoing a period of consolidation**.
Several of the Company's competitors **and customers** have merged with other industry participants…"
(l.745-747). Also filed, and unglamorous: "Creative recently disclosed that it has acquired in excess of 5%
of the outstanding stock of 3Dfx, a competitor of the Company. … Creative could significantly reduce or
eliminate altogether the amount of product it purchases from the Company" (S-1/A 1998-11-20 l.1136-1143).

**What this licenses the reader to know, and what it does not.** The field is knowable in-period as a named,
segmented set with dated moves — that is more than "no market data exists" implies, and part 1's §C.3 was too
sweepersome about the *competitive* half of the question. What remains unknowable: any third-party unit or
revenue count for any of those firms, any pricing comparison, any benchmark, and any statement by a competitor
about Nvidia. The category labels themselves are the registrant's (each is a *Company belief about where it
competes*), the i740 paragraph is an external announcement reported by the registrant, and the three
consolidation sentences are reported events with the company's own admission of damage attached. Confidence:
High that these statements were made in 1998; **Low-to-UNKNOWN** for the competitive economics they describe.

### H.2 The three lawsuits, dated from the index and from the text

The corpus holds a second, better-documented face of the competitive field: **the registrant was sued on
patents by three competitors inside the window, and the drafts date each arrival.** From the S-1/A of
1998-11-20 (l.984-1007, *Legal Proceedings*), verbatim in substance: "On **April 9, 1998**, the Company was
notified that **SGI** had filed a patent infringement lawsuit against the Company in the United States
District Court for the District of Delaware … On **May 11, 1998**, the Company was notified that **S3** had
filed a patent infringement lawsuit … in the Northern District of California … alleges … three United States
patents … On **September 21, 1998**, the Company was notified that **3Dfx** had filed a patent infringement
lawsuit … alleges that the sale and use of the Company's **RIVA TNT** graphics processor infringes a United
States patent held by 3Dfx … The Company has filed answers to each suit and has filed **counter-claims
asserting that the patents in each suit are neither infringed nor valid.**" Each suit seeks unspecified
damages including treble damages, a permanent injunction and attorneys' fees. The consequence set is printed
too: "pay substantial damages …; permanently cease the manufacture, use and sale of any infringing products;
expend significant resources to develop non-infringing technology; or obtain a license from SGI, S3 or 3Dfx"
(l.1009-1021).

The version evidence is unusually clean here, because the `3Dfx` token count is a clock: **5 hits in the
1998-03-06 S-1, 4 in each of the April, June and July 1998 amendments, 40 in the 1998-11-20 amendment, 48
from 1998-12-23 through the 424B4** (measured this pass by count per file). SGI's count runs 4 → 44 → 49 →
50 → 54 across the same nine files. So: the SGI suit enters the record with the **1998-04-24** amendment
(36 days after the notification date), the S3 and 3Dfx suits with the **1998-11-20** amendment, and the
STB-acquisition sentence with **1998-12-23**. Nothing in part 1 records any of this: part 1's §E.2 and §F
speak of a company with one manufacturer and two customers, and the bytes show a company being litigated by
three named competitors, losing its largest customer's independence, and telling investors that a licence or
a redesign might be required — all inside the eight months before the offering. This is not hindsight; it is
what the instrument printed, and it belongs in §O (failures), §Q (consequences) and §U (conflicts).

A basis point §6 requires, and RD-127's rule requires it twice: **the dates above are notification dates, not
filing dates.** "In April 1998, SGI filed a patent infringement lawsuit against the Company, in May 1998, S3
filed … and in September 1998, 3Dfx filed" (l.1455-1458) is the same content in month form. The docket
records — the actual filing dates — are not in this corpus (family (e) UNTRIED), so the court-filed date is
UNKNOWN and the notification date is the earliest date the instrument supports. Do not let the month-form and
day-form sentences be quoted as two sources: they are one paragraph set in one document.

### H.3 The paths not taken, written as a firewall rather than as a story

The near-death is the classic place retrospective memory gets promoted, and the console-to-PC reversal is its
nearest neighbour. Part 1 §D.4 handled the first; this section handles the second, because §H is where the
"obviously right pivot" reading enters. State the filed thing:

* **Filed (CONTEMPORANEOUS printing, retrospective content):** the NV1 was "targeted primarily to the game
  console market" and "developed in the absence of industry standards with the goal of establishing the
  Company's proprietary NV technology as a 3D graphics standard"; sales stopped in Q1 1996; NV2 development
  ceased; RIVA128 was "designed to be compatible with Microsoft's Direct3D"; "By the end of 1996, the PC
  industry had broadly adopted Microsoft's Direct3D and Silicon Graphics Inc.'s ('SGI's') OpenGL 3D APIs. As a
  result, the Company experienced a significant reduction in revenue from sales of the NV1…" (S-1/A 1998-03-06
  l.1892-1902; identical in the 424B4 l.2062-2071 and in the FY1999 10-K405 l.1152-1158). All of it is one
  lineage, written 1998–99 about 1993–97.
* **Also filed, and the part the pivot story drops:** the industry-background section still names the consoles
  as a live 3D market — "Interactive 3D graphics is required across various computing and entertainment
  platforms, such as workstations, specialized arcade systems and **home gaming consoles**. However, the
  mainstream PC market has only recently begun to transition from traditional 2D graphics…" (S-1/A 1998-03-06
  l.2406-2409). And the 1998 competition set still contains a "strength in the interactive entertainment
  market" category with three named firms in it. So the company did not record that the console market had
  ceased to exist; it recorded that it was not going to be in it.
* **Filed and dated, and cuts against inevitability:** the same registrant that pivoted to an open API was,
  eight months after its best year, **being sued on patents by three competitors in that same API-rich
  market**, with the RIVA TNT specifically named, and with the company printing that it might have to "obtain
  a license from SGI, S3 or 3Dfx". A Direct3D-compatible design did not remove infringement exposure; saying
  so would be hindsight in the other direction, so record it as what the filing says and stop.
* **Explicitly declined, in the company's own words, dated:** "The Company does not currently have any plans
  to enter into **contractual development arrangements** and does not expect contract funding in the future"
  (424B4 l.2335-2338). Read with §G.4, that is the company closing the funding channel that had paid for the
  NV1/NV2 era — the one in-window sentence in this corpus that records an alternative being foregone rather
  than lost.
* **NOT held, and not to be written as fact:** any decision date for the architecture change; who decided;
  whether any board or investor weighed a console continuation; the sunk cost in NV2 beyond the $5.0M of
  credits and the $2,500K advance; any account of a moment of crisis. The searches behind that negative are
  listed in part 1 §D.4 and were re-run here (§G.5). A founder recollection of the pivot or of near-collapse
  exists in the wider record; **this corpus does not hold it**, and anything later fetched must be classified
  FOUNDER CLAIM / retrospective memory, dated to the interview, never to 1995 or 1996.

**Anti-hagiography test applied to this section (§2).** If this company had failed in 2001, would §H still
read as plausible? It would, and because it is written from the risk factors: the pivot is recorded as a
change of standard with an unresolved infringement exposure, the customer base as three firms that were also
lenders, the largest of them being bought by a plaintiff, and the market as "highly fragmented and undergoing
a period of consolidation". A company that failed would have filed sentences very like these. What would have
changed is only the last clause of the offering.

### H.4 Claim records for §H

P1-34 Claim: The registrant named its competitive field in five categories and by eleven to fourteen firms across the lineage, adding SGI, Evans and Intergraph and VideoLogic only in the final drafts. — Date: 1998-03-06 → 1999-01-22 — Source path: sources/sec/0001012870-98-000618_0001012870-98-000618.txt l.755-769; sources/sec/0001012870-99-000192 l.727-746 — Source date: 1999-01-22 — Tier: 1 — Class: FACT about the printing; CONTEMPORARY OBSERVATION about the named firms' existence; the categorisation is the registrant's own — Passage: "companies with strength in the interactive entertainment market, such as Chromatic Research, Inc. ('Chromatic'), 3Dfx Interactive, Inc. ('3Dfx') and Rendition, Inc." — Conf: High — Corroboration: 1 lineage — Conflicts: None
P1-35 Claim: SGI, S3 and 3Dfx each filed a patent infringement suit against the company inside the window, and the company answered and counter-claimed that the patents are neither infringed nor valid. — Date: notified 1998-04-09, 1998-05-11, 1998-09-21 — Source path: sources/sec/0001012870-98-003021_0001012870-98-003021.txt l.984-1021 — Source date: 1998-11-20 — Tier: 1 — Class: FACT (pleaded in a statutory disclosure); docket filing dates UNKNOWN — Passage: "The Company has filed answers to each suit and has filed counter-claims asserting that the patents in each suit are neither infringed nor valid." — Conf: High — Corroboration: 1 lineage; no court record held (family (e) UNTRIED) — Conflicts: U.113
P1-36 Claim: The registrant disclosed that 3Dfx's pending acquisition of its largest customer would significantly reduce that customer's purchases. — Date: announced by 1998-12-23 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.753-762 and l.3313-3322 — Source date: 1999-01-22 — Tier: 1 — Class: FACT as disclosed (forward-looking, and disclosed against interest) — Passage: "The Company expects that as a result of the pending acquisition, sales to STB will be reduced significantly from prior levels" — Conf: High — Corroboration: 1 lineage — Conflicts: U.111
P1-37 Claim: Intel announced the i740, a mainstream-PC 3D accelerator, in February 1998, and the registrant treated it as a standing competitive risk through the offering. — Date: 1998-02 — Source path: sources/sec/0001012870-98-000618_0001012870-98-000618.txt l.771-790 — Source date: 1998-03-06 — Tier: 1 — Class: CONTEMPORARY OBSERVATION reported by the registrant; FACT as to the paragraph's persistence (six `i740` hits in all nine held drafts) — Passage: "In February 1998, Intel announced the introduction of the i740, a 3D graphics accelerator that is targeted at the mainstream PC market." — Conf: High for the disclosure; the Intel announcement itself is not held — Corroboration: 1 lineage — Conflicts: None
---

## I

STATUS: WRITTEN 2026-09-26

### I.1 The manufacturing decision the corpus can actually date

Part 1 §E.2 established the 1998-state: "Substantially all of the Company's products currently are
manufactured by **ST in Crolles, France** pursuant to a strategic collaboration agreement", with TSMC
"recently established … on a purchase order basis", and "in December 1997, the Company experienced low
manufacturing yields at ST". Reading the rest of the lineage changes that from a state into a **switch**, and
the switch is dated by the documents themselves:

| Draft (index filing date) | What the manufacturing text says | Consequence |
|---|---|---|
| S-1 1998-03-06 | "Substantially all … manufactured by ST in Crolles, France pursuant to a strategic collaboration agreement"; TSMC "recently established … on a purchase order basis"; December 1997 ST yield problem | ST is the fabricator and the assembler; TSMC is a prospective second source |
| S-1/A 1998-04-24, 1998-06-08, 1998-07-27 | same frame (the string "primary manufacturer" returns **0** hits in all four March–July files) | no migration yet disclosed |
| S-1/A 1998-11-20 | first appearance of **Amkor Technology Inc.** and **Siliconware Precision Industries** (2 and 2 hits), first appearance of "the Company's **primary manufacturer**" applied to **TSMC** (1 hit), and the first risk factor: "During 1998, the Company experienced difficulties in achieving volume production at TSMC of the Company's RIVA128ZX and RIVA TNT graphics processors" | the migration and its cost enter the record together, in the same amendment as the S3 and 3Dfx suits |
| S-1/A 1998-12-23 → 424B4 1999-01-22 | "The Company in the past utilized ST and **currently utilizes TSMC** to produce the Company's semiconductor wafers and utilizes independent contractors to perform assembly, test and packaging"; "**The Company used ST in the past to assemble and test substantially all of the Company's products**"; "The RIVA TNT and RIVA128ZX graphics processors are manufactured by TSMC and assembled and tested by Amkor" | at the stage boundary ST is past-tense in two roles, and no single counterparty any longer holds fabrication *and* test *and* licence |

The counts in that table were measured this pass over all nine held in-window files (`primary manufacturer`,
`Amkor`, `Siliconware`, `STB will be reduced`), so the dating does not rest on reading one draft.

### I.2 What the company owned, and what it rented, in its own words

The *Manufacturing* section of the final prospectus (l.3372-3400) is the cleanest statement of the model in
the whole corpus: "The Company has a **'fabless' manufacturing strategy** whereby the Company employs world
class suppliers for all phases of the manufacturing process, including fabrication, assembly and testing.
This strategy leverages the expertise of industry-leading, **ISO-certified** suppliers … and allows the
Company to **avoid the significant costs and risks associated with owning and operating such manufacturing
operations**. These suppliers also are responsible for **procurement of raw materials** … As a result, the
Company can focus its resources on product design, additional quality assurance, marketing and customer
support." And the risk transfer, stated as accounting: "When production of a new product begins, as with the
RIVA TNT graphics processor, the Company typically pays for wafers, which may or may not have any functional
products. Accordingly, **the Company bears the financial risk until production is stabilized. Once production
is stabilized, the Company pays for functional die only.**"

Three scaling facts follow from held text and are the substance of §I:

* **The yield cost of the switch is dated and quantified at the quarter level.** "The Company experienced
  difficulties commencing volume production of the RIVA128ZX graphics processor in **March 1998** and the RIVA
  TNT graphics processor in **July 1998**. These difficulties were primarily due to yield problems that
  resulted in lower than expected revenues and higher manufacturing costs during the quarter ended **July 28,
  1998**" (424B4 l.515-520) — and the Business section states the same event with a different end-date:
  "The lower yields resulting from such difficulties resulted in higher expenses and lower revenues in the
  quarter ended **July 26, 1998**, as the Company was not able to timely supply such product to its customers"
  (l.3399-3402). The quarterly table itself uses **July 26, 1998** as the column heading (l.2471-2474). Two
  dates for one fiscal quarter inside one document: U.104. The magnitude of that quarter is in §M: revenue
  $12,134K, cost of revenue $12,961K, **gross loss $(827)K**, net loss **$(9,652)K** — the largest single-period
  loss anywhere in this corpus, larger than any full year 1993–1997 except 1995's $(6,377)K.
* **Capacity was bought, not built.** Capital expenditures "increased from $1.4 million in 1995 to $5.8
  million in 1997, due to additional capital leases and purchases of computer equipment, including workstations
  and servers to support the Company's increased research and development activities. The Company invested
  $6.5 million in capital expenditures in the nine months ended October 25, 1998 … The Company expects to
  spend approximately $10.0 million for capital expenditures in fiscal 2000" (l.2788-2805). The instrument of
  that buying is leases: non-current capital-lease obligations of $617K (1996-12-31), $1,891K (1997-12-31),
  $1,756K (1998-01-31) and $2,032K (1998-10-25), each with a current portion, and $2,032K carried into the
  capitalization table at the boundary (l.5229-5232, l.1804-1805); "In **July 1998**, the Company entered into a **noncancelable operating lease** for its
  facilities that extends through 2002" (l.6182-6184), whose future minimums run $334K/$1,614K/$1,845K/
  $1,899K/$1,788K by year ending January. The March 1998 draft's balance sheet had carried the Amdahl sublease
  (part 1 §B.4, Ex-10.11) at $341,190 annual base rent; by July 1998 the company had its own longer lease on a
  Santa Clara site — the register keeps both, each with its own date.
* **Commitments ran ahead of the balance sheet.** "As of October 25, 1998, in addition to commitments under
  operating and capital leases, the Company had **manufacturing commitments of $48.0 million**" (l.2789-2791).
  Against cash of $12,461K at that date and equity of $18,294K, that is the number that shows what scaling in
  this industry meant on the eve of the offering: purchase obligations at four times the cash position,
  incurred on purchase orders that the foundries had no obligation to accept in any specified quantity.

### I.3 Single-threading, and what the company did about it between drafts

The dependency language did not soften across 1998; it was rewritten from one supplier to another. The March
1998 draft: "because the lead time needed to establish a strategic relationship with a new manufacturing
partner could be several months, there is no readily available alternative source of supply for any specific
product". The November 1998 draft and after: "**TSMC** fabricates wafers for other companies, **including
certain competitors of the Company**, and could choose to prioritize capacity for other users or reduce or
eliminate deliveries to the Company on short notice … The Company is dependent **primarily on TSMC** …
**The Company's wafer requirements represent a small portion of the total production capacity of TSMC**"
(l.802-830 of the 424B4, the same paragraphs in the 1998-11-20 file). And on test: "The Company does **not**
have long-term agreements with either of these subcontractors [Amkor, Siliconware] … Due to the amount of time
typically required to qualify assemblers and testers, the Company could experience significant delays in the
shipment of its products if it is required to find alternative third parties" (l.1297-1312).

The ST relationship itself was not a supply contract only: "ST is entitled to manufacture the RIVA128ZX
graphics processor and to sell the RIVA128 and RIVA128ZX graphics processors in consideration for a royalty
payment to the Company. Under the ST Agreement, ST also has a **worldwide license to incorporate the
technology underlying the RIVA128 and RIVA128ZX graphics processors (including the source code and
architecture)** … subject to certain limitations on the modification of such technology, and a right to
receive software engineering and quality assurance support from the Company for the RIVA Technology **through
December 31, 1998**" (l.3325-3339). The royalty it produced was "6% of the Company's total revenue in each of
the nine months ended September 30, 1997 and the nine months ended October 25, 1998" — and the company
forecast its own decline: "**The Company expects royalty revenue from ST to decrease in the quarter ending
January 31, 1999** and subsequent quarters." Two observations belong here, both INFERENCE with alternatives
kept: (i) the company sold its fabricator the right to become a reseller of its product and to hold its source
code — an unusual risk allocation whose mechanism the filing does not explain (no consideration is stated
beyond "a royalty payment", and the rate is not printed); (ii) the ST obligation to provide support ran out
with calendar 1998, one week after the stage boundary, so the relationship as filed was *time-limited* — the
alternative reading, that it would simply be renewed, is not supported by any held text. **The instrument
itself is not held:** the S-1 exhibit index carries "10.10* Amended and Restated Strategic Collaboration
Agreement, dated March ____ , 1998, between the Company and ST Microelectronics, Inc." with the date left
**blank** and the asterisk entry "*To be filed by amendment". No amendment this pass read files it. The
company's single most consequential commercial contract therefore never entered the public record inside the
stage (U.117).

### I.4 Claim records for §I

P1-39 Claim: Between the March and November 1998 drafts of one registration statement the company's primary fabricator changed from ST Microelectronics to TSMC and assembly/test moved to Amkor and Siliconware. — Date: 1998-03-06 → 1998-11-20 — Source path: sources/sec/0001012870-98-000618_0001012870-98-000618.txt; sources/sec/0001012870-98-003021_0001012870-98-003021.txt; sources/sec/0001012870-99-000192 l.802-830, l.1297-1312, l.3404-3406 — Source date: 1999-01-22 — Tier: 1 — Class: FACT about the printings (token counts measured across all nine drafts); the decision date and the internal reason UNKNOWN — Passage: "The Company in the past utilized ST and currently utilizes TSMC to produce the Company's semiconductor wafers and utilizes independent contractors to perform assembly, test and packaging." — Conf: High — Corroboration: 1 lineage (version evidence) — Conflicts: U.106
P1-40 Claim: Volume-production difficulties at TSMC on the RIVA128ZX and RIVA TNT cost the company a negative gross margin quarter in mid-1998. — Date: quarter ended 1998-07-26 (printed also as 1998-07-28) — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.515-520, l.2471-2474, l.3399-3402 — Source date: 1999-01-22 — Tier: 1 — Class: FACT (self-disclosed negative, with a quantified table) — Passage: "These difficulties were primarily due to yield problems that resulted in lower than expected revenues and higher manufacturing costs during the quarter ended July 28, 1998." — Conf: High — Corroboration: 1 lineage — Conflicts: U.104
P1-41 Claim: Under the ST Agreement, ST held a worldwide licence to the RIVA technology including source code and architecture, was entitled to resell the product, and the company's support obligation ran through December 31, 1998; the agreement itself was never filed. — Date: as of 1999-01-22 (instrument dated "March ____, 1998", blank) — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.3325-3339; sources/sec/0001012870-98-000618 l.5499-5500 and the note "*To be filed by amendment" — Source date: 1999-01-22 / 1998-03-06 — Tier: 1 — Class: FACT as disclosed; the counterparty-signed instrument is NOT in this corpus — Passage: "ST also has a worldwide license to incorporate the technology underlying the RIVA128 and RIVA128ZX graphics processors (including the source code and architecture)" — Conf: High as to the description; the terms themselves UNKNOWN — Corroboration: 0 independent — Conflicts: U.117
P1-42 Claim: As of October 25, 1998 the company disclosed $48.0 million of manufacturing commitments in addition to its lease commitments, and expected about $10.0 million of capital expenditure in fiscal 2000. — Date: 1998-10-25 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.2788-2805 — Source date: 1999-01-22 — Tier: 1 — Class: FACT as disclosed — Passage: "in addition to commitments under operating and capital leases, the Company had manufacturing commitments of $48.0 million" — Conf: High — Corroboration: 1 lineage — Conflicts: None

---

## J

STATUS: WRITTEN 2026-09-26

### J.1 The instrument set, item by item

Part 1 §B.3 and §A.1 established the preferred ladder (Series A $0.50 in 1993 · B $1.80 in 1994 and 1995 · C
$6.67 in 1995 · D $5.26 in 1997 on two dates), the $19.7M aggregate, the ladder's internal footing, and the
down price. What part 1 did not carry, and what the notes do print, is the **term sheet of the paper itself**,
which turns the ladder from a price series into an instrument set (424B4 l.5848-5878, Note 3):

| Term | Series A | Series B | Series C | Series D |
|---|---|---|---|---|
| Dividend rate, noncumulative, only when declared | $.04 | $.144 | $.533 | $.42 |
| Liquidation preference per share | $.50 | $1.80 | $6.67 | $5.26 |
| Conversion | one-for-one, subject to dilution adjustment | same | same | same |
| Automatic conversion | \multicolumn — by the same clause for all four classes: a two-thirds vote of preferred, **or** an IPO closing with aggregate proceeds exceeding **$15,000,000** **and** an offering price of at least **$10.00 per share** | | | |

Four consequences, each with its carrier. **(a) The liquidation preferences equal the issue prices.** In every
one of the four rounds the price paid is the preference rank: this is flat-liquidation-preference paper with no
reported accruing dividend, i.e. investor protection through rank rather than through yield. **(b) The ladder
foots exactly once the warrant exercises are counted, and reading the equity statement line by line closes a
reconciliation part 1 left open.** The 1995 rows print: Balances 1994, preferred **6,693,831** shares (= 4,303,000
Series A + 2,390,831 Series B, exactly); "Issuance of Series B preferred stock … 416,667 … $750"; "**Exercise of
Series B warrants … 13,888 … $25**"; "Issuance of Series C preferred stock, net of issuance costs of $14 …
750,000 … $4,986"; and the 1995 balance **7,874,386** shares. The 1996 row adds a further **13,889** warrant
shares for $25K to reach 7,888,275, and 1997 adds the 1,438,812 Series D to reach **9,327,087** — the printed
outstanding count, to the share. So the 27,777 shares the four *stated rounds* do not account for are two
warrant exercises and nothing mysterious; and 1995 preferred proceeds foot as $750 + $25 + $4,986 = **$5,761K**
against the cash-flow statement's $5,762K, a $1K rounding difference rather than a $26K exception. Class:
DERIVED, arithmetic in §M.4; **this narrows part 1's "the ladder is complete" finding from "within $50K" to
"exact to $1K".** **(c) The 1993–1997 warrants are a second instrument class.**
"During the period 1993 through 1997, the Company granted warrants to purchase **80,000; 66,877; 10,000 and
29,706** shares of Series A, B, C and D preferred stock, respectively, **in connection with lease financing and
services**. These warrants are exercisable at $.50, $1.80, $6.67 and $5.26" (l.5881-5889). So equipment
financiers and service providers were paid in **preferred at the round price**, which is the corpus's only
documented non-cash compensation instrument of the private period. **(d) The company's own customers were paid
in common.** "the Company has undertaken to issue warrants to acquire **300,000 shares of Common Stock at a per
share exercise price equal to the initial public offering price**" (l.5714-5716) — the counterparty and the
purpose are not stated; a marketing/advertising consideration reading is an INFERENCE and stays one.

### J.2 The private common price, which is the price the preferred ladder never gives

The preferred ladder prices the company at $0.50 → $1.80 → $6.67 → $5.26. The *Director Compensation* section
prices the **common** at four dated moments, and those are in-window contemporaneous statements of the common
stock's fair value as the company and its board understood it (424B4 l.4059-4072): in July 1996 Coxe and
Stevens received options at **$.36**; Gaither at **$.36** (July 1996) and **$7.00** (December 1998); Jones at
**.05** (November 1993) and **$.36** (August 1996); Miller at $.05 (November 1994) and $.36 (September 1996);
Seawell at **$3.15** (December 1997) and $7.00 (December 1998). "Directors currently do not receive any cash
compensation for their services as members of the Board of Directors."

That yields the ladder the filings actually support: common at **$.05** (Nov 1993 and Nov 1994 grants) →
**$.36** (1996) → **$3.15** (Dec 1997) → **$7.00** (Dec 1998), a 70-fold nominal rise in the common's stated
exercise price across the stage, against a preferred price that rose 3.6×, then 3.7× again, then **fell 21%**.
Three uses and one prohibition. Use: it shows the middle years from the common's side (the 1996 grants at $.36
were made in the year the NV1 was pulled and NV2 cancelled, which is a valuation fact, not a narrative). Use:
it dates the 1998 acceleration without invoking the IPO. Use: it is the only in-window evidence in this corpus
of what the founders' and directors' own equity was worth before 1999. **Prohibition:** it does not support
any statement about what the company was "worth" — no held document states a valuation, a 409A, or a board
fair-market-opinion figure, and the $.05 and $.36 exercise prices are compensation inputs, not transaction
prices. The option overhang at the boundary is quantified once: "As of October 25, 1998, there were
**7,455,458 options** to acquire shares of common stock with a **weighted-average exercise price of $4.46**"
(l.5707-5708) — which is 53% of the 14,166,710 shares then outstanding, and the largest single dilution
number in the private-period record.

### J.3 Deferred compensation: the number part 1 called a mechanism candidate is now a ledger row

The 1997 equity statement rows, read in both drafts (S-1/A 1998-03-06 l.4595-4610; 424B4 l.5372-5405):

| Row | 1998-03-06 draft | 1999-01-22 prospectus | Movement |
|---|---|---|---|
| Grant of common stock options for lease financing and consulting services | $120 | $120 | none |
| **Deferred compensation related to grant of common stock options (1997)** | **$2,100** | **$4,277** | +$2,177 |
| **Amortization of deferred compensation (1997)** | **$62** | **$961** | **+$899** |
| Deferred compensation balance at 1997-12-31 (contra-equity) | $(2,038) | $(3,316) | +$1,278 |
| Additional paid-in capital at 1997-12-31 | $22,902 | $25,079 | +$2,177 |
| Accumulated deficit at 1997-12-31 | $(13,991) | $(14,889) | +$898 |
| Total stockholders' equity at 1997-12-31 | $6,896 | $6,897 | +$1 |

Part 1 §Boundary 5 recorded that the FY1997 loss moved inside the lineage, named "$4.3 million … in 1997" as a
mechanism candidate and marked it INFERENCE because "$4.3M does not equal the $898K net movement". The full
ledger closes that gap arithmetically, and the closure is a DERIVED finding rather than a printed one: the
1997 **amortization** line moved by exactly **$899K**, which is exactly the operating-loss movement
($(2,560)→$(3,459)); the paid-in capital moved by exactly the grant increase ($2,177K); and the deficit moved
by the net-loss increase ($898K), with the $1K interest-line drift reconciling the equity total to a $1
difference. The 424B4's own expense rows show where the $899K landed: **cost of revenue +$18K (gross profit
7,845→7,827), research and development +$471K (6,632→7,103), sales, general and administrative +$410K
(3,773→4,183)** — and 18 + 471 + 410 = 899 exactly, which is the allocation pattern the company's own policy
describes: "Deferred compensation arising from stock-based awards is amortized in accordance with Financial
Accounting Standards Board Interpretation No. 28" (l.5616-5618), an allocation-by-function standard. No held
sentence says "the restatement was caused by deferred compensation". **Class: DERIVED, with the arithmetic
printed in §M; Confidence High that the identity holds in the bytes, Medium that it is the explanation.**
Part 1's P1K01 residual ("whether the change was an audit adjustment, a reclassification, or a stock-
compensation true-up is UNKNOWN") narrows to the last of the three, and §R carries the narrowing.

### J.4 The 1998 rounds, and the one instrument that shows the round price was not the market price

No new preferred series was sold in 1998 in any held document: the preferred share count is
**9,327,087 at 1997-12-31 and still 9,327,087 at 1998-10-25** (four-date balance sheet, 424B4 l.5240-5248),
and the deferred-comp note records only $361K of new 1998 grants. The 1998 money arrived in three other forms,
each dated and each on the face of the balance sheet. **(1) $11.0M of customer notes** in July–August 1998
(§G.3), carried *inside* stockholders' equity at 1998-10-25 as "Mandatorily convertible notes … -- -- --
11,000" (l.5237) — an unusual placement that itself signals the instrument's equity-like character. **(2) A
drawn line of credit: `Line of credit … -- -- -- 5,000`** (l.5227), which sits among **current liabilities**,
so the $5,000K at October 25, 1998 is an outstanding borrowing, not an authorisation, and it is the first
appearance of bank money anywhere in the lineage after the March draft's "no outstanding bank indebtedness"
sentence for 1997-12-31. The 1998-03-06 S-1 contains **no line-of-credit balance-sheet row at all** (0 hits;
the only mentions are the generic covenant phrase "borrowings under line of credit arrangements", l.1469 and
l.2355), so the facility is a *late-1998* entry — dated by the four-date balance sheet's columns, which are
December 31, 1996, December 31, 1997, **January 31, 1998** and October 25, 1998. **(3) $25K of common issued
for 25,000 shares** in the nine months to October 25, 1998, on a row labelled "Exercise of common stock"
(l.5409-5412), plus $6K for 1,125 shares in the January 1998 transition month — amounts too small to price a
round and unattributed by any held sentence to a named instrument, which is recorded as a gap rather than
converted into an option-exercise story.

The related-party case, which the corpus does print: "In August 1997, **Harvey C. Jones, Jr., a director of the
Company, purchased 24,334 shares of the Company's Series D Preferred Stock for an aggregate purchase price of
$127,997.** The Company sold these securities pursuant to a preferred stock purchase agreement and an
investors' rights agreement **on substantially the same terms as the other investors of Series D Preferred
Stock**, including registration rights, information rights and a right of first refusal, among other
provisions standard in venture capital financings" (424B4 l.4483-4491, *Certain Transactions*).
$127,997 ÷ 24,334 = **$5.2599…**, i.e. the round price to the dollar (§M DERIVED row). The same section
records registration rights granted in August 1997 to Coxe, Jones and Miller — "each of whom is a director" —
and to "Sequoia Capital VI and its related entities and Sutter Hill Ventures and its related entities, **both
of which are holders of more than 5% of the Company's Common Stock**", with the sentence "shares held by **and**
Sequoia Capital VI" printed with a name missing between "by" and "and" (as printed; see §K: either a drafting
error in the final prospectus or a dropped party; which is not resolvable from held bytes).

### J.5 The conversion condition that the offering's own assumed price does not satisfy

The preferred converts automatically on an IPO "in which the aggregate proceeds exceed $15,000,000 **and the
offering price equals or exceeds $10.00 per share**" (Note 3). The December 1998 amendment's pro-forma
footnote — carried by the 424B4 — assumes an initial price of **$8.00 per share** (part 1 P1S02; the March
1998 draft prints the same footnote with a literal blank, "an assumed initial public offering price of $ per
share"). At $8.00 × 3,500,000 shares the proceeds test passes ($28.0M > $15.0M) and the **price test fails**
($8.00 < $10.00). Yet the same prospectus presents pro-forma common shares of **25,065,226** as though all
9,327,087 preferred shares and 1,571,429 note-conversion shares had converted (l.1811-1817). Read strictly,
the two printed facts require a third fact that is not in the corpus: either the two-thirds vote (or a waiver
or amendment of the conversion condition) occurred, or the assumption was not the price. The register carries
this as U.109 and as a data gap, because the *mechanism* by which the preferred converted is exactly the kind
of consent that leaves no public trace when it is granted by written consent of the same five signatories who
control the board seats. Note that the **customer notes' own trigger is a different and lower number** —
"at least $10.0 million" of gross proceeds — so the two instruments in one note have two thresholds, and only
one of them is satisfied on the document's face.

### J.6 Claim records for §J

P1-43 Claim: The preferred carried flat liquidation preferences equal to each round's issue price, non-cumulative dividends of $.04/$.144/$.533/$.42, and automatic conversion only on a two-thirds vote or an IPO above $15.0M gross at $10.00 or more per share. — Date: as printed 1999-01-22 for instruments of 1993-1997 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.5848-5878 — Source date: 1999-01-22 — Tier: 1 — Class: FACT (instrument terms recited by the registrant; the instruments themselves are not held) — Passage: "Holders of Series A, B, C and D preferred stock have a liquidation preference of $.50, $1.80, $6.67, and $5.26 per share, respectively, plus any declared but unpaid dividends over holders of common stock." — Conf: High — Corroboration: 1 lineage — Conflicts: U.109
P1-44 Claim: Between 1993 and 1997 the company granted warrants over 80,000/66,877/10,000/29,706 preferred shares at each round's price in connection with lease financing and services. — Date: 1993-1997 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.5881-5889 — Source date: 1999-01-22 — Tier: 1 — Class: FACT as disclosed — Passage: "the Company granted warrants to purchase 80,000; 66,877; 10,000 and 29,706 shares of Series A, B, C and D preferred stock, respectively, in connection with lease financing and services" — Conf: High — Corroboration: 1 lineage — Conflicts: None
P1-45 Claim: Director option grants date the private common at $.05 (1993, 1994), $.36 (1996), $3.15 (Dec 1997) and $7.00 (Dec 1998), while directors took no cash compensation. — Date: 1993-11 → 1998-12 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.4055-4072 — Source date: 1999-01-22 — Tier: 1 — Class: FACT (grants with stated exercise prices); the fair-value basis of those prices is not disclosed — Passage: "In November 1993 and August 1996, Mr. Jones was granted options to purchase 75,000 and 70,000 shares of the Company's Common Stock at exercise prices of $.05 and $.36 per share, respectively." — Conf: High for the grants; Low for treating exercise price as value — Corroboration: 1 lineage — Conflicts: None
P1-46 Claim: The FY1997 restatement moved deferred-compensation amortization by exactly $899K, allocated $18K/$471K/$410K across cost of revenue, R&D and SG&A, and the 1997 grant by $2,177K. — Date: 1998-03-06 → 1999-01-22 — Source path: sources/sec/0001012870-98-000618 l.4595-4610 and l.4520-4536; sources/sec/0001012870-99-000192 l.5372-5405 and l.1950-1985 — Source date: 1999-01-22 — Tier: 1 — Class: DERIVED (arithmetic on two printings of one lineage); no held sentence states causation — Passage: "Amortization of deferred compensation........... -- -- 62" / "Amortization of deferred compensation........... -- -- 961" — Conf: High that the identity holds, Medium that it is the mechanism — Corroboration: 1 lineage — Conflicts: P1K01 (part 1), U.101
P1-47 Claim: No preferred stock was sold in 1998; that year's outside money was $11.0M of customer notes, a $5.0M line of credit first shown at October 25, 1998, and $25K of common issuances. — Date: 1998 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.5227, l.5403-5412, l.5825-5846 — Source date: 1999-01-22 — Tier: 1 — Class: FACT as disclosed; whether the line was drawn or merely authorised is UNKNOWN — Passage: "Line of credit................ -- -- -- 5,000" — Conf: Medium — Corroboration: 1 lineage — Conflicts: None
P1-48 Claim: A sitting director bought 24,334 Series D shares at the round price in August 1997 under a purchase and investors' rights agreement. — Date: 1997-08 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.4483-4491 — Source date: 1999-01-22 — Tier: 1 — Class: FACT (Certain Transactions disclosure) — Passage: "In August 1997, Harvey C. Jones, Jr., a director of the Company, purchased 24,334 shares of the Company's Series D Preferred Stock for an aggregate purchase price of $127,997." — Conf: High — Corroboration: 1 lineage; Jones's own signature appears on the Ex-4.3 shareholder pages (part 1 §B.3), which is the same lineage — Conflicts: None

## K

STATUS: WRITTEN 2026-09-26

**How to read this section.** §K is the corpus's list of what cannot be settled *and stays* unsettled after
this pass. Each item names the state it is in — EMPTY (searched here, perimeted), UNANSWERED (bytes not
reached: 403/404/429/zero), UNTRIED (never attempted, with the route named) — because conflating the three is
how a null becomes a fabricated absence (RD-127, RD-128). Part 1's `data_gaps.csv` rows P1G01–P1G10 remain
live; this section adds to them and marks which part-1 gaps this pass narrowed.

1. **Who the first customer was, and when the first order was booked.** UNKNOWN. **EMPTY** for the strings
   listed in §G.5 across the seven held in-window drafts and the 424B4. Narrowed, not closed: the earliest
   named buyer of record is Diamond Multimedia Systems, Inc. at 86% of 1995 revenue, and the transaction type
   included a licence. Route: family (c) trade press, family (e) documentary — **UNTRIED**.
2. **The counterparty of the NV2 development contract and of the $2,500K advance.** UNKNOWN. **EMPTY**: no
   held sentence names it; the contract is not an exhibit. This pass *did* establish that a paid third-party
   contract for NV2 existed and its amounts by year (§G.4), which is the largest narrowing of a part-1 gap
   made here (P1G04).
3. **The identities of the three "major customers" who lent $11.0M in July–August 1998.** UNKNOWN. The note
   gives a count, a total, dates and terms; no schedule names them. **EMPTY** for any list tying noteholders
   to names. The cheapest untried route is the underlying instruments, which were not filed.
4. **Whether the $5,000K line of credit was secured, from whom, and on what covenants.** UNKNOWN; the balance
   sheet prints the drawn amount and the MD&A prints the phrase "credit line and capital lease financing" and
   "available borrowings under line of credit arrangements". No credit agreement is an exhibit — **EMPTY** in
   the corpus, **UNTRIED** at state-level secured-interest filings and family (e).
5. **The ST Agreement itself.** Never filed: exhibit 10.10 was "to be filed by amendment" and its date prints
   "March ____ , 1998". No later held amendment files it. So the terms that gave a competitor-fabricator a
   royalty, a resell right and the source code are known only from the registrant's summary of them. U.117.
6. **How much the NV1 cost to develop, what it sold for, and how many units moved.** UNKNOWN; **EMPTY** —
   unit volumes, prices and bill of materials appear nowhere in the lineage (part 1 §E.3), and this pass found
   only the aggregate product/royalty split by year and quarter (§M). NV1 die, datasheet, clock rate: not in
   any held byte; the RIVA parts' specs *are* held (3.5M transistors, 100 MHz, 20 BOPS, .35 micron), which is
   a partial closure of part 1's P1G09 pointing the wrong way — detail exists for the second product, none for
   the first.
7. **The internal decision record for every choice in §P.** UNKNOWN, structurally: no board minute, no
   investor presentation, no business plan, no rejected-option memo is in EDGAR for this registrant before
   1998-03-06 (part 1 §Boundary 3, re-measured there, not here). **UNANSWERED** for web archives (empty
   directory, no negative artifact) and **UNTRIED** for family (e).
8. **Whether the offering price satisfied the preferred's own conversion condition.** Unsettled by held bytes;
   the two printed facts conflict on their face (U.109, §J.5). Best available evidence is the pro-forma column
   itself. Route: the underwriting agreement (Exhibit 1.1, "to be filed by amendment", never filed in the held
   drafts) — **UNTRIED** at the FY1999 10-K405 exhibit set, which is on disk but was not read for this
   question.
9. **What is left of the preferred reconciliation.** Closed by this pass rather than inherited: the 27,777
   shares the four stated rounds miss are two Series B **warrant exercises** (13,888 in 1995 and 13,889 in 1996,
   both printed in the equity statement, §J.1(b)), and the aggregate liquidation preference then foots to
   **$19,825.7K against the printed $19,827K** — a $1.3K rounding residual. What stays UNKNOWN is the identity of
   the warrant holders and what the warrants were given for beyond the note's "lease financing and services".
10. **Any independent count of anything.** There is none, and no route in this corpus reaches one. Every
    1993–1998 figure is the registrant's; the two third-party-signed in-window exhibits part 1 names are a
    *shareholders'* agreement and a *sublease*. §T keeps the ledger.
11. **What the two Form RW filings of 1998-05-07 withdrew, and what the 1998-03-23 Form 8-A12B, the
    1998-04-03 and 1999-01-12 Forms 8-A12G and the 1999-01-22 Form S-1MEF were.** All six rows are **indexed
    with a blank `primaryDocument`** in `sources/_index/submissions.csv` and none is stored under
    `sources/sec/`, so this pass could not read them: **UNTRIED**, not EMPTY, not UNANSWERED. A listing defect
    is not an absence of filings — part 1's P1G10 made the same point about nameless rows; the specific rows are
    enumerated in the timeline register below.
12. **The Google Books items the harvest dossier recorded as UNANSWERED.** `research/A4_harvest_mine.md`
    prints three volume ids (`U9n74ngfDU8C`, `z3zsxvtRSv4C`, `vcdVAAAAMAAJ`, scan-dated 1998/1999) at 0 bytes,
    labelled UNANSWERED. Per the dispatch correction, those are **Google Books volume ids fetched from the
    wrong host** — so the correct statement is **UNTRIED at the right host**, not a refusal, and they are
    carried in `## Untried` with the host named. Chronicling America is likewise **a 404-on-our-path defect,
    not a refusal** (RD-128/RD-129): the route has never returned an answer either way, and it is the family
    that could hold 1994–1997 trade and local newspaper naming of this company. Neither is a null.

## L

STATUS: WRITTEN 2026-09-26

**The firewall is a rule about evidence, restated here as it applies to §G–§U (§2).** The company succeeded.
That fact is not evidence in any of these sections, and §L exists to name, item by item, where the corpus is
tempted to use it.

1. **The 1997 revenue turn is not proof that the 1996 re-architecture was right.** What is filed: Q3 1997
   product revenue $5,225K and Q4 $22,055K after an August 1997 introduction; and in the same document, three
   patent suits by competitors whose designs were also API-compatible, a negative gross margin in the quarter
   ended July 26, 1998, and the loss of the 63% customer to a plaintiff. A reader holding only these bytes
   could equally conclude that the Direct3D path exposed the company to litigation and to a one-product
   dependency. Both readings are inadmissible as conclusions; §H.3 states why.
2. **The down round is not proof of weakness overcome.** $5.26 against $6.67 is a filed price (part 1
   P1-10). Its *meaning* — distress, a market clear, a renegotiated protection package — is not printed. The
   temptation is to read it as "the year before they were right"; the corpus supports only "the fourth priced
   round cleared 21% below the third".
3. **The customer notes are not proof that customers believed in the company.** Interest-free convertible
   paper from three buyers is consistent with confidence and equally consistent with a customer securing
   supply, securing priority, or placing cash it could not otherwise deploy. **Mechanism UNKNOWN** — §14's
   coda rule applies: a coda that cannot name a mechanism says so instead of implying one.
4. **"Fabless" is not a prediction.** The company wrote the word in 1998 to describe *not owning a fab*. It
   did not describe a durable model, and the same drafts record the cost of the dependence it created — "The
   Company's wafer requirements represent a small portion of the total production capacity of TSMC". The
   reverse reading is blocked too: the model did not cause the 1998 yield losses. Cause UNKNOWN.
5. **The 1999 listing is not a validation of anything in this window.** The stage closes on the date the
   prospectus was printed; the offering's result, the aftermarket and the FY1999 figures are `(PB)` and are
   excluded from every §G–§U conclusion. The single place a `(PB)` document is used in this volume — the
   1999-08-06 SC 13G by Creative Technology Ltd in §T — is used to date a silence about who later spoke about
   the company, and for no Stage-1 fact.
6. **The record-selection null applies hardest to §P.** The alternatives in §P are *printed* alternatives:
   each is something the company said it did not do, or something the shape of its paper implies it did not
   choose. They are not the rejected options of the internal record, which is gone (§K.7). Any §P row that
   reads as "they considered X" overstates; the register wording is deliberately "NONE PRINTED".
7. **The "obviously huge market" reading is blocked by the corpus's own silence.** The industry-background
   section quantifies nothing except by quotation: "Mercury Research estimates that 3D graphics will be
   standard in every PC unit shipped by 2001. Mercury Research also estimates 8.6 million 3D graphics
   processors…" (S-1/A 1998-03-06 l.2418-2421). That is a third-party estimate **relayed** by the registrant —
   Tier 1 as to the printing, and its independence is capped at "a research firm the company chose to quote",
   with the underlying report absent. It is not a market-size fact, and the sentence's own frame ("the Company
   believes") governs the paragraphs around it.
8. **Anti-hagiography test, run per §2 on this volume's codas.** Each was rewritten until it survived: the
   channel section reads as a description of a concentrated, customer-financed, single-fab business with a
   litigation docket; the competition section as a consolidation the company was exposed to; §I as a capacity
   story bought with leases and commitments; §J as a term sheet. If this company had failed in 2001 these
   sections would be shorter, not different.

## M

STATUS: WRITTEN 2026-09-26

**Every value below carries carrier + basis + CONTEMPORANEOUS/RESTATED (§6, §8).** "Carrier" names the stored
file and the table; "basis" names calendar-vs-fiscal, product-vs-total, audited-vs-unaudited,
period-end-vs-weighted-average. Register row tags `P1Q31`+ continue part 1's quantitative series.

### M.1 The quarterly series, which part 1 named and did not read

The 424B4 carries a seven-column unaudited quarterly table (l.2466-2516), "*Selected quarterly financial
data* … derived from the internal quarterly financial reports for the periods shown", with the fiscal-calendar
sentence immediately above it (l.2471-2478). In thousands of dollars:

| Quarter ended | Product rev | Royalty | Total rev | Cost of revenue | Gross profit (loss) | R&D | SG&A | Operating income (loss) | Net income (loss) | Basic EPS | Basic shares |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1997-03-30 | 65 | -- | 65 | 208 | (143) | 616 | 385 | (1,144) | (1,176) | (.10) | 11,578 |
| 1997-06-29 | 6 | -- | 6 | 150 | (144) | 512 | 569 | (1,225) | (1,265) | (.11) | 11,662 |
| 1997-09-28 | 5,154 | 312 | 5,466 | 4,548 | 918 | 2,390 | 1,070 | (2,542) | (2,572) | (.19) | 13,328 |
| 1997-12-31 | 22,055 | 1,479 | 23,534 | 16,338 | 7,196 | 3,585 | 2,159 | 1,452 | **1,424** | .10 | 14,074 |
| 1998-04-26 | 24,642 | 3,621 | 28,263 | 20,873 | 7,390 | 4,642 | 3,885 | (1,137) | (1,021) | (.07) | 14,141 |
| 1998-07-26 | 10,963 | 1,171 | 12,134 | 12,961 | **(827)** | 5,724 | 3,962 | (10,513) | **(9,652)** | (.68) | 14,148 |
| 1998-10-25 | 51,150 | 1,153 | 52,303 | 33,566 | 18,737 | 6,290 | 4,697 | 7,750 | **7,141** | .50 | 14,165 |

Four derived checks, each printed in the register with its arithmetic. **(a) 1997 quarters foot to the year:**
(1,176)+(1,265)+(2,572)+1,424 = **(3,589)**, the *restated* annual net loss (part 1 P1K01), so the final
quarterly table and the final annual column are mutually consistent. **(b) The March 1998 draft's own
quarterly row footed to its own annual figure**: its four 1997 quarters print (1,176) (1,265) **(2,413)
2,163** = (2,691) (l.2075) — so the restatement is not a transcription slip; it moved **Q3 by $(159)K and Q4
by $(739)K** and left Q1 and Q2 alone. **(c) The fiscal-1999 quarters foot to the nine months:**
(1,021)+(9,652)+7,141 = **(3,532)**, the reported nine-month net loss. **(d) Revenue foots too:** the four
1997 quarters sum to $29,071K, exactly the annual total part 1 recorded as "the one 1997 line that does not
move across the lineage".

That last check is the section's most useful single number and its basis must be carried: **unaudited,
internally derived, on the pre-change calendar quarters of a December-fiscal year** — the company's later
"quarters" are not the same length (§S). It also destroys a comfortable reading of the turn: the first
profitable quarter ($1,424K) was followed by two loss quarters and the worst period loss in the corpus, and the
company's own Overview says exactly that: "The Company incurred a loss in the quarters ended April 26, 1998 and
July 26, 1998 and realized profits in the quarters ended December 31, 1997 and October 25, 1998"
(l.2052-2056).

### M.2 The one-month columns, including the period part 1 kept verbatim and used for nothing

Part 1 recorded the string "one month ended January 26, 1997", declared the period UNKNOWN and used it for
nothing (P1K05). Reading the tables settles the datum and **refutes part 1's premise about it**. The string is
not an orphan footnote phrase: **it is a printed column in the Selected Financial Data table and in the
Statements of Operations and Cash Flows.** The F-pages index lists "Statements of Operations for the years
ended December 31, 1995, 1996 and 1997, **one month ended January 26, 1997 (unaudited)**, one month ended
January 31, 1998, nine months ended September 28, 1997 (unaudited), and nine months ended October 25, 1998"
(l.5132-5136). Part 1's §Boundary 4 enumerated the summary table as carrying seven columns and stated that the
January-1997 date "corresponds to no column in its own summary table"; the table at l.1941 prints **nine**, two
of which are one-month columns. That is an enumeration error of exactly the class RD-124/RD-127 warn about — a
column assumed rather than listed — and it is recorded as U.110 and as a correction to P1K05, not as a silence.

What the two one-month columns contain (thousands; l.1947-1985, with the identical figures at l.5283-5300):

| Line | One month ended **January 26, 1997** (unaudited) | One month ended **January 31, 1998** |
|---|---|---|
| Product revenue | 190 | 11,420 |
| Royalty | — | 1,911 |
| Total revenue | 190 | 13,331 |
| Cost of revenue | 127 | 10,071 |
| Gross profit | 63 | 3,260 |
| R&D | 415 | 1,121 |
| SG&A | 164 | 640 |
| Operating income (loss) | **(516)** | **1,499** |
| Income (loss) before tax | (522) | 1,481 |
| Income tax | — | 134 |
| Net income (loss) | **(522)** | **1,347** |
| Weighted basic shares (Note 8) | 11,567 → EPS $(.05) | 14,141 → basic $0.10, diluted $0.05 |

So the January 1997 month is a real, quantified period — a $190K revenue month, the smallest reported revenue
period of the stage, inside the year that produced the largest loss — and the January 1998 month is the
company's **first profitable reported period**, $1,347K, which part 1 could only describe as "a single
profitable quarter". Both are used in the registers with their labels; and both labels are contested inside the
same document, which is §S's subject.

### M.3 The four-date balance sheet, which is where the scaling is actually visible

The prospectus prints a balance sheet at **December 31, 1996, December 31, 1997, January 31, 1998 and October
25, 1998** (l.5205-5262), and the movement across those four dates is the clearest in-window picture of what
growth cost. In thousands:

| Line | 1996-12-31 | 1997-12-31 | 1998-01-31 | 1998-10-25 |
|---|---|---|---|---|
| Cash and equivalents | 3,133 | 6,551 | 7,984 | 12,461 |
| Accounts receivable, net | 1,041 | 12,487 | 15,399 | 35,918 |
| Inventory | 63 | 25 | 521 | **17,193** |
| Total current assets | 4,278 | 19,341 | 24,498 | 66,735 |
| Property and equipment, net | 1,144 | 5,536 | 5,512 | 9,218 |
| **Total assets** | **5,525** | **25,039** | **30,172** | **76,502** |
| Accounts payable | 277 | 11,572 | 15,312 | **46,370** |
| Line of credit | — | — | — | 5,000 |
| Accrued liabilities | 2,872 | 3,245 | 3,266 | 2,963 |
| Current capital-lease obligations | 722 | 1,434 | 1,228 | 1,843 |
| Total stockholders' equity | 1,037 | 6,897 | 8,610 | 18,294 |

The receivable line carries "allowances of $100, $349 and $3,506, at December 31, 1997, January 31, 1998 and
October 25, 1998, respectively" — **three dates for four columns**, so which allowance belongs to December 31,
1996 is undetermined by the sentence; recorded as a basis caveat rather than resolved.

Read as a scaling mechanism: between the last day of the calendar year in which the company first earned money
and the last measured day of the stage, **inventory moved from $25K to $17,193K, receivables from $12,487K to
$35,918K and payables from $11,572K to $46,370K**, while cash rose only $5.9M and equity only $11.4M — the
growth was funded out of suppliers' credit and customers' obligations, plus the $11.0M customer notes and the
$5.0M line, not out of earnings. The 1997 cash-flow statement (March draft l.4637-4650) shows the same shape a
year earlier: accounts receivable +$11,446K against accounts payable +$11,295K, so the RIVA turn was almost
entirely a working-capital event before it was a cash event. Capital expenditure for 1997 was $2,732K against
$9K in 1996 and $5K in 1995. **Class for all of this: FACT as printed; the mechanism reading is INFERENCE,
Medium**, because no held text describes the credit terms that produced the payables figure.

### M.4 Share and preference arithmetic (all DERIVED; arithmetic shown)

* **Post-offering share count, three ways, and they do not all agree.** Pro forma as adjusted in the
  capitalization table: **28,565,226** = 14,166,710 common + 9,327,087 as-converted preferred + 1,571,429
  note-shares + 3,500,000 new (l.1811-1817). The cover and the ownership footnote print **28,595,976** (l.238,
  l.1705, l.4598), "assuming no exercise of outstanding options and warrants". Difference: **30,750 shares**.
  The footnote supplies the third datum that closes it: ownership percentages are computed on **23,524,547
  as-converted shares "as of December 31, 1998"**, and 23,524,547 + 1,571,429 = 25,095,976 restricted shares,
  + 3,500,000 = 28,595,976 exactly. The two figures are an October 25, 1998 measurement and a December 31, 1998
  measurement, and the 30,750 shares are the issuances between them — which yields a number the prospectus
  never prints: common outstanding at 1998-12-31 of **14,197,460** (= 14,166,710 + 30,750). Confidence High for
  the identity, Medium for the attribution of the 30,750 (the only printed 1998 issuance is 25,000 shares for
  $25K).
* **Aggregate liquidation preference.** The balance sheet prints "aggregate liquidation preference of
  **$19,827** in 1997, January 31, 1998, and October 25, 1998". Summing the stated preferences across every
  share the equity statement accounts for: 4,303,000×$.50 + (2,390,831 + 416,667 + 13,888 + 13,889)×$1.80 +
  750,000×$6.67 + 1,438,812×$5.26 = 2,151.5 + 5,103.5 + 5,002.5 + 7,568.2 = **$19,825.7K**, i.e. **$1.3K below**
  the printed aggregate — rounding, not an exception. The same share set foots to the printed 9,327,087
  outstanding at 1997-12-31 exactly (§J.1(b)). Class DERIVED, Confidence High.
* **The preference stack exceeded the money raised.** $19,827K of liquidation preference against the MD&A's
  "$19.7 million" of preferred proceeds: at the boundary the investors' prior claim was larger than the cash
  they had put in, and the common stood behind all of it. Class FACT + DERIVED comparison, High.
* **Option overhang.** 7,455,458 options at a weighted-average exercise price of $4.46 against 14,166,710
  shares outstanding = **52.6%** overhang (derived), and the quarterly table's diluted share count for the
  profitable quarter ended 1998-10-25 — 27,774K against 14,165K basic — shows what conversion plus options did
  to the per-share result ($0.50 basic → $0.26 diluted).
* **The down-round ratio, again with the arithmetic rather than as a figure of speech:** $5.26 ÷ $6.67 =
  0.7886, i.e. 21.1% below (part 1 P1Q13; restated here because this pass re-read both prices at l.5850-5858).
* **Jones's Series D purchase:** $127,997 ÷ 24,334 = **$5.2599**, the round price to the cent (derived, High).

### M.5 Claim records for §M

P1-49 Claim: The prospectus carries a seven-column unaudited quarterly table whose 1997 and fiscal-1999 quarters foot exactly to the printed annual and nine-month figures. — Date: 1997 Q1 – 1998 Q3 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.2466-2516 — Source date: 1999-01-22 — Tier: 1 — Class: FACT as printed; the quarterly figures are unaudited internal-report derivations by the table's own header — Passage: "Selected quarterly financial data included in this table has been derived from the internal quarterly financial reports for the periods shown." — Conf: High (footings re-computed this pass) — Corroboration: 1 lineage — Conflicts: U.101
P1-50 Claim: The FY1997 restatement is localised to Q3 and Q4 1997 and equals the increase in amortization of deferred compensation, allocated $18K/$471K/$410K to cost of revenue, R&D and SG&A. — Date: 1998-03-06 → 1999-01-22 — Source path: sources/sec/0001012870-98-000618 l.2075, l.4520-4536, l.4595-4610; sources/sec/0001012870-99-000192 l.1950-1985, l.5372-5405 — Source date: 1999-01-22 — Tier: 1 — Class: DERIVED (an arithmetic identity across two printings of one lineage); causation is stated in no held sentence — Passage: "Amortization of deferred compensation … 62" (March draft) against "… 961" (final) — Conf: High for the identity, Medium for the explanation — Corroboration: 1 lineage — Conflicts: P1K01 (part 1), U.101
P1-51 Claim: The January 1997 one-month period is a printed financial-statement column with revenue $190K and net loss $(522)K, and the January 1998 transition month is a printed column with revenue $13,331K and net income $1,347K. — Date: 1997-01-26 and 1998-01-31 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.1941-1985, l.5132-5136, l.5283-5300, l.5660-5700 — Source date: 1999-01-22 — Tier: 1 — Class: FACT as printed; the January 1997 column is unaudited — Passage: "one month ended January 26, 1997 (unaudited), one month ended January 31, 1998" — Conf: High — Corroboration: 1 lineage — Conflicts: U.102, U.110 (corrects part 1 P1K05's premise)
P1-52 Claim: Between December 31, 1997 and October 25, 1998 inventory rose from $25K to $17,193K, receivables to $35,918K and payables to $46,370K, against a $5.9M rise in cash. — Date: 1997-12-31 → 1998-10-25 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.5205-5262 — Source date: 1999-01-22 — Tier: 1 — Class: FACT as printed (four-date balance sheet); the funding mechanism is INFERENCE — Passage: "Inventory....................... 63 25 521 17,193" — Conf: High — Corroboration: 1 lineage — Conflicts: U.114
P1-53 Claim: The prospectus prints two different post-offering share counts, reconciled by a December 31, 1998 as-converted figure that itself yields an unprinted common share count of 14,197,460. — Date: 1998-10-25 and 1998-12-31 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.1811-1817, l.4594-4604, l.1705 — Source date: 1999-01-22 — Tier: 1 — Class: DERIVED, arithmetic shown in §M.4 — Passage: "Percentage of beneficial ownership is based on 23,524,547 shares of Common Stock outstanding on an as-converted basis as of December 31, 1998" — Conf: High for the identity — Corroboration: 1 lineage — Conflicts: U.108
P1-54 Claim: Aggregate liquidation preference at the stage boundary was $19,827K, more than the $19.7M of preferred proceeds the company reported raising, and reconcilable to within $1.3K of the sum of the stated per-share preferences once the two Series B warrant exercises are counted. — Date: 1998-10-25 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.5239-5242 and the MD&A $19.7M sentence at l.2752-2758 — Source date: 1999-01-22 — Tier: 1 — Class: FACT (printed aggregate) plus DERIVED comparison — Passage: "aggregate liquidation preference of $19,827 in 1997, January 31, 1998, and October 25, 1998" — Conf: High — Corroboration: 1 lineage — Conflicts: None (the $1.3K rounding residual is recorded in §M.4, not as a conflict)

## N

STATUS: WRITTEN 2026-09-26

**§6 (time audit) applied to §G–§U.** Nothing in these sections imports post-1999 knowledge into 1993–1998,
and every in-window statement is labelled by the date of the **carrier**, not the date of the event. Because
this corpus is one registration lineage written in 1998–99, §N's real work is a **version trail**: for each
material fact, the first held document that prints it. That trail is the closest thing to contemporaneity
available, and it is what part 1's §3 rule asks to be recorded.

| Fact | First held printing (index filing date) | Latest held printing | Status |
|---|---|---|---|
| Inception label April 5, 1993; zero revenue 1993–1994 | 1998-03-06 | 1999-01-22 | registrant-retrospective about the event; audited stub for the numbers |
| NV1 introduced May 1995, console-targeted, sales stopped Q1 1996, NV2 ceased | 1998-03-06 | 1999-01-22 | retrospective narrative, identical wording in all drafts |
| NV2 developed under third-party contract; credits $2.0M (1995), $3.0M (1996) | 1998-03-06 | 1999-01-22 | retrospective, but a quantified filed contract effect |
| Diamond 86% / 82% of 1995 / 1996 revenue | 1998-03-06 | 1999-01-22 | retrospective concentration disclosure |
| Preferred ladder A–D: prices, share counts, issuance costs, terms | 1998-03-06 | 1999-01-22 | note disclosure covering 1993–1997 |
| Competition named in five categories | 1998-03-06 | 1999-01-22 | in-period statement about 1998 |
| Intel i740, February 1998 | 1998-03-06 | 1999-01-22 | contemporaneous (one month after the event) |
| SGI suit | **1998-04-24** | 1999-01-22 | contemporaneous, 15 days after notification |
| S3 and 3Dfx suits; answers and counter-claims | **1998-11-20** | 1999-01-22 | contemporaneous |
| Amkor / Siliconware assembly; TSMC "primary manufacturer"; 1998 TSMC volume-production difficulty | **1998-11-20** | 1999-01-22 | contemporaneous |
| Quarterly table; the two one-month columns; the four-date balance sheet | **1998-11-20** | 1999-01-22 | contemporaneous unaudited and audited data |
| RIVA TNT; .35 micron specs; March 1998 / July 1998 shipments | **1998-11-20** | 1999-01-22 | contemporaneous |
| 3Dfx–STB acquisition and "sales to STB will be reduced significantly" | **1998-12-23** | 1999-01-22 | contemporaneous, forward-looking against interest |
| VideoLogic, SGI/Evans/Intergraph added; Chromatic dropped as acquired | **1998-12-23** | 1999-01-22 | contemporaneous |
| Nine-month customer mix 40/28/12 | not tested (see note) | 1999-01-22 | contemporaneous as printed in the final draft |
| "$19.7 million" of preferred financing | 1998-03-06 | 1999-01-22 | retrospective aggregate |
| The three founder sentences and biographies | 1998-03-06 | 1999-01-22 | registrant FOUNDER CLAIM about 1993 |
| Over 40 → over 180 awards | 1998-03-06 → 1999-01-22 | — | marketing claim; the escalation is the fact (P1K06, part 1) |

**About the one row with a gap.** The nine-month customer-mix percentages were read in the 424B4; this pass did
**not** test which of the two January 1999 amendments first printed them, so the entry date is not established
and the row is marked rather than guessed. The adjacent rows *were* tested by string counts across all nine held
files (`3Dfx` 5→4→40→48; `primary manufacturer` 0→1; `Amkor` 0→2; `Siliconware` 0→2→3; `STB will be reduced`
0→3; `VideoLogic` 0→4; `Evans` 0→3; `January 26, 1997` 0→4→19), which is why their dates are firm and the
untested one is not. **Method stated so the numbers are checkable:** every count quoted here is a `grep -c`
**line** count — the number of lines containing at least one match, case-sensitive unless the passage says
otherwise — not a token total, and all were run against the stored `.txt` accession files listed in the sources
register, whose dates come from `_MANIFEST.csv`/`submissions.csv` and not from filenames (RD-127).

**What §N forbids, concretely.** (i) Treating the 1998-12-23 sentence about STB as evidence of the 1997
relationship — it is December 1998's knowledge about 1997's dependence. (ii) Treating the November 1998 yield
admission as the consequence of the 1996 decision. (iii) Reading "1997" figures as fiscal: they are calendar
(part 1 §Boundary 4), and the first fiscal-basis comparative is the nine months ended **October 25, 1998**,
which is 38 weeks and not nine calendar months (§S). (iv) Counting the retrospective narrative as corroborated
because seven drafts print it: one instrument, seven printings.

## O

STATUS: WRITTEN 2026-09-26

**Evidence class on every row, because "failure" is where retrospective language enters most easily (§7
format adapted: a failure is recorded with its carrier, not with its lesson).**

| # | Failure, as filed | Date / basis | Evidence class | Magnitude | What it does NOT show |
|---|---|---|---|---|---|
| O1 | First product withdrawn; second product's development ceased | Q1 1996 (both drafts) | FACT as disclosed | the NV1 was the company's only 1995–96 revenue | whether any inventory was written off — no write-down is printed |
| O2 | Negative gross margin in the first full product year | calendar 1995 | FACT (audited-basis column) | gross loss $(367)K on $1,182K | cause: price, yield or inventory is not stated |
| O3 | The largest loss of the stage | calendar 1995 | FACT | operating $(6,470)K, net $(6,377)K | proximity to stopping, which is not measured anywhere |
| O4 | Low manufacturing yields at ST | December 1997 | FACT, self-disclosed | not costed | how much of that quarter's $1,424K profit it consumed |
| O5 | Volume-production failure on two successive products at the new fabricator | March 1998 (RIVA128ZX), July 1998 (RIVA TNT) | FACT, self-disclosed | quarter ended 1998-07-26: gross loss $(827)K, net loss $(9,652)K | root cause; whether the foundry, the design or the schedule |
| O6 | Three patent suits by competitors, with an admitted remedy set including ceasing sales or taking a licence | notified 1998-04-09, 1998-05-11, 1998-09-21 | FACT (pleaded disclosures) | "significant expense"; outcome UNKNOWN | merit: "meritorious defenses … vigorously" is a company belief |
| O7 | 63% of 1997 revenue owed to a customer being bought by one of the plaintiffs | disclosed 1998-12-23 about 1997 | FACT as disclosed + INFERENCE on exposure | STB 63%; 40% still in the nine months to 1998-10-25 | whether the acquisition completed, and when: not in held bytes |
| O8 | The receivable allowance rose to $3,506K while three customers held all receivables | 1997-12-31 → 1998-10-25 | FACT as printed | $100K/$349K/$3,506K across the stated dates | which customer, and whether anything was actually written off |
| O9 | "Financial and management controls, reporting systems and procedures are very limited" | 1998-03-06 through the offering | FACT as disclosed | the company's own adjective | what was built afterwards — `(PB)` |
| O10 | The FY1997 loss figures moved between drafts of one registration statement with no explanatory note | 1998-03-06 → 1998-11-20 | FACT about the printings | $899K of operating expense | whether any outside reader could have known before the amendment |
| O11 | Two material contracts were left blank-dated or unfiled in the exhibit index | 1998-03-06 | FACT (the index's own asterisk and blank date) | the ST Agreement and the underwriting agreement | whether they were filed after effectiveness; not read here |

**Failures with no carrier in this corpus, and therefore absent from the table:** any product recall (the word
appears only prospectively, in a risk factor about possible recalls); any stated loss of a customer as a past
event; any missed quarter — revenue never falls in a printed period except the quarter ended July 26, 1998, and
that fall is attributed to yields and to being unable "to timely supply such product"; any litigation outcome;
and **any going-concern language at all**, whose absence this pass verified by search and which is itself a
datum about a company that was, on its own numbers, repeatedly short of money.

## P

STATUS: WRITTEN 2026-09-26

**Discipline (§7 decisions format, and part 1's decisions.csv wording).** `state_before`,
`information_available` and `unknowns` are written from held text; `alternatives` records only what a held
document prints as an alternative, and where none is printed the cell says so; `actual_result` stays inside the
window. Tags `P1D04`+ continue part 1's three decision rows.

| Date | Decision | State before | Information available in-period | Unknowns | Alternatives | Constraints | Rationale | Expected result | Actual result | Evidence | Conf |
|---|---|---|---|---|---|---|---|---|---|---|---|
| by 1998-03-06 (as disclosed) | **Take development money from a third party for the second product** instead of funding it internally | NV1 shipping, NV2 in development, revenue $0→$1.2M | the company's own credits: $2.0M (1995) and $3.0M (1996) booked as reductions to R&D | who the third party was; what it received besides a credit | **NONE PRINTED** | operating cash use of $6.1M in 1995 | not printed; the funding is what the company itself named as the reason 1996 burn fell to $300K | a funded second product | the second product was cancelled in 1996 and a $2,500K advance still sat in accrued liabilities at 1996 and 1997 | S-1/A 1998-03-06 l.2003-2010; 424B4 l.2223-2236 | Medium |
| 1996–1998 (disclosed 1998-11-20) | **Move fabrication from ST to TSMC and split assembly/test to Amkor and Siliconware** | ST fabricated, assembled, tested, licensed and resold the product; December 1997 yields | the ST yield event; TSMC already engaged "on a purchase order basis"; "no readily available alternative source of supply for any specific product" | when the shift was decided; whether ST's capacity or ST's competing position drove it | the licence to ST was **kept** while the manufacturing moved — the only alternative visible in the text | "the lead time needed to establish a strategic relationship with a new manufacturing partner could be several months"; "wafer requirements represent a small portion of the total production capacity of TSMC" | not printed | supply independent of a competitor-reseller | 1998 volume-production difficulties on both new parts and a negative-gross-profit quarter | 424B4 l.802-830, l.1297-1312, l.3404-3406 | Medium |
| 1998-07 / 1998-08 | **Borrow $11.0M from three customers on non-interest-bearing subordinated paper convertible at 90% of the offering price** | revenue up 16× year-on-year, inventory and receivables exploding, one profitable quarter behind, one loss quarter ahead | its own cash ($6.5M at 1997-12-31), lease obligations, the stated absence of bank debt | which three customers; what the notes cost in margin or priority | a bank line — and one appears at 1998-10-25 for $5.0M, so both routes were used rather than chosen between | "subordinated to certain senior indebtedness"; conversion contingent on an IPO by 1998-12-31 or a fixed $7.00 fallback on 1999-01-15 | not printed | working capital for the next product generation | converted on 1999-01-15 into 1,571,429 shares (the conversion itself is printed in the same lineage) | 424B4 l.5825-5846; part 1 P1Q19 | High as to terms; Medium as the reading "a decision under constraint" |
| by 1999-01-22 | **Give up contract funding as a financing method** | $5.0M of NV2 credits and $4.3M of ST credits had reduced reported R&D across 1995–1997 | the ST support obligation expired with calendar 1998; royalty revenue expected to fall | why the company closed the channel that had cheapened its R&D line | **NONE PRINTED** | "does not expect contract funding in the future" | stated as an intention, not a rationale | R&D reported gross of customer money from 1999 | not used — `(PB)` | 424B4 l.2335-2338 | High as to the statement; reason UNKNOWN |

## Q

STATUS: WRITTEN 2026-09-26

**Consequences inside the window only, each with the mechanism it is allowed to have.**

* **Validation signals the record supports** (tags `P1V06`+): two private rounds priced upward before any
  revenue ($0.50 → $1.80); a first product that shipped and sold, at a negative margin; a paying development
  sponsor for the second product; quarterly product revenue of $5,225K then $22,055K after the re-architecture;
  two profitable quarters by the boundary ($1,424K, $7,141K); a first profitable **month** ($1,347K, January
  1998); a buyer set that widened from two names at 94% to three at 80%; and customers willing to lend
  $11.0M interest-free. Each demonstrates only what its own sentence says. The last two arguably *reduce*
  independence rather than increase validation: a customer who lends you money is not the same kind of signal
  as a customer who buys, and the class on that row is INFERENCE.
* **The negative signals were filed in the same instrument as the positive ones.** The prospectus that prints
  $52,303K of quarterly revenue also prints: a largest customer being acquired by a patent plaintiff with
  sales expected to "be reduced significantly"; three suits seeking injunctions; a foundry owing no minimum
  quantity; controls that are "very limited"; $48.0M of manufacturing commitments; a receivable allowance up
  from $100K/$349K to $3,506K; inventory of $17,193K against cash of $12,461K. **Mechanism connecting the two
  sets: UNKNOWN** — no internal document weighs them, and any sentence claiming the company "knew" which way
  the balance would fall would be hindsight.
* **Consequences that are genuinely of Stage 2, named and flagged.** The STB channel loss, the outcomes of the
  three suits, the expiry of the ST support obligation on 1998-12-31, the expected fall in royalty revenue in
  the quarter ending 1999-01-31, and the manner in which the preferred converted are all **open at the
  boundary**. They enter `data_gaps.csv` with follow-up tasks rather than being resolved here; the FY1999
  10-K405 (on disk, `(PB)`) is the first carrier that could close three of them, and it is a Stage-2 document.
* **The end-of-stage snapshot**, in part 1's frame and extended by this pass's reads. At 1999-01-21 the
  registrant sold three Direct3D-compatible products through seven named add-in board houses, with 80% of the
  last nine months' revenue in three of them; fabricated at TSMC on a purchase order with no minimum quantity;
  assembled and tested at two firms with no long-term agreements; owed $11.0M to three customers and $5.0M to a
  lender; carried $48.0M of manufacturing commitments and $4,515K of gross lease obligations; had been sued by
  three competitors within ten months and had counter-claimed validity in each; had an accumulated deficit of
  $17,074K and 184 employees; was governed by an amended charter whose execution date was blank; and had, in
  the whole of its public record, exactly two documents signed by people who were not it.

### Q.1 Claim records for §O and §Q

P1-55 Claim: The company disclosed three patent suits and answered each with counter-claims that the patents are invalid and not infringed, and it printed the adverse remedies it could face. — Date: 1998-04-09 / 1998-05-11 / 1998-09-21 (notifications) — Source path: sources/sec/0001012870-98-003021_0001012870-98-003021.txt l.984-1021; sources/sec/0001012870-99-000192 l.3782-3812 (Business—Legal Proceedings) and l.889-911 (Risk Factors) — Source date: 1998-11-20 / 1999-01-22 — Tier: 1 — Class: FACT (statutory disclosure of pleaded matters); outcomes UNKNOWN — Passage: "the Company could be required to do one or more of the following: pay substantial damages (including treble damages); permanently cease the manufacture, use and sale of any infringing products" — Conf: High for the suits' existence, Low for any prediction about them — Corroboration: 1 lineage; no docket held — Conflicts: U.113
P1-56 Claim: The company reported a negative gross margin in the quarter ended July 26, 1998, the largest single-period loss in the corpus, and attributed it to yield problems and inability to supply. — Date: quarter ended 1998-07-26 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.2466-2516, l.515-520, l.3399-3402 — Source date: 1999-01-22 — Tier: 1 — Class: FACT (unaudited quarterly table plus self-disclosed cause) — Passage: "The lower yields resulting from such difficulties resulted in higher expenses and lower revenues in the quarter ended July 26, 1998, as the Company was not able to timely supply such product to its customers." — Conf: High — Corroboration: 1 lineage — Conflicts: U.104
P1-57 Claim: No in-window draft of this registration statement contains going-concern language, and the company reported no bad-debt write-offs through 1997. — Date: window-wide — Source path: sources/sec/ (search of the seven held drafts plus the 424B4) — Source date: 2026-09-26 — Tier: 1 — Class: FACT about this corpus, NOT a finding that none existed elsewhere — Passage: "Although the Company has not experienced any bad debt write-offs to date, there can be no assurance that the Company will not be required to write off bad debt in the future" — Conf: High as to the corpus — Corroboration: 0 — Conflicts: None
P1-58 Claim: By the last measured date the company's growth was carried on supplier payables, customer loans and a drawn line rather than on earnings. — Date: 1998-10-25 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.5205-5262, l.5825-5846 — Source date: 1999-01-22 — Tier: 1 — Class: INFERENCE from FACTs as printed; mechanism named in §M.3 — Passage: "Accounts payable................ $ 277 $ 11,572 $ 15,312 $ 46,370" — Conf: Medium — Corroboration: 1 lineage — Conflicts: None

P1-59 Claim: The registrant stated that moving production away from ST would increase its infringement risk because ST's third-party patent licences would no longer cover its products, and that it had agreed to indemnify certain customers against infringement claims. — Date: as printed 1999-01-22 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.3700-3716 — Source date: 1999-01-22 — Tier: 1 — Class: FACT as disclosed; the only held sentence naming a mechanism that links the manufacturing switch to the litigation — Passage: "As the Company's products are manufactured by TSMC or other manufacturers, such licenses will no longer benefit the Company and therefore the risk of a third-party claim of patent infringement against the Company will increase." — Conf: High — Corroboration: 1 lineage — Conflicts: U.106
P1-60 Claim: The company agreed to indemnify certain customers for third-party infringement claims arising from the sale of its product. — Date: as printed 1999-01-22 — Source path: sources/sec/0001012870-99-000192_0001012870-99-000192.txt l.3711-3713 — Source date: 1999-01-22 — Tier: 1 — Class: FACT as disclosed; which customers and what cap are UNKNOWN — Passage: "The Company has agreed to indemnify certain customers for claims of infringement arising out of sale of the Company's product." — Conf: High — Corroboration: 1 lineage; no indemnity agreement held — Conflicts: None

## R

STATUS: WRITTEN 2026-09-26

**§R continues part 1's conflict series.** P1K01–P1K07 are part 1's, are not restated or renumbered, and the
reference to P1K01 below is a *narrowing* of it, not a duplicate. Rows P1K08+ are this volume's, in the §7
conflict format (CLAIM A / CLAIM B / WHY THEY DIFFER / EVIDENCE WEIGHT / BEST-SUPPORTED INTERPRETATION /
RESIDUAL UNCERTAINTY / CONFIDENCE), each with the `U.` anchor declared in §U.

**P1K08 — the FY1997 restatement's shape (narrows P1K01).** CLAIM A: the March 1998 S-1 prints calendar-1997
net loss $(2,691)K, quarterly rows (1,176) (1,265) (2,413) 2,163, deferred-comp grants $2,100K and amortisation
$62K. CLAIM B: the December 1998 amendment and the 424B4 print $(3,589)K, quarters (1,176) (1,265) (2,572)
1,424, grants $4,277K and amortisation $961K. WHY THEY DIFFER: $2,177K of additional 1997 stock-option deferred
compensation was recognised, $899K of it amortised into 1997 expense (cost of revenue 18 + R&D 471 + SG&A 410),
and the accumulated deficit moved by the resulting $898K. EVIDENCE WEIGHT: the later printing is the one
declared effective and sold; **both** printings foot internally, and the quarterly table pins the movement to
two quarters — more than part 1 could establish. BEST-SUPPORTED INTERPRETATION: carry $(3,589)K; the March
figures are SUPERSEDED-DRAFT rows; the mechanism is stock-based-compensation amortisation, **DERIVED,
Confidence Medium**, because no sentence states it. RESIDUAL UNCERTAINTY: why the grants were re-measured, and
whether an audit adjustment or a policy judgment under the intrinsic-value method drove it, is UNKNOWN; the $1K
equity drift (6,896 → 6,897) is rounding and is recorded as such. CONFIDENCE: High on arithmetic, Medium on
explanation.

**P1K09 — the customer percentages' two bases.** CLAIM A: "Sales to STB and Diamond accounted for 63% and 31%,
respectively, of the Company's **total revenue** in 1997." CLAIM B: "**Product revenue** from STB … and
Diamond … accounted for 63% and 31%, respectively, of the Company's 1997 revenue." WHY THEY DIFFER: the first
takes the denominator as $29,071K, the second as the $27,280K product line, yet both print identical
percentages, so at most one is literally true. EVIDENCE WEIGHT: one lineage, both in the final instrument (MD&A
and the note), no reconciliation anywhere. BEST-SUPPORTED INTERPRETATION: quote the registrant's own words and
name the denominator when converting to dollars. RESIDUAL UNCERTAINTY: up to 4.5 points of denominator, about
$1.1M of 1997 revenue, unallocated between the readings. CONFIDENCE: High that the ambiguity exists; the
underlying sales are unknowable from this corpus.

**P1K10 — the January one-month labels.** CLAIM A: the notes' running header and the interim-information note
say the unaudited data are "as of **January 26, 1997** and September 28, 1997", and the statement index and the
summary table print a column "one month ended **January 26, 1997** (unaudited)". CLAIM B: the EPS reconciliation
table prints the same period as "**One month ended January 28, 1997**" with net loss $(522)K, and prints the
1998 transition month as "**One month ended January 26, 1998**" with net income $1,347K, while the statements
themselves label that column **January 31, 1998**. WHY THEY DIFFER: the *values* match across the two labels, so
the document names two periods four ways rather than reporting four periods. EVIDENCE WEIGHT: the structured
presentations (statements, summary table) and the FY1999 10-K405's identical "one month ended January 31, 1998"
outrank a note table's captions. BEST-SUPPORTED INTERPRETATION: the transition month is the one month ended
January 31, 1998, net income $1,347K; a January-1997 unaudited month of $190K revenue and $(522)K loss is a real
printed comparative; the "26/28" captions are calendar variants chosen by different drafters of the same
52/53-week company. This **refines** part 1's P1K05, which preserved the string and used it for nothing.
RESIDUAL UNCERTAINTY: which convention each caption intended is UNKNOWN; the figures are not in doubt.
CONFIDENCE: High.

**P1K11 — who manufactured the company.** CLAIM A (1998-03-06): "Substantially all of the Company's products
currently are manufactured by ST in Crolles, France", TSMC "recently established … on a purchase order basis".
CLAIM B (1998-11-20 onward): "the Company **in the past utilized ST and currently utilizes TSMC**", TSMC is
"the Company's **primary manufacturer**", and ST is past tense for assembly and test as well. WHY THEY DIFFER:
eight months of operating history, a yield failure, and a document being updated for effectiveness. EVIDENCE
WEIGHT: both are true at their own dates; the later is nearer the boundary and is corroborated *within the same
lineage* only by the token counts (§N). BEST-SUPPORTED INTERPRETATION: a foundry switch occurred between the
March and November 1998 drafts and is among the two or three most consequential events in the second half of
the stage. RESIDUAL UNCERTAINTY: the decision date, the qualification path, and whether ST's exit from
fabrication was chosen by either party are UNKNOWN. CONFIDENCE: High on sequence, Medium on causality. The
registrant's own consequence — that the move ended ST's patent umbrella and would **increase** infringement
risk — is in P1-59 and is the one mechanism chain the filings do draw.

**P1K12 — one fiscal quarter, two end-dates.** CLAIM A: "yield problems … during the quarter ended **July 28,
1998**". CLAIM B: "higher expenses and lower revenues in the quarter ended **July 26, 1998**", and the
quarterly table's column heading is July 26, 1998. WHY THEY DIFFER: two drafters, one document, one quarter; the
table's neighbouring headings (April 26, October 25) are Sunday endings consistent with the stated convention,
and July 28 belongs to none of them. EVIDENCE WEIGHT: the table column plus the Business section outrank an
incidental risk-factor sentence — which is exactly RD-127's rule that an instrument's date comes from the
structured record. BEST-SUPPORTED INTERPRETATION: the quarter ended **July 26, 1998**; "July 28" is a stale or
mistaken date surviving in a risk factor. RESIDUAL UNCERTAINTY: whether internal reports used a different
period end is UNKNOWN. CONFIDENCE: Medium-High.

**P1K13 — when the fiscal-year change took effect.** CLAIM A (Note 1): "Effective **January 1, 1998**, the
Company changed its fiscal year-end financial reporting period to January 31 … In addition, effective
**February 1, 1998** the Company changed its fiscal year end from January 31 to a 52- or 53-week year ending on
the last Sunday in January." CLAIM B (MD&A and the quarterly preamble): "Effective **January 31, 1998**, the
Company changed its fiscal year-end financial reporting period to a 52- or 53-week year…" WHY THEY DIFFER: the
note describes two steps with two dates; the MD&A compresses them and attaches the transition month's end date
to the whole change. EVIDENCE WEIGHT: the note is the financial-statement disclosure and is coherent with the
existence of a calendar "one month ended January 31, 1998" column, which only makes sense if the January-31
year-end came first. BEST-SUPPORTED INTERPRETATION: a **two-step** change — calendar-January year-end effective
January 1, 1998 (producing the audited one-month transition period), then the 52/53-week convention from
February 1, 1998. RESIDUAL UNCERTAINTY: immaterial to any figure; the hazard is in quoting. CONFIDENCE:
Medium-High.

**P1K14 — the conversion condition the offering's own assumption does not meet.** CLAIM A: automatic
conversion of the preferred requires an IPO where "aggregate proceeds exceed $15,000,000 **and the offering
price equals or exceeds $10.00 per share**". CLAIM B: pro-forma common of **25,065,226** shares is reachable
only if all 9,327,087 preferred shares converted, while the December 1998 amendment's capitalization footnote
assumes **$8.00** per share. WHY THEY DIFFER: an instrument-level condition versus a presentation that assumes
the outcome. EVIDENCE WEIGHT: both are printed in the operative document; the reconciling fact — a two-thirds
vote, a waiver, or an amended charter — is absent. BEST-SUPPORTED INTERPRETATION: the preferred converted **by
consent rather than by satisfaction of the price condition**, marked INFERENCE. RESIDUAL UNCERTAINTY: the
mechanism, its date, and whether the blank-dated Ex-3.1 A&R charter was the instrument that changed the terms
are UNKNOWN. CONFIDENCE: Medium on the inference, High on the tension. Note the customer notes' trigger is a
*different and lower* threshold ($10.0M of gross proceeds), so two instruments in one note have two tests and
only one is satisfied on the face of the document.

**P1K15 — the 28,595,976 question.** CLAIM A: "Upon the closing of this offering, the Company will have
outstanding an aggregate of **28,595,976** shares of Common Stock, (assuming no exercise of outstanding options
and warrants)". CLAIM B: the capitalization table's pro forma as adjusted is **28,565,226**. WHY THEY DIFFER:
two measurement dates (December 31, 1998 and October 25, 1998) and 30,750 shares. EVIDENCE WEIGHT: the ownership
footnote's basis line (23,524,547 as-converted at December 31, 1998) makes each number right at its own date, so
this is a basis difference and not a contradiction — the same class as part 1's P1K04 headcount trap.
BEST-SUPPORTED INTERPRETATION: use 28,595,976 with its date or not at all. RESIDUAL UNCERTAINTY: the identity of
the 30,750 shares is UNKNOWN; the only printed 1998 issuance row is 25,000 shares for $25K. CONFIDENCE: High on
the reconciliation, Low on the residual.

**P1K16 — where part 1's enumeration left a column out.** CLAIM A (`(Nvidia S1 §Boundary 4, part_1)`): the
summary table's columns are the 1993 stub, 1994–1997, and two nine-month periods, so the "one month ended
January 26, 1997" string "corresponds to no column in its own summary table". CLAIM B (this pass): the header
row at l.1941 prints **nine** columns, two of them one-month columns (January 26, 1997 and January 31, 1998),
both carrying values. WHY THEY DIFFER: a column count taken by reading part of a wrapped table instead of
listing its header cells — RD-124's fourth-pass failure mode arriving in an inherited premise. EVIDENCE WEIGHT:
the bytes. BEST-SUPPORTED INTERPRETATION: part 1's decision to keep the string verbatim and use it for nothing
was right; the reason given for it was wrong, and the period is now quantified (§M.2, §S.3). RESIDUAL
UNCERTAINTY: none for the figures; the merge must not carry the "no column" statement forward. CONFIDENCE: High.

## S

STATUS: WRITTEN 2026-09-26

**Why this section is mandatory (§6, §7 adaptation).** The registrant's reporting basis changed twice inside the
last two years of the stage and the changes are *documented inconsistently* (P1K13), so any Stage-1 figure
quoted without its basis can mislead. Part 1 established the headline rule — calendar 1993–1997; a 52/53-week
January year-end from 1998; prior periods not restated — and preserved the January-1997 footnote period verbatim
while using it for nothing. Both moves were right in kind; here the rule is extended to every period the corpus
prints, and the preserved period is finally read.

### S.1 The period inventory, each with its basis

| Printed period | Basis | Where it appears | Note |
|---|---|---|---|
| Period from inception (April 5, 1993) to December 31, 1993 | calendar stub, audited | Summary Financial Data; the only audited 1993 figures | 8 months 26 days |
| Years ended December 31, 1994 / 1995 / 1996 / 1997 | calendar; 1995–97 audited by KPMG Peat Marwick, 1994 audited but "not included in this Prospectus" | all annual figures | the 1997 column is RESTATED across the lineage (P1K08) |
| **One month ended January 26, 1997** | calendar January month, **unaudited** | summary table, statements of operations, cash flows, notes header | also captioned "January 28, 1997" in the EPS table (P1K10): $190K revenue, $(522)K net loss |
| **One month ended January 31, 1998** | calendar January month, audited-basis | the same four places; the FY1999 10-K405 carries the same label | the transition month: $13,331K revenue, $1,347K net income; captioned "January 26, 1998" in the EPS table |
| Nine months ended September 28, 1997 | Sunday-ending comparative, **unaudited** | summary table, statements, quarterly table | the MD&A also calls a comparative "the nine months ended **September 30, 1997**" (U.103) |
| Nine months ended October 25, 1998 | fiscal, 38 weeks | every 1998 figure in the volume | **38 weeks**, not nine calendar months |
| Quarters ended March 30 / June 29 / Sept. 28 / December 31, 1997 | Sunday-ending, unaudited, "derived from the internal quarterly financial reports" | quarterly table | the sentence above it calls fiscal-1997 quarters "ended March 31, June 30, September 30 and December 31" — calendar dates for the same four quarters (U.103) |
| Quarters ended April 26 / July 26 / October 25, 1998 | fiscal 1999, unaudited | quarterly table | "July 26" also printed "July 28" in a risk factor (P1K12) |
| Balance-sheet dates December 31, 1996 and 1997; January 31, 1998; October 25, 1998 | four dates across two regimes | the four-date balance sheet | the 1996–97 columns are calendar year-ends; 1998's two are the transition month-end and a fiscal quarter-end |

### S.2 Five rules imposed on every register row emitted here

1. **A "1997" figure is calendar; a "fiscal 1999" figure is a 52-week year and is not additive to it** without
   the transition month. `3,589 (calendar 1997 net loss)` and `1,347 (one month ended January 31, 1998 net
   income)` are different periods of different lengths and are never combined in this volume.
2. **"Nine months ended October 25, 1998" is 38 weeks** (12 + 13 + 13 from February 1, 1998). Any run-rate
   derived from it states 38 weeks; the corpus never prints the lengths, so the derivation is the reader's and
   must be shown.
3. **Fiscal 1999's first and fourth quarters are 12 and 14 weeks**, so a quarterly comparison across them is
   partly a length artifact; the company supplies the other half itself — "the tendency of PC sales to decrease
   in the second quarter and increase in the second half of each calendar year".
4. **Unaudited is a basis, not a hedge.** The quarterly table, the January-1997 month and the September-1997
   nine months are labelled unaudited and internally derived; 1995–97 annual columns are covered by the
   auditor's report. No row here mixes the two without naming which.
5. **Percentage bases are named, not assumed.** Total vs product revenue (P1K09); royalty share, where the
   printed "6%" reconciles to 1,791/29,071 = 6.16% for calendar 1997, 312/5,537 = 5.6% for the nine months to
   September 28, 1997 and 5,945/92,700 = 6.4% for the nine months to October 25, 1998 (derived, High); and the
   receivable-allowance sentence that gives **three dates for four balance-sheet columns** (§M.3), carried as a
   caveat rather than resolved.

### S.3 The January-1997 footnote period, put to work

Part 1 kept the string and used it for nothing. Read as a column it supports three statements and no more.
**(a)** It is the smallest reported revenue period in the corpus, $190K, and is the floor against which the
Q4-1997 quarter ($22,055K product) and the October-1998 quarter ($51,150K product) should be read. **(b)** It
lost $(522)K — about 17% of the whole of calendar-1996's net loss in a single month — which shows the 1997
losses were front-loaded before the product turn, the first two quarters of 1997 printing $(1,176)K and
$(1,265)K on product revenue of $65K and $6K. **(c)** Paired with January 1998 — $(522)K against $1,347K on the
same January-month basis thirteen months apart — it is the cleanest before/after in the corpus, with the left
side unaudited and the right side audited-basis. It does **not** support a runway calculation, and §L.1 blocks
reading it as the moment of danger: on the figures part 1 carries, 1993 and 1994 were worse in every absolute
sense available.

## T

STATUS: WRITTEN 2026-09-26

**The independence ledger (§3), kept as an accounting rather than an assertion.** An item counts here only if its
**origin** is independent of the registrant's narrative; authorship by a paid adviser is independent authorship
and *not* independent interest, and that distinction is drawn explicitly because it is where this corpus could
drift into false corroboration.

| Held item | Origin | Independent of the registrant's narrative? | Usable as | Limit |
|---|---|---|---|---|
| S-1 1998-03-06 + six held amendments + 424B4 1999-01-22 | registrant and its counsel | **No — one lineage** | every Stage-1 statement, single-source | repetition across drafts is version evidence |
| Ex-4.3 Investors' Rights signature pages, 1997-08-19 | ~30 counterparties: JAFCO entities, eight Sequoia vehicles, Sutter Hill, ANVEST, Worldview, Itochu, **Sega Enterprises**, Stanford, founders in person | **Yes — third-party signatures** | that identifiable parties held rights and contracted for information and inspection | names holders as of 1997, not purchasers of 1993; the company selected what to file |
| Ex-10.11 Amdahl sublease, 1995-02-16, as amended 1995-03-01 and 1995-09-01 | Amdahl Corporation; landlord Oakmead Investments | **Yes** | premises, rent, square footage, dated amendments | a facility document only |
| Ex-3.1 Delaware certificate, subscribed 1998-02-23 | Mitchell R. Truelock, Cooley Godward, sole incorporator | **Partly** — an officer of company counsel | that the Delaware vehicle was formed on a dated instrument | the operative A&R charter is blank-dated (part 1 P1K02) |
| KPMG Peat Marwick LLP report and Ex-23.1 consent (renamed KPMG LLP by the December draft) | auditor | **Yes in kind** | that 1995–97 statements were audited and included in reliance on the report | an audit of management's assertions is not an independent count of customers or units |
| Opinion of the Law Offices of Michael A. Glenn, patent counsel (cited at 424B4 l.3806-3810) | retained outside counsel | **Yes in authorship, No in interest** | that a validity/non-infringement opinion existed by January 1999 | the opinion is not filed; retained by the company |
| Underwriter syndicate, eleven firms, 3,500,000 shares allocated (l.4981-4997) | third parties bearing §11 liability | **Yes in kind** | the size and composition of the offering's distribution | underwriters' counsel reproduces the company's text (part 1 §Header) |
| **SC 13G filed 1999-08-06** by **Creative Technology Ltd** and **CTI Limited**: 2,192,785 shares, ~7.5% of the 29,308,984 outstanding at 1999-04-30 | **a named AIB customer, filing on its own behalf** | **Yes — the only held document authored by a counterparty describing the registrant** | a route, and the fact that a customer later reported an equity stake | **`(PB)`**: it post-dates the boundary and witnesses no Stage-1 fact; used in no §G–§S claim |
| `sources/_index/submissions.csv`, `sources/sec/_MANIFEST.csv` | SEC / intake tool | **Yes (catalog)** | instrument dates, existence, and which rows are blank | an index witnesses no events; 30 of 69 in-window rows have a blank primary document (part 1) |
| `research/A_chronology_feasibility.md`, `A3_intake_regrade.md`, `A4_harvest_mine.md` | prior passes' dossiers | **No — not sources** | leads, and the provenance of the premises part 1 refuted | cited as dossiers, never counted |

**What the ledger cannot buy.** No customer-side in-window document exists (no order, invoice, design-win
notice or AIB announcement); no supplier-side document exists (the ST Agreement is summarised, never filed —
U.117); no competitor document, no analyst report and no press body of 1993–1998 exists in this corpus. The
rule part 1 enforced therefore holds for every claim in this volume: statements about 1993–1998 *decisions* are
FOUNDER CLAIM or RETROSPECTIVE INTERPRETATION about the event and FACT about the printing. The two genuinely
third-party in-window carriers bear on **who owned** and **where they worked**, never on **who bought**.

## U

STATUS: WRITTEN 2026-09-26

**Anchor block for part 2.** Each `U.nnn` is this volume's conflicting-evidence or open-question entry; `P1Knn`
is the same item's register key and the two series are aliases, declared here so a citation resolves. Part 1's
P1K01–P1K07 keep their own addresses in part 1 and are not re-declared. The seven-field conflict format is
carried in §R above and in the `conflicts.csv` cells below; §U is the index, not a second statement.

<!-- ANCHORS: U.101-U.118 -->

**U.101** — FY1997 net loss moved $(2,691)K → $(3,589)K inside one lineage; localised to Q3 $(159)K and Q4
$(739)K; mechanism = deferred-compensation amortisation +$899K (P1K08; narrows part 1's P1K01). *DERIVED, Medium.*

**U.102** — Two January months are captioned four ways: "January 26, 1997" (statements/header) vs "January 28,
1997" (EPS table); "January 31, 1998" (statements) vs "January 26, 1998" (EPS table); values identical (P1K10).

**U.103** — Fiscal-1997 quarter-ends printed as Sunday dates in the quarterly table and as calendar dates in the
sentence above it; "nine months ended September 28, 1997" in the statements vs "September 30, 1997" in the MD&A.
*Best-supported: the table's dates are the periods actually presented.*

**U.104** — "The quarter ended July 28, 1998" (risk factor) vs "July 26, 1998" (Business and the table column)
(P1K12). *Best-supported: July 26, 1998.*

**U.105** — Fiscal-year change effective January 1 then February 1, 1998 (Note 1) vs a single January 31, 1998
(MD&A/quarterly preamble) (P1K13). *Best-supported: a two-step change.*

**U.106** — ST fabricated "substantially all" products in March 1998 vs TSMC "the Company's primary manufacturer"
from November 1998, with the registrant's own notice that the switch ended ST's licence umbrella and would
increase infringement risk (P1K11, P1-59).

**U.107** — STB 63% / Diamond 31% stated once as a share of total revenue and once as product revenue of 1997
revenue (P1K09). *Residual: ~$1.1M of denominator.*

**U.108** — Post-offering shares 28,565,226 (basis 1998-10-25) vs 28,595,976 (basis 1998-12-31 via 23,524,547
as-converted); 30,750 shares unattributed (P1K15).

**U.109** — The preferred's automatic conversion needs ≥$10.00 per share; the document's assumed price is $8.00;
conversion is nevertheless presented. No consent or waiver held (P1K14, §J.5). *INFERENCE, Medium.*

**U.110** — Part 1's §Boundary 4 column enumeration is refuted by the header row: nine columns, two of them
one-month columns, so the January-1997 period is quantified (P1K16, §M.2, §S.3). *A named correction of an
inherited premise, not a silent edit.*

**U.111** — The 63% customer was being acquired by a patent plaintiff, disclosed in the same instrument that
reported that customer's 40% share of the last nine months (P1-36, §Q). *Completion date UNKNOWN.*

**U.112** — Whether the $2,500K balance-sheet advance and the $2.0M/$3.0M NV2 contract credits are the same
funding: no held sentence joins them (part 1 P1G04, §G.4). *Open, and narrowed to naming the third party.*

**U.113** — Suits dated by notification day (1998-04-09, 1998-05-11, 1998-09-21) vs month-only statements in the
same document; court filing dates not held (P1-35, §H.2).

**U.114** — "The Company operates primarily in one business segment in the United States" against fabrication in
Taiwan, assembly/test in Korea and the Philippines, earlier fabrication in France, investor notices c/o a Tokyo
building, and sales through US, Canadian and Israeli AIB makers. *Both printed; never reconciled in the text.*

**U.115** — Filed distress versus the absent rescue recollection: nine quantified distress facts against zero
carriers for any runway or rescue statement (part 1 §D.4, P1-12, P1-20; re-searched §G.5). *EMPTY with its
perimetre named; the recollection itself stays UNTRIED.*

**U.116** — First customer UNKNOWN with a narrowed perimetre; earliest named buyer of record is Diamond at 86% of
1995 revenue under a "sale and license" structure (§G.4, §G.5, §K.1). *The §10 trigger remains open.*

**U.117** — The ST Agreement and the underwriting agreement were blank-dated or "to be filed by amendment" and
are not filed in any held draft: the stage's two most consequential commercial instruments never entered the
public record inside it (P1-41, §K.5, O11).

**U.118** — Six in-window instruments are indexed with a blank `primaryDocument` and are not on disk: 8-A12B
1998-03-23, 8-A12G 1998-04-03, two RW 1998-05-07, 8-A12G 1999-01-12, S-1MEF 1999-01-22 (§K.11). *UNTRIED; a
listing defect is not an absence.*


---

## Register rows for merge

>>> REGISTER ROWS FOR MERGE <<<
STATUS: WRITTEN 2026-09-26

*Emit-only. **No register CSV at the company root was opened, created or edited by this pass** — there are
none (baseline `merge_census` output on this company before this emission: "no register CSVs at root or
research/ -- csv/anchors gates DID NOT RUN"), and a merge applies these. `stage` is the literal **`stage1`** on
every row (§13). All ids are dossier-local; global `source_id` blocks are minted centrally at merge (RD-123).
Headers are copied verbatim from `company_001_amazon/<register>.csv` and every block below was re-parsed with a
CSV reader after writing. The filing-lineage note (`same lineage as P1S01`) is carried on every registration row
because part 1's §3 rule is what the merge exists to enforce. **Emission defect reported rather than worked
around:** `validation.csv` and `failures.csv` have identical column sets, so `merge_census.match_register()`
scores them tied and returns `AMBIGUOUS:validation.csv,failures.csv` — part 1's combined 10-row block was
listed UNATTRIBUTED for this reason, and the same will happen to the two blocks below however they are marked.
They are still emitted as separate blocks with separate markers, per the emission contract, because the schema
in `company_001_amazon/` is the authority and a header invented to please the census would be worse than an
unattributed block. Tool defect filed in the report.*

>>> REGISTER ROWS FOR MERGE <<<

```csv
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
P1S08,stage1,"P1-35 §H.2 §N","Form S-1/A Amendment No. 1 (first held amendment)","NVIDIA Corporation",securities registration statement amendment,primary,1998-04-24,1998-04-24,2026-09-26,"EDGAR accession 0001012870-98-001089","sources/sec/0001012870-98-001089_0001012870-98-001089.txt (564,104 B per _MANIFEST.csv)",1,"CONTEMPORANEOUS for February-April 1998 events; registrant-retrospective for 1993-1997",High,"SAME LINEAGE AS P1S01 - never corroboration. Version role: first held draft to print the SGI patent suit; SGI token count jumps 4 to 44 here","SGI token count 44; January 26, 1997 count 0; primary manufacturer count 0","Date taken from _MANIFEST.csv filingDate which traces to the EDGAR index, not from the filename (RD-127)"
P1S09,stage1,"§N version trail","Form S-1/A Amendment No. 2","NVIDIA Corporation",securities registration statement amendment,primary,1998-06-08,1998-06-08,2026-09-26,"EDGAR accession 0001012870-98-001519","sources/sec/0001012870-98-001519_0001012870-98-001519.txt (440,312 B)",1,"CONTEMPORANEOUS as a printing; no new in-window event established",Medium,"SAME LINEAGE AS P1S01","SGI token count 49; 3Dfx count 4; NV2 under contract count 0","Read by token count only this pass; its prose was not opened line by line and nothing in it is cited as a fact"
P1S10,stage1,"§N version trail","Form S-1/A Amendment No. 3","NVIDIA Corporation; filed under agent accession 0000929624",securities registration statement amendment,primary,1998-07-27,1998-07-27,2026-09-26,"EDGAR accession 0000929624-98-001285","sources/sec/0000929624-98-001285_0000929624-98-001285.txt (626,995 B)",1,"CONTEMPORANEOUS as a printing",Medium,"SAME LINEAGE AS P1S01. Note the filer agent prefix differs from the registrant CIK block, which is why instrument dates come from the index","3Dfx count 4; Chromatic 5; January 26, 1997 count 0","Read by token count only"
P1S11,stage1,"P1-35 P1-39 P1-40 P1-49 §N §S","Form S-1/A Amendment No. 4 (the great revision)","NVIDIA Corporation",securities registration statement amendment,primary,1998-11-20,1998-11-20,2026-09-26,"EDGAR accession 0001012870-98-003021","sources/sec/0001012870-98-003021_0001012870-98-003021.txt (590,627 B)",1,"CONTEMPORANEOUS for the 1998 litigation, manufacturing and interim data; RESTATED for calendar 1997 against P1S01",High,"SAME LINEAGE AS P1S01 - the instrument that first prints the S3 and 3Dfx suits, TSMC as primary manufacturer, Amkor and Siliconware, the seven-quarter table and the two one-month columns","On September 21, 1998, the Company was notified that 3Dfx had filed a patent infringement lawsuit against the Company","3Dfx count 40 against 4-5 in every earlier draft; January 26, 1997 count 4 against 0 - the version clock for §N"
P1S12,stage1,"§N version trail","Form S-1/A Amendment No. 5 (January 13, 1999)","NVIDIA Corporation",securities registration statement amendment,primary,1999-01-13,1999-01-13,2026-09-26,"EDGAR accession 0001012870-99-000100","sources/sec/0001012870-99-000100_0001012870-99-000100.txt (425,132 B)",1,"CONTEMPORANEOUS as a printing; carries the final 1997 column",Medium,"SAME LINEAGE AS P1S01","January 26, 1997 count 19; STB will be reduced count 3; VideoLogic count 4","First held draft in which the January-1997 column caption appears 19 times; the 424B4 keeps the same count"
P1S13,stage1,"§G.1 §M","Form S-1/A Amendment No. 6 (January 20, 1999, one day before the prospectus)","NVIDIA Corporation",securities registration statement amendment,primary,1999-01-20,1999-01-20,2026-09-26,"EDGAR accession 0000898430-99-000180","sources/sec/0000898430-99-000180_0000898430-99-000180.txt (424,134 B)",1,"CONTEMPORANEOUS as a printing",Medium,"SAME LINEAGE AS P1S01; token profile identical to P1S12 and to the 424B4 on every string tested","SGI count 54; 3Dfx 48; January 26, 1997 count 19","Filed the day before the 424B4 and one day before the prospectus date printed on it; the sequence is index-derived"
P1S14,stage1,"§T independence ledger","Schedule 13G reporting beneficial ownership by Creative Technology Ltd and CTI Limited","Creative Technology Ltd; CTI Limited (not the registrant)",beneficial ownership report,primary,1999-08-04,1999-08-06,2026-09-26,"EDGAR accession 0001012870-99-002654, SEC File No. 005-56649","sources/sec/0001012870-99-002654_0001012870-99-002654.txt (14,950 B)",1,"(PB) for Stage 1 - post-dates the 1999-01-21 boundary and witnesses no Stage-1 fact",High,"THE ONLY HELD DOCUMENT AUTHORED BY A COUNTERPARTY DESCRIBING THE REGISTRANT, and the only genuinely independent origin in the corpus. Its independence is used to name a route and to complete the ledger, never to corroborate a Stage-1 figure","As of August 4, 1999, CTI Limited and Creative Technology Ltd. beneficially owned 2,192,785 shares of the Issuer's Common Stock","approximately 7.5% of the 29,308,984 shares outstanding as of April 30, 1999 per the issuer's proxy dated June 17, 1999; Creative is one of the seven named add-in board customers and 12% of the nine months to 1998-10-25"
P1S15,stage1,"§K.11 U.118","EDGAR index rows for six in-window instruments with a blank primaryDocument","U.S. Securities and Exchange Commission",regulatory index,primary,1998-03-23,2026-09-23,2026-09-26,"data.sec.gov submissions (via tools/sec_intake.py index)","sources/_index/submissions.csv columns filingDate,form,accession,reportDate,primaryDocument,source",1,"FACT-about-the-index",High,"The index cannot witness events; a blank primaryDocument is a listing or intake defect, not an absence of filing","1998-03-23 8-A12B 0001012870-98-000716; 1998-04-03 8-A12G 0001032210-98-000344; 1998-05-07 RW 0001012870-98-001201 and -001200; 1999-01-12 8-A12G 0001012870-99-000093; 1999-01-22 S-1MEF 0001012870-99-000186","None of the six is stored under sources/sec/. Dates are index-derived per RD-127; every reportDate cell in these rows is blank"
P1S16,stage1,"§K.12 ## Untried","Harvest-mine dossier for this company, re-read this pass for its UNANSWERED items","tools/harvest_mine.py output dossier research/A4_harvest_mine.md",internal dossier,secondary,1993-01-01,2026-09-26,2026-09-26,"local","research/A4_harvest_mine.md; research/A3_intake_regrade.md",4,"LEAD ONLY - never counts in a tier verdict (RD-124)",Medium,"A dossier is not a source. Recorded so the merge can see which family verdicts are inherited and which were measured","U9n74ngfDU8C | 1998-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED (and two siblings)","The three zero-byte items are Google Books volume ids fetched from the wrong host, so the correct state is UNTRIED at books.google.com, not UNANSWERED; the entity-bearing item 01.-nvidia-annual-reports has FY2005-FY2026 text layers"
```

>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
Nvidia,stage1,1997-03-30,quarter_total_revenue,65,USD thousands,P1S11 and P1S03 quarterly table,1999-01-22,"CONTEMPORANEOUS, unaudited, internal-report derived",High,not_derived,"Product 65, royalty 0. Calendar-1997 quarter, Sunday-ending label March 30. U.103"
Nvidia,stage1,1997-06-29,quarter_total_revenue,6,USD thousands,P1S11 and P1S03 quarterly table,1999-01-22,"CONTEMPORANEOUS, unaudited",High,not_derived,"Product 6, royalty 0; gross loss (144). The smallest revenue quarter in the corpus before the January 1997 month is counted"
Nvidia,stage1,1997-09-28,quarter_total_revenue,5466,USD thousands,P1S11 and P1S03 quarterly table,1999-01-22,"CONTEMPORANEOUS, unaudited",High,not_derived,"Product 5,154 plus royalty 312; first quarter with RIVA128 revenue"
Nvidia,stage1,1997-12-31,quarter_total_revenue,23534,USD thousands,P1S11 and P1S03 quarterly table,1999-01-22,"CONTEMPORANEOUS, unaudited",High,"65 + 6 + 5,466 + 23,534 = 29,071, which equals the printed calendar-1997 annual total","Product 22,055 plus royalty 1,479; the quarter part 1 called the first profitable quarter"
Nvidia,stage1,1997-12-31,quarter_net_income,1424,USD thousands,P1S03 quarterly table,1999-01-22,"CONTEMPORANEOUS, unaudited, RESTATED against P1S01",High,"basic EPS .10 on 14,074 weighted shares; diluted .06 on 24,942 shares","The March 1998 draft printed 2,163 for the same quarter; the movement is -739. U.101"
Nvidia,stage1,1997-09-28,quarter_net_loss,2572,USD thousands,P1S03 quarterly table,1999-01-22,"CONTEMPORANEOUS, unaudited, RESTATED",High,not_derived,"March 1998 draft printed 2,413; movement -159. With Q4 this accounts for the whole 898-899 restatement. U.101"
Nvidia,stage1,1998-04-26,quarter_total_revenue,28263,USD thousands,P1S03 quarterly table,1999-01-22,"CONTEMPORANEOUS, unaudited; fiscal basis, 12-week quarter",High,not_derived,"Product 24,642 plus royalty 3,621; net loss (1,021). Fiscal 1999 Q1 was a 12-week period, so a run-rate here is 12 weeks not a quarter-month"
Nvidia,stage1,1998-07-26,quarter_gross_loss,827,USD thousands negative,P1S03 quarterly table,1999-01-22,"CONTEMPORANEOUS, unaudited; fiscal basis, 13 weeks",High,"revenue 12,134 less cost of revenue 12,961 = (827)","The only negative gross-profit quarter printed. Net loss (9,652) is the largest single-period loss anywhere in the corpus. The risk factor dates the same quarter July 28, 1998. U.104"
Nvidia,stage1,1998-10-25,quarter_total_revenue,52303,USD thousands,P1S03 quarterly table,1999-01-22,"CONTEMPORANEOUS, unaudited; fiscal basis, 13 weeks",High,"(1,021) + (9,652) + 7,141 = (3,532), which equals the printed nine-month net loss","Product 51,150 plus royalty 1,153; net income 7,141; basic EPS .50, diluted .26 on 27,774 shares"
Nvidia,stage1,1997-01-26,one_month_total_revenue,190,USD thousands,P1S03 Selected Financial Data and F-4,1999-01-22,"CONTEMPORANEOUS, unaudited, calendar January month",High,not_derived,"CORRECTS PART 1 P1K05: the period is a printed column, not an orphan footnote string. Net loss (522), operating loss (516), gross profit 63. U.102 U.110"
Nvidia,stage1,1998-01-31,one_month_total_revenue,13331,USD thousands,P1S03 Selected Financial Data and F-4,1999-01-22,"audited-basis transition month",High,"product 11,420 plus royalty 1,911 = 13,331","Net income 1,347 - the company's first profitable reported PERIOD (a month, not a quarter); tax expense 134 on pre-tax 1,481"
Nvidia,stage1,1997,product_revenue,27280,USD thousands,P1S03 Summary Financial Data,1999-01-22,"CONTEMPORANEOUS and RESTATED alike (revenue did not move)",High,"27,280 + 1,791 royalty = 29,071 total","Closes part 1 P1G09 for 1995-1997: product 1,103 / royalty 79 (1995); product 3,710 / royalty 202 (1996); product 27,280 / royalty 1,791 (1997)"
Nvidia,stage1,1997,royalty_pct_check,6.16,percent of total revenue,P1S03 derived from Summary Financial Data,1999-01-22,DERIVED,High,"1,791 / 29,071 = 6.16%, against the disclosed 6%","Also 312/5,537 = 5.6% for the nine months ended 1997-09-28 and 5,945/92,700 = 6.4% for the nine months ended 1998-10-25"
Nvidia,stage1,1995,rd_expense_reported,2426,USD thousands,P1S03 Summary Financial Data,1999-01-22,"CONTEMPORANEOUS, NET of contract credits",High,"reported 2,426 plus the 2,000 NV2 contract credit = approximately 4,426 of gross development spend","R&D AS PRINTED IS NET of customer contract funding. 1996 reported 1,218 is net of roughly 5,000 of credits (3,000 NV2 plus 2,000 ST). Do not read the 1996 fall as a drop in engineering"
Nvidia,stage1,1997,rd_expense_reported,7103,USD thousands,P1S03 Summary Financial Data,1999-01-22,"RESTATED; March draft printed 6,632",High,not_derived,"+$471K of the 1997 restatement landed in R&D; +410 in SG&A; +18 in cost of revenue; 18+471+410 = 899 = the operating-loss movement. U.101"
Nvidia,stage1,1997,sga_expense,4183,USD thousands,P1S03 Summary Financial Data,1999-01-22,RESTATED,High,not_derived,"March draft printed 3,773"
Nvidia,stage1,1997,deferred_comp_grant,4277,USD thousands,P1S03 Statement of Stockholders Equity,1999-01-22,RESTATED,High,"4,277 less amortization 961 = 3,316, which equals the printed contra-equity balance at 1997-12-31","March draft printed a 2,100 grant, 62 amortization and a (2,038) balance. The grant increase of 2,177 equals the APIC increase of 2,177. U.101"
Nvidia,stage1,1997,deferred_comp_amortization,961,USD thousands,P1S03 Statement of Stockholders Equity,1999-01-22,RESTATED,High,"961 - 62 = 899, exactly the operating-loss movement between drafts","This is the arithmetic identity part 1 could only name as a mechanism candidate"
Nvidia,stage1,1996-12-31,inventory,63,USD thousands,P1S03 four-date balance sheet,1999-01-22,CONTEMPORANEOUS period-end,High,not_derived,"Series: 63 (1996-12-31) / 25 (1997-12-31) / 521 (1998-01-31) / 17,193 (1998-10-25). FIFO at lower of cost or market per Note 1"
Nvidia,stage1,1998-10-25,inventory,17193,USD thousands,P1S03 four-date balance sheet,1999-01-22,"CONTEMPORANEOUS, fiscal period-end",High,"17,193 inventory against 12,461 cash at the same date","The single most informative scaling number in the corpus: 688 times the 1997-12-31 figure in ten months"
Nvidia,stage1,1998-10-25,accounts_payable,46370,USD thousands,P1S03 four-date balance sheet,1999-01-22,"CONTEMPORANEOUS, fiscal period-end",High,"11,572 at 1997-12-31 to 46,370 at 1998-10-25; accounts receivable 12,487 to 35,918 over the same dates","Growth funded on supplier credit. 1997 alone added 11,446 of receivables and 11,295 of payables (March draft cash-flow statement)"
Nvidia,stage1,1998-10-25,line_of_credit_drawn,5000,USD thousands,P1S03 four-date balance sheet,1999-01-22,"CONTEMPORANEOUS, fiscal period-end",High,not_derived,"Carried inside CURRENT LIABILITIES, so the figure is an outstanding borrowing, not an authorisation. Dashes at 1996-12-31, 1997-12-31 and 1998-01-31. The 1998-03-06 S-1 has no such row at all"
Nvidia,stage1,1998-10-25,manufacturing_commitments,48000,USD thousands,P1S03 MD&A Liquidity,1999-01-22,"CONTEMPORANEOUS, period-end",High,not_derived,"In addition to operating and capital lease commitments; against 12,461 of cash. Purchase orders with no minimum-quantity obligation on the manufacturer"
Nvidia,stage1,1998-10-25,customer_concentration_top_three,80,percent of total revenue,P1S03 Business Sales and Marketing,1999-01-22,"CONTEMPORANEOUS as disclosed; basis = fiscal nine months ended 1998-10-25",High,"STB 40 + Diamond 28 + Creative 12 = 80","Compare 94 for calendar 1997 on two names. Different basis, different date, and the widest buyer set the corpus prints"
Nvidia,stage1,1996,diamond_share_of_revenue,82,percent of total revenue,P1S01 MD&A and Note F-13,1998-03-06,"FACT as disclosed, retrospective to 1995-1996",High,not_derived,"Diamond 86% in 1995 and 82% in 1996 - a single-customer company for its first two revenue years, which part 1 did not carry"
Nvidia,stage1,1998-10-25,options_outstanding,7455458,options,P1S03 Note 8 EPS,1999-01-22,"CONTEMPORANEOUS, period-end",High,"7,455,458 / 14,166,710 shares outstanding = 52.6% overhang; weighted-average exercise price $4.46","Diluted share count for the profitable quarter ended 1998-10-25 was 27,774 thousand against 14,165 thousand basic"
Nvidia,stage1,1998-06-30,customer_convertible_notes,11000,USD thousands,P1S03 Note 3 Mandatorily Convertible Notes,1999-01-22,"CONTEMPORANEOUS; issued July and August 1998",High,not_derived,"NON-INTEREST-BEARING, subordinated, issued to THREE MAJOR CUSTOMERS; converts at 90% of the IPO price if a qualifying IPO closes by 1998-12-31, otherwise at $7.00 on 1999-01-15; 11,000/7.00 = 1,571,429 shares, which is the printed conversion"
Nvidia,stage1,1998-10-25,aggregate_liquidation_preference,19827,USD thousands,P1S03 balance sheet preferred caption,1999-01-22,CONTEMPORANEOUS,High,"sum of stated preferences 2,151.5 + 5,103.5 + 5,002.5 + 7,568.2 = 19,825.7, i.e. 1.3 below the printed 19,827 (rounding); the share set includes the 1995 and 1996 Series B warrant exercises of 13,888 and 13,889 and foots to the printed 9,327,087 outstanding","Preference stack exceeds the $19.7 million the MD&A says was raised. U.109 relates to the conversion condition, not this figure"
Nvidia,stage1,1997-08-19,jones_series_d_purchase,127997,USD,P1S03 Certain Transactions,1999-01-22,"CONTEMPORANEOUS, related-party disclosure",High,"127,997 / 24,334 = 5.2599, the Series D round price to the cent","A sitting director buying at the round price under a purchase and investors' rights agreement"
Nvidia,stage1,1998-12-31,post_offering_shares,28595976,shares,P1S03 cover and ownership footnote,1999-01-22,DERIVED reconciliation,High,"23,524,547 as-converted at 1998-12-31 + 1,571,429 note shares + 3,500,000 offered = 28,595,976 exactly","Against the capitalization table's 28,565,226 (basis 1998-10-25): a 30,750-share difference and an unprinted 14,197,460 common count at 1998-12-31. U.108"
Nvidia,stage1,1997-01-26,common_option_price_ladder,0.05,USD per share,P1S03 Director Compensation,1999-01-22,"CONTEMPORANEOUS grants dated 1993-11 and 1994-11",Medium,not_derived,"The private-common ladder as filed: .05 (1993 and 1994) to .36 (1996) to 3.15 (December 1997) to 7.00 (December 1998). Exercise prices are compensation inputs and not transaction prices; a 70-fold nominal rise across the stage while the preferred price rose 3.6x then 3.7x then fell 21 percent"
Nvidia,stage1,1998-10-25,capital_lease_obligations_noncurrent,2032,USD thousands,P1S03 four-date balance sheet,1999-01-22,"CONTEMPORANEOUS, fiscal period-end, non-current portion only",High,"series 617 (1996-12-31) / 1,891 (1997-12-31) / 1,756 (1998-01-31) / 2,032 (1998-10-25); current portions 722 / 1,434 / 1,228 / 1,843","Gross future minimum payments 4,515 at 1998-10-25 less imputed interest 640 at 8-10 percent. 1997 cash flow paid 1,037 under capital leases against 307 (1995) and 502 (1996)"
Nvidia,stage1,1998-07-01,facility_operating_lease_start,July 1998,qualitative,P1S03 Note 4 Lease Obligations,1999-01-22,CONTEMPORANEOUS contract,Medium,not_derived,"A noncancelable operating lease entered in July 1998 running through 2002, with future minimums of 334 / 1,614 / 1,845 / 1,899 / 1,788 by year ending January. The successor state to the 1995 Amdahl sublease (part 1); both kept, each with its own date"
Nvidia,stage1,1998-03-06,intel_i740_announcement,February 1998,qualitative,P1S01 Competition,1998-03-06,CONTEMPORANEOUS report of an external event,High,not_derived,"The i740 paragraph is printed six times in all nine held drafts, so it was never softened as the offering progressed"
Nvidia,stage1,1998-09-21,patent_suits_pending,3,lawsuits,P1S11 and P1S03 Legal Proceedings,1999-01-22,"CONTEMPORANEOUS disclosure",High,not_derived,"SGI notified 1998-04-09 (D Del), S3 notified 1998-05-11 (N D Cal, three patents), 3Dfx notified 1998-09-21 (N D Cal, RIVA TNT); answers and invalidity counter-claims in each. Court filing dates UNKNOWN. U.113"
```

>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
Nvidia,stage1,1998-04-24,"First amendment after the S-1 adds the SGI patent infringement suit to the record","the Company; Silicon Graphics Inc. as plaintiff",UNKNOWN,P1S08,FACT-about-the-printing; the suit itself is a pleaded matter,High,U.113,"SGI token count moves 4 to 44 between the March and April drafts - the amendment cycle is the clock for this event"
Nvidia,stage1,1998-05-11,"Company notified that S3 had filed a second patent infringement suit, alleging three patents","the Company; S3 Incorporated",San Francisco / Northern District of California,P1S11,FACT as disclosed,High,U.113,"Enters the record only with the 1998-11-20 amendment, six months after notification - a disclosure lag, not an event date"
Nvidia,stage1,1998-09-21,"Company notified that 3Dfx had filed a third patent suit, directed at the RIVA TNT product","the Company; 3Dfx Interactive, Inc.",Northern District of California,P1S11,FACT as disclosed,High,U.113,"3Dfx token count moves 4 to 40 in the same amendment. The company answered and counter-claimed that the patents are invalid and uninfringed, relying on an opinion from named outside patent counsel"
Nvidia,stage1,1998-07,"Three major customers lend the company 11.0 million dollars on non-interest-bearing subordinated convertible notes","the Company; three unnamed major customers",UNKNOWN,P1S03,"CONTEMPORANEOUS disclosure of an instrument; holders unnamed",High,U.109,"The channel financed the balance sheet. Second tranche in August 1998. No note instrument or counterparty schedule is filed"
Nvidia,stage1,1998-07,"Company enters a noncancelable operating lease for its facilities running through 2002","the Company; landlord unnamed",Santa Clara / 3535 Monroe Street,P1S03,CONTEMPORANEOUS contract summary,Medium,None,"The successor to the Amdahl sublease of 1995; the registrant's address of record had already moved from Sunnyvale to Santa Clara by this draft"
Nvidia,stage1,1998-11-20,"Amendment discloses that TSMC is now the primary manufacturer and that assembly and test run through Amkor and Siliconware","the Company; TSMC; Amkor Technology Inc.; Siliconware Precision Industries Co. Ltd.",Hsinchu / Korea and the Philippines,P1S11,"FACT about the printing; the switch itself is registrant-narrated",High,U.106,"Also the draft in which the company states that leaving ST's manufacturing ends ST's patent umbrella and will increase infringement risk"
Nvidia,stage1,1998-12-23,"Amendment discloses 3Dfx's pending acquisition of STB, the company's largest customer, and forecasts a significant reduction in sales to it","the Company; 3Dfx; STB Systems, Inc.",UNKNOWN,P1S03,"FACT as disclosed; forward-looking against interest",High,U.111,"The first held draft containing the phrase sales to STB will be reduced significantly (3 hits, 0 in every earlier file)"
Nvidia,stage1,1998-12-23,"Competitor list revised: VideoLogic, Evans and Intergraph and SGI added to the professional tier; Chromatic dropped because ATI acquired it; Micron (an OEM customer) is recorded as having acquired Rendition","the Company; ATI; Chromatic Research; Micron; Rendition",UNKNOWN,P1S03,FACT about the printing; reported consolidations,Medium,None,"Consolidation is the registrant's own word for the state of the field: highly fragmented and undergoing a period of consolidation"
Nvidia,stage1,1998-10-25,"Nine-month customer mix reported as STB 40 percent, Diamond 28 percent, Creative 12 percent","the Company; STB; Diamond; Creative",UNKNOWN,P1S03,FACT as disclosed,High,U.107,"Fiscal basis (38 weeks). Creative also lent into the July-August notes if the three noteholders are AIB houses - an inference the corpus does not support"
Nvidia,stage1,1998-10-25,"Manufacturing commitments of 48.0 million dollars disclosed alongside a 5.0 million dollar drawn line of credit and 4.5 million of gross lease payments","the Company; TSMC; lenders unnamed",UNKNOWN,P1S03,FACT as disclosed,High,None,"The commitment figure is the scale of purchase orders a fabless company carries into an offering; cash at the same date was 12,461"
Nvidia,stage1,1998-03-23,"Form 8-A12B filed - registration of a class of security on a national exchange, thirteen days after the S-1","the Company; Nasdaq",UNKNOWN,P1S15,FACT-about-the-index only,Medium,U.118,"Indexed with a blank primaryDocument and NOT stored; an 8-A before effectiveness is a sequence question worth a fetch, not a null"
Nvidia,stage1,1998-05-07,"Two Form RW registration withdrawals filed in the same month as an amendment","the Company; unnamed registrant of the withdrawn statement",UNKNOWN,P1S15,FACT-about-the-index only,Low,U.118,"Part 1 named this UNTRIED item 10; still unfetched. A withdrawal inside a live registration is an event"
Nvidia,stage1,1999-01-22,"Form S-1MEF filed the same day as the 424B4","the Company",UNKNOWN,P1S15,FACT-about-the-index only,Medium,U.118,"A merger of registrations filed with the final prospectus; the only held index row for it has a blank primary document"
Nvidia,stage1,1999-08-06,"Schedule 13G filed by Creative Technology Ltd and CTI Limited reporting 2,192,785 shares, about 7.5 percent","Creative Technology Ltd; CTI Limited; NVIDIA Corporation",UNKNOWN,P1S14,"(PB) - independent-origin document, post-boundary",High,None,"Used in the §T ledger and for no Stage-1 claim. It is the only counterparty-authored description of this registrant anywhere in the corpus"
Nvidia,stage1,1997-01-31,"One month ended January 26, 1997: revenue 190, net loss (522) - the smallest reported revenue period in the corpus","the Company",UNKNOWN,P1S03,"CONTEMPORANEOUS unaudited column",High,U.102,"Restates part 1's P1K05 finding: the period is a printed column with values, not an orphan footnote string with none"
Nvidia,stage1,1998-01-31,"One month ended January 31, 1998: revenue 13,331, net income 1,347 - the first profitable reported period","the Company",UNKNOWN,P1S03,"audited-basis transition month",High,U.105,"Ends the calendar-January year-end step; the 52/53-week convention begins February 1, 1998 (P1K13)"
```

>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date,decision,state_before,information_available,unknowns,alternatives,constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref
Nvidia,stage1,1995-12-31,"Take development funding from a third party for the NV2 instead of financing it internally","NV1 shipping and failing; NV2 in development; operating cash use of 6.1 million in 1995","the company's own ability to book 2.0 million of credits in 1995 and 3.0 million in 1996 as reductions to research and development","who the third party was; what it received; what the milestone terms were; how much of the 2,500 advance on the balance sheet it represents",NONE PRINTED,"a 1994 Series B round at 1.80 and a 1995 Series C at 6.67 - both equity, both dilutive","not printed; the funding is what the company named as the reason 1996 burn fell to 300,000","a funded second-generation product","the second product was cancelled in 1996; a 2,500 advance still sat in accrued liabilities at 1996-12-31 and 1997-12-31",P1S01 and P1S03,Medium,"P1-31 P1-49"
Nvidia,stage1,1998-11-20,"Move primary fabrication from ST Microelectronics to TSMC and split assembly and test to Amkor and Siliconware","ST fabricated, assembled, tested, licensed and resold the product; December 1997 low yields at ST; TSMC already engaged on a purchase-order basis","the yield failure at ST; that no alternative source was readily available for a specific product; that establishing a new relationship could take several months","when it was decided; whether ST capacity or ST's competing position drove it; what the qualification cost",the licence to ST was KEPT while the manufacturing moved - the only alternative visible in the text,"TSMC has no obligation to provide any specified minimum quantities; the company's wafer requirements are a small portion of TSMC capacity","not printed","manufacturing capacity independent of a licensee-reseller","1998 volume-production difficulties on the RIVA128ZX and RIVA TNT and a negative gross-profit quarter; the company itself states that infringement risk will increase because ST's licences no longer cover TSMC-built parts",P1S11 and P1S03,Medium,"P1-39 P1-40 P1-59"
Nvidia,stage1,1998-08,"Borrow 11.0 million dollars from three customers on non-interest-bearing subordinated notes convertible at 90 percent of the offering price","revenue up roughly sixteenfold year on year; one profitable quarter behind and one loss quarter ahead; 6.5 million of cash and no bank indebtedness at 1997-12-31","its own reported working-capital position: receivables plus 11,446 and payables plus 11,295 in 1997; inventory rising toward 17,193 by October 1998","which three customers; what the paper cost in margin or priority; whether equity was sought first","a bank line - and one appears drawn for 5,000 at 1998-10-25, so both routes were used rather than chosen between","subordinated to certain senior indebtedness; automatic conversion at 7.00 on January 15, 1999 if no qualifying IPO closed by 1998-12-31",not printed,"capital to fund the next product generation and the inventory it required","converted on 1999-01-15 into 1,571,429 common shares, as printed in the same lineage",P1S03,Medium,"P1-30"
Nvidia,stage1,1999-01-22,"Give up contract funding as a financing method","5.0 million of NV2 credits and 4.3 million of ST credits had reduced reported research and development across 1995-1997; the ST support obligation expired with calendar 1998","the royalty at 6 percent was expected to fall; the company stated it did not expect contract funding in the future","why the company closed the channel that had cheapened its largest expense line",NONE PRINTED,"the company's own statement is an intention, not a rationale","not printed","research funding reported gross of customer money","not used - post-boundary outcome, excluded",P1S03,Low,"P1-38"
```

>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes
Nvidia,stage1,1995-12-31,"One add-in board manufacturer took 86 percent of the company's first revenue year",86 percent of total revenue,"that a named buyer existed for the NV1 at scale relative to the company","that the buyer wanted the product for its own market: the same year printed a negative gross margin and the product was withdrawn in Q1 1996",P1S01,"CONTEMPORANEOUS disclosure, retrospective content",High,"Diamond Multimedia Systems, Inc. The corpus's earliest named customer fact, and the narrowing of the first-customer gap"
Nvidia,stage1,1996-12-31,"Contract credits of 3.0 million dollars reduced reported research and development","3,000 USD thousands","that a third party paid real money for the NV2 programme - the strongest in-window evidence that the console-era work had a sponsor","who paid, or that the sponsor was enthusiastic: the product was cancelled in the same year",P1S01 and P1S03,CONTEMPORANEOUS disclosure,High,"Named counterparty UNKNOWN; do not attribute to Sega, which appears in the record only as an equity party"
Nvidia,stage1,1997-12-31,"First profitable period: the quarter ended December 31, 1997 earned 1,424 thousand dollars","1,424 USD thousands","that unit economics could turn positive at existing scale","durability: the following two fiscal quarters lost 1,021 and 9,652, and the full calendar year printed a net loss of 3,589",P1S03,"CONTEMPORANEOUS, unaudited quarterly data, RESTATED annual basis",High,"The March 1998 draft printed 2,163 for this same quarter. P1K08"
Nvidia,stage1,1998-01-31,"The one-month transition period earned 1,347 thousand dollars on 13,331 of revenue","1,347 USD thousands","that the turn was not confined to one quarter: a January month on the old calendar basis was profitable","that January is representative; a one-month period is 3 percent of a year",P1S03,"audited-basis transition month",High,"Part 1 could not name a dollar figure for the first profitable period; two now exist"
Nvidia,stage1,1998-08,"Three customers advanced 11.0 million dollars as interest-free convertible notes","11,000 USD thousands","that identifiable buyers were willing to place unsecured, non-interest-bearing capital in the company","that this was a demand signal rather than a supply-security or pricing device - mechanism UNKNOWN; and it demonstrably reduces the independence of the sales relationship",P1S03,CONTEMPORANEOUS disclosure,High,"The most striking channel fact in the corpus and the one part 1 did not carry. Holders unnamed"
Nvidia,stage1,1998-10-25,"Buyer set widened from two customers at 94 percent to three at 80 percent","80 percent across three named AIB houses","that the channel was diversifying in numbers","that it was diversifying in power: the three largest buyers were also the three lenders and held all accounts receivable",P1S03,FACT as disclosed,Medium,"Basis is the fiscal nine months ended 1998-10-25, not a calendar year"
```

>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes
Nvidia,stage1,1996-03-31,"The founding product was withdrawn and the second cancelled inside the stage","revenue of 3,912 thousand in 1996 came from a product already stopped in Q1","that the architecture bet failed on the company's own account","that the failure was useful: the filing's own causal sentence places API adoption after the withdrawal (part 1 P1K03)",P1S01 and P1S03,CONTEMPORANEOUS,High,"Extended here: all 1995 and 1996 revenue was sale AND licence of that same product"
Nvidia,stage1,1998-04-09,"First of three competitor patent suits notified","one patent, treble damages and an injunction sought","that the market the company entered in 1997 was policed by litigation","merit or outcome: UNKNOWN; the company's belief in its defences rests on a retained counsel's opinion",P1S08,"CONTEMPORANEOUS disclosure of pleaded matters",High,"Notification date, not filing date (U.113)"
Nvidia,stage1,1998-09-21,"Third patent suit directed specifically at the newest product, RIVA TNT","one patent against the flagship","that the re-architected product line drew infringement claims of its own","that infringement occurred. This is the failure class the pivot narrative omits, and it is filed by the company itself",P1S11,CONTEMPORANEOUS disclosure,High,"Answers and invalidity counter-claims filed in each suit"
Nvidia,stage1,1998-07-26,"Negative gross margin quarter at the new fabricator: cost of revenue 12,961 on revenue 12,134","gross loss 827 and net loss 9,652 thousand","that the manufacturing switch carried a quantified cost within the stage","root cause: the company attributes it to yield problems and inability to supply in a timely way, and no further. TSMC, the design or the schedule is not distinguished",P1S03,"CONTEMPORANEOUS, unaudited quarterly data, self-disclosed cause",High,"The largest single-period loss in the corpus. The same quarter is dated July 28 in a risk factor (U.104)"
Nvidia,stage1,1998-10-25,"Receivable allowance rose to 3,506 thousand while three customers held all accounts receivable","35 times the stated earlier allowance","that concentration had begun to be priced into the accounts","that any amount was written off; the company reported no bad debt write-offs through 1997",P1S03,"FACT as printed, with a three-date allowance caption against four columns",Medium,"The allowance caption does not map cleanly to the balance sheet columns; recorded as a basis caveat"
Nvidia,stage1,1998-12-23,"The largest customer is being acquired by a patent plaintiff, and the company says so","63 percent of 1997 revenue; 40 percent in the last nine months","that the registrant disclosed a channel loss before it happened rather than after","that it could be avoided: no mitigation is printed beyond finding other buyers",P1S03,"CONTEMPORANEOUS disclosure against interest",High,"Completion and date of the acquisition are UNKNOWN from held bytes (U.111)"
```

>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,channel,date_tested,why_tested,cost_or_effort,result,repeatability,source_id,confidence,notes
Nvidia,stage1,"direct sales to add-in board manufacturers",1995,"the only route to PC sockets without a sales organisation of its own","UNKNOWN - selling effort is not separated in any held draft","86 percent of 1995 revenue through Diamond; 94 percent through two houses in 1997; 80 percent through three in the nine months ended 1998-10-25","UNKNOWN within the window; purchase orders rather than agreements mean it is re-won every quarter",P1S01 and P1S03,Medium,"The channel is also the lender and the creditor: three of these buyers wrote 11.0 million of notes and all three held the receivables"
Nvidia,stage1,"technology licence to the manufacturer as a distribution route",1996,"to convert fabrication capacity into resale reach at the same time","royalty-based; the rate is not printed","ST's sales of the RIVA parts produced 6 percent of total revenue in 1997 and in each of the two nine-month periods; ST held a worldwide licence to the architecture and source code","single counterparty, and the company expected the royalty to fall in the quarter ending 1999-01-31",P1S03,High,"The most distinctive channel arrangement in the corpus. The instrument itself was never filed (U.117)"
Nvidia,stage1,"distributors",never tested within the stage,"the company had a written policy for the channel it had not yet used","UNKNOWN - a deferral policy implies sell-in risk borne by the company until resale","Nothing: 'While the Company has not yet sold products through distributors' is printed in every held draft including the final prospectus","UNKNOWN; the policy exists, the channel does not",P1S01 and P1S03,High,"A contemporaneous negative of real weight, and the single clearest statement of where the channel stood at the boundary"
Nvidia,stage1,"OEM design wins as the demand mechanism behind the AIB sale",1997,"because add-in board sales follow OEM choices","UNKNOWN - application-engineering support is described but not costed","products used by five of the top ten US PC OEMs (March 1998) then six plus Intel as a motherboard maker (January 1999); design cycles twice a year, spring and fall","UNKNOWN; the company stated the next product must be designed in to produce significant revenue at all",P1S01 and P1S03,Medium,"five-to-six is version evidence about a marketing sentence, not a new sale. The spring/fall cycle sentence is new to this volume"
Nvidia,stage1,"product demonstrations, trade press, analyst relations, tradeshows, advertising and the corporate web site",1998,"to build brand recognition in a market where the buyer is an engineer and a retailer at once","significant resources devoted, amount not broken out","the award counts the company prints for itself: over 40 (March 1998) to over 180 (January 1999)","UNKNOWN",P1S03,Low,"Company marketing statements throughout. The 4.5x escalation in ten months is the finding; either count is unverifiable from this corpus (part 1 P1K06)"
Nvidia,stage1,"customer-funded development contracts as a financing channel",1995,"to fund a generation without diluting","credits of 2.0 million (1995) and 3.0 million (1996) for the NV2; 2.0 million (1996) and 2.3 million (1997) from ST","worked twice, then closed by the company itself: it 'does not currently have any plans to enter into contractual development arrangements'","explicitly ended as at the boundary",P1S01 and P1S03,High,"The only in-window case where the record shows the company giving up a channel rather than losing it"
```

>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
Nvidia,stage1,P1K08,"U.101; §J.3; §M.1; narrows part 1 P1K01","Calendar-1997 net loss (2,691), quarters (1,176) (1,265) (2,413) 2,163, deferred-comp grant 2,100 and amortization 62, APIC 22,902, deficit (13,991), equity 6,896","P1S01 statements and equity ledger",1998-03-06,"Calendar-1997 net loss (3,589), quarters (1,176) (1,265) (2,572) 1,424, grant 4,277 and amortization 961, APIC 25,079, deficit (14,889), equity 6,897","P1S11 and P1S03",1999-01-22,"An additional 2,177 of 1997 stock-option deferred compensation was recognised and 899 of it amortised into 1997 - allocated 18 to cost of revenue, 471 to R&D and 410 to SG&A, which sums exactly to the operating-loss movement. Both printings foot internally, so this is a restatement and not a transcription slip","The later printing is the one declared effective and sold, and its quarterly table foots to its annual column; side B outranks side A and the movement is now localised to two quarters","Carry (3,589) as canonical; keep the March figures as SUPERSEDED-DRAFT rows; the mechanism is deferred-compensation amortisation, DERIVED, and FASB Interpretation No. 28 allocation is the printed policy that explains the three-line split","Why the grants were re-measured, and whether this was an audit adjustment or a policy judgment, is UNKNOWN; the 1K total-equity drift is rounding",High
Nvidia,stage1,P1K09,"U.107; §G.2; §S.2","Sales to STB and Diamond accounted for 63 and 31 percent of the Company's TOTAL revenue in 1997","P1S01 MD&A l.961 and l.2823; P1S03 l.3310",1998-03-06,"Product revenue from STB and Diamond accounted for 63 and 31 percent of the Company's 1997 revenue","P1S03 Note F-13 l.5202",1999-01-22,"Same percentages, two stated denominators: total revenue 29,071 versus product revenue 27,280. Both sentences are in the final prospectus, one in MD&A and one in the audited note","Neither outranks the other; they are one lineage","Quote the registrant's words with its own base and never convert the percentage to dollars without naming which denominator","Up to 4.5 points, roughly 1.1 million dollars of 1997 revenue, is unallocated between the readings",High
Nvidia,stage1,P1K10,"U.102 and U.103; §M.2; §S.1; refines part 1 P1K05","The unaudited data are as of January 26, 1997 and September 28, 1997, and the statements print a column one month ended January 26, 1997","P1S03 notes header l.5522 and l.5589, F-pages index l.5133, summary table l.1941",1999-01-22,"The EPS reconciliation table prints One month ended January 28, 1997 and One month ended January 26, 1998, while the statements print January 31, 1998","P1S03 Note 8 l.5660-5700",1999-01-22,"Four captions for two periods, with identical values: net loss (522) and net income 1,347 appear under both variants. Separately, the quarterly table labels 1997 quarters with Sunday dates while the sentence above it calls them March 31, June 30, September 30 and December 31","The structured presentations (statements, summary table) and the FY1999 10-K405's matching January 31, 1998 label outrank a note table's captions","Two January months exist, one in each year; the transition month is the one month ended January 31, 1998 with net income 1,347; the 26/28 captions are calendar-convention variants of the same two periods","Which convention each caption intended is UNKNOWN. Part 1's premise that no column existed for January 26, 1997 is refuted by the header row at l.1941, and the merge must not carry it forward",High
Nvidia,stage1,P1K11,"U.106; §I.1; §P","Substantially all of the Company's products currently are manufactured by ST in Crolles, France, with TSMC recently established as a second source","P1S01 Business and Risk Factors",1998-03-06,"The Company in the past utilized ST and currently utilizes TSMC; TSMC is the Company's primary manufacturer; ST assembled and tested substantially all products in the past","P1S11 first, then P1S03",1998-11-20,"Eight months of operating history plus a yield failure, recorded as a change in the present tense across drafts. The token primary manufacturer appears 0 times in the four March-July files and 1 time in each of the five later files","Both are true at their own dates; the later is nearer the boundary and is accompanied by the company's own statement that the move ends ST's patent licences and increases infringement risk","A foundry migration completed between the July and November 1998 amendments, with the assembly/test step split to Amkor and Siliconware at the same moment","The decision date, the qualification path, the cost and whether ST's exit was chosen by either party are UNKNOWN. The ST Agreement itself was never filed (U.117)",High
Nvidia,stage1,P1K12,"U.104; §I.2; §S.1","Yield problems resulted in lower than expected revenues and higher manufacturing costs during the quarter ended July 28, 1998","P1S03 Risk Factors l.515-520",1999-01-22,"Lower yields resulted in higher expenses and lower revenues in the quarter ended July 26, 1998, and the quarterly table column is headed July 26, 1998","P1S03 Business l.3399 and quarterly table l.2471",1999-01-22,"Two end-dates for one fiscal quarter inside one document; April 26 and October 25 1998 are Sunday endings consistent with the stated last-Sunday convention and July 28 is not","The table column and the Business section, which agree, outrank an incidental risk-factor sentence - RD-127's rule that a date comes from the structured record","The fiscal quarter ended July 26, 1998; July 28 is a stale or mistaken date that survived in one paragraph","Whether internal reports used another period end is UNKNOWN",Medium
Nvidia,stage1,P1K13,"U.105; §S.1","Effective January 31, 1998, the Company changed its fiscal year-end financial reporting period to a 52- or 53-week year ending on the last Sunday in January","P1S03 MD&A and quarterly preamble l.2446",1999-01-22,"Effective January 1, 1998 the Company changed its fiscal year-end reporting period to January 31; in addition, effective February 1, 1998 it changed from January 31 to a 52- or 53-week year","P1S03 Note 1 l.5544-5551",1999-01-22,"Note 1 describes a two-step change with two dates; the MD&A compresses both steps into one sentence dated at the end of the transition month","The note is the financial-statement disclosure and is coherent with the existence of a calendar one-month transition period, which the Sunday convention alone would not produce","A two-step change: calendar-January year-end effective January 1, 1998 (hence the audited one month ended January 31, 1998), then the 52/53-week convention from February 1, 1998","No held figure depends on which date is quoted; the hazard is entirely in quotation",Medium
Nvidia,stage1,P1K14,"U.109; §J.5","Automatic conversion of all preferred occurs on an IPO in which aggregate proceeds exceed 15,000,000 and the offering price equals or exceeds 10.00 per share","P1S03 Note 3 l.5870-5878",1999-01-22,"Pro forma common of 25,065,226 shares is presented as though all 9,327,087 preferred shares had converted, on a capitalization whose December 1998 footnote assumes 8.00 per share","P1S03 Capitalization l.1811-1817; P1S02 footnote (part 1)",1998-12-23,"A condition stated in instrument terms and a presentation assuming the outcome, in the same document. The notes' own conversion test is different and lower - gross proceeds of at least 10.0 million - so two instruments in one note carry two thresholds","Both are printed in the operative document; the reconciling consent, waiver or charter amendment is absent from the corpus","The preferred converted by consent or by amended terms rather than by satisfaction of the price condition - labelled INFERENCE because nothing printed says so","The mechanism, its date, and whether the blank-dated Ex-3.1 amended charter was the instrument are UNKNOWN",Medium
Nvidia,stage1,P1K15,"U.108; §M.4","Upon closing the Company will have outstanding an aggregate of 28,595,976 shares of Common Stock","P1S03 cover l.238, l.1705, ownership footnote l.4598",1999-01-22,"Pro forma as adjusted total capitalization shares are 25,065,226 plus the 3,500,000 offered, i.e. 28,565,226","P1S03 Capitalization l.1811-1817",1999-01-22,"Two measurement dates: 1998-10-25 in the capitalization table and December 31, 1998 in the ownership footnote, whose 23,524,547 as-converted figure plus 1,571,429 plus 3,500,000 equals 28,595,976 exactly","The arithmetic identity resolves it: both numbers are right at their own dates, the same mis-citation trap as part 1 P1K04 headcount","Use 28,595,976 with its date or not at all; the identity also implies an unprinted 14,197,460 common shares outstanding at December 31, 1998","Which instruments issued the 30,750 intervening shares is UNKNOWN; the only printed 1998 issuance row is 25,000 shares for 25 thousand dollars",High
Nvidia,stage1,P1K16,"U.110; §Boundary 4 of part 1; §M.2","The summary table carries seven columns and the one month ended January 26, 1997 corresponds to no column; the period is recorded as UNKNOWN and used for nothing","research part 1 §Boundary 4 and P1K05",1998-03-06,"The summary table header prints nine columns including One Month Ended January 26, 1997 and One Month Ended January 31, 1998, both with values","P1S03 l.1941-1985",1999-01-22,"A column count taken by reading part of a wrapped table rather than listing its header cells - RD-124 and RD-127's assumed-column failure mode, arriving here in an inherited premise","The bytes. The table's own caption row is decisive","Part 1's handling was conservative and its conclusion (use nothing) was safe, but its stated reason was wrong and the period is now quantified: revenue 190, net loss (522)","None for the figures. The register and any later volume must not carry the no-column statement forward",High
```

>>> REGISTER ROWS FOR MERGE <<<

```csv
company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task
Nvidia,stage1,"U.116 identity of the first customer and the first booked order","revenue is printed only as annual, monthly and quarterly totals; no order, invoice, licence or press item is held; the strings first customer, initial customer, first order, first purchase, first shipment and customer since return zero hits across all held drafts",High,"Diamond at 86 percent of 1995 total revenue, and the sentence that all 1995 and 1996 revenue came from the sale and licence of the NV1",Low,"UNTRIED-3 and UNTRIED-4 periodicals and trade press for a 1995 NV1 purchaser naming; the §10 research-debt trigger first customer is unknown remains OPEN"
Nvidia,stage1,"U.115 any carrier for the near-death or cash-runway recollection","zero hits across the lineage for the rescue phrasings; no interview, memoir or trade body of 1995-1999 is on disk",High,"the filed distress set only: zero revenue 1993-94, negative 1995 gross margin, 6,470 operating loss in 1995, a down-priced 1997 round, 6.5 million cash and no bank debt at 1997-12-31, controls very limited",Medium,"UNTRIED-1 to UNTRIED-4. Anything fetched must be classified FOUNDER CLAIM / retrospective memory and dated to the interview, never to 1995"
Nvidia,stage1,"U.112 the counterparty behind the NV2 development contract and the 2,500 advance on development agreement","the P and L credits and the balance-sheet line are held; the contract is not an exhibit and no sentence names the payer or links the two figures",High,"credits of 2,000 (1995) and 3,000 (1996) to research and development for a contracted NV2, plus a 2,500 advance still in accrued liabilities at 1996 and 1997",Medium,"re-read the exhibit tables of every held amendment for a named development agreement; UNTRIED-5 Wayback for a 1995-96 console-partner announcement"
Nvidia,stage1,"U.117 the text of the Amended and Restated Strategic Collaboration Agreement with ST","Exhibit 10.10 is dated March blank 1998 in the index and asterisked to be filed by amendment, and no held amendment files it; ditto Exhibit 1.1 the underwriting agreement",High,"the registrant's own summary: ST may manufacture the RIVA128ZX and resell the RIVA128 and RIVA128ZX for a royalty, holds a worldwide licence to the architecture and source code, and had a right to engineering support through December 31, 1998",Medium,"check the post-effectiveness exhibit list in the FY1999 10-K405 and the FY2000 10-K on disk (both (PB)) for the filed agreement; do not treat the summary as the terms"
Nvidia,stage1,"U.113 the court-filed dates of the SGI, S3 and 3Dfx suits and their outcomes","only the company's notification dates are printed; no docket, opinion or settlement document is in the corpus",Medium,"notification dates April 9, May 11 and September 21, 1998, with answers and invalidity counter-claims in each",High,"UNTRIED-6 federal court records (PACER) for the three district-court cases, and UNTRIED-7 press coverage of any settlement or cross-licence"
Nvidia,stage1,U.114 reconciliation of the one-business-segment United States statement with the actual geography,"the accounting note is a segment statement and the geography is operational; no held text connects them",Low,"one business segment in the United States (Note 1) against TSMC in Taiwan, Amkor in Korea and the Philippines, ST in France, JAFCO and Itochu notices at a Tokyo address",Medium,"test whether any held draft gives revenue by geography; this pass found none, and no such table was located"
Nvidia,stage1,"U.118 what the 1998-05-07 RW pair, the 1998-03-23 8-A12B, the 1998-04-03 and 1999-01-12 8-A12G filings and the 1999-01-22 S-1MEF were were","indexed in the submissions table with a blank primaryDocument and never fetched",Medium,"the six index rows themselves, with accession numbers recorded in the sources register",Low,"UNTRIED-8: run tools/sec_intake.py auto against CIK 1045810 for these six accessions and read them; a withdrawal inside a live registration is an event"
Nvidia,stage1,"the identities and terms of the three customer noteholders","the note gives a count, a total, dates and terms but no schedule",High,"11,000 of non-interest-bearing subordinated convertible notes issued to three major customers in July and August 1998",High,"UNTRIED-9 the FY1999 10-K405 related-party and customer disclosures ((PB), so usable only for stage-2 handoff); no held in-window document names them"
Nvidia,stage1,"the 1993-1994 period in any contemporaneous carrier","EDGAR holds nothing for this registrant before 1998-03-06 and the two archive families are empty or untried",High,"the audited 1993 stub and the 1994 column, both recited in 1998",Medium,"UNTRIED-2 (Wayback, empty directory), UNTRIED-3/4 (periodicals), UNTRIED-10 (Google Books at the right host for the three volume ids the harvest dossier mis-hosted)"
Nvidia,stage1,"an XBRL or machine-readable early financial series","tools/sec_intake.py facts prints a path and writes no file (RD-112 defect 1, unfixed); sources/financials/ is empty",Medium,"the hand-transcribed tables this pass read, now cited by line number in every claim record",High,"re-run facts after the script defect is fixed; until then every figure here is a hand read and the merge should spot-check the quarterly table against the same lines"
```

**Row count requested: 101** — sources 9 · quantitative 35 · timeline 16 · decisions 4 ·
**validation 6 + failures 6** (identical column sets; emitted as two blocks, which
`merge_census.match_register()` will report as `AMBIGUOUS:validation.csv,failures.csv` — a tool limitation
recorded in the report, not a drift to repair by inventing a header) · channels 6 · conflicts 9 ·
data_gaps 10. Every `stage` cell is the literal `stage1`; every row was written from a line opened in this
session; every block was re-parsed through a CSV reader after writing (0 column drift, 0 empty cells). All
`P1x` ids are dossier-local and no row assumes a global `source_id` (RD-123).

## Untried

**Continuing part 1's series.** Part 1's header promised an `## Untried` block of eleven routes; the file on
disk ends after the register row-count note with a stray `#` line and **contains no `## Untried` section at
all**, although its prose cites items 1, 3, 4, 5, 6, 7 and 10 of it (this is reported as a part-1 defect, not
silently repaired here — part 1 is not edited). The routes below are therefore numbered fresh for this volume,
with the part-1 item numbers kept in parentheses where the same route is re-named.

1. **UNTRIED — Founder and press interviews of 1994–1999 (part 1 items 3–4).** The near-death and pivot
   recollections (§D.4 part 1, U.115) have no carrier here. Whatever is fetched is FOUNDER CLAIM / retrospective
   memory, dated to the interview. Web budget for this pass: 0 calls; nothing attempted.
2. **UNTRIED — Wayback Machine for 1996–1999 nvidia.com** (part 1 item 5; the current state is UNANSWERED,
   `sources/wayback/` is an empty directory with no negative artifact). Highest-value single route for the
   channel, first-customer and NV1 datasheet questions.
3. **UNTRIED — Trade periodicals for 1995–1998 naming this registrant** (part 1 item 6). Requires the correct
   harvester path; the one entity-bearing item on disk has FY2005–FY2026 text layers.
4. **UNTRIED — Chronicling America for local newspaper naming, 1995–1999.** **This is a 404-on-our-path defect,
   not a refusal** (RD-128/RD-129): `periodical_harvest.py` builds
   `www.loc.gov/chroniclingamerica/search/pages/results/?format=json`, which does not exist; from this machine
   the candidate shapes return 403 behind Cloudflare, so a wrong path and a blocked client are
   indistinguishable locally and only the CI probe can answer it. Do not write "LOC refuses us".
5. **UNTRIED — Google Books at the correct host.** `research/A4_harvest_mine.md` records three volume ids
   (`U9n74ngfDU8C`, `z3zsxvtRSv4C`, `vcdVAAAAMAAJ`) as UNANSWERED at 0 bytes; they are Google Books ids fetched
   from the wrong host, so the route has never been tried as such.
6. **UNTRIED — Documentary and registry family (e)** (part 1 item 7): California Secretary of State and Santa
   Clara County records for the 1993 California incorporation, and PACER for the three district-court patent
   cases (U.113).
7. **UNTRIED — The six blank-primaryDocument in-window accessions** (part 1 item 10, and U.118): 8-A12B
   1998-03-23, 8-A12G 1998-04-03, two RW 1998-05-07, 8-A12G 1999-01-12, S-1MEF 1999-01-22. Command when
   authorised: `python tools/sec_intake.py auto 1045810 --company-dir
   founders_playbook/01_companies/company_016_nvidia`. Script work, not agent work (§15.1).
8. **UNTRIED — The held-but-unread documents of this corpus.** 31 stored documents; this pass opened the seven
   lineage drafts, the 424B4, the FY1999 10-K405 (grep-level plus the Sega/console counts), the SC 13G of
   1999-08-06, the manifest and the index. **Not opened: the 1999-05-17 DEF 14A (94,006 B), the FY2000 10-K405,
   the 2000 S-3 and 424B2, the 2000-09-28 and 2001 8-Ks, the 2000-10-10 and 2001-04-30 SC 13Gs.** All are
   `(PB)` for Stage 1, and three of them (the FY1999 proxy, the FY2000 10-K, the 2000 S-3) are the cheapest
   carriers for the STB loss, the litigation outcomes and the filed ST Agreement.
9. **UNTRIED — Customer- and supplier-side primary documents.** Nothing in any family has been reached from
   ST/TSMC/Amkor/Siliconware/STB/Diamond/Creative sides; the one counterparty-authored holding is the `(PB)`
   1999 SC 13G (§T).
10. **UNTRIED — The 424B4's remaining unmined sections** (not a fetch, a read): the legal and executive-
     compensation tables, the principal-stockholder grid with its after-offering column (part 1 left it
     unread), the trademark and patent schedule, and the description of capital stock. This pass read the
     business, risk-factor, MD&A, financial-statement, Certain Transactions and Underwriters sections and
     stopped there by choice, and the choice is recorded rather than hidden.
11. **UNTRIED — An independent 1997–1998 count of the 3D add-in board market** from any source that did not
     use the filing (Mercury Research is *named* in the registrant's industry background but its report is not
     held), which is the only route that would let §H carry a third-party denominator.
