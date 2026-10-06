# Harvest mining -- kroger

Window applied: 1883-01-01 .. 1960-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

26 candidate rows in the harvest index; 12 items mined; 12 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 1 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 1 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 10 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: none; **other quoted terms** (predecessors, siblings, trade titles): `big star`, `chain store age`, `progressive grocer`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `NNn52klcXpsC` | 1905-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `GEA_AQAAMAAJ` | 1901-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `BajGB4fFBk0C` | 1929-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `nYAwAQAAMAAJ` | 1914-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `7ZFBAQAAMAAJ` | 1921-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `FeFLAQAAMAAJ` | 1922-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `7McuAQAAIAAJ` | 1925-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `PvyrwBlrrQUC` | 1940-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `OWW2v9FmTekC` | 1925-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `krogercoannualreports` | ? / title:1925 | in-window | 511,713 | 200 | 8 | `kroger co`, `kroger stock` | TIER1_CANDIDATE_TEXT |
| `Z08SAQAAMAAJ` | 1951-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `micro_IA41152647_0718` | 1987-01-01 / title:1985 | outside? MISMATCH | 110,951 | 5 | 0 | - | BARE_WORD_MATCH |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `krogercoannualreports` l.181: dividends and stock buybacks. If you had invested $100 in Kroger stock on January 31, 2000, and reinvested
- `krogercoannualreports` l.182: all dividends issued, your investment would have been worth $233 on January 31, 2014, and Kroger’s Total
- `krogercoannualreports` l.267: • Contributing an additional $9.1 million to local organizations in 2013 through The Kroger Co. Foundation.
- `micro_IA41152647_0718` l.30: oe: Peter M. Kroger
- `micro_IA41152647_0718` l.87: 15. Supplementary Notes (Authors, continued) Ojars J. Sovers, Peter M. Kroger, Lisa L.
- `micro_IA41152647_0718` l.515: 1985; Kroger et al., 1987; Sovers et al., 1984]. The results from these and
