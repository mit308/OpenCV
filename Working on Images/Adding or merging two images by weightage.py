import cv2
import numpy as np

img=cv2.imread("messi5.jpg")
img2=cv2.imread("opencv-logo-white.png")

#ball=img[280:340, 330:390]
#img[273:333, 100:160] = ball

img=cv2.resize(img, (512, 512))
img2=cv2.resize(img2, (512, 512))

merge=cv2.addWeighted(img, 0.5, img2, 0.5, 0) # ratio can be changed by changing value for alpha, beta & gamma
cv2.imshow('Messi', merge)
cv2.waitKey(0)
cv2.destroyAllWindows()