# Data Storage /project/db/rabbitMQ.py
import json
import os
import pika

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = os.getenv('RABBITMQ_PORT', '5672')
RABBITMQ_USER = os.getenv('RABBITMQ_USER', 'PRIME')
RABBITMQ_PASS = os.getenv('RABBITMQ_PASS', 'PRIME')

class RabbitMQ:
    """Class to rabbit MQ"""
    # SEND Logs to RabbitMQ.
    def sendLogES(self, dataInfo, exchangeName, routing_keyName):
        """Method for send data to rabbit mq"""
        # RABBIT MQ
        try:
            credentials = pika.PlainCredentials(username=RABBITMQ_USER, password=RABBITMQ_PASS)
            parameter = pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT,
                                                  credentials=credentials, socket_timeout=300)
            connection = pika.BlockingConnection(parameter)
            channel = connection.channel()
            channel.queue_declare(queue=routing_keyName, passive=False, durable=True,
                                  exclusive=False, auto_delete=False)
            channel.queue_bind(exchange=exchangeName,
                               queue=routing_keyName)
            channel.basic_publish(exchange=exchangeName,
                                  routing_key=routing_keyName,
                                  body=json.dumps(dataInfo))
            print(" [x] DATA  Send  in Rabbit")
            connection.close()
            return True
        except Exception as e:
            return False