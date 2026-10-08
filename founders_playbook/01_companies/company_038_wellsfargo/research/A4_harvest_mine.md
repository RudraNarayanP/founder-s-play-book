# Harvest mining -- wellsfargo

Window applied: 1852-01-01 .. 1998-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

85 candidate rows in the harvest index; 12 items mined; 69 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 2 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 10 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `wells fargo`, `wells fargo bank`, `wells fargo company`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `01.-wells-fargo-annual-report-archive` | 1919-01-01 / title:1919 | in-window | 1,195,717 | 6 | 200 | `wells fargo` | TIER1_CANDIDATE_TEXT |
| `TFQYD05NX58C` | 1901-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `6H4pAAAAYAAJ` | 1919-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `v0MaAQAAIAAJ` | 1920-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `W0ocAQAAIAAJ` | 1915-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `vC4wAQAAMAAJ` | 1910-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `muvrWlWDX7sC` | 1912-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `DxcDAAAAYAAJ` | 1915-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `wellsfargoadvanc0000edwa_s8g6` | 1949-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `wellsfargo0000ralp` | 1961-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `NPDP19380212` | 1938-01-01 / title:1938 | in-window | 282,316 | 0 | 5 | `wells fargo` | TIER1_CANDIDATE_TEXT |
| `wellsfargonevada1988davi` | 1988-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `01.-wells-fargo-annual-report-archive` l.1: Cover: Wells Fargo customer Erik Gruber outside his new home in Philadelphia. Learn more on page 34.
- `01.-wells-fargo-annual-report-archive` l.46: Wells Fargo Board of Directors, Iam encouraged
- `01.-wells-fargo-annual-report-archive` l.48: have made as we build a better Wells Fargo for
- `NPDP19380212` l.4008: “Wells Fargo.”
- `NPDP19380212` l.4019: “Wells Fargo.”
- `NPDP19380212` l.4045: WELLS FARGO
