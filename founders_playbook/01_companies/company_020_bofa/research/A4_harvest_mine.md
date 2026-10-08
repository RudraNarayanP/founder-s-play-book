# Harvest mining -- bofa

Window applied: 1791-01-01 .. 1998-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

122 candidate rows in the harvest index; 12 items mined; 93 left untried at the --limit.

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

Entity vocabulary this pass applied -- **name phrases**: `bank of america`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `bankofamericadat2619sanf` | 1977-01-01 | in-window | 342,480 | 0 | 50 | `bank  of  america` | TIER1_CANDIDATE_TEXT |
| `01-bank-of-america-bac` | 1998-01-01 | in-window | 1,332,198 | 7 | 200 | `bank of america` | TIER1_CANDIDATE_TEXT |
| `micro_IA41153448_0117` | 1981-01-01 | in-window | 31,005 | 0 | 4 | `bank of america` | TIER1_CANDIDATE_TEXT |
| `micro_IA41153448_0114` | 1983-01-01 | in-window | 15,855 | 0 | 4 | `bank of america` | TIER1_CANDIDATE_TEXT |
| `micro_IA41153448_0115` | 1983-01-01 | in-window | 17,172 | 0 | 4 | `bank of america` | TIER1_CANDIDATE_TEXT |
| `micro_IA41153448_0111` | 1982-01-01 | in-window | 28,708 | 0 | 4 | `bank of america` | TIER1_CANDIDATE_TEXT |
| `micro_IA41153448_0106` | 1983-01-01 | in-window | 33,346 | 0 | 5 | `bank of america` | TIER1_CANDIDATE_TEXT |
| `micro_IA41153448_0108` | 1983-01-01 | in-window | 33,213 | 0 | 4 | `bank of america` | TIER1_CANDIDATE_TEXT |
| `micro_IA41153448_0105` | 1980-01-01 | in-window | 19,410 | 0 | 5 | `bank of america` | TIER1_CANDIDATE_TEXT |
| `micro_IA41153448_0112` | 1980-01-01 | in-window | 15,446 | 0 | 5 | `bank of america` | TIER1_CANDIDATE_TEXT |
| `micro_IA41153448_0116` | 1981-01-01 | in-window | 32,428 | 0 | 4 | `bank of america` | TIER1_CANDIDATE_TEXT |
| `micro_IA41153448_0107` | 1982-01-01 | in-window | 30,706 | 0 | 8 | `bank of america` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `bankofamericadat2619sanf` l.13: ^  BANK  OF  AMERICA  DATA  PROCESSING  CENTER
- `bankofamericadat2619sanf` l.114: Bank  of  America  data
- `bankofamericadat2619sanf` l.303: The  proposed  Bank  of  America  data  center  parking  structure  would  provide  about
- `01-bank-of-america-bac` l.1: Bank of America a
- `01-bank-of-america-bac` l.4: Bank of America Corporation
- `01-bank-of-america-bac` l.51: This is Bank of America
- `micro_IA41153448_0117` l.8: INSTITUTION Bank of America NT & SA, San Francisco, CA.
- `micro_IA41153448_0117` l.305: COPYRIGHT © BANK OF AMERICA NTASA 1981
- `micro_IA41153448_0117` l.1174: Prepared by Bank of America, Box 37128, San Francisco, California 94137
- `micro_IA41153448_0114` l.8: INSTITUTION Bank of America NT & SA, San Francisco, CA.
- `micro_IA41153448_0114` l.14: AVAILABLE FROM Bank of America, Dept. 3401, Box 37128, San
- `micro_IA41153448_0114` l.285: BANK OF AMERICA NT&S A 1979. 1980. 1981. 1983
- `micro_IA41153448_0115` l.15: INSTITUTION Bank of America NT & SA, San Francisco, CA.
- `micro_IA41153448_0115` l.311: COPYRIGHT © BANK OF AMERICA NT&SA 1979, 1961, 1983
- `micro_IA41153448_0115` l.566: Prepared by Bank of America, Box 37128, San Francisco, California 94137 (3)
- `micro_IA41153448_0111` l.8: INSTITUTION Bank of America NT & SA, San Francisco, CA.
- `micro_IA41153448_0111` l.280: BANK OF AMERICA NTASA 1977, 1978. 1979. 1980 198). 1982
- `micro_IA41153448_0111` l.938: Prepared by Bank of America, Box 37128, San Francisco, California 94137 (ER)
- `micro_IA41153448_0106` l.8: INSTITUTION Bank of America NT & SA, San Francisco, CA.
- `micro_IA41153448_0106` l.14: AVAILABLE FROM Bank of America, Dept. 3401, Box 37128, San
- `micro_IA41153448_0106` l.288: COPYRIGHT © BANK OF AMERICA NTA&SA 1979 1981, 1983
- `micro_IA41153448_0108` l.9: INSTITUTION Bank of America NT & SA, San Francisco, CA,
- `micro_IA41153448_0108` l.299: COPYRIGHT © BANK OF AMERICA NTASA 1976, 1979, 1980. 1982, 1963 ya
- `micro_IA41153448_0108` l.1078: Prepared by Bank of America, Box 37128, San Francisco, California 94137 Ui
- `micro_IA41153448_0105` l.31: Bank of America NT & SA, San Francisco,
- `micro_IA41153448_0105` l.35: Bank of America, Dept. 3401, Box 37128, San
- `micro_IA41153448_0105` l.315: COPYRIGHT © BANK OF AMERICA NT & SA 1977. 1980
- `micro_IA41153448_0112` l.31: Bank of America NT & SA, San Francisco, CA.
- `micro_IA41153448_0112` l.36: Bank of America, Dept. 3401, Box 37128, San
- `micro_IA41153448_0112` l.304: COPYRIGHT © BANK OF AMERICA NT&SA 1978. 1980
- `micro_IA41153448_0116` l.8: INSTITUTION Bank of America NT & SA, San Francisco, CA.
- `micro_IA41153448_0116` l.280: COPYRIGHT © BANK OF AMERICA NT&SA 1981
- `micro_IA41153448_0116` l.1066: Prepared by Bank of America, Box 37128, San Francisco, California 94137 (BR)
- `micro_IA41153448_0107` l.8: INSTITUTION Bank of America NT & SA, San Francisco, CA.
- `micro_IA41153448_0107` l.14: AVAILABLE FROM Bank of America, Dept. 3401, Box 37128, San
- `micro_IA41153448_0107` l.27: IDENTIFIERS Bank of America; *Checking Accounts; PF Project
