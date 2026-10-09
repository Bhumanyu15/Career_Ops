#!/usr/bin/env python3
"""Create a plugin ZIP with privacy-safe exclusions."""

from __future__ import annotations

import argparse
import fnmatch
from pathlib import Path
import zipfile

REQUIRED_PATHS = [
    ".claude-plugin/plugin.json",
    "agents",
    "commands",
    "references",
    "skills",
    "README.md",
    "LICENSE",
    "ATTRIBUTION.md",
]

EXCLUDE_GLOBS = [
    ".git/*",
    ".git/**",
    ".github/*",
    ".github/**",
    "data/*",
    "data/**",
    "config/*",
    "config/**",
    "dist/*",
    "dist/**",
    "build/*",
    "build/**",
    "tmp/*",
    "tmp/**",
    "**/__pycache__/*",
    "**/.pytest_cache/*",
    "**/*.pyc",
    "**/*.env",
    "**/*.pem",
    "**/*.key",
    "**/*credentials*",
    "**/*secret*",
    "samples/*",
    "samples/**",
]


def excluded(rel: str) -> bool:
    return any(fnmatch.fnmatch(rel, pat) for pat in EXCLUDE_GLOBS)


def iter_files(root: Path):
    seen = set()
    for req in REQUIRED_PATHS:
        p = root / req
        if not p.exists():
            raise FileNotFoundError(f"Required path missing: {req}")
        if p.is_file():
            rel = p.relative_to(root).as_posix()
            if not excluded(rel):
                seen.add(rel)
                yield p
        else:
            for f in sorted(x for x in p.rglob("*") if x.is_file()):
                rel = f.relative_to(root).as_posix()
                if rel in seen:
                    continue
                if excluded(rel):
                    continue
                seen.add(rel)
                yield f


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="dist/career-ops-plugin.zip")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    out = root / args.output
    out.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in iter_files(root):
            rel = f.relative_to(root).as_posix()
            zf.write(f, rel)

    print(f"Created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
