# Tesla Stage 1 — repair pass 1 (`tesla-repair-1`, 2026-09-30)

**STATUS: REPAIR COMPLETE — NOT A CERTIFICATION.** Work order: `03_quality_control/tesla_s1_audit1.md`
(PASS-WITH-FINDINGS, 5 blockers + 9 advisories). **Web calls: 0 made, 0 permitted**; no figure below is second-hand,
and every carrier named here was opened from `sources/sec/` on this disk. Paths claimed with
`python tools/scaffold.py claim --path <p> --agent tesla-repair-1` and released `--done`; **no `--force` was used
and no claim was refused** (14 paths: the 9 registers, `stage_1.md`, `stage_1_index.md`, `_MANIFEST.md`,
`CORRECTIONS.md`, this sheet). `_parts/` was never claimed and never written.

**Every fact in the audit sheet was re-measured before it was acted on, per §14 rule 8 — including the auditor's.**
Four of its headline facts confirmed exactly, two of its own numbers did not; both directions are recorded in
"Audit corrections" below, and one advisory (A4) is dispositioned differently than the auditor framed it.

## Gate, run after the last corpus write

`python tools/gates.py --company-dir founders_playbook/01_companies/company_043_tesla --tier auto --out
founders_playbook/03_quality_control/tesla_s1_gates_repair1.md` → **Findings: 2 | Passes: 18**, tier resolves
**T3** from `research/A_chronology_feasibility.md` ("a stated-verdict line"), **0 substantive**:
`advisory | stage_1.md | 54903 words over the T3 density target 8000 -- NOT a split mandate and NOT a defect`, and
`quotes | ADVISORY | 16 of 58 checked spans unmatched (28%)`. **The gate was re-run after the very last corpus write**
(the intermediate run before the final §B annotation printed 54,831 words; the report on disk carries 54,903, which
is also the number `stage_1_index.md` and `_MANIFEST.md` publish). 92% of the 60,000 hard cap, so no §9.3 split. and `quotes | ADVISORY | 16 of 58 checked spans unmatched (28%)` — **the same 16 spans and
the same 2 findings the auditor measured; my pass did not reduce the unmatched count, it labelled the 3 real
defects in place** (A5) and left the 10 entity/markup artifacts and 2 instrument artifacts alone.
`corrections | 7 retraction ids; register layer reaches 7, volumes 7` ✓ (COR-01…COR-07).
`keys | 3 retired keys inside collision/re-key text — protected history` — pre-existing, untouched.
**A tier overage is advisory, not a defect (RD-122, §15.4).**

## Blockers

| # | Disposition | Before → after (re-measured after the last write) |
|---|---|---|
| **1** The 2009-12-31 refundable-reservation false null | **CLOSED** | `U.23` "no printed cell on disk gives a 2009-12-31 reservation balance" + COR-01 "the 2009-12-31 value is **UNKNOWN**" + index `U.23` row + merge-notes §7 → **withdrawn in place**; the value is now a row: `quantitative.csv` `2009-12-31 \| refundable reservation liability \| 26.0 \| USD millions \| S4370 \| FACT \| High`, registers **208 → 210 rows**, anchors **23 ↔ 23 unchanged** (re-grade, not a new conflict). `decisions.csv` row 1 re-labelled **carried and now supported**; its causal reading stays unproven |
| **2** `validation.csv` Daimler row | **CLOSED** | `2009-05` → **`2009-11`**, signal re-worded "First powertrain shipments to Daimler (battery packs and chargers)", magnitude split from recognition ("revenue recognition began in the quarter ended 2009-12-31"), carrier sentences quoted in the note; the May-2009 formalisation recorded **inside the same row** so validation stays **9 rows**. Matches `timeline.csv` 2009-11 and claim record `P1-28` (the volume was already right) |
| **3** Per-share across the May-2010 split | **CLOSED** | Three rows re-pointed off `S4372`: 30 → `S4369` (its 2009-09-30 table is `S4369`'s, dated "at September 30, 2009"; `S4372`'s table is 2010-03-31), 31 → `S4369 (with S4370 / S4371)`, 32 → `S4369`. Measured: `0.493` **5× in `ds1.htm`, 5× in `-068933`, 5× in `-099603`, 0× in `-149105`**, which prints `valued at $0.49 per share` and `Series A $ 0.001 $ 0.49 7,213,000 7,213,000 $ 3,556 $ 3,549 *`. Residuals now stated per basis: **$8k on the $0.493 carrier / $16k on the $0.49 carrier** against the identical recorded **$3,936k**; 15,213,000 × $0.493 re-derived to **$7,500,009** (cell printed $7,499,999). Split basis named in every cell (8,000,000 → **2,666,666** common, 1-for-3 effected May 2010, `U.13`) |
| **4** `_MANIFEST.md` mis-sum + duplicate sections + glued row | **CLOSED** | Published **13,329 w / 111,343 B** → **210 rows / 16,837 w / 128,812 B**, footing printed: 4,261+2,567+2,004+3,402+1,829+951+541+814+468 = 16,837 and 33,577+20,945+16,101+24,056+13,063+7,089+4,223+5,990+3,768 = 128,812. The auditor's recomputation of the merge's cells (**14,323 / 111,943**) confirmed cell-for-cell against disk. Sections "Intermediates…" and "Open research debt…" printed **twice** (lines 48-69 and 71-92) → **each appears once** (verified by count); the prose-glued `| Gate finding | …` row removed → gate findings moved into their own named table (A9). Two rows this pass broke by wrapping inside a table cell were re-flowed; `grep` shows **0 table rows not ending in `|`** and balanced `**` |
| **5** `timeline.csv` central silence row | **CLOSED** | `2003-07-01 -> 2004-05 \| no dated corporate act of any kind` → **`2003-08-01 -> 2004-02-29`** + "inside THIS narrowed window", with the three refuting rows and the `S4369` carrier quoted (*"board of directors adopted, and our stockholders approved our 2003 Equity Incentive Plan, or the 2003 Plan, **in July 2003*"*) and the "not an inference of inactivity" caveat preserved. 46 rows unchanged. **Extension found on this pass:** Volume 1's own “Opening edge” prose (line 251, under ## Boundary, 227 lines into the volume) claims the same absolute over a window its own register refutes at 2004-03 and 2004-04; annotated in place (the line number is a locator only, §14 rule 12) |

## Sweep: commands and hit counts (post-repair; `… | grep -v audit1.md` to exclude the work order itself)

Pattern `grep -rn --include=*.csv --include=*.md -F "<s>" 01_companies/company_043_tesla 03_quality_control`:

| string | hits | where, and status |
|---|---|---|
| `no printed cell` | **2** | `conflicts.csv:24` and `quantitative.csv:44` — both **inside the withdrawal that names them** |
| `value is UNKNOWN` | **8** | conflicts 1 (bracket), CORRECTIONS 2 (the kept-original + the WITHDRAWN header), stage_1 3 (anchor's kept sentence + its bracket + COR-01 row), index 1 (marked withdrawn), `_parts/s1_p2.md` 1 (protected) — **0 live claims in the owned instruction layer** |
| `stays UNKNOWN at U.23` | **2** | both inside `WITHDRAWN` tags on the two 2010-03-31 rows |
| `not carried as a finding` | **7** | conflicts 1, CORRECTIONS 1, `decisions.csv` 1 (retraction bracket), stage_1 3, **merge notes §7 1** (residual, below) |
| `flat-liability reading is not carried` | **1** | stage_1, inside the bracket that withdraws it |
| `verbatim, nothing dropped` | **1** | CORRECTIONS COR-07 only; **0 in any register** (8 rows swept: `S4369`, `S4371`, `S4372`, `S4375`–`S4377`, `S4389`, `S4390`) |
| `13,329` / `111,343` | **3** / **3** | index 1 + manifest 2, every one inside "the merge published … which did not foot" |
| `no dated corporate act of any kind` | **8** | CORRECTIONS 1 (retraction), stage_1 3 (**line 251 prose, kept + annotated**; line 829 = Volume 1's **printed emission copy**, protected as emitted), timeline 1 (in the note quoting the withdrawn wording), `_parts` 1, COR-07 row 1 |
| `offset 9,746` / `102,736` | **1** / **2** | merge notes (not owned); `_MANIFEST.md` 1 = the retraction sentence explaining why offsets are no longer published |
| `2009-05,First powertrain` | **2** | `stage_1.md:2587` = **part 2's printed register emission copy inside Volume 2**, and `_parts/s1_p2.md` — both protected as-emitted history; the canonical `validation.csv` now reads 2009-11 |
| `53,553` | **2** | `stage_1_index.md` (the merge's number, in the row it re-publishes for the pre-repair state) and merge notes — see residual R3 |

## Register deltas

| register | rows before → after | words/bytes before → after | what moved |
|---|---|---|---|
| `sources.csv` | 24 → **24** | 3,732 / 29,716 → **4,261 / 33,577** | 8 rows' fold claim corrected (A4); `S4390` title re-made from measured directory contents (A8) |
| `quantitative.csv` | 61 → **62** | 1,756 / 15,749 → **2,567 / 20,945** | +1 reservation row 2009-12-31 (B1); 3 per-share rows re-pointed (B3); Toyota rounded-vs-exact (A2); EPA date/value (A1); 2 rows' stale UNKNOWN tags |
| `timeline.csv` | 46 → **46** | 1,862 / 15,189 → **2,004 / 16,101** | silence row narrowed (B5) |
| `conflicts.csv` | 23 → **23** | 3,152 / 22,274 → **3,402 / 24,056** | `U.23` re-graded in place, all 8 adjudication cells rewritten with the withdrawal visible |
| `data_gaps.csv` | 15 → **16** | 1,604 / 11,565 → **1,829 / 13,063** | +1 near-collapse gap (minted to make a false pointer true, A3) |
| `decisions.csv` | 9 → **9** | 841 / 6,329 → **951 / 7,089** | row 1 `actual_result`/`source_id`/`confidence` (B1d) |
| `validation.csv` | 9 → **9** | 372 / 3,121 → **541 / 4,223** | Daimler row (B2) |
| `failures.csv` | 11 → **11** | 536 / 4,232 → **814 / 5,990** | ten→thirteen months and 2008-02→2009-03; memory-layer row labelled an evidentiary null (A3) |
| `channels.csv` | 10 → **10** | 468 / 3,768 → **468 / 3,768** | **untouched** |
| **total** | **208 → 210** | **14,323 / 111,943 → 16,837 / 128,812** | **23 rows** carry a repair marker: sources 8, quantitative 8, failures 2, timeline 1, conflicts 1, data_gaps 1, decisions 1, validation 1 |

Volume/instruction layer: `stage_1.md` 53,553 → **54,903 words** (381,797 B, 92% of the 60,000 hard cap, one
volume, no §9.3 split); `stage_1_index.md` 1,564 → **2,005** (13,369 B) (13,347 B); `_MANIFEST.md` 1,652 → **1,941**;
`CORRECTIONS.md` 1,475 → **2,792**. **`_MANIFEST.md` and `stage_1_index.md` publish the same numbers, both
measured from the same disk state after the last register write.**

## Advisories: accepted, declined, or re-framed

- **A1 EPA — ACCEPTED.** Row re-dated `2009-12-21` → **`2010-01`** (the settlement month the carrier prints) with
  the certificate date preserved in the note; metric re-worded so the date and the value belong to each other.
- **A2 Toyota — ACCEPTED.** Value cell now `50000000 (rounded, as filed); 49999992 exact`; derived cell prints the
  true product and both carriers. **Noticed while verifying:** the exact-figure carrier
  (`sources/sec/0001193125-11-149963_ds1.htm`, "for aggregate proceeds of $49,999,992") is **held but unregistered** —
  0 hits for `149963` in `sources.csv`. That is intake debt, not a value debt; it does not get an `S####` row from a
  repair pass, so it is named in the repair sheet and in the row's note.
- **A3 memory-layer failures row — ACCEPTED as a label, and the auditor's premise is FALSIFIED.** It is now marked
  an evidentiary null, kept in place (RD-122). But A3 asserted "data_gaps.csv already carries it": measured, **0**
  of the 15 data_gaps rows did (no hits for "collapse", "anecdote", "days-to-bankruptcy"), and the failures row's
  own pointer "logged open in data_gaps" was therefore false too. Fixed in the direction of truth by minting the
  gap, not by deleting the row. (Also repaired: a U+FFFD artifact at the head of that cell.)
- **A4 fold preservation — ACCEPTED, then WIDENED.** The auditor tested `S4369`. Measured, the identical false
  boilerplate sat on **eight** `sources.csv` rows; all eight corrected. Hit counts for the five lost probe strings
  across the nine registers: **0, 0, 1 (my own new text), 0, 0** — and, unreported by the auditor, **0 in `_parts/`
  and 0 in `stage_1.md` as well**: the lost `source_title`/`independence_note` values survive **only** in
  `research/sources.csv`, the emission `merge_census.py` cannot see. So the loss is a **third-emission fold loss**,
  not a merge-only one, and restoring the columns "inside the MERGE[…] tag" as A4 suggested could not have been
  done from the registers — it needs the research file, which is why I corrected the claim instead.
- **A5 three quotations — ACCEPTED all three, after reading each span** (I honoured the auditor's 40% pre-unfolding
  false-positive warning and did not accept any of them from the gate list). (i) *"We cannot, **however**, access
  all of these funds at once…"* — elision marked inline; (ii) the 2010-06-08 Conclusion reads *"The Company believes
  the errors are not material to any periods previously presented and will correct the error in the three months
  ending June 30, 2010"* — the spliced first-person subject marked inline; (iii) the §H "luxury/performance … in our
  target market" span is **not a quotation at all**: every held printing reads *"we will face competition from
  existing and future automobile manufacturers in the extremely competitive luxury sedan market, including Audi,
  BMW, Lexus and Mercedes"*. Annotated as **NOT A VERBATIM QUOTATION** with the filed sentence printed beside it.
  No original words were removed.
- **A6 gate pass counts — ACCEPTED.** `_MANIFEST.md` now carries a named table: merge run `--tier T3` 2 findings /
  **20 passes**; audit 1 `--tier auto` 2 / **18**; this pass 2 / **18**, tier **T3**, `tools/gates.py` dated
  **2026-10-06 17:39** on this disk and edited three times on 2026-09-30 — which is why the pass count is published
  with its tool date and never bare.
- **A7 slice offsets — ACCEPTED as a class, DECLINED as a renumber.** I re-located the bodies **on the bytes as of the last write to `stage_1.md`**, i.e. after every annotation this pass
  made: Volume 1's first body line at byte 11,821 / char 11,706, Volume 2's at byte 106,424 / char 105,187, and the
  `## Volume 1` / `## Volume 2` headings at bytes 11,662 / 106,248. (Volume 1's number is the one script measured
  mid-pass and it held; Volume 2's moved +474 bytes under the Boundary annotation alone, which is the argument for §14 rule 12). `_MANIFEST.md` and the index now address each
  slice by its heading `## Volume N` and its first body line, and state why 9,746 vs 9,859 disagreed. Publishing a
  fresh number that my own next edit invalidates would have re-created the defect.
- **A8 zero-byte CDX file — ACCEPTED with a correction to the auditor.** The row title is rebuilt from the measured
  directory: 8 entries — `cdx_tesla_com_2003_2005.json` 153 B (504 HTML), `cdx_tesla_com_root_exacts.json` 153 B
  (504 HTML), `cdx_www_tesla_com_root_exacts.json` **11,832 B (IA "Temporarily Offline" HTML, named .json)**,
  `cdx_tesla_com_2008_2011_founderish.json` **0 B**, the README transcript, 3 sidecars. The auditor wrote "0 bytes
  **with no sidecar**" — the sidecar **exists** (473 B); what it lacks is `http_status`. My first version of the new
  title repeated that error; it is corrected in the cell, and the correction is printed there so the pass that
  re-certifies can see I caught it.
- **A9 malformed glued table row — ACCEPTED** (folded into BLOCKER-4).

## Audit corrections (a correction is itself a claim)

1. **"in our target market" occurs 0× across held bodies** — false: **56×** across the 80 held `.htm`/`.txt`
   bodies (4× per prospectus printing, 2× per 2011 printing), always about **brand recognition**, never competition.
   A5(iii) still stands, on a better basis: the phrase is *real but from a different sentence*, which makes the
   volume's span a splice rather than an invention.
2. **"printed by eight held documents"** — 8 is the **accession** count; the measured figure is **11 bodies across 8
   accessions** (and the 4 bindings inside `S4370` are 4 distinct sentences, including the contractual-obligations
   table and the Roadster+Model S aggregate line, not 4 repeats).
3. **A3's "data_gaps.csv already carries it"** — false, see above.
4. **A8's "no sidecar"** — false, see above.
5. Confirmed exactly as written and acted on: the `S4370`/424B4 carrier sentences, `0.493` counts
   (5/5/5/**0**), the 8,000,000 vs 2,666,666 basis, the Daimler May/November pair, the three contradicting timeline
   rows, the `_MANIFEST` mis-sum, and the 40%-then-20-character matcher caveat.

## Residuals (not this pass's paths; carried to the certifier)

- **R1 — `03_quality_control/tesla_s1_merge_notes.md` §7, line 161-162** still prints "**$2009-12-31 is
  UNKNOWN**" and "the 'liability held flat across the deposit-policy inversion' reading **is not carried as a
  finding**". It is the merge agent's own report; §14 rule 7 gives one path one owner, so I did **not** edit it, and
  the retraction is instead propagated to `_MANIFEST.md` ("Repair pass 1 — what this file does NOT claim"),
  `CORRECTIONS.md` COR-01, `stage_1_index.md` and `stage_1.md`. **A re-certifier should treat R1 as an open
  instruction-layer hit against `U.23`.**
- **R2 — protected history left standing by design:** `stage_1.md:829` (Volume 1's printed `timeline.csv` emission,
  still the pre-repair range), `stage_1.md:2587` (Volume 2's printed `validation.csv` emission, still `2009-05`),
  `_parts/s1_p1.md:703`, `_parts/s1_p2.md:1166/1708/1738/1904`. The canonical registers are corrected; the volume
  says so at its foot.
- **R3 — `stage_1_index.md` and `stage_1.md` keep the merge's 53,553-word figure** where they describe the
  *pre-repair* state (the index's volume row now reads 54,831 at first repair and 54,903 after the §B annotation —
  `_MANIFEST.md` is the live publisher, and it is the only file whose numbers were re-measured twice this pass).
- **FETCH REQUESTs unchanged and still unexecuted (0 web calls):** FRA-1 CDX re-query + a body/sidecar with
  `http_status` for the 0-byte founder-is-CEO file (settles `U.4`'s LEAD status); FRA-2 exhibit folders of
  `-017054` / `-149105` — now needed for the **flow** data and the charter, **not** for the reservation balance;
  FRA-3 binary re-fetch of the 3 staff UPLOAD PDFs. **New:** register the held-but-unregistered
  `0001193125-11-149963` S-1 (carrier of the exact $49,999,992) and of the 12 SEC-generated REGDEX rows COR-03
  already names. No claim above was moved to a second-hand figure for want of a fetch.

## Re-certification

**§15.6 and AUDIT-rule 1: certifier ≠ repairer. I do not sign this repair.** A **different** agent must
re-certify Stage 1 against `03_quality_control/tesla_s1_gates_repair1.md`, this sheet, and the re-graded `U.23` /
`COR-01` / `COR-07` text; Tesla's Stage-1 verdict stays **PASS-WITH-FINDINGS pending re-certification**, and the
tier stays **T3** (unchanged by this pass: no family was added, so §15.2 gives the same answer, and §15.4 makes the
word overage a legitimate state rather than a defect).
