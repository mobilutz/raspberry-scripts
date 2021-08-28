#!/bin/bash
DATESTR=`date +%F`

NAS_URL='nas.tru.net'

# Copy single files
function copyFile {
 ssh $NAS_URL "mkdir -p $1/$DATESTR"
 scp -p $2 $NAS_URL:$1/$DATESTR
}

# Read from file `toBackup.txt` and save the listed files if they exists.
# NOTE: The need to have UNIX-linefeed
function backupProject {
    for fileToBackup in `cat $2` ; do
        # relative path
        file="`dirname $2`/$fileToBackup"
        if [[ $fileToBackup == *"/"* ]]; then
            # use absolute path
            file="$fileToBackup"
        fi
        if [ -f $file ]; then
            #parameter:     weatherProxy   /home/pi/weatherProxy/main.log
            copyFile `basename $1` $file
        fi
    done
}

# Search in `/home/pi` folder for file `toBackup.txt`
for project in `find ~ -name toBackup.txt` ; do
    backupProject `dirname $project` $project
done
