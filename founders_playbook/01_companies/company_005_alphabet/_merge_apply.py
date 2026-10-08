#!/usr/bin/env python3
"""Alphabet Stage-1 merge -- register apply pass.

Headers are read as RAW BYTES from company_001_amazon/<name>.csv and written back verbatim as line 1.
Every emitted row is applied: 0 refused. On a duplicate the later/aliased emission is FOLDED into the
kept row with a printed MERGE[...] marker; nothing is deleted to fit a column count.
Dossier-local source keys are re-pointed to the globally minted ids (S4332-S4352, tools/id_mint.py),
and the retired local keys stay printed as aliases in the kept sources row's notes.
"""
import csv, io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
AMAZON = os.path.join(REPO, "founders_playbook", "01_companies", "company_001_amazon")
REGISTERS = ["sources.csv", "quantitative.csv", "timeline.csv", "decisions.csv", "validation.csv",
             "failures.csv", "channels.csv", "conflicts.csv", "data_gaps.csv"]
FENCE = re.compile(r"```([a-zA-Z]*)\n(.*?)```", re.S)
LOCAL_SRC = re.compile(r"\bP[12]SRC\d{2}\b")
ROWTAG = re.compile(r"\b(P[12](?:VAL|FAI)\d{2})\b")

# ---- global ids, minted by tools/id_mint.py --claim (range recorded in 00_universe/_ID_BLOCKS.tsv)
IDMAP = {  # dossier-local source key -> global id
    "P1SRC01": "S4332", "P1SRC02": "S4333", "P1SRC03": "S4334", "P1SRC04": "S4335",
    "P1SRC05": "S4336", "P1SRC06": "S4337", "P1SRC07": "S4338", "P1SRC08": "S4339",
    "P1SRC09": "S4340", "P1SRC10": "S4341", "P1SRC11": "S4342",
    "P2SRC01": "S4343", "P2SRC02": "S4335", "P2SRC03": "S4344", "P2SRC04": "S4345",
    "P2SRC05": "S4346", "P2SRC06": "S4347", "P2SRC07": "S4348", "P2SRC08": "S4349",
    "P2SRC09": "S4350", "P2SRC10": "S4351", "P2SRC11": "S4352",
}
# ---- hand-adjudicated collision groups: kept <- absorbed (all are cross-part same-record pairs)
FOLDS = {
    "sources.csv":     [("P1SRC04", "s1_p2.md", "P2SRC02")],
    "timeline.csv":    [("P1TML16", "s1_p2.md", "P2TML13")],
    "channels.csv":    [("P1CHN02", "s1_p2.md", "P2CHN01"),
                        ("P1CHN03", "s1_p2.md", "P2CHN02"),
                        ("P1CHN04", "s1_p2.md", "P2CHN05")],
    "data_gaps.csv":   [("P1GAP01", "s1_p2.md", "P2GAP01"),
                        ("P1GAP04", "s1_p2.md", "P2GAP03"),
                        ("P1GAP05", "s1_p2.md", "P2GAP02"),
                        ("P1GAP09", "s1_p2.md", "P2GAP12")],
    "validation.csv":  [("P2VAL04", "s1_p1.md", "P1VAL06")],
    "failures.csv":    [("P2FAI03", "s1_p1.md", "P1FAI02")],
}
ROWKEY_COL = {"sources.csv": "source_id", "conflicts.csv": "conflict_id"}
# rows carrying each correction id (matched on the dossier-local row key)
CORTAGS = {
    "COR-01": ["P1TML01", "P2TML08"],
    "COR-02": ["P1SRC04", "P2SRC01", "P1SRC05", "P1CNF01", "P1GAP06", "P2SRC05"],
    "COR-03": ["U.017", "P2QTN04", "P2QTN05", "P2QTN08", "P2QTN09", "P2QTN10", "P2QTN11",
               "P2QTN13", "P2QTN14", "P2QTN15"],
    "COR-04": ["U.024", "P2QTN17", "P1GAP05"],
    "COR-05": ["U.021", "P2FAI03", "P2QTN21"],
    "COR-07": ["P1SRC01", "P1SRC02", "P1SRC03", "P1SRC04", "P1SRC05", "P1SRC06", "P1SRC07",
               "P1SRC08", "P1SRC09", "P1SRC10", "P1SRC11", "P2SRC01", "P2SRC03", "P2SRC04",
               "P2SRC05", "P2SRC06", "P2SRC07", "P2SRC08", "P2SRC09", "P2SRC10", "P2SRC11"],
    "COR-08": ["P1SRC07", "P1SRC08"],
}
NOTES_COL = {"sources.csv": "notes", "quantitative.csv": "notes", "timeline.csv": "notes",
             "decisions.csv": "claim_ref", "validation.csv": "notes", "failures.csv": "notes",
             "channels.csv": "notes", "conflicts.csv": "residual_uncertainty",
             "data_gaps.csv": "follow_up_task"}


ROWTAGPAT = {"sources.csv": r"\bP[12]SRC\d{2}\b", "quantitative.csv": r"\bP[12]QTN\d{2}\b",
             "timeline.csv": r"\bP[12]TML\d{2}\b", "channels.csv": r"\bP[12]CHN\d{2}\b",
             "data_gaps.csv": r"\bP[12]GAP\d{2}\b", "validation.csv": r"\bP[12](VAL|FAI)\d{2}\b",
             "failures.csv": r"\bP[12](VAL|FAI)\d{2}\b", "conflicts.csv": None,
             "decisions.csv": None}
TAILCOL = {"sources.csv": "notes", "quantitative.csv": "notes", "timeline.csv": "notes",
           "decisions.csv": "claim_ref", "validation.csv": "notes", "failures.csv": "notes",
           "channels.csv": "notes", "conflicts.csv": "residual_uncertainty",
           "data_gaps.csv": "follow_up_task"}


def raw_header(name):
    with open(os.path.join(AMAZON, name), "rb") as f:
        return f.readline().rstrip(b"\r\n")


def row_tag(reg, cols, row):
    """the dossier-local key addressing this row: the parts print it as the FIRST characters of the
    notes cell (gap rows: of the gap cell). A tag found later in the row is a forward reference."""
    pat = ROWTAGPAT.get(reg)
    if pat:
        for cc in ("notes", "gap"):
            if cc in cols:
                v = row[cols.index(cc)] if cols.index(cc) < len(row) else ""
                m = re.match(r"\s*(" + pat[1:] + r")", v)
                if m:
                    return m.group(1)
    if reg == "sources.csv":
        return row[0].strip()
    if reg == "conflicts.csv":
        return row[cols.index("conflict_id")].strip()
    if pat:
        m = re.search(pat, " ".join(row))
        return m.group(0) if m else None
    return None


def _row_tag_old(reg, cols, row):
    """the dossier-local key that addresses this row"""
    if reg == "sources.csv":
        return row[0].strip()
    if reg == "conflicts.csv":
        return row[cols.index("conflict_id")].strip()
    pat = ROWTAGPAT.get(reg)
    if not pat:
        return None
    m = re.search(pat, " ".join(row))
    return m.group(0) if m else None


def load():
    em = {r: [] for r in REGISTERS}
    split = []
    for part in ("s1_p1.md", "s1_p2.md"):
        t = io.open(os.path.join(HERE, "_parts", part), encoding="utf-8").read()
        for m in FENCE.finditer(t):
            if m.group(1).lower() != "csv":
                continue
            heading = [x for x in re.finditer(r"^#{2,4}\s+(.*?)$", t[:m.start()], re.M)][-1].group(1)
            named = [r for r in REGISTERS if ("%s.csv" % r[:-4]) in heading]
            rows = list(csv.reader(io.StringIO(m.group(2).strip())))
            cols = [c.strip() for c in rows[0]]
            if len(named) == 1:
                for r in rows[1:]:
                    em[named[0]].append((part, cols, r, row_tag(named[0], cols, r)))
            elif set(named) == {"validation.csv", "failures.csv"}:
                for r in rows[1:]:
                    k = row_tag("validation.csv", cols, r)
                    m = re.match(r"^\s*(P[12](?:VAL|FAI)\d{2})", r[cols.index("notes")] if "notes" in cols else "")
                    if not m:
                        raise SystemExit("shared-block row with no leading P1VAL/P1FAI tag: %s" % r[:2])
                    tag = m.group(1)
                    reg = "failures.csv" if "FAI" in tag else "validation.csv"
                    if k and k != tag:
                        print("   tag-correction: leading notes tag %s (row elsewhere cites %s)" % (tag, k))
                    split.append((part, tag, reg, r[2]))
                    em[reg].append((part, cols, r, tag))
            else:
                raise SystemExit("UNATTRIBUTED BLOCK %s %s" % (part, heading[:60]))
    return em, split


def words(s):
    return {w.lower().strip(".,;:\"'()[]") for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-\.]*", s)}


IDCOLS = ("source_id", "conflict_id")
DATE_COLS = ("date", "date_or_range", "event_date", "publication_date", "access_date",
             "source_date", "date_tested")
SENTINELS = ("unknown", "n/a", "none", "not dated", "see notes", "untried", "not retrieved",
             "in-window", "continuous", "undated", "no dated")
REPAIRS = []


def fold(kept, absorbed, cols, reg, keptkey, apart, akey):
    """union the distinct wording of the absorbed emission into the kept row.
    Prose columns get an inline printed marker; id columns union as a token list so the key
    column stays parseable, and the union is named in the kept row's notes tail."""
    marks, idun = [], []
    for i, c in enumerate(cols):
        if c in ("stage", "company"):
            continue
        kv, av = kept[i], absorbed[i]
        if not av.strip() or words(av) <= words(kv):
            continue
        if c in IDCOLS:
            extra = [t for t in re.findall(r"(?:P[0-9]SRC[0-9]{2}|U[.][0-9]{3})", av)
                       if t not in kv]
            if extra:
                kept[i] = (kv.rstrip(".;") + " and " + " and ".join(dict.fromkeys(extra))).strip()
                idun.append("%s: %s" % (c, " and ".join(extra)))
            continue
        marker = "MERGE[%s <- %s %s, %s: %s]" % (keptkey, apart, akey, c, av)
        kept[i] = (kv.rstrip() + ". " + marker) if kv.strip() else marker
        marks.append(c)
    tail = ("MERGE[%s <- %s %s FOLDED: one record, nothing dropped; columns unioned: %s]" %
            (keptkey, apart, akey, ", ".join(marks + idun) if (marks or idun)
             else "no wording unique to the aliased emission"))
    ti = cols.index(TAILCOL[reg])
    kept[ti] = (kept[ti].rstrip() + " " + tail).strip()
    return marks + idun


def repoint(cell):
    """local carrier keys -> globally minted ids, but NEVER inside a printed MERGE[...] marker:
    the marker is the record of the retired key and must keep showing it."""
    spans = [(m.start(), m.end()) for m in re.finditer(r"MERGE\[[^\]]*\]", cell)]
    out, prev = [], 0
    for a, b in spans:
        out.append(LOCAL_SRC.sub(lambda m: IDMAP.get(m.group(0), m.group(0)), cell[prev:a]))
        out.append(cell[a:b])
        prev = b
    out.append(LOCAL_SRC.sub(lambda m: IDMAP.get(m.group(0), m.group(0)), cell[prev:]))
    return "".join(out)


def date_fix(reg, cols, row, key):
    for c in DATE_COLS:
        if c not in cols:
            continue
        i = cols.index(c)
        v = row[i]
        if not v.strip() or re.search(r"\d{4}", v) or any(x in v.lower() for x in SENTINELS):
            continue
        row[i] = "UNKNOWN (%s)" % v.strip()
        REPAIRS.append((reg, key, c, v.strip(), "UNKNOWN (%s)" % v.strip()))
    return row


UNMAPPED = set()
FOLDLOG = []


def main():
    em, split = load()
    print("== shared block attribution (the parts' own P1VAL/P1FAI tags; RD-132 defect) ==")
    for s in split:
        print("   %-10s %-8s -> %-14s (date %s)" % s)
    report = {}
    for reg in REGISTERS:
        rows = em[reg]
        hdrb = raw_header(reg)
        cols = [c.strip() for c in hdrb.decode("utf-8").split(",")]
        if cols != [c.strip() for c in rows[0][1]]:
            print("   NOTE %s: emission header differs in order from Amazon -- re-keying by name" % reg)
        out, dropped = [], set()
        for keptkey, apart, akey in FOLDS.get(reg, []):
            dropped.add((apart, akey))
        for part, ecols, r, key in rows:
            if (part, key) in dropped:
                continue
            row = list(r)
            # re-key emission columns onto Amazon's column order by NAME (never by position)
            mapped = [""] * len(cols)
            for i, c in enumerate(ecols):
                if c in cols and i < len(row):
                    mapped[cols.index(c)] = row[i]
            for keptkey, apart, akey in FOLDS.get(reg, []):
                if key == keptkey:
                    src = [(p, ec, rr, k) for p, ec, rr, k in rows if p == apart and k == akey]
                    if not src:
                        raise SystemExit("fold target missing: %s %s" % (apart, akey))
                    p2, ec2, rr2, k2 = src[0]
                    m2 = [""] * len(cols)
                    for i, c in enumerate(ec2):
                        if c in cols and i < len(rr2):
                            m2[cols.index(c)] = rr2[i]
                    FOLDLOG.append((reg, keptkey, apart, akey,
                                    fold(mapped, m2, cols, reg, keptkey, apart, akey)))
            for i, c in enumerate(cols):
                if mapped[i]:
                    mapped[i] = repoint(mapped[i])
            if reg == "sources.csv":
                toks = [x for x in mapped[0].replace(" and", "").split() if x]
                mapped[0] = " and ".join(dict.fromkeys(toks))
            elif reg != "conflicts.csv":
                ti = cols.index("source_id") if "source_id" in cols else None
                if ti is not None and " and " in mapped[ti]:
                    keep = re.match(r"^([^\[]*)", mapped[ti]).group(1)
                    mapped[ti] = " and ".join(dict.fromkeys(
                        x.strip() for x in keep.split(" and ") if x.strip())) + mapped[ti][len(keep):]
            date_fix(reg, cols, mapped, key)
            if reg == "sources.csv":
                local = IDMAP.get(key, mapped[0])
                aliases = [k for k, v in IDMAP.items() if v == local]
                ni = cols.index("notes")
                mapped[ni] = (mapped[ni].rstrip() + " GLOBAL-ID %s <- %s (dossier-local alias kept so "
                              "prose citing these keys still resolves)." %
                              (local, "+".join(sorted(aliases)))).strip()
            if reg in ("validation.csv", "failures.csv"):
                vi = cols.index("notes")
                mapped[vi] = (mapped[vi].rstrip() + " [COR-06]").strip()
            for cor, keys in CORTAGS.items():
                if key in keys:
                    ni = cols.index(NOTES_COL[reg]) if NOTES_COL[reg] in cols else cols.index("notes")
                    mapped[ni] = (mapped[ni].rstrip() + " [%s]" % cor).strip()
            if len(mapped) != len(cols):
                raise SystemExit("width drift after application in %s row %s" % (reg, key))
            for i, v in enumerate(mapped):
                if cols[i] != "derived_arithmetic" and not v.strip():
                    raise SystemExit("empty cell %s in %s row %s" % (cols[i], reg, key))
            out.append(mapped)
        for k, n in sorted(UNMAPPED): raise SystemExit("local carrier key with no global id: %s x%d"%(k,n))
        with open(os.path.join(HERE, reg), "wb") as f:
            f.write(hdrb + b"\n")
            buf = io.StringIO()
            w = csv.writer(buf, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
            for r in out:
                w.writerow(r)
            f.write(buf.getvalue().encode("utf-8"))
        report[reg] = {"requested": len(rows), "applied": len(out), "folded": len(FOLDS.get(reg, [])),
                       "refused": 0, "groups": len(FOLDS.get(reg, []))}
        print("%-18s requested %3d -> kept %3d (folded %d, refused 0)" %
              (reg, len(rows), len(out), len(FOLDS.get(reg, []))))
    tot_r = sum(v["requested"] for v in report.values())
    tot_k = sum(v["applied"] for v in report.values())
    print("TOTAL requested %d -> kept %d, folded %d, refused 0" % (tot_r, tot_k, tot_r - tot_k))
    print("\n== fold log: kept <- absorbed, columns unioned ==")
    for f in FOLDLOG:
        print("   %-16s %-9s <- %s %s   [%s]" % (f[0], f[1], f[2], f[3], ", ".join(f[4])))
    print("\n== §13 date-column vocabulary repairs (value kept, prefixed with the controlled literal) ==")
    for r in REPAIRS:
        print("   %-14s %-9s %-12s %s -> %s" % (r[0], r[1], r[2], r[3][:52], r[4][:52]))
    print("   repairs: %d" % len(REPAIRS))
    json_out = __import__("json").dumps(report, indent=1)
    print(json_out)


main()
