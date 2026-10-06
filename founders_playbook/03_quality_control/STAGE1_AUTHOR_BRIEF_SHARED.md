# STAGE-1 AUTHOR BRIEF — shared contract (read fully before writing a word)

You are writing **one part of one company's Stage-1 dossier** for the Founder's Playbook. You are an author,
not a merge agent, not an auditor, not a certifier. Your part file is the only corpus file you create.

## Read first, in this order
1. `founders_playbook/00_METHOD_AND_STYLE.md` — §4–§8 (claim classes: FACT / FOUNDER CLAIM /
   CONTEMPORANEOUS OBSERVATION / RESTATED / RETROSPECTIVE INTERPRETATION / INFERENCE / ESTIMATE / UNKNOWN;
   confidence; the hindsight firewall), §9 (report shape, §9.2/§9.3 word caps, §9.6 live counts), §13 (the
   nine registers and their controlled vocabularies), §14 (the defect catalogue — it is a list of things this
   project paid for in lost work, not advice), §15 (the scripted pipeline that binds you).
2. Your company's probe dossier `research/A_chronology_feasibility.md` (and `A3_intake_regrade.md` /
   `A4_harvest_mine.md` if present). **The probe's tier and its five-family verdict are your scope.** If you
   disagree with a tier, say so in your log — do not silently re-tier.
3. `company_001_amazon/` **for format only.** Amazon is the exemplar whose shape the registers and sections
   must match. Its content is a different company: never import an Amazon value, date, or phrasing.
4. `founders_playbook/03_quality_control/PROBE_BRIEF_SHARED.md` if you need the tool forms again.

## The six rules that have each cost real work already
1. **No invention.** A figure, date, name, or role enters only if you can point at bytes in `sources/`. Where
   nothing prints it, write `UNKNOWN` and name the route that could. `UNKNOWN` is a deliverable, not a failure.
2. **Quote or attribute honestly.** A quotation must appear in a held file at the place you cite. A
   paraphrase inside quotation marks is a defect (§14.10). Cite by stable label — `§P147`, `U.3`, a register
   key — and use a line number only as a locator, because your own edits move lines.
3. **Independence (§3).** An S-1 + its amendments + the 424B are ONE lineage. A scanner is a carrier, not a
   second witness. Byte-identical files across two shelves are one document (md5 before counting corroboration).
   A search-index row, a `TIER1_CANDIDATE` label, or a tier stamp is not evidence.
4. **Roles are not founders; predecessors are not the registrant.** If the famous founding year belongs to a
   different legal person, that IS the finding — write it that way. This project has now caught Morgan Stanley
   (= Dean Witter), Cigna (a 2018 shell), AT&T (= SBC), Marathon (= MPC Holdings), Boeing, Kroger, Ford,
   Citigroup, Verizon, ExxonMobil and BofA doing it.
5. **A null must be earned.** Distinguish TRIED–ANSWERED / TRIED–UNANSWERED (the tool or network refused — name
   the remedy) / UNTRIED. Never report a family you did not attempt as empty, and never report a faceted query
   or a capped enumeration as a census (§14.14, RD-130, RD-134).
6. **Append as you go.** Write each section and mark it `STATUS: WRITTEN` before starting the next. Several
   agents in this run died at their turn ceiling; the file survived every time, the report never did. Close
   out early rather than being cut off mid-sentence.

## Registers you emit (do NOT write the company's live CSVs)
Emit register rows as **fenced CSV append blocks** inside your part file, one per register, each preceded by a
`>>> REGISTER ROWS FOR MERGE <<<` marker naming the target register, with a header row identical to Amazon's
corresponding register, and every column quoted where a comma can appear. Nine registers: `quantitative,
timeline, sources, conflicts, data_gaps, decisions, validation, failures, channels`. Controlled vocabulary:
`stage` = `stage1` (never a bare number), CONTEMPORANEOUS vs RESTATED labelled per row, and a `source_id`
**left blank or provisional** — the merge agent mints real ids centrally via `tools/id_mint.py`, because ids
minted by authors have collided. Each conflict you register needs its `U.nn` anchor section written in your
narrative too: the merge proves 1:1 parity, and a mismatch is a defect you will be asked to fix.

## Emission contract (measured, so the merge can actually use your rows)
- One block per register, contiguous, no prose inside a block, and **every row at the header's width**
  (unquoted commas have shifted whole registers by one field).
- State per block: rows emitted. State in your REPORT: rows emitted per register, and any row you withheld.
- A row you cannot attribute to a register is worse than a paragraph — leave it out and describe it in prose.

## Gate before you report
`python tools/gates.py --company-dir <your company dir> --tier auto --checks csv,keys,anchors,corrections --out <your gate file>`
Coverage findings ("no registers yet", "no stage volumes yet") are the **expected** pre-merge state — they are
not defects and you must not "fix" them by inventing files. A finding you believe is the tool's error: write
the evidence in your log and leave the data alone; never reshape real data to silence a gate.

## Report format (and every number re-measured after your last write)
Part file path · word count · sections written / pending · claim records for your sections · anchors declared
· register rows by register · the five families as you found them · `## Untried` written · `FETCH REQUEST:`
blocks emitted · what you refused to claim and why · one line stating what you did NOT examine.
