---
name: setup
description: "Set up your job search profile from resume or guided questions. Required before evaluation."
argument-hint: "[--reset to start over]"
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Glob
---

# Set Up Your Profile

Friendly setup flow for first-time users.

## Path + Safety Rules (required)

1. Read `${CLAUDE_PLUGIN_ROOT}/references/path-policy.md`.
2. Read `${CLAUDE_PLUGIN_ROOT}/references/safety-policy.md`.
3. Set `WORKSPACE_ROOT` to `${CLAUDE_PROJECT_DIR}/.career-ops` when available.
4. If `CLAUDE_PROJECT_DIR` is unavailable, ask user to choose a writable workspace path before proceeding.

Use:
- `${WORKSPACE_ROOT}/profile.yml`
- `${WORKSPACE_ROOT}/resume.md`
- `${WORKSPACE_ROOT}/applications.md`

## Step 0: Check Existing Profile

Read `${WORKSPACE_ROOT}/profile.yml`.

If it exists and no `--reset`, summarize and ask whether to edit specific sections.

## Step 1: Collect Information

Offer two modes:
- Paste resume text/content (preferred)
- Guided questions

Always collect/confirm these fields explicitly (do not infer):
- target roles
- location preferences
- relocation willingness (separate from remote/hybrid/onsite)
- work authorization status and any constraints
- earliest start date

If anything is unclear, ask follow-up questions.

## Step 2: Build Draft Profile (no final write yet)

Build a draft profile according to `${CLAUDE_PLUGIN_ROOT}/references/profile-schema.md`.

Rules:
- Never fabricate missing details.
- Keep uncertain values as explicit unknowns and ask the user.
- Keep facts from resume/profile unchanged; only normalize formatting.

## Step 3: Mandatory Review Before Finalize

Show a concise profile summary and ask for corrections.

Only after explicit user confirmation:
- Write `${WORKSPACE_ROOT}/profile.yml`
- If resume text was provided, write `${WORKSPACE_ROOT}/resume.md`

## Step 4: Ensure Tracker Exists

If missing, create `${WORKSPACE_ROOT}/applications.md` with:

```markdown
# Job Applications

| Date Added | Date Applied | Company | Role | Score | Status | Evaluation | Notes |
|---|---|---|---|---|---|---|---|
```

## Step 5: Next Commands

Suggest:
- `help`
- `quick-eval`
- `evaluate`
