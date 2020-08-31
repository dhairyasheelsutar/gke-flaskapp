from google.cloud import pubsub
from google.cloud import logging

PROJECT_ID = 'training-freshers'
TOPIC = 'topic-gke-cluster'
SUB = 'subscription-gke-cluster-topic'
subscriber = pubsub.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUB)
logging_client = logging.Client()
log_name = 'gke-application-logs'
logger = logging_client.logger(log_name)

def callback(message):
    logger.log_text(message.data)
    print("Received message: {}".format(message.data))
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print("Listening for messages on {}..\n".format(subscription_path))
with subscriber:
    try:
        streaming_pull_future.result()
    except:
        streaming_pull_future.cancel()