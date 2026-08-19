import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("API KEY EXISTS:", bool(api_key))

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")

client = Groq(api_key=api_key)

try:
    models = client.models.list()

    print("\nAvailable models:\n")

    for model in models.data:
        print(model.id)

except Exception as e:
    print("\nGROQ ERROR:")
    print(e)