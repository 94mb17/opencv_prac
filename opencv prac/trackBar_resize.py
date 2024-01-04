import cv2 as cv

mx = 580
my = 280
width = 320
# track func

def on_width(val):
    global width
    width = val
    cam_obj.set(cv.CAP_PROP_FRAME_WIDTH, width)
    cam_obj.set(cv.CAP_PROP_FRAME_HEIGHT, int(width*(9/16)))
def mv_winx(val):
    global mx
    mx = val
    cv.moveWindow('Window', mx, my)

def mv_winy(val):
    global my 
    my = val
    cv.moveWindow('Window', mx, val)


# camera object
cam_obj = cv.VideoCapture(0, cv.CAP_DSHOW)

if not cam_obj.isOpened():
    print("Failed to open the video capture device. Another application might be using it.")
else:
    print("The video capture device is accessible.")

cam_obj.set(cv.CAP_PROP_FRAME_HEIGHT, int(width*(9/16)))
cam_obj.set(cv.CAP_PROP_FRAME_WIDTH, width)
cam_obj.set(cv.CAP_PROP_FPS, 30) 

# trackbar

cv.namedWindow('Remove')
cv.resizeWindow('Remove', 300, 110)
cv.moveWindow('Remove', 640, 440)
cv.createTrackbar('X axis', 'Remove', 580, 1000, mv_winx)
cv.createTrackbar('Y axis', 'Remove', 280, 1000, mv_winy)
cv.createTrackbar('Width', 'Remove', 320, 1000, on_width)
x = cv.getTrackbarPos('Width', 'Remove')

#video display
while True:
        
    ignore, frame = cam_obj.read()
        
    cv.imshow('Window', frame)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cam_obj.release()