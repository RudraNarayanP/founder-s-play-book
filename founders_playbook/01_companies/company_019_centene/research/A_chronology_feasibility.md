# A — Chronology Feasibility: CENTENE CORP (Fortune rank 19, company_019_centene)

STATUS: WRITTEN — Stage-1 probe (agent probe-centene). Registrant resolves cleanly by name-exact:
**CENTENE CORP, CIK 0001071739, ticker CNC**, registrant guard `ok` (slug token `centene` matches the
registrant); `former_names` empty — the CIK-vs-name fallback in `tools/legacy_cik.py` was **not** needed here.

## Verdict (one line)
**T3 register, provisional.** Exactly one of the five corpus families returns in-window Tier-1 text; the other
four are UNTRIED or UNANSWERED, never nulls. Unusually, the one family that answers (a) carries the *whole*
lineage because Centene IPO'd late (2001) and its S-1 self-recites 1984/1993/1997 — but a tier counts
**families**, not richness inside one family, so the numeric rule (§15.2: ≤1 family → T3) caps it at register.

## PROPOSED windows (RD-112 — set by this probe, NOT inherited from a filename or harvester parameter)
`fortune_top_50_2026.csv` has no founding-date column; the intake window `1984-01-01..2002-12-31` is a
*search setting*, and I do not use it as evidence. My proposed stage windows, each graded against its OWN span:

| stage | PROPOSED window | what it is |
|---|---|---|
| 1 — Predecessor operating history | 1984-01-01 .. 1992-12-31 | Medicaid managed-care line operating in Wisconsin |
| 2 — Registrant formation & naming | 1993-01-01 .. 1997-12-31 | organized 1993 (Coordinated Care) → renamed 1997 (Centene) |
| 3 — IPO / first public validation | 2001-10-09 .. 2002-12-31 | S-1 → 424B1 → first 10-K; reincorporation Delaware |

## Per-stage tiers with the families that counted
- **Stage 1 (1984–1992): T3 register (provisional).** Families returning in-window Tier-1 text: **0**. The only
  1984 evidence is a *recital inside the 2001 S-1* ("operating in Wisconsin since 1984"; "First Year of
  Operations 1984") — a later-filing mention, not an in-window primary document. No family answers *in-window*.
- **Stage 2 (1993–1997): T3 register (provisional).** Families returning: **1 — (a) only, as a later-filing
  recital.** EDGAR perimeter floor is 2001-10-09, so there is no 1993/1997 filing for this registrant; the
  origin is established solely by the 2001 S-1's self-recital. Provisional pending families (b)/(c)/(d).
- **Stage 3 (2001-10-09..2002-12-31): T3 register, one family carrying the stage.** Families returning:
  **1 — (a)**, and here (a) is genuinely *in-window* Tier-1 (prospectus, first-year-of-operations table, dated
  membership figures). This is the intake note's point ("filings genuinely reach its origin"), but ≤1 family
  still grades T3 by §15.2. It moves to **T2 core the moment a second family returns in-window Tier-1 text.**

## Five-family verdict (TRIED–ANSWERED / TRIED–UNANSWERED / UNTRIED kept distinct)
| family | state | measurement |
|---|---|---|
| (a) SEC / EDGAR filings | **TRIED–ANSWERED** | `sec_intake index` walked all slices: 3,256 filings enumerated, perimeter floor **2001-10-09**, latest 2026-09-16, **0 UNANSWERED slices**. In-window `auto` (`_RUN.json`) stored **30 docs / 20 accessions**, identity OK. `facts` pass → NULL: **0 of 25,924** companyfacts observations in-window; XBRL coverage runs **2007-12-31..2026-07-24** for this filer — EDGAR's XBRL start, not a fetch failure; early money figures must come from filing text. |
| (b) web archives | **UNTRIED** | No `sources/web_archive/` directory exists; fleet gap #1 — `queries.json` has no web-archive family at all (0 candidate rows carry it). Structurally a four-family run until a CDX task set is added. |
| (c) periodical corpora | **TRIED via local mine = UNANSWERED; live = UNTRIED** | I did NOT run `periodical_harvest.py` (fleet mine lane owns it tonight). Local evidence only — see `## A4 re-read` below: 12 mined items all UNANSWERED (no text layer reached the corpus), 18 untried at `--limit`. **Not a null.** |
| (d) digitised corporate print | **UNTRIED** | `sources/corporate_print/` empty (0 items). CP harvesting deferred to the mine lane; fleet gap #2 notes CP `report_terms` are blind to house organs — but Centene is too recent (1984/1993) to sit in a house-organ era anyway. |
| (e) auction / museum / manuscript | **UNTRIED** | No tool lane; would need a live web call, and my web-call budget is 0. Not attempted → not a null. |

## Carriers for the origin / predecessor question (file + line, all under `sources/sec/`)
One lineage only (§3): the S-1 + its two amendments + the 424B1 are **ONE source**. Every recital below is the
same text restated; the amendment/final-prospectus variants are version differences, not corroborations.
- **`0000950109-01-504218_ds1.txt`** (S-1, filed 2001-10-09, accession 0000950109-01-504218):
  - L367–371 origin recital: *"We were organized in Wisconsin in 1993 as Coordinated Care Corporation, and we
    changed our corporate name to Centene Corporation in 1997. We initially were formed to serve as a holding
    company for a Medicaid managed care line of business that has been operating in Wisconsin since 1984. We
    will reincorporate in Delaware immediately before the closing of this offering."*
  - L30 cover-page state of incorporation = **Delaware** (reincorporation target).
  - L141–142: *"This is an initial public offering of shares of common stock of Centene Corporation"* — the
    2001 S-1 **is** the IPO.
  - L2534–2545 dated "First Year of Operations" table — Wisconsin/Managed Health Services **1984**,
    Indiana/Managed Health Services **1995**, Texas/**Superior HealthPlan 1999**; membership at 2001-09-30 =
    108,126 / 61,840 / 54,901; ownership 100% / 100% / 90%.
  - L820: Humana contract-rights acquisition (Feb 2001) "accounted for 88% of the increase in our net premium
    revenues"; L1988–1991: bought rights to Humana Medicaid contracts (Texas + Wisconsin) for $1.2M, adding the
    Austin and San Antonio markets; L2324–2326: Texas acquisition added **30,000 new members**.
- **Same lineage, restated** (do NOT count as second corroboration):
  `0000940180-01-500572_ds1a.txt` L446–449; `0000950109-01-505224_ds1a.txt` L380–383;
  `0000950131-01-504490_d424b1.txt` L260–263 (424B1, filed 2001-12-13).

## A4 re-read (quoted per instruction; must not be re-run tonight)
File `research/A4_harvest_mine.md`, **mtime 2026-10-06T11:52:06Z** (3,162 bytes), re-read immediately before
quoting. Verbatim state: *"31 candidate rows in the harvest index; 12 items mined; 18 left untried at the
--limit."* Match classes: `TIER1_CANDIDATE_TEXT` 0, `VARIANT_TERM_HIT` 0, `BARE_WORD_MATCH` 0, `NULL` 0,
`UNANSWERED` 12. Entity vocabulary this pass applied: *"name phrases: none; other quoted terms … none."*
→ Family (c) local-mine result is **UNANSWERED (no text reached the corpus), not a null**; the 18 untried rows
are **UNTRIED**. The 12 scanned identifiers all show scan/title dates 2005–2009 marked `outside?` (scan-date is
often the digitisation year, not an out-of-scope ruling).

## Origin finding vs the two traps (dispatch brief)
- **1984 founding vs the registrant:** the S-1 prints **1984 = a Medicaid managed-care *line of business*
  operating in Wisconsin** (Managed Health Services, First Year of Operations 1984) — an operating-history claim.
  The **registrant's legal origin is 1993 (organized in Wisconsin as Coordinated Care Corporation)**, renamed
  **Centene 1997**, reincorporated Delaware, IPO **2001**. I quote the S-1, not a later 10-K restatement.
- **"1996 Texas IPO":** **not supported by this registrant's shelf.** `sec_intake` measured **0 filings before
  2001-10-09** on CIK 1071739 and no 1996 row; the 2001 S-1 is itself the IPO (L141). The only in-window "1996"
  in the S-1 is **HIPAA, the Health Insurance Portability and Accountability Act of 1996** (L634) — an OCR-style
  decoy, not an offering. **Texas** enters as **Superior HealthPlan, First Year of Operations 1999**, with
  Medicaid contracts **purchased from Humana** (Austin/San Antonio, +30,000 members, 2001) — an
  acquired-operating-history claim about a different legal person, exactly the "founding claim and
  acquired-history claim can both be true" trap.

## ## Untried
- Family (b) web archives — no CDX tooling/queries (fleet gap #1); centene.com / coordinatedcare.com never probed.
- Family (c) LIVE periodical queries — `periodical_harvest.py --facet-free` not run (mine lane); local mine only,
  and it ran with **entity vocabulary = none**.
- Family (d) corporate print — `harvest_mine`/CP not run by me; shelf empty.
- Family (e) auction/museum/manuscript — no lane, 0 web calls permitted.
- 10 in-window filings were **NOT-ENUMERATED** (`sources/sec/_UNANSWERED.csv`: max-docs 30 reached) — their
  documents exist but are unknown to this run.

## FETCH REQUESTs (named remedy; claims tied to these stay UNANSWERED)
- **FR-1 (family b):** CDX snapshot set for `centene.com` + `coordinatedcare.com` over 1996-01-01..2002-12-31.
  Remedy: add a `web_archive` task set to `queries.json`, then a CDX harvest. Needed before any T1/T2 tier.
- **FR-2 (family c):** re-harvest `periodical_harvest.py --company centene --facet-free` once the mine lane
  adds name phrases + predecessors `Coordinated Care Corporation`, `Managed Health Services`,
  `Superior HealthPlan` (A4 ran with vocabulary = none, so 12 UNANSWERED proves nothing about absence).
- **FR-3 (family a completeness):** re-run in-window `sec_intake auto … --max-docs 60` to enumerate the 10
  NOT-ENUMERATED filings and confirm none is a pre-2001/1996 registration for this CIK.
- **FR-4 (family a, renewal-vs-award check):** earliest annual report **10-K405 accession 0000950134-02-002985
  (filed 2002-03-29)** — beyond this run's max-docs; needed for a post-IPO state-contract/membership figure.

## What I refused to claim (and why)
- Refused to assert a **1996 founding or IPO** — no shelf support; the only 1996 is HIPAA (decoy).
- Refused to read **"since 1984"** as the registrant's incorporation date — it is a business operating-history
  recital; registrant organized **1993**.
- Refused to label families (c)/(d)/(e) as **nulls** — they are UNTRIED/UNANSWERED, never "no document exists".
- Refused to treat the **XBRL facts NULL** as "no figures" — it is EDGAR's ~2007 XBRL floor for this filer.
- Refused to grade **T1/T2 on richness within one family** — §15.2 counts distinct families returning.
- Refused to name a **founder**: the S-1 identifies **no founder**; Michael F. Neidorff is President/CEO/
  Treasurer/Director (L1289, L3030) and Brian G. Spanel is SVP/CIO since Dec 1996 (L3097) — roles, not
  founders (§13; do not invent register rows).

## Route most likely to change the verdict
**Family (b) web-archive CDX (FR-1).** A 1996–1998 snapshot or a trade-press hit naming Coordinated Care /
Centene would open a genuine second, in-window Tier-1 family for Stage 2 — the single cheapest path off the
"filings-only, T3 register" floor, since filings here are one self-reciting lineage.
