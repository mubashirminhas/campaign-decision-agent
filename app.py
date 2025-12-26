import os
from flask import Flask, request, jsonify, render_template
import pandas as pd
from agent.feature_engineering import add_features
from agent.decision_agent import campaign_decision_agent
from flask import send_file

# Initialize Flask app
app = Flask(__name__)

# Path to data folder
DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_FOLDER, exist_ok=True)  # create if it doesn't exist
UPLOAD_FILE = os.path.join(DATA_FOLDER, "campaign_data.csv")  # fixed CSV path

# ---------------------------
# Health Check Endpoint
# ---------------------------
@app.route("/", methods=["GET"])
def health():
    return {"status": "Agent API running"}, 200

# ---------------------------
# Upload CSV Endpoint
# ---------------------------
@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    results = None
    message = None

    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename.endswith(".csv"):
            # Save uploaded CSV to data folder
            file.save(UPLOAD_FILE)
            message = f"File '{file.filename}' uploaded successfully!"
        else:
            return "Please upload a valid CSV file", 400

    # Load latest results if file exists
    if os.path.exists(UPLOAD_FILE):
        df = pd.read_csv(UPLOAD_FILE)
        df = add_features(df)
        df = campaign_decision_agent(df)
        results = df.to_dict(orient="records")

    return render_template("upload.html", results=results, message=message)

# ---------------------------
# API Endpoint for Dynamic Table
# ---------------------------
@app.route("/agent/results", methods=["GET"])
def agent_results():
    """
    Reads the fixed CSV file and returns JSON results.
    """
    if not os.path.exists(UPLOAD_FILE):
        return jsonify([])  # empty list if file doesn't exist

    try:
        df = pd.read_csv(UPLOAD_FILE)
        df = add_features(df)
        df = campaign_decision_agent(df)
        return jsonify(df.to_dict(orient="records"))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------
# API Endpoint for JSON Decisions (Optional)
# ---------------------------
@app.route("/agent/decide", methods=["POST"])
def agent_decide():
    data = request.get_json()
    df = pd.DataFrame(data)
    df = add_features(df)
    df = campaign_decision_agent(df)
    return jsonify(df.to_dict(orient="records"))

@app.route("/download", methods=["GET"])
def download_file():
    """
    Allows user to download the latest decision results as CSV.
    """
    if not os.path.exists(UPLOAD_FILE):
        return "No data file found. Upload a CSV first.", 400

    try:
        # Read the latest data
        df = pd.read_csv(UPLOAD_FILE)
        df = add_features(df)
        df = campaign_decision_agent(df)

        # Save to a temporary CSV file (or send directly)
        temp_path = os.path.join(DATA_FOLDER, "campaign_decision_results.csv")
        df.to_csv(temp_path, index=False)

        return send_file(temp_path, as_attachment=True)
    except Exception as e:
        return f"Error generating CSV: {e}", 500
# ---------------------------
# Run Flask App
# ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
