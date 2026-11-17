import datetime
import webbrowser
import subprocess
import os


def execute_command(command):

    command = command.lower()

    # -----------------------
    # Time
    # -----------------------
    if "time" in command:
        return f"The time is {datetime.datetime.now().strftime('%I:%M %p')}"

    # -----------------------
    # Date
    # -----------------------
    elif "date" in command:
        return f"Today is {datetime.datetime.now().strftime('%d %B %Y')}"

    # -----------------------
    # Hello
    # -----------------------
    elif "hello" in command:
        return "Hello! How can I help you today?"

    # -----------------------
    # Name
    # -----------------------
    elif "your name" in command:
        return "I am your personal Alexa assistant."

    # -----------------------
    # Open Google
    # -----------------------
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    # -----------------------
    # Open YouTube
    # -----------------------
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    # -----------------------
    # Open Gmail
    # -----------------------
    elif "open gmail" in command:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail."

    # -----------------------
    # Open ChatGPT
    # -----------------------
    elif "open chatgpt" in command:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT."

    # -----------------------
    # Open Notepad
    # -----------------------
    elif "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad."

    # -----------------------
    # Open Calculator
    # -----------------------
    elif "open calculator" in command:
        os.system("calc")
        return "Opening Calculator."

    # -----------------------
    # Open Paint
    # -----------------------
    elif "open paint" in command:
        os.system("mspaint")
        return "Opening Paint."

    # -----------------------
    # Open VS Code
    # -----------------------
    elif "open vs code" in command or "open vscode" in command:
        subprocess.Popen(["code"])
        return "Opening Visual Studio Code."

    return None