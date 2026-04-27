import lancedb
from backend.constants import VECTOR_DB_PATH

db = lancedb.connect(VECTOR_DB_PATH)


def retrieve_documents(query: str, k: int = 3):
    return db["articles"].search(query).limit(k).to_list()
