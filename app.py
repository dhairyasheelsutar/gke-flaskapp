import base64
from google.cloud import logging
from google.cloud import pubsub

logging_client = logging.Client()

PROJECT_ID = 'training-freshers'
TOPIC = 'topic-gke-cluster'
SUB = 'subscription-gke-topic'
subscriber = pubsub.SubscriberClient()

def callback(message):
    print(message.data)
    message.ack()

subscription_path = subscriber.subscription_path(PROJECT_ID, SUB)
future = subscriber.subscribe(subscription_path, callback)
try:
    future.result()
except:
    future.cancel()