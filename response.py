 #Convert the raw response into a Python dictionary
data = r.json()

# Navigate the nested JSON structure to get the text response
answer = data["choices"][0]["message"]["content"]
print("--- AI Answer ---")
print(answer)

# Extract token usage statistics
tokens = data["usage"]["total_tokens"]
print(f"\nTotal Tokens Used: {tokens}")