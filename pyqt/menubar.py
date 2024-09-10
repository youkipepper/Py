import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        
        # Application menu (for macOS)
        appMenu = menubar.addMenu('&Application')

        # File menu (added to application menu)
        fileMenu = appMenu.addMenu('&File')
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q') 
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitApp)
        fileMenu.addAction(exitAction)

        # Edit menu
        editMenu = menubar.addMenu('&Edit')
        editAction = QAction('&Edit', self)
        editAction.setStatusTip('Edit')
        editAction.triggered.connect(self.edit)
        editMenu.addAction(editAction)

        # View menu
        viewMenu = menubar.addMenu('&View')
        viewAction = QAction('&View', self)
        viewAction.setStatusTip('View')
        viewAction.triggered.connect(self.view)
        viewMenu.addAction(viewAction)

        # Tools menu
        toolsMenu = menubar.addMenu('&Tools')
        toolsAction = QAction('&Tools', self)
        toolsAction.setStatusTip('Tools')
        toolsAction.triggered.connect(self.tools)
        toolsMenu.addAction(toolsAction)

        # Help menu
        helpMenu = menubar.addMenu('&Help')
        helpAction = QAction('&Help', self)
        helpAction.setStatusTip('Help')
        helpAction.triggered.connect(self.help)
        helpMenu.addAction(helpAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menu Example')
        self.show()

    def exitApp(self):
        print("Exit clicked")

    def edit(self):
        print("Edit clicked")

    def view(self):
        print("View clicked")

    def tools(self):
        print("Tools clicked")

    def help(self):
        print("Help clicked")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
