import numpy as np
import pandas as pd

n_mangoes = 20

total_mangoes = np.arange(n_mangoes)
price_per_mango = np.array([2 * x for x in total_mangoes])

columns = ["amount_mangoes", "price"]
df = pd.DataFrame(list(zip(total_mangoes, price_per_mango)), columns=columns)

df.to_csv("mango_prices.csv", index=False)
