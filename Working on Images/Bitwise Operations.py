import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255,), -1)
img2 = cv2.imread('image_1.png')

bitAnd=cv2.bitwise_and(img2, img1) 
# bitOr=cv2.bitwise_or(img2, img1)
# bitXOr = cv2.bitwise_xor(img2, img1)
# bitNot = cv2.bitwise_not(img1)

cv2.imshow('Image2', img2)
cv2.imshow('Image', img1)
cv2.imshow("bitAnd", bitAnd)
# cv2.imshow("bitOr", bitOr)
# cv2.imshow("bitXOr", bitXOr)
# cv2.imshow("bitNot", bitNot)  # can be performed on any one image

cv2.waitKey(0)
cv2.destroyAllWindows()
