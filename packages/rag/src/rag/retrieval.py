import lancedb
import mlflow
from rag.constants import VECTOR_DB_PATH, TABLE_NAME

db = lancedb.connect(VECTOR_DB_PATH)


def get_table():
    if TABLE_NAME not in db.table_names():
        return None
    return db[TABLE_NAME]


def retrieve_documents(query: str, k: int = 3) -> list[dict]:
    table = get_table()
    if table is None:
        return []

    with mlflow.start_span(name="retrieve_documents", span_type="RETRIEVER") as span:
        span.set_inputs({"query": query, "k": k})

        results = table.search(query).limit(k).to_list()

        documents = [
            {
                "document_name": result["document_name"],
                "file_path": result["file_path"],
                "content": result["content"],
                "distance": result["_distance"],
            }
            for result in results
        ]

        span.set_outputs(
            [
                {
                    "page_content": doc["content"],
                    "metadata": {
                        "doc_uri": doc["file_path"],
                        "document_name": doc["document_name"],
                        "distance": doc["distance"],
                    },
                    "id": doc["document_name"],
                }
                for doc in documents
            ]
        )
        return documents


def get_document(document_name: str) -> dict | None:
    table = get_table()
    if table is None:
        return None

    df = table.to_pandas()
    match = df[df["document_name"] == document_name]
    if match.empty:
        return None

    row = match.iloc[-1]
    return {
        "document_name": str(row["document_name"]),
        "file_path": str(row["file_path"]),
        "content": str(row["content"]),
    }


def list_document_names(*, include_extension: bool = False) -> list[str]:
    table = get_table()
    if table is None:
        return []

    df = table.to_pandas()
    if df.empty or "document_name" not in df.columns:
        return []
    # preserve insertion order of first occurrence while de-duping
    names = list(dict.fromkeys(df["document_name"].astype(str).tolist()))

    if include_extension:
        return names

    return [name.removesuffix(".md") for name in names]
