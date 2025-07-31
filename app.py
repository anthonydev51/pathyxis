import os
import time
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

VIRUSTOTAL_API_KEY = os.environ.get("VT_API_KEY")  # Set your API key in env variable

UPLOAD_URL = "https://www.virustotal.com/api/v3/files"
REPORT_URL = "https://www.virustotal.com/api/v3/analyses/"

HEADERS = {
    "x-apikey": VIRUSTOTAL_API_KEY
}

@app.route('/scan', methods=['POST'])
def scan_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Upload file to VirusTotal
    files = {'file': (file.filename, file.stream, file.content_type)}
    upload_resp = requests.post(UPLOAD_URL, headers=HEADERS, files=files)

    if upload_resp.status_code != 200:
        return jsonify({"error": "Failed to upload file to VirusTotal", "details": upload_resp.text}), 500
    
    upload_data = upload_resp.json()
    analysis_id = upload_data['data']['id']

    # Poll VirusTotal for analysis report
    for _ in range(20):  # try 20 times max (~40s wait)
        time.sleep(2)
        report_resp = requests.get(REPORT_URL + analysis_id, headers=HEADERS)
        if report_resp.status_code != 200:
            continue
        report_data = report_resp.json()
        status = report_data['data']['attributes']['status']
        if status == 'completed':
            stats = report_data['data']['attributes']['stats']
            return jsonify({
                "fileName": file.filename,
                "scanId": analysis_id,
                "detections": stats.get('malicious', 0),
                "totalEngines": sum(stats.values()),
                "details": report_data['data']['attributes']['results']
            })
    
    return jsonify({"error": "Timeout waiting for VirusTotal scan"}), 504


if __name__ == '__main__':
    app.run(debug=True)