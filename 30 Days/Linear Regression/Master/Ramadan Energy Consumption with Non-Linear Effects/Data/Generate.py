import numpy as np
import pandas as pd


n_days = 30


days = np.arange(1, n_days + 1)
temperature = np.random.uniform(25, 40, size=n_days)
n_people = np.random.randint(3, 10, size=n_days)
cooking_hours = np.random.uniform(1, 4, size=n_days)
high_temp_flag = np.array([1 if t > 35 else 0 for t in temperature])


base_usage = 5 * temperature + 2 * n_people + 10 * cooking_hours + 50 * high_temp_flag


outlier_mask = np.random.rand(n_days) < 0.05
energy_usage = base_usage.copy()
energy_usage[outlier_mask] *= 3


energy_usage = energy_usage + np.random.uniform(-20, 20, size=n_days)
energy_usage = np.maximum(energy_usage, 5)


df = pd.DataFrame(
    {
        "days": days,
        "temperature": temperature,
        "number_of_people": n_people,
        "cooking_hours": cooking_hours,
        "high_temp_flag": high_temp_flag,
        "energy_consumption": energy_usage,
    }
)


df.to_csv("ramadan_energy_consumption.csv", index=False)


print(df.head())
