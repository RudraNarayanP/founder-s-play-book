# NOTES_centene_p1.md

Owner/agent: `s1-centene` (Stage-1 AUTHOR). Paths owned: `_parts/s1_p1.md`, this file. Not a merge, not an
auditor, not a certifier.

## 1. Probe tier verdict — quoted verbatim (FIRST ACTION)

The dispatch note said "my grep for a verdict line found none." **Verified: the dossier DOES issue a tier.**
It is not a "no tier" case, so I do NOT record `PROBE ISSUES NO TIER` (that would be false against the bytes).
From `research/A_chronology_feasibility.md` (probe `probe-centene`):

> ## Verdict (one line)
> **T3 register, provisional.** Exactly one of the five corpus families returns in-window Tier-1 text; the other
> four are UNTRIED or UNANSWERED, never nulls. (§15.2: ≤1 family → T3) caps it at register.

Per-stage (same dossier, §Per-stage tiers): "**Stage 1 (1984–1992): T3 register (provisional).** Families
returning in-window Tier-1 text: **0**." **I therefore write Stage 1 at T3 register (≈8k words/stage).** No
re-tiering by me; if a later regrade dossier lifts the tier it will supersede this part, and I say so in §S.

## 2. Finding against the probe — family (b) is no longer UNTRIED

The probe wrote family (b) web archives as **UNTRIED** ("No `sources/web_archive/` directory exists"). That was
true at the probe's mtime (`2026-10-06T11:52Z`). A CDX run landed **after** it: `sources/web_archive/_RUN.json`
mtime `2026-10-06T12:35Z`, `attempted 2 / ANSWERED 2 / NULL 0`. So at authoring time family (b) is
**TRIED–ANSWERED**, and this part must report it with its perimeter (I do, in §A/§T/§U and the registers).

Perimeter, honestly (never turned into an archive null): the CDX query window was `1996-01-01..2002-12-31`;
`centene.com` enumerated **159 captures**, `coordinatedcare.com` **500**, but only **6 stored per domain** and
the **earliest stored capture is 1999-09-03**. So the **1996–1998 sub-window was enumerated (captures exist)
but NOT resolved to stored bytes** — that is a named gap with a re-fetch remedy, not a null and not a "no web
presence." The 1999 captures DO return in-window Tier-1 text ("For 15 years, CENTENE … Medicaid … in Wisconsin,
Indiana and Illinois").

**Two-family implication (recorded, not acted on):** with filings (a) **and** now web archives (b) both returning
in-window Tier-1 text for the 1993–2002 part of the Stage-1 span, §15.2 would grade that window T2 core. The
probe graded T3 because it scored the 1984–1992 opening beat (0 families) and had (b) UNTRIED. **I write T3 as
issued** and flag the regrade candidate in §S/§U; upgrading is a regrade dossier's call, not an author's.

## 3. Registrant resolution (by CIK, as instructed)

`legacy_cik.py detail 0001071739` → `CENTENE CORP`, tickers `['CNC']`, **former_names `[]`**, guard `ok`. The
1993 "Coordinated Care Corporation" and the 1997 "Centene Corporation" are this one CIK; the `legacy_cik`
name-vs-CIK fallback was NOT needed. `search` is UNPROVEN — silence ≠ absence, so the acquired-plan entities
(Managed Health Services WI/IN, Superior HealthPlan TX, and the Humana Medicaid contract-rights sellers) are
**NOT resolved to their own CIKs** by me (route named in §S; UNTRIED, not null).

## 4. The founder / geography trap (dispatch trap 1) — status

`grep` for `Ruckelsberger | Hoan | founder | founded` across the whole held corpus: **zero hits in any filing
byte or web byte.** The only `found`/`founded` strings in the S-1 are directors' bios describing OTHER ventures
("a health plan that he co-founded" = Dr. Drozda's earlier St. Louis plan; "Merganser Corporation … he founded";
"a venture capital firm he co-founded" = Mr. Cahill). The registrant's own 2001 S-1 fixes: **organized in
Wisconsin in 1993 as Coordinated Care Corporation; renamed Centene 1997; holding company for a Medicaid line
operating in Wisconsin since 1984; HQ 7711 Carondelet Ave, Saint Louis, Missouri; reincorporate Delaware.** No
natural person is called a founder. The 1999–2001 web corroborates the **Wisconsin/Indiana/Illinois** operating
geography and names **Greylock** as "original investment partner." So the "founded 1984 in Missouri by the
Ruckelsberger family" recital is a **Wikipedia-shaped claim with no contemporaneous carrier in this corpus**: the
1984 marker is a **Wisconsin Medicaid operating line**, the **Missouri** datum is a **1999–2001 HQ address**, and
the **founder identity is UNKNOWN**. Registered as `U.1` (narrative §U.1). Roles (Neidorff CEO "instrumental in
developing our mission"; Johnson director since **1987**; Cox partner of Greylock since 1993) are **not**
founder attributions — refused to mint them as such.

## 5. Acquisition-forest trap (dispatch trap 2)

Centene's growth is an acquisition forest, but the **in-window** acquisitions the byte actually shows are: the
**Feb 2001 purchase of the rights to the Humana Medicaid contracts** (Texas + Wisconsin) for **$1.2 million**,
adding Austin/San Antonio and **30,000 new members**, and **Superior HealthPlan** as the Texas plan (First Year of
Operations **1999**, 90% owned). The dispatch-named later/wider events — **Humana Health Plans 2002, Provider
Group, Windy City, Meridian, WellCare 2020** — are **not evidenced in-window** for this CIK by any held byte and
mostly post-date my Stage-1 closing edge (2001-12-13). The "first market (1984 Wisconsin)" belongs to the
pre-existing operating **line** the registrant was formed (1993) to hold, NOT to a later acquired plan — but the
corporate identity of that 1984 plan is unresolved (§S gap). Recorded with that caution in §D/§L and `U.1`.

## 6. Contract-date ≠ experiment trap (dispatch trap 3)

`grep`/read: the byte gives **"First Year of Operations 1984"** and membership counts **as of 2001-09-30** only;
it shows **no first-enrollee date**. Per the trap, the 1984 Medicaid line is an **operating-history marker**, not
a dated real-world experiment with first enrollees. §D says so explicitly; no first-contract date is claimed as
an experiment.

## 7. What I refused to claim

- Refused a founder name (none in any held byte).
- Refused "founded 1984 in Missouri" as the registrant's origin (1984 = WI operating line; MO = 1999–2001 HQ).
- Refused a 1996 IPO (EDGAR perimeter floor is **2001-10-09**; the 2001 S-1 **is** the IPO; the 424B1 priced it
  2001-12-13). No 1996 row for this CIK.
- Refused to read `coordinatedcare.com` captures as Centene history: they are **"Coordinated Care Solutions /
  CareGuide"** elder-care, a **name collision**, not the registrant's predecessor `Coordinated Care Corporation`
  (registered `U.2`).
- Refused to turn the 1996–1998 web sub-window into a null (enumerated, not fetched — §S gap).
- Refused to grade the XBRL NULL as "no figures" (EDGAR XBRL floor 2007-12-31) or the harvest mine UNANSWERED as
  absence (503/401/404 refusals, vocabulary none).
- Refused to re-tier above T3 on my own authority.

## 8. Five families as I found them (kept distinct)

- (a) SEC/EDGAR filings — **TRIED–ANSWERED** (in-window lineage 2001-10-09..2001-12-13).
- (b) web archives — **TRIED–ANSWERED** (centene.com 1999/2000/2001; coordinatedcare.com = collision). Perimeter
  floor 1999-09-03; 1996–1998 enumerated-but-unresolved. (Probe had this UNTRIED — see §2.)
- (c) periodicals — **TRIED via local mine = UNANSWERED** (12 refusals, text layers not resolved, vocabulary none);
  **18 UNTRIED**; live `periodical_harvest.py` **UNTRIED**. Not a null.
- (d) corporate print — **UNTRIED** (shelf empty).
- (e) auction/museum/manuscript — **UNTRIED** (no tool lane; 0 web calls permitted). Not a null.

## 9. Ids and tools

Global `source_id` minted centrally: **S4554–S4561** (8 ids, `id_mint.py --claim --agent s1-centene`; allocation
sits at S4554+, nowhere near the **S4222–S4229** Microsoft collision range). Claim records `P1-xx`, conflicts
`P1U-0x` (→ merge `U.x`), gaps `P1Gxx` are dossier-local per §13. Tools run: `scaffold claim` (both paths),
`legacy_cik detail`, `id_mint claim`, `gates` (see §10).

## 10. Gate outcome — measured AFTER the last write

Recorded after writing `s1_p1.md`: see the report and `centene_s1_gates_p1.md`. (Do not merge; do not certify.)
