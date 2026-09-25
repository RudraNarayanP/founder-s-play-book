# amazon_s3_audit1_chronology.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:05:43Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

**PASS-WITH-DEFECTS.** High-severity defects: **1** (CH-01). Medium: **5**. Low: **2**.

Scope: the chronology layer of Amazon Stage 3 only — sequence and duration, boundary honesty, dated-but-not-dated
citation content, single-lineage inflation, version differences. Mechanical gates were run once for context
(`gates.py --checks csv,keys,anchors`: 15 findings, 17 passes; column drift, unresolvable retired-form `S300x`
tokens, and the §U.201–U.220 anchor/register parity gap) and are **not** counted in this verdict.

What this pass certifies: **Stage 3's boundary argument is sound as written, and its centre of gravity is
correct.** The opening date 1997-05-16 is defended from a document on disk; the closing date is presented as a
live contest rather than settled by file geometry; and the load-bearing falsification of Position A's first-use
test was checked line-by-line against the three earlier accessions and holds verbatim (see *Checks that passed*
§1). Nothing in this layer was found to be averaged, and no version difference I sampled was smoothed into a
range.

What this pass will not certify: **the retraction of the first-use test has not reached the register layer.**
`timeline.csv` still carries the withdrawn claim as a live High-confidence row while two other rows in the same
file record its falsification (CH-01). By method §14 rule 10 that is the highest-severity place a stale claim can
live, because the register is what a later agent filters on. Second, the recommended boundary's managerial leg is
attributed to a document that does not contain it (CH-03): the Q3-1999 10-Q, cited as the carrier of the Wilke
instrument, has **zero** occurrences of the name, and Wilke is disclosed in-window only at 1999-10-28 — after the
date the recommendation closes on. Third, one stated duration contradicts the dates on either side of it in the
volume's own text (CH-02, twenty-two months against eleven).

These are local, evidence-named and repairable without disturbing the boundary contest. None of them is a reason
to re-run the stage. Certifier did not edit any stage volume, register, dossier or source file; every remedy
below is proposed for a different agent.

STATUS: WRITTEN 2026-09-25

## Defect register

Addresses are stable labels, not line numbers (method §14 rule 12). Severity is this audit's judgment on the
chronology layer only. I have proposed every fix and executed none.

**CH-01 — HIGH — a retracted dating test is still a live register row, contradicted in the same file.**
`timeline.csv`, stage3 row keyed `1999-h1` ("First distribution centre the company states it opened (Nevada);
five more announced for Kansas, Georgia, Kentucky, Germany and the UK"), Confidence `High`, notes: "Q2 1999 10-Q:
'the Company opened a new distribution center in Nevada'. **The verb, not the lease, is the event.**"
*What the text asserts:* that the Q2-1999 10-Q carries the company's first opened-state distribution-centre
disclosure, and that the verb is the discriminating event. *What the documents say:*
`10-K_FY1997_…filed-1998-03-30.txt` l.1647 "In November 1997 the Company **opened** a 200,000-square-foot
distribution center in Delaware" — ~20 months earlier; `ARS_1998_…filed-1999-04-07.txt` l.160 "We **opened**
distribution and customer service centers in the U.K. and Germany" — 11 weeks earlier;
`10-Q_Q1-1999_…filed-1999-05-17.txt` l.592 and l.915 "leased and opened a distribution center in Nevada" — the
**same plant**, one quarter earlier. `stage_3_part_1.md` §STAGE BOUNDARY JUSTIFICATION voids the criterion,
U.153 registers the void, and `timeline.csv` itself carries rows keyed `1997-11` ("…Form 10-K405 FY1997 l.1646-1648
uses the word 'opened' — falsifies the first-'opened' dating test for a later boundary") and `1997-12-31` ("First
filed use of 'opened' for a second distribution center"). One register therefore asserts "first", asserts
"not first", and grades both High.
*Proposed remedy:* (a) strike "First" from the `1999-h1` event text and restate it as a re-recital; (b) replace the
"verb, not the lease" note with a pointer to U.153 and to the `1997-11` row; (c) move the row's date key from
`1999-h1` to the quarter it reports — the opening was disclosed in the quarter it happened (Q1-1999, filed
1999-05-17), so dating the event to the half-year of the re-recital is itself the outcome placed after its own
carrier; (d) resolve the row's dangling `source_id` (`UNRESOLVED(cand=S30010|S30064)`) at the same time, since
the row cannot be re-cited without it. Method §14 rule 10: the retraction is not finished until it reaches the
instruction layer, and a stage register is that layer for every downstream agent.

**CH-02 — MEDIUM — a stated duration contradicts the date printed elsewhere in the same volume.**
`stage_3_part_1.md` §A.0 first sentence: at 1997-05-16 Amazon was "a **Delaware corporation twenty-two months
old**". *Document:* `424B1_final-prospectus_…filed-1997-05-15.txt` l.366-367 "The Company was incorporated in
Washington in July 1994 and reincorporated in Delaware in **June 1996**"; l.4004 "On **May 28, 1996**, the Company
reincorporated in the state of Delaware". May–June 1996 to 1997-05-16 is **eleven to twelve months**. Twenty-two
months reaches back to ~1995-07, a date no document in this corpus assigns to the Delaware form; it is consistent
with the company's own age counted from a mid-1995 start, which is a different subject. The same volume's
Stage-2 boundary row correctly prints "Delaware form effected **1996-06-18**".
*Proposed remedy:* set the elapsed period to eleven months against the 424B1's June 1996 date, or split the
sentence ("twenty-five months as a going concern; eleven as a Delaware corporation"). Separately: this corpus
carries **three** dates for one event — 1996-05-28 (424B1 l.4004), "June 1996" (l.367) and 1996-06-18 (Stage 2's
boundary row, and the volume repeats it at line 101 of the boundary table). Under §3 and §13 those are version
differences to be registered as a conflict with each carrier named, not merged into a month.

**CH-03 — MEDIUM — the recommended boundary's managerial leg rests on a document that does not contain it.**
`stage_3_part_1.md`, §STAGE BOUNDARY JUSTIFICATION, Position C row and the CLAIM C block of U.153: M′ is satisfied
by "**three senior operating offers inside thirty days — Wilke 1999-09-02, Jenson 1999-09-04, and Galli's offer
letter amended and restated 1999-09-30** — … disclosed by the Q3-1999 10-Q filed **1999-11-15**".
*What the documents say:* `10-Q_Q3-1999_…filed-1999-11-15.txt` has **zero** occurrences of "Wilke"; l.824-826 names
Galli and Jenson only. Wilke appears in-window first at `8-K_event-1999-10-28_…txt` l.339-342 ("Jeffrey A. Wilke
was named vice president-general manager of operations"), i.e. **28 days after the date the recommendation closes
on**, and otherwise only in `10-K_FY1999_…filed-2000-03-23.txt`. The 1999-09-02 execution date itself is carried
solely by that 10-K's exhibit index (10.11), a 2000 document — which this volume's own header (Record-selection
null) rules admissible "as *records of in-window state*, never as what a 1999 reader could know".
*Consequence for the boundary:* two of the three instruments are disclosed in-window at 1999-11-15; the third is
disclosed at 1999-10-28, and at the closing date itself nothing in the corpus discloses the Wilke hire. This does
not void C's date (the instrument was executed 1999-09-02), but it falsifies the sentence's disclosure claim and
it puts a `(PB)`-carrier at the load-bearing point of an un-`(PB)`-tagged row.
*Proposed remedy:* re-attribute the Wilke leg to `8-K(1999-10-28)`; mark its 1999-09-02 date "execution date
evidenced only by the FY1999 10-K exhibit index (2000-03-23) — `(PB)` carrier, `RETROSPECTIVE CARRIER`"; and add
to U.153's RESIDUAL UNCERTAINTY that no in-window document discloses the third instrument before the boundary
has passed. *Verified sound on the same row:* the exhibit index (l.4525-4533) does list **four** offer letters,
three of them dated or amended-and-restated in September 1999, so the falsification of Position A's "only filed
executive hiring package" claim stands.

**CH-04 — MEDIUM — a quotation is attributed to the earlier of two accessions and only exists in the later one.**
`stage_3_part_1.md`, Position A row of the boundary table, quoting the **Q2-1999 10-Q**: "In late June 1999
Amazon.com named Joseph Galli**, Jr.** as its **P**resident and **C**hief **O**perating **O**fficer".
*Document:* `10-Q_Q2-1999_…filed-1999-08-16.txt` l.818-819 reads "In late June 1999 Amazon.com named Joseph Galli
as its president and chief operating officer." — no "Jr.", lower-case titles, and the words "Jr." appear nowhere
in that accession (grep count 0). The quoted string belongs to `10-Q_Q3-1999` l.824-825.
*Why it matters here:* the defect is precisely the species this volume is prosecuting — a priority claim resting
on the wrong accession, in the passage that determines which document is first. The Q3 wording is a re-recital of
the Q2 sentence one accession later, the same relationship the volume correctly identifies for the Nevada
"opened" sentences.
*Proposed remedy:* either quote Q2-1999 verbatim or re-attribute to Q3-1999 (1999-11-15) and note that the
earlier Q2 disclosure is the one A's date turns on.

**CH-05 — MEDIUM — a reconciliation is asserted in a confidence cell that does not foot against the filed line.**
`stage_3_part_3.md` §Q, the row dated `1997-11-07 → 11-10` ($75m Deutsche Bank facility), Confidence cell:
"§P202's **76,702 at 1997-12-31 is this facility net of a $47 repayment**".
*Document:* `10-K_FY1997_…filed-1998-03-30.txt` l.1213 prints 76,702 as "Long-term debt, net of current portion"
in Selected Financial Data; Note 3 (l.2312-2345) prints "On December 23, 1997, the Company borrowed $75 million
pursuant to a three-year senior secured term Loan" and **no repayment of any amount** before 1997-12-31.
`10-K_FY1998_…filed-1999-03-05.txt` l.2815 prints "The debt is to be repaid in four equal payments" — i.e.
~18,750 per instalment, beginning after the year-end. Arithmetically 75,000 − 47 = 74,953, which is 1,749 away
from the filed 76,702, and the 1,749 is unattributed. A grep for any `47` repayment figure in the FY1997 report
returns nothing.
*Why it is a chronology defect, not only an arithmetic one:* the cell places an event (a repayment) inside a
period whose documents record none, and uses it to explain a balance. That is an outcome without a cause, and it
is in the row that anchors the stage's "debt pivot".
*Proposed remedy:* delete the identity, or replace it with the filed composition of 76,702 with each component's
line, or mark the reconciliation UNKNOWN. If the $47 came from a dossier, method §14 rule 8 applies: grep it
first; here it occurs zero times on disk.

**CH-06 — MEDIUM — a stated interval contradicts the dates on either side of it, in the same §Q row.**
Same row, event cell: "**The company that four months earlier had $79k of working capital** now takes secured bank
debt". *The volume's own dating:* §A.0 (`stage_3_part_1.md`) attaches the $79,000 working-capital figure to
**1997-03-31** ("256 employees at 1997-03-31 and $79,000 of working capital against $16,005k of quarterly sales",
carried from S2 §A). 1997-03-31 → 1997-11-07 is **seven months**; from the stage's opening 1997-05-16 it is under
six. No reading of the two flanking dates yields four.
*Proposed remedy:* restate as "seven months after the last filed working-capital figure of $79,000
(1997-03-31)". Note for the repairer, outside my layer: I could not locate $79,000 as working capital in the
424B1 on disk, and the FY1997 10-K's own selected data prints 1996 working capital as **2,270** and 1997 as
**93,517** (l.1211) — the carried figure's basis is a question for the numbers audit, and CH-06 stands on the
interval alone regardless of how that resolves.

**CH-07 — MEDIUM — the register records as a null a publication date the document itself prints.**
`sources.csv` row **S30071** (HistoryLink.org Essay 23230, "Amazon: The Early Years (1995-1999)"):
`event_date` = `1995-1999`, `publication_date` = **`UNKNOWN-essay-date`**, tier `3`.
*Document on disk:* `sources/historylink-essay-23230_Amazon-The-Early-Years-1995-1999.txt` header line 7 prints
"Publication / issue date : essay posted **2025-04-07**", and the body quotes a 2010 Princeton address, a 2011
Kaphan remark and "As of 2025, Scott retained a 4 percent ownership stake". `stage_3_part_3.md` §T records the
correct date (2025-04-07) and grades the essay "derivative by its own footnotes — every day-level and dollar-level
detail traces to Stone (2013) or press".
*Why it is chronology:* this is the single most hindsight-exposed artifact in the Stage-3 archive, and the register
is the field every later agent filters in-window rows on. A 2025 essay registered with no date, carrying an
event-date span that reads as in-window, is exactly how post-boundary material drifts into a Stage-3 row. The
narrative is honest; the join key is not. Also a §13 violation: `UNKNOWN` is a legal value, `UNKNOWN-essay-date`
is not an ISO date and not the literal `UNKNOWN`.
*Proposed remedy:* repairer sets `publication_date=2025-04-07`, adds `RETROSPECTIVE SOURCE` to
`evidence_class`/`independence_note` as already worded in §T, and reconciles the tier (register `3` vs §T "2 at
best"). No Stage-3 §P/§Q/§R row was found resting on this essay, so no narrative change is needed.

**CH-08 — LOW — §Q breaks its own stated ordering rule twice.**
`stage_3_part_3.md` §Q preamble: "**Rows are ordered by date.**" The row dated `1998-06-03 / 06-12` (two S-4s) is
printed before the row dated `1998-06-01` (2-for-1 split effected); the row dated `1998-11-19` (3-for-1 split
announced) is printed before the row dated `1998-11-17` (video store launch). The second pair matters more than
it looks: 1998-11-17 is the only day-dated product launch in the entire stage, and the day after it is the row a
reader uses to situate it.
*Proposed remedy:* re-sort the four rows, or amend the preamble to state the real rule (grouped, then ordered) so
a later reader does not read an ordering argument into the geometry.

**CH-09 — LOW — a citation range that does not contain one element of the row it supports.**
`stage_3_part_3.md` §Q, row `1997-11` (Delaware centre), cites `10-K405/97` l.1643-1652 for a cell containing the
city "**New Castle**, Delaware". The MD&A sentence at l.1647 names only "Delaware"; the city is printed at
l.1075 in Item 2 Properties ("a 200,000-square-foot facility located in New Castle, Delaware under a lease that
expires in October 2002"). Same accession, so no lineage or dating error — but the cited range does not contain
the quoted place-name, which is the shape of defect CH-04 has in a harmful form.
*Proposed remedy:* extend the citation to `l.1069-1080, l.1643-1652` (claim record B125 already cites the correct
Item 2 range, so the fix is a pointer copy, not new research).

**Note, not a defect (basis observation for the numbers audit).** In `stage_3_claim_records.md`, A29 derives
FY1998 international dollars as `0.20 × 609,996` while A28 derives the FY1998 segment ratio as
`21,806 ÷ 609,819` — two printed values for one fiscal year, each correct against its own carrier (FY1998 10-K
own-year vs FY1999 10-K comparative). Nothing is averaged and no range is presented, so this is **not** a
version-discipline defect. The gap is that neither record cross-references the other, so the appendix shows FY1998
net sales on two bases in adjacent rows without a word of warning. Worth one sentence in each record's `Conflicts`
cell; belongs to §U parity, and U.126 may already carry it — I did not open U.126's text.

STATUS: WRITTEN 2026-09-25

## Checks that passed

Each of these was tested by grepping the local source text, not by reading the citation's own label.

1. **The boundary falsification holds, verbatim, at the cited lines.** Position A's first-use test is defeated by
   three earlier Tier-1 strings, and all three are on disk where claimed: FY1997 10-K405 l.1647 ("In November 1997
   the Company opened a 200,000-square-foot distribution center in Delaware and expanded its Seattle distribution
   center to 85,000 square feet"); ARS 1998 l.160 ("We opened distribution and customer service centers in the U.K.
   and Germany…"); Q1-1999 10-Q l.592 and l.915 ("A new distribution center was leased and opened in Nevada during
   the quarter"). The 424B1's filing date (1997-05-15) is on the filename and the accession, so the stage's opening
   date is documented, and no dossier proposes an alternative — the opening boundary is uncontested and correct.
2. **The other load-bearing quotations in the boundary section are all in their cited documents**: Q1-1999 10-Q
   l.637 "Revenue related to auction services was minimal" (used to downgrade A's Axis T to PASS-on-definition);
   Q3-1999 10-Q l.1631-1633 "no previous experience with automated distribution centers, as the two distribution
   centers in operation prior to 1999, in Washington and Delaware, were manually operated" (C's P′ leg and ST3E-08);
   Q2-1999 10-Q l.822-823 "During the six months ended June 30, 1999 the Company opened a new distribution center in
   Nevada"; Q3-1999 l.829-833 five opened DCs with Kentucky also listed among the announced.
3. **Outcome-before-cause, tested where the corpus is most exposed to it, and found clean.**
   A19's cause date 1998-08-27 is the PlanetAll completion, printed at `8-K_event-1998-08-27` l.130-131 under a
   merger agreement dated 1998-08-03; the restatement sentence appears only in later carriers (Q3-1998 10-Q,
   8-K 1998-10-28, FY1998 10-K), so the restatement is correctly placed after its cause and each carrier is dated.
   §Q's priority claim that the FY1997 gross-fixed-asset figure **13,490** appears "before the FY1998 10-K prints it
   as a comparative" is verified: it is in the 1998-08-27 8-K at l.1485 and l.2327. U.147 is the right home for it.
   The B&N/Ingram item placed inside the 1998-12-31 row is supported by the filing's own words "In late 1998,
   Barnes & Noble announced an agreement to purchase Ingram" (FY1998 10-K l.797-799, l.2375-2376).
4. **Post-boundary material is labelled where it is used.** The 2000-03-23 / 2000-09-08 rows and the 2000-02-29
   Associates count carry `(PB)`; the FY1999 10-K's own two filed clocks (index 2000-03-23, header
   `FILED AS OF DATE 20000329`) are printed as a difference rather than resolved silently; the amendment is
   registered as "AAP-99 (second state of the SAME instrument) — NOT a fourth source".
5. **Single-lineage inflation: not present in the claim-record appendix.** The field's own distribution is
   honest: by far the dominant value across both appendix files is `Corroboration: 1`, then `n/a` and
   `n/a (structural / assessment / negative result)`, and every multi-document claim I opened names the lineage
   problem rather than counting it as corroboration — "2 accessions, one registrant" (A19), "2 accessions, one lineage" (A30),
   "1 (same lineage: 10-K/10-K/A one document)", "1 lineage" (A33), "0 independent" (A31). A17, which could have
   been scored as two sources, says "2 form families describing **one transaction**". I found no record asserting
   independence between two documents of one registration lineage. §T states the rule per family (the seven EX-27
   re-recitals, the ARS-as-re-presentation, the five distinct shelf lineages) and the FY1998 10-K's FY1997
   comparative is named "a recast of S0805's own-year column, not a corroboration".
6. **Version differences are conflicts, not averages.** The pairs 147,758/147,787, (27,590)/(31,020),
   609,996/609,819, 133,841/133,664, 9,692/9,421 and the 2000 cash restatements (+23,685 → (38,536)) are each
   printed as two states with their carriers and routed to U.125 / U.126 / U.145 / U.147 / U.154 / U.159 / U.164.
   No mean, no range, no "approximately".
7. **Retrospective-source handling in the narrative is correct** — the class the brief warned about. Sheff/*Playboy*
   is registered "conducted 1999 / published 2000", tagged `RETROSPECTIVE SOURCE`, tiered "1 as a 1999/2000
   artifact; **4 as evidence for 1997-99**", and the §T cell states that no §P/§Q/§R row rests on it; the two ARS
   letters are expressly ranked above it for founder-state claims. The 2005-anniversary-type and web-capture
   artifacts are handled the same way: the Wayback null file is registered as "evidence about the record, never
   about the site", with the HTTP 504 prefix queries correctly recorded as a failure rather than a null, and the
   NCSA/Mosaic and First Virtual captures are Stage-1 rows used for their own dates. **The defect is only in the
   register's date field for the essay (CH-07), not in how it is used.**
8. **No dated artifact was cited for something its date cannot reach, in the rows I opened.** The most tempting
   drift in this window — a 2000 document re-dating a 1999 event — is pre-empted: zShops' "late September 1999"
   (Q3-1999 10-Q) against the FY1999 launch table's "October 1999" is registered as U.155 with both texts printed
   and the day declared unobtainable, not harmonised to one month (A30). The music store is carried at month
   confidence with `UNKNOWN (day)`; the UK/German opening likewise.
9. **Split-vintage ordering is chronologically sound.** The 3-for-1 announced 1998-11-19, effected 1999-01-04/05
   with record 1998-12-18; the 2-for-1 approved 1999-07-21, effective 1999-09-01; the FY1998 10-K's own F2
   footnote that the selected data "HAVE NOT BEEN RESTATED FOR THE STOCK SPLIT" is quoted as the reason one
   document carries two share bases — which is the correct handling of an instrument that post-dates its own
   printed comparatives.

STATUS: WRITTEN 2026-09-25

## Things I could not test

1. **Whether the $79,000 working-capital datum in §A.0 is a filed figure at all.** I tested only its interval
   (CH-06). The string does not appear as working capital where I looked in the 424B1 on disk, and the FY1997
   10-K's selected data prints 1996 working capital as 2,270 (l.1211). A number arriving from an upstream stage
   and not found on disk is §14 rule 8 territory — but that is a numbers-audit call, and RD-076 already lists a
   re-based 1996 working-capital leg among the four carried defects. **Classified as a suspicion, not a finding.**
2. **What the 8-K/A of 1998-10-26 actually corrected.** §Q grades it High that an amendment exists and UNKNOWN as
   to substance, and routes the question to §S. That grading is defensible; I did not test it, because reading the
   amendment's body is the sources layer, not the chronology layer.
3. **Whether the May-28 / "June 1996" / June-18-1996 reincorporation spread is a genuine version difference or
   three different events** (board action, effective date, filing date). The 424B1 gives two of them and Stage 2
   gives the third. I could not tell which the corpus means, so CH-02 asks for a conflict entry naming each
   carrier rather than asserting one.
4. **The independence of the FY1997/FY1998 comparative pairs from an auditor's standpoint.** I verified that the
   two printings are labelled as recasts and not counted twice. Whether E&Y's dual-dated opinion (Feb 2 2000,
   Note 15 Feb 16 2000) makes the 10-K/A a second *witness* rather than a second *copy* is a judgment about
   audit evidence, outside chronology.
5. **Anything that depends on a document not in `sources/`.** The non-Amazon 1997-99 periodical family is absent
   from disk (recorded UNTRIED in §T with queries), the 35 further 424B3 supplements and 10 third-party Schedule
   13s were deliberately not fetched, and the B&N 10-K is held only through a Stage-2 dossier. A day-level
   commissioning date from local press could displace every boundary candidate, as the boundary section itself
   says. **I did not go and fetch any of it:** zero-web budget, and a document that is not on disk is a finding
   in this audit, not a task.
6. **Whether the §Q table's `(L)` lineage marker was applied consistently.** The convention is stated in the
   preamble and used on the opening row and the FY1996/S-1 rows; I spot-checked three uses and they are correct,
   but I did not audit every cell's `(L)`, and the gates report that 3 `S3001`-family source tokens in Stage 3 do
   not resolve at all — so some rows cannot be joined to a document by machine, which limits what any check here
   can certify about their lineage labels.

STATUS: WRITTEN 2026-09-25

## Untried

Not examined at all on this pass. This is the coverage note; none of it is a null result.

**Volumes and sections.**
- `stage_3_part_1.md` §B through §J (≈34,000 words) — read for the boundary and §A.0 only. Specifically
  unexamined: §B.1 "Dated ladder, Stage 3" (a chronology table, and the most likely place in the corpus for a
  sequence defect), §B.3 "who ran it, dated", §B.5 headcount's three filed dates, §B.6 the estate "as an
  instrument chain", §D.0 signal ledger, §G.1 "nine openings, four kinds of evidence" (the single richest source
  of opening-vs-announced-vs-leased date drift in the stage), §E.1 category ledger, §F.1 customer series.
- `stage_3_part_2.md` §K–§O in full, except the two sentences I traced into the boundary section. **§K.8 "Split
  vintage — the one arithmetic trap that manufactures false conflicts" was not read**, though CH-05 touches its
  subject matter; §L validation-signal ordering and §M failures-by-date were not read; §N decisions table
  (state-before / information-available) is the file where an outcome can most easily precede its cause and I
  did not open it.
- `stage_3_part_3.md` §P, §P.2a, §P.2 arithmetic tables t11/t17/t18, §R snapshot, §S gaps, §U.114–U.168 text.
  **Only U.153 was read in substance.** The other 54 conflict entries were seen only as pointers from §Q rows,
  which means I certified that §Q *routes* to them, not that they are correctly dated.

**Registers.** Of the nine, I examined `sources.csv` (targeted rows) and `timeline.csv` (stage3 rows, ordered
scan). Untouched: `quantitative.csv`, `validation.csv`, `failures.csv`, `decisions.csv`, `channels.csv`,
`conflicts.csv`, `data_gaps.csv`, and `stage_3_pending_registers.md` including its 134 unapplied rows and the ten
held rows at §S.9. **The index itself flags two chronology-shaped open items I did not chase:** `decisions.csv`
block row 3 (the 1998-06-01 stock-dividend row whose date and citation cannot both stand — directly a
dated-but-not-dated case) and `failures.csv` block row 8.

**Claim records.** Volume 1 declares 596 records (§A09–T58) and volume 2 declares 55 §U conflict records; my own
line-count grep finds 312 record heads in volume 1 and 56 in volume 2, so a portion of the appendix is not keyed
in the form a machine can enumerate — itself a note for whoever re-keys the spine. I read volume 1's §A block
(A16–A34) and B125 in full and searched the whole appendix for corroboration claims. **§C, §D, §E–§T and all 55
§U records were not read**, so "no single-lineage inflation found" is a finding about the sample plus the field's
overall vocabulary, not about every record.

**Dossiers and assembly copies.** No file under `research/` was opened (the brief's scope is the published
volumes and registers; every dossier-level assertion I tested I tested against the filing). `_parts/s3_p1–p4.md`
were not diffed against the published parts — a drift between an assembly copy and its volume would be invisible
to this pass.

**Families never tried, per method §14 rule 6.** Non-Amazon periodicals and local-newspaper back files for
1997–1999: **UNTRIED by all four Stage-3 dossiers and by me** (§T says so). Auction/museum documentary records:
UNTRIED. Section 16 Forms 3/4/5 in catalogue slice `-001`: UNTRIED. The `tools/` periodical-harvest run records:
UNTRIED. Any dated amazon.com page inside the window: the corpus contains none and the deep-path CDX queries
returned 504, so that leg is UNANSWERED rather than EMPTY.

STATUS: WRITTEN 2026-09-25

