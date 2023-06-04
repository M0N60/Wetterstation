"""
# Rotary Encoder

# Rotory_Encoder.py
# von https://www.elektronik-kompendium.de/sites/raspberry-pi/2703131.htm 

# Bibliotheken laden
from rotary import Rotary

# GPIOs zum Rotary Encoder
pin_dt = 18
pin_clk = 19
pin_sw = 17

# Initialiserung Rotary Encoder
rotary = Rotary(pin_dt, pin_clk, pin_sw)
value = 0

# Funktion
def rotary_changed(change):
    global value
    if change == Rotary.ROT_CW:
        value = value + 1
        print('Rechts (', value, ')')
    elif change == Rotary.ROT_CCW:
        value = value - 1
        print('Links (', value, ')')
    elif change == Rotary.SW_PRESS:
        print('Gedr�ckt')
    elif change == Rotary.SW_RELEASE:
        print('Losgelassen')

# Wenn der Encoder bedient wird
rotary.add_handler(rotary_changed)



# test_von_Jenne
# windrichtung (rotory encoder) !�NDERN! siehe Rotory_Encoder.py (beispiel in test2_von_Jenne_(! ka !))
def windrichtung_rotine(neuePosition , altePosition):
    neuePosition = meinEncoder.read();  # Die "neue" Position des Encoders wird definiert. Dabei wird die aktuelle Position des Encoders �ber die Variable.Befehl() ausgelesen. 
    if (neuePosition != altePosition):  # Sollte die neue Position ungleich der alten (-999) sein (und nur dann!!)...
        altePosition = neuePosition;       
        print(neuePosition);      # ...soll die aktuelle Position im seriellen Monitor ausgegeben werden.
    else:
        pass #pass ist nur um weiter zugebne 
    return(neuePosition) 


# test2_von_Jenne
# windrichtung (rotory encoder) (verstehe ich nicht)
def windrichtung_rotine(change):
    global value
    if change == Rotary.ROT_CW:
        value = value + 1
        print('Rechts (', value, ')')
    elif change == Rotary.ROT_CCW:
        value = value - 1
        print('Links (', value, ')')
    else:
        pass
    print(value)
    return(value)

# Wenn der Encoder bedient wird
rotary.add_handler(rotary_changed)
"""




# mein Test

# windrichtung (rotory encoder) (verstehe ich nicht)
# 19-1 Nord, 2,3 NO, 4-6 Ost, 7,8 SO, 9-11 Süd, 12,13 SW, 14-16 West, 17,18 NW
windrichtung = "Norden"                 
def windrichtung_rotine(change):        
    global value                        
    if change == Rotary.ROT_CW:                 
        value = value + 1
        windrichtung = "Sueden"         # falsch
        print('Rechts (', value, ')')
    elif change == Rotary.ROT_CCW:
        value = value - 1
        windrichtung = "Norden"         # falsch
        print('Links (', value, ')')
    elif value == 20:                   # 20 Rotationen auf 360° deswegen nulll setzen 
        value = 0
    elif value == -20:                  # 20 Rotationen auf 360° deswegen nulll setzen (auch wenn es einmal in die anderer Richtung geht )
        value = 0 
    else:
        pass
    print(value)
    return(value)

# Wenn der Encoder bedient wird
rotary.add_handler(rotary_changed)


# while-Schleife
windrichtung_rotine(change)
print("Der Wind weht nach", windrichtung)




"""
note: 
wert über 360 grad musss wieder auf null gehen 
wert enderund sollte nur den wert erhöhne 
richtung basirent auf der wert zahl
"""


# mein (Jenne) Test
# Angenommen, Position 0/20 ist Norden, 10 = Süden, 5 = Osten, 15 Westen 
# 19-1 Nord, 2,3 NO, 4-6 Ost, 7,8 SO, 9-11 Süd, 12,13 SW, 14-16 West, 17,18 WN 


def windrichtung_rotine(change):        
    # das gibt die encoder werte (0-20 ) wieder
    global value                       
    if change == Rotary.ROT_CW:
        value = value + 1
        
    elif change == Rotary.ROT_CCW:
        value = value - 1
    else:
        pass

    # ab heir gebne wier den werten (0-20) einen Namen
    if value == 0  :  
        return("Norden")
    elif value == 19:
        return("Norden")
    elif value == -19:                  
        return("Norden")
    elif value == 1:
        return("Norden")
    elif value <= -17:
        return("WN")
    elif value <= -14:
        return("West")
    elif value <= -12:
        return("WN")
    elif value <= -9:
        return("WN")
    elif value <= -7:
        return("WN")
    elif value <= -4:
        return("WN")
    elif value <= -2:
        return("WN")
    elif value <3:
        return("ka")
    elif value <6:
        return("WN")
    elif value <= 8:
        return("WN")
    elif value <= 11:
        return("WN")
    elif value <= 13:
        return("WN")
    elif value <= 16:
        return("WN")
    elif value <= 18:
        return("WN")

    # 19-1 Nord, 2,3 NO, 4-6 Ost, 7,8 SO, 9-11 Süd, 12,13 SW, 14-16 West, 17,18 WN 


    # if value == 1 :
        # return ("Norden") 

    # ab hier  seten wir die umdrehung zurück

    if value == 20:                   # 20 Rotationen auf 360° deswegen nulll setzen 
        value = 0

    elif value == -20:                  # 20 Rotationen auf 360° deswegen nulll setzen (auch wenn es einmal in die anderer Richtung geht )
        value = 0 
    else:
        pass


# Wenn der Encoder bedient wird
rotary.add_handler(rotary_changed)


# while-Schleife
while True :
    windrichtung_rotine(change)
    print("Der Wind weht nach", windrichtung_rotine(change))