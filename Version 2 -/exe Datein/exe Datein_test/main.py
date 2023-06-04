from bibliotheken  import *

from sensoren import *
from ploter import *
from sensore_bme import *

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

# sensoren_initalisieren() #? wie XD 
#!  mussen wir hier alles von vor den Sensoren hin kopieren ???
#? oder ist es genug das die sachen in der anderen Datei sind ?

while True:
    bme_rotine()
    niederschlag_rotine()
    windgeschwindikeit_rotine()
    windrichtung_rotine()
    aktuelle_zeit = time.time()
    ausfürungs_delay = 1 # abstants zeit (delay Zeit zwischen den Messungen) 
    if aktuelle_zeit == ausfürungs_delay :
        all_ploter()
        ausfürungs_delay = ausfürungs_delay + aktuelle_zeit
