from bibliotheken import *
from main import *

# Den I2C-Bus erstellen
i2c = busio.I2C(board.SCL, board.SDA) #  oder  I²C adress (via Jumper configurable) 0x48 - 0x4B


port = 1
address = 0x77 #! Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus,address)
bme280_data = bme280.sample(bus,address)


bme_rotine()

aktivirungs_anzahl = 0


def bme_rotine():
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature

    aktivirungs_zeitpunkt = time.time()

    global aktivirungs_anzahl
    

    y= y_BME_Time.view()
    y[aktivirungs_anzahl] = aktivirungs_zeitpunkt
    
    x = x_Luftfeuchtigkeit_Wert.view()
    x[aktivirungs_anzahl] = humidity

    x = x_Luftdruck_Wert.view()
    x[aktivirungs_anzahl] = pressure
    
    x = x_Temperatur_Wert.view()
    x[aktivirungs_anzahl] = ambient_temperature

    aktivirungs_anzahl += 1

    if aktivirungs_anzahl == 5:
        aktivirungs_anzahl = 0 
        quit
    return