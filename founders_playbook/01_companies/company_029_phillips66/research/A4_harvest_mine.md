# Harvest mining -- phillips66

Window applied: 1917-01-01 .. 2002-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

138 candidate rows in the harvest index; 12 items mined; 125 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 6 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 6 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `phillips 66`, `phillips petroleum`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `nXLDIgvUa4QC` | 1957-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `OrsZAAAAMAAJ` | 1990-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `fXzrPyaNBMcC` | 1987-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `sPuWltm5VHkC` | 1968-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `MR4hAQAAIAAJ` | 1959-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `o-S1DFZBOp4C` | 1968-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `dc_circ_1952_11247_11241_11242_11245_11252_wis_v_fed_power_commn` | 1952-01-01 / title:1952 | in-window | 1,117,732 | 0 | 187 | `phillips petroleum` | TIER1_CANDIDATE_TEXT |
| `Phil1411_1988` | 1988-01-01 / title:1988 | in-window | 148,722 | 0 | 22 | `phillips 66`, `phillips petroleum` | TIER1_CANDIDATE_TEXT |
| `DTIC_AD0261024` | 1961-01-01 | in-window | 24,052 | 0 | 5 | `phillips  petroleum` | TIER1_CANDIDATE_TEXT |
| `cia-readingroom-document-cia-rdp90g01353r000200180023-0` | 1988-01-01 / title:2001 | in-window MISMATCH | 90,305 | 0 | 1 | `phillips petroleum` | TIER1_CANDIDATE_TEXT |
| `cia-readingroom-document-cia-rdp62-00328a000100100002-3` | 1956-01-01 / title:1956 | in-window | 197,648 | 0 | 2 | `phillips petroleum` | TIER1_CANDIDATE_TEXT |
| `cia-readingroom-document-cia-rdp02-06341r000302420011-5` | 1975-01-01 / title:2001 | in-window MISMATCH | 7,827 | 0 | 1 | `phillips petroleum` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `dc_circ_1952_11247_11241_11242_11245_11252_wis_v_fed_power_commn` l.143: Gas Act, the provisions of that Act apply to Phillips Petroleum
- `dc_circ_1952_11247_11241_11242_11245_11252_wis_v_fed_power_commn` l.180: Gas Act, the provisions of that Act apply to Phillips Petroleum
- `dc_circ_1952_11247_11241_11242_11245_11252_wis_v_fed_power_commn` l.392: In the Matter of Phillips Petroleum Company, Opinion No. 217,
- `Phil1411_1988` l.1: PHILLIPS PETROLEUM COMPANY *"ANNUAL; REPORT 1988.
- `Phil1411_1988` l.66: Phillips Petroleum Company In Brief
- `Phil1411_1988` l.195: standards for all stations bearing the Phillips 66 shield and
- `DTIC_AD0261024` l.42: PHILLIPS  PETROLEUM  COMPANY
- `DTIC_AD0261024` l.45: PHILLIPS  PETROLEUM  COMPANY  -  RESEARCH  DIVISION  REPOIT  2873-61R
- `DTIC_AD0261024` l.101: PHILLIPS  PETROLEUM  CGHPANT
- `cia-readingroom-document-cia-rdp90g01353r000200180023-0` l.2788: PHILLIPS PETROLEUM
- `cia-readingroom-document-cia-rdp62-00328a000100100002-3` l.1421: working with these compounds. Phillips Petroleum also has been engaged
- `cia-readingroom-document-cia-rdp62-00328a000100100002-3` l.3617: Chemical Co.; Olin Mathieson; Phillips Petroleum; Westvaco Chlor-
- `cia-readingroom-document-cia-rdp02-06341r000302420011-5` l.58: : .Phillips Petroleum, Gulf and Northrop :
