import cv2 as cv
import numpy as np

print(cv.__version__)

evt = 0

def on_color(event, x, y, flag, params):
    global xPos
    global yPos
    global evt
    if event == cv.EVENT_LBUTTONDOWN:
        xPos = x
        yPos = y
        evt = event

cam_obj = cv.VideoCapture(0)

cv.namedWindow('Windows')
cv.setMouseCallback('Windows', on_color)

while True:
    # read frame from the camera
    ignore, frame = cam_obj.read()

    if evt == 1:
        f = np.zeros([320, 320, 3], dtype=np.uint8)
        frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        f[:,:] = frame[yPos][xPos]
        cv.putText(f, f'{frame[yPos][xPos]}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv.imshow('color picker', f)
        cv.moveWindow('color picker', 800, 280)
        evt = 0

    # web cam
    cv.imshow('Windows', frame)

    # this function opens window given to the position provided 
    # by the user
    cv.moveWindow('Windows', 0, 0)

    # wait for a millisecond if some key is pressed
    # & 0xff is to get the least 8 bits code would work
    # if masking is removed but code would not be robust
    if cv.waitKey(1) & 0xff ==ord('d'):
        cam_obj.release()
        break

# to release control of the camera from python on closing of the window