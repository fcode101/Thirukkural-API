from fastapi import FastAPI
import random

app = FastAPI()

# Declare Global 
thirukkural = []
english = []

@app.on_event("startup")
def load_thirukkural():
    global thirukkural
    global english
              # Read Tamil version of Thirukkural
    with open('thirukkural.txt', 'r', encoding='utf8') as file:
        thirukkural = [line.strip() for line in file if line.strip()] 
        
                # Read English version of Thirukkural
    with open('English_thirukkural.txt', 'r', encoding='utf8') as file:
        english = [line.strip() for line in file if line.strip()]     

@app.get("/")
def read_thirukkural():
    
    #Get random Thirukkural
    random_index = random.randint(0, len(thirukkural) - 1)  
    tamil_version = thirukkural[random_index]
    
     # Get the corresponding English version or provide fallback if out of bounds
    english_version = english[random_index] if random_index < len(english) else "No translation available"

    return {
        "Tamil Thirukkural": tamil_version,
        "English Translation": english_version
    }
