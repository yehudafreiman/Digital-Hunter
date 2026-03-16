import json
import os
import uuid
from confluent_kafka import Consumer
from shared.logger import log_event
from shared.connection import collection


class KafkaEventProcessor:
    # configuration
    def __init__(self, broker, group_id, topic):
        self.consumer = Consumer({
            "bootstrap.servers": broker,
            "group.id": group_id,
            "auto.offset.reset": "earliest"
        })
        self.consumer.subscribe([topic])

    # listen kafka events
    def process_event(self, callback):
        try:
            while True:
                msg = self.consumer.poll(15)
                if msg is None:
                    continue
                if msg.error():
                    log_event(level="error", message=f"{msg.error()}")
                    continue
                data = json.loads(msg.value().decode("utf-8"))
                data["id"] = str(uuid.uuid4())
                log_event(level="info", message=data["id"])
                callback(data)
        finally:
            self.consumer.close()

class DataStorageManager:
    # send mongo
    @staticmethod
    def save_events_mongodb(data):
        try:
            for event in data:
                collection.insert_one(event)
                log_event(level="info", message="saved to mongoDB")
        except Exception as e:
            log_event(level="error", message=f"{e}")

def handle_data(data):
    DataStorageManager.save_events_mongodb(data)

if __name__ == '__main__':
    consumer = KafkaEventProcessor(
        os.getenv('KAFKA_BROKER', 'kafka:9092'),
        'signals-tracker',
        ["intel", "attack", "damage"]
    )
    consumer.process_event(handle_data)

