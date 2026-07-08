import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

import pandas as pd

from config import MATCH_DATA, EVALUATION_DATA


def load_matches():
    return pd.read_csv(MATCH_DATA)


def evaluate(matches):
    return pd.DataFrame({
        "Metric": [
            "Total Matches",
            "Average Score",
            "Maximum Score",
            "Minimum Score"
        ],
        "Value": [
            len(matches),
            matches["score"].mean(),
            matches["score"].max(),
            matches["score"].min()
        ]
    })


def save_report(report):
    report.to_csv(EVALUATION_DATA, index=False)


def run_evaluation():
    matches = load_matches()
    report = evaluate(matches)

    save_report(report)

    print("Evaluation Completed")
    print(report)

    return report


if __name__ == "__main__":
    run_evaluation()