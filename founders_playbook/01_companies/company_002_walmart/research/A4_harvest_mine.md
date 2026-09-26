# Harvest mining -- walmart

Window applied: 1945-01-01 .. 1972-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

53 candidate rows in the harvest index; 4 items mined; 45 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 4 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 0 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `wal mart`, `wal mart stores`; **other quoted terms** (predecessors, siblings, trade titles): `five and dime`, `walton s`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `1972-annual-report-for-walmart-stores-inc` | 1972-01-01 / title:1972 | in-window | 23,989 | 0 | 22 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1976-annual-report-for-walmart-stores-inc` | 1976-01-01 / title:1976 | outside? | 63,235 | 0 | 67 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1986-annual-report-for-walmart-stores-inc` | 1986-01-01 / title:1986 | outside? | 67,944 | 0 | 56 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1990-annual-report-for-walmart-stores-inc` | 1990-01-01 / title:1990 | outside? | 54,096 | 0 | 57 | `wal-mart` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `1972-annual-report-for-walmart-stores-inc` l.203: considered  Wal-Mart's  best  ever.  Our  total  sales
- `1972-annual-report-for-walmart-stores-inc` l.210: These  were  some  of  the  highlights  for  Wal-Mart
- `1972-annual-report-for-walmart-stores-inc` l.221: our  Board  of  Directors  for  all  regular  Wal-Mart
- `1976-annual-report-for-walmart-stores-inc` l.55: year  in  ihe  history  of  Wal-Mart  with  sales  and  net  income  both
- `1976-annual-report-for-walmart-stores-inc` l.69: assure  Wal-Mart's  position  as  a  leading  retail  growth  company.
- `1976-annual-report-for-walmart-stores-inc` l.71: Wal-Mart  completed  the  year  with  125  stores  in  operation,  an
- `1986-annual-report-for-walmart-stores-inc` l.6: OF  WAL-MART
- `1986-annual-report-for-walmart-stores-inc` l.65: Wal-Mart  Stores
- `1986-annual-report-for-walmart-stores-inc` l.145: most  important  role  in  Wal-Mart's  pursuit  of  excellence.
- `1990-annual-report-for-walmart-stores-inc` l.1: WAL-MART  ANNUAL  REPORT
- `1990-annual-report-for-walmart-stores-inc` l.10: WAL-MART"
- `1990-annual-report-for-walmart-stores-inc` l.65: Wal-Mart  Stores   1,402  1,259
