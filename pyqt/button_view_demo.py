import sys 

from PyQt5 import QtWidgets, QtCore, QtGui
import cv2 as cv

class ButtonPanel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        select_btn = QtWidgets.QPushButton("Select image ...")
        self.path_label = QtWidgets.QLabel("")
        self.path_label.setText('No image selected.')
        self.path_label.setAlignment(QtCore.Qt.AlignCenter)
        self.path_label.setStyleSheet("color: green; background-color: black;")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSizeF(18)
        self.path_label.setFont(font)

        self.image_label = QtWidgets.QLabel()
        src = cv.imread("./assets/test.jpg")
        image = cv.cvtColor(src, cv.COLOR_BGR2RGB)
        h, w, c = image.shape
        img = QtGui.QImage(image.data, w, h, 3 * w, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(img)
        pix = pixmap.scaled(QtCore.QSize(640, 640), QtCore.Qt.IgnoreAspectRatio)
        self.image_label.setPixmap(pix)

        btnPanel = QtWidgets.QGroupBox('Choose image')
        hboxlayout = QtWidgets.QHBoxLayout()
        hboxlayout.addWidget(self.path_label)
        hboxlayout.addWidget(select_btn)
        hboxlayout.addStretch(1)
        btnPanel.setLayout(hboxlayout)

        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setStyleSheet("color: green; background-color: pink;")

        vboxlayout = QtWidgets.QVBoxLayout()
        vboxlayout.addWidget(self.image_label)
        vboxlayout.addWidget(btnPanel)
        self.setLayout(vboxlayout)

    def on_select_image(self):
        self.path_label.setText('Image selected.')
        print('Image selected.')

app = QtWidgets.QApplication(sys.argv)
main_win = QtWidgets.QMainWindow()
main_win.setWindowTitle("image viewer")
myPanel = ButtonPanel()
main_win.setCentralWidget(myPanel)

main_win.setMinimumSize(1080, 720)
main_win.show()
app.exec_()


