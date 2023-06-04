# niederschlag (mit ADC)

def niederschlag_rotine(anzahl_an_öffnungen, niederschlagswert, niederschlagsmenge):
    if wert_A0 () >= schalt_wert_feutigkeit: # (mit ADC ?)
        GPIO.output(relaispin, GPIO.LOW) 
        anzahl_an_öffnungen += 1 
    else:
        GPIO.output(relaispin, GPIO.HIGH) 
    niederschlagswert = anzahl_an_öffnungen * niederschlagsmenge  # Herausfinden, wie viel ml in dem Beh�lter sind und auf Quadratmeter umrechnen! ml pro qm in 24h
    
    x = x_Niederschlag_Wert.view()
    x[o] = anzahl_an_öffnungen
    o += 1
    return 