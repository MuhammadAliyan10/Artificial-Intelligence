from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract vote fractions (match training features)
        features = [
            float(data["smooth_fraction"]),
            float(data["features_fraction"]),
            float(data["artifact_fraction"]),
        ]

        # Convert to numpy array and reshape for prediction
        features_array = np.array(features).reshape(1, -1)

        # Predict (0 = features/spiral, 1 = smooth/elliptical)
        prediction = model.predict(features_array)[0]
        probability = model.predict_proba(features_array)[0]

        # Interpret result
        result = "Smooth (Elliptical)" if prediction == 1 else "Features (Spiral)"
        confidence = max(probability) * 100  # Highest probability as confidence

        return jsonify({"prediction": result, "confidence": f"{confidence:.2f}%"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
