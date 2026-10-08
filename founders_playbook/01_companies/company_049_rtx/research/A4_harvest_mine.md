# Harvest mining -- rtx

Window applied: 1920-01-01 .. 1997-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

71 candidate rows in the harvest index; 12 items mined; 48 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 6 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 3 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 2 | text held, zero hits. |
| `UNANSWERED` | 1 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `rtx corporation`; **other quoted terms** (predecessors, siblings, trade titles): `e systems`, `formerly known as`, `hughes aircraft`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `cia-readingroom-document-cia-rdp67b00074r000500020003-8` | 1965-01-01 / title:2000 | in-window MISMATCH | 3,231 | 1 | 1 | `raytheon company` | TIER1_CANDIDATE_TEXT |
| `DTIC_ADA312323` | 1994-01-01 | in-window | 57,054 | 8 | 4 | `raytheon  company` | TIER1_CANDIDATE_TEXT |
| `NASA_NTRS_Archive_19800017025` | 1980-01-01 / title:1980 | in-window | 11,994 | 0 | 0 | - | VARIANT_TERM_HIT |
| `DTIC_ADA312286` | 1992-01-01 | in-window | 20,116 | 8 | 6 | `raytheon  company` | TIER1_CANDIDATE_TEXT |
| `DTIC_ADA312708` | 1992-01-01 | in-window | 23,991 | 0 | 0 | - | VARIANT_TERM_HIT |
| `DTIC_ADA221452` | 1988-01-01 | in-window | 42,940 | 0 | 0 | - | VARIANT_TERM_HIT |
| `NASA_NTRS_Archive_19960002042` | 1995-01-01 / title:1996 | in-window MISMATCH | 403,526 | 0 | 0 | - | NULL |
| `TNM_Cover_-_Ratheon_Company_Annual_Report_1965` | 1965-01-01 / title:1965 | in-window | 38 | 0 | 0 | - | UNANSWERED |
| `micro_IA41153549_0300` | 1978-01-01 | in-window | 78,051 | 3 | 2 | `raytheon company` | TIER1_CANDIDATE_TEXT |
| `pilotdatacollect00unit` | 1973-01-01 | in-window | 49,945 | 3 | 2 | `raytheon   company`, `raytheon  company` | TIER1_CANDIDATE_TEXT |
| `micro_IA41153513_0027` | 1977-01-01 / title:1977 | in-window | 64,800 | 17 | 4 | `raytheon employees` | TIER1_CANDIDATE_TEXT |
| `cia-readingroom-document-cia-rdp96b01172r000300020005-3` | 1982-01-01 / title:2000 | in-window MISMATCH | 13,871 | 0 | 0 | - | NULL |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `cia-readingroom-document-cia-rdp67b00074r000500020003-8` l.24: Raytheon Company
- `DTIC_ADA312323` l.17: Raytheon  Company's  Data
- `DTIC_ADA312323` l.68: Raytheon  Company's  Data  Supporting:
- `DTIC_ADA312323` l.153: Raytheon  Company
- `NASA_NTRS_Archive_19800017025` l.32: CRITIQUE OF THE HUGHES AIRCRAFT SHUTTLE
- `NASA_NTRS_Archive_19800017025` l.68: A bit synchronizer proposed by Hughes Aircraft (Culver City)
- `NASA_NTRS_Archive_19800017025` l.71: proposed by P. H. Conway [1] of Hughes Aircraft Company (HAC).
- `DTIC_ADA312286` l.12: Raytheon  Company's  Data
- `DTIC_ADA312286` l.49: Raytheon  Company's  Data
- `DTIC_ADA312286` l.253: Raytheon  Company's  interpretation  and  use  of  the  CALS  stan^ds  in  transferring  tech¬
- `DTIC_ADA312708` l.14: Using  Hughes  Aircraft
- `DTIC_ADA312708` l.52: Using  Hughes  Aircraft  Company
- `DTIC_ADA312708` l.217: analyze  Hughes  Aircraft  Company's  interpretation  and  use  of  the
- `DTIC_ADA221452` l.9: HUGHES  AIRCRAFT  COMPANY
- `DTIC_ADA221452` l.59: Hughes  Aircraft  Company  Missile  Systems  Group
- `DTIC_ADA221452` l.333: Hughes  Aircraft  Company,  Missile  Systems  Group  (MSG)  was  to  identify  best  practices,
- `micro_IA41153549_0300` l.100: Raytheon Company/Autometric
- `micro_IA41153549_0300` l.186: by personnel from Raytheon Company/Autometric and Human Factors Research
- `pilotdatacollect00unit` l.36: RAYTHEON   COMPANY
- `pilotdatacollect00unit` l.123: The  Raytheon  Company,  Autometric  Operation  began  working  with  the
- `micro_IA41153513_0027` l.1198: regular Raytheon employees wno had been working for the com-
- `micro_IA41153513_0027` l.1248: end of August. The Raytheon employees did not retake the
- `micro_IA41153513_0027` l.1367: lower attitude score than the base line Raytheon employees.
