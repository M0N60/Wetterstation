from bibliotheken import *




port = 1
address = 0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

def bme_rotine():
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature

    with open ('/home/praxis/Desktop/txt/Luftfeuchtigkeit.txt' , 'w') as humidity_txt:
        humidity_txt.write (str(humidity))

    with open ('/home/praxis/Desktop/txt/Luftdruck.txt' , 'w') as pressure_txt:
        pressure_txt.write (str(pressure))
    
    with open ('/home/praxis/Desktop/txt/Temperatur.txt' , 'w') as ambient_temperature_txt:
        ambient_temperature_txt.write (str(ambient_temperature))
    
    with open ('/home/praxis/Desktop/txt/Zeit/BME_TIME.txt' , 'w') as BME_TIME_txt:
        BME_TIME_txt.write (str(time.time())) # zeit bekommen

    return
