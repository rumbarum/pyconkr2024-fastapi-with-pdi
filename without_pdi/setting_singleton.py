import json

def get_setting() -> dict:
    with open("config.json") as f:
        setting = json.load(f)
    return setting

setting = get_setting()
