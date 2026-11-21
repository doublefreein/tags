#!/usr/bin/env python3
"""Check every passport's hash chain (PRD R14). No dependencies, no account.

    python3 verify.py            # all passports
    python3 verify.py DF-CRO-26-0001

Each event is hashed as SHA-256 of its canonical JSON (sorted keys, no
spaces, UTF-8). Every event must carry the hash of the event before it,
and every photo it names must exist under media/ with a matching hash.
Signature checks will be added when signing keys are introduced (PRD 7.3).
"""
import hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def h(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False,
                                     separators=(",", ":")).encode()).hexdigest()

def verify(pdir: Path) -> list[str]:
    errors, prev = [], None
    for f in sorted((pdir / "events").glob("*.json")):
        ev = json.loads(f.read_text())
        if ev.get("prev_hash") != prev:
            errors.append(f"{f.name}: prev_hash does not match the previous event")
        for sha in ev.get("payload", {}).get("media", []):
            m = ROOT / "media" / f"{sha}.jpg"
            if not m.exists():
                errors.append(f"{f.name}: missing media {sha[:12]}…")
            elif hashlib.sha256(m.read_bytes()).hexdigest() != sha:
                errors.append(f"{f.name}: media {sha[:12]}… does not match its hash")
        prev = h(ev)
    head = json.loads((pdir / "passport.json").read_text()).get("head_hash")
    if head != prev:
        errors.append("passport.json head_hash does not match the last event")
    return errors

ids = sys.argv[1:] or sorted(p.name for p in (ROOT / "passports").iterdir() if p.is_dir())
bad = 0
for pid in ids:
    errs = verify(ROOT / "passports" / pid)
    print(f"{pid}: {'OK' if not errs else 'FAILED'}")
    for e in errs:
        print("  -", e)
    bad += bool(errs)
sys.exit(1 if bad else 0)
