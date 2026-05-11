import os
from pathlib import Path
from urllib.parse import quote

import httpx
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")
ASSETS = Path(__file__).resolve().parent.parent / "assets"


def display_document_name(raw: str) -> str:
    return raw.replace("_", " ").strip().title()


try:
    list_response = httpx.get(f"{API_URL}/documents")
    list_response.raise_for_status()
    documents = list(list_response.json().get("documents", []))
except httpx.HTTPError as exc:
    st.error(f"The backend returned an error while listing documents: {exc}")
    st.stop()
except httpx.RequestError as exc:
    st.error(f"Could not connect to the backend at {API_URL}. {exc}")
    st.stop()

if not documents:
    st.info("No documents are available yet. Ingest markdown into LanceDB or check the backend data path.")
    st.stop()

with st.sidebar:
    st.image(str(ASSETS / "logo-dark.png"))
    st.subheader("Documents")
    st.markdown(
        "\n".join(f"- {display_document_name(name)}" for name in documents)
    )

st.title("Knowledge base")

choice = st.selectbox(
    "Open a document",
    options=documents,
    index=None,
    placeholder="Choose one…",
    format_func=display_document_name,
)

if choice is None:
    st.caption("Select a document to show its contents here.")
else:
    path = quote(choice, safe="")
    try:
        doc_response = httpx.get(f"{API_URL}/documents/{path}")
        doc_response.raise_for_status()
        doc = doc_response.json()
    except httpx.HTTPStatusError as exc:
        if exc.response.status_code == 404:
            st.warning("That document was not found.")
        else:
            st.error(
                f"Request failed ({exc.response.status_code}): {exc.response.text}"
            )
    except httpx.RequestError as exc:
        st.error(f"Could not connect to the backend at {API_URL}. {exc}")
    else:
        with st.expander("Metadata", expanded=False):
            st.markdown(f"**document_name:** `{doc.get('document_name', '')}`")
            st.markdown(f"**file_path:** `{doc.get('file_path', '')}`")

        st.markdown(doc.get("content", ""))
