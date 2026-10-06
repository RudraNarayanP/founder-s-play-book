# NOTES — Meta Stage-1 part 1 (`s1-meta-p1`)

Author log for the merge and for `s1-meta-p2`. Written 2026-10-06. **Files touched by this pass, and only
these:** `company_017_meta/_parts/s1_p1.md` (authored), this file, and the gate output
`03_quality_control/meta_s1_gates_p1.md`. **No register CSV was opened, created or edited** — the company root
still has none. Nothing under `sources/` was written, moved, pruned or "tidied" (§14 rule 4); `sources/` is a
protected archive and every artifact cited here already existed on disk. **Web calls used: 0 of 8** — every
statement in part 1 rests on bytes already under `company_017_meta/sources/`, so no fetch was attempted and no
Tier-4 material entered the dossier.

## 1. What is on disk and what it is worth

`_parts/s1_p1.md`: **25,200 words**, all twelve dispatched sections `STATUS: WRITTEN` (14 WRITTEN markers
counting the boundary and the register block), §A–§J (Header, boundary,
§A, §B, §C, §D, §E, §F, §G, §H, §I, §J); **33 claim records `P1-01`…`P1-33`**; **99 register rows in 9 fenced
append blocks** (sources 11 · quantitative 30 · timeline 22 · decisions 3 · validation 6 · failures 5 ·
channels 4 · conflicts 7 · data_gaps 11), each preceded by its own `>>> REGISTER ROWS FOR MERGE <<<` marker
(9 markers + 1 section-header marker); **7 §U anchors declared** (`<!-- ANCHORS: U.1-U.7 -->`);
`## Untried` with 11 numbered routes; five `FETCH REQUEST` blocks F-1…F-5. `STATUS: PENDING` remaining: **0**.

**CSV integrity, re-measured after the last write** (each block parsed back through `csv.reader`):
sources 18 cols / 11 rows, quantitative 12/30, timeline 11/22, decisions 15/3, validation 11/6, failures 11/5,
channels 11/4, conflicts 15/7, data_gaps 8/11 — **0 width drift, 0 empty cells, `stage` = `stage1` on all 99
rows**. Two quoting defects were found and repaired on this pass (unquoted commas in five conflicts rows and
four data_gaps rows, plus one merged data_gaps pair); the repair touched only my own part file.

## 2. Tier: I am reporting the probe's verdict, not the dispatch's label

The dispatch calls `company_017_meta` a **T1 exemplar**. `research/A_chronology_feasibility.md` measures
**T2 core — 2 of 5 families returned in-window Tier-1 text**, with the shortfall traced to one archive.org
outage and one consecutive-failure breaker. I re-checked all five families in their held bytes and **the count
is still 2** (filings yes; legal yes at register level; web UNANSWERED; periodicals no in-window text;
corporate print UNQUERIED; auction UNTRIED). Per the brief's rule — say so, do not silently re-tier — this
volume is written at **T1 section density** (Header, boundary, §A–§J, registers, claim records) because that
is the deliverable the dispatch ordered, while **every tier statement in the file reports the measured 2 of 5**.
Nothing in part 1 upgrades the tier; §15.2's capacity expectation (15–20 runs) is the orchestrator's call.

## 3. The five families as found by this pass

| family | as found | bytes this pass read |
|---|---|---|
| (a) filings | **in-window Tier-1 text, but registrant-retrospective for the origin** | 31 stored documents (`_RUN.json`: window 2003-01-01..2012-12-31, attempted 31, stored 30, 50,285,422 B, 1,901,418 words); `_MANIFEST.csv` 30 rows; 424B4 body; S-1 body; 7 S-1/A bodies; exhibits 3.3, 3.4, 4.2A, 4.6, 10.2, 10.4, 10.11, 10.13, 10.14, 10.15, 10.16A, 1.1 |
| — legal | **Tier-1 register, in-window, independent** | `cl2_%22ConnectU%22.json` (count 670 / document_count 4204), `cl2_%22Winklevoss%22.json` (303 / 2939); three HTTP 500 negative artifacts kept |
| (b) web archives | **UNANSWERED, not a null** | `web/cdx_thefacebook.com.txt` 160 B (504), `web/cdx_facebook.com.txt` and `web/cdx_thefacebook_retry.txt` 11,832 B each (503, "Internet Archive services are temporarily offline"). Zero timestamps, so zero capture dates |
| (c) periodical corpora | **no in-window Tier-1 text** | `_harvest/candidates.csv` 30 rows (CA 3 × 403 with blank ids; HathiTrust 2 × status 0; Google Books 22 metadata-only, one 2006 item); 7 stored periodical text files, all `BARE_WORD_MATCH` |
| (d) corporate print | **UNQUERIED** | one `corporate_print` task and two `internet_archive` tasks, all blank, skipped by the breaker |
| (e) auction / museum | **UNTRIED** | nothing in `sources/`; the one skip not attributable to an outage |

## 4. Corrections this pass took, with the byte-level proof

These are the findings the merge must not lose, and each is registered (conflict row, data_gaps row, or
`sources.csv.notes`). The probe ran on 2026-09-26; the exhibit set arrived **2026-09-29/30** and the S-1 body
was re-fetched **2026-10-07**, so §14 rule 11 applies directly — the newest bytes are the ones that changed
the answers.

1. **COR-1 (biggest).** The probe wrote *"No EDGAR document can ever fix the founding day for this company"*
   and *"the day-level Delaware incorporation date … exist[s] only in the registry."* **Refuted:** Ex-3.3
   (acc. 0001193125-12-175673, filed 2012-04-23) recites **"The date of filing its original Certificate of
   Incorporation with the Secretary of State was July 29, 2004, under the name TheFacebook, Inc."** Caveats
   carried: it is a **FORM** (blank `Dated:` and signature block), the string is `July&nbsp;29, 2004` (so a
   plain grep for the date misses it), and `TheFacebook` occurs in **exactly 1 of 31** stored SEC documents.
   → **U.1**, `P1S03`, `P1-03`, `P1-18`.
2. **COR-2.** The probe's blanket *"`Saverin` 0 across the lineage"* is **refuted for the exhibit set**:
   "Saverin" appears once, in Ex-10.16A, as **"the Saverin Agreement"** — a defined term in a conversion
   agreement with Mail.ru/DST, never described. `Winklevoss`, `ConnectU`, `Divya`, `Moskowitz` remain 0
   everywhere. → `P1S05`, `P1-10`, **U.4**.
3. **COR-3.** The probe's framing that the dorm narrative is not in the filings needs splitting: `Harvard
   College` 0 and `February 2004` 0 confirmed, but **"our beginnings in a college dorm room in 2004"** is in
   the Business section of every lineage document that carries `dorm` (12 of them), and `Harvard` occurs in
   the director-biography sentence and the Pages sentence. So: the **place is in the filing** (FOUNDER CLAIM,
   year-level), the **month and day of the launch are not** → **U.5**.
4. **COR-4.** "Six in-window matters" → **seven**: `Leader Technologies Inc. v. Facebook Inc.`, 1:08-cv-00862,
   D. Del., `dateFiled` 2008-11-19, sits in the same payload inside the EDGAR-empty period. The EDGAR null
   stands; a litigation null must never be inferred from it.
5. **COR-5 (provenance, reported not repaired).** `0001193125-12-034517_d287954ds1.htm` on disk is
   **2,657,075 B / sha1 `d749855a…` / mtime 2026-10-07**, while its sidecar and `_MANIFEST.csv` record
   **2,627,682 B / sha1 `bf14d107…` / fetched 2026-09-29T19:05:37Z**. The 424B4's sidecar **does** match
   (`sha1 f7fa2eb2…`). I did not rewrite anything in `sources/`. Every quoted passage was read from the bytes
   currently at the path. → `P1S02.notes`, data_gaps row 11, §Boundary 6.

New independent dating this pass adds: **Series A financing "in 2005"** and the IRA descending from it;
**Breyer a director "since April 2005"**; **"In 2004 and 2005, Mr. Zuckerberg's father provided us with
initial working capital"** with the option that lapsed and the December 2009 cure to Glate LLC; the **2005
Stock Plan** with eleven dated amendment headers; **Zynga Developer Addendum No. 2 effective 2010-12-26**; the
**Wilson Menlo Park lease commencing 2011-02-07** to 2026-02-06; **credit and bridge facilities dated
2012-02-28**; and the audited comparative series **FY2007–FY2011**.

## 5. What part 2 (`s1-meta-p2`) inherits from this volume

- **Do not re-date the origin.** §K–§U must use **2004-07-29** (formation, Medium) and must not let it become
  a launch date; the launch stays **UNKNOWN** (`P1-14`, `P1-05`).
- **Anchors.** Part 1 declares `U.1`–`U.7`. **§U continues from `U.8` upward** and must either fold these
  seven entries into §U's body verbatim or renumber centrally and publish the map; the merge's 1:1 parity test
  compares conflicts rows against declared anchors, and part 1's declaration is explicit HTML
  (`<!-- ANCHORS: U.1-U.7 -->`) rather than inferred from headings.
- **Register overlap.** Part 1's quantitative rows are limited to what §A–§J cites (the FY2007–FY2011 series,
  the 2011-12-31 / 2012-03-31 metric set, the IDC and comScore figures, headcount, P&E, the 2,000,000-share
  cure). §P and §K will re-emit some of these; **p2's rows should be canonical**, deduplicate by
  (date, metric, source), and keep part 1's `notes` provenance labels.
- **Carriers already established for the money sections:** the father's working capital, the lapsed option,
  Glate LLC, the 2005 Series A and IRA, the named IRA parties (Andreessen, Thiel, Breyer, Accel, DST), the
  December 2010 Zynga addendum, the February 2012 credit/bridge facilities, and the fact that **no held
  document dates any venture investor to 2004**.
- **Restatement constraint.** §L, §M, §P and the 2008-2011 material can only be **RESTATED**: XBRL starts 2010
  (215 rows, zero before 2010), EDGAR is empty 2008-10-14 → 2012-02-01, and FY2007–FY2009 audited statements
  are recited but **not included** in the prospectus.
- **The `845 million MAU (2011-12-31)` row** is carried from the probe with `confidence Medium` and an explicit
  "not re-read by this pass" note. Whoever uses it must re-verify it against the S-1 body.

## 6. Refusals and non-claims (with the rule that forced each)

- **No launch date, no February, no first-capture date, no 2004-2006 user figure, no first customer, no first
  salary, no first ad price.** §1 (no invention) + §10 triggers; families (b)/(c)/(d) returned bytes only as
  failures, and failures are not evidence of absence (§12).
- **The "thirty days" growth claim was not given a substitute.** Measured: `thirty days` once (2005 Stock Plan
  exercise window), `30 days` 71 times (MAU definition, RSU settlement, contract boilerplate). Retraction left
  the value UNKNOWN rather than replaced it — §14 rule 8's corollary, and **U.6**.
- **"Facebook registered in 2005" was not written.** The 2005-06 `REGDEX` cluster is indexed and unattributed
  (**U.3**); the probe's prohibition is carried forward.
- **The pre-2004 acts were not attached to the corporation** (Facemash, Photo Manual: **0 hits**, and the
  alleged April-2003 Ceglia contract is an adversary's pleading about a person) — §4 of the shared brief and
  **U.2**.
- **The 2021 renaming was not dated.** EDGAR's `former_names` field is the only carrier here and carries no
  date; the act itself is outside this window (§Boundary 7, data_gaps row 9).
- **Market size was not read backwards.** The IDC figure is dated August 2011 and measures 2010; using it as a
  2004 motivation is the §6 contamination the firewall forbids (§H.1).
- **`TIER1_CANDIDATE` / `BARE_WORD_MATCH` harvest rows were not cited as evidence** (§3), including the 2006
  New Yorker row (metadata only) and the seven stored periodical texts.
- **Nothing in Amazon's dossier was imported.** `company_001_amazon/` was read for register headers and section
  shape only; the nine header lines were copied character-for-character and no value, date or phrasing came
  across.

## 7. Not examined by this pass (so the next one can decide)

S-1/A financial statements, share-ownership and underwriting sections (only origin strings were read from
those bodies); the `CORRESP` letters; the six `UPLOAD`/`.paper` items; the 26 history JPGs (no OCR); the FY2012
10-K (indexed, never stored); Zynga's/landlord's/banks' own copies; families (b), (c) re-runs, (d), (e); the
Delaware and California registries; the FTC and Ireland-DPC privacy material; anything post-2012-12-31; and
§K–§U entirely.

## 8. Fetch requests emitted (F-1…F-5), all for documents a script can reach

F-1 CDX `thefacebook.com` / `facebook.com` → `sources/web/`; F-2 Delaware certified copy of the original
certificate → `sources/legal/`; F-3 RECAP/PACER docket text for the seven matters → `sources/legal/`;
F-4 the six EDGAR paper items behind the 2005-06 REGDEX cluster → `sources/sec/`; F-5 the five `CORRESP`
letters and their `UPLOAD` responses → `sources/sec/`. Per §15.1 this pass **declined to fetch**; a declined
fetch is the correct behaviour, not a failure.

## 10. A live `s1-meta-p2` writer exists on this company — no path collision, but one real contradiction

Discovered at gate time (not before, because the dispatch assigned me one path and I did not read the others
until the gate enumerated the volumes): `_parts/s1_p2.md` (mtime 2026-10-07T03:18) and
`_parts/NOTES_meta_p2.md` (03:19) were written **while part 1 was being authored**. Per §14 rule 7 I touched
none of those paths; part 1 was appended only into `s1_p1.md`.

* **The anchor handoff worked.** Part 2 §U states in its own numbering note that it adopts part 1's `U.1`–`U.7`
  taxonomy verbatim and adds **`U.8`** (the truncated-index tooling artifact, the probe's META-C3), declaring
  `<!-- ANCHORS: U.1-U.8 -->`. Part 1's declaration remains `U.1`-`U.7`, so the union across the two volumes is
  `U.1`–`U.8` and each `§U.n` cross-reference inside part 1's §A–§J resolves. **No renumbering is needed from
  the merge, only the 1:1 parity check** (7 conflicts rows from part 1 + part 2's rows against `U.1`–`U.8`).
* **OUTBOUND CORRECTION FOR THE MERGE — part 2's day-level null is refuted.** `s1_p2.md` §K.2 and §U.1 CLAIM B
  both say there is **no certificate-of-incorporation exhibit anywhere in `sources/`**, that the day-level
  incorporation date is "unobtainable from EDGAR permanently", and that it lives only in the Delaware registry;
  `grep -c TheFacebook` in part 2 returns **0**. **Exhibit 3.3 of accession 0001193125-12-175673 (the S-1/A of
  2012-04-23), stored at `sources/sec/0001193125-12-175673_d287954dex33.htm` and fetched 2026-09-29, recites:
  "The date of filing its original Certificate of Incorporation with the Secretary of State was July 29, 2004,
  under the name TheFacebook, Inc."** Part 2 evidently read only the S-1 accession's own file list, which is
  where the probe's claim came from. Correct posture, which part 1's rows already carry: **EDGAR fixes the day
  at the company's own recital, in an unexecuted form, and only the registry can fix it as a record** — which
  is why `P1-03`/`P1S03` are `Medium` and `U.1` remains open rather than closed. Part 2's `§K.2` sentence and
  its `§U.1` CLAIM B should be superseded with a `[MERGE]` annotation; **do not delete part 2's paragraphs**
  (§14 rule 7 recovery rule), and note that part 2's `§K.1`/`§Q` dating of the earliest CIK row to 2005-05-06
  is correct and matches `P1S08`.
* **Part 2 also keeps the stage boundary at July 2004** (`§K` header line), which is the probe's architecture;
  part 1's registered conflict **`U.7`** records that the dispatched window is 2003→2012 and leaves the
  re-homing decision to the merge. Both parts are consistent about the facts and divergent only about which
  stage owns the 2004-2012 material.

## 12. Duplicate conflict-ids across the two volumes — an explicit outbound correction for the merge

**Both volumes emit `conflicts.csv` rows keyed `U.1`–`U.7`.** Part 1 emits 7 rows (this volume's §A–§J
adjudications); part 2 emits 8 rows, `U.1`–`U.8`, having adopted part 1's taxonomy verbatim and added `U.8`
(the truncated-index tooling artifact). Applied as written, the merge would create **seven duplicate
`conflict_id` primary keys**, which `tools/gates.py` fails on the `csv` gate. Per §14 rule 7's recovery rule —
never delete the other pass's work, declare one canonical, alias the rest — the recommended resolution is:

* **`U.8` is part 2's alone** and applies unaltered.
* **For `U.1`–`U.7`, part 1's rows should be canonical** because they are the ones carrying this pass's
  byte-level evidence: the Ex-3.3 recital behind `U.1`, the Ex-10.16A "Saverin Agreement" narrowing behind
  `U.4`, the `thirty days` / `30 days` census (1 and 71 occurrences) behind `U.6`, and the window carriers
  behind `U.7`. Part 2's seven rows should be aliased to them in a collision note, **keeping every
  genuinely-additive sentence in part 2's text** rather than discarding the rows.
* **Do not merge the volumes blindly on `U.1`.** Part 2's §K.2 and §U.1 still assert that no charter exhibit
  exists anywhere in `sources/` and that the day-level date is permanently unobtainable from EDGAR; part 2's
  own text contains **zero occurrences of `TheFacebook` and zero of `July 29, 2004`**, i.e. it never opened
  Ex-3.3. Part 1's `U.1` is the corrected version of the same conflict. If the merge prefers part 2's §U prose
  as the visible body, the adjudication content must still come from part 1's row.
* **`company` column literal differs between the volumes**: part 1 writes `Facebook Inc.` on every register
  row (the Stage-1 subject); part 2 writes `Meta`. Normalise to one literal at merge — `merge_census.py` and
  the primary-key gate will otherwise treat matching rows as distinct records. The same applies to
  `quantitative.csv` and `timeline.csv`, where both volumes emit the same filed figures (FY2007–FY2011 revenue
  and net income, the 2011-12-31 and 2012-03-31 user metrics, the 2005-05-06 index row, the 2004-09-02 docket
  row), so deduplicate on (date, metric) / (date, event) before appending.


## 13. Gate result as measured

`tools/gates.py --checks csv,keys,anchors,corrections --out 03_quality_control/meta_s1_gates_p1.md`:
**1 finding, 0 failing checks** — `coverage / registers: no register CSVs at root or research/ -- csv/anchors
gates DID NOT RUN`, which is the **expected pre-merge state** (the brief says coverage findings are not
defects, and nothing was invented to silence them). Recorded notes, not findings: `_parts/s1_p1.md declares an
explicit ANCHORS set (7 ids)`; `_parts/s1_p2.md declares an explicit ANCHORS set (8 ids)`;
`anchors: no register anchors found -- UNANSWERED, not passed`; `corrections: no CORRECTIONS.md -- gate DID
NOT RUN (not a pass)`; coverage census `0 registers, 2 stage volumes, 43 source documents`.
