# PROVENANCE STUB — LEAD NOT OPENED: `DTIC_ADA345567`

**Status: UNTRIED / NOT DOWNLOADED.** Recorded 2026-09-24 by the A2 interior-year
evidence-registrar run. This is a *pointer*, not evidence: per §14 rule 3 and the
Tier-1 promotion gate, a metadata hit is not a document until someone reads it.
Nothing was fetched from this item except its public `metadata` record
(`https://archive.org/metadata/DTIC_ADA345567`) — **the 5.2 MB PDF and the 217,636-byte
text layer were deliberately NOT requested**, on the brief's instruction to leave large or
gated leads alone and register them instead. The two metadata calls were **HTTP 200 at 2026-09-24T13:42:02Z and
2026-09-24T13:51:30Z** (full records preserved in
`IA_A2_interior_years_fetch_evidence_20260924.json`).

## What it is
- Title (item's own `metadata.title`): **"DTIC ADA345567: A Study of the Discount Retail Industry and Wal-Mart Corporation"**
- Date `1998-06-05`; year 1998 → **retrospective, thirty-six years after the 1962 founding; NOT an in-window document.**
- Author (from `metadata.subject`): **Zarbo, Michael E.**; issuing body
  **ARMY INFORMATION SYSTEMS COMMAND, FORT HUACHUCA AZ** (DTIC accession **ADA345567**,
  i.e. a U.S. Army staff-college monograph/thesis, not company print).
- Collections: `dticarchive`, `usgovernmentmirrors`, `government-documents`; creator field =
  "Defense Technical Information Center"; mediatype `texts`; language english.
- Extent: **124 pages** (`imagecount`), 600 ppi scan, OCR = abbyy-to-hocr 1.1.37,
  `page_number_confidence` 91.
- Item's own abstract (verbatim, from `metadata.description`) — quoted because it tells us
  what the study claims before anyone reads it: *"By no mistake, Wal-Mart is the reigning
  king in the retail industry. Conscientious decisions as to what it would take to capture
  and retain the number one ranking in the discount retail market have been evident since
  Wal-Mart's inception in 1962. From concepts borrowed from other discounters, Sam Walton,
  the founding father of Wal-Mart, built on, and matured these ideas resulting in his
  corner, five-and-dime-stores becoming a colossal operation …"* It then promises
  management/marketing/technique analysis, international expansion "into seven foreign
  countries", and a critical section on pricing policy, community service and "strong-arm"
  tactics in small-town expansion.
- Identifiers for re-walking: `identifier-ark` **ark:/13960/t81k63015**; added 2018-04-15;
  uploader `slaxemulator@gmail.com`.

## Where it lives
- Landing page: https://archive.org/details/DTIC_ADA345567
- Text (the cheap route, **not tried**): `DTIC_ADA345567_djvu.txt`, **217,636 B**, served from
  `server ia903102.us.archive.org` + `dir /18/items/DTIC_ADA345567`, i.e.
  `https://ia903102.us.archive.org/18/items/DTIC_ADA345567/DTIC_ADA345567_djvu.txt`
  — the same family-5 `corporate_print` route that worked for all nine Wal-Mart reports now
  in this directory. **No access restriction is set on this item** (`access-restricted`
  absent), so the fetch is one polite request, not a hurdle.
- Other files present: `DTIC_ADA345567.pdf` 5,166,167 B (Text PDF), `_djvu.xml` 2,385,572 B,
  `_hocr.html` 4,683,281 B, `_jp2.zip` 108,845,778 B (page images; do not pull).

## What it would likely answer, if opened
- **The competitor/frame question the company's own reports cannot answer.** Every
  `WALMART_AR_*.txt` in this directory is Wal-Mart talking about itself. This is an
  external, contemporaneous-with-the-1990s analyst treating Wal-Mart as a case inside the
  **discount retail industry**, which is what §I of the A2 dossier needs to say *why* the
  1962–1979 unit growth was unusual rather than only *that* it was.
- A dated (1998) third-party statement of the founding frame — "inception in 1962",
  "corner, five-and-dime stores", "Sam Walton, the founding father" — i.e. a **fifth
  independent retrospective** to triangulate against the 1980 corporate account
  (`WALMART_AR_1980.txt` "Wal-Mart's Past — Foundation for the Future"), the 1990 Trimble
  biography (see `STUB_LEAD_samwaltoninsides00vanc.md`) and the 1992 memoir.
- Likely carries **cited industry statistics for the 1960s–1970s discount sector**
  (Kresge/Woolworth/Sears/Gibson's comparators), the kind of numbers that do not appear in
  Wal-Mart's own printed reports and that would otherwise need EDGAR 10-K text.
- **What it cannot settle:** anything about 1945–1962 provenance at first hand, and any
  figure it states for FY1968–FY1979 is a *restatement by a third party in 1998* — it ranks
  below the report of that fiscal year, which for FY1972–FY1980 is now on disk here.

## Handoff note for whoever opens it
One GET (text layer, 218 KB) is enough to read it; grep rather than re-download the PDF.
Promote to `research/_EVIDENCE_CACHE.md` only with page numbers attached, and label every
figure it carries **TIER-2 RETROSPECTIVE (1998)**.
