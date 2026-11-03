#MAKE FIRST API REQUEST
import requests

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

#send the POST request
r = requests.post(url, headers=headers, json=body)

#check the HTTP status code(200 means success!)
print("HTTP status code:", r.status_code)