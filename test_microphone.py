"""
test_microphone.py
Microphone diagnostics and testing tool for Alexa.
"""

import pyaudio
import speech_recognition as sr

def list_microphones():
    p = pyaudio.PyAudio()
    print("=" * 60)
    print("AVAILABLE AUDIO INPUT DEVICES (PyAudio)")
    print("=" * 60)
    default_dev = p.get_default_input_device_info()
    print(f"Default Input Device: Index {default_dev['index']} -> {default_dev['name']}\n")

    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        if dev.get('maxInputChannels', 0) > 0:
            is_default = " [DEFAULT]" if i == default_dev['index'] else ""
            print(f"Index {i:2d}: {dev['name']}{is_default}")
            print(f"          Channels: {dev['maxInputChannels']}, Rate: {dev['defaultSampleRate']} Hz, HostApi: {dev['hostApi']}")

    p.terminate()

    print("\n" + "=" * 60)
    print("SPEECHRECOGNITION MICROPHONE NAMES")
    print("=" * 60)
    for idx, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"SR Index {idx:2d}: {name}")

def test_microphone_listen(device_index=None):
    print("\n" + "=" * 60)
    print(f"TESTING SPEECH RECOGNITION (Device Index: {device_index})")
    print("=" * 60)
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone(device_index=device_index) as source:
            print("Calibrating ambient noise (0.5s)...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print(f"Energy threshold set to: {recognizer.energy_threshold:.2f}")
            print("Please speak now (e.g. 'What is Python?')...")
            
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
                print(f"Audio captured! Data length: {len(audio.frame_data)} bytes")
            except sr.WaitTimeoutError:
                print("WaitTimeoutError: No voice detected within 5 seconds.")
                return

        print("Sending audio to Google Speech Recognition...")
        try:
            text = recognizer.recognize_google(audio)
            print(f"SUCCESS! Recognized: '{text}'")
        except sr.UnknownValueError:
            print("UnknownValueError: Audio captured, but speech could not be understood.")
        except sr.RequestError as e:
            print(f"RequestError: Service request failed: {e}")

    except Exception as e:
        print(f"Microphone Device Error: {e}")

if __name__ == "__main__":
    list_microphones()
    test_microphone_listen()
