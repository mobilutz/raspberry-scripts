#!/bin/sh


# Save everyting to the NAS
/sbin/runuser -u pi /home/pi/backupToNAS.sh >> /var/log/rsnapshot.log

# Notify that backup finished
python3 /home/pi/code/raspi/backup-finished.py

# Shutdown unless it is a test run!
if test -f /home/pi/runBackupOnceBefore21h; then
	mv /home/pi/runBackupOnceBefore21h /home/pi/runBackupOnceBefore21h.done
else
	python3 /home/pi/code/raspi/shutdown.py
	/sbin/shutdown -h +1 &
fi
