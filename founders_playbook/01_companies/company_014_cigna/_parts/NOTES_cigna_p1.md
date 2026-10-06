# NOTES — `s1-cigna-p1` (Stage-1 author, `company_014_cigna`), 2026-10-06

## Claim / scope / budget
- Claim run as first tool call: `python tools/scaffold.py claim --path founders_playbook/01_companies/company_014_cigna/_parts/s1_p1.md --agent s1-cigna-p1 --sections "Header,boundary,A..U,registers"` → `CREATED … (owner=s1-cigna-p1 ttl=240 min, sections=4)`.
- Web calls this pass: **0** (§15.1 — everything script-reachable was returned as a FETCH REQUEST instead). Budget: 130 ceiling, closed at ~45 tool calls, section by section, each marked `STATUS: WRITTEN`.
- Tier honored as issued by the probe: **Stage 1 = T2 core, PROVISIONAL** on the lineage frame, with the **T3** strict-registrant reading carried as a *state* (§boundary, §U.4). **No re-tiering attempted.** Note for the fleet: this run's gate tier-reader printed `tier: T2 … (35 mentions, 0 on a verdict line)` — it read T2 tonight where the probe had recorded it printing T3; the reading is now consistent with the issued verdict either way.

## Byte-verification pass — what I confirmed and what moved
Every load-bearing passage was read from the stored file before use. Corrections/additions vs the probe's cited locators (probe remains the measurement of record; these are this-pass locators, cited in the dossier as locators per §14.12):
- DeBlase merger sentence: **l.2484-2487** (probe cited 2486-2487). Caption l.19-30; receipt-stamp line is OCR-garbled `9417 46 APR 19 1995` (l.5).
- 8-K 2018-12-20: "(Exact name…)" prints at **l.36**; former-name block is **two lines, l.77-78**; merger anatomy l.163-166 (probe said l.164-165 — same sentence, different wrap).
- EIN `82-4991898`: grep over the 4 probe-representative SEC files = **1 (s4) + 1 (form8k) + 0 (ex4-1) + 0 (ex4-2)**; the probe's "occurs in 3 stored documents" counts a third file I did not open (likely the 2018-09-21 halfmoon8k set) — left un-adjudicated, recorded here.
- `1792` corpus census re-measured: **exactly 2**, both in `INAC2115_1979_djvu.txt` l.5 + l.371, zero elsewhere across all shelf `.txt`.
- `sources/_index/submissions.csv`: **1,019 lines = 1,018 filings + header**, matching the probe.
- A4 harvest census as re-read tonight: **96 / 12 / 81** (probe had caught 79 / 12 / 65) → §U.5 conflict row written, both readings preserved.
- S-4 1981 recital: `grep -n` = exactly l.4995 + l.23191, same lineage (one recital, printed twice).
- Pierre Rule 29.1: l.6102-6121 chain sentence verified **including the ERISA "claim administrators" Questions Presented at l.6081-6096** (new to this dossier — used for §C/§F).
- Creative Bath: CG named at l.15 caption (probe said l.15/190/203/498 — first occurrence verified).
- CIA rdp88t: `grep -ic cigna` = **1**; the sentence is l.1174-1175 (used for §M/timeline with the adjacency caveat).
- `assessingitperfo00wils`: sponsor-acknowledgment-list reading confirmed from probe; logged as CG10 naming-only.

## New evidence mined this pass (all from the already-held INA 1979 report; none was in the probe)
Full Financial Highlights set (l.80-100, OCR damage on the 1978 column disclosed), segment shares (P&C 66%/L 18%/HC 12%/parent 4% of revenues; a 5% pre-tax loss line), segment pre-tax dollars, **written** premiums $2.78B vs $2.55B, combined ratio 101.8% with INA's own mixed definition, reserves $2.9B and reserves-to-**earned** 96→111%, written-to-surplus 3.0-to-1, goodwill charges, the industry-size sentence (~2,900 firms / est. $90B), the **prepaid-health entry narrative** (1978 California plan, 1979 Arizona plan, two Florida options, INA Healthplan naming, Dallas HQ), HMO International Dec-1978 purchase note with self-assessed immateriality, hospital/SNF/management counts, and the health-care 1969 + life 1957 internal dates. These carry §K, §D, §E, §L, §M, §N, §Q and most register rows.

## Registers (emit-only contract honored; no live CSV written)
78 rows total: **sources 16 · quantitative 15 · timeline 14 · decisions 3 · validation 4 · failures 6 · channels 2 · conflicts 6 · data_gaps 12**. All 9 blocks validated programmatically: header-width identical, zero drift, zero empty cells (non-derived rows carry `n/a (value as printed)`). `source_id`s left dossier-local (CG01-CG16); merge mints globally. Withheld rows: none of the `TIER1_CANDIDATE` label rows, no 1982-as-fact row (it lives in conflicts/timeline as the U.3 hypothesis only).

## What I refused to claim, and why
1. **1792 for the registrant, or "Cigna was founded in 1792"** — only the INA self-report's own words support 1792, of the *subsidiary*, retrospectively; Medium cap; §U.2.
2. **1981 for CIK 0001739940** — recital subject is the 1981 corporation which the 8-K makes a *subsidiary of* the registrant; §U.1.
3. **The registrant's incorporation date** — printed nowhere; NOT 2018-05-16; FR-2.
4. **The 1982 combination as evidence** — carried as unattested hypothesis; §U.3.
5. **1872/1850s for the second ancestor** — UNTRIED, never "no evidence"; the lone 1850 is the ERIC New-Haven sentence (CG13 decoy row).
6. **Two shelves as two documents / five S-4 files as five witnesses** — md5 + lineage rules.
7. **Annuity/securities product substance in DeBlase** — `annuit|variable life|single premium` searched = zero hits in that byte; captions only.
8. **"Cigna" in the CIA 1988 roundup as a self-evident corporate act** — single third-party press-summary hit; Medium-Low.
9. **No competitor, membership, PPO, or registrant-financial fact** — none is in held bytes; named as query-scope silences with routes.

## FETCH REQUEST blocks (nothing fetched by me)
FR-1 … FR-7 inherited verbatim in scope from the probe (predecessor CIK index+auto; registrant's own cert/first 10-K; the 18 capped filings; mine the backlog + facet-free CP; CA endpoint; first CDX pass; ancestor-2 query block). **New: FR-8** (defined in part file §UNTRIED-8) — pre-1979 outside witnesses to the 1792 claim, to settle §U.2's residual.

## What I did NOT examine
- The 26 SEC files beyond the 4 representatives (amendments/exhibits of the CG01 lineage and the other 2018-09/12 + 2019-01 accessions) — byte-identical-lineage boilerplate per the probe; the ex4-3/halfmoon8k pair and `0000950159-18-000533`/`-19-000007` bodies.
- Page interiors of all three SCOTUS records beyond caption/structure/Rule-29.1 ranges (merits, appendices, jurisdictional statements).
- The INA report's full audited-statement pages (l.3400+ only partially read; balance sheets not reconstructed).
- `sources/sec/*.meta.json` sidecars individually; the fleet intake files beyond the probe's quoted lines; every unmined candidate row (81); HathiTrust/GB/CA result pages (bytes never landed).

## Gate
Command (briefed, run 2026-10-06): `python tools/gates.py --company-dir founders_playbook/01_companies/company_014_cigna --tier auto --checks csv,keys,anchors,corrections --out founders_playbook/03_quality_control/cigna_s1_gates_p1.md` → **exit 0**, Findings 1 | Passes 0, the single finding `coverage/registers` ("no register CSVs at root or research/") — the expected pre-merge state, not a defect. Anchors read: explicit ANCHORS set (6 ids) declared in `_parts/s1_p1.md`; "no register anchors — UNANSWERED, not passed" (pre-merge, correct). Corrections: no CORRECTIONS.md → DID NOT RUN (not a pass) — none is owed by this pass; no retraction was made here (the probe's own header regrade stayed inside the probe file).

## Part-file stats (re-measured after last write)
`_parts/s1_p1.md`: **15,707 words**, 0 PENDING / 26 `STATUS: WRITTEN` markers; sections Header, boundary, A–U, UNTRIED, claim records, registers — all written; **25 claim records** (A01…S01); anchors **U.1–U.6** with 1:1 conflicts-row parity; register rows **78** (breakdown above). T2 cap (22k/stage) respected.
