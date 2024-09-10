import sys 

from PyQt5 import QtWidgets, QtGui, QtCore

class MWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Status Bar')
        self.resize(300, 200)

        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('show')
        file.addAction('hide')
        file.triggered.connect(self.processTrigger)

        self.setCentralWidget(QtWidgets.QTextEdit())

        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)


    def processTrigger(self, action):
        if action.text() == 'show':
            self.statusBar.showMessage(f'{action.text()} is clicked', 2000)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main_win = MWindow()
    main_win.show()
    app.exec_()