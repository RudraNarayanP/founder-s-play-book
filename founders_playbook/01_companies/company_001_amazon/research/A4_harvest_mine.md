# Harvest mining -- amazon

Window applied: 1994-01-01 .. 1997-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

41 candidate rows in the harvest index; 4 items mined; 36 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 0 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 1 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 1 | text held, zero hits. |
| `UNANSWERED` | 2 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `amazon com`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `NASA_NTRS_Archive_19980017484` | 1997-01-01 / title:1998 | in-window MISMATCH | 35,332 | 18 | 0 | - | BARE_WORD_MATCH |
| `soulasvirginwife0000holl` | 1995-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `first-ecommerce-announcement` | 1995-01-01 | in-window | 759 | 0 | 0 | - | NULL |
| `handbookofdefens0002unse` | 1995-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `NASA_NTRS_Archive_19980017484` l.9: Title: Land-Use Change, Soil Process and Trace Gas Fluxes in the Brazilian Amazon Basin
- `NASA_NTRS_Archive_19980017484` l.35: southwest Amazon that has experienced rapid deforestation, primarily for cattle ranching, since
- `NASA_NTRS_Archive_19980017484` l.100: Vida on soils that are typical of Rondonia and the Amazon Basin as a whole. One sequence on
