import lancedb
from dotenv import load_dotenv

from rag.constants import VECTOR_DB_PATH, DATA_PATH, TABLE_NAME
from rag.data_models import Article

load_dotenv()


def setup_vector_db():
    db = lancedb.connect(VECTOR_DB_PATH)
    db.create_table(TABLE_NAME, schema=Article, exist_ok=True)

    return db


def ingest_docs(table):
    for file in DATA_PATH.glob("*.md"):
        content = file.read_text()

        table.delete(f"document_name = '{file.name}'")
        table.add(
            [{"document_name": file.name, "file_path": str(file), "content": content}]
        )


if __name__ == "__main__":
    db = setup_vector_db()
    ingest_docs(db[TABLE_NAME])
