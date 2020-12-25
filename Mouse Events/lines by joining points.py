import cv2
import numpy as np

# img = cv2.imread('lena.jpg', 1)
img = np.zeros((255, 255, 3), np.uint8)  # for a black image using numpy array
points=[]


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        if len(points)>=2:
            cv2.line(img, points[-1], points[-2], (0,255,0), 4)
            cv2.imshow('Image', img)


cv2.imshow('Image', img)
cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
