---
name: track
description: "View and update application tracking data and status summaries."
argument-hint: "[status filter, company, or 'update Company to Status']"
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Glob
---

# Application Tracker

Manage application statuses from workspace data.

## Path Rules

Read `${CLAUDE_PLUGIN_ROOT}/references/path-policy.md`.
Use `${WORKSPACE_ROOT}/applications.md` where `WORKSPACE_ROOT = ${CLAUDE_PROJECT_DIR}/.career-ops`.
Validate state transitions using `${CLAUDE_PLUGIN_ROOT}/references/states.md`.

## Step 0: Load tracker

Read `${WORKSPACE_ROOT}/applications.md`; create with standard header if missing.

## Step 1: Parse intent

Support view/filter/update/stats/delete actions.

## Step 2: Safe update flow

For status updates:
1. Show current row + proposed change.
2. Ask explicit confirmation.
3. Apply only valid transitions.
4. Set Date Applied when moving into `Applied`.

## Step 3: Dashboard + suggestions

Show summary metrics and practical suggestions.

Reminder behavior note:
- Do not promise automatic reminder scheduling.
- Explain that follow-up candidates are surfaced when tracker is opened, unless user has separately configured an external scheduler.
