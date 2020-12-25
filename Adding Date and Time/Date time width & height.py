import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# cap.set(3, 320)
# cap.set(4, 280)

# print(cap.get(3))
# print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()

    if (ret == True):

        font = cv2.FONT_HERSHEY_COMPLEX
        textv = str(cap.get(3)) + 'X' + str(cap.get(4))
        frame = cv2.putText(frame, textv, (3, 30), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
        date1 = str(datetime.datetime.now())
        frame = cv2.putText(frame, date1, (3, 80), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('Capture', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
