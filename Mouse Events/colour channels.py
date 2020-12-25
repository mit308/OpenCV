import cv2
import numpy as np

img = cv2.imread('lena.jpg', 1)
#img = np.zeros((255, 255, 3), np.uint8)  # for a black image using numpy array
points=[]


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.imshow('Image', img)
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        colorImage=np.zeros((512, 512, 3), np.uint8)

        colorImage[:] = [blue, green, red]
        cv2.imshow("Color", colorImage)


cv2.imshow('Image', img)
cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
