import cv2 as cv
import mediapipe as mp

print(cv.__version__)

cam_obj = cv.VideoCapture(0)

faceMesh = mp.solutions.face_mesh.FaceMesh(False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
box = mp.solutions.drawing_utils

draw_spec_circle = box.DrawingSpec(color=(140, 150, 110), thickness=1, circle_radius=2)
draw_spec_line = box.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=0)

while True:
    # read frame from the camera
    ignore, frame = cam_obj.read()

    fameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    results = faceMesh.process(fameRGB)
    print(results.multi_face_landmarks)

    if results.multi_face_landmarks is not None:
        for face in results.multi_face_landmarks:
            i = 0
            box.draw_landmarks(frame, face, mp.solutions.face_mesh.FACEMESH_TESSELATION, draw_spec_circle, draw_spec_line)
            for ind in face.landmark:
                cv.putText(frame, str(i), (int(ind.x*640), int(ind.y*480)), cv.FONT_HERSHEY_SIMPLEX, 0.5,(0, 255, 0), 1)
                i+=1
    frame = cv.resize(frame, (640, 480))

    cv.putText(frame, 'hello', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    # web cam
    cv.imshow('Windows', frame)
    # this function opens window given to the position provided 
    # by the user
    cv.moveWindow('Windows', 505, 280)

    # wait for a millisecond if some key is pressed
    # & 0xff is to get the least 8 bits code would work
    # if masking is removed but code would not be robust
    if cv.waitKey(1) & 0xff ==ord('d'):
        break

# to release control of the camera from python on closing of the window
cam_obj.release()