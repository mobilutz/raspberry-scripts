#!/usr/bin/env python3
import notify
from subprocess import check_output
from re import findall
from datetime import datetime
import socket

def get_uptime():
	temp = check_output(["uptime","-p"]).decode("UTF-8")
	return(temp)

def get_current():
	now = datetime.now()
	return(now.strftime("%Y/%m/%d, %H:%M:%S"))

temp = get_uptime()
notify.publish_message('pies/'+socket.gethostname()+'/uptime', temp)

time = get_current()
notify.publish_message('pies/'+socket.gethostname()+'/time', time)
