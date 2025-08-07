import os
import requests

def get_weather():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set!")

    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching weather: {response.text}")

    data = response.json()
    location = data["location"]["name"]
    country = data["location"]["country"]
    local_time = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{location}/{country} {local_time} Weather: {temp_c} Celsius, {condition}")

if __name__ == "__main__":
    get_weather()

