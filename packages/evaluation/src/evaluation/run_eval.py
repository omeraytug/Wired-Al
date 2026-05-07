import asyncio
import json

import mlflow
from mlflow.genai import evaluate
from mlflow.genai.datasets import create_dataset
from mlflow.genai.scorers import Correctness, RetrievalRelevance, RelevanceToQuery

from backend.constants import LLM_JUDGE, MLFLOW_DB_PATH, EVAL_DATA_PATH
from backend.model import chat


def bot_answer(question: str):
    response = asyncio.run(chat(question))

    return {
        "answer": response.answer,
        "sources": [source.model_dump() for source in response.sources],
    }


def main() -> None:
    mlflow.set_tracking_uri(MLFLOW_DB_PATH)

    experiment = mlflow.set_experiment(experiment_name="wired_al_evaluation")

    with open(EVAL_DATA_PATH) as file:
        eval_data = json.load(file)

    evaluation_dataset = create_dataset(
        name="wired_al_evaluation", experiment_id=experiment.experiment_id
    )

    evaluation_dataset.merge_records(eval_data)

    scorers = [
        Correctness(name="factual_accuracy", model=LLM_JUDGE),
        RetrievalRelevance(model=LLM_JUDGE),
        RelevanceToQuery(model=LLM_JUDGE),
    ]

    with mlflow.start_run(run_name="evaluation_short"):
        results = evaluate(
            data=evaluation_dataset, predict_fn=bot_answer, scorers=scorers
        )

    print(results)


if __name__ == "__main__":
    main()
