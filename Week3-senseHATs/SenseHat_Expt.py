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

# =========== DISPLAY A MESSAGE ON THE LED MATRIX ============================

sense.show_message("Hello APSC1001 and CS1010", text_colour=[0,255,0])

# =========== DRAW A PICTURE ON THE LED MATRIX ===============================

R = [255, 0, 0]
B = [0, 0, 255]
W = [0, 0, 0]

pixel_list = [W, W, W, W, W, W, W, W,
              W, R, R, W, W, R, R, W,
              W, R, R, W, W, R, R, W,
              W, W, W, B, B, W, W, W,
              W, R, W, B, B, W, R, W,
              W, R, W, W, W, W, R, W,
              W, W, R, R, R, R, W, W,
              W, W, W, R, R, W, W, W]

sense.set_pixels(pixel_list)
time.sleep(5)
sense.clear()

# =========== GET THE ORIENTATION DATA [Pitch, Yaw and Roll] =================

orientation_data = sense.get_orientation()

pitch = orientation_data['pitch']
yaw = orientation_data['yaw']
roll = orientation_data['roll']

# =========== GET COMPASS DATA [X, Y and Z] ==================================

compass_data = sense.get_compass_raw()

m_x = compass_data['x']
m_y = compass_data['y']
m_z = compass_data['z']

# =========== GET ACCELEROMETER DATA [AX, AY and AZ] =========================

accelerometer_data = sense.get_accelerometer_raw()

a_x = accelerometer_data['x']
a_y = accelerometer_data['y']
a_z = accelerometer_data['z']

# =========== GET GRYOSCOPE DATA [GX, GY and GZ] =============================

gyroscope_data = sense.get_gyroscope_raw()

g_x = gyroscope_data['x']
g_y = gyroscope_data['y']
g_z = gyroscope_data['z']


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