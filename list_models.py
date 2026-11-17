import google.generativeai as genai
from config import API_KEY

genai.configure(api_key=API_KEY)

print("Available Models:\n")

for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(model.name)