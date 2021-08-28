#!/bin/sh

# Setup time correctly
/usr/sbin/ntpd -q -g

currentHour24=`date +%H`
currentYear=`date +%Y`
lastBackupYear=`tail -1 /home/pi/lastYearlyBackup.txt`

# Normally the backup only runs when the pi is started after 21:00.
# If it was started before, we check if a backup should run anyways
if test -f /home/pi/runBackupOnceBefore21h; then
	currentHour24=23
fi


if [ $currentHour24 -gt 21 ]; then
	# First run on the year?
	if [ $currentYear -gt $lastBackupYear ]; then
		# Save new year in file
		echo $currentYear >> /home/pi/lastYearlyBackup.txt

		# rotate yearly snapshot
		/usr/bin/rsnapshot yearly
	fi

	# Do the weekly snapshot
	/usr/bin/rsnapshot weekly
fi
