# Kafka FastAPI Experiment

This is an experimental project that demonstrates the use of Kafka producers and consumers within a FastAPI application. The project showcases how to produce and consume messages from Kafka topics using the `confluent_kafka` Python client. This is not intended for production use but rather for learning and experimentation purposes.

## Features

- **Producer**: Send messages to a specified Kafka topic using FastAPI.
- **Consumer**: Poll messages from a Kafka topic and process them.

## Project Structure

```
.
├── connectors
│   ├── consumer.py             # Kafka consumer logic
│   ├── producer.py             # Kafka producer logic
├── main.py                     # FastAPI app for producing and consuming messages
├── requirements.txt            # Project dependencies
├── script_consumer.py          # Script to manually consume messages
└── venv                        # Python virtual environment (optional)
```

## Prerequisites

Before running the project, ensure that you have the following:

- **Kafka**: Install Apache Kafka on your machine or use a cloud-based Kafka service. Instructions to install Kafka can be found [here](https://kafka.apache.org/quickstart).
- **Python 3.x**: Ensure you have Python 3.x installed.
- **Kafka server**: The Kafka server should be running at `localhost:9092` by default or change the `bootstrap_servers` setting in the code to match your Kafka server.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Set up a Python virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure Kafka is running. If you’re running Kafka locally, start both the **Zookeeper** and **Kafka** servers:
   ```bash
   bin/zookeeper-server-start.sh config/zookeeper.properties
   bin/kafka-server-start.sh config/server.properties
   ```

## Running the FastAPI Application

1. Start the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser or API tool (e.g., Postman) and visit the following endpoints:

   - **Send a message**: 
     ```bash
     GET http://localhost:8000/send_message/{topic}
     ```
     Replace `{topic}` with the name of your Kafka topic. This sends a message to the specified Kafka topic.

   - **Consume messages**: 
     ```bash
     GET http://localhost:8000/consume_messages/{topic}
     ```
     Replace `{topic}` with the name of the Kafka topic from which you want to consume messages.

## Running the Kafka Consumer Script

You can also manually consume messages using the `script_consumer.py` script:

1. Run the consumer script:
   ```bash
   python script_consumer.py
   ```
   This script consumes messages from the `kafka_with_django` topic.

## Notes

- This is an **experimental project** for testing Kafka integration with FastAPI.
- The default Kafka topic in the code is `order_notification`. Ensure that this topic exists in your Kafka server, or adjust the topic names as needed in the code.
- The consumer will only poll 3 messages before terminating, adjust this logic in `consumer.py` if needed.
  
## License

This project is open-source and available for experimentation. No license is applied.

---

Feel free to modify this as needed for your specific project.
