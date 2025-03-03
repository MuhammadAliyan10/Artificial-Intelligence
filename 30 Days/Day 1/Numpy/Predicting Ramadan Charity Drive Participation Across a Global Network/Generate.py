import numpy as np
import pandas as pd

n_cities = 30
n_volunteers = 50
n_days = 30
total_rows = n_cities * n_volunteers * n_days

city_id = np.repeat(np.arange(1, n_cities + 1), n_volunteers * n_days)
volunteer_id = np.tile(np.repeat(np.arange(1, n_volunteers + 1), n_days), n_cities)
days = np.tile(np.arange(1, n_days + 1), n_cities * n_volunteers)

energy_level = np.random.uniform(0, 10, size=total_rows)
temperature = np.tile(np.random.uniform(20, 45, size=n_days), n_cities * n_volunteers)
funds_base = np.random.randint(100, 1001, size=n_days)
funds_shift = np.roll(funds_base, 1)
donation_funds = np.tile(
    np.where(np.random.rand(n_days) < 0.8, funds_base, funds_shift * 1.5),
    n_cities * n_volunteers,
)
demand_options = np.array(["low", "medium", "high"])
demand_level = np.tile(
    np.random.choice(demand_options, size=n_days, p=[0.3, 0.4, 0.3]),
    n_cities * n_volunteers,
)
demand_numeric = np.where(
    demand_level == "low", 1, np.where(demand_level == "medium", 2, 3)
)

is_friday_base = np.zeros(n_days)
is_friday_base[[4, 11, 18, 25]] = 1
is_friday = np.tile(is_friday_base, n_cities * n_volunteers)
days_until_eid = np.tile(np.linspace(29, 0, n_days), n_cities * n_volunteers)

energy_reshaped = np.reshape(energy_level, (total_rows, 1))
funds_reshaped = np.reshape(donation_funds, (total_rows, 1))
commitment_interaction = np.clip(
    np.dot(energy_reshaped, funds_reshaped.T).diagonal(), 0, 50
)

energy_norm = (energy_level - np.mean(energy_level)) / np.std(energy_level)
funds_norm = (donation_funds - np.mean(donation_funds)) / np.std(donation_funds)
conditions = np.sum(
    np.vstack([energy_norm > 0, funds_norm > 0, demand_numeric > 1, temperature < 40]),
    axis=0,
)
participate_base = np.where(conditions >= 3, 1, 0)
participate_noise = np.where(
    np.random.rand(total_rows) < 0.9, participate_base, 1 - participate_base
)
friday_eid_mask = (
    (is_friday == 1) & (days_until_eid < 5) & (np.random.rand(total_rows) < 0.05)
)
participate = np.where(friday_eid_mask, 0, participate_noise)
participate = np.clip(participate, np.min(participate), np.max(participate))

df = pd.DataFrame(
    np.hstack(
        [
            city_id.reshape(-1, 1),
            volunteer_id.reshape(-1, 1),
            days.reshape(-1, 1),
            energy_level.reshape(-1, 1),
            temperature.reshape(-1, 1),
            donation_funds.reshape(-1, 1),
            demand_numeric.reshape(-1, 1),
            is_friday.reshape(-1, 1),
            days_until_eid.reshape(-1, 1),
            commitment_interaction.reshape(-1, 1),
            participate.reshape(-1, 1),
        ]
    ),
    columns=[
        "city_id",
        "volunteer_id",
        "days",
        "energy_level",
        "temperature",
        "donation_funds",
        "demand_level",
        "is_friday",
        "days_until_eid",
        "commitment_interaction",
        "participate",
    ],
)

df.to_csv("charity_drive_participation.csv", index=False)
print(df.head())
