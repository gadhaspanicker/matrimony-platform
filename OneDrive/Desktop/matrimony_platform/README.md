# Matrimony Platform – Matching & Ranking Backend

## Project Overview

This project implements the backend matching and ranking workflow for a matrimony platform. It focuses on processing user profile data, engineering feature vectors, calculating compatibility scores, generating ranked matches, and evaluating the matching results.

The project does not include any frontend or application interface. It is designed as a modular backend pipeline that can later be integrated into a web or mobile application.

---

## Features

* Generate synthetic matrimony profiles
* Clean and preprocess profile data
* Encode categorical and ordinal features
* Create profile feature vectors
* Calculate rule-based compatibility scores
* Generate ranked matches
* Evaluate matching results
* Configuration through `.env` and `config.py`
* Modular backend architecture

---

## Project Structure

```
matrimony_platform/
│
├── demo_data/
│   └── profiles.csv
│
├── outputs/
│   ├── cleaned_profiles.csv
│   ├── profile_vectors.csv
│   ├── compatibility_scores.csv
│   ├── ranked_matches.csv
│   └── evaluation_report.csv
│
├── src/
│   ├── generate_demo_data.py
│   ├── data_preparation.py
│   ├── feature_engineering.py
│   ├── scoring.py
│   ├── inference.py
│   └── evaluation.py
│
├── .env
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Workflow

### Stage 1 – Demo Data Generation

Generates synthetic matrimony profiles with realistic information including:

* Personal details
* Education
* Income
* Religion
* Location
* Preferences
* Hobbies
* Biography

Output:

```
demo_data/profiles.csv
```

---

### Stage 2 – Data Preparation

* Removes duplicate records
* Handles missing values
* Cleans text fields
* Encodes education levels
* Encodes income levels

Output:

```
outputs/cleaned_profiles.csv
```

---

### Stage 3 – Feature Engineering

* Encodes categorical attributes
* Creates numerical feature vectors
* Saves encoded information

Output:

```
outputs/profile_vectors.csv
```

---

### Stage 4 – Compatibility Scoring

Computes compatibility scores based on user preferences using weighted rules.

Current scoring weights:

| Feature   | Weight |
| --------- | -----: |
| Religion  |     30 |
| Age       |     20 |
| Education |     20 |
| Location  |     15 |
| Income    |     15 |

Output:

```
outputs/compatibility_scores.csv
```

---

### Stage 5 – Inference

Ranks candidate profiles according to compatibility score and returns the top matches.

Output:

```
outputs/ranked_matches.csv
```

---

### Stage 6 – Evaluation

Generates a summary report including:

* Total Matches
* Average Score
* Maximum Score
* Minimum Score

Output:

```
outputs/evaluation_report.csv
```

---

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the complete backend pipeline:

```bash
python main.py
```

The pipeline automatically performs:

1. Generate demo dataset
2. Prepare data
3. Build feature vectors
4. Calculate compatibility scores
5. Generate ranked matches
6. Evaluate results

---

## Configuration

All configurable values are stored in the `.env` file and accessed through `config.py`.

Examples include:

* Number of profiles
* File paths
* Matching weights
* Number of top matches

---

## Output Files

| File                     | Description                              |
| ------------------------ | ---------------------------------------- |
| profiles.csv             | Synthetic profile dataset                |
| cleaned_profiles.csv     | Cleaned and encoded dataset              |
| profile_vectors.csv      | Feature vector representation            |
| compatibility_scores.csv | Compatibility scores for candidate pairs |
| ranked_matches.csv       | Top ranked matches                       |
| evaluation_report.csv    | Evaluation summary                       |

---

## Technologies Used

* Python
* Pandas
* NumPy
* Faker
* Python Dotenv
* Scikit-learn

---

## Future Improvements

* Real-time profile matching
* Vector database integration
* Content-based recommendation
* Collaborative filtering
* Precision@K and Recall@K evaluation
* REST API integration
* Database connectivity
* Deployment using Docker and cloud services

---

## Author

**Gadha S Panicker**

M.Sc. Computer Science (Data Analytics)

Backend Data Science Workflow – Matrimony Platform
