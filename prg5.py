import requests

def get_weather(city):
    API_KEY = "your_api_key_here"  # Replace with your real API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print("City not found.")
    else:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        print(f"Weather in {city}: {temp}°C, {desc}")

city = input("Enter a city name: ")
get_weather(city)
