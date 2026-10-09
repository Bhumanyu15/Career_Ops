---
name: compare
description: "Compare multiple evaluated opportunities side by side with qualified recommendations."
argument-hint: "[company names to compare, or 'my top options']"
user-invocable: true
allowed-tools:
  - Read
  - Glob
---

# Compare Opportunities

Compare evaluated roles from workspace data.

## Path Rules

Read `${CLAUDE_PLUGIN_ROOT}/references/path-policy.md`.
Read evaluations from `${WORKSPACE_ROOT}/evaluations/`.

## Flow

1. Select 2+ opportunities from evaluation files.
2. Build side-by-side table (score, comp, location, risks, status).
3. Provide recommendation with uncertainty/assumptions clearly stated.

Use qualified language:
- Guidance only, not a guarantee of offer outcomes.
- Avoid deterministic claims like "most likely to get an offer".
