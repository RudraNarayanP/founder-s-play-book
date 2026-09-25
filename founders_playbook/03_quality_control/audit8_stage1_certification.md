# AUDIT 8 — INDEPENDENT FINAL CERTIFICATION, AMAZON STAGE 1 (`company_001_amazon`)

**My status.** I am the fourth pair of eyes and the final certifier. I wrote none of the material under review: not
`audit6_stage1_independent_qa.md` (verdict REOPEN), not `audit6_repairs.md`, not
`audit7_stage1_recertification.md` (verdict REOPEN), not `audit7_repairs.md` (the third pass). I grade the third
pass, and I re-measure rather than inherit.

**Read-only: YES.** No existing file was edited, moved or deleted by this run. The only file created inside the
repo is `founders_playbook/03_quality_control/audit8_stage1_certification.md` (this sheet). Every script and every
output dump lives OUTSIDE the repo at `E:\tmp\qoder_audit8\`. Git was used read-only only
(`log`, `status`, `show`, `diff`, `rev-parse`); no ref moved, nothing staged, nothing checked out.

**Zero web requests: YES.** No WebSearch and no WebFetch call was issued. Every figure below is derived from files
on disk in `E:\founder's playbook`. Where a question can only be settled off-disk I say UNTRIED and name the query.

**Counting conventions stated up front**, because the third pass's sweep numbers are the thing I am partly grading.
For each family I report four separate measures and never conflate them: (i) occurrences of the token pattern
(`grep -o`-equivalent / `re.finditer`), (ii) matching lines (`grep -n`), (iii) files touched, (iv) occurrences my
negation-window classifier cannot account for. The sweeps below were re-run from a clean shell
(`C:/Program Files/Git/usr/bin/bash` via the Bash tool, `PYTHONIOENCODING=utf-8`), from
`E:\founder's playbook/founders_playbook/01_companies/company_001_amazon`, and the Stage-2 exclusion filter is the
third pass's own (`grep -v -E "stage_2|s2_|ST2_|_EVIDENCE_CACHE"`).

**Repo state at certification, and drift during it.** I began against `HEAD = 4a48648` ("Stage 1 third repair
pass: the retracted share-count leg swept to zero live sites") and the repository moved under me mid-run: commit
`6b80495` ("Walmart registers built from A3 …") landed during my sweeps, and `stage_2_part_3.md` remains modified in
the working tree by the concurrent Stage-2 agent. **I re-checked the drift rather than assuming it**: the only
Stage-1 artifact touched between the two commits is `research/_EVIDENCE_CACHE.md` (a Stage-2 cache), and
`git diff 4a48648..HEAD -- <any Stage-1 file>` is empty for `stage_1.md`, `stage_1_claim_records.md`,
`context_appendices.md`, `CORRECTIONS.md`, `adversarial_review.md`, `_MANIFEST.md` and every `_parts/s1_*.md`, so
every line number, arity and parity figure below is re-runnable against `HEAD` as printed. The third pass's own
baseline claim (`stage_1.md` diff = one hunk) is tested at §3.5 and §2.

---

## Verdict table

**Part 1 — the four AUDIT-6 blockers as they stand after three repair passes** (AUDIT 7's two blockers are the
B-1 and B-2b rows; its B-2a is the A-B1 row):

| Blocker | Item | Verdict | My primary proof (file:line) |
|---|---|---|---|
| **B-1** — a retracted figure live in a Value column / correction voice | 6 | **CLOSED** | Sites the passes named, now withdrawn in place: `_parts/s1_p1.md:144–163` · `_parts/s1_p3.md:182–199` · `research/E_supply_ops_finance.md:564–581` · `_parts/NUMBER_DEFECTS.md:74–78` + `:112–154`. Sibling found by sweeping, not by the list: `_parts/NUMBER_DEFECTS.md:90–97`. Row-level (not just footer-level): `_parts/NUMBER_DEFECTS.md:27`, `:28`. Canonical text verified at `stage_1.md:610`, `:874`, `:961`, `:1487`, `:1539`, `quantitative.csv:35`, `context_appendices.md:598`, `:641`. Sweep: §1.1 (174/179 occurrences, **0 live** under three tests) |
| **B-2a** — filing-lineage demotion + attack A-B1 | 9, 12 | **CLOSED** | `stage_1.md:39–48` (scope statement that names its own prior falsity), `:63–73` (premise proved), `:586`, `:896`, `:1169`, `:1233–1236`; `sources.csv:51`, `:53`; `CORRECTIONS.md:253`, `:279–304`; `stage_1_claim_records.md:590–619` — and my independent census reproduces the field distribution 6-for-6 (§2) |
| **B-2b** — a withdrawn instruction printed as governing (COR-03) | 8 | **CLOSED** | `_parts/U_CONCORDANCE.md:16–25` (SUPERSESSION NOTICE heading the file) + `:59` (in-cell, with the retired clause left standing); `adversarial_review.md:34` (in-cell, 8 pipes preserved); `CORRECTIONS.md:13–16`, `:210`; `context_appendices.md:597`. Every external coordinate in the new notice re-read by me against the filings (§1.3, §7.2) |
| **B-3** — a false equation live in a volume of the report | 4 | **CLOSED** | `_parts/s1_p4.md:106–114` (filed two-line form; false form named inside its retraction) · `stage_1.md:1012` · `quantitative.csv:66` · `validation.csv:17` · `_parts/s1_p4.md:493`. Sweep §1.4: 4 occurrences of the `=944` form, **0 live**; filed terms re-read at orig. ll.3560–3562 / 3556–3559 / 4294–4296 / 4300–4302 |
| **B-4** — closure assertions must be re-derived, not re-argued | 13 | **CLOSED IN THE CORPUS / CLOSED-WRONG IN THE LOG** | Corpus: all four false closure sentences fixed and their own coordinates re-verified by me — `_MANIFEST.md:39` (four items listed, and `context_appendices.md:623/628/641` = §J and `:467` = §G, both true), `CORRECTIONS.md:296–298` ("five" over a list of five), `stage_1_claim_records.md:592` (49 reproduces). Log: `audit7_repairs.md:69–70` asserts "before 170 … the 4 added occurrences" where the before-state is **121** and the delta **+53**, and `:154` names the wrong CSV field (`notes` for `independence_note`). §1.5, §7.6–§7.7, and **RD-057** |

**Part 2 — the two questions no earlier pass asked, and what the answers cost**

| Test | Result | Where |
|---|---|---|
| Cold-reader test (would a reader arriving cold be misled before the correction arrives?) | **1 new live defect class found, in the first 4 lines of two batch-1 deliverables**: `adversarial_review.md:3` and `stage_1_claim_records.md:4` still date Stage 1 to **1993**, the barred boundary re-based at `stage_1.md:92–98` (RD-020/021) and contradicted by the first file's own verdict row `adversarial_review.md:35`. Three further cold-reader hazards named as residuals | § Cold-reader test |
| Addendum re-read (do the repair addenda themselves assert anything false?) | **5 assertions that do not hold or overstate, all in the two QC sheets, none inside a Stage-1 deliverable's addendum**: `audit7_repairs.md:69–70` (the "170 before / +4 added" arithmetic), `:69–70` again (a classifier output reported as a result), `:154` (the `notes` field name); `amazon_s1_audit4_audit5_final.md:498` ("eleven citations" enumerating fourteen) and `:508` ("anywhere in the corpus" over-stating AUDIT 7's check). Everything else held — 40+ coordinates re-read against `sources/`, none wrong | § Addendum re-read (§7.1–§7.7) |
| Shared blind spot in the instrument itself | The ±320-char negation-window classifier — used by AUDIT 7, by the third pass, and re-run by me — **cannot separate the broken state from the fixed one**: with my marker list it raises **0** occurrences on the pre-repair disk, which contained four live sites; with the pass's *declared* list it raises 14 before and 12 after, a two-site movement across a repair that eliminated every live instance. My verdict therefore rests on the structural census and on reading, not on the count | §1.6, §7.6 |

**Tally: 4 blockers — 3 CLOSED, 1 CLOSED IN THE CORPUS with a false account of itself in the repair log.
Nothing OVERCORRECTED: all 25 deleted lines (23 in the eleven Stage-1 files, 2 in the audit sheet) audited one by one, every one re-emitted with its retired text quoted
inside the replacement; 0 value/unit/date/class/confidence changes on any Stage-1 row or record; no verdict
erased; `quantitative.csv` L35 still holds `976000` with its `UNKNOWN` composition, and the 11-at-1995-12-31
ruling, COR-12, and the 43%/41% version pair all stand unmoved.**

---

## 3. Blocker grading, one by one

*(Placed immediately after the verdict table because it is the grading the gate turns on; §§1–2 below carry the raw
measurements it cites, and every `§1.x` / `§2` reference in this section points backward to them.)*

### 3.1 B-1 (item 6) — the retracted share-count leg — **CLOSED**

**What had to be true:** the pair `$871,000 / $976,408` (with `2,613,000` behind it) appears nowhere as a live
value, in no Value column, in no cell, in no correction voice. **What is true:** §1.1, three independent tests
(occurrence-window, CSV field census, markdown cell census) → 0 live.

The four AUDIT-7 sites are closed in the only acceptable shape, and I checked the shape, not just the claim:

| Site | Standing footer | Addendum appended below it | Retired limbs quoted verbatim? | Substituted? |
|---|---|---|---|---|
| `_parts/s1_p1.md` | `:142` untouched | `:144–163` | "**The one-third leg is $871,000** (`2,613,000 ÷ 3`, orig. l.4301–4302)" quoted, then withdrawn | **No** — "NO THIRD NUMBER IS SUBSTITUTED"; fourth leg UNKNOWN |
| `_parts/s1_p3.md` | `:180` untouched | `:182–199` | same, plus the "$24 gap accounted for rather than plugged" limb | No |
| `research/E_supply_ops_finance.md` | `:562` untouched | `:564–581` | limbs (2) and the leg withdrawn; **(1) and (3) expressly declared standing** (the 43%/41% version pair and the option-cash demotion) — so a true claim was *not* collateral-damaged | No |
| `_parts/NUMBER_DEFECTS.md` | `:68–78`, `:86–97` | `:112–154` + in-cell `:27`, `:28` | all three limbs quoted then withdrawn; the citation retracted separately at `:133–138` | No — `:140–143` restates only what still instructs correctly |

**The failure AUDIT 7 named was working the list instead of sweeping the siblings. This pass swept, and I can show
it caught something the list did not contain:** `_parts/NUMBER_DEFECTS.md:86–97` — the ROUND-2 bullet asserting that
`stage_1.md` §K **prints** the composition at $976,408 and that claim-record P09 **carries** it. Both descriptions
were false, neither was in AUDIT 7's site list, and both are now marked in place (`:90–97`) with the true state
(§K at `stage_1.md:610` withdraws the total; P09 at `stage_1_claim_records.md:466` carries the withdrawal). I
verified both canonical lines myself rather than taking the marker's word.

**Overcorrection test on B-1:** the retraction sentences assert no unsupported number of their own. Every figure
inside them is either the filing's (`$5,408 / $150,000 / $50,000 / $105,408 / 3,021,000 / 23 / $.3333 /
$1,007,000 / 2,811,000 ÷ 3 = 937,000`, all re-derived at §1.4), or a *named* retracted value quoted as retracted,
or the `0 occurrences` census claim, which I re-ran over all 60 `.txt` files in `sources/` and it is **0 for
`2,613,000` and `2613000` everywhere**, with `3,021,000` present in 9 files as positive control. One sentence in
one addendum overstates its own footprint (`audit7_repairs.md:69–70`, §1.5) — that is the log, not the retraction.

### 3.2 B-2a (items 9 and 12) — lineage demotion and attack A-B1 — **CLOSED**

Independently re-measured, not inherited: the live `Corroboration:` population is **49 fields, none above 3, and
the two at 3 are `L06` and `M05`** with their reasons on the record — my census reproduces the third pass's
distribution exactly (40/4/3/2/0) and its two secondary counts (55 on record-header lines, 63 corpus-wide). The
one-instrument premise is proved from cached filings at `stage_1.md:63–73`, and every citation in that block lands:
I re-read original l.49 and l.77, No. 3 l.49/79/5112, No. 5 l.49/70/79/5106 with `<TYPE>EX-23.1` at l.5091, 424B1
l.66/92, 10-K405 l.2913/3105 — fourteen coordinates, all correct (§7.3 on the word "eleven").

**The narrowing the brief asked me to test for softening:** `stage_1.md:63–64` was reduced from "carries … on its
own face" to "carried on its own face by the four S-1-family documents and cited by incorporation by reference in
the FY1997 10-K405, whose own face number is `000-22513`". I verified that this is a *precision gain, not a dodge*:
face numbers are `333-23795` at original/No. 3/No. 5 l.49 and 424B1 l.66 ✓; `000-22513` at 10-K405 l.50 (repeated
l.90) ✓; `333-23795` occurs **exactly twice** in the 10-K405, at l.2913 and l.3105 ✓. Nothing was weakened to evade
an attack: the lineage conclusion is unchanged and the file-number count is unchanged.

### 3.3 B-2b (item 8) — COR-03's supersession — **CLOSED**

39 occurrences, none governing unrouted (§1.3). The shape is the one this gate demanded: the retired clause stays
printed inside a cell that withdraws it, and the file now warns top-down before the table (`_parts/U_CONCORDANCE.md:16–25`).
Two things I checked that the pass did not claim: (a) the U.17 row's pipe count is uniform with the rest of its
table, so the 1,900-char insert did not break the register's parse (§7.4); (b) every external coordinate asserted
in the notice and the cell resolves — `stage_1.md:896` §P42 and `:1169` §R both print "11 employees at 1995-12-31";
No. 3 l.797 and No. 5 l.796 both carry "…expanded from 11 to 256 employees"; original l.667 carries the 1996-01-01
form; original l.2364 attaches "full-time" to the 151 only; `CORRECTIONS.md:210` routes to COR-12; `conflicts.csv`
U.17 contains "is WITHDRAWN and must not be followed".

**One honest qualification**, carried as **RD-051**: inside the U.17 cell a reader meets "COR-03 / COR-11.2
govern" at offset 131 of the cell and travels **766 characters** before the withdrawal marker opens at offset 897
(measured, `E:\tmp\qoder_audit8\arity8.py`). The stricter reading of "no live governing reference" would call that
still-live. I do not: the cell is one table row, the file heads with the notice, and
`conflicts.csv` is the named authority. But this is the shape that produced the last three refusals, and the next
edit to that row should put the marker first.

### 3.4 B-3 (item 4) — the dead bridge — **CLOSED**

Zero live copies of the false form (§1.4), and the replacement is the filing's own two-line statement with each
term on the line cited. No substitution: `quantitative.csv:66` and `validation.csv:17` both state that both
endpoints are filed, so the closure needed no invented number. The one live-looking hit in the whole family —
`_parts/NUMBER_DEFECTS.md:55`'s "the cash bridge 52 − 232 − 52 + 1,228 = 996" listed under *Not defects — verified
correct* — is arithmetically true (I evaluated it: 996) and is the opening-inclusive reading, so it is correctly
placed. AUDIT 7's "one flagged LIVE is a false positive of my classifier" is confirmed from the other side: the
`=996` form is legitimate and the `=944` form is extinct.

### 3.5 B-4 (item 13) — closure assertions re-derived — **CLOSED IN THE CORPUS, CLOSED-WRONG IN THE LOG**

Corpus side, all four sentences fixed and *their own coordinates checked by me* (the thing AUDIT 7 said nobody
did): `_MANIFEST.md:39` now says four and lists four, and its new proof coordinates are true — `context_appendices.md:623`
is `## J. Data gaps and contested figures`, `:628` is its header row, `:641` is the `#`-12 row, and `:467` is
`## G. Institutional support environment` and does not contain it. `CORRECTIONS.md:296–298` says five and the list
it prints has five items. `stage_1_claim_records.md:592` says 49 and my census gives 49.

Log side: the third pass's own summary of its sweep is wrong in one arithmetic claim and one field name
(`audit7_repairs.md:69–70` "before … 170 … the 4 added occurrences"; `:154` "`notes` field"), and the two older
closure sheets it declined still certify overturned work — with one **new** fact I measured that neither AUDIT 6
nor AUDIT 7 recorded: `amazon_s1_numeric_closure_final.md:17`'s coordinate list "**stage_1.md ll. 939–941, 1037,
1488, 1157**" points at six lines, **none of which contains any figure in the retracted family** (they hold d4's
$100,020 correction, a stub-period note, the U.8 heading and a salary-UNKNOWN row). A closure sentence whose
evidence pointers do not resolve is the same defect the gate has refused three times, sitting in the sheet whose
job is to certify pointers. Non-blocking for Stage 1's content; blocking for the *next* closure claim, hence
**RD-050** below.


## 1. Independent re-run of the third pass's own sweeps

### 1.1 S1 — the retracted share-count leg (`871,000 / 871,024 / 976,408 / 2,613,000`)

Their command, re-executed verbatim, then my own occurrence-level classifier (`E:\tmp\qoder_audit8\s1_leg.py`,
±320-char negation window, same family as AUDIT 7's `bridge.py`):

```
$ grep -rn -E "871,000|871,024|976,408|2,613,000|2613000|976408" \
    --include=*.md --include=*.csv company_001_amazon | grep -v -E "stage_2|s2_|ST2_|_EVIDENCE_CACHE" | wc -l
81                                                   # matching LINES
$ <same pattern, occurrence-level, Stage-1 scope>     179                  # OCCURRENCES
$ <occurrences, whole folder incl. Stage 2>           284                  # 105 of them Stage-2
$ <Stage-1 occurrences with NO retraction marker in +/-320 chars>  1
```

**My tally vs theirs: 179 occurrences, not 174.** Their "before → after" of 170 → 174 does not reproduce from a
clean shell under the convention that yields their 4-live-site finding; the delta is +5, and the four new
retraction sentences they say they added are in there (I count 13 occurrences inside the four AUDIT-7 addenda).
The count discrepancy is reported as a sweep-log defect (§1.5); it is not a data defect, because the substantive
claim — **zero live copies** — I tested independently and it holds.

**The single occurrence my classifier raised, read by hand:** `stage_1.md:1539` — "**The label "unaffiliated"
belongs to the filed 2,811,000 and to nothing else** — using it of `2,613,000` collided with the only
unaffiliated count on the record, and that misuse retires with the figure." This is inside §U.8's
RETRACTED-FIGURE RECORD (l.1559 onward is that record's own heading; the passage l.1520–1543 is the
best-supported-interpretation block that retracts both figures). Classified **RETRACTION-FRAMED**: the verb is
"retires", the figure is named as the misuse. My marker list lacks "retire"; the occurrence is a false positive of
my own classifier, and I say so rather than counting it as damage.

**The brief's stricter rule — "treat any occurrence in a Value column or a table cell as LIVE" — I ran as a
separate structural test** (`E:\tmp\qoder_audit8\s1_structural.py`), because a ±320-char window can be satisfied by
a neighbour's retraction while the cell itself still asserts:

* **CSV registers:** 34 occurrences, in `conflicts.csv` (r9 `evidence_weight`, r108 `claim_a`, r114
  `best_supported_interpretation`), `data_gaps.csv` (r11 `best_available_evidence`, r30, r43), `quantitative.csv`
  (r35 `notes`, r172 `notes`). **None sits in a `value`, `unit`, `date` or `evidence_class` field.** Every one of
  them sits in a sentence that names it retracted — `quantitative.csv` L35's `notes` reads "…COMPOSITION (verify-3
  F-3 / RD-031 rewrite): the residual is NOT explained by option cash … Only THREE legs of it are filed … =
  $105,408", and `data_gaps.csv` r11's `best_available_evidence` carries "**THE FOURTH LEG IS UNKNOWN, and so is the
  amount of the balance it stood for**". L35's **`value` field is `976000`**, i.e. the surviving band, not the
  retracted `976408`.
* **One register cell my window-score accepted and I would not have left had I not read it:** `data_gaps.csv:43`
  (`stage=stage2`) matched "retraction language" only because the word *retracted* is in it. What the cell asserts is
  **false as worded**: its `gap` field reads "`context_appendices.md` **still prints** the retracted 2613000 and
  871000 (REGISTER DEFECT, recorded and **not fixed**)", while the same row's `why_missing` explains that "the
  figures appear twice each **inside a row that LABELS them retracted**" and its `confidence` reads "High (that the
  residue is present **and labelled**)". The row contradicts itself — `context_appendices.md:598` and `:641` print
  both figures only inside labelled RETRACTION sentences, which is what §1.1 established — so "still prints / not
  fixed" is a stale accusation, and its `follow_up_task` orders an orchestrator to re-parse `quantitative.csv` for
  the pair. **Recorded as RD-054** (a Stage-2-tagged row, so its owner is the Stage-2 pass, not this gate). It is
  also the cleanest illustration of the instrument problem in §1.6 / §7.7: **the token "retracted" makes a false
  sentence look like a retraction — to their classifier, and to mine until I read the cell.**
* **Markdown table rows** (`|` ≥ 2 on the hit line): 11 rows across `_MANIFEST.md` (l.39, l.68),
  `_parts/NUMBER_DEFECTS.md` (l.27, l.28), `context_appendices.md` (l.598, l.641), `stage_1.md` (l.242, l.610,
  l.874, l.1179, l.1187, l.1207). **Each carries the withdrawal inside the same cell**, not in a neighbouring
  cell: NUMBER_DEFECTS l.27–28 now read "**[THAT FOURTH LEG IS WITHDRAWN 2026-09-25 …]**" /
  "**[THE THIRD TERM OF THAT INSTRUCTION IS WITHDRAWN 2026-09-25 — do NOT substitute ≈$871,000 …]**", which is the
  row-level fix AUDIT 7 said was missing when the only marker was 85 lines below.

**Verdict on S1: the retracted leg is 0 live under my own classifier and under the stricter structural rule.** The
four AUDIT-7 sites (`_parts/s1_p1.md:142`, `_parts/s1_p3.md:180`, `research/E_supply_ops_finance.md:562`,
`_parts/NUMBER_DEFECTS.md:68–78`) each still print the retired pair **inside a standing footer**, and each now
carries an appended addendum that quotes the footer's limbs verbatim and withdraws them — I read all four addenda
end to end at §3.1 and §7.4 and re-derived every claim in them.

### 1.2 S2 — the `orig. l.4301–4302` citation family

Their narrow grep re-executed (`grep -rnoE "l\.430[01][–-]430[12]|ll\.4300[–-]4302"`): **43** matches corpus-wide.
My wider classifier (`s2_citation.py`, any `43xx` line citation in the 4300–4309 band): **39 occurrences across 38
lines in Stage-1 scope**, plus 6 in Stage-2 scope. Their "37 citation occurrences" does not reproduce under either
convention; the nearest form is 38 Stage-1 lines. Reported at §1.5.

Co-occurrence test — is `2,613,000` within ±320 chars of a 4300–4302 citation, and is that citation offered *for*
it? My count is **16** co-occurrences (they claim 25), **all 16 with retraction language in the same window**,
which I read individually rather than trusting the window:
`conflicts.csv:9`, `quantitative.csv:172`, `stage_1.md:1566`, `stage_1_claim_records.md:466`,
`research/E_supply_ops_finance.md:562,566,569`, `_parts/NUMBER_DEFECTS.md:133,134`,
`_parts/s1_p1.md:142,147,149`, `_parts/s1_p3.md:180,185,187`, `_parts/s1_p4.md:490`. Every one either (a) quotes
the line for what it actually contains, or (b) is the withdrawing sentence.

**Ground truth, read from the filing myself** (`sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt`):

```
4300   4. Between December 6, 1995 and May 16, 1996, the registrant issued an
4301   aggregate of 3,021,000 shares of Common Stock to 23 investors for a
4302   consideration of approximately $.3333 per share, or an aggregate of $1,007,000.
```

* `2,613,000` / `2613000`: **0 occurrences in every `.txt` in `sources/`** — all 60 of them, not just the four
  cited documents. Positive control `3,021,000`: present in 9 files including the original, all six amendments and
  the FY1997 10-K405 cache set.
* Therefore the third pass's withdrawal is **correct in substance and the quotation in every addendum is exact**
  (I compared the quoted sentence against l.4300–4302 word for word).
* The **withdrawn-with-nothing-substituted** requirement is met: each addendum states "**NO THIRD NUMBER IS
  SUBSTITUTED**" / "the fourth leg is UNKNOWN", and `_parts/NUMBER_DEFECTS.md:140–143` re-states only what the
  register still instructs correctly (`≈$976,000 (±$1,000)`, identity UNKNOWN, option-cash clause struck, filed legs
  `$5,408 + $150,000 − $50,000 = $105,408`). I re-derived `105408` ✓ and checked orig. l.3560–3562 really files
  "Exercise of common stock options … 120,000 … --" i.e. **$0** of option cash ✓.

**Verdict on S2: CLOSED.** One caveat that a cold reader needs (§1.6, and §3.1): the citation string survives 37
times in
Stage-1 files, and 23 of those cite the line for the **filed** program figures, which is legitimate. Distinguishing
the two requires reading the sentence, and every one of the 23 that I sampled is legitimate.

### 1.3 S3 — COR-03 as governing

`grep -rn "COR-03"` Stage-1 scope = **33 lines / 41 occurrences**; corpus = **42 lines / 51 occurrences**
(Stage-2 scope 10 occurrences: `stage_2_part_3.md:925`, `_parts/s2_p4.md:1298` = "as COR-03 already said", unrouted,
plus 8 elsewhere in Stage 2). **Their "39 occurrences after the repair, 36 routed, classifier raised 3" does not
reproduce** on any of the four conventions above — nearest is my 41/33. Reported at §1.5.

My classifier raised 4 Stage-1 occurrences with no supersession marker in ±320 chars. I read all four:

| Site | Text | My classification |
|---|---|---|
| `context_appendices.md:597` | "…**[COR-12, which supersedes COR-03]**… COR-03 had treated that phrasing as the only filed wording and so **over-claimed**" | routed — the 320-char window simply misses the marker at offset 130 of a 1,404-char cell; in-cell supersession is explicit |
| `CORRECTIONS.md:253` | "**COR-03's error:** …" inside COR-12 | the superseding text itself |
| `_parts/s1_p3b_H_addendum.md:131` | "already in §B/§J/§R **with COR-03's phrasing**" | describes merge-time state; a `[SUPERSESSION MARKER, added 2026-09-24.]` paragraph sits at `:136–142`, 5 lines below, and I verified the sentence at `:131–134` reads whole (AUDIT 7's IR-08 worry) |
| `_parts/U_CONCORDANCE.md:59` | U.17 cell opens "**COR-03 / COR-11.2 govern.**" | **retained original clause with the withdrawal appended 766 characters later in the SAME cell**, plus a SUPERSESSION NOTICE heading the file at `:16–25`. This is the one site where a reader inside the cell travels three-quarters of the cell before being warned — graded at §3.3 as a cold-reader residual (**RD-051**), not a live governing reference |

I verified every load-bearing claim in the U.17 cell's correction against the filings rather than against the log:
`S-1/A No. 3 l.797` and `S-1/A No. 5 l.796` both read "…31, 1995 to March 31, 1997, the Company expanded from 11 to
256 employees" ✓; original S-1 `l.667` "…1, 1996 to December 31, 1996, the Company expanded from 11 to 151
employees" ✓; `l.2364` "As of December 31, 1996, the Company employed 151 full-time employees" ✓ (so "full-time"
attaches only to the 151 ✓); `CORRECTIONS.md:210` routes to COR-12 ✓; `conflicts.csv` U.17 carries "is WITHDRAWN
and must not be followed" and RD-032 ✓; §P42 at `stage_1.md:896` and §R at `stage_1.md:1169` print **"11 employees
at 1995-12-31"** ✓; `quantitative.csv` L74 = `stage1 / 1995-12-31 / Employees at the Stage-1 boundary / 11 /
persons / FACT / High` ✓.

**Verdict on S3: CLOSED as a class in Stage 1**, with the concordance cell graded at §3.3 (blocker B-2b) and the two
Stage-2 "as COR-03 already said" copies confirmed as real and correctly routed out of my gate (Declined-item
adjudication, item 6 / **RD-054**).

### 1.4 The false cash bridge and the other retraction-only families

Newline-normalised sweep over every `.md`, `.csv` **and `.txt`** under the company folder, Stage 2 included
(`E:\tmp\qoder_audit8\bridge_and_retonly.py`), pattern
`52 [−-] 232 [−-] 52 [+] 1,?228` with the equality captured:

```
occurrences of the LHS string anywhere          : 7
occurrences of the FALSE form  "… = +944"       : 4     live: 0
occurrences of the TRUE  form  "… = 996"        : 3     (arithmetically correct: 52-232-52+1228 = 996)
```

The four `= 944` copies, each read with its sentence:
`_parts/s1_p4.md:112` ("**The form removed reads** `52 − 232 − 52 + 1,228 = +944`, whose left-hand side is 996,
not 944"), `_parts/s1_p4.md:493` (AUDIT-6 addendum naming the same), `stage_1.md:1012` (§P.2 d14, "The deleted
form read …"), `quantitative.csv:66` (notes: "this cell read … for three repair rounds, **and the equation is
false**"). **Zero live copies. Their "4 occurrences, 0 live" reproduces exactly.**

`21,382.98`: **3 lines** — `quantitative.csv:112`, `stage_1.md:1087`, `1088` — all inside the correction naming it
a truncation (`511,000 ÷ 23.8975 = 21,382.9899`, which rounds to 21,382.99). Reproduced.

**The filed terms, re-read by me, not inherited** (`sources/S-1_original…txt`): l.3560–3562 "Exercise of common
stock options … 120,000 … --" → 1995 option proceeds filed at **$0** ✓; l.3556–3559 "Advances received for common
stock … 150 … 150" ✓; l.4294–4296 the 42,000-share / $.1287 / **$5,408** August-1995 purchase ✓; l.4300–4302 the
3,021,000 / 23 / $.3333 / $1,007,000 program ✓. Arithmetic: `5,408 + 150,000 − 50,000 = 105,408` ✓;
`1,272,000 − 295,568 = 976,432` ✓; `3,021,000 ÷ 3 = 1,007,000` ✓; `2,811,000 ÷ 3 = 937,000` ✓;
`5,408 + 150,000 + 937,000 − 50,000 = 1,042,408`, overshoot vs 976,432 = **65,976** ≈ the stated ≈$66,000 ✓;
`4,235,244 − 582,528 − 847,716 − 42,000 = 2,763,000`, less 150,000 = `2,613,000` ✓ (arithmetically alive,
denominator unfiled — the exact shape every addendum now states); `582,528 × 0.1717 = 100,020.0576`,
`847,716 × 0.1717 = 145,552.8372`, sum + 49,995 = **295,567.8948** ✓; `0.3333/0.1717 − 1 = 94.1176%` and
`(1,007,000/3,021,000)/0.1717 − 1 = 94.1371%` ✓ (so +94.1 and not +95.2); `569,396 × 14.05 = 8,000,013.80` ✓.

### 1.5 What reproduces from the third pass's sweep log, and what does not

Its §Sweep log printed four headline numbers. I re-derived each against the **pre-repair blobs**
(`git show 4a48648^:<path>`) and the current disk, sweeping for the convention that yields them
(`E:\tmp\qoder_audit8\conventions.py`, `cooc.py`, `before_after.py`). The convention that reproduces them is
**occurrences, not lines, over Stage-1 files only, with `_MANIFEST.md` excluded** — a convention the sheet never
states. Under it:

| Their printed claim | My re-run under that convention | Reproduces? |
|---|---|---|
| "After: **174 occurrences** / 0 unclassified" (leg family) | **174** (179 if `_MANIFEST.md`'s 5 are counted) | **YES** |
| "**37** citation occurrences" (the l.430x family) | **37** | **YES** |
| "**25** co-occurrences of `2,613,000` with that citation … all 25 sit inside a retraction" | **25**, **25** with retraction language (`_parts/s1_p1.md` 5, `_parts/s1_p3.md` 5, `research/E_supply_ops_finance.md` 5, `stage_1.md` 3, `conflicts.csv` 2, `stage_1_claim_records.md` 2, `_parts/NUMBER_DEFECTS.md` 1, `_parts/s1_p4.md` 1, `quantitative.csv` 1) | **YES** |
| "**39** occurrences [COR-03] … the classifier raised 3" | **39** (41 with `_MANIFEST.md`); my classifier raised 4 and all 4 are routing/demotion text — the extra one is `context_appendices.md:597`, whose in-cell marker simply sits outside a ±320 window on a 1,404-char cell | **YES** (count), with one extra site I read and dismiss |
| "Before this pass: **170 occurrences** / 4 unclassified live sites … the 4 added occurrences are the new retraction sentences themselves" | Before-state occurrences under their convention = **121**, not 170; the after-state is **+53**, not +4, because the four new addendum bodies themselves quote the pair repeatedly. And "4 unclassified / 0 unclassified" is the **human-adjudicated live set** (AUDIT 7's four sites), not the window classifier's raw output — re-run with their declared marker list it raises **14 before / 12 after** (§7.6) | **NO — the arithmetic and the label are both false** |
| The four live sites, and "AUDIT 7's four, reproduced exactly" | I located exactly those four in the pre-repair blobs (`_parts/s1_p1.md:142`, `_parts/s1_p3.md:180`, `research/E_supply_ops_finance.md:562`, `_parts/NUMBER_DEFECTS.md:68–74`) | **YES** |
| Deletion audit (`git diff --numstat`, 12 files) | **Every pair reproduces exactly**: 21/0, 18/0, 19/0, 11/11, 4/1, 3/3, 1/1, 13/1, 58/4, 16/1, 56/2 (`E:\tmp\qoder_audit8\deletion_audit.py`, line-by-line) | **YES** |
| "Nothing deleted … every 'deleted' line is a line rewritten in place with its retired text quoted" | 23 deleted lines across the eleven Stage-1 files (+2 in the audit sheet), the eleven numstat pairs reproducing exactly; each one I matched to a replacement carrying its own text — the sole mechanical miss is `CORRECTIONS.md` "four found by re-running its own phrase sweep", where "four" survives quoted inside the correction two lines above | **YES** |
| "one live 'on its own face' use narrowed … `_parts/s1_p4.md:287` left alone" | `grep -rn "own face"` Stage-1 scope now returns only `stage_1.md:63–64` (narrowed) and `sources.csv:51` (narrowed) | **YES** |

**So two sentences in the sweep log overstate it and the rest is sound.** The false arithmetic is precisely the
kind this gate exists to catch — a retraction sentence asserting an unsupported number about itself ("170 … the 4
added occurrences"; measured 121 and +53), and a classifier output ("4 unclassified → 0 unclassified") reported as
the instrument's result when the instrument with that marker list raises 14 → 12 (§7.6). Neither is load-bearing for
the verdict: **"0 live" is established by my structural test, by reading every table cell and register field that
carries the family, and by reading all four addenda end to end** — which is the standard the log should have claimed
instead of the one its classifier cannot meet. Carried as **RD-057** for correction by addition in
`audit7_repairs.md`.

### 1.6 The method every pass shared, which I will not certify as sufficient

Every pass in this chain, **including my own first draft of the S1 test**, used the same instrument: a
negation-window classifier that scores an occurrence as retraction-framed if a marker word sits within ±320
characters. I ran that classifier against the **pre-repair** disk to size its power. With my marker list it returned
**zero unclassified occurrences in the state that contained four live sites**; with the pass's own *declared* marker
list it returns **14 raised before and 12 after** — a 2-site movement across a repair that eliminated every live
instance (§7.6 has both runs and the reading of all 12). Either way the instrument cannot certify this defect: the
first result is a false clean, the second is a false positive list. The reason for the first is on one line of the
pre-repair `_parts/s1_p1.md:142`:

> "…and the disclosed-component composition foots to **$976,408** … The one-third leg **is $871,000**
> (`2,613,000 ÷ 3`, orig. l.4301–4302); the `$871,024` this figure family once carried is a **retracted
> back-solve** and appears only inside retraction sentences."

The live assertion and the word "retracted" sit forty characters apart, in the same sentence, and the window
test cannot tell them apart. **The classifier is insensitive to the exact defect it is used to certify**; it
passes the broken state and the fixed state identically. What actually distinguishes them is a structural and
semantic question — does the figure stand in the present indicative as *the corrected value*, and does the
withdrawal sit in the same cell? — which is why my verdict above rests on the field-level CSV census, the
pipe-row census, and reading all four addenda end to end, and not on the count. I recommend the next protocol
sheet retire the window count as evidence and keep it only as a triage list.

---

## 2. The invariants as they now stand on disk

All measured by me at `HEAD` (`E:\tmp\qoder_audit8\invariants.py`, `p2_r.py`). The Stage-2 repair agent was
appending during this run — `HEAD` moved from `4a48648` to `6b80495` mid-certification, and
`stage_2_part_3.md` is modified in the working tree — so I count Stage 1's subset for parity and report the totals I
actually see rather than expecting a fixed number.

| Invariant | My measurement | Third pass's claim | Holds |
|---|---|---|---|
| Stage-1 U-blocks ↔ `conflicts.csv` rows | `^\*\*U\.<n> — ` in `stage_1.md` → **43 blocks**, lines 1292…2303, ids **contiguous 1–43**, duplicates ∅, missing ∅; `conflicts.csv` rows with `stage=1` → **43**, ids 1–43 contiguous; **set parity both ways, orphans ∅** | 43 ↔ 43 | **YES** |
| Stage-2 ids unshifted and 1:1 | `conflicts.csv` now **113 data rows**: 43 × `stage=1` + **70 × stage≠1, ids U.44–U.113, no duplicates, none ≤43**; `stage_2_part_3.md` carries **70 `**U.n —` blocks, U.44–U.113** → blocks-only ∅, rows-only ∅ (the older `_parts/s2_p4.md` holds the U.44–U.111 subset, 68) | "conflicts.csv now carries 70 Stage-2 rows (U.44–U.113)" | **YES** |
| Nine registers parse at uniform field count | `sources 113×18 · quantitative 193×12 · timeline 116×11 · decisions 25×15 · validation 40×11 · failures 46×11 · channels 23×11 · conflicts 113×15 · data_gaps 45×8`; **every file's field-count map has exactly one key — 0 ragged rows**; **714 data rows total** | "0 ragged … 714 rows" | **YES — their nine-file arity table reproduces line for line** |
| Stage-1 subset of each register | **102 / 94 / 49 / 15 / 26 / 33 / 12 / 43 / 23** | same nine numbers | **YES, nine for nine** |
| `derived_arithmetic` on every DERIVED row | Stage-1-tagged: **26 DERIVED rows, 26 populated**; **0 empty DERIVED stage1 rows**; **0 non-DERIVED stage1 rows carrying arithmetic**; file-wide **50 DERIVED / 50 populated**, and **28 non-DERIVED rows** (lines ≥118, all Stage-2 band) carry arithmetic | 26/26; 0; 50/50 | **YES** |
| …recomputed | First-111-row block: **29 rows carry arithmetic, 29 of them class `DERIVED`** — i.e. `_MANIFEST.md:42`'s "exactly the **30** DERIVED/ESTIMATE/INFERENCE rows" is false by one row and false as to the 111 count (193 now) — which is the third pass's declined item 1, and it is real | declined, not edited | **Invariant holds; manifest sentence does not** |
| §P.2 recomputed | d-entry census over `stage_1.md:928–1100`: **32** distinct ids — `d1…d30` plus `d8a`, `d15a`, none of d1–d30 missing ✓. Machine-parsed every `a ± b (± c)… = r` string printed in the region: **13 equations, 11 foot exactly**, and the 2 that do not foot are **the quoted false bridge** (`52 − 232 − 52 + 1,228 = +944` → 996, i.e. the false form inside its own retraction — the expected non-foot) and one date-string parse artefact (`1995-12-31 = 184`). I re-derived 12 named terms by hand at §1.4, all footing | "32 entries, 12/12 spot-recomputes" | **YES** |
| §P.2 provably untouched by the third pass | `git show --numstat 4a48648 -- stage_1.md` = **11/11**, and `git show 4a48648 -- stage_1.md` returns **exactly one hunk**, `@@ -60,17 +60,17 @@`, i.e. ll. 63–73; file still **2,372 lines** ⇒ ll. 928–1100 are byte-identical | "single hunk at ll. 63–73 … 2,372 lines" | **YES** |
| §R's d-refs and U-refs resolve | §R at `stage_1.md:1160–1192` ✓; d-refs **{8a, 15a, 24, 25, 26, 30} = 6**, all defined in §P.2 ✓; U-refs **{1,7,8,9,10,11,17,20,22,23,25,26,27,28,39,40,43} = 17**, all resolving against the 43 blocks ✓, missing ∅ | identical | **YES** |
| False bridge has zero live copies | 4 occurrences of the `= 944` form, **0 live** (§1.4) | 4 / 0 | **YES** |
| Retracted leg has zero live copies | 174 / 179 occurrences, **0 live** by occurrence-window, **0 live** by the stricter cell/field rule (§1.1) | 174 / 0 | **YES** |
| `l.4301–4302` supports nothing unfiled | 37 citation occurrences; 25 co-occurrences with the unfiled denominator, all 25 in retractions; **0 live claims rest on it** (§1.2) | same | **YES** |
| COR-03 superseded everywhere in Stage 1 | 39 occurrences; 4 raised by my window, all 4 read and none governing (§1.3) | 39 / 3 raised | **YES** |
| Value / unit / date / class / confidence invariance | The third pass touched **no** register other than `sources.csv`, and its whole `sources.csv` diff is **one row (51, S0801) in one field** — but that field is **`independence_note`, not `notes`** as the sheet says; 114 rows × 18 fields both before and after. Registers carrying changed rows inside the same commit (`conflicts.csv`, `timeline.csv`, `data_gaps.csv`) are changed **only in `stage2`-tagged rows** — no Stage-1 row, value or confidence moved | "no value/unit/date/class/confidence changed; `sources.csv` edit is inside the `notes` field" | **YES on the substance; the field name in the sentence is wrong → §7.7 / RD-057** |
| Claim-record count | `grep -c "Claim:"` = **431**, and all 431 match a record-header form: **418 letter-ID records + 13 `U.n` records at ll. 559–571** ✓ exactly the third pass's self-caught side-effect census | 431 | **YES** |
| Live `Corroboration:` census | **49** live record-level fields; distribution **40 at 1, 4 at 0, 3 at 2, 2 at 3, none at 4**; ≥3 = **{L06, M05}**; 55 field-shaped occurrences on record-header lines; **63** corpus-wide. **Every number in R12's note reproduces exactly** | 49 / 40-4-3-2-0 / 55 / 63 | **YES — 6 for 6** |
| `_MANIFEST.md:40` element counts | `adversarial_review.md`: **30** `E-nn` rows; verdicts **4 well supported / 18 contested / 8 unsourced folklore** — reproduces exactly | 30 / 4-18-8 | **YES** |

## Declined-item adjudication

The third pass declined six items and said why. Declined items are how a gate passes in name only if the verifier
accepts the decline without measuring the item, so I counted each one myself first.

| # | Item | My own count / measurement | Blocks the gate? |
|---|---|---|---|
| 1 | `_MANIFEST.md:38` "432 claim records" | **431.** `grep -c "Claim:"` → 431; anchored record-header form → 431; split **418 letter-ID + 13 `U.n`** at `stage_1_claim_records.md:559–571`. The row is false by one record | **NO — named residual RD-052.** Inventory register, not the evidentiary spine; the ceilings it feeds (§9.1/§9.2) are word/byte ceilings, which it also misstates in the same row (49,258 vs 50,814 actual words for `stage_1.md`). Fix by addition before batch-1 handoff |
| 2 | `_MANIFEST.md:42` "exactly the **30** DERIVED/ESTIMATE/INFERENCE rows" and "111 data rows" | Over the first-111-row block: **29** rows carry `derived_arithmetic` and **all 29 are `DERIVED`** (the one `INFERENCE` row's string was relocated to `notes` by a repair AUDIT 6 graded correct). The file now holds **193** data rows, not 111 | **NO — named residual RD-052** (same row-class, same fix). Note the declined item is *doubly* false: the count and the population size |
| 3 | `stage_1.md:2358` "432 records … reconciled to the canonical U.1–U.42 spine" | **Inside the deliverable.** 431, and the U-range is U.1–U.43. The 2026-09-24 parenthetical fixes the range and then re-affirms the wrong tally: "**the record count is unchanged**" | **NO — but this is the item that comes closest to blocking.** It is the only known-false *count* left inside `stage_1.md`, and it sits in a paragraph a downstream agent treats as the file's self-description. **RD-053**, must-fix-before-upload |
| 4 | `_parts/U_CONCORDANCE.md:13` "Final count: **42** canonical conflicts (U.1–U.42)", and no U.43 row in the mapping table | **43** blocks, **43** stage-1 rows (my parity test). U.43 appears in the file exactly once, and only as a *part-local* AJ key at `:54` — the concordance has no U.43 row. A cold reader meets the false count at line 13, *before* the SUPERSESSION NOTICE at line 16, and the notice does not mention it | **NO — RD-051**, but named as the sharpest residual: the file's header is now "the designated authority for `Conflicts: U.n`", and its own count is stale one line above the warning |
| 5 | `amazon_s1_numeric_closure_final.md:17/:29/:42`, `amazon_s1_causal_lineage_closure.md:37/:86` | **All five live and uncorrected.** `:17` and `:29` are now *true on today's disk* (0 live leg; 0 live false bridge) though both were false when signed, and neither says so. `:42` R-4 is false in the other direction ("**still prints live** in `_parts/s1_p4.md` ll. 102–103" — it does not). **New:** `:17`'s four evidence coordinates (`stage_1.md` ll. 939–941, 1037, 1488, 1157) contain **none** of the figures they are offered for. `:37` tabulates `stage_1.md` at "**4**" demotion sites, "ll. 431, 560, 1203, 1280" — today the file carries **11** at ll. 241, 310, 457, 586, 896, 1169, 1233–1236, 1314; `:86` still certifies "all 31 named sites" | **NO — RD-050.** QC-layer sheets, superseded by `audit6`/`audit7` in the reading order, and the repairer disclaimed write authority. But the decline is now *materially understated*: these sheets not only assert overturned closures, they assert coordinates that do not resolve |
| 6 | Stage-2 files describing `context_appendices.md` as "still printing" the retracted pair (`_parts/s2_p1.md:6`, `stage_2_part_1.md:23`) | Confirmed both still read "no capital figure from `context_appendices.md`, **still printing** the retracted `2,613,000 / $871,000` (S2E-28)". **False of Stage 1 today**: `context_appendices.md:598` and `:641` are labelled retraction rows, and `:598` prints "NO COMPOSITION TOTAL IS PRINTED ON THIS ROW" | **NO for this gate — RD-054, routed to the Stage-2 owner, with a warning.** It is the same failure shape as my cold-reader finding (a false sentence in a *header* that outranks the body that corrects it), it is in a deliverable that is being written now, and Stage 2's own gate should refuse it if left standing |
| 7 | `adversarial_review.md` U-refs beyond the 43-row spine (declined: "a full re-key is its own work order") | The file references U.1 … U.50 — `U.49`, `U.50` exceed the spine — and its **header `:5–6` declares the local key**: "the 46 conflict-register items keyed at the end of `_parts/s1_claims_AJ.md` (**U.1–U.50**)". The one reference this pass had to resolve (`U.21` → canonical U.17) is disclosed in-cell at `:34` | **NO — RD-055**, and the decline is *better defended than it looks*: the file names its own key at the top. Residual risk is a reader quoting `U.49` into a spine query |

**Verdict on the declines:** six of the seven are legitimate scope discipline and none touches a stored figure. The
seventh (§1–2–3, the 432/30 counts) is a *class* the pass had already agreed was correctable — it fixed three
miscounts of exactly this shape at R10/R11/R12 and declined three others while confirming its own census proved them
false. That is a defensible scope call and an indefensible consistency call; it is why my decision below is
**with named residuals** rather than clean, and why RD-052/RD-053 carry a must-fix-before-upload condition rather
than a "later" flag.

## Cold-reader test

The brief's candidate class (a) is real, and it is not the one I expected. Every pass in this chain measured
occurrences; none read the openings. I took the first 40 lines of each Stage-1 deliverable and asked: **would a
reader who trusts what they have read so far be misled before the correction arrives?**

| File | First-40-line verdict | Evidence |
|---|---|---|
| `stage_1.md` | **Warned in time.** The stale spine count at `:7` is retracted at `:9–11`; the lineage ruling at `:39–48` opens by admitting its first statement was false; the boundary is correctly re-based at `:5` and `:92–98` | — |
| `context_appendices.md` | **Warned.** Its header itself records the 1993-boundary correction at `:17–23` | — |
| `CORRECTIONS.md` | **Warned.** `:13–16` promises "marked where they stand, not only where they were retired", and that promise is true as stated | — |
| `_MANIFEST.md` | **Misled, then re-misled.** The staleness disclosure at `:21–31` is honest and useful, but the register then prints "432 claim records" (`:38`), "111 data rows … exactly the 30" (`:42`), word counts ~2% low (`:37`), and "43 data rows" for a 113-row `conflicts.csv` (`:43`) | §Declined items 1–2, §7.5 |
| `_parts/NUMBER_DEFECTS.md` | **Warned at the row.** The retracted leg appears at `:27–28` inside the first 40 lines, but both cells carry in-cell WITHDRAWN markers — this is the pass's best cold-reader result, and it was not required by any named site | `_parts/NUMBER_DEFECTS.md:27`, `:28` |
| `_parts/U_CONCORDANCE.md` | **Misled for one line.** "Final count: **42** canonical conflicts" at `:13`, one line *above* the SUPERSESSION NOTICE at `:16` that does not mention the count | `:13` |
| `adversarial_review.md` | **MISLEAD, and uncorrected anywhere in the file.** `:3` "**Stage:** Amazon.com, Stage 1 (**1993** → 1995-12-31)" — the barred dating `stage_1.md:92–98` re-based (RD-020/021: "**no document in the record supports a 1993 origin**"). The file's own `:35` grades "Founded in **1993**" as **UNSOURCED FOLKLORE**, and no boundary note appears anywhere in its 242 lines | `adversarial_review.md:3` vs `:35`, `stage_1.md:92–98` |
| `stage_1_claim_records.md` | **MISLEAD in line 4.** "(**1993** idea formation → 1995-12-31; inception 1994-07-05)" — the same barred form, with the corrected 1994 span used by `stage_1.md:5`, `:1106` and the appendices. Its `:15` also keys every `Conflicts:` reference to "the canonical register **U.1–U.42**" | `stage_1_claim_records.md:4`, `:15` |
| `_parts/s1_p1.md:1`, `_parts/s1_p3.md:3`, `_parts/s1_p4.md:3`, `research/E_supply_ops_finance.md:3`, `research/A_corporate_historian.md:3`, `research/H_legal_organization.md:3` | Same barred "1993" opening in six working/dossier volumes. Those files carry "do not import figures" footers below them, but no boundary note | **RD-056** |

**What I conclude from it.** Three passes refused for "the sentences about the numbers were false" while all three
counted occurrences of retracted numerals; nobody read the openings, where a *false dating* — the one thing this
project's own audit-1 re-based, RD-020/021 — still prints as a header in two batch-1 deliverables and in `stage_1.md`'s
own companion register. It misleads a cold reader in line 3 or 4 and is contradicted by the file's own body 30 lines
later. It changes no stored figure and no evidence weight, so it does not reopen the four blockers — but it is the
clearest demonstration in this whole closure that occurrence-counting is not a substitute for reading, and it is the
reason my sign-off is conditional (**RD-056**, must-fix-before-upload, one line at each of the two deliverables,
`adversarial_review.md:3` and `stage_1_claim_records.md:4`).

## Addendum re-read

### 7.1 Method and scorecard

Candidate class (b) from the brief: nobody had re-read the repair prose for *new* false assertions. I read every
addendum the third pass wrote, in full, line by line — `_parts/s1_p1.md:144–163`, `_parts/s1_p3.md:182–199`,
`research/E_supply_ops_finance.md:564–581`, `_parts/NUMBER_DEFECTS.md:74–78`+`:90–97`+`:112–154`,
`_parts/U_CONCORDANCE.md:16–25`+`:59`, `adversarial_review.md:34`, `stage_1.md:63–73`, `sources.csv:51`,
`CORRECTIONS.md:296–298`, `stage_1_claim_records.md:592`+`:608–619`, `_MANIFEST.md:39`+`:67–68`, and
`amazon_s1_audit4_audit5_final.md:480–530` — and for each assertion asked whether a local artifact proves,
contradicts, or cannot reach it. **Scorecard: ~90 discrete assertions; 85 hold under my own re-derivation;
5 do not or overstate — all five in the two QC sheets, none inside a Stage-1 deliverable's addendum** (§7.7: the
"170 before / +4 added" arithmetic, the "4 unclassified / 0 unclassified" label, the `notes` field name; §7.3: the
"eleven citations" that enumerates fourteen and the "anywhere in the corpus" scope generalisation).

### 7.2 The concordance notice and the U.17 cell — every outward coordinate re-read

The notice asserts: COR-03 superseded by COR-12; the "print `11 (per the filing: at 1996-01-01)`" instruction
withdrawn; §P42 and §R Employees now print "11 employees at 1995-12-31"; the count is filed at that date by
S-1/A No. 3 l.797 and No. 5 l.796; `conflicts.csv` U.17 is the authority. **All six verified**: `stage_1.md:896`
(§P42) and `stage_1.md:1169` (§R) both say "11 employees at 1995-12-31"; `S-1A-No3…txt:797` and
`S-1A-No5…txt:796` both read "…31, 1995 to March 31, 1997, the Company expanded from 11 to **256** employees";
`conflicts.csv` U.17 carries "is WITHDRAWN and must not be followed" + RD-032; `CORRECTIONS.md:210` routes to
COR-12. The cell's own extra claims also hold: original S-1 `l.667` = the 1996-01-01 "11 to 151" sentence ✓, and
`l.2364` = "As of December 31, 1996, the Company employed **151 full-time** employees" ✓, which is what licenses
"the 'full-time' style attaches only to the 151". **No break found.**

### 7.3 The A-B1 closure addendum (`amazon_s1_audit4_audit5_final.md:480–530`)

The test I cared about was its own reproducible check: "Verify with
`grep -c "Corroboration: 1 (same lineage as S0801 — re-keyed" stage_1_claim_records.md` → 22; add the short form → 24."
**Run: 22 ✓. Short form: 2 records, `K04` and `P01` ✓. Total 24 ✓** — the 22-vs-24 reconciliation is arithmetically
exact. The eleven-citation claim was re-checked line by line against `sources/`: original `l.49`
`SEC FILE NUMBER: 333-23795` ✓, original `l.77` `REGISTRATION NO. 333-` (truncated exactly as filed — I read the raw
line: it does stop there) ✓, No. 3 `l.49`/`l.79`/`l.5112` ✓ (`l.5112` is inside Ernst & Young's consent, as the next
clause says), No. 5 `l.49`/`l.79`/`l.70`/`l.5106` ✓ and `<TYPE>EX-23.1` at `l.5091` ✓, 424B1 `l.66`/`l.92` ✓, 10-K405
`l.2913`/`l.3105` ✓. **Two imprecisions, no falsehood**: the addendum says "all eleven citations" and then enumerates
fourteen line coordinates (the eleven is inherited from AUDIT 7's eight-row table); and "the two `sources.csv` notes
… S0801 l. 51, S0803 l. 53" ✓ correct. Its verdict-preservation claim is true: `l.409` still opens "| A-B1 | … |
**YES** | Ruling required, not re-research…" and `l.431` still carries the original site list "ll. 417, 532, 1126,
1202; appendix ll. 406–407; 24 claim records"; the diff against `4a48648^` re-emits those two rows with appended
pointers and their verdict text intact (§2). **Its one generalisation is too wide**: "Zero confidence changes
**anywhere in the corpus**, verified field by field by AUDIT 7" — AUDIT 7 verified Stage-1 rows and the 431 records,
and expressly noted confidence values on the new U.44–U.113 rows. Nothing *changed*, so the claim survives on
"change", but the scope stated exceeds the scope checked. **RD-057**.

### 7.4 The four footer addenda, and the arity they had to preserve

Each footer addendum quotes its target verbatim, and I compared the quoted limbs character-for-character against the
standing footers: `_parts/s1_p1.md:146` quotes `:142`'s "the disclosed-component composition foots to
**$976,408** (a band-level tie, not an exact one)" and "The one-third leg **is $871,000** (`2,613,000 ÷ 3`, orig.
l.4301–4302)" ✓ both exact. The E-dossier addendum's declarations of what *stands* are true and were checked: limb
(1) at `research/E_supply_ops_finance.md:25` still carries the 43%/41% version pair ✓; limb (3)'s option-cash
withdrawal rests on orig. `l.3560–3562` = "Exercise of common stock options … 120,000 … --" ✓ i.e. **$0**, exactly
as claimed. `_parts/NUMBER_DEFECTS.md:145–147` makes a rare *self-locating* claim — that the two bullets its markers
point into "began at l. 68 and l. 82 before this pass" — and `git show 4a48648^` puts them at **68 and 82** ✓.
Arity after the 1,900-char in-cell insert: concordance mapping table 44 rows, **all 7 pipes** ✓;
`adversarial_review.md` §1 table all **8 pipes** ✓ — so R7's "row arity restored to 7 pipes after the first attempt
dropped one" and R8's "8/8 verified" are both true on disk.

### 7.5 `_MANIFEST.md:39`, `:67`, `:68` — the rows the pass wrote about its own work

`:39` is the strongest sentence in the closure: it names the miscount, re-counts the list, gives four coordinates for
the §J re-labelling and one for what §G actually is — and **all five resolve** (`context_appendices.md:623`, `:628`,
`:641`, `:467`, plus the four sites listed). `:67` now truthfully records that the concordance cell "printed the
retired COR-03 as governing **until 2026-09-25**" and that a notice heads the file. `:68` truthfully describes the
NUMBER_DEFECTS withdrawal **and prints two numbers that are no longer its own**: 3,348 words / 21,505 bytes against
**4,198 / 27,150** on disk — the row advertises "+ the AUDIT-7 addendum of 2026-09-25" while sizing the file as if
the addendum were not in it. Same in `:67` (5,143 / 32,280 vs 5,613 / 35,241), `:60` (`s1_p1.md` 4,278 / 27,599 vs
4,602 / 29,732), and `:62`, `:64`, `:78`, plus the two deliverable rows `:37`/`:38`. The register's own staleness
disclosure at `:21–31` covers "the ten files that the **AUDIT-6** repair pass edited" — the third pass grew ten more
and did not extend the disclosure, which is the "sweep scoped to the file open" mechanism one level up. Cosmetic (no
ceiling is approached: `stage_1.md` is 50,814 words = 85% of the 60,000 cap), so it is a residual, not a blocker.
**RD-052**.

**Verdict on B-4: CLOSED IN THE CORPUS, and the log's sweep statement about the same class does not fully
reproduce** — see §7.6, which sizes the classifier's discriminating power directly and finds one further false
`gap` statement in `data_gaps.csv`.

---

### 7.6 The classifier sized against the disk: a test no pass in this chain ran, and what it exposed

§1.6 asserted that the window classifier is insensitive to the defect it certifies. Since that claim reopens
RD-057 — the pass's own "174 occurrences / **0 unclassified**" — I measured it instead of arguing it
(`E:\tmp\qoder_audit8\their_classifier.py`, `before_live.py`: same ±320 window, occurrence-level, `_MANIFEST.md`
excluded, run against the pre-repair blobs and the repaired disk).

| Marker list used | BEFORE occurrences | BEFORE raised | AFTER occurrences | AFTER raised |
|---|---|---|---|---|
| **The pass's own declared list** (`retract, withdraw, supersed, not be followed, 0 times, no composition, unfiled, not adopted, audit-6/audit-7, do not import`, + the undeclared "…") | 121 | **14** | 174 | **12** |
| My broad synonym list (§1.1) | 121 | 0 | 174 | 1 (`stage_1.md:1539`) |

So the pass's *occurrence* figure reproduces (174) and its *live* finding matches AUDIT 7's four sites, but
**"0 unclassified" does not reproduce under the marker list it printed: 12 occurrences still raise**, and only its
closed "…" (an undeclared extension of the list) can close them. Three consequences, all of which I have to state
rather than smooth:

1. **The classifier is not a closure instrument.** Under its own declared list it moves 14 → 12 across a repair that
   eliminated every live instance — i.e. it registers about one-fifth of the change. The instrument every pass in
   this chain used to certify this defect is nearly blind to it. It was AUDIT 7's *reading* of four footers, not any
   count, that found B-1, and the third pass's own `data_gaps.csv` row 43 says so in its `why_missing` field:
   "**The figures appear twice each inside a row that LABELS them retracted, so a grep-based or copy-out register
   key cannot distinguish a retraction from an assertion.**" That sentence is the correct diagnosis of the method
   and it has been sitting in the register since before this pass ran.
2. **Every one of the 12 residual raises is benign — I read all of them**, and the repair's verdict survives the
   test I set it: `quantitative.csv:35` (`notes`: "…COMPOSITION … the residual is NOT explained by option cash …
   UNKNOWN"), `stage_1.md:1066–1067` ("THIS IS THE ONLY ROUTE BY WHICH `2,613,000` EVER ENTERED THE DOSSIER … which
   is why d8a's composition leg is now UNKNOWN"), `:1530` ("Neither the retired $976,408 composition total nor its
   … account survives"), `:1539` ("that misuse retires with the figure"), `:1567` (the CLAIM-B retraction),
   `_parts/NUMBER_DEFECTS.md:138` ("it supports **no** `2,613,000`"), and `data_gaps.csv:43`.
3. **One of those twelve is a genuine new defect, and it is not Stage 1's.** `data_gaps.csv:43`'s `gap` field reads:
   "**`context_appendices.md` still prints the retracted 2613000 and 871000 (REGISTER DEFECT, recorded and not
   fixed)**". That is false of Stage 1 on today's disk — `:598` prints "NO COMPOSITION TOTAL IS PRINTED ON THIS ROW"
   and both figures inside a labelled RETRACTION; the row's own `why_missing` explains exactly why it is false — and
   the row is `stage=stage2`, i.e. a Stage-2 register row accusing a Stage-1 deliverable of the defect Stage 1 has
   already closed. It is the third instance of RD-054 (after `_parts/s2_p1.md:6` and `stage_2_part_1.md:23`), and
   the first one living in a machine-read register, which is how a false accusation outlives the repair. Its
   `follow_up_task` tells the orchestrator to "parse quantitative.csv for 2613000 … and re-key any hit" — an
   instruction to re-litigate a closed site. **Added to RD-054, routed to the Stage-2 owner, with the same
   warning I gave for the headers.**

**What this does to my verdict.** It does not soften B-1's closure: the 0-live finding rests on the structural
tests and the reads, which survive. It does confirm RD-057 (the log overstates what its classifier can see), widens
RD-054, and it is the concrete answer to the brief's question — the shared class is *trusting an instrument that
cannot distinguish a retraction from an assertion, and never sizing it against a disk state known to be broken.*

### 7.7 The three assertions in the repair log that do not hold — all in the log, none in the corpus

1. **`audit7_repairs.md:69–70`** — "Before this pass: **170 occurrences** / 4 unclassified live sites … After: 174
   … The 4 added occurrences are the new retraction sentences themselves." Re-run against the pre-repair blobs under
   the pass's own convention: before = **121**, after = **174**, delta = **+53**. The retraction sentences did add
   more than four occurrences of the family, because each addendum quotes the retired pair repeatedly — correct
   practice, and the sentence understates its own footprint. **A false statement about the repair's own effect.**
2. **`audit7_repairs.md:154`** — "`sources.csv` edit is inside the `notes` field of S0801 only". The file has both a
   `notes` and an `independence_note` column; the diff moves **`independence_note`** and leaves `notes` untouched.
   Everything else in that row (114 rows × 18 fields, one row, one field, no value/class/confidence change) is true.
   **A false statement about the repair's own site.**
3. **The unsaid convention** — the sheet prints four occurrence counts without saying they exclude `_MANIFEST.md`
   and count occurrences rather than lines; three of the four reproduce only under that undeclared rule, and the
   fourth (item 1) reproduces under no rule at all. An auditor who does not reverse-engineer the convention gets
   "179 vs 174" and reports a false sweep — which is how this gate has spent three rounds. **RD-057** asks the sheet
   to state its convention on one line and correct items 1–2 by addition.

**What I could not break, stated plainly:** the retracted leg's four addenda, the concordance notice and cell, the
`adversarial_review` cell, the NUMBER_DEFECTS row-level markers, `CORRECTIONS.md:296–298`, the census note at
`stage_1_claim_records.md:608–619` (reproduces 6-for-6), the A-B1 addendum's 22/24 reconciliation, the narrowed
file-number clause, the deletion audit (all twelve numstat pairs; 25 deleted lines, none of them a lost claim), and
the eleven invariants.

## GATE DECISION

**SIGN WITH NAMED RESIDUALS.**

Stage 1's four blockers are closed on evidence I re-derived rather than inherited: the retracted equity leg is
0-live under three independent tests including the stricter cell/Value-column rule; the `l.4301–4302` citation is
withdrawn with **nothing substituted** and the fourth leg stands at UNKNOWN for a stated reason; COR-03's
supersession now routes through all 39 occurrences in Stage 1; the false bridge has zero live copies; and the whole
invariant layer holds — **43 ↔ 43** Stage-1 U-blocks/rows, contiguous 1–43, orphans ∅, with Stage 2's **70**
U.44–U.113 rows still 1:1 with their blocks; nine registers at uniform arity over **714** rows with the nine
Stage-1 subsets unchanged (**102/94/49/15/26/33/12/43/23**); `derived_arithmetic` **26/26** with 0 non-DERIVED
Stage-1 rows carrying it; §P.2 at **32** entries with every term I re-computed footing; §R's **6** d-refs and **17**
U-refs all resolving; the claim census at **431** (418 + 13) and the `Corroboration:` census at **49** with
distribution 40/4/3/2/0 reproducing exactly. **Nothing was overcorrected**: no value, unit, date, class or confidence
moved on any Stage-1 row or record; all 25 deleted lines audited one at a time, every one re-emitted with its retired
text quoted inside the replacement.

### Residuals (each a research-debt item; ids allocated from RD-050 — AUDIT 7's own "RD-042 id collision" remains unresolved and was not created here)

| RD | Residual | Site | Condition |
|---|---|---|---|
| **RD-050** | Two superseded QC closure sheets still certify overturned work, and now assert coordinates that do not resolve | `03_quality_control/amazon_s1_numeric_closure_final.md:17` (its four `stage_1.md` pointers carry none of the figures), `:29`, `:42`; `amazon_s1_causal_lineage_closure.md:37` ("4" sites at ll. 431/560/1203/1280 vs **11** actual), `:86` ("all 31 named sites") | correct **by addition**; sheet owners' work, not Stage 1's |
| **RD-051** | Concordance self-description stale, plus in-cell travel before the warning | `_parts/U_CONCORDANCE.md:13` "Final count: 42 canonical conflicts (U.1–U.42)" with no U.43 row; `:59` govern-clause at offset 131 vs withdrawal at offset 897 (766 chars) | one line each; put the marker before the clause at the next touch |
| **RD-052** | Inventory register's own numbers stale, including rows the third pass edited without re-sizing | `_MANIFEST.md:38` (432 vs **431**), `:42` (30 vs **29**; 111 vs 193), `:37`/`:43`/`:44`/`:45`/`:46`/`:60`/`:62`/`:64`/`:67`/`:68`/`:78` | must-fix before batch-1 handoff; no ceiling at risk |
| **RD-053** | A false count inside the deliverable, re-affirmed by its own corrective note | `stage_1.md:2358` "**432 records** … the record count is **unchanged**" (census 431); companion `stage_1_claim_records.md:15` "canonical register U.1–U.42" | **must-fix before upload** — the item closest to reopening |
| **RD-054** | Stage 2 still charges Stage 1 with a defect it has closed — in two headers **and in a machine-read register row** | `_parts/s2_p1.md:6`, `stage_2_part_1.md:23` "`context_appendices.md` **still printing** the retracted `2,613,000 / $871,000`"; **`data_gaps.csv:43` `gap` field: "`context_appendices.md` still prints the retracted 2613000 and 871000 (REGISTER DEFECT, recorded and not fixed)"** — false of `:598`/`:641`, which print both inside labelled RETRACTIONS, and self-refuted by that row's own `why_missing`; its `follow_up_task` orders a re-parse of `quantitative.csv` for the retracted pair. Also `stage_2_part_3.md:925`, `_parts/s2_p4.md:1298` "as COR-03 already said" | routed to the Stage-2 owner; **its gate should refuse if it stands** — a stale false accusation in a register outlives every footer fix |
| **RD-055** | Deliverable keyed partly to a local conflict register beyond the spine | `adversarial_review.md` refs to U.50 against a 43-row spine (its header `:5–6` does declare the local key) | re-key work order |
| **RD-056** | The **barred 1993 boundary still prints in cold-reader position**, contradicting `stage_1.md:92–98` (RD-020/021) | `adversarial_review.md:3`, `stage_1_claim_records.md:4`; also `_parts/s1_p1.md:1`, `s1_p2.md:3`, `s1_p3.md:3`, `s1_p4.md:3`, `research/E_supply_ops_finance.md:3`, `research/H_legal_organization.md:3`, `research/A_corporate_historian.md:3` | **must-fix before upload** for the two deliverables; one line each, mark not erase |
| **RD-057** | The repair log's account of its own sweep has two false specifics and one undeclared convention | `audit7_repairs.md:69–70` ("170 before", "+4 added"; measured **121** and **+53**), `:154` ("`notes` field"; it is `independence_note`), the unstated `_MANIFEST.md` exclusion behind 174/37/39; `:69–70`'s "4 unclassified / 0 unclassified" reported as a classifier result when the classifier with that marker list raises 14 before and 12 after (§7.6); `amazon_s1_audit4_audit5_final.md:498` "eleven" enumerating fourteen and "anywhere in the corpus" over-stating AUDIT 7's scope | correct by addition; state the convention |
| **RD-058** | Protocol defect: the negation-window classifier every pass used is insensitive to the defect it certifies | §1.6 — it scores the pre-repair disk (4 live sites) as 0 unclassified | amend `AUDIT_PROTOCOLS.md`: window counts are triage, never closure evidence |

Carried unchanged and still **UNTRIED**, because I made zero web requests and none of the verdicts above depends on
them: AUDIT 6's U-a (re-savability of the `restoration pending` §T items), U-b (whether 1998-12-12 is still the
earliest amazon.com root capture — the named CDX query), U-c (completeness of the 3,084-entry Mosaic mirror).

### What I tried that would have failed me

- I refused to accept any of the third pass's counts and re-ran all three sweeps plus the bridge and `21,382.98`
  sweeps from a clean shell. **This nearly failed me in their favour**: my first numbers (179 / 16 co-occurrences /
  41 COR-03) contradicted theirs (174 / 25 / 39), and I had a finding drafted before I noticed the convention
  difference — occurrences not lines, `_MANIFEST.md` excluded. Under their convention **three of the four reproduce
  exactly**, and the only one that does not is "before: 170". Had I stopped at my own default scope I would have
  refused the gate over my undocumented regex.
- I ran the brief's stricter rule (any table cell or Value column = LIVE) as a separate structural test instead of
  trusting the window, and then ran that window against the **pre-repair** disk to measure its power. That second
  move is what found RD-058: the classifier passes the broken state, so "0 unclassified" is not evidence, and I did
  not certify on it.
- I re-read every coordinate the addenda lean on (40+: filing lines, register rows, table cells, the two pre-pass
  bullet positions, the `context_appendices.md` §G/§J coordinates, the concordance's four printing sites, the A-B1
  citation block, `sources.csv:51/53`, `quantitative.csv` L35/L74/L99/L172) — which is how RD-050's non-resolving
  pointers and the §J re-labelling were both settled.
- I audited deletions line by line (25) rather than trusting `--numstat`, and audited what the footers declared
  *still standing* (the 43%/41% pair, the option-cash demotion, P36's `= 996`), because a pass that retracted a limb
  it never disputed would have been an overcorrection. This one did not.
- I read the openings of every Stage-1 volume, which found RD-056 — the one substantive defect in this closure that
  three earlier passes never saw, because it is not an occurrence of a retracted numeral.

**If the caller's policy is that any known-false count inside a batch-1 deliverable reopens the gate, this decision
flips on RD-053 (`stage_1.md:2358`, "432 records", twice independently measured as 431) and RD-056
(`adversarial_review.md:3` / `stage_1_claim_records.md:4`, the barred 1993 boundary in line 3 or 4).** I did not
reopen on them because neither is a stored figure, an evidence weight, or a conclusion; both are one-line
inventory/dating statements whose corrections already stand elsewhere in the same file or in the spine; and because
this pass behaved the opposite way to the three that were refused — it swept rather than worked the list, it found
and marked a sibling nobody named (`_parts/NUMBER_DEFECTS.md:86–97`), it substituted nothing where support is
absent, and every one of its invariant claims reproduced under my own parser.

**Certifier's attestation.** One file created: `founders_playbook/03_quality_control/audit8_stage1_certification.md`.
No existing file edited, moved or deleted; git used read-only (`log`, `status`, `show`, `diff`, `rev-parse`); scratch
at `E:\tmp\qoder_audit8\` (`s1_leg.py`, `s1_structural.py`, `s2_citation.py`, `s3_cor03.py`, `bridge_and_retonly.py`,
`invariants.py`, `p2_r.py`, `corcount8.py`, `conventions.py`, `cooc.py`, `before_after.py`, `deletion_audit.py`,
`arity8.py`, `manifest_counts.py`, `census_extra.py`, `before_live.py`); **web requests: 0**.



