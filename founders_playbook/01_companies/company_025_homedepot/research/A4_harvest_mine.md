# Harvest mining -- homedepot

Window applied: 1978-01-01 .. 1990-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

41 candidate rows in the harvest index; 12 items mined; 23 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 2 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 1 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 9 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `home depot`; **other quoted terms** (predecessors, siblings, trade titles): `chain store age`, `discount store news`, `do it yourself`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `1989-sears-christmas-wishbook-catalog` | ? / title:1989 | in-window | 1,219,067 | 17 | 0 | - | VARIANT_TERM_HIT |
| `Wpo8v92NgjoC` | 2008-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `qQswSQwJqWUC` | 2011-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `KQUKFmw0BkAC` | 2004-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `ZbBkDAAAQBAJ` | 2016-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `vYlFDAAAQBAJ` | 2016-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `k7HWONIo88YC` | 1999-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `98ktCgAAQBAJ` | 2002-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `t2JexBk5PXQC` | 2012-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `homeimprovement100benj` | 1995-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `491bayshoreboule2820sanf` | 2005-01-01 | outside? | 1,483,641 | 200 | 200 | `home  depot` | TIER1_CANDIDATE_TEXT |
| `491bayshoreboul2820sanf_0` | 2005-01-01 | outside? | 919,040 | 200 | 205 | `home  depot`, `stores  group`, `stores  sales` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `1989-sears-christmas-wishbook-catalog` l.65758: X-ACTO® do-it-yourself knife set is great for
- `491bayshoreboule2820sanf` l.17: Home  Depot         documents  dept.
- `491bayshoreboule2820sanf` l.65: HOME  DEPOT
- `491bayshoreboule2820sanf` l.91: 491  Bayshore  Boulevard,  Home  Depot
- `491bayshoreboul2820sanf_0` l.14: Home  Depot
- `491bayshoreboul2820sanf_0` l.66: HOME  DEPOT
- `491bayshoreboul2820sanf_0` l.117: •  G.         Community  Commitments  of  Home  Depot,  U.S.A.,  Inc  G-l
