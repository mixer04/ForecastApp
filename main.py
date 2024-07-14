import requests
from datetime import datetime, timedelta

api_key = "" # TODO: API key

print("Welcome to the ForecastApp")

city_name = input("City: ").split() # user input is split into separate words
city_name = " ".join(word.capitalize() for word in city_name) # if the city name has 2 or more words, each word is capitalized

if city_name != None:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:  # checks if the city exists in the database
        temperature = data['main']['temp']
        feels_like_temperature = data['main']['feels_like']
        pressure = data['main']['pressure']
        visibility = data['visibility'] / 1000  # converting meters to kilometers
        clouds = data['clouds']['all']
        weather_description = data['weather'][0]['description']
        wind = data['wind']['speed']
        humidity = data['main']['humidity']
        print("1. Simple forecast")
        print("2. Detailed forecast")
        mode = input("Choose display mode: ")
        if mode == "1":
            print(f"\nWeather in {city_name}:\n")
            print(f"Temperature: {temperature} C")
            print(f"Description: {weather_description}")
            print(f"Wind: {wind} m/s")
            print("\n")
        elif mode == "2":
            print(f"\nWeather in {city_name}:\n")
            print(f"Temperature: {temperature} C (feels like {feels_like_temperature} C)")
            print(f"Description: {weather_description}")
            print(f"Wind: {wind} m/s")
            print(f"Humidity: {humidity}%")
            print(f"Pressure: {pressure} hPa")
            if visibility >= 10.0:     
                print(f"Visibility: more than {visibility} km")
            else:
                print(f"Visibility: {visibility} km")
            print(f"Clouds: {clouds}%")
            print("\n")
    else:
        print("City not found, try again.")
else: 
    raise ValueError("Invalid city")