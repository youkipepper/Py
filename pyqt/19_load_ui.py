import sys 

from PyQt5 import QtWidgets, QtGui, QtCore, uic, QtMultimedia

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = uic.loadUi("./mini_system.ui")

    window.show()
    app.exec_()