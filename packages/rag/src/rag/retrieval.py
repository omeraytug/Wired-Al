import lancedb
from backend.constants import VECTOR_DB_PATH, TABLE_NAME

db = lancedb.connect(VECTOR_DB_PATH)


def retrieve_documents(query: str, k: int = 3):
    results = db[TABLE_NAME].search(query).limit(k).to_list()
    return [
        {
            "document_name": result["document_name"],
            "file_path": result["file_path"],
            "content": result["content"],
            "distance": result["_distance"],
        }
        for result in results
    ]
