import cv2
import numpy as np

def callback(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')

ilowH = 0
ihighH = 179

ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

# create trackbars for color change
cv2.createTrackbar('lowH','image',ilowH,179,callback)
cv2.createTrackbar('highH','image',ihighH,179,callback)

cv2.createTrackbar('lowS','image',ilowS,255,callback)
cv2.createTrackbar('highS','image',ihighS,255,callback)

cv2.createTrackbar('lowV','image',ilowV,255,callback)
cv2.createTrackbar('highV','image',ihighV,255,callback)


while(True):
    # grab the frame
    ret, frame = cap.read()

    # get trackbar positions
    ilowH = cv2.getTrackbarPos('lowH', 'image')
    ihighH = cv2.getTrackbarPos('highH', 'image')
    ilowS = cv2.getTrackbarPos('lowS', 'image')
    ihighS = cv2.getTrackbarPos('highS', 'image')
    ilowV = cv2.getTrackbarPos('lowV', 'image')
    ihighV = cv2.getTrackbarPos('highV', 'image')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)

    frame = cv2.bitwise_and(frame, frame, mask=mask)

    smallFrame = cv2.resize(frame, (0,0), fx=0.75, fy=0.75) 
    cv2.imshow('image', smallFrame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


# while(1):
#     # frame = cv2.imread("frame.jpg")
#     _, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#     lower_red = np.array([30,150,50])
#     upper_red = np.array([255,255,180])

#     lower_green = np.array([50, -20, 215])
#     upper_green = np.array([90, 25, 295])
#     # [ 50 -17 215] [ 90  23 295]
    
#     mask = cv2.inRange(hsv, lower_green, lower_green)
#     res = cv2.bitwise_and(frame,frame, mask= mask)

#     cv2.imshow('frame',frame)

#     # cv2.imshow('mask',mask)
#     cv2.imshow('res',res)
    
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         # Initial frame capture
#         # cv2.imwrite("frame.jpg", frame)
#         break

cv2.destroyAllWindows()
cap.release()