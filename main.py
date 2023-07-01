import requests
import time

api_key = "2b31fe111d8c6a2c08e2a316edd08b32"

def get_location_key(city, state, country):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={api_key}")
    response = response.json()
    if response == []:
        return -1, -1
    lat = response[0]["lat"]
    long = response[0]["lon"]
    return lat, long
    
def get_weather_json(lat, long):
    
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={api_key}&units=imperial")
    
    return response.json()

def get_greeting(hour):
    if hour >= 2 and hour < 5:
        return "Hello!"
    elif hour >= 5 and hour < 12:
        return "Good morning!"
    elif hour >=12 and hour < 18:
        return "Good afternoon!"
    elif hour >= 18 or hour < 2:
        return "Good evening!"

def main():
    current_time = time.strftime("%H:%M:%S")
    hour = int(current_time[0:2])
    
    city = input("Enter city name (required): ")
    state = input("Enter state name (required for USA): ")
    country = input("Enter country name (required): ")
    lat, long = get_location_key(city, state, country)
    if lat == -1 and long == -1:
        raise Exception("Invalid Input")
    
    weather_json = get_weather_json(lat, long)
    
    hour = int(current_time[0:2])
    greeting = get_greeting(hour)
    temperature = str(round(weather_json["list"][0]["main"]["temp"], 2)) + u"\N{DEGREE SIGN}" + "F"
    feels_like = str(round(weather_json["list"][0]["main"]["feels_like"], 2)) + u"\N{DEGREE SIGN}" + "F"
    weather =  weather_json["list"][0]["weather"][0]["description"]

    response = f"{greeting} The temperature is {temperature} in {city}, and it feels like {feels_like} with {weather}. Have a great day!"
    print(response)

if __name__ == "__main__":
    main()