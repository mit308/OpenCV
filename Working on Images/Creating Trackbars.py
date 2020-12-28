import cv2
import numpy as np


def nothing(x):
    print(x)


# creating a black image

img = np.zeros((512, 512, 3), np.uint8)
# creating a blank window

cv2.namedWindow('Image')

# creating trackbars
cv2.createTrackbar('Blue', 'Image', 0, 255, nothing)
cv2.createTrackbar('Green', 'Image', 0, 255, nothing)
cv2.createTrackbar('Red', 'Image', 0, 255, nothing)
cv2.createTrackbar('Switch', 'Image', 0, 1, nothing)

while 1:
    cv2.imshow('Image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv2.getTrackbarPos('Blue', 'Image')
    g = cv2.getTrackbarPos('Green', 'Image')
    r = cv2.getTrackbarPos('Red', 'Image')
    s = cv2.getTrackbarPos('Switch', 'Image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()
