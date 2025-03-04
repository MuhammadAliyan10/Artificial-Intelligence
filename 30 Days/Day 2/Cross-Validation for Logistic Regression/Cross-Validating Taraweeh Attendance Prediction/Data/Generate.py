import numpy as np
import pandas as pd

n_days = 20
days = np.arange(1, n_days + 1)
tiredness = np.random.uniform(0, 10, size=n_days)
temperature = np.random.uniform(20, 40, size=n_days)
attend_mask = (tiredness < 5) & (temperature < 35)
attend_base = np.where(attend_mask, 1, 0)
attend = np.where(np.random.rand(n_days) < 0.9, attend_base, 1 - attend_base)


df = pd.DataFrame(
    {"days": days, "tiredness": tiredness, "temperature": temperature, "attend": attend}
)

df.to_csv("taraweeh.csv", index=False)
