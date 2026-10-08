# Harvest mining -- mckesson

Window applied: 1969-01-01 .. 1995-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

67 candidate rows in the harvest index; 12 items mined; 54 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 1 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 2 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 1 | text held, zero hits. |
| `UNANSWERED` | 8 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: none; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `m0OkScrANH4C` | 1995-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `vYlFDAAAQBAJ` | 2016-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `ZbBkDAAAQBAJ` | 2016-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `zGNdqqufumEC` | 1995-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `micro_IA40385002_0162` | 1990-01-01 / title:1990 | in-window | 143,793 | 0 | 0 | - | NULL |
| `ERIC_ED130304` | 1976-01-01 / title:1976 | in-window | 59,069 | 6 | 0 | - | BARE_WORD_MATCH |
| `micro_IA40385003_0251` | 1976-01-01 / title:1976 | in-window | 1,063,607 | 156 | 8 | `mckesson, inc` | TIER1_CANDIDATE_TEXT |
| `simpletruthpoems0000levi` | 1994-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `storyofforemostm0000mori` | 1979-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `history0000knig` | 1980-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `DTIC_ADA113164` | 1981-01-01 | in-window | 9,020 | 2 | 0 | - | BARE_WORD_MATCH |
| `unitedstatesofam0000unse_f6r3` | 1982-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `ERIC_ED130304` l.70: McKesson, and Dave Mil4s;
- `ERIC_ED130304` l.240: just for kids - w/Reporter Mike McKesson
- `ERIC_ED130304` l.832: early as kindergarten^. - Reporl.er lMike -McKesson of member station
- `micro_IA40385003_0251` l.11: FOREMOST-McKESSON, INC.,
- `micro_IA40385003_0251` l.31: Foremost-McKesson, Inc.
- `micro_IA40385003_0251` l.229: Foremost-McKesson, Inc.,
- `DTIC_ADA113164` l.100: and  the  Narco-McKesson  Brown  scavenging  mask  were  used  during  the
- `DTIC_ADA113164` l.268: The  Narco-McKesson  (Brown)  scavenging  mask  used  during  this  survey  was  a
