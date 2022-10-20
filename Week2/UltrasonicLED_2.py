"""
==== Prof. Kartik V. Bulusu
==== MAE Department, SEAS GWU
==== Description
======== This program incorporates an Ultrasonic Sensor
======== It has been written exclusively for CS1010 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
"""

# IMPORT MODULES ====================================================

import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt
import csv #https://docs.python.org/3/library/csv.html
# =====================================================================

# INTIALIZE GPIO-PINS =================================================
# Declare the channels for each device

TRIG = 16 #Ultrasound projector
ECHO = 15 #Ultrasound Receiver
RedLED = 12 #Red LED
GreenLED = 11 #Green LED

# =====================================================================

# INTIALIZE VARIABLES =================================================

timeElapsed = 0
threshold = 25 # distance in centimeters
T = np.array([]) # Null array for 'timeElapsed'
D = np.array([]) # Null array for 'dist'
        
# =====================================================================


# DEFINE FUNCTIONS ====================================================
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Set up GPIO mode and define input and output pins

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(RedLED, GPIO.OUT)
    GPIO.setup(GreenLED, GPIO.OUT)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~               
# Function given by SunFounder to calculate distance from sensor

def distance():
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    
    while GPIO.input(ECHO) == 0:
        time1 = time.time()
        
    while GPIO.input(ECHO) == 1:
        time2 = time.time()

    during = time2 - time1
    return during * 340 / 2 * 100 #Returns distance in cm


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                
# WRITE DATA TO CSV FILE AND PRINT ON TERMINAL and WRITE TO CSVfile for 10 seconds

def loop():
    
    global csvfile
    with open("test.csv",'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Time(s)', 'Distance(cm)'])

        global timeElapsed, T, D
        
        while timeElapsed <= 10:
            # writes the time elapsed and distance measured
            # Turns LED to RED if object within 'threshold' distance
            dist = distance()

            print(timeElapsed, 's', dist, 'cm')
            print('')
            csvwriter.writerow([timeElapsed, dist])

            time.sleep(0.1)
            timeElapsed = timeElapsed+0.1
            
            D = np.append(D, dist)
            T = np.append(T, timeElapsed)
            
            global threshold
            if(dist<threshold):
                GPIO.output(11, GPIO.LOW)
                GPIO.output(12, GPIO.HIGH)
            else:
                GPIO.output(11, GPIO.HIGH)
                GPIO.output(12, GPIO.LOW)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PLOTTING TIME (seconds) vs DISTANCE (centimeters)
def plotting():
    plt.plot(T,D)
    plt.title('Result of Ultrasonic sensor data')
    plt.xlabel('Time <seconds>')
    plt.ylabel('Distance <Centimeters> ')
    plt.grid(True)
    plt.show()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
# CLEAR GPIO CHANNELS, STOP Buzzer and close CSV FILEs

def destroy():
    GPIO.cleanup()
    csvfile.close()
# ====================================================================
# MAIN FUNCTION to RUN PROGRAM  ======================================

if __name__ == '__main__':
    setup()
    try:
        loop()
        plotting()
    except KeyboardInterrupt: #Quits out on ctrl+c
        destroy()
# ====================================================================
