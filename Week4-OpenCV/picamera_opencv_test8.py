# modified by Prof. Kartik Bulusu and Josephina Libbon for CS1010-Fall2022

import cv2
import numpy as np

#GRADIENTS AND EDGES
cap = cv2.VideoCapture(0)

while True:
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    
    _, frame = cap.read()
    
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame, 100, 200)
    
    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()