import time 
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array(["3", "8", "1", "10"])
i = 0

for x in ypoints:
  seconds = time.time()
  local_time = time.ctime(seconds)
  ypoints[i] = local_time
  time.sleep(2.4)
  i =+1

plt.plot(xpoints, ypoints)
plt.show()



