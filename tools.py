import json
import os

def get_scholarships():
    file_path = os.path.join(os.path.dirname(__file__), "scholarships.json")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data