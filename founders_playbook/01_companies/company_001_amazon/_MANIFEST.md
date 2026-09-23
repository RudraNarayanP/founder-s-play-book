# _MANIFEST — company_001_amazon

Generated 2026-09-23. Per `00_METHOD_AND_STYLE.md` §9.6, every directory carrying split files keeps
this register so a file can be checked against the per-source ceiling (**500,000 words / 200 MB,
whichever binds first**) before it is handed off or uploaded. No file here is within two orders of
magnitude of the byte ceiling, and the largest is at 43% of the word ceiling.

**Reading order is by section, not by size.** Parts marked *intermediate* are working volumes that
were merged into the deliverables; they are retained as the audit trail of the merge, not as
additional content to read.

## Deliverables (read these)

| File | Words | Bytes | Contents | Upload batch | Status |
|---|---|---|---|---|---|
| `stage_1.md` | 37,730 | 246,567 | Header, stage-boundary justification, §A–§U (42 canonical conflicts) | 1 | MERGED, pending audits |
| `stage_1_claim_records.md` | ~45,500 | — | Appendix: claim records B–U with `[src: …]` traces | 1 | being written |
| `context_appendices.md` | 8,527 | 56,078 | Environment appendices A–J (macro, household tech, catalog precedent, book trade, payments, technology, institutional, press, quantitative, gaps) | 1 | MERGED, pending audits |
| `adversarial_review.md` | 4,611 | 29,565 | 30 origin-story elements: 4 well supported / 18 contested / 8 unsourced folklore | 1 | COMPLETE |
| `CORRECTIONS.md` | 2,197 | 14,643 | Binding provenance corrections COR-01…COR-11 | 1 | LIVING — append, never rewrite history |
| `quantitative.csv` | — | — | Stage-1 metrics, basis-labelled, `derived_arithmetic` mandatory on DERIVED rows | 2 | being written |
| `timeline.csv` | — | — | Micro-timeline rows | 2 | being written |
| `decisions.csv` | — | — | Founder decision forensics | 2 | being written |
| `validation.csv` / `failures.csv` | — | — | Validation signals; negative signals and failures | 2 | being written |
| `channels.csv` | — | — | Distribution channels tested, with repeatability | 2 | being written |
| `data_gaps.csv` | — | — | Gap register; High-importance rows carry an RD id | 2 | being written |
| `sources.csv` | — | — | Global provenance register, blocks S0001–S1899, `independence_note` per row | 2 | being written |
| `conflicts.csv` | — | — | Conflict register keyed to canonical U.1–U.42 | 2 | being written |

**Upload batch 1** = the readable stage volume (~92k words across two files, both far under the
ceiling, no splitting required). **Batch 2** = structured data. **Batch 3** = evidence and audit trail.

## Intermediate merge volumes (`_parts/`)

| File | Words | Contents | Why retained |
|---|---|---|---|
| `s1_p1.md` | 4,129 | header, boundary, §A–D | Shows what the merge accepted, moved or corrected |
| `s1_p2.md` | 4,825 | §E–J | ditto; independently caught the accession error |
| `s1_p3.md` | 3,286 | §K–O | ditto |
| `s1_p3b_H_addendum.md` | 1,515 | six splice blocks from the late legal dossier, `⟨covered⟩` dedup markers | records what was deliberately not double-printed |
| `s1_p4.md` | 10,337 | §P–U | ditto |
| `s1_claims_AJ.md` | 26,235 | claim records B–J (288 records, 381 traces) | source of the appendix; also holds the coverage note disclosing deferrals |
| `s1_claims_KU.md` | 19,330 | claim records K–U (144 records) | ditto |
| `U_CONCORDANCE.md` | 5,103 | **canonical conflict mapping, U.1–U.42**, adjudicating three independent registers | the only authority for `Conflicts: U.n` references |

## Specialist dossiers (`research/`) — the archival evidence layer

| File | Words | Records | Scope |
|---|---|---|---|
| `A_corporate_historian.md` | 15,757 | 98 | founding chronology, incorporations, domains, launches |
| `B_founder_forensics.md` | 25,122 | 133 | founder state, household, network, capital access |
| `C_market_environment.md` | 13,814 | 75 | 1990–95 web and book market, growth-statistic provenance |
| `D_customers_distribution.md` | 14,845 | 82 | first customers, channels, trust |
| `E_supply_ops_finance.md` | 21,851 | 94+ | supply, fulfilment, Stage-1 money |
| `F_technology.md` | 18,352 | 88 | original system, recollection vs documented |
| `G_adversarial.md` | 9,297 | 38 challenges | origin-story attack surface |
| `H_legal_organization.md` | 15,061 | 61 | legal, IP, trademark, tax posture, people register |
| `I_environment_context.md` | 12,147 | 64 | macro, household tech, catalog precedent, press climate |
| `J_archive_artifacts.md` | 9,575 | 46 | in-window product artifacts, CDX null results |
| `K_roadmap_provenance.md` | 8,488 | 36 | the 1994 planning document's evidence ladder |
| `_EVIDENCE_CACHE.md` | 5,838 | — | document inventory, tiers, documented nulls, deletion incident |

Total dossier text ≈ **150,000 words / 994 KB**. The appendix draws ~430 records from these; the
remainder stay addressable by their own IDs (`A-61`, `E-71`, `G-15` …), which is why the appendix
carries `[src: …]` traces. **Dossier word counts exceed any single-file target by design:** they are
eleven separate sources, each far under the ceiling.

## Primary evidence (`sources/`)

| File | Words | Bytes | Document |
|---|---|---|---|
| `S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` | 213,118 | 1,445,709 | **Form S-1 (original)** — the founding-instrument facts exist only here |
| `s1_original_0000891618-97-001309.txt` | 212,929 | 1,444,013 | duplicate retrieval of the same filing (pre- and post-deletion agents); retained rather than deleted, flagged for a future dedupe pass |
| `S-1A-No5_acc-0000891020-97-000839_filed-1997-05-14.txt` | 39,728 | 303,069 | S-1/A No. 5 — the accession several briefs mislabelled "the S-1" |
| `s1_0000891020-97-000839.txt` | 39,576 | 301,685 | duplicate retrieval of No. 5 |
| `S-1A-No3_acc-0000891020-97-000755_filed-1997-05-09.txt` | 39,743 | 306,425 | S-1/A No. 3 |
| `10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` | 85,504 | 607,959 | FY1997 annual report (form 10-K405) |
| `sheff-playboy-interview_davidsheff-com-jeff-bezos.txt` | 9,051 | 52,098 | **1999 interview, published 2000** — retrospective, never contemporaneous |
| `historylink-essay-23230_Amazon-The-Early-Years-1995-1999.txt` | 3,442 | 21,399 | 2025-04-07 secondary essay |
| `mosaic-whats-new_aug-1995.html` | — | 985,639 | NCSA Mosaic archive, August 1995 — its only "Amazon" is the river |
| `s1_graphics/INVENTORY.md` | — | 4,427 | **null result:** 0 images; the caption was a printer's art instruction |
| `NULL_RESULT_wayback_1995_1996.md` | — | — | **null result:** no in-window archived amazon.com page |

**Ceiling check.** Largest single file = 213,118 words (43% of the 500,000-word limit) and 1.45 MB
(0.7% of 200 MB). No splitting needed anywhere, and none will be needed at this density: a whole
company stage-plus-appendix is ~92k words.

**Duplicate retrievals are disclosed, not hidden.** Four `sources/` files are second copies of the same
filing, because the evidence base was rebuilt after an agent deleted the originals. Dedupe requires
byte-level confirmation that the pairs match; until then both copies are listed so no citation can
point at a file whose existence is uncertain.

## Aggregate

| Measure | Value |
|---|---|
| Repository total, all text | **1,016,961 words** |
| Company 001 deliverables (root `.md`) | 53,065 words written so far, ~92,000 with appendix |
| Specialist dossiers | ~150,000 words, 738+ claim records |
| Primary filings held locally | ~630,000 words / 3.9 MB |
| Projected full run (50 companies × 3 stages at exemplar density) | 1.5–2.5M words ⇒ **≥4 upload sources**; at current Amazon density more like 150–200 files |

## Housekeeping

- `_scratch/` no longer exists — destroyed mid-run by an agent's cleanup on 2026-09-23 (see
  `_EVIDENCE_CACHE.md` §deletion incident and `CORRECTIONS.md` COR-08). Restored copies live here.
- `sources/` is **read-only for retrieval agents** and is never a cleanup target (§14 rule 4).
- Regenerate this manifest's counts after every merge or repair pass.
