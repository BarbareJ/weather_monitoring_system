from .weather_observer import WeatherObserver


class WeatherDisplay(WeatherObserver):
    def update(self, temperature: float, humidity: float, wind_speed: float) -> None:
        print(
            f"WeatherDisplay: Showing Temperature = {temperature}°C, "
            f"Humidity = {humidity}%, Wind Speed = {wind_speed} km/h"
        )