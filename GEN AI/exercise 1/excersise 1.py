import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables (optional but recommended)
load_dotenv()

client = OpenAI(
    api_key="APIKEY", 
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="Explain the purpose of Generative AI in detail with examples.",
    model="openai/gpt-oss-20b",
)

print(response.output_text)
