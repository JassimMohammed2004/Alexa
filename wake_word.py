"""
wake_word.py
Independent Wake Word Detection Module for Alexa using openWakeWord.
"""

import sys
import numpy as np
import pyaudio
from openwakeword.model import Model
from config import MIC_DEVICE_INDEX

# Audio stream configuration
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK_SIZE = 1280  # 80ms at 16kHz, required frame size for openWakeWord
WAKE_WORD_NAME = "alexa"
DEFAULT_THRESHOLD = 0.5


def wait_for_wake_word(threshold=DEFAULT_THRESHOLD, device_index=MIC_DEVICE_INDEX):
    """
    Blocks and continuously listens to the microphone until the wake word
    'Alexa' is detected with a confidence above the threshold.

    Returns:
        True: When the wake word is detected.
        False: If listening was interrupted (e.g., Ctrl+C) or an error occurred.
    """
    audio = None
    stream = None

    try:
        # 1. Load the openWakeWord model for 'alexa' using ONNX runtime
        oww_model = Model(
            wakeword_models=[WAKE_WORD_NAME],
            inference_framework="onnx"
        )
    except Exception as e:
        print(f"Error loading openWakeWord model: {e}")
        return False

    try:
        # 2. Initialize PyAudio stream
        audio = pyaudio.PyAudio()
        stream_kwargs = {
            "format": FORMAT,
            "channels": CHANNELS,
            "rate": RATE,
            "input": True,
            "frames_per_buffer": CHUNK_SIZE
        }
        if device_index is not None:
            stream_kwargs["input_device_index"] = device_index

        stream = audio.open(**stream_kwargs)
    except Exception as e:
        print(f"Error initializing microphone stream: {e}")
        if audio is not None:
            audio.terminate()
        return False

    try:
        # 3. Continuous frame capture & prediction loop
        while True:
            # Read 16-bit PCM chunk from mic
            raw_data = stream.read(CHUNK_SIZE, exception_on_overflow=False)

            # Convert binary audio buffer to int16 numpy array
            audio_data = np.frombuffer(raw_data, dtype=np.int16)

            # Feed to model and retrieve prediction scores
            prediction = oww_model.predict(audio_data)

            # Check if 'alexa' score meets or exceeds the threshold
            score = prediction.get(WAKE_WORD_NAME, 0.0)
            if score >= threshold:
                return True

    except KeyboardInterrupt:
        # Handle user termination gracefully
        return False
    except Exception as e:
        print(f"Error during wake word detection: {e}")
        return False
    finally:
        # 4. Clean up audio resources safely
        if stream is not None:
            try:
                stream.stop_stream()
                stream.close()
            except Exception:
                pass
        if audio is not None:
            try:
                audio.terminate()
            except Exception:
                pass
