import cv2
import numpy as np

img=cv2.imread("messi5.jpg")
img2=cv2.imread("opencv-logo-white.png")

# Resizing the two images to add or merge

img=cv2.resize(img, (512, 512))
img2=cv2.resize(img2, (512, 512))

merge=cv2.add(img, img2) # Merging two images

cv2.imshow('Messi', merge)
cv2.waitKey(0)
cv2.destroyAllWindows()