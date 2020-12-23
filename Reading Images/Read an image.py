import cv2

img=cv2.imread('lena.jpg', 1)
print(img) # shows image in matrix form
cv2.imshow('Image', img)

k=cv2.waitKey(0)
if(k== ord('q')):
    cv2.imwrite('copy_lena.jpg', img)
    cv2.destroyAllWindows()

else:
    cv2.destroyAllWindows()
