# Harvest mining -- gm

Window applied: 1908-01-01 .. 1930-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

66 candidate rows in the harvest index; 8 items mined; 57 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 1 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 7 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `general motors`, `general motors corporation`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `yndIAQAAMAAJ` | 1909-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `I1SmQH86zxIC` | 1928-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `61sgJTm2wF8C` | 1929-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `GrdvdLXgLNgC` | 1928-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `cHgpAAAAYAAJ` | 1917-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `ou0bAAAAIAAJ` | 1926-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `IyZKAQAAMAAJ` | 1920-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `NPSH19290609` | 1929-01-01 / title:1929 | in-window | 332,625 | 2 | 8 | `general motors` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `NPSH19290609` l.14708: GENERAL MOTORS
- `NPSH19290609` l.14714: General Motors has formed an
- `NPSH19290609` l.14733: The General Motors analysis of
