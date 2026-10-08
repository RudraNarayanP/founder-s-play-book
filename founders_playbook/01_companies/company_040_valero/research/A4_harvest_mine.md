# Harvest mining -- valero

Window applied: 1979-01-01 .. 2001-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

15 candidate rows in the harvest index; 12 items mined; 1 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 2 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 3 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 7 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `formerly known as valero`, `valero energy`, `valero energy corporation`; **other quoted terms** (predecessors, siblings, trade titles): `diamond shamrock`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `ANA-DIG-THENEWSARUBA-D0216-05-20051104-DOC` | 2005-01-01 | outside? | 1,993 | 5 | 0 | - | BARE_WORD_MATCH |
| `ANA-DIG-THENEWSARUBA-D0046-01-20050903-DOC` | 2005-01-01 | outside? | 3,175 | 9 | 0 | - | BARE_WORD_MATCH |
| `6382447-Valero-Benicia-Exceedance-Investigation-Report` | 2019-01-01 | outside? | 10,553 | 10 | 0 | - | BARE_WORD_MATCH |
| `gov.uscourts.cand.173961` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.laed.144436` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.tnwd.97261` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `ANA-DIG-THENEWSARUBA-D0072-03-20060209-DOC` | 2006-01-01 | outside? | 3,446 | 14 | 3 | `valero employees`, `valero energy` | TIER1_CANDIDATE_TEXT |
| `gov.uscourts.cacd.793552` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.laed.135477` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.oked.17485` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.txnd.248740` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `ANA-DIG-THENEWSARUBA-D0078-05-20070214-DOC` | 2007-01-01 | outside? | 8,097 | 27 | 3 | `valero corporation`, `valero energy` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `ANA-DIG-THENEWSARUBA-D0216-05-20051104-DOC` l.1: Valero Refinery Aruba is hiring!
- `ANA-DIG-THENEWSARUBA-D0216-05-20051104-DOC` l.3: of the opportunity to get a job at the Valero Refinery this past Thursday and Friday. David Smith,
- `ANA-DIG-THENEWSARUBA-D0216-05-20051104-DOC` l.4: Community and Government Affairs Director for Valero stated they expected to take applications and
- `ANA-DIG-THENEWSARUBA-D0046-01-20050903-DOC` l.8: day of golf was donated by of Tierra del Sol, while Valero Refinery donated the trophies and dinner.
- `ANA-DIG-THENEWSARUBA-D0046-01-20050903-DOC` l.9: The “Aruba Way” is a charitable program sponsored by Valero Refinery Aruba, which gets its main funds
- `ANA-DIG-THENEWSARUBA-D0046-01-20050903-DOC` l.10: from donations made by Valero Refinery employees. They specify a percentage of their salaries to be
- `6382447-Valero-Benicia-Exceedance-Investigation-Report` l.3: Valero'
- `6382447-Valero-Benicia-Exceedance-Investigation-Report` l.6: Valero Benicia Refinery
- `6382447-Valero-Benicia-Exceedance-Investigation-Report` l.15: I, 000 ppm ("Incident"). Valero Benicia Refinery ("Valero" or "Refinery") promptly shutdown the Fluid
- `ANA-DIG-THENEWSARUBA-D0072-03-20060209-DOC` l.28: Valero Energy Corporation, A Fortune 500 Company based out of San Antonio, Texas has already awarded
- `ANA-DIG-THENEWSARUBA-D0078-05-20070214-DOC` l.1: CEO and Chairman of Valero Energy Corporation, Bill Klesse, clarifies the position of
- `ANA-DIG-THENEWSARUBA-D0078-05-20070214-DOC` l.3: Oranjestad, February 14, 2007-The CEO and Chairman of Valero Energy Corporation, Mr. Bill
