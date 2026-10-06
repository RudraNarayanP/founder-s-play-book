# Harvest mining -- berkshire

Window applied: 1962-01-01 .. 1978-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

122 candidate rows in the harvest index; 12 items mined; 87 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 7 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 3 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 2 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `berkshire hathaway`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `berkshire-hathaway-brk-annual-report-1972` | 1973-01-01 / title:1972 | in-window MISMATCH | 56,586 | 54 | 54 | `berkshire hathaway`, `hathaway inc` | TIER1_CANDIDATE_TEXT |
| `berkshire-hathaway-brk-annual-report-1974` | 1975-01-01 / title:1974 | in-window MISMATCH | 105,518 | 69 | 63 | `berkshire hathaway`, `hathaway inc` | TIER1_CANDIDATE_TEXT |
| `berkshirehathawa0000stan` | 1962-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `annualberkshirevt1978` | 1978-01-01 / title:1978 | in-window | 127,132 | 52 | 0 | - | BARE_WORD_MATCH |
| `CAT88901059` | 1976-01-01 | in-window | 655,541 | 200 | 0 | - | BARE_WORD_MATCH |
| `CAT31444852` | 1977-01-01 | in-window | 14,032 | 1 | 0 | - | BARE_WORD_MATCH |
| `berkshireridgewa0000unse` | 1971-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `berkshire-hathaway-brk-annual-report-1988` | 1989-01-01 / title:1988 | outside? MISMATCH | 248,407 | 190 | 52 | `berkshire hathaway`, `berkshire shares`, `hathaway inc` | TIER1_CANDIDATE_TEXT |
| `berkshire-hathaway-brk-annual-report-1996` | 1997-01-01 / title:1996 | outside? MISMATCH | 231,608 | 200 | 37 | `berkshire hathaway`, `berkshire shares`, `hathaway inc` | TIER1_CANDIDATE_TEXT |
| `1997-berkshire-hathaway-annual-report` | 1998-01-01 / title:1997 | outside? MISMATCH | 253,519 | 200 | 44 | `berkshire hathaway`, `berkshire shares`, `berkshire stock`, `hathaway inc` | TIER1_CANDIDATE_TEXT |
| `berkshire-hathaway-1994-annual-report` | 1995-01-01 / title:1994 | outside? MISMATCH | 195,254 | 179 | 41 | `berkshire hathaway`, `berkshire stock`, `hathaway inc` | TIER1_CANDIDATE_TEXT |
| `berkshire-hathaway-annual-report-1982` | 1983-01-01 / title:1982 | outside? MISMATCH | 209,932 | 138 | 51 | `berkshire hathaway`, `hathaway inc` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `berkshire-hathaway-brk-annual-report-1972` l.1: BERKSHIRE HATHAWAY unc.
- `berkshire-hathaway-brk-annual-report-1972` l.19: 5-10 Berkshire Hathaway Inc. and Consolidated Subsidiary
- `berkshire-hathaway-brk-annual-report-1972` l.29: Berkshire Hathaway Inc.
- `berkshire-hathaway-brk-annual-report-1974` l.1: BERKSHIRE HATHAWAY inc.
- `berkshire-hathaway-brk-annual-report-1974` l.10: Berkshire Hathaway Inc.
- `berkshire-hathaway-brk-annual-report-1974` l.34: 6 Accountants’ Certificate Regarding Financial Statements of Berkshire Hathaway Inc.
- `annualberkshirevt1978` l.70: Berkshire, Vermont
- `annualberkshirevt1978` l.79: BERKSHIRE
- `annualberkshirevt1978` l.192: The legally qualified voters of the Town of Berkshire and the Town School District
- `CAT88901059` l.10: BERKSHIRE  REGION  REPORT
- `CAT88901059` l.49: report  presents  the  results  of  that  study  on  the  Berkshire  Region  which
- `CAT88901059` l.86: BERKSHIRE  REGION
- `CAT31444852` l.56: _ Dale E. Hathaway;-at the Annual Summer Meeting of Great Plains Wheat, in Wichita,
- `berkshire-hathaway-brk-annual-report-1988` l.1: BERKSHIRE HATHAWAY INC.
- `berkshire-hathaway-brk-annual-report-1988` l.115: BERKSHIRE HATHAWAY INC. and its subsidiaries engage in a number of diverse business activities.
- `berkshire-hathaway-brk-annual-report-1988` l.139: Shareholders of Berkshire Hathaway Inc. in the 1983 Annual Report. Because the material remains
- `berkshire-hathaway-brk-annual-report-1996` l.1: BERKSHIRE HATHAWAY unc.
- `berkshire-hathaway-brk-annual-report-1996` l.11: Berkshire Hathaway Inc. is a holding company owning subsidiaries engaged
- `berkshire-hathaway-brk-annual-report-1996` l.15: ‘report as the Berkshire Hathaway Insurance Group. Included in this group of
- `1997-berkshire-hathaway-annual-report` l.11: Berkshire Hathaway Inc. is a holding company owning subsidiaries engaged
- `1997-berkshire-hathaway-annual-report` l.33: Additionally, Berkshire Hathaway Inc. publishes the Buffalo News, a daily
- `1997-berkshire-hathaway-annual-report` l.43: world (FlightSafety International). On January 7, 1998, Berkshire Hathaway
- `berkshire-hathaway-1994-annual-report` l.4: Berkshire Hathaway Inc. is a holding company owning subsidiaries engaged
- `berkshire-hathaway-1994-annual-report` l.8: report as the Berkshire Hathaway Insurance Group.
- `berkshire-hathaway-1994-annual-report` l.25: Additionally, Berkshire Hathaway Inc. publishes the Buffalo News, a daily
- `berkshire-hathaway-annual-report-1982` l.1: BERKSHIRE HATHAWAY wc.
- `berkshire-hathaway-annual-report-1982` l.8: Berkshire Hathaway Inc.
- `berkshire-hathaway-annual-report-1982` l.42: A compilation of the letters from the principal executives of Berkshire Hathaway Inc. and Blue Chip
