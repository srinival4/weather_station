#!/usr/bin/python
#import the correct libraries
import bme280
import smbus2
import logging

import time
from time import sleep
import datetime
from datetime import date

logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
                
class Chip:
    def __init__(self):   
        self._port = 1
        self.bus = smbus2.SMBus(self._port)
        self.address = 0x76 #Adafruit BME280 address
  
    def reading(self):
        self.humidity = round(bme280_data.humidity,2)
        self.pressure = round(bme280_data.pressure,2)
        self.ambient_temperature = round(bme280_data.temperature,2)      

    def append_reading_with_datetime(self, w_log):
        today = date.today()
        now = time.strftime("%H:%M:%S")        
        print(today, now, self.humidity, self.pressure, self.ambient_temperature)
        w_log.write("Date: {0}\n\nTime: {1}\n\nHumidity: {2}\n\nPressure: {3}\n\nTemperature: {4}\n".format(today, now, self.humidity,self.pressure, self.ambient_temperature))

BME280 = Chip()

try:
    with open("/home/pi/linda_proj/current_weather.txt", "w") as w_log:
        bme280_data = bme280.sample(BME280.bus,BME280.address)
        if (bme280_data) is None:
            logging.debug("No reading from sensor")
        BME280.reading()
        BME280.append_reading_with_datetime(w_log)

    
finally:
    w_log.close()
    print('Goodbye!')
