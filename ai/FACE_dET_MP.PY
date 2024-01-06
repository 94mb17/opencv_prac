import cv2 as cv
import mediapipe as mp

def fac(frame):
    result = findFace.process(frame)
    if result.detections != None:
        for face in result.detections:
            # box.draw_detection(frame, face)
            f = face.location_data.relative_bounding_box
            left = (int(f.xmin * 640), int(f.ymin * 480))
            right = (int(f.xmin * 640 + f.width * 640), int(f.ymin * 480 + f.height * 480))
            return left, right

cam_obj = cv.VideoCapture(0)

cam_obj.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cam_obj.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
cam_obj.set(cv.CAP_PROP_FPS, 30)
cam_obj.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*'MJPG'))

findFace = mp.solutions.face_detection.FaceDetection()
box = mp.solutions.drawing_utils

while True:

    ret, frame = cam_obj.read()
    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame=cv.resize(frame, (640, 480))

    left, right = fac(frameRGB)
    cv.rectangle(frame, left, right, (155, 140, 0), 2)

    cv.imshow('Windows', frame)
    cv.moveWindow('Windows', 520, 200)
    if cv.waitKey(1) & 0xff == ord('q'):
        cv.destroyAllWindows()
        cam_obj.release()
        break