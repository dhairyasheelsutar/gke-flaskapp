import base64
from google.cloud import logging
from google.cloud import pubsub

logging_client = logging.Client()
logger = logging_client.logger('gke_python_logger')  

PROJECT_ID = 'training-freshers'
TOPIC = 'topic-gke-cluster'
SUB = 'subscription-gke-topic'
subscriber = pubsub.SubscriberClient()

def callback(message):
    logger.log_struct({"message": message.data.decode("utf-8")})
    print(message.data)
    message.ack()

subscription_path = subscriber.subscription_path(PROJECT_ID, SUB)
future = subscriber.subscribe(subscription_path, callback)
with subscriber:
    try:
        future.result()
    except TimeoutError:
        future.cancel()