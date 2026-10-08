# Harvest mining -- statefarm

Window applied: 1922-01-01 .. 1960-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

112 candidate rows in the harvest index; 12 items mined; 98 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 1 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 11 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `state farm`, `state farm mutual automobile insurance`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `cia-readingroom-document-cia-rdp80-00809a000700030578-6` | 1951-01-01 | in-window | 3,872 | 0 | 2 | `state farm` | TIER1_CANDIDATE_TEXT |
| `kPqol0cgyh4C` | 1929-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `CJUpAQAAMAAJ` | 1928-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `EU4gAQAAMAAJ` | 1930-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `j-pJAQAAMAAJ` | 1929-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `lgn-vMSLIDgC` | 1930-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `wlGCx8nvNzkC` | 1930-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `VzTafbhUxuQC` | 1929-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `jtZxG0cxtRIC` | 1930-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `59oZAQAAIAAJ` | 1930-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `2pUjAQAAIAAJ` | 1927-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `JK8ZAQAAIAAJ` | 1926-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `cia-readingroom-document-cia-rdp80-00809a000700030578-6` l.64: HUANG-TIEN-FAN STATE FARM IN CHEKIANG
- `cia-readingroom-document-cia-rdp80-00809a000700030578-6` l.99: + present, the state farm is employing over 22 cadres and 258 agricultural
