# Harvest mining -- walmart

Window applied: 1945-01-01 .. 1972-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

69 candidate rows in the harvest index; 6 items mined; 59 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 6 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 0 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `wal mart`, `wal mart stores`; **other quoted terms** (predecessors, siblings, trade titles): `five and dime`, `walton s`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `1972-annual-report-for-walmart-stores-inc` | 1972-01-01 / title:1972 | in-window | 23,989 | 0 | 22 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1996-annual-report-for-walmart-stores-inc` | 1996-01-01 / title:1996 | outside? | 103,092 | 0 | 156 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1986-annual-report-for-walmart-stores-inc` | 1986-01-01 / title:1986 | outside? | 67,944 | 0 | 56 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1985-annual-report-for-walmart-stores-inc` | 1985-01-01 / title:1985 | outside? | 67,944 | 0 | 57 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1987-annual-report-for-walmart-stores-inc` | 1987-01-01 / title:1987 | outside? | 69,056 | 0 | 61 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1998-annual-report-for-walmart-stores-inc` | 1998-01-01 / title:1998 | outside? | 120,540 | 0 | 200 | `wal-mart` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `1972-annual-report-for-walmart-stores-inc` l.203: considered  Wal-Mart's  best  ever.  Our  total  sales
- `1972-annual-report-for-walmart-stores-inc` l.210: These  were  some  of  the  highlights  for  Wal-Mart
- `1972-annual-report-for-walmart-stores-inc` l.221: our  Board  of  Directors  for  all  regular  Wal-Mart
- `1996-annual-report-for-walmart-stores-inc` l.9: at  our  vending  machines,  Wal-Mart  will  donate  a  nichel  to  local  Edge  Scholarship  Fund,  Competitive  Edge  SenoUwmpfl  help
- `1996-annual-report-for-walmart-stores-inc` l.16: WAL-MART
- `1996-annual-report-for-walmart-stores-inc` l.19: Inside  Wal-Mart!
- `1986-annual-report-for-walmart-stores-inc` l.6: OF  WAL-MART
- `1986-annual-report-for-walmart-stores-inc` l.65: Wal-Mart  Stores
- `1986-annual-report-for-walmart-stores-inc` l.145: most  important  role  in  Wal-Mart's  pursuit  of  excellence.
- `1985-annual-report-for-walmart-stores-inc` l.1: WAL-MART
- `1985-annual-report-for-walmart-stores-inc` l.42: In  Wal-Mart's  promise  of  "satisfaction  guaranteed,"  people  make  the  differmce.  Whatever  their
- `1985-annual-report-for-walmart-stores-inc` l.43: capacity,  Wal-Mart  associates  are  supported  by  up-to-date  systems  that  enhance  productivity  and
- `1987-annual-report-for-walmart-stores-inc` l.1: WAL-MART
- `1987-annual-report-for-walmart-stores-inc` l.71: Wal-Mart  Stores
- `1987-annual-report-for-walmart-stores-inc` l.252: feet.  We  opened  121  new  Wal-Mart
- `1998-annual-report-for-walmart-stores-inc` l.28: WAL-MART  Annual  -jy
- `1998-annual-report-for-walmart-stores-inc` l.46: investment  base,  Wal-Mart  focuses  on  customer
- `1998-annual-report-for-walmart-stores-inc` l.53: Letters  to  Wal-Mart
