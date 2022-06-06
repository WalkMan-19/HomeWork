import json


def load_json():
    with open('candidates.json', 'r', encoding="utf-8") as f:
        candidates_info = json.load(f)
        return candidates_info
