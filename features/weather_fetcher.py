# Weather Fetcher
import os
import requests
import random
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("5bf329464f3b0c878c8eb1846b65c08e")
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_forecast_weather(city, date_str, time_str):
    """
    Fetch the closest matching forecast for a given city, date (YYYY-MM-DD), and time (HH:MM).
    """
    target_dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"API error: {response.json().get('message', 'Unknown error')}")

    data = response.json()
    forecasts = data.get("list", [])

    closest_forecast = min(
        forecasts,
        key=lambda x: abs(datetime.strptime(x["dt_txt"], "%Y-%m-%d %H:%M:%S") - target_dt)
    )

    return closest_forecast

def get_weather_data_for_city(city, datetime_str):
    """
    Wrapper for main.py — takes a single datetime string and splits it.
    """
    date_str, time_str = datetime_str.split()
    return get_forecast_weather(city, date_str, time_str)

CITY_POOL = [
    "Tokyo", "Paris", "Cairo", "São Paulo", "Bangkok",
    "New York", "Moscow", "Reykjavik", "Toronto", "Sydney",
    "Cape Town", "Mumbai", "Istanbul", "Oslo", "Buenos Aires"
]

def get_random_city(exclude=None):
    """
    Picks a random city not equal to 'exclude'.
    """
    choices = [city for city in CITY_POOL if city.lower() != exclude.lower()]
    return random.choice(choices)
