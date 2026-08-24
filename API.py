import requests

cities = {
    "malmö": (55.6, 13.0),
    "stockholm": (59.3, 18.1),
    "göteborg": (57.7, 12.0),
    "london": (51.5, -0.1),
    "paris": (48.9, 2.3)
}

city = input("Which city? ").lower()
if city in cities:
    lat, lon = cities[city]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    current = data["current_weather"]
    temperature = current["temperature"]
    windspeed = current["windspeed"]
    winddirection = current["winddirection"]
    print("Current weather in", city)
    print("Temperature:", current["temperature"], "°C")
    print("Wind speed:", current["windspeed"], "km/h")
    print("Wind direction:", current["winddirection"], "°")
else:
    print("City not found. Try Malmö, Stockholm, Göteborg, London, or Paris.")