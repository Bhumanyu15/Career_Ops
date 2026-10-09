# Career Ops Plugin (Replicated Source)

This repository contains the **actual Career Ops Claude plugin files** (not just clone instructions), copied from:

- Source: https://github.com/andrew-shwetzer/career-ops-plugin-do-not-fork-currently-updating-v2-
- Source commit: `ae447d7bf902da2a5cf4f22762c4e8dfdd8e6f9d`

## What this tool does

Career Ops is a job-search copilot plugin for Claude that helps you:

- Evaluate job postings with a structured score
- Tailor ATS-friendly resumes for specific roles
- Scan company career pages for openings
- Track applications and pipeline status
- Draft outreach messages and interview prep content

It is designed for multiple industries, not only software roles.

## Included plugin structure

This repo includes the plugin directories and files from the source project:

- `.claude-plugin/plugin.json`
- `agents/`
- `commands/`
- `references/`
- `skills/`
- `LICENSE`, `ATTRIBUTION.md`, `.gitignore`

## Requirements

- A Claude host that supports local plugin directories (for example, Claude Cowork / compatible Claude CLI workflow)
- Git (to clone this repository)
- A local workspace where Claude can read/write files (the plugin stores profile/application data in `data/` during use)

## Installation

1. Clone this repository locally.
2. Start Claude with this plugin directory, e.g. using your host's plugin-dir option.
   - Example from source docs:
     - `claude --plugin-dir /path/to/this/repo`
3. In Claude, run `setup` and paste your resume (or answer questions) to initialize `data/profile.yml`.

## First-time usage

After setup, try:

- `help` — list all available skills
- `quick-eval` — fast score for a job post
- `evaluate` — full assessment
- `tailor-resume` — generate a role-specific resume
- `track` — view/update application tracker

## Accounts and costs

- The plugin itself is local content in this repo and has no separate license fee.
- You still need access to a Claude product that supports this plugin workflow (that host may require a paid plan).
- Some skills may use web lookup/tooling provided by your Claude environment; any cost depends on your Claude/tool provider plan.

## Notes and limitations

- `data/` and `config/` are gitignored to avoid committing personal job-search data.
- `references/ats-endpoints.md` notes that some ATS API domains can be blocked in Cowork sandbox environments, and recommends WebSearch fallbacks.

## License and attribution

- License: MIT (`LICENSE`)
- Attribution: `ATTRIBUTION.md`

Original copyright and attribution are preserved.
