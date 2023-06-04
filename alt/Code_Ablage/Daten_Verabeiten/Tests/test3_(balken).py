import matplotlib.pyplot as plt
import numpy as np

# um style zu verwenden (die es schöner machen) 
#   plt.style.use('ggplot')


# daten ( in einem arry )
daten_x  = [1,2,3,4,5]
daten_y = [1,2,3,4,5]
#--> Daten_arrys aus 'Python'/'SQL' iportieren 




# plottet den Graphen (x , y , color , marker, linestyle, linewidth )
plt.bar(daten_x, daten_y , color = 'b', marker = '_', linestyle = '-', linewidth = 2 ) 
#--> img/? in der webseite ('PHP','HTML5', 'CSS3' ,'JavaScript') einfögen]  
#--> img/? in der webseite ('PHP','HTML5', 'CSS3' ,'JavaScript') einfügen]



# name an der x achse
plt.xlabel('Zeit in min')

# name an der y achse
plt.ylabel('Niederschlag ml pro qm')


# titel über dem graphen
plt.title('Niederschlag')

# um leichter die x/y werte abzulesen zu können
plt.grid(True)

# speicher als png (name)
plt.savefig('Niederschlag.png')

# anzeige befehl
#plt.show()
