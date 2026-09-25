# amazon_s2_recertification_audit7.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:55:20Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Verdict

STATUS: WRITTEN 2026-09-26 (certifier `s2-recertify-2`, independent of both the audit-6 sheet and the repair pass)

**NOT-CERTIFIED.** The retraction itself is genuine and is the best-executed correction in this sequence — I re-read the
primary layer myself and it holds — but it stopped at the boundary of the narrative. It reached the prose, the index,
`CORRECTIONS.md` and `MASTER_RESEARCH_LOG.md`; it did **not** reach `conflicts.csv` or `sources.csv`, which is precisely
the surface Stage 3 cites. The repair sheet is candid about this ("handed off", "NOT EDITED (live register owner)"), so
nothing here is concealed. What is new is that the withdrawal also did **not** reach the retracted *chronology* wording
in `quantitative.csv`, did **not** reach the second half of the index that was supposed to record it, and the withdrawn
figure `0.194995` is **live and unmarked at six Stage-3 sites I have now read individually** — the repair pass counted
them and declared them "not asserted as live". I assert them.

**Gate criteria, as a whole.**
1. **Chronology / price walk** — **FAIL.** §U.113a's re-stated walk is correct at the document, and the narrative it
   protects (`stage_2_part_1.md` §A.3) is confirmed. But `quantitative.csv` **row 189** (`stage2`) still prints the
   struck wording as its own metric name and note, with **zero** retraction markers, citing U.98 as authority while
   §U.113a's BEST-SUPPORTED INTERPRETATION forbids those exact strings. → **B4**.
2. **Sources / citation** — **FAIL (register only).** All eleven re-keyed pointers in §U.113a land byte-exactly; the
   repair's rejection of audit-6's "pointer wrong by 60" is **correct** and audit-6 was wrong. Two pointers are still
   wrong in the register: `conflicts.csv` **U.113a** `claim_b` cites twin l.191/l.149/l.1204, and **U.113b** cites
   FY1998 10-K **l.1243**, which is the `========` totals rule and prints no digits (the figures are at l.1244). → B1, B2.
3. **Numbers** — **FAIL.** Stage 2's own two `0.194995` sites are genuinely repaired and residue-marked (§P.2 s4, record
   P26, §P80a, §U.52 all print `0.1950013`). The class is not closed corpus-wide: `quantitative.csv` **row 342**
   (`stage3`) carries it in `derived_arithmetic` as live arithmetic. → **B5**.
4. **Hindsight / class / independence** — **PASS in Stage 2, FAIL in the register.** Independence discipline is the
   strongest thing I found (see `## Independence audit`): every S-1 accession row says `DERIVATIVE OF S0801 within
   lineage L-97/333-23795`, and the two new §U records say `Corroboration: 1 lineage` rather than counting four
   accessions as four sources. But `sources.csv` **S2009** still reads `FACT (audited counterparty)` @ **High** on the
   same row as `not held locally`, with a `relevant_passage` quotation from a document the corpus cannot open. → **B3**.
5. **Internal consistency** — **FAIL (instruction layer, second half).** Parity is real and I re-measured it: **72** §U
   blocks ↔ **72** `stage2` conflict rows ↔ **72** §U records; **305 + 105 + 72 = 482** records. The index states the
   correct numbers at l.31/34/51 and the *withdrawn* numbers at l.128 and l.154, and two volume headers plus volume 2's
   coverage note still announce the superseded "70 rows" state. → **B6**.

**Blockers: 7.** B1 `conflicts.csv` U.113a (withdrawn proposition still live in the register); B2 `conflicts.csv`
U.113b (l.1243 pointer); B3 `sources.csv` S2009 (class + confidence + unverbatim passage); B4 `quantitative.csv` row
189 (struck chronology wording, unmarked); B5 six read-and-confirmed live Stage-3 sites of `0.194995`, plus the
**unfenced** `_parts/s3_p4.md`; B6 retraction not fully propagated through the index and volume headers; B7
`MASTER_RESEARCH_LOG.md` RD-100 mis-dates the blank-field original as "(21 Mar)".

**None of the seven re-opens the stage's argument.** §D's verdict, the boundary, the `(PB)` firewall, the price-walk
*sequence*, the 43%/41% conflict handling, and B125 all survive this audit intact — B125's six document pointers I read
individually and every one is exact. Six of the seven blockers are register rows already written out verbatim in
`amazon_s2_blocker_repairs.md` waiting to be applied, or a re-pointing sweep. B7 is one word in one log line.

**Method note on my own parsing (RD-100).** Every structural claim below is either from `tools/gates.py` output or
re-derived by importing **`gates.read_rows` itself** — not a hand-rolled reader. I made one hand-rolled parse at the
start, saw it disagree with the gate on `conflicts.csv`, discarded it, and re-ran through the gate's own function.
`python tools/gates.py --self-test` → **PASS** (9 defect cases CAUGHT, 1 false-positive case STAYS CLEAN).

**Instability during this certification.** The mandated command returned **two different answers** across my runs:
first `Findings: 7 | Passes: 41` with `conflicts.csv` passing at **170 rows**, later `conflicts.csv` failing with
**172 rows** and one 16-field row. Cause is a **live concurrent writer**: `conflicts.csv` mtime 01:26:17,
`quantitative.csv` 01:27:44, `sources.csv` 01:26:31, `timeline.csv` 01:26:54 — all during this pass, all owned by the
unfinished `_OWNER_LEDGER.json` claim of `s3-adversarial-repair`. Both new off-width rows (quantitative l.3, conflicts
l.3) are **`stage3`** rows and I do not count them against Stage 2 (T1), but the record must show that a certifier
cannot get a fixed measurement while an owner is writing shared registers (§14 rule 7).

## Retraction integrity

**1. Does the retracted correction now match the document? YES — and this is not a rewording.** I went to the primary
layer myself rather than trusting either sheet. `sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt`
**l.208–209** prints, on its face:

> "It / is currently estimated that the initial public offering price will be between / **$       and $       per share.**"

Two unfilled form fields. The original states **no** range, so audit-6's B1 was right and the withdrawal of the
asserted "stated range" was correct, necessary, and is not cosmetic: the re-stated CLAIM B changes the *evidence*
(a blank field standing beside a filled assumption), not the *adjective*. Every load-bearing pointer in the repaired
§U.113a I re-read independently and every one is byte-exact:

| §U.113a asserts | Document | My read |
|---|---|---|
| blank range fields, 1997-03-24 | S-1 orig. l.208–209 | **VERIFIED** — blanks present |
| fee table "2,875,000 shares $13.00 $37,375,000 $11,326" | S-1 orig. **l.166** | **VERIFIED**; re-key from twin l.149 is correct |
| DERIVED 2,875,000 × $13.00 = $37,375,000 | arithmetic | **EXACT**; share count reconciles at l.170–171 (2,500,000 offered + 375,000 over-allotment option; l.206 confirms "All of the 2,500,000 shares … are being sold") |
| dilution "Assumed initial public offering price per share … $13.00" | S-1 orig. **l.1221** | **VERIFIED**; re-key from twin l.1204 correct |
| No. 1 (1997-04-21) = **first accession to print a range**, $12.00–$14.00 | S-1A-No1 **l.247–248** | **VERIFIED** — the same sentence frame now carries digits |
| No. 1 fee table already at $14.00 / $40,250,000 | No. 1 **l.192** | **VERIFIED** |
| No. 1 pro-forma still $13.00 | No. 1 **l.1365** | **VERIFIED** |
| No. 3 range l.222–223 / cover $14.00 l.173 / "$13.00 per share" **l.1230** | S-1A-No3 | **ALL THREE VERIFIED** |

So the substantive repair is sound: the $13.00 is recorded as a **fee-and-pro-forma computation**, not a stated price;
the first *stated* range is correctly moved to Amendment No. 1 of 1997-04-21; and the block keeps the withdrawn
sentence visible inside the `⟪COR-16 SUPERSEDES …⟫` marker instead of erasing it (§14 rule 4).

**2. The repair refuted the certifier, and the repair was right.** Audit-6 l.102 ruled No. 3's `(l.1230)` "POINTER WRONG
BY 60". **I reject that finding.** No. 3 l.1230 reads "public offering price of $13.00 per share and after deducting the
estimated …" — inside the CAPITALIZATION pro-forma description, which is what the block said. Three pointers were
twin-inverted, not four, which is what `MASTER_RESEARCH_LOG.md` RD-094 already says. This is a correction to audit-6
itself, the sheet I am closing; audit-6 is not mine to edit.

**3. Did the retraction reach every layer? NO. It stopped at the register boundary — §14 rule 10.** `COR-16` occurrence
counts, measured: `CORRECTIONS.md` **3** (a full `## COR-16 — SUPERSEDES §U.113a's CLAIM B AS MINTED` entry that opens
with the instruction a cold reader needs: *"the 1997-03-24 S-1 original states NO IPO price range. Do not 'correct' any
narrative that says the range field was blank"*) · `stage_2_index.md` **3** · `MASTER_RESEARCH_LOG.md` **1** (RD-100) ·
`conflicts.csv` **0** · `sources.csv` **0** · `quantitative.csv` **0**.

The instruction layer is genuinely good. The data layer — the thing Stage 3 reads — is untouched. Sites still carrying
the withdrawn content, named:

* **`conflicts.csv`, `stage2` row `U.113a`, field `claim_b`** — still the false proposition verbatim: "S-1 orig.
  (1997-03-24) **states an estimated range** at l.191 while its cover prints $13.00 on 2,875,000 sh (l.149) and
  pro-forma repeats $13.00 (l.1204)". Contradicted by S-1 orig. l.208–209 (blanks) and by the row's own twin pointers,
  which the keyed file puts at l.208/l.166/l.1221. → **B1**.
* **`conflicts.csv`, `stage2` row `U.113b`, field `claim_b`** — still cites FY1998 10-K **l.1243** for
  "basic/diluted LPS (0.84)(0.24)(0.06)". I read it: **l.1243 is the `========` totals rule and prints no digits**;
  the LPS line is l.1244. The narrative §U.113b was fixed to l.1244 by the repair pass; the register row was not. → **B2**.
* **`sources.csv` row `S2009`** — untouched by the retraction: `evidence_class` still `FACT (audited counterparty)`,
  `confidence` still `High`, `archived_url` still `not held locally`, and `relevant_passage` still the quotation
  `'stocking over 400,000 titles'` offered as filed wording from a document no byte backs. The repair sheet supplied a
  full 18-field replacement; nothing was applied. → **B3**.
* **`quantitative.csv` `stage2` row 189** — carries the *other* half of what §U.113a retracts (below).

**4. The retraction's own sweep missed its own second claim.** §U.113a's BEST-SUPPORTED INTERPRETATION closes: "**no
'same morning', no 'five days', no 'first stated range', no 'obsolete on its own filing date'**". The repair swept
`states a range` / `one breath` / the twin cites — and did not re-sweep those four phrases against the registers.
`quantitative.csv` row 189 (`stage2`, dated 1997-05-15) still reads, with **no** retraction marker anywhere in the row:
metric = "Offer price relative to the range ceiling **filed the previous day**"; notes = "The upsize (+500000 = +20%)
and the re-price happened **within five days**: the roadshow document was **obsolete on its own filing date** (U.98)."
It cites U.98 as its authority while §U.113a — the block that now governs this walk — forbids the wording. Audit-6
flagged this row under criterion 1; the repair pass neither fixed it nor handed it off. → **B4**.

**5. B125 (the newly minted authorised-capital record) — VERIFIED, closes audit-6 B8.** All six of its pointers I read
at the document and every one is exact: pre-increase authorisation "5,000,000 … preferred … 25,000,000 … common" at
S-1 orig. **l.3813–3816** and Exhibit 3.1 Art. 4 **l.5192–5194**; the increase board-approved "In March 1997 … subject
to stockholder approval" at **l.4075–4080**; the summary at **l.280–283**; and the **1997-04-18** effecting date only in
No. 1 **l.4590–4593** ("On April 18, 1997, the Company effected a three-for-two common stock split, increased its
authorized common stock to 100,000,000 … preferred … 10,000,000"). The record's discipline is right in the way that
matters: it attributes the *date* to the accession that files it, and leaves the stockholder-approval date and the
purpose **UNKNOWN** instead of inferring them.

## Sibling sweeps

Whole-corpus sweep of the withdrawn figure `0.194995` / `19.4995`, run with `grep -o` over **all** of
`founders_playbook/` (`.md`, `.csv`, `.txt`, every sub-tree, `sources/` included), occurrence-counted not line-counted:
**63 occurrences in 18 files.** Nothing outside `company_001_amazon`, `03_quality_control/` and the log carries it, and
`sources/` returns **zero** hits — as it must, since no Amazon filing prints that quotient.

| File | Occ. | Classification |
|---|---|---|
| `03_quality_control/amazon_s2_audit3_repairs.md` | 11 | QC audit trail (D-06's own record) — not corpus |
| `03_quality_control/amazon_s2_recertification_audit6.md` | 10 | QC audit trail — not corpus |
| `_parts/s2_p4.md` | 8 | **FENCED** — 3 lines, each carrying `⟪SUPERSEDED 2026-09-25 · R-3 · 28813 ÷ 147758 = 19.50013% not 19.4995 …⟫`; value repeats inside the banner |
| `03_quality_control/amazon_s2_audit3_numbers.md` | 6 | QC audit trail |
| `03_quality_control/amazon_s2_blocker_repairs.md` | 5 | QC audit trail (the repair's own sweep) |
| `MASTER_RESEARCH_LOG.md` | 3 | Instruction layer, RD-100 — states the survival honestly |
| `_parts/s3_p4.md` | 3 | **UNFENCED — see below** |
| `03_quality_control/audit8_residue_repairs.md` | 2 | QC audit trail |
| `company_001_amazon/stage_3_part_3.md` | 2 | **LIVE ×2** (§P188, §P.2 t1) |
| `company_001_amazon/stage_3_claim_records_part_1b.md` | 2 | **LIVE ×2** (P95, P179) |
| `company_001_amazon/stage_2_part_2.md` | 2 | Correct / residue-marked (§P.2 s4, §P80a both print `0.1950013` with the old value kept visible as a residue note) |
| `company_001_amazon/quantitative.csv` | 2 | row 127 (`stage2`) **correct** `0.1950013`; row 342 (`stage3`) **LIVE** in `derived_arithmetic` |
| `company_001_amazon/CORRECTIONS.md` | 2 | Correct — inside the `19.4995` → `19.50013%` supersession pair |
| `03_quality_control/stage3_register_binding.md` | 1 | QC audit trail |
| `company_001_amazon/stage_3_pending_registers.md` | 1 | **LIVE** — held row, same content as quantitative.csv 342 |
| `company_001_amazon/stage_2_part_3.md` | 1 | Correct — §U.52 prints `19.50013%` and names the bad value as struck |
| `company_001_amazon/stage_2_claim_records.md` | 1 | Correct — record **P26** retraction |
| `company_001_amazon/stage_2_claim_records_part_2.md` | 1 | Correct — record **U.52** |

**Stage 2 itself is clean: 0 live.** The B2 repair holds at every Stage-2 site, and each repaired cell prints the
superseded value inside the same cell as a residue note, which is the §14 rule-8 form.

**But the class is NOT closed, and the repair pass's own hedge is now resolved against it.** The blocker sheet counted
six downstream sites and said they were "counted but not read individually … may already sit in retraction language …
**Not asserted as live**." I read all six. **All six are live, presented as arithmetic, with no retraction marker:**

1. `quantitative.csv` **row 342** (`stage3`) — `derived_arithmetic` = `28813/147758=0.194995 and 28818/147787=0.194935`
2. `stage_3_part_3.md` **§P188** — "**19.5** as filed (`28,813 ÷ 147,758 = 19.4995`)"
3. `stage_3_part_3.md` **§P.2 t1** — "As filed: `28,813 ÷ 147,758 = 0.194995 → 19.5%`"
4. `stage_3_claim_records_part_1b.md` **P95** — "(19.4995 filed / 19.4935 restated)"
5. `stage_3_claim_records_part_1b.md` **P179** — "Value: filed 28,813 ÷ 147,758 = 0.194995 → **19.5%**"
6. `stage_3_pending_registers.md` **row at l.61** — the same `derived_arithmetic`, queued to become register row 342

Correct value 28,813 ÷ 147,758 = **0.19500129**, i.e. `0.1950013`. The false quotient rounds to the same 19.5%, which
is why no total ever broke (§14 rule 8's exact failure mode: a plausible number that survives because it never
disagrees with anything). → **B5**.

**New finding the fencing convention depends on: `_parts/s3_p4.md` is NOT fenced.** Audit-6's T8 tolerated the whole
`_parts/` layer *because* `s2_p4.md` carries inline `⟪SUPERSEDED …⟫` banners. `s3_p4.md` contains **zero** occurrences
of `SUPERSEDED`, and l.79 is a byte-copy of the stale §P188 row. So the T8 argument does not extend to the Stage-3
draft parts, and `s3_p4.md` is the re-import mechanism for this class — the same mechanism audit-6 blamed for B1.
Included in **B5**.

**Two sibling sweeps of my own, beyond the digits.**
* **Struck price-walk wording** (`five days`, `same morning`, `previous day`, `obsolete on its own filing date`) across
  the nine registers and all stage volumes: **1 live unmarked site, `quantitative.csv` row 189 (`stage2`)** → B4. Every
  narrative site is retraction-marked; `timeline.csv` keeps the wording only inside a retraction note.
* **Twin-vs-keyed pointer inversion** on the S-1 original family: the three re-keys in §U.113a are correct; the same
  **twin** numbers (l.191/l.149/l.1204) are still printed in `conflicts.csv` U.113a → B1. No other Stage-2 site carries
  them.
* **`43%` vs `41%` version difference** (the pair a bad pass would average): swept across all nine registers and every
  stage volume. Recorded as a **conflict with both carriers named** at §U.53 (CLAIM A = S-1 original Risk Factors
  l.986, 1997-03-24; CLAIM B = No. 5 l.1055, 1997-05-14), at `conflicts.csv` **U.53** (`stage2`), in records **B97**,
  **P60**, **Q51**, **Q59**. **No averaged or ranged form exists in the corpus** — the only `~41-…%` strings are
  dossier-local (`research/ST2_E_adversarial.md`, `research/H_legal_organization.md`), which §13 makes non-canonical.
  This check **passes**.

## Independence audit

The brief's test: *a figure printed in an S-1 and again in its amendment is ONE source, not two.* Stage 2 applies this
correctly, and applies it better than I expected to find it. **One breach, and it is in `sources.csv`.**

**1. Corroboration language — PASSES, in the exact place the failure class lives.** The two records minted for the
lettered addenda do not count the lineage as corroboration:
* record **U.113a** — `Corroboration: **1 lineage**`
* record **U.113b** — `Corroboration: **1 issuer lineage re-printed**, which is exactly why this is a conflict and not a
  corroboration (§3)`

The second is the correct inference drawn from the filing-lineage rule and worth quoting to the next pass: two states of
one instrument do not corroborate each other, they *conflict*. §U.113a's own WHY THEY DIFFER says the same thing in
operational terms — "the lineage is one source family (§3), each amendment re-prints its predecessor's sentence while
re-striking the numbers in the cover table, so a reader who takes the cover figure from one accession and the range
sentence from another gets two states at once". That is the precise mechanism that produced the withdrawn CLAIM B, and
it is named rather than papered over.

**2. `independence_note` fields — PASSES across the whole accession family.** Measured at the register with the gate's
own reader, all eight lineage rows carry the cap explicitly: **S0801** "THE SINGLE LARGEST ANCESTOR IN THE CORPUS …
S0802-S0805 largely restate it, so those are ONE instrument"; **S0802** "Second state of the same registration statement
as S0801: repetition here is NOT corroboration, and where the two differ only in rounding that is not corroboration
either"; **S0803** "Third state … NOT an independent source for anything already in S0801; the four disclosures this
note formerly credited as independent …"; **S0807/S0808/S0809/S0810** (Nos. 1, 2, 4, 6) each "DERIVATIVE OF S0801 within
lineage L-97/333-23795 … one instrument in eight accessions, not eight"; **S2012** (424B1) "NOT INDEPENDENT - the issuer
reporting its own pricing … also NOT INDEPENDENT OF THE LINEAGE: the 424B1 of 15 May is the same registration statement,
File No. 333-23795." Per-record: **K19** and **K20** both `Corroboration: 1 (same lineage as the registration statement,
File 333-23795)`. §13's `independence_note` contract is being honoured, and the 424B1's repetition of the No. 6 hedge is
credited to No. 6, not double-counted.

**3. Retrospective material is not labelled FACT — PASSES, including at the site audit-6 flagged.** I checked the B5
repair specifically rather than trusting its summary. Record **K19** now reads `FACT (acts and terms) + INFERENCE
(bounded superlative, this closing clause)` and states in the record itself: "it is a retrospective ranking, not a
Stage-2 fact (§2, §6)"; record **N13** carries `INFERENCE (bounded superlative) over FACT (acts and terms) / UNKNOWN
(motive)`, both bounded to "the boundary of this stage (1997-05-15)" and both naming the post-boundary evidence that an
unbounded claim would have to survive (the 1997-12-23 $75,000,000 facility). Record **N14** separates
`FACT (amounts) / RETRO (rationale)`. The firewall is doing its job here.

**4. Version differences are recorded as conflicts, never averaged — PASSES.** 43% vs 41% is held as §U.53 with both
carriers and both filing dates named (S-1 original Risk Factors l.986, 1997-03-24 / No. 5 l.1055, 1997-05-14), plus the
matching `conflicts.csv` U.53 row and records B97/P60/Q51/Q59. No `"~41-43%"` form exists anywhere in the corpus; the
restated-pair conflict U.113b likewise prints as-filed and re-based side by side with the rule "never average, never
call either 'the figure'".

**5. The breach: `sources.csv` row S2009 — independence of ORIGIN is being used to buy independence of VERIFIABILITY.**
Sole `stage2` row in the register still carrying `FACT (audited counterparty)` (measured: exactly 1 such row), and its
`independence_note` reads "GENUINELY INDEPENDENT of every Amazon row in this register: a different registrant, a
different auditor, no common drafter. This is the ONLY Tier-1 Amazon-universe document in the stage that Amazon did not
write." Every word of that is true about *origin*. It is also the sentence a Stage-3 reader uses to raise a
confidence — on a row whose own `archived_url` cell says `not held locally` and whose `relevant_passage` is
`'stocking over 400,000 titles'`, a quotation from bytes the corpus does not contain. §3 caps confidence "at what a
single document supports" when only the lineage exists; here not even a document exists, only a dossier transcription of
a temporary read. Independence cannot substitute for evidence, and a competitor's provenance does not make an
uncitable passage citable. This is the same failure family as §U.113a's ellipsis — **a quotation offered as evidence
from a text the corpus cannot open** — which the repair sheet itself diagnoses and then leaves in the register. → **B3**.

**Consistency check against the rest of the corpus:** `quantitative.csv` L181/L182 and §P164 already carry this identical
witness as **UNKNOWN** with a `NOT-ON-DISK` opener, and record U.67 classes both multipliers UNKNOWN. So the narrative
and the registers agree with each other and disagree with `sources.csv`. Stage 3 cites `sources.csv`. That is why B3 is
a blocker and not a tolerable.

## Blockers

Seven. Each is file + stable label + the document line that contradicts it. Line numbers appear only as locators
alongside labels (§14 rule 12). Addressed to the register owner and the Stage-3 owner, not to me: I edited no stage
volume, register, source or `CORRECTIONS.md`.

**B1 — the withdrawn proposition is still the live content of the register row Stage 3 cites.**
`conflicts.csv` **U.113a** (`stage2`), field `claim_b`: "S-1 orig. (1997-03-24) **states an estimated range** at l.191
while its cover prints $13.00 on 2,875,000 sh (l.149) and pro-forma repeats $13.00 (l.1204)". **Contradicted by**
`sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` **l.208–209**, which I read: "…will be between /
**$       and $       per share.**" The fields are blank; the accession states no range. The row also (i) still prints
**twin** numbers against **keyed** paths, when the same file's convention is keyed = twin + 17 and the keyed locations
are l.208 / l.166 / l.1221, all three of which I verified byte-exact, and (ii) puts prose in a §13 date column
(`claim_a_date` = "struck 2026-09-25; wording had been current in Stage 2 from 2026-09-24") and line numbers as
addresses in `claim_a_source` ("`stage_2_part_3.md` §T l.97-104"). The correct 15-field row already exists, written out
in `amazon_s2_blocker_repairs.md` `## Register handoff`. **Apply it; do not append** — the U.113a row exists and
duplicating `conflict_id` is what the keys gate catches.

**B2 — the sibling row's pointer is wrong in the register and right in the narrative.**
`conflicts.csv` **U.113b** (`stage2`), field `claim_b`: FY1998 10-K "basic and diluted loss per share (0.84)(0.24)(0.06)
(**l.1243**)". **Contradicted by** `sources/10-K_FY1998_acc-0000891020-99-000375_filed-1999-03-05.txt` **l.1243**, which
I read and which is the `========` totals rule and prints no digits; the LPS line is **l.1244** ("Basic and diluted loss
per share (2)…. $(0.84) $(0.24) $(0.06)"), and the net-loss row is l.1242. The narrative §U.113b was corrected to
l.1244 by the repair pass; the register row was not. Travels with the same handed-off row.

**B3 — class and confidence still exceed the evidence in `sources.csv`.**
`sources.csv` **S2009** (`stage2`, the B&N FY1996 Form 10-K) — measured as the **only** `stage2` row in the register
still reading `FACT (audited counterparty)` — carries `confidence: High` and
`relevant_passage: 'stocking over 400,000 titles'` on the same row as `archived_url: not held locally`.
**Contradicted by** the absence of any byte for that accession under `sources/` (nothing to read the passage at), and by
the corpus's own treatment of the identical witness: `quantitative.csv` L181/L182 open `NOT-ON-DISK` and record **U.67**
classes both multipliers UNKNOWN. The row's `independence_note` ("GENUINELY INDEPENDENT … the ONLY Tier-1
Amazon-universe document in the stage that Amazon did not write") establishes independence of **origin**, which §3 caps
at the evidence a single document supports; with no document, High is unearned. The 18-field replacement is already
written out in the handoff section of the repair sheet: `FACT (the filing exists) / UNKNOWN (its CONTENTS)` +
`Low / UNKNOWN` + the passage marked NOT VERIFIABLE AT THE CITATION, with no value, date, accession or URL changed.

**B4 — the retraction swept the *quotation* and not the *chronology*, and a register row kept the struck wording.**
`quantitative.csv` **row 189** (`stage2`, `1997-05-15`), metric cell "Offer price relative to the range ceiling **filed
the previous day**", notes cell "The upsize (+500000 = +20%) and the re-price happened **within five days**: the
roadshow document was **obsolete on its own filing date** (U.98)." Zero retraction markers anywhere in the row
(measured). **Contradicted by** `stage_2_part_3.md` **§U.113a**, whose BEST-SUPPORTED INTERPRETATION states the rule for
this exact record: "no 'same morning', no 'five days', no 'first stated range', no 'obsolete on its own filing date'".
**Contradicted in turn by the documents the block keys:** the range ceiling 16.00 is filed in Amendment No. 4
(`sources/S-1A-No4_acc-0000891020-97-000822_filed-1997-05-13.txt`, §T l.101), i.e. two days before the 1997-05-15 offer
date this row carries, not one, and the intervening document was current for two days rather than obsolete on its
filing date. Audit-6 caught this row under criterion 1; the repair pass neither repaired nor handed it off, and its
sweep patterns (`states a range`, `one breath`, twin cites) could not have found it. The row's `derived_arithmetic`
(18.00 / 16.00 = 1.125) is correct and stays; only the narrative cells need the retraction.

**B5 — `0.194995` is live and unmarked at six Stage-3 sites, all now read individually, plus an unfenced draft part.**
The repair pass counted these and declined to assert them ("counted but not read individually … may already sit in
retraction language"). I read all six; **none is in retraction language**:
`quantitative.csv` **row 342** (`stage3`, `derived_arithmetic` = `28813/147758=0.194995`);
`stage_3_part_3.md` **§P188** ("**19.5** as filed (`28,813 ÷ 147,758 = 19.4995`)");
`stage_3_part_3.md` **§P.2 t1**;
`stage_3_claim_records_part_1b.md` **P95**;
`stage_3_claim_records_part_1b.md` **P179**;
`stage_3_pending_registers.md` row queued at l.61 (the same arithmetic, which will *become* the register row if merged
unfixed).
**Contradicted by** `sources/10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` **l.1402/l.1403** with **l.1177**
(gross profit 28,813 ÷ net sales 147,758 = **0.19500129**, and the company's own comparative row prints 19.5%), and by
Stage 2's own corrected cells: `quantitative.csv` **row 127** (`stage2`) now carries `28813 / 147758 = 0.1950013`.
Both quotients render to 19.5%, so nothing footed wrong — the reason this survived five passes.
Also **`_parts/s3_p4.md` l.79**: three occurrences of the false value with **zero `SUPERSEDED` banners in the whole
file**, which breaks the specific ground on which audit-6's T8 tolerated the `_parts/` layer, and makes it the
re-import path for this class.

**B6 — the retraction reached the top half of the index and not the bottom, and two volume headers still teach the
withdrawn count.** `stage_2_index.md` correctly reports **72 §U blocks / 72 stage2 rows / 305 + 105 + 72** at l.31,
l.34, l.51 and l.89 — all of which I re-measured and all of which are true. But the same file still asserts, at
**l.128**, that the appendix is "`stage_2_claim_records.md` + `stage_2_claim_records_part_2.md`, **479** records" (a
two-volume description that omits volume 1b entirely), and at **l.154**, "**Stage-2 total: 479 records, unchanged by the
split**". **Contradicted by measurement**: 305 + 105 + 72 = **482**, and the split *did* change the total (it added
records U.113a and U.113b and minted B125). `479` is the withdrawn pre-repair count. Compounding it, the header block of
**both** narrative volumes — `stage_2_part_1.md` l.6 and `stage_2_part_3.md` l.6 — still reads "`conflicts.csv` still
holds **70** Stage-2 rows until the register owner appends them", and `stage_2_claim_records_part_2.md` **l.222** still
frames coverage as "U.44 → U.113 … (70/70)". **Contradicted by** `conflicts.csv`, which the gate's own reader measures
at **72** `stage2` rows. This is the one-place-fixed/one-place-stale class that RD-094 names, now in the file every
agent reads first.

**B7 — the log entry that records this retraction mis-dates the document it retracts.**
`MASTER_RESEARCH_LOG.md` **RD-100**: "the claim became: blank field plus the $13.00 fee assumption (**21 Mar**) → the
first *stated* range at Amendment No. 1, 21 Apr". **Contradicted by**
`sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt`, whose filename and cover are **1997-03-24**, and by
`CORRECTIONS.md`'s own COR-16 entry and §U.113a, both of which date the blank-field original to 24 March. 21 March is
not a filing date of any accession in lineage 333-23795; 21 **April** is No. 1's. Under §14 rule 10 the instruction
layer is the highest-severity home for a stale value, and this is the single line a cold reader takes as the corrected
chronology. One word.

## Tolerable

What this certifier does **not** count against Stage 2, and why.

**T1 — gate `csv`: `quantitative.csv` row 3 at 13 fields, `conflicts.csv` row 3 at 16 fields.** Both are **`stage3`**
rows (quantitative l.3 carries `stage3`/`1998-05-08`; conflicts l.3 is `U.170`, `stage3`) written by a live concurrent
owner during this certification. Stage 2 does not own them. Reproduced with `gates.read_rows`, not with a hand-rolled
reader (RD-100).
**T2 — gate `keys`: unresolvable `S3001/S3004/S3007/S3012/S3013/S3020/S3022/S3024` tokens.** Every finding names a
**Stage-3** volume. All nine Stage-2 volumes pass `keys` (16 tokens in the index, 259/109/116 hyphenated dossier keys in
the record volumes, all resolving). Carried forward as the warning audit-6 read it: Stage 3's source keys are not bound,
and B1–B5 land on exactly that surface.
**T3 — gate `anchors`: `U.220` with no register row; register rows for `U.169`, `U.201–U.211` with no narrative anchor.**
Stage-3 dossier-local keys written into global columns. Stage 2's own parity is intact and I re-measured all three
sides of it independently: **72** `**U.nnn —` blocks in `stage_2_part_3.md` ↔ **72** `^U.nnn Claim:` records in
`stage_2_claim_records_part_2.md` ↔ **72** `stage2` rows in `conflicts.csv`. 1:1:1.
**T4 — gate `budget`: nothing.** All seventeen stage volumes now pass; the largest Stage-2 file is `stage_2_part_3.md`
at 46,016 and `stage_2_claim_records.md` is **44,766** words. The 60,718-word breach audit-6 recorded as B7/T1 is gone,
it was closed by splitting rather than by trimming (§9.6), and the split is intact — so I do **not** re-raise it, and I
note the opposite failure did not occur: no evidence was cut to satisfy a gate.
**T5 — `_parts/s2_p4.md` (8 occurrences of the withdrawn value) and `_parts/s3_p1..p3`.** Tolerable **only** for
`s2_p4.md`, whose three value lines each carry an inline `⟪SUPERSEDED 2026-09-25 · R-3 · 28813 ÷ 147758 = 19.50013% not
19.4995 …⟫` banner, and only in combination with `stage_2_index.md`'s declaration that the parts are the drafting audit
trail. **`_parts/s3_p4.md` has no such banner** (0 occurrences of `SUPERSEDED` in the file) and is therefore *not*
tolerable — it is inside B5. Audit-6's T8 generalised from the fenced file to the whole layer; that generalisation is
the residue.
**T6 — the class-integrity site I expected to fail and did not.** I went looking for a half-applied B5 and found the
opposite: record **K19** carries `FACT (acts and terms) + INFERENCE (bounded superlative, this closing clause)` and
names itself "a retrospective ranking, not a Stage-2 fact (§2, §6)". The repair's claim was true at the site it named.
**Recorded as a pass, not a tolerable defect.**
**T7 — the repair pass's rejection of audit-6's "pointer wrong by 60" is upheld, and audit-6's count is corrected.**
Three twin-inverted pointers, not four. `conflicts.csv` row 135, which audit-6 attributed to Stage 2's U.107, is
`P-U.134`, a `stage3` row; U.107 sits elsewhere. Both of the repair sheet's corrections **to** the certifier are
accepted, and B6's withdrawal as a parser artifact is accepted: I reproduced 170-of-170 rows at 15 fields using
`gates.read_rows` and agree that applying the width "fix" would have corrupted valid data.
**T8 — `context_appendices.md` / U.107 CLOSED status: not re-tested by me.** Audit-6 measured the strings inside
withdrawal sentences only; the surviving instruction-layer assertion it routed to the orchestrator (`MASTER_RESEARCH_LOG.md`
around the U.107 line, with off-by-2 pointers) is outside my budget this round. Neither confirmed nor cleared.

**UNTRIED at the ceiling — named as a deliverable, not a disclaimer.** (1) The 10-K405 **l.1721** integrity question
audit-6 raised and the repair pass explicitly deferred — whether the `22,655` denominator behind the as-filed `$(0.25)`
is labelled *revised* by the same document that files it, and whether §P.2 s1 must therefore name the revision. This is
a live basis question about a Stage-2 figure and the next pass should settle it. (2) `(PB)` firewall census and
`part_1b`'s §Q–§T margin sites. (3) Per-row basis labelling of `147,787` vs `147,758`; `(0.31)` sites lacking the words
"PRO FORMA"; the 365/366 day basis; D-13's eight new `timeline.csv` rows. (4) `_MANIFEST.md` — whether it registers
volume 1b and carries the 70→72 / 479→482 deltas; given B6 I regard a manifest check as likely to find the same
half-propagation. (5) `data_gaps.csv` High-importance-gap completeness. (6) RD-072's `research/ST3_B_*` dossier side.
(7) A **directed** Stage-3 sweep for the other Stage-2 repaired classes (rent 257, 30.81409, 0.2549989, 14.0500004,
39.5690, the B&N reclass, the restatement pair): B5 proves the pattern — a Stage-2 repair verified clean in Stage 2 is
not clean in Stage 3, and I only swept the one class the brief named.

## Gate gaps found

The suite was proven for my round: **`python tools/gates.py --self-test` → PASS** (9 cases — 8 defects CAUGHT across
`csv`/`keys`/`anchors`/`quotes`, and the *must-stay-clean* false-positive control "correctly escaped doublequote"
STAYS CLEAN). The mandated run
`--checks csv,keys,anchors,budget` → **Findings: 7 | Passes: 41** on its first execution, and **Findings: 2** on `csv`
alone later in the same session; the drift is explained under gap 5, not by a changed parser.
**Every blocker in this sheet except B6 was invisible to that run.** That is the finding.

**1. There is no retired-value sweep, so the suite structurally cannot see `0.194995`.** The dispatched checks are
`gate_csv` (width, duplicate primary keys, stage vocabulary, year-bearing date columns, `source_id` resolution),
`gate_keys`, `gate_anchors`, `gate_quotes`, `gate_budgets`. **None accepts a list of withdrawn literals, and none greps
the corpus for a value that a prior pass retired.** B5 — six live sites of a quotient retracted five passes ago — is
not a check the gate fails to pass; it is a check the gate does not have. This is the single highest-value addition,
and it is cheap because the corpus already carries the inputs in machine-readable form:
`CORRECTIONS.md` prints supersession pairs (`**19.4995`** (`**19.50013%**`)`, `30.813`→`30.81409`, `0.2548`,
`14.0500007`, `≈39.5` …) and every fenced retirement uses the literal `⟪SUPERSEDED …⟫` / `COR-nn` idiom. A
`retired` gate would parse those pairs, sweep every stage volume and register, and fail any occurrence that is **not**
on the same row or inside the same cell as a retraction marker. Its must-stay-clean control is already sitting in the
corpus: the 3 fenced lines of `_parts/s2_p4.md` and the 5 residue-marked Stage-2 cells.
**Corollary, and it is the version of this that produced B4:** the same gate should carry **struck phrases**, not only
digits. §U.113a's own BEST-SUPPORTED INTERPRETATION enumerates four forbidden strings; `quantitative.csv` row 189 uses
three of them unmarked. A phrase list is as mechanical as a number list.

**2. No cross-stage propagation check.** B4 and B5 are the same shape: a repair verified clean *inside the stage that
made it*, surviving in a later stage. Every register already has a `stage` column and `narr_files()` enumerates all
three stages' volumes, so "a literal retired at `stageN` may not appear unmarked at `stageN+1`" is one comparison.
audit-6 called the directed Stage-3 sweep "the highest-value next call"; three passes later it still has not run, and
this round I found live instances by sweeping only the one class the brief named.

**3. No pointer-resolution check, which is where B1 and B2 live.** `stage_2_index.md` *declares* the convention
(`twin line = keyed line − 17`) in prose, and then four blockers' worth of cites were minted against the wrong side of
it. `gate_quotes` verifies that a **quoted span exists somewhere** in the local source text; it does not resolve an
`l.NNNN` attached to a named `sources/` path. Resolving "does the cited line contain the cited string" is a two-line
dict lookup per file, and it would have caught twin inversion mechanically — including audit-6's own false positive
(No. 3 l.1230, byte-present) and the repair pass's newly found l.1243 → l.1244.

**4. `anchors` compares two of the three things that must agree.** It measures §U blocks against `conflicts.csv` rows.
The invariant Stage 3 actually relies on is **block ↔ conflict row ↔ claim record**, and the missing leg is the one
audit-6's B7 turned on (72 blocks against 70 records). I re-measured all three legs by hand with a regex count; the
gate cannot see the record leg at all, so a future pass that restores 1:1 rows-and-blocks while dropping records would
report clean.

**5. The suite takes no account of file ownership, so its output is not reproducible while a register has a live
writer.** My mandated command returned `conflicts.csv` passing at **170 rows** and, twenty minutes later, failing with
**172 rows**. Both were correct at their instant: `conflicts.csv`, `sources.csv`, `quantitative.csv` and `timeline.csv`
were all modified during this certification by the unfinished `s3-adversarial-repair` claim in `_OWNER_LEDGER.json`.
gates never reads that ledger and its report stamps no mtime or row count. A certifier therefore cannot tell from the
report whether it measured a file or a moving target — and RD-084/RD-078-style "residue" findings get re-litigated
because of it. Minimum fix: emit each register's mtime and row count into the report body; better: warn, not pass, when
a file's mtime post-dates the run start or sits under a live claim.

**6. The mandated set omitted `quotes`.** `--checks csv,keys,anchors,budget` was the instructed command, so verbatim
existence in this round is my judgment against `sources/`, not the script's. Stated as a limit on my own verdict.
But I will not over-claim what `quotes` would have caught: §U.113a's quoted span "is currently estimated that the
initial public offering price will be between …" **is** byte-present in the original. The defect was never the quote;
it was the *elided* text being the refutation. **No existence check can see an ellipsis that hides a blank field** —
that requires comparing the quoted span against the sentence's own predicate slots, which is a judgment. Independence,
class integrity, ellipsis honesty and conflict adjudication stay with agents under §15.1; gaps 1–3 and 5 are the parts
that are not.

