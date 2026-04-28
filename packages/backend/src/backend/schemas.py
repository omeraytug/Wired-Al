from typing import Literal
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(min_length=1)


class SourceDocument(BaseModel):
    document_name: str
    file_path: str
    category: Literal["policy", "adr", "runbook", "example", "culture"] | None = None
    content_preview: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[SourceDocument] = Field(default_factory=list)
