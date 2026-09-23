# Audit Sheet — Amazon.com (company_001) · Stage 1 · Run 2026-09-24
Auditor: Level-3 Verification Auditor (independent of producer: **yes** — no section of `stage_1.md` was
written by this agent; the dossiers, `_parts/`, `CORRECTIONS.md` and `adversarial_review.md` were read only
after the target text was quoted from)

**Scope of this pass: AUDIT 2 (Sources) plus the citation spot-check.** Audits 1, 3, 4 and 5 are recorded as
executed by their own runs; only AUDIT 5's coverage is stated here from `adversarial_review.md` (2026-09-23),
and it is flagged as a **partial** protocol satisfaction by that file's own admission (its reviewer had read
the corpus). This sheet does not re-run or endorse those rows.

| Audit | Result | Items checked | Failures found | Actions taken | Residual risk |
|---|---|---|---|---|---|
| 1 Chronology | **not run here** — a sibling sheet exists (`amazon_s1_audit1_chronology.md`, verdict **CONDITIONAL FAIL** on the 1993 start). Only the row below was touched by this pass | — | **1 shared with this audit:** that sheet's endpoint-snapshot row repeats "11 employees (as of **1996-01-01**)" and so inherits the same COR-03 over-claim found at DEFECT-3 | DEFECT-3 wording is written to be applied to **both** sheets | low — boundary dates are untouched by this audit's findings; the shared defect is a one-cell basis fix |
| **2 Sources** | **PASS WITH CORRECTIONS** | **24 driving claims + 6 corroboration chains + 9 COR rows + the full numeric spine (17 audited lines re-verified against the filed tables) + 11 documented nulls re-run + the claim-record appendix (432 records) at step 1** | **5 citation/attribution defects (DEFECT-1…5) + 2 presentation fixes (PRESENTATION-1, PRESENTATION-2) + the step-1 field-schema gap** | 1 dual-citation split; 3 citations re-keyed; 1 correction (COR-03) marked over-claimed; 2 claim classes adjusted; **0 claims cut for want of support** | the claim-record appendix carries **3 of the 5 fields procedure step 1 requires** → RD-024 |
| 3 Numbers | not run in this pass | ~18 rows touched incidentally while verifying claims 1-7, 17, 18 | 1 (`P39` classes a printed balance-sheet line as DERIVED) | UPGRADE-1 raised; no figure altered | basis/derivation audit of `P.2 d1-d23` outstanding — d14, d15, d16, d22, d23 were re-run here and tie |
| 4 Hindsight | not run in this pass | — | — | — | — |
| 5 Adversarial | ran 2026-09-23, **PASS (partial protocol)** | 38 challenges, 42 conflicts | 1 self-declared (reviewer had read the corpus) | none by this auditor | `stage_1.md` sentences were never attacked; this audit's findings must be fed back into the register |

**Method note (AUDIT 2 step 2 as executed).** All primary re-verification was done **locally**, by `grep -n`
against the restored originals in `01_companies/company_001_amazon/sources/`, and no large file was read whole.
Per-string presence was tested across **all four** restored filings simultaneously, so every "which document
actually contains this" question is answered by a 4-column matrix rather than by memory. Web budget used: **7 fetches attempted of the 8 allowed, 6 successful** — press release
`press.aboutamazon.com/1995/10/worlds-largest-bookseller-opens-on-the-web` (three attempts: content read; a
refetch of a stale proxy URL that returned 403 and yielded nothing; then a verbatim re-read of its telephone
numbers, ordering channels and quotations after the first pass rendered the phone number inconsistently),
press release `press.aboutamazon.com/1996/6/…`, USPTO `tsdr.uspto.gov/statusview/sn75008413`,
Verisign RDAP `relentless.com`, Verisign RDAP `amazon.com`. Two of the seven bought nothing and are recorded so
the next auditor does not repeat them. No filing, registry or press item was verified from the web where a local
copy exists.

Files actually looked at, every time:
`S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` (1,445,709 B) ·
`S-1A-No3_acc-0000891020-97-000755_filed-1997-05-09.txt` ·
`S-1A-No5_acc-0000891020-97-000839_filed-1997-05-14.txt` ·
`10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` ·
`sheff-playboy-interview_davidsheff-com-jeff-bezos.txt` ·
`historylink-essay-23230_Amazon-The-Early-Years-1995-1999.txt` ·
`ncsa-mosaic-whats-new_1995-08_kitchencloset.html` ·
`s1_graphics/INVENTORY.md` · `NULL_RESULT_wayback_1995_1996.md`.

---

## 0. Procedure step 1, re-run against the claim-record appendix (which landed mid-audit)

**Timing, stated because it changes what step 1 could test.** When this pass opened,
`01_companies/company_001_amazon/stage_1_claim_records.md` did not exist — `stage_1.md` itself says so at
l.1880-1883, and the directory listing confirmed it. It was written during this audit run (312,146 B; four
thousand-odd lines; coverage note declares **432 records**: B 93, C 29, D 16, E 29, F 24, G 30, H 30, I 16,
J 21, then K 14, L 8, M 14, N 11, O 10, P 15, Q 16, R 9, S 12, T 22, U 13). Step 1 was therefore **re-run
against it** rather than reported as unexecutable. The nine specialist dossiers remained the control text, since
the appendix states it merges `_parts/s1_claims_AJ.md` and `_parts/s1_claims_KU.md` verbatim and adds nothing.

**Result of the five-field test the procedure specifies:**

| Field required by step 1 | Present | Finding |
|---|---|---|
| publication / source date | 397 of 432 | **PASS** |
| confidence rating | 419 of 432 | **PASS** |
| verbatim passage | 397 of 432 (35 carry `NO_VERBATIM_PASSAGE_RECORDED`, which is correct for a documented null) | **PASS** |
| **tier** | **58 of 432 (13%)** | **FAIL as a field.** Tier survives only as an inline `[T1 · FACT]` token in `stage_1.md`'s tables and as a `(T01)`/`(T02)` **source-key** in the appendix — and `(Tnn)` here denotes a row of the appendix's own source register, **not a tier**, so it is not interchangeable and a reader cannot filter the appendix by evidence tier at all |
| **evidence class** | **36 of 432 (8%)** | **FAIL as a field.** The class (FACT / FOUNDER CLAIM / RETRO / DERIVED / ESTIMATE / UNKNOWN) — the single most load-bearing tag in this project, because it is what stops a founder claim being read as an audited number — is present in `stage_1.md`'s cells but almost never at the claim record that is supposed to evidence the cell |
| **retrievable URL** | **22 of 432 (5%)** | **FAIL at the record.** URLs exist, but only in `stage_1.md` §T, keyed by *source name*; a claim record therefore cannot be followed to its document without a manual join, and 12 records that cite `restoration pending` primaries have no retrievable locator anywhere |
| **archived / local-copy status** | **0 of 432** | **FAIL — field absent.** The source dossiers carried it (`Archived: EDGAR`, `Archived: sources/s1_…`); the merge dropped it. Given that the shared evidence cache was destroyed mid-run (COR-08) and six primaries are still unre-saved, this is the one missing field with an actual cost attached: nothing in the appendix records which of its own 432 claims still has a byte on disk |

**Verdict on step 1: PARTIAL PASS.** Three of five required fields are complete; three are missing at the record
level, one of them entirely. Because the missing information mostly exists one join away in `stage_1.md` §T and
in the per-cell tokens, this is a **schema failure, not an evidence failure** — nothing is unsourced. But the
appendix's own front matter asserts *"Nothing was dropped, renumbered for tidiness, or rewritten… no class was
upgraded"*, and that sentence is not accurate for the tier, class, URL and archived-status columns, which the
dossier records carried inline and the merged spine does not. **RD-024 opens on that basis.**

**What step 1 found that only step 1 could find — three records that bear directly on §2's defects:**

- **`F01`** cites the Dec-1996 statistics (180,000 accounts, >$16 million) to `S-1 Prospectus Summary/Business —
  Source date: **1997-03-24**`. The appendix has DEFECT-1 **right**, so `stage_1.md` `P60` is the lone carrier of
  the wrong accession and the correct citation can be lifted straight out of `F01`.
- **`B50`** cites 151 to the original (1997-03-24) and 256 to "S-1/A Risk Factors" (1997-05-14), i.e. DEFECT-2 is
  likewise confined to `stage_1.md` `P61`. But `B50` then writes *"nothing filed gives a 1994 or 1995 headcount"*
  in the same breath as *"the S-1/A employee series starts at 11"*, and routes to `U.17` — the same
  self-contradiction as DEFECT-3, reproduced in the appendix.
- **`L04` is the strongest single piece of evidence for DEFECT-3, and it was found only by reading the new file.**
  Its Claim is *"Headcount at 31 December 1995 was 11 employees"*; its Date is `1995-12-31`; its Source date is
  `1997-05-14`; its Tier is 1, Class FACT, Conf High — and its **Passage field quotes S-1/A No. 5 verbatim**:
  *"From December 31, 1995 to March 31, 1997, the Company expanded from 11 to 256 employees."* Only then is an
  appended `[corrected 2026-09-23: … 11 is its 1996-01-01 count …]` marker tacked on, quoting the *original*
  S-1's sentence as the authority. So the specialist read the amendment correctly, produced a defensible record,
  and had it overwritten by a correction that holds for one of the three filings carrying the number.
  `L04`'s `Corroboration: 2 (1996 10-K: 158 at 12/31/96)` is separately a small instance of §3's pattern: a
  1996 headcount does not corroborate a 1995-12-31 one.

That sequence — correct primary reading, then a register correction that removes support the record gives — is
the mechanism DEFECT-3 describes, caught in the act at the record level. It is also why RD-019 is addressed to
the register and not to a dossier.

**One convention slip worth one line:** `P13` dates the launch release `Date: 1995-10-03`, where 21 other
records use COR-11.4's required `dated 1995-10-04 (indexed 1995-10-03)` form. Folded into RD-028.

## 1. Claim-by-claim ratings (AUDIT 2 step 2)



Format: **rating — the passage actually found — where it was found.** `orig / A3 / A5 / 10K` counts are the
per-file `grep -c` results from this run.

**C-01 — net sales 1994 $0 · 1995 $511,000 · 1996 $15,746,000, and "grew from $511,000 … to $15.7 million".
→ SUPPORTED.** Selected Financial Data, orig. l.355 and the MD&A table l.1302:
`Net sales.............. $ --  $ 511  $ 15,746  $ 875  $2,230  $ 4,173  $ 8,468`, under a caption whose first
column is `FOR THE PERIOD FROM JULY 5, 1994 (INCEPTION) TO DECEMBER 31, 1994`. MD&A l.1435 verbatim:
*"Net sales grew from $511,000 in 1995 to $15.7 million in 1996."* Independently confirmed in the FY1997
10-K405 Item 6, l.1177 (`$147,758 $15,746 $ 511 $ --`). Counts: `15,746` orig 3 / A3 · / A5 3;
`Net sales grew from $511,000` 1/1/1/0. Target text is correct, and `P06` properly files 1994 as
`0 (filed as "--")` on a **179-day inception stub** rather than as a calendar year.

**C-02 — FY1995 operating loss $(304,000). → SUPPORTED.** orig. l.356 and l.1315:
`Loss from operations... (52)  (304)  (5,979)`; balance-sheet-area copy l.3500; 10-K405 l.1188. In thousands.

**C-03 — $107,000 cumulative losses and the Subchapter C election on 1995-03-31. → SUPPORTED.** Note 1,
Income Taxes, orig. l.3709-3716: *"Effective March 31, 1995, the Company, with the consent of its stockholders,
elected to be taxed under the provisions of Subchapter C of the Code. Accordingly, cumulative net losses of
$107,000 incurred by the Company as of that date have been reclassified to common stock."* Version-safe
(`Effective March 31, 1995` 1/1/1/0). Target §B.2 and §K carry "with the consent of its stockholders" verbatim.

**C-04 — 3,021,000 shares to 23 investors at ≈$0.3333 = $1,007,000. → SUPPORTED.** Part II Item 5 ¶4,
orig. l.4300-4302: *"Between December 6, 1995 and May 16, 1996, the registrant issued an aggregate of 3,021,000
shares of Common Stock to 23 investors for a consideration of approximately $.3333 per share, or an aggregate of
$1,007,000."* **COR-10's wording finding re-proved:** `23 investors` = 1/0/1→**0 in A3 and A5**;
`23 purchasers` = 0/1/1. The original alone says "investors", exactly as the register claims. Target text
correctly refuses to book the whole program inside Stage 1.

**C-05 — $345,525 at ≈$0.1717. → SUPPORTED.** Item 5 ¶2, orig. l.4287-4289: *"On February 9, 1995, July 24, 1995
and May 3, 1996, the registrant issued an aggregate of 2,012,772 shares of Common Stock to three investors for a
consideration of approximately $.1717 per share, or an aggregate of $345,525."* The target's own sharpening —
that the **aggregate itself straddles the boundary** because the third issuance is 1996-05-03 — is supported by
this text and is an improvement on the register.

**C-06 — $1,272,000 common-equity cash in CY1995. → SUPPORTED.** Statements of Cash Flows, orig. l.3644-3645:
`Proceeds from exercise of stock options, sale of stock, and advances received for common stock ... 60 1,272 231`,
columns being the 1994 stub / 1995 / 1996 (fixed by the adjacent `Net loss (52) (303) (5,777)`). Target is
correct that the line **commingles option exercises and advances** — that caution is in the filing's own caption.

**C-07 — $44,000 notes payable tracing to the July and November 1994 interest-free loans. → SUPPORTED,
tie exact.** Cash flow l.3647: `Proceeds from (repayment of) notes payable ... 44 (44) --`. Certain
Transactions l.2849-2851: *"Mr. Bezos made interest-free loans to the Company in the principal amounts of
$15,000, $29,000 and $40,000 in July 1994, November 1994 and November 1995, respectively, which were fully
repaid in August 1995, April 1995 and November 1995, respectively."* 15,000 + 29,000 = **44,000**; both 1994
loans were repaid inside CY1995, which is precisely the `(44)` in the 1995 column, and the November-1995
$40,000 drawn-and-repamed in the same month nets to zero — so the target's "$0 debt at 1995-12-31" is arithmetically
established, not assumed.

**C-08 — $10,000 founder subscription, 1,700,000 shares, "Cadabra, Inc., a Washington corporation", 1994-07-05,
Ex. 10.12. → SUPPORTED, and original-only.** Exhibit 10.12, orig. l.11446-11470: *"The undersigned, a resident of
the State of Washington, hereby subscribes for 1,700,000 shares of the common stock of Cadabra, Inc., a
Washington corporation, and agrees to pay therefor the sum of $10,000 … Dated: July 5, 1994 … Jeff P. Bezos."*
String-by-string presence re-run this pass: `Cadabra` 1/0/0/0; `1,700,000` 3/0/0/0. **COR-02 holds absolutely**,
and no row of `stage_1.md` attributes either string to an amendment (checked: every `S-1/A No. 5` citation in
the file — 77 of them — was filtered for Cadabra / 1,700,000 / sole stockholder / Ex. 10.12 / September 15 and
returned zero hits). One internal tension is correctly kept, not smoothed: Item 5 ¶1 prices **10,200,000**
shares at $10,000 (≈$.0010), a factor of six from the instrument's 1,700,000, and `U.29` + `P.2 d1/d2` carry
both bases; the six is `4-for-1 (Nov 23 1996) × 3-for-2 (Note 6)`, both stated in Note 3/Note 6 (l.3842,
l.4078) — the arithmetic in `d2` is right.

**C-09 — option plan approved by the board "and the sole stockholder" on September 15, 1994. → SUPPORTED.**
Employee Benefit Plans, orig. l.2705-2706: *"The 1994 Stock Option Plan was approved by the Board of Directors
and the sole stockholder on September 15, 1994, and amended by the Board of Directors on September 25, 1996."*
Presence `sole stockholder` = 2/0/0/0 (the second hit is the unrelated 1996 Articles of Merger). **Original
only** — COR-02 confirmed a third time.

**C-10 — Seafirst merchant account under personal guarantee from Nov 1994. → SUPPORTED.** Same passage,
l.2852-2853: *"From November 1994 to December 1996, Mr. Bezos personally guaranteed the obligations of the
Company under a merchant account with Seafirst Bank."* `Seafirst` 2/1/1/0 — so the target's citations to
`S-1 (orig.)/S-1/A No. 5, Certain Transactions` are both good, and its silence on the 10-K405 is correct
(the annual report **does not** carry this passage).

**C-11 — Wells Fargo bankcard account from Jul 1995. → SUPPORTED.** l.2854-2855: *"Since July 1995, Mr. Bezos
has personally guaranteed the obligations of the Company under a bankcard merchant account with Wells Fargo
Bank."* `Wells Fargo` 2/1/1/0.

**C-12 — company cards from Apr 1995. → SUPPORTED.** l.2856: *"Since April 1995, Mr. Bezos has personally
guaranteed company credit cards."* `company credit cards` 1/1/1/0. Target §U.24's discipline — that the filing
evidences a guarantee was **used**, never that a company-only account was **sought and refused** — is exactly
what the text supports and no more.

**C-13 — Ingram = 59% of 1996 purchases, and no long-term contract. → SUPPORTED.** Risk Factors, orig.
l.870-876: *"Ingram is the single largest supplier and accounted for 59% of the Company's inventory purchases in
1996 … The Company has no long-term contracts or arrangements with any of its vendors that guarantee the
availability of merchandise, the continuation of particular payment terms or the extension of credit limits."*
Also Warehousing and Fulfillment l.2194-2196 and Note 1 l.3696 (`59% of the Company's book` — the note's
phrasing). Presence `59% of the Company's inventory purchases` 2/2/2/1. The target's insistence that the 59% is
an **FY1996** basis and that the **1995 share is UNKNOWN** is correct and is the load-bearing point.

**C-14 — 2.5M titles offered vs up to 400,000 sourceable; distributors stocking up to 350,000. → SUPPORTED.**
orig. l.2196-2197: *"Of the more than 2.5 million titles offered by the Company, up to 400,000 are currently
supplied by book distributors and wholesalers, including Ingram and B&T."* l.1788-1789: *"Distributors serve as
the primary vendors for many retailers and carry up to 350,000 of the best-selling titles."*
`up to 400,000 are currently supplied` 1/1/1/0; `carry up to 350,000` 1/1/1/0 — present in all three S-1
versions, absent from the 10-K. The target's dating (1997 disclosure about the 1996-97 operation, and **not**
a Stage-1 measurement, against ~1,000,000 advertised in-window) is the correct basis and matches C-46/C-47.

**C-15 — ~2,200 average daily visits, December 1995. → SUPPORTED.** Prospectus Summary (heading at orig.
l.288), l.317 and repeated l.450, l.1734: *"Average daily visits (not "hits") have grown from approximately
2,200 in December 1995 to approximately 50,000 in December 1996."* `2,200` 3/3/3/0 — survives in every version,
including where the surrounding Dec-1996 statistics were replaced (see DEFECT-1). The §L qualifier "company
self-measured" is right: this is the seller's own traffic count.

**C-16 — "from January 1, 1996 to December 31, 1996, the Company expanded from 11 to 151 employees".
→ SUPPORTED as quoted; but the filed **correction built on it over-reaches** (→ DEFECT-3).** orig. l.666-667,
verbatim. Presence `11 to 151` 1/**0**/**0**/0 — **the original alone**.

**C-17 — $81,000 gross equipment and ~$17,000 inventory at 1995-12-31. → SUPPORTED; and understated by the
target** (→ UPGRADE-1). Note 2, Equipment, orig. l.3796-3805, columns `1995 / 1996` (in thousands):
`Computers and equipment $73 / $1,031 · Purchased software 8 / 134 · Leasehold improvements -- / 130 ·
[total] 81 / 1,295 · Less accumulated depreciation 24 / 310 · $57 / $ 985`. Balance sheet l.3429:
`Inventories ............... 17 571`. So **$81,000 gross and $17,000 inventory are both printed audited lines**,
and `$0 leasehold improvements at 1995-12-31` — which §B.2 and §U.10 lean on as the footprint evidence — is a
filed `--`, not an inference. `P39` classes the inventory as DERIVED/Medium-High; see UPGRADE-1.

**C-18 — $200,000 FY1995 marketing spend. → SUPPORTED.** MD&A l.1461-1462: *"Marketing and sales expenses
increased from $200,000 in 1995 to $6.1 million in 1996. Marketing and sales expenses as a percentage of net
sales were 39% in each of 1995 and 1996."* Selected Financial Data l.1307 (`Marketing and sales.... -- 200
6,090`). The 39.1% DERIVED and the 20%-gross-margin collision that §M-2 builds are correct and are the file's
strongest evidenced negative signal.

**C-19 — Bezos 1996 compensation $64,333, no bonus, no options. → SUPPORTED, with one wording tightening.**
Summary Compensation Table, orig. l.2690: `Jeffrey P. Bezos.... $ 64,333 $ -0- $ -0- $ -0-`, and l.2695-2696:
*"Mr. Bezos does not currently hold options to purchase capital stock of the Company."* The table's own
introduction (l.2669-2671) scopes it to *"the year ended December 31, 1996"* — post-boundary, which the target
states (`P53`, `U.17`-adjacent). Two precision points for the appendix: (i) "no options" is a **present-tense
statement of position as of the filing**, not a disclosure that none were ever granted; the target's wording at
§B.1 ("no options held") is defensible but should read "holds none as filed"; (ii) "no bonus" is the `-0-` in
the `BONUS($)` column, which is sound. The **conclusion the target draws — that Stage-1 pay is UNKNOWN because
the table begins at FY1996 — is exactly right** and is the more important finding.

**C-20 — D. E. Shaw tenure Dec 1990–June 1994, senior VP from 1992. → SUPPORTED verbatim.** Bio, orig.
l.2431-2436: *"From December 1990 to June 1994, Mr. Bezos was employed by D.E. Shaw & Co., a Wall Street
investment firm, becoming Senior Vice President in 1992. From April 1988 to December 1990, Mr. Bezos was
employed by Bankers Trust Company, becoming Vice President in February 1990."* `becoming Senior Vice President
in 1992` 1/1/1/1. The target's related findings also hold: **CEO only from May 1996** (`Chief Executive Officer
since May` 1/1/1/1 — present in all four, so §B.1's citation to S-1/A No. 5 is legitimate here), and the
"youngest SVP" superlative is a **filing null**, not a filing fact (`U.35`).

**C-21 — trademark "AMAZON", applied 1995-10-23, SN 75008413, registered 1997-07-15, no opposition.
→ SUPPORTED.** USPTO TSDR `statusview/sn75008413`, retrieved this pass: Word Mark **AMAZON**; Serial Number
**75008413**; Registration Number **2078496**, **Registered Jul. 15, 1997**; Filing Date **Oct. 23, 1995**;
International Class **042**; goods *"computerized on line ordering service featuring the [wholesale and] retail
distribution of books"*; Current Status **"LIVE/REGISTRATION/Issued and Active"**; **no opposition and no
cancellation proceeding recorded**; owner of record **AMAZON TECHNOLOGIES, INC.** — a later entity, which is
why §I.4's caveat "current registrant of record is a later Nevada entity" is required and is correct. The
filing-side half is separately confirmed: A5 cover l.285-287 *"The Company has applied for federal registration
of the marks 'AMAZON.COM' and 'AMAZON.COM BOOKS.'"* — **applications, no registration**, and note this covers
the composite marks only; the bare "AMAZON" word mark is evidenced by TSDR alone, exactly as §B.1 splits it.
The §I.4 wording ruling ("not **establishable in the Stage-1 record**", never "never happened") is the correct
limit and the register's zero-pending-proceedings check is consistent.

**C-22 — domain creation dates `relentless.com` 1994-09-25 and `amazon.com` 1994-11-01. → SUPPORTED.**
Verisign RDAP, retrieved this pass: `relentless.com` (handle `4854190_DOMAIN_COM-VRSN`) `{"eventAction":
"registration","eventDate":"1994-09-25T04:00:00Z"}`; `amazon.com` (handle `281209_DOMAIN_COM-VRSN`)
`{"eventAction":"registration","eventDate":"1994-11-01T05:00:00Z"}`. Both dates confirmed to the day. The
target's two cautions are the right ones and should not be quietly dropped later: pre-1996 `.com` "created"
values can reflect a later migration, and **the registrant is not verifiable** — RDAP names no 1994 holder, so
§B.2's "Medium-High (date) / Low (holder)" is correctly split.

**C-23 — the 1995-10-04 press release's claims. → PARTIAL.** This is the one claim in the set that does not
survive intact, and the defect is in the **attribution**, not the fact.

*Confirmed present in the release* (verbatim re-read): dateline *"SEATTLE, WA (October 4, 1995)"*; headline
*"World's Largest Bookseller Opens on the Web"*; *"all 50 states and more than 45 countries"*; *"first four
weeks of operation"*; *"more than one million different titles"*; discounts of *"10-40 percent"*; *"Netscape
and Yahoo have each included Amazon.com in their 'What's New' and 'What's Cool' lists"*; *"via UPS or Airborne
Express"*; *"Eyes & Editors" personal notification service*; telephone *"(206) 622-2335"* (a second number,
(206) 223-1606, is the media contact — so `§Q`'s single number is the right one); and two Bezos quotations
including *"Our motto is 'If it's in print, it's in stock'"* and *"We are able to offer more items for sale than
any retailer in history, thanks entirely to the Internet."*

*NOT present in the release:* **nine mailboxes**, **toll-free ordering**, **fax ordering**, and **e-mail
ordering**. On ordering channels the release says only *"customers order online and books are delivered directly
to their doors"* — i.e. it is affirmatively **narrower** than the target's multi-channel picture. The nine
addresses are the **S-1's**, at orig. l.2174: *"Amazon.com offers nine e-mail addresses to enable customers to
request information and to encourage feedback and suggestions."* The toll-free line is the S-1's too, l.2179-2180:
*"Amazon.com also offers a toll-free line for customers who are reluctant to enter their credit card numbers
through the Web site."* Fax appears in **neither**: `fax` is absent from the ordering text of all four filings
(the only `facsimile` hits in the S-1 are signature and notice boilerplate), and it reaches Stage 1 only from
the Nov-1995 Knight Ridder item. So the release corroborates eight of the ten sub-claims and supplies none of
the last two, while **actively contradicting the "nine mailboxes" attribution**.

**C-24 — "commenced offering products for sale on its Web site in July 1995 … from inception through July 1995
the Company had no sales". → SUPPORTED verbatim.** MD&A Overview, orig. l.1372-1374: *"The Company was
incorporated in July 1994 and commenced offering products for sale on its Web site in July 1995. For the period
from inception through July 1995, the Company had no sales and its operating activities related primarily to the
development of the necessary computer infrastructure…"* Corroborating sentences in the same instrument:
l.484 *"began selling books on its Web site in July"* and l.297 *"Since opening for business as 'Earth's Biggest
Bookstore' in July 1995"*. Version-safe (`commenced offering products` 1/1/1/2). **`U.1` is the best single
entry in the volume**: it keeps "July 1995 per the filings" and the release's "first four weeks" apart as two
company statements of different objects, flags that "through July 1995" is itself ambiguous as to whether July
recognised anything, and refuses a day. **No primary document in this corpus supports 16 July.**

**Tally: 23 SUPPORTED, 1 PARTIAL (C-23), 0 UNSUPPORTED.** Nothing in the target text is presented as fact
without a document that contains it; every failure found is a **citation pointing at a document that does not
contain the figure**, which is a different and more correctable defect.

---

## 2. Citation defects found while verifying the above

### DEFECT-1 (AUDIT 2 step 2 failure) — `P60` attributes to S-1/A No. 5 figures that amendment replaced
`stage_1.md` l.774 (`P60`, 1996-12 / 1996-12-31, average daily visits ≈50,000, ≈180,000 accounts,
>$16,000,000 cumulative) cites **S-1/A No. 5, 1997-05-14**. Tested: `50,000 in December 1996` = **0** in A5;
`180,000` = **0** in A5; `more than $16 million` = **0** in A5. S-1/A No. 5 superseded all three and says, at
l.336-339: *"Through March 31, 1997, Amazon.com had sales of more than $32 million to approximately 340,000
customer accounts in over 100 countries. Average daily visits (not "hits") have grown from approximately 2,200
in December 1995 to approximately 80,000 in March 1997."* The 50,000 / 180,000 / $16M trio exists only in the
**original** (l.447-450). **Action:** re-key `P60` to `S-1 (orig.), 1997-03-24, Prospectus Summary`; if the
amendment is wanted for its own numbers, they are 80,000 / 340,000 / >$32M **through 1997-03-31** and belong on
a separate post-boundary row. Note the useful by-product: this is a second, independent instance of the same
LA Times 1997-07-20 datum the target already quotes ("lost $9 million … to generate sales of $32 million"),
which is now confirmed against the filing that produced it.

### DEFECT-2 (AUDIT 2 step 2 failure) — `P61` attributes 151 to S-1/A No. 5
`stage_1.md` l.775: *"Employees (S-1/A No. 5 **151** vs 10-K405 **158**)"* and source cell `S-1/A No. 5;
10-K405 FY1997`. Tested: `grep -n "\b151\b"` on S-1/A No. 5 and on S-1/A No. 3 returns **nothing** in either.
151 exists only in the original, twice: l.667 (`expanded from 11 to 151 employees`) and l.2364 (*"As of
December 31, 1996, the Company employed 151 full-time employees."*). The 158 side is correct
(10-K405 l.729: *"growing from 158 employees as of December 31, 1996 to 614 employees as of December 31,
1997"*). **This is the exact error class `COR-02` exists to prevent, re-introduced at merge** — and it survives
in the P-table while `U.17` (l.1402) states the fact correctly ("in the S-1 (twice, and '151 full-time
employees')"), so the appendix now contradicts itself. **Action:** `P61` → `S-1 (orig.), 1997-03-24, Risk
Factors + Management; vs 10-K405, 1998-03-30`. Post-boundary, so no Stage-1 cell moves.

### DEFECT-3 (**most important**) — COR-03 is over-claimed, and three rows cite a filing that has no such number
`stage_1.md` states in five places (§B.1 l.142-143 area, §B.2 l.162, §D.1 l.226, §L l.557, §P l.752, §R
l.863, §Q l.851) that the employee count of 11 is **"per the filing: at 1996-01-01"**, not at 1995-12-31, on
the authority of the original S-1's phrasing, and `P42`/`§R` additionally cite `S-1/A No. 5, Risk Factors;
10-K405` as co-sources for the 11.

Both halves are wrong, in opposite directions:

1. **S-1/A No. 3 and S-1/A No. 5 date the same 11 to 1995-12-31.** A5 l.794-796: *"From **December 31, 1995** to
March 31, 1997, the Company expanded from **11** to 256 employees."* A3 l.797 is identical. The count was
**re-based, not re-counted, between the March and May 1997 filings** — and the later, amendment-basis wording
places the 11 squarely on the Stage-1 boundary date. The dossier rendering that COR-03 set out to correct
("11 employees at 1995-12-31") is therefore **affirmatively supported by two separately-accessioned filings**,
and the correction as written removes support the record actually gives.
2. **The FY1997 10-K405 contains no 11 at all.** Its only headcount series begins one year later (l.729, 158 at
1996-12-31 → 614 at 1997-12-31). Citing it for the 11 is a defect of the DEFECT-2 class.

**Corrected wording (apply at all five locations plus §U.17, which inherits the same over-claim):**

> **11 employees.** Three filings carry the figure on two different as-of bases. S-1 (orig.), 1997-03-24, Risk
> Factors: *"From January 1, 1996 to December 31, 1996, the Company expanded from 11 to 151 employees"* — i.e.
> 11 at **1996-01-01**, and not styled "full-time" there. S-1/A No. 3 (1997-05-09) and S-1/A No. 5 (1997-05-14),
> same Risk Factors: *"From December 31, 1995 to March 31, 1997, the Company expanded from 11 to 256 employees"*
> — the same 11 at **1995-12-31**. The FY1997 10-K405 discloses no 1995 headcount. **The count 11 is High; the
> as-of date is filed twice and inconsistently, so the boundary placement is a conflict (U.17) and not a
> correction.** Immaterial either way: 1995-12-31 and 1996-01-01 are one day apart, and the Stage-1 reading does
> not change.

**Consequential instruction to CORRECTIONS.md:** amend **COR-03** to read as a *dating conflict between two
bases of one filing family*, not as a correction of the dossiers, and note that the dossiers'
"11 at 1995-12-31" is the **amendment** basis. `adversarial_review.md` row E-01 carries the same over-claim and
should be re-keyed when next touched. This does **not** reopen COR-01/COR-02, both of which were independently
re-proved this pass.

### DEFECT-4 — `§F.2 Trust devices` merges two sources into one apparent corroboration
`stage_1.md` l.331 lists *"Published phone number; a toll-free line maintained specifically for those refusing
to type a card; nine e-mail addresses; ordering by phone or e-mail"* under the single dual citation
`S-1 (orig.) [T1 · FACT]; press release dated 1995-10-04 [T1]`. As C-23 shows, the release supplies the phone
number and nothing else on that list, and it is affirmatively narrower on ordering channel ("order online"). A
dual citation over a mixed list is how single-source facts acquire a second source, and it is the one live
instance of the pattern §3 is about. **Action:** split the cell — S-1 (orig.) l.2174, l.2179-2180 for the nine
addresses and the toll-free line; press release 1995-10-04 for the published number and for online ordering
only; keep fax on the Knight Ridder item at Medium. Everything else in the file already does this correctly
(§D.1 l.229 and §E.3 l.302-304 cite the S-1 and the Nov-1995 press for those facts), so the fix is local.

### PRESENTATION-1 — `§A` opex component list double-counts
l.91: *"operating expenses $406,000 (marketing $200,000; product development $171,000; G&A $35,000; advertising
$30,000)"*. Advertising is not a fourth component: Note 1 l.3734-3735 reads *"For the years ended December 31,
1995 and 1996, the Company incurred advertising expense of $30,000 and $3.4 million, respectively"* — a
disclosure **within** marketing and sales. `P.2 d10` ties 200+171+35 = 406 correctly. **Action:** render
advertising as "(of which advertising $30,000, Note 1)".

### PRESENTATION-2 — the impossible recital is not confined to Exhibit 10.13
`U.15` (l.1359-1382) treats Ex. 10.13's *"Amazon.com, Inc. … a Delaware corporation"* as a one-off drafting
defect. Checked directly: **Ex. 10.15 (Kaphan, "this 8th day of August 1995") carries the identical recital**,
orig. l.12373-12376, as does Ex. 10.13, l.11489-11491, and §K.4 l.511 cites Ex. 10.15 without the caveat.
**Action:** broaden `U.15` to "the conformed Shareholder's Agreement preambles (Ex. 10.13 and Ex. 10.15, at
minimum)" and carry the conforming caveat wherever those exhibits are cited for a date. Strengthens rather than
weakens the finding: a recurring anachronism across a 1996-97 exhibit set is documentary evidence of
conforming, where one preamble is only a suspicion.

---

### DEFECT-5 (**highest practical reach**) — all three citation defects have already propagated into `quantitative.csv`

The nine structured deliverables were written alongside this audit, and the defects are in them too — which
matters because the CSVs are what AUDIT 3 cross-foots and what Stage 2 will ingest mechanically:

| CSV row | Text as written | Required fix |
|---|---|---|
| `quantitative.csv` **l.71** | `1995-12-31, Employees at the Stage-1 boundary, 11, persons, "S-1/A No. 5 Risk Factors; Form 10-K405 FY1997", 1997-05-14` — with a note asserting "11 is a 1996-01-01 count" | source cell is right that A5 carries the 11 and **wrong to add the 10-K405**; and the note contradicts the row's own source, because the A5 wording it cites dates that 11 to **1995-12-31**. Replace the note with DEFECT-3's two-basis text |
| `quantitative.csv` **l.96** | `1996-12-31, Employees (S-1 151 vs 10-K405 158), 151 / 158, S-1/A No. 5; Form 10-K405 FY1997, 1997-05-14` | 151 is **absent from S-1/A No. 5** → `S-1 (original), 1997-03-24; Form 10-K405, 1998-03-30` (same fix as DEFECT-2) |
| `quantitative.csv` **l.97** | `1996-12-31, Cumulative customer accounts and cumulative sales, ≈180,000 accounts; >$16,000,000, S-1/A No. 5, 1997-05-14` | both figures are **original-only** (A5 reports 340,000 / >$32M through 1997-03-31) → `S-1 (original), 1997-03-24` (same fix as DEFECT-1) |

Because `stage_1.md` `P42`/`P60`/`P61`, the appendix, and `quantitative.csv` now carry the same three errors in
three formats, the repair must be applied **once and propagated**, and any of the three corrected in isolation
will create a new internal contradiction. Recommend the merge treat DEFECT-1/2/3/5 as one change set.

One unrelated, content-neutral inconsistency noted in passing while reading the CSV: l.81 labels the IDC $318M
row `S-1 (original)` but stamps its source date `1997-05-14`. Re-checked — the figure is in **both** versions, so
nothing is mis-sourced; it is a label/date mismatch and simply says a mechanical accession-name-vs-date check
across the CSVs is worth running once.



## 3. False corroboration (AUDIT 2 step 3) — six chains traced; all six already collapsed in the target

Method: for each anecdote, list the distinct URLs cited across the 11 dossiers' records, then chase each URL to
its own stated source until the lineages fuse. Where N sites resolve to M lineages, N−M records were being
double-counted as corroboration.

**FC-1 — "16 July 1995 launch, $12,000 first week, $14,000 second week". 10+ records → 1 lineage.**
Cited across `A-62, A-63, A-timeline-313, B-48, C-40, D-11, D-242, E-77, F-metrics-282/283, G-17` on five
different sites (HistoryLink, aboutamazon, Wikipedia, Seattle Times 2005, Stone). Resolution: the **dollar
figures and the day** come from one place — HistoryLink Essay 23230, verified locally at
`historylink-…txt:75` — *"On July 16, 1995, the website had its official launch. … With $12,000 worth of orders
in the first week and $14,000 in the second week"* — which footnotes **Stone 2013**; the same numbers appear in
that essay's opening paragraph (`:15`). Wikipedia's variants ("$20,000 a week within two months", "about $1
million in the first 30 days") are **mutations of the same item**, not checks (`D-12`, `U.9`). Re-verified this
pass: none of the four filings contains a first-week figure, and `August 1995` appears only as a loan-repayment
date and two exhibit dates. **Verdict: FALSE CORROBORATION CONFIRMED; target already collapsed it** (§F.1 V4
Low; §U.9; §M-10). One dossier error is *not* inherited and should be noted as resisted: `B-48` graded the
launch "Medium-High, Corroboration: 2" by counting Sheff's *"On July 15, we sent e-mail to those 300 friends and
family"* (`sheff-…txt:241`) as an independent second source for a 16-July "official launch" — the two are the
**same event told from one founder's mouth at different dates**, and `stage_1.md` l.839 correctly holds both at
Low.

**FC-2 — "$1.1 million from 22 friends and family at $50,000 each, ~20% for a ~$5M valuation". 4+ sites →
2 lineages, both the founder.**
Cited at `A-90, B-47, B-123, B-373, B-409, B-587` across HistoryLink, GeekWire 2013 (quoting CBS/60 Minutes),
Business Insider 2016 and LA Times 1997. Resolution: `historylink-…txt:87` carries the whole package verbatim —
*"Bezos pitched Amazon to 60 potential backers … 22 investors supported the venture at the $50,000 level, which
brought in $1.1 million … Bezos gave up 20 percent"* — and HistoryLink's own footnote is the **GeekWire/CBS
item**, so those two sites are one lineage; Business Insider is Bezos again; the only element reaching back to
1997 is the round's existence. The **audited counter-figure was re-verified independently** (C-04): 23
purchasers, $1,007,000, $0.3333, **1995-12-06 → 1996-05-16**, with no per-investor amount and no "friends and
family" label anywhere in the filings. **Verdict: CONFIRMED; target handles it well** (§B.2 l.164, §K.5(a),
§U.8) — including the two disciplines that matter: the near-agreement ($1,007,000 vs $1.1M; 23 vs 22) is
recorded but **not** treated as corroboration, and $50,000-each is refused. `P.2 d22`'s $43,783 is correctly
labelled an arithmetic mean, not a cheque size.

**FC-3 — "The first book sold on Amazon was Hofstadter's *Fluid Concepts*, to John Wainwright, 3 April 1995,
$27.95". 6 sites → 2 lineages that contradict each other.**
`D-08, D-09, A-71, A-72, B-114, F-69, G-15` cite MarketWatch 2015, The Atlantic 2012, NY Daily News,
aboutamazon.com, the 2007-archived IR timeline and Wikipedia. Resolution: the three journalistic items are one
interview cycle (Wainwright/Kaphan, and both name an Amazon spokesperson); the company page and the 2007 IR row
are the company's own commemoration — and **the two lineages disagree on the date**, which is the tell: the
buyer says 3 April 1995, the company says July 1995. Re-verified: `shipped our first book` = **0** in all four
filings; no filing names a first customer or title. **Verdict: CONFIRMED; target collapsed it** (§F.1 V1-V5 +
IR row; §U.2 refuses to certify any individual and notes that only $27.95 is common across versions, and that
it is a list-derived price).

**FC-4 — "The Web was growing 2,300% a year, and that triggered the founding". ~22 records, 12+ cited sites →
1 origin.**
The highest-density example in the corpus: rows in A, B, C, G and K attribute it variously to LA Times
1997-07-20, Sheff 1999/2000, Stone Ch.1, HistoryLink, the Academy of Achievement 2001 address, Business Insider
2016, Tier-4 social clips, and (as counter-evidence) W3C/Netcraft. Every affirmative instance is Bezos, at
increasing distance from 1994. Re-verified this pass across the whole filing family:
`2,300` = **0/0/0/0**, `percent a year` = **0/0/0/0**, `roadmap` = 0, `business plan` = 0, `91 pages` = 0. The
target's treatment (§H l.403-410 + §U.6) is exemplary and is the model for the others: classified as a founder
claim of unestablished provenance, genealogy logged (1997 journalism quoting him → 2000 first-person → 2013
book reconstructing it from *Matrix News* byte and packet **factors** ×2,057/×2,560), no `§P` row printed, and
the defensible residue stated separately ("a 1993-94 traffic series showing roughly 2,000-fold annual change").

**FC-5 — "The Seattle garage, four employees, Bezos wrote the software, the 200 sq ft warehouse, 'One million
titles, consistently low prices' in blue underlined text". ≥5 sites → 2 lineages, internally contradictory.**
Sheff is the single node for the garage and the writing: `sheff-…txt:23` *"Then he set up shop in Seattle in the
garage of his rented home, with four employees. Bezos wrote the software for the bookselling operation as the
rented furniture was being delivered"*; `:237` the B&N-café meetings; `:245` *"a real office with a
400-square-foot warehouse"*. HistoryLink supplies the competing details: `historylink-…txt:45/51` the Bellevue
garage and the Home Depot door desks, `:63` *"a small office and a 200-square-foot warehouse"* plus the blue-
underlined tagline, and it footnotes Stone and GeekWire. The aboutamazon "humble beginnings" photo page restates
the same material. So the cluster is **Sheff on one side, Stone/Kaphan on the other, and they disagree on the
two numbers the anecdote is about** (4 employees against a filed 11; 400 sq ft against 200), which is the
strongest possible proof they are not corroborating each other. **Verdict: CONFIRMED; target collapsed it**
(§B.2 Premises, §U.10, §U.26, §U.27, §E.1 l.270, §R Employees "memoir 'four' is Low").

**FC-6 — "His parents put in almost $250,000" — a derived restatement of the filings, counting as an
independent second source.** (Bonus chain; the sharpest of the six.)
`B-40`, `B-110`, `B-122`, `B-372`, `B-441` carry $150,000 (HistoryLink citing Stone p.33) and "almost $250,000"
(Wikipedia citing Metcalf, LA Times 2018-08-01). Resolution: the 2018 figure is **reverse-engineered from later
shareholdings**, and `B-110` records that Wikipedia's own wikitext is an inflation template around **$245,573**.
That number is the filings: the two dated 1995 parental purchases re-verified this pass at orig. l.2864-2865
(`582,528` to Miguel A. Bezos, `847,716` to the Gise Family Trust, both `@ $0.1717`) and Ex. 10.13/10.14 give
$100,019.06 + $145,552.83 = **$245,571.89**. The "newspaper analysis" and the "primary record" are therefore the
**same number**, one being arithmetic performed on the other — the textbook false-corroboration shape.
**Verdict: CONFIRMED; target collapsed it** (§B.1 l.147, §K.5(c), §U.8, `P.2 d4/d5/d23`), and correctly keeps
the founder's own only quantification — *"a significant portion of their life savings"* — as a claim with no
figure.

**Count: 6 false-corroboration chains traced; 6 confirmed; 6 already collapsed in the target text; 1 new
instance of the same pattern found inside the appendix (DEFECT-4).** No chain required re-tiering a Stage-1
conclusion, because in every case the filing or the register had already isolated the single origin — which is
the strongest thing this volume can be said to have done.

---

## 4. Filed corrections: do they still hold? (re-tested against the restored documents)

| ID | Claim of the register | Result of this re-test | Evidence applied |
|---|---|---|---|
| **COR-01** | `0000891020-97-000839` is S-1/A No. 5 (1997-05-14), not the S-1; the original is `0000891618-97-001309` (1997-03-24); the 9-May item is **No. 3**; the FY1997 report is form **10-K405** | **HOLDS** | Read from each restored file's own Registrar header: A5 `Filing date per EDGAR 1997-05-14`, A3 `1997-05-09`, 10-K `form type "10-K405"`, `Period of report 1997-12-31`. `stage_1.md` front matter matches exactly |
| **COR-02** | "Cadabra, Inc., a Washington corporation", the 1,700,000 subscription and "the sole stockholder on September 15, 1994" exist **in the original only** | **HOLDS — re-proved string-by-string** | `Cadabra` 1/0/0/0 · `1,700,000` 3/0/0/0 · `sole stockholder` 2/0/0/0 (orig/A3/A5/10-K). All 77 `S-1/A No. 5` citations in the target filtered: **none** attributes these three facts to an amendment |
| **COR-03** | "11 employees" is the filing's **1996-01-01** figure, not 1995-12-31; 151 is post-Stage-1 | **DOES NOT FULLY HOLD — over-claimed.** True of the original; **contradicted by S-1/A No. 3 and No. 5, which date the same 11 to 1995-12-31.** The 151-is-post-boundary half holds | A5 l.794-796 and A3 l.797: *"From December 31, 1995 to March 31, 1997, the Company expanded from 11 to 256 employees."* → **DEFECT-3**; amendment text supplied above |
| **COR-04** | The four bracketed "web page pictures" are a printer's art-direction instruction; zero images exist; the "2.5 million titles"/"40% discount" captions are 1997 numbers | **HOLDS — re-proved arithmetically, independently** | `PUBLIC DOCUMENT COUNT: 38` at orig. l.32; `grep -c "^<DOCUMENT>"` = **38**; `<TYPE>GRAPHIC` = **0**; `<img` = **0**; `.gif`/`.jpg` = **0**; file 1,445,709 B. `s1_graphics/INVENTORY.md` confirms 41 index rows / 38 unnamed / PDC 38 "yes", and "Images recovered: 0". Bonus confirmation: A5's cover still carries the instruction form *"PICTURE OF THE COMPANY'S AMAZON.COM JOURNAL WEB PAGE, ACCOMPANIED BY TEXT"* (l.282-284) — singular "PICTURE", an instruction, not a file |
| **COR-05** | `wb_amazon.html` is a 2006-05-22 capture; no root capture before 1998-12-12 (a bare 302); earliest rendered 1999-08-28; 1996 deep-path absence **unanswered, not proven** | **HOLDS (not re-fetchable offline; register is self-consistent and the four 504s are correctly preserved as failures, not nulls)** | `NULL_RESULT_wayback_1995_1996.md` (4,427 B) restored; `research/cdx_prefix96.txt` holds a 504 page; §S row 2 and §U.21 both refuse to convert the timeout into a null. §T records `www.` vs bare host as **one** test |
| **COR-06** | Sheff is a **1999 interview, published 2000** (Playboy), not a 1994 Wired profile; no contemporaneous founder-state interview exists for Stage 1 | **HOLDS** | File header, `sheff-…txt` block: *"Publication / issue date : conducted 1999; published 2000 (Playboy)"*. Internal anachronisms confirmed on the first page: zShops-era framing, a **$22 billion** valuation, *"41 percent share"*, 1997 sales of $147M. The §N consequence — that founder *reasoning* for 1994-95 is unrecoverable and the only in-window Bezos words are a company-issued PR quotation — is exactly what the corpus supports |
| **COR-07** | HistoryLink 23230 is a **2025-04-07** essay, Tier 2 at best; the NCSA Mosaic page is genuinely August-1995 and is a technology artifact only | **HOLDS** | Header *"Publication / issue date : essay posted 2025-04-07"*; its Stage-1 detail demonstrably runs to Stone (`:57`, `:75`, `:87` all footnote-anchored). Mosaic header: *"Publication / issue date : August 1995"* plus the recorded negative finding that the only "Amazon" in 984 KB is the **river** — and §H/§I.4/§J all use it only for the environment (3,084 entries), never for the company |
| **COR-10** | The first round **is** disclosed: 3,021,000 / 23 / ≈$.3333 / $1,007,000, 1995-12-06 → 1996-05-16; plus $345,525 at ≈$.1717; $8,000,014 and $200,000 are 1996 Series A; original says "investors", A5 says "purchasers"; E's "nothing disclosed" was wrong | **HOLDS on every element** | Item 5 ¶¶1-4 verbatim at orig. l.4281-4303; `23 investors` 1/0/0/0 vs `23 purchasers` 0/1/1/0 — the wording difference is real and one-directional; `8,000,014` 1/1/1/0. §B.2's "Adjudicated at merge" note (l.169-176) records the deletion of E's claim rather than hiding it, which is what COR-10 action 1 required |
| **COR-11.1** | $511K must be cited to the filing, not Sheff; re-tier 2→1, class FOUNDER CLAIM→FACT | **HOLDS, and the need for it is real** | The figure **is** in Sheff's own editor's preamble (`sheff-…txt:25`: *"Amazon.com's sales of $511,000 in 1995 were impressive"*), so a dossier citing Sheff would have looked reasonable; the audited lines (C-01) are the correct authority and `P23`/`§K` say so explicitly |
| **COR-11.2** | 151 vs 158 must each carry its own document | **PARTIALLY BROKEN in the target** — 158 is correctly cited; 151 is cited to the wrong accession | → **DEFECT-2** |
| **COR-09** | the forbidden-figure list must not reappear as Stage-1 fact | **HOLDS — full scan** | Every occurrence in `stage_1.md` of "July 16" / 16 July · $12,000 / $14,000 · 2,300 · Cadamia · $50,000 each · $250,000 · Bulgaria · Washington Post · "shipped our first book" · "91 pages" · "Future of Computer Stores" · "roadmap" was read in context: **all are inside a legend, null or rebuttal frame**, none is asserted. Independent filing confirmation: `Cadamia` 0/0/0/0; `shipped our first book` 0/0/0/0; `MacKenzie` and `Tuttle` **0/0/0/0**, so the §B.1 established null stands as written |

**Nothing that the corrections register fixed has been re-introduced into the target text, with two
exceptions, both in the P-table's post-boundary rows and both traceable to the merge rather than to a dossier:
`P61`'s 151 (the COR-02 error class) and `P60`'s Dec-1996 trio (a superseded-datum error the register has no
rule for yet).** The third item, COR-03's over-reach, is a defect **in the register itself**, not a
re-introduction — and it is the reason RD-019 exists.

## 5. Founder-claim density by section (AUDIT 2 step 4)

Sections whose material claims rest primarily on founder or employee retrospective telling: **§C** (the problem
and the 1994 plan), **§N** (decisions — the Rationale and Expected-result columns), **§O** (counterfactuals),
**§F.1** (the first sale). All four are correctly labelled, and two carry an explicit front-loaded limit
statement: §C.2 caps the planning document at *evidence rung 3, founder description*, and §N opens with the
COR-06 finding that *"the founders' reasoning in 1994-95 is largely unrecoverable."* §O.2 goes the right way
round on the temptation and records CD-ROM as **UNKNOWN rather than as a rejected alternative**. No section
rests on founder storytelling without saying so. **Contemporaneous vs retrospective is distinguished at every
one of these points** — and the volume's answer to its hardest question is the honest one: the only
contemporaneous Bezos words in the window are a publicity quotation (1995-10-04), which is dated, tiered
`T1 as artifact / T4 as 1994 evidence`, and never mistaken for independent reporting.

**Sections that are *not* founder-carried, and should be protected in any later edit:** §D.1 Costs and Revenue,
§G, §I.4, §K, §L rows 3-5, §M, §P and §R — these run on audited lines. §M is the file's most valuable section
precisely because every one of its eleven negative signals is an audited number or a filed disclaimer, not a
judgment.

## 6. Legal boundary (AUDIT 2 step 5)

Clean. No material sourced from leaks, private communications or confidential documents. The one proximity
item — the **1996-06-19 subrogation agreement filed under confidential treatment**, §U.24 — is recorded only as
existing, redacted and UNKNOWN in substance, and labelled post-boundary. The 1998 proxy that could name
MacKenzie Tuttle is recorded as an absent primary (§S), not worked around. No DEEP PUBLIC-SOURCE EVIDENCE label
was required, because nothing in the volume needed one: the intrusive material here is registry and filing data
(RDAP, TSDR, EDGAR), which is ordinary public record and is tiered accordingly.

## 7. Cross-cutting observations (positive output)

Three things this pass confirmed that are worth stating because later stages will rely on them:
(i) **the $511K spine is self-corroborating.** Note 1's international figure ($198,000 / 38.75% of $511,000)
against MD&A's "approximately 39%" is an internal cross-check inside one instrument, and `P.2 d12` uses it
correctly as a check rather than as a second source.
(ii) **the cash bridge ties to the dollar.** `52 − 232 − 52 + 1,228 = 944; 52 + 944 = 996` (`d14`) reproduces the
audited closing cash from four other filed lines, which is the strongest single integrity test available on this
document and it passes.
(iii) **the 1994 and 1995 zeros are audited facts, not retellings.** The 10-K405's own Item 6 columns print the
inception stub as `--` across net sales, cost of sales, gross profit **and marketing and sales**, with $52,000
of operating expense and a $(52) loss — so §M-1's "a full year of no revenue" is as hard as the volume claims,
and it is the single most under-used datum in Amazon mythology.

---

## Claims cut or downgraded

| Claim ref | Was | Now | Why | Evidence applied |
|---|---|---|---|---|
| **U.17 / §B.1 / §B.2 / §D.1 / §L / §P `P42` / §Q / §R (11 employees)** | "11 employees (per the filing: at **1996-01-01**)"; co-cited to `S-1/A No. 5, Risk Factors; 10-K405` | **"11 employees — filed on two inconsistent as-of bases: 1996-01-01 (S-1 orig.) and 1995-12-31 (S-1/A No. 3 and No. 5). 10-K405 discloses no 1995 headcount."** Count stays High; the date becomes a stated conflict, not a correction | S-1/A No. 5 l.794-796 and S-1/A No. 3 l.797 read *"From December 31, 1995 to March 31, 1997, the Company expanded from 11 to 256 employees"*; `grep` for any 11-employee statement in the 10-K405 returns **nothing** | Local: orig. l.666-667 · A5 l.794-796 · A3 l.797 · 10-K405 l.729. → **DEFECT-3**, COR-03 amended |
| §P `P42`, §R Employees — `10-K405` co-citation | cited as a source for the 11 | **cut** | the FY1997 annual report has no 1995 headcount | 10-K405 headcount text begins at 158 / 1996-12-31 |
| §P `P61` (1996-12-31 employees) | "S-1/A No. 5 **151** vs 10-K405 **158**" | **"S-1 (orig.), 1997-03-24 **151** vs 10-K405, 1998-03-30 **158**"** | `151` occurs **zero** times in S-1/A No. 3 and No. 5; it is original-only (l.667, l.2364). S-1/A No. 5 instead gives **256 at 1997-03-31** | 4-file presence matrix. → **DEFECT-2**; COR-02 error class re-introduced |
| §P `P60` (Dec-1996 visits / accounts / cumulative sales) | "≈50,000; ≈180,000 accounts; >$16,000,000 — S-1/A No. 5, 1997-05-14" | **re-keyed to S-1 (orig.), 1997-03-24, Prospectus Summary (l.447-450)**; and if the amendment is wanted, its own numbers are 80,000 visits at 1997-03-31, ~340,000 accounts and >$32M cumulative, which need a separate post-boundary row | S-1/A No. 5 l.336-339 superseded all three figures with March-1997 statistics; `50,000 in December 1996`, `180,000` and `more than $16 million` each return **0** in A5 | Local grep matrix. → **DEFECT-1** |
| §F.2 "Trust devices" | single dual citation `S-1 (orig.); press release 1995-10-04` across a mixed list including **nine e-mail addresses** and the **toll-free line** | **split by fact:** S-1 (orig.) l.2174 (nine addresses) and l.2179-2180 (toll-free line); press release 1995-10-04 for the published number and **online ordering only**; fax stays on the Nov-1995 Knight Ridder item at Medium | The release contains neither "nine mailboxes" nor any e-mail/toll-free/fax ordering language; it says *"customers order online"*, so it is narrower than the cited list, not additional support for it. The standalone word `fax` occurs **0** times in the original S-1, S-1/A No. 3 and S-1/A No. 5, and exactly **once** in the FY1997 10-K405 — as the landlord's letterhead number (`TEL 682-3300 FAX 340-1283`) on a Seattle office-lease exhibit at l.8807. There is no ordering-by-fax sentence in any filing in the family | 2 fetches of PR 1995-10-04 for verbatim ordering-channel text + local `grep -iw fax` across all four filings. → **DEFECT-4**; the C-23 **PARTIAL** |
| §K.4 Ex. 10.15 (Kaphan, 1995-08-08) | cited for the shareholder-agreement date with no drafting caveat | **add the conforming-preamble caveat and broaden U.15** to "the conformed Shareholder's Agreement preambles (Ex. 10.13 **and Ex. 10.15**, at minimum)" | Ex. 10.15 recites *"Amazon.com, Inc. (the 'Company'), a **Delaware corporation**"* on 1995-08-08, the same impossible form as Ex. 10.13 | orig. l.12373-12376 vs l.11489-11491. → **PRESENTATION-2** |
| §A operating-expense list | "operating expenses $406,000 (marketing $200,000; product development $171,000; G&A $35,000; **advertising $30,000**)" | **"… (marketing & sales $200,000 — of which advertising $30,000 per Note 1; product development $171,000; G&A $35,000)"** | advertising is a component of marketing and sales, not a fourth opex line; `d10` already ties 200+171+35 = 406 | orig. l.3734-3735, l.1307-1311. → **PRESENTATION-1** |
| §B.1 / §P `P53` "no options" | "no options held" | **"holds none as filed (1997); no FY1996 option grant disclosed"** — the statement is present-tense as of filing, not a grant history | orig. l.2695-2696 *"Mr. Bezos **does not currently** hold options…"*; the Summary Compensation Table has no option column | wording tightening only; the 1994-95 UNKNOWN conclusion is unaffected |
| **UPGRADE (evidence better than claimed), §P `P39`** | "Inventory carried ≈17,000 — **DERIVED** from the cash-flow movement, Medium-High" | **FACT (audited), High** — $17,000 is a printed 1995-12-31 balance-sheet line; keep `d16` as an independent cross-check | orig. l.3429 `Inventories ............... 17 571` | → **UPGRADE-1**. Raised because AUDIT 2 must report both directions: understating one's own evidence invites a later reader to discard it |
| `quantitative.csv` **l.71 / l.96 / l.97** | the 11 co-cited to `S-1/A No. 5; Form 10-K405 FY1997`; 151 cited to `S-1/A No. 5`; the Dec-1996 accounts/cumulative-sales row cited to `S-1/A No. 5` | **l.71** source cell drops the 10-K405 and its note is replaced by the two-basis text; **l.96** and **l.97** re-keyed to `S-1 (original), 1997-03-24` | same three errors as `P42`/`P60`/`P61`, now replicated into the machine-readable deliverable Stage 2 will ingest | → **DEFECT-5**; the appendix (`F01`, `B50`) already carries the correct 1997-03-24 citations to lift from |
| `stage_1_claim_records.md` **l.376 (`L04`)**, l.90 (`B50`), and 62 records reading "Form S-1" at source date 1997-05-14 | `L04` quotes S-1/A No. 5's *"From December 31, 1995 … 11 … 256"* and dates the claim 1995-12-31 — then carries an appended `[corrected: … 11 is its 1996-01-01 count]` marker; `B50` says *"nothing filed gives a 1994 or 1995 headcount"* in the same sentence as *"the S-1/A employee series starts at 11"* | **keep the quoted passage and the 1995-12-31 date; replace the correction marker with the two-basis note**; correct `B50`'s clause to "nothing filed gives a 1994 or mid-1995 headcount" | the record's own primary quotation refutes the correction layered on it — the clearest available demonstration that COR-03 removed support rather than adding it | → **RD-019**; `L04`'s `Corroboration: 2 (1996 10-K: 158 at 12/31/96)` is also cut to 1, since a 1996 count does not corroborate a 1995 one |
| *(no change — recorded so it is not "corrected" back)* §M-1, §U.8, §U.9, §U.6, §U.10, §U.26, §F.1 | folk figures held as legend / null | **unchanged; all six false-corroboration chains confirmed already collapsed** | see §3 | — |

**Net: 0 claims cut for want of support. 1 claim downgraded from SUPPORTED to PARTIAL (C-23, by attribution,
not by fact). 3 citations re-keyed in `stage_1.md`, and the same 3 again in `quantitative.csv` (DEFECT-5).
1 dual citation split. 1 correction (COR-03) ruled over-claimed and rewritten, with 3 appendix records
(`L04`, `B50`, and 62 unmarked `Form S-1`/1997-05-14 rows) needing the same treatment. 1 upgrade (`P39`).
2 presentation fixes. AUDIT 2 procedure step 1: PARTIAL PASS — 3 of 5 required fields complete across 432
records; tier, class, URL and archived-status are absent as fields.**

## Research debt opened by this audit

> **Id-collision warning for the Company Lead.** The sibling AUDIT 1 sheet has already taken **RD-020, RD-021,
> RD-022 and RD-023** for unrelated debts (re-dating the §Q/§R start; the §Q header scope mismatch; pinning the
> CEO title to the Management bio; quarantining `retrieved` stamps). This audit's debts are therefore numbered
> from **RD-024**, and nothing below should be merged into an RD-020…RD-023 slot.

| RD id | Section | Debt | Assigned | Status |
|---|---|---|---|---|
| **RD-019** | §U.17, §R, §P `P42`; `CORRECTIONS.md` COR-03 | **Rewrite COR-03 as a two-basis dating conflict, not a dossier correction**, and re-key `adversarial_review.md` row E-01 **and `amazon_s1_audit1_chronology.md` §3's endpoint-snapshot row**, both of which inherit the one-sided basis. Decide which basis the Stage-1 snapshot uses and say so once; the boundary reading does not change either way, but the appendix must not assert one basis while two are filed | Consolidation lead (merge) | **OPEN — High**; blocks sign-off of §R |
| **RD-024** | whole file; AUDIT 2 step 1 | **Claim-record appendix schema gap.** `stage_1_claim_records.md` landed **during this audit run** (312 KB, **432 records**, B→U) and was initially reported by this sheet as absent; step 1 was consequently **re-executed against it** — see §0. Result: publication date, confidence and verbatim passage are complete, but **tier is a field on 58 of 432 records, evidence class on 36, a retrievable URL on 22, and archived / local-copy status on 0**, and the appendix's front-matter claim that "nothing was dropped, no class was upgraded" is inaccurate for exactly those four columns, which its own dossier sources carried inline. Two of the three information losses are cheap to repair (tier and class are recoverable from `stage_1.md`'s `[T1 · FACT]` cells and §T's URL column); **`Archived:` is not recoverable from anything on disk** and is the column that records which claims still have a byte behind them after the COR-08 cache destruction | Evidence Registrar | **OPEN — High**; renumbered from this sheet's first draft, whose RD-020 read "the appendix does not exist" and is now superseded |
| **RD-025** | §P `P60`, `P61`; §T rows for A3/A5 | **New register rule needed: "superseded datum."** COR-02 covers *facts absent from an amendment*; it does not cover *facts the amendment replaced with a later measurement* — here Dec-1996 statistics restated as March-1997 statistics in S-1/A No. 3 and No. 5. Sweep **every** post-boundary row citing an amendment and re-test it against that amendment's own current text, not the original's | QC lead → Evidence Registrar | **OPEN — Medium**; 2 rows already known |
| **RD-026** | §I.4, §B.1 Brand row | **USPTO: confirm the bare-"AMAZON" vs "AMAZON.COM"/"AMAZON.COM BOOKS" filing set.** TSDR settles SN 75008413, but the S-1 cover's two composite marks were not separately register-checked, and the "no pending proceedings" reading rests on the filings' own statement. Cheap, closes §U.4's remaining door | Legal/organization | **OPEN — Low**; conclusion does not move |
| **RD-027** | §T `restoration pending` set | **Re-save the non-SEC primaries named in §A, §D, §E, §F, §Q, §U to `sources/`** — the 1995-10-04 and 1996-06-14 releases (both re-read this pass and still live on `press.aboutamazon.com`, so they are retrievable at zero research cost and are the **only two dated in-window company artifacts**), plus LA Times 1997-07-20 and the Kaphan GeekWire series. Right now six claims' supporting text exists only inside dossier quotation; two of them (C-23, C-24) are load-bearing on the launch conflict | Evidence Registrar | **OPEN — High**; this pass supplied verbatim re-reads of both releases, which can be dropped in |
| **RD-028** | §C.1, §E.3 | **The 1995-10-04 release's exact advertised-title wording is quoted three ways in the corpus** (">one million different titles", "more than one million different titles", "over one million titles"), and §A/§E.3/§U.3 each use one. Freeze one verbatim string with its sentence context before `context_appendices.md` is regenerated, since U.3's whole "advertised vs sourceable" argument hangs on it | Copy/QC | **OPEN — Low** |
| RD-011 *(carried)* | §A, §D.1, §E.2, §F.2 | Tallahassee Democrat 1995-10-22 and Knight Ridder Nov 1995 remain Tier-4-quoting-T1 with no print original held. **Unchanged by this pass**; it is the last route to any independent in-window observation of the live store | Distribution | OPEN — High |
| RD-016 *(narrowed)* | §E.3, §U.18 | The 10%-40% band is now **confirmed verbatim in the release**, so the in-window discounting side of this conflict is closed; the residual is only the pricing-programme wording difference between the original and S-1/A No. 5 | Legal/finance | OPEN → **narrowed**, still must not be closed without the line-by-line |

## Sign-off

Stage status: **RECONSTRUCTION → ADVERSARIAL REVIEW → QA → COMPLETE** — currently at **QA, not passable**.

**AUDIT 2 result: PASS WITH CORRECTIONS, conditional on RD-019 and RD-024 closing.**

The substantive case is strong and got stronger under testing. All 24 driving claims resolve to a document that
contains them; 23 are SUPPORTED and the single PARTIAL is an attribution error, not a factual one. Every
material number was re-run against the filed tables rather than against the appendix that quotes them, and the
arithmetic that could be re-run ties: 15,000 + 29,000 = 44,000 against the notes-payable line; 73 + 8 = 81 and
81 − 24 = 57 against Note 2; 52 − 232 − 52 + 1,228 = 944 to closing cash; 198/511 = 38.75% against MD&A's
"approximately 39%"; 2,012,772 × 0.1717 and 3,021,000 × 0.3333 against the Item 5 aggregates. COR-01, COR-02,
COR-04, COR-05, COR-06, COR-07, COR-09, COR-10 and COR-11.1 all hold under independent re-test, four of them
re-proved arithmetically rather than by assertion. Nothing the corrections register fixed has been laundered
back into the text, and all six of the widely-told origin anecdotes that look multi-sourced were confirmed to
one or two lineages each — and had **already** been collapsed by the volume, which is the opposite of the
failure mode this audit exists to catch.

Three things stop this from being an unqualified pass, and none is a fabrication. **First, and most important,
COR-03 itself over-claims:** the filing family carries the number 11 on two different as-of dates, and the
amendments give it the boundary date, so the appendix currently converts a real conflict into a correction and
cites the FY1997 annual report for a headcount it never discloses. **Second, `P60` and `P61` attribute to
S-1/A No. 5 four numbers that amendment either moved to a later date or does not contain at all** — the exact
error class COR-02 was written to prevent, arriving at merge rather than from a dossier, and now sitting in
contradiction with `U.17`, which has it right. Both rows are post-boundary, so **no Stage-1 conclusion moves**,
but an appendix that cites a document which lacks the figure is a citation that will be trusted later by
someone who is not this auditor. **Third, on procedure step 1:** the claim-record appendix was written *during* this run, so step 1 could be
executed and was — see §0 — and its result is a **PARTIAL PASS**. Dates, confidence and verbatim passages are
complete across the 432 records, but tier, evidence class and URL appear as fields on 13%, 8% and 5% of them
respectively, and `Archived:`/local-copy status appears on **none**. The information is not lost (tier and class
live in `stage_1.md`'s cells, URLs in its §T) — it is simply not where the protocol says an auditor should find
it, which means the appendix cannot presently be filtered, audited or re-verified **claim by claim** without a
manual join, and it silently asserts in its own front matter that nothing was dropped when four columns were.
Step 1's useful return, though, was positive: reading the new records surfaced **`L04`, `B50` and `F01`**, which
together show the appendix getting the employee-basis and Dec-1996-statistics questions **right** in the places
where `stage_1.md`'s P-table gets them wrong — so DEFECT-1 and DEFECT-2 have correct citations already written,
one join away, and COR-03's over-claim is caught in the act at `L04`, where a verbatim and accurate S-1/A No. 5
quotation has a correction marker appended over it.

Recommendation to the Company Lead: apply the four defects and three presentation fixes in the table above as a
single merge pass (they are mechanical and none reopens a conclusion), rewrite COR-03 from correction to
conflict, and make `stage_1_claim_records.md` a prerequisite for QA rather than a companion to it. The one
judgment call worth surfacing to the Master Orchestrator: this run found that the corrections register can fail
in the conservative direction, by *removing* support the record gives. Registers that only ever downgrade are
as much a distortion as registers that upgrade, and COR-03 is the example.
