# Audit Sheet — Amazon.com (company_001_amazon) · Stage 1 · Run 2026-07-31
Auditor: Level-3 Chronology Auditor (independent of producer: yes)
Audit: **AUDIT 1 — CHRONOLOGY** (does every statement belong to the period it is placed in, and does the sequence hold?)
Target: `01_companies/company_001_amazon/stage_1.md` (37,730 w) + `context_appendices.md`
Boundary claimed: **1993 idea formation → 1995-12-31**
Primaries used for date verification: original S-1 (acc. 0000891618-97-001309, filed 1997-03-24); S-1/A No. 3 (1997-05-09); S-1/A No. 5 (1997-05-14); FY1997 10-K405 (1998-03-30); Sheff/Playboy (conducted 1999 / pub. 2000); HistoryLink 23230 (2025-04-07); NCSA Mosaic "What's New" (Aug-1995). RDAP / USPTO TSDR / IA-CDX are cited in-text as `retrieved 2026-09-23` (provenance metadata, not subject dates).

| Audit | Result | Items checked | Failures found | Actions taken | Residual risk |
|---|---|---|---|---|---|
| 1 Chronology | **CONDITIONAL FAIL** (single defect: the 1993 start) | full §Q + §B sequence (~45 events), all §P Date↔Source-date pairs, 42 §U conflict entries, boundary bookends | 1 boundary-support failure (start); 1 internal scope contradiction (§Q header); 0 date errors vs primaries; 0 untagged time-travel | start re-dated to 1994 in `Claims cut`; §Q scope defect logged to `Research debt` | low — end boundary and whole interior sequence hold |
| 2 Sources | n/a (not this run) | — | — | — | — |
| 3 Numbers | n/a (not this run) | — | — | — | — |
| 4 Hindsight | n/a (not this run) | — | — | — | — |
| 5 Adversarial | n/a (not this run) | — | — | — | — |

**Headline:** the interior chronology is exceptionally clean — every load-bearing date I could test resolves to the cited document's own date, event and publication dates are held apart throughout §P and §U, and **no later-period fact is presented as Stage-1 state**. The one genuine failure is the **1993 start**, which is not a date at all but a label with no source; it cannot satisfy the "boundary event dated to at least month precision with a source" pass condition. Re-base the start to 1994.

---

## 1. Rebuilt event sequence and date verification (event date vs. cited document's own date)

Sequence rebuilt from §B boundary table + §Q micro-timeline and re-checked line-by-line against the primaries. "Doc" = the earliest on-disk document that actually carries the statement; where Doc ≠ event date the file must (and does) keep them distinct.

| # | Event date | Event | Doc that evidences it | Doc own date | Verified against source |
|---|---|---|---|---|---|
| 1 | 1994-07-05 | Incorporation / "Cadabra, Inc." subscription, 1,700,000 sh / $10,000 | Ex. 10.12 | 1997-03-24 | ✓ lines 348/1272 "FROM JULY 5, 1994"; line 11452 "Cadabra, Inc., a Washington corporation… 1,700,000 shares"; **original only** (COR-02) |
| 2 | 1994-09-25 | `relentless.com` created | Verisign RDAP | retrieved 2026-09-23 | not on disk; date stated; holder flagged unverifiable — OK |
| 3 | 1994-09-15 | 1994 Stock Option Plan adopted; "Board of Directors and the sole stockholder on September 15, 1994" | Ex. 10.22/10.20 | 1997-03-24 | ✓ line 2706 exact string; **original only** |
| 4 | 1994-10 | Kaphan starts, VP Research & Development | Management bio | 1997-03-24 | ✓ lines 2501-2503 "From October 1994 to March 1997… VP of Research and Development" |
| 5 | 1994-10-24 | Kaphan ISO effective (earliest dated equity instrument) | Ex. 10.22/10.20 | 1997-03-24 | ✓ predates all outside money — sequence holds |
| 6 | 1994-11-01 | `amazon.com` created | RDAP | retrieved 2026-09-23 | ~8 mo before any sale — consistent, not a claim of trading |
| 7 | 1994-11 | Seafirst merchant account, personally guaranteed | Certain Transactions | 1997-03-24 | ✓ line 2852 "From November 1994 to December 1996… Seafirst Bank" |
| 8 | 1995-02-09 | First priced outside money, $0.1717 (582,528 sh, Miguel A. Bezos) | Ex. 10.13 / Item 5 ¶2 | 1997-03-24 | ✓ lines 2863/4287 "February 9, 1995"; $0.1717 (line 2864) |
| 9 | 1995-03-31 | S-election ends; Subchapter C elected | Note 1 | 1997-03-24 | ✓ (version-safe; $107,000 cumulative losses) |
| 10 | 1995-04-23 | `relational.com` created | RDAP | retrieved 2026-09-23 | OK |
| 11 | 1995-04 | Company credit cards guaranteed | Certain Transactions | 1997-03-24 | ✓ line 2856 "Since April 1995… company credit cards" |
| 12 | 1995-07 | Sales commence / "commenced offering products… in July 1995"; "no sales… through July 1995" | MD&A + Risk | 1997-03-24 | ✓ lines 1372-1374 exact; line 484/297 "July 1995" |
| 13 | 1995-07 | Wells Fargo bankcard guaranteed | Certain Transactions | 1997-03-24 | ✓ line 2854 "Since July 1995… Wells Fargo" |
| 14 | 1995-07-24 | Gise Family Trust purchase (847,716 sh @ $0.1717) | Ex. 10.14 / Item 5 ¶2 | 1997-03-24 | ✓ lines 2864/4287 "July 24, 1995" |
| 15 | 1995-08-07 | Employee purchase, 42,000 sh @ ≈$0.1287 | Item 5 ¶3 | 1997-03-24 | ✓ lines 4294-4295 |
| 16 | 1995-08-08 | Kaphan Shareholder's Agreement | Ex. 10.15 | 1997-03-24 | ✓ |
| 17 | 1995-10-04 (indexed 1995-10-03) | First press release, ">1M titles, 10–40% off, 50 states/45+ countries in 'first four weeks'" | Company PR | 1995-10-04 | release itself `restoration pending` (§T); **date in-window**; two-date discrepancy correctly routed to U.16 (COR-11.4) |
| 18 | 1995-10-22 | Tallahassee Democrat search test (earliest dated outside press) | via paleofuture | 2019 reprint | event date 1995-10-22, pub 2019 — file keeps them distinct; chain flagged incomplete |
| 19 | 1995-10-23 | "AMAZON" TM application SN 75008413 Cl. 042 | USPTO TSDR | retrieved 2026-09-23 | Reg. No. 2078496 issued 1997-07-15 — file correctly tags registration post-window |
| 20 | 1995-11 | Knight Ridder feature (web/phone/fax, $3.00+$0.95) | via paleofuture | 2019 reprint | event Nov 1995, pub 2019 — distinct, chain incomplete (RD-011) |
| 21 | 1995-11-26 | Alberg Shareholder's Agreement | Ex. 10.16 | 1997-03-24 | ✓ precedes his Dec option grants and June-1996 seat |
| 22 | 1995-12-06 | $1,007,000 / 23-purchaser §4(2) program OPENS | Item 5 ¶4 | 1997-03-24 | ✓ line 4300 "Between December 6, 1995 and May 16, 1996… 23 investors… $1,007,000"; only the pre-12-31 sliver is in-window (COR-10) |
| 23 | 1995-12 | Alberg 150,000 sh @ $0.3333 (= $49,995); ≈2,200 avg daily visits | Certain Transactions; Prospectus Summary | 1997-03-24 | ✓ lines 2872-2873; visits company self-measured |
| 24 | 1995-12-31 | Endpoint snapshot: $511k / GP $102k / op $(304k) / cash $996k / int'l $198k / **11 employees (as of 1996-01-01)** / ≈$17k inventory / $0 LT obligations | Selected Financial Data, Notes, Risk | 1997-03-24 | ✓ lines 666-667 "From January 1, 1996 to December 31, 1996, the Company expanded from 11 to 151 employees"; $511k line 1435; $198k line 3722 |
| 25 | 1996-05-16 | $1,007,000 program CLOSES (post-boundary) | Item 5 ¶4 | 1997-03-24 | ✓ correctly excluded from Stage-1 totals |

**Result — procedure step 1:** 0 date errors. Every dated event matches the cited document's own content; every event date is kept distinct from its publication date. No place conflates the two.

## 2. Time-travel hunt (procedure step 2)

Grepped the whole file for 1996/1997 metrics-as-state, later features, later discounting, "everything store," and untagged retrospection. **0 untagged time-travel instances.** Every candidate is correctly quarantined:

| Time-trap sought | Where it would bite | Handling found |
|---|---|---|
| 2.5M titles / 40% discount as Stage-1 | §A/§E/§G | ✓ 2.5M is a **1997** number (confirmed present in original S-1 lines 1719/2197 **and** No. 5 — both 1997), tagged out-of-stage; 40% featured-title discounting dated **March-1997** (U.18; E.3; appendix "Sequence correction" line 208). Only 10–40% band from the 1995-10-04 release is in-window. |
| "first four weeks" reach as verified demand | §A/§D/§L | ✓ U.1 keeps "July 1995 (High, audited)" and "company's four-week claim (High-that-claimed / Low-that-verified)" apart; §L explicitly: "Anything independent: a company self-report, **not** verified demand." |
| Associates Program (Jul-1996) as Stage-1 | §D/§E/§R | ✓ U.41 re-labels it Stage-2/1996; §E version table and §R Distribution cell both tag `post-boundary`. |
| 1-Click / marketplace / Wish List / reviews-at-scale / Gift Center / MatchMaker | §E/§J | ✓ all dated 1996-97 or listed under "Customer could NOT"; patent US 5,960,411 filed 1997-09-12 tagged out-of-stage. |
| FY1995 $511k / 11 staff / ~2,200 visits as if annual | §P/§R | ✓ "≈5.5 months, not a run-rate"; annualisation explicitly refused. |
| Post-boundary figures in a Stage-1 cell (151/158, 180k, >40%, Ingram 59%, $15.7M, KP $8M) | §A firewall; §L; §P55-63 | ✓ all consequence-column only; firewall lines 52-54 enumerate them. **Lowest-grade residual:** §A line 107 mentions Ingram "59%" inside the year-end-state paragraph but immediately qualifies "on a **1996** basis and the 1995 share undisclosed" — acceptable, not a violation. |
| Founder-state retrospection as contemporaneous | §B/§C/§N | ✓ COR-06 honoured: Sheff (conducted 1999/pub. 2000, confirmed in file header lines 7/19/37) tagged T4-as-1994-evidence; §N states no contemporaneous founder-state interview exists; 10-K405/S-1 use to explain in-window states tagged `RETRO`/`FACT (audited)`. |

**Result — procedure step 2:** PASS. No later-only-true statement is presented as Stage-1 reality.

## 3. Boundary stress test (procedure step 3)

**START (claimed 1993).** FAILS the pass condition. Confirmed against every primary: **no document dates any Amazon-relevant act to 1993.** The S-1's inception line is 1994-07-05 (lines 348/1272); the only 1993-anchored facts are personal (marriage to MacKenzie Tuttle 1993 — HistoryLink line 30) and D. E. Shaw employment (Dec 1990–Jun 1994), neither an act of the entity. The file itself concedes this (boundary table line 73: "**Low** (1993 as an Amazon event); **High** (that no source supports it)"). Does §C need 1993? **No** — §C.1/C.2 rest the origin on the 1994 planning document (rung 3 only, earliest telling LA Times 1997-07-20) and the filed "founded to capitalize on the opportunity for online book retailing." Nothing in the origin narrative depends on 1993. → **Evidence supports starting at the documented mid-1994 window.**

**END (1995-12-31).** HOLDS. (i) The $1,007,000 / 23-purchaser subscriptions straddle 12-31 (window 1995-12-06 → 1996-05-16, line 4300); the file does not treat it as a Stage-1 raise — it isolates the in-window amount as **UNKNOWN** (filings do not disaggregate by date), splits it from CY1995 equity cash ($1,272,000, line 1677) and the $345,525 tranche (whose third leg is 1996-05-03), and reconciles the three objects without averaging (P.2 d7/d8/d22/d23). (ii) The employee count's first documented value is 1996-01-01 ("From January 1, 1996… from 11 to 151," line 666); the file renders it `11 employees (per the filing: at 1996-01-01)` and notes the one-day basis is immaterial to the boundary (COR-03). Both straddle-hazards are correctly handled; the year-end is defensible.

## 4. Sequence integrity (procedure step 4)

Causes precede effects throughout: incorporation (1994-07) → option plan (09-15) → Kaphan hire (Oct) → earliest dated equity instrument (10-24) → amazon.com domain + Seafirst guarantee (Nov 1994) → first priced money (Feb 1995) → Wells Fargo + sales commence (Jul 1995) → TM application (Oct-23) → release (Oct-04) → Alberg paper (Nov-26) → $1,007,000 window opens (Dec-06) → snapshot (Dec-31). The guarantee preceding any sale, and the option preceding all outside money, are both asserted and both correct.

- **"first four weeks" vs "July 1995" (U-listed):** correctly kept as two facts in U.1; the release's "first four weeks" (counting back to ≈early Sept 1995) is not silently reconciled with the audited July-1995 commencement, and **no launch day is computed.** PASS.
- **§L and the company's own PR:** §L does **not** treat PR as independent corroboration — the 1995-10-04 row's "Did NOT demonstrate" column says outright "a company self-report, not verified demand," and the ≈2,200 visits row is labelled "company self-measured." PASS.
- **§Q internal scope contradiction (finding):** the section is headed "CHRONOLOGICAL MICRO-TIMELINE, **1994-07-05 → 1995-12-31**" but its first two rows are dated **1993** (idea formation) and **1994-02** (Matrix News byte/packet charts) — i.e. the header's declared start is contradicted by its own content (and the title §R span likewise reads "1994-07-05 → 1995-12-31" while the file title says 1993). Not a wrong date, but an unresolved scope mismatch between the section label and the rows it prints.

## 5. §P and §U date-vs-source-date audit (procedure step 5)

- **§P (P01–P65) `Date` vs `Source date`:** all internally consistent — `Date` is the event (1994-07-05, 1995-12-06→1996-05-16, etc.), `Source date` is the filing's own date (1997-03-24 / 1997-05-14 / 1998-03-30). Straddling rows (P51/P64) carry both endpoint dates; post-boundary rows (P55–P62) are fenced off. No conflation.
- **§U (U.1–U.42):** every entry's event dates resolve to the primary. Spot-checked and confirmed: U.1 July-1995 (lines 1372-1374); U.8 Item 5 ¶2/¶3/¶4 (Feb-9/Jul-24/May-3 1996; Aug-7-1995; Dec-6-1995→May-16-1996); U.15 Delaware execution 1996-05-28 vs effective 1996-06-18 (lines 3813/4307) correctly called "not a contradiction, post-boundary"; U.17 "11" as-of 1996-01-01; U.21 printer's `[PICTURES …]` caption (line 1987) with `PUBLIC DOCUMENT COUNT: 38` (line 32) and its absence from No. 5. **No event/publication conflation in any of the 42.** The minor-dating list (line 1870-1876) correctly collects the indexed-vs-datelined release, "23 investors" vs "23 purchasers," "Amendment No. 4" vs No. 3, Brandt 2011-not-1999, and HistoryLink 2025-not-1999.

---

## Claims cut or downgraded

| Claim ref | Was | Now | Why | Evidence applied |
|---|---|---|---|---|
| Title / §B boundary / §R header | "STAGE 1 (**1993** idea formation) → 1995-12-31" | "STAGE 1 (**1994**, mid-year ideation → **founding instrument 1994-07-05**) → 1995-12-31"; 1993 moved out of the operative boundary | 1993 cannot satisfy "boundary event dated to ≥ month precision **with a source**"; no document dates any Amazon act to 1993 (it is the only boundary event with no source) | original S-1 inception line "FROM JULY 5, 1994" (lines 348/1272); file's own line 73 (Low, no source) |
| §C.2 / §Q "91-page roadmap / business plan" | (already rung-3 only) | confirm: no artifact, and **zero** hits for "roadmap"/"business plan"/"2,300"/"shipped our first book" in original S-1 **and** 10-K405 | chronology: nothing here supplies a 1993 or 1994-dated origin document | full-text nulls confirmed in `sources/` |
| §A year-end-state paragraph | "one distributor at 59% of purchases" | keep, with the existing inline "on a **1996** basis" tag made mandatory (must not be lifted into any Stage-1 state cell) | prevents a 1996 figure reading as a 1995-12-31 attribute | 10-K405 lines 388/1670 (58%/59% = 1996/1997) |

## Research debt opened by this audit

| RD id | Section | Debt | Assigned | Status |
|---|---|---|---|---|
| RD-020 | §Q / §R / title | Re-dated start applied: re-head §Q and §R and the file title to the 1994 window (first hard anchor 1994-07-05; earliest origin = spring-1994 ideation, tagged `RETRO`), and move the "1993" line in §Q from a dated row to an explicitly-unsourced pre-window tag or to §S | Chronology auditor → Company Lead | OPEN |
| RD-021 | §Q | Resolve the header/content scope mismatch: the "1994-07-05 → 1995-12-31" micro-timeline prints 1993 and 1994-02 rows above its own start | Company Lead | OPEN |
| RD-022 | §B.1 / §U.26 | Pin the CEO title to the **Management-section bio** only (lines 2431-2433, "CEO since May 1996"). The original S-1's prospectus summary (line 766) and officers table (line 2404) call Bezos "Chief Executive Officer" as an undated present-title descriptor — must never be cited as 1994 status | Company Lead | OPEN (low) |
| RD-023 | §P / §U (RDAP/TSDR/IA) | Keep `retrieved 2026-09-23` stamps quarantined as provenance metadata distinct from both event and publication dates (already done; flagged so no future pass collapses them) | Evidence Registrar | MONITOR |

## Sign-off
Stage status: RECONSTRUCTION → ADVERSARIAL REVIEW → QA → COMPLETE.
**AUDIT 1 verdict: CONDITIONAL FAIL.** Interior chronology passes all three sub-tests (0 date errors vs primaries; 0 untagged time-travel; sequence holds). The single blocking defect is the **1993 start**, which fails "every boundary event dated to at least month precision with a source." Re-dating the start to 1994 (RD-020/021) converts this to a full **PASS**; the 1995-12-31 end and every §P/§U date pair stand as-is. Per §11 the start is re-based, not disclaimed.
