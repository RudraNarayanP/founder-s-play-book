# Harvest mining -- jpmorgan

Window applied: 1799-01-01 .. 1960-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

93 candidate rows in the harvest index; 12 items mined; 80 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 2 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 7 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 3 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `chase manhattan`, `jpmorgan chase`; **other quoted terms** (predecessors, siblings, trade titles): `successor by merger`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `NPDP19340704` | 1934-01-01 / title:1934 | in-window | 292,253 | 9 | 0 | - | BARE_WORD_MATCH |
| `NPDP19360702` | 1936-01-01 / title:1936 | in-window | 291,106 | 12 | 0 | - | BARE_WORD_MATCH |
| `armstrong-george-third-zionist-war` | 1951-01-01 | in-window | 144,610 | 9 | 0 | - | BARE_WORD_MATCH |
| `chasechasemanhat0000wils` | 1986-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `NPDP19230426` | 1923-01-01 / title:1923 | in-window | 207,783 | 6 | 2 | `morgan co`, `morgan company` | TIER1_CANDIDATE_TEXT |
| `NPDP19250817` | 1925-01-01 / title:1925 | in-window | 200,658 | 6 | 0 | - | BARE_WORD_MATCH |
| `NPCM19271228` | 1927-01-01 / title:1927 | in-window | 244,913 | 17 | 0 | - | BARE_WORD_MATCH |
| `NPCM19370823` | 1937-01-01 / title:1937 | in-window | 106,307 | 2 | 0 | - | BARE_WORD_MATCH |
| `sim_business-in-brief_1957-07_16` | 1957-01-01 / title:1957 | in-window | 24,281 | 4 | 2 | `chase manhattan` | TIER1_CANDIDATE_TEXT |
| `letterfrommessrs00jpmorich` | 1913-01-01 | in-window | 46,581 | 6 | 0 | - | BARE_WORD_MATCH |
| `XS6wCQAAQBAJ` | 2009-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `-2slEQAAQBAJ` | 2024-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `NPDP19340704` l.1057: ‘Savio in 'thé"chase and dg “the
- `NPDP19340704` l.1144: rier who chased the gang, recelved
- `NPDP19340704` l.2350: IEP: MORGAN & co.
- `NPDP19360702` l.200: J. P. MORGAN IS
- `NPDP19360702` l.209: “Mr J. Pierpont Morgan, who is
- `NPDP19360702` l.1496: Chase Nat. Bk. ...... 432
- `armstrong-george-third-zionist-war` l.54: 2. That the members of the firms of J. P. Morgan & Co.,
- `armstrong-george-third-zionist-war` l.908: Chinese War. That is the program of J. P. Morgan & Co., Kuhn,
- `armstrong-george-third-zionist-war` l.1607: of J. P. Morgan & Co., as Secretary of State; Henry Stimson, at-
- `NPDP19230426` l.5447: PARTNER OF J: P."MORGAN CO.
- `NPDP19230426` l.5455: ‘partter of tho J. Po Morgan Company,
- `NPDP19250817` l.63: "Fer thp Purchase, sage aac Oa fer
- `NPDP19250817` l.2281: ‘Owing to..the .purchases: effected by:
- `NPDP19250817` l.2325: “On General, Chang's arrival'at, Tsing; | tained by the, people.” - large -purchases for Shanghai ond Tien-| not. theft, ‘and. Mr.’McCallum asked His .
- `NPCM19271228` l.1697: government to limit its purchases
- `NPCM19271228` l.1730: purchases made through the bureau
- `NPCM19271228` l.1738: they could make their purchases
- `NPCM19370823` l.2470: J . MORGAN. w
- `NPCM19370823` l.2476: ohn Pierpoint Morgan, the _
- `sim_business-in-brief_1957-07_16` l.16: THE CHASE MANHATTAN BANK
- `sim_business-in-brief_1957-07_16` l.1002: Chase Manhattan, a leader in
- `letterfrommessrs00jpmorich` l.24: ^  J.  P.  Morgan  &  Co.,
- `letterfrommessrs00jpmorich` l.42: Letter  from  Messrs.  J.  P.  Morgan  &  Co.,  in  response  to  the
- `letterfrommessrs00jpmorich` l.294: It  has  often  been  observed  that  Mr.  Morgan  aided
