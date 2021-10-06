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
    finally:
	destroy()
