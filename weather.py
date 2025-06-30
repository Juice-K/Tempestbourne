import requests

API_KEY = "5bf329464f3b0c878c8eb1846b65c08e"  # Replace this with your OpenWeatherMap key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_current_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        raise Exception("City not found or API error.")
    
    return response.json()
