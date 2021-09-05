import cv2
import numpy as np

image=input("Enter the image")
img = cv2.imread(image)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 150, apertureSize=3)
cv2.imshow('edges', edges)
cv2.imshow("Image", img)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    # plotting the point 1 by creating a formula
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    # plotting the point 2 by creating a formula
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyWindow("image")
