from shared.logger import log_event
from shared.connection import collection

# Loader to MongoDB
class Loader:
    # configuration
    def __init__(self):
        self.collectin = collection

    # send
    def processor(self):
        message = {"a":"b"}
        try:
            self.collectin.insert_one(message)
            log_event(level="info", message="saved to mongoDB")
        except Exception as e:
            log_event(level="error", message=f"{e}")

if __name__ == '__main__':
    loader = Loader()
    loader.processor()