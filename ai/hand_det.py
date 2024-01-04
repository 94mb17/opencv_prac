import cv2 as cv
import mediapipe as mp

print(cv.__version__)

cam_obj = cv.VideoCapture(0)

# calls hands method - if hands are to be detected in still frame pass True
# otherwise pass False as done, number of hands to detect,
# min detection confidence
hand = mp.solutions.hands.Hands(False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
box = mp.solutions.drawing_utils


while True:

    hands = []
    ignore, frame = cam_obj.read()
    frame = cv.resize(frame, (640, 480))
    #mediapipe work on RGB
    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hand.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handLandMarks in results.multi_hand_landmarks:
            hand_pts = []
            # box.draw_landmarks(frame, handLandMarks)
            for landmark in handLandMarks.landmark:
                hand_pts.append((int(landmark.x*640), int(landmark.y*480)))
            cv.circle(frame, hand_pts[4], 5, (160, 0, 155), -1)
            cv.circle(frame, hand_pts[8], 5, (160, 0, 155), -1)
            cv.circle(frame, hand_pts[12], 5, (160, 0, 155), -1)
            cv.circle(frame, hand_pts[16], 5, (160, 0, 155), -1)
            cv.circle(frame, hand_pts[20], 5, (160, 0, 155), -1)
            hands.append(hand_pts)

    cv.imshow('Windows', frame)

    cv.moveWindow('Windows', 580, 280)

    if cv.waitKey(1) & 0xff ==ord('d'):
        break

cam_obj.release()