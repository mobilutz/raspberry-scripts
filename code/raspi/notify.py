#!/usr/bin/env python3
import argparse
import paho.mqtt.publish as publish
from subprocess import check_output
from re import findall
import socket

MQTT_SERVER = "mqtt.tru.net"

#parser = argparse.ArgumentParser(description='Send message to ioBroker/MQTT')
#parser.add_argument('path', help='Path the message is being send to.')
#parser.add_argument('message', help='Message to send.')

#args = parser.parse_args()

#print(args)

def datetime_to_int(dt):
    return int(dt.strftime("%Y%m%d%H%M%S"))

def publish_message(path, message):
    topic = 'pies/'+socket.gethostname()+'/'+path
    print("Publishing to MQTT topic: " + topic)
    print("Message: " + message)

    publish.single(topic, message, hostname=MQTT_SERVER)

#publish_message(args.path, args.message)
