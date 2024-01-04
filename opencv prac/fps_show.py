import cv2 as c
import time

cam_obj = c.VideoCapture(0)

cam_obj.set(c.CAP_PROP_FRAME_WIDTH, 320)
cam_obj.set(c.CAP_PROP_FRAME_HEIGHT, 320)
cam_obj.set(c.CAP_PROP_FPS, 30)
cam_obj.set(c.CAP_PROP_FOURCC, c.VideoWriter_fourcc(*'MJPG'))

s_time = time.time()
# no_of_frame = 0
time.sleep(0.1)
fpsFilter = 0

while True:


    currentTime = time.time()
    
    # no_of_frame = no_of_frame + 1

    t = currentTime - s_time
    s_time = currentTime

    # fps = no_of_frame / t - this gives average time per frame

    if t > 0:
        fps = (1 // t)

    # trust value is assigned as it gives more accurate value trusting that the last fps value is in majority
    ignore, frame = cam_obj.read()

    c.putText(frame, 'fps: '+ str(fps) + ' actual fps: ' + str(cam_obj.get(c.CAP_PROP_FPS)), (120, 120), c.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 3)

    c.imshow('Window', frame)
    c.moveWindow('Window', 580, 280)

    if c.waitKey(1) & 0xff == ord('d'):
        break

cam_obj.release()
c.destroyAllWindows()