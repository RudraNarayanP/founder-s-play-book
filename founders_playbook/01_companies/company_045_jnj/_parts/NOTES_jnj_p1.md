# NOTES — jnj Stage-1, part 1 (`s1-jnj-p1`)

**Owner:** s1-jnj-p1. **Path written:** `founders_playbook/01_companies/company_045_jnj/_parts/s1_p1.md`
(only file written besides this one and the gate). **Date:** 2026-10-07. **Tool calls used:** ~100 of 130;
closed out per the dispatch's 100-call rule, section by section, each marked `STATUS: WRITTEN` as I went.
**Web budget used:** 0 WebSearch / 0 WebFetch. Everything below was reached by reading bytes on disk.

## What was claimed, and against which probe findings

* **Tier: T2 core — PROVISIONAL, inherited, not re-tiered** (probe §4). I logged disagreement in place
  (U.008, U.012) rather than enacting it: the two families returning in-window Tier-1 text are still two,
  because the newly arrived SEC bodies are all post-1960.
* **The origin is written as a range inside a retrospective**, per the probe's finding, and **sharpened**: the
  same lineage tells the story twice, and the *later* volume collapses the range `1886-*87` into the single
  year 1886 while adding a corporate leg (`began in business in 1886; in 1887 they became a corporation`).
* **Probe §5.1's `Incorporation: tested directly and not found` is superseded.** I reproduced the probe's
  adjacency regex and its **0** result exactly, then found the statement at `redcrossnotes01` L5717-5719. The
  zero was a **same-line requirement in two-column OCR**, not an absence. Registered as U.002; the probe's
  *no NJ charter is in the corpus* half stands untouched.
* **Probe §5.2's `no document calls anyone a founder` holds**, and I measured it three ways (same-line 0;
  ±2-line 1 non-company hit about a USP committee; `three brothers` 0; `brother(s)` within ±3 lines of a
  naming 0; `James Wood` 0; `Miles Stone` 0; `Earle Dickson` 0; `Band-Aid` 0). Roles only: RWJ printed as
  *Manufacturing Chemist, President Johnson & Johnson Corporation* (≥1893 bounded by the volume's own
  citation of the 1893 Pharmacopoeia — **I did not inherit the probe's 1894**).
* **Probe §3(d)'s `asepsissecunduma00john … authorship UNESTABLISHED` is superseded on bytes**: the title page
  prints firm, `ASEPTIC LABORATORIES`, `NEW BRUNSWICK, NEW JERSEY`, `1897`, `COPYRIGHT, 1897`.
* **Probe §3(d)'s `redcrossnotes01 … 1910` is unsupported**: the layer's own copyright legs are 1914/1915/1919,
  so the retrospective lag on three load-bearing claims moves from 24 years to 33+ (U.006).
* **Probe §3(c) locator and classification defects registered, not silently fixed**: `americandruggis29`
  l.25490 / l.36865 are in `americandruggis**07**` (U.009); and `americandruggis07` l.45597
  (`Robert Wood Johnson. The objects of`) is **not a company naming** — it is an incorporator list for the
  **New York Red Cross**, with 0 entity namings within ±25 lines (U.010). The Red Cross collision is live
  because the company's own organ and cotton carry that device.
* **New material this pass, none of it in the probe:** the 1896 outsider factory report (Vol XXVIII leg read
  on-page); the 1898–99 **four-firm plaster price agreement and its 1904 rate-war collapse** (Vol XLV,
  dateline Philadelphia August 17 + sequel); the **1902 stamp-tax suits** ($40,800 aggregate; the Commissioner
  decided against the firm); the **1899 Red Cross imitation bill in equity** against Seabury & Johnson, printed
  by the firm and calling it *which corporation*; the **1904 marriage paragraph** naming
  `Robert W. Johnson (Johnson & Johnson)` of New Brunswick with a $100,000 securities gift; the **anonymous
  first-person** origin passage (`When I started Johnson & Johnson…`, unstable I/We, hedging `in or about the
  year 1886`); the 1897 priced `Aseptic Armamentarium $5.00`; the 1901 `$6.0U` cabinet; the printed Papoid
  price cut with the new figure OCR-corrupt; the `1886-*87` **asterisk is OCR, not an apostrophe**
  (`1886-'87` occurs 0 times in held bytes).

## Corpus state, re-enumerated (§14 rule 11)

**15 layers / 23,308,643 B / 642 namings** (probe: 14 / 23,275,060 / 619). The delta is `John0851_1970`
(33,583 B, fetched 2026-10-06, 23 namings) — a **company 1970 annual report** whose bytes carry 23 namings
while `research/A4_harvest_mine.md` records it as **NULL, 0 word hits, 0 entity hits** (U.011). It is `(PB)`,
and its load-bearing in-window value is negative: **0 occurrences of `1886`** in the earliest company annual
report on disk. Also new since the probe: **26 SEC bodies / 4,671,102 B (1994–1999)**, all `(PB)`; the probe's
`SEC document bytes held: 0` is stale (U.008). EDGAR re-measured by me: 3,371 rows, earliest 1994-03-10,
latest 2026-09-10, 65 forms, **0 forms beginning `S-1`, 0 rows ≤ 1960-12-31**, 134 rows with no
`primaryDocument`; generic + CIK-keyed duplicate artefacts both present (RD-098 vector, **not deleted**).

## Windows proposed, not inherited

The harvester's `1886-01-01 → 1960-12-31` is treated as a **search setting**. §Boundary proposes
**Stage 1 = 1886\*–87 → 1904-12-31**, each edge carried by a document I read (open: the range sentence;
close: Vol XLV Jul–Dec 1904, the last dated naming carrier), rejects 1886→1960 with the reason
(no in-window held document between 1905 and 1960 except the 1914–1919 house-print legs), and rejects
1886→1919 as the close while adopting it as the Stage-1→Stage-2 hand-off. **Stage 2/3 windows remain unset**
— the probe's RD-112 reasoning holds and I did not date a hand-off to a document I have not read.

## Five families as measured here

(a) **TRIED–ANSWERED, documented in-window NULL** (with UNANSWERED sub-slices: 134 shell rows, `_SKIPPED.csv`,
`_UNANSWERED.csv`). (b) **UNTRIED as a scripted family** — `tools/web_domains.json` has **no `jnj` entry**
(verified by grep), so `cdx_intake.py` has never run for this slug; the probe's 1996 CDX floor is recorded as
an ad-hoc two-URL measurement, not as family (b) answered. (c) **TRIED–ANSWERED with Tier-1 in-window text**,
47 namings in 5 volumes, and **790 of 795 unopened; 44 of 44 *Pharmaceutical Era* unopened**. (d)
**TRIED–ANSWERED, the richest and the self-narrative** (504 of 642 namings). (e) **UNTRIED — has no tool**
(`tools/HARVEST_README.md` family 4, *not implemented*). Chronicling America **UNANSWERED** (7 shapes
CHALLENGED), never a null.

## Deliberate refusals and judgement calls

* The **`Seabury & Johnson`** collision is treated as a first-order hazard (a "& Johnson" competitor in the
  same commodity, same state, listed beside the registrant in the price agreement and as defendant in its
  suit). No row anywhere attributes a Seabury act to J&J.
* `Messrs. Johnson & Johnson` / `The Johnsons` / the anonymous `I` are reported as **printings**, never
  resolved into persons; the 1904 `Robert W. Johnson` and the 1893-or-later `Robert Wood Johnson` are **not**
  merged into one man except as an explicitly labelled inference.
* **No revenue arithmetic.** The 370,000 / 7,000 counts and the $6.00 / $5.00 prices are kept in separate
  registers with a written prohibition on multiplying them (§E.2).
* The 1899 equity narrative and the 1904 `plaster trust` sentence are quoted **with the trade paper's own
  denial attached**, and no legal conclusion is drawn (no outcome of either suit is held).
* 163 `1886` lines in the Canadian `alphabetfirstth00goog` (126 `New Brunswick`, 0 namings) and the
  `ErnestFairfield` 1888 layer were read and **refused** as evidence; they are emitted only as one control
  register row.

## Gate

`python tools/gates.py --company-dir founders_playbook/01_companies/company_045_jnj --tier auto --checks csv,keys,anchors,corrections --out founders_playbook/03_quality_control/jnj_s1_gates_p1.md`
→ **`_parts/s1_p1.md` declares 12 anchors**, matching 12 conflicts rows 1:1. Findings are coverage-only and
expected pre-merge: `no register CSVs at root or research/ — csv/anchors gates DID NOT RUN`,
`no CORRECTIONS.md — gate DID NOT RUN (not a pass)`, 1 coverage finding of 1, exit not failing
(`--fail-on substantive`). **Nothing under `sources/` was created, moved, pruned or "tidied"**; the duplicate
`submissions.csv` / `submissions_CIK0000200406.csv` pair was left in place and reported instead.
Every one of the 9 fenced CSV blocks machine-checks at header width (16+21+18+8+7+5+4+12+11 = **101 rows,
0 column drift, 0 empty cells**), re-checked after the last write.

## Defects seen this pass (not worked around)

1. Sidecars carry **no year at all** (`identifier,url,fetched,bytes,route,note,transport`), so any inherited
   date in the probe is unverifiable from metadata; dating had to come from printed volume legs. This is the
   root cause of U.004/U.006/U.010-class defects.
2. The harvest index's `NULL` for `John0851_1970` contradicts its bytes (23 namings) → **harvest NULL counts
   cannot bound coverage for this slug**.
3. The probe's incorporation regex is **line-bound** and blind to two-column OCR; the same shape will hide
   other "0 line" findings in this corpus.
4. Every layer is **UNVERIFIED TLS**, which caps the whole volume at Medium — a transport property, fixable by
   a script run (U8 in the part file), not by research.
5. `tools/web_domains.json` has no jnj slug, so family (b) is UNTRIED even though a domain string is printed
   in the SEC bodies already on disk (FR-4).

## Not examined

The 26 SEC bodies beyond machine-counting; the 790 unopened Druggist items; the 44 *Pharmaceutical Era*
volumes; HathiTrust; any auction/museum holding; any court record; `_SKIPPED.csv` slots; `00_universe/`
metadata. Amazon was read for **format only** — no value, date or phrasing imported.
