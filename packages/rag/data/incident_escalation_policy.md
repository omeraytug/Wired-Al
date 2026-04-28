# incident_escalation_policy.md

## Incident Escalation Policy — 404 Brain Not Found

**Version:** 0.1

# Purpose

Defines when and how operational or security incidents should be escalated.

---

# Severity Levels

## Sev 4 — Minor

Low impact.
Localized issue.
No customer harm.

Examples:

* Noncritical bug
* Internal tool degraded
* Single-user issue

Default: solve in team.

---

## Sev 3 — Moderate

Customer-facing degradation.
Limited impact.

Examples:

* Partial service outage
* Repeated failed deploys
* Retrieval quality collapse in production

Escalate to responsible engineer.

---

## Sev 2 — Major

Significant customer or business impact.

Examples:

* Production instability
* Data corruption risk
* Security anomaly
* Failed rollback

Escalate immediately.

---

## Sev 1 — Critical

Company-threatening event.

Examples:

* Major outage
* Credential compromise
* Sensitive data exposure
* Autonomous model action causing harm

Wake people up.

---

# Escalation Rules

Escalate early if:

* Unsure of severity
* Blast radius unknown
* Security may be involved
* You think “maybe this is serious”

That thought is often the escalation trigger.

---

# Incident Principles

1. Stabilize before optimize.
2. Contain before explain.
3. Facts before theories.
4. No blame during active incident.

---

# What To Include In Escalation

Provide:

* What happened
* Current impact
* What you observed
* What you already tried
* What risk worries you

Good escalation reduces chaos.

---

# Things You Never Wait On

Immediately escalate:

* Possible secrets leak
* Customer data exposure
* Production deletion risk
* Suspicious model/tool behavior

Minutes matter.

---

# Rookie Rule

When unsure whether to escalate:
Escalate.

False-positive escalation is usually cheaper than missed incidents.

---

# Informal Law

If someone says
“this is probably fine”
during an incident,
verify.

---

Related:
example_incident_postmortem.md
incident_lessons_learned.md
