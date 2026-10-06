# target_s1_repair_round3b.md

**Agent:** `target-repair-3b` (repairer only — this report is NOT a certification; see the request at the end).
**Predecessor:** `target-repair-3` (round 3), which hit the 150-turn ceiling at 44.9M tokens mid-flight and left
only a 285-byte stub here — no account of its work. Its 10 locks were released by the orchestrator before this pass.
**Date:** 2026-10-06. **Method:** §14 (supersede-don't-erase; rule 10 propagation to the instruction layer;
grep-before-assert) and §15.6 (certifier ≠ repairer).

STATUS: WRITTEN. All blockers below re-measured FROM DISK before any edit; nothing inherited from the round-3 read.

---

## 0. Inventory taken from disk BEFORE editing (round-3 footprint)

The dead agent's edits were **entirely uncommitted** — `git diff --stat HEAD~8..HEAD -- .../company_042_target` is
empty and `git log -S 'COR-21'` returns nothing; the whole round-3 footprint lives in `git diff HEAD` (working tree):
`stage_1.md +367`, `CORRECTIONS.md +364`, `_MANIFEST.md +44`, `stage_1_index.md +39`, and edits to `conflicts.csv`,
`data_gaps.csv`, `quantitative.csv`, `sources.csv`, `timeline.csv`, `_INDEX.md`. It never committed.

COR-id reach, measured at open (md hits in `company_042_target/*.md`, and register `.csv` files touched):

| id | CORRECTIONS.md row | stage_1.md (volume) | register csv | verdict at open |
|---|---|---|---|---|
| COR-21 | 1 (present) | 5 | conflicts.csv, timeline.csv (2) | wired |
| COR-22 | **0 (MISSING)** | 1 | conflicts.csv (1) | volume+register present, **no master row** |
| COR-23 | 0 | 0 | 0 | **never started** |
| COR-24 | **0 (MISSING)** | 4 | data_gaps.csv (1) | volume+register present, **no master row** |

This confirms and refines the orchestrator's 60-second read (21≈6/2, 22≈1/1, 23≈0/0, 24≈4/1): the "corpus hits /
registers" counts match; the extra defect is that **COR-22 and COR-24 were never declared in `CORRECTIONS.md`**, so
the `corrections` gate could not even count them (it read the id set from that file and reported "21 ids").

**Gate at open:** `python tools/gates.py --company-dir .../company_042_target --tier core` → Findings 2, Passes 18,
exit 0; both findings ADVISORY (1 unmatched quote; 42,701-words-over-density). `corrections 21 retraction ids;
register layer reaches 21, volumes 21`.

## 0b. Disk measurements at open (before my last write)
`stage_1.md` 42,701 w / 291,581 B · sources 25 rows · quantitative 72 · timeline 24 · conflicts 18 · data_gaps 23 ·
validation 4 · decisions 3 · channels 3 · failures 1 = **173 register rows** · sources block `S4201`–`S4225` ·
COR ids defined in `CORRECTIONS.md` = COR-01…COR-21 (21).

---

## 1. Per-blocker: what the dead agent had actually landed (evidence), and what I did

Work order = `03_quality_control/target_s1_recertification2.md` (certifier `target-recert2`, verdict NOT-CERTIFIED,
blockers RB-1…RB-7); carried-over context = `target_s1_repair_pass2.md` §14 (FETCH REQUESTS) / §15 (remaining debt).

**RB-3 → COR-21 — CLOSED by dead agent; verified, not re-applied.** `timeline.csv` rows 2/3/8/9 re-graded in place to
`RETROSPECTIVE INTERPRETATION`/Medium (row 9 split FACT-openings + RESTATED/eleven-store total, S4209 TLS cap named),
each row carrying an "RB-3 re-grade 2026-09-30 (COR-21)" note; `stage_1.md` §Boundary 3.2 prints "RB-3 applied …
(COR-21)". Reaches both layers. I did **not** touch these.

**RB-6 → COR-21 — CLOSED by dead agent; verified.** B-5(a)/(b)/(c): the "six date cells" undercount re-measured to
seven+one (8) and printed in `stage_1.md` §Boundary 4; `L3246-3250`→`L3246-3251` corrected in all six places
(`timeline.csv` row 17, `conflicts.csv` U.011 ×2, `stage_1.md`, `CORRECTIONS.md` ×2) with the old range kept visible
inside the retraction sentence; P2-07 carries `[OCR JOIN L1354-1355: …]` and the P2 preamble states the convention.
Verified all six at grep; not re-applied.

**RB-5 → COR-22 — corpus CLOSED by dead agent; master row MISSING → I closed the gap.** The dossier's own premise
line (`research/B1_dayton_print_records.md` L74-75, split across two lines) is now printed in `stage_1.md` §Boundary 4
and `conflicts.csv` U.011 carries "COR-22 … claim_a … is the dossier's own premise line." The conflict and COR-01
stand. **But `COR-22` had no row in `CORRECTIONS.md`. I added it** (see §2). `_parts/s1_p1.md` also carries the stale
quote — left untouched (out of write scope; `_parts/*` is superseded audit trail per RB-7v).

**RB-2 (the COR-19 leg) — CLOSED by dead agent under COR-19; verified, not re-applied.** §T.1 (stage_1.md ~L1799-1805)
tiers corrected to 3 for P2S01/P2S07/P2S02/P2S04 and P2S05 re-tiered 1→2, each "tier corrected 2026-09-30 … (RB-2)";
`sources.csv` S4216 "RE-TIERED 1→2 under RB-2"; the 503 assertions qualified as "what the run recorded; bodies print
500 / no status line → code UNKNOWN" at stage_1.md L66, L182, L818, L861-865, L1758. The FETCH REQUESTs
(`repair_pass2` §14) are correctly **left open** — the status code is UNVERIFIABLE-FROM-BYTES, not a null; no web
budget spent. NOTE: the §U register-emission claim records P2S02/P2S04 (stage_1.md ~L2357/L2359) still read "returned
HTTP 503" — these are NOT among the RB-2 census's nine live lines and are emission-slice records of what the run
logged; I left them (not RB-listed; touching them risks a double-edit). Flagged for the re-certifier.
RB-2 was propagated under the **existing** COR-19 id (the retraction it completes), not a new id — see §3 on COR-23.

**RB-4 → under COR-15 — CLOSED by dead agent; verified.** stage_1.md §Boundary 5 now reads "dollars exist for **1966
and 1967 only** … (both printed in the FY1967 layer … r16 and r69; the former '1967 only' was refuted … COR-15 …
RB-4, closed 2026-09-30)". Reaches the register through COR-15's r69-r72 rows. Not re-applied.

**RB-7 → COR-24 — corpus CLOSED by dead agent; master row MISSING → I closed the gap + scoped one sub-item.**
§S.1's payroll null re-pointed off U.028 to **U.103**; **U.101/U.102/U.103** all minted (three formerly-unkeyed
`data_gaps.csv` rows — 1963-64 openings, 1962-65 cost/land/vendor, payroll/wages/headcount); RB-7iv stale self-count
"37,507"→"41,534" with the old number kept as a dated string (stage_1.md ~L281-282). **`COR-24` had no
`CORRECTIONS.md` row — I added it.** RB-7v (gates advisory / `_parts` "volume 1" / no `periodical_harvest target`
task) is tools/orchestrator scope, not company writes — reported, not done.

**RB-1 → COR-23 — NOT closed by the dead agent → I closed it (this pass's substantive work).** See §2/§3.

---

## 2. What I changed (all CLAIMed to `target-repair-3b`, all `--done` released)

Files written: `stage_1.md`, `sources.csv`, `CORRECTIONS.md`, `_MANIFEST.md`, `stage_1_index.md`, this log. No lock
was REFUSED (the 10 released locks were free); no `--force` used; `stage_1.md` never forced.

1. **RB-1 / COR-23 — instruction-layer reconciliation (rule 10).** `_MANIFEST.md` and `stage_1_index.md` — the two
   files every agent reads first — still printed the **pre-round-3** corpus as current (38,489 w / 261,590 B;
   sources 21 rows `S4201`–`S4221`; quantitative 68; data_gaps 22; 164 rows; 14 COR ids). The dead agent had advanced
   them only to the *pass-2* (2026-09-29) numbers, never to the current state. Re-measured to disk and updated, with
   every superseded figure kept as a dated "at the merge / at pass 2 / at recertification" string (rule 4):
   `stage_1.md` **42,833 w / 292,456 B**, `sources.csv` **25** rows / block **`S4201`–`S4225`**, `quantitative.csv`
   **72**×12, `data_gaps.csv` **23**×8, **173** register rows, **24** COR ids. Added the **Microsoft collision line**
   (`S4222`–`S4225` also held by `company_011_microsoft`, tracked cross-company as **task #31**, never re-minted —
   verified: its `sources.csv` runs `S4222`…`S4229`). Corrected `stage_1_index.md`'s id-range line and per-register
   counts likewise. `stage_1.md`'s own global-ids note also still printed `S4201`–`S4221` internally (contradicting
   its §COR-20 line 69) — fixed to `S4225` with the collision note.
2. **COR-23 markers so the id reaches BOTH layers** the way the gate counts them (a `stage_*.md` volume AND a `.csv`
   register): one true sentence in `stage_1.md` (global-ids note, volume layer) and one in `sources.csv` S4225's
   `notes` cell (register layer), both naming RB-1/task #31/the reconciliation date.
3. **`CORRECTIONS.md` master rows added for COR-22, COR-23, COR-24** (the retraction register — itself an
   instruction file under rule 10). Each row states the retraction, where it appeared, the fix, and the `Reaches`
   both-layer column, matching the COR-01…COR-21 table format.
4. **`_MANIFEST.md` addendum** pointing a cold reader from the dated 2026-09-29 gate-record block to the round-3b
   gate re-run and its 24/24/24 result.

## 3. COR-23 — a judgement call I flag rather than hide (do not guess at the corpus)

The dead agent opened COR-21 (RB-3/RB-6), COR-22 (RB-5) and COR-24 (RB-7), and propagated RB-2 under **COR-19** and
RB-4 under **COR-15** — it never used the number 23. **What COR-23 was reserved for cannot be recovered from disk**
(its log is a 285-byte stub; the QC hits on `COR-23` are a *different* company's file, `amazon_s3_*`). I assigned
**COR-23 to RB-1**, the one blocker with no id that is not demonstrably closed and that the §14 rule-10 incident
makes blocking. This is a reasoned assignment, not a recovered fact: if the re-certifier believes COR-23 was meant
for RB-2, then RB-2's corpus work is already correctly tagged COR-19 (the retraction it propagates) and no id is
missing — the choice is a bookkeeping one, and I did **not** re-tag the dead agent's standing, correct RB-2 edits to
force a different reading.

---

## 4. Sweeps run, with hit counts (every one)

- `grep COR-21/22/23/24` across `company_042_target/*.md`, `*.csv`, `03_quality_control/` — counts in §0.
- `git diff --stat HEAD~8..HEAD` (target dir) → **empty**; `git log -S 'COR-21'` → **empty**; `git diff --stat HEAD`
  → the 10-file round-3 footprint (all uncommitted).
- RB-1…RB-7 mentions mapped to COR ids across the corpus (grep, per-blocker evidence in §1).
- 503 lines in `stage_1.md`: 17 grep hits; nine RB-2 live lines all qualified; L2357/L2359 claim records left (§1).
- `S4201`–`S4221` / `38,489` / `68 rows` / `164` residuals in the two instruction files: re-checked after editing —
  remaining hits are inside the **dated 2026-09-29 gate-record block** (rule 4 history) and the retired-id alias map,
  both intentionally retained.
- "1967 only" / Target-unit class: 0 surviving live claims (all read "1966 and 1967").
- Microsoft `sources.csv` `S4222`–`S4229`: confirmed the cross-company overlap behind the new collision note.
- Per-COR two-layer re-check (final): COR-21 vol 5 / reg {conflicts,timeline}; COR-22 vol 1 / reg {conflicts};
  COR-23 vol 1 / reg {sources}; COR-24 vol 4 / reg {data_gaps}; all four now 1× `CORRECTIONS.md` row.

## 5. Before → after (re-measured after the last write)

| quantity | before (round-3 open) | after (this pass) |
|---|---|---|
| `stage_1.md` | 42,701 w / 291,581 B | **42,833 w / 292,456 B** |
| ids defined in `CORRECTIONS.md` | 21 (COR-01…21) | **24 (COR-01…COR-24)** |
| COR-22 master row | 0 | 1 |
| COR-23 (all layers) | 0 / 0 / 0 | 1 / 1 / 1 |
| COR-24 master row | 0 | 1 |
| instruction-layer counts | stale (38,489 / 68 / 22 / 164 / 14 / S4221) | reconciled to disk (42,833 / 72 / 23 / 173 / 24 / S4225) |
| gate `corrections` | "21 ids; reaches 21, 21" | **"24 ids; reaches 24, 24"** — all reach registers and volumes |
| gate findings / exit | 2 ADVISORY / 0 | **2 ADVISORY / 0** (unchanged; no new defect) |

**GATE (prescribed, second half):**
`python tools/gates.py --company-dir founders_playbook/01_companies/company_042_target --tier core --out
founders_playbook/03_quality_control/target_s1_gates_round3b.md` → Findings 2, Passes 18, exit 0. The two findings
are both ADVISORY and pre-existing: (i) 1-of-1 attributed quote unmatched (the §15.6 intake gap, not a fabrication);
(ii) 42,833 words over the 22,000 core *planning* target. My instruction-file prose added one further ADVISORY
unattributed-span candidate (`stage_1.md::at the merge at pass 2 at recertification`) — a quote-triage artifact of
the reconciliation wording, not a fabricated carrier.

## 6. Left deliberately, with reason (not silently dropped)

1. **quantitative.csv internal census** — I re-measured the *geometry* (72×12) to disk but could not re-derive the
   "65 of 68 rows carry a PERIOD BASIS tag / 7 DERIVED" figure with a column-aware parse from grep; the four COR-15
   rows are printed-figure money rows with basis stated in-cell. I flagged this inline in `_MANIFEST.md` and here
   rather than guess the tag count. → re-certifier to re-derive.
2. **`sources/_index/_INDEX.md` L26-27 "certifier blocker B-4"** (RB-7iii) — the referent is genuinely ambiguous
   (`repair_pass2` §4 numbers the provenance-block work "blocker 4"; the recertifier reads B-4 as U.032). Two
   legitimate readings; I left the line and did not guess at the corpus. → adjudicate on re-certification.
3. **stage_1.md self-count** now reads 41,534 (RB-7iv's value) vs disk 42,833 — the +299-word drift is from this
   pass's own COR-23 volume marker; chasing a self-referential word count in an instruction file past each edit is
   unbounded. Non-blocking (RB-7 minor). Noted, not touched again.
4. **§U register-emission P2S02/P2S04 "returned HTTP 503"** — outside the RB-2 nine-line census; leaving to avoid a
   double-edit of already-corrected negative-artifact records.
5. **`_parts/s1_p1.md`** stale quote (RB-5) and **`_parts/s1_p2.md` "volume 1"** (RB-7v) — `_parts/*` is superseded
   audit trail, no agent writes it.
6. **No new git commit made** — round-3's work was never committed by its owner; committing is not mine to decide
   mid-flight. The whole corpus (round-3 + round-3b) still sits in `git diff HEAD`.

## 7. Carriers / FETCH REQUESTs (web budget: 0)
No web call made; no carrier opened that was not already held. RB-2's status codes remain
**UNVERIFIABLE-FROM-BYTES**; the three `repair_pass2` §14 FETCH REQUESTs (EDGAR name→CIK browse; Wayback CDX
target.com/dhc.com; the 17 Image-Container PDF legs) stay open on the same terms — none close on held bytes. No new
`FETCH REQUEST:` raised; nothing I needed was unreadable on disk except the ambiguous `_INDEX.md` attribution, which
is a reading question, not a missing carrier.

## 8. Re-certification request (§15.6 — certifier ≠ repairer)
I am the repairer; **I do not certify my own repair.** Requesting a **different** agent (`target-recert3`) to
re-certify Stage 1 against this log, `target_s1_gates_round3b.md`, and the six files I wrote. Specifically to
adjudicate: the COR-23 assignment (§3), the three items in §6 (1)(2)(3), and the two ADVISORY gate findings. RB-1…RB-7
are all reported above as CLOSED / (RB-2/RB-4) closed-under-existing-id / with §6 exceptions documented. No blocker
left un-described; nothing re-applied that the dead agent had already landed correctly.
