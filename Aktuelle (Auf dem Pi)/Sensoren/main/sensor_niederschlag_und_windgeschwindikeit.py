from bibliotheken import *
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

# zähler für bestimte funktionen 
anzahl_an_öffnungen  = 0 # um den niederschalag zu messen
anzahl_an_umdrehungen = 0 # um die anzahl an umdrehungen zu messen

# entpreller
trigger = 0
trigger1 = 0

# BCM-Nummerierung verwenden
GPIO.setmode(GPIO.BCM)

# einzelen Ein und Ausgänge deklariren 
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(relaispin, GPIO.OUT)

# Werte für Rechnungen

#!NIEDERSCHALG! 
# UNTTER DER BEDINGUNG DAS ES BEI DER HÄLFTE CA SCHALTET WIRD UND  mess_zeit== 60!!

#grundwerte
grundvolumen = 13125 #in mm3 (35mm*15mm*25mm ( sensorwert_schalt_wert(max = 50 mm) hälfte = 25mm ))
grundflache  = 4125  #in mm2 (75mm*55mm)




#! CUPS! 
# Anamometer vane diameter (set to the value for your cup-to-cup in mm)
vane_diameter = float(106)

# Calculate vane circumference in metres
vane_circ = float (vane_diameter/1000)*3.1415

# Set an anamometer factor to account for inefficiency (value is a guess)
afactor = float(2.5)

# Define variable endtime to be current time in seconds plus 10 seconds
endtime = time.time() + 10
endtime1 = time.time() + 10


# led an 
GPIO.output(ledpin, GPIO.HIGH)

def niederschlag_rotine(schalt_wert_feutigkeit ,mess_zeit):

    global anzahl_an_öffnungen
    global trigger

    endtime = time.time() + mess_zeit

    print("----- Messeung des Niederschlag ------")

    while time.time() < endtime:    
        if chan0.value <= schalt_wert_feutigkeit and trigger== 0: 
            GPIO.output(relaispin, GPIO.LOW) 
            anzahl_an_öffnungen = anzahl_an_öffnungen + 1 
            # entprellen !
            trigger= trigger+1
        if chan0.value >= schalt_wert_feutigkeit:
            trigger = 0
            GPIO.output(relaispin, GPIO.HIGH)
            
        #-Debunnging-
        #print(chan0.value ,anzahl_an_öffnungen)
    
    # Calculate stuff!
    gesamt_volumen_mm = anzahl_an_öffnungen * grundvolumen 
    liter = float(gesamt_volumen_mm)*0.000001    # von mm3 zu l
    gesamtflache_m = float(grundflache)*0.000001 # von mm2 in m2 
    niederschlagswert = liter/gesamtflache_m *60 # l/mm2 pro stunde (wenn mess_zeit=60s = 1m ~ 60 min = 1h == *60)

    #-Debunnging-
    #print(anzahl_an_öffnungen ,"offungen")
    #print(niederschlagswert,"wert")   

    with open ('/home/praxis/Desktop/txt/Niederschlag.txt' , 'w') as Niederschlag_txt:
        Niederschlag_txt.write (str(niederschlagswert))

    with open ('/home/praxis/Desktop/txt/Zeit/NIEDERSCHLAG_TIME.txt' , 'w') as NIEDERSCHLAG_TIME_txt:
        NIEDERSCHLAG_TIME_txt.write (str(time.time())) # zeit bekommen


def windgeschwindikeit_rotine(schalt_wert_lichtschranke,mess_zeit):
    global anzahl_an_umdrehungen
    global trigger1

    endtime1 = time.time() + mess_zeit

    print("----- Messeung der Windgeschwindikeit ------")

    while time.time() < endtime1:
        if chan1.value <= schalt_wert_lichtschranke and trigger1== 0: 
            anzahl_an_umdrehungen += 1 
            trigger1 = 1
        if chan1.value >= schalt_wert_lichtschranke:
            trigger1 = 0

        #-Debunnging-
        #print(chan1.value, anzahl_an_umdrehungen)
    
    # Calculate stuff!
    rots_per_second = float(anzahl_an_umdrehungen/mess_zeit)
    windspeed = float((rots_per_second)*vane_circ*afactor)

    #-Debunnging-
    #print(anzahl_an_umdrehungen ,"rotation")
    #print("die windgeschindikeit ist ",windspeed,"m/s")
    #print("die windgeschindikeit ist ",(float(windspeed)*3.6),"km/h")
  

    with open ('/home/praxis/Desktop/txt/Windgeschwindigkeit.txt' , 'w') as Windgeschwindigkeit_txt:
        Windgeschwindigkeit_txt.write (str(windspeed))
    with open ('/home/praxis/Desktop/txt/Zeit/WINDGESCHINDIKEIT_TIME.txt' , 'w') as WINDGESCHINDIKEIT_TIME_txt:
        WINDGESCHINDIKEIT_TIME_txt.write (str(time.time())) # zeit bekommen
