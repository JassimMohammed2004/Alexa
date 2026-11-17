from commands import execute_command
from ai import ask_ai
from learn import remember, recall


def process_command(command):

    command = command.lower()

    if command.startswith("remember my"):

        data = command.replace("remember my", "").strip()

        if " is " in data:
            key, value = data.split(" is ", 1)
            return remember(key.strip(), value.strip())

    elif command.startswith("what is my"):

        key = command.replace("what is my", "").strip()

        if key.endswith("?"):
            key = key[:-1]

        return recall(key)

    elif "open chrome" in command:

        return execute_command(command)

    else:

        return ask_ai(command)