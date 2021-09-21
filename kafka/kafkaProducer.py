from kafka import KafkaProducer, producer
from kafka.admin import KafkaAdminClient, NewTopic
from json import dumps
from time import sleep


admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092", 
    client_id='test'
)

topic_list = []
topic_list.append(NewTopic(name="assignmentTopic1", num_partitions=3, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x:dumps(x).encode('UTF-8'))

for i in range(1,11):
    producer.send('assignmentTopic1',value={"value":i})
    sleep(3)