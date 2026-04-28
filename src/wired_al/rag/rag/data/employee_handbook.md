# employee_handbook.md

## Employee Handbook — 404 Brain Not Found

**Version:** 0.1
**Audience:** Interns, junior engineers, and new team members
**Purpose:** Provide a lightweight but realistic internal handbook for onboarding and daily collaboration.

---

# Welcome

Welcome to **404 Brain Not Found**.

We build practical AI systems with a bias toward experimentation, reliability, and thoughtful engineering.

As a small technical organization, we expect everyone — including interns — to contribute meaningfully, ask questions early, and improve systems as they learn.

This handbook explains how we work, what we expect, and how to navigate the organization.

---

# Our Principles

We try to optimize for:

1. **Clarity over complexity**
   Prefer understandable systems over clever ones.

2. **Ship small, improve often**
   Iteration beats overdesign.

3. **Evidence over opinion**
   Use data, experiments and reasoning.

4. **Escalate risks early**
   Bad surprises are worse than early warnings.

5. **Documentation is part of the work**
   If it is not documented, it probably does not scale.

---

# Team Roles

## Intern / Junior Engineer

Expected to:

* Complete onboarding tasks
* Ask questions when blocked
* Contribute code, documentation or analysis
* Participate in reviews
* Surface uncertainty early
* Learn team norms and workflows

You are not expected to know everything.
You are expected to reason, communicate and learn.

---

## Engineer

Responsible for:

* Delivery and implementation
* Code reviews
* Technical guidance
* Maintaining quality standards
* Supporting onboarding

---

## Tech Lead

Responsible for:

* Architecture decisions
* Technical prioritization
* Risk escalation
* Mentoring
* Final approval for major changes

---

# How We Work

## Default Work Pattern

Most work follows:

* Ticket or task definition
* Clarify requirements
* Implement in small increments
* Open pull request early
* Iterate through feedback
* Merge when approved

Work in visible increments.
Avoid long-lived hidden work.

---

## Ownership

If you pick up a task, you own:

* Understanding the problem
* Communicating blockers
* Asking for help when needed
* Leaving the work in a better state

Ownership does not mean solving everything alone.

---

# Communication Channels

## Chat (Slack/Teams)

Used for:

* Quick questions
* Coordination
* Async updates
* Lightweight discussions

Good messages include:

* Context
* What you tried
* Specific ask

Example:

Bad:

> Deploy broken, help.

Better:

> Staging deploy failed after config change. Checked logs and rollback notes, suspect env variable mismatch. Can someone sanity-check?

---

## Meetings

Recurring meetings may include:

* Daily check-in
* Planning
* Demo/review
* Retrospective

Come prepared.
Short meetings should stay short.

---

## Documentation

Use documentation for:

* Decisions
* Runbooks
* Architecture notes
* Repeated questions

Don’t bury operational knowledge in chat threads.

---

# Expectations for New Team Members

## First 30 Days

You should aim to:

* Understand system basics
* Ship at least one small contribution
* Participate in a code review
* Learn escalation paths
* Become productive in core tools

Progress matters more than speed.

---

## Asking Questions

Ask early when:

* You are blocked more than ~30–60 minutes
* You might introduce risk
* Requirements are ambiguous
* A decision affects others

Before asking:

1. Read relevant documentation
2. Try a reasonable approach
3. Bring your reasoning with the question

---

# Feedback Culture

Feedback is expected.

Review feedback critiques work, not people.

Good responses to feedback:

* Ask clarifying questions
* Revise thoughtfully
* Challenge respectfully if needed

Defensiveness slows learning.

---

# Escalation Guidance

Use this model:

## Proceed Yourself (Green)

Examples:

* Small refactors
* Documentation improvements
* Minor bug fixes
* Non-risky experiments

---

## Ask Teammate First (Yellow)

Examples:

* Unclear design choices
* Shared code ownership areas
* Changes affecting interfaces
* Suspicious test failures

---

## Escalate to Lead (Red)

Examples:

* Security concerns
* Production risks
* Incident indicators
* Architectural changes
* Data integrity uncertainty

Escalating early is considered good judgment.

---

# Working Agreements

We generally prefer:

* Small PRs over massive PRs
* Explicit assumptions over hidden assumptions
* Reproducible fixes over manual heroics
* Calm incident handling over improvisation

Avoid:

* Silent blockers
* Scope creep without discussion
* “Works on my machine” handoffs
* Merging unreviewed risky code

---

# Time and Availability

Respect focus time.

Not every message requires immediate response.

Use urgency intentionally.

If something is urgent, say why.

---

# Tooling Expectations

You are expected to learn and use:

* Git and pull requests
* Issue tracking
* Local development setup
* Testing basics
* Documentation conventions

Advanced expertise is not assumed on day one.

---

# What Good Interns Tend To Do

Patterns we often value:

* Ask thoughtful questions
* Document what they learn
* Improve small things proactively
* Accept feedback quickly
* Surface risks early
* Leave breadcrumbs for others

Signal reliability before trying to signal brilliance.

---

# Common Anti-Patterns

Watch for these:

* Waiting too long before asking for help
* Overengineering simple tasks
* Treating review comments as personal criticism
* Solving symptoms instead of root causes
* Assuming undocumented norms

These are common, fixable mistakes.

---

# Decision Making

Many decisions are reversible.

For reversible decisions:

* decide fast
* test
* adjust

For hard-to-reverse decisions:

* slow down
* gather evidence
* involve others

---

# Security and Confidentiality

Basic rules:

* Never commit secrets
* Use approved access paths
* Ask before using production data
* Report accidental exposure immediately

Security mistakes hidden become incidents.

---

# When Unsure

Default sequence:

1. Check documentation
2. Check examples
3. Ask teammate
4. Escalate if risk exists

Do not stay stuck alone.

---

# Employment Basics

## Working Hours

Standard expectation is roughly 40 hours per week.

Core collaboration hours are normally:

* 09:00–15:00 available for meetings and collaboration
* Flexible time outside this is common

We optimize for outcomes, not performative online presence.

---

## Remote and Hybrid Work

Hybrid work is normal.

Default expectation:

* Be reachable during core hours
* Keep calendars updated
* Communicate when working asynchronously

Remote does not mean invisible.

---

## Lunch and Breaks

Take lunch.

Recommended lunch break:

* 45–60 minutes

Short breaks are normal and encouraged.

We strongly encourage food before making production decisions.

Historical evidence supports this.

---

## Sick Leave

If sick:

* Notify your team lead or team channel early
* Do not work through illness unless genuinely optional and light
* Recovery outranks performative availability

---

## Vacation

Vacation should be coordinated early and documented.

Avoid disappearing with sole ownership of critical work.

If only one person understands a system before vacation, that is a systems problem.

---

# Office Conduct

## Shared Spaces

Leave shared spaces usable.

This includes:

* Clean up after meals
* Label food if storing it
* Do not occupy meeting rooms as private offices all day

If you make the last coffee and do not start a new pot, consequences may be mostly social.

---

## Smoking and Vaping

Only in designated areas.

Never near entrances, ventilation or outdoor collaboration areas.

---

## Noise and Focus

Use judgment with interruptions.

When someone is visibly in deep focus, prefer async questions unless urgent.

---

## Office Cat Policy

If the office cat occupies your chair, that chair may be considered temporarily reassigned.

---

# Information Handling

## Information Classification

We use four practical classes:

### Public

Safe to share externally.

### Internal

Default internal material.

### Confidential

Restricted to relevant teams.

### Restricted

Sensitive systems, credentials, incident data or regulated information.

When unsure, classify upward.

---

## AI Tool Usage

Do not paste confidential or restricted data into external AI systems unless explicitly approved.

Questions about this should be escalated.

---

# Acceptable Security Practices

Expected:

* Lock devices when away
* Use approved password management
* Never share credentials
* Never commit secrets
* Use least privilege access

Security incidents hidden tend to grow.

---

# Benefits and Team Culture

Typical cultural norms may include:

* Team lunches
* Demo Fridays
* Learning sessions
* Pairing hours
* Conference or study budget where applicable

First Friday demo failures are considered a rite of passage.

---

# Informal Internal Principles

## The Two-Coffee Rule

Do not escalate architecture debates before at least two people have had coffee.

---

## The Rubber Duck Clause

Before interrupting a senior engineer, explain the problem once to a duck, plant or empty terminal.

---

## The 404 Principle

Confusion is not failure.

It is a documented state.

---

# Final Note

We do not expect perfect decisions.

We expect thoughtful decisions, visible reasoning and steady improvement.

That is how people grow here.

---

**Related documents:**

* onboarding_checklist.md
* engineering_handbook.md
* code_review_guidelines.md
* incident_escalation_policy.md
* rookie_mistakes.md
* what_good_interns_do.md
