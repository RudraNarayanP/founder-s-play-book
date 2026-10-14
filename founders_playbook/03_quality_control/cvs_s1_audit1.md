# CVS Stage 1 — audit 1

Agent `audit-wave-20261014`. Not the author and not the merger. Web calls: 0.

## VERDICT: **FAILED** — no fabrication blocker; two substantive gate findings

## B-n
None. I did not find a held byte that contradicts a load-bearing date, and I did not recompute the quantitative series, so I am not in a position to declare that lens clean.

## F-1 — `quantitative.csv` source_date `-`
The row dated 1963–1979, metric "Any quantity of the origin enterprise", value UNKNOWN, source "0 carriers in 36 SEC files and 16 unique press/print documents", `source_date` `-`, evidence_class UNKNOWN. The csv gate requires a four-digit year in `source_date`. The row is an explicit null, not a fake figure. A repair can put the census date in that cell or the gate will keep failing. I did not change it.

## F-2 — quotes, 1 of 11
The unmatched span squashes to "to support this growth cvs increased distribution capacity by a 400 000 square foot dc in new jersey…". The volume's sentence is at `stage_1.md` around the New Jersey DC (the line with `[~]a 400,000-square-foot DC`). I did not re-open the carrier, so I am not calling the quotation fabricated and I am not calling it matched.

## Census
Conflicts 10/10. Sources requested 18 provisional `PROV-CVS-*` keys; live sources are 18 rows, S4431–S4448. Re-mint, not 18 lost rows.

## Clean checks
Keys resolve (one hyphenated note `S3-97`). Anchors 10, parity holds. Corrections: 4 ids in both layers. Other csv registers passed width and stage vocabulary.

## Matcher
No second matcher. The one quote miss is under the 25% line, which is why it is substantive rather than advisory.

## Untouched
Volumes, registers, manifests, `sources/`, `research/`, and `CORRECTIONS.md` were not edited. No retrieval. Every quantitative row was not recomputed from its carrier; that lens is open. This audit does not repair and does not certify.
