# Meta Stage 1 — audit 1

Agent `audit-wave-20261014`. Not the author and not the merger. Web calls: 0.

## VERDICT: **FAILED** — quote gate 6 of 35, one of them checked against the filing

## B-n
None on the lenses run. I did not recompute the 36 quantitative rows.

## F-1 — six unmatched attributed spans
The gate lists, squashed:
- facebook inc 2005 stock plan as amended april 2006…
- in 2004 and 2005 mr zuckerberg s father provided us with initial working capital
- walmart u s purchased advertising on facebook…
- this prospectus contains estimates and information concerning our industry…
- we estimate that false or duplicate accounts may have represented approximately 5 6 of our maus…
- twitter google s social media properties including orkut…

I opened the second. `sources/sec/0001193125-12-232582_d287954ds1a.htm` line 19576 prints "In 2004 and 2005, Mr. Zuckerberg's father provided us with initial working capital", with `&#146;` for the apostrophe. `strip_html` decodes `&nbsp;` and `&#39;` and does not decode `&#146;`, so the squashed filing does not contain the squashed quotation. That span is in the filing. I did not open the other five one by one, and I did not rewrite any of them.

## Census
Conflicts: the census shows the part's U-ids present (15 requested, 15 present on the key it could read). Sources requested 20 provisional keys (`P1S*` and `P2SRC*`); live sources are **15** rows, S4495–S4509. The merge report accounts for the difference: 5 part-2 rows were aliased onto part-1 carriers (`03_quality_control/meta_s1_merge.md`). I did not re-read each alias. The count matches that account. It is not 20 dropped documents.

## Clean checks
Keys resolve. Anchors 8, parity holds. Corrections: 9 ids in both layers. 30,212 words over the T2 target, advisory. Csv registers passed.

## Matcher
One of six substantive misses was re-read and is an entity-decoding miss, not an absent sentence. I am not extending that classification to the other five.

## Untouched
Volumes, registers, manifests, `sources/`, `research/`, and `CORRECTIONS.md` were not edited. No retrieval. Every quantitative row was not recomputed from its carrier; that lens is open. This audit does not repair and does not certify.
