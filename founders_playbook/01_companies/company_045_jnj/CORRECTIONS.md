# CORRECTIONS — company_045_jnj (Stage 1)

Binding merge-pass corrections for `stage_1.md` and the nine registers. Append-only: never rewrite history,
never re-tier, re-date, re-value or delete. Applied at merge 2026-10-07 by `merge-jnj`.

## COR-01 — provisional source keys are superseded by minted globals
`P1S01…P1S15` (and `P1S05b`) are dossier-local reading keys. In the **live registers** the `source_id`
(and the `source` / `claim_a_source` / `claim_b_source` cells) are the minted globals **S4463–S4478**, allocated
centrally by `tools/id_mint.py --count 16 --company company_045_jnj --claim --agent merge-jnj` above the highest
live id. No register row may keep a `P1Sxx` value in a key column. The full map is in the `stage_1.md`
**MERGE RECORD**; the narrative keeps the local tags and is bound by that table. This correction touches no
value, date or wording — only the key space.

## COR-02 — validation vs failures bound by row content, not by header
`validation.csv` and `failures.csv` share a byte-identical 11-column header, so `merge_census.py` reports the
pair `AMBIGUOUS` and cannot attribute either block (expected residue, not a defect). The author emitted **two
separate fenced blocks** under `### validation.csv` (7 rows) and `### failures.csv` (5 rows). Bound on those
headings **and** on content: positive demonstration signals → `validation.csv`; adverse and record-selection
signals (lost stamp-tax determination, imitation bill, broken price ring, illegible price cut, and the
"ABSENCE-OF-ANY-ESTABLISHED-FAILURE" null) → `failures.csv`. Bound into the first-row `notes` cells of each
register. The content split is a reader HINT; the block headings are the authority.

## COR-03 — late-arrival accounting and the harvest-NULL-vs-bytes finding preserved at merge
The corpus grew after the probe: **15 layers / 23,308,643 B / 642 entity namings** (the probe measured 14 /
23,275,060 / 619). The single delta is the late-arriving `John0851_1970` annual report (33,583 B, fetched
2026-10-06, 23 namings) whose bytes carry 23 namings while `research/A4_harvest_mine.md` records it as **NULL,
0 entity hits** — a label outranked by the bytes (RD-124, **U.011**). This accounting is preserved in
`_MANIFEST.md`, the `stage_1.md` MERGE RECORD, the `quantitative.csv` census row and the `timeline.csv` 1970
row, so that no later pass inherits the probe's 14/619 as the live count. It re-tiers nothing (**T2 core —
PROVISIONAL stands**, `U.008`/`U.012`).

## COR-04 — three quantitative `source_date` cells aligned to the carrier's established date
Three `quantitative.csv` rows (the absorbent-cotton series citing S4464) carried `source_date` as the bare word
**`UNCONFIRMED`**, while their carrier S4464 (`redcrossnotes01`) carries the publication date **`UNCONFIRMED
(>=1919)`** — the author's own finding (U.006: the volume's copyright legs 1914/1915/1919 push the retrospective
lag past 33 years). The merge aligned those cells to **`UNCONFIRMED (>=1919)`** so a date column carries the year
the dossier already established. This **adds the finding's own bound and removes no value**; it is not a re-timing.

## Not corrected, and why
No row was folded, trimmed or added (**102 emitted, 102 applied** — the part's own `= 101` total mis-sums its
authoritative per-register breakdown; the merge applied every emitted row rather than deleting one to match it).
The author's probe supersessions
(`U.002` incorporation-not-found regex defeated by a line-broken sentence; `U.004` asepsis title-page authorship;
`U.006` `redcrossnotes01` ≥1919; `U.009`/`U.010` americandruggis07 locator and Red-Cross-incorporator misfile)
are carried as conflicts and narrative **exactly as written** — they are the finding, not defects to repair.
No value, date, quote or verdict in the part was edited during application.
