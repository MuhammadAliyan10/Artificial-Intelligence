import numpy as np
import pandas as pd

n_days = 30

days = np.arange(1, n_days + 1)
n_dishes = np.random.randint(2, 6, size=n_days)
n_helpers = np.random.randint(1, 4, size=n_days)

prep_time = 10 * n_dishes - 5 * n_helpers + np.random.uniform(-5, 5, size=n_days)


df = pd.DataFrame(
    {
        "days": days,
        "number_of_dishes": n_dishes,
        "number_of_helpers": n_helpers,
        "preparation_time": prep_time,
    }
)

df.to_csv("iftar_preparation_time.csv", index=False)
