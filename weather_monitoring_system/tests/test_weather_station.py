from src.station import WeatherObserver, WeatherStation


class MockObserver(WeatherObserver):
    def __init__(self) -> None:
        self.updated = False

    def update(self, temperature: float, humidity: float, wind_speed: float) -> None:
        self.updated = True


def test_weather_station_add_observer() -> None:
    station = WeatherStation()
    observer = MockObserver()
    station.add_observer(observer)
    assert observer in station._observers


def test_weather_station_remove_observer() -> None:
    station = WeatherStation()
    observer = MockObserver()
    station.add_observer(observer)
    station.remove_observer(observer)
    assert observer not in station._observers


def test_weather_station_notify_observers() -> None:
    station = WeatherStation()
    observer = MockObserver()
    station.add_observer(observer)
    station.set_weather_data(25.0, 60.0, 10.0)
    assert observer.updated