import time
import random

class EdgeNode:
    def __init__(self):
        self.device_id = "EdgeNode-001"

    def collect_data(self):
        temperature = random.uniform(20.0, 30.0)
        humidity = random.uniform(50.0, 70.0)
        return {"temperature": temperature, "humidity": humidity}

    def process_data(self, data):
        return f"Processed data: {data}"

    def run(self):
        while True:
            data = self.collect_data()
            result = self.process_data(data)
            print(result)
            time.sleep(5)

if __name__ == "__main__":
    node = EdgeNode()
    node.run()
