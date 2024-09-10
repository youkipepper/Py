import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QScrollArea, QFileDialog, QPushButton

import sys 
import os

from PyQt5 import QtWidgets, QtCore, QtGui
import cv2 as cv

class ButtonPanel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_files = []
        self.img_idx = -1

        select_btn = QtWidgets.QPushButton("Select image ...")

        back_pix = QtWidgets.QStyle.SP_ArrowBack
        back_icon = self.style().standardIcon(back_pix)
        back_btn = QtWidgets.QPushButton(back_icon, "")
        back_btn.setToolTip("Back")
        back_btn.setMinimumHeight(50)

        forward_pix = QtWidgets.QStyle.SP_ArrowForward
        forward_icon = self.style().standardIcon(forward_pix)
        forward_btn = QtWidgets.QPushButton(forward_icon, "")
        forward_btn.setToolTip("Forward")
        forward_btn.setMinimumHeight(50)

        bfPanel = QtWidgets.QWidget()
        bf_layout = QtWidgets.QHBoxLayout()
        bf_layout.addWidget(back_btn)
        bf_layout.addWidget(forward_btn)
        bfPanel.setLayout(bf_layout)

        self.path_label = QtWidgets.QLabel("")
        self.path_label.setText('No image selected.')
        self.path_label.setAlignment(QtCore.Qt.AlignCenter)
        self.path_label.setStyleSheet("color: green; background-color: black;")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSizeF(18)
        self.path_label.setFont(font)

        self.image_label = QtWidgets.QLabel()

        # src = cv.imread("test.jpg")
        # image = cv.cvtColor(src, cv.COLOR_BGR2RGB)
        # h, w, c = image.shape
        # img = QtGui.QImage(image.data, w, h, 3 * w, QtGui.QImage.Format_RGB888)
        # pixmap = QtGui.QPixmap(img)
        # pix = pixmap.scaled(QtCore.QSize(640, 640), QtCore.Qt.IgnoreAspectRatio)
        # self.image_label.setPixmap(pix)

        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setStyleSheet("color: green; background-color: pink;")
        pixmap = QtGui.QPixmap(640, 640)
        pixmap.fill(QtGui.QColor("pink"))
        self.image_label.setPixmap(pixmap)

        btnPanel = QtWidgets.QGroupBox('Choose image')
        hboxlayout = QtWidgets.QHBoxLayout()
        hboxlayout.addWidget(self.path_label)
        hboxlayout.addWidget(select_btn)
        hboxlayout.addStretch(1)
        btnPanel.setLayout(hboxlayout)

        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setStyleSheet("color: green; background-color: pink;")

        vboxlayout = QtWidgets.QVBoxLayout()
        vboxlayout.addWidget(btnPanel)
        vboxlayout.addWidget(self.image_label)
        vboxlayout.addWidget(bfPanel)
        vboxlayout.addStretch(1)
        self.setLayout(vboxlayout)

        select_btn.clicked.connect(self.on_select_dir)
        back_btn.clicked.connect(self.on_back_image)
        forward_btn.clicked.connect(self.on_forward_image)
    
    def on_select_dir(self):
        current_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select directory", ".")
        files = os.listdir(current_dir)
        self.image_files.clear()
        self.path_label.setText(current_dir)
        for file in files:
            print(file)
            self.image_files.append(os.path.join(current_dir, file))

        self.img_idx = 0

        pixmap = QtGui.QPixmap(self.image_files[0])
        pix = pixmap.scaled(QtCore.QSize(640, 640), QtCore.Qt.IgnoreAspectRatio)
        self.image_label.setPixmap(pix)


    def on_select_image(self):
        file_info = QtWidgets.QFileDialog.getOpenFileName(self, "Select image", ".", "Image files (*.jpg *.png)")
        file_name = file_info[0]
        if file_name != "":
            self.path_label.setText(file_name)
            pix_map = QtGui.QPixmap(file_name)
            pix = pix_map.scaled(QtCore.QSize(640, 640), QtCore.Qt.IgnoreAspectRatio)
            self.image_label.setPixmap(pix)

    def on_back_image(self):
        if self.img_idx == -1:
            return
        self.img_idx -= 1
        if self.img_idx >= 0:
            pixmap = QtGui.QPixmap(self.image_files[self.img_idx])
            pix = pixmap.scaled(QtCore.QSize(640, 640), QtCore.Qt.IgnoreAspectRatio)
            self.image_label.setPixmap(pix)
        else:
            self.img_idx = 0

    def on_forward_image(self):
        if self.img_idx == -1:
            return
        self.img_idx += 1
        if len(self.image_files) > self.img_idx:
            pixmap = QtGui.QPixmap(self.image_files[self.img_idx])
            pix = pixmap.scaled(QtCore.QSize(640, 640), QtCore.Qt.IgnoreAspectRatio)
            self.image_label.setPixmap(pix)
        else:
            self.img_idx = len(self.image_files) - 1

app = QtWidgets.QApplication(sys.argv)
main_win = QtWidgets.QMainWindow()
main_win.setWindowTitle("grid image viewer")
myPanel = ButtonPanel()
main_win.setCentralWidget(myPanel)

main_win.setMinimumSize(1080, 720)
main_win.show()
app.exec_()

