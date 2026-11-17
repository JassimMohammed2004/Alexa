import speech_recognition as sr
import pyttsx3


# ==========================================
# TEXT TO SPEECH SETUP
# ==========================================

engine = pyttsx3.init()

# Speech speed
engine.setProperty("rate", 170)

# Volume
engine.setProperty("volume", 1.0)

# Get available voices
voices = engine.getProperty("voices")

# Select first available voice
if voices:
    engine.setProperty("voice", voices[0].id)


# ==========================================
# SPEAK FUNCTION
# ==========================================

def speak(text):
    """
    Convert text into speech.
    Used in both Voice Mode and Text Mode.
    """

    try:

        if text is None:
            return

        text = str(text).strip()

        if not text:
            return

        # Show what Alexa is speaking
        print(f"\nAlexa: {text}")

        # Add speech to engine
        engine.say(text)

        # Speak
        engine.runAndWait()

    except Exception as e:
        print("Speech Error:", e)


# ==========================================
# LISTEN FUNCTION
# ==========================================

from config import MIC_DEVICE_INDEX


def listen(device_index=MIC_DEVICE_INDEX):
    """
    Listen through microphone and
    convert user's speech into text.
    """

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone(device_index=device_index) as source:

            print("\nListening...")

            # Adjust microphone for background noise
            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            # Speech settings
            recognizer.pause_threshold = 1

            # Wait for user
            try:
                audio = recognizer.listen(
                    source,
                    timeout=8,
                    phrase_time_limit=12
                )

            except sr.WaitTimeoutError:
                print("No voice detected.")
                return ""

        # ==========================================
        # SPEECH TO TEXT
        # ==========================================

        try:
            command = recognizer.recognize_google(audio)
            print(f"\nYou: {command}")
            return command.lower().strip()

        except sr.UnknownValueError:
            print("Alexa: Sorry, I couldn't understand you.")
            return ""

        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")
            return ""

    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(f"Microphone Error: {e}")
        return ""