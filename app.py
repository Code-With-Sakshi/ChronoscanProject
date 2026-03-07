
from flask import Flask, request, jsonify
import os

from ml.change_detector import analyze_change
from ml.report import generate_report

app = Flask(__name__)

# Ensure upload directory exists
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route("/analyze", methods=["POST"])
def analyze():
    # ✅ Validate inputs
    if "day0" not in request.files or "day5" not in request.files:
        return jsonify({"error": "Both day0 and day5 files are required"}), 400

    day0 = request.files["day0"]
    day5 = request.files["day5"]

    # ✅ Save files
    path0 = os.path.join(UPLOAD_DIR, "day0.png")
    path5 = os.path.join(UPLOAD_DIR, "day5.png")

    day0.save(path0)
    day5.save(path5)

    # ✅ Run analysis
    area0, area5, percent = analyze_change(path0, path5)

    # ✅ Generate text report
    report = generate_report(percent)

    return jsonify({
        "day0_area": int(area0),
        "day5_area": int(area5),
        "change_percent": round(percent, 2),
        "report": report
    })

# if __name__ == "__main__":
#     app.run(port=5001, debug=True)
if __name__ == "__main__":
    app.run(port=5001, debug=False, use_reloader=False)
