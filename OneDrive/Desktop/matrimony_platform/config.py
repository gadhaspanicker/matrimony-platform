from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

DEMO_DATA = BASE_DIR / "demo_data"
OUTPUTS = BASE_DIR / "outputs"

INPUT_DATA = BASE_DIR / os.getenv("INPUT_DATA")
CLEAN_DATA = BASE_DIR / os.getenv("CLEAN_DATA")
VECTOR_DATA = BASE_DIR / os.getenv("VECTOR_DATA")
SCORE_DATA = BASE_DIR / os.getenv("SCORE_DATA")
MATCH_DATA = BASE_DIR / os.getenv("MATCH_DATA")
EVALUATION_DATA = BASE_DIR / os.getenv("EVALUATION_DATA")

NUM_PROFILES = int(os.getenv("NUM_PROFILES"))

WEIGHTS = {
    "religion": int(os.getenv("RELIGION_WEIGHT")),
    "age": int(os.getenv("AGE_WEIGHT")),
    "education": int(os.getenv("EDUCATION_WEIGHT")),
    "location": int(os.getenv("LOCATION_WEIGHT")),
    "income": int(os.getenv("INCOME_WEIGHT"))
}

TOP_MATCHES = int(os.getenv("TOP_MATCHES"))

DEMO_DATA.mkdir(exist_ok=True)
OUTPUTS.mkdir(exist_ok=True)