# Stage-3 register binding — Amazon.com (company_001)

Pass date 2026-09-25. Input: `../01_companies/company_001_amazon/stage_3_pending_registers.md` (134 data rows in
nine `>>> CSV APPEND BLOCK` sections). Authority for the re-keyed register:
`03_quality_control/stage3_sourceid_rekey_map.md` (canonical **S30001–S30081**, application order ST3_A, B, C, D).
Web requests made by this pass: **zero**. Files written: the nine `company_001_amazon/*.csv` registers,
`stage_3_pending_registers.md` (status annotations only — no row text changed), and this report.

## 1. What was parsed and validated

All nine blocks parsed at the canonical width copied from each target register header: `conflicts` 15,
`quantitative` 12, `timeline` 11, `sources` 18, `data_gaps` 8, `decisions` 15, `channels` 11, `failures` 11,
`validation` 11. **134 of 134 rows parsed at canonical width, data rows only, no header emitted, no newline inside
any field, every comma-bearing field quoted** (the quote test is described in §6). Row counts by block match the
emitted counts: conflicts 16, quantitative 47, timeline 35, sources 2, data_gaps 12, failures 8, validation 7,
decisions 5, channels 2.

## 2. The binding rule this pass used (stated so it can be re-run or reversed)

1. **Content, never position.** A bare `S3001`-style citation is read as *a claim about a document*, and the claim
   (form type, period, filing date, line numbers, exhibit names, and whether the document could even have existed on
   the row's date) is tested against the map's `Source` column and the dossier text in `stage_3_part_3.md`
   (`§P248`, `§P249`, `§P250`, `§P234`, `§P263` were used as the deciding evidence where the row named a `§P`).
   Where the cited number's three candidates all fail the row's own text, the citation is treated as **falsified**
   and the row is re-bound from its text, not from its number (timeline row 33; see §4).
2. **Alias sets are not ambiguity.** Because the re-key kept each dossier's registration, *one accession is
   registered under several canonical ids* (FY1997 10-K405 = S30005/S30032/S30053/S30072; FY1998 10-K =
   S30009/S30031/S30054/S30073; Q3-1999 10-Q = S30011/S30043/S30065/S30076; 8-K 1997-11-07 = S30004/S30040;
   8-K 1998-04-17 = S30006/S30048; 8-K 1999-02-03 = S30019/S30041; 8-K 1999-03-30 = S30020/S30061;
   424B2 1998-08-13 = S30022/S30039; 424B3 = S30017/S30047/S30069; Q1-1999 10-Q = S30018/S30042/S30060/S30074;
   Q2-1999 10-Q = S30010/S30064; ARS 1997 = S30012/S30050/S30059/S30080; ARS 1998 = S30013/S30050/S30068;
   DEF 14A 1999 = S30008/S30035/S30067; intake manifest = S30030/S30070). Once the row's text identifies **the
   document**, the choice among ids naming that same document is not a factual question, so this pass binds to
   **the earliest-numbered canonical id whose primary object is that document** (S30039, not S30022, for the 424B2:
   S30022's primary object is the S-4 that bundles it). Every alias set used is listed in this section; nothing is
   silently merged. **Candidate *documents* that both fit a row is a different matter — see §3 (held).**
3. **Free-text citations are prefixed, never replaced.** In `quantitative.source` and
   `conflicts.claim_a_source/claim_b_source` the bound ids are written as `S30009; S30075 — <original text>`, so
   the line-level evidence survives verbatim. Legs citing a filing that the register does not carry keep their text
   and gain an explicit `[no canonical id: …]` marker; legs citing project-internal artefacts (a dossier file, a
   `§P`/`§P.2` table, a machine string-count, `context_appendices.md`) were **left unbound rather than given an id
   they cannot support**.
4. **New ids.** `S3P-001`/`S3P-002` were this part's collision workaround. With the collision closed they are
   re-keyed to the next free canonical ids **S30082** (Form 10-K/A FY1999, acc. 0000891020-00-001638) and
   **S30083** (Forms 8-K events 1998-11-19 and 1999-07-21); the re-key is recorded inside each row's `notes` and
   every register row citing `S3P-*` now carries the canonical id. S30083's second accession is *also* registered
   as S30077 — left as two ids over one accession, §9.4 forbids re-defining an id, and the duplication is in
   §7 (residual risk).

## 3. Held rows (2) — not applied, both candidates recorded

| Held row | Its own citation | Candidate documents that fit | Why irreducible | The fact that would separate them |
|---|---|---|---|---|
| `decisions.csv` block row 3 — 1998-06-01, "Pay a stock dividend rather than raise the par value or issue new shares for the 2-for-1 split" (D-3) | `S3P-002` (= S30083) | (a) **S30083** itself, whose registered passages are the 1998-11-19 8-K announcing the **3-for-1** and the 1999-07-21 8-K approving a **different 2-for-1**; (b) the **FY1998 Form 10-K** (S30009 et al.), which per U.164 l.1175-1176 prints "the 2-for-1 stock split effected June 1 1998"; (c) **`10-Q Q1-1998` l.468**, named first for this split in `stage_3_part_3.md` §P234 — **unregistered in `sources.csv`** | The row's decision date (1998-06-01) and its stated mechanism (stock dividend to holders of record 1998-05-20) cannot be evidenced by (a); (b) is evidenced only to the split's *date and ratio*, not its form or record date; (c) would carry the detail but has no canonical id. Binding to any of the three silently chooses a different split or a different document than the row cited. | Does `10-Q Q1-1998` l.468 (or the FY1998 10-K's financial-data footnote) state that the 1998-06-01 2-for-1 was **effected as a stock dividend to holders of record 1998-05-20**? Yes → register the Q1-1998 10-Q and bind row to it. No → the row's mechanism is unsupported and it is the row, not the citation, that must be re-cut. Also: was D-3 actually about the 1999-09-01 2-for-1 (which S30083's 1999-07-21 leg *does* approve)? Then the row's date is wrong. |
| `failures.csv` block row 8 — "1997 (and every year of the stage) | The metric that would answer the stage's central question was never filed", source_id `S3001` | (a) **FY1997 Form 10-K405** (S30005 / S30032 / S30053 / S30072); (b) **FY1998 Form 10-K** (S30009 / S30031 / S30054 / S30073); (c) **S30052**, "Corpus scan of all 80+ archived filings against the 1997 registration lineage" — the only corpus-level registration in the block | The row's own text is a **scope** claim ("no order count, average order value, fill rate or returns rate **in any accession 1997-1999**"). Binding it to (a) or (b) shrinks a corpus-wide null to one filing — a smaller claim with the same confident citation, which is the exact failure mode §14 warns about. (c) keeps the scope but is a scan *against the 1997 registration lineage*, a different question than the unit-metrics null, and the row never cites it. | What corpus was `§P263`'s null computed over? `stage_3_part_3.md` §P263 says "documented null across all Stage-3 filings; §P.2 'Not computed' list". If the assembler means the 80+-filing scan, bind to **S30052** and re-word the row to say which population was searched; if it means the three annual reports only, the row's "any accession" must be narrowed to "no annual report". |

Everything else resolved. Where a bare citation's candidates were separated only by **date impossibility** (a
1997-08-14 10-Q cannot report a June-1998 split; a 1998-03-30 10-K405 cannot report an October-1998 store opening)
that is recorded below as the deciding fact, because it is the row's own text doing the work.

## 4. Binding decisions — bare-id rows (the collision-affected references)

Format: **row → reference → chosen canonical id → deciding phrase in the row**.

### timeline.csv (35 rows, all bound)
1. 1997-11-07 $75m Deutsche Bank term facility → `S3004` → **S30004** — "reported on Form 8-K Item 5" + event date 1997-11-07 (A's S30004 and B's S30040 are one accession; earliest primary taken; C's candidate is a Q2-1998 10-Q).
2. 1997-11 New Castle DC opens → `S3001` → **S30005** — note reads "Form 10-K405 FY1997 l.1646-1648"; an S-8 option plan and a FY1998 10-K do not print that line.
3. 1998-03-05 first annual report ever filed → `S3002` → **S30005** — "a Form 10-K405 for FY1997"; excludes A's 10-Q (June 1997) and C's candidate FY1998 10-K.
4. 1998-04-17 Bookpages/Telebook/IMDB, 540066 shares → `S3018` → **S30006** — event date + U.163's "sources/8-K_event-1998-04-17"; A's S30018 candidate is the Q1-1999 10-Q, filed a year later.
5. 1998-04-24 $275m Senior Discount Notes → `S3021` → **S30021** — "upsized 1998-05-05" matches only "Form 8-K events 1998-04-24 and 1998-05-05".
6. 1998-06-01 2-for-1 split → `S3001` → **S30009** (FY1998 10-K) — the split falls inside the year that filing reports; A's S-8 (1997-06-06) and C's 10-K405 (filed 1998-03-30) pre-date it. *Record date/form leg → see held decisions row 3 and §7.*
7. 1998-06-03 S-4 333-55943 → `S3005` → **S30057** — "S-4 File No. 333-55943" is C's registration; A's S30005 is the FY1997 10-K405.
8. 1998-06-12 S-4 333-56723 → `S3022` → **S30022** — "S-4 File No. 333-56723 filed for the European set"; B's candidate at S3022 is a corpus scan.
9. 1998-08-03 Junglee/PlanetAll plans of merger → `S3023` → **S30023** — S3023 is un-collided (A-only): "Forms 8-K events 1998-08-03 and 1998-08-12 and 1998-08-27".
10. 1998-08-13 424B2 half-year state → `S3009` → **S30039** — "424B2 … filed 1998-08-13"; A's S30009 is the FY1998 10-K, which prints 6.2m accounts, not 3.1m.
11. 1998-10 UK and German stores open → `S3002` → **S30009** — only a filing after October 1998 can report the opening; excludes the 10-Q (Aug 1997) and the 10-K405 (Mar 1998).
12. 1998-10-28 Q3-1998 results, music $14.4m → `S3021` → **S30051** — "Forms 8-K, events 1998-10-28 and 1999-01-05"; A's S30021 is April–May 1998. *The 1998-10-28 8-K's own registration (C's S3007) was held at merge for width and never applied, so this is the only canonical route to it — §7.*
13. 1998-11-19 3-for-1 announced → `S3P-002` → **S30083** — "the last split announcement on any Form 8-K" matches that row's registered passage.
14. 1998-11-17 video store → `S3003` → **S30033** — "more than 60000 titles" survives only in the Q4/FY1998 release (U.162: `sources/8-K_event-1999-01-26 l.306`); A's S30003 is a 1997 lease 10-Q, C's is the April-1998 8-K.
15. 1998-12-31 year-two close, 609996 → `S3002` → **S30009** — "net sales **609996 as filed**" is printed only by the FY1998 10-K; the FY1999 10-K restates to 609819.
16. 1998 (late) B&N/Ingram → `S3002` → **S30009** — U.163/q27 fix the disclosure at `10-K FY1998 l.422 l.797-799` risk factors.
17. 1999-01-04 3-for-1 effected → `S3021` → **S30051** — "reported on Form 8-K for period ended 1999-01-05" is verbatim that row's second event.
18. 1999-01-26 FY1998 results release → `S3003` → **S30033** — "fourth quarter and fiscal 1998 results", ev 1999-01-26 pub 1999-01-27.
19. 1999-02-03 $1.25bn converts closed → `S3019` → **S30019** — event date; alias S30041 (B's Item-5 form of the same accession).
20. 1999-03-30 Auctions launches → `S3010` → **S30020** — "Auctions launches" on 1999-03-30; C's S30061 names it "Auctions launch release" (same accession); A's S30010 candidate is the Q2-1999 10-Q, filed five months later.
21. 1999-04-26 POS AM to 15m → `S3016` → **S30016** — "the 333-55943 shelf" + POS AM; that id's title is the only S-4 registration carrying "POS AM Nos. 1 and 2 and POS AMI".
22. 1999-05-14 Exchange.com/LiveBid → `S3P-001` → **S30082** — "1893944 and 553770 shares issued" = that row's Note 2 l.1695-1760.
23. 1999-05-17 Q1-1999 10-Q filed → `S3018` → **S30018** — the row's date is the filing date of A's S30018 (pub 1999-05-17).
24. 1999-05-19 $2bn S-3 shelf → `S3015` → **S30045** — "File No. 333-78797" is B's S-3 title verbatim.
25. 1999-06-10 Alexa/Accept → `S3024` → **S30024** — "an 8-K event date of 1999-06-08" + 1999-06-09, both in that group's title.
26. late June 1999 Galli named → `S3013` → **S30011** — ARS 1998 (A's candidate, pub 1999-04-07) pre-dates the appointment; B's and C's candidates are both the Q3-1999 10-Q, earliest primary S30011.
27. 1999-07-21 board approves 2-for-1 + seven-DC claim → `S3P-002` → **S30083** — "seven distribution centres, nearly 4 million sq ft" is that row's l.311-317.
28. 1999-08-16 Q2-1999 10-Q, 10.7m accounts → `S3010` → **S30010** — the row's date is A's S30010 publication date (1999-08-16) and the redefinition is in the Q2-1999 10-Q (U.139). *Contrast row 20, where the same bare `S3010` had to be read as the launch 8-K — one citation, two documents, resolved separately.*
29. 1999-08-31 POS AMI description defect → `S3016` → **S30016** — "its own file number is 333-55943"; that id's pub date is 1999-08-31.
30. late September 1999 zShops/Payments/All Products → `S3013` → **S30011** — U.155's claim A cites `sources/10-Q_Q3-1999 l.801-806 filed 1999-11-15`.
31. 1999-09-01 2-for-1 effected, "announced on no Form 8-K" → `S3013` → **S30011** — only a 10-Q whose period closes after the effect date can recite it as effected (row 13: "its only record is a 10-Q recital").
32. 1999-09-30 five DCs + Jenson → `S3013` → **S30011** — "Five new distribution centres opened in nine months" is the Q3-1999 certification (validation row 5's own words: "certified in a periodic report, not claimed in a release").
33. 1999-11 home improvement/tools/software/video games/sothebys → `S3004` → **S30011; S30075 (two ids, citation falsified as written)** — all three candidates for S3004 (8-K 1997-11-07, 8-K Q3-1999 results of 1999-10-27, Q2-1998 10-Q) pre-date November 1999 and cannot carry the list; the row's own `§P248 §P250` name `10-Q Q3-1999 l.795-816` (§P250) and `10-K/99 l.277-278, l.284` (§P248, which is where *sothebys.amazon.com November 1999* is printed). Both documents were therefore bound, not one.
34. 1999-12-31 endpoint close → `S3D-004` → **S30075** — un-collided D key; "net sales 1639839" is the FY1999 10-K.
35. 2000-09-08 10-K/A amendment → `S3P-001` → **S30082** — "Form 10-K/A amends the FY1999 annual report", acc. 0000891020-00-001638.

### failures.csv (7 of 8 applied)
1. 1999 fulfilment ratio → `S3D-004` → **S30075** ("11.5 percent of net sales in 1999" = the FY1999 10-K note, l.1970-1972/l.3097-3102).
2. 1999-07-21 DC count → `S3P-002` → **S30083** (the seven-DC claim text).
3. 1999-06-09/10 in-process R&D → `S3P-001` → **S30082** ($2.8m, "Note 2 l.1719-1725" quoted verbatim in that registration).
4. 1999 marketplace disclaimers → `S3D-004` → **S30075**.
5. 2000-09-08 two audited errors → `S3P-001` → **S30082** ("Note 9 … inadvertently transposed" is the amendment's own statement).
6. 1998-10-26 8-K/A → `S3023` → **S30023** ("with the 8-K/A of 1998-10-26" is in that title and nowhere else).
7. 1999-03-30 auctions revenue minimal → `S3020` → **S30020** — §P249's primary leg is `8-K(1999-03-30)`; the later prints that say "minimal" (Q2/Q3-1999 10-Qs, 10-K/A l.292) are named in §7 as secondary, and none is a candidate for the citation as written.
8. **HELD** — §3.

### validation.csv (7 of 7)
1. 1997-12-31 audited year → `S3001` → **S30005** — decisive: "net sales **147758 as filed**"; the FY1998 10-K (B's candidate) prints 147787 restated, and the S-8 option plan (A's) prints nothing.
2. 1998-06-30 / 08-13 matched repeat pair → `S3009` → **S30039** — "3.1 million cumulative accounts; international **21 percent**" is the 424B2 half-year state; the FY1998 10-K says 6.2m accounts and 20 percent.
3. 1998-11-17 video store → `S3003` → **S30033** (the release that carries the day).
4. 1999-02-03 converts at 2.5× the ask → `S3011` → **S30019** — "closed" on 1999-02-03; A's S30011 candidate is the Q3-1999 10-Q, B's S30041 is the same accession as S30019.
5. 1999-09-30 capacity certified → `S3013` → **S30011** — "certified in a periodic report, not claimed in a release".
6. 1999-12-31 scale → `S3D-004` → **S30075**. 7. 1999-12-31 negative validation → `S3D-004` → **S30075**.

### decisions.csv (4 of 5 applied)
D-1 1997-11 borrow → `S3004` → **S30004** ("$75 million senior secured term facility", event 1997-11-07).
D-2 1998-04 buy local sites → `S3018` → **S30006** (the 1998-04-17 8-K; A's S30018 candidate is the Q1-1999 10-Q).
D-3 **HELD** — §3.
D-4 1999-03-30 open to sellers → `S3020` → **S30020** (only content-compatible candidate; B's is the ARS pair, C's the HistoryLink essay).
D-5 1999-06 Galli → `S3013` → **S30011** (Q3-1999 10-Q; ARS 1998 pre-dates it).

### channels.csv (2 of 2; multi-id cells re-bound in place)
1. Portals/aggregators → `S3001, S3002, S3D-004` → **S30005, S30009, S30075** — the row's own notes name the three documents by line: "10-K405/97 l.2187-2189, 10-K/98 l.2459-2461, 10-K/99 l.3107-3109".
2. zShops → `S3011, S3D-004` → **S30011, S30075** — "placement fees plus sales commissions, levels undisclosed; the company takes no possession" is Q3-1999 10-Q/10-K FY1999 language (U.155, U.160).

### conflicts.csv (16 rows) — legs bound where a filing is identifiable
Bound: U.153 b→S30005;S30013;S30018 · U.154 a→S30009;S30075, b→S30082 · U.155 a→S30011;S30034, b→S30075;S30011 ·
U.156 a→S30082;S30018;S30011 · U.157 a→S30082;S30075, b→S30082 · U.158 b→S30005;S30009;S30075;S30082 ·
U.159 a→S0803;S30005, b→S30009;S30075 · U.160 a→S30075, b→S30082;S30075 · U.161 a→S30005;S30075, b→S30013;S30009 ·
U.162 a→S30033, b→S30075;S30009 (+`[no canonical id]` for `sources/10-Q_Q3-1998`) · U.163 b→S30006;S30056;S30009
(+`[no canonical id]` for `10-Q_Q1-1998`) · U.164 a and b→S30009 (both legs are one accession, MD&A table vs F2
schedule — that is the finding) · U.165 a and b→S30082 · U.166 a→S30030;S30034;S30024 · U.167 a→S0801,
b→S30030;S30009 · U.168 b→S0801. **Left unbound as non-filings:** U.153 a (dossier dating argument), U.156 b
(machine string-count), U.158 a ("register and dossier convention"), U.163 a (a held-row pointer in
`03_quality_control/stage3_register_merge_held_rows.md`), U.166 b (SEC header blocks), U.168 a
(`context_appendices.md`).

### quantitative.csv (47 rows) — `source` prefixed with canonical ids
All 47 bound. Distribution: FY1997 10-K405 **S30005** (14 rows), FY1998 10-K **S30009** (20), FY1999 10-K
**S30075** (24), 10-K/A **S30082** (10), ARS 1997 **S30012** (3), ARS 1998 **S30013** (2), Q1-1999 **S30018**,
Q2-1999 **S30010**, Q3-1999 **S30011** (5 rows between them), 424B2 **S30039**, 8-K groups **S30023 / S30051 /
S30083**, Stage-2 **S0803** (the 1996 working-capital derivation). Deciding evidence is the document phrase plus
line number already in each row (e.g. q15 "ARS 1997 l.210-211, reproduced ARS 1998 l.440" → S30012; S30013;
q37 "Form 10-K FY1999 l.2820 less Form 10-Q Q3-1999 l.314" → S30075; S30011). **q29 carries an explicit
`[no canonical id: Form 10-Q Q1-1998 l.468 is not registered in sources.csv]`.**

### data_gaps.csv (12 rows)
Applied with no id binding: the register has no `source_id` column and `best_available_evidence` cites paths and
section numbers. No ids were invented into it.

## 5. Stage-column normalisation (`§13`: `stage1 · stage2 · stage2-consequence · stage3`)

Before → after, per register (all rows, existing rows edited in the `stage` field only):

| register | before | after |
|---|---|---|
| conflicts.csv | `1`:43 · `2`:70 · `3`:39 | `stage1`:43 · `stage2`:70 · `stage3`:**55** |
| quantitative.csv | `stage1`:94 · `stage2`:82 · `stage2-consequence`:17 · `stage3`:31 · `3`:110 | `stage1`:94 · `stage2`:82 · `stage2-consequence`:17 · `stage3`:**188** (141 existing + 47 new) |
| timeline.csv | `stage1`:49 · `stage2`:67 · `stage2-consequence`:8 · `stage3`:43 · `3`:61 | `stage1`:49 · `stage2`:67 · `stage2-consequence`:8 · `stage3`:**139** (104 + 35) |
| sources.csv | `1`:102 · `2`:12 · `3`:81 | `stage1`:102 · `stage2`:12 · `stage3`:**83** (81 + 2) |
| data_gaps.csv | `stage1`:23 · `stage2`:23 · `stage3`:11 · `3`:31 | `stage1`:23 · `stage2`:23 · `stage3`:**54** (42 + 12) |
| decisions.csv | `stage1`:15 · `stage2`:10 | `stage1`:15 · `stage2`:10 · `stage3`:**4** |
| channels.csv | `stage1`:12 · `stage2`:8 · `stage2-consequence`:3 | same + `stage3`:**2** |
| failures.csv | `stage1`:33 · `stage2`:13 · `3`:8 | `stage1`:33 · `stage2`:13 · `stage3`:**15** (8 + 7) |
| validation.csv | `stage1`:26 · `stage2`:11 · `stage2-consequence`:3 · `3`:12 | `stage1`:26 · `stage2`:11 · `stage2-consequence`:3 · `stage3`:**19** (12 + 7) |

Numeric Stage-1/Stage-2 conversions (permitted by the task, reported): `conflicts.csv` 43 `1`→`stage1` and 70
`2`→`stage2`; `sources.csv` 102 `1`→`stage1` and 12 `2`→`stage2`. No other register carried numeric stage values,
and no `stage2-consequence` row was touched. After this pass **zero** rows in the nine registers carry a stage value
outside the four literals.

## 6. Invariants, as measured

| invariant | measured |
|---|---|
| Stage-1 §U blocks ↔ `conflicts.csv` stage1 rows | **43 ↔ 43** ✓ (blocks U.1–U.43 in `stage_1.md`, no gaps) |
| Stage-2 blocks U.44–U.113 ↔ stage2 rows | **70 ↔ 70** ✓ (across `stage_2_part_1/2/3.md`, no gaps) |
| Stage-3 blocks U.114–U.168 (`stage_3_part_3.md`) ↔ stage3 rows | **55 ↔ 55** ✓ *after* this pass. Before: 55 blocks ↔ 39 rows, **16 missing**, all sixteen accounted for by exactly the pending block (`U.153`–`U.168`) — none was lost, none was duplicated, no §U block lacks a row. |
| Nine registers at uniform width | ✓ conflicts 15/15 rows(168), quantitative 12(381), timeline 11(263), sources 18(197), data_gaps 8(100), decisions 15(29), channels 11(25), failures 11(61), validation 11(59). No ragged row anywhere. |
| `derived_arithmetic` on every DERIVED row | ✓ across all 381 `quantitative.csv` rows: **0** DERIVED-class rows with an empty `derived_arithmetic` (including all 47 new rows); 0 arithmetic strings that fail to recompute; 0 back-solved denominators (test defined in §7). |
| Duplicate `source_id` / `conflict_id` | ✓ none: sources.csv 197 ids / 197 distinct; conflicts.csv 168 / 168 distinct. New rows' source references: **0 dangling** in all six id-bearing registers. |

## 7. Validator proof (the width-check trap that burned this project)

Checks run: (W) csv-parsed field count == header count, separately for the new rows; (Q) **quote discipline** —
every field containing a comma or quote must occupy a quoted span in the raw line, and no field may contain a
newline; (S) stage ∈ the four literals; (C) **column-domain coherence** — in `quantitative.csv`, if the `unit`
column names a currency/volume unit then the `value` column must carry a figure or a recognised null token
(`UNKNOWN`/`EMPTY`/`not computed`/`unquantified`), which is what catches a row whose fields shifted while the count
stayed right; (R) referential integrity of every `source`/`source_id` token against `sources.csv`; (U) id
uniqueness; (D) derived-row population, recomputation of each `a/b=c`, and **denominator traceability** — a
denominator that is not a filed value anywhere in the register but sits within 0.5 % of one is flagged as
back-solved.

Run on a copy of the nine registers (control): 1 failure, and it is **not** one of this pass's rows —
`timeline.csv` line 68 (a pre-existing Stage-2 row) carries a comma-bearing `notes` field whose embedded quotes
make `csv` swallow the commas, so it *parses* at 11 fields and a width-only check passes it. Left in place (the
registers are append-only for existing rows); it is the historical defect class, still live in the file.

Two known defects then planted into separate copies:

* **Plant 1 — unquoted comma shifting fields.** In a new FY1997 cost-of-sales row the metric's quotes were removed
  and `value`+`unit` were merged into one quoted field, so the row still parsed to **12 fields = the header width**:
  a width-only check prints "PASSES (count unchanged)". The validator caught it:
  `FAIL [column-domain] quantitative.csv :: row 337: unit='118945 / 28813,USD thousands' but value=' as filed'
  holds no figure and is not a null token`.
* **Plant 2 — back-solved denominator.** In the gross-margin row, `28813/147758=0.194995` was changed to
  `28813/147786=0.194965`: the quotient **recomputes correctly** and the printed value (19.5 %) still matches, so
  the recomputation check passes. Caught only by traceability:
  `FAIL [derived-traceability] quantitative.csv :: back-solved denominator: ('Gross margin FY1997', 'denominator
  147786 is not a filed value anywhere in quantitative.csv but sits within 0.5% of filed 147787')`.

Both plants are detected and neither check fires on the real registers. The proof also caught a defect in **this
pass's own work**: `failures.csv` and `validation.csv` were first written with the bound id in `evidence_class`
(index 8) instead of `source_id` (index 7) — referential integrity reported 7+7 dangling ids in new rows. The 14
appended rows were rebuilt from the pending text with the correct column and now pass every check; no pre-existing
row was touched by the repair.

## 8. Residual risk — what a later audit must re-check

1. **Pre-existing Stage-3 rows still cite the collided ids.** After the re-key, `S3001`-style tokens resolve to
   nothing: **timeline.csv 105 rows (37 distinct), quantitative.csv 87 rows (15 distinct), failures.csv 8,
   validation.csv 7, channels.csv 2**, plus Stage-2 provisional keys (`S2A-98`, `S2C-20`, …) and 20 `S2P4`
   pointers. Re-binding them is a separate pass over rows this task may not rewrite. Until then any join on
   `source_id` for those rows silently drops them.
2. **Four ids per accession.** The alias sets in §2.2 mean the same document is registered up to four times; a
   later de-duplication must collapse them (and must decide whether to keep the earliest id, as this pass bound to,
   or to rename). `S30077`/`S30083` are now a live two-id/one-accession pair, one of them created by this pass.
3. **Two accessions used by applied rows are not registered at all**: `10-Q Q1-1998` (l.468 split record, l.483
   Bookpages/Telebook shares) and `10-Q Q3-1998` (l.954, l.1408 video-store "plans"), plus `10-Q Q2-1998`'s
   Item-1-only registration S30062 vs S30056. Register them or every row citing them keeps a `[no canonical id]`
   marker instead of a resolvable key.
4. **Conflict-id grammar.** The 39 previously-applied Stage-3 rows carry `P-U.114`–`P-U.152` while the 16 added
   here carry `U.153`–`U.168`. Counts now match the §U blocks (55↔55) but the labels do not share a grammar, and
   re-basing them means rewriting existing rows — refused here under the append-only rule. `stage3_register_merge_held_rows.md`
   ordered exactly this re-basing; it is still owed.
5. **Company-column grammar**: the two new `channels.csv` rows carry `Amazon.com, Inc.` (as emitted) while the
   register's Stage-1/2 spine and the other Stage-3 rows use `Amazon.com`; a `company=` filter splits them.
6. **Judgement calls to re-test against the filings**: (a) timeline row 33 bound to two documents (S30011; S30075)
   whose line ranges were taken from `§P248`/`§P250`, not from a re-read of the 10-Q; (b) q29/timeline row 6 and 31
   assume the 1998-06-01 2-for-1's record date and stock-dividend form are in the FY1998/FY1999 10-K split notes —
   the leg the held D-3 turns on; (c) the 8-K 1998-10-28 is reached only through the grouped S30051; (d) failures
   row 7 binds the "revenue minimal" leg to the launch 8-K because §P249 lists it first, while the word "minimal"
   is in the Q2/Q3-1999 10-Qs; (e) `S30052` (corpus scan) is the natural home of held failures row 8 and of any
   absence claim — no other applied row uses it, which suggests absence rows are being cited to single filings
   elsewhere in the pre-existing Stage-3 set.
7. **`timeline.csv` line 68** — malformed quoting described in §7; it will read cleanly to a naive parser and
   wrongly to a strict one.
