()
# Hier ändere ich sache wo ich nicht weiß was sie machen XD

# bme bibioteken 
# link von : https://core-electronics.com.au/guides/piicodev-atmospheric-sensor-bme280-raspberry-pi-guide/ 

import bme280
import smbus2

# generell fur Input und Outupt (PIN BELEGUNG) ++ delay funkion 
# link von : https://www.elektronik-kompendium.de/sites/raspberry-pi/2611151.htm 
import RPi.GPIO as GPIO #sudo apt-get install python-rpi.gpio
import time


# Bibliothek für den Rotary Encoder
# link von : https://www.elektronik-kompendium.de/sites/raspberry-pi/2703131.htm
from rotary import Rotary


# für den AD siehe analoge_signal.py (verstehe ich nicht)

import time # haben wir schon oben 
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
# Den I2C-Bus erstellen
i2c = busio.I2C(board.SCL, board.SDA)
# Erstellen des ADC-Objekts über den I2C-Bus
ads = ADS.ADS1115(i2c)
# Single-Ended-Eingang auf Kanälen erstellen
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)




# pin definition sind ohne const int  && funktionen sind mit : anstat {}

# Pin ort mit den richtigen GPIO zahlen
fotopin = 0 
ledpin = 0  
rainsenpin = 0 # nur wenn wir den digital machen 
relaispin = 0


pin_clk = 0 #
pin_dt = 0  #
pin_sw = 0  # das ist so wie ich es verstehe nur für den taster im encoder XD


#Rotory zustrand werte
neuePosition = 0     # wäre ein long: gibt es nicht also hab ich den als int erstmal gelasen
altePosition = -999  # wäre ein long: gibt es nicht also hab ich den als int erstmal gelasen



# zähler für bestimte funktionen 
anzahl_an_öffnungen  = 0 # um den niederschalag zu messen
anzahl_an_umdrehungen = 0 # um die anzahl an umdrehungen zu messen




# wert bestimmung wo es auslösen soll 
schalt_wert_feutigkeit = 500
schalt_wert_lichtschranke = 500


# ab hier ist das void setup()

# BCM-Nummerierung verwenden
GPIO.setmode(GPIO.BCM)

# einzelen Ein und Ausgänge deklariren 
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(relaispin, GPIO.OUT)


# Rotory_Encoder Setup
rotary = Rotary(pin_dt, pin_clk, pin_sw)
value = 0

# ab hier kommen eigen funktionen wie {def .. (anstat void ...)} und {der loop (mit while(True) ...)}


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
    print(humidity, pressure, ambient_temperature)
    return(humidity, pressure, ambient_temperature)



# niederschlag
def niederschlag_rotine(anzahl_an_öffnungen):
    if GPIO.input(rainsenpin) >= schalt_wert_feutigkeit: # das ist noch für digitale Werte (muss noch durch den befehl vom ADC gewechselt werden)
        # ventil offen
        GPIO.output(relaispin, GPIO.LOW)
        anzahl_an_öffnungen += 1 # hoch zählen
    else:
        # ventil schliesen
        GPIO.output(relaispin, GPIO.HIGH)  
    print(anzahl_an_öffnungen)
    return (anzahl_an_öffnungen)


# windgeschwindikeit 
def windgeschwindikeit_rotine(anzahl_an_umdrehungen):
    if GPIO.input(fotopin) >= schalt_wert_lichtschranke: # das ist noch für digitale Werte (muss noch durch den befehl vom ADC gewechselt werden)
        anzahl_an_umdrehungen += 1 # hoch zählen
    else:
        pass
    GPIO.output(ledpin, GPIO.HIGH)
    print(anzahl_an_umdrehungen)
    return (anzahl_an_umdrehungen)



# windrichtung (rotory encoder) (verstehe ich nicht)
def windrichtung_rotine(change):
    global value
    if change == Rotary.ROT_CW:
        value = value + 1
        print('Rechts (', value, ')')
    elif change == Rotary.ROT_CCW:
        value = value - 1
        print('Links (', value, ')')
    else:
        pass
    print(value)
    return(value)

# Wenn der Encoder bedient wird
rotary.add_handler(rotary_changed)



# Endlosschleife
while True: 
    # noch mit einer if abfrage betimmen wann / wer  ausgeführt werden soll
    bme_rotine()
    niederschlag_rotine(anzahl_an_öffnungen) 
    windgeschwindikeit_rotine(anzahl_an_umdrehungen)
    windrichtung_rotine(neuePosition, altePosition)
    time.sleep(1) # nur um nach dem durch lauf 1s zu warten  (würde ich aber verhindern wollen)


# eigentlich müssten die parallel zu einander laufen und in bestimmten zeit abstanden abgefagt werden aber eagl XD
# können ja erstam gucken wie das überhaubt geht XD

















"""
das folgende ist nur ein Beispiel für mich 

# for schleife
for i in range(5): # für das 5 mal 
    GPIO.output(ledpin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(ledpin, GPIO.LOW)
    time.sleep(0.5)
    
#in if else ohne wert in else
if GPIO.input(fotopin) == 0: 
        GPIO.output(ledpin, GPIO.LOW)
    else:
        pass
    retun(wert)



# delay --> time.sleep(1)


# funkion von https://forum.arduino.cc/t/python3-is-there-a-funcion-like-millis-of-arduino/660016
# welche die aktuelle lauf zeit in ms wiedergeben sollte 
def millis():
  return round(time.time() * 1000)





"""
