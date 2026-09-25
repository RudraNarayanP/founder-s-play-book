# intake_hardening.md

Proof sheet for the three defects in `tools/sec_intake.py`. Owner: `intake-hardening`.
Every byte count, date, status and quote below was printed by a command run in this
session; nothing here is recalled from a prior pass. Scratch corpus lives outside the
repo at `/tmp/intake_proof/` (Windows: `%TEMP%/intake_proof/`), per §14.9.

## Defect 1 — slice host: verify, not re-fix

**Symptom (historical).** `index` silently stopped at ~2020 because archive slices were
requested at `/Archives/edgar/data/<cik>/<name>` instead of the JSON-API host.

**Change already in place (read, not written by this pass).** `submissions_index()`
builds `url = "https://data.sec.gov/submissions/%s" % f["name"]`, and a slice that will
not return is appended as a row with `"status": "UNANSWERED: " + note` rather than being
skipped. Both are now asserted by `python tools/sec_intake.py selftest`.

**Proof (live, this session).**

| company | command | observed |
|---|---|---|
| Microsoft | `auto/index --cik 789019` | `index: 4525 filings from MICROSOFT CORP (MSFT)`; CSV: `rows=4525 earliest=1994-02-14 latest=2026-09-17 pre2001=158` |
| Costco | `index --cik 909832` | `index: 2723 filings from COSTCO WHOLESALE CORP /NEW (COST)`; CSV: `rows=2723 earliest=1994-01-05 latest=2026-09-24 pre2001=110` |

4,525 rows with earliest 1994-02-14 matches the expected Microsoft history exactly.
For Costco the slice contribution is measured rather than asserted: with `http_get`
monkeypatched so every `...-submissions-00*` slice raises a simulated outage, the same
CIK returns **1,008 rows** (1,007 filings + the UNANSWERED row) — i.e. the `recent`
block alone. Slices therefore add 2,723 − 1,007 = **1,716 extra rows**, the expected
figure, with earliest 1994-01-05.

**Unfetchable slice is recorded, not truncated.** Same simulated-outage run printed:
`simulated-slice-outage rows recorded as UNANSWERED: 1` /
`CIK0000909832-submissions-001.json | UNANSWERED: simulated outage`, and
`_INDEX.md` renders that under "## UNANSWERED slices (never report these as absent)".

Caveat worth carrying forward: every pre-2001 row in these slices has a **blank
`primaryDocument`** — observed directly, e.g. Costco `10-K earliest 1994-11-17
0000912057-94-003945 pd=`(empty) and `10-K405 earliest 1995-11-30 0000912057-95-010555
pd=`(empty). That blank is the seam Defect 3 falls through; see below.

STATUS: WRITTEN 2026-09-25

## Defect 2 — `str` marker among `bytes`: verify, plus a standing check

**Symptom (historical).** `ERROR_MARKERS` mixed a `str` entry into `bytes` entries, so
`marker in raw` on a bytes body raised `TypeError`, every binary fetch fell through the
`except Exception` arm, and the run reported `UNANSWERED after 3 tries` — an outage that
was a code bug.

**Current state.** All 12 entries are `bytes` literals. The failure mode is now closed in
three places rather than by inspection:

1. `_looks_like_error_page()` carries an inline
   `assert isinstance(marker, bytes), "ERROR_MARKERS must be bytes: %r"`, so a `str`
   marker fails loudly at the call site instead of being swallowed as a fetch error.
2. `selftest` asserts the whole tuple: `every ERROR_MARKERS entry is bytes PASS
   str markers: []`, and repeats it for the retry classifier.
3. `selftest` also asserts the detector *fires* on each page shape it must catch and
   *does not* fire on real filing text (§15.5's must-stay-clean control):
   `error-page detector fires on NoSuchKey PASS`,
   `... on File Unavailable PASS`, `... on undeclared-tool 403 PASS`,
   `real filing text is not flagged PASS`.

**Result.** `python tools/sec_intake.py selftest` → `selftest: 18 checks, 0 failing`, rc 0.
Note the self-reference trap found while writing this check: the first version of the
"no /Archives/edgar slice URL remains" assertion embedded the forbidden literal in this
very file, so `src` contained it and the check could never pass. The forbidden string is
now assembled at runtime (`"/Archives/edgar/data/" + "%s/%s.json"`) and the check passes
for the right reason.

STATUS: WRITTEN 2026-09-25

## Defect 3 diagnosis

**Symptom.** `auto --cik 1045810 --from 1998-01-01 --to 2000-12-31` reported `HTTP 503` on
`<accession>-index-headers.html`, `HTTP 503` on `0001.txt`, `HTTP 404` on `0003.txt`, and
stored almost nothing. An Amazon S-1 probe had earlier produced a ~4,819 B placeholder
where the filing should have been.

**Root cause, in the order the evidence arrived. Four things were wrong at once; only one
was EDGAR's fault.**

1. **The document names that `index.json` yields for a pre-2001 accession are mostly
   absent.** Amazon's S-1 directory (`0000891618-97-001309`) returned `200`, 3,347 B, and
   a 41-item listing of which **only the first 3 carry a `name`** — and those 3 are the
   scaffolding stubs (`...-index-headers.html`, `...-index.html`, `...-97-001309.txt`,
   all with `size:""`). The remaining 38 items are `{'name': '', 'type': '', 'size':
   '5319'}` and so on. `auto` took `[:6]` of the *listing order*, so every accession in a
   paper-era window spent its budget on stubs and blank names. A blank name concatenated
   onto the directory URL fetches **the directory itself**, not a document.
2. **The stub it did fetch does not exist.** `.../1045810/000101287000004830/
   0001012870-00-004830-index-headers.html` → `404` with body
   `<Error><Code>NoSuchKey</Code>...<Key>edgar/data/1045810/000101287000004830/...`.
   The generic `0001.txt` reported as `primaryDocument` in the submissions row is also a
   real 404 NoSuchKey, not a throttle.
3. **`pick_auto` required a non-blank `primaryDocument`,** and for Nvidia 1998-01-01..
   2000-12-31 the whole pick set collapsed to 4 accessions, every one of them an
   agent-conformed paper-era shell with `primaryDocument='0001.txt'` (observed:
   `424B2 2000-09-19 0001012870-00-004830 primaryDoc= '0001.txt'`, plus 8-K, S-3,
   SC 13G identically). Combined with (1) and (2), coverage looked like an outage.
4. **Two apology pages were invisible to the detector, and the code saved whatever
   arrived.** With a browser-style `User-Agent` (no declared contact) `0001.txt` returned
   `403` and a **4,814-byte** `<title>SEC.gov | Your Request Originates from an Undeclared
   Automated Tool</title>` page — the placeholder shape §14 names. With our declared UA the
   same request returns a real S3 404, and any unresolvable object can come back as a
   **7,747-byte** `<title>SEC.gov | File Unavailable</title>` page with HTTP 503. Neither
   string was in `ERROR_MARKERS`, so any of these arriving with a 200 status was written
   into the corpus as if it were a filing.

**Candidates eliminated by test, not by reasoning.**

- *Accession-directory form.* Both `data/0001045810/000101287000004830/index.json` and
  `data/1045810/000101287000004830/index.json` returned `200, 558 B`; the `-index`
  suffixed directory returned `404`. So the old directory form was right and the trailing
  `-index` form is wrong — it is now excluded, and `selftest` asserts
  `` `-index` directory form is not tried PASS``.
- *Missing path separator.* All candidate prefixes end in `/` and the constructed URLs
  were observed well-formed; the real separator bug was (1): a *blank* name silently
  collapses the URL onto the directory. `grab()` now refuses an empty filename and
  records `UNANSWERED (empty document name in index.json listing, no URL constructed)`.
- *`Accept-Encoding` handling.* Tested head-to-head on the same Amazon S-1 object:
  `AE=True -> 200 1444013` and `AE=False -> 200 1444013`. It is not the cause. It *is*
  a latent corruption source: a 503 page was observed arriving with the gzip magic
  `1f 8b` while `Content-Encoding` was absent, so the header-only check in the old
  `http_get` would have stored undecoded bytes. `_maybe_gunzip()` now sniffs the magic.
- *Request rate.* Real: the old loop slept 0.12 s **between accessions and not at all
  between documents**, so 6 grabs fired back-to-back. One global gap
  (`_pace()`, `POLITE_SECONDS = 0.35`) now applies to every request. It is not the whole
  story, because a cold single request after a 25 s pause still drew the 7,747 B
  `File Unavailable` page — hence 503/504/429 now back off 5/10/20/40 s instead of
  1.5/3/4.5 s, and a 503 stops trying further directory forms for the same name
  (`break`), because it means the host is cooling down, not that the path is wrong.

**Changes made to `tools/sec_intake.py` (the only file touched).** `accession_dirs()`
ordered by observed status; `doc_listing()` returns `(items, note, form)`, keeps `size`
as a string-parsed int and **counts unnamed items**; `candidate_docs()` new — primary
document first, then named non-scaffolding text items largest-first, then the
full-submission SGML `<accession>.txt`; `grab()` tries each directory form, records every
attempt in `tried`, never writes an error page, keeps the 60 MB cap, and stamps
`url_form`/`http_status`/`tried_before` into the sidecar; `http_get()` flags apology
pages on the text path too and reads the error body to name the reason; `pick_auto()`
accepts blank `primaryDocument`; `auto` writes `_MANIFEST.csv` **and `_UNANSWERED.csv`**
so nothing is dropped and an unanswered document is never counted as a null; `--dry-run`
lists accession, form, document, `bytes_in_index_json` and URL without downloading;
`selftest` subcommand added (§15.5). Stdlib-only, UA/Referer etiquette and the 60 MB cap
unchanged.

STATUS: WRITTEN 2026-09-25

## Three-company proof

Scratch root outside the repo: `/tmp/intake_proof/` (Windows `%TEMP%\intake_proof\`).
Command shape for every row: `python tools/sec_intake.py auto --cik <cik> --company-dir
/tmp/intake_proof/<name> --from <lo> --to <hi> --max-docs <n> --docs-per-filing 2`.
Totals below are recomputed from `_MANIFEST.csv` on disk and each byte count was
re-checked with `ls -l`, so they describe the corpus rather than a console line.

| dir | window | stored | bytes | words | UNANSWERED |
|---|---|---|---|---|---|
| `amazon` | 1995-01-01..1998-12-31 | **8** | 3,765,367 | 515,516 | 0 |
| `amazon_annual` | 1998-01-01..1998-12-31 | **3** | 683,645 | 94,539 | 0 |
| `costco` | 1994-01-01..1998-12-31 | **7** | 1,006,429 | 131,266 | 1 |
| `nvidia` | 1998-01-01..2000-12-31 | **8** | 4,610,910 | 634,274 | 0 |

**One verified byte count each (the `ls -l` column is the independent check):**

| carrier | form / filed | manifest B | `ls -l` B |
|---|---|---|---|
| `amazon/sources/sec/0000891618-97-001309_0000891618-97-001309.txt` | S-1 1997-03-24 | 1,444,013 | **1,444,013** |
| `amazon_annual/.../0000891020-98-000448_0000891020-98-000448.txt` | 10-K405 1998 (first annual report) | 606,461 | **606,461** |
| `costco/.../0000912057-94-003945_0000912057-94-003945.txt` | 10-K 1994-11-17 (earliest annual on the index) | 396,621 | **396,621** |
| `nvidia/.../0001012870-98-000618_0001012870-98-000618.txt` | S-1 1998 | 856,608 | **856,608** |

The original S-1/S-1/A families are present with real volume, not placeholders: Amazon
1 × S-1 (1,444,013 B) + 6 × S-1/A (436,103 / 403,334 / 304,886 / 309,865 / 301,661 /
301,685 B) + 424B1 (263,820 B); Nvidia 1 × S-1 + 7 × S-1/A (564,104 / 440,312 / 626,995 /
590,627 / 682,998 / 425,132 / 424,134 B). Nvidia — the company that started this — went
from "stored almost nothing" to **8 documents / 4,610,910 bytes / 0 UNANSWERED**. Costco
carries 8-K, 10-K, DEF 14A, SC 13D, S-3, 424B1, SC 13G; it has **no S-1 in the window
because its 1985 IPO predates EDGAR full text**, which is an absence proved from the
4,525/2,723-row index rather than from a failed guess.

**Grep confirmations that the bytes are the filing (verbatim, as printed):**

```
amazon/.../0000891618-97-001309_0000891618-97-001309.txt
  "The Company was incorporated in July 1994 and commenced offering products"
costco/.../0000912057-94-003945_0000912057-94-003945.txt
  "merchandising  industry.  When  Price pioneered  the  membership  warehouse club"
```

**No error page reached the corpus.** `grep -l -i -E "File Unavailable|NoSuchKey|Undeclared
Automated" */sources/sec/*.txt` listed nothing.

**UNANSWERED is recorded with its status, never dropped, never a null.** Costco's
`0000912057-95-010555.txt` (the FY1995 10-K405) sits in `_UNANSWERED.csv` as
`UNANSWERED (padded-cik/nodash-dir: - UNANSWERED after 2 tries (HTTP 503 b'SEC.gov | File
Unavail...` — counted separately from the 7 stored, and the note quotes the apology page
that came back.

**Sidecar fields observed** (`nvidia/sources/sec/0000898430-99-000180_...txt.meta.json`):
`url, fetched, sha1, bytes, words, cik, accession, document, url_form, http_status,
tried_before, html_stripped_word_count, full_submission_sgml` — values
`bytes: 424134`, `words: 57037`, `url_form: "padded-cik/nodash-dir"`, `http_status: 200`,
`full_submission_sgml: true`.

**`--dry-run` works and is cheap.** `auto ... --dry-run` printed
`dry-run: 10 accessions, 10 documents WOULD be fetched; no bytes downloaded`, wrote
`sources/sec/_DRY_RUN_PLAN.csv`, and showed URL + `index.json` size + carrier per row,
e.g. `1997-03-24 S-1 0000891618-97-001309.txt 0 B
https://www.sec.gov/Archives/edgar/data/0001018724/000089161897001309/0000891618-97-001309.txt`.

**Nothing outside this file broke:** `python tools/gates.py --self-test` →
`self-test: PASS` (all planted defects CAUGHT / STAYS CLEAN, `clean fixture CLEAN`);
`python tools/gates.py --company-dir founders_playbook/01_companies/company_001_amazon
--checks csv` → 10 registers parsed (e.g. `sources.csv 204 rows x 18 cols`,
`conflicts`/`validation`/`failures`/`data_gaps` `source_id` all resolve), rc 0.
`python tools/sec_intake.py selftest` → `selftest: 18 checks, 0 failing`.

**Writer collision disclosed.** A background loop this pass started was killed at the
python level only (`pkill` is absent on this box), so its shell resumed and ran the same
patched script against the same scratch directories. The totals above are the on-disk
state left by those overlapping runs, which is why Amazon's manifest holds 8 documents
where one console line reported 6. No repo path, company directory or register was
written by any of them; the only repo file touched is this one plus `tools/sec_intake.py`.

STATUS: WRITTEN 2026-09-25

## Still broken

Reported as limits of this pass, not as nulls (§14.6: an untried family is not a null).

1. **The corpus is SGML `.txt` only.** Every `.htm`/`.html` object under `/Archives/`
   drew the 7,747 B `SEC.gov | File Unavailable` 503 in this session, including a control
   URL for a modern Microsoft 10-K, while `index.json` and the `<accession>.txt` carriers
   returned 200 in the same minutes. So the intake now stores full filing text, but the
   HTML renderings and separately-filed exhibits are not being reached. UNTRIED: a long
   (hours) cool-off, the `cgi-bin/browse-edgar?action=getfile` carrier, and the
   `efts.sec.gov` / `filing-index` JSON endpoints that may replace the legacy directory.
2. **Pre-2001 listings still hide most names.** 38 of 41 items in Amazon's S-1 directory
   carry a size and no name, so those objects are unreachable by construction and the
   dry-run reports `0 B` for the SGML carrier (the scaffolding item's size is empty) and
   `(size unlisted)` elsewhere. Recovering names from the `-index.htm` page is the fix and
   it is blocked by item 1.
3. **`auto` overwrites `_MANIFEST.csv` and `_UNANSWERED.csv`** on each run into the same
   directory: the bytes of an earlier pass survive, its manifest record does not. This is
   exactly how the 6-vs-8 discrepancy in the section above became invisible to the console.
   Should append or write a per-run timestamped manifest. Not changed here.
4. **`pick_auto` has no per-form quota**, keeping every S-1/A as §14 intends (version
   differences are findings), so a 6-accession Amazon budget bought 1 S-1 + 5 S-1/A and no
   annual report; capturing the first 10-K needed a second dated pass (`amazon_annual`).
   A `--per-form N` cap is UNTRIED.
5. **Apology-page detection is 12 literal strings.** An unseen SEC error shape would be
   saved as a document. The obvious floor — reject a `text/html` body served for a `.txt`
   name, and a body under a few hundred bytes — was not implemented and is UNTRIED.
6. **Backoff can still cost minutes per accession** when EDGAR is in cooldown
   (`tries=2` per form, 5 s between), and `index` fetches up to 8 slices with `tries=3`,
   so a throttled window made one dry-run exceed 7 minutes. A wall-clock budget
   (`--max-seconds`) is UNTRIED.
7. **Untouched by this pass and therefore unverified after the change:** `facts`,
   `resolve`, and standalone `grab`; the `xbrl_facts` path; gates other than `csv`
   (columns, keys, anchors, quotes, word budget); and the 1989-1994 half of the question,
   which no EDGAR route answers for these three companies.

STATUS: WRITTEN 2026-09-25
