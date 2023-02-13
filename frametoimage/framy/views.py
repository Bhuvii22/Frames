from django.shortcuts import render,redirect
import cv2
import os
from framy import *
def frame(request):
    return render (request,'frame.html')
try:

    # creating a folder named data
    if not os.path.exists('images'):
        os.makedirs('images')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')
def image(vid):
    vid = cv2.VideoCapture("D:\BHUVAN/b1.mp4")
    vid.set(cv2.CAP_PROP_FPS,5)
    currentframe = 0
    while (True):
        success, frame = vid.read()
        vid.set(cv2.CAP_PROP_FPS,5)
        #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        if currentframe % 5==0:
            name = './images/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)
        

        # writing the extracted images
        cv2.imwrite(name,hsv)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
       
        if currentframe>=200:
            break
        elif cv2.waitKey(1)& 0xFF ==ord('q'):
             break
# Release all space and windows once done
    vid.release()
    cv2.destroyAllWindows()
    return redirect('image.html')