#!/bin/bash

# 
# Install python dependences
#
apt update
apt install ansible python3-pip git -y
pip3 install pika
