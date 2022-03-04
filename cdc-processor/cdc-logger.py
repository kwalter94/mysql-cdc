from confluent_kafka import Consumer

import json
import os

KAFKA_HOST = os.environ["KAFKA_HOST"]
KAFKA_PORT = os.environ["KAFKA_PORT"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]

def main():
    consumer = Consumer({"bootstrap.servers": f"{KAFKA_HOST}:{KAFKA_PORT}", "group.id": "cdc-loggers"})
    consumer.subscribe([KAFKA_TOPIC])
    
    log_file = open("log/cdc.log", "w")
    
    try:
        while True:
            cdc_event = consumer.poll(1.0)
            
            if cdc_event is None:
                print("Waiting for cdc events...")
                continue
            
            error = cdc_event.error()
            if error:
                print(f"error: {error}")
                continue
            
            raw_key = cdc_event.key()
            key = raw_key and raw_key.decode('utf-8')

            value = cdc_event.value().decode('utf-8')
            
            log = json.dumps({"key": json.loads(key), "value": json.loads(value)}, indent=2)
            print(log, file=log_file, flush=True)
            print(file=log_file, flush=True)
    finally:
        consumer.close()
        log_file.close()

if __name__ == "__main__":
    main()
