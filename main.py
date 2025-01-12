from fastapi import FastAPI
import random

app = FastAPI()

# Load Thirukkural once at startup
thirukkural = []
english = []

@app.on_event("startup")
def load_thirukkural():
    global thirukkural
    global english
    with open('thirukkural.txt', 'r', encoding='utf8') as file:
        thirukkural = [line.strip() for line in file if line.strip()] 
    with open('English_thirukkural.txt', 'r', encoding='utf8') as file:
        english = [line.strip() for line in file if line.strip()]     

@app.get("/")
def read_thirukkural():
    random_index = random.randint(0, len(thirukkural) - 1)  # Get a random index
    tamil_version = thirukkural[random_index]
    english_version = english[random_index] if random_index < len(english) else "No translation available"

    return {
        "Tamil Thirukkural": tamil_version,
        "English Translation": english_version
    }
