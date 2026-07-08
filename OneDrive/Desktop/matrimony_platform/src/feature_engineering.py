import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

import joblib
import numpy as np
import pandas as pd

from config import CLEAN_DATA, VECTOR_DATA


def load_data():
    return pd.read_csv(CLEAN_DATA)


def encode_basic(df):
    columns = [
        "gender",
        "religion",
        "caste",
        "diet",
        "city",
        "state"
    ]

    encoders = {}

    for col in columns:
        df[col] = df[col].fillna("Unknown").astype(str)
        df[col], values = pd.factorize(df[col])
        encoders[col] = list(values)

    return df, encoders


def create_match_flags(df):
    df["age_match"] = 1
    df["income_match"] = 1
    return df


def get_feature_columns():
    return [
        "age",
        "height_cm",
        "education",
        "income",
        "gender",
        "religion",
        "caste",
        "diet",
        "city",
        "state",
        "age_match",
        "income_match"
    ]


def create_vectors(df):
    columns = get_feature_columns()
    return df[columns].fillna(0).to_numpy()


def save_vectors(df, vectors, encoders):
    vector_df = pd.DataFrame(vectors)

    vector_df.insert(0, "user_id", df["user_id"])
    vector_df.insert(1, "profile_vector_id", df["profile_vector_id"])

    vector_df.to_csv(VECTOR_DATA, index=False)

    joblib.dump(
        encoders,
        VECTOR_DATA.parent / "encoders.pkl"
    )


def build_features():
    df = load_data()
    df, encoders = encode_basic(df)
    df = create_match_flags(df)

    vectors = create_vectors(df)

    save_vectors(df, vectors, encoders)

    print("Feature Engineering Completed")
    print("Vector Shape:", vectors.shape)

    return vectors


if __name__ == "__main__":
    build_features()