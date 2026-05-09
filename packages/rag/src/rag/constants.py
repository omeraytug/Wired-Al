import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

RAG_PACKAGE_PATH = Path(__file__).parents[2].resolve()

DATA_PATH = RAG_PACKAGE_PATH / "data"
VECTOR_DB_PATH = RAG_PACKAGE_PATH / "knowledge_base"

TABLE_NAME = "articles"

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "embed-multilingual-light-v3.0")
