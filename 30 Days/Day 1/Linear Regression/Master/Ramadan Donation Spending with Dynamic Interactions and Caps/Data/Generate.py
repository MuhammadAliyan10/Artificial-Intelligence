import numpy as np
import pandas as pd

n_days = 30

days = np.arange(1, n_days + 1)

daily_income = np.random.uniform(50, 250, size=n_days)
n_appeals = np.random.randint(1, 6, size=n_days)
is_friday = np.array([1 if n in [5, 12, 19, 26] else 0 for n in days])
days_until_eid = np.arange(29, -1, -1)
income_appeals_interaction = daily_income * n_appeals

base_donation = (
    0.15 * daily_income
    + 4 * n_appeals
    + 25 * is_friday
    + 0.5 * days_until_eid
    + 0.3 * income_appeals_interaction
)
burst_mask = (is_friday == 1) & (days_until_eid < 5) & (np.random.rand(n_days) < 0.1)
donation_spending = np.where(
    burst_mask,
    base_donation + np.random.uniform(50, 100, size=n_days),
    np.clip(base_donation, None, 100),
)
donation_spending = donation_spending + np.random.uniform(-15, 15, size=n_days)

df = pd.DataFrame(
    {
        "days": days,
        "daily_income": daily_income,
        "number_of_appeals": n_appeals,
        "is_friday": is_friday,
        "days_until_eid": days_until_eid,
        "income_appeals_interaction": income_appeals_interaction,
        "donation_spending": donation_spending,
    }
)

df.to_csv("ramadan_donation_spending.csv", index=False)

print(df.head())
