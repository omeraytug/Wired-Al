import os
from pathlib import Path
from urllib.parse import quote

import httpx
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")
# Azure cold starts and LanceDB scans can exceed httpx’s short default; override in Container App if needed.
HTTP_TIMEOUT = float(os.getenv("HTTP_TIMEOUT", "120"))
ASSETS = Path(__file__).resolve().parent.parent / "assets"


def display_document_name(raw: str) -> str:
    return raw.replace("_", " ").strip().title()


with st.sidebar:
    st.image(str(ASSETS / "logo-dark.png"))

documents: list[str] = []
list_error: str | None = None
try:
    list_response = httpx.get(
        f"{API_URL}/documents",
        timeout=HTTP_TIMEOUT,
    )
    list_response.raise_for_status()
    documents = list(list_response.json().get("documents", []))
except httpx.HTTPStatusError as exc:
    list_error = f"HTTP {exc.response.status_code}: {exc.response.text}"
except httpx.RequestError as exc:
    # Includes ReadTimeout, ConnectError, etc. (subclasses of RequestError, not HTTPStatusError)
    list_error = str(exc)

with st.sidebar:
    st.subheader("Documents")
    if list_error is not None:
        st.caption("Could not load the document list.")
    elif not documents:
        st.caption("No documents in the index.")
    else:
        st.markdown(
            "\n".join(f"- {display_document_name(name)}" for name in documents)
        )

st.title("Knowledge base")

if list_error is not None:
    st.error(
        f"Could not load documents from `{API_URL}`. {list_error}\n\n"
        "In Azure Container Apps, set the frontend **API_URL** to your backend’s base URL "
        "(for example `https://<your-backend-app>.azurecontainerapps.io`, no trailing slash). "
        "If the backend is slow to start, increase **HTTP_TIMEOUT** (seconds)."
    )
    st.stop()

if not documents:
    st.info("No documents are available yet. Ingest markdown into LanceDB or check the backend data path.")
    st.stop()

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
        doc_response = httpx.get(
            f"{API_URL}/documents/{path}",
            timeout=HTTP_TIMEOUT,
        )
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
        st.error(f"Could not reach the backend at {API_URL}. {exc}")
    else:
        with st.expander("Metadata", expanded=False):
            st.markdown(f"**document_name:** `{doc.get('document_name', '')}`")
            st.markdown(f"**file_path:** `{doc.get('file_path', '')}`")

        st.markdown(doc.get("content", ""))
