from fastapi import FastAPI, Query
from connectors.producer import KafkaProducer
from connectors.consumer import KafkaConsumer

app = FastAPI()


bootstrap_servers = 'localhost:9092'
global_counter = 0
kafka_consumer = KafkaConsumer(bootstrap_servers, 'my_consumer_group', o)
kafka_producer = KafkaProducer(bootstrap_servers)


@app.get("/send_message/{topic}")
async def send_message(topic: str):
    global global_counter
    value = f"NEW global_counter #{global_counter}".encode("utf-8")
    kafka_producer.publish(topic, key="",
                           msg=value)
    global_counter += 1
    return {"status": "Message sent successfully"}


def consume_messages(topic: str):
    kafka_consumer.subscribe_to_topic(topic)
    kafka_consumer.poll()
    return {"status": "Consumed messages"}


@app.get("/consume_messages/{topic}")
async def consume_messages_endpoint(
    topic: str
    # topic: str = Query("order_notification", title="Kafka Topic", description="Specify the Kafka topic to consume")
):
    print("TOPIC IS = ", topic)
    result = consume_messages(topic)
    return result
