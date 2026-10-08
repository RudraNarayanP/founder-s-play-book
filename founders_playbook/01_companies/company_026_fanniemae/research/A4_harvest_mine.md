# Harvest mining -- fanniemae

Window applied: 1938-01-01 .. 1970-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

75 candidate rows in the harvest index; 12 items mined; 58 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 0 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 5 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 3 | text held, zero hits. |
| `UNANSWERED` | 4 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `fannie mae`; **other quoted terms** (predecessors, siblings, trade titles): `federal national mortgage`, `federal national mortgage association`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `annualreport02assogoog` | 1968-01-01 | in-window | 522,671 | 0 | 0 | - | NULL |
| `annualreport05assogoog` | 1968-01-01 | in-window | 90,809 | 0 | 0 | - | NULL |
| `cia-readingroom-document-cia-rdp86t00268r000100010009-3` | 1957-01-01 | in-window | 92,277 | 0 | 0 | - | VARIANT_TERM_HIT |
| `cia-readingroom-document-cia-rdp80-01240a000500050007-6` | 1956-01-01 | in-window | 101,833 | 0 | 0 | - | VARIANT_TERM_HIT |
| `cia-readingroom-document-cia-rdp80-01240a000500050008-5` | 1953-01-01 | in-window | 114,910 | 0 | 0 | - | VARIANT_TERM_HIT |
| `cia-readingroom-document-cia-rdp80-01240a000500050014-8` | 1952-01-01 | in-window | 70,287 | 0 | 0 | - | VARIANT_TERM_HIT |
| `cia-readingroom-document-cia-rdp65b00383r000300150002-6` | 1963-01-01 | in-window | 33,975 | 0 | 0 | - | NULL |
| `cia-readingroom-document-cia-rdp80-01240a000500060012-9` | 1964-01-01 | in-window | 125,202 | 0 | 0 | - | VARIANT_TERM_HIT |
| `GfIrbypRXbQC` | 2006-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `7Anqx6v08sEC` | 1996-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `iD8-bWporl8C` | 2007-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `bEHadqS9X-YC` | 1996-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `cia-readingroom-document-cia-rdp86t00268r000100010009-3` l.831: Federal National Mortgage Association (net):
- `cia-readingroom-document-cia-rdp86t00268r000100010009-3` l.1870: Federal National Mortgage Association:
- `cia-readingroom-document-cia-rdp86t00268r000100010009-3` l.1984: Federal National Mortgage Association:
- `cia-readingroom-document-cia-rdp80-01240a000500050007-6` l.237: 39) President of the Federal National Mortgage Association.
- `cia-readingroom-document-cia-rdp80-01240a000500050008-5` l.305: (89) President of the Federal National Mortgage Association.
- `cia-readingroom-document-cia-rdp80-01240a000500050014-8` l.1197: “Federal National Mortgage Association” (increase of $244,000
- `cia-readingroom-document-cia-rdp80-01240a000500060012-9` l.2098: (95) President of the Federal National Mortgage Association.
