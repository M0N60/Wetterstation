#HAllo Miriam



# setup
anzahl_an_�ffnungen  = 0 # um den niederschalag zu messen
niederschlagsmenge = 50 # zum Beispiel 50ml

# niederschlag
niederschlagswert = anzahl_an_�ffnungen * niederschlagsmenge  # Herausfinden, wie viel ml in dem Beh�lter sind und auf Quadratmeter umrechnen! ml pro qm in 24h


def niederschlag_rotine(anzahl_an_�ffnungen):
    if GPIO.input(rainsenpin) >= schalt_wert_feutigkeit: # das ist noch f�r digitale Werte (muss noch durch den befehl vom ADC gewechselt werden)
        GPIO.output(relaispin, GPIO.LOW) 
        anzahl_an_�ffnungen += 1 
    else:
        GPIO.output(relaispin, GPIO.HIGH) 
    print(niederschlagswert) # "anzahl_an_�ffnungen" durch "niederschlagswert" ersetzt
    return (niederschlagswert)






#loop
while True:
    niederschlag_rotine()
    function()