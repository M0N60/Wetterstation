# import the time module
import time


seconds = time.time()

print("Seconds since epoch =", seconds)	


local_time = time.ctime(seconds)

print("Local time:", local_time)



result = time.localtime(seconds)
print("\nresult:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)