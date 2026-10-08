# Harvest mining -- humana

Window applied: 1961-01-01 .. 1985-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

25 candidate rows in the harvest index; 12 items mined; 12 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 1 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 1 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 10 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `humana inc`; **other quoted terms** (predecessors, siblings, trade titles): none. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `cultura-personal-y-ycultura-nacional` | 1964-01-01 | in-window | 26,191 | 5 | 0 | - | BARE_WORD_MATCH |
| `micro_IA40385011_1273` | 1984-01-01 / title:1984 | in-window | 218,762 | 154 | 12 | `humana inc`, `humana, inc` | TIER1_CANDIDATE_TEXT |
| `gov.uscourts.kywd.135623` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.tnmd.60607` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.ncwd.119907` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.alsd.62465` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.ca5.14-20358` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.azd.602859` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.cand.334008` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.cand.287609` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.casd.775864` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.uscourts.cod.158387` | ? | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `cultura-personal-y-ycultura-nacional` l.101: bilidad que realzan la existencia humana,
- `cultura-personal-y-ycultura-nacional` l.329: dad de la índole humana, comienza a
- `cultura-personal-y-ycultura-nacional` l.363: Jestad de la persona humana.
- `micro_IA40385011_1273` l.102: : Humana Inc., a publicly-traded company. .
- `micro_IA40385011_1273` l.1709: to General Hospitals of Humana Inc. (“Humana”) for the
- `micro_IA40385011_1273` l.1718: On January 15, 1982, General Hospitals of Humana Inc.,
