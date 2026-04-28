# example_design_doc.md

## Mini Design Spec Example

Problem:
Interns repeatedly ask similar onboarding questions.

Proposal:
Add retrieval-backed onboarding assistant with escalation guidance.

Scope:

* answer questions over knowledge base
* provide escalation suggestions
* log unanswered questions

Out of scope:

* autonomous task execution
* ticket creation

Risks:

* weak retrieval relevance
* hallucination risk
* stale documentation

Mitigations:

* evaluation
* fallback responses
* document ownership

Decision note:
Start narrow.
Expand after evidence.
