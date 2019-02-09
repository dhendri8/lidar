import cv2
import numpy as np

def callback(x):
    pass

cap = cv2.VideoCapture(1)
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

    smallFrame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 
    rotated = cv2.rotate(smallFrame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    rows_max = rotated.shape[0]
    cols_max = rotated.shape[1]

    # print (str(rows_max))
    # print (rotated.shape)
    result = rotated[200:rows_max-200, 0:cols_max]
    rows_max = result.shape[0]
    cols_max = result.shape[1]

    # Trying to find brightest location on screen
    gray_trimmed = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    

    radius = 41
    new_gray = cv2.GaussianBlur(gray_trimmed, (radius, radius), 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(new_gray)
    cv2.circle(result, maxLoc, radius, (255, 0, 0), 2)
    print (maxLoc)

    brightest_row = maxLoc[0]
    brightest_col = maxLoc[1]
    # break

    # cv2::rotate(image, image, cv::ROTATE_90_CLOCKWISE);

    # result = result[brightest_row-30:brightest_row+30, 0:cols_max]

    crosshair_size = 10
    cv2.line(result,(int(cols_max/2),int((rows_max/2)-crosshair_size)),(int(cols_max/2),int((rows_max/2)+crosshair_size)),(255,255,255),1)
    cv2.line(result,(int((cols_max/2)-crosshair_size),int(rows_max/2)),(int((cols_max/2)+crosshair_size),int(rows_max/2)),(255,255,255),1)

    cv2.imshow('image', result)

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