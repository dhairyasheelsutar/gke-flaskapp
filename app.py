from flask import Flask, request, jsonify
from concurrent.futures import TimeoutError
import base64
from google.cloud import logging
from google.cloud import pubsub

app = Flask(__name__)
logging_client = logging.Client()
log_name = 'gke-application-logs'
logger = logging_client.logger(log_name)
PROJECT_ID = 'training-freshers'
TOPIC = 'topic-gke-cluster'
SUB = 'subscription-gke-topic'
subscriber = pubsub.SubscriberClient()

def callback(message):
    logger.log_text(message.data.decode("utf-8"))
    print(message.data)
    message.ack()

@app.route("/")
def index():

    # Receive the input    
    subscription_path = subscriber.subscription_path(PROJECT_ID, SUB)
    future = subscriber.subscribe(subscription_path, callback)
    try:
        future.result(timeout=3.0)
    except:
        future.cancel()

    # Return response in json format
    return jsonify({"message": "Message read successfully"}, 200);

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)