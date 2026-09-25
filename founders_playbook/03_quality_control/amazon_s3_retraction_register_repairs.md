# amazon_s3_retraction_register_repairs.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:29:38Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## COR inventory

STATUS: WRITTEN 2026-09-25

Gate logic (`tools/gates.py:420 gate_corrections`): a `COR-nn` passes the **registers** check only if the
literal string `COR-nn` appears in one of the nine root CSVs, and passes the **volumes** check only if it
appears in a `stage_*.md`. Before this pass: register layer reached 15/26 (COR-01..15 only); volumes reached
23/26 (missing COR-21, COR-25, COR-26). The 11 unpropagated ids are the whole Stage-3 hindsight-repair wave
(COR-16..COR-26). Propagation below is semantic, not a bare tag drop: each target row keeps the withdrawn
reading inside retraction language and carries the corrected class/confidence.

### COR-16 .. COR-26 -> register row (what carries the withdrawn claim, and where)

| COR | withdrawn reading (prose site) | register row that teaches it | action |
|---|---|---|---|
| 16 | §O.1/§M.13 strike "never entered the money on any 1999 range" (part_2) | `quantitative.csv` L265 conversion price 156.055 (the §K.4 DERIVED `156.055÷2=78.0275` home) | tag + note: strike was in-the-money every 1999 quarter; only the $117.04 issuer-redemption gate was never met; no number back-solved |
| 17 | "softened admission ... before it could be read against the charge"; G31 "printed weaker each time" (part_1 §G.5/part_2 §M.5) | `failures.csv` L53 "no previous experience operating automated DCs" | tag + note: restated as 'limited experience', not softened; motive = RETROSPECTIVE INTERPRETATION / mechanism UNKNOWN / Conf Low |
| 18 | §C.2 closing: risk factors = "self-description of a company ... unsure of the machine ... legally exposed" (part_1) | `conflicts.csv` L104 (U.104 filings disclose each dependency) | tag + note: confined to CONTEMPORANEOUS OBSERVATION "registrant disclosed X"; UNKNOWN whether any disclosed risk was experienced |
| 19 | §M.3 "denominator pulled up ... money moved out of advertising into fulfilment" (part_2) | `quantitative.csv` L332 fulfillment cost relative to advertising 1.337 | tag + note: transfer mechanism withdrawn; all three grew (adv 2.34x, ful 3.75x, sales 2.7x); per-order basis forbidden |
| 20 | §L "covenant's removal came from bondholders"; "1998 bull bid for convertibles" (part_2) | `decisions.csv` L27 ($75m secured facility / covenant) | tag + note: covenant ended by REPAYMENT (10-Q Q1-1998; 424B2), not bondholders; 1998 notes were NON-convertible senior discount notes; escape-covenant motive kept as inference @Medium |
| 21 | §D.0 magnitude cell "no day, no amount in that sentence" (part_1) | `quantitative.csv` L393 charge ~39000 / L394 ratios 13.4% & 2.4% | tag + note: MD&A amount $39m IS filed (10-K FY1999); cell confined to "in that sentence"; UNKNOWN stays for the day & category split |
| 22 | §D.0 "$1.25bn converts ... hardest external demand-side signal" (part_1) | `validation.csv` L57 ($1.25B converts closed, capital markets validated) | tag + note: label corrected to external CAPITAL-SUPPLY / price signal; not a customer-demand signal (§H.3) |
| 23 | §D.3 "cost of capital fell, not the cost of doing business" (part_1) | `quantitative.csv` L261 gross proceeds 326,000,000 (1998 notes home) | tag + note: conclusion downgraded to INFERENCE Conf Low; cost of capital UNKNOWN as a measured quantity; no yield computed (option-value assumption not on disk) |
| 24 | §L 1999-02-03 splits "the cheapest available signal of expected appreciation" (part_2) | `quantitative.csv` L367 stock splits effected in the window | tag + note: superlative "cheapest available" withdrawn (no minute/board record; alternatives never costed); INFERENCE, Low as validation signal |
| 25 | §M.1 "cost of delivering an ORDER rose 3.24 pp"; §L "quarterly-comparable dollar series" (part_2) | `quantitative.csv` L251 contribution per $1 net sales (per-dollar basis home) + `data_gaps.csv` L62/L86 cost-per-order UNKNOWN | tag + note: basis is fulfilment cost per $1 of NET SALES (188,400/1,639,839 vs 50,300/609,819); series is ANNUAL at 3 filed points, NOT quarterly; per-order reading prohibited |
| 26 | H-4 residue: "$178.4m of cash paid" vs note's "$266m principal = accreted $178.4m; $190.7m remains" (part_2) | `quantitative.csv` L395 FY1999 repurchases of the 10% notes | tag + note: BOTH printings registered; WHICH figure is the cash outlay = UNKNOWN; `530,000-266,000=264,000` vs the $190.7m the note says remains -> left as §U candidate (not back-solved) |

**Volume-only gaps (COR-21, COR-25, COR-26):** their withdrawn text never carried the `COR-nn` string in any
`stage_*.md`; after this pass each id is named in a Stage-3 volume I own at the section the retraction edited.

### D-1 / D-2 / C-1 / sweep — filed components verified against held documents

D-1 (verified in `sources/10-K_FY1998_...txt`): balance-sheet long-term debt **348,077** (l.1977) + long-term
portion of capital-lease obligation **63** (l.1978) = **348,140** = Item 6 / Selected Financial Data (l.1264).
Same mechanism FY1997: **76,521** (l.1977) + **181** (l.1978) = **76,702** (l.1264) — foots twice. Current
portion of long-term debt = **684** (l.1974), a separate line, not inside 348,140. Total incl. current =
348,140 + 684 = **348,824** (part_3 P219). `348,761` in part_2 = 348,077 + 684 (omits the 63, mislabels the
pair "(restated)"); its declared "$621k gap not reconciled" reconciles exactly as **684 - 63 = 621**.

D-2 (verified `sources/10-K_FY1999_...txt`): `part_2` line 75 FY1999 components loss-from-ops (605,755) +
interest income 45,451 + interest expense (84,566) = **(644,870)**, but the filing prints **(643,199)**; the
missing leg is **Other income, net 1,671** (l.2625/l.1751). (605,755)+45,451+(84,566)+1,671 = **(643,199)**.

C-1: `stage_3_part_1.md` L289 grounds the note completion on "indenture dated 1998-05-08 (`424B2` l.1571,
l.264)". Verified: a standalone *indenture document* is NOT in `sources/`; `424B2` **is** held and l.264 does
print "the Indenture, dated May 8, 1998", and l.1571 prints the May 8 closing date — so 424B2 is a valid
carrier. The cleaner held carrier for the completion sentence is **`10-Q Q1-1998` l.495** "On May 8, 1998, the
Company completed an offering of approximately $326 million". Re-pointing to 10-Q Q1-1998 (held, verified).

Sweep `0.194995`: **10 occurrences across the company, 6 of them Stage-3** = quantitative.csv L342,
stage_3_pending_registers.md L61, stage_3_part_3.md L93 & L227, and stage_3_claim_records_part_1b.md L177 &
L484 (the latter two are claim-records = NOT mine -> FOR OWNER). Correct quotient `28813/147758 = 0.1950013`;
the restated `28818/147787 = 0.194935` is a different (correct) basis and stays. Non-Stage-3 hits are all
already retraction markers (CORRECTIONS.md x2, stage_2 files, `_parts/`) -> classify-and-leave.

## D-1 denominator

STATUS: WRITTEN 2026-09-25

**Filed components, grepped from `sources/10-K_FY1998_acc-0000891020-99-000375_filed-1999-03-05.txt`:**
balance-sheet long-term debt **348,077** (l.1977) + long-term portion of capital-lease obligation **63**
(l.1978) = **348,140** = Item 6 / Selected Financial Data (l.1264). Mechanism proved twice by the same
document: FY1997 **76,521** (l.1977) + **181** (l.1978) = **76,702** (l.1264). The **684** at l.1974 is the
*current* portion of long-term debt — a separate line, not inside 348,140.

**Reconciliation equation (no figure back-solved; all four inputs are printed in the held filing):**
`348,077 + 63 = 348,140` (Item 6 long-term) · `348,140 + 684 = 348,824` (long-term incl. current portion).

**defect 1 — `stage_3_part_2.md` §K.1 line 80:** printed `"$348,077k + $684k current = $348,761k"` and
mislabelled the FY1997 pair "(restated)" and declared a `"$621k presentation difference ... recorded not
reconciled"`. Repaired to the filed decomposition above; the 621 gap is shown to be `684 - 63`, i.e. that
subtotal added the current portion while dropping the 63 capital-lease line — a presentation decomposition,
not an unresolved conflict. Withdrawn reading kept in place as a retraction.

**defect 2 — `stage_3_part_3.md` P219 / U.131 (lines 125, 1002-1013):** already totalled 348,824 incl. the
684 current portion, which is correct; the composition (348,077 + 63) is now stated and the residual note
that had suggested capital leases might be *outside* the figure is corrected — the 63 is exactly what Item 6
adds to the balance-sheet line, and the FY1999 supplemental 25,850 is a later-year lease disclosure, not the
1998 capital-lease leg. 348,824 (part_3) vs 348,761 (old part_2) = 63, the capital-lease line.

**register rows:** `quantitative.csv` L361 (1998-12-31 balance-sheet multi-metric row) — composition written
into notes; `conflicts.csv` P-U.131 row — `residual_uncertainty` now carries the full `348077+63=348140` /
`684-63=621` reconciliation and reclassifies the "gap" as reconciled. `U.170` (349 vs 291 senior-indebtedness
across years) left standing — it is a genuine year-to-year conflict, not the 1998 denominator defect.

## D-2 FY1999

STATUS: WRITTEN 2026-09-25

**defect — `stage_3_part_2.md` line 75 FY1999 reprint block:** itemised `loss from operations (605,755) +
interest income 45,451 + interest expense (84,566)` and jumped to `loss before equity in losses of investees
(643,199)` — omitting the filed **Other income, net 1,671**. The itemised legs therefore summed to **(644,870)**
against the printed **(643,199)**, a 1,671 shortfall.

**Repair + arithmetic shown in place:** inserted `other income, net 1,671 / — / —` (10-K FY1999 l.2625 /
l.1751) and the identity `(605,755) + 45,451 − 84,566 + 1,671 = (643,199)`.

**register row:** `quantitative.csv` L372 (FY1999 loss/net-loss/LPS/shares) had bundled the non-operating legs
as `-37444`; its `derived_arithmetic` now decomposes `37444 = 45,451 − 84,566 + 1,671` so the omitted leg is
visible in the register. (The other FY1999 rows L368-372 already foot; no value altered.)

## C-1 carrier

STATUS: WRITTEN 2026-09-25

**defect — `stage_3_part_1.md` line 289 (§K.1 raise row):** grounded the note completion on `indenture dated
1998-05-08 (424B2 l.1571, l.264)`, and `quantitative.csv` L261 carried the same bare `indenture l.264`. A
standalone *indenture* document is **not** in `sources/` (verified: `ls sources/ | grep -i indent` returns
none), so "indenture" as a label names an unverifiable carrier.

**Held carriers, each grepped:**
- `sources/10-Q_Q1-1998_acc-0000891020-98-000846_filed-1998-05-15.txt` **l.495** = "On May 8, 1998, the
  Company **completed** an offering of approximately $326 million" — the completion sentence. (Also l.924,
  l.1246 "$530 million aggregate principal amount".)
- `sources/424B2_final-prospectus_..._filed-1998-08-13.txt` (a held document) **l.264** = "the terms of the
  **Indenture, dated May 8, 1998**" and **l.1571** = "issued and sold by the Company on May 8, 1998 (the
  'Closing Date')" — so 424B2 legitimately carries the instrument/closing date, but only 10-Q Q1-1998 l.495
  carries the *completion of the offering*.

**Action taken (not UNANSWERED):** the date IS in held documents, so no FETCH REQUEST is required. Re-pointed
both the volume line 289 and the quantitative L261 note to **`10-Q Q1-1998` l.495** as the completion carrier,
with 424B2 retained for the instrument date and an explicit marker that the indenture itself is not on disk.
No unverifiable carrier is left standing.

## 0.194995 sweep

STATUS: WRITTEN 2026-09-25

Correct quotient `28813 / 147758 = 0.1950013` (→ 19.50013%); restated basis `28818 / 147787 = 0.194935` is a
different, correct figure and stays. **Total `0.194995` occurrences across the company: 10; Stage-3 sites: 6.**

| # | location | class | action |
|---|---|---|---|
| 1 | `quantitative.csv` L342 (stage3 gross-margin row) | **stale** | fixed to 0.1950013, withdrawn reading kept as retraction (mine) |
| 2 | `stage_3_pending_registers.md` L61 | **stale** | fixed to 0.1950013 + retraction (mine) |
| 3 | `stage_3_part_3.md` L93 (§P188) | **stale** | fixed to 19.50013% + supersession note (mine) |
| 4 | `stage_3_part_3.md` L227 (§P.2 t1) | **stale** | fixed to 0.1950013 + retraction (mine) |
| 5 | `stage_3_claim_records_part_1b.md` L177 (P95) | **stale — NOT mine** | report to claim-record owner |
| 6 | `stage_3_claim_records_part_1b.md` L484 (P179) | **stale — NOT mine** | report to claim-record owner |
| — | `CORRECTIONS.md` L348, L528 | retraction marker | leave |
| — | `stage_2_part_2.md` L530/L716, `stage_2_part_3.md` L515, `stage_2_claim_records.md` L625, `stage_2_claim_records_part_2.md` L66 | quoted retraction (already repaired AUDIT-3 D-06) | leave (not mine) |
| — | `_parts/s2_p4.md`, `_parts/s3_p4.md` (SUPERSEDED banners / pre-merge trail) | retraction / superseded intermediate | leave (not mine, gated-out) |

Tally: 6 Stage-3 sites; **4 fixed** (quantitative L342, pending_registers L61, part_3 L93 & L227); **2 left for
the claim-record owner** (P95, P179 — `stage_3_claim_records*` are out of scope). The correct value 0.1950013
now appears in every register/volume row I own.

## Register edits

STATUS: WRITTEN 2026-09-25

Rows edited (nine-register layer), each referencing its `COR-nn` / repair id and keeping the withdrawn reading
visible as a retraction:

| COR | file | row | corrected class / conf |
|---|---|---|---|
| 16 | quantitative.csv | L265 (conversion price 156.055) | note: strike 78.0275 in-the-money; only 117.04 gate unmet; no number substituted |
| 17 | failures.csv | L53 (no previous experience, automated DCs) | FACT kept; motive → RETROSPECTIVE INTERPRETATION / Low / mechanism UNKNOWN |
| 18 | conflicts.csv | L107 U.104 (risk-factor disclosures) | → CONTEMPORANEOUS OBSERVATION; UNKNOWN whether any disclosed risk experienced |
| 19 | quantitative.csv | L332 (fulfilment/advertising 1.337) | transfer mechanism withdrawn; relative-growth at High; per-order basis UNKNOWN |
| 20 | decisions.csv | L27 ($75m secured facility / covenant) | bondholder/convertibles reading withdrawn; escape-covenant kept as inference @Medium |
| 21 | quantitative.csv | L393 & L394 (charge ~39000; ratios 13.4%/2.4%) | "no amount" cell superseded; day/split/causation stay UNKNOWN |
| 22 | validation.csv | L57 ($1.25bn converts closed) | label → external capital-supply / price signal, not demand-side |
| 23 | quantitative.csv | L261 (1998 notes gross 326,000,000) | cost-of-capital → INFERENCE / Low; cost of capital UNKNOWN as measured quantity |
| 24 | quantitative.csv | L367 (stock splits in window) | "cheapest available" withdrawn; INFERENCE, Low as validation signal |
| 25 | quantitative.csv L251 + data_gaps.csv L62 | per-dollar-of-net-sales basis / per-order UNKNOWN | per-order + "quarterly-comparable" superseded; annual, 3 points only |
| 26 | quantitative.csv | L395 (1999 repurchase 266000/accreted 178400) | dual printing registered; which-is-cash UNKNOWN; 264000-vs-190700 → §U candidate |

Numbers rows touched outside the COR list: **D-1** quantitative L361 + conflicts P-U.131; **D-2** quantitative
L372; **C-1** quantitative L261; **sweep** quantitative L342. Volume edits: part_1 (§D.0 COR-21, §K.1 D-1 line
80→ actually part_2, C-1 line 289), part_2 (D-1 line 80, D-2 line 75, COR-25 line 377, COR-26 line 194), part_3
(sweep L93/L227, P219/U.131 D-1 composition), pending_registers L61 (sweep). Sources.csv, timeline.csv,
channels.csv NOT modified.

## Gate before and after

STATUS: WRITTEN 2026-09-25

**BEFORE — `--checks corrections`: Findings 2.** registers reached 15/26 (COR-16..26 absent); volumes 23/26
(COR-21, COR-25, COR-26 absent). Before full `csv,keys,anchors,budget,corrections`: csv/keys/anchors/budget all
green (9 registers, widths 11/12/15/18/8/11/11/15/11; anchors parity 183↔183; budgets all under cap).

**AFTER — `--checks corrections`: Findings 0.** "all 26 retraction(s) reach registers and volumes"; register
layer 26/26, volumes 26/26.

**AFTER — `--checks csv,keys,anchors,budget,corrections`: Findings 1.** csv 14/14 pass (no width drift from
any register edit), anchors parity holds, budget holds, corrections 0. The one finding is a pre-existing
`keys` defect unrelated to this pass — see next section.

## Left for adjudication

STATUS: WRITTEN 2026-09-25

1. **Pre-existing `keys` finding — `S3007` in `stage_3_claim_records_part_1b.md` L648 (record S52).** S3007 is
   not a source_id in sources.csv (grep count 0) and sits inside a "held for width / merge-refused" record.
   The claim-records file's mtime (00:45) and sources.csv's mtime (01:26) both pre-date this session, so the
   finding is **not introduced here**; it is byte-invariant across my edits. Clearing it would require either
   editing `stage_3_claim_records*` (out of scope) or minting S3007 into sources.csv (an invented carrier) —
   both forbidden. **>>> FOR MERGE / FOR OWNER <<<** leave `stage_3_claim_records_part_1b.md` (and
   `stage_3_claim_records.md`, `stage_3_claim_records_part_2.md`): the 2 stale `0.194995` sites there (P95
   L177, P179 L484) need the same `0.1950013` fix applied to the claim-record layer.

2. **D-1 S-3 "$349 million" summary composition.** Registered (U.131), not resolved: no document footnotes
   whether the S-3 senior-indebtedness line also carries the 63 capital lease or only the 348,077; the
   rounding to $349M is consistent either way. No back-solve performed.

3. **COR-26 $178.4m identity + the 264000-vs-190700 residue.** Deliberately left UNKNOWN / §U candidate for
   the certifier; the reconciling items (conversions, exchanges) are not in the lines read. Not forced.

4. **No `COR-nn` was propagated by inventing a register row.** Every Stage-3 id 16-26 was attached to a row
   that already carried the withdrawn content (or its corrected counterpart); none required a fabricated
   carrier. Where the withdrawn reading was prose-only *and* had a correct register counterpart already (e.g.
   COR-16/17/18/19/20/22/23/24), the tag was placed on that counterpart with the retraction text, satisfying
   §14 rule 10 without laundering.

