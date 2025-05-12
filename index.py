from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

POWER_AUTOMATE_URL = "https://prod-75.westeurope.logic.azure.com:443/workflows/4b127412de9b4126bd4430c52aee0625/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=fZcQFpEwJ-K3gj-lRmG00DVafFeOFPAOqc94FoJ8P4s"

@app.route("/verzend", methods=["POST"])
def verzend():
    try:
        data = request.json
        response = requests.post(POWER_AUTOMATE_URL, json=data, headers={"Content-Type": "application/json"})
        return jsonify({"status": "success", "power_automate_response": response.text}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
