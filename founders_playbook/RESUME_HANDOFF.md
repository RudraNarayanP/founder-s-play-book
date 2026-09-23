# RESUME HANDOFF — read this first if you are starting this project cold

Generated 2026-09-23, while Amazon Stage 1 was in its final repair passes.

## 1. What this project is

`THE FOUNDER'S PLAYBOOK` — a forensic longitudinal dataset reconstructing the early histories
(origin → first experiment → repeatable validation → scalable company) of the 2026 Fortune 500 top-50,
claim by claim, with public-source provenance and a hindsight firewall.

**Read in this order:** `00_METHOD_AND_STYLE.md` (the binding spec, incl. §9 file-splitting and §14
retrieval discipline) → `MASTER_RESEARCH_LOG.md` (universe freeze, status table, decisions, open
research debt) → `01_companies/company_001_amazon/CORRECTIONS.md` → `company_001_amazon/stage_1.md`.

## 2. State at handoff

| Item | Status |
|---|---|
| Universe | **FROZEN, verified.** `00_universe/fortune_top_50_2026.csv` — 50 rows, 49 complete, revenue XBRL-verified on 45; feasibility register classes all 50 by evidence depth |
| Amazon Stage 1 | **Assembled, ~92k words** (`stage_1.md` 37.7k + `stage_1_claim_records.md` 47.9k + `context_appendices.md` + `adversarial_review.md`), 11 dossiers, 9 CSV registers |
| Audit 1 chronology | **FAIL → repaired.** Boundary re-based 1993 → **1994** (first anchor 1994-07-05 founding instrument); 0 date errors otherwise |
| Audit 2 citations | **PASS.** 23 supported / 1 partial / 0 unsupported; caught a wrong orchestrator correction (COR-03 → superseded by COR-12) and a mis-attributed press release (COR-13); its own "$245,572" claim was **rejected as unverified** (RD-022) |
| Audit 3 numbers | **FAIL → repair in flight at handoff.** 31 defects, 9 HIGH (`_parts/NUMBER_DEFECTS.md`) — incl. a $355,000 cumulative-losses figure against an audited $248,000 deficit |
| Audit 4 hindsight | **FAIL → repaired.** All 19 findings applied; record-selection null added to §A/§S; five causal codas given mechanism + alternative |
| Audit 5 adversarial | Deliverable `adversarial_review.md` exists (30 elements: 4 well supported / 18 contested / 8 unsourced folklore); the **verdict pass on the repaired file has not been re-run** |
| Walmart (002) | **Feasibility probe in flight at handoff** — depth verdict pending before any fleet is committed |

**If the machine was shut down mid-flight, the two in-flight passes may have left partial edits.**
Check `git status` / `git log -1` for the last clean commit, then re-run only the pass that was open.

## 3. To resume Amazon Stage 1 sign-off

1. Re-run **Audit 3** against the repaired numbers; require PASS before anything else.
2. Re-run **Audit 4**'s four failing conditions (outcome-dependent sentences, causal mechanisms,
   endpoint framing) to confirm the repair, not just the intent.
3. Run **Audit 5** as a verdict pass on the repaired text, per `03_quality_control/AUDIT_PROTOCOLS.md`.
4. Regenerate `01_companies/company_001_amazon/_MANIFEST.md` word counts.
5. Only then mark Stage 1 `QA → COMPLETE` in the status table. **Do not mark COMPLETE on the strength
   of this file.**

## 4. Non-negotiables the last session learned the hard way

- **Never invent** a URL, date, quotation, accession or number. `UNKNOWN` is a correct answer; a
  plausible filler is not.
- **A correction is a claim** and gets audited — one authored by the orchestrator was wrong
  (COR-03) and an auditor's unsourced figure was rejected (RD-022).
- **Auditors do not edit what they audit.** Repairs are a separate pass.
- **Never delete or tidy a shared directory.** An agent destroyed the entire downloaded evidence base
  this way; it was rebuilt from EDGAR at real cost. `sources/` is read-only; agents write only their
  own named output file.
- **Write first, then research.** Six agents in one session burned their whole budget retrieving and
  wrote nothing (§14).
- **Repeated copying is one source**, not corroboration — `independence_note` in `sources.csv` exists
  to enforce this.
- Serialize writers on `stage_1.md`: two agents editing it at once produced conflicts that had to be
  re-applied in order.

## 5. Open work, highest value first

1. RD-030 — could a two-person Washington firm obtain a **company-only** merchant account in Nov 1994?
   Decides whether Bezos's personal guarantee was credit rationing or standard practice. Nothing in the
   file answers it, and §K currently implies an answer.
2. RD-029/031 — directory-placement and press efficacy in 1995 are **company-claimed, unmeasured**; chase
   an independent dated record or leave them UNKNOWN.
3. RD-008 — the Cadabra → Amazon rename date is undocumented; Washington Secretary of State was
   unreachable. Try Washington State Archives and period trade notices.
4. Stage 2 (Amazon, 1996–1997) — the primary filings are already local in
   `company_001_amazon/sources/`, so Stage 2 starts with a much cheaper evidence base than Stage 1 did.
5. Cross-company synthesis stays **closed** until individual reports pass QA (spec §22).

## 6. Throughput, so nobody over-promises again

Exemplar depth measured out at **~8–10 hours of agent time per company** (11 dossiers, 7 assembly parts,
5 audits, 2+ repair passes), which is ~400–500 hours across the remaining 49. One stage per working
session is the real rate. Parallelizing companies is what the feasibility-register tiers exist to support:
exemplar only where archives can carry it.
