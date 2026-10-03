import os
from urllib.parse import unquote_plus

import boto3

TABLE_NAME = os.environ["TABLE_NAME"]
DYNAMODB = boto3.resource("dynamodb")
TABLE = DYNAMODB.Table(TABLE_NAME)


def lambda_handler(event, context):
    if event.get("Event") == "s3:TestEvent":
        print("Received the S3 notification test event.")
        return {"statusCode": 200, "processed": 0, "event_ids": []}

    event_ids = []

    for record in event.get("Records", []):
        bucket = record["s3"]["bucket"]["name"]
        object_data = record["s3"]["object"]
        object_key = unquote_plus(object_data["key"])
        sequencer = object_data.get("sequencer", "no-sequencer")
        event_id = f"{bucket}#{object_key}#{sequencer}"

        item = {
            "event_id": event_id,
            "bucket": bucket,
            "object_key": object_key,
            "size_bytes": object_data.get("size", 0),
            "event_name": record["eventName"],
            "event_time": record["eventTime"],
            "sequencer": sequencer,
            "status": "RECORDED"
        }

        TABLE.put_item(Item=item)
        event_ids.append(event_id)
        print(f"Recorded upload event: {event_id}")

    return {
        "statusCode": 200,
        "processed": len(event_ids),
        "event_ids": event_ids
    }