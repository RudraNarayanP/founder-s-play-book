# Harvest mining -- unitedhealth

Window applied: 1974-01-01 .. 1995-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

47 candidate rows in the harvest index; 4 items mined; 41 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 0 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 1 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 0 | text held, zero hits. |
| `UNANSWERED` | 3 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: `united healthplan`; **other quoted terms** (predecessors, siblings, trade titles): `charter med`, `metropolitan health plans`, `physicians health plan`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `udRwLIq-iMoC` | 1978-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `CKD-KolMt-8C` | 1981-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `micro_IA40385020_0854` | 1990-01-01 / title:1990 | in-window | 516,579 | 0 | 0 | - | VARIANT_TERM_HIT |
| `Rn5PAQAAIAAJ` | 1994-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `micro_IA40385020_0854` l.10: OCEAN STATE PHYSICIANS HEALTH PLAN, INC., et al.,
- `micro_IA40385020_0854` l.436: OCEAN STATE PHYSICIANS HEALTH PLAN, INC., et al.,
- `micro_IA40385020_0854` l.515: 1. Petitioner Ocean State Physicians Health Plan
