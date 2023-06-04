import RPi.GPIO as GPIO #sudo apt-get install python-rpi.gpio
import time

rainsenpin = 0
# setup
anzahl_an_öffnungen  = 0 # um den niederschalag zu messen
niederschlagsmenge = 50 # zum Beispiel 50ml

# werte wenn er das Relais auslöst
schalt_wert_feutigkeit = 0
# niederschlag
niederschlagswert = anzahl_an_öffnungen * niederschlagsmenge  # Herausfinden, wie viel ml in dem Beh�lter sind und auf Quadratmeter umrechnen! ml pro qm in 24h


def niederschlag_rotine(anzahl_an_öffnungen):
    if GPIO.input(rainsenpin) >= schalt_wert_feutigkeit: # das ist noch f�r digitale Werte (muss noch durch den befehl vom ADC gewechselt werden)
        GPIO.output(relaispin, GPIO.LOW) 
        anzahl_an_öffnungen += 1 
    else:
        GPIO.output(relaispin, GPIO.HIGH) 
    return (niederschlagswert)


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
    return(humidity, pressure, ambient_temperature) # nicht notwendig ? 

# windgeschwindikeit 
def windgeschwindikeit_rotine(anzahl_an_umdrehungen):
    if GPIO.input(fotopin) >= schalt_wert_lichtschranke: # das ist noch für digitale Werte (muss noch durch den befehl vom ADC gewechselt werden)
        anzahl_an_umdrehungen += 1 
    else:
        pass
    GPIO.output(ledpin, GPIO.HIGH)
    print(anzahl_an_umdrehungen)
    return (anzahl_an_umdrehungen)



#loop
while True:
    niederschlag_rotine(anzahl_an_öffnungen)
    print("Der Niederschlag beträgt: ", niederschlagswert, "ml pro qm")
    bme_rotine()
    print("Die Luftfeuchtigkeit beträgt: ", humidity, "%")
    print("Der Luftdruck liegt bei: ", pressure, "hPa")
    print( "Die Außentemperatur beträgt: ", ambient_temperature, "°C")
    windgeschwindikeit_rotine(anzahl_an_umdrehungen)
    print("Die Windgeschwindigkeit beträgt: ", anzahl_an_umdrehungen, "km/h")