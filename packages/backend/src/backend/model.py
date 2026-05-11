import mlflow
from mlflow.genai import load_prompt
from dotenv import load_dotenv
from pydantic_ai import Agent

from backend.constants import MODEL_MEDIUM, MLFLOW_TRACKING_URI, PROMPTS_PATH
from backend.schemas import ChatResponse, SourceDocument

from rag.retrieval import retrieve_documents

load_dotenv()

if MLFLOW_TRACKING_URI:
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)


def load_local_prompt(filename: str) -> str:
    prompt_path = PROMPTS_PATH / filename

    if not prompt_path.exists():
        raise FileNotFoundError(f"Local fallback prompt not found: {prompt_path}")

    return prompt_path.read_text(encoding="utf-8")


def load_prompts() -> tuple[str, str]:
    try:
        system_prompt = load_prompt("prompts:/system_prompt@latest").template
        rag_prompt = load_prompt("prompts:/rag_prompt@latest").template
        return system_prompt, rag_prompt

    except Exception as e:
        print(
            "Could not load prompts from MLflow. "
            f"Falling back to local prompt files. Reason: {type(e).__name__}"
        )
        system_prompt = load_local_prompt("system_prompt.md")
        rag_prompt = load_local_prompt("rag_prompt.md")
        return system_prompt, rag_prompt


system_prompt, rag_prompt = load_prompts()

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
        escalation_level=result.output.escalation_level,
        escalation_reason=result.output.escalation_reason,
        sources=[
            SourceDocument(
                document_name=doc["document_name"],
                file_path=doc["file_path"],
                content_preview=(doc.get("content") or "")[:200],
            )
            for doc in documents
        ],
    )
