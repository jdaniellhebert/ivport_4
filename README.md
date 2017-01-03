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
* Both files will be deleted on first boot after they are used.

In MacOS bash shell:

Eject flash drive and plug into RPI.  Restart RPI
```
# In MacOS run My Net application (or equivalent) to find IP address.  SSH to IP address of RPI
$ $ ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no pi@<IP address>
$ password: raspberry

# Once connected to RPI
$ sudo raspi-config  # change SSH default to on & change the rpi password.
```

#### Links
* https://github.com/hypriot/flash
* https://www.raspberrypi.org/blog/a-security-update-for-raspbian-pixel/
* https://www.arrow.com/en/research-and-events/articles/headless-setup-for-your-raspberry-pi-3
