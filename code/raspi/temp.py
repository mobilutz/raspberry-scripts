#!/usr/bin/env python3
import notify
from subprocess import check_output, run, getoutput
from re import findall
import socket

def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    return(findall("\d+\.\d+",temp)[0])

def get_ssd_temp():
    temp = getoutput("/usr/sbin/smartctl -A /dev/sda | grep \"194 Temperature_Celsius\" | awk '{print $10}'")
    return temp

temp = get_temp()
notify.publish_message('pies/'+socket.gethostname()+'/temperature', temp)

# uncomment if the raspberry pi has an ssd connected to it
# temp = get_ssd_temp()
# notify.publish_message('pies/'+socket.gethostname()+'/ssd_temperature', temp)
