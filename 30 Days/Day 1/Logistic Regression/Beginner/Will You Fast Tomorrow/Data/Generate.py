import numpy as np
import pandas as pd

np.random.seed(42)
n_days = 30

days = np.arange(1, n_days + 1)
tiredness = np.random.uniform(0, 10, size=n_days)
prayer_time = np.random.uniform(15, 60, size=n_days)
hydration = np.random.uniform(0, 10, size=n_days)
temperature = np.random.uniform(20, 45, size=n_days)
is_friday = np.array([1 if n in [5, 12, 19, 26] else 0 for n in days])
days_until_eid = np.arange(29, -1, -1)

fast_condition = (
    (tiredness < 6) & (prayer_time < 45) & (hydration > 5) & (temperature < 40)
)
fast_base = np.where(fast_condition, 1, 0)
fast = np.where(np.random.rand(n_days) < 0.9, fast_base, 1 - fast_base)
friday_eid_mask = (
    (is_friday == 1) & (days_until_eid < 5) & (np.random.rand(n_days) < 0.05)
)
fast = np.where(friday_eid_mask, 0, fast)

df = pd.DataFrame(
    {
        "days": days,
        "tiredness": tiredness,
        "prayer_time": prayer_time,
        "hydration": hydration,
        "temperature": temperature,
        "is_friday": is_friday,
        "days_until_eid": days_until_eid,
        "fast": fast,
    }
)

df.to_csv("fasting_success_one_person.csv", index=False)
print(df.head())
