import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    
    w.setWindowTitle('qlabel')

    label = QLabel('Hello World', w)
    label.setGeometry(20, 20, 30, 30)

    w.show()

    app.exec_()