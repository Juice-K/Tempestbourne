# Local Db
import json
import os
from datetime import datetime

DATA_DIR = "data"

def _get_filename(city):
    """Returns a safe filename for storing city-based weather data."""
    return os.path.join(DATA_DIR, f"{city.lower().replace(' ', '_')}.json")

def save_weather_data(city, data):
    """Appends a new weather entry to the city's weather history file."""
    os.makedirs(DATA_DIR, exist_ok=True)
    filename = _get_filename(city)

    entry = {
        "timestamp": datetime.now().isoformat(),
        "weather": data
    }

    history = []
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                history = json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️ Warning: Malformed JSON in {filename}. Starting fresh.")

    history.append(entry)

    with open(filename, "w") as f:
        json.dump(history, f, indent=4)

def load_weather_history(city):
    """Loads all weather history entries for a city."""
    filename = _get_filename(city)
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return json.load(f)
