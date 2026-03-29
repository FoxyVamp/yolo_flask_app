from flask import Flask, render_template, request
from ultralytics import YOLO
from werkzeug.utils import secure_filename
from PIL import Image
from pillow_heif import register_heif_opener
import os
import shutil

register_heif_opener()

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
PREDICTION_FOLDER = "static/predictions"
MODEL_PATH = "model/best.pt"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "heic", "heif"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PREDICTION_FOLDER, exist_ok=True)

model = None

def get_model():
    global model
    if model is None:
        model = YOLO(MODEL_PATH)
        model.to("cpu")
    return model

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_if_needed(file_path):
    ext = file_path.rsplit(".", 1)[1].lower()
    if ext in {"heic", "heif"}:
        img = Image.open(file_path).convert("RGB")
        new_path = os.path.splitext(file_path)[0] + ".jpg"
        img.save(new_path, "JPEG")
        return new_path
    return file_path


@app.route("/healthz")
def healthz():
    return "ok", 200


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

        if not allowed_file(file.filename):
            error = "Unsupported file type. Please upload JPG, JPEG, PNG, or HEIC."
            return render_template("index.html", result_image=None, error=error)

        try:
            filename = secure_filename(file.filename)
            upload_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(upload_path)

            processed_path = convert_if_needed(upload_path)
            processed_filename = os.path.basename(processed_path)

            results = get_model().predict(
                source=processed_path,
                save=True,
                conf=0.20,
                imgsz=640
            )

            predicted_dir = results[0].save_dir
            predicted_image_path = os.path.join(predicted_dir, processed_filename)

            final_path = os.path.join(PREDICTION_FOLDER, processed_filename)
            shutil.copy(predicted_image_path, final_path)

            result_image = final_path

        except Exception as e:
            error = f"Prediction failed: {str(e)}"

    return render_template("index.html", result_image=result_image, error=error)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port)
