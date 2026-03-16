import json
from confluent_kafka import Consumer
from shared.logger import log_event

class Tracker:
    def __init__(self):
        consumer_config = {
            "bootstrap.servers": "localhost:9092",
            "group.id": "tracker",
            "auto.offset.reset": "earliest"
        }
        consumer = Consumer(consumer_config)

        consumer.subscribe(["intel", "attack", "damage"])

        log_event(level="info", message="Consumer is running")

    def tracker(self):
        consumer = Tracker()
        try:
            while True:
                msg = consumer.poll(20)
                if msg is None:
                    break
                if msg.error():
                    print("Error:", msg.error())
                    continue

                value = msg.value().decode("utf-8")
                order = json.loads(value)
                log_event(level="info", message=f"get {order} from producer")
        except KeyboardInterrupt:
            print("Stopping consumer")

        finally:
            consumer.close()

if __name__ == '__main__':
    tracker = Tracker()
    tracker.tracker()

