# Amazon Stage 2 — dangling §U reference repair (RD-081)

**Pass date:** 2026-09-26 · **Owner:** Stage-2 dangling-ref repair pass
**Scope:** the six Stage-2 files carrying live citations to `U.114` / `U.115`. No register opened, no CSV touched, nothing renumbered, no text deleted (§14 rule 4: annotations and re-points only).

---

## 0. Measurement (run before any edit, as required)

```bash
cd "E:/founder's playbook/founders_playbook/01_companies/company_001_amazon" && \
for f in stage_2_part_1.md stage_2_part_2.md stage_2_part_3.md stage_2_index.md \
         stage_2_claim_records.md stage_2_claim_records_part_2.md; do
  echo "$f : 114=$(grep -o 'U\.114' $f | wc -l) 115=$(grep -o 'U\.115' $f | wc -l)"; done
grep -n "^\*\*U\.[0-9]\+[a-z]\? —" stage_2_part_3.md | wc -l          # §U blocks defined
python -c "import csv,collections; \
  r=list(csv.DictReader(open('conflicts.csv',encoding='utf-8-sig'))); \
  print(collections.Counter(x['stage'] for x in r))"                    # register rows by stage
```

**Result (verified from disk, this pass):**

| Item | Measured | Task premise | Verdict |
|---|---|---|---|
| §U blocks defined in `stage_2_part_3.md` | **70**, `U.44 → U.113`, contiguous, **no gap, no duplicate** | 70 blocks, contiguous | PREMISE HOLDS. The previous pass's "U.94–U.106 do not exist" is **false**; the previous pass's "re-pointed them" is **false** (nothing was written) |
| Live `U.114`/`U.115` citations in Stage-2 files | **39** occurrences on 35 lines | 39 | CONFIRMED (per-file split identical to the brief: part_3 13 · index 10 · part_2 9 · claim_records 3 · claim_records_part_2 2 · part_1 2) |
| `conflicts.csv` Stage-2 rows | **70** (`stage2`), ids `U.44`–`U.113` | 70 | CONFIRMED |
| `U.114` / `U.115` in the register | registered as **`stage3` `P-U.114`** (five 1999-03-11 Buschman sales/equipment agreements in the Q1-1999 10-Q) and **`stage3` `P-U.115`** (DEF 14A 1998 officer roster `(Aposporos, Dalzell, Duenas, Kaphan, Spiegel)`). Stage-3 total rows: 55 | same | CONFIRMED — both ids belong to Stage 3; Stage 2 has no claim on them (§9.3) |

**Defect statement.** The price-walk repair pass wrote citations to `U.114`/`U.115` into Stage 2 and its report asserted the matching §U blocks had been emitted and the rows reserved; neither the blocks nor the rows exist in Stage 2, and the ids are already spoken for by Stage 3. Every one of the 39 citations is therefore dangling *and* collision-bearing.

---

## 1. The 39 sites, classified and disposed

Classification key — **(a)** claim already registered under an existing Stage-2 block `U.44–U.113` → re-point by label (§14.12); **(b)** claim is genuinely new Stage-2 material → mint as `U.113a` (second block, if needed, `U.113b`), per the `U.111a` addendum precedent.

| # | File | Line | Id cited | Claim at the site (read in context) | Class | Disposition |
|---|---|---|---|---|---|---|
| S01 | stage_2_part_1.md | 66 | U.115 | FY1996 opex/loss as-filed vs the issuer's later printings, UNRECONCILED | (b) | → `U.113a` |
| S02 | stage_2_part_1.md | 68 | U.115 | same restated pair, "stops being the only printings" | (b) | → `U.113a` |
| S03 | stage_2_part_2.md | 255 | U.115 | FY1996 equity/retained-earnings row keyed to §P147 restatement | (b) | → `U.113a` |
| S04 | stage_2_part_2.md | 306 | U.115 | FY1997 close $147,758k as filed vs $147,787k / $(31,020)k later printed | (b) | → `U.113a` |
| S05 | stage_2_part_2.md | 356 | U.115 | 22.0%→19.5% pair whose FY1997 denominator is restated | (a)+(b) | → `U.52` (pair) ; `U.113a` (restatement) |
| S06 | stage_2_part_2.md | 360 | U.115 | 26.4% marketing ratio on three bases incl. restated | (b) | → `U.113a` |
| S07 | stage_2_part_2.md | 500 | U.115 | P-window row citing restated FY1997 loss path | (b) | → `U.113a` |
| S08 | stage_2_part_2.md | 530 | U.115 | P80a `(PB)` margin tag, both legs restated | (b) | → `U.113a` |
| S09 | stage_2_part_2.md | 560 | U.115 | P106 FY1996 net loss as-filed vs restated | (b) | → `U.113a` |
| S10 | stage_2_part_2.md | 604 | U.115 | P147 five EPS bases, numerator moved twice | (a)+(b) | → `U.55` (three as-filed LPS bases) ; `U.113a` (moved numerator) |
| S11 | stage_2_part_2.md | 759 | U.115 | "only the first three are on the filed $(5,777)k numerator (→ U.55; → U.115, appended by the …)" | (a)+(b) | → `U.55` ; `U.113a`, prose "appended by" corrected to "minted by" |
| S12 | stage_2_part_3.md | 97 | U.114 | §T row: amendments read at line, U.95 CLOSED by that pass | (a) | → `U.95` |
| S13 | stage_2_part_3.md | 100 | U.114 | §T row: $14–$16 range filed as an intention; U.52, U.97 | (b) | → `U.113b` |
| S14 | stage_2_part_3.md | 101 | U.114 | §T row: Amendment No. 4, 1997-05-13, is the pivot | (b) | → `U.113b` |
| S15 | stage_2_part_3.md | 102 | U.114 | §T row: No. 5 re-files (not first files) 3,000,000 at $14–16 | (b) | → `U.113b` |
| S16 | stage_2_part_3.md | 104 | U.114 | §T row: $18.00 announced 14 May, $2.00 over the filed ceiling | (a) | → `U.95` (+ `U.98`) |
| S17 | stage_2_part_3.md | 140 | U.115 | §H/§K cell: opex $9,902k vs $9,438k, largest part of the $469k restatement | (b) | → `U.113a` |
| S18 | stage_2_part_3.md | 140 | U.115 | same line, "(§P147 → U.55, **U.115**)" | (a)+(b) | → `U.55` ; `U.113a` |
| S19 | stage_2_part_3.md | 140 | U.115 | same line, "RESTATED PAIR (AUDIT-5 R-3 / U.115 …)" | (b) | → `U.113a` |
| S20 | stage_2_part_3.md | 202 | U.115 | §U-adjacent note: FY1997 printed $147,787k / $(31,020)k | (b) | → `U.113a` |
| S21 | stage_2_part_3.md | 242 | U.115 | UG-4: FY1998/FY1999 rows carry the FY1996/FY1997 restatements | (b) | → `U.113a` |
| S22 | stage_2_part_3.md | 275 | U.115 | "both re-opened at U.115" (three/five FY1996 EPS enumerations) | (a) | → `U.55` |
| S23 | stage_2_part_3.md | 296 | U.115 | §T row: FY1999 10-K restated opex $9,902k vs as-filed $9,438k | (b) | → `U.113a` |
| S24 | stage_2_part_3.md | 1350 | U.114 | inside U.95's closure text: "re-registered as the appended **U.114**" — the phantom assertion | (b) | prose corrected → `U.113b`, "minted … in this volume, no register row pending" |
| S25 | stage_2_index.md | 28 | U.115 | asserts spine `§U.44 → §U.115`, "72 blocks … against 70 rows" | phantom | rewrite to true counts |
| S26 | stage_2_index.md | 29 | U.114 | "two-row excess is deliberate: U.114 (IPO price-walk re-key)" | phantom | rewrite |
| S27 | stage_2_index.md | 30 | U.115 | "U.115 (the FY1996/FY1997 restatement pair) were appended …" | phantom | rewrite |
| S28 | stage_2_index.md | 39 | U.114 | "§Q now Q17–Q69; U.114 and …" | phantom | rewrite |
| S29 | stage_2_index.md | 40 | U.115 | "…U.115 records appended 2026-09-25" | phantom | rewrite |
| S30 | stage_2_index.md | 41 | U.115 | "volume 2 carries 72 conflict records (U.44–U.115)" | phantom | rewrite |
| S31 | stage_2_index.md | 77 | U.114 | "spine emits 72 blocks: U.114 and U.115 are emitted with their CSV rows … and are RESERVED" | phantom | rewrite |
| S32 | stage_2_index.md | 77 | U.115 | same line, second token | phantom | rewrite |
| S33 | stage_2_index.md | 124 | U.114 | repair log: "'filing date' wording is retracted at every site (U.114)" | (a)+(b) | → `U.112`/`U.113b` per site |
| S34 | stage_2_index.md | 126 | U.115 | repair log: "the FY1996 EPS enumeration moves from three bases to five (U.115)" | (a) | → `U.55` |
| S35 | stage_2_claim_records.md | 485 | U.114 | K25 price-walk record "Conflicts: U.45, U.114" | (b) | → `U.113b` |
| S36 | stage_2_claim_records.md | 658 | U.115 | P45 five LPS bases record "→ §P147, §U.115" | (a)+(b) | → `U.55` ; `U.113a` |
| S37 | stage_2_claim_records.md | 840 | U.114 | Q60 "Conflicts: U.95 CLOSED by this pass, U.98, U.114"; "obsolete on its own filing date" struck | (b) | → `U.113b` |
| S38 | stage_2_claim_records_part_2.md | 150 | U.114 | U.95 record: "damage … re-registered as the appended U.114 rather than renumbering" | (b) | prose corrected → `U.113b` |
| S39 | stage_2_claim_records_part_2.md | 150 | U.115 | "the four EPS/LPS variants are now FIVE (§P147, → U.115)" | (a) | → `U.55` |

Planned minting: **`U.113a`** = the as-filed-vs-restated pair (FY1996 and FY1997 figures the issuer's own later 10-Ks reprint differently) — carries S01–S10, S17–S23, S36 and the (b) halves of S05/S10/S11/S18/S33. **`U.113b`** = the IPO price-walk re-key (Amendment No. 4 of 1997-05-13 sets the 3,000,000 / $14.00–$16.00 state that the corpus had keyed to 14 May; "obsolete on its own filing date" retracted) — carries S13–S16, S24, S33(b), S35, S37, S38.

Dispositions marked (a) are confirmed only after the block texts of `U.52`, `U.55`, `U.95`, `U.97`, `U.98`, `U.112` are read on disk; any site that fails that check stays at the minted block rather than being force-fitted. Nothing is renumbered and `U.114`/`U.115` are not taken.

---

## 2. Register rows — EMITTED ONLY, NOT APPLIED

To be appended by the run owner. Two Stage-2 rows, ids `U.113a`/`U.113b` (addendum form per the `U.111a` precedent; they do **not** consume `U.114`/`U.115`).

>>> CSV APPEND BLOCK: conflicts.csv
"Amazon.com, Inc.",stage2,U.113a,K; P; R; T,"FY1996 net loss $(5,777)k and FY1997 net sales $147,758k / net loss $(27,590)k / operating loss $(27,610)k are the as-filed record and are the figures this stage's argument uses; total operating expense as filed $(9,438)k","10-K405 acc. 0000891020-97-001303 l.1186 (opex), l.1242-1247; S-1/A No. 5 acc. 0000891020-97-000839 audited statements of operations l.3748-3751",1997-05-14,"The issuer's own FY1998 and FY1999 10-Ks later reprint the SAME fiscal years differently: FY1996 net loss $(6,246)k (+$469k, 8.1%, on byte-identical net sales, cost of sales and gross profit) with total operating expense $(9,902)k, and FY1997 net sales $147,787k with net loss $(31,020)k","10-K_FY1998 acc. 0000891020-99-024187 Selected Financial Data l.1242/l.1244/l.1247; 10-K_FY1999 acc. 0000891020-00-000622 Selected Financial Data l.1761/l.1763/l.1765 and footnote (1) l.1788",2000-03-16,"Same company, same audited years, two printings two and three years later; the movement is inside operating expense (+$464k of +$469k) and no document in sources/ reconciles it, so the disagreement is between filings and not between a filing and a secondary report. The later printings also move FY1997 sales by $29k, which no footnote explains.","High — both sides are Tier-1 primary filings of the issuer itself and each is read to line.","Treat the as-filed set as the stage's working record and every citation to it as bounded: the later printings are neither a correction nor a retraction but a second filing fact, and the FY1996/FY1997 deltas are UNRECONCILED, never causal. The FY1999 footnote 'Reflects restatement for pooling of interests' is recorded as a CANDIDATE reason, not the reason.","UNKNOWN whether the pooling-of-interests footnote is the whole of the $469k, since no instrument reconciles opex line by line; UNKNOWN why FY1997 net sales moves $147,758k to $147,787k; no confidence level and no consequence figure is retracted at any site.",medium
"Amazon.com, Inc.",stage2,U.113b,K; Q; R; T,"The corpus carried the 3,000,000-share size and the $14.00-$16.00 range as FIRST FILED on 1997-05-14 by S-1/A No. 5, and printed the range document as obsolete on its own filing date because $18.00 was announced the same day","stage_2 §Q/§K rows as written before the AUDIT-4/AUDIT-5 combine; S-1/A No. 5 acc. 0000891020-97-000839 (filed 1997-05-14) l.673",1997-05-14,"Amendment No. 4 (acc. 0000891020-97-000822), filed 1997-05-13, is the instrument that first states 3,000,000 shares at $14.00-$16.00; No. 5 RE-STATES the identical state on 1997-05-14, so the range document was NOT obsolete on its filing date and the $2.00 gap is against a ceiling the company had filed the day before the announcement","S-1/A Amendment No. 4 acc. 0000891020-97-000822 (read 2026-09-25, cited to line) and Amendment No. 5 acc. 0000891020-97-000839, compared line by line; 424B1/pricing release announcing $18.00",1997-05-13,"One dated state was attributed to the wrong accession and the wrong day; both amendments are in the restored primary set and were readable from the start, so the error is a reading debt inside the dossier rather than a gap in the record.","High — the finding rests on two filed instruments read at line level against each other, not on inference.","The price walk is seven dated states across eight accessions of one instrument; re-key No. 4 to 13 May as the origin of the $14-$16/3,000,000 state, keep $18.00 as an announcement one day after the last filed ceiling, and retract the 'obsolete on its own filing date' wording at every site that carried it.","UNKNOWN whether the issuer re-filed on 14 May for a commission reason, a share-count reason or neither, because neither amendment states a reason; the 60,000-share gap (U.45) and the $45,191k bundling question (U.64) are untouched by this block and stay open.",high
>>> END CSV APPEND BLOCK

**Effect when appended:** Stage-2 `conflicts.csv` rows 70 → **72**; §U blocks in `stage_2_part_3.md` 70 → **72** (70 numbered `U.44–U.113` + the two addenda `U.113a`, `U.113b`). Block-to-row 1:1 is restored without taking a Stage-3 id. Until the owner appends, the volume states 70 blocks / 70 rows with two addenda emitted-not-applied.
