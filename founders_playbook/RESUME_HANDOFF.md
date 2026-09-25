# RESUME HANDOFF — read this first if you are starting this project cold

Generated 2026-09-23, while Amazon Stage 1 was in its final repair passes.

## 0. STOPPING POINT — 2026-09-24 ~13:50 UTC (supersedes the 09-23 block below, kept as history)
## 0. STOPPING POINT — 2026-09-25 ~20:20 UTC (supersedes the 09-24 block; the 09-25-morning table below it is also now stale in its "running" column)

| Gate | State now |
|---|---|
| Amazon Stage 1 | **SIGNED** (AUDIT 8, read-only certifier, 26 of 50 calls). 43 U-blocks ↔ 43 rows; §P.2 recomputed; named residuals RD-050…RD-067, no blockers. Its retracted-value sweep is what exposed RD-059 — the handoff file itself was still teaching agents to use `$871,000`; withdrawn in place, rule generalised as §14.10 |
| Amazon Stage 2 | 3 volumes, 81k narrative + 479 claim records + 70 §U blocks (U.44–U.113). Chronology audit repaired; **citation audit repaired and independently verified** (all nine defects closed; verifier overturned the audit on three points). Remaining Stage-2 gates: numbers, hindsight, adversarial |
| Amazon Stage 3 | Five dossiers: chronology (59 rec), finance (22 rec/142 rows), product+market (68 rec), tech+ops (53 rec, 9 DC openings), adversarial **still running**. Boundary argued for **1999-06-30 substantive / 1999-08-16 disclosed**, rivals FY1998 close rejected on its own documents and 1999-09-30 held as the conservative alternative. **Registers merged early**: 427 Stage-3 rows applied, conflict rows keyed **provisionally P-U.114…P-U.152** with each dossier's own id preserved in `section` (see `03_quality_control/stage3_register_merge_held_rows.md`); 10 rows held for width. Assembly into §A–U has **not** started |
| Off-machine | QCA sessions still **402** (no credit). The nightly harvester **runs and writes to `main`** (first commit `2e90df0`) — and that run is what disproved the bot-block diagnosis: Google Books and HathiTrust answer once requests are shaped right; **LoC really is gated** (`robots.txt` itself returns a Cloudflare challenge) |
| Other companies | Walmart: A2 (133 rec, superseded at 39 sites) + A3 (9 fiscal years, every row labelled CONTEMPORANEOUS/RESTATED) + A4 (40 rec, 164 register rows) + A5 (the SEC-statistical hypothesis closed as a page-level negative; independent lineage **still 1**; NLRB volumes unspent). Apple: 4 dossiers + 4 registers, probe corrected. UnitedHealth: money series to FY1990, verdict forensic-core on an explicit premise |

**Next five actions:** (1) when ST3_E lands, dispatch Stage-3 assembly in four parts mirroring Stage 2's geometry; (2) re-base Stage-3 conflict ids P-U.114… → U.114… in the same operation that writes the §U blocks, then re-test 1:1 parity; (3) resolve `RD-060`'s split factor (**12×, not 6×**) through every per-share figure before the numbers gate; (4) run the three remaining Stage-2 audits with auditors who wrote none of the text; (5) apply the FY1999 10-K riders (`OC-D1`/`OC-D2`) into ST3_A/B/C rather than re-running those dossiers.

**Standing discipline:** every agent brief now carries an explicit tool-call budget and a byte destination (§14.9), one write path per agent (§14.7), and a "verify from disk before re-dispatching" instruction — four agents died at their ceiling this week with the work done and the record blank.


Run `git log --oneline -6` for the exact last state; everything named here is committed and pushed.

| Gate | State now |
|---|---|
| Amazon Stage 1 | **QA — REOPENED.** AUDIT 6 (independent verifier, `03_quality_control/audit6_stage1_independent_qa.md`) = CONFIRMED 7 / DEFECT 6. All stored arithmetic held (43 U blocks ↔ 43 conflicts rows, 428 rows parsing clean, 29/29 `derived_arithmetic`, 32/32 §P.2 recomputations); the gate still failed because four *closure assertions* were false and one adversarial attack (A-B1) still lands. Repair in flight (`audit6_repairs.md`); **a third agent must re-certify — not the repairer, not the verifier** |
| Amazon Stage 2 | **RECONSTRUCTION.** Parts on disk: `s2_p1` 10,545 w (boundary + §A–D), `s2_p2` 14,810 w (§E–J), `s2_p3` 5,668 w (§K–O, thin — RD-043), `s2_p4` **incomplete** (§P only; §P.2/§Q–§U from U.44 + CSV append blocks in flight). Window is frozen: **1996-01-01 → 1997-05-15** |
| Walmart Stage 1 | `A2_chronology_finance.md` at **133 records / 38k w** after a double-dispatch collision (renumbered under a collision note). Boundary proposal: start 1945 *registrant-retrospective*, end **1970-10-08**. Verdict stays **provisional exemplar-gated**: corporate print positive, periodicals **UNANSWERED (not null)**. COR-A2-10 found the IA corporate_print run contiguous **FY1972→FY1998** → FY1974/75/77/78/79 retrievable as primaries; retrieval in flight (several "audited" years are currently later restatements — RD-044) |
| Apple Stage 1 | `A2_periodical_archive_mine.md` **80 records / 29k w, 0 web calls**, four registers built (`quantitative` 30 / `timeline` 23 / `sources` 13 / `conflicts` 13, headers verified byte-identical to the §13-conformant Amazon registers). Its 13 outbound corrections are being applied as supersession (RD-046); `C_corporate_legal_org.md` and `D_adversarial.md` in flight |
| Off-machine compute | **Not yet real.** `.github/workflows/harvest.yml` is registered `active` on the default branch but has run **zero** times: it was pushed at 12:16 UTC and its cron is 06:17 UTC, so it simply has not fired yet. `workflow_dispatch` is the way to force it — needs a GitHub token, which is deliberately NOT stored in this repo. QCA sessions are still blocked on HTTP 402 (no account credit); see `CLOUD_LAUNCH.md` §8 |

**In flight right now (six agents, disjoint paths by construction):**
Stage-1 repairs (`s1-repair`) · Stage-2 `_parts/s2_p4.md` completion (`s2-p4b`) · Walmart FY1974-79 IA
retrieval (`wm-ia`) · Apple probe supersession (`apple-sup`) · Apple `C_corporate_legal_org.md` (`apple-C`)
· Apple `D_adversarial.md` (`apple-D`).
**Do not relaunch any of these until they have reported** — this wave already paid for a double-dispatch
collision (method §14.7).

**Next five actions, in order:**
1. When `s2_p4` lands: merge `s2_p1..p4` → `stage_2.md` (mirror Stage 1's geometry, 60k-word cap per file,
   split at section boundaries only), then dispatch the Stage-2 claim-record registrar.
2. Apply `s2_p4`'s `>>> CSV APPEND BLOCK` sections to the nine registers — conflicts rows must key 1:1 to
   U.44…U.nn, because 43-block/43-row parity is a verified Stage-1 invariant.
3. Re-certify Stage 1 with a **third** agent against `audit6_repairs.md` (the repairer may not sign its own
   work; the AUDIT 6 verifier may not either, since it changed nothing but asserted nothing fixed).
4. Once the Walmart FY1974/75/77/78/79 texts are on disk: re-run the audited-series section against
   contemporaneous reports, and re-derive the depth verdict on five corpus families, not three.
5. Trigger the nightly harvester once (or wait for 06:17 UTC) so the UNANSWERED periodical families get a
   first real attempt — that single change gates the depth verdict of every pre-1994 company in the universe.

> ### ⚠ CANONICAL-VALUES WARNING — added 2026-09-25, supersedes every instruction below it
>
> Two passages in this file (the 2026-09-23 history block: the Audit 3 row and action-list item 1, and the
> older status table's Audit 3 row) tell a cold reader to use **$871,000** and a **$976,408** composition as
> "canonical values". **That instruction is withdrawn.** The leg depends on a `2,613,000` denominator that
> appears in **0 of the 93 filing texts on disk**, and the citation offered for it — original S-1
> l.4301–4302 — in fact prints `3,021,000 / 23 investors / $.3333 / $1,007,000`. The correct state of that
> figure is **UNKNOWN**, and so is the composition split. What *is* filed and safe: the
> **$1,007,000 / 23-purchaser** program, the **$345,525** tranche at **$.1717**, **$1,272,000** of CY1995
> equity cash, the **$996,000** and **$(248,000)** balance-sheet points, and the **+94.1%** step-up.
>
> Why this matters more than one wrong number: **this file is an instruction set, not a report.** Every
> agent dispatched reads it before it reads anything else, so a retracted value written here as canonical
> re-imports into whatever that agent writes. That is how it survived three repair passes — the corpus was
> fixed around it and the handoff kept telling people to use it. Recorded as **RD-059** by
> `03_quality_control/audit8_stage1_certification.md`, whose certifier noted the same asymmetry: it is the
> one file in this repository whose job is to be believed without being checked.
>
> **Rule adopted:** a retraction must be propagated to the instruction layer (this file, the master log's
> status sections, `_MANIFEST.md`) in the same pass that retracts it in the corpus. Sweeping the corpus and
> leaving the handoff stale is how a fixed defect comes back.

## 0-hist. STOPPING POINT — session ended 2026-09-23, machine powering down (superseded, retained as the audit trail of what was decided then)


Everything below is committed and pushed to `main` on
`github.com/RudraNarayanP/founder-s-play-book`; run `git log --oneline -5` for the exact last state.

| Gate | State at shutdown |
|---|---|
| Audit 1 chronology | FAIL → repaired. Boundary re-based 1993 → **1994**; consistency of that re-base across header, §B, §C, §Q, §R and the appendices was re-confirmed later |
| Audit 2 citations | **PASS** — 23 supported / 1 partial / 0 unsupported. Overturned the orchestrator's own COR-03 (superseded by COR-12) and had its own unsourced "$245,572" rejected (RD-022) |
| Audit 3 numbers | FAIL (31 defects) → repaired → **RECHECK ALSO FAILS, and this time the repair itself introduced errors.** Verdict: "all 31 fixed" was false — checks 1 basis, 2 provenance, 3 arithmetic and 4 cross-foot FAIL; 5 units and 6 precision PASS. **All 9 HIGH items are genuinely fixed at the filing line** (the $(248,000) deficit agrees at every site, orig. l.3461/l.3571; 14,555,244 shares confirmed on the balance sheet l.3455–3457 with no percentage using it as a denominator; $100,020.06 verified as 582,528 × .1717; the round now runs as division; the ~$921,000 refusal was correct because the audit's own tie was off by $3). 26/31 confirmed fixed. **Repair-introduced defects to close:** a false "+95.2%" step-up (real **+94.1%**) at P17/d6/L30; `§R` cites a `quantitative.csv` row that does not exist (D19 half-applied); `validation.csv` r20's class correction was written into the `confidence` column, leaving `evidence_class: DERIVED` stale; and "$871,024 at the filing's exact ⅓" is a plug — a true third gives $871,000. **One new conflict:** `conflicts.csv` r30 / §U.29 attributes 41% to the original S-1, which says **43%**; 41% is from No. 5. **ALL NOW CLOSED (2026-09-24)** by `amazon_s1_number_repairs2.md` and the two residual register sweeps (`amazon_s1_residual_sweep.md`, `amazon_s1_residual_sweep2.md`). **Canonical values, as of this line — use these, not the strings quoted above:** step-up **+94.1%** (both conventions; `+95.2%` is retired and appears only inside its own retractions); one-third leg **$871,000** (2,613,000 ÷ 3; `$871,024` is a **retracted back-solve**, allowed only inside a retraction sentence); purchaser composition **$976,408** at band level (`$976,432` superseded as a composition tie, still correct as the raw residual arithmetic 1,272,000 − 295,568, rendered ≈$976,000 ±$1,000); **43% = original S-1** (l.985–988, l.2919) and **41% = S-1/A No. 5** (l.1055–1062, l.3149), a version discrepancy kept visible, never averaged, never an unattributed range | **[WITHDRAWN 2026-09-25 by AUDIT 7 / AUDIT 8: the $871,000 leg and the $976,408 composition rest on an unfiled 2,613,000 denominator that appears in 0 of 93 local filings, and the citation to original-S-1 l.4301–4302 does not carry it. The value is UNKNOWN, not these numbers. See `03_quality_control/audit8_stage1_certification.md` RD-059.]**
| Audit 4 hindsight | FAIL → repaired → **RECHECK FAIL on 2 of 7 conditions.** 19/19 repairs genuinely applied, none faked. Survivors: causal claims still incomplete in the appendices; `context_appendices.md` line ~345 **"Borrowed credibility did the work"** — the same proposition fixed 25 lines earlier, left standing and contradicting `stage_1.md` §H line 515 and §M.9; plus one endpoint-framing leak. Passed: outcome-dependent sentences (7/7), the §H/§D.1 contradiction, the record-selection null, the language sweep (17 hits, all legitimate), the 1994 re-base |
| Audit 5 adversarial | `adversarial_review.md` exists (30 elements: 4 well supported / 18 contested / 8 unsourced folklore). **The verdict pass on the repaired text has not been run** |
| Cloud | Environment `env_00qc1l2f605xdtc6phw8` and agent `agent_00qc1mmg4hg5crb4221c` **created and idle**. Sessions **refused: HTTP 402, no account credit.** Nothing has ever executed remotely — cloud execution is unverified, not proven. See `CLOUD_LAUNCH.md` §8 |

**Deliberately held:** the appendix repair was queued rather than started, because the Audit 3 recheck
was reading `context_appendices.md` — editing under an auditor yields a report about a half-written file.

**Next five actions, in order:**
1. ~~**Close the five defects the AUDIT 3 repair introduced**~~ **DONE 2026-09-24** — they are named in
   `03_quality_control/amazon_s1_audit3_recheck.md`: the +95.2% step-up is corrected to **+94.1%** at
   P17/d6/L30; the missing `quantitative.csv` row was written (line 112) so §R's citation stands;
   `validation.csv` r20's class value was moved out of the `confidence` column and its
   `evidence_class` refreshed; the "$871,024" plug is deleted and restated as the true third,
   **$871,000**, with the composition at **$976,408**; D15 closed. **[WITHDRAWN 2026-09-25 by AUDIT 7 / AUDIT 8: the $871,000 leg and the $976,408 composition rest on an unfiled 2,613,000 denominator that appears in 0 of 93 local filings, and the citation to original-S-1 l.4301–4302 does not carry it. The value is UNKNOWN, not these numbers. See `03_quality_control/audit8_stage1_certification.md` RD-059.]**
2. ~~**Fix the §U.29 attribution**~~ **DONE 2026-09-24** (43% is the original S-1; 41% is S-1/A No. 5) in
   `conflicts.csv` r30 and `stage_1.md` §U.29 — this one was not in any earlier defect list, so it is a
   genuinely new finding. The two residual sweeps then carried the same split to §B.1 (the former
   unattributed "~41–43%"), to `stage_1_claim_records.md` K14, and to `_parts/` markers.
3. Repair the AUDIT 4 survivors **by scanning for siblings, not by working the line list** — the failure
   mode found twice now is that a repair fixes the instance named in a finding and leaves the same claim
   standing nearby. After fixing `context_appendices.md` line ~345, grep the appendices for causal
   constructions and the remaining endpoint-framing leak.
4. Re-verify the failed conditions only (AUDIT 3 checks 1–4; AUDIT 4 conditions 2 and 5), then run
   AUDIT 5 as a verdict pass on the repaired text.
5. Regenerate `_MANIFEST.md` counts, then — and only then — mark Stage 1 `QA → COMPLETE` in
   `MASTER_RESEARCH_LOG.md` and start Stage 2.

**Process lesson worth carrying into the remaining 49:** repair passes introduce errors at a real rate.
Both rechecks this session found defects that did not exist before the repair — one wrote a value into
the wrong CSV column, another invented a precision figure to close a gap, another produced a wrong
percentage. **A repair is a change to the corpus and needs its own verification pass; "the audit's list
is closed" is not evidence that it is correct.**

**Security:** the Qoder PAT was pasted into chat — **rotate it**. It lives only at `~/.qca/pat`
(mode 600, outside the repository) and was never committed or written into any file in the corpus.

## 1. What this project is

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
| Audit 3 numbers | **FAIL → repaired → recheck FAIL (repairs introduced errors) → repaired again, and the two residual register sweeps closed the copies left outside the repair passes' scopes (2026-09-24).** 31 defects, 9 HIGH (`_parts/NUMBER_DEFECTS.md`) — incl. a $355,000 cumulative-losses figure against an audited $248,000 deficit. Canonical values now carried everywhere: step-up **+94.1%**; one-third leg **$871,000**; composition **$976,408** (band-level, residual arithmetic ≈$976,000 ±$1,000); **43% = original S-1 / 41% = S-1/A No. 5** as a visible version discrepancy | **[WITHDRAWN 2026-09-25 by AUDIT 7 / AUDIT 8: the $871,000 leg and the $976,408 composition rest on an unfiled 2,613,000 denominator that appears in 0 of 93 local filings, and the citation to original-S-1 l.4301–4302 does not carry it. The value is UNKNOWN, not these numbers. See `03_quality_control/audit8_stage1_certification.md` RD-059.]**
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
