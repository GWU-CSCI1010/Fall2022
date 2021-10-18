"""
==== Prof. Kartik V. Bulusu
==== MAE Department, SEAS GWU
==== Description
======== This program incorporates the RaspberryPi SenseHat sensors and library
============ SenseHat documentation: https://www.raspberrypi.com/documentation/accessories/sense-hat.html
======== It has been written exclusively for CS1010 & APSC1001 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
"""

# =========== IMPORT MODULES THAT WORK WITH SENSE HAT ========================

from sense_hat import SenseHat
import time

sense = SenseHat()

# =========== GET THE SENSE HAT TO LIGHT UP ONE LED ==========================

sense.set_pixel(7,7,255,0,0)
time.sleep(2)
sense.clear()

# =========== DISPLAY ONE ALPHABET ON THE LED MATRIX =========================

sense.show_letter("A", text_colour=[0,0,255])
time.sleep(2)
sense.clear()

# =========== ENVIRONMENTAL SENSING =============================
timeElapsed = 0

while timeElapsed < 2:
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()
        
        t = round(t,1)
        p = round(p,1)
        h = round(h,1)
        
        msg = "Temp = %s C, Pressure = %s mbar, Humidity =%s" % (t, p, h)
        
        sense.show_message(msg, scroll_speed=0.05)
        
        time.sleep(1)
        timeElapsed = timeElapsed+1     
        
        sense.clear()