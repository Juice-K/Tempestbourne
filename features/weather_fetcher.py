# Weather Fetcher
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
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
