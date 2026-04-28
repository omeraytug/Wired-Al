from fastapi import FastAPI
from backend.agent.model import chat
from backend.schemas import ChatResponse, ChatRequest

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/ask")
async def ask(query: ChatRequest)-> ChatResponse:
    result = await chat(query.prompt)

    return result


@app.post("/ingest")
async def ingest():
    return {
        "status": "stub",
        "endpoint": "/ingest",
        "detail": "Not wired to vector ingest; swap to pipeline when ready.",
    }
