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

# =========== DISPLAY ONE ALPHABET ON THE LED MATRIX =========================

sense.show_letter("A", text_colour=[0,0,255])
time.sleep(2)
sense.clear()

# =========== DISPLAY A MESSAGE ON THE LED MATRIX ============================

# sense.show_message("Hello APSC1001 and CS1010", text_colour=[0,255,0])

# =========== GET THE ORIENTATION DATA [Pitch, Yaw and Roll] =================

orientation_data = sense.get_orientation()

pitch = orientation_data['pitch']
yaw = orientation_data['yaw']
roll = orientation_data['roll']

# =========== ORIENTATION SENSING =============================
timeElapsed = 0

while timeElapsed < 2:
        
        pitch = round(pitch,1)
        yaw = round(yaw,1)
        roll = round(roll,1)
        
        msg = "pitch = %d, yaw = %d, roll =%d" % (pitch, yaw, roll)
        
        sense.show_message(msg, scroll_speed=0.05)
        
        time.sleep(1)
        timeElapsed = timeElapsed+1     
        
        sense.clear()