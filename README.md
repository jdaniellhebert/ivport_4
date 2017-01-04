# meccam2

#### Copy Raspbian image to SD Card with Etcher Application (MacOS)
* Download application:  https://etcher.io/
* Download latest Raspbian from Rpi foundation: https://www.raspberrypi.org/downloads/raspbian/ (Lite version)
* Run Etcher Application and copy to SD card.

#### Set up headless boot Wifi credentials and enable SSH for initial boot from SD card
The boot partition on a Pi should be accessible from any machine with an SD card reader, on Windows, Mac, or Linux. 

* To set the Wifi credentials copy a file called "wpi_supplicant.conf" to the /boot/ directory on the SD card.  The file should contain the following:
```
network={
  ssid="The_ESSID_from_earlier"
  psk="Your_wifi_password"
}
```
* If you want to enable SSH, all you need to do is to put a file called ssh in the /boot/ directory. The contents of the file don’t matter: it can contain any text you like, or even nothing at all. When the Pi boots, it looks for this file; if it finds it, it enables SSH and then deletes the file.  On first boot run raspi-config to enable SSH.
```
$ cd /Volumes/boot
$ touch ssh
```
* Both the ssh file and the wpi_supplicant.conf file will be deleted on first boot after they are used.

#### Boot RPI with SD card
* Run "My Net" application to find IP address of RPI.
* Then SSH to pi@<IP address>
```
$ ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no pi@<IP address> # password: raspberry
```
#### Configure RPI
* Once connected to RPI use raspi-config to change:
 * expand filesystem
 * default SSH on
 * enable camera
 * enable I2C
```
$ sudo raspi-config  # change SSH default to on & change the rpi password.
```
#### Enable I2C
```
$ sudo apt-get update
$ sudo apt-get install -y python-smbus i2c-tools
```
```
sudo halt # wait 10 seconds and then unplug and plug back in
```
* When you power up or reboot your Pi you can check the i2c module is running by using the following commands:
```
$ lsmod | grep i2c_  #  If it lists “i2c_bcm2708” then the module is running.
$ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: 20 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
This result shows one device connected and its address is 0x20 (32 in decimal).
```
#### Install IVport
```
$ sudo apt-get install git                              # git may not yet be installed
$ git clone https://github.com/ivmech/ivport-v2.git     # clone ivport v2
$ sudo apt-get install python-smbus                     # in case this is not installed

$ sudo apt-get remove python-picamera                   # uninstall picamera because IVport v2 updates this
$ sudo apt-get install python-pip                       # install pip
$ sudo pip uninstall picamera

$ sudo apt-get update
$ sudo apt-get upgrade                                   # you may have to use the switch:  --fix-missing
$ sudo apt-get dist-upgrade
$ sudo apt-get install rpi-update
$ sudo rpi-update                                        # update firmware
```
#### Usage
```
$ cd ivport-v2
$ python init_ivport.py

$ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: 10 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- 64 -- -- -- -- -- -- -- -- -- -- --
70: 70 -- -- -- -- -- -- --
#  You should get both 0x70 and 0x64 as addresses of respectively ivport v2 and camera module v2.
$ vcgencmd get_camera
supported=1 detected=1

```

#### Links
* https://github.com/hypriot/flash
* https://www.raspberrypi.org/blog/a-security-update-for-raspbian-pixel/
* https://www.arrow.com/en/research-and-events/articles/headless-setup-for-your-raspberry-pi-3
* http://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/
