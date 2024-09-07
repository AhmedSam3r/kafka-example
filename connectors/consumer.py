from confluent_kafka import Consumer, KafkaError
import logging


class KafkaConsumer:
    def __init__(self, bootstrap_servers, group_id=None,
                 offset_reset='earliest'):
        self.consumer = Consumer({
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': offset_reset,
        })
        print("STARTING CONSUMER")
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        self.subscribe_to_topic()

    def subscribe_to_topic(self, topic: str = 'order_notification'):
        self.consumer.subscribe([topic])
        self.logger.info(f'Subscribed to topic: {topic}')

    def process_message(self, msg):
        try:
            decoded_message = msg.value().decode('utf-8')
            print(f'Received message from partition {msg.partition()}: {decoded_message} & offset: {msg.offset()}')
            print(f"TESTING TIMESTAMP {msg.timestamp().decode('utf-8')}")
        except Exception as e:
            print(f'Error decoding message: {e}')

    def poll(self):
        i = 0
        try:
            while True and i < 3:
                msg = self.consumer.poll(5.0)
                if msg is None:
                    i+=1
                    self.logger.info('Message is None')
                    continue

                if msg.error():
                    self.logger.error(f'Error in message processing: {str(msg.error())}')
                    # what is this part ?
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        self.logger.info("PARTITION EOF")
                        continue

                self.process_message(msg)
                i += 1
        finally:
            pass

    def close_subscribe_connection(self):
        print("CLOSING CONSUMER")
        self.consumer.close()
