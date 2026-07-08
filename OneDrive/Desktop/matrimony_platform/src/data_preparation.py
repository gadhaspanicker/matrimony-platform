import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

import pandas as pd
from config import INPUT_DATA, CLEAN_DATA


def load_data():
    return pd.read_csv(INPUT_DATA)


def remove_duplicates(df):
    return df.drop_duplicates().reset_index(drop=True)


def fill_missing(df):
    obj_cols = df.select_dtypes(include=["object", "string"]).columns
    num_cols = df.select_dtypes(exclude=["object", "string"]).columns

    df[obj_cols] = df[obj_cols].fillna("Unknown")
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    return df


def clean_text(df):
    obj_cols = df.select_dtypes(include=["object", "string"]).columns

    for col in obj_cols:
        if col != "profile_vector_id":
            df[col] = df[col].astype(str).str.strip().str.title()

    return df


def encode_education(df):
    education_map = {
        "Higher Secondary": 1,
        "Diploma": 2,
        "Bachelor": 3,
        "Master": 4,
        "Phd": 5
    }

    df["education"] = df["education"].map(education_map)
    return df


def encode_income(df):
    income_map = {
        "3-5 Lpa": 1,
        "5-10 Lpa": 2,
        "10-15 Lpa": 3,
        "15-25 Lpa": 4,
        "25-40 Lpa": 5,
        "40+ Lpa": 6
    }

    df["income"] = df["income"].map(income_map)
    return df


def save_data(df):
    df.to_csv(CLEAN_DATA, index=False)


def prepare_data():
    df = load_data()
    df = remove_duplicates(df)
    df = fill_missing(df)
    df = clean_text(df)
    df = encode_education(df)
    df = encode_income(df)
    save_data(df)

    print("Data Preparation Completed")
    print("Shape:", df.shape)

    return df


if __name__ == "__main__":
    prepare_data()