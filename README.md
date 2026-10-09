# Career_Ops

This repository is set up as your own copy so you can use and customize the Career Ops plugin source.

## Create and use your own repository

1. Create a new empty repository in your GitHub account (for example: `Career_Ops`).
2. Clone the source project locally:
   ```bash
   git clone https://github.com/andrew-shwetzer/career-ops-plugin-do-not-fork-currently-updating-v2-.git
   cd career-ops-plugin-do-not-fork-currently-updating-v2-
   ```
3. Point the local clone to your new repository:
   ```bash
   git remote rename origin upstream
   git remote add origin https://github.com/<your-username>/<your-repo>.git
   ```
4. Push the code to your repository:
   ```bash
   git push -u origin main
   ```

After that, work from your own repository (`origin`) and optionally pull updates from `upstream` when needed.
