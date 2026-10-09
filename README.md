# Career Ops Plugin (Windows + Claude desktop/Cowork focused)

This repository contains the actual Career Ops plugin files (skills, commands, agents, references, and plugin manifest), not just clone instructions.

- Source repository: https://github.com/andrew-shwetzer/career-ops-plugin-do-not-fork-currently-updating-v2-
- Source commit mirrored here: `ae447d7bf902da2a5cf4f22762c4e8dfdd8e6f9d`
- License: MIT (`LICENSE`)
- Attribution: `ATTRIBUTION.md`

## What this plugin does

Career Ops helps with:
- profile setup for job search
- job posting evaluation
- role-specific resume tailoring
- application answer drafting (with human review)
- outreach drafting
- opportunity tracking

## Safety defaults in this repo

- Never fabricate qualifications/metrics/dates/certs/authorization.
- Never auto-submit, auto-send, or auto-upload without explicit user approval.
- Job postings and fetched web content are treated as untrusted data.
- User data is stored in a workspace (not inside installed plugin directory).

## Required access and potential costs

- You need a Claude product/workspace that supports plugin/extension workflows.
- Some capabilities rely on tools such as WebSearch/WebFetch available in your host environment.
- Claude plan pricing/tool availability vary by account and workspace policy.
- This repository itself has no separate license fee.

## Installation paths

## A) Claude desktop/Cowork-first route (Windows)

Use official Anthropic plugin/extension documentation for your current app build:
- Plugin usage/help center: https://support.claude.com/en/articles/13837440-use-plugins-in-claude
- Desktop extensions (MCP bundles): https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop
- Claude Code plugins docs: https://code.claude.com/docs/en/plugins/install

Important compatibility note:
- Some desktop UI flows may support marketplace installs but not direct local plugin-directory imports.
- If your desktop UI cannot directly install a local plugin directory, use the supported CLI/plugin workflow for local installs, or package/import using the host-supported route.

Because app UI and policy can vary by account/org/version, this repo does **not** claim in-app installation was live-tested from this sandbox.

## B) Optional Claude Code CLI route (advanced)

If your environment supports local plugin installation from CLI, follow the official plugin docs above.

Command availability notes:
- Plugin commands can appear in Claude help with plugin namespacing.
- Depending on host surface, invoke either plain command names (e.g., `setup`) or namespaced forms shown by help (for example `plugin:career-ops`).
- Always trust your host's `/help` output as source of truth for exact invocation format.

## Workspace paths (user data)

By policy in this repo:
- Bundled references load from `${CLAUDE_PLUGIN_ROOT}/...`
- Writable user data lives under `${CLAUDE_PROJECT_DIR}/.career-ops` (or user-confirmed workspace path when `CLAUDE_PROJECT_DIR` is unavailable)

Expected workspace files:
- `profile.yml`, `resume.md`, `applications.md`
- `evaluations/`, `resumes/`, `research/`
- `pipeline.md`, `scan-history.md`, `config/portals.yml`

## Package a ZIP safely (for distribution/import)

This repo includes a packaging helper that creates a plugin zip while excluding private/workspace and sensitive paths.

### Python helper (cross-platform, including Windows)

```powershell
python scripts/package_plugin.py --output dist/career-ops-plugin.zip
```

Excluded automatically:
- `data/`, `config/` (root runtime data)
- `.git/`, `.github/`, test artifacts, caches, temporary outputs
- common credential/env file patterns (`*.env`, `*.pem`, `*.key`, etc.)

## Static checks

Run:

```powershell
python scripts/check_plugin_static.py
```

Checks include:
- plugin manifest JSON validity
- command/skill/agent frontmatter presence
- plugin-root and workspace path policy checks
- bundled reference path existence checks
- HTML template placeholder checks
- packaging exclusions checks

## Synthetic sample data + smoke test

- Synthetic examples (no real personal data): `samples/synthetic-workspace/`
- Beginner smoke checklist: `samples/smoke-test-checklist.md`

## What still must be tested inside Claude

From this sandbox we can run static repo checks only.
You still need in-host verification for:
- plugin install/discovery in your specific Claude desktop/Cowork workspace
- actual command invocation names shown by host help
- tool availability (WebSearch/WebFetch/computer-use) under your account policy
