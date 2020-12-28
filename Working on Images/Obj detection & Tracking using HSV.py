import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0)  # for object detection in video/ camera

c = cv2.namedWindow('Tracker')
cv2.resizeWindow('Tracker', 512, 512)
cv2.createTrackbar('LH', 'Tracker', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracker', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracker', 0, 255, nothing)
cv2.createTrackbar('UH', 'Tracker', 255, 255, nothing)
cv2.createTrackbar('US', 'Tracker', 255, 255, nothing)
cv2.createTrackbar('UV', 'Tracker', 255, 255, nothing)

while True:
    # frame = cv2.imread('Colour test image.jpeg') # for obj det. in image
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH', 'Tracker')
    l_s = cv2.getTrackbarPos('LS', 'Tracker')
    l_v = cv2.getTrackbarPos('LV', 'Tracker')
    u_h = cv2.getTrackbarPos('UH', 'Tracker')
    u_s = cv2.getTrackbarPos('US', 'Tracker')
    u_v = cv2.getTrackbarPos('UV', 'Tracker')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('image', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break

cap.read()
cv2.destroyAllWindows()
