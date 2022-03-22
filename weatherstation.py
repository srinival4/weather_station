#import the correct libraries
import bme280
import smbus2

import logging
import time
from time import sleep
import datetime
from datetime import date

#from openpyxl import load_workbook

#set up logging

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Chip:
    #function to intialize chip
    def __init__(self):
        self._port = 1
        self.bus = smbus2.SMBus(self._port)
        self.address = 0x76 #Adafruit BME280 address
        
    #function to take a reading
    def read_chip(self):
        self.humidity = round(bme280_data.humidity,2)
        self.pressure = round(bme280_data.pressure,2)
        self.ambient_temperature = round(bme280_data.temperature,2)
        
        
    def write_chip_reading_with_datetime(self, wl):
        today = date.today()
        now = time.strftime("%H:%M:%S")
        print(today, now, self.humidity, self.pressure, self.ambient_temperature)
        wl.write("{0},{1},{2},{3},{4}\n".format(today, now, self.humidity,self.pressure, self.ambient_temperature))

reading = 1
BME280 = Chip()

try:
    with open("/home/pi/Documents/readings.csv", "a") as weatherlog:
        weatherlog.write("Date," + "Time," + "Humidity," + "Pressure," + "Temperature" +"\n")
        while(reading < 40):
            bme280_data = bme280.sample(BME280.bus,BME280.address)
            if (bme280_data) is None:
                logging.debug("No reading from sensor")
                break;
            BME280.read_chip()
            BME280.write_chip_reading_with_datetime(weatherlog)
            reading += 1
            sleep(1800)
        
finally:
    weatherlog.close()
    print('Goodbye!')
