
# generell fur Input und Outupt (PIN BELEGUNG) 
# link von : https://pypi.org/project/RPi.GPIO/
import RPi.GPIO as GPIO #sudo apt-get install python-rpi.gpio

# bme bibioteken 
# link von : https://pypi.org/project/smbus2/ ++ https://pypi.org/project/RPi.bme280/
import bme280
import smbus2

# ADC bibioteken 
# link von : https://joy-it.net/files/files/Produkte/COM-KY053ADC/COM-KY053ADC_Anleitung_2023-02-28.pdf
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# array 
# link von : https://numpy.org/doc/stable/index.html
import numpy as np

# plotter 
# link von : https://matplotlib.org/
import matplotlib.pyplot as plt

# time stuff (locale zeit und delay)
# link von : https://docs.python.org/3/library/time.html
import time
