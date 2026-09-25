# FORENSIC LONGITUDINAL DATASET — WAL-MART STORES, INC., STAGE 1 — MERGED VOLUME 2 (continuing)
## `UNTRIED ROUTES, CARRIED FORWARD`, the CLAIM-RECORD APPENDIX (§§M–U), and part 3's register-row handoff block

**This is the second volume of one document** (method §9.3). It continues `stage_1.md` at the section boundary
between §U.4 and the carried-forward UNTRIED list; nothing is renumbered — the anchors U.001–U.048, U.101–U.116
and U.201–U.222, and the §A–§U section letters, are the same spine the first volume prints, and the canonical
mapping table is §U.0.1 **in volume 1**. Every route and record below is registered: the U.2xx rows land in
`data_gaps.csv` (transcribed at merge so each anchor has a register row) and the claim records are the
`claim_ref` targets for §M–§U. The `>>> REGISTER ROWS FOR MERGE <<<` block at the end is the part-3 handoff,
kept verbatim as the merge's audit trail; it is not live register content.
*(Added by the merge pass, 2026-09-26.)*

---

## UNTRIED ROUTES, CARRIED FORWARD

STATUS: WRITTEN 2026-09-26

**§14 rule 6 requires a probe to name the routes it never tried, and §15.1 requires that no agent brief spend
its budget fetching what a script or another agent can reach.** Per the latter, the six items below marked
**FETCH REQUEST** are recorded **as named routes, not chased**: a mining agent is working several of them
during this pass, and their results will arrive as merge requests rather than as edits to this file. Nothing in
this section is a null; **each row states the exact query, the document that would settle it, and the anchor
that owns it.**

### 1. Routes handed back as FETCH REQUESTs (in flight — do not re-issue)

```
FETCH REQUEST: SEC issuer/list registers for 1972-1979 — "Securities traded on exchanges" 1978 edition and the
1979NO1 "Official list of section 13(f) securities" (both in the HathiTrust hit set, rights-proven pd, text
walled at /cgi/pt and /cgi/imgsrv/html). Owner anchor: U.201 (with U.044, U.207). Settles: whether the company
is positively named by a third-party government register after the 1972-08-25 NYSE listing — the one test that
could turn a negative corroboration into a positive one. Route: browser session or an Internet-Archive binding
under those exact series terms (A5 searched neither). A5's dossier-local key: X-A5/2.
```

```
FETCH REQUEST / FILE MINE: on-disk but never mined — sources/periodicals/ia_arkgaz.json, ia_satpost.json,
ia_supermerch.json, ca_01_waltons_five.json, gb_01_waltons_five_and_dime.json. Owner anchor: U.202 (with
U.101, U.110). Settles: the ONLY on-disk route to a 1945-1962 named witness. Constraint recorded in A6's
census: three of the retrieved JSON families are error or challenge bodies and are therefore UNANSWERED, not
null. A4's own perimeter note: the 18 unspent requests were withheld in the belief these hosts were dead;
U.043 records that the belief was partly wrong.
```

```
FETCH REQUEST (LOCAL, no web budget): EDGAR former-name and state-of-incorporation search against
sources/probe_SEC_tickers.json, sources/EDGAR_submissions_CIK0000104169.json and
..._002_1994-2012.json — the `formerNames` field is present and holds ["Walmart Inc.", "WAL MART STORES INC"].
Owner anchor: U.203 (with U.013, U.014). Settles: the shortest remaining path to the state-of-incorporation
defect retracted at part 1 §D-R03c. Note recorded by the held-corpus census: the three
probe_EDGAR_submissions_00*.json files are S3 `NoSuchKey` error bodies = UNANSWERED, not empty.
```

```
FETCH REQUEST (LOCAL): FY1976 origin-wording re-walk — sources/periodicals/WALMART_AR_1976.txt, the partially
OCR'd "Company's first unit … a franchise Ben Franklin … in 1945, his brother …" (A2 W-50). Owner anchor:
U.204 (with U.045, U.110). Settles: the earliest statement of the fifteen-store count and the 1945/1946 label
drift, and whether that report names the brother.
```

```
FETCH REQUEST: FY1975 page-image digit test — the declared but unretrieved `_text.pdf` (3,706,555 B) and
`_djvu.xml` page map (448,062 B) of the FY1975 report, registered as S0111 (LEAD / UNTRIED, "the highest-value
untried item in the dossier; it is cheap and needs one fetch"). Owner anchor: U.205 (with U.016, U.017,
U.018, U.026, U.047). Settles: the $226,209 / $236,209 top line, the FY1970 net-income cell, the FY1973 share
count, the refuted FY1980 dividend row and the FY1973 misprint — five live conflicts on one page walk.
Sibling act: the FY1974 / FY1977 / FY1978 / FY1979 page images (U.206).
```

```
FETCH REQUEST: the 1972-1979 SEC registers above PLUS the FY1976 / FY1977 / FY1978 quarterly market-price and
dividend tables and the FY1974-FY1978 lease-commitment notes. Owner anchor: U.217 (with U.106, U.116).
Settles: whether "leases as the recurring exposure" has interior holes, and the earliest price series.
```

### 2. Routes that are UNTRIED because they are outside this machine's reach (named, not chased)

| Anchor | Route | Exact query or act | What it would settle |
|---|---|---|---|
| U.206 | page images, four reports | FY1974/77/78/79 `_text.pdf` + `_djvu.xml`, declared in each file's own IA metadata | U.017, U.018, U.026, U.047, FY1975's balance sheet, FY1976's employee chart |
| U.207 | HathiTrust **page text** | `/cgi/pt?id=hvd.hl4rdm` → 403 (5,303 B); `/cgi/imgsrv/html` → 403 "Blocked from HathiTrust" (66,873 B). Search and catalog API answer. **Trap registered:** `/cgi/ls` silently drops unknown restriction parameters and returns corpus-wide counts (94,222 / 13,526) — a count off such a URL indicts the request, not the corpus | whether any of the 573 full-view 1970s records — **52 of the first 100 being SEC serials** — prints the name |
| U.208 | NLRB and FAA registers | NLRB *Court decisions relating to the NLRA* v.26 (1973-74) and *Decisions and orders* v.201 (1973); FAA *civil aircraft register* editions 1971-1978, all full-view `pd`, ranked top on a narrow name+home-town query | **the most probable positive-naming document class this project has located** — and the purest lineage (§14.6), because nothing in an adjudicated proceeding is registrant-supplied |
| U.209 | SEC *Directory of companies filing annual reports* 1970/1971/1972 | rights-proven Full view in the catalog; IA holds none (E-A5/4) | a positive **registration** naming, which the 1970 issuer register structurally cannot give |
| U.210 | 1970 registration statement | EDGAR full-text (never queried by any pass) + SEC Reference Room / National Archives paper request | the only accession-numbered, dated filing for the IPO years: gross price, underwriter, use of proceeds (U.031) |
| U.211 | Arkansas SoS + county records | entity index (Wal-Mart, Inc.; Walton Enterprises, Inc.; the subsidiaries); **Benton County** deeds (Bentonville) and **Mississippi County** deeds (Newport) | U.013, U.014, the 1950 lease cluster, the "15 March 1962" lore, the franchise terms |
| U.212 | *Stores* monthlies + NRDGA/NRMA roster | a **designed sample of ~10** roster-bearing issues (convention and membership numbers), 2 requests each; plus "membership roster / chain directory" as a title class | whether the trade's silence (U.111) is genre or fact |
| U.213 | the sector's own counting instruments | *Chain Store Age* "Directory of Chain Stores" 1963-1970; *Discount Store News*; *Discount Merchandising*; D&B discount volumes (BW indexes one at p.79, Nov.9 1963); AUDITS & Surveys; the **Cornell discount-chain study the company itself cites in FY1973** (S0102 W-38, never located); Hoover's firm reports | **A3 §7.2(d)'s named missing witness: a non-company contemporaneous count of Wal-Mart's stores or sales for FY1964-FY1970.** Until one exists the depth verdict stays `PROVISIONAL` |
| U.214 | the 1962 advertisement image | read the catalogued "First Walmart Advertisement" (asset year 1962; A2 W-77 records the image path and states it has **never been read**) | whether any in-period **price** survives — the closest thing to a 1962 primary in existence |
| U.215 | held harvest bodies that no Stage-1 dossier had read | `00_universe/harvest/corporate_print/` (four walmart bodies + the 27-item FY1972-FY1998 run list + a 23,989 B direct-server pull of the FY1972 text layer); `00_universe/harvest/internet_archive/` (8 queries on `walton` / `Walton's` / `five-and-dime` / `$1.25 store`, 1945-1965); `.../chronicling_america/` (5 queries × 3 rounds, **all HTTP 403 = UNANSWERED, never EMPTY**) | A6's census calls the corporate_print bodies "the two strongest pre-1972 naming nulls in the corpus" — **cited here as in-flight; its own merge sections were still unwritten when this volume was drafted (§14 rule 11: a late-arriving primary is evidence FOR the pass that reads it)** |
| U.216 | refused endpoints | Wayback `matchType=prefix` (**HTTP 504**, an upstream capacity failure); December 1970 SEC bulletin (**HTTP 500**, one attempt, retryable at 1 request); Google Books keyed v1 `dateRestrict` (429 keyless; the feeds endpoint **ignores** `as_ylo/as_yhi` and returned only 1992-2013 and 2000-2023 volumes); Federal Register pre-1994 (its `term` index is 1994+, so its `count: 0` is not a null); **and the 1970-08-27 / 1970-09-03 first-trade cluster**, which no document on disk dates | `U-A5/2…5`, `X-A5/5`, part 1 §A.2 item (b); the boundary's rejected rival |
| U.217 | local report interiors | FY1979/FY1980 Management's Analysis comparable-store sentences; FY1974/75/77/78 lease-commitment notes; FY1977-79 price/dividend tables | U.107's second data point; the lease estate's continuity |
| U.218 | government and chamber tabulations | **Census of Business 1963 / 1967** for AR/MO/OK/KS/TX (`1967censusofbusi674uns` in-set; layers are 6.6 MB of text / 2.69 GB per item ⇒ **extract-only, never dumped**); `hf-5465.-u-55-g-7` Greensboro trade-area study (metadata read, `_djvu.txt` present, deliberately not pulled — North Carolina, outside the four-state area); duplicate BW index bindings as an OCR control | a **government** bound on the company's retail environment that does not ask the company |
| U.219 | the 1992 memoir as a text | bytes not in this repository | nothing admissible: it would remain **FOUNDER CLAIM / retrospective memory**, and the "$1,402", the lease-loss motive and the 1962 "discovery" story stay **UNTRACEABLE in the Stage-1 record**, which is a different sentence from "false" |
| U.220 | FY1981-FY1998 corporate print | the rest of the contiguous IA run | outside Stage 1; recorded so the run's remaining gap stays visible |
| U.221 | **auction / museum documentary family** | §14 rule 6's fourth family, **never properly tried for this company** (the Apple contrast is explicit in the method file). `STUB_LEAD_samwaltoninsides00vanc.md`, `STUB_LEAD_DTIC_ADA345567.md`, the five `*.bin` probes, `ia_anywalmart.json`, `ia_chain_store_age.json`, `ca_01_probe.json`, `GOOGLEBOOKS_batch1.json` are enumerated and unmined | founding documents at sale. **This is the largest single untried act left in Stage 1 and the reason the company-level verdict cannot be lifted to core on document-count arguments alone** |
| U.222 | the genre control | read a **non-Walmart** 1950s-60s printed annual report (a regional chain of comparable size) and ask whether the genre ever states a founding rationale | whether §C.1's central silence — "the single most consequential silence in Stage 1" — is a property of the **record** or of the **form**. This is the only test available, and it does not require Walmart at all |

### 3. What is NOT on this list

No route is dropped by exhaustion or by budget: **web budget for this volume was 0 and none was spent**, so
nothing here was closed for cost reasons. The three UNANSWERED endpoint families (HathiTrust page text,
Chronicling America, Google Books v1) are recorded at **U.207 / U.216** and are **statements about this
environment, not about the past**. The 504 and the 500 are **unanswered**, not empty. Where a route was
deliberately not walked so that the register could be written instead, A3's own words are inherited: *the
marginal source is worth less than the unwritten file* (§14 rule 2).

---

## CLAIM RECORDS APPENDIX — part 3 (§§M–U)

STATUS: WRITTEN 2026-09-26

*Claim IDs continue the volume's letter scheme: `M01…`, `N01…`, `P01…`, `Q01…`, `R01…`, `S01…`, `T01…`,
`U01…`. Records for §§A–D are in `s1_p1.md`; for §§E–L in `s1_p2.md`. Verbatim passages are ≤ 40 words and are
transcribed from the files on disk; where no passage was taken, the field reads
`NO_VERBATIM_PASSAGE_RECORDED` rather than paraphrasing a quote.*

```
M01 Claim: No document of any kind in the Walmart Stage-1 corpus names the company before 1972-03-22. — Date:
1945-01-01→1972-03-21 — Source: negative enumeration across nine printed annual reports, 13 Business Week
index volumes, 8 Stores apparatuses, 2 SEC government documents, EDGAR and web archives — Source date:
2026-09-26 — URL: founders_playbook/01_companies/company_002_walmart/sources/ (all families) — Archived: on
disk — Tier: 1 — Class: FACT (of absence, within a stated perimeter) — Passage: NO_VERBATIM_PASSAGE_RECORDED —
Conf: High — Corroboration: 0 (an absence is not corroborated, it is measured) — Conflicts: U.101.
M02 Claim: The FY1980 ten-year summary's 1976-1979 dividend row is refuted by each year's own report and no
split factor reconciles them. — Date: 1980-04-01 — Source: WALMART_AR_1980.txt (S0109) vs S0105/S0106/S0107/
S0108 — Source date: 1976-03-26 … 1980-04-01 — URL: sources/periodicals/ — Archived: on disk — Tier: 1 —
Class: FACT (of refutation) — Passage: "Comparable stores sales (excluding the effect of new stores) increased
17 percent" — Conf: High — Corroboration: 4 contemporaneous prints, ONE lineage — Conflicts: U.026.
M03 Claim: Business Week's 1962 index printed four discount-sector distress items in the year of the first
Wal-Mart opening while printing the company's name zero times. — Date: 1962-08-18 … 1962-12-01 — Source:
Business Week 1962 Index (S0112) — Source date: 1963 — URL:
https://ia802906.us.archive.org/14/items/sim_business-week_1962_index/sim_business-week_1962_index_djvu.txt —
Archived: extract in sources/periodicals/BUSINESSWEEK_INDEX_1962-1971_EXTRACT_walmart_and_sector_hits.txt —
Tier: 2 — Class: CONTEMPORARY OBSERVATION (index-level only) — Passage: "Discounters strive to ride out storm:
Fast-growing $6-billion industry is facing a major shakeout (with illus) p78, Dec.1" — Conf: High (existence),
Medium (content, unreachable) — Corroboration: 1 independent publisher — Conflicts: U.035, U.037, U.039.
N01 Claim: The registrant's consolidated life begins at the 1970-02-01 pooling, and FY1968-FY1971 earnings are
labelled pro forma by the company itself. — Date: 1970-02-01 — Source: WALMART_AR_1972.txt Note 1 and the
five-year table (S0101) — Source date: 1972-03-22 — URL:
https://archive.org/details/1972-annual-report-for-walmart-stores-inc — Archived: on disk — Tier: 1 —
Class: FACT — Passage: "Excess of net proceeds over par value of 200,000 shares sold in public offering
October 8, 1970  3,010,467" — Conf: High — Corroboration: 1 lineage (auditor attests the statements, not the
1945-1962 events) — Conflicts: U.013, U.102.
N02 Claim: No document in the corpus records any rationale for any decision inside the Stage-1 window. — Date:
1945-01-01 → 1970-10-08 — Source: nine-file search; the FY1974 report is the only place the registrant states a
gate at all — Source date: 1972-03-22 → 1980-04-01 — URL: sources/periodicals/ — Archived: on disk — Tier: 1 —
Class: FACT (of absence) / UNKNOWN (mechanism) — Passage: "Further expansion of this division will depend on
the results obtained from these first two units." (FY1974, OUT of window) — Conf: High — Corroboration: 0 —
Conflicts: U.109, U.222.
P01 Claim: FY1975 net sales are carried at $236,209 thousand on the inversion of the FY1975 report's own five
printed rows, with the 226,209 alternative recorded and unresolved. — Date: 1975-01-31 — Source:
WALMART_AR_1975.txt (S0104) + S0106/S0107/S0108 — Source date: 1975-03-28 — URL:
https://archive.org/details/1975-annual-report-for-walmart-stores-inc — Archived: on disk — Tier: 1 —
Class: ESTIMATE/DERIVED from contemporaneous inputs — Passage: "(5855+6353)+1800+48088+176591-2478 = 236209" —
Conf: Medium-High — Corroboration: 1 lineage in four printings — Conflicts: U.016, U.205.
P02 Claim: FY1978 total assets exist at two values for one date, and the asset series is therefore broken and
printed broken. — Date: 1978-01-31 — Source: WALMART_AR_1978.txt (S0107) vs WALMART_AR_1979.txt comparative
(S0108) — Source date: 1978-04-14 / 1979-04-06 — URL: sources/periodicals/ — Tier: 1 — Class: FACT — Passage:
"All financial information has been restated to reflect the retroactive application ot [sic] Statement of
Financial Accounting Standards No. 13" — Conf: High — Corroboration: 1 lineage — Conflicts: U.022 (and the
forbidden-operation rule at §P.0.4(i)).
P03 Claim: The share of the issuer sold publicly on 1970-10-08 was about 6.7% of the pre-split base, derived,
because no document states a float percentage. — Date: 1970-10-08 — Source: DERIVED from S0101's rows —
Source date: 1972-03-22 — URL: sources/periodicals/WALMART_AR_1972.txt — Tier: 1 — Class: DERIVED — Passage:
"6,000,000 ÷ 2 = 3,000,000; 200,000 ÷ 3,000,000 = 6.7%" — Conf: Medium — Corroboration: 1 — Conflicts: U.031.
Q01 Claim: The earliest attestation of the 1945 origin is FY1973's "twenty-eight year history", a back-cast
made 28 years after the event by the entity whose history it is. — Date: 1973-03-20 — Source:
WALMART_AR_1973.txt (S0102) — Source date: 1973-03-20 — URL:
https://archive.org/details/1973-annual-report-for-walmart-stores-inc — Archived: on disk — Tier: 1 —
Class: RETROSPECTIVE INTERPRETATION — Passage: "…pany's twenty-eight year history. Let's" (OCR fragment as
printed) — Conf: High (the telling) / Low (the told) — Corroboration: 1 lineage in six printings —
Conflicts: U.045, U.110.
Q02 Claim: At 1970-01-01 the company owned and operated 18 Wal-Mart Discount Cities and 14 Ben Franklin
variety stores in a four-state area with sales of $31 million. — Date: 1970-01-01 — Source:
WALMART_AR_1980.txt "Wal-Mart's Past — Foundation for the Future" (S0109); the 18-store figure inside
WALMART_AR_1972.txt President's message (S0101) — Source date: 1980-04-01 / 1972-03-22 — URL:
sources/periodicals/ — Tier: 1 — Class: FACT (as company state) / RETROSPECTIVE SOURCE (a 1980 sentence about
1970) — Passage: "On January 1, 1970, eight years after the opening of the first Wal-Mart Discount City store
in Rogers, Arkansas, the Company owned and operated 18 Wal-Marts and 14 Ben Franklin variety stores in a
four-state area, with sales totaling $31 million" — Conf: Medium-High — Corroboration: 1 lineage; the
18+14=32 agreement with the audited FY1970 count is an internal check, not a second source — Conflicts: U.029.
R01 Claim: The company's shares were not exchange-listed as of 1970-12-31, and this is the only Stage-1 company
fact with a non-registrant origin. — Date: 1970-12-31 — Source: SEC, Securities traded on exchanges … as of
December 31, 1970 (`S0139`, pending issue) — Source date: 1971 — URL:
https://archive.org/download/securitiestraded1970unit/securitiestraded1970unit_djvu.txt — Archived:
sources/gov_docs/ (941,197 B read whole) — Tier: 1 — Class: FACT (of absence) + INFERENCE (that the silence is
informative) — Passage: "This publication contains the alphabetical list by issuers of all securities admitted
to trading on stock exchanges under the Securities Exchange Act of 1934 except securities exempted under
Section 3" — Conf: High — Corroboration: 1 (independent of the registrant and its auditor), corroborating
listing status and NO figure — Conflicts: U.112, U.044.
S01 Claim: Pre-1994 for this company is digitised print, not EDGAR: the electronic filing history begins
1994-02-14 and the 1970 registration statement is paper. — Date: 1994-02-14 — Source:
sources/EDGAR_submissions_CIK0000104169_002_1994-2012.json — Source date: 2026-09-24 — URL: EDGAR — Archived:
on disk — Tier: 1 — Class: FACT — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High — Corroboration: 1 —
Conflicts: none; route U.210 UNTRIED.
T01 Claim: Every positive statement about this company inside Stage 1 traces to one lineage — the registrant's
reports plus its auditor's opinions — and downloading five more reports from the same run left the independent
count at 1. — Date: 1972-03-22 → 1980-04-01 — Source: A3 §7.2(c), re-tested by A5 §What this changes —
Source date: 2026-09-25 — URL: research/A3_audited_series_1962_1980.md; research/A5_sec_statistical_lineage_probe.md —
Archived: on disk — Tier: n/a (method finding) — Class: INFERENCE from documentary enumeration — Passage: "no
number of further years of Wal-Mart's own annual reports can move this verdict; only a different publisher can"
— Conf: High — Corroboration: 1 — Conflicts: U.038.
U01 Claim: The 1962 opening month is attested by the registrant as November 1962 and by its own curated page as
2 July 1962, and the conflict is unresolved. — Date: 1962 — Source: WALMART_AR_1975.txt and _1978.txt (S0104,
S0107) vs sources/EXTRACT_corporate_walmart_history_timeline.md — Source date: 1975-03-28 / 1978-04-14 vs
undated page retrieved 2026-09-23 — URL: as cited — Archived: on disk — Tier: 1 / Tier 4-equivalent as
evidence — Class: FOUNDER CLAIM (retrospective) both sides — Passage: "the Company did not open its first
discount department store until November 1962" — Conf: Low on both; High that they disagree — Corroboration:
0 independent origins — Conflicts: U.001 (part 1's U-C0/1 and part 2's U-E/1 are the same conflict).
U02 Claim: This volume's central negative finding is not an embarrassment but the result: the archive is dense
from 1972 and mute before it, and no FY1962-FY1967 value exists to be found in it. — Date: 1945→1970 — Source:
A3-039; part 1 §A.2 — Source date: 2026-09-25/26 — URL: research/; _parts/s1_p1.md — Archived: on disk —
Tier: 1 — Class: FACT (of a measured perimeter) — Passage: NO_VERBATIM_PASSAGE_RECORDED — Conf: High —
Corroboration: 4 independent document families all returning the same silence — Conflicts: U.101, U.102.
```

**Records deliberately not written:** any claim resting only on *Made in America* (1992) — the bytes are not in
this repository and the class would be `FOUNDER CLAIM (retrospective memory)` with a source line the reader
cannot check (**U.219**); and any claim whose only support is the FY1980 ten-year dividend row or the
"Delaware / 1969-10-01" header line, both of which are retracted (**U.026, U.014**).

---

>>> REGISTER ROWS FOR MERGE <<<

**Merge contract, read before appending.** (1) `conflicts.csv` **already carries 18 rows** under
`U-A3/1…9` and `U-A4/1…9`; those are **renumbered per §U.0.1, never re-issued** — the rows below are only the
conflicts no register row covers. (2) `s1_p2.md`'s block drafts `U-E/1 → U.001`, `U-F/1 → U.034`,
`U-K/1 → U.025`, `U-A2/2 → U.031`, `U-A2/3 → U.027`, `U-A2/4 → U.032`, `U-A2/5 → U.028`, `U-A2/6 → U.029`,
`U-A2/7 → U.011`; **take part 2's text and renumber it, do not duplicate**. (3) A5's pending rows
(`S0139`–`S0141` proposed, three quantitative rows, two timeline rows, `U-A5/1 → U.044`) and part 2's
`S0139`–`S0142` collide at `S0141`: **see U.048 — one id per document, assigned centrally, then re-point both
volumes' prose.** (4) Every `stage` cell below is the literal `stage1` (§13 register vocabulary). (5)
`§P`'s rows P01–P80 and `§S.1`'s table are the drafted bodies for `quantitative.csv` and `data_gaps.csv`;
**§S.1 is in `data_gaps.csv`'s exact column order and that file does not yet exist for this company.**
(6) Where one of my `quantitative.csv` rows duplicates a part-2 row on `(date, metric)`, **the §P row
governs**, because it carries the CONTEMP/RESTAT basis flag.

### `conflicts.csv` — 11 rows (all new; none duplicates an existing or drafted row)

```
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence
Walmart,stage1,U.013,B; C; N; boundary,"The company was incorporated as Wal-Mart Stores, Inc. in 1969","corporate.walmart.com/about/history (extract), sources/EXTRACT_corporate_walmart_history_timeline.md",2026-09-23,"The consolidated registrant was created by a pooling-of-interests exchange effective 1970-02-01 out of the various subsidiaries held by Walton Enterprises, Inc.; and lore holds Wal-Mart, Inc. incorporated 15 March 1962","Wal-Mart Stores Inc. FY1972 report Note 1, S0101 (the 15 March 1962 leg is UNATTESTED anywhere on disk)",1972-03-22,"a corporate-history page compresses a multi-entity reorganisation into one anniversary date, and separate lore supplies the missing operating entity with a day and a month; the audited note never claims to be a founding story","the 1970-02-01 pooling is Tier-1, audited and dated to the day; the 1969 claim is Tier-1 as an artifact and uncited as evidence; the 1962 charter has no document at all","the 1962-vs-1969 argument is the wrong frame: the documented event is 1970-02-01 (kept as the live losing rival for the stage close); the 1962 operating entity remains a separate, still-undated question","names, dates and states of every predecessor entity; what Walton Enterprises, Inc. was; whether any 1962 or 1969 charter exists. Arkansas SoS and county records UNTRIED (U.211); EDGAR formerNames search in flight (U.203)",High on 1970-02-01; UNKNOWN on 1962 and 1969
Walmart,stage1,U.014,Header; B; D,"Wal-Mart Stores, Inc. is a Delaware corporation incorporated 1969-10-01","_parts/s1_p1.md header block and §D record D-R03 (an upstream probe assertion carried into a volume header)",2026-09-23,"No document in sources/ states a state of incorporation or a 1969 date at day precision: 'Delaware' occurs 0 times across the nine printed annual reports and the company page gives 1969 as a year only, uncited","negative search across WALMART_AR_1972.txt … WALMART_AR_1980.txt; sources/EXTRACT_corporate_walmart_history_timeline.md",1972-03-22 to 1980-04-01,"an inherited upstream assertion was never grepped against the corpus (method §14 rule 8); the only 'Delaware' strings in the corpus are a state navigation list in walmart_museum_page.html and an unrelated SEC ticker file","the verified negative covers nine Tier-1 documents; the assertion rests on none","State: UNKNOWN · Day: UNKNOWN · Date carried: 1969 (company-asserted, year only) · Class: UNKNOWN · the claim is RETRACTED, not restated","whether a charter exists at the Arkansas SoS or in Benton County records (U.211) or whether EDGAR's formerNames field states a state (U.203, in flight)",High (that no local document supports either element)
Walmart,stage1,U.015,D; P; Q,"1975-08-19 was the one and only two-for-one stock split in the attested series and no second split exists in the corpus","_parts/s1_p1.md §D record D-R09",2026-09-25,"The corpus prints THREE two-for-one events: 1971-06-11 (1,500,000 shares, $150,000 par charge) and 1972-04-05 (3,000,000 shares, $300,000) inside the audited FY1972 capital note, plus 1975-08-19 (+6,687,789 shares) in the FY1976 report Note 4","Wal-Mart Stores Inc. FY1972 report capital note, S0101; FY1976 report Note 4, S0105",1972-03-22 / 1976-03-26,"a count taken from one comparative table instead of from the note that authorises the events","the refutation is printed in two Tier-1 audited documents; the original claim rests on none","three splits printed, of which exactly one (1975-08-19) falls inside the EPS-restatement dispute — proven by the halving pattern FY1974 $.93 then $.47, i.e. ONE adjustment not two; and 1975-08-19 is OUTSIDE Stage 1's window","whether further splits sit in the FY1981-FY1998 reports (UNTRIED, outside stage, U.220)",High (that the single-split claim is refuted)
Walmart,stage1,U.019,P; A3 §3.6,"FY1972-FY1976 net income as published: 2,907k / 4,591k / 6,159k / 6,353k / 11,506k","Wal-Mart Stores Inc. FY1972-FY1976 reports, S0101-S0105",1976-03-26,"FY1980 ten-year table: 2,806k / 4,439k / 5,954k / 5,995k / 11,132k, with FY1976 pre-tax 22,057k not 22,798k","Wal-Mart Stores Inc. FY1980 report ten-year summary, S0109",1980-04-01,"retroactive application of SFAS-13 to store capital leases, over a base already broken by the LIFO change effective 1975-01-31","both Tier-1, same lineage, same auditors; A is what investors were told at the time, B is the series' final audited shape","quote A for any statement about what was known when and B for comparison with FY1979/FY1980, labelling every figure as-filed or restated; there is no third figure that is 'the real' number","the FY1971-FY1974 restated values are read from OCR-scrambled FY1980 middle rows and whether pre-tax income was restated for those years is not shown; FY1975-FY1978 restated values print clean in FY1979 (COR-A3-03)",High (that a restatement occurred); Low (individual pre-1976 restated values)
Walmart,stage1,U.026,A; P,"FY1980 ten-year dividend row: 1976 $.09, 1977 $.11, 1978 $.19, 1979 $.25","Wal-Mart Stores Inc. FY1980 report ten-year summary, S0109",1980-04-01,"Each year's own report: $.065 (FY1976), $.085 (FY1977), $.16 (FY1978, quarterly .025/.045/.045/.045), $.22 (FY1979, four quarters at $.055)","Wal-Mart Stores Inc. FY1976-FY1979 reports, S0105-S0108",1976-03-26 to 1979-04-06,"no split factor reconciles the two series ($.09 / .065 = 1.38 is not a split) and the documents supply no bridge; the candidates are a typesetting/OCR failure in the ten-year block or an unstated alternative basis","four contemporaneous prints against one retrospective table whose middle rows are independently known to be OCR-damaged (A2 W-69)","the contemporaneous rows govern; the FY1980 row stays on the record as printed and is BARRED from quantitative.csv and from any per-share dividend series (COR-A3-04)","why the FY1980 table prints what it does: the FY1980 page image is UNTRIED (U.206)",High
Walmart,stage1,U.030,B; Q,"FY1973 printed 16 new stores plus 2 enlarged relocations","Wal-Mart Stores Inc. FY1973 report, S0102",1973-03-20,"FY1973 year-end stores 64 against 51 a year earlier: net +13, implying at least 5 units left the base unlisted; FY1976 by contrast prints 22 openings against a net +21 which closes exactly on the January 1976 Rogers Ben Franklin closure","Wal-Mart Stores Inc. FY1973 and FY1976 reports, S0102 and S0105",1973-03-20 / 1976-03-26,"openings are gross and the year-end tables are net; the FY1973 report does not list its exits at all","one lineage, but the arithmetic is internal and checkable, and FY1976 demonstrates the mechanism","FY1976 reconciles and FY1973 does not; the exits are recorded as UNKNOWN and NOT as variety-store conversions, which no document licenses","which stores, where, under which banner, sold or closed",High (the arithmetic); UNKNOWN (the exits)
Walmart,stage1,U.033,B; D,"Sam Walton opens the first Walmart store (single founder, no co-operator named)","corporate.walmart.com/about/history (extract), sources/EXTRACT_corporate_walmart_history_timeline.md",2026-09-23,"The first Wal-Mart Discount City was opened in 1962 in Rogers, Arkansas by Sam M. Walton and his brother James L. Walton, captioned Wal-Mart's co-founders; J. L. 'Bud' Walton appears in FY1977/FY1979 and as Senior Vice President in FY1974's officer list","Wal-Mart Stores Inc. FY1980 report, S0109; FY1974 officers page, S0103",1980-04-01 / 1974-03-21,"an anniversary page compresses the story to one name; the audited-era report names two operators and a board page attests the second as an officer","the co-founder print is Tier-1 inside the audited document set and is corroborated three times within the same lineage; the single-founder page is Tier-1 as artifact, uncited as evidence. BOTH are the registrant's own record, so the independent-origin count is 1 either way","the co-operator is in the company's own documents and the single-founder form is a curation choice; neither reading is independently evidenced for 1962. Recorded against the single-genius framing (§2)","what either man did in 1962, and who decided: no document in this corpus records either",High (that the two company artifacts disagree); Low (the 1962 event)
Walmart,stage1,U.045,B; C; Q,"Between 1945 and 1962 the Waltons assembled fifteen successful Ben Franklin stores; Beginning in 1945, with a Ben Franklin franchised store in Newport, Arkansas","Wal-Mart Stores Inc. FY1975 and FY1980 reports, S0104 and S0109",1980-04-01,"15 Ben Franklin stores between 1946 and 1962; the brothers formed a partnership in 1946; Bud Walton's Versailles, Missouri store dates to 1946","Wal-Mart Stores Inc. FY1977, FY1978, FY1979 reports, S0106-S0108",1977-04-01 to 1979-04-06,"the second date marks the brothers' partnership and the first Sam's individual franchise, and the reports use both without reconciling them; the label also drifts from 'Ben Franklin stores' to 'variety stores'","equal: one lineage, several reports, three years apart","the stage opens on the claimed 1945 individual franchise, the count's start is printed both ways, and 1946 is flagged as the partnership year; neither year is documented","no deed, franchise agreement or register entry for either year is in this corpus (U.110); Mississippi County (AR) records UNTRIED",Low on both dates; High that the registrant prints both
Walmart,stage1,U.046,A; P; Header,"The company's own page dates '1967 — The Walton family owns 24 stores, ringing up $12.7 million in sales'","sources/EXTRACT_corporate_walmart_history_timeline.md",2026-09-23,"FY1968 (ended 1968-01-31) is the year with 24 stores and net sales $12,618,754; FY1967 prints NOTHING anywhere in the corpus","Wal-Mart Stores Inc. FY1972 report five-year table, S0101; A3 Table S1; A3 §0 fiscal-basis note",1972-03-22,"a fiscal year ending 31 January is labelled on the page by its starting calendar year","the audited series is Tier-1 and internally consistent; the page carries the same number with the wrong label","the page's '1967' is FY1968. Every register row must carry the fiscal basis, and no FY1967 value may be created out of this label — the year is EMPTY, not $12.7 million (the page's '1972 — 51 stores, $78 million' is, by contrast, correct)",none about the mechanism; whether other page labels shift the same way is checkable the same way and was checked for the two rows the page carries,High
Walmart,stage1,U.047,P,"FY1973 net sales $124,889,141 — in FY1973's own presentation and every later comparative print","Wal-Mart Stores Inc. FY1973 report, S0102",1973-03-20,"$124,059,141 printed for FY1973 on the FY1974 report's audited statement pages","Wal-Mart Stores Inc. FY1974 report, audited statement pages (A3-002); the FY1974 own-column is separately missing from the same block",1974-03-21,"a typewriter or OCR transposition in a statement block with a second known defect, which is why FY1974's money is taken from the Five Year Progress Report and not the statement pages","A has many printings (one lineage) and is consistent with FY1973's own totals; B is a single cell in a block already shown to drop cells","$124,889,141 governs; the misprint is recorded, not deleted","which physical page erred: the FY1974 page image is UNTRIED (U.206)",High (claim A); Low (claim B)
Walmart,stage1,U.048,T; register hygiene,"_parts/s1_p2.md's merge block issues S0141 = the company's curated history page (and S0142 = the museum page)","s1_p2.md >>> REGISTER ROWS FOR MERGE <<< sources.csv block",2026-09-26,"research/A5_sec_statistical_lineage_probe.md's pending block issues S0141 = the HathiTrust search/catalogue route probe","A5 §CSV append rows (S0139-S0141 proposed)",2026-09-25,"two writers extended the same append-only id block without the central assignment §13 requires; S0139 and S0140 happen to agree, S0141 does not","both rows are genuine content; the identifier is not unique — this is the exact failure class §14 rule 7 records (22 ids each naming three documents)","the merge issues one id per document: keep S0139/S0140 as both blocks have them, assign the next free central ids (S0143+) to the corporate page, the museum page and the HathiTrust probe, then re-point both volumes' prose; the keys gate then resolves","the final numbering, which the register owner owns; this volume depends on none of it because every not-yet-issued id is written backticked",High (that the collision exists and is verifiable from the two blocks)
```

### `timeline.csv` — 11 rows (in-window and attestation-geometry events; no duplicate of an existing or part-2 row)

```
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes
Walmart,stage1,1946,The Walton brothers' partnership is the year three later reports give for the start of the fifteen-store assembly — a rival label to the claimed 1945 individual franchise,Walton brothers,"Bentonville/Newport, AR",S0107,FOUNDER CLAIM,Low,U.045,"no instrument, firm name or date is documented; S0106 puts Bud's Versailles MO store in 1946 and S0108 counts 'between 1946 and 1962'. Earliest attestation is 1977-dated"
Walmart,stage1,1945-1980,The 1945 origin is re-printed in six dated restatements (FY1973 'twenty-eight year history' through FY1980 'Beginning in 1945 … Newport, Arkansas'), so the distance between event and attestation GROWS from 28 to 35 years,Wal-Mart Stores Inc.,Bentonville AR,S0102-S0109,RETROSPECTIVE INTERPRETATION,High,none,"Version evidence, not corroboration (§3): six printings of one lineage. Recorded as a timeline row because the growth of the attestation distance is itself the finding of §B-1"
Walmart,stage1,1955,First company office established above Walton's Family Store in Bentonville — the earliest pre-1962 date carrying a NAMED business premises,Walton family,"Bentonville, AR",S0105,FOUNDER CLAIM,Medium,none,"Attested only by a 1976 sentence, 21 years after (A2 W-49). It is an office above a store, not a venture, and part 1 §C.0 ranks it below both 1945 and 1962 as a stage marker"
Walmart,stage1,1957,Company office moved to a small building on Southeast A Street, Bentonville,Walton family,"Bentonville, AR",S0105,FOUNDER CLAIM,Medium,none,"Same single 1976 sentence; no 1957 document exists"
Walmart,stage1,1968-01-31,FY1968 year end — the EARLIEST year any document in this corpus counts: 24 stores and net sales $12,618,754, with earnings captioned pro forma by the registrant,Wal-Mart Stores Inc.,"Bentonville, AR",S0101,FACT,Medium,U.046,"Restated in the FY1972 report four years after the year end and OUTSIDE every audit opinion on disk. The company page's '1967' label for this same data is the U.046 conflict"
Walmart,stage1,1969,The company page's only incorporation statement: 'The company officially incorporates as Wal-Mart Stores, Inc.' — year only, no month, no day, no state, no citation,Wal-Mart Stores Inc.; Walton family,UNKNOWN,S0141-proposed,UNKNOWN,Low,"U.013, U.014","Adopted nowhere in this part-set. A2's data-gap row records the claim as undated and uncited; 'Delaware' occurs 0 times in the nine reports"
Walmart,stage1,1969-11,Initial portion of the present Bentonville general-office facility completed,Wal-Mart Stores Inc.,"Bentonville, AR",S0105,FACT,Medium,none,"A 1976 sentence about 1969; no cost, size or decision-maker stated. It anchors the office line 1955 → 1957 → 1969 → the 1972-12-03 open house (U.028)"
Walmart,stage1,1970-01-01,Fleet at the boundary's edge: 18 Wal-Mart Discount Cities + 14 Ben Franklin variety stores in a four-state area, sales 'totaling $31 million',Wal-Mart Stores Inc.; Ben Franklin,"AR, MO, OK, KS (four states, not enumerated in the document)",S0109,FACT,Medium-High,U.029,"A 1980-dated statement of a 1970 state, corroborated within the same lineage by S0101's 'eighteen Wal-Mart stores that already existed as of February 1, 1970'. 14/32 = 43.8% of units still carried another firm's banner at the float"
Walmart,stage1,1971-01-31,FY1971 year end: 38 stores, net sales $44,286,012, pre-tax $3,170,599, pro-forma net $1,651,599, 6,000,000 shares, equity $7,840,701; profit-sharing program adopted by the Board,Wal-Mart Stores Inc.,"Bentonville, AR",S0101,FACT,Medium,none,"No FY1971 report exists; every value is a 1972-dated comparative and the FY1972 opinion names only 'the year then ended'. The profit-sharing act is the only organisational decision dated inside the window by a signed document"
Walmart,stage1,1972-03-22,ATTESTATION FLOOR: the earliest document of any kind in this corpus that names the company (FY1972 report; President's message signed Sam M. Walton; stockholders approve authorised common of 11,000,000),Wal-Mart Stores Inc.; Arthur Young & Company,"Bentonville, AR / Tulsa, OK",S0101,FACT,High,U.101,"The load-bearing date of Stage 1: nothing in the corpus is dated earlier. Twelve of this volume's §S rows and all of §M's silence-row are defined against it"
Walmart,stage1,2026-09-26,Research-state event: the canonical §U anchor set U.001-U.048 / U.101-U.116 / U.201-U.222 is minted and every dossier-local and part-local conflict key is mapped onto it,s1_p3 (this volume); merge agent,n/a,s1_p3.md,LEAD,High,U.048,"Not a company event. Registered so the merge cannot renumber the spine blind: 18 existing conflicts.csv rows are renumber-only, 11 new conflict rows and 11 timeline rows are requested here, and the S0141 collision between part 2 and A5 is disclosed rather than silently harmonised"
```

### `quantitative.csv` — 24 rows (register gaps verified against `quantitative.csv` as read; §P's basis flags govern)

```
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,derived_arithmetic,notes
Walmart,stage1,FY1968,Income before income taxes,779754,USD,S0101,1972-03-22,FACT,Medium,,"RESTAT (in FY1972 report), only printing anywhere; outside every audit opinion on disk"
Walmart,stage1,FY1968,Net income (pro forma),481754,USD,S0101,1972-03-22,FACT,Medium,,"The registrant's own caption is 'Pro forma net income'; the group did not exist in FY1968 — pooling is 1970-02-01"
Walmart,stage1,FY1968,Net income per share (pro forma),0.09,USD/share,S0101,1972-03-22,FACT,Medium,,pro forma; split-adjusted once for the 1975-08-19 two-for-one in later prints
Walmart,stage1,FY1968,Stores in operation at end of period,24,stores,S0102,1973-03-20,FACT,Medium,,RESTAT (in the FY1973 'Six Years at a Glance'); earliest store count anywhere in the corpus
Walmart,stage1,FY1969,Net sales,21365081,USD,S0101,1972-03-22,FACT,Medium,,RESTAT (in FY1972); the company page's calendar-year label for this data is the U.046 conflict
Walmart,stage1,FY1969,Income before income taxes,1056211,USD,S0101,1972-03-22,FACT,Medium,,RESTAT; outside every opinion
Walmart,stage1,FY1969,Net income (pro forma) / per share,605211 / 0.12,USD; USD/share,S0101,1972-03-22,FACT,Medium,,pro forma label kept verbatim
Walmart,stage1,FY1969,Stores in operation at end of period,27,stores,S0102,1973-03-20,FACT,Medium,,RESTAT (in FY1973)
Walmart,stage1,FY1970,Net sales,30862659,USD,S0101,1972-03-22,FACT,Medium,,"RESTAT (in FY1972); reprinted in S0103 (1974) and S0107 (1978). The FY1980 narrative rounds it to '$31 million'"
Walmart,stage1,FY1970,Income before income taxes,2198764,USD,S0101,1972-03-22,FACT,Medium-High,,"Independently consistent with the FY1978 nine-year table's own rows (2,199 thousand) — an internal check, not a second lineage"
Walmart,stage1,FY1970,Total assets,8493,USD thousands,S0107,1978-04-14,FACT,High,,FIRST statement of FY1970's balance sheet anywhere in this corpus; RESTAT (in the FY1978 nine-year table); no FY1970 report exists (U.104)
Walmart,stage1,FY1970,Stockholders' equity,3159,USD thousands,S0107,1978-04-14,FACT,High,,confirmed by the table's own ROE row: 1,652 / 3,159 = 52.3 as printed for FY1971
Walmart,stage1,FY1970,Stores in operation at end of period,32,stores,S0101,1972-03-22,FACT,Medium,,"Ties exactly to S0109's 18 Discount Cities + 14 Ben Franklin at 1970-01-01 — an internal consistency check within ONE lineage"
Walmart,stage1,FY1971,Net sales,44286012,USD,S0101,1972-03-22,FACT,Medium,,RESTAT (in FY1972); reprinted FY1974/FY1975/FY1978; no FY1971 report exists
Walmart,stage1,FY1971,Net income (pro forma) / per share,1651599 / 0.30,USD; USD/share,S0101,1972-03-22,FACT,Medium,,the FY1975 and FY1978 tables print 1,652 thousand and $.15 (split-adjusted once)
Walmart,stage1,FY1971,Total assets / Stockholders' equity,15331 / 7841,USD thousands,S0107; S0101,1978-04-14 / 1972-03-22,FACT,High,,"position RESTAT (in FY1978); the equity figure also prints CONTEMP in the FY1972 report's own comparative column"
Walmart,stage1,FY1971,Number of shares outstanding,6000000,shares,S0101,1972-03-22,FACT,High,,par $.10 evidenced in the same document's capital note (1,500,000 → 150,000; 3,000,000 → 300,000)
Walmart,stage1,FY1971,Current ratio,1.87,ratio,S0101,1972-03-22,FACT,High,,falls to 1.65 by FY1972 in the same document while the fleet grew 38 → 51 — §M.1 row 5
Walmart,stage1,FY1972,Net sales,78014164,USD,S0101,1972-03-22,FACT,High,,CONTEMP (as-filed) — the first year with a report of its own
Walmart,stage1,FY1972,Net income / EPS (pro forma) / Total assets / Equity,2907354 / 0.47 / 28463 / 10748055,USD; USD/share; USD thousands; USD,S0101,1972-03-22,FACT,High,,EPS $.47 as filed; later prints show $.24 (one split adjustment); balance-sheet rows also RESTAT in S0107
Walmart,stage1,FY1972,Stores / new store space added / employees,51 / 604000 / 2300,stores; square feet; people,S0101,1972-03-22,FACT,High,,"headcount is 'some 2,300' in a letter signed by the founder; the basis ('employees' vs 'associates') is never defined in any of the nine documents"
Walmart,stage1,FY1973,Net sales,124889141,USD,S0102,1973-03-20,FACT,High,,"CONTEMP. The FY1974 report's audited statement pages misprint FY1973 as 124,059,141 — recorded as conflict U.047, not corrected silently"
Walmart,stage1,FY1973,Net income / EPS / Total assets / Equity / Stores / Inventories,4591469 / 0.70 / 46241 / 24754 / 64 / 29427119,USD; USD/share; USD thousands; USD,S0102; S0103,1973-03-20 / 1974-03-21,FACT,High,,"inventory reprinted exact in the FY1974 report's Note 2 — same lineage; shares contested (U.018) and at least 5 exits unexplained (U.030)"
Walmart,stage1,1970-10-08,Shares sold publicly / net proceeds / derived net per share / derived float,200000 / 3030467 / 15.15 / 0.067,shares; USD; USD/share; percent of pre-split shares,S0101,1972-03-22,FACT + DERIVED,Medium,,"(3,010,467 excess over par + 20,000 par) / 200,000 = 15.15; 6,000,000 / 2 = 3,000,000 pre-split; 200,000 / 3,000,000 = 6.7%. The gross price is NOT evidenced: $16.50 is company-page lore with no licensed bridge (U.031). Day precision comes from inside an audited FY1972 note — a 1972 document reporting a 1970 event"
```

### `sources.csv` — 4 rows requested; **`source_id` values are PROPOSED and subordinate to central assignment at merge (see U.048)**

```
source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes
S0143,stage1,The 1970 first-distribution-centre date and the pre-1962 anniversary framing carried into §M/§N/§U.027 as unsupported retrospectives,PBS: Wal-Mart Timeline (2004),Public Broadcasting Service,third-party retrospective web summary,secondary,1945-1970,2004-08-20,2026-09-24,UNKNOWN (as held),sources/EXTRACT_pbs_2004_timeline.md,3,RETROSPECTIVE INTERPRETATION,Low,INDEPENDENT publisher but retrospective and uncited: it is not a witness to any company state and moves the independent-lineage count for no fact,NO_VERBATIM_PASSAGE_RECORDED,"used only to show that the 1970 / Springfield-MO first-DC folklore has no document behind it (U.027); never cited for a fact"
S0144,stage1,The same first-DC and origin folklore as re-transmitted in 2012 in a trade-logistics digest,SCDigest 2012 retrospective note,SCDigest,third-party trade-logistics retrospective,secondary,1945-1970,2012,2026-09-24,UNKNOWN (as held),sources/EXTRACT_scdigest_2012_timeline.md,3,RETROSPECTIVE INTERPRETATION,Low,INDEPENDENT publisher, derivative of the same lore family — NOT a second source for anything (method §3 copying rule),NO_VERBATIM_PASSAGE_RECORDED,registered so a later pass does not count PBS + SCDigest + a company page as three witnesses
S0145,stage1,"The EDGAR floor: nothing electronic before 1994-02-14, first 10-K 1995-04-27, and the 1970 registration statement is therefore paper — plus the formerNames field that the U.203 local route reads",EDGAR submissions JSON for CIK 0000104169 (two blocks: current and 1994-2012; 1,409 filings),U.S. Securities and Exchange Commission,regulatory metadata,primary (as to what EDGAR holds),1994-02-14→2012,2026-09-24,2026-09-24,https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000104169,sources/EDGAR_submissions_CIK0000104169.json and _002_1994-2012.json,1,FACT,High,INDEPENDENT of the registrant as to holdings but derivative as to content (it indexes the registrant's own filings); it proves the ABSENCE of electronic filings before 1994 and nothing about the 1945-1970 business,NO_VERBATIM_PASSAGE_RECORDED,"the three companion files probe_EDGAR_submissions_001/002/current.json are S3 NoSuchKey XML error bodies and are therefore UNANSWERED, not empty; probe_SEC_tickers.json holds formerNames = ['Walmart Inc.', 'WAL MART STORES INC'] — the shortest remaining path to U.014, in flight as U.203"
S0146,stage1,The two documentary leads whose bytes are NOT in this repository: the Sam Walton inside-book lead and the DTIC ADA345567 report,STUB_LEAD_samwaltoninsides00vanc.md and STUB_LEAD_DTIC_ADA345567.md,THE FOUNDER'S PLAYBOOK (intake stubs),lead stub with no retrieved text,secondary,UNKNOWN,2026-09,2026-09-24,in-repo,sources/periodicals/STUB_LEAD_samwaltoninsides00vanc.md; sources/periodicals/STUB_LEAD_DTIC_ADA345567.md,n/a,LEAD / UNTRIED,UNKNOWN,neither a source of facts nor an independent lineage: registered so the next pass does not re-probe them and so §14 rule 6's fourth family (auction / museum documentary) is recorded as TRIED-AND-EMPTY-for-the-queries-run rather than skipped,NO_VERBATIM_PASSAGE_RECORDED,"the §14 rule 6 requirement that all four corpus families be attempted before a depth verdict is met only for three: the documentary/auction family is UNTRIED (U.221), which is why §A.2's verdict and §S.3 keep Stage 1 at PROVISIONAL"
```

### Register notes for the merge

1. **Anchor parity.** Every `U.nnn` declared in this volume appears in a row above **or** in
   `s1_p2.md`'s pending block, and every register row above declares its anchor in the `conflict_id` /
   `conflict_ref` column, so `gates.py --checks anchors` can pass once the merge runs. **Until it does, the
   registers contain no `U.nnn` token at all and the anchors check is UNANSWERED by construction, not passed.**
2. **Three outbound corrections this volume asks the register owner to apply** (it wrote no CSV): (a) the
   `timeline.csv` 1962-11 row's `conflict_ref` reads `U-A3/8`, which is the **population** conflict — it should
   point at **U.001** (month) with **U.012** for population; (b) the `timeline.csv` 1961-12 row's
   `conflict_ref` reads `U-A4/7-adjacent`, which is not an id — resolve to **U.041** or clear; (c) the
   `conflicts.csv` section cells carry dossier-local section names (`P; A3 §3.4`) — these are harmless as
   provenance but should not be read as stage-volume pointers now that §P is in part 3.
3. **Files this volume needs but did not create:** `data_gaps.csv` (body drafted in `§S.1`, exact column
   order), `decisions.csv` (body drafted in `§N.1`), `failures.csv` (body drafted in `§M.1`). Their absence is
   recorded at §U.0 note R-3 and is a register-set defect, not a §S/§M/§N shortfall.


