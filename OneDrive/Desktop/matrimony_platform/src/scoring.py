import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

import pandas as pd

from config import CLEAN_DATA, SCORE_DATA, WEIGHTS


def load_data():
    return pd.read_csv(CLEAN_DATA)


def religion_score(user, candidate):
    if candidate["religion"] == user["preferred_religion"]:
        return WEIGHTS["religion"]
    return 0


def age_score(user, candidate):
    if user["preferred_age_min"] <= candidate["age"] <= user["preferred_age_max"]:
        return WEIGHTS["age"]
    return 0


def education_score(user, candidate):
    if candidate["education"] == user["preferred_education"]:
        return WEIGHTS["education"]
    return 0


def location_score(user, candidate):
    if candidate["city"] == user["preferred_city"]:
        return WEIGHTS["location"]
    return 0


def income_score(user, candidate):
    if candidate["income"] == user["preferred_income"]:
        return WEIGHTS["income"]
    return 0


def compatibility(user, candidate):
    score = 0
    score += religion_score(user, candidate)
    score += age_score(user, candidate)
    score += education_score(user, candidate)
    score += location_score(user, candidate)
    score += income_score(user, candidate)
    return score


def generate_scores(df):
    results = []

    for _, user in df.iterrows():

        for _, candidate in df.iterrows():

            if user["user_id"] == candidate["user_id"]:
                continue

            score = compatibility(user, candidate)

            results.append(
                {
                    "user_id": user["user_id"],
                    "candidate_id": candidate["user_id"],
                    "score": score
                }
            )

    return pd.DataFrame(results)


def save_scores(scores):
    scores.to_csv(SCORE_DATA, index=False)


def run_scoring():
    df = load_data()
    scores = generate_scores(df)
    save_scores(scores)

    print("Scoring Completed")
    print(scores.head())

    return scores


if __name__ == "__main__":
    run_scoring()