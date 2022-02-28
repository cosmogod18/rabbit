#!/usr/bin/env python3

import pika
import time

####
### DECLARE VARIABLES ### 
####

USER = 'testuser'
PASSWORD = 'testuserpassword'
EXCHANGE = 'test_exchange'
QUEUE= 'test_queue'
ROUTING_KEY = 'test_key'
BODY = 'Hello RabbitMQ :)'
VIRTUAL_HOST = '/myvirtualhost'

def make_request(virtualhost, exchange, queue, routing_key, user, password, body):
    try:
        credentials = pika.PlainCredentials(user,password)
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,virtualhost, credentials=credentials))
        channel = connection.channel()
        # Declare Exchange and queue 
        channel.exchange_declare(exchange=exchange,durable=True, exchange_type='direct')
        channel.queue_declare(queue=queue, durable=True, arguments={'x-message-ttl': 3600000})
        #Bind exchange to queue
        channel.queue_bind(exchange=exchange, queue=queue, routing_key=routing_key)
        time.sleep(3)       
        channel.basic_publish(exchange=exchange, routing_key=routing_key, body=body)
        print(f'Connected to RabbitMQ virtualhost: {virtualhost}\n')
        print(f'### REQUEST SETTINGS ###\nExchange name: {exchange} \nRouting key: {routing_key}\nMessage: {body}')
        print('### REQUST SETTINGS END ###\n')
        connection.close()
        print('Message sent, Connection closed')
    except Exception as error:
        print(error)

if __name__== "__main__":
    make_request(VIRTUAL_HOST, EXCHANGE, QUEUE, ROUTING_KEY, USER, PASSWORD, BODY)
