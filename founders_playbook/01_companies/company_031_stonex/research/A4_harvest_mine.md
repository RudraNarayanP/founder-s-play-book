# Harvest mining -- stonex

Window applied: 1984-01-01 .. 2000-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

109 candidate rows in the harvest index; 12 items mined; 95 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 0 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 3 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 2 | text held, zero hits. |
| `UNANSWERED` | 7 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `formerly known as stonex`, `stonex group`; **other quoted terms** (predecessors, siblings, trade titles): `formerly known as`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `quintetinmajork50000rudo` | 1986-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `isbn_9789686769388` | 1997-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `isbn_9780892140244_50` | 2000-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `isbn_9780793301386` | 1990-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `cia-readingroom-document-cia-rdp75b00380r000800070007-4` | 2000-01-01 | in-window | 1,324 | 2 | 0 | - | BARE_WORD_MATCH |
| `cia-readingroom-document-cia-rdp87t00758r000101580001-3` | 1987-01-01 / title:1986 | in-window MISMATCH | 64,706 | 4 | 0 | - | BARE_WORD_MATCH |
| `cia-readingroom-document-cia-rdp88t00539r000100070004-9` | 1986-01-01 | in-window | 20,530 | 1 | 0 | - | BARE_WORD_MATCH |
| `cia-readingroom-document-cia-rdp88-00798r000600080002-8` | 1987-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `cia-readingroom-document-cia-rdp71t00730r000600100133-9` | 2000-01-01 | in-window | 1,211 | 0 | 0 | - | NULL |
| `micro_IA40243801_1055` | 1990-01-01 | in-window | 951 | 0 | 0 | - | NULL |
| `us-sprint-geo-rus` | 1990-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `1994annualbookof0000unse` | 1994-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `cia-readingroom-document-cia-rdp75b00380r000800070007-4` l.54: STATINTL tices in Government.
- `cia-readingroom-document-cia-rdp75b00380r000800070007-4` l.71: ae ein STATINTL
- `cia-readingroom-document-cia-rdp87t00758r000101580001-3` l.822: AUGUSTO CESAR SANDINO INTL AIRFIELD NU NPC CA $00112888
- `cia-readingroom-document-cia-rdp87t00758r000101580001-3` l.1647: 05D AUGUSTO CESAR SANDINO INTL AIRFIELD NU NpC CA $C-628827-86 $039112888 25x1
- `cia-readingroom-document-cia-rdp87t00758r000101580001-3` l.2061: 35€ AUGUSTO CESAR SANDINO INTL AIRFIELD NU NPC CA 50011288
- `cia-readingroom-document-cia-rdp88t00539r000100070004-9` l.693: DEPUTY ASSISTANT SECRETARY FOR INTL
