import numpy as np
import pandas as pd


np.random.seed(42)


n_states = 10000


data = np.zeros((n_states, 16))


for i in range(n_states):
    real_part = np.random.normal(size=4)
    imag_part = np.random.normal(size=4)
    state = real_part + 1j * imag_part

    norm = np.sqrt(np.sum(np.abs(state) ** 2))
    state /= norm

    density_matrix = np.outer(state, state.conj())

    real_elements = density_matrix.real.flatten()

    data[i, :16] = real_elements

columns = [
    "Re_rho_00",
    "Re_rho_01",
    "Re_rho_02",
    "Re_rho_03",
    "Re_rho_10",
    "Re_rho_11",
    "Re_rho_12",
    "Re_rho_13",
    "Re_rho_20",
    "Re_rho_21",
    "Re_rho_22",
    "Re_rho_23",
    "Re_rho_30",
    "Re_rho_31",
    "Re_rho_32",
    "Re_rho_33",
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("haar_random_2qubit_states.csv", index=False)
print(
    f"Generated {n_states} two-qubit states and saved to './Data/haar_random_2qubit_states.csv'"
)
print(f"Dataset shape: {df.shape}")
print("First few rows:")
print(df.head())
