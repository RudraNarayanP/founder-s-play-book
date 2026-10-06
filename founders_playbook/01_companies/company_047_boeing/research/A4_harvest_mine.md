# Harvest mining -- boeing

Window applied: 1916-01-01 .. 1940-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

102 candidate rows in the harvest index; 12 items mined; 90 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 8 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 4 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 0 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `boeing airplane company`, `boeing commercial airplane`; **other quoted terms** (predecessors, siblings, trade titles): `pacific aerospace`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `NASA_NTRS_Archive_19730003169` | 1972-01-01 / title:1973 | outside? MISMATCH | 507,591 | 17 | 3 | `boeing  company` | TIER1_CANDIDATE_TEXT |
| `NASA_NTRS_Archive_19740009636` | 1974-01-01 / title:1974 | outside? | 66,218 | 35 | 2 | `boeing commercial airplane` | TIER1_CANDIDATE_TEXT |
| `NASA_NTRS_Archive_19770008138` | 1976-01-01 / title:1977 | outside? MISMATCH | 663,754 | 17 | 4 | `boeing  co` | TIER1_CANDIDATE_TEXT |
| `NASA_NTRS_Archive_19730021280` | 1973-01-01 / title:1973 | outside? | 110,069 | 34 | 8 | `boeing company` | TIER1_CANDIDATE_TEXT |
| `NASA_NTRS_Archive_19750025089` | 1975-01-01 / title:1975 | outside? | 337,205 | 19 | 4 | `boeing  company` | TIER1_CANDIDATE_TEXT |
| `NASA_NTRS_Archive_19770013137` | 1976-01-01 / title:1977 | outside? MISMATCH | 351,487 | 25 | 4 | `boeing  company` | TIER1_CANDIDATE_TEXT |
| `NASA_NTRS_Archive_20050010183` | 1952-01-01 / title:2005 | outside? MISMATCH | 27,485 | 9 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19930092121` | 1952-01-01 / title:1993 | outside? MISMATCH | 43,684 | 7 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19770011174` | 1977-01-01 / title:1977 | outside? | 46,875 | 5 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19770008139` | 1976-01-01 / title:1977 | outside? MISMATCH | 1,203,968 | 17 | 5 | `boeing  co` | TIER1_CANDIDATE_TEXT |
| `NASA_NTRS_Archive_19750009268` | 1975-01-01 / title:1975 | outside? | 61,358 | 2 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19750012383` | 1975-01-01 / title:1975 | outside? | 279,401 | 165 | 5 | `boeing company` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `NASA_NTRS_Archive_19730003169` l.206: The  Boeing  Company
- `NASA_NTRS_Archive_19730003169` l.245: The  Boeing  Company
- `NASA_NTRS_Archive_19730003169` l.268: The  Boeing  Company
- `NASA_NTRS_Archive_19740009636` l.48: BOEING COMMERCIAL AIRPLANE COMPANY
- `NASA_NTRS_Archive_19740009636` l.77: Boeing Commercial Airplane Company
- `NASA_NTRS_Archive_19770008138` l.60: The  Boeing  Co.
- `NASA_NTRS_Archive_19770008138` l.108: The  Boeing  Co.
- `NASA_NTRS_Archive_19770008138` l.118: The  Boeing  Co.
- `NASA_NTRS_Archive_19730021280` l.40: BOEING VERTOL COMPANY
- `NASA_NTRS_Archive_19730021280` l.41: A Division of tha Boeing Company
- `NASA_NTRS_Archive_19730021280` l.258: BOEING VERTOL COMPANY
- `NASA_NTRS_Archive_19750025089` l.111: The  Boeing  Company
- `NASA_NTRS_Archive_19750025089` l.125: The  Boeing  Company
- `NASA_NTRS_Archive_19750025089` l.142: The  Boeing  Company
- `NASA_NTRS_Archive_19770013137` l.141: The  Boeing  Company
- `NASA_NTRS_Archive_19770013137` l.152: The  Boeing  Company
- `NASA_NTRS_Archive_19770013137` l.161: The  Boeing  Company
- `NASA_NTRS_Archive_20050010183` l.27: STRUCTURAL VULNERABILITY OP IHE BOEING B-29 AIRCRAFP
- `NASA_NTRS_Archive_20050010183` l.99: STRUCTURAL VULNERABILITY OF THE BOEING B-29 AIRCRAFT
- `NASA_NTRS_Archive_20050010183` l.110: of a B -29 airplane. The remaining inboard structure of the Boeing B-29
- `NASA_NTRS_Archive_19930092121` l.6: CHARACTERISTICS OF A BOEING B-29 AIRPLANE
- `NASA_NTRS_Archive_19930092121` l.60: CHARACTERISTICS OF A BOEING B-29 AIRPLANE
- `NASA_NTRS_Archive_19930092121` l.194: OF A BOEING B-29 AIRPLANE OF VARIATIONS IN STICK-FORCE AND
- `NASA_NTRS_Archive_19770011174` l.13: FREIGHT SYSTEMS UTILIZING A BOEING 747 AS THE TUG
- `NASA_NTRS_Archive_19770011174` l.18: , BOEING 747 AS THE TUG (NASA) 52 p HC A04/MF
- `NASA_NTRS_Archive_19770011174` l.60: UTILIZING A BOEING 747 AS THE TUG
- `NASA_NTRS_Archive_19770008139` l.55: The  Boeing  Co.
- `NASA_NTRS_Archive_19770008139` l.106: The  Boeing  Co.
- `NASA_NTRS_Archive_19770008139` l.121: The  Boeing  Co.
- `NASA_NTRS_Archive_19750009268` l.16: A BOEING 727 DURING TWO-SEGMENT AND NORMAL ILS APPROACHES
- `NASA_NTRS_Archive_19750009268` l.905: varying distances behind a Boeing 727-200 produced the following comments.
- `NASA_NTRS_Archive_19750012383` l.81: The Boeing Aerospace Company
- `NASA_NTRS_Archive_19750012383` l.82: A Division of The Boeing Company
- `NASA_NTRS_Archive_19750012383` l.3536: Test Description . The pattern tests will be conducted at the Boeing Company
