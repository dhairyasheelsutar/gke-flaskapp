from flask import Flask, request, jsonify
import base64
from google.cloud import logging

app = Flask(__name__)
logging_client = logging.Client()
log_name = 'gke-application-logs'
logger = logging_client.logger(log_name)

@app.route("/")
def index():

    # Receive the input
    request_json = request.get_json()
    message = base64.b64decode(request_json['message']['data']).decode("utf-8")

    # Logging text
    logger.log_text(message)
    print(message)

    # Return response in json format
    return jsonify({"message": message}, 200);

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)