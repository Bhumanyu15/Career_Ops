---
name: outreach
description: "Draft personalized outreach messages for networking and recruiting conversations."
argument-hint: "<contact/company context>"
user-invocable: true
allowed-tools:
  - Read
  - Write
  - WebSearch
  - Glob
---

# Draft Outreach

Create personalized outreach drafts using verified facts only.

## Rules

- Never fabricate achievements, relationships, or credentials.
- Never claim referrals/connections that do not exist.
- Never send messages automatically; user must review and send personally.
- Keep requests specific and respectful.

## Path Rules

Read `${CLAUDE_PLUGIN_ROOT}/references/path-policy.md`.
Use `${WORKSPACE_ROOT}` for user data and `${CLAUDE_PLUGIN_ROOT}` for bundled refs.

## Flow

1. Load `${WORKSPACE_ROOT}/profile.yml`, related research, and evaluations.
2. Identify contact and channel.
3. Draft using Hook + Proof + Proposal structure.
4. Offer variations (tone/channel/follow-up draft text).

Note: follow-up drafts are templates only; no automatic reminder/sending behavior.
