import cv2 as cv
import numpy as np
print(cv.__version__)

def track1(val):
    global hueLow
    hueLow = val

def track2(val):
    global hueHigh
    hueHigh = val

def track3(val):
    global satLow
    satLow = val

def track4(val):
    global satHigh
    satHigh = val

def track5(val):
    global valLow
    valLow = val

def track6(val):
    global valHigh
    valHigh = val

cam_obj = cv.VideoCapture(0)

hueLow = 0
hueHigh = 17
satLow = 0
satHigh = 255
valLow = 0
valHigh = 255

cv.namedWindow('Windows')

cv.createTrackbar('hueLow', 'Windows', 0, 179, track1)
cv.createTrackbar('hueHigh', 'Windows', 17, 179, track2)
cv.createTrackbar('satLow', 'Windows', 0, 255, track3)
cv.createTrackbar('satHigh', 'Windows', 25, 255, track4)
cv.createTrackbar('valLow', 'Windows', 0, 255, track5)
cv.createTrackbar('valHigh', 'Windows', 25, 255, track6)

while True:
    # read frame from the camera
    ignore, frame = cam_obj.read()
    
    # range for object color 
    lower_bound = np.array([hueLow, satLow, valLow])
    upper_bound = np.array([hueHigh, satHigh, valHigh])

    # convert frame to hsv
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv, lower_bound, upper_bound)

    myObject = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('Object', myObject)
    cv.moveWindow('Object', 900, 300)

    cv.imshow('Track', mask)
    cv.moveWindow('Track', 800, 0)

    # web cam
    cv.imshow('main', frame)

    # this function opens window given to the position provided 
    # by the user
    cv.moveWindow('main', 580, 280)


    # wait for a millisecond if some key is pressed
    # & 0xff is to get the least 8 bits code would work
    # if masking is removed but code would not be robust
    if cv.waitKey(1) & 0xff ==ord('d'):
        break

# to release control of the camera from python on closing of the window
cam_obj.release()