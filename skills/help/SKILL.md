---
name: help
description: "Show available career-ops commands/skills and suggest the best next step."
argument-hint: "[skill name for detailed help]"
user-invocable: true
allowed-tools:
  - Read
  - Glob
---

# career-ops Help

## Path Rules

Read `${CLAUDE_PLUGIN_ROOT}/references/path-policy.md`.
Use workspace files under `${WORKSPACE_ROOT}`:
- `${WORKSPACE_ROOT}/profile.yml`
- `${WORKSPACE_ROOT}/applications.md`
- `${WORKSPACE_ROOT}/evaluations/*.md`
- `${WORKSPACE_ROOT}/resumes/*.html`

## Behavior

- Show command/skill directory.
- Suggest next step from current state.
- Mention safety expectations: human review before submit/send/upload actions.
