import cv2 as cv
import numpy as np

img = cv.imread("./test.jpg")
cv.imshow("Hello, Python OpenCV!", img)

cv.waitKey(0)
cv.destroyAllWindows()
