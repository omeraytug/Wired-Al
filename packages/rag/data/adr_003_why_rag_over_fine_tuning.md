# adr_003_why_rag_over_fine_tuning.md

## ADR-003: Why We Chose RAG Over Fine-Tuning

**Status:** Accepted  
**Date:** 2026-05-09  
**Decision owners:** 404 Brain Not Found engineering team  
**Related system:** Wired Al onboarding copilot

---

# Context

Wired Al is an AI onboarding copilot for interns and junior engineers.
It answers questions about company knowledge, engineering workflow, cultural expectations and escalation decisions.

The system needs access to information such as:

* onboarding material
* code review guidelines
* engineering handbook content
* architectural decision records
* runbooks
* incident and escalation policies
* examples of good and bad pull requests
* cultural expectations for interns

This information changes over time.
Policies are updated, architecture decisions are added, workflows evolve and new examples are created.

The team considered two main approaches:

1. Retrieval-Augmented Generation, also called RAG.
2. Fine-tuning a language model on company documents.

---

# Decision

We chose RAG over fine-tuning for Wired Al.

The system should retrieve relevant company documents at answer time and generate responses grounded in that retrieved context.

Fine-tuning is not used as the primary method for storing company knowledge.

---

# Why RAG Fits This Project

## 1. Company knowledge changes often

Wired Al depends on documents that may change during the project.
Examples include onboarding checklists, runbooks, escalation policies and ADRs.

With RAG, we can update or add documents and re-run ingestion.
The model can then retrieve the new content without retraining the model itself.

With fine-tuning, updated knowledge usually requires a new training process or dataset preparation step.
That is too heavy for this project and too slow for a realistic onboarding knowledge base.

---

## 2. We need source-grounded answers

Wired Al should show which documents influenced an answer.
This is important because interns should be able to verify advice against company documentation.

RAG supports this directly by returning source documents with the generated answer.

Fine-tuning does not naturally provide source attribution.
A fine-tuned model may answer from learned patterns, but it cannot reliably explain which internal document the answer came from unless retrieval or citation logic is added separately.

---

## 3. Maintainability is more important than model specialization

The goal of Wired Al is not to create a model with a unique writing style.
The goal is to provide useful, current and grounded onboarding support.

RAG keeps knowledge in editable documents.
This makes the system easier to maintain:

* non-model files contain the source of truth
* documents can be reviewed in pull requests
* changes can be traced in Git
* bad or outdated information can be fixed without model retraining

Fine-tuning would make knowledge harder to inspect because some behaviour would be stored inside model weights.

---

## 4. The dataset is small and controlled

The current knowledge base is made of a limited number of Markdown documents.
That is a good fit for retrieval.

Fine-tuning usually makes more sense when there is a larger and carefully prepared dataset, or when the goal is to teach a model a stable style, format or task pattern.

For Wired Al, the stronger need is document access, not model retraining.

---

## 5. RAG is easier to evaluate for this use case

The team can evaluate whether:

* the answer is relevant to the user question
* the retrieved sources are relevant
* expected source documents are returned
* the answer is grounded in the knowledge base

This matches the LLMOps goals of the project.
It also fits MLflow evaluation better because retrieval relevance and answer correctness can be evaluated separately.

With fine-tuning, it would be harder to separate whether a good or bad answer came from training data, prompt design or model behaviour.

---

# Alternatives Considered

## Option A: Fine-tune a model on all company documents

Rejected.

Reasons:

* too much operational overhead for the project scope
* harder to update when documents change
* weak source traceability
* higher risk of stale knowledge
* harder to debug incorrect answers

Fine-tuning may still be useful in the future for tone, formatting or classification behaviour, but not as the main knowledge mechanism.

---

## Option B: Prompt-only chatbot without retrieval

Rejected.

Reasons:

* limited context window
* higher hallucination risk
* difficult to keep answers aligned with changing documentation
* no reliable source list
* poor fit for onboarding questions that depend on specific internal policies

---

## Option C: RAG with structured sources

Accepted.

Reasons:

* keeps company knowledge outside the model
* supports source display
* easier to update and maintain
* easier to evaluate
* fits the project requirement for a document-grounded AI assistant
* works well with FastAPI, LanceDB, MLflow and the current monorepo structure

---

# Consequences

## Positive Consequences

* Knowledge can be updated by editing Markdown documents.
* Answers can include source documents.
* The system is easier to debug.
* Evaluation can check both answer quality and retrieval quality.
* The architecture is easier to explain in the project presentation.
* The team can improve retrieval without changing the LLM.

---

## Negative Consequences

* Retrieval quality becomes critical.
* Bad chunking or missing ingestion can cause weak answers.
* The vector database must be built and available at runtime.
* The system needs clear behaviour when no relevant document is found.
* The answer quality depends on both retrieval and generation.

---

# Implementation Notes

The chosen flow is:

1. User asks a question.
2. Backend receives the question through FastAPI.
3. RAG retrieves relevant documents from LanceDB.
4. The retrieved context is inserted into the prompt.
5. The model generates a structured answer.
6. The API returns the answer and source documents.
7. Evaluation checks answer quality and retrieval relevance.

The system should not answer as if unsupported information is known.
If the retrieved context is insufficient, Wired Al should say that the knowledge base does not contain enough information.

---

# When Fine-Tuning Might Be Reconsidered

Fine-tuning may be reconsidered later if the team needs:

* a highly specific and stable response format
* classification behaviour that is hard to prompt reliably
* a model that consistently follows the company tone
* lower latency for repeated known tasks
* enough high-quality training examples to justify the cost

Even then, RAG would probably remain the source of factual company knowledge.
Fine-tuning would support behaviour, not replace retrieval.

---

# Final Decision

RAG is the correct primary architecture for Wired Al because the system depends on changing company knowledge, source-grounded answers and maintainable documentation.

Fine-tuning is not rejected as a technology, but it is not the right mechanism for storing onboarding knowledge in this project.
