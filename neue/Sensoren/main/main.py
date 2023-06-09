from bibliotheken  import *

from sensor_bme import *
from sensor_niederschlag_und_windgeschwindikeit import *
from ploter import *

# ! Windrichtung 

# wenn das Programm nicht Sterben soll lass es ein Kommentar 
#GPIO.setwarnings(False) 


# abstand zwischen dem Messen der sensoren 
anbstants_zeit = 0

while True:

    #werte auslesen
    bme_rotine()
    time.sleep(anbstants_zeit)
    niederschlag_rotine(25000 ,60) # schalt_wert ,mess_zeit
    time.sleep(anbstants_zeit)
    windgeschwindikeit_rotine(10,30)# schalt_wert ,mess_zeit
    time.sleep(anbstants_zeit)
    # windrichtung_rotine() 
    
    #!!Termainal anzeige!!

    #werte fürs Terminal bekommne
    with open ('/home/praxis/Desktop/txt/Luftfeuchtigkeit.txt' , 'r') as humidity_txt:
        humidity_wert= humidity_txt.read()

    with open ('/home/praxis/Desktop/txt/Luftdruck.txt' , 'r') as pressure_txt:
        pressure_wert =  pressure_txt.read()
    
    with open ('/home/praxis/Desktop/txt/Temperatur.txt' , 'r') as ambient_temperature_txt:
       Temperatur_wert= ambient_temperature_txt.read()
    
    with open ('/home/praxis/Desktop/txt/Windrichtung.txt' , 'r') as Windrichtung_txt:
       Windrichtung_wert= Windrichtung_txt.read()

    with open ('/home/praxis/Desktop/txt/Windgeschwindigkeit.txt' , 'r') as Windgeschwindigkeit_txt:
        windspeed_wert = Windgeschwindigkeit_txt.read()

    with open ('/home/praxis/Desktop/txt/Niederschlag.txt' , 'r') as Niederschlag_txt:
        niederschlag_wert = Niederschlag_txt.read()
    

    #Terminal ausgaben
    print("----------------------------------------------")
    print("Die Aktuellen Werte sind:")
    print("Luftfeutigkeit:", humidity_wert,"%")
    print("Luftdruck:", pressure_wert,"hPa")
    print("Luftdruck:", (float(pressure_wert)*0.014503773773), "Psi")
    print("Temperatur:", Temperatur_wert,"Grad")
    print("Windgeschindikeit: ",windspeed_wert,"m/s")
    print("Windgeschindikeit: ",(float(windspeed_wert)*3.6),"km/h")
    print("Niederschalag: ",niederschlag_wert ,"l/m2/h")
    print("Windrichtung: ",Windrichtung_wert)

    time.sleep(anbstants_zeit)
    
    wert_ploter()