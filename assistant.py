import time
from voice import listen, speak
from brain import process_command
from wake_word import wait_for_wake_word


def voice_mode():
    """Voice Mode"""

    print("\n================================")
    print("        VOICE MODE")
    print("================================")

    speak("Voice mode activated. How can I help you?")

    while True:

        command = listen()

        if not command:
            continue

        command = command.lower()

        if command in ["exit", "quit", "stop", "back"]:
            speak("Returning to main menu.")
            break

        try:
            response = process_command(command)

            if response:
                speak(response)
            else:
                speak("Sorry, I didn't understand.")

        except Exception as e:
            print("Error:", e)
            speak("Sorry, something went wrong.")


def text_mode():
    """Text Mode (AI still speaks)"""

    print("\n================================")
    print("         TEXT MODE")
    print("================================")

    speak("Text mode activated. Type your question.")

    while True:

        command = input("\nYou: ").strip()

        if command == "":
            continue

        command = command.lower()

        if command in ["exit", "quit", "stop", "back"]:
            speak("Returning to main menu.")
            break

        try:
            response = process_command(command)

            if response:
                # speak() prints and speaks the response
                speak(response)

            else:
                speak("Sorry, I couldn't answer that.")

        except Exception as e:
            print("Error:", e)
            speak("Sorry, something went wrong.")


def wake_word_mode():
    """Wake Word Mode"""

    print("\n================================")
    print("      WAKE WORD MODE")
    print("================================")

    speak("Wake word mode activated. Say Alexa to begin.")
    print("Waiting for wake word 'Alexa'... (Press Ctrl+C to return to main menu)")

    try:
        while True:
            print("\nListening for 'Alexa'...")
            detected = wait_for_wake_word()

            if not detected:
                # wait_for_wake_word returns False on interrupt or mic error
                break

            print("\n>>> Wake word 'Alexa' detected! <<<")
            speak("Yes?")
            time.sleep(0.2)

            command = listen()

            if not command:
                continue

            command = command.lower()

            if command in ["exit", "quit", "stop", "back"]:
                speak("Returning to main menu.")
                break

            try:
                response = process_command(command)

                if response:
                    speak(response)
                else:
                    speak("Sorry, I didn't understand.")

            except Exception as e:
                print("Error:", e)
                speak("Sorry, something went wrong.")

    except KeyboardInterrupt:
        print("\nReturning to main menu.")
        speak("Returning to main menu.")
    except Exception as e:
        print("Wake Word Mode Error:", e)
        speak("Sorry, something went wrong.")


def main():

    speak("Welcome to Alexa AI Assistant.")

    while True:

        print("\n====================================")
        print("        ALEXA AI ASSISTANT")
        print("====================================")
        print("1. Voice Mode")
        print("2. Text Mode")
        print("3. Wake Word Mode")
        print("4. Exit")
        print("====================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            voice_mode()

        elif choice == "2":
            text_mode()

        elif choice == "3":
            wake_word_mode()

        elif choice == "4":
            speak("Goodbye. Have a nice day.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
            speak("Please choose a valid option.")


if __name__ == "__main__":
    main()