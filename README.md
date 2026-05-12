
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-API-brightgreen" alt="FastAPI">
  <img src="https://img.shields.io/badge/Streamlit-Frontend-red" alt="Streamlit">
  <img src="https://img.shields.io/badge/MLflow-LLMOps-orange" alt="MLflow">
  <img src="https://img.shields.io/badge/RAG-Enabled-purple" alt="RAG">
  <img src="https://img.shields.io/badge/Docker-Ready-blue" alt="Docker">
  <img src="https://img.shields.io/badge/Azure-Deployed-blue" alt="Azure">
</p>



<div align="center">
<img src="design/wiredal-screen.png", width="800">
</div>

---


Wired Al is an AI onboarding copilot for interns and junior engineers.  
It combines Retrieval-Augmented Generation (RAG), mentor-style guidance, escalation support, and LLMOps practices to help new developers become productive faster in a fictional engineering organization: **404 Brain Not Found**.

## Overview

Wired Al is designed to answer questions about company knowledge, technical decisions, workflows, team culture, and onboarding expectations.

Instead of acting as a simple document chatbot, the system provides:

- **Knowledge retrieval** from internal company documents
- **Mentor-style coaching** for junior developers
- **Escalation guidance** for risky or uncertain situations
- **Source-backed answers** from the project knowledge base
- **LLMOps support** through MLflow prompt versioning and evaluation

Example questions:

```text
How do code reviews work here?
Why did we choose FastAPI?
When should an incident be escalated?
Should I merge a large PR late on Friday?
````

## Core Features

### RAG-based Knowledge Retrieval

The assistant retrieves relevant information from a curated internal knowledge base containing documents such as:

* onboarding material
* engineering handbook
* code review guidelines
* architectural decision records
* deployment runbooks
* incident escalation policy
* examples of good and bad pull requests
* team communication norms

### Escalation Guidance

<div align="center">
<img src="design/escalation-screen.png", width="400">
</div>

Wired Al can classify a situation into one of three escalation levels:

```text
proceed
ask_teammate
escalate_supervisor
```

This helps junior engineers decide whether they can continue independently, ask a teammate, or involve a supervisor.

### MLflow Integration

The project uses MLflow for:

* prompt registry
* prompt versioning
* LLM-based evaluation
* tracing/evaluation of the chat pipeline

<div align="center">
<img src="design/eval-screen.png", width="400">
</div>

Evaluation cases are stored as structured test data and are used to check factual correctness, query relevance, and retrieval relevance.

## Tech Stack

| Area                         | Technology              |
| ---------------------------- | ----------------------- |
| Backend                      | FastAPI                 |
| Frontend                     | Streamlit               |
| RAG / Vector DB              | LanceDB                 |
| LLM agent                    | PydanticAI              |
| Prompt registry / evaluation | MLflow                  |
| Package management           | uv                      |
| Deployment                   | Docker / Docker Compose |
| Language                     | Python 3.13+            |

## Project Structure

```text
.
├── docker-compose.yaml
├── dockerfiles/
│   ├── backend.dockerfile
│   └── frontend.dockerfile
├── docs/
│   └── way_of_working.md
├── packages/
│   ├── backend/
│   │   └── src/backend/
│   │       ├── api.py
│   │       ├── model.py
│   │       ├── schemas.py
│   │       ├── constants.py
│   │       └── prompt_registry.py
│   ├── frontend/
│   │   └── src/frontend/app.py
│   ├── rag/
│   │   ├── data/
│   │   └── src/rag/
│   │       ├── ingestion.py
│   │       ├── retrieval.py
│   │       └── data_models.py
│   └── evaluation/
│       ├── data/eval_cases.json
│       └── src/evaluation/run_eval.py
└── pyproject.toml
```

## API Endpoints

| Method | Endpoint                     | Description                               |
| ------ | ---------------------------- | ----------------------------------------- |
| `GET`  | `/health`                    | Health check                              |
| `POST` | `/ask`                       | Ask the onboarding copilot a question     |
| `GET`  | `/documents`                 | List indexed knowledge base documents     |
| `GET`  | `/documents/{document_name}` | Read one document from the knowledge base |
| `POST` | `/ingest`                    | Ingestion endpoint placeholder            |

Example request:

```bash
curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "How do code reviews work here?"}'
```

## Local Development

### 1. Install dependencies

```bash
uv sync
```

### 2. Configure environment variables

Create a `.env` file in the project root.

Example:

```env
MLFLOW_TRACKING_URI=http://localhost:5001
MLFLOW_BACKEND_STORE_URI=postgresql://user:password@host:5432/mlflow
OPENROUTER_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
COHERE_API_KEY=your_key_here
```

Do not commit real secrets.

### 3. Register prompts in MLflow

```bash
uv run --package backend python -m backend.prompt_registry
```

### 4. Ingest knowledge base documents

```bash
uv run --package rag python -m rag.ingestion
```

### 5. Start the backend

```bash
uv run --package backend uvicorn backend.api:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

### 6. Start the frontend

```bash
uv run --package frontend streamlit run packages/frontend/src/frontend/app.py
```

Frontend runs on:

```text
http://localhost:8501
```

## Running with Docker Compose

Start the full stack:

```bash
docker compose up --build
```

Services:

| Service  | URL                     |
| -------- | ----------------------- |
| Backend  | `http://localhost:8000` |
| Frontend | `http://localhost:8501` |
| MLflow   | `http://localhost:5001` |

Inside Docker Compose, the frontend connects to the backend using:

```env
API_URL=http://backend:8000
```

## Evaluation

Run the MLflow evaluation script:

```bash
uv run --package evaluation python -m evaluation.run_eval
```

The evaluation uses predefined test cases from:

```text
packages/evaluation/data/eval_cases.json
```

The current evaluation checks questions related to:

* code reviews
* architectural decisions
* incident escalation
* intern mistakes
* RAG vs fine-tuning

## Way of Working

The team follows a lightweight professional workflow:

* feature branches only
* pull requests before merge
* no direct commits to `main`
* conventional commit messages
* at least one reviewer per PR
* daily check-ins
* Discord communication
* GitHub issues and project board when relevant

Example branch names:

```text
feature/rag-ingestion
feature/streamlit-ui
fix/frontend-error-handling
docs/readme
```

Example commit messages:

```text
feat(api): add chat endpoint
fix(rag): handle missing vector table
docs(readme): update setup instructions
```

## Definition of Done

A task is considered done when:

* code is merged
* relevant functionality is tested
* the issue or task is updated
* documentation is updated when needed

## About the Project

Wired Al was built as an LLMOps project to demonstrate how modern AI applications can combine:

* practical backend engineering
* RAG architecture
* prompt management
* evaluation
* frontend integration
* containerized deployment
* team-based development workflow

The project is intentionally built around a fictional startup so the knowledge base, culture, policies, and onboarding material can be realistic while remaining controlled for demonstration purposes.


## Contributors

<a href="https://github.com/hazajijan-prog">
<img src="https://avatars.githubusercontent.com/hazajijan-prog" width="50" height="50" style="border-radius: 30%;" alt="Haza">
</a>
<a href="https://github.com/omeraytug">
<img src="https://avatars.githubusercontent.com/omeraytug" width="50" height="50" style="border-radius: 30%;" alt="Ömer">
</a>
<a href="https://github.com/pytt156">
<img src="https://avatars.githubusercontent.com/pytt156" width="50" height="50" style="border-radius: 30%;" alt="Daniela">
</a>
