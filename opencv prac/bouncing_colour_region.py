import cv2 as c

# def driver(x1, y1, x2, y2, m, fx = 1, fy = 1):

    # boundary conditions
    # if x1 >=0 and x2<=320:
    #     if fx == 1:
    #         x1 = x1 + m
    #         x2 = x2 + m
    #     else:
    #         x1 = x1 - m
    #         x2 = x2 - m
    # elif x1 < 0:
    #     x1 = x1 + m
    #     x2 = x2 + m
    #     fx = 1
    # elif x2 > 320:
    #     x1 = x1 - m
    #     x2 = x2 - m
    #     fx = 0

    # if y1 >=0 and y2<=290:
    #     if fy == 1:
    #         y1 = y1 + m
    #         y2 = y2 + m
    #     else:
    #         y1 = y1 - m
    #         y2 = y2 - m
    # elif y1 < 0:
    #     y1 = y1 + m
    #     y2 = y2 + m
    #     fy = 1
    # elif y2 > 290:
    #     y1 = y1 - m
    #     y2 = y2 - m
    #     fy = 0 



    # print(x1, x2, y1, y2, fx, fy)
    # return x1, y1, x2, y2, fx, fy


cam_obj = c.VideoCapture(0)

cam_obj.set(c.CAP_PROP_FRAME_WIDTH, 320)
cam_obj.set(c.CAP_PROP_FRAME_HEIGHT, 320)
cam_obj.set(c.CAP_PROP_FPS, 30)
cam_obj.set(c.CAP_PROP_FOURCC, c.VideoWriter_fourcc(*'MJPG'))

x1 = 60
y1 = 60
x2 = 60
y2 = 60
# fx = 1
# fy = 0
m = 2
n = 2

while 1:

    ignore, frame = cam_obj.read()

    # x1, y1, x2, y2, fx, fy = driver(x1, y1, x2, y2, 2, fx, fy)        # x and y upper left , x and y lower right, change in x and change in y

    frameGray = c.cvtColor(frame, c.COLOR_BGR2GRAY)

    frameGray = c.cvtColor(frameGray, c.COLOR_GRAY2BGR)
    frameROI = frame[(x1)-30:x2+30, y1-30:y2+30]
    frameGray[(x1)-30:x2+30, y1-30:y2+30] = frameROI

    c.imshow('Window', frameGray)

    if (x1 - 30 <= 0 or x2 + 30 >= 320):
        m = m * -1
    if (y1 - 30 <= 0 or y2 + 30 >= 320):
        n = n * -1

    x1+=m
    x2+=m
    y1+=n
    y2+=n

    if c.waitKey(1) & 0xFF == ord('d'):
        break

cam_obj.release()