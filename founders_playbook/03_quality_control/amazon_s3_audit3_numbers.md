# amazon_s3_audit3_numbers.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T20:09:17Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

STATUS: WRITTEN 2026-09-25

**PASS-WITH-DEFECTS. High-severity count = 1** (D-1, the FY1998 long-term-debt denominator family),
**Medium = 2** (C-1 unresolvable carrier pointer to a document not held; D-2 the $1,671k broken
income-statement chain), **Low / advisory = 4** (P-1 bare `U.D` pointer, L-1 `(PB)`-unlabelled FY1999
lease datum on a 1998 item, A-1 ratio-with-no-denominator, A-2 working-capital bridge term labels).

Both headline defects named in my brief were found **already repaired on the current volumes and the
repairs hold under independent grepping**: the `$349m` carrier (AD-01) and the `$326m` gross/net/face
set (U.169, AD-13). I did not re-report them; I re-tested them and they pass (§Sampled figures).

**The numeric layer's remaining damage is not a wrong number — it is a caption mislabel that three
volumes inherit.** Item 6's `Long-term debt 348,140` is not a restatement of the balance sheet's
`348,077`; it is `348,077` **plus** the `63` long-term capital-lease line printed two lines below it
(`10-K_FY1998` l.1977-1978), proved in the second year of the same table: `76,521 + 181 = 76,702`.
`stage_3_part_2.md` nonetheless prints that pair as "as filed / **restated**" and prints a **different
total** (`348,761`) from `stage_3_part_3.md` P219 and **U.131** (`348,824`) — a silent $63k divergence —
and then declares the resulting $621k gap "recorded **not reconciled**" when it reconciles to the
dollar as `684 − 63`. A restatement that does not exist, a conflict register missing the caption that
is actually on the page, and a reconciliation abandoned one line short of finishing.

### Mechanical gates (quoted, not re-derived)

`python tools/gates.py --company-dir "founders_playbook/01_companies/company_001_amazon" --checks csv,keys,anchors,budget`
→ `Findings: **6** | Passes: 42`, `- coverage 9 registers, 17 stage volumes, 101 source documents`:

| gate | subject | finding |
|---|---|---|
| keys | stage_3_claim_records_part_1b.md | unresolvable source tokens: S3007 |
| keys | stage_3_part_2.md | unresolvable source tokens: S3001, S3012, S3013, S3020 |
| keys | stage_3_part_3.md | unresolvable source tokens: S3007 |
| keys | stage_3_pending_registers.md | unresolvable source tokens: S3001, S3004, S3022, S3024 |
| anchors | narrative | anchor with no register row: U.220 |
| anchors | registers | register row citing an anchor absent from the narrative: U.201, U.202, U.203, U.204, U.205, U.206, U.207, U.208, U.209, U.210, U.211 |

`python tools/gates.py --self-test` → `anchor with no register row [anchors] CAUGHT`,
`correctly escaped doublequote must stay clean [neg] STAYS CLEAN`, `dangling source_id [csv] CAUGHT`,
`duplicate record id [csv] CAUGHT`, `numeric stage vocabulary [csv] CAUGHT`,
`paraphrase presented as quote [quotes] CAUGHT`, `row with wrong column count [csv] CAUGHT`,
`unquoted comma shifts fields [csv] CAUGHT`, `unresolvable source token in narrative [keys] CAUGHT`,
`clean fixture CLEAN`, `self-test: PASS`.

**Gate findings I treat as certification blockers:** the 4 unresolved tokens in `stage_3_part_2.md`
(that is the volume carrying D-1 and D-2, so its citations must resolve before it can be certified) and
`anchors / narrative: anchor with no register row: U.220` (a conflict asserted in the narrative and not
registered). Everything else in the 6 — the retired-key *mentions* inside collision/re-key prose, the
hyphenated dossier-local keys (`S2D-05`, `S3P-002` …), and the U.201–U.211 register-side parity set — is
protected history or the concurrent §U pass's declared work, and I leave it alone.

**Concurrency note (per brief):** all cites below are by stable label (U.nnn, Pnnn, §Pnnn, record key,
claim id), never by row or line number. Counts observed: `quantitative.csv` 395 rows / 202 `stage3` at
mtime **2026-09-26T01:32:51**, `conflicts.csv` at **01:33:09**, `stage_3_part_2.md` at **01:34:57**,
`stage_3_part_3.md` at **01:29:35**, `stage_3_part_1.md` at **01:20:58** — the registers and `_part_3`
were live while I worked, so a count above may already be stale. `ls sources/` returned **99 entries**
(98 files + `s1_graphics/`) against the gate's "101 source documents"; I did not reconcile that by hand
because reconciling it is the gate's job, not mine, and I record the difference instead.

## Carrier failures

STATUS: WRITTEN 2026-09-25

**C-1 — MEDIUM — a day-precise completion date carried by a pointer to a document the archive does not
hold.** `stage_3_part_1.md`, the row headed "**~$326m of 10% Senior Discount Notes** — gross proceeds at
issuance…" (the same row that carries U.169): the cell asserts the raise
> `**completed 1998-05-08** (indenture l.264; "In May 1998 … completed", 10-K l.1676)`

What the corpus actually holds: **no indenture document exists under `sources/`** (`ls sources/` → no
`*indenture*`, no `*ex99*`, no `*exhibit*` file; the FY1998 10-K carries only the *index entry*
"4.1 Indenture, dated as of May 8, 1998, between Amazon.com, Inc." at `10-K_FY1998` l.3417 and l.3640).
The pointer `l.264` resolves to a **blank line** in the document a reader would guess
(`10-Q_Q1-1998`). So the citation as written cannot be checked by anyone holding this archive, and the
exhibit it names is missing from `sources/` — which my brief makes a finding in its own right.

**The number is not fabricated**, and that is why this is Medium, not High: `10-Q_Q1-1998` **l.495** and
**l.924** both print `On May 8, 1998, the Company completed an offering of approximately $326 million`.
The right number is in the corpus with the wrong pointer on it.

*Remedy (for the repairer, not me):* re-point to `10-Q_Q1-1998` l.495, keep the 10-K l.1676 month-level
citation as the same-lineage echo it is, and open a `data_gaps.csv` row for Ex-4.1 (indenture dated
1998-05-08) with `follow_up_task` set — the exhibit is referenced by two held 10-Ks and is unfetched.

**C-2 — LOW (pointer hygiene) — `stage_3_part_2.md`**, the row headed **"The obligation, and what
'interest expense' meant in 1998"**, cites its own $621k debt item to
> `(→ **U.D** marker, §K.8)`

`grep -o "U\.D[^0-9*]" stage_3_part_2.md` → 3 bare `U.D` strings, none numbered. In `stage_3_part_3.md`
the dossier-local conflict series `U.D1…U.D8` is a *tech/ops* block mapped to `P-U.145`–`P-U.152`
(`| P-U.145 | **U.145** | U.D1 | ST3_D_tech_ops.md |`), so `U.D` alone names no conflict, and the
substantive carrier for this item is **U.131** — which states the pair differently (see D-1). Remedy:
point at `U.131` and, if the §U pass renumbers, re-key per §14 rule 12.

**Carrier tests that PASSED this pass** (recorded so the next auditor does not re-spend budget):
see §Sampled figures. Most importantly the run's most expensive defect class was checked head-on and is
now clean — `$349m` **does** live in exactly one held document. `grep -c "349"` on `10-K_FY1998` = **0**;
`grep -rl "349 million|$349|349,000" sources/` returns **only**
`S-3_FileNo-333-74435_acc-0000891020-99-000441_filed-1999-03-16.txt`, at **l.915** and **l.1325**, both
printing `As of December 31, 1998, we had approximately $349 million of` — which is precisely what the
AD-01 cell (row "**Debt overhang at the fiscal floor**", `stage_3_part_1.md`) and **U.170** assert. The correction's own three
pointers to the 10-K (`l.1676 / l.2436 / l.2761` for "approximately $326 million") are **exact**: those
are the only three lines in `10-K_FY1998` matching `326 million`. A repaired carrier that would have
failed a less careful audit.

## Denominator failures

STATUS: WRITTEN 2026-09-25

**D-1 — HIGH — the FY1998 long-term-debt family: one caption mislabelled as a restatement, two
different stage totals, and a reconciliation abandoned $63k short of finishing.**

What the held document prints (`sources/10-K_FY1998_acc-0000891020-99-000375_filed-1999-03-05.txt`,
occurrence counts grepped this pass: `348,077`=1, `348,140`=2, `348,761`=**0**, `348,824`=**0**):

```
l.1264  (Item 6, Selected Financial Data)  Long-term debt.....................  348,140   76,702  --  --  --
l.1974  (balance sheet)                    Current portion of long-term debt ..     684    1,500
l.1977  (balance sheet)                    Long-term debt..................... 348,077   76,521
l.1978  (balance sheet)                    Long-term portion of capital lease .     63      181
```

The identities are exact and they close in **both** columns: `348,077 + 63 = 348,140` and
`76,521 + 181 = 76,702`. Item 6's "Long-term debt" line is therefore **long-term debt plus the
long-term capital-lease portion** — not a different vintage, not a rounding, not a restatement. Four
consequences, each traceable to a labelled row:

1. **A fabricated restatement pair.** The row headed "The obligation, and what 'interest expense' meant
   in 1998" in `stage_3_part_2.md` prints `Long-term debt **$76,521k (FY1997 as filed) / $76,702k
   (restated)**`. Both numbers are in the **same** FY1998 10-K, on adjacent lines, on different
   captions. Labelling `76,702` "restated" asserts a re-audit that never happened and, under the
   restated-vs-contemporary rule, poisons the row's whole evidentiary grammar: a reader is told a later
   document corrected an earlier one when the earlier document already carried both.
2. **Two totals for one date, $63k apart, in two volumes.** Same part_2 row:
   `**$348,077k + $684k current = $348,761k (FY1998)**`. `stage_3_part_3.md` **P219** ("Long-term debt,
   three ways") and **U.131**: `**348,824** including the **684** current portion`. Neither total is in
   the filing; both are derived; they differ by exactly the `63` lease line; neither volume names it.
3. **"Recorded not reconciled" — when it reconciles to the dollar.** The part_2 cell calls the
   `348,140` vs `348,761` gap "a **$621k presentation difference inside one document**, recorded not
   reconciled". `684 − 63 = 621` exactly. The gap is fully explained by the two adjacent balance-sheet
   lines the same cell cites. Declaring it unreconciled converts a solved problem into an open one and
   is the reason the $63k never reached U.131.
4. **U.131's register entry is wrong about its own caption.** Its BEST-SUPPORTED INTERPRETATION says
   "**$348.1M as the long-term-debt line**"; the long-term-debt line is **348,077**, and 348,140 is a
   lease-inclusive summary caption. Its three-way list (348,140 / 348,824 / "$349 million") omits
   348,077 entirely — the only balance-sheet long-term-debt caption in the filing — and its
   WHY- THEY-DIFFER clause hypothesises "a definitional difference" that this pass has now resolved.
   `stage_3_part_1.md`'s AD-01 cell repeats the same mislabel: "the FY1998 10-K's own long-term-debt
   line is **$348,140k**".

**L-1 — LOW, same cluster (post-boundary, unlabelled).** U.131's RESIDUAL UNCERTAINTY asks whether
"$349 million" includes "capital leases, **which appear in the FY1999 supplemental disclosures at
$25,850**" — verified present at `10-K_FY1999` l.2873 (`Fixed assets acquired under capital leases....
$25,850 $ -- $3,463`), i.e. a FY1999 datum, one fiscal year later, used to characterise a 1998-12-31
composition, with no `(PB)` tag. The convention **is** declared and used elsewhere in the volume
(P201/P202 carry `(PB)`), so this is a labelling slip, not a missing rule — and it is only needed at
all because the FY1998 lease line (`63`) was never read.

*Remedy:* amend **U.131** to a four-way conflict naming `348,077` (l.1977), `63` (l.1978), `684`
(l.1974) and `348,140` (l.1264) with the two identities printed as the resolution, and state
`$348,824 = 348,077 + 63 + 684` as the single total the stage uses; delete "(restated)" from the
part_2 pair and relabel it `same-document caption difference (Item 6 includes the long-term capital
lease)`; delete "recorded not reconciled"; align part_2's `348,761` to `348,824` or label it explicitly
"excluding capital leases"; tag the `$25,850` clause `(PB)`. I have not touched any of these files.

**D-2 — MEDIUM — a broken income-statement chain in `stage_3_part_2.md`, FY1999 restated block.** The
cell prints, for FY1999: loss from operations **(605,755)**; interest income **45,451**; interest
expense **(84,566)**; then "loss before equity in losses of investees **(643,199)**"; equity in losses
**(76,769)**; net loss **(719,968)**. Recomputed:
`-605,755 + 45,451 - 84,566 = -644,870`, not `-643,199` — a **$1,671k** hole. The missing component is
filed, two columns of the very document the row cites: `10-K_FY1999` l.2625 and l.1751 print
`Other income, net ............ 1,671  --  --  --  --`. Two aggravators: (a) the FY1998 column in the
same cell foots exactly (`-109,055 + 14,053 - 26,639 = -121,641`) because FY1998 had no other-income
line (the "--" columns), so a reader adding the printed components gets no signal that a line is
missing only in FY1999; (b) the row's tail ties (`-643,199 - 76,769 = -719,968` ✓) and its margin and
growth derivations tie (`290,645 ÷ 1,639,839 = 17.724%` ✓, `1,639,839 ÷ 609,819 = 2.689` ✓), so the
defect is invisible next to the arithmetic that does work. The hole is exactly the omitted filed line,
so this is an incomplete citation rather than a back-solved plug. *Remedy:* insert
`other income, net **1,671**` between interest expense and the sub-total (and note it is the FY1999-only
line), or add the chain as `derived_arithmetic`.

## Arithmetic failures

STATUS: WRITTEN 2026-09-26 (C-1..L-1 settled; D-1/D-2 cross-referenced)

**Register (DERIVED/ESTIMATE rows, `stage3`): recomputed in full, 0 broken identities.** All 38 Stage-3
derived rows carry a populated `derived_arithmetic` (**0** empties — checked with the stdlib `csv`
reader, not a hand-rolled split, per §15.1 and the `doublequote=False` incident; the self-test's
`correctly escaped doublequote must stay clean [neg] STAYS CLEAN` line is the control that makes that
choice right). No Stage-3 row has an empty `value`, `unit`, `source`, `source_date`,
`evidence_class` or `confidence` cell. Spot-verified as exact: `2,100/614 = 3.42` ✓ ·
`31,035 − 78,674 = −47,639` ✓ · `25,561 + 347,884 = 373,445` ✓ · `(133,841 − 60,200)/609,996 = 0.12073`
✓ · `476,155/((8,971+29,501)/2) = 24.75` ✓ · `38,005/159,267 = 23.86%` ✓ · `93,000+200,000+323,000 =
616,000` ✓ · `9,885,000 × 2 × 3 = 59,310,000; − 58,770,000 = 540,000` ✓ · `81,840/201,512 = 0.4061` ✓ ·
`31,739,000/7,600 = 4,176` ✓ · `$188.4m/16.9m = $11.15` ✓ · `163,804/1,639,839 = 9.99%` ✓ ·
`463,026/(1,349,194/365) = 125.26 → 125.2` ✓ · `39,000/290,645 = 13.4%`, `39,000/1,639,839 = 2.38%` ✓ ·
`36,806 − 22,935 = 13,871; 13,871/9,421 = 1.47` ✓ · `3,800,000 + 690,000 = 4,490,000` ✓.

**Tie-outs performed on narrative aggregates (all foot):** FY1999 total operating expenses
`413,150+159,722+70,144+30,618+214,694+8,072 = 896,400` ✓; `290,645 − 896,400 = (605,755)` ✓;
`1,639,839 − 1,349,194 = 290,645` ✓; FY1998 `132,654+46,424+15,618+1,889+42,599+3,535 = 242,719` ✓;
per-share `719,968/326,753 = 2.20` ✓, `124,546/296,344 = 0.42` ✓, `31,020/260,682 = 0.119 → 0.12` ✓;
`530 − 126 = 404` ✓ (Q1-1999 buy-back, `10-Q_Q1-1999` l.438-442 prints all three).

**A-1 — the only two arithmetic failures found are in the narrative, not the register: D-2's silent
$1,671k** (`stage_3_part_2.md` FY1999 block, missing the filed `Other income, net 1,671`) **and D-1's
"not reconciled" $621k**, which is `684 − 63` exactly. Both are stated under §Denominator; both are
small deltas and both are real, which is the point: no aggregate in this stage was found to be plugged,
but two chains are printed as though complete when they are one line short.

**A-2 — LOW / advisory (label, not value).** Two derived rows use a numerator and denominator that are
not the same kind of thing. (i) `stock consideration as share of the debt raise = 66.6% ::
217,241 / 325,987` — an equity consideration divided by a debt-proceeds line; the division is correct
(`0.6664`) but nothing is "of" anything here, so the metric's name promises a share it does not
compute. (ii) The FY1996 working-capital row's bridge `2270-1698=572 against +163 assets and -458
equity = 621, a residual of 49 undisclosed` explains a **working-capital** delta with **total assets**
and **equity**, neither of which is a current asset or current liability. The arithmetic itself is
honest (`163+458 = 621`, `621 − 572 = 49`) and §P.2 **t22** prints the same reasoning and reaches the
correct conclusion — "the working-capital change is **not** fully explained" — so no plug is being
passed off. Remedy: rename (i)'s metric to a "ratio to" form and relabel (ii)'s terms as
total-assets/equity so no reader mistakes the bridge for a current-account decomposition.

## Restated-as-contemporary

**The lineage rules are being honoured where it counts.** `10-K/99` vs `10-K/A/99` sit as **one
instrument in two states** in P244 ("FACT (audited, one instrument two states)", `High → **U.154**`),
and I verified every figure in that cell against the held bytes: `116,962` and `589,226` print **only**
in the original FY1999 10-K (4 and 6 occurrences; **0** in the 10-K/A), `133,309` and `572,879` print
**only** in the 10-K/A (3 and 5; **0** in the original), and the four lines the cell calls "unchanged"
(`273,243`, `2,471,551`, `1,466,338`, `266,278`) appear in **both**. The claimed $16,347 reclass ties
both ways: `133,309 − 116,962 = 16,347` and `589,226 − 572,879 = 16,347` ✓. The four hyphenated
`S-1A-No*` files and their `S-1A_No*` underscore twins are declared byte-identical duplicates with a
"cite the hyphenated form" instruction (part_3 provenance table), and the S-1 + six amendments + 424B1
are named as **one lineage** in that same cell.

**R-1 — MEDIUM (same defect as D-1a, logged separately because it is the class, not the value): the
word "restated" is carrying three different things.** Besides `76,702 (restated)` — a caption
difference inside one 10-K — the §R snapshot row in `stage_3_part_3.md` reads
> `**Start:** Bezos, CEO and Chairman, beneficial owner of ≈**41%** of the post-offering common (restated from 43% on 1997-05-14)`

The pair is **not** averaged, not printed as "~41-43%", and it **is** registered as a version conflict
in `conflicts.csv` ("**43% belongs to the ORIGINAL and the approximately 41% to No. 5: a version
discrepancy between** …", "**S-1/A No. 5 1997-05-14 gives 41%/10% and 47.4%/41.4%. Both pairs are** …"),
and I confirmed the original does print it: `43%` appears **1×** in
`S-1_original_acc-0000891020-97-001309_filed-1997-03-24.txt` and **0×** in each of Nos. 4, 5 and 6. So
the conflict handling is correct; the **snapshot row's verb is not** — an amendment that supersedes a
percentage on a specific date is not a restatement, and "restated" tells a reader an accounting
correction happened. Remedy: "superseded by S-1/A No. 5 (1997-05-14), conflict registered in
conflicts.csv" and name the carrier document in the cell.

**R-2 — tested clean, recorded so it is not re-litigated: the FY1997 as-filed / restated revenue pair
is real.** `147,758` and `28,813` occur **only** in the FY1997 10-K (5× and 3×; **0×** in the FY1998
10-K, FY1999 10-K and S-3 333-74435); `147,787` and `28,818` occur **only** in the later filings
(`28,818`: 3× FY1998, 4× FY1999, **0×** FY1997 10-K). So §P.3 **t5**'s pairing and its "growth 838% /
839%" version pair sit on genuinely different documents, and the two percentages are printed as a pair
rather than averaged — correct under the filing-lineage rule. Same test on `609,996` (5× in FY1998 10-K,
**0×** in FY1999 10-K) vs `609,819` (4× in FY1999, **0×** in FY1998) ✓.

**R-3 — D-2's own dependency.** The `stage_3_part_2.md` FY1999 block is labelled "a second
restatement, and a caption re-cut" and is used to source FY1997/FY1998 comparatives; that is a correct
contemporary-vs-restated framing (and it is where the `214,694` amortization-of-goodwill line first
appears, with `—` for FY1997, which is what a re-cut caption looks like). No defect, but note that its
`Other income, net` omission (D-2) is in the **restated** column only, so a repair that copies the
contemporary FY1999 statement will not fix it by accident.

STATUS: WRITTEN 2026-09-26 (R-1..R-3 above)

## Sampled figures

STATUS: WRITTEN 2026-09-26

Carrier fidelity — **what I actually grepped in the held bytes, and what it printed.** Pointers below
are the *document's own* line numbers, verified as locators only; every finding cites by label.

| figure as the volumes print it | cited carrier | held bytes say | verdict |
|---|---|---|---|
| `$349 million` senior indebtedness at 1998-12-31 | S-3 333-74435 (AD-01 moved it off the FY1998 10-K) | `10-K_FY1998` **0×** `349`; `grep -rl` over all of `sources/` → **only** the S-3, l.915 + l.1325, both "we had approximately $349 million of" | **PASS** — one carrier, corroboration 1, exactly as U.131/U.170 now say |
| `≈$291 million` at 1999-03-31 (U.170 CLAIM B) | `10-Q_Q1-1999` l.1607 | l.1607 prints "`$291 million of outstanding senior indebtedness.  The Indenture does not`" | **PASS** — the $58m unexplained fall is real in the bytes |
| `$326m` gross / `~$315.7m` / `$318.2m` net / `$530m` at maturity | 8-K 1998-05-05 l.118-119 + headline; 424B2 l.1355; FY1998 10-K l.1635; l.1688 | 8-K l.119 "…to approximately $326", l.174 headline "FROM $275 MILLION TO APPROXIMATELY $326 MILLION GROSS PROCEEDS"; `315.7` in 424B2/S-4/S-4A only; `318.2` at FY1998 10-K l.1635; "principal amount at maturity of $530 million" l.1688, "no cash interest … Prior to November 1, 2003" l.1689 | **PASS** — all four denominators present and distinct; the notes' own paragraph carries the $530m, so no instrument-misassignment |
| FY1998 debt captions | `10-K/98` l.1264 / l.1974 / l.1977 / l.1978 | `348,140`=2, `348,077`=1, `684`, `63`, `181`, `76,521`, `76,702` all present; `348,761`=**0**, `348,824`=**0** | **FAIL → D-1** (both totals are derived; the composition was never read) |
| `1,671` other income, FY1999 | cited? **no** | `10-K_FY1999` l.2625 + l.1751 | **FAIL → D-2** (a filed line absent from a row that presents itself as a component list) |
| `275,000,000` announced before the upsize | 8-K event 1998-04-24 | 1× in that 8-K | **PASS** |
| `$2.4 million` / `$75.0 million` in the exchange prospectus | 424B2 l.699/1114/2220, l.1355-1357 | `2.4` 4×, `75.0 million` 3× | **PASS** |
| `254,462` / `1,104,071` net financing; `325,987` / `1,263,639` proceeds | FY1998 / FY1999 10-K | 1× each in the stated year | **PASS** |
| FY1999 balance sheet "two cash bases", 8 figures + 4 "unchanged" | `10-K/99` l.1779-1785; `10-K/A/99` l.221-226 | per-document split exactly as claimed (§Restated-as-contemporary) | **PASS** |
| `9,885,000` shares / `41.3%` | Bezos SC 13G, 1998-02-17 | l.154/165/174/261/267/272 shares; l.182/263 "41.3%" | **PASS** |
| `4,490,000 sq ft` (3.8m US + 690k UK/DE) | FY1999 10-K l.1604, l.1612 | "approximately 3.8 million square feet" l.1605; `690,000` 3×; `4,490` 0× — and the row is classed ESTIMATE/DERIVED with the sum shown | **PASS** (derived, correctly labelled) |
| `36,806` FY / `22,935` 9M D&A | FY1999 10-K l.2820 vs Q3-1999 10-Q l.314 | `36,806` 1× in the 10-K, **0×** in the 10-Q; `22,935` **0×** in the 10-K, 1× in the 10-Q | **PASS** — the subtraction is honestly split across two instruments |
| `9,692 as filed / 9,421 as recast`; `3,388 / 3,442` | FY1998 / FY1999 10-K + 10-K/A | both renderings named per document in the register's own `source` cells | **PASS** — a recut pair kept as a pair |
| `126.0` repurchased / `83.9` accreted / `404` left | Q1-1999 10-Q | l.438-442 print all three; `530 − 126 = 404` ✓ | **PASS** |
| `25,850` capital leases | FY1999 10-K l.2873 | present, FY1999 column | **PASS as a fact; FAIL as a label → L-1** |

Not sampled (out of budget, listed rather than guessed at): the ~45 §P rows in `stage_3_part_3.md`
outside the P201-P262 block I read, the `channels.csv` / `failures.csv` / `validation.csv` magnitude
cells, `stage_3_pending_registers.md`, `context_appendices.md`, and the claim-record volumes beyond
records **A14** and **A26**. Counts here were taken at `stage_3_part_1.md` 01:20:58, `_part_3.md`
01:29:35, `quantitative.csv` 01:32:51, `_part_2.md` 01:34:57 (2026-09-26); the registers and `_part_3`
were being edited while I worked, so any count above may already be stale — that is expected and is not
a reason to re-open a settled finding.

## Sibling sweeps

Swept each load-bearing family across all three narrative volumes + the register + `conflicts.csv`,
looking for a value that changes when it crosses a volume boundary:

1. **The FY1998 debt family — DIVERGES (D-1).** `part_1` AD-01 cell (`348,140` called "the 10-K's own
   long-term-debt line") → `part_2` obligation row (`348,077 + 684 = 348,761`, `76,702 (restated)`,
   `$621k … not reconciled`) → `part_3` **P219** + **U.131** (`348,824`, three ways, `348,077` absent).
   One date, three printed totals (`348,761` / `348,824` / "$349 million"), a $63k reconciling item
   named in **no** volume, and a `(PB)` FY1999 lease figure used in the residual. This is the finding
   the register cannot see, because no register row carries the debt total — the pair lives only in
   prose.
2. **The $326m gross / nets / face family — CONSISTENT.** `part_1` (the Senior Discount Notes row),
   `part_2` ("~$326m gross / ~$315.7m net; principal at maturity $530m"), `part_3` **U.169**, plus the
   §T provenance cell that names "the **$326m gross** of the notes". Every use states which denominator
   it is, both nets are kept as a filed pair rather than averaged, and **U.169**'s own text explains why
   it did not pick one ("carry net proceeds $318.2m" would have replaced one filed figure with
   another). This is the correct handling of the class and I record it as clean.
3. **The FY1997 as-filed / restated revenue pair — CONSISTENT** across §P.3 **t5**, `stage_3_part_2.md`'s
   restated block (`147,787` / `1,639,839 / 609,819 / 147,787`) and the register's margin and growth
   rows (each printing both). The `838% / 839%` version pair is printed as a pair, never averaged.
4. **The interest-expense accretion datum — CONSISTENT and load-bearing.** `part_2` prints
   `(326) → (26,639)` with `23,970` non-cash and `26,639 − 23,970 = 2,669` cash ✓; the `(326)` FY1997
   interest line is the **same digits** as the `$326` million gross-proceeds figure and the `349` case
   in reverse — I checked both, and each is in its own document (`10-K_FY1998` income statement vs
   l.1676/2436/2761 prose), so the coincidence is not a mis-carrier. Flagging it because a
   right-number-wrong-document pair is one careless copy away.
5. **The `(PB)` convention — present and used** (`part_3` header " `(PB)` marks material after the
   window", P201/P202 carried from Stage 2's `(PB)` rows, the 2000-03-23 / 2000-09-08 filing-dating
   rows, "Stage 2's `(PB)` row becomes in-window here"). Counts: `(PB)` appears 19× in `part_1`,
   3× in `part_2`, 9× in `part_3` (mtimes as §Sampled). The only unlabelled later-year datum I found is
   L-1.
6. **Not swept (declared):** I did not trace the `$18.00` IPO price, the "87.4% restricted" float
   claim, the S-4 shelf time series `5m → 15m → 30m` (U.116), or the eight S-8 registrations as a
   hiring curve — all are numeric but outside the debt/proceeds/EPS/per-unit scope I was given.

## Not testable

- **The 1998-05-08 indenture itself.** Ex-4.1 ("Indenture, dated as of May 8, 1998") is referenced by
  two held 10-Ks but **its body is not under `sources/`**; `sources.csv` carries 2 rows mentioning an
  indenture. The date survives on `10-Q_Q1-1998` l.495/l.924, so nothing in this stage depends on the
  exhibit — but the note's terms beyond "no cash interest before 2003-11-01", the accretion schedule
  behind the `$530m` face, and any per-note covenant are **UNKNOWN from this archive**, and the
  `indenture l.264` pointer (C-1) cannot be checked at all. **A missing document, reported as such.**
- **What "$349 million of outstanding senior indebtedness" is made of**, and therefore whether the
  1998-12-31 → 1999-03-31 `349 → 291` fall is a carrying-value change, a definitional change or a
  transcription error. The S-3 prints the sentence with no composition footnote (U.131's own phrase:
  "the summary line's composition is **not footnoted**") and the Q1-1999 10-Q prints no reconciliation.
  The honest value is **UNKNOWN**; U.170 is correctly registered and I did **not** propose a substitute
  explanation.
- **Whether the FY1999 `Other income, net 1,671` was itself ever restated.** The 10-K/A holds only the
  balance-sheet reclass (per P244, the four "unchanged" lines tie); no amended income statement is on
  disk, so D-2's fix is a citation fix, not a value dispute.
- **The `13G like-for-like` founder-stake derivation** `9,885,000 × 2 × 3 = 59,310,000; − 58,770,000 =
  540,000`. The arithmetic works and the 9,885,000 / 41.3% inputs are carried (13G l.154-272), but I
  cannot test **which** split(s) the `× 2 × 3` stands for from the held Stage-3 corpus without reading
  the Stage-1/2 split history, which is outside my scope. Classed **not-tested**, not clean.
- **Secondary print for Stage 3.** No Stage-3 newspaper/magazine text is under `sources/`, so any
  Stage-3 quote resting on periodical print is unverifiable here. Per §15.6 that is an **intake gap,
  ADVISORY, not a defect**, and I ran a zero-web pass as instructed, so I did not attempt to close it.
- **UNTRIED at close (budget):** the ~45 unsampled §P rows (§Sampled); `stage_3_pending_registers.md`
  numeric rows; `timeline.csv` / `channels.csv` / `failures.csv` / `validation.csv` magnitude cells;
  the claim-record volumes beyond **A14**/**A26**; `context_appendices.md`; the per-order / per-unit
  economics of the marketplace rows (`1 million registered users`, `1.5 million listings`) — I read the
  filing's own caution that listings "are **not** commutable with the title counts" and stopped there;
  U.116's shelf series; and whether any `stage3` register row double-counts a same-lineage document as
  a second source of corroboration (only the 6 explicit `same lineage` notes were read).

STATUS: Sibling sweeps and Not testable WRITTEN 2026-09-26 (sections above)

