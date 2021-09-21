from kafka import KafkaConsumer

consumer = KafkaConsumer('assignmentTopic1',bootstrap_servers=['localhost:9092'],auto_offset_reset="earliest",enable_auto_commit=True)

for message in consumer:
    print(message.value.decode('UTF-8'))