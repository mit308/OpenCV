import cv2

img = cv2.imread('lena.jpg', 1)

img = cv2.line(img, (0, 50), (50, 200), (255, 0, 0), 10)
img = cv2.arrowedLine(img, (200, 0), (400, 200), (0, 0, 0), 10)
img = cv2.rectangle(img, (250, 0), (0, 250), (0, 0, 255), -1)  # line wt. -1 for filled
img=cv2.circle(img, (200,400), (50), (0,255,0), -1)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
