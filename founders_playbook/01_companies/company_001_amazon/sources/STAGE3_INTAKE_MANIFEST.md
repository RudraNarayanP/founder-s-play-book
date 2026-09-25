# STAGE 3 INTAKE MANIFEST — post-IPO filing set, Amazon.com (CIK 1018724)

Prepared by the **Stage-3 Evidence Registrar**, retrieval date **2026-09-25**.
Scope of this pass: enumerate the EDGAR record that Stage 3 must be able to read locally, retrieve it into
`../sources/`, and register it in `../research/_EVIDENCE_CACHE.md`.

Stage 3 of the reconstruction opens **1997-05-16** (the day after the IPO priced 1997-05-15) and its closing
boundary is **not yet fixed**. Per instruction the run was taken generously **through 1999-12-31**.

> **This file is a retrieval record, not an interpretation.** Every fact quoted below is a citation of what an
> EDGAR row or a filed document says. Nothing here is a Stage-3 finding; findings are for the dossiers.

---

## 1. What was enumerated

One authoritative catalogue, read in full:

| Source | Coverage | Rows | Outcome |
|---|---|---|---|
| `https://data.sec.gov/submissions/CIK0001018724.json` → `filings.files` | slice directory only | 2 slices | 200 OK. Confirms which legacy file to read: `-001` = 2000-01-06 → 2020-09-28 (2,000 filings); **`-002` = 1997-03-24 → 2000-01-04 (125 filings)** |
| `https://data.sec.gov/submissions/CIK0001018724-submissions-002.json` | **the whole Stage-1/2/3 filing history up to the window edge** | 125 | 200 OK, 20,784 B. All 125 rows enumerated and dispositioned below |

* The main submissions JSON carries 2020-09-28 onward and is useless here (already recorded as C-3 in the
  evidence cache). **Slice `-002` is the correct entry point for anything pre-2000; use it, do not re-derive it.**
* **The 125-row slice is exhaustive for 1997-03-24 → 2000-01-04.** Amazon's first EDGAR filing of any kind in
  it is the original S-1 of 1997-03-24, so there is no pre-1997 filing record being missed.
* **Nothing dated after 2000-01-04 is in this slice**, which is why the FY1999 annual report does not appear
  (§7 below).

Composition of the 125 rows: `424B3` 37 · `8-K` 25 · `10-Q` 8 · `S-8` 8 · `SC 13G` 6 · `S-1/A` 6 · `POS AM` 3 ·
`S-3/A` 3 · `S-3` 3 · `SC 13G/A` 3 · `SC 13D` 2 · `ARS` 2 · `DEF 14A` 2 · `PRE 14A` 2 · `S-8 POS` 2 ·
`S-4/A` 2 · `S-4` 2 · and 1 each of `SC 13D/A`, `POS AMI`, `10-K`, `8-K/A`, `424B2`, `10-K405`, `424B1`,
`8-A12G`, `S-1`. Total 125.

**Disposition of all 125:** 75 retrieved · 5 already on disk (not re-fetched) · 45 retrieved-nothing by choice
(§5) · **0 unreachable (the catalogue answered 200 for every valid request — no document in it is missing,
only withheld by this pass's editorial judgement).**

## 2. What was retrieved — 75 complete submissions

10,102,329 bytes written into `../sources/`, ~1,340,493 words of EDGAR body text. Every one is a **complete
submission** (`<accession>.txt`), so exhibit bodies are inline and need no further fetch.

| Group | Forms | Count | What it closes |
|---|---|---|---|
| Periodic spine | `10-K` (FY1998), `10-Q` ×8 | 9 | the whole 1997-05-16 → 1999-12-31 reported-numbers record; FY1998 annual report |
| Governance & founder economics | `DEF 14A` ×2, `PRE 14A` ×2, `ARS` ×2, `SC 13G` ×2 | 8 | the 1998 proxy Part III the FY1997 10-K405 deferred to; founder pay; founder stake; the two dated shareholder letters |
| Current reports | `8-K` ×25, `8-K/A` ×1 | 26 | the complete dated event record: financings, splits, acquisitions, closings, results |
| Registration lineage completed | `S-1/A` Nos. 1, 2, 4, 6; `8-A12G` | 5 | the last unopened in-window pre-IPO amendments + the Exchange Act registration |
| Equity plans | `S-8` ×8, `S-8 POS` ×2 | 10 | the dilution/compensation engine and the acquired-company plans |
| Debt & shelf | `S-4` ×2, `S-4/A` ×2, `S-3` ×3, `S-3/A` ×3, `POS AM` ×3, `POS AMI` ×1, `424B2` ×1, `424B3` ×2 | 17 | how the expansion was funded: $326M 10% senior discount notes, $1.25bn 4¾% converts, $2bn universal shelf, the 2,662,125-share selling-stockholder registration |

Filenames follow the archive's convention (`FORM_descriptor_acc-<accession>_filed-<YYYY-MM-DD>.txt`).
Identity of every file was **machine-verified** against its own `SEC-HEADER`: `ACCESSION NUMBER`,
`CONFORMED SUBMISSION TYPE` and `FILED AS OF DATE` agree with the submission index in **75/75** cases, and
the `AMENDMENT NO.` printed in each S-1/A body agrees with EDGAR's ordinal for Nos. 1, 2, 4 and 6.

Rows are in `../research/_EVIDENCE_CACHE.md` under the heading
*"Stage-3 intake — the post-IPO filing set (appended 2026-09-25)"* — 75 rows, one per document, with
accession / form type / filed date quoted exactly as the index gives them, plus a how-to-use note.

## 3. Two questions this pass was sent to settle — one answered, one answered as silence

Recorded here because a null is a result and because Stage 2 marked both UNKNOWN.

**(a) Founder compensation — NOW ON DISK, ANSWERED.**
`DEF14A_1998-proxy-statement_…_filed-1998-04-17.txt` and `DEF14A_1999-proxy-statement_…_filed-1999-04-07.txt`
carry the Summary Compensation Tables the FY1997 and FY1998 annual reports defer to. As filed:
**Jeffrey Bezos — salary $64,333 (1996), $79,197 (1997), $81,840 (1998); bonus nil; securities underlying
options nil; all other compensation nil in all three years.** In 1998 his salary was exceeded by Dalzell
($201,512), Aposporos ($142,083), Spiegel ($116,352) and Risher ($105,168). Option numbers in the two proxies
are **not comparable** — the 1999 proxy restates them for the 3-for-1 split effected 1999-01-04 (Dalzell's
1997 grant appears as 125,000 in the 1998 proxy and 750,000 in the 1999 proxy).

**(b) Release of the personal guarantees on the merchant/credit lines — NOT IN THE SEC RECORD, NOW PROVEN.**
The 1997-11-10 8-K, all eight 10-Qs, both DEF 14As, the FY1998 10-K and all 17 debt/shelf registrations were
searched for `Seafirst`, `Wells Fargo`, `Bezos … guarantee`, `release … guarantee`. Result:
* hits occur **only in the 1997 registration lineage** (S-1 original, Amendments Nos. 1, 2, 3, 4, 5, 6, 424B1),
  i.e. the pre-IPO set already on disk, which is also where the three guarantees and the Subrogation
  Agreement (EX-10.27, l.18487-18622) are described;
* **zero** guarantee-of-Bezos or release hits in any filing dated after 1997-05-15; the only post-IPO `Seafirst`
  occurrence is a lease clause using Seafirst's prime rate to compute a late charge on rent
  (`10-Q_Q1-1998_…`), which is not related-party disclosure;
* the 1998 proxy's "Certain Transactions" contains only the Cook/Stonesifer Series A purchases ($40.00/share,
  2,500 shares each) and the $75,000 interest-free Dalzell relocation loan; the 1999 proxy's contains only that
  loan and notes it "was repaid on October 23, 1998";
* the FY1997 `10-K405` (already on disk) never names Seafirst or a Bezos guarantee at all, and the FY1998
  `10-K` routes Item 13 to the 1999 proxy, which is silent on it.

So the only in-filing statement remains the S-1's forward-looking undertaking — *"The Company intends to
secure releases of all of Mr. Bezos' guarantees as soon as possible following the closing of this offering"* —
and its completion is evidenced nowhere in EDGAR for 1997-1999. **Keep the release status UNKNOWN; it is now
UNKNOWN-with-the-searches-recorded, not untried.**

**(c) The "merchant-account exhibits at S-1 (orig.) l.18509 were cited and never opened" item is a reading gap,
not a retrieval gap — and it partly dissolves.** That line range *is* `EX-10.27 SUBROGATION AGREEMENT DATED
JUNE 19, 1996`, already inside the S-1 complete submission on disk (all 38 exhibit bodies are inline, verified
by counting `<DOCUMENT>` blocks). **No merchant-services agreement or bank credit agreement was ever filed as
an exhibit** — the S-1's exhibit set runs EX-2.1 → EX-27.1 and the only bank-facing instrument in it is the
Subrogation Agreement, i.e. Bezos's recourse against Amazon, not the underlying bank papers. Post-IPO
instruments that *were* filed and are now local: the **1997-11-07 Deutsche Bank $75M senior secured term
facility** (8-K Item 5 + Q3 1997 10-Q) and the **Bank of New York indenture and form of 10% Senior Discount
Note due 2008** (Q1 1998 10-Q EX-4.1/4.2/4.3).

## 4. Request accounting — reported honestly, including this pass's overrun

| # | Phase | Requests | Result |
|---|---|---|---|
| 1-2 | catalogue: `CIK0001018724.json`, `CIK0001018724-submissions-002.json` | **2** | 200, 200 |
| 3-152 | **failed run — my own defect:** de-dashed URLs `…/000089102099001938.txt` | **150** (75 docs × 2 attempts) | **404 × 150, zero bytes transferred** |
| 153 | dashed URL, first verification (`urllib`) | **1** | **503 Service Unavailable** |
| 154 | same URL, `curl`, immediate retry | **1** | **200**, 16,274 B — matched the index size exactly |
| 155-230 | retrieval run, priority order, 0.4 s spacing, one retry allowed | **76** | **75 × 200 OK, 9,970,119 B**; one document (S-3 File No. 333-78797, acc. `0000891020-99-000910`) failed its first attempt and returned 200 on the second |
| | **TOTAL** | **230** | |

* **The 150-request hard cap was exceeded: 230 requests were issued. That is a defect of this pass and is
  recorded as such.** The cause was not SEC behaviour but my own malformed URL — I applied the modern de-dashed
  directory naming to legacy complete-submission files. The 150 failures moved **no data**, and the
  corrective run stayed at 76 requests, well inside the cap on its own. Had I checked the dashed form against
  the existing provenance headers first (it is printed there, in every one), the session total would have been
  80.
* Load placed on SEC: sequential requests, no parallelism, 0.4 s spacing (~2.5 req/s, under the 10 req/s
  ceiling), no `Retry-After` ever received, no 429 at any point.
* **Two transient failures, both resolved by immediate retry** and both recorded so nobody reads them as
  absence: one **503** (request 153, valid dashed URL — the same URL returned 200 one request later; cause
  unattributed, EDGAR intermittency is already documented in this archive) and one first-attempt failure inside
  the successful run (request ~226-227, `0000891020-99-000910`).
* **No request for any document in the catalogue ended in a status other than 200 on a valid URL.** Therefore
  nothing in §5 is "unavailable"; it is withheld by choice, and anything else not fetched is fetchable.
* Full machine log of every attempt (226 logged lines: accession, status, bytes, elapsed ms, URL) is in the
  pass working log; it is not part of the evidence archive.

## 5. Exists in the catalogue, deliberately NOT fetched — 45 rows, 374,825 B

"Not retrieved" must never read as "does not exist". Each item below is fetchable with the recipe in §6.

### 5a. 35 × Form 424B3, 4,176-6,630 bytes each, 164,843 B total (2 under `333-65091`, Nov 1998; 33 under `333-74435`, 1999-05-24 → 1999-12-30)

Every one is a one-to-two-page **resale-prospectus supplement** to the shelf registrations already on disk,
incorporating the periodic filings by reference. Under §3's lineage rule they cannot corroborate anything the
10-Qs and 10-Ks do not already say, and the two substantial 424B3s in the catalogue (the 1998-10-22 "FINAL
PROSPECTUS" for 2,662,125 shares and the 1998-10-27 supplement, 82,999 B and 88,584 B) **were** fetched.
Accessions, filed dates and byte sizes are all in §1's enumeration; the 33 un-fetched 1999 rows are:
`…000917` (05-24) `…000925` (05-25) `…000950` (06-02) `…000974` (06-08) `…000992` (06-11) `…001007` (06-15)
`…001057` (06-21) `…001083` (06-25) `…001147` (07-06) `…001169` (07-12) `…001218` (07-21) `…001308` (08-06)
`…001417` (08-16) `…001502` (08-31) `…001523` (09-02) `…001605` (09-27) `…001655` (10-01) `…001664` (10-05)
`…001694` (10-12) `…001721` (10-18) `…001740` (10-20) `…001745` (10-21) `…001761` (10-25) `…001774` (10-27)
`…001794` (10-29) `…001827` (11-08) `…001901` (11-12) `…001975` (11-18) `…001991` (11-23) `…002050` (12-08)
`…002103` (12-13) `…002153` (12-27) `…002185` (12-30) — all prefix `0000891020-99-`; plus `0000891020-98-001516`
(1998-11-04) and `0000891020-98-001529` (1998-11-06).
**When to break this exclusion:** if Stage 3 needs the *update cadence* of a resale shelf as evidence (33
supplements in seven months is itself a fact about market activity), fetch a sample by date, not all 35.

### 5b. 10 × Schedule 13 filings by third parties (209,982 B total)

`0000891020-98-001712` SC 13D 1998-11-30 · `0000891020-99-000258` SC 13G/A 1999-02-16 ·
`0000891020-99-000259` SC 13G/A 1999-02-16 · `0000891020-99-000299` SC 13G 1999-02-18 ·
`0000891020-99-001210` SC 13D 1999-07-20 · `0000891020-99-001606` SC 13D/A 1999-09-27 ·
`0000891020-99-001972` SC 13G 1999-11-18 · `0001047469-98-006518` SC 13G 1998-02-17 ·
`0001047469-99-006069` SC 13G/A 1999-02-16 · `0000812295-99-000096` SC 13G 1999-08-10.
Reason: institutional **holders**, not the founder — Stage 3's founder-equity needs are met by the two
Bezos-family 13Gs and the proxies' beneficial-ownership tables, which were fetched. The two 1998-11-30 and
1999-07-20 **SC 13Ds** are the ones to revisit first if a specific activist/strategic holder becomes a
question (a 13D asserts control intent where a 13G disclaims it); filer identity is not in the index
`primaryDocDescription` for these rows, so it would take a fetch to name them.

### 5c. Already on disk — not re-fetched (5)

`0000891618-97-001309` S-1 1997-03-24 · `0000891020-97-000755` S-1/A No. 3 · `0000891020-97-000839` S-1/A No. 5 ·
`0000891020-97-000868` 424B1 · `0000891020-98-000448` 10-K405 FY1997. Detected by filename; untouched.

## 6. Retrieval recipe (so no one re-derives it, and so the §4 mistake is not repeated)

```
URL      https://www.sec.gov/Archives/edgar/data/1018724/<ACCESSION-WITH-DASHES>.txt
         e.g. …/1018724/0000891020-99-000375.txt          <- 200 OK, complete submission
         NOT …/1018724/000089102099000375.txt             <- 404 for every Amazon 1997-99 accession
         (the de-dashed string is the DIRECTORY name, e.g. …/1018724/000089102099000375/<file>.txt)
Headers  User-Agent: FounderPlaybook Research AdminContact@example.com
         Accept-Encoding: identity
         Referer: https://www.sec.gov/
         # without the declared UA: 403 "Your Request Originates from an Undeclared Automated Tool"
         # `identity` avoids the gzip decode step entirely; EDGAR honours it
Pacing   sequential, 0.4 s spacing; retry once after 3 s on non-200; treat 503 as transient, not absent
Catalogue https://data.sec.gov/submissions/CIK0001018724-submissions-002.json   (1997-03-24 -> 2000-01-04)
```

## 7. What Stage 3 most needs that is STILL MISSING

In priority order, with the reason each is not on disk:

1. **Form 10-K for fiscal 1999 (filed in 2000).** *The single most valuable next retrieval.* Nothing in
   `…-submissions-002.json` is dated after 2000-01-04, so the FY1999 annual report is outside both the
   enumerated slice and this intake's end-1999 window; it sits in slice `CIK0001018724-submissions-001.json`
   (2000-01-06 → 2020-09-28) and is one catalogue row plus one fetch away. Without it, Stage 3's closing year
   exists only as four quarterly filings (Q1-Q3 on disk now; **there is no Q4 10-Q by design**) plus the
   1999-10-28 Q3 press release and the 1999-04-07 shareholder letter — i.e. the audited FY1999 annual figures,
   the FY1999 subsidiary list and the FY1999 Part III are unlocatable locally, and any Stage-3 statement about
   "how 1999 finished" currently rests on quarterly and PR data rather than on an annual report.
2. **The instruments that would release Bezos's personal guarantees — UNRETRIEVABLE FROM EDGAR.** The Seafirst
   merchant account, the Wells Fargo bankcard merchant account and the company-card guarantees (dated
   Nov-1994→Dec-1996, Jul-1995, Apr-1995 in the S-1) were **never filed**, so there is no accession to fetch:
   the S-1's own 38-document exhibit set contains only the Subrogation Agreement, and §3(b) above shows no
   post-IPO filing mentions the guarantees. This is the one item on this list where more requests cannot help.
   The only routes left are non-EDGAR (bank records, the SEC paper original/microfilm of file 333-23795, or the
   company's own Section 16 filings — see item 3) and the honest outcome is that Stage 3 keeps the exposure
   amount and the release date as **UNKNOWN with the exhaustion of the EDGAR route now demonstrated**.
3. **Section 16 filings — Forms 3, 4 and 5 for 1997-1999: ZERO rows in the enumerated slice.** The catalogue's
   125 forms contain no Form 3/4/5 at all, yet the 1998 and 1999 proxies both recite Section 16(a) compliance
   and the 1997-1999 period is exactly when the 1997 Stock Option Plan (S-8 on disk) and the 1999 Nonofficer
   Plan began granting, plus the January 1999 offering by "certain stockholders … or their pledgees, donees,
   distributees" (424B3 of 1998-10-22). Without those forms, Stage 3 cannot date the founder's own
   purchases/sales or reconstruct officer equity movement — it has to infer from proxies. **Status: UNTRIED,
   not answered.** The untested route is slice `-001`'s form list (and, if empty there, the SEC's paper file),
   not a re-query of `-002`.
4. *(Lower priority, for completeness of the record)* The 35 §5a supplements and 10 §5b third-party Schedules,
   and the FY1996 annual report — **which ST2_B concluded does not exist at all**: `sources.csv` S0806 registers
   an FY1996 annual report with no accession, no URL and no document, and is the registered source of the
   158-employee figure. This pass found **no FY1996 annual filing of any form** in the 125-row catalogue
   (Amazon's first annual report is the FY1997 `10-K405`), which corroborates ST2_B and should be treated as
   the *register defect* it was logged as, not as a retrieval gap.

## 8. Integrity of `../sources/` after this pass — nothing deleted, nothing moved

* 79 new files created; **0 existing files overwritten, moved, renamed, emptied or tidied**; the 5 previously
  held filings and all Stage-1 artefacts (`s1_graphics/`, the Sheff and HistoryLink files, the two documented
  null files, `idx.html`/`idx.json` 403 pages) are untouched and still present. `../sources/` now holds 95 files
  (17,500,444 B) plus the `s1_graphics/` directory.
* **Known naming defect, left in place deliberately.** The four S-1/A files were first written as
  `S-1A_No1_…`, `S-1A_No2_…`, `S-1A_No4_…`, `S-1A_No6_…` (underscore), whereas the archive's convention — set by
  the pre-existing `S-1A-No3_…` and `S-1A-No5_…` — joins the form code and ordinal with a **hyphen**. The
  hyphenated, convention-correct files were then **created** (not renamed, not moved), each carrying a header
  note, and the four underscore variants remain on disk because deletion is forbidden. `cmp`-equivalent SHA-256
  over the EDGAR body confirms the pairs are **byte-identical** (bodies: 436,103 / 403,334 / 309,865 / 301,661 B,
  each matching the catalogue `size` exactly). **Cite the hyphenated names**; the underscore variants are
  duplicates in the same sense as the pre-existing unheadered `s1_original_…` copies already noted in the cache,
  and are not to be cited or counted as separate sources.
* Every new file opens with a provenance header block (rule 6): retrieval URL, access date, HTTP status,
  accession, filed date, `CONFORMED SUBMISSION TYPE`, Exchange Act file number, period of report, byte count,
  completeness statement (`</SEC-DOCUMENT>` present), component-document list with EDGAR `DESCRIPTION`s,
  headers used, wire encoding, and the catalogue row it came from.
* **Word/byte totals are body figures**, computed on the EDGAR payload after the header block, not on the file.

## 9. For the Stage-3 researcher — the three lines worth grepping first

1. **The debt pivot, precisely dated:** `8-K_event-1997-11-07_…` (Item 5, $75M Deutsche Bank facility) →
   `8-K_event-1998-04-24_…` ($275M announced) → `8-K_event-1998-05-05_…` (upsize) →
   `10-Q_Q1-1998_…` EX-4.1/4.2/4.3 (indenture, note form, registration rights) → `424B2_…` /
   `S-4_FileNo-333-56723_…` (~$326M gross) → `8-K_event-1999-01-28_…` ×2 ($500M ask) →
   `8-K_event-1999-02-03_…` (**$1.25bn 4¾% converts closed**) → `S-3_FileNo-333-78797_…` ($2bn shelf).
2. **Capability bought rather than built:** `8-K_event-1998-04-17_…` (Bookpages / Telebook / IMDB for 540,066
   Reg S shares) → `8-K_event-1998-08-03_…` (Junglee + PlanetAll merger agreements) →
   `8-K_event-1999-04-26_…`, `…-05-14_…`, `…-06-09_…`, `…-06-10_…` (Alexa, e-Niche, Exchange.com, Accept.com)
   with the matching S-8 plan registrations on disk.
3. **Founder-state documents that are contemporaneous rather than retrospective:** the two ARS shareholder
   letters (`ARS_1997-…` "But this is Day 1 for the Internet…"; `ARS_1998-…` "We predict the next 3 1/2 years
   will be even more exciting"). These outrank the Sheff *Playboy* interview — which the cache records as
   conducted 1999 / published 2000 — for any claim about what Bezos believed *while* Stage 3 was running.
