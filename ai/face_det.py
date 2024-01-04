import cv2 as cv
import time as t

print(cv.__version__)

cam_obj = cv.VideoCapture(0)
cam_obj.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cam_obj.set(cv.CAP_PROP_FRAME_HEIGHT, 320)

faceCascade = cv.CascadeClassifier('D:\\python_vm\\haar\\haarcascade_frontalface_default.xml')

t.sleep(0.1)

x = 520
y = 280

while True:

    s_t = t.time()

    ignore, frame = cam_obj.read()

    # gray frame name, scale factor, minNeighbors
    face = faceCascade.detectMultiScale(frame, 1.3, 5)

    for f in face:
        cv.rectangle(frame, (f[0], f[1]), (f[0]+f[2], f[1]+f[3]), (0, 255, 0), 2)

    print(face)

    e_t = t.time()

    fps = 1 / (e_t - s_t)
    
    s_t = e_t

    cv.putText(frame, f'{int(fps)}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv.imshow('Windows', frame)

    cv.moveWindow('Windows', int((x/320)*1900), int((y/320)*1000))
    

    if cv.waitKey(1) & 0xff ==ord('d'):
        cam_obj.release()
        break