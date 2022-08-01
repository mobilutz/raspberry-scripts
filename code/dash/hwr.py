#!/usr/bin/env python3
from scapy.all import *
import sys, os
import paho.mqtt.publish as publish
import notify

MQTT_PATH = "dash/hwr"

def arp_display(pkt):
    if pkt.haslayer(DHCP):
        if pkt[Ether].src == "50:f5:da:2f:c2:75": # die MAC Adresse des Button mit Kleinbuchstaben!
            notify.publish_message(MQTT_PATH, 'true')

print(sniff(prn=arp_display, store=0,count=0))
