import sys 

from PyQt5 import QtWidgets, QtCore, QtGui

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    w.setWindowTitle('PyQt5 Demo')

    w.show()

    app.exec_()