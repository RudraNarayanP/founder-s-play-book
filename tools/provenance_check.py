#!/usr/bin/env python3
"""Provenance census: does every fetched byte still match the sidecar that describes it?

The corpus carries two sidecar families. `periodical_harvest`/`sec_intake` write `<file>.meta.json` with
`bytes` and `evidence_file`; `cdx_intake` additionally records `sha256`. Neither is ever re-checked after the
write, so a truncation, an outage page stored as a document, or a tool that normalises line endings on the way
to disk stays invisible until an agent quotes the file. This tool re-verifies all of it from disk and reports
the classes separately, because they mean different things:

  OK              size (and hash, if recorded) matches
  SIZE            sidecar says N bytes, file is M         -- the file is not what was fetched
  MISSING         sidecar names an evidence_file that is not on disk
  NO_EVIDENCE     sidecar records no evidence_file at all (listing-only responses)
  HASH            sha256 recorded and differs            -- the bytes changed, however same the size looks
  UNPARSEABLE     the sidecar is not JSON                -- a crashed writer left a half file

Usage:  python tools/provenance_check.py [--root founders_playbook] [--out file.md] [--self-test]
"""
import argparse, glob, hashlib, json, os, re, sys

CLASSES = ("OK", "SIZE", "MISSING", "HASH", "UNPARSEABLE", "NO_EVIDENCE")


def check_pair(meta_path):
    """Classify one sidecar against the bytes on disk."""
    try:
        d = json.load(open(meta_path, encoding="utf-8"))
    except Exception:
        return "UNPARSEABLE", "sidecar is not valid JSON"
    ev = d.get("evidence_file") or ""
    if not ev:
        return "NO_EVIDENCE", "no evidence_file recorded"
    p = os.path.join(os.path.dirname(meta_path), ev)
    if not os.path.isfile(p):
        return "MISSING", "evidence_file %s not on disk" % ev
    size = os.path.getsize(p)
    want = d.get("bytes")
    if isinstance(want, int) and want != size:
        return "SIZE", "sidecar %d B, disk %d B" % (want, size)
    h = d.get("sha256") or (d.get("hashes") or {}).get("sha256")
    if h and re.fullmatch(r"[0-9a-f]{64}", str(h).lower()):
        # Only read the file when a hash was actually recorded; the corpus is 1.3 GB of layers and a
        # census that slurps every one of them is a census nobody runs.
        digest = hashlib.sha256()
        with open(p, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                digest.update(chunk)
        if digest.hexdigest() != str(h).lower():
            return "HASH", "sidecar sha %s..., disk sha %s..." % (str(h)[:12], digest.hexdigest()[:12])
    return "OK", "%d B verified" % size


def census(root):
    rows, tot = [], {c: 0 for c in CLASSES}
    metas = glob.glob(os.path.join(root, "**", "*.meta.json"), recursive=True)
    for m in metas:
        cls, note = check_pair(m)
        tot[cls] += 1
        rows.append((cls, m.replace("\\", "/"), note))
    return tot, rows, len(metas)


def self_test():
    import shutil, tempfile
    tmp = tempfile.mkdtemp(prefix="provst-")
    ok = True
    try:
        def plant(name, payload, meta):
            open(os.path.join(tmp, name), "wb").write(payload)
            json.dump(meta, open(os.path.join(tmp, name + ".meta.json"), "w"))
        good = b"hello world\r\n"
        plant("good.txt", good, {"evidence_file": "good.txt", "bytes": len(good),
                                 "sha256": hashlib.sha256(good).hexdigest()})
        plant("sized.txt", b"truncated", {"evidence_file": "sized.txt", "bytes": 999})
        plant("hashed.txt", b"changed bytes", {"evidence_file": "hashed.txt", "bytes": 13,
                                               "sha256": "0" * 64})
        plant("lonely.txt", b"x", {"evidence_file": "absent.txt", "bytes": 1})
        plant("listing.json", b"[]", {"bytes": 2})
        open(os.path.join(tmp, "broken.meta.json"), "w").write("{not json")
        want = {"good.txt": "OK", "sized.txt": "SIZE", "hashed.txt": "HASH",
                "lonely.txt": "MISSING", "listing.json": "NO_EVIDENCE", "broken": "UNPARSEABLE"}
        for stem, exp in want.items():
            p = os.path.join(tmp, stem + ".meta.json") if stem != "broken" else os.path.join(tmp, "broken.meta.json")
            got, note = check_pair(p)
            print("%-12s %-11s %s" % (stem, got, "PASS" if got == exp else "*** FAILED, expected %s ***" % exp))
            ok = ok and got == exp
        tot, rows, n = census(tmp)
        print("census over the fixture: %d sidecars -> %s" % (n, tot))
        ok = ok and n == 6 and tot["OK"] == 1 and tot["SIZE"] == 1 and tot["HASH"] == 1 \
            and tot["MISSING"] == 1 and tot["NO_EVIDENCE"] == 1 and tot["UNPARSEABLE"] == 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("provenance_check self-test: %s" % ("PASS" if ok else "FAIL -- a checker that cannot catch a bad "
                                              "sidecar is not a checker"))
    return 0 if ok else 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="founders_playbook")
    ap.add_argument("--out")
    ap.add_argument("--show", type=int, default=40, help="worst-class rows to print")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    tot, rows, n = census(a.root)
    byfam = {}
    for cls, path, note in rows:
        fam = re.sub(r"^founders_playbook/", "", path).split("/")[0:3]
        key = "/".join(fam[:2]) + "/**/" + (path.split("/")[-1].replace(".meta.json", ""))
        famkey = "/".join(re.sub(r"^founders_playbook/", "", path).split("/")[:3])
        byfam.setdefault(famkey, {c: 0 for c in CLASSES})[cls] += 1
    lines = ["# Provenance census -- %s" % a.root, ""]
    lines.append("Sidecars read: **%d**. Classes: %s" % (n, ", ".join("%s %d" % (c, tot[c]) for c in CLASSES)))
    bad = [r for r in rows if r[0] != "OK" and r[0] != "NO_EVIDENCE"]
    lines.append("")
    lines.append("A `NO_EVIDENCE` row is a listing-only response (the harvester stored a query answer, not a "
                 "document) and is NOT damage. Everything else here is: the sidecar and the bytes disagree.")
    lines.append("")
    lines.append("## Families carrying non-OK rows")
    for k, v in sorted(byfam.items(), key=lambda kv: -(kv[1]["SIZE"] + kv[1]["HASH"] + kv[1]["MISSING"]
                                                       + kv[1]["UNPARSEABLE"])):
        s = v["SIZE"] + v["HASH"] + v["MISSING"] + v["UNPARSEABLE"]
        if s:
            lines.append("- `%s` -- SIZE %d, HASH %d, MISSING %d, UNPARSEABLE %d (OK %d)"
                         % (k, v["SIZE"], v["HASH"], v["MISSING"], v["UNPARSEABLE"], v["OK"]))
    lines.append("")
    lines.append("## First %d rows" % a.show)
    for cls, path, note in bad[:a.show]:
        lines.append("- `%s` **%s** -- %s" % (path, cls, note))
    md = "\n".join(lines) + "\n"
    print(md.split("## Families")[0])
    print("non-OK, non-listing rows: %d (listed in the report)" % len(bad))
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        open(a.out, "w", encoding="utf-8").write(md)
        print("written: %s" % a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
