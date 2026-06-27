import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"


def fetch_data(endpoint, params):
    try:
        response = requests.get(
            f"{BASE_URL}/{endpoint}",
            params=params,
            timeout=10
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException:
        return None


def get_current_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    return fetch_data("weather", params)


def get_forecast(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    return fetch_data("forecast", params)


def get_air_quality(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY
    }

    return fetch_data("air_pollution", params)


def is_api_key_available():
    return bool(API_KEY)