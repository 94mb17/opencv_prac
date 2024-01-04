import cv2 as cv
import face_recognition as fc

cam_obj = cv.VideoCapture(0)

face_rgb = fc.load_image_file("C:\\Users\\eclos\\OneDrive\\Desktop\\rai.jpg")
face_encode_rai = fc.face_encodings(face_rgb)[0]

face_rgb = fc.load_image_file("C:\\Users\\eclos\\OneDrive\\Desktop\\me.jpg")
face_encode_me = fc.face_encodings(face_rgb)[0]

known_encoding = [face_encode_rai, face_encode_me]
known_face = ['rai', 'me']

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