import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from any origin

# Load the student marks from the JSON file
try:
    with open("data.json", "r") as file:
        student_data = json.load(file)
except FileNotFoundError:
    student_data = {}

@app.route("/api", methods=["GET"])
def get_student_marks():
    # Get names from the query parameters
    names = request.args.getlist("name")
    if not names:
        return jsonify({"error": "No names provided"}), 400

    marks = []
    for name in names:
        # Get the marks for each name if it exists, otherwise "Not found"
        for data in student_data:
            if data["name"] == name:
                marks.append(data.get("marks", None))
                break

    return {"marks": marks}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)