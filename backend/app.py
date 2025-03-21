from flask import Flask, request, jsonify
from models.text_extraction import extract_text
from models.resume_parser import parse_resume
import os
import sys

# Add the parent directory to sys.path so Python can find `models/`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now import the function
from models.text_extraction import extract_text

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_resume():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    file_type = file.filename.split(".")[-1].lower()
    extracted_text = extract_text(file_path, file_type)
    parsed_data = parse_resume(extracted_text)

    return jsonify(parsed_data)

if __name__ == "__main__":
    app.run(debug=True)
