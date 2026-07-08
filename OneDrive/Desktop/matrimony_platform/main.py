from src.generate_demo_data import generate
from src.data_preparation import prepare_data
from src.feature_engineering import build_features
from src.scoring import run_scoring
from src.inference import run_inference
from src.evaluation import run_evaluation


def main():
    print("=" * 60)
    print(" MATRIMONY MATCHING PIPELINE ")
    print("=" * 60)

    print("\n[1/6] Generating Demo Dataset...")
    generate()

    print("\n[2/6] Preparing Data...")
    prepare_data()

    print("\n[3/6] Building Feature Vectors...")
    build_features()

    print("\n[4/6] Running Compatibility Scoring...")
    run_scoring()

    print("\n[5/6] Running Inference...")
    run_inference()

    print("\n[6/6] Running Evaluation...")
    run_evaluation()

    print("\n" + "=" * 60)
    print(" PIPELINE COMPLETED SUCCESSFULLY ")
    print("=" * 60)


if __name__ == "__main__":
    main()