FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

# Workspace + package metadata
COPY pyproject.toml uv.lock ./
COPY packages/backend/pyproject.toml packages/backend/pyproject.toml
COPY packages/frontend/pyproject.toml packages/frontend/pyproject.toml
COPY packages/rag/pyproject.toml packages/rag/pyproject.toml

# Frontend source
COPY packages/frontend/src/frontend packages/frontend/src/frontend

RUN uv sync --frozen --no-dev --package frontend

WORKDIR /app/packages/frontend/src/frontend
CMD ["uv", "run", "--package", "frontend", "streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]