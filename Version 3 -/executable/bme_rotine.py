# geklauen XD 
# war mit dem normal en os siehe link
#https://core-electronics.com.au/guides/piicodev-atmospheric-sensor-bme280-raspberry-pi-guide/ 

import bme280
import smbus2
from time import sleep

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

humidity  = 0
pressure  = 0
temperature = 0
verbrauche_zeit = 0
anzahl_der_aktivirungen = 0

def bme_rotine():
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    temperature = bme280_data.temperature
    verbrauche_zeit = 0    # insert a funktion that returns the time of the pi´s aktive time
    anzahl_der_aktivirungen += 1
    return(humidity, pressure, temperature , verbrauche_zeit , anzahl_der_aktivirungen) 

# braucht man die ??
def get_bme_humidity():
    return humidity
def get_bme_pressure():
    return pressure
def get_bme_temperature ():
    return temperature 
def get_bme_verbrauche_zeit():
    return verbrauche_zeit
def get_bme_anzahl_der_aktivirungen():
    return anzahl_der_aktivirungen