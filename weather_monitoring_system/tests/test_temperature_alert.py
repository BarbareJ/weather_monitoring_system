from src.station.temperature_alert import TemperatureAlert
from _pytest.capture import CaptureFixture


def test_temperature_alert_no_alert(capsys: CaptureFixture[str]) -> None:
    alert = TemperatureAlert(threshold=30.0)
    alert.update(25.0, 60.0, 10.0)
    captured = capsys.readouterr()
    assert "**Alert!" not in captured.out


def test_temperature_alert_with_alert(capsys: CaptureFixture[str]) -> None:
    alert = TemperatureAlert(threshold=30.0)
    alert.update(35.0, 60.0, 10.0)
    captured = capsys.readouterr()
    assert "**Alert! Temperature exceeded 30.0°C: 35.0°C**" in captured.out