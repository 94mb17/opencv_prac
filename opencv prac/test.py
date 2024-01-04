import cv2 as cv
import mediapipe as mp

def dist(t, p):
    return ((t[0] - p[0])**2 + (t[1] - p[1])**2)**0.5

print(cv.__version__)

cam_obj = cv.VideoCapture(0)

hand = mp.solutions.hands.Hands(False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
box = mp.solutions.drawing_utils

up = []
right = []
left = []
down = []

while True:
    ignore, frame = cam_obj.read()
    frame = cv.resize(frame, (640, 480))

    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hand.process(frameRGB)

    itr = 0

    if results.multi_hand_landmarks is not None:
        for handLandMarks in results.multi_hand_landmarks:
            hand_pts = []
            for landmark in handLandMarks.landmark:
                hand_pts.append((int(landmark.x*640), int(landmark.y*480)))

            key = input("u for up, r for right, l for left, d for down: ")

            if key == 'u':
                if not up and len(hand_pts) >= 9:
                    up.append((int(abs(hand_pts[5][0] - hand_pts[8][0])), int(abs(hand_pts[5][1] - hand_pts[8][1]))))
                    itr += 1

            if key == 'r':
                if not right and len(hand_pts) >= 5:
                    right.append((int(abs(hand_pts[1][0] - hand_pts[4][0])), int(abs(hand_pts[1][1] - hand_pts[4][1]))))
                    itr += 1

            if key == 'l':
                if not left and len(hand_pts) >= 21:
                    left.append((int(abs(hand_pts[17][0] - hand_pts[20][0])), int(abs(hand_pts[17][1] - hand_pts[20][1]))))
                    itr += 1

            if key == 'd':
                if not down and len(hand_pts) >= 17:
                    down.append((int(abs(hand_pts[13][0] - hand_pts[16][0])), int(abs(hand_pts[13][1] - hand_pts[16][1]))))
                    itr += 1

            if itr == 3:
                break

        if up and right and left and down and len(hand_pts) >= 21:
            for handLandMarks in results.multi_hand_landmarks:
                hand_pts = []
                for landmark in handLandMarks.landmark:
                    hand_pts.append((int(landmark.x*640), int(landmark.y*480)))

                if dist(hand_pts[5], hand_pts[8]) == dist(up[0], up[1]):
                    print("u")
                    cv.moveWindow('Windows', 580, 100)

                if dist(hand_pts[1], hand_pts[4]) == dist(right[0], right[1]):
                    print("r")
                    cv.moveWindow('Windows', 290, 280)

                if dist(hand_pts[17], hand_pts[20]) == dist(left[0], left[1]):
                    print("l")
                    cv.moveWindow('Windows', 870, 280)

                if dist(hand_pts[13], hand_pts[16]) == dist(down[0], down[1]):
                    print("d")
                    cv.moveWindow('Windows', 580, 400)

    cv.imshow('Windows', frame)

    if cv.waitKey(1) & 0xff == ord('q'):
        break

cam_obj.release()
cv.destroyAllWindows()