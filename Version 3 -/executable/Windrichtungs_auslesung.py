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
    elif value <= -17:           # gleiche Position wie 3
        return("Nordosten")
    elif value <= -14:           # 6
        return("Osten")
    elif value <= -12:
        return("Südosten")
    elif value <= -9:
        return("Süden")
    elif value <= -7:
        return("Südwesten")
    elif value <= -4:
        return("Westen")
    elif value <= -2:
        return("Nordwesten")
    elif value <=3:
        return("Nordosten")
    elif value <=6:
        return("Osten")
    elif value <= 8:
        return("Südosten")
    elif value <= 11:
        return("Süden")
    elif value <= 13:
        return("Südwesten")
    elif value <= 16:
        return("Westen")
    elif value <= 18:
        return("Nordwesten")
    # 19-1 Nord, 2,3 NO, 4-6 Ost, 7,8 SO, 9-11 S�d, 12,13 SW, 14-16 West, 17,18 WN 
    # ab hier setzen wir zurück
    if value == 20:                   # 20 Rotationen auf 360� deswegen nulll setzen 
        value = 0
    elif value == -20:                  # 20 Rotationen auf 360� deswegen nulll setzen (auch wenn es einmal in die anderer Richtung geht )
        value = 0 
    else:
        pass
