# Harvest mining -- cardinal

Window applied: 1971-01-01 .. 1995-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

64 candidate rows in the harvest index; 12 items mined; 46 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 0 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 5 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 7 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `cardinal health`; **other quoted terms** (predecessors, siblings, trade titles): `formerly known as`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `NASA_NTRS_Archive_19740006639` | 1974-01-01 / title:1974 | in-window | 27,819 | 24 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19850020263` | 1985-01-01 / title:1985 | in-window | 6,495 | 5 | 0 | - | BARE_WORD_MATCH |
| `cardinaldividear00noto` | 1998-01-01 / title:1995 | in-window MISMATCH | 41,687 | 28 | 0 | - | BARE_WORD_MATCH |
| `saopaulogrowthpo0000unse` | 1978-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `micro_IA41152927_0526` | 1972-01-01 | in-window | 186,841 | 100 | 0 | - | BARE_WORD_MATCH |
| `ERIC_ED073079` | 1972-01-01 | in-window | 171,126 | 92 | 0 | - | BARE_WORD_MATCH |
| `ZbBkDAAAQBAJ` | 2016-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `vYlFDAAAQBAJ` | 2016-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `iXtAAQAAIAAJ` | 1978-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `H0kcIn9nGqwC` | 1994-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `RdxrWjdEyJAC` | 2004-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `VMQwCwAAQBAJ` | 2012-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `NASA_NTRS_Archive_19740006639` l.28: FOR A CESSNA CARDINAL
- `NASA_NTRS_Archive_19740006639` l.57: FLIGHT TEST DATA FOR A CESSNA CARDINAL
- `NASA_NTRS_Archive_19740006639` l.105: a standard Cessna 177B Cardinal airplane. The airplane was fully instrumented to
- `NASA_NTRS_Archive_19850020263` l.1: A NATURAL BIAS APPROACH TO CARDINAL SPLINE CURVES*
- `NASA_NTRS_Archive_19850020263` l.9: The cardinal spline approach to defining interpo latory curves has been of recent
- `NASA_NTRS_Archive_19850020263` l.41: T. have been defined we may write the cardinal spline curve V(s) as a collection of
- `cardinaldividear00noto` l.1: CARDINAL  DIVIDE  AREA  BASELINE  SURVEY
- `cardinaldividear00noto` l.50: Table  1 .  List  of  sampling  sites  during  the  Cardinal  Divide  survey,  1995-96.
- `cardinaldividear00noto` l.52: Table  2.  Water  quality  data  for  the  Cardinal  Divide  area,  1995-96.
- `micro_IA41152927_0526` l.8: TITLE Cardinal Principles Report: An Educational
- `micro_IA41152927_0526` l.22: IDENTIFIERS *Cardinal Principles Report
- `micro_IA41152927_0526` l.29: Secondary Education" (C.R.S.EF.), otherwise known as the Cardinal
- `ERIC_ED073079` l.30: Cardinal Principles Report: An Educational
- `ERIC_ED073079` l.43: ♦Cardinal Principles Report
- `ERIC_ED073079` l.50: Secondary Education" (C.R.S.E.)» otherwise known as the Cardinal
