# target_s1_repair_round4.md — company_042_target Stage 1, round 4 (propagation repair)

**Agent:** `target-round4` (repairer only — this is NOT a certification; §15.6).
**Brief:** close N-1…N-5 of `target_s1_recertification3.md` (verdict NOT-CERTIFIED on propagation only, ≈10 cells, no
retrieval) plus the R-1…R-8 residuals it names. **Method:** §14 rule 4 (supersede, never erase) and rule 10 (the
instruction layer re-imports stale claims). **Web calls made by me:** 0 (the one network action was the intake script
the brief ordered; see N-5).

STATUS: WRITTEN. **N-1, N-2, N-3, N-4, N-5 are all CLOSED.** Every figure below is my own measurement taken from disk
after my last corpus write, not inherited from the certifier's or the repairer's counts.

---

## 0. Claim / write record

Claimed and released with `tools/scaffold.py` as `target-round4`; **0 claims REFUSED, 0 `--force` used.**
Written: `_MANIFEST.md`, `stage_1_index.md`, `CORRECTIONS.md`, `sources.csv`, `data_gaps.csv`,
`tools/web_domains.json`, `sources/web_archive/**` (created by the ordered `cdx_intake.py` run, not by hand), this log,
and the gate sheet `target_s1_gates_round4.md`.

**Scope note the certifier should price.** `data_gaps.csv` is **not** on my brief's owned list, and N-5(a)'s remedy cell
lives only there (`U.026` `follow_up_task`) — the brief's own claim protocol ("claim each path; if REFUSED, skip and
report") was the test I applied: the claim **ATTACHED** (no other agent holds it), so I edited it and report it here
rather than leave N-5(a) half-done. `stage_1.md`, `timeline.csv`, `conflicts.csv`, `quantitative.csv` and `tools/cdx_intake.py`/
`sec_intake.py` were **not** touched: `stage_1.md:27` (the volume half of N-4c) and `stage_1.md:281`/`_INDEX.md:26-27`
(R-1/R-2) stay with their owners — see §6.

## 1. N-1 — `_MANIFEST.md:12-16` five Words/Bytes rows — **CLOSED**

Re-measured all 13 files myself before and after writing. Five cells published pre-round-3 values.

| file | published (before) | disk (measured at open) | printed now (after my last write) |
|---|---|---|---|
| `sources.csv` | 2,698 / 22,693 | 5,242 / 40,482 | **5,388 / 41,586** |
| `quantitative.csv` | 7,468 / 55,010 | 8,729 / 63,567 | **8,729 / 63,567** |
| `timeline.csv` | 1,335 / 10,433 | 1,623 / 12,251 | **1,623 / 12,251** |
| `conflicts.csv` | 3,021 / 21,489 | 3,165 / 22,458 | **3,165 / 22,458** |
| `data_gaps.csv` | 2,234 / 15,543 | 2,890 / 19,672 | **3,238 / 22,335** |

`sources.csv` and `data_gaps.csv` moved again **because of this pass's own edits** (N-5b and N-5a), so each cell now
prints the chain (merge state → round-4 open → final) with both superseded pairs retained as dated strings (rule 4).
The four unedited registers and both `_parts` rows already matched disk byte-for-byte, and I re-confirmed them.

Also corrected in the same pass: `stage_1_index.md` **1,351 / 9,432 → 1,542 / 10,742** and `CORRECTIONS.md`
**8,804 / 57,872 → 9,463 / 62,153** — both stale *through my own N-2/N-3/N-4 edits*, which is why the re-measure was
done last, not first. `stage_1.md` **42,833 / 292,456** unchanged (untouched by this pass) ✓.

New line under the table: **nine-register sum now 22,962 w / 168,755 B** (published 17,575 / 141,726; the
certifier's round-4-open measurement 22,468 / 164,988 is named in the same sentence rather than hidden, the delta
being this pass's two register writes).

**Line 13 period-basis census** — re-derived column-aware myself: **69 of 72** rows carry a literal `PERIOD BASIS`
tag, bare-year rows **40**, **all 40 tagged**, `DERIVED` rows **7**, **all 7 with non-empty `derived_arithmetic`**,
`stage=stage1` 72/72, **0** `-12-31` in the `date` column, 0 empty cells. The published "65 of 68 / 38 bare-year" is
retained in-cell as the dated 68-row-state census it was, and the round-3b caveat that asked for a re-measure is
recorded as **closed by this pass** (R-6 discharged).

## 2. N-2 — `stage_1_index.md` anchor census — **CLOSED**

Carrier re-read: `stage_1.md:1078` = `<!-- ANCHORS: U.001-U.037, U.101-U.103 -->`; `stage_1.md:2298` = "**40** declared";
this pass's gate = **40 narrative ↔ 40 register**, 46 distinct ids resolving. Three lines fixed, and the two clauses
that made them read as current:

* `:22` `37 anchors` → **`ANCHORS: U.001-U.037, U.101-U.103` — 40 anchors**, with "37 at the merge, pre-COR-24" kept
  as the dated census.
* `:23-24` "`U.101-up` … was left unused" → superseded in place: the range **is in use now** (COR-24/RB-7 minted
  U.101–U.103 on 2026-09-30 for three formerly-unkeyed `data_gaps.csv` rows).
* `:25` "37 narrative ↔ 37 register" → **40 ↔ 40**, cited to `target_s1_gates_round4.md`, with rule 12's reason
  written into the cell (a stale count here makes a later pass "discover" three anchorless registers).
* `:35-36` "the reserved `U.101`" → **"reserved" struck from the present tense**: U.101–U.103 are **minted keys**
  citing three real rows; `U.0`–`U.5` stay narrative prose, ADVISORY only.

**`_MANIFEST.md:47` not touched**, as ordered — its 37↔37 sits in the merge pass's `Before | After | Account` row and is
correctly historical. Same for the dated 2026-09-26 / 09-29 gate-record blocks at `:62` and `:83` (they name "the
reserved `U.101`" and "37 ↔ 37" *as that pass's record*, which is rule 4 history, not a live census).

## 3. N-3 — COR-22's false zero — **CLOSED** (the substantive one)

Each line opened in the bytes first. My census: `calendar year` (case-insensitive) occurs in **4 of the 14 `.txt`
layers** held under `sources/corporate_print/` — **28 files in that directory** (the certifier's "28 `.txt` layers" is
the file count, not the `.txt` count; both denominators are stated in the row so the next reader need not re-litigate
it) — plus the one dossier line.

| carrier | line | print |
|---|---|---|
| FY1998 | **L2483** | `report relate to fiscal years rather than to calendar years.` (under L2481-2482 `Fiscal Year Our fiscal year ends on the Saturday nearest / January 31. Unless otherwise stated, references to years in this`) |
| FY1999 | **L2001** | same sentence, L2002 `years 1999, 1998 and 1997 consisted of 52 weeks.` |
| FY2000 | **L1997** | same sentence, L1995-1996 the same `Saturday nearest` preamble |
| FY1975 | **L2978** | `have adopted a calendar year as their` — sentence runs L2976-2981: `All the joint ventures of the Real Estate subsidiaries have adopted a calendar year as their fiscal year. See Note F …` |

COR-22 superseded in place: the **0-times half is withdrawn by the row itself**, the citation-form retraction and the
id/scope **stand unchanged**, and the refuted zero is kept visible as the row's dated record. The four carriers are
cited with what each buys: FY1998/99/2000 as a **second explicit documentary refutation** of fiscal=calendar, flagged
**`(PB)` post-boundary, never for 1962–1975**; FY1975 L2978 as the accounting-policy sentence **inside the same layer**
whose December prints COR-08 traced to `F. INVESTMENT iN JOINT VENTURES` (L3570), `Condensed combined … joint ventures
follow:` (L3578-3579), `FOR THE YEAR ENDED DECEMBER 31, 1975` (L3582-3583), `DECEMBER 31, 1975` (L3604) — an uncited
carrier now named by the live retraction it supports (§14 rule 11).

## 4. N-4 — mis-pointers, a count, and a provenance clause — **CLOSED**

* **(a)** `CORRECTIONS.md:21` (COR-08's own row) and `:141` (above the six-line quote at `:143-148`) now print
  **L3246-3251**, each with `L3246-3250` retained inside that row's own retraction clause exactly as the four
  previously-fixed places do. Verified in the carrier: L3246-3251 are six printed lines and the tail
  `consisted of 52 weeks.` **is L3251**; L3252 is blank.
* **(b)** `CORRECTIONS.md:20` (COR-07's own row) opens "the **eight** re-dated `date` cells" — my re-derivation:
  7 `quantitative.csv` rows r54-r60 (r54-r57 `1974-02-02`, r58 `1970-01-31`, r59 `1973-02-03`, r60 `1975-02-01`) +
  1 `timeline.csv` row 23 = **8**; "six as first counted" retained, and the cell says plainly that COR-21's claim to
  have printed the count "where each stale `six` stood" had **not** reached the row the correction is about.
* **(c)** COR-23's provenance clause added to `CORRECTIONS.md:37`: the number was **assigned post hoc as a reasoned
  judgement**, not minted for RB-1 from the start — the reserving agent died at the turn ceiling with a 285-byte stub,
  what it reserved for is unrecoverable from disk, and round-3b deliberately did not re-tag the dead agent's correct
  RB-2/RB-4 edits (which stand under COR-19 / COR-15). **Volume leg `stage_1.md:27` not written** — outside my brief's
  file set and not claimed; the master row is the file agents read to learn what to believe, and it now carries it (§6).

## 5. N-5 — family (b) route named, Target registered, lineage cell fixed — **CLOSED**

* **Provenance verified before writing** (all four citations opened): `www.dhc.com` at FY1998 **L4224**
  (`Information about Dayton Hudson is also available on the internet at www.dhc.com.`) and **L4284**
  (`(612) 370-6948 www.dhc.com`) — 2 occurrences in that layer; `www.target.com` at FY2000 **L3743**
  (`on the Internet at www.target.com.`) and **L3827** (`777 Nicollet Mall, … 612.370.6948, www.target.com`)
  — 2 occurrences. `www.dhc.com` count in FY1998 re-measured = 2; `www.target.com` in FY2000 = 2.
* `tools/web_domains.json`: **`target` slug added** (6th slug; was 5), 2 domains `dhc.com` / `target.com`, window
  **1996-2002** with each entry citing the file, the line numbers and the register ids (S4224/S4225, COR-20), and each
  `why` stating that no result from this entry can lift the tier. JSON re-parsed after writing ✓.
* `data_gaps.csv` **U.026 `follow_up_task`** now names `tools/cdx_intake.py` and replaces the hand retry with the
  scripted command, records the orchestrator FETCH REQUEST for slug registration with its provenance, and states the
  ceiling (family (b)'s floor is mid-1996 vs the 1962–1975 window) so the route opens without re-pricing T2.
* **Run executed:** `python tools/cdx_intake.py run --slug target --max-requests 20` →
  **per-state counts ANSWERED=1, NULL=0, UNANSWERED=1, UNTRIED=0** (identity 1+0+1+0 = 2 raw / 2 unique slots vs
  attempted 2 → OK), **12 of 20 requests used**.
  * `dhc.com` — HTTP **200**, enumeration hit the 500-capture **limit (a floor, not a census)**, **8 snapshot bodies
    stored with `.meta.json` sidecars**: `dhc.com_19961222005842 / 19970217135039 / 19970412090823 / 19981207043436 /
    19990208012648 / 20000229040123 / 20010106121500 / 20020109061457.html` (3,046 / 3,353 / 16,231 / 19,849 B etc.),
    earliest capture **1996-12-22** — **all 1996-2002, i.e. post-boundary `(PB)`, none in-window**.
  * `target.com` — **UNANSWERED**, transport failed after 3 tries (`IncompleteRead(32911 …)`), recorded at
    `sources/web_archive/target.com_1996_2002.UNANSWERED.md`.
  * `_RUN.json` written by the tool. U.026's own cell now records this result and moves the gap from
    TRIED–UNANSWERED to **TRIED–ANSWERED-WITHOUT-IN-WINDOW-TEXT** — the route works and still returned nothing in the
    stage window, which is what the floor predicts; **tier unchanged**.
  * **No `sources.csv` row minted for the 9 new artifacts**: Target's next increment would be `S4226`, inside
    `company_011_microsoft`'s held `S4222`–`S4229`, and task #31's mint map does not exist — the artifacts are
    enumerated in U.026 and in `_RUN.json` and their registration is an orchestrator FETCH REQUEST.
* **S4220 `independence_note`** rewritten off the lineage field: `not a source of facts and never citable as an
  absence; ONE ARTIFACT CAPTURED TWICE …` with the sha and the cross-company identity. **My own hashes:**
  `cdx_dhc.txt` = `cdx_targetcom.txt` = **`e084d527921708642a79724e9f0210da659bbc0905c6ce9a1f416e4628091c`**
  (11,832 B each), matching the certifier's; `why_missing` carries the same sha so the pair cannot be counted twice.
  The superseded wording is retained inside the cell as its dated record, and the **no-sidecar FETCH REQUEST stands**
  for these two old bodies (the eight NEW ones do have sidecars).

## 6. Sweeps run, with hit counts (every one)

* `calendar year` across `sources/corporate_print/**/*.txt` → **4 layers / 4 lines** (FY1975 L2978, FY1998 L2483,
  FY1999 L2001, FY2000 L1997); across all of `sources/` → **17 `.txt`** files exist (14 corporate print + 1 periodical
  + 2 web_archive), hits confined to the 4 above.
* `L3246-3250` in `*.md` after the fix → **4 hits, 0 live**: `stage_1.md:274` (inside "the former locator … truncated"),
  `CORRECTIONS.md:21`, `:33`, `:141` — all four inside retraction/retention clauses. `L3246-3251` → **5** hits in
  `CORRECTIONS.md`.
* `the six ` + backticked `date` + ` cells` → **1** hit, and it is the quoted-then-superseded phrase inside COR-07's
  own row; the row's operative count is **eight**. `0 times in any held corporate-print` → **1** hit, the withdrawn
  zero quoted inside COR-22's SUPERSEDED clause.
* `cdx_intake` in the company directory: **0 → 4** (`sources.csv` S4220 notes-area cell, `data_gaps.csv` U.026 ×2,
  `CORRECTIONS.md`-adjacent text in the two cells I wrote). `web_domains` in the company directory: **0 → 1** (U.026).
* `-12-31` in any `quantitative.csv` date column → **0**; `stage=stage1` 72/72; empty cells 0.
* `_MANIFEST.md` supersession check: each of `2,698 / 7,468 / 1,335 / 3,021 / 2,234 / 17,575 / 22,468 / 5,242` present
  **exactly 1** time as a dated string → **0 erasures**; `22,962` present as the current sum.
* CSV integrity after writing: `sources.csv` **25 data rows × 18** and `data_gaps.csv` **23 × 8**, every row one width,
  both re-parsed with `csv.reader` ✓ (the two new cells are correctly quoted; a whole-file csv round-trip was tested
  first and **rejected** because it rewrites 56 / 18 bytes of unrelated quoting — so the edits are targeted raw
  substitutions, validated to match exactly once each before any file was written).
* `grep -i 'target' tools/web_domains.json` → **1 slug block, 2 domains**; JSON parses.

## 7. GATE (as prescribed by the brief)

```
python tools/gates.py --company-dir founders_playbook/01_companies/company_042_target --tier core \
  --out founders_playbook/03_quality_control/target_s1_gates_round4.md
```
**Findings: 2 | Passes: 18 | exit 0.** **`corrections 24 retraction ids; register layer reaches 24, volumes 24`** ✓ and
**`anchors parity 40 narrative anchors <-> 40 register anchors`**, 46 distinct ids resolving ✓ — **neither regressed**,
both identical to recert3's run. The 2 findings are the same two pre-existing ADVISORYs (1-of-1 attributed quote
unmatched = the §15.6 intake gap where `sources/**` is outside the quotes index; 42,833 words over the core *planning*
density target, RD-122: not a split mandate and not a defect). `coverage 9 registers, 1 stage volumes, 25 source
documents`; csv widths unchanged (25×18, 72×12, 24×11, 18×15, 23×8, 4×11, 1×11, 3×15, 3×11). I added no new ADVISORY
quote finding. **I did not trim evidence to move either number.**

## 8. Counts re-measured after my last corpus write

`stage_1.md` **42,833 / 292,456** (untouched) · `stage_1_index.md` **1,542 / 10,742** · `_MANIFEST.md` **2,750 /
17,608** (its own count is published nowhere in the corpus, so no cell went stale with it) · `CORRECTIONS.md`
**9,463 / 62,153** · registers **5,388/41,586 · 8,729/63,567 · 1,623/12,251 · 3,165/22,458 · 3,238/22,335 · 344/2,651 ·
232/1,858 · 72/649 · 171/1,400** = **173 rows**, **22,962 words / 168,755 bytes** · COR ids **24**, gate reach
**24/24/24** · anchors **40 ↔ 40**, 46 distinct · period-basis tags **69/72**, bare-year **40/40 tagged**, DERIVED
**7/7 with arithmetic** · `calendar year` in held corporate print **4 layers / 4 lines** · live `L3246-3250`
mis-pointers **0** (was 2) · live `six` date-cell count **0** (was 1) · live `0 times` census claim **0** (was 1) ·
`cdx_intake` mentions in the company dir **4** (was 0) · `web_domains.json` slugs **6** (was 5) · cdx sha shared by
**4** files across **2** companies · `sources/web_archive/` now holds **20** files, of which the run created **18**
(8 `.html` bodies + their 8 `.html.meta.json` sidecars + 1 `target.com_1996_2002.UNANSWERED.md` + `_RUN.json`) and **2**
pre-existed (`cdx_dhc.txt`, `cdx_targetcom.txt`) · requests spent by the run **12 of 20** · files written by this pass: the 5 corpus files +
`tools/web_domains.json` + the run's output + this log + the gate sheet.

## 9. Left as named residuals, with reason (nothing dropped silently)

* **R-1** `_INDEX.md:26-27` "certifier blocker B-4" — not my file set, not claimed; the one-word repair the certifier
  describes ("audit-2 hand-off / COR-20") still waits for the next legitimate open.
* **R-2** `stage_1.md:281` self-count **41,534** vs disk **42,833** — `stage_1.md` is outside my brief's owned list and
  I did not claim it; the authoritative figure lives in `_MANIFEST.md:9` and is correct. Still a named residual.
* **R-3** §U emission-slice 503/tier wording `stage_1.md:2364/2366/2367` — protected by the `SUPERSEDED — DO NOT
  RE-APPLY` banner; the repairer's refusal and recert3's ruling both stand. Not touched.
* **R-4** `_parts/s1_p1.md:159` stale quote, `_parts/s1_p2.md` "volume 1" ×2 — superseded merge audit trail, no agent
  writes it. Not touched.
* **R-5** 21 unsideared content docs: **partially discharged by this pass** — the 8 new `dhc.com_*.html` bodies all
  carry `.meta.json`; the 2 `cdx_*.txt` and the 19 route/index artifacts still have none, and the FETCH REQUEST
  stands (S4220's note says so explicitly).
* **R-6** period-basis census — **DISCHARGED** (re-derived 69/72, 40/40, 7/7; see §1).
* **R-7** `target_s1_repair_round3b.md` §0/§6.6 "nothing committed" is stale after RD-139 — QC history, not mine to
  rewrite; noted here so the next reader does not re-open it.
* **R-8** tools/orchestrator: `gates.py` exit-code-vs-ADVISORY contradiction still unfixed (and off this round again
  because the corpus passed); `research/` and the method file still outside the quotes index; `periodical_harvest`
  still has no `target` task set (the only route that can settle U.032); the `S42xx` cross-company mint scheme
  (task #31) now has a **fresh and sharper edge** — this pass generated 9 artifacts that cannot be registered until
  that map exists.
* **New, raised by this pass:** the `dhc.com` enumeration hit the tool's **500-capture limit**, so the capture count
  published in `_RUN.json` is a floor; a real census needs `--limit` raised, which is `cdx_intake.py` scope I do not
  hold. And `www.dhc.com` / `www.target.com` are registered as the **apex** domains `dhc.com` / `target.com`
  (matchType=domain returns the `www` URLs) — the microsoft precedent in the same file; a host-form leg is not
  registered because the 20-request budget is Target's, not the fleet's.

## 10. Certification request (§15.6)

I am the repairer; **I do not certify this repair.** N-1…N-5 are reported CLOSED with the figures above, and the gate
condition in my brief (`corrections 24/24/24`, anchors **40↔40**) is met with no regression. **The certifier ruled that
if these five close with its figures unchanged its next verdict is CERTIFIED-WITH-NAMED-RESIDUALS — that ruling is the
certifier's and I claim nothing of it.** Requesting a **different** agent to re-certify against this log,
`target_s1_gates_round4.md`, and the 6 files I wrote; the three items on which I would most want a ruling are (i) the
`data_gaps.csv` edit outside my brief's owned list (§0), (ii) whether the U.026 state move from TRIED–UNANSWERED to
TRIED–ANSWERED-WITHOUT-IN-WINDOW-TEXT is the honest one given the 8 bodies are all `(PB)`, and (iii) whether refusing
to mint `S4226`–`S4227` for 9 real new artifacts is the right call or a new propagation gap.

STATUS: WRITTEN 2026-10-06, agent `target-round4`. No git commit made (not in this brief).
