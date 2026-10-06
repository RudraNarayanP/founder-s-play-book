# Stage-1 chronology-feasibility PROBE — GOLDMAN SACHS (company_036_goldman, Fortune rank 36)

Owner: `probe-goldman` · Method: `PROBE_BRIEF_SHARED.md` + `00_METHOD_AND_STYLE.md` §3/§13/§14/§15 + RD-112/124/130/134.
Web calls this pass: **0.** All figures below are measurements from bytes already on disk under `sources/` (commands and outputs at §10). STATUS: WRITTEN

---

## 1. Window proposed and the measured intake state

**Stage-1 window: 1869-01-01 → 1950-12-31 — PROPOSED.** `00_universe/fortune_top_50_2026.csv` carries no
founding-date column, so this window is a proposal, not an inherited fact; both candidate founding years
(1869 and 1882) fall inside it so the window does not silently discard either.

Registrant resolved by the intake: **CIK 0000886982 = "GOLDMAN SACHS GROUP INC"** (tickers GS/GSCE/GS-PA/PC/PD;
former name only the trailing-slash duplicate). Guard `ok` (slug token `goldman` matches registrant).

Measured date perimeter of that CIK's full EDGAR index (RD-134 fixed full-slice walk, **not** capped):
**1998-08-24 → 2026-09-29**, 92,568 rows. Rows with a filingDate in the proposed window (1869-01-01..1950-12-31): **0**.
Rows before 1951: **0**. This is not "the company filed nothing" — it is the **legal-person break** at the 1999
incorporation/IPO: the modern registrant did not exist until it registered. EDGAR's own 1993-94 floor is not even
the binding constraint here; the registrant's creation is.

Two intake passes are recorded (`sources/sec/_RUN.json`):
- **In-window pass (1869→1950): 0 stored** — expected, no CIK.
- **Forward recital pass (window `1950-12-31..2006-12-31`): 29 stored**, 278 attempted, 2 UNANSWERED, 247 skipped,
  0 nameless; identity `29+2+247=278` OK. Floor document = the **S-1 filed 1998-08-24** (registrant's first filing).
  NOTE: the dispatch context asserted "391 accessions in that window"; my count of index rows dated 1998-2006 is
  **2408**, and the tool's own selection stream is 278 attempted. I cannot reproduce 391 and do not publish it — it
  is a tool-internal figure, not a measurement (§ hard-rule 8).

## 2. The founding recital — carriers, one lineage, and role-vs-founder (STATUS: WRITTEN)

The origin reaches the corpus **only** as the registrant's own retrospective sentence, ~130 years after the event.
Verbatim, two distinct carriers of one text:

- `0000950123-99-002156_0000950123-99-002156.txt` (S-1, filed **1999-03-16**), l.4355-4356 —
  *"The Firm is the successor to a commercial paper business founded in 1869 by Marcus Goldman. Since then, we have
  grown our business as a participant and intermediary in securities…"*
- `0000950123-00-001143_0000950123-00-001143.txt` (10-K, filed **2000-02-14**), l.722-723 — the same sentence,
  opening "Goldman Sachs is the successor to…".

The phrase `Marcus Goldman | founded in 1869 | successor to a commercial paper` recurs **44 times across 22 stored
files** — but those 22 are the 1999 IPO line (S-1, every S-1/A, the 424B4), subsidiary S-1s that paste the same
boilerplate, and the FY1999 10-K. **That is ONE self-narrative lineage, not 22 witnesses** (§3, RD-124). The
**1998-08-24 S-1 carries no founding recital at all** — grep for `Marcus`/`1869`/`successor to a commercial paper`
returns nothing in it; its only "successor"/"commercial paper" hits are lease covenants and modern commercial-paper
funding. The founding sentence first appears in the **1999** documents.

**Legal-person break, in the registrant's own words** (l.4360-4369 of the 1999-03-16 S-1): *"In 1989, Group L.P. was
formed… GS Inc. was formed to succeed to the business of Group L.P."* The 1869 commercial-paper business is a
**predecessor**; GS Inc. (Delaware, IPO 1999) is the registrant. Same evidence class as Boeing's "since 1916" and
Ford's Delaware/Michigan split (RD-130/RD-134), with Ford's polarity: the *later* entity is the registrant, so
1869-1950 is a **predecessor window on the registrant's own account**.

**Competing founding year 1882: 0 occurrences** across all 29 stored SEC bytes. The filings settle the *narrative*
on 1869; they are silent on 1882, so the discrepancy is **not resolvable from family (a)** — it needs a
print/manuscript carrier (see §9).

**Role vs founder — Samuel Sachs.** The literal `SAMUEL SACHS` occurs exactly **once** in the whole SEC corpus:
`0000950123-99-003931_0000950123-99-003931.txt` (S-1/A, 1999-04-30) l.19383-19384, as a **stock-certificate picture
label** — `[PICTURE OF MARCUS GOLDMAN] … [AND SAMUEL SACHS]`. It is commemorative artwork, not a founding claim; the
recital names Marcus Goldman alone. A later partner who lends his name to the firm is **not** a founder, and the
document does not say he is. STATUS: WRITTEN

## 3. The 1930s examinations and the antisemitism allegations — as claims about what a document says (STATUS: WRITTEN)

Checked as instructed, i.e. *does any in-scope document assert them?* Measured across the stored SEC set:
- `Pecora | subcommittee on investigation | 1932 | Henry Sachs | Walter Sachs | son-in-law | joined the firm`: **0 occurrences.**
  The only `1934` hits are the statutory string "Securities Exchange Act of **1934**" (a rule citation, an OCR/keyword
  decoy of exactly the class rule-6 warns about — not a claim about Goldman being examined).
- `anti-semit | antisemit`: **0 occurrences.** `discriminat*`: 22 occurrences, every one boilerplate
  ("discrimination"/"discriminatory" in EEO covenants and pricing/tax language) — none about the firm's founding era.

**Verdict:** the registrant's own record says **nothing** about a 1930s Pecora-era examination of Goldman, and nothing
about antisemitism. Those are **real popular claims that carry no document here**. They must not be imported as
settled background; at best they are Tier-2/3 assertions awaiting a periodical, corporate-print, or manuscript
carrier — none of which returned in-scope text this pass. STATUS: WRITTEN

## 4. Five-family verdict (each family explicitly; no untried family reported as a null) (STATUS: WRITTEN)

| Family | State | Measured basis |
|---|---|---|
| (a) SEC / EDGAR | **TRIED–ANSWERED, but out-of-window for origin** | Perimeter 1998-08-24→2026-09-29, 0 rows <1951; founding recital exists but is a 1999/2000 **retrospective**, ONE lineage; 1882 & 1930s & antisemitism all 0. In-window Tier-1 documents = **0**. |
| (b) Web archives | **UNTRIED** | No `sources/web_archive/` dir, no sidecar → genuinely not attempted (0 calls). Not a null. |
| (c) Periodical corpora | **TRIED–UNANSWERED / partial** | 32 candidates, 6 mined (A4): 1 in-window item `flyer_20240620` = **NULL decoy** (a modern "Hyperborean Wisdom" nihilist-terror flyer, metadata date 1933, 0 Goldman content, `entity_hits:0`); 5 items = **UNANSWERED HTTP 503**, and all 5 are out-of-window scan dates (2010/2016). **25 candidates left UNTRIED at `--limit`.** In-window Tier-1 Goldman-naming text = **0**. |
| (d) Digitised corporate print | **UNTRIED** | `sources/corporate_print/` empty (0 bytes), **no sidecar**; the harvest index carries no `corporate_print` task. Prior fleet queries were YEAR-faceted — RD-130 proved a faceted corporate-print zero is a statement about the *parameter*, never a NULL. Facet-free corporate print for goldman was not run. |
| (e) Auction / museum / manuscript | **UNTRIED** | No dir, no query, and **no verified tool reaches it** (Web calls = 0). Route named at §7/§9. |

STATUS: WRITTEN

## 5. Per-stage tiers — measured against each stage's own window (RD-112) (STATUS: WRITTEN)

- **Stage 1 (origin, 1869-01-01→1950-12-31): T3 — register — PROVISIONAL.** Families returning in-window Tier-1 text =
  **0**. The founding is carried only by a retrospective filing lineage that post-dates the window by a century; periodical
  returned a NULL decoy; corporate print, web and manuscript are UNTRIED. §15.2 rule (≤1 family → T3). **Provisional**
  because three of five families were never tried and (c) was only partially tried — this is the RD-112/RD-122 Costco
  boundary case ("family (a) yields in-window *text* but no in-window *document*," here not even text).
- Later stages are outside this probe, but for planning: a stage window that **includes 1998-08-24→1999** (GS Inc.'s own
  incorporation/IPO) flips family (a) to in-window Tier-1 — the S-1/424B/10-K narrate that restructuring contemporaneously.
  That is a scaling stage, **not** the origin, and the planning tier for **Stage 1 stays the minimum = T3 (~3-4 agent runs,
  not 15-20).**

## 6. Untried (must be re-approached, not re-declared empty) (STATUS: WRITTEN)

1. **Family (d) corporate print, facet-free** — the single most tier-relevant UNTRIED route (see §9).
2. **Family (c) periodical: the 25 harvest candidates not mined at `--limit`,** and the 5 HTTP-503 items once IA/Hathi egress recovers.
3. **Family (b) web archives** — 0 attempted; a Wayback/CDX pass has never been opened for this company.
4. **Family (e) manuscript / auction / archive finding aid** — 0 attempted, no tool.
5. **SEC tail** — `_UNANSWERED.csv` rank 30 (SC 13G/A `0000769993-00-000432`, 404 on three path forms) and the note that
   **362 in-window recital filings were never listed** because `--max-docs 30` was reached. STATUS: WRITTEN

## 7. FETCH REQUESTs (script-owned; declining is correct behaviour, not a gap) (STATUS: WRITTEN)

```
FETCH REQUEST: periodical_harvest --company company_036_goldman --facet-free --family corporate_print
  for the Goldman house histories / centennial volumes / bank annual-report runs on Internet Archive + HathiTrust.
  Why: RD-130 showed every prior corporate-print zero here rode a YEAR facet; a facet-free run is the only honest
  way to record this family as answered-vs-null. This is the family most likely to lift Stage 1 off T3.
FETCH REQUEST: harvest_mine --company company_036_goldman --limit 32   (raise the --limit past the 25 untried candidates)
FETCH REQUEST: sec_intake auto "GOLDMAN SACHS GROUP INC" --company-dir company_036_goldman \
  --from 1998-08-24 --to 1999-12-31 --max-docs 300   (to enumerate the 362 not-listed recital filings and re-reach the 404 SC 13G/A)
FETCH REQUEST: an archive finding aid for the Goldman family / Marcus Goldman papers (NYPL, Leo Baeck Institute,
  PA/WI historical societies) — no verified tool reaches family (e); orchestrator judgement whether to route it.
```
STATUS: WRITTEN

## 8. Refused to claim (and why) (STATUS: WRITTEN)

- **1869 as a settled founding date.** Refused. Class **FOUNDER CLAIM / RETROSPECTIVE SOURCE**, confidence **Low** —
  it rests on the registrant's own 1999 sentence, one lineage, ~130 years after the fact, with a competing 1882 the
  record does not address. The *content* (a Goldman-family commercial-paper business founded by Marcus Goldman) is
  what the document asserts, not independent 1869 evidence.
- **Marcus Goldman "the founder" as fact.** Recorded as *what the document says*; the 1869 legal person does not
  survive to the registrant (successor language §2).
- **Corroboration from the 22 files / 44 occurrences.** Refused — one lineage (§3, RD-124).
- **Samuel Sachs as founder.** Refused — a certificate picture, 1 occurrence; role ≠ founder.
- **1930s examination / antisemitism as background facts.** Refused — 0 carriers in scope; they are claims needing a
  print/manuscript document I do not hold.
- **Any of families (b)(d)(e) as a null.** Refused — they are UNTRIED, not empty (RD-134 NR-1 discipline).
- **"391 accessions"** asserted in the brief context. Refused to publish — my count is 2408 rows (1998-2006); not reproduced.
STATUS: WRITTEN

## 9. Route most likely to change the verdict (STATUS: WRITTEN)

**Family (d) digitised corporate print — the firm's own published house/centennial histories and bank annual-report
runs, harvested facet-free (RD-130) — seconded by family (e) an archive finding aid for the Goldman-family / Marcus
Goldman papers.** Neither is IN-WINDOW today, and neither was TRIED. A bank's own printed history is the class of
document that flipped Boeing/Kroger/Walmart tiers (RD-130) and is the *only* route that could supply a Tier-1 document
*dated inside 1869-1950* and adjudicate 1869-vs-1882 — the filings family cannot, by construction. Until it lands,
Stage 1 is **T3 (register), provisional**. STATUS: WRITTEN

## 10. Provenance of the numbers I published (commands → outputs) (STATUS: WRITTEN)

- `submissions_CIK0000886982.csv` header = `filingDate,form,accession,reportDate,primaryDocument,source`; 92,568 rows.
  Earliest `filingDate` = **1998-08-24**, latest = **2026-09-29**; rows dated before 1951 = **0** (`grep -E '^(18|19[0-4]|1950)' | wc -l`).
- `_RUN.json`: window `1950-12-31..2006-12-31`, stored 29, attempted 278, skipped 247, unanswered 2, nameless 0, identity OK; floor `0000950123-98-007892` S-1 1998-08-24.
- `_MANIFEST.csv`: 29 `status:ok` rows; earliest forms S-1 1998-08-24, then S-1/S-1/A 1999, 424B4 1999-05-04, 10-K/DEF 14A 2000-02-14.
- Grep counts over `sources/sec`: `1882` → 0; `Marcus Goldman|founded in 1869|successor to a commercial paper` → 44 across 22 files;
  `Samuel Sachs|Ernst Sachs|Pecora|subcommittee on investigation|anti-semit|antisemit|discriminat` → 23 hits, all `-o`-resolved
  to boilerplate `discrimination`/`discriminatory` plus the single `SAMUEL SACHS` at `0000950123-99-003931` l.19384.
- Periodicals: `flyer_20240620_djvu.txt` 2,096 B, content = "DON'T DESTROY A PART… Hyperborean Wisdom" (no Goldman); its
  `harvest_mine/_index.json` verdict `NULL`, `entity_hits` 0; 5 UNANSWERED (HTTP 503), scan dates 2010/2016; `corporate_print/` empty.
