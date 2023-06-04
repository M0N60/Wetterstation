from bibliotheken  import *

from sensor_bme import *
from sensor_niederschlag_und_windgeschwindikeit import *
from sensor_windrichtung import *
from ploter import *

# könnte man auch in eine eigene Datei packen, aber das ist nicht nötig / wie XD
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


while True:
    bme_rotine()
    niederschlag_rotine()
    windgeschwindikeit_rotine()
    
    windrichtung_rotine()
    # oder rotary.add_handler(windrichtung_rotine) #! wo für / muss das in den LOOP ?

    aktuelle_zeit = time.time()
    ausfürungs_delay = 1 # abstants zeit (delay Zeit zwischen den Plottungen) 
    if aktuelle_zeit == ausfürungs_delay :
        all_ploter()
        ausfürungs_delay = ausfürungs_delay + aktuelle_zeit
