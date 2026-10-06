# target_s1_recertification4.md — CERTIFIER (pass 4), company_042_target Stage 1

Agent `target-recert4`, claimed at `founders_playbook/03_quality_control/target_s1_recertification4.md`.
§15.6 exclusion holds by name: I am none of `target-repair-3`, `target-repair-3b`, `target-round4`, nor the prior
certifiers (`target-cert`, `target-recert2`, `target-recert3`). I edited **no corpus file**: one file, this report,
plus the gate output the brief ordered. Web calls: **0**. Claims: 1 path, **0 REFUSED**, no `--force`.

Chain read in order: `target_s1_recertification3.md` (verdict NOT-CERTIFIED; N-1…N-5 blockers, R-1…R-8 residuals;
its stated rule *"if N-1…N-5 close with these figures unchanged, my ruling at the next pass is
CERTIFIED-WITH-NAMED-RESIDUALS"*), then `target_s1_repair_round4.md` (the repairer's account and its self-reported
scope deviation), then the corpus: `stage_1.md`, `stage_1_index.md`, `_MANIFEST.md`, `CORRECTIONS.md`, the nine
registers, `sources/**`, `tools/web_domains.json`, and the Target `sources/web_archive/` bytes. **Every figure below
is my own re-measurement from disk, not inherited from the repairer or from recert3.**

---

## VERDICT: **CERTIFIED-WITH-NAMED-RESIDUALS**

All five blockers N-1…N-5 are **genuinely closed by measurement**, with the figures recert3 published unchanged. No
fabrication, no evidence lost, no new false statement introduced. Two independent things reached the same place:
the gate's two prescribed conditions (`corrections 24/24/24`, `anchors 40↔40`) are met with no regression, and my
own cell-by-cell re-measurement confirms every number the repairer reports. I am not bound by recert3's
pre-commitment — but I independently arrive at its ruling. **No blockers.** The residual list below (R-1…R-8
carried forward plus two I re-sharpen) is none of it company content.

## GATE — run by me, verbatim

```
python tools/gates.py --company-dir founders_playbook/01_companies/company_042_target --tier core \
  --out founders_playbook/03_quality_control/target_s1_gates_recert4.md
```
`Findings: 2 | Passes: 18 | **exit 1**`. **GATE condition MET: `corrections 24 retraction ids; register layer reaches
24, volumes 24`** ✓ and **`anchors parity 40 narrative anchors <-> 40 register anchors`** ✓ (46 distinct ids resolving;
all csv widths clean: timeline 24×11, quantitative 72×12, conflicts 18×15, sources 25×18, data_gaps 23×8, validation
4×11, failures 1×11, decisions 3×15, channels 3×11; `keys stage_1.md 15 source tokens all resolve`; S4229 classified
*protected history*). **Neither regressed — no automatic blocker fires.**

**The exit code is the R-8 tool defect, not a corpus finding, and I re-sharpen it (see NEW-2).** recert3 ran the
identical command on the round-3b corpus and recorded **exit 0** on the same two findings; my run records **exit 1**
on the same two findings (`quotes ADVISORY`, `advisory word-count`). The mechanism, read in `tools/gates.py`:
`gate_quotes` files the finding as `report.fail("quotes", "ADVISORY", "1 of 1 checked spans unmatched…")`, whose
signature is `fail(gate, subject, msg)` — so the literal **`ADVISORY` lands in the finding's `subject` field**, not
`gate` or `msg`. The exit filter `_advisory(f)` (line 735) tests only `f["gate"] in ("coverage","advisory")` or
`f["msg"].upper().startswith("ADVISORY")`; it **never reads `f["subject"]`**. With `gate="quotes"` and a `msg` that
begins "1 of 1…", an ADVISORY-severity finding is miscounted as substantive → `substantive=1` → `return 1 if
metric`. That single finding is the §15.6 intake gap recert3 already ruled "**not** counted against the company"
(`source id blocks are assigned centrally at merge…` is verbatim `00_METHOD_AND_STYLE.md` §13, invisible because the
quotes index is built from `sources/**` only). **Conclusion: zero substantive company findings; the exit-1 is a
fleet/tools bug (R-8) that has now begun firing rather than "happening to be off", and it must not be charged to
Target Stage 1.** Fix belongs to `gates.py`: classify on the finding's own severity label.

---

## PART 1 — N-1…N-5, each by my own measurement

### N-1 — `_MANIFEST.md` five register cells + sum — **CLOSED**
I re-measured all 13 files with `wc -w`/`wc -c`. Every cell disk-matches the printed figure: `sources.csv` **5,388 /
41,586** · `quantitative.csv` **8,729 / 63,567** · `timeline.csv` **1,623 / 12,251** · `conflicts.csv` **3,165 /
22,458** · `data_gaps.csv` **3,238 / 22,335** (the five recert3 found stale) · plus `stage_1.md` 42,833/292,456,
`stage_1_index.md` 1,542/10,742, `CORRECTIONS.md` 9,463/62,153, decisions 344/2,651, validation 232/1,858, failures
72/649, channels 171/1,400 — **13/13 exact**. **Sum independently re-derived: words 5,388+8,729+1,623+3,165+3,238+
344+232+72+171 = 22,962; bytes 41,586+63,567+12,251+22,458+22,335+2,651+1,858+649+1,400 = 168,755** — the published
**22,962 w / 168,755 B** is correct to the byte. **Supersession chain reads as history, not noise:** each of the two
cells the repairer re-moved prints its whole dated chain in-cell — `sources.csv` "2,698/22,693 at the 21-row merge
state → 5,242/40,482 at the round-4 open → the figures now printed" (`_MANIFEST.md:12`); `data_gaps.csv` "2,234/15,543
at the 22-row state and 2,890/19,672 at the round-4 open → 3,238/22,335" (`:16`). The two moved **because of the
pass's own N-5 writes** (S4220 and U.026 cells grew), which is exactly the honest case rule 4 requires, and the sum
sentence names recert3's 22,468/164,988 as the round-4-open measurement with the delta attributed to those two writes
rather than hidden. **0 erasures**; every prior figure survives as a dated string.

### N-2 — `stage_1_index.md` anchor census — **CLOSED**
Carrier re-read by me: `stage_1.md:1078` = `<!-- ANCHORS: U.001-U.037, U.101-U.103 -->`; `stage_1.md:2298` = "**40**
declared". My own counts: **40** narrative `**U.0xx/U.1xx**` anchor headings (U.001–U.037 + U.101, U.102, U.103) and
**40** distinct `U.###` keys in the nine registers — **40↔40, gate-confirmed.** Index lines fixed and the two
current-tense clauses retired: `:22` now "40 anchors" with "37 at the merge, pre-COR-24" kept as the dated census;
`:23-25` "was left unused at the merge and is in use now"; `:25` parity restated to **40↔40** cited to
`target_s1_gates_round4.md`; `:34-36` "reserved" struck from the present tense ("U.0–U.5 remain narrative prose only").
`_MANIFEST.md:47` (37↔37 inside the merge pass's `Before | After | Account` table) correctly **left historical**, as
ordered — a cold reader sees it in a supersession row, not a census row.

### N-3 — COR-22's false zero — **CLOSED (the substantive one; verified line by line)**
I opened every cited carrier in the bytes. `calendar year` (case-insensitive) occurs in **exactly 4** of the corporate-print
`.txt` layers, and each sentence says what the row claims:
* **FY1998 L2483** `report relate to fiscal years rather than to calendar years.` under L2481-2482 `Fiscal Year Our fiscal
  year ends on the Saturday nearest / January 31. Unless otherwise stated, references to years in this` ✓
* **FY1999 L2001** same sentence; L2002 `years 1999, 1998 and 1997 consisted of 52 weeks.` ✓
* **FY2000 L1997** same sentence; L1995-1996 the same `Saturday nearest` preamble ✓
* **FY1975 L2978** `have adopted a calendar year as their`, inside L2976-2981: `All the joint ventures of the Real Estate
  subsidiaries have adopted a calendar year as their fiscal year. See Note F for condensed financial statements of the
  combined joint ventures.` ✓

The **withdrawal keeps its scope and citation form**: COR-22's row (`CORRECTIONS.md:36`) still retracts only the
*quotation-as-verbatim-single-line* form and keeps `id`/scope unchanged, keeps the conflict and COR-01 standing, and
keeps the refuted "0 times" visible as the row's dated record (§14 rule 4). **FY1975 L2978 is attached to COR-08's
joint-venture story, not orphaned** — the COR-22 row explicitly names it "the accounting-policy sentence in the very
layer whose December-31 prints COR-08 traced to `F. INVESTMENT iN JOINT VENTURES`," and I verified COR-08's own legs
L3570 (`F. INVESTMENT iN JOINT VENTURES`), L3578-3579 (`Condensed combined … joint ventures / follow:`), L3582-3583
(`… FOR THE YEAR ENDED DECEMBER 31, 1975`), L3604 (`DECEMBER 31, 1975`) all print as quoted. §14 rule 11 is satisfied:
an uncited carrier on the shelf is now named by the live retraction it supports.

**The certifier's own denominator — my ruling: it is a genuine auditor error, and it is now correctly recorded.**
recert3 wrote "four hits across the **28 `.txt` layers** under `sources/corporate_print/`." Disk: that directory holds
**28 files, 14 `.txt` + 14 `.json` sidecars.** recert3 conflated the file count with the `.txt` count. The repairer
measured it, stated **both** denominators ("4 of the 14 held `.txt` layers … (28 files in that directory)"), and
flagged the conflation in `stage_1_repair_round4.md` §3, so the next reader need not re-litigate it. I record it as
**auditor error AE-1** — the substantive count (4 layers) recert3 published was correct; only its denominator label
was wrong, and the correction is accurate on disk.

### N-4 — mis-pointers, count, provenance — **CLOSED on the authoritative layer; one clause left as a named residual**
* **(a)** `CORRECTIONS.md:21` (COR-08 row) and `:141` (the COR-08 prose, above the six-line block quote at `:143-148`)
  both now print **L3246-3251** with `L3246-3250` retained inside their own retraction clause. Carrier verified: L3246-3251
  are six printed lines, tail `consisted of 52 weeks.` is **L3251**, L3252 blank. My sweep of `L3246-3250` across `*.md`
  returns **4 hits, 0 live** — all four inside retraction/retention clauses (CORRECTIONS `:21`,`:33`,`:141`,
  `stage_1.md:274`). ✓
* **(b)** `CORRECTIONS.md:20` (COR-07 row) now opens "the **eight** re-dated `date` cells" with "six as first counted"
  retained quoted, and plainly says COR-21's claim to have printed the count "where each stale `six` stood" had not
  reached the row it is about. My sweep of "the six `date`" returns **1 hit, quoted-then-superseded inside COR-07.** ✓
* **(c)** The COR-23 provenance clause is present in the **master row** (`CORRECTIONS.md:37`: "assigned post hoc … not
  minted for RB-1 … the reserving agent died … unrecoverable from disk … deliberately did not re-tag … COR-19/COR-15").
  The **volume leg `stage_1.md:27` does not carry it** — `stage_1.md` is off the repairer's owned list and un-claimed.
  Per recert3's own framing ("the master row is the file agents read to learn what to believe"), the authoritative
  surface is closed; the missing one-clause volume restatement is **named residual NR-1**, not a blocker.

### N-5 — family (b) route named + Target registered + lineage cell fixed — **CLOSED**
`data_gaps.csv` U.026 `follow_up_task` now supersedes the hand retry with the §15.1 reason, names
`tools/cdx_intake.py`, states the scripted command, and raises the orchestrator FETCH REQUEST for slug registration
with its provenance. `tools/web_domains.json` `target` slug is **present as the 6th slug** (`centene, cencora,
elevance, marathon, microsoft, target`) with domains `dhc.com`/`target.com`, window 1996-2002, and I verified the
provenance lines actually print: **FY1998 L4224** `…available on the internet at www.dhc.com.` and **L4284**
`(612) 370-6948 www.dhc.com` (count 2); **FY2000 L3743** `on the Internet at www.target.com.` and **L3827** `…612.370.6948,
www.target.com` (count 2). `sources.csv` S4220 `independence_note` is rewritten off the lineage field (see Part 5).

---

## PART 2 — the scope deviation, and the remaining items

**Ruling on the off-owned `data_gaps.csv` edit: ACCEPTABLE, and correct.** N-5(a)'s remedy cell lives *only* in
`data_gaps.csv` U.026 — recert3's own blocker text placed it there ("Repair: name the script in the remedy cell").
Closing an assigned blocker therefore *required* editing that file. The brief's claim protocol ("claim each path; if
REFUSED, skip and report") supplies the test the repairer applied: the claim on `data_gaps.csv` **ATTACHED** (no live
owner), so editing it is authorized, and the repairer **self-reported the deviation at §0 rather than conceal it.**
That is the disciplined way to finish an assigned blocker whose carrier sits just outside the owned list. I hold it
against the repairer in no way.

**Ruling on the remaining open halves — named residuals, none a blocker:**
* **NR-1 (was N-4c volume leg)** `stage_1.md:27` lacks the post-hoc-assignment clause. Off-owned/un-claimed; master row
  authoritative and carries it. One clause on the next legitimate open.
* **R-2** `stage_1.md:281` self-count still "in this volume's **41,534** words" vs disk **42,833** — the sentence itself
  dates it ("re-measured 2026-09-30"), the authoritative count lives in `_MANIFEST.md:9` (correct), and the file is
  off-owned. Reads as history, not noise. Named residual.
* **R-3** §U emission-slice 503/tier wording `stage_1.md:2364/2366/2367` — inside the dated `SUPERSEDED — DO NOT
  RE-APPLY` banner (COR-16/B-2); the repairer's refusal to rewrite another pass's audit trail was correct. Named residual.
* **R-4** `_parts/s1_p1.md:159` stale quote and `_parts/s1_p2.md` "volume 1" ×2 — superseded merge audit trail,
  `SUPERSEDED` in the manifest, outside every agent's write set. Named residual.
* **R-1** `sources/_index/_INDEX.md:26-27` "certifier blocker B-4 / COR-20" — ambiguous source label, dated cell,
  self-disambiguating via the COR-20 id; not my file set. Named residual.

## PART 3 — family (b) after the first Target CDX run — **honest**

`sources/web_archive/_RUN.json` (which I read): `slug=target`, `attempted=2`, **ANSWERED=1 / NULL=0 / UNANSWERED=1 /
UNTRIED=0**, identity `1+0+1+0=2 vs 2 → OK`, `requests_used=12 of 20`. `dhc.com` verdict **ANSWERED**, `http_status`
200, `captures=500` with note *"500 captures, enumeration hit --limit 500: this is a FLOOR, not a census — raise
--limit before concluding anything about coverage."* `target.com` verdict **UNANSWERED**, `captures: None`, note *"no
answer after 3 tries (IncompleteRead: IncompleteRead(32911 bytes read))."* I confirmed the artifact footprint:
`web_archive/` holds **20** files — the run created **18** (8 `dhc.com_*.html` bodies, each with a `.meta.json`
sidecar, + `target.com_1996_2002.UNANSWERED.md` + `_RUN.json`), 2 pre-existed. The 8 dhc bodies are dated
**19961222 / 19970217 / 19970412 / 19981207 / 19990208 / 20000229 / 20010106 / 20020109** — earliest 1996-12-22,
every one **1996-2002**, i.e. **all post-boundary `(PB)`, none inside the 1962–1975 window.**

**My ruling: U.026's new state `TRIED–ANSWERED-WITHOUT-IN-WINDOW-TEXT` is the honest one.** The route now works and
returned nothing in-window — precisely what family (b)'s mid-1996 floor predicts — and the row says plainly that the
T2 tier does not move. Both limit-legs are reported **as limits, not nulls**: the 500-capture enumeration is flagged a
**floor** (a census needs `--limit` raised, an item the repairer correctly names as `cdx_intake.py` scope it does not
hold), and `target.com` is a **transport failure** (`UNANSWERED`, `IncompleteRead ×3`) never written as a coverage
absence. `NULL=0` in the run and the tool's own `never_write_empty_as_null` policy line hold the distinction. No
over-claim: the run does not pretend the 8 bodies are Target history, nor that the census is complete.

## PART 4 — the outage-banner pair — **clean; no fact rests on them**

`sha256sum` by me: `sources/web_archive/cdx_dhc.txt` = `cdx_targetcom.txt` = `company_011_microsoft/…/cdx_microsoft_com_earliest_200.json`
= its `_retry.json` = **`e084d527921708642a79724e9f0210da659bbc0905c6ce9a3a1f416e4628091c`**, 11,832 B each — four files,
two companies, one byte-stream. I opened the body: title `Internet Archive: Temporarily Offline` — an outage banner,
not Target content. Both are **sidecarless** (no `.meta.json`). **No Target fact rests on them:** my scan of the nine
registers finds `S4218/S4219/S4220` cited in **only** `data_gaps.csv` (as route state) and their own `sources.csv`
rows — **0 mentions in every fact register** (quantitative/timeline/conflicts/decisions/failures/validation = 0/0/0/0/0/0).
**S4220 `independence_note` no longer uses the lineage field for what §13 reserves it for:** it now reads "not a
source of facts and never citable as an absence; ONE ARTIFACT CAPTURED TWICE … no lineage, no independence, no
corroboration … the pair may never be counted as two observations," with the sha and the cross-company identity and
the FETCH REQUEST for the absent sidecars; the superseded "independent of the company but unreachable" is retained
in-cell as its dated record. Tier 3, `evidence_class = UNANSWERED - dead route`. `why_missing` on U.026 carries the
same sha so the pair cannot be double-counted. **Closed.**

## PART 5 — the id-namespace question and the held-mint restraint

**My ruling: holding the 9 new artifacts unregistered is correct restraint, NOT a Stage 1 blocker.** The next Target
increment is `S4226`, inside `company_011_microsoft`'s held `S4222`–`S4229`, and task #31's mint map does not exist;
minting into a colliding range would be the defect the whole chain has guarded against. The 9 artifacts are
enumerated in U.026 and `_RUN.json` and their registration is an orchestrator FETCH REQUEST. Target's own ids remain
unique inside Target and every `S####` token in every register and both volumes resolves (gate `csv … all resolve`,
`keys 15 tokens all resolve`). Certification of one company's Stage 1 is not hostage to another's register.

**Position on the id namespace, stated once for the record (three tools assume different scopes):** `source_id` is
**company-scoped by the way `gates.py` resolves it** (a 4-digit, company-index block) but is **written as if
globally-unique by the `S42xx`-by-dispatch-order mint scheme**. These are incompatible. The scheme — not Target, not
Microsoft — is the defect: it handed `S4222`–`S4229` to two companies. Required fix at the fleet level before any
cross-company union, upload, or `merge_census`-style join: an explicit composite `(company, source_id)` namespace (or
a global central mint), with per-company ranges that provably do not overlap. Until then the four-surface disclosure
(`_MANIFEST.md:12`, `stage_1_index.md:63-65`, `stage_1.md:24-26`, `sources.csv` S4225 notes) and the
"never re-minted here" rule are adequate interim protection — which is why this stays **task #31, orchestrator
scope, and off Target's Stage 1 verdict.**

---

## CHECKS THAT FOUND NOTHING (with item counts)

1. **Instruction-layer re-measure** — 13 files × (words, bytes) + the nine-register sum + row counts (25/72/24/18/
   23/4/3/3/1 = 173): **all exact, 0 stale cells**, 0 erasures (every superseded figure retained as a dated string).
2. **Anchor census, four independent ways** — carrier decl at `:1078`, self-decl at `:2298`, my narrative-heading
   count (40), my register-key count (40), gate parity (40↔40, 46 distinct): **no disagreement**.
3. **N-3 carrier census** — `calendar year` in exactly 4 corporate-print `.txt` files; 3 `(PB)` post-boundary
   (FY1998/99/2000), 1 in-window (FY1975 L2978); all four sentences verbatim against the row; COR-08's 4 JV legs
   (L3570/3578/3582/3604) confirmed: **0 mis-citations**.
4. **Range/pointer sweeps** — `L3246-3250` 4 hits 0 live; `L3246-3251` correct at the 6 carriers; "the six `date`
   cells" 1 hit (quoted-superseded); "0 times in any held corporate-print" 1 hit (withdrawn inside SUPERSEDED):
   **0 live false counts**.
5. **Negative-artifact lineage hunt** — S4218/S4219/S4220 cited by 0 fact rows (fact-register mentions 0/0/0/0/0/0);
   §T.2 counts no pair; outage banners witnessed only the archive's outage.
6. **Codepoint integrity of the raw-substitution edits** — `data_gaps.csv`, `sources.csv`, `CORRECTIONS.md`,
   `_MANIFEST.md`, `stage_1_index.md`: **0 U+FFFD** each (the mojibake in console output is cp1252 rendering of
   em/en-dashes and §, not file corruption).
7. **CDX run arithmetic** — `_RUN.json` per-state identity 1+0+1+0=2=attempted, requests 12≤20, 8 bodies = 8
   sidecars, all capture-years ∈ 1996–2002, none ∈ 1962–1975: **internally consistent, honestly bounded**.
8. **Domain provenance** — `www.dhc.com` FY1998 L4224/L4284 and `www.target.com` FY2000 L3743/L3827 confirmed to
   print (count 2 each): **0 invented domains in `web_domains.json`.**

## WHAT I DID NOT TEST — same weight as what I did
1. **0 web calls** — no URL/HTTP/archived.org route verified; `captures=500` and the `IncompleteRead` are read off
   `_RUN.json` and the stored bytes, which is exactly why they are recorded as a floor and a transport failure.
2. `gates.py --self-test` not run by me; my exit-code ruling is `gates.py` source (lines 516, 650, 735, 976) plus the
   table's severity column, reconciled against disk.
3. I opened the two `cdx_*.txt` and the 8 `dhc.com_*.html` only enough to confirm the banner identity, the sidecars,
   and the capture years — I did not read the 8 `(PB)` snapshot bodies as content, because none is in-window.
4. The 17 PDF image legs, U.030–U.037 UNTRIED legs, and `periodical_harvest` (the only route that can settle U.032)
   remain out of scope, unchanged from recert3.
5. I did not audit every inline claim record or the merge's 34-folded/28-group id ledger, nor `publication_date`/
   `access_date` cells generally.

## COUNTS RE-MEASURED AFTER MY LAST WRITE
(writes: this report + `target_s1_gates_recert4.md`; **no corpus file touched**, so all corpus figures are stable)
`stage_1.md` **42,833 / 292,456** · `stage_1_index.md` **1,542 / 10,742** · `CORRECTIONS.md` **9,463 / 62,153** ·
`_MANIFEST.md` **2,750 / 17,608** · nine registers **173 rows** (25/72/24/18/23/4/3/3/1) = **22,962 words / 168,755
bytes** (manifest sum ✓) · per-file cells `sources 5,388/41,586 · quantitative 8,729/63,567 · timeline 1,623/12,251 ·
conflicts 3,165/22,458 · data_gaps 3,238/22,335 · decisions 344/2,651 · validation 232/1,858 · failures 72/649 ·
channels 171/1,400` — all disk-exact · COR ids **24**, gate reach **24/24/24** · anchors **40 ↔ 40**, 46 distinct ·
`sources` block **S4201–S4225** (25 `source_id` values; S4226–S4229 appear only inside the Microsoft collision note) ·
`calendar year` in held corporate print **4 of 14 `.txt`** (28 files in dir) · `L3246-3250` live mis-pointers **0** ·
live "0 times" census **0** · live "six date cells" **0** · PERIOD BASIS tags **69/72**, bare-year **40/40 tagged**,
DERIVED **7/7 with arithmetic** · `-12-31` in date columns **0** · U+FFFD in edited files **0** · `cdx_*.txt` sha
`e084d527…` shared by **4** files / **2** companies, **0** sidecars, fact-register citations **0** · `web_archive/`
**20 files** (run-created 18 = 8 bodies + 8 sidecars + 1 UNANSWERED + `_RUN.json`) · `web_domains.json` slugs **6**
(target = 2 domains) · gate **exit 1** (2 findings, both ADVISORY; substantive company findings **0**) · files written
by this pass: this report + the gate sheet; **no corpus file edited**.

## NAMED RESIDUALS (recorded, not blocking)
NR-1 `stage_1.md:27` missing COR-23 post-hoc-assignment clause (master row carries it). R-1 `_INDEX.md:26-27`
"blocker B-4" label ambiguity. R-2 `stage_1.md:281` self-count 41,534 vs 42,833 (dated string; `_MANIFEST.md:9`
authoritative and correct). R-3 §U emission-slice 503/tier wording under the SUPERSEDED banner. R-4 `_parts/` stale
quote and "volume 1" ×2. R-5 sidecars: 8 new dhc bodies carry them; the 2 `cdx_*.txt` + 19 route/index artifacts
still have none (FETCH REQUESTs stand). R-6 period-basis census **discharged** (69/72, 40/40, 7/7 verified). R-7
`target_s1_repair_round3b.md` §0/§6.6 "nothing committed" stale after RD-139 (QC history). **NEW-1** — auditor error
AE-1: recert3's "28 `.txt` layers" conflated the 28-file directory count with its 14 `.txt` files; corrected in-corpus
with both denominators by round-4. **NEW-2 (R-8 sharpened)** — `gates.py` exit-code-vs-ADVISORY contradiction is
**live, not "off this round"**: the ADVISORY label sits in the finding's `subject` field while the `_advisory()`
filter reads only `gate`/`msg`, so the §15.6 intake ADVISORY forces exit 1 on a corpus with **zero substantive
findings** (recert3 got exit 0 on the same findings). Tools/orchestrator scope; must not be charged to Target. The
`S42xx` cross-company mint scheme (**task #31**) is now sharper — 9 real artifacts wait on the mint map.

---

STATUS: WRITTEN 2026-10-06, agent `target-recert4`. Verdict **CERTIFIED-WITH-NAMED-RESIDUALS**. **N-1, N-2, N-3,
N-4, N-5 are all closed by my own measurement, with recert3's figures unchanged** (22,962/168,755 exact to the byte;
40↔40 confirmed four ways; the four `calendar year` layers verified verbatim; the `L3246-3251` range fixed; the COR-23
provenance clause on the authoritative master row; the family-(b) route named, registered with verified repo-line
provenance, and honestly reported as a floor + a transport failure). The gate's prescribed conditions
(`corrections 24/24/24`, `anchors 40↔40`) are met with **no regression**; the gate's exit-1 is the R-8 tool defect,
not a company defect. The off-owned `data_gaps.csv` edit was **acceptable and correctly self-reported** (an assigned
blocker's carrier lived only there and the claim ATTACHED). The id-namespace is a company-scoped field mis-minted
globally — task #31, orchestrator scope, off this verdict. Nothing may be trimmed to satisfy the 42,833-word ADVISORY.
