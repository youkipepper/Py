import cv2 as cv
import numpy as np

img = cv.imread("/Users/youkipepper/Desktop/Py/OpenCV/test.jpg")
cv.imshow("Hello, Python OpenCV!", img)

cv.waitKey(0)
cv.destroyAllWindows()
