from confluent_kafka import Producer
import json

conf = {
    'boostrap.servers':'localhost:9092',
    'client.id':'flask-producer'
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'[Kafka ERORR] Delivery failed: {err}')
    else:
        print(f'[Kafka OK] {msg.topic()} [{msg.partition()}] {msg.value()}')

def sent_to_kafka(topic: str, message: dict):
    payload = json.dumps(message).encode('utf-8')
    producer.produce(topic=topic, value = payload, callback=delivery_report)
    prodcuer.flush()