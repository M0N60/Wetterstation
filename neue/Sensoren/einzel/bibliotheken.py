import RPi.GPIO as GPIO #sudo apt-get install python-rpi.gpio
# bme 
import bme280
import smbus2
# ADC 
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Diagramm
import numpy as np

import matplotlib.pyplot as plt

# time (locale zeit und delay)
import time
