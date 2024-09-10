import sys

from PyQt5 import QtWidgets, QtCore, QtGui
import cv2 as cv

app = QtWidgets.QApplication(sys.argv)
main_win = QtWidgets.QMainWindow() 
main_win.setWindowTitle("test vbox") 

txt_label = QtWidgets.QLabel()
txt_label.setText("QVBoxLayout")
txt_label.setAlignment(QtCore.Qt.AlignCenter)
txt_label.setStyleSheet("color: green; background-color: black;")
font = QtGui.QFont()
font.setBold(True)
font.setPointSizeF(32)
txt_label.setFont(font)

image_label  = QtWidgets.QLabel() 
# pixmap = QtGui.QPixmap("./assets/test.jpg")
src = cv.imread("./assets/test.jpg") 
image = cv.cvtColor(src, cv.COLOR_BGR2RGB)
h, w, c = image.shape 
img = QtGui.QImage(image.data, w, h, w * c, QtGui.QImage.Format_RGB888) 
pixmap = QtGui.QPixmap(img)
pix = pixmap.scaled(QtCore.QSize(640, 640), QtCore.Qt.KeepAspectRatio)
image_label.setPixmap(pix) 

image_label.setAlignment(QtCore.Qt.AlignCenter) # 设置标签的对齐方式
image_label.setStyleSheet("color: black; background-color: pink;") # 设置标签的样式

panel = QtWidgets.QWidget()
vboxlayout = QtWidgets.QVBoxLayout()
vboxlayout.addWidget(txt_label)
vboxlayout.addWidget(image_label)
panel.setLayout(vboxlayout)

main_win.setCentralWidget(panel) # 设置主窗口的中心部件

main_win.setMinimumSize(1080, 720) # 设置主窗口的最小尺寸
main_win.show() # 显示主窗口
app.exec_() # 进入消息循环
