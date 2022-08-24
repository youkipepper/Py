import cv2 as cv

img = cv.imread("/Users/youkipepper/Desktop/Py/opentest/test.jpg")
cv.imshow("Hello, Python OpenCV!", img)

cv.waitKey(0)
cv.destroyAllWindows()
