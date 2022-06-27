# weather_station
A weather station built with Raspberry Pi Zero

Part 1: Setting up a Raspberry Pi

Watch this video

<https://www.youtube.com/watch?v=yn59qX-Td3E>

Download the Raspberry Pi Operating System (OS) and flash the OS to the SD Drive.

Download Raspberry pi imager to laptop from 

-[  https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/)

Remove the SD card from Raspberry pi.

Insert the SD card into an SD card reader/writer with a USB port. 

Connect the card reader/write to the laptop via USB.

Look for the SD card connection in Explorer.

Open the imager. Choose OS - Raspberry Pi 32 bit.

Choose the CORRECT storage. Select Write.

Set up a Headless Raspberry Pi

To enable a headless setup, turn on SSH, and supply WiFi credentials.

Add 2 files.

1.  SSH file will have no content, its presence in the boot directory signals that SSH should be enabled.

2.  Download the wpa_supplicant.conf file to Desktop.

Open file and edit the ssid, and password. (connect to 2.4GHz network, not a 5G network) to enable Wifi.

Drag both the SSH and the wpa_supplicant file to boot directory of SD drive

Eject the SD drive, and insert it into Raspberry pi 0.

Connect the power cable to the Raspberry Pi.

The green LED should blink.

Open terminal and ping raspberypi and see if it responds.

ssh pi@raspberrypi (password is raspberry).

Find the IP address of the raspberry pi

Run ifconfig, and note down IP address.

Success! Raspberry Pi Zero has been set up with a brand new OS, and can now work headless.

Update packages so the latest packages are loaded on Pi.

To install the newest versions of the packages  run

sudo su -

apt-get update

apt-get upgrade

