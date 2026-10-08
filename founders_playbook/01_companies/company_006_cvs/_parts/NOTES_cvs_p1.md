# NOTES — company_006_cvs, Stage 1, part 1 (`_parts/s1_p1.md`)

Author: `s1-cvs-p1` · written 2026-10-06 · claim: `scaffold.py claim --path …/_parts/s1_p1.md --agent s1-cvs-p1
--sections "Header,boundary,A..U,registers"` (all four sections stamped WRITTEN) · gate:
`03_quality_control/cvs_s1_gates_p1.md`.

## 1. Scope carried from the probe (not re-tiered)

`research/A_chronology_feasibility.md` is the scope document. Carried verbatim: **per-stage tiers S1a/S1b/S1c = T3
register, S1d = T2 core, whole dispatched window 1963-01-01→1996-12-31 = T2 core (2 of 5 families)**; the five-family
verdict; the "counting the `corporate_print` shelf as family (d)" refusal; the R-1…R-5 route list; the refusal to write
the shoe store. `research/A4_harvest_mine.md` was read **immediately before use** and re-checked against
`sources/harvest_mine/_index.json`, which at close reads **candidates 70 / mined 12 / untried_by_limit 57** — the A4
dossier and the index agree; the probe's own earlier 36/6/29 and 68/12/55 are stale states of a live lane, reported in
§U.10 rather than hidden.

## 2. The corpus moved under this pass (§14 r11) — re-enumerated before writing

The probe left `sources/sec/` at 10 `.txt`. At this author's first measurement it was **36 `.txt` + 36 sidecars**: the
fleet had run the **forward recital pass (R-1)** at 17:42–17:43 — `sources/sec/_RUN.json`, `window
1997-01-01..2006-12-31`, `stored 28`, `attempted 128`, `skipped 97`, `unanswered 3`, `bytes 6,980,278`,
`identity_ok **false**` with 6 `duplicate_slots`. The pre-existing in-window record survives as
`_RUN.prev-20261006T121331Z.json` / `_MANIFEST.prev-20261006T121331Z.csv`. Decomposition proved at §T.1:
**7 (in-window pass 1) + 28 (forward pass) + 1 (the probe's 8-B12B grab, in neither manifest) = 36**.
Periodical side: **14** `.txt` in `sources/periodicals/` + **4** in `sources/corporate_print/` = 18 files,
**16 unique documents** after md5 (2 cross-shelf duplicates). `sources/` total files: **126**.

Consequence: **R-1 is CLOSED** and its yield is measured (below), so §S.1 no longer asks for it, and every count in the
probe that said "7 stored files" or "10 stored files" is superseded in this part.

## 3. What R-1 changed, and what it did not

* It **did not** add a second witness to 1963. Measured over all 36 files: `Founded in 19XX` = **4 hits total** —
  `Founded in 1963` × **3 files of one lineage** (S-4 1997-03-28, S-4/A 1997-04-17, DEF 14A 1997-04-23 — identical
  sentence) + `Pharmacare, founded in 1994` × 1 (FY1996 10-K405 L469). `Consumer Value` **0**, `Jacksonville` **0**,
  `Newport` **0**, `Kandel` **0**, `Lowell` **0**, `first store` **0**. `Riverside` = 8 hits, **all addresses**
  (`Two CVS Riverside Plaza`, `2 North Riverside Plaza`, S-4 L13072/L13080, plus S-3/SC 13D/8-K address blocks).
  One new `1963` appeared (DEF 14A 2001-03-15 L436) and it is a **director's employment history** — recorded as the
  standing decoy **U.06**.
* It **did** supply the legs the dossier needed: the FY1996 10-K405 subsidiary stack (CVS New York → CVS Center (NH) →
  CVS Pharmacy (RI, *"formerly known as CVS, Inc."* → **U.09 resolved**) + CVS H.C. (MN) → Nashua Hollis (NH) → ~1,145
  subsidiaries, plus Melville Realty Company), the estate metrics (1,408 stores, $2.4 bn pharmacy / $3.1 bn front,
  43.9/56.1, ~1,200 scripts/week, $573/sq ft), Pharmacare's >1 m managed lives, the EIN change 04-1611460 →
  05-0494040 (**U.07**), and the fact that **`Caremark` occurs 0 times in all 36 files** while `insurance` in-window is
  only self-insurance for liabilities.

## 4. Corrections this part issues against the probe (all byte-verified, none re-tiering)

1. **§U.10 — the naming lineage is older and longer than the probe recorded.** Probe §9.4/§10.1: *Consumer Value
   Stores* = 4 in-window press rows, all 1990-1994. Measured with OCR line-break-hyphen healing and
   nearest-preceding-masthead issue dating: **6 rows across 5 unique documents — 1980-01-21, 1983-11-14, 1990-04-09,
   1991-05-06, 1993-04-26, 1994-04-25**. The probe missed the 1980 row's prose context and the 1983 row entirely
   because the name is broken as `Con-`/`sumer Value Stores (CVS)` (DSN-8384 L1788-1789, WOONSOCKET dateline, headline
   `CVS weighs warehouse growth in three regions`). Raw-string searching is the defect; the fix is in the tool, not
   the corpus.
2. **`Consumer Value Stores` was never promoted by the mine.** `named_terms` is `[]` on **all 12** mined items; the
   promotions are `cvs sales` / `cvs stores` identity-word hits. So the naming rows are **found by reading, not
   stamped by the tool** — a coverage warning for the merge (and proof that a `TIER1_CANDIDATE_TEXT` label tracks
   nothing relevant here).
3. **Issue dating beats scan-year metadata.** DSN layers carry dated mastheads in bulk (e.g. `DSN-7980` = 115
   mastheads, 1979-10-29→1980-10-13; `DSN-88` = 220, 1987-11-09→1988-10-24; `DSN-9091` = 179, 1990-11-05→1991-10-28).
   Every periodical row in §Q/§P is dated by the **nearest preceding masthead in the same file**, not by the item's
   `meta_date`. Recorded so the merge does not re-import the metadata years as issue dates.
4. **Probe §5's S1b reasoning is refined, not reversed.** The oldest held press bytes now reach **1979-10-29**, but the
   1979-dated run (16 mastheads, lines 365–5906 of `DSN-7980`) carries **0 `CVS`-bearing lines** — measured. So S1b
   remains empty for naming purposes and stays T3.

## 5. Five families as this author found them (per stage, never globally)

| Family | Verdict | Measured basis at close |
|---|---|---|
| (a) SEC / EDGAR | **TRIED–ANSWERED** (identity, S1d; and S1a **by recital only**) | 36 `.txt` + 36 sidecars; 2,968 indexed rows, floor 1994-02-10, 0 rows before 1994-01-01; `Founded in 1963` in one lineage; `1963` in the FY1996 10-K405 = 0 |
| (b) Web archives | **UNTRIED — 0 calls** | no `sources/web_archive/` shelf, no CDX artefact; `tools/cdx_intake.py` exists on the shelf and was never run for CIK 64803 |
| (c) Periodical corpora | **TRIED–ANSWERED**, in part; **TRIED–UNANSWERED** for Chronicling America; **57 candidates UNTRIED** at the limit | 16 unique docs; naming 1980→1994; `1963` decoys measured; 2 index-shelf `NULL`s are structural |
| (d) Digitised corporate print | **TRIED–UNANSWERED (year-faceted)** and **ZERO BYTES** | the 4-file shelf is Internet Archive serial layers (`family: internet_archive` in the mine index, `route= … _djvu.txt` in every sidecar), 2 of them md5-duplicates of periodicals copies. **Not counted as a family** — §U.08 |
| (e) Auction / museum / manuscript | **UNTRIED — 0 calls, and no query block exists for `cvs`** | no shelf, no `tools/queries.json` task; recorded as the missing ask, not as a null |

**Families that counted: 2 (a, c) for the dispatched window ⇒ T2 core carried; S1a/S1b/S1c remain T3.**

## 6. `## Untried` (as written for the merge, §S rows 6–10)

1. Family **(b)** CDX for `cvs.com` / `melville.com`, 1996–2001 (cannot reach 1963–1979 by construction).
2. Family **(e)** auction/museum/manuscript — never queried, and **no query block exists** for this company.
3. **57 periodical candidates** untried at the `--limit` cut (DSN/JAPHA/*Pharmacy Times* layers; note that the
   candidate set as harvested contains **nothing before 1980** except four out-of-window textbooks shelved
   `LEAD_ONLY`, so the press route *as queried* cannot reach 1963–1979).
4. Family **(d) facet-free** — both corporate-print queries still carry `year_range [1960,1998]` (RD-130).
5. Chronicling America **re-run with the corrected endpoint** under the right string `andtext:"Consumer Value Stores"`
   and **no state facet** (the existing rows searched `Consumer Drug Stores`, a string no carrier in this repo uses).
6. EDGAR **Oct–Dec 1996 8-K/8-K/A rows** for CIK 64803 (the succession's Effective Time), and **1990–1993** accessions
   (the FY1989–FY1992 comparators for §U.04/§U.05) — all reachable with add-only `sec_intake.py grab`.
7. RI / MA **incorporation registry** lookups for a 1963 corporation named *Consumer Value Stores* — never attempted by
   any pass in this company directory.

## 7. `FETCH REQUEST:` status for this part

No new FETCH REQUEST is emitted. Inherited: **R-1 CLOSED** (run by the fleet 2026-10-06 17:42, yield measured above);
**R-2 CLOSED** (probe); **R-3, R-4, R-5 OPEN** and re-asked as §S.1/§S.4/§S.7 follow-ups. This author ran **0 network
calls** and **0 intake/harvest commands** — `sec_intake.py auto` was refused again for the same reason the probe gave
(it rewrites `_RUN.json`/`_MANIFEST.csv` through an unconditional `open(path,"w")`), and the harvest lanes are owned
by the fleet. Everything measured here is a read over held bytes.

## 8. Refusals (what this part will not say)

* **No shoe store.** The folk origin (1963 shoe store; *Consumer Value Stores* as the 1963 entity; Jacksonville; the
  Riverside–Newport naming) is written **UNKNOWN with the named route** (§U.02, claim record **CVS-A20**). A dispatch
  brief is not a carrier.
* **No 1996 IPO.** `S-1`/`S-1/A`/`SB-2`/`10-A` = 0 of 2,968; `8-B12B` = 1. Called a
  reincorporation-and-rename with a §12(b) successor registration; "was equity separately floated in 1996" left
  UNKNOWN with importance High (§S.5, **U.03**).
* **No founder, therefore no founder class.** `FOUNDER CLAIM` is not used for 1963 anywhere: no founder exists in the
  record (**U.01/B.1**). The 1963 year is `COMPANY CLAIM (RETROSPECTIVE)`, Medium, one lineage.
* **No insurance or Caremark leg in Stage 1.** No underwriter is named in any held byte; `Caremark` = 0 occurrences;
  `CVS/CAREMARK CORP` is EDGAR **metadata**, cited as such only.
* **No periodical citation at High.** All 18 sidecars say `transport = UNVERIFIED TLS`; every press value is Medium.
* **No index label as a source.** `TIER1_CANDIDATE*`, `classification`, tier stamps and `former_names` are pointers.
* **No counting of the `corporate_print` shelf as family (d)** — §U.08, and the reason this project keeps catching it.
* **Entity adjacency required** for every `CVS` row; the medical-abbreviation and rival-founding decoys are enumerated
  in §T.6 so a later pass cannot re-import them as hits.
* **Nothing was renamed, moved, pruned or "fixed"** in `sources/`, `_index`, the manifests or `_FLEET_INTAKE.tsv`
  (§14 r4). The three drift defects are reported in §T.5 and `data_gaps.csv` S.10.

## 9. Numbers re-measured after the last write

Words on disk **22,951** total; **18,295** outside the fenced register blocks. Headings: 4 scaffold-claimed sections
(all stamped WRITTEN by `scaffold.py section`) + **21 narrative sections §A–§U**, each carrying its own
`STATUS: WRITTEN 2026-10-06` (7 chunk-level markers, one per written group, plus the 4 claimed), + `## CLAIM RECORDS` +
`## registers`. `STATUS: PENDING` remaining: **0**. Fence pairs:
**9** (one per register, header rows byte-identical to `company_001_amazon`'s nine registers — column widths verified at
12/11/18/15/8/15/11/11/11). Claim records: **20** (CVS-A01…A20; A20 is the standing non-claim and is bolded in-file,
so a plain `^CVS-A\d\d Claim` regex counts 19). Register rows: quantitative **29**, timeline **24**, sources **18**,
conflicts **10**, data_gaps **10**, decisions **14**, validation **8**, failures **7**, channels **6** = **126**.
Anchors declared `U.01–U.10` (in-file `<!-- ANCHORS: U.01-U.10 -->`), and the gate read **10 declared anchors**; 10 §U
headings, 1:1 with the 10 `conflicts.csv` rows.
Gate at final bytes: `03_quality_control/cvs_s1_gates_p1.md` — **1 finding, coverage-only** ("no register CSVs at root
or research/ — csv/anchors gates DID NOT RUN"), which is the **expected pre-merge state** and is not a defect; notes
include `keys _parts/s1_p1.md cites 1 hyphenated record keys: S3-97` (a §T.1 document label, not a source id) and
`corrections no CORRECTIONS.md — gate DID NOT RUN`. Tier read by the gate: **T2** ✓ (matches the probe's
whole-window verdict).
**Budget: closed out at 82 of 130 tool calls.**

## 10. For the merge / next agent

* **Do not count** `sources/corporate_print/` as family (d); its bytes are family (c) (md5-proved, §U.08).
* **Lineage:** S-4 + S-4/A + merger DEF 14A = **one** source for `Founded in 1963`; the FY1996 10-K405 is a **second**
  document that prints **zero** 1963s — do not let a count of "three files say 1963" become "three sources".
* `sources/sec/0000950103-96-001174.txt` (the 8-B12B) is **in neither manifest**; anything counting stored SEC docs
  from `_RUN.json` alone under-counts by 1 and misses the succession instrument entirely.
* `_FLEET_INTAKE.tsv` cvs row is **stale** (`pass2_status` empty) — re-key by window; do not re-run intake to fix it.
* **§B.3's fifteen legal persons** are the working set for any later genealogy claim; the 1963 question is a §U.01
  conflict, and the only route that can name a 1963 person is a **registry** or **newspaper** answer, not more EDGAR.
* Word budget: the raw token count of this part (22,951) exceeds the T2 22k/level figure mainly because of the
  126 register rows; narrative alone is 18.3k. §9.2's 60k hard cap is respected with wide margin. Measure the tier cap
  **after merge**, on the assembled volume, not on a part.

## 11. What this part did NOT examine

I did not read the FY1997–FY2001 financial statements, exhibit 13, or the 1999 S-4/A series beyond the term censuses
reported in §T.1/§T.3 (they are post-window and were used only for the EIN/identity census and the Pharmacare/Caremark
absences); I did not open the Revco SC 13D (`D97`), the Linens 'n Things SC 13G (`G97`), the 2001 8-Ks, or the
`0000315066-00-000956` SC 13G/A beyond header/EIN extraction; I did not read the six JAPHA/*Pharmacy Times* index
volumes as anything but `NULL`-by-construction; I did not examine `02_cross_company/`, `MASTER_RESEARCH_LOG.md`, or
any sibling company beyond `company_001_amazon` **for format only** (no Amazon value, date or phrasing was imported);
I did not query EDGAR, archive.org, Chronicling America, HathiTrust or Google Books; I did not read
`tools/queries.json` beyond the cvs family list and the year facets quoted in §Boundary; and I did not audit
another agent's gate output.
