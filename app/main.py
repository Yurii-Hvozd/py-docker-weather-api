import os

import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": api_key,
        "q": "Paris",
    }

    response = requests.get(url, params=params)

    data = response.json()

    print(data)


if __name__ == "__main__":
    get_weather()
