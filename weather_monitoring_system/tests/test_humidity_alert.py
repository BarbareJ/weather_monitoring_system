from _pytest.capture import CaptureFixture
from src.station import HumidityAlert


def test_humidity_alert_no_alert(capsys: CaptureFixture[str]) -> None:
    alert = HumidityAlert(threshold=80.0)
    alert.update(25.0, 75.0, 10.0)
    captured = capsys.readouterr()
    assert "**Alert!" not in captured.out


def test_humidity_alert_with_alert(capsys: CaptureFixture[str]) -> None:
    alert = HumidityAlert(threshold=80.0)
    alert.update(25.0, 85.0, 10.0)
    captured = capsys.readouterr()
    assert "**Alert! Humidity exceeded 80.0%: 85.0%**" in captured.out