import cv2
import numpy as np
def empty(a):
    pass

framewidth = 500
frameHeight = 350
cap = cv2.VideoCapture(0)
cap.set(10, 150)




cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 640, 240)
cv2.createTrackbar('HueMin', 'Trackbars', 0, 179, empty)
cv2.createTrackbar('HueMax', 'Trackbars', 179, 179, empty)
cv2.createTrackbar('SatMin', 'Trackbars', 0, 255, empty)
cv2.createTrackbar('SatMax', 'Trackbars', 255, 255, empty)
cv2.createTrackbar('ValMin', 'Trackbars', 0, 255, empty)
cv2.createTrackbar('ValMax', 'Trackbars', 255, 255, empty)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (framewidth, frameHeight))
    img = cv2.flip(img, 1)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue_min = cv2.getTrackbarPos('HueMin', 'Trackbars')
    hue_max = cv2.getTrackbarPos('HueMax', 'Trackbars')
    sat_min = cv2.getTrackbarPos('SatMin', 'Trackbars')
    sat_max = cv2.getTrackbarPos('SatMax', 'Trackbars')
    val_min = cv2.getTrackbarPos('ValMin', 'Trackbars')
    val_max = cv2.getTrackbarPos('ValMax', 'Trackbars')

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(img_hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('Img', img)
    cv2.imshow('Mask', mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()