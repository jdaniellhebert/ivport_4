# meccam2

#### Copy image to SD Card using Hypriot flash command (MacOS)
```
$ diskutil list   # Lists mounted drives.  Make a note of the disk # of the SD card.  
$ flash --hostname <unique-rpi-hostname> --ssid <Your-Wifi-SID> --password <Your-Wifi-Password> http://downloads.hypriot.com/hypriotos-rpi-v1.0.0.img.zip  

# Modify the fields above that are delinated by "<>" with a unique hostname and wifi creditionals.
# WARNING: flash will prompt you to double check the SD card disk #, take care.

# Example:  
$ flash --hostname cam1 --ssid "58 Eero" --password aubinriopumpernickel https://downloads.raspberrypi.org/raspbian_lite_latest

when prompted for password: type in password of machine you are doing this build on.
