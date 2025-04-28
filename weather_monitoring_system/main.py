import random

from src.station import (
    HumidityAlert,
    TemperatureAlert,
    WeatherDisplay,
    WeatherStation,
    WindSpeedAlert,
)


def main() -> None:
    station = WeatherStation()
    display = WeatherDisplay()
    temperature_alert = TemperatureAlert(threshold=32.0)
    wind_speed_alert = WindSpeedAlert()
    humidity_alert = HumidityAlert(threshold=75.0)

    station.add_observer(display)
    station.add_observer(temperature_alert)
    station.add_observer(wind_speed_alert)
    station.add_observer(humidity_alert)

    for week in range(1, 21):
        print(f"\nWeek {week}:")
        temperature = random.uniform(20, 40)
        humidity = random.uniform(50, 90)
        wind_speed = random.uniform(5, 30)
        station.set_weather_data(temperature, humidity, wind_speed)


if __name__ == "__main__":
    main()