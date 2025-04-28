from typing import List

from .weather_observer import WeatherObserver


class WeatherStation:
    def __init__(self) -> None:
        self._observers: List[WeatherObserver] = []
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._wind_speed: float = 0.0

    def add_observer(self, observer: WeatherObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: WeatherObserver) -> None:
        self._observers.remove(observer)

    def set_weather_data(
        self, temperature: float, humidity: float, wind_speed: float
    ) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._wind_speed = wind_speed
        self._notify_observers()

    def _notify_observers(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._wind_speed)