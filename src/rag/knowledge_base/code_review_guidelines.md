# code_review_guidelines.md

## Code Review Guidelines — 404 Brain Not Found

**Version:** 0.1
**Purpose:** Shared expectations for writing, reviewing and merging pull requests.

---

# Why We Review

Code review exists to improve:

* Correctness
* Maintainability
* Shared understanding
* Risk detection
* Learning

It is not a ritual before merge.
It is part of engineering.

---

# What Good Pull Requests Look Like

Good PRs are usually:

* Small enough to review in one sitting
* Focused on one coherent change
* Clear about intent
* Honest about tradeoffs

A reviewer should not need detective skills.

---

## A Good PR Description Includes

* What changed
* Why it changed
* Risks or edge cases
* Testing performed
* Questions where feedback is wanted

Template:

## Summary

Short explanation.

## Why

Problem addressed.

## Testing

What was validated.

## Risks

Known uncertainties.

---

# PR Size Guidance

Rough preference:

* Small: ideal
* Medium: normal
* Large: justify
* Massive: probably should be split

If someone needs snacks before reviewing your PR, it may be too large.

---

# Before Opening a PR

Ask yourself:

* Would I understand this PR cold?
* Is scope too broad?
* Are assumptions explained?
* Did I update docs if needed?
* Would I merge this if someone else wrote it?

That last question catches things.

---

# What Reviewers Look For

Reviewers commonly check:

## Correctness

* Does it work?
* Are edge cases missed?
* Can it fail dangerously?

---

## Design

* Is complexity justified?
* Is simpler possible?
* Does it fit surrounding patterns?

---

## Maintainability

* Can others support this later?
* Is naming understandable?
* Is hidden coupling introduced?

---

## Operational Risk

* Logging impact?
* Deployment implications?
* Failure modes?

---

# Review Comments

Common kinds of comments:

**Blocking**
Must resolve before merge.

**Non-blocking suggestion**
Improvement opportunity.

**Question**
Reviewer uncertainty.

Treat these differently.

Not every comment is a stop sign.

---

# How To Respond To Review Feedback

Good responses:

* Revise the code
* Explain reasoning respectfully
* Ask follow-ups
* Disagree when justified, calmly

"Fixed" is rarely a useful response by itself.

---

# What Review Is Not For

Review is not for:

* Personal criticism
* Showing superiority
* Rewriting everything to personal taste
* Architecture ambushes unrelated to scope

Do not smuggle redesigns into typo fixes.

---

# Approval Expectations

Default:

* At least one meaningful review
* Higher-risk changes may require more
* Author should not self-approve around safeguards

Approval means:

Reasonable confidence.
Not perfection guarantee.

---

# When To Escalate Instead Of Merge

Escalate if PR includes:

* Security concerns
* Data integrity risk
* Architectural boundary changes
* Unclear ownership conflicts

Some PRs are decisions disguised as code.

Those need discussion.

---

# Common Rookie PR Mistakes

Frequent patterns:

* PR too large
* No context in description
* Defensive response to feedback
* Mixing many concerns in one branch
* Opening PR only when "finished"

Open earlier.

Draft PRs exist for a reason.

---

# Common Reviewer Mistakes

Also common:

* Nitpicking style over substance
* Vague comments
* Drive-by approvals without reading
* Turning review into ego theater

"Looks good" on a 700-line PR is suspicious.

---

# Review Latency Norm

Do not leave teammates waiting indefinitely.

Review is part of delivery, not optional volunteer work.

If overloaded:

* acknowledge
* set expectation
* redirect if needed

---

# Special Guidance for AI/LLM Code

Review additionally for:

* Prompt behavior risks
* Schema validation
* Tool failure handling
* Hallucination guardrails
* Evaluation coverage

Model output logic deserves skepticism.

---

# Merge Readiness Checklist

Before merge:

* [ ] Tests pass
* [ ] Review comments addressed
* [ ] Risks understood
* [ ] Docs updated if needed
* [ ] Rollback path known

Then merge.
Monitor.
Breathe.

---

# Informal Review Principles

## The Reviewer Is Not The Enemy

Good reviewers reduce incidents.

---

## The Three-Question Rule

Before major criticism, ask:

* Is it wrong?
* Is it risky?
* Or is it just not how I would do it?

Only the first two may justify blocking.

---

## The Friday Rule

Deploy skepticism increases late Friday.

This is rational.

---

# Example of a Strong Review Comment

Weak:

> This seems bad.

Better:

> I may be missing context, but this introduces retry logic without timeout bounds. Could this create runaway behavior under failure?

Precision scales.

---

**Related documents**

* good_pull_request_example.md
* bad_pull_request_example.md
* branching_and_git_workflow.md
* rookie_mistakes.md
