import numpy as np
import pandas as pd

n_days = 30
n_cities = 10
n_rows = 30 * 10

city_id = np.repeat(np.arange(1, n_cities + 1), n_days)
days = np.tile(np.arange(1, n_days + 1), n_cities)
temperature = np.random.uniform(20, 45, size=n_rows)

prev_day_funds = np.zeros(n_rows)
for i in range(n_cities):
    start_idx = i * n_days
    end_idx = (i + 1) * n_days
    funds = np.random.randint(100, 1000, size=n_days)
    for j in range(1, n_days):
        if funds[j - 1] > 700 and np.random.rand() < 0.8:
            funds[j] = np.random.randint(700, 1000)
    prev_day_funds[start_idx:end_idx] = funds

n_volunteers = np.random.randint(5, 20, size=n_rows)
is_friday_base = np.zeros(n_days)
is_friday_base[[4, 11, 18, 25]] = 1
is_friday = np.tile(is_friday_base, n_cities)

success_condition = (temperature < 35) & (prev_day_funds > 500) & (n_volunteers > 10)
success_base = np.where(success_condition, 1, 0)
success = np.where(np.random.rand(n_rows) < 0.8, success_base, 1 - success_base)


df = pd.DataFrame(
    {
        "city_id": city_id,
        "days": days,
        "temperature": temperature,
        "prev_day_funds": prev_day_funds,
        "n_volunteers": n_volunteers,
        "is_friday": is_friday,
        "success": success,
    }
)
df.to_csv("donation_drive.csv", index=False)
