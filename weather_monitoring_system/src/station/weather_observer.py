from abc import ABC, abstractmethod


class WeatherObserver(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, wind_speed: float) -> None:
        pass