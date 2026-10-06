# Harvest mining -- ford

Window applied: 1903-01-01 .. 1950-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

178 candidate rows in the harvest index; 12 items mined; 140 left untried at the --limit.

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

Entity vocabulary this pass applied -- **name phrases**: `ford motor`, `ford motor car company`, `ford motor company`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `McGillLibrary-635611-36509` | 1948-01-01 / title:1948 | in-window | 28,529 | 36 | 11 | `ford motor` | TIER1_CANDIDATE_TEXT |
| `McGillLibrary-635589-36440` | 1925-01-01 / title:1925 | in-window | 5,853 | 15 | 5 | `ford motor` | TIER1_CANDIDATE_TEXT |
| `McGillLibrary-635612-36512` | 1949-01-01 / title:1949 | in-window | 35,191 | 47 | 14 | `ford motor` | TIER1_CANDIDATE_TEXT |
| `McGillLibrary-635598-36467` | 1934-01-01 / title:1934 | in-window | 9,659 | 13 | 11 | `ford motor` | TIER1_CANDIDATE_TEXT |
| `McGillLibrary-635596-36461` | 1932-01-01 / title:1932 | in-window | 5,352 | 5 | 2 | `ford motor` | TIER1_CANDIDATE_TEXT |
| `McGillLibrary-635602-36479` | 1938-01-01 / title:1938 | in-window | 9,512 | 14 | 10 | `ford motor` | TIER1_CANDIDATE_TEXT |
| `McGillLibrary-635587-36434` | 1923-01-01 / title:1923 | in-window | 5,851 | 13 | 2 | `ford motor` | TIER1_CANDIDATE_TEXT |
| `McGillLibrary-635601-36476` | 1937-01-01 / title:1937 | in-window | 9,716 | 13 | 11 | `ford motor` | TIER1_CANDIDATE_TEXT |
| `McGillLibrary-635585-36428` | 1920-01-01 / title:1920 | in-window | 4,898 | 7 | 1 | `ford motor` | TIER1_CANDIDATE_TEXT |
| `McGillLibrary-635597-36464` | 1933-01-01 / title:1933 | in-window | 7,878 | 5 | 3 | `ford motor` | TIER1_CANDIDATE_TEXT |
| `McGillLibrary-635610-36503` | 1946-01-01 / title:1946 | in-window | 18,030 | 15 | 10 | `ford motor` | TIER1_CANDIDATE_TEXT |
| `McGillLibrary-635592-36449` | 1928-01-01 / title:1928 | in-window | 4,835 | 9 | 2 | `ford motor` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `McGillLibrary-635611-36509` l.149: To the Shareholders of Ford Motor Company of Canada, Limited:
- `McGillLibrary-635611-36509` l.185: mercial vehicles imported from Ford Motor Company, Limited, Dagenham,
- `McGillLibrary-635611-36509` l.285: industry in Canada, the factory of Ford Motor Company of Canada, Limited in Windsor, Ontario, occupies
- `McGillLibrary-635589-36440` l.64: FORD MOTOR COMPANY OF AUSTRALIA (PTY.) LIMITED
- `McGillLibrary-635589-36440` l.74: FORD MOTOR COMPANY OF SOUTH AFRICA, LIMITED
- `McGillLibrary-635589-36440` l.127: FORD MOTOR COMPAN\
- `McGillLibrary-635612-36512` l.16: FORD MOTOR COMPANY OF CANADA,
- `McGillLibrary-635612-36512` l.31: annual meeting of shareholders of Ford Motor Company
- `McGillLibrary-635612-36512` l.201: To the Shareholders of Ford Motor Company of Canada, Limited:
- `McGillLibrary-635598-36467` l.7: FORD MOTOR COMPANY OF CANADA
- `McGillLibrary-635598-36467` l.29: FORD MOTOR COMPANY OF CANADA, LIMITED
- `McGillLibrary-635598-36467` l.56: FORD MOTOR COMPANY OF CANADA, LIMITED
- `McGillLibrary-635596-36461` l.80: FORD MOTOR COMPAN'
- `McGillLibrary-635596-36461` l.123: We have audited the books and accounts of Ford Motor Company of Canada,
- `McGillLibrary-635602-36479` l.1: FORD MOTOR COMPANY OF CANADA,
- `McGillLibrary-635602-36479` l.28: FORD MOTOR COMPANY OF CANADA, LIMITED
- `McGillLibrary-635602-36479` l.61: FORD MOTOR COMPANY OF CANADA, LIMITED
- `McGillLibrary-635587-36434` l.97: FORD MOTOR COMPAN
- `McGillLibrary-635587-36434` l.124: We certify that we have audited the books and accounts of Ford Motor Company
- `McGillLibrary-635601-36476` l.1: FORD MOTOR COMPANY OF CANADA,
- `McGillLibrary-635601-36476` l.33: FORD MOTOR COMPANY OF CANADA,
- `McGillLibrary-635601-36476` l.63: FORD MOTOR COMPANY OF CANADA, LIMITED
- `McGillLibrary-635585-36428` l.65: FORD MOTOR COMPAD
- `McGillLibrary-635597-36464` l.71: Shareholders of Ford Motor Company of Canada, Limited,
- `McGillLibrary-635597-36464` l.159: FORD MOTOR COMPAN
- `McGillLibrary-635597-36464` l.224: We have audited the books and accounts of Ford Motor Company of Canada,
- `McGillLibrary-635610-36503` l.60: shareholders of Ford Motor Company of Canada, Limited will be held
- `McGillLibrary-635610-36503` l.150: Ford Motor Company of Malaya, Limited written
- `McGillLibrary-635610-36503` l.177: FORD MOTOR COMPAN
- `McGillLibrary-635592-36449` l.90: FORD MOTOR COMPAN
- `McGillLibrary-635592-36449` l.120: We certify that we have audited the books and accounts of Ford Motor Company
