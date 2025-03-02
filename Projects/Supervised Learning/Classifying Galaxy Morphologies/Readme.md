# Galaxy Morphology Prediction Project Guide

This project uses supervised learning to predict galaxy morphologies based on data from Galaxy Zoo 2 (`gz2_hart16.csv.gz`). It involves understanding galaxy shapes, defining features and targets, building a machine learning model, and creating a full-stack web application with a Flask backend and Tailwind CSS frontend. This guide outlines the key concepts you need to learn, without code, focusing on the "why" and "what" of each step.

---

## 1. Project Overview

- **Goal**: Predict whether a galaxy is "smooth" (elliptical) or has "features" (spiral) using citizen scientist classifications.
- **Real-Life Problem**: Automating galaxy morphology classification helps astronomers analyze vast datasets from surveys like SDSS, aiding research into galaxy formation and cosmic evolution.
- **Components**:
  - Machine Learning: Build a model to classify galaxies.
  - Backend: Serve predictions via an API.
  - Frontend: Create a user interface for input and results.

---

## 2. Understanding Galaxy Shapes (Morphologies)

Galaxy morphologies describe the visual and structural forms of galaxies, reflecting their evolutionary history and physical processes.

### Main Types

- **Spiral Galaxies**:
  - Shape: Disk-like with a central bulge and winding arms.
  - Characteristics: Rich in gas and dust, active star formation, rotating disks.
  - Why It Matters: Indicates dynamic, ongoing processes; our Milky Way is a barred spiral.
- **Elliptical Galaxies**:
  - Shape: Smooth, rounded, or oval, lacking arms or disks.
  - Characteristics: Older stars, little gas/dust, minimal star formation, often from mergers.
  - Why It Matters: Represents older, stable systems shaped by past interactions.
- **Irregular Galaxies**:
  - Shape: Chaotic, no clear structure.
  - Characteristics: High star formation, often disrupted by gravity.
  - Why It Matters: Shows the diversity and complexity of galaxy evolution.

### Why Classify Morphologies?

- Reveals how galaxies form and evolve over billions of years.
- Connects to physical properties like dark matter, rotation, and star formation rates.
- Big datasets (e.g., SDSS) need automation—manual classification is too slow.

---

## 3. Dataset: `gz2_hart16.csv.gz`

- **Source**: Galaxy Zoo 2, where citizen scientists classified SDSS galaxy images (Hart et al., 2016).
- **Size**: ~304,000 galaxies, 231 columns.
- **Content**:
  - Metadata: Galaxy IDs, coordinates (RA, Dec), total votes.
  - Morphology Votes: Fractions of votes for various shapes and features across 11 tasks (e.g., smooth vs. features, edge-on, spiral arms).

### What’s Missing?

- No direct measurements like brightness (magnitudes) or redshift—only vote-based data.
- Limits feature options, so we adapt by using votes as a proxy.

---

## 4. Defining Features (X) and Target (y)

### Features (X): What We Use to Predict

- **Chosen Features**: Vote fractions from Task 1:
  - Fraction voting "smooth" (elliptical-like).
  - Fraction voting "features/disk" (spiral-like).
  - Fraction voting "star/artifact" (noise).
- **Why These?**: They’re the only numerical data available in this dataset that correlate with morphology. Ideally, we’d use magnitudes (brightness in u, g, r, i, z bands) or physical properties, but those require extra SDSS queries.
- **Challenge**: Using votes as features risks overlap with the target (data leakage), but it’s a workaround given the dataset.

### Target (y): What We Predict

- **Chosen Target**: A simplified label derived from the `gz2_class` column (e.g., "E" for elliptical = 1, "S" for spiral = 0).
- **Why Binary?**: Simplifies the multi-class problem (e.g., subtypes like "Sb", "Er") into something manageable for a first model. Real astronomy uses finer categories, but this is a starting point.
- **Alternative**: Could use vote fractions directly (e.g., smooth > features), but `gz2_class` offers a consolidated label.

---

## 5. Why Random Forest?

### What Is Random Forest?

- An ensemble method that builds many decision trees and averages their predictions.
- Each tree votes on the outcome (smooth or features), and the majority wins.

### Why We Use It

- **Handles Complex Data**: Works well with multiple features (even vote fractions) without needing heavy preprocessing.
- **Robustness**: Reduces overfitting compared to a single decision tree by averaging results.
- **Easy to Use**: Requires minimal tuning to get decent performance (e.g., number of trees = 100).
- **Probability Output**: Provides confidence scores (e.g., 85% smooth), useful for the frontend.
- **Astronomy Fit**: Commonly used in galaxy classification due to its flexibility with noisy, high-dimensional data.

### Alternatives

- Logistic Regression: Simpler, but assumes linear relationships (less likely here).
- Neural Networks: Powerful, but overkill for this small feature set and requires more data prep.
- XGBoost: Faster and potentially more accurate, but trickier to tune.

---

## 6. Machine Learning Concepts

- **Supervised Learning**: We train with labeled data (vote fractions → morphology).
- **Classification**: Predict discrete categories (smooth vs. features).
- **Train/Test Split**: Split data to evaluate performance on unseen galaxies, avoiding overfitting.
- **Missing Values**: Fill gaps (e.g., with averages) since real data often has holes.
- **Accuracy**: Measure how often predictions match true labels—simple but effective for a baseline.

---

## 7. Backend: Flask API

### What It Does

- Takes user inputs (vote fractions) and returns a prediction (smooth or features).
- Loads the trained model and processes requests.

### Why Flask?

- **Lightweight**: Simple to set up for a small API.
- **Python-Friendly**: Integrates seamlessly with our ML model.
- **RESTful**: Handles POST requests (input data) and returns JSON (prediction).

### Key Concepts

- **Routing**: Define endpoints (e.g., homepage, predict).
- **JSON**: Standard format for sending/receiving data.
- **Error Handling**: Catch bad inputs (e.g., non-numeric values) to keep the app running.

---

## 8. Frontend: Tailwind CSS UI

### What It Does

- Lets users enter vote fractions and see the prediction with a clean, modern design.
- Displays results (e.g., "Smooth (Elliptical), Confidence: 85%").

### Key Concepts

- **Forms**: Collect user inputs (three vote fractions, 0–1 range).
- **JavaScript**: Send data to the backend and update the page with results.
- **Dynamic UI**: Show/hide results, style with Tailwind for a professional feel.

---

## 9. Why This Approach?

- **Dataset-Driven**: Limited by `gz2_hart16.csv.gz` lacking magnitudes, so we adapt with votes.
- **Full-Stack Learning**: Combines ML, backend, and frontend for a complete project.
- **Real-World Relevance**: Mimics how astronomers might automate classification, even if simplified.

---

## 10. What You’ll Learn

- **Galaxy Morphologies**: How shapes reflect physics and evolution.
- **ML Workflow**: From data to model to deployment.
- **Features vs. Target**: Defining X and y in a real dataset.
- **Random Forest**: Why it’s a go-to for classification.
- **Web Development**: Backend API and frontend UI basics.
- **Problem-Solving**: Workarounds for missing data (e.g., no magnitudes).

---

## 11. Next Steps

- **Better Features**: Fetch SDSS magnitudes (brightness) for more scientific inputs.
- **More Classes**: Predict irregular galaxies or spiral subtypes.
- **Visualization**: Add galaxy images or feature importance plots.
- **Deployment**: Host online for others to use.

---

This project teaches you to think like an astronomer and a developer, bridging data science with practical application. Start with understanding galaxy shapes, then build each layer—ML, backend, frontend—to see the full picture!
