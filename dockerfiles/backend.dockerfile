FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

# Copy workspace metadata first for better layer caching
COPY pyproject.toml uv.lock ./
COPY packages/backend/pyproject.toml packages/backend/pyproject.toml
COPY packages/frontend/pyproject.toml packages/frontend/pyproject.toml
COPY packages/rag/pyproject.toml packages/rag/pyproject.toml

# Copy source code needed at runtime
COPY packages/backend/src/backend packages/backend/src/backend
COPY packages/rag/src/rag packages/rag/src/rag
COPY packages/rag/knowledge_base packages/rag/knowledge_base

# Sync only backend project (and its workspace deps like rag)
RUN uv sync --frozen --no-dev --package backend

WORKDIR /app/packages/backend/src/backend
CMD ["uv", "run", "--package", "backend", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]