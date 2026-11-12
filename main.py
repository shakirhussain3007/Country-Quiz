
import requests
import os
import random
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

API_URL = "https://api.restcountries.com/countries/v5"


def fetch_countries():
    """Fetch country data from REST Countries API."""

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    params = {
        "limit": 100,
        "response_fields": "names.common,capitals,currencies,flag.emoji"
    }

    response = requests.get(
        API_URL,
        headers=headers,
        params=params,
        timeout=15
    )

    response.raise_for_status()

    data = response.json()

    return data.get("data", {}).get("objects", [])


def prepare_countries(raw_countries):
    """Extract useful information from API data."""

    countries = []

    for country in raw_countries:
        name = country.get("names", {}).get("common")

        capitals = country.get("capitals", [])
        currencies = country.get("currencies", [])

        capital = capitals[0].get("name") if capitals else None
        currency = currencies[0].get("name") if currencies else None

        if name and (capital or currency):
            countries.append({
                "name": name,
                "capital": capital,
                "currency": currency
            })

    return countries


def play_quiz(countries):
    """Run the country quiz game."""

    score = 0
    total_questions = 10

    print("\n================================")
    print("       WELCOME TO COUNTRY QUIZ")
    print("================================")
    print("Guess the capital or currency!")
    print("Choose A, B, C, or D.\n")

    for question_number in range(1, total_questions + 1):

        question_type = random.choice(["capital", "currency"])

        # Countries with the selected information
        available = [
            country for country in countries
            if country[question_type]
        ]

        if len(available) < 4:
            print("Not enough countries for this question.")
            break

        selected = random.choice(available)

        correct_answer = selected[question_type]

        # Create three different wrong options
        wrong_answers = list({
            country[question_type]
            for country in available
            if country[question_type] != correct_answer
        })

        if len(wrong_answers) < 3:
            print("Not enough answer options.")
            break

        options = random.sample(wrong_answers, 3)
        options.append(correct_answer)

        random.shuffle(options)

        print(f"\nQuestion {question_number}/{total_questions}")

        if question_type == "capital":
            print(f"What is the capital of {selected['name']}?")
        else:
            print(f"What is the currency of {selected['name']}?")

        for index, option in enumerate(options):
            letter = chr(65 + index)
            print(f"{letter}. {option}")

        user_answer = input("\nYour answer: ").strip().upper()

        while user_answer not in ["A", "B", "C", "D"]:
            user_answer = input(
                "Please enter A, B, C, or D: "
            ).strip().upper()

        selected_option = options[ord(user_answer) - 65]

        if selected_option == correct_answer:
            print("Correct answer!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {correct_answer}")

    print("\n================================")
    print("           QUIZ RESULT")
    print("================================")
    print(f"Your Score: {score}/{total_questions}")

    if score >= 8:
        print("Excellent work!")
    elif score >= 5:
        print("Good effort!")
    else:
        print("Keep practicing!")

    print("Thanks for playing Country Quiz!")


def main():
    try:
        if not API_KEY:
            print("API key not found. Check your .env file.")
            return

        print("Fetching country data...")

        raw_countries = fetch_countries()
        countries = prepare_countries(raw_countries)

        print(f"Successfully loaded {len(countries)} countries.")

        play_quiz(countries)

    except requests.exceptions.RequestException as error:
        print("API connection error:", error)

    except (KeyError, TypeError, IndexError) as error:
        print("Unexpected API data format:", error)


if __name__ == "__main__":
    main()
