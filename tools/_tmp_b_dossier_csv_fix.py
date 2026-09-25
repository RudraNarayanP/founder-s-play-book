import csv, io, re, json

P = "E:/founder's playbook/founders_playbook/01_companies/company_004_apple/research/B_founder_forensics.md"

HDR = {
 "decisions.csv": "company,stage,date,decision,state_before,information_available,unknowns,alternatives,constraints,rationale,expected_result,actual_result,source_id,confidence,claim_ref",
 "timeline.csv": "company,stage,date_or_range,event,actors,location,source_id,evidence_class,confidence,conflict_ref,notes",
 "sources.csv": "source_id,stage,claim_supported,source_title,author_or_publication,source_type,primary_or_secondary,event_date,publication_date,access_date,url,archived_url,tier,evidence_class,confidence,independence_note,relevant_passage,notes",
 "conflicts.csv": "company,stage,conflict_id,section,claim_a,claim_a_source,claim_a_date,claim_b,claim_b_source,claim_b_date,why_they_differ,evidence_weight,best_supported_interpretation,residual_uncertainty,confidence",
}

DEC = [
 {"decision": "Operate as a named multi-person concern rather than as an unregistered hobby partnership (the agreement said to have been executed 1976-04-01)",
  "state_before": "Two people building and delivering boards to whoever came; no printed document names a firm in 1975 or in the first months of 1976",
  "information_available": "That dealer pages and club letters were circulating the name APPLE by April 1976; that a machine existed and its designer was personally transporting it to clubs in another county",
  "unknowns": "Whether a firm was needed for trade credit, for liability, or only for a name to put on a dealer page - no document states the purpose",
  "alternatives": "Remain unincorporated and unnamed; sell boards privately; attach to an existing distributor instead of forming a firm",
  "constraints": "The instrument itself has never been read by this project; the 45/45/10 split, the signatories and the capital clause are auction prose",
  "rationale": "UNKNOWN: no document in this corpus states why a partnership was formed",
  "expected_result": "A firm that could be dealt with by name by retailers and by the trade press",
  "actual_result": "The style Apple Computer Co was in trade print by December 1976. RETROSPECTIVE framing of later outcomes is out of stage.",
  "date": "1976-04", "source_id": "BSS-14", "confidence": "Low (the existence of the decision rests on an unread instrument)", "claim_ref": "B-18; B-31; BC-1"},

 {"decision": "Let retailers advertise the product before the maker advertised anything",
  "state_before": "BYTE's twelve 1976 issues carry zero maker copy; the brand name appears only inside other people's pages",
  "information_available": "East-Coast and Berkeley retailers were already naming the Apple-1 in their own brand lists; a manufacturer's list price existed that no cached file prints",
  "unknowns": "Whether the firm welcomed, tolerated or was unaware of the retailer advertising - nothing in the corpus records an internal decision",
  "alternatives": "Advertise directly; sell only by hand as the designer later described; withhold stock from retailers",
  "constraints": "No documented authorized-dealer relationship of any kind in 1976 (D's L-4); no capital record exists",
  "rationale": "UNKNOWN: no internal document records the choice",
  "expected_result": "Stock moved to buyers without advertising spend",
  "actual_result": "The product was named in New York print by September 1976 and offered by mail order in Berkeley by November 1976, with no founder named in either. RETROSPECTIVE: the maker's own advertising began only in June 1977.",
  "date": "1976-09/1976-11", "source_id": "BSS-01", "confidence": "Medium on the print sequence; UNKNOWN on the decision", "claim_ref": "B-07; B-14; BC-6"},

 {"decision": "Give a magazine editor a hands-on demonstration of an unreleased prototype",
  "state_before": "BYTE's editor had conversed with the firm's named principal at WESCON in September 1976 and had printed one clause about it",
  "information_available": "An editor with a national technical readership was present in Palo Alto that evening",
  "unknowns": "Whether the visit was arranged, opportunistic, or solicited; no document records who proposed it",
  "alternatives": "Withhold the machine until it shipped; demonstrate only to dealers; decline press access",
  "constraints": "The editor was simultaneously a commercial party selling advertising space and buying design work",
  "rationale": "UNKNOWN: no document records who proposed the meeting or why",
  "expected_result": "Print coverage by a technical editor who had handled the machine",
  "actual_result": "The prototype was demonstrated, a program was written on it that evening, and the editor promised next month's article. RETROSPECTIVE: the article appeared in April 1977 and the designer's own piece in May 1977.",
  "date": "1976-11-20", "source_id": "BSS-02", "confidence": "Medium-High that it happened; UNKNOWN as to the decision behind it", "claim_ref": "B-09; B-31; B-32"},

 {"decision": "Incorporate in California",
  "state_before": "An unincorporated concern whose address of record was not yet published; the 1976-04-01 instrument (if executed) was still the only founding paper",
  "information_available": "That a corporation was filed on 1977-01-03; nothing in the corpus states why, or who signed",
  "unknowns": "Motive, signatories and the share structure at incorporation",
  "alternatives": "Continue as a partnership; incorporate in another state; delay until outside money arrived",
  "constraints": "California fictitious-business-name and filing obligations; no printed reason appears in any retrieved document",
  "rationale": "UNKNOWN",
  "expected_result": "A corporation able to issue stock",
  "actual_result": "Apple, incorporated in 1977, was reported as a public company in December 1980 print. Two lineage-free Tier-1 witnesses support the fact; none supports the motive.",
  "date": "1977-01-03", "source_id": "BSS-04", "confidence": "High on the date; UNKNOWN on the decision's reasoning", "claim_ref": "B-26; BC-1"},

 {"decision": "Introduce the Apple II at the first West Coast Computer Faire rather than only through the club circuit",
  "state_before": "A machine in demonstration in November 1976; a magazine article commissioned for May 1977",
  "information_available": "The Faire was billed for April 1977 with 200 commercial and homebrew exhibits and an expected 7,000 to 10,000 attendees; its organisers were the Homebrew newsletter's editor and the editor of Dr Dobb's Journal",
  "unknowns": "Who decided on the Faire debut, and whether the company had a choice of venues",
  "alternatives": "Debut in BYTE alone; debut at a dealer; skip the show",
  "constraints": "UNKNOWN who decided; the Faire's own flyer names no exhibitor",
  "rationale": "UNKNOWN: no internal document states the choice",
  "expected_result": "A public introduction to a several-thousand-person buying audience",
  "actual_result": "Apple was a billed exhibitor in December 1976 print and the introduction was reported afterwards. RETROSPECTIVE framing of the product's later reception is out of stage.",
  "date": "1977-04", "source_id": "BSS-09", "confidence": "High that the debut was planned and billed; UNKNOWN as to who planned it", "claim_ref": "B-33; B-40"},

 {"decision": "Take consumer orders directly by mail, on credit cards, with free shipping and a free carrying case",
  "state_before": "The maker had placed no advertisement of its own; distribution as described by the designer was word of mouth then retail",
  "information_available": "A nine-line price ladder and a working address and telephone; a $50-value case and continental freight could be absorbed; personal cheques needed three weeks to clear",
  "unknowns": "Whether direct mail was a channel choice or a substitute for a dealer network that did not yet exist",
  "alternatives": "Sell only through retailers; refuse cards; require cash instruments only",
  "constraints": "The cash-flow constraint is inferred from the offer terms, not documented; no capital record exists",
  "rationale": "UNKNOWN: no document says who set the terms",
  "expected_result": "Orders and payment arriving by post from anywhere in the continental United States",
  "actual_result": "The company's own first advertising was simultaneously a mail-order catalogue. RETROSPECTIVE: the mechanism is visible only because the advertisement survives.",
  "date": "1977-06", "source_id": "BSS-04", "confidence": "High that the terms were printed; UNKNOWN on the decision", "claim_ref": "B-35; B-36"},
]

SRC = [
 {"source_id": "BSS-05", "claim_supported": "The absence of any officer title for either founder in founding print (B-37)",
  "source_title": "Negative census: president / vice-president / treasurer in Apple context, BYTE 1976-77 and Homebrew 1975-77",
  "author_or_publication": "this pass", "source_type": "corpus census", "primary_or_secondary": "primary (about the corpus)",
  "event_date": "1975-11/1977-12", "publication_date": "2026-09-26", "access_date": "2026-09-26",
  "url": "local corpus", "archived_url": "sources/ia_byte_1976, ia_byte_1977, ia_homebrew (header lines excluded)",
  "tier": "1", "evidence_class": "FACT (documented absence within these files)", "confidence": "High",
  "independence_note": "derived from the same cached files as A2S-01..A2S-13; not an independent witness of the world",
  "relevant_passage": "NO_VERBATIM_PASSAGE_RECORDED",
  "notes": "Zero hits. Scope stated per method: a family-scoped negative, not a disproof."},

 {"source_id": "BSS-06", "claim_supported": "Family-scoped negatives for Atari, Hewlett-Packard and college status (B-06, B-38, BG-1..BG-3)",
  "source_title": "Negative census: atari / hewlett / packard / reed / dropout / college, cached 1975-77 files",
  "author_or_publication": "this pass", "source_type": "corpus census", "primary_or_secondary": "primary (about the corpus)",
  "event_date": "1971/1977-12", "publication_date": "2026-09-26", "access_date": "2026-09-26",
  "url": "local corpus", "archived_url": "sources/ia_byte_1976, ia_byte_1977, ia_homebrew (header lines excluded)",
  "tier": "1", "evidence_class": "FACT (documented absence within these files)", "confidence": "High",
  "independence_note": "confirms and extends A2S-13/A2-61c; the Atari coin-op advertising occurrences are additions by this pass",
  "relevant_passage": "PONG is a trademark of Atari Inc.",
  "notes": "Atari appears in Apple's own advertisements (June and July 1977) and in unrelated third-party ATARI GAME BOARDS advertising; HP only as component, calculator and press matter; no education token at all."},

 {"source_id": "BSS-13", "claim_supported": "First dated carrier found for the Wozniak-at-HP offer/refusal legend (B-43)",
  "source_title": "Woz 'Begged' HP to Make the Apple PC", "author_or_publication": "Business Insider",
  "source_type": "business web article", "primary_or_secondary": "secondary",
  "event_date": "1970s claimed", "publication_date": "2013-02-01", "access_date": "2026-09-26",
  "url": "https://www.businessinsider.com/woz-begged-hp-to-make-the-apple-pc-2013-2",
  "archived_url": "not fetched (budget spent)", "tier": "3",
  "evidence_class": "FOUNDER CLAIM (retrospective memory) - carrier dated, text unread", "confidence": "Low",
  "independence_note": "part of the same retrospective interview cycle as the museum item returned by the same search; not independent of Wozniak's own telling",
  "relevant_passage": "NO_VERBATIM_PASSAGE_RECORDED",
  "notes": "Title and date recovered by search only (W2). Never to be printed as a dated employment fact."},
]

CONST = {"company": "Apple", "stage": "1"}


def render(name, dicts, id_key=None):
    cols = HDR[name].split(",")
    rows = []
    for d in dicts:
        full = dict(CONST)
        full.update(d)
        rows.append([full.get(c, "") for c in cols])
    out = io.StringIO()
    w = csv.writer(out, lineterminator="\n")
    for r in rows:
        w.writerow(r)
    return out.getvalue().rstrip("\n")


s = open(P, encoding="utf-8").read()

# --- rebuild the whole decisions block (intro + header fence + data fence) ---
a = s.index("### `decisions.csv`")
b = s.index("### `timeline.csv`")
old_dec = s[a:b]
intro = old_dec[:old_dec.index("```")]          # the '### ...' line and any prose
dec_block = (intro.rstrip("\n") + "\n\n```\n" + HDR["decisions.csv"] + "\n```\n\n```\n"
             + render("decisions.csv", DEC) + "\n```\n\n")
s = s[:a] + dec_block + s[b:]

# --- rebuild the whole sources block, preserving existing rows and ordering by ID ---
a = s.index("### `sources.csv`")
b = s.index("### `conflicts.csv`")
old_src = s[a:b]
intro = old_src[:old_src.index("```")]
rows_by_id = {}
for r in old_src.split("\n"):
    if r.startswith("BSS-"):
        rows_by_id[next(csv.reader(io.StringIO(r)))[0]] = r
for d in SRC:
    rows_by_id[d["source_id"]] = render("sources.csv", [d])
ordered = [rows_by_id[k] for k in sorted(rows_by_id, key=lambda x: int(x.split("-")[1]))]
src_block = (intro.rstrip("\n") + "\n\n```\n" + HDR["sources.csv"] + "\n```\n\n```\n"
             + "\n".join(ordered) + "\n```\n\n")
s = s[:a] + src_block + s[b:]

open(P, "w", encoding="utf-8").write(s)

bad = 0
for name in HDR:
    a = s.index("### `" + name + "`")
    nxt = re.search(r"\n### `", s[a + 10:])
    blk = s[a:a + 10 + nxt.start()] if nxt else s[a:]
    pre = "BSS-" if name == "sources.csv" else "Apple,1,"
    rows = [l for l in blk.split("\n") if l.startswith(pre)]
    n = len(HDR[name].split(","))
    for r in rows:
        f = next(csv.reader(io.StringIO(r)))
        if len(f) != n:
            bad += 1
            print("BAD", name, len(f), "!=", n, r[:60])
        if any(x.strip() == "" for x in f):
            print("EMPTY CELL", name, r[:50])
    print(f"{name}: {len(rows)} rows x {n} cols")
print("total field-count defects:", bad)
