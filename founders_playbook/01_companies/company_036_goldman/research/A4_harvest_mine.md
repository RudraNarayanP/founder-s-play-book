# Harvest mining -- goldman

Window applied: 1869-01-01 .. 1950-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

91 candidate rows in the harvest index; 12 items mined; 78 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 0 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 6 | text held, zero hits. |
| `UNANSWERED` | 6 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `goldman sachs`, `goldman sachs co`, `goldman sachs group`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `flyer_20240620` | 1933-01-01 | in-window | 2,096 | 0 | 0 | - | NULL |
| `KingLeonardWilliamBabylonianMagicAndSorcery` | ? / title:1896 | in-window | 437,811 | 0 | 0 | - | NULL |
| `HomiliesOfFeastsAndSundaysByCatholicChurchFathers1901` | ? / title:1901 | in-window | 839,042 | 0 | 0 | - | NULL |
| `3gWaTkXKzhgC` | 2010-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `XediUP9CiLQC` | 2010-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `GE6_DAAAQBAJ` | 2016-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `rtUvBlY83TIC` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `l8SevxCqA9oC` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `W8FGEQAAQBAJ` | 2022-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `german-ww-2-physics-anthology-berserker-books` | 1988-01-01 | outside? | 2,063,265 | 0 | 0 | - | NULL |
| `the-sacred-proto-writing-of-mankind-herman-wirth-berserker-books` | 1988-01-01 | outside? | 1,708,647 | 0 | 0 | - | NULL |
| `angel-to-some-demon-to-others_202406` | 1973-01-01 | outside? | 14,058 | 0 | 0 | - | NULL |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

