# Repair Sheet — Amazon.com (company_001) · Stage 2 · AUDIT 2 (Citation) repairs

Repair agent: independent of the AUDIT-2 author and of the Stage-2 producer. Run 2026-09-25.
Target sheet: `03_quality_control/amazon_s2_audit2_citation.md` (verdict FAIL).
Web requests made in this pass: **zero**. Every correction below is keyed to bytes on disk.

Scope of edits: `stage_2_claim_records.md`, `stage_2_claim_records_part_2.md`, `stage_2_part_1.md`,
`stage_2_part_2.md`, `stage_2_part_3.md`, `stage_2_index.md`, the nine `*.csv` registers,
`research/_EVIDENCE_CACHE.md`, and this sheet. Stage 1, `context_appendices.md`, `CORRECTIONS.md`,
`adversarial_review.md`, `_parts/` untouched.

## How this sheet was written (verification-first, not re-doing)

The first repair agent worked the nine defects and died at its turn limit with **this log still blank**: the
version of this file held until 2026-09-25 20:xx read `OPEN` on all nine rows while the corpus files it edited
carried mtimes of 19:51–19:56. Rather than re-run the repairs (which is how duplicates and overcorrections get
made), each row below was **tested against the files as they stand**, and only what was genuinely absent was
executed. The finding is that **eight of the nine rows were already complete on disk**, and the log was the only
missing artifact. Two narrative loci and one register-wide flag had not landed; those are the four edits credited
to *this* pass below. Everything marked *(previous pass)* is left exactly as it was found, un-repaired, because
it was already right.

Harness used (outside the repo, in `E:/tmp/citaudit2/`, so nothing was added to the corpus): `classify.py` (the
AUDIT-2 verbatim classifier, re-run here), `mark.py` / `restore.py` / `apply_rest.py` / `rest_list.py` (the
previous agent's), and `verify_markers.py` written this pass. `classification.tsv` was re-run and both states are
kept: `classification_pre_repair_backup.tsv` and `classification_after.tsv`.

## Work order and outcomes

| Row | Defect (audit ID) | Severity | Task | Status | **Verdict after verification** | **Measured at** |
|---|---|---|---|---|---|---|
| R1 | DEFECT-1 / B110 — invented Lipsky employment range "from 1993 to 1995" | HIGH | correct to filed dates, cite accession+line, re-check surrounding claim | was `OPEN` | **DONE — 5 loci by the previous pass, 1 by this pass** (`stage_2_part_3.md` l.55) | `stage_2_claim_records.md:155`; `:778` (Q29); `stage_2_claim_records_part_2.md:118` (U.79); `stage_2_part_1.md:446`; `stage_2_part_2.md:97`; `stage_2_part_3.md:55` |
| R2 | DEFECT-2 / B100 — inverted repurchase-right holder ("by the investor") | HIGH | correct to filed text; mark affected §A.1 wording | was `OPEN` | **DONE — 2 loci by the previous pass, 1 by this pass** (`stage_2_part_1.md` §A.1 table row l.111) | `stage_2_claim_records.md:135`; `stage_2_part_1.md:71` (prose), `:111` (table cell) |
| R3 | DEFECT-3 — boundary pricing leg has no carrier; press release unregistered | HIGH | search `sources/` for the release; register it if on disk, else re-label the leg | was `OPEN` | **DONE (previous pass), both halves** — split label + register row S2012 as a documented null; no value substituted for the retraction | `stage_2_part_1.md:12-13` (header), `:22` (three-date cluster), `:79`; `sources.csv:115` (S2012); `stage_2_claim_records.md:521` (L16) |
| R4 | DEFECT-5 / D32 — spliced "New Castle, Delaware" quotation | MEDIUM | fix quotation + citation to `l.1646-1647` + `l.1075` | was `OPEN` | **DONE (previous pass)**, and it went one better than the sheet: it added a third carrier the audit had not found | `stage_2_claim_records.md:241`; `stage_2_part_1.md:245`, `:412` |
| R5 | DEFECT-4 — ~96 of 479 records present paraphrase as quotation | SYSTEMIC | build classifier outside repo, run over all 479, emit machine list; add preambles; mark non-verbatim records | was `OPEN` | **DONE (previous pass) and independently re-verified this pass**: 479 records classified, five-class `Passage:` convention declared, 186 in-cell markers applied, **0 dishonest markers** | `stage_2_claim_records.md:19-40` (preamble); marker census §R5 below |
| R6 | DEFECT-6 — two local copies of one accession, constant 17-line offset | MEDIUM | declare spine keying + offset in `research/_EVIDENCE_CACHE.md`; delete nothing | was `OPEN` | **DONE (previous pass)**; this pass added the one-line pointer the audit also asked for in `stage_2_index.md` (a section header, not a repair) | `research/_EVIDENCE_CACHE.md:313-341`; `stage_2_index.md` "Line-reference keying" |
| R7 | DEFECT-7 / U.80 — non-SEC evidence has no bytes on disk | HIGH (structural) | search whole repo for periodicals; else downgrade U.80's independence claim; report the 75-doc intake | was `OPEN` | **PARTLY DONE by the previous pass → COMPLETED here.** The U.80 downgrade and the `(NO LOCAL COPY)` tags landed; the `local_copy:` flag the downgrade *points to* existed on only 1 of 12 Stage-2 register rows, so four in-text cross-references dangled. All 12 rows now carry it | `stage_2_claim_records_part_2.md:120`; `sources.csv` (12 Stage-2 rows); tags at `stage_2_part_1.md:67,75,22`; `stage_2_part_2.md:621` |
| R8 | DEFECT-8 — exhibit quotations conflate 10.30 / 10.31; "& other products" dropped | LOW-MED | re-quote per exhibit, restore tail (if budget allows) | was `OPEN` | **DONE (previous pass)**, with the withdrawn wording left visible in-cell as §14 rule 4 requires | `stage_2_claim_records.md:756` (Q18), `:816` (Q48), `:159` (B112), `:163` (B114); `stage_2_claim_records_part_2.md:138` (U.89) |
| R9 | DEFECT-9 — header self-pointer l.18 → l.22; id-join grammar | LOW | re-point; note in this sheet | was `OPEN` | **DONE (previous pass)** for the self-pointer; register-join half now keyed by `source_id` in 13 places; the `S2B-X-*` grammar and the `Tier:`/`[T#]` two-grammar issue are **reported, not merged** — see §Left alone | `stage_2_part_1.md:12` |

## Row detail — what was measured, with the command

**R1 — DONE.** `grep -rn "1993 to 1995" .` over the whole company folder now returns exactly two hits, both
legitimate: `stage_2_claim_records.md:155` where the string sits inside `**RETRACTION (Audit-2 DEFECT-1, repair
2026-09-25):** … **Withdrawn.**`, and `research/H_legal_organization.md:98` where Stage 1 uses "1993 to
1995-12-31" as a *window bound* in an unrelated trademark claim (untouched — Stage-1 file, and not a Lipsky
claim). The filed dates **March 1994 to July 1996** are now printed with both accessions and both wordings in
`B110`, `Q29`, `U.79`, `part_1 l.446`, `part_2 l.97`. Verified at the cited lines: `sed -n '2509,2512p'` on
`sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` and `sed -n '2727,2731p'` on
`sources/S-1A-No5_acc-0000891020-97-000839_filed-1997-05-14.txt` both file the March-1994–July-1996 range, and
"superstore division" is indeed in the original only.
*My edit:* `stage_2_part_3.md:55` was the one locus in the audit's six that had not been re-keyed — it still
cited No. 5 alone for the original's phrase, and still said "crossed over **in the month the Series A money
landed**", which the previous pass had already corrected to "the month **after** the Series A closes" in `Q29`
(No. 5 l.4687 files the issue at 1996-06-21; the hire is July). Re-keyed to `S-1 (orig.) l.2509-2512` +
`No. 5 l.2727-2731` with the accession differential named, the month corrected, and the superseded reading
stated in the cell.

**R2 — DONE.** `grep -rn "by the investor" *.md` returns one file, `stage_2_claim_records.md`, and one place in
it: inside `B100`'s `**RETRACTION (AUDIT-2 DEFECT-2 …)**`. The live `Passage:` is now the filed sentence lifted
from `S2E-47`, quoting `424B1 l.2969-2973` verbatim ("Mr. Bezos **granted the Company** a right to repurchase …
**if his employment terminates** … lapses **ratably** over the 36-month period ending June 21, 1999") plus the
No. 5 note version with the 510,000 still subject at 1996-12-31. Confirmed present at the cited lines by
`sed -n '2969,2973p'` on `sources/424B1_final-prospectus_acc-0000891020-97-000868_filed-1997-05-15.txt`.
`part_1` §A.1 was **adjusted, not deleted**: the prose cell (l.71) keeps the old wording visible — "*this cell
previously read 'conditional control (612,000 of Bezos's own shares repurchaseable at $0.0010 to 1999-06-21)',
omitting the holder*".
*My edit:* the **table** row of the same §A cell (`stage_2_part_1.md:111`) had not been reached — it still read
"a repurchase right over 612,000 of his shares at $0.001 **lapsed only to** 1999-06-21", naming no holder and
implying a cliff. Now names the Company as holder, the termination trigger, and the ratable lapse, with the old
wording quoted in the repair note; the citation gained `424B1 l.2969-2973 = No. 5 l.4176-4182`.

**R3 — DONE, and done the right way.** The press release is **not on disk** — re-verified by
`grep -ril "announces-initial-public-offering"` across `sources/` (94 `.txt`) and the whole folder: the only
hits are the two Stage-2 dossiers that cite it. So the leg was re-labelled rather than back-filled: the header
(l.22) now splits the boundary into "(a) effectiveness leg: EXACT — `10-K405 l.1126`" and "(b) pricing leg: **NOT
A FILED FACT** … no document on disk states that the offering was priced on 14 May", prints
`(NO LOCAL COPY — … see sources.csv S2012)`, and points at the split label. `sources.csv:115` adds **S2012** with
`tier 2`, `evidence_class: ASSERTION (company statement of its own act; not a filed fact)`, `local_copy: NO`, and
an explicit "Intake would close it; retrieval was out of budget in this pass (method §11: research debt)". This
pass found a genuine extra carrier while verifying it and it is registered in S2012's text: the Q2- and Q3-1997
10-Qs (`l.889-892`, `l.810-813`) date the **completion** to 15 May at $18.00 — post-boundary, so it corroborates
the price, never the pricing day. **No value was substituted for the retraction.**

**R4 — DONE.** `D32` now prints the two 10-K405 passages **separately** — `l.1646-1647` for the event ("in
Delaware", no place-name) and Item 2 Properties `l.1075-1076` for "New Castle, Delaware" — the spliced sentence
is quoted only inside `**REPAIR (Audit-2 DEFECT-5 …)** … **Withdrawn — it is a splice and exists in no document
on disk**`, and the repair added a carrier the audit had not located: the executed lease at
`10-Q Q3-1997 … l.1225` ("Centerpointe Business Complex, 700 Frenchtown Road, New Castle, Delaware"). Verified:
`sed -n '1075,1076p'` and `sed -n '1225p'` prove both strings verbatim. `grep -rn "New Castle" sources/*.txt`
returns 30 lines across 11 files, of which exactly two carry the **distribution-centre** place-name the D32 cell
needs — `10-K_FY1997 … l.1075` and `10-Q_Q3-1997 … l.1225` (the same lease repeats it at l.1278, 1314, 1322, 2042)
— so the audit's "no Stage-2 citation points to l.1075" is now false in the good sense. The other hits are the
**County** of New Castle in the Wilmington registered-office address (`S-1 original l.5180`,
`S-1A-No1 l.5299`) and later years' 10-Ks: a county, not the DC, and not to be spliced in either direction.
`part_1 l.245` and `l.412` carry the joint citation and the same note.

**R5 — DONE and re-verified honestly.** See the census and the honesty test below.

**R6 — DONE.** `research/_EVIDENCE_CACHE.md:313-341` declares the keying rule ("No Stage-2 reference resolves
against a bare-named twin"), the table of the two duplicates with their 17-line deltas, the four probe rows, and
the directional conversion `twin line = keyed line − 17`; it also notices a **second** duplicate family the audit
missed (`S-1A_No1/2/4/6_…` underscore vs the hyphenated convention copies, byte-identical). Nothing was deleted.
*My edit:* `stage_2_index.md` gained the one-line pointer the audit recommended ("state once in
`stage_2_index.md`/`_MANIFEST.md`"), pointing at the cache rather than restating it (index is not mine to widen
beyond that; `_MANIFEST.md` is owned by the orchestrator and was not touched).

**R7 — PARTLY DONE by the previous pass; the dangling half is completed here.** Judged against the record **as
it is now**, not as the audit saw it: the corpus has grown to 94 `.txt` (75 post-IPO filings plus Stage-3
intake), and `tools/HARVEST_README.md` documents working Google Books and HathiTrust routes — so the audit's
"the harvest machinery was never run to disk for company_001" is now only partly true: it was run for Walmart,
Apple and UnitedHealth (`00_universe/harvest/periodicals_intake/{walmart,apple,unitedhealth}_*`), **and Amazon
was still not served**: `ls` shows no `company_001_amazon/sources/periodicals/`, and a repo-wide search
(`find . -iname "*barnes*"` and `ls sources/ | grep -i barn`) returns **no Barnes & Noble document of any kind**.
The judgment therefore stands unchanged, and U.80 says so in the right words: its Corroboration is now printed as
"**(downgraded 2026-09-25 by the AUDIT-2 DEFECT-7 repair … only ONE of them has a byte on disk … Read the pairing
as the stage's only *candidate* independent-issuer comparison, unverifiable at the citation**, not as a checked
one)**", and it retracts the adjacent inference — "that downgrade is also the reason §P164 cannot be called the
highest-value verified row in §P … it is the highest-value **unverifiable** one". The `(NO LOCAL COPY)` in-cell tag
is printed at 14 places across the five files.
*What was NOT done, and is now:* the audit's recommendation was a `local_copy: yes|no` flag on every register row,
and four Stage-2 text locations cite that flag as a register property — `stage_2_claim_records_part_2.md:120`
("See `sources.csv` S2009 (`local_copy: NO`)"), `stage_2_part_1.md:67`, `:75`, `stage_2_part_2.md:621` — but the
token existed on **1 row of 12** (S2012, the row the same pass had just written). Those pointers dangled. Every
Stage-2 row now declares it, **computed from bytes on disk in this pass** rather than from the row's own prose
(`os.path.exists` against the file named in `archived_url`, following S2011's back-references to S0801/S0803/S0805):
**6 YES** (S2001–S2004, S2010, S2011) and **6 NO** (S2006, S2007, S2008, S2009, S2012 = five witnesses with no
byte anywhere; S2005 = documented null, no such document exists). This is a register *status* addition: no claim,
figure or tier moved, and DEFECT-7 itself remains **research debt, not a repair** — intake was not attempted at
zero web budget.

**R8 — DONE.** `Q18`/`B112` now quote **Ex-10.31's** own "Allowed Use" sentence including the tail
"**& other products**", and state inside the cell that 10.30's "PERMITTED USE" heading belongs to a different
lease with different words ("general office, storage, manufacturing and distribution and for no other purpose",
`l.22988-22991`); the fused wording is quoted only as "the withdrawn wording of this cell read". `Q48`/`U.89`/
`B114` likewise print the filed `l.26077-26078` "Lessor and Lessee agree that each Lease is a 'Finance Lease' as
defined by Section 103 of Article 2A…" and keep "each schedule delivered under this Master Lease" visible as the
superseded reading. Both filed strings re-verified at the cited lines (`sed -n '23387,23388p'`,
`sed -n '26077,26078p'` on the S-1 original). `part_1 l.404` carries the restored "& other products" in the
narrative cell, which is where §Rejected (iii) needs it.

**R9 — DONE for the self-pointer.** `stage_2_part_1.md:12` now reads "the three-date cluster is disclosed at
**part_1 l.22** *(self-pointer corrected by the AUDIT-2 DEFECT-9 repair, 2026-09-25: it read l.18, which is the
volume H1 carrying only one of the three dates)*", and l.22 does carry the cluster. Register join: S2012/S2009/
S2007/S2005 are now keyed by `source_id` in the Stage-2 text in 13 places (was 1, S2001).

## §R5 — the systemic row: classifier output, marker census, and the honesty test

**Classification (re-run this pass over all 479 records, harness `E:/tmp/citaudit2/classify.py`, corpus 90 local
documents, output `classification_after.tsv`):**

| Verdict | n | Meaning after the repair |
|---|---|---|
| `VERBATIM` | 186 | unmarked quotation, present in the cited document — rule 1 holds |
| `PARAPHRASE` | 137 | non-filed wording; 128 now carry `[paraphrase, not filed wording]`, 9 are table-row composites carrying the more accurate `[table composite, figures filed]` |
| `PARTIAL` | 27 | 16 carry `[partly filed wording]`, 8 are the `[restored …]` cells whose *withdrawn* wording sits inside the label (the harness reads it as a quote; it is not a live quote), 3 are the §Q/U.112–U.113 rows in the same shape |
| `NO-CARRIER` | 26 | 23 carry `[no local carrier]` / `(NO LOCAL COPY)`, 3 are table composites whose witness is off-disk |
| `SHORT-META` | 28 | quoted **value or label**, outside rule 1 by the preamble's own exception |
| `NO-QUOTE` | 75 | `NO_VERBATIM_PASSAGE_RECORDED` or no Passage field |

**Marker census on disk** (`grep -o "\[paraphrase, not filed wording\]"` → 110 + 20 = **130**; the tasking's
"134 occurrences of 'paraphrase'" includes the 4 preamble definitions): `[partly filed wording]` **17**,
`[no local carrier]` **25**, `[table composite, figures filed]` **13**, `[restored …]` **10** — **186 in-cell
markers**, plus the five-class declaration at `stage_2_claim_records.md:19-40`, which also **strikes `Passage`
out of the front-matter guarantee** (`~~Passage~~`, l.14) exactly as DEFECT-4 required, and states that the old
claim "now holds only of unmarked cells".

**Honesty test — is the marker decorative?** Two directions were tested, machine-wide, not sampled.
Command: `python verify_markers.py` (bracket-aware `Passage:` parser; each quote split at its own ellipses;
every ≥4-word run normalised and searched against all 94 local documents, and separately against **the cited
lines only** for the 12-record spot check).

1. **Marked-paraphrase-that-is-actually-verbatim (the over-flagging failure):** **0 of 112** testable marked
   strings. All 112 have **no** ≥4-word run anywhere in the corpus, so every `[paraphrase, not filed wording]`
   is a true statement. (The remaining 18 marked strings are ≤4-word value labels, outside the test.)
2. **Unmarked-quote-that-is-not-filed (the under-flagging failure):** 0 live Passage cells. The 177 raw hits from
   the first pass were 163 harness artifacts — quotes sitting in Claim prose, `(NO LOCAL COPY)` notes, register
   titles and retraction brackets rather than in `Passage:`. After bracket-masking, every remaining unmarked
   Passage string classifies `VERBATIM` or `SHORT-META`.
3. **Twelve-record cited-line spot check** (ids `E39, B114, D19, G36, R16, K21, U.92, Q18, U.80, A01, P61, B112`):
   the three `[paraphrase]` cells (E39, B114, U.80) are absent at the cited line **and** absent corpus-wide →
   honest; the eight `[restored …]` cells were checked **at their own label's line range** and 8/8 are verbatim
   there (`U.92` at No. 5 l.2598-2600, `G36`/`R16` at l.4038-4039, `K21`/`R18` at l.1797-1799, `Q48`/`U.89` at
   orig. l.26077-26078). **One failed and was corrected:** `D19`'s label cited `S-1 original l.2147-2148` but the
   sentence runs to "**31, 1996.**" on **l.2149**, so the quote was not inside the cited range. Re-pointed to
   `l.2147-2149` with the reason printed in the cell — this pass's third edit.
   Of the 130 `[paraphrase]` tags, 112 sit on strings long enough to test (≥4 words); the other 18 are short
   value/label quotes the preamble already places outside rule 1, and were not adjudicated either way — the
   honest count of *tested* markers is 112, not 130.

## Invariants, re-measured after the four edits of this pass

| Invariant | Result | Command |
|---|---|---|
| §U blocks U.44–U.113 ↔ `conflicts.csv` Stage-2 rows | **70 ↔ 70 ↔ 70, 1:1**, symmetric difference empty across part_3 blocks / appendix records / register rows | python set-compare of `^\*\*U\.(\d+)` in `stage_2_part_3.md`, `^U\.\d+ Claim:` in part_2, `stage=="2"` rows of `conflicts.csv` |
| Nine registers parse at uniform field count | **9/9 uniform** — channels 24×11, conflicts 114×15, data_gaps 46×8, decisions 26×15, failures 47×11, quantitative 194×12, **sources 115×18** (was 113; +S2012 by the previous pass, edited to 18 fields by this pass with `csv` re-parse proving it), timeline 117×11, validation 41×11 | `csv.reader` + `collections.Counter(len(row))` |
| `derived_arithmetic` on every DERIVED row | **61 DERIVED rows, 0 empty** | `quantitative.csv` col 9 = DERIVED → col 11 non-empty |
| Claim records | **479** (409 + 70), 0 duplicate ids | `grep -o "^[A-Z][0-9]\{1,3\}[a-z]\? Claim:"` both files, `uniq -d` → empty |
| False cash bridge `52 − 232 − 52 + 1,228 = 944` | **0 live copies.** 3 occurrences repo-wide: `quantitative.csv:66` and `stage_1.md:1012` inside explicit retractions, `_parts/s1_p4.md:112` in the frozen staging fragment already annotated by audit-6 IR-01. The arithmetically **true** `= 996` form survives at `stage_1.md:890`/`validation.csv:17` and is correctly labelled as carrying the opening balance on its left-hand side | regex `52\s*[−-]\s*232\s*[−-]\s*52\s*[+]\s*1,?228\s*[=≈]\s*\+?\s*\(?\s*(944|996)` over every `*.md`/`*.csv` outside `sources/` |

## What this pass changed, in one list

1. `stage_2_part_3.md:55` — §Q Lipsky row: re-keyed to both accessions, month-after correction, superseded reading kept visible *(R1)*.
2. `stage_2_part_1.md:111` — §A founder-state table cell: holder = **the Company**, termination trigger, **ratable** lapse, old wording quoted in the note, two new line citations *(R2)*.
3. `sources.csv` — `local_copy: YES|NO` added to all 11 Stage-2 rows that lacked it (S2012 already had it), computed from files on disk; field count held at 18 *(R7)*.
4. `stage_2_claim_records.md:215` — `D19`'s `[restored from … l.2147-2148]` re-pointed to `l.2147-2149`, the line where the quoted sentence ends *(R5 honesty test)*.
5. `stage_2_index.md` — added the DEFECT-6 keying pointer + the DEFECT-7 local_copy note, corrected the stale `sources.csv` register row (11→12 rows, 113→115), and added a measured post-Audit-2 word column (85,198 narrative tokens).
6. This sheet, rewritten as the record it should have been.

**Nothing was deleted anywhere.** Every withdrawn string, every superseded wording and every retraction note left
by the previous pass is still on the page, and this pass added to them rather than replacing them.

## What I now believe the audit got wrong, or would have found different had it re-run

- **Its own DEFECT-4 denominator was too high, and its class-D count mixed two different failures.** The audit
  reported "96 class D + 18 class C"; the re-run over the same 479 records returns **137 PARAPHRASE + 27 PARTIAL
  + 26 NO-CARRIER = 190 non-verbatim-or-untestable**, and the audit's 40 "class B elided composites" are counted
  here as VERBATIM. The repair did not chase the 96; it classified all 479 and marked 186 cells, so the
  repair is *broader* than the defect as scoped. That is not overcorrection — 46 of the extra marks are
  `[partly filed wording]`/`[table composite]` labels on cells the audit itself conceded were "filed but not
  contiguous" — but the two sheets do not count the same thing and a reader should not add them.
- **`l.1075` is not the only local carrier of "New Castle".** DEFECT-5 asserted "no Stage-2 citation points to
  it" and that it is the only carrier; the executed lease at `10-Q Q3-1997 l.1225` ("700 Frenchtown Road,
  New Castle, Delaware") is a second, earlier and better one — same event, in-window filing, counterparty paper.
  The repair found it; the audit did not.
- **The Q2/Q3-1997 10-Qs do carry $18.00 with a date** (`l.889-892`, `l.810-813`). DEFECT-3's strongest sentence,
  "no document in this corpus states that the offering was priced at $18.00 on 1997-05-14", survives — they date
  the **completion** to 15 May, which is not the pricing day and is post-boundary — but the audit's §15 machine
  test ("`$18.00` occurs 0 times in each of the S-1 original and Amendments 1–6, 8 times in the 424B1") omits
  the 10-Qs, and the corrected claim is narrower: the price is **filed** from 15 May onward, only the
  **14-May pricing act** is uncarried.
- **U.80's independence is not merely unverifiable, it is unbuildable as printed** — but the audit's framing
  ("the stage's one true two-issuer corroboration") is right to have flagged it, and the repair's wording
  ("the stage's only *candidate* independent-issuer comparison") is the accurate form. Now that the B&N 10-K
  has a URL in the register (`sources.csv` S2009 `url`, accession `0000889812-97-001072`) and the repo has
  working EDGAR routes, DEFECT-7 is closable by intake in Stage 3's budget rather than by downgrade; the
  downgrade should be revisited then, not silently kept.
- **The audit's DEFECT-9 item 1 (the `S2B-X-*` grammar) is a dossier-side keying difference, not a citation
  defect**, and normalising it would mean editing `research/ST2_B_finance.md`, which is out of both repair
  scopes. Reported here and left alone (§14 rule 4). Same for `Tier:` field vs `[T#]` token: they are two
  grammars by design, one for the spine and one for the narrative; the join now exists through `source_id` and
  the record ids, so the harm the audit predicted is gone without a re-grammar.
- **A defect the audit did not test:** it verified that `Passage:` line anchors land, but never verified that
  the *repair labels* land. `D19`'s `[restored from … l.2147-2148]` was off by one line and would have made the
  next auditor's check fail on a cell that had just been correctly fixed. Any `[restored]`/`[partly]` label with
  a line range should be re-tested at the range, which is how this sheet's honesty test found it.
