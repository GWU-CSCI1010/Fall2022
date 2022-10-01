"""
==== Prof. Kartik V. Bulusu
==== MAE Department, SEAS GWU
==== Description
======== This program is for continuously blinking an LED wired to Raspberry PI
======== It has been written exclusively for CS1010 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

def loop():
    while True:
        GPIO.output(12, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(12, GPIO.LOW)
        time.sleep(0.5)

def destroy():
    GPIO.output(12, GPIO.LOW)    # Turn off all leds
    GPIO.cleanup()
        
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
