from google.cloud import logging_v2
client = logging_v2.LoggingServiceV2Client()

resource = {
    "type": "container",
    "labels": {
        "project_id": "training-freshers",
        "cluster_name": "cluster-1",
        "namespace_id": "default"
    }
}

e = {
    "log_name": "projects/training-freshers/logs/test-logging",
    "resource": resource,
    "text_payload": "this is a log statement",
}

entries = [e]

response = client.write_log_entries(entries)
