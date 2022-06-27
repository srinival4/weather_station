# weather_station
A weather station built with Raspberry Pi Zero

Part 1: Setting up a Raspberry Pi
----------------------------------

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

exit

Change the password on Raspberry Pi, to increase security.

Run raspi-config

Go to system options, change password.

sudo reboot

Connect remotely to pi.

ssh pi@raspberrypi

Connect over VNC to use remote desktop.

ifconfig raspberrypi to get IP address. Note it down.

raspi-config

Interface options

Enable VNC server.

Download VNC software from Real VNC

Connect via VNC by putting in the IP address into the VNC Viewer.

Set country and language correctly.

Part 2: Building a basic weather station
-----------------------------------------

The BME280 chip contains sensors for temperature, pressure and humidity.

BME280 Sensor Pinout
--------------------

The BME280 module has only 4 pins that interface it to the outside world. The connections are as follows:

![BME280 Pinout - Temperature Humidity Barometric Pressure Sensor](https://lh6.googleusercontent.com/ieKZVHcG8nV-xfcOcd4dITbolZyQ6WQzwZh1Bq0zCDHiB0xCE60rpdT9n4A3WQlkDCCPufKT83z-K4h6bCD4xARpzsik7VzlL8SNj6nZWGAdEHaJ1K9N9n7abP0ff74YxVuxAd2IhVAq5aTNBg)

VIN is the power supply for the module which can be anywhere between 3.3V to 5V.

GND should be connected to the ground of the Raspberry Pi

SCL is a serial clock pin for I2C interface.

SDA is a serial data pin for I2C interface.

Solder the pins to the chip.


![](https://lh4.googleusercontent.com/d6uSAFebrZWi4tqsfZEkqgMHPwpxb4Py1P5TDGTZ_smDVUJpaH3ZSovsdYIlrFpv6O71ey0z29HguniM5cnZZQAJNr_NWNkw1fGvIIOOh5_uHf9DEl_7sOHGef9hkE47plLMtgRD6k8spv6OcQ)

Raspberry Pi Zero GPIO Pin Layout.

![](https://lh6.googleusercontent.com/7W2CdS1i3TBqS4jC1nY1rJlE9Ed8WBpr6_lmek0WRyf6Ib-95WYXHrfXwqeKZXANqiHmsSM3SmytX60w3waag9oW4hX7sj5n7-DiQvSgsP6IQh64Suusb25uBCyw48UFZ-O6-g2TfpP4B5z-uw)

Connect the BME280 chip to the Raspberry pi, as shown below.

![](https://lh5.googleusercontent.com/Ns4gzDhxT0IXfu1ne9YBB0cY71dtYuuRAlAu7VUND6sBm8A2y2faAkoVVv_VbpqkV4cg4APsLiX6Qiy8u8dxh8ksb5BMPfuGssu4cPBNFpIGq5nMSmVgFFKXH0E3iK5-WBC2ZgE3FdFFzt5Cow)


Part 3: Enable I2CBus
----------------------

Enable the I2C interface on the Raspberry Pi.

The I2C Bus allows multiple devices to be connected to the Raspberry Pi, each with a unique address. It is very useful to see which devices are connected to the Pi using i2cdetect.

Run i2cdetect to ensure that  the BME280 chip can be detected, and note down the bus address to be scanned. This bus address will be used in the python program to talk to the BME280 chip.

 sudo i2cdetect -y 1

Install the right python packages to talk to the BME280 chip

sudo pip install RPi.bme280 smbus

Part 4: Collecting weather readings programmatically
-----------------------------------------------------

Download and edit (to change file paths)  the python program (weatherstation.py) to read the temperature, pressure and humidity values from the chip, and write the values to a csv file. Add a loop to the program, so that weather readings are taken at intervals of 30 minutes.Program is set to collect data 10 times at half hour intervals. Store the collected weather results in a local csv file on the Raspberry Pi.

Run the python program as a background process. 

python weatherstation.py &

Transfer the csv file to laptop.

 scp pi@raspberrypi:/home/pi/Documents/readings.csv .

 <put the changed password for pi> to allow the transfer

