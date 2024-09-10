import sys

from PyQt5 import QtWidgets, QtCore, QtGui
import cv2 as cv

app = QtWidgets.QApplication(sys.argv) # 创建一个应用程序对象
main_window = QtWidgets.QMainWindow() # 创建一个主窗口对象
main_window.setWindowTitle("test image loading") # 设置窗口标题
label  = QtWidgets.QLabel("Hello World", main_window) # 创建一个标签对象
# pixmap = QtGui.QPixmap("./assets/test.jpg") # 创建一个图片对象
img = cv.imread("./assets/test.jpg") # 用opencv读取图片
img = cv.cvtColor(img, cv.COLOR_BGR2RGB) # 将图片从BGR格式转换为RGB格式
height, width, channel = img.shape # 获取图片的高度、宽度和通道数
img = QtGui.QImage(img.data, width, height, width * channel, QtGui.QImage.Format_RGB888) # 创建一个QImage对象
pixmap = QtGui.QPixmap(img) # 创建一个QPixmap对象

pix = pixmap.scaled(640, 480) # 缩放图片


label.setAlignment(QtCore.Qt.AlignCenter) # 设置标签的对齐方式
label.setStyleSheet("color: black; background-color: green;") # 设置标签的样式
label.setPixmap(pix) # 设置标签的图片

font = QtGui.QFont() # 创建一个字体对象
font.setBold(True) # 设置字体为粗体
font.setPointSizeF(32) # 设置字体大小
label.setFont(font) # 设置标签的字体

main_window.setCentralWidget(label) # 设置主窗口的中心部件

main_window.setMinimumSize(1080, 720) # 设置主窗口的最小尺寸
main_window.show() # 显示主窗口
app.exec_() # 进入消息循环
