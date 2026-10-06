# Harvest mining -- elevance

Window applied: 1944-01-01 .. 2014-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

44 candidate rows in the harvest index; 12 items mined; 29 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 3 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 0 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 1 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 6 | text held, zero hits. |
| `UNANSWERED` | 2 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `elevance health`; **other quoted terms** (predecessors, siblings, trade titles): `formerly known as`, `wellpoint formerly known as`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `2006MoFinExamBlueCrossBlueShieldofKC` | 2006-01-01 | in-window | 77,115 | 0 | 0 | - | NULL |
| `cia-readingroom-document-cia-rdp79-00999a000200010009-6` | 1973-01-01 / title:2000 | in-window MISMATCH | 72,756 | 1 | 0 | - | BARE_WORD_MATCH |
| `wellpointsystemi00grif` | 1950-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `Well4302_2003` | 2003-01-01 / title:2003 | in-window | 65,665 | 40 | 8 | `wellpoint systems` | TIER1_CANDIDATE_TEXT |
| `comparisonofqual00blue` | 1997-01-01 | in-window | 582,047 | 0 | 0 | - | NULL |
| `08C-09` | 2006-01-01 | in-window | 134,342 | 0 | 0 | - | NULL |
| `77B8A2FD-BF86-40E7-99B7-3487EA77B96F` | 2002-01-01 / title:2000 | in-window MISMATCH | 53,829 | 0 | 0 | - | NULL |
| `analysisevaluati2004wolc` | 2004-01-01 / title:2002 | in-window MISMATCH | 187,253 | 0 | 0 | - | NULL |
| `analysisevaluati2006wolc` | 2006-01-01 | in-window | 133,877 | 0 | 0 | - | NULL |
| `gov.gpo.fdsys.CHRG-111hhrg74091` | 2009-01-01 | in-window | 321,806 | 106 | 8 | `wellpoint, inc` | TIER1_CANDIDATE_TEXT |
| `evidenceteaching00rona` | 2012-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `gov.gpo.fdsys.CHRG-113hhrg91184` | 2014-01-01 | in-window | 428,131 | 63 | 6 | `wellpoint, inc` | TIER1_CANDIDATE_TEXT |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `cia-readingroom-document-cia-rdp79-00999a000200010009-6` l.1543: elevance of quantum
- `Well4302_2003` l.35: WellPoint Systems Inc. creates products and services that have transformed
- `Well4302_2003` l.42: IT projects from strategic and design to complete implementation. WellPoint Systems’
- `Well4302_2003` l.46: WellPoint Systems Inc.was founded in 1997 and is headquartered in Calgary, Alberta.
- `gov.gpo.fdsys.CHRG-111hhrg74091` l.192: Wellpoint, Inc 44
- `gov.gpo.fdsys.CHRG-111hhrg74091` l.2651: OFFICER, CONSUMER BUSINESS, WELLPOINT, INC.; CAROL
- `gov.gpo.fdsys.CHRG-111hhrg74091` l.3035: WellPoint, Inc.
- `gov.gpo.fdsys.CHRG-113hhrg91184` l.238: Wellpoint, Inc 41
- `gov.gpo.fdsys.CHRG-113hhrg91184` l.891: change Strategy at WellPoint, Inc.
- `gov.gpo.fdsys.CHRG-113hhrg91184` l.941: STRATEGY, WELLPOINT, INC.
