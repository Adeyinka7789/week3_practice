# TEST OUR ENVIRONMENT VARIABLES
import requests
import os
from dotenv import load_dotenv

# Load variables from the local .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL")

print("API key loaded successfully: ", api_key is not None)
print("Active Model: ", model)

# MAKE FIRST API REQUEST

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json"
}

body = {
    "model": model,
    "messages": [
        {"role": "user", "content": "Explain APIs to a beginner."}
    ]
}

# send the POST request
r = requests.post(url, headers=headers, json=body)

# check the HTTP status code(200 means success!)
print("HTTP status code:", r.status_code)

# Convert the raw response into a Python dictionary
data = r.json()

# Navigate the nested JSON structure to get the text response
answer = data["choices"][0]["message"]["content"]
print("--- AI Answer ---")
print(answer)

# Extract token usage statistics
tokens = data["usage"]["total_tokens"]
print(f"\nTotal Tokens Used: {tokens}")
