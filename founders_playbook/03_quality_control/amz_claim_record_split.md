# amz_claim_record_split.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:05:44Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Plan

STATUS: WRITTEN 2026-09-26 (agent `amz-split-oversize`). Mechanical budget repair only: two claim-record
volumes exceed the 60,000-word hard cap (method §9.2) and `tools/gates.py --checks budget` fails on them.
Zero web, zero git, no file deleted or moved, no record's text, classification, confidence or citation
touched. If a defect is spotted it is named below, not repaired.

**Defect measured.** `stage_2_claim_records.md` = 60,718 words (over by 718); `stage_3_claim_records.md` =
84,337 words (over by 24,337). Both already chain to a `_part_2.md` (volume 2 = §U + coverage note), so the
legacy scheme is base-file = volume 1, `_part_2.md` = volume 2. The cap break is inside volume 1, which is
why the new volumes are labelled **1a / 1b** and nothing existing is renamed or renumbered: the letter-suffix
sub-split follows this project's own `_parts/s1_p3b_H_addendum.md` precedent (§9.3 "never renumber").

**Chain after the repair (numbering continuous, ids untouched).**
- `stage_N_claim_records.md` = **volume 1a** — front matter + §A…§P (S2) / §A…§L (S3), under the cap; gets a
  one-line volume label under its H1, a one-line cut cross-reference at the cut, and a supersession footer note.
- `stage_N_claim_records_part_1b.md` = **volume 1b** — new; the moved tail sections verbatim, with a
  self-labelled header naming the record range held, the file it continues and the file it continues into.
- `stage_N_claim_records_part_2.md` = **volume 2** — unchanged content; gets one added chain-note line under its
  H1, because its backward reference ("continuation of `stage_N_claim_records.md`") is now indirect.

**Cut points, chosen at a section heading so the split is simultaneously at a RECORD boundary and at a
section boundary (§9.3: never mid-table, never mid-claim-record block), measured by the census run of
2026-09-26 (`w_before` = words preceding the heading line):**
- Stage 2, cut before `Q. CHRONOLOGICAL MICRO-TIMELINE … — CLAIM RECORDS` (L750, w_before 43,738):
  head 43,738 / tail 16,980. Head keeps §A–§P (356 records A01–P90); 1b carries §Q–§T (53 records Q17–T40)
  plus the §U carry-forward stub and the "Coverage note (volume 1)" block, which travel with the text they end.
- Stage 3, cut before `M. NEGATIVE SIGNALS AND FAILURES (STAGE 3) — CLAIM RECORDS` (L902, w_before 43,929):
  head 43,929 / tail 40,408. Head keeps §A–§L (280 records A09–L15); 1b carries §M–§T (347 records M01–T58)
  plus the "VOLUME 1 ENDS HERE" statement.
- Rationale: §9.2's soft target is ≤40,000 and the amber band is 40–60k, so the cut is placed where BOTH parts
  land near the soft target with >15k words of drift headroom each, not at the last boundary before the cap —
  these files have already drifted 4,300 words past their own self-reported count (F-1), which is exactly how
  they broke the gate.

**Byte-discipline.** Split performed by `tools/_tmp_split_claim_records.py` (deterministic line-slice, no
regeneration of prose, no model round-trip of the text). The script asserts, per file, that after writing:
volume-1a text with its three added blocks removed, concatenated with volume-1b text with its header removed,
equals the original bytes exactly (SHA-256 match). It refuses to write if the assertion pair fails.

**Census baseline (before any cut), record-id regex `^((?:[A-T]\d{1,3})|(?:U\.\d{2,3}[a-z]?))\s+Claim:`** —
the 3-digit alternation is required or §P ids are lost:
- S2 vol 1 = 409 records; S2 vol 2 = 70 (U.44–U.113 + U.111a form) → stage total 479, which matches the
  front matter's own "all 479 Stage-2 records". S3 vol 1 = 627; S3 vol 2 = 55 (U.114–U.168) → 682.
- After the split each stage must still census 479 / 682 across its three volumes, with no id duplicated
  across volumes and no id absent.

**Findings spotted, NOT repaired (a mechanical pass must not smuggle in unreviewed content changes).**
- **F-1 stale self-reported counts.** `stage_2_claim_records.md` closes "Volume 1 is under the 60,000-word cap
  at 56,416 words as this note stands" while the file measured 60,718; `stage_3_claim_records.md` says
  "84,288 words on disk" against 84,337. Appends after those notes were written were not reflected.
- **F-2 count disagreement across a chain.** `stage_3_claim_records_part_2.md` states volume 1 carries
  "A09–T58, 596 records", while volume 1's own closing statement says 627 and the mechanical census says 627.
  596 is wrong or is counting a different id set; needs a judgment pass, not this one.
- **F-3 label left behind by a forced split.** The heading "## Coverage note (volume 1 — this file)" of S2 and
  the "VOLUME 1 ENDS HERE" statement of S3 now sit in volumes 1b, and S2's §U stub ("This section is carried
  in `stage_2_claim_records_part_2.md`") now sits one volume further from the file it names. Content left
  byte-identical; the labels are navigational, and the added part headers restate the true geometry.
- **F-4 gate blind spot worth knowing about.** `stage_docs()` globs `stage_*.md` in the company dir and
  `research/`, so every continuation file this pass creates IS gated (good), but `_parts/` is gated only while
  no merged volume exists — superseded intermediates there are never budget-checked by design (§15.1).

## Stage2 split

STATUS: WRITTEN 2026-09-25

## Stage3 split

STATUS: WRITTEN 2026-09-25

## Proof

STATUS: WRITTEN 2026-09-26. Determinism is the point, so every number above is reproducible with one command
and nothing depends on this agent's memory.

**1. The census command** (run from the repo root; word = whitespace-delimited token, the same regex
`tools/gates.py` uses in `gate_budgets`; record = a line opening a claim-record block, which requires the
3-digit alternative or Stage-3 §P ids up to P209 are silently missed):

```
python -c "import io,re,glob;\
 REC=re.compile(r'^((?:[A-T]\\d{1,3})|(?:U\\.\\d{2,3}[a-z]?))\\s+Claim:');\
 [print(f,len(re.findall(r'\\S+',t:=io.open(f,encoding='utf-8').read())),\
 sum(1 for l in t.split('\\n') if REC.match(l))) for f in sorted(glob.glob(\
 'founders_playbook/01_companies/company_001_amazon/stage_[23]_claim_records*.md'))]"
```

**2. Before / after, records (must be equal) and words (must differ only by added headers).**

| set | records before | records after | words before | words after | delta |
|---|---|---|---|---|---|
| Stage 2, 3 volumes | 409 + 70 = **479** | 304 + 105 + 70 = **479** | 60,718 + 27,852 = 88,570 | 44,044 + 17,340 + 27,908 = 89,292 | **+722** |
| Stage 3, 3 volumes | 627 + 55 = **682** | 347 + 280 + 55 = **682** | 84,337 + 14,990 = 99,327 | 44,228 + 40,764 + 15,036 = 100,028 | **+701** |

Every word of both deltas is this pass's own added metadata: 6 part headers/volume labels, 2 cut
cross-references, 1 supersession footer per original, 1 chain line per existing volume-2 file. No record line
contributes to the delta — the per-file record counts in the table above are the same on both sides.

**3. No id duplicated, no id lost, no id re-based.** Duplicated ids across each three-volume chain: **0**
(computed as the id set intersection of the head and tail slices, and as the multiset check over the whole
chain). Id ranges are contiguous with the company sequence and unchanged: Stage 2 runs A01 → T40 in volumes
1a/1b and U.44 → U.113 in volume 2; Stage 3 runs A09 → T58 and U.114 → U.168. Stage 2 still closes where the
Stage-3 front matter says it closes (A08, B124, C40, D34, E48, F41, G49, H44, I35, J35, K34, L20, M26, N19,
O17, P90, Q69, R25, S30, T40, U.44 → U.113), so the inter-stage boundary the §9.3 continuity rule depends on
is intact.

**4. Byte-identity of the moved content.** `tools/_tmp_split_claim_records.py` refuses to write unless, before
writing, (1a with its added blocks removed) + "\\n" + (1b with its added header removed) equals the original
string, and it re-reads both files from disk afterwards and re-checks the concatenation against the original
**SHA-256**: `6dea6dd3aac6338a…` (Stage 2) and `386a67f07a772201…` (Stage 3) both returned
`ON-DISK RECONSTRUCTION OK`. Stage 2 then received four further edits to its added metadata only (see the
correction note in `## Stage2 split`); Stage 3 received none, so its on-disk proof still stands unqualified.

**5. Gate.** `python tools/gates.py --company-dir "founders_playbook/01_companies/company_001_amazon"
--checks budget` — output pasted into the run log and into the report; both over-cap files now PASS and every
new continuation file is inside the cap (largest Stage-3 volume 44,228 words, 74% of cap; largest overall
`stage_2_claim_records_part_2.md` at 27,908 is unaffected).

**Findings for a judgment pass (see `## Plan` F-1…F-4).** F-1 stale self-reported word counts in the volume
front matter/footers (56,416 against 60,718; 84,288 against 84,337). F-2 `stage_3_claim_records_part_2.md`
states volume 1 holds 596 records; the mechanical census of the pre-split volume 1 is 627, which is also what
volume 1's own closing line says — 596 is wrong or keys a different id set, and needs the §P.2 arithmetic ids
(t1–t29) and the `s1…s35` sub-ids checked before any count in Stage-3 prose is trusted. F-3 volume labels left
behind by the forced split ("volume 1 — this file", "VOLUME 1 ENDS HERE"), which the added part headers
restate but do not overwrite. F-5 (new): the manifest `company_001_amazon/_MANIFEST.md` last regenerated its
counts 2026-09-24 and does not carry Stage-2/Stage-3 claim-record rows at all; this pass appended a
split-register so the six volumes are checkable before upload, but the register's own staleness (and the
split-watch list at its l.136, which tracks `stage_1_claim_records.md` only) is a standing §9.6 defect for
whoever next closes Stage 1.

**UNTRIED by design (zero-web, mechanical scope).** No web verification of anything; no judgment on whether
the §Q/§M section is the *right* seam beyond the word geometry; no repair of F-1/F-2/F-3 prose; no recount of
the Stage-1 volumes against the same 3-digit-inclusive census, so `stage_1_claim_records.md` at 51,632–52,549
words (86% of cap) remains unsplit and unverified by this pass; no touch of `_parts/` intermediates, which
`stage_docs()` deliberately stops gating once the merged volumes exist (F-4).

