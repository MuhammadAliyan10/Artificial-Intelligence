import pandas as pd
import numpy as np

n_days = 100
days = np.arange(1, n_days + 1)
tiredness = np.random.uniform(0, 10, size=n_days)
prayer_time = np.random.uniform(15, 60, size=n_days)
temperature = np.random.uniform(20, 50, size=n_days)
hydration = np.random.uniform(0, 10, size=n_days)

success_condition = (
    (tiredness < 7) & (prayer_time < 50) & (temperature < 40) & (hydration > 4)
)
fast_base = np.where(success_condition, 1, 0)
fast = np.where(np.random.rand(n_days) < 0.95, fast_base, 1 - fast_base)
heat_mask = (temperature > 45) & (np.random.rand(n_days) < 0.2)
fast = np.where(heat_mask, 0, fast)

df = pd.DataFrame(
    {
        "days": days,
        "tiredness": tiredness,
        "prayer_time": prayer_time,
        "temperature": temperature,
        "hydration": hydration,
        "fast": fast,
    }
)
df.to_csv("fasting_failures_extreme.csv", index=False)
