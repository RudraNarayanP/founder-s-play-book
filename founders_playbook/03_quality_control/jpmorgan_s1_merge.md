# JPMorgan Stage 1 — merge close-out

**Agent:** `merge-jpmorgan-finish` (2026-10-14). **Role:** finish the bookkeeping the 2026-10-07 merger
(`merge-jpmorgan`) had already done inside `stage_1.md` and the nine registers. This file is not an audit
and not a certification. The author's narrative was not rewritten. No source id was minted. Nothing under
`sources/` was edited.

The resume brief said the mint had never happened. Measured from disk before any write, that sentence was
already false, so the mint was not repeated.

## What was already on disk

| item | measured |
|---|---|
| `stage_1.md` | present, with a full MERGE RECORD dated 2026-10-07 |
| nine registers | 214 data rows: sources 23, quantitative 52, timeline 61, conflicts 13, data_gaps 15, decisions 17, validation 14, failures 10, channels 9 |
| id block | `00_universe/_ID_BLOCKS.tsv` rows S4531–S4553, company `company_012_jpmorgan`, agent `merge-jpmorgan` |
| `sources.csv` keys | S4531–S4553, zero `PROV-*` |
| `CORRECTIONS.md` | absent, and the MERGE RECORD says that absence was a decision |
| `_MANIFEST.md`, this report, the gates report | scaffold stubs |

`tools/id_mint.py` was not run. Re-claiming S4531–S4553 would either be refused or would allocate a second
block above S4657. Neither is the binding the registers already use.

## Census, re-run, and how the ambiguous pair was left

`python tools/merge_census.py --company-dir founders_playbook/01_companies/company_012_jpmorgan`

| register | requested | present | missing | unkeyed |
|---|---|---|---|---|
| `conflicts.csv` | 13 | 13 | 0 | 0 |
| `sources.csv` | 23 | 0 | **23** | 0 |
| the other seven | as in the volume's table | — | 0 | all of them |

**TOTAL missing keyed rows: 23**, every one `PROV-JP1-01`…`PROV-JP1-23` from `_parts/s1_p1.md`. The live
register holds the same 23 documents under S4531–S4553. The census compares the part's key string to the
register's key string and cannot see a re-mint. The volume's id map is the adjudication: `PROV-JP1-nn` →
`S(4530+nn)`. Provisional keys were never supposed to survive into the live register. The part stays
read-only, so this "missing" line will keep printing. It is not 23 dropped rows.

`validation.csv` and `failures.csv` still print as one `AMBIGUOUS` pair (identical 11-column schemas). The
census's content hints are the **decisions** block, the defect the tool's own comment names, and they were
not used. The 2026-10-07 merger adjudicated by block heading and by row: part l.1154 names validation (14
rows) and l.1177 names failures (10 rows); 14+10 = 24 = the unattributed total; the written files share 0
rows. This pass re-counted 14 and 10 with `csv.reader` and moved nothing.

## Two preamble lines that were making the gates read the wrong set

Both edits are in the merger's own MERGE RECORD, not in the author's sections.

1. **Anchors.** `declared_anchors()` takes the first `ANCHORS:` comment in the file. The MERGE RECORD
   illustrated the part's comment as `` `<!-- ANCHORS: U.001 … U.013 -->` ``, and the ellipsis does not
   expand, so the gate's authoritative set was `{U.001, U.013}`. The real declaration, listing all thirteen
   ids, sits later and was ignored. That is why the baseline reported register rows citing U.002, U.004,
   U.006–U.009, U.011 and U.012 as undeclared, while `### U.001` through `### U.013` are all in §U. The
   illustration no longer contains the token `ANCHORS:`. The declaration the gate now reads is line 174,
   and the re-run reports **13 narrative anchors ↔ 13 register anchors**.

2. **Keys.** The sentence naming Cigna's already-claimed ids used an en-dash range `` `S4529–S4530` ``.
   The gate protects the id *before* an en-dash and does not protect the id after it, so `S4530` (held by
   `repair-cigna`, not by this company) fired as an unresolvable citation. The word `range` was added in
   front of that backtick. `S4530` is now in the protected-history note with S0001, S4222, S4229, S4528 and
   S4529. It was not added to `sources.csv`. Nine JPMorgan source tokens in the volume resolve.

`stage_1.md` is **34,641 words** after those two edits (it was 34,637). Still under the 60,000-word cap,
still over the T2 22,000-word target. The overage stays advisory.

## Quote gate: one tool defect fixed, four spans left for an auditor

`gates.py` `strip_html` used `<[^>]+>`. On
`sources/periodicals/historyofchemica00chemuoft_djvu.txt` an OCR debris span opening `<^^  X-` and running
12,458 characters was treated as a tag and deleted. Inside that span, at lines 1887–1889, is the verbatim
sentence the volume quotes: "The pressure in the money market has not been so great since the spring of
1837 as it is at this moment." The tag pattern now requires an HTML name
that starts with a letter. Real tags (`<html>`, `<div …>`) still strip. `gates.py --self-test` passes,
including a new control that plants this shape. Re-run on Boeing and GM (temp outputs, not written over
their reports) still exits 0 under `--fail-on substantive`.

After that fix the money-market span matches. **4 of 24** attributed spans still do not, and they were not
rewritten:

| span in `stage_1.md` | what the held byte actually is |
|---|---|
| "supply the double-quote pairs around the bracketed phrases on merge, never backslash escapes" | The merger quoting `data_gaps.csv`'s FR-6 instruction. That instruction is not a source document. Registers are not in the quote corpus. |
| "An American Bank offering complete Foreign Banking Service in the principal Markets of the world" | `NPDP19360702_djvu.txt` l.15284–15290 prints "An American: Bank' offering com- / plete Foreign Banking Bervice / in the principal Marketa of the / * world". The volume has normalised OCR (`Service`, `Markets`, the hyphenation). |
| "There are nine banks now in existence whose history reaches back into the Eighteenth Century … two are in Massachusetts …" | `bankofthemanhatt17374gut__17374.txt` l.97–100 has both sides. The volume's ellipsis drops "Of these,". The gate concatenates across `…`, so the joined string is not a contiguous span. Both fragments are in the booklet. |
| "John Pierpoint Morgan, the American financial magnate, who left Flushing, in Belgium … has arrived in Gdynia" | `NPCM19370823_djvu.txt` l.2476–2480 prints "ohn Pierpoint Morgan", "Veft Flashing", "Gydnia", and the words "several days ago in his private yacht" where the volume puts an ellipsis. The volume has cleaned OCR and bridged a gap. |

Those four are an auditor's question. Changing the quotations to force a match would either repair OCR in
the narrative or invent a contiguous sentence the carrier does not print.

## What this pass did not do

- No `CORRECTIONS.md`. Seeding one with no `COR-nn` makes the corrections gate report UNANSWERED. Seeding
  one that records the id map would require propagating every new tag into a register and into the volume.
  The 2026-10-07 merger declined, no `data_gaps` row asks for the file, and the id map is already in the
  MERGE RECORD. Left as that decision.
- No audit verdict. `anchors` and `keys` now pass; `quotes` still fails substantive (4/24). A different
  agent audits. This agent does not certify.
- No second id block, no register rewrite, no source-file edit.

## Commands that produced the numbers above

```
python tools/merge_census.py --company-dir founders_playbook/01_companies/company_012_jpmorgan
python tools/gates.py --company-dir founders_playbook/01_companies/company_012_jpmorgan --tier auto \
  --out founders_playbook/03_quality_control/jpmorgan_s1_gates_merge.md --fail-on substantive
python tools/gates.py --self-test
```

Gates exit on this company is **1** (the quote finding). Self-test exit is **0**.
