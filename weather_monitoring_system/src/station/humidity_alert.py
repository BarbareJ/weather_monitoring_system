from .weather_observer import WeatherObserver


class HumidityAlert(WeatherObserver):
    def __init__(self, threshold: float) -> None:
        self._threshold = threshold

    def update(self, temperature: float, humidity: float, wind_speed: float) -> None:
        if humidity > self._threshold:
            print(
                f"HumidityAlert: **Alert! Humidity exceeded {self._threshold}%: "
                f"{humidity}%**"
            )