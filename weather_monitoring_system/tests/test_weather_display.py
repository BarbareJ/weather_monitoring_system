from src.station.weather_display import WeatherDisplay
from _pytest.capture import CaptureFixture


def test_weather_display_update(capsys: CaptureFixture[str]) -> None:
    display = WeatherDisplay()
    display.update(25.0, 60.0, 10.0)
    captured = capsys.readouterr()
    expected_output = (
        "WeatherDisplay: Showing Temperature = 25.0°C, "
        "Humidity = 60.0%, Wind Speed = 10.0 km/h"
    )
    assert expected_output in captured.out