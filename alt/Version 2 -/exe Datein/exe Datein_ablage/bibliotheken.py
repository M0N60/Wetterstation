# Dinge die so gehen sollten 


# generell fur Input und Outupt (PIN BELEGUNG) ++ delay funkion 
# link von : https://www.elektronik-kompendium.de/sites/raspberry-pi/2611151.htm 
import RPi.GPIO as GPIO #sudo apt-get install python-rpi.gpio
import time

# bme bibioteken 
# link von : https://core-electronics.com.au/guides/piicodev-atmospheric-sensor-bme280-raspberry-pi-guide/ 

import bme280
import smbus2

# Rotory_Encoder bibioteken
# link von : https://www.elektronik-kompendium.de/sites/raspberry-pi/2703131.htm 

from rotary import Rotary  # bin mir nicht sicher ob die so richtig eingebunden wurde XD


# ADC stuff (unsicher)
#sudo raspi-config # um den I2C zu aktiviren 
#sudo pip3 install adafruit-circuitpython-ads1x15 # um die biblo herunterzuladen
#nano KY053ADC.py # erstellt eine neue Datei auf Ihrem Raspberry Pi 
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


# plotter stuff
import matplotlib.pyplot as plt
import numpy as np