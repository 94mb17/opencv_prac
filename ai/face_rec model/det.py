# for database
import mysql.connector

# for decoding
import base64 as b

# for face recognition
import cv2 as cv
import face_recognition as fc

# for deocding
import numpy as np

# connection established
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="faceattendence"
)

# storage created
known_encoding = []
known_face = []

# cursor created
cursor = mydb.cursor()

# data fetched
cursor.execute("SELECT * FROM attendance")

#data traversed
for x in cursor:

    # decoding
    decode = b.b64decode(x[1])
    
    # appending
    known_encoding.append(decode)

    # appending
    known_face.append(x[0])

print(known_encoding[0])
print(known_encoding[1])

# setting camera
cam_obj = cv.VideoCapture(0)

# for face detection
faceCascade = cv.CascadeClassifier('D:\\python_vm\\haar\\haarcascade_frontalface_default.xml')

while True:

    ignore, frame = cam_obj.read()

    m = frame

    face_encode = fc.face_encodings(frame)
    
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

    face_loc = faceCascade.detectMultiScale(frame, 1.3, 5)
    
    
    for f in face_loc:
        # print(top, right, bottom, left)
        for face,name in zip(known_encoding,known_face):
            if face_encode and fc.compare_faces([face], face_encode[0])[0]:
                cv.rectangle(m, (f[0], f[1]), (f[0]+f[2], f[1]+f[3]), (0, 255, 0), 2)
                cv.putText(m, name, (f[0], f[1]-3), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv.imshow('frame', m)
                cv.moveWindow('frame', 530, 280)
                break
    
    if cv.waitKey(1) & 0xFF == ord('d'):
        cv.destroyAllWindows()
        break
cam_obj.release()