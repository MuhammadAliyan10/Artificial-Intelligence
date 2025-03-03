import numpy as np
import pandas as pd

n_days = 30

days = np.arange(1, n_days + 1)
temperature = np.random.uniform(25, 40, size=n_days)
n_fasters = np.random.randint(3, 9, size=n_days)
is_weekend = np.array([1 if n in [6, 7, 13, 14, 20, 21, 27, 28] else 0 for n in days])
base_usage = 2 * temperature + 3 * n_fasters + 20 * is_weekend

outlier_mask = np.random.rand(n_days) < 0.1
water_usage = base_usage.copy()
water_usage[outlier_mask] *= 2

water_usage = water_usage + np.random.uniform(-30, 30, size=n_days)
water_usage = np.maximum(water_usage, 5)


df = pd.DataFrame(
    {
        "days": days,
        "temperature": temperature,
        "number_of_fasters": n_fasters,
        "is_weekend": is_weekend,
        "water_usage": water_usage,
    }
)


df.to_csv("daily_water_usage.csv", index=False)
