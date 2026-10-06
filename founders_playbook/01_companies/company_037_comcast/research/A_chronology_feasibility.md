# A — Chronology-Feasibility Probe — company_037_comcast (Fortune rank 37)

Agent: `probe-comcast` · Stage: **Stage-1 feasibility PROBE** · Dataset: Founder's Playbook
Web budget used: **0** (all retrieval through scripts + local grep; no WebSearch/WebFetch).
Tool calls used: ~16 of 85 (stopped opening new routes well under the 70 ceiling).

**PLANNING / PROBE TIER (named in this header, because `gates.py` assumes `exemplar` when no tier is
stated — the RD-122/RD-123 hole): `T3 register`, PROVISIONAL.** See §4/§5.

Hindsight-firewall statement: nothing below treats Comcast's later scale as evidence that the 1963
financing was rational, obvious, or correctly recounted. The origin window has **no document on disk**;
the popular money-raising account is tested against held bytes and is not corroborated here.

---

## 1. Context measured tonight (verbatim tool output — every quantifier below is a grep/run, per hard rule 8)

**Full EDGAR walk (not the RD-134 8-slice cap):**
```
python tools/sec_intake.py index "Comcast Corporation" --company-dir .../company_037_comcast --max-slices 200
identity: 'Comcast Corporation' resolved to CIK 1166691 (COMCAST CORP) by name-exact
walk: 2 slices (2 fetched, 0 failed), 3515 filing rows, date perimeter 2002-02-11 -> 2026-10-02
```
→ registrant CIK **1166691**; **date perimeter 2002-02-11 → 2026-10-02**; walk reached every slice (2 of 2).

**In-window XBRL pass:**
```
python tools/sec_intake.py facts ... --from 1963-01-01 --to 1990-12-31
facts: NULL -- NO DATA FILE WRITTEN. WINDOW: 0 of 25,048 observations ... XBRL coverage runs
2006-12-31..2026-06-30, and 468 tags are present, so the absence is EDGAR's XBRL start date (~2007 ...),
not a fetch failure ... Early-window money figures must come from the filings themselves.
```
→ in-window stored = **0 documents** (matches brief). Cause: this registrant's whole EDGAR identity is
2002+; pre-2002 Comcast history is under a **different (legacy) CIK** this probe did not enumerate.

**Forward recital route (method §"the recital route"):**
```
python tools/sec_intake.py auto "Comcast Corporation" ... --from 2002-01-01 --to 2002-12-31 --max-docs 30
walk: 2 slices ... date perimeter 2002-02-11 -> 2026-10-02
auto: 11 accessions in window, ... 30 kept under --max-docs 30, 1 skipped past the cut
auto: 30 documents stored (18070799 bytes, 2392834 words); 1 UNANSWERED ... 1 SKIPPED
```
→ forward recital stored = **30 documents**, floor **2002-02-11**. The **earliest filing per form** in
`_INDEX_CIK0001166691.md` is `S-4 | 2002-02-11` — **no form appears before 2002**.

**Held bytes enumerated (rule 8):**
```
SEC txt: 30 | sec meta: 30 | corporate_print: 0 | periodicals: 12 files (6 docs + 6 sidecars) | web_archive: 0
```
→ brief's "12 periodicals" = **files**; distinct periodical **documents = 6** (all `Broadcasting` magazine,
1987–1990). 30 SEC, 0 corporate print, 6 periodicals, 0 web. Earliest held doc of any family = **1987**
(periodical); earliest company-authored Tier-1 = **2002-02-11** (SEC S-4).

---

## 2. Window (PROPOSED — `00_universe/fortune_top_50_2026.csv` has NO founding-date column)

A filename / harvest parameter is a search setting, not evidence (RD-112). Windows are **PROPOSED** and
split where the evidence cannot itself fix a boundary:
- **Stage 1 (origin → formation): PROPOSED 1963-01-01 → 1976-12-31** — the small Mississippi-neighborhood
  system and its financing, the re-formation (American Cable Communications of Delaware / Comcast Cable
  Communications), and the first public formation. **No document on disk in any family.**
- **Stage 2 (scaling to a major MSO): PROPOSED 1977 → 1990-12-31** — top bound = measured candidate
  window. Held family (c) text lives here.
- **Stage 3 (modern registrant): 1991 → present** — CIK 1166691's own EDGAR history (2002+). Out of this
  probe's deliverable; SEC is abundant there.
- The task's measured candidate window **1963-01-01 → 1990-12-31 (PROPOSED)** deliberately spans Stage 1
  + Stage 2 because the founding date is unestablished; narrowing it would discard the evidence that could
  establish it.

---

## 3. Five-family verdict table (every family gets an explicit verdict; three states only)

| # | family | verdict | measured basis (file/command) | in-window Tier-1 for Stage 1? |
|---|--------|---------|-------------------------------|-------------------------------|
| a | SEC / EDGAR | **TRIED–ANSWERED (perimeter only)** | full walk `2002-02-11 -> 2026-10-02`; window facts = 0/25,048; earliest form S-4 2002-02-11 | NO (0 docs in 1963-1976) |
| b | web archives | **UNTRIED** | 0 CDX/Wayback calls; `sources/web_archive/` empty | NO (untried; and floor is mid-1990s) |
| c | periodical corpora | **TRIED–UNANSWERED for the founding event; in-window YES at the 1987-1990 tail only** | 6 held `Broadcasting` docs, all 1987-1990; harvest mine 31 candidates / 6 mined / **24 untried**; founding-decade (1963-76) never reached | 0 for 1963-1976; 2 verified name-mentions for 1987-1990 |
| d | digitised corporate print | **UNTRIED** | 0 held; no RD-130 facet-free query run this pass | NO (untried) |
| e | auction / museum / manuscript | **UNTRIED** | 0 calls | NO (untried) |

A pre-2002 EDGAR silence is reported as a **measured perimeter** (walk floor 2002-02-11) plus a
**wrong-CIK successor-matter** (founding-era filings sit under a legacy CIK), **not** as "Comcast filed
nothing" (rule 8 / RD-134). An untried family is never a null (method §family rule).

---

## 4. Per-stage tiers (RD-112: measured against that stage's own window) and the families that counted

§15.2 counts **families returning in-window Tier-1 text**.

- **Stage 1 (1963→1976): 0 families** return in-window Tier-1 text (a=0, c=0-in-this-sub-range, b/d/e=UNTRIED)
  → **T3 register, PROVISIONAL**. Provisional, not final: the one family that could carry the founding
  (c periodicals, and d corporate print) was **never queried for 1963-1976**; 24 harvest rows sit untried.
  Under RD-112 this is the Costco/"family (c) went untried" case → **PROVISIONAL**, not "not provisional".
- **Stage 2 (1977→1990): 1 family** (c) returns in-window Tier-1 text — 2 `Broadcasting` docs verified in
  bytes to name the registrant (contemporaneous, Tier-1) — but **none recites the origin** → **T3**.
- **Stage 3: T1-capable** on family (a) alone (3,515 filings), but this probe does not deliver Stage 3.
- **Planning tier = the minimum = T3 → ~3-4 agent runs, not 15-20.** Say which counted: only (c), and only
  for *naming* at 1988-89. Which are provisional: (b), (d), (e) untried; (c) untried for the founding decade.

---

## 5. Carriers found for the origin / predecessor question (file + line)

**There is NO carrier for the 1963 Mississippi event in any family on disk.** The only Tier-1 carriers that
name the registrant, and what they actually say (verified in bytes, not in the index column — rule 6/RD-124):
- `sources/sec/0000950123-02-001136_e56461s4s-4.txt` — S-4, filed **2002-02-11**: the *modern successor*
  registrant's AT&T Broadband registration statement. Not a founding recital.
- `sources/periodicals/bc-1988-11-14_djvu.txt:18769` → `Comcast Corporation` (adjacent line `Tele-Communications,
  Inc.`) — a **listing/roster entry**, not origin.
- `sources/periodicals/bc-1989-01-16_djvu.txt:15650` → `chief financial officer of Comcast Corp.` (Julian
  Brodsky, quoted about a 1989 deal) and `:16218` → `MSO's Comcast Corp.` in a J. Bruce Llewellyn/Lenfest
  partnership deal — **contemporaneous naming**, Tier-1, but 1989, not the 1963 story.

Predecessor/identity note (rule 5): CIK **1166691** `COMCAST CORP` (tickers CMCSA/CCZ), whose EDGAR record
begins 2002-02-11, is the **successor** registrant. The 1963 system, American Cable Communications of
Mississippi / of Delaware, and Comcast Cable Communications sit under a **legacy CIK not enumerated here**.

---

## 6. THE TRAP, tested against held bytes (this company's specific trap)

The popular account — a small 1963 Mississippi-neighborhood system financed by a handful of professionals —
circulates in three forms. Each was tested against the bytes actually held:

1. **A founder's own later retelling of how the money was raised** → class **FOUNDER CLAIM (retrospective
   memory)**. Present in held bytes? **NO** — no founder transcript/interview on disk; `grep` of the 30 SEC
   docs for an incorporation/origin recital returned **0 genuine hits** (only Irish "Companies Acts, 1963 to
   2001" boilerplate at `...y62410a2sv4za.txt:12353` and "Funded (unfounded) benefit obligation" at
   `...e56461s4s-4.txt:41048`). A retrospective retelling cannot be corroborated by anything on disk.
2. **A 1980s prospectus restating 1963** → a **RESTATED source = ONE lineage** (method §3 filing-lineage
   rule). Present? **NO** — the only company-authored Tier-1 on disk is the 2002 S-4, and it does **not**
   restate a 1963 founding (grep 0). If such a prospectus is later fetched, restating 1963 twice (prospectus
   + its amendment) is one source, not corroboration.
3. **The registrant's Delaware formation date is NOT the 1963 event.** Confirmed from bytes: CIK 1166691's
   earliest filing is **2002-02-11**, and no `incorporated in 19xx` / `Delaware in 19xx` recital exists in
   the held files (grep 0). Even if a Delaware incorporation year surfaces in the legacy-CIK filings, it is
   the successor entity's registry date, not the 1963 Mississippi franchise. Where the window has no
   document, the answer is a **measured perimeter** (§3) plus the **UNTRIED families below** — not the
   founding date.

---

## 7. What I refused to claim, and why

- Refused to **date the founding** from the 2002-02-11 EDGAR floor, any filename, or a harvest parameter (rule 5 / RD-112).
- Refused to **promote the two periodical name-mentions to origin evidence** — verified in bytes they are a
  roster entry and a CFO title in a 1989 deal, not a founding recital (rule 6 / RD-124).
- Refused to report EDGAR **"silent"** for the window as absence of filings — it is a measured perimeter for
  CIK 1166691 plus a legacy-CIK gap (RD-134).
- Refused to **count folklore** (the "handful of professionals" money story) that is not on disk (rule 8).
- Refused to treat the "1963 / founded / Mississippi / Roberts / Gillett" grep hits as origin text — all are
  decoys or non-origin: Irish Companies Acts; "unfounded/ill founded"; "Cohen founded his own PR firm 1983";
  Kohlberg Kravis **Roberts**; George Gillett in a **1990** $365M radio deal; "Mississippi Association of
  Broadcasters"; Batesville, MS. None recites the 1963 system.

---

## 8. ## Untried (an untried family may never be reported as a null)

- **Family (c) — FOUNDING-DECADE TRADE PRESS, 1963–1976.** The 6 held `Broadcasting` docs are all 1987–1990;
  **24 harvest-mine candidate rows are untried** (`_index.json`: candidates 31 / mined 6 / untried_by_limit 24).
  A small 1960s MSO is exactly the company whose founding/financing survives in **cable/broadcast trade
  press** (`Broadcasting`, and the cable-side weeklies it folded). **This is the trade route I did not get to.**
- **Family (d) — corporate print.** Comcast's own early annual reports/house organ and 1970s cable-industry
  directories/rosters naming the Mississippi system: **0 held, no facet-free (RD-130-safe) query run.**
- **Family (e) — auction / museum / manuscript.** Ralph Roberts / Comcast corporate archive, Mississippi
  local-historical-society holdings, dealer catalogues for a 1963 franchise document: **UNTRIED, 0 calls.**
- **Family (b) — web archives.** No CDX/Wayback call; irrelevant to 1963 but the likely carrier of a
  company "about" page (a FOUNDER-CLAIM source, Tier-4 → chase to origin): **UNTRIED.**

## 9. FETCH REQUEST (no script on this probe can reach these; rule 1 — refusing the fetch is correct behaviour)

```
FETCH REQUEST:
  target: the LEGACY Comcast registrant CIK(s) covering American Cable Communications of Mississippi /
          of Delaware and Comcast Cable Communications, Inc. (pre-2002, i.e. NOT CIK 1166691).
  action: python tools/sec_intake.py resolve --cik <legacy> then index/auto over any window holding an
          origin recital (a 1980s-1990s S-1/S-3 or 10-K "Business: history" paragraph).
  claim it would settle: whether a filing — as opposed to folklore — ever states the 1963 Mississippi
          financing; and the Delaware formation year, correctly separated from the 1963 event.
  status of that element if unfetched: UNTRIED / UNANSWERED.
FETCH REQUEST:
  target: 24 untried harvest-mine rows for `comcast`, re-mined filtered to Broadcasting + cable trade
          press in 1963-1976 (family c). Tonight's harvest-mine run (task #24) is the carrier.
  claim it would settle: contemporaneous Tier-1 text for the founding decade.
```

## 10. Route most likely to change the verdict

**Re-mining family (c) over the 1963–1976 founding-decade trade press (`Broadcasting` / cable weeklies) and,
in parallel, family (d) for a 1970s cable directory entry — if either returns a contemporaneous naming of the
1963 Mississippi system, Stage 1 moves from `T3 PROVISIONAL` toward `T2 core` (trade press of 1963 = family
(c) Tier-1; a later restating prospectus/roster = family (d) = a second, differently-sourced family), which
is the only path to a higher planning tier.**

## 11. A4 re-read (rule: re-read before quoting, give mtime)

Re-read `research/A4_harvest_mine.md`. **mtime 2026-09-29 23:28:56 +0530, 3,960 bytes** (`stat`). It records
"31 candidate rows … 6 items mined; 24 left untried at the --limit" and stamps `bc-1988-11-14` and
`bc-1989-01-16` as `TIER1_CANDIDATE_TEXT`. Per RD-124 I did **not** trust the label: I opened the bytes and
confirmed those two `entity_hits` are the registrant being **named** (roster entry; CFO title), **not** a
founding recital — so they count for Stage 2 naming, and contribute nothing to the Stage-1 origin.

## 12. Gate (ran before reporting)

```
python tools/gates.py --company-dir .../company_037_comcast --checks csv,keys --fail-on substantive \
  --out founders_playbook/03_quality_control/comcast_s1_probe_gates.md
Findings: 2 | Passes: 0
| coverage | registers  | no register CSVs at root or research/ -- csv/anchors gates DID NOT RUN |
| coverage | narrative  | no stage_*.md volumes found -- keys/anchors gates DID NOT RUN |
```
Both findings are **coverage-only** (a gate had no input yet), expected for a freshly probed company; the
run wrote no register rows, so `--fail-on substantive` is **not** triggered → **gate passes for this probe**.
The report printed `tier: exemplar (no tier stated … exemplar assumed)` — the RD-122/123 hole; hence the
tier is stated in this header as **T3 PROVISIONAL**.

## 13. Claim records (dossier-local P-ids; no global `source_id` minted — that happens at merge, §13)

P01 Claim: CIK 1166691's EDGAR record begins 2002-02-11, so no filing exists in the 1963-1990 window. —
Date: 2002-02-11 — Source: sec_intake full walk + `_INDEX_CIK0001166691.md` — Source date: 2026-10-06 —
URL: — — Archived: — — Tier: 1 — Class: FACT — Passage: "date perimeter 2002-02-11 -> 2026-10-02" —
Conf: High — Corroboration: 1 (perimeter) — Conflicts: None.

P02 Claim: the in-window XBRL pass stored 0 documents; the absence is EDGAR's start, not a fetch failure. —
Date: UNKNOWN — Source: sec_intake facts window output — Source date: 2026-10-06 — URL: — — Archived: — —
Tier: 1 — Class: FACT — Passage: "WINDOW: 0 of 25,048 observations" — Conf: High — Corroboration: 1 — Conflicts: None.

P03 Claim: no held SEC document recites the 1963 founding or a Delaware formation year. — Date: UNKNOWN —
Source: grep of 30 held SEC txt for incorporation/origin recital — Source date: 2026-10-06 — URL: — —
Archived: — — Tier: 1 — Class: FACT (negative, measured) — Passage: "NO_VERBATIM_PASSAGE_RECORDED" (0 genuine hits) —
Conf: High — Corroboration: 1 — Conflicts: None.

P04 Claim: the forward recital route stored 30 company-authored Tier-1 documents (18,070,799 B). —
Date: 2002-02-11 — Source: sec_intake auto 2002 window — Source date: 2026-10-06 — URL: — — Archived: — —
Tier: 1 — Class: FACT — Passage: "auto: 30 documents stored (18070799 bytes, 2392834 words)" — Conf: High —
Corroboration: 1 (same S-4 lineage family) — Conflicts: None.

P05 Claim: `bc-1989-01-16:15650` names Comcast Corp only as the employer of CFO Julian Brodsky, not as a founding. —
Date: 1989-01-16 — Source: Broadcasting Magazine (Jan 16, 1989) — Source date: 1989-01-16 — URL: — —
Archived: sources/periodicals/bc-1989-01-16_djvu.txt — Tier: 1 — Class: CONTEMPORARY OBSERVATION —
Passage: "chief financial officer of Comcast Corp.," — Conf: High — Corroboration: 1 — Conflicts: None.

P06 Claim: `bc-1988-11-14:18769` names Comcast Corporation in a roster alongside Tele-Communications, Inc. —
Date: 1988-11-14 — Source: Broadcasting Magazine (Nov 14, 1988) — Source date: 1988-11-14 — URL: — —
Archived: sources/periodicals/bc-1988-11-14_djvu.txt — Tier: 1 — Class: CONTEMPORARY OBSERVATION —
Passage: "Comcast Corporation" — Conf: High — Corroboration: 1 — Conflicts: None.

P07 Claim: the "small 1963 Mississippi system financed by a handful of professionals" money-raising account is
unsupported by any held document. — Date: 1963 (event) — Source: — (no carrier on disk) — Source date: UNKNOWN —
URL: — — Archived: — — Tier: UNKNOWN — Class: FOUNDER CLAIM (retrospective) — Passage: NO_VERBATIM_PASSAGE_RECORDED —
Conf: UNKNOWN — Corroboration: 0 — Conflicts: None.

P08 Claim: 24 of 31 harvest-mine candidate rows (1963-1976 trade press) are UNTRIED; the founding decade was never queried. —
Date: UNKNOWN — Source: `sources/harvest_mine/_index.json` — Source date: 2026-09-29 — URL: — — Archived: — —
Tier: 1 (index row = pointer only, not evidence — rule 6) — Class: FACT (state=UNTRIED) —
Passage: "candidates: 31, mined: 6, untried_by_limit: 24" — Conf: High — Corroboration: 1 — Conflicts: None.

---

### Report-back (mirrors the dossier)
- **Path:** `founders_playbook/01_companies/company_037_comcast/research/A_chronology_feasibility.md`
- **Planning tier:** **T3 register, PROVISIONAL** (min across stages). Stage 1 (1963-76) = 0 families; Stage 2
  (1977-90) = 1 family (c, naming only); Stage 3 T1-capable (not delivered here). Families that counted: (c)
  only, for naming at 1988-89. Provisional/untried: (b), (d), (e); (c) founding decade.
- **Five-family verdicts:** (a) TRIED–ANSWERED perimeter 2002-02-11→2026-10-02, 0 in-window; (b) UNTRIED;
  (c) TRIED–UNANSWERED for origin, in-window Tier-1 only 1987-90 (6 docs / 2 verified namings); (d) UNTRIED; (e) UNTRIED.
- **Carriers for origin/predecessor:** none for 1963; 2002 S-4 (`...e56461s4s-4.txt`, successor registrant);
  1988-89 `Broadcasting` namings at `bc-1988-11-14:18769`, `bc-1989-01-16:15650`/`:16218`.
- **Untried:** founding-decade trade press (24 rows), corporate print (RD-130 facet-free query), auction/museum, web archives.
- **FETCH REQUESTs:** (1) legacy Comcast CIK origin recital; (2) re-mine 1963-1976 harvest rows.
- **Refused to claim:** the 1963 financing story; a founding date read off the 2002 floor/filename; periodical
  namings as origin; "EDGAR silent" as absence; the "1963/founded" grep hits.
- **Route most likely to change the verdict:** re-mine family (c) over 1963-1976 trade press (+ family (d)
  cable directory) → could lift Stage 1 toward **T2 core**.
- **Gate:** `comcast_s1_probe_gates.md` — 2 coverage-only findings, 0 passes, `--fail-on substantive` not triggered.
- **Web calls: 0.**
