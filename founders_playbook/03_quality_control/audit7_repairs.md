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

## Outcome log
(appended per row as worked)

## Invariants — recomputed at the end
