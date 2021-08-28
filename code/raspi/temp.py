#!/usr/bin/env python3
import paho.mqtt.publish as publish
from subprocess import check_output
from re import findall
import socket

MQTT_SERVER = "mqtt.tru.net"

def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    return(findall("\d+\.\d+",temp)[0])

def publish_message(topic, message):
    print("Publishing to MQTT topic: " + topic)
    print("Message: " + message)

    publish.single(topic, message, hostname=MQTT_SERVER)

temp = get_temp()
publish_message('pies/'+socket.gethostname()+'/temperature', temp)
