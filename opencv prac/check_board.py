import cv2 as cv
import numpy as np

a = int(input("enter side: "))

c1 = (0, 0, 255) #255
c2 = (0, 0, 0)

size_of_square = 3

''' 
    8 x 8 x 3
    each cell is 3 value of bgr
    each row has 8 cells
    total 8 rows
'''

while True:
    frame = np.zeros([a*size_of_square, a*size_of_square, 3], dtype=np.uint8)

    for l in range(size_of_square):
        for i in range(l,a*size_of_square):
            for j in range(l, a*size_of_square, 6):
                for k in range(3):
                    frame[i, j+k] = c2

    for l in range(size_of_square):
        for i in range(l,a*size_of_square, 6):
            for j in range(size_of_square, a*size_of_square, 6):
                for k in range(size_of_square):
                    frame[i, j+k] = c1

    for i in range(l,a*size_of_square, 6):
        for j in range(size_of_square, a*size_of_square, 6):
            for k in range(size_of_square):
                frame[i, j+k] = c1

    frame = cv.resize(frame, (1000, 1000))

    cv.imshow('checkboard2', frame)


    if cv.waitKey(1) & 0xff == ord('d'):
        break

cv.destroyWindow('checkboard2')