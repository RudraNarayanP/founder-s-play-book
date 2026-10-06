# registrant_resolve_repairs.md

Owner: `registrant-tools` · claimed with `python tools/scaffold.py claim --path tools/sec_intake.py --agent registrant-tools`
(attached, ttl 240 min) and a separate claim on this file. Pass type: **TOOLING REPAIR** — two defects in
`tools/sec_intake.py`, each proved by a self-test control. No register, volume, `_parts/` or company
`sources/` content was written; `tools/gates.py`, `queries.json`, `harvest_mine.py`, `fleet_intake.py`,
`cdx_intake.py`, `web_domains.json` were not touched (other agents hold them tonight).

Baseline before my edits: `selftest` **42 checks / 0 failing**, file 1,431 lines.
After the last write: **54 checks / 0 failing**, rc 0, file **1,803** lines, diff **+374 / −2** —
the only two deleted lines are `if len(hits) == 1:` / `return hits[0][0], hits[0][1], "name-exact"`
inside `resolve_name`, whose behaviour is preserved (it is now reached only after the conflation test
passes). **No pre-existing self-test check was changed.**

---

## 1. Defect R-1 — `resolve_name` conflated two registrants and called it `name-exact`

**What the code did.** `_norm_name` deletes every word in `NAME_STOP_WORDS`, which holds both `corp`/
`corporation` and `inc`/`incorporated`, and `resolve_name` returned a single confident match on that
token set. Measured against the live ticker map (10,434 rows) before my edit:

```
'AT&T Corp'      -> (732717, 'AT&T INC.', 'name-exact')      # WRONG registrant
'AT&T Inc.'      -> (732717, 'AT&T INC.', 'name-exact')
```

`AT&T Corp` and `AT&T Inc.` both reduce to `{at, t}`, and `company_tickers.json` holds **only** the row
`732717 AT&T INC.` (measured: it appears three times, one CIK) — the historic registrant **CIK
0000005907, American Telephone & Telegraph / AT&T CORP, incorporated New York 1885, perimeter
1994-01-07→2007-01-18**, is not in EDGAR's name table at all, while **732717 is SBC Communications /
Southwestern Bell, incorporated Delaware 1983**. So the name route did not merely prefer one of two
candidates; it answered a question the map cannot answer, and the AT&T probe only found the historic
registrant by reading a co-filer SGML header inside a stored 425
(`company_035_att/research/A_chronology_feasibility.md` §0 B-2, §1.2, U1).

**What it does now** (`resolve_name`, L1029 ff., helpers `corp_suffixes` L293 / `_raw_norm` L303):

1. A **designator-exact** match (whole name, punctuation/case folded, suffixes *kept*) is computed and
   preferred: verdict `name-exact-designator`. When other registrants still share the stripped tokens,
   the tool prints that they were **not excluded** — the caller sees the risk instead of inheriting it.
2. When the only match exists *because stop words were deleted* and the corporate designators disagree
   (query carries `corp`, the map's registrant carries `inc`), the resolver **refuses**: it prints
   `*** NAME-CONFLATION-WARNING ***` plus one `CANDIDATE CIK <n> -- <name>` line per candidate, and
   returns the candidate list in the verdict, telling the caller to pass `--cik` and that a name absent
   from `company_tickers.json` is a delisted/ancestor registrant reachable **only** by CIK. No CIK is
   returned, so no wrong-registrant intake is possible from the name route.
3. Both options in the brief were taken, in that order: prefer the raw-string match **and** return
   AMBIGUOUS-with-candidates when only the stop-word match exists.

**Live proof, run after the last write** (scratch dir outside the corpus; nothing was written to any
company directory — the refusal precedes every write):

```
$ python tools/sec_intake.py index "AT&T Corp" --company-dir $SCRATCH/company_035_att
name: *** NAME-CONFLATION-WARNING *** 'AT&T Corp' and the map's 'AT&T INC.' reduce to the same
   tokens only because NAME_STOP_WORDS deletes corporate suffixes.
   CANDIDATE CIK 732717 -- AT&T INC.
identity 'AT&T Corp' not resolved: NAME-CONFLATION-WARNING 'AT&T Corp': the only stop-word-equal
registrant is 'AT&T INC.' (CIK 732717), whose designator is inc, while the name asked for carries
corp -- ... Choose the registrant and pass --cik; if the name you want is absent from
company_tickers.json altogether it is a delisted or ancestor registrant, reachable ONLY by CIK.
exit code: 1
$ python tools/sec_intake.py resolve --ticker T
{"ticker": "T", "cik": 732717, "name": "AT&T INC."}          # the ticker route is unchanged
$ find $SCRATCH -type f          ->  (no files)
```

The second command is the contrast that matters: `T` genuinely **is** 732717, and the fix does not
disturb the ticker route — it stops a *name* from being promoted to an identity claim it cannot carry.

**Controls (4 new checks, all offline fixtures — the self-test spends no EDGAR request):**

| check | what it plants |
|---|---|
| R-1 `'AT&T Corp' vs 'AT&T Inc.' cannot resolve to one name-exact answer` | the map holding **only** `AT&T INC. (732717)` — tonight's real map — and asserts CIK `None` + verdict starting `NAME-CONFLATION-WARNING` naming 732717 |
| R-1 NEGATIVE: names that genuinely have one answer still resolve | `AT&T Inc.`, `AT&T`, `Boeing`, `Home Depot, Inc.`, `Microsoft` must all return a CIK |
| R-1 a designator-exact registrant is preferred | the map holding **both** rows → `AT&T Corp` must return **5907**, verdict `name-exact-designator` |
| R-1 a suffix-free brand naming two registrants stays AMBIGUOUS and lists both | `AT&T` with both rows → refused, and both CIKs in the message |

**Compatibility with the other agents' parsers.** `tools/fleet_intake.py:129` classifies a pass as
REFUSED on the substring `"not resolved"`, which the refusal path still prints (via `main`'s existing
SystemExit) — so a conflated name now records as REFUSED rather than as a successful intake of the
wrong registrant. Nothing anywhere greps the string `name-exact` (checked across `tools/`), and
`name-exact-designator` contains it as a prefix.

---

## 2. Defect R-2 — `_RUN.json` could record an intake that did not happen, or fail to record one that did

**What the code did.** `auto` wrote `attempted/stored/bytes` from in-memory lists at one instant and
never looked at the shelf again. The AT&T case, re-measured read-only on this repo at close:

```
RECORD (_RUN.json, built 2026-10-06T11:57:32Z): attempted=10 stored=6 bytes=70,666 window=2005-01-01..2006-06-30
SHELF  (sources/sec/, same instant)           : 33 bodies / 10,500,602 B / 33 .meta.json sidecars, 0 orphans
bodies named by THIS record: 6   bodies named by NO record on the shelf: 27  (= 10,429,936 B)
body mtime range 11:52:30Z -> 12:00:14Z ; `_RUN` artefacts present: one, no `.prev-` versions
```

Every one of the record's six claimed paths exists on disk (so this shelf is not the
record-without-bytes direction), but the record under-states the shelf by **27 documents and
10.4 MB**, and the last 3 minutes of writes happened *after* the record was stamped. The absence of
`.prev-` artefacts dates the cause: those passes ran at 11:52–12:00Z, and `version_aside()` landed at
**12:07Z** (commit `42f6cfc`, RD-137) — so the earlier records were overwritten, not versioned. RD-137
fixed *overwriting*; it did not make a record correspond to bytes, and nothing compared the two. A
merge or re-grade agent reads the record, so `stored 0` for the 1885–1984 pass became a corpus-wide
false null inherited by `00_universe/_FLEET_INTAKE.tsv`.

**What it does now** (`shelf_census` L793, `reconcile_shelf` L834, wired at L1740 and the summary
print; token `RECORD/SHELF MISMATCH` at L790):

* At the end of `auto` — after every fetch, before the record is written — the module **re-counts the
  target `sources/` subtree**: body count, total bytes, `.meta.json` sidecar count, the count of bodies
  whose mtime is at or after the run's start, `bodies_without_sidecar` and `sidecars_without_body` by
  name. Run artefacts (`_RUN.json`, `_MANIFEST.csv`, `_PLAN.csv`, `_SKIPPED.csv`, `_UNANSWERED.csv` and
  their `prev-` versions) are the record, not the corpus, and are never counted as documents.
* Those numbers are written **into `_RUN.json` beside the in-memory totals** (`shelf{...}`,
  `record_shelf`, `record_shelf_lines`, `status`) — so even where the *trigger* stays silent, a reader
  sees `stored=6` next to `files=33` instead of having to go and find out.
* Four named disagreement classes print, each grep-able behind the one token:
  `RECORD-WITHOUT-BYTES` (the record claims a document whose body is absent or 0 B — RD-112's original
  direction), `BYTES-WITHOUT-RECORD` (AT&T's direction), `BODY-WITHOUT-SIDECAR`,
  `SIDECAR-WITHOUT-BODY`.
* Any of them makes `auto` **exit 2** instead of a silent 0, and the print says outright that neither
  the record nor the shelf may be read as "what was intaked" until it is resolved.

Sample of the new output, from the end-to-end control (fake wire, `main()`'s real `auto` branch):

```
auto: 2 documents stored (120 bytes, 16 words); 0 UNANSWERED (of which 0 nameless pre-2001 listing
      rows); 0 SKIPPED
auto: SHELF census of sources/sec -- 3 bodies / 143 B / 3 sidecars on disk, 3 of them written during
      this run; the record above claims stored=2, bytes=120
auto: *** RECORD/SHELF MISMATCH: BYTES-WITHOUT-RECORD -- 1 file(s) written during this run are named
      by no record, so a reader of `_RUN.json` will conclude they were never intaked:
      0000732717-97-000001_b.txt ***
auto: the run record and the bytes on disk DISAGREE (classes above). `_RUN.json` carries both sets of
      numbers, but neither may be read as what was intaked until this is resolved -- exiting 2, not 0.
```

And against the **real AT&T shelf**, read-only, asking the whole-shelf question (`since=0`, i.e.
"every byte here should be accounted for"):

```
reconcile ok = False | census: files=33 bytes=10500602 sidecars=33
  RECORD/SHELF MISMATCH: BYTES-WITHOUT-RECORD -- 27 file(s) ... 0000005907-94-000008_...txt,
  0000009749-94-000044_...txt, 0000732717-00-000018_...txt ...
```

I did **not** back-fill that record: it is `company_035_att`'s `sources/`, and writing it would be the
brief's forbidden move. The finding is handed to the orchestrator in §4.

**Controls (8 new checks).** Six direct + two end-to-end, all in `tempfile.mkdtemp`, no network:

| check | what it plants |
|---|---|
| a stored document the record says zero for **FIRES** (AT&T's exact shape) | one body + sidecar on the shelf, `stored=[]` → `BYTES-WITHOUT-RECORD`, and the census numbers `files=1 bytes>0 sidecars=1` |
| a record claiming bytes that are not on disk **FIRES** | `stored=[{path: sec/missing.txt}]` → `RECORD-WITHOUT-BYTES` |
| a body without a sidecar is reported by name | `orphan_body.txt` → class + name in `bodies_without_sidecar` |
| a sidecar without a body is reported by name | `gone.txt.meta.json` → class + `gone.txt` in `sidecars_without_body` |
| NEGATIVE: a run record that matches its shelf stays clean | body + sidecar + a `stored` row naming it + a `_RUN.json` in the dir → `ok=True`, `files==1`, `files_written_during_run==1` (proves run artefacts are excluded from the count) |
| auto writes the disk numbers and cannot exit 0 on disagreement | source-text: the record keys, `recon_lines`, `if not recon_ok: return 2` |
| end-to-end: `auto` with an unrecorded body on its shelf exits **2** | `main()`'s whole auto branch with a faked wire; a body lands during the run named by nothing → rc 2, `record_shelf == RECORD/SHELF MISMATCH`, `stored=2`, `shelf.files=3` |
| end-to-end: the record carries the disk counts beside the in-memory ones | the `_RUN.json` read back off disk has all six `shelf` keys and the mismatch line inside it |

---

## 3. Where I judged the fix should NOT be applied, and why

1. **`NAME_STOP_WORDS` itself is untouched.** Deleting `corp` or `inc` from the set would change
   `_norm_name`, which is also `registrant_guard`'s matcher (D-5) and `slug_tokens'` — while the fleet's
   intake and re-grade passes are live against it tonight, and RD-135's de-spaced matcher fix (Home
   Depot, Wells Fargo, Morgan Stanley — "eight companies that never ran the incident", RD-135's own
   count) lives on that same function. The conflation is a property of the *resolver's claim of
   confidence*, not of tolerant matching, so it is fixed in `resolve_name`.
2. **A suffix-free query still resolves.** `Boeing` → `BOEING CO`, `AT&T` → one candidate: the query
   asserts no designator, so nothing was erased *from the question*; refusing those would break every
   shorthand the fleet was briefed to run (`auto "Boeing"`, `index "Microsoft"`). The guard fires only
   when the query **names** a designator and the matched registrant carries a different one — a
   one-directional test, deliberately.
3. **Non-designator stop words (`the`, `and`, `group`, `new`, `delaware`) are not treated as
   suffixes.** `Johnson & Johnson` vs `JOHNSON & JOHNSON` must stay a match; `INC`/`INCORPORATED`,
   `CORP`/`CORPORATION`, `CO`/`COMPANY` are each one class so a synonymous suffix cannot fire.
4. **Wire bytes vs on-disk bytes is reported but never asserted.** `grab` stores `len(raw)` (bytes off
   the wire) in the sidecar and writes `raw.decode("utf-8","replace")`, so any document carrying
   non-UTF-8 bytes has a different size on disk. A detector that fires on correct behaviour gets
   switched off; only a 0-byte body counts as disagreement.
5. **The trigger is freshness-scoped, not whole-shelf.** The shelf is additive and the fleet runs two
   passes per company, so "files != stored" would fire on every second pass and be ignored by
   tomorrow. Bodies older than this run are *recorded* in `shelf{...}` but not *flagged*; a 50 ms
   grace (`FRESH_GRACE_SECONDS`) covers Windows' ~15 ms clock tick and stays three orders of magnitude
   below the gap between two passes (AT&T's were 28 s apart).
6. **`facts` and `index` are not wired into the reconciliation.** `xbrl_facts` already answers this
   defect class with `_write_verified` + a named NULL/UNANSWERED artefact per CIK-and-window (D-1), and
   `write_index` keys artefacts by CIK with its own dropped-row counts (D-2, D-5); pointing
   `reconcile_shelf` at `sources/_index` would grade the index, not the intake, and would collide with
   the quarantine layout the same guard produces on purpose (ExxonMobil holds three registrants —
   34088 EXXON MOBIL CORP, 67182 MOBIL CORP, and the 2020s `ExxonMobil Holdings Corp` 0002115436 that
   owns the canonical slot — the same class as AT&T, and the guard's quarantine is the *correct*
   outcome there).
7. **The refusal exits 1, not 2.** The pre-existing `AMBIGUOUS` path exits 1 through the same
   SystemExit; changing it would alter what `fleet_intake` sees for reasons unrelated to this defect.
8. **D1 (`write_index` legacy `submissions.json` with an int `cik` calls `.strip()`, now L483) was
   NOT fixed.** It is the orchestrator's own queued item ("URGENT one-line fix owed, immediately after
   `registrant-tools` releases `tools/sec_intake.py`"), and touching it would be editing another
   agent's claim in spirit. My change does make its damage *visible*: a run that crashes after storing
   bytes leaves those bodies as `BYTES-WITHOUT-RECORD` for the next pass and in every record's
   `shelf{...}`.

---

## 4. Self-test counts and hand-off

* `python -m py_compile tools/sec_intake.py` → clean.
* `python tools/sec_intake.py selftest` → **54 checks, 0 failing**, rc **0** (was 42/0). Run three
  consecutive times with the same result; the 12 added checks are the 4 `R-1` + 8 `R-2` controls
  above. All new checks use fixtures/temp dirs — **the self-test still makes no network call.**
* Re-measured after the last write: file **1,803 lines**, diff **+374/−2**, deleted lines: the two
  `name-exact` return lines quoted in §0.
* **Offline proof of the offline claim:** the same suite run with `urllib.request.urlopen` replaced by
  a raising stub → `NO-NETWORK RUN: rc=0 urlopen attempts=0 elapsed=0.1s`, `54 checks, 0 failing`. The
  self-test therefore cannot be slowed, rate-limited or falsified by EDGAR.
* **For the orchestrator, not for me to write:** `company_035_att/sources/sec/_RUN.json` records 6
  stored / 70,666 B against a shelf of 33 / 10,500,602 B (27 bodies named by no record on that shelf,
  and its 11:52:02Z predecessor is gone — overwritten before `version_aside` landed at 12:07Z). The
  fleet TSV's `att` row inherits the record, not the shelf. Re-running `auto` for that window now
  prints the numbers side by side, and any *new* unrecorded byte exits 2.
* **Still open in the name route, untouched by design:** RD-137's addendum records that `resolve_name`
  has no ALIAS map (`bofa`, and by the same logic `att`, resolve 7 name forms to 0 candidates while the
  mine holds 12 entity-bearing documents). The conflation guard makes the *wrong* answer impossible to
  reach silently; it does not make the *right* ancestor registrant reachable by name, because
  `company_tickers.json` does not contain it. `--cik` is still the only route to 5907.
