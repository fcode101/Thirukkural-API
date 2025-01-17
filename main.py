from fastapi import FastAPI, HTTPException
import random

app = FastAPI(
    title="Thirukkural API",
    description="""
    The Thirukkural API is a simple FastAPI-based web service that provides random verses from the Tamil literary work, the Thirukkural, along with their English translations. It aims to serve those interested in exploring the wisdom of the Thirukkural in both its original Tamil form and its English version.

    This API fetches random Thirukkural verses each time a request is made, offering a seamless way for users to access a piece of this ancient text without having to read through the entire book. It's designed to be a convenient resource for education, research, or personal enrichment.
    """,
    version="1.0.0",
    docs_url="/",
    redoc_url="/redoc",
    contact={
        "name": "Support Team",
        "email": "heavenlyapi@example.com",
    },
    openapi_tags=[
        {
            "name": "Random Thirukkural",
            "description": "Fetches a random Thirukkural verse along with its English translation.",
        },
        {
            "name": "Get Thirukkural by ID",
            "description": "Fetches a specific Thirukkural verse by its ID (1-1330).",
        },
    ],
)

# Declare Global variables
thirukkural = []
english = []


@app.on_event("startup")
def load_thirukkural():
    global thirukkural
    global english

    # Read Tamil version of Thirukkural
    with open("Tamil_Thirukkural.txt", "r", encoding="utf8") as file:
        thirukkural = [line.strip() for line in file if line.strip()]

    # Read English version of Thirukkural
    with open("English_Thirukkural.txt", "r", encoding="utf8") as file:
        english = [line.strip() for line in file if line.strip()]


@app.get("/thirukkural/random", tags=["Random Thirukkural"])
def read_random_thirukkural():
    """Fetches a random Thirukkural verse and its English translation"""

    # Get random index
    random_index = random.randint(0, len(thirukkural) - 1)

    # Get the Tamil verse
    tamil_version = thirukkural[random_index]

    # Get the corresponding English translation
    english_version = english[random_index] if random_index < len(english) else "No translation available"

    # Get the verse number (Kural)
    verse_number = random_index + 1  # Add 1 to match the verse number (1-based index)

    return {
        "Kural Number": verse_number,
        "Tamil Thirukkural": tamil_version,
        "English Translation": english_version,
    }


@app.get("/thirukkural/id", tags=["Get Thirukkural by ID"])
def read_thirukkural_by_id(kural_id: int):
    """
    Fetches a specific Thirukkural verse by its ID (1-1330).
    - **kural_id**: The number of the Kural to fetch.
    """

    # Validate ID
    if kural_id < 1 or kural_id > len(thirukkural):
        raise HTTPException(status_code=404, detail="Kural not found")

    # Get the Tamil verse
    tamil_version = thirukkural[kural_id - 1]

    # Get the corresponding English translation
    english_version = english[kural_id - 1] if kural_id <= len(english) else "No translation available"

    return {
        "Kural Number": kural_id,
        "Tamil Thirukkural": tamil_version,
        "English Translation": english_version,
    }
