# Alexa AI Voice Assistant

A modular, multi-mode voice assistant built with Python. It integrates offline wake word detection, speech recognition, local text-to-speech, and generative AI powered by the modern Google GenAI SDK.

---

## Features

- **Multi-Mode Operation**:
  - **Voice Mode**: Microphone-driven interaction using speech recognition (`SpeechRecognition`) with spoken audio responses.
  - **Text Mode**: Interactive terminal text interface while still speaking responses aloud (`pyttsx3`).
  - **Wake Word Mode**: Hands-free offline keyword spotting using `openWakeWord` ("Alexa"), automatic microphone handoff, audio confirmation ("Yes?"), followed by command execution.
- **AI Intelligence**:
  - Integrated with Gemini using the new `google.genai` SDK (`gemini-3.5-flash-lite` / `gemini-3.8-flash`).
  - Includes exponential backoff and retry handling for transient API issues (e.g., 503 high-demand or rate spikes).
- **Personal Memory System**:
  - Persistent memory storage (`remember` / `recall`) for user-specific key-value facts (e.g., *"remember my favorite color is blue"* $\rightarrow$ *"what is my favorite color?"*).
- **Desktop & System Commands**:
  - Common desktop utilities including telling the time/date, launching Google, YouTube, Gmail, Notepad, Calculator, Paint, and Visual Studio Code.
- **Configurable Audio Pipeline**:
  - Configurable input device selection (`MIC_DEVICE_INDEX`) and standalone diagnostic tools to test microphone hardware, energy thresholds, and speech recognition reliability.

---

## Technologies Used

- **Language**: Python 3.10+
- **AI / LLM**: `google-genai` (Google Gemini API)
- **Wake Word Engine**: `openWakeWord` + `onnxruntime` + `numpy` (Local ONNX model inference)
- **Speech-to-Text (STT)**: `SpeechRecognition` (Google Web Speech API backend)
- **Text-to-Speech (TTS)**: `pyttsx3` (Offline Windows SAPI5 synthesizer)
- **Audio I/O**: `PyAudio`

---

## Project Structure

```
Alexa/
├── assistant.py          # Main application entry point and interactive menu loop
├── ai.py                 # Gemini AI client and retry logic (google.genai SDK)
├── brain.py              # Central command router (memory, desktop commands, AI)
├── commands.py           # Predefined desktop commands and application openers
├── config.py             # Environment configuration (API keys, models, mic index)
├── learn.py              # Persistent user memory store (remember / recall)
├── voice.py              # Audio input (listen) and output (speak) functions
├── wake_word.py          # Offline wake word detector ("Alexa") via openWakeWord
├── knowledge.json        # Local fallback knowledge base
├── memory.json           # User facts and remembered values (ignored by git)
├── history.json          # Interaction history cache (ignored by git)
├── test_microphone.py    # Diagnostic tool to test audio inputs and speech recognition
├── test_wake_word.py     # Standalone tester for wake word detection
├── requirements.txt      # Project dependencies
├── .env.example          # Template for environment variables
└── README.md             # Project documentation
```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Alexa
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Windows (CMD):
.\venv\Scripts\activate.bat
# Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

> **Note on Windows Dependencies**: `openwakeword` and `onnxruntime` require compatible binary wheels. Pinning `numpy==1.26.4` and `onnxruntime==1.17.3` ensures seamless C-API compatibility on Windows 64-bit.

### 4. Configure Environment Variables
Copy the example environment file to `.env`:
```bash
copy .env.example .env
```
Open `.env` and configure your settings:
```ini
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.5-flash-lite
MIC_DEVICE_INDEX=
```
- Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/).
- `MIC_DEVICE_INDEX` can be left blank to use your system's default microphone, or set to a specific device index identified by `test_microphone.py`.

---

## Running Alexa

Start the assistant by executing `assistant.py`:
```bash
python assistant.py
```

You will see the main menu:
```text
====================================
        ALEXA AI ASSISTANT
====================================
1. Voice Mode
2. Text Mode
3. Wake Word Mode
4. Exit
====================================
Enter your choice:
```

### Mode Descriptions

#### 1. Voice Mode
- Continually listens through your microphone using `SpeechRecognition`.
- Converts spoken audio to text, queries the command dispatcher/Gemini, and reads the response aloud using `pyttsx3`.
- Say `"exit"`, `"quit"`, `"stop"`, or `"back"` to return to the main menu.

#### 2. Text Mode (Speak Mode)
- Type questions and commands directly into the terminal prompt.
- Alexa processes queries through memory or Gemini, prints the reply, and simultaneously speaks the answer aloud.
- Type `exit` to return to the main menu.

#### 3. Wake Word Mode
- Runs an idle, low-overhead local listener waiting for the keyword **"Alexa"** using `openWakeWord`.
- When "Alexa" is recognized:
  1. Alexa chimes and speaks `"Yes?"`.
  2. The wake word audio stream is released cleanly.
  3. The microphone opens for your voice command.
  4. Alexa processes the command, speaks the answer aloud, and resumes waiting for the next "Alexa".
- Press `Ctrl+C` or say `"exit"` to return cleanly to the main menu.

---

## Diagnostic & Testing Tools

- **Test Microphone**: Inspect all available audio inputs, default devices, sample rates, and verify speech capture:
  ```bash
  python test_microphone.py
  ```
- **Test Wake Word**: Test keyword detection in isolation without launching the full assistant:
  ```bash
  python test_wake_word.py
  ```

---

## License

This project is licensed under the MIT License.
