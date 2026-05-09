from typing import Literal
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(min_length=1)


class SourceDocument(BaseModel):
    document_name: str
    file_path: str
    category: Literal["policy", "adr", "runbook", "example", "culture"] | None = None
    content_preview: str


class DocumentResponse(BaseModel):
    document_name: str
    file_path: str
    content: str


class DocumentListResponse(BaseModel):
    documents: list[str] = Field(default_factory=list)


EscalationLevel = Literal["proceed", "ask_teammate", "escalate_supervisor"]


class ChatResponse(BaseModel):
    answer: str
    escalation_level: EscalationLevel = Field(
        description="Recommended action level for the user."
    )
    escalation_reason: str = Field(
        description="Short explanation for why this escalation level was chosen."
    )
    sources: list[SourceDocument] = Field(default_factory=list)
