import cv2 as c
import numpy as np

frame_sat = np.zeros([256, 720, 3], dtype=np.uint8)
frame_val = np.zeros([256, 720, 3], dtype=np.uint8)

c.namedWindow('Window_val')
c.namedWindow('Window_sat')

c.resizeWindow('Window_val', 500, 500)
c.resizeWindow('Window_sat', 500, 500)

while True:

    for i in range(0, 256):
        for j in range(0, 720):
            frame_sat[i][j] = (int(j/4), i, 255)

    fsat = c.cvtColor(frame_sat, c.COLOR_HSV2BGR)

    for i in range(0, 256):
        for j in range(0, 720):
            frame_val[i][j] = (int(j/4), 255, i)

    fval = c.cvtColor(frame_val, c.COLOR_HSV2BGR)

    c.imshow('Window_sat', fsat)
    c.moveWindow('Window_sat', 0, 0)
    c.imshow('Window_val', fval)
    c.moveWindow('Window_val', 0, 300)

    if c.waitKey(1) & 0xFF == ord('d'):
        c.destroyAllWindows()
        break