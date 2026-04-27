# engineering_handbook.md

## Engineering Handbook — 404 Brain Not Found

**Version:** 0.1
**Audience:** Engineers, interns, technical contributors

---

# Purpose

This handbook describes how we build software.

Employee handbook explains how we work together.
This document explains how we engineer.

---

# Engineering Philosophy

We generally prefer:

* Simple systems over impressive systems
* Observable systems over opaque systems
* Small changes over heroic rewrites
* Reliable boring solutions over fragile cleverness

Default question:

Can we make this simpler?

---

# Typical Development Flow

Most work follows:

1. Pick up ticket
2. Clarify scope
3. Sketch approach
4. Implement small increments
5. Open PR early
6. Review and revise
7. Merge and monitor

Merge is not the end of work.
Production behavior matters.

---

# Definition of Done

Work is generally done when:

* Requirements addressed
* Tests pass
* Edge cases considered
* Documentation updated
* Review completed
* Monitoring implications considered

"It runs locally" is not definition of done.

---

# Code Principles

## Readability

Code is written for future humans.

Including tired future-you.

---

## Prefer Explicitness

Hidden magic ages badly.

Prefer:

* Clear names
* Small functions
* Predictable interfaces
* Visible error handling

---

## Comments

Comment why.
Not what obvious code does.

---

# Testing Expectations

Reasonable expectations:

* Unit tests for logic
* Integration tests for flows
* Manual validation for risky changes

No one expects exhaustive tests for every prototype.

But zero testing should feel suspicious.

---

# Git and Branching

Typical model:

* Feature branches
* Pull requests for changes
* Small atomic commits preferred

Commit messages should help archaeology.

Future debugging is time travel.
Leave clues.

---

# Pull Requests

Good PRs tend to:

* Solve one coherent thing
* Explain why change exists
* Note risks or tradeoffs
* Stay reviewable in size

Large mysterious PRs are called novels.

Novels are rarely merged happily.

---

# Code Review Norms

Review looks for:

* Correctness
* Maintainability
* Risk
* Simplicity
* Learning opportunities

Review is collaboration, not border control.

---

# Error Handling

Prefer:

* Fail clearly
* Log useful context
* Degrade gracefully where possible
* Use fallback behavior intentionally

Silent failure is usually just delayed failure.

---

# Observability

Think about:

* Logs
* Metrics
* Traces
* Alerts

If a system breaks and no one can tell why, monitoring is incomplete.

---

# Deployments

Normal principles:

* Small changes safer than giant releases
* Use checklists
* Have rollback path
* Never assume deployment succeeded

Trust, then verify.

---

# Working with AI Systems

For LLM and retrieval systems, additionally consider:

* Grounding
* Evaluation
* Prompt behavior
* Fallbacks
* Hallucination risk
* Tool failure modes

Model output is input requiring scrutiny.

---

# Escalation in Engineering Decisions

Proceed yourself:

* Refactors
* Small improvements
* Documentation fixes

Ask teammate:

* Interface changes
* Design uncertainty
* Shared ownership code

Escalate lead:

* Security risk
* Architecture shifts
* Production instability

---

# Engineering Anti-Patterns

Watch for:

* Premature abstraction
* Overengineering
* Cargo-cult patterns
* Hidden coupling
* Copy-paste architecture

And the classic:

"We’ll clean it up later."

History suggests otherwise.

---

# Design Biases We Prefer

When tradeoffs are close, bias toward:

* Maintainability
* Reversibility
* Operational simplicity
* Clear ownership

Elegant systems that no one can operate are not wins.

---

# The Carbon–Silicon Principle

Humans make judgment.
Systems provide leverage.

Good engineering augments people.
It does not hide reasoning from them.

---

# Informal Engineering Commandments

1. Do not deploy on vibes.

2. Read the error before rewriting the system.

3. If three people debug manually, automate it.

4. If everyone fears touching code, the code owns you.

5. There shall be no unhandled exceptions left behind.

---

**Related documents**

* code_review_guidelines.md
* branching_and_git_workflow.md
* deployment_runbook.md
* adr_001_why_fastapi.md
* adr_004_error_handling_strategy.md