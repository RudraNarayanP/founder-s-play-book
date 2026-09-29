# microsoft_s1_audit1_chronology_hindsight.md

Independent Stage-1 audit, **Microsoft** (`company_011_microsoft`), scope = chronology, hindsight firewall,
independence/lineage, negative-result discipline. Auditor did not write, merge or repair the volume.
**Nothing outside this file was modified.** No defect was repaired; every finding is a report item.

Subject: `founders_playbook/01_companies/company_011_microsoft/stage_1.md` (34,707 w; 9 registers, 127 rows;
14 declared anchors <-> 14 cited; COR-01…COR-05).
Method: §13, §14, §15.5-15.6. Window audited: **1975-01-01 → 1986-12-31** probe-set, volume covers §A-U.
History read: `MASTER_RESEARCH_LOG.md` RD-117 (part 1), RD-122, RD-125/RD-131 (failure classes only),
`CORRECTIONS.md` COR-01…COR-05, merge note at `stage_1.md:11-131`.
`03_quality_control/msft_s1_merge.md` **does not exist** (`ls` of that directory returns no msft/microsoft
file); the merge record lives inside the volume (`stage_1.md:11-131`) and RD-131. That is not a defect of the
company, but a cold reader of `03_quality_control/` cannot find the merge report by name.

Severity scale used here: BLOCKING / HIGH / MEDIUM / LOW / COSMETIC.

---

## Chronology defects

STATUS: WRITTEN 2026-09-30

**CH-1 — MEDIUM. The SEC-carrier census is stated as "14 of 17" in prose and as "12 of 16" in the register;
the measured truth is 12 of 16.**
- Where: `stage_1.md:1114` (§K.1 row "1975, asserted": "**14 of 17 held SEC documents** … 14 carriers, **one**
  lineage"); `stage_1.md:1136-1137` (K02: "carried by **fourteen** held SEC documents"); `stage_1.md:1248`
  (§L.3: "**17 files** under `sources/sec/`"); `stage_1.md:1307-1308` (L05: "17 under sources/sec/");
  `stage_1.md:1736` (Q.2: "0 word-boundary namings … across **17 held filings**"); `stage_1.md:1782` (§R.7:
  "**Fourteen** held SEC documents print the founding sentence … one lineage with **fourteen** copies");
  `stage_1.md:1800` (§R.12: "the MITS deal is absent from **17 filings**").
- What is wrong: the carrier count is inflated by 1 in the denominator and 2 in the numerator. The volume
  contradicts itself: `stage_1.md:1829-1830` (§S.1) says "**16** `.txt` under `sources/sec/`" and "Documents
  printing 'founded as a partnership' = **12 of 16** with whitespace tolerated … only 6 of 16 on a single
  line", and `stage_1.md:1889` (§T.1) says "12 stored documents". `quantitative.csv:20` carries "12 documents
  of 16 stored" and `quantitative.csv:22` carries "0 namings over 16 stored documents".
- Commands (measured this audit):
  `ls sources/sec/*.txt | wc -l` → **16**;
  python, case-insensitive `founded as a\s+partnership in\s+1975` over those 16 files → **12 files**;
  `grep -l -iE "founded as a[[:space:]]+partnership in[[:space:]]+1975" sources/sec/*.txt | wc -l` → **4**
  (per-line; the line-break cases are invisible to it, which is the point §S.1 makes). The denominator 17
  appears to count the one `.html` exhibit on the shelf (`0001032210-99-001374-d1.html`) as a document.
  §S.1's "6 of 16 on a single line" is not reproducible under either invocation (I get 4 per-line, 12
  whole-file); recorded as a secondary imprecision inside the row that is otherwise correct.
- Carrier that fails to support it: `sources/sec/` itself. No listing of that directory yields 17 documents or
  14 founding-sentence carriers.
- Why it matters: §R.7 converts this count into an anti-hindsight assertion (fourteen copies of one corporate
  self-account), and a downstream pass inherits the number, not the caveat. The lineage conclusion (one
  lineage) is unaffected.

**CH-2 — MEDIUM. Month-only periodicals given month-end day precision in `quantitative.csv` — the corpus's
named recurring trap (Target COR-01 / `S435` class: asserting more precision than the carrier holds).**
- Where: `quantitative.csv:9` `date`=1976, `source_date`=**1976-12-31** for "company-name hit lines across held
  BYTE 1976" (an aggregate over 12 issues — no document in the census is dated 31 December 1976);
  `quantitative.csv:10` `source_date`=**1986-01-31** (BYTE January 1986);
  `quantitative.csv:11` `source_date`=**1988-08-31** (BYTE August 1988).
- Carrier: `sources/periodicals/byte-magazine-1986-01_djvu.txt` l.17 prints `JANUARY 1986 VOL. 11, NO. 1` and
  l.550 `VOLUME 11, NUMBER I, 1986`; `byte-magazine-1988-08_djvu.txt` l.14 prints `AUGUST 1988`, l.766
  `AUGUST 1988 VOLUME 13 NUMBER 8`. Neither prints a day. `sources.csv:12` (S4232) and `sources.csv:13`
  (S4233) correctly carry `1986-01` / `1988-08`, and `timeline.csv:9,10,12` correctly carry `1986-01`/`1988-08`.
- Evidence the rule is known in this volume and these three rows were left behind: `quantitative.csv:17`
  preserves B1's superseded `source_date: "1980-12-31"` only inside a `MERGE[same-fact fold …]` tag while the
  kept value is `1980-12`.

**CH-3 — MEDIUM. A bi-monthly issue span converted into an ISO day date.**
- Where: `stage_1.md:1884` (§T.1, BYTE July 1976 row) — `Event date` = `1976-05 / 1976-02 / 1976-03-04 (the
  reprints)`.
- What is wrong: `1976-03-04` reads as 4 March 1976. The carrier prints a two-month issue:
  `company_004_apple/sources/ia_byte_1976/byte-1976-07.txt` l.31477-31478 — "page 24 of **March-April 1976**
  PCC (Box 310, Menlo Park CA 94025)". The volume writes the same datum correctly elsewhere:
  `stage_1.md:1237`, `:1323`, `:1736`, `data_gaps.csv:9` ("People Computer Company Mar-Apr 1976").
- Severity raised by location: §T is the volume's own provenance table, the artifact a cold reader trusts for
  date precision.

**CH-4 — LOW. Four different line ranges for the one club-survey passage, and the register carries the wrong
one.**
- Where: `stage_1.md:1474` (§N.1) and `:1511` (N02) and `:1839` (§S.1) cite `hcc0201.txt` **l.135-141**;
  `quantitative.csv:27` cites **l.141** for "The group also has 28 computers under construction";
  `stage_1.md:1657` (§P.1) cites **l.137-141**; `stage_1.md:691` (§F) and `sources.csv:17` (S4237) cite
  **l.137-142** / **l.137-150**.
- Carrier: `company_004_apple/sources/ia_homebrew/hcc0201.txt` — l.133 `JANUARY MEETINGS`, l.134-136 blank,
  l.137 `January 7, 1976 - The first meeting of 1976 …`, l.138 `At least 300 were on hand …`, l.139-141 the
  distribution, **l.142** `The group also has 28 computers under construction.` So l.135-141 starts two lines
  early and misses the line `quantitative.csv:27` quotes; l.137-142 is correct, and RD-117
  (`MASTER_RESEARCH_LOG.md:1930-1931`) records part 1 reading exactly `hcc0201 l.137-142`.
- Also: `timeline.csv:19` (`about 300 attendees`) — the carrier prints "**At least** 300 were on hand" (l.138),
  a lower bound rendered as an approximation; §F l.687-691 and §S.1 l.1839 both use the correct "at least".
  The register row is the only place the bound becomes "~300/about 300", so the field-level wording loses the
  inequality. MEDIUM-adjacent; recorded here as LOW because the accompanying note still says "bounded".

**CH-5 — LOW. Editor's-note pointer lands on the column head.**
- Where: `stage_1.md:1475` (§N.1) and `validation.csv:3` cite `hcc0201.txt` **l.15-19** for "A LETTER FROM
  MITS … the only MITS 'software' we have ever reproduced"; `stage_1.md:394,572,727,750` (part 1) cite
  **l.17-20** / **l.17-18**.
- Carrier: l.15 = `THIS MONTH - Robert Re i ling`; the quoted note runs **l.17-20**. `sources.csv:17` (S4237)
  carries l.17-20 ✓.

**CH-6 — LOW. A claimed naming-form location the carrier does not print, plus an address-block pointer off by
two.**
- Where: `stage_1.md:1116` (§K.1, 1976-02-29 row): "Same hyphenated form, now in the club's *reply* **heading**
  and signature line | `company_004_apple/sources/ia_homebrew/hcc0202.txt` **l.18**, l.87".
- Carrier: `grep -n -i "micro-soft" hcc0202.txt` returns **exactly one hit, l.87** (`Bill Gates, Micro-Soft`).
  l.18 reads `BILL GATES - One response to Bill* 8 letter to hobbyists that appeared in our last Newsletter` —
  it names Gates, not the hyphenated entity. The heading leg of the row is unsupported; the signature leg is
  supported.
- Same row family: `conflicts.csv:14` (U.14) and `stage_1.md:1615` (O04) cite `hcc0202.txt` **l.85-88** for the
  Albuquerque address; measured at **l.87-89** (l.85-86 blank). `timeline.csv:15` also quotes "the same issue
  reprints the Albuquerque address block at l.85-88".

**CH-7 — LOW. The move interval is bounded one month too early in prose, contradicting the register.**
- Where: `stage_1.md:1581` (§O.1: "between **1976-01-30** and 1980-12") and `stage_1.md:1738` (Q.4: "move lies
  in **1976-01-30** → 1980-12") vs `conflicts.csv:14` (U.14: "the move occurred between **1976-02-29** and
  1980-12") and `decisions.csv:5` ("between 1976-02-29 and 1980-12").
- Carrier: `hcc0202.txt` l.87-89 reprints the same Albuquerque address under a masthead that prints
  `February 29, 1976`, so the earliest defensible bound is 1976-02-29. Both bounds are stated as bounds, not
  events, so the error is one month of the interval, not an invented date.

### Chronology items tested and CLEAN (so the next reader does not re-open them)

- **Masthead day precision is real, not manufactured.** All six Homebrew carriers print a full date on their
  own face, matching `timeline.csv:13-17,19`: `hcc0109` l.13 `Volume Number 1, Issue 9 November 30, 1975`;
  `hcc0110` l.13 `… December 31, 1975`; `hcc0201` l.13 `January 31, 1976`; `hcc0202` l.14 `February 29, 1976`;
  `hcc0203` l.14 `March. 31, 1976`; `hcc0204` l.12 `April 30, 1976`. The 1975-11-30 / 1975-12-31 rows that
  carry the 0-hit 1975 null are therefore stated at the precision the carriers hold.
- **The fiscal-year trap is handled correctly at every site I tested** (Target's COR-01 class):
  `quantitative.csv:26` tags the Schedule X row "USD millions (fiscal year ended 30 June 1994; charged to
  costs and expenses)" with `date`=1994-06-30; `stage_1.md:1255-1258` says "its basis is a **fiscal year ended
  30 June**, not a calendar year"; `stage_1.md:1828` says the EDGAR census basis is "**as-filed dates**, not
  period-of-report dates". `sources/_index/submissions.csv` re-read confirms accession 0000891020-94-000175 is
  `10-K, filingDate 1994-09-27, reportDate 1994-06-30` — the row's `date` is the report date and is labelled
  fiscal. No row in the nine registers reads an MS fiscal year as a calendar year.
- **`1994-10-14` is a document date used honestly.** `timeline.csv:29` places the S-3 by its filing date and
  says so ("Event date is the filing, not the founding"); the carrier's own header prints
  `FILED AS OF DATE: 19941014` and the index prints `S-3 / 1994-10-14` (verified), so the (PB)-style
  post-window placement is disclosed, not laundered.
- **Post-window documents inside window rows**: `timeline.csv:2` and `:7` both write "Company **later states**"
  with `evidence_class` = RETROSPECTIVE INTERPRETATION; `timeline.csv:8` uses the non-date token
  `catalogue-1982` rather than a fabricated event date for a layer with no year on its face.
- **`(PB)` material**: `stage_1.md:628` (1981 Adventure brochure), `:1490/:1547` (Allen transcript),
  `:1582` (1981 incorporation row), `:1905`, `:925` (1986-1990 silence) — all marked, all outside the
  contemporaneous class, none presented as in-window observation.
- **Line-pointer verification over 51 cited ranges** (script run from `/tmp`, no repo file created): 44 pass,
  including every load-bearing quotation — Gates's signature (hcc0201 l.127-129), "Almost a year ago"
  (l.83-84), the royalty lines (l.94-95, l.104-105), the VDM-1 column (l.49-55), the Bellevue imprint in
  **both** physical copies of BYTE Dec 1980 at their **different** line numbers (Apple copy l.13346-13347;
  Microsoft copy l.13342-13344 — the volume cites each against its own path, which is correct), the sibling
  review line (l.39649-39653), the `S435/S45` price pair (l.38112-38113), the reader-letter "end of the line"
  (l.51394-51400), `MICROSOFT. Inc.` (l.16017), Compute! l.21051 and l.17602, `Watch out Micro-Soft.`
  (1987-04 l.96074), AR2017 l.623, S4241 l.396-397, S4242 l.3900, S4226 l.181-182 / l.975-977 /
  Schedule X l.1408-1418. The 7 failures are CH-4, CH-5, CH-6 and two false alarms of my own (see Untried).

---

## Hindsight leaks

STATUS: WRITTEN 2026-09-30

**Sweep first, because the headline result is a negative.** Command:
`grep -n -i -E "would become|would later|would go on|proved that|it proved|showed that|inevitab|laid the
ground|set the stage|the decision that made|destined|foreshadow|trajectory|future giant|in hindsight|clearly
the|was born|seeds of|blueprint|DNA|turning point|vision" stage_1.md`
→ 7 hits, **all of them refusals or unrelated print**: `:162` ("not proof that a corporation was inevitable"),
`:220` (window statement), `:869` ("Death Dreadnaught" — an adventure-game title), `:1305` ("advance,
territory" — L05), `:1795` (§R.11 "Not implying that anything was inevitable"), `:1805` ("a picture of a small
firm, not a future giant"), `:1847` ("< 2 USD/hour" — "hour" matching `DNA`-adjacent noise). **No causal or
significance sentence in the volume uses hindsight vocabulary.** The firewall section §R (`:1754-1812`) and the
Header's firewall statement (`:160-166`) are load-bearing and are honoured in the body: §C's coda refuses the
"founders identified the industry's core problem" inference (`:508-516`), §I lists NOT-SUPPORTED refusals
(`:877-881`), M06 keeps the 1980 user criticism with "whatever it later became" (`:1431-1432`).

**HS-1 — MEDIUM. Prose asserts a *chosen* scaling path that the same volume's register row labels as an
inference with no deliberation on record.**
- Where: `stage_1.md:1569-1572` (§O opening): "…and **the scaling it chose** visible in print is **breadth of
  machines, not depth of staff**: ports and OEM-style placement into other manufacturers' configurations
  (§M, §N) rather than a growing programming workforce".
- What is wrong: "the scaling it chose" states a decision. The section's own decision table row 1 gives the
  rationale as "**NOT RECORDED — mechanism UNKNOWN**; the corpus has no deliberation"
  (`stage_1.md:1578`), O05 is CLASSed "**INFERENCE** (this pass's only load-bearing inference)"
  (`stage_1.md:1626-1627`), `decisions.csv:2` carries `rationale` = "NOT RECORDED - mechanism UNKNOWN", and
  §R.3 refuses "the ports were a strategy" on exactly this ground (`stage_1.md:1770-1772`). The sentence is
  one removal away from the classic "the decision that made Microsoft" shape; the artefact-vs-choice
  distinction §O's first paragraph sets up (`:1559-1562`) is not applied to this sentence.
- Carrier that fails to support it: no held byte records a choice of breadth over depth. The inputs are one
  syndicated Kilobaud item, one Compute! user note, and three 1980 third-party ads.

**HS-2 — LOW. A causal "strong reason why" built on a two-document market picture.**
- Where: `stage_1.md:800-804` (§H coda): "What the knowable market explains is the firm's **shape**, not its
  fortune: a product whose buyers were identifiable only through another company's machine and another
  company's magazine, in a period when the surrounding print was actively offering free substitutes, **is a
  strong reason why** the earliest documented act is an *appeal to pay* rather than a launch".
- What is wrong: "explains" plus "a strong reason why" is a causal claim resting on one Popular Electronics
  price page (which the volume rules may **never** be cited for this company — `stage_1.md:247-250`,
  `sources.csv:16`) and one club survey of 70 machines in one self-selected room (`quantitative.csv:13`). The
  hedge is present two lines later (`:805-807`, the alternative "a market this thin may have made per-unit
  pricing unsound regardless of copying"), and §D/§N never call the letter a market test, so severity is LOW:
  the sentence is a mechanism *proposal*, but "strong" ranks a causal weight the record cannot carry.

**HS-3 — LOW. Two registers cannot carry a hindsight class at all, and rows that restate retrospective
self-report sit in them unclassed.**
- Where: `channels.csv` (header has no `evidence_class`) and `data_gaps.csv` (likewise). Rows:
  `channels.csv:8` (unauthorised reseller channel, "The firm predicted resellers may lose in the end",
  source S4222), `channels.csv:2` (MITS channel terms/result cells drawn from the letter's own account),
  `data_gaps.csv:5` (founder pre-history, "only retrospectives" in the evidence cell but no class field).
- What is wrong: §3 requires every FOUNDER CLAIM to be sub-classified contemporaneous vs retrospective memory.
  The volume does it in prose and in the four registers that have the column (`sources.csv`, `timeline.csv`,
  `quantitative.csv`, `validation.csv`, `failures.csv`, `conflicts.csv` all carry class/weight language), so
  the gap is a schema limit rather than a mis-classification — reported so no later reader treats a
  `channels.csv` row as classed evidence. Every class I could check is correct:
  S4226/S4240/S4241/S4242 = RETROSPECTIVE INTERPRETATION; S4222 = FOUNDER CLAIM; S4231 = FOUNDER CLAIM with
  `event_date` UNKNOWN; the 1994 restatement rows are classed retrospective in `timeline.csv:2,7,29`; and no
  retrospective account anywhere in the nine registers is classed FACT or CONTEMPORANEOUS OBSERVATION.
- Also checked clean: `stage_1.md:1219` renders the letter's OCR `§2 an hour` as "$2 an hour" inside a table
  cell while §L.2 (`:1232-1234`) prints `§2 … [sic: § = $]` and §C (`:454`) prints `§2 [sic: $]`. The damaged
  form is preserved in the sections that matter and the repaired form appears only in a summary cell — a
  print-fidelity inconsistency against the Header's own rule (`:208-213`), not a silent repair of a quoted
  passage.

---

## Independence audit

STATUS: WRITTEN 2026-09-30

**IN-1 — HIGH. `conflicts.csv` U.3 counts two Microsoft self-accounts as corroboration.**
- Where: `conflicts.csv:3` (U.3), `residual_uncertainty` cell: "1975 stands as the company's own account,
  **corroborated across two independent lineages (1976 letter, 1994 filing)** but never documented
  contemporaneously".
- What is wrong: both named carriers are the registrant's own words about its own start. `sources.csv:2`
  (S4222) is classed **FOUNDER CLAIM** — Gates's letter; `sources.csv:6,21,22` are classed
  **RETROSPECTIVE INTERPRETATION** — Microsoft's own filings. The volume's §A states the correct limit:
  "Both lineages are company-side about the company's own start; the independence is in the **institutional
  route**, not in the **interest**" (`stage_1.md:325-327`), and K02 counts "**1** lineage … plus one
  contemporary-side **match**" (`stage_1.md:1143-1145`). The register cell drops "match" and keeps
  "corroborated", which is the word a downstream agent reads as external support. Compounding it: the 1976
  letter never states 1975 and never states a founding; it prints "Almost a year ago, Paul Allen and myself …
  hired Monte Davidoff and developed Alt air BASIC" (`hcc0201.txt` l.83-84, verified), so what "corroborates"
  the 1975 year is a subtracted span, not a second witness.
- This is the defect §3 exists to stop, in the layer RD-125 says later passes trust most.

**IN-2 — MEDIUM. `channels.csv` attributes third-party observations to the company's own letter.**
- Where: `channels.csv:2` — channel "Distributor's own channel (MITS, including MITS Computer Notes)",
  `result` = "the letter reached the club via MITS **and the text was reprinted on page 3 of February 1976
  Computer Notes**", `source_id` = **S4222**. `channels.csv:3` — `repeatability` = "reprints recorded across
  at least 4 titles **per BYTE 1976-07**", `source_id` = **S4237**.
- Carrier that fails to support it: S4222 is the Gates letter (`hcc0201.txt` l.75-129); it says nothing about
  reprints or about *Computer Notes*. The reprint facts are BYTE's, carrier **S4227**
  (`byte-1976-07.txt` l.31476-31480 and `byte-1976-09.txt` l.2040-2045, both verified on those lines) — the
  row's own `notes` cell even cites `byte-1976-09 l.2041`. Same for `channels.csv:3`: the "3 printed replies"
  leg belongs to S4223/S4224/S4225, not to S4237 (club masthead/editor pages). §G does rule this correctly in
  prose (`stage_1.md:316-317`: "cite the venue for the fact of publication, the letter for the content of the
  claim") — the register row ignores it, and `sources.csv:2`'s `claim_supported` for S4222 (R01-R05) does not
  include any channel row.

**IN-3 — MEDIUM. §T.2 counts two issues of one magazine as "two non-company authors".**
- Where: `stage_1.md:1901`: "MITS is the channel … corroborated in *form* by **two non-company authors** at
  distance 6-8 months | `hcc0201` l.103-105 + `byte-1976-07` l.31477, `byte-1976-09` l.2038".
- What is wrong: BYTE July 1976 and BYTE September 1976 are one publication (BYTE / McGraw-Hill) and one
  register row (S4227). The volume's own rulings forbid the count: §G "the two BYTE passages are **one fact
  told twice by one magazine**" (`stage_1.md:738-743`), L03 "same magazine family, so de-duplicated before
  counting" (`:1291-1292`), N05 "3 unrelated vendors, **1 magazine** (not 3 independent markets)" (`:1540`),
  U.12 "four unrelated vendors, one magazine, one month — treated as one market signal, not four
  corroborations" (`:1986`). The arithmetic (6-8 months) is right; the lineage count is wrong.

**IN-4 — LOW. The 1986 "eight further national entities" census includes a third party's name that the
volume's own pattern rule excludes.**
- Where: `timeline.csv:9` — "Company print names Microsoft Corporation at Bellevue **plus eight further
  national entities**", actors list `Bellevue; Munich; Sydney; Berks; Ontario; Sollentuna; Paris; Seoul;
  Tokyo`, carrier S4232.
- Carrier: `sources/periodicals/byte-magazine-1986-01_djvu.txt` l.5342-5372 prints, inside a Windows
  advertisement, `Microsoft Corporation / Bellevue, Washington USA`, then `Microsoft GmbH` (Munich),
  `Microsoft Pty` (Sydney), `Microsoft Ltd` (Berks), `Microsoft Canada Inc` (Ontario), `Microsoft AB`
  (Sollentuna), `Microsoft SARL` (Paris), **`ONIX Microsoft`** (Seoul), `Microsoft Far East` (Tokyo). Seven of
  the eight carry a corporate suffix; **ONIX** is another company's house name in a co-branded form. §U.15 and
  §S.1 establish exactly this exclusion for 1980 (`:1834`: l.10305 `Pro-Micro Software Ltd.` is "**a
  different company**"; `:1118`: `Microsoftware Systems` "is **a different company**"; `:1117`:
  `portable microsoftware` excluded "from every count in this volume"), so the 1986 row applying no exclusion
  is inconsistent with the rule the same volume minted. The row's hedge ("corporate relationships not
  established") covers the *relationship*, not the *name attribution*.

**IN-5 — LOW / observation. Same-measurement pairs beyond the retired `U.5`→`U.15` fold.**
- **`conflicts.csv:2` (U.2) and `:9` (U.9) carry one identical leg**: the same BYTE September 1976 sentence at
  the same lines (l.2038-2039) at the same date (1976-09) is U.2's `claim_b` and U.9's `claim_a`. The rows
  legitimately differ on the counter-leg (paid fraction vs ownership), so this is not a fold candidate, but
  one passage is adjudicated twice under two anchors, and a reader counting "distinct 1976-09 evidence" gets
  two. Not folded by the merge even though `U.5`/`U.15` — a weaker overlap — was.
- **The 134-hit-line measurement is asserted under two different `source_id`s for one census**:
  `quantitative.csv:17` cites **S4238** (Microsoft-shelf copy) while `timeline.csv:6` and `validation.csv:2`
  cite **S4230** (Apple-shelf copy) for the same "134 hit lines, 0 of them hyphenated". Values agree, so there
  is no numeric conflict; but §S.1 `stage_1.md:1833` calls it "a replication over two physically distinct
  files, not a second source", and the two register rows that carry the count do not point at each other.
  A "which source supports 134?" query returns two ids for one measurement.
- **Checked clean** (the discipline is largely present and I record it so repairs are not attempted):
  `sources.csv:10` (S4230 annotation: "this row, D17 and D24 are ONE identifier … across two physical copies
  and three authorship sets … annotated here so no pass counts three sources"); `sources.csv:18` (S4238
  "Replication of a measurement, NOT a second source for any print fact"); `sources.csv:21-22` (S4241/S4242
  "third copy, not third source"); `sources.csv:6` (no second row minted for the FY1994 10-K, P2 instruction 2
  applied); `stage_1.md:68-69` (D16/S4237 deliberately **not** de-duplicated against D01/S4222 — same file,
  different author — which is what keeps the 70-machine count independent); `sources.csv:4` (the "10 percent
  minority" phrasing is D01's number, not an independent count); `quantitative.csv:20-21` ("12 copies, ONE
  lineage", "stated numerically so no pass counts 13 sources"); §R.7 (`:1782-1784`); K07 (`:1190-1191`); the
  syndicated OSI item held at "one item, three documents" in all four places it appears
  (`timeline.csv:4`, `sources.csv:8`, `:1349`, `:1395-1396`). No claim in the volume or registers counts the
  registrant's re-printed self-account as corroboration **except** IN-1 and IN-3.

---

## Negative-result discipline

STATUS: WRITTEN 2026-09-30

**NR-1 — HIGH. Family (b) web archives recorded as UNTRIED with "0 calls", while the company's own shelf holds
two attempted calls and a recorded dead-route verdict.**
- Where: `stage_1.md:1047-1048` ("**UNTRIED from this pass, unchanged and not silently closed:** family (b)
  web archives (**0 calls**); family (e) documentary (0 calls)"); `stage_1.md:157-158` ("a third family could
  only come from (b) web archives or (e) documentary, **both UNTRIED/UNANSWERED**").
- What is wrong: the state is **UNANSWERED (dead route)**, not UNTRIED, and "0 calls" is a false count.
  `sources/web_archive/` holds `cdx_microsoft_com_earliest_200.json` (11,832 B) and
  `cdx_microsoft_com_earliest_200_retry.json` (11,832 B) plus sidecars; the first sidecar records
  `"http_status": 503`, `"body": "Internet Archive: Temporarily Offline banner (HTML, not a CDX JSON answer)"`,
  `"verdict": "UNANSWERED (service 503, not an empty result)"`. Two calls were made on 2026-09-26
  (00:45 and 00:48). The volume's own sidecar layer states the correct class; the volume's prose and its
  §15.5 "dead routes are named" close-out contradict it. The slash in `:158` ("UNTRIED/UNANSWERED") is the
  tell — the two classes are being used as one word for two families.
- Consequence: family (b) is the only route that could lift this company from T2 to T1 (§A `:156-158`), and a
  cold planner reading "0 calls, UNTRIED" mis-estimates both the remaining work and the reason coverage is
  thin. Conversely the 503 must not be read as "no web record exists" — the sidecar gets that right
  ("not an empty result") and the volume never claims it, so the defect runs one way only.

**NR-2 — HIGH. RD-130's class, still live in this company's files: a YEAR-faceted harvest written up as an
absence of the record class, contradicted by a carrier the same volume cites.**
- Where: `stage_1.md:340` (§A floors: "there is **no digitised annual-report run** (N-1)");
  `stage_1.md:1735` (Q.1) and `data_gaps.csv:8` (GAP-K1: "the creator-scoped annual-report run returned
  numFound 1 and it is a 1997 manual"), repeated at `stage_1.md:1638-1639` (§P: "family (a) is floored …
  (N-1/N-2)") and `stage_1.md:2173`.
- Carrier / query: `sources/corporate_print/ia_q4_creator_microsoft_reports_1977_1998.json`
  `responseHeader.params.query` = `(creator:microsoft OR creator:"microsoft corp" OR
  creator:"the microsoft corp") AND (title:annual OR title:report OR title:reports) AND mediatype:texts AND
  year:[1977 TO 1998]` → `numFound: 1` (a 1997 Visual Basic manual). Two facets manufactured this null:
  a **YEAR facet whose floor is 1977**, so 1975-1976 corporate print was never inside the query perimeter, and
  a **title facet** (annual/report/reports). RD-130 (`MASTER_RESEARCH_LOG.md:2519-2524`) records the identical
  Kroger case: numFound 0 **with** `AND YEAR:[…]`, 1 **without** it.
- Internal contradiction, decisive without any web call: the same company directory holds a digitised
  Microsoft annual report — `sources/periodicals/01-microsoft-annual-reports_djvu.txt`, 295,724 B, sidecar
  `"identifier": "01-microsoft-annual-reports"`, source filename decoding to "Microsoft Corp (MSFT) Annual
  Report, 2017" — and this volume cites it at `stage_1.md:1186-1191` (K07), `sources.csv:20` (S4240), and
  `stage_1.md:1747` (§Q.8: "`01-microsoft-annual-reports` puts a **2017** document inside a 1975-window
  census"). So "no digitised annual-report run" is false as a class statement. What is true, and should be the
  sentence: *no annual-report layer dated inside 1975-1990 is held; the only corporate-print annual-report
  digitisation this project holds is FY2017 (S4240); the creator+title+YEAR:[1977 TO 1998] facet run returned a
  manual; a facet-free re-query is UNTRIED.*
- Severity: this is a **floor statement used to set tier and knowability** ("NOT KNOWABLE on the current
  archive", Q.1; "T2 … the T1 bar is not reachable here by filings at all", `:156-158`), so the defect is
  load-bearing rather than cosmetic. I did **not** re-run any query (0 web calls this audit): the finding is
  the facet/perimeter mismatch plus the held-carrier contradiction, both measurable on disk.

**NR-3 — LOW. A route already emptied is re-assigned as open.**
- Where: `data_gaps.csv:11` (GAP-M1 follow_up): "Grep Popular Electronics Jul-Dec 1975 and Jan-Feb 1976,
  Kilobaud 1975-1977 **and BYTE 1976** for a Micro-Soft product announcement or ship date".
- What is wrong: BYTE 1976 **is** held (12 issues, 5,743,636 B on the Apple shelf) and has already been
  measured at 0 hit lines — `quantitative.csv:9`, `stage_1.md:1113` (§K.1), `conflicts.csv:3` (U.3's `claim_b`
  names "BYTE 1976 x12 5,743,636 B … all 0 hits"). Assigning it as a follow-up re-opens an EMPTY-within-
  perimeter route and will consume a pass. The other four targets in the sentence are genuinely unheld (see
  the verification below).

**NR-4 — LOW. Three different perimeters for the 1975 null.**
- Where: `stage_1.md:1740` (Q.6: "0 across 6,272,665 B … a bounded sample of **~44** of a 545-item shelf");
  `data_gaps.csv:13` (GAP-Q1: "0 hits over 6,272,665 B … out of a shelf of about 545 items of which this
  project has opened **11 layers**"); `stage_1.md:1832` (§S.1: "Microsoft-shelf text layers **11 layers** /
  **9,763,197 B**").
- What is wrong: "~44" matches nothing else in the volume, and the two byte totals (6,272,665 vs 9,763,197)
  are different perimeters with no stated relation (the first is the 1975-or-covering-it subset, the second the
  whole Microsoft shelf). The bounded-sample *language* is correct in all three places; the numbers need one
  definition each. No claim of absence is harmed, but a later pass comparing censuses cannot tell which
  perimeter produced the null.

**NR-5 — CLEAN, and the model case for the rest of the corpus.** The EDGAR floor was re-measured independently
and holds exactly: `sources/_index/submissions.csv` = 4,525 rows, columns
`filingDate,form,accession,reportDate,primaryDocument,source` (header enumerated before use), min `filingDate`
**1994-02-14**, **0** rows earlier, **0** rows of form `S-1` or `S-1/A` among 62 distinct forms. `stage_1.md:185-189`
and `:1828` state it as EMPTY-within-perimeter and refuse to imply any 1975-1990 filing was consulted.
`sources/sec/_UNANSWERED.csv` (1 data row) records accession 0000891020-94-000114 as
`UNANSWERED … HTTP 503 … TimeoutError … 404 NoSuchKey`, `bytes=0` — a dead route kept visibly distinct from
the UNTRIED 3,468 unfetched 1994-1999 accessions named at `stage_1.md:1050` and from the EMPTY census above.
Every other route my scope names was checked against the filesystem and the classification is right:

| Route | Volume's state | Measured | Verdict |
|---|---|---|---|
| MITS *Computer Notes* | not held / FETCH REQUEST (`:757-760`, `data_gaps.csv:9`) | `find` over `01_companies/`: 0 items | correct (UNTRIED) |
| PCC Mar-Apr 1976 | not held, page named by BYTE (`:1240-1242`) | 0 items | correct |
| Popular Electronics Jul-Dec 1975 | unheld / UNTRIED (`:244-246`, `:1740`) | only `197503…` held | correct |
| Kilobaud 1977-78 | "unheld" (`:1969`, `conflicts.csv:10`) | only `kilobaudmagazine-1977-05` held | correct |
| `byte-magazine-1977-08` | "unheld: UNTRIED" (`stage_1.md:2158` region, `:1712-1713`) | 0 items anywhere in `01_companies/` | correct |
| Family (e) documentary | UNTRIED, 0 calls (`:1036`, `:1934`) | no documentary layer on any shelf | correct |
| Family (b) web archives | **UNTRIED, 0 calls** | **2 attempted CDX calls, HTTP 503, verdict UNANSWERED** | **WRONG — NR-1** |
| Corporate print 1975-1990 | "no digitised annual-report run" | faceted query + an held FY2017 report | **WRONG — NR-2** |

---

## Gate

STATUS: WRITTEN 2026-09-30

Command exactly as briefed, output verbatim (exit code 0; **no check reported DID NOT RUN**):

```
$ python tools/gates.py --company-dir founders_playbook/01_companies/company_011_microsoft \
    --checks csv,keys,anchors,corrections --tier core --fail-on substantive

# Mechanical gate report -- company_011_microsoft

Findings: **0** | Passes: 19

- coverage 9 registers, 2 stage volumes, 31 source documents
- keys     stage_1.md mentions 2 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S4221, S435
- keys     stage_1_index.md mentions 4 retired keys inside collision/re-key/range text -- protected history, not re-pointed: S4201, S4221, S4301, S4331
- anchors  stage_1.md declares an explicit ANCHORS set (14 ids)
- anchors  stage_1.md declares 14 anchors
- anchors  11 id(s) read as backticked references or range endpoints, not citations (U.1, U.11, U.12, U.13, U.14, U.15, U.2, U.3)
- corrections 5 retraction ids; register layer reaches 5, volumes 5

## Passing checks

csv      timeline.csv                       28 rows x 11 cols
csv      timeline.csv.source_id             all S#### tokens resolve
csv      quantitative.csv                   26 rows x 12 cols
csv      conflicts.csv                      14 rows x 15 cols
csv      sources.csv                        22 rows x 18 cols
csv      data_gaps.csv                      13 rows x 8 cols
csv      validation.csv                     7 rows x 11 cols
csv      validation.csv.source_id           all S#### tokens resolve
csv      failures.csv                       5 rows x 11 cols
csv      failures.csv.source_id             all S#### tokens resolve
csv      decisions.csv                      5 rows x 15 cols
csv      decisions.csv.source_id            all S#### tokens resolve
csv      channels.csv                       7 rows x 11 cols
csv      channels.csv.source_id             all S#### tokens resolve
keys     stage_1.md                         22 source tokens all resolve
keys     stage_1_index.md                   22 source tokens all resolve
anchors  citation resolution                every register-cited anchor resolves (15 distinct ids across registers and volumes)
anchors  parity                             14 narrative anchors <-> 14 register anchors
corrections propagation                        all 5 retraction(s) reach registers and volumes
```

**The one standing `budget` finding was not emitted by this command, and that is a property of the command,
not of the company.** `gates.py` runs the budget gate only when `budget` is in `--checks`
(`tools/gates.py:641-642`), and the four briefed checks exclude it. To confirm the adjudicated finding is
still the same single one, I ran the briefed set plus `budget` — no file touched:

```
$ python tools/gates.py --company-dir …/company_011_microsoft \
    --checks csv,keys,anchors,corrections,budget --tier core --fail-on substantive

Findings: **1** | Passes: 20
| budget | stage_1.md | 34707 words > core cap 22000 (split required) |
```

That matches the merge note's own statement (`stage_1.md:21-26`) and RD-122: an adjudicated dispatch-cap miss,
**not a defect, and I propose no trimming.** The `keys` info lines are likewise not defects: `S435` is the OCR
dollar-sign pair at `byte-magazine-1980-12` l.38112-38113 (verified on that line: "To licensed users of
Microsoft BASIC-80 / (MBASIC) S435/S45"), and per RD-131/COR-05 a quoted `S####` inside a verbatim passage is
print, not a pointer; `S4221`/`S4201`/`S4301`/`S4331` are retired-key history in collision text. **I do not
flag any of them.**

---

## Sweep counts

STATUS: WRITTEN 2026-09-30

**What I opened.**
- `stage_1.md`: 2,191 lines total. Eight contiguous reads (1-300, 300-670, 670-969, 1032-1061, 1100-1219,
  1227-1466, 1466-1736, 1754-2023) = **1,692 of 2,191 lines read directly**; **not read directly**:
  970-1031 and 2024-2191 (part 1's and part 2's `>>> REGISTER ROWS FOR MERGE <<<` blocks) and the small seams
  1062-1099, 1220-1226, 1467-1467, 1737-1753 — the emission blocks are protected pre-merge text whose
  canonical form is the nine CSVs, all of which I did read (next bullet).
- All **9 canonical registers, 127 of 127 rows** read in full and header-enumerated before any field was read
  by name: `timeline.csv` 28, `quantitative.csv` 26, `conflicts.csv` 14, `sources.csv` 22,
  `data_gaps.csv` 13, `validation.csv` 7, `channels.csv` 7, `decisions.csv` 5, `failures.csv` 5
  (28+26+14+22+13+7+7+5+5 = 127 ✓ matches the merge note's census at `stage_1.md:28-35`).
- `CORRECTIONS.md` (COR-01…COR-05) in full; the merge note (`stage_1.md:11-131`) in full;
  `MASTER_RESEARCH_LOG.md` RD-117, RD-122, RD-125, RD-130, RD-131.
- **20 source carriers opened**, 51 citation ranges machine-checked against the bytes (helper script run from
  `/tmp`, created no repo file): `hcc0109`, `hcc0110`, `hcc0201`, `hcc0202`, `hcc0203`, `hcc0204`,
  `byte-1976-07`, `byte-1976-09`, `byte-1977-07`, BYTE Dec 1980 **both** copies (Apple 1,669,716 B /
  Microsoft 1,669,324 B), `byte-magazine-1982-03`, `byte-magazine-1986-01`, `byte-magazine-1987-04` (Dell
  shelf, read-only), `byte-magazine-1988-08`, `1979-Fall-compute-magazine`, `197503PopularElectronics`,
  `01-microsoft-annual-reports`, `sources/sec/…94-000175`, `…94-000180`, `…95-000018`;
  plus `sources/_index/submissions.csv`, `sources/sec/_UNANSWERED.csv`,
  `sources/corporate_print/ia_q4_…json` (+sidecar), `sources/web_archive/*` (+sidecars),
  `sources/periodicals/01-microsoft-annual-reports_…meta.json`.
- **28 of 28 `timeline.csv` rows** read against their carriers; **26 of 28** verified against the bytes
  themselves for printed date and precision.
- Language sweeps (commands in the sections above): hindsight vocabulary (7 hits, all refusals); negative-class
  vocabulary counts (`UNTRIED` 12, `UNANSWERED` 2, `404` 2, `EMPTY` 0, `403`/`429`/`zero-byte` 0 in
  `stage_1.md`); filesystem `find` for the six named unheld routes; the 3,468-accession claim located at
  `stage_1.md:1050` and `research/B1_periodical_records.md:463`.

**What I did NOT test (deliberately, and it is not a clean bill for these).**
- The two `>>> REGISTER ROWS FOR MERGE <<<` blocks as text (`stage_1.md:969-1045`, `:2021-2191`) beyond the
  parts quoted in the merge note and the rows the registers carry: the canonical data is the nine CSVs and the
  blocks are marked DO-NOT-RE-APPLY (`stage_1.md:127-129`). Any drift between an emission block and its
  applied register row is therefore **unmeasured** here.
- `_MANIFEST.md`'s per-register arithmetic (148 requested → 127 applied, 18 collision groups). I accepted it
  and did not re-run `merge_census.py`.
- `stage_1_index.md`, `research/A1-A4` and `B1_periodical_records.md` internal claims (B1 read only for the
  3,468 line and COR-referenced rows), `tools/gates.py` and `tools/scaffold.py` internals beyond the budget
  gating question.
- Any **web** route: 0 calls. I did not re-run the IA facet-free corporate-print query RD-130 prescribes,
  did not re-run the CDX, and did not attempt `MITS Computer Notes`, PCC Mar-Apr 1976, Radio Electronics May
  1976, Popular Electronics Jul-Dec 1975, Kilobaud 1977-78, or `byte-magazine-1977-08`.
- The 44 passing line-pointer checks are evidence the pointers land, not that the readings are right; I did
  not re-derive any *print fact* beyond date precision, name form and the counts I ran commands for.
- The other two audit lanes (numbers, citations) and other companies' files. UnitedHealth was not touched.
- 2 of the 28 timeline rows (`1977-05` Kilobaud product-news line; `catalogue-1982` Allen transcript) were not
  byte-verified for content — the register's carrier pointer was accepted.

---

## Untried

STATUS: WRITTEN 2026-09-30

Routes and questions this audit could not close, stated so no later reader takes them as absent records.

1. **Facet-free corporate-print re-query** (RD-130's fix): `(creator:microsoft) AND (title:annual OR
   title:report OR title:reports) AND mediatype:texts` with **no `year:` facet**, and with a range reaching
   1975-1976 (the held q4 run's floor is 1977, i.e. the founding window was never inside it). Until this runs,
   GAP-K1/Q.1/§A's "no annual-report run" is a *faceted* null, not an archive fact — and the volume's own
   `S4240` FY2017 layer proves the class exists on IA at all. Never attempted by this audit (0 calls).
2. **Family (b) web archives after the 503**: the CDX route returned `Internet Archive: Temporarily Offline`
   twice. UNANSWERED (dead route), not empty; re-attempt is untried. The volume's "0 calls" label must be
   corrected before a planner sizes this route (NR-1).
3. **The five named unheld periodicals** — *MITS Computer Notes* (Feb 1976 p.3, and a 1975-1977 run),
   *People's Computer Company* (Mar-Apr 1976 p.24), *Radio Electronics* (May 1976 p.14), Popular Electronics
   Jul-Dec 1975 (the shelf holds candidate items named at `data_gaps.csv:13`), Kilobaud 1975 and 1977-78,
   `byte-magazine-1977-08`. All verified absent from disk; none was ever fetched. The MITS-terms UNKNOWN
   (GAP-L1/Q.2/U.9) stays **earned** only while this is labelled UNTRIED, which the volume does correctly.
4. **`ia_text.py` after its route fix** over the ~500 unopened Homebrew-shelf items (GAP-Q1) — the 1975
   name-vacuity is a 6.3-9.8 MB bounded sample, never a proven absence.
5. **Registrant-side instruments**: New Mexico and Washington Secretary of State assumed-name/corporation
   records 1975-1982 (U.6, U.11, GAP-K2); Copyright Office records for 1976-1978 BASIC registrations (U.9);
   family (e) auction/museum search for partnership or licence paper. 0 calls anywhere in this company's
   history, including this audit.
6. **The 3,468 unfetched 1994-1999 accessions** and `sec_intake.py facts` for 1994-1999: UNTRIED, and the one
   accession actually attempted is recorded UNANSWERED in `sources/sec/_UNANSWERED.csv` — the two states must
   stay separate in any repair pass.
7. **Which 14-vs-12/16 discrepancy produced CH-1**: I did not open `research/A2` or B1's census rows to find
   the "14 of 17" arithmetic, because a repair agent can locate it faster than I can guess it. The measured
   truth (16 documents, 12 carriers) stands on the commands in CH-1.
8. **Whether `hcc0202`'s reply heading "Regarding your Letter of 3 February 1976 Appearing in Homebrew
   Computer Club Newsletter Vol. 2 No. 1" (measured at l.91-92) conflicts with the January 31, 1976 masthead of
   V2N1.** The corpus quotes the string (`sources.csv:3` S4223 `relevant_passage`) but no anchor records the
   date tension, and `timeline.csv:15` describes the reply as citing "the January letter". I did **not**
   resolve it — a 3-February-dated incoming letter cannot have appeared in a 31-January issue, so either the
   reply answers a *different* Gates communication or the heading is the club's date of receipt. Not asserted
   as a defect here because I did not read the reply's full body to establish which; recorded as the highest-
   value untried chronology item inside the window's first four months.

---

## Counts

STATUS: WRITTEN 2026-09-30

| Severity | Count | Findings |
|---|---|---|
| BLOCKING | 0 | — |
| HIGH | 3 | IN-1 (U.3 counts two Microsoft self-accounts as corroboration); NR-1 (family (b) UNTRIED/"0 calls" vs two attempted 503 CDX calls); NR-2 (faceted "no annual-report run" vs the held FY2017 layer, RD-130's class) |
| MEDIUM | 6 | CH-1 (SEC census 14-of-17 vs measured 12-of-16); CH-2 (month-only periodicals given month-end day precision, `quantitative.csv:9-11`); CH-3 (Mar-Apr 1976 rendered `1976-03-04`, §T.1); HS-1 ("the scaling it chose" over its own INFERENCE row); IN-2 (`channels.csv` attributes BYTE's observations to the company letter); IN-3 (two issues of BYTE counted as "two non-company authors", §T.2) |
| LOW | 10 | CH-4 (four line ranges for one survey, wrong one in the register); CH-5 (editor's-note pointer lands on the column head); CH-6 (`hcc0202` l.18 "heading" leg has no carrier); CH-7 (move interval bounded a month too early); HS-2 ("a strong reason why" causal ranking); HS-3 (channels/data_gaps carry no class column, so letter-derived rows are unclassed); IN-4 (1986 eight-entity count includes `ONIX Microsoft`); IN-5 (U.2/U.9 share one identical leg; the 134 measurement rides on two source ids); NR-3 (BYTE 1976 re-assigned as an open follow-up though already measured 0); NR-4 (three perimeters for the 1975 null: ~44 vs 11 layers vs two byte totals) |
| COSMETIC | 1 | `stage_1.md:1219` prints `$2` where the byte prints `§2`; the damaged form is restored two lines of the same section down at `:1232-1234` |

**Total 20 findings, 0 BLOCKING.** The gate itself reports 0 substantive findings on the four briefed checks;
none of the 20 above is a gate-visible mechanical defect — they are carrier-support, class-discipline and
negative-result defects that the gate cannot see.

**Three most consequential, one line each:**
1. **IN-1 (HIGH)** — `conflicts.csv:3` U.3 says the 1975 founding is "corroborated across two independent
   lineages (1976 letter, 1994 filing)" when both carriers are Microsoft's own account and the 1976 letter
   never states 1975, which is precisely §3's forbidden move in the register layer later passes trust.
2. **NR-2 (HIGH)** — "there is no digitised annual-report run (N-1)" (`stage_1.md:340`, GAP-K1, Q.1) rests on a
   `YEAR:[1977 TO 1998]` + title + creator faceted query that never covered 1975-76, and is contradicted by the
   FY2017 annual-report layer the same volume cites at S4240: RD-130's class, live, and load-bearing for the
   tier and the "NOT KNOWABLE" verdict.
3. **NR-1 (HIGH)** — family (b) is written as "UNTRIED … 0 calls" (`stage_1.md:1047`) while
   `sources/web_archive/` holds two attempted CDX calls with HTTP 503 and the sidecar's own
   `UNANSWERED (not an empty result)` verdict: a dead route recorded as an unattempted one, on the single
   route that could raise this company's tier.

**STATUS of this file:** all sections written. No volume, register, `CORRECTIONS.md`, `tools/`, or
other-company file was created or modified; the only paths written are this file and (outside the repo) one
throwaway verification script in `/tmp`.
