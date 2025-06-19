import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from backend.forecast import load_data, simple_forecast


def test_forecast_length():
    data = load_data(Path(__file__).resolve().parent.parent / 'data' / 'synthetic_sales.csv')
    forecast = simple_forecast(data, periods=2)
    assert len(forecast) == 2
