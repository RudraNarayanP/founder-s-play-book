# Harvest mining -- walmart

Window applied: 1945-01-01 .. 1972-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

127 candidate rows in the harvest index; 12 items mined; 101 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 12 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 0 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `wal mart`, `wal mart stores`; **other quoted terms** (predecessors, siblings, trade titles): `five and dime`, `walton s`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `1972-annual-report-for-walmart-stores-inc` | 1972-01-01 / title:1972 | in-window | 23,989 | 7 | 23 | `wal-mart`, `walton  enterprises` | TIER1_CANDIDATE_TEXT |
| `1997-annual-report-for-walmart-stores-inc` | 1997-01-01 / title:1997 | outside? | 52,565 | 15 | 151 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1998-annual-report-for-walmart-stores-inc` | 1998-01-01 / title:1998 | outside? | 120,540 | 9 | 200 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1985-annual-report-for-walmart-stores-inc` | 1985-01-01 / title:1985 | outside? | 67,944 | 12 | 57 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1987-annual-report-for-walmart-stores-inc` | 1987-01-01 / title:1987 | outside? | 69,056 | 13 | 61 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1974-annual-report-for-walmart-stores-inc` | 1974-01-01 / title:1974 | outside? | 39,954 | 9 | 43 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1989-annual-report-for-walmart-stores-inc` | 1989-01-01 / title:1989 | outside? | 64,932 | 14 | 66 | `wal-mart`, `walton,  co` | TIER1_CANDIDATE_TEXT |
| `1973-annual-report-for-walmart-stores-inc` | 1973-01-01 / title:1973 | outside? | 29,779 | 10 | 31 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1982-annual-report-for-walmart-stores-inc` | 1982-01-01 / title:1982 | outside? | 74,087 | 11 | 72 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1990-annual-report-for-walmart-stores-inc` | 1990-01-01 / title:1990 | outside? | 54,096 | 11 | 57 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1975-annual-report-for-walmart-stores-inc` | 1975-01-01 / title:1975 | outside? | 58,278 | 9 | 73 | `wal-mart` | TIER1_CANDIDATE_TEXT |
| `1986-annual-report-for-walmart-stores-inc` | 1986-01-01 / title:1986 | outside? | 67,944 | 13 | 56 | `wal-mart` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `1972-annual-report-for-walmart-stores-inc` l.203: considered  Wal-Mart's  best  ever.  Our  total  sales
- `1972-annual-report-for-walmart-stores-inc` l.210: These  were  some  of  the  highlights  for  Wal-Mart
- `1972-annual-report-for-walmart-stores-inc` l.221: our  Board  of  Directors  for  all  regular  Wal-Mart
- `1997-annual-report-for-walmart-stores-inc` l.37: 1997   WAL-MART  Mt
- `1997-annual-report-for-walmart-stores-inc` l.46: Wal-Mart  anchors  revitalized  downtown
- `1997-annual-report-for-walmart-stores-inc` l.60: Wal-Mart  culture  drives  international  growth
- `1998-annual-report-for-walmart-stores-inc` l.28: WAL-MART  Annual  -jy
- `1998-annual-report-for-walmart-stores-inc` l.46: investment  base,  Wal-Mart  focuses  on  customer
- `1998-annual-report-for-walmart-stores-inc` l.53: Letters  to  Wal-Mart
- `1985-annual-report-for-walmart-stores-inc` l.1: WAL-MART
- `1985-annual-report-for-walmart-stores-inc` l.42: In  Wal-Mart's  promise  of  "satisfaction  guaranteed,"  people  make  the  differmce.  Whatever  their
- `1985-annual-report-for-walmart-stores-inc` l.43: capacity,  Wal-Mart  associates  are  supported  by  up-to-date  systems  that  enhance  productivity  and
- `1987-annual-report-for-walmart-stores-inc` l.1: WAL-MART
- `1987-annual-report-for-walmart-stores-inc` l.71: Wal-Mart  Stores
- `1987-annual-report-for-walmart-stores-inc` l.252: feet.  We  opened  121  new  Wal-Mart
- `1974-annual-report-for-walmart-stores-inc` l.13: History  of  Wal-Mart   4
- `1974-annual-report-for-walmart-stores-inc` l.54: WAL-MART
- `1974-annual-report-for-walmart-stores-inc` l.181: AND  WAL-MART  ASSOCIATES
- `1989-annual-report-for-walmart-stores-inc` l.1: WAL-MART
- `1989-annual-report-for-walmart-stores-inc` l.80: Wal-Mart  Stores
- `1989-annual-report-for-walmart-stores-inc` l.245: Wal-Mart  stores,  21  Sam's  Wholesale
- `1973-annual-report-for-walmart-stores-inc` l.1: WAL-MART  STORES,  INC.
- `1973-annual-report-for-walmart-stores-inc` l.171: To  Our  Stockholders  and  Wal-Mart  Associates
- `1973-annual-report-for-walmart-stores-inc` l.175: was  a  tremendous  year  for  Wal-Mart
- `1982-annual-report-for-walmart-stores-inc` l.15: $55.7  million  in  the  prior  year).  Wal-Mart  is  the
- `1982-annual-report-for-walmart-stores-inc` l.17: Company  opened  69  new  Wal-Mart  stores,
- `1982-annual-report-for-walmart-stores-inc` l.19: expanded  18  older  Wal-Mart  stores  during  the
- `1990-annual-report-for-walmart-stores-inc` l.1: WAL-MART  ANNUAL  REPORT
- `1990-annual-report-for-walmart-stores-inc` l.10: WAL-MART"
- `1990-annual-report-for-walmart-stores-inc` l.65: Wal-Mart  Stores   1,402  1,259
- `1975-annual-report-for-walmart-stores-inc` l.183: Wal-Mart  Expands  Distribution  FnciSitlet
- `1975-annual-report-for-walmart-stores-inc` l.204: It  is  a  pleasure  to  report  that  Wal-Mart  Stores,  Inc..
- `1975-annual-report-for-walmart-stores-inc` l.210: Wal-Mart  sales  were  $236.2  million  compared  to  $167.6
- `1986-annual-report-for-walmart-stores-inc` l.6: OF  WAL-MART
- `1986-annual-report-for-walmart-stores-inc` l.65: Wal-Mart  Stores
- `1986-annual-report-for-walmart-stores-inc` l.145: most  important  role  in  Wal-Mart's  pursuit  of  excellence.
