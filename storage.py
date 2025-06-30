import json
import os
from datetime import datetime

DATA_DIR = "data"

def save_weather_data(city, data):
    os.makedirs(DATA_DIR, exist_ok=True)
    filename = os.path.join(DATA_DIR, f"{city.lower().replace(' ', '_')}.json")
    entry = {
        "timestamp": datetime.now().isoformat(),
        "weather": data
    }

    if os.path.exists(filename):
        with open(filename, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(entry)

    with open(filename, "w") as f:
        json.dump(history, f, indent=4)
