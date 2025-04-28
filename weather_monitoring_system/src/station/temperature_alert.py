from .weather_observer import WeatherObserver


class TemperatureAlert(WeatherObserver):
    def __init__(self, threshold: float) -> None:
        self._threshold = threshold

    def update(self, temperature: float, humidity: float, wind_speed: float) -> None:
        if temperature > self._threshold:
            print(
                f"TemperatureAlert: **Alert! Temperature exceeded {self._threshold}°C: "
                f"{temperature}°C**"
            )