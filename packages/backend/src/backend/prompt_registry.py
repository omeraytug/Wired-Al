import mlflow
from backend.constants import PROMPTS_PATH, MLFLOW_DB_PATH
from mlflow.genai import register_prompt

def register_prompts(**kwargs):
    mlflow.set_tracking_uri(MLFLOW_DB_PATH)
    mlflow.set_experiment("wired-al-prompts")
    for filepath in PROMPTS_PATH.glob("*.md"):
        with open(filepath) as file:
            filename = filepath.stem
            prompt = file.read()
            
        register_prompt(name=filename,template=prompt, **kwargs)
        

if __name__ == "__main__":
    register_prompts()
    print(MLFLOW_DB_PATH)