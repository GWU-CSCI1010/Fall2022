# ==== PROGRAM TO MEASURE THE HEART RATE  ===========================
# ==== Prof. Kartik V. Bulusu
# ==== MAE Department, SEAS GWU
# ==== Description:
# ======== This program incorporates a heart rate sensor .
# ======== It is a prototype or proof of concept for the applications if stated below.
# ======== It has been written exclusively for CS1010 & APSC1001 students in GWU.
# ======== It may not be used for any other purpose unless author's prior permission is acquired.
# ======== Find peaks using Numpy only and not Scipy: https://tcoil.info/find-peaks-and-valleys-in-dataset-with-python/
# ======== https://blog.ytotech.com/2015/11/01/findpeaks-in-python/
# ======== https://github.com/MonsieurV/py-findpeaks

import PCF8591 as ADC
import time
import numpy as np
import matplotlib.pyplot as plt
from detect_peaks import detect_peaks


# =====================================================================
# INTIALIZE VARIABLES =================================================

t = 0
dt = .01
xs = np.array([])
ys = np.array([])
ADC.setup(0x48)

if __name__ == '__main__':
    while t <= 10:
        ys = np.append(ys, ADC.read(0))
        #xs.append(float(time.time()))
        xs = np.append(xs, t)
        time.sleep(dt)
        t += dt
        #print(t,ADC.read(0))
        #print('')

        
    print(">>>> Look at the plot <<<")
    print('')
        
    print("How many peaks can you count despite the noise? ")
    print('')

    print("Close the plot when you are done counting.")
    print('')
    
    # moving average
    data = np.convolve(ys, np.ones(11), 'valid')/11
    # local max
    # +1 due to the fact that diff reduces the original index number
    #peaks = (np.diff(np.sign(np.diff(data))) < 0).nonzero()[0] + 1
    
    p3fit = np.poly1d(np.polyfit(xs[0:np.size(data)], data, 3))
    baseline_corrected = data-p3fit(xs[0:np.size(data)])
    #threshold set to (max - (max-mean)*50%)
    threshold = np.max(baseline_corrected)-((np.max(baseline_corrected) - np.mean(baseline_corrected))*50/100) 
    peaks = detect_peaks(baseline_corrected, mph=threshold)
    
    
    plt.plot(xs,ys, color='lightcoral')
    plt.plot(xs[0:np.size(data)], data, 'k', linewidth=4)
    #plt.show(block=False)
    plt.title('Result of Pulse sensor data')
    plt.xlabel('Time <seconds>')
    plt.ylabel('Digitized pulse reading <-> ')
    plt.grid(True)
    # saving the file.Make sure you 
    # use savefig() before show().
    plt.savefig("Pulse_data1.png")
    plt.show()    
    
    beats = int(input("How many peaks did you count? (Input an integer) "))
    interval = input("What was the time interval in seconds? (Input an two integers with a space) ").strip().split()
    # using list comprehension to
    # perform conversion
    interval = [int(i) for i in interval]
    t_interval = np.diff(interval)
    print('')
    BPM_counting = np.ceil(beats*60/(t_interval[0]))
    print('Heart Rate is ', BPM_counting, 'BPM by manual counting')        
    #indices = np.where(ys > 225)
    #peaks = np.size(indices)
    print('')
    BPM_auto = np.ceil(np.size(peaks)*60/(t))
    print('Heart Rate is ', BPM_auto, 'BPM by this python program')
    print('')

print("NOTE: If your data looks noisy, try changing the gain and rerun!!")
    
plt.ion()
plt.plot(xs,ys,color='lightcoral', label="signal")
plt.plot(xs[0:np.size(data)], data, 'k', label="moving average", linewidth=4)
plt.plot(xs[peaks], data[peaks], "o", label="max", color='b')
#plt.axis([interval[0], interval[1], None, None])
#plt.show(block=False)
plt.title('Result of Pulse sensor data')
plt.xlabel('Time <seconds>')
plt.ylabel('Digitized pulse reading <-> ')
plt.grid(True)
# saving the file.Make sure you 
# use savefig() before show().
plt.savefig("Pulse_data2.png")
plt.show() 
#plt.pause(5)
#plt.close('all')

