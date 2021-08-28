#!/bin/bash

echo "Running automated raspi-config tasks"

echo "What hostname should this raspberry have (example TruPiSmart)"
read host

# Via https://gist.github.com/damoclark/ab3d700aafa140efb97e510650d9b1be
# Execute the config options starting with 'do_' below
grep -E -v -e '^\s*#' -e '^\s*$' <<END | \
sed -e 's/$//' -e 's/^\s*/\/usr\/bin\/raspi-config nonint /' | bash -x -
#

# Drop this file in SD card root. After booting run: sudo /boot/setup.sh

# --- Begin raspi-config non-interactive config option specification ---

# Hardware Configuration
do_boot_wait 0            # Turn on waiting for network before booting
do_boot_splash 1          # Disable the splash screen
do_overscan 1             # Enable overscan
do_camera 0               # Disable the camera
do_ssh 1                  # Enable remote ssh login

# System Configuration
do_configure_keyboard us
do_hostname $host
do_change_timezone Europe/Berin
do_change_locale LANG=en_US.UTF-8

# Don't add any raspi-config configuration options after 'END' line below & do
END

echo "Updating packages"
sudo apt-get update && sudo apt-get -y upgrade

