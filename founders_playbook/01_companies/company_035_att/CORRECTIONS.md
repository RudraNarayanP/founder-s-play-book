# CORRECTIONS.md — company_035_att (Stage 1)

Append-only provenance-correction register for the AT&T Stage-1 dossier. Established **at the Stage-1 merge pass,
2026-10-07** (agent `merge-att`), each item verified against the author emission `_parts/s1_p1.md`, against
`_parts/NOTES_att_p1.md`, and against the register rows applied by that pass. **Nothing here re-tiers, re-dates,
re-values, re-titles or deletes a claim.** These are key, propagation and schema corrections — the classes a merge is
allowed to make. A later pass adds a dated entry below this one; it does not delete one.

**Reading rule.** Every `COR-nn` below is printed in the register layer *and* in `stage_1.md`, because a correction
that reaches only the prose leaves the registers teaching the withdrawn form (method §14.10). Propagation is measured
by `tools/gates.py --checks corrections`; the cell each entry touched is named in
`03_quality_control/att_s1_merge.md`. Where an entry names an annotation, the annotation was **appended to the end of
an existing `notes` cell**: no value, date, source key, evidence class or confidence on any of the 136 applied rows was
altered, and no row was folded or moved between registers.

---

## COR-01 — the dossier-local source tags `P1S01–P1S14` are superseded by minted ids `S4449–S4462` (2026-10-07)

**What the author emitted.** 14 `sources.csv` rows keyed `P1S01`…`P1S14`, with the same tags carried in the
`source_id` / `source` cells of `quantitative`, `timeline`, `decisions`, `validation`, `failures` and `channels`, and
inside prose cells of `conflicts` (`claim_a_source`, `claim_b_source`) and `data_gaps`
(`best_available_evidence`). `_parts/s1_p1.md` l.906 states the arrangement: "`source_id` values are dossier-local and
provisional (`P1Sxx`); real ids are minted centrally at merge (§13, `tools/id_mint.py`), and no row here assumes one."

**Correction applied.** `python tools/id_mint.py --count 14 --company company_035_att --claim --agent merge-att`
allocated **S4449 … S4462** contiguously, above the highest live id (`--audit` at mint time: 351 distinct issued ids in
range `S0001`–`S4430`, registry claims held through `S4448` by `company_006_cvs`, tool's own `next assignable:
S4449`). Every applied register cell now carries the minted id — **no register row and no cell retains a `P1Snn` tag
as a citation** (verified by regex over all nine files; the only 14 surviving occurrences are the alias annotations
this entry itself mandates, inside the `notes` cells of `sources.csv`). The narrative volume keeps the author's local
tags, because they are the reading keys of §Header 1, §T, §U and the claim records, and is bound to the global space
by the mapping table in `stage_1.md` (merge record, "Provisional-to-global id map").

**Why this is a correction and not a rename.** Ids minted by authors have collided in this project (RD-123, RD-131),
which is why allocation runs through `00_universe/_ID_BLOCKS.tsv`. **This entry is the authority for treating any
`P1Snn` value found in a live register cell from now on as a stale key, not as a second source.**

**Propagated to.** all 14 `sources.csv` `notes` cells · `stage_1.md` merge record.

---

## COR-02 — the two schema-identical emission blocks are bound: 7 rows → `validation.csv`, 10 rows → `failures.csv` (2026-10-07)

**The defect class.** `validation.csv` and `failures.csv` share a byte-identical 11-column header, so
`tools/merge_census.py` cannot attribute either block and printed both as
`AMBIGUOUS:validation.csv,failures.csv`. Left alone, a later pass could read the 7-row block as failures or the
10-row block as validation and re-key 17 rows wrongly — the misfile the wave plan names for Nvidia, Tesla and
Microsoft.

**Correction applied, by content.** Three rules, in order: (1) each `>>> REGISTER ROWS FOR MERGE <<<` marker names
its target, and `_parts/NOTES_att_p1.md` §5 declares validation **7** · failures **10**, exactly the parsed widths;
(2) 7 + 10 = 17 = the rows listed unattributed, with no row in both groups; (3) row-by-row content against Amazon's
conformant usage — every `what_it_demonstrated` cell in the 7-row group states a validation (the 1912 and 1913
underground conversations, the 1913-12-19 acceptance by the Administration, the shareholder base, growth at network
scale, the ten-of-eleven cross-foots, asserted self-financing capacity), while all 10 cells of the other group state
an incurred adverse signal (the defective tinsel-braid cable, lead-sheath corrosion, the Boston cable failures, the
1883 distance ceiling, the 1905 receivership, the Central Union consent to receivers, the fall in surplus earnings,
the independent wave's own collapse, the loud-speaking promotions, the asserted wholesale obsolescence). **No row was
moved and none was split.**

**Recorded as a tool finding, not repaired here.** The content hints the census printed for these two groups were the
*decisions* block's rows: `merge_census.py` calls `hint_validation_or_failures(data)` in the AMBIGUOUS branch before
`data` is assigned for that block, so it reports the previous iteration's rows. The adjudication was therefore made
from the block text, not from the hints.

**Propagated to.** `validation.csv` last-row `notes` cell · `failures.csv` last-row `notes` cell · `stage_1.md`
merge record and application table.

---

## COR-03 — the probe's label counts and periodical-shelf byte total are superseded by this dossier's re-measurements (2026-10-07)

**What was inherited.** `research/A_chronology_feasibility.md` (agent `probe-att`) printed `American\s+Telephone` =
**35** in the FY1913 layer; token counts over **37** stored SEC files (`1984` 74, `Bell Telephone Company` 47,
`Southwestern Bell` 566); one `1915` hit in the FY1913 layer; and a periodical shelf of **660,753 B**.

**What this dossier measured** (`_parts/NOTES_att_p1.md` §2 and §4, items `ATT-S1-C1`, `C2`, `C5`, and the two new
counts): **29** case-sensitive / **35** case-insensitive / **0** single-space literal; re-measured over the **7**
documents this stage cites (`1984` 40, `1885` 1, `Bell Telephone Company` 32, `Southwestern Bell` 207, `American
Telephone and Telegraph` 7) with the load-bearing zeros surviving at the smaller denominator; **two** `1915` hits,
the second at l.5091 being a **1914→1915 stock-payable maturity, not an opening**; one `1894` hit, a chart-axis tick;
and **707,735 B** over the same six periodical layers.

**Correction applied.** The supersession is recorded in the register layer (S4461 `notes`) and in the volume, **not**
by rewriting the volume's own §T.4 line: `stage_1.md` still prints **660,753 B** where the author wrote it, because
§14 rule 4 bars a merge from silently re-issuing another pass's numbers. The audit pass decides whether to repair it
in place. **Until then, `707,735 B` is the measured figure and `660,753 B` is the inherited one; both are on the
record and neither is deleted.**

**Propagated to.** `sources.csv` S4461 `notes` cell · `stage_1.md` merge record ("Not applied, not attempted, and
why", item 1) and §Header 4 / §T.4 as written by the author.

---

## COR-04 — the 1885 recital belongs to CIK 0000005907 (P2) and is never attachable to CIK 0000732717 (P4); the quarantined 5907 index stays NOT EVIDENCE (2026-10-07)

**The risk this binds against.** Four legal persons carry the name. The ticker `T` resolves to CIK **0000732717**
(Southwestern Bell Corporation, Delaware 1983 → SBC Communications Inc → AT&T Inc), and the name route returns it for
"AT&T Corp" too, because `NAME_STOP_WORDS` deletes both `corp` and `inc`. The only filed sentence for **1885** is in
CIK **0000005907**'s own FY1993 Form 10-K (l.238, "incorporated in 1885 under the laws of the State of New York"),
which is **RESTATED** — a 1994 instrument reciting 1885 — and is not an in-window document. Attaching that sentence
to 732717, or attaching the 1983/1984 recital to the 1885–1913 record, is the Morgan Stanley / Cigna / Marathon
failure mode this project has already paid for eleven times.

**Binding.** `sources.csv` **S4452** carries the 1885 recital with `evidence_class` = `RESTATED as to 1885`; the P4
rows **S4453–S4456** carry the 1983/1984 recital as a separate registrant's own words; and **S4459** (the quarantined
CIK 5907 submissions index, 1,255 filing rows, perimeter 1994-01-07 → 2007-01-18) and **S4460** (CIK 732717, 7,922
filing rows, perimeter 1994-02-14 → 2026-10-02) are registered as **"NOT EVIDENCE — a measurement of the archive's
reach"**, with the perimeter, and not as filings and not as an absence of filings. The `timeline.csv` rows for 1983
and 1984-01-01 stay marked `OUT OF WINDOW`, and the 1915 row stays `CONTEMPORANEOUS as DESIGN; event UNKNOWN`.

**Propagated to.** `sources.csv` S4452 and S4459 `notes` cells · `stage_1.md` §Header 1, §Boundary 2–3, §U.1, §U.2,
§U.3, §U.7 and the merge record.

---

## Not corrected, and why

1. **The two unresolvable `claim_ref` cells in `decisions.csv`** (rows 4 and 5 print `L03`, `L07`; the volume's §L
   claim records are `L01`/`L02` and its table labels are `L-3`/`L-7`). Applied verbatim; named in the application
   table and in `03_quality_control/att_s1_merge.md`; rewriting another pass's cross-reference is a repair-pass job.
2. **`S6-11` in §Header 1 and §T.6** is the DTIC document code `S6-11-25-ATT`, quoted as print to show that a bare
   `att` token is a substring of somebody else's code. `gates.py --checks keys` reads it as a hyphenated record key
   and lists it for review; it is **not** re-pointed to any register, and no source row is minted for a document code.
3. **The tier was not re-tiered and no word count was trimmed.** T2 core, PROVISIONAL, is inherited from the probe;
   the volume is 31,282 words against a 22,000 density target, which `gates.py` now classifies `advisory`, and
   §9.6 forbids cutting evidence to fit a file limit.
4. **The five `FETCH REQUEST` blocks (R-1…R-5) were not run by this pass** and are therefore not closed, not
   retried and not reported empty. Family (b) remains **UNTRIED for lack of any route** (no `att` entry in
   `tools/web_domains.json`), and family (e) remains **UNTRIED and UNIMPLEMENTED** (no auction/museum endpoint exists
   in `tools/*.py`).
