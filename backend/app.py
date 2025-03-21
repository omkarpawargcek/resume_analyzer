from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    filename = file.filename
    file.save(f"uploads/{filename}")

    return jsonify({"message": "File uploaded successfully", "filename": filename})

if __name__ == "__main__":
    app.run(debug=True)
