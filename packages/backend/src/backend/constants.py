import mlflow
import os
from pathlib import Path

BASE_PATH = Path(__file__).parents[3].resolve()

ROOT_PATH = BASE_PATH.parents[0]

PROMPTS_PATH = BASE_PATH / "backend" / "src" / "backend" / "prompts"
MLFLOW_PATH = ROOT_PATH / "mlflow"

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")

DATA_PATH = BASE_PATH / "rag" / "data"
VECTOR_DB_PATH = BASE_PATH / "rag" / "knowledge_base"

EVAL_DATA_PATH = BASE_PATH / "evaluation" / "data" / "eval_cases.json"

TABLE_NAME = "articles"

EMBEDDING_MODEL = "embed-multilingual-light-v3.0"

MODEL_SMALL = "openrouter:openai/gpt-oss-20b:free"
MODEL_MEDIUM = "google-gla:gemini-3-flash-preview"
MODEL_LARGE = "openrouter:nvidia/nemotron-3-super-120b-a12b:free"
OPENAI_MODEL = "openai:gpt-4o-mini"

LLM_JUDGE = "openrouter:/nvidia/nemotron-3-nano-30b-a3b:free"

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
