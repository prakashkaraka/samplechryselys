import random
from typing import List, Dict


def simulate_what_if(base_forecast: List[Dict[str, float]], shock: float = 0.1):
    """Generate simple what-if scenario by applying random noise."""
    simulated = []
    for row in base_forecast:
        noise = random.uniform(-shock, shock) * row['Forecast']
        simulated.append({
            'Date': row['Date'],
            'Simulated': round(row['Forecast'] + noise, 2)
        })
    return simulated
