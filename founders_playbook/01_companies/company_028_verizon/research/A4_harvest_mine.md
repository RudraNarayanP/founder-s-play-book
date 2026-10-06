# Harvest mining -- verizon

Window applied: 1877-01-01 .. 2000-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

82 candidate rows in the harvest index; 6 items mined; 75 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 0 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 6 | text held, zero hits. |
| `UNANSWERED` | 0 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: none; **other quoted terms** (predecessors, siblings, trade titles): `bell atlantic`, `bell system`, `chesapeake potomac`, `new york telephone`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `McGillLibrary-630557-27062` | 1914-01-01 / title:1914 | in-window | 7,859 | 0 | 0 | - | NULL |
| `McGillLibrary-630577-27188` | 1966-01-01 / title:1966 | in-window | 58,963 | 0 | 0 | - | NULL |
| `McGillLibrary-630554-27071` | 1917-01-01 / title:1917 | in-window | 14,750 | 0 | 0 | - | NULL |
| `McGillLibrary-630559-27056` | 1912-01-01 / title:1912 | in-window | 16,602 | 0 | 0 | - | NULL |
| `McGillLibrary-630576-27185` | 1965-01-01 / title:1965 | in-window | 51,536 | 0 | 0 | - | NULL |
| `McGillLibrary-632736-27035` | 1905-01-01 / title:1905 | in-window | 3,825 | 0 | 0 | - | NULL |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

