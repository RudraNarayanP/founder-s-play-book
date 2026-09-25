# A2_periodical_settlement.md

<!-- SCAFFOLDED by tools/scaffold.py at 2026-09-25T19:51:31Z. STATUS: nothing written yet. Any agent reading this: the owner has a live claim; do NOT write this path. Every PENDING below is an unwritten section. -->

## Route used

STATUS: WRITTEN — 2026-09-26, agent periodicals-alphabet

Tool: `python tools/ia_text.py` (`search`, `fetch`, `grep`) as briefed, with `--insecure`. Web budget
used: 0. Every retrieved byte was written under
`founders_playbook/01_companies/company_005_alphabet/sources/periodicals/`.

**Three route defects found and worked around (none is a fact about Google):**

1. `ia_text.py search` cannot enumerate. `search()` builds the URL with
   `urllib.parse.urlencode({"fl[]": fl, ...})` **without `doseq=True`**, so the field list travels as
   the Python repr `fl[]=['identifier', 'title', ...]`. advancedsearch answers 200 with field-stripped
   docs: `--q 'title:("Popular Electronics") AND year:1975'` → `{"num": 1, "items": [{}]}`. Because
   `mine` then does `if not ident: continue`, **`mine` can only ever report zero items** — a silent
   no-op that reads as "searched, nothing found". Enumeration here used a stdlib urllib call passing
   `fl[]=identifier&fl[]=title&fl[]=year&fl[]=collection` correctly.
2. `ia_text.py fetch` does not percent-encode the text-layer filename. This subject's periodicals store
   OCR under names containing spaces (`Yahoo Internet Life Magazine July 2000_djvu.txt`, 361,043 B,
   format DjVuTXT — read from the metadata API, per the `_djvu.txt`-convention warning). `fetch`
   requests it raw, gets 404, and reports `UNANSWERED -- no text layer resolved`. **The tool's failure
   is indistinguishable from an item with no OCR.** Its bytes were retrieved by encoding the path
   (`%20`) and are held, with a sidecar naming the route.
3. Requests without the tool's `User-Agent` are refused from this egress (empty body / non-JSON); with
   `FounderPlaybook Research AdminContact@example.com` the same URL returns 200 JSON.

TLS: all fetches used unverified transport (`--insecure`, stale local CA store), so **every byte below
arrived UNVERIFIED**; sidecars carry `"transport": "UNVERIFIED TLS"` and none may be cited at High
confidence until re-checked. Both traps were respected: bare quoted terms expand to
`(text:"…" OR text__reviews:"…")` — visible in the `responseHeader` — i.e. **uploader annotations, not
page OCR**, so no verdict rests on a search hit; and 0-row searches are recorded as UNANSWERED. Range
grammar was proved live the same session (`collection:(internetarchivebooks) AND year:[1998 TO 2004]`
→ numFound 860,362), so a zero is not always a syntax error — and never a proven absence.

## Held-bytes census

STATUS: WRITTEN

| # | identifier | what it is | bytes held | date seen **in the bytes** |
|---|---|---|---|---|
| 1 | `bub_gb_fBsEAAAAMBAJ` | Network World (tech trade press) | **304,352** | masthead `MARCH 30. 1998 VOLUME 15, NUMBER 13`; running head `Network World • March 30, 1998` |
| 2 | `bub_gb_VA0EAAAAMBAJ` | Network World (tech trade press) | **536,111** | `NEWS BRIEFS. MAY 10, 1999`; `90 Network World May 10, 1999` |
| 3 | `yahoo-internet-life-magazine-july-2000` | Yahoo Internet Life (consumer tech monthly) | **361,043** | metadata `date: 2000-07-01`; in-text `Search the Web, Part Il` feature |

Total periodical OCR held: **1,201,506 B (≈1,173 KB)**. These are authentic full-issue OCR, not
snippet stubs: line 1 of #2 reads `CISCO'S FUZZY WAN PLAN` and control words behave as expected in a
network-trade issue (`network` 441 lines / `Cisco` 68 in #1; `network` 1,002 / `router` 108 in #2).
So the zero counts below are nulls over real kilobytes, not over empty files.

Pre-existing bytes in this company's `sources/`, not periodical print, not re-adjudicated here:
`sources/ia/cia_1487901_djvu.txt` (16,305 B, a CIA Reading Room item fetched 2026-09-25 by the filings
pass) — held but untested against the founding question (see *Untried*).

## 1998-2004 corroboration question

STATUS: WRITTEN

**Does any in-window periodical independently corroborate the September-1998 founding story the S-1
tells? ANSWER: NO — not on the bytes held this session.**

Across all 1,173 KB, `(Larry Page | Sergey Brin | BackRub | "Page and Brin")` returned **0 hits in all
three items**, and `(founded | launch | start)` within 60 chars of `(1998 | Stanford)` returned **0
hits** in the only item carrying any Google text. Neither Network World issue mentions Google, Overture
or Go2Net on any line (`google` 0, `overture` 0, `go2net` 0, `cost per click`/`pay-per` 0 over 840 KB).
The origin **event** — the date, the two Stanford PhD students, the September-1998 California
incorporation — therefore still rests on exactly what the probe had: one lineage (the S-1's own
account, a FOUNDER CLAIM in a Tier-1 wrapper), plus the Stanford patent filing of 1998-01-09 and the
Wayback capture of 1998-11-11. This pass added nothing to that tripod.

**What the held periodical does corroborate, from outside the EDGAR lineage, is existence and character
in-window.** Yahoo Internet Life, July 2000, ranks Google fourth in its "Search the Web, Part II"
round-up — held lines 11027-11033:

> `4, GOOGLE / [google.com] / Our new favorite for general / searches. Unlike othersearch / engines,
> Google uses propri- / etary technology to ensure / that the first hits you get for / your search are
> the best.`

also line 2079 `OOGLE [google.com]` (OCR of `GOOGLE [google.com]`) and line 5196
`Searches conducted at Google.com`. An unaffiliated magazine thus confirms, in 2000-07, that Google was
**operating at google.com as a general search engine and was already distinguished from other engines
by ranking quality** — the first third-party print characterisation of the *product* in this dossier.

**First ads:** the same issue lists `GOTO.COM [goto.com]` (line 2927) and reports
`I went to GOTO.coM to compare online / prices` (line 8018) — contemporaneous evidence that paid
inclusion via GoTo was the visible commercial channel of the period. That is a competitor's channel,
not Google's revenue: `AdWords` returned 0 hits in held bytes, so the S-1's AdWords account stays
uncorroborated by periodicals.

## Verdict on family c

STATUS: WRITTEN

**Family (c) periodicals: UNTRIED → TRIED, PARTIAL / LEAD-ONLY on the founding question.**

Item verdicts: #3 `TIER1_CANDIDATE` (in-window hits in held bytes; the *title* itself is Tier-3 press
under §5, so it corroborates the product, not the origin); #1 and #2 `NULL` (zero hits over 304 KB and
536 KB of confirmed OCR). Two further items `UNANSWERED` (see below).

Effect on tiering, stated narrowly: this pass **closes the "untried" record** for family (c) — the
config hole, not the corpus. It does **not** yield in-window Tier-1 text on the 1998-2003 founding
window, so a third qualifying family *for the founding period* is still not established; the probe's
reading stands: **"T1 from the IPO end, thin at the founding end."** Re-tiering belongs to the probe
owner with all five families in view. New and defensible from this pass: a July-2000 third-party print
characterisation of the product, and the fact that the founders' names appear in **no** periodical byte
this project holds.

## queries.json additions

STATUS: WRITTEN

**9 tasks appended under `"company": "alphabet"`, taking `tools/queries.json` from 49 tasks to 58.**
Append-only was honoured literally: the new objects were **spliced textually** before the closing
bracket of the `tasks` array (`out = raw[:j] + new + raw[j:]`), so no existing task could be touched,
reordered or re-serialised. Post-write checks: the 49 non-alphabet tasks are unchanged and in original
order, the 9 new ones are contiguous at the tail, top-level key order is identical, the file re-parses.
`company: "alphabet"` is the slug matching `company_005_alphabet`; the probe's `--company google`
selector returns nothing by design and is not a second company.

Field names and task shape copied from the existing Walmart and Apple entries read before writing
(`company`, `source_family`, `kind`, `query_label`, optional `_note`, optional `window`, `params`; the
7-key `_note`+`window` form matches 10 pre-existing tasks). Labels:
`IA Yahoo Internet Life / Network World tech-press sweep 1998-2004` ·
`IA magazine_rack/computermagazines annotation sweep for 'google' 1998-2004` ·
`IA founder-name query 1998-2000 (kept as a canary -- returned 0, DO NOT read as absence)` ·
`CA-CANARY titles Google search company` · `CA 'Google' search engine 1998-2004` ·
`HT 'Google' 'Larry Page' 1998-2004` · `GB Google search engine launch 1998-2004` ·
`CP alphabet/google annual + shareholder print 1998-2006` ·
`CP google corporate print by creator 1998-2006`.

All **five families are now represented for Alphabet**, which is the point: an unqueried family reads
as a null. Notes record what is verified versus merely queued (the HathiTrust and Google Books shapes
were **not exercised** this pass; the CA page search is UNANSWERED by construction), and the two tool
defects are written inside the first task's `_note` so the nightly harvester cannot silently
manufacture false nulls on spaced filenames.

## Companies with no task

STATUS: WRITTEN

**47 of the 50 companies in `founders_playbook/00_universe/fortune_top_50_2026.csv` have no task in
`tools/queries.json` today.** Measured, not fixed, as instructed: 50 universe rows; 4 tasks-bearing
company slugs in the file (`walmart`, `apple`, `unitedhealth`, and now `alphabet`); 3 of them matched
universe rows when measured against the pre-append file, so 50 − 3 = 47, and Alphabet is the 48th
company that was uncovered before this pass. Matching normalised the Fortune label to the slug
convention (`Alphabet (Google)` → `alphabet`, `UnitedHealth Group` → `unitedhealth`); the mapping is
name-based, not register-keyed, so a future pass should re-check parenthetical and multi-word forms.

This is the hole the next 40 companies inherit: **47 companies × 5 families = 0 configured queries**,
and any of them probed under §15.2 today would emit the same "UNTRIED for a real reason" finding
Alphabet did. Handing the number back rather than filling it: writing 47 unverified query sets is
exactly the mass-config-edit that has previously taught the fleet a retracted value.

## Nulls vs UNANSWERED

STATUS: WRITTEN

**NULLS — zero over held bytes (2 items, 840,463 B):**
1. `bub_gb_fBsEAAAAMBAJ` Network World 1998-03-30 — 304,352 B held, `google` 0, `overture` 0,
   `go2net` 0, ad-forms 0 → NULL. (Pre-founding date: it cannot corroborate Sept-1998 even in
   principle, but it does answer nothing on the ads question either.)
2. `bub_gb_VA0EAAAAMBAJ` Network World 1999-05-10 — 536,111 B held, `google` 0, `overture` 0, ad-forms 0
   → NULL (`ia_text.py grep` verdict: `NULL -- 523 KB of OCR held, zero hits`).

**UNANSWERED — no bytes, or bytes too thin to mean anything (3 cases, 0 usable KB):**
1. `yahoo-internet-life-magazine-april-2001` — metadata proves a 337,014 B DjVuTXT layer exists; the
   encoded download returned **HTTP 500**. 0 bytes held → UNANSWERED. A server error is not absence.
2. `yahoo-inc.-yhoo-annual-report-1999` (in `magazine_rack`) — a candidate *independent* corporate-print
   item for the 1998-1999 window, but its text layer is a **199-byte stub**, below the tool's own 400 B
   floor → UNANSWERED, deliberately not a null: an image-only scan says nothing about whether Yahoo's
   own 1999 report names Google.
3. `("Larry Page" AND "Sergey Brin") AND mediatype:texts AND YEAR:[1998 TO 2000]` → `numFound=0`, yet
   the same grammar returns 0 for `title:("Red Herring") AND year:1999`, which must match. An
   annotation-scoped zero from this egress is **UNANSWERED**; the query is kept in `queries.json` as a
   canary.

Also **not** counted as evidence: every `text:`/`text__reviews:` hit on this route, including the 8
`magazine_rack` "google" rows (none is tech press) and the 21 `Internet World` rows (Israeli edition,
OCR not fetched).

**Tally: 2 NULL · 3 UNANSWERED · 1 TIER1_CANDIDATE · 10 UNTRIED headings below.**

## Untried

STATUS: WRITTEN

Reported as UNTRIED, never as nulls (§14 rule 6):

1. **The general/magazine half of family (c) reached nothing.** Fortune, BusinessWeek, Red Herring,
   The IndustryStandard, Fast Company, Interactive Week, WIRED issues: **no item retrieved**. Every
   title probe returned 0 rows on annotation-scoped grammar that also returned 0 for queries that must
   match. Their absence here is a route question, not a finding.
2. **Network World issues enumerated but not fetched**: `bub_gb_ohkEAAAAMBAJ`, `bub_gb_tw4EAAAAMBAJ`,
   `bub_gb_lxEEAAAAMBAJ`, `bub_gb_QhkEAAAAMBAJ`.
3. **The other 7 in-window Yahoo Internet Life issues** (2001, 2002) returned by the same verified
   title query. YIL 2000-07 proved the collection holds Google-relevant OCR; the AdWords/first-ads
   question is likeliest to settle in a 2001-2002 issue and did not.
4. **`magazine-internetworld-*` (13 items, 1998-2000)** — an in-window internet-trade monthly; OCR not
   fetched (Hebrew titles lower the prior but do not exclude a Google listing).
5. **HathiTrust and Google Books unexercised this pass** (routes known-live elsewhere from 2026-09-25).
   Tasks queued; no bytes held; therefore zero findings and zero nulls.
6. **Chronicling America**: queued only; the zone is blocked to scripted clients per this repo's own
   PROVEN 2026-09-25 canary.
7. **`sources/ia/cia_1487901_djvu.txt` (16,305 B) already on disk** — never grepped for founding terms.
8. **The 47 companies with no harvester task** — untried by configuration, not by search.
9. **A verified-TLS re-fetch of all three held items** — every byte here is unverified.
10. **Family (e) documentary / auction records** — untouched, as the probe left it.

**Outbound corrections for the tooling owner (files I do not own):** `tools/ia_text.py` needs
`doseq=True` on the `fl[]`/`rows[]` params (else `search`/`mine` are no-ops) and `urllib.parse.quote`
on the text-layer filename (else every spaced filename becomes a false "no text layer"). Until then the
`tools/HARVEST_README.md`-adjacent guidance should state that an `ia_text.py` "UNANSWERED — no text
layer resolved" is **not** evidence of a missing OCR layer: check `archive.org/metadata/<id>` for
`format: DjVuTXT` first. Recorded here rather than edited there — one path, one owner (§14 rule 7).

