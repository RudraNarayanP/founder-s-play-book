# Shared Stage-1 audit brief (read this whole file before your first tool call)

Orchestrator-dispatched. Every Stage-1 volume in this run gets audited by an agent that is **not** its
author, **not** its merger, and will **not** be its repairer or certifier (§15.6). You produce findings.
You do not repair them.

## Path discipline (three agents have gotten this wrong)
Repo root is `E:\founder's playbook`. Write your report to
`founders_playbook/03_quality_control/<slug>_s1_audit<n>.md` — that is relative to the repo root, so the
full path is `E:\founder's playbook\founders_playbook\03_quality_control\...`. A root-level
`03_quality_control/` already exists as a mistake; **do not create files there and do not delete what is
in it.** Claim the path first: `python tools/scaffold.py claim --agent <your-id> --path <the report path>`,
release it `--done` at the end. If a claim is refused by a LIVE owner, report the refusal; never `--force`.

## What to check (five lenses, in this order — all against bytes, not against the volume's own summary)
1. **Merge integrity.** Re-run `python tools/merge_census.py --company-dir <dir> --verbose`. Prove every
   requested register row is present in the CSVs, count them per register, and diff the volume against the
   read-only `_parts/*.md` (nothing of the author's was dropped or silently rewritten). Report any row the
   census cannot attribute (`validation.csv` vs `failures.csv` have byte-identical schemas — adjudicate by
   content and say how).
2. **Numbers.** Recompute every quantitative row from the carrier it cites (`sources/**`, file + line). For
   each: does the line exist, does the figure match, and is the row labelled CONTEMPORANEOUS vs RESTATED
   correctly for its own date? This corpus's recurring arithmetic traps: earned vs written premium, combined
   ratio read as margin, period-end vs average headcount, a restated figure presented as contemporaneous,
   `(PB)` post-boundary values, and one lineage's amendments counted as corroboration.
3. **Citations.** Every `Snnnn` in the narrative and registers must resolve to a `sources.csv` row, and that
   row's file+line must print the quoted text. Run `python tools/gates.py --company-dir <dir> --checks
   quotes,keys --out <your report path>` and treat its ADVISORY output as a **triage list, not a defect
   list** — but check a sample of the unmatched spans by hand and say which class each is: real paraphrase
   in quotes, OCR/glyph difference, or a quotation of a `research/*.md` dossier (that last class is a known
   `gate_quotes` limitation: it indexes `sources/**` only, so it can never match — do not report it as a
   defect, and do not "fix" the quotation).
4. **Chronology / hindsight.** Does any claim's evidence post-date its event by a generation and get
   presented as contemporaneous? Are founding years attributed to the right **legal person** — the famous
   date often belongs to a predecessor or a differently-named registrant (Morgan Stanley = Dean Witter, Cigna
   = a 2018 shell, AT&T = SBC, Marathon = MPC Holdings, ExxonMobil's historic CIK 34088 vs the ticker's
   2115436, Boeing's 1916 "Aircraft" vs the 1927 "Airplane"). An UNKNOWN with a named route is a pass, not a
   failure; a confident date with no carrier is a blocker.
5. **False nulls.** For every "0 occurrences", "no held byte", "never printed", "absent from the archive"
   claim in the volume: grep the held bytes yourself, and check whether the null was produced by **our own
   parameters** (a YEAR facet, a slice cap, a name-only matcher, an in-window perimeter that excludes EDGAR's
   1994 floor, an unfetched family). A false zero inside a CORRECTIONS marker is the worst variant, because
   later passes trust the marker.

## Also check, cheaply
- Registers vs narrative agreement on the same fact (a retraction that reached `CORRECTIONS.md` but not
  `conflicts.csv`/`quantitative.csv` is a finding: `--checks corrections`).
- Published live counts (`_MANIFEST.md`, `## Close-out measurements`) — re-measure and report drift.
- `stage` vocabulary is `stage1`, never a bare number; no renumbered sections; hard cap 60,000 words per
  volume (`--tier auto` is fixed as of RD-142 and now reads per-stage table rows — do **not** pin
  `--tier core` unless the tool disagrees with the dossier, and if it does, say so rather than editing prose).

## Output contract (six lines, then the detail)
- **VERDICT**: PASS / FAILED — with one blocker named if FAILED.
- **B-n** blockers (a claim that contradicts a held byte, a fabricated citation, a row that does not recompute).
- **F-n** findings (wrong label, unreproduced count, missing carrier, mis-tiered row) each with file+line evidence.
- **Clean checks** — list what you tested and found nothing, so absence of a finding is not silence.
- **Your matcher's error rate** — how many of your own hits were false positives. This is mandatory.
- **Untouched**: files you did not write, and the fetches you did not run.

Write only your report. Do not edit a volume, a register, a manifest, `sources/`, `research/`, or
`MASTER_RESEARCH_LOG.md`.
