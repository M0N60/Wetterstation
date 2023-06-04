from bibliotheken import*
from bme import*
from niederschlag import*
from windgeschwindigkeit import*
from windrichtung import*
from plotter import*


# Dinge die so gehen sollten 


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