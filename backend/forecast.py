import csv
from datetime import datetime, timedelta


def simple_forecast(data, periods=3):
    """Simple moving average forecast as a stand in for Prophet."""
    dates = [datetime.strptime(row['Date'], "%Y-%m-%d") for row in data]
    sales = [float(row['Sales']) for row in data]
    if not sales:
        return []
    avg_growth = (sales[-1] - sales[0]) / len(sales)
    last_date = dates[-1]
    last_value = sales[-1]
    forecast = []
    for _ in range(periods):
        last_date += timedelta(days=30)
        last_value += avg_growth
        forecast.append({'Date': last_date.strftime('%Y-%m-%d'), 'Forecast': round(last_value, 2)})
    return forecast


def load_data(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))

