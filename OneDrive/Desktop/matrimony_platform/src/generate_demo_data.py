import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from faker import Faker
import pandas as pd
import random
from config import INPUT_DATA, NUM_PROFILES

fake = Faker("en_IN")

Faker.seed(42)
random.seed(42)

RELIGIONS = [
    "Hindu",
    "Muslim",
    "Christian",
    "Sikh",
    "Jain"
]

CASTES = [
    "General",
    "OBC",
    "SC",
    "ST"
]

DIETS = [
    "Veg",
    "Non-Veg",
    "Eggetarian"
]

MARITAL_STATUS = [
    "Single",
    "Divorced",
    "Widowed"
]

EDUCATIONS = [
    "Higher Secondary",
    "Diploma",
    "Bachelor",
    "Master",
    "PhD"
]

INCOMES = [
    "3-5 LPA",
    "5-10 LPA",
    "10-15 LPA",
    "15-25 LPA",
    "25-40 LPA",
    "40+ LPA"
]

OCCUPATIONS = [
    "Software Engineer",
    "Doctor",
    "Teacher",
    "Business",
    "Data Analyst",
    "Data Scientist",
    "Lawyer",
    "Accountant",
    "Professor",
    "Government Employee"
]

HOBBIES = [
    "Reading",
    "Music",
    "Movies",
    "Travel",
    "Cooking",
    "Cycling",
    "Painting",
    "Photography",
    "Chess",
    "Yoga",
    "Swimming",
    "Cricket",
    "Football"
]

BIOS = [
    "Simple and family oriented.",
    "Career focused with strong values.",
    "Love travelling and exploring.",
    "Looking for a caring partner.",
    "Passionate about learning.",
    "Friendly and optimistic.",
    "Love books and technology.",
    "Enjoy spending time with family."
]

CITIES = {
    "Kerala": ["Kochi", "Kottayam", "Kannur", "Kozhikode"],
    "Tamil Nadu": ["Chennai", "Coimbatore"],
    "Karnataka": ["Bengaluru", "Mangalore"],
    "Telangana": ["Hyderabad"],
    "Delhi": ["Delhi"],
    "Goa": ["Panaji"],
    "Maharashtra": ["Mumbai", "Pune"]
}


def get_gender():
    return random.choice(["Male", "Female"])


def get_location():
    state = random.choice(list(CITIES.keys()))
    city = random.choice(CITIES[state])
    return state, city


def get_hobbies():
    return random.sample(HOBBIES, 3)


def get_preferences(age, height, gender):
    return {
        "preferred_gender": "Female" if gender == "Male" else "Male",
        "preferred_age_min": max(21, age - random.randint(2, 5)),
        "preferred_age_max": min(50, age + random.randint(2, 6)),
        "preferred_height_min": max(145, height - 10),
        "preferred_height_max": min(200, height + 10),
        "preferred_religion": random.choice(RELIGIONS),
        "preferred_caste": random.choice(CASTES),
        "preferred_city": random.choice(
            [city for cities in CITIES.values() for city in cities]
        ),
        "preferred_state": random.choice(list(CITIES.keys())),
        "preferred_education": random.choice(EDUCATIONS),
        "preferred_income": random.choice(INCOMES)
    }


def create_profile(user_id):
    gender = get_gender()
    state, city = get_location()
    age = random.randint(21, 45)
    height = random.randint(150, 190)
    hobby1, hobby2, hobby3 = get_hobbies()

    profile = {
        "user_id": user_id,
        "profile_vector_id": f"VEC_{user_id}",
        "name": fake.name_male() if gender == "Male" else fake.name_female(),
        "gender": gender,
        "age": age,
        "height_cm": height,
        "religion": random.choice(RELIGIONS),
        "caste": random.choice(CASTES),
        "marital_status": random.choice(MARITAL_STATUS),
        "diet": random.choice(DIETS),
        "city": city,
        "state": state,
        "education": random.choice(EDUCATIONS),
        "income": random.choice(INCOMES),
        "occupation": random.choice(OCCUPATIONS),
        "hobby_1": hobby1,
        "hobby_2": hobby2,
        "hobby_3": hobby3,
        "about_me": random.choice(BIOS)
    }

    profile.update(get_preferences(age, height, gender))
    return profile


def generate():
    profiles = []

    for user_id in range(1, NUM_PROFILES + 1):
        profiles.append(create_profile(user_id))

    df = pd.DataFrame(profiles)
    df.to_csv(INPUT_DATA, index=False)

    print("Dataset Generated Successfully!")
    print("Shape:", df.shape)

    return df


if __name__ == "__main__":
    generate()