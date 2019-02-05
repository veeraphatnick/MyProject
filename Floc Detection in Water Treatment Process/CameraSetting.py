import cv2
import numpy as np

cap = cv2.VideoCapture("rtsp://admin:admin@192.168.1.127")
#cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()

    #img = cv2.resize(frame,(1280,840))

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
