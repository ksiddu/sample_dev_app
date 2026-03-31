# Sample Dev App

This is a minimal static web app used to demonstrate CI/CD integration with a separate QA automation repo.

## Run Locally
```bash
python3 serve.py
```
Open http://127.0.0.1:8000

## CI Integration
The GitHub Actions workflow triggers the QA repo smoke workflow on PRs to main or master.

Required secrets in this repo:
- QA_REPO_TOKEN: a token with permission to dispatch workflows in the QA repo

Update the QA repo target in .github/workflows/pr-smoke.yml if your QA repo is different.
PR smoke test Tue 31 Mar 2026 20:05:31 +08
