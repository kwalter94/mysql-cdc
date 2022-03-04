FROM python:3

WORKDIR /opt/cdc-processor

RUN apt-get update && apt-get install librdkafka-dev -y
RUN pip install confluent-kafka

COPY cdc-logger.py /opt/cdc-processor/cdc-logger.py

CMD ["python", "/opt/cdc-processor/cdc-logger.py"]
