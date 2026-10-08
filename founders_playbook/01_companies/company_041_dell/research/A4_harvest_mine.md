# Harvest mining -- dell

Window applied: 1984-01-01 .. 1992-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

40 candidate rows in the harvest index; 12 items mined; 16 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 0 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 5 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 7 | text held, zero hits. |
| `UNANSWERED` | 0 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `dell computer`, `dell computer corporation`; **other quoted terms** (predecessors, siblings, trade titles): `pc s limited`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `DTIC_ADA199042` | 1987-01-01 / title:1990 | in-window MISMATCH | 92,941 | 0 | 0 | - | NULL |
| `DTIC_ADA206527` | 1988-01-01 | in-window | 89,738 | 0 | 0 | - | NULL |
| `DTIC_ADA210817` | 1989-01-01 | in-window | 95,721 | 0 | 0 | - | NULL |
| `DTIC_ADA220594` | 1989-01-01 | in-window | 98,386 | 0 | 0 | - | NULL |
| `DTIC_ADA211962` | 1989-01-01 / title:1962 | in-window MISMATCH | 96,494 | 0 | 0 | - | NULL |
| `DTIC_ADA211965` | 1989-01-01 / title:1965 | in-window MISMATCH | 36,159 | 0 | 0 | - | NULL |
| `DTIC_ADA210818` | 1989-01-01 | in-window | 96,227 | 0 | 0 | - | NULL |
| `DTIC_ADA298471` | 1995-01-01 | outside? | 953,168 | 200 | 0 | - | BARE_WORD_MATCH |
| `DTIC_ADA425243` | 1994-01-01 | outside? | 1,015,500 | 137 | 0 | - | BARE_WORD_MATCH |
| `micro_IA41155130_0548` | 1999-01-01 / title:1995 | outside? MISMATCH | 25,413 | 2 | 0 | - | BARE_WORD_MATCH |
| `cu31924029194665` | 1921-01-01 | outside? | 193,456 | 4 | 0 | - | BARE_WORD_MATCH |
| `changesinmentalt00broouoft` | 1921-01-01 | outside? | 215,797 | 5 | 0 | - | BARE_WORD_MATCH |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `DTIC_ADA298471` l.4: LITTLE  DELL  LAKE
- `DTIC_ADA298471` l.44: LITTLE  DELL  LAKE
- `DTIC_ADA298471` l.92: UTTLE  DELL  LAKE
- `DTIC_ADA425243` l.1: LITTLE  DELL  LAKE
- `DTIC_ADA425243` l.61: 1 .  Little  Dell  Lake,  Salt  Lake  City  Streams,  Utah,  Embankment  Criteria  and
- `DTIC_ADA425243` l.104: LITTLE  DELL  LAKE
- `micro_IA41155130_0548` l.51: Susan J. Dell, Ph.D
- `micro_IA41155130_0548` l.210: Susan J. Dell, Ph.D., and Margaret McNemey, M. Ed share the responsibility of provid
- `cu31924029194665` l.103: FOWLER DELL BROOKS
- `cu31924029194665` l.129: FOWLER DELL BROOKS
- `cu31924029194665` l.154: Copyright, 192 1, by Fowler Dell Brooks
- `changesinmentalt00broouoft` l.8: Brooks,  Fowler  Dell
- `changesinmentalt00broouoft` l.21: FOWLER  DELL  BROOKS
- `changesinmentalt00broouoft` l.48: FOWLER  DELL  BROOKS
