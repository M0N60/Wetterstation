from bme_rotine import *
from ploter import *
from Windrichtungs_auslesung import *



while True:
    # !help! #
    # !sensors! #
    # !plot! #
    # wir mussen aus der sensoren den wert mit der akutellen zeit bekommen 
    # diesen danach plotten XD 

    # !BME! #

    bme_rotine()

    i = get_bme_anzahl_der_aktivirungen()

    humidity[i] = get_bme_humidity()
    pressure[i] = get_bme_pressure()
    temperature[i] = get_bme_temperature ()
    verbrauche_zeit[i] = get_bme_verbrauche_zeit()

    Luftdruck_ploter(pressure[] ,verbrauche_zeit[])
    Luftfeuchtigkeit_ploter(humidity[] ,verbrauche_zeit[])
    Temperatur_ploter(temperature[] ,verbrauche_zeit[])

    # !windrichtung! #


    if (rotary.add_handler(windrichtung_rotine) != 0 ): # also wenn  der Interrupt an ist dann soll er ausgelesen werdem 
        richtung = windrichtung_rotine()
        zeit = get_windrichtung_zeit() # muss noch in Windrichtung hinzugefügt werden
    else:
        quit
    
    Windrichtung_ploter(richtung ,zeit)
