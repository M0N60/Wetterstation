import matplotlib.pyplot as plt
import numpy as np

# um style zu verwenden
#   plt.style.use('ggplot')


# daten arry zum ploten
daten_x  = [1,2,3,4,5]
daten_y = [1,2,3,4,5]
#--> arrys aus 'Python','SQL', iportieren 




# plottet den Graphen (x , y , color , marker, linestyle, linewidth )
plt.plot(daten_x, daten_y , color = 'red', marker = 'o', linestyle = '--', linewidth = 2 ) 
#--> img/? in der webseite ('PHP','HTML5', 'CSS3' ,'JavaScript') einfögen]  
#--> img/? in der webseite ('PHP','HTML5', 'CSS3' ,'JavaScript') einfügen]



# name an der x achse
plt.xlabel('x-Achse')

# name an der y achse
plt.ylabel('y-Achse')


# titel über dem graphen
plt.title('titel der seite hier eibeben')

# um leichter die x/y werte abzulesen zu können
plt.grid(True)




# anzeige befehl
plt.show()

# fehlt speicher/als img und wert eingeabe/als Arry 
# auserdem falsche graphen art