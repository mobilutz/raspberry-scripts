#!/bin/sh

# Set the time correctly
/usr/sbin/ntpd -q -g >> /var/log/rsnapshot.log

# Notify iobroker that a backup is being started
python3 /home/pi/code/raspi/backup-started.py

python3 /home/pi/code/raspi/startup.py

df -h /mnt/usbdisk/ >> /var/log/rsnapshot.log

# Add a sleep for the pi to startup completely.
# For successful RSYNC we need to have this!!!
sleep 60
