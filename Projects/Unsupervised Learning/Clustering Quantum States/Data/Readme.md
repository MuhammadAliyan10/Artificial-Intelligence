# Haar-Random Two-Qubit States Generation: Code Explanation

This document explains each line and function in the Python script that generates 10,000 Haar-random two-qubit pure states, including how it works and an example output. The goal is to create a dataset for unsupervised learning (clustering) with 10,000 rows and 16 columns representing the real parts of 4x4 density matrices.

---

## Line-by-Line Explanation

### Imports

- **Purpose**: Load libraries for numerical operations and data handling.
- **Details**:
  - `import numpy as np`: Brings in NumPy, a library for fast array and matrix math. Alias `np` is standard.
  - `import pandas as pd`: Brings in pandas, a library for data manipulation and CSV export. Alias `pd` is common.

### Random Seed

- **Line**: `np.random.seed(42)`
- **What It Does**: Sets a fixed starting point for NumPy’s random number generator.
- **Why**: Ensures the same random numbers each run (reproducibility). `42` is an arbitrary choice.
- **How**: Seeds the random state—every `np.random` call follows this sequence.

### Parameters

- **Line**: `n_states = 10000`
- **What It Does**: Defines how many quantum states to generate.
- **Why**: 10,000 is small enough (~1–2 MB) for memory limits, big enough for clustering patterns.
- **How**: Just a number—controls the loop later.

### Initialize Data Array

- **Line**: `data = np.zeros((n_states, 16))`
- **What It Does**: Creates a 10,000 x 16 array filled with zeros.
- **Why**: Pre-allocates space for 10,000 states, each with 16 features (real parts of a 4x4 matrix).
- **How**: `np.zeros(shape)` makes an array of zeros; `(10000, 16)` sets rows and columns.
- **Details**: Each row will hold one state’s density matrix real elements.

### Loop Over States

- **Line**: `for i in range(n_states):`
- **What It Does**: Loops 10,000 times (0 to 9999).
- **Why**: Generates one state per iteration to fill the `data` array.
- **How**: Standard Python loop—`i` indexes each row.

### Generate Random Vector

- **Line**: `real_part = np.random.normal(size=4)`
- **What It Does**: Creates a 4-element array of random numbers from a normal (Gaussian) distribution.
- **Why**: Two qubits need a 4D vector (2² = 4 basis states: |00⟩, |01⟩, |10⟩, |11⟩).
- **How**: `np.random.normal()` draws from a bell curve (mean 0, std 1); `size=4` gives 4 values.

- **Line**: `imag_part = np.random.normal(size=4)`
- **What It Does**: Same as above, for imaginary parts.
- **Why**: Quantum states are complex—need separate real and imaginary components.
- **How**: Another Gaussian draw for the imaginary axis.

- **Line**: `state = real_part + 1j * imag_part`
- **What It Does**: Combines real and imaginary into a 4D complex vector.
- **Why**: Forms a quantum state vector (e.g., [a + bi, ...]).
- **How**: `1j` is Python’s imaginary unit (√-1); adds element-wise (e.g., 0.5 + 0.3j).

### Normalize the Vector

- **Line**: `norm = np.sqrt(np.sum(np.abs(state) ** 2))`
- **What It Does**: Computes the vector’s magnitude (norm).
- **Why**: Pure states must have norm 1 (100% probability).
- **How**:

  - `np.abs(state)`: Absolute value of complex numbers (√(real² + imag²)).
  - `np.sum(... ** 2)`: Squares and sums them.
  - `np.sqrt()`: Takes the square root—total length.

- **Line**: `state /= norm`
- **What It Does**: Divides the vector by its norm.
- **Why**: Normalizes to unit length—makes it a valid quantum state.
- **How**: In-place division (`/=`); scales each element (e.g., [0.5, 0.3] → [0.7, 0.4] if norm was ~0.7).

### Compute Density Matrix

- **Line**: `density_matrix = np.outer(state, state.conj())`
- **What It Does**: Creates a 4x4 complex matrix.
- **Why**: Density matrix (|ψ><ψ|) fully describes a pure state, including entanglement.
- **How**:
  - `state.conj()`: Complex conjugate (flips imaginary sign, e.g., 0.5 + 0.3j → 0.5 - 0.3j).
  - `np.outer()`: Outer product—multiplies state (4x1) by its conjugate transpose (1x4) to get 4x4.

### Extract Features

- **Line**: `real_elements = density_matrix.real.flatten()`
- **What It Does**: Pulls out the 16 real parts and flattens them.
- **Why**: Real parts are features for clustering (imaginary could be added).
- **How**:

  - `.real`: Extracts real components (drops imaginary).
  - `.flatten()`: Turns 4x4 into a 1D array of 16.

- **Line**: `data[i, :16] = real_elements`
- **What It Does**: Stores the 16 real elements in the i-th row.
- **Why**: Builds the dataset row-by-row.
- **How**: Assigns to `data`’s i-th row, columns 0–15.

### Define Columns

- **Line**: `columns = ["Re_rho_00", ..., "Re_rho_33"]`
- **What It Does**: Lists 16 column names.
- **Why**: Labels features as real parts of the density matrix (ρ₀₀ to ρ₃₃).
- **How**: Manual list—`Re_rho_ij` means real part of matrix element at row i, column j.

### Create DataFrame

- **Line**: `df = pd.DataFrame(data, columns=columns)`
- **What It Does**: Turns the NumPy array into a pandas table.
- **Why**: Easier to handle and save as CSV.
- **How**: `pd.DataFrame()` pairs `data` (10,000 x 16) with `columns` names.

### Save to CSV

- **Line**: `df.to_csv("./Data/haar_random_2qubit_states.csv", index=False)`
- **What It Does**: Writes the table to a CSV file.
- **Why**: Saves the dataset for clustering later.
- **How**:
  - `"./Data/..."`: Path to save (assumes a `Data` folder exists).
  - `index=False`: Skips row numbers in the file.

### Print Output

- **Line**: `print(f"Generated {n_states} ...")`
- **What It Does**: Confirms the file was saved.
- **Why**: Feedback on success.
- **How**: `f-string` inserts `n_states` (10,000).

- **Line**: `print(f"Dataset shape: {df.shape}")`
- **What It Does**: Shows rows and columns.
- **Why**: Verifies the dataset size (should be 10,000 x 16).
- **How**: `df.shape` returns a tuple (rows, cols).

- **Line**: `print("First few rows:"); print(df.head())`
- **What It Does**: Displays the top 5 rows.
- **Why**: Quick peek at the data.
- **How**: `df.head()` grabs the first 5 rows.

---

## How It Works Overall

- **Flow**: Loops 10,000 times, each time creating a random 4D complex vector, normalizing it, making a 4x4 density matrix, extracting 16 real parts, and storing them.
- **Quantum Bit**: Haar-randomness (Gaussian sampling + normalization) ensures uniform distribution over all possible two-qubit pure states.
- **Result**: A CSV with 10,000 rows, each representing a unique quantum state’s real density matrix elements.

---

## Example Output

**Console Output**:
