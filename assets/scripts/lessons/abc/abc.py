#!python3

# ABC Song Video

import cv2
import numpy as np

capture=cv2.VideoCapture('../video/Phonics-Song.mp4')

if (capture.isOpened()==False):
	print("Video Failed to Open")

while(capture.isOpened()):

	ret,frame=capture.read()
	if ret==True:
		cv2.imshow("Frame",frame)
		if cv2.waitKey(25) & 0xFF==ord('q'):
			break


	else:
		break
capture.release()
cv2.destroyAllWindows()

