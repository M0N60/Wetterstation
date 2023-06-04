
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

from rotary import Rotary


# ADC stuff (unsicher)
#sudo raspi-config # um den I2C zu aktiviren 
#sudo pip3 install adafruit-circuitpython-ads1x15 # um die biblo herunterzuladen
#nano KY053ADC.py # erstellt eine neue Datei auf Ihrem Raspberry Pi 
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# ADC stuff (unsicher)
# Den I2C-Bus erstellen
i2c = busio.I2C(board.SCL, board.SDA) #  oder  I²C adress (via Jumper configurable) 0x48 - 0x4B
# Single-Ended-Eingang auf Kanälen erstellen
chan0 = AnalogIn(ads, ADS.P0) # RAIN_SEN
chan1 = AnalogIn(ads, ADS.P1) # FOTO_TRANSISTOR
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)


#GPIOs von der Lichtschranke
ledpin = 24  
relaispin = 17

# GPIOs zum Rotary Encoder
pin_dt = 18
pin_clk = 19
pin_sw = 17

# Initialiserung Rotary Encoder
rotary = Rotary(pin_dt, pin_clk, pin_sw)
value = 0

# zähler für bestimte funktionen 
anzahl_an_öffnungen  = 0 # um den niederschalag zu messen
anzahl_an_umdrehungen = 0 # um die anzahl an umdrehungen zu messen


# wert bestimmung wo es auslösen soll 
schalt_wert_feutigkeit = 500
schalt_wert_lichtschranke = 500

# Werte für Rechnungen
niederschlagswert = 0


# BCM-Nummerierung verwenden
GPIO.setmode(GPIO.BCM)

# einzelen Ein und Ausgänge deklariren 
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(relaispin, GPIO.OUT)


# ab hier kommen eigen funktionen

# ADC stuff (unsicher)

def wert_A0 (): # RAIN_SEN
    #print(chan0.value)
    return(chan0.value)

def wert_A1 (): # FOTO_TRANSISTOR
    #print(chan1.value)
    return(chan1.value)



# bme
def bme_rotine():
    port = 1
    address = 0x77 # Adafruit BME280 address. Other BME280s may be different
    bus = smbus2.SMBus(port)
    bme280.load_calibration_params(bus,address)
    bme280_data = bme280.sample(bus,address)
    # das obere sollte aus dem loop raus 
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    print("Die Luftfeuchtigkeit beträgt: ", humidity, "%")
    print("Der Luftdruck liegt bei: ", pressure, "hPa")
    print( "Die Außentemperatur beträgt: ", ambient_temperature, "°C")
    return(humidity, pressure, ambient_temperature) # nicht notwendig ? 



# niederschlag (mit ADC)

def niederschlag_rotine(anzahl_an_öffnungen, niederschlagswert):
    if wert_A0 () >= schalt_wert_feutigkeit: # (mit ADC ?)
        GPIO.output(relaispin, GPIO.LOW) 
        anzahl_an_öffnungen += 1 
    else:
        GPIO.output(relaispin, GPIO.HIGH) 
    niederschlagswert = anzahl_an_öffnungen * niederschlagsmenge  # Herausfinden, wie viel ml in dem Beh�lter sind und auf Quadratmeter umrechnen! ml pro qm in 24h
    print("Der Niederschlag beträgt: ", niederschlagswert, "ml pro qm")
    return (anzahl_an_öffnungen) # nicht notwendig ? 
    

# windgeschwindikeit (mit ADC)
def windgeschwindikeit_rotine(anzahl_an_umdrehungen):
    if wert_A1 () >= schalt_wert_lichtschranke: # (mit ADC ?)
        anzahl_an_umdrehungen += 1 
    else:
        pass
    GPIO.output(ledpin, GPIO.HIGH)
    print("Die Windgeschwindigkeit beträgt: ", anzahl_an_umdrehungen, "km/h")
    return (anzahl_an_umdrehungen) # nicht notwendig ? 


# Funktion
# Angenommen, Position 0/20 ist Norden, 10 = S�den, 5 = Osten, 15 Westen 
# 19-1 Nord, 2,3 NO, 4-6 Ost, 7,8 SO, 9-11 S�d, 12,13 SW, 14-16 West, 17,18 WN 


def windrichtung_rotine(change):        
    # das gibt die encoder werte (0-20 ) wieder
    global value                       
    if change == Rotary.ROT_CW:
        value = value + 1
    elif change == Rotary.ROT_CCW:
        value = value - 1
    else:
        pass
    # ab heir gebne wier den werten (0-20) einen Namen
    if value == 0  :  
        return("Norden")
    elif value == 19:
        return("Norden")
    elif value == -19:                  
        return("Norden")
    elif value == 1:
        return("Norden")
    elif value <= -17:           # gleiche Position wie 3
        return("Nordosten")
    elif value <= -14:           # 6
        return("Osten")
    elif value <= -12:
        return("Südosten")
    elif value <= -9:
        return("Süden")
    elif value <= -7:
        return("Südwesten")
    elif value <= -4:
        return("Westen")
    elif value <= -2:
        return("Nordwesten")
    elif value <=3:
        return("Nordosten")
    elif value <=6:
        return("Osten")
    elif value <= 8:
        return("Südosten")
    elif value <= 11:
        return("Süden")
    elif value <= 13:
        return("Südwesten")
    elif value <= 16:
        return("Westen")
    elif value <= 18:
        return("Nordwesten")
    # 19-1 Nord, 2,3 NO, 4-6 Ost, 7,8 SO, 9-11 S�d, 12,13 SW, 14-16 West, 17,18 WN 
    # ab hier setzen wir zurück
    if value == 20:                   # 20 Rotationen auf 360� deswegen nulll setzen 
        value = 0
    elif value == -20:                  # 20 Rotationen auf 360� deswegen nulll setzen (auch wenn es einmal in die anderer Richtung geht )
        value = 0 
    else:
        pass

# Wenn der Encoder bedient wird
rotary.add_handler(rotary_changed)


# Endlosschleife (void loop)
while True: 
    niederschlag_rotine(anzahl_an_öffnungen, niederschlagswert)
    bme_rotine()
    windgeschwindikeit_rotine(anzahl_an_umdrehungen)
    windrichtung_rotine(change)
    print("Der Wind weht nach", windrichtung_rotine(change))
    time.sleep(1) 