# Audit Protocols — the Five Mandatory Gates

Spec §28 requires five independent audits before any output is produced, and §11 forbids
answering a failed audit with a disclaimer: **a failed audit means researching again.**
This file defines how each audit is executed, what counts as pass, and where failures go.

Every company runs all five per stage, plus one consolidated pass across its three stages.
Results are recorded in `per_company/<company>_audit_sheet.md` using the template at the
bottom of this file. Auditors are independent of the agent who produced the material being
audited; the Master Orchestrator assigns, and a Company Lead never audits its own report.

**An auditor never edits what it audits.** A repair is a separate pass by a different agent, so that
the audit sheet stays a record of what was wrong rather than being quietly rewritten to match what the
file now says. Where a defect is found in a correction the orchestrator itself authored, the auditor
reports it and the orchestrator supersedes its own ruling in `CORRECTIONS.md` with the superseded text
visible (as AUDIT 2 did with COR-03 → COR-12). Findings that would require re-running retrieval are
opened as research debt, not repaired inside the audit sheet.

**Audits may not manufacture verdicts to look rigorous, nor soften them to be agreeable.** Both are
audit failures. A clean pass must cite the line that proves it.

---

## AUDIT 1 — Chronology

**Question:** does every statement belong to the period it is placed in, and does the
sequence hold together?

Procedure:
1. Build the stage's event list from `timeline.csv` and sort it.
2. For each dated event, verify the date against the cited source's own date — not against
   the article's memory of it. Record `publication_date` vs `event_date` mismatch explicitly.
3. Hunt for **time travel**: any description of an earlier period that is only true of a
   later one (a 2020s fact stated as 1995 knowledge; today's product architecture used to
   describe the first version; a later feature retro-projected onto an MVP).
4. Check stage boundaries against the evidence: does the boundary event actually fall where
   claimed, and is the claim that "Stage N ends here" supported by something contemporaneous?
5. Check that no event later than the stage's endpoint is used as *evidence* rather than as
   `RETROSPECTIVE SOURCE` explaining an earlier event.

**Pass:** zero unexplained date contradictions; every boundary event dated to at least month
precision with a source; every post-stage reference tagged.
**Fail →** open research debt; re-date from primary records (filings, registry, archived
pages, contemporary press), do not average two conflicting dates.

## AUDIT 2 — Sources

**Question:** does every material claim have adequate evidence, and is that evidence what it
claims to be?

Procedure:
1. Sample every claim in sections A–U against the claim-record appendix: does each carry a
   retrievable URL, a publication date, a tier, an evidence class, and a confidence rating?
2. Re-verify a stratified sample (all Tier-1 claims, all numbers, all famous anecdotes, plus
   10% of the rest): fetch the source and check the passage actually says what is claimed.
   Rate SUPPORTED / PARTIAL / UNSUPPORTED.
3. Collapse false corroboration: where three sources trace to one unsourced origin, mark
   them as one source and re-derive confidence.
4. Verify founder-claim density per section: flag any section whose material claims rest
   primarily on founder storytelling, and label whether each is a contemporaneous statement
   or a retrospective memory.
5. Confirm the legal boundary held: nothing sourced from leaks, private communications, or
   confidential documents; deep-but-public material labeled DEEP PUBLIC-SOURCE EVIDENCE.

**Pass:** no UNSUPPORTED claims surviving in the text; every material claim ≥2 independent
sources or explicitly downgraded to Medium/Low with the reason stated; no Tier-4-only
material presented as fact.
**Fail →** the offending claim is cut back to what evidence supports, or a gap-fill
investigation is opened.

## AUDIT 3 — Numbers

**Question:** is every number real, correctly based, and arithmetically consistent?

Procedure — for every row of `quantitative.csv`:
1. Basis check: revenue vs GMV vs bookings; users vs customers; transactions vs orders;
   annual vs monthly; fiscal vs calendar (note Amazon's Nov–Oct fiscal year pre-1996 and
   calendar switch after); company vs segment; nominal vs inflation-adjusted.
2. Provenance check: contemporaneous, retrospective, or calculated? Calculated rows must
   carry `derived_arithmetic`; re-run the arithmetic.
3. Unit check: currency, and for pre-2000 figures state nominal unless adjusted.
4. Cross-foot: do stage totals reconcile with the next stage's opening snapshot (§R)? A
   snapshot that disagrees with the last metric in the same section is a defect.
5. Precision check: no manufactured exactness. A figure from a rounded memoir is written as
   `~$300,000 (ESTIMATE)`, never `$300,000 (FACT)`.
6. Contradiction check: where two sources give different numbers, both must appear in
   `conflicts.csv` with a best-supported interpretation. Silent reconciliation is prohibited.

**Pass:** every number basis-labeled, derived numbers shown, totals cross-footed, all
disagreements in the conflict register.
**Fail →** re-derive from the filing or contemporaneous report; if unrecoverable, replace
with UNKNOWN and record the loss in `data_gaps.csv`.

## AUDIT 4 — Hindsight

**Question:** would this reconstruction still read as plausible if the company had failed
five years after the stage ended?

Procedure:
1. Read each conclusion and ask what it would look like if the outcome were unknown. Rewrite
   any sentence whose force depends on later success ("this proved the model worked",
   "visionary decision to sell everything", "investors missed that...").
2. Check for inevitability language, and for the temporal-to-causal fallacy: X before Y is
   not X because of Y. Each causal claim needs a stated mechanism plus an alternative
   explanation, per spec §16.
3. Check survivorship framing: claims of the form "successful companies did X" must not be
   presented as "companies that do X tend to succeed" (§25).
4. Confirm the knowability split exists for the stage: KNOWABLE / NOT KNOWABLE / UNKNOWN,
   and that founders' decisions are explained from what they could reasonably have known.
5. Confirm no section optimizes for inspiration (§R: "Never optimize the report for
   inspiration") — failures and weak signals must be present, not implied.

**Pass:** zero outcome-dependent sentences; every causal claim mechanism + alternative;
knowability split present; negative-signal section non-empty.
**Fail →** rewrite the section, then re-run Audit 1 on anything re-dated in the process.

## AUDIT 5 — Adversarial

**Question:** what breaks this reconstruction?

Procedure:
1. Hand the stage file to an adversarial agent that has not seen the dossier that produced
   it, with the brief: try to prove the dominant narrative wrong, citing only evidence.
2. Require it to address: contradictory dates, divergent founder accounts, alternate revenue
   figures, failures omitted by popular histories, competitors overlooked, exaggerated early
   traction, retrospective mythology, survivorship bias, negative contemporaneous reporting.
3. Require the adversarial agent to grade the standard story element-by-element: well
   supported / contested / unsourced folklore, with the earliest traceable source for each.
4. For every challenge that lands, either re-research or downgrade the claim in the text;
   record the decision. For every challenge that fails, record why — that is the positive
   output of the audit.
5. The adversarial agent must not invent objections or use hindsight to sneer at actors
   who lacked the ending.

**Pass:** every narrative element has a verdict; no surviving claim rests on a challenge
that was never answered.
**Fail →** reopen investigation; do not proceed to output.

---

## Consolidated per-company pass (after Stage 3)

1. Run Audits 1–3 across stage boundaries: the end-of-stage snapshots must form one
   continuous series, and each transition must be justified by evidence, not by calendar.
2. Answer spec §21 — what actually changed from Stage 1 start to Stage 3 end, across founder
   capability, product, customer understanding, distribution, supply, technology, organization,
   capital, market understanding, business model, operations, trust, competitive position —
   plus the most important bottleneck per stage and the evidence that it broke.
3. Verify the endpoint rule (§7): Stage 3 must not end at IPO/unicorn/acquisition unless that
   event is itself the first evidence of the transition studied.
4. No scores, no rankings, no founder winner (§21).

## Per-company audit sheet template

```markdown
# Audit Sheet — <Company> (<company_id>) · Stage <N> · Run <YYYY-MM-DD>
Auditor: <agent id> (independent of producer: <yes/no>)

| Audit | Result | Items checked | Failures found | Actions taken | Residual risk |
|---|---|---|---|---|---|
| 1 Chronology | PASS/FAIL | | | | |
| 2 Sources | PASS/FAIL | | | | |
| 3 Numbers | PASS/FAIL | | | | |
| 4 Hindsight | PASS/FAIL | | | | |
| 5 Adversarial | PASS/FAIL | | | | |

## Claims cut or downgraded
| Claim ref | Was | Now | Why | Evidence applied |
## Research debt opened by this audit
| RD id | Section | Debt | Assigned | Status |
## Sign-off
Stage status: RECONSTRUCTION → ADVERSARIAL REVIEW → QA → COMPLETE
COMPLETE requires all five rows = PASS and all High-importance gaps to carry a follow-up task.
```
