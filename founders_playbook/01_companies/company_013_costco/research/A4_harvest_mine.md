# Harvest mining -- costco

Window applied: 1975-01-01 .. 1993-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

33 candidate rows in the harvest index; 4 items mined; 28 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 2 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 2 | text held, zero hits. |
| `UNANSWERED` | 0 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `costco wholesale`; **other quoted terms** (predecessors, siblings, trade titles): `chain store age`, `discount store news`, `price club`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `costcowholesalef1619sanf` | 1991-01-01 | in-window | 568,295 | 200 | 59 | `costco  wholesale` | TIER1_CANDIDATE_TEXT |
| `costcowholesaled1219sanf` | 1991-01-01 | in-window | 419,592 | 104 | 48 | `costco  wholesale` | TIER1_CANDIDATE_TEXT |
| `Pric0158_1978` | 1978-01-01 / title:1978 | in-window | 12,396 | 0 | 0 | - | NULL |
| `Pric0158_1977` | 1977-01-01 / title:1977 | in-window | 107,938 | 0 | 0 | - | NULL |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `costcowholesalef1619sanf` l.9: COSTCO  WHOLESALE
- `costcowholesalef1619sanf` l.54: COSTCO  WHOLESALE
- `costcowholesalef1619sanf` l.79: Costco  Wholesale  :
- `costcowholesaled1219sanf` l.73: This  is  the  Draft  of  the  Environmental  Impact  Report  for  the  Costco  Wholesale
- `costcowholesaled1219sanf` l.112: Costco  Wholesale  :
- `costcowholesaled1219sanf` l.135: 89.469E  -  Costco  Wholesale  Project
