# _MANIFEST — company_001_amazon

**Counts regenerated 2026-09-24** by the Stage-1 closure pass (word = whitespace-delimited tokens,
`wc -w`-equivalent; byte = file size). Previous counts were generated 2026-09-23 and were stale by two
repair rounds and one closure round. Per `00_METHOD_AND_STYLE.md` §9.6 every directory carrying split
files keeps this register so a file can be checked against the ceilings before handoff or upload.

**Which ceiling governs which file.** §9.1's hard upload constraint — **500,000 words / 200 MB per file,
whichever binds first** — governs *every* file, primaries included. §9.2's **60,000-word hard cap** is the
cap on a *stage file and its companion deliverables*; the restored primaries under `sources/` are the
evidence base, not volumes of the document, and are checked against §9.1 only (the largest, the original
S-1 at 213,118 words, is 43% of that ceiling). Nothing in this directory exceeds either ceiling that
applies to it, and no file is at hard cap; **no splitting is required and none was done.**

**Reading order is by section, not by size.** Parts marked *intermediate* are working volumes that were
merged into the deliverables; they are retained as the audit trail of the merge, not as additional content
to read. **Nothing in this directory is a cleanup target** (§14 rule 4): the duplicate retrievals, the
`_parts/` volumes and the harvest-run scratch files in `../../../tools/` (`_dryrun_20260924.txt`,
`_live_run_20260924.log`) are all left exactly where they are.

## Deliverables (read these)

| File | Words | Bytes | Contents | Upload batch | Status |
|---|---|---|---|---|---|
| `stage_1.md` | **49,258** | 320,164 | Header (incl. the filing-lineage ruling, 2026-09-24), stage-boundary justification, §A–§U; **43 canonical conflicts U.1–U.43** | 1 | AT QA — amber band (§9.2: 40–60k allowed to finish as one file); 82% of the 60,000 cap |
| `stage_1_claim_records.md` | **51,632** | 336,161 | Appendix: 432 claim records B–U with `[src: …]` traces, the §T provenance table and the 2026-09-24 closure addendum | 1 | AT QA — 86% of cap; split is **not** yet required, and the trigger is §9.3 geometry (a section boundary), never a trim |
| `context_appendices.md` | 10,882 | 72,450 | Environment appendices A–J | 1 | MERGED — **carries three sites the 2026-09-24 closure could not reach** (see Residual defects, and `03_quality_control/amazon_s1_numeric_closure_final.md` §5) |
| `adversarial_review.md` | 4,611 | 29,565 | 30 origin-story elements: 4 well supported / 18 contested / 8 unsourced folklore | 1 | COMPLETE |
| `CORRECTIONS.md` | 2,777 | 18,355 | Binding provenance corrections COR-01…COR-14 | 1 | LIVING — append, never rewrite history |
| `quantitative.csv` | 7,914 | 60,014 | 111 data rows × 12 cols; `derived_arithmetic` populated on exactly the 30 DERIVED/ESTIMATE/INFERENCE rows | 2 | AT QA — validated 2026-09-24 |
| `conflicts.csv` | 13,102 | 87,680 | 43 data rows × 15 cols, keyed to canonical **U.1–U.43** | 2 | AT QA — U.43 appended 2026-09-24 |
| `validation.csv` | 2,225 | 16,823 | 29 data rows × 11 cols | 2 | AT QA — r9 re-keyed 2026-09-24 |
| `data_gaps.csv` | 2,613 | 18,343 | 23 data rows × 8 cols; every High-importance row carries a follow-up task | 2 | AT QA — r11 rewritten 2026-09-24 |
| `sources.csv` | 14,778 | 116,434 | Global provenance register, blocks S0001–S1899, `independence_note` per row | 2 | UNTOUCHED this pass — **not in the closure agent's write scope**; its S0803 `independence_note` still asserts amendment independence (residual defect) |
| `timeline.csv` | 3,069 | 24,839 | 57 data rows × 11 cols | 2 | STABLE this pass |
| `decisions.csv` | 1,726 | 13,212 | 15 data rows × 15 cols | 2 | STABLE this pass |
| `failures.csv` | 2,555 | 19,308 | 33 data rows × 11 cols | 2 | STABLE this pass |
| `channels.csv` | 1,279 | 9,805 | 15 data rows × 11 cols | 2 | STABLE this pass |

**Upload batch 1** = the readable stage volume. **Batch 2** = structured data. **Batch 3** = evidence and
audit trail. Word totals are counts of tokens, not of evidence: **no file was shortened to meet a number**,
and §9.6 forbids it ("Cutting evidence to fit a file limit is forbidden").

## Intermediate merge volumes (`_parts/`) — retained, read-only to repair passes

| File | Words | Bytes | Contents | Why retained |
|---|---|---|---|---|
| `s1_p1.md` | 4,278 | 27,599 | header, boundary, §A–D | Shows what the merge accepted, moved or corrected; carries an appended `SUPERSEDED 2026-09-24` footer at l.52/70 |
| `s1_p2.md` | 4,825 | 30,720 | §E–J | ditto; independently caught the accession error; l.78 is the mirror of the appendix credibility claim (RD-038, OPEN) |
| `s1_p3.md` | 3,403 | 22,461 | §K–O | ditto; `SUPERSEDED` footer, l.24 |
| `s1_p3b_H_addendum.md` | 1,515 | 10,102 | six splice blocks from the late legal dossier, `⟨covered⟩` dedup markers | records what was deliberately not double-printed |
| `s1_p4.md` | 10,536 | 68,573 | §P–U | ditto; `SUPERSEDED` footer, ll.46/98/176/203 |
| `s1_claims_AJ.md` | 26,235 | 168,855 | claim records B–J (288 records, 381 traces) | source of the appendix; also holds the coverage note disclosing deferrals |
| `s1_claims_KU.md` | 19,420 | 128,176 | claim records K–U (144 records) | ditto; **ll.37 and 153 still hold the pre-merge K14/P09 forms** (residual defect; footer marker is the route) |
| `U_CONCORDANCE.md` | 5,143 | 32,280 | **canonical conflict mapping U.1–U.42**, adjudicating three independent registers | the only authority for `Conflicts: U.n` references — **does not yet list U.43**, appended 2026-09-24 by the append-only rule (residual defect) |
| `NUMBER_DEFECTS.md` | 3,348 | 21,505 | the numbers defect register, rounds 1–2 | row 43 is where the false `+95.2%` was imported from; round-2 footer records propagation |

## Specialist dossiers (`research/`) — the archival evidence layer

| File | Words | Bytes | Records | Scope |
|---|---|---|---|---|
| `A_corporate_historian.md` | 15,757 | 108,924 | 98 | founding chronology, incorporations, domains, launches |
| `B_founder_forensics.md` | 25,122 | 160,726 | 133 | founder state, household, network, capital access |
| `C_market_environment.md` | 13,814 | 95,850 | 75 | 1990–95 web and book market, growth-statistic provenance |
| `D_customers_distribution.md` | 14,845 | 102,611 | 82 | first customers, channels, trust |
| `E_supply_ops_finance.md` | 22,090 | 141,180 | 94+ | supply, fulfilment, Stage-1 money; `SUPERSEDED` footer ll.25/75/261/324 |
| `F_technology.md` | 18,352 | 123,402 | 88 | original system, recollection vs documented |
| `G_adversarial.md` | 9,297 | 64,566 | 38 challenges | origin-story attack surface |
| `H_legal_organization.md` | 15,061 | 104,113 | 61 | legal, IP, trademark, tax posture, people register |
| `I_environment_context.md` | 12,147 | 82,313 | 64 | macro, household tech, catalog precedent, press climate |
| `J_archive_artifacts.md` | 9,575 | 63,230 | 46 | in-window product artifacts, CDX null results |
| `K_roadmap_provenance.md` | 8,488 | 54,453 | 36 | the 1994 planning document's evidence ladder |
| `ST2_A_chronology_org.md` | 16,056 | 115,128 | — | **Stage-2** dossier — present in this directory, not Stage-1 evidence, listed for completeness |
| `ST2_B_finance.md` | 13,385 | 86,316 | — | Stage-2 dossier |
| `ST2_D_tech_ops.md` | 1,442 | 11,250 | — | Stage-2 dossier (partial) |
| `ST2_E_adversarial.md` | 14,679 | 102,716 | — | Stage-2 dossier |
| `_EVIDENCE_CACHE.md` | 5,838 | 40,557 | — | document inventory, tiers, documented nulls, deletion incident |
| `cdx_prefix96.txt` | 11 | 160 | — | the HTTP-504 page proving the prefix CDX queries **failed** rather than returned a null (COR-05) |

Total dossier text **215,959 words / 1,457,495 B** across seventeen files, every one far under the §9.1
ceiling. The Stage-1 appendix draws ~430 records from the eleven Stage-1 dossiers; the remainder stay
addressable by their own IDs (`A-61`, `E-71`, `G-15` …), which is why the appendix carries `[src: …]`
traces. **Dossier word counts exceed any single-file *target* by design:** they are many separate sources.

## Primary evidence (`sources/`) — protected archive, read-only to every pass

| File | Words | Bytes | Document |
|---|---|---|---|
| `S-1_original_acc-0000891618-97-001309_filed-1997-03-24.txt` | 213,118 | 1,445,709 | **Form S-1 (original)** — the founding-instrument facts exist only here (COR-01, COR-02) |
| `s1_original_0000891618-97-001309.txt` | 212,929 | 1,444,013 | duplicate retrieval of the same filing (pre- and post-deletion agents); retained, not deleted, flagged for a future dedupe pass |
| `S-1A-No5_acc-0000891020-97-000839_filed-1997-05-14.txt` | 39,728 | 303,069 | S-1/A No. 5 — the accession several briefs mislabelled "the S-1" |
| `s1_0000891020-97-000839.txt` | 39,576 | 301,685 | duplicate retrieval of No. 5 |
| `S-1A-No3_acc-0000891020-97-000755_filed-1997-05-09.txt` | 39,743 | 306,425 | S-1/A No. 3 |
| `424B1_final-prospectus_acc-0000891020-97-000868_filed-1997-05-15.txt` | 35,054 | 266,755 | **final prospectus (S-1/A No. 6) — NEW ON DISK 2026-09-24, 17:00 local, i.e. during this closure pass.** `stage_1.md` §T still reads `restoration pending` for it (RD-027): a closure agent may not read a primary into the corpus it is closing, so **nothing in the deliverables cites it and no claim was re-derived from it.** Handing it to the retrieval owner, which can now settle RD-027 and test COR-14.1's P60/P61 citation item |
| `10-K_FY1997_acc-0000891020-98-000448_filed-1998-03-30.txt` | 85,504 | 607,959 | FY1997 annual report, form **10-K405** (cite the form as filed) |
| `sheff-playboy-interview_davidsheff-com-jeff-bezos.txt` / `.html` | 9,051 / 10,917 | 52,098 / 133,811 | **1999 interview, published 2000** — retrospective, never contemporaneous (COR-06) |
| `historylink-essay-23230_Amazon-The-Early-Years-1995-1999.txt` / `.html` | 3,442 / 6,276 | 21,399 / 54,616 | 2025-04-07 secondary essay, Tier 2 at best (COR-11.3) |
| `ncsa-mosaic-whats-new_1995-08_kitchencloset.html` | 99,268 | 985,639 | NCSA Mosaic "What's New", August 1995 — 3,084 entries; **its only "Amazon" is the river** (COR-08) |
| `NULL_RESULT_wayback_1995_1996.md` | 634 | 4,427 | **null result:** no in-window archived amazon.com page, plus the four 504 time-outs that are *not* nulls |
| `edgar_s1_index.json`, `idx.html`, `idx.json` | 11 / 582 / 582 | 616 / 4,819 / 4,819 | EDGAR index captures behind COR-04's document-count proof |
| `s1_graphics/` (18 files) | 60,596 total | 652,829 total | **the graphics inventory and its working files** — `INVENTORY.md` (1,884 w / 11,690 B) is the COR-04 null: 0 images exist, the caption was a printer's art instruction; the largest member is `hdr_000089102097000659.txt` (54,066 w / 403,334 B), an EDGAR directory header, retained because COR-04's document-count arithmetic is checkable only from these files |

**Ceiling check (§9.1).** Largest single file = 213,118 words (42.6% of 500,000) and 1.45 MB (0.7% of
200 MB). No splitting needed anywhere. `sources/` holds **857,011 words / 6,590,688 B (6.29 MB)** across its
own 17 files plus the 18 in `s1_graphics/`.

**Duplicate retrievals are disclosed, not hidden.** Five `sources/` files are second copies or near-copies
of a filing already on disk, because the evidence base was rebuilt after an agent deleted the originals
(COR-08). Dedupe requires byte-level confirmation that the pairs match; until then both copies are listed
so no citation can point at a file whose existence is uncertain. **The duplicates are not a tidy-up
opportunity** (§14 rule 4).

## Aggregate

| Measure | Value (2026-09-24) |
|---|---|
| Root deliverables (14 files, excluding this manifest) | **169,275 words / 1,148,589 B** |
| — of which the stage file + claim appendix (batch 1 readable text) | **100,890 words** — both under §9.2's 60,000-word cap individually (49,258 / 51,632) |
| `_parts/` intermediate volumes (9 files) | 78,703 words / 510,271 B |
| `research/` dossiers (17 files) | 215,959 words / 1,457,495 B |
| `sources/` primaries and working captures (17 + 18 files) | 857,011 words / 6,590,688 B |
| Directory total, this manifest included | **≈1,623,600 words / 9.7 MB** |
| Files at or over §9.2's 60,000-word cap | **0** |
| Files at 80–90% of the cap (split-watch list) | `stage_1_claim_records.md` 86%, `stage_1.md` 82% — split at a section boundary per §9.3 *if* a later pass pushes either past 60,000; never by trimming |

## Housekeeping

- `_scratch/` no longer exists — destroyed mid-run by an agent's cleanup on 2026-09-23 (see
  `_EVIDENCE_CACHE.md` §deletion incident and `CORRECTIONS.md` COR-08). Restored copies live in `sources/`.
- `sources/` is **read-only for retrieval agents** and is never a cleanup target (§14 rule 4).
- `../../../tools/_dryrun_20260924.txt` (9,606 B) and `../../../tools/_live_run_20260924.log` (4,611 B) are
  left exactly where they are. They are the periodical-harvester's run records from 2026-09-24, not this
  company's scratch, and on a multi-agent run "scratch" is usually somebody else's primary source.
- Line endings: the nine CSVs are **LF-only, UTF-8, no BOM, trailing newline present**. `stage_1.md`,
  `stage_1_claim_records.md`, `conflicts.csv`, `quantitative.csv` and `validation.csv` were rewritten by the
  2026-09-24 numeric-closure round and are now LF where `residual_sweep2` had recorded `stage_1.md` as
  CRLF; the conversion is geometry only — no content changed, and it is recorded here rather than silently
  repaired.
- Regenerate this manifest's counts after every merge or repair pass.
