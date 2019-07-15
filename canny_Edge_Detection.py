import cv2
import numpy as np


def sketching(image):

    resim=image
    edge=cv2.Canny(resim,50,100)
    return edge


cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge=sketching(gray)
    cv2.imshow('frame',edge)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()