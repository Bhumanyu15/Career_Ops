---
name: research
description: "Research a company before applying or interviewing and save a structured brief."
argument-hint: "<company name>"
user-invocable: true
allowed-tools:
  - Read
  - Write
  - WebSearch
  - WebFetch
  - Glob
---

# Company Research

Build a factual intelligence brief for a target company.

## Path Rules

Read `${CLAUDE_PLUGIN_ROOT}/references/path-policy.md`.
Use workspace files:
- `${WORKSPACE_ROOT}/evaluations/`
- `${WORKSPACE_ROOT}/research/{company-slug}.md`

## Safety

- Cite where information came from when possible.
- Mark uncertain/outdated information clearly.
- Do not scrape private data or request credentials.

## Flow

1. Gather public company info, recent developments, and interview context.
2. Find likely contacts from public sources.
3. Save the brief for reuse.
