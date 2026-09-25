# AUDIT 7 REPAIRS — Amazon Stage 1 (`company_001_amazon`)

**Agent.** Repair pass responding to `03_quality_control/audit7_stage1_recertification.md` (verdict: **REOPEN**,
two blockers + named small items). Scope is **exactly** AUDIT 7's B-1, B-2 and its named small items.

**Discipline declared before the first edit.**
- Read-only on everything outside the allow-list; no Stage-2 file, no `MASTER_RESEARCH_LOG.md`, no
  `RESUME_HANDOFF.md`, no `00_METHOD_AND_STYLE.md` touched.
- **Retract, never substitute.** Where a value has no filed support the answer is UNKNOWN plus the reason.
- Corrections cite document and line; prior corrections are superseded **visibly**, not erased.
- Invariants preserved and recomputed at the end (§Invariants below), not inherited from AUDIT 7.
- **Zero web requests** in this session (no WebSearch, no WebFetch).

---

## Work order — planned repairs

### B-1 — the retracted share-count leg still runs live (AUDIT 7 item 6)

| Row | File | Site | Before → After | Why | Sweep command |
|---|---|---|---|---|---|
| R1 | `_parts/s1_p1.md` | :142 | footer asserting "composition foots to **$976,408** … one-third leg **is $871,000** (`2,613,000 ÷ 3`, orig. l.4301–4302)" → appended AUDIT-7 addendum withdrawing limbs (a) the composition total and (b) the one-third leg, pointing at `stage_1.md` §P.2 d8a and §U.8; original text left standing | AUDIT 7 B-1: the retracted figure is printed in the voice of a *correction* in a file a downstream reader trusts | `grep -rn -E "871,000\|871,024\|976,408\|2,613,000\|2613000" <company folder>` |
| R2 | `_parts/s1_p3.md` | :180 | same defect, verbatim twin → same addendum | same | same |
| R3 | `research/E_supply_ops_finance.md` | :562 | same defect inside a dossier Stage 2 mines → same addendum | same | same |
| R4 | `_parts/NUMBER_DEFECTS.md` | :68–74 | "$871,000 … **the canonical figure**", "composition foots to $976,408", "the $24 difference is **accounted for**" → addendum retracting all three limbs (the $24 account is withdrawn by IR-04 / `stage_1.md:1530, 1573`) | strongest instance: calls a retracted figure canonical and revives a withdrawn account | same |
| R5 | **class sweep, folder-wide** | all Stage-1 files | every live instance of the leg found, not only the four named sites | AUDIT 7's core charge: "worked a named site list and did not sweep siblings — twice". Fix the class | see §Sweep log (three commands: the leg, unfiled-denominator claims, the l.4301–4302 citation) |
| R6 | **citation sweep** | folder-wide | every citation to "orig. l.4301–4302" checked against what the line contains; non-supporting ones retracted | AUDIT 7: "the citation itself is wrong, not just the value" — the line holds `3,021,000 / 23 investors / $.3333 / $1,007,000` | `grep -rn -E "l\.430[0-9]\|l\.431[0-9]\|4301" <company folder>` + read `sources/S-1_original*.txt:4296–4306` |

### B-2 — a withdrawn instruction still printed as governing (AUDIT 7 item 8)

| Row | File | Site | Before → After | Why | Sweep command |
|---|---|---|---|---|---|
| R7 | `_parts/U_CONCORDANCE.md` | :48 | U.17 row printing "COR-03 / COR-11.2 govern … §P and §R print `11 (per the filing: at 1996-01-01)`" as the operative action → supersession addendum: COR-03 is SUPERSEDED BY COR-12, that instruction is WITHDRAWN, aligned to `conflicts.csv` U.17 | the concordance is the designated authority for `Conflicts: U.n` references and contradicts a cell edited in the same wave | `grep -rn "COR-03" <company folder>` |
| R8 | `adversarial_review.md` | :34 | "(COR-03, U.21)" cited as live authority, unmarked → marked `(COR-03 [SUPERSEDED BY COR-12 — the date reading was withdrawn; COR-12 governs])` | deliverable, batch 1, still routes a reader to a retired correction | same |
| R9 | **COR-03 reference sweep** | folder-wide | every other `COR-03` occurrence classified governing vs routed/marked | AUDIT 7: "grep for every other reference to COR-03 to make sure none of them still treats it as governing" | `grep -rn "COR-03" <company folder>` |

### Named small items

| Row | File | Site | Before → After | Why | Sweep command |
|---|---|---|---|---|---|
| R10 | `_MANIFEST.md` | :39 | "the **three** sites … were reached", listing four, and "gap row 12" labelled **§G** → count corrected to four with the retraction visible, section label corrected to **§J** | AUDIT 7 item 13: false closure sentence; the gap row lives in `## J. Data gaps and contested figures` (`context_appendices.md:623/:628/:641`), not §G | `grep -n "^## [A-Z]\." context_appendices.md` |
| R11 | `CORRECTIONS.md` | :295–299 | "…plus **four** found by re-running its own phrase sweep", then names five → count corrected to five, list preserved | same class | read the sentence + count its own list |
| R12 | `stage_1_claim_records.md` | :592 | census sentence "**52** populated `Corroboration:` fields, 5 at ≥3" → re-derived: **49 record-level fields / 54 raw occurrences**, operative "5 at ≥3" confirmed unchanged | AUDIT 7 measured 49/54 and could not reproduce 52 under either convention | python census over `^Corroboration:` fields and records |
| R13 | `03_quality_control/amazon_s1_audit4_audit5_final.md` | :409, :431 | **addendum only**, appended under the auditor's original "Lands? YES" verdict text, recording A-B1 closed on evidence and where the proof lives | AUDIT 7 item 12 / residual 2 — attack register is not retro-edited, so closure is added as an addendum. **Scope note:** this file is outside my allow-list; the delegation names it explicitly, so it is edited additively and nothing else. | `grep -n "Lands?" amazon_s1_audit4_audit5_final.md` |
| R14 | folder-wide | "on its own face" | wherever the umbrella clause claims the file number is on each member's own face → corrected: true for the four S-1-family documents, **false for the FY1997 10-K405**, whose face number is `000-22513` (`sources/10-K_FY1997*.txt:50`); 333-23795 appears there only at l.2913 and l.3105 | AUDIT 7 item 9 residual + named small item "correct … wherever that phrase was used" | `grep -rn "own face\|on its own face" <company folder>` |

---

## Sweep log
(run, then recorded here with counts so any verifier can re-run)

All three sweeps run from `founders_playbook/01_companies/company_001_amazon/`. Stage-2 artifacts
(`stage_2_*`, `_parts/s2_*`, `research/ST2_*`, `research/_EVIDENCE_CACHE.md`) are **excluded from the edit set but
included in the read**, and their hits are reported at §Routed-to-other-owners below.

**S1 — the retracted leg (B-1 class sweep).** Re-runnable shell form:

```
grep -rn -E "871,000|871,024|976,408|2,613,000|2613000|976408" \
  --include=*.md --include=*.csv company_001_amazon | grep -v -E "stage_2|s2_|ST2_|_EVIDENCE_CACHE"
```

Because a line-level grep cannot classify a wrapped footer, the operative version is a **negation-window
classifier** (same family as AUDIT 7's `bridge.py`): for every occurrence it reads ±320 chars and asks whether any
retraction/demotion marker (`retract`, `withdraw`, `supersed`, `not be followed`, `0 times`, `no composition`,
`unfiled`, `not adopted`, `audit-6`/`audit-7` marker, `do not import`, …) sits in that window; every hit without one
is printed for a human to read.

* Before this pass: **170 occurrences / 4 unclassified live sites** — AUDIT 7's four, reproduced exactly.
* After: **174 occurrences / 0 unclassified.** The 4 added occurrences are the new retraction sentences themselves.
* The two hits the classifier still raised after the four footers were closed were `_parts/NUMBER_DEFECTS.md`
  **l.27–28** (register `should_be` cells, ~85 lines above the audit-trail declaration and outside any ±320-char
  window from the foot addendum). Those are now marked **in-cell**, so the class is closed at the row level too,
  not merely at the footer level.

**S2 — claims resting on an unfiled denominator, and the l.4301–4302 citation.**

```
grep -rn -E "l\.430[01][–-]430[12]|ll\.4300[–-]4302" --include=*.md --include=*.csv company_001_amazon
python - <<'PY'   # co-occurrence test: is 2,613,000 ever within 220 chars of a 4300-4302 citation?
...
PY
```
Ground truth read from the filing: `sources/S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` **ll.
4300–4302** = "*Between December 6, 1995 and May 16, 1996, the registrant issued an aggregate of **3,021,000**
shares of Common Stock to **23 investors** for a consideration of approximately **$.3333** per share, or an
aggregate of **$1,007,000.***" `2,613,000` → **0** occurrences in all five cached documents, both with and without
the separator; positive control `3,021,000` present in the original and both amendments.
Result: **37** citation occurrences; the **10** the classifier raised were each read and every one is a **correct**
use — it cites the line for `3,021,000` / `23` / `$.3333` / `$1,007,000` or for the filed window, which is what the
line contains. **25** co-occurrences of `2,613,000` with that citation exist and all **25 sit inside a retraction**.
Zero live claims now rest on the unfiled denominator.

**S3 — COR-03 as governing (B-2 class sweep).**

```
grep -rn "COR-03" --include=*.md --include=*.csv company_001_amazon
```
**39** occurrences after the repair. **36** are routed or are the superseding text itself. The classifier raised 3,
read individually: `CORRECTIONS.md:253` ("**COR-03's error:** …", inside COR-12 — the correction describing the
retired one), `_parts/s1_p3b_H_addendum.md:141` (a pointer to "COR-03 banner, COR-12"), and
`_parts/U_CONCORDANCE.md:59` — the **original clause retained on purpose** (`**COR-03 / COR-11.2 govern.**`) with
its withdrawal appended in the same cell and warned **before** the table by the new SUPERSESSION NOTICE, which is
the shape `CORRECTIONS.md:62–85` already uses. **No unrouted governing reference remains in Stage 1.**

## Outcome log

| Row | Result | What was done, and the re-read that confirms it |
|---|---|---|
| R1 | **CLOSED** | `_parts/s1_p1.md` — 20-line AUDIT-7 addendum appended below the standing footer; limbs quoted verbatim, then withdrawn; 43%/41% limb declared unaffected. No substitution: fourth leg left UNKNOWN. |
| R2 | **CLOSED** | `_parts/s1_p3.md` ll. 182–199 — same shape; footer at l. 180 left standing. |
| R3 | **CLOSED** | `research/E_supply_ops_finance.md` ll. 564–582 — same shape, plus an explicit "this dossier is mined by Stage 2; do not import the pair" warning; limbs (1) and (3) declared standing. |
| R4 | **CLOSED** | `_parts/NUMBER_DEFECTS.md` — in-cell AUDIT-7 marker appended to the ROUND-1 bullet (l. 74–78) **and** a 43-line addendum at the foot (ll. 112–154) withdrawing three statements, retracting the citation, and stating what the rows still instruct correctly. Rows 27–28 themselves now carry in-cell markers (S1 residual). |
| R4b | **CLOSED — sibling found by sweeping, not by the list** | `_parts/NUMBER_DEFECTS.md` l. 86–90 (ROUND-2 bullet) asserted that `stage_1.md` §K **prints** the composition at $976,408 and that P09 "carr[ies] … the $976,408 composition". Both false: §K (l. 610) says no $976,408 total survives; P09 (l. 466) carries the **withdrawal**. Not named by AUDIT 7. Marked in place. |
| R5 | **CLOSED** | S1: 170/4 live → 174/**0** live. |
| R6 | **CLOSED** | S2: 37 citation uses checked against the filing; 25/25 co-occurrences of the unfiled denominator are inside retractions. |
| R7 | **CLOSED** | `_parts/U_CONCORDANCE.md` — U.17 cell (now l. 59) gets a 1,900-char in-cell correction; a **SUPERSESSION NOTICE** heads the file so a top-down reader is warned before meeting "COR-03 governs"; `conflicts.csv` U.17 named as the authority. Row arity restored to 7 pipes after the first attempt dropped one. |
| R8 | **CLOSED** | `adversarial_review.md` l. 34 — COR-03 marked retired in-cell, COR-12 stated as governing, the true half of the sentence preserved, table arity 8/8 verified. Also records that this cell's `U.21` is the `s1_claims_AJ.md` local key for canonical **U.17**. |
| R9 | **CLOSED** | S3 — see sweep log. |
| R10 | **CLOSED** | `_MANIFEST.md` l. 39 — "three sites" → **four**, miscount retracted visibly in-cell; "§G gap row 12" → **§J**, with the three coordinates that prove it (`context_appendices.md` l. 623 heading, l. 628 header, l. 641 row = the `#`-12 row) and what §G actually is (l. 467). Also extended l. 67/68 to disclose the concordance and register changes. |
| R11 | **CLOSED** | `CORRECTIONS.md` — "plus four found" → **five**, with the five-item list untouched and the correction attributed in-cell. |
| R12 | **CLOSED** | `stage_1_claim_records.md` l. 592 — "52" → **49**, and a 12-line census-convention note appended at ll. 608–619. My independent re-derivation reproduces AUDIT 7 exactly: **49 live record-level fields; 40 at 1, 4 at 0, 3 at 2, 2 at 3, none at 4**; pre-repair under the same convention 38/4/2/4/1, so the operative "**5 at ≥3**" was right and stands. 52 matches nothing: 55 field-shaped occurrences sit in record lines, 63 corpus-wide. |
| R13 | **CLOSED** | `03_quality_control/amazon_s1_audit4_audit5_final.md` — `**YES**` at l. 409 and the l. 431 row **not touched**; two dated in-cell pointers added, plus a **51-line "A-B1 CLOSURE ADDENDUM"** (ll. 480–530) carrying the proof block, the eleven verified citations, the executed consequences, and the 22-vs-24 reconciliation. **Scope note below.** |
| R14 | **CLOSED** | "on its own face" — one live occurrence corpus-wide (`stage_1.md` l. 63). Narrowed to: own face for the four S-1-family documents, incorporation by reference for the 10-K405, whose face number is `000-22513` (its l. 50, repeated l. 90) and which carries 333-23795 exactly **twice** (l. 2913, l. 3105). Original wording quoted inside the marker. The sibling looseness at `sources.csv` S0801 ("carried on all five accessions") corrected in the same terms. `_parts/s1_p4.md` l. 287's "appears on all five" **left alone** — true as worded, as AUDIT 7 found. |

**Side effect self-caught and reversed (recorded because it moved a measured invariant).** My R12 census note
originally contained the literal string `` `^<ID> Claim:` `` as an illustration of the record-header pattern. That
made the note itself a line matching `grep -c "Claim:"` on `stage_1_claim_records.md`, moving the count **431 → 432**
— i.e. this repair pass was about to bump the very record-count invariant AUDIT 7 measures, and worse, to make the
wrong "432" in `_MANIFEST.md` l. 38 and `stage_1.md` l. 2358 look *right* by accident. Re-worded to describe the
pattern without the token; re-verified: **431 lines contain "Claim:", and all 431 match a record-header form**
(418 letter-ID records B–U + 13 `U.n` records at ll. 559–571). Re-check with:
`grep -c "Claim:" stage_1_claim_records.md` → 431.


**Edit made outside the allow-list, on the delegation's own instruction (flagged, not hidden):** row R13 required an
addendum to `03_quality_control/amazon_s1_audit4_audit5_final.md`, which is not in the "may edit only" list. The
delegation names that file and that action explicitly, so I executed it **additively only** — the auditor's verdict
text is byte-preserved, and the diff is 2 in-cell pointers + 1 appended section. Had the instruction not named it,
I would have declined and routed it to the sheet owner.

## Invariants — recomputed after every edit, not inherited

| Invariant | AUDIT 7 | **Recomputed now** | Holds |
|---|---|---|---|
| Stage-1 U-blocks ↔ `conflicts.csv` | 43 ↔ 43 | **43 ↔ 43**; `stage_1.md` blocks U.1–U.43 contiguous, no dups; set parity both ways; all 43 rows `stage=1` | **YES** |
| Stage 2 ids must not shift | U.44–U.111, 68 rows | Stage-1 subset untouched by me; `conflicts.csv` now carries **70** Stage-2 rows (U.44–U.113) — a **concurrent Stage-2 agent's append**, not this pass. `git status` shows `conflicts.csv` and `timeline.csv` modified by other agents; my diff touches neither | **YES for Stage 1; the growth is another owner's** |
| Nine registers parse at uniform field count | 711 rows, 0 ragged | **0 ragged**, every file a single field-count key: sources 113×18 · quantitative 193×12 · timeline 116×11 · decisions 25×15 · validation 40×11 · failures 46×11 · channels 23×11 · conflicts 113×15 · data_gaps 45×8. **714 rows** — +1 timeline and +2 conflicts, all Stage-2-tagged, from the concurrent agents | **YES** (arity uniform; +3 rows not mine) |
| Stage-1 subset of each register | 102/94/49/15/26/33/12/43/23 | **102/94/49/15/26/33/12/43/23 — identical, nine for nine** | **YES** |
| `derived_arithmetic` on every DERIVED row | 26/26 stage-1; 0 empty file-wide | **26/26**; **0** non-DERIVED Stage-1 rows carrying arithmetic; file-wide **50 DERIVED / 50 populated** | **YES** |
| §P.2 recomputations | 32/32 | §P.2 is **provably untouched**: `git diff` on `stage_1.md` is a **single hunk at ll. 63–73** (11 lines in, 11 out), so ll. 928–1100 are byte-identical. d-entry census re-run: **32** (d1–d30 + d8a + d15a), no d31+. 12 of the printed terms independently re-derived and all foot: `94.118` / `94.137`, `100,020.0576` + `145,552.8372` + `49,995 = 295,567.8948`, `1,272,000 − 295,568 = 976,432`, `5,408 + 150,000 − 50,000 = 105,408`, `3,021,000 ÷ 3 = 1,007,000`, `2,811,000 ÷ 3 = 937,000`, `52 + 944 = 996`, `−232 − 52 + 1,228 = 944`, false LHS `= 996` | **YES — 32 entries, 12/12 spot-recomputes, remainder unchanged by construction** |
| §R's d-refs and U-refs | 6 and 17, none missing | §R still ll. **1160–1192**; d-refs `{8a, 15a, 24, 25, 26, 30}` = **6**; U-refs `{1,7,8,9,10,11,17,20,22,23,25,26,27,28,39,40,43}` = **17**; all 17 resolve against the 43 blocks | **YES** |
| Retraction-only sweeps | bridge 0 live; leg 4 live | **both re-run here, not inherited.** Newline-normalised false-bridge sweep over every `.md`/`.csv` in the folder **including** the Stage-2 volumes (`52 [-−] 232 [-−] 52 [+] 1,?228 = 944`): **4 occurrences, 0 live** — all four sit inside retraction sentences. `21,382.98`: **3 lines** (`quantitative.csv` l. 112, `stage_1.md` ll. 1087, 1088), all inside the correction naming it a truncation. Retracted equity leg: **0 live** (S1) | **YES** |
| Value / confidence / class invariance | 0 changes | **0**. This pass changed **no** `value`, `unit`, `date`, `evidence_class` or `confidence` field anywhere; `sources.csv` edit is inside the `notes` field of S0801 only, and re-parses at 114 rows × 18 fields | **YES** |
| Nothing deleted | — | Every withdrawal **quotes** the text it retires; no original sentence, verdict or banner was erased in any file edited | **YES** |

## Declined / not done, with reasons

1. **`_MANIFEST.md` l. 38 "432 claim records" and l. 42 "exactly the 30 DERIVED… rows" / "111 data rows";
   `stage_1.md` l. 2358 "432 records"** (AUDIT 7 residuals 4, and item 13's carried `_MANIFEST.md:42` row). Same
   defect family as my three named miscounts, and my census independently confirms **431** `Claim:` records and
   **29** arithmetic-bearing rows in the 111-row block — but AUDIT 7 lists these as **non-blocking residuals**, not
   as my named small items, and `stage_1.md` l. 2358 sits below my single permitted hunk. **Reported, not edited.**
2. **`_parts/U_CONCORDANCE.md` l. 13 "Final count: 42 canonical conflicts (U.1–U.42)"** and the missing U.43 row —
   AUDIT 7 residual 6, already disclosed at `_MANIFEST.md:67`. Out of named scope; I left the count and added only
   the COR-03 notice to that file.
3. **`03_quality_control/amazon_s1_numeric_closure_final.md` ll. 17, 29, 42 and
   `amazon_s1_causal_lineage_closure.md` ll. 37, 86** — AUDIT 7's three uncorrected false sweep certificates and its
   marker-census-reported-as-site-audit. These are the *other* repair-introduced closures AUDIT 7 graded "NOT
   CLOSED", but they are outside my allow-list and outside my named items, and AUDIT 7 itself assigns them to "the
   sheet owners" as correct-by-addition. **Declined: no authority granted.** Recorded here so the next work order
   inherits them.
4. **Stage-2 artifacts that carry the retracted pair or the loose lineage wording**: `_parts/s2_p1.md` l. 6 and
   `stage_2_part_1.md` l. 20 still say `context_appendices.md` is "**still printing** the retracted
   `2,613,000 / $871,000`" — false of Stage 1 today (appendices ll. 598/641 are labelled retractions, as Stage 2's
   own U.107 `best_supported_interpretation` concedes); `_parts/s2_p4.md` l. 1298 / `stage_2_part_3.md` l. 908 cite
   "as COR-03 already said" without the supersession marker. **Routed to the Stage-2 owner, not edited** — other
   agents are live in those files this minute and the duplicate-ID damage is already on the record.
5. **`adversarial_review.md`'s U-refs are not all canonical** — the file uses ids up to `U.50`, which exceed the
   43-row spine, i.e. it keys partly to the `s1_claims_AJ.md` local register. I resolved the one I had to touch
   (`U.21` → canonical U.17) and left the rest; a full re-key of that deliverable is its own work order.

## Attestation

Files edited by this pass, all inside `company_001_amazon/` unless flagged: `_parts/s1_p1.md`, `_parts/s1_p3.md`,
`_parts/NUMBER_DEFECTS.md`, `_parts/U_CONCORDANCE.md`, `research/E_supply_ops_finance.md`, `stage_1.md`
(one hunk, ll. 63–73), `stage_1_claim_records.md`, `CORRECTIONS.md`, `_MANIFEST.md`, `adversarial_review.md`,
`sources.csv` (S0801 `notes` field), plus this sheet and the additive A-B1 addendum in
`03_quality_control/amazon_s1_audit4_audit5_final.md`. **Not touched:** `MASTER_RESEARCH_LOG.md`,
`RESUME_HANDOFF.md`, `00_METHOD_AND_STYLE.md`, every `stage_2_*` and `_parts/s2_*` file, every other company
folder, and the eight registers other than `sources.csv`. **Web requests: 0** — no WebSearch or WebFetch call was
made; every figure above is local. Git used read-only (`status`, `diff`).

**Deletion audit, from `git diff --numstat` on the twelve files above** (added/deleted): `_parts/s1_p1.md` 21/0 ·
`_parts/s1_p3.md` 18/0 · `research/E_supply_ops_finance.md` 19/0 — these three are **pure appends**, no line of the
standing footer removed. `stage_1.md` **11/11** — one hunk, same line count, file still 2,372 lines.
`CORRECTIONS.md` 4/1 · `_MANIFEST.md` 3/3 · `adversarial_review.md` 1/1 · `sources.csv` 1/1 ·
`_parts/U_CONCORDANCE.md` 13/1 · `_parts/NUMBER_DEFECTS.md` 58/4 · `stage_1_claim_records.md` 16/1 ·
`amazon_s1_audit4_audit5_final.md` 56/2 — every "deleted" line in these is a line **rewritten in place with its
retired text quoted inside the replacement**, verified line by line; no claim, verdict, banner or figure was
removed from the corpus by this pass.


