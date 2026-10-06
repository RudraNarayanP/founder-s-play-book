# Harvest mining -- citigroup

Window applied: 1812-01-01 .. 1998-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

156 candidate rows in the harvest index; 12 items mined; 133 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 1 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 7 | text held, zero hits. |
| `UNANSWERED` | 4 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: none; **other quoted terms** (predecessors, siblings, trade titles): `first national city bank`, `formerly known as`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `citibankralphnad00lein` | 1973-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `travelersaidsoci1921trav` | 1921-01-01 / title:1921 | in-window | 13,388 | 0 | 0 | - | NULL |
| `Firs2314_1969_0` | 1969-01-01 / title:1969 | in-window | 111,014 | 84 | 1 | `citicorp systems` | TIER1_CANDIDATE_TEXT |
| `micro_IA41153428_0048` | 1982-01-01 | in-window | 77,122 | 0 | 0 | - | NULL |
| `travelersaidsoci1922trav` | 1922-01-01 / title:1922 | in-window | 12,120 | 0 | 0 | - | NULL |
| `CIA-RDP78-03985A000700030034-1` | 1953-01-01 | in-window | 3,898 | 0 | 0 | - | NULL |
| `travelersaidsoci1923trav` | 1923-01-01 / title:1923 | in-window | 52,094 | 0 | 0 | - | NULL |
| `dli.ministry.19544` | 1969-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `citibankralphnad0000unse` | 1974-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `roadstozion0000kurt` | 1948-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `tassd_monthly_1915` | 1915-01-01 / title:1915 | in-window | 49,654 | 0 | 0 | - | NULL |
| `dli.csl.1046` | 1969-01-01 | in-window | 59,151 | 0 | 0 | - | NULL |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `Firs2314_1969_0` l.609: Citicorp Systems Inc. was formed to
