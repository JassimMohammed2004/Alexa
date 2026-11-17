import speech_recognition as sr
import traceback

r = sr.Recognizer()

with sr.Microphone(device_index=2) as source:
    print("Speak something...")
    r.adjust_for_ambient_noise(source, duration=2)
    audio = r.listen(source, timeout=5, phrase_time_limit=5)

print("Recognizing...")

try:
    text = r.recognize_google(audio, language="en-IN")
    print("You said:", text)

except Exception:
    traceback.print_exc()