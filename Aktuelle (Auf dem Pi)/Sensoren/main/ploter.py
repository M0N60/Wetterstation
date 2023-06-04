from bibliotheken import *

from main import *   



x_Luftfeuchtigkeit_Wert = np.array([0, 0, 0, 0, 0])
x_Luftdruck_Wert = np.array([0, 0, 0, 0, 0])
x_Temperatur_Wert = np.array([0, 0, 0, 0, 0])

y_BME_Time = np.array([0, 0, 0, 0, 0])


x_Windgeschwindigkeit_Wert = np.array([0, 0, 0, 0, 0])
y_Windgeschwindigkeit_Time = np.array([0, 0, 0, 0, 0])


x_Niederschlag_Wert = np.array([0, 0, 0, 0, 0])
y_Niederschlag_Time = np.array([0, 0, 0, 0, 0])

x_Windrichtung_Wert = np.array([0, 0, 0, 0, 0])
y_Windrichtung_Time = np.array([0, 0, 0, 0, 0])

# zäler der anzahlen wie heufig es übergeben wurde
i = 0


def wert_ploter():# started werte annamnen und alle plotter nach 5 mal ausführen  #? ka ob der das schaft XD
    global i
    give_wert_Luftdruck_ploter(i)
    give_wert_Niederschlag_ploter(i)
    give_wert_Luftfeuchtigkeit_ploter(i)
    give_wert_Windgeschwindigkeit_ploter(i)
    give_wert_Windrichtung_ploter(i)
    give_wert_Temperatur_ploter(i)
    i += i 
    if i == 4:
        i = 0
        all_ploter() # dann wären einmal alle werte erneuert




def all_ploter(): # started alle plotter #? ka ob der das schaft XD
    Luftdruck_ploter()
    Niederschlag_ploter()
    Luftfeuchtigkeit_ploter()
    Windgeschwindigkeit_ploter()
    Windrichtung_ploter()
    Temperatur_ploter()




def give_wert_Luftdruck_ploter(i):
    with open ('/home/praxis/Desktop/txt/Luftdruck.txt' , 'r') as pressure_txt:
        pressure_wert =  pressure_txt.read()

    with open ('/home/praxis/Desktop/txt/Zeit/BME_TIME.txt' , 'r') as BME_TIME_txt:
        BME_TIME =  BME_TIME_txt.read()

    y_BME_Time[i] = BME_TIME 
    x_Luftdruck_Wert[i] = pressure_wert 

def give_wert_Temperatur_ploter(i):
    with open ('/home/praxis/Desktop/txt/Temperatur.txt' , 'r') as ambient_temperature_txt:
       Temperatur_wert= ambient_temperature_txt.read()  
    #y selbe wie BME_TIME
    x_Temperatur_Wert[i] = Temperatur_wert

    
def give_wert_Luftfeuchtigkeit_ploter(i):
    with open ('/home/praxis/Desktop/txt/Luftfeuchtigkeit.txt' , 'r') as humidity_txt:
        humidity_wert= humidity_txt.read()
    #y selbe wie BME_TIME
    x_Luftfeuchtigkeit_Wert[i] = humidity_wert

def give_wert_Windgeschwindigkeit_ploter(i):
    with open ('/home/praxis/Desktop/txt/Windgeschwindigkeit.txt' , 'r') as Windgeschwindigkeit_txt:
        windgeschwindigkeit_wert = Windgeschwindigkeit_txt.read()
    with open ('/home/praxis/Desktop/txt/Zeit/WINDGESCHINDIKEIT_TIME.txt' , 'r') as WINDGESCHINDIKEIT_TIME_txt:
        WINDGESCHINDIKEIT_TIME= WINDGESCHINDIKEIT_TIME_txt.read()
    
    x_Windgeschwindigkeit_Wert[i] = windgeschwindigkeit_wert
    y_Windgeschwindigkeit_Time[i] =WINDGESCHINDIKEIT_TIME
    
def give_wert_Windrichtung_ploter(i):
    with open ('/home/praxis/Desktop/txt/Windrichtung.txt' , 'r') as Windrichtung_txt:
       Windrichtung_wert= Windrichtung_txt.read()
    with open ('/home/praxis/Desktop/txt/Zeit/WINDREICHUNG_TIME.txt' , 'r') as WINDREICHUNG_TIME_txt:
        WINDREICHUNG_TIME =  WINDREICHUNG_TIME_txt.read()
    x_Windrichtung_Wert[i] = Windrichtung_wert
    y_Windrichtung_Time[i] = WINDREICHUNG_TIME

def give_wert_Niederschlag_ploter(i):
    
    with open ('/home/praxis/Desktop/txt/Niederschlag.txt' , 'r') as Niederschlag_txt:
        niederschlag_wert = Niederschlag_txt.read()
    with open ('/home/praxis/Desktop/txt/Zeit/NIEDERSCHLAG_TIME.txt' , 'r') as NIEDERSCHLAG_TIME_txt:
        NIEDERSCHLAG_TIME =  NIEDERSCHLAG_TIME_txt.read()

    x_Niederschlag_Wert[i] = niederschlag_wert
    y_Niederschlag_Time[i] = NIEDERSCHLAG_TIME



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
    plt.savefig('/var/www/html/Luftdruck.png')


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