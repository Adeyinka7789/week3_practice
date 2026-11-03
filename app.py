# TEST OUR ENVIRONMENT VARIABLES
import os
from dotenv import load_dotenv

# Load variables from the local .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL")

print("API key loaded successfully: ", api_key is not None)
print("Active Model: ", model)
