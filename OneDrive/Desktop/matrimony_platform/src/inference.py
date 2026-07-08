import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

import pandas as pd

from config import SCORE_DATA, MATCH_DATA, TOP_MATCHES


def load_scores():
    return pd.read_csv(SCORE_DATA)


def get_matches(scores, user_id):
    matches = scores[scores["user_id"] == user_id]
    matches = matches.sort_values("score", ascending=False)
    return matches.head(TOP_MATCHES)


def save_matches(matches):
    matches.to_csv(MATCH_DATA, index=False)


def run_inference(user_id=1):
    scores = load_scores()
    matches = get_matches(scores, user_id)

    save_matches(matches)

    print("Inference Completed")
    print(matches)

    return matches


if __name__ == "__main__":
    run_inference()