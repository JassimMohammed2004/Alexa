import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 5

print("Recording... Speak now!")

recording = sd.rec(
    int(seconds * fs),
    samplerate=fs,
    channels=1,
    dtype="int16"
)

sd.wait()

write("voice.wav", fs, recording)

print("Recording saved as voice.wav")