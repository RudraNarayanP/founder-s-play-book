# Harvest mining -- pepsico

Window applied: 1898-01-01 .. 1965-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

43 candidate rows in the harvest index; 12 items mined; 21 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 9 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 1 | text held, zero hits. |
| `UNANSWERED` | 2 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `pepsi cola`; **other quoted terms** (predecessors, siblings, trade titles): `progressive grocer`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `01-pepsi-co` | 1938-01-01 / title:1938 | in-window | 520,419 | 200 | 17 | `pepsi-cola`, `pepsico, inc` | TIER1_CANDIDATE_TEXT |
| `cor5_0_s06_ss01_boxrg5_0_2008_006_f61` | 1948-01-01 | in-window | 20,875 | 25 | 25 | `pepsi-cola` | TIER1_CANDIDATE_TEXT |
| `twelvefullounces0000mart` | 1962-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `NPTG19060630` | 1906-01-01 / title:1906 | in-window | 196,947 | 0 | 0 | - | NULL |
| `pepsicofritolayannualreports` | ? / title:1938 | in-window | 795,597 | 12 | 8 | `pepsico,  inc` | TIER1_CANDIDATE_TEXT |
| `1974-12-press-release` | 1974-01-01 | outside? | 3,209 | 2 | 2 | `pepsi cola` | TIER1_CANDIDATE_TEXT |
| `report-100-of-corn-in-frito-lay-sun-chips-completely-gmo` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `pepsi-co-inc.-pep-annual-report-2020` | 2021-01-01 | outside? | 448,866 | 200 | 17 | `pepsi-cola`, `pepsico, inc` | TIER1_CANDIDATE_TEXT |
| `pepsi-co-inc.-pep-proxy-statement-2022-05-04` | 2022-01-01 | outside? | 451,194 | 200 | 17 | `pepsi-cola`, `pepsico, inc` | TIER1_CANDIDATE_TEXT |
| `pepsi-co-inc.-pep-proxy-statement-2024-05-01` | 2024-01-01 | outside? | 580,431 | 200 | 8 | `pepsico stock`, `pepsico, inc` | TIER1_CANDIDATE_TEXT |
| `pepsi-co-inc.-pep-proxy-statement-2020-05-06` | 2020-01-01 / title:2019 | outside? MISMATCH | 510,463 | 200 | 17 | `pepsi-cola`, `pepsico, inc` | TIER1_CANDIDATE_TEXT |
| `pepsi-co-inc.-pep-proxy-statement-2023-05-03` | 2023-01-01 | outside? | 470,741 | 200 | 15 | `pepsi-cola`, `pepsico, inc` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `01-pepsi-co` l.122: Two years later, in 1965, Frito-Lay and Pepsi-Cola merged
- `01-pepsi-co` l.1366: Lay, Gatorade, Pepsi-Cola, Quaker and Tropicana. Through our operations, authorized bottlers, contract
- `01-pepsi-co` l.3080: environmental control authority, began an audit of a bottling plant of our subsidiary, Pepsi-Cola General
- `cor5_0_s06_ss01_boxrg5_0_2008_006_f61` l.5: PEPSI-COLA COMPANY’S
- `cor5_0_s06_ss01_boxrg5_0_2008_006_f61` l.121: Pepsi-Cola Company is happy to give recognition and encouragement to these
- `cor5_0_s06_ss01_boxrg5_0_2008_006_f61` l.131: hibition of the Pepsi-Cola Achievement Award Medal, designed by the noted
- `pepsicofritolayannualreports` l.2216: Corporation,  PepsiCo,  Inc.,  Starbucks  Corporation,  The  Coca-Cola  Company  and  The  Procter  &  Gamble
- `pepsicofritolayannualreports` l.2244: Depot,  OfficeMax  Incorporated,  PepsiCo,  Inc.,  Staples,  Inc.  and  Walgreen  Co.
- `pepsicofritolayannualreports` l.2246: (3)  Includes  Colgate-Palmolive  Company,  Kellogg  Company,  McDonald’s  Corporation,  PepsiCo,  Inc.,
- `1974-12-press-release` l.25: SPONSORED BY PEPSI COLA CANADA LTD.
- `1974-12-press-release` l.34: This year's tourney will be sponsored by Pepsi Cola Canada Ltd.
- `pepsi-co-inc.-pep-annual-report-2020` l.1208: Lay, Gatorade, Pepsi-Cola, Quaker and Tropicana. Through our operations, authorized bottlers, contract
- `pepsi-co-inc.-pep-annual-report-2020` l.2560: Operations from 2009 to 2010, President of Pepsi-Cola North America from 2007 to 2009, Executive Vice
- `pepsi-co-inc.-pep-annual-report-2020` l.2849: including Frito-Lay, Gatorade, Pepsi-Cola, Quaker and Tropicana. Through our operations, authorized
- `pepsi-co-inc.-pep-proxy-statement-2022-05-04` l.1260: including Lays, Doritos, Cheetos, Gatorade, Pepsi-Cola, Mountain Dew, Quaker and SodaStream.
- `pepsi-co-inc.-pep-proxy-statement-2022-05-04` l.2701: Operations from 2009 to 2010, President of Pepsi-Cola North America from 2007 to 2009, Executive Vice
- `pepsi-co-inc.-pep-proxy-statement-2022-05-04` l.2948: brands, including Lays, Doritos, Cheetos, Gatorade, Pepsi-Cola, Mountain Dew, Quaker and SodaStream.
- `pepsi-co-inc.-pep-proxy-statement-2024-05-01` l.321: PepsiCo, Inc. Long-Term Incentive Plan.
- `pepsi-co-inc.-pep-proxy-statement-2024-05-01` l.444: Director Independence 28 Approval of the Amended and Restated PepsiCo, Inc.
- `pepsi-co-inc.-pep-proxy-statement-2024-05-01` l.459: Appendix B-PepsiCo, Inc. Long-Term Incentive Plan B-1
- `pepsi-co-inc.-pep-proxy-statement-2020-05-06` l.1374: Pepsi-Cola, Quaker and Tropicana. Through our operations, authorized bottlers, contract manufacturers and
- `pepsi-co-inc.-pep-proxy-statement-2020-05-06` l.3282: 2010, President of Pepsi-Cola North America from 2007 to 2009, Executive Vice President, Operations from
- `pepsi-co-inc.-pep-proxy-statement-2020-05-06` l.4110: Frito-Lay, Gatorade, Pepsi-Cola, Quaker and Tropicana. Through our operations, authorized bottlers, contract
- `pepsi-co-inc.-pep-proxy-statement-2023-05-03` l.1266: including Lay’s, Doritos, Cheetos, Gatorade, Pepsi-Cola, Mountain Dew, Quaker and SodaStream.
- `pepsi-co-inc.-pep-proxy-statement-2023-05-03` l.2709: Operations from 2009 to 2010, President of Pepsi-Cola North America from 2007 to 2009, Executive Vice
- `pepsi-co-inc.-pep-proxy-statement-2023-05-03` l.2982: brands, including Lay’s, Doritos, Cheetos, Gatorade, Pepsi-Cola, Mountain Dew, Quaker and SodaStream.
