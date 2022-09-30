# ==== PROGRAM TO MEASURE THE ROTATIONS PER MINUTE (RPM) of Cordless Screw Driver ===========================
# ==== Prof. Kartik V. Bulusu
# ==== MAE Department, SEAS GWU
# ==== Description:
# ======== This program incorporates a senseHat.
# ======== It is a prototype or proof of concept for the applications if stated below.
# ======== It has been written exclusively for CS1010 & APSC1001 students in GWU.
# ======== It may not be used for any other purpose unless author's prior permission is acquired.
# ======== Find peaks using Numpy only and not Scipy: https://tcoil.info/find-peaks-and-valleys-in-dataset-with-python/
# ======== https://blog.ytotech.com/2015/11/01/findpeaks-in-python/
# ======== https://github.com/MonsieurV/py-findpeaks

# =========== IMPORT MODULES THAT WORK WITH SENSE HAT ========================

from sense_hat import SenseHat
import time
import numpy as np
import matplotlib.pyplot as plt
from detect_peaks import detect_peaks


sense = SenseHat()
raw = sense.get_compass_raw()


#print("x: (), y: = (y), z: (z)".format(**raw))
#while True:
#    print(sense.compass_raw)
    
t = 0
dt = .01
xs = np.array([])
ys = np.array([])

if __name__ == '__main__':
    while t <= 5:
            #print(sense.compass_raw)
            compass_list = list(sense.compass_raw.values())
            #print(compass_list)
            compass_array = np.array(compass_list)
            #print(compass_array)
            ys = np.concatenate((ys, compass_array))
            ##xs.append(float(time.time()))
            xs = np.append(xs, t)
            time.sleep(dt)
            t += dt
            
ys =ys.reshape(int(ys.size/3),3)
ysX = ys[:,0]
ysY = ys[:,1]
ysZ = ys[:,2]

# ======== Baseline correction in X, Y and Z directions ===================
p3fitX = np.poly1d(np.polyfit(xs[0:np.size(ysX)], ysX, 3))
p3fitY = np.poly1d(np.polyfit(xs[0:np.size(ysY)], ysY, 3))
p3fitZ = np.poly1d(np.polyfit(xs[0:np.size(ysZ)], ysZ, 3))

baselineX_corrected = ysX-p3fitX(xs[0:np.size(ysX)])
baselineY_corrected = ysY-p3fitY(xs[0:np.size(ysY)])
baselineZ_corrected = ysZ-p3fitZ(xs[0:np.size(ysZ)])


# ======== Thresholding in X, Y and Z directions ===================
thresholdX = np.max(baselineX_corrected)-((np.max(baselineX_corrected) - np.mean(baselineX_corrected))*50/100)
thresholdY = np.max(baselineY_corrected)-((np.max(baselineY_corrected) - np.mean(baselineY_corrected))*50/100)
thresholdZ = np.max(baselineZ_corrected)-((np.max(baselineZ_corrected) - np.mean(baselineZ_corrected))*50/100)

# ======== Peak Detection in X, Y and Z directions ===================
peaksX = detect_peaks(baselineX_corrected, mph=thresholdX)
peaksY = detect_peaks(baselineY_corrected, mph=thresholdY)
peaksZ = detect_peaks(baselineZ_corrected, mph=thresholdZ)


print('')
RPM_autoX = np.ceil(np.size(peaksX)*60/(t))
RPM_autoY = np.ceil(np.size(peaksY)*60/(t))
RPM_autoZ = np.ceil(np.size(peaksZ)*60/(t))

RPM_auto = np.ceil(np.max([RPM_autoX, RPM_autoY, RPM_autoZ]))

print('Maximum Rotations Per Minute (RPM) across X-, Y- and Z-directions = ', RPM_auto, '(Calculated by this python program)')
print('')

# ======== Plotting data from X, Y and Z directions ===================
plt.plot(xs,ysX, color='red', label='x-direction')
plt.plot(xs,ysY, color='blue', label='y-direction')
plt.plot(xs,ysZ, color='lightcoral', label='z-direction')

plt.plot(xs[peaksX], ysX[peaksX], "o", label="X-peaks", color='m')
plt.plot(xs[peaksY], ysY[peaksY], "s", label="Y-peaks", color='m')
plt.plot(xs[peaksZ], ysZ[peaksZ], "X", label="Z-peaks", color='m')
#plt.plot(xs[0:np.size(data)], data, 'k', linewidth=4)
    #plt.show(block=False)
plt.title('Magentometer data')
plt.xlabel('Time <seconds>')
plt.ylabel('Digitized reading <micro Teslas> ')
plt.grid(True)
plt.legend();
plt.show()

