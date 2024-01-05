import cv2 as cv
import mediapipe as mp

print(cv.__version__)

def l_r(frame):
    results = hand.process(frame)

    if results.multi_hand_landmarks != None:
        
        handType = []
        # this gives an array of classifications-
        # index
        # score
        # label - left, right

        # for h in results.multi_handedness:
        #     print(h)

        # this gives an array of classifications but only
        # index
        # score
        # label - left, right
        
        # for h in results.multi_handedness:
        #     print(h.classifications)

        # since there will be only one classification in the array
        # for h in results.multi_handedness:
        #     print(h.classifications[0])

        # for only getting the label
        for h in results.multi_handedness:
            handtype = h.classifications[0].label
            handType.append(handtype)

        for handLandMarks in results.multi_hand_landmarks:
            hand_pts = []
            # box.draw_landmarks(frame, handLandMarks)
            for landmark in handLandMarks.landmark:
                hand_pts.append((int(landmark.x*640), int(landmark.y*480)))

            hands.append(hand_pts)
        return hands, handType

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
    hands, type = l_r(frameRGB)

    for hand, t in hands,type:
        if t=='right':
            color = (0, 0, 255)
        else:
            color = (255, 0, 0)
        for ind in hand:
            cv.putText(frame, t, (hand[0]), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv.imshow('Windows', frame)

    cv.moveWindow('Windows', 580, 280)

    if cv.waitKey(1) & 0xff ==ord('d'):
        break

cam_obj.release()