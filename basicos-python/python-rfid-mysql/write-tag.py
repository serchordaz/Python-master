#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)

reader = SimpleMFRC522()

try:
        text = input('Escribe tu nombre:')
        print("Coloca tu Tag en el Sensor")
        reader.write(text)
        print("Escrito")
finally:
        GPIO.cleanup()