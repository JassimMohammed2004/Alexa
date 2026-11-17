import os
import time
from dotenv import load_dotenv
from google import genai
from config import GEMINI_MODEL

# Load .env file
load_dotenv()

# Get API Key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

# Create Gemini client
client = genai.Client(api_key=API_KEY)


def ask_ai(prompt, max_retries=3):
    """
    Send a prompt to Gemini with retry logic for transient errors (e.g. 503 UNAVAILABLE).
    Returns response text or a clean error message.
    """
    model = GEMINI_MODEL
    delay = 1.0

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )
            return response.text

        except Exception as e:
            err_str = str(e)
            is_transient = "503" in err_str or "UNAVAILABLE" in err_str or "high demand" in err_str

            if is_transient and attempt < max_retries - 1:
                time.sleep(delay)
                delay *= 2.0
                continue

            if is_transient:
                return "The AI service is currently experiencing high demand. Please try again in a moment."

            return f"AI Error: {e}"