import cv2 as cv
import mediapipe as mp

hand = mp.solutions.hands.Hands(False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
box = mp.solutions.drawing_utils

cam_obj = cv.VideoCapture(0)

def dist(x, y):
    s = ((x[0] - y[0])**2 + (y[1] - x[1])**2)**0.5
    if s < 100:
        s = 0
    else:
        s = 1
    return s

# hash of finger positions 
# thumb index middle ring pinky}
stored = [[1,1,1,1,1], [1,1,1,0,0], [1,1,0,0,1], [1,0,0,0,0], [0,0,1,0,0], [1,1,0,0,0], [1,0,0,0,1]]
names = ['High Five', 'Peace', 'Yo', 'Power', 'FUCK U', 'L', 'Y']

while True:

    hands = []
    finger_pos = []

    ret, frame = cam_obj.read()
    frame = cv.resize(frame, (640, 480))
    # mediapipe work on RGB
    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hand.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handLandMarks in results.multi_hand_landmarks:
            hand_pts = []
            box.draw_landmarks(frame, handLandMarks)
            for landmark in handLandMarks.landmark:
                hand_pts.append((int(landmark.x*640), int(landmark.y*480)))
            for i in (1, 5, 9, 13, 17):
                finger_pos.append(dist(hand_pts[i], hand_pts[i+3]))
            hands.append(hand_pts)

    i = 0
    for guess in stored:
        if finger_pos == guess:
            cv.rectangle(frame, (10, 10), (90, 90), (0, 105, 120), 2)
            cv.putText(frame, names[i], (20, 50), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        i+=1

    cv.imshow('Windows', frame)
    if cv.waitKey(1) & 0xff == ord('d'):
        cv.destroyAllWindows()
        break