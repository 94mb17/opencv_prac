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

    ignore, frame = cam_obj.read()
    
    lower_bound = np.array([hueLow, satLow, valLow])
    upper_bound = np.array([hueHigh, satHigh, valHigh])

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv, lower_bound, upper_bound)



    contours, ignore = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # frame to be applied, which is to be applied, which array is to be applied,
    # color, thickness

    # cv.drawContours(frame, contours, -1, (0, 255, 0), 3)
    x=0
    y=0
    w=0
    h=0
    for c in contours:
        area = cv.contourArea(c)
        if area >= 100:
            # cv.drawContours(frame, [c], -1, (0, 255, 0), 3)
            x,y, w,h = cv.boundingRect(c)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    myObject = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('Object', myObject)
    cv.moveWindow('Object', 900, 300)

    cv.imshow('Track', mask)
    cv.moveWindow('Track', 800, 0)

    cv.imshow('main', frame)

    cv.moveWindow('main', int(((x+w/2))/320*1900), int((y+h/2)/320*1000))

    if cv.waitKey(1) & 0xff ==ord('d'):
        break

cam_obj.release()