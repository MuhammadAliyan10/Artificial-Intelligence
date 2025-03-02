from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)


kmeans = joblib.load("Model.pkl")
scaler = joblib.load("scaler.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        input_state = [
            float(data[f"Re_rho_{i}{j}"]) for i in range(4) for j in range(4)
        ]

        input_array = np.array(input_state).reshape(1, -1)
        input_scaled = scaler.transform(input_array)

        cluster = kmeans.predict(input_scaled)[0]

        return jsonify({"cluster": int(cluster)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
