---
name: tailor-resume
description: "Generate an ATS-oriented resume tailored to a specific role while preserving factual accuracy."
argument-hint: "<company name or 'for the latest evaluation'>"
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Glob
---

# Tailor Your Resume

Generate a role-specific resume in HTML from verified user facts.

## Path + Safety Rules

Read:
- `${CLAUDE_PLUGIN_ROOT}/references/path-policy.md`
- `${CLAUDE_PLUGIN_ROOT}/references/safety-policy.md`
- `${CLAUDE_PLUGIN_ROOT}/references/ats-rules.md`
- `${CLAUDE_PLUGIN_ROOT}/references/resume-template.html`

Workspace:
- `${WORKSPACE_ROOT}/profile.yml`
- `${WORKSPACE_ROOT}/resume.md`
- `${WORKSPACE_ROOT}/evaluations/*.md`
- output `${WORKSPACE_ROOT}/resumes/{company}-{role}.html`

## Step 0: Load Context

Load profile + resume + target evaluation.
If no evaluation exists, ask user to evaluate first.

## Step 1: Build Resume Content

- Preserve factual history; tailor emphasis only.
- Never invent metrics, dates, certifications, qualifications, or projects.
- If a needed metric/detail is missing, ask user before finalizing.
- Include relevant projects when they materially support the role, including
  finance/data-analysis projects where applicable (not only creative/technology).

## Step 2: Generate HTML

Fill template placeholders and apply ATS-oriented constraints from rules file.

## Step 3: Review + Save

Show a short preview and ask user to confirm factual accuracy.
Write `${WORKSPACE_ROOT}/resumes/{filename}.html` after review.

## Step 4: Update Tracker

Update `${WORKSPACE_ROOT}/applications.md` status to `Resume Ready` when appropriate.

## Step 5: Next Steps

Provide print-to-PDF instructions (Ctrl+P on Windows) and suggest `apply`.
