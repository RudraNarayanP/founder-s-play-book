# Harvest mining -- cvs

Window applied: 1963-01-01 .. 1996-12-31 (deliberately WIDE where the founding date is itself unestablished -- narrowing it here would silently discard the evidence that could establish it).

70 candidate rows in the harvest index; 12 items mined; 57 left untried at the --limit.

**Nothing on this page is a finding.** It is held bytes, hit counts and line numbers for an agent to interpret. Zero hits over held KB is a NULL; a missing text layer or a 404/403 is UNANSWERED; an item not attempted is UNTRIED.

**The match class is the verdict, and it is the half that keeps this honest.**

| class | here | what it means |
|---|---|---|
| `TIER1_CANDIDATE_TEXT` | 3 | a phrase naming this registrant, or its word hard against an identity word (`COSTCO  WHOLESALE`), matched. The string that carried it is in the `promoted by` column, so the label is checkable rather than trusted. |
| `VARIANT_TERM_HIT` | 2 | a hit on a quoted term that is NOT this registrant's name -- a predecessor (`price club`, `dayton hudson`) or the trade title the query ran inside (`chain store age`). Related and worth opening; not a naming of this company. |
| `BARE_WORD_MATCH` | 0 | only the company *word* matched, and that word is also a surname, an acronym and a fruit. The 1976 federal education report whose APPLE means *Anecdotal Processing to Promote Learning Experience* is the case that produced this class, at 162 fake Tier-1 hits. |
| `NULL` | 5 | text held, zero hits. |
| `UNANSWERED` | 2 | no text reached the corpus, so nothing is known either way. |

A row below `TIER1_CANDIDATE_TEXT` may be cited as a pointer to a file, never as evidence, and never counted in a tier verdict.

Entity vocabulary this pass applied -- **name phrases**: none; **other quoted terms** (predecessors, siblings, trade titles): `consumer drug stores`, `drug store news`, `pharmacy times`. Both come from the harvester's own `query` column, not from a list I typed.

| identifier | dates (scan/title) | window | bytes | word hits | entity hits | promoted by | verdict |
|---|---|---|---|---|---|---|---|
| `sprowlsamericanp0000spro` | 1974-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `micro_IA40706951_0252` | 1995-01-01 | in-window | 412,228 | 1 | 0 | - | VARIANT_TERM_HIT |
| `sim_journal-of-the-american-pharmacists-association-japha_1983_23_index` | 1983-01-01 / title:1983 | in-window | 67,074 | 0 | 0 | - | NULL |
| `micro_IA40706944_0407` | 1993-01-01 | in-window | 1,831,676 | 76 | 1 | `cvs sales` | TIER1_CANDIDATE_TEXT |
| `sim_journal-of-the-american-pharmacists-association-japha_1990_30_index` | 1990-01-01 / title:1990 | in-window | 58,919 | 0 | 0 | - | NULL |
| `micro_IA40706938_0038` | 1990-01-01 | in-window | 1,560,994 | 56 | 1 | `cvs sales` | TIER1_CANDIDATE_TEXT |
| `micro_IA40706948_0070` | 1994-01-01 | in-window | 2,147,187 | 142 | 1 | `cvs stores` | TIER1_CANDIDATE_TEXT |
| `sim_journal-of-the-american-pharmacists-association-japha_1981_21_index` | 1981-01-01 / title:1981 | in-window | 69,310 | 0 | 0 | - | NULL |
| `sim_journal-of-the-american-pharmacists-association-japha_1991_31_index` | 1991-01-01 / title:1991 | in-window | 39,082 | 0 | 0 | - | NULL |
| `bwb_P9-ECG-775` | 1977-01-01 | outside? | 0 | 0 | 0 | - | UNANSWERED |
| `sim_pharmacy-times_1989_55_index` | 1989-01-01 / title:1989 | in-window | 38,668 | 0 | 0 | - | VARIANT_TERM_HIT |
| `sim_journal-of-the-american-pharmacists-association-japha_1986_26_index` | 1986-01-01 / title:1986 | in-window | 51,830 | 0 | 0 | - | NULL |

_The scan-date field is often the digitisation year, so `outside?` means the metadata does not place it in the window -- not that the item is out of scope._

## Sample hit lines (verbatim, with the held file's line numbers)

- `micro_IA40706951_0252` l.207: received, along with your telephone number. We'll do everything possible to solve the problem at once. Write to Subscriber Services, Drug Store News, P.O. Box 31182, Tampa. Fla.
- `micro_IA40706951_0252` l.214: Drug Store News For the Pharmacist (ISSNO89 19828) is published monthly—pius a Pharmacist's Reference to Patient Counseling in Decermber—by Lebhar-Friedman Inc., 425 Park Ave., New
- `micro_IA40706951_0252` l.222: send address changes to Subscription Dept., Drug Store News For the Pharmacist, P.O. Box 31185, Tampa, Fla.
- `micro_IA40706944_0407` l.34175: CVS sales advance
- `micro_IA40706938_0038` l.37894: CVS sales leap
- `micro_IA40706948_0070` l.38242: of CVS stores on West Coast, roll-
- `sim_pharmacy-times_1989_55_index` l.289: 120 Pharmacy Times - December 1989
- `sim_pharmacy-times_1989_55_index` l.581: 120 Pharmacy Times - December 1989
- `sim_pharmacy-times_1989_55_index` l.868: December 1989 - Pharmacy Times 121
