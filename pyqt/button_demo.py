import sys

from PyQt5 import QtWidgets, QtCore, QtGui
import cv2 as cv

def click_btn1():
    print("Button One Clicked")
    txt_label.setText("I am Button One")

def click_btn2():
    print("Button Two Clicked")
    txt_label.setText("I am Button Two")

def click_btn3():
    print("Button Three Clicked")
    txt_label.setText("I am Button Three")

app = QtWidgets.QApplication(sys.argv)
main_win = QtWidgets.QMainWindow() 
main_win.setWindowTitle("test vbox") 

btn1 = QtWidgets.QPushButton("Button One")
btn2 = QtWidgets.QPushButton("Button Two")
btn3 = QtWidgets.QPushButton("Button Three")
btn1.clicked.connect(click_btn1)
btn2.clicked.connect(click_btn2)
btn3.clicked.connect(click_btn3)

txt_label = QtWidgets.QLabel()
txt_label.setText("botton demo")
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
image_label.setStyleSheet("color: green; background-color: pink;") # 设置标签的样式

btnPanel = QtWidgets.QWidget()
hboxlayout = QtWidgets.QHBoxLayout()
hboxlayout.addStretch(1)
hboxlayout.addWidget(btn1)
hboxlayout.addWidget(btn2)
hboxlayout.addWidget(btn3)
btnPanel.setLayout(hboxlayout)

panel = QtWidgets.QWidget()
vboxlayout = QtWidgets.QVBoxLayout()
vboxlayout.addWidget(txt_label)
vboxlayout.addWidget(image_label)
vboxlayout.addWidget(btnPanel)
panel.setLayout(vboxlayout)

main_win.setCentralWidget(panel) # 设置主窗口的中心部件

main_win.setMinimumSize(1080, 720) # 设置主窗口的最小尺寸
main_win.show() # 显示主窗口
app.exec_() # 进入消息循环
