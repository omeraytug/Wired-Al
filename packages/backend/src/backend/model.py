from dotenv import load_dotenv
from pydantic_ai import Agent

from backend.prompts import SYSTEM_PROMPT, RAG_PROMPT_TEMPLATE
from backend.constants import MODEL_MEDIUM
from backend.schemas import ChatResponse, SourceDocument

from rag.retrieval import retrieve_documents

load_dotenv()

wired_al_agent = Agent(
    model=MODEL_MEDIUM, system_prompt=SYSTEM_PROMPT, output_type=ChatResponse
)


async def chat(question: str) -> ChatResponse:
    documents = retrieve_documents(question)

    context = "\n\n".join(
        f"Document: {doc['document_name']}\nContent:\n{doc['content']}"
        for doc in documents
    )

    prompt = RAG_PROMPT_TEMPLATE.format(question=question, context=context)

    result = await wired_al_agent.run(prompt)

    return ChatResponse(
        answer=result.output.answer,
        sources=[
            SourceDocument(
                document_name=doc["document_name"],
                file_path=doc["file_path"],
                content_preview=(doc.get("content") or "")[:200],
            )
            for doc in documents
        ],
    )


@wired_al_agent.tool_plain
def search_knowledge_base(query: str):
    return str(retrieve_documents(query))
