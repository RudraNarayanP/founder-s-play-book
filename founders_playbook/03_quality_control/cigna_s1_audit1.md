# Cigna Stage 1 — AUDIT 1

Agent `cigna-audit1`. Independent first audit of `company_014_cigna` Stage 1. I did not write the part, did not
merge it, and **repaired nothing** — this file is the only corpus file I created. Web calls this pass: **0**.
Claim: `python tools/scaffold.py claim --path founders_playbook/03_quality_control/cigna_s1_audit1.md
--agent cigna-audit1 --title "Cigna Stage 1 audit 1"` → `CREATED … (owner=cigna-audit1 ttl=240 min,
sections=0, 39 words)` (accepted; no live-owner refusal).

Read first: `03_quality_control/STAGE1_AUTHOR_BRIEF_SHARED.md`; `MASTER_RESEARCH_LOG.md` (see §A-9 — the
entries I was told to read, RD-138–RD-141, are **not in the log**);
`_parts/NOTES_cigna_p1.md`; `03_quality_control/cigna_s1_merge.md`; then `stage_1.md` (14,513 w),
`_MANIFEST.md`, `stage_1_index.md`, `CORRECTIONS.md`, all nine registers (78 rows), and the bytes under
`sources/` (30 filing documents + 11 periodical/text bytes + 2 corporate_print + 4 index artefacts).

---

## VERDICT: **FAILED** — 1 blocker (B-1), 8 findings

The volume is otherwise the strongest first-pass product of tonight's pipeline I can see: merge integrity
reproduces exactly, the validation/failures adjudication is right, every number recomputes from the filed
print, and the health-insurer traps (earned-vs-written, combined-ratio-as-margin, restated-vs-contemporaneous)
were all avoided. B-1 is a **false byte-state claim carried at High confidence into the header, the boundary
and three registers**, contradicted by a held byte the author named as unexamined. Repairing it converts this
to **PASS-WITH-FINDINGS**; it needs no new retrieval — the carrier is already on disk.

---

## Blockers

### B-1 — "No held byte prints this registrant's own date of incorporation" is false; the byte prints **2018-03-06**

* **Claim, as the volume states it** (`stage_1.md` l.132, Header): "**No held byte prints this registrant's own
  date of incorporation.**" Repeated at: §STAGE BOUNDARY row 2 ("start **UNKNOWN** — no held byte gives
  Halfmoon Parent, Inc.'s incorporation date"); §A.3 ("Its first EDGAR appearance is 2018-05-16"); §B.2 row
  "Date of incorporation — **UNKNOWN — no held byte prints it.** Not 2018-05-16 (a filing floor)"; §Q row
  "(no date) … incorporation of Halfmoon Parent, Inc. — **UNKNOWN, no held byte**"; §R ("nonexistent /
  date-unknown"); §U.1 ("**no held byte gives the registrant's own incorporation date**", **CONFIDENCE: High**);
  claim record A02 ("No held byte anywhere in the corpus prints the registrant's own date of incorporation",
  Conf: High); §D "Registrant first experiment … Route FR-2".
* **Registers carrying it:** `timeline.csv` row 13 (`date_or_range = UNKNOWN`, "no held byte prints it");
  `data_gaps.csv` row 1 ("No held byte; the instruments that would print it … are indexed but UNHELD");
  `conflicts.csv` U.1 `best_supported_interpretation` ("registrant's own incorporation date is printed nowhere").
* **Companion files:** `stage_1_index.md` U.1 row ("the registrant's incorporation date printed nowhere");
  `_MANIFEST.md` family (a) row / FR-2.
* **What the carrier prints.** `sources/sec/0001140361-18-024107_s002268x1_s4.htm` **l.48371**:
  `(Originally incorporated on March 6, 2018 under the name Halfmoon Parent, Inc.)` — inside Annex E,
  "FORM OF AMENDED AND RESTATED CERTIFICATE OF INCORPORATION OF CIGNA CORPORATION", i.e. **the registrant's own
  certificate of incorporation, in the accession the dossier itself cites 20 times as S4407/CG01**. Also in the
  held exhibit `sources/sec/0001140361-18-024107_s002268x1_ex3-3.htm`. Reproduced command and result:
  `grep -n "Originally incorporated" sources/sec/0001140361-18-024107_s002268x1_s4.htm` → `48371:…`;
  occurrences of the literal `March 6, 2018`: s4.htm **12**, each of the four amendments **12** each,
  ex3-3.htm **1** — all one lineage (S4407), so it is **one witness printed many times, not corroboration**;
  `grep -c "March 6, 2018\|2018-03-06" stage_1.md *.csv _parts/s1_p1.md` → **0 in every file**: the real date
  appears nowhere in the dossier, so this is an omission/under-claim, not an invented value.
* **Severity: blocking.** It is the load-bearing Line-3 date, the boundary's front edge under the
  strict-registrant reading, and it is asserted at High confidence. Direction matters for the calibration
  message: nothing was invented, the corpus was **under-read** because the author skipped "byte-identical-lineage
  boilerplate" exhibits (`_parts/NOTES_cigna_p1.md` §"What I did NOT examine") and the probe never mentions
  `March 6`, `ex3-3`, `organised` or `originally incorporated` at all.
* **Minimal honest repair** (no FETCH REQUEST): re-date Line 3's origin to **2018-03-06, organised in Delaware
  as Halfmoon Parent, Inc. — FACT, printed by the registrant's own Annex E certificate form and held
  `ex3-3.htm` (S4407 lineage, l.48371)**. Keep standing, unchanged: "not 2018-05-16 (that is a filing floor)",
  the rename 2018-12-20, and the whole identity finding (the 1981 corporation is a **subsidiary of** the shell).
  Change `timeline.csv` row 13 `date_or_range` UNKNOWN → `2018-03-06` (evidence_class FACT, source S4407);
  `data_gaps.csv` row 1 → the date is ANSWERED from held bytes, and FR-2 survives **narrowed** to "the *as-filed*
  charter and the first 10-K remain unheld"; `conflicts.csv` U.1 residual → "Delaware registry may still print a
  different effective date; the held form prints 2018-03-06"; §boundary row 2 start → 2018-03-06 (still
  out-of-window by 22+ years, so the T3 strict-registrant reading is **unharmed and strengthened**); and the
  2018-03-06 date must be labelled **one lineage** everywhere it is cited, never counted as a second witness.

---

## Findings (non-blocking, numbered)

**F-2 (Medium) — §A's PPO/managed-care census claim is contradicted by a held byte.** §A: "the PPO/managed-care
vocabulary entirely (**absent from every held byte** — searched this pass)". `managed care` occurs **5×** in
held S4407 `…s4.htm` (l.26112, 29379, 33424, 47186 + 1) and 5× in each amendment, and 1× each in
`0000950159-19-000007_*` (l.189/l.145): `grep -rnw -E "PPO|managed care" sources/` → 27 hits, all in out-of-window
2018-19 SEC bytes; **0** word-bounded `PPO` and **0** `managed care` in any 1979-1995 byte. Repair: scope to
"absent from every **in-window** held byte; present only in the out-of-window 2018 S-4 lineage about Cigna
Corporation". §E, §S and §R state the same fact *correctly scoped*, so the fix is one clause.

**F-3 (Medium) — a "truncated" quote whose completion is in the same byte.** §D row "Product of the
experiment": `"INA Healthplan provides comprehensive medical services, including preventive …"` — "(text
truncates at the shelf edge … the completion is **UNKNOWN**)". The held byte continues at
`INAC2115_1979_djvu.txt` l.2014-2019: "check-ups, physician office visits, and hospitalization, **for a
pre-determined monthly fee**. Individuals and families are able to obtain health care services at a cost which
they know in advance. **Subscribers join the plan primarily through their employers.**" Consequently §E.1's
"No plan design, no premium pricing" is partly contradicted (a monthly-fee prepaid design and an employer-based
distribution channel are printed). Repair: quote the completion, keep `UNKNOWN` for membership counts and
plan-level results (those genuinely are absent — `enroll` 0 hits, `policy count` 0 hits corpus-wide).

**F-4 (Medium) — "no failure disclosure in the held report" is false, and `failures.csv` is incomplete on the
author's own single carrier.** §D: "Nothing independent: no membership figures, no plan-level results, **no
failure disclosure in the held report**." The same report prints: Annuity operations revenues "**decreased 5%**
to $195.8 million" with a stated cause (l.1754-1760; table line l.1645 "Annuity 195,825 24"), a decline in
annuity purchases (l.2217), a Blyth Eastman Dillon loss (l.503, l.516) and the 1975 P&C pre-tax **loss of $2M**
(l.444 — the only one of these the dossier carries, and it does carry it, §K.2). Repair: scope the sentence to
the prepaid-health unit, and/or add a 7th `failures.csv` row for the annuity-line revenue decline (dollars as
printed, self-report, Medium). This is the health-insurer-specific omission: an in-window adverse product-line
result inside the one Tier-1 self-report.

**F-5 (Low-Medium) — two held in-window CIGNA-naming bytes are unregistered.** `sources/periodicals/
cia-readingroom-document-cia-rdp90g00152r001102380002-3_djvu.txt` l.1431 `CIGNA` + l.1436 "The CIGNA Consumer
Marketing Department offers insurance and non-insurance products to financial institutions through their
customer base" (with a 1600 Arch Street, Philadelphia address block) and `…rdp91-00929…` l.1071 (OCR fragment).
Both were **mined by A4** (its table rows l.31-32, class `BARE_WORD_MATCH`) and both are held, but neither is a
`sources.csv` row nor a line of §T. No volume claim is falsified (M02 says one *divestiture* naming; §I says no
named *competitor*), yet §T/§B.1 present CG01-CG16 as the provenance set. Repair: two naming-only/decoy rows in
the S4416 pattern, or one §T sentence enumerating the held-but-bare-word matches. Not a FETCH REQUEST.

**F-6 (Low) — four quoted spans are not verbatim in the carrier they are cited to** (my matcher's residual
after OCR normalisation; each independently re-read from the byte):
(a) §G `HMO International … "through an exchange of stock … accounted for as a purchase"` — l.3679 prints
"accounted for **the transaction** as a purchase";
(b) §U.5 CLAIM A `"79 candidate rows; 12 mined; 65 untried."` — the probe l.399-400 prints "79 candidate rows
**in the harvest index**; 12 items mined; 65 **left untried at the --limit**"; the 96/12/81 quote is exact;
(c) `sources.csv` S4417 passage `"1018 filings enumerated; UNANSWERED slices: (none)"` — a **composite** of
`_INDEX.md` l.4 and the "(none)" under the l.45 heading, contiguous nowhere;
(d) §B.1 `"at a 23% annual compound rate, compared with 9% growth for the overall field"` — the byte prints
"at **a23%**" (OCR space loss, l.382); elsewhere the dossier discloses OCR damage, here it silently repairs it.
Related: §F "(searched this pass: `membership` **absent** from INA report)" — the token occurs once
(l.2618, "suggestions for **board** membership"); the load-bearing half (no membership *count*) survives.
Repair: re-quote (a)-(b), split (c) into two locators, flag (d) as an OCR repair, change "absent" →
"no membership count printed".

**F-7 (Low) — three derived counts do not reproduce from the bytes.**
(i) "CG01 is **one lineage of 23 files**" (`stage_1.md` l.57, l.76; inherited from probe l.117): measured **20**
non-meta documents in the S-4 + 4 amendments + exhibits (accessions 0001140361-18-024107/-029349/-031849/
-032199/-032454, 4 files each), **22** if the 2018-12-20 8-K pair (S4408) is folded in, **30** filing documents
in all of `sources/sec/`, 35 non-meta files including 5 index artefacts.
(ii) A4's own arithmetic never closes: 96 − 12 = **84**, not the printed 81 (and the earlier reading 79 − 12 =
67 ≠ 65); the volume repeats 96/12/81 in six places (§I, §J, UNTRIED-4, §U.5, `data_gaps.csv` row 5, S4421)
without noting the 3-row non-closure — its RD-134 hedge ("a capped enumeration is a sample, never a census") is
right, but the gap should be named.
(iii) Checked and **clean**: K.1's damaged 1978 equity cell "1 307" is internally inconsistent with the printed
+15% change (1,526/1,307 = +16.8%), and the dossier labelled it damaged-print rather than repairing it — correct
handling, recorded here as a check that passed.

**F-8 (Low) — coda duty (§7/§16: evidence · mechanism · alternative · confidence) is met in one of three
codas.** §L.1 is exemplary (all four, with "Alternative explanation not excluded …" and a named confidence).
§H.1 has evidence, "mechanism UNKNOWN", and an alternative, but **no confidence token**. §D.2 "Assessment" has
evidence and an implicit confidence but **names no alternative explanation and no confidence word**. Two-clause
repair; §R's KNOWABLE / NOT KNOWABLE / UNKNOWN column complies as written (method l.133).

**F-9 (Low, administrative) — one published live count is stale, 17 of 18 reproduce.** `_MANIFEST.md` l.54
publishes `_parts/NOTES_cigna_p1.md` at **1,003 words**; `wc -w` = **1,111** (bytes 7,830 match). Every other
figure in `_MANIFEST.md`, `stage_1_index.md` (including its 78-row / 3,130-word / 30,350-byte register totals,
which sum exactly) and the merge record reproduced under my own `wc`: stage_1.md 14,513 w / 94,432 B; sources
872/9,346; quantitative 353/3,511; timeline 441/4,241; data_gaps 404/3,381; conflicts 424/3,606; failures
223/2,139; validation 150/1,503; decisions 173/1,715; channels 90/908; s1_p1 16,016/114,204; index 1,141/7,053;
CORRECTIONS 1,076/7,435; probe 7,190/48,751; A4 833/5,611.

---

## Checks, with counts and the command that produced them

**1. Merge integrity — PASSES IN FULL.** `python tools/merge_census.py --company-dir
founders_playbook/01_companies/company_014_cigna --verbose` → 9 blocks, 78 requested, `conflicts 6 present /
0 missing`, `TOTAL missing keyed rows: 16`, 2 `AMBIGUOUS:validation.csv,failures.csv` groups — the merger's
before/after readings reproduced exactly. Both halves of the claim are true, and the 16 **are** key-form
blindness, not lost rows: I parsed the nine fenced blocks out of the read-only `_parts/s1_p1.md` and matched
them cell-by-cell against the live CSVs (CG→S re-key applied, annotation tolerance on) →
**sources 16/16, quantitative 15/15, timeline 14/14, decisions 3/3, validation 4/4, failures 6/6, channels 2/2,
conflicts 6/6, data_gaps 12/12: 78 part rows all with live twins, 0 unmatched, 0 live rows without a part
origin, and exactly 5 annotation-only diffs — the five cells the merger named** (`sources.csv` S4407, the
`quantitative.csv` census row, `conflicts.csv` U.2, `validation.csv` r1, `failures.csv` r1). Ids: 16 distinct
keys `S4407–S4422`, contiguous, 0 duplicates; `id_mint.py --audit` → `company_014_cigna n=16 S4407..S4422`,
`next assignable: S4529`; a cross-company scan found **no other company citing any Cigna id as a source** (the
one hit, `company_023_gm/stage_1.md` l.46, is GM's *narrative* "range S0001–S4422, next assignable: S4423").
Header equality against `company_001_amazon/<register>`: **9/9 True**; width defects **0**; empty cells **0**;
`stage != stage1` **0**; exact duplicate rows **0**; `CG` residue **0**.

**2. The validation/failures adjudication — THE CALL IS CORRECT.** All ten rows read. 4 positive: health
pre-tax +48%; buy-a-plan repetition; three SCOTUS records naming the structure; the 2018 indenture designation
(firewall-tagged, "DO NOT use as an in-window signal"). 6 adverse: 101.8 combined ratio; $84.8M 1978 losses;
reserves outgrowing earned premiums 96→111%; the 5%-of-income parent-and-other LOSS; goodwill write-downs; three
appearances **as respondent**. No incurred adverse event sits in `validation`, and no validating signal sits in
`failures` — the Tesla-20 / Microsoft-11 / Nvidia-3 inversion class is **absent**. The merger's stated basis
(block headings + counts + row semantics, 4+6=10, no row in both) is verified against
`_parts/s1_p1.md` headings at the 4-row and 6-row blocks. Observation, not a defect: the same three court
records appear once in each register (validation r3 = structural legibility, failures r6 = adversity); they are
different propositions about different columns of the same filings, each disclosing what it does **not** show,
so the pair is not a duplicate row.

**3. Numbers — 15/15 quantitative rows and 16/16 §P rows recompute from the filed print.** Verified against
`INAC2115_1979_djvu.txt`: 4,551/4,025 = +13% (print 13%); 8,987/8,036 = +11.8% (print 12%); 262/214;
17 vs 2 = +750%; EPS 6.34/5.58 and 6.13/5.39 (print 14%); dividends 2.05/1.73 (print 18%); ROE 17.1/17.0;
35,280/33,987; avg shares 38,579,370/37,888,500 — all at l.78-100 exactly as the dossier transcribed, including
the two cells it refused to read ("21", "1 307"). Segment: P&C 66% revenue / 69% pre-tax (l.366-368), Life 18/22
(l.377-378), Health 12/14 (l.391-393), Parent-and-other 4% revenue / **5% pre-tax loss** (l.414-416):
66+18+12+4 = 100 and 69+22+14−5 = 100. Underwriting: 101.8 vs 99.8 with INA's own mixed definition quoted
verbatim (l.740-753); written 2.78B vs 2.55B = +9% (l.675-676); losses 84.8 vs 20.8 (l.678-684); reserves 2.9B,
+392M/15%, 18% compound 1975-79, 111/105/96 of **earned** (l.750-762); written-to-surplus 3.0/3.5/4.5
(l.765-773); health 41.6 vs 28.1 = +48%, 45% compound (l.451-455); life 67.1 vs 56.2 = +19%, 28% compound
(l.447-449); investment income 450.4 vs 353.4 = +27% (l.458-459); P&C pre-tax 213.4 vs 209.3, after-tax 185.2
+15% (l.660-674); goodwill 82,684,000 / ~27.6M pre-1971 / +4.3M / 4.2M in 1978 (l.3711-3719); industry
~2,900 firms / ~$90B (l.653-657); DERIVED 2,780/90,000 = 3.09% → 3.1 with the mixed-basis flag intact; the
1975 P&C "loss of $2 million" (l.444) and the GNMA $1.2B/$700M (l.3666-3674) both print as cited.
CONTEMPORANEOUS vs RESTATED per row: correct — 1792 RESTATED; 1957/1969 "CONTEMPORANEOUS print of a restated
internal date"; the 1978 comparators labelled "printed as the 1978 comparator inside the 1979 report"; the 2018
S-4 product sentence RESTATED-at-2018 (§E row 8). Fiscal basis: the highlights table is "Years Ended December
31" and every row says 1979/1978-12-31 accordingly.

**4. Health-insurer-specific traps — NONE PRESENT.** Earned vs written: P06/P07 are written (byte says
"Written premiums reached $2.78 billion") and P10 is earned ("as a percentage of earned premiums") — never
swapped, and the written-to-surplus row is labelled written. A benefit ratio read as a margin: the 101.8
combined ratio is filed in `failures.csv` with ">100 = underwriting loss on INA's own mixed definition" and the
definition is quoted in full — no margin reading; the after-policyholders'-dividends series (102.8/100.4/102.1
at l.2703) is correctly not used to contradict it. Membership at period-end vs average: employees are
year-end headcount, "Average shares outstanding" is labelled average; no membership figure exists to mislabel
(`enroll`/`policy count` = 0 hits corpus-wide). A restated segment series presented as contemporaneous: none —
the 1975/1978 points are all marked as comparators inside the 1979 print, and `quantitative.csv` row 8 says so.

**5. Dates — every table-row date has a printing carrier; no invented date survived; one real date was missed.**
Carriers verified line-by-line: **2018-12-20** name change/event date — 8-K l.32 "Date of Report (Date of
earliest event reported): December 20, 2018", l.163, l.170; the cover's "(Exact name…)" at l.36 and the
two-line former-name block at l.77-78 as cited; **2018-05-16** — `submissions.csv` min filingDate (1,018 rows,
header line 1019, `wc -l` ✓) with `CORRESP`+`S-4` on that date, max 2026-09-08 ✓ as S4417 states; **2018-09-21**
— `0000950159-18-000404_halfmoon8k.htm` l.646 "Date: September 21, 2018" (and the Designated Subsidiary
definition at ex4-1 **l.2584** ✓ and ex4-2 **l.72** ✓ — both locators exact, including the "successor of"
clause); **1981** — `s4.htm` l.4995 + l.23191 exactly as cited, subject = Cigna Corporation, and the volume
keeps it off the registrant (§U.1, §B.2, §Q); **1792** — corpus census re-run: exactly **2** occurrences,
`INAC2115_1979_djvu.txt` l.5 + l.371, 0 elsewhere across all 43 held text/HTML bytes, and attributed to **INA /
its principal subsidiary**, never to the registrant (Header, §A.2 "a different legal person than the registrant
… attributed by its own grammar to the subsidiary", §U.2, `timeline.csv` row 2 RESTATED, Medium ceiling);
**1872** — **0** occurrences corpus-wide, kept UNTRIED not null (`conflicts.csv` U.3, `data_gaps.csv` row 4,
UNTRIED-7, FR-7), the lone `1850` blocked as the ERIC New-Haven decoy (S4419); **1982** — present only as
UNATTESTED HYPOTHESIS (`timeline.csv` row 7 class UNKNOWN/Low, §Q bolded, §U.3), never as fact; DeBlase —
"October Term, 1994" l.13/l.254/l.2394 and the OCR stamp l.5 "9417 46 APR 19 1995" ✓; Creative Bath caption
l.15 ✓; Pierre chain and the ERISA "claim administrators" questions at l.6091 (cited range l.6081-6096 ✓);
A4 l.5, `_INDEX.md`, `_UNANSWERED.csv` ("18 in-window filings were never listed because --max-docs 30 was
reached" — the UNANSWERED is earned). The one defect is B-1 (a missing true date, not an invented one).

**6. Citations and quotes — 0 carrier-existence defects; 0 sustained right-document-wrong-place; 4
in-range-but-does-not-support items (F-2/F-3/F-4 + the §F "membership absent" clause).**
Tested: **74** distinct quoted spans from `stage_1.md` plus all nine registers, against 55 held bytes + 2
research files. **Matcher's own error rate, stated before handing anything to a repairer:** my corpus
normalises tags/entities/quotes and joins OCR hyphen line-breaks; of the 12 residual misses, **8 (67%) are my
false positives** — spans the volume quotes from its *own* prose or claim-record metadata (`URL: local —
Archived…`, "no held validation is not no validation", "clause names both ancestor carriers with a", "Low as a
decision-as-decision / Medium as print", etc.), not from a carrier — so **4 of 74 (5%) are real deviations**,
and those four are the ones itemised as F-6 (a)-(d). Independently: 2 further spans I *expected* to fail are
**verified good** — the S4414 quote is a disclosed re-join over an OCR stray ("…to local | 2 management.",
l.1174-1175, labelled "(re-joined…)" in M02) and the Pierre chain quote is a disclosed re-join across
l.6113-6116. `sources.csv` passage cells: **14/16 verbatim in a held byte**, 1 declared `NO_VERBATIM` (S4420),
1 composite (S4417, F-6c). **No fact is cited to an unheld document**: S4420 is the only unheld pointer, it
self-declares `BYTES UNHELD` / `UNKNOWN` / tier 4 and is used only inside FR-4 — correct. **No FETCH REQUEST is
owed by this audit**: every repair above is a re-read of bytes already on disk.

**7. The gate's one finding is a confirmed false advisory.** `python tools/gates.py --company-dir
founders_playbook/01_companies/company_014_cigna --tier core --out
03_quality_control/cigna_s1_gates_audit1.md` → **Findings 1 | Passes 19** (`quotes | verbatim | 1 of 5 quoted
spans not found in local sources`; the evidence line names the A4 span). `grep` of
`research/A4_harvest_mine.md` **l.5** prints it verbatim: "96 candidate rows in the harvest index; 12 items
mined; 81 left untried at the --limit." The gate's own diagnostic proves the cause — `quotes corpus: 9,956,365
chars of squashed local source text indexed` (i.e. `sources/**` only), and it checked 5 of 93 candidates
(1 unmatched = 20% of the checked subset, 20 unattributed spans reported advisory). **Verified, not reported as
paraphrase**; the data was correctly left alone. **Tier flag as briefed:** I passed `--tier core` explicitly
(the tier is a table row in this dossier, so `--tier auto` can misread it — the probe saw T3, the merge saw T2)
and the budget check applied target 22,000 / hard cap 60,000 to 14,513 words = 66%, consistent with both prior
runs. Side effect I could not avoid and did not repair: the briefed `--out` path is relative to the repo root,
so the report landed at `E:\founder's playbook\03_quality_control\cigna_s1_gates_audit1.md`, **not** beside its
siblings in `founders_playbook/03_quality_control/`.

**8. Independence — 3 lineages tested, all honoured.** md5: the three court bytes are **distinct**
(`c7c9…`, `b271…`, `0a99…`) = three cases, three filers ✓, and DeBlase is **byte-identical** across
`periodicals/` and `corporate_print/` (`0a992051…` on both) = **one document, counted once**, no fold-and-mint
✓. `sources.csv` collapses 5 S-4 accessions / 20 documents into **one** row (S4407) ✓; the 1981 recital's 10
corpus occurrences are 5 files of that one lineage ✓; the indenture's two exhibits are one accession ✓. No
label used as a witness: `TIER1_CANDIDATE_TEXT` rows are registered as naming-only (S4416, "promotion opened
and dismissed", RD-124) and pointer-only (S4420); the `in-window` index cell in A4 is used only as census.
Corroboration claims audited for one-lineage inflation: **none found** — A01 "1 lineage", B03 "two copies, one
lineage — hard rule 3", E01 "1 judicial origin, independent of every corporate lineage", H01 "0 independent",
M02 "Corroboration: 0 (no second witness in corpus)", N01 "1 lineage, two passages (same doc)". The §T ledger
sentence "CG01+amendments+**CG03** = one lineage" is looser than `sources.csv` S4409's own note ("two exhibits,
one accession") — accession 0000950159-18-000404 is a **separate filing** carrying the 2018-09-21 indenture —
but the looseness runs *against* counting, so it is not a corroboration defect.

**9. Hindsight and boundary — firewall holds; frames kept as states; boundary needs B-1 to be re-labelled, not
re-based.** Evidence–mechanism–alternative–confidence: §L.1 complete, §H.1 and §D.2 short by one element each
(F-8). The Header firewall paragraph, §N.1, `validation.csv` r4 ("DO NOT use as an in-window signal") and
§M r8 ("silence here must not be read as the ancestors' silence") are all present and are **not** decorative:
no 1979-1995 row is narrated as a step toward Express Scripts, and the HMO International note's own "would not
have been material" is kept against retrospective weight (§N.1). Earliest defensible origin: on the lineage
frame 1979 is right (the earliest held self-report; 1792 is restated and capped Medium; 1982 is unattested); on
the registrant frame the answer is now **2018-03-06** (B-1), which is *further* from the window, so the
strict-registrant reading strengthens rather than weakens. Two tier frames carried as attributed states in 5
volume sites + `conflicts.csv` U.4 + `_MANIFEST.md` + `stage_1_index.md`, **never averaged**, with the machine
tie-break registered as U.4 rather than deleted ✓. Five-family nulls earned and kept distinct (TRIED–ANSWERED /
TRIED–UNANSWERED / UNTRIED): (a) perimeter answered + predecessor UNTRIED + 18 UNANSWERED backed by
`sources/sec/_UNANSWERED.csv`; (b) 0 calls; (c) answered/UNANSWERED (7/7 CA shapes 403) + 81-of-96 backlog
UNTRIED; (d) answered by document class off-shelf (U.6) + facet-ed task UNANSWERED; (e) 0 calls — no unattempted
family reported empty. `UNKNOWN` is used where the corpus is silent and, in every instance I checked except
B-1, genuinely silent.

**A-9 — one process note for the orchestrator.** I was told to read `MASTER_RESEARCH_LOG.md` entries
**RD-138–RD-141**; the log's last numbered entry is **RD-135** and those ids appear only in
`00_universe/_AUTHOR_WAVE_PLAN.md` (RD-138 `grab` 3-tuple fix, RD-139 `cdx_intake.py` + `version_aside()`),
`00_universe/_DISPATCH_QUEUE.md` (RD-136 Elevance overwrite fix, RD-138) and
`03_quality_control/registrant_resolve_repairs.md` (RD-137). I audited against the tool behaviour I could
measure instead, and record the gap so no one later claims the audit ignored entries that do not exist.

---

## What I did not examine

The 26 SEC documents beyond the 4 representatives (only the accession/lineage counts and the Annex-E/`ex3-3`
formation date were extracted, not read); page interiors of the three court records beyond captions, structure
and Rule 29.1 ranges; the INA report's audited statement pages beyond the passages quoted; the four CIA bytes
beyond the `Cigna`/`Connecticut General` hit lines; `sources/sec/_MANIFEST.csv` / `_PLAN.csv` row by row; and I
ran no retrieval at all (0 web calls), so every UNTRIED family remains UNTRIED after this audit exactly as the
dossier left it.

## Counts (re-measured after my last write)

This file: **4,048 words / 28,432 bytes** measured before this sentence's own edit, **4,081 / 28,625** measured
immediately after it — a file cannot publish its own final size (the rule `_MANIFEST.md` l.42 states), so any
later touch must re-measure with `wc -w`. Registers re-measured after my run, unchanged (I wrote no corpus file but this one):
78 rows total, `sources.csv` 16×18 … `channels.csv` 2×11; `stage_1.md` **14,513 words / 94,432 bytes**;
gate output: Findings 1 | Passes 19. Blockers: 1. Findings: 8. FETCH REQUESTs: **0** — B-1 is repaired from
bytes already held.
