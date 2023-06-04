# bme
def bme_rotine():
    port = 1
    address = 0x77 # Adafruit BME280 address. Other BME280s may be different
    bus = smbus2.SMBus(port)
    bme280.load_calibration_params(bus,address)
    bme280_data = bme280.sample(bus,address)
    # das obere sollte aus dem loop raus 
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature

    x = x_Luftfeuchtigkeit_Wert.view()
    x[i] = humidity
    i += 1

    x = x_Luftdruck_Wert.view()
    x[j] = pressure
    j += 1
    
    x = x_Temperatur_Wert.view()
    x[k] = ambient_temperature
    k += 1

    y = y_BME_Time.view()
    y[l] = function # dieses musss zu einer geändert werden die die zeit überegibt 
    l +=1

    return