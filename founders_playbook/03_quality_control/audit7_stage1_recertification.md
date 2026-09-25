# AUDIT 7 — INDEPENDENT RE-CERTIFICATION OF THE STAGE-1 REPAIRS (Amazon, company_001)

**My status.** I am the third pair of eyes. I did not write `audit6_stage1_independent_qa.md` (the verifier)
and I did not write `audit6_repairs.md` (the repairer). I change nothing.

**Read-only: YES.** I edited and deleted no existing file anywhere in `E:\founder's playbook`. The only file
created by this run is `founders_playbook/03_quality_control/audit7_stage1_recertification.md` (this sheet).
Scratch scripts live OUTSIDE the repo at `E:\tmp\qoder_audit7\`. Git was used read-only: `git log`,
`git show`, `git diff HEAD~5 -- <path>`, `git rev-parse`. No ref moved, no working tree touched.

**Zero web requests: YES.** No WebSearch or WebFetch call was issued in this session. Every artifact cited
below is local. Probes that would need the network are marked UNTRIED with the query named.

**Method discipline.** For each AUDIT-6 DEFECT I (a) re-derived the item myself from the current file state,
(b) compared `git diff HEAD~5 -- <file>` against what `audit6_repairs.md` claims, and (c) asked whether the
fix deleted a true claim, softened language instead of fixing evidence, or replaced a wrong number with an
unsourced right one. I do not accept a repair-log row as evidence of a repair.

**Commit under review, and a note on the repo moving during my run.** I began against `HEAD = b6094bc`
("Wave results: Stage 2 sections P-U at 68 new conflicts, Stage 1 repairs applied …", 2026-09-25), where
`HEAD~5 = 7dbaa8b`, and every `git diff HEAD~5 -- <file>` I quote is `7dbaa8b` versus the working tree. During
the run two further commits landed (`ddb8293`, `470d0e1`) which added the Stage-2 volumes, `stage_2_claim_records.md`,
the Stage-2 register rows and this sheet's own stub. I re-checked the drift: `git diff --stat b6094bc..HEAD --
company_001_amazon` is **insertions only, in `_MANIFEST.md`, the eight register CSVs, `research/_EVIDENCE_CACHE.md`
and the Stage-2 volumes** — `stage_1.md`, `stage_1_claim_records.md`, `context_appendices.md`, `CORRECTIONS.md`,
`adversarial_review.md` and every `_parts/s1_*.md` are **byte-identical to what I read**, and the Stage-1 files
are clean against `HEAD`. So every line number, arity and parity figure below is re-runnable as
`git diff 7dbaa8b..HEAD -- <path>` and as the scripts in the reproducibility appendix. The AUDIT-6 baseline is
`f468cb2` / `3ef318a`.

---

## Verdict table

| # | AUDIT-6 item | Verdict | My primary proof |
|---|---|---|---|
| 4 | The dead bridge (`_parts/s1_p4.md:102–103`) | **CLOSED at the named site**; the paired false-sweep claims in `03_quality_control/amazon_s1_numeric_closure_final.md:29` **NOT CLOSED**, and its R-4 at `:42` is now false in the opposite direction | `_parts/s1_p4.md:106–114` (filed two-line form + the deleted false form named inside the retraction); my newline-normalised sweep of the whole company folder returns 7 copies of the LHS, 0 of them live (see §Item 4) |
| 6 | Retracted denominators `2,613,000` / `$871,024` / `$871,000` | **NOT CLOSED** — the two named sites are closed correctly, but **four further sites still run `$871,000` and `$976,408` live as the *corrected* values**, one of them with a citation to a line that does not contain the figure | `_parts/s1_p1.md:142`; `_parts/s1_p3.md:180`; `research/E_supply_ops_finance.md:562`; `_parts/NUMBER_DEFECTS.md:68–74` — see §Item 6 |
| 8 | COR-10 / COR-12 coherence, COR-03 supersession in place | **CLOSED at the three named sites**; **NOT CLOSED as a class** — two unrouted "COR-03 governs" directions survive, one in the mapping authority, one in a deliverable | fixed: `CORRECTIONS.md:13–16, 62, 78–86, 210–211`, `_parts/s1_p3b_H_addendum.md:136–142`; survivors: `_parts/U_CONCORDANCE.md:48`, `adversarial_review.md:34` |
| 9 | Filing-lineage demotion | **CLOSED** — every named site demoted; my own classified sweep (330 `corroborat*` occurrences across all 24 Stage-1 files; 7 kept as lineage-adjacent with no negation in ±300 chars, each read individually) finds **0 live "S-1 corroborates its own amendments" claims**; no live `Corroboration:` count exceeds what the lineage permits (max now 3, both defended on-record) | `stage_1.md:19–25, 55, 126, 241, 310, 896, 1169, 1233–1236`; `quantitative.csv:74`; `context_appendices.md:407, 597, 598`; `CORRECTIONS.md:259, 262–277`; `stage_1_claim_records.md:387, 401, 458, 590–600` |
| 12 | A-B1 (`amazon_s1_audit4_audit5_final.md:409, :431`) | **CLOSED ON EVIDENCE, not papered over.** The repair proved the one-instrument premise from the cached filings; I re-read every citation it adduces and all of them are on the stated lines. One wording overreach named as a residual | `stage_1.md:62–73`, `CORRECTIONS.md:279–296`, `sources.csv` S0801/S0803; my verification: original S-1 l.49/77, No. 3 l.49/79/5112, No. 5 l.49/70/79/5106 + EX-23.1 at l.5091, 424B1 l.66/92, 10-K405 l.2913/3105 — all confirmed |
| 13 | Fix-introduced false closure assertions | **PARTLY CLOSED — the class is NOT CLOSED.** **3 of 6** of AUDIT 6's repair-introduced assertions are fixed and I re-derived each; the **3** that remain are all in the two QC closure sheets, untouched; and **this repair pass introduced 3 new small false closure sentences of exactly the same class (+1 carried from the prior pass)** | fixed: `stage_1.md:40–48`, `:1281–1284`, `:1560–1563`, `:2264–2286`, `conflicts.csv` U.8/U.17 cells; unfixed: `amazon_s1_numeric_closure_final.md:17, :29, :42`, `amazon_s1_causal_lineage_closure.md:37, :86`; new: `_MANIFEST.md:39`, `_MANIFEST.md:42`, `CORRECTIONS.md:295–299`, `stage_1_claim_records.md:592` |

**Tally: CLOSED 2 (items 9, 12) · CLOSED AT THE NAMED SITES / CLASS SURVIVES 2 (items 4, 8) · NOT CLOSED 1 (item 6) · PARTLY CLOSED, CLASS NOT CLOSED 1 (item 13). Nothing I examined was OVERCORRECTED: no true claim was deleted, no confidence moved, no language softened in place of evidence — I tested for all three and the numbers are in §Invariants.**
**UNTRIED: 0 for these six items.** All three of AUDIT 6's UNTRIED sub-probes remain UNTRIED (they need the network); they are carried, not re-attempted — see §Sub-probes.

---

## Item 4 — the dead bridge — **CLOSED at the named site**

### What the repair did (I read the diff, not the log)

`git diff HEAD~5 -- founders_playbook/01_companies/company_001_amazon/_parts/s1_p4.md` — three hunks, at received
ll. 62, 93–103 and 476+. The d14 line now reads, at `_parts/s1_p4.md:106–114`:

> `d14 **IN FILED FORM — the equation this line printed for three repair rounds was FALSE and is retracted here
> in place, not silently rewritten.** Filed form, two lines, both endpoints filed: −232 (operating, orig. l.3636)
> − 52 (investing, l.3641) + 1,228 (financing, l.3649) = +944 … **The form removed reads
> `52 − 232 − 52 + 1,228 = +944`, whose left-hand side is 996, not 944:** …`

So the false form survives **only inside its own retraction**, which is what the rule requires; it was not
silently deleted, and the corrected terms are the filing's, not invented.

### I re-read the filed terms myself

`sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt`, printed lines 3636, 3641, 3649, 3652–3655:

```
3636  Net cash used in operating activities...........  (24)  (232)  (1,735)
3641  Net cash used in investing activities...........  (28)   (52)  (1,214)
3649  Net cash provided by financing activities........ 104   1,228   8,201
3652  Net increase in cash.............................  52     944   5,252
3653  Cash and cash equivalents at beginning of year...  --      52     996
3655  Cash and cash equivalents at end of year......... $52    $996  $6,248
```

Every term cited is on the line cited. `-232 - 52 + 1228 = 944` ✓; `52 + 944 = 996` ✓; and the retraction's
arithmetic charge is right: `52 - 232 - 52 + 1228 = 996`, not 944 ✓ (Python).

### My own sweep, not the repair's

A single-line grep cannot see this defect (it wraps), so I ran a **newline-normalised** pattern sweep over every
`.md`/`.csv` under `company_001_amazon/` (script `E:\tmp\qoder_audit7\bridge.py`), for
`52 [-−] 232 [-−] 52 [+] 1,?228`, and classified each hit by whether retraction language sits within ±260 chars:

```
_parts\NUMBER_DEFECTS.md   [RETRACTION]  …the cash bridge 52 − 232 − 52 + 1,228 = 996…   (true form, a passing tie)
_parts\s1_p4.md            [RETRACTION]  ×2  (d14 in place; AUDIT-6 addendum)
quantitative.csv           [RETRACTION]  L66 notes "this cell read … and the equation is false"
quantitative.csv           [flagged LIVE]  line 112 notes: "(52 - 232 - 52 + 1,228 = 996), which is also true"
stage_1.md                 [RETRACTION]  §P.2 d14 "The deleted form read … = +944, whose left-hand side is 996"
validation.csv             [RETRACTION]  file line 17 "…previously printed that same left-hand side as '= 944', which was false"
total occurrences: 7
```

The one flagged "LIVE" is a **false positive of my own classifier**: it is the `= 996` form, which is
arithmetically true, and the sentence says "which is also true". **Zero live copies of the FALSE (`= 944`) form
survive anywhere in the company folder**, including `research/`, `_parts/` and the Stage-2 volumes.

Also closed here, and I checked rather than accepted: d4/d5/d7 at `_parts/s1_p4.md:96–100` are marked
`[SUPERSEDED …]` with corrected values beside them, and the corrected values recompute
(`582,528 × 0.1717 = 100,020.0576 → $100,020.06` ✓; `847,716 × 0.1717 = 145,552.8372 → $145,552.84` ✓);
`_parts/s1_p4.md:62` (P36) is annotated as the opening-inclusive reading ✓.

### What is NOT closed under this item

`03_quality_control/amazon_s1_numeric_closure_final.md:29` still certifies "**Sweep for a surviving live
instance of the false equation across all registers, parts and claim records: 0**" — false when signed (that is
what AUDIT 6 caught) and left uncorrected because the repair logged it at `audit6_repairs.md:60–61` as "paths I
may not edit". And its residual R-4 at `:42` ("The deleted false bridge **still prints live** in
`_parts/s1_p4.md` ll. 102–103") is now **false in the other direction**: the site is annotated. Neither sheet
was corrected by addition, which is what AUDIT 6's B-4 asked for.

---

## Item 6 — retracted denominators — **NOT CLOSED**

### The two named sites: closed, and closed correctly (retraction, not substitution)

`git diff HEAD~5 -- …/context_appendices.md` hunk `@@ -592,8 +594,8 @@`. Current `context_appendices.md:598` (§I,
Value column) now opens "**THE COMPOSITION OF THAT UN-NAMED RESIDUAL IS UNKNOWN AND NO COMPOSITION TOTAL IS
PRINTED ON THIS ROW**", foots only the filed legs to **$105,408**, and prints both retracted one-third values
**inside** an explicit "**RETRACTION, this row having carried the number twice**" sentence. `:641` (§J gap row
12) does the same and adds the reason ("the filing … dates the program only as a window … so no in-window share
count exists for the anonymous leg — the reason the composition is UNKNOWN rather than pending").

I did not accept the repair's arithmetic: `5,408 + 150,000 − 50,000 = 105,408` ✓; `2,811,000 ÷ 3 = 937,000` ✓;
`5,408 + 150,000 + 937,000 − 50,000 = 1,042,408` ✓; `1,042,408 − 976,432 = 65,976` ≈ the stated ≈$66,000 ✓;
`1,272,000 − 295,568 = 976,432` ✓; `569,396 × 14.05 = 8,000,013.80` ✓. And the retraction's *premise* is true:
my own per-file `grep -c` over all nine local `sources/*.txt` returns **0** for `2,613,000` and 0 for the
no-separator form `2613000`, with positive controls on the same method (`3,021,000` present in 5 of the 9). The
 Confidence column was split rather than deleted (`High` for the filed lines, `UNKNOWN` for the composition) —
no true claim lost. Table arity preserved: §I region parses to 35 rows × 9 pipes; the two edited rows carry 9
and 6 pipes, matching their own tables (`E:\tmp\qoder_audit7\arity5.py`).

### The defect: four sites still run the leg live, and the repairer had already identified this exact pattern

Same sweep as AUDIT 6's brief instructs, company folder wide (`grep -rn` for `871,000|871,024|2,613,000|976,408`):
`stage_1.md` (22 hits) and the registers are all retraction-framed — I read each: `stage_1.md:242, 610, 874,
969–993, 1066–1067, 1179, 1187, 1207, 1522–1539, 1564–1573` are all inside RETRACTED-FIGURE / CLAIM-A-CLAIM-B
language, and `stage_1.md:1565–1567` explicitly records that the `2,613,000 ÷ 3` leg "cited to orig.
l.4301–4302, which contains 3,021,000 / 23 investors / $.3333 / $1,007,000 and **not** 2,613,000". I confirmed
that by reading orig. ll.4296–4306: the citation is indeed worthless for that figure.

**But four sites state the retracted figures as the *corrected* values, in the present indicative, outside any
retraction sentence:**

| Site | Live text | Why it is the item-6 defect |
|---|---|---|
| `_parts/s1_p1.md:142` | "the disclosed-component composition foots to **$976,408** … The one-third leg **is $871,000** (`2,613,000 ÷ 3`, orig. l.4301–4302)" | asserts the withdrawn composition total **and** the withdrawn leg as current, and re-uses the citation `stage_1.md:1565–1567` proves false |
| `_parts/s1_p3.md:180` | "…the disclosed-component composition foots to **$976,408** — a band-level tie … The unaffiliated one-third leg **is $871,000** (`2,613,000 ÷ 3`, orig. l.4301–4302)" | same, verbatim twin |
| `research/E_supply_ops_finance.md:562` | "…with the disclosed-component composition **at $976,408** … The one-third leg **is $871,000** (`2,613,000 ÷ 3`, orig. l.4301–4302)" | same, in a dossier Stage 2 mines |
| `_parts/NUMBER_DEFECTS.md:68–74` | "their `should_be` leg reads **≈$871,000, which is the canonical figure** … so the composition foots to **$976,408** … the $24 difference is **accounted for** … not plugged" | the strongest of the four: it calls the retracted figure *canonical* and revives the "$24 accounted for" account that IR-04 and `stage_1.md:1530/1573` withdraw |

All four are `SUPERSEDED 2026-09-24` **correction banners** — i.e. the annotations that tell a downstream reader
what to believe instead. `_parts/NUMBER_DEFECTS.md:91–95` states the design: those files "each received an
appended `SUPERSEDED 2026-09-24` footer naming the site, **the corrected value** and where it lives." The
corrected value in those footers is itself a retracted value.

This is not a pattern I inferred — **the repairer found it once and fixed only the one instance.**
`audit6_repairs.md` IR-03b: "an AUDIT-6 addendum was appended recording that the footer's own limbs (a) and (b)
are superseded … **because the footer itself printed $871,000 as the *corrected* value, which is the item-6
defect in a third place**." It is the defect in a **sixth, seventh, eighth and ninth** place (three sibling
footers + the Level-3 register's supersession marker), and the pass did not sweep for the siblings of the site
it had just diagnosed. That is the same failure mode AUDIT 6 named at item 13 ("sweep scoped to the file open").

**Verdict: NOT CLOSED.** Two named sites closed properly; the retracted leg is still live in the folder, with a
false line-citation attached. Blocking.

---

## Item 8 — COR-03 / COR-12 coherence — **CLOSED at the three named sites; NOT CLOSED as a class**

### (a) The arithmetic limb, re-derived

`3,021,000 × 0.3333 = 1,006,899.30` ✓ (Python). Reverse: `1,007,000 ÷ 3,021,000 = 0.3333333…`, so the aggregate
is the precise figure and `$.3333` its rounded display — which is what `context_appendices.md:599` and
`CORRECTIONS.md` COR-10 now say. Filed at `sources/S-1_original…txt:4300–4302` (I read the paragraph: "3,021,000
shares … to 23 investors … approximately $.3333 per share, or an aggregate of $1,007,000") ✓. **CONFIRMED again.**

### (b) The three named supersession sites: closed

- `CORRECTIONS.md:62` — heading now `## COR-03 [SUPERSEDED BY COR-12, 2026-09-23] — …`, plus a blockquote
  immediately under it (`:64–70`), plus the Action line relabelled
  `**Action [WITHDRAWN BY COR-12 — the rule below is inverted and must not be applied]:**` at `:78` **with the
  original command left standing**, and a new standing action appended at `:83–85`. This is the correct shape:
  marked in place, nothing deleted, the reader working top-down is warned before meeting the retracted text.
- `CORRECTIONS.md:210–211` — the COR-11.2 route now reads "see COR-03 — **which is SUPERSEDED BY COR-12: apply
  COR-12 …**". I grepped every `COR-03` reference inside `CORRECTIONS.md`: the only "see COR-03" in the file is
  that one, and it is routed, so the file's new header promise at `:16` ("Any other cross-reference in this file
  that says 'see COR-03' is routed through that marker") is **true as stated**.
- `_parts/s1_p3b_H_addendum.md:131/136–142` — the original sentence was left intact and a separate
  `[SUPERSESSION MARKER, added 2026-09-24.]` paragraph appended, which also states the one limb COR-12 leaves
  standing (151 is post-Stage-1). I checked the repair log's worry (IR-08: "a first attempt clipped its tail —
  caught on re-read"): the sentence at `:131–133` reads whole in the current file ✓.

### The class survives at two sites the pass did not look at

1. **`_parts/U_CONCORDANCE.md:48`** — the U.17 row reads "**COR-03 / COR-11.2 govern.** … so **11 is a
   1996-01-01 count** … §P and §R print `11 (per the filing: at 1996-01-01)`." That is the **withdrawn Action,
   verbatim, presented as governing**, in the file `_MANIFEST.md:67` calls "the only authority for `Conflicts:
   U.n` references". `conflicts.csv` U.17 (whose cell the repair just edited) says the opposite about the same
   instruction: "the instruction this cell carried — print '11 employees (per the filing: at 1996-01-01)' …
   is WITHDRAWN and must not be followed".
2. **`adversarial_review.md:34`** — a deliverable (`_MANIFEST.md:40`, "COMPLETE", upload batch 1):
   "`"11 employees" is the filing's **1996-01-01** figure (COR-03, U.21)`" — cites the superseded correction as
   the live authority with no marker. Less severe (the statement is true as far as it goes, which is exactly
   COR-03's over-claim shape), but it is an unrouted reference to a retired correction.

`_MANIFEST.md:67` does already disclose that the concordance "**does not yet list U.43**, appended …", so the
volume is known-stale for one item — but not for COR-03. Fix is a marker line, not a rewrite.

---

## Item 9 — filing-lineage demotion — **CLOSED**

### The phrase test, run as instructed (grep, not sample)

`grep -rniE "independent corroboration"` over the whole company folder returns 15 lines. Classified individually:
`CORRECTIONS.md:297` (quoting the phrase it strikes); `stage_1.md:583` and `_parts/s1_p2.md:157` (a table row
labelled "Independent corroboration" whose content is US 5,960,411 — a USPTO patent, genuinely a different
originator, not the filing family); `sources.csv:17` (S0204, the Academy of Achievement interview — "**no**
independent corroboration of anything it asserts about 1994", a negation in a founder-testimony lineage note);
`sources.csv:51` and `:53` (S0801's "PHRASE SWEEP 2026-09-24: this note used to say that the T1/ISP … items DO
GAIN INDEPENDENCE … That is the exact wording A-B1 ordered struck, and it is wrong on the rule", and S0803's
"the four disclosures this note formerly credited as independent corroboration … are restatements … and
corroborate nothing");
`_MANIFEST.md:46` (status record); `stage_1_claim_records.md:380, 404, 469, 492, 502, 568` — every one inside
"**not** independent corroboration" or "the wording this record carried, 'independent corroboration', was struck
across the appendix on 2026-09-24". The three hits in `research/ST2_*.md` / `_EVIDENCE_CACHE.md` are Stage 2.
**Zero live claims of independent corroboration between S-1 / amendments / 424B1 survive in Stage 1.**

Same for `gain(s) independence` / `genuinely corroborat`: 6 hits corpus-wide, all inside withdrawal sentences
(`stage_1.md:55` "that phrasing is withdrawn"; `CORRECTIONS.md:297`; `sources.csv:51` and `_parts/s1_p4.md:287`,
both inside `PHRASE SWEEP` / `[RETRACTED IN PLACE …]` brackets; `_MANIFEST.md:46`).

I also ran a classifier I designed to *find* violations rather than confirm none
(`E:\tmp\qoder_audit7\corrob2.py`): every `corroborat*` occurrence in all 24 Stage-1 files (330 hits), kept only
those with a lineage neighbour (`S-1 (orig.`, `No. 3/5`, `424B1`, `10-K405`, `S080x`, `accession`, `amendment`)
in ±300 chars and **no** negation/demotion marker anywhere in that window. It returned 7, and I read all 7:
`stage_1.md:434`, `:893`, `stage_1_claim_records.md:467`, `quantitative.csv:70` — all four are the balance sheet
l.3429 vs the statement of cash flows l.3630, i.e. two **primary audited statements** agreeing inside one filing,
which method §3 does not place in the prohibited set (it names amendments, superseding prospectuses and
*exhibits* to the same accession, and lists "an auditor's report" among independent origins);
`stage_1.md:1387` (Exhibit 10.12 corroborated by Kaphan's memoir — a different originator);
`context_appendices.md:407` and `CORRECTIONS.md:268` (both self-descriptions of the demotion). **No violation.**

### The counts test, run as instructed (census, not sample)

Every live `Corroboration:` field in `stage_1_claim_records.md` extracted per record
(`E:\tmp\qoder_audit7\corcount2.py`): 49 populated record fields → **40 at 1, 4 at 0, 3 at 2, 2 at 3, none at 4.**
Pre-repair state at `HEAD~5` under the same script: 49 fields, 7 at ≥2, **5 at ≥3** — exactly the population
AUDIT 6 described, and the three violations moved: **K04 3→1, L01 4→2, P01 3→1** (git-verified field diff),
with **L05, P13** left at 2 and **M05, L06** left at 3, each carrying the reason in the record.

I checked the two survivors at 3 against their own source lines rather than the log:
`M05` (`:416`) — "Source: Amazon.com Form S-1 (T01); WSJ via paleofuture and The Seattle Times (T19)" →
1 lineage + 2 independent papers = 3 ✓ the addendum's arithmetic is right;
`L06` (`:406`) — "Corroboration: 3 (June 1996 release; LA Times 1996-12-11; Wired 1996-12-16)" → no filing
lineage in the count at all, and the claim is what the **October 1995** release advertised, so the June 1996
leg is not load-bearing ✓ defensible as written (this stays a judgement call, not a defect — same as AUDIT 6's).
`L01`'s re-key to 2 is the right answer, not a softening: it keeps the *Seattle Times* leg and drops the 424B1
and the FY1997 10-K405, both of which §3 puts inside the lineage.

### §T and the register sites

All five §T lineage rows now carry the demotion: `stage_1.md:1232` (original), `:1233` (No. 5), `:1234` (No. 3),
`:1235` (10-K405), `:1236` (424B1). The 424B1 row's stale `restoration pending` is gone, replaced with the
on-disk fact **and a refusal to import it**: "266,755 B … **It is not read into this volume:** no Stage-1 claim
here is cited to it … because a closure pass may not import a primary into the corpus it is closing; COR-14.1's
P60/P61 citation item stays with the retrieval owner." I verified the size: `wc -c` = **266,755** ✓. That is the
correct conservative move, not a deletion of a true claim.

`quantitative.csv:74`: source, source_date and notes all demoted; **`confidence` still `High`, value still `11`,
evidence_class still `FACT`** — I diffed the row field-by-field against `HEAD~5` to be sure nothing else moved.
`context_appendices.md:597` (headcount row) and `:407` (the §F T1-line row) demoted; the latter's
`corroboration 2` → `corroboration 1`, i.e. the count was **reduced** to what the lineage permits ✓.
`CORRECTIONS.md:259` + `:262–277`: the generating instruction is quoted verbatim inside an appended block and
withdrawn there, so it cannot regenerate. That was AUDIT 6's sharpest point ("unfixed it regenerates") and it is
handled.

**Overcorrection test:** none. The 11-at-1995-12-31 claim survives everywhere with its filed citation; COR-12's
ruling is untouched; only the *independence credit* moved.

**Named residuals under this item (not reopening):**
- `stage_1.md:63` says every member "carries the same SEC file number, 333-23795, **on its own face**". For
  the FY1997 10-K405 that is false — its face number is `SEC FILE NUMBER: 000-22513`
  (`sources/10-K_FY1997…txt:50`); 333-23795 appears in it only twice, inside the exhibit index's
  incorporation-by-reference notes at l.2913 and l.3105 (which is exactly the evidence the row then cites, so the
  itemised line is honest and only the umbrella clause overreaches). Same looseness in `sources.csv` S0801's
  "carried on all five accessions" and `_parts/s1_p4.md:287`'s "appears on all five" (that last one is true as
  worded).
- `_MANIFEST.md:38` still says "432 claim records" and `stage_1.md:2358` still says "**432 records … reconciled to
  the canonical U.1–U.42 spine**". My census, two ways: 431 `grep -c "Claim:"` and 431 on the anchored pattern.
  The record count was carried unchanged from before the repair (431 at `HEAD~5` too), so the spine note added
  there is right and the 432 is still wrong.

---

## Item 12 — adversarial attack A-B1 — **CLOSED ON EVIDENCE** (not papered over)

### What AUDIT 6 asked and what the repair actually did

AUDIT 6's decision at item 12 was that A-B1 "still lands" because the demotion was incomplete **and because its
completeness had been asserted on a marker census**. Two things had to change: the sites, and the *method* by
which completeness was claimed. The repair did both, and the second is the part that could have been faked with
softer wording. It was not. What was added is a **proof block** whose every element I re-read from the cached
filings:

`stage_1.md:62–73` ("THE PREMISE IS PROVED FROM THE CACHED FILINGS, NOT STIPULATED … this is what closes A-B1")
and the same proof tabulated at `CORRECTIONS.md:279–296`. My verification, line by line from `sources/`:

| Cited | I read | Result |
|---|---|---|
| original S-1 `SEC FILE NUMBER: 333-23795` at l.49 | `SEC FILE NUMBER:\t333-23795` | ✓ on l.49 |
| original S-1 "REGISTRATION NO. 333-" at l.77 | `REGISTRATION NO. 333-` | ✓ on l.77 — and the repair prints it **truncated exactly as filed**, which is the honest rendering |
| S-1/A No. 3 at l.49 and l.79 | `333-23795` / `REGISTRATION 333-23795` | ✓ both |
| No. 3 "signature page l.5112" | l.5112: "No. 3 to the Registration Statement (Form S-1 No. 333-23795)" | ✓ at that line — it is inside **Ernst & Young's consent**, not the signature block (the repair's next clause names the consent, so the substance is right and only the label is loose) |
| S-1/A No. 5 at l.49, l.79, cover l.70, "signature page l.5106" | all four located; l.70 is `<DESCRIPTION>AMENDMENT NO. 5 TO FORM S-1` | ✓ |
| "E&Y consent is its own exhibit EX-23.1" | `S-1A-No5…txt:6` header "complete submission incl. EX-23.1 consent of Ernst & Young LLP"; `<TYPE>EX-23.1` at l.5091 | ✓ |
| 424B1 at l.66 and cover l.92 | `SEC FILE NUMBER: 333-23795` at l.66; `Registration Statement No. 333-23795` at l.92 | ✓ |
| 10-K405 at l.2913 and l.3105 | "Incorporated by reference to the Company's Registration Statement on Form S-1 (Registration No. 333-23795)" — `grep -n` returns exactly 2913 and 3105 | ✓ (and see the residual: this document's **own** face number is `000-22513` at l.50) |

Counts: `333-23795` appears 1 / 3 / 3 / 3 / 2 times in the original / No. 3 / No. 5 / 424B1 / 10-K405
respectively — so "appears on all five" is true as an occurrence claim for all five, and true as *their own file
number* for the four S-1-family documents only. That is the only soft spot in the closure and it is one clause,
not the argument.

### Closed on evidence vs softer wording — my determination

**Closed on evidence.** Three independent reasons:
1. The proof is re-derivable by any verifier from local files in minutes; it does not depend on any sentence the
   repair wrote. A-B1's ruling had been "Ruling required, not re-research"
   (`amazon_s1_audit4_audit5_final.md:409`) — the repair complied and did not spend a web request either.
2. The *consequences* were executed, not just described: `Corroboration: 4 → 2`, `3 → 1`, `3 → 1`;
   `corroboration 2 → corroboration 1` at `context_appendices.md:407`; the two `sources.csv` notes that asserted
   "DO gain independence" rewritten to say the opposite; three §T rows demoted; COR-12's generating instruction
   withdrawn in place.
3. The claim "No claim in this corpus is reopened or moved to UNKNOWN by A-B1 … confidence levels were verified
   unmoved" is **true and I verified it independently of the log**: across `HEAD~5 → HEAD` there are
   **0 confidence changes** on all 431 claim records and **0** on every Stage-1 row of `quantitative.csv`,
   `validation.csv`, `timeline.csv`, `failures.csv`, `data_gaps.csv`, `decisions.csv`, `channels.csv` and all 43
   Stage-1 `conflicts.csv` rows (the only confidence diffs in those two files belong to new U.44–U.111 / S2xxx
   rows). A paper-over would typically have moved or hollowed something.

### What is NOT done

`03_quality_control/amazon_s1_audit4_audit5_final.md:409` and `:431` still read as an unresolved attack
("**Lands? YES**", site list "ll. 417, 532, 1126, 1202; appendix ll. 406–407; 24 claim records") with no closure
status appended. That file is an attack register and by this project's own rule the audit trail is not
retro-edited — but AUDIT 6's B-4 asked for these sheets to be "corrected **by addition**", and that addition has
not happened. The repairer itself listed `:409 / :431` as "Out-of-scope findings recorded here for the sheet
owner (`audit6_repairs.md:66`)". So Stage 1's text is clean and the QC layer still contradicts it.
This is a **one-line addition**, and it does not block signing Stage 1's content; it blocks the claim that the
AUDIT-6 finding list is closed.

---

## Item 13 — fix-introduced false closure assertions — **PARTLY CLOSED / NOT CLOSED**

### AUDIT 6's six, one by one

| # | AUDIT 6's finding | Current state | Verdict |
|---|---|---|---|
| 1 | `stage_1.md:36` "four sites that contradicted it are corrected below" | Replaced at `stage_1.md:40–48` by a scope statement that names what was done (4 sites + 22 records), why the census missed (marker count, not site audit), and lists the survivors it then closes | **CLOSED, and true as re-stated** — I verified each element: prose sites now carrying the demotion at `:457, :586, :1233, :1314`; exactly 22 records at `1 (same lineage as S0801)`; all seven named survivors demoted (verified under items 9 and 12) |
| 2 | `amazon_s1_numeric_closure_final.md:29` "Sweep … **0**" | Untouched (the wave changed no QC sheet except `audit6_repairs.md`) | **NOT CLOSED.** Worse: its own R-4 at `:42`, which contradicted it, is now stale in the opposite direction ("The deleted false bridge **still prints live** in `_parts/s1_p4.md` ll. 102–103" — it no longer does) |
| 3 | `amazon_s1_numeric_closure_final.md:17` "no live value cell carries either" | Untouched | **NOT CLOSED**, and now false for a *new* reason: the three footer sites under item 6 carry `$871,000`/`$976,408` as corrected values |
| 4 | `amazon_s1_causal_lineage_closure.md:37 / :86` — a marker count reported as a site audit ("all 31 named sites demoted") | Untouched; `:37` still tabulates `stage_1.md | **4** | ll. 431, 560, 1203, 1280` | **NOT CLOSED** (the underlying work is now far more complete than the census claimed, which makes the sheet's *method* claim the thing still standing uncorrected) |
| 5 | `stage_1.md:2218–2231` pointer census omitted `timeline.csv` | Rewritten at `stage_1.md:2264–2286`, self-critical, and re-derived across the register set | **CLOSED and true**: I confirmed from git that at `HEAD~5` the 49 Stage-1 `timeline.csv` rows held **0** `U.41`, **0** `U.43`, **2** `U.16`, and that at `HEAD` they hold 1 `U.43` (`:33`) + 1 `U.41` (`:55`, a `stage2-consequence` row), with `[conflict_ref RE-KEYED from U.16 to U.4x on 2026-09-24 …]` recorded inside each row's notes; `sources.csv` S0608 does carry `(U.41)` on the Associates row as the note asserts |
| 6 | `conflicts.csv:9` + `stage_1.md:1526` "the canonical spine is fixed at U.1–U.42" | Both annotated without altering the reason they give | **CLOSED**: `conflicts.csv` U.8 `evidence_weight` now reads "…fixed at U.1–U.42 (spine note appended 2026-09-24: U.43 has since been added … the point stands, because appending happens at the end of the spine and this retraction mints no id of its own)"; mirrored at `stage_1.md:1560–1563`; `stage_1.md:7` header likewise at `:9–12`; §U preamble at `:1281–1284` now says **43 canonical conflicts, U.1–U.43** |

**Score: 3 of 6 closed; 3 open — all three in the two closure sheets, all three by deliberate scope
restriction, all recorded rather than hidden.** That is better behaviour than the original failure, but it is
not closure, and AUDIT 6 listed them as defects it introduced.

### New false closure assertions introduced **by this repair pass** (my finding, not AUDIT 6's)

| Site | Claim | What I measured |
|---|---|---|
| `_MANIFEST.md:39` | "**the three sites** the 2026-09-24 closure could not reach **were reached** by the AUDIT-6 repair pass": §I Capital row, "**§G** gap row 12", §I headcount row, "plus **§F**'s T1-line row" | Four things are named as "three"; all four **were** genuinely repaired (I read each), so the substance holds. But the gap row is in **§J** (`## J. Data gaps and contested figures` at `context_appendices.md:623`, table header at `:628`, the row at `:641`), not §G (`:467 Institutional support environment`). The mislabel is repeated in `audit6_repairs.md` IR-05. Same defect class AUDIT 6 is built on: a closure sentence whose coordinates were not re-checked |
| `CORRECTIONS.md:295–299` | A-B1 "complete at the sites AUDIT 6 named plus **four** found by re-running its own phrase sweep", then names five (S0801, S0803, boundary-state row, §B.2, §D.1) | All five **are** demoted (`sources.csv:51/53`; `stage_1.md:126, 241, 310`) — the count word is wrong, the work is not |
| `stage_1_claim_records.md:590–593` (addendum i-bis) | "A full census of the field … **52 populated `Corroboration:` fields, 5 at ≥3**" | Reproduced at `HEAD~5`: **5 at ≥3 ✓ exactly** (K04 3, L01 4, P01 3, M05 3, L06 3) — the operative number. "52" does not reproduce under either convention I can defend: 49 record-level fields, 54 raw `Corroboration:` occurrences (which is also what AUDIT 6's "9 at ≥2" cannot be matched to — I get 7 record-level at ≥2) |
| `_MANIFEST.md:42` (carried, not new) | "`derived_arithmetic` populated on exactly the **30** DERIVED/ESTIMATE/INFERENCE rows"; "quantitative.csv … **111 data rows** × 12 cols" | Over the 111-row Stage-1 block: **29** rows carry arithmetic and **all 29 are `DERIVED`**; the single `INFERENCE` row (L38) had its string relocated to `notes` by verify-3 F-7, which AUDIT 6 graded a *correct* repair. So "30" is false, and the row is also stale against the file's current 193 rows (the 2026-09-25 regeneration section supersedes word/byte counts, not this sentence) |

### The one place the repair over-reached rhetorically

`stage_1.md:48` — "**All of them are demoted** as of the 2026-09-24 audit-6 repair pass, and the completeness
claim is re-derived from a site list rather than a marker count." Both halves held for the sites it names. But
the sentence sits in the *header*, which is the volume's governing statement, and the same pass that wrote it
left `_parts/U_CONCORDANCE.md:48` commanding the withdrawn COR-03 action and four `_parts/`/`research/` footers
printing `$871,000` as canonical. **Re-derived from a site list, yes — from a site list that stopped at the
deliverables and did not include the parts, the concordance, or the dossier footers.** That is the identical
mechanism AUDIT 6 diagnosed at item 13 ("the sweep scoped to the file the agent happened to have open"), which is
why I weight items 6 and 8 as NOT CLOSED rather than as trivia.

---

## Invariants — recomputed, not inherited

| Invariant | AUDIT 6's figure | **My figure now** | Holds? |
|---|---|---|---|
| Stage-1 U blocks ↔ `conflicts.csv` rows | 43 ↔ 43 | **43 ↔ 43.** `^\*\*U\.[0-9]+ — ` in `stage_1.md` → 43 blocks at lines 1292…2303, ids contiguous 1–43, no duplicates; `conflicts.csv` rows with `conflict_id` U.1–U.43 → 43, at **file lines 2–44 in order**, `stage` column = `1` on all 43; set parity both ways, orphans `∅` either direction | **YES — and nothing was renumbered.** Stage 2's U.44–U.111 = 68 rows at file lines 45–112, all `stage = 2`, contiguous, **zero id overlap** with Stage 1's subset. Stage-1's block↔row mapping resolves exactly as before the wave |
| Nine registers parse at uniform field count with quoting | 9 files, 428 data rows | **9 files, 711 data rows**, ragged rows **0**: `sources.csv` 113 × 18 · `quantitative.csv` 193 × 12 · `timeline.csv` 115 × 11 · `decisions.csv` 25 × 15 · `validation.csv` 40 × 11 · `failures.csv` 46 × 11 · `channels.csv` 23 × 11 · `conflicts.csv` 111 × 15 · `data_gaps.csv` 45 × 8. Every file's `Counter({n: rows+1})` is a single key, so quoting is holding commas, parentheses and `""` escapes across the whole set | **YES** (428 → 711 because of the 283 Stage-2 rows; growth is additive) |
| Stage-1 subset of each register unchanged | 111 / 43 / 57 / 15 / 29 / 33 / 15 / 43 / 23 | Stage-1-tagged rows now: sources **102**, quantitative **94** (+17 `stage2-consequence` = the old 111), timeline **49** (+8 consequence), decisions **15**, validation **26** (+3 consequence), failures **33**, channels **12** (+3 consequence), conflicts **43**, data_gaps **23** — **each identical to `HEAD~5`** | **YES.** No Stage-1 row added, dropped, re-tagged or moved by the repair |
| `derived_arithmetic` populated on every DERIVED row | 29/29, 0 non-DERIVED carrying arithmetic | Stage-1-tagged: **26/26** populated (the other 3 DERIVED rows sit in the `stage2-consequence` band, which is why AUDIT 6's 29 ≠ my 26; nothing left the file). **0 empty DERIVED rows file-wide (50 DERIVED rows, all populated)**; **0 non-DERIVED Stage-1 rows carrying arithmetic** | **YES for Stage 1.** Named for the Stage-2 owner: file-wide, **28 non-DERIVED rows** at `quantitative.csv` lines 118–194 carry arithmetic (e.g. L118 `FACT`, L132 `FACT (unaudited)`, L184 `ESTIMATE (third party)`), which is the same rule Stage 1 is held to. Out of my scope; recorded because I re-ran the census |
| §P.2 recomputations | 32/32 | **32/32.** I re-ran the d-chain from filed inputs with 60 independent checks (d1–d30 plus d8a/d15a and their band/arithmetic sub-terms) — `E:\tmp\qoder_audit7` inline script, all OK. The **only** changed figure in the repaired text, d7's printed terms `100,020.0576 + 145,552.8372 + 49,995 = 295,567.8948 → $295,567.89 → $295,568`, recomputes exactly, and the note's own explanation of the one-cent gap is right (rounded addends foot to 295,567.90) | **YES** |
| 29/29 "derived rows" as AUDIT 6 framed it | 29 | **29 rows, 29 populated** in the 111-row Stage-1-era block; classes 26 `DERIVED` in the re-tagged stage1 subset + 3 in the `stage2-consequence` band. Same set, same coverage | **YES** |
| §R ↔ §P / register cross-references resolve | 6 d-refs, 17 U-refs, 0 missing | **Identical result re-run on the current file**: §R now at `stage_1.md:1160–1192`; d-refs `{8a, 15a, 24, 25, 26, 30}`, U-refs `{1,7,8,9,10,11,17,20,22,23,25,26,27,28,39,40,43}`, **missing = ∅** against the 43 blocks and the §P.2 id set; and §R's self-description of the weekly-sales row still matches `quantitative.csv` **file line 112** field for field (stage1 / 1995-12-31 / metric string / `19440-21383` / USD/week / DERIVED) | **YES** — the line shifts from the wave's insertions broke nothing |
| Row-reference integrity of citations the repair added | — | `conflicts.csv` U.17's cell cites "quantitative.csv L74, validation.csv r7": L74 = the `Employees at the Stage-1 boundary / 11` row ✓; under this corpus's `rN` = file-line convention (the convention AUDIT 6 used at `conflicts.csv:9`/`r42`/`r44`), `validation.csv` **r7** = file line 7 = the `Eleven employees / 11 persons` row ✓ — I checked the alternative convention too and it would land on the Steinbeck search test, so the convention matters and is stated. `stage_1.md:1565–1567`'s retraction correctly records that *the old* citation "orig. l.4301–4302" carries `3,021,000 / 23 investors / $.3333 / $1,007,000` and not `2,613,000` — I read those lines | **YES** for Stage 1's own citations; **NO** for the four item-6 footers, which re-use that same disproved citation as if it were live |
| No renumbering / append-only id rule | respected | `stage_1.md:9–12`, `:1281–1284`, `:1560–1563`, `conflicts.csv` U.8 cell, `stage_1.md:2297/2306` all state it; my parse shows ids U.1–U.43 and U.44–U.111 both contiguous | **YES** |
| Retraction-only sweeps | `21,382.98` = 6 sites retraction-only; false bridge = 1 live | `21,382.98` now **3 lines** (`quantitative.csv:112`, `stage_1.md:1087, 1088`), all three inside the correction sentence naming it a truncation ✓; false bridge (`= +944`) **0 live** corpus-wide (§Item 4); `$871,000` / `2,613,000` / `$976,408` **4 live sites** (§Item 6) | **Bridge/headcount clean; the equity leg is not** |

**Confidence- and value-invariance test (my own, added because a repair that silently changes a rating is worse
than one that leaves a marker off):** across `HEAD~5 → HEAD`, changed fields in the registers are confined to
`source`, `source_date`, `notes`, `independence_note`, `conflict_ref`, `evidence_weight`,
`best_supported_interpretation` and `derived_arithmetic`. **Zero** changes to `value`, `unit`, `date`,
`evidence_class` or `confidence` on any Stage-1 row, and zero to `Conf:` on any of the 431 claim records. Every
number the repair printed is re-derivable and I re-derived the 14 that were new (`$105,408`, `$937,000`,
`$1,042,408`, `65,976`, `976,432`, `105,408`, `8,000,013.80`, `266,755 B`, `43/43`, `22 records`, `5 at ≥3`,
`3,021,000/3`, `2,613,000 ÷ 3 = 871,000` arithmetically true but denominator-unfiled, `52+944=996`).

---

## Sub-probes still UNTRIED (all three need the network; none is a Stage-1 blocker)

Carried from AUDIT 6 unchanged, since I made no web request and none of my six verdicts depends on them:

| Probe | Query that would settle it |
|---|---|
| U-a: whether the §T items still graded `restoration pending` (`stage_1.md:1237–1274`) can be re-saved | WebFetch each URL as cited in the §T row, recording HTTP status, per COR-08 |
| U-b: whether 1998-12-12 remains the earliest amazon.com root capture | `https://web.archive.org/cdx/search/cdx?url=amazon.com/&matchType=exact&from=1994&to=1999&output=json` (`stage_1.md:353` and `:1199` record that every capable prefix query returned HTTP 504 for this corpus — an unanswered, not a null) |
| U-c: completeness of the 3,084-entry Mosaic mirror (A-B3's ask) | locate a second in-window copy of the NCSA "What's New" August-1995 listing and diff entry keys |

---

## Gate recommendation

**REOPEN.** Two blockers, both narrow, both retraction-discipline failures of a class this gate has now caught
three times, and neither one fixable by adjusting wording.

**B-1 (item 6) — the retracted equity leg is still live, in the voice of a correction.**
`_parts/s1_p1.md:142`, `_parts/s1_p3.md:180`, `research/E_supply_ops_finance.md:562` and
`_parts/NUMBER_DEFECTS.md:68–74` all state **`$871,000`** and **`$976,408`** as the *corrected* values, each
citing "orig. l.4301–4302" — a line I read, which contains `3,021,000 / 23 investors / $.3333 / $1,007,000` and
**not** `2,613,000`. The two named sites (`context_appendices.md:598`, `:641`) are closed properly and I have no
complaint about how they were closed. But the repair pass **found this exact pattern once, named it "the item-6
defect in a third place" (IR-03b), fixed that one place, and never swept for the siblings of the site it had just
diagnosed.** The fix is the same four-line move already applied at `_parts/s1_p4.md:492–504`: an addendum to each
footer withdrawing limbs (a) and (b) and pointing at `stage_1.md` §P.2 d8a / §U.8. Until then the folder still
launders a retracted figure into the files a Stage-2 miner reads — which is B-1 in AUDIT 6's words, still true.

**B-2 (item 8) — the withdrawn COR-03 action still governs in the mapping volume.**
`_parts/U_CONCORDANCE.md:48` prints "§P and §R print `11 (per the filing: at 1996-01-01)`" as a governing
instruction; `conflicts.csv` U.17 — edited *in this same wave* — says that exact instruction "is WITHDRAWN and
must not be followed". `adversarial_review.md:34` cites COR-03 as live authority in a deliverable. AUDIT 6's
item-8 finding was that supersession must be marked where the retired entry *stands* and wherever it is
*referenced*; the repair honoured the rule at the three sites it was given and did not apply it to the two it
was not. One marker line at each closes this.

**Non-blocking residuals to carry into the eventual sign-off note** (I verified each; none changes a number):

1. `amazon_s1_numeric_closure_final.md:17` and `:29` — the two false sweep certificates, still uncorrected; and
   `:42` R-4 is now false in the other direction (it says the false bridge still prints live in `_parts/s1_p4.md`
   ll. 102–103; it no longer does). `amazon_s1_causal_lineage_closure.md:37/:86` — marker census still reported as
   a site audit ("all 31 named sites"). All three are "correct by addition" items for the sheet owners; the
   repairer explicitly disclaimed write authority over them.
2. `amazon_s1_audit4_audit5_final.md:409` / `:431` — A-B1's "Lands? YES" line with no closure status appended,
   although the attack is now closed on evidence.
3. `stage_1.md:60–61` "carries the same SEC file number … **on its own face**" — false for the FY1997 10-K405
   (face number `000-22513`; 333-23795 appears only in its incorporation-by-reference notes). One clause.
4. `stage_1.md:2358` and `_MANIFEST.md:38` — "432 records" against a **431** `Claim:` census, twice-verified;
   `_MANIFEST.md:42` — "`derived_arithmetic` populated on exactly the **30**" against **29**, and "111 data rows"
   against the file's 193.
5. `_MANIFEST.md:39` — "the three sites" over a list of four, and the §J gap row labelled §J's neighbour §G.
   `CORRECTIONS.md:295–299` — "four found" over a list of five. `stage_1_claim_records.md:592` — "52 populated
   fields" (I get 49 record-level / 54 raw); the operative "5 at ≥3" is correct.
6. `_parts/U_CONCORDANCE.md:13` — "Final count: 42 canonical conflicts (U.1–U.42)", no U.43 row (disclosed at
   `_MANIFEST.md:67`); `stage_1_claim_records.md:15` — keyed to "the canonical register U.1–U.42";
   `_parts/s1_claims_AJ.md:157–162, 325` — part-local `Conflicts: U.41` on the artifact rows (canonical U.21).
   All three were R-5/R-6/R-9 residuals and remain open.
7. `quantitative.csv` Stage-2 rows (lines 118–194): 28 non-DERIVED rows carry `derived_arithmetic`, against the
   rule Stage 1 is enforced on. Stage-2 owner's item, named because I re-ran the census to certify Stage 1.
8. RD-042's RD-id collision (traceability), and AUDIT 6's UNTRIED U-a/U-b/U-c above.

**Where I tried to break it and could not.** I attacked the four items the brief flagged hardest and the repairs
survived: A-B1's file-number proof (every one of 11 citations lands on the line it claims, from cached filings,
with zero web requests); the §P.2/derived invariants (32/32 and 26/26, and the *only* number the repair changed
in the d-chain is the printed-addend string, which now foots exactly); the `Corroboration:` census (no live count
above what the lineage permits, and the two survivors at 3 justified from their own source lines, not from the
log); and the false-bridge sweep (0 live copies of the `= 944` form anywhere in the folder, once you grep
across line breaks — which is the trick AUDIT 6 used and which the repair then matched). I also confirmed nothing
was overcorrected: no confidence moved, no value or class moved, no claim deleted, and the 11-at-1995-12-31
ruling intact everywhere. **Where it fails, it fails the way it failed before: a repair that fixes the sites it
was handed and re-certifies completeness from a list it drew itself** — four footers with a retracted figure in
the "corrected value" slot, and a concordance still commanding a withdrawn action.

---

## Reproducibility appendix

Scripts, all OUTSIDE the repo, none writing into it: `E:\tmp\qoder_audit7\regs.py` (nine-register parse, arity,
ragged-row check), `parity2.py` (U-block ↔ `conflicts.csv` set parity, stage split, line map), `quant2.py` /
`quant3.py` (DERIVED coverage, stage census and line ranges), `corrob2.py` (the `corroborat*` violation-finder
described at item 9), `corcount.py` / `corcount2.py` (live `Corroboration:` census, current and at `HEAD~5`),
`bridge.py` (newline-normalised false-equation sweep), `arity5.py` (`context_appendices.md` §I/§J table arity),
`corrob.py`–`arity4.py` (earlier passes of the same), plus inline `python -` blocks for the 60-check §P.2
recomputation, the `sources/` `grep -c` denominators test, and the field-level before/after diffs of
`quantitative.csv`, `sources.csv`, `conflicts.csv`, `stage_1_claim_records.md` and `timeline.csv` against
`HEAD~5`. Git used read-only throughout (`log`, `show`, `diff`, `rev-parse`).

**Attestation.** One file created by this run: `founders_playbook/03_quality_control/audit7_stage1_recertification.md`.
No existing file was edited, moved or deleted; no web request was made; no task-management or delegation tool was
used. Where I could not break a repair I say so and show the attempt; where I found the repair's own sweep
narrower than its closure sentence, I named the sites rather than the sentiment.
