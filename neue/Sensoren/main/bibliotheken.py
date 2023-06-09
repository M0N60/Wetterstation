import RPi.GPIO as GPIO 
#BME
import bme280
import smbus2
#ADC
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#Diagramme
import numpy as np
import matplotlib.pyplot as plt

import time
