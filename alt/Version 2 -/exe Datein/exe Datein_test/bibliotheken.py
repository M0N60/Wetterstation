
# generell fur Input und Outupt (PIN BELEGUNG) 
# link von : https://www.elektronik-kompendium.de/sites/raspberry-pi/2611151.htm 
import RPi.GPIO as GPIO #sudo apt-get install python-rpi.gpio

# bme bibioteken 
# link von : https://core-electronics.com.au/guides/piicodev-atmospheric-sensor-bme280-raspberry-pi-guide/ 
import bme280
import smbus2

# Rotory_Encoder bibioteken
# link von : https://www.elektronik-kompendium.de/sites/raspberry-pi/2703131.htm 
from rotary import Rotary  # bin mir nicht sicher ob die so richtig eingebunden wurde XD


# ADC stuff (unsicher)
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# array stuff (gibt uns übergreifende Diagramm)
import numpy as np

# plotter stuff (ist zum plotten )
import matplotlib.pyplot as plt

# time stuff (locale zeit und delay)
import time
