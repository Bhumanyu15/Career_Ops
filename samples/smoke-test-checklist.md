# Beginner Smoke-Test Checklist (Synthetic Data Only)

Use only synthetic files from `samples/synthetic-workspace/`.
Do not paste real resume or credentials.

- [ ] **Setup**: run `setup`, confirm profile review is shown before final save.
- [ ] **Help**: run `help` and confirm command/skill list appears.
- [ ] **Quick eval**: run `quick-eval` on a sample JD text and confirm score + short rationale.
- [ ] **Full evaluation**: run `evaluate` and confirm report is saved under workspace `evaluations/`.
- [ ] **Resume HTML**: run `tailor-resume` and confirm HTML output under workspace `resumes/`.
- [ ] **Tracking**: run `track`, update a status, confirm transition validation and confirmation prompt.
- [ ] **Apply safety**: run `apply` and confirm no auto-submit/upload/send occurs without explicit approval.
- [ ] **Sensitive questions**: verify demographic/EEO answers are deferred to user.
- [ ] **Relocation/auth/start date**: verify explicit prompts appear when missing/ambiguous.
