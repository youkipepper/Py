import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1. 读取图像
img = cv.imread("test.jpg")

# 2. 显示图像
# 2.1 opencv
# cv.imshow("test",img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# 2.2 matplotlib
plt.imshow(img, cmap=plt.cm.gray)
plt.show()

# 3. 图像保存
cv.imwrite("./storage.jpg", img)
