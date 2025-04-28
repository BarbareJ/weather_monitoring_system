from src.station.wind_speed_alert import WindSpeedAlert
from _pytest.capture import CaptureFixture


def test_wind_speed_alert_no_alert(capsys: CaptureFixture[str]) -> None:
    alert = WindSpeedAlert()
    alert.update(25.0, 60.0, 10.0)
    # alert.update(25.0, 60.0, 12.0)
    captured = capsys.readouterr()
    assert "**Alert!" not in captured.out


def test_wind_speed_alert_with_alert(capsys: CaptureFixture[str]) -> None:
    alert = WindSpeedAlert()
    alert.update(25.0, 60.0, 10.0)
    alert.update(25.0, 60.0, 15.0)
    captured = capsys.readouterr()
    assert "**Alert! Wind speed is increasing: 10.0 km/h → 15.0 km/h**" in captured.out