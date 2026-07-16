#!/usr/bin/env python3
"""Package engine/IDUNEX into a ZIP + external SHA companion.

This creates a new package from the repository source tree. Its SHA may differ
from the original received ZIP because packaging metadata and ordering may differ.
The result is a candidate artifact, not an official release unless release gates pass.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path
from datetime import datetime, timezone

FIXED_DOS_DATE = (2026, 1, 1, 0, 0, 0)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--version", required=True)
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    engine_root = root / "engine" / "IDUNEX"
    if not engine_root.is_dir():
        print("ERROR: engine/IDUNEX not found", file=sys.stderr)
        return 1

    version = args.version.strip()
    if version.startswith("v"):
        clean_version = version
    else:
        clean_version = f"v{version}"

    dist = root / "dist"
    dist.mkdir(exist_ok=True)
    zip_path = dist / f"IDUNEX_MOTOR_{clean_version}.zip"
    sha_path = dist / f"IDUNEX_MOTOR_{clean_version}.zip.sha256"
    manifest_path = dist / f"IDUNEX_MOTOR_{clean_version}_BUILD_MANIFEST.json"

    files = sorted(p for p in engine_root.rglob("*") if p.is_file())
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for file_path in files:
            rel = file_path.relative_to(root / "engine").as_posix()
            info = zipfile.ZipInfo(rel, FIXED_DOS_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, file_path.read_bytes())

    with zipfile.ZipFile(zip_path) as z:
        testzip = z.testzip()
        infos = z.infolist()
        stored = sum(1 for i in infos if i.compress_type == zipfile.ZIP_STORED)
        dirs = sum(1 for i in infos if i.filename.endswith("/"))
        internal_zip = sum(1 for i in infos if i.filename.lower().endswith(".zip"))

    digest = sha256_file(zip_path)
    sha_path.write_text(f"{digest}  {zip_path.name}\n", encoding="utf-8")
    manifest = {
        "status": "EN_REVISION",
        "artifact": zip_path.name,
        "sha256": digest,
        "bytes": zip_path.stat().st_size,
        "entries": len(infos),
        "directories": dirs,
        "stored": stored,
        "internal_zip": internal_zip,
        "testzip": "PASS" if testzip is None else f"FAIL:{testzip}",
        "source_path": "engine/IDUNEX",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "note": "Candidate package generated from repository source. Not official until M02/M03 and release gates pass.",
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 0 if testzip is None and stored == 0 and dirs == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
