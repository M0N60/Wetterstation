
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
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


# plotter stuff
import matplotlib.pyplot as plt
import numpy as np



# ADC stuff (unsicher)
# Den I2C-Bus erstellen
i2c = busio.I2C(board.SCL, board.SDA) #  oder  I²C adress (via Jumper configurable) 0x48 - 0x4B

# Erstellen des ADC-Objekts über den I2C-Bus
ads = ADS.ADS1115(i2c)

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
niederschlagsmenge = 0




# Arrays 
x_Luftfeuchtigkeit_Wert = np.array([0, 0, 0, 0, 0])
x_Luftdruck_Wert = np.array([0, 0, 0, 0, 0])
x_Temperatur_Wert = np.array([0, 0, 0, 0, 0])

y_BME_Time = np.array([0, 0, 0, 0, 0])


x_Windstärke_Wert = np.array([0, 0, 0, 0, 0])
y_Windstärke_Time = np.array([0, 0, 0, 0, 0])


x_Niederschlag_Wert = np.array([0, 0, 0, 0, 0])
y_Niederschlag_Time = np.array([0, 0, 0, 0, 0])

x_Windrichtung_Wert = np.array([0, 0, 0, 0, 0])
y_Windrichtung_Time = np.array([0, 0, 0, 0, 0])


x_Windrichtung_Wert = np.array([0, 0, 0, 0, 0])
y_Windrichtung_Time = np.array([0, 0, 0, 0, 0])




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

    x = x_Luftfeuchtigkeit_Wert.view()
    x[i] = humidity
    i += 1

    x = x_Luftdruck_Wert.view()
    x[j] = pressure
    j += 1
    
    x = x_Temperatur_Wert.view()
    x[k] = ambient_temperature
    k += 1

    y = y_BME_Time.view()
    y[l] = function # dieses musss zu einer geändert werden die die zeit überegibt 
    l +=1

    return



# niederschlag (mit ADC)

def niederschlag_rotine(anzahl_an_öffnungen, niederschlagswert, niederschlagsmenge):
    if wert_A0 () >= schalt_wert_feutigkeit: # (mit ADC ?)
        GPIO.output(relaispin, GPIO.LOW) 
        anzahl_an_öffnungen += 1 
    else:
        GPIO.output(relaispin, GPIO.HIGH) 
    niederschlagswert = anzahl_an_öffnungen * niederschlagsmenge  # Herausfinden, wie viel ml in dem Beh�lter sind und auf Quadratmeter umrechnen! ml pro qm in 24h
    
    x = x_Niederschlag_Wert.view()
    x[o] = anzahl_an_öffnungen
    o += 1
    return 
    

# windgeschwindikeit (mit ADC)
def windgeschwindikeit_rotine(anzahl_an_umdrehungen):
    if wert_A1 () >= schalt_wert_lichtschranke: # (mit ADC ?)
        anzahl_an_umdrehungen += 1 
    else:
        pass
    GPIO.output(ledpin, GPIO.HIGH)

    x = x_Windstärke_Wert.view()
    x[p] = anzahl_an_öffnungen
    p += 1

    return 


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
rotary.add_handler(windrichtung_rotine)





def Luftdruck_ploter():

    daten_x = x_Luftdruck_Wert.view()
    daten_y = y_BME_Time.view()

    # plottet den Graphen (x , y , color , marker, linestyle, linewidth )
    plt.plot(daten_x, daten_y , color = 'red', marker = 'x', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Luftdruck in hPa')

    # titel über dem graphen
    plt.title('Luftdruck')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('Luftdruck.png')


def Niederschlag_ploter():
    
    daten_x = x_Niederschlag_Wert
    daten_y = y_Niederschlag_Time


    # plottet den Balken (x , y , color , marker, linestyle, linewidth )
    plt.bar(daten_x, daten_y , color = 'b', marker = '_', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Niederschlag in ml pro qm')

    # titel über dem graphen
    plt.title('Niederschlag')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('Niederschlag.png')

def Luftfeuchtigkeit_ploter():

    daten_x = x_Luftfeuchtigkeit_Wert.view()
    daten_y = y_BME_Time.view()

    # plottet den Graphen (x , y , color , marker, linestyle, linewidth )
    plt.plot(daten_x, daten_y , color = 'red', marker = 'x', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Luftfeuchtigkeit in %')

    # titel über dem graphen
    plt.title('Luftfeuchtigkeit')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('Luftfeuchtigkeit.png')




def Windstärke_ploter():
    
    daten_x  = x_Windstärke_Wert
    daten_y =  y_Windstärke_Time

    # plottet den Graphen (x , y , color , marker, linestyle, linewidth )
    plt.plot(daten_x, daten_y , color = 'red', marker = 'x', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Windstärke in km/h')

    # titel über dem graphen
    plt.title('Windstärke')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('Windstärke.png')




def Windrichtung_ploter():

    daten_x = x_Windrichtung_Wert
    daten_y = y_Windrichtung_Time
    # plottet den Graphen (x , y , color , marker, linestyle, linewidth )
    plt.plot(daten_x, daten_y , color = 'red', marker = 'x', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Windrichtung in °')

    # titel über dem graphen
    plt.title('Windrichtung')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('Windrichtung.png')





def Temperatur_ploter():

    daten_x = x_Temperatur_Wert.view()
    daten_y = y_BME_Time.view()
    # plottet den Graphen (x , y , color , marker, linestyle, linewidth )
    plt.plot(daten_x, daten_y , color = 'red', marker = 'x', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Temperatur in °C')

    # titel über dem graphen
    plt.title('Temperatur')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('Temperatur.png')














f = 0

# Endlosschleife (void loop)
while True: 
    niederschlag_rotine(anzahl_an_öffnungen, niederschlagswert , niederschlagsmenge)
    Niederschlag_ploter()

    bme_rotine()
    Luftdruck_ploter( )
    Temperatur_ploter()
    Luftfeuchtigkeit_ploter()

    windgeschwindikeit_rotine(anzahl_an_umdrehungen)
    Windstärke_ploter()

    x = x_Windrichtung_Wert.view()
    x[f] = windrichtung_rotine()
    f += 1
    
    Windrichtung_ploter()

    time.sleep(10000) #  warte in ms