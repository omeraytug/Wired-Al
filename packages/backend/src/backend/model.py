import mlflow
from mlflow.genai import load_prompt
from dotenv import load_dotenv
from pydantic_ai import Agent

from backend.constants import MODEL_MEDIUM, MLFLOW_DB_PATH
from backend.schemas import ChatResponse, SourceDocument

from rag.retrieval import retrieve_documents

load_dotenv()
mlflow.set_tracking_uri(MLFLOW_DB_PATH)

system_prompt = load_prompt("prompts:/system_prompt/1").template
rag_prompt = load_prompt("prompts:/rag_prompt/1").template

wired_al_agent = Agent(
    model=MODEL_MEDIUM, system_prompt=system_prompt, output_type=ChatResponse
)


async def chat(question: str) -> ChatResponse:
    documents = retrieve_documents(question)

    context = "\n\n".join(
        f"Document: {doc['document_name']}\nContent:\n{doc['content']}"
        for doc in documents
    )

    prompt = rag_prompt.format(question=question, context=context)

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
