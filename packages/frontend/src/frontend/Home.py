import streamlit as st
import httpx
import os
from pathlib import Path

ASSETS = Path(__file__).resolve().parent / "assets"

API_URL = os.getenv("API_URL", "http://localhost:8000")

ESCALATION_LABELS = {
    "proceed": "🟢 Proceed yourself",
    "ask_teammate": "🟡 Ask teammate first",
    "escalate_supervisor": "🔴 Escalate to supervisor",
}


def layout():
    st.set_page_config(
        page_title="WIRED-AL", page_icon=str(ASSETS / "favicon-96x96.png")
    )

    with st.sidebar:
        st.image(str(ASSETS / "logo-dark.png"))

    st.markdown("# Wired-Al")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hi! I am your onboarding copilot. Ask me anything about onboarding.",
            }
        ]


    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    suggested_questions = [
        "How do code reviews work here?",
        "Why did we choose FastAPI?",
        "When should an incident be escalated?"]
    
    cols = st.columns(2)
    
    for index, question in enumerate(suggested_questions):
        with cols[index % 2]:
            if st.button(question, use_container_width=True):
                st.session_state.pending_question = question

    user_question = st.session_state.pop("pending_question", None)

    if user_question is None:
        user_question = st.chat_input("Ask a question")

    if user_question:
        st.session_state.messages.append({"role": "user", "content": user_question})

        with st.chat_message("user"):
            st.markdown(user_question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = httpx.post(
                        f"{API_URL}/ask",
                        json={"question": user_question},
                        timeout=120,
                    )
                    response.raise_for_status()
                    data = response.json()

                    answer = data.get("answer", "I could not find an answer.")
                    sources = data.get("sources", [])
                    escalation_level = data.get("escalation_level")
                    escalation_reason = data.get("escalation_reason")

                    st.markdown(answer)

                    render_escalation(escalation_level, escalation_reason)
                    render_sources(sources)

                    assistant_message = build_assistant_message(
                        answer=answer,
                        escalation_level=escalation_level,
                        escalation_reason=escalation_reason,
                    )

                    st.session_state.messages.append(
                        {"role": "assistant", "content": assistant_message}
                    )


                except httpx.RequestError as e:
                    error_message = (
                        f"Could not connect to the backend API on url: {API_URL}. "
                        f"Original error: {e}"
                    )
                    st.error(error_message)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": error_message}
                    )

                except httpx.HTTPStatusError as e:
                    error_message = f"The backend returned {e.response.status_code}: {e.response.text}"
                    st.error(error_message)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": error_message}
                    )
                    
                    
def render_escalation(
    escalation_level: str | None,
    escalation_reason: str | None,
) -> None:
    if not escalation_level and not escalation_reason:
        return

    label = ESCALATION_LABELS.get(escalation_level, escalation_level or "Unknown")

    st.markdown(
        f"""
        <div style="
            border: 1px solid #3b4a40;
            background: #171d18;
            border-radius: 12px;
            padding: 0.9rem 1rem;
            margin: 0.8rem 0;
        ">
            <strong>{label}</strong><br>
            <span style="color: #a9b8aa;">{escalation_reason or ""}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sources(sources: list[dict]) -> None:
    if not sources:
        return

    with st.expander("Sources"):
        for source in sources:
            document_name = source.get("document_name", "Unknown document")
            content_preview = source.get("content_preview", "")

            clean_preview = (
                content_preview.replace("#", "")
                .replace("\n", " ")
                .replace(document_name, "")
                .strip()
            )

            st.markdown(f"**{format_document_name(document_name)}**")
            st.caption(document_name)

            if clean_preview:
                st.markdown(clean_preview[:180] + "...")

            st.divider()


def build_assistant_message(
    answer: str,
    escalation_level: str | None,
    escalation_reason: str | None,
) -> str:
    assistant_message = answer

    if escalation_level:
        label = ESCALATION_LABELS.get(escalation_level, escalation_level)
        assistant_message += f"\n\n**Escalation:** {label}"

    if escalation_reason:
        assistant_message += f"\n\n{escalation_reason}"

    return assistant_message

def format_document_name(document_name: str) -> str:
    return document_name.removesuffix(".md").replace("_", " ").replace("-", " ").title()

if __name__ == "__main__":
    layout()
