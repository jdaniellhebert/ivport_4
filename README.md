# meccam2

###  Build Docker Image via SD card
#### Install Hypriot flash command (MacOS)
```
$ brew install pv  
$ brew install awscli  

$ curl -O https://raw.githubusercontent.com/hypriot/flash/master/$(uname -s)/flash  
$ chmod +x flash  
$ sudo mv flash /usr/local/bin/flash  
```
#### Copy Raspbian image to SD Card using Hypriot flash command (MacOS)
```
$ diskutil list   # Lists mounted drives.  Make a note of the disk # of the SD card.  
$ flash --hostname <unique-rpi-hostname> --ssid <Your-Wifi-SID> --password <Your-Wifi-Password> http://downloads.hypriot.com/hypriotos-rpi-v1.0.0.img.zip  

# Modify the fields above that are delinated by "<>" with a unique hostname and wifi creditionals.
# WARNING: flash will prompt you to double check the SD card disk #, take care.

# Example:  
$ flash --hostname cam1 --ssid "58 Eero" --password aubinriopumpernickel https://downloads.raspberrypi.org/raspbian_lite_latest

when prompted for password: type in password of machine you are doing this build on.
```
#### Enable SSH for initial boot from SD card
The boot partition on a Pi should be accessible from any machine with an SD card reader, on Windows, Mac, or Linux. If you want to enable SSH, all you need to do is to put a file called ssh in the /boot/ directory. The contents of the file don’t matter: it can contain any text you like, or even nothing at all. When the Pi boots, it looks for this file; if it finds it, it enables SSH and then deletes the file.  On first boot run raspi-config to enable SSH.

In MacOS bash shell:
```
$ cd /Volumes/boot
$ touch shh
```
Eject flash drive and plug into RPI.  Restart RPI
```
# In MacOS run My Net application (or equivalent) to find IP address.  SSH to IP address of RPI
$ ssh pi@<IP address>
$ password: raspberry

# Once connected to RPI
$ sudo raspi-config  # change SSH default to on.
```

#### Links
* https://github.com/hypriot/flash
* https://www.raspberrypi.org/blog/a-security-update-for-raspbian-pixel/
