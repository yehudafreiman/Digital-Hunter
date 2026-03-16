import json
import os
from confluent_kafka import Consumer
from shared.logger import log_event


class KafkaConsumer:
    # configuration
    def __init__(self, broker, group_id, topic):
        self.consumer = Consumer({
            "bootstrap.servers": broker,
            "group.id": group_id,
            "auto.offset.reset": "earliest"
        })
        self.consumer.subscribe(topic)

    # listen kafka producer
    def processor(self):
        try:
            while True:
                msg = self.consumer.poll(20)
                if msg is None:
                    log_event(level="info", message="No more massages")
                    break
                if msg.error():
                    log_event(level="error", message=msg.error())
                    continue

                data = json.loads(msg.value().decode("utf-8"))
                log_event(level="info", message=f"Get {data} from producer")
        except KeyboardInterrupt:
            print("Stopping consumer")
        finally:
            self.consumer.close()


if __name__ == '__main__':
    consumer = KafkaConsumer(
        os.getenv('KAFKA_BROKER', 'kafka:9092'),
        'signals-tracker',
        ["intel", "attack", "damage"]
    )

    log_event(level="info", message="Consumer is running")

    consumer.processor()

