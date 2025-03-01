from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import cv2
import numpy as np
import tensorflow as tf
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Global variables
NUM_CATEGORIES = 43
IMG_WIDTH = 30
IMG_HEIGHT = 30
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# GTSRB class names
CLASS_NAMES = [
    "Speed limit (20km/h)",
    "Speed limit (30km/h)",
    "Speed limit (50km/h)",
    "Speed limit (60km/h)",
    "Speed limit (80km/h)",
    "End of speed limit (80km/h)",
    "Speed limit (100km/h)",
    "Speed limit (120km/h)",
    "No passing",
    "No passing for vehicles over 3.5t",
    "Right-of-way at next intersection",
    "Priority road",
    "Yield",
    "Stop",
    "No vehicles",
    "Vehicles over 3.5t prohibited",
    "No entry",
    "General caution",
    "Dangerous curve left",
    "Dangerous curve right",
    "Double curve",
    "Bumpy road",
    "Slippery road",
    "Road narrows on the right",
    "Road work",
    "Traffic signals",
    "Pedestrians",
    "Children crossing",
    "Bicycles crossing",
    "Beware of ice/snow",
    "Wild animals crossing",
    "End of all speed and passing limits",
    "Turn right ahead",
    "Turn left ahead",
    "Ahead only",
    "Go straight or right",
    "Go straight or left",
    "Keep right",
    "Keep left",
    "Roundabout mandatory",
    "End of no passing",
    "End of no passing for vehicles over 3.5t",
]

# Load the pre-trained model
MODEL_PATH = "./Model/traffic_cnn.h5"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file '{MODEL_PATH}' not found.")
model = tf.keras.models.load_model(MODEL_PATH)


def preprocess_image(image_path):
    """Preprocess the uploaded image for the model."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Failed to load image.")
    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)
    return img


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400
        file = request.files["image"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        # Save the file with a unique name to avoid overwriting
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        # Verify file exists
        if not os.path.exists(file_path):
            return jsonify({"error": "Failed to save image"}), 500

        # Predict
        try:
            img = preprocess_image(file_path)
            predictions = model.predict(img, verbose=0)
            predicted_class = np.argmax(predictions[0])
            confidence = predictions[0][predicted_class] * 100
            result = {
                "prediction": CLASS_NAMES[predicted_class],
                "confidence": f"{confidence:.2f}",
                "image_url": f"/static/uploads/{filename}",
            }
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return render_template("index.html")


# Route to serve static files (for debugging)
@app.route("/static/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True)
