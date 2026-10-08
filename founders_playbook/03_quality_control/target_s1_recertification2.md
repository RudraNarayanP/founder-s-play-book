# target_s1_recertification2.md — CERTIFIER (pass 2), company_042_target Stage 1

Agent `target-recert2`, claimed at `founders_playbook/03_quality_control/target_s1_recertification2.md`.
I wrote none of this corpus, repaired none of it, and repair nothing here: this file is a verdict plus a
blocker list. Excluded by name as required: `target-s1-repair2` (dead at its ceiling, had landed edits
silently) and `target-repair-2` (pass-2 repairer, author of `target_s1_repair_pass2.md`).
Method read before writing: `00_METHOD_AND_STYLE.md` §13 (schemas, register vocabulary, central id mint),
§14 rules 4/6/8/9/10/11/12, §15.2/15.4/15.5/15.6 (certifier ≠ repairer; advisory ≠ defect).
Read: `target_s1_certification.md` (the five blockers I am closing or re-opening),
`target_s1_repair_pass2.md` (every claim treated as unverified until measured),
`target_s1_audit1/2/3` sheets, and the corpus itself.
Web calls used: **0**. Corpus files edited by this pass: **none** (only my own report and the gate output).

**A note on the blocker list I was handed.** The brief's five items (Tier-1 error pages, S4211, held-but-
uncited docs, `_INDEX.md`, "whatever the sheet lists fifth") are **not** the five blockers in
`target_s1_certification.md`, which are B-1 `60,731,468`, B-2 nine withdrawn-date rows, B-3 five
register-only findings, B-4 U.032's tier expectation, B-5 the six minor legs. Items 1–4 come from
`target_s1_audit2_sources_independence.md`'s hand-off list and from the certifier's B-5(f) outbound leg;
they were routed to a sources agent and landed under **COR-19/COR-20** by the dead agent, not by the
certification. I therefore adjudicate **both** lists — nine items — because closing the wrong five would
let pass 2 self-certify against a work order of its own construction.

---

## VERDICT: **NOT-CERTIFIED**

Nothing was fabricated and no evidence was lost: I opened the carriers behind every load-bearing new claim
and they are real. The volume fails on **propagation**, in the two places §14 singles out as highest
severity — the instruction layer and the register-vs-narrative seam. A cold reader of `_MANIFEST.md` today
gets a pre-repair corpus (38,489 words, 21 sources, 68 quantitative rows, 164 register rows, 14 COR ids,
id block ending at **S4221**) and would re-mint S4222–S4225 into Microsoft's already-held space; a cold
reader of the volume's own provenance table (§T.1) gets **Tier 1** for four artifacts its `sources.csv`
re-tiered to 3 under COR-19. Both are the same failure the prior certification called blocking (B-3: "the
RD-105/106 direction, reversed"), one repair pass is enough, and no judgment call is required to fix them.

## GATE — run by me, quoted verbatim

```
python tools/gates.py --company-dir founders_playbook/01_companies/company_042_target --tier core \
  --out founders_playbook/03_quality_control/target_s1_gates_recert2.md
```
```
# Mechanical gate report -- company_042_target
Findings: **2** | Passes: 18
| quotes     | ADVISORY  | 2 of 2 checked spans unmatched (100%) -- gate precision is not established ... |
| advisory   | stage_1.md | 41534 words over the core density target 22000 -- NOT a split mandate ... |
- coverage 9 registers, 1 stage volumes, 17 source documents
- anchors  stage_1.md declares an explicit ANCHORS set (37 ids) / declares 37 anchors
- anchors  39 id(s) read as backticked references or range endpoints, not citations
- anchors  5 prose mention(s) match no declared entry, ADVISORY only: U.1, U.3, U.4, U.5, U.101
- quotes   candidates 38, attributed+checked 2, skipped 23, unmatched 2 (100%); unattributed spans unmatched: 13
- corrections 20 retraction ids; register layer reaches 20, volumes 20
csv: timeline 24x11 · quantitative 72x12 · conflicts 18x15 · sources 25x18 · data_gaps 22x8 ·
     validation 4x11 · failures 1x11 · decisions 3x15 · channels 3x11 (all S#### resolve)
keys  stage_1.md 10 source tokens all resolve
anchors citation resolution: 44 distinct ids; parity 37 narrative <-> 37 register
corrections propagation: all 20 retraction(s) reach registers and volumes
```
Exit code **1**. Reconciliation with my own findings: (i) `--out` now accepts a `.md` path — the tool/brief
mismatch pass 2 reported is closed; (ii) the **17 source documents** audit-2 could not reproduce is
reproducible and I reproduced it: `*.txt|*.htm|*.html` under `sources/` = 14 corporate_print + 1 CSA +
2 `web_archive/cdx_*.txt` = **17** (a tool-scope census, not a register census); (iii) "1 stage volume"
vs the certifier's "2" is the same scope rule (`stage_*.md` at root only counts `stage_1.md` on this run) —
no corpus change; (iv) `budget` is now an **advisory density note**, so RD-122's ruling is now encoded in
the tool and I do not re-litigate 41,534 words either (§15.4); (v) **a finding labelled ADVISORY drove the
non-zero exit** — §15.6 says advisory is not a defect, so `gates.py` contradicts the method in its exit
code while agreeing in its label. That is an orchestrator item, not a Target one, and I did not count it
against the company. (vi) The gate saw none of my seven blockers, exactly as §15.5 predicts: it has no
carrier test, no tier-vs-class test, and its quotes index covers only `sources/**`, which is why it could
not see the one attributed quote that is genuinely misattributed (RB-5).

---

## PART 1 — the five inherited blockers, adjudicated on bytes

### Inherited 1 — four Tier-1 error/apology rows (S4218–S4221): **CLOSED-WRONG-WAY** (one leg only)
*Register, measured:* all four are `tier=3` with honest classes — S4218 `UNANSWERED - dead route`,
S4219 `INDEX FLOOR - not a null`, S4220 `UNANSWERED - dead route`, S4221 `MANIFEST OF AN EMPTY WINDOW`;
independence notes read "not a source of facts and never citable as an absence"; S4221's invented quote is
replaced by the real header line plus a `NOT-A-QUOTE:` sentence. Tier census: 17 tier-1, 5 tier-3, 2 tier-2,
1 tier-4. S4217's swapped note is back to self-limiting ("CANNOT witness anything before its own floor
1994-02-10"; COR-19 withdrew "independent of the company"). I opened the six bodies and confirmed the new
passages are printed: `SEC.gov | File Unavailable`, `This page is temporarily unavailable` (7,747 B),
`Internet Archive: Temporarily Offline` (11,832 B), the 40-byte header line, and
`"hits":{"total":{"value":0,"relation":"eq"}}` (1,018 B). `503` occurs in **0** of those bytes and `500` in
**6 of 6**, so S4218/S4220's titles now say "the code is UNKNOWN" and `data_gaps.csv` U.025/U.026 now read
"what the run recorded as HTTP 503 … the code is UNKNOWN on the bytes". Citations: S4218–S4221 are named
only in `CORRECTIONS.md`, `stage_1_index.md`, `data_gaps.csv`, `_MANIFEST.md` and one merge-header line —
**no live register row treats any of them as a fact carrier**, so every citation that pointed at one still
stands and none is now a Tier-1 pointer.
*Why not CLOSED:* the re-tier never reached the narrative. §T.1's provenance table still prints
`P2S02 … Tier 1`, `P2S03 … Tier 1`, `P2S07 … Tier 1` (stage_1.md:1777–1780, `P2S04`'s tier cell left empty)
and §H.4 (840, 842), §U.3 (2129, 2135), §S.2 (1734), §T.1 (1780) still state "HTTP 503 on all four" as the
**result**, with three looser "the route 503'd" mentions at 181, 796, 2230 — **9 live lines**, all censused in
RB-2. → **RB-2**.

### Inherited 2 — S4211 scanner-as-second-lineage: **CLOSED**
`independence_note` now reads, verbatim: `NO independent lineage: a third party that SCANNED a company's own
report is a conduit, not a second origin … it sits inside the eleven-layer single lineage this volume
already states. COR-19 WITHDREW the former note (digitised by a third-party backfile service not by the
company) …`. The id was kept (correct: fix the claim, not the id). `claim_supported` is re-pointed at
`timeline.csv` row 17, closing the certifier's B-5(f) leg. S4211 is cited 12× across the corpus and I found
no surviving two-lineage claim for the same fact: "second lineage" occurs once, in the merge header's
retraction ("a scanner is not a second lineage"); "independent of the company" survives only at
stage_1.md:2304/2306, inside the COR-16 banner-marked pre-repair emission slices, and in the withdrawal
sentences of S4211/S4217. §T.1's FY1975 row grades it "Medium (cite the layer, not the company, as the
scanner)" and §T.2 states one lineage `B1S01`–`B1S11`+`B1S14`. Bonus leg I measured and the repairer did not
claim: **all five** UNVERIFIED-TLS rows (S4202/03/07/09/10) now stamp `transport UNVERIFIED TLS` in
`archived_url` and sit at Medium — audit-2's "2 of 5" asymmetry is closed.

### Inherited 3 — held-but-uncited documents: **CLOSED**, and the "0 of 36" survives my re-measure
I did not reuse the repairer's method. `sources/` = **51 files = 36 content docs + 15 `.meta.json`**
(reproduced exactly). Test 1: is each content doc's basename named by any cell of `sources.csv`? → **0 of 36
named by no row** (audit-2's 8 are now S4222/S4223/S4224/S4225). Test 2 (stricter, my own): does the
basename appear anywhere in the 30 corpus/instruction/QC files I scanned? → **0 of 36**. So the count is
true, and the stronger claim holds because the four new rows carry locators I opened myself: S4224's
`www.dhc.com` at FY1998 **L4224** and **L4284** (and `Target Corporation` 0 hits, `1962` 0 hits, as the row
says); S4225's masthead at FY2000 **L1** (`Target Corporation Annual Report 2000 G rowth |`) and
`www.target.com` at **L3743/L3827**; S4222's five `ia_search` bodies at `numFound` 0/1/4/489 exactly as the
cell states; S4223's three derived `_index` bytes at the paths and sizes it names. `data_gaps.csv` U.026 now
cites S4224/S4225 instead of asserting the layers uncited.
*What I did NOT let the "0" cover:* the original complaint's other half — files with **no provenance
sidecar** — is not 0 and is not claimed to be: 36 − 15 = **21** content docs still have no `.meta.json`
(the 19 route/index artifacts of audit-2 plus the 2 `cdx_*.txt`). That is correctly held as a FETCH REQUEST
(§14 rule 9) in pass 2 §14, and 503-vs-500 stays UNKNOWN rather than being quietly re-asserted. "Named" is
also not "used": S4222–S4225 are cited as route/provenance evidence only, which their tiers (3/2/1 `(PB)`)
correctly permit.

### Inherited 4 — `_INDEX.md` over-reach + provenance/TLS table: **CLOSED, and it matches the sidecars**
L12 now reads "**It is NOT a source of truth about what exists**"; corpus-wide, `source of truth` occurs
once in the volume (the merge note describing the rewording) and the rest in COR-20's retraction. The file
bounds itself (CIK 27419, floor 1994-02-10, names predecessor-CIK as open via U.025/U.036) and states how it
goes stale. The new "Provenance and transport" table: I re-read every figure — `raw_submissions…json`
149,561 B ✓, `submissions.json` 576,114 B ✓, `submissions.csv` 237,026 B / **2,628** data rows (2,629 lines
− header) ✓, **0** sidecars in `_index/` ✓ ("UNSTAMPED" is therefore honest), 15 sidecars total with
**10 `verified TLS` / 5 `UNVERIFIED TLS`** = FY1966/67/71/73/74 ✓ (my sidecar-by-sidecar census), the 2
`cdx_*.txt` with no sidecar ✓, and the Medium cap it asserts is actually on all five rows ✓. It does **not**
restate sidecar content as evidence — it defers to the citing `sources.csv` rows, which is the correct
division. One blemish: its header attributes the work to "certifier blocker B-4", which in the
certification sheet is the U.032/HathiTrust expectation, not this item — an instruction file that
mis-cites its own correction record. → folded into **RB-7**.

### Inherited 5 — the sheet's fifth (B-5 a–f) + the residuals pass 2 itself called PARTIAL: **NOT CLOSED (3 of 6 legs)**
- (a) **not closed.** Measured re-dated rows: 7 in `quantitative.csv` (December strings survive only in
  `notes` retraction sentences; **0** `-12-31` in any date column) + 1 in `timeline.csv` = 8. But
  `CORRECTIONS.md:20` (COR-07's own table cell) still reads "the **six** `date` cells", and
  `stage_1.md:267` still reads "the six December dates COR-01 wrote into `quantitative.csv`". "Seven
  December year-ends" exists only in COR-16's row (:30/:276). So the correction record now disagrees with
  itself, and the pass-2 claim "CORRECTIONS.md now prints seven" is **false as to COR-07**.
- (b) **not closed, and wider than reported.** Carrier: FY1975 note runs **L3246–L3251** — I read it: L3250
  ends `Each of these years` and **L3251 is `consisted of 52 weeks.`** The short locator `L3246-3250` stands
  in **six** places, not one: `timeline.csv` row 17, `conflicts.csv` (2 cells), `stage_1.md:254` (§Boundary 4,
  live prose), `CORRECTIONS.md:21` and `CORRECTIONS.md:137` — and the last two introduce a **six-line block
  quote** (CORRECTIONS L139-144, conflicts "quoted in full") that visibly runs past the range it names, so
  the correction record itself mis-points its own evidence. The corrected `L3246-3251` exists only twice, in
  `CORRECTIONS.md` and `stage_1.md`. Pass 2 named only the timeline row.
- (c) **not closed.** `[L1354` = **0** hits in the volume (so P2-07's OCR join at 1965 L1354-1355 is still
  unmarked) and the P2 preamble at `stage_1.md:2257` still promises `Passage:` is "verbatim from held bytes,
  ≤40 words, as printed". P2-10's corrupt label is now shown, so that half is closed.
- (d) **closed** — U.031 now carries the route state (`UNTRIED-2 … fetch the 2013-07-06 Twin Cities
  obituary … into sources/documentary/ with sidecars`), matching U.030/U.032/U.036.
- (e) **not closed, and correctly so** — `_parts/s1_p2.md` still says "volume 1" 2× (it holds one superseded
  footer). `_parts/*` is outside every repair write set and is the merge's audit trail; it is documentation
  debt for the orchestrator, not a company defect. I am recording it, not counting it.
- (f) **closed and verified by me** — S4203's `relevant_passage` places the locator outside the quoted span
  (`[locator L1952-1956, placed OUTSIDE the quoted span per method 14 rule 12 …]`) and restores the
  possessive; S4209's circular self-citation is replaced with the real lineage (`same lineage as
  S4201-S4211 … the former cell read [same lineage as S4208/S4209], naming ITSELF`) and the stray `U ` is
  gone. I also re-ran the repairer's codepoint claim independently: `sources.csv` contains only U+2014 (4),
  U+00A7 (7), U+2019 (2) and **0 U+FFFD** — the "`U `" seen on S4219/S4220 is a cp1252 console rendering of
  `§`, not corpus corruption. That claim is true.

## PART 2 — the certification sheet's own B-1…B-4 (pass 2 claims these closed via the dead agent)

- **B-1 `60,731,468`: CLOSED except one surviving instance → RB-4.** New row for the printed FY1966 dollar
  (`1966 | target_unit_sales_printed | 60731468 | FACT | Medium | S4203 … L409-412`), r15's
  "printed nowhere" withdrawn with the footing kept visible, r16's "only … printed anywhere" withdrawn,
  §A.1:334, §H.4 N4:834, §P:1274/1455/1663-1664, §K.7:1719 and U.021 all re-scoped to "1966 **and** 1967",
  COR-15 opened and propagated (the gate's 20-id census reaches both layers). The three extra quantities the
  sheet demanded are now rows and I opened their carrier: `161 percent` (L412), `1,184,900` (L416),
  `298,600` (L415). **Survivor:** `stage_1.md:297`, §Boundary 5's "erased loser class", still prints
  "Target-unit dollars exist for **1967 only** in FY1962-FY1968" — live prose, not a marked slice.
- **B-2 nine withdrawn-date rows: CLOSED.** All 9 `stage1,19xx-12-31` rows are still present (nothing
  deleted, RD-122's byte-identical trail intact) and each is now marked `WITHDRAWN BY` **in place** (measured
  9/9), under dated `SUPERSEDED — DO NOT RE-APPLY` banners at :901 and :2285 that state the root CSVs are
  canonical, name COR-07/COR-08, print the replacement carrier dates, and add "No row below was deleted or
  revalued; none of them may be copied into a register or cited as live". The two banners' internal
  arithmetic agrees with mine (1 + 8 = 9; `1973-12-31` ×5 across the slices).
- **B-3 five register-only findings: CLOSED.** `989,225`/`171,932,690` at §K.2:1266-1267 and §K.3:1342-1343;
  `220,511,038`/`1,088,338,000` at §E.2:664-677 with the rule now stated in prose at :672-673 ("no growth
  rate may cross FY1966→FY1967 or FY1971→FY1972 without naming which restatement it used");
  `868,336` at §P.1:1588-1591. COR-17 records the retraction of the cells that had claimed otherwise.
- **B-4 U.032: CLOSED, honestly.** data_gaps U.032's expectation cell now opens `COR-18 … WITHDREW the
  expectation "the route most likely to lift the tier from T2 to T1"` and cites **RD-127 as a measurement**
  (RD-127: 4× in the volume, 1× in data_gaps, 4× in CORRECTIONS; it was 0× corpus-wide at certification);
  §U.4:2189-2204 keeps the route **OPEN and UNTRIED**, names what remains unexamined (6 undated rows, 4
  unparsed facet records, every page past the first), states that a sector pool cannot lift a tier under
  §15.2, and hands the `periodical_harvest --query-set target_dayton_print_1955_1964` task set to the
  orchestrator because `tools/` is outside agent write scope. The two remaining "most likely to lift the
  tier" strings are the COR-18 withdrawal sentence and a banner-marked slice row (:2398). Tier re-derived by
  me, not inherited: corporate print (11 in-window layers) + one trade periodical (CSA Apr-1963, verified
  TLS, 170,260 B) = **2 families** → **T2 core is right**, and EDGAR/web-archive return 0 in-window Tier-1.
  I do not ask for the volume to be trimmed (§15.4).

---

## PART 3 — the certification questions

**6. Are the nulls named? YES, with one mis-key (RB-7).** No family is a silent zero. Filings: TRIED–
UNANSWERED (U.025 with the retry route U.036; U.027 an **index floor 2001**, not a null; the registrant
floor itself is TRIED–ANSWERED — 0 of 2,628 rows before 1994-02-10 and `_INDEX.md`'s `UNANSWERED slices:
(none)` is bounded to this CIK). Web archives: TRIED–UNANSWERED (U.026, remedy = CDX retry once IA answers
200). Corporate print: TRIED–ANSWERED, richly. Periodicals: TRIED–ANSWERED for the one leg held (§H.2's
"does not name the company once" is **argued, not assumed** — I re-ran it: `Target` 0, `Goodfellow` 0,
`Minnesota` 0, `Dayton` 2, `Hudson` 3) and TRIED–UNANSWERED for `Discount Store News` (`numFound 0`, a
catalogue absence, never a text null). Book corpora (U.032), newspaper back-files (U.033), the 17 PDF legs
(U.030), the founder-credit obituaries (U.031), a second carrier (U.034), XBRL/first-10-K (U.035),
predecessor CIKs (U.036), TLS re-verification (U.037): all **UNTRIED with the exact command attached**, and
§S.4 names auction/museum documentary collections and the other unsearched families as untried rather than
null. U.024/U.019 are re-scoped to EMPTY-within-perimeter, so the two cells audit-2 caught stating a
corpus-wide null over unrun families are fixed. All 22 `data_gaps` rows carry a `follow_up_task`, so no
High-importance gap is ownerless (§13). Boundary claims have carriers: the December leg prints at FY1975
**L3583/L3604** inside `F. INVESTMENT iN JOINT VENTURES` (L3570) — I read all three lines — and the
early-1960s leg prints at FY1965 **L397** `Since the first Target store was opened early in 1962 in`, with
the month correctly left UNKNOWN (U.002/U.018, route U.033).

**7. Is the boundary defensible? YES.** Earliest **defensible** date = the **1962 event floor**, attested by
one document (FY1965, `entered the discount merchandising field in 1962 with Target Stores, Inc.`) inside a
**FY1965 document floor** and a **1994-02-10 registrant floor**, with the three floors named as different
kinds of floor (§Boundary 2). Every rival is enumerated and defeated with a reason: `Target Corporation
1962` (wrong registrant, three years before any held byte), the 1902 Goodfellow leg (rejected as a frame,
retained at UNKNOWN rather than deleted), the archive-boundary-as-stage (refused: "would silently convert a
preservation accident into a history"), the 1969 merger (adopted as the Stage 1→2 hand-off by masthead
changeover, no day claimed), and the dispatch's re-based `1972-03-22` floor — grepped to zero and **not
written** anywhere: all 6 volume occurrences are in COR-02/P1K11 retraction language, and it appears in no
register row. The known failure mode (re-based origins) is absent, and the uploader's filename-vs-masthead
trap is decided for text (§Boundary 1, K3). One caveat, and it is RB-3: the *date* is defensible while four
`timeline.csv` rows carry it in a **class** the volume's own rule forbids.

**8. Does the register layer contradict the narrative? YES — in three places, one of them new.** Spot-check:
12 claims across the volume, each read against `sources.csv`, `conflicts.csv`, `quantitative.csv`. Passed:
E02/§A.4 1966+1967 pair (r69 RESTATED-tagged, r16 CONTEMPORANEOUS, carrier L409-412) · r15 footing vs r69 ·
r18/r64 denominator arithmetic present in-cell · r27 868,336 vs the printed 868,335 (§K.2) · r68
171,932,690 vs L825-837 · r63/r66/r67 restatement deltas · timeline row 17 (S4211, verified-TLS layer, so
High is allowed) · S4224/S4225 locators · S4222 numFound set · B02's Geisse census (3 layers, 0 from FY1968
— re-run by me) · S4215's five name counts (re-run) · CSA byte/char census. Vocabulary and keys are clean:
`stage` = `stage1` on **all 9 registers, 172 rows**, 0 numeric values; every `S####` in every register and
volume resolves; **0 unresolved `conflict_ref`** in timeline and quantitative; 40 bare-year rows, all 40
PERIOD BASIS-tagged (69/72 rows tagged; the 3 untagged carry exact period-end dates and state their basis in
prose); 7 DERIVED rows all carry `derived_arithmetic`; 0 December placeholders in any date column.
Contradictions: RB-1 (instruction layer), RB-2 (tier + 503), RB-3 (recap-as-FACT).

**9. The two defects I was told not to count — and whether I agree.**
*S4222–S4225 vs Microsoft:* confirmed as cross-company and **not** a Target content defect. Microsoft's
`sources.csv` (22 rows) holds `S4222, S4223, S4224, S4225, S4226 … S4243`, and Target's own ids are unique
inside Target, so no Target row is ambiguous; task #31 owns the mint map. I agree with the exclusion, with
one honest addendum that costs nothing and is mine to record: nothing in Target's instruction layer says the
block now runs to S4225 — `_MANIFEST.md:12` still prints "global `S4201`–`S4221`" — which is how a
cross-company collision becomes a within-company one on the next merge. That is a leg of **RB-1**.
*Advisory quotes:* **partly intake, not wholly.** I checked the two attributed-and-checked spans
individually. `source_id blocks are assigned centrally at merge, never per dossier` is **verbatim**
`00_METHOD_AND_STYLE.md` §13:329 and is invisible to the gate because the quotes index is built only from
`sources/**` — genuine intake/scope, not a defect, and I did not count it. The second is **not** intake:
`stage_1.md:234` attributes *"Fiscal year = calendar year in these reports."* to
`research/B1_dayton_print_records.md`, and that dossier contains **zero** occurrences of "calendar year" (I
searched it directly); the phrase exists only in the volume, `CORRECTIONS.md:14`, `conflicts.csv` U.011's
`claim_a` and the two `_parts` copies. It is a **quote of an inherited premise with no carrier behind it**,
which is paraphrase-in-quotes — small, but §15.6's "advisory is an intake gap" does not license it → **RB-5**.
The 13 unattributed spans I sampled are what §15.6 says they are: table prose, method restatements, and
withdrawn readings kept visible under a COR-16 banner (e.g. "route most likely to lift the tier from T2 to
T1"). Agreement: **intake, with one named exception.**

---

## BLOCKERS (execute in this order; none requires new retrieval)

**RB-1 — BLOCKING (instruction layer, §14 rule 10). `_MANIFEST.md` and `stage_1_index.md` still print the
pre-pass-2 corpus as current.**
Corpus says: pass 2 §13 records 25 sources / 72 quantitative / 172 rows / 20 COR ids; disk agrees exactly
(re-measured by me). Carriers print: `_MANIFEST.md:9` `stage_1.md | 38,489 | 261,590` (disk **41,534 w /
283,996 B**), `:12` `sources.csv | 21 rows × 18 … global S4201–S4221` (disk **25 rows**, block runs to
**S4225**), `:13` `quantitative.csv | 68 rows × 12` (disk **72**), `:29` "`stage1` on all **164** rows of
the nine registers (157 at the merge, +7 …)" (disk **172**, +8), `:82` `csv quantitative.csv 68 rows`;
`stage_1_index.md:11` 38,489 "re-measured after the 2026-09-29 repair pass", `:40` `sources.csv 21 × 18 ·
quantitative.csv 68 × 12`, `:42` "**164 rows**", `:75` "14 retraction ids". `git diff --stat HEAD` shows
both files were edited by the **first** repair pass and **never** by the dead agent or by pass 2, so a
reader of the two files every agent is told to read first is handed the superseded state — including an id
range that, combined with the Microsoft collision, is exactly how a bad re-mint happens.
*Minimal honest fix:* update the two files' per-file tables to the measured disk state (41,534 w / 283,996 B
/ sources 25 × 18 with the block `S4201–S4225` / quantitative 72 × 12 / 172 rows / 20 COR ids), keep the
older numbers as dated "at the merge" strings rather than deleting them (rule 4), and add one line naming
that `S4222–S4225` are also held by `company_011_microsoft` and are tracked cross-company as task #31.

**RB-2 — BLOCKING (register/narrative seam, the COR-19 leg that did not travel).**
Corpus says: `sources.csv` tiers S4218/S4219/S4220/S4221 = **3**, and their titles plus U.025/U.026 say the
status code is **UNKNOWN on the bytes**. Carriers print: `stage_1.md:1777` `P2S02 … | 1 | UNANSWERED`,
`:1779` `P2S03 … | 1`, `:1778` `P2S07 … | 1 | High (as a manifest, not as an absence)` — i.e. §T.1, the
volume's own provenance table, still stamps Tier 1 on the four artifacts COR-19 demoted — and `:840`/`:842`
(§H.4), `:2129`/`:2135` (§U.3), `:1734` (§S.2), `:1780`, `:181`, `:796`, `:2230` state "HTTP 503 on all four"
/ "503" / "HTTP 503 bodies" / "the route 503'd" as measured result — **9 live lines**, censused in the fix
below. The held bodies print `500` and `temporarily` and **no** `503`.
*Minimal honest fix:* change the four §T.1 rows to `3` (and `P2S04`'s empty tier cell to `3`), and qualify
each 503 assertion in the live sections as "what the run recorded; the bodies print 500 and capture no
status line, so the code is UNKNOWN (U.025/U.026, COR-19)". The census I took: **9** live lines — six flat
result assertions (`:840`, `:842`, `:1734`, `:1780`, `:2129`, `:2135`) and three loose "the route 503'd"
mentions (`:181`, `:796`, `:2230`); `:66` (merge header) and `:839` (§H.4's rule "a 403/429/503 is never an
absence") are already correct and must not be touched. Do **not** invent a status code, and leave the
FETCH REQUESTs where they are. *Same-leg item, judged and recorded rather than assumed:* `P2S05`/`S4216`
(Internet Archive item-metadata listing) is still stamped **Tier 1 / High** both in `sources.csv` and at
`stage_1.md:1781`, which audit-2's tier-inflation #3 flagged and pass 2 never addressed; I do not re-tier it
myself, and its bounded note ("the only evidence for the 1965 to 2024 layer run") keeps it honest *as used* —
the repairer should either re-tier catalogue metadata to 2 with a one-line §5 reason or state, in the row and
in §T.1, why a corpus index is being graded above the trade periodical that actually is Tier 1.

**RB-3 — SUBSTANTIVE (the volume's own class rule is not applied in `timeline.csv`).**
Corpus says: §Boundary 3.2 (`:223-226`) "A recap may not carry a FACT about a decision … the *printing* is
FACT (High, for its own year), the *event* is RETROSPECTIVE INTERPRETATION (Medium at best)", §Boundary 6
(`:305`) grades the 1962 opening exactly that way, `:585` grades the FY1968 eleven-store total as "a 1973
recap", and §U.3/U.028 caps everything resting on FY1966/67/71/73/74 at Medium. Carriers print:
`timeline.csv` row 2 `1962 … FACT/High/S4201` ("narrated in the first person plural"), row 3 `1962-early
First Target store opens FACT/High/S4201`, row 8 `1967-late … FACT/High/S4206` whose own note concedes
"printed in the FY1970 Operating Review rather than in a 1967 layer", and row 9 `1968 … FACT/High/S4204`
whose own note says "the eleven-store total is a 1973 recap (S4209 L565)" — S4209 being an **UNVERIFIED-TLS**
layer, so a High row carries a Medium-capped restated component. Row 18 files the *same* 1962 cohort
correctly as `RETROSPECTIVE INTERPRETATION at three years' remove / Medium`, so the register disagrees with
itself. This is audit-2's "confidence the carrier cannot carry — four register rows", never listed as a
blocker by either the sheet or pass 2, therefore still open.
*Minimal honest fix:* split each of rows 2/3/8/9 per the volume's own two-record rule — keep FACT/High for
the printing in the layer's own year, move the event to `RETROSPECTIVE INTERPRETATION`/Medium — and set
row 9's class/confidence for the eleven-store total to `RESTATED`/Medium with the S4209 TLS cap named. No
date changes; the 1962 floor is unaffected (Q7).

**RB-4 — SUBSTANTIVE (B-1's class survives in one live sentence).**
Corpus: `stage_1.md:297` §Boundary 5, "The erased loser class … Target-**unit** dollars exist for **1967
only** in FY1962-FY1968" — live prose, not a marked slice, and refuted by the carrier the same volume now
quotes eight times. Carrier: FY1967 layer L409-412 prints `of 1966 volume of $60,731,468` (r69, FACT,
Medium, RESTATED basis). *Minimal honest fix:* one phrase → "exist for **1966 and 1967 only** (both printed
in the FY1967 layer; COR-15)" plus a `SUPERSEDED` note if the sentence must be kept as emitted.

**RB-5 — SUBSTANTIVE-MINOR (attributed quote with no such line in the named carrier).**
Corpus: `stage_1.md:234` and `_parts/s1_p1.md:159` attribute *"Fiscal year = calendar year in these
reports."* to `research/B1_dayton_print_records.md`; `conflicts.csv` U.011 `claim_a` and
`CORRECTIONS.md:14` repeat it as the inherited premise. Carrier: the dossier contains **0** tokens of
"calendar year" (the premise is the dispatch's/merge's restatement, and the bytes refute it with four
printed late-January/early-February year-ends). *Minimal honest fix:* re-attribute to "the inherited
premise as restated by the Stage-1 dispatch and B1's dossier (no such sentence is printed in
`research/B1_dayton_print_records.md`)" or drop the quote marks; keep the refutation and U.011 intact — the
finding itself is sound and COR-01 stands.

**RB-6 — MINOR, one pass (B-5(a)/(b)/(c) residuals, counted by me, not inherited).** (a) `CORRECTIONS.md:20`
"the six `date` cells" and `stage_1.md:267` "the six December dates" → seven quantitative rows + one
timeline row = eight. (b) `L3246-3250` → `L3246-3251` in all **six** occurrences: `timeline.csv` row 17,
both `conflicts.csv` U.011 cells, `stage_1.md:254`, `CORRECTIONS.md:21` and `CORRECTIONS.md:137` (the carrier
tail `consisted of 52 weeks.` is L3251, and CORRECTIONS:139-144 / conflicts print a six-line quote under
the short range). (c) mark P2-07's OCR join `[L1354|L1355]` or re-label the P2 preamble
(`stage_1.md:2257`) as "verbatim digits, normalized labels and marked OCR joins"; the preamble currently
promises the opposite of what P2-07/P2-10 do.

**RB-7 — MINOR (id hygiene, non-blocking, listed so it is not re-derived).** (i) §S.1's payroll/wages/
headcount null is anchored to `U.028` (`stage_1.md:1723`), which in `data_gaps.csv` is the transport gap —
mis-keyed pointer; give it its own id or point at the right row. (ii) Two `data_gaps.csv` rows have no
`U.0xx` key at all ("store openings in 1963 and 1964"; "what the 1962-65 stores cost …"), so they cannot be
anchored or cited — mint keys (the merge already suggests `U.101+` free range at `:1044`). (iii)
`sources/_index/_INDEX.md:26-27` attributes its own provenance block to "certifier blocker B-4", which is
U.032, not this item. (iv) `stage_1.md:260` still says the decisive sentence was quoted nowhere "in this
volume's **37,507** words" — the volume is 41,534. (v) **Orchestrator, not company:** `gates.py` exits 1 on
a finding it labels ADVISORY (§15.6 says advisory is not a defect); `research/` and the method file are
outside the quotes index, so RB-5 is invisible to the gate — a carrier-existence check on attributed quotes
is the §15.5 self-test this company is now evidence for; `_parts/s1_p2.md` "volume 1" ×2 (B-5(e)) is
undocumented debt in an audit-trail file no agent may write; `periodical_harvest` still has no `target` task
set, which is the only thing that can settle U.032.

## WHAT I DID NOT TEST — same weight as what I did
1. Zero web calls: no URL, HTTP status or archive.org route verified. U.025/U.026/U.027/U.028 are judged
   only on whether held bytes support what the cells say about them.
2. The 17 PDF image legs do not exist on disk; the two year-end days stay UNKNOWN and I re-confirmed
   **0** `-12-31` values in any date column of any register.
3. Claim records: I opened or re-verified **17** (A01–A04, B01–B05, E02, F01, P2-02/03/05/06/07/09/10/12);
   §I–§U inline records C01/D01/G01/H01/H02 and all `B1-01…B1-12` (dossier-only, superseded) are unopened.
4. Sidecars: I byte-verified all 15 `bytes` cells and their `transport` fields, but did not audit the
   21 unsideared artifacts' retrieval histories (they are the FETCH REQUEST set), nor `publication_date` /
   `access_date` cells generally.
5. I did not re-derive the merge's fold arithmetic (157→164→172), the 34-folded/28-group id ledger, or the
   byte-identical-slice non-destruction proof; I measured end states.
6. Post-boundary `(PB)` money (FY1998/1999/2000 layers): I verified only the three locator strings behind
   S4224/S4225 and the 0-hit claims; I did not audit their financials.
7. FY1962–FY1965 and FY1968/1970–1972 Target-unit absence: RB-4's year list is taken from the printed pair
   and the volume's census, not from an exhaustive absence hunt (U.030/U.032 remain the routes).
8. `gates.py --self-test` was not run by me; my reconciliation is of its output against disk.

## CHECKS THAT FOUND NOTHING (with items covered)
1. **Register arithmetic and schema hygiene — 9 registers, 172 rows.** Sources 25 · quantitative 72 ·
   timeline 24 · conflicts 18 · data_gaps 22 · validation 4 · decisions 3 · channels 3 · failures 1 = 172,
   matching the orchestrator's STATE line exactly (and pass 2's correction that conflicts is 18, not 23).
   `stage` = `stage1` on every row of all nine; 0 numeric stage values.
2. **Citation resolvability — 5 layers.** Every `S####` in all registers and in `stage_1.md`/
   `stage_1_index.md` resolves (gate + my own token scan); **0 unresolved `conflict_ref`** across 24
   timeline and 72 quantitative rows; anchors **37↔37**; 20/20 retraction ids reach both layers.
3. **Fabrication hunt on the fresh rows — 14 new/edited citations opened (S4222–S4225 locators, 4
   `numFound` bodies, 6 demoted-artifact passages, 2 cdx sizes, the 40-byte manifest).** All present in the
   bytes at the named lines; **zero invented passages** found this pass. The old S4203 "fabricated quote"
   charge remains refuted (L1952 = `JOHN F. GEISSE`) and I did not retry it.
4. **Held-but-uncited — 36 content docs, two independent tests (row-naming and cross-file occurrence):**
   0 and 0. **Provenance/TLS table — 4 byte figures + 1 row count + 15 sidecars:** all match disk.
5. **December-placeholder hunt — every date column of all 9 registers plus the volume's live rows:** 0;
   the 8 superseded December strings survive only inside `notes` retraction sentences and marked slices.
6. **Re-based-origin hunt — `1972-03-22`, `1902`, `1946`, `1962-as-Target-Corporation` across the volume and
   9 registers:** the retracted floor appears in retraction language only, in 0 register rows; the 1902 leg
   is retained at UNKNOWN and never used to date 1902-1961; no claim rests Stage 1 on a 1999 marketing
   timeline.
7. **Confidence-cap audit — 15 rows citing the five UNVERIFIED-TLS layers:** all Medium or Low, **0 High**,
   and all 5 citing rows now stamp the transport (was 2 of 5).
8. **Arithmetic-integrity checks — 7 DERIVED rows:** every one carries a non-empty `derived_arithmetic`
   (§13); 40 bare-year rows all carry a `PERIOD BASIS` tag; the FY1966 footing difference (60,800,000 vs
   printed 60,731,468 = 0.11%) is disclosed in-cell, not smoothed.
9. **Name-census reproduction — 17 layers × 4 tokens (Target/Goodfellow/Dayton/Hudson/Geisse):**
   reproduces the volume's numbers exactly, including §H.2's "does not name the company once".
10. **Codepoint integrity of `sources.csv`:** only U+2014/U+00A7/U+2019, **0 U+FFFD** — the "stray `U `"
    defect is a console artifact, as pass 2 claimed.

## COUNTS RE-MEASURED AFTER MY LAST WRITE
`stage_1.md` **41,534** words / **283,996** B · registers **172** rows (25/72/24/18/22/4/3/3/1) · distinct
COR ids **20**, propagated to both layers · anchors **37↔37** · `sources/` **51** files = **36** content
docs + **15** sidecars, **0** uncited content docs (two independent tests), **21** content docs with no
provenance sidecar (unchanged, held open by FETCH REQUEST) · December values in any date column of any
register **0** · unresolved `S####`/`conflict_ref` ids **0** · §T.1 Tier-1 stamps on COR-19-demoted artifacts
**3** plus **1** empty tier cell (RB-2) · live 503-as-result lines **9** = six flat + three loose (RB-2) ·
wrong-locator `L3246-3250` occurrences **6** (RB-6b) · "six date cells"/"six December dates" **2** (RB-6a) ·
`[L1354` markers **0** (RB-6c) · "calendar year" tokens in `research/B1_dayton_print_records.md` **0**
(RB-5). This report and the gate output the brief ordered are the only files I wrote; no corpus file was
edited by this pass.

STATUS: WRITTEN 2026-09-30, agent `target-recert2`. Verdict **NOT-CERTIFIED**; blockers **RB-1…RB-7**
(RB-1, RB-2 blocking; RB-3, RB-4 substantive; RB-5 substantive-minor; RB-6, RB-7 minor). Inherited 2, 3, 4
and certifier B-2, B-3, B-4 are CLOSED and must not be re-opened by a later pass; inherited 1 is
CLOSED-WRONG-WAY (one leg), inherited 5 (B-5) is PARTIALLY CLOSED. No evidence may be trimmed to satisfy
the word-count advisory, and RB-1/RB-2 need no retrieval — they are propagation legs.
