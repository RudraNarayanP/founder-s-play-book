# Harvest mining -- att

Window applied: 1885-01-01 .. 1984-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

67 candidate rows in the harvest index; 12 items mined; 48 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 0 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 3 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 2 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 1 | text held, zero hits. |
| `UNANSWERED` | 6 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `at t`; **other quoted terms** (predecessors, siblings, trade titles): `american telephone and telegraph`, `bell labs`, `southwestern bell`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `DTIC_ADA189360` | 1987-01-01 / title:1893 | in-window MISMATCH | 59,814 | 1 | 0 | - | BARE_WORD_MATCH |
| `somecommentsona00chicgoog` | 1908-01-01 / title:1907 | in-window MISMATCH | 60,341 | 0 | 0 | - | VARIANT_TERM_HIT |
| `report-of-a-conference-held-at-the-office-of-the-american-telephone-and-telegraph-company` | 1887-01-01 | in-window | 334,305 | 0 | 0 | - | VARIANT_TERM_HIT |
| `DTIC_ADA189269` | 1987-01-01 / title:1892 | in-window MISMATCH | 59,696 | 1 | 0 | - | BARE_WORD_MATCH |
| `annualreportofdi00amer_14` | 1914-01-01 | in-window | 136,506 | 0 | 0 | - | VARIANT_TERM_HIT |
| `DTIC_ADA197243` | 1987-01-01 / title:1972 | in-window MISMATCH | 57,073 | 0 | 0 | - | NULL |
| `birthbabyhoodoft00wats` | 1940-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `xEJbUdD0uBsC` | 1921-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `DFUSAQAAMAAJ` | 1901-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `KOBRAQAAMAAJ` | 1928-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `qYIphO8ACGAC` | 1925-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `2xVAAAAAYAAJ` | 1915-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `DTIC_ADA189360` l.17: S6-11-25-ATT
- `somecommentsona00chicgoog` l.408: the report of the American Telephone and Telegraph Company. The pub-
- `somecommentsona00chicgoog` l.735: obliged to pay tribute to the American Telephone and Telegraph Company
- `report-of-a-conference-held-at-the-office-of-the-american-telephone-and-telegraph-company` l.24: AMERICAN TELEPHONE AND. TELEGRAPH COMPANY. 2
- `report-of-a-conference-held-at-the-office-of-the-american-telephone-and-telegraph-company` l.90: AMERICAN TELEPHONE AND TELEGRAPH COMPANY,
- `report-of-a-conference-held-at-the-office-of-the-american-telephone-and-telegraph-company` l.2446: AMERICAN TELEPHONE AND TELEGRAPH Co.,
- `DTIC_ADA189269` l.9: 86-1 1-25 -ATT
- `annualreportofdi00amer_14` l.11: AMERICAN  TELEPHONE  AND  TELEGRAPH  COMPANY
- `annualreportofdi00amer_14` l.135: AMERICAN  TELEPHONE  AND  TELEGRAPH
- `annualreportofdi00amer_14` l.340: and  of  the  American  Telephone  and  Telegraph  Com¬
