# Path Policy (Plugin Root + User Workspace)

Use this policy in all commands, skills, and agents.

## 1) Read-only bundled plugin files

Use plugin-root resolution for bundled assets:

- `${CLAUDE_PLUGIN_ROOT}/references/...`
- `${CLAUDE_PLUGIN_ROOT}/commands/...`
- `${CLAUDE_PLUGIN_ROOT}/skills/...`
- `${CLAUDE_PLUGIN_ROOT}/agents/...`

Do not assume relative paths like `references/...` resolve correctly in every host.

## 2) Writable user files (never inside installed plugin dir)

Store user data in a project workspace folder:

- Preferred workspace root: `${CLAUDE_PROJECT_DIR}/.career-ops`
- If `${CLAUDE_PROJECT_DIR}` is unavailable, ask user to choose a writable folder first and use that consistently.

Use these workspace files:

- `${WORKSPACE_ROOT}/profile.yml`
- `${WORKSPACE_ROOT}/resume.md`
- `${WORKSPACE_ROOT}/applications.md`
- `${WORKSPACE_ROOT}/evaluations/*.md`
- `${WORKSPACE_ROOT}/resumes/*.html`
- `${WORKSPACE_ROOT}/research/*.md`
- `${WORKSPACE_ROOT}/pipeline.md`
- `${WORKSPACE_ROOT}/scan-history.md`
- `${WORKSPACE_ROOT}/config/portals.yml`

## 3) Host limitations

- Claude Code exposes plugin commands/skills directly and supports `${CLAUDE_PLUGIN_ROOT}` paths in plugin instructions.
- Some Claude Desktop/Cowork surfaces may not expose local plugin-directory install flows in UI; users may need supported plugin/extension install routes for their host.
- If required variables are unavailable, stop and ask the user to confirm workspace location before writing files.
