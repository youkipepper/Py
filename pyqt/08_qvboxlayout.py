import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300, 300)

        self.setWindowTitle('Vertical Layout')

        layout = QVBoxLayout()

        btn1 = QPushButton('Button 1')
        btn2 = QPushButton('Button 2')
        btn3 = QPushButton('Button 3')

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    w.show()
    app.exec_()