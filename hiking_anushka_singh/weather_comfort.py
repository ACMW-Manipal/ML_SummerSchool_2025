import pandas as pd
import numpy as np

# Weather Data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Temperature': [25, 28, 30, 22, 26, 27, 24],
    'Humidity': [60, 55, 50, 70, 65, 60, 75],
    'Wind Speed': [15, 10, 20, 10, 8, 5, 12]
}

df = pd.DataFrame(data)

# Comfort Score formula
df['Comfort Score'] = df['Temperature'] * 0.4 + df['Humidity'] * 0.4 + df['Wind Speed'] * 0.2

# Find best day
best_day = df.loc[df['Comfort Score'].idxmin(), 'Day']

# Print results
print(df)
print(f"\n🏕️ Best day to go hiking: {best_day}")
