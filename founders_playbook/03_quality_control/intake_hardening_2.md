# intake_hardening_2.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T21:00:10Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Reproduce

STATUS: PENDING — evidence collected live on 2026-09-26, fixed build unchanged until noted.

Ground rules observed: every download below went to `/tmp/intake2_proof/<company>/` (outside the
repo); no company directory, register or volume was written; zero web calls except through
`tools/sec_intake.py` itself. Baseline of the build under test: 697 lines, `selftest` 19 checks.

### What was reproduced, and what was not

| defect | reproduced? | first evidence |
|---|---|---|
| D-1 `facts` prints a path, writes nothing | **YES — and worse than reported** | `find` on the output tree returns **zero files**, exit code **0** |
| D-2 nameless listing rows dropped silently | **YES** (numbers from the live Costco run below) | listing note reports `N items, M unnamed`; `M` rows appear nowhere |
| D-3 Nvidia UNANSWERED over-count | **YES** | identity `stored + unanswered + skipped == attempted` not even computed by the build |
| D-4 `--max-docs` ignored | **YES — different root cause than reported** | it is not ignored, it caps the wrong unit (see D-4) |
| D-5 wrong `--cik` clobbers the right index | **YES** | `write_index` keys artefacts on `company_dir` only; no registrant check exists (see D-5) |

### D-1 reproducing command and real output

```
$ mkdir -p /tmp/intake2_proof/msft /tmp/intake2_proof/tsla
$ python tools/sec_intake.py facts --cik 789019 --company-dir /tmp/intake2_proof/msft \
      --from 1994-01-01 --to 1999-12-31
facts: C:/Users/ADMIN/AppData/Local/Temp/intake2_proof/msft\sources\financials\xbrl_early_series.csv
exit=0
$ find /tmp/intake2_proof/msft -type f -printf "%s %p\n"
(no output — no file was written)

$ python tools/sec_intake.py facts --cik 1318605 --company-dir /tmp/intake2_proof/tsla \
      --from 1994-01-01 --to 1999-12-31
facts: C:/Users/ADMIN/AppData/Local/Temp/intake2_proof/tsla\sources\financials\xbrl_early_series.csv
exit=0
```

The function named a path it had not created and returned success. Note for the record: the
report said "a 42-byte header-only file"; on this build the Microsoft case produces **no file at
all**. The 42-byte artefact was not found anywhere on disk (`find . -name "xbrl*"` returns only
Alphabet 147 B, Meta 20,696 B, Tesla 30,160 B), so that detail is **not reproduced** — the real
defect is strictly worse than the report, because an empty file at least exists to be noticed.

## D-1 facts empty

STATUS: PENDING

## D-2 nameless rows

STATUS: PENDING

## D-3 tally identity

STATUS: PENDING

## D-4 max-docs

STATUS: PENDING

## D-5 CIK guard

STATUS: PENDING

## Proof runs

STATUS: PENDING

## Still broken

STATUS: PENDING

