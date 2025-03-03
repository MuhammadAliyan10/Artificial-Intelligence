import numpy as np
import pandas as pd


n_days = 30
days = np.arange(n_days)
prayer_time = np.zeros(n_days)


for i in range(n_days):
    if i < 5:
        prayer_time[i] = 20
    elif 5 <= i < 15:
        prayer_time[i] = 40
    elif 16 <= i < 25:
        prayer_time[i] = 50
    else:
        prayer_time[i] = 60


columns = ["days", "prayer_time"]
df = pd.DataFrame(list(zip(days, prayer_time)), columns=columns)


df.to_csv("prayer_time.csv", index=False)

print(df)
