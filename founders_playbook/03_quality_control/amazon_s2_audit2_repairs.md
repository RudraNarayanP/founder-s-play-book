# Repair Sheet — Amazon.com (company_001) · Stage 2 · AUDIT 2 (Citation) repairs

Repair agent: independent of the AUDIT-2 author and of the Stage-2 producer. Run 2026-09-25.
Target sheet: `03_quality_control/amazon_s2_audit2_citation.md` (verdict FAIL).
Web requests made in this pass: **zero**. Every correction below is keyed to bytes on disk.

Scope of edits: `stage_2_claim_records.md`, `stage_2_claim_records_part_2.md`, `stage_2_part_1.md`,
`stage_2_part_2.md`, `stage_2_part_3.md`, `stage_2_index.md`, the nine `*.csv` registers,
`research/_EVIDENCE_CACHE.md`, and this sheet. Stage 1, `context_appendices.md`, `CORRECTIONS.md`,
`adversarial_review.md`, `_parts/` untouched.

| Row | Defect (audit ID) | Severity | Task | Status |
|---|---|---|---|---|
| R1 | DEFECT-1 / B110 — invented Lipsky employment range "from 1993 to 1995" | HIGH | correct to filed dates, cite accession+line, re-check surrounding claim | OPEN |
| R2 | DEFECT-2 / B100 — inverted repurchase-right holder ("by the investor") | HIGH | correct to filed text; mark affected §A.1 wording | OPEN |
| R3 | DEFECT-3 — boundary pricing leg has no carrier; press release unregistered | HIGH | search `sources/` for the release; register it if on disk, else re-label the leg | OPEN |
| R4 | DEFECT-5 / D32 — spliced "New Castle, Delaware" quotation | MEDIUM | fix quotation + citation to `l.1646-1647` + `l.1075` | OPEN |
| R5 | DEFECT-4 — ~96 of 479 records present paraphrase as quotation | SYSTEMIC | build classifier outside repo, run over all 479, emit machine list; add preambles; mark non-verbatim records | OPEN |
| R6 | DEFECT-6 — two local copies of one accession, constant 17-line offset | MEDIUM | declare spine keying + offset in `research/_EVIDENCE_CACHE.md`; delete nothing | OPEN |
| R7 | DEFECT-7 / U.80 — non-SEC evidence has no bytes on disk | HIGH (structural) | search whole repo for periodicals; else downgrade U.80's independence claim; report the 75-doc intake | OPEN |
| R8 | DEFECT-8 — exhibit quotations conflate 10.30 / 10.31; "& other products" dropped | LOW-MED | re-quote per exhibit, restore tail (if budget allows) | OPEN |
| R9 | DEFECT-9 — header self-pointer l.18 → l.22; id-join grammar | LOW | re-point; note in this sheet | OPEN |

## Outcomes

Appended per row as work completes.
