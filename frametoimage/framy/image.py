from django.shortcuts import render

# Create your views here.
import cv2
import os
import time

# Read the video from specified path

vid = cv2.VideoCapture("rtsp://admin:cosmdumayil1965@10.0.0.235:554")
vid.set(cv2.CAP_PROP_FPS,5)

try:

    # creating a folder named data
    if not os.path.exists('bhuvan'):
        os.makedirs('bhuvan')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0
while (True):
        success, frame = vid.read()
        vid.set(cv2.CAP_PROP_FPS,5)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        if currentframe % 5==0:
            name = './bhuvan/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)
        

        # writing the extracted images
        cv2.imwrite(name, gray)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
       

        if cv2.waitKey(1)& 0xFF ==ord('q'):
             break

# Release all space and windows once done
vid.release()
cv2.destroyAllWindows()