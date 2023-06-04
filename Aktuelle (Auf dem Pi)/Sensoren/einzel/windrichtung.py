# Idee von  https://www.linkerkit.de/index.php?title=KY-040_Kodierter_Drehschalter_(Rotary_Encoder)


import RPi.GPIO as GPIO
import time

# was macht das? 
GPIO.setmode(GPIO.BCM)
 
# Hier werden die Eingangs-Pins deklariert, an dem der Sensor angeschlossen ist.
PIN_CLK = 27
PIN_DT = 23
BUTTON_PIN = 22
 
GPIO.setup(PIN_CLK, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_DT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
# Benötigte Variablen werden initialisiert
Counter = 0
Richtung = True
PIN_CLK_LETZTER = 0
PIN_CLK_AKTUELL = 0
delayTime = 0.1



# Initiales Auslesen des Pin_CLK
PIN_CLK_LETZTER = GPIO.input(PIN_CLK)
 
# Diese AusgabeFunktion wird bei Signaldetektion ausgefuehrt
def ausgabeFunktion(Null):
    global Counter
 
    PIN_CLK_AKTUELL = GPIO.input(PIN_CLK)
 
    if PIN_CLK_AKTUELL != PIN_CLK_LETZTER:
 
        if GPIO.input(PIN_DT) != PIN_CLK_AKTUELL:
            Counter += 1
        else:
            Counter =Counter -1

        #zuweisung von der Richtung basireden auf den wert des counters
        if Counter == 0  :  
            windrichtungs_wert = "Norden"
        elif Counter == 19:
            windrichtungs_wert = "Norden"
        elif Counter == -19:                  
            windrichtungs_wert = "Norden"
        elif Counter == 1:
            windrichtungs_wert = "Norden"
        elif Counter <= -17:           # gleiche Position wie 3
            windrichtungs_wert = "Nordosten"
        elif Counter <= -14:           # 6
            windrichtungs_wert = "Osten"
        elif Counter <= -12:
            windrichtungs_wert = "Südosten"
        elif Counter <= -9:
            windrichtungs_wert = "Süden"
        elif Counter <= -7:
            windrichtungs_wert = "Südwesten"
        elif Counter <= -4:
            windrichtungs_wert = "Westen"
        elif Counter <= -2:
            windrichtungs_wert = "Nordwesten"
        elif Counter <=3:
            windrichtungs_wert = "Nordosten"
        elif Counter <=6:
            windrichtungs_wert = "Osten"
        elif Counter <= 8:
            windrichtungs_wert = "Südosten"
        elif Counter <= 11:
            windrichtungs_wert = "Süden"
        elif Counter <= 13:
            windrichtungs_wert = "Südwesten"
        elif Counter <= 16:
            windrichtungs_wert = "Westen"
        elif Counter <= 18:
            windrichtungs_wert= "Nordwesten"
        # resets bei voller umdrehung 
        if Counter == 20:
            Counter = 0
        if Counter == -20: 
            Counter = 0 
 
        with open ('/home/praxis/Desktop/txt/Windrichtung.txt' , 'w') as Windrichtung_txt:
            Windrichtung_txt.write (str(windrichtungs_wert))

    print(Counter ,  windrichtungs_wert)
    

def CounterReset(Null):
    global Counter
 
    print ("Position auf Norden resettet / eingestllet!")
    print ("----------------------------------------------")
    Counter = 0

# Um einen Debounce direkt zu integrieren, werden die Funktionen zur Ausgabe mittels
# CallBack-Option vom GPIO Python Modul initialisiert
GPIO.add_event_detect(PIN_CLK, GPIO.BOTH, callback=ausgabeFunktion, bouncetime=50)
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=CounterReset, bouncetime=50)
 
# Hauptprogrammschleife
try:
        while True:
            time.sleep(delayTime)
 
# Aufraeumarbeiten nachdem das Programm beendet wurde
except KeyboardInterrupt:
        GPIO.cleanup()

