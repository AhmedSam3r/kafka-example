from connectors.consumer import KafkaConsumer  # Adjust the import based on your file structure
bootstrap_servers = 'localhost:9092'
kafka_consumer = KafkaConsumer(bootstrap_servers, 'my_consumer_group')

if __name__ == "__main__":
    kafka_consumer.subscribe_to_topic('kafka_with_django')  # Make sure it matches the producer's topic
    print('subscribed')
    kafka_consumer.poll()
    print('poll done')
