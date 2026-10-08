# Harvest mining -- ups

Window applied: 1907-01-01 .. 1960-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

59 candidate rows in the harvest index; 12 items mined; 43 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 0 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 2 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 9 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 1 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `united parcel service`; **other quoted terms** (predecessors, siblings, trade titles): `of america`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `cia-readingroom-document-0000920852` | 1954-01-01 | in-window | 230 | 0 | 0 | - | UNANSWERED |
| `cia-readingroom-document-cia-rdp80-00809a000600390262-8` | 1951-01-01 / title:1950 | in-window MISMATCH | 8,886 | 1 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19930092496` | 1942-01-01 / title:1993 | in-window MISMATCH | 23,963 | 14 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19930086564` | 1951-01-01 / title:1993 | in-window MISMATCH | 79,337 | 7 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19930081063` | 1928-01-01 / title:1993 | in-window MISMATCH | 25,415 | 6 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19930086369` | 1950-01-01 / title:1993 | in-window MISMATCH | 116,224 | 7 | 0 | - | BARE_WORD_MATCH |
| `NPDP19300107` | 1930-01-01 / title:1930 | in-window | 295,388 | 2 | 0 | - | VARIANT_TERM_HIT |
| `blowupsonresurfa00gres` | 1976-01-01 | outside? | 176,023 | 59 | 0 | - | BARE_WORD_MATCH |
| `ERIC_ED221842` | 1982-01-01 / title:1842 | outside? MISMATCH | 61,601 | 3 | 0 | - | BARE_WORD_MATCH |
| `NASA_NTRS_Archive_19800018384` | 1980-01-01 / title:1980 | outside? | 306,810 | 74 | 0 | - | BARE_WORD_MATCH |
| `jprs-report_jprs-ups-85-013` | 1985-01-01 / title:1984 | outside? MISMATCH | 248,978 | 64 | 0 | - | VARIANT_TERM_HIT |
| `NASA_NTRS_Archive_19810007997` | 1981-01-01 / title:1981 | outside? | 48,989 | 10 | 0 | - | BARE_WORD_MATCH |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `cia-readingroom-document-cia-rdp80-00809a000600390262-8` l.44: FENG-MAN HYDROELECTRIC PLANT Ups POWER OUTPUT
- `NASA_NTRS_Archive_19930092496` l.23: IN ABRUPT PULL-UPS
- `NASA_NTRS_Archive_19930092496` l.69: IN ABRUPT PULL-UPS
- `NASA_NTRS_Archive_19930092496` l.209: third phase was the actual pull-ups in flight. The relation
- `NASA_NTRS_Archive_19930086564` l.17: AND IN PULL-UPS AT MACH NUMBERS
- `NASA_NTRS_Archive_19930086564` l.57: AND IN PULL-UPS AT MACH NUMBERS
- `NASA_NTRS_Archive_19930086564` l.67: stall and in pull-ups at Mach numbers of 0.74, 0.75, 0.94, and O. 97 .
- `NASA_NTRS_Archive_19930081063` l.39: PART II: PULL-UPS
- `NASA_NTRS_Archive_19930081063` l.70: PART II : PULL-UPS.
- `NASA_NTRS_Archive_19930081063` l.79: particular maneuver of flight. The results for pull-ups are pre-
- `NASA_NTRS_Archive_19930086369` l.24: BELL X-1 AIRPLANE IN PULL-UPS AT MACH
- `NASA_NTRS_Archive_19930086369` l.92: BELL X-1 AIRPLANE IN PULL-UPS AT MACH
- `NASA_NTRS_Archive_19930086369` l.101: research airplane. The data were obtained in 10 pull-ups at Mach numbers
- `NPDP19300107` l.2815: hind the seedes in one. of America’s
- `blowupsonresurfa00gres` l.12: BLOW-UPS  ON  RESURFACED
- `blowupsonresurfa00gres` l.38: BLOW-UPS  ON  RESURFACED  CONCRETE  PAVEMENTS
- `blowupsonresurfa00gres` l.49: research  study  entitled  "Pavement  Blow-ups  and  Resurfacing".
- `ERIC_ED221842` l.37: Classroom or Simulating the "Ups" and "Downs" of
- `ERIC_ED221842` l.139: SIMULATING THE ''UPS" AND "DOWNS'' ^
- `ERIC_ED221842` l.194: Simulatjng the-^'Ups^' and ''Downs" of Reading Comprehension
- `NASA_NTRS_Archive_19800018384` l.13: STUDY (SEV-UPS): SURFACE AND AIRBORNE
- `NASA_NTRS_Archive_19800018384` l.44: 1979 SOUTHEASTERN VIRGINIA URBAN PLUME STUDY (SEV-UPS):
- `NASA_NTRS_Archive_19800018384` l.110: dits at SEV-UPS sites during the program.
- `jprs-report_jprs-ups-85-013` l.6978: Voice of America
- `NASA_NTRS_Archive_19810007997` l.11: Data for the SEV-UPS
- `NASA_NTRS_Archive_19810007997` l.55: Data for the SEV-UPS
- `NASA_NTRS_Archive_19810007997` l.272: The Southeastern Virginia Urban Plume Study (SEV-UPS) is a program
