from .weather_observer import WeatherObserver


class WindSpeedAlert(WeatherObserver):
    def __init__(self) -> None:
        self._previous_wind_speed: float | None = None

    def update(self, temperature: float, humidity: float, wind_speed: float) -> None:
        if (self._previous_wind_speed is not None
                and wind_speed > self._previous_wind_speed):
            print(
                f"WindSpeedAlert: **Alert! Wind speed is increasing: "
                f"{self._previous_wind_speed} km/h → {wind_speed} km/h**"
            )
        self._previous_wind_speed = wind_speed