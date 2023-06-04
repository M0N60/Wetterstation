
# Hier Teste ich wie man den code weiter scheiben kann

# bme bibioteken 
# link von : https://core-electronics.com.au/guides/piicodev-atmospheric-sensor-bme280-raspberry-pi-guide/ 

import bme280
import smbus2

# generell fur Input und Outupt (PIN BELEGUNG) ++ delay funkion 
# link von : https://www.elektronik-kompendium.de/sites/raspberry-pi/2611151.htm 
import RPi.GPIO as GPIO
import time


# Bibliothek für den Rotary Encoder
# link von : https://funduino.de/nr-32-der-rotary-encoder-ky-040
import Encoder.h    # Verwendung der adrino Bibliothek vom Rotary Encoder (ka ob das überhaubt so geht XD)




# für den AD siehe analoge_signal.py (beispiel in test2_von_Jenne_(! ka !))





# pin definition sind ohne const int  && funktionen sind mit : anstat {}

# Pin ort mit den richtigen GPIO zahlen
fotopin = 0 # ist an A1
rainsenpin = 0 # ist an A0  wenn wir den digital machen wäre es 4
ledpin = 24  
relaispin = 17

Rotory_CLK = 23 # alle Rotory könne auch an den anderen sein aber musssen richtig verbunden werden
Rotory_DT = 22  #  "
Rotory_SW = 27  # das ist so wie ich es verstehe nur für den taster im encoder XD


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



# windrichtung (rotory encoder) !ÄNDERN! siehe Rotory_Encoder.py (beispiel in test2_von_Jenne_(! ka !))
def windrichtung_rotine(neuePosition , altePosition):
    neuePosition = meinEncoder.read();  # Die "neue" Position des Encoders wird definiert. Dabei wird die aktuelle Position des Encoders über die Variable.Befehl() ausgelesen. 
    if (neuePosition != altePosition):  # Sollte die neue Position ungleich der alten (-999) sein (und nur dann!!)...
        altePosition = neuePosition;       
        print(neuePosition);      # ...soll die aktuelle Position im seriellen Monitor ausgegeben werden.
    else:
        pass #pass ist nur um weiter zugebne 
    return(neuePosition) 



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
