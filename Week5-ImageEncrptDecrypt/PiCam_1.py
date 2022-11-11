"""
==== Prof. Kartik V. Bulusu
==== MAE Department, SEAS GWU
==== Description
======== This program incorporates a PiCam
======== It has been written exclusively for CS1010 & APSC1001 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
"""

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180

camera.start_preview(alpha=200)

for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/Fall2022/Week5-ImageEncrptDecrypt/image%s.jpg' % i)
    
camera.stop_preview()
