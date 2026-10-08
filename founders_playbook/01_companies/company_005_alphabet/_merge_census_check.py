#!/usr/bin/env python3
"""My own REQUEST-side census. merge_census.py (RD-131/RD-132) is blind to research/, only counts blocks
with a nearby marker, and can never attribute the validation.csv/failures.csv pair (11 identical column
names). This parses every fenced ```csv block under _parts/ and research/, attributes it by the preceding
`### <registers> - <declared header>` heading, and splits a shared validation/failures block by ROW CONTENT:
channel/validity/evidence-strength signal -> validation; collapse/write-off/abandonment/close-down -> failures.
Headers are enumerated before any field is read by name (RD-124/127/132)."""
import csv, io, os, re, json

BASE = os.path.dirname(os.path.abspath(__file__))
FENCE = re.compile(r"```([a-zA-Z]*)\n(.*?)```", re.S)
HDR = re.compile(r"^###\s+(.*?)`\s*$|^###\s+(.*)$", re.M)
REGNAMES = ("sources", "quantitative", "timeline", "decisions", "validation", "failures",
            "channels", "conflicts", "data_gaps")
FAIL_KW = re.compile(r"\b(fail|collapse|write[- ]?off|abandon|close[- ]?down|closure|loss(es)?\b|reject|"
                     r"refus|declin|withdraw|regress|did not|never|error|defect|negative|absence|null|"
                     r"unsuccess|problem|threat|risk)", re.I)
VALID_KW = re.compile(r"(valid|endorse|evidence[- ]strength|signal|independent|tier|channel|certif|attest|"
                      r"corroborat|prototype|traffic|usage|adoption|placement|citat|mention|award|screen|"
                      r"review|third[- ]party|authorit|peer|press|print(?:ing)? (?:mention|record))", re.I)


def nearest_heading(text, start):
    """last `### ...` heading before the fence, plus the register names it names"""
    pre = text[:start]
    hs = [m for m in re.finditer(r"^#{2,4}\s+.*$", pre, re.M)]
    if not hs:
        return None, []
    h = hs[-1].group(0)
    names = [r for r in REGNAMES if re.search(r"\b%s\.csv\b" % r, h)]
    return h, names


def declared_cols(text, start):
    pre = text[:start]
    m = list(re.finditer(r"`([^`\n]*,[^`\n]*)`", pre))
    if not m:
        return None
    return [c.strip() for c in m[-1].group(1).replace("\n", "").split(",")]


def parse(path):
    t = io.open(path, encoding="utf-8", errors="replace").read()
    out = []
    for m in FENCE.finditer(t):
        if m.group(1).lower() != "csv":
            continue
        body = m.group(2).strip()
        rows = list(csv.reader(io.StringIO(body)))
        if not rows:
            continue
        cols = [c.strip() for c in rows[0]]
        h, names = nearest_heading(t, m.start())
        dec = declared_cols(t, m.start())
        out.append({"file": os.path.basename(path), "path": path, "heading": h, "names": names,
                    "cols": cols, "n_declared": len(dec) if dec else None,
                    "match_declared": (dec == cols) if dec else None,
                    "rows": rows[1:], "body": body})
    return out


def classify(row, cols):
    """content attribution for a validation/failures shared block"""
    idx = {}
    for i, c in enumerate(cols):
        idx[c] = i
    fields = []
    for c in ("signal_or_failure", "what_it_demonstrated", "what_it_did_not_demonstrate", "magnitude", "notes"):
        if c in idx and idx[c] < len(row):
            fields.append(row[idx[c]])
    text = " | ".join(fields)
    fv, vv = bool(FAIL_KW.search(text)), bool(VALID_KW.search(text))
    if fv and not vv:
        return "failures", text
    if vv and not fv:
        return "validation", text
    # tie-break on the leading id token, which the parts key P1VAL/P1FAI, VAL/FAI
    head = (row[0] if row else "") + " " + (row[3] if len(row) > 3 else "")
    if re.search(r"FAI|fail", head, re.I):
        return "failures", text
    return "validation", text


def main():
    files = []
    for sub in ("_parts", "research"):
        d = os.path.join(BASE, sub)
        if os.path.isdir(d):
            files += [os.path.join(d, x) for x in sorted(os.listdir(d)) if x.endswith(".md")]
    totals, log = {}, []
    for f in files:
        for b in parse(f):
            n = len(b["rows"])
            names = b["names"]
            if len(names) == 1:
                targets = [(names[0], b["rows"])]
            elif len(names) > 1 and set(names) == {"validation", "failures"}:
                v, fl = [], []
                for r in b["rows"]:
                    (fl if classify(r, b["cols"])[0] == "failures" else v).append(r)
                targets = [("validation", v), ("failures", fl)]
            else:
                targets = [("UNATTRIBUTED:%s" % (names or b["heading"]), b["rows"])]
            for reg, rows in targets:
                totals[reg] = totals.get(reg, 0) + len(rows)
                log.append("%-22s %-14s rows=%-4s cols=%-3s declared=%-4s hdrmatch=%s" %
                           (b["file"], reg, len(rows), len(b["cols"]), b["n_declared"],
                            b["match_declared"]))
    print("TOTALS", json.dumps(totals, sort_keys=True))
    print("GRAND", sum(totals.values()))
    print("\n".join(log))


main()
