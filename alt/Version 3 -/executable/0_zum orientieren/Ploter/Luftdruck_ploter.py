import matplotlib.pyplot as plt
import numpy as np


#Daten_arrys aus 'Python'/'SQL' iportieren 
# !([ändern])!
daten_x  = [1,2,3,4,5]
daten_y = [1,2,3,4,5]

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
