"""
test_wake_word.py
Standalone test script to verify wake word detection.
"""

import sys
from wake_word import wait_for_wake_word


def main():
    print("====================================")
    print("       WAKE WORD TEST STARTED       ")
    print("====================================")
    print("Listening for wake word...")
    print("Say 'Alexa' clearly into your microphone.")
    print("(Press Ctrl+C to stop the test)\n")

    try:
        detected = wait_for_wake_word()
        if detected:
            print("\n>>> Wake word detected! <<<")
            print("Test successful. Exiting cleanly.")
        else:
            print("\nListening stopped without detection.")
    except KeyboardInterrupt:
        print("\nTest cancelled by user (Ctrl+C).")
    except Exception as e:
        print(f"\nUnexpected test error: {e}")


if __name__ == "__main__":
    main()
