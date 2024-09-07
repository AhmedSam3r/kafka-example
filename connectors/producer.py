from confluent_kafka import Producer
import logging


class KafkaProducer:
    def __init__(self, bootstrap_servers) -> None:
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def delivery_report(self, err, msg):
        self.logger.info('At delivery_report')
        if err is not None:
            print(f'Message delivery failed: {err}.')
            self.logger.info(f'Message delivery failed: {err}.')
        else:
            topic = msg.topic()
            partition = msg.partition()
            offset = msg.offset()
            self.logger.info(f"Message delivered to topic:{topic} partition:{partition} & offset {offset}")

    def publish(self, topic, key, msg):
        self.producer.produce(topic, key=key, value=msg,
                              callback=self.delivery_report)
        self.logger.info(f"Publishing topic={topic}, key={key} & msg={msg}")
        # flush functions invokes the delivery report callback
        self.producer.flush()
