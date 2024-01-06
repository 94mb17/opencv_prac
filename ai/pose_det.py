import cv2 as cv
import mediapipe as mp

cam_obj = cv.VideoCapture(0)

cam_obj.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cam_obj.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
cam_obj.set(cv.CAP_PROP_FPS, 30)
cam_obj.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*'MJPG'))

pose = mp.solutions.pose.Pose(static_image_mode=False,
                               model_complexity=1,
                               enable_segmentation=True,
                               smooth_landmarks=True,
                               min_detection_confidence=0.5,
                               min_tracking_confidence=0.5)

while True:
    ignore, frame = cam_obj.read()
    frame = cv.resize(frame, (640, 480))
    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = pose.process(frameRGB)
    land = []
    if results.pose_landmarks != None:
        # mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
        for l in results.pose_landmarks.landmark:
            land.append((int(l.x*640), int(l.y*480)))
    
    #nose
        cv.circle(frame, (land[0]), 5, (160, 0, 155), -1)
    #eyes
        cv.circle(frame, (land[2]), 5, (120, 90, 155), -1)
        cv.circle(frame, (land[5]), 5, (120, 90, 155), -1)
        
    cv.imshow('Frame', frame)

    if cv.waitKey(1) & 0xFF == ord('d'):
        cv.destroyAllWindows()
        cam_obj.release()
        break
