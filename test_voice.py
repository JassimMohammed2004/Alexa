from voice import speak, listen

speak("Hello! I am Alexa.")

while True:

    command = listen()

    if command:
        speak(f"You said {command}")

    if command == "exit":
        speak("Goodbye!")
        break