import cv2 as cv

print(cv.__version__)

cam_obj = cv.VideoCapture(0)

while True:
    # read frame from the camera
    ignore, frame = cam_obj.read()
    
    # web cam
    cv.imshow('Windows', frame)

    # this function opens window given to the position provided 
    # by the user
    cv.moveWindow('Windows', 984, 512)

    # wait for a millisecond if some key is pressed
    # & 0xff is to get the least 8 bits code would work
    # if masking is removed but code would not be robust
    if cv.waitKey(1) & 0xff ==ord('d'):
        break

# to release control of the camera from python on closing of the window
cam_obj.release()