# Harvest mining -- microsoft

Window applied: 1975-01-01 .. 1986-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

30 candidate rows in the harvest index; 4 items mined; 24 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 3 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 1 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `micro soft`, `microsoft corporation`; **other quoted terms** (predecessors, siblings, trade titles): `five and dime`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `01-microsoft-annual-reports` | 1975-01-01 | in-window | 295,724 | 107 | 23 | `microsoft corporation`, `microsoft software` | TIER1_CANDIDATE_TEXT |
| `ty8EAAAAMBAJ` | 1983-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `byte-magazine-1980-12` | 1980-01-01 | in-window | 1,669,324 | 129 | 2 | `micro soft`, `microsoft. inc` | TIER1_CANDIDATE_TEXT |
| `byte-magazine-1982-03` | 1982-01-01 | in-window | 2,072,713 | 134 | 4 | `micro soft`, `microsoft inc`, `microsoft, inc` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `01-microsoft-annual-reports` l.531: Microsoft Corporation
- `01-microsoft-annual-reports` l.542: Among Microsoft Corporation, the S&P 500 Index,
- `01-microsoft-annual-reports` l.1471: intended to help the reader understand the results of operations and financial condition of Microsoft Corporation. MD8A is
- `byte-magazine-1980-12` l.75599: Micro Soft Z-80 Software Card
- `byte-magazine-1982-03` l.42890: show you how to sell your own micro soft-
