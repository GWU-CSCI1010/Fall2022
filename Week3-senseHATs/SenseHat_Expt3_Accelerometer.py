# =========== IMPORT MODULES THAT WORK WITH SENSE HAT ========================

from sense_hat import SenseHat
import time

sense = SenseHat()


# =========== GET ACCELEROMETER DATA [AX, AY and AZ] =========================

accelerometer_data = sense.get_accelerometer_raw()

a_x = accelerometer_data['x']
a_y = accelerometer_data['y']
a_z = accelerometer_data['z']


# =========== ORIENTATION SENSING =============================
timeElapsed = 0

while timeElapsed < 2:
        
        a_x = round(a_x,1)
        a_y = round(a_y,1)
        a_z = round(a_z,1)
        
        msg = "Ax = %d, Ay = %d, Az =%d" % (a_x, a_y, a_z)
        
        sense.show_message(msg, scroll_speed=0.05)
        
        time.sleep(1)
        timeElapsed = timeElapsed+1     
        
        sense.clear()