#!/usr/bin/env python3

import pika

EXCHANGE = 'myexchange'
ROUTING_KEY = 'mykey'
BODY = 'Hello RabbitMQ :)'
VIRTUAL_HOST = 'myvirtualhost'

def make_request(virtualhost, exchange, routing_key, body):
    try:
        credentials = pika.PlainCredentials('tomas','cosmogod')
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,virtualhost, credentials=credentials))
        channel = connection.channel()
        print(f'Connection on RabbitMQ virtualhost: {virtualhost}\n')
        channel.basic_publish(exchange=exchange, routing_key=routing_key, body=body)
        print(f'### REQUEST SETTINGS ###\nExchange name: {exchange} \nRouting key: {routing_key}\nMessage: {body}')
        print('### REQUST SETTINGS END ###\n')
        connection.close()
        print('Message sent, Connection closed')
    except Exception as error:
        print(error)

if __name__== "__main__":
    make_request(VIRTUAL_HOST, EXCHANGE, ROUTING_KEY, BODY)
