# Harvest mining -- jnj

Window applied: 1886-01-01 .. 1960-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

24 candidate rows in the harvest index; 12 items mined; 12 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 0 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 1 | text held, zero hits. |
| `UNANSWERED` | 11 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `johnson and johnson`, `johnson johnson`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `John0851_1970` | 1970-01-01 / title:1970 | outside? | 33,583 | 0 | 0 | - | NULL |
| `gov.uscourts.moeb.425961` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.moeb.426030` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.moeb.426142` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.moeb.426358` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.mowb.352359` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.laed.236813` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.moeb.426028` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.moeb.426394` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.moeb.426359` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `flatarmycreating0000pont_i0b1` | 2013-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.njd.385833` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

