# PepsiCo Stage 1 — audit 1

Agent `audit-wave-20261014`. Not the author and not the merger. Web calls: 0.

## VERDICT: **FAILED** — one substantive quote finding, classified

## B-n
None found on the lenses run.

## F-1 — the one unmatched span is the TLS caveat, and it lives in sidecars the quote gate does not index
Gates: 1 of 12 quoted spans unmatched (8%), so the finding is `verbatim` rather than ADVISORY. The evidence line is "unverified tls re check before citing at high confidence". That sentence is the transport caveat. It is present in periodical `.meta.json` sidecars (for example `sources/periodicals/01-pepsi-co_djvu.txt.meta.json`). The quote index is `*.txt/*.htm/*.html/*.sgml`, not json. This is an index gap, not a sentence invented for a carrier. I did not rewrite the quotation.

Tier note: `--tier auto` graded this volume T3 (target 8,000). The volume is 22,958 words. That overage is advisory, not a defect. I am not re-tiering it.

## Census
Conflicts 15/15. Sources requested 16 provisional keys; live sources are 16 rows, S4479–S4494.

## Clean checks
Keys resolve. Anchors 15, parity holds. Corrections: 6 ids in both layers. Csv registers passed.

## Matcher
No second matcher. One span was opened far enough to name its class.

## Untouched
Volumes, registers, manifests, `sources/`, `research/`, and `CORRECTIONS.md` were not edited. No retrieval. Every quantitative row was not recomputed from its carrier; that lens is open. This audit does not repair and does not certify.
