# Harvest mining -- chevron

Window applied: 1879-01-01 .. 1984-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

138 candidate rows in the harvest index; 12 items mined; 114 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 1 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 11 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 0 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `chevron corporation`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `NASA_NTRS_Archive_19840005539` | 1983-01-01 / title:1984 | in-window MISMATCH | 80,955 | 65 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19780024484` | 1978-01-01 / title:1978 | in-window | 19,542 | 55 | 0 | - | BARE_WORD_MATCH |
| `01-chevron-cover` | 1920-01-01 / title:1920 | in-window | 429,532 | 200 | 107 | `chevron corporation`, `chevron employees` | TIER1_CANDIDATE_TEXT |
| `NASA_NTRS_Archive_19840025763` | 1984-01-01 / title:1984 | in-window | 67,504 | 147 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19840021180` | 1984-01-01 / title:1984 | in-window | 38,244 | 59 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19830011631` | 1983-01-01 / title:1983 | in-window | 16,834 | 26 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19800023978` | 1980-01-01 / title:1980 | in-window | 20,157 | 42 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_20080012230` | 1977-01-01 / title:2008 | in-window MISMATCH | 16,576 | 30 | 0 | - | BARE_WORD_MATCH |
| `standard-oil-company-of-california-annual-report-1956` | 1957-01-01 / title:1956 | in-window MISMATCH | 68,405 | 2 | 0 | - | BARE_WORD_MATCH |
| `standard-oil-company-of-california-annual-report-1957` | 1958-01-01 / title:1957 | in-window MISMATCH | 67,323 | 3 | 0 | - | BARE_WORD_MATCH |
| `environmentalbas01clea` | 1982-01-01 | in-window | 360,356 | 25 | 0 | - | BARE_WORD_MATCH |
| `standard-oil-company-of-california-annual-report-1958` | 1959-01-01 / title:1958 | in-window MISMATCH | 75,124 | 3 | 0 | - | BARE_WORD_MATCH |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `NASA_NTRS_Archive_19840005539` l.12: THREErDIMENSIONAL ANALYSIS OF CHEVRON-NOTCHED
- `NASA_NTRS_Archive_19840005539` l.155: THSEE-DIMENSIOHAL ANALYSIS OF CHEVRON-NOTCHED SPECIMENS
- `NASA_NTRS_Archive_19840005539` l.168: chevron-notched short-bar and short-rod speclmemens, using the
- `NASA_NTRS_Archive_19780024484` l.7: CHEVRON cutting --EXPERIMENT WITH NEW
- `NASA_NTRS_Archive_19780024484` l.33: Translation of "CHEVRON CUTTING- ; Vex such mit
- `NASA_NTRS_Archive_19780024484` l.56: CHEVRON CUTTING- -EXPERIMENT WITH NEW
- `01-chevron-cover` l.1567: This Annual Report of Chevron Corporation contains forward-looking statements relating to Chevron's operations that are based on management's current
- `01-chevron-cover` l.1673: 26 CHEVRON CORPORATION 2005 ANNUAL REPORT
- `01-chevron-cover` l.1905: CHEVRON CORPORATION 2005 ANNUAL REPORT 27
- `NASA_NTRS_Archive_19840025763` l.10: A REVIEW OF CHEVRON-NOTCHED FRACTURE SPECIMENS
- `NASA_NTRS_Archive_19840025763` l.45: A REVIEW OF CHEVRON-NOTCHED FRACTURE SPECIMENS
- `NASA_NTRS_Archive_19840025763` l.55: This paper reviews the historical development of chevron-notched fracture
- `NASA_NTRS_Archive_19840021180` l.5: CHEVRON-NOTCHED FRACTURE SPECIMENS
- `NASA_NTRS_Archive_19840021180` l.28: CHEVRON-NOTCHED FRACTURE SPECIMENS
- `NASA_NTRS_Archive_19840021180` l.38: been calculated for chevron-notched bar and rod fracture specimens using a
- `NASA_NTRS_Archive_19830011631` l.58: Chevron-Notch Specimens
- `NASA_NTRS_Archive_19830011631` l.77: Symposium on Chevron-Notched Specimens:
- `NASA_NTRS_Archive_19830011631` l.110: short rod and short bar chevron-notch specimens previously calibrated by the au-
- `NASA_NTRS_Archive_19800023978` l.16: Determined With Chevron Notch Specimens
- `NASA_NTRS_Archive_19800023978` l.20: BRITTLE MATERIALS LET rat MI NED Mil'll CHEVRON
- `NASA_NTRS_Archive_19800023978` l.59: DETERMINED WITH CHEVRON NOTCH SPECIMENS
- `NASA_NTRS_Archive_20080012230` l.16: [54] PASSIVE CHEVRON REPLICATOR
- `NASA_NTRS_Archive_20080012230` l.62: the replicator uses chevron type elements arranged in
- `NASA_NTRS_Archive_20080012230` l.88: PASSIVE CHEVRON REPLICATOR
- `standard-oil-company-of-california-annual-report-1956` l.80: This Chevron hallmark, adopted generally throughout
- `standard-oil-company-of-california-annual-report-1956` l.1253: generally under the brand name “Chevron,”
- `standard-oil-company-of-california-annual-report-1957` l.693: from the Gulf. Development of the Chevron
- `standard-oil-company-of-california-annual-report-1957` l.1111: Chevron Supreme Gasoline and a new RPM
- `standard-oil-company-of-california-annual-report-1957` l.1126: California family by display of the Chevron
- `environmentalbas01clea` l.9: ENVIRONMENTAL  BASELINE  REPORT  FOR  CHEVRON'S
- `environmentalbas01clea` l.17: CHEVRON  SHALE  OIL  COMPANY
- `environmentalbas01clea` l.51: ENVIRONMENTAL  BASELINE  REPORT  FOR  CHEVRON'S
- `standard-oil-company-of-california-annual-report-1958` l.1549: these stations displayed the familiar Chevron
- `standard-oil-company-of-california-annual-report-1958` l.1592: { Chevron (formerly “Calso”) station of The California Oil
- `standard-oil-company-of-california-annual-report-1958` l.1613: Chevron dealer station, operating in Western United States.
