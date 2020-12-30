import cv2

image = cv2.imread('data/sudoku.png', 0)

th1 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)
th2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 7)

cv2.imshow('image', image)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)

cv2.waitKey(0)
cv2.destroyAllWindows()
