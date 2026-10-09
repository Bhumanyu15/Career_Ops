#!/usr/bin/env python3
"""Static checks for plugin structure and policy conformance."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_TEMPLATE_PLACEHOLDERS = {
    "{{NAME}}",
    "{{CONTACT_LINE}}",
    "{{SUMMARY}}",
    "{{EXPERIENCE}}",
    "{{EDUCATION}}",
    "{{SKILLS}}",
}

errors: list[str] = []


def check_manifest() -> None:
    p = ROOT / ".claude-plugin" / "plugin.json"
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"manifest parse failed: {e}")
        return
    for key in ("name", "version", "description", "license"):
        if key not in data:
            errors.append(f"manifest missing key: {key}")


def check_frontmatter(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"frontmatter missing start: {path.relative_to(ROOT)}")
        return
    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append(f"frontmatter missing end: {path.relative_to(ROOT)}")


def check_frontmatters() -> None:
    for p in sorted((ROOT / "commands").glob("*.md")):
        check_frontmatter(p)
    for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
        check_frontmatter(p)
    for p in sorted((ROOT / "agents").glob("*.md")):
        check_frontmatter(p)


def check_path_policy_usage() -> None:
    scope_files = list((ROOT / "commands").glob("*.md")) + list((ROOT / "skills").glob("*/SKILL.md")) + list((ROOT / "agents").glob("*.md"))
    for p in sorted(scope_files):
        text = p.read_text(encoding="utf-8")
        if "path-policy.md" not in text:
            errors.append(f"missing path-policy reference: {p.relative_to(ROOT)}")
        if "CLAUDE_PLUGIN_ROOT" not in text:
            errors.append(f"missing CLAUDE_PLUGIN_ROOT mention: {p.relative_to(ROOT)}")
        if "WORKSPACE_ROOT" not in text:
            errors.append(f"missing WORKSPACE_ROOT mention: {p.relative_to(ROOT)}")


def check_bundled_reference_paths() -> None:
    md_files = list((ROOT / "commands").glob("*.md")) + list((ROOT / "skills").glob("*/SKILL.md")) + list((ROOT / "agents").glob("*.md"))
    pattern = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/([A-Za-z0-9_./-]+)")
    for p in md_files:
        text = p.read_text(encoding="utf-8")
        for m in pattern.finditer(text):
            rel = m.group(1)
            target = ROOT / rel
            if not target.exists():
                errors.append(f"missing bundled reference target {rel} in {p.relative_to(ROOT)}")


def check_resume_template() -> None:
    t = (ROOT / "references" / "resume-template.html").read_text(encoding="utf-8")
    found = set(re.findall(r"\{\{[A-Z_]+\}\}", t))
    missing = REQUIRED_TEMPLATE_PLACEHOLDERS - found
    if missing:
        errors.append("resume template missing placeholders: " + ", ".join(sorted(missing)))


def check_packaging_exclusions() -> None:
    txt = (ROOT / "scripts" / "package_plugin.py").read_text(encoding="utf-8")
    must_have = ["data/**", "config/**", ".git/**", "*.env", "*.pem", "*.key"]
    for token in must_have:
        if token not in txt:
            errors.append(f"packaging exclusions missing token: {token}")


def main() -> int:
    check_manifest()
    check_frontmatters()
    check_path_policy_usage()
    check_bundled_reference_paths()
    check_resume_template()
    check_packaging_exclusions()

    if errors:
        print("FAILED static checks:")
        for e in errors:
            print(f"- {e}")
        return 1

    print("All static checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
