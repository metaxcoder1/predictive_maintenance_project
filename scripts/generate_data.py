import pandas as pd
import numpy as np

data = {
    'temperature': np.random.normal(25, 5, 100),
    'voltage': np.random.normal(400, 20, 100),
    'current': np.random.normal(10, 2, 100),
    'humidity': np.random.normal(30, 5, 100),
    'power_output': np.random.normal(2000, 100, 100),
    'inverter_status': np.random.choice([0, 1], size=100, p=[0.95, 0.05]),
    'failure_status': np.random.choice([0, 1], size=100, p=[0.9, 0.1])
}

df = pd.DataFrame(data)
df.to_csv('../data/solar_power_data.csv', index=False)
print("Data generated and saved to data/solar_power_data.csv")
