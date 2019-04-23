import cv2
import numpy as np
from datetime import datetime, date, time

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

counter = 0
second = 0
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

    smallFrame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 

    result = smallFrame

    cv2.imshow('image', result)

    counter += 1

    k = cv2.waitKey(5)
    if k == ord(' '):
        nowTime = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        filename = str(nowTime)  + ".jpg"
        filepath = "sample_images/" + filename
        cv2.imwrite(filepath, result)
        print("Take picture!!! -> " + filename)

    # http://www.asciitable.com
    elif k == 27:
        print("pressed key: [" + str(k) +"]")
        break