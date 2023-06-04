from bibliotheken import *
from main import *
import time

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

# zähler für bestimte funktionen 
anzahl_an_öffnungen  = 0 # um den niederschalag zu messen
anzahl_an_umdrehungen = 0 # um die anzahl an umdrehungen zu messen


# wert bestimmung wo es auslösen soll 
schalt_wert_feutigkeit = 500
schalt_wert_lichtschranke = 500

# Werte für Rechnungen
niederschlagswert = 0
niederschlagsmenge = 0


# BCM-Nummerierung verwenden
GPIO.setmode(GPIO.BCM)

# einzelen Ein und Ausgänge deklariren 
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(relaispin, GPIO.OUT)


# zaler für die arrays in den einzelene funktionen 
zahler_niederschlag = 0
zahler_windgeschwindikeit = 0





def niederschlag_rotine():

    global zahler_niederschlag
    global anzahl_an_öffnungen

    if chan0.value >= schalt_wert_feutigkeit: 
        GPIO.output(relaispin, GPIO.LOW) 
        anzahl_an_öffnungen += 1 
    else:
        GPIO.output(relaispin, GPIO.HIGH) 
    niederschlagswert = anzahl_an_öffnungen * niederschlagsmenge  # Herausfinden, wie viel ml in dem Beh�lter sind und auf Quadratmeter umrechnen! ml pro qm in 24h
    
    x = x_Niederschlag_Wert.view()
    x[zahler_niederschlag] = niederschlagswert

    y = y_Niederschlag_Time.view()
    y[zahler_niederschlag] = time.time()
    zahler_niederschlag += 1
    return 


# windgeschwindikeit (mit ADC)
def windgeschwindikeit_rotine():

    global zahler_windgeschwindikeit
    global anzahl_an_umdrehungen

    if chan1.value >= schalt_wert_lichtschranke: 
        anzahl_an_umdrehungen += 1 
    else:
        pass
    GPIO.output(ledpin, GPIO.HIGH)

    x = x_Windstärke_Wert.view()
    x[zahler_windgeschwindikeit] = anzahl_an_öffnungen
    
    y = y_Windstärke_Time.view()
    y[zahler_windgeschwindikeit] = time.time()
    zahler_windgeschwindikeit += 1
    return 