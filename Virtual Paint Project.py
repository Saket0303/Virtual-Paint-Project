import cv2
import numpy as np
framewidth = 750
frameHeight = 600
cap = cv2.VideoCapture(0)
cap.set(10, 150)
myColors = [[70, 121, 200, 135, 255, 255]]
myColorValues = [[205, 0, 0]]
points = [] # [x , y , colorId ]
def findColor(img, mycolor, myColorValue):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in mycolor:
        lower = np.array(color[:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValue[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[1]), mask)
    return newPoints
def getContours(img):
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (0,255,0), 3)
            perimeter = cv2.arcLength(cnt, True)
            # print(perimeter)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y
def DrawOnCanvas(points, myColorValue):
    for point in points:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValue[point[2]], cv2.FILLED)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (framewidth, frameHeight))
    img = cv2.flip(img, 1)
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            points.append(newP)
    if len(points) != 0:
        DrawOnCanvas(points, myColorValues)
    cv2.imshow('Result', imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break