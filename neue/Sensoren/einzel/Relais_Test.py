from bibliotheken import *

relaispin = 17

GPIO.setup(relaispin, GPIO.OUT)

GPIO.output(relaispin, GPIO.HIGH) 