import io
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy
import time

#Create a memory stream so photos doesn't need to be saved in a file
#stream = io.BytesIO()
#Source: https://pythonprogramming.net/raspberry-pi-camera-opencv-face-detection-tutorial/
#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

# allow the camera to warmup
time.sleep(0.1)

# with picamera.PiCamera() as camera:
#     camera.resolution = (320, 240)
#     camera.capture(stream, format='jpeg')

# #Convert the picture into a numpy array
# buff = numpy.frombuffer(stream.getvalue(), dtype=numpy.uint8)
# 
# #Now creates an OpenCV image
# image = cv2.imdecode(buff, 1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    #Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier("/home/pi/opencv-3.4.1/data/haarcascades/haarcascade_frontalface_default.xml")

    #Convert to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

# print("Found "+str(len(faces))+" face(s)")

    #Draw a rectangle around every found face
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

#Save the result image
#     cv2.imwrite('result.jpg',image)
    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF