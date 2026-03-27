from flask import Flask, render_template, request
from ultralytics import YOLO
from werkzeug.utils import secure_filename
import os
import shutil

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
PREDICTION_FOLDER = "static/predictions"
MODEL_PATH = "model/best.pt"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PREDICTION_FOLDER, exist_ok=True)

# Load your trained model
model = YOLO(MODEL_PATH)


@app.route("/", methods=["GET", "POST"])
def index():
    result_image = None
    error = None

    if request.method == "POST":
        if "file" not in request.files:
            error = "No file uploaded"
            return render_template("index.html", result_image=None, error=error)

        file = request.files["file"]

        if file.filename == "":
            error = "No file selected"
            return render_template("index.html", result_image=None, error=error)

        filename = secure_filename(file.filename)
        upload_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(upload_path)

        # Run prediction
        results = model.predict(source=upload_path, save=True, conf=0.25)

        # Get saved prediction image
        predicted_dir = results[0].save_dir
        predicted_image_path = os.path.join(predicted_dir, filename)

        final_path = os.path.join(PREDICTION_FOLDER, filename)
        shutil.copy(predicted_image_path, final_path)

        result_image = final_path

    return render_template("index.html", result_image=result_image, error=error)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
