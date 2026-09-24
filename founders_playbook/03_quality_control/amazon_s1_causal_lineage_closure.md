# Amazon Stage 1 — CAUSAL-LINEAGE CLOSURE (Level-3 Register Finisher)

Run **2026-09-24**. Companion to `amazon_s1_numeric_closure_final.md`; owns the **causal** half of the closure that
the previous round finished executing and never wrote down. **0 web requests**; everything here was read off disk.
Line numbers are post-edit (`stage_1.md` grew 13 lines inside U.41 and 3 at the spine paragraph). **No pointer was
deleted, no id renumbered, no file moved or tidied.**

Sources of the findings: `amazon_s1_audit4_audit5_final.md` **PART 1** (five live causal failures, Condition 1 =
FAIL) and **A-B1/A-B2** (AUDIT 5); `MASTER_RESEARCH_LOG.md` RD-035…RD-042.

---

## 1. The five causal sites — verified one by one

| ID | Site as named by AUDIT 4 | Site now | Verdict |
|---|---|---|---|
| **F-1** · High | `stage_1.md` §H l.463 — KNOWABLE asserted "**that card entry frightened buyers**" with no mechanism, alternative or confidence, contradicted by §F.2's "High 1996 / UNKNOWN 1995 incidence" and appendix §B's "Low that consumer distrust produced them" | `stage_1.md` **ll. 476–494**. KNOWABLE now carries only that **two period documents *described*** buyers as reluctant to type a card (registrant's own risk language; the rival's remark dated **1996-09-18**, about a rival), and the measured half sits under "**NOT KNOWABLE:** whether card entry frightened 1995 buyers as a measured condition", with the two contradicting gradings cited, "no 1995 refusal rate, chargeback rate or card-decline figure exists anywhere in the record", Confidence **Low** as a measured condition / **UNKNOWN** as to incidence, and the withdrawal of the old wording recorded at l.493 (RD-036 / audit4_audit5 F-1) | **FIXED — verified by grep: `frightened` survives at 2 lines only, both on the NOT-KNOWABLE/withdrawn side; 0 in KNOWABLE** |
| **F-2** · Medium | §D.1 l.282 third clause stated the company's own 1995-10-04 listing claim as learned fact ("the directory-era route **placed the store** in the period's principal discovery channels") inside a cell repaired one clause earlier to read "The company reported" | `stage_1.md` **l.296** (§D.1 "What was learned"): "the directory-era route **is claimed, by the company's own 1995-10-04 release,** to have placed the store in the period's principal discovery channels — no independent dated listing survives (§F.2 borrowed-credibility row, capped **Medium** on that ground; RD-029 open) — and that it converted there is not knowable inside the boundary", followed by the mechanism, the three alternatives and "none excluded" | **FIXED — the required wording is present verbatim; the §F.2 row it cites is `stage_1.md` l.392** |
| **F-3** · Medium | `validation.csv` r9 `what_it_demonstrated`: "That a two-person firm **could earn** editorial distribution" — an efficacy+merit reading no source carries, contradicting the row's own did-NOT cell, §D.1, §F.2 and `channels.csv` r2–3 | `validation.csv` **r9** (l.9): "That the company **CLAIMED** editorial placement inside its first quarter of trading; that it earned it is not established, no independent dated listing for amazon.com surviving; effect UNKNOWN", with the retired string quoted inside the closure note (AUDIT 4 CONFIRMATION F-3 / **RD-037 CLOSED 2026-09-24**) and "Adjudicated at U.43" | **FIXED** |
| **F-4** · Low | §O.7 ll.770–775 — "The Stage-1 differentiator **the evidence supports** is aggregation and discoverability — **directory placement**, … **tiered discounting**": an unmeasured channel inside an evidence-backed list, plus a 1997 discount program read backwards | `stage_1.md` **ll. 800–812**: the list now names only what is evidenced — a licensed catalogue searchable over **~400,000** sourceable titles against a superstore shelf of **~130,000** (basis-labelled 1996–97), **a published telephone number** ((206) 622-2335; toll-free line, orig. l.2179–2180), the **automatic e-mail confirmation/shipment notice**, and the **advertised 10–40% band** "a claim about price and not a measurement of it" — then: "**Directory placement is not among them**: it belongs to the list of channels the store used, not to the list of effects it can claim (effect of each UNKNOWN, §D.1 and §H; → **U.43**)", and "tiered discounting" is restricted to the advertised band with the **March-1997** "Amazon.com 500" barred (→ U.18) | **FIXED** |
| **F-5** · Low | Traceability: ll. 274, 469, 1075 each routed the channel-efficacy question to "**→ U.41**", which is the Associates Program; grep of the 42 blocks confirmed **no** U block adjudicated directory-placement or credibility efficacy at all | **U.43 appended** — `stage_1.md` **ll. 2251–2293**, "**U.43 — Whether directory placement or borrowed press credibility acquired anyone in 1995**", carrying CLAIM A (company's own 1995-10-04 release + filing's Marketing and Promotion section), CLAIM B (no independent dated listing; the NCSA Mosaic August-1995 census of 3,084 entries **does not contain the company**; no amazon.com root capture before 1998-12-12), WHY THEY DIFFER, **EVIDENCE WEIGHT** (split, and the split is the finding — A is Tier 1 *as a claim*, B is the only external census and returns nothing; neither carries an effect measure), **BEST-SUPPORTED INTERPRETATION** ("hold both and spend neither": existence **High**, third-party-observed listing **UNKNOWN**, conversion **UNKNOWN and not knowable inside the boundary**), **RESIDUAL UNCERTAINTY** (the share of ≈2,200 daily December-1995 visits, unrecoverable by construction) and **CONFIDENCE**. No id renumbered; the block says so | **FIXED** — and the three stale pointers it names now read → U.43 at ll. **288, 496, 1152** (§D.1, §H, §R), plus §O.7 l.809 and `conflicts.csv` **r44** |

**Condition 1: 5 of 5 sites closed, 0 outstanding.** What remains **open is the verdict, not the work**: RD-040 reads
"CLOSED as to the five sites and the routing (2026-09-24) … **AUDIT 4 has NOT re-confirmed it — a repair is not a
pass**." That re-confirmation belongs to the Hindsight Auditor, not to this finisher, and is recorded as such.
The one live residue in this family is **RD-038**: `_parts/s1_p2.md` l.78 still mirrors the pre-repair credibility
claim inside a frozen staging part (not in this pass's write scope).

## 2. Same-lineage demotions — the census

AUDIT 5 **A-B1** landed: copies of one 1997 filing family (S-1 original + S-1/A + 424B1, plus the 10-K405
restatement) were being counted as **two** corroborations, against the volume's own header rule and method §3.
Demotion sites, counted by line on the exact markers:

| File | "same lineage as S0801" sites | Line numbers (first/last) |
|---|---|---|
| `stage_1.md` | **4** | ll. 431, 560, 1203, 1280 |
| `conflicts.csv` | **2** | r2 (U.1), r9 (U.8) |
| `stage_1_claim_records.md` | **25** | ll. 51; 380–410 (13 lines); 455–467 (9 lines); 527; 581 |
| **Total** | **31** | — the "31 places" the brief counts |

Wider census, same files, any lineage-demotion wording ("registration lineage", "version evidence, not a second
confirmation", "not corroboration", "same lineage" of another family): **40 lines** — 7 + 3 + 30. The 9 additions
are one row of each register using the long form (`conflicts.csv` **r10 / U.9**, "the SAME registration lineage …
version evidence, not a second confirmation"; `stage_1.md` ll. 242, 583, 889) and, in the claim records, five sites
of the same discipline pointed at other lore: **two demotions of a different family** (ll. **444, 545** —
HistoryLink repeating Stone p.3, "same lineage, not corroboration") and **three** in the "repeated copying is not
corroboration" form (ll. **60, 417, 524**).

What the demotion did **not** do, and was not allowed to: **no confidence moved.** §3 grants High on a primary
document alone, so 22 records re-keyed to `Corroboration: 1 (same lineage as S0801 …)` keep High; **2 records were
left at 2** on stated grounds. RD-041's remaining open items are **outside this company's Stage-1 text** —
`sources.csv` `independence_note` for S0803/S0805, `context_appendices.md` §F, and the Walmart/Apple/UnitedHealth
re-audit — and RD-041 recurs across the other 49 companies.

## 3. Pointer / block reconciliation (item 3)

`stage_1.md` §U carries **43 canonical blocks**, `**U.1` … `**U.43`, no gaps and no duplicates (parse, not eye).
The **six** pre-existing `U.41` strings in the file were adjudicated one at a time against
`_parts/U_CONCORDANCE.md`, which maps **claims_AJ U.41 → canonical U.21** and **claims_AJ U.44 → canonical U.41**:

| Mention (pre-edit line) | What it raises | Disposition |
|---|---|---|
| l.347 §E.2 version table, `Medium-High → U.41` | The **Associates Program**, 1996-07, 4,800+ members at 1996-12-31 | **LIVE POINTER — correct as it stands.** Canonical U.41 *is* the Associates Program slot; it lands. Not retargeted |
| l.497 §H | Directory-placement / channel **efficacy** — the question U.41 "does not address" | **Already retargeted to U.43** by the closure round; the sentence is a deliberate quotation of the id, kept because it explains the re-point. U.43 exists (ll. 2251–2293), so the question is **adjudicated, not orphaned** |
| l.1830 U.21 block, "absorbs claims_AJ's U.41" | A **part-local key** for the in-window-artifact conflict | **Intentional quotation of a superseded local id**, per the concordance; canonical target U.21 exists. The merged claim records' E01–E06 read `Conflicts: U.21` (verified at ll. 212–217); the stale local keys survive only in `_parts/s1_claims_AJ.md` (residual R-6 of the numeric sheet) |
| l.2203 | The block header itself | — |
| l.2229 U.42 block, "the same treatment in U.1–U.41" | The **range** the Fortune precedent licenses | **In-range statement, not a pointer**; already fenced by the file's own spine note (now l.2245) |
| l.2239 U.43 block, "§D.1, §H and §R each routed it to U.41" | History of the misroute | **Intentional quotation**; the three routes it names now read → U.43 (ll. 288, 496, 1152) |

**Added by this pass** (`stage_1.md` ll. 2218–2231): a `POINTER/BLOCK RECONCILIATION` note inside U.41 recording the
above, so a future grep of `U.41` finds the answer next to the mentions rather than re-opening them; and at
l.2316 an append-only spine note on the stale generation instruction ("one row per canonical id **U.1–U.42**" →
read as **U.1–U.43**), because `conflicts.csv` now parses to exactly 43 rows, U.1–U.43, no gaps, no duplicates.

**Final counts: live `U.41` pointers = 1; canonical `U.41` blocks = 1 — they match.** Across the spine:
**43 blocks / 43 conflict rows / 0 unresolvable pointers**, with `U.1–U.43` also cross-checked for out-of-range
targets: the only mention above the spine is `stage_1.md` l.1899's "**Absorbs claims_AJ's U.25 and U.49**", which is
explicitly scoped to the part-local volume and needs no canonical target — **not** a dangling pointer.

## 4. Verdict

**Stage 1's causal layer is internally consistent.** Every causal proposition in the Stage-1 text now carries its
own mechanism, alternative and confidence or says plainly that the mechanism is UNKNOWN; the one channel-efficacy
question that had no home is adjudicated at U.43; the pointers route there and nowhere else; and the
same-registration-lineage double count is demoted at all 31 named sites (40 counting the wider family) without a
single confidence being moved. **What is not claimed:** that AUDIT 4 has re-confirmed the five repairs (RD-040 says
it has not — a repair is not a pass), and that the two `_parts/` mirrors (R-4, R-6) and the RD-id collision (R-7)
are closed; they are open, named, and outside a Stage-1 number.
