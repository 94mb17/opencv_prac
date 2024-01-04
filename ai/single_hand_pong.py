import cv2 as cv
import mediapipe as mp

print(cv.__version__)

# object declared 

def bar(frame):

    hand = mp.solutions.hands.Hands(False, max_num_hands=2, min_detection_confidence=0.1, min_tracking_confidence=0.5)
    results = hand.process(frame)
    
    hands=[]
    if results.multi_hand_landmarks != None:

        for handLandMarks in results.multi_hand_landmarks:
            han = []
            for landmark in handLandMarks.landmark:
                han.append((landmark.x*640, landmark.y*480))
            hands.append(han)

    return hands

cam_obj = cv.VideoCapture(0)

cam_obj.set(cv.CAP_PROP_FPS, 30)
cam_obj.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cam_obj.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
cam_obj.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*'MJPG'))

padColor = (255,0,0)
padWidth = 10
padHeight = 100

# bar 
x1 = 0
x2 = padWidth
y1 = 0
y2 = padHeight

# ball
xb = 320
yb = 240
rb = 2
mx=5
my=5
flag=False

# score
score = 0

while True:

# ball position

    ignore, frame = cam_obj.read()

    frame = cv.resize(frame, (640, 480))
    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    hands = bar(frameRGB)

    for hand in hands:
        
        y1 = int(hand[8][1]-padHeight/2)
        y2 = int(hand[8][1]+padHeight/2)
    
        # score change
        if xb-rb==padWidth and y1<=yb<=y2:
            score+=1
            flag=True
        if xb-rb<padWidth:
            score-=1
            flag = False

        if xb==0 and not flag:
            mx=5
        if yb==0:
            my=5
        if xb==640 or (xb==padWidth and flag):
            mx=-5
        if yb==480:
            my=-5
        
        xb+=mx
        yb+=my
        cv.rectangle(frame, (x1, y1), (x2, y2), padColor, cv.FILLED)
        cv.circle(frame, (xb, yb), rb, (0, 0, 255), -1)
        cv.putText(frame, f'{score}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv.imshow('Windows', frame)

    cv.moveWindow('Windows', 0, 0)

    if cv.waitKey(1) & 0xff ==ord('d'):
        cv.destroyAllWindows()
        break

cam_obj.release()