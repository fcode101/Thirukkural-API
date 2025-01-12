# Thirukkural API

The Thirukkural API is a simple FastAPI-based web service that provides random verses from the Tamil literary work, the Thirukkural, along with their English translations. It aims to serve those interested in exploring the wisdom of the Thirukkural in both its original Tamil form and its English version.

This API fetches random Thirukkural verses each time a request is made, offering a seamless way for users to access a piece of this ancient text without having to read through the entire book. It's designed to be a convenient resource for education, research, or personal enrichment.

## Purpose and Motivation

The motivation behind developing this project was to create an easy-to-use API that makes the Thirukkural accessible to a global audience. While the Thirukkural is a classic piece of literature widely studied in Tamil culture, its availability in different languages, especially English, is often scattered or difficult to access in a structured way.

By developing this API, I wanted to provide an automated and simple interface to read random verses from the Thirukkural and their English translations. This can help promote the text to a wider audience, including those who may not be familiar with Tamil, and encourage the appreciation of this ancient wisdom.

## Problem Solved

This project addresses the need for easy access to the Thirukkural, particularly for English-speaking audiences. Users no longer need to sift through various websites or books to find a verse and its translation. The API delivers it at the click of a button, making it more convenient for individuals to interact with the text.

## What I’ve Learned

Through this project, I learned how to use FastAPI to build a simple, yet powerful API. I also gained experience with handling text files, parsing data, and implementing randomization in an efficient way. Working with multiple text files for the Tamil and English versions of the Thirukkural also taught me how to structure data and ensure synchronization between the two versions.

I learned how to set up endpoints, handle requests, and structure an application for easy deployment. Additionally, I enhanced my skills in reading, writing, and serving static data through APIs.

## Tech Stack

- **Backend Framework**: FastAPI
- **Programming Language**: Python
- **Server**: Uvicorn (for running the FastAPI app)
- **File Format**: .txt (for storing Thirukkural verses and translations)

The API uses two text files: `thirukkural.txt` (for Tamil verses) and `English_thirukkural.txt` (for the English translation). The API loads these files during startup and serves a random verse each time a request is made.

## Design

Since this project is an API, the interface is command-line based and interacts with HTTP requests. However, I plan to build a simple front-end interface where users can click to get a random Thirukkural verse. For now, the user can test it through a local or hosted API endpoint.

### Example Response:
```json
{
  "Tamil Thirukkural": "எப்பொருள் எத்தன்மைத் தாயினும் அப்பொருள். மெய்ப்பொருள் காண்பது அறிவு.",
  "English Translation": "It doesn’t matter what anything seems to be; wisdom lies in seeking to grasp its true nature."
}
```
## Features
Random Thirukkural Verse: Fetches a random Tamil verse along with its English translation.
Dual Language Support: Serves both Tamil and English versions.
FastAPI: Built using FastAPI for speed and simplicity.
Startup Optimization: Efficient file reading during startup to load data only once.

## How to Run the Project
**Prerequisites**
- **Python 3.6 or higher**
- **Uvicorn for serving the FastAPI app**

Setup Instructions
Clone the repository:

```
git clone https://github.com/yourusername/thirukkural-api.git
cd thirukkural-api
```

You Can Run in API 
API Link : " "

Run the FastAPI app:

Access the API at http://127.0.0.1:8000/ to get a random Thirukkural verse.

Hosting
To make the API accessible online, you can deploy it using platforms like Heroku, AWS, or DigitalOcean. The hosted API will allow users from anywhere to access the Thirukkural API easily.
