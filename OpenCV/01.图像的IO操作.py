
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1. 读取图像
img = cv.imread("./test.jpg")

# 2. 显示图像
# 2.1 opencv
# cv.imshow("test",img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# 2.2 matplotlib
if len(img.shape) == 2 or img.shape[2] == 1:
    plt.imshow(img, cmap=plt.cm.gray)
else:
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.show()

# 3. 图像保存
cv.imwrite("./storage.jpg", img)
