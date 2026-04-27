# adr_002_why_lancedb.md

## ADR-002 Why LanceDB

Status: Accepted

## Context

Need vector store for RAG retrieval.

---

## Decision

Use LanceDB.

---

## Reasons

Selected for:

* Good Python ergonomics
* Local-first simplicity
* Suitable for project scale
* Vector + tabular model appealing
* Easy experimentation

---

## Tradeoffs Accepted

Not highest-scale option.
Some production ecosystems more mature elsewhere.

Accepted for current needs.

---

## Alternatives Considered

FAISS:
Strong, but less database-like workflow.

Managed vector DB:
Useful later, heavier now.

---

## Consequences

Fast iteration favored.
Can revisit later.

---

## Informal Note

Optimize for learning leverage before hyperscale fantasies.
