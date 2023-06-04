from bibliotheken import *

from main import *   

# eigentlich in bibliotheken aber egal XD

import matplotlib.pyplot as plt
import numpy as np

def all_ploter(): # started alle plotter #? ka ob der das schaft XD
    Luftdruck_ploter()
    Niederschlag_ploter()
    Luftfeuchtigkeit_ploter()
    Windstärke_ploter()
    Windrichtung_ploter()
    Temperatur_ploter()


def Luftdruck_ploter():

    daten_x = x_Luftdruck_Wert.view() # x_Luftdruck_Wert ist die Variable aus main.py
    daten_y = y_BME_Time.view()       # y_BME_Time ist die Variable aus main.py

    # plottet den Graphen (x , y , color , marker, linestyle, linewidth )
    plt.plot(daten_x, daten_y , color = 'red', marker = 'x', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Luftdruck in hPa')

    # titel über dem graphen
    plt.title('Luftdruck')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('Luftdruck.png')


def Niederschlag_ploter():
    
    daten_x = x_Niederschlag_Wert.view()
    daten_y = y_Niederschlag_Time.view()


    # plottet den Balken (x , y , color , marker, linestyle, linewidth )
    plt.bar(daten_x, daten_y , color = 'b', marker = '_', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Niederschlag in ml pro qm')

    # titel über dem graphen
    plt.title('Niederschlag')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('Niederschlag.png')

def Luftfeuchtigkeit_ploter():

    daten_x = x_Luftfeuchtigkeit_Wert.view()
    daten_y = y_BME_Time.view()

    # plottet den Graphen (x , y , color , marker, linestyle, linewidth )
    plt.plot(daten_x, daten_y , color = 'red', marker = 'x', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Luftfeuchtigkeit in %')

    # titel über dem graphen
    plt.title('Luftfeuchtigkeit')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('Luftfeuchtigkeit.png')




def Windstärke_ploter():
    
    daten_x  = x_Windstärke_Wert.view()
    daten_y =  y_Windstärke_Time.view()

    # plottet den Graphen (x , y , color , marker, linestyle, linewidth )
    plt.plot(daten_x, daten_y , color = 'red', marker = 'x', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Windstärke in km/h')

    # titel über dem graphen
    plt.title('Windstärke')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('Windstärke.png')




def Windrichtung_ploter():

    daten_x = x_Windrichtung_Wert.view()
    daten_y = y_Windrichtung_Time.view()
    # plottet den Graphen (x , y , color , marker, linestyle, linewidth )
    plt.plot(daten_x, daten_y , color = 'red', marker = 'x', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Windrichtung in °')

    # titel über dem graphen
    plt.title('Windrichtung')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('Windrichtung.png')





def Temperatur_ploter():

    daten_x = x_Temperatur_Wert.view()
    daten_y = y_BME_Time.view()
    # plottet den Graphen (x , y , color , marker, linestyle, linewidth )
    plt.plot(daten_x, daten_y , color = 'red', marker = 'x', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Temperatur in °C')

    # titel über dem graphen
    plt.title('Temperatur')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('Temperatur.png')