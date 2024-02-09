import requests

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Check for errors in the HTTP response
          
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def display_weather_info(self, weather_data):
        if weather_data:
            print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Description: {weather_data['weather'][0]['description']}")
            print(f"Humidity: {weather_data['main']['humidity']}%")
            print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        else:
            print("Failed to fetch weather data.")

if __name__ == "__main__":
    api_key = "6012ded6d7fc3dbeaf9d4c38690672ca"

    cities_to_check = ["Mumbai", "Mount Abu", "Noida" , "madison"]

    weather_fetcher = WeatherFetcher(api_key)

    for city in cities_to_check:
        print("\n------------------------")
        print(f"Fetching weather for {city}...")
        weather_data = weather_fetcher.fetch_weather(city)
        weather_fetcher.display_weather_info(weather_data)
