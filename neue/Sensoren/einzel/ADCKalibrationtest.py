from bibliotheken import *

# Den I2C-Bus erstellen
i2c = busio.I2C(board.SCL, board.SDA) # I²C adress  0x48

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

# zähler für bestimte funktionen 
anzahl_an_öffnungen  = 0 # um den niederschalag zu messen
anzahl_an_umdrehungen = 0 # um die anzahl an umdrehungen zu messen

# entpreller
trigger = 0
trigger1 = 0


# wert bestimmung wo es auslösen soll 
schalt_wert_feutigkeit = 25000
schalt_wert_lichtschranke = 10



# BCM-Nummerierung verwenden
GPIO.setmode(GPIO.BCM)

# einzelen Ein und Ausgänge deklariren 
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(relaispin, GPIO.OUT)


# zaler für die arrays in den einzelene funktionen 
zahler_niederschlag = 0
zahler_windgeschwindikeit = 0


GPIO.output(ledpin, GPIO.HIGH)



def niederschlag_rotine():

    global zahler_niederschlag
    global anzahl_an_öffnungen
    global trigger

    if chan0.value <= schalt_wert_feutigkeit and trigger== 0: 
        GPIO.output(relaispin, GPIO.LOW) 
        anzahl_an_öffnungen = anzahl_an_öffnungen + 1 
        # entprellen !
        trigger= trigger+1
    if chan0.value >= 0:
        trigger = 0
        GPIO.output(relaispin, GPIO.HIGH) 
    


# windgeschwindikeit (mit ADC)
def windgeschwindikeit_rotine():

    global zahler_windgeschwindikeit
    global anzahl_an_umdrehungen
    global trigger1

    if chan1.value <= schalt_wert_lichtschranke and trigger1== 0: 
        anzahl_an_umdrehungen += 1 
        trigger1 = 1
    if chan1.value >= schalt_wert_lichtschranke:
        trigger1 = 0
    
    

while(1):
    niederschlag_rotine()
    windgeschwindikeit_rotine()
    print(anzahl_an_öffnungen ,anzahl_an_umdrehungen ,"///" ,chan0.value , chan1.value)