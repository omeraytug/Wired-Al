# adr_001_why_fastapi.md

## ADR-001 Why FastAPI

Status: Accepted

## Context

Need API framework for agent endpoints and RAG service.

---

## Decision

Use FastAPI.

---

## Reasons

Chosen for:

* Python-native fit
* Pydantic validation
* Async support
* Good developer velocity
* Strong ecosystem

---

## Tradeoffs Accepted

* Not minimal as Flask
* Some framework abstraction overhead
* Async misuse can add complexity

Accepted.

---

## Alternatives Considered

Flask:
Simpler, less structure.

Django:
Too heavy for current scope.

---

## Consequences

API schemas become first-class.
Validation shifts earlier.
Good fit for agent interfaces.

---

## Informal Note

We chose boring-good over novel-interesting.
