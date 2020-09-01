import base64
from google.cloud import logging_v2
from google.cloud import pubsub

client = logging_v2.LoggingServiceV2Client()
PROJECT_ID = "training-freshers"
TOPIC = "topic-gke-cluster"
SUB = "subscription-gke-topic"

resource = {
    "type": "global",
    "labels": {
        "project_id": PROJECT_ID,
    }
}

e = {
    "log_name": "projects/"+ PROJECT_ID +"/logs/test-logging",
    "resource": resource
}

subscriber = pubsub.SubscriberClient()

def callback(message):
    e["text_payload"] = message.data.decode("utf-8")
    client.write_log_entries([e])
    print(message.data)
    message.ack()

subscription_path = subscriber.subscription_path(PROJECT_ID, SUB)
future = subscriber.subscribe(subscription_path, callback)
with subscriber:
    try:
        future.result()
    except TimeoutError:
        future.cancel()