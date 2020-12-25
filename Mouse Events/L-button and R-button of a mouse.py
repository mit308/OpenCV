import cv2
import numpy as np

img = cv2.imread('lena.jpg', 1)


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

	# to print co-ordinates on the image
 
        print(x, ', ', y)
        strXY = str(x) + ', ' + str(y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, strXY, (x, y), font, 0.5, (0, 0, 0), 2)
        cv2.imshow('Image', img)
    if event == cv2.EVENT_RBUTTONDOWN:

	# to print the colour channel

        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        strColor = str(blue) + ', ' + str(green) + ', ' + str(red)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, strColor, (x, y), font, 0.5, (0, 0, 0), 2)
        cv2.imshow('Image', img)


cv2.imshow('Image', img)

cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
