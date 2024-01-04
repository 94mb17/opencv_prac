import cv2 as c

evt = 0
f=0
def on_mouse(event, x, y, flags, param):
    global evt
    global pnt1
    global pnt2
 
    if event == c.EVENT_LBUTTONDOWN:
        evt = event
        pnt1 = (x, y)

    if event == c.EVENT_LBUTTONUP:
        evt = event
        pnt2  = (x, y)
    
    if event == c.EVENT_RBUTTONUP:
        evt = event

cam_obj = c.VideoCapture(0)

cam_obj.set(c.CAP_PROP_FRAME_WIDTH, 320)
cam_obj.set(c.CAP_PROP_FRAME_HEIGHT, 320)
cam_obj.set(c.CAP_PROP_FPS, 30)
cam_obj.set(c.CAP_PROP_FOURCC, c.VideoWriter_fourcc(*'MJPG'))
c.namedWindow('Window')
c.setMouseCallback('Window', on_mouse)

while True:

    ignore, frame = cam_obj.read()
    
    if evt == 4:
        frameROI = frame[pnt1[1]:pnt2[1], pnt1[0]:pnt2[0]]
        c.rectangle(frame, pnt1, pnt2, (0, 0, 255), 2)
        c.imshow('WindowROI', frameROI)
        c.moveWindow('WindowROI', 580, 280)
    if evt == 5:
        c.destroyWindow('WindowROI')
        evt = 0

    c.imshow('Window', frame)
    c.moveWindow('Window', 290, 140)

    if c.waitKey(1) & 0xFF == ord('d'):
        break

cam_obj.release()