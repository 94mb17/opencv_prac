import cv2 as cv

# print(cv.__version__)

cam_obj = cv.VideoCapture(0)

# another way to set the size of window
cam_obj.set(cv.CAP_PROP_FRAME_WIDTH, 191.5)
cam_obj.set(cv.CAP_PROP_FRAME_HEIGHT, 191.5)

# set frame rate of the display
cam_obj.set(cv.CAP_PROP_FPS, 30)
cam_obj.set(cv.CAP_PROP_FOURCC,cv.VideoWriter_fourcc(*'MJPG'))

while True:
    # read frame from the camera
    ignore, frame = cam_obj.read()
    
    # resize the frame
    # frame = cv.resize(frame, (320, 240))

    # convert frame to grayscale
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # web cam 1
    cv.imshow('Windows1', frame)

    # this function opens window given to the position provided 
    # by the user
    cv.moveWindow('Windows1', 0, 0)

    # gray show 1
    cv.imshow('gray1', gray_frame)

    # gray move
    cv.moveWindow('gray1', 330, 0)

    # web cam 2
    cv.imshow('Windows2', frame)

    # this function opens window given to the position provided 
    # by the user
    cv.moveWindow('Windows2', 660, 0)

    # gray show 2
    cv.imshow('gray2', gray_frame)

    # gray move
    cv.moveWindow('gray2', 990, 0)

    # wait for a millisecond if some key is pressed
    # & 0xff is to get the least 8 bits code would work
    # if masking is removed but code would not be robust
    if cv.waitKey(1) & 0xff ==ord('d'):
        break

# to release control of the camera from python on closing of the window
cam_obj.release()