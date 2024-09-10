import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    
    w.setWindowTitle('Push Button')

    btn = QPushButton('Click me')

    btn.setParent(w)

    w.show()

    app.exec_()