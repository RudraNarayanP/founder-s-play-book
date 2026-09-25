# THE FOUNDER'S PLAYBOOK — Method, Style, and File-Splitting Rules

Governing document for every file in this repository. Level-2 Company Leads and Level-3
specialists produce work against these rules; the Master Orchestrator audits against them.

---

## 1. What the product is

A forensic longitudinal dataset reconstructing what each company in the frozen universe
(`00_universe/`) actually looked like while its outcome was still unknown: origin → first
real-world experiment → repeatable validation → scalable company formation.

It is not biography, not inspiration, and not a leaderboard. No scores, no rankings, no
"winner" judgments (spec §21). Where the record is thin, the dataset says UNKNOWN.

## 2. Hindsight firewall

The eventual success of a company is never evidence that an early decision was rational,
that investors were obviously wrong, that the market was obviously huge, or that any
strategy was inevitable. Every stage boundary must be defensible from evidence existing
at that time. Anti-hagiography test before finalizing any section: *would this still read
as plausible if the company had failed five years later?* If not, it contains hindsight
contamination and must be rewritten.

**Record-selection null (added from AUDIT 4, RD-032).** Hindsight contamination is not only
linguistic — it is also in *which* facts survive into the report. Every stage file must state, in §A
and §S, what evidence about the period is now unrecoverable *because the winners' archive is the one
that was kept*: internal deliberations, rejected options, contemporaneous failures nobody printed, and
the absence of any independent count behind a company self-report. Without that null, a well-sourced
reconstruction of a survivor still reads as a story about a future winner.

## 3. Claim classification (every material statement carries one)

| Class | Meaning |
|---|---|
| FACT | Directly supported by retrieved public evidence |
| FOUNDER CLAIM | A founder stated it; classify further as *contemporaneous* vs *retrospective memory* |
| CONTEMPORARY OBSERVATION | From people/media/documents existing near the event |
| RETROSPECTIVE INTERPRETATION | A later explanation of what supposedly happened |
| INFERENCE | Reasoned conclusion from multiple pieces of evidence |
| ESTIMATE / DERIVED | Calculated value; the arithmetic must be shown |
| UNKNOWN | Reliable evidence could not be established |

Confidence: **High** (2+ independent sources or primary document), **Medium** (one reliable
source, or approximate date corroborated later), **Low** (conflicting, vague, or
retrospective-only), **UNKNOWN** (no evidence recovered).

Independence rule: repeated copying of one origin story is **one** source, not many.

**Filing-lineage rule (from AUDIT 5 on Amazon Stage 1).** Documents inside the same registration
lineage — an S-1 and its amendments, a prospectus and the filing that superseded it, or exhibits to
the same accession — are **one source**, however many files they are. Two agents counted a figure as
"corroborated in the original S-1 and in S-1/A No. 5" when the second is the same instrument
refiled. The same holds for a company's own reprinted history pages and its filings when both trace
to the same corporate record. Corroboration means an **independent origin**: an SEC accession, an
auditor's report, a contemporaneous newspaper that did not use the filing, a court record, an
unrelated third party's data. Where only the lineage exists, confidence is capped at what a single
document supports and `independence_note` says `same lineage as S00xx`.

## 4. Legal / access boundary

Public information only: filings, court and corporate registry records, patents, archived
websites, legitimate databases, public interviews and technical material, books/articles
accessed legitimately. Hard prohibitions: no hacked material, no confidential corporate
documents, no private communications, no protected personal records, no unauthorized leaks.
Difficult-but-public material is labeled **DEEP PUBLIC-SOURCE EVIDENCE**, never "confidential".
Early customers and employees are described only with publicly published information;
no unnecessary private personal data.

## 5. Source tiers

- **Tier 1** — SEC and other regulatory filings, annual reports, incorporation and court
  records, patents, archived company pages, original interviews and transcripts, original
  blogs/decks, contemporaneous statistics.
- **Tier 2** — investigative journalism, major newspapers, serious business publications,
  reported books, academic research.
- **Tier 3** — industry/trade publications, reputable historical databases.
- **Tier 4** — blogs, aggregators, forums, social posts, unsourced summaries. **Leads only:**
  a Tier-4 hit must be chased to the source it rests on, or recorded as untraceable.

Current-state artifacts are not evidence of early state. Today's website says nothing about
the 1995 product; the archived snapshot does.

## 6. Time audit

No statement may import later knowledge into an earlier period. Where a later source is
needed to explain an earlier event it is tagged `RETROSPECTIVE SOURCE`. Numerals carry their
basis: revenue vs GMV vs bookings, nominal vs inflation-adjusted, fiscal vs calendar,
company vs segment, users vs customers, monthly vs annual.

## 7. Required section set, per stage file

Mirrors the reference exemplar exactly. Narrative sections A–U, then the claim-record appendix.

```
Header block:   dataset title, company, stage number, stage date span, stage definition,
                hindsight-firewall statement, confidence scale
A  Executive state summary          B  Founder / company state          C  Original problem
D  First experiment                 E  Product reconstruction           F  Customer
G  Supply / host side               H  Market (as knowable in-period)   I  Competition
J  Technology                       K  Money / personal finances        L  Validation signals
M  Negative signals / failures      N  Founder decisions                O  Counterfactual opportunities
P  Quantitative metrics table       Q  Chronological micro-timeline     R  End-of-stage structured snapshot
S  Data gaps                        T  Source / provenance table        U  Conflicting evidence
—  Claim records appendix (A...U — one record per claim)
```

Not every section applies to every business model. Adapt, never delete: a section that does
not fit the model is answered with the adapted equivalent plus a note on why the standard
frame did not apply (spec §19: SaaS→pilots/ARR/churn; hardware→prototypes/component
sourcing/yield; retail→stores/supply chain/same-store sales; industrial→contracts/capex/
certification; financial→licensing/underwriting/capital/trust; marketplace→supply/demand/
liquidity/trust; consumer technology→adoption/retention/platform dependence).

### Line formats (fixed)

Claim record:
```
B01 Claim: <one sentence> — Date: <event date> — Source: <title, publication> — Source date:
<YYYY-MM-DD or UNKNOWN> — URL: <retrieved URL> — Archived: <— or wayback> — Tier: <1-4> —
Class: <FACT|FOUNDER CLAIM|...> — Passage: "<verbatim ≤40 words>" or NO_VERBATIM_PASSAGE_RECORDED —
Conf: <High|Medium|Low|UNKNOWN> — Corroboration: <n independent> — Conflicts: <None | U.x>
```
Quantitative table: `| ID | Date | Metric | Value | Unit | Source | Source date | Confidence |`
Provenance: `| Source | Type | Primary/Secondary | Event date | Publication date | URL | Tier | Confidence |`
Conflicting evidence: `CLAIM A / CLAIM B / WHY THEY DIFFER / EVIDENCE WEIGHT / BEST-SUPPORTED
INTERPRETATION / RESIDUAL UNCERTAINTY / CONFIDENCE`
Decisions: `| Date | Decision | State before | Information available | Unknowns | Alternatives |
Constraints | Rationale | Expected result | Actual result | Evidence | Confidence |`
Validation: `| Date | Signal | Magnitude | What it demonstrated | What it did NOT demonstrate |
Source | Confidence |`
Knowability, per stage: `KNOWABLE` / `NOT KNOWABLE` / `UNKNOWN`.

**Interpretive codas carry the same duty as tables (added from AUDIT 4, RD-034).** Any "so what",
assessment, or takeaways paragraph — including the environment appendices' per-block codas, which are
prose rather than tables — must satisfy §16 whenever it asserts a consequence: *evidence, mechanism,
alternative explanation, confidence*. Tables were audited for this from the start; five of Amazon
Stage 1's seven causal failures lived in codas the template had left unpoliced. A coda that cannot
name a mechanism says "mechanism UNKNOWN" instead of implying one.

## 8. Table discipline

Tables use the literal 4-column form `| Variable | Value | Source | Confidence |`. Never a
value without its source cell and confidence cell. Never a derived number labeled as if
observed. `UNKNOWN` is a complete, acceptable value.

---

## 9. File-splitting rules — hard upload constraint

**Each individual source file, however produced, must stay within 500,000 words and 200 MB —
whichever limit binds first. No exceptions. Exceeding it does not truncate; it starts a new file.**

Full projected dataset (50 companies × 3 stages at reference density) runs to roughly
1.5–2.5 million words, so it cannot and must not live in one document. Splitting is by
structure, not by word count, so that each file remains independently readable and
independently citable.

### 9.1 Unit of division

1. **Primary unit: one file per company per stage** — `stage_1.md`, `stage_2.md`, `stage_3.md`.
2. Supporting data lives in CSV, never inside prose files.
3. Claim-record appendix may move to its own file (9.3).
4. Environmental context appendices (macro/market/competitor-state/infrastructure/press)
   live in a separate `context_appendices.md` when they exceed ~6,000 words.

### 9.2 Soft target and hard cap

- Soft target: **≤ 40,000 words** per stage file.
- Amber: 40,000–60,000 words — allowed to finish the stage as one file.
- Hard cap: **60,000 words** per file. At the cap, split (9.3). At hard cap the file is
  still only ~0.5 MB of text, far below the 200 MB ceiling; the word limit is the binding
  one, which is why part-splitting is planned at file level rather than waiting for size.

### 9.3 Splitting procedure (when a file hits the hard cap)

Split **only at a section boundary** — never mid-table, never mid-claim-record block:
```
stage_1_part_1.md     sections Header, A–H
stage_1_part_2.md     sections I–P
stage_1_part_3.md     sections Q–U
stage_1_claim_records.md          appendix A…U
stage_1_index.md                  ordered part list + word counts + which sections live where
```
Cross-references use the form `(Amazon S1 §D.1, part_1)` so pointers survive splitting.
Numbering (A–U, claim IDs, metric IDs) **continues across parts**; parts are volumes of one
document, not separate documents. Never renumber to make a part look self-contained.

### 9.4 CSV division

- `quantitative.csv`, `timeline.csv`, `decisions.csv`, `conflicts.csv`, `sources.csv`
  per company, one row per record, header row repeated in every continuation file.
- Split a CSV at **150,000 rows or 40 MB**, whichever first, into
  `quantitative_part_2.csv` etc. Never split a multi-line field across files.
- `sources.csv` is global-append-only per company: reuse source IDs, never re-define one.

### 9.5 Cross-company and QC division

`02_cross_company/` splits by mechanism family (founder / product / distribution / financing /
scaling / failure) rather than growing one mega-file. `03_quality_control/` splits per audit
type plus per-company audit sheets when a single audit file exceeds 40,000 words.
`MASTER_REPORT.md` is an index plus synthesis only — it never absorbs company detail, so it
cannot become the file that breaks the cap.

### 9.6 Manifest requirement (upload safety)

Every directory containing split files carries `_MANIFEST.md`:

```
| File | Words | Bytes | Sections contained | Upload batch | Status |
```

`Upload batch` assigns each file to a numbered upload group (10 companies per group).
Before any handoff or upload, regenerate word counts. Any file above the hard cap is a
**defect**: split it, do not trim content to fit. Cutting evidence to fit a file limit is
forbidden — the limit governs file geometry, never research depth.

### 9.7 Word-count check

```
wc -w <file>            # single file
find . -name '*.md' -o -name '*.csv' | xargs wc -w | sort -n | tail   # whole repo, spot the oversize files
```

---

## 10. Research-debt triggers — dig deeper automatically

Continue investigating (spawn another task) whenever: a major claim rests on one weak
source; a famous anecdote lacks primary evidence; a financial figure looks inconsistent;
founders' accounts conflict; a stage boundary is arbitrary; the first customer is unknown;
product history is vague; funding history is incomplete; a competitor seems missing; a
metric repeats across many sites but traces to one unsourced origin; a popular narrative
conflicts with contemporary evidence. Each trigger is logged as **RESEARCH DEBT** and
assigned a follow-up investigation, not papered over with a disclaimer.

## 11. Completion gate for a company

A company is NOT complete until all three stages have defensible boundaries; founder state,
first experiment, product evolution, customers, competition, distribution, financial
evidence, financing, organization, technology, legal/regulatory, validation signals,
failures, founder decisions, contradictions, data gaps, quantitative dataset and chronology
are reconstructed; hindsight audit passes; adversarial review is done; provenance is closed.
Five independent audits precede output: **chronology, sources, numbers, hindsight, adversarial**.
A failed audit means research again.

## 12. Status vocabulary (research log)

`NOT STARTED` · `DISCOVERY` · `DEEP RESEARCH` · `RECONSTRUCTION` · `ADVERSARIAL REVIEW` ·
`QA` · `COMPLETE`

## 13. Structured dataset schemas (one file per deliverable, per company)

All files: UTF-8, header row always present, `\n` line endings, any field containing a comma,
quote, or newline is double-quoted with `"` escaped as `""`. Literal `UNKNOWN` is a valid
value; an empty cell is a defect. Dates are ISO (`1995-07-01`); partial dates use
`1995-07` or `1995` and carry the confidence that matches. Split per method §9.4 at 150,000
rows or 40 MB, repeating the header in every continuation file. `claim_ref` points at the
claim-record ID in the stage file's appendix; `source_id` points at `sources.csv` and is
never redefined.

**`sources.csv`** — append-only master provenance register
```
source_id,stage,claim_supported,source_title,author_or_publication,source_type,
primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,
evidence_class,confidence,independence_note,relevant_passage,notes
```
`independence_note` records whether a source traces back to another source already in the
register (`derivative of S0042`) — this is what stops copied folklore being counted twice.

**`quantitative.csv`** (spec §V)
```
company,stage,date,metric,value,unit,source,source_date,evidence_class,confidence,
derived_arithmetic,notes
```
`derived_arithmetic` is mandatory whenever `evidence_class` is `ESTIMATE`/`DERIVED`
(e.g. `3 guests x $80 = $240`), empty otherwise.

**`timeline.csv`** (spec §W)
```
company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,
conflict_ref,notes
```

**`decisions.csv`** (spec §S)
```
company,stage,date,decision,state_before,information_available,unknowns,alternatives,
constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref
```
`actual_result` may reference post-stage outcomes only when labeled `RETROSPECTIVE`.

**`validation.csv`** (spec §Q) and **`failures.csv`** (spec §R)
```
company,stage,date,signal_or_failure,magnitude,what_it_demonstrated,
what_it_did_not_demonstrate,source_id,evidence_class,confidence,notes
```

**`channels.csv`** (spec §I)
```
company,stage,channel,date_tested,why_tested,cost_or_effort,result,repeatability,
source_id,confidence,notes
```

**`conflicts.csv`** (spec §X)
```
company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,
claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,
residual_uncertainty,confidence
```

**`data_gaps.csv`** (spec §Y)
```
company,stage,gap,why_missing,importance,best_available_evidence,confidence,follow_up_task
```
`follow_up_task` is mandatory where importance is High — a High-importance gap with no
assigned follow-up is an open research-debt violation, not a finished section.

**Per-company file set:** `stage_1.md` (+ parts), `stage_2.md`, `stage_3.md`, `final_report.md`,
`adversarial_review.md`, `context_appendices.md`, the seven CSVs above, `_MANIFEST.md`.

## 14. Retrieval discipline (learned from wave-1 failures)

Two of eight wave-1 agents exhausted their budget on retrieval and ended having written
nothing — the dataset's most expensive failure mode, because the evidence was gathered and then
lost. Three standing rules:

1. **Write the skeleton first — enforced as the first two tool calls.** A specialist's first act is
   creating its dossier file with the full section structure, and its **second** act is writing at
   least 10 claim records to disk. Only then may it search further, and it must append after every
   source rather than accumulating. Phrasing this as advice did not work: the failure recurred four
   times across two sessions, each costing the whole retrieval pass. Four web requests max for
   mining-only re-runs against local primaries.
2. **Hard web budget.** Max 8 WebSearch + 8 WebFetch per specialist. Past that, the marginal
   source is worth less than the unwritten one. Time-boxed agents must spend the remainder
   writing.
3. **Evidence cache before retrieval.** Each company carries `research/_EVIDENCE_CACHE.md`
   listing documents already downloaded, their tier, and which claims they can settle. Check it
   before fetching; append to it after fetching. Never let a retrieved document live only in a
   scratch directory where the next agent cannot find it.
4. **Nothing is a cleanup target.** An agent may create, modify or delete **only** the files
   named in its own brief. Shared working evidence lives in `company_<id>/sources/` — a protected
   archive, read-only to retrieval agents. Agents must never empty, prune, "tidy", or recursively
   delete any directory they were not assigned, even one they created themselves, and even when it
   looks like their own scratch: on a multi-agent run, "scratch" is usually somebody else's primary
   source. A wave-1 agent destroyed the entire downloaded evidence base of ten siblings by cleaning
   up after itself; the recovery cost is in that company's evidence cache.
5. **Never report a write as complete without naming the file.** A specialist's final summary must
   state the output path and the record count actually on disk, verified by reading it back. Three
   wave-1 agents described finished research and had written nothing.
6. **A depth verdict requires four corpus families, not two.** Established by comparing Amazon, Walmart
   and Apple: **EDGAR reaches essentially nothing before ~1994 and web archives nothing before the
   mid-1990s** — but digitised **periodicals** (Internet Archive magazine collections, HathiTrust,
   Google Books, trade-journal and local-newspaper back files) carry 1950s–1980s contemporaneous text,
   which is Tier-1 evidence for precisely the period those two families miss. A probe may not conclude
   forensic-core or lean until it has searched all four: **filings, web archives, periodical corpora, and
   auction or museum documentary sale records.** Walmart was judged on two families; Apple, searched with
   periodicals, came back exemplar-capable with 20+ in-window Tier-1 records and surviving founding
   documents at auction. Report which families returned nothing **and which were never tried** — a null
   from one family is not a null, and an untried family is not a null either.

7. **One path, one owner — check for live writers before dispatching.** Before any wave is launched or
   relaunched, the orchestrator enumerates still-running agents (a stopped-looking session may merely be
   detached) and gives each write target to exactly one of them. After a machine interruption the
   temptation is to re-issue an identical brief; re-issuing it while the original is alive puts two
   writers on one file.
   **Failure observed.** A Stage-2 relaunch collided with four pre-shutdown agents on all four `_parts/`
   paths and on a company dossier. Nothing was lost only because both writers preserved rather than
   overwrote, but the collision cost ~35% of the wave in re-merging and produced 38 duplicate record IDs
   in one register, which then had to be renumbered with a superseding note.
   **Recovery rule when a collision has already happened:** never delete the other pass's records. Declare
   one register canonical in a collision note at the top of the file, alias the duplicate IDs to it, keep
   the genuine value-adds from the losing pass, and hand the de-duplication to the merge as an explicit
   outbound correction.
8. **Before writing any inherited figure, grep it against the local corpus.** A number that arrived from an
   upstream dossier must be searched across every filing and artifact on disk before it is written down; if
   it appears nowhere, it is not evidence and it becomes a retraction with a conflict entry, not a value.
   **Success recorded.** The Stage-2 quantitative assembler found that a received FY1996 money set
   (`12,284 / 3,462 / 4,322 / 850 / 1,326 / (3,036) / (0.18) / 2,398 / 3,268 / 8,839 / 5,804`) occurred **zero
   times** across all five SEC accessions on disk, footed only against itself, and failed three balance-sheet
   and cross-foot identities — while looking entirely plausible. It kept every row ID, reset each value to the
   filed figure, printed the superseded value inside the same cell as a retraction, and opened **U.60**
   (`### P.2a Corrections taken on this pass` in `_parts/s2_p4.md`). The registers were then verified to carry
   the received set only inside retraction language. The corollary is the reason §3 exists: a plausible number
   with a citation is still unchecked until the cited line has been read.

