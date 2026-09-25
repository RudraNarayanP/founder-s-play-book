# amazon_s3_audit4_hindsight.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:05:44Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

STATUS: WRITTEN

**AUDIT 4 (Amazon Stage 3, hindsight layer) — FAIL, with 5 high-severity defects.** 16 findings total: **5 HIGH,
9 MEDIUM, 2 LOW.** Calibrated against `amazon_s2_audit4_hindsight.md`, which returned FAIL on a comparable tally
(5 outcome-dependent claims at 9 sites, 1 failing coda of 9, 4 `(PB)` misuses, 6 register-drift findings): Stage 3
has fewer linguistic failures and a better-built firewall, but it carries one outright factual self-contradiction
(**H-1**) and the registers are missing the stage's most adverse audited facts (**H-4**), which is the defect
class that survives an audit cycle because no script looks for it.

**Why not PASS-WITH-DEFECTS.** Three of the five HIGH defects are causal readings whose alternative explanation
is refuted by a table inside the same volume (H-1 strike-vs-gate; H-2 the softened admission; H-3 per-order cost
where §K.6 registers it UNKNOWN), and H-4 means §8/§13 are unmet for load-bearing values. Method §11 makes a
failed hindsight audit a `RECONSTRUCTION`, not a `QA → COMPLETE`, text.

**What passes, and should not be re-audited.** The firewall is structural, not decorative: §C.1 exists precisely
to separate later narrative from in-window documents; `(PB)` tagging (80 sites) plus §H.2's admissibility ruling
keep 2000-printed data out of 1997–99 readers' hands; the Sheff interview is ranked below the ARS on publication
date, not label (§N limit ii); the record-selection null is stated in §A/§N/§R; §D.4 excludes seven popular
signals with reasons; §E.6/§H.3/§I print the full §16 quartet; the anti-hagiography question answers cleanly —
this stage's own conclusion is that **no candidate signal demonstrates a repeatable model**, which is the reading
that survives a 2000 failure. Nothing found here contradicts that spine.

**Repair conditions to convert this to certifiable.** H-1, H-2, H-3 and H-5 are **relabel / re-source / cut**
edits in existing sentences; M-1…M-9 are relabels plus one arithmetic request. **H-4 is the only finding that
needs work of another kind** — new `quantitative.csv` and `failures.csv` rows keyed to `10-K/99` l.4155-4200,
l.1890-1892, l.2545 and the 10-Q cumulatives, all of which are already on disk. **No new retrieval is required
for any of the 16**, and none of the corrections touches a value: every register figure I recomputed footed.
Execution belongs to a repair agent; this certifier edited no stage volume, register, dossier or source.

## Defect register

STATUS: WRITTEN (certifier only — no stage volume, register, dossier or source was edited on this pass)

Scope audited: the hindsight layer of `stage_3_part_1.md` (§A–§J + §C/§D/§G/§H/§I codas), `stage_3_part_2.md`
(§K–§O, with §L/§M/§N/§O read in full), `stage_3_part_3.md` (§P–§U, with §R, §S and the §P.2 arithmetic blocks
read), and the company registers at `company_001_amazon/`. `stage_3_claim_records.md` (+ `_part_2`) were swept
for construction counts only, not read line by line (see Untried).

**Headline.** This is the strongest hindsight discipline in the corpus so far: the anti-hindsight machinery is
built in (the §C.1 "later narrative vs in-window document" table, `(PB)` post-boundary tagging at 80 sites,
`mechanism UNKNOWN` at 7 sites, alternative-explanation language at 21 sites, zero occurrences of
`inevitable/destined/trajectory/set the stage/would later/in hindsight`), and the §E/§H/§I codas each carry
evidence → mechanism → alternative → confidence. The failures that remain are not the classic ones. They are
(a) causal readings whose *alternative explanation* is contradicted by the volume's own data tables, and
(b) the load-bearing figures never reaching the registers, which is where a later reader gets its numbers.

**Block order:** MEDIUM and LOW print before HIGH as an artefact of the edit sequence on this pass; read
**HIGH** first.

### MEDIUM

**M-1 · `stage_3_part_1.md` · D.3 (closing sentence, keyed `§D.3`) — a cost-of-capital mechanism asserted with
no comparable price observation, no alternative, no confidence.**
Offending text: "**The largest signal in this window is that the cost of capital fell, not that the cost of
doing business did.**" The supporting list is 10% Senior Discount Notes (1998, no cash coupon before
2003-11-01, $530m principal at maturity against ~$326m gross) and 4¾% convertible subordinated notes (1999,
with a $156.055/6×-vintage conversion option). A zero-coupon senior discount note and a cash-coupon convertible
subordinate are not the same instrument on the same security ranking: the convert's coupon is low *because* the
equity option carries the consideration, and §L/§N of the same stage say so ("the conversion price … was
**below every filed 1999 quarterly high**, so the embedded equity option was live from the first quarter after
closing"). So the printed coupons move in the direction of the claim only by ignoring the option value that
explains them. The market-condition alternative (1999 technology-paper demand, which §O.1 itself invokes as "a
window open for US high-yield convertibles") is not tested against the claim, and the coda carries no confidence
grade, which §7/§16 require of interpretive prose.
*Remedy:* either compute effective yields (accretion to $530m face vs 4¾% cash plus conversion value) in one
shown DERIVED line, or restate as INFERENCE at Medium/Low with the 1999-market alternative named.

**M-2 · `stage_3_part_2.md` · §L row 1998-04-24 → 1998-05-05 — a bank covenant's end credited to bondholders,
and the motive stated flat where §N grades it Medium-inferred.**
Offending text: "at a moment when the only secured money available had covenanted on its **accounts-payable
aging** — the removal of that covenant was itself the validation, **and it came from bondholders**"; and in the
same cell: "the upsizing happened in a **1998 bull bid for convertibles**".
The covenant did not come off at bondholders' hands: it ended because the company repaid the secured facility
with the notes' own proceeds — `sources/10-Q_Q1-1998_acc-0000891020-98-000846_filed-1998-05-15.txt` l.988-989
"The Company has repaid the Senior Loan in full with a portion of the net proceeds of the Senior Discount
Notes", and §N row 1's own 424B2 use-of-proceeds citation. §N row 1 grades the *same* inference "**Medium** on
the covenant motive, which is inferred from the ordering of the company's own use-of-proceeds sentence rather
than stated"; §L states it as fact, in a validation table. The "convertibles" label is also wrong for a
non-convertible senior discount note.
*Remedy:* re-source to the repayment (FACT, High), downgrade the covenant-motive reading to §N's Medium wording,
delete "convertibles".

**M-3 · `stage_3_part_2.md` · M.3 — a transfer of money between captions asserted where both captions grew.**
Offending text: "the ratio fell because the **denominator was pulled up by the first-party merchandise base
while the money actually spent to serve each customer moved out of advertising and into fulfilment**".
By M.3's own four-figure list advertising rose $21.2m → $60.2m → $140.9m (2.34× in 1999) — nothing moved *out*
of advertising; advertising and fulfilment both grew, fulfilment faster (3.75×), so the shares moved. The
sentence is a manufactured mechanism that its own paragraph refutes, and "per each customer" reintroduces the
per-unit basis H-3 flags.
*Remedy:* replace with the relative-growth statement the table supports, at High, and drop the movement verb.

**M-4 · `stage_3_part_1.md` · §D.0 final row (Q4-1999 inventory charges) — confidence understated and
contradicting §G.0/§M.4/§N-5/§O.1.**
Offending text: magnitude cell "**no day, no amount in that sentence**"; Conf cell "High (incurred); **UNKNOWN**
(size)". The amount *is* filed in the same document at FY1999 10-K l.1892 ("inventory-related charges of
approximately $39 million incurred in the fourth quarter of 1999", the line §M.4 quotes and §G.0 row 6 relies
on: "whose amount it then gives"). Registering the size as UNKNOWN while four other volumes' sections use
$39m — including a DERIVED 13.4%-of-gross-profit claim — is an internal inconsistency in the same direction the
audit corrected at §A.3.
*Remedy:* Conf → High (incurred, amount, quarter); UNKNOWN only for the category split and the day; make the
"no amount" claim read "in that sentence, though the same report gives ~$39m at l.1892".

**M-5 · `stage_3_part_1.md` · §C assessment coda (keyed `§C.2` assessment, l.570 block) — §16 quartet incomplete
and an outcome word for a contested boundary.**
Offending text: "The mechanism connecting Stage 3's filings to Stage 3's **outcome** is **financed capacity**";
and "**no independent witness to demand exists at any date**."
Evidence, mechanism and alternative are present and good; the **confidence grade is missing**, which is the one
§16 duty this coda does not perform — and §C.1's own table grades the same proposition Medium-High. "Outcome" is
the wrong object for a stage whose endpoint is argued four ways on the same page (§STAGE BOUNDARY
JUSTIFICATION); the firewall asks for end-of-stage state. The second sentence is a corpus-total negative stated
absolutely, whereas the volume's own convention elsewhere scopes it ("across all 99 files", §I's provenance
boundary); no third-party document of any date is in `sources/`, so "exists at any date" claims more than the
search supports.
*Remedy:* append Conf; replace "outcome" with "state at the recommended boundary"; scope the null to the local
corpus.

**M-6 · `stage_3_part_3.md` · §R "Current objective (in-period, as evidenced)" row — an intent attribution
graded High on what the row itself calls an inference.**
Offending text: "**High (that capacity was the objective, as a reading of what the money and the filings were
for)**", sitting beside "UNKNOWN (any internal number, authorship, deliberation)" and "No quantified internal
target surfaced for any date in this stage."
Grading *what the company was trying to do* at High from the direction of capital flows is exactly the reading
§N's evidentiary limit refuses ("no board minute, no plan document, no option list survives"; rationale confined
to two ARS-signed rows). Capacity is at least as well described as the disclosed **constraint** — the filings
the row cites call it "dependent on expansion of our infrastructure" — and an objective whose content was never
stated internally cannot be High.
*Remedy:* relabel INFERENCE, Medium, with the constraint-vs-objective alternative in the same cell; point to §N's
limit.

**M-7 · `stage_3_part_1.md` · §D.0 row "$1.25bn converts" — a capital-supply event labelled demand-side.**
Offending text: "the **hardest external demand-side signal in the stage**: professional investors sized the
unproven model at $1.25bn inside a week". Note-buying is a supply of capital; "demand-side" in this stage's own
vocabulary means customer demand (§D.2's GMV/listings discipline, §H.3's "NOT KNOWABLE as demand"). The label
borrows the later marketplace sense of "demand" and, left in place, lets a financing row do the work of a
sales row in the signal ledger.
*Remedy:* "the hardest external **capital-**supply signal"; §L's "clearest external price signal" is the correct
formulation and should be the one propagated.

**M-8 · `stage_3_part_1.md` · §C.1 ("The later narrative, separated from the in-window record") — the refuted
column has no published source.**
The seven quoted narratives ("1997–99 is when Amazon became a general retailer", "By 1999 the company had
clearly broken through, and everyone could see it", "Its technology was the moat", "It acquired its way to the
platform, and the acquisitions worked") are printed in quotation marks with no source cell; where the row does
carry keys, they are to this project's own adversarial dossier (ST3E-04, ST3E-15/16, ST3E-22). An unattributed
quotation invites the reader to treat it as folklore the audit cannot name — and it is the one place in Stage 3
where text inside quotation marks may not be traceable to a document, which is the failure the run's earlier
verbatim gate already flags corpus-wide. As the firewall's showcase table, it should attack *sourced* claims.
*Remedy:* add a `Later narrative sourced from:` cell (published secondary work + date, or
`RECONSTRUCTED BY THIS PROJECT — authorship UNKNOWN`), and if reconstructed, restyle them as paraphrases rather
than quotations. Not a fabrication finding — an attribution finding.

**M-9 · `stage_3_part_1.md` · §A.2/§A.3 float row (keyed to the §A money table) — a universal mechanism adopted
beyond the corpus's reach.**
Offending text: "This is a *weaker* version of 'supplier float did the work' and a *stronger* version of
'**working-capital behaviour that only scale produces**'". The chosen formulation is a cross-firm generalisation
("only scale produces") and this volume's own provenance boundary (§I preamble, §H.0) records that **no
non-Amazon filing of the period is in `sources/`**, so no comparison that could support "only" exists anywhere
in the evidence base. The FY1999 10-K's payables stretch is filed; its cause is not.
*Remedy:* drop the counterfactual generalisation, keep the filed movement, mark mechanism UNKNOWN, or label the
sentence INFERENCE-with-no-comparator.

### LOW

**L-1 · `quantitative.csv` · stage-3 row "Revenue run rate asserted by the company" (ESTIMATE)** —
`derived_arithmetic` cell empty, which §13 makes mandatory for ESTIMATE/DERIVED. The arithmetic exists in the
narrative (§D.4, §L row 1999-01-26: `$252.9 × 4 = $1,011.6m`), so this is a propagation miss, not a missing
calculation. Sole instance: 1 of 30 stage-3 DERIVED/ESTIMATE rows.
*Remedy:* copy the arithmetic into the row.

**L-2 · `stage_3_part_2.md` · §L row 1999-02-03 — "the cheapest available signal of expected continued
appreciation"** (about the three splits) is a motive sentence for a board act with no minute; the same row's
Confidence cell already grades "Low as a validation signal". Carried as Low because §N's evidentiary limit
governs the table's *Rationale* column, not its prose cells. *Remedy:* relabel as INFERENCE or cut the adjective.

### HIGH

**H-1 · `stage_3_part_2.md` · O.1 (counterfactual "Raise equity first", keyed `§O.1`) — a false mechanism
carried into an argument, contradicting §M.13 and §L of the same file.**
Offending text: *"they were struck at a conversion price that **never entered the money on any filed 1999
range** (§M.13), so the equity option they sold never relieved the debt."*
The cited §M.13 says the opposite: "**$78.0275** (§K.4), so the notes were **in the money in every quarter of
1999 at their highs** — but the [redemption gate] … **$117.04** (DERIVED `78.0275 × 1.5`), and **no filed
quarterly high** [reached it]" (also §L row 1999-02-03: "below every filed 1999 quarterly high, so the embedded
equity option was live from the first quarter after closing"). The conversion *strike* was exceeded by the filed
Q2-1999 high of $110.63; what was never reached was the *150% redemption gate*. O.1 collapses strike and gate,
inverts the sign, then draws the economic conclusion ("never relieved the debt") from the inverted premise. This
is outcome-shaped reasoning in the one section whose job is to keep counterfactuals inside what was visible.
*Remedy (for a repair agent, not me):* rewrite the O.1 *For* leg as "the $117.04 redemption gate was never
reachable on any filed 1999 high, so the issuer could not force conversion, although the $78.0275 strike was in
the money at every 1999 quarterly high"; delete "never entered the money" and "never relieved the debt";
cross-reference the `N-5 vs M.13` conflict note already at the foot of §N.

**H-2 · `stage_3_part_2.md` · M.5 (heading, keyed `§M.5`) + `stage_3_part_1.md` · §G.5 row G31 — a wording
change read as disclosure management, with the obvious alternative unconsidered and contradicted by the
volume's own estate table.**
Offending text: "**The automation inexperience was admitted in writing — and the admission was then softened,
in the same corpus, before it could be read against the charge**"; "**'No previous experience' became 'limited
experience'** between November 1999 and March 2000, in the same document family, **without any stated change of
fact** — a softened admission, not a withdrawn one"; §G.5 G31: "**Two statements of inexperience, printed
weaker each time**, while the equipment contracts for three unnamed sites were already signed."
A change of fact is carried by this same file's evidence base: five automated plants **opened** during 1999
(§G.1 rows G3–G8; §D.0 "Five DCs opened in nine months"), so at the FY1999 count date "no previous experience"
had become literally false and "limited experience" true. "Before it could be read against the charge"
attributes a protective motive to a drafting change with no document; the unexamined alternative
(mechanical accuracy update after a year of automated operation) is the better-supported reading. Compare the
volume's own correct discipline at §D.1: the enumerated failure modes are "**enumerated, not evidenced as
experienced**, and this file does not upgrade them."
*Remedy:* keep both wordings and both dates (FACT); relabel the *softening* as RETROSPECTIVE INTERPRETATION at
Low; state the experience-accumulated alternative; delete "before it could be read against the charge" or
source it; G31 → "printed differently, as the automated estate opened".

**H-3 · `stage_3_part_2.md` · M.1 (keyed `§M.1`) — a per-order basis asserted where §K.6 registers per-order
cost as UNKNOWN.**
Offending text: "i.e. **the cost of delivering an order rose 3.24 percentage points of revenue** in the single
year the network doubled"; and §L row (music/video launch → FY1999 MD&A): "the cost of serving customers is now
an audited-adjacent, **quarterly-comparable** dollar series".
The 3.24 points are `11.49% − 8.25%` **of net sales**; there is no order count in any year of the stage, and
§K.6 prints "Contribution margin **per order**; fulfilment cost per order | **UNKNOWN** … no order count exists
to divide it by". The sentence performs precisely the substitution §K.6 forbids. The "quarterly-comparable"
label is unsupported too: the fulfilment series exists at three **annual** points out of one FY1999 note
(quantitative.csv rows 325–327), never filed quarterly.
*Remedy:* "fulfilment cost per dollar of net sales rose 3.24 points"; strike "quarterly-comparable"; carry a §6
basis note.

**H-4 · registers (`quantitative.csv`, `failures.csv`) vs narrative §C.0/§H.2/§L/§M.4/§N — the stage's most
adverse audited facts have no register row at all.**
String-checked across all nine company CSVs (188 stage-3 quantitative rows) and `stage_3_pending_registers.md`:
**zero hits** for `163,804 · 242,148 · 7,801 · 167,743 · 21,806 · 25,498 · 79,223 · 1,308,292 · 262,871` (the
FY1999 segment note and its comparatives), for the Q4-1999 inventory charge (`39 million`), `220,646`
(inventories), `13,871` (Q4-1999 D&A — arithmetic shown at §P.2 t17 and row P242, only a `timeline` row
exists), `125.2`/`101.3` (days payable; only 1998's 86.8 is registered), `1,263,639`, `178.4`, `126.0` (1999
debt proceeds and note repurchases), `1,099` (officer's note receivable).
These are load-bearing: §L calls the segment row "the single most adverse audited fact in the stage"; §M.4
builds DERIVED claims on the charge (`39,000 ÷ 290,645` = 13.4% of gross profit; 2.4% of net sales); §G.0 lists
CIP and the charge among its six load-bearing fact classes. Method §8 (no value without its source and
confidence cells) and §13 (one row per record; `derived_arithmetic` mandatory for ESTIMATE/DERIVED) are both
unmet, and `gates.py` does not test figure-to-row existence, so no other check will catch it. A downstream agent
working from the register — the deliverable per §13 — cannot reproduce the stage's central negative finding.
*Remedy:* new register rows per figure (document + line as `source`; FACT or DERIVED; arithmetic in
`derived_arithmetic`), plus a `failures.csv` row for the Q4-1999 charge. These are additions, not the two rows
already held in `stage3_register_merge_held_rows.md`.

**H-5 · `stage_3_part_1.md` · C.2 (closing sentence, keyed `§C.2`) — filed risk-factor boilerplate read as the
company's mental state, against this volume's own rule.**
Offending text: "**Read together these are the self-description of a company mid-build and unsure of the
machine, not of a company that had broken through.**", resting on "The company's own risk language is the best
available proxy for the questions it thought it was facing, because it is dated, filed and **legally exposed**."
"Legally exposed" cuts the other way: safe-harbour risk factors enumerate worst cases whether or not they are
experienced, so their bias runs *toward* over-stating trouble, and "unsure of the machine" is a mind-state
inference in the wrong direction from the class of text. The same volume refuses this at §D.1 ("enumerated, not
evidenced as experienced, and this file does not upgrade them"). The coda also measures the window against "a
company that had broken through", a benchmark no in-window document contains.
*Remedy:* relabel as CONTEMPORANEOUS OBSERVATION confined to "the registrant disclosed X on date Y"; add the
disclosure-incentive alternative explanation; downgrade "unsure of the machine" to INFERENCE at Low or UNKNOWN;
keep the filed list itself, which is sound.

## Sweep counts

STATUS: WRITTEN

Construction sweep over the whole Stage-3 corpus, not only noticed instances. Columns: `part_1 / part_2 /
part_3 / claim_records / claim_records_part_2 / total`.

| construction | 1 | 2 | 3 | CR | CR2 | tot | disposition |
|---|---|---|---|---|---|---|---|
| `proved` | 2 | 1 | 7 | 5 | 2 | **17** | all evidentiary (a filed document or an arithmetic identity proves a value) |
| `proves` | 4 | 1 | 10 | 7 | 2 | **24** | all evidentiary; 2 accepted-with-caveat (§G.4 "a fifth of the estate's book value was **not producing anything**" → "not yet in service"; §P258 "and what it proves" about a typographical correction) |
| `showed that` / `shows that` / `demonstrated that` / `demonstrates that` | 0 | 0 | 0 | 0 | 0 | **0** | clean |
| `drove` | 0 | 0 | 0 | 0 | 0 | **0** | clean |
| `did the work` | 1 | 0 | 0 | 0 | 0 | **1** | in §A money table, inside a formulation the row *rejects* — but the replacement it adopts is defective → **M-9** |
| `clearly` | 1 | 0 | 0 | 0 | 0 | **1** | inside a §C.1 quoted later-narrative it refutes → counts as **M-8**'s attribution problem, not leakage |
| `inevitab*` | 1 | 0 | 0 | 0 | 0 | **1** | verbatim Wal-Mart pleading language ("inevitably disclose") quoted in §B — not this project's voice |
| `the reason was` | 0 | 0 | 0 | 0 | 0 | **0** | clean |
| `the reason` (pointing at causes) | 2 | 4 | 7 | 3 | 1 | **17** | spot-checked: each names a documentary cause ("the reason §Q dates officers only from a proxy line"), not a teleology |
| `destined` / `turned out` / `eventually` / `later became` / `would become` / `set the stage` / `groundwork` / `trajectory` / `meant that` / `key to` | 0 | 0 | 0 | 0 | 0 | **0** | clean |
| `would later` / `in hindsight` / `with hindsight` | 0 | 0 | 0 | 0 | 0 | **0** | clean |
| coda / assessment markers | 7 | 0 | 1 | 8 | 0 | **16** | 2 fail the §16 quartet → **M-1**, **M-5** |
| `KNOWABLE` lists | 26 | 12 | 2 | 20 | 2 | **62** | §H.3 and §L/§N knowability blocks pass; no KNOWABLE list leaked a later fact in the rows read |
| `mechanism UNKNOWN` | 1 | 2 | 0 | 3 | 1 | **7** | honest nulls present — but only 7 against **18** asserted `Mechanism:`/`*Mechanism*` readings (**0.39 ratio**); §M.1/M.3/M.5, §A float row, §C.2, §D.3 are the surplus → H-2, H-3, H-5, M-1, M-3, M-9 |
| alternative explanation named | 13 | 7 | 0 | 1 | 0 | **21** | §U uses `WHY THEY DIFFER` instead, so part_3's zero is not a defect |
| `(PB)` post-boundary tags | 30 | 4 | 11 | 33 | 2 | **80** | working: every 2000-printed datum is tagged and admissibility argued (§H.2) |
| `RETRO` / `RETROSPECTIVE` tags | 8 | 8 | 11 | 12 | 2 | **41** | see Checks passed |
| teleology strings (`everything store`, `anything they might want to buy`, `general retail`) | 3 | 3 | 0 | 3 | 0 | **9** | 2 are the founder's own filed sentence; §C explicitly refuses "the 'everything store' teleology" |

Defect totals: **5 HIGH, 9 MEDIUM, 2 LOW = 16.**

## Checks passed

STATUS: WRITTEN

Run once for context, **not redone** (mechanical, per brief): `python tools/gates.py --company-dir
"founders_playbook/01_companies/company_001_amazon" --checks csv,keys,anchors` → **15 findings / 17 passes**.
Csv width drift (quantitative 13 rows, sources 26, conflicts 3, timeline 1, data_gaps 1); `access_date` = "NOT
ACCESSED IN THIS PASS (zero-web budget)"; `failures.csv` date "Stage 2"; unresolvable `S3001/S3004/S3007/S3012/
S3013/S3020/S3022/S3024/S3081` tokens in six Stage-3 volumes; anchor `U.220` with no register row; register rows
`U.201`–`U.211` citing anchors absent from the narrative. Two notes for the orchestrator, not defects of mine:
the `S3xxx` hits are the **retired dossier-local key space** that `stage_3_index.md` documents and the texts
mark `[RETIRED-KEY REFERENCE]`, so the key gate is reading marked residue; and `U.201–U.211` / `U.220` are the
same §U-parity gap the anchors gate has reported since before this pass.

Judgment checks that **pass**:
1. **Retrospective-source handling (§6).** The Sheff/*Playboy* interview is handled in the right order — §N
   evidentiary limit (ii): "**conducted 1999, published 2000** — contemporaneous in conduct, retrospective in
   publication, and ranked below the ARS for any claim about what Bezos believed in-window (ST3A-13's ordering)".
   The FY1999 10-K (printed 2000-03-23) is admitted for *state at* 1999-12-31 and expressly "inadmissible as
   something a contemporaneous observer could have read before 2000-03-23" (§H.2); §K.1 keeps "the FY1998
   audited series" apart from "the same years as re-witnessed in 2000"; §K.8 splits the 6×/12× share vintages
   before any per-share figure is used. No 1999 interview was found printed as a 1997–98 source, and no memoir
   or anniversary profile is used as evidence anywhere in the three volumes.
2. **Filing-lineage / independence (§3).** Applied and stated in the claim-records preamble and per row in §H
   ("the four annual reports are four states of the issuer's own annual reporting"); §I's provenance boundary
   records that only Amazon's own period documents exist, and competitor cells say UNKNOWN instead of being
   filled from memory.
3. **Record-selection null (§2).** Present in §A and in §R's snapshot row and §N's preamble ("only the chosen
   path was printed"; deliberations, rejected options and the missing independent count behind every self-report
   named).
4. **Anti-hagiography test (§2).** The stage's headline finding — "a capacity-and-participation build
   underwritten by capital markets", with **no** candidate signal demonstrating a repeatable model — would read
   the same if the company had failed in 2000. §L, §M, §R(11 evidenced weaknesses) and §S are structured to
   that end, and §D.4 excludes seven popular signals with reasons.
5. **§16 quartet in codas.** §E.6, §H.3 and §I each print evidence → mechanism → alternative → confidence; the
   two that do not are **M-1** and **M-5**.
6. **DERIVED arithmetic visibility in the narrative.** All three arithmetic chains I recomputed foot
   (`33,027 ÷ 118,969 × 365 = 101.3`; `113,273 ÷ 476,155 × 365 = 86.8`; `463,026 ÷ 1,349,194 × 365 = 125.2`;
   `188.4 ÷ 1,639,839 = 11.49%`; `39,000 ÷ 290,645 = 13.4%`; `2 × 3 × 2 = 12`), and §P.2 prints arithmetic for
   every derived figure the narrative uses **inside the narrative**. The failure is propagation to the CSV, not
   calculation → **H-4**, **L-1**.
7. **Borrowed wording.** No sentence was found that reads as verbatim secondary-source prose presented as this
   project's finding; every quotation in the volumes read carries a `sources/` document and a line anchor. The
   one attribution gap is §C.1's refuted-narrative column → **M-8**.

## Untestable

STATUS: WRITTEN — with zero web on this pass, the following could be tested neither for nor against:

1. **Quote fidelity of attributed print.** The `Passage:` strings and in-text quotations against the original
   magazine/newspaper/interview print. The corpus itself declares this limit (§15.6 advisory: ~39% unmatched
   attributed quotes corpus-wide because Stage-1 secondary print was never saved under `sources/`), and it is an
   **intake gap, not 179 fabricated citations**. **M-8** is the one site where the *attribution target* (not the
   words) is missing.
2. **Whether the cost of capital fell** (**M-1**). Requires comparable issue pricing (effective yields on a
   zero-coupon senior discount note vs a cash-coupon convertible of different security ranking) or a peer
   issuance of the same week. Neither exists in `sources/`, and §I's provenance boundary says no non-Amazon
   registrant document is present.
3. **Whether "only scale produces" the payables behaviour** (**M-9**). Same limit: no comparator filing in the
   corpus, so the universal cannot be tested either way.
4. **Whether the disclosed risks were or were not experienced** (**H-5**). The internal operating record is
   unrecoverable (§S records it EMPTY, not UNANSWERED); only the disclosure act is evidence.
5. **Whether the wording change in §M.5 was managed** (**H-2**). No counsel file, no drafting history; the
   audit can only require that motive language be labelled, not settle it.
6. **Whether any 1999 category operated at scale.** The volumes' own answer is UNKNOWN and this audit confirms
   the null rather than testing it: no category revenue line exists for toys, electronics, home improvement,
   video or zShops in any local document (§E.6), and the Forrester/Media Metrix/Relevant Knowledge/Opinion
   Research reports behind §H1–H5 are not in `sources/`.
7. **Whether the ARS shareholder letters reflect deliberation** rather than explanation. §N's limit (i) states
   the problem correctly; nothing retrieved here could settle it.

## Untried

STATUS: WRITTEN — named so the next pass does not re-derive the need. Closed out at budget: this sheet was
written with 43 of 55 permitted tool calls, zero web, zero git, and no file deleted.

1. **`stage_3_claim_records.md` (84,337 words) and `_part_2.md` (14,990) read line by line.** Swept for
   constructions only (they carry 8 coda markers, 41 `(PB)` tags, 20 `KNOWABLE` uses). **Untried test:** for
   every `Class: FOUNDER CLAIM` record, whether the record distinguishes *contemporaneous* from *retrospective
   memory* as §3 requires, and whether any `Source date:` that post-dates its `Date:` by more than ~18 months is
   tagged `RETROSPECTIVE SOURCE`. This is the highest-value remaining hindsight check on the corpus, and it is a
   mechanical-plus-judgment pass a script can pre-select.
2. **§U's 55 conflict blocks, U.114 → U.168 (part_3, ~30k words).** Sampled 3 (U.114/117/151 geometry, the
   `BEST-SUPPORTED INTERPRETATION` lines at l.1013 and l.1244, and the re-key map). **Untried test:** whether
   any `BEST-SUPPORTED INTERPRETATION` resolves a conflict by appeal to what later happened, and whether
   `RESIDUAL UNCERTAINTY` cells are honest rather than deferential.
3. **§K.1–§K.8 money prose** beyond the §K.6/§K.7 UNKNOWN lists, and **§M.6–§M.13** beyond M.13's cross-
   references (the §M layer is the volume's causal spine and 4 of 16 defects sit in it).
4. **§J.3 / §J.6 and §E.1–E.5** (technology spend, endpoint sensitivity, the category ledger rows). §E's coda was
   read and passes; its table rows were not.
5. **§P.2's remaining 18 arithmetic blocks** (3 of 21 recomputed by hand; all footed).
6. **`context_appendices.md`'s per-block codas.** Out of the assigned scope, but RD-034 records that Stage 1's
   five worst causal failures lived in exactly those prose blocks, and this file carries none of Stage 3's §A–§U
   discipline. Recommend a sibling sheet.
7. **A `FETCH REQUEST:` that would actually settle something:** the Forrester and Media Metrix reports behind
   §H1–H2 (and the 60%-brand-recognition survey's instrument), which are the only route to converting
   `NOT KNOWABLE` market size into a dated third-party measurement. Not issued — this pass had zero web budget,
   and the null is a legitimate deliverable (§15.2).
8. **RD-073 / RD-076 / RD-077** carried-in defects named in `stage_3_index.md` — not re-opened.

