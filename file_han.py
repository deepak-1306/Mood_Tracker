import json
import os

file_name = "mood_data.json"

def create_file():
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            json.dump([], file)

def save_entry(date, mood, stress, note):

    entry = {
        "date": str(date),
        "mood": mood,
        "stress": stress,
        "note": note
    }

    with open(file_name, "r") as file:
        data = json.load(file)

    data.append(entry)

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def read_data():

    try:
        with open(file_name, "r") as file:
            data = json.load(file)
        return data
    except:
        return None

