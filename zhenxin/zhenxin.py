import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cap = cv.VideoCapture("./59_1667472917.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv.Canny(frame, 100, 200)
    if ret == True:
        cv.imshow('frame', frame)
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()