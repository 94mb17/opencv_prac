import cv2 as c

xPos = 0
yPos = 0

def xrack(val):
    global xPos
    xPos = val
    print(val)

def yrack(val):
    global yPos
    yPos = val
    print(val)

cam_obj = c.VideoCapture(0)
cam_obj.set(c.CAP_PROP_FRAME_WIDTH, 320)
cam_obj.set(c.CAP_PROP_FRAME_HEIGHT, 320)
cam_obj.set(c.CAP_PROP_FPS, 30)
cam_obj.set(c.CAP_PROP_FOURCC, c.VideoWriter_fourcc(*'MJPG'))

c.namedWindow('Track')

c.resizeWindow('Track', 300, 90)

c.createTrackbar('xPos', 'Track', 0, 320, xrack)
c.createTrackbar('yPos', 'Track', 0, 320, yrack)

while True:

    ignore, frame = cam_obj.read()
    
    c.circle(frame, (xPos, yPos), 16, (0, 0, 255), 2)
    c.imshow('Window', frame)

    if c.waitKey(1) & 0xFF ==ord('d'):
        break

cam_obj.release()