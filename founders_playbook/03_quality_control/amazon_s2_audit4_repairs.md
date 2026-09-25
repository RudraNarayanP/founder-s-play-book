# AUDIT 4 + AUDIT 5 · AMAZON.COM STAGE 2 — COMBINED REPAIR LOG (run 6)

Sheet: `03_quality_control/amazon_s2_audit4_repairs.md` · Executor: repair agent, **not** the author of either
sheet · Date 2026-09-25 · **Web requests: 0.**
Work orders read in the mandated order: `amazon_s2_audit4_hindsight.md` (FAIL, checks 1–5, C-1…C-16) then
`amazon_s2_audit5_adversarial.md` (CONDITIONAL, R-1/R-2/R-3 blocking).

**Files edited (permitted set only):** `stage_2_part_1.md`, `stage_2_part_2.md`, `stage_2_part_3.md`,
`stage_2_index.md`, `stage_2_claim_records.md`, `stage_2_claim_records_part_2.md`.
**No `*.csv` touched** — the binding agent holds them. Every register-side wish is in
`## For the register owner` at the foot of this sheet.

**Log discipline:** written in full **before the first edit**; outcomes appended as work completes.
Status tokens: `APPLIED` / `PARTIAL` / `NOT-DONE` / `INSTRUCTION-WRONG`.

---

## 0. Source lines quoted and verified THIS pass, before any edit

Every citation below was read off disk with `sed` line-for-line, not lifted from an audit sheet.

| Doc (all under `company_001_amazon/sources/`) | Line | Verbatim / measured |
|---|---|---|
| `S-1A-No1_acc-0000891020-97-000603_filed-1997-04-21.txt` | l.246–248 | "It is currently estimated that the initial public offering price will be between / **$12.00 and $14.00 per share.**" |
| same | l.192 | fee table: "Common Stock, $0.01 par value per share... **2,875,000 shares  $14.00  $40,250,000  $12,197(3)**" |
| `S-1A-No2_…filed-1997-04-29.txt` | l.234–235 | "…**$12.00 and $14.00 per share.**" |
| `S-1A-No3_…filed-1997-05-09.txt` | l.222–223 | "…**$12.00 and $14.00 per share.**" |
| `S-1A-No4_acc-0000891020-97-000822_filed-1997-05-13.txt` | l.241–243 | "It is currently estimated that the initial public offering price will be between / **$14.00 and $16.00 per share.**" |
| same | l.233 | "**3,000,000 SHARES**" (cover block) |
| same | l.186 | fee table: "**3,450,000 shares  $16.00  $55,200,000  $16,727(3)**" |
| same | l.368–369 | "Common Stock offered....................................... **3,000,000 shares**" |
| same | l.673 | "near future. **B&N, specifically, has launched a Web site to sell books online** and has a relationship with AOL…" |
| `S-1A-No5_…filed-1997-05-14.txt` | l.224–225 | "…**$14.00 and $16.00 per share.**" |
| same | l.4414 | "The Company **is evaluating** Barnes & Noble, Inc.'s claims **and intends to defend against them vigorously**." |
| `S-1A-No6_acc-0000891020-97-000847_filed-1997-05-14.txt` | l.225–226 | "…**$14.00 and $16.00 per share.**" |
| same | l.4412–4414 | "The Company is **still in the process of evaluating** Barnes & Noble, Inc.'s claims, and therefore **is not in a position at this time to estimate possible outcomes**. The Company intends to defend against the lawsuit vigorously." |
| `424B1_…filed-1997-05-15.txt` | l.124 | "**Per Share  $18.00  $1.26  $16.74**" |
| `10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` (10-K405) | l.1177 / l.1178 / l.1180 | FY1996 col.: Net sales **15,746**; Cost of sales **12,287**; Gross profit **3,459** |
| same | l.1182 / l.1183 / l.1184 / l.1186 | FY1996: Marketing **6,090**; Product development **2,313**; G&A **1,035**; **Total operating expenses 9,438** |
| same | l.1188 / l.1190 / l.1191 / l.1192 | FY1996: Loss from operations **(5,979)**; Interest income **202**; Interest expense **--**; **Net loss $(5,777)** |
| same | l.1194 / l.1197 | "**Pro forma** basic and diluted loss per share(1)… **$(0.31)**" on **18,544** pro-forma shares |
| `10-K_FY1998_acc-0000891020-99-000375_filed-1999-03-05.txt` | l.1222 / l.1223 / l.1225 | FY1996 col.: Net sales **15,746**; Cost of sales **12,287**; Gross profit **3,459** (identical to 10-K405) |
| same | l.1227 / l.1228 / l.1229 / l.1234 | FY1996: Marketing **6,090**; Product development **2,401**; G&A **1,411**; **Total operating expenses 9,902** |
| same | l.1236 / l.1242 / l.1244 / l.1247 | FY1996: Loss from operations **(6,443)**; **Net loss $(6,246)**; LPS **$(0.06)**; shares **111,271** |
| `10-K_FY1999_acc-0000891020-00-000622_filed-2000-03-23.txt` | l.1732 / l.1733 / l.1735 | FY1996 col.: Net sales **15,746**; Cost of sales **12,287**; Gross profit **3,459** |
| same | l.1737 / l.1738 / l.1739 / l.1740 / l.1741 / l.1746 | FY1996: Marketing **6,081**; Technology and content **2,377**; G&A **1,408**; Stock-based compensation **36**; **Total operating expenses 9,902** |
| same | l.1761 / l.1763 / l.1765 | FY1996: **Net loss $(6,246)**; LPS **$(0.03)**; shares **222,542** |
| same | l.1788 | Selected-Financial-Data footnote, governing both tables' `(1)`: "**(1) Reflects restatement for pooling of interests. See Notes 1 and 2 of Notes to Consolidated Financial Statements.**" |
| String census, 8 × 1997 accessions | — | "over 40% of orders" = **3 prints in each of the 8 accessions (24 total), 0 in the 10-K405** — L-7's count reproduced exactly |

**Independent arithmetic done on this pass, and it contradicts an audit instruction — see §4 INSTRUCTION-WRONG.**

---

## 1. GROUP A — the price walk (R-1, R-2, R-3-of-L-4/L-5, U-1…U-3; with C-10)

Canonical replacement text, used at every site and nowhere paraphrased into quotation marks:

> blank (24 Mar, S-1 orig.) → **$12.00–$14.00 on 2,500,000** (No. 1, 21 Apr, l.247–248; No. 2, 29 Apr,
> l.234–235; No. 3, 9 May, l.222–223) → **$14.00–$16.00 on 3,000,000** (No. 4, 13 May, l.242–243; re-filed by
> No. 5, l.224–225, and No. 6, l.225–226, **both 14 May**) → **$18.00** (424B1, 15 May, cover l.124).
> Eight accessions, seven dated states. **No document in the corpus states an hour for any 13–15 May 1997 event.**
> The differentials that carry information are 24 Mar → 21 Apr, 9 May → 13 May (four days), 13 May → 15 May (two days).

**What survives and is kept at every site:** $18.00 ÷ $16.00 − 1 = **+12.5%** over the last filed ceiling;
all-primary / no selling stockholder; **+500,000 = 20% upsize**; ten-house firm commitment; 7.00% gross spread;
$54,000,000 gross / $50,220,000 before expenses; 18.00 ÷ 15.00 = +20% against the assumed price.
**What is deleted everywhere:** "the same morning", "filed that morning", "14 May morning", "five days earlier",
"the FIRST stated price range in the whole lineage", "one source in four dated states".
**What is added everywhere it is load-bearing:** the deletion test — the boundary does not rest on the price
(`part_1` §D.6 and boundary l.42 already carry it), so the honest argument (a five-week sequence the company ran
itself, cleared two days after its own last ceiling) replaces the same-day-shock rhetoric rather than defending it.

| Ref | Site | Before (exact) | After | Authorising document line | Status |
|---|---|---|---|---|---|
| **A-1** | `part_1` l.24 (pricing leg) | "after the filed range moved $12–14 → $14–16 **the same morning**, a 20% upsize **clearing above its own ceiling**" | sequence per the canonical text + "no document states an hour"; upsize and +12.5% kept | No. 4 l.242–243 (13 May); §Q l.95 already dates No. 4 to 13 May | PENDING |
| **A-2** | `part_1` l.53 ("The deal and its repricing") | "Range: blank → $12.00–$14.00 / 2,500,000 (9 May) → $14.00–$16.00 / 3,000,000 (**14 May morning**) → $18.00"; "one source, **four dated states**" | canonical walk; "**eight accessions, seven dated states**" | No. 1 l.247–248; No. 4 l.242–243/l.233/l.369/l.186 | PENDING |
| **A-3** | `part_1` l.79 (§A.3 keystone) | "Amendment No. 3 (1997-05-09): … Amendment No. 5 (1997-05-14, the same day as pricing) … $2.00 above the ceiling the company had filed **that morning** … **inside one week** … one source in four dated states" | re-keyed; the "company ran its own sequence" reading stated; +12.5%/20%/all-primary/firm-commitment retained; **R-7 clause added** (the priced document is the 24th printing of the ">40% of orders" self-measurement — provenance, no confidence change) | No. 4 l.242–243; No. 6 l.225–226; 424B1 l.124; print census | PENDING |
| **A-4** | `part_1` l.27 ("Nos. 1/2/4/6 **unread**") | four accessions declared unread; U.95 keeps them at UNKNOWN contents | **read**; the four carry: No. 1 = first stated range; No. 4 = upsize + $14–16 + "B&N has launched" + assumed $15.00; No. 6 = the B&N litigation hedge | the four files are on disk, lines quoted in §0 | PENDING |
| **A-5** | `part_2` l.305 (§L) | "deal +20% larger than **five days** earlier" | "**two days** earlier (No. 4, 13 May)" | No. 4 filed 13 May vs 424B1 15 May | PENDING |
| **A-6** | `part_2` l.420 (§N row) | decision window "1997-05-09 → 05-15"; "+$2.00 at both ends **in five days**, then $18.00 — 12.5% above the ceiling of the document filed the **previous day**, thereby **obsolete on its own filing date**" | window **1997-04-21 → 1997-05-15**; range moved +$2.00 at both ends and size +500,000 **between 9 and 13 May (four days)**; $18.00 is +12.5% over a ceiling filed **13 May** and re-filed **14 May**; "obsolete on its own filing date" **struck** — the ceiling document was current for two days, not obsolete on filing | No. 3 l.222–223 → No. 4 l.242–243 | PENDING |
| **A-7** | `part_2` l.613 (§P156) | "The offering's **five-day** re-shaping" + four-state walk + "filed one day earlier" | seven-state walk, "the offering's **twenty-four-day** re-shaping", interval named per state | as A-1..A-6 | PENDING |
| **A-8** | `part_3` l.94 (§Q 1997-05-09 row) | "**the first stated price range in the whole lineage**, $12.00–$14.00" | "the range **re-stated** for the third time; **first stated in No. 1 on 1997-04-21 (l.247–248)**". Simon & Schuster + the margin-intention wording stay as No. 3's own-only content | No. 1 l.247–248 | PENDING |
| **A-9** | `part_3` l.95 (§Q 1997-05-13 row) | "Amendment No. 4 (acc. …822) filed — body **UNTRIED** locally … UNKNOWN (contents)" | **read**, with its own-only content (upsize, $14–16, B&N rewrite, assumed $15.00) | No. 4 l.233/l.242–243/l.369/l.673 | PENDING |
| **A-10** | `part_3` l.98 (§Q 1997-05-14 row) | "$2.00 above the ceiling of the prospectus **filed that morning**"; "accession …847 filed (a further amendment body, **UNTRIED**)" | ceiling filed **13 May**, re-filed **twice on 14 May**; no hour stated anywhere; …847 = **No. 6**, read, and it is the last pre-pricing instrument and the first filing of the B&N hedge | No. 6 l.225–226, l.4412–4414 | PENDING |
| **A-11** | `part_3` §T l.262–263 (S0801/S0802 rows) | S0802 "**Earns its own citation only for what the original lacks: the FIRST stated price range in the whole lineage**" | S0802 = margin-intention wording, COR-12 employee anchor, **Simon & Schuster first addition**; the "first range" credit moves to the new **S0807** row | No. 1 l.247–248 | PENDING |
| **A-12** | `part_3` §T — four new rows **S0807 / S0808 / S0809 / S0810** (Nos. 1 / 2 / 4 / 6) with their own-only content, and U.95 re-adjudicated UNKNOWN → **CLOSED-with-finding** in the same row | R-2 | file paths + lines in §0 | PENDING |
| **A-13** | claim records **Q60** l.840, **Q59** l.838, **K25** l.485, **N17** l.569, **P54** l.676, **T24** l.942 | "the ceiling of the prospectus filed **that morning**"; "**four dated states**"; "the offering's **five-day** re-shaping"; "**filed one day earlier**"; "**A5 was obsolete on its own filing date**"; S0802 "**the FIRST stated price range in the whole lineage**" | same re-key as the narrative sites; class and confidence unchanged | as above | PENDING |
| **A-14** | `part_3` l.93 / l.96 and `part_2` l.383 (**R-4 / L-4 / U-4**) | "**Filed thirteen days before Amazon's amendment**"; "**the same sentence, one day after B&N's own filing** made it true"; "Between A3 and A5 Amazon's own text changed" | B&N 10-K 1997-05-02 → **eleven days to No. 4 (13 May)**, **twelve to No. 5 (14 May)**; the rewrite is a **No. 4** event; **three states not two** (original 24 Mar "has entered into a …" l.2278 → No. 3 9 May "has a relationship with AOL" → No. 4 13 May "has launched") | No. 4 l.673; No. 3 l.641; S-1 orig. l.2278 | PENDING |
| **A-15** | **R-5 / L-5** — `part_3` l.98, `part_2` §M.9, U.68 | the "not in a position at this time to estimate possible outcomes" hedge carried as a 424B1 wording | first filed **1997-05-14 in No. 6 l.4412–4414, the last pre-pricing instrument**, and reaches the 424B1 unchanged | No. 6 l.4412–4414 vs No. 5 l.4414 | PENDING |
| **A-16** | **R-7 / L-7** — `part_3` §T l.262 (S0801 "all three … prints") and `part_3` U.95 text | "three prints" | "**three prints in each of the eight 1997 accessions (24), zero in the 10-K405**" | census in §0 | PENDING |
| **A-17** | **R-9** — `part_1` l.42 (§Boundary substantive row) and §D.0 l.176 | — | append: 1996-12-31 is "not only unaudited and conflicted but **observationally empty**: every artifact that would certify it is 1997 paper"; and to the five-quarters row "no same-quarter comparison exists; the company's own seasonality text is future tense in every instrument" | No. 5 l.604/1780; 424B1 l.484/1658; 10-K405 l.629/1350 (quoted in §0 next pass) | PENDING |
| **A-18** | **new §U block U.114 + `>>> CSV APPEND BLOCK: conflicts.csv` row, reserved to the register owner** | — | registers the price-walk re-key as a conflict with both sides kept (the spine's four-state/same-morning account vs the eight-accession filed sequence) | R-1's "register as U.114, do not renumber" | PENDING |

---

## 2. GROUP B — the restatement layer (R-3 / L-2)

**The spine's as-filed set is correct and stays.** §P106/P107/P107a/P108/P109/P110 and §A l.63 print
$(5,777) / $(5,979) / 9,438 / 6,090 / 2,313 / 1,035 — exactly the 10-K405 columns at l.1182–1192. Nothing is
retracted. What is added is the **pair**, because two audited annual reports on disk print the same fiscal year
differently.

| Ref | Site | Before | After (restatement pair) | Authorising lines | Status |
|---|---|---|---|---|---|
| **B-1** | `part_2` **P147** l.604 | "**two as-filed bases and one PRO FORMA basis across three documents, numerator unchanged at $(5,777)k**" | "**five bases across five documents; the numerator moved twice: $(5,777)k as filed (S-1 orig., No. 5, 10-K405) → $(6,246)k in the FY1998 and FY1999 10-Ks, +$469k / 8.1% larger loss**"; the two new rows carry $(0.06)/111,271k and $(0.03)/222,542k; "numerator unchanged" **deleted** | 10-K_FY1998 l.1242/1244/1247; 10-K_FY1999 l.1761/1763/1765 | PENDING |
| **B-2** | `part_2` §P.2 **l.758** | "**Three FY1996 EPS bases exist in the corpus** and only one is the audited line" | "**Five FY1996 EPS bases exist across five instruments**" + the restatement pair; the $(0.18) retraction and the U.55 pointer kept | same | PENDING |
| **B-3** | `part_1` l.63 §A | "Audited FY1996: … net loss **$(5,777)k**" | append "**as filed; the issuer's own FY1998 and FY1999 10-Ks later printed FY1996's loss as $(6,246)k (+$469k, 8.1%) — unreconciled in any local document**" | same | PENDING |
| **B-4** | **composition of the $469k** — P147 and U.115 | — | **NOT "below the operating line".** Net sales 15,746, cost of sales 12,287 and gross profit 3,459 ARE byte-identical across the four instruments; **total operating expenses are NOT**: **$9,438k** as filed (10-K405 l.1186) vs **$9,902k** in both later 10-Ks (l.1234 / l.1746) — **+464**, all of it inside operating expense (product development 2,313→2,401 **+88**; G&A 1,035→1,411 **+376**; marketing 6,090 unchanged in the FY1998 10-K, printed 6,081 in the FY1999 10-K against a stock-compensation carve-out of 36 that leaves the 9,902 total intact) — plus interest expense **$0 → $(5)k = +5**. **464 + 5 = 469, exactly the movement.** Loss from operations therefore also moved: **$(5,979) → $(6,443)**. Written as `unreconciled`; the FY1999 10-K's "restatement for pooling of interests" footnote (l.1788) is named as a **candidate, not adopted** | 10-K405 l.1182–1192; 10-K_FY1998 l.1227–1242; 10-K_FY1999 l.1737–1761 | PENDING |
| **B-5** | FY1997 pair | §A l.65, §L l.306, §M.2, §M.6, §Q l.105, §R l.134, P80a | annotate: FY1997 net sales printed **$147,758k** (10-K405 l.1177) and **$147,787k** (FY1998 10-K l.1222 / FY1999 10-K l.1731); FY1997 net loss **$(27,590)k** → **$(31,020)k**; FY1997 marketing **38,964 / 40,486 / 40,077** — three printings, so the "26.4% of net sales" at §M.6 has three bases and §F.1's 38.7% has two (6,090 / 6,081 ÷ 15,746 = 38.7% / 38.6%) | same | PENDING |
| **B-6** | `part_2` P106 l.560 | "(5,777) / (0.25) / 22,655" | append the two restated rows as a **pair**, classing the original as-filed value unchanged | same | PENDING |
| **B-7** | share-basis warning | — | the same fiscal year carries **two different share counts two years apart** (111,271k vs 222,542k), so the cumulative split factor applied to the 1996 column differs between the two 10-Ks; **S2E-46's split warning does not reach this**, and no cross-year per-share ladder may inherit it | 10-K_FY1998 l.1247; 10-K_FY1999 l.1765 | PENDING |
| **B-8** | §A.2 UNKNOWN list, `part_1` l.75 | list of searched absences | add: "**and no reconciliation anywhere in the corpus of the FY1996 or FY1997 loss restatement**" | absence verified by the four tables printed identically above the operating line and differently below it | PENDING |
| **B-9** | **new §U block U.115 + `>>> CSV APPEND BLOCK` row**, reserved to the register owner | U.55 currently asserts three bases | register the five-basis / moved-numerator finding as an appended conflict against U.55, **no renumbering, no confidence changed** | R-3 | PENDING |

---

## 3. GROUP C — the hindsight failures (audit 4 checks 1–5)

Priority order as briefed.

| Ref | Site | Before | After | Authority | Status |
|---|---|---|---|---|---|
| **C-1** | `part_1` l.180 (§D.0 row head), l.206 (§D.2 Cost), l.523 (§H.2 null) | the FY1997 margin pair and "**3.25 points of gross margin in a quarter**" carried **untagged** where they do the most argumentative work | tag `22.00% (Q1-97) → 18.75% (Q2-97)` and the 19.5% `(PB)` in-cell at all three sites; row heading → "the only channel whose **post-boundary** consequence was filed"; §H.2's closing clause → "**and no measured consequence of its newest lever inside the window at all** — the −3.25-point fall is Q2-1997 `(PB)` (→ U.52)" | U.52 l.481–498; the identical series is already tagged at `part_2` l.303, l.357, l.421 and `part_3` l.84 | PENDING |
| **C-2** | `part_1` l.208 (§D.2 *What it proved*) | "That management forecast its own margin loss and **was right within one quarter** — the cleanest self-measured test in the stage" | "That management **wrote its own margin forecast into an offering document before it could be checked**; the check falls in Q2-1997 `(PB)` — so this row evidences a **forecast**, not a **hit**" | U.52; §R Margins l.134 | PENDING |
| **C-3** | `part_3` l.185–187 (§S "three rows that are NOT gaps") | "tagged `(PB)` **everywhere it appears**" | narrowed to what is true: "tagged `(PB)` at §K, §L, §M.6, §N, §Q, §R and §P.2; **three uses in §D.0/§D.2 and §H.2 of part_1 were untagged and were repaired by this pass (audit-4 DR-1); any re-repair of the margin pair must re-open those three sites**" | this is a false universal **about its own volume** | PENDING |
| **C-4** | `part_1` l.183 heading, l.194 *What it proved*, l.252 §D.6 | "distribution **that scales without the company**"; "the one part of the Stage-2 model that **demonstrably scaled**"; "**4,800 third-party storefronts live** at 1996-12-31 reproducing Amazon's catalogue with none of Amazon's headcount or leases"; and "at **negligible marginal cost**" | heading → "distribution **disclosed** without the company's own premises"; "*demonstrably scaled*" → "**counted once, then degraded in precision**"; "storefronts live" → "**over 4,800 registered members (undefined; no live-site, revenue or order count exists)**"; **"at negligible marginal cost" struck from §D.1** — it is filed language about the **e-mail loop** (`part_2` l.125 "run 'at a negligible incremental cost'"; `part_1` l.242, l.371–372 same) and is spent here on Associates; §D.6 gains the alternative its own *Did NOT prove* cell already carries (attrition vs accumulation) | §D.1 *Cost* l.192 "UNKNOWN, disclosed nowhere in the window"; §F.1 l.337 and U.51/U.65 "no channel … attributable"; `part_2` l.300 "**no Associates revenue or order share exists**" | PENDING |
| **C-5** | `part_1` l.28 and l.52 (+ l.41) | "where the firm **first held its Delaware form, officers, board**, auditors' consent and a public price" / "Delaware form (effected 1996-06-18), officers, board, signed financing paper (Series A 1996-06-21), auditors' consent, a public price, reporting duties — **all in place only from 05-14/15**" | cut the three 1996 nouns; rest the cut on the four carriers that are genuinely IPO items: **auditors' consent, a public price, effectiveness, continuous reporting duties**. l.41's 1996 items re-labelled **stage-opening evidence**, not end-of-stage proof. Note retained: §B.0 l.93 records the **CIO seat still advertised as to be filled** and the **CTO title four weeks old** at pricing, so "officers first held" is false in both directions | §B.0 l.91–93 (Delaware 1996-06-18; CEO+board on the 1996-05-28 instrument; Covey CFO 1996-12); §Q l.49/l.51/l.53/l.55; U.78, U.102 | PENDING |
| **C-6** | `part_1` l.71 (§A.1 seam) | "…the folklore figure is barred [S2B-23]. `B100` reversed the party outright and is retracted there. **a payment rail still standing on his personal guarantees**, released only as an *intention* at pricing [S2B-54]; and **no valuation of any kind…"** — an ungoverned fragment that also collapses the Seafirst/card distinction | re-list with a lead-in and the §Q distinction restored: "the **Seafirst Bank merchant-account** guarantee **ended December 1996**; the **Wells Fargo and company-card** guarantees were **still live at pricing**, amounts UNKNOWN, release only *intended*" | `part_3` l.66 ("From November 1994 to December 1996, Mr. Bezos personally guaranteed the obligations of the Company under a merchant account with Seafirst Bank"; card guarantees continue); `part_1` l.111 | PENDING |
| **C-7** | `part_1` l.138, l.396 (C-7/C-11) | l.138 "**no dilution with scale**"; l.396 "**Did scale dilute it? No** … structural, not a scaling artefact … against **~100 days of payables, roughly $19m of a $32.7m payable balance** owed to a firm under no long-term agreement" | l.138: the 1996 property stated as unproven — "whether scale would have diluted the dependence is **not knowable inside the window**; the FY1997 leg `(PB)` shows it had not". l.396: the barred point figure replaced by the register's **band** "days payable ≈39.6–84.7 in-window; **neither measures terms** (U.56)"; the FY1997-12-31 dollar sentence **moved to §M.2's consequence entry** and tagged `(PB)` | U.56 l.569–584; §R Supply l.130 already prints the band, not 100 days | PENDING |
| **C-8** | `part_1` l.63, l.152 (C-14 / DR-5) | "federally classified as a **book publisher, SIC 2731**" and "the SIC class is 2731" as bald fact of the stage | inherit §H.1's hedge: "classified **on the EDGAR header** as 2731; the fit is a **Medium** reading and the Commission's reasoning is **UNKNOWN**" | `part_1` l.486, l.529–531 | PENDING |
| **C-9** | `part_1` l.71 / `part_2` l.416 / claim record **N13** l.561 (C-1a/b/c / OD-1) | "**the cheapest capital the firm ever raised**, paid for with a board seat" (3 sites) — a whole-life superlative | bound: "the cheapest capital the company **is filed as having raised to 1997-05-15** — $10.2m cumulative pre-IPO equity, the only priced round in the window; preference at cost, no ratchet, non-cumulative". N13's Class → "**INFERENCE (bounded)**", Conf ≤ Medium, wording "on the filed record the cheapest capital raised **to the boundary**" | method §2/§6; §R Valuation `part_3` l.136 already refuses post-boundary reach; `part_1` l.43 itself carries the 1997-12-23 loan | PENDING |
| **C-10** | `part_2` l.416 *Actual result* (C-15) | "**a contractual price floor constraining every later financing, including the size of the offering**" — unlabelled retrospective | label `RETROSPECTIVE` per method §13, or bound to the window: "constrained the offering's minimum size, per the Ex. 10.2 conversion trigger (≥$20.00 and ≥$7,500,000)" | method §13; §P145; §R Capital l.135 | PENDING |
| **C-11** | `part_2` l.421 *Information available* (C-16) | "The **filed** intention to 'offer attractive pricing programs, which will reduce its gross margins'" offered as information for a **March** decision | "**its own March 1997 pricing decision; filed as an intention in Amendment No. 3, 1997-05-09**" — a March decision cannot have been informed by a May filing; substance survives, direction does not | U.52; §Q l.94 | PENDING |
| **C-12** | `part_2` l.500 §O.7 (C-6) | "and a **$27.6m loss year forming**" (FY1997, post-boundary, doing boundary-time work) | "and the loss run-rate the filed quarterly path was already producing (**$(3,038)k in Q1-1997**)" — the argument (against the IPO's evidentiary value) is kept and strengthened; if the FY1997 figure is kept it is tagged `(PB)` | §L l.304; Q1-197 net loss at §Q l.88 | PENDING |
| **C-13** | `part_2` l.416 *Information available* (audit-4 check 6, CONDITIONAL) | "Q1/Q2-1996 sales 875/2,230" offered as available at the 1996-06-21 closing | "Q1-1996 sales 875 and a **partial** Q2 — Q2-1996 closed 1996-06-30, nine days **after** the closing, so the filed 2,230 was not in hand at the decision date" | §Q 1996-Q2 row l.54; the closing date 1996-06-21 at §Q l.53 | PENDING |
| **C-14** | `part_1` l.67 / l.254 / `part_2` l.301 (**R-6 / L-6 / U-5**) | l.254 "**a founder predicting profit 'by accident' in December 1996**" and l.301 printing the words as a filed observation, both **untagged**, while l.67 carries the full `(NO LOCAL COPY — S2007)` device | carry the S2007 tag at both sites; l.254's speaker corrected to "**a magazine article reporting the founder as saying**" — the words are a journalist's relay, and `part_1` l.112/§N hold founder reasoning UNKNOWN. Sweep string: `by accident` | part_1 l.67's own tag; `sources.csv` S2007 `local_copy: NO` (per `stage_2_index.md` l.47–53) | PENDING |
| **C-15** | `part_3` l.22 (**C-10 / DR-6**) | "the three-date cluster is disclosed at **part_1 l.18**" | re-pointed. Chosen form: name the **label**, not the number — "part_1, the `**Stage:** 2 of 3. **Span:**` header line" — because part_1's own DEFECT-9 self-pointer at l.12–13 now reads "l.22", which lands on a **blank** line while the cluster text is at **l.24**: the same drift class re-creating itself one edit later. Both part_1's self-pointer and part_3's cross-pointer are re-keyed to the label form | `part_1` l.12–13 (DEFECT-9 note); `part_1` l.21/22/24 as read this pass | PENDING |

---

## 4. INSTRUCTION-WRONG — findings against the audit sheets themselves

1. **audit-5 L-2's composition claim is false and the brief repeats it.** Both say the $469k FY1996 movement is
   "**entirely below the operating line**" and that "**total operating expense [is] byte-identical across four
   instruments**". It is not. L-2's own decomposition — "6,090 + 2,401 + 1,411 **in the FY1997 10-K405
   (l.1182–1184)**" — mislabels the source: the 10-K405's l.1182–1184 print **6,090 / 2,313 / 1,035** (sum
   **9,438**, l.1186), and **2,401 / 1,411 are the FY1998 10-K's l.1228 / l.1229**. The movement is
   **+464 inside operating expense + 5 in interest expense = 469**, and loss from operations moves with it
   ($(5,979) → $(6,443)). Only net sales, cost of sales and gross profit are identical across the four. Repaired
   as B-4: written as `unreconciled`, with the composition measured, **not** with a cause.
2. **L-1's "one and a half days" understates its own finding, and the brief's "+20% larger than five days earlier
   is two days" is right, but the sheet's step 2 mis-dates the first range.** L-1 body says the $12–14 range was
   stated "**second or third** printed" by No. 1; No. 1 is simply the **first** accession to state a range (the
   original left it blank), so "second or third" is hedged below what the disk supports. Repaired to
   "**first stated on 1997-04-21**".
3. **audit-4 C-1c changes a `Class`, which my invariant list says only the restatement pairs may do.** The
   instruction is explicit ("Class → INFERENCE (bounded)") and the task names N13 as one of the three sites, so
   it is applied. Reported as an authorised exception, not hidden: it is a claim-record class on a superlative,
   not a quantitative value or a `derived_arithmetic` field, and no DERIVED row is touched.
4. **audit-5 L-1 point 4 asks for "seven dated states across eight accessions"; counted against the disk the
   *price/range* states are seven but the *share* states are fewer** (2,500,000 → 3,000,000 only; the
   2,875,000/3,450,000 figures are fee-table totals including the over-allotment option, not the base offering).
   Recorded at both conventions so no later pass "reconciles" them: **base shares 2,500,000 → 3,000,000; fee-table
   totals 2,875,000 @ $14.00 (No. 1 l.192) → 3,450,000 @ $16.00 (No. 4 l.186)**.
5. **C-12 (audit-4) asks §S to name the §D/§H.2 sites as "a live defect". After this pass they are repaired, not
   live.** §S is written to say repaired-with-a-re-open-warning instead, which is the true state.
6. **audit-5 R-8 asks that §S row UG-4 record "which of the newly-used local documents arrived during Stage 2 and
   which arrived beside it, by reading `_MANIFEST.md`".** `_MANIFEST.md` is outside my permitted edit set **and**
   R-8 itself rules the distinction "the orchestrator's fact, not this auditor's inference". Outcome: UG-4's false
   items are struck (a corpus fact, verifiable now) and the during/beside question is handed to the orchestrator
   in this log rather than answered here.

---

## 5. Sweeps to run before and after (commands, to be reported as measured)

```sh
cd founders_playbook/01_companies/company_001_amazon
# (PB) census
for f in stage_2_part_1.md stage_2_part_2.md stage_2_part_3.md stage_2_claim_records.md stage_2_claim_records_part_2.md; do
  printf "%s %s\n" "$f" "$(grep -o '(PB)' $f | wc -l)"; done
# price-walk class
grep -n "same morning\|that morning\|five days earlier\|first stated price range\|14 May morning\|one day earlier\|four dated states\|obsolete on its own filing" \
  stage_2_part_*.md stage_2_claim_records*.md stage_2_index.md
# untagged margin pair
grep -n "18\.75\|3\.25 points" stage_2_part_1.md
# restatement class
grep -n "numerator unchanged\|Three FY1996 EPS\|three FY1996 EPS" stage_2_part_1.md stage_2_part_2.md stage_2_claim_records.md
# hindsight classes
grep -n "cheapest capital\|demonstrably scaled\|negligible marginal cost\|was right within one quarter\|storefronts live\|first held its Delaware\|by accident" stage_2_*.md
# live-copy status of the four newly-read accessions
ls sources/S-1A-No1* sources/S-1A-No2* sources/S-1A-No4* sources/S-1A-No6*
```

### Measured BEFORE (2026-09-25, pre-edit)

* `(PB)` literal: part_1 **10**, part_2 **16**, part_3 **25**, claim records **88 + 22** = **161 occurrences**,
  **116 lines** carrying the string (index carries 2 more, outside the 161). Reproduces audit-4's census exactly.
* Untagged FY1997 margin pair in `part_1`: **3 sites** — l.180, l.206, l.523.
* Price-walk defect strings live: `same morning`/`that morning` **4** (part_1 l.24, l.79; part_3 l.98; Q60),
  `14 May morning` **1**, `first stated price range in the whole lineage` **2** (part_3 l.94, l.263) **+ 2 more**
  (P156 l.613, T24 l.942), `five days earlier` / `in five days` / `five-day` **4** (part_2 l.305, l.420, l.613;
  N17/P54/K25 family), `four dated states` **2** (part_1 l.53/l.79 "one source in four dated states"; K25 l.485),
  `obsolete on its own filing date` **5** sites, `thirteen days` **1**, `one day after B&N` **1**.
* `cheapest capital … ever raised` **3 sites** (part_1 l.71, part_2 l.416, N13 l.561).
* `numerator unchanged` **1** (P147 l.604) + `unchanged numerator` **2** (B124 l.183, P45 l.658);
  `Three FY1996 EPS bases exist` **1** (l.758).
* `§U blocks` **70** (U.44–U.113) ↔ `conflicts.csv` Stage-2 rows **70** (per `stage_2_index.md` register table).
* 10-K405 as-filed FY1996 set confirmed identical to the spine's §P106/P107/P107a/P108/P109/P110 → **no as-filed
  value is retracted by Group B**.

---

## 6. For the register owner (no CSV touched by this pass)

*(populated as work completes — see foot of sheet)*

---

## 7. Outcomes

*(appended below as each group closes)*
