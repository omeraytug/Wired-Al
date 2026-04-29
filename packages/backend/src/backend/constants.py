from pathlib import Path

BASE_PATH = Path(__file__).parents[3].resolve()

DATA_PATH = BASE_PATH / "rag" / "data"
VECTOR_DB_PATH = BASE_PATH / "rag" / "knowledge_base"

TABLE_NAME = "articles"

EMBEDDING_MODEL = "embed-multilingual-light-v3.0"

MODEL_SMALL = "openrouter:openai/gpt-oss-20b:free"
MODEL_MEDIUM = "google-gla:gemini-3-flash-preview"
MODEL_LARGE = "openrouter:nvidia/nemotron-3-super-120b-a12b:free"


