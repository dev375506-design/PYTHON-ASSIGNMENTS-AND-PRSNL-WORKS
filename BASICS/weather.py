import requests

def get_coordinates(city):
   
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=5" #enter you free weather website url
    response = requests.get(geo_url)

    if response.status_code == 200:
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            print("\n🔎 Multiple matches found:")
            for i, result in enumerate(data["results"]):
                print(f"{i+1}. {result['name']}, {result['country']} (lat: {result['latitude']}, lon: {result['longitude']})")

            choice = int(input("Enter the number of your city: ")) - 1
            result = data["results"][choice]
            return result["latitude"], result["longitude"], result["name"], result["country"]
        else:
            print("❌ City not found! ;(")
            return None
    else:
        print("⚠️ Error fetching coordinates:", response.status_code, response.text)
        return None


def get_weather(lat, lon, city_name, country):
    """Fetch current weather using Open-Meteo Weather API"""
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(weather_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["current_weather"]
        print(f"\n📍 Weather in {city_name}, {country}")
        print(f"🌡 Temperature: {weather['temperature']}°C")
        print(f"💨 Windspeed: {weather['windspeed']} km/h")
        print(f"⏱ Time: {weather['time']}")
    else:
        print("⚠️ Error fetching weather:", response.status_code, response.text)


city = input("Enter city name: ")
coords = get_coordinates(city)

if coords:
    lat, lon, city_name, country = coords
    get_weather(lat, lon, city_name, country)
