# Government-document evidence for Wal-Mart Stage 1

Promoted from OS temp on 2026-09-25 (method §14.9: fetched bytes belong in `sources/`, not in a temp
directory that a reboot erases). The dossier that retrieved them owns only its own file, so the copy was
made by the orchestrator.

## `SEC_SecuritiesTradedOnExchanges_asof-1970-12-31_IA-securitiestraded1970unit.txt`
* **What:** *Securities Traded on Exchanges Under the Securities Exchange Act of 1934, As of December 31, 1970*
  — the SEC's complete alphabetical issuer register. Front matter: "This publication contains the alphabetical
  list by issuers of all securities admitted to trading on stock exchanges under the Securities Exchange Act of
  1934 except securities exempted under Section 3…"
* **Source:** Internet Archive identifier `securitiestraded1970unit`, HTTP 200 over a **TLS-verified** channel,
  retrieved 2026-09-25 19:50 UTC. `153,481 words` / 941,197 bytes, read whole.
* **Why it matters:** it is the strongest available test of the hypothesis that a government-published,
  third-party, contemporaneous document names Wal-Mart during Stage 1. **It does not.** Occurrence counts in
  this text: `Wal-Mart` **0**, `Wal Mart` **0**, `WALMART` **0**, `Bentonville` **0**, `Rogers` **0** — while the
  same W-block legibly prints WALGREEN COMPANY, WALWORTH COMPANY, WALTHAM INDUSTRIES CORP, WALLACE-MURRAY CORP
  and WALCO NATIONAL CORP. A null next to five neighbours that *are* present is a real negative, not an OCR
  failure.
* **Limit that must travel with the citation:** this volume covers exchange-listed issuers as of 1970-12-31.
  Wal-Mart listed on the NYSE on **1972-08-25** (OTC from October 1970), so its absence here is consistent with
  the company being small and unlisted — the document **cannot** witness 1962–1971, and cannot be cited as
  evidence that the company did not exist or did not grow. It disposes only of the claim that an SEC statistical
  publication naming Wal-Mart exists **for 1970**.
* Re-walk: `A5_sec_statistical_lineage_probe.md` §Verdict; `https://archive.org/download/securitiestraded1970unit`.

## Not promoted, and why
The remaining probe bodies (≈2.3 MB of HathiTrust challenge/error HTML and Google Books atom) stayed in
`$TEMP/a5_sec_lineage_20260926/` with their harvester sidecars. They are **negative artifacts** — 403 pages and
a dropped-filter result — whose value is the request that produced them, which the dossier records line by line.
Keeping them out of the repository is a size decision, not a loss of evidence; re-run the recorded requests to
regenerate them.

## The lead this pass did not spend
The narrow `"Wal-Mart Stores" Bentonville` 1970–79 search re-ranks two document classes most likely to name the
company: **NLRB Court Decisions v.26** and **NLRB Decisions and Orders v.201**, plus the FAA civil aircraft
registers (implausible). An NLRB decision naming Wal-Mart would be a genuinely independent, contemporaneous,
government-published witness — recorded as research debt rather than quietly dropped.
