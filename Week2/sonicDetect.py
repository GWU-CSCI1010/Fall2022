# IMPORT LIBRARIES ====================================================

import RPi.GPIO as GPIO
import time
import csv
# =====================================================================

# INTIALIZE GPIO-PINS =================================================
# Declare the channels for each device

TRIG = 12 #Ultrasound projector
ECHO = 11 #Ultrasound Receiver
SPEAK = 13 #Buzzer
# =====================================================================

# INTIALIZE VARIABLES =================================================

timeElapsed = 0
threshold = 50
# =====================================================================


# DEFINE FUNCTIONS ====================================================
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Set up GPIO mode and define input and output pins

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(SPEAK, GPIO.OUT)
    
    global buzz
    buzz = GPIO.PWM(SPEAK, 400) #S ets the speaker's channel to 440hz
    buzz.start(100) # Sends a constant high voltage (duty cycle of 100%)

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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                
# Returns a frequency from 440-880hz
# Frequency increases as distance decreases

def getFreq(dist):
    global threshold
    return 880 - (440 * dist/threshold)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                
# WRITE DATA TO CSV FILE AND PRINT ON TERMINAL for 10 seconds

def loop():
    
    global csvfile
    with open("test.csv",'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Time(s)', 'Distance(cm)'])
        
        global timeElapsed
        while timeElapsed <= 10:
            # writes the time elapsed and distance measured
            # Turns speaker on if object within 'threshold'
            dist = distance()
            print(timeElapsed, 's', dist, 'cm')
            print('')
            csvwriter.writerow([timeElapsed, dist])

            time.sleep(0.1)
            timeElapsed = timeElapsed+0.1
            
            global threshold
            if(dist<threshold):
                buzz.ChangeDutyCycle(50)
                buzz.ChangeFrequency(getFreq(dist))
            else:
                buzz.ChangeDutyCycle(100)
                
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
# CLEAR GPIO CHANNELS, STOP Buzzer and close CSV FILEs

def destroy():
    buzz.stop()
    GPIO.output(SPEAK, 1)
    GPIO.cleanup()
    csvfile.close()
# ====================================================================

# MAIN FUNCTION to RUN PROGRAM  ======================================

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt: #Quits out on ctrl+c
        destroy()
# ====================================================================