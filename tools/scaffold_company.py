#!/usr/bin/env python3
"""
scaffold_company.py -- create a company directory for every Fortune-50 slug that lacks one, and move
into it the bytes the harvester already holds for that slug.

Why this exists (RD-124). 37 of the 50 slugs have no `company_NNN_<slug>` directory, so 1,051 harvest
candidate rows and 11.4 MB of already-held founding-decade print sit in
`00_universe/harvest/mine_bytes/<slug>/`, where no company gate, no `company_status` line and no
authoring agent can reach them. Scaffolding -- not searching -- is the binding constraint on the tail.

The slug vocabulary is the HARVESTER's, because that is what `candidates.csv` and `mine_bytes/` are keyed
by; the rank comes from the frozen universe CSV by matching normalised company names. Four universe names
are abbreviated in the harvester (`bofa`, `gm`, `jnj`, `ups`) and no containment test can reach them, so
they are aliased explicitly and the alias list is printed, so a wrong one is visible instead of silent.

Conservative by construction: it creates directories and empty `research/`, `_parts/`,
`sources/corporate_print/` and never a dossier, register, verdict or STATUS line -- those are an agent's
work, and a script that writes a plausible-looking empty structure invites a later reader to trust it.
Bytes are moved only when the file is attributed to this slug, and never over an existing file: a clash
is reported and both copies stay put.

  python tools/scaffold_company.py --dry-run
  python tools/scaffold_company.py --only berkshire,chevron
"""

import argparse
import csv
import io
import json
import os
import re
import shutil
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAY = os.path.join(REPO, "founders_playbook")
UNIVERSE = os.path.join(PLAY, "00_universe", "fortune_top_50_2026.csv")
CAND = os.path.join(PLAY, "00_universe", "harvest", "candidates.csv")
BASE = os.path.join(PLAY, "01_companies")
MINE = os.path.join(PLAY, "00_universe", "harvest", "mine_bytes")

# Universe name -> harvester slug, where no normalised containment test can bridge them.
ALIAS = {"Bank of America": "bofa", "General Motors": "gm", "Johnson & Johnson": "jnj",
         "United Parcel Service": "ups"}


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def universe_rows():
    out = []
    for r in csv.DictReader(io.open(UNIVERSE, encoding="utf-8")):
        digits = re.sub(r"\D", "", r.get("rank") or "")
        if not digits:
            continue
        out.append((int(digits), (r.get("company") or "").strip()))
    return sorted(out)


def harvest_slugs():
    if not os.path.exists(CAND):
        return set()
    return {(r.get("company") or "").strip().lower() for r in csv.DictReader(io.open(CAND, encoding="utf-8"))
            if (r.get("company") or "").strip()}


def assign_slugs(uni, hs):
    """rank -> slug, from the harvester's own vocabulary. Anything unresolved is returned, never guessed."""
    mapping, unresolved = {}, []
    taken = set()
    for rank, name in uni:
        if name in ALIAS and ALIAS[name] in hs:
            slug = ALIAS[name]
        else:
            n = norm(name)
            cands = [s for s in hs if s and s not in taken and (n == s or n.startswith(s) or s in n)]
            slug = cands[0] if len(cands) == 1 else None
        if not slug:
            unresolved.append((rank, name))
            continue
        mapping[rank] = slug
        taken.add(slug)
    return mapping, unresolved, sorted(hs - set(mapping.values()))


def existing_dirs():
    out = {}
    if not os.path.isdir(BASE):
        return out
    for d in os.listdir(BASE):
        m = re.match(r"company_(\d+)_(.+)$", d)
        if m:
            out[m.group(2)] = int(m.group(1))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="comma-separated slugs to consider (default: all missing)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    uni = universe_rows()
    hs = harvest_slugs()
    if not uni:
        print("no universe file at %s -- refusing to invent ranks" % UNIVERSE)
        return 2
    if not hs:
        print("no candidates.csv -- the harvester slug vocabulary is unknown; refusing to guess slugs")
        return 2
    mapping, unresolved, extra_slugs = assign_slugs(uni, hs)
    have = existing_dirs()
    want = {s.strip().lower() for s in a.only.split(",")} if a.only else None

    created, moved, clashes = [], [], []
    for rank in sorted(mapping):
        slug = mapping[rank]
        if want and slug not in want:
            continue
        if slug in have:
            continue
        d = os.path.join(BASE, "company_%03d_%s" % (rank, slug))
        if not a.dry_run:
            for sub in ("", "research", "_parts", os.path.join("sources", "corporate_print")):
                os.makedirs(os.path.join(d, sub), exist_ok=True)
        created.append((rank, slug, os.path.relpath(d, REPO)))
        src = os.path.join(MINE, slug)
        if os.path.isdir(src):
            for fn in sorted(os.listdir(src)):
                p = os.path.join(src, fn)
                if not os.path.isfile(p):
                    continue
                dst = os.path.join(d, "sources", "corporate_print", fn)
                if os.path.exists(dst):
                    clashes.append(fn)
                    continue
                if not a.dry_run:
                    shutil.move(p, dst)
                moved.append((slug, fn))
            if not a.dry_run and not [f for f in os.listdir(src) if os.path.isfile(os.path.join(src, f))]:
                os.rmdir(src)

    rep = {"created": created, "bytes_moved": len(moved), "clashes": clashes,
           "unresolved_universe_rows": unresolved, "harvest_slugs_with_no_universe_row": extra_slugs,
           "dry_run": bool(a.dry_run)}
    if a.json:
        print(json.dumps(rep, indent=1))
    else:
        print("dirs created: %d | bytes moved: %d | clashes: %d" % (len(created), len(moved), len(clashes)))
        for r, s, rel in created:
            print("   +%3d %-16s %s" % (r, s, rel))
        if unresolved:
            print("UNRESOLVED universe rows (no unique slug): %s"
                  % ", ".join("%d:%s" % (r, n) for r, n in unresolved))
        if extra_slugs:
            print("HARVEST slugs with no universe row: %s" % ", ".join(extra_slugs))
        if clashes:
            print("CLASHES left in place, nothing overwritten: %s" % ", ".join(clashes[:10]))
        if a.dry_run:
            print("(dry run: nothing written)")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
