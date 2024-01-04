import cv2 as c

cam_obj = c.VideoCapture(0)

cam_obj.set(c.CAP_PROP_FRAME_WIDTH, 320)
cam_obj.set(c.CAP_PROP_FRAME_HEIGHT, 320)
cam_obj.set(c.CAP_PROP_FPS, 30)
cam_obj.set(c.CAP_PROP_FOURCC, c.VideoWriter_fourcc(*'MJPG'))

while True:

    ignore, frame = cam_obj.read()

    ignore, f = cam_obj.read()

    frameROI = frame[120:180, 120:180]

    frameROIGrayScale = c.cvtColor(frameROI, c.COLOR_BGR2GRAY)

    # this is used because when we assign gray scale image from above in the parts the grayscale image is a matrix 320 x 320 x 1 and bgr image is 320 x 320 x 3
    # so we need to convert it to bgr (1 for gray scale because it takes values from 0 to 255 and 3 for bgr because it takes values from (0-255, 0-255, 0-255))
    frameROIGrayScale = c.cvtColor(frameROIGrayScale, c.COLOR_GRAY2BGR) 
    
    f[10:70, 10:70] = frameROIGrayScale

    c.rectangle(f, (120, 120), (180, 180), (200, 206, 0), 2)

    c.imshow('Window', f)
    c.imshow('WindowROI', frameROI)
    c.imshow('WindowROIGrayScale', frameROIGrayScale)

    c.moveWindow('Window', 580, 280)
    c.moveWindow('WindowROI', 280, 280)
    c.moveWindow('WindowROIGrayScale', 980, 280)

    if c.waitKey(1) & 0xff == ord('d'):
        break

cam_obj.release()