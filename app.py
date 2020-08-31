from flask import Flask
from flask import request
from google.cloud import pubsub
from google.cloud import logging

app = Flask(__name__)
logging_client = logging.Client()
log_name = 'gke-application-logs'
logger = logging_client.logger(log_name)

@app.route("/")
def index():
    print(request.json)
    print(request.form)
    return "Hello world from kubernetes!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)