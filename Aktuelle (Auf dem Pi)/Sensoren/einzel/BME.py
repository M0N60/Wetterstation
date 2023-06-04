# geklauen XD 
# war mit dem normal en os siehe link
#https://core-electronics.com.au/guides/piicodev-atmospheric-sensor-bme280-raspberry-pi-guide/ 

import bme280
import smbus2
from time import sleep

port = 1
address = 0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    print("Luftfeutigkeit:", humidity,"%")
    print("Luftdruck:", pressure,"hPa")
    print("Luftdruck:", (float(pressure)*0.014503773773), "Psi")
    print("Temperatur:", ambient_temperature,"Grad")
    print("----------------------------------------------")

    with open ('/home/praxis/Desktop/txt/Luftfeuchtigkeit.txt' , 'w') as humidity_txt:
        humidity_txt.write (str(humidity))

    with open ('/home/praxis/Desktop/txt/Luftdruck.txt' , 'w') as pressure_txt:
        pressure_txt.write (str(pressure))
    
    with open ('/home/praxis/Desktop/txt/Temperatur.txt' , 'w') as ambient_temperature_txt:
        ambient_temperature_txt.write (str(ambient_temperature))

    sleep(1)