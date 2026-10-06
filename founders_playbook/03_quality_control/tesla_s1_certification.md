# Tesla Stage 1 — certification (`tesla-cert-1`, 2026-10-06)

Independent certifier for `company_043_tesla` Stage 1. §15.6 role separation holds: I am not
`tesla-s1-merge`, not `tesla-s1-audit1`, not `tesla-repair-1`; I edited no corpus file, no register and no
source byte. **Web calls: 0 made, 0 permitted** — every carrier named below is a path under
`founders_playbook/01_companies/company_043_tesla/`. Every figure in this sheet was measured from the bytes,
including the figures I quote from the audit sheet and the repair sheet.

## VERDICT: **CERTIFIED-WITH-NAMED-RESIDUALS**

The five blockers are closed on the bytes, not on their account: the false null is retracted everywhere that
matters, the value is now a row, and no adjudication has to be reopened. What remains is six one-cell repair
items — one of them an instruction-layer stale null (blocker B1\*) and one a withdrawn denominator still
printed in the volume's own tier line (B6\*) — plus named intake debt. **The certification
would flip to NOT-CERTIFIED the moment a Stage-2 pass imports `tesla_s1_merge_notes.md` §7's "UNKNOWN"**, which
is exactly the harm channel this project has paid for three times; that is why B1 is a blocker and not a note.

Gate (my own run, command below): **Findings 2 | Passes 18, tier auto → T3, 0 substantive.**

---

## 1. The five blockers, measured

**B1 (the false null) — CLOSED, verified on bytes.** `sources/sec/0001193125-10-068933_ds1a.htm` (S4370,
Amendment No. 1, 2010-03-29) prints four *distinct* sentences binding $26.0m to 2009-12-31 (contractual
obligations table; "As of December 31, 2009, we had an aggregate of $26.0 million … for the Tesla Roadster and
the Model S"; the current-liability sentence; the Note 4 subscribers sentence) — measured, all four in one body.
`-149105_d424b4.htm` prints the 2008/2009/2010-03-31 triad ("December 31, 2008, 2009 and March 31, 2010" = 24×
in that body). `$24.8 million` = 4× in `ds1.htm` (-017054) and **0× in every other held body** ✓, so the real
conflict is the lineage dropping the 2009-09-30 interim datum, not a missing number.
- `U.23` is now honestly a **period-end pair of one filed series**: `why_they_differ`, `evidence_weight`,
  `best_supported_interpretation`, `residual_uncertainty` and `confidence` all rewritten with the merge wording
  quoted inside a `REPAIR[…]` withdrawal; the only live disagreement left in the row is part 2's cross-date
  supersession, which stays **DECLINED** ✓; residual = the never-filed receipts/refunds flow ✓.
- **COR-01 stays visible as superseded, not erased** ✓: `CORRECTIONS.md` keeps the withdrawn paragraph
  ("the 2009-12-31 value is **UNKNOWN**") printed at lines 40–42 and retracts it beneath, retires its own
  "FETCH REQUEST" label (the route was a local read — §15.1 applied correctly at last), and prints the carrier
  sentence + accession.
- **The new quantitative row landed at the right carrier and basis**: `date 2009-12-31 | refundable reservation
  liability | 26.0 | USD millions | source S4370 | source_date 2010-03-29 | FACT | High`, note quoting the
  carrier; `-068933` is registered as S4370 ✓; the original printing (`-017054`, S4369) prints no $26.0m ✓, so
  2010-03-29 is the right first-printing date. The two 2010-03-31 rows keep their own dates and now carry the
  withdrawal of "stays UNKNOWN at U.23" ✓. `decisions.csv` "Invert the reservation-deposit instrument" is
  re-labelled carried-and-supported with the causal reading explicitly withheld ✓. Anchors unchanged at 23↔23 ✓
  (gate). Registers 208 → **210 rows** (measured: 24/62/46/23/16/9/9/11/10) ✓.

**B2 (Daimler date) — CLOSED.** `validation.csv` now reads `2009-11 | First powertrain shipments to Daimler …`
with recognition split out. Both carrier sentences are in the bytes I opened: "We began shipping the first of
these battery packs and chargers in November 2009…" occurs 86× across 18 held bodies (including `ds1.htm`, so
the row's `source_id` "S4372 (S4369 prints the same sentence)" is true ✓) and "In May 2009, we formalized a
development agreement with Daimler" 16× in 16 bodies ✓. The row was re-dated, not deleted ✓ (RD-122). Volume,
`timeline.csv` and claim record P1-28 now agree.

**B3 (per-share across the split) — CLOSED.** Measured `0.493` = **5× in `ds1.htm`, 5× in `-068933`, 5× in
`-099603`, 0× in `-149105`**, which instead prints "valued at $0.49 per share" and "Series A $ 0.001 $ 0.49
7,213,000 7,213,000 $ 3,556 $ 3,549" ✓ — the audit's and the repair's counts both check out. All three rows are
re-pointed to carriers that print their own inputs, and both bases are stated in the cell.

**B4 (`_MANIFEST.md`) — CLOSED.** Published totals 210 rows / 16,837 w / 128,812 B: I re-added the nine files
and both sums foot exactly (4,261+2,567+2,004+3,402+1,829+951+541+814+468 = 16,837;
33,577+20,945+16,101+24,056+13,063+7,089+4,223+5,990+3,768 = 128,812) ✓. "Intermediates…" and "Open research
debt…" each appear once ✓; the glued gate row is now its own named table with the tool date ✓; the superseded
13,329/111,343 stay quoted so the correction is checkable ✓.

**B5 (central silence) — CLOSED.** `timeline.csv` now reads `2003-08-01 -> 2004-02-29` with the three refuting
rows and the "in July 2003" carrier quoted, and I measured **no register row inside the narrowed window** ✓.
The extension the repairer found is real and is annotated: Volume 1's Boundary prose (line 251) claimed the same
absolute and now carries the withdrawal inline ✓.

## 2. Where the repairer says the auditor was wrong — each judged on the bytes

1. **"in our target market 0×"** — auditor **wrong**, repairer **right, exactly**. Measured **56×** across 16 of
   the 80 held `.htm`/`.txt` bodies (4× per prospectus printing, 2× in the 10-K, 1× per 2011 printing), and a
   context sweep returned **0** occurrences of the phrase in any competition sentence — it is brand-recognition
   language ("the Tesla brand is well recognized in our target market"). `luxury/performance` = **0×** ✓. So
   A5(iii) survives, and survives better than the auditor framed it: the volume's span is a **splice from a
   different sentence**, and the filed sentence ("…competition from existing and future automobile manufacturers
   in the extremely competitive luxury sedan market, including Audi, BMW, Lexus and Mercedes") prints 26× in 13
   bodies. The volume now prints that sentence beside a "NOT A VERBATIM QUOTATION" annotation ✓.
2. **"printed by eight held documents" vs "11 bodies across 8 accessions"** — the auditor's *class* of error is
   real (he counted accessions and called them documents), but the repairer's replacement number is **also short**:
   measured, **15 bodies across 11 accessions** print $26.0m bound to 2009-12-31. The 11/8 pair is exactly the
   **2010 registration lineage**; the three omitted bodies are two unregistered 2011 printings (`-149963`,
   `-157135`: "As of December 31, 2009, 2010 and March 31, 2011, reservation payments in the amount of $26.0
   million…") and — the one that matters — the **registered FY2010 10-K `S4375`**: "As of December 31, 2010 and
   2009, reservation payments in the amount of $30.8 million and $26.0 million, respectively, were recorded as
   current liabilities". A second instrument family corroborates the value and the corpus does not say so.
   See blocker **B2\*** below.
3. **A3's "data_gaps.csv already carries it"** — auditor **wrong**: no pre-repair `data_gaps.csv` row carried the
   near-collapse absence; the `failures.csv` pointer "logged open in data_gaps" was false in its own cell. The
   repairer minted the gap instead of deleting the row ✓ (new High row, `follow_up_task` present → no §13
   research-debt violation ✓) and kept the evidentiary-null label on the failures row ✓.
4. **A8's "0 bytes with no sidecar status"** — auditor **wrong**: `cdx_tesla_com_2008_2011_founderish.json.meta.json`
   exists at **473 B**; what it lacks is `http_status`, which is the actual defect. The repairer's correction is
   right in substance but **its own recount is wrong** (blocker **B3\***): `sources/wayback/` holds **7** entries
   and **2** sidecars, not "8 files … 3 sidecars", and the two 504 bodies are 160 B each, not 153 B.
5. Confirmed as written and acted on: the S4370/424B4 carrier sentences, the 0.493 counts, the 8,000,000 →
   2,666,666 basis, the Daimler May/November pair, the three refuting timeline rows, the `_MANIFEST` mis-sum,
   and the 80-body held denominator ("61 `.htm`, 19 `.txt`, 3 `.pdf`, 85 files incl. `_MANIFEST.csv` and
   `_UNANSWERED.csv`") — I measured 61/19/3 and 83 documents / 32 accessions / **59,881,144 B** ✓ = COR-06.

**Finding about the auditor.** Four of its headline measurements did not survive the bytes; its matcher caveat
(40% false-absent before entity unfolding, 20-character probes matching trivial words) is honest and is the
reason most of its list was right. Its two most consequential claims — the false null and the Daimler date — were
exact.

## 3. The repairer's self-correction ("no sidecar")

No trace of the wrong claim stands in the corpus or in the instruction layer. `grep` across the company
directory: `stage_1.md` 0, `stage_1_index.md` 0, `_MANIFEST.md` 0, registers 1 (`sources.csv` S4390 — and that
occurrence is the self-correction itself: "My first pass of this row said 'no sidecar' - false: the sidecar
exists at 473 B but records no HTTP status"), `CORRECTIONS.md` 0 (COR-07 item 4 prints "1 zero-byte JSON whose
473-byte sidecar records no http_status" ✓). The wrong claim survives only in `tesla_s1_audit1.md` A8 — the
auditor's own work order, whose ledger claim is still open (`done=false`, heartbeat 2026-10-06T11:48Z), which is
why I report it rather than annotate it.

## 4. Residual R1 — my adjudication: **it is a blocker**

`03_quality_control/tesla_s1_merge_notes.md` §7 (lines 161–162) still prints, with no supersession marker:
"**$2009-12-31 is UNKNOWN**, and the 'liability held flat across the deposit-policy inversion' reading is **not
carried as a finding**". Both clauses were retracted by the very repair this file certifies. The repairer's
reason for not touching it was scope ("not my write path"), not ownership: `_OWNER_LEDGER.json` carries **no
entry at all** for that path, so it is unclaimed and the fix is executable by anyone. §14 rule 10 is explicit
that the files a cold reader trusts are the highest-severity home for a stale claim, and this project has
re-imported retracted values from QC sheets before. `_MANIFEST.md` names the hit and hands it to me; a hand-off
is not a repair. → **B1\*** below. The same file also still publishes 53,553 words / 208 rows / offsets 9,746 and
102,736 (§1) and "TRIED — UNANSWERED" family wording that is fine — those are history properly labelled, except
the §7 sentence, which is asserted in the present tense.

## 5. Arithmetic on the face of the records, re-derived by me

- Repair's own finds confirmed: **15,213,000 × $0.493 = $7,500,009** (cell printed $7,499,999 — a $10 keying
  error) and **× $0.49 = $7,454,370**; **8,000,000 × $0.493 = $3,944,000** → residual **$8,000**; **8,000,000 ×
  $0.49 = $3,920,000** → residual **$16,000**; recorded $3,936k identical in both printings ✓, so the residual
  moves only with the printed price. The two per-share residuals genuinely differ by carrier basis and both are
  now stated ✓.
- Split basis: **8,000,000 → 2,666,666** (1-for-3, May 2010, `U.13`) — measured 18× across 9 bodies, every
  post-split printing; the preferred-side counts (7,213,000 / 8,000,000) are unadjusted by design ✓; and the
  intra-carrier inconsistency the repairer volunteered ("1 for 1 basis" prose beside 8,000,000→2,666,666 notes in
  the same 424B4) is real and registered ✓.
- Whole-register sweep: 19 machine-checkable identities in `quantitative.csv`; **all correct**. Five looked like
  failures only because my parser dropped parenthesised negatives and thousands units — re-read by hand:
  (2046)+2101+7699+1781 = 9535 ✓; 160+154+96+103+45+88 = 646 ✓; 82.4+49.4−54.8 = 77.0 and 99.4−77.0 = 22.4 ✓;
  8,000,000 × $0.493 = $3,944**k** ✓.
- Independent spot-checks, all ✓: 2,941,176 × $17.00 = **49,999,992** (and the 424B4's rounded "$50.0 million of
  our common stock" prints 4× per 2010 body; the exact figure prints 1× each in `-149963` txt+htm and `-157135`
  — the cell now states rounded-vs-exact and names the unregistered carrier ✓); 13,300,000 = 11,880,600+1,419,400
  ✓; 11,880,600 × $15.895 = 188,842,137 ✓; 1,419,400 × $15.895 = 22,561,363 ✓; 13,300,000 × 1.105 = 14,696,500 ✓;
  12,881/93,358 = 13.8% and 80,477+12,881 = 93,358 ✓; 9,535/111,943 = 8.52% ✓; 1,275+4,341+2,030+506 = 8,152 ✓;
  6.3+19.7 = 26.0 ✓; 45,419−29,920 = 15,499 ✓; 107,487−7,487 = 100,000 ✓; 1,063−937 = 126 ✓; 8,284+2,135+86+8+7
  = 10,520 ✓; 249+2,443 = 2,692 ✓; 45.4/465.0 = 9.8% ✓; (18,585−45,527)/45,527 = −59.2% ✓; 14,742−3,458 = 11,284 ✓;
  20,585+227 = 20,812 ✓; 11,475+523 = 11,998 ✓; 160+154+96+103+45+88 = 646 ✓.
- DOE committed/drawn kept distinct ✓; deliveries-vs-recognition now separated in every row I opened ✓; the
  `failures.csv` ten → **thirteen** months / `2008-02 -> 2009-03` fix matches Volume 2 §O.2(a) ✓.

## 6. Nulls and families

| family | state as printed | my measurement |
|---|---|---|
| (a) filings | TRIED — ANSWERED | ✓ 83 docs / 32 accessions / 59,881,144 B held; XBRL 336 rows; index 1,750 rows / 269 in-window |
| (b) web archives | TRIED — UNANSWERED | ✓ label correct (3 negative bodies: 2× 504 HTML at 160 B + 11,832 B IA "Temporarily Offline"; 1 zero-byte JSON; 1 answering CDX surviving only as transcript → `S4390` title now says exactly that ✓; `U.4` stays a LEAD ✓). **Not UNTRIED — but a scripted route now exists and was never run here**: `tools/cdx_intake.py` (family-(b) intake, ships ANSWERED/NULL/UNANSWERED/UNTRIED states) has produced `sources/web_archive/` for other companies (e.g. `company_010_cencora`) and **tesla has no such directory and no entry in `tools/web_domains.json` (5 slugs)**. The live chain still points the open route at a hand CDX URL (`stage_1.md` U-1, `data_gaps.csv` follow_up_task "via the CDX route at FRA-1", `_MANIFEST.md` open debt, merge notes FR-3, audit FRA-1 "harvest_mine.py"), and the two held wayback sidecars assert "(no scripted route exists for the web-archive family)" — true in 2026-09, false today, and those bytes are protected. → **B4\*** |
| (c) periodicals | TRIED at metadata / page text UNTRIED | ✓ 9 harvest bodies measured (IA 3, GB 2, CA 1, HT 1, corp-print 2); CA 5,896 B and HT 6,113 B are 403 challenges → UNANSWERED not null ✓; IA numFound 0/0/6 with six items 2015–2018 ✓; Google Books 10 records per feed from a 300-total set = first-page statement, and the register says so ✓ |
| (d) corporate print | TRIED at metadata / items UNTRIED | ✓ numFound 2 (`tesla-logo` 2003-07-01 — correctly refused as a date carrier; `teslaroadster0000maur` 2008), creator-scoped 0, neither opened |
| (e) auction / museum | UNTRIED entirely, never a null | ✓ and "no scripted route in `tools/`" is **still true** — no auction/manuscript tool exists; this is the one family whose untriedness no script can cure |
| legal (extra) | federal ANSWERED / state UNTRIED | ✓ 2 CourtListener bodies with sidecars; California Superior Court out of scope, silence ≠ absence |

No dead route is written as UNTRIED and no UNTRIED family is written as a null. `## Untried` is carried twice
(part 2's NEW-1…NEW-11 inside Volume 2, probe U-1…U-8 + the family table at the foot) ✓; `S4392` is a proper
UNTRIED row with `url = UNTRIED` ✓; §K.1's four-state vocabulary (EMPTY / UNANSWERED / UNTRIED / NOT KNOWABLE)
is stated and used consistently, and `gaps: 16 rows` every High row carries a `follow_up_task` ✓.

## 7. Boundary, dates, hindsight, tier

- **Dates**: every date I re-tested has a carrier that prints it (list in §5 and §1). The changed cells are the
  best-carriered rows in the corpus. No table row I opened rests on an inference printed as a date.
- **Codas** (§7/§16 duty): 17 `mechanism`, 22 `alternative`, 13 `EVIDENCE`, 14 `CONFIDENCE` occurrences in
  `stage_1.md`, and **6 explicit "mechanism UNKNOWN"** where no flow data is filed — including the U.23 residual
  and the deposit-policy decision, so the carried-and-supported equality is not smuggled into a cause ✓. §L.1
  runs the anti-hagiography test on all four temptations and names what a failure narrative would keep (the
  1,419,400 selling-stockholder shares the issuer does not receive) ✓; §L.3 refuses to read 2008 survival as
  resilience ✓; §O.3 grades every closeness measure `CLASS RETROSPECTIVE INTERPRETATION`, confidence
  Low-to-UNKNOWN, no carrier, and records that "`going concern` and `substantial doubt` return 0 occurrences"
  is itself a datum that does not license "it was safe" ✓.
- **One standing §13 violation, unfixed**: `decisions.csv` row 1 (`2010-06-08 | Correct the FY2009
  stock-compensation error prospectively`) has `actual_result` = "…the uncorrected $(55740)k comparative **later
  printed in the 10-K**" — a post-stage outcome with no `RETROSPECTIVE` label. The auditor saw it and graded it
  advisory; `RETROSPECTIVE` occurs **0× in `decisions.csv`** (8× in the volume), so §13's "only when labeled"
  condition is not met. → **B5\***.
- **Tier**: T3 is measured, not asserted. `research/A_chronology_feasibility.md` fixes it on families returning
  **in-window** Tier-1 text (exactly one: filings) against this stage's own window (2003→2010-06-29), and
  `research/A3_intake_regrade.md` re-issues T3 unchanged because the intake grew family (a) ~10× in bytes and
  added the 336-row XBRL series without adding a family — §15.2 counts families, not prose ✓. `gates.py --tier
  auto` resolves T3 from the stated-verdict line, which is the tier the merge used ✓. The 54,903-word overage
  against the 8,000 density target is advisory under §15.4/RD-122 and the volume is under the 60,000 hard cap, so
  no §9.3 split ✓. **B4\*** is the only item that could move the tier, and only if the route runs and answers.

## 8. Gate run (my command, my bytes)

`python tools/gates.py --company-dir founders_playbook/01_companies/company_043_tesla --tier auto --out
founders_playbook/03_quality_control/tesla_s1_gates_cert1.md` → **Findings: 2 | Passes: 18**, `corrections | 7
retraction ids; register layer reaches 7, volumes 7`, `anchors | parity | 23 ↔ 23`, all nine `csv` width checks
pass, `source_id` resolution passes, findings = the T3 word advisory and `quotes | ADVISORY | 16 of 58 (28%)`.

**On the quote rate I do not accept the "intake gap" explanation as written for this company** (merge notes §8;
§15.6's Amazon precedent). Tesla's intake is filings-only and those filings **are** on disk, so the secondary
print that explains Amazon's 39% does not exist here. I rebuilt the flagged spans and matched them against a
tag-stripped, entity-unfolded index of everything under `sources/`: **12 of the 15 unique spans resolve verbatim
in held bytes** (incorporation sentence, Tesla-store definition, "virtually all of our competitors…", the Rule
83 letters, 236 miles, "no agreements with Daimler or Freightliner", "event subsequent to the date of…",
traditional practices, pages 31 and 108–109, the $2.7m understatement, "We cannot, however, access…") — those
are the gate's matcher failing on markup/apostrophe splits (RD-131's class, exactly as the merge claimed for
*some* of them). **2 are the volume's own prose mis-extracted as quotations** ("until that edit happens a green
anchors result…", "three held exhibits and only three are contemporaneous documents") — instrument artifacts,
and the second is retracted by COR-04. **1 is genuine paraphrase-inside-quotation** (A5(iii), still unmatched,
now annotated in place with the filed sentence). **1 is the spliced first-person subject** ("we will correct the
error…"), annotated in place; the raw spliced string stays unmatched by design.
So: **advisory — yes, defect — no; "intake gap" — no.** The right label is *matcher gap plus two annotated
fidelity defects*. The 118 unattributed unmatched spans the gate also prints are a separate, larger advisory
bucket and none of them carries a citation.

---

## BLOCKERS (numbered, executable; none reopens an adjudication)

**B1\* — instruction layer still asserts the retracted false null.**
Locator `03_quality_control/tesla_s1_merge_notes.md` §7, lines 161–162. Claim quoted: "**$2009-12-31 is
UNKNOWN**, and the 'liability held flat across the deposit-policy inversion' reading **is not carried as a
finding**". The carrier prints: `-068933_ds1a.htm` "As of December 31, 2008 and 2009, refundable reservation
payments in the amount of $48.0 million and $26.0 million, respectively, were recorded as current liabilities",
plus three more 2009-12-31 bindings in that body, plus `-149105_d424b4.htm`, plus `S4375`. Minimal honest repair:
**append** a `> SUPERSEDED 2026-10-06 (certifier `tesla-cert-1`): §7's "$2009-12-31 is UNKNOWN" and "not carried
as a finding" were withdrawn by repair pass 1 and COR-01; the balance is filed at $26.0m (quantitative.csv,
2009-12-31). Do not apply this file's §7 as a current statement.` block — do not rewrite §7. The path has **no
entry in `_OWNER_LEDGER.json`**, so claim it first (`scaffold.py claim --path … --agent …`) and no owner is
displaced.

**B2\* — the carrier count published for the 2009-12-31 balance is understated in five cells.**
Locators: `conflicts.csv` `U.23` (`claim_b_source` + `evidence_weight`), `quantitative.csv` row
`2009-12-31 | refundable reservation liability` (note), `CORRECTIONS.md` COR-01, `stage_1.md` merge-header
repair paragraph and §U, `stage_1_index.md` `U.23` row. Claim quoted in all five: "**11 held bodies across 8
accessions** print it". The bytes print **15 bodies across 11 accessions**: the 11/8 pair is exactly the 2010
registration lineage; omitted are `-11-149963` (txt+htm), `-11-157135`, and the **registered** FY2010 10-K
`S4375`, which binds the value in a different instrument family — "As of December 31, 2010 and 2009, reservation
payments in the amount of $30.8 million and $26.0 million, respectively, were recorded as current liabilities on
the consolidated balance sheets". Minimal repair: restate the count as "15 held bodies across 11 accessions, of
which 10 bodies / 7 accessions are registered sources (S4370, S4371, S4372, S4375, S4379, S4380, S4381, S4387)
and the 2010 registration lineage alone accounts for 11 bodies / 8 accessions", or scope the existing sentence
to "in the 2010 registration lineage" and add `S4375` to the carrier list. (The auditor's "eight held documents"
was the same conflation; the fix must not re-publish either number bare.)

**B3\* — `sources.csv` `S4390`'s measured directory count is wrong in the register cell.**
Locator: `sources.csv` row `S4390`, `source_title`. Claim quoted: "Measured 2026-09-30: **8 files in
sources/wayback/, 3 negative HTML bodies …, 1 zero-byte JSON, 1 transcript, 3 sidecars**" (repeated in
`tesla_s1_repair_pass1.md` A8). The directory holds **7 entries: 4 `.json` bodies (`cdx_tesla_com_2003_2005.json`
160 B, `cdx_tesla_com_root_exacts.json` 160 B, `cdx_www_tesla_com_root_exacts.json` 11,832 B,
`cdx_tesla_com_2008_2011_founderish.json` 0 B), 2 sidecars (`*.meta.json`, 473 B each), 1 README.** There are 3
negative HTML bodies ✓ and the zero-byte-with-a-sidecar point is correct ✓; the counts "8 files / 3 sidecars" and
the repair sheet's "153 B" are not. Minimal repair: correct the enumeration in that one cell (7 entries, 2
sidecars, 160 B / 160 B / 11,832 B / 0 B) and note that only 2 of the 4 CDX bodies carry a sidecar — which is
itself the `http_status` gap A8 named.

**B4\* — family (b)'s open route is named to a hand fetch, not to the script that now exists.**
Locators: `stage_1.md` §U `U-1 / FETCH REQUEST`; `data_gaps.csv` rows whose `follow_up_task` says "via the CDX
route at FRA-1"; `_MANIFEST.md` "Open research debt … Web archives: domain-scoped CDX 2003–2009 then one `id_`
snapshot"; `03_quality_control/tesla_s1_merge_notes.md` FR-3; `tesla_s1_audit1.md` FRA-1 ("`tools/harvest_mine.py`
/ CDX re-query"). Carrier on disk: `tools/cdx_intake.py` — a deterministic family-(b) intake that records every
slot as ANSWERED / NULL / UNANSWERED / UNTRIED and writes `sources/web_archive/` with sidecars; it has run for
other slugs (`company_010_cencora/sources/web_archive/` exists, which is also why `scaffold.py ledger` now
PermissionErrors — see Residuals) and **has never run for tesla** (`company_043_tesla/sources/web_archive/`
absent; tesla absent from `tools/web_domains.json`, 5 slugs). §15.1: "no agent brief may include retrieval of a
document a script can reach" — as written, the next pass is briefed to hand-curl. The two held wayback sidecars
still assert "(no scripted route exists for the web-archive family)"; those bytes are protected and must be
superseded from the register, not edited. Minimal repair: name
`python tools/cdx_intake.py run --slug tesla --domain tesla.com` (domain provenance: the held CDX sidecars'
`url_param: "tesla.com matchType=domain"`, so the ledger entry can be cited rather than invented) in the four
instruction-layer locations, and record explicitly that **(b) stays TRIED–UNANSWERED and the tier stays T3 until
that command has run and been graded** — no tier claim may be made from an unexecuted route either.

**B5\* — §13 register vocabulary: a post-stage outcome with no `RETROSPECTIVE` label.**
Locator: `decisions.csv` row `2010-06-08 | Correct the FY2009 stock-compensation error prospectively in`,
`actual_result`. Claim quoted: "the uncorrected $(55740)k comparative **later printed in the 10-K**". Measured:
`RETROSPECTIVE` occurs **0× in `decisions.csv`**. §13 permits a post-stage reference "only when labeled
`RETROSPECTIVE`". Minimal repair: append ` [RETROSPECTIVE]` to that clause in the same cell (one token; the
volume already uses the label 8×, and the fact itself is correct and useful).

**B6\* — a denominator COR-06 withdrew is still printed in the volume's own tier line.**
Locator: `stage_1.md`, §U "Corpus-family status as this merge leaves it", family (a). Claim quoted: "**(a)
filings — TRIED and ANSWERED**, **76 held documents / 59,479,299 B** / 3,059,480 words … the reason T3 holds".
The same merge wrote COR-06 to withdraw exactly that count ("76 documents / 24 accessions; 76 / 28; 85 / 33") and
substitute "**83 documents across 32 accessions, 59,881,144 B**" — which I re-measured independently: 83 files
(61 `.htm` + 19 `.txt` + 3 `.pdf`), 32 accessions, 59,881,144 B. The COR-06 row two sections later in the same
volume prints the corrected figures, so one volume asserts both. Minimal repair: replace the three numbers in
that one clause with the COR-06 denominator (`83 documents / 32 accessions / 59,881,144 B`) and keep the words
figure only if re-measured. The T3 verdict does not move — family (a) is the one family with in-window Tier-1
text under either denominator — so this is a self-contradiction inside the tier justification, not a re-tier.

## NAMED RESIDUALS (reported; not blockers, not silent)

- **R-a intake debt.** Held-but-unregistered SEC printings: `-11-149963` (named as the exact-$49,999,992 carrier
  in a register cell), `-11-157135` (same sentence), `-10-147655`, `-10-147850`, and the 12 SEC-generated REGDEX
  rows COR-03 names. Rows must be minted centrally by a merge pass (`id_mint.py`), not by a repair or a certifier.
  No value depends on them; every prose citation names the path, so nothing is second-hand.
- **R-b protected pre-repair emissions**, deliberately left standing: `stage_1.md:829` (Volume 1's printed
  `timeline.csv` emission), `stage_1.md:2587` (Volume 2's `2009-05` validation emission), `_parts/s1_p1.md`,
  `_parts/s1_p2.md`. The canonical registers are corrected and the volume says so.
- **R-c `stage_1_index.md` decision 2 still reads "208 applied"** while its own register table reads 210, and
  `stage_1_index.md` + merge notes keep the merge's 53,553 words as a pre-repair statement. Scoped as merge
  history and labelled at the U.23 row; `_MANIFEST.md` is the live publisher and its numbers foot ✓.
- **R-d the auditor's sheet** still carries A5(iii)'s "0×", A8's "no sidecar", BLOCKER-1's "eight held documents"
  and A3's false premise, uncorrected in place; `tesla_s1_audit1.md` is claimed `done=false` in the ledger
  (heartbeat 2026-10-06T11:48Z, ttl 240), so it must be released before anyone annotates it.
- **R-e tool defects seen by this pass, not edited.** (i) `tools/scaffold.py ledger` dies with
  `PermissionError: … company_010_cencora/sources/web_archive` (it tries to read a directory as a file), so the
  ownership check a certifier is required to do is unavailable through the tool; (ii) `gates.py coverage` reports
  **81 source documents** against the 83 measured under `sources/sec/` (COR-06's denominator again); (iii) the
  quote gate's matcher still scores 12 spans absent that the held bytes contain (§8) — a gate precision problem
  the method's §15.5 would want self-tested.
- **R-f FETCH requests still owed, all script-reachable or named:** FRA-2 `sec_intake.py grab -017054` / `-149105`
  exhibit folders (charter, Series A/B purchase agreements, 2003 Plan, 424B4 column heads — now needed for the
  **flow**, not the balance); FRA-3 binary re-fetch of the 3 UPLOAD PDFs (`S4386` stays UNANSWERED, not empty);
  FR-4 state docket; FR-5/FR-6 the two unopened families. None of these is a Stage-1 defect.

## Checks that found nothing, and what each covered

1. **Merge-integrity re-measure (13 items)** — 210 rows at widths 18/12/11/15/8/15/11/11/11; headers present in
   all nine; `stage` column `stage1` throughout; 24 sources S4369–S4392 contiguous; 23 conflicts U.1–U.23 one row
   each, 0 duplicate keys; anchors 23↔23 by gate; every `source_id` in all six carrying registers resolves; the
   three emissions' arithmetic (40→24 sources with 16 aliases, 23 conflicts, 23→16 gaps, 46 timeline, 62/9/10/9/11)
   is consistent with `_MANIFEST.md` and the index. No orphan, no silent drop.
2. **Re-grade audit (5 blockers × 8–48 checks)** — every retracted statement located; 8 sites still print the old
   wording and all eight sit inside a withdrawal or a protected emission except merge notes §7 (B1*).
3. **Arithmetic sweep (19 register identities + 27 independent recomputations + the manifest/row totals)** — 0
   errors after repair; the two the repair found ($7,500,009 and 49,999,992) confirmed; residuals $8k/$16k
   confirmed on their stated bases.
4. **Byte tests against `sources/sec` (34 string/context tests over 80 bodies / 32 accessions)** — the carrier
   sentences for every changed cell verified, the counts in §1–§5 measured, and no quotation asserted as verbatim
   that the bytes do not print (beyond the two annotated in §8).
5. **Directory/accounting tests (5 sub-directories, 9 harvest bodies, 7 wayback entries, 2 ledgers)** — family
   claims supported except B3*/B4*; `_OWNER_LEDGER.json` confirms no live writer on any path I name as fixable.
6. **Hindsight/coda duty (4 temptations in §L.1, 6 "mechanism UNKNOWN", 3 closeness measures in §O.3, 8
   RESTATED/CONTEMPORANEOUS tags in §M/§N)** — no coda asserts a consequence without evidence, mechanism (or an
   explicit mechanism UNKNOWN), alternative and confidence; the firewall survives the repair.

## Re-measured after my last write

Measured from disk after writing this file (my only write): `stage_1.md` **54,903 words / 382,275 B**, 35 `##`
sections, one volume, `<!-- ANCHORS: U.1-U.23 -->`; `stage_1_index.md` **2,005 w / 13,369 B**; `_MANIFEST.md`
**1,941 w / 12,720 B**; `CORRECTIONS.md` **2,792 w / 19,666 B**, COR-01…COR-07 present; registers **210 rows /
16,837 w / 128,812 B** (24/62/46/23/16/9/9/11/10) — the totals `_MANIFEST.md` and the index publish foot exactly
against these cells; anchors 23↔23; conflicts U.1–U.23 unique; `sources/sec` = 83 documents / 32 accessions /
59,881,144 B / 61 `.htm` + 19 `.txt` + 3 `.pdf`; `sources/wayback` = 7 entries / 2 sidecars;
`company_043_tesla/sources/web_archive` **absent**; `tools/cdx_intake.py` present, tesla absent from
`tools/web_domains.json` (5 slugs). Gates: **2 findings / 18 passes, T3, 0 substantive**
(`03_quality_control/tesla_s1_gates_cert1.md`). This sheet: see its own footer count.

**Stage 1 verdict: CERTIFIED-WITH-NAMED-RESIDUALS.** Blockers B1\*–B6\* are one-cell mechanical edits; none
changes a value, a date or an adjudication. Tier stays **T3**. No value in this company may be re-imported from
`tesla_s1_merge_notes.md` §7 or from `tesla_s1_audit1.md` A5/A8/BLOCKER-1 without re-measurement.

**Second re-measure, taken after the final write of this file** (nothing in the corpus was touched by this
certification, and every number above is from the same disk state): `stage_1.md` 54,903 w / 382,275 B / 35 `##`
sections / `ANCHORS: U.1-U.23`; `stage_1_index.md` 2,005 / 13,369; `_MANIFEST.md` 1,941 / 12,720;
`CORRECTIONS.md` 2,792 / 19,666; registers 210 rows / 16,837 w / 128,812 B with the per-file numbers identical to
those published by `_MANIFEST.md` and `stage_1_index.md`; `sources/sec` 83 documents / 32 accessions /
59,881,144 B; `sources/wayback` 7 entries / 2 sidecars; `sources/web_archive` absent. This sheet: **5,004 words /
33,948 B**, 13 sections written, one file owned (`tesla-cert-1`), 0 web calls, 0 corpus edits.
