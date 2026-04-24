from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/ask")
async def ask():
    return {
        "status": "stub",
        "endpoint": "/ask",
        "detail": "Not wired to RAG; swap to Person 1 models + service when ready.",
    }


@app.post("/ingest")
async def ingest():
    return {
        "status": "stub",
        "endpoint": "/ingest",
        "detail": "Not wired to vector ingest; swap to pipeline when ready.",
    }
