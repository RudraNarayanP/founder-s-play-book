# CORRECTIONS.md — company_014_cigna (Stage 1)

Append-only provenance-correction register for the Cigna Stage-1 dossier. Established **at the Stage-1 merge
pass, 2026-10-06** (agent `merge-cigna`), each item verified against the author emission `_parts/s1_p1.md`
and against the held bytes under `sources/` and `research/`. **Nothing here re-tiers, re-dates, re-values or
deletes a claim.** These are key, propagation and schema corrections — the three classes a merge is allowed
to make. A later pass adds a dated entry above this one; it does not delete one.

**Reading rule.** Every `COR-nn` below is printed in the register layer *and* in `stage_1.md`, because a
correction that reaches only the prose leaves the registers teaching the withdrawn form (method §14.10). The
propagation is measured by `tools/gates.py --checks corrections`, and the cell each entry touched is named in
the merge record `03_quality_control/cigna_s1_merge.md`. Where an entry names an annotation, the annotation
was **appended to the end of an existing `notes` / `residual_uncertainty` cell**: no value, date, source key
or confidence on any of the 78 applied rows was altered, and no row was folded.

---

## COR-01 — the dossier-local source tags `CG01–CG16` are superseded by minted ids `S4407–S4422` (2026-10-06)

**What the author emitted.** 16 `sources.csv` rows keyed `CG01`…`CG16`, with the same tags carried in the
`source_id` cells of `quantitative`, `timeline`, `decisions`, `validation`, `failures`, `channels` and inside
notes text (`_parts/s1_p1.md` l.490, merge instruction (1) and (4): "the merge mints global ids … blank them
at merge into the minted ids").

**Correction applied.** `python tools/id_mint.py --count 16 --company company_014_cigna --claim --agent
merge-cigna` allocated **S4407 … S4422** contiguously, above the highest live id (`--audit`: range
S0001–S4406, `next assignable: S4407`). Every register row now carries the minted id; **no register row and no
cell retains a `CG` tag** (verified by regex over all nine files: zero matches). The narrative volume keeps the
author's local tags — they are the reading keys of §B, §K, §T and the claim records — and is bound to the
global space by the mapping table in `stage_1.md` (the merge record, "Provisional-to-global id map").

**Why this is a correction and not a rename.** Ids minted by authors have collided in this project:
`tools/id_mint.py --audit` reports `S4222–S4229` cited by both `company_011_microsoft` and
`company_042_target`, which is why Target's next mint is held (task #31). A local key may not survive into a
global register. **This entry is the authority for treating any `CG01–CG16` row found in a live register from
now on as stale.**

**Propagated to.** `sources.csv` S4407 `notes` cell · `stage_1.md` merge record.

---

## COR-02 — the 4-row and 6-row emissions are bound to `validation.csv` and `failures.csv` respectively (2026-10-06)

**The ambiguity.** `validation.csv` and `failures.csv` share a byte-identical 11-column header, so
`tools/merge_census.py` prints both blocks as `AMBIGUOUS:validation.csv,failures.csv` and cannot attribute
them (it did so before this merge and does so after — a schema property, not a defect in the emission).

**Correction applied — decided by reading, not by position.** (i) the part's own block headings name the
targets (`### \`validation.csv\` — 4 rows` at l.576, `### \`failures.csv\` — 6 rows` at l.589); (ii) the
author's stated counts agree (4 and 6, `_parts/NOTES_cigna_p1.md`); (iii) the rows' semantics agree with the
registers' control meaning — the 4-row block's `what_it_demonstrated` cells are all positive validation claims
(health pre-tax +48%; the buy-a-plan pattern repeated; three independent court records; the 2018 indenture
designation), the 6-row block's are all adverse signals (101.8 combined ratio; $84.8M 1978 losses; reserves
96→111% of earned; the 5%-of-income parent-and-other loss; goodwill write-downs; three respondent appearances).
4 + 6 = 10 = the census's unattributed total, with no row in both groups.

**Propagated to.** `validation.csv` first row `notes` · `failures.csv` first row `notes` · `stage_1.md` merge
record. **The census's `AMBIGUOUS` line is expected to persist after this correction** — it is the tool's
schema blindness, now adjudicated on the record rather than left to a future pass.

---

## COR-03 — the probe's 17:20 header claim ("both ancestor dates occur 0 times in every held byte", Stage 1 = **T3 register**) is withdrawn at the instruction layer (2026-10-06)

**The withdrawn form.** The first version of `research/A_chronology_feasibility.md`'s verdict line, written
against the 17:20 corpus (4 non-SEC documents), asserted that the two ancestor dates "occur **0** times in
every held byte" and graded Stage 1 **T3 register, PROVISIONAL**.

**What the bytes print now.** At 17:22-17:23 the fleet mine landed six layers; `1792` occurs **2** times, both
inside `sources/periodicals/INAC2115_1979_djvu.txt` (l.5, l.371) — re-measured by the author and re-measured
again for this merge; `1872` remains **0**, and the lone `1850` is an ERIC sentence about New Haven. The probe
regraded itself to **T2 core, PROVISIONAL** on the lineage frame, keeping the T3 reading for the
strict-registrant frame (§7 row 2). The retraction stayed **inside the probe file** and had never reached the
instruction layer until this entry.

**Correction applied, and its limit.** This entry registers the withdrawal so no downstream pass resurrects
either half. It **does not** re-tier anything: Stage 1 stays T2 core PROVISIONAL (lineage frame) **and** T3
register (strict-registrant frame), both carried as states in `stage_1.md` §boundary, §A, §B.2, §R and §U.4,
never averaged. `1872`/1850s for the second ancestor remains **UNTRIED** — a query-scope silence, explicitly
not a null (FR-7).

**Propagated to.** `conflicts.csv` U.2 `residual_uncertainty` cell · `quantitative.csv` census row `notes`
cell · `stage_1.md` §U.2, §U.4 and the merge record.

---

# REPAIR PASS 2026-10-06 — agent `repair-cigna`, Stage-1 audit 1 (`03_quality_control/cigna_s1_audit1.md`)

Nine entries follow (COR-04…COR-12), one per blocker/finding. Each was **re-measured on the bytes before
being written**: nothing below rests on the auditor's say-so. The rules the entries obey: a withdrawn claim
stays **readable** (its exact words are quoted, then refuted by a file+line, never deleted); corrections go to
the register layer **and** the volume that carried the withdrawn text; and **no quotation was rewritten to
force a match** — non-verbatim spans are marked, not repaired (COR-09). Ids `S4529`/`S4530` were minted for
COR-08 with `python tools/id_mint.py --count 2 --company company_014_cigna --claim --agent repair-cigna`
(above the highest live id; the `S4222–S4229` collision band was not entered).

---

## COR-04 — B-1: the null "No held byte prints this registrant's own date of incorporation" is WITHDRAWN; the held byte prints **2018-03-06** (2026-10-06)

**The withdrawn form, verbatim.** `stage_1.md` l.132 (Header): "**No held byte prints this registrant's own
date of incorporation.**" The same null in nine further places — §boundary row 2 "start **UNKNOWN** — no held
byte gives Halfmoon Parent, Inc.'s incorporation date"; §A.3 "Its first EDGAR appearance is 2018-05-16" (as
the first date the entity has); §A's unknown-list "the registrant's own incorporation date"; §B.2 "Date of
incorporation — **UNKNOWN — no held byte prints it.**"; §N row 4 "its incorporation date itself (FR-2)"; §Q
"(no date) … incorporation of Halfmoon Parent, Inc. — **UNKNOWN, no held byte**"; §R "nonexistent /
date-unknown"; §U.1 "**no held byte gives the registrant's own incorporation date**" at **CONFIDENCE: High**;
claim record A02 "No held byte anywhere in the corpus prints the registrant's own date of incorporation",
Conf: High. Registers: `timeline.csv` r13, `data_gaps.csv` r1, `conflicts.csv` U.1. Companions:
`stage_1_index.md` U.1, `_MANIFEST.md`.

**The byte that refutes it** (verified with `grep -n "Originally incorporated"` this pass, before any edit):
`sources/sec/0001140361-18-024107_s002268x1_s4.htm` **l.48371** —
`(Originally incorporated on March 6, 2018 under the name Halfmoon Parent, Inc.)`
— the caption of Annex E, "FORM OF AMENDED AND RESTATED CERTIFICATE OF INCORPORATION OF CIGNA CORPORATION",
inside accession **S4407**, the dossier's own most-cited carrier. A second, stronger print in the same body:
**l.5011** — `New Cigna was incorporated on March 6, 2018, solely for the purpose of effecting the mergers
and, immediately after the mergers, New Cigna will be renamed "Cigna Corporation"` — and the name chain is
carried by the same document at **l.279** (`Halfmoon Parent, Inc., which we refer to as New Cigna`) and
**l.370**, so the date attaches to **the registrant itself**, not to a predecessor.

**Three attribution guards, applied because the same date prints other legal persons.** (1) `l.5033` and
`l.5037` print "Cigna Merger Sub **was incorporated on March 6, 2018**" and "Express Scripts Merger Sub **was
incorporated on March 6, 2018**" — same day, **different legal persons**; the registrant's date is not
inferred from them and they are not counted with it. (2) The 12 literal occurrences of `March 6, 2018`
(re-measured `grep -o | wc -l`: s4.htm **12**, each of the 4 amendments **12**, ex3-3.htm **1**) are
**one lineage printed many times** — method §3's filing-lineage rule, so corroboration stays **1**. (3) The
auditor named `…ex3-3.htm` as a second incorporation carrier; **re-measured and only partly sustained** —
ex3-3 l.37 prints `dated as of March 6, 2018` under the title line `BY-LAWS of HALFMOON PARENT, INC.`, which
is a by-law date, **not** an incorporation recital. It corroborates existence on or before that date; the
date-of-incorporation claim rests on l.48371 and l.5011 alone.

**Correction applied.** Line 3's origin re-dated to **2018-03-06** (Delaware, organised as Halfmoon Parent,
Inc.), class **FACT**, evidence carried as **one lineage (S4407)**, confidence **High that the byte prints it /
Medium as the Delaware effective date** — the ceiling is Medium because the print is inside a *form* of
charter and a merger-description paragraph, while the **as-filed** certificate remains unheld. Standing and
**unchanged**: "not 2018-05-16, which is a filing floor"; the 2018-12-20 rename; the whole identity finding
(the 1981 corporation is a *subsidiary of* the shell); and §D's "no held byte places any Halfmoon activity
**inside the window**" — 2018-03-06 is out-of-window by 22+ years, so that null survives and the
strict-registrant T3 reading is **strengthened**, not weakened. No FETCH REQUEST is raised or closed: **FR-2
survives, narrowed** from "the date is nowhere" to "the *as-filed* charter and the first 10-K remain unheld".

**Propagated to.** `stage_1.md` Header l.132, the three-lines paragraph, §boundary row 2, §A.3, §A
unknown-list, §B.2, §N, §Q, §R, §U.1, claim record A02, and the repair-record table · `timeline.csv` r13
(`UNKNOWN` → `2018-03-06`, `UNKNOWN` → `FACT`, source `S4408` → `S4407`) · `data_gaps.csv` r1 (ANSWERED from
held bytes; FR-2 narrowed) · `conflicts.csv` U.1 (`best_supported_interpretation` + `residual_uncertainty`).

---

## COR-05 — F-2: the PPO/managed-care vocabulary null is **in-window**, not **archive-wide**; `managed care` occurs 5× in the held out-of-window S-4 lineage (2026-10-06)

**The withdrawn form, verbatim.** `stage_1.md` §A l.170: "the PPO/managed-care vocabulary entirely
(**absent from every held byte** — searched this pass)".

**What the bytes print.** Re-measured with `grep -rnw -E "PPO|managed care" sources/`: `managed care` occurs
**5 times across 4 lines** in held `sources/sec/0001140361-18-024107_s002268x1_s4.htm` (**l.26112, l.29379,
l.33424, l.47186**) and the same count in each of the four amendments, plus **1 line each** in
`sources/sec/0000950159-19-000007_0000950159-19-000007.txt` and `…_cigna8k1-7.htm`. All of it is the
out-of-window 2018/2019 SEC material about Cigna Corporation. **`PPO` with word boundaries occurs 0 times in
every held byte** (17 hits corpus-wide, none word-bounded — re-run: `grep -rnw "PPO" sources/ | wc -l` = 0),
and every 1979–1995 byte (`INAC2115_1979_djvu.txt`, the three court records, the four CIA bytes, the Wilsen
report) returns **0** for both terms.

**Correction applied — half the sentence was true and is kept.** The claim is re-scoped, not reversed: the
**`PPO` half stands as an archive null** (0 word-bounded occurrences in any held byte, in-window or out),
while the **`managed care` half is withdrawn as archive-wide and re-asserted as in-window-only**, with the
out-of-window occurrences named so the next reader does not re-derive a false zero. §E, §H and §S already
scope the same fact to 1979–1995 and are unchanged; §D's "the completion is UNKNOWN" and §R's "no PPO byte"
survive on the in-window reading.

**Propagated to.** `stage_1.md` §A l.170 and §E adjacency paragraph · `data_gaps.csv` r5
(`best_available_evidence`: "absent from held bytes" → "absent **in-window**; 5× out-of-window in the S-4
lineage") · `sources.csv` S4407 `notes` (the vocabulary occurrences are recorded against the lineage that
prints them).

---

## COR-06 — F-3: the INA Healthplan quotation is NOT truncated at the shelf edge — the completion prints four lines later in the same byte (2026-10-06)

**The withdrawn form, verbatim.** `stage_1.md` §D l.232: `"INA Healthplan provides comprehensive medical
services, including preventive …"` — "(text truncates at the shelf edge … **the completion is UNKNOWN**)"; and
§E.1 l.258 "**No plan design, no premium pricing**, no provider network description…".

**What the byte prints.** `sources/periodicals/INAC2115_1979_djvu.txt` **l.2012-2019** continues without
break: `check-ups, physician office visits, and hospitalization, for a pre-determined monthly fee. Individuals
and families are able to obtain health care services at a cost which they know in advance. Subscribers join
the plan primarily through their employers.` There is no shelf-edge truncation — the sentence ends inside the
held text layer.

**Correction applied.** The full span is quoted (l.2012-2019) and the two facts it prints are credited: a
**prepaid monthly-fee product design** and an **employer-based subscriber channel**. §E.1's "no plan design,
no premium pricing" is therefore **withdrawn as written and re-scoped**: what stays UNKNOWN is the *fee level*,
provider network, utilization and any membership/policy/enrollment **count**. **One of the auditor's own
supporting zeros did not reproduce and was not carried forward:** the brief says "`enroll` 0 hits, `policy
count` 0 hits corpus-wide". Re-measured: `policy count` **is** 0, but `enroll` occurs **11 times** — every one
of them in `sources/periodicals/micro_IA41153629_0618_djvu.txt` (l.50, l.408, l.912, l.1166, l.1173, l.1320,
l.1327, l.1509, l.1561, l.1593, l.1650), the 1992 ERIC **charter-school** decoy already registered as S4418,
where the word means parents enrolling children in school. `enroll` = **0** in every insurance, court and
corporate byte, so the substantive claim survives; the census statement was rewritten to the measured form in
§E.1 rather than copied.

**Propagated to.** `stage_1.md` §D l.232 (value + confidence cells), §D.2, §E row 3 of the INA block, §E.1 ·
`timeline.csv` r9 (the 1979 INA Healthplan row's `event` text now carries the printed design) ·
`data_gaps.csv` r2 (membership/enrollment gap re-scoped to *counts*, design no longer a gap).

---

## COR-07 — F-4: "no failure disclosure in the held report" is false — the same report prints an in-window adverse product-line result (annuity revenues −5% to $195.8M); `failures.csv` gains row 7 (2026-10-06)

**The withdrawn form, verbatim.** `stage_1.md` §D l.234: "Nothing independent: no membership figures, no
plan-level results, **no failure disclosure in the held report**."

**What the byte prints.** `sources/periodicals/INAC2115_1979_djvu.txt` **l.1754-1760**: `Annuity operations
produced pre-tax income of $8.5 million, an increase of 17% over 1978. Revenues decreased 5% to $195.8
million. This resulted from the significant increase in interest rates late in the year, which made available
alternate competitive investments that were attractive to buyers.` The segment table prints the same cell at
l.1645 (`Annuity 195,825 24`). Also in the same report: a decline in annuity purchases (l.2217), a Blyth
Eastman Dillon operation loss (l.503, l.516) and the 1975 P&C "loss of $2 million" (l.444) — the last the
dossier already carries at §K.2.

**Correction applied — scoped, not reversed.** The sentence is true of the **prepaid-health unit** (the report
prints no failure narrative about INA Healthplan specifically) and false of **the held report**, which is what
it said. It is rewritten to the narrower scope and the refuted reading is superseded by a new adverse row:
`failures.csv` **r7**, 1979, annuity-line revenue decline −5% to $195.8M with the company's own stated cause,
`S4410`, CONTEMPORANEOUS self-report, Medium. This is the health-insurer-specific omission class: an in-window
adverse product-line line inside the one Tier-1 self-report.

**Propagated to.** `stage_1.md` §D l.234 · §M (new 1979 annuity row) · §K.2 (new line) · `failures.csv` r7 ·
`_MANIFEST.md` failures row (6 → 7 rows) · `stage_1_index.md` register counts.

---

## COR-08 — F-5: two held in-window CIGNA-naming CIA bytes were unregistered; they are now `S4529` and `S4530` (2026-10-06)

**The state corrected.** `stage_1.md` §T presents CG01–CG16 as the provenance set and §B.1 the same, yet
`sources/periodicals/cia-readingroom-document-cia-rdp90g00152r001102380002-3_djvu.txt` and
`…rdp91-00929r000200960032-0_djvu.txt` were **mined by A4** (its table rows class `BARE_WORD_MATCH`) and are
**held on disk**, but carried no `sources.csv` row and no §T line. No volume claim was falsified; the defect
is a register that under-lists its own shelf.

**What the bytes print (re-read, and the two are NOT alike).**
`rdp90g…` (36,048 B, 1987): **l.1431** `CIGNA` as an address-block header over `1600 Arch Street - 3 Penn
Center, Suite 110 / Philadelphia, PA 19103`, and **l.1436** `The CIGNA Consumer Marketing Department offers
insurance and non-insurance products to financial institutions through their customer base` — a genuine
in-window corporate naming with a product-channel sentence.
`rdp91-00929…` (24,680 B; index date 1983, title 2009, flagged `in-window MISMATCH` by A4): **l.1071**
`water-~nitric acid system. CIGNA, Rez DI CAVE, S.ej3` — an OCR mangle of a **journal-article author list**
(Cigna/Reza/Di Cave/Giona/Mariani, translated from *Chimica Industriale*, Milan 1964). **It is a surname
decoy, not a company naming.** Registering it as evidence of the company would have been the error; it is
registered as a decoy, which is what the hit actually is.

**Correction applied.** Two `sources.csv` rows in the S4416 naming-only pattern: **S4529** (rdp90g,
NAMING-ONLY, Tier 3, Medium, `relevant_passage` = the Consumer Marketing line at l.1436 with the l.1431 address
block) and **S4530** (rdp91, **DECOY — personal surname in an OCR'd bibliography**, Tier 4, no claim support).
Two §T lines added; §I and §B.1 gain one enumerating sentence each so the bare-word layer is visible.
**Nothing that was true became false:** M02 still holds that the corpus's one in-window *divestiture* naming is
the 1988 Africa Review line, and §I's "no named competitor" survives — neither new row names a rival or an
event. Both stay **outside** the chronology: no date-moving claim cites them.

**Propagated to.** `sources.csv` S4529, S4530 · `stage_1.md` §T (two rows + the independence ledger), §I bad-name
adjacency row, §B.1 census row · `data_gaps.csv` r6 (the naming-layer census row now counts them) ·
`_MANIFEST.md` / `stage_1_index.md` sources counts (16 → 18 rows).

---

## COR-09 — F-6: four quoted spans are not verbatim in the carriers cited; they are MARKED, not rewritten (2026-10-06)

**Rule obeyed.** A quotation is never edited to make a matcher pass. Each span below keeps its reading value
and gains an honest label; where the byte's wording matters, the byte's wording is substituted and the
paraphrase is recorded as the withdrawn form.

| # | site | the span as quoted | what the carrier prints | correction |
|---|---|---|---|---|
| (a) | §G l.288 | `"through an exchange of stock … accounted for as a purchase"` | `INAC2115_1979_djvu.txt` **l.3679**: "…through an exchange of stock and **has accounted for the transaction** as a purchase" | re-quoted verbatim (claim record N01 already carried it correctly — the §G cell was the loose one) |
| (b) | §U.5 CLAIM A l.554 | `"79 candidate rows; 12 mined; 65 untried."` | probe `research/A_chronology_feasibility.md` **l.399-400**: "79 candidate rows in the harvest index; 12 items mined; 65 left untried at the --limit" | re-quoted verbatim; the condensation is the withdrawn form |
| (c) | `sources.csv` S4417 `relevant_passage` | `"1018 filings enumerated; UNANSWERED slices: (none)"` | `sources/_index/_INDEX.md` **l.4** prints the first clause ("1018 filings enumerated; 0 submissions rows dropped…"); **l.45-47** prints the heading `## UNANSWERED slices (never report these as absent)` with `(none)` under it — contiguous **nowhere** | split into two locators, labelled **COMPOSITE (two locators, not contiguous)** |
| (d) | §B.1 l.186 | `"at a 23% annual compound rate, compared with 9% growth for the overall field"` | byte **l.382** prints "grown **at a23%** annual compound rate," — an OCR space loss; the dossier discloses OCR damage elsewhere (§K.1) but silently repaired it here | kept readable, marked **(byte prints `at a23%`; space supplied — OCR damage, disclosed repair)** |

**Also corrected on the same lens, and only partly.** §F l.270 "(searched this pass: `membership` **absent**
from INA report)" — re-measured: the token occurs **once** at **l.2618** ("suggestions for **board**
membership"). The load-bearing half survives untouched (no membership *count* anywhere: `enroll` 0,
`policy count` 0 corpus-wide), so the fix is the wording "absent" → "**no membership count printed; the one
occurrence is a board-membership sentence at l.2618**". §E01/E03's claim that membership and PPO print nowhere
in held bytes is likewise **kept** for `PPO` (word-bound 0) and re-scoped for `managed care` per COR-05.

**Propagated to.** `stage_1.md` §G l.288, §U.5, §B.1 l.186, §H l.303, §F l.270, claim records N01/E03 ·
`sources.csv` S4417 (`relevant_passage` + `notes`), S4421 `notes` · `data_gaps.csv` r2 `best_available_evidence`
(the `membership` wording).

---

## COR-10 — F-7: two derived counts do not reproduce from the bytes — "one lineage of 23 files" measures **20**, and A4's own 96 − 12 ≠ 81 (2026-10-06)

**(i) The file count.** `stage_1.md` l.57 and l.76 say CG01/S4407 is "ONE lineage incl. 4 amendments +
exhibits (**23 files**)". Measured this pass (`ls sources/sec/ | grep -v meta.json`, 5 accessions
0001140361-18-024107 / -029349 / -031849 / -032199 / -032454, 4 documents each): **20**. The surrounding
counts also re-measured: **30** filing documents in all of `sources/sec/`, **35** non-meta files there
including **5** index artefacts (`_MANIFEST.csv`, `_PLAN.csv`, `_RUN.json`, `_UNANSWERED.csv`, `_SKIPPED.csv`),
and **22** only if the separate 2018-12-20 8-K accession (S4408, 2 files) is folded in — which it is not,
being a different filing. **23 reproduced from no counting rule I could construct**, and the figure is
inherited from the probe (`research/A_chronology_feasibility.md` l.117), i.e. it was never measured on this
volume's own shelf. Corrected to **20** with the command that produces it; the count change is **cosmetic to
the lineage finding** — one lineage however many files it holds, so no corroboration moves.

**(ii) The census non-closure.** `stage_1.md` §U.5 and six other sites carry "96 / 12 / 81" from A4 l.5
(quoted there verbatim, and correctly). **96 − 12 = 84, not 81**, and the earlier reading the probe caught is
likewise short: **79 − 12 = 67, not 65**. Both were re-read from the carriers (`research/A4_harvest_mine.md`
l.5; `research/A_chronology_feasibility.md` l.399-400). **The figures are NOT corrected toward arithmetic** —
A4 prints them and the register must keep what its carrier prints. What was missing is the *named gap*: the
volume's RD-134 hedge ("a capped enumeration is a sample, never a census") is right but did not say that its
own three numbers do not close. The non-closure is now stated wherever the census is carried, and it is
stated as a defect in the **enumeration record**, not in this dossier's reading of it.

**(iii) Checked and clean, recorded so the absence is not silence.** §K.1's damaged 1978 equity cell "1 307"
is internally inconsistent with the printed +15% (1,526/1,307 = +16.8%) and the dossier labelled it
damaged-print rather than repairing it — correct handling, unchanged by this pass.

**Propagated to.** `stage_1.md` l.57, l.76 (id map + folds paragraph), §J l.328, §S G5, §U.5, UNTRIED item 4,
claim record P01, merge-record table · `sources.csv` S4407 `notes` (20 measured), S4421 `relevant_passage` +
`notes` (non-closure named at the carrier) · `data_gaps.csv` r5 and r10 (the 81-row backlog rows) ·
`quantitative.csv` census row `notes`.

---

## COR-11 — F-8: the coda duty (evidence · mechanism · alternative · confidence) was complete in §L.1 only; §H.1 and §D.2 each lacked one element (2026-10-06)

**What was short.** §L.1 is exemplary and is unchanged. §H.1 carried evidence, "mechanism UNKNOWN" and an
alternative but **no confidence word**; §D.2 "Assessment" carried evidence and an implicit confidence but
**named no alternative explanation and no confidence word** (method §7/§16).

**Correction applied.** Two clauses added, each bounded by what the registers already decide: §H.1 now closes
with a named confidence **and keeps its mechanism UNKNOWN**; §D.2 now names its alternative explanation (the
prepaid build-out may have been ordinary portfolio expansion rather than an experiment-shaped entry — nothing
in the byte distinguishes the readings) and a confidence **matching `decisions.csv`'s own split label** ("Low
as a decision-as-decision / Medium as print"), so the coda cannot drift above the register. §R's KNOWABLE /
NOT KNOWABLE / UNKNOWN column already complies and was not touched. **No claim was upgraded** by either
clause; the added words are confidence labels for text already on the page.

**Propagated to.** `stage_1.md` §H.1, §D.2 · `decisions.csv` r1 `notes` · `quantitative.csv` industry-estimate
(ESTIMATE) row `notes`.

---

## COR-12 — F-9: a published live count in `_MANIFEST.md` was stale (1,003 → measured 1,111 words), and every count this repair pass moved is re-published (2026-10-06)

**What was stale.** `_MANIFEST.md` **l.55** (the auditor cited l.54 — off by one line; the figure and the file
are right) publishes `_parts/NOTES_cigna_p1.md` at **1,003 words**. Measured: `wc -w` = **1,111**,
`wc -c` = **7,830** — bytes match what was published, so the word figure alone drifted; the file was edited
after its count was taken.

**Correction applied.** The row is republished at the measurement. The auditor's other 17 counts reproduced
exactly and were left alone. **This pass then moved further counts, and each is re-published in the same
edit rather than recollected**: `failures.csv` 6 → **7** rows (COR-07), `sources.csv` 16 → **18** rows and
16 → 18 keys with the minted S4529/S4530 (COR-08), `stage_1.md` word/byte count (COR-04…COR-11 text), and the
register total **78 → 79 rows**. Every figure quoted in `_MANIFEST.md`, `stage_1_index.md` and the volume's own
register-application table after this pass is `wc`-measured on the final bytes; a file cannot publish its own
final size, so `_MANIFEST.md` does not list itself.

**Propagated to.** `_MANIFEST.md` (the NOTES row, the `sources.csv`/`failures.csv` rows, the register total,
the volume row) · `stage_1_index.md` (register counts, totals) · `stage_1.md` merge-record application table
(16 → 18 sources, 6 → 7 failures, 78 → 79 total) · `sources.csv` S4529/S4530 `notes` (the mint that produced
the new key range).

---

## Not corrected, and why (recorded so the absence is a decision, not an oversight)

1. **No fold, no dedup, no row withheld.** 78 rows requested, 78 applied. No `sources.csv` row was minted for
   the four S-4 amendments or the exhibits of acc. 0001140361-18-024107 (one lineage), for CG03's two exhibits
   (one accession), or for CG07's md5-identical pair on two shelves (one document).
2. **The 1982 combination stays a hypothesis** (U.3): 0 held bytes pair `1982` with a merger verb; it lives in
   `conflicts.csv` and `timeline.csv` as an unattested assertion, never as a fact. Nothing here "corrects" it
   toward fact or toward null.
3. **FR-8** (pre-1979 outside witnesses to the 1792 claim) has **no `data_gaps.csv` row**, because the author
   emitted none and the merge does not invent register rows; its home is UNTRIED item 8 in `stage_1.md` and the
   `residual_uncertainty` cell of `conflicts.csv` U.2. Named here so it is not lost.
4. **`research/_EVIDENCE_CACHE.md`** is still absent. `data_gaps.csv` row 11 asks for it "at merge", but the
   cache is not among the deliverables this merge claimed (`stage_1.md`, the nine registers, `_MANIFEST.md`,
   `stage_1_index.md`, `CORRECTIONS.md`). The row stays open and is reported as an uncarried follow-up in
   `03_quality_control/cigna_s1_merge.md`, not silently closed.

## Refused at the repair pass — claims left standing because the bytes support them (2026-10-06, `repair-cigna`)

These were named or touched by audit 1 and were **not** changed after re-measurement. A withdrawal requires a
byte, not a preference.

1. **§D l.235 "no held byte places any Halfmoon activity inside the window"** — survives COR-04 unchanged:
   2018-03-06 is 22+ years outside 1979–1995, so the in-window null is untouched. Only the *date* claim was
   false, and only that was withdrawn.
2. **"Not 2018-05-16 (a filing floor)"** — survives in full. `sources/_index/submissions.csv` still has no row
   for CIK 1739940 before 2018-05-16, and an incorporation date printed in a 2018-05-16 filing does not move
   the EDGAR floor.
3. **The identity finding** — "Cigna was incorporated in Delaware in 1981" still describes a different legal
   person that became a *subsidiary of* the registrant (S-4 l.4995, l.23191; 8-K l.163-166). COR-04 re-dates
   the shell; it does not merge the two persons.
4. **`PPO` as an archive-wide null** — kept (COR-05): `grep -rnw "PPO" sources/` = **0** across all 43 held
   text/HTML bytes. Only `managed care` was re-scoped.
5. **The membership/policy-count null** — kept (COR-09): `enroll` = 0 and `policy count` = 0 corpus-wide; only
   the word "absent" for the *token* `membership` was corrected, because the token prints once at l.2618.
6. **The 1982 combination as UNATTESTED HYPOTHESIS** and **1872 as UNTRIED** — untouched by this pass; no new
   byte reached either.
7. **`_parts/s1_p1.md` and `_parts/NOTES_cigna_p1.md`** — read-only emissions of record; the stale 1,003-word
   count was republished in `_MANIFEST.md` (COR-12), **not** by editing the author's log.
8. **`research/A4_harvest_mine.md`'s own 96/12/81** — not corrected toward 84 (COR-10ii): A4 prints what it
   printed; the register quotes its carrier and names the non-closure instead of rewriting it.
9. **The tier frames** — Stage 1 stays T2 core PROVISIONAL (lineage) **and** T3 register (strict-registrant),
   both as states. COR-04 strengthens the T3 reading; nothing was re-tiered or averaged.
10. **The auditor's secondary carrier for COR-04** — `…ex3-3.htm` is recorded as printing `dated as of March 6,
    2018` under `BY-LAWS of HALFMOON PARENT, INC.` (l.37), which is **not** a date-of-incorporation recital.
    The blocker stands on s4.htm l.48371 and l.5011; the ex3-3 half of the citation was refused as stated.
