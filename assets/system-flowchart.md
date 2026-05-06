# System flowchart

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 50, "rankSpacing": 70}} }%%
flowchart TD
  U["User"] --> ST["Streamlit UI<br/>packages/frontend/src/frontend/app.py"]
  ST --> API["FastAPI backend<br/>packages/backend/src/backend/api.py"]

  API --> CHAT["chat(question)<br/>packages/backend/src/backend/model.py"]

  CHAT --> RETRIEVE["retrieve_documents(question, k=3)<br/>packages/rag/src/rag/retrieval.py"]
  RETRIEVE --> LDB["LanceDB Vector DB<br/>path: VECTOR_DB_PATH"]
  LDB --> TOPK["Top-k matches<br/>table: articles"]

  TOPK --> CONTEXT["Build context string<br/>Doc name + content"]
  CONTEXT --> PROMPT["Fill RAG_PROMPT_TEMPLATE<br/>packages/backend/src/backend/prompts.py"]
  PROMPT --> AGENT["pydantic_ai.Agent.run(prompt)<br/>wired agent: wired_al_agent"]

  AGENT --> RESP["Build ChatResponse<br/>answer + source previews"]
  RESP --> API
  API --> ST
  ST --> U

  %% Ingestion path (not invoked by /ask)
  subgraph OFFLINE["Offline setup (knowledge base creation)"]
    MD["Markdown docs in DATA_PATH"]
    ING["ingest_docs()<br/>packages/rag/src/rag/ingestion.py"]
    MD --> ING -->|table.add(...)| LDB
  end

  %% Embedding happens via LanceDB schema
  subgraph EMBED["Embeddings (implicit)"]
    SCHEMA["Article schema<br/>packages/rag/src/rag/data_models.py<br/>content = SourceField()<br/>embedding = VectorField()"]
    SCHEMA --> LDB
  end
```

