# Gates baseline for the 19 merged Stage-1 volumes -- 2026-10-08

Produced by the main agent with zero model lanes: `gates.py --tier auto --fail-on substantive` per company, findings read back from the JSON the gate writes (not from its stdout prose).

| company | tier the gate read | findings total | substantive | gates carrying them | exit |
|---|---|---|---|---|---|
| jpmorgan | T2 | 5 | 4 | anchors; keys; quotes | exit1 |
| cvs | T2 | 2 | 2 | csv; quotes | exit1 |
| cigna | T2 | 2 | 2 | corrections; keys | exit1 |
| walmart | T1 | 1 | 1 | quotes | exit1 |
| unitedhealth | T3 | 2 | 1 | quotes | exit1 |
| apple | T1 | 1 | 1 | quotes | exit1 |
| costco | T3 | 2 | 1 | quotes | exit1 |
| meta | T2 | 2 | 1 | quotes | exit1 |
| pepsico | T3 | 2 | 1 | quotes | exit1 |
| amazon | T1 | 1 | 0 | - | clean |
| alphabet | T1 | 1 | 0 | - | clean |
| microsoft | T2 | 2 | 0 | - | clean |
| nvidia | T3 | 2 | 0 | - | clean |
| gm | T2 | 1 | 0 | - | clean |
| att | T2 | 2 | 0 | - | clean |
| target | T2 | 1 | 0 | - | clean |
| tesla | T3 | 2 | 0 | - | clean |
| jnj | T2 | 2 | 0 | - | clean |
| boeing | T2 | 2 | 0 | - | clean |

**Substantive findings across the corpus: 14** across 19 volumes. Advisory/coverage rows are excluded by the same rule the exit code uses (s15.6).
