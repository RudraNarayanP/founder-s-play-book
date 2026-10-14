# GM Stage 1 — audit 1

Agent `audit-wave-20261014`. Not the author and not the merger. Web calls: 0.

## VERDICT: **NO SUBSTANTIVE GATE FINDING** — not a five-lens certification

Gates exit 0. The quote miss rate is above 25%, so the gate labels it ADVISORY (a triage list, not defects). I did not recompute all 26 quantitative rows.

## What was run
`gates.py --tier auto` and `merge_census.py` on `company_023_gm`, 2026-10-14.

## Census
Conflicts 10/10 present. Sources requested 8 / missing 8, all `PROV-*` in the read-only part. Live `sources.csv` is 8 rows, S4423–S4430, no provisional keys. Same re-mint reading as JPMorgan: the census cannot see a key change. Unkeyed registers were not diffed cell by cell.

## Findings
None substantive. Quotes: 7 of 24 checked spans unmatched (29%), ADVISORY. Corrections: 9 ids reach registers and the volume.

## Clean checks
Keys resolve, with 4 retired ids protected as collision/range text (S0001, S4222, S4229, S4422). Anchors 10 declared, parity holds. Stage vocabulary passed the csv gate (26×12 quantitative, 30×11 timeline, and the other seven registers).

## Matcher
I did not build a second matcher. I am not reporting a personal false-positive rate. The gate's own advisory threshold is what classified the 7 spans.

## Untouched
Volumes, registers, manifests, `sources/`, `research/`, and `CORRECTIONS.md` were not edited. No retrieval. Every quantitative row was not recomputed from its carrier; that lens is open. This audit does not repair and does not certify.
