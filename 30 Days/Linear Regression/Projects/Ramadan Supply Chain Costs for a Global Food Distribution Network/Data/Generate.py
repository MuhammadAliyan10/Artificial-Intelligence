import numpy as np
import pandas as pd

n_days = 30 * 50
days = np.arange(1, n_days + 1)

total_city = 50


city_population = np.random.randint(100000, 10000000, size=total_city)
temperature = np.random.uniform(20, 45, size=n_days)


chance = np.random.rand(n_days) < 0.10
fuel_price = np.random.uniform(2, 5, size=n_days)
fuel_price = np.where(
    chance & (np.roll(chance, 1, axis=0)),
    fuel_price * 1.5,
    fuel_price,
)


is_friday = np.tile(
    np.array([1 if n % 30 in [5, 12, 19, 26] else 0 for n in range(1, 31)]), total_city
)
days_until_eid = np.tile(np.arange(29, -1, -1), total_city)


base = np.repeat(10 + (city_population / 100000) * 2, 30)
deliveries_mask = (is_friday == 1) | (days_until_eid < 5)
n_deliveries = np.random.randint(10, 100, size=n_days)
n_deliveries = np.where(
    deliveries_mask, np.clip(n_deliveries * 1.5, None, 100), n_deliveries
)
demand_interaction = np.repeat(city_population, 30) * n_deliveries
weather_disruption_flag = np.where(
    (temperature > 40) | (np.random.rand(n_days) < 0.05), 1, 0
)

base_cost = (
    0.001 * np.repeat(city_population, 30)
    + 2 * temperature
    + 10 * fuel_price
    + 5 * n_deliveries
    + 20 * is_friday
    + 0.8 * days_until_eid
    + 0.0001 * demand_interaction
    + 50 * weather_disruption_flag
)
crisis_mask = (weather_disruption_flag == 1) & (np.random.rand(n_days) < 0.05)
supply_chain_cost = np.where(
    crisis_mask,
    np.clip(base_cost + np.random.uniform(-500, 500, size=n_days), None, 100000),
    np.clip(base_cost + np.random.uniform(-500, 500, size=n_days), None, 50000),
)

df = pd.DataFrame(
    {
        "days": days,
        "city_population": np.repeat(city_population, 30),
        "temperature": temperature,
        "fuel_price": fuel_price,
        "n_deliveries": n_deliveries,
        "is_friday": is_friday,
        "days_until_eid": days_until_eid,
        "demand_interaction": demand_interaction,
        "weather_disruption_flag": weather_disruption_flag,
        "supply_chain_cost": supply_chain_cost,
    }
)

df.to_csv("ramadan_supply_chain_costs.csv", index=False)
print(df.head())
