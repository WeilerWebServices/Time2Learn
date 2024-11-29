#!python3

# Basic Video Capture in openCV

import numpy as np
import cv2

cap=cv2.VideoCapture('Phonics-Song-2.mp4')

while(True):
        ret, frame=cap.read()

        cv2.imshow('output',frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
        
cap.release()
cv2.destroyAllWindows()
