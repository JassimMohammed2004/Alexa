import json


MEMORY_FILE = "memory.json"



def load_memory():

    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    except:
        return {}



def save_memory(memory):

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)



def remember(key, value):

    memory = load_memory()

    memory[key] = value

    save_memory(memory)

    return f"Okay, I'll remember that your {key} is {value}."



def recall(key):

    memory = load_memory()

    if key in memory:
        return f"Your {key} is {memory[key]}."

    else:
        return "I don't remember that yet."