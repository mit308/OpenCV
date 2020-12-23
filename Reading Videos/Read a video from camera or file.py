import cv2

cap= cv2.VideoCapture(0) # path for a file

while(cap.isOpened()):
    isTrue, frame=cap.read()
    cv2.imshow('frame', frame)

    if(cv2.waitKey(1) & 0xFF == ord('s')):
        break

cap.release()
cv2.destroyAllWindows()