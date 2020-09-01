import base64
from google.cloud import logging
from google.cloud import pubsub

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

subscription_path = subscriber.subscription_path(PROJECT_ID, SUB)
future = subscriber.subscribe(subscription_path, callback)
try:
    future.result()
except:
    future.cancel()