import matplotlib.pyplot as plt
import numpy as np


def Luftdruck_ploter(daten_x ,daten_y):

    #Daten_arrys aus 'Python' iportieren (ka)
    
    # zum test
    # daten_x  = [1,2,3,4,5]
    # daten_y = [1,2,3,4,5]

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


def Niederschlag_ploter(daten_x ,daten_y):
    
    #Daten_arrys aus 'Python' iportieren (ka)
    
    # zum test
    # daten_x  = [1,2,3,4,5]
    # daten_y = [1,2,3,4,5]


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

def Luftfeuchtigkeit_ploter(daten_x ,daten_y):

    #Daten_arrys aus 'Python' iportieren (ka)

    # zum test
    # daten_x  = [1,2,3,4,5]
    # daten_y = [1,2,3,4,5]
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




def Windstärke_ploter(daten_x ,daten_y):

    #Daten_arrys aus 'Python' iportieren (ka)

    # zum test
    # daten_x  = [1,2,3,4,5]
    # daten_y = [1,2,3,4,5]
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




def Windrichtung_ploter(daten_x ,daten_y):

    #Daten_arrys aus 'Python' iportieren (ka)

    # zum test
    # daten_x  = [1,2,3,4,5]
    # daten_y = [1,2,3,4,5]
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





def Temperatur_ploter(daten_x ,daten_y):

    #Daten_arrys aus 'Python' iportieren (ka)

    # zum test
    # daten_x  = [1,2,3,4,5]
    # daten_y = [1,2,3,4,5]
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