import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GOOGLE_GENAI_API_KEY")
model = os.getenv("GOOGLE_GENAI_MODEL", "gemini-pro")

if not api_key:
    raise ValueError("GOOGLE_GENAI_API_KEY environment variable not set.")

llm = GoogleGenerativeAI(
    model=model,
    google_api_key=api_key,
    temperature=0.7,
)