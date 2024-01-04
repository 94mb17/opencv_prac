import cv2 as c

cam_obj = c.VideoCapture(0)
cam_obj.set(c.CAP_PROP_FRAME_WIDTH, 320)
cam_obj.set(c.CAP_PROP_FRAME_HEIGHT, 320)
cam_obj.set(c.CAP_PROP_FPS, 30)
cam_obj.set(c.CAP_PROP_FOURCC, c.VideoWriter_fourcc(*'MJPG'))

while  True:

    ignore, frame = cam_obj.read()

    # using slicing and not function 
    frame[140:180, 140:180] = (205, 206, 135)    # sky blue square at center 

    # first point gives upper left and send point gives lower right in (x, y) order
    # frame matrix , left upper point, right lower point, color, thickness (can't be an integer)
    c.rectangle(frame, (120, 140), (180, 180), (205, 6, 0), -1)
    c.rectangle(frame, (120, 140), (180, 180), (0, 206, 0), 2)
    c.circle(frame, (150, 160), 16, (0, 0, 255), 2)
    c.putText(frame, 'image operations series', (120, 120), c.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    c.imshow('Window', frame)
    c.moveWindow('Window', 580, 280)


    if c.waitKey(1) & 0xFF == ord('d'):
        break

cam_obj.release()