# what_good_interns_do.md

## What Good Interns Do — 404 Brain Not Found

**Version:** 0.1  
**Purpose:** Describe the behaviours that help interns and junior engineers succeed at 404 Brain Not Found.

---

# Why This Document Exists

Good interns are not expected to know everything.
They are expected to learn in a visible, structured and responsible way.

At 404 Brain Not Found, strong interns make progress by combining curiosity, communication and engineering discipline.

This document explains what good intern behaviour looks like in practice.

---

# Core Principle

A good intern does not try to appear senior.
A good intern works in a way that makes their thinking easy to review, support and trust.

That means:

* asking clear questions
* documenting decisions
* making small changes
* communicating blockers early
* learning from review feedback
* respecting team workflows

---

# What Good Interns Do

## 1. They clarify the task before building

Before writing code, good interns make sure they understand:

* the user problem
* the expected outcome
* the scope of the task
* where the change belongs in the system
* how the work will be tested

They do not need a perfect plan, but they should know what they are trying to achieve.

A good starting question is:

> What should be true when this task is done?

---

## 2. They work in small, reviewable steps

Strong interns avoid large, unfocused pull requests.

A good intern prefers:

* one issue per branch
* one clear purpose per pull request
* small commits with meaningful messages
* code that is easy for a reviewer to understand

Small work is easier to review, easier to fix and easier to merge.

---

## 3. They communicate blockers early

Getting stuck is normal.
Staying stuck silently is the problem.

Good interns try to solve a problem independently first, but they do not disappear for hours without giving context.

A useful rule:

* If blocked for more than 30 minutes, write down what you tried.
* If still blocked, ask a teammate or supervisor with that context.

Good blocker messages include:

* what you tried
* what you expected to happen
* what actually happened
* the exact error message, if there is one
* what file, endpoint or command is involved

---

## 4. They ask specific questions

Weak question:

> It does not work. What should I do?

Better question:

> I expected `/ask` to return an answer with sources, but the backend returns a 500 error. I checked the API URL and the request body. The traceback points to LanceDB table lookup. Could this mean ingestion has not run?

Good interns make it easy for others to help them.

---

## 5. They make their thinking visible

Good interns do not only show the final code.
They also show the reasoning behind decisions.

Examples:

* explaining why a branch was created
* writing a short PR description
* linking the issue being solved
* documenting tradeoffs in an ADR when relevant
* leaving comments only where the code is not self-explanatory

Visible reasoning builds trust.

---

## 6. They respect the team workflow

Good interns follow the agreed way of working:

* no direct commits to main
* feature branches for changes
* pull requests before merge
* at least one reviewer
* conventional commit messages
* update the issue when the task changes status

This is not bureaucracy.
It protects the team from confusion, lost work and unstable demos.

---

## 7. They test their own work before asking for review

Before opening a pull request, good interns run the smallest relevant test.

Depending on the change, this can mean:

* checking that the app starts
* calling `/health`
* sending one request to `/ask`
* running ingestion after changing RAG documents
* running one evaluation smoke test
* checking that the frontend can reach the backend

A reviewer should not be the first person to run the code.

---

## 8. They learn from code review

Good interns do not treat review comments as personal criticism.
Review is part of engineering.

A good response to feedback is:

* read the comment carefully
* ask if the feedback is unclear
* make the change or explain the tradeoff
* avoid repeating the same issue in the next PR

The goal is not to “win” the review.
The goal is to improve the system and the developer.

---

## 9. They know when to escalate

Good interns do not escalate every small problem.
They also do not hide high-risk problems.

Use this guidance:

### Proceed yourself

Proceed when:

* the change is low risk
* the task is clear
* you know how to test it
* failure would be easy to revert

### Ask a teammate first

Ask a teammate when:

* you are blocked after a serious attempt
* you are unsure which file or package owns the problem
* the issue affects another person's work
* the change may expand beyond the original scope

### Escalate to supervisor

Escalate when:

* production or demo stability is at risk
* secrets may have been committed
* a merge may break main
* requirements are unclear and affect project direction
* the team cannot agree on an architectural decision

Escalation is not failure.
It is risk management.

---

# Common Rookie Mistakes to Avoid

Good interns actively avoid these patterns:

* working too long without feedback
* opening huge pull requests
* changing unrelated files in the same branch
* hiding uncertainty
* asking vague questions
* skipping tests before review
* copying code without understanding it
* using LLM-generated code without checking it
* treating documentation as optional
* ignoring team norms because “it works locally”

---

# What Supervisors Notice

Supervisors do not only notice technical output.
They notice how the intern works.

Strong signals:

* clear communication
* honest status updates
* thoughtful questions
* small and safe changes
* willingness to learn
* respect for the codebase
* ability to explain tradeoffs

Weak signals:

* silence when blocked
* unexplained changes
* repeated merge conflicts from poor branching
* overconfidence without tests
* lack of ownership

---

# Practical Checklist Before Asking for Review

Before asking someone to review your work, check:

- [ ] The branch has one clear purpose.
- [ ] The code runs locally.
- [ ] The relevant endpoint, UI flow or script has been tested.
- [ ] The PR description explains what changed.
- [ ] The issue has been updated if needed.
- [ ] Any known limitation is written clearly.
- [ ] No secrets, local databases or generated cache files are included.

---

# Summary

Good interns do not need to know everything in advance.
They succeed by making their work clear, small, testable and easy to support.

At 404 Brain Not Found, a strong intern communicates early, follows team norms, learns from review and escalates risk before it becomes damage.
