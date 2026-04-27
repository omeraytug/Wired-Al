# branching_and_git_workflow.md

## Branching and Git Workflow

Default model:

* main is protected
* work happens in feature branches
* changes land through pull requests

---

## Branch Naming

Prefer:
feature/...
fix/...
chore/...

Examples:
feature/seed-rag-knowledge-base
fix/handle-tool-timeout

Names should explain intent.

---

## Commit Guidance

Prefer small atomic commits.

Good:
feat: add retrieval fallback handling

Bad:
stuff

Commits are historical evidence.

---

## Rules

* No direct commits to main
* Rebase or merge per team convention
* Keep branches short-lived
* Avoid giant divergence

Long-lived branches grow teeth.

---

## Informal Rule

If resolving merge conflicts feels archaeological,
branch lived too long.
