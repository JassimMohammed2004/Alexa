from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Microphone configuration: None uses system default, or integer index
_mic_env = os.getenv("MIC_DEVICE_INDEX", "").strip()
MIC_DEVICE_INDEX = int(_mic_env) if _mic_env.isdigit() else None

# Gemini model configuration
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")