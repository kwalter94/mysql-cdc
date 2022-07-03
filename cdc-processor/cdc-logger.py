from confluent_kafka import Consumer

import json
import os

KAFKA_HOST = os.environ["KAFKA_HOST"]
KAFKA_PORT = os.environ["KAFKA_PORT"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]

def main():
    print("Starting CDC consumer")
    consumer = Consumer({
        "bootstrap.servers": f"{KAFKA_HOST}:{KAFKA_PORT}",
        "group.id": "CDC-loggers",
        "auto.offset.reset": "earliest",
    })
    consumer.subscribe([KAFKA_TOPIC])
    
    log_file = open("log/CDC.log", "w")
    
    try:
        while True:
            CDC_event = consumer.poll()
            
            if CDC_event is None:
                print("Waiting for CDC events...")
                continue
            
            error = CDC_event.error()
            if error:
                print(f"Error: {error}")
                continue
                
            print(f"Decoding CDC event: {CDC_event}")
            raw_key = CDC_event.key()
            key = raw_key and raw_key.decode('utf-8')

            value = CDC_event.value().decode('utf-8')
            
            log = json.dumps({"key": json.loads(key), "value": json.loads(value)}, indent=2)
            print(f"Decoded CDC event: {log}")
            print(log, file=log_file, flush=True)
            print(file=log_file, flush=True)
    finally:
        consumer.close()
        log_file.close()

if __name__ == "__main__":
    main()
