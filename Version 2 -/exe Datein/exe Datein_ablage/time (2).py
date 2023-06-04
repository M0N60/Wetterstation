import time
import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([1, 1, 1, 1])
i = 0


for x in ypoints:
    named_tuple = time.localtime() 
    time_string = time.strftime(%S, named_tuple)
    ypoints[i] = time_string
    time.sleep(2222)
    i +=1


plt.plot(xpoints, ypoints)
plt.show()
