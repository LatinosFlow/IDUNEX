#!/usr/bin/env python3
"""High-confidence secret pattern scan for IDUNEX repository."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PATTERNS = {
    "OPENAI_OR_GENERIC_SK_TOKEN": re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}\b"),
    "GITHUB_CLASSIC_TOKEN": re.compile(r"\bghp_[A-Za-z0-9_]{30,}\b"),
    "GITHUB_FINE_GRAINED_TOKEN": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b"),
    "PRIVATE_KEY_BLOCK": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
}
TEXT_EXT = {".py", ".json", ".md", ".txt", ".yml", ".yaml", ".csv", ".sh", ".toml", ".ini"}
SKIP_PARTS = {".git", "dist", "node_modules", "__pycache__"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    hits: list[str] = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if set(path.relative_to(root).parts) & SKIP_PARTS:
            continue
        if path.suffix.lower() not in TEXT_EXT:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for name, pattern in PATTERNS.items():
            if pattern.search(text):
                hits.append(f"{name}: {path.relative_to(root)}")

    if hits:
        print("High-confidence secret patterns found:")
        for hit in hits:
            print(f"- {hit}")
        return 1
    print("PASS: no high-confidence secret patterns found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
