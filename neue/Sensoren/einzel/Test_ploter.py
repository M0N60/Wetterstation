import numpy as np
import matplotlib.pyplot as plt

x_Luftfeuchtigkeit_Wert = np.array([45, 50, 65, 40, 40])
x_Luftdruck_Wert = np.array([1005, 1048, 1032, 1021, 1008])
x_Temperatur_Wert = np.array([23.5, 24.1, 24.8, 25.1, 24.6])

y_BME_Time = np.array([1, 2, 3, 4, 5])


x_Windgeschwindigkeit_Wert = np.array([15, 16, 16, 15, 161])
y_Windgeschwindigkeit_Time = np.array([1, 2, 3, 4, 5])


x_Niederschlag_Wert = np.array([0, 1, 3, 1, 0])
y_Niederschlag_Time = np.array([1, 2, 3, 4, 5])

x_Windrichtung_Wert = np.array(["Norden", "Nordost", "Norden", "Norden", "Norden"])
y_Windrichtung_Time = np.array([1, 2, 3, 4, 5])





def Luftdruck_ploter():

    daten_x = x_Luftdruck_Wert.view() 
    daten_y = y_BME_Time.view()       

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
    plt.savefig('/var/www/html/diagramm/Luftdruck.png')


def Niederschlag_ploter():
    
    daten_x = x_Niederschlag_Wert.view()
    daten_y = y_Niederschlag_Time.view()


    # plottet den Graphen (x , y , color , marker, linestyle, linewidth )
    plt.plot(daten_x, daten_y , color = 'red', marker = 'x', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Niederschlag in ml pro qm')

    # titel über dem graphen
    plt.title('Niederschlag')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('/var/www/html/diagramm/Niederschlag.png')

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
    plt.savefig('/var/www/html/diagramm/Luftfeuchtigkeit.png')




def Windgeschwindigkeit_ploter():
    
    daten_x  = x_Windgeschwindigkeit_Wert.view()
    daten_y =  y_Windgeschwindigkeit_Time.view()

    # plottet den Graphen (x , y , color , marker, linestyle, linewidth )
    plt.plot(daten_x, daten_y , color = 'red', marker = 'x', linestyle = '-', linewidth = 2 ) 

    # name an der x achse
    plt.xlabel('vergangene Zeit in min')

    # name an der y achse
    plt.ylabel('Windgeschwindigkeit in km/h')

    # titel über dem graphen
    plt.title('Windgeschwindigkeit')

    # um leichter die x/y werte abzulesen zu können
    plt.grid(True)

    # speicher als png (name)
    plt.savefig('/var/www/html/diagramm/Windgeschwindigkeit.png')




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
    plt.savefig('/var/www/html/diagramm/Windrichtung.png')





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
    plt.savefig('/var/www/html/diagramm/Temperatur.png')





#ausfüren
Luftdruck_ploter()
Niederschlag_ploter()
Luftfeuchtigkeit_ploter()
Windgeschwindigkeit_ploter()
Windrichtung_ploter()
Temperatur_ploter()